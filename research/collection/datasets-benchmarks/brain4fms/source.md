# **Brain4FMs: A Benchmark of Foundation Models for Electrical Brain Signals** 

Fanqi Shen shenfanqi@zju.edu.cn Zhejiang University Hangzhou, Zhejiang, China 

## Junru Chen 

jrchen_cali@zju.edu.cn Zhejiang University Hangzhou, Zhejiang, China 

Enhong Yang yeh1115@zju.edu.cn Zhejiang University Hangzhou, Zhejiang, China 

## Xiaoran Pan 

panxiaoran@zju.edu.cn Zhejiang University Hangzhou, Zhejiang, China 

Jiahe Li 

jiaheli@zju.edu.cn Zhejiang University Hangzhou, Zhejiang, China 

Zhizhang Yuan zhizhangyuan@zju.edu.cn Zhejiang University Hangzhou, Zhejiang, China 

Li Meng 

limeng.braindecoder@gmail.com Shanghai Institute of Microsystem and Information Technology, CAS Shanghai, China 

### **Abstract** 

Brain Foundation Models (BFMs) are transforming neuroscience by enabling scalable and transferable learning from neural signals, advancing both clinical diagnostics and cutting-edge neuroscience exploration. Their emergence is powered by large-scale clinical recordings, particularly electroencephalography (EEG) and intracranial EEG, which provide rich temporal and spatial representations of brain dynamics. However, despite their rapid proliferation, the field lacks a unified understanding of existing methodologies and a standardized evaluation framework. To fill this gap, we map the benchmark design space along two axes: (i) from the model perspective, we organize BFMs under a self-supervised learning (SSL) taxonomy; and (ii) from the dataset perspective, we summarize common downstream tasks and curate representative public datasets across clinical and human-centric neurotechnology applications. Building on this consolidation, we introduce Brain4FMs, an open evaluation platform with plug-and-play interfaces that integrates 15 representative BFMs and 18 public datasets. It enables standardized comparisons and analysis of how pretraining data, SSL strategies, and architectures affect generalization and downstream performance, guiding more accurate and transferable BFMs. The code is available at https://anonymous.4open.science/r/Brain4FMs-85B8. 

### **CCS Concepts** 

• **Computing methodologies** → **Machine learning** ; • **Applied computing** → _Health informatics_ . 

### **Keywords** 

Brain Foundation Model, Electroencephalography, Self-Supervised Learning, Benchmarking and Evaluation 

### **1 Introduction** 

Neuroscience is fundamental to understanding the brain and translating insights into societal impact. Beyond supporting clinical 

Yang Yang 

yangya@zju.edu.cn Zhejiang University Hangzhou, Zhejiang, China 

advances in neurological disease detection [86] and sleep staging [2], the study of neural mechanisms drives paradigms in humantechnology interaction, including neural communication [79] and affective computing [118]. Electroencephalography (EEG) and intracranial EEG (iEEG) provide millisecond temporal resolution, high fidelity and direct measurements of neural electrical activity. 

Deep learning has emerged as a powerful tool for neural signal analysis, with architectures such as CNNs, LSTMs, and GNNs achieving promising results in decoding tasks [27, 55, 83]. However, reliance on small, task-specific labeled datasets limits generalization, given the high cost of annotation and inter-subject variability. To overcome these limitations, self-supervised learning (SSL) leverages unlabeled neural data for representation learning [34]. This shift parallels advances in Natural Language Processing (NLP) [21] and Computer Vision (CV) [24], where large-scale pretraining enabled foundation models. A similar transition is emerging in neuroscience, with Brain Foundation Models (BFMs) serving as universal encoders that learn robust representations across subjects and support efficient adaptation to downstream tasks (Figure 1). 

Recent surveys review BFMs from pretraining, architectural, and application perspectives [3, 51, 56, 120]. However, a unified SSL-centric, formulation-based perspective for systematically organizing methods and enabling principled comparison remains lacking. Existing benchmarks are also limited, as they either focus on specific tasks [20, 61] or lack comprehensive coverage of datasets and models [101, 104]. To bridge these gaps, we propose a unified operator-based formulation for SSL pretraining (Figure 1a), and introduce a cross-task benchmark with cross-subject finetuning for standardized evaluation. The main contributions of this paper are: 

- 1) **Unified Taxonomy of SSL Mechanisms.** We present an up-todate, SSL-centric taxonomy for BFMs by abstracting methods into a unified objective and categorizing them into three paradigms, enabling systematic comparison of learning mechanisms. 

- 2) **Extensive Benchmark for BFMs Evaluation.** We construct an open benchmark covering 11 downstream tasks across 18 EEG and 

Shen et al. 



**Figure 1: Overview of BFMs.** (a) A unified pretraining pipeline. EEG/iEEG recordings are preprocessed, encoded into latent representations, and optimized under different SSL paradigms. (b) Model scale statistics. Parameter-size buckets by training paradigm are shown for the reported subset, using each model’s maximum parameter count, alongside yearly model counts under the same grouping. (c) Timeline-style family tree of representative BFMs from 2021 to 2025, organized by paradigm and annotated with major methodological shifts. 

iEEG public datasets, enabling consistent comparison through a standardized preprocessing and evaluation pipeline. 

- 3) **Systematic Analysis.** We perform a comprehensive study on 15 BFMs, analyzing how pretraining data, training strategies, and architectures affect generalization and downstream performance. 

masking operator, while N is the negative set when contrastive objectives are employed. Based on this formulation, we categorize BFMs pretraining strategies into three SSL paradigms. We focus on the underlying learning mechanisms in this section, and defer detailed model instantiations and developments to Appendix A. 

### **2 Model Taxonomy** 

EEG and iEEG are naturally modeled as multivariate time series. We denote a recording as _𝑋_ ∈ R<sup>_𝐶_×</sup><sup>_𝑁_</sup> , where _𝐶_ is the number of channels and _𝑁_ = _𝑓𝑠_ × _𝑡_ is the number of samples over duration _𝑡_ at sampling rate _𝑓𝑠_ . For electrode-wise representations, let _𝜖_ ⊆{1 _, . . . ,𝐶_ } be a subset of electrodes with _𝐸𝑒_ = | _𝜖_ |. The corresponding multivariate time series is _𝑥_<sup>_𝑒_</sup> ∈ R<sup>_𝐸𝑒_×</sup><sup>_𝑁_</sup> . We categorize pretraining pipelines into patch-level and sequence-level formulations. In patch-level modeling, the raw signal _𝑋_ is partitioned along the temporal dimension into _𝑘_ non-overlapping windows of length _𝑤_ =<sup>_<u>𝑁</u>_</sup> _𝑘_<sup>. Objectives are</sup> defined at the patch granularity, and patches are typically treated as exchangeable tokens. Sequence-level modeling preserves the temporal structure and treats the input as an ordered sequence. 

SSL derives training signals from the data, enabling pretraining without manual annotations. Most SSL methods can be viewed as optimizing an objective constructed from transformations and prediction modules applied to the input signal. We form two sets from input, a source set X _𝑠𝑟𝑐_ and a target set X _𝑡𝑔𝑡_ . An encoder F (·) maps the input to a _𝑑_ -dimensional latent representation, followed by an optional module G(·) that serves either as a decoder for reconstruction or as a prediction or alignment head. Under this formulation, SSL methods can be expressed with a unified objective: Lsum = L(G(Q(F(T _𝑑,𝑠_ (X _𝑠𝑟𝑐_ ) _,_ M))) _,_ F(T _𝑑,𝑠_ (X _𝑡𝑔𝑡_ )) _,_ N) (1) 

Here, T _𝑑,𝑠_ = Φ _𝑑_ ◦ _𝑎𝑠_ denotes a deterministic transform composed of domain mapping Φ _𝑑_ and augmentation _𝑎𝑠_ . The tokenizer Q(·) discretizes continuous latent representations. And M denotes a 

### **2.1 Contrastive-based Methods** 

Contrastive-based SSL defines learning objectives by comparing representations of paired inputs and contrasting them against a set of negatives. This paradigm can be expressed as: 



where _𝑧_ 1 = F1 (T _𝑑,𝑠_ (X _𝑠𝑟𝑐,_ M)) and _𝑧_ 2 = F2 (T _𝑑,𝑠_ (X _𝑡𝑔𝑡_ )), F1 (·) produces a query representation from the causal context while F2 (·) generates the target embedding from a future segment. The projection head G(·) maps representations into a latent space. The loss contrasts the positive pair ( _𝑧_ 1 _,𝑧_ 2) with negatives N , promoting alignment of matched pairs and separation from mismatches. 

_2.1.1 Augmentation Contrast._ Augmentation-based method constructs positive pairs by applying transformations to the same input. Given an input _𝑥𝑖_ ∈X _𝑠𝑟𝑐_ , two augmented views are generated as _𝑥𝑖_<sup>1= T</sup><sup>_𝑠_</sup> 1<sup>(</sup><sup>_𝑥𝑖_)and</sup><sup>_𝑥_</sup> _𝑖_<sup>2= T</sup><sup>_𝑠_</sup> 2<sup>(</sup><sup>_𝑥𝑖_), where T</sup><sup>_𝑠_is an augmentation oper-</sup> ator designed to preserve neural semantics. The positive pair is ( _𝑥𝑖_<sup>1</sup><sup>_,𝑥_</sup> _𝑖_<sup>2), while negatives Nare obtained from samples T</sup><sup>_𝑠_(</sup><sup>_𝑥𝑗_)with</sup> _𝑥 𝑗_ ∈X _𝑠𝑟𝑐_ and _𝑗_ ≠ _𝑖_ . For neural signals, effective augmentations must retain physiologically meaningful patterns rather than introducing arbitrary perturbations. Beyond standard time-domain perturbations (e.g., jittering, scaling, and temporal shifts), work explores frequency-domain transformations that selectively suppress or inject spectral components [58, 115] as well as view construction for multichannel recordings [71, 105]. Recent work enforces subjectlevel consistency via same-subject representation alignment [94]. 

Brain4FMs: A Benchmark of Foundation Models for Electrical Brain Signals 

_2.1.2 Contrastive Predictive Coding._ Contrastive Predictive Coding (CPC) [80] formulates contrastive objectives over ordered representations. In CPC-based pretraining, an encoder produces a context representation _𝑐𝑖_ = F1 (T _𝑑,𝑠_ (X _𝑠𝑟𝑐,_ M)), where F1 (·) encodes observations and aggregates past information into a contextual state. Conditioned on _𝑐𝑖_ , the model extracts a target representation _𝑧𝑖_ = F2 (T _𝑑,𝑠_ (X _𝑡𝑔𝑡_ )) from a future segment. Projection operator G(·) maps _𝑐𝑖_ into a latent space, where a contrastive objective aligns the context with future representation _𝑧𝑖_ while contrasting it against negatives. CPC-based BFMs range from sequence-level modeling [49, 122] to spatio-temporal architectures [13]. 

_2.1.3 Cross-modal Contrast._ Cross-modal contrastive learning aligns representations derived from complementary views or modalities that reflect the same neural state. In EEG/iEEG, two views are constructed via the composite transform T (·) and assigned as _𝑥𝑚_ 1 ∈ X _𝑠𝑟𝑐_ and _𝑥𝑚_ 2 ∈X _𝑡𝑔𝑡_ . Features are extracted using modality-specific encoders F1 (·) and F2 (·). Unidirectional alignment is adopted by freezing the target branch with a stop-gradient operator _𝑠𝑔_ [·]. Cross-modal BFMs range from contrasting multiple EEG/iEEGderived views [50, 95] to aligning heterogeneous biosignals [87, 111], and further to EEG/iEEG–multimodal alignment [26, 28]. 

### **2.2 Generative-based Methods** 

Generative-based SSL formulates pretraining objectives by reconstructing or predicting structured targets from transformed inputs, avoiding explicit pair construction and negative sampling [113]. This paradigm has become increasingly prevalent in recent BFMs. Given a transformed input T _𝑑_ ( _𝑥_ ), an encoder F _𝜃_ 1 (·) produces a continuous latent representation _𝑧𝑖_ = F _𝜃_ 1 (T _𝑑_ ( _𝑥𝑖_ )) where _𝑥𝑖_ ∈X _𝑠𝑟𝑐_ . A learnable codebook Q _𝜃_ 3 (·) discretizes _𝑧𝑖_ into a latent embedding, which is then processed by a decoder G _𝜃_ 2 (·) to reconstruct a target view or predict future content. The objective is defined as: 



By minimizing the reconstruction or prediction loss, the model learns latent representations that retain information necessary to recover the underlying signal structure. 

_2.2.1 Autoregressive-based._ Autoregressive (AR) modeling learns representations by causal prediction over ordered sequences [44]. In BFMs, neural signals are cast as token sequences, and learning proceeds via next-token prediction from past context. Given an index _𝑖_ and a prediction window of length _𝑘_ , future tokens are predicted from the causal context _𝑥_ ≤ _𝑖_ ∈X _𝑠𝑟𝑐_ under a causal constraint. ARbased BFMs progress from patch-level prediction with GPT-style decoders [19, 63] to richer spatio-temporal modeling for cross-channel dependencies [70, 98, 108, 119]. Recent work further incorporates prompt-based conditioning for in-context learning [59]. 

_2.2.2 Autoencoder-based._ Autoencoder-based methods learn representations by reconstructing transformed inputs through an encoder–decoder architecture [68] and are widely used in BFMs [47]. An encoder F _𝜃_ 1 (·) maps the input _𝑥𝑖_ or an optional transformed view T _𝑑_ ( _𝑥𝑖_ )) into a latent code, and then decoded by G _𝜃_ 2 (·) to reconstruct a target view. The reconstruction objective encourages the latent space to preserve information required for signal recovery. 

AE-based BFMs evolve from masked reconstruction in the time domain [18, 35, 41, 91] to domain-aware masking strategies operating in spectral or latent space [10, 90, 99, 100, 107, 113]. To better handle multi-electrode recordings, models incorporate spatial inductive biases through channel dictionaries, positional encodings, or graph-structured connectivity, enabling modeling of cross-channel topology [17, 25, 81, 93]. Transformer backbones are increasingly adopted to capture long-range temporal dependencies and spatial interactions [23, 60, 92], and masked learning has been further scaled to iEEG and large-population datasets [31, 90, 107, 112]. 

Recent BFMs further discretize EEG/iEEG signals into token sequences via codebook quantization, bridging autoencoding with token-based generative modeling. This line of work progresses from direct temporal quantization [9] to pretrained VQ-VAE tokenizers [16, 39, 40], and toward more structured codebooks, including time–frequency dual tokenizers [67], topology-aware hierarchical VQ-VAE variants [106], and residual codebooks [10]. Codebooks are objective-agnostic and can also pair with non-AE objectives. 

### **2.3 Other Advanced Methods** 

Beyond the SSL paradigms discussed above, BFMs explore explicit predictive objectives, hybrid formulations, and post-SSL instruction tuning. These methods extend the pretraining framework along dimensions of supervision, objective design, and task alignment. 

_2.3.1 Explicit Predictive-based._ Explicit predictive-based methods learn representations by predicting predefined, interpretable attributes of the signal derived from T _𝑑,𝑠_ (·), such as temporal order, channel configuration, or future patterns. These pretext tasks impose supervised-like objectives grounded in intrinsic signal structure. The general form of the loss is given by: 



where G _𝜃_ 2 (·) denotes a task-specific prediction head, and M is an optional masking operator. In EEG/iEEG applications, predictive targets are often designed to reflect neurophysiological properties [43, 89]. Such objectives rely on predefined predictive targets and are therefore tied to specific assumptions about signal structure. 

_2.3.2 Hybrid-based._ Hybrid SSL combines multiple self-supervised objectives within a unified framework to exploit complementary learning signals [97]. Recent BFMs couple contrastive objectives with generative modeling to jointly capture cross-view consistency and signal structure [14, 52, 54, 91, 96]. Other approaches integrate reconstruction with autoregressive prediction to model both signal structure and temporal dynamics [38, 106], and may further incorporate adversarial objectives for domain-aware alignment [39, 53]. 

_2.3.3 Instruction-tuned._ Instruction tuning is not a self-supervised paradigm, but is typically applied after SSL pretraining as a supervised alignment stage to support multi-task decoding. In this setting, EEG/iEEG features are mapped to LLM-compatible tokens through an adapter or tokenizer Q _𝜃_ 2 , and a pretrained language model G _𝜃_ 3 generates task outputs _𝑦_ conditioned on prompts P: 



Existing designs mainly differ in the choice of tokenization strategies, alignment schemes, and prompt formulations [14, 37, 39, 109]. 

Shen et al. 

### **3 Benchmark** 

To promote standardized and reproducible evaluation, we introduce Brain4FMs, a comprehensive benchmark for BFMs-based electrical brain signal classification. It integrates 15 BFMs and 18 public datasets for systematic cross-task assessment, and provides plugand-play interfaces for adding new models and datasets. 

### **3.1 Pipeline** 

The benchmark focuses on classification tasks, which aims to divide the input electrical brain signal samples _𝑋_ = _𝑥_ 1 _,𝑥_ 2 _, ...,𝑥𝑛_ into pre-defined categories _𝐶_ = _𝑐_ 1 _,𝑐_ 2 _, ...,𝑐𝑚_ , where _𝑥𝑖_ represents the i-th sample, _𝑚_ is the number of categories, and _𝑐𝑖_<sup>′is predicted labels.</sup> The evaluation pipeline is organized into two stages: data preprocessing, followed by model finetuning and evaluation (Figure 2b). Preprocessing includes bandpass and notch filtering, downsampling, event-aligned window segmentation, channel selection, and perchannel z-score normalization. Then, use BFMs with pre-trained weights as the main backbone model _𝑀_ to extract hidden features _𝑧𝑖_ , and fine-tune the model with task-specific classifiers _𝐶𝑙𝑠_ : 



We adopt a cross-subject leave-subjects-out protocol with train/ valid/test splits of approximately 3:1:1, ensuring no data leakage. This setup enforces generalization to unseen subjects and is critical for clinical applicability in neuroscience [107]. Models are evaluated via group-wise cross-validation, with results reported as the mean performance across all test folds for reliable comparison. 

As summarized in Table 1, Brain4FMs includes 15 BFMs spanning diverse pretraining strategies and evaluates them systematically across datasets. All models are tested under identical protocols, enabling fair and comprehensive comparison across neural decoding tasks and supporting robustness assessment across subjects. The included BFMs are chosen from accepted or highly cited works with public code and pretrained weights. 

**Table 1:** Overview of benchmark models, including SSL strategies, BFMs parameters, pretraining data modalities and feature domain. 

|Name|Strategy|Param|Modality|Domain|
|---|---|---|---|---|
|**Contrastive-bas**|**ed Metho**|**d**|||
|SppEEGNet [58]|Aug.|138 K|EEG|time|
|BIOT [105]|Aug.|3.19 M|EEG|time, frequency|
|Bendr [49]|CPC|3.97 M|EEG|time, frequency|
|MBrain [13]|CPC|8.34 M|EEG/iEEG|time, frequency, space|
|**Generative-base**|**d Metho**|**d**|||
|Brant [112]|AE|196.10 M|iEEG|time, frequency, space|
|BFM [9]|AE|708.96 M|EEG|time|
|Brainbert [90]|AE|43.18 M|iEEG|time, frequency|
|CBraMod [92]|AE|4.88 M|EEG|time, frequency, space|
|NeuroGPT [19]|AR|79.62 M|EEG|time, frequency|
|LaBraM [40]|AE|5.80 M|EEG|time, frequency, space|
|BrainWave [107]|AE|102.13 M|EEG+iEEG|time, frequency, space|
|REVE [81]|AE|69.19 M|EEG|time, space|
|BrainOmni [103]|AE|32.71 M|EEG|time, frequency, space|
|**Other Advanced**|**Method**||||
|EEGPT-1 [91]|G & C|51.04 M|EEG|time, space|
|NeuroLM [39]|G & Adv.|169.60 M|EEG|time, frequency|



