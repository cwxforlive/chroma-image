Chroma使用指南
1	商品说明
chroma向量数据库存储嵌入，并允许您按最近邻进行搜索，而不是像传统数据库那样按子字符串进行搜索。默认情况下，Chroma 使用 Sentence Transformers 为您进行嵌入，但您也可以使用 OpenAI 嵌入、Cohere（多语言）嵌入或您自己的嵌入。


本商品通过鲲鹏服务器+EulerOS2.0进行安装部署
2	商品购买
您可以在云商店搜索“Chroma”。

其中，地域、规格、推荐配置使用默认，购买方式根据您的需求选择按需/按月/按年，短期使用推荐按需，长期使用推荐按月/按年，确认配置后点击“立即购买”。
3	商品资源配置
商品支持ECS控制台配置，下面对资源配置的方式进行介绍。
3.1	ECS控制台配置
3.1.1	准备工作
在使用ECS控制台配置前，需要您提前配置好安全组规则。
安全组规则的配置如下：
	入方向规则放通端口8000，源地址内必须包含您的客户端ip，否则无法访问
	入方向规则放通CloudShell连接实例使用的端口22，以便在控制台登录调试。
	出方向规则一键放通

3.1.2	创建ECS
前提工作准备好后，选择ECS控制台配置跳转到购买ECS页面，ECS资源的配置如下图所示：
 
 
 
值得注意的是：
	VPC您可以自行创建
	安全组选择3.1.1章节中配置的安全组
	弹性公网IP选择现在购买，推荐选择“按流量计费”，带宽大小可设置为5Mbit/s
	高级配置需要在高级选项支持注入自定义数据，所以登录凭证不能选择“密码”，选择创建后设置
	其余默认或按规则填写即可。


4.1	Chroma使用

4.1.1	Chroma服务端启动
	切换到chroma运行目录
cd /chroma  
	运行python虚拟化环境
source /chroma/chroma-env/bin/activate
	启动chroma server
chroma run --path /data/chroma_db --host 0.0.0.0 --port
 
4.1.2	Chroma客户端使用示例
	复制一个运行窗口
	切换到chroma运行目录
cd /chroma
	运行python虚拟化环境
source /chroma/chroma-env/bin/activate
	编辑一个python客户端示例test.py

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
	执行python示例文件
python test.py 结果如下:
 

4.2	参考文档
	chroma参考文档
