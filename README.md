# Awesome VLA-WAM

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated reading list for Vision-Language-Action (VLA), World Action Model
(WAM), and agentic robotics research, organized around four active directions:

- Agentic robotics for embodied agents that coordinate multi-step physical
  tasks through planning, memory, tool or skill composition, and self-improvement.
- World Action Models for robotics.
- Failure detection, correction, feedback, and recovery in VLA systems.
- Efficient VLA models, action tokenization, compression, and deployment.

<p align="center">
  <img src="assets/awesome-vla-wam-hero-v2.png" alt="Awesome VLA-WAM hero image" width="100%">
</p>

<p align="center">
  <img src="assets/vla-wam-papers-by-month.gif" alt="Animated monthly paper counts by category" width="100%">
</p>

The animation tracks papers added since January 2026 and is regenerated from
the arXiv identifiers in this README with
[`scripts/generate_monthly_paper_chart.py`](scripts/generate_monthly_paper_chart.py).

The agentic robotics section requires an explicit embodied-agent layer that
coordinates multi-step physical execution through high-level planning, memory,
tool or skill discovery and composition, VLA/VLM or policy orchestration,
navigation, recovery, or online policy self-improvement. Standalone prompt
optimization, generic exploration, or low-level VLA improvements without this
agent-level role are out of scope.
The failure
detection/correction section is not a one-to-one heading in the source
repository; it groups papers that are closely related through environment
feedback, self-improvement, verification, closed-loop learning, preference
alignment, online planning, or robustness evaluation.

## Contents