### **3.2 Dataset Construction** 

Brain4FMs presents a comprehensive benchmark covering 18 public datasets across 11 tasks, grouped into four categories: disease diagnosis, sleep staging, communication [114], and affective computing. Table 2 summarizes widely used datasets that support cross-subject evaluation and comprise EEG or iEEG recordings collected across diverse experimental settings. Most datasets are disjoint from the pretraining corpora of the evaluated BFMs. Pretraining sources, limited overlap, and dataset statistics are provided in Appendix B. 

_3.2.1 Disease Diagnosis._ Neurological disorders are a major global health burden, representing the leading cause of disability and the second leading cause of death worldwide [57]. To support clinically relevant evaluation, Brain4FMs groups disease diagnosis tasks, including Epilepsy, drug-resistant epilepsy (DRE), Parkinson’s Disease (PD), Depression, Major Depression Disorder (MDD), Schizophrenia Disease (SD), Attention Deficit Hyperactivity Disorder (ADHD) and Alzheimer’s Disease (AD). These tasks align with real clinical objectives, featuring cross-subject splits and clinically grounded labels to enable robust, generalizable evaluation. 

_3.2.2 Sleep Staging._ Sleep staging supports the diagnosis and treatment of sleep disorders. Manual scoring of overnight recordings is labor-intensive and time-consuming, motivating automatic sleep stage classification [2]. The task requires modeling long-duration signals and capturing rich time–frequency structure, making robust long-range temporal modeling essential. 

_3.2.3 Communication._ Communication maps neural activity to external outputs, enabling intent expression for users with severe motor impairments. Typical tasks include Motor Imagery (MI), Motor Execution (ME) and decoding speech or semantic intent, translating brain signals into symbolic outputs for spelling, typing, or command selection. 

_3.2.4 Affective Computing._ Affective computing infers internal emotional and cognitive states from EEG or iEEG. Core tasks include emotion recognition and mental workload estimation (MW), which rely on time–frequency and spatial patterns to capture arousal, valence, and cognitive demand across diverse settings. 

### **3.3 Centralized Benchmarking Results** 

We evaluate 22 downstream classification tasks from 18 public datasets, as some datasets contain multiple subtasks. Standard metrics are reported, including Accuracy, AUROC, F1, F2, and Cohen’s _𝜅_ , with full results provided in Appendix D. In our tables, C/G/O/Adv. denote Contrastive/Generative/Other/Adversarial methods, while Aug./Hyb./CB indicate augmentation/hybrid/codebook approaches. Performance varies significantly across tasks, with no single BFMs consistently outperforming others. To interpret these differences and inform future development, we organize our analysis along a typical pipeline, from pretraining data and SSL strategies to model design with a focus on spatial or frequency structure and discrete representations. This motivates the five questions below: 

Q1: How do data composition and modality affect BFMs performance? Q2: How do SSL strategies correlate with cross-task performance? 

Q3: Do BFMs learn task-relevant spatial structure? 

Q4: How is frequency information represented in BFMs across tasks? 

Brain4FMs: A Benchmark of Foundation Models for Electrical Brain Signals 



**Figure 2: Overview of benchmark pipeline.** (a) Data acquisition scenarios covering sleep staging, affective computing, disease diagnosis, and communication. (b) Evaluation under cross-subject and cross-validation protocols, with a standardized EEG/iEEG preprocessing pipeline. 

#### Q5: Do codebook discretization strategies benefit BFMs? 

_3.3.1 Q1: How do data composition and modality affect BFMs performance?_ From a data perspective, a primary factor is the modality of the pretraining corpus. On epilepsy datasets (Table 3), iEEGpretrained models tend to perform better on iEEG cohorts, while EEG-pretrained models favor EEG datasets. For example, Brant, pretrained on iEEG, achieves strong performance on MAYO and FNUSA with high AUROC and Accuracy, but degrades markedly on CHBMIT, revealing pronounced modality dependence. By contrast, BrainWave, pretrained jointly on EEG and iEEG, remains robust across settings, consistent with improved tolerance to domain shift. 

Task-specific supervised baselines are provided as reference points: SPaRCNet [42] for epilepsy, DeprNet [85] for depression, CCNSE [55] for sleep staging, and MSCARNet [4] for communication and affective computing. For completeness, we also report their best results on ADHD, AD, and PD as supervised references rather than task-optimized baselines. Regarding epilepsy and sleep 

**Table 2: Public datasets** used in the benchmark, including signal type, number of subjects (Sub.), and dataset category (Cat.), where H denotes healthy subjects. 

staging benchmarks, BFMs exhibit stronger cross-subject transfer under unified evaluation protocols. Supervised baselines can be competitive but typically outperform only a subset of BFMs. In epilepsy, SPaRCNet outperforms SppEEGNet, NeuroLM, and BFM in both AUROC and accuracy, while most BFMs still achieve higher overall performance. CCNSE achieves moderate AUROC but low accuracy, indicating limited calibration. In contrast, on depression datasets such as MDD-64, DeprNet remains a strong baseline but is surpassed by several BFMs (e.g., REVE, BrainOmni, and BrainWave). Overall, these results indicate that large-scale pretraining yields more transferable representations than task-specific supervised training in most clinical diagnosis settings. 

Communication and affective computing remain challenging for cross-subject generalization [65] due to strong non-stationarity and large cross-subject/inter-session variability (Table 5). The BCItailored supervised baseline MSCARNet shows stronger cross-subject transfer than most BFMs. Although several BFMs show improvements on benchmarks (e.g., NeuroGPT), their overall transfer performance on concept decoding and emotion recognition remains limited. In contrast, MI and MW tasks are more separable, enabling models such as REVE and NeuroGPT to achieve higher Accuracy and AUROC, and BrainOmni performs strongly on EEGMMIDB. 

|Name|Signal|Task|Subject|Cat.|
|---|---|---|---|---|
|CHBMIT [30]|EEG|Epilepsy|23 sub.|2|
|MAYO [75]|iEEG|DRE|25 sub.|2|
|FNUSA [75]|iEEG|DRE|14 sub.|2|
|Dep-BDI [36]|EEG|Depression|122 sub.|2|
|MDD-64 [73]|EEG|MDD|30H, 43MDD|2|
|SD-28 [102]|EEG|SD|28 sub.|2|
|UCSD [84]|EEG|PD|31H, 15PD|2|
|ADFD [69]|EEG|AD|88 sub.|2|
|ADHD_Adult [7]|EEG|ADHD|42H 37ADHD|2|
|ADHD_Child [72]|EEG|ADHD|60H 61ADHD|2|
|ISRUC [46]|EEG|Sleep Stage|100 sub.|5|
|SleepEDFx [45]|EEG|Sleep Stage|44 sub.|5|
|DEAP [48]|EEG|Emotion Recognition|32 sub.|4|
|SEED-IV [117]|EEG|Emotion Recognition|15 sub.|4|
|EEGMat [123]|EEG|MW|36 sub.|2|
|EEGMMIDB [29]|EEG|MI & ME|109 sub.|4|
|BCI-2a [11]|EEG|MI|9 sub.|4|
|Chisco [116]|EEG|Concept Classifcation|5 sub.|39|



**Table 3:** Primary performance metrics of BFMs on epilepsy datasets. We show a representative subset across method types, C/G/O/SL denote contrastive/generative/other/supervised methods. 

||Method|MA|YO|FNU|SA|CHB|MIT|
|---|---|---|---|---|---|---|---|
|Type|Model|AUROC|Acc|AUROC|Acc|AUROC|Acc|
|C|MBrain|.92±.04|.92±.02|.91±.08|.87±.08|.71±.03|.73±.06|
||BIOT|.90±.07|.88±.05|.87±.07|.83±.08|.56±.08|.29±.05|
||SppEEGNet|.56±.03|.75±.05|.64±.08|.67±.05|.43±.05|.60±.06|
|G|BrainWave|**.98±.01**|.93±.02|**.92±.05**|.89±.06|**.90±.03 **|**.80±.12**|
||BrainBERT|.97±.01|**.94±.01**|.90±.04|**.89±.04**|.78±.06|.75±.10|
||LaBraM|.96±.02|.93±.02|.89±.08|.82±.10|.75±.10|.73±.10|
||Brant|.92±.03|.82±.12|.87±.12|.84±.07|.55±.05|.70±.01|
||BrainOmni|.91±.06|.90±.02|.88±.07|.84±.05|.74±.13|.67±.19|
||BFM|.81±.08|.68±.08|.78±.12|.69±.11|.74±.075|.72±.03|
|O|EEGPT|.92±.03|.90±.03|.90±.04|.84±.06|.71±.09|.67±.11|
||NeuroLM|.64±.09|.72±.16|.64±.14|.72±.17|.67±.06|.54±.20|
|SL|SPaRCNet|.83±.10|.83±.08|.85±.10|.82±.11|.61±.10|.66±.05|



Shen et al. 



**Figure 3: Supplemental analyses.** (a) Box plots of decision-boundary diagnostics (q=0.10) comparing contrastive and generative models on cross-subject tasks. (b) AUROC of NeuroGPT variants across tasks. (c) Slopegraph of AUROC changes from original to channel-permuted, comparing spatially strong and weak models. (d) Heatmap of Spearman’s rank correlation between band-wise predictability and model performance rankings across tasks. Points in (a–c) denote n-fold cross-validation means; asterisks in (c-d) indicate *(p<0.05) and **(p<0.001). 

These results suggest that current BFMs capture motor-related neural patterns more reliably than higher-level affective or communicative semantics. Notably, even models pretrained with emotionrelated data (e.g., NeuroLM) may perform competitively in withinsubject settings but still struggle to generalize across subjects. 

_3.3.2 Q2: How do SSL strategies correlate with cross-task performance?_ A consistent paradigm-associated gap is observed: contrastivebased BFMs tend to underperform generative-based ones on most downstream tasks in the benchmark (e.g., seizure detection, AD, SD, and PD). This gap cannot be attributed solely by the SSL objective, as the models also differ in pretraining data, architecture, and scale. To probe the potential role of SSL, decision-boundary diagnostics are conducted on three representative datasets, comparing contrastive and generative models through analyses of their 

**Table 4:** AUROC and Accuracy (Acc) on ME, MW, emotion recognition and concept decoding datasets. Chisco-R results are reported with three decimal places for clarity. 

||EEGMM|IDB-R|EEG|Mat|DE|AP|Chisco-R|
|---|---|---|---|---|---|---|---|
|Model|AUROC|Acc|AUROC|Acc|AUROC|Acc|Acc|
|MBrain|.52±.01|.26±.01|.68±.06|.75±.02|.51±.05|.42±.04|.038±.004|
|BIOT|.50±.01|.25±.01|.59±.08|.27±.01|.50±.03|.30±.06|.037±.003|
|REVE|**.82±.00 **|**.59±.01 **|**.78±.09 **|**.75±.08**|.50±.05|.26±.05|.026±.003|
|NeuroGPT-E|.77±.02|.54±.02|.70±.04|.73±.04|.49±.01|.42±.03|.047±.004|
|NeuroGPT-D|.50±.00|.25±.00|.51±.06|.73±.01|.51±.03|**.44±.04 **|**.048±.003**|
|BrainOmni|.74±.01|.49±.01|.68±.07|.60±.07|.45±.03|.22±.03|.030±.009|
|CBraMod|.57±.01|.30±.02|.63±.06|.72±.04|.51±.01|.19±.02|.025±.009|
|LaBraM|.55±.02|.28±.02|.71±.03|.68±.04|.51±.02|.29±.04|.033±.007|
|BrainBERT|.50±.01|.25±.00|.61±.07|.67±.06|**.52±.02**|.23±.02|.032±.005|
|BrainWave|.50±.01|.25±.01|.66±.06|.51±.20|.51±.03|.27±.07|.029±.005|
|MSCARNet|.80±.01|.57±.01|.59±.06|.74±.01|.51±.04|.39±.03|.047±.004|



embedding spaces and classifier boundaries. Given predicted probabilities _𝑝_ ( _𝑥_ ) and the margin _𝑚_ ( _𝑥_ ) = _𝑝𝑖_ ( _𝑥_ ) − _𝑝 𝑗_ ( _𝑥_ ), the boundary region is defined as B _𝑞_ = _𝑥_ | _𝑚_ ( _𝑥_ ) _< 𝑄𝑞_ ( _𝑚_ ), where _𝑄𝑞_ (·) denotes the _𝑞_ -quantile of the margin distribution. Relative trends remain stable for _𝑞_ ∈ 0 _._ 05 _,_ 0 _._ 10 _,_ 0 _._ 20, _𝑞_ = 0 _._ 10 is therefore used in the main text, with full sensitivity analyses reported in Appendix E. The error-at-boundary proportion _𝐿𝑀𝐸𝑅_ and the boundary-in-errors proportion _𝐿𝑀𝐸𝑆_ are then computed as follows: 



To quantify embedding cluster structure, the class-separation ratio _𝑅𝑐𝑙𝑠_ is adopted, defined as the average inter-class distance divided by the average intra-class distance. Higher values indicate more compact clusters and greater separation between classes. 

Across all three datasets, a consistent pattern emerges. Contrastive models show higher _𝐿𝑀𝐸𝑅_ than generative models, indicating more frequent misclassification in the low-margin boundary region and weaker discrimination near the decision boundary. Generative models, in turn, achieve markedly higher _𝑅𝑐𝑙𝑠_ , reflecting tighter within-class clusters and larger inter-class separation, corresponding to a more separable latent geometry. Notably, despite higher boundary-region error rates, contrastive models often present lower _𝐿𝑀𝐸𝑆_ , indicating that their errors are less concentrated near the boundary. This suggests that generative models primarily fail on ambiguous borderline samples, whereas contrastive models incur errors farther from the boundary, consistent with less stable global geometry and decision surfaces. Results are summarized in Figure 3a, with full quantitative values reported in Appendix E. 

Contrastive BFMs are analyzed by distinguishing augmentation methods from CPC approaches. CPC-based models show stronger robustness and transferability across clinically relevant tasks, with 

Brain4FMs: A Benchmark of Foundation Models for Electrical Brain Signals 

**Table 5: Primary performance metrics on disease disorder and sleep staging.** We show a subset of BFMs across method types and _𝑆𝐿_<sup>†</sup> denotes dataset-specific supervised baselines, MSCARNet for AD/PD/SD, SPaRCNet for ADHD, DeprNet for MDD, and CCNSE for Sleep. 

||Method|ADHD-|Adult|ADHD|-Child|AD|FD|MDD|-64|SD|-28|Sleep|EDF|UCSD|-ON|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|SSL|Model|AUROC|Acc|AUROC|Acc|AUROC|Acc|AUROC|Acc|AUROC|Acc|AUROC|Acc|AUROC|Acc|
|C|MBrain|.95±.03|.92±.04|.69±.11|.63±.08|.53±.12|.50±.10|.93±.08|.87±.11|.58±.10|.58±.10|**.94±.01**|**.79±.04**|.49±.15|.46±.14|
||Bendr|.62±.03|.61±.04|.53±.02|.51±.01|.52±.02|.52±.01|.78±.07|.73±.04|.49±.05|.50±.03|.91±.01|.69±.06|.51±.05|.49±.05|
|G|REVE|.96±.02|.91±.02|**.79±.07**|**.71±.04**|**.84±.07**|**.77±.08**|**.97±.04**|**.88±.09**|.81±.13|.75±.13|.78±.38|.63±.30|.63±.19|**.56±.13**|
||BrainOmni|**.96±.02**|.91±.02|.71±.09|.62±.07|.80±.07|.71±.04|.94±.07|.85±.09|.69±.15|.69±.12|.87±.00|.63±.03|.53±.14|.49±.12|
||BrainWave|.96±.03|.91±.04|.78±.04|.71±.04|.74±.05|.68±.05|.94±.03|.85±.02|**.88±.07**|**.81±.06**|.89±.02|.67±.05|**.69±.20**|.53±.08|
||CBraMod|.95±.02|**.92±.04**|.64±.05|.64±.06|.55±.06|.59±.04|.90±.13|.84±.12|.54±.14|.58±.05|.93±.01|.73±.04|.60±.12|.49±.08|
||LaBraM|.95±.04|.91±.04|.66±.12|.64±.08|.72±.07|.68±.05|.87±.12|.81±.11|.54±.07|.54±.04|.93±.01|.76±.04|.51±.22|.45±.11|
||BrainBERT|.74±.05|.69±.05|.55±.03|.56±.03|.59±.05|.58±.05|.92±.07|.85±.07|.73±.11|.66±.15|.91±.02|.68±.07|.51±.05|.51±.06|
|O|EEGPT|.96±.03|.91±.04|.67±.13|.64±.10|.81±.05|.72±.05|.94±.05|.87±.08|.56±.21|.56±.11|.91±.00|.68±.03|.51±.21|.48±.17|
||NeuroLM|.82±.14|.75±.07|.64±.06|.60±.05|.51±.04|.53±.03|.82±.11|.80±.06|.49±.04|.49±.05|.61±.06|.18±.04|.44±.18|.51±.18|
|_𝑆𝐿_<sup>†</sup>|Dataset-spec|.94±.02|.89±.03|.66±.05|.62±.03|.73±.11|.69±.08|.91±.06|.78±.04|.78±.15|.74±.09|.84±.02|.33±.04|.48±.19|.44±.08|



MBrain emerging as the strongest contrastive baseline, achieving consistently higher AUROC and accuracy. Augmentation methods are not uniformly inferior; for example, BIOT remains competitive for ADHD and AD. Nevertheless, CPC approaches dominate performance on most datasets. This trend aligns with differences in training signals. Augmentation approaches rely on generic perturbations to form positive pairs, which may introduce boundary noise under high inter-subject variability. CPC instead exploits temporal continuity by segment prediction, encouraging representations that preserve physiological dynamics. MBrain integrates multi-channel CPC with a GNN to capture both spatial and long-range temporal dependencies, benefiting time-structured tasks. 

Within the generative family, most BFMs favor AE pretraining over AR paradigms. A plausible explanation lies in the mismatch between AR objectives and downstream EEG/iEEG classification tasks. AR models predict each step from past context, producing inherently unidirectional representations [62], whereas AE-style model aggregates bidirectional context over the entire window. Since most tasks involve global discrimination rather than sequence generation [110], such bidirectional, window-level representations are generally more suitable for feature learning. Controlled experiments on NeuroGPT further support this interpretation. Two variants are finetuned: an encoder-only model (NeuroGPT-E) and an encoder–decoder model (NeuroGPT-D). Both are evaluated across multiple downstream tasks, including epilepsy, sleep staging, MW, and MI in Figure 3b, and full results are reported in Appendix D. NeuroGPT-E consistently outperforms NeuroGPT-D, indicating that finetuning performance in brain signal classification tasks is largely driven by encoder representations, while the decoder contributes more limited gains in this setting. 

