---
title: 示例-Attention Is All You Need
type: source
sources:
  - raw/02-papers/示例-attention-is-all-you-need.md
date: 2026-11-12
tags: [示例, Transformer]
---

# 示例-Attention Is All You Need

> 示例来源摘要页。演示 ingest 后 `wiki/sources/` 的样子。

## 核心观点

- 序列建模无需 RNN 或 CNN，仅凭[[注意力机制]]即可，这就是 Transformer 架构。

## 关键内容摘要

自注意力让序列中每个位置直接关注所有其他位置，解决了长距离依赖和并行化问题。多头注意力在不同子空间并行学习多种关系。因为去掉了循环结构，需要位置编码注入词序信息。该架构是 GPT、BERT 等大模型的基础。

## 涉及的概念与实体

- 概念：[[注意力机制]]
- 实体：[[Google Brain]]

## 与已有知识的联系 / 矛盾

- 这是本库第一份资料，暂无可对照的已有知识。
