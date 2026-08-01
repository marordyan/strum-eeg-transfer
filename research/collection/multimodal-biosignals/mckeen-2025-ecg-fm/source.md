_JAMIA Open_ , 2025, **8(5)** , ooaf122 https://doi.org/10.1093/jamiaopen/ooaf122 **Research and Applications** 



## Research and Applications 

# **ECG-FM: an open electrocardiogram foundation model** 

### **Kaden McKeen , HBSc**<sup>�</sup><sup>**,1,2,3,4,5**</sup> **, Sameer Masood, MPH**<sup>**1,6**</sup> **, Augustin Toma, MD**<sup>**4,7**</sup> **, Barry Rubin, MD CM**<sup>**1,2,3**</sup> **, Bo Wang, PhD**<sup>**1,2,3,4,5,7,8**</sup> 

1Toronto General Hospital Research Institute, University Health Network, Toronto, M5G 2C4, Canada, 2Peter Munk Cardiac Centre, University Health Network, Toronto, M5G 2N2, Canada,<sup>3</sup> UHN AI Hub, University Health Network, Toronto, M5G 2C4, Canada,<sup>4</sup> Vector Institute for Artificial Intelligence, Toronto, M5G 0C6, Canada,<sup>5</sup> Department of Laboratory Medicine and Pathobiology, University of Toronto, Toronto, M5S 3K3, Canada,<sup>6</sup> Department of Medicine, University of Toronto, Toronto, M5S 3H2, Canada,<sup>7</sup> Department of Medical Biophysics, University of Toronto, Toronto, M5G 2C4, Canada,<sup>8</sup> Department of Computer Science, University of Toronto, Toronto, M5S 2E4, Canada 

�Corresponding author: Kaden McKeen, HBSc, Laboratory Medicine and Pathobiology, University of Toronto, 140 McCaul Street, Toronto, ON M5T 1W2, Canada (kaden.mckeen@mail.utoronto.ca) 

#### **Abstract** 

**Objectives:** To develop ECG-FM, an open-weight foundation model for electrocardiogram (ECG) analysis, rigorously evaluate its performance on clinically salient tasks, and openly release it alongside a public benchmark. 

**Materials and Methods:** In a study using 1.5 million 12-lead ECGs, we present ECG-FM, a transformer-based foundation model pretrained with hybrid self-supervision that combines masked reconstruction and contrastive learning with ECG-specific augmentation. Downstream, we evaluate multi-label ECG interpretation and prediction of reduced left ventricular ejection fraction (LVEF), introducing an openly available benchmark on the MIMIC-IV-ECG dataset. We assess ECG-FM’s capabilities through data scaling experiments, latent-space structure analysis, and attention-based saliency. 

**Results:** Finetuned ECG-FM models outperform task-specific baselines in the small-to-medium-scale data regime, exhibit strong label efficiency and cross-dataset generalizability, and achieve high AUROC on salient labels, including atrial fibrillation (0.996) and LVEF ≤ 40% (0.929). The pretrained encoder showcases competitive linear probing performance, with functionally discriminative embeddings. 

**Discussion:** Findings indicate that ECG-FM is generalizable, label-efficient, and discriminative for screening, risk stratification, and monitoring. Its representations capture low-level morphology and high-order cardiac semantics, and the pretrained encoder serves as a robust feature-set generator. This work mitigates reliance on large labeled datasets, reduces compute and data requirements, and lowers barriers to reproducibility and cross-study comparison. 

**Conclusion:** ECG-FM is an open, rigorously validated ECG foundation model intended to accelerate transparent, comparable research in the ECG analysis subfield. It is designed for rapid integration and evaluation, especially for delivering practical gains in low-label settings. We release our code, model weights, tutorials, and benchmark at https://github.com/bowang-lab/ECG-FM/. 

#### **Lay Summary** 

An electrocardiogram (ECG) is a quick, low-cost recording of the heart’s electrical activity. Artificial intelligence (AI) can help interpret ECGs, but most tools rely on large expert-labeled datasets. Foundation models address this by first learning ECG structure from many unlabeled recordings through pretraining, then adapting to new tasks while needing fewer labels. We present ECG-FM, a foundation model for ECG analysis, and evaluate it on practical tasks: interpreting common ECG findings and predicting reduced left ventricular ejection fraction, a measure of how well the heart pumps blood. ECG-FM requires little labeled data and its capabilities transfer well to UHN-ECG, an institutional cohort held out from pretraining. To support comparability and usage, we release ECG-FM alongside a public benchmarking task so others can evaluate, adapt, and improve upon our work. For patients and communities, this may enable faster, more consistent ECG interpretation for screening, risk stratification, and monitoring. For clinicians and researchers, it lowers the time and cost to build, test, integrate, and improve ECG tools, especially in resource-constrained settings. 

**Key words:** foundation model; electrocardiography; self-supervised learning; deep learning; time series analysis. 

