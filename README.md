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
- [World Action Models](#world-action-models)
- [VLA Failure Detection and Correction](#vla-failure-detection-and-correction)
- [Efficient VLA](#efficient-vla)
- [Benchmarks for Robustness and Evaluation](#benchmarks-for-robustness-and-evaluation)
- [Contributing](#contributing)

## Surveys and Definitions

- **World Action Models: The Next Frontier in Embodied AI.** [arXiv](https://arxiv.org/abs/2605.12090) [Website](https://openmoss.github.io)
- **RT-2**, RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control. [arXiv](https://arxiv.org/abs/2307.15818) [Website](https://robotics-transformer2.github.io)
- **DreamZero**, World Action Models are Zero-shot Policies. [arXiv](https://arxiv.org/abs/2602.15922) [Website](https://dreamzero0.github.io)
- **Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges.** [arXiv](https://arxiv.org/abs/2505.04769) [Website](https://github.com/Applied-AI-Research-Lab/Vision-Language-Action-Models-Concepts-Progress-Applications-and-Challenges)
- **A Survey on Vision-Language-Action Models for Embodied AI.** [arXiv](https://arxiv.org/abs/2405.14093) [Website](https://github.com/yueen-ma/Awesome-VLA)

## World Action Models

### Video-Generation-Based WAM

- **HarmoWAM**, HarmoWAM: Harmonizing Generalizable and Precise Manipulation via Adaptive World Action Models. [arXiv](https://arxiv.org/abs/2605.10942)
- **NoiseGate**, NoiseGate: Learning Per-Latent Timestep Schedules as Information Gating in World Action Models. [arXiv](https://arxiv.org/abs/2605.07794)
- **OA-WAM**, OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation. [arXiv](https://arxiv.org/abs/2605.06481)
- **MotuBrain**, MotuBrain: An Advanced World Action Model for Robot Control. [arXiv](https://arxiv.org/abs/2604.27792) [Website](https://www.shengshu.com/en/motubrain)
- **GigaWorld-Policy**, GigaWorld-Policy: An Efficient Action-Centered World-Action Model. [arXiv](https://arxiv.org/abs/2603.17240) [Website](https://gigaai-research.github.io/GigaWorld-Policy/)
- **Fast-WAM**, Fast-WAM: Do World Action Models Need Test-time Future Imagination? [arXiv](https://arxiv.org/abs/2603.16666) [Website](https://yuantianyuan01.github.io/FastWAM/)
- **DreamZero**, World Action Models are Zero-shot Policies. [arXiv](https://arxiv.org/abs/2602.15922) [Website](https://dreamzero0.github.io)
- **Cosmos Policy**, Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning. [arXiv](https://arxiv.org/abs/2601.16163) [Website](https://research.nvidia.com/labs/dir/cosmos-policy/)
- **World-VLA-Loop**, World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy. [arXiv](https://arxiv.org/abs/2602.06508) [Website](https://showlab.github.io/World-VLA-Loop/)
- **Lingbot-VA**, Causal World Modeling for Robot Control. [arXiv](https://arxiv.org/abs/2601.21998) [Website](https://technology.robbyant.com/lingbot-va)
- **mimic-video**, mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs. [arXiv](https://arxiv.org/abs/2512.15692) [Website](https://mimic-video.github.io)
- **Dream2Flow**, Dream2Flow: Bridging Video Generation and Open-World Manipulation with 3D Object Flow. [arXiv](https://arxiv.org/abs/2512.24766) [Website](https://dream2flow.github.io)
- **Video Policy**, Video Generators are Robot Policies. [arXiv](https://arxiv.org/abs/2508.00795) [Website](https://videopolicy.cs.columbia.edu)
- **DreamGen**, DreamGen: Unlocking Generalization in Robot Learning through Video World Models. [arXiv](https://arxiv.org/abs/2505.12705) [Website](https://research.nvidia.com/labs/gear/dreamgen/)
- **VPP**, Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations. [arXiv](https://arxiv.org/abs/2412.14803) [Website](https://video-prediction-policy.github.io)
- **GR-2**, GR-2: A Generative Video-Language-Action Model with Web-Scale Knowledge for Robot Manipulation. [arXiv](https://arxiv.org/abs/2410.06158) [Website](https://gr2-manipulation.github.io)
- **GR-1**, Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation. [arXiv](https://arxiv.org/abs/2312.13139) [Website](https://gr1-manipulation.github.io)
- **UniPi**, Learning Universal Policies via Text-Guided Video Generation. [arXiv](https://arxiv.org/abs/2302.00111) [Website](https://universal-policy.github.io/unipi/)

### VLM-Based WAM

- **pi0.7**, pi0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities. [Website](https://www.pi.website/blog/pi07)
- **CKT-WAM**, CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models. [arXiv](https://arxiv.org/abs/2605.06247) [Code](https://github.com/YuhuaJiang2002/CKT-WAM)
- **VLAW**, VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model. [arXiv](https://arxiv.org/abs/2602.12063) [Website](https://sites.google.com/view/vlaw-arxiv)
- **WoG**, World Guidance World Modeling in Condition Space for Action Generation. [arXiv](https://arxiv.org/abs/2602.22010) [Website](https://selen-suyue.github.io/WoGNet/)
- **VLA-JEPA**, VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model. [arXiv](https://arxiv.org/abs/2602.10098) [Website](https://ginwind.github.io/VLA-JEPA/)
- **MM-ACT**, MM-ACT: Learn from Multimodal Parallel Generation to Act. [arXiv](https://arxiv.org/abs/2512.00975) [Website](https://github.com/HHYHRHY/MM-ACT)
- **RynnVLA-002**, RynnVLA-002: A Unified Vision-Language-Action and World Model. [arXiv](https://arxiv.org/abs/2511.17502) [Website](https://github.com/alibaba-damo-academy/RynnVLA-002)
- **F1**, F1: A Vision-Language-Action Model Bridging Understanding and Generation to Actions. [arXiv](https://arxiv.org/abs/2509.06951) [Website](https://aopolin-lv.github.io/F1-VLA/)
- **FlowVLA**, FlowVLA: Visual Chain of Thought-based Motion Reasoning for Vision-Language-Action Models. [arXiv](https://arxiv.org/abs/2508.18269) [Website](https://irpn-lab.github.io/FlowVLA/)
- **DreamVLA**, DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge. [arXiv](https://arxiv.org/abs/2507.04447) [Website](https://zhangwenyao1.github.io/DreamVLA/)
- **WorldVLA**, WorldVLA: Towards Autoregressive Action World Model. [arXiv](https://arxiv.org/abs/2506.21539) [Website](https://github.com/alibaba-damo-academy/RynnVLA-002)
- **FLARE**, FLARE: Robot Learning with Implicit World Modeling. [arXiv](https://arxiv.org/abs/2505.15659) [Website](https://research.nvidia.com/labs/gear/flare)
- **UP-VLA**, UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent. [arXiv](https://arxiv.org/abs/2501.18867) [Website](https://github.com/CladernyJorn/UP-VLA)

### WAM from Scratch and Latent Dynamics

- **Being-H0.7**, Being-H0.7: A Latent World-Action Model from Egocentric Videos. [Paper](https://research.beingbeyond.com/projects/being-h07/being-h07.pdf) [Website](https://research.beingbeyond.com/being-h07)
- **DexWorldModel**, DexWorldModel: Causal Latent World Modeling towards Automated Learning of Embodied Tasks. [arXiv](https://arxiv.org/abs/2604.16484)
- **WAV**, World Action Verifier: Self-Improving World Models via Forward-Inverse Asymmetry. [arXiv](https://arxiv.org/abs/2604.01985) [Website](https://world-action-verifier.github.io)
- **Enhancing Policy Learning with WAM**, Enhancing Policy Learning with World-Action Model. [arXiv](https://arxiv.org/abs/2603.28955)
- **LeWorldModel**, LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels. [arXiv](https://arxiv.org/abs/2603.19312) [Website](https://le-wm.github.io)
- **LPS**, Latent Policy Steering with Embodiment-Agnostic Pretrained World Models. [arXiv](https://arxiv.org/abs/2507.13340)
- **UWM**, Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets. [arXiv](https://arxiv.org/abs/2504.02792) [Website](https://weirdlabuw.github.io/uwm/)
- **UVAM**, Unified Video Action Model. [arXiv](https://arxiv.org/abs/2503.00200) [Website](https://unified-video-action-model.github.io)
- **Seer**, Predictive Inverse Dynamics Models are Scalable Learners for Robotic Manipulation. [arXiv](https://arxiv.org/abs/2412.15109) [Website](https://github.com/InternRobotics/Seer)
- **DreamerV3**, Mastering Diverse Domains through World Models. [arXiv](https://arxiv.org/abs/2301.04104) [Website](https://danijar.com/project/dreamerv3/)

## VLA Failure Detection and Correction

These papers are useful entry points for failure-aware VLA systems, especially
when the method uses feedback, online adaptation, closed-loop correction,
self-evaluation, or policy/world-model co-improvement.

- **VLAs-as-Tools**, Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models. [arXiv](https://arxiv.org/abs/2605.13119)
- **RePO-VLA**, RePO-VLA: Recovery-Driven Policy Optimization for Vision-Language-Action Models. [arXiv](https://arxiv.org/abs/2605.09410)
- **Failing Forward**, Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models. [arXiv](https://arxiv.org/abs/2605.08434)
- **AT-VLA**, AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models. [arXiv](https://arxiv.org/abs/2605.07308) [Website](https://sites.google.com/view/at-vla)
- **When to Trust Imagination**, When to Trust Imagination: Adaptive Action Execution for World Action Models. [arXiv](https://arxiv.org/abs/2605.06222)
- **VLA-ATTC**, VLA-ATTC: Adaptive Test-Time Compute for VLA Models with Relative Action Critic Model. [arXiv](https://arxiv.org/abs/2605.01194)
- **Sentinel-VLA**, Sentinel-VLA: A Metacognitive VLA Model with Active Status Monitoring for Dynamic Reasoning and Error Recovery. [arXiv](https://arxiv.org/abs/2605.01191)
- **ReconVLA**, ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control. [arXiv](https://arxiv.org/abs/2604.16677)
- **STRONG-VLA**, STRONG-VLA: Decoupled Robustness Learning for Vision-Language-Action Models under Multimodal Perturbations. [arXiv](https://arxiv.org/abs/2604.10055)
- **WAV**, World Action Verifier: Self-Improving World Models via Forward-Inverse Asymmetry. [arXiv](https://arxiv.org/abs/2604.01985) [Website](https://world-action-verifier.github.io)
- **EVOLVE-VLA**, EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models. [arXiv](https://arxiv.org/abs/2512.14666) [Website](https://showlab.github.io/EVOLVE-VLA/)
- **VLAW**, VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model. [arXiv](https://arxiv.org/abs/2602.12063) [Website](https://sites.google.com/view/vlaw-arxiv)
- **World-VLA-Loop**, World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy. [arXiv](https://arxiv.org/abs/2602.06508) [Website](https://showlab.github.io/World-VLA-Loop/)
- **SRPO**, SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models. [arXiv](https://arxiv.org/abs/2511.15605)
- **VLA-Reasoner**, VLA-Reasoner: Empowering Vision-Language-Action Models with Reasoning via Online Monte Carlo Tree Search. [arXiv](https://arxiv.org/abs/2509.22643)
- **RIPT-VLA**, Interactive Post-Training for Vision-Language-Action Models. [arXiv](https://arxiv.org/abs/2505.17016) [Website](https://ariostgx.github.io/ript_vla/)
- **GRAPE**, GRAPE: Generalizing Robot Policy via Preference Alignment. [arXiv](https://arxiv.org/abs/2411.19309) [Website](https://grape-vla.github.io)
- **CronusVLA**, CronusVLA: Towards Efficient and Robust Manipulation via Multi-Frame Vision-Language-Action Modeling. [arXiv](https://arxiv.org/abs/2506.19816) [Website](https://lihaohn.github.io/CronusVLA.github.io/)
- **AVA-VLA**, AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention. [arXiv](https://arxiv.org/abs/2511.18960)

## Efficient VLA

### Compression, Adaptation, and Model Merging

- **DA-PTQ**, DA-PTQ: Drift-Aware Post-Training Quantization for Efficient Vision-Language-Action Models. [arXiv](https://arxiv.org/abs/2604.11572)
- **HBVLA**, HBVLA: Pushing 1-Bit Post-Training Quantization for Vision-Language-Action Models. [arXiv](https://arxiv.org/abs/2602.13710)
- **MergeVLA**, MergeVLA: Cross-Skill Model Merging Toward a Generalist Vision-Language-Action Agent. [arXiv](https://arxiv.org/abs/2511.18810) [Website](https://mergevla.github.io)
- **VLA-Adapter**, VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model. [arXiv](https://arxiv.org/abs/2509.09372) [Website](https://vla-adapter.github.io)
- **FLOWER**, FLOWER: Democratizing Generalist Robot Policies with Efficient Vision-Language-Action Flow Policies. [arXiv](https://arxiv.org/abs/2509.04996) [Website](https://intuitive-robots.github.io/flower_vla/)
- **TinyVLA**, TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation. [arXiv](https://arxiv.org/abs/2409.12514) [Website](https://tiny-vla.github.io)

### Tokenization, Fine-Tuning, and Deployment-Friendly VLAs

- **A1**, A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model. [arXiv](https://arxiv.org/abs/2604.05672)
- **Premover**, Premover: Fast Vision-Language-Action Control by Acting Before Instructions Are Complete. [arXiv](https://arxiv.org/abs/2605.12160)
- **OneWM-VLA**, One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy. [arXiv](https://arxiv.org/abs/2605.07931)
- **ConsisVLA-4D**, ConsisVLA-4D: Advancing Spatiotemporal Consistency in Efficient 3D-Perception and 4D-Reasoning for Robotic Manipulation. [arXiv](https://arxiv.org/abs/2605.05126) [Website](https://github.com/iLearn-Lab/CVPR26-ConsisVLA-4D)
- **Latent Bridge**, Latent Bridge: Feature Delta Prediction for Efficient Dual-System Vision-Language-Action Model Inference. [arXiv](https://arxiv.org/abs/2605.02739)
- **PokeVLA**, PokeVLA: Empowering Pocket-Sized Vision-Language-Action Model with Comprehensive World Knowledge Guidance. [arXiv](https://arxiv.org/abs/2604.20834) [Website](https://getterupper.github.io/PokeVLA)
- **StreamingVLA**, StreamingVLA: Streaming Vision-Language-Action Model with Action Flow Matching and Adaptive Early Observation. [arXiv](https://arxiv.org/abs/2603.28565) [Website](https://ghahahahag.github.io/StreamingVLA_Website/)
- **ETA-VLA**, ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models. [arXiv](https://arxiv.org/abs/2603.25766)
- **FASTer**, FASTer: Toward Efficient Autoregressive Vision Language Action Modeling via Neural Action Tokenization. [arXiv](https://arxiv.org/abs/2512.04952)
- **FAST**, FAST: Efficient Action Tokenization for Vision-Language-Action Models. [arXiv](https://arxiv.org/abs/2501.09747) [Website](https://www.pi.website/research/fast)
- **OpenVLA-OFT**, Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success. [arXiv](https://arxiv.org/abs/2502.19645) [Website](https://openvla-oft.github.io)
- **SmolVLA**, SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics. [arXiv](https://arxiv.org/abs/2506.01844) [Website](https://github.com/huggingface/lerobot)
- **SimVLA**, SimVLA: A Simple VLA Baseline for Robotic Manipulation. [arXiv](https://arxiv.org/abs/2602.18224) [Website](https://frontierrobo.github.io/SimVLA/)
- **VLA-0**, VLA-0: Building State-of-the-Art VLAs with Zero Modification. [arXiv](https://arxiv.org/abs/2510.13054) [Website](https://vla0.github.io)

## Benchmarks for Robustness and Evaluation

- **LIBERO-Plus**, LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models. [arXiv](https://arxiv.org/abs/2510.13626) [Website](https://sylvestf.github.io/LIBERO-plus/)
- **WorldArena**, WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models. [arXiv](https://arxiv.org/abs/2602.08971) [Website](https://world-arena.ai)
- **RoboArena**, RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies. [arXiv](https://arxiv.org/abs/2506.18123) [Website](https://robo-arena.github.io)
- **RoboTwin 2.0**, RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation. [arXiv](https://arxiv.org/abs/2506.18088) [Website](https://github.com/robotwin-Platform/robotwin/)
- **SimplerEnv**, Evaluating Real-World Robot Manipulation Policies in Simulation. [arXiv](https://arxiv.org/abs/2405.05941) [Website](https://simpler-env.github.io)
- **LIBERO**, LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning. [arXiv](https://arxiv.org/abs/2306.03310) [Website](https://libero-project.github.io/main.html)

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
