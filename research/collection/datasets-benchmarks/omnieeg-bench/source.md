# **OmniEEG-Bench: A Standardized Evaluation Benchmark for EEG Foundation Models** 

**Ziling Lu**<sup>1</sup><sup>_†_</sup> **Zongsheng Li**<sup>2</sup><sup>_,_1</sup><sup>_†_</sup> **Xinke Shen**<sup>1</sup><sup>_†_</sup> **Kexin Lou**<sup>1</sup><sup>_,_3</sup><sup>_†_</sup> **Yingyue Xin**<sup>1</sup> **Xiaoqi Chen**<sup>1</sup> **Shinan Wang**<sup>1</sup> **Xiang Chen**<sup>1</sup> **Jiahao Fan**<sup>1</sup> **Chenyu Huang**<sup>1</sup> **Xin Xu**<sup>1</sup> **Zhoujie Hou**<sup>1</sup> **Chen Wei**<sup>1</sup><sup>_,_3</sup><sup>*****</sup> **Quanying Liu**<sup>1</sup><sup>_,_3</sup><sup>_,_4</sup><sup>*****</sup> 

> 1 **Department of Biomedical Engineering, Southern University of Science and Technology, Shenzhen, China** 

> 2 **School of Computer Science and Engineering, The Chinese University of Hong Kong, Shenzhen, China** 

> 3 **Omni-Intelligence, Shenzhen, China** 

> 4 **Shenzhen Loop Area Institute, Shenzhen, China** 

> _†_ **Equal contribution** 

> ***Corresponding authors:** `liuqy@sustech.edu.cn; chen.wei@omni-intel.cn` 



<!-- Start of picture text -->
a 3 Performance vs. Dataset diversity b Performance vs. Model size<br>CBraMod BrainOmni CBraMod BrainOmni<br>4 REVE REVE<br>5<br>FEMBA FEMBA<br>BIOT LaBraM BIOT LaBraM<br>6 NeuroLM NeuroLM<br>NeuroGPT EEGMamba EEGMamba NeuroGPT<br>7<br>8<br>BENDR Per-dataset median Wilcoxon p=1.1e-07 ρ =-0.27,  BENDR Per-dataset median Wilcoxon p=7.0e-04 ρ =-0.21,<br>9<br>1 3 5 10 20 50 100 3 5 10 20 50 100 200<br># Pretrained datasets # Parameters<br>Average rank (lower is better) Average rank (lower is better)<br><!-- End of picture text -->

Figure 1: **Scaling law of pretraining data diversity (a) and model size (b) for linear-probing generalization of EEG foundation models.** Tests on OmniEEG-Bench with 58 datasets show that EEG foundation models pretrained on a greater number of datasets and models with a larger number of parameters tend to achieve lower average ranks (i.e., better performance). 

## **Abstract** 

Electroencephalography (EEG) supports a variety of brain-computer interface (BCI) tasks ranging from brain-state monitoring to human-LLM interactions. EEG foundation models are emerging, but evaluation remains fragmented due to heterogeneous datasets and inconsistent task protocols. Here, we introduce OmniEEG-Bench, a unified benchmark and downstream task roadmap for EEG foundation models (FMs). It organizes evaluation of EEG FMs into six task families spanning (i) signal reliability, (ii) biometrics and disease, (iii) consciousness and state, (iv) cognition and emotion, (v) naturalistic stimulus decoding, and (vi) motor and interaction, introducing a new generation of tasks not systematically benchmarked in prior EEG FM work. OmniEEG-Bench standardizes model deployment, task definitions, and metrics through a task-card specification, and unifies 54 EEG datasets with consistent evaluation protocols. We benchmark 10 representative EEG foundation models and report a leaderboard that covers diverse evaluation settings. Both pretraining dataset diversity and model size are significantly associated with better average ranks across datasets, revealing scalinglaw behavior in EEG foundation models (Figure 1). These results suggest that scaling EEG foundation models requires not only larger architectures but also broader and more diverse pretraining data. The benchmark code is available at `https://github.com/ncclab-sustech/omni-eegbench.git` . 

## **1 Introduction** 

EEG foundation models are rapidly emerging as a new paradigm for brain decoding: by pretraining on large-scale, heterogeneous EEG, a single model can be adapted to many downstream tasks, with the long-term promise of capturing universal EEG representations and enabling practical “reading the brain” [1, 2, 3]. Recent models, such as BIOT [4], LaBraM [5] and BrainOmni [6], explicitly pursue universal and transferable EEG representations via self-supervised pretraining such as masked autoencoding and contrastive learning. However, the field lacks a fair way to compare them: each model is evaluated on different datasets, tasks, and splits in terms of decoding ability and generalizability, and even for the same task, evaluation settings can substantially alter the results. This fragmentation obscures what foundation models truly improve, and hinders the development of robust and generalizable brain decoding systems. 

This lack of comparability is not only a protocol issue. It also reflects the absence of a shared view of what EEG foundation models should be good at. Different work implicitly prioritizes different task families, making “general-purpose EEG representation” difficult to operationalize. A coherent task roadmap is therefore a prerequisite for fair evaluation: it makes the capability axes explicit and encourages models to be assessed across a broad spectrum of EEG objectives rather than a few isolated settings. EEG tasks span a wide range of regimes, from clinical abnormality detection [7] to global state monitoring (such as sleep staging) [8] and fast, low-latency BCI control [9]. Meanwhile, recent open datasets increasingly capture EEG under more naturalistic, high-dimensional sensory contexts—such as viewing rich visual scenes [10] or listening to continuous speech [11, 12]—where the stimulus space is complex [13]. However, most EEG foundation models are still evaluated on a narrow subset of controlled paradigms, and are rarely tested in a standardized way on these naturalisticcontext datasets. Therefore, a benchmark should reflect the field’s evolution from tightly controlled experiments toward naturalistic, interaction-centric paradigms, while maintaining standardization through well-defined tasks. 

We introduce OmniEEG-Bench, a standardized evaluation benchmark for EEG foundation models. OmniEEG-Bench organizes downstream evaluation into six task families: (i) signal reliability, (ii) biometrics and disease, (iii) consciousness and state, (iv) cognition and emotion, (v) naturalistic stimulus decoding, and (vi) motor and interaction. This taxonomy is organized by three dimensions: from stable traits to transient states, from slow- to fast-changing temporal scales, and from passive monitoring to active interaction. We standardize preprocessing, task definitions, and metrics through a task-card specification. We benchmark 10 EEG foundation models on 54 EEG datasets with a protocol suite that probes four complementary capabilities: (i) multi-subject cross-trial adaptation, (ii) cross-subject transfer, (iii) label-efficiency via zero-/few-shot adaptation, and (iv) noise robustness under sensor degradation via channel corruption. Our contributions are threefold: 

- **A unified task roadmap for EEG foundation models.** We organize EEG downstream evaluation into six task taxonomies and formalize each task with a _task-card_ specification that standardizes preprocessing, inputs/outputs, and metrics. 

- **Standardized evaluation protocols that probe transfer, data efficiency, and robustness.** We report results under multi-subject (trial-level splits with pooled subjects) and crosssubject (held-out subjects) settings, and further include zero-shot/few-shot adaptation and channel corruption tests. These tests systematically characterize the transferability and robustness of pretrained representations. 

- **Large-scale, reproducible benchmarking with diagnostic insights.** We benchmark 10 EEG foundation models on 54 EEG datasets, release a public leaderboard, and identify the predictive factors that influence the model’s downstream performance. 

## **2 EEG Task Taxonomy and Dataset Organization** 

OmniEEG-Bench adopts a capability-driven task taxonomy that organizes downstream EEG tasks into a continuous task space, as illustrated in Fig. 2. We use three broad organizing dimensions to guide this design. First, tasks differ in the extent to which they reflect stable **subject-specific characteristics** or **transient brain states** , consistent with the view that EEG measurements can contain both trait-like and state-dependent components [14]. Biometrics and clinical phenotyping emphasize relatively 

2 



Figure 2: Task taxonomy of OmniEEG-Bench. We organize 58 tasks (from 54 datasets) into 6 categories: signal reliability, biometrics and disease, consciousness and state, cognition and emotion, naturalistic stimulus decoding, and motor and interaction. 

stable individual variability, whereas sleep staging, vigilance, emotion recognition, and task-context decoding emphasize time-varying neural dynamics. Second, tasks differ in **temporal scale** , ranging from slow global state estimation to faster perceptual, cognitive, and interaction-related decoding. This dimension separates tasks that can be characterized over extended windows from those requiring more temporally precise predictions. Naturalistic stimulus decoding is included as an important dynamic regime because naturalistic stimuli provide richer and more continuous sensory contexts than classical controlled paradigms [13]. Third, tasks differ in their **interaction regime** , from passive monitoring to active brain-computer interaction. In passive settings, EEG is used to monitor cognitive, affective, or brain-state variables without requiring the user to actively generate control signals. In active settings, the user intentionally modulates mental activity, such as motor imagery, and model predictions may support closed-loop control [15]. 

Under this framing, the six OmniEEG-Bench families cover complementary task regions of EEG: **signal reliability** assesses artifact sensitivity and session consistency, **biometrics and disease** captures trait-like individual and clinical variability, **consciousness and state** targets global brainstate dynamics, **cognition and emotion** covers affective and cognitive changes at intermediate time scales, **naturalistic stimulus decoding** evaluates perceptual and semantic decoding under dynamic real-world stimuli, and **motor and interaction** focuses on time-sensitive intent decoding and control. 

**Type-I: Signal reliability.** This family probes artifact-aware and session-consistent representations. We include (i) ocular artifact/noise identification (EEGDenoiseNet) and (ii) longitudinal stability, where representations of the same participant should remain consistent across sessions (Longitudinal test-retest). 

3 

**Type-II: Biometrics and disease.** This family evaluates clinically and biologically meaningful individual differences. Subtypes include (i) stable traits (MPI-LEMON derived age/gender/personality splits), (ii) epilepsy and abnormalities (HFO, TUAB, TUEP, TUSL, TUEV, and Siena EEG), (iii) neurodevelopmental disorders (ADHD), (iv) neurodegenerative disorders (AD65, PD31, and PD mortality prognosis), and (v) mental disorders (MDD, TDBRAIN, Depression resting, and MODMA). 

**Type-III: Consciousness and state.** This family targets global brain state and slow-to-intermediate dynamics. Subtypes include (i) consciousness level detection (Awakening), (ii) sleep staging (e.g., ISRUC-Sleep I/II/III, Sleep-EDF, and HMC), and (iii) cognitive task identification (e.g., HBN-EEG, PEARL-Neuro, RestCog). 

**Type-IV: Cognition and emotion.** This family covers affective and cognitive labels with more rapid dynamics. We include (i) vigilance detection (SEED-VIG), (ii) emotion recognition across diverse elicitation settings and label granularities, ranging from video-driven affect induction (DEAP, SEED, SEED-IV, SEED-V, SEED-VII, and SEED-FRA, EEG-SVRec, FACED) to music (MusicEEG) and conversational (CIRE) contexts, with label spaces spanning binary valence or arousal classification (DEAP), mid-granularity categorical emotion (SEED/SEED-IV/SEED-V/SEED-VII, 3–7 classes), and more fine-grained categories (FACED, 9 classes), and (iii) cognitive load assessment (EEGMAT and Workload). 

**Type-V: Naturalistic stimulus decoding.** This family targets fast-timescale decoding under naturalistic stimuli, where labels correspond to stimulus attributes or natural listening/reading/viewing context. We include (i) natural speech perception and auditory attention, encompassing multi-class speech phrase discrimination (BCI Speech), selective attention to competing speakers (Broderick, cocktail party), and forward versus reversed speech discrimination (Broderick, reverse); (ii) natural reading with tonal discrimination (ChineseEEG2 reading aloud condition, four Mandarin tones); and (iii) visual semantic categorization (ThingsEEG2, biological vs. non-biological). 

**Type-VI: Motor and interaction.** This family focuses on active intent decoding for control and interaction-centric monitoring. Subtypes include (i) motor imagery (BCIC-IV-2a, BCIC-IV-1, PhysioNet-MI, and SHU-MI), (ii) SSVEP control (BETA-SSVEP, Benchmark-SSVEP, Dual-FreqSSVEP, SSVEP-9-chn), (iii) error-related potential feedback decoding (Monitoring ErrP), and (iv) closed-loop assistive control (EEG-controlled exoskeleton). 

See Appendix A for details and references of the 58 tasks in OmniEEG-Bench. 

## **3 Evaluation Protocols** 

To systematically assess the transferability, data efficiency, and robustness of EEG foundation models, we implement four complementary evaluation paradigms: (i) cross-subject transfer, (ii) multi-subject adaptation, (iii) few-shot adaptation, and (iv) channel masking robustness (Fig. 3). These configurations are materialized through flexible data loading strategies, including cross-subject splits, cross-trial splits, few-shot downsampling, and channel masking. We preprocess the 54 EEG datasets through a standardized pipeline of downsampling, band-pass and notch filtering, common average referencing, and window segmentation (See Appendix I for details). To facilitate efficient benchmarking while maintaining statistical reliability, we randomly select up to 40 samples per subject per class for linear probing (determined by variance stabilization analysis in Appendix D), from which all subsequent splits derive. 

All backbone architectures are wrapped in a common interface that accepts an EEG sample **_x_** _∈_ R<sup>_C×T_</sup> and outputs a representation **_z_** = _fθ_ ( **_x_** ). A lightweight linear classifier _g_ ( _·_ ) maps **_z_** to task logits. We adopt linear probing as the primary evaluation method—freezing the pretrained backbone _θ_ and training only the classification head. This protocol enables heterogeneous models to be evaluated under consistent input specifications and optimization settings. To characterize the performance ceiling of each architecture, we additionally perform full fine-tuning on all the datasets from each task category under the cross-subject setting. We benchmark ten representative EEG foundation models: BENDR, BIOT, LaBraM, CBraMod, BrainOmni, FEMBA, Neuro-GPT, NeuroLM, EEGMamba, and REVE. We report results averaged over multiple independent runs, each using a pre-generated, fixed data split derived from a different random seed. Three runs were employed for cross-subject 

