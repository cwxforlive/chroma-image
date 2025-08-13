<p align="center">
  <a href="https://trychroma.com"><img src="https://user-images.githubusercontent.com/891664/227103090-6624bf7d-9524-4e05-9d2c-c28d5d451481.png" alt="Chroma logo"></a>
</p>

<p align="center">
    <b>Chroma - the open-source embedding database</b>. <br />
    The fastest way to build Python or JavaScript LLM apps with memory!
</p>

<p align="center">
  <a href="https://discord.gg/MMeYNTmh3x" target="_blank">
      <img src="https://img.shields.io/discord/1073293645303795742?cacheSeconds=3600" alt="Discord">
  </a> |
  <a href="https://github.com/chroma-core/chroma/blob/master/LICENSE" target="_blank">
      <img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License">
  </a> |
  <a href="https://docs.trychroma.com/" target="_blank">
      Docs
  </a> |
  <a href="https://www.trychroma.com/" target="_blank">
      Homepage
  </a>
</p>

```bash
pip install chromadb # python client
# for javascript, npm install chromadb!
# for client-server mode, chroma run --path /chroma_db_path
```

## Chroma Cloud

Our hosted service, Chroma Cloud, powers serverless vector and full-text search. It's extremely fast, cost-effective, scalable and painless. Create a DB and try it out in under 30 seconds with $5 of free credits.

[Get started with Chroma Cloud](https://trychroma.com/signup)

## API

The core API is only 4 functions (run our [💡 Google Colab](https://colab.research.google.com/drive/1QEzFyqnoFxq7LUGyP1vzR4iLt9PpCDXv?usp=sharing)):

```python
import chromadb
# setup Chroma in-memory, for easy prototyping. Can add persistence easily!
client = chromadb.Client()

# Create collection. get_collection, get_or_create_collection, delete_collection also available!
collection = client.create_collection("all-my-documents")

# Add docs to the collection. Can also update and delete. Row-based API coming soon!
collection.add(
    documents=["This is document1", "This is document2"], # we handle tokenization, embedding, and indexing automatically. You can skip that and add your own embeddings as well
    metadatas=[{"source": "notion"}, {"source": "google-docs"}], # filter on these!
    ids=["doc1", "doc2"], # unique for each doc
)

# Query/search 2 most similar results. You can also .get by id
results = collection.query(
    query_texts=["This is a query document"],
    n_results=2,
    # where={"metadata_field": "is_equal_to_this"}, # optional filter
    # where_document={"$contains":"search_string"}  # optional filter
)
```

Learn about all features on our [Docs](https://docs.trychroma.com)

## Features
- __Simple__: Fully-typed, fully-tested, fully-documented == happiness
- __Integrations__: [`🦜️🔗 LangChain`](https://blog.langchain.dev/langchain-chroma/) (python and js), [`🦙 LlamaIndex`](https://twitter.com/atroyn/status/1628557389762007040) and more soon
- __Dev, Test, Prod__: the same API that runs in your python notebook, scales to your cluster
- __Feature-rich__: Queries, filtering, regex and more
- __Free & Open Source__: Apache 2.0 Licensed

## Use case: ChatGPT for ______

例如，“聊天数据”用例：
1. 将文档添加到数据库。您可以传入自己的嵌入、嵌入函数，或让 Chroma 为您嵌入。
2. 使用自然语言查询相关文档。
3. 将文档编写到 LLM（例如“GPT4”）的上下文窗口中，以进行进一步的摘要或分析。

## Embeddings?

什么是Embeddings？

- [阅读 OpenAI 指南](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings)
- __字面意思__：嵌入会将图像/文本/音频转化为数字列表。🖼️ 或 📄 => `[1.2, 2.1, ....]`。此过程使文档对机器学习模型“可理解”。
- __类比__：嵌入表示文档的本质。这使得具有相同本质的文档和查询彼此“接近”，从而易于查找。
- __技术__：嵌入是文档在深度神经网络某一层的潜在空间位置。对于专门训练嵌入数据的模型，这是最后一层。
- __小例子__：如果您在照片中搜索“旧金山著名的桥梁”。通过嵌入此查询并将其与您的照片及其元数据的嵌入进行比较，它应该会返回金门大桥的照片。

嵌入数据库（也称为**矢量数据库**）存储嵌入，并允许您按最近邻进行搜索，而不是像传统数据库那样按子字符串进行搜索。默认情况下，Chroma 使用 [Sentence Transformers](https://docs.trychroma.com/guides/embeddings#default:-all-minilm-l6-v2) 为您进行嵌入，但您也可以使用 OpenAI 嵌入、Cohere（多语言）嵌入或您自己的嵌入。
## Get involved

Chroma 项目正在快速发展。我们欢迎您提交 PR，并提出改进项目的建议。
- [加入 Discord 讨论](https://discord.gg/MMeYNTmh3x) - `#contributing` 频道
- [查看 🛣️ 路线图并贡献您的想法](https://docs.trychroma.com/roadmap)
- [提交 Issue 并发起 PR](https://github.com/chroma-core/chroma/issues) - [`Good first issue tag`](https://github.com/chroma-core/chroma/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
- [阅读我们的贡献指南](https://docs.trychroma.com/contributing)
Chroma xiàngmù zhèngzài kuàisù fāzhǎn. Wǒmen huānyíng nín tíjiāo PR, bìng tíchū gǎijìn xiàngmù dì jiànyì.
- [Jiārù Discord tǎolùn](https://Discord.Gg/MMeYNTmh3x) - `#contributing`píndào
- [chákàn 🛣️ lùxiàn tú bìng gòngxiàn nín de xiǎngfǎ](https://Docs.Trychroma.Com/roadmap)
- [tíjiāo Issue bìng fāqǐ PR](https://Github.Com/chroma-core/chroma/issues) - [`Good first issue tag`](https://Github.Com/chroma-core/chroma/issues?Q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
- [yuèdú wǒmen de gòngxiàn zhǐnán](https://Docs.Trychroma.Com/contributing)

**Release Cadence**
目前，我们每周一发布 `pypi` 和 `npm` 软件包的新标签版本。热修复补丁会在一周内随时发布。

## License

[Apache 2.0](./LICENSE)
