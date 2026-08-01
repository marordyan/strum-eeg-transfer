# BrainWave: A Brain Signal Foundation Model for Clinical Applications 

Zhizhang Yuan<sup>1</sup> , Fanqi Shen<sup>1</sup> , Meng Li<sup>2,3</sup> , Yuguo Yu<sup>4,5</sup> , Fei Wu<sup>1</sup> , Chenhao Tan<sup>6</sup> , Yang Yang<sup>1*</sup> 

> 1Computer Science and Technology, Zhejiang University, Hangzhou, Zhejiang, China. 

> 2Shanghai Institute of Microsystem and Information Technology, Chinese Academy of Sciences, Shanghai, China. 

> 3INSIDE Institute for Biological and Artificial Intelligence, Street, Shanghai, China. 

> 4Research Institute of Intelligent and Complex Systems, State Key Laboratory of Medical Neurobiology and MOE Frontiers Center for 

Brain Science, and Institute of Science and Technology for Brain-Inspired Intelligence, Fudan University, Shanghai, China. 5Shanghai Artificial Intelligence Laboratory, Fudan University, Shanghai, China. 

> 6University of Chicago, Chicago, Illinois, USA. 

*Corresponding author(s). E-mail(s): yangya@zju.edu.cn; Contributing authors: zhizhangyuan@zju.edu.cn; fanqishen@zju.edu.cn; li.meng@mail.sim.ac.cn; yuyuguo@fudan.edu.cn; wufei@zju.edu.cn; chenhao@uchicago.edu; 

#### **Abstract** 

Neural electrical activity is fundamental to brain function, and abnormal patterns of neural signaling often indicate the presence of underlying brain diseases. The variability among individuals, the diverse array of clinical symptoms from various brain disorders, and the limited availability of diagnostic classifications, have posed significant barriers to formulating reliable models of neural signals for diverse application contexts. Here, we present BrainWave, the first foundation model for both invasive and non-invasive neural recordings, pretrained on more than 40,000 hours of electrical brain recordings (13.79 TB of data) from 

1 

approximately 16,000 individuals. Our analysis show that BrainWave consistently achieves state-of-the-art performance in the identification of neurological disorders across various experimental settings. In addition, we demonstrate the effectiveness of pretraining, as BrainWave achieves strong few-shot classification performance without fine-tuning, indicating our pretraining strategy extracts informative representations from neural signals. BrainWave is also evaluated in real-world clinical scenarios, highlighting its potential in facilitating clinical interpretation and decision-making. We hence believe that open-sourcing BrainWave will facilitate a wide range of clinical applications in medicine, paving the way for AI-driven approaches to investigate brain disorders. 

**Keywords:** foundation model, brain signals, EEG, iEEG 

## **1 Introduction** 

Electrical brain recordings, capturing the intricate patterns of the brain’s electrical activities, are essential in advancing our understanding of brain across scientific domains [1–7]. In particular, they can be used to identify medical conditions and diagnose neurological disorders, and are thus essential for addressing major global health challenges in developing nations [8, 9]. Scalp electroencephalography (EEG) and intracranial electroencephalography (iEEG) are two primary methods to conduct these types of recordings. EEG is non-invasive and economical viable, and has thus been used in diverse applications [10–14]. In contrast, iEEG offers high signal fidelity and spatial resolution [15], but the invasive nature limits its applicability to only the most severe patient cases and restricted scenarios. Due to the distinct features of EEG and iEEG data, such as different acquisition rates and notable variations in channel numbers [16–18], studies have so far investigated them separately. We hypothesize that combining EEG and iEEG data can offer information that are not only rich in detail but also highly generalizable across diverse neural electrical activities, and develop a pioneering foundational model, BrainWave, for both EEG and iEEG data. BrainWave learns robust representations that achieve state-of-the-art performance in a wide range of tasks, demonstrating the synergy of EEG and iEEG data for the first time. 

BrainWave overcomes a suite of inherent challenges in conventional supervised artificial intelligence (AI) models used for the analysis of brain signals. First, BrainWave leverages self-supervised training, circumventing the need for large-scale, high-quality manual labeling. In clinical applications, the process of brain data annotation is laborintensive and reliant on specialized expertise [19–21], exemplified by the need for multi-day monitoring for epilepsy patients [22] and the clinical experts’ capacity to annotate only tens of seconds of data in a single work period. Second, BrainWave provides much-need generalization at two levels that were not possible in supervised training, which requires an understanding of fundamental and general patterns in brain signals. Individual variability in brain neural activities, a consequence of each person’s distinct brain structure and functional behaviors [23], leads to markedly different brain recording patterns [24]. This diversity hinders the generalizability of supervised AI 

2 

models, as they often struggle to extend the insights gained from a subset of patients to a broader population, due to significant differences across individuals, as well as variability that changes with different behavioral states. Moreover, there are numerous types of brain-related diseases with various underlying mechanisms [25–28], and even a single disease may present with multiple subtypes [29]. Supervised AI models are task-specific and fail to address a diverse range of tasks using brain signals [24, 30–37]. 

While prior work has attempted to build foundation models for brain signals [38– 43], BrainWave offered unique technical contributions by building the largest dataset of electrical brain recordings and developing novel techniques to integrate EEG and iEEG data for the first time. As illustrated in Figure 1a, we collected a total of 13.79 TB of combined EEG and iEEG data over a duration of 40,907 hours, which serves as the foundation for pretraining BrainWave. The data were obtained from 15,997 individuals, including both healthy individuals and those with various brain disorders, spanning an age range from infancy ( _<_ 1 year) to over 90 years old. The sampling rates vary across different brain signal datasets, with a more pronounced disparity between EEG and iEEG data, which increases the difficulty of unified modeling. Previous works generally focused on modeling either EEG or iEEG alone, so they often uniformly resampled the data to a common sampling rate [44–46]. We proposed a scale alignment layer that adapts to arbitrary temporal resolutions without the need for resampling, thereby improving data scalability and enhancing generalization capabilities. In the pretraining stage, we adopt a masked modeling strategy that reconstructs the timefrequency representations of the masked patches (Fig. 1b). We also employed a channel count-agnostic approach to capture the inter-channel relationships. Empowered by growing datasets and advances in model design, BrainWave exhibited highly robust pretrained representations and excellent transfer learning capabilities (Fig. 1c). 

To comprehensively assess the capabilities of BrainWave as a foundation model for electrical brain recordings in healthcare scenarios, we constructed a benchmark consisting of 15 datasets and 20 tasks. To evaluate generalization, we systematically assessed BrainWave across different cross-domain settings, including cross-subject (Fig. 2a and b), cross-hospital (Fig. 2c) and cross-subtype (Fig. 2d) tasks. To verify the effectiveness of pretraining, we introduced few-shot classification tasks to evaluate the capability of the pretrained representations when directly applied to downstream tasks without fine-tuning (Fig. 3). BrainWave is compared against the previous state-of-the-art foundation models that are publicly available, including LaBraM [44], BrainBERT [46] and MOMENT [47]. Figure 1d summarizes the overall results of BrainWave compared with other methods, in which BrainWave attains consistently state-of-the-art performance on all the 24 experiments, with significant improvement ( _p <_ 0 _._ 001) over the second-best method in 20 experiments, showing the versatility of BrainWave in a wide array of tasks. To demonstrate the practical value of BrainWave, we designed a series of clinical tasks in two real-world scenarios: seizure onset zone localization in epilepsy, and prediction of key biomarkers and clinical scale scores in Alzheimer’s disease, showcasing its potential in supporting clinical decision-making (Fig. 5). To investigate the effectiveness of joint pretraining with both non-invasive and invasive neural data, we compared BrainWave with two model variants pretrained exclusively 

3 



<!-- Start of picture text -->
a<br>Data processing Large data corpus Different electrical brain recordings Different data collection scenarios<br>Epilepsy Alzheimer'sdisease Stroke Concussion<br>EEG<br>Sleep-disorderedbreathing Narcolepsy Parkinson'sdisease Insomnia ...<br>13.79 TB iEEG<br>40,907 hours<br>Pretrain 15,997 individuals<br>b Latent representations<br>[CLS] [CLS]<br>[CLS][CLS][CLS] [CLS][CLS][CLS]<br>Reconstruct masked specgrams<br>[MSK]<br>[MSK]<br>[CLS] [CLS]<br>[CLS]<br>Signal Specgrams<br>patches with masks<br>c Few-shot classification with class prototypes d BrainWave LaBraM BrainBERT MOMENT<br>Cross-subject Cross-hospital Cross-subtype Few-shot classification<br>Support set Query<br>Absence-16 CHB-MIT ADHD-Child<br>BrainWave BrainWave BrainWave BrainWave Mayo-Clinic 97 91 81 ADHD-Adult<br>FNUSA 98 92 80 72 97 Schizophrenia-28<br>93 90 90 89<br>AD-65 67 60 84 76 83 758681 6070 566475 82 66 78 70 79 Depression-122<br>Prototypes MDD-64 90 82 74 52 4567 54 50 6083 88 92 MDD-64<br>Cross-domain transfer learning Depression-122 74 70 65 6660 7954 61 68 76 AD-65<br>Source subjects Hospital A Absence seizure 53 61<br>BrainWavefine-tune BrainWavefine-tune BrainWavefine-tune Schizophrenia-28ADHD-Adult72 91 66 80 596970 61 607254 667567 5664 495856 556466 62 747072 83 83 91 94Mayo-Clinicto FNUSAMayo-ClinicFNUSA to<br>Target subjectspredict Hospital Bpredict Clonic seizurepredict ADHD-Child 76 83 78 83 72 68 72 80 78 Absence-16to Atonic-5<br>CHB-MIT 92 80 77 Absence-16to Clonic-6<br>Absence-16 Mayo-Clinic FNUSA<br>... ... ...<br>Channel 0Channel 1Channel 2 Channel C<br>3 s<br>2 s<br>1 s<br>0 s<br>... ...<br>... ... ...<br>...<br>Channel attention<br>Scale alignment layer Transformer encoder<br>Nx<br>... ... ... ...<br>... ...<br>loss<br>Projection layer Reconstruction<br>Transformer blocks<br>Lightweight decoder<br><!-- End of picture text -->

**Fig. 1 Overview of BrainWave** . **a,** Data curation for pretraining BrainWave. The pretraining corpus contains both invasive and non-invasive brain recordings collected from diverse healthcare scenarios. **b,** The pretraining pipeline of BrainWave. BrainWave is pretrained on more than 3 billion signal patches using a masked modeling strategy. **c,** The evaluation tasks consist of few-shot classification and cross-domain evaluation. We conduct few-shot classification with a prototypical network in which the we directly compare the representations of the queries with class prototypes. We perform three different levels of cross-domain analysis: cross-subject, cross-hospital, and cross-subtype. **d,** The overall results of BrainWave compared to other pretrained models. BrainWave outperforms other models across all the 24 experiments, with significant4 improvement ( _p <_ 0 _._ 001) in 20 of them. 



