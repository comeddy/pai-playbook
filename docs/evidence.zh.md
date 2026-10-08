---
ko_hash: c52bf32e3cb8f788b6384f47337ac5a43f993bf1
---
# 证据记录 — 每项主张的日期、范围与复核状态

_最后更新: 2026-09 · owner: Youngjin · volatility: 中_

**L0 TL;DR**: 页面修改日期不等于所有主张已重新验证。以下七项记录覆盖本次核心修正，其他旧有主张尚未迁入，不代表全量事实审计。

`source-checked` 表示与指定一手来源对照；`withdrawn` 撤回旧有泛化或承诺；`reproduction-pending` 表示待实际运行复现。全部**待人工复核**，不代表 AWS 官方批准或保证。原文对照、实验复现和现场发布批准是不同阶段。

源数据为 [claims.json](assets/claims.json)，本页区块由其生成。CI 检查必填字段、四种语言、影响页面、日期及显示同步，并对过期复核发出警告；不判断来源真实性或客户现场适用性。

<!-- evidence:start -->

### openvla-license { #openvla-license }

OpenVLA 区分 MIT 代码与适用 Llama Community License 的 Llama-2 派生预训练权重。商业判断应核对所选权重、基础模型和数据条件，不能仅依据代码 LICENSE。

- 确认日期: 2026-09-15 · 状态: `source-checked` · 复核周期（天）: 30
- 对照者: Codex (source comparison) · 人工复核: 待定
- 影响页面: [pillar-2](pillar-2.md) · [decisions](decisions.md) · [exec](exec.md)
- 来源: [OpenVLA README](https://github.com/openvla/openvla#pretrained-vlas)

### agentcore-residency { #agentcore-residency }

AgentCore 可用区域、存储区域和推理处理区域不同。Memory 可跨 APAC 区域推理，首尔发起的 Evaluations 使用全球跨区域推理。韩国境内处理要求需按功能、模型和路径审查。

- 确认日期: 2026-09-15 · 状态: `source-checked` · 复核周期（天）: 30
- 对照者: Codex (source comparison) · 人工复核: 待定
- 影响页面: [pillar-5](pillar-5.md) · [decisions](decisions.md) · [exec](exec.md) · [operations](operations.md)
- 来源: [AWS cross-region inference](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/cross-region-inference.html) · [AWS Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-cross-region-inference.html)

### fleetwise-new-customers { #fleetwise-new-customers }

IoT FleetWise 不接受新客户，现有客户可继续使用。不要称为服务已终止，也不要作为新机器人机群架构的默认选项。

- 确认日期: 2026-09-15 · 状态: `source-checked` · 复核周期（天）: 30
- 对照者: Codex (source comparison) · 人工复核: 待定
- 影响页面: [pillar-5](pillar-5.md) · [radar](radar.md)
- 来源: [AWS IoT FleetWise](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/what-is-iotfleetwise.html)

### action-chunking { #action-chunking }

动作输出数量不等于响应新观测的频率，不能用推理 Hz 乘 chunk 长度作为反馈控制频率。PI 单独处理切换与延迟问题；Helix S1/S2 都在板载运行，不是云部署的证据。

- 确认日期: 2026-09-15 · 状态: `source-checked` · 复核周期（天）: 90
- 对照者: Codex (source comparison) · 人工复核: 待定
- 影响页面: [pillar-2](pillar-2.md) · [pillar-4](pillar-4.md) · [pillar-5](pillar-5.md) · [decisions](decisions.md) · [operations](operations.md)
- 来源: [PI real-time chunking](https://www.physicalintelligence.company/research/real_time_chunking) · [Figure Helix](https://www.figure.ai/news/helix)

### simulation-cost { #simulation-cost }

撤回“首尔 g6e.xlarge + 4~20 分钟 = 每轮 $11~12”的泛化。$0.98/小时乘 4~20 分钟仅得算术值约 $0.07~0.33，并非该实例实测。样本作者约两小时/$12 的估算属于其他配置。

- 确认日期: 2026-09-15 · 状态: `withdrawn` · 复核周期（天）: 30
- 对照者: Codex (source comparison) · 人工复核: 待定
- 影响页面: [pillar-3](pillar-3.md) · [execution](execution.md) · [exec](exec.md)
- 来源: [Pinned simulation sample](https://github.com/aws-samples/sample-issac-lab-on-aws/tree/50ea76d87d873c1d69bed92c450ab144894f437e) · [ETH parallel RL paper](https://arxiv.org/abs/2109.11978)

### finetuning-outcomes { #finetuning-outcomes }

撤回“100~500 个演示 → 80%+ 成功”和“100 个演示一天出结果”的通用承诺。成功率及周期需要明确数据、任务、模型、训练及评估条件的实验。

- 确认日期: 2026-09-15 · 状态: `withdrawn` · 复核周期（天）: 90
- 对照者: Codex (source comparison) · 人工复核: 待定
- 影响页面: [pillar-2](pillar-2.md) · [exec-guide](exec-guide.md) · [decisions](decisions.md) · [execution](execution.md)
- 来源: [OpenVLA fine-tuning](https://github.com/openvla/openvla#fine-tuning-openvla-via-lora)

### execution-samples { #execution-samples }

对照了三个样本的提交、README 和命令；本次修订未运行 AWS 或实机。训练作者报告 Pattern A 完成运行，不能将 B/C、RL 及强制中断恢复视为同等已验证。

- 确认日期: 2026-09-15 · 状态: `reproduction-pending` · 复核周期（天）: 30
- 对照者: Codex (source comparison) · 人工复核: 待定
- 影响页面: [execution](execution.md) · [pillar-1](pillar-1.md) · [pillar-2](pillar-2.md) · [pillar-3](pillar-3.md)
- 来源: [Data sample](https://github.com/aws-samples/sample-lerobot-data-collection-on-aws-iot-greengrass/tree/6078f4f3cf2cc2432cdc52ffbc98b85abfa22d2e) · [Simulation sample](https://github.com/aws-samples/sample-issac-lab-on-aws/tree/50ea76d87d873c1d69bed92c450ab144894f437e) · [Training sample](https://github.com/aws-samples/sample-vla-finetuning/tree/f21e4a9bf0ec11f40c2298a85951690b61efeaac)

<!-- evidence:end -->

## 更新及复核分工 { #review }

owner Youngjin 分配复核任务。许可证、AWS 服务/区域、机器人控制/安全、实验复现的人工复核人**待分配**，不虚构姓名。记录原文对照者，只有实际人工确认后才设置 `human_review: complete` 并填写实名。

主张变化时同步修改 `pages` 列出的原文、摘要及翻译，并更新确认日期及依据。运行 `python3 scripts/check_evidence.py --render`，更新翻译哈希后执行全部检查。HTTP 200、构建通过及翻译哈希不能替代事实验证。

_owner: Youngjin · updated: 2026-09 · volatility: 中_
