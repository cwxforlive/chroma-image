import chromadb

#创建客户端
chroma_client = chromadb.Client()

# 创建集合
collection = chroma_client.create_collection(name="my_collection")

# 添加数据
collection.add(
    documents=["Document 1", "Document 2"],
    ids=["id1", "id2"]
)

# 查询相似文档
results = collection.query(
    query_texts=["Document"],
    n_results=2
)
print(results)