<!-- Start of picture text -->
BrainWave LaBraM BrainBERT MOMENT<br>a b P  < 0.001 c P  = 0.009 d P  < 0.001 e P  < 0.001<br>1.0 1.0 1.0 1.0 1.0<br>P  < 0.001<br>0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4<br>AD-65 CHB-MIT Absence-16 Mayo-Clinic FNUSA<br>f 1.0 P  < 0.001 g 1.0 h 1.0 P  < 0.001 i 1.0 P  < 0.001 j 1.0<br>P  < 0.001 P  < 0.001<br>0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4<br>MDD-64 Depression-122 Schizophrenia-28 ADHD-Adult ADHD-Child<br>BrainWave LaBraM BrainBERT MOMENT BrainWave LaBraM BrainBERT MOMENT<br>k l m n<br>1.0 P  = 0.012 1.0 P  < 0.001 1.0 1.0<br>P  < 0.001 P  < 0.001<br>0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4<br>Mayo-Clinic to FNUSA FNUSA to Mayo-Clinic Absence-16 to Clonic-6 Absence-16 to Atonic-5<br>AUROC<br>AUROC<br>AUROC AUROC<br><!-- End of picture text -->

**Fig. 2 Performance of cross-domain evaluation. a-j,** Bar plots comparing the AUROC scores of BrainWave and competing models on cross-subject tasks. Each experiment is conducted with _n_ - fold cross validation ( _n_ is the number of subject groups), where we repeat five runs for each fold. **k,l,** Bar plots comparing the AUROC scores of BrainWave and competing models on cross-hospital tasks. **m,n,** Bar plots comparing the AUROC scores of BrainWave and competing models on crosssubtype tasks. **k-n,** The source dataset is served as the training set and the target dataset is served as the evaluation set. In each experiment, we repeat five runs. **a-n,** Data are mean _±_ SD. The listed _p_ value indicates the significance for BrainWave outperforming the best comparison model, with the two-sided _t_ -test. 

on EEG or iEEG data across all experiments (Fig. 5a-d). The results show that BrainWave outperforms other variants in diverse tasks, highlighting the effectiveness of its design empowered by joint pretraining. In conclusion, our study demonstrates (1) the robustness of the pretrained representations, (2) the potential of BrainWave in clinical diagnostic support, and (3) the effectiveness of joint pretraining. 

We will release BrainWave as a publicly available model, which will serve as a basis for others in their own tasks, facilitating diverse clinical applications and research for brain recordings. 

5 

## **2 Results** 

### **2.1 Cross-domain Disease Diagnosis and Detection** 

Cross-domain evaluation is an important setting for verifying the generalization capability of the model. Firstly, we conducted cross-subject evaluation, in which we split the subjects into _n_ non-overlapping groups and employed _n_ -fold cross validation to evaluate all models, ensuring that all subjects are included in the testing process. In each fold, we randomly selected a subject group from the training set for validation and repeated five runs. BrainWave was evaluated against competing methods on a total of 10 datasets, including Alzheimer’s disease (AD), epilepsy, major depressive disorder, schizophrenia and attention-deficit/hyperactivity disorder (ADHD). Model performance was reported using the area under the receiver operating curve (AUROC) and balanced accuracy (BACC). We calculated _p_ values with the two-sided _t−_ test between BrainWave and the most competitive comparison model for each task to check for significance. Across all experiments, BrainWave consistently outperformed other methods with an average relative improvement of 11.93% in AUROC and 17.59% in BACC over each second-best performing model (Fig. 2a-j and Extended Data Fig. A1). In schizophrenia diagnosis (Fig. 2h; dataset Schizophrenia-28 [48]), BrainWave achieved an improvement of 37.44% and 41.59% compared to the best comparison model in terms of AUROC and BACC. In seizure detection (Fig. 2b; dataset CHB-MIT [49]), BrainWave demonstrated a 26.18% boost relative to the second best method. The strong performance of BrainWave on both ADHD-Adult [50] (Fig. 2i) and ADHD-Child [51] (Fig. 2j) indicated its robustness across age groups, owing to the broad age distribution in our pretraining corpus. In conclusion, BrainWave significantly surpassed other models ( _p <_ 0 _._ 001) on 9 out of the 10 datasets, demonstrating its superiority in disease diagnosis and detection. 

The promising results of BrainWave on cross-subject evaluation motivated us to further explore its transfer capability across more divergent distributions. Thus, we attempted two more challenging experimental setups. Under these settings, we finetuned on one dataset and directly apply the model to another. These datasets are not only collected from different individuals but also from different hospitals and collection devices, or from patients with different disease subtypes. Unlike the traditional paradigm where fine-tuning is dataset-specific, these settings allow the model to be seamlessly deployed across different datasets and even different but related tasks. The cross-hospital evaluation involved mutual transfer between two datasets, Mayo-Clinic and FNUSA [52], both collected from patients with drug resistant epilepsy (DRE) but from different hospitals. The cross-subtype evaluation included three datasets, namely Absence-16, Clonic-6, and Atonic-5, collected from patients with different subtypes of seizures (absence seizure, clonic seizure, and atonic seizure), and we performed zeroshot transfer from Absence-16 to Clonic-6 and Atonic-5. BrainWave showed promising results and achieved the best performance in all cross evaluations (Fig. 2m-p and Extended Data Fig. A2). For instance, BrainWave achieved an impressive AUROC of 93.82% in the zero-shot transfer from FNUSA to Mayo-Clinic (Fig. 2n). When transferring across different seizure subtypes (Fig. 2o,p), BrainWave exhibited average improvements of 13.90% and 13.49% in terms of AUROC and BACC, respectively, 

6 



<!-- Start of picture text -->
BrainWave LaBraM BrainBERT MOMENT<br>a b c d e<br>1.0 AD-65 1.0 CHB-MIT 1.0 Absence-16 1.0 Mayo-Clinic 1.0 FNUSA<br>0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4<br>3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot<br>f g h i j<br>1.0 MDD-64 1.0 Depression-122 1.0 Schizophrenia-28 1.0 ADHD-Adult 1.0 ADHD-Child<br>0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4<br>3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot<br>k BrainWave LaBraM BrainBERT MOMENT<br>AUROC<br>AUROC<br>Absence-16<br><!-- End of picture text -->

**Fig. 3 Performance and analysis of few-shot classification. a-j,** Box plots comparing the AUROC scores of BrainWave and competing models on few-shot classification. We conduct _n_ -fold cross validation for each experiment and repeat five runs per fold. We perform 3-shot and 8-shot classification for each task. **k,** t-SNE (t-distributed Stochastic Neighbor Embedding) plots of the pretrained representations on Absence-16 generated from BrainWave and other pretrained encoders. Each model contains four subplots, with each subplot generated by randomly sampling a portion of the original dataset. 

compared to the second-best model. In summary, our experimental results indicated that BrainWave holds the potential to reduce labeling and training costs under similar scenarios, demonstrating strong transferability across disease detection tasks. 

### **2.2 Few-shot Classification** 

In clinical practice, limited availability of labeled data sometimes poses challenges for fine-tuning models, which hig ~~<u>h</u>~~ lights the critical i ~~<u>m</u>~~ portance of learnin ~~<u>g</u>~~ sufficien ~~<u>t</u>~~ ly robust representations. Conseq ~~<u>u</u>~~ ently, we ~~<u>p</u>~~ erformed ~~fe~~ w-shot cl ~~<u>a</u>~~ ssificatio ~~n,~~ which is ~~a~~ n evaluation scheme that studies ~~<u>t</u>~~ he gener ~~<u>a</u>~~ lization ca ~~p~~ abilities ~~<u>o</u>~~ f models ~~o~~ n new tas ~~k~~ s given a very limited number o ~~<u>f</u>~~ labeled ~~<u>e</u>~~ xamples. ~~<u>W</u>~~ e adopt ~~<u>e</u>~~ d a direct comparis ~~<u>o</u>~~ n strategy for classification by co ~~<u>m</u>~~ paring t ~~h~~ e represen ~~<u>t</u>~~ ations of the querie ~~<u>s</u>~~ with pro ~~<u>t</u>~~ o- type of each category (Fig. 1c). The proc ~~<u>e</u>~~ ss solely i ~~n~~ volved o ~~<u>b</u>~~ taining re ~~<u>p</u>~~ resentatio ~~<u>n</u>~~ s 

7 

from the pretrained models and computing class prototypes, without any parameter updates or introduction of new parameters. The few-shot experiments were still conducted under the cross-subject setting and we employed _n_ -fold cross validation, where in each fold we randomly chose labeled examples from the training set as the support set. We established two sizes for the support set, with 3 and 8 labeled examples per class (3-shot and 8-shot), respectively. Given that the performance can fluctuate depending on the support set, we repeated experiments over five runs in each fold. 

We conducted few-shot experiments (Fig. 3a-j and Extended Data Fig. A3) on all datasets used in the cross-subject evaluation and found that BrainWave still maintained solid performance by achieving an average improvement of 22.23% in terms of AUROC compared to the second-best model. For instance, on Absence16 (Fig. 3c) and ADHD-Adult (Fig. 3i), BrainWave achieved an AUROC over 90% (91.93% on Absence-16, 90.39% on ADHD-Adult) in 8-shot classification. On MDD64 [53] (Fig. 3f), the performance of 8-shot learning even nearly matched that of full-label supervised fine-tuning (89.83% versus 91.50%). BrainWave not only outperformed other models by a large margin but also demonstrated greater robustness to the selection of the support set. Specifically, we calculated the average standard deviation across all few-shot experiments and found that the fluctuations in BrainWave’s performance are, on average, smaller than those of the second-best performing models (5.74% versus 6.06%). The poor performance of BrainBERT in few-shot classification may be due to its limitation in supporting only fixed input length and sampling rate. This limitation requires additional operations to accommodate varying datasets, highlighting the importance of flexible input support for diverse tasks. 

Surprisingly, we also observed that when comparing the 8-shot performance of BrainWave with the full-label fine-tuning (i.e., with thousands or even tens of thousands of labeled examples) performance of other pretrained models, our model still outperforms on the majority of datasets (Extended Data Fig. A4). Across all datasets, BrainWave achieved average AUROC improvements of 2.27%, 26.40% and 14.87% over LaBraM, BrainBERT and MOMENT, respectively. To better illustrate the results, we visualized the representations of the pretrained models, with different colored points representing different categories (Fig. 3k) and Extended Data Fig. A5). Even without fine-tuning, the representations generated by BrainWave are sufficiently discriminative and enable its outstanding performance in few-shot classification. Overall, our extensive evaluation of few-shot classification demonstrated the immense potential of BrainWave as a foundational model that offers robust and off-the-shelf representations for electrical brain recordings. 

