# 示例原始资料：Attention Is All You Need

> 这是一份**示例原始资料**，用来演示 ingest 流程。你可以在熟悉流程后删除它，或连同它生成的 wiki 页面一起删掉。
> 真实使用时，这里放你剪藏的文章、论文转的 Markdown 等。

Vaswani 等人在 2017 年提出 Transformer 架构，核心主张是：序列建模不必依赖循环（RNN）或卷积（CNN），仅用注意力机制（attention）就够了。

关键点：
- 自注意力（self-attention）让序列中每个位置直接关注所有其他位置，解决了 RNN 的长距离依赖和无法并行的问题。
- 多头注意力（multi-head attention）让模型在不同表示子空间里并行学习多种关系。
- 由于没有循环结构，需要位置编码（positional encoding）来注入词序信息。

这篇论文是后续 GPT、BERT 等大模型的架构基础，由 Google Brain 团队主导。
