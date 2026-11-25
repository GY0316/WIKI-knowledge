---
title: Nginx最小配置骨架
type: concept
tags: [Nginx, 配置, 模板, 反向代理, 落地, TLS]
sources:
  - 抖音-Nginx控制入口层（2026-11）
  - 抖音-Nginx为什么快（2026-11）
---

# Nginx 最小配置骨架

## 一句话定义

把 [[Nginx的需求与实现原理]] 里的 R1–R11 压成一套**可直接改、改完就能验**的配置骨架。它给的是结构与顺序，不是参数基准——所有数字都要按你的机器、后端和流量重算。

## 文件布局

```
/etc/nginx/
├── nginx.conf              # 全局：worker、超时、日志、gzip、缓存区、include
├── conf.d/
│   └── app.conf            # 站点：upstream、TLS、路径分流、缓存、WebSocket
└── certs/
    ├── app.crt             # 证书只在入口一份（R6）
    └── app.key
```

## 一、主配置 nginx.conf

```nginx
user  nginx;
worker_processes auto;                 # R3：一核一 worker
worker_rlimit_nofile 65535;            # 必须 ≥ worker_connections × 2
error_log /var/log/nginx/error.log warn;
pid /run/nginx.pid;

events {
    worker_connections 10240;          # R2：单 worker 并发上限
    multi_accept on;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;
    server_tokens off;                 # 不对外暴露版本号

    log_format main '$remote_addr - [$time_local] "$request" $status '
                    '$body_bytes_sent rt=$request_time '
                    'uct=$upstream_connect_time uht=$upstream_header_time '
                    'urt=$upstream_response_time us=$upstream_addr '
                    'cs=$upstream_cache_status';
    access_log /var/log/nginx/access.log main;

    sendfile on;
    tcp_nopush on;
    keepalive_timeout 65s;

    # R1：入口对客户端要"有限但宽松"——慢连接到点就断
    client_header_timeout 10s;
    client_body_timeout   12s;
    send_timeout          10s;
    client_max_body_size  10m;
    client_header_buffer_size 4k;
    large_client_header_buffers 4 8k;

    gzip on;
    gzip_comp_level 5;
    gzip_min_length 1024;
    gzip_types text/plain text/css application/json application/javascript
               text/xml application/xml image/svg+xml;
    gzip_vary on;

    # WebSocket 升级用的连接头映射
    map $http_upgrade $connection_upgrade {
        default upgrade;
        ''      close;
    }

    # R10：缓存区（目录需存在且 nginx 用户可写）
    proxy_cache_path /var/cache/nginx/api levels=1:2 keys_zone=api_cache:10m
                     max_size=1g inactive=60m use_temp_path=off;

    include /etc/nginx/conf.d/*.conf;
}
```

## 二、站点配置 conf.d/app.conf

```nginx
upstream app_backend {
    least_conn;                                        # R8
    server 127.0.0.1:8080 max_fails=3 fail_timeout=10s;
    server 127.0.0.1:8081 max_fails=3 fail_timeout=10s;
    keepalive 32;                                      # 复用到后端的连接
}

server {
    listen 80;
    server_name app.example.com;
    return 301 https://$host$request_uri;              # 明文一律跳转
}

server {
    listen 443 ssl;
    http2 on;                                          # nginx 1.25.1+ 写法
    server_name app.example.com;

    # R6：证书只在这里配一次
    ssl_certificate     /etc/nginx/certs/app.crt;
    ssl_certificate_key /etc/nginx/certs/app.key;
    ssl_protocols       TLSv1.2 TLSv1.3;
    ssl_session_cache   shared:SSL:10m;
    ssl_session_timeout 1d;
    ssl_prefer_server_ciphers off;

    root /var/www/app;
    index index.html;

    # R7：静态直出，不占应用进程
    location ^~ /assets/ {
        expires 30d;
        add_header Cache-Control "public, immutable";
        access_log off;
        try_files $uri =404;
    }

    location = /favicon.ico { access_log off; log_not_found off; }

    # R5 + R9：业务接口，收齐请求体后才转发
    location /api/ {
        proxy_pass http://app_backend/;                # 结尾斜杠 → 剥掉 /api/

        proxy_http_version 1.1;
        proxy_set_header Host              $host;
        proxy_set_header X-Real-IP         $remote_addr;
        proxy_set_header X-Forwarded-For   $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Connection        "";         # 用 upstream keepalive 时必须清空

        proxy_request_buffering on;
        proxy_buffering on;
        proxy_buffer_size 8k;
        proxy_buffers 8 8k;

        # 内层先失败：后端超时必须短于入口对客户端的超时
        proxy_connect_timeout 5s;
        proxy_send_timeout    30s;
        proxy_read_timeout    30s;

        proxy_next_upstream error timeout http_502 http_503;
    }

    # R10：可缓存的只读接口
    location /api/report/ {
        proxy_pass http://app_backend/report/;
        proxy_cache api_cache;
        proxy_cache_key "$scheme$host$request_uri";
        proxy_cache_valid 200 5m;
        proxy_cache_use_stale error timeout updating http_500 http_502 http_503;
        add_header X-Cache-Status $upstream_cache_status;

        proxy_http_version 1.1;
        proxy_set_header Host            $host;
        proxy_set_header X-Real-IP       $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Connection      "";
    }

    # 长连接：WebSocket / SSE
    location /ws/ {
        proxy_pass http://app_backend/ws/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade    $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
        proxy_set_header Host       $host;
        proxy_read_timeout  3600s;         # 默认 60s 会掐断长连接
        proxy_buffering off;               # SSE 必须关
        proxy_request_buffering off;
    }

    location / {
        try_files $uri $uri/ /index.html;  # SPA 兜底
    }
}
```

