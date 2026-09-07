# Awesome VLA–WAM

<p align="center">
  <strong>Vision-Language-Action · World Action Models · Agentic Robotics</strong><br>
  <em>A curated, quality-gated reading list for embodied intelligence.</em>
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/Curated-2026--08--22-0A7F5A?labelColor=333333" alt="Curated 2026-08-22">
  <img src="https://img.shields.io/badge/Core%20paper%20lists-10%20each-3F88D6?labelColor=333333" alt="Core paper lists keep 10 entries each">
</p>

<p align="center">
  <img src="assets/awesome-vla-wam-hero-v2.png" alt="Awesome VLA-WAM hero image" width="100%">
</p>

<p align="center">
  <img src="assets/vla-wam-papers-by-month.gif" alt="Animated monthly paper counts by category" width="100%">
</p>

The animation tracks papers added since January 2026. It is regenerated from
the arXiv identifiers in this README with
[`scripts/generate_monthly_paper_chart.py`](scripts/generate_monthly_paper_chart.py).

## Curation Policy

> **Core lists:** Every primary paper table or subsection in this README keeps
> exactly the 10 newest qualifying papers, ordered by available arXiv date or
> identifier. The linked archive documents retain the longer historical lists.
>
> **Reference lists:** Surveys and Definitions, and Benchmarks for Robustness
> and Evaluation, are compact reference sections and may contain fewer than 10
> entries when fewer items are retained.
>
> **Relevance:** ⭐⭐⭐ direct fit · ⭐⭐ adjacent/supporting · ⭐ background/context.

The agentic robotics section requires an explicit embodied-agent layer that
coordinates multi-step physical execution through high-level planning, memory,
tool or skill discovery and composition, VLA/VLM or policy orchestration,
recovery, or online policy self-improvement. Pure navigation or VLN policies
without another agentic robotics capability are out of scope. Standalone prompt
optimization, generic exploration, or low-level VLA improvements without this
agent-level role are also out of scope.
The failure
detection/correction section is not a one-to-one heading in the source
repository; it groups papers that are closely related through environment
feedback, self-improvement, verification, closed-loop learning, preference
alignment, online planning, or robustness evaluation.

## Contents

