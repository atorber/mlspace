# 模型产物模块

本模块对应百度百舸 AI 计算平台中的 AI 资产 `Model` 相关资料目录，用于承接模型权重、导出物、归档与交付规范。

## 该模块管什么

- 模型权重与导出物的版本化规则（与 `governance/manifest` 的记录建立可追溯关联）
- 产物归档结构（便于存储、下载、校验与回滚）
- 交付清单（上线或交付时需要明确哪些文件“缺一不可”）

## 不管什么（平台边界）

- 训练过程组织与日志：归 `job/`
- 推理兼容性检查与导出验证：归 `serving/compatibility/`
- 运行时资源与存储访问模式：归 `ai_compute_resource/`

## 建议产物目录结构

```text
ai_asset/model/
  <model_name>/
    <version>/
      weights/                # 训练权重（如 .pt/.ckpt）
      exported/               # 导出物（如 onnx/tensorrt）
      configs/                # 训练/导出配置的快照（不依赖外部路径）
      checksums/             # 文件校验和（用于完整性验证）
      reports/               # 指标报告、导出验证报告等
      README.md              # 该版本产物的简要说明与使用方式
```

## 与治理记录的关联方式

建议把以下关键字段写入 `governance/manifest/`，并在产物中留出反向可读入口：

- `data_lineage.dataset_name`、`dataset_version`
- `code_fingerprint.git_hash`（以及未提交补丁状态）
- `environment_baseline.docker_image_tag`、`cuda_version`、`python_version`
- `outputs.model_artifact`（产物存储位置或引用 URI）
- `outputs.report_uri`（指标与验证报告位置）

## 交付清单（发布前检查）

发布/交付时至少应确认：

- 权重与导出物都存在，且文件校验和可用
- 导出验证通过（参考 `serving/compatibility/` 的检查项）
- manifest 记录与产物 URI 能互相对应
