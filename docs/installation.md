# 1、环境准备

## 1.1 python安装

```shell
# ubuntu 系统
apt update
apt install -y python3-pip python3-venv build-essential libpq-dev
#CENTOS/RHEL
yum update
yum nstall -y python3-pip python3-venv build-essential libpq-dev
```

## 1.1 创建虚拟化环境

```shell
python3 -m venv chroma-env
souorce chroma-env/bin/activate
```
# 2、安装chroma

```shell
pip3 install chromadb
```
