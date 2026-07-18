---
ko_hash: be63066cfda3cea2fe37cf8958b3837afac82b48
---
# Decisions — 横向决策树

_最终更新: 2026-07 · owner: 待定 ⚠️ · volatility: 中_
[← 返回 index](index.md)

> **L0 TL;DR**: 把客户常遇到的 4 个岔路口以**决策表/树**（而非散文）呈现。每个决策都横跨多个支柱。赶时间就只看对应的表来确定方向。

目录: [1) Cloud vs Edge](#1-cloud-training-vs-edge-inference-边界) · [2) NVIDIA vs 开源](#2-nvidia-全栈-vs-开源) · [3) GPU 获取策略](#3-gpu-获取策略) · [4) Build vs Buy](#4-build-vs-buy基础模型)

---

## 1) Cloud training vs Edge inference 边界

**核心问题: "这个推理能放云上，还是必须放边缘？"**

最重要的判别因素是**控制频率**。

```
推理频率的要求是？
├─ 30~100Hz+ 反应式控制（平衡·力·抓取·行走·避障）
│     → 🔴 必须边缘板载 (Jetson Thor/Orin)。不能云端往返。
│        System 1（轻量 diffusion/flow-matching 策略, sub-20ms）
│
├─ few-Hz ~ sub-1Hz 高层规划·重规划·工具选择·场景理解
│     → 🟢 可放云/异步 (Bedrock AgentCore, 大型 VLM)。
│        System 2（重型 VLM 规划器, 5~10Hz 或更低）
│
└─ 两者都需要（几乎所有真实机器人）
      → 🟡 分离部署: System 2=云, System 1=边缘。
         用 action chunking 连接两种 rate。← 标准架构
```

| 区分 | System 2（规划） | System 1（控制） |
|---|---|---|
| 频率 | 5~10Hz 以下 | 50~200Hz |
| 延迟容忍 | 有（异步） | 无（sub-20ms） |
| 位置 | **云** (AgentCore) 或板载 | **边缘板载** (Jetson) |
| 模型 | 大型 VLM/LLM | 轻量 diffusion/flow-matching |
| AWS | Bedrock AgentCore, EC2 | IoT Greengrass V2, SageMaker Neo, ONNX/TensorRT |

> **判定原则**: "涉及实时安全·反应的回路就放边缘，有时间思考就放云。" action chunking 是桥梁。
> 依据: [pillar-4 边缘](pillar-4.md)、[pillar-2 System1/System2](pillar-2.md)、[pillar-5](pillar-5.md)。

---

## 2) NVIDIA 全栈 vs 开源

**核心问题: "全押 Isaac，还是走开源？"**

```
工作负载的性质是？
├─ 照片级渲染 + 合成数据生成(SDG) + 全栈整合
│     → Isaac Sim/Lab (🟢 GA 5.1)。GPU 必须 RTX (G6e/G7e)。
│
├─ 快速 RL 迭代 · 可微分物理 · 跨厂商 GPU · 轻量
│     → MuJoCo/MJX (🟢)。也可利用计算 GPU(P5 A100/H100) → 成本优势。
│        Unitree 实际使用 [1]（生产验证 → pillar-3）。
│
├─ ROS 2 原生整合 · CPU · 传统机器人
│     → Gazebo (🟢 Jetty/Harmonic)。⚠️ Classic 11 已 EOL。不适合 GPU 并行 RL。
│
└─ "话题性" Genesis？
      → ⚪ 仅限 PoC/实验。"430,000 倍"已被反驳 [1]（→ pillar-3）。禁止生产依赖。
```

| 标准 | Isaac Sim/Lab | MuJoCo/MJX | Gazebo |
|---|---|---|---|
| 成熟度 | 🟢 GA 5.1 | 🟢 GA（Warp 为 Alpha） | 🟢 GA（Classic EOL） |
| GPU | **必须 RTX**（A100/H100 ✗） | 可用计算 GPU（P5 ✓） | 以 CPU 为主 |
| 渲染/SDG | 最佳 | 有限 | 有限 |
| 可微分 | △ | ✓ (JAX) | ✗ |
| ROS 整合 | 可以 | 辅助 | **原生** |
| 许可证 | Apache（源码）+AI Enterprise（再分发/SaaS） | Apache | Apache |
| AWS | G6e/G7e + AMI + Batch | EC2（含 P5）+ Batch | EC2 + Batch |

> **判定原则**: 按工作负载选即可。**"AWS 三者都能跑好"** —— 对担心 NVIDIA 依赖的客户给出中立立场。用 MuJoCo 则有复用计算 GPU 的成本优势。
> 依据: [pillar-3](pillar-3.md)。

---

## 3) GPU 获取策略

**核心问题: "怎么获取 GPU？On-Demand 拿不到。"**

```
训练规模·时长是？
├─ 少数 GPU · 一次性 · LoRA 微调（多数起点）
│     → On-Demand G7e/G6e。即时、灵活。够用。
│
├─ 大规模 · 未来时点确定 · 超大型集群(P6e-GB200 等)
│     → Capacity Blocks for ML。提前预约，获取 UltraServer。
│
├─ 灵活日程 · 成本最优 · 数天~数周级训练窗口
│     → Flexible Training Plans (SageMaker HyperPod)。
│
└─ 需要 RTX 渲染 (Isaac Sim) vs 仅计算 (MuJoCo/VLA 训练)
      → 渲染=G6e/G7e (RTX)，计算=P5/P6 (A100/H100/B200) 或用 MuJoCo 则复用 P5。
```

| 策略 | 何时 | AWS |
|---|---|---|
| On-Demand | 少数·一次性·探索 | EC2 G7e/G6e/P6 |
| Capacity Blocks for ML | 大规模·时点确定·UltraServer | P6e-GB200，预约 |
| Flexible Training Plans | 灵活日程·成本最优 | SageMaker HyperPod |
| Trainium | 降低 LLM 训练成本 | Trn2/Trn3 ⚠️ **VLA 无公开案例 [4]**（→ pillar-2） |

> **判定原则**: 起步用 On-Demand G7e。拿不到或规模大则用 Capacity Blocks/Flexible Training Plans。**Trainium 对 LLM 安全，但 VLA/机器人无验证案例** —— 提议时明示风险。
> 依据: [pillar-2 训练栈](pillar-2.md)、[pillar-3](pillar-3.md)。

---

## 4) Build vs Buy（基础模型）

**核心问题: "是微调基础模型，还是自行训练？"**

```
数据·目标·资源是？
├─ 真实演示 100~数千个 · 特定任务 · 快速出结果
│     → 微调开放 VLA (LoRA)。单张 G7e，1 天 PoC。← 99% 的现实
│        商用则确认许可证: π=Apache-2.0 ✅, OpenVLA=MIT ✅, GR00T=需确认 ⚠️
│
├─ 多 embodiment · 大规模真实数据 · 连骨干一起调
│     → 全量微调 (P6/HyperPod)。70~100GB+ GPU。
│
├─ 从零预训练（自研前沿 VLA）
│     → 🔴 极少数。多节点 Blackwell 集群·大规模真实数据。
│        对多数客户不推荐 —— 微调即够。
│
└─ 只需要推理·规划层（无需低层控制）
      → Gemini Robotics-ER(API) 或用 AgentCore 编排。
```

| 选项 | 数据 | GPU | 何时 |
|---|---|---|---|
| LoRA 微调 | 100~数千演示 | 单张 24~40GB | **默认起点** |
| 全量微调 | 大规模真实数据 | 70~100GB+ / 多节点 | 多 embodiment |
| 预训练(Build) | 超大规模 | Blackwell 集群 | 极少数前沿 |
| Buy 推理层 | — | — | 控制用开放模型，规划用 API |

> **判定原则**: **几乎总是微调(Buy+adapt) 才是答案。** 从零预训练是极少数。商用时许可证是第一道门禁（注意 GR00T 非商业）。"仅靠仿真做操作策略"是陷阱 —— 真实数据必需（[pillar-4](pillar-4.md)）。
> 依据: [pillar-2](pillar-2.md)、[pillar-1 数据·许可证](pillar-1.md)、[pillar-4](pillar-4.md)。

---

## 附录 — 区域/数据驻留快速判定

_（下表为易变 —— 2026-07，以 AWS 官方区域表 `[1]` 直接确认为准。引用前再确认最新区域表）_

| 服务 | 首尔(ap-northeast-2) | 备注 |
|---|---|---|
| Bedrock AgentCore（核心+Policy+Evaluations） | ✅ | Agent Registry·Payments 为 ✗（东京 Registry ✅）—— 以 2026-07 区域表为准 |
| EC2 G7e / G6e / P6 | ✅（按区域确认） | 利用 Capacity Blocks |
| SageMaker HyperPod | ✅ | Flexible Training Plans 区域扩展中 |
| IoT Greengrass V2 | ✅ | V1 于 2026-06 EOL |

> 担心数据驻留的客户: 先让其确认 **AgentCore 首尔 GA** 来安心（更正过时的"首尔不支持"信息）。→ [pillar-5](pillar-5.md)。

---
_owner: 待定 ⚠️ · updated: 2026-07 · volatility: 中（树的原理为低，实例/区域细节为高）_
