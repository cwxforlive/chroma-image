# 1、环境准备

## 1.1 docker安装

```shell

#CENTOS/RHEL
sudo yum update -y
sudo yum install -y yum-utils device-mapper-persistent-data lvm2 curl wget git
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install -y docker-ce-20.10.21 docker-ce-cli-20.10.21 containerd.io
sudo systemctl enable docker && sudo systemctl start docker
docker -v
# 输出应为 Docker version 20.10.x
```

## 1.2 k8s安装

```shell
cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-\$basearch
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOF
sudo yum install -y kubelet-1.21.14-0 kubeadm-1.21.14-0 kubectl-1.21.14-0 --disableexcludes=kubernetes
sudo systemctl enable kubelet && sudo systemctl start kubelet
sudo kubeadm init --apiserver-advertise-address=<master-ip> --pod-network-cidr=10.244.0.0/16 --kubernetes-version=1.21.14
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
kubectl taint nodes --all node-role.kubernetes.io/master-
```
# 2、安装ArgoWorkflows

```shell
kubectl create namespace argo
kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo-workflows/stable/manifests/install.yaml
cat <<EOF | kubectl apply -n argo -f -
apiVersion: v1
kind: Secret
metadata:
  name: default.service-account-token
  annotations:
    kubernetes.io/service-account.name: default
type: kubernetes.io/service-account-token
EOF
kubectl get serviceaccount -n argo | grep argo-server
# 如果存在，则创建对应的 Secret
cat <<EOF | kubectl apply -n argo -f -
apiVersion: v1
kind: Secret
metadata:
  name: argo-server.service-account-token
  annotations:
    kubernetes.io/service-account.name: argo-server
type: kubernetes.io/service-account-token
EOF
curl -sLO https://github.com/argoproj/argo-workflows/releases/download/v3.7.1/argo-linux-arm64.gz
gunzip argo-linux-arm64.gz
chmod +x argo-linux-arm64
sudo mv ./argo-linux-arm64 /usr/local/bin/argo
argo version
```
