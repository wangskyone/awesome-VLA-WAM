# Awesome VLA-WAM

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated reading list for Vision-Language-Action (VLA), World Action Model
(WAM), and agentic robotics research, organized around four active directions:

- Agentic robotics for long-horizon embodied agents, tool use, reusable skill
  libraries, and policy self-improvement.
- World Action Models for robotics.
- Failure detection, correction, feedback, and recovery in VLA systems.
- Efficient VLA models, action tokenization, compression, and deployment.

<p align="center">
  <img src="assets/awesome-vla-wam-hero.png" alt="Awesome VLA-WAM hero image" width="100%">
</p>

This seed list was extracted from
[DravenALG/awesome-vla-wam](https://github.com/DravenALG/awesome-vla-wam)
and reorganized around the four directions above. The agentic robotics section
highlights a new trend where robot foundation models are embedded inside
broader agent loops for planning, tool use, self-improvement, and long-horizon
execution. The failure
detection/correction section is not a one-to-one heading in the source
repository; it groups papers that are closely related through environment
feedback, self-improvement, verification, closed-loop learning, preference
alignment, online planning, or robustness evaluation.

## Contents

- [Agentic Robotics (New Trend)](#agentic-robotics-new-trend)
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

## Agentic Robotics (New Trend) ![Updated](https://img.shields.io/badge/Updated-2026--07--02-0A7F5A?labelColor=333333)

This emerging line treats robot foundation models as components inside a
broader agent loop, combining high-level planning, tool use, reusable skill
libraries, policy self-improvement, and long-horizon execution.

| Paper | Title | Links |
| --- | --- | --- |
| ASPIRE | ASPIRE: Agentic /Skills Discovery for Robotics. | [arXiv](https://arxiv.org/abs/2607.00272) · [Website](https://research.nvidia.com/labs/gear/aspire/) |
| Analytic Concept-Centric Memory | Analytic Concept-Centric Memory for Agentic Embodied Manipulation. | [arXiv](https://arxiv.org/abs/2606.29774) |
| OmniAct | Advancing Omnimodal Embodied Agents from Isolated Skills to Everyday Physical Autonomy. | [arXiv](https://arxiv.org/abs/2606.27251) |
| RAVEN | RAVEN: Long-Horizon Reasoning & Navigation with a Visuo-Spatio-Temporal Memory for Robotics. | [arXiv](https://arxiv.org/abs/2606.25206) |
| HoloAgent-0 | HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory. | [arXiv](https://arxiv.org/abs/2606.23565) · [Code](https://github.com/HorizonRobotics/HoloAgent) |
| ENPIRE | ENPIRE: Agentic Robot Policy Self-Improvement in the Real World. | [arXiv](https://arxiv.org/abs/2606.19980) |
| Playful Agentic Robot Learning | Playful Agentic Robot Learning. | [arXiv](https://arxiv.org/abs/2606.19419) · [Website](https://playful-rats.github.io/) |
| Qwen-RobotNav | Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System. | [arXiv](https://arxiv.org/abs/2606.18112) · [Website](https://qwen.ai/blog?id=qwen-robotnav) |
| FCGraft | Functional Cache Grafting: Robust and Rapid Code-Policy Synthesis for Embodied Agents. | [arXiv](https://arxiv.org/abs/2606.13097) |
| Embodied-R1.5 | Embodied-R1.5: Evolving Physical Intelligence via Embodied Foundation Models. | [arXiv](https://arxiv.org/abs/2606.11324) · [Website](https://embodied-r1.github.io/) · [Code](https://github.com/Embodied-R1/Embodied-R1) |

## Surveys and Definitions ![Updated](https://img.shields.io/badge/Updated-2026--07--02-0A7F5A?labelColor=333333)

| Paper | Title | Links |
| --- | --- | --- |
| From World Models to World Action Models | From World Models to World Action Models: A Concise Tutorial for Robotics. | [arXiv](https://arxiv.org/abs/2607.00836) · [Website](https://clearlab-sustech.github.io/WorldModelSurvey/) · [Code](https://github.com/clearlab-sustech/WorldModelSurvey) |
| World Action Models: The Next Frontier in Embodied AI. | World Action Models: The Next Frontier in Embodied AI. | [arXiv](https://arxiv.org/abs/2605.12090) · [Website](https://openmoss.github.io) |
| DreamZero | World Action Models are Zero-shot Policies. | [arXiv](https://arxiv.org/abs/2602.15922) · [Website](https://dreamzero0.github.io) |
| Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges. | Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges. | [arXiv](https://arxiv.org/abs/2505.04769) · [Website](https://github.com/Applied-AI-Research-Lab/Vision-Language-Action-Models-Concepts-Progress-Applications-and-Challenges) |
| A Survey on Vision-Language-Action Models for Embodied AI. | A Survey on Vision-Language-Action Models for Embodied AI. | [arXiv](https://arxiv.org/abs/2405.14093) · [Website](https://github.com/yueen-ma/Awesome-VLA) |
| RT-2 | RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control. | [arXiv](https://arxiv.org/abs/2307.15818) · [Website](https://robotics-transformer2.github.io) |

## World Action Models ![Updated](https://img.shields.io/badge/Updated-2026--07--01-0A7F5A?labelColor=333333)

Full archive: [World Action Models](WORLD_ACTION_MODELS.md).

### Video-Generation-Based WAM ![Updated](https://img.shields.io/badge/Updated-2026--07--01-0A7F5A?labelColor=333333)

| Paper | Title | Links |
| --- | --- | --- |
| SWAM | Pondering the Way: Spatial-perceiving World Action Model for Embodied Navigation. | [arXiv](https://arxiv.org/abs/2606.29908) |
| NavWM | NavWM: A Unified Navigation World Model for Foresight-Driven Planning. | [arXiv](https://arxiv.org/abs/2606.24101) |
| ImageWAM | ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing? | [arXiv](https://arxiv.org/abs/2606.19531) · [Website](https://zhangwenyao1.github.io/ImageWAM/) |
| Metis | Metis: A Generalizable and Efficient World-Action Model for Autonomous Driving and Urban Navigation. | [arXiv](https://arxiv.org/abs/2606.15869) |
| WAM4D | WAM4D: A Fast 4D World Action Model for Robotic Manipulation. | [arXiv](https://arxiv.org/abs/2606.14048) |
| MaskWAM | MaskWAM: Unifying Mask Prompting and Prediction for World-Action Models. | [arXiv](https://arxiv.org/abs/2606.13515) · [Website](https://hanyangyu1021.github.io/maskwam.github.io/) |
| NavWAM | NavWAM: A Navigation World Action Model for Goal-Conditioned Visual Navigation. | [arXiv](https://arxiv.org/abs/2606.13494) · [Website](https://dachii-azm.github.io/navwam/) |
| AGRA | Making Foresight Actionable: Repurposing Representation Alignment in World Action Models. | [arXiv](https://arxiv.org/abs/2606.12217) |
| AHA-WAM | AHA-WAM: Asynchronous Horizon-Adaptive World-Action Modeling with Observation-Guided Context Routing. | [arXiv](https://arxiv.org/abs/2606.09811) |
| OSCAR | OSCAR: Omni-Embodiment Skeleton-Conditioned World Action Model for Robotics. | [arXiv](https://arxiv.org/abs/2606.04463) |

### VLM-Based WAM ![Updated](https://img.shields.io/badge/Updated-2026--07--01-0A7F5A?labelColor=333333)

| Paper | Title | Links |
| --- | --- | --- |
| WLA | World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis. | [arXiv](https://arxiv.org/abs/2606.05979) · [Website](https://github.com/SJTU-DENG-Lab/WLA) |
| CKT-WAM | CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models. | [arXiv](https://arxiv.org/abs/2605.06247) · [Website](https://github.com/YuhuaJiang2002/CKT-WAM) |
| World-Value-Action Model | World-Value-Action Model: Implicit Planning for Vision-Language-Action Systems. | [arXiv](https://arxiv.org/abs/2604.14732) |
| WoG | World Guidance World Modeling in Condition Space for Action Generation. | [arXiv](https://arxiv.org/abs/2602.22010) · [Website](https://selen-suyue.github.io/WoGNet/) |
| VLAW | VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model. | [arXiv](https://arxiv.org/abs/2602.12063) · [Website](https://sites.google.com/view/vlaw-arxiv) |
| VLA-JEPA | VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model. | [arXiv](https://arxiv.org/abs/2602.10098) · [Website](https://ginwind.github.io/VLA-JEPA/) |
| MM-ACT | MM-ACT: Learn from Multimodal Parallel Generation to Act. | [arXiv](https://arxiv.org/abs/2512.00975) · [Website](https://github.com/HHYHRHY/MM-ACT) |
| RynnVLA-002 | RynnVLA-002: A Unified Vision-Language-Action and World Model. | [arXiv](https://arxiv.org/abs/2511.17502) · [Website](https://github.com/alibaba-damo-academy/RynnVLA-002) |
| F1 | F1: A Vision-Language-Action Model Bridging Understanding and Generation to Actions. | [arXiv](https://arxiv.org/abs/2509.06951) · [Website](https://aopolin-lv.github.io/F1-VLA/) |
| FlowVLA | FlowVLA: Visual Chain of Thought-based Motion Reasoning for Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2508.18269) · [Website](https://irpn-lab.github.io/FlowVLA/) |

### WAM from Scratch and Latent Dynamics ![Updated](https://img.shields.io/badge/Updated-2026--07--01-0A7F5A?labelColor=333333)

| Paper | Title | Links |
| --- | --- | --- |
| Synthetic-Prior Sim-to-Real WAM | Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors. | [arXiv](https://arxiv.org/abs/2606.31101) |
| DIM-WAM | DIM-WAM: World-Action Modeling with Diverse Historical Event Memory. | [arXiv](https://arxiv.org/abs/2606.27677) · [Website](https://wangkai-casia.github.io/dim-wam/) |
| REGEN | World Action Models Enable Continual Imitation Learning with Recurrent Generative Replays. | [arXiv](https://arxiv.org/abs/2606.27374) |
| Tactile-WAM | Tactile-WAM: Touch-Aware World Action Model with Tactile Asymmetric Attention. | [arXiv](https://arxiv.org/abs/2606.26663) |
| MV-WAM | MV-WAM: Manifold-Aware World Action Model with Value Augmentation. | [arXiv](https://arxiv.org/abs/2606.21088) |
| MemoryWAM | MemoryWAM: Efficient World Action Modeling with Persistent Memory. | [arXiv](https://arxiv.org/abs/2606.20562) |
| Mem-World | Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation. | [arXiv](https://arxiv.org/abs/2606.18960) |
| WAM-RL | WAM-RL: World-Action Model Reinforcement Learning with Reconstruction Rewards and Online Video SFT. | [arXiv](https://arxiv.org/abs/2606.17906) |
| LaWAM | LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies. | [arXiv](https://arxiv.org/abs/2606.15768) · [Website](https://github.com/RLinf/LaWAM) |
| RepWAM | RepWAM: World Action Modeling with Representation Visual-Action Tokenizers. | [arXiv](https://arxiv.org/abs/2606.13674) · [Website](https://wdrink.github.io/RepWAM) |

## VLA Failure Detection and Correction ![Updated](https://img.shields.io/badge/Updated-2026--07--02-0A7F5A?labelColor=333333)

Full archive: [VLA Failure Detection and Correction](VLA_FAILURE_DETECTION_AND_CORRECTION.md).

These papers are useful entry points for failure-aware VLA systems, especially
when the method uses feedback, online adaptation, closed-loop correction,
self-evaluation, or policy/world-model co-improvement.

| Paper | Title | Links |
| --- | --- | --- |
| DART | Domain Arithmetic: One-Shot VLA Adaptation under Environmental Shifts. | [arXiv](https://arxiv.org/abs/2607.00666) · [Website](https://twkang43.github.io/projects/dart/) · [Code](https://github.com/snumprlab/dart) |
| PhysReflect-VLA | PhysReflect-VLA: Physical Feasibility and Self-Reflective Regulation for Reliable Vision-Language-Action Policies. | [arXiv](https://arxiv.org/abs/2606.27146) |
| ROAD-VLA | ROAD-VLA: Robust Online Adaptation via Self-Distillation for Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2606.25800) |
| RECALL | RECALL: Recovery Experience Collection for Active Lifelong Learning in Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2606.23617) |
| Tri-Info | Tri-Info: Generalizable, Interpretable Failure Prediction for VLA Models via Information Theory. | [arXiv](https://arxiv.org/abs/2606.19998) |
| VERITAS | Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement. | [arXiv](https://arxiv.org/abs/2606.18247) |
| SAVE | Uncertainty Quantification for Flow-Based Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2606.18043) · [Website](https://save-vla.github.io/) |
| DREAM-Chunk | DREAM-Chunk: Reactive Action Chunking with Latent World Model. | [arXiv](https://arxiv.org/abs/2606.17258) |
| ROVE | ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement Learning. | [arXiv](https://arxiv.org/abs/2606.17011) · [Website](https://xpeng-robotics.github.io/rove/) |
| Self-Improving VLA Policies | Self-Improving VLA Policies through Online Reinforcement Learning. | [arXiv](https://arxiv.org/abs/2606.14084) |

## Efficient VLA ![Updated](https://img.shields.io/badge/Updated-2026--07--02-0A7F5A?labelColor=333333)

Full archive: [Efficient VLA](EFFICIENT_VLA.md).

### Compression, Adaptation, and Model Merging ![Updated](https://img.shields.io/badge/Updated-2026--07--02-0A7F5A?labelColor=333333)

| Paper | Title | Links |
| --- | --- | --- |
| Parameter Redundancy in VLA | Revisiting Parameter Redundancy in Vision-Language-Action Models: Insights from VLM-to-VLA Adaptation. | [arXiv](https://arxiv.org/abs/2606.31382) · [Code](https://github.com/Niannnnnn/VLA_Parameter_Redundancy_VLM2VLA) |
| Mix-QVLA | Mix-QVLA: Task-Evidence-Aware Mixed-Precision Quantization of Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2606.19565) |
| Learned Image Compression | Learned Image Compression for Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2606.16253) |
| Omega-QVLA | Ω-QVLA: Robust Quantization for Vision-Language-Action Models via Composite Rotation and Per-step Scaling. | [arXiv](https://arxiv.org/abs/2605.28803) · [Website](https://github.com/UCMP13753/Omega-QVLA) |
| EXPO-FT | EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2605.25477) |
| ActQuant | ActQuant: Sub-4-bit Action-Guided Quantization for Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2605.24011) · [Website](https://actquant.github.io/) |
| Agentic-VLA | Agentic-VLA: Efficient Online Adaptation for Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2605.22896) |
| DA-PTQ | DA-PTQ: Drift-Aware Post-Training Quantization for Efficient Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2604.11572) |
| DyQ-VLA | DyQ-VLA: Temporal-Dynamic-Aware Quantization for Embodied Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2603.07904) |
| QuantVLA | QuantVLA: Scale-Calibrated Post-Training Quantization for Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2602.20309) · [Website](https://quantvla.github.io/) |

### Tokenization, Fine-Tuning, and Deployment-Friendly VLAs ![Updated](https://img.shields.io/badge/Updated-2026--07--01-0A7F5A?labelColor=333333)

| Paper | Title | Links |
| --- | --- | --- |
| SA-VLA | SA-VLA: State-aware tokenizer for improving Vision-Language-Action Models' performance. | [arXiv](https://arxiv.org/abs/2606.30113) |
| SpikeVLA | SpikeVLA: Vision-Language-Action Models with Spiking Neural Networks. | [arXiv](https://arxiv.org/abs/2606.27807) |
| FORCE | FORCE: Efficient VLA Reinforcement Fine-Tuning via Value-Calibrated Warm-up and Self-Distillation. | [arXiv](https://arxiv.org/abs/2606.26006) |
| Action ControlNet | Action ControlNet: A Lightweight Delay-Aware Adapter for Smooth Asynchronous Control in Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2606.25985) |
| UniFS | UniFS: Unified Fast-to-Slow Hierarchical Architecture for Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2606.22794) · [Code](https://github.com/linsun449/UniFS) |
| Fewer-Layer VLA Finetuning | Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think. | [arXiv](https://arxiv.org/abs/2606.20246) |
| Acting While Understanding | Acting While Understanding: Asynchronous Semantic-Action Decoupling for Real-Time Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2606.15285) |
| AVA-VLA | Think Less, Act Early: Reinforced Latent Reasoning with Early Exit in Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2606.15099) |
| X-Tokenizer | X-Tokenizer: A Multimodal Action Tokenizer for Vision-Language-Action Pretraining. | [arXiv](https://arxiv.org/abs/2606.14752) · [Website](https://x-square-robot.github.io/X-Tokenizer_projectPage/) |
| Output-Level Regularization | Output-Level Regularization Eliminates the Seed Lottery in Single-GPU VLA Fine-Tuning. | [arXiv](https://arxiv.org/abs/2606.13856) |

## Benchmarks for Robustness and Evaluation ![Updated](https://img.shields.io/badge/Updated-2026--07--01-0A7F5A?labelColor=333333)

| Paper | Title | Links |
| --- | --- | --- |
| WorldArena | WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models. | [arXiv](https://arxiv.org/abs/2602.08971) · [Website](https://world-arena.ai) |
| LIBERO-Plus | LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models. | [arXiv](https://arxiv.org/abs/2510.13626) · [Website](https://sylvestf.github.io/LIBERO-plus/) |
| RoboArena | RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies. | [arXiv](https://arxiv.org/abs/2506.18123) · [Website](https://robo-arena.github.io) |
| RoboTwin 2.0 | RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation. | [arXiv](https://arxiv.org/abs/2506.18088) · [Website](https://github.com/robotwin-Platform/robotwin/) |
| SimplerEnv | Evaluating Real-World Robot Manipulation Policies in Simulation. | [arXiv](https://arxiv.org/abs/2405.05941) · [Website](https://simpler-env.github.io) |
| LIBERO | LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning. | [arXiv](https://arxiv.org/abs/2306.03310) · [Website](https://libero-project.github.io/main.html) |

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
