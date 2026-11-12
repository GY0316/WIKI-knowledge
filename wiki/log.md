---
title: 操作日志
type: log
---

# 操作日志

> 只追加、不修改的时间线。记录每次 ingest / query / lint。
> 固定前缀便于 grep：`grep "^## \[" log.md | tail -5` 查看最近 5 条。
> 格式：`## [YYYY-MM-DD] 操作类型 | 标题`

## [2026-11-12] init | 知识库初始化

建立三层结构（raw / wiki / schema），配置 ingest、query、lint 三个工作流。等待第一份资料导入。

## [2026-11-12] ingest | 示例-Attention Is All You Need

示例导入，演示完整链路。生成 1 篇来源摘要（[[示例-Attention Is All You Need]]）、1 个概念页（[[注意力机制]]）、1 个实体页（[[Google Brain]]），更新 index。熟悉流程后可删除所有「示例-」前缀的文件。