### **2.3 Clinical Application** 

In addition to its superior performance on brain disorder detection benchmarks, BrainWave demonstrates practical utility by offering valuable assistance and guidance in real-world clinical scenarios. 

Firstly, we utilized BrainWave to assist in localizing the seizure onset zone (SOZ), which refers to the region of the brain where epileptic seizures originate. Accurate identification of the SOZ is critical for planning surgical treatment in patients with DRE, as it guides the localization of the epileptogenic focus and supports diagnostic evaluation 

8 



<!-- Start of picture text -->
patient 01 patient 03<br>patient 02 patient 04<br>0.75 0.85 0.95<br>0.95<br>0.85<br>0.75<br>Sensitivity<br>0.8 0.9 1.0<br>1.0<br>0.9<br>0.8<br>Specificity<br>AP<br><!-- End of picture text -->



<!-- Start of picture text -->
Epileptic discharge occurrence<br>A1-A2 A2-A3 A3-A4 A4-A5 A5-A6 A6-A7 A7-A8 A8-A9 A9-A10 A10-A11 A11-A12 A12-A13 A13-A14 A14-A15 A15-A16 Pinpoint<br>B1-B2 B2-B3 B3-B4 B4-B5 B5-B6 B6-B7 B7-B8 B8-B9 B9-B10 B10-B11 B11-B12 B12-B13 B13-B14 B14-B15 B15-B16<br>C1-C2 C2-C3 C3-C4 C4-C5 C5-C6 C6-C7 C7-C8 C8-C9 C9-C10 C10-C11 C11-C12 C12-C13 C13-C14 C14-C15 C15-C16<br>D1-D2 D2-D3 D3-D4 D4-D5 D5-D6 D6-D7 D7-D8 D8-D9 D9-D10 D10-D11 D11-D12<br>E1-E2 E2-E3 E3-E4 E4-E5 E5-E6 E6-E7 E7-E8 E8-E9 E9-E10 E10-E11 E11-E12 E12-E13 E13-E14 E14-E15 E15-E16<br>F1-F2 F2-F3 F3-F4 F4-F5 F5-F6 F6-F7 F7-F8 F8-F9 F9-F10 F10-F11 F11-F12 F12-F13 F13-F14 F14-F15 F15-F16<br>G1-G2 G2-G3 G3-G4 G4-G5 G5-G6 G6-G7 G7-G8 G8-G9 G9-G10 G10-G11 G11-G12 G12-G13 G13-G14 G14-G15 G15-G16<br>H1-H2 H2-H3 H3-H4 H4-H5 H5-H6 H6-H7 H7-H8 H8-H9 H9-H10 H10-H11 H11-H12 H12-H13 H13-H14 H14-H15 H15-H16<br><!-- End of picture text -->



<!-- Start of picture text -->
A1-A2 A2-A3 A3-A4 A4-A5 A5-A6 A6-A7 A7-A8<br>B1-B2 B2-B3 B3-B4 B4-B5 B5-B6 B6-B7 B7-B8<br>C1-C2 C2-C3 C3-C4 C4-C5 C5-C6 C6-C7 C7-C8<br>D1-D2 D2-D3 D3-D4 D4-D5 D5-D6 D6-D7 D7-D8<br>E1-E2 E2-E3 E3-E4 E4-E5 E5-E6 E6-E7 E7-E8<br>F1-F2 F2-F3 F3-F4 F4-F5 F5-F6 F6-F7 F7-F8<br>G1-G2 G2-G3 G3-G4 G4-G5 G5-G6 G6-G7 G7-G8<br>H1-H2 H2-H3 H3-H4 H4-H5 H5-H6 H6-H7 H7-H8<br>A1-A2 A2-A3 A3-A4 A4-A5 A5-A6 A6-A7 A7-A8<br>B1-B2 B2-B3 B3-B4 B4-B5 B5-B6 B6-B7 B7-B8<br>C1-C2 C2-C3 C3-C4 C4-C5 C5-C6 C6-C7 C7-C8<br>D1-D2 D2-D3 D3-D4 D4-D5 D5-D6 D6-D7 D7-D8<br>E1-E2 E2-E3 E3-E4 E4-E5 E5-E6 E6-E7 E7-E8<br>F1-F2 F2-F3 F3-F4 F4-F5 F5-F6 F6-F7 F7-F8<br>G1-G2 G2-G3 G3-G4 G4-G5 G5-G6 G6-G7 G7-G8<br>H1-H2 H2-H3 H3-H4 H4-H5 H5-H6 H6-H7 H7-H8<br><!-- End of picture text -->



<!-- Start of picture text -->
Pinpoint<br><!-- End of picture text -->



<!-- Start of picture text -->
G1-G2 G2-G3 G3-G4 G4-G5 G5-G6 G6-G7 G7-G8 G8-G9 G9-G10 G10-G11 G11-G12 G12-G13 G13-G14 G14-G15 G15-G16<br>H1-H2 H2-H3 H3-H4 H4-H5 H5-H6 H6-H7 H7-H8 H8-H9 H9-H10 H10-H11 H11-H12 H12-H13 H13-H14 H14-H15 H15-H16<br><!-- End of picture text -->











**Fig. 4 Clinical tasks on epilepsy and AD. a,** Channel-level epileptic waveform detection on 4 patients with DRE. Sensitivity/Specificity and AUROC/AP are reported. **b,** The process of pinpointing channels with frequent epileptic discharges and repeated involvement as seizure onset sites. We can quickly quantify these metrics for each channel from model predictions. **c-g,** Predictions of amyloid-beta deposition and a series of clinical scale scores from AD patients. Each experiment is conducted with 5-fold cross validation, where we repeat five runs for each fold. **c,** Amyloid-beta deposition prediction. **d,** MMSE score prediction. We divide it into 4 discrete ranges: 24-30, 21-23, 10-20 and 0-9. **e,** MoCA-B score prediction. We divide it into 4 discrete ranges: 26-30, 18-25, 10-17 and 0- ~~9.~~ **f,** ROCF score prediction. We divide it into 5 discrete ranges: 33-36, 24-32, 18-23, 12-17 and <mark>0-11.</mark> **<mark>g</mark>** **<u>,</u>** PSQI score prediction. We divide it into 4 discrete ranges: 0-5, 6-10, 11-15 and 16-21. 



<mark>for su</mark> ~~b~~ sequent resective surgery. Patients with DRE often require intracranial elec- <mark>trode</mark> ~~i~~ mplantation to record seizure activity. The SOZ can be localized by analyzing <mark>the w</mark> ~~<mark>a</mark>~~ veforms of different channels, which involves distinguishing seizure patterns on a per-channel basis. Such a process demands more fine-grained and precise analysis than merely classifying epileptic versus normal waveforms over a certain time period. As shown in Fig. 4a, BrainWave is evaluated on channel-level epileptic waveform detection across 4 patients with DRE, in which the average Sensitivity/Specificity, AUROC/Average Precision (AP) achieved 84.65%/86.87% and 93.24%/86.71% respectively. The predictions of BrainWave helped reveal the spatial distribution of seizure activity. We took patient 04 as an example. The heatmap shown on the left side of Fig 4b is the channel-level predicted probabilities of multiple seizures from patient 04 provided by BrainWave. As shown in the middle of Fig 4b, the predictions enabled us to quantify two metrics for each channel: the probability of epileptic discharge occurrence across multiple seizures (upper), and the number of times it serves as the seizure onset site (lower). Higher values of these two metrics suggested a greater likelihood of the channel being part of the SOZ. As shown on the right side of Fig 4b, clinicians can quickly 



9 

identify the corresponding brain regions based on the statistical results, facilitating surgical planning. 

Secondly, BrainWave can predict clinical assessment indicators for AD based on EEG signals. The diagnosis of AD involves a series of physiological examinations and cognitive scale tests. The results of these assessments serve as important references for the clinical diagnosis of AD. We conducted experiments on 6 patients, using their recorded EEG data to predict amyloid-beta deposition and a range of clinical scale scores (Supplementary Tables 17), including Mini-Mental State Examination (MMSE), Montreal Cognitive Assessment-Basic (MoCA-B), Rey–Osterrieth Complex Figure Test (ROCF), and Pittsburgh Sleep Quality Index (PSQI). Amyloid-beta deposition is one of the key biomarkers in the diagnosis of AD, which is often detected by Positron Emission Tomography (PET) imaging. MMSE, MoCA-B, and ROCF are cognitive assessment tests, and PSQI is used to evaluate sleep quality. For the clinical scale scores, we divided the scores into several discrete ranges for prediction. Each range represents an evaluation category, such as normal, mild cognitive impairment, moderate cognitive impairment, severe cognitive impairment, and so on. We split the data into 5 groups and utilized a 5-fold cross validation. Each fold was repeated 5 runs. Fig 4c-g shows the results, in which BrainWave achieved an average accuracy close to or exceeding 95% across all tasks, along with an average Cohen’s Kappa above 0.9. BrainWave’s predictions exhibited strong consistency with established clinical evaluation outcomes, highlighting its great potential to support clinical diagnosis. 

### **2.4 Analysis of Joint Pretraining** 

To the best of our knowledge, BrainWave is the first foundational model that combines invasive and non-invasive neural data. We next examine the effectiveness of this joint pretraining strategy to determine whether it is more effective to pretrain a separate model for each recording type and apply it for corresponding downstream tasks with the same recording type, or to utilize a joint pretraining approach. To this end, we separately pretrained two model variants, namely BrainWave-EEG and BrainWave-iEEG, using EEG and iEEG data, respectively, while keeping the model and pretraining configurations (Supplementary Tables 18 and 19) identical to BrainWave. The numbers of patches for pretraining BrainWave-EEG and BrainWave-iEEG are relatively balanced (1.74 billion versus 1.42 billion). Subsequently, we conducted cross-domain evaluation and few-shot classification on both model variants, in which BrainWave-EEG was evaluated on EEG datasets and BrainWave-iEEG was evaluated on iEEG datasets. 

Through a series of experiments, we observed that BrainWave outperformed the other two variants in almost all tasks and experimental settings (Fig. 5a-d and Extended Data and Figs. A6 and A7), except in experiment Absence-16 to Atonic-5 where BrainWave is slightly lower than BrainWave-EEG in terms of BACC (44.55% versus 47.23%). From the overall results, we discovered that the integration of iEEG during joint pretraining enhanced the performance on downstream tasks based on EEG data and vice versa, suggesting that BrainWave is able to capture fundamental insights about brain activities by combining two distinct types of signals. In comparison to the average improvement over two model variants (Fig. 5e), the improvement of 

10 