_3.3.3 Q3: Do BFMs learn task-relevant spatial structure?_ Several topperforming models in our benchmark, such as BrainWave, BrainOmni, and REVE, are designed with a special structure to capture the multi-channel characteristics of EEG/iEEG signals. This motivates testing whether BFMs internalize dataset-specific spatial structure during training. We therefore apply channel-permutation perturbations to the train/valid splits while keeping the test split unchanged. Spatially strong models (BrainWave, BrainOmni, CBraMod, EEGPT, MBrain, REVE) are compared with spatially weak models 

(BrainBERT, NeuroGPT-E) by examining AUROC changes and assessing statistical significance using paired tests in Figure 3c. And full results are in Appendix F. 

It finds that performance degradation under spatial perturbation is mainly driven by task-specific spatial dependence. We distinguish spatial heterogeneity, which captures region-specific channel statistics, from spatial topology dependence, which requires modeling relative channel organization and propagation. Channel permutation preserves per-channel temporal statistics while removing absolute channel ordering, enabling assessment of topology invariance. Epilepsy is widely regarded as a spatiotemporal network disorder involving seizure onset and propagation across cortical regions [1]. Thus, it shows strong sensitivity to spatial topology, for which channel permutation causes substantial AUROC drops. PD is characterized by region-specific spectral abnormalities [8] and pronounced spatial heterogeneity, resulting in an intermediate sensitivity to permutation. In contrast, ADHD exhibits milder sensitivity. Although its signals are often linked to frontal network dysfunction [74], performance depends less on precise channel adjacency, leading to smaller drops. For AD, where biomarkers primarily reflect global spectral statistics rather than localized cortical patterns [5], most models remain largely unaffected by channel permutation, with BrainWave as a notable exception. 

Clear architectural differences in robustness are further observed. Among spatially weak models, BrainBERT does not explicitly encode channel interactions and is thus insensitive to channel permutation, whereas NeuroGPT-E degrades on some datasets. And for spatially strong models, BrainWave, which uses CNN to capture spatial information, drops on CHBMIT, ADHD-Child, and ADFD, suggesting it may rely on generic inter-channel attention rather than learning dataset-specific spatial structure. EEGPT similarly remains sensitive to channel-identity perturbations on spatially heterogeneous tasks despite implicit channel alignment. In contrast, other spatially strong models are more stable across tasks and datasets. By explicitly encoding channel topology via graph structures, spatial embeddings, or semantic spatial modeling, they encourage learning relative spatial topology rather than absolute channel indices, improving robustness to channel reconfiguration. 

Shen et al. 

_3.3.4 Q4: How is frequency information represented in BFMs across tasks?_ Models reconstructing frequency-domain features (e.g., BrainWave, BrainBERT, LaBraM) demonstrate strong performance across tasks, particularly in disease diagnosis. This aligns with evidence that different frequency bands encode distinct cognitive and pathological states [12]. Compared with raw waveforms, which entangle multiple oscillatory components with noise, transformed representations make the oscillatory structure more explicit. Reconstruction in frequency domains, therefore, encourages models to capture band-structured statistics tied to neural rhythms, which may better match EEG/iEEG physiology than fitting the raw signal. 

Motivated by this, we probe whether BFMs encode dominant frequency bands (six bands; Figure 3d) by freezing the fine-tuned encoder and training a lightweight band-wise Power Spectral Density (PSD) head that maps embeddings to the band-specific PSD profiles via separate linear heads per band. Let _𝑃𝑏_ ( _𝑥_ ) and _𝑃_<sup>ˆ</sup> _𝑏_ ( _𝑥_ ) denote the ground-truth and predicted PSD for band _𝑏_ . We measure band predictability by _𝑟𝑏_ = corr( _𝑃𝑏_ ( _𝑥_ ) _, 𝑃_<sup>ˆ</sup> _𝑏_ ( _𝑥_ )), then normalize _𝑟𝑏_ across bands to obtain each band’s relative predictive strength as _𝑟_<sup>_𝑛_</sup> _𝑏_<sup>, with detailed results reported in Appendix G. Finally, Spearman</sup> rank correlation and significance are computed between _𝑟𝑏_<sup>_𝑛_and</sup> downstream performance rankings, primarily based on AUROC, to link frequency encoding with task performance. 

The results show clear task-dependent patterns. In ADFD, the relative predictability of _𝛼_ and _𝛾𝑙_ is significantly correlated with performance ranking. In depression tasks, correlations are uniformly weak and non-significant. In ADHD-Adult, _𝛽_ and _𝛾𝑙_ show significant positive correlations, whereas _𝜃_ is negatively correlated. In ADHD-Child, _𝛼_ , _𝛽_ , and _𝛾𝑙_ are all significantly associated with performance, with _𝛽_ being the strongest. Across several datasets, band-wise relative predictability shows a consistent association with performance ranking. Clinically, AD is often linked to elevated _𝛿_ / _𝛼_ and _𝜃_ / _𝛼_ ratios [76], while ADHD studies highlight the relevance of _𝜃_ / _𝛽_ -related markers [64]. It suggests that BFMs emphasize different frequency bands across tasks, and some salient bands are task-relevant. This task-adaptive frequency emphasis may help guide improvements in downstream performance. 

_3.3.5 Q5: Do codebook discretization strategies benefit BFMs?_ Discrete codebooks have recently been introduced in BFMs to improve representation stability and generalization. To assess the impact of codebook design on representation usage and discriminability, three benchmark models with explicit discretization (BFM, LaBraM, BrainOmni) are analyzed. These models adopt distinct mechanisms. BFM applies the tokenizer from Chronos to discretize raw signals into token IDs. LaBraM discretizes encoder features during pretraining via a VQ-VAE but removes the codebook during finetuning. BrainOmni follows a similar paradigm but employs multi-layer residual vector quantization (RVQ). We analyze codebook behavior on the test set by characterizing token-embedding geometry, using _𝑖𝑛𝑡𝑒𝑟_ to measure class-wise center similarity and distance ratio ( _𝐷𝑅_ ) to quantify inter-intra class separation. 

It observes clear design-dependent behaviors. BFM activates many tokens with high coverage and entropy, yet exhibits extremely high _𝑖𝑛𝑡𝑒𝑟_ and low _𝐷𝑅_ , suggesting that a generic temporal codebook favors cross-domain robustness but is hard to encode task-specific EEG/iEEG semantics. LaBraM shows sparser and 

**Table 6: Codebook token usage and class geometry under different settings.** We report the coverage (Cov.) and entropy (Ent.) of token, mean inter-class similarity (inter), and inter-/intraclass distance ratio (DR) for BFM, fine-tuned and non–fine-tuned LaBraM ( _𝐿𝑎𝐵𝑟𝑎𝑀𝑛𝑜_ ), and BrainOmni with four RVQ layers. 

|||A|DFD||CH|BMIT||SD|-28|
|---|---|---|---|---|---|---|---|---|---|
|Model|Cov.|Ent.|inter|DR|Cov. Ent.|inter|DR|Cov. Ent.|inter DR|
|BFM|.430|.868|.998|.002|.635 .838|.999|.001|.547 .853|.999 .001|
|BrainOmni1|.997|**.947**|.996|.007|.988 .948|.999|.001|.964 .941|.999 .002|
|BrainOmni2|.998|.891|.928|.077|.998 .950|.966|.037|.998 **.982**|.994 .007|
|BrainOmni3|.998|.929|.927|.076|.998 .970|.959|.043|.998 .973|.954 .049|
|BrainOmni4|.998|.946|.947|.055|.998 **.988**|.930|.072|.998 .972|.909 .094|
|LaBraM_𝑛𝑜_|.353|.755|.995|.006|.369 .721|.973|.038|.171 .607|.986 .022|
|LaBraM|.140|.694|**.267 **|**1.155**|.093 .518|**-.954 **|**6.755**|.043 .586|**.800 .294**|



more preferential token usage, although its _𝑖𝑛𝑡𝑒𝑟_ and _𝐷𝑅_ improve over BFM, class separation remains weak, indicating that the pretrained codebook cannot directly transfer into class-discriminative geometry for downstream tasks. In contrast, BrainOmni’s hierarchical RVQ maintains high token coverage and entropy, and as the residual level deepens, _𝐷𝑅_ tends to increase. This suggests that coarse-to-fine discretization can mitigate codebook collapse and progressively introduce more class-discriminative structure. Further, fine-tuning LaBraM’s codebook results in decreased token coverage and entropy, alongside increased class separation, indicating that the codebook is able to adapt to new tasks. However, reusing discretization during finetuning still degrades downstream performance, suggesting quantization may constrain discriminative flexibility and discard fine-grained cues (Appendix H). Overall, the results in Table 6 highlight hierarchical discretization as a promising route to balance robustness and capacity for BFMs. 

### **4 Conclusion** 

Brain4FMs provides a unified, plug-and-play framework for analyzing BFMs. We organize BFMs with an SSL-centric taxonomy and evaluate 15 models on 18 public datasets under standardized crosssubject finetuning, enabling fair and reproducible comparison. Our analyses relate performance variation to key factors, including pretraining data composition, SSL strategy, and model design. Together, Brain4FMs offers a solid reference for future BFMs development and supports transparent, comparable, and extensible evaluation in this rapidly evolving field. We plan to extend the benchmark with frozen-encoder, few-shot, and zero-shot settings, and to keep the open-source leaderboard up to date. 

### **References** 

- [1] 2020. Ictal EEG source localization in focal epilepsy: Review and future perspectives. _Clinical Neurophysiology_ 131, 11 (2020), 2600–2616. 

- [2] Khald Ali I Aboalayon, Miad Faezipour, Wafaa S Almuhammadi, and Saeid Moslehpour. 2016. Sleep stage classification using EEG signal analysis: a comprehensive survey and new investigation. _Entropy_ 18, 9 (2016), 272. 

- [3] Hamdi Altaheri, Fakhri Karray, Md Milon Islam, SM Raju, and Amir-Hossein Karimi. 2025. Bridging Brain with Foundation Models through Self-Supervised Learning. _arXiv preprint arXiv:2506.16009_ (2025). 

- [4] Danilo Avola, Luigi Cinque, Angelo Di Mambro, Romeo Lanzino, Daniele Pannone, and Francesco Scarcello. 2024. Multi-stream 1d CNN for EEG motor imagery classification of limbs activation. _IEEE Access_ 12 (2024), 83940–83951. 

- [5] Claudio Babiloni, Raffaele Ferri, Davide V Moretti, Andrea Strambi, Giuliano Binetti, Gloria Dal Forno, Florinda Ferreri, Bartolo Lanuzza, Claudio Bonato, 

Brain4FMs: A Benchmark of Foundation Models for Electrical Brain Signals 

Flavio Nobili, et al. 2004. Abnormal fronto-parietal coupling of brain rhythms in mild Alzheimer’s disease: A multicentric EEG study. _European Journal of Neuroscience_ 19, 9 (2004), 2583–2590. 

- [6] Alexei Baevski, Yuhao Zhou, Abdelrahman Mohamed, and Michael Auli. 2020. wav2vec 2.0: A framework for self-supervised learning of speech representations. _Advances in neural information processing systems_ 33 (2020), 12449–12460. 

- [7] Ghasem Sadeghi Bajestani, Shima Abedian, Fatemeh Makhloughi, Motahhareh Raoufitabar, and Hamid Saeedi. 2023. A dataset of eeg signals from adults with adhd and healthy controls: Resting state, cognitive function, and sound listening paradigm. _Mendeley Data_ (2023). 

- [8] Jacopo Barone and Holly E Rossiter. 2021. Understanding the role of sensorimotor beta oscillations. _Frontiers in systems neuroscience_ 15 (2021), 655886. 

- [9] Mohammad Javad Darvishi Bayazi, Hena Ghonia, Roland Riachi, Bruno Aristimunha, Arian Khorasani, Md Rifat Arefin, Amin Darabi, Guillaume Dumas, and Irina Rish. [n. d.]. General-Purpose Brain Foundation Models for TimeSeries Neuroimaging Data. In _NeurIPS Workshop on Time Series in the Age of Large Models_ . 

- [10] Ruggero G Bettinardi, Mohamed Rahmouni, and Ulysse Gimenez. 2025. BioSerenity-E1: a self-supervised EEG model for medical applications. _arXiv preprint arXiv:2503.10362_ (2025). 

- [11] Clemens Brunner, Robert Leeb, Gernot Müller-Putz, Alois Schlögl, and Gert Pfurtscheller. 2008. BCI Competition 2008–Graz data set A. _Institute for knowledge discovery (laboratory of brain-computer interfaces), Graz University of Technology_ 16, 1-6 (2008), 34. 

- [12] Gyorgy Buzsaki and Andreas Draguhn. 2004. Neuronal oscillations in cortical networks. _science_ 304, 5679 (2004), 1926–1929. 

- [13] Donghong Cai, Junru Chen, Yang Yang, Teng Liu, and Yafeng Li. 2023. Mbrain: A multi-channel self-supervised learning framework for brain signals. In _Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining_ . 130–141. 

- [14] Chi-Sheng Chen, Ying-Jung Chen, and Aidan Hung-Wen Tsai. 2025. Large Cognition Model: Towards Pretrained EEG Foundation Model. _arXiv preprint arXiv:2502.17464_ (2025). 

- [15] Ting Chen, Simon Kornblith, Mohammad Norouzi, and Geoffrey Hinton. 2020. A simple framework for contrastive learning of visual representations. In _International conference on machine learning_ . PmLR, 1597–1607. 

- [16] Yuqi Chen, Kan Ren, Kaitao Song, Yansen Wang, Yifan Wang, Dongsheng Li, and Lili Qiu. 2024. EEGFormer: Towards transferable and interpretable large-scale EEG foundation model. _arXiv preprint arXiv:2401.10278_ (2024). 

- [17] Zhige Chen, Chengxuan Qin, Wenlong You, Rui Liu, Congying Chu, Rui Yang, Kay Chen Tan, and Jibin Wu. 2025. HEAR: An EEG Foundation Model with Heterogeneous Electrode Adaptive Representation. _arXiv preprint arXiv:2510.12515_ (2025). 

- [18] Hsiang-Yun Sherry Chien, Hanlin Goh, Christopher M Sandino, and Joseph Y Cheng. 2022. Maeeg: Masked auto-encoder for eeg representation learning. _arXiv preprint arXiv:2211.02625_ (2022). 

- [19] Wenhui Cui, Woojae Jeong, Philipp Thölke, Takfarinas Medani, Karim Jerbi, Anand A Joshi, and Richard M Leahy. 2023. Neuro-gpt: Developing a foundation model for eeg. _arXiv preprint arXiv:2311.03764_ 107 (2023). 

- [20] Jonathan Dan, Amirhossein Shahbazinia, Christodoulos Kechris, and David Atienza. 2025. SzCORE as a benchmark: report from the seizure detection challenge at the 2025 AI in Epilepsy and Neurological Disorders Conference. _arXiv preprint arXiv:2505.18191_ (2025). 

- [21] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. Bert: Pre-training of deep bidirectional transformers for language understanding. In _Proceedings of the 2019 conference of the North American chapter of the association for computational linguistics: human language technologies, volume 1 (long and short papers)_ . 4171–4186. 

- [22] Alexandru Dimofte, Glenn Anta Bucagu, Thorir Mar Ingolfsson, Xiaying Wang, Andrea Cossettini, Luca Benini, and Yawei Li. 2025. CEReBrO: Compact Encoder for Representations of Brain Oscillations Using Efficient Alternating Attention. _arXiv preprint arXiv:2501.10885_ (2025). 

- [23] Berkay Döner, Thorir Mar Ingolfsson, Luca Benini, and Yawei Li. 2025. Luna: Efficient and topology-agnostic foundation model for eeg signal analysis. _arXiv preprint arXiv:2510.22257_ (2025). 

- [24] Alexey Dosovitskiy. 2020. An image is worth 16x16 words: Transformers for image recognition at scale. _arXiv preprint arXiv:2010.11929_ (2020). 

- [25] Zitao Fang, Chenxuan Li, Hongting Zhou, Shuyang Yu, Guodong Du, Ashwaq Qasem, Yang Lu, Jing Li, Junsong Zhang, and Sim Kuan Goh. 2025. Neuript: Foundation model for neural interfaces. _arXiv preprint arXiv:2510.16548_ (2025). 

- [26] Matteo Ferrante, Tommaso Boccato, Grigorii Rashkov, and Nicola Toschi. 2024. Towards Neural Foundation Models for Vision: Aligning EEG, MEG, and fMRI Representations for Decoding, Encoding, and Modality Conversion. _arXiv preprint arXiv:2411.09723_ (2024). 

- [27] Luay Fraiwan and Mohanad Alkhodari. 2020. Classification of focal and nonfocal epileptic patients using single channel EEG and long short-term memory learning system. _IEEE Access_ 8 (2020), 77255–77262. 

- [28] Sam Gijsen and Kerstin Ritter. [n. d.]. EEG-Language Pretraining for Highly Label-Efficient Clinical Phenotyping. In _Forty-second International Conference on Machine Learning_ . 

- [29] Ary L Goldberger, Luis AN Amaral, Leon Glass, Jeffrey M Hausdorff, Plamen Ch Ivanov, Roger G Mark, Joseph E Mietus, George B Moody, Chung-Kang Peng, and H Eugene Stanley. 2000. PhysioBank, PhysioToolkit, and PhysioNet: components of a new research resource for complex physiologic signals. _circulation_ 101, 23 (2000), e215–e220. 

- [30] J. Guttag. 2010. CHB-MIT Scalp EEG Database (version 1.0.0). 

- [31] Danny Dongyeop Han, Yonghyeon Gwon, Ahhyun Lucy Lee, Taeyang Lee, Seong Jin Lee, Jubin Choi, Sebin Lee, Jihyun Bang, Seungju Lee, David Keetae Park, et al. 2025. DIVER-1: Deep Integration of Vast Electrophysiological Recordings at Scale. _arXiv preprint arXiv:2512.19097_ (2025). 

- [32] Amir Harati, Silvia Lopez, I Obeid, J Picone, MP Jacobson, and S Tobochnik. 2014. The TUH EEG CORPUS: A big data resource for automated EEG interpretation. In _2014 IEEE signal processing in medicine and biology symposium (SPMB)_ . IEEE, 1–5. 

- [33] Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr Dollár, and Ross Girshick. 2022. Masked autoencoders are scalable vision learners. In _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ . 16000– 16009. 

- [34] Olivier Henaff. 2020. Data-efficient image recognition with contrastive predictive coding. In _International conference on machine learning_ . PMLR, 4182–4192. 

- [35] Jiazhen Hong, Geoffrey Mackellar, and Soheila Ghane. 2025. SAMBA: Toward a Long-Context EEG Foundation Model via Spatial Embedding and Differential Mamba. _arXiv preprint arXiv:2511.18571_ (2025). 

- [36] James F Cavanagh jcavanagh@unm.edu. 2021. _"EEG: Depression rest"_ . doi:10. 18112/openneuro.ds003478.v1.1.0 

- [37] Jaehyun Jeon, Seungwoo Jeong, Yeajin Shon, and Heung-Il Suk. [n. d.]. TaKF+: A versatile and parameter-efficient tuning for EEG foundation model. ([n. d.]). 

- [38] Muyun Jiang, Shuailei Zhang, Zhenjie Yang, Mengjun Wu, Weibang Jiang, Zhiwei Guo, Wei Zhang, Rui Liu, Shangen Zhang, Yong Li, et al. 2025. ELASTIQ: EEG-Language Alignment with Semantic Task Instruction and Querying. _arXiv preprint arXiv:2509.24302_ (2025). 