4 



Figure 3: OmniEEG-Bench evaluation pipeline, equipped with four evaluation protocols: crosssubject transfer, multi-subject trial-level adaptation, zero-/few-shot adaptation, and channel-masking robustness. 

transfer and multi-subject adaptation, and five for zero-/few-shot adaptation and channel masking. This ensures fair and comparable performance estimates in the benchmark. The four evaluation protocols are detailed below: 

**Cross-subject transfer and primary leaderboard.** In the _cross-subject_ setting, splits are made at the subject level: subjects are partitioned into train/validation/test groups with a ratio of 8:1:1. For the primary leaderboard, we use cross-subject transfer whenever subject-level splitting is meaningful. For the signal-reliability task (Longitudinal test-retest) that do not admit a standard held-out-subject formulation, we use the corresponding multi-subject protocol as a fallback and include them in the main leaderboard for task coverage. 

**Multi-subject adaptation.** In the _multi-subject_ setting, samples from each subject are split into train/validation/test with an 8:1:1 ratio over trials and pooled across subjects. This setting requires the model to generalize to unseen trials, measuring adaptation when training data spans multiple subjects. 

**Zero-shot and few-shot adaptation.** To quantify data efficiency, we evaluate _few-shot_ adaptation by sampling labeled examples of ratio _k_ per class from the training split ( _k ∈{_ 0 _._ 02 _,_ 0 _._ 05 _,_ 0 _._ 1 _,_ 0 _._ 3 _}_ ). _Zero-shot_ is treated as the _k_ = 0 special case with no dataset-specific supervised training. We compute the pairwise cosine similarity between sample embeddings. For each sample from the test split, we identify its most similar sample from the validation split (to avoid information leakage) in the embedding space and check whether the two samples share the same class label. The prediction is counted as correct if the labels match and incorrect otherwise. The data split follows the cross-subject setting. 

**Channel masking robustness.** To measure the model’s robustness to missing or degraded sensors, we apply _channel masking_ in linear probing: For each sample, a random subset of channels is 

5 



Figure 4: Primary cross-subject-prioritized leaderboard of ten EEG foundation models. 

6 

zero-masked with a corruption ratio _p ∈{_ 20% _,_ 40% _,_ 60% _,_ 80% _}_ . We report the performance with increasing channel corruptions, using fixed corruption seeds across models. The data split also follows the cross-subject setting. 

## **4 Results** 

### **4.1 Primary cross-subject transfer benchmark** 

In the primary linear-probing benchmark, we prioritize cross-subject transfer because EEG foundation models are expected to learn representations that generalize to unseen individuals. For the dataset where cross-subject evaluation is not meaningful or not applicable (Longitudinal test-retest), we use the corresponding multi-subject evaluation as a fallback. Under this cross-subject-prioritized protocol, BrainOmni achieves the best overall average rank, followed by CBraMod and REVE (Fig. 4; see Supplementary Table 5 for detailed accuracy). 

Across tasks, the majority of models achieve above-chance performance. Several tasks are especially difficult, including Parkinson’s detection (PD31), arousal classification (DEAP-arousal), speech attention detection (Broderick-Cocktail-party), natural-versus-reversed speech classification (Broderick-reverse), image concept identification (ThingsEEG2), and error-related potential detection (Monitoring-Errp). Overall, naturalistic stimulus decoding emerges as one of the most challenging task categories for current EEG foundation models. 

Under full fine-tuning, the model rankings change substantially compared with linear probing, with CBraMod, LaBraM, and FEMBA achieving the top three overall ranks with average ranks of 4.51, 4.88, and 5.42, respectively (Supplementary Fig. 3; see Supplementary Table 7 for detailed accuracy). This suggests that these models can benefit substantially from task-specific end-to-end optimization. We further compare EEG foundation models with two task-specific baselines, EEGConformer and EEGNet. Under full fine-tuning, seven foundation models outperform EEGConformer (avg. rank 7.25) and nine outperform EEGNet (avg. rank 8.24), highlighting the advantage of pretrained models after task-specific adaptation. In contrast, under linear probing, only five foundation models surpass EEGConformer (avg. rank 6.66), while five fall behind this baseline (Supplementary Fig. 5), indicating that frozen pretrained representations remain substantially limited for direct transfer. 

### **4.2 Zero-shot and few-shot learning** 

Under few-shot adaptation, BrainOmni exhibits steeper performance scaling with sample size, indicating superior sample efficiency during linear probing (Fig. 5). Task categories display heterogeneous scaling behaviors: Longitidinal test-retest and HMC datasets show gradual, monotonic gains as training data increases. By contrast, most models plateau in FACED, AD65, and Physionet-MI datasets once the few-shot ratio exceeds 0.05. Notably, several models like BrainOmni defy this saturation trend in FACED as well as Physionet-MI datasets, continuing to improve beyond this threshold. 

### **4.3 Robustness to channel corruptions** 

On the longitudinal test-retest dataset, most models exhibit robustness to channel corruption, except for BrainOmni (Fig. 6). On other tasks, performance degrades gradually as channel dropout increases. Notably, BIOT sustains stable performance under moderate corruption (ratios of 0.2 and 0.4). At severe corruption levels (ratios of 0.6 and 0.8), most models collapse to near-chance performance. 

### **4.4 Predictive factors of model performance** 

To identify the key factors that influence the generalization performance of EEG foundation models, we systematically analyzed the relationships between model performance and the number of pretraining datasets, number of training subjects, training hours, model size, publication year, model architecture, pretraining paradigm, tokenization strategy, and spatial modeling design. First, Fig. 1 shows that both the number of pretraining datasets and model size are significantly associated with better average ranks across datasets. Specifically, models pretrained on more datasets tend to achieve lower average ranks, suggesting that dataset diversity is an important factor for improving generalization. Meanwhile, larger models also show better overall rankings, indicating emerging scaling-law 

7 



Figure 5: The performance of zero-shot and few-shot learning. 



Figure 6: The robustness of model performance on channel masking. 

behavior in EEG foundation models. Further per-dataset Spearman correlation analyses support this trend. For each dataset, we computed the Spearman correlation between each model factor and the model rank, and then used a Wilcoxon signed-rank test to assess whether the resulting correlations were systematically different from zero. Because lower ranks indicate better performance, a negative correlation means that a larger value of the corresponding factor is associated with better model performance. The number of pretraining datasets shows a median correlation of _ρ_ = _−_ 0 _._ 27 with a Wilcoxon _p_ = 1 _._ 1 _×_ 10<sup>_−_7</sup> , indicating that the association between dataset diversity and improved performance is consistent across multiple datasets. 

Fig. 7 further compares the effects of different model factors on performance. Among quantitative factors, publication year, model size, and the number of pretraining datasets are all significantly associated with better per-dataset ranks, with publication year showing the strongest correlation. This suggests that more recent EEG foundation models tend to benefit from larger model capacity, richer pretraining data, and updated modeling designs. In contrast, training hours and the number of training subjects show weaker associations with performance, suggesting that simply increasing training time or the number of subjects does not necessarily lead to stable improvements in downstream generalization. Qualitative architecture analyses show that masked reconstruction pretraining, VQbased tokenization, and Criss-Cross spatial modeling each significantly outperform their respective 

8 