<!-- Start of picture text -->
a BrainWave (EEG dataset) BrainWave (iEEG dataset) BrainWave-EEG BrainWave-iEEG<br>1.0 1.0<br>0.8 0.8<br>0.6 0.6<br>b BrainWave BrainWave-iEEG c BrainWave BrainWave-EEG<br>1.0 P  < 0.001 1.0 P  = 0.014 1.0 P  = 0.032 1.0 P  = 0.010 1.0 P  < 0.001 1.0 P  < 0.001 1.0 P  < 0.001 1.0 P  = 0.080<br>0.8 0.8<br>0.8 0.8<br>0.8 0.8 0.8 0.8 0.6 0.6<br>0.6 0.6 0.4 0.4<br>0.6 0.6 0.6 0.6<br>0.4 0.4 0.2 0.2<br>Mayo-Clinic to FNUSA to Mayo-Clinic to FNUSA to Absence-16 to Absence-16 to Absence-16 to Absence-16 to<br>FNUSA Mayo-Clinic FNUSA Mayo-Clinic Clonic-6 Atonic-5 Clonic-6 Atonic-5<br>d BrainWave BrainWave-EEG BrainWave-iEEG<br>1.0 AD-65 1.0 CHB-MIT 1.0 Absence-16 1.0 Mayo-Clinic 1.0 FNUSA<br>0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4<br>3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot<br>MDD-64 Depression-122 Schizophrenia-28 ADHD-Adult ADHD-Child<br>1.0 1.0 1.0 1.0 1.0<br>0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4<br>3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot<br>e f<br>Average improvement over BrainWave-EEG Average improvement over BrainWave-iEEG BrainWave BrainWave-EEG BrainWave-iEEG<br>AUROC BACC 1.0 1.0<br>cross-domain  cross-domain<br>evaluation evaluation 0.8 0.8<br>classificationfew-shot classificationfew-shot 0.6 0.6<br>0 0.03 0.06 0.09 0 0.03 0.06 0.09 0.12<br>Apnea-ECG<br>AD-65 CHB-MITAbsence-16Mayo-Clinic FNUSA MDD-64Depression-122Schizophrenia-28ADHD-AdultADHD-Child AD-65 CHB-MITAbsence-16Mayo-Clinic FNUSA MDD-64Depression-122Schizophrenia-28ADHD-AdultADHD-Child<br>AUROC BACC<br>AUROC BACC AUROC BACC<br>AUROC<br>AUROC<br>AUROC BACC<br><!-- End of picture text -->

**Fig. 5 Analysis of joint pretraining. a,** Scatter plots comparing the AUROC and BACC scores of BrainWave, BrainWave-EEG and BrainWave-iEEG on cross-subject tasks. **b,** Bar plots comparing the AUROC and BACC scores of BrainWave and BrainWave-iEEG on cross-hospital tasks. **c,** Bar plots comparing the AUROC and BACC scores of BrainWave and BrainWave-EEG on cross-subtype tasks. **b,c,** The source dataset is served as the training set and the target dataset is served as the evaluation set. In each experiment, we repeat five runs. Data are mean _±_ SD. The listed _p_ value indicates the significance for BrainWave outperforming the best comparison model, with the two-sided _t_ -test. **d,** Box plots comparing the AUROC scores of BrainWave, BrainWave-EEG and BrainWaveiEEG on few-shot classification. We perform 3-shot and 8-shot classification for each dataset. **e,** Average improvement of BrainWave over BrainWave-EEG and BrainWave-iEEG on cross-domain evaluation and few-shot classification. We first calculate the relative improvement for each experiment and then compute the average of them. **f,** Bar plots comparing the AUROC and BACC scores of BrainWave, BrainWave-EEG and BrainWave-iEEG on out-of-domain recording type evaluation. We collect a ECG dataset (Apnea-ECG) with a sleep apnea detection task. Data are mean _±_ SD. **a,d,f,** Each experiment is conducted with _n_ -fold cross validation ( _n_ is the number of subject groups), where we repeat five runs for each fold. 

11 

the BrainWave over BrainWave-EEG was more significant than the improvement over BrainWave-iEEG (7.25% versus 2.05% on cross-domain evaluation and 8.30% versus 4.98% on few-shot classification in terms of AUROC). The phenomenon suggested that the boost in performance achieved by incorporating iEEG data in the pretraining was more pronounced, which might be attributed to the lower signal-to-noise ratio and higher accuracy of intracranial neural signals. 

Given that joint pretraining leads to increase in performance, we further explored the underlying reasons by analyzing the representations learned by the models. First, we validated whether joint pretraining can learn more enriched information. For this purpose, we performed principal component analysis (PCA) to the pretrained representations, selecting principal components until 99% of the variance could be explained. We conducted analysis on 12 datasets and recorded the number of principal components _k_ of each dataset. On 11 out 12 datasets, BrainWave yielded a higher _k_ value (Supplementary Tables 20 and 21), indicating that BrainWave demonstrated the ability to extract more enriched information from downstream datasets. Furthermore, we conducted an additional experiment by evaluating the performance of the BrainWave versus other variants on another type of biosignal, electrocardiogram (ECG), through which we aimed to verify if joint pretraining results in a stronger adaptability on new tasks due to the acquisition of more general patterns. The results (Fig. 5f) showed that BrainWave achieves an improvement of 9.90% and 19.48% in terms of AUROC over BrainWave-iEEG and BrainWave-EEG, respectively, demonstrating that joint pretraining enables better generalization to unseen data types. To summarize, BrainWave learned richer semantic information and more general patterns of the data than other model variants with only one type of data. This finding opens up possibilities for expanding signal types and developing more versatile foundational models for biosignals. 

## **3 Discussion** 

We have introduced BrainWave, a brain signal foundation model that learns robust representations of electrical brain recordings for a broad range of clinical applications. To the best of our knowledge, BrainWave is the first model pretrained on a largescale dataset composed of recordings from both invasive and non-invasive modalities, which comprised more than 3 billion signal patches from approximately 16,000 individuals. The architectural design accommodated brain recordings of varying lengths, sampling rates, and electrode counts, thereby enhancing the flexibility of BrainWave for joint pretraining and deployment on EEG and iEEG data. We employed a masked modeling strategy to pretrain BrainWave, enabling the model to reconstruct the complete sequence from partial observations. In comprehensive experiments involving cross-domain evaluation and few-shot classification, we demonstrated the versatility of BrainWave across a wide array of brain disorder detection tasks under diverse conditions. We also applied BrainWave to real-world clinical scenarios, suggesting that BrainWave holds significant potential to support clinical diagnostics and the identification of health conditions. 

12 

Beyond its practical value, BrainWave yields valuable insights into the fundamental model governing multimodal neural electrical signals. The present study represents the initial investigation to utilize joint pretraining with both EEG and iEEG data. Through rigorous assessment, we demonstrated the effectiveness of this novel methodological approach. The results of our study demonstrate a significant performance boost derived from the joint pretraining approach, compared to control model configurations. Additionally, we have elucidated the factors contributing to the enhanced performance associated with joint training. Future investigations can build upon our findings to examine whether comparable performance enhancements can be attained with other neural data types or even cross-domain data encompassing varied physiological signals. 

As an exciting interdisciplinary research direction between neuroscience and artificial intelligence, BrainWave may also provide a new approach to deciphering the mechanisms of brain information processing. A key challenge in neuroscience research involves analyzing and elucidating the fundamental operating principles governing population-level neural networks, as derived from high-volume neural recording data. Large language models have demonstrated its capacity to extract fundamental attributes of human cognition by compressing substantial human linguistic data **??** . Similarly, the impressive performance of BrainWave, as shown in the present study, may be attributed to their ability to thoroughly comprehend and effectively extract features of brain neural activity. Analyzing the network properties of BrainWave could potentially offer insights to guide research on biological neural networks. Specifically, by modulating various parameters of BrainWave, analogous models representing diverse brain disorders can be generated, thereby establishing a novel experimental framework for neuroscience and brain disease research. 

Despite the promising results, there is a wealth of potential for further development and advancement. Firstly, BrainWave cannot handle data from other modalities, such as magnetic resonance imaging (MRI), which can provide higher spatial resolution compared to electrical signals and is widely used in healthcare applications. Consequently, our ultimate objective is to develop a model framework that can accommodate various data modalities. Secondly, diverse medical scenarios collect various physiological signals, with diagnoses sometimes relying on multiple signal types. For instance, stroke diagnosis and rehabilitation often require the recording of EEG and EMG (Electromyography)[54]. To enhance suitability for a more expansive set of healthcare applications, the model should possess the capability to accommodate a more diverse array of biosignals. This investigation involved initial efforts utilizing electrocardiogram data, which indicates that additional advancements are necessary before constructing a comprehensive model able to accommodate a variety of physiological measurements. 

13 

## **4 Methods** 

### **4.1 Technique details** 

Fig. 1b shows the overall architecture of BrainWave, which is composed of three main components: scale alignment layer, Transformer encoder and channel attention. This section aims to introduce the details of these components. 

**Scale alignment layer.** One of the largest challenges in modeling brain signals by a unified model is the diversity of sampling rates, which leads to inconsistent temporal resolutions. Previous works often address this issue by resampling all the signals into a common frequency. However, such a strategy becomes ineffective when dealing with both iEEG and EEG data. As sampling rates of iEEG and EEG differ greatly, resampling them to a shared scale is not only inflexible but may lead to a loss of signal fidelity. To overcome this problem, we propose a novel embedding approach which maps signals with arbitrary sampling rates into a space with a unified scale. 

The scale alignment layer of BrainWave projects the original signals into latent embeddings, in which each channel is operated independently. Given a single-channel brain recording, we first divided the signal into a series of consecutive non-overlapping 1-second patches **P** _i ∈_ R<sup>_N×P_</sup> , where _N_ is the number of patches, _P_ is the number of timestamps in each 1-second patch, and _i_ is the channel index. Then we calculated the time-frequency representations of each patch, in which we chose the spectrograms with Gaussian window. By keeping the ratio of the window size and the hop size to the patch length _P_ constant, we can align recordings with different sampling rates onto spectrograms with consistent temporal and frequency resolutions. Specifically, we set the window size equal to<sup>_<u>P</u>_</sup> 4<sup>andthehopsizeequalto</sup><sup>_<u>P</u>_</sup> 8<sup>,andtheresulting</sup> spectrograms are denoted as **S** _i ∈_ R<sup>_N×T ×F_</sup> , where _T_ is the length of the time axis and _F_ is the length of the frequency axis. We convolved **S** _i_ using 2D convolutional kernels to obtain the feature maps **M** _i ∈_ R<sup>_N×C_out</sup><sup>_×T_out</sup><sup>_×F_out</sup> , where _C_ out is the output channels and _T_ out _× F_ out is the size of the feature maps. Since our design ensured that data with different sampling rates have the same temporal and frequency resolution, the length of the time axis _T_ out in the resulting feature maps was the same (because the duration of all patches is 1 second), while the length of the frequency axis _F_ out varied. Therefore, we performed padding or truncation on the frequency axis to standardize the size of the feature maps. Then we flattened the standardized feature maps and projected them with a linear layer to derive the input embeddings **E** _i ∈_ R<sup>_N×D_</sup> , where _D_ is the hidden size. 

