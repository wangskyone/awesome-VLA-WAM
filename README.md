# Awesome VLA-WAM

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated reading list for Vision-Language-Action (VLA) and World Action Model
(WAM) research, with an emphasis on:

- World Action Models for robotics.
- Failure detection, correction, feedback, and recovery in VLA systems.
- Efficient VLA models, action tokenization, compression, and deployment.

<p align="center">
  <img src="assets/awesome-vla-wam-hero.png" alt="Awesome VLA-WAM hero image" width="100%">
</p>

This seed list was extracted from
[DravenALG/awesome-vla-wam](https://github.com/DravenALG/awesome-vla-wam)
and reorganized around the three directions above. The failure
detection/correction section is not a one-to-one heading in the source
repository; it groups papers that are closely related through environment
feedback, self-improvement, verification, closed-loop learning, preference
alignment, online planning, or robustness evaluation.

## Contents

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

## Surveys and Definitions ![Updated](https://img.shields.io/badge/Updated-2026--05--20-0A7F5A?labelColor=333333)

- **World Action Models: The Next Frontier in Embodied AI.** [![arXiv](https://img.shields.io/badge/arXiv-2605.12090-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.12090) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://openmoss.github.io)
- **RT-2**, RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control. [![arXiv](https://img.shields.io/badge/arXiv-2307.15818-b31b1b?labelColor=333333)](https://arxiv.org/abs/2307.15818) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://robotics-transformer2.github.io)
- **DreamZero**, World Action Models are Zero-shot Policies. [![arXiv](https://img.shields.io/badge/arXiv-2602.15922-b31b1b?labelColor=333333)](https://arxiv.org/abs/2602.15922) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://dreamzero0.github.io)
- **Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges.** [![arXiv](https://img.shields.io/badge/arXiv-2505.04769-b31b1b?labelColor=333333)](https://arxiv.org/abs/2505.04769) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://github.com/Applied-AI-Research-Lab/Vision-Language-Action-Models-Concepts-Progress-Applications-and-Challenges)
- **A Survey on Vision-Language-Action Models for Embodied AI.** [![arXiv](https://img.shields.io/badge/arXiv-2405.14093-b31b1b?labelColor=333333)](https://arxiv.org/abs/2405.14093) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://github.com/yueen-ma/Awesome-VLA)

## World Action Models ![Updated](https://img.shields.io/badge/Updated-2026--06--15-0A7F5A?labelColor=333333)

Full archive: [World Action Models](WORLD_ACTION_MODELS.md).

### Video-Generation-Based WAM ![Updated](https://img.shields.io/badge/Updated-2026--06--15-0A7F5A?labelColor=333333)

- **WAM4D**, WAM4D: A Fast 4D World Action Model for Robotic Manipulation. [![arXiv](https://img.shields.io/badge/arXiv-2606.14048-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.14048)
- **MaskWAM**, MaskWAM: Unifying Mask Prompting and Prediction for World-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2606.13515-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.13515) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://hanyangyu1021.github.io/maskwam.github.io/)
- **AGRA**, Making Foresight Actionable: Repurposing Representation Alignment in World Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2606.12217-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.12217)
- **AHA-WAM**, AHA-WAM: Asynchronous Horizon-Adaptive World-Action Modeling with Observation-Guided Context Routing. [![arXiv](https://img.shields.io/badge/arXiv-2606.09811-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.09811)
- **OSCAR**, OSCAR: Omni-Embodiment Skeleton-Conditioned World Action Model for Robotics. [![arXiv](https://img.shields.io/badge/arXiv-2606.04463-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.04463)
- **WorldVLN**, WorldVLN: Autoregressive World Action Model for Aerial Vision-Language Navigation. [![arXiv](https://img.shields.io/badge/arXiv-2605.15964-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.15964) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://embodiedcity.github.io/WorldVLN/)
- **HarmoWAM**, HarmoWAM: Harmonizing Generalizable and Precise Manipulation via Adaptive World Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2605.10942-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.10942)
- **NoiseGate**, NoiseGate: Learning Per-Latent Timestep Schedules as Information Gating in World Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2605.07794-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.07794)
- **OA-WAM**, OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation. [![arXiv](https://img.shields.io/badge/arXiv-2605.06481-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.06481)
- **MotuBrain**, MotuBrain: An Advanced World Action Model for Robot Control. [![arXiv](https://img.shields.io/badge/arXiv-2604.27792-b31b1b?labelColor=333333)](https://arxiv.org/abs/2604.27792) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://www.shengshu.com/en/motubrain)

### VLM-Based WAM ![Updated](https://img.shields.io/badge/Updated-2026--06--14-0A7F5A?labelColor=333333)

- **WLA**, World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis. [![arXiv](https://img.shields.io/badge/arXiv-2606.05979-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.05979) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://github.com/SJTU-DENG-Lab/WLA)
- **CKT-WAM**, CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2605.06247-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.06247) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://github.com/YuhuaJiang2002/CKT-WAM)
- **World-Value-Action Model**, World-Value-Action Model: Implicit Planning for Vision-Language-Action Systems. [![arXiv](https://img.shields.io/badge/arXiv-2604.14732-b31b1b?labelColor=333333)](https://arxiv.org/abs/2604.14732)
- **WoG**, World Guidance World Modeling in Condition Space for Action Generation. [![arXiv](https://img.shields.io/badge/arXiv-2602.22010-b31b1b?labelColor=333333)](https://arxiv.org/abs/2602.22010) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://selen-suyue.github.io/WoGNet/)
- **VLAW**, VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model. [![arXiv](https://img.shields.io/badge/arXiv-2602.12063-b31b1b?labelColor=333333)](https://arxiv.org/abs/2602.12063) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://sites.google.com/view/vlaw-arxiv)
- **VLA-JEPA**, VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model. [![arXiv](https://img.shields.io/badge/arXiv-2602.10098-b31b1b?labelColor=333333)](https://arxiv.org/abs/2602.10098) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://ginwind.github.io/VLA-JEPA/)
- **MM-ACT**, MM-ACT: Learn from Multimodal Parallel Generation to Act. [![arXiv](https://img.shields.io/badge/arXiv-2512.00975-b31b1b?labelColor=333333)](https://arxiv.org/abs/2512.00975) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://github.com/HHYHRHY/MM-ACT)
- **RynnVLA-002**, RynnVLA-002: A Unified Vision-Language-Action and World Model. [![arXiv](https://img.shields.io/badge/arXiv-2511.17502-b31b1b?labelColor=333333)](https://arxiv.org/abs/2511.17502) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://github.com/alibaba-damo-academy/RynnVLA-002)
- **F1**, F1: A Vision-Language-Action Model Bridging Understanding and Generation to Actions. [![arXiv](https://img.shields.io/badge/arXiv-2509.06951-b31b1b?labelColor=333333)](https://arxiv.org/abs/2509.06951) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://aopolin-lv.github.io/F1-VLA/)
- **FlowVLA**, FlowVLA: Visual Chain of Thought-based Motion Reasoning for Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2508.18269-b31b1b?labelColor=333333)](https://arxiv.org/abs/2508.18269) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://irpn-lab.github.io/FlowVLA/)

### WAM from Scratch and Latent Dynamics ![Updated](https://img.shields.io/badge/Updated-2026--06--14-0A7F5A?labelColor=333333)

- **RepWAM**, RepWAM: World Action Modeling with Representation Visual-Action Tokenizers. [![arXiv](https://img.shields.io/badge/arXiv-2606.13674-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.13674) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://wdrink.github.io/RepWAM)
- **JOPAT**, Point Tracking Improves World Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2605.23856-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.23856)
- **STARRY**, STARRY: Spatial-Temporal Action-Centric World Modeling for Robotic Manipulation. [![arXiv](https://img.shields.io/badge/arXiv-2604.26848-b31b1b?labelColor=333333)](https://arxiv.org/abs/2604.26848)
- **DexWorldModel**, DexWorldModel: Causal Latent World Modeling towards Automated Learning of Embodied Tasks. [![arXiv](https://img.shields.io/badge/arXiv-2604.16484-b31b1b?labelColor=333333)](https://arxiv.org/abs/2604.16484)
- **WAV**, World Action Verifier: Self-Improving World Models via Forward-Inverse Asymmetry. [![arXiv](https://img.shields.io/badge/arXiv-2604.01985-b31b1b?labelColor=333333)](https://arxiv.org/abs/2604.01985) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://world-action-verifier.github.io)
- **Enhancing Policy Learning with WAM**, Enhancing Policy Learning with World-Action Model. [![arXiv](https://img.shields.io/badge/arXiv-2603.28955-b31b1b?labelColor=333333)](https://arxiv.org/abs/2603.28955)
- **LeWorldModel**, LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels. [![arXiv](https://img.shields.io/badge/arXiv-2603.19312-b31b1b?labelColor=333333)](https://arxiv.org/abs/2603.19312) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://le-wm.github.io)
- **Explicit World Model**, Building Explicit World Model for Zero-Shot Open-World Object Manipulation. [![arXiv](https://img.shields.io/badge/arXiv-2603.13825-b31b1b?labelColor=333333)](https://arxiv.org/abs/2603.13825) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://bojack-bj.github.io/projects/thesis/)
- **LPS**, Latent Policy Steering with Embodiment-Agnostic Pretrained World Models. [![arXiv](https://img.shields.io/badge/arXiv-2507.13340-b31b1b?labelColor=333333)](https://arxiv.org/abs/2507.13340)
- **UWM**, Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets. [![arXiv](https://img.shields.io/badge/arXiv-2504.02792-b31b1b?labelColor=333333)](https://arxiv.org/abs/2504.02792) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://weirdlabuw.github.io/uwm/)

## VLA Failure Detection and Correction ![Updated](https://img.shields.io/badge/Updated-2026--06--15-0A7F5A?labelColor=333333)

Full archive: [VLA Failure Detection and Correction](VLA_FAILURE_DETECTION_AND_CORRECTION.md).

These papers are useful entry points for failure-aware VLA systems, especially
when the method uses feedback, online adaptation, closed-loop correction,
self-evaluation, or policy/world-model co-improvement.

- **Self-Improving VLA Policies**, Self-Improving VLA Policies through Online Reinforcement Learning. [![arXiv](https://img.shields.io/badge/arXiv-2606.14084-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.14084)
- **Mostly Harmless VLA Steering**, Learning What to Say to Your VLA: Mostly Harmless Vision Language Action Model Steering. [![arXiv](https://img.shields.io/badge/arXiv-2606.12299-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.12299)
- **VeriSpace**, VeriSpace: Spatially Grounded Action Verification for Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2606.10568-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.10568)
- **TORL-VLA**, TORL-VLA: Tactile Guided Online Reinforcement Learning for Contact-Rich Manipulation. [![arXiv](https://img.shields.io/badge/arXiv-2606.09337-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.09337)
- **pi0-EqM**, pi0-EqM: Equilibrium Matching for Closed-Loop Vision-Language-Action Control. [![arXiv](https://img.shields.io/badge/arXiv-2605.23128-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.23128)
- **Pre-VLA**, Pre-VLA: Preemptive Runtime Verification for Reliable Vision-Language-Action and World-Model Rollouts. [![arXiv](https://img.shields.io/badge/arXiv-2605.22446-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.22446)
- **StableVLA**, StableVLA: Towards Robust Vision-Language-Action Models without Extra Data. [![arXiv](https://img.shields.io/badge/arXiv-2605.18287-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.18287)
- **Health-Conditioned VLA**, Health-Conditioned Vision-Language-Action Models for Malfunction-Aware Robot Control. [![arXiv](https://img.shields.io/badge/arXiv-2605.16056-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.16056) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://github.com/h-arslan/health-aware-vla)
- **VLAs-as-Tools**, Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2605.13119-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.13119)
- **A3**, Dynamic Execution Commitment of Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2605.11567-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.11567)

## Efficient VLA ![Updated](https://img.shields.io/badge/Updated-2026--06--15-0A7F5A?labelColor=333333)

Full archive: [Efficient VLA](EFFICIENT_VLA.md).

### Compression, Adaptation, and Model Merging ![Updated](https://img.shields.io/badge/Updated-2026--06--14-0A7F5A?labelColor=333333)

- **Omega-QVLA**, Ω-QVLA: Robust Quantization for Vision-Language-Action Models via Composite Rotation and Per-step Scaling. [![arXiv](https://img.shields.io/badge/arXiv-2605.28803-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.28803) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://github.com/UCMP13753/Omega-QVLA)
- **EXPO-FT**, EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2605.25477-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.25477)
- **ActQuant**, ActQuant: Sub-4-bit Action-Guided Quantization for Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2605.24011-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.24011) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://actquant.github.io/)
- **Agentic-VLA**, Agentic-VLA: Efficient Online Adaptation for Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2605.22896-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.22896)
- **DA-PTQ**, DA-PTQ: Drift-Aware Post-Training Quantization for Efficient Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2604.11572-b31b1b?labelColor=333333)](https://arxiv.org/abs/2604.11572)
- **DyQ-VLA**, DyQ-VLA: Temporal-Dynamic-Aware Quantization for Embodied Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2603.07904-b31b1b?labelColor=333333)](https://arxiv.org/abs/2603.07904)
- **QuantVLA**, QuantVLA: Scale-Calibrated Post-Training Quantization for Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2602.20309-b31b1b?labelColor=333333)](https://arxiv.org/abs/2602.20309) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://quantvla.github.io/)
- **HBVLA**, HBVLA: Pushing 1-Bit Post-Training Quantization for Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2602.13710-b31b1b?labelColor=333333)](https://arxiv.org/abs/2602.13710)
- **MergeVLA**, MergeVLA: Cross-Skill Model Merging Toward a Generalist Vision-Language-Action Agent. [![arXiv](https://img.shields.io/badge/arXiv-2511.18810-b31b1b?labelColor=333333)](https://arxiv.org/abs/2511.18810) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://mergevla.github.io)
- **VLA-Adapter**, VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model. [![arXiv](https://img.shields.io/badge/arXiv-2509.09372-b31b1b?labelColor=333333)](https://arxiv.org/abs/2509.09372) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://vla-adapter.github.io)

### Tokenization, Fine-Tuning, and Deployment-Friendly VLAs ![Updated](https://img.shields.io/badge/Updated-2026--06--15-0A7F5A?labelColor=333333)

- **Output-Level Regularization**, Output-Level Regularization Eliminates the Seed Lottery in Single-GPU VLA Fine-Tuning. [![arXiv](https://img.shields.io/badge/arXiv-2606.13856-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.13856)
- **Real-Time Execution**, Real-Time Execution with Autoregressive Policies. [![arXiv](https://img.shields.io/badge/arXiv-2606.13355-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.13355)
- **Efficient-WAM**, Efficient-WAM: A 1B-Parameter World-Action Model with Low-Cost Future Imagination. [![arXiv](https://img.shields.io/badge/arXiv-2606.10040-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.10040)
- **Light-WAM**, Light-WAM: Efficient World Action Models with State-Fusion Action Decoding. [![arXiv](https://img.shields.io/badge/arXiv-2606.08242-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.08242)
- **vla.cpp**, vla.cpp: A Unified Inference Runtime for Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2606.08094-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.08094) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://fai-modelopt-tech.github.io/vla-cpp.github.io/)
- **RhinoVLA**, RhinoVLA Technical Report. [![arXiv](https://img.shields.io/badge/arXiv-2606.07383-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.07383) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://github.com/HuixiAI/RhinoVLA)
- **ElegantVLA**, ElegantVLA: Learning When to Think for Efficient Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2605.29438-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.29438)
- **CrossVLA**, Cross-Paradigm Post-Training and Inference Optimization for Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2605.21854-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.21854) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://github.com/lz-googlefycy/vla-lab)
- **VLA-AD**, Offline Semantic Guidance for Efficient Vision-Language-Action Policy Distillation. [![arXiv](https://img.shields.io/badge/arXiv-2605.16241-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.16241)
- **Realtime-VLA FLASH**, Realtime-VLA FLASH: Speculative Inference Framework for Diffusion-based VLAs. [![arXiv](https://img.shields.io/badge/arXiv-2605.13778-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.13778)

## Benchmarks for Robustness and Evaluation ![Updated](https://img.shields.io/badge/Updated-2026--05--20-0A7F5A?labelColor=333333)

- **LIBERO-Plus**, LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2510.13626-b31b1b?labelColor=333333)](https://arxiv.org/abs/2510.13626) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://sylvestf.github.io/LIBERO-plus/)
- **WorldArena**, WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models. [![arXiv](https://img.shields.io/badge/arXiv-2602.08971-b31b1b?labelColor=333333)](https://arxiv.org/abs/2602.08971) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://world-arena.ai)
- **RoboArena**, RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies. [![arXiv](https://img.shields.io/badge/arXiv-2506.18123-b31b1b?labelColor=333333)](https://arxiv.org/abs/2506.18123) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://robo-arena.github.io)
- **RoboTwin 2.0**, RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation. [![arXiv](https://img.shields.io/badge/arXiv-2506.18088-b31b1b?labelColor=333333)](https://arxiv.org/abs/2506.18088) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://github.com/robotwin-Platform/robotwin/)
- **SimplerEnv**, Evaluating Real-World Robot Manipulation Policies in Simulation. [![arXiv](https://img.shields.io/badge/arXiv-2405.05941-b31b1b?labelColor=333333)](https://arxiv.org/abs/2405.05941) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://simpler-env.github.io)
- **LIBERO**, LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning. [![arXiv](https://img.shields.io/badge/arXiv-2306.03310-b31b1b?labelColor=333333)](https://arxiv.org/abs/2306.03310) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://libero-project.github.io/main.html)

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