<!-- Start of picture text -->
a Factor-performance correlations b Model pretraining/design profiles<br>PublicationYear -0.40 **** 1.0<br>0.8<br>log(# Params) -0.21 ***<br>0.6<br>TrainingHours -0.08<br>0.4<br># TrainingSubjects -0.10<br>0.2<br># PretrainingDatasets -0.27 **** Per-dataset median rhoAvg-rank rho 0.0<br>-1.00 -0.75 -0.50 -0.25 0.00 0.25 0.50 0.75 1.00 Dataset Training Model size Publication<br>Spearman  ρ  (negative = better rank) diversity subjects (log params) year<br>Model<br>BrainOmni REVE BIOT NeuroLM EEGMamba<br>CBraMod FEMBA LaBraM NeuroGPT BENDR<br>c 0 Architecture factor comparisons d Dataset diversity effect per-DS p=1.7e-04***<br>2 **** 2<br>per-DS p=1.1e-08<br>CrissCross<br>4 * per-DS p=4.8e-08 **** per-DS p=1.3e-02 * 4<br>per-DS p=2.4e-02 Masked Recon. VQ-based<br>Transformer-family<br>6 Mamba Non-VQ Others 6<br>Contrastive<br>8<br>8<br>10<br>10<br>Backbone Pretrain Tokenization Spatial Single-dataset Multi-dataset<br>Paradigm Modeling 4 models 6 models<br>Normalized design factor<br>Per-dataset rank<br>Avg Rank (lower is better)<br><!-- End of picture text -->

Figure 7: Pretraining design factors and cross-subject linear-probing performance of EEG foundation models. Quantitative factors are evaluated via per-dataset Spearman correlations with Wilcoxon signed-rank tests (a, b). Per-dataset median rho represents the median correlations of model ranks and the predictive factor on each dataset. Avg-rank rho represents the correlation of average model ranks and the predictive factor. Qualitative factors are compared using paired Wilcoxon tests between model groups (c), and single- versus multi-dataset pretraining is compared via Mann–Whitney U test (d). 

alternatives, indicating that effective architectural and training-objective designs remain critical determinants of performance. Finally, models pretrained on multiple datasets outperform those pretrained on a single dataset overall, further supporting the importance of dataset diversity for EEG foundation model generalization. Overall, these results indicate that improvements in EEG foundation models are not driven by a single factor, but by the joint effects of pretraining data diversity, model scale, temporal progress in model development, and architectural design. 

## **5 Conclusion** 

In this work, we present OmniEEG-Bench, a comprehensive benchmark for evaluating EEG foundation models across 54 datasets and 58 tasks. By organizing downstream EEG evaluation into six task families and standardizing preprocessing, task definitions, and evaluation protocols, OmniEEG-Bench provides a unified testbed for assessing the transferability, data efficiency, and robustness of EEG foundation models. 

Our results show that EEG foundation models can benefit substantially from task-specific finetuning, whereas frozen representations remain limited under direct linear probing. Performance also varies markedly across task families, with naturalistic stimulus decoding posing one of the greatest challenges for current models. Beyond the leaderboard, our diagnostic analyses reveal scaling-law-like trends: models pretrained on more diverse datasets and models with larger parameter counts tend to achieve better average ranks across datasets. These findings suggest that improving EEG foundation models may require not only larger architectures, but also broader and more diverse pretraining data. In addition, VQ-based tokenization and criss-cross spatial modeling are associated 

9 

with stronger downstream performance, indicating that architectural and pretraining-design choices remain critical for generalization. 

By providing a public leaderboard, standardized task cards, and transparent evaluation protocols, OmniEEG-Bench aims to support more reproducible and comparable research on EEG foundation models. We hope that this benchmark will serve as a foundation for tracking progress, diagnosing model limitations, and guiding the development of more generalizable EEG representation learning methods. 

## **6 Limitations** 

In this work, the evaluation is limited to linear probing and full fine-tuning without exploring parameter-efficient transfer strategies. Additionally, the 54 datasets, while diverse, do not exhaustively cover all clinical populations, recording contexts, or geographic regions, and the channel corruption simulation simplifies real-world sensor degradation patterns. 

## **Impact Statement** 

The goal of this paper is to advance the field of brain-computer interfaces through standardized benchmarking of EEG foundation models. EEG data have diverse applications in clinical monitoring, assistive technologies, and neuroscience research, and our work aims to support progress in these areas through systematic, rigorous evaluations. There are potential societal consequences of improvements in EEG-based modeling, including enhanced diagnostic tools and accessible neurotechnologies. However, these developments also raise considerations around data privacy, equitable access, and responsible deployment. Although our benchmark itself does not introduce new modeling techniques, it can accelerate research that impacts users across clinical and consumer domains. We encourage careful consideration of ethical, privacy, and societal implications in subsequent research that builds upon this benchmark. 

10 

## **References** 

- [1] Gayal Kuruppu, Neeraj Wagh, Vaclav Kremen, Sandipan Pati, Gregory Worrell, and Yogatheesan Varatharajah. Eeg foundation models: A critical review of current progress and future directions. _arXiv preprint arXiv:2507.11783_ , 2025. 

- [2] Xinliang Zhou, Chenyu Liu, Zhisheng Chen, Kun Wang, Yi Ding, Ziyu Jia, and Qingsong Wen. Brain foundation models: A survey on advancements in neural signal processing and brain discovery. _arXiv preprint arXiv:2503.00580_ , 2025. 

- [3] Jiamin Wu, Zichen Ren, Junyu Wang, Pengyu Zhu, Yonghao Song, Mianxin Liu, Qihao Zheng, Lei Bai, Wanli Ouyang, and Chunfeng Song. Adabrain-bench: Benchmarking brain foundation models for brain-computer interface applications. _arXiv preprint arXiv:2507.09882_ , 2025. 

- [4] Chaoqi Yang, M Westover, and Jimeng Sun. Biot: Biosignal transformer for cross-data learning in the wild. _Advances in Neural Information Processing Systems_ , 36:78240–78260, 2023. 

- [5] Wei-Bang Jiang, Li-Ming Zhao, and Bao-Liang Lu. Large brain model for learning generic representations with tremendous EEG data in BCI. In _The Twelfth International Conference on Learning Representations_ , 2024. 

- [6] Qinfan Xiao, Ziyun Cui, Chi Zhang, Siqi Chen, Wen Wu, Andrew Thwaites, Alexandra Woolgar, Bowen Zhou, and Chao Zhang. Brainomni: A brain foundation model for unified eeg and meg signals. In _The Thirty-ninth Annual Conference on Neural Information Processing Systems_ , 2025. 

- [7] Hao Zhang, Qing-Qi Zhou, He Chen, Xiao-Qing Hu, Wei-Guang Li, Yang Bai, Jun-Xia Han, Yao Wang, Zhen-Hu Liang, Dan Chen, et al. The applied principles of eeg analysis methods in neuroscience and clinical neurology. _Military Medical Research_ , 10(1):67, 2023. 

- [8] Huy Phan and Kaare Mikkelsen. Automatic sleep staging of eeg signals: recent development, challenges, and future directions. _Physiological Measurement_ , 43(4):04TR01, 2022. 

- [9] Kaido Värbu, Naveed Muhammad, and Yar Muhammad. Past, present, and future of eeg-based bci applications. _Sensors_ , 22(9):3331, 2022. 

- [10] Tijl Grootswagers, Ivy Zhou, Amanda K Robinson, Martin N Hebart, and Thomas A Carlson. Human eeg recordings for 1,854 concepts presented in rapid serial visual presentation streams. _Scientific Data_ , 9(1):3, 2022. 

- [11] Michael P Broderick, Andrew J Anderson, Giovanni M Di Liberto, Michael J Crosse, and Edmund C Lalor. Electrophysiological correlates of semantic dissimilarity reflect the comprehension of natural, narrative speech. _Current Biology_ , 28(5):803–809, 2018. 

- [12] Sitong Chen, Beiqianyi Li, Cuilin He, Dongyang Li, Mingyang Wu, Xinke Shen, Song Wang, Xuetao Wei, Xindi Wang, Haiyan Wu, et al. An eeg dataset for multimodal semantic alignment and neural decoding during reading and listening. _Scientific Data_ , 2025. 

- [13] Saurabh Sonkusare, Michael Breakspear, and Christine Guo. Naturalistic stimuli in neuroscience: critically acclaimed. _Trends in cognitive sciences_ , 23(8):699–714, 2019. 

- [14] Tim Martin, Erica Holliday, Cyril Okhio, Alexis Newman, Lamar LaTella, Makayla Mcginnis, Bruno Giordani, Voyko Kavcic, et al. States, traits, and the resting state eeg task aftereffect. _International Journal of Psychophysiology_ , 210:112523, 2025. 

- [15] Xiaorong Gao, Yijun Wang, Xiaogang Chen, and Shangkai Gao. Interface, interaction, and intelligence in generalized brain–computer interfaces. _Trends in cognitive sciences_ , 25(8):671–684, 2021. 

- [16] Haoming Zhang, Mingqi Zhao, Chen Wei, Dante Mantini, Zherui Li, and Quanying Liu. Eegdenoisenet: a benchmark dataset for deep learning solutions of eeg denoising. _Journal of Neural Engineering_ , 18(5):056057, 2021. 

- [17] Shantanu Sarkar, Kevin Nathan, and Jose L. Contreras-Vidal. "dataset: Eeg-controlled exoskeleton for walking and standing - a longitudinal study of healthy individuals", 2025. 

- [18] Anahit Babayan, Miray Erbey, Deniz Kumral, Janis D Reinelt, Andrea MF Reiter, Josefin Röbbig, H Lina Schaare, Marie Uhlig, Alfred Anwander, Pierre-Louis Bazin, et al. A mind-brain-body dataset of mri, eeg, cognition, emotion, and peripheral physiology in young and old adults. _Scientific data_ , 6(1):1–21, 2019. 

- [19] Dorottya Cserpan, Ece Boran, Richard Rosch, San Pietro Lo Biundo, Georgia Ramantani, and Johannes Sarnthein. "dataset of eeg recordings of pediatric patients with epilepsy based on the 10-20 system ", 2021. 

11 

- [20] Iyad Obeid and Joseph Picone. The temple university hospital eeg data corpus. _Frontiers in Neuroscience_ , Volume 10 - 2016, 2016. 

- [21] Amir Harati, Meysam Golmohammadi, Silvia Lopez, Iyad Obeid, and Joseph Picone. Improved eeg event classification using differential energy. In _IEEE Signal Processing in Medicine and Biology Symposium (SPMB)_ , 2015. 

- [22] Neural Engineering Data Consortium. Temple university eeg corpus - downloads, 2026. 

- [23] Paolo Detti. Siena scalp eeg database. _PhysioNet_ , 2020. 

- [24] Ghasem Sadeghi Bajestani, Shima Abedian, Fatemeh Makhloughi, Motahhareh Raoufitabar, and Hamid Saeedi. A dataset of eeg signals from adults with adhd and healthy controls: Resting state, cognitive function, and sound listening paradigm. _Mendeley Data_ , 2023. 

- [25] Andreas Miltiadous, Katerina D Tzimourta, Theodora Afrantou, Panagiotis Ioannidis, Nikolaos Grigoriadis, Dimitrios G Tsalikakis, Pantelis Angelidis, Markos G Tsipouras, Euripidis Glavas, Nikolaos Giannakeas, et al. A dataset of scalp eeg recordings of alzheimer’s disease, frontotemporal dementia and healthy subjects from routine eeg. _Data_ , 8(6):95, 2023. 

- [26] Alexander P. Rockhill, Nicko Jackson, Jobi George, Adam Aron, and Nicole C. Swann. "uc san diego resting state eeg data from patients with parkinson’s disease", 2021. 

- [27] Simin Jamshidi, Arturo Espinoza, Soura Dasgupta, and Nandakumar Narayanan. "eeg mortality dataset in parkinson’s disease", 2025. 

- [28] Wajid Mumtaz. MDD Patients and Healthy Controls EEG Data (New). 11 2016. 

- [29] Hanneke Van Dijk, Guido Van Wingen, Damiaan Denys, Sebastian Olbrich, Rosalinde Van Ruth, and Martijn Arns. The two decades brainclinics research archive for insights in neurophysiology (tdbrain) database. _Scientific data_ , 9(1):333, 2022. 

- [30] James F Cavanagh jcavanagh@unm.edu. "eeg: Depression rest", 2021. 

- [31] Hanshu Cai, Yiwen Gao, Shuting Sun, et al. Modma dataset: a multi-modal open dataset for mental-disorder analysis. _CoRR_ , abs/2002.09283, 2020. 

- [32] Imad J Bajwa, Andre S Nilsen, René Skukies, Arnfinn Aamodt, Gernot Ernst, Johan F Storm, and Bjørn E Juel. A repeated awakening study exploring the capacity of complexity measures to capture dreaming during propofol sedation. _Scientific Reports_ , 15(1):32746, 2025. 

- [33] Sirvan Khalighi, Teresa Sousa, José Moutinho Santos, and Urbano Nunes. Isruc-sleep: A comprehensive public dataset for sleep researchers. _Computer methods and programs in biomedicine_ , 124:180–192, 2016. 

- [34] Bob Kemp, Aeilko H Zwinderman, Bert Tuk, Hilbert AC Kamphuisen, and Josefien JL Oberye. Analysis of a sleep-dependent neuronal feedback loop: the slow-wave microcontinuity of the eeg. _IEEE Transactions on Biomedical Engineering_ , 47(9):1185–1194, 2000. 

- [35] Diego Alvarez-Estevez and Roselyne Rijsman. Haaglanden medisch centrum sleep staging database. _PhysioNet_ , 2022. 

- [36] Seyed Yahya Shirazi, Alexandre Franco, Maurício Scopel Hoffmann, Nathalia B Esper, Dung Truong, Arnaud Delorme, Michael P Milham, and Scott Makeig. Hbn-eeg: The fair implementation of the healthy brain network (hbn) electroencephalography dataset. _bioRxiv_ , pages 2024–10, 2024. 

- [37] Lindsay M Alexander, Jasmine Escalera, Lei Ai, Charissa Andreotti, Karina Febre, Alexander Mangone, Natan Vega-Potler, Nicolas Langer, Alexis Alexander, Meagan Kovacs, et al. An open resource for transdiagnostic research in pediatric mental health and learning disorders. _Scientific data_ , 4(1):1–26, 2017. 

- [38] Patrycja Dzianok and Ewa Kublik. Pearl-neuro database: Eeg, fmri, health and lifestyle data of middle-aged people at risk of dementia. _Scientific Data_ , 11(1):276, 2024. 

- [39] Ian Daly, Nicoletta Nicolaou, Duncan Williams, Faustina Hwang, Alexis Kirke, Eduardo Miranda, and Slawomir J. Nasuto. "an eeg dataset recorded during affective music listening", 2024. 

- [40] Wei-Long Zheng and Bao-Liang Lu. A multimodal approach to estimating vigilance using eeg and forehead eog. _Journal of neural engineering_ , 14(2):026017, 2017. 

12 

- [41] Sander Koelstra, Christian Muhl, Mohammad Soleymani, Jong-Seok Lee, Ashkan Yazdani, Touradj Ebrahimi, Thierry Pun, Anton Nijholt, and Ioannis Patras. Deap: A database for emotion analysis; using physiological signals. _IEEE transactions on affective computing_ , 3(1):18–31, 2011. 

- [42] Jingjing Chen, Xiaobin Wang, Chen Huang, Xin Hu, Xinke Shen, and Dan Zhang. A large finer-grained affective computing eeg dataset. _Scientific Data_ , 10(1):740, 2023. 

- [43] Ruo-Nan Duan, Jia-Yi Zhu, and Bao-Liang Lu. Differential entropy feature for eeg-based emotion classification. In _2013 6th international IEEE/EMBS conference on neural engineering (NER)_ , pages 81–84. IEEE, 2013. 

- [44] Wei-Long Zheng, Wei Liu, Yifei Lu, Bao-Liang Lu, and Andrzej Cichocki. Emotionmeter: A multimodal framework for recognizing human emotions. _IEEE transactions on cybernetics_ , 49(3):1110–1122, 2018. 

- [45] Wei Liu, Jie-Lin Qiu, Wei-Long Zheng, and Bao-Liang Lu. Comparing recognition performance and robustness of multimodal deep learning models for multimodal emotion recognition. _IEEE Transactions on Cognitive and Developmental Systems_ , 14(2):715–729, 2021. 

- [46] Wei-Bang Jiang, Xuan-Hao Liu, Wei-Long Zheng, and Bao-Liang Lu. Seed-vii: A multimodal dataset of six basic emotions with continuous labels for emotion recognition. _IEEE Transactions on Affective Computing_ , 2024. 

- [47] Syed Anas Imtiaz and Esther Rodriguez-Villegas. An open-source toolbox for standardized use of physionet sleep edf expanded database. In _2015 37th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)_ , pages 6014–6017. IEEE, 2015. 

- [48] Shaorun Zhang, Zhiyu He, Ziyi Ye, Peijie Sun, Qingyao Ai, Min Zhang, and Yiqun Liu. Eeg-svrec: An eeg dataset with user multidimensional affective engagement labels in short video recommendation. In _Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval_ , pages 698–708, 2024. 

- [49] Shengrui He, Zhongjie Li, Jianwu Dang, Yingyi Luo, and Gaoyan Zhang. Cire: A chinese eeg dataset for decoding speech intention modulated by prosodic emotion. _Scientific Data_ , 12(1):1664, 2025. 

- [50] Xin Xu, Xinke Shen, Xuyang Chen, Qingzhu Zhang, Sitian Wang, Yihan Li, Zongsheng Li, Dan Zhang, Mingming Zhang, and Quanying Liu. A multi-context emotional eeg dataset for cross-context emotion decoding. _Scientific Data_ , 12(1):1142, 2025. 

- [51] Igor Zyma, Sergey Tukaev, Ivan Seleznov, Ken Kiyono, Anton Popov, Mariia Chernykh, and Olexii Shpenkov. Electroencephalograms during mental arithmetic task performance. _Data_ , 4(1):14, 2019. 

- [52] Marcel F. Hinss, Emilie S. Jahanpour, Bertille Somon, et al. Open multi-session and multi-task eeg cognitive dataset for passive brain-computer interface applications. _Scientific Data_ , 10:85, 2023. 

- [53] Seong-Whan Lee, Klaus-Robert Müller, and José del R. Millán. 2020 bci competition, track 3, 2020. 

- [54] Alessandro T Gifford, Kshitij Dwivedi, Gemma Roig, and Radoslaw M Cichy. A large and rich eeg dataset for modeling human visual object recognition. _NeuroImage_ , 264:119754, 2022. 

- [55] Benjamin Blankertz, Guido Dornhege, Matthias Krauledat, Klaus-Robert Müller, and Gabriel Curio. The non-invasive berlin brain–computer interface: fast acquisition of effective performance in untrained subjects. _NeuroImage_ , 37(2):539–550, 2007. 

- [56] Clemens Brunner, Robert Leeb, Gernot Müller-Putz, Alois Schlögl, and Gert Pfurtscheller. Bci competition 2008–graz data set a. _Institute for knowledge discovery (laboratory of brain-computer interfaces), Graz University of Technology_ , 16(1-6):34, 2008. 

- [57] Gerwin Schalk, Dennis J McFarland, Thilo Hinterberger, Niels Birbaumer, and Jonathan R Wolpaw. Bci2000: a general-purpose brain-computer interface (bci) system. _IEEE Transactions on biomedical engineering_ , 51(6):1034–1043, 2004. 

- [58] Jun Ma, Banghua Yang, Wenzheng Qiu, Yunzhe Li, Shouwei Gao, and XinXing Xia. SHU Multi-session Dataset. 8 2022. 

- [59] Bingchuan Liu, Xiaoshan Huang, Yijun Wang, Xiaogang Chen, and Xiaorong Gao. Beta: A large benchmark database toward ssvep-bci application. _Frontiers in neuroscience_ , 14:627, 2020. 