**Transformer encoder.** The Transformer encoder is composed of stacked Transformer blocks with bidirectional self-attention, which captures the temporal relationship among the patches within a sequence. We first concatenated the input embeddings **E** _i_ with a [CLS] token, then added a set of learnable positional embeddings **PE** _i ∈_ R<sup>(</sup><sup>_N_+1)</sup><sup>_×D_</sup> to obtain the input of the Transformer encoder. Like the embedding layer, the Transformer encoder encoded each channel independently and generated a set of outputs **O** 1 _,_ **O** 2 _, ...,_ **O** _C_ , where _C_ is the number of channels. We derived the whole output **O** _∈_ R<sup>_C×_(</sup><sup>_N_+1)</sup><sup>_×D_</sup> by concatenating the outputs together. **Channel attention.** The channel attention module aims at capturing the correlation between different channels. Specifically, the input **O**<sup>_j_</sup> _∈_ R<sup>_C×D_</sup> _, j_ = 0 _,_ 1 _, ..., N_ 

14 

contained _C_ different patches at the same time, which was then performed with a bidirectional self-attention operation. The output of the channel attention, denoted as **Z** _∈_ R<sup>_C×_(</sup><sup>_N_+1)</sup><sup>_×D_</sup> , served as the latent representation of BrainWave, where **Z**<sup>0</sup> were sequence-level representations (representations of [CLS] tokens) and **Z**<sup>1</sup> _,_ **Z**<sup>2</sup> _, ...,_ **Z**<sup>_N_</sup> were patch-level representations. 

### **4.2 Pretraining** 

**Data curation.** We curated large collections of unannotated electrical brain recordings for pretraining, totaling 13.79 TB data over a duration of 40,907 hours. The iEEG data were obtained from CCEP [55] and a private corpus collected by ourselves, comprising 10.63 TB of data. The recordings spanned a duration of 5231 hours and were collected from 91 subjects, ranging in age from 4 to 51 years. The sampling rate ranged from 1000 Hz to 4096 Hz, and the number of channels varied from 48 to 238. The EEG recordings consisted of CAP [56], HMC [57], Siena [58], SRM [59], TUEG [60], Schizophrenia-81, Sleep-EDF [61], Stroke-50 [62], PD-31 [63], IowaDataset, UNMDataset, AD-184 [64], and a private EEG corpus, with a total of 3.16 TB of data. The recording duration of the data reached 35,675.5 hours and involved 15,906 subjects, ranging in age from less than 1 year to over 90 years. The sampling rate ranged from 100 Hz to 1024 Hz, and the number of channels varied from 1 to 64. 

The preprocessing of the pretraining data primarily involved channel selection and filtering. Due to potential equipment issues during the data collection process, there might be invalid channels where no valid brain signals were captured. Therefore, we needed to perform channel selection, in which we visualized the recordings and manually selected the valid channels. Because data acquisition may be affected by power line interference, we apply a 50 Hz or 60 Hz notch filter to remove power line noise. Since the AC power grid frequency varies across countries and regions (commonly 50 Hz or 60 Hz), the notch filter frequency is determined by the local power line frequency where the data is collected. 

**Pretraining details.** The main backbone of BrainWave is the RoBERTa [65] encoder architecture. The model had a hidden size of 768 and an intermediate size of 2048, with 10 layers and 16 attention heads. We applied absolute positional encoding with a maximum sequence length of 61 (60 signal patches along with a [CLS] token). We pretrained BrainWave on a total of 3,162,233,694 signal patches, including 1,739,447,411 EEG data patches and 1,422,786,283 iEEG data patches. BrainWave was trained using the AdamW optimizer [66], with _β_ 1 = 0 _._ 9, _β_ 2 = 0 _._ 95, _eps_ = 10<sup>_−_5</sup> . For the learning rate scheduling, we utilized a linear warmup of 1000 steps to reach a peak learning rate of 1 _._ 0 _×_ 10<sup>_−_5</sup> , followed by a cosine decay of 30,000 steps to decay the final learning rate to 0. The total training steps of BrainWave was 16,600. We employed gradient accumulation during pretraining, where we accumulated gradients for 16 times of forward and backward before performing a parameter update. The training process was conducted on 4 _×_ A100 GPUs with a global batch size of 2,560,000 (patches) and the entire process took 100 hours. 

15 

### **4.3 Downstream evaluation** 

**Competing methods.** We compared BrainWave to 3 publicly available models: LaBraM [44], BrainBERT [46] and MOMENT [47]. LaBraM is an open-weight model pretrained on more than 2500 hours of EEG data. It tokenized the EEG into discrete tokens by training a neural tokenizer, and was pretrained with symmetric masked modeling. BrainBERT is a reusable, off-the-shelf, subject-agnostic, and electrode-agnostic model that provides embeddings for intracranial recordings. It was pretrained on 43.7 hours of iEEG data recorded from 10 subjects. During pretraining, it masked multiple continuous bands of random frequencies and time intervals in the time-frequency representations. MOMENT is a family of open-source foundation models for generalpurpose time series analysis. It was pretrained on a large collection of publicly available datasets from 13 different domains, which included 20.085 GB ( _≈_ 0 _._ 02 TB) worth of 13 million unique time series and 1.23 billion timestamps (0.15 billion patches). MOMENT also adopted a masked modeling strategy by masking and reconstructing the original time series. 

**Evaluation datasets.** The evaluation benchmark comprised 13 distinct datasets. 

Alzheimer’s disease: AD-65 [67] contains the EEG resting state-closed eyes recordings from 88 subjects in total (44 males, ages 53–79; and 44 females, ages 44–79). For the participants, 36 were diagnosed with Alzheimer’s disease (AD group), 23 were diagnosed with Frontotemporal Dementia (FTD group) and 29 were healthy subjects (CN group). We randomly split the subjects from AD group and CN group into 5 groups. The data comprised 19 channels with a sampling rate of 250 Hz. After processing, we obtained a total of 5349 samples and each sample contains a 10-second data segment. 

Epilepsy: The CHB-MIT [49, 68] database consists of EEG recordings from 22 pediatric subjects (5 males, ages 3–22; and 17 females, ages 1.5–19) with intractable seizures. We randomly split the subjects into 5 groups. The data comprised 23 channels with a sampling rate of 256 Hz. We split the data into 10-second segments and obtained 4148 samples in total. Absence-16, Clonic-6 and Atonic-5 are 3 private datasets that were collected from patients with absence seizures, clonic seizures and atonic seizures, respectively. The annotations were divided into three categories: epileptic waveforms, normal waveforms, and Interictal epileptiform discharge (IED). The recordings comprised 19 channels with a sampling rate of 256 Hz. After processing the data into 4-second segments, we obtained a total of 8016 samples from Absence-16, 2426 samples from Clonic-6, and 1587 samples from Atonic-5. We randomly divided the 16 patients in Absence-16 into 5 groups. The Mayo-Clinic [52] data were collected between 1 AM and 3 AM from 25 patients with DRE undergoing evaluation for epilepsy surgery. The FNUSA [52] dataset is made up of iEEG data collected in awake resting state from 14 patients diagnosed with DRE. We split Mayo-Clinic and FNUSA into 6 and 5 subject groups, respectively. Both Mayo-Clinic and FNUSA were segmented into 3-second data clips and downsampled to 1000 Hz. In order to locate the SOZ, annotations were made for each channel. We preserved the data segments annotated with physiological activity, pathological (epileptic) activity and artifacts. In total, Mayo-Clinic contained 113,260 samples and FNUSA contained 179,629 samples. 

16 

Depression: MDD-64 [53] contains EEG recordings from 64 subjects with 34 of them diagnosed with Major Depressive Disorder (MDD). We randomly split the subjects into 5 groups. The data comprised 19 channels with a sampling rate of 256 Hz. We split the data into 10-second segments and obtained 7309 samples in total. Depression-122 [69] consists of resting EEG data with 122 college-age participants (47 males, ages 18–24; 74 females, ages 18–23; and 1 unknown) with their scores in Beck Depression Inventory (BDI). According to [70], participants with BDI scores _>_ 13 were considered depressed. Healthy controls had stable low BDI scores ( _<_ 7) and no self-reported history or symptoms of anxiety disorder. The data comprised 64 channels with a sampling rate of 500 Hz. We split the data into 10-second segments and obtained 5836 samples in total. 

Schizophrenia: Schizophrenia-28 [48] comprises 14 patients with paranoid schizophrenia and 14 healthy controls. Data were acquired with the sampling frequency of 250 Hz using the standard 10-20 EEG montage with 19 EEG channels. We randomly split the subjects into 5 groups. For the EEG recordings, we split the data into 10-second segments and obtained 5744 samples. Attention deficit hyperactivity disorder (ADHD): ADHD-Adult [50] was collected from 79 participants, including 42 healthy adults and 37 adults with ADHD (age 20-68 years; male/female: 56/23). The dataset contained 256 Hz EEG signals recorded from five channels, including O1, F3, F4, Cz, and Fz, with each subject recorded with two channels. The subjects were randomly split into 5 groups. We split the data into 5- second segments and obtained 5056 samples in total. ADHD-Child [51] contains EEG data collected from 121 children (ages 7-12), including 61 with ADHD and 60 healthy controls. The EEG recordings were performed based on 10-20 standard by 19 channels at 128 Hz sampling frequency. We randomly split the subjects into 5 groups. After processing, we obtained a total of 3322 samples and each sample contains a 5-second data segment. 

Sleep Apnea: Apnea-ECG [71] is an annotated database with 70 nighttime ECG recordings. Each recording included a continuous digitized ECG signal with a sampling rate of 100 Hz. We divided the recordings into 5 groups, split the data into 60-second segments, and obtained 34,271 samples in total. 

**Cross-subject evaluation.** The cross-subject evaluation involved experiments on 10 datasets: AD-65 (Alzheimer’s disease diagnosis), CHB-MIT (seizure detection), Absence-16 (seizure detection), Mayo-Clinic (seizure detection), FNUSA (seizure detection), MDD-64 (MDD diagnosis), Depression-122 (depression diagnosis), Schizophrenia-28 (schizophrenia diagnosis), ADHD-Adult (ADHD diagnosis) and ADHD-child (ADHD diagnosis). We used the AdamW optimizer for fine-tuning, with _β_ 1 = 0 _._ 9, _β_ 2 = 0 _._ 95, _eps_ = 10<sup>_−_5</sup> . For all the models, we fine-tuned the pretrained encoder and the classification head with a learning rate of 1 _×_ 10<sup>_−_5</sup> and 1 _×_ 10<sup>_−_4</sup> . The models were trained for up to 30 epochs, and then the best-performing models on the validation set were selected for testing. 