- [39] Wei-Bang Jiang, Yansen Wang, Bao-Liang Lu, and Dongsheng Li. 2024. NeuroLM: A Universal Multi-task Foundation Model for Bridging the Gap between Language and EEG Signals. _arXiv preprint arXiv:2409.00101_ (2024). 

- [40] Wei-Bang Jiang, Li-Ming Zhao, and Bao-Liang Lu. 2024. Large brain model for learning generic representations with tremendous EEG data in BCI. _arXiv preprint arXiv:2405.18765_ (2024). 

- [41] Bu Jin, Shuning Xue, Jie Jiang, Longteng Guo, Xinxin Zhu, Jin Zhou, Jing Liu, et al. [n. d.]. UniEEG: Advancing Universal EEG Representation with ElectrodeWise Time-Frequency Pretraining. ([n. d.]). 

- [42] Jin Jing, Wendong Ge, Shenda Hong, Marta Bento Fernandes, Zhen Lin, Chaoqi Yang, Sungtae An, Aaron F Struck, Aline Herlopian, Ioannis Karakis, et al. 2023. Development of expert-level classification of seizures and rhythmic and periodic patterns during EEG interpretation. _Neurology_ 100, 17 (2023), e1750–e1762. 

- [43] Sangmin Jo, Jaehyun Jeon, Seungwoo Jeong, and Heung-Il Suk. 2023. Channelaware self-supervised learning for eeg-based bci. In _2023 11th International Winter Conference on Brain-Computer Interface (BCI)_ . IEEE, 1–4. 

- [44] Jatinder Kaur, Kulwinder Singh Parmar, and Sarbjit Singh. 2023. Autoregressive models in environmental forecasting time series: a theoretical and application review. _Environmental Science and Pollution Research_ 30, 8 (2023), 19617–19641. 

- [45] Bob Kemp, Aeilko H Zwinderman, Bert Tuk, Hilbert AC Kamphuisen, and Josefien JL Oberye. 2000. Analysis of a sleep-dependent neuronal feedback loop: the slow-wave microcontinuity of the EEG. _IEEE Transactions on Biomedical Engineering_ 47, 9 (2000), 1185–1194. 

- [46] Sirvan Khalighi, Teresa Sousa, José Moutinho Santos, and Urbano Nunes. 2016. ISRUC-Sleep: A comprehensive public dataset for sleep researchers. _Computer methods and programs in biomedicine_ 124 (2016), 180–192. 

- [47] Diederik P Kingma and Max Welling. 2013. Auto-encoding variational bayes. _arXiv preprint arXiv:1312.6114_ (2013). 

- [48] Sander Koelstra, Christian Muhl, Mohammad Soleymani, Jong-Seok Lee, Ashkan Yazdani, Touradj Ebrahimi, Thierry Pun, Anton Nijholt, and Ioannis Patras. 2011. Deap: A database for emotion analysis; using physiological signals. _IEEE transactions on affective computing_ 3, 1 (2011), 18–31. 

- [49] Demetres Kostas, Stephane Aroca-Ouellette, and Frank Rudzicz. 2021. BENDR: Using transformers and a contrastive self-supervised learning task to learn from massive amounts of EEG data. _Frontiers in Human Neuroscience_ 15 (2021), 653659. 

- [50] Vamsi Kumar, Likith Reddy, Shivam Kumar Sharma, Kamalaker Dadi, Chiranjeevi Yarra, Raju S Bapi, and Srijithesh Rajendran. 2022. mulEEG: a multi-view representation learning on EEG signals. In _International Conference on Medical Image Computing and Computer-Assisted Intervention_ . Springer, 398–407. 

- [51] Jii Kwon and Youmin Shin. 2026. Foundation Models for Neural Signal Decoding: EEG-Centered Perspectives Toward Unified Representations. _European Journal of Neuroscience_ 63, 1 (2026), e70376. 

Shen et al. 

- [52] Cheol-Hui Lee, Hakseung Kim, Byung C Yoon, and Dong-Joo Kim. 2025. Toward Foundational Model for Sleep Analysis Using a Multimodal Hybrid SelfSupervised Learning Framework. _arXiv preprint arXiv:2502.17481_ (2025). 

- [53] Harim Lee, Eunseon Seong, and Dong-Kyu Chae. 2022. Self-Supervised Learning with Attention-based Latent Signal Augmentation for Sleep Staging with Limited Labeled Data.. In _IJCAI_ . 3868–3876. 

- [54] Ang Li, Zikai Wang, Liuyin Yang, Zhenyu Wang, Tianheng Xu, Honglin Hu, and Marc M Van Hulle. 2025. CoMET: A Contrastive-Masked Brain Foundation Model for Universal EEG Representation. _arXiv preprint arXiv:2509.00314_ (2025). 

- [55] Fan Li, Rui Yan, Reza Mahini, Lai Wei, Zhiqiang Wang, Klaus Mathiak, Rong Liu, and Fengyu Cong. 2021. End-to-end sleep staging using convolutional neural network in raw single-channel EEG. _Biomedical Signal Processing and Control_ 63 (2021), 102203. 

- [56] Hongqi Li, Yitong Chen, Yujuan Wang, Weihang Ni, and Haodong Zhang. 2025. Foundation models for cross-domain eeg analysis application: A survey. _arXiv preprint arXiv:2508.15716_ (2025). 

- [57] Jiahe Li, Xin Chen, Fanqi Shen, Junru Chen, Yuxin Liu, Daoze Zhang, Zhizhang Yuan, Fang Zhao, Meng Li, and Yang Yang. 2025. Deep learning-powered electrical brain signals analysis: Advancing neurological diagnostics. _IEEE Reviews in Biomedical Engineering_ (2025). 

- [58] Xiaomin Li and Vangelis Metsis. 2022. Spp-eegnet: An input-agnostic selfsupervised eeg representation model for inter-dataset transfer learning. In _International Conference on Computing and Information Technology_ . Springer, 173–182. 

- [59] Chenyu Liu, Yuqiu Deng, Tianyu Liu, Jinan Zhou, Xinliang Zhou, Ziyu Jia, and Yi Ding. 2025. ECHO: Toward Contextual Seq2Seq Paradigms in Large EEG Models. _arXiv preprint arXiv:2509.22556_ (2025). 

- [60] Hanwen Liu, Daniel Hajialigol, Benny Antony, Aiguo Han, and Xuan Wang. 2024. Eeg2text: Open vocabulary eeg-to-text decoding with eeg pre-training and multi-view transformer. _arXiv preprint arXiv:2405.02165_ (2024). 

- [61] Huan Liu, Shusen Yang, Yuzhe Zhang, Mengze Wang, Fanyu Gong, Chengxi Xie, Guanjian Liu, Zejun Liu, Yong-Jin Liu, Bao-Liang Lu, et al. 2025. Libeer: A comprehensive benchmark and algorithm library for eeg-based emotion recognition. _IEEE Transactions on Affective Computing_ (2025). 

- [62] Xiao Liu, Fanjin Zhang, Zhenyu Hou, Li Mian, Zhaoyu Wang, Jing Zhang, and Jie Tang. 2021. Self-supervised learning: Generative or contrastive. _IEEE transactions on knowledge and data engineering_ 35, 1 (2021), 857–876. 

- [63] Catherine Lloyd, Loic Lorente Lemoine, Reiyan Al-Shaikh, Kim Tien Ly, Hakan Kayan, Charith Perera, and Nhat Pham. 2024. Stress-GPT: Stress detection with an EEG-based foundation model. In _Proceedings of the 30th Annual International Conference on Mobile Computing and Networking_ . 2341–2346. 

- [64] Sandra K Loo, Alexander Cho, T Sigi Hale, James McGough, James McCracken, and Susan L Smalley. 2013. Characterization of the theta to beta ratio in ADHD: identifying potential sources of heterogeneity. _Journal of attention disorders_ 17, 5 (2013), 384–392. 

- [65] Fabien Lotte, Laurent Bougrain, Andrzej Cichocki, Maureen Clerc, Marco Congedo, Alain Rakotomamonjy, and Florian Yger. 2018. A review of classification algorithms for EEG-based brain–computer interfaces: a 10 year update. _Journal of neural engineering_ 15, 3 (2018), 031005. 

- [66] Weiheng Lu, Chunfeng Song, Jiamin Wu, Pengyu Zhu, Yuchen Zhou, Weijian Mai, Qihao Zheng, and Wanli Ouyang. 2025. UniMind: Unleashing the Power of LLMs for Unified Multi-Task Brain Decoding. _arXiv preprint arXiv:2506.18962_ (2025). 

- [67] Jingying Ma, Feng Wu, Qika Lin, Yucheng Xing, Chenyu Liu, Ziyu Jia, and Mengling Feng. 2025. CodeBrain: Bridging Decoupled Tokenizer and MultiScale Architecture for EEG Foundation Model. _arXiv preprint arXiv:2506.09110_ (2025). 

- [68] Umberto Michelucci. 2022. An introduction to autoencoders. _arXiv preprint arXiv:2201.03898_ (2022). 

- [69] Andreas Miltiadous, Katerina D. Tzimourta, Theodora Afrantou, Panagiotis Ioannidis, Nikolaos Grigoriadis, Dimitrios G. Tsalikakis, Pantelis Angelidis, Markos G. Tsipouras, Evripidis Glavas, Nikolaos Giannakeas, and Alexandros T. Tzallas. 2023. _"A dataset of 88 EEG recordings from: Alzheimer’s disease, Frontotemporal dementia and Healthy subjects"_ . doi:doi:10.18112/openneuro.ds004504.v1. 0.2 

- [70] Navid Mohammadi Foumani, Geoffrey Mackellar, Soheila Ghane, Saad Irtza, Nam Nguyen, and Mahsa Salehi. 2024. Eeg2rep: enhancing self-supervised EEG representation through informative masked inputs. In _Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining_ . 5544–5555. 

- [71] Mostafa Neo Mohsenvand, Mohammad Rasool Izadi, and Pattie Maes. 2020. Contrastive representation learning for electroencephalogram classification. In _Machine Learning for Health_ . PMLR, 238–253. 

- [72] Ali Motie Nasrabadi, Armin Allahverdy, Mehdi Samavati, and Mohammad Reza Mohammadi. 2020. EEG data for ADHD / Control children. doi:10.21227/rzfhzn36 

- [73] Wajid Mumtaz. 2016. MDD Patients and Healthy Controls EEG Data (New). (11 2016). doi:10.6084/m9.figshare.4244171.v2 

- [74] Michael Murias, James M Swanson, and Ramesh Srinivasan. 2007. Functional connectivity of frontal cortex in healthy and ADHD children reflected in EEG coherence. _Cerebral Cortex_ 17, 8 (2007), 1788–1799. 

- [75] Petr Nejedly, Vaclav Kremen, Vladimir Sladky, Jan Cimbalnik, Petr Klimes, Filip Plesinger, Filip Mivalt, Vojtech Travnicek, Ivo Viscor, Martin Pail, et al. 2020. Multicenter intracranial EEG dataset for classification of graphoelements and artifactual signals. _Scientific data_ 7, 1 (2020), 179. 

- [76] Jennifer J Newson and Tara C Thiagarajan. 2019. EEG frequency bands in psychiatric disorders: a review of resting state studies. _Frontiers in human neuroscience_ 12 (2019), 521. 

- [77] Iyad Obeid and Joseph Picone. 2016. The temple university hospital EEG data corpus. _Frontiers in neuroscience_ 10 (2016), 196. 

- [78] Mattson Ogg and William G Coon. 2024. Self-supervised transformer model training for a sleep-eeg foundation model. In _2024 46th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)_ . IEEE, 1–6. 

- [79] B Orkan Olcay and Bilge Karaçalı. 2023. Time-resolved EEG signal analysis for motor imagery activity recognition. _Biomedical Signal Processing and Control_ 86 (2023), 105179. 

- [80] Aaron van den Oord, Yazhe Li, and Oriol Vinyals. 2018. Representation learning with contrastive predictive coding. _arXiv preprint arXiv:1807.03748_ (2018). 

- [81] Yassine El Ouahidi, Jonathan Lys, Philipp Thölke, Nicolas Farrugia, Bastien Pasdeloup, Vincent Gripon, Karim Jerbi, and Giulia Lioi. 2025. REVE: A Foundation Model for EEG–Adapting to Any Setup with Large-Scale Pretraining on 25,000 Subjects. _arXiv preprint arXiv:2510.21585_ (2025). 

- [82] Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever, et al. 2019. Language models are unsupervised multitask learners. _OpenAI blog_ 1, 8 (2019), 9. 

- [83] Abdellah Rahmani, Arun Venkitaraman, and Pascal Frossard. 2023. A Meta-GNN approach to personalized seizure detection and classification. In _ICASSP 20232023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ . IEEE, 1–5. 

- [84] Alexander P. Rockhill, Nicko Jackson, Jobi George, Adam Aron, and Nicole C. Swann. 2021. _"UC San Diego Resting State EEG Data from Patients with Parkinson’s Disease"_ . doi:doi:10.18112/openneuro.ds002778.v1.0.5 

- [85] Ayan Seal, Rishabh Bajpai, Jagriti Agnihotri, Anis Yazidi, Enrique HerreraViedma, and Ondrej Krejcar. 2021. DeprNet: A deep convolution neural network framework for detecting depression using EEG. _IEEE Transactions on Instrumentation and Measurement_ 70 (2021), 1–13. 

- [86] Ali Shoeb. 2009. _Application of Machine Learning to Epileptic Seizure Onset Detection and Treatment_ . Ph. D. Dissertation. Massachusetts Institute of Technology. 

- [87] Rahul Thapa, Bryan He, Magnus Ruud Kjaer, H Moore IV, Gauri Ganjoo, Emmanuel Mignot, and James Zou. 2024. Sleepfm: foundation model for sleep analysis. In _ICLR Workshop on Learning from Time Series For Health_ . 

- [88] Aaron Van Den Oord, Oriol Vinyals, et al. 2017. Neural discrete representation learning. _Advances in neural information processing systems_ 30 (2017). 

- [89] Neeraj Wagh, Jionghao Wei, Samarth Rawal, Brent Berry, Leland Barnard, Benjamin Brinkmann, Gregory Worrell, David Jones, and Yogatheesan Varatharajah. 2021. Domain-guided self-supervision of EEG data improves downstream classification performance and generalizability. In _Machine Learning for Health_ . PMLR, 130–142. 

- [90] Christopher Wang, Vighnesh Subramaniam, Adam Uri Yaari, Gabriel Kreiman, Boris Katz, Ignacio Cases, and Andrei Barbu. 2023. BrainBERT: Selfsupervised representation learning for intracranial recordings. _arXiv preprint arXiv:2302.14367_ (2023). 

- [91] Guangyu Wang, Wenchao Liu, Yuhong He, Cong Xu, Lin Ma, and Haifeng Li. 2024. Eegpt: Pretrained transformer for universal and reliable representation of eeg signals. _Advances in Neural Information Processing Systems_ 37 (2024), 39249–39280. 

- [92] Jiquan Wang, Sha Zhao, Zhiling Luo, Yangxuan Zhou, Haiteng Jiang, Shijian Li, Tao Li, and Gang Pan. 2024. CBraMod: A Criss-Cross Brain Foundation Model for EEG Decoding. _arXiv preprint arXiv:2412.07236_ (2024). 

- [93] Limin Wang, Toyotaro Suzumura, and Hiroki Kanezashi. 2024. Graph-Enhanced EEG Foundation Model. _arXiv preprint arXiv:2411.19507_ (2024). 

- [94] Yihe Wang, Nan Huang, Nadia Mammone, Marco Cecchi, and Xiang Zhang. 2025. LEAD: Large Foundation Model for EEG-Based Alzheimer’s Disease Detection. _arXiv preprint arXiv:2502.01678_ (2025). 

- [95] Xinxu Wei, Kanhao Zhao, Yong Jiao, Nancy B Carlisle, Hua Xie, Gregory A Fonzo, and Yu Zhang. 2025. Multi-modal cross-domain self-supervised pretraining for fMRI and EEG fusion. _Neural Networks_ 184 (2025), 107066. 

- [96] Xinxu Wei, Kanhao Zhao, Yong Jiao, Nancy B Carlisle, Hua Xie, and Yu Zhang. 2024. Pre-Training Graph Contrastive Masked Autoencoders are Strong Distillers for EEG. _arXiv preprint arXiv:2411.19230_ (2024). 

- [97] Weining Weng, Yang Gu, Shuai Guo, Yuan Ma, Zhaohua Yang, Yuchen Liu, and Yiqiang Chen. 2025. Self-supervised learning for electroencephalogram: A systematic survey. _Comput. Surveys_ 57, 12 (2025), 1–38. 

- [98] Anqi Wu, Yifan Zhang, Yang Yu, and Ling-Li Zeng. 2024. EEG-ARNet: An Autoregressive Pre-training Model for Extracting EEG Features. In _2024 5th_ 

Brain4FMs: A Benchmark of Foundation Models for Electrical Brain Signals 

_International Conference on Computers and Artificial Intelligence Technology (CAIT)_ . IEEE, 255–259. 

- [99] Di Wu, Siyuan Li, Jie Yang, and Mohamad Sawan. 2022. neuro2vec: Masked fourier spectrum prediction for neurophysiological representation learning. _arXiv preprint arXiv:2204.12440_ (2022). 

- [100] Di Wu, Siyuan Li, Jie Yang, and Mohamad Sawan. 2024. Neuro-BERT: Rethinking Masked Autoencoding for Self-Supervised Neurological Pretraining. _IEEE Journal of Biomedical and Health Informatics_ (2024). 

- [101] Jiamin Wu, Zichen Ren, Junyu Wang, Pengyu Zhu, Yonghao Song, Mianxin Liu, Qihao Zheng, Lei Bai, Wanli Ouyang, and Chunfeng Song. 2025. AdaBrainbench: Benchmarking brain foundation models for brain-computer interface applications. _arXiv preprint arXiv:2507.09882_ (2025). 

- [102] Chuqin Xiang, Xinrui Fan, Duo Bai, Ke Lv, and Xu Lei. 2024. _"A Resting-state EEG Dataset for Sleep Deprivation"_ . doi:doi:10.18112/openneuro.ds004902.v1.0.5 

- [103] Qinfan Xiao, Ziyun Cui, Chi Zhang, Siqi Chen, Wen Wu, Andrew Thwaites, Alexandra Woolgar, Bowen Zhou, and Chao Zhang. 2025. BrainOmni: A Brain Foundation Model for Unified EEG and MEG Signals. _arXiv preprint arXiv:2505.18185_ (2025). 

- [104] Wei Xiong, Jiangtong Li, Jie Li, and Kun Zhu. 2025. Eeg-fm-bench: A comprehensive benchmark for the systematic evaluation of eeg foundation models. _arXiv preprint arXiv:2508.17742_ (2025). 

- [105] Chaoqi Yang, M Westover, and Jimeng Sun. 2023. Biot: Biosignal transformer for cross-data learning in the wild. _Advances in Neural Information Processing Systems_ 36 (2023), 78240–78260. 

- [106] Wenchao Yang, Weidong Yan, Wenkang Liu, Yulan Ma, and Yang Li. 2025. THDBAR: Topology Hierarchical Derived Brain Autoregressive Modeling for EEG Generic Representations. _arXiv preprint arXiv:2511.13733_ (2025). 