- [60] Yijun Wang, Xiaogang Chen, Xiaorong Gao, and Shangkai Gao. A benchmark dataset for ssvep-based braincomputer interfaces. _IEEE Transactions on Neural Systems and Rehabilitation Engineering_ , 25(10):1746– 1752, 2017. 

13 

- [61] Yike Sun, Yuhan Li, Yuzhen Chen, et al. Efficient dual-frequency ssvep brain-computer interface system exploiting interocular visual resource disparities. _Expert Systems with Applications_ , 252:124144, 2024. 

- [62] OpenNeuro. A multimodal neuroimaging dataset to study spatiotemporal dynamics of brain activity and gait during real-world walking with and without a lower-limb exoskeleton, 2025. 

- [63] Ricardo Chavarriaga and José del R Millán. Monitoring error–related potentials. 

- [64] Nadide Gulsah Gulenc and Mahmut Ozturk. Diagnosis of major depressive disorder using eeg signals. In _2024 Innovations in Intelligent Systems and Applications Conference (ASYU)_ , pages 1–6. IEEE, 2024. 

- [65] Anna Tegon, Thorir Mar Ingolfsson, Xiaying Wang, Luca Benini, and Yawei Li. Femba: Efficient and scalable eeg analysis with a bidirectional mamba foundation model. _arXiv preprint arXiv:2502.06438_ , 2025. 

- [66] Wei-Bang Jiang, Yansen Wang, Bao-Liang Lu, and Dongsheng Li. Neurolm: A universal multi-task foundation model for bridging the gap between language and eeg signals. _arXiv preprint arXiv:2409.00101_ , 2024. 

- [67] Jiquan Wang, Sha Zhao, Zhiling Luo, Yangxuan Zhou, Haiteng Jiang, Shijian Li, Tao Li, and Gang Pan. Cbramod: A criss-cross brain foundation model for eeg decoding. _arXiv preprint arXiv:2412.07236_ , 2024. 

- [68] Jiquan Wang, Sha Zhao, Zhiling Luo, Yangxuan Zhou, Shijian Li, and Gang Pan. Eegmamba: An eeg foundation model with mamba. _Neural Networks_ , page 107816, 2025. 

- [69] Wenhui Cui, Woojae Jeong, Philipp Thölke, Takfarinas Medani, Karim Jerbi, Anand A Joshi, and Richard M Leahy. Neuro-gpt: Towards a foundation model for eeg. In _2024 IEEE International Symposium on Biomedical Imaging (ISBI)_ , pages 1–5. IEEE, 2024. 

- [70] Yassine El Ouahidi, Jonathan Lys, Philipp Thölke, Nicolas Farrugia, Bastien Pasdeloup, Vincent Gripon, Karim Jerbi, and Giulia Lioi. Reve: A foundation model for eeg–adapting to any setup with large-scale pretraining on 25,000 subjects. _arXiv preprint arXiv:2510.21585_ , 2025. 

- [71] Demetres Kostas, Stephane Aroca-Ouellette, and Frank Rudzicz. Bendr: Using transformers and a contrastive self-supervised learning task to learn from massive amounts of eeg data. _Frontiers in Human Neuroscience_ , 15:653659, 2021. 

14 

## **A Tasks and datasets** 

This supplementary section provides a complete inventory of the datasets included in OmniEEG-Bench. Supplementary Table 1 summarizes, for each dataset, its assigned taxonomy and subtype, the number of subjects and channels, and a concise description of the corresponding classification objective. See references for detailed information on the datasets. 

_Supplementary Table 1_ . OmniEEG-Bench dataset inventory. 

|Task type|Datasets|#Subjects|#Channels|Sample<br>|Task description|
|---|---|---|---|---|---|
|||||length||
|**Type-I: Signal**|**reliability**|||||
|Artifact<br>identifcation|1. EEGDenoiseNet [16]|1|1|2 s|Single-channel noise-related binary classifcation (2<br>classes).|
|Test-retest<br>|2. Longitudinal test-retest [17]|45|60|2 s|Cross-session subject identifcation (2 classes in the<br>|
|reliability|||||current mounted version).|
|**Type-II: Biome**|**trics and disease**|||||
||3MPI-LEMON-age [18]|203|64|1 s|Age group classifcation derived from the MPI-|
|Biometrics|.||||<br>LEMON cohort (4 groups in the current mounted<br>version).|
||4. MPI-LEMON-gender [18]|203|64|1 s|Gender classifcation derived from the MPI-LEMON<br>cohort(2 classes).|
||5. MPI-LEMON-extraversion<br>|203|64|1 s|Extraversion classifcation (2 classes).|
||[18]|||||
||6. HFO [19]|30|18|2 s|High-frequency oscillation related binary classifcation<br>|
||||||(2 classes).|
|Epilepsy and<br>abnormalities|7. TUAB [20]|325|23|10 s|Clinical normal vs. abnormal EEG classifcation (2<br>classes).|
||8. TUEV[21]|370|32|5 s|EEG event classifcation(6 classes).|
||9. TUEP[20]<br>|200<br>|32<br>|10 s<br>|Seizure-related binaryclassifcation(2 classes).<br>|
||10. TUSL[22]<br>11. Siena EEG[23]|38<br>14|32<br>31|10 s<br>10 s|Sleep-state classifcation(3 classes).<br>Seizure-related binaryclassifcation(2 classes).|
|Neurodevelopme|ntal<br>12. Adult ADHD [24]|121|64|2 s|Healthy vs. ADHD classifcation (2 classes).|
|disorders||||||
|Ndti|13. AD65 [25]|88|19|10 s|Neurodegenerative disease classifcation(3 classes).|
|euroegenera<br>disorders|e<br>14. PD31 [26]|31|64|1 s|Healthy vs. Parkinson’s disease classifcation (2<br>classes).|
||15. PD-Mortality [27]|94|64|2 s|Mortalityvs. survival classifcation(2 classes).|
||16. MDD [28]|63|22|5 s|Healthy vs. major depressive disorder classifcation (2<br>classes)|
|Mental disorders|<br>17. TDBRAIN [29]|285|26|2 s|.<br>Psychiatric phenotype classifcation (4 classes in the<br>current mounted version).|
||18. Depression resting [30]|122|67|1 s|<br>Depression severity groupingvia BDI.|
||19. MODMA [31]|53|128|20 s|Depression / patient vs. control classifcation (2<br>classes).|
|**Type-III: Cons**|**ciousness and state**|||||
|Consciousness|20. Awakening [32]|21|65|10 s|Awake vs. sedation state classifcation (2 classes).|
|level detection||||||
||21. ISRUC-Sleep Subgroup I|57|6|30 s|Sleep stage classifcation (5 classes).|
||[33]|||||
|Sleep staging|22. ISRUC-Sleep Subgroup II<br>[33]|8|6|30 s|Sleep stage classifcation (5 classes).|
||23. ISRUC-Sleep Subgroup|10|6|30 s|Sleep stage classifcation (5 classes).|
||III[33]|||||
||<br>24. Sleep-EDF [34]|153|2|30 s|Sleepstage classifcation(5 classes).|
||25. HMC[35]|124|8|30 s|Sleepstage classifcation(5 classes).|
|Cognitive task|26. HBN-EEG [36, 37]|136|129|2 s|Multi-context task-type classifcation (13 classes in the<br>crrent monted ersion)|
|identifcation|27. PEARL-Neuro [38]|79|128|1 s|u u v.<br>Context/task discrimination classifcation (3 classes in<br>the current mounted version)|
||28. RestCog [39]|60|61|1 s|.<br>Task-type classifcation (5 classes).|
|**Type-IV: Cogn**|**ition and emotion**|||||
|Vigilance detec-|29. SEED-VIG [40]|21|17|8 s|Vigilance state classifcation (3 classes in the current|
|<br>tion|||||<br>mounted version).|
||30. DEAP-arousal [41]|32|32|10 s|High/low arousal classifcation(2 classes).|
||31. DEAP-valence [41]<br>32FACED[42]|32<br>123|32<br>32|10 s<br>10 s|<br>High/low valence classifcation(2 classes).<br>Fine-grained emotion classifcation(9 classes)|
||.  <br>33. SEED [43]|15|62|<br>10 s|.<br>Positive/negative/neutral video-elicited emotion|
||||||classifcation(3 classes).|
|Emotion|34. SEED-IV [44]|15|62|4 s|<br>Emotion classifcation(4 classes).|
|recognition|35. SEED-V [45]|16|62|1 s|Audio-visual elicited emotion classifcation(5 classes).|
||36. SEED-VII [46]|20|62|10 s|Audio-visual elicited emotion classifcation(7 classes).|



15 

|Task type|Tasks|#Subjects|#Channels|Sample<br>Length|Task description|
|---|---|---|---|---|---|
||37. SEED-FRA [47]|8|60|10 s|Emotion classifcation with French movie stimuli (3<br>classes).|
||38. EEG-SvRec [48]|30|69|1 s|Affective / preference related binary classifcation (2<br>classes in the current mounted version).|
||39. CIRE [49]|38|128|2 s|Speech-related affective classifcation (2 classes in the<br>current mounted version).|
||40. MusicEEG[39]|31|19|1 s|Music-evoked emotion classifcation(2 classes).|
||41. EmoEEG-MC [50]|53|64|5 s|Multi-context emotion classifcation.|
|Workload<br>detection|42. EEGMAT [51]|36|21|5 s|Cognitive workload / task-state classifcation (2<br>classes).|
||43. Workload [52]|12|61|2 s|Workload level classifcation(3 classes).|
|**Type-V: Natura**|**listic stimulus decoding**|||||
|Imagined speech|44. BCI-speech[53]|45|64|3 s|Speech intention / keyword classifcation(5 classes).|
|Listening|45. Broderick (cocktail<br>party) [11]|33|69|2 s|Left–right auditory attention classifcation (2 classes).|
||46. Broderick (reverse) [11]|19|69|2 s|Natural vs. time-reversed speech classifcation (2<br>classes).|
|Reading|47. ChineseEEG2 [12]|4|128|2 s|Tone classifcation(4 classes).|
|Visual|48. Things-EEG2 [54]|10|17|1 s|Animate vs. inanimate concept classifcation (2<br>classes).|
|**Type-VI: Motor**|**and interaction**|||||
||49. BCI Competition IV-<br>1[55]|7|59|4 s|Motor imagery classifcation (2 classes).|
|Motor imagery|50. BCI Competition IV-<br>2A[56]|9|22|4 s|Motor imagery classifcation (4 classes).|
||51. PhysioNet-MI[57]|109|64|4 s|Motor imageryclassifcation(4 classes).|
||52. SHU-MI[58]|25|32|4 s|Motor imageryclassifcation(2 classes).|
||53. BETA[59]|70|64|1 s|SSVEP target classifcation(40 classes).|
|SSVEP|54. Benchmark-SSVEP [60]|35|64|2 s|SSVEP target classifcation(40 classes).|
||55. Dual-Freq-SSVEP [61]|14|64|1 s|Dual-frequency SSVEP target classifcation (40<br>classes).|
||56. SSVEP-9-ch[62]|20|9|3 s|SSVEP target classifcation(160 classes).|
|ErrP feedback|57. Monitoring ErrP [63]|6|64|1 s|Error-related potential classifcation (2 classes in the<br>current mounted version).|
|Closed-loop<br>assistive control|58. EEG-Controlled Exoskele-<br>ton [17]|7|60|1 s|Closed-loop control of walking and stopping (2<br>classes).|



## **B The rationale of data windowing** 

Because OmniEEG-Bench integrates datasets with heterogeneous experimental designs, sample length was determined at the dataset level rather than fixed globally. When a dataset or clinical convention defines a standard epoch, we follow that convention. Sleep-staging datasets are segmented into 30-s epochs, consistent with standard sleep-scoring practice and the annotations used in ISRUC-Sleep and Sleep-EDF. EEGDenoiseNet is kept at its native 2-s segment length. For motor imagery datasets, we use the task-relevant imagery interval when available, such as the 4-s cue or imagery period in BCI Competition IV datasets. 

For datasets with longer continuous recordings but no single canonical trial length, we choose windows according to the dominant temporal scale of the downstream task. Resting-state and clinical-state datasets are segmented into windows long enough to capture stable spectral or state-level features while remaining approximately stationary. For example, MODMA uses longer windows (20s) following prior depression-classification practice with long resting-state segments [64]. For naturalistic language and speech datasets, such as ChineseEEG2 and Broderick, the window length (2s) is designed to retain local linguistic or prosodic context while avoiding excessive mixing across adjacent words, sentences, or stimulus events. For SSVEP and closed-loop BCI tasks, we use short windows to emphasize low-latency decoding. 

All segmentation choices are fixed before model evaluation and are applied identically to all models within each dataset. 

## **C Benchmarked EEG foundation models** 

We selected EEG-FMs to provide a representative and reproducible coverage of current foundation-model designs for EEG. Models were included if they provide accessible pretrained weights or reproducible implementations, are intended for general-purpose or cross-dataset EEG representation learning, and can be adapted to the unified OmniEEG-Bench evaluation interface. The selected models span several major methodological families: Transformer-based masked modeling, state-space or Mamba-based sequence modeling, contrastive biosignal representation learning, and multi-task or task-aligned pretraining. They also differ substantially in pretraining 

16 

scale, data diversity, input modality, channel-processing strategy, and model size. This diversity allows OmniEEGBench to evaluate not only which model performs best, but also which design factors are associated with stronger transfer across heterogeneous EEG tasks. Supplementary Table 2 summarizes characteristics of EEG-FMs included in OmniEEG-Bench. Because papers often differ in how they report data volume and parameter counts (e.g., multiple model sizes or partially reported hours), we keep the table faithful to the original disclosures and mark unreported fields accordingly. The underlined parameter size is that of the "base" model and is used in our benchmark. To quantify the data diversity used in the pre-training of each model and exclude the training datasets from evaluation, we list the pre-training datasets for each model in Supplementary Table 3. To ensure reproducibility, we summarize the implementation details of each model in Supplementary Table 4, including the target sampling rate, input shape, channel input policy, and normalization strategy. Notably, models differ substantially in how they handle channel configurations: some accept arbitrary layouts via adaptive encoding (CBraMod) or coordinate-based mapping (BrainOmni), while others require fixed montages such as the 10–20 system (LaBraM, NeuroLM) or predefined bipolar derivations (FEMBA, Neuro-GPT, BIOT). 