**Cross-hospital and cross-subtype evaluation.** The cross-hospital evaluation involved Mayo-Clinic and FNUSA, and the cross-subtype evaluation involved Absence16, Clonic-6, and Atonic-5. In the experiments, we fine-tuned the models on the source dataset with a fixed number of epochs and directly evaluated on the target dataset. 

17 

We used the AdamW optimizer, with _β_ 1 = 0 _._ 9, _β_ 2 = 0 _._ 95, _eps_ = 10<sup>_−_5</sup> . We fine-tuned the pretrained encoder and the classification head for 5 epochs with a learning rate of 1 _×_ 10<sup>_−_5</sup> and 1 _×_ 10<sup>_−_4</sup> . 

**Few-shot classification.** The datasets used for few-shot classification were identical to those used for cross-subject evaluation. We classified the queries by comparing with prototypes. Specifically, in _K_ -shot, _M_ -class classification, given the representations of the support set _{_ **u**<sup>_j_</sup> _i_<sup>_|i_=1</sup><sup>_,_2</sup><sup>_, ..., K_;</sup><sup>_j_=1</sup><sup>_,_2</sup><sup>_, ..., M}_,weobtainedtheprototypesfor</sup> each class as the mean of the examples: _{_ **v**<sup>_j_</sup> = _K_ <u>1</u> � _Ki_ =1<sup>**u**</sup> _i_<sup>_j|j_= 1</sup><sup>_,_2</sup><sup>_, ..., M}_.Giventhe</sup> representation of a query **z** _∈_ R<sup>_C×D_</sup> , where _C_ is the number of channels and _D_ is the hidden size, we calculated the channel-wise cosine similarities between the query representation and prototypes: _{_ sim<sup>_j_</sup> = cos( **z** _,_ **v**<sup>_j_</sup> ) _∈_ R<sup>_C_</sup> _|j_ = 1 _,_ 2 _, ..., M }_ . The scores of the query were the mean of channel-wise similarities and we chose the class with the highest score as the prediction: _y_ pred = argmax([ _s_<sup>1</sup> _, s_<sup>2</sup> _, ..., s_<sup>_M_</sup> ]), where _s_<sup>_j_</sup> =<sup>�</sup><sup>_C_</sup> _c_ =1<sup>sim</sup> _c_<sup>_j_.</sup> **SOZ localization.** The SOZ localization was conducted on 4 patients with DRE implanted with 4 to 10 electrodes (47 to 120 channels). The data contain channellevel annotations. The sampling rate is 500 Hz and we split the data into 3-second segments. For a patient experienced _N_ seizures, BrainWave provided channel-level predicted probabilities **p** = _{_ **p**<sup>_c,t_</sup> _i ∈_ [0 _,_ 1] _|i_ = 1 _,_ 2 _..., N_ ; _c_ = 1 _,_ 2 _, ..., C_ ; _t_ = 1 _,_ 2 _, ..., Ti}_ , where _C_ is the number of channels and _Ti_ is the number of segments during _i_ ’th seizure. For each channel, we calculated two metrics based on the predictions: the probability of epileptic discharge occurrence, and the number of times it serves as the seizure onset site. The first metric was obtained by a mean pooling of **p** along the channel axis: <u>�</u> _Ni_ =11<sup>_Ti_</sup> � _Ni_ =1 � _Tt_ =1 _i_<sup>**p**</sup> _i_<sup>_c,t_</sup> _∈_ R<sup>_C_</sup> . The second metric was counted across _N_ seizures. For each seizure, we smoothed the probabilities with median filtering along the time axis. Then we identified the earliest channel(s) that generated epileptic waveforms, defined as: _c_<sup>_∗_</sup> = arg min( _c,t_ ) _∈Si t_ , where _Si_ is the set of ( _c, t_ ) pairs that satisfy MedianFilter( **p**<sup>_c,t_</sup> _i_<sup>)</sup><sup>_≥_0</sup><sup>_._5. We counted the occurrences of each identified channel</sup> across _N_ seizures. **Prediction of clinical assessment scores in AD patients.** The clinical scale scores we predicted in Sec. 2.3 included MMSE, MoCA-B, ROCF, and PSQI. We divided these scores into several discrete ranges. MMSE: 24-30, 21-23, 10-20 and 0- 9. MoCA-B: 26-30, 18-25, 10-17 and 0-9. ROCF: 33-36, 24-32, 18-23, 12-17 and 0-11. PSQI: 0-5, 6-10, 11-15 and 16-21. 

### **4.4 Data Availability** 