- [Agentic Robotics (New Trend)](#agentic-robotics-new-trend) ([full archive](AGENTIC_ROBOTICS.md))
- [Surveys and Definitions](#surveys-and-definitions)
- [World Action Models](#world-action-models) ([full archive](WORLD_ACTION_MODELS.md))
- [VLA Failure Detection and Correction](#vla-failure-detection-and-correction) ([full archive](VLA_FAILURE_DETECTION_AND_CORRECTION.md))
- [Efficient VLA](#efficient-vla) ([full archive](EFFICIENT_VLA.md))
- [Benchmarks for Robustness and Evaluation](#benchmarks-for-robustness-and-evaluation)
- [Contributing](#contributing)

Section badges indicate the last curated refresh date for each category.
The main paper sections below show the latest 10 entries for each direct
list or subsection, sorted by available arXiv date/id. Full retained lists are
kept in the linked archive documents.

Relevance: stars indicate topical relevance only, not paper quality: ⭐⭐⭐ direct fit · ⭐⭐ adjacent/supporting · ⭐ background/context.

## Agentic Robotics (New Trend) ![Updated](https://img.shields.io/badge/Updated-2026--07--27-0A7F5A?labelColor=333333)

Full archive: [Agentic Robotics](AGENTIC_ROBOTICS.md).

This emerging line treats robot foundation models as components inside a
broader embodied-agent loop. Papers belong here only when the agent layer is
central to coordinating physical multi-step execution through planning,
memory, tool or skill composition, policy orchestration, navigation, recovery,
or online self-improvement; standalone model or prompt improvements are out of
scope.

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| Physical Agency | Addressing the Orchestration Gap in Generalist Robots via Physical Agency. | [arXiv](https://arxiv.org/abs/2607.21725) | ⭐⭐⭐ |
| LENS | LENS: LLM-guided Environment Simplification for Planning and Control in Clutter. | [arXiv](https://arxiv.org/abs/2607.19633) · [Website](https://lens-2026.github.io/) | ⭐⭐⭐ |
| Intelligent Multi-UAV Navigation | Intelligent Multi-UAV Navigation in ITNTNs: A Hierarchical LLM Approach. | [arXiv](https://arxiv.org/abs/2607.18604) | ⭐⭐⭐ |
| RoboHarness | RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning. | [arXiv](https://arxiv.org/abs/2607.18060) | ⭐⭐⭐ |
| SkillNav | Score-Level Skill Intervention for Zero-Shot Object Goal Navigation. | [arXiv](https://arxiv.org/abs/2607.15758) | ⭐⭐⭐ |
| RoboTTT | RoboTTT: Context Scaling for Robot Policies. | [arXiv](https://arxiv.org/abs/2607.15275) · [Website](https://research.nvidia.com/labs/gear/robottt/) | ⭐⭐⭐ |
| Agent-Client Protocol | Human-Robot Interaction in GenAI Architectures via the Agent-Client Protocol. | [arXiv](https://arxiv.org/abs/2607.14919) | ⭐⭐⭐ |
| PhysClaw-0 | PhysClaw-0: A Symbiotic Agentic System for Robot Autonomy via Language Corrections. | [arXiv](https://arxiv.org/abs/2607.14047) · [Website](https://open-gigaai.github.io/PhysClaw) | ⭐⭐⭐ |
| Hy-Embodied-VLM-1.0 | Hy-Embodied-VLM-1.0: Efficient Physical-World Agents. | [arXiv](https://arxiv.org/abs/2607.12894) · [Code](https://github.com/Tencent-Hunyuan/HY-Embodied) | ⭐⭐ |
| PHILIA | A Glimpse into Long-term Physical Coexistence with Intelligent Robots. | [arXiv](https://arxiv.org/abs/2607.11377) | ⭐⭐⭐ |

## Surveys and Definitions ![Updated](https://img.shields.io/badge/Updated-2026--07--15-0A7F5A?labelColor=333333)

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| From World Action Models to Embodied Brains | From World Action Models to Embodied Brains: A Roadmap for Open-World Physical Intelligence. | [arXiv](https://arxiv.org/abs/2607.11689) | ⭐ |
| From World Models to World Action Models | From World Models to World Action Models: A Concise Tutorial for Robotics. | [arXiv](https://arxiv.org/abs/2607.00836) · [Website](https://clearlab-sustech.github.io/WorldModelSurvey/) · [Code](https://github.com/clearlab-sustech/WorldModelSurvey) | ⭐ |
| World Action Models: The Next Frontier in Embodied AI. | World Action Models: The Next Frontier in Embodied AI. | [arXiv](https://arxiv.org/abs/2605.12090) · [Website](https://openmoss.github.io) | ⭐ |
| DreamZero | World Action Models are Zero-shot Policies. | [arXiv](https://arxiv.org/abs/2602.15922) · [Website](https://dreamzero0.github.io) | ⭐⭐ |
| Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges. | Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges. | [arXiv](https://arxiv.org/abs/2505.04769) · [Website](https://github.com/Applied-AI-Research-Lab/Vision-Language-Action-Models-Concepts-Progress-Applications-and-Challenges) | ⭐⭐ |
| A Survey on Vision-Language-Action Models for Embodied AI. | A Survey on Vision-Language-Action Models for Embodied AI. | [arXiv](https://arxiv.org/abs/2405.14093) · [Website](https://github.com/yueen-ma/Awesome-VLA) | ⭐ |
| RT-2 | RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control. | [arXiv](https://arxiv.org/abs/2307.15818) · [Website](https://robotics-transformer2.github.io) | ⭐ |

## World Action Models ![Updated](https://img.shields.io/badge/Updated-2026--07--27-0A7F5A?labelColor=333333)

Full archive: [World Action Models](WORLD_ACTION_MODELS.md).

### Video-Generation-Based WAM ![Updated](https://img.shields.io/badge/Updated-2026--07--27-0A7F5A?labelColor=333333)

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| Robot-Factored World Models | Robot-Factored World Models via Robot Rendering. | [arXiv](https://arxiv.org/abs/2607.22535) · [Website](https://bjkim95.github.io/rofacto/) | ⭐⭐⭐ |
| Masked Visual Actions | Masked Visual Actions for Unified World Modeling. | [arXiv](https://arxiv.org/abs/2607.19343) · [Website](https://masked-visual-actions.github.io/) | ⭐⭐⭐ |
| AeroAct | AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight. | [arXiv](https://arxiv.org/abs/2607.14997) | ⭐⭐⭐ |
| FlowWAM | FlowWAM: Optical Flow as a Unified Action Representation for World Action Models. | [arXiv](https://arxiv.org/abs/2607.13017) · [Website](https://flow-wam.github.io/) | ⭐⭐⭐ |
| LingBot-VA 2.0 | Native Video-Action Pretraining for Generalizable Robot Control. | [arXiv](https://arxiv.org/abs/2607.08639) · [Website](https://technology.robbyant.com/lingbot-va-v2) | ⭐⭐⭐ |
| Temporal Ratio | Understanding and Mitigating the Video-Action Generalization Gap via Temporal Ratio. | [arXiv](https://arxiv.org/abs/2607.08127) · [Website](https://umishra.me/temporal-ratio/) | ⭐ |
| SWAM | Pondering the Way: Spatial-perceiving World Action Model for Embodied Navigation. | [arXiv](https://arxiv.org/abs/2606.29908) | ⭐⭐⭐ |
| NavWM | NavWM: A Unified Navigation World Model for Foresight-Driven Planning. | [arXiv](https://arxiv.org/abs/2606.24101) | ⭐ |
| ImageWAM | ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing? | [arXiv](https://arxiv.org/abs/2606.19531) · [Website](https://zhangwenyao1.github.io/ImageWAM/) | ⭐⭐⭐ |
| Metis | Metis: A Generalizable and Efficient World-Action Model for Autonomous Driving and Urban Navigation. | [arXiv](https://arxiv.org/abs/2606.15869) | ⭐⭐ |

### VLM-Based WAM ![Updated](https://img.shields.io/badge/Updated-2026--07--25-0A7F5A?labelColor=333333)

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| HyWorldVLA | HyWorldVLA: A Vision-Language-Action Model with Hybrid World Modeling for Autonomous Driving. | [arXiv](https://arxiv.org/abs/2607.20988) | ⭐⭐⭐ |
| DSWAM | DSWAM: A Dual-System World Action Foundation Model for Fine-Grained Robot Manipulation. | [arXiv](https://arxiv.org/abs/2607.04927) | ⭐⭐⭐ |
| FutureNav | FutureNav: Unified World-Action Modeling for Vision-and-Language Navigation. | [arXiv](https://arxiv.org/abs/2606.30367) | ⭐⭐⭐ |
| WLA | World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis. | [arXiv](https://arxiv.org/abs/2606.05979) · [Website](https://github.com/SJTU-DENG-Lab/WLA) | ⭐⭐⭐ |
| CKT-WAM | CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models. | [arXiv](https://arxiv.org/abs/2605.06247) · [Website](https://github.com/YuhuaJiang2002/CKT-WAM) | ⭐⭐ |
| World-Value-Action Model | World-Value-Action Model: Implicit Planning for Vision-Language-Action Systems. | [arXiv](https://arxiv.org/abs/2604.14732) | ⭐⭐⭐ |
| WoG | World Guidance World Modeling in Condition Space for Action Generation. | [arXiv](https://arxiv.org/abs/2602.22010) · [Website](https://selen-suyue.github.io/WoGNet/) | ⭐⭐ |
| VLAW | VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model. | [arXiv](https://arxiv.org/abs/2602.12063) · [Website](https://sites.google.com/view/vlaw-arxiv) | ⭐⭐⭐ |
| VLA-JEPA | VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model. | [arXiv](https://arxiv.org/abs/2602.10098) · [Website](https://ginwind.github.io/VLA-JEPA/) | ⭐⭐⭐ |
| MM-ACT | MM-ACT: Learn from Multimodal Parallel Generation to Act. | [arXiv](https://arxiv.org/abs/2512.00975) · [Website](https://github.com/HHYHRHY/MM-ACT) | ⭐⭐ |

### WAM from Scratch and Latent Dynamics ![Updated](https://img.shields.io/badge/Updated-2026--07--21-0A7F5A?labelColor=333333)

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| GeoWorldAD | GeoWorldAD: Geometry World Action Model for Autonomous Driving. | [arXiv](https://arxiv.org/abs/2607.17521) | ⭐⭐⭐ |
| BadWAM | BadWAM: When World-Action Models Dream Right but Act Wrong. | [arXiv](https://arxiv.org/abs/2607.15207) | ⭐⭐⭐ |
| GigaWorld-Policy-0.5 | GigaWorld-Policy-0.5: A Faster and Stronger WAM Empowered by AutoResearch. | [arXiv](https://arxiv.org/abs/2607.13960) · [Website](https://open-gigaai.github.io/giga-world-policy/) | ⭐⭐⭐ |
| FlowDAgger | FlowDAgger: Human-in-the-Loop Adaptation of Generative Robot Policies in Latent Space. | [arXiv](https://arxiv.org/abs/2607.08877) · [Website](https://microsoft.github.io/FlowDAgger) | ⭐ |
| EgoWAM | EgoWAM: World Action Models Beyond Pixels with In-the-Wild Egocentric Human Data. | [arXiv](https://arxiv.org/abs/2607.08436) · [Website](https://gatech-rl2.github.io/egowam.github.io) | ⭐⭐⭐ |
| WAM-TTT | WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time. | [arXiv](https://arxiv.org/abs/2607.06988) | ⭐⭐⭐ |
| 4D Geometric Priors for WAM | Learning 4D Geometric Priors for Inference-Efficient World Action Models. | [arXiv](https://arxiv.org/abs/2607.05468) | ⭐⭐⭐ |
| VT-WAM | VT-WAM: Visual-Tactile World Action Model for Contact-Rich Manipulation. | [arXiv](https://arxiv.org/abs/2607.02503) · [Website](https://vt-wam.github.io/) | ⭐ |
| Bridge-WA | Bridge-WA: Predicting Where and How the World Changes for Robotic Action. | [arXiv](https://arxiv.org/abs/2607.02195) · [Website](https://hcplab-sysu.github.io/BRIDGE-WA) | ⭐⭐⭐ |
| ABot-M0.5 | ABot-M0.5: Unified Mobility-and-Manipulation World Action Model. | [arXiv](https://arxiv.org/abs/2607.00678) · [Code](https://github.com/amap-cvlab/ABot-Manipulation) | ⭐⭐⭐ |

## VLA Failure Detection and Correction ![Updated](https://img.shields.io/badge/Updated-2026--07--27-0A7F5A?labelColor=333333)

Full archive: [VLA Failure Detection and Correction](VLA_FAILURE_DETECTION_AND_CORRECTION.md).

These papers are useful entry points for failure-aware VLA systems, especially
when the method uses feedback, online adaptation, closed-loop correction,
self-evaluation, or policy/world-model co-improvement.

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| FORGE-plus | FORGE-plus: Force-Budgeted Recovery for Contact-Rich Assembly with a Frozen LLM Supervisor. | [arXiv](https://arxiv.org/abs/2607.21227) | ⭐⭐⭐ |
| Robostral Navigate | Robostral Navigate. | [arXiv](https://arxiv.org/abs/2607.20785) | ⭐⭐⭐ |
| No Training, Better Flights | No Training, Better Flights: Test-Time Scaled VLMs for UAV Navigation. | [arXiv](https://arxiv.org/abs/2607.19288) | ⭐⭐⭐ |
| Closing the Loop in Humanoid VLA | Closing the Loop in Humanoid VLA: Persistent 3D Object Tokens for Verifiable Loco-Manipulation. | [arXiv](https://arxiv.org/abs/2607.18016) | ⭐⭐⭐ |
| AC-VLA | Robust Out-of-Distribution Action Execution via Compositional Learning. | [arXiv](https://arxiv.org/abs/2607.15714) | ⭐⭐⭐ |
| CosFly-VLA | CosFly-VLA: A Spatially Aware Vision-Language-Action Model for UAV Tracking. | [arXiv](https://arxiv.org/abs/2607.15004) | ⭐⭐⭐ |
| Robust Execution with Agentic RL | Learning Robust Execution in Robotic Manipulation with Agentic Reinforcement Learning. | [arXiv](https://arxiv.org/abs/2607.13818) | ⭐⭐⭐ |
| Artificial Foveated Perception | Artificial Foveated Perception for Mitigating Shortcut Learning in Robotic Foundation Models. | [arXiv](https://arxiv.org/abs/2607.10655) | ⭐ |
| Learning from Hindsight | Learning More from Less: Reinforcement Learning from Hindsight. | [arXiv](https://arxiv.org/abs/2607.09042) | ⭐⭐ |

## Efficient VLA ![Updated](https://img.shields.io/badge/Updated-2026--07--27-0A7F5A?labelColor=333333)

Full archive: [Efficient VLA](EFFICIENT_VLA.md).

### Compression, Adaptation, and Model Merging ![Updated](https://img.shields.io/badge/Updated-2026--07--26-0A7F5A?labelColor=333333)

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| DEED | Closing the Lab-to-Store Gap: A Data-Efficient Post-Training and Experience-Driven Learning VLA Framework for Retail Humanoids. | [arXiv](https://arxiv.org/abs/2607.20345) | ⭐⭐⭐ |
| Offline Supervision RL | Leveraging Offline Supervision for Efficient and Generalizable Reinforcement Learning in Large-Scale Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2607.19399) · [Project](https://alstar8.github.io/offline-supervision-vla-rl) | ⭐⭐⭐ |
| LifelongVLA | Towards Human-like Physical Intelligence: LifelongVision-Language-Action Learning for Robotic Manipulation. | [arXiv](https://arxiv.org/abs/2607.14852) | ⭐⭐⭐ |
| ExToken | ExToken: Structured Exploration for Efficient Vision-Language-Action Reinforcement Fine-tuning. | [arXiv](https://arxiv.org/abs/2607.12931) | ⭐⭐ |
| Z-1 | Z-1: Efficient Reinforcement Learning for Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2606.31846) | ⭐⭐ |
| Parameter Redundancy in VLA | Revisiting Parameter Redundancy in Vision-Language-Action Models: Insights from VLM-to-VLA Adaptation. | [arXiv](https://arxiv.org/abs/2606.31382) · [Code](https://github.com/Niannnnnn/VLA_Parameter_Redundancy_VLM2VLA) | ⭐ |
| Mix-QVLA | Mix-QVLA: Task-Evidence-Aware Mixed-Precision Quantization of Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2606.19565) | ⭐⭐⭐ |
| Learned Image Compression | Learned Image Compression for Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2606.16253) | ⭐⭐⭐ |
| Omega-QVLA | Ω-QVLA: Robust Quantization for Vision-Language-Action Models via Composite Rotation and Per-step Scaling. | [arXiv](https://arxiv.org/abs/2605.28803) · [Website](https://github.com/UCMP13753/Omega-QVLA) | ⭐⭐⭐ |
| EXPO-FT | EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2605.25477) | ⭐⭐ |

### Tokenization, Fine-Tuning, and Deployment-Friendly VLAs ![Updated](https://img.shields.io/badge/Updated-2026--07--27-0A7F5A?labelColor=333333)

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| OAT | Ordered Action Tokens for Visuomotor Policy Learning. | [arXiv](https://arxiv.org/abs/2607.21670) | ⭐⭐⭐ |
| JoyNexus | JoyNexus: Service-Oriented Multi-Tenant Post-Training for VLA Models. | [arXiv](https://arxiv.org/abs/2607.16074) | ⭐⭐⭐ |
| Fast-Slow VLA | Think at 5 Hz, Act at 20 Hz: Asynchronous Fast-Slow Vision-Language-Action Inference for Closed-Loop Driving. | [arXiv](https://arxiv.org/abs/2607.15621) | ⭐⭐⭐ |
| Jetson-PI | Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference. | [arXiv](https://arxiv.org/abs/2607.12659) · [Code](https://github.com/PKU-SEC-Lab/Jetson-PI) · [Inference Engine](https://github.com/PKU-SEC-Lab/Jetson-PI-Edge) | ⭐⭐⭐ |
| LoRA Fine-Tuning for VLA | On the Efficiency of LoRA Fine-Tuning for Vision-Language-Action Models in Industrial Robotic Manipulation. | [arXiv](https://arxiv.org/abs/2607.10172) | ⭐⭐⭐ |
| CLAP | CLAP: Direct VLM-to-VLA Adaptation via Language-Action Grounding. | [arXiv](https://arxiv.org/abs/2607.08974) · [Website](https://omron-sinicx.github.io/clap/) | ⭐ |
| FabriVLA | FabriVLA: A Lightweight Vision-Language-Action Model for Precise Multi-Task Manipulation. | [arXiv](https://arxiv.org/abs/2607.08575) | ⭐⭐⭐ |
| NativeMEM | NativeMEM: Native Memory Compression for Long-Horizon Robotic Manipulation. | [arXiv](https://arxiv.org/abs/2607.06678) | ⭐⭐⭐ |
| Action Caching and Refinement | Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement. | [arXiv](https://arxiv.org/abs/2607.06370) | ⭐⭐⭐ |
| XS-VLA | XS-VLA: Coupling Coarse-grained Spatial Distillation with Latent Flow Matching for Lightweight Robotic Control. | [arXiv](https://arxiv.org/abs/2607.04171) | ⭐⭐⭐ |

## Benchmarks for Robustness and Evaluation ![Updated](https://img.shields.io/badge/Updated-2026--07--15-0A7F5A?labelColor=333333)

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| WorldArena | WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models. | [arXiv](https://arxiv.org/abs/2602.08971) · [Website](https://world-arena.ai) | ⭐⭐ |
| LIBERO-Plus | LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2510.13626) · [Website](https://sylvestf.github.io/LIBERO-plus/) | ⭐⭐⭐ |
| RoboArena | RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies. | [arXiv](https://arxiv.org/abs/2506.18123) · [Website](https://robo-arena.github.io) | ⭐ |
| RoboTwin 2.0 | RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation. | [arXiv](https://arxiv.org/abs/2506.18088) · [Website](https://github.com/robotwin-Platform/robotwin/) | ⭐⭐ |
| SimplerEnv | Evaluating Real-World Robot Manipulation Policies in Simulation. | [arXiv](https://arxiv.org/abs/2405.05941) · [Website](https://simpler-env.github.io) | ⭐ |
| LIBERO | LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning. | [arXiv](https://arxiv.org/abs/2306.03310) · [Website](https://libero-project.github.io/main.html) | ⭐ |

## Contributing

Pull requests are welcome. A good entry should include:

- Paper or project name.
- Full title.
- arXiv, paper, project, or code link.
- One suggested category.
- Optional note explaining why it belongs in that category.

## Acknowledgements

Initial paper entries were reorganized from
[DravenALG/awesome-vla-wam](https://github.com/DravenALG/awesome-vla-wam).