## **D Validity of the Downsampled Evaluation Protocol** 

To justify the use of a downsampled evaluation protocol in linear probing, we provide two complementary analyses. We first determine an appropriate number of training samples per class by examining how performance and its variance evolve with increasing sample size. As shown in Supplementary Fig. 1, performance stabilizes beyond approximately 40 samples per class, after which variance across repeated subsampling runs also diminishes. This supports the choice of 40 samples per subject per class as a reliable operating point. We then verify that this downsampled protocol preserves the relative ranking of models compared to using the full dataset, as shown in Supplementary Fig. 2. Model rankings under both protocols remain largely consistent across task categories and evaluation settings, confirming that downsampling does not introduce systematic bias in comparative evaluation. 





Supplementary Fig. 1. Model performance as a function of the number of training samples per class under the downsampled linear probing setting, shown for two representative datasets (ISRUC-S1 and HMC). Error bars denote standard deviation across 15 random subsampling runs. 

## **E Full Fine-tuning Results** 

We report full fine-tuning results under the cross-subject setting in Supplementary Fig. 4. Note that these results are obtained under the same downsampled evaluation protocol (40 samples per subject per class) as described in Supplementary Section D. Compared to linear probing, model rankings shift substantially under full fine-tuning, with LaBraM, NeuroLM, and FEMBA achieving the top three overall ranks. Notably, EEGConformer, included as a task-specific baseline, ranks competitively among foundation models, highlighting the benefit of end-to-end optimization for task-specific adaptation. 

## **F Multi-subject adaptation** 

In the linear probing setting for multi-subject adaptation, CBraMod, REVE, and BrainOmni achieve the top three overall ranks with average ranks of 2.76, 3.25, and 4.36, respectively (Fig. 11; see Supplementary Table 6 for detailed accuracy). The model ranking is broadly consistent with that observed in the cross-subject setting — where BrainOmni, CBraMod, and REVE also occupied the top three positions — with only minor reordering, suggesting that stronger pretrained representations tend to perform well under both cross-trial adaptation and cross-subject transfer. Several tasks remain difficult in the multi-subject setting. Eight models perform near 

17 









Supplementary Fig. 2. Rank consistency between full-sample and downsampled evaluation settings. _Top_ : Scatter plots comparing model ranks under cross-subject (left) and multi-subject (right) protocols, where each point encodes a model (shape) and task category (color). _Bottom_ : Overall model ranking curves under cross-subject (left) and multi-subject (right) protocols; the blue solid line and shaded band denote the mean and min–max range across three seeds under the downsampled setting, and the red dashed line denotes the full-sample rank. 

chance on Chinese tone classification (ChineseEEG2-RA-Tone), and seven models perform near chance on workload classification (Workload), indicating that current EEG foundation models still have limited cross-trial discriminability for these tasks. 

18 



Supplementary Fig. 3. Full fine-tuning results under the cross-subject setting. _Top_ : Average rank across all datasets for each model. _Bottom_ : Per-dataset rank heatmap; lower rank (darker color) indicates better performance. “PT” denotes that the dataset was used in the model’s pretraining and is excluded from ranking. 

19 



Supplementary Fig. 4. Multi-subject transfer ranks of ten EEG foundation models using OmniEEGBench. 

20 

## **G Comparison between Full Fine-tuning and Linear Probing** 

We compare model performance under full fine-tuning and linear probing in Supplementary Fig. 5. Task-specific baselines (EEGConformer and EEGNet, highlighted in blue) are included for reference. 

Under full fine-tuning, the majority of foundation models outperform both task-specific baselines, suggesting that pretrained representations can be effectively adapted through end-to-end optimization. In contrast, under linear probing, the advantage of foundation models diminishes significantly. Many foundation models fail to match or surpass the task-specific baseline EEGConformer (average rank of 6.66), with only five top-performing models outperforming it. This clear performance drop indicates that while some advanced models show promise, many current EEG foundation models still struggle to provide sufficiently strong frozen representations that transfer across heterogeneous datasets without task-specific adaptation. 



<!-- Start of picture text -->
Full fine tuning<br>Linear probing<br><!-- End of picture text -->

Supplementary Fig. 5. Model ranks in full finetuning and linear probing. 

## **H Average model ranks on each task taxonomy** 

Supplementary Fig. 6 summarizes the average rank of each model across different task families under both evaluation protocols (where points closer to the outer edge indicate better ranks). 

Under multi-subject adaptation (left), CBraMod and REVE exhibit the most consistently strong performance, forming the outermost boundaries of the radar chart. Specifically, CBraMod demonstrates exceptional strength in motor & interaction and cognition & emotion tasks, while REVE excels in signal reliability and naturalistic stimulus decoding. 

Under cross-subject transfer (right), the performance landscape shifts, revealing distinct category-specific strengths. BrainOmni emerges as highly competitive, achieving top ranks in motor & interaction and naturalistic stimulus decoding. Other models also display targeted advantages: BIOT notably spikes to the top rank in biometrics & disease, REVE maintains dominance in consciousness & state, and CBraMod remains a strong contender in cognition & emotion. 

Notably, no single model dominates uniformly across all task axes in either setting. The varying shapes of the radar webs emphasize that different model architectures capture complementary aspects of EEG represeantations, and their relative advantages depend heavily on the specific characteristics of the downstream task. 

21 



<!-- Start of picture text -->
Signal Reliability Biometrics & Disease<br>Motor &  Consciousness &  Motor &  Consciousness &<br>Interaction State Interaction State<br>Naturalistic Stimulus Naturalistic Stimulus<br>Cognition & Emotion Cognition & Emotion<br> Decoding Decoding<br>Multi-Subject Cross-Subject<br><!-- End of picture text -->



Supplementary Fig. 6. Average model ranks on each task taxonomy. Left: multi-subject adaptation; Right: cross-subject transfer. 

22 

_Supplementary Table 2_ . Summary of 10 EEG foundation models included in the benchmark. 

|**Model**|**#Training**<br>**subj.**|**Training data**<br>**(h)**|**#Params**<sup>1</sup>|**Input**|**Pre-training**<br>**paradigm**|**Backbone**|**Channel**<br>**processing**|
|---|---|---|---|---|---|---|---|
|BrainOmni [6]|6550|1,997 (EEG) +<br>656 (MEG)|8.4M,<br>37.7M|EEG/MEG|Masked<br>reconstruction<br>(temporal)|Criss-Cross<br>Transformer|Sensor Encoder|
|FEMBA [65]|14,987|27,062|7.8M,<br>16.1M<br>,<br>77.8M,<br>389M|EEG|Masked<br>reconstruction<br>(temporal)|Mamba|fxed channel<br>(10/20)|
|NeuroLM [66]|15,444|27,762|255.1M<br>,<br>500M,<br>1.69B|EEG|Multi-task /<br>autoregressive|Transformer|Unifed channel<br>vocabulary<br>(10–20-based)|
|CBraMod [67]|14,987|27,062|5.0M|EEG|Masked<br>reconstruction<br>(temporal)|Criss-Cross<br>Transformer|Asymmetric<br>Conditional<br>Positional<br>Encoding|
|EEGMamba [68|] Unreported|16,724|3.3M|EEG|Masked<br>reconstruction<br>(temporal)|Mamba|ST-Adaptive<br>Module|
|LaBraM [5]|Unreported|2534.78|5.8M|EEG|Masked<br>reconstruction<br>(frequency)|Transformer|Unifed channel<br>vocabulary<br>(10–20-based)|
|Neuro-<br>GPT [69]|14,987|27,062|78.4M|EEG|Masked<br>reconstruction<br>(temporal)|GPT-2|fxed channel<br>(10/20)|
|REVE [70]|24,274|61,415|69.2M|EEG|Masked<br>Autoencoder|Transformer|Unifed channel<br>embedding|
|BIOT [4]|Unreported|Unreported|3.2M|EEG/ECG|Contrastive<br>learning|Linear<br>Transformer|fxed channel<br>(18-channel<br>bipolar<br>montage)|
|BENDR [71]|14,987|27,062|4.0M|EEG|Contrastive<br>predictive<br>coding|Transformer|fxed channel<br>(10/20)|



## **I Data preprocessing** 

As EEG signals are inherently noisy and complex, rigorous data preprocessing is critical to enhance signal quality and mitigate artifacts. To ensure consistency across heterogeneous datasets and facilitate efficient training of foundation models, we developed a unified HDF5-based benchmarking infrastructure. The standardized pipeline includes filtering, resampling, segmentation, and hierarchical storage. 

**Band-pass and notch filtering.** EEG signals span a wide frequency range, but only specific bands are relevant to cognitive and emotional decoding tasks. We employ a standard 0.1–75 Hz band-pass filter using MNE-Python, preserving crucial task-relevant frequency components (from _δ_ to _γ_ bands) while suppressing low-frequency drifts and high-frequency noise. In addition, a notch filter is dynamically configured (typically 60 Hz or 50 Hz) based on the data collection environment, effectively attenuating mains hum. The 0.1–75 band-pass filter is employed in the original implementation of a majority of EEG foundation models. 

23 

_Supplementary Table 3_ . Pre-training datasets of the foundation models. 

|**Model**|**Pre-training Dataset(s)**|
|---|---|
|BrainOmni|**EEG:**Go-Nogo, MusicEEG, HFO, SRM, RestCog, HBN EO/EC, Features-EEG,<br>PEARL-Neuro, HBN-EEG, Awakening<br>**MEG:**MEG-MASC, MEG-Narrative-Dataset, OMEGA, CC700, AversiveMEG, MIND,<br>SMN4Lang, THINGS-MEG, ASWR-MEG, ImageLine, NeuroMorph, Kymata-SOTO.<br>**Total number: 22**|
|FEMBA|TUEG.**Total number: 1**|
|NeuroLM|TUEG, SEED-IV, SEED-V, SEED-GER, SEED-FRA, BCI Competition IV-1, Emobrain,<br>Grasp and Lift, Inria BCI, Motor Movement/Imagery, Raw EEG Data, Resting State, Siena<br>Scalp EEG Database, SPIS Resting State, Target Versus Non-Target, Self-collected EEG<br>corpus. **Total number: 16**|
|CBraMod|TUEG.**Total number: 1**|
|EEGMamba|TUEG (clean subset) , PhysioNet 2018, Raw EEG Data, Siena Scalp EEG Database, B-<br>SNIP1 (clean subset). **Total number: 5**|
|LaBraM|BCI Competition IV-1, Emobrain, Grasp and Lift EEG Challenge, Inria BCI Challenge,<br>EEG Motor Movement/Imagery Dataset, Raw EEG Data, Resting State EEG Data, SEED,<br>SEED-IV, SEED-GER, SEED-FRA, Siena Scalp EEG Database, SPIS Resting State Dataset,<br>Target Versus Non-Target, TUAR, TUEP, TUSZ, TUSL, Self-collected EEG Data<br>**Total number: 19**|
|Neuro-GPT|TUEG.**Total number: 1**|
|REVE|TUH, Physionet, OpenNeuro (), MOABB.**Total number: 92**|
|BIOT|**EEG:**SHHS, PREST<br>**ECG:**Cardiology<br>**Total number: 3**|
|BENDR|TUEG.**Total number: 1**|



**Resampling.** Raw EEG recordings from different datasets are typically acquired at varying sampling rates (ranging from 128 Hz to 1000 Hz). We resample the EEG signals according to the requirement of each foundation model (250 Hz for Neuro-GPT, 256 Hz for BrainOmni and BENDR, and 200 Hz for others, Supplementary Table 4). 

**Windowing and segmentation.** The data are segmented to generate fixed-length inputs for the model. We employ a sliding window strategy with a dataset-specific window ranging from 1s to 30s (non-overlapping). See Supplementary Table 1 for details. 

**Unified data storage.** To resolve the disparity in raw data formats (e.g., .mat, .edf), all preprocessed data are organized into a standardized HDF5 schema. The root level stores subject-specific attributes (e.g., montage, sampling rate), trial groups organize recording sessions, and segment groups contain the actual preprocessed EEG matrices and synchronized labels, minimizing I/O latency while supporting flexible data splitting strategies during training. The data are split into train/val/test sets separately. 

## **J Detailed results** 

We report the means and standard deviations of balanced accuracy across three runs for linear probing of cross-subject transfer and multi-subject adaptation in Supplementary Tables 5 and 6, respectively. The crosssubject full-finetuning results are reported in Supplementary Table 7. In each table, **bold** entries indicate the best-performing model per dataset, <u>underlined</u> entries indicate the second best, and _italic_ entries indicate performance below the chance level. “–” indicates that the model is incompatible with the dataset due to channel configuration constraints. 

24 

_Supplementary Table 4_ . Implementation details of the 10 EEG foundation models included in the benchmark. 