This study utilized the following publicly available datasets for downstream benchmarking: AD-65 (https://openneuro.org/datasets/ds004504/versions/1.0.2), CHB-MIT (https://physionet.org/content/chbmit/1.0.0/), Mayo-Clinic (https: //springernature.figshare.com/collections/Multicenter ~~i~~ ntracranial ~~E~~ EG ~~d~~ ataset for ~~c~~ lassification ~~o~~ f ~~g~~ raphoelements ~~a~~ nd ~~a~~ rtifactual ~~s~~ ignals/4681208), FNUSA (https://springernature.figshare.com/collections/Multicenter ~~i~~ ntracranial ~~E~~ EG dataset ~~f~~ or ~~c~~ lassification ~~o~~ f ~~g~~ raphoelements ~~a~~ nd ~~a~~ rtifactual ~~s~~ ignals/4681208), MDD64 (https://figshare.com/articles/dataset/EEG ~~D~~ ata ~~N~~ ew/4244171), Depression-122 (https://openneuro.org/datasets/ds003478/versions/1.1.0, Schizophrenia-28 

18 

(https://repod.icm.edu.pl/dataset.xhtml?persistentId=doi:10.18150/repod.0107441), ADHD-Adult (https://data.mendeley.com/datasets/6k4g25fhzg/1), ADHD-Child (https://ieee-dataport.org/open-access/eeg-data-adhd-control-children), 

### **4.5 Code Availability** 

We will release the model weights, pretraining code, and usage code upon publication. 

## **References** 

- [1] Barborica, A., Mindruta, I., L´opez-Madrona, V.J., Alario, F.-X., Tr´ebuchon, A., Donos, C., Oane, I., Pistol, C., Mihai, F., B´enar, C.G.: Studying memory processes at different levels with simultaneous depth and surface eeg recordings. Frontiers in Human Neuroscience **17** (2023) https://doi.org/10.3389/fnhum.2023. 1154038 

- [2] Jiang, S., Patel, D.C., Kim, J., _et al._ : Spatially expandable fiber-based probes as a multifunctional deep brain interface. Nature Communications **11** (1), 6115 (2020) https://doi.org/10.1038/s41467-020-19946-9 

- [3] Engel, A.K., Moll, C.K., Fried, I., Ojemann, G.A.: Invasive recordings from the human brain: clinical insights and beyond. Nature Reviews Neuroscience **6** (1), 35–47 (2005) 

- [4] Pesaran, B., Vinck, M., Einevoll, G.T., Sirota, A., Fries, P., Siegel, M., Truccolo, W., Schroeder, C.E., Srinivasan, R.: Investigating large-scale brain dynamics using field potential recordings: analysis and interpretation. Nature neuroscience **21** (7), 903–919 (2018) 

- [5] Urai, A.E., Doiron, B., Leifer, A.M., Churchland, A.K.: Large-scale neural recordings call for new insights to link brain and behavior. Nature neuroscience **25** (1), 11–19 (2022) 

- [6] Khodagholy, D., Gelinas, J.N., Thesen, T., Doyle, W., Devinsky, O., Malliaras, G.G., Buzs´aki, G.: Neurogrid: recording action potentials from the surface of the brain. Nature neuroscience **18** (2), 310–315 (2015) 

- [7] Horejs, C.M.: Long-term recording of electrical activity in brain organoids. Nature Reviews Bioengineering **2** , 200 (2024) https://doi.org/10.1038/ s44222-024-00164-7 

- [8] Shih, J.J., Krusienski, D.J., Wolpaw, J.R.: Brain-computer interfaces in medicine. Mayo Clinic Proceedings **87** (3), 268–279 (2012) https://doi.org/10.1016/j. mayocp.2011.12.008 

- [9] Feigin, V.L., Vos, T., Nichols, E., al.: The global burden of neurological disorders: translating evidence into policy. Lancet Neurology **19** (3), 255–265 (2020) https: 

19 

//doi.org/10.1016/S1474-4422(19)30411-9 

- [10] Soufineyestani, M., Dowling, D., Khan, A.: Electroencephalography (eeg) technology applications and available devices. Applied Sciences **10** (21) (2020) https: //doi.org/10.3390/app10217453 

- [11] V¨arbu, K., Muhammad, N., Muhammad, Y.: Past, present, and future of EEGBased BCI applications. Sensors (Basel) **22** (9), 3331 (2022) https://doi.org/10. 3390/s22093331 . Published 2022 Apr 26 

- [12] Jadhav, C., Kamble, P., Mundewadi, S., _et al._ : Clinical applications of EEG as an excellent tool for event related potentials in psychiatric and neurotic disorders. International Journal of Physiology, Pathophysiology and Pharmacology **14** (2), 73–83 (2022). Published 2022 Apr 15 

- [13] Silva, C., Tedesco, S., O’Flynn, B.: Eeg datasets for healthcare: A scoping review. IEEE Access **PP** , 1–1 (2024) https://doi.org/10.1109/ACCESS.2024.3376254 

- [14] Amer, N.S., Belhaouari, S.B.: Eeg signal processing for medical diagnosis, healthcare, and monitoring: A comprehensive review. IEEE Access **11** , 143116–143142 (2023) https://doi.org/10.1109/ACCESS.2023.3341419 

- [15] Yamada, L., Oskotsky, T., Nuyujukian, P., Center, S.C.E., Center, S.P.E.: A scalable platform for acquisition of high-fidelity human intracranial EEG with minimal clinical burden. PLOS ONE **19** (6), 0305009 (2024) https://doi.org/10. 1371/journal.pone.0305009 . Published 2024 Jun 13 

- [16] Dasgupta, D., Miserocchi, A., McEvoy, A.W., Duncan, J.S.: Previous, current, and future stereotactic eeg techniques for localising epileptic foci. Expert Review of Medical Devices **19** , 571–580 (2022) 

- [17] Parvizi, J., Kastner, S.: Promises and limitations of human intracranial electroencephalography. Nature Neuroscience **21** (4), 474–483 (2018) https://doi.org/10. 1038/s41593-018-0108-2 

- [18] Lachaux, J.P., Rudrauf, D., Kahane, P.: Intracranial eeg and human brain mapping. Journal of Physiology-Paris **97** (4-6), 613–628 (2003) 

- [19] Mesk´o, B.: Data annotators are the unsung heroes of medicine’s artificial intelligence revolution. Journal of Medical Artificial Intelligence **3** (0) (2019) 

- [20] Pascual, D., Aminifar, A., Atienza, D.: A self-learning methodology for epileptic seizure detection with minimally-supervised edge labeling. In: 2019 Design, Automation & Test in Europe Conference & Exhibition (DATE), pp. 764–769 (2019). https://doi.org/10.23919/DATE.2019.8714995 

- [21] Zhao, X., Zhao, Q., Tanaka, T., al.: Classification of the epileptic seizure onset 

20 

zone based on partial annotation. Cognitive Neurodynamics **17** (3), 703–713 (2023) https://doi.org/10.1007/s11571-022-09857-4 

- [22] Friedman, D.E., Hirsch, L.J.: How long does it take to make an accurate diagnosis in an epilepsy monitoring unit? Journal of Clinical Neurophysiology **26** (4), 213– 217 (2009) https://doi.org/10.1097/WNP.0b013e3181b2f2da 

- [23] Brown, T.T.: Individual differences in human brain development. Wiley Interdisciplinary Reviews: Cognitive Science **8** (1-2), 1389 (2017) https://doi.org/10. 1002/wcs.1389 

- [24] Yuan, Z., Zhang, D., Yang, Y., Chen, J., Li, Y.: PPi: Pretraining brain signal model for patient-independent seizure detection. In: Thirty-seventh Conference on Neural Information Processing Systems (2023) 

- [25] Clemente-Su´arez, V.J., Redondo-Fl´orez, L., Beltr´an-Velasco, A.I., Ramos-Campo, D.J., Belinch´on-deMiguel, P., Martinez-Guardado, I., Dalamitros, A.A., Y´a˜nezSep´ulveda, R., Mart´ın-Rodr´ıguez, A., Tornero-Aguilera, J.F.: Mitochondria and brain disease: a comprehensive review of pathological mechanisms and therapeutic opportunities. Biomedicines **11** (9), 2488 (2023) 

- [26] McEwen, B.S., Bowles, N.P., Gray, J.D., Hill, M.N., Hunter, R.G., Karatsoreos, I.N., Nasca, C.: Mechanisms of stress in the brain. Nature neuroscience **18** (10), 1353–1363 (2015) 

- [27] Delgado-Morales, R., Ag´ıs-Balboa, R.C., Esteller, M., Berdasco, M.: Epigenetic mechanisms during ageing and neurogenesis as novel therapeutic avenues in human brain disorders. Clinical epigenetics **9** , 1–18 (2017) 

- [28] Gaiteri, C., Ding, Y., French, B., Tseng, G.C., Sibille, E.: Beyond modules and hubs: the potential of gene coexpression networks for investigating molecular mechanisms of complex brain disorders. Genes, brain and behavior **13** (1), 13–24 (2014) 

- [29] Yang, S., Zhang, Z., Chen, H., Meng, Y., Li, J., Li, Z., Xu, Q., Zhang, Q., Fan, Y.-S., Lu, G., _et al._ : Temporal variability profiling of the default mode across epilepsy subtypes. Epilepsia **62** (1), 61–73 (2021) 

- [30] Guo, J., Li, H., Sun, X., Qi, L., Qiao, H., Pan, Y., Xiang, J., Ji, R.: Detecting high frequency oscillations for stereoelectroencephalography in epilepsy via hypergraph learning. IEEE Transactions on Neural Systems and Rehabilitation Engineering **29** , 587–596 (2021) 

- [31] Wang, Y., Yang, Y., Cao, G., Guo, J., Wei, P., Feng, T., Dai, Y., Huang, J., Kang, G., Zhao, G.: Seeg-net: An explainable and deep learning-based cross-subject pathological activity detection method for drug-resistant epilepsy. Computers in Biology and Medicine **148** , 105703 (2022) https://doi.org/10.1016/j.compbiomed. 

21 

2022.105703 

- [32] Chen, J., Yang, Y., Yu, T., Fan, Y., Mo, X., Yang, C.: Brainnet: Epileptic wave detection from seeg with hierarchical graph diffusion learning. In: Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, pp. 2741–2751 (2022) 

- [33] Bagherzadeh, S., Shahabi, M.S., Shalbaf, A.: Detection of schizophrenia using hybrid of deep learning and brain effective connectivity image from electroencephalogram signal. Computers in Biology and Medicine **146** , 105570 (2022) https://doi.org/10.1016/j.compbiomed.2022.105570 

- [34] Sahu, G., Karnati, M., Gupta, A., Seal, A.: Scz-scan: An automated schizophrenia detection system from electroencephalogram signals. Biomedical Signal Processing and Control **86** , 105206 (2023) https://doi.org/10.1016/j.bspc.2023.105206 

- [35] Miltiadous, A., Gionanidis, E., Tzimourta, K.D., Giannakeas, N., Tzallas, A.T.: Dice-net: A novel convolution-transformer architecture for alzheimer detection in eeg signals. IEEE Access **11** , 71840–71858 (2023) https://doi.org/10.1109/ ACCESS.2023.3294618 

- [36] Vicchietti, M.L., Ramos, F.M., Betting, L.E., _et al._ : Computational methods of EEG signals analysis for Alzheimer’s disease classification. Scientific Reports **13** , 8184 (2023) https://doi.org/10.1038/s41598-023-32664-8 

- [37] Sun, X., Xu, Y., Zhao, Y., Zheng, X., Zheng, Y., Cui, L.: Multi-granularity graph convolution network for major depressive disorder recognition. IEEE Transactions on Neural Systems and Rehabilitation Engineering **32** , 559–569 (2024) https: //doi.org/10.1109/TNSRE.2023.3311458 

- [38] Zhou, Y., Chia, M.A., Wagner, S.K., _et al._ : A foundation model for generalizable disease detection from retinal images. Nature **622** , 156–163 (2023) https://doi. org/10.1038/s41586-023-06555-x 

- [39] Chen, R.J., Ding, T., Lu, M.Y., _et al._ : Towards a general-purpose foundation model for computational pathology. Nature Medicine **30** , 850–862 (2024) https: //doi.org/10.1038/s41591-024-02857-3 

- [40] Xu, H., Usuyama, N., Bagga, J., _et al._ : A whole-slide foundation model for digital pathology from real-world data. Nature **630** , 181–188 (2024) https://doi.org/10. 1038/s41586-024-07441-w 

- [41] Pai, S., Bontempi, D., Hadzic, I., _et al._ : Foundation model for cancer imaging biomarkers. Nature Machine Intelligence **6** , 354–367 (2024) https://doi.org/10. 1038/s42256-024-00807-9 

- [42] Zhang, K., Zhou, R., Adhikarla, E., _et al._ : A generalist vision–language foundation 

22 

model for diverse biomedical tasks. Nature Medicine (2024) https://doi.org/10. 1038/s41591-024-03185-2 

- [43] Hao, M., Gong, J., Zeng, X., _et al._ : Large-scale foundation model on single-cell transcriptomics. Nature Methods **21** , 1481–1491 (2024) https://doi.org/10.1038/ s41592-024-02305-7 

- [44] Jiang, W., Zhao, L., Lu, B.-l.: Large brain model for learning generic representations with tremendous EEG data in BCI. In: The Twelfth International Conference on Learning Representations (2024) 

- [45] Zhang, D., Yuan, Z., Yang, Y., Chen, J., Wang, J., Li, Y.: Brant: Foundation model for intracranial neural signal. In: Thirty-seventh Conference on Neural Information Processing Systems (2023) 

- [46] Wang, C., Subramaniam, V., Yaari, A.U., Kreiman, G., Katz, B., Cases, I., Barbu, A.: BrainBERT: Self-supervised representation learning for intracranial recordings. In: The Eleventh International Conference on Learning Representations (2023) 

- [47] Goswami, M., Szafer, K., Choudhry, A., Cai, Y., Li, S., Dubrawski, A.: MOMENT: A family of open time-series foundation models. In: Forty-first International Conference on Machine Learning (2024) 

- [48] Olejarczyk, E., Jernajczyk, W.: EEG in Schizophrenia. https://doi.org/10.18150/ repod.0107441 

- [49] Guttag, J.: CHB-MIT Scalp EEG Database. PhysioNet (2010). https://doi.org/ 10.13026/C2K01R 

- [50] Sadeghi Bajestani, G., Abedian, S., Makhloughi, F., Raoufitabar, M., Saeedi, H.: A Dataset of EEG Signals from Adults with ADHD and Healthy Controls: Resting State, Cognitive function, and Sound Listening Paradigm. Mendeley Data (2023). https://doi.org/10.17632/6k4g25fhzg.1 

- [51] Motie Nasrabadi, A., Allahverdy, A., Samavati, M., Mohammadi, M.R.: EEG Data for ADHD / Control Children. https://doi.org/10.21227/rzfh-zn36 

- [52] Nejedly, P., Kremen, V., Sladky, V., Cimbalnik, J., Klimes, P., Plesinger, F., Mivalt, F., Travnicek, V., Viscor, I., Pail, M., et al.: Multicenter intracranial eeg dataset for classification of graphoelements and artifactual signals. Scientific data **7** (2020) 

- [53] Mumtaz, W.: MDD Patients and Healthy Controls EEG Data (New). figshare. Dataset (2016). https://doi.org/10.6084/m9.figshare.4244171.v2 . https://doi. org/10.6084/m9.figshare.4244171.v2 

23 

- [54] Jo, S., Jung, J.H., Yang, M.J., Lee, Y., Jang, S.J., Feng, J., Heo, S.H., Kim, J., Shin, J.H., Jeong, J., Park, H.S.: Eeg-emg hybrid real-time classification of hand grasp and release movements intention in chronic stroke patients. In: 2022 IEEE International Conference on Rehabilitation Robotics (ICORR), pp. 1–6 (2022). https://doi.org/10.1109/ICORR55369.2022.9896592 

- [55] Blooijs, D., Boom, M.A., Aar, J.F., Huiskamp, G.J.M., Castegnaro, G., Demuru, M., Zweiphenning, W.J.E.M., Eijsden, P., Miller, K.J., Leijten, F.S.S., Hermes, D.: ”CCEP ECoG Dataset Across Age 4-51”. https://doi.org/10.18112/ openneuro.ds004080.v1.2.4 

- [56] Terzano, M.G., Parrino, L., Sherieri, A., Chervin, R., Chokroverty, S., Guilleminault, C., Hirshkowitz, M., Mahowald, M., Moldofsky, H., Rosa, A., Thomas, R., Walters, A.: Atlas, rules, and recording techniques for the scoring of cyclic alternating pattern (cap) in human sleep. Sleep Medicine **2** (6), 537–553 (2001) https://doi.org/10.1016/s1389-9457(01)00149-6 . Erratum in: Sleep Med. 2002 Mar;3(2):185 

- [57] Alvarez-Estevez, D., Rijsman, R.M.: Inter-database validation of a deep learning approach for automatic sleep scoring. PLoS ONE **16** (8), 0256111 (2021) https: //doi.org/10.1371/journal.pone.0256111 

- [58] Detti, P., Vatti, G., Lara, G.: Eeg synchronization analysis for seizure prediction: A study on data of noninvasive recordings. Processes **8** (7) (2020) https://doi.org/ 10.3390/pr8070846 

- [59] Hatlestad-Hall, C., Rygvold, T.W., Andersson, S.: ”SRM Resting-state EEG”. https://doi.org/10.18112/openneuro.ds003775.v1.2.1 

- [60] Harati, A., Lopez, S., Obeid, I., Picone, J., Jacobson, M., Tobochnik, S.: The tuh eeg corpus: A big data resource for automated eeg interpretation. In: 2014 IEEE Signal Processing in Medicine and Biology Symposium (SPMB) (2014) 

- [61] Kemp, B., Zwinderman, A.H., Tuk, B., Kamphuisen, H.A.C., Oberye, J.J.L.: Analysis of a sleep-dependent neuronal feedback loop: the slow-wave microcontinuity of the eeg. IEEE Transactions on Biomedical Engineering **47** (9), 1185–1194 (2000) https://doi.org/10.1109/10.867928 

- [62] Liu, H., Lv, X.: EEG datasets of stroke patients (2022) https://doi.org/10.6084/ m9.figshare.21679035.v5 

- [63] Rockhill, A.P., Jackson, N., George, J., Aron, A., Swann, N.C.: ”UC San Diego Resting State EEG Data from Patients with Parkinson’s Disease”. https://doi. org/10.18112/openneuro.ds002778.v1.0.5 

- [64] Vicchietti, M.L., Ramos, F.M., Betting, L.E., Campanharo, A.S.: Computational methods of eeg signals analysis for alzheimer’s disease classification. Scientific 

24 

Reports **13** (1), 8184 (2023) 

- [65] Liu, Y., Ott, M., Goyal, N., Du, J., Joshi, M., Chen, D., Levy, O., Lewis, M., Zettlemoyer, L., Stoyanov, V.: RoBERTa: A Robustly Optimized BERT Pretraining Approach (2019). https://arxiv.org/abs/1907.11692 

- [66] Loshchilov, I., Hutter, F.: Decoupled Weight Decay Regularization (2019). https: //arxiv.org/abs/1711.05101 

- [67] Miltiadous, A., Tzimourta, K.D., Afrantou, T., Ioannidis, P., Grigoriadis, N., Tsalikakis, D.G., Angelidis, P., Tsipouras, M.G., Glavas, E., Giannakeas, N., Tzallas, A.T.: ”A Dataset of 88 EEG Recordings From: Alzheimer’s Disease, Frontotemporal Dementia and Healthy Subjects”. https://doi.org/10.18112/openneuro. ds004504.v1.0.2 

- [68] Shoeb, A.H.: Application of machine learning to epileptic seizure onset detection and treatment. PhD thesis, Massachusetts Institute of Technology (2009) 

- [69] jcavanagh@unm.edu, J.F.C.: ”EEG: Depression Rest”. https://doi.org/10.18112/ openneuro.ds003478.v1.1.0 

- [70] Chang, J., Choi, Y.: Depression diagnosis based on electroencephalography power ratios. Brain and Behavior **13** (8), 3173 (2023) 

- [71] Penzel, T., Moody, G.B., Mark, R.G., Goldberger, A.L., Peter, J.H.: The apneaecg database. In: Computers in Cardiology 2000. Vol.27 (Cat. 00CH37163), pp. 255–258 (2000). https://doi.org/10.1109/CIC.2000.898505 

25 

## **Appendix A Extended Data** 



<!-- Start of picture text -->
BrainWave LaBraM BrainBERT MOMENT<br>1.0 1.0 P  < 0.001 1.0 P  < 0.001 1.0 P  < 0.001 1.0 P  < 0.001<br>P  < 0.001<br>0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4<br>AD-65 CHB-MIT Absence-16 Mayo-Clinic FNUSA<br>1.0 P  < 0.001 1.0 1.0 P  < 0.001 1.0 P  < 0.001 1.0<br>P  < 0.001 P  < 0.001<br>0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4<br>MDD-64 Depression-122 Schizophrenia-28 ADHD-Adult ADHD-child<br>BACC<br>BACC<br><!-- End of picture text -->

**Fig. A1 Performance of cross-subject tasks.** Bar plots comparing the BACC scores of BrainWave and competing models on cross-subject tasks. Data are mean _±_ SD. Each experiment is conducted with _n_ -fold cross validation ( _n_ is the number of subject groups), where we repeat five runs for each fold. The listed _p_ value indicates the significance for BrainWave outperforming the best comparison model, with the two-sided _t_ -test. 

26 



<!-- Start of picture text -->
a b<br>BrainWave LaBraM BrainBERT MOMENT BrainWave LaBraM BrainBERT MOMENT<br>1.0 P  < 0.001 1.0 P  < 0.001 1.0 1.0<br>0.8 0.8 0.8 0.8<br>P  < 0.001<br>0.6 0.6 P  < 0.001<br>0.6 0.6<br>0.4 0.4<br>0.4 0.4<br>Mayo-Clinic to FNUSA FNUSA to Mayo-Clinic Absence-16 to Clonic-6 Absence-16 to Atonic-5<br>BACC BACC<br><!-- End of picture text -->

**Fig. A2 Performance of cross-hospital and cross-subtype tasks. a,** Bar plots comparing the BACC scores of BrainWave and competing models on cross-hospital tasks. **b,** Bar plots comparing the BACC scores of BrainWave and competing models on cross-subtype tasks. Data are mean _±_ SD. Each experiment is repeated five runs. The listed _p_ value indicates the significance for BrainWave outperforming the best comparison model, with the two-sided _t_ -test. 

27 



<!-- Start of picture text -->
BrainWave LaBraM BrainBERT MOMENT<br>1.0 AD-65 1.0 CHB-MIT 1.0 Absence-16 1.0 1.0 FNUSA<br>0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4<br>3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot<br>1.0 MDD-64 1.0 Depression-122 1.0 Schizophrenia-28 1.0 ADHD-Adult 1.0 ADHD-Child<br>0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4<br>3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot<br>Mayo-Clinic<br>BACC<br>BACC<br><!-- End of picture text -->

**Fig. A3 Performance of few-shot classification.** Box plots comparing the BACC scores of BrainWave and competing models on few-shot classification. We conduct _n_ -fold cross validation for each experiment and repeat five runs per fold. We perform 3-shot and 8-shot classification for each task. 

28 



<!-- Start of picture text -->
BrainWave LaBraM BrainBERT MOMENT<br>1.0 1.0 1.0 1.0 1.0<br>0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4<br>AD-65 CHB-MIT Absence-16 Mayo-Clinic FNUSA<br>1.0 1.0 1.0 1.0 1.0<br>0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4<br>AD-65 CHB-MIT Absence-16 Mayo-Clinic FNUSA<br>1.0 1.0 1.0 1.0<br>0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4<br>MDD-64 Depression-122 Schizophrenia-28 ADHD-Adult ADHD-Child<br>1.0 1.0 1.0 1.0 1.0<br>0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4<br>MDD-64 Depression-122 Schizophrenia-28 ADHD-Adult ADHD-Child<br>AUROC<br>BACC<br>AUROC<br>AUROC<br>BACC<br><!-- End of picture text -->

**Fig. A4 Comparison between few-shot classification with BrainWave and full-label finetuning of competing models.** Box plots comparing the AUROC and BACC scores of BrainWave on 8-shot classification and other pretrained models on full-label fine-tuning. For all the models, we conduct _n_ -fold cross validation in each experiment and repeat five runs per fold. 

29 



<!-- Start of picture text -->
BrainWave LaBraM BrainBERT MOMENT<br>BrainWave LaBraM BrainBERT MOMENT<br>ADHD-Adult<br>MDD-64<br><!-- End of picture text -->

**Fig. A5 t-SNE analysis of few-shot classification.** t-SNE plots of the pretrained representations on ADHD-Adult and MDD-64 generated from BrainWave and other pretrained encoders. Each model contains four subplots, with each subplot generated by randomly sampling a portion of the original dataset. 

30 



<!-- Start of picture text -->
BrainWave BrainWave-iEEG BrainWave-EEG<br>P  < 0.001 P  < 0.001 P  = 0.200 P  = 0.033<br>1.0 1.0 1.0 1.0 1.0<br>P  < 0.001<br>0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4<br>AD-65 CHB-MIT Absence-16 Mayo-Clinic FNUSA<br>1.0 1.0 P  < 0.001 1.0 P  < 0.001 1.0 P  < 0.001 1.0 P  = 0.002<br>P  < 0.001<br>0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4<br>AD-65 CHB-MIT Absence-16 Mayo-Clinic FNUSA<br>P  = 0.003<br>P  < 0.001 P  < 0.001<br>1.0 1.0 P  < 0.001 1.0 1.0 1.0 P  < 0.001<br>0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4<br>MDD-64 Depression-122 Schizophrenia-28 ADHD-Adult ADHD-child<br>1.0 P  = 0.017 1.0 1.0 P  < 0.001 1.0 P  < 0.001 1.0<br>P  < 0.001 P  < 0.001<br>0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4<br>MDD-64 Depression-122 Schizophrenia-28 ADHD-Adult ADHD-child<br>AUROC<br>BACC<br>AUROC<br>BACC<br><!-- End of picture text -->

**Fig. A6 Performance of cross-subject evaluation with BrainWave, BrainWave-EEG and BrainWave-iEEG.** Bar plots comparing the AUROC and BACC scores of BrainWave, BrainWaveEEG and BrainWave-iEEG on cross-subject tasks. Each experiment is conducted with _n_ -fold cross validation ( _n_ is the number of subject groups), where we repeat five runs for each fold. 

31 



<!-- Start of picture text -->
BrainWave BrainWave-iEEG BrainWave-EEG<br>1.0 AD-65 1.0 CHB-MIT 1.0 Absence-16 1.0 Mayo-Clinic 1.0 FNUSA<br>0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4<br>3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot<br>1.0 MDD-64 1.0 Depression-122 1.0 ADHD-Adult 1.0 ADHD-Child 1.0 Schizophrenia-28<br>0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4<br>3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot<br>BACC<br>BACC<br><!-- End of picture text -->

**Fig. A7 Performance of few-shot classification with BrainWave, BrainWave-EEG and BrainWave-iEEG.** Box plots comparing the BACC scores of BrainWave, BrainWave-EEG and BrainWave-iEEG on few-shot classification. We perform 3-shot and 8-shot classification for each task. Data are mean _±_ SD. The listed _p_ value indicates the significance for BrainWave outperforming the best comparison model, with the two-sided _t_ -test. 

32 

