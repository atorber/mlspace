# 镜像模块

本模块对应百度百舸 AI 计算平台中的 AI 资产 `Image` 模块，沉淀训练与推理镜像规范，以及镜像仓库初始化方式。

## 包含内容

- `docker/`：机器学习工作负载的容器镜像约定
- `setup_registry.sh`：本地或私有镜像仓库初始化占位脚本

## 边界说明

镜像构建和镜像分发归本模块管理。
Kubernetes 运行时与存储 sidecar 访问模式归 `ai_compute_resource/`。