### **Introduction** 

AI-based ECG analysis methods have outperformed traditional computerized interpretation,<sup>1–3</sup> even matching or exceeding human performance.<sup>4–6</sup> Recent technological advancements and growing large, publicly available datasets have seen conventional task-specific models replaced by foundation models due to their high performance and reduced reliance on costly labeled data. 

Through self-supervised learning (SSL), foundation models are pretrained to encode ECG structure and semantics, then finetuned on downstream tasks with fewer labeled examples. SSL techniques fall into generative or contrastive categories, each with distinct strengths and limitations. Generative methods reconstruct signals from masked inputs,<sup>7–9</sup> capturing local structural patterns but potentially underrepresenting high-level cardiac semantics.<sup>10</sup> Contrastive approaches learn 

**Received:** August 29, 2025; **Revised:** September 16, 2025; **Accepted:** September 26, 2025 

© The Author(s) 2025. Published by Oxford University Press on behalf of the American Medical Informatics Association. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (https://creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited. 

_JAMIA Open_ , 2025, Vol. 8, No. 5 

discriminative representations from augmented ECG samples,<sup>11–13</sup> but risk faulty alignment, wherein augmentations degrade physiologically significant patterns.<sup>9,14</sup> Hybrid SSL techniques combine both approaches<sup>15,16</sup> to capture lowlevel patterns while preserving semantic information, though augmentation-based strategies remain vulnerable to faulty alignment. 

Oh et al<sup>16</sup> proposed a hybrid approach that circumvents faulty alignment and is based on well-established SSL objectives. They adopted the transformer-based model and generative masking objective from wav2vec 2.0,<sup>17</sup> as well as the Contrastive Multi-Segment Coding (CMSC) objective, originally introduced in Contrastive Learning of Cardiac Signals (CLOCS).<sup>11</sup> CMSC treats temporally adjacent ECG segments as positive pairs, exploiting the relative stability of cardiac function over short intervals and eliminating the need for augmentation altogether. Oh et al<sup>16</sup> also introduced Random Lead Masking (RLM), an ECG-specific augmentation wherein leads are stochastically masked, and demonstrated that by exposing the model to diverse lead combinations during pretraining, their model can be finetuned using arbitrary reduced lead sets of the standard 12-lead ECG.<sup>16</sup> This leads to a flexible model which prioritizes both low-level patterns and high-level semantic information, while also addressing common drawbacks associated with SSL approaches. 

Progress in the ECG analysis field is slowed by unshared weights which hinder reproducibility and comparability. Even when code is released, training modern SSL approaches is often cost-prohibitive. While patient privacy can preclude model release, the availability of large public ECG datasets now makes competitive open-weight pretraining feasible, shifting the barrier from data access to responsible model development and evaluation. 

In this study, we present ECG-FM, a transformer-based ECG foundation model pretrained on 1.4 million ECG segments using a hybrid self-supervised objective. ECG-FM is validated on multi-label interpretation and reduced LVEF prediction tasks, demonstrating strong performance, labelefficiency, and generalization. To lower entry costs and enable comparison, we release the weights, code, tutorials, and a public benchmark. 

### **Methods** 

#### Data 

We collected 1.5 million standard 12-lead ECGs from the UHN-ECG, PhysioNet 2021,<sup>18–20</sup> and MIMIC-IV-ECG<sup>20,21</sup> datasets. Specifically, we include 6 datasets in PhysioNet 2021: CPSC, CPSC-Extra, PTB-XL, Georgia, Ningbo, and Chapman. The PTB and St Petersburg INCART datasets are excluded due to having few long samples with inconsistent sampling rates. The MIMIC-IV-ECG v1.0 database contains many 10 s ECGs collected from the Beth Israel Deaconess Medical Center. PhysioNet 2021 and MIMIC-IV-ECG are 2 public data sources used for our pretraining dataset, while UHN-ECG is external to pretraining; we evaluate solely on UHN for downstream tasks, providing evidence of crossdataset generalization to an institutional cohort. 

##### **UHN-ECG** 

UHN-ECG is a newly assembled private, institutional dataset containing 622k ECG recordings from 211k patients who were seen in the emergency department and/or admitted to 

hospital between January 2010 and December 2018. This 9-year dataset was collected at Toronto General Hospital and Toronto Western Hospital, 2 acute care hospitals with emergency departments, cardiology wards, and coronary care units. These exist as part of the University Health Network (UHN), a network of academic hospitals located in Toronto, Canada. All recordings are 10 s, where 88.8% have an original sampling frequency of 500 Hz and the remaining have 250 Hz. Every ECG has a cardiologist over-read and there are several associated clinical reports and auxiliary data modalities which make for excellent label availability. We report split- and task-specific age and sex in respective Tables S2 and S3. Although 12.8% of ECGs were labeled with poor data quality, we noticed interpretation may be attempted regardless; therefore, we opted to retain these samples and produce a model more tolerant of real-world artifacts. 

##### **ECG preprocessing** 

We extracted raw waveforms and tabularized ECG metadata, including sample rates, sample size, and patient demographic information wherever available. We resampled the waveforms at 500 Hz using linear interpolation, performed z-score normalization, and segmented the signals into nonoverlapping 5 s segments to produce the model inputs. 

#### Cohort curation 

As seen in Figure 1, we removed ECGs with null values or constant-valued leads. To maintain representative distributions and avoid selection bias, no additional exclusions were applied. Each dataset was stratified into 80%/10%/10% splits for training, validation, and testing. UHN-ECG was stratified by patient and temporally to prevent overlap across splits, avoiding label leakage and enabling prospective-like evaluation (see Figure S1). MIMIC-IV-ECG was split by patient only due to imprecise acquisition dates. PhysioNet 2021 was randomly split, with evaluative sets unused. UHNECG was excluded from pretraining to respect patient privacy and evaluate cross-dataset generalizability. 

#### Model architecture 

ECG-FM has 90.9 million parameters and uses the wav2vec 2.0 architecture,<sup>17</sup> consisting of a multi-layer CNN feature extractor and BERT-like transformer encoder. The feature extractor embeds raw signal portions into latent representations **z** _t_ , which feed a transformer encoder to create contextualized representations **c** _t_ . 

The feature encoder contains 4 blocks, each with a convolutional layer (256 channels, stride 2, kernel length 2), layer normalization, and a GELU activation. Relative positional embeddings are added to the latent representations. The transformer encoder follows BERT-Base, having 12 layers, 768 embedding dimensions, 12 attention heads, and 3072 feed-forward dimensions. 

#### Pretraining method 

We build upon the work of Oh et al,<sup>16</sup> adopting their pretraining method and engaging in open-source collaboration (https:// github.com/Jwoo5/fairseq-signals/). As seen in Figure 2, this hybrid self-supervised approach combines wav2vec 2.0’s continuous signal masking,<sup>17</sup> CLOCS’s contrastive CMSC objective,<sup>11</sup> and RLM augmentation.<sup>16</sup> Previously termed W2VþCMSCþRLM, we refer to this method as WCR. 

_JAMIA Open_ , 2025, Vol. 8, No. 5 **3** 



**Figure 1.** Cohort and sample selection. This flow diagram shows the data sources and ECG exclusion criteria, as well as the dataset partitioning. The pretraining cohort combines samples from public datasets PhysioNet2021 and MIMIC-IV-ECG. Downstream task cohorts utilize MIMIC-IV-ECG and UHNECG datasets, where the reduced LVEF task undergoes filtering according to task-specific label availability. 



**Figure 2.** Framework illustration. Raw waveforms are inputted and individual leads are randomly masked. A convolutional feature encoder generates latent representations that feed into a transformer encoder, producing local representations that are then average-pooled to create global representations. Latent representations are randomly masked in spans as _m_ , and are quantized to _q_ . We then apply a local contrastive loss attracting each _q_ to its corresponding local representation, using a subset of other _q_ as the negative samples, or distractors. A batch of 4 ECG inputs, making up 2 positive pairs of temporally-adjacent ECG segments, are shown to visualize the CMSC global contrastive loss acting on the global representations across samples. Positive and negative contrastive learning pair relationships are depicted using blue and red arrows, respectively. 

_JAMIA Open_ , 2025, Vol. 8, No. 5 

**4** 

##### **wav2vec 2.0** 

Inspired by masked language modeling, wav2vec 2.0 masks spans of CNN latent representations **z** _t_ . Each token has 6.5% probability of being a starting index; if selected, we mask 10 subsequent tokens, resulting in approximately 49% masked tokens. We quantize **z** _t_ to **q** _t_ using 2 trainable codebooks of 320 codes to remove artifacts that may otherwise trivialize the task.<sup>17</sup> A contrastive loss maximizes cosine similarity between quantized target **q** _t_ and corresponding contextualized representation **c** _t_ , while minimizing similarity with dis~ tractors **q** � **Q** _t_ sampled from all masked token targets **Q** _t_ . 

##### **CMSC** 

CMSC applies contrastive learning between global representations, treating temporally adjacent ECG segments as positive pairs.<sup>11</sup> This augmentation-free strategy avoids faulty alignment while encouraging consistent representations between consecutive segments, promoting temporal invariance and capturing functionally relevant information over superficial differences. 

##### **RLM** 

RLM masks each lead with probability _P_ ¼ 0 _:_ 5, enhancing robustness through diverse lead combinations during pretraining.<sup>16</sup> Although not explored in this work, RLM enables finetuning on arbitrary lead subsets, making ECG-FM applicable in contexts where only reduced 12-lead sets are available. 

#### Downstream tasks 

To demonstrate that ECG-FM is useful for a variety of downstream applications, we selected several classification tasks for our evaluation. For each task, we report split-specific outcome prevalence in Table S4 and show receiver operating characteristic (ROC) curves and the precision-recall curves (PRC) for each label in our _Full_ , _Random Init._ , and _Linear_ experiment suites, reporting the label names in the legend. 

##### **UHN-ECG interpretation** 

As primary readers, cardiologists demonstrate greater interpretation accuracy and less interobserver variability compared to physicians with less specialized training.<sup>22,23</sup> In the UHN-ECG dataset, each ECG is accompanied by a cardiologist’s interpretation, provided as an over-read of an automated analysis. We extracted binary labels from these free-text expert interpretations using a knowledge graph and text-parsing system. Further details can be found in Section S1.1. 

##### **MIMIC-IV-ECG machine reads** 

MIMIC-IV-ECG utilizes machine measurements to automatically generate ECG reports. For this task, we generate our labels from these reports using the same text-parsing system as with the UHN-ECG interpretation task, adjusting the patterns to accommodate dataset-specific terminology. We focused on all the same labels as in the UHN-ECG interpretation task, given they were available. Our conversion of free-text interpretations into binary labels culminates in an accessible benchmark task. 

##### **UHN-ECG reduced LVEF** 

Heart failure is a major contributor of morbidity and mortality worldwide, with approximately 50% of cases being heart failure with reduced ejection fraction (HFrEF).<sup>24</sup> The heightened risk of mortality associated with HFrEF, even in 

asymptomatic cases, underscores the significance of early detection for timely intervention.<sup>25,26</sup> We predict low, or reduced, LVEF as a step towards early screening for left ventricular systolic dysfunction and HFrEF. Using regex to extract LVEF percentages from echocardiography reports, we generated labels at various common LVEF thresholds: ≤ 50%, ≤ 40%, ≤ 35%, and ≤ 30%. We paired each ECG with its closest associated echocardiography report which indicates an LVEF percentage, taking only those ECG samples with a valid report within ±7 days of acquisition. 

#### Experiments 

The ECG-FM model was pretrained on 1 405 625 samples using 3 A100 80GB GPUs applying distributed data parallelism. The 1026 batch size was composed of 171 positive pairs, each consisting of 2 segments, distributed across the 3 GPUs. A fixed learning rate schedule was used, where it was initially set at 1 × 10<sup>_−_4</sup> for the first 5 epochs, reduced to 8 × 10<sup>_−_5</sup> from epoch 6 to 200, and further decreased to 5 × 10<sup>_−_5</sup> for epochs 201 to 240. Training concluded after 240 epochs, totaling a computational wall time of 9.51 days. We do not perform ablation studies on WCR, as these have been performed previously by Oh et al.<sup>16</sup> 

We ran several suites of ECG-FM multi-label classification experiments for each downstream task. Loss balancing was applied using weights inversely proportional to the outcome prevalence. We initialized our _Full_ models with the pretrained weights and performed full finetuning, wherein all model weights are updated, using a learning rate of 1 × 10<sup>_−_6</sup> . For _Random Init._ , we randomly initialized the models and then performed full finetuning with a learning rate of 1 × 10<sup>_−_5</sup> . To maintain a fair comparison, the weight initialization and learning rates were the only experimental differences between the _Full_ and _Random Init._ experiments. In the _Linear_ experiment, we performed linear probing with learning rate 1 × 10<sup>_−_5</sup> . For this frozen evaluation, pretrained model embeddings are extracted and fed as inputs to a single linear layer to generate predictions. 

We also employed 2 competitive, task-specific baseline models: The _Nejedly_ baseline is a ResNet with multi-head attention which follows the configuration seen in Nejedly et al<sup>27</sup> ; the _SE-WRN_ baseline implementation is similar to that of Han et al.<sup>28</sup> Each is trained with a learning rate of 1 × 10<sup>_−_4</sup> . 

Data scaling experiments were performed by taking a percentage subset of ECGs in the training set while maintaining the same evaluative sets. We ran experiments on 50%, 10%, and 1% of the training set ECGs for the interpretation tasks, as well as 50% and 10% for the reduced LVEF task. 

All downstream tasks ran on a single A100 80GB GPU using a batch size of 256. Experiments used the Adam optimizer<sup>29</sup> with _β_ 1 ¼ 0 _:_ 9, _β_ 2 ¼ 0 _:_ 98. Checkpoints were selected according to which had the best AUPRC on the validation set. Thresholds were computed to achieve target recall values on the validation set. Aside from the aggregated results shown in Table S5, all evaluative metrics are computed by randomly sampling a single segment per ECG. 

We mitigate class imbalance by applying a per-label positive-class reweighting scheme during finetuning using a standard pos ~~w~~ eightk¼ NNneposg _<u>;;</u>_ kk<sup>per label</sup><sup>_k_, as computed from</sup> the training split sample counts. We report Area Under the 

_JAMIA Open_ , 2025, Vol. 8, No. 5 **5** 

Precision-Recall-Gain curve (AUPRG)<sup>30</sup> to support prevalence-robust evaluation (see Section S1.3). 

### **Results** 

#### Data scaling 

##### **Pretraining benefits** 

The _Linear_ results in Figure 3 demonstrate that our pretrained model embeddings encode rich, task-relevant information. The _Random Init._ performance is relatively poor with few training samples, confirming that ECG-FM’s pretraining is responsible for its superior data efficiency. At the smallest training set sizes, _Linear_ outperforms the baselines and performs comparably to _Full_ in the MIMIC-IV-ECG machine reads and UHN-ECG reduced LVEF tasks; however, its performance plateaus because it lacks the representational capacity necessary to exploit additional downstream data. Although task-dependent, this indicates that the benefits of WCR pretraining are quite significant in smaller data regimes and transfer well to unseen task-specific datasets. 

##### **Downstream performance** 

Across all tasks, _Full_ outperforms the baselines given approximately 100 000 training samples. However, for the UHN- 

ECG interpretation and MIMIC-IV-ECG machine reads tasks, the _Full_ and baseline model performances trend to a similar plateau. ECG-FM tends to outperform strong taskspecific models on downstream tasks, especially in the smallto-medium-scale data regime; however, it may not provide significant value downstream given sufficiently large taskspecific datasets. 

#### Latent space analysis 

The UMAP visualization of the UHN-ECG dataset in Figure 4 highlights ECG-FM’s ability to encode relationships in rhythm, heart rate, and pathology for an unseen dataset. This latent space depicts our pretrained model—which has never been trained on any labels—making the label overlay strictly evaluative. Additional label-specific UMAP views are provided in Figure S2. 

A distinct _Normal sinus rhythm_ cluster sits within a broader _Sinus rhythm_ region, with _Bradycardia_ and _Tachycardia_ samples forming its extremities and encoding heart rate along the vertical axis. Non-sinus tachycardias like _Atrial fibrillation_ and _Atrial flutter_ occupy a separate upper region, while conduction defects, such as the bundle branch blocks, cluster more centrally. This spatial arrangement, along with the close proximity of related tachycardias, suggests ECG- 



**Figure 3.** Data scaling results. Label-averaged AUPRC across experiment suites and training dataset sizes for all tasks. 

**6** _JAMIA Open_ , 2025, Vol. 8, No. 5 



**Figure 4.** Pretrained latent space UMAP. A UMAP visualization of pretrained ECG-FM global representations from ECGs in the UHN-ECG dataset. An additive color scheme employs select labels from the UHN-ECG interpretation task to enable a latent space analysis, wherein some prioritization was performed to prevent label overlap from reducing readability. 

FM captures functional similarity. A pacemaker-positive evaluative subset revealed no performance drop for other labels despite the strong clustering of electronic pacemaker samples, indicating a robust encoding of diverse relationships beyond those visually evident in Figure 4. Overall, these observations highlight ECG-FM’s capacity to produce physiologically meaningful and functionally discriminative representations. 

##### **UHN-ECG reduced LVEF** 

Table S9 presents performances across all experiment suites, where our _Full_ experiment outperforms both baselines across all data scales and labels. It is unclear whether the performance gap between the baselines and _Full_ would similarly close, as with the other tasks, given greater task-specific data availability. We see an upwards trend in the _Full_ experiment performance which suggests that WCR pretraining would continue to provide benefit given a larger dataset. We report ROC and PRC curves in Figure S5. 

#### Downstream tasks 

##### **UHN-ECG interpretation** 

As evidenced in Table S7, we achieve strong performance across numerous labels using a cohort representative of real in-hospital populations. Our results demonstrate that ECG-FM is resilient even to low-quality recordings, with a considerable 12.4% of the test set labeled with _Poor data quality_ . Per-label AUPRG (see Section S1.3) is generally quite high across labels and confirms reliable performance even for extremely rare labels. We report ROC and PRC curves in Figure S3. 

##### **MIMIC-IV-ECG machine reads** 

To evaluate the quality of this task for benchmarking, we compare Tables S6 and S8 with labels shared with the UHNECG interpretation task. While AUPRC is often lower on this task than their UHN-ECG equivalent, re-expressing performance with AUPRG narrows cross-dataset differences and yields several labels with comparable performances. Residual discrepancies concentrate in labels whose annotation likely benefits from cardiologist adjudication, consistent with differences in label sourcing. This indicates that the machine read labels rely on patterns consistently recognizable by ECG-FM, supporting this task as a practical benchmark, while highlighting performance discrepancies that are plausibly attributable to label quality rather than model limitations. We report ROC and PRC curves in Figure S4. 

#### Saliency maps 

We generated attention-based saliency maps by extracting attention weights from the final transformer encoder selfattention layer, averaging across attention heads, and projecting these into the input space. The visualizations in Figure 5 serve as a heuristic for relative input importance. Our models consistently attend to relevant regions across cardiac cycles. For instance, in predicting _Ventricular pacing_ , attention focuses on pacing spikes—a hallmark of paced rhythms— indicating sensitivity to focal, clinically relevant patterns. This preferential attention suggests effective use of local contextual information for prediction. 

### **Discussion** 

We demonstrate strong performance of ECG-FM on clinically relevant tasks. The UHN-ECG interpretation experiment marks a step toward full, expert-level 12-lead interpretation, while the reduced LVEF task highlights ECGFM’s potential to inform rapid development of medical management plans. Evaluated in a simulated prospective setting that reflects representative in-hospital populations and tracing quality, these UHN-ECG tasks provide strong evidence for ECG-FM’s cross-dataset generalizability. 

Standard metrics can be misleading under class imbalance: Metrics like accuracy are dominated by the majority class and AUPRC shifts with outcome prevalence. The depressed 

_JAMIA Open_ , 2025, Vol. 8, No. 5 **7** 



**Figure 5.** Saliency maps. Distinct 5 s ECG segments colored using corresponding self-attention weight activations derived from pretrained, full-finetuned ECG-FM models. Red represents a higher relative activation. (A) UHN-ECG interpretation model activations for an ECG labeled with ventricular pacing (lead II); (B) UHN-ECG interpretation model activations for an ECG labeled with LBBB (lead V1); and (C) UHN-ECG reduced LVEF model activations for an ECG labeled with LVEF ≤ 30% (lead V3). 

AUPRC observed for rare outcomes partly reflects low positive rates rather than poor discrimination, as per-label AUPRG remains high in our prevalence-robust evaluation and better reflects model utility (Section S1.3).<sup>30</sup> Furthermore, this analysis indicates that performance primarily tracks ECG signature specificity and label ontology, offering a promising explanation for the lower relative performances of more composite labels _Myocardial infarction_ and _Poor data quality_ . 

Our data scaling experiments demonstrate rapid adaptability to downstream tasks and reduced reliance on labeled data. ECG-FM consistently outperforms conventional taskspecific methods in the small-to-medium-scale data regime, underscoring the benefit of WCR pretraining. The linear probing experiments confirm that the pretrained embeddings encode task-relevant information, suggesting that ECG-FM can act as a robust, competitive feature-set generator for diverse clinical applications. 

Our results suggest that ECG-FM commands local and global contextual information effectively. In our saliency maps, it displays relevant, preferential attention to the same regions across the cardiac cycle. Our latent space analysis exhibits pretrained embeddings which are functionally discriminative and indicative of ECG-FM’s ability to capture underlying cardiac function. Such explorations form a basis to demystify internal model workings and improve model interpretability. 

CMSC’s positive pair strategy requires 2 consecutive segments, necessitating ECG-FM accept 5 s ECG inputs rather than the full 10 s available in the MIMIC-IV-ECG and UHNECG datasets. Our labels are not segment-specific, creating an input-to-label mismatch in the case of focal patterns which are more present in 1 segment than its neighbor. We perform a segment-aware evaluation in Section S1.2 which significantly improves performance on select labels, showcasing that these effects are mitigable. As discussed in Section S1.3, one limitation is the label-space rigidity that results from predicting a fixed set of binary labels. We partially mitigate this with a curated knowledge graph that captures and aggregates condition subtypes (see Section S1.1); however, any captured nuance in clinician interpretation is then collapsed into composite labels which conflate heterogeneous phenotypes. Text-based methodology or hierarchical labeling may better capture such granularity in future work. Other promising 

avenues for extending this work include integration of ECG-FM into text-conditioned frameworks and multimodal foundation models as an ECG encoder. 

### **Conclusion** 

We present ECG-FM, an open-weight ECG foundation model pretrained using a hybrid SSL method and evaluate it across clinically salient tasks. Our results indicate that ECGFM is a robust, generalizable, and functionally discriminative model which performs strongly in low-label regimes, alleviating the need for large annotated datasets. By releasing the model, code, tutorials, and a public benchmark, we aim to accelerate transparent, comparable research and streamline practical adoption—especially where labeled data and compute are constrained. 

### **Author contributions** 

Kaden David Gougeon McKeen (Conceptualization, Data curation, Formal analysis, Investigation, Methodology, Software, Validation, Visualization, Writing—original draft, Writing—review & editing), Sameer Masood (Conceptualization, Data curation, Funding acquisition, Project administration, Resources, Supervision, Validation, Writing—review & editing), Augustin Toma (Conceptualization, Investigation, Validation, Writing—review & editing), Barry Rubin (Funding acquisition, Project administration, Resources, Supervision, Validation, Writing—review & editing), and Bo Wang (Investigation, Resources, Supervision, Validation, Writing— review & editing) 

### **Supplementary material** 

Supplementary material is available at _JAMIA Open_ online. 

### **Funding** 

This research received no specific grant from any funding agency in the public, commercial or not-for-profit sectors. 

### **Conflicts of interest** 

The authors have no competing interests to declare. 

_JAMIA Open_ , 2025, Vol. 8, No. 5 

**8** 

### **Data availability** 

PhysioNet 2021 v1.0.3 is available for public download (https://doi.org/10.13026/34va-7q14), as is MIMIC-IV-ECG v1.0 (https://doi.org/10.13026/4nqg-sb35). The UHN-ECG dataset is not available for public use. Model weights are available on our GitHub for our pretrained model and downstream MIMIC-IV-ECG machine reads models. Downstream UHN-ECG models cannot be made available due to privacy concerns. Code for data preprocessing, model training, model inference, and experiment reproduction is available, as are tutorial notebooks. Refer to https://github.com/bowang-lab/ ECG-FM/. 

### **References** 

- 0 1. Herman R, Demolder A, Vavrik B, et al. Validation of an automated artificial intelligence system for 12-lead ECG interpretation. _J Electrocardiol._ 2024;82:147-154. 

- 0 2. Rafie N, Kashou AH, Noseworthy PA. ECG interpretation: clinical relevance, challenges, and advances. _Hearts_ . 2021;2:505-513. 

- 0 3. Kadish AH, Buxton AE, Kennedy HL, et al.; International Society for Holter and Noninvasive Electrocardiology. ACC/AHA clinical competence statement on electrocardiography and ambulatory electrocardiography. _Circulation._ 2001;104:3169-3178. 

- 0 4. Choi YJ, Park MJ, Ko Y, et al. Artificial intelligence versus physicians on interpretation of printed ECG images: diagnostic performance of ST-elevation myocardial infarction on electrocardiography. _Int J Cardiol._ 2022;363:6-10. 

- 0 5. He B, Kwan AC, Cho JH, et al. Blinded, randomized trial of sonographer versus AI cardiac function assessment. _Nature._ 2023;616:520-524. 

- 0 6. Al-Zaiti SS, Martin-Gill C, Z�egre-Hemsey JK, et al. Machine learning for ECG diagnosis and risk stratification of occlusion myocardial infarction. _Nat Med._ 2023;29:1804-1813. 

- 0 7. Choi S, Mousavi S, Si P, Yhdego HG, Khadem F, Afghah F. ECGBERT: understanding hidden language of ECGs with self-supervised representation learning. _arXiv_ [Preprint]. 2023. arXiv:2306.06340. 

- 0 8. Vaid A, Jiang J, Sawant A, et al. A foundational vision transformer improves diagnostic performance for electrocardiograms. _NPJ Digit Med._ 2023;6:108. 

- 0 9. Na Y,  Park M, Tae Y, Joo S. Guiding masked representation learning to capture spatio-temporal relationship of electrocardiogram. In: Chaudhuri S, Fragkiadaki K, Khan ME, Sun Y, eds. _International Conference on Learning Representations (ICLR 2024)_ . ICLR Proceedings; 2024:Paper 5394. https://openreview. net/forum?id=WcOohbsF4H 

10. Liu Y, Zhang S, Chen J, Yu Z, Chen K, Lin D. Improving pixelbased MIM by reducing wasted modeling capability. In: Kosecka J, Ponce J, Schmid C, Zisserman A, eds. _Proceedings of the IEEE/ CVF International Conference on Computer Vision (ICCV)._ Piscataway, NJ: IEEE; 2023:5361-5372. 

11. Kiyasseh D, Zhu T, Clifton DA. CLOCS: contrastive learning of cardiac signals across space, time, and patients. In: Meila M and Zhang T, eds. _Proceedings of the 38th International Conference on Machine Learning_ . Vol 139. PMLR; 2021:5606-5615. 

12. ldele E, Ragab M, Chen Z, Wu M, Kwoh CK, Li  X, Guan C. Time-series representation learning via temporal and contextual contrasting. In: Zhou ZH, ed. _Proceedings of the Thirtieth International Joint Conference on Artificial Intelligence (IJCAI-21)._ International Joint Conferences on Artificial Intelligence Organization; 2021:2352-2359. https://doi.org/10.24963/ijcai.2021/324. 

13. Wang N, Feng P, Ge Z, Zhou Y, Zhou B, Wang Z. Adversarial spatiotemporal contrastive learning for electrocardiogram signals. 

_IEEE Trans Neural Netw Learn Syst._ 2024;35:13845-13859. https://doi.org/10.1109/TNNLS.2023.3272153. 

14. Lan X, Yan H, Hong S, Feng M. Towards enhancing time series contrastive learning: a dynamic bad pair mining approach. In: Kim B, Yue Y, Chaudhuri S, Fragkiadaki K, Khan ME, Sun Y, eds. _Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)_ . ICLR Proceedings; 2024. https:// openreview.net/forum?id=K2c04ulKXn 

15. Song J, Jang J-H, Lee BT, Hong D, Kwon J-M, Jo Y-Y. Foundation models for electrocardiograms. _arXiv_ [Preprint]. 2024. arXiv:2407.07110v1. 

16. Oh J, Chung H, Kwon J, Hong D, Choi E. Lead-agnostic selfsupervised learning for local and global representations of electrocardiogram. In: Flores G, Chen GH, Pollard T, Ho JC, Naumann T, eds. _Proceedings of the Conference on Health, Inference, and Learning (CHIL 2022)._ Vol 174. PMLR; 2022:338-353. 

17. Baevski A, Zhou H, Mohamed A, Auli M. wav2vec 2.0: a framework for self-supervised learning of speech representations. In: Larochelle H, Ranzato M, Hadsell R, Balcan M-F, Lin H, eds. _Advances in Neural Information Processing Systems._ Vol 33. Red Hook, NY: Curran Associates, Inc.; 2020:12449-12460. 

18. Reyna MA, Sadr N, Perez Alday EA, et al. Will two do? Varying dimensions in electrocardiography: the PhysioNet/Computing in Cardiology Challenge 2021. In: MacLeod RS, Provazn�ık I, eds. _2021 Computing in Cardiology (CinC)._ Vol 48. IEEE; 2021:1-4. https://doi.org/10.23919/CinC53138.2021.9662687 

19. Reyna M, Sadr N, Gu A, et al. _Will Two Do? Varying Dimensions in Electrocardiography: The PhysioNet/Computing in Cardiology Challenge 2021._ Version 1.0.3. PhysioNet; 2022. https://doi.org/ 10.13026/34va-7q14 

20. Goldberger AL, Amaral LA, Glass L, et al. PhysioBank, PhysioToolkit, and PhysioNet: components of a new research resource for complex physiologic signals. _Circulation._ 2000;101: e215-e220. 

21. Johnson AEW, Bulgarelli L, Shen L, et al. MIMIC-IV, a freely accessible electronic health record dataset. _Sci Data._ 2023;10:1. https://doi.org/10.1038/s41597-022-01899-x 

22. Cook DA, Oh SY, Pusic MV. Accuracy of physicians’ electrocardiogram interpretations: a systematic review and meta-analysis. _JAMA Intern Med._ 2020;180:1461-1471. 

23. Attia ZI, Kapa S, Lopez-Jimenez F, et al. Screening for cardiac contractile dysfunction using an artificial intelligence–enabled electrocardiogram. _Nat Med._ 2019;25:70-74. 

24. Murphy SP, Ibrahim NE, Jr, Januzzi JL. and Heart failure with reduced ejection fraction: a review. _JAMA._ 2020;324:488-504. 

25. Yao X, Rushlow DR, Inselman JW, et al. Artificial intelligence– enabled electrocardiograms for identification of patients with low ejection fraction: a pragmatic, randomized clinical trial. _Nat Med._ 2021;27:815-819. 

26. Yao X, McCoy RG, Friedman PA, et al. ECG AI-Guided screening for Low Ejection fraction (EAGLE): rationale and design of a pragmatic cluster randomized trial. _Am Heart J._ 2020;219:31-36. 

27. Nejedly P, Ivora A, Viscor I, et al. Classification of ECG using ensemble of residual CNNs with or without attention mechanism. _Physiol Meas._ 2022;43:044001. https://doi.org/10.1088/13616579/ac647c 

28. Han H, Park S, Min S, et al. Improving generalization performance of electrocardiogram classification models. _Physiol Meas._ 2023;44:054003. https://doi.org/10.1088/1361-6579/acb30f 

29. Kingma DP, Ba J. Adam: a method for stochastic optimization. In: Bengio Y, LeCun Y, eds. _Proceedings of the 3rd International Conference on Learning Representations (ICLR 2015)._ ICLR Proceedings; 2015. https://arxiv.org/abs/1412.6980 

30. Flach P, Kull M. Precision-recall-gain curves: PR analysis done right. In: Cortes C, Lawrence ND, Lee DD, Sugiyama M, Garnett R, eds. _Advances in Neural Information Processing Systems._ Vol 28. Red Hook, NY: Curran Associates, Inc.; 2015:838-846. 

© The Author(s) 2025. Published by Oxford University Press on behalf of the American Medical Informatics Association. 

This is an Open Access article distributed under the terms of the Creative Commons Attribution License (https://creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited. JAMIA Open, 2025, 8, 1–8 https://doi.org/10.1093/jamiaopen/ooaf122 Research and Applications 

