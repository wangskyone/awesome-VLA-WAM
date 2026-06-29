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

## Agentic Robotics (New Trend) ![Updated](https://img.shields.io/badge/Updated-2026--06--29-0A7F5A?labelColor=333333)

This emerging line treats robot foundation models as components inside a
broader agent loop, combining high-level planning, tool use, reusable skill
libraries, policy self-improvement, and long-horizon execution.

- **RAVEN**, RAVEN: Long-Horizon Reasoning & Navigation with a Visuo-Spatio-Temporal Memory for Robotics. [![arXiv](https://img.shields.io/badge/arXiv-2606.25206-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.25206)
- **OmniAct**, Advancing Omnimodal Embodied Agents from Isolated Skills to Everyday Physical Autonomy. [![arXiv](https://img.shields.io/badge/arXiv-2606.27251-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.27251)
- **HoloAgent-0**, HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory. [![arXiv](https://img.shields.io/badge/arXiv-2606.23565-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.23565) [![Code](https://img.shields.io/badge/Code-GitHub-24292F?labelColor=333333)](https://github.com/HorizonRobotics/HoloAgent)
- **ENPIRE**, ENPIRE: Agentic Robot Policy Self-Improvement in the Real World. [![arXiv](https://img.shields.io/badge/arXiv-2606.19980-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.19980)
- **Playful Agentic Robot Learning**, Playful Agentic Robot Learning. [![arXiv](https://img.shields.io/badge/arXiv-2606.19419-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.19419) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://playful-rats.github.io/)
- **Qwen-RobotNav**, Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System. [![arXiv](https://img.shields.io/badge/arXiv-2606.18112-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.18112) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://qwen.ai/blog?id=qwen-robotnav)
- **FCGraft**, Functional Cache Grafting: Robust and Rapid Code-Policy Synthesis for Embodied Agents. [![arXiv](https://img.shields.io/badge/arXiv-2606.13097-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.13097)
- **Embodied-R1.5**, Embodied-R1.5: Evolving Physical Intelligence via Embodied Foundation Models. [![arXiv](https://img.shields.io/badge/arXiv-2606.11324-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.11324) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://embodied-r1.github.io/) [![Code](https://img.shields.io/badge/Code-GitHub-24292F?labelColor=333333)](https://github.com/Embodied-R1/Embodied-R1)
- **VLAs-as-Tools**, Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2605.13119-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.13119)
- **RoboClaw**, RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks. [![arXiv](https://img.shields.io/badge/arXiv-2603.11558-b31b1b?labelColor=333333)](https://arxiv.org/abs/2603.11558) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://roboclaw-agibot.github.io/)
- **SELF-VLA**, SELF-VLA: A Skill Enhanced Agentic Vision-Language-Action Framework for Contact-Rich Disassembly. [![arXiv](https://img.shields.io/badge/arXiv-2603.11080-b31b1b?labelColor=333333)](https://arxiv.org/abs/2603.11080)

## Surveys and Definitions ![Updated](https://img.shields.io/badge/Updated-2026--05--20-0A7F5A?labelColor=333333)

- **World Action Models: The Next Frontier in Embodied AI.** [![arXiv](https://img.shields.io/badge/arXiv-2605.12090-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.12090) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://openmoss.github.io)
- **RT-2**, RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control. [![arXiv](https://img.shields.io/badge/arXiv-2307.15818-b31b1b?labelColor=333333)](https://arxiv.org/abs/2307.15818) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://robotics-transformer2.github.io)
- **DreamZero**, World Action Models are Zero-shot Policies. [![arXiv](https://img.shields.io/badge/arXiv-2602.15922-b31b1b?labelColor=333333)](https://arxiv.org/abs/2602.15922) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://dreamzero0.github.io)
- **Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges.** [![arXiv](https://img.shields.io/badge/arXiv-2505.04769-b31b1b?labelColor=333333)](https://arxiv.org/abs/2505.04769) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://github.com/Applied-AI-Research-Lab/Vision-Language-Action-Models-Concepts-Progress-Applications-and-Challenges)
- **A Survey on Vision-Language-Action Models for Embodied AI.** [![arXiv](https://img.shields.io/badge/arXiv-2405.14093-b31b1b?labelColor=333333)](https://arxiv.org/abs/2405.14093) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://github.com/yueen-ma/Awesome-VLA)

## World Action Models ![Updated](https://img.shields.io/badge/Updated-2026--06--29-0A7F5A?labelColor=333333)

Full archive: [World Action Models](WORLD_ACTION_MODELS.md).

### Video-Generation-Based WAM ![Updated](https://img.shields.io/badge/Updated-2026--06--25-0A7F5A?labelColor=333333)

- **NavWM**, NavWM: A Unified Navigation World Model for Foresight-Driven Planning. [![arXiv](https://img.shields.io/badge/arXiv-2606.24101-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.24101)
- **ImageWAM**, ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing? [![arXiv](https://img.shields.io/badge/arXiv-2606.19531-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.19531) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://zhangwenyao1.github.io/ImageWAM/)
- **Metis**, Metis: A Generalizable and Efficient World-Action Model for Autonomous Driving and Urban Navigation. [![arXiv](https://img.shields.io/badge/arXiv-2606.15869-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.15869)
- **WAM4D**, WAM4D: A Fast 4D World Action Model for Robotic Manipulation. [![arXiv](https://img.shields.io/badge/arXiv-2606.14048-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.14048)
- **MaskWAM**, MaskWAM: Unifying Mask Prompting and Prediction for World-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2606.13515-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.13515) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://hanyangyu1021.github.io/maskwam.github.io/)
- **NavWAM**, NavWAM: A Navigation World Action Model for Goal-Conditioned Visual Navigation. [![arXiv](https://img.shields.io/badge/arXiv-2606.13494-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.13494) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://dachii-azm.github.io/navwam/)
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

### WAM from Scratch and Latent Dynamics ![Updated](https://img.shields.io/badge/Updated-2026--06--29-0A7F5A?labelColor=333333)

- **DIM-WAM**, DIM-WAM: World-Action Modeling with Diverse Historical Event Memory. [![arXiv](https://img.shields.io/badge/arXiv-2606.27677-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.27677) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://wangkai-casia.github.io/dim-wam/)
- **REGEN**, World Action Models Enable Continual Imitation Learning with Recurrent Generative Replays. [![arXiv](https://img.shields.io/badge/arXiv-2606.27374-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.27374)
- **Tactile-WAM**, Tactile-WAM: Touch-Aware World Action Model with Tactile Asymmetric Attention. [![arXiv](https://img.shields.io/badge/arXiv-2606.26663-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.26663)
- **MV-WAM**, MV-WAM: Manifold-Aware World Action Model with Value Augmentation. [![arXiv](https://img.shields.io/badge/arXiv-2606.21088-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.21088)
- **WAM-RL**, WAM-RL: World-Action Model Reinforcement Learning with Reconstruction Rewards and Online Video SFT. [![arXiv](https://img.shields.io/badge/arXiv-2606.17906-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.17906)
- **MemoryWAM**, MemoryWAM: Efficient World Action Modeling with Persistent Memory. [![arXiv](https://img.shields.io/badge/arXiv-2606.20562-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.20562)
- **Mem-World**, Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation. [![arXiv](https://img.shields.io/badge/arXiv-2606.18960-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.18960)
- **LaWAM**, LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies. [![arXiv](https://img.shields.io/badge/arXiv-2606.15768-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.15768) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://github.com/RLinf/LaWAM)
- **RepWAM**, RepWAM: World Action Modeling with Representation Visual-Action Tokenizers. [![arXiv](https://img.shields.io/badge/arXiv-2606.13674-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.13674) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://wdrink.github.io/RepWAM)
- **HiMem-WAM**, HiMem-WAM: Hierarchical Memory-Gated World Action Models for Robotic Manipulation. [![arXiv](https://img.shields.io/badge/arXiv-2606.10363-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.10363)
- **JOPAT**, Point Tracking Improves World Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2605.23856-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.23856)
- **STARRY**, STARRY: Spatial-Temporal Action-Centric World Modeling for Robotic Manipulation. [![arXiv](https://img.shields.io/badge/arXiv-2604.26848-b31b1b?labelColor=333333)](https://arxiv.org/abs/2604.26848)
- **DexWorldModel**, DexWorldModel: Causal Latent World Modeling towards Automated Learning of Embodied Tasks. [![arXiv](https://img.shields.io/badge/arXiv-2604.16484-b31b1b?labelColor=333333)](https://arxiv.org/abs/2604.16484)
- **WAV**, World Action Verifier: Self-Improving World Models via Forward-Inverse Asymmetry. [![arXiv](https://img.shields.io/badge/arXiv-2604.01985-b31b1b?labelColor=333333)](https://arxiv.org/abs/2604.01985) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://world-action-verifier.github.io)
- **Enhancing Policy Learning with WAM**, Enhancing Policy Learning with World-Action Model. [![arXiv](https://img.shields.io/badge/arXiv-2603.28955-b31b1b?labelColor=333333)](https://arxiv.org/abs/2603.28955)
- **LeWorldModel**, LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels. [![arXiv](https://img.shields.io/badge/arXiv-2603.19312-b31b1b?labelColor=333333)](https://arxiv.org/abs/2603.19312) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://le-wm.github.io)
- **Explicit World Model**, Building Explicit World Model for Zero-Shot Open-World Object Manipulation. [![arXiv](https://img.shields.io/badge/arXiv-2603.13825-b31b1b?labelColor=333333)](https://arxiv.org/abs/2603.13825) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://bojack-bj.github.io/projects/thesis/)
- **LPS**, Latent Policy Steering with Embodiment-Agnostic Pretrained World Models. [![arXiv](https://img.shields.io/badge/arXiv-2507.13340-b31b1b?labelColor=333333)](https://arxiv.org/abs/2507.13340)
- **UWM**, Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets. [![arXiv](https://img.shields.io/badge/arXiv-2504.02792-b31b1b?labelColor=333333)](https://arxiv.org/abs/2504.02792) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://weirdlabuw.github.io/uwm/)

## VLA Failure Detection and Correction ![Updated](https://img.shields.io/badge/Updated-2026--06--28-0A7F5A?labelColor=333333)

Full archive: [VLA Failure Detection and Correction](VLA_FAILURE_DETECTION_AND_CORRECTION.md).

These papers are useful entry points for failure-aware VLA systems, especially
when the method uses feedback, online adaptation, closed-loop correction,
self-evaluation, or policy/world-model co-improvement.

- **PhysReflect-VLA**, PhysReflect-VLA: Physical Feasibility and Self-Reflective Regulation for Reliable Vision-Language-Action Policies. [![arXiv](https://img.shields.io/badge/arXiv-2606.27146-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.27146)
- **ROAD-VLA**, ROAD-VLA: Robust Online Adaptation via Self-Distillation for Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2606.25800-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.25800)
- **RECALL**, RECALL: Recovery Experience Collection for Active Lifelong Learning in Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2606.23617-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.23617)
- **Tri-Info**, Tri-Info: Generalizable, Interpretable Failure Prediction for VLA Models via Information Theory. [![arXiv](https://img.shields.io/badge/arXiv-2606.19998-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.19998)
- **VERITAS**, Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement. [![arXiv](https://img.shields.io/badge/arXiv-2606.18247-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.18247)
- **SAVE**, Uncertainty Quantification for Flow-Based Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2606.18043-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.18043) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://save-vla.github.io/)
- **DREAM-Chunk**, DREAM-Chunk: Reactive Action Chunking with Latent World Model. [![arXiv](https://img.shields.io/badge/arXiv-2606.17258-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.17258)
- **ROVE**, ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement Learning. [![arXiv](https://img.shields.io/badge/arXiv-2606.17011-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.17011) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://xpeng-robotics.github.io/rove/)
- **Self-Improving VLA Policies**, Self-Improving VLA Policies through Online Reinforcement Learning. [![arXiv](https://img.shields.io/badge/arXiv-2606.14084-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.14084)
- **Mostly Harmless VLA Steering**, Learning What to Say to Your VLA: Mostly Harmless Vision Language Action Model Steering. [![arXiv](https://img.shields.io/badge/arXiv-2606.12299-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.12299)
- **World Pilot**, Steering Vision-Language-Action Models with World-Action Priors. [![arXiv](https://img.shields.io/badge/arXiv-2606.12403-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.12403) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://world-pilot.github.io/)
- **VeriSpace**, VeriSpace: Spatially Grounded Action Verification for Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2606.10568-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.10568)
- **TORL-VLA**, TORL-VLA: Tactile Guided Online Reinforcement Learning for Contact-Rich Manipulation. [![arXiv](https://img.shields.io/badge/arXiv-2606.09337-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.09337)
- **pi0-EqM**, pi0-EqM: Equilibrium Matching for Closed-Loop Vision-Language-Action Control. [![arXiv](https://img.shields.io/badge/arXiv-2605.23128-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.23128)
- **Pre-VLA**, Pre-VLA: Preemptive Runtime Verification for Reliable Vision-Language-Action and World-Model Rollouts. [![arXiv](https://img.shields.io/badge/arXiv-2605.22446-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.22446)
- **StableVLA**, StableVLA: Towards Robust Vision-Language-Action Models without Extra Data. [![arXiv](https://img.shields.io/badge/arXiv-2605.18287-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.18287)
- **Health-Conditioned VLA**, Health-Conditioned Vision-Language-Action Models for Malfunction-Aware Robot Control. [![arXiv](https://img.shields.io/badge/arXiv-2605.16056-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.16056) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://github.com/h-arslan/health-aware-vla)
- **A3**, Dynamic Execution Commitment of Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2605.11567-b31b1b?labelColor=333333)](https://arxiv.org/abs/2605.11567)

## Efficient VLA ![Updated](https://img.shields.io/badge/Updated-2026--06--29-0A7F5A?labelColor=333333)

Full archive: [Efficient VLA](EFFICIENT_VLA.md).

### Compression, Adaptation, and Model Merging ![Updated](https://img.shields.io/badge/Updated-2026--06--22-0A7F5A?labelColor=333333)

- **Mix-QVLA**, Mix-QVLA: Task-Evidence-Aware Mixed-Precision Quantization of Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2606.19565-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.19565)
- **Learned Image Compression**, Learned Image Compression for Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2606.16253-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.16253)
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

### Tokenization, Fine-Tuning, and Deployment-Friendly VLAs ![Updated](https://img.shields.io/badge/Updated-2026--06--29-0A7F5A?labelColor=333333)

- **SpikeVLA**, SpikeVLA: Vision-Language-Action Models with Spiking Neural Networks. [![arXiv](https://img.shields.io/badge/arXiv-2606.27807-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.27807)
- **FORCE**, FORCE: Efficient VLA Reinforcement Fine-Tuning via Value-Calibrated Warm-up and Self-Distillation. [![arXiv](https://img.shields.io/badge/arXiv-2606.26006-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.26006)
- **Action ControlNet**, Action ControlNet: A Lightweight Delay-Aware Adapter for Smooth Asynchronous Control in Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2606.25985-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.25985)
- **UniFS**, UniFS: Unified Fast-to-Slow Hierarchical Architecture for Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2606.22794-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.22794) [![Code](https://img.shields.io/badge/Code-GitHub-24292F?labelColor=333333)](https://github.com/linsun449/UniFS)
- **Fewer-Layer VLA Finetuning**, Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think. [![arXiv](https://img.shields.io/badge/arXiv-2606.20246-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.20246)
- **Acting While Understanding**, Acting While Understanding: Asynchronous Semantic-Action Decoupling for Real-Time Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2606.15285-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.15285)
- **AVA-VLA**, Think Less, Act Early: Reinforced Latent Reasoning with Early Exit in Vision-Language-Action Models. [![arXiv](https://img.shields.io/badge/arXiv-2606.15099-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.15099)
- **X-Tokenizer**, X-Tokenizer: A Multimodal Action Tokenizer for Vision-Language-Action Pretraining. [![arXiv](https://img.shields.io/badge/arXiv-2606.14752-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.14752) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://x-square-robot.github.io/X-Tokenizer_projectPage/)
- **Output-Level Regularization**, Output-Level Regularization Eliminates the Seed Lottery in Single-GPU VLA Fine-Tuning. [![arXiv](https://img.shields.io/badge/arXiv-2606.13856-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.13856)
- **Real-Time Execution**, Real-Time Execution with Autoregressive Policies. [![arXiv](https://img.shields.io/badge/arXiv-2606.13355-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.13355)
- **DAM-VLA**, DAM-VLA: Decoupled Asynchronous Multimodal Vision Language Action model. [![arXiv](https://img.shields.io/badge/arXiv-2606.12105-b31b1b?labelColor=333333)](https://arxiv.org/abs/2606.12105) [![Website](https://img.shields.io/badge/Website-Link-0A66C2?labelColor=333333)](https://intuitive-robots.github.io/DAM-VLA/)
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
