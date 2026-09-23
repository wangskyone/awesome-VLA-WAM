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

## Agentic Robotics (New Trend) ![Updated](https://img.shields.io/badge/Updated-2026--09--23-0A7F5A?labelColor=333333)

Full archive: [Agentic Robotics](AGENTIC_ROBOTICS.md).

This emerging line treats robot foundation models as components inside a
broader embodied-agent loop. Papers belong here only when the agent layer is
central to coordinating physical multi-step execution through planning,
memory, tool or skill composition, policy orchestration, recovery, or online
self-improvement; pure navigation-only or VLN policies are out of scope.

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| Local Coding Agent | Generalizing Manipulation Skills with a Local Coding Agent. | [arXiv](https://arxiv.org/abs/2609.26499) | ⭐⭐⭐ |
| GLIDE | Learning Beyond What Humans Can Demonstrate. | [arXiv](https://arxiv.org/abs/2609.24996) · [Project](https://guardrail-policy.github.io/) | ⭐⭐⭐ |
| AgenticSwarm | AgenticSwarm: Semantic Perception and Adaptive Task Allocation for Heterogeneous Multi-UAV Missions. | [arXiv](https://arxiv.org/abs/2609.21716) | ⭐⭐⭐ |
| SafeHarness | Coding Agents with an Obstacle-Aware Harness for Safe Robot Manipulation. | [arXiv](https://arxiv.org/abs/2609.20822) | ⭐⭐⭐ |
| GPT-Policy | In-Context Robot Learning with VLM Agents. | [arXiv](https://arxiv.org/abs/2609.19138) · [Project](https://cheng-haha.github.io/) | ⭐⭐⭐ |
| XPACE | XPACE: Joint World and Action Modeling from Heterogeneous Experience. | [arXiv](https://arxiv.org/abs/2609.17372) | ⭐⭐⭐ |
| MessyMem | MessyMem: Learning-from-Doing Memory for Mobile Manipulation. | [arXiv](https://arxiv.org/abs/2609.15976) · [Project](https://messymem.github.io/) | ⭐⭐⭐ |
| DASL | Dual-Process Atomic Skill Learning: Decoupling Semantic Reasoning and Real-Time Control. | [arXiv](https://arxiv.org/abs/2607.10625) · [Code](https://github.com/Hatakekaka/DASL) | ⭐⭐⭐ |
| 2AM | 2AM: Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-Horizon Manipulation. | [arXiv](https://arxiv.org/abs/2609.11308) | ⭐⭐⭐ |
| Show-Harness | Show-Harness: Just a VLM Agent Can Play Robots. | [arXiv](https://arxiv.org/abs/2609.10522) · [Project](https://showlab.github.io) | ⭐⭐⭐ |

## Surveys and Definitions ![Updated](https://img.shields.io/badge/Updated-2026--08--22-0A7F5A?labelColor=333333)

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| Embodied Brains Roadmap | From World Action Models to Embodied Brains: A Roadmap for Open-World Physical Intelligence. | [arXiv](https://arxiv.org/abs/2607.11689) | ⭐⭐⭐ |
| VLA Review: UAV and Bimanual | Vision Language Action (VLA) Models for Unmanned Aerial Robotics and Bimanual Manipulation: A Review. | [arXiv](https://arxiv.org/abs/2607.06706) | ⭐⭐⭐ |
| World Action Models Tutorial | From World Models to World Action Models: A Concise Tutorial for Robotics. | [arXiv](https://arxiv.org/abs/2607.00836) · [Website](https://clearlab-sustech.github.io/WorldModelSurvey/) · [Code](https://github.com/clearlab-sustech/WorldModelSurvey) | ⭐⭐⭐ |
| World Model for Robot Learning | World Model for Robot Learning: A Comprehensive Survey. | [arXiv](https://arxiv.org/abs/2605.00080) · [Website](https://ntumars.github.io/wm-robot-survey/) · [Code](https://github.com/NTUMARS/Awesome-World-Model-for-Robotics-Policy) | ⭐⭐⭐ |
| Embodied Agentic AI | Towards Embodied Agentic AI: Review and Classification of LLM- and VLM-Driven Robot Autonomy and Interaction. | [arXiv](https://arxiv.org/abs/2508.05294) | ⭐⭐⭐ |

## World Action Models ![Updated](https://img.shields.io/badge/Updated-2026--09--23-0A7F5A?labelColor=333333)

Full archive: [World Action Models](WORLD_ACTION_MODELS.md).

### Video-Generation-Based WAM ![Updated](https://img.shields.io/badge/Updated-2026--09--14-0A7F5A?labelColor=333333)

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| CLAP | CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators. | [arXiv](https://arxiv.org/abs/2608.27406) · [Project](https://omni-clap.github.io/) | ⭐⭐⭐ |
| TacPAC | TacPAC: Tactile Prediction and Real-Time Action Correction in World-Action Models for Contact-Rich Manipulation. | [arXiv](https://arxiv.org/abs/2609.05266) · [Code](https://github.com/LogosRoboticsGroup/TacPAC) | ⭐⭐⭐ |
| SV-WAM | SV-WAM: An Efficient Surround-View World-Action Model for End-to-End Autonomous Driving. | [arXiv](https://arxiv.org/abs/2609.03602) | ⭐⭐⭐ |
| SA-WAM | Spatially Aware World Action Model via Geometric Latent Diffusion. | [arXiv](https://arxiv.org/abs/2609.02531) | ⭐⭐⭐ |
| IMPACT | IMPACT: Attention Is the Interaction Map for Scalable Interaction-Aware World Model Training. | [arXiv](https://arxiv.org/abs/2609.00161) | ⭐⭐⭐ |
| AcrossVAM1.0 | AcrossVAM1.0: Particle World Modeling for Text-Assisted Robot Video Prediction. | [arXiv](https://arxiv.org/abs/2608.28491) | ⭐⭐⭐ |
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

### WAM from Scratch and Latent Dynamics ![Updated](https://img.shields.io/badge/Updated-2026--09--23-0A7F5A?labelColor=333333)

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| PatchWAM | An Action Is Worth One Patch: Unified World-Action Modeling with PatchWAM. | [arXiv](https://arxiv.org/abs/2609.25961) | ⭐⭐⭐ |
| DexTacWAM | DexTacWAM: A Visuo-Tactile World-Action Model for Dexterous Manipulation. | [arXiv](https://arxiv.org/abs/2609.24976) · [Project](https://dextacwam.github.io/) | ⭐⭐⭐ |
| SkelWAM | SkelWAM: A Skeleton-Guided World-Action Model for Zero-Shot Cross-Embodiment Manipulation. | [arXiv](https://arxiv.org/abs/2609.21983) · [Project](http://www.liukepku.com/skelwam/index.html) | ⭐⭐⭐ |
| Agile-WAM | Agile-WAM: An Agile Tactile World Action Model for Contact-Rich Robot Control. | [arXiv](https://arxiv.org/abs/2609.20761) · [Project](https://hanchuzhou.github.io/TARO_project_page/) | ⭐⭐⭐ |
| CSWAM | CSWAM: Better Causal Semantic Representations for Out-of-Distribution Generalization in World Action Models. | [arXiv](https://arxiv.org/abs/2609.18462) | ⭐⭐⭐ |
| ModAR | Modality-Autoregressive World-Action Models. | [arXiv](https://arxiv.org/abs/2609.17524) · [Project](https://adamhung60.github.io/) | ⭐⭐⭐ |
| WLA³ | WLA³: World Latent Action Modeling for Semantics, Dynamics, and Kinematics. | [arXiv](https://arxiv.org/abs/2609.15870) · [Project](https://wla-3.github.io/) | ⭐⭐⭐ |
| Dynin-Robotics | Dynin-Robotics: Omnimodal Unified Diffusion Vision-Language-Action Model. | [arXiv](https://arxiv.org/abs/2609.13053) · [Project](https://dynin.ai/robotics/) · [Code](https://github.com/AIDASLab/Dynin-Robotics) | ⭐⭐⭐ |
| Motus2 | Motus2: A Self-Evolving General World Model for Dexterous Manipulation. | [arXiv](https://arxiv.org/abs/2608.30237) · [Project](https://motus-robotics.github.io/motus2) | ⭐⭐⭐ |
| MaP-WAM | Memory as Plans: World-Action Modeling with Memory-Grounded Planning. | [arXiv](https://arxiv.org/abs/2609.11561) · [Project](https://sizhezhao.github.io/) | ⭐⭐⭐ |

## VLA Failure Detection and Correction ![Updated](https://img.shields.io/badge/Updated-2026--09--23-0A7F5A?labelColor=333333)

Full archive: [VLA Failure Detection and Correction](VLA_FAILURE_DETECTION_AND_CORRECTION.md).

These papers are useful entry points for failure-aware VLA systems, especially
when the method uses feedback, online adaptation, closed-loop correction,
self-evaluation, or policy/world-model co-improvement.

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| RouteRLT | RouteRLT: Learning When and Which RL Specialist Should Control a Vision-Language-Action Policy. | [arXiv](https://arxiv.org/abs/2609.26467) | ⭐⭐⭐ |
| CARE | CARE: Experience-Guided Atomic Corrective Execution for Vision-Language-Action Policies. | [arXiv](https://arxiv.org/abs/2609.24118) · [Code](https://github.com/xiaojunlan/care) | ⭐⭐⭐ |
| CommitFlow | CommitFlow: Semantic Commitment Verification and Local Correction for Long-Horizon Robot Manipulation VLA Execution. | [arXiv](https://arxiv.org/abs/2609.21908) | ⭐⭐⭐ |
| TraceFlow | Guiding Frozen Flow-Matching Robot Policies with Success and Failure Traces. | [arXiv](https://arxiv.org/abs/2609.20646) | ⭐⭐⭐ |
| DistAL | DistAL: Distance-based Advantage Learning for VLA Fine-Tuning. | [arXiv](https://arxiv.org/abs/2609.18392) | ⭐⭐⭐ |
| MoSS | Modular Sensory Stream for Integrating Physical Feedback in Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2604.23272) · [Project](https://jiminlx.github.io/MoSS/) | ⭐⭐⭐ |
| ActSafeGuard | ActSafeGuard: Differentiable and Training-Aligned Constraint Enforcement for Flow-Matching Policies. | [arXiv](https://arxiv.org/abs/2609.11697) | ⭐⭐⭐ |
| VLA-Corrector | VLA-Corrector: Stage-Aware Observable State Understanding for Prompt-Based Closed-Loop Recovery of Vision-Language-Action Policies. | [arXiv](https://arxiv.org/abs/2609.06508) | ⭐⭐⭐ |
| FWBC-VLA | FWBC-VLA: Force-Aware Whole-Body Compensation for Contact-Rich Loco-Manipulation. | [arXiv](https://arxiv.org/abs/2609.03889) | ⭐⭐⭐ |
| CorrectVLA | Training-Free Action Correction for VLA Model Failures via Language Feedback. | [arXiv](https://arxiv.org/abs/2608.29967) · [Project](https://correctvla.github.io) | ⭐⭐⭐ |

## Efficient VLA ![Updated](https://img.shields.io/badge/Updated-2026--09--23-0A7F5A?labelColor=333333)

Full archive: [Efficient VLA](EFFICIENT_VLA.md).

### Compression, Adaptation, and Model Merging ![Updated](https://img.shields.io/badge/Updated-2026--09--23-0A7F5A?labelColor=333333)

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| ε4P | Imperfection for Precision: Upcycling Imperfect Data for High-Precision Robotic Manipulation. | [arXiv](https://arxiv.org/abs/2609.26672) · [Project](https://varepsilon4p.github.io/) | ⭐⭐⭐ |
| AdaDE | Dense to MoE Adaptation for Compact Vision Language Action Policies. | [arXiv](https://arxiv.org/abs/2609.16503) | ⭐⭐⭐ |
| Beyond Data Scaling | Beyond Data Scaling: Representation-Centric Continued Pre-training for Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2608.27550) · [Project](https://starvla.github.io/) | ⭐⭐⭐ |
| GVLA | Gripper-aware Vision Language Action Models. | [arXiv](https://arxiv.org/abs/2608.24603) | ⭐⭐⭐ |
| Action-JND | Just Noticeable Difference Modeling for Token Compression in Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2608.21247) | ⭐⭐⭐ |
| BridgeVLA++ | BridgeVLA++: A Data-Efficient, Generalizable, and Memory-Augmented Vision-Language-Action Framework for 3D Manipulation. | [arXiv](https://arxiv.org/abs/2608.05042) · [Code](https://github.com/BridgeVLA/BridgeVLA) | ⭐⭐⭐ |
| VQVLA | A Motion-Aware Vector Quantization Framework with Centroid Reuse for Efficient VLA Inference. | [arXiv](https://arxiv.org/abs/2607.24148) | ⭐⭐⭐ |
| DEED | Closing the Lab-to-Store Gap: A Data-Efficient Post-Training and Experience-Driven Learning VLA Framework for Retail Humanoids. | [arXiv](https://arxiv.org/abs/2607.20345) | ⭐⭐⭐ |
| Offline Supervision RL | Leveraging Offline Supervision for Efficient and Generalizable Reinforcement Learning in Large-Scale Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2607.19399) · [Project](https://alstar8.github.io/offline-supervision-vla-rl) | ⭐⭐⭐ |
| LifelongVLA | Towards Human-like Physical Intelligence: LifelongVision-Language-Action Learning for Robotic Manipulation. | [arXiv](https://arxiv.org/abs/2607.14852) | ⭐⭐⭐ |

### Tokenization, Fine-Tuning, and Deployment-Friendly VLAs ![Updated](https://img.shields.io/badge/Updated-2026--09--22-0A7F5A?labelColor=333333)

| Paper | Title | Links | Relevance |
| --- | --- | --- | --- |
| Think Like a World Model | Think Like a World Model, Act Like a VLA: Distilling World-Model Representations into Compact Robot Policies. | [arXiv](https://arxiv.org/abs/2609.24682) · [Project](https://thaw-vla.trung-dt.com/) | ⭐⭐⭐ |
| Coda | Fewer Steps, Better Actions: Rethinking Flow-Matching Inference for VLA Policies. | [arXiv](https://arxiv.org/abs/2609.21216) | ⭐⭐⭐ |
| GeoAAC | GeoAAC: Geometry-Based Adaptive Action Chunking from Denoising Trajectories in VLA Policies. | [arXiv](https://arxiv.org/abs/2609.20776) | ⭐⭐⭐ |
| rMuscle | rMuscle: Robotic Muscle Memory for Efficient Vision-Language-Action Model Inference. | [arXiv](https://arxiv.org/abs/2609.19104) | ⭐⭐⭐ |
| DiffAdapterVLA | Planning in the Backbone: DiffAdapterVLA for Native Continuous Trajectory Generation with Driving VLMs. | [arXiv](https://arxiv.org/abs/2609.15322) | ⭐⭐⭐ |
| Dynin-Robotics | Dynin-Robotics: Omnimodal Unified Diffusion Vision-Language-Action Model. | [arXiv](https://arxiv.org/abs/2609.13053) · [Project](https://dynin.ai/robotics/) · [Code](https://github.com/AIDASLab/Dynin-Robotics) | ⭐⭐⭐ |
| IMLE-VLA | IMLE-VLA: Fast Single-Step Action Generation for Vision-Language-Action Policies. | [arXiv](https://arxiv.org/abs/2609.10915) · [Project](https://kianhk6.github.io/) | ⭐⭐⭐ |
| ComVLA | ComVLA: Communication-Aware Split Inference for VLA Models in 6G-Connected Robotics. | [arXiv](https://arxiv.org/abs/2609.07838) | ⭐⭐⭐ |
| LSS | Reasoning Without Inference Cost: Latent Semantic Scaffolding for Robot VLA Policies. | [arXiv](https://arxiv.org/abs/2609.04893) | ⭐⭐⭐ |
| LaPla | Continuous Actions from Discrete Minds: Latent-Aligned Planning for End-to-End Autonomous Driving. | [arXiv](https://arxiv.org/abs/2609.04070) | ⭐⭐⭐ |

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