|**Model**|**Target**<br>**SR (Hz)**|**Bandpass**<br>**Filter (Hz)**|**Channel Policy**|**Normalization**|**Sequence**<br>**Length**|
|---|---|---|---|---|---|
|BrainOmni|256|0.1–96|Maps input channels to<br>standard electrode positions<br>via 3D coordinates|Z-score|Any|
|FEMBA|200|0.1–75|Interpolates to 22-channel<br>TUEG bipolar montage via<br>SSI|IQR normalization|1280 pts|
|NeuroLM|200|0.1–75|Retains channels matching<br>the 10–20 system<br>vocabulary|_÷_100 (_µ_V to<br>0.1 mV)|200 pts/patch|
|CBraMod|200|0.3–75|Accepts arbitrary channel<br>confgurations via ACPE<br>adaptive positional<br>encoding|_÷_100 (_µ_V to<br>0.1 mV)|200 pts/patch|
|EEGMamba|200|0.1–50|Reorders to 19-channel<br>standard layout; missing<br>channels zero-padded|Identity|6000 pts|
|LaBraM|200|0.1–75|Maps channels via 10–20<br>system vocabulary; requires<br>channel ID as input|_÷_100 (_µ_V to<br>0.1 mV)|200 pts/patch|
|Neuro-GPT|250|0.5–100|Interpolates to 22-channel<br>standard montage via SSI|Z-score|500 pts/chunk|
|REVE|256|0.5–99.5|Maps channels via unifed<br>channel embedding; accepts<br>variable confgurations|Z-score|Any|
|BIOT|200|–|Constructs 18-channel<br>bipolar montage (BIOT-18);<br>missing channels<br>zero-padded|P95 absolute<br>scaling|Any|
|BENDR|256|0.1–100|Maps to 19 standard<br>channels plus one<br>relative-amplitude auxiliary<br>channel|Identity (internal<br>min-max)|Any|



25 

_Supplementary Table 5_ . Cross-subject transfer results (balanced accuracy, mean _±_ std over 3 runs). 

|Dataset|#Classe|s<br>BrainOmni|CBraMod|REVE|FEMBA|BIOT|LaBraM|NeuroLM|NeuroGPT|EEGMamba|BENDR|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Type-I**<br>||||||||||||
|Longitudinal test-retest|2|**0.755**_±_**0.006**|0.743_±_0.020|0.725_±_0.025|0.683_±_0.038|0.677_±_0.005|0.745_±_0.018|0.703_±_0.005|0.695_±_0.022|0.639_±_0.014|_0.500±0.000_|
|**Type-II**||||||||||||
|MPI-LEMON-age|4|0.479_±_0.018|0.462_±_0.048|**0.498**_±_**0.030**|0.480_±_0.025|0.477_±_0.033|0.439_±_0.048|0.403_±_0.052|0.426_±_0.046|_0.332±0.001_|0.333_±_0.000|
|MPI-LEMON-gender<br>|2<br>|0.532_±_0.020<br>|**0.644**_±_**0.048**<br>|0.599_±_0.030<br>|0.569_±_0.058<br>|0.587_±_0.060<br>|0.571_±_0.073<br>|0.553_±_0.052<br>|0.545_±_0.055<br>|_0.499±0.001_<br>|_0.500±0.000_<br>|
|MPI-LEMON-extraversion|2|**0.536**_±_**0.013**|_0.481±0.017_|0.505_±_0.026|_0.490±0.012_|_0.463±0.013_|0.509_±_0.039|0.518_±_0.026|_0.464±0.026_|0.504_±_0.005|_0.500±0.000_|
|HFO|2|–|0.563_±_0.026|**0.608**_±_**0.016**|0.525_±_0.011|0.586_±_0.029|0.541_±_0.015|0.537_±_0.009|0.544_±_0.010|0.580_±_0.022|_0.500±0.000_|
|TUAB|2|0.727_±_0.034|–|–|–|**0.793**_±_**0.006**|0.732_±_0.009|–|–|–|–|
|TUEV<br>TUEP|6<br>2|0.467_±_0.034<br>**0596**_±_**0053**|–|–|–|**0.683**_±_**0.075**<br>0588_±_0031|0.417_±_0.056|–|–|–|–|
|TUSL|3|**..**<br>0.450_±_0.051|–<br>–|–<br>–|–<br>–|..<br>**0.645**_±_**0.055**|–<br>–|–<br>–|–<br>–|–<br>–|–<br>–|
|Siena EEG<br>ADHD|2<br>2|0.694_±_0.086<br>0.627_±_0.076|**0.755**_±_**0.171**<br>0.666_±_0.077|0.419_±_0.178<br>0.626_±_0.059|0.439_±_0.206<br>0.602_±_0.018|0.691_±_0.080<br>0.535_±_0.035|–<br>0.580_±_0.084|–<br>0.662_±_0.057|0.479_±_0.106<br>**0.673**_±_**0.110**|–<br>0.552_±_0.082|0.333_±_0.236<br>_0.500±0.000_|
|AD65|3|0.462_±_0.111|**0.582**_±_**0.130**|0.527_±_0.153|0.470_±_0.056|0.491_±_0.089|0.457_±_0.081|0.339_±_0.025|0.410_±_0.071|0.390_±_0.060|0.333_±_0.000|
|PD31|2|_0.406±0.128_|_0.369±0.167_|_0.459±0.076_|0.511_±_0.140|**0.544**_±_**0.129**|_0.280±0.062_|_0.414±0.126_|_0.323±0.135_|_0.336±0.136_|_0.333±0.236_|
|PD-motaility|2<br>|0.501_±_0.003<br>|0.530_±_0.016<br>|0.568_±_0.045<br>|_0.500±0.010_<br>|**0.623**_±_**0.049**<br>|0.516_±_0.017<br>|0.560_±_0.075<br>|0.530_±_0.046<br>|0.501_±_0.003<br>|_0.500±0.000_<br>|
|MDD|2|**0.993**_±_**0.008**|0.826_±_0.121|0.948_±_0.063|0.742_±_0.058|0.861_±_0.075|0.743_±_0.133|0.883_±_0.090|0.640_±_0.055|0.701_±_0.045|_0.500±0.000_|
|TDBRAIN|4|0413_±_0007|**0.446**_±_**0.023**|0437_±_0019|0396_±_0018|0393_±_0030|0391_±_0027|0413_±_0006|0362_±_0008|0323_±_0021|0278_±_0039|
|Depression-resting|2|..<br>0.501_±_0.001|0.509_±_0.009|..<br>0.511_±_0.000|..<br>**0.522**_±_**0.017**|..<br>0.505_±_0.006|..<br>0.500_±_0.000|..<br>0.503_±_0.002|..<br>0.503_±_0.003|..<br>_0.499±0.001_|..<br>_0.500±0.000_|
|MODMA|2|0.657_±_0.152|0.500_±_0.000|0.572_±_0.076|**0.773**_±_**0.072**|0.500_±_0.000|0.500_±_0.000|–|0.544_±_0.000|0.610_±_0.000|0.500_±_0.000|
|**Type-III**||||||||||||
|Awakening|2|–|0.890_±_0.046|0.962_±_0.026|0.961_±_0.026|**0.973**_±_**0.019**|0.934_±_0.041|0.811_±_0.023|0.781_±_0.089|0.833_±_0.024|0.500_±_0.000|
|ISRUC-S1|5|0.615_±_0.021|0.570_±_0.030|**0.658**_±_**0.018**|0.586_±_0.010|0.557_±_0.017|0.558_±_0.032|0.562_±_0.084|0.549_±_0.026|0.501_±_0.046|0.200_±_0.000|
|ISRUC-S2|5|**_0.282_**_±_**_0.010_**|_0.206±0.006_|_0.249±0.023_|_0.242±0.016_|_0.250±0.014_|_0.189±0.012_|_0.207±0.008_|_0.266±0.011_|_0.197±0.007_|_0.200±0.000_|
|ISRUC-S3|5|0.345_±_0.014|0.319_±_0.021|**0.374**_±_**0.025**|0.321_±_0.010|0.345_±_0.033|0.304_±_0.008|0.298_±_0.002|0.289_±_0.030|0.306_±_0.010|_0.200±0.000_|
|SleepEDF|5|0.667_±_0.019|0.690_±_0.016|0.681_±_0.009|0.625_±_0.014|_0.200±0.000_|**0.693**_±_**0.008**|0.685_±_0.015|0.638_±_0.018|0.526_±_0.010|_0.200±0.000_|
|HMC|5|0.664_±_0.017|0.658_±_0.005|**0.682**_±_**0.017**|0.611_±_0.012|0.569_±_0.018|0.630_±_0.011|0.615_±_0.021|0.572_±_0.020|0.551_±_0.014|_0.200±0.000_|
|HBN EEG|13|–|0.136_±_0.007|**0.158**_±_**0.004**|0.118_±_0.006|0.133_±_0.012|0.114_±_0.007|_0.090±0.004_|_0.103±0.004_|_0.100±0.003_|_0.077±0.000_|
|PEARL-Neuro|3|–|**0.535**_±_**0.006**|0.484_±_0.014|0.465_±_0.005|0.462_±_0.012|0.478_±_0.017|0.438_±_0.013|0.437_±_0.012|0.419_±_0.008|0.333_±_0.000|
|RestCog|5|–|**0.368**_±_**0.029**|0.346_±_0.027|0.308_±_0.024|0.350_±_0.025|0.318_±_0.023|0.309_±_0.024|0.276_±_0.017|_0.229±0.006_|_0.200±0.000_|
|**Type-IV**||||||||||||
|SEED-VIG|3|0.432_±_0.014|**0.440**_±_**0.035**|0.418_±_0.064|0.414_±_0.026|0.333_±_0.000|0.437_±_0.025|0.360_±_0.028|0.432_±_0.028|0.350_±_0.059|0.333_±_0.000|
|DEAP-arousal|2|0.505_±_0.024|**0.515**_±_**0.021**|0.508_±_0.029|0.503_±_0.005|0.484_±_0.031|0.478_±_0.007|0.500_±_0.017|0.510_±_0.011|0.487_±_0.025|0.500_±_0.000|
|DEAP-valence|2|0.530_±_0.011|0.519_±_0.020|0.521_±_0.008|0.517_±_0.020|0.498_±_0.049|0.507_±_0.033|0.500_±_0.014|0.494_±_0.023|**0.533**_±_**0.005**|0.500_±_0.000|
|SEED|3|_0.492±0.013_|0.525_±_0.027|**0.543**_±_**0.010**|_0.434±0.008_|_0.430±0.015_|–|_0.399±0.015_|_0.466±0.035_|_0.471±0.012_|_0.333±0.000_|
|SEED-IV|4|0.316_±_0.017|**0.334**_±_**0.005**|0.297_±_0.013|0.303_±_0.009|0.259_±_0.029|–|–|0.292_±_0.006|0.288_±_0.008|0.250_±_0.000|
|SEED-V|5|_0.235±0.003_|_0.234±0.008_|_0.257±0.007_|**_0.290_**_±_**_0.006_**|_0.257±0.010_|_0.241±0.010_|–|_0.242±0.011_|_0.204±0.006_|_0.200±0.000_|
|SEED-VII|7|_0.185±0.008_|_0.176±0.009_|**_0.191_**_±_**_0.006_**|_0.189±0.015_|_0.159±0.006_|_0.187±0.018_|_0.161±0.005_|_0.176±0.008_|_0.181±0.013_|_0.143±0.000_|
|SEED-FRA|3|**0.425**_±_**0.011**|0.417_±_0.013|0.353_±_0.006|0.398_±_0.023|0.385_±_0.013|–|–|0.366_±_0.014|0.409_±_0.003|0.333_±_0.000|
|EEG-SVRec|2|**0.511**_±_**0.003**|0.508_±_0.012|_0.499±0.002_|0.506_±_0.002|0.503_±_0.003|0.510_±_0.005|0.501_±_0.009|_0.500±0.004_|0.504_±_0.005|_0.500±0.000_|
|FACED|9|_0.204±0.002_|**0.481**_±_**0.034**|_0.203±0.016_|_0.174±0.014_|_0.156±0.006_|_0.155±0.020_|_0.170±0.022_|_0.146±0.004_|_0.151±0.011_|_0.111±0.000_|
|MusicEEG|2|–|**0.591**_±_**0.012**|0.528_±_0.059|0.486_±_0.023|0.475_±_0.014|0.524_±_0.032|0.519_±_0.031|0.480_±_0.039|0.528_±_0.045|0.500_±_0.000|
|EmoEEG-MC|10|_0.322±0.015_|0.340_±_0.017|_0.305±0.035_|_0.326±0.010_|_0.332±0.017_|0.340_±_0.017|_0.327±0.009_|_0.328±0.013_|**0.346**_±_**0.020**|0.333_±_0.000|
|CIRE|2|0.531_±_0.017<br>|0.526_±_0.018<br>|**0.538**_±_**0.017**<br>|0.532_±_0.029<br>|0.513_±_0.012<br>|0.535_±_0.025<br>|0.523_±_0.022<br>|0.524_±_0.036<br>|0.528_±_0.021<br>|_0.500±0.000_<br>|
|EEGMAT|2|_0.485±0.022_|_0.500±0.000_|_0.499±0.013_|0.602_±_0.021|0.549_±_0.079|_0.495±0.007_|**0.616**_±_**0.082**|0.522_±_0.035|0.503_±_0.004|_0.498±0.002_|
|Workload|3|0.444_±_0.007|0.470_±_0.042|0.409_±_0.046|0.411_±_0.016|0.466_±_0.009|0.478_±_0.028|**0.496**_±_**0.019**|0.358_±_0.023|0.406_±_0.022|0.333_±_0.000|
|**Type-V**||||||||||||
|BCI-Speech|5|0.225_±_0.010|**0.289**_±_**0.033**|0.223_±_0.009|0.210_±_0.013|0.204_±_0.014|0.203_±_0.011|0.211_±_0.004|0.212_±_0.008|0.197_±_0.012|0.200_±_0.000|
|Broderick-Cocktail-party|2|**0.516**_±_**0.004**|0.384_±_0.052|0.399_±_0.068|0.358_±_0.039|0.346_±_0.085|0.465_±_0.042|0.443_±_0.061|0.336_±_0.229|0.425_±_0.092|0.333_±_0.236|
|Broderick-reverse|2|_0.466±0.046_|0.580_±_0.049|**0.710**_±_**0.138**|_0.499±0.001_|_0.481±0.026_|_0.464±0.052_|_0.492±0.058_|_0.465±0.049_|0.500_±_0.000|_0.500±0.000_|
|ChineseEEG2-RA-Tone|4|_0.252±0.002_|**_0.253_**_±_**_0.004_**|_0.250±0.005_|_0.250±0.001_|_0.253±0.002_|_0.250±0.003_|_0.252±0.001_|_0.250±0.004_|_0.252±0.001_|_0.250±0.000_|
|ThingsEEG2|2|**0.504**_±_**0.001**|_0.500±0.000_|_0.500±0.000_|_0.500±0.000_|_0.500±0.000_|_0.500±0.000_|_0.500±0.000_|0.502_±_0.002|_0.500±0.000_|_0.500±0.000_|
|**Type-VI**||||||||||||
|BCIC-IV-2a|4|_0.303±0.028_|**_0.329_**_±_**_0.006_**|_0.298±0.009_|_0.256±0.002_|_0.250±0.000_|–|–|_0.283±0.016_|_0.289±0.009_|_0.250±0.000_|
|BCICIV1|2|0510_±_0011|**0552**_±_**0031**|0525_±_0035|0507_±_0005|0505_±_0004|0513_±_0008|0503_±_0015|_0463±0009_|0508_±_0010|_0500±0000_|
|--<br>Physionet-MI|4|..<br>_0.307±0.011_|**..**<br>**_0.499_**_±_**_0.007_**|..<br>–|..<br>_0.293±0.007_|..<br>_0.256±0.008_|..<br>_0.280±0.011_|..<br>_0.312±0.016_|_.._<br>_0.305±0.016_|..<br>–|_.._<br>_0.250±0.000_|
|SHUMI|2|**0533**_±_**0018**|0515_±_0009|0523_±_0003|0511_±_0002|0519_±_0014|0507_±_0011|0504_±_0012|0504_±_0002|0490_±_0012|0500_±_0000|
|-<br>BETA-SSVEP|40|**..**<br>_0.037±0.004_|..<br>**_0.103_**_±_**_0.014_**|..<br>_0.043±0.006_|..<br>_0.040±0.007_|..<br>_0.031±0.004_|..<br>_0.032±0.004_|..<br>_0.033±0.004_|..<br>_0.030±0.005_|..<br>_0.028±0.008_|..<br>_0.025±0.000_|
|Benchmark-SSVEP|40|0078_±_0021|**0425**_±_**0103**|0056_±_0008|0051_±_0009|0065_±_0019|0033_±_0003|0032_±_0002|0026_±_0005|0033_±_0006|0025_±_0000|
|Dual-Freq-SSVEP|40|..<br>_0.050±0.004_|**..**<br>**_0.079_**_±_**_0.006_**|..<br>_0.035±0.005_|..<br>_0.030±0.003_|..<br>_0.023±0.006_|..<br>_0.028±0.003_|..<br>_0.027±0.005_|..<br>_0.033±0.008_|..<br>_0.032±0.003_|..<br>_0.025±0.000_|
|SSVEP-9-chn<br>|160<br>|_0.016±0.006_<br>|_0.029±0.002_<br>|**_0.032_**_±_**_0.001_**<br>|_0.008±0.002_<br>|_0.006±0.000_<br>|_0.007±0.001_<br>|_0.013±0.004_<br>|_0.009±0.002_<br>|_0.011±0.002_<br>|_0.006±0.000_<br>|
|Monitoring-Errp<br>EEG-Controlled Exoskeleton|2<br>2|**0.532**_±_**0.022**<br>**0.523**_±_**0.001**|0.498_±_0.008<br>0.513_±_0.021|0.497_±_0.006<br>0.509_±_0.016|0.493_±_0.014<br>0.502_±_0.009|0.498_±_0.002<br>0.488_±_0.057|0.518_±_0.014<br>0.492_±_0.016|0.487_±_0.004<br>0.518_±_0.028|0.482_±_0.014<br>0.522_±_0.023|0.510_±_0.014<br>0.491_±_0.017|0.500_±_0.000<br>0.500_±_0.000|