## 三、最容易错的一条：`proxy_pass` 的斜杠

规则只有一句：**`proxy_pass` 带 URI 就替换，不带就原样转发。**

| 配置 | 请求 `/api/users` 实际转发到 |
|---|---|
| `location /api/` + `proxy_pass http://backend;` | `http://backend/api/users`（整条 URI 原样） |
| `location /api/` + `proxy_pass http://backend/;` | `http://backend/users`（`/api/` 被替换成 `/`） |
| `location /api/` + `proxy_pass http://backend/v1/;` | `http://backend/v1/users` |

**实践约定**：`location` 与 `proxy_pass` 保持同形态——要剥前缀就两边都带斜杠，要保留就两边都不带。混着写不会报错，但会静默转错地址，是这一层最高频的事故。

同理，`alias` 必须与 `location` 的斜杠形态严格一致，`root` 则总是拼接完整 URI。

## 四、校验与生效

```bash
nginx -t                    # 语法 + include 全部校验，必须先过
nginx -s reload             # 平滑重载：新 worker 接班，旧 worker 排空退出
# 或：systemctl reload nginx
```

reload 后确认旧 worker 真的退出了（排空耗时取决于长连接）：

```bash
ps -o pid,lstart,cmd -C nginx          # 旧 worker 的启动时间应停止更新
ss -lntp | grep nginx                  # 确认监听端口与进程数
```

**不要用 `nginx -s stop` 代替 reload**：stop 是立即杀，进行中的下载和长连接全部中断。

## 五、验收清单（对应 R1–R11）

| 需求 | 怎么验 |
|---|---|
| R1 慢连接不耗尽容量 | 用 `slowhttptest` 或 `nc` 造慢连接，再压新请求，看是否仍能进入 |
| R2 万级并发内存可控 | `ss -tan state established \| wc -l` 与 RSS 一起看 |
| R3 用满多核 | `nproc` 与 `ps -C nginx` 的 worker 数对齐 |
| R4 改配置不停服 | 大文件下载中执行 reload，校验字节完整 |
| R5 只暴露一个入口 | 从公网扫后端端口，应当不可达 |
| R6 证书集中 | `openssl s_client -connect app.example.com:443` 看证书链 |
| R7 静态不占应用 | 静态请求的 access log 中 `us=-`（没有上游地址） |
| R8 多实例分发 | 停掉一个 upstream，观察请求是否切走且无 5xx 堆积 |
| R9 慢请求不打到后端 | 慢速上传大请求体，观察后端 worker 占用是否被拖住 |
| R10 缓存生效 | 连续两次请求，看 `X-Cache-Status` 从 MISS 变 HIT |
| R11 入口可观测 | 用 log 里的 `uct/uht/urt` 三段耗时把 504 定位到连接、首字节还是响应体 |

## 六、常见故障对照

| 现象 | 最可能的位置 |
|---|---|
| 502 | 后端进程没起、端口写错、upstream 全被 `max_fails` 摘掉 |
| 504 | `proxy_read_timeout` 短于后端实际耗时，或后端阻塞 |
| 499 | 客户端先断开（入口记录，通常说明前端超时更短） |
| 413 | `client_max_body_size` 太小 |
| 400 / 431 | 请求头过大，调 `large_client_header_buffers` |
| 静态 404 | `root` / `alias` 与 `location` 斜杠不一致 |
| 长连接频繁断 | `proxy_read_timeout` 仍是默认 60s，或上游有空闲超时 |

## 七、三件不要做的事

1. **不要在 `if` 里写 `proxy_pass`**：`if` 在 location 内是"指令上下文陷阱"，行为与直觉不符。
2. **不要让 `worker_connections × worker_processes` 超过 `worker_rlimit_nofile`**：多出的连接会直接失败。
3. **不要在入口做业务鉴权**：入口只做粗粒度限流与路由；鉴权放网关或后端，否则每加一个服务都要改一次入口配置。

## 相关概念

- [[Nginx的需求与实现原理]] — 这份骨架服务的需求清单与优先级
- [[反向代理与统一入口层]] — 这一层在架构中的位置与四类入口层分工
- [[Nginx]] — 实体页：并发模型与边界
- [[通讯协议对比与选型]] — 长连接、空闲超时的协议侧约束

## 出现的来源

- [[抖音-Nginx控制入口层（2026-11）]] — 场景与判断依据
- [[抖音-Nginx为什么快（2026-11）]] — worker、缓冲转发与 reload 的机制依据

> 本页的配置结构由两条视频的需求推导而来，具体指令与参数属工程实践补充，未经生产验证；上线前必须按实际后端与流量重算，并做压测。