| Section | Focus | Archive |
| --- | --- | --- |
| [Agentic Robotics](#agentic-robotics-new-trend) | Long-horizon embodied agents, tools, skills, and orchestration | [10+ historical entries](AGENTIC_ROBOTICS.md) |
| [Surveys and Definitions](#surveys-and-definitions) | Roadmaps, reviews, and shared terminology | — |
| [World Action Models](#world-action-models) | Predictive world-action modeling for robotics | [Historical lists](WORLD_ACTION_MODELS.md) |
| [VLA Failure Detection and Correction](#vla-failure-detection-and-correction) | Feedback, verification, recovery, and online adaptation | [Historical entries](VLA_FAILURE_DETECTION_AND_CORRECTION.md) |
| [Efficient VLA](#efficient-vla) | Compression, tokenization, fine-tuning, and deployment | [Historical lists](EFFICIENT_VLA.md) |
| [Benchmarks and Evaluation](#benchmarks-for-robustness-and-evaluation) | Robustness and evaluation resources | — |

Section badges show the latest curation date. Core paper lists below keep the
10 newest entries; reference sections may be shorter.

## Agentic Robotics (New Trend) ![Updated](https://img.shields.io/badge/Updated-2026--09--07-0A7F5A?labelColor=333333)

Full archive: [Agentic Robotics](AGENTIC_ROBOTICS.md).

This emerging line treats robot foundation models as components inside a
broader embodied-agent loop. Papers belong here only when the agent layer is
central to coordinating physical multi-step execution through planning,
memory, tool or skill composition, policy orchestration, recovery, or online
self-improvement; pure navigation-only or VLN policies are out of scope.

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| CFAM | Continual Field-Adaptive Models (CFAMs) for Post-Deployment Physical AI. | [arXiv](https://arxiv.org/abs/2609.04552) | ⭐⭐⭐ |
| HINT | HINT: Human-Intent Inception for Long-Horizon Robot Manipulation. | [arXiv](https://arxiv.org/abs/2609.02653) · [Project](https://robot-hint.github.io/) | ⭐⭐⭐ |
| EmbodiedSkills | EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents. | [arXiv](https://arxiv.org/abs/2609.01281) | ⭐⭐⭐ |
| SUN | SUN: Persistent Programs For Language-Grounded Control-to-Learning-to-Real Policies. | [arXiv](https://arxiv.org/abs/2608.31167) | ⭐⭐⭐ |
| LUCID | LUCID: An Agentic AI Framework on Digital-Twin in the Loop for QoS-Guaranteeing Robotic Control. | [arXiv](https://arxiv.org/abs/2608.28437) | ⭐⭐⭐ |
| Instruct-to-Act | Decoupling Planning and Control for Instructable Agents. | [arXiv](https://arxiv.org/abs/2608.26788) · [Project](https://zinengtang.github.io/) | ⭐⭐⭐ |
| R³ | R³: Training Robots to Reason in Natural Language via Reinforcement Learning. | [arXiv](https://arxiv.org/abs/2608.26053) · [Project](https://robotic-reasoner.github.io/) | ⭐⭐⭐ |
| PonderPounce | PonderPounce: A Pretrained MLLM as an Episode Context Engine for Robot Control. | [arXiv](https://arxiv.org/abs/2608.24115) · [Project](https://worv-ai.github.io/) | ⭐⭐⭐ |
| Physical Agentic AI | Physical Agentic AI: An Architecture for Orchestrating a Robot Crew with LLMs. | [arXiv](https://arxiv.org/abs/2608.22657) | ⭐⭐⭐ |
| Beyond Imitation | Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning. | [arXiv](https://arxiv.org/abs/2608.21204) · [Project](https://varungiridhar.github.io/) | ⭐⭐⭐ |

## Surveys and Definitions ![Updated](https://img.shields.io/badge/Updated-2026--08--22-0A7F5A?labelColor=333333)

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| Embodied Brains Roadmap | From World Action Models to Embodied Brains: A Roadmap for Open-World Physical Intelligence. | [arXiv](https://arxiv.org/abs/2607.11689) | ⭐⭐⭐ |
| VLA Review: UAV and Bimanual | Vision Language Action (VLA) Models for Unmanned Aerial Robotics and Bimanual Manipulation: A Review. | [arXiv](https://arxiv.org/abs/2607.06706) | ⭐⭐⭐ |
| World Action Models Tutorial | From World Models to World Action Models: A Concise Tutorial for Robotics. | [arXiv](https://arxiv.org/abs/2607.00836) · [Website](https://clearlab-sustech.github.io/WorldModelSurvey/) · [Code](https://github.com/clearlab-sustech/WorldModelSurvey) | ⭐⭐⭐ |
| World Model for Robot Learning | World Model for Robot Learning: A Comprehensive Survey. | [arXiv](https://arxiv.org/abs/2605.00080) · [Website](https://ntumars.github.io/wm-robot-survey/) · [Code](https://github.com/NTUMARS/Awesome-World-Model-for-Robotics-Policy) | ⭐⭐⭐ |
| Embodied Agentic AI | Towards Embodied Agentic AI: Review and Classification of LLM- and VLM-Driven Robot Autonomy and Interaction. | [arXiv](https://arxiv.org/abs/2508.05294) | ⭐⭐⭐ |

## World Action Models ![Updated](https://img.shields.io/badge/Updated-2026--09--07-0A7F5A?labelColor=333333)

Full archive: [World Action Models](WORLD_ACTION_MODELS.md).

### Video-Generation-Based WAM ![Updated](https://img.shields.io/badge/Updated-2026--09--07-0A7F5A?labelColor=333333)

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| TacPAC | TacPAC: Tactile Prediction and Real-Time Action Correction in World-Action Models for Contact-Rich Manipulation. | [arXiv](https://arxiv.org/abs/2609.05266) · [Code](https://github.com/LogosRoboticsGroup/TacPAC) | ⭐⭐⭐ |
| SV-WAM | SV-WAM: An Efficient Surround-View World-Action Model for End-to-End Autonomous Driving. | [arXiv](https://arxiv.org/abs/2609.03602) | ⭐⭐⭐ |
| SA-WAM | Spatially Aware World Action Model via Geometric Latent Diffusion. | [arXiv](https://arxiv.org/abs/2609.02531) | ⭐⭐⭐ |
| IMPACT | IMPACT: Attention Is the Interaction Map for Scalable Interaction-Aware World Model Training. | [arXiv](https://arxiv.org/abs/2609.00161) | ⭐⭐⭐ |
| AcrossVAM1.0 | AcrossVAM1.0: Particle World Modeling for Text-Assisted Robot Video Prediction. | [arXiv](https://arxiv.org/abs/2608.28491) | ⭐⭐⭐ |
| CLAP | CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators. | [arXiv](https://arxiv.org/abs/2608.27406) · [Project](https://omni-clap.github.io/) | ⭐⭐⭐ |
| Zero-WAM | Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization. | [arXiv](https://arxiv.org/abs/2608.26103) · [Project](https://robbyant-research.github.io/) | ⭐⭐⭐ |
| WorldSync | Do Robotic World Models Really Follow Actions? Diagnosing and Aligning Action-Conditioned Generation for Policy Learning. | [arXiv](https://arxiv.org/abs/2608.24885) | ⭐⭐⭐ |
| Surgical WAM | Surgical WAM: A World-Action Model for Data-Efficient Surgical Robot Learning. | [arXiv](https://arxiv.org/abs/2608.11204) | ⭐⭐⭐ |
| SimWAM | SimWAM: A Simple World Action Model for End-to-End Autonomous Driving. | [arXiv](https://arxiv.org/abs/2608.07468) · [Code](https://github.com/H-EmbodVis/SimWAM/) | ⭐⭐⭐ |

### VLM-Based WAM ![Updated](https://img.shields.io/badge/Updated-2026--08--24-0A7F5A?labelColor=333333)

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| ForeTime-VLA | ForeTime-VLA: Causal Future-Token Distillation from a World Action Model for Conveyor-Belt Manipulation. | [arXiv](https://arxiv.org/abs/2608.20735) | ⭐⭐⭐ |
| HyWorldVLA | HyWorldVLA: A Vision-Language-Action Model with Hybrid World Modeling for Autonomous Driving. | [arXiv](https://arxiv.org/abs/2607.20988) | ⭐⭐⭐ |
| DSWAM | DSWAM: A Dual-System World Action Foundation Model for Fine-Grained Robot Manipulation. | [arXiv](https://arxiv.org/abs/2607.04927) | ⭐⭐⭐ |
| FutureNav | FutureNav: Unified World-Action Modeling for Vision-and-Language Navigation. | [arXiv](https://arxiv.org/abs/2606.30367) | ⭐⭐⭐ |
| WLA | World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis. | [arXiv](https://arxiv.org/abs/2606.05979) · [Website](https://github.com/SJTU-DENG-Lab/WLA) | ⭐⭐⭐ |
| CKT-WAM | CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models. | [arXiv](https://arxiv.org/abs/2605.06247) · [Website](https://github.com/YuhuaJiang2002/CKT-WAM) | ⭐⭐ |
| World-Value-Action Model | World-Value-Action Model: Implicit Planning for Vision-Language-Action Systems. | [arXiv](https://arxiv.org/abs/2604.14732) | ⭐⭐⭐ |
| WoG | World Guidance World Modeling in Condition Space for Action Generation. | [arXiv](https://arxiv.org/abs/2602.22010) · [Website](https://selen-suyue.github.io/WoGNet/) | ⭐⭐ |
| VLAW | VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model. | [arXiv](https://arxiv.org/abs/2602.12063) · [Website](https://sites.google.com/view/vlaw-arxiv) | ⭐⭐⭐ |
| VLA-JEPA | VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model. | [arXiv](https://arxiv.org/abs/2602.10098) · [Website](https://ginwind.github.io/VLA-JEPA/) | ⭐⭐⭐ |

### WAM from Scratch and Latent Dynamics ![Updated](https://img.shields.io/badge/Updated-2026--09--01-0A7F5A?labelColor=333333)

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| PAVE | PAVE: Predictive Alignment and Value-Guided Evolution for World-Action Policies. | [arXiv](https://arxiv.org/abs/2608.30378) | ⭐⭐⭐ |
| GeoWAM | GeoWAM: Visual Geometry World Action Models for Autonomous Driving. | [arXiv](https://arxiv.org/abs/2608.23486) | ⭐⭐⭐ |
| DECOWAM | DECOWAM: Decoupled Whole-Body World-Action Model for Legged Mobile Manipulation. | [arXiv](https://arxiv.org/abs/2608.20114) | ⭐⭐⭐ |
| DA-WAM | DA-WAM: Decision-Aligned Future Latents for Driving World Models. | [arXiv](https://arxiv.org/abs/2608.19085) | ⭐⭐⭐ |
| Hydra-0 | Hydra-0: Action Flow for Generalist World Modeling and Control. | [arXiv](https://arxiv.org/abs/2608.18077) · [Project](https://nvidia-isaac.github.io/video_to_data/hydra-0/) | ⭐⭐⭐ |
| ContactGuard | ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models. | [arXiv](https://arxiv.org/abs/2608.13438) | ⭐⭐⭐ |
| RIFT | Keep the Future, Drop the Rollout: RIFT for World Action Models. | [arXiv](https://arxiv.org/abs/2608.11521) | ⭐⭐⭐ |
| HarnessWAM | HarnessWAM: Bridging Prediction and Deliberation in World Action Models. | [arXiv](https://arxiv.org/abs/2608.09516) | ⭐⭐⭐ |
| ω-0 | ω-0: A Latent Predictive World Action Model for Concurrent Humanoid Loco-Manipulation. | [arXiv](https://arxiv.org/abs/2608.06375) | ⭐⭐⭐ |
| LiLa-WAM | LiLa-WAM: Lightweight Latent Reasoning World-Action Model for Robotic Manipulation. | [arXiv](https://arxiv.org/abs/2608.03701) | ⭐⭐⭐ |

## VLA Failure Detection and Correction ![Updated](https://img.shields.io/badge/Updated-2026--09--04-0A7F5A?labelColor=333333)

Full archive: [VLA Failure Detection and Correction](VLA_FAILURE_DETECTION_AND_CORRECTION.md).

These papers are useful entry points for failure-aware VLA systems, especially
when the method uses feedback, online adaptation, closed-loop correction,
self-evaluation, or policy/world-model co-improvement.

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| FWBC-VLA | FWBC-VLA: Force-Aware Whole-Body Compensation for Contact-Rich Loco-Manipulation. | [arXiv](https://arxiv.org/abs/2609.03889) | ⭐⭐⭐ |
| CorrectVLA | Training-Free Action Correction for VLA Model Failures via Language Feedback. | [arXiv](https://arxiv.org/abs/2608.29967) · [Project](https://correctvla.github.io) | ⭐⭐⭐ |
| GRAFT | GRAFT: Grounded and Efficient Online Reinforcement Adaptation for Fine-Grained Robot Manipulation. | [arXiv](https://arxiv.org/abs/2608.27079) | ⭐⭐⭐ |
| TacForcing | TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback. | [arXiv](https://arxiv.org/abs/2608.25798) | ⭐⭐⭐ |
| TOWN-VLA | Think Only When Needed: Prompt-Authority Control for Selective Slow-Path Intervention in Vision-Language-Action Manipulation. | [arXiv](https://arxiv.org/abs/2608.23224) | ⭐⭐⭐ |
| SafeBranch | SafeBranch: Branch-Pair Safety Alignment for Embodied Agents. | [arXiv](https://arxiv.org/abs/2608.19729) | ⭐⭐⭐ |
| GS-VLA | GS-VLA: Plug-and-Play Viewpoint Canonicalization for Frozen VLA Policies via Gaussian Splatting. | [arXiv](https://arxiv.org/abs/2608.19066) | ⭐⭐⭐ |
| Calibrated Predictive Safety | Calibrated Predictive Safety for Heterogeneous Robots: An Action-Conditioned JEPA Framework with Model-Based Safety Shields. | [arXiv](https://arxiv.org/abs/2608.17496) | ⭐⭐⭐ |
| ViTaR | ViTaR: Visuo-Tactile Residual Adaptation for Foundation VLA Manipulation. | [arXiv](https://arxiv.org/abs/2608.15816) | ⭐⭐⭐ |
| Decoding Task Progress | Decoding Task Progress from VLA Representations. | [arXiv](https://arxiv.org/abs/2608.13474) | ⭐⭐⭐ |

## Efficient VLA ![Updated](https://img.shields.io/badge/Updated-2026--09--07-0A7F5A?labelColor=333333)

Full archive: [Efficient VLA](EFFICIENT_VLA.md).

### Compression, Adaptation, and Model Merging ![Updated](https://img.shields.io/badge/Updated-2026--08--31-0A7F5A?labelColor=333333)

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| Beyond Data Scaling | Beyond Data Scaling: Representation-Centric Continued Pre-training for Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2608.27550) · [Project](https://starvla.github.io/) | ⭐⭐⭐ |
| GVLA | Gripper-aware Vision Language Action Models. | [arXiv](https://arxiv.org/abs/2608.24603) | ⭐⭐⭐ |
| Action-JND | Just Noticeable Difference Modeling for Token Compression in Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2608.21247) | ⭐⭐⭐ |
| BridgeVLA++ | BridgeVLA++: A Data-Efficient, Generalizable, and Memory-Augmented Vision-Language-Action Framework for 3D Manipulation. | [arXiv](https://arxiv.org/abs/2608.05042) · [Code](https://github.com/BridgeVLA/BridgeVLA) | ⭐⭐⭐ |
| VQVLA | A Motion-Aware Vector Quantization Framework with Centroid Reuse for Efficient VLA Inference. | [arXiv](https://arxiv.org/abs/2607.24148) | ⭐⭐⭐ |
| DEED | Closing the Lab-to-Store Gap: A Data-Efficient Post-Training and Experience-Driven Learning VLA Framework for Retail Humanoids. | [arXiv](https://arxiv.org/abs/2607.20345) | ⭐⭐⭐ |
| Offline Supervision RL | Leveraging Offline Supervision for Efficient and Generalizable Reinforcement Learning in Large-Scale Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2607.19399) · [Project](https://alstar8.github.io/offline-supervision-vla-rl) | ⭐⭐⭐ |
| LifelongVLA | Towards Human-like Physical Intelligence: LifelongVision-Language-Action Learning for Robotic Manipulation. | [arXiv](https://arxiv.org/abs/2607.14852) | ⭐⭐⭐ |
| ExToken | ExToken: Structured Exploration for Efficient Vision-Language-Action Reinforcement Fine-tuning. | [arXiv](https://arxiv.org/abs/2607.12931) | ⭐⭐ |
| Z-1 | Z-1: Efficient Reinforcement Learning for Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2606.31846) | ⭐⭐ |

### Tokenization, Fine-Tuning, and Deployment-Friendly VLAs ![Updated](https://img.shields.io/badge/Updated-2026--09--07-0A7F5A?labelColor=333333)

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| LSS | Reasoning Without Inference Cost: Latent Semantic Scaffolding for Robot VLA Policies. | [arXiv](https://arxiv.org/abs/2609.04893) | ⭐⭐⭐ |
| LaPla | Continuous Actions from Discrete Minds: Latent-Aligned Planning for End-to-End Autonomous Driving. | [arXiv](https://arxiv.org/abs/2609.04070) | ⭐⭐⭐ |
| Adaptive Action Chunking | Knowing When to Stop: Adaptive Action Chunking via Internal Cross-Attention Dynamics in VLAs. | [arXiv](https://arxiv.org/abs/2609.00908) | ⭐⭐⭐ |
| DriftingVLA | DriftingVLA: Native One-Step Vision-Language-Action Generation via Per-Dimension Temporal Drifting. | [arXiv](https://arxiv.org/abs/2608.29749) | ⭐⭐⭐ |
| FlashVLA | FlashVLA: Streaming Action Decoding for Fast and Asynchronous VLA Inference. | [arXiv](https://arxiv.org/abs/2608.27384) | ⭐⭐⭐ |
| StreamPI | StreamPI: Streaming Multimodal Temporal Modeling for Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2608.26067) | ⭐⭐⭐ |
| Pointing-VLA | Pointing-VLA: Typed Spatial Grounding Interfaces for Vision-Language-Action Manipulation. | [arXiv](https://arxiv.org/abs/2608.23138) | ⭐⭐⭐ |
| EXIMO | EXIMO: VLM Guided Exploration of VLA Policies. | [arXiv](https://arxiv.org/abs/2608.19891) | ⭐⭐⭐ |
| Prism-GRPO | Prism-GRPO: Faster VLA Policy Optimization via Splitting Same-outcome Groups. | [arXiv](https://arxiv.org/abs/2608.17423) | ⭐⭐⭐ |
| HAF | HAF: Adapting Generalist VLAs to Humanoid Whole-Body Loco-manipulation via Hierarchical Action Flow and Spectral Latent RL. | [arXiv](https://arxiv.org/abs/2608.16837) · [Website](https://grange007.github.io/) | ⭐⭐⭐ |

## Benchmarks for Robustness and Evaluation ![Updated](https://img.shields.io/badge/Updated-2026--08--22-0A7F5A?labelColor=333333)

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

For every curated update, keep the primary Codex author and add
`Co-authored-by: wangskyone <wangskyone@users.noreply.github.com>` to the
commit message.

## Acknowledgements

Initial paper entries were reorganized from
[DravenALG/awesome-vla-wam](https://github.com/DravenALG/awesome-vla-wam).