## **K Regression Tasks** 

We evaluate on SEED-VIG, a vigilance estimation dataset containing 20,355 EEG segments from 21 subjects, where the label is a per-segment continuous value (ratio of eye closure, range [0 _._ 02 _,_ 1 _._ 00]). As shown in Table 11, most models yield near-zero or negative _R_<sup>2</sup> with high variance across seeds, indicating that frozen EEG representations generalize poorly to cross-subject prediction with continuous labels. 

26 

_Supplementary Table 6_ . Multi-subject adaptation results (balanced accuracy, mean _±_ std over 3 runs). 

|Dataset|#Classes|CBraMod|REVE|BrainOmni|FEMBA|LaBraM|NeuroLM|BIOT|NeuroGPT|EEGMamba|BENDR|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Type-I**<br>Longitudinal test-retest|2|**0.755**_±_**0.006**|0.743_±_0.020|0.725_±_0.025|0.683_±_0.038|0.677_±_0.005|0.745_±_0.018|0.703_±_0.005|0.695_±_0.022|0.639_±_0.014|_0.500±0.000_|
|**Type-III**||||||||||||
|Awakening|2|0.888_±_0.049|**0.976**_±_**0.008**|–|0.927_±_0.025|0.854_±_0.077|0.823_±_0.086|0.964_±_0.005|0.776_±_0.067|0.707_±_0.066|0.500_±_0.000|
|HMC|5|0.664_±_0.003|**0.684**_±_**0.005**|0.657_±_0.001|0.588_±_0.005|0.643_±_0.005|0.620_±_0.004|0.575_±_0.001|0.575_±_0.006|0.570_±_0.001|_0.200±0.000_|
|HBN EEG|13|_0.087±0.004_|**0.138**_±_**0.006**|–|_0.108±0.009_|0.117_±_0.006|_0.088±0.003_|0.120_±_0.005|_0.097±0.006_|_0.108±0.006_|_0.079±0.003_|
|RestCog|5|**0.413**_±_**0.001**|0.362_±_0.004|–|0.321_±_0.001|0.339_±_0.002|0.334_±_0.002|0.367_±_0.002|0.293_±_0.001|_0.234±0.003_|_0.200±0.000_|
|**Type-IV**||||||||||||
|DEAP-arousal|2|0.513_±_0.004|**0.514**_±_**0.009**|0.502_±_0.017|0.484_±_0.009|0.495_±_0.010|0.512_±_0.010|0.511_±_0.020|0.505_±_0.006|0.483_±_0.005|0.500_±_0.000|
|DEAP-valence|2|0.516_±_0.016|0.524_±_0.014|0.505_±_0.013|**0.531**_±_**0.004**|0.506_±_0.007|0.504_±_0.003|0.524_±_0.004|0.504_±_0.021|0.509_±_0.009|0.500_±_0.000|
|SEED|3|0.546_±_0.055|**0.576**_±_**0.070**|0.518_±_0.102|_0.457±0.129_|–|_0.438±0.041_|_0.474±0.090_|_0.433±0.039_|_0.420±0.070_|_0.333±0.000_|
|SEED-IV|4|**0.341**_±_**0.014**|0.340_±_0.023|0.305_±_0.013|0.300_±_0.020|–|–|0.303_±_0.006|0.287_±_0.002|0.278_±_0.005|0.250_±_0.000|
|SEED-V|5|**_0.263_**_±_**_0.032_**|_0.251±0.029_|_0.243±0.018_|_0.229±0.007_|_0.211±0.033_|–|_0.216±0.005_|_0.219±0.021_|_0.214±0.013_|_0.200±0.000_|
|SEED-VII|7|_0.191±0.008_|**_0.212_**_±_**_0.021_**|_0.210±0.008_|_0.194±0.006_|_0.191±0.009_|_0.154±0.019_|_0.164±0.006_|_0.185±0.017_|_0.175±0.011_|_0.143±0.000_|
|SEED-FRA|3|**0.441**_±_**0.004**|0.350_±_0.012|0.422_±_0.009|0.421_±_0.028|–|–|0.440_±_0.007|0.372_±_0.016|0.376_±_0.001|0.333_±_0.000|
|FACED|9|**0.484**_±_**0.023**|_0.197±0.010_|_0.194±0.018_|_0.170±0.004_|_0.145±0.006_|_0.171±0.016_|_0.147±0.009_|_0.151±0.004_|_0.144±0.004_|_0.111±0.000_|
|MusicEEG|2|0.480_±_0.034|0.468_±_0.019|–|0.458_±_0.024|0.465_±_0.015|0.470_±_0.020|0.462_±_0.022|0.453_±_0.039|0.490_±_0.010|**0.500**_±_**0.000**|
|CIRE|2|0.545_±_0.014|0.535_±_0.028|**0.554**_±_**0.021**|0.553_±_0.018|0.509_±_0.056|0.518_±_0.019|0.537_±_0.034|0.549_±_0.025|0.519_±_0.064|_0.500±0.000_|
|Workload|3|0.315_±_0.032|_0.242±0.081_|0.313_±_0.029|0.318_±_0.022|0.335_±_0.002|**0.356**_±_**0.024**|0.297_±_0.053|0.259_±_0.073|0.334_±_0.002|0.333_±_0.000|
|**Type-V**||||||||||||
|BCI-Speech|5|**0.321**_±_**0.011**|0.225_±_0.013|0.198_±_0.022|0.214_±_0.014|0.229_±_0.011|0.226_±_0.005|0.213_±_0.007|0.210_±_0.003|0.219_±_0.010|0.200_±_0.000|
|Broderick-Cocktail-party|2|**0.804**_±_**0.006**|0.616_±_0.010|0.525_±_0.000|0.540_±_0.005|0.582_±_0.009|0.558_±_0.002|0.588_±_0.004|0.506_±_0.001|0.502_±_0.005|0.500_±_0.000|
|Broderick-reverse|2|**0.838**_±_**0.017**|0.769_±_0.017|0.554_±_0.013|0.570_±_0.015|0.573_±_0.007|0.634_±_0.014|0.527_±_0.017|0.506_±_0.002|_0.500±0.001_|_0.500±0.000_|
|ChineseEEG2-RA-Tone|4|_0.248±0.007_|**_0.253_**_±_**_0.002_**|_0.247±0.010_|_0.248±0.002_|_0.245±0.004_|_0.248±0.004_|_0.248±0.001_|_0.250±0.006_|_0.247±0.004_|_0.250±0.000_|
|**Type-VI**||||||||||||
|BCIC-IV-2a|4|**_0.401_**_±_**_0.020_**|_0.335±0.005_|_0.308±0.005_|_0.300±0.019_|–|–|_0.250±0.000_|_0.284±0.011_|_0.291±0.005_|_0.250±0.000_|
|Physionet-MI|4|**_0.490_**_±_**_0.016_**|–|_0.291±0.010_|_0.264±0.015_|_0.263±0.016_|_0.285±0.026_|_0.236±0.011_|_0.279±0.016_|–|_0.250±0.000_|
|SHU-MI|2|**0.589**_±_**0.011**|0.538_±_0.013|0.557_±_0.027|0.535_±_0.019|0.506_±_0.015|0.501_±_0.013|0.528_±_0.008|0.497_±_0.012|0.507_±_0.003|0.500_±_0.000|
|BETA-SSVEP|40|**_0.097_**_±_**_0.003_**|_0.037±0.006_|_0.035±0.004_|_0.038±0.006_|_0.029±0.003_|_0.027±0.001_|_0.033±0.003_|_0.025±0.006_|_0.026±0.001_|_0.025±0.000_|
|Dual-Freq-SSVEP|40|**_0.087_**_±_**_0.002_**|_0.036±0.009_|_0.052±0.007_|_0.032±0.005_|_0.020±0.011_|_0.025±0.005_|_0.031±0.006_|_0.023±0.003_|_0.023±0.004_|_0.025±0.000_|
|SSVEP-9-chn|160|_0.023±0.006_|**_0.043_**_±_**_0.002_**|_0.018±0.003_|_0.006±0.001_|_0.007±0.002_|_0.011±0.003_|_0.006±0.000_|_0.007±0.003_|_0.012±0.003_|_0.006±0.000_|
|Monitoring-Errp|2|**0.540**_±_**0.014**|0.503_±_0.016|0.509_±_0.008|0.502_±_0.013|0.519_±_0.006|0.509_±_0.012|0.480_±_0.018|0.501_±_0.007|0.507_±_0.010|0.500_±_0.000|
|EEG-Controlled Exoskeleto|n<br>2|0.544_±_0.004|0.516_±_0.004|0.519_±_0.009|0.519_±_0.008|0.528_±_0.003|0.518_±_0.003|**0.546**_±_**0.003**|0.513_±_0.018|0.505_±_0.005|0.500_±_0.000|



_Supplementary Table 7_ . Cross-subject full-finetuning results (balanced accuracy, mean _±_ std over 3 runs). 

