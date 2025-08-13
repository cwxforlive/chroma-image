<p align="center">
  <h1 align="center">Flink Stream Data Analysis Tool</h1>
  <p align="center">
    <a href="README_ZH.md"><strong>简体中文</strong></a> | <strong>English</strong>
  </p>
</p>

## Table of Contents

- [Repository Introduction](#repository-introduction)  
- [Prerequisites](#prerequisites)  
- [Image Specifications](#image-specifications)
- [Getting Help](#getting-help)
- [How to Contribute](#how-to-contribute)

## Repository Introduction  
Chroma embeddings databases (also known as vector databases) store embeddings and allow you to search by nearest neighbors rather than by substrings like a traditional database. By default, Chroma uses Sentence Transformers to embed for you but you can also use OpenAI embeddings, Cohere (multilingual) embeddings, or your own.

**Core Features:**

1.Extremely low entry barriers and an excellent developer experience: simple installation, intuitive APIs, and ready-to-use out of the box.

2.Flexible runtime modes: from fast in-memory prototyping to persistent production deployment.

3.Powerful metadata filtering: a key weapon for improving retrieval accuracy.

4.Deep integration with AI development ecosystems (Python/JS, LangChain): seamlessly integrates into existing workflows.

5.Efficient core vector operations: delivering fast and accurate similarity searches.

**Architecture Design:**

![](./images/img.png)

![](./images/img2.png)

This project offers pre-configured [**Flink Stream Analysis Tool**](https://marketplace.huaweicloud.com/contents/992480da-64a3-4ba8-90cb-686d1832e96a#productid=OFFI1111485128289529856) images with Flink and its runtime environment pre-installed, along with deployment templates. Follow the guide to enjoy an "out-of-the-box" experience.

> **System Requirements:**
> - CPU: 2GHz or higher  
> - RAM: 4GB or more  
> - Disk: At least 40GB  

## Prerequisites  
[Register a Huawei account and activate Huawei Cloud](https://support.huaweicloud.com/usermanual-account/account_id_001.html)

## Image Specifications  

| Image Version                                                                                                            | Description | Notes |  
|--------------------------------------------------------------------------------------------------------------------------|-------------|-------|  
| [Chroma-1.0.16-kunpeng](https://github.com/HuaweiCloudDeveloper/chroma-image/tree/Chroma-1.0.16-kunpeng)                    | Deployed on Kunpeng servers with Huawei Cloud EulerOS 2.0 64bit |  | 


## Getting Help
- Submit an [issue](https://github.com/HuaweiCloudDeveloper/flink-image/issues)
- Contact Huawei Cloud Marketplace product support

## How to Contribute
- Fork this repository and submit a merge request.
- Update README.md synchronously based on your open-source mirror information.