- [107] Zhizhang Yuan, Fanqi Shen, Meng Li, Yuguo Yu, Chenhao Tan, and Yang Yang. 2024. BrainWave: A Brain Signal Foundation Model for Clinical Applications. _arXiv preprint arXiv:2402.10251_ (2024). 

- [108] Tongtian Yue, Shuning Xue, Xuange Gao, Yepeng Tang, Longteng Guo, Jie Jiang, and Jing Liu. 2024. EEGPT: Unleashing the Potential of EEG Generalist Foundation Model by Autoregressive Pre-training. _arXiv preprint arXiv:2410.19779_ (2024). 

- [109] Ziyi Zeng, Zhenyang Cai, Yixi Cai, Xidong Wang, Junying Chen, Rongsheng Wang, Yipeng Liu, Siqi Cai, Benyou Wang, Zhiguo Zhang, et al. 2025. Wavemind: Towards a conversational eeg foundation model aligned to textual and visual modalities. _arXiv preprint arXiv:2510.00032_ (2025). 

- [110] George Zerveas, Srideepika Jayaraman, Dhaval Patel, Anuradha Bhamidipaty, and Carsten Eickhoff. 2021. A transformer-based framework for multivariate time series representation learning. In _Proceedings of the 27th ACM SIGKDD conference on knowledge discovery & data mining_ . 2114–2124. 

- [111] Daoze Zhang, Zhizhang Yuan, Junru Chen, Kerui Chen, and Yang Yang. 2024. Brant-X: A Unified Physiological Signal Alignment Framework. In _Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining_ . 4155–4166. 

- [112] Daoze Zhang, Zhizhang Yuan, Yang Yang, Junru Chen, Jingjing Wang, and Yafeng Li. 2023. Brant: Foundation model for intracranial neural signal. _Advances in Neural Information Processing Systems_ 36 (2023), 26304–26321. 

- [113] Wenrui Zhang, Ling Yang, Shijia Geng, and Shenda Hong. 2023. Self-supervised time series representation learning via cross reconstruction transformer. _IEEE Transactions on Neural Networks and Learning Systems_ (2023). 

- [114] Xiang Zhang, Lina Yao, Xianzhi Wang, Jessica Monaghan, David Mcalpine, and Yu Zhang. 2021. A survey on deep learning-based non-invasive brain signals: recent advances and new frontiers. _Journal of neural engineering_ 18, 3 (2021), 031002. 

- [115] Xiang Zhang, Ziyuan Zhao, Theodoros Tsiligkaridis, and Marinka Zitnik. 2022. Self-supervised contrastive pre-training for time series via time-frequency consistency. _Advances in neural information processing systems_ 35 (2022), 3988– 4003. 

- [116] Zihan Zhang, Xiao Ding, Yu Bao, Yi Zhao, Xia Liang, Bing Qin, and Ting Liu. 2024. Chisco: An EEG-based BCI dataset for decoding of imagined speech. _Scientific Data_ 11, 1 (2024), 1265. 

- [117] Wei-Long Zheng, Wei Liu, Yifei Lu, Bao-Liang Lu, and Andrzej Cichocki. 2018. Emotionmeter: A multimodal framework for recognizing human emotions. _IEEE transactions on cybernetics_ 49, 3 (2018), 1110–1122. 

- [118] Wei-Long Zheng and Bao-Liang Lu. 2015. Investigating critical frequency bands and channels for EEG-based emotion recognition with deep neural networks. _IEEE Transactions on autonomous mental development_ 7, 3 (2015), 162–175. 

- [119] Jinzhao Zhou, Zehong Cao, Yiqun Duan, Connor Barkley, Daniel Leong, Xiaowei Jiang, Quoc-Toan Nguyen, Ziyi Zhao, Thomas Do, Yu-Cheng Chang, et al. 2025. Pretraining Large Brain Language Model for Active BCI: Silent Speech. _arXiv preprint arXiv:2504.21214_ (2025). 

- [120] Xinliang Zhou, Chenyu Liu, Zhisheng Chen, Kun Wang, Yi Ding, Ziyu Jia, and Qingsong Wen. 2025. Brain foundation models: A survey on advancements in neural signal processing and brain discovery. _arXiv preprint arXiv:2503.00580_ (2025). 

- [121] Yangxuan Zhou, Sha Zhao, Jiquan Wang, Haiteng Jiang, Shijian Li, Tao Li, and Gang Pan. [n. d.]. BrainUICL: An unsupervised individual continual learning framework for EEG applications. In _The Thirteenth International Conference on Learning Representations_ . 

- [122] Qiushi Zhu, Xiaoying Zhao, Jie Zhang, Yu Gu, Chao Weng, and Yuchen Hu. 2023. EEG2VEC: Self-supervised electroencephalographic representation learning. _arXiv preprint arXiv:2305.13957_ (2023). 

- [123] Igor Zyma, Sergii Tukaev, Ivan Seleznov, Ken Kiyono, Anton Popov, Mariia Chernykh, and Oleksii Shpenkov. 2019. Electroencephalograms during mental arithmetic task performance. _Data_ 4, 1 (2019), 14. 

### **A SSL Paradigm** 

### **A.1 Contrastive-based Method** 

_A.1.1 Augmentation contrast._ Augmentation-based contrastive learning constructs positive pairs by applying transformation operators _𝑎𝑠_ to the same input signal, with representation learning driven by enforcing invariance across augmented views. Early BFMs works primarily focused on expanding the effective view space induced by _𝑎𝑠_ . SeqCLR [71] adapts SimCLR [15] to multichannel EEG by recombining channels to expand the augmentation-induced view space and enforce consistency across views. SppEEGNet [58] further applies a suite of EEG-specific augmentations and forms positive pairs within sliding windows on a 2D signal representation, which helps reduce cross-dataset sampling-rate mismatch. BIOT [105] introduces channel-level augmentations tailored to biosignals. Nevertheless, contrastive objectives can suffer from false negatives, especially in sleep staging, where adjacent segments may share labels. SSLAPP [53] addresses this by adversarially generating highquality positives and performing attention-guided augmentation in latent space, mitigating semantic collisions in pair construction. 

As view construction strategies matured, research attention gradually shifted toward the design of the encoder F (·) to better capture EEG dynamics. Early approaches predominantly relied on CNN-based architectures [50, 58, 71], which primarily model local temporal patterns. Recognizing the intrinsically non-stationary and multi-scale nature of neural signals, later works incorporate temporal–spectral duality into representation learning. TF-C [115] enforces consistency between time-domain and frequency-domain embeddings of the same signal, explicitly coupling complementary signal views. More recently, transformer-based encoders have been introduced to support cross-dataset and cross-subject learning at scale. BIOT [105] employs a biosignal transformer to unify heterogeneous modalities, while LEAD [95] further regularizes representations through subject-level consistency, encouraging invariant embeddings across samples from the same individual. 

_A.1.2 Contrastive Predictive Coding._ Inspired by BERT and wav2vec 2.0[6], Bendr[49] encodes EEG segments into a unified sequence of learned vector representations. Maeeg[18] and GEFM[93] have similar architecture to Bendr with different PT mindset. Although Bendr can extract features well, it ignores spatial information. To address this issue, several models have been proposed. GEFM adds a graph structure to Bendr and proposes a sequence length adjustment mechanism before GNN to make EEG signal lengths consistent for fixed-length node features in GNN. Zhu et al. [122] incorporated spatial information through channel-mixing augmentation, effectively enhancing dataset diversity and improving the performance of the contrastive EEG2Vec framework. Another line of work extends CPC to better exploit multichannel structure and continual 

Shen et al. 

data streams. MBrain [13] augments CPC with spatial awareness by aggregating multichannel semantics to predict single-channel local representations, encouraging implicit spatio-temporal dependencies across channels. BrainUICL [121] further combines CPC with replay-based continual learning, and the contrastive model is incrementally updated via joint training with replayed samples. 

_A.1.3 Cross-modal Contrast._ Inspired by multimodal contrastive learning, BFMs extend cross-modal alignment to EEG, where “modality” arises from the inherent heterogeneity of brain recordings. At the intra-signal level, different views of the same EEG (e.g., raw waveforms vs. time–frequency representations) can serve as distinct modalities. MuLEEG [50] follows this paradigm by contrasting multi-view raw signals with spectrograms. Beyond view-level heterogeneity, MCSP [95] mines complementary information across modalities and models latent interactions within each domain, particularly spatial structure via graphs. For truly multi-sensor settings, SleepFM [87] jointly embeds three biosignal modalities using both pairwise contrast and a leave-one-out objective, aligning each modality to the average of the others. Brant-X [111] further targets EEG–EXG coupling by aligning representations at both patch and sequence levels, capturing correlations at fine- and coarse-grained semantic scales. Moving to heterogeneous cross-modal alignment beyond biosignals, Ferrante et al. [26] align neural recordings with visual stimuli, demonstrating that visual content can be decoded from neural data and that images can be mapped into neural representation spaces. 

### **A.2 Generative-based Methods** 

_A.2.1 Autoregressive._ The success of autoregressive (AR) language models in modeling long-range dependencies via next-token prediction has motivated the adoption in BFMs. Using a decoder-only transformer architecture, GPT-style models [82] have been adapted to EEG pretraining in several BFMs [19, 63, 91, 108]. Early efforts such as Neuro-GPT [19] segment continuous EEG into fixed-length chunks and treat each chunk as a token, enabling a GPT model G _𝜃_ 2 (·) to learn spatio-temporal structure by predicting masked segments. Building on this framework, Stress-GPT [63] fine-tunes the pretrained model for stress-related tasks, demonstrating the transferability of AR-pretrained representations. 

Subsequent works refine the tokenization and prediction strategy to better reflect EEG-specific structure. EEGPT-2 [108] adopts an electrode-wise autoregressive formulation, treating each electrode signal _𝑥𝑖_<sup>_𝑒_asabasictokenandmodelingtemporaldependencies</sup> through an Electrode Temporal Encoder. EEG2Rep [70] shifts target prediction into latent space via context-driven masking and introduces a semantic subsequence preserving mechanism to provide more informative masked inputs. Inspired by large language models, NeuroLM [39] generalizes autoregressive pretraining to multi-channel EEG, explicitly modeling inter-channel dependencies. More recently, LBLM [119] unifies temporal and spectral autoregression to capture spectro-temporal dynamics, while ECHO [59] constructs discrete, prompt-like context supports encoding hierarchical signal–task–label relations, improving in-context learning for downstream EEG tasks. 

_A.2.2 Autoencoder._ Autoencoder is the most common method in BFMs pretraining. To learn informative representations M( _𝑥_ ), AEbased BFMs rely on carefully designed disturbance mechanisms that force reconstruction from partial observations. Masked Autoencoders (MAE) [33] randomly mask input regions and reconstruct missing content from visible context, encouraging the model to capture global structure. Inspired by both BENDR [49] and MAE, MAEEG [18] and GEFM [93] adopt masked reconstruction for EEG pretraining. UniEEG [41] further introduces Masked Signal Modeling (MSM) with electrode-wise masking, while EEGPT-1 [91] embeds local spatio-temporal patches as tokens and proposes a dual SSL objective combining mask-based reconstruction with spatiotemporal alignment. 

Beyond masking strategies, modern AE-based BFMs primarily differ in the design of the encoder F _𝜃_ 1 (·), which must model long-range temporal dependencies while capturing cross-channel interactions. Early models such as BrainBERT [90] largely encode electrodes independently, limiting spatial coupling. Subsequent works introduce stronger spatial inductive biases: EEG2TEXT [60] employs multi-view attention to reflect region-wise processing, while CBraMod [92] adopts a criss-cross encoder that alternates spatial–temporal attention with asymmetric conditional positional encoding. To handle heterogeneous montages, LUNA [23] unifies variable electrode layouts into a fixed latent space via learned queries, and REVE [81] injects anatomical priors through 4D positional embeddings derived from electrode coordinates and time indices. Beyond attention-based designs, Mamba-style encoders enable linear-time sequence modeling for long recordings. SynthSleepNet [52] introduces a Mamba-based Temporal Context Module for inter-epoch dependencies, while SAMBA [35] proposes a Multi-head Differential Mamba to suppress background noise while aggregating contextual information. 

However, the inherent randomness, non-stationarity, and nonlinearity of neurophysiological signals make direct amplitude reconstruction in the spatiotemporal domain suboptimal [99]. As a result, recent BFMs increasingly perform masking and reconstruction in transformed spaces T _𝑑_ (·) or low-dimensional latent variables _𝑧𝑖_ . Neuro2vec [99] pioneers denoising in the Fourier domain, while CRT [113] performs cross-domain dropping–reconstruction to align time- and frequency-domain representations. Building on Fourier-domain MAE, Neuro-BERT [100] introduces Fourier Inversion Prediction (FIP) as a pretraining objective. In parallel, spectrogram-based reconstruction has gained traction due to its rich time–frequency semantics, supporting both signal understanding and downstream learning [78, 90, 107]. 

Most AE-based BFMs are developed for non-invasive EEG, while intracranial EEG (iEEG) remains comparatively underexplored. To bridge this gap, BrainBERT [90], Brant [112], and Brainwave [107] extend AE-based pretraining to SEEG recordings. BrainBERT leverages SEEG data from subjects watching videos, Brant adopts a dual-encoder MAE to jointly capture temporal dependencies and spatial correlations, and Brainwave scales pretraining to over 16,000 subjects, setting new benchmarks for diagnosis tasks. While these approaches substantially improve performance, they often increase model size. To address this, CEReBrO [22] proposes a compact 

Brain4FMs: A Benchmark of Foundation Models for Electrical Brain Signals 

encoder that represents brain oscillations through alternating attention, offering a parameter-efficient alternative for AE-based BFMs. 

_A.2.3 Codebook._ The codebook mechanism, originally introduced by Vector-Quantized Variational Autoencoders (VQ-VAE) [88], offers a key advantage over standard VAEs by discretizing continuous representations into a finite set of tokens. Recently, this paradigm has been adapted to EEG and iEEG modeling, where encoder outputs are quantized into discrete codebook entries via a quantization operator Q ∗ _𝜃_ 3 (·) prior to decoding. Such discretization enables token-based representations of neural signals, bridging continuous biosignals with sequence modeling frameworks. The codebook is optimized using the vector-quantization objective: L _𝑣𝑞_ = || _𝑠𝑔_ [Q _𝜃_ 3 ( _𝑧𝑖_ )] − _𝑧𝑖_ ||<sup>2</sup> 2<sup>+</sup><sup>_𝛽_||</sup><sup>_𝑠𝑔_[</sup><sup>_𝑧𝑖_] −Q</sup><sup>_𝜃_</sup> 3<sup>(</sup><sup>_𝑧𝑖_)||2</sup> 2<sup>where</sup><sup>_𝑠𝑔_[·]de-</sup> notes the stop-gradient operator. Compared to conventional masked reconstruction, vector-quantized transformers often learn more generalizable neural representations and exhibit strong adaptability across heterogeneous downstream tasks. 

A central challenge of this paradigm lies in learning an effective quantization operator Q _𝜃_ 3 (·). EEGFormer [16] first applies codebook-based discretization to EEG pretraining, generating discrete indices that yield transferable and interpretable representations. LaBraM [40] further introduces a neural codebook that quantizes patch-level embeddings, with the codebook optimized through reconstruction in the Fourier domain. BioSerenity-E1 [10] adopts a transformer-based VQ-VAE to tokenize EEG spectra and performs masked token prediction, forcing the model to capture complex spatiotemporal dependencies and achieving state-of-the-art diagnostic performance. Beyond reconstruction-based objectives, NeuroLM [39] extends this line of work by introducing vector-quantized time–frequency prediction and aligning EEG tokens with textual representations via adversarial training. After discretization, it employs multi-channel autoregressive modeling, enabling LLMs to predict EEG tokens in a manner analogous to language modeling. 

While codebook learning is often instantiated within autoencoderstyle frameworks, it should be viewed as a general representation mechanism rather than a method specific to AE-based BFMs. Discrete neural tokens can serve as a unifying interface across reconstruction, contrastive, and autoregressive paradigms, motivating their independent treatment in this appendix. 

### **A.3 Other Advanced Method** 

_A.3.1 explicit predictive._ In the context of EEG, several predictive tasks have been specifically proposed by updating the form of G _𝜃_ 2 (·) to better align with neurophysiological characteristics. Domain-guided CL [89] introduces Behavioral State Estimation, which predicts the delta-beta ratio to capture arousal-related spectral patterns. The Stopped Band Prediction pretext task[43] focuses on learning frequency-aware representations by asking the model to identify which frequency band has been suppressed in the input signal to capture frequency information. And the Temporal Trend Identification task[43] aims to extract temporal dynamics by classifying pre-defined trends. Although these tasks are neurophysiologically interpretable, their dependence on specific assumptions about signal behavior has still limited their adoption in BFMs. 

_A.3.2 Hybrid-based._ Hybrid SSL combines multiple self-supervised objectives within a unified framework to exploit complementary learning signals [97]. In EEG, Domain-guided contrastive learning [89] designs SSL pretext tasks grounded in neurophysiological priors, leveraging similarity of brain activity as well as behavioralstate and age-related differences. EEG-DisGCMAE [96] further introduces a graph-structured hybrid that couples Graph Contrastive pretraining with Graph MAE. LCM [14] follows a different route, using masked generative reconstruction as the primary objective and adding a momentum-updated target encoder with a contrastive term to stabilize representation learning. More broadly, BFMs increasingly pair contrastive objectives with generative modeling to jointly enforce cross-view consistency and preserve signal structure [14, 52, 54, 91]. Other hybrids integrate reconstruction with autoregressive prediction to capture both local structure and longrange temporal dynamics [38, 106], and may further incorporate adversarial objectives for domain-aware alignment [39, 53]. 

_A.3.3 Instruction-tuned._ Recent instruction-tuned BFMs bridge EEG representations with language semantics through lightweight alignment modules while keeping LLM backbones mostly frozen. NeuroLM[39] discretizes EEG into temporal–frequency tokens via VQ encoding and aligns EEG and text embeddings through domainadversarial learning, followed by multi-channel autoregressive pretraining and prompt-based multi-task instruction tuning. TaKF+[37] emphasizes parameter-efficient transfer by injecting task information through adapters and cross-attention blocks after masked patch pretraining. UniMind[66] proposes a Neuro-Language Connector that extracts task-relevant temporal–spatial semantics using learnable queries with task-aware routing, and aligns them to the LLM latent space for instruction-conditioned generation. WaveMind[109] combines contrastive multimodal alignment with CLIP and instruction tuning on a large EEG instruction dataset, enabling conversational EEG understanding across tasks. 

### **B Dataset** 

This section summarizes additional dataset characteristics omitted from the main text for brevity (Table 7). These attributes reflect dataset acquisition protocols and are provided to facilitate reproducibility and practical reuse of the benchmark. All datasets are processed under consistent cross-subject and cross-validation protocols. Dataset-specific preprocessing procedures are implemented in our open-source code. For transparency and reproducibility, the complete preprocessing pipelines for each dataset are documented in the data_preprocess directory. All datasets used Brain4FMs are publicly released; ethics and fairness considerations are therefore limited, as no new data collection is involved. 

To further support transparent benchmarking, pretraining data sources of the evaluated BFMs are documented whenever disclosed by the original papers or released checkpoints. In selecting downstream benchmarks, overlap with commonly used pretraining corpora was minimized a priori: most downstream datasets are disjoint from the dominant pretraining sources (e.g., TUH [77]/TUEG [32] or large private collections). Potential overlap is therefore limited to a small subset of models that incorporate BCI-oriented resources during pretraining (e.g., the SEED series and BCI Competition IV, overlapping with SEED-IV and BCI-2a). In addition, some 