|Dataset<br>|#Classe|s<br>CBraMod|LaBraM|FEMBA|NeuroGPT|NeuroLM|BIOT|BrainOmni|REVE|EEGMamba|EEGConformer|EEGNet|BENDR|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Type-II**||||||||||||||
|MPI-LEMON-age|4|0.581_±_0.051|0.518_±_0.031|0.540_±_0.010|0.537_±_0.019|**0.582**_±_**0.030**|0.485_±_0.008|0.527_±_0.007|0.457_±_0.021|0.502_±_0.004|0.343_±_0.028|0.333_±_0.000|0.333_±_0.000|
|MPI-LEMON-gender<br>|2<br>|**0.692**_±_**0.022**<br>|0.682_±_0.006<br>|0.587_±_0.023<br>|0.636_±_0.010<br>|0.569_±_0.027<br>|0.593_±_0.052<br>|0.587_±_0.002<br>|0.533_±_0.011<br>|0.564_±_0.031<br>|0.578_±_0.033<br>|0.513_±_0.000<br>|_0.500±0.000_<br>|
|MPI-LEMON-extraversion|2|0.552_±_0.010|0.556_±_0.033|0.531_±_0.000|**0.562**_±_**0.014**|0.541_±_0.002|_0.463±0.000_|0.502_±_0.000|0.508_±_0.017|0.506_±_0.015|_0.486±0.041_|_0.471±0.033_|_0.500±0.000_|
|HFO|2|0.603_±_0.016|**0.688**_±_**0.004**<br>|0.546_±_0.012|0.545_±_0.015|0.595_±_0.000|0.647_±_0.030<br>|–<br>|0.528_±_0.022|0.596_±_0.009|0.535_±_0.012<br>|0.529_±_0.014<br>|_0.500±0.000_|
|TUAB|2|–|**0.767**_±_**0.009**|–|–|–|0.761_±_0.016|0.703_±_0.021|–|–|0.687_±_0.037|0.666_±_0.015|–|
|TUEV|6|–|0.606_±_0.032|–|–|–|**0.707**_±_**0.014**|0.615_±_0.046|–|–|0.506_±_0.110|0.434_±_0.117|–|
|TUEP|2|–|–|–|–|–|0.623_±_0.022<br>|0.634_±_0.013<br>|–|–|**0.634**_±_**0.021**<br>|0.585_±_0.011<br>|–|
|TUSL|3|–|–|–|–|–|**0.742**_±_**0.066**|0.624_±_0.180|–|–|0.425_±_0.066|_0.287±0.005_|–|
|Siena EEG|2|0.742_±_0.041|–|0.733_±_0.151|0.491_±_0.082|–|**0.795**_±_**0.033**|0.445_±_0.129|0.573_±_0.022|–|0.715_±_0.117|0.632_±_0.158|0.750_±_0.250|
|ADHD|2|0.640_±_0.093|0.718_±_0.099|**0.728**_±_**0.017**|0.714_±_0.127|0.713_±_0.093|0.593_±_0.004|0.702_±_0.055|0.565_±_0.035|0.645_±_0.108|0.593_±_0.060|0.627_±_0.022|_0.500±0.000_|
|AD65|3|0.612_±_0.048|**0.631**_±_**0.136**|0.616_±_0.133|0.405_±_0.105|0.499_±_0.096|0.567_±_0.001|0.423_±_0.064|0.421_±_0.048|0.546_±_0.192|0.364_±_0.044|0.380_±_0.044|0.333_±_0.000|
|PD31|2|0.563_±_0.000|0.585_±_0.000|0.745_±_0.000|**0.764**_±_**0.000**|_0.098±0.000_|0.602_±_0.000|0.651_±_0.000|0.537_±_0.000|_0.188±0.000_|_0.377±0.190_|_0.272±0.179_|_0.000±0.000_|
|PD-motaility|2|0.664_±_0.106|0.642_±_0.033|0.545_±_0.040|0.506_±_0.008|0.518_±_0.018|**0.683**_±_**0.047**|_0.499±0.014_|0.561_±_0.042|0.579_±_0.006|_0.499±0.003_|_0.500±0.000_|_0.500±0.000_|
|MDD|2|0.736_±_0.259|0.773_±_0.173|0.775_±_0.145|0.885_±_0.048|0.961_±_0.036|0.853_±_0.010|**0.977**_±_**0.015**|0.901_±_0.003|0.870_±_0.083|0.927_±_0.045|0.947_±_0.028|_0.500±0.000_|
|TDBRAIN|4|0.370_±_0.002|0.421_±_0.009|**0.448**_±_**0.044**|0.385_±_0.011|0.423_±_0.069|0.392_±_0.034|0.378_±_0.008|0.345_±_0.000|0.381_±_0.021|0.389_±_0.013|0.379_±_0.024|_0.250±0.000_|
|Depression-resting|2|**0.704**_±_**0.000**|0.519_±_0.000|0.562_±_0.000|0.531_±_0.000|0.580_±_0.000|0.613_±_0.000|0.537_±_0.000|0.519_±_0.000|0.572_±_0.000|_0.500±0.000_|_0.500±0.000_|_0.500±0.000_|
|**Type-III**||||||||||||||
|Awakening|2|0.979_±_0.010|**0.992**_±_**0.008**|0.975_±_0.006|0.975_±_0.009|0.893_±_0.051|0.986_±_0.014|–|0.982_±_0.014|0.955_±_0.033|0.805_±_0.001|0.668_±_0.008|0.500_±_0.000|
|ISRUC-S1|5|0.586_±_0.026|0.653_±_0.051|**0.691**_±_**0.001**|0.666_±_0.005|0.551_±_0.089|0.650_±_0.032|0.629_±_0.030|0.654_±_0.016|0.633_±_0.053|0.495_±_0.027|0.453_±_0.033|0.200_±_0.000|
|ISRUC-S2|5|_0.218±0.002_|_0.196±0.012_|_0.235±0.015_|_0.240±0.012_|_0.199±0.004_|_0.265±0.036_|**_0.276_**_±_**_0.000_**|_0.242±0.013_|_0.241±0.019_|_0.227±0.024_|_0.206±0.007_|_0.200±0.000_|
|ISRUC-S3|5|0.233_±_0.011|0.327_±_0.010|0.333_±_0.064|0.304_±_0.020|0.298_±_0.048|**0.355**_±_**0.039**|0.326_±_0.001|0.303_±_0.021|0.335_±_0.010|0.290_±_0.017|0.255_±_0.029|_0.200±0.000_|
|SleepEDF|5|0.733_±_0.011|**0.745**_±_**0.015**|0.736_±_0.002|0.703_±_0.015|0.740_±_0.006|_0.200±0.000_|0.700_±_0.003|0.733_±_0.008|0.677_±_0.001|0.631_±_0.009|0.587_±_0.018|_0.200±0.000_|
|RestCog|5|0.389_±_0.023|**0.400**_±_**0.026**|0.351_±_0.021|0.390_±_0.033|0.345_±_0.016|0.396_±_0.030|–|0.289_±_0.014|0.345_±_0.020|0.284_±_0.004|0.267_±_0.008|_0.200±0.000_|
|**Type-IV**||||||||||||||
|SEED-VIG|3|0.458_±_0.008|0.479_±_0.031|0.321_±_0.065|0.406_±_0.013|0.439_±_0.012|0.333_±_0.000|**0.505**_±_**0.007**|0.392_±_0.003|0.396_±_0.025|0.340_±_0.008|0.342_±_0.000|0.333_±_0.000|
|EEG-SVRec|2|**0.503**_±_**0.001**|_0.497±0.003_|0.502_±_0.006|_0.498±0.000_|_0.499±0.001_|_0.499±0.005_|_0.498±0.003_|_0.497±0.003_|_0.500±0.001_|_0.498±0.004_|_0.492±0.005_|_0.500±0.000_|
|MusicEEG|2|0.556_±_0.027|0.454_±_0.008|0.492_±_0.067|0.485_±_0.031|0.532_±_0.074|0.378_±_0.068|–|0.499_±_0.038|0.471_±_0.045|0.546_±_0.005|**0.595**_±_**0.030**|0.500_±_0.000|
|CIRE|2|0.524_±_0.006|**0.551**_±_**0.007**|0.515_±_0.010|0.528_±_0.041|0.506_±_0.017|0.523_±_0.013|0.523_±_0.009|0.511_±_0.001|0.544_±_0.031|0.517_±_0.002|0.519_±_0.001|_0.500±0.000_|
|Workload|3|0.400_±_0.011|0.437_±_0.020|0.395_±_0.013|0.404_±_0.010|**0.492**_±_**0.021**|0.447_±_0.037|0.473_±_0.018|0.360_±_0.003|0.400_±_0.015|0.476_±_0.012|0.402_±_0.013|0.333_±_0.000|
|**Type-V**||||||||||||||
|BCI-Speech|5|0.262_±_0.010|0.225_±_0.003|0.249_±_0.003|0.210_±_0.022|0.207_±_0.005|**0.267**_±_**0.025**|0.199_±_0.007|0.208_±_0.012|0.200_±_0.008|0.222_±_0.022|0.206_±_0.009|0.200_±_0.000|
|Broderick-Cocktail-party|2|0.400_±_0.144|0.332_±_0.061|0.432_±_0.028|0.202_±_0.202|0.255_±_0.255|0.388_±_0.051|0.431_±_0.113|0.410_±_0.015|0.421_±_0.064|**0.514**_±_**0.002**|0.503_±_0.004|0.250_±_0.250|
|Broderick-reverse|2|0.688_±_0.116|0.656_±_0.035|0.566_±_0.067|0.570_±_0.051|0.570_±_0.029|_0.459±0.002_|_0.443±0.035_|**0.918**_±_**0.049**|_0.392±0.108_|_0.496±0.003_|_0.500±0.000_|_0.500±0.000_|
|ChineseEEG2-RA-Tone|4|_0.253±0.003_|_0.251±0.003_|_0.252±0.002_|_0.251±0.001_|_0.251±0.001_|_0.252±0.002_|_0.246±0.000_|_0.250±0.001_|**_0.255_**_±_**_0.007_**|_0.253±0.005_|_0.252±0.003_|_0.250±0.000_|
|ThingsEEG2|2|_0.500±0.000_|_0.500±0.000_|_0.498±0.002_|_0.500±0.000_|_0.500±0.000_|_0.498±0.002_|**0.502**_±_**0.002**|_0.500±0.000_|_0.500±0.000_|_0.498±0.002_|_0.498±0.002_|_0.500±0.000_|
|**Type-VI**||||||||||||||
|BCIC-IV-2a|4|_0.372±0.005_|–|**_0.391_**_±_**_0.016_**|_0.309±0.026_|–|_0.250±0.000_|_0.338±0.011_|_0.273±0.007_|_0.324±0.010_|_0.374±0.004_|_0.348±0.023_|_0.250±0.000_|
|BCIC-IV-1|2|0.517_±_0.022|0.507_±_0.028|**0.527**_±_**0.033**|0.502_±_0.013|_0.487±0.003_|_0.458±0.043_|_0.482±0.028_|0.515_±_0.015|_0.490±0.000_|0.502_±_0.007|_0.495±0.030_|_0.500±0.000_|
|Physionet-MI|4|**0.549**_±_**0.000**|0.501_±_0.022|0.519_±_0.020|_0.480±0.007_|0.508_±_0.004|_0.261±0.001_|_0.387±0.017_|–|–|_0.489±0.015_|_0.437±0.016_|_0.250±0.000_|
|SHU-MI|2|0.520_±_0.018|0.525_±_0.009|**0.544**_±_**0.002**|0.500_±_0.002|0.502_±_0.000|0.527_±_0.013|0.536_±_0.021|0.536_±_0.019|0.481_±_0.015|0.525_±_0.034|0.530_±_0.012|0.500_±_0.000|
|BETA-SSVEP|40|**_0.150_**_±_**_0.009_**|_0.100±0.010_|_0.041±0.000_|_0.095±0.005_|_0.082±0.003_|_0.044±0.009_|_0.081±0.001_|_0.100±0.022_|_0.037±0.005_|_0.027±0.000_|_0.028±0.001_|_0.025±0.000_|
|Benchmark-SSVEP|40|0.678_±_0.090|**0.701**_±_**0.096**|0.291_±_0.078|0.617_±_0.090|0.340_±_0.065|0.310_±_0.048|0.268_±_0.011|0.674_±_0.140|0.116_±_0.002|0.036_±_0.004|0.062_±_0.006|0.025_±_0.000|
|Dual-Freq-SSVEP|40|**_0.173_**_±_**_0.027_**|_0.057±0.012_|_0.033±0.005_|_0.052±0.002_|_0.037±0.007_|_0.043±0.010_|_0.067±0.013_|_0.089±0.009_|_0.033±0.002_|_0.033±0.005_|_0.027±0.004_|_0.025±0.000_|
|SSVEP-9-chn|160|**0.227**_±_**0.001**|_0.016±0.004_|_0.005±0.002_|_0.015±0.001_|_0.140±0.026_|_0.006±0.000_|_0.043±0.010_|_0.110±0.009_|_0.020±0.009_|_0.008±0.001_|_0.010±0.000_|_0.006±0.000_|
|Monitoring-Errp|2|0.527_±_0.006|0.491_±_0.015|0.510_±_0.006|0.515_±_0.003|0.509_±_0.006|0.501_±_0.007|0.493_±_0.017|0.507_±_0.008|0.502_±_0.006|**0.542**_±_**0.038**|0.513_±_0.019|0.500_±_0.000|



27 

_Supplementary Table 8._ Linear probing on SEED-VIG vigilance regression (cross-subject, mean _±_ std over 3 seeds). 

|**Model**|_R_<sup>2</sup> _↑_|_r ↑_|RMSE_↓_|
|---|---|---|---|
|BENDR|_−_0_._009_±._008|0_._042_±._038|0_._257_±._039|
|BIOT|_−_0_._064_±._080|_−_0_._082_±._008|0_._270_±._032|
|BrainOmni|_−_0_._073_±._277|0_._428_±._239|0_._259_±._047|
|CBraMod|_−_0_._023_±._433|0_._548_±._207|0_._242_±._028|
|EEGMamba|_−_0_._002_±._272|0_._463_±._139|0_._247_±._025|
|FEMBA|+0_._054_±._190|0_._441_±._167|0_._242_±._032|
|LaBraM|_−_0_._033_±._340|0_._458_±._207|0_._252_±._032|
|NeuroGPT|+0_._076_±._100|0_._443_±._204|0_._238_±._043|
|NeuroLM|_−_0_._019_±._335|0_._550_±._113|0_._249_±._021|
|REVE|_−_0_._296_±._905|0_._559_±._167|0_._270_±._059|



28 