Shen et al. 

models leverage task-related corpora for AD, SD, or sleep staging pretraining. The downstream datasets were curated to avoid direct dataset-level reuse in these categories whenever possible. Brain4FMs evaluates models as released under unified protocols rather than re-pretraining leave-dataset-out variants. Empirically, performance differences cannot be explained by partial overlap alone under the standardized cross-subject fine-tuning setting, suggesting that pretraining scale, data diversity, SSL objectives, and architectural choices also contribute. 

**Table 7:** Public EEG/iEEG datasets used in the benchmark, listing the number of channels (#Ch), sequence length (SeqLen), sampling frequency, total recording duration, and dataset category. 

|Name|#Ch|SeqLen|Frequency|Total Time|Category|
|---|---|---|---|---|---|
|CHBMIT [30]|23|10s|256|686 h|2|
|MAYO [75]|1|3s|5000→1000|94.38 h|2|
|FNUSA [75]|1|3s|5000→1000|149.69 h|2|
|Dep-BDI [36]|64|10s|500→250|31.5 h|2|
|Dep-STAI [36]|64|10s|500→250|31.5 h|3|
|MDD-64 [73]|19|10s|256|20.53 h|2|
|SD-28 [102]|19|5s|250|958 min|2|
|UCSD-ON [84]|32|10s|512→256|220 min|2|
|UCSD-OFF [84]|32|10s|512→256|220 min|2|
|ADFD [69]|19|10s|500→250|1164 min|2|
|ADHD_Adult [7]|2|5s|256|423 min|2|
|ADHD_Child [72]|19|5s|128|274.5 min|2|
|ISRUC-G1 [46]|6|30s|200|744.5 h|5|
|SleepEDF [45]|1|30s|100|378.7 h|5|
|DEAP [48]|32|10s|128|2133 min|4|
|SEED-IV [117]|62|4s|200|54 h|4|
|EEGMat [123]|32|10s|500→250|144 min|2|
|EEGMMIDB-R [29]|64|4s|160|2834 min|4|
|EEGMMIDB-I [29]|64|4s|160|2834 min|4|
|BCI-2a [11]|22|3s|250|130 min|4|
|Chisco-R [116]|125|3.3s|500|58.6 h|39|
|Chisco-I [116]|125|3.3s|500|58.6 h|39|



AUROC, Accuracy, F1, and F2 to capture threshold-free discrimination and positive-class detection under imbalance. For multi-class tasks, we report Accuracy, AUROC (one-vs-rest; OvR), macro-F1 (MF1), and Cohen’s _𝜅_ (Kappa) to measure overall discrimination, class-wise performance, and agreement beyond chance. We report results as mean ± standard deviation over n-fold cross-validation, and bold indicates the best performance based on unrounded values. All metrics use two decimal places, except Cohen’s _𝜅_ , which uses three decimals due to its small magnitude on some datasets. In Tables 8 to 29, models are grouped by SSL paradigm and sorted by the primary metric within each group. 

**Table 8:** Performance of BFMs on the CHBMIT dataset. 

|Type|Model|AUROC|Acc|F1|F2|
|---|---|---|---|---|---|
|C|MBrain|.71±.03|.73±.06|.31±.15|.28±.20|
||BIOT|.56±.08|.29±.05|.41±.03|.61±.02|
||Bendr|.55±.03|.59±.03|.32±.02|.36±.04|
||SppEEGNet|.43±.05|.60±.06|.31±.04|.33±.05|
|G|BrainWave|**.90±.03**|**.80±.12**|**.71±.09**|**.78±.04**|
||REVE|.84±.10|.78±.12|.63±.14|.66±.13|
||NeuroGPT-E|.78±.12|.75±.07|.51±.22|.63±.16|
||BrainBERT|.78±.06|.75±.10|.58±.08|.61±.09|
||LaBraM|.75±.10|.73±.10|.53±.14|.57±.17|
||BrainOmni|.74±.13|.67±.19|.51±.12|.56±.12|
||BFM|.74±.05|.72±.03|.51±.09|.51±.14|
||CBraMod|.69±.04|.70±.08|.46±.08|.49±.14|
||NeuroGPT-D|.61±.07|.73±.03|.18±.23|.19±.25|
||Brant|.55±.05|.70±.01|.00±.00|.00±.00|
|O|EEGPT|.71±.09|.67±.11|.46±.06|.51±.15|
||NeuroLM|.67±.06|.54±.20|.27±.23|.38±.34|



### **C Experimental Setup** 

We evaluate all models under a unified cross-subject protocol with cross-validation, following standard practice in benchmarks. Models are finetuned for up to 50 epochs with early stopping (patience = 5) based on validation performance. For optimization, we primarily use Adam or AdamW. For a small number of BFMs, we retain their original optimizers as specified by the authors to avoid unintended performance degradation caused by altering model specific training designs. Batch sizes are adjusted according to model capacity and GPU memory constraints. To ensure comparability and avoid excessive tuning, we use fixed learning rates across all models: 1 × 10<sup>−5</sup> for the BFMs backbone and 1 × 10<sup>−4</sup> for the classifier head. 

### **D Benchmark Result** 

We report the complete evaluation results of all 15 BFMs across 22 downstream classification tasks. For NeuroGPT, we report both encoder-only (NeuroGPT-E) and encoder–decoder (NeuroGPT-D) variants, complementing the analysis in Section 3.3.2. Full results provide comprehensive evidence for the observed cross-task performance trends among different BFMs. For binary tasks, we report 

**Table 9:** Performance of BFMs on the MAYO dataset. 

|Type|Model|AUROC|Acc|F1|F2|
|---|---|---|---|---|---|
|C|Bendr|.93±.03|.90±.02|.69±.13|.75±.11|
||MBrain|.92±.04|.92±.02|.70±.11|.73±.09|
||BIOT|.90±.07|.88±.05|.63±.14|.72±.13|
||SppEEGNet|.56±.03|.75±.05|.34±.09|.39±.09|
|G|BrainWave|**.98±.01**|.93±.02|.81±.09|**.86±.03**|
||BrainBERT|.97±.01|**.95±.01**|**.81±.07**|.83±.07|
||LaBraM|.96±.02|.93±.02|.76±.12|.80±.09|
||NeuroGPT-E|.96±.02|.93±.02|.71±.07|.67±.08|
||REVE|.92±.04|.89±.04|.66±.13|.72±.11|
||Brant|.92±.03|.82±.12|.58±.19|.69±.14|
||BrainOmni|.91±.06|.91±.02|.67±.13|.69±.12|
||CBraMod|.89±.04|.87±.02|.59±.12|.64±.10|
||BFM|.81±.08|.68±.08|.43±.15|.59±.14|
||NeuroGPT-D|.77±.15|.88±.03|.23±.26|.19±.21|
|O|EEGPT|.92±.03|.90±.03|.67±.10|.70±.07|
||NeuroLM|.64±.09|.72±.16|.30±.20|.37±.26|



Brain4FMs: A Benchmark of Foundation Models for Electrical Brain Signals 

**Table 10:** Performance of BFMs on the FNUSA dataset. 

|Type|Model|AUROC|Acc|F1|F2|
|---|---|---|---|---|---|
|C|MBrain|.91±.08|.87±.08|.75±.13|.76±.16|
||Bendr|.88±.06|.84±.06|.73±.11|.77±.10|
||BIOT|.87±.07|.83±.08|.73±.14|.77±.10|
||SppEEGNet|.64±.08|.67±.05|.48±.13|.52±.18|
|G|BrainWave|**.92±.05**|.89±.06|**.83±.06**|**.83±.04**|
||NeuroGPT-E|.90±.06|.86±.05|.74±.04|.72±.11|
||BrainBERT|.90±.04|**.89±.04**|.77±.09|.79±.08|
||LaBraM|.89±.08|.82±.10|.72±.15|.76±.11|
||BrainOmni|.88±.07|.84±.05|.73±.08|.75±.09|
||REVE|.87±.08|.82±.07|.71±.10|.74±.08|
||Brant|.87±.12|.84±.07|.75±.06|.79±.08|
||BFM|.78±.12|.69±.11|.62±.05|.69±.08|
||NeuroGPT-D|.72±.12|.77±.12|.30±.38|.27±.35|
||CBraMod|.71±.13|.78±.08|.62±.13|.64±.12|
|O|EEGPT|.90±.04|.84±.06|.75±.11|.78±.08|
||NeuroLM|.64±.14|.72±.17|.37±.28|.38±.35|



**Table 11:** Performance of BFMs on the ADFD dataset. 

|Type|Model|AUROC|Acc|F1|F2|
|---|---|---|---|---|---|
|C|BIOT|.56±.17|.49±.12|.58±.14|.70±.24|
||MBrain|.53±.12|.50±.10|.53±.12|.52±.14|
||Bendr|.52±.02|.52±.01|.54±.05|.52±.07|
||SppEEGNet|.52±.02|.51±.02|.51±.05|.49±.07|
|G|REVE|**.84±.07**|**.77±.08**|**.79±.07**|.79±.09|
||BrainOmni|.80±.07|.71±.04|.73±.05|.72±.09|
||BrainWave|.74±.05|.68±.05|.68±.10|.73±.10|
||LaBraM|.72±.07|.68±.05|.68±.09|.72±.07|
||BrainBERT|.59±.05|.58±.05|.60±.11|.64±.15|
||BFM|.59±.08|.58±.09|.59±.12|.61±.09|
||CBraMod|.55±.06|.59±.04|.41±.20|.37±.20|
||NeuroGPT-E|.51±.03|.55±.01|.71±.01|.85±.01|
||Brant|.50±.07|.54±.04|.70±.03|.84±.04|
||NeuroGPT-D|.50±.03|.55±.01|.71±.01|**.86±.01**|
|O|EEGPT|.81±.05|.72±.05|.73±.05|.70±.07|
||NeuroLM|.51±.04|.53±.03|.63±.09|.71±.16|



**Table 12:** Performance of BFMs on the ADHD-Adult dataset. 

|Type|Model|AUROC|Acc|F1|F2|
|---|---|---|---|---|---|
|C|BIOT|.96±.02|.90±.04|.89±.04|.90±.05|
||MBrain|.95±.03|.92±.04|.91±.04|.91±.06|
||Bendr|.62±.03|.61±.04|.60±.05|.61±.06|
||SppEEGNet|.51±.04|.54±.06|.36±.30|.36±.35|
|G|BrainOmni|.96±.02|.91±.02|.90±.03|.89±.04|
||BrainWave|.96±.03|.91±.04|.91±.04|.91±.05|
||REVE|.96±.02|.91±.02|.91±.02|.90±.05|
||Brant|.95±.03|.89±.04|.89±.04|.90±.05|
||LaBraM|.95±.04|.91±.04|**.92±.04**|**.91±.04**|
||CBraMod|.95±.02|**.92±.04**|.91±.04|.91±.07|
||NeuroGPT-E|.91±.05|.84±.06|.83±.05|.82±.03|
||BFM|.88±.04|.82±.04|.80±.04|.81±.05|
||NeuroGPT-D|.88±.05|.82±.05|.82±.04|.85±.03|
||BrainBERT|.74±.05|.69±.05|.61±.11|.57±.14|
|O|EEGPT|**.96±.03**|.91±.04|.90±.05|.89±.08|
||NeuroLM|.82±.14|.75±.07|.74±.06|.77±.11|



**Table 13:** Performance of BFMs on the ADHD-Child dataset. 

|Type|Model|AUROC|Acc|F1|F2|
|---|---|---|---|---|---|
|C|MBrain|.69±.11|.63±.08|.66±.06|.66±.04|
||BIOT|.55±.05|**.75±.06**|**.85±.04**|**.93±.02**|
||SppEEGNet|.53±.05|.49±.04|.48±.07|.45±.08|
||Bendr|.53±.02|.51±.01|.52±.02|.49±.02|
|G|REVE|**.79±.07**|.71±.04|.74±.06|.74±.08|
||BrainWave|.78±.04|.71±.04|.74±.06|.74±.12|
||BrainOmni|.71±.09|.62±.07|.63±.09|.61±.14|
||BFM|.69±.11|.69±.09|.75±.07|.75±.04|
||LaBraM|.66±.12|.64±.08|.74±.06|.70±.07|
||CBraMod|.64±.05|.64±.06|.73±.03|.81±.05|
||Brant|.58±.07|.54±.07|.62±.15|.68±.23|
||NeuroGPT-E|.55±.02|.56±.03|.72±.02|.86±.01|
||BrainBERT|.55±.03|.56±.03|.56±.07|.53±.09|
||NeuroGPT-D|.47±.12|.56±.06|.64±.11|.69±.18|
|O|EEGPT|.67±.13|.64±.10|.68±.10|.68±.12|
||NeuroLM|.64±.06|.60±.05|.71±.04|.80±.05|



**Table 14:** Performance of BFMs on the UCSD-OFF dataset. 

|Type|Model|AUROC|Acc|F1|F2|
|---|---|---|---|---|---|
|C|SppEEGNet|.53±.07|.51±.06|.59±.15|**.71±.25**|
||Bendr|.52±.04|.51±.03|.48±.05|.47±.05|
||BIOT|.51±.19|.49±.05|.56±.27|.69±.35|
||MBrain|.50±.04|.44±.04|.32±.23|.34±.29|
|G|BrainOmni|**.64±.09**|.57±.06|.54±.16|.57±.26|
||CBraMod|.63±.05|.58±.04|.46±.09|.40±.12|
||REVE|.62±.19|**.58±.17**|.58±.19|.60±.24|
||LaBraM|.59±.05|.56±.03|.57±.08|.60±.15|
||BrainWave|.58±.06|.53±.10|**.62±.12**|.71±.19|
||NeuroGPT-E|.56±.06|.54±.05|.57±.12|.62±.22|
||BFM|.53±.03|.49±.12|.36±.09|.47±.17|
||Brant|.52±.10|.45±.22|.42±.29|.58±.35|
||BrainBERT|.51±.06|.54±.06|.49±.17|.49±.20|
||NeuroGPT-D|.45±.07|.51±.05|.01±.01|.00±.01|
|O|EEGPT|.61±.13|.55±.08|.56±.10|.58±.17|
||NeuroLM|.51±.07|.50±.05|.53±.15|.61±.23|



**Table 15:** Performance of BFMs on the UCSD-ON dataset. 

|Type|Model|AUROC|Acc|F1|F2|
|---|---|---|---|---|---|
|C|Bendr|.51±.05|.49±.05|.43±.05|.41±.06|
||SppEEGNet|.49±.08|.50±.11|.46±.23|.48±.27|
||MBrain|.49±.15|.46±.14|.37±.17|.34±.18|
||BIOT|.46±.18|.49±.05|**.65±.05**|**.81±.04**|
|G|BrainWave|**.69±.20**|.53±.08|.60±.06|.69±.14|
||REVE|.63±.19|**.56±.13**|.45±.29|.46±.33|
||CBraMod|.60±.12|.49±.08|.18±.08|.13±.07|
||NeuroGPT-E|.56±.10|.53±.07|.58±.10|.64±.13|
||Brant|.56±.11|.52±.11|.29±.28|.31±.34|
||BrainOmni|.53±.14|.49±.12|.49±.16|.51±.20|
||LaBraM|.51±.22|.45±.11|.33±.19|.31±.19|
||BrainBERT|.51±.05|.51±.06|.51±.11|.54±.17|
||NeuroGPT-D|.46±.10|.47±.06|.29±.25|.31±.28|
||BFM|.44±.08|.48±.07|.42±.17|.42±.20|
|O|EEGPT|.51±.21|.48±.17|.49±.15|.49±.14|
||NeuroLM|.44±.18|.51±.18|.47±.24|.48±.29|



Shen et al. 

**Table 16:** Performance of BFMs on the EEGMat dataset. 

|Type|Model|AUROC|Acc|F1|F2|
|---|---|---|---|---|---|
|C|MBrain|.68±.06|.75±.02|.13±.15|.10±.11|
||BIOT|.59±.08|.27±.01|.42±.01|**.65±.01**|
||Bendr|.54±.02|.66±.05|.34±.07|.34±.06|
||SppEEGNet|.52±.03|.50±.07|.37±.04|.47±.09|
|G|REVE|**.78±.09**|**.75±.08**|.39±.27|.61±.09|
||LaBraM|.71±.03|.68±.04|.48±.07|.53±.13|
||NeuroGPT-E|.70±.04|.73±.04|.25±.20|.22±.20|
||BrainOmni|.68±.07|.60±.07|.48±.04|.60±.06|
||BrainWave|.66±.06|.51±.20|.44±.07|.55±.08|
||CBraMod|.63±.06|.72±.04|.19±.18|.16±.17|
||BrainBERT|.61±.07|.67±.06|.45±.09|.50±.13|
||BFM|.60±.03|.66±.04|.35±.06|.36±.10|
||Brant|.57±.12|.75±.01|.00±.00|.00±.00|
||NeuroGPT-D|.51±.06|.73±.01|.00±.00|.00±.00|
|O|EEGPT|.67±.04|.64±.06|**.49±.02**|.59±.04|
||NeuroLM|.63±.08|.31±.10|.42±.04|.64±.04|



**Table 17:** Performance of BFMs on the SD-28 dataset. 

|Type|Model|AUROC|Acc|F1|F2|
|---|---|---|---|---|---|
|C|MBrain|.58±.10|.58±.10|.64±.13|.66±.15|
||BIOT|.56±.09|.62±.12|.68±.18|.65±.21|
||Bendr|.49±.05|.50±.03|.48±.05|.45±.04|
||SppEEGNet|.49±.03|.47±.04|.33±.06|.27±.05|
|G|BrainWave|**.88±.07**|**.81±.06**|**.83±.08**|.81±.11|
||REVE|.81±.13|.75±.13|.80±.10|**.86±.11**|
||NeuroGPT-D|.80±.17|.77±.13|.80±.11|.84±.14|
||BrainBERT|.73±.11|.66±.15|.63±.26|.62±.29|
||NeuroGPT-E|.72±.12|.66±.14|.73±.15|.69±.19|
||BrainOmni|.69±.15|.69±.12|.73±.14|.77±.19|
||BFM|.69±.15|.62±.05|.73±.04|.81±.08|
||CBraMod|.54±.14|.58±.05|.58±.18|.58±.24|
||LaBraM|.54±.07|.54±.04|.59±.07|.59±.13|
||Brant|.51±.11|.46±.08|.47±.17|.50±.30|
|O|EEGPT|.56±.21|.56±.11|.62±.12|.66±.15|
||NeuroLM|.49±.04|.49±.05|.53±.28|.62±.35|



**Table 18:** Performance of BFMs on the MDD-64 dataset. 

|Type|Model|AUROC|Acc|F1|F2|
|---|---|---|---|---|---|
|C|MBrain|.93±.08|.87±.11|.89±.08|.91±.05|
||Bendr|.78±.07|.73±.04|.75±.03|.76±.04|
||BIOT|.53±.12|.33±.01|.50±.01|.71±.00|
||SppEEGNet|.52±.02|.55±.04|.50±.05|.45±.05|
|G|REVE|**.97±.04**|**.88±.09**|**.90±.06**|**.92±.04**|
||BrainOmni|.94±.07|.85±.09|.87±.07|.89±.05|
||BrainWave|.94±.03|.85±.02|.84±.03|.81±.06|
||BFM|.93±.08|.86±.11|.88±.08|.91±.05|
||BrainBERT|.92±.07|.85±.07|.85±.06|.85±.10|
||Brant|.92±.09|.80±.10|.80±.14|.80±.19|
||CBraMod|.90±.13|.84±.12|.86±.09|.87±.09|
||LaBraM|.87±.12|.81±.11|.78±.09|.83±.04|
||NeuroGPT-E|.87±.05|.80±.05|.84±.03|.90±.03|
||NeuroGPT-D|.70±.12|.67±.13|.77±.07|.89±.04|
|O|EEGPT|.94±.05|.87±.08|.88±.06|.90±.04|
||NeuroLM|.82±.11|.80±.06|.80±.09|.81±.18|



**Table 19:** Performance of BFMs on the Dep-BDI dataset. 

|Type|Model|AUROC|Acc|F1|F2|
|---|---|---|---|---|---|
|C|BIOT|.60±.11|.30±.17|.11±.02|.22±.05|
||MBrain|.59±.07|.62±.03|.24±.16|.20±.16|
||Bendr|.54±.03|.54±.03|.45±.03|.47±.03|
||SppEEGNet|.50±.02|.49±.04|.41±.04|.45±.04|
|G|BrainWave|**.72±.03**|.66±.03|**.62±.03**|.67±.06|
||BrainOmni|.68±.12|.63±.09|.55±.10|.58±.13|
||REVE|.67±.12|.65±.08|.47±.14|.45±.17|
||LaBraM|.65±.10|.59±.11|.60±.09|**.71±.08**|
||BrainBERT|.64±.09|.61±.05|.48±.11|.48±.12|
||BFM|.62±.10|.59±.06|.48±.10|.51±.13|
||NeuroGPT-E|.59±.08|.62±.01|.02±.02|.01±.01|
||CBraMod|.54±.05|**.69±.14**|.13±.08|.16±.10|
||Brant|.53±.09|.62±.01|.00±.00|.00±.00|
||NeuroGPT-D|.51±.08|.62±.01|.00±.00|.00±.00|
|O|EEGPT|.63±.04|.62±.05|.50±.05|.51±.11|
||NeuroLM|.54±.05|.61±.02|.30±.26|.31±.31|



**Table 20:** Performance of BFMs on the Dep-STAI dataset. 

|Type|Model|AUROC|Acc|MF1|Kappa|
|---|---|---|---|---|---|
|C|BIOT|.56±.09|.37±.07|.33±.07|.073±.088|
||MBrain|.55±.04|.60±.03|.30±.05|.054±.059|
||Bendr|.54±.03|.48±.03|.36±.03|.047±.041|
||SppEEGNet|.51±.02|.46±.03|.33±.01|.007±.024|
|G|BrainWave|**.64±.06**|.51±.05|**.42±.05**|**.150±.053**|
||NeuroGPT-E|.61±.09|.55±.07|.38±.10|.129±.155|
||LaBraM|.61±.09|.36±.10|.26±.06|.081±.093|
||BrainBERT|.60±.06|.48±.11|.32±.08|.064±.126|
||BrainOmni|.60±.06|.53±.05|.36±.05|.105±.062|
||BFM|.58±.08|.45±.09|.37±.06|.099±.117|
||NeuroGPT-D|.57±.06|**.61±.01**|.25±.00|.000±.000|
||REVE|.54±.11|.54±.10|.35±.08|.079±.200|
||CBraMod|.54±.04|.60±.02|.30±.04|.049±.052|
||Brant|.53±.03|**.61±.01**|.25±.00|.000±.000|
|O|EEGPT|.56±.06|.51±.06|.34±.06|.025±.080|
||NeuroLM|.50±.04|.58±.04|.26±.02|.009±.018|



**Table 21:** Performance of BFMs on the ISRUC-G1 dataset. 

|Type|Model|AUROC|Acc|MF1|Kappa|
|---|---|---|---|---|---|
|C|MBrain|.87±.04|.63±.07|.55±.07|.514±.084|
||BIOT|.78±.04|.46±.07|.44±.02|.322±.071|
||Bendr|.72±.04|.43±.07|.39±.05|.269±.076|
||SppEEGNet|.53±.01|.17±.03|.15±.02|.012±.009|
|G|REVE|**.92±.01**|**.69±.03**|**.65±.05**|**.598±.036**|
||BrainOmni|.91±.02|.68±.03|.64±.04|.581±.030|
||BrainWave|.89±.01|.62±.05|.60±.02|.522±.064|
||CBraMod|.86±.05|.54±.08|.48±.10|.419±.094|
||LaBraM|.85±.02|.61±.02|.56±.05|.502±.028|
||Brant|.84±.02|.55±.01|.50±.04|.427±.016|
||NeuroGPT-E|.80±.02|.44±.11|.41±.11|.319±.101|
||BrainBERT|.80±.03|.47±.05|.42±.07|.332±.058|
||BFM|.78±.03|.47±.04|.37±.13|.264±.148|
||NeuroGPT-D|.61±.07|.31±.07|.17±.08|.060±.102|
|O|EEGPT|.87±.02|.60±.05|.57±.08|.486±.070|
||NeuroLM|.67±.05|.27±.11|.15±.10|.074±.074|



Brain4FMs: A Benchmark of Foundation Models for Electrical Brain Signals 

**Table 22:** Performance of BFMs on the SleepEDF dataset. 

|Type|Model|AUROC|Acc|MF1|Kappa|
|---|---|---|---|---|---|
|C|MBrain|**.94±.01**|**.79±.04**|**.73±.05**|**.709±.059**|
||Bendr|.91±.01|.69±.06|.65±.04|.591±.062|
||BIOT|.58±.16|.35±.16|.21±.12|.070±.145|
||SppEEGNet|.57±.01|.22±.01|.20±.01|.104±.028|
|G|NeuroGPT-E|.94±.01|.78±.03|.70±.03|.696±.045|
||Brant|.94±.01|.73±.07|.70±.05|.639±.083|
||CBraMod|.93±.01|.73±.04|.69±.04|.642±.054|
||LaBraM|.93±.01|.76±.04|.68±.03|.669±.050|
||BrainBERT|.91±.02|.68±.07|.65±.05|.578±.079|
||BrainWave|.89±.02|.67±.05|.54±.08|.516±.104|
||BFM|.89±.01|.65±.04|.60±.03|.558±.053|
||BrainOmni|.87±.00|.63±.03|.60±.01|.506±.025|
||REVE|.78±.38|.63±.30|.60±.28|.561±.257|
||NeuroGPT-D|.65±.03|.48±.04|.21±.05|.100±.068|
|O|EEGPT|.91±.00|.68±.03|.66±.01|.578±.026|
||NeuroLM|.61±.06|.18±.04|.11±.03|.189±.263|



**Table 23:** Performance of BFMs on the BCI-2a dataset. 

|Type|Model|AUROC|Acc|MF1|Kappa|
|---|---|---|---|---|---|
|C|MBrain|.54±.02|.27±.02|.19±.03|.027±.023|
||Bendr|.51±.01|.25±.01|.25±.01|.005±.011|
||SppEEGNet|.51±.01|.25±.01|.24±.02|.003±.020|
||BIOT|.50±.01|.24±.02|.17±.02|-.015±.022|
|G|REVE|**.61±.01**|.34±.01|.30±.02|.115±.012|
||NeuroGPT-E|.61±.02|**.35±.03**|**.33±.02**|**.128±.041**|
||LaBraM|.55±.03|.28±.02|.23±.04|.045±.027|
||Brant|.54±.00|.25±.00|.10±.00|.000±.000|
||BrainWave|.54±.02|.27±.02|.20±.03|.031±.022|
||BrainOmni|.54±.01|.27±.02|.22±.02|.021±.029|
||CBraMod|.54±.01|.27±.01|.20±.02|.022±.012|
||BFM|.51±.01|.26±.01|.25±.00|.013±.012|
||NeuroGPT-D|.51±.03|.26±.01|.15±.03|.007±.019|
||BrainBERT|.50±.01|.25±.02|.23±.02|.005±.023|
|O|EEGPT|.57±.03|.28±.02|.22±.01|.036±.024|
||NeuroLM|.52±.02|.27±.01|.20±.02|.030±.018|



**Table 24:** Performance of BFMs on the EEGMMIDB-I dataset. 

|Type|Model|AUROC|Acc|MF1|Kappa|
|---|---|---|---|---|---|
|C|Bendr|.55±.01|.29±.01|.29±.01|.054±.010|
||MBrain|.51±.01|.26±.01|.16±.05|.009±.011|
||SppEEGNet|.51±.01|.26±.01|.23±.01|.008±.013|
||BIOT|.50±.01|.25±.00|.20±.02|-.005±.004|
|G|REVE|**.82±.01**|**.59±.02**|**.59±.02**|**.451±.031**|
||NeuroGPT-E|.78±.01|.54±.01|.54±.01|.392±.019|
||BrainOmni|.76±.01|.51±.01|.51±.01|.351±.019|
||LaBraM|.59±.02|.31±.02|.25±.03|.078±.032|
||CBraMod|.58±.02|.30±.02|.28±.04|.073±.028|
||BFM|.52±.01|.27±.01|.26±.01|.023±.009|
||BrainWave|.51±.01|.25±.01|.18±.01|.001±.014|
||Brant|.51±.01|.25±.00|.10±.00|.000±.000|
||BrainBERT|.49±.00|.25±.00|.16±.02|-.003±.005|
||NeuroGPT-D|.49±.01|.25±.01|.16±.05|-.007±.008|
|O|EEGPT|.52±.01|.27±.02|.24±.04|.023±.022|
||NeuroLM|.51±.01|.25±.01|.15±.05|.005±.008|



**Table 25:** Performance of BFMs on the EEGMMIDB-R dataset. 

|Type|Model|AUROC|Acc|MF1|Kappa|
|---|---|---|---|---|---|
|C|Bendr|.55±.01|.29±.01|.29±.01|.060±.014|
||SppEEGNet|.52±.00|.26±.01|.24±.01|.014±.008|
||MBrain|.52±.01|.26±.01|.19±.05|.008±.016|
||BIOT|.50±.01|.25±.01|.21±.02|.003±.011|
|G|REVE|**.82±.00**|**.59±.01**|**.58±.01**|**.448±.014**|
||NeuroGPT-E|.77±.02|.54±.02|.53±.02|.381±.030|
||BrainOmni|.74±.01|.49±.01|.49±.01|.325±.014|
||CBraMod|.57±.01|.30±.02|.27±.03|.061±.022|
||LaBraM|.55±.02|.28±.02|.23±.03|.041±.027|
||BFM|.52±.01|.27±.01|.26±.01|.024±.008|
||NeuroGPT-D|.50±.00|.25±.00|.14±.01|.003±.003|
||Brant|.50±.01|.25±.00|.10±.00|.000±.000|
||BrainWave|.50±.01|.25±.01|.17±.02|-.004±.011|
||BrainBERT|.50±.01|.25±.00|.16±.03|.001±.006|
|O|NeuroLM|.52±.02|.26±.01|.14±.05|.009±.017|
||EEGPT|.51±.01|.25±.01|.23±.03|.006±.017|



**Table 26:** Performance of BFMs on the DEAP dataset. 

|Type|Model|AUROC|Acc|MF1|Kappa|
|---|---|---|---|---|---|
|C|SppEEGNet|.51±.03|.27±.06|.23±.03|.007±.027|
||MBrain|.51±.05|.42±.04|.15±.01|.000±.000|
||BIOT|.50±.03|.30±.06|.18±.02|-.014±.030|
||Bendr|.50±.02|.26±.02|**.24±.02**|-.004±.035|
|G|BrainBERT|**.52±.02**|.23±.02|.18±.03|.017±.020|
||NeuroGPT-D|.51±.03|**.44±.04**|.15±.01|.000±.000|
||BrainWave|.51±.03|.27±.07|.23±.06|.010±.077|
||CBraMod|.51±.01|.19±.02|.14±.02|-.001±.009|
||LaBraM|.51±.02|.29±.04|.21±.03|.016±.014|
||REVE|.50±.05|.26±.05|.21±.03|-.013±.035|
||BFM|.50±.02|.28±.07|.22±.02|.005±.015|
||NeuroGPT-E|.49±.01|.42±.03|.17±.03|-.004±.006|
||Brant|.48±.02|.34±.17|.12±.06|.000±.000|
||BrainOmni|.45±.03|.22±.03|.19±.01|-.046±.022|
|O|NeuroLM|.51±.03|.33±.13|.13±.03|-.003±.007|
||EEGPT|.50±.02|.26±.05|.22±.04|**.029±.027**|



**Table 27:** Performance of BFMs on the SEED-IV dataset. 

|Type|Model|AUROC|Acc|MF1|Kappa|
|---|---|---|---|---|---|
|C|MBrain|.52±.01|.26±.01|.21±.04|.014±.020|
||Bendr|.50±.00|.25±.00|.25±.00|-.001±.005|
||SppEEGNet|.50±.00|.25±.00|.24±.00|-.001±.002|
||BIOT|.48±.00|.24±.01|.19±.02|-.018±.003|
|G|NeuroGPT-E|**.57±.01**|**.30±.01**|.26±.02|.003±.005|
||REVE|.54±.01|.28±.02|**.27±.01**|**.039±.019**|
||BrainOmni|.53±.01|.28±.02|.26±.01|.035±.019|
||BrainWave|.53±.02|.27±.02|.22±.03|.023±.026|
||BFM|.52±.01|.27±.01|.24±.01|.012±.004|
||CBraMod|.51±.01|.26±.01|.21±.03|.010±.010|
||BrainBERT|.51±.03|.25±.02|.17±.05|.003±.012|
||LaBraM|.51±.01|.25±.01|.20±.02|.008±.014|
||NeuroGPT-D|.50±.00|.27±.00|.11±.00|.000±.000|
||Brant|.50±.01|.26±.01|.10±.00|.000±.000|
|O|EEGPT|.51±.01|.25±.01|.22±.02|.006±.016|
||NeuroLM|.50±.00|.25±.00|.13±.04|.001±.002|



Shen et al. 

**Table 28:** Performance of BFMs on the Chisco-I dataset. 

|Type|Model|AUROC|Acc|MF1|Kappa|
|---|---|---|---|---|---|
|C|MBrain|.50±.01|.03±.00|.00±.00|.000±.001|
||Bendr|.50±.01|.03±.00|**.02±.00**|.000±.002|
||SppEEGNet|.50±.00|.02±.00|.01±.00|-.000±.001|
||BIOT|.49±.00|.03±.01|.01±.00|.000±.001|
|G|LaBraM|**.51±.01**|.04±.01|.01±.00|**.005±.004**|
||CBraMod|.51±.01|.04±.01|.01±.00|.003±.003|
||BrainOmni|.50±.01|.02±.00|.01±.00|.001±.001|
||BFM|.50±.00|.03±.00|.01±.00|.001±.001|
||NeuroGPT-D|.50±.00|.05±.00|.00±.00|.001±.004|
||BrainBERT|.50±.01|.03±.00|.01±.01|.001±.003|
||REVE|.50±.00|.03±.00|.02±.00|.000±.001|
||NeuroGPT-E|.50±.01|**.05±.00**|.00±.00|-.000±.004|
||BrainWave|.50±.01|.03±.01|.00±.00|.002±.003|
||Brant|.50±.00|.04±.01|.00±.00|.000±.000|
|O|EEGPT|.50±.00|.03±.01|.01±.00|.001±.003|
||NeuroLM|.50±.00|.04±.01|.00±.00|-.001±.001|



**Table 30: Full quantitative results of decision-boundary diagnostics.** The table reports _𝐿𝑀𝐸𝑅_ , _𝐿𝑀𝐸𝑆_ , and _𝑅𝑐𝑙𝑠_ for all contrastiveand generative-based models (q=0.10). 

|||ADFD||C|HBMI|T||SD-28||
|---|---|---|---|---|---|---|---|---|---|
|Model|_𝐿𝑀𝐸𝑅_|_𝐿𝑀𝐸𝑆_|_𝑅𝑐𝑙𝑠_|_𝐿𝑀𝐸𝑅_|_𝐿𝑀𝐸𝑆_|_𝑅𝑐𝑙𝑠_|_𝐿𝑀𝐸𝑅_|_𝐿𝑀𝐸𝑆_|_𝑅𝑐𝑙𝑠_|
|SppEEGNet|.497|.107|0.658|.483|.127|2.208|.490|.098|1.557|
|Bendr|.499|.105|0.658|.497|.117|0.962|.488|.994|0.941|
|BIOT|.470|.098|2.344|.615|.087|2.328|.497|.112|2.865|
|MBrain|.526|.113|1.980|.550|.219|2.047|.480|.103|2.590|
|BrainBERT|.492|.126|0.842|.457|.203|2.103|.478|.157|2.091|
|BrainWave|.455|.172|2.275|.499|.197|2.613|.409|.179|3.229|
|CBraMod|.492|.109|1.892|.445|.161|2.207|.456|.097|2.510|
|BrainOmni|.487|.175|3.465|.469|.173|2.558|.376|.122|3.546|
|REVE|.431|.205|2.914|.447|.261|2.408|.447|.213|3.534|
|NeuroGPT-E|.506|.193|3.736|.478|.201|3.385|.422|.219|5.577|
|LaBraM|.443|.176|3.846|.435|.179|2.979|.482|.098|2.003|
|BFM|.490|.124|0.815|.460|.169|0.838|.516|.134|1.266|
|Brant|.408|.089|0.730|.361|.146|0.791|.375|.070|1.551|



**Table 29:** Performance of BFMs on the Chisco-R dataset. 

|Type|Model|AUROC|Acc|MF1|Kappa|
|---|---|---|---|---|---|
|C|BIOT|.50±.01|.04±.00|.01±.00|-.000±.003|
||MBrain|.50±.00|.04±.00|.00±.00|.000±.000|
||SppEEGNet|.50±.00|.02±.00|.01±.00|.000±.003|
||Bendr|.50±.00|.03±.00|**.02±.00**|.001±.003|
|G|BrainWave|**.51±.02**|.03±.01|.00±.00|.001±.003|
||BrainOmni|.51±.01|.03±.01|.01±.00|.002±.005|
||LaBraM|.51±.01|.03±.01|.01±.00|.002±.004|
||NeuroGPT-D|.51±.01|**.05±.00**|.00±.00|.002±.003|
||CBraMod|.51±.01|.03±.01|.01±.00|-.000±.005|
||NeuroGPT-E|.50±.01|.05±.00|.00±.00|.001±.003|
||BFM|.50±.00|.03±.01|.01±.00|.001±.002|
||REVE|.50±.01|.03±.00|.02±.00|.000±.003|
||Brant|.50±.00|.04±.01|.00±.00|.000±.000|
||BrainBERT|.50±.00|.03±.01|.00±.00|.001±.001|
|O|EEGPT|.50±.01|.03±.01|.01±.01|**.002±.002**|
||NeuroLM|.50±.00|.03±.02|.00±.00|-.000±.000|



### **E Additional Results for SSL Strategy Analysis** 

This section reports full results and robustness checks that support the trends discussed in Section 3.3.2. Specifically, we report the complete quantitative results of the decision-boundary and embedding diagnostics across all evaluated models, and a sensitivity analysis with respect to the boundary quantile parameter _𝑞_ . Table 30 reports the decision-boundary metrics _𝐿𝑀𝐸𝑅_ and _𝐿𝑀𝐸𝑆_ and the embedding class-separation ratio _𝑅𝑐𝑙𝑠_ for all contrastive- and generative-based BFMs on the three representative datasets analyzed in the main text. The complete table allows a fine-grained comparison beyond the representative models shown in the main paper. 

Figure 4 presents a sensitivity analysis of the decision-boundary metrics under different quantile thresholds _𝑞_ ∈{0 _._ 05 _,_ 0 _._ 10 _,_ 0 _._ 20} used to define the low-margin region B _𝑞_ . While absolute values vary with _𝑞_ , the relative trends between contrastive and generative models remain stable. This confirms that the conclusions are not an artifact of a specific boundary choice. 



**Figure 4:** Sensitivity of decision-boundary error concentration to the boundary definition. 

### **F Additional Spatial Analysis Results** 

This appendix provides detailed results supporting the spatialstructure analysis discussed in Section 3.3.3. We report the full quantitative impact of channel-permutation perturbations across datasets and models. We permute channels in the training and validation splits to probe whether BFMs encode dataset-specific spatial structure. All other settings are kept identical, so any performance change is attributable to disrupted channel topology. Tables 31 to 34 reports all metrics before or after permutation. We focus on AUROC in the main analysis, and these results support that some BFMs internalize dataset-specific spatial structure during training. 

Brain4FMs: A Benchmark of Foundation Models for Electrical Brain Signals 

**Table 31:** Performance under channel-permutation setting. We report AUROC, Accuracy, F1 and F2 for models trained on original data (origin) and shuffled data (shuffle) on ADHD-Child. 

||AUROC|A|cc|F|1<br>F2|
|---|---|---|---|---|---|
|Model|shufe origin|shufe|origin|shufe|origin shufe origin|
|BrainBERT|.54±.04 .55±.03|.55±.03|.56±.03|.58±.04|.56±.07 .58±.05 .53±.09|
|BrainWave|.68±.04 .78±.04|.66±.05|.71±.04|.68±.12|.74±.06 .68±.19 .74±.12|
|BrainOmni|.71±.09 .71±.09|.62±.07|.62±.07|.63±.09|.63±.09 .61±.15 .61±.14|
|CBraMod|.60±.06 .64±.05|.57±.03|.64±.06|.72±.03|.73±.03 .85±.03 .81±.05|
|EEGPT|.63±.11 .67±.13|.60±.10|.64±.10|.57±.28|.68±.10 .59±.32 .68±.12|
|MBrain|.69±.11 .69±.11|.63±.09|.63±.08|.68±.07|.66±.06 .70±.05 .66±.04|
|NeuroGPT-E|.55±.02 .55±.02|.56±.03|.56±.03|.72±.02|.72±.02 .86±.01 .86±.01|
|REVE|.71±.09 .79±.07|.55±.11|.71±.04|.36±.31|.74±.06 .32±.30 .74±.08|



**Table 35:** Channel-permutation performance on UCSD-OFF. 

||AUROC|A|cc|F|1<br>F2|
|---|---|---|---|---|---|
|Model|shufe origin|shufe|origin|shufe|origin shufe origin|
|BrainBERT|.52±.09 .51±.06|.53±.06|.54±.06|.60±.10|.49±.17 .68±.15 .49±.20|
|BrainWave|.49±.19 .58±.06|.56±.10|.53±.10|.43±.29|.62±.12 .44±.34 .71±.19|
|BrainOmni|.62±.07 .64±.09|.56±.04|.57±.06|.57±.10|.54±.16 .61±.21 .57±.26|
|CBraMod|.60±.05 .63±.05|.56±.04|.58±.04|.32±.17|.46±.09 .27±.19 .40±.12|
|EEGPT|.62±.15 .61±.13|.60±.12|.55±.08|.55±.17|.56±.10 .53±.20 .58±.17|
|MBrain|.48±.09 .50±.04|.44±.06|.44±.04|.35±.22|.32±.23 .38±.31 .34±.29|
|NeuroGPT-E|.56±.07 .56±.06|.52±.05|.54±.05|.57±.09|.57±.12 .63±.17 .62±.22|
|REVE|.63±.11 .62±.19|.59±.13|.58±.17|.61±.13|.58±.19 .63±.16 .60±.24|



**Table 32:** Channel-permutation setting performance on ADFD. 

||AUROC|A|cc|F1|F2|
|---|---|---|---|---|---|
|Model|shufe origin|shufe|origin|shufe origin|shufe origin|
|BrainBERT|.62±.05 .59±.05|.64±.01|.58±.05|.66±.02 .60±.11|.64±.04 .64±.15|
|BrainWave|.62±.12 .74±.05|.57±.09|.68±.05|.49±.26 .68±.10|.47±.31 .73±.10|
|BrainOmni|.80±.07 .80±.07|.71±.04|.71±.04|.73±.05 .73±.05|.72±.09 .72±.09|
|CBraMod|.51±.02 .55±.06|.52±.07|.59±.04|.32±.26 .41±.20|.28±.25 .37±.20|
|EEGPT|.79±.04 .81±.05|.72±.04|.72±.05|.72±.05 .73±.05|.68±.07 .70±.07|
|MBrain|.52±.13 .53±.12|.51±.09|.50±.10|.54±.12 .53±.12|.54±.15 .52±.14|
|NeuroGPT-E|.49±.05 .51±.03|.55±.01|.55±.01|.71±.01 .71±.01|.85±.01 .85±.01|
|REVE|.79±.08 .84±.07|.68±.07|.77±.08|.74±.05 .79±.07|.79±.07 .79±.09|



### **G Additional Frequency Analysis Results** 

This appendix provides detailed results supporting the frequencyband analysis described in Section 3.3.4. We report the full quantitative outcomes of the band-wise PSD prediction experiments. Tables 36 to 38 reports the band-wise prediction performance for all evaluated models across the six canonical frequency bands. For each band _𝑏_ , we list the correlation between the ground-truth PS and the predicted PSD, as well as the normalized relative strength _𝑟_<sup>_𝑛_</sup> _𝑏_<sup>used in the main analysis.</sup> 

**Table 33:** Channel-permutation setting performance on CHBMIT. 

||AUROC|A|cc|F|1<br>F2|
|---|---|---|---|---|---|
|Model|shufe origin|shufe|origin|shufe|origin shufe origin|
|BrainBERT|.79±.04 .78±.06|.80±.04|.75±.10|.59±.08|.58±.08 .59±.11 .61±.09|
|BrainWave|.59±.14 .90±.03|.63±.09|.80±.12|.30±.11|.71±.09 .32±.15 .78±.04|
|BrainOmni|.74±.13 .74±.13|.67±.19|.67±.19|.51±.12|.51±.12 .56±.12 .56±.12|
|CBraMod|.67±.12 .69±.04|.67±.11|.70±.08|.42±.16|.46±.08 .48±.23 .49±.14|
|EEGPT|.69±.13 .71±.09|.73±.10|.67±.11|.47±.16|.46±.06 .48±.19 .51±.15|
|MBrain|.70±.08 .71±.03|.77±.03|.73±.06|.22±.22|.31±.15 .17±.18 .28±.20|
|NeuroGPT-E|.65±.07 .78±.12|.70±.06|.75±.07|.26±.10|.51±.22 .24±.14 .63±.16|
|REVE|.78±.12 .84±.10|.59±.25|.78±.12|.53±.18|.63±.14 .65±.12 .66±.13|



**Table 34:** Channel-permutation setting performance on UCSD-ON. 

||AUROC|A|cc|F|1<br>F2|
|---|---|---|---|---|---|
|Model|shufe origin|shufe|origin|shufe|origin shufe origin|
|BrainBERT|.50±.09 .51±.05|.49±.05|.51±.06|.57±.04|.51±.11 .64±.06 .54±.17|
|BrainWave|.50±.11 .69±.10|.49±.12|.53±.08|.40±.28|.60±.06 .43±.31 .69±.14|
|BrainOmni|.51±.19 .64±.09|.46±.15|.57±.06|.44±.21|.54±.16 .46±.26 .57±.26|
|CBraMod|.59±.08 .60±.12|.51±.07|.49±.08|.21±.29|.18±.08 .22±.35 .13±.07|
|EEGPT|.63±.17 .51±.21|.55±.14|.48±.17|.49±.16|.49±.15 .46±.16 .49±.14|
|MBrain|.43±.16 .49±.15|.46±.06|.46±.14|.49±.21|.37±.17 .56±.28 .34±.18|
|NeuroGPT-E|.55±.25 .56±.10|.53±.10|.53±.07|.51±.25|.58±.10 .57±.34 .64±.13|
|REVE|.58±.12 .63±.19|.58±.06|.56±.13|.53±.17|.45±.29 .53±.25 .46±.33|



**Table 36:** Band-wise PSD predictability across BFMs on ADFD and Dep-122, reporting normalized band predictability _𝑟𝑏_<sup>_𝑛_for delta (d),</sup> theta (t), alpha (a), beta (b), low gamma (gl), and high gamma (gh). 

||||AD|FD|||||Dep|-122|||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Model|_𝑟_<sup>_𝑛_</sup><br>_𝑑_|_𝑟_<sup>_𝑛_</sup><br>_𝑡_|_𝑟_<sup>_𝑛_</sup><br>_𝑎_|_𝑟_<sup>_𝑛_</sup><br>_𝑏_|_𝑟_<sup>_𝑛_</sup><br>_𝑔𝑙_|_𝑟_<sup>_𝑛_</sup><br>_𝑔ℎ_|_𝑟_<sup>_𝑛_</sup><br>_𝑑_|_𝑟_<sup>_𝑛_</sup><br>_𝑡_|_𝑟_<sup>_𝑛_</sup><br>_𝑎_|_𝑟_<sup>_𝑛_</sup><br>_𝑏_|_𝑟_<sup>_𝑛_</sup><br>_𝑔𝑙_|_𝑟_<sup>_𝑛_</sup><br>_𝑔ℎ_|
|REVE|.85|.00|.71|.11|.59|1.0|.99|.00|1.0|.92|.78|.65|
|EEGPT|1.0|.32|.36|.20|.92|.00|.80|.67|1.0|.67|.13|.00|
|BrainOmni|.95|.00|.82|.02|.28|1.0|.83|.39|1.0|.81|.35|.00|
|BrainWave|.63|.35|.77|.00|.14|1.0|1.0|.47|.75|.23|.00|.28|
|LaBraM|.08|.00|1.0|.26|.28|.10|.77|.36|1.0|.55|.15|.00|
|BrainBERT|.69|.08|.16|.00|.68|1.0|.70|.44|1.0|.00|.27|.87|
|BFM|.89|.00|.33|.09|.27|1.0|.89|1.0|.99|.76|1.0|.71|
|BIOT|.87|.00|.62|.31|.37|1.0|.80|.38|1.0|.75|.17|.00|
|CBraMod|.84|.00|.67|.55|.64|1.0|.91|.00|1.0|.86|.47|.05|
|MBrain|.87|.00|.42|.15|.40|1.0|.98|.00|1.0|.87|.87|.61|
|SppEEGNet|.26|.10|.00|.02|.27|1.0|1.0|.55|.94|.27|.00|.08|
|NeuroLM|.66|.89|.51|.08|.00|1.0|1.0|.36|.35|.00|.20|.05|
|NeuroGPT-E|.85|.13|.00|.01|.06|1.0|.52|.39|1.0|.00|.06|.10|
|Bendr|.74|.28|.00|.10|.07|1.0|1.0|.28|.79|.44|.00|.03|
|Brant|.53|.33|.17|.08|.00|1.0|.00|.68|.33|.43|.93|1.0|
|NeuroGPT-D|.95|.23|.25|.10|.00|1.0|1.0|.30|.86|.62|.11|.00|



Shen et al. 

**Table 37:** Band-wise PSD predictability on SD-8 and MDD-64. 

||||SD|-28|||||MD|D-64|||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Model|_𝑟_<sup>_𝑛_</sup><br>_𝑑_|_𝑟_<sup>_𝑛_</sup><br>_𝑡_|_𝑟_<sup>_𝑛_</sup><br>_𝑎_|_𝑟_<sup>_𝑛_</sup><br>_𝑏_|_𝑟_<sup>_𝑛_</sup><br>_𝑔𝑙_|_𝑟_<sup>_𝑛_</sup><br>_𝑔ℎ_|_𝑟_<sup>_𝑛_</sup><br>_𝑑_|_𝑟_<sup>_𝑛_</sup><br>_𝑡_|_𝑟_<sup>_𝑛_</sup><br>_𝑎_|_𝑟_<sup>_𝑛_</sup><br>_𝑏_|_𝑟_<sup>_𝑛_</sup><br>_𝑔𝑙_|_𝑟_<sup>_𝑛_</sup><br>_𝑔ℎ_|
|BrainWave|.95|.64|1.0|.75|.00|.22|.89|1.0|.89|.61|.00|.02|
|REVE|1.0|.00|.97|.66|.67|.22|.96|1.0|.99|1.0|.93|.00|
|NeuroGPT-E|1.0|.87|.06|.00|.41|.90|.25|1.0|.00|.62|.60|.08|
|BrainBERT|.82|.15|1.0|.00|.13|.29|.75|1.0|.73|.70|.80|.00|
|BrainOmni|.86|.46|1.0|.71|.27|.00|.66|.84|1.0|.99|.74|.00|
|BFM|.92|.00|1.0|.84|.90|.84|.86|1.0|.97|.97|.97|.00|
|MBrain|1.0|.00|1.0|.94|.83|.69|.94|.96|.96|1.0|.92|.00|
|EEGPT|.91|.66|1.0|.97|.38|.00|.89|.97|1.0|.89|.74|.00|
|BIOT|.68|.00|1.0|.58|.65|.19|.93|.97|1.0|.99|.86|.00|
|NeuroGPT-D|1.0|.00|.76|.67|.36|.14|.92|1.0|.98|.71|.67|.00|
|CBraMod|1.0|.25|.90|.89|.58|.00|.95|.96|.98|1.0|.90|.00|
|LaBraM|.87|.44|1.0|.70|.34|.00|.59|.86|.59|1.0|.76|.00|
|Brant|.64|.00|1.0|.71|.61|.54|.84|.87|.89|1.0|.93|.00|
|Bendr|1.0|.34|.53|.51|.01|.00|.73|1.0|.48|.49|.46|.00|
|SppEEGNet|1.0|.16|.68|.29|.00|.02|1.0|.84|.78|.63|.51|.00|
|NeuroLM|1.0|.31|.81|.31|.00|.24|.59|.86|.59|1.0|.76|.00|



**Table 39:** LaBraM codebook analysis on ADFD, CHBMIT, and SD28. We compare standard finetuning without codebook (Origin) and codebook-enabled finetuning (CB) under identical protocols, reporting AUROC, Accuracy, F1, and F2. 

||AUR|OC|A|cc|F|1|F|2|
|---|---|---|---|---|---|---|---|---|
|Dataset|CB|origin|CB|origin|CB|origin|CB|origin|
|ADFD|.65±.06|.77±.10|.62±.05|.72±.08|.68±.03|.75±.06|.70±.03|.75±.06|
|CHBMIT|.77±.06|.78±.07|.75±.04|.75±.06|.60±.10|.54±.24|.55±.7|.53±.16|
|SD-28|.47±.12|.54±.07|.50±.09|.54±.04|.56±.12|.59±.07|.60±.15|.59±.13|



**Table 40:** LaBraM codebook analysis on SleepEDF, reporting Accuracy, AUROC (OvR), macro-F1 (MF1), and Cohen’s _𝜅_ . 

|AUROC|A|cc|M|F1|Kap|pa|
|---|---|---|---|---|---|---|
|CB<br>origin|CB|origin|CB|origin|CB|origin|
|.86±.02 .93±.01|.66±.04|.76±.04|.61±.03|.68±.03|.54±.05|.67±.05|



**Table 38:** Band-wise PSD predictability across BFMs on ADHD. 

|||AD|HD|-Ad|ult|||A|DHD|-Ch|ild||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Model|_𝑟_<sup>_𝑛_</sup><br>_𝑑_|_𝑟_<sup>_𝑛_</sup><br>_𝑡_|_𝑟_<sup>_𝑛_</sup><br>_𝑎_|_𝑟_<sup>_𝑛_</sup><br>_𝑏_|_𝑟_<sup>_𝑛_</sup><br>_𝑔𝑙_|<sup>_𝑟𝑛_</sup><br>_𝑔ℎ_|_𝑟_<sup>_𝑛_</sup><br>_𝑑_|_𝑟_<sup>_𝑛_</sup><br>_𝑡_|_𝑟_<sup>_𝑛_</sup><br>_𝑎_|_𝑟_<sup>_𝑛_</sup><br>_𝑏_|_𝑟_<sup>_𝑛_</sup><br>_𝑔𝑙_|<sup>_𝑟𝑛_</sup><br>_𝑔ℎ_|
|EEGPT|.66|.00|.59|1.0|.18|.08|.95|.82|1.0|1.0|.56|.00|
|BrainOmni|.65|.00|.67|1.0|.32|.14|1.0|.86|.99|.84|.39|.00|
|BrainWave|.32|.00|.68|1.0|.80|.82|.83|.59|.94|1.0|.34|.00|
|BIOT|.40|.00|.40|1.0|.58|.17|.98|.89|1.0|.78|.32|.00|
|REVE|.71|.00|.25|1.0|.53|.30|.96|.82|.98|1.0|.62|.00|
|MBrain|.66|.00|.55|1.0|.53|.16|1.0|.87|.98|1.0|.60|.00|
|Brant|.71|.00|.33|1.0|.32|.08|.89|.58|.68|1.0|.59|.00|
|CBraMod|.65|.19|.61|1.0|.52|.00|.99|.86|.94|1.0|.79|.00|
|LaBraM|.76|.39|.71|1.0|.08|.00|1.0|.86|.96|.92|.41|.00|
|NeuroGPT-E|.39|.74|.00|1.0|.40|.15|.84|1.0|.75|.37|.00|.44|
|NeuroGPT-D|.95|.00|.71|1.0|.16|.03|1.0|.70|.83|.77|.34|.00|
|BFM|.61|.00|.45|1.0|.70|.62|.96|.83|.94|1.0|.67|.00|
|NeuroLM|.41|.00|.55|1.0|.29|.19|1.0|.82|.97|.88|.27|.00|
|BrainBERT|1.0|.26|.91|.84|.13|.00|1.0|.64|.82|.66|.60|.00|
|SppEEGNet|1.0|.06|.72|.61|.06|.00|1.0|.80|.70|.64|.31|.00|
|Bendr|1.0|.16|.73|.78|.03|.00|1.0|.62|.83|.57|.20|.00|



### **H Additional Codebook Analysis Results** 

This section complements the codebook analysis discussed of LaBraM in Section 3.3.5. LaBraM adopts a discrete codebook during pretraining. However, in its standard downstream finetuning protocol, it finetunes the encoder and task head while keeping the codebook unused (i.e., finetuning is performed on continuous embeddings). To isolate the effect of reusing discretization at finetuning time, we additionally evaluate a variant that enables codebook-based finetuning (CB) and compare it against the standard setting (origin) on four representative datasets, with all other settings held fixed. Table 40 reports full results for both variants. LaBraM codebook analysis on ADFD, CHBMIT, SleepEDF, and SD-28. We report AUROC, Accuracy, F1, and F2 for the binary datasets, and AUROC (OvR), Accuracy, MF1, and Cohen’s _𝜅_ for SleepEDF. 

