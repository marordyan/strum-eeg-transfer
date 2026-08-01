AdaBrain-Bench: Benchmarking Brain Foundation
Models for Brain-Computer Interface Applications
Jiamin Wu1,2†, Zichen Ren1†, Junyu Wang1,3, Pengyu Zhu1,4,
Yonghao Song1,3, Mianxin Liu1, Qihao Zheng1, Lei Bai1,
Wanli Ouyang1,2*, Chunfeng Song1*
1Shanghai Artificial Intelligence Laboratory.
2The Chinese University of Hong Kong.
3Tsinghua University.
4North China Electric Power University.
*Corresponding author(s). E-mail(s): songchunfeng@pjlab.org.cn;
†These authors contributed equally to this work.
Abstract
Non-invasiveBrain-ComputerInterfaces(BCI)offerasafeandaccessiblemeans
of connecting the human brain to external devices, with broad applications in
homeandclinicalsettingstoenhancehumancapabilities.However,thehighnoise
level and limited task-specific data in non-invasive signals constrain decoding
capabilities.Recently,theadoptionofself-supervisedpre-trainingistransforming
the landscape of non-invasive BCI research, enabling the development of brain
foundationmodelstocapturerobustneuralrepresentationsfromlarge-scaleunla-
beled electroencephalography (EEG) signals. However, despite these advances,
the field currently lacks standard and comprehensive benchmarks to assess the
utilityofthepublicfoundationmodelsacrossdiverseBCItasks,hinderingtheir
widespread adoption. To address this challenge, we present AdaBrain-Bench, a
large-scale standardized benchmark to systematically evaluate brain foundation
models in widespread non-invasive BCI tasks. AdaBrain-Bench encompasses a
diverse collection of representative BCI decoding datasets spanning 7 key appli-
cations. It introduces a streamlined model adaptation pipeline integrated with
multi-dimensional evaluation metrics and a set of adaptation tools for flexi-
bledeployment.Thebenchmarkestablishesmultipletransfersettings,including
cross-subject, multi-subject, and few-shot settings, to rigorously evaluate mod-
els’ transferability across diverse real-world application scenarios. We leverage
AdaBrain-Benchtoevaluatepubliclyavailablebrainfoundationmodelsandoffer
insights into practices for selecting appropriate models in various scenarios. We
1
5202
guA
5
]GL.sc[
2v28890.7052:viXra

make our benchmark pipeline available at GitHub repository to enable repro-
ducible research and external use, offering a continuously evolving platform to
foster progress toward robust and generalized neural decoding solutions.
1 Introduction
Brain-ComputerInterfaces(BCIs)havesparkedsignificantinterestincreatingsystems
that facilitate direct information transmission between human brains and computers
or external devices [1–3]. Over recent decades, several teams have used BCIs to effi-
ciently decode movement [4, 5] and communication [6–10] from electrodes implanted
in the cortex or over its surface. Despite their efficacy, the requirement for invasive
brainsurgerylimitstheapplicabilityofthesedecodingmethodsandthesehigh-quality
signals are difficult to maintain chronically. Several laboratories have thus focused
on non-invasive BCIs that decode brain activity from non-invasive recordings. The
mostpopularnon-invasiveBCItechniqueiselectroencephalography(EEG).EEGpro-
videsmillisecond-levelmonitoringofmacroscopicchangesofelectricsignalselicitedin
the cortex [11–13], offering a safe and potentially wearable approach for neural data
acquisition.Braindecodingtechniques[14]thatinterpretlatentneuralpatternsunder-
lying EEG signals have powered a diverse range of BCI applications, spanning motor
imagery decoding [15], sleep stage classification [16], seizure detection [17], mental
state classification [18, 19] and visual decoding [20].
Traditional brain decoding efforts utilize supervised deep learning techniques for
various BCI tasks, including convolution neural networks (CNN) [2, 29, 30], long
short-termmemory(LSTM)[31–33],andTransformer[27,28,34].Nevertheless,EEG
recordings exhibit an inherent low signal-to-noise ratio and present significant vari-
ability [35, 36]. Moreover, compared to image or text data, the high cost of EEG data
collectionandannotationmakesitchallengingtobuildlarge,high-quality,task-specific
datasets, resulting in data scarcity for certain applications [23, 37]. These challenges
make traditional supervised deep learning-based decoding methods struggle in learn-
ing effective neural representation [37, 38], and limit their generalization ability for
real-world BCI deployment.
To address these challenges, recent efforts have been focusing on adopting
self-supervised pre-training (SSP) to revolutionize brain decoding pipelines. Self-
supervised pre-training algorithms have driven a paradigm shift by enabling deep
neural networks to be trained on vast unlabeled datasets, achieving performance on
parwithsupervisedlearning.Largeneuralnetworkstrainedthiswaycanbedescribed
as foundation models that can be used for diverse downstream tasks with minimal
fine-tuning. SSP is well-suited for developing robust and generalizable brain decod-
ingmodels,asitenablestrainingbrainfoundationmodelsonlargeunannotatedEEG
data from diverse sources. Therefore, SSP for brain decoding has recently garnered
attention,withincreasingefforts[21–24]focusedondevelopingbrainfoundationmod-
els for generalized BCI decoding. Table 7 provides a summary of open-source brain
foundation models. For instance, BIOT [21] proposes a unified tokenizer to encode
2

a
|                     | 13Datasetsfrom7TasksCoveringVariousBCIApplications |                    |     |                           |     | b   |                | TaskParadigms |           |
| ------------------- | -------------------------------------------------- | ------------------ | --- | ------------------------- | --- | --- | -------------- | ------------- | --------- |
|                     |                                                    | EmotionRecognition |     | Clinical AnomalyDetection |     |     | Classification | Regression    | Retrieval |
| VigilanceEstimation |                                                    |                    |     | TUEV/TUAB/Siena           |     |     |                |               |           |
SEED-VIG
SEED
SEED-IV
| WorkloadClassification |     |     | AdaBrain-Bench |     | SleepStaging      | c   |     |           |     |
| ---------------------- | --- | --- | -------------- | --- | ----------------- | --- | --- | --------- | --- |
|                        |     |     |                |     | SleepEDF/SHHS/HMC |     |     | Baselines |     |
EEGMAT
Self-supervisedFoundationModels
|     |     |               |                |     |     |     |                             | BIOT    | EEGPT     |
| --- | --- | ------------- | -------------- | --- | --- | --- | --------------------------- | ------- | --------- |
|     |     |               |                |     |     |     |                             | LaBraM  | CBraMod   |
|     |     | MotorImagery  | VisualDecoding |     |     |     | SupervisedTraditionalModels |         |           |
|     |     | SHU/BCI-IV-2a | Things-EEG     |     |     |     |                             | EEGNet  | LDMA      |
|     |     |               |                |     |     |     |                             | ST-Tran | Conformer |
d
Evaluationof3KeyTransferSettings
Cross-subjectTransferSetting
|     |     |     |     |     | Multi-subjectAdaptationSetting |     |     | Few-shotTransferSetting |     |
| --- | --- | --- | --- | --- | ------------------------------ | --- | --- | ----------------------- | --- |
…
Sub 1
|       |     |     | Sub 4 | Sub 1 |     |     |     | Sub 1 |     |
| ----- | --- | --- | ----- | ----- | --- | --- | --- | ----- | --- |
|       |     |     |       | …     |     |     |     | …     |     |
| Sub 2 |     |     |       |       |     | …   |     |       |     |
Sub 5
| Sub 3 |          |     |         | Sub N |          |         |     | Sub N    |         |
| ----- | -------- | --- | ------- | ----- | -------- | ------- | --- | -------- | ------- |
|       |          |     |         |       | Trainset | Testset |     | Trainset | Testset |
|       | Trainset |     | Testset |       |          |         |     |          |         |
e
FoundationModelAdaptationPipeline
|     |                   |     |     |     | FoundationModel |          |     | AccuracyMetric |     |
| --- | ----------------- | --- | --- | --- | --------------- | -------- | --- | -------------- | --- |
|     | DatasetDataloader |     |     |     |                 | TaskHead |     |                |     |
•Balancedacc/F1-W
|       | • C | r o s s - s u b j e c t tr a n s f | e r          | RepresentationExtraction |     | • C l a | s s i f i c a tion | • A U R | O C / A… U C - P R |
| ----- | --- | ---------------------------------- | ------------ | ------------------------ | --- | ------- | ------------------ | ------- | ------------------ |
| B r a | in  |                                    | S ta n d a r | d iz e d                 |     | • R e g | r e s s i o n      |         |                    |
S ig n a ls • M u l t i- s u b j e c t a d a p t a t ion Dat a P r e p r oc e s sing • R e t r i e v a l Tr a n s fe r a b i li t y Metric
•Few-shottransfer
•Few-shottransferscore
|     |     |     |                   |     | AdaptationStrategy           |     |     | •Cross-subjecttransferscore |     |
| --- | --- | --- | ----------------- | --- | ---------------------------- | --- | --- | --------------------------- | --- |
|     |     |     | Benchmark-defined |     | User-defined User-customized |     |     |                             |     |
Fig.1 OverviewofAdaBrain-Bench.a,categorizationof13benchmarkdatasetsand7bench-
mark tasks ranging from cognitive state assessment, human augmentation, and clinical monitoring.
b, diverse task paradigms including classification, regression, and retrieval paired with comprehen-
siveevaluationmetrics.c,evaluatedbaselinesincludingseveralrecentlyopen-sourcedself-supervised
foundation models (BIOT [21], EEGPT [22], LaBraM [23], and CBraMod [24]) and supervised tra-
ditionalmodels(EEGNet[25],LDMA[26],ST-Tran[27],andConformer[28])usedforcomparison.
d,multifacetedevaluationsettingsincludingcross-subjecttransfer,multi-subjectadaptationandfew-
shottransfersettingstothoroughlyassessmodelsdownstreamtaskgeneralizationabilityinvarious
scenarios.e,theoverallfoundationmodeladaptationpipeline.Usersinputtheirmodeltothebench-
markandbrainsignaldatafromtheirselectedtask.
EEG signals of varying forms into structured segments, enabling efficient cross-data
learning. LaBraM [23] attempts to learn robust EEG representations through masked
signal modeling of discretized EEG tokens during pretraining, achieving consistently
enhanced decoding performance after pretrained on 2,500 hours of EEG data.
DespitetheadvancementsinSSPforgeneralizedbraindecoding,thefieldcurrently
suffersfromthelackoflarge-scaleandstandardizedbenchmarksforassessingtheutil-
ity ofthe brain foundationmodels in abroad rangeof BCItasks. Thedevelopmentof
3

Table1 AcomparativeanalysisfromrepresentativestudiesassessingEEG-basedbrain
decoding.Thecomparedelementsinvolveevaluatedmodels(includingself-supervisedfoundation
andsupervisedtraditionmodels),theevaluationscope(includingtasksfromcognitivestate
assessment,humanaugmentation,andclinicalmonitoring),theevaluationsettings(cross-subject,
multi-subjectandfew-shotsettings)andadaptationstrategies(fullfine-tuneandlinearprobe).
|            |                       |        |                  | E v a l u                  | ationScop e           |                 |                       |             | F i n e - t u n e |
| ---------- | --------------------- | ------ | ---------------- | -------------------------- | --------------------- | --------------- | --------------------- | ----------- | ----------------- |
|            | EvaluatedModels       |        |                  |                            |                       |                 | EvaluationSettings    |             | S t r a t e g y   |
| Study      |                       |        | Co g n i t iv eS | ta te H u m a n            |                       |                 |                       |             |                   |
|            |                       |        | A s s e s sm en  | t Aug m e n t a t i o      | n C linicalMonitoring |                 |                       |             |                   |
|            | FoundationTraditional |        | Workload         | Motor Visual               | Emotion               | ClinicalAnomaly | Sleep Cross-          | Multi- Few- | FullFine-Linear   |
|            | Models                | Models | Classification   | ImageryDecodingRecognition |                       | Detection       | Stagingsubjectsubject | shot        | tune Probe        |
| ALBM[39]   | ✓                     | ✓      |                  | ✓                          |                       |                 | ✓                     | ✓           |                   |
| LibEER[40] |                       | ✓      |                  |                            | ✓                     |                 |                       | ✓           |                   |
|            |                       | ✓      |                  |                            |                       | ✓               |                       | ✓           |                   |
SzCORE[41]
| LaBraM[23]     | ✓   | ✓   |     | ✓   | ✓   | ✓   |     | ✓ ✓ | ✓ ✓   |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
| CbraMod[24]    | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓ ✓ | ✓     |
| EEGPT[22]      | ✓   | ✓   |     | ✓   |     | ✓   | ✓   | ✓ ✓ | ✓ ✓   |
| BIOT[21]       |     | ✓   |     |     |     | ✓   |     | ✓   | ✓     |
| MOABB[42]      |     | ✓   |     | ✓   |     |     |     |     |       |
| AdaBrain-Bench | ✓   | ✓   | ✓   | ✓ ✓ | ✓   | ✓   | ✓   | ✓ ✓ | ✓ ✓ ✓ |
openbenchmarksinnaturallanguageandvisiondomains[43–45]havehadatransfor-
mativeimpactontheresearchcommunity.However,braindecodinglackscomparable
evaluation frameworks. Existing benchmarks [40, 42] are constrained by small scales,
narrow task sets, and limited BCI paradigms. For instance, BIOT [21] focuses exclu-
sively on seizure detection, and does not involve other fundamental BCI tasks such
as motor imagery and cognitive state assessment. The lack of systematic evaluation
restrictsourunderstandingofdecodingmodels’generalizabilityandpracticalapplica-
bility.Morecritically,currentevaluationpracticesforbrainfoundationmodelsexhibit
notableheterogeneity.Theevaluatedtasks/datasets,evaluationsettings,andpipelines
vary widely across studies (see Table 1). Even for identical tasks, the data splitting
strategiesanddatapreprocessingpipelinesareinconsistentacrossstudies,causingsig-
nificantperformancefluctuations.Therefore,theabsenceofastandardizedbenchmark
impedes objective methodology comparisons and thorough evaluation of foundation
models, limiting both reproducible research and cross-application generalization in
BCI systems.
Totacklethesechallenges,thisarticlepresentsAdaBrain-Bench,amulti-tasknon-
invasive BCI benchmark framework to assess the generalizability of brain foundation
modelsacrossdiverseapplicationscenarios.AdaBrain-Benchaddressesexistingbench-
markshortfallsbyadvancingpriorworkinthreedistinctways.Firstly,thebenchmark
transcends the boundary of traditional single-task domains by incorporating a broad
spectrum of representative downstream tasks with varied task paradigms, spanning
cognitivestateassessment,humanaugmentation,andclinicalmonitoringapplications.
Secondly, AdaBrain-Bench offers a modular pipeline for adapting foundation mod-
els to downstream tasks, combining standardized data preprocessing procedures with
flexible adaptation strategies. The pipeline not only facilitates seamless and action-
able downstream deployment of foundation models in a plug-and-play manner, but
alsoprovidesflexibilityforfutureexpansionofemergingalgorithmsandtasks.Finally,
the benchmark establishes a multi-faceted evaluation system to rigorously assess the
generalizationperformanceoffoundationmodelsacrossdiversereal-worldapplication
4

scenarios. The evaluation system defines three distinct settings, namely cross-subject
transfer, multi-subject adaptation and few-shot transfer settings, paired with multi-
level metrics encompassing both accuracy and transferability metrics to capture key
performance indicators of interest. As a whole, AdaBrain-Bench intends to unify the
non-invasiveBCIdecodingcommunityandbrainfoundationmodelresearchtowardsa
standard benchmark framework, offering a continuously evolving platform to support
and accelerate future advancements in the field.
As Figure 1 presents, AdaBrain-Bench contains a curated collection of 13 EEG
datasets from 7 key BCI tasks in classification, regression, and retrieval task
paradigms. To bridge the pipeline gap and enable direct comparisons, the proposed
foundation model adaptation pipeline integrates standardized EEG preprocessing,
a suite of adaptation strategies, specialized task heads and comprehensive metrics,
ensuring broad compatibility across models and datasets. Beyond conventional accu-
racy metrics, we introduce a transfer score to assess the improved transferability
benefit from pretraining. Using this pipeline, we evaluate a bunch of baselines in
cross-subject transfer, multi-subject adaptation and few-shot transfer settings. These
settings target adaptation to multiple unseen subjects, intra-subject variability, and
data-limited scenarios, respectively. We provide a systematic analysis of key factors
affecting brain foundation model’s generalizability in different scenarios, providing
insights for advancing the practice of large-scale EEG pretraining and selecting foun-
dationmodels.WeofferanliveandpubliclyavailablebenchmarkintheofficialGitHub
repository. As new foundation models and datasets are integrated to our benchmark,
we will continuously update our findings to provide the community a comprehensive
view of progress of foundation models in brain decoding.
2 Results
Comprehensive Benchmark for Generalized BCI Decoding
We provide a comprehensive benchmark for evaluating brain foundation models’ gen-
eralizationperformanceon7keyBCIdecodingtasks.Ourbenchmarkincludesdiverse
datasets and covers critical applications in health monitoring, cognitive monitoring,
andhumanaugmentation.TheproposedAdaBrain-Benchframeworkevaluatesseveral
recently published EEG foundation models using self-supervised pretraining and tra-
ditionalnon-foundationmodels.Toensurerobustnessofthestudyresultsandaccount
for dataset variability, we curated 13 public EEG-based brain decoding datasets with
varying electrodes, collected from the task including emotion recognition, workload
classification,vigilanceestimation,motorimageryclassification,visualdecoding,clini-
calanomalydetection,andsleepstaging.Foreffectiveadaptationandfaircomparison,
we established a unified foundation model adaptation pipeline, integrating uniform
data splitting, standardized data preprocessing, various task heads and adaptation
strategies. Systematic evaluations were conducted across three distinct evaluation
settings, namely cross-subject transfer, multi-subject adaptation and few-shot trans-
fer settings. In addition to conventional accuracy metrics, we utilized transferability
metrics for a direct comparison of foundation models’ adaptability to downstream
tasks. In this study, we evaluated several recently published brain foundation models
5

Table 2 Benchmarking results in the cross-subject setting.Thebrainfoundationmodels
arefullyfine-tunedtoadapttodownstreamtasks.Thebestandsecond-bestresultsaremarkedin
darkblueandlightblue,respectively.
| Dataset | Metrics |            | TraditionalModels |             |               |          | EEGFoundationModels |            |             |
| ------- | ------- | ---------- | ----------------- | ----------- | ------------- | -------- | ------------------- | ---------- | ----------- |
|         |         | EEGNet[25] | LDMA[26]          | ST-Tran[27] | Conformer[28] | BIOT[21] | EEGPT[22]           | LaBraM[23] | CBraMod[24] |
|         | B-Acc   | 52.32      | 53.34             | 50.15       | 53.12         | 47.89    | 49.90               | 55.78      | 51.11       |
SEED
|     | F1-W | 49.50 | 52.96 | 48.02 | 50.80 | 47.18 | 46.70 | 53.78 | 50.81 |
| --- | ---- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
SEED-IV B-Acc 34.85 36.32 32.94 34.94 35.06 31.20 40.98 39.36
|        | F1-W  | 28.72 | 35.45 | 33.20 | 33.20 | 33.52 | 29.94 | 40.61 | 38.70 |
| ------ | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| EEGMAT | B-Acc | 63.33 | 64.72 | 57.50 | 73.89 | 73.61 | 61.66 | 85.83 | 88.89 |
|        | AUROC | 67.79 | 69.03 | 65.96 | 75.61 | 84.44 | 63.85 | 94.42 | 95.56 |
SEED-VIG Corr 58.34 57.22 49.19 52.11 62.98 57.83 65.52 60.47
|     | R2    | 26.65 | 11.15 | 3.98  | 2.55  | 27.09 | 23.47 | 25.35 | 2.40  |
| --- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
|     | B-Acc | 47.83 | 36.20 | 31.42 | 44.88 | 42.53 | 25.81 | 54.98 | 47.71 |
BCI-IV-2A F1-W 45.46 32.55 26.84 41.54 39.70 18.52 54.90 46.25
|     | B-Acc | 56.48 | 56.39 | 51.66 | 52.96 | 49.99 | 55.23 | 58.88 | 59.21 |
| --- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| SHU | AUROC | 61.06 | 60.17 | 53.31 | 56.76 | 49.87 | 58.34 | 62.74 | 62.02 |
|     | 2-Way | 82.58 | 80.93 | 84.40 | 69.92 | 57.90 | 77.30 | 84.50 | 83.20 |
Things-EEG
|     | Top-5 | 18.67 | 19.36 | 24.85 | 10.25 | 4.65  | 19.70 | 26.05 | 23.15 |
| --- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
|     | B-Acc | 32.65 | 32.88 | 38.68 | 54.06 | 51.78 | 42.89 | 59.05 | 57.69 |
TUEV
|     | F1-W  | 71.66 | 69.54 | 70.06 | 77.52 | 75.17 | 74.65 | 79.62 | 78.69 |
| --- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
|     | B-Acc | 77.58 | 78.37 | 81.04 | 78.92 | 78.07 | 80.54 | 81.50 | 80.05 |
TUAB
|       | AUC-PR | 86.48 | 86.97 | 90.41 | 87.95 | 86.93 | 89.36 | 90.08 | 89.19 |
| ----- | ------ | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Siena | B-Acc  | 72.29 | 66.37 | 64.37 | 72.87 | 71.67 | 59.54 | 66.03 | 65.12 |
|       | AUC-PR | 33.26 | 41.39 | 31.97 | 41.23 | 49.13 | 28.30 | 42.29 | 51.53 |
| HMC   | B-Acc  | 66.67 | 70.33 | 73.73 | 73.84 | 70.63 | 70.21 | 71.94 | 71.40 |
|       | F1-W   | 67.63 | 76.15 | 77.52 | 77.30 | 74.52 | 74.22 | 74.28 | 72.24 |
| SHHS  | B-Acc  | 61.65 | 65.75 | 68.67 | 68.42 | 72.22 | 66.46 | 71.69 | 73.51 |
|       | F1-W   | 73.79 | 78.64 | 80.88 | 81.15 | 83.56 | 78.43 | 82.90 | 84.00 |
|       | B-Acc  | 48.94 | 58.83 | 69.55 | 61.15 | 64.95 | 60.99 | 68.94 | 69.47 |
Sleep-EDF F1-W 78.11 84.06 86.36 84.07 83.80 84.90 87.28 87.40
Macro-average 56.32 56.73 55.64 58.12 58.42 55.00 64.61 62.66
Table 3 Benchmarking results in the multi-subject setting.Thebestandsecond-best
resultsaremarkedindarkblueandlightblue,respectively.
|     |     |     | TraditionalModels |     |     |     | EEGFoundationModels |     |     |
| --- | --- | --- | ----------------- | --- | --- | --- | ------------------- | --- | --- |
Dataset Metrics
|         |       | EEGNet[25] | LDMA[26] | ST-Tran[27] | Conformer[28] | BIOT[21] | EEGPT[22] | LaBraM[23] | CBraMod[24] |
| ------- | ----- | ---------- | -------- | ----------- | ------------- | -------- | --------- | ---------- | ----------- |
|         | B-Acc | 52.72      | 58.13    | 55.59       | 57.42         | 58.37    | 57.50     | 70.90      | 70.31       |
| SEED    | F1-W  | 53.38      | 58.71    | 55.08       | 57.61         | 58.74    | 58.15     | 71.37      | 70.69       |
|         | B-Acc | 33.82      | 27.17    | 25.50       | 37.62         | 36.19    | 30.57     | 47.63      | 44.20       |
| SEED-IV | F1-W  | 37.25      | 19.42    | 28.71       | 42.13         | 38.67    | 28.31     | 49.14      | 45.58       |
|         | B-Acc | 56.30      | 39.12    | 32.10       | 52.39         | 50.67    | 54.01     | 60.75      | 59.03       |
BCI-IV-2A F1-W 56.30 38.84 28.01 52.39 50.57 53.86 60.71 59.07
|     | B-Acc | 62.17 | 62.94 | 61.41 | 61.31 | 59.16 | 62.87 | 67.90 | 66.47 |
| --- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
SHU
|     | AUROC | 69.15 | 70.18 | 67.25 | 68.42 | 63.28 | 68.11 | 74.58 | 73.16 |
| --- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
Macro-average 52.64 46.81 44.21 53.66 51.96 51.67 62.87 61.06
(BIOT [21], EEGPT [22], LaBraM [23], and CBraMod [24]). We also selected sev-
eralrepresentativetraditionalsuperviseddecodingmodels(EEGNet[25],LDMA[26],
| ST-Tran       | [27], | and Conformer |     | [28]) for comparison. |     |     |     |     |     |
| ------------- | ----- | ------------- | --- | --------------------- | --- | --- | --- | --- | --- |
| Cross-Subject |       | Transfer      |     |                       |     |     |     |     |     |
Substantial inter-subject variability in EEG signals presents a critical challenge for
developing generalizable decoding models. In this study, we introduce a cross-subject
transfer setting where foundation models are finetuned on a subset of subjects and
required to simultaneously generalize to a distinct cohort of previously unseen sub-
jects, testing model’s capacity to capture subject-shared general neural patterns.
Table 2 reports the benchmarking results for brain foundation models and traditional
6

a
b
c d
Fig. 2 Performance comparison of brain foundation models in cross-subject, multi-
subject, and few-shot settings. a, comparison of downstream performance (balanced accuracy)
withdifferentfine-tuningstrategies:linearprobe(linear)andfullfine-tuning(fullft).b,comparisonof
downstreamperformance(balancedaccuracyandweightedF1-score)inmulti-subject(mul-subj)vs.
cross-subject(crs-subj)settingsacrossalldatasets.c,benchmarkingresultsinthefew-shotsetting,
with the few-shot sampling ratio r ranging from [0.02,0.05,0.1,0.3,0.5]. Few-shot fine-tuned results
of foundation models and their trained-from-scratch counterpart (-s) are presented. d, the overall
comparisonoffoundationmodelsacrossmultipleevaluationsettings.Eachboxplotsthedistribution
ofevaluatedresultsacrossallbenchmarkdatasets.
7

supervised models in the cross-subject transfer setting, with foundation models fully
fine-tuned. We observe that foundation models consistently outperform traditional
baselinestrainedfromscratchacrossmetricsonmostofdatasets,claimingthebestor
secondbestresultsonthemajorityoftasks.Forinstance,forEEGMAT(workloadclas-
sification),foundationmodelsclaimhighperformanceofover80%inB-Acc(LaBraM
85.83% and CBraMod 88.89%, respectively), while the best traditional model obtains
accuracy of 73.89%. For SHHS, the SOTA traditional approach had an accuracy of
68.67%,whileBIOTandCBraModachievedhigheraccuraciesof72.22%and73.51%,
respectively. However, for clinical monitoring tasks, including TUAB, Siena, HMC,
andSleep-EDF,foundationmodelsperformcomparableorevenworsethantraditional
models.Forinstance,onSleep-EDF,thebestfoundationmodelresultis69.47%,com-
pared to 69.55% for the best traditional model result. This may be attributed to the
largevolumeofEEGrecordingsintheseclinicalmonitoringdatasets,whichlowersthe
generalization complexity and thus reduces the performance gap. Overall, the macro-
average of primary and secondary metrics show that well-trained foundation models
significantly outperform traditional models, with LaBraM and CBraMod achieving
scores of 64.61% and 62.66%, respectively, compared to 58.12% for the SOTA tra-
ditional model. The results demonstrate that brain foundation models show great
potential for enhancing cross-subject generalization performance.
Amongmodels,LaBraMandCBraModconsistentlyachievedhigherdecodingper-
formancethanothermodels,achievingthebestandsecond-bestMacro-averagescores.
Wehypothesizethatthisisbecausethesemodelsarepretrainedonalargeramountof
data and have better channel adaptability by learning adaptive spatial and temporal
position embeddings. Individual tasks exhibited considerable potential for improve-
ment in the cross-subject transfer setting. Some tasks like emotion recognition (i.e.,
SEED, SEED-IV) and motor imagery (i.e., BCI, SHU) yielded suboptimal perfor-
mance across methods. This can be explained by the greater inherent challenges of
these tasks due to high individual variability in mental states.
Apart from using full fine-tuning strategy for adaptation, we also considered the
linear probe strategy that fine-tunes an additional task head while keeping the whole
pretrained models frozen, offering a computationally efficient adaptation approach.
Figure 2a presents benchmarking results in the cross-subject transfer setting using
linearprobe,comparedwiththefullfine-tuningresults.Resultsdemonstratethatlin-
ear probing remains a challenging setting. Compared to fine-tuning, linear evaluation
consistently yields lower performance across most datasets, including those with lim-
itedsamples(e.g.,EEGMAT).Forinstance,forBCI-IV-2A,CbraModattains47.71%
accuracy with fine-tuning but only 32.32% with linear probing. It is worth noting
that EEGPT demonstrates stronger performance using linear probing compared to
full fine-tuning across certain datasets. For instance, on BCI-IV-2A and HMC, the
linear probing performance is 47.89% and 73.82%, respectively, compared to 25.81%
and 70.21% with full fine-tuning performance. It can be attributed to EEGPT’s large
parametercount(seeTable7)thatincreasestheriskofoverfittingwhenusingthefull
fine-tuningstrategy.Wecaninferthatforlarge-scalefoundationmodel,linearprobing
may better preserve their brainwave representation capabilities.
8

Multi-Subject Adaptation
To evaluate the adaptability of models against intra-subject variability, we introduce
a multi-subject adaptation setting wherein models are trained on EEG data from
multiple subjects and subsequently tested on data from distinct recording trials or
sessions of the same subject cohort. We follow established methodologies [21, 23, 24]
that employ similar within-subject setting to assess model performance on emotion
recognition task (i.e., SEED, SEED-IV) and motor imagery classification task (i.e.,
BCI-IV-2A, SHU). The non-stationarity of EEG signals poses significant challenges
for brain decoding. This is due to variations in factors like electrode placement, the
participant’sphysiologicalstateandenvironmentalconditionsoverdifferentrecording
sessions or trials.
Table 3 reports the decoding performance for brain foundation models and tra-
ditional models in the multi-subject adaptation setting. Hereafter we report linear
probing results for EEGPT given its better performance, while employing full fine-
tuning for other foundation models. The results demonstrate a more consistent trend
across methods compared to the cross-subject transfer setting. We observe notable
differences in the decoding performance that emerged among the foundation models.
LaBraM and CBraMod achieved the top-2 macro-average scores, consistently out-
performing traditional decoding methods across all datasets with an average score
advantageexceeding6points.Forinstance,onSEED,LaBraMandCBraModattained
accuracies of 70.90% and 70.31%, respectively, significantly exceeding the SOTA tra-
ditional model (LDMA 58.13%). In contrast, the multi-subject performance of other
foundation models showed a performance gap compared to traditional models. BIOT
andEEGPTachievedmacro-averagescoresof51.96%and51.67%,respectively,falling
below traditional models such as EEGNet (52.64%) and Conformer (53.66%).
Comparison between Cross-Subject and Multi-Subject Settings.Wefurther
conduct a cross-setting comparison analysis between multi-subject and cross-subject
results.AspresentedinFigure2b,thecross-subjectresultsareconsistentlylowerthan
multi-subject results across models. For example, on SEED, the cross-subject perfor-
mance of LaBraM, CBraMod, and EEGPT are lower than multi-subject performance
by 15%, 19%, and 7%, respectively. Foundation models demonstrated superior gen-
eralization when transferring across sessions than across subjects. These results hint
that inter-subject variability poses a greater challenge for decoding models than the
inter-trial or session variability for the same subjects. Individual variations in brain
anatomy,functionalorganizationandcognitiveexperienceleadtohighlydiverseEEG
signal characteristics, making it exceptionally difficult to develop foundation models
with subject-universal representation capacity. The multi-subject setting could serve
as a crucial baseline for generalization research, acting as a natural upper bound to
quantify the performance drop when attempting to generalize across subjects.
Impact of Pretraining
To explore how self-supervised pretraining strategies impact the performance, we
directly trained foundation models from scratch on downstream datasets without any
pretrainingacrossmulti-subjectandcross-subjectsettings,asshowninFigure3a.We
9

a
b
Fig.3 Impactingfactorsvs.downstreamperformance.a,comparisonofdownstreamperfor-
mance (balanced accuracy) with vs. without the pre-training stage across multi-subject (mul-subj)
and cross-subject (crs-subj) settings. b, the downstream task performance shows a positive correla-
tionwiththenumberofsubjectsinthetrainingsetinthecross-subjectsetting.
can observe that the utilization of pretraining strategies brings substantial improve-
ment across different foundation methods. LaBraM and CBraMod with pretraining
outperform the non-pretrained counterpart by over 10% and 7% in average, respec-
tively. Based on these results, we highlight that large-scale self-supervision through
maskedsignalmodelingcaneffectivelydiscoverfunctionallymeaningfulbrainpatterns
from unlabeled EEG data, improving transferability to different BCI tasks. Notably,
theperformancegainsaretypicallymorepronouncedondatasetswithlimitedscaleof
training data, including BCI-IV-2A and EEGMAT, compared to datasets with large
amount of data, including SHHS, HMC, and TUAB. These results hinted that pre-
trainedfoundationmodelsmaybeparticularlyadvantageousfordata-limiteddatasets.
However,pretrainingstrategiesshowlimitedeffectivenessincertaincases.Anobserva-
tion is that the performance improvement from EEGPT and BIOT pretraining is less
pronounced compared to other methods, with limited improvement on some datasets.
This likely stems from EEGPT’s relatively small pretraining data amount (246 hours
10

ofEEGdata),comparedtoLaBraM(2,500hours)andCBraMod(27,000hours).The
constrainedpretrainingdatasetsizemaycauseinsufficientlearningofuniversalneural
representations, particularly given its significantly larger model architecture (25M vs.
5.8M/4M). This suggests model scaling should be proportional to available training
data. For BIOT, the bottleneck likely stems from its support for fixed 18 channels in
its pretrained version, which is incompatible with downstream tasks such as SEED
and SEED-IV (62 channels), potentially diminishing the spatial cues of downstream
EEG signals.
Few-Shot Transfer
To investigate the models’ generalization capacity in the data-limited scenario, we
design a few-shot transfer setting where the models are fine-tuned with a small set of
training data from the downstream task. For each dataset, a subset of the training
data is used as the support set for training, with the sampling ratios r ranging from
[0.02,0.05,0.1,0.3,0.5]. Figure 2c presents the decoding performance in the few-shot
transfer setting, with the full-data performance (i.e., r =1) also presented. The few-
shot performance consistently lags behind the full-data performance by a significant
margin, especially for emotion recognition tasks (SEED and SEED-IV). The accura-
cies exhibit a clear upward trend as the amount of training data increases. For motor
imagery classification datasets (SHU and BCI-IV-2A), the accuracy rapidly grows
with just a few dozen additional samples. For emotion recognition datasets (SEED,
SEED-IV), the trend of performance improvement gradually slows down. On SEED-
IV, EEGPT’s performance is significantly lower than other methods across few-shot
ratios, achieving an accuracy of 27.93% at r =0.5 compared to BIOT’s 37.36%, indi-
catingpotentialoverfittinginhigh-parametermodels.Weobservethatthefoundation
model’s performance lead compared to models without pretraining is pronounced in
the data-limited settings. On SEED, CBraMod outperforms non-pretrained version
by10%,12%whenr =[0.05,0.1],andby3%whenusingthefullsetofdata.OnBCI-
IV-2A, CBraMod achieves gains of 14.09% when using 33% training data compared
to models trained from scratch. These findings suggest that the employment of self-
supervised pretraining could enhance the generalizability of foundation models when
only limited EEG recordings are available.
Quantitative Assessment of the Transferability
Wehavepreviouslyhintedattheimprovedtransferabilityofthefoundationmodelvia
the use of a self-supervised strategy. We further quantify the enhanced transferability
of the foundation models by introducing the transfer score (TS), which is defined
astherelativeimprovementofthepretrainedfoundationmodeloveritstrained-from-
scratch counterpart (see Methods Section for more details). Table 4 presents the TS
inthecross-subjecttransferandfew-shottransfersettings.Self-supervisedfoundation
models show positive transferability in most cases and exhibit distinct advantages
in different settings. CBraMod exhibits superior transfer scores under the few-shot
transfer setting. This may be attributed to its adoption of input-conditioned channel
embedding that adapts flexibly to datasets with varying channel configurations, a
challenge that becomes more pronounced under few-shot constraints.
11

| Table 4 The | transfer | score in various | settings.ThetablepresentstheTSinthe |     |     |
| ----------- | -------- | ---------------- | ----------------------------------- | --- | --- |
cross-subjecttransfersetting(Cross-subjectTS)andthefew-shottransfersetting(Few-shotTS)
withdifferentfew-shotsamplingratios.Thebolddenotesthebestresults.
Few-shotTS
| Method      |           | Cross-subjectTS |               |                |         |
| ----------- | --------- | --------------- | ------------- | -------------- | ------- |
|             |           |                 | 0.02 0.05     | 0.1 0.3        | Average |
| BIOT[21]    |           | 0.0264          | 0.0402 0.0111 | 0.0683 -0.3489 | -0.0573 |
| EEGPT[22]   |           | 0.0764          | 0.0209 0.1159 | 0.0651 0.1135  | 0.0789  |
| LaBraM[23]  |           | 0.2373          | 0.1092 0.1231 | 0.1783 0.2987  | 0.1773  |
| CBraMod[24] |           | 0.1391          | 0.1937 0.2315 | 0.3096 0.3695  | 0.2761  |
| Impact      | of Number | of Training     | Subjects      |                |         |
Given the challenge of cross-subject transfer setting, how to increase cross-subject
performance is a critical issue. We thus assess how the number of subjects used in
training can impact the model’s ability to generalize to new subjects. We fine-tune
LaBraM and CbraMod with different numbers of subjects, denoted as N , in the
subj
cross-subject transfer setting. Datasets with a large amount of subjects were selected
for this experiment, including HMC and SHHS. These two datasets are both sleep
staging datasets, including 120 and 263 subjects, respectively. To isolate the effect of
sample amount on the performance, we keep identical sample counts per epoch for
each dataset. The results with varying N are reported in Figure 3b. We observe
subj
a steady improvement in cross-subject decoding accuracies on unseen subjects as the
number of training subjects increases in the early phase. When trained on a limited
number of subjects, model performance is consistently unsatisfactory across methods
and datasets compared to training with all subjects. For instance, on HMC, utilizing
only two subjects leads to 10.75% and 18.19% lower performance for LaBraM and
CbraMod, respectively, compared to using 20 subjects. On SHHS, CbraMod attains a
balanced accuracy of 40.70% with a single subject, while demonstrating a substantial
23.09% increase in performance when 40 subjects are used for training. Performance
tendstoplateauatapproximately40subjectsonbothHMCandSHHS.AfterN =
subj
40, further increasing training subjects provides only marginal gains. These findings
suggest that expanding the training cohort size may be an effective way to enhance
| cross-subject | generalization   | performance. |     |     |     |
| ------------- | ---------------- | ------------ | --- | --- | --- |
| Impact        | of Normalization |              |     |     |     |
Duetotheinherentnon-stationarityandhighnoisesinEEGsignals,thesignalnormal-
ization techniques may have a non-negligible influence on decoding. The distribution
gap between pretrained datasets and downstream tasks may further exacerbate this
impact. Various normalization choices have been utilized in previous task-specific
methods, such as z-score [22], unit rescale [23], and 95-percentile normalization [21].
How to select the optimal normalization strategy becomes a critical problem when
adapting foundation models to downstream tasks. Thus, we studied the impact of
different normalization choices, including z-score, 95-percentile, and unit rescale
normalization. Z-score normalization standardizes the EEG data X by subtracting
themean(µ)anddividingitbythestandarddeviation(σ),resultinginadistribution
withzeromeanandunitvariance.95-percentilenormalizationusesthe95-percentileof
12

Table 5 Decoding performance across various normalization techniques.Westudiedthe
impactofthreecommonly-usednormalizationchoices,includingz-score,95-percentile,andunit
rescalenormalization.ForSEED,SEED-IV,BCI-IV-2A,andSHU,wefollowedthemulti-subject
settingforevaluation.Theremainingdatasetswereevaluatedusingcross-subjectsetting.BIOT,
LaBraMandCBraModareevaluatedunderfullfine-tuningsetting.Thebestperformanceforeach
modelishighlightedinbold.
| Dataset | Metrics     | BIOT[21]      |         | LaBraM[23]                |                     | CBraMod[24]   |         |
| ------- | ----------- | ------------- | ------- | ------------------------- | ------------------- | ------------- | ------- |
|         | UnitRescale | 95-percentile | Z-Score | UnitRescale 95-percentile | Z-Score UnitRescale | 95-percentile | Z-Score |
|         | B-Acc 57.59 | 59.31         | 58.37   | 70.94 71.91               | 70.90               | 65.95 67.33   | 70.31   |
SEED
|     | F1-W 57.79 | 59.79 | 58.74 | 71.22 72.26 | 71.37 | 66.41 67.82 | 70.69 |
| --- | ---------- | ----- | ----- | ----------- | ----- | ----------- | ----- |
SEED-IV B-Acc 35.61 33.72 36.19 46.80 47.92 47.63 39.87 36.92 44.20
|     | F1-W 35.14  | 34.12 | 38.67 | 48.59 49.23 | 49.14 | 36.89 37.33 | 45.58 |
| --- | ----------- | ----- | ----- | ----------- | ----- | ----------- | ----- |
|     | B-Acc 72.50 | 70.55 | 73.61 | 85.83 77.50 | 85.83 | 76.94 75.83 | 88.89 |
EDMAT AUROC 83.57 75.62 84.44 94.32 86.26 94.42 86.29 83.95 95.56
|     | Corr 52.27 | 52.59 | 62.98 | 64.00 69.09 | 65.52 | 47.51 51.43 | 60.47 |
| --- | ---------- | ----- | ----- | ----------- | ----- | ----------- | ----- |
SEED-VIG R2 17.67 8.65 27.09 10.86 41.47 25.35 -17.19 4.29 2.40
|     | B-Acc 50.05 | 48.89 | 50.67 | 60.24 57.38 | 60.75 | 57.46 56.38 | 59.03 |
| --- | ----------- | ----- | ----- | ----------- | ----- | ----------- | ----- |
BCI-IV-2A
|     | F1-W 49.92 | 48.82 | 50.57 | 60.19 57.35 | 60.71 | 57.41 56.37 | 59.07 |
| --- | ---------- | ----- | ----- | ----------- | ----- | ----------- | ----- |
SHU B-Acc 54.70 59.16 50.36 66.01 67.90 65.25 64.24 66.47 64.12
|     | AUROC 56.62 | 63.28 | 49.61 | 72.22 74.58 | 71.50 | 70.53 73.16 | 70.42 |
| --- | ----------- | ----- | ----- | ----------- | ----- | ----------- | ----- |
|     | B-Acc 50.31 | 47.12 | 51.78 | 60.33 56.41 | 59.05 | 58.50 56.38 | 57.69 |
TUEV F1-W 76.57 74.85 75.17 81.35 78.16 79.62 79.06 77.62 78.69
|     | B-Acc 78.03 | 78.94 | 78.07 | 81.29 80.32 | 81.50 | 80.45 79.79 | 80.05 |
| --- | ----------- | ----- | ----- | ----------- | ----- | ----------- | ----- |
TUAB
|     | AUC-PR 86.77 | 87.85 | 86.93 | 89.64 88.92 | 90.08 | 89.39 88.68 | 89.19 |
| --- | ------------ | ----- | ----- | ----------- | ----- | ----------- | ----- |
Siena B-Acc 62.53 60.31 71.67 57.36 56.36 66.03 69.75 52.07 65.12
|     | AUC-PR 38.16 | 25.64 | 49.13 | 46.54 38.95 | 42.29 | 51.81 26.57 | 51.53 |
| --- | ------------ | ----- | ----- | ----------- | ----- | ----------- | ----- |
HMC B-Acc 71.78 72.57 70.63 71.43 71.83 71.94 71.72 73.27 71.40
|     | F1-W 75.75  | 76.28 | 74.52 | 73.57 72.25 | 74.28 | 72.90 74.02 | 72.24 |
| --- | ----------- | ----- | ----- | ----------- | ----- | ----------- | ----- |
|     | B-Acc 72.14 | 71.87 | 72.22 | 71.57 69.87 | 71.69 | 73.86 69.93 | 73.51 |
SHHS F1-W 83.34 83.01 83.56 81.87 79.19 82.90 83.71 80.09 84.00
|     | B-Acc 63.59 | 56.55 | 64.95 | 67.87 68.50 | 68.96 | 69.09 69.53 | 69.47 |
| --- | ----------- | ----- | ----- | ----------- | ----- | ----------- | ----- |
Sleep-EDF
|     | F1-W 83.33 | 83.88 | 83.80 | 86.54 87.27 | 87.29 | 85.84 87.39 | 87.40 |
| --- | ---------- | ----- | ----- | ----------- | ----- | ----------- | ----- |
theabsoluteamplitudetonormalizeeachchannel.Unitrescalenormalizationdirectly
rescales the unit magnitude of the signal to ensure most values fall within the range
of approximately [-1,1]. As reported in Table 5, our results indicate that z-score turns
outtobearobustnormalizationstrategy,generallyyieldingbetterperformanceacross
themajorityofdatasets.Z-scoreensuresscaleinvarianceanddemonstratesanadvan-
tageinhandlingnon-stationaryprocesses.However,indatasetsexhibitingsubstantial
outliers (e.g., SHU), 95-percentile normalization demonstrates better performance.
This rank-based normalization enhances robustness to outliers by reducing reliance
on extreme values, making it suitable for datasets containing such anomalies.
3 Discussions
Self-supervisedpretrainedfoundationmodelshavethepotentialtorevolutionizebrain
decoding techniques for non-invasive BCI systems. Brain foundation models trained
on large-scale EEG recordings are showing a clear benefit compared to traditional
supervised models in terms of generalizability in various settings. While there is
still much work to be done towards adapting decoding models to downstream real-
world BCI systems, the emergence of foundation models will likely become pivotal to
future advances. As more and more foundation models are trained, a comprehensive
benchmark including wide-ranging tasks and a unified evaluation pipeline becomes
essential for both researchers training foundation models and looking to apply these
13

pretrainedfoundationmodelsondownstreamtasks.Developingnewfoundationmod-
els requires substantial resources, making it essential to build upon previous efforts.
A well-designed benchmark can provide insights for improving pretraining and mod-
els in the future. For downstream BCI applications, such benchmarks can guide the
model selection by systematically evaluating performance across various tasks and
experimental conditions. In this work, we presented AdaBrain-Bench, a comprehen-
sive benchmark focusing on 13 brain decoding datasets. We provided a benchmark
study of publicly available brain foundation models to investigate their generalization
performance in cross-subject transfer, multi-subject adaptation, and few-shot trans-
fer settings. Importantly, the evaluated data covers a wide range of BCI applications,
spanning cognitive state assessment, human augmentation, and clinical monitoring.
The benchmark code and instructions are provided in GitHub repository.
Pre-trained brain foundation models show significant potential to improve cross-
subject generalization across BCI applications. LaBraM [23] and CBraMod [24]
demonstrate good transferability across various datasets and BCI tasks (see Table 2),
whichcanbeexplainedbytheirself-supervisedpretrainingthatcaneffectivelyextract
meaningful features from large, heterogeneous EEG data. As evidenced in Figure 3a,
theadoptionofpretrainingstrategiesconsistentlyenhancesperformanceacrossdiverse
foundation models and datasets. Besides large-scale pretraining, anotherreason could
be their better channel compatibility enabled by flexible channel coverage and adap-
tive spatial-temporal position embeddings. EEG datasets present significant channel
variability, and the gap between pretrained channels and downstream channels may
leadtoneuralpatternmissing.Overall,large-scaleanddiversepretrainingdatasources
and high compatibility with heterogeneous EEG configurations are crucial for strong
foundation models. Despite the improvement, individual tasks still have significant
roomforcross-subjectgeneralizationimprovement.Onsometaskslikeemotionrecog-
nition (i.e., SEED, SEED-IV) and motor imagery (BCI, SHU), foundation models
exhibit suboptimal performance and require further improvement before being avail-
able for real-world usage. We hypothesize that cross-subject generalization challenges
stem from highly individual neural responses shaped by personal experiences and
mental imagery in these tasks, which introduce inherent subjectivity and complicate
the identification of neural patterns across subjects. In contrast, clinical monitoring
tasks like sleep stage classification and clinical anomaly detection show comparably
higher performance, as they present more consistent cross-subject EEG patterns that
serve as good biological markers. Consequently, there is an urgent need to develop
better cross-subject decoding models, either to improve pretraining strategy to learn
subject-sharedpatterns,ortodevelopefficientlearningstrategiesforfastcross-subject
adaptation. As an initial attempt, we investigated whether the subject number could
impact the cross-subject performance. The results in Figure 3b suggest that expand-
ing the training cohort size may effectively improve the adaptability of foundation
models across subjects.
In the multi-subject adaptation setting, the performance of certain foundation
models also generally surpasses traditional models. This underscores the good adapt-
ability of foundation models in handling EEG’s inherent non-stationarities of the
same subject cohort. We also conduct cross-setting comparison analysis. As shown
14

in Figure 2b, the cross-subject results consistently lag behind multi-subject results,
which further confirms the generalization difficulty in cross-subject transfer setting.
Thisindicatesthatinter-subjectvariabilitypresentsagreaterchallengeforfoundation
models than inter-trial or session variability of the same subject cohort.
Comparedtomulti-subjectandcross-subjectsettings,few-shottransferpresentsa
greater generalization challenge. Current models show substantial performance gaps
between few-shot and full-data conditions, as shown in Figure 2c, underscoring the
needforfoundationmodelswithmorerobustandgeneralizableneuralrepresentations.
We can also observe significantly better performance from foundation models com-
pared to their non-pretrained counterparts in few-shot setting. This advantage likely
stems from their ability to transfer knowledge acquired during large-scale pretraining
to novel tasks with limited data. We further quantify models’ transferability via the
transferscoreoverthenon-pretrainedcounterpartacrosssettings,asshowninTable4.
Results suggest that large-scale self-supervised pretraining, when combined with flex-
ible handling of channel variability, could consistently enhance the transferability of
neural decoding models in both cross-subject and few-shot transfer settings.
We systematically investigated key factors affecting the downstream task per-
formance. Regarding adaptation strategies, the results in Figure 2a reveal that full
fine-tuning yields superior performance for most models compared to linear prob-
ing. While the latter offers stronger computational efficiency, the current foundation
models are not prepared for direct generalization with frozen representations. While
self-supervised learning captures meaningful representations, they often lack linear
separability without full fine-tuning. A promising solution could be extensive pre-
training with combined model and data scaling to learn more generalizable neural
representations. For large-scale models like EEGPT, linear probing proves to be a
moreeffectiveadaptationstrategy,asit mitigatestherisk ofover-fittingof whenfine-
tuningonlimitedEEGdata.Regardingthenormalizationtechniques,ourresults(see
Table5)indicatethatz-scorenormalizationisthemostrobustpreprocessingstrategy
for aligning downstream data with foundation model representations.
Thisstudyhasseverallimitationsthatshouldbeacknowledged.Duetotherapidly
evolving nature of this field, our study cannot cover all tasks and models. Instead,
we focus on establishing baseline performance for key BCI applications using rep-
resentative models, while ensuring full transparency through publicly released data,
evaluation pipelines, and code. This enables downstream users to fairly benchmark
newfoundationmodelsandassociatedmethods,helpingthemtodeterminetheappli-
cability of foundation models in their specific use cases. Future work will prioritize
inclusivity by expanding the scope to incorporate a wider range of foundation models
and BCI tasks.
4 Methods
Benchmark Tasks
To comprehensively evaluate the EEG foundation models, AdaBrain-Bench selects
7 popular tasks in EEG-based BCIs, covering critical applications in cognitive state
assessment (i.e., emotion recognition, workload classification, vigilance estimation),
15

human augmentation (i.e. motor imagery classification, visual decoding), and clinical
monitoring(i.e.,clinicalanomalydetection,sleepstaging),rangingfrompassiveBCIs
toactiveBCIs.Thefollowingsectionsprovideadetailedintroductionofinvolvedtasks
and datasets. Table 6 summarizes the downstream BCI tasks and datasets currently
included in AdaBrain-Bench.
Emotion Recognition aims at decoding human emotional experiences by recogniz-
ing human emotional states via EEG analysis, enabling early detection of emotional
disorders. This task leverages the SEED [46] and SEED-IV [47] datasets, which
both compromise EEG recordings collected from 15 participants exposed to emotion-
evoking video stimuli. The SEED dataset classifies emotional responses into three
categories: negative, neutral, and positive. The SEED-IV dataset provides a more
granular classification, categorizing EEG signals into neutral, sad, fearful, and happy
states. Both datasets contain EEG recordings acquired from 62 channels.
Workload Classification aims to assess cognitive load by analyzing EEG signals
collected from subjects under varying mental demands, facilitating real-world appli-
cations in cognitive training and early detection of cognitive fatigue in high-stakes
environments. This task is based on EEGMAT dataset [48, 49], which comprises
19-channel EEG recordings collected from 36 participants engaged in mental arith-
metictasks.Thedatasetprovidesbinarylabelsthatdistinguishbetweenrestingstates
(low-load) and mental arithmetic working states (high-load).
Vigilance Estimation aims to measure fatigue levels from EEG signals, enabling
real-time monitoring of individuals in high-risk environments and helping prevent
fatigue-related accidents. This task is based on SEED-VIG dataset [50]. 21 sub-
jects were instructed to perform simulated driving tasks, during which they gradually
transitioned from vigilance to fatigue. EEG signals were recorded from 17 channels
throughoutthetask,andfatiguelevelswereannotatedusingthePERCLOSindicator
obtained from SMI eye-tracking glasses.
Motor Imagery Classificationaimsatdecodingtheintendedmotormovementsby
analyzing brain activity from EEG signals during the motor imagery process, where
the decoded signals can be leveraged for controlling external devices for individuals
with movement disorders. This task leverages the BCI Competition IV-2A(BCI-IV-
2A) dataset [51] and SHU dataset [52]. BCI-IV-2A contains 22-channel EEG signals
collected from 9 subjects, capturing 4 classes of motor imagery: left hand, right hand,
feet, and tongue. SHU dataset consists of 32-channel EEG signals from 25 subjects,
including two motor imagery tasks: left hand and right hand.
VisualDecodingaimsatdecodingthevisualexperiencethatindividualsperceivedor
imaginedfrombrainactivity[20].Forthistask,weutilizetheThings-EEGdataset[53,
54], which comprises 63-channel EEG recordings from 10 subjects viewing 16,540
images across various object categories. We follow previous work [55] to adopt an
EEG-based image retrieval task to evaluate the decoding performance.
Clinical Anomaly Detection focuses on identifying irregular patterns in brain
activity to support the clinical diagnosis, monitoring of neurological conditions,
and early identification of neurological disorders through EEG analysis. We select
TUEV [56], TUAB [56], and Siena [49, 57] datasets containing EEG signals col-
lected from clinical patients from the Temple University Hospital (TUH) and Unit
16

Table 6 Summary of downstream BCI tasks and datasets currently included in
AdaBrain-Bench.Foreachdataset,wepresentitsprimaryandsecondaryaccuracymetrics.
| Application |     |     | Sampling |     |     | Primary Secondary |
| ----------- | --- | --- | -------- | --- | --- | ----------------- |
Domain Task Dataset Rate #Channel Duration #Subj #Samples Metric Metric
|                | Emotion     | SEED[46]    | 1,000Hz | 62 1s | 15 144,852 | B-Acc F1-W |
| -------------- | ----------- | ----------- | ------- | ----- | ---------- | ---------- |
|                | Recognition | SEED-IV[47] | 1,000Hz | 62 1s | 15 151,845 | B-Acc F1-W |
| CognitiveState | Workload    |             |         |       |            |            |
Assessment Classification EEGMAT[48,49] 500Hz 19 4s 36 1,080 B-Acc AUROC
Vigilance
|     | Estimation   | SEED-VIG[50]  | 200Hz | 17 8s | 21 20,355 | Corr R2    |
| --- | ------------ | ------------- | ----- | ----- | --------- | ---------- |
|     | MotorImagery | BCI-IV-2A[51] | 250Hz | 22 4s | 9 5,184   | B-Acc F1-W |
Human Classification SHU[52] 250Hz 32 4s 25 11,988 B-Acc AUROC
| Augmentation | Visual |                   |         |       |            |             |
| ------------ | ------ | ----------------- | ------- | ----- | ---------- | ----------- |
|              |        | Things-EEG[53,54] | 1,000Hz | 63 1s | 10 821,600 | 2-Way Top-5 |
Decoding
|     |     | TUEV[56] | 256Hz | 23 5s | 370 112,237 | B-Acc F1-W |
| --- | --- | -------- | ----- | ----- | ----------- | ---------- |
ClinicalAnomaly
|          | Detection | TUAB[56]     | 250/256/512Hz | 23 10s | 2,383 409,083 | B-Acc AUC-PR |
| -------- | --------- | ------------ | ------------- | ------ | ------------- | ------------ |
| Clinical |           | Siena[49,57] | 512Hz         | 29 10s | 14 51,307     | B-Acc AUC-PR |
Monitoring
|     |              | HMC[49,58]       | 256Hz | 4 30s | 151 137,243 | B-Acc F1-W |
| --- | ------------ | ---------------- | ----- | ----- | ----------- | ---------- |
|     | SleepStaging | SHHS[59,60]      | 125Hz | 1 30s | 329 324,854 | B-Acc F1-W |
|     |              | Sleep-EDF[49,61] | 100Hz | 2 30s | 78 414,961  | B-Acc F1-W |
of Neurology and Neurophysiology of the University of Siena, respectively. TUEV
includes 23-channel EEG recordings from 370 subjects and distinguishes EEG signals
into 6 event types associated with seizures, including spike and/or sharp wave, gen-
eralized periodic epileptiform discharge, periodic lateralized epileptiform discharge,
eye movement, artifact, and background. TUAB contains EEG recordings from 2383
subjects and classifies EEG recordings as clinically normal or abnormal activities.
Siena includes 29-channel EEG recordings from 14 subjects, with recordings labeled
| as seizure | or non-seizure | events. |     |     |     |     |
| ---------- | -------------- | ------- | --- | --- | --- | --- |
Sleep Staging, also referred to as sleep stage classification, identifies different sleep
stages based on individual’s EEG signals recorded during sleep, enabling early detec-
tion of sleep disorders and facilitating personalized healthcare solutions. This task
|     |     |     |     | HMC | SHHS |     |
| --- | --- | --- | --- | --- | ---- | --- |
adopts commonly used sleep staging benchmarks, [49, 58], [59, 60] and
Sleep-EDF[49,61]datasets.ThesedatasetscategorizeEEGsignalsintosleepstages
inaccordancewiththeAASMstandard[62]:REM,N1,N2,N3,andWake.Specifically,
HMCcontains4-channelEEGrecordingsfrom151subjects;SHHSprovides2-channel
EEG recordings from 6,441 subjects; and Sleep-EDF includes 2-channel EEG record-
ingsfrom78subjects.Following[63],weselected329healthysubjectsfromSHHSand
| used EEG   | signals  | recorded from | the C4-A1 | channel. |     |     |
| ---------- | -------- | ------------- | --------- | -------- | --- | --- |
| Evaluation | Settings |               |           |          |     |     |
To provide a multifaceted analysis of brain foundation model’s transferability to BCI
tasks, we design three distinct evaluation settings: cross-subject transfer, multi-
subject adaptation, and few-shot transfer. These settings systematically assess
the model’s generalization ability when adapting to downstream BCI tasks in diverse
| application | scenarios. |     |     |     |     |     |
| ----------- | ---------- | --- | --- | --- | --- | --- |
Cross-Subject Transfer Setting. This setting trains or fine-tunes models on EEG
datafromagroupofsubjectsandteststhemonnewsubjectswhosedataisexplicitly
excludedfromtraining.Thissettingistoevaluatethegeneralizationabilityofmodels
acrossadiverserangeofindividuals.Giventheinherentandpervasiveinter-individual
17

variability in brain anatomy, functional organization, and skull conductivity, effective
cross-subject generalization is a critical challenge.
Multi-Subject Adaptation Setting. Models are trained on EEG data from mul-
tiple subjects and tested on data from the same subject cohort but from different
recording sessions or trials. This setting assesses the model’s robustness to intra-
subject temporal variability in EEG signals, which is crucial for generalizing across
sessions/trialsforagroupofseensubjects.EEGsignalsarepronetotime-relateddata
distribution shifts due to unstable recording devices and individual mental state fluc-
tuations [64–67], leading to inconsistent decoding accuracy for the same subjects [68].
While previous work [18, 28, 69] has explored similar settings (e.g., within-subject,
intra-subject), their data split strategies are inconsistent and limited to the single
subject. In this study, we propose a multi-subject adaptation setting for emotion
recognition and motor imagery tasks for fair comparison.
Few-Shot Transfer Setting. This setting is to evaluate the capacity of foundation
models to swiftly adapt to new tasks with limited data and minimal labels. Follow-
ing the practice of previous multi-modal foundation models [70, 71], we sample a
small number of samples from each category for each subject to create the support
set, used for training or fine-tuning. Then the model is evaluated on the query set
from the remaining samples. Specifically, the support set consists of a proportion of
randomly sampled instances for each category, with the proportion k ranging from
[0.02,0.05,0.3,0.5]. The results are averaged from three runs. This setting simulates
the scenario where a new task/user has only a small amount of calibration data,
which is vital for real-world BCI deployment where gathering extensive data is often
impractical and expensive.
Task Adaptation Pipeline
Standardized Data Preprocessing
AsEEGsignalsareinherentlynoisyandcomplex,datapreprocessingstepsarecritical
toenhancesignalqualityandmitigateartifacts.Here,wedevelopastandardizeddata
preprocessing pipeline including band-pass filtering, notch filtering, resampling, and
normalization, that can be universally applied in various BCI tasks and decoding
models.
Band-Pass Filtering. EEG signals span 0 Hz to hundreds of Hz, but among which
only specific frequency bands are pertinent to the task. Following previous prac-
tice [23], we employ a 0.1–75 Hz band-pass filter, preserving crucial task-relevant
frequency components like δ (0.5–4 Hz), θ (4–8 Hz), α (8–12 Hz), β (12–30 Hz), and
γ (30–50 Hz), while suppressing low-frequency drifts and high-frequency noise.
Notch Filtering. To eliminate power line interference, notch filtering was applied
to the EEG signals in this study. A Fast Fourier Transform (FFT) is conducted on
the raw EEG data to identify the power-line frequency at the collection site from the
frequency spectrum.
Resampling. Raw EEG signals are typically recorded at high sampling rates (e.g.,
1000 Hz or higher), leading to data redundancy and increased computational over-
head. Additionally, the sampling rates of different datasets often vary. Therefore, we
18

resampledtheEEGsignalstoalignwiththesamplingrateconfiguredintheevaluated
model.
Normalization. Data normalization is essential to accommodate varying data dis-
tributions across EEG datasets. We applied z-score normalization as the standard
technique for most datasets, which normalizes each sample using global statistics
across all trials to conform to a normal distribution. For SHU dataset, which is prone
tooutliers,weused95-percentile normalizationtoenhancerobustness,whichnor-
malizesdatapointsbydividingthembythe95-thpercentileofabsoluteamplitudeper
channelineachtrial,thusmitigatingtheimpactofoutliers.ForThings-EEGdataset,
we directly rescaled the signal to ensure that most signal values fall within the range
of approximately [−1,1] following previous practice [23].
Adaptation Strategy
AdaBrain-Bench does not constrain the adaptation strategy. Here we use two
commonly-used adaptation strategies for fine-tuning: full fine-tuning and linear
probing. The full fine-tuning approach updates all model parameters when adapting
to new tasks. Although computationally intensive, this method generally yields supe-
riorperformancewithsufficienttrainingdata[72]whentheupstreamanddownstream
datasetsdiffersignificantly,asitfacilitatestask-specificfeaturelearningacrossalllay-
ers of the network. Thus we adopt full fine-tuning as the primary transfer strategy. It
is also common to freeze the pretrained foundation models and fine-tune additional
linear layers to adapt to downstream tasks in transfer learning, a method referred to
as linear probe strategy. While computationally efficient, linear probe demands more
transferable representations from EEG foundation models.
Task Heads
Wedevelopedseveralspecializedtaskheadstohandlediversetaskparadigms,includ-
ing classification, regression, and retrieval. These task heads are lightweight and can
be seamlessly attached to models in a plug-and-play manner.
For classification tasks, the output embeddings of the model first undergo dimen-
sion reduction using its original methodologies (average pooling or linear reduction).
Theresultingembeddingsarethenflattenedintoone-dimensionalvectorsbeforebeing
fed into a linear classification layer for final prediction. For regression-based decod-
ing, the model’s output embeddings undergo average pooling before being processed
by a three-layer linear regression network. Each linear layer is sequentially followed
byanELUactivationandadropoutlayer.Fortheretrievaltask(i.e.,visualdecoding
on Things-EEG), the model outputs are first uniformly flattened and then are pro-
cessedthroughaweight-normalizedlinearprojectionlayer.Toevaluatevisualsemantic
decoding performance, we adopt the contrastive learning framework from the previ-
ous work [55] to align projected EEG embeddings with corresponding image features.
The EEG-to-image retrieval is subsequently conducted.
Other Experimental Details. We use binary cross-entropy (BCE) loss for binary
classification, cross-entropy (CE) loss for multiclass classification, mean squared error
(MSE)forregression,andcontrastivelossforretrieval.Weperformalearningrategrid
19

searchover[1e−3,5e−4,1e−4,5e−4,1e−5]foreachadaptationstrategy/settingcom-
bination to determine the optimal value. The batch size is set as 64. We adopted the
AdamW optimizer, with the weight decay set as 0.05. The number of training epoch
is set as 50. The experiments are conducted using Python 3.10.13 and PyTorch 2.4.0
with CUDA 11.8 support. Notably, for foundation models (e.g., BIOT and EEGPT)
unable to directly decode downstream datasets due to channel system incompatibili-
ties, we applied a 1×1 channel-wise convolutional layer to ensure compatibility with
input requirements.
Evaluation Metrics
Ourbenchmarkemploysvariousevaluationmetricstoassessthedecodingperformance
for different kinds of tasks: binary classification, multiclass classification, regression
and retrieval tasks. Table 6 summarizes the evaluation metrics corresponding to each
dataset in AdaBrain-Bench.
Accuracy Metrics. For binary classification tasks, different evaluation metrics are
adopted based on the characteristics of each dataset. For balanced binary classifica-
tiontasks(e.g.,EEGMATandSHU),wereporttheBalancedAccuracy(B-Acc)and
the Area Under the Receiver Operating Characteristic Curve (AUROC). B-Acc is
defined as the average recall across all classes, while AUROC quantifies the model’s
overall discriminative ability across different classification thresholds. For imbalanced
classification tasks (e.g., TUAB and Siena), where the positive class is of particular
importance,wereportB-AccandtheAreaUnderthePrecision-RecallCurve(AUC-
PR), as AUC-PR more effectively reflects the model’s performance on the minority
(positive) class. For multiclass classification tasks (i.e., SEED, SEED-IV, EEGMAT,
BCI-IV-2A, TUEV, HMC, SHHS, and Sleep-EDF), we use B-Acc and the Weighted
F1-Score (F1-W) as the metric. F1-W evaluates model performance by calculating
a weighted average of each class’s F1 score, where weights are determined by class
sampleproportiontoalleviateclassimbalanceissue.Forregression tasks (i.e.,SEED-
VIG), we adopt Pearson Correlation Coefficient (Corr) and R2 score as the metric.
Corrmeasuresthelinearrelationshipbetweenpredictedandtruevalues,whileR2rep-
resentstheproportionofvarianceinthedependentvariableexplainedbythedecoding
model. For retrieval tasks (i.e., Things-EEG), we use 2-Way and Top-5 accuracy as
the metric, following the previous practice [55]. The N-way accuracy is computed by
constructing a set containing the target sample and N −1 distractor samples from
the test set, assessing the model’s ability to identify the correct target among N cat-
egories. Top-5 accuracy measures the frequency that the true target image is among
the top 5 retrieved results, based on the corresponding EEG signals.
Transferability Metric. To further quantify the transferability of foundation mod-
els, we introduce the transfer score (TS), which is defined as the combination
of the relative gain of a pretrained foundation model over its trained-from-scratch
counterpart and the relative improvement to the maximum possible gain:
P −P P −P
TS=λ· prt scr +(1−λ)· prt scr , (1)
P P −P
scr oracle scr
20

Table 7 Summary of recently published brain foundation models.
Pretraining PretrainingDataSize Pretraining #Supported
Model #Params. Architecture Pre-trainingDatasets
Strategy (#channels*h) SignalDuration Channels
Self-supervised PREST,SHHS,CHB-MIT,
BIOT[21] 3.2M LinearTransformer 354,625 59,304h 18
ContrastiveLearning IIICSeizure,TUAB&TUEV
MaskedSignal PhysioNet-MI,HGD,TSU,
EEGPT[22] 25M CNN&Transformer 11,476 198h 58
Reconstruction SEED&M3CV
BCI-IV-1,Emobrain,SPIS,
MaskedSignal GraspandLiftEEG,InriaP300,
LaBraM[23] 5.8M CNN&Transformer 76,801 2,535h 136
Reconstruction SEEDseries,Siena,
TUEP,TUSZ&others
TUAB,TUAR
MaskedSignal
CBraMod[24] 4.0M CNN&Transformer 175,678 9,246h TUEP,TUEV Flexible
Reconstruction
TUSE&TUSL
where P denotes the performance of the adapted foundation model, P denotes
prt scr
the performance achieved by training the same model from scratch. P denotes
oracle
the approximate upper bound, which is set as 1 for the cross-subject transfer setting
and the full-data performance for the few-shot transfer setting. λ is set as default 0.5
in the experiment.
Models
We considered several open-sourced pre-trained EEG foundation models to be eval-
uated in our benchmark, including LaBraM [23], EEGPT [22], CBraMod [24], and
BIOT [21]. Next we provide details of these methods and summary in Table 7. Apart
from these EEG foundation models, we also included traditional supervised models
with state-of-the-art performance as baselines, including EEGNet [25], LDMA [26],
ST-Tran [27], and Conformer [28].
BIOT [21]. BIOT adopts linear transformer architecture that facilitates effective
cross-data learning by uniform EEG tokenization. The tokenization involves dividing
EEG signals into fixed-length segments. The segment embeddings along with spa-
tial and temporal position embeddings are re-arranged into token sequences. BIOT
conducts self-supervised contrastive learning between masked and unmasked signal
embeddings. We utilize the BIOT version pretrained on six clinical datasets related
to seizure and sleep, supporting 18 pre-defined channels.
EEGPT[22].EEGPTisatransformer-basedfoundationmodeladoptingmask-based
self-supervised learning. The pretraining involves a mask-based reconstruction strat-
egy and a spatio-temporal representation alignment strategy to learn generic neural
representations from unlabeled EEG data. EEGPT was pretrained on 246 hours of
EEG signals from five datasets from various tasks, rendering a large-scale foundation
model with 25 million parameters and 58 supported channels.
LaBraM [23]. LaBraM is a pretrained transformer model that employs a codebook-
based neural tokenizer. The tokenizer is trained by vector-quantized neural spectrum
prediction to convert raw EEG signals into discrete neural code. The code is then
used for masked EEG pretraining, allowing the model to capture generalizable neural
representations.LaBraMwaspretrainedonabout2,500hoursofvarioustypesofEEG
signals from around 20 datasets, supporting 137 EEG channels as input.
CBraMod[24].CBraModrefinesLaBraMbyimplementingacriss-crosstransformer
that separately models spatial and temporal dependencies separately via parallel
attention mechanisms. It also utilizes dynamic positional encoding conditioned on
21

EEG signals, enabling adaptation to arbitrary EEG channels. The model was pre-
trained on approximately 27,000 hours of EEG signals from the Temple University
| Hospital EEG | Corpus (TUEG) | [56]. |     |
| ------------ | ------------- | ----- | --- |
Data Availability
AllthedatasetsusedinthisbenchmarkarepubliclyavailableattheGitHubrepository
alongwithinstructionsfordatasplittingandpreprocessingtoreproducethereported
results.
| Code Availability |     |     |     |
| ----------------- | --- | --- | --- |
The code associated with this work is available in this GitHub repository with a MIT
License.
References
[1] Lemm, S., Blankertz, B., Curio, G., Muller, K.-R.: Spatio-spectral filters for
improving the classification of single trial eeg. IEEE Transactions on Biomedical
| Engineering | 52(9), 1541–1548 | (2005) |     |
| ----------- | ---------------- | ------ | --- |
[2] Cecotti, H., Graser, A.: Convolutional neural networks for p300 detection with
applicationtobrain-computerinterfaces.IEEETransactionsonPatternAnalysis
| and Machine | Intelligence | 33(3), 433–445 | (2010) |
| ----------- | ------------ | -------------- | ------ |
[3] He, L., Hu, D., Wan, M., Wen, Y., Von Deneen, K.M., Zhou, M.: Common
bayesian network for classification of eeg-based multiclass motor imagery bci.
IEEE Transactions on Systems, man, and cybernetics: systems 46(6), 843–854
(2015)
[4] Flesher, S.N., Downey, J.E., Weiss, J.M., Hughes, C.L., Herrera, A.J., Tyler-
Kabara, E.C., Boninger, M.L., Collinger, J.L., Gaunt, R.A.: A brain-computer
interface that evokes tactile sensations improves robotic arm control. Science
| 372(6544), | 831–836 (2021) |     |     |
| ---------- | -------------- | --- | --- |
[5] Ding, Y., Udompanyawit, C., Zhang, Y., He, B.: Eeg-based brain-computer
interface enables real-time robotic hand control at individual finger level. Nat.
| Commun. | 16(1), 1–20 | (2025) |     |
| ------- | ----------- | ------ | --- |
[6] Anumanchipalli, G.K., Chartier, J., Chang, E.F.: Speech synthesis from neural
| decoding | of spoken sentences. | Nature | 568(7753), 493–498 (2019) |
| -------- | -------------------- | ------ | ------------------------- |
[7] Willett, F.R., Kunz, E.M., Fan, C., Avansino, D.T., Wilson, G.H., Choi,
E.Y., Kamdar, F., Glasser, M.F., Hochberg, L.R., Druckmann, S., et al.: A
high-performance speech neuroprosthesis. Nature 620(7976), 1031–1036 (2023)
22

[8] Tang, J., LeBel, A., Jain, S., Huth, A.G.: Semantic reconstruction of continu-
ous language from non-invasive brain recordings. Nat. Neurosci. 26(5), 858–866
(2023)
[9] Chen, X., Wang, R., Khalilian-Gourtani, A., Yu, L., Dugan, P., Friedman, D.,
Doyle,W.,Devinsky,O.,Wang,Y.,Flinker,A.:Aneuralspeechdecodingframe-
work leveraging deep learning and speech synthesis. Nat. Mach. Intell. 6(4),
467–480 (2024)
[10] Wairagkar, M., Card, N.S., Singer-Clark, T., Hou, X., Iacobacci, C., Miller,
L.M., Hochberg, L.R., Brandman, D.M., Stavisky, S.D.: An instantaneous voice-
| synthesis | neuroprosthesis. |     | Nature, | 1–8 (2025) |     |     |
| --------- | ---------------- | --- | ------- | ---------- | --- | --- |
[11] Ramadan,R.A.,Vasilakos,A.V.:Braincomputerinterface:controlsignalsreview.
223,
| Neurocomputing |     |     | 26–44 (2017) |     |     |     |
| -------------- | --- | --- | ------------ | --- | --- | --- |
[12] Ang, K.K., Guan, C.: Eeg-based strategies to detect motor imagery for con-
trolandrehabilitation.IEEETransactionsonNeuralSystemsandRehabilitation
| Engineering | 25(4), | 392–401 | (2016) |     |     |     |
| ----------- | ------ | ------- | ------ | --- | --- | --- |
[13] Han, J., Gu, X., Yang, G.-Z., Lo, B.: Noise-factorized disentangled representa-
tion learning for generalizable motor imagery eeg classification. IEEE Journal of
| Biomedical | and | Health | Informatics | 28(2), 765–776 | (2023) |     |
| ---------- | --- | ------ | ----------- | -------------- | ------ | --- |
[14] Li, Y., Zhang, X., Zhang, B., Lei, M., Cui, W., Guo, Y.: A channel-projection
mixed-scale convolutional neural network for motor imagery eeg decoding. IEEE
TransactionsonNeuralSystemsandRehabilitationEngineering27(6),1170–1180
(2019)
[15] Ding,Y.,Udompanyawit,C.,Zhang,Y.,He,B.:Eeg-basedbrain-computerinter-
face enables real-time robotic hand control at individual finger level. Nature
| Communications |     | 16, 5401 | (2025) |     |     |     |
| -------------- | --- | -------- | ------ | --- | --- | --- |
[16] Supratak, A., Dong, H., Wu, C., Guo, Y.: Deepsleepnet: A model for automatic
sleepstagescoringbasedonrawsingle-channeleeg.IEEETransactionsonNeural
| Systems | and Rehabilitation |     | Engineering | 25(11), | 1998–2008 | (2017) |
| ------- | ------------------ | --- | ----------- | ------- | --------- | ------ |
[17] Acharya, U.R., Oh, S.L., Hagiwara, Y., Tan, J.H., Adeli, H.: Deep convolutional
neural network for the automated detection and diagnosis of seizure using eeg
| signals. | Computers | in  | Biology | and Medicine 100, | 270–278 | (2018) |
| -------- | --------- | --- | ------- | ----------------- | ------- | ------ |
[18] Song, T., Zheng, W., Song, P., Cui, Z.: Eeg emotion recognition using dynamical
graphconvolutionalneuralnetworks.IEEETransactionsonAffectiveComputing
| 11(3), 532–541 |     | (2018) |     |     |     |     |
| -------------- | --- | ------ | --- | --- | --- | --- |
[19] Brouwer, A.-M., Hogervorst, M.A., Van Erp, J.B., Heffelaar, T., Zimmerman,
P.H., Oostenveld, R.: Estimating workload using eeg spectral power and erps in
23

| the n-back | task. | Journal | of Neural | Engineering |     | 9(4), 045008 |     | (2012) |
| ---------- | ----- | ------- | --------- | ----------- | --- | ------------ | --- | ------ |
[20] Li,D.,Wei,C.,Li,S.,Zou,J.,Qin,H.,Liu,Q.:Visualdecodingandreconstruction
via eeg embeddings with guided diffusion. In: Advances in Neural Information
| Processing | Systems, | vol. | 37, pp. | 102822–102864 |     | (2024) |     |     |
| ---------- | -------- | ---- | ------- | ------------- | --- | ------ | --- | --- |
[21] Yang,C.,Westover,M.,Sun,J.:Biot:Biosignaltransformerforcross-datalearn-
ing in the wild. In: Advances in Neural Information Processing Systems, vol. 36,
| pp. 78240–78260 |     | (2023) |     |     |     |     |     |     |
| --------------- | --- | ------ | --- | --- | --- | --- | --- | --- |
[22] Wang,G.,Liu,W.,He,Y.,Xu,C.,Ma,L.,Li,H.:Eegpt:Pretrainedtransformer
for universal and reliable representation of eeg signals. In: Advances in Neural
| Information | Processing |     | Systems, | vol. | 37, pp. | 39249–39280 | (2024) |     |
| ----------- | ---------- | --- | -------- | ---- | ------- | ----------- | ------ | --- |
[23] Jiang, W., Zhao, L., Lu, B.: Large brain model for learning generic representa-
tions with tremendous eeg data in bci. In: International Conference on Learning
| Representations |     | (2024) |     |     |     |     |     |     |
| --------------- | --- | ------ | --- | --- | --- | --- | --- | --- |
[24] Wang,J.,Zhao,S.,Luo,Z.,Zhou,Y.,Jiang,H.,Li,S.,Li,T.,Pan,G.:CBramod:
A criss-cross brain foundation model for EEG decoding. In: International
| Conference | on Learning |     | Representations |     | (2025) |     |     |     |
| ---------- | ----------- | --- | --------------- | --- | ------ | --- | --- | --- |
[25] Lawhern, V.J., Solon, A.J., Waytowich, N.R., Gordon, S.M., Hung, C.P., Lance,
B.J.: Eegnet: a compact convolutional neural network for eeg-based brain–
| computer | interfaces. | Journal |     | of neural | engineering | 15(5), | 056013 | (2018) |
| -------- | ----------- | ------- | --- | --------- | ----------- | ------ | ------ | ------ |
[26] Miao, Z., Zhao, M., Zhang, X., Ming, D.: Lmda-net: A lightweight multi-
dimensional attention network for general eeg-based brain-computer interfaces
| and interpretability. |     | NeuroImage |     | 276, | 120209 | (2023) |     |     |
| --------------------- | --- | ---------- | --- | ---- | ------ | ------ | --- | --- |
[27] Song, Y., Jia, X., Yang, L., Xie, L.: Transformer-based spatial-temporal feature
| learning | for eeg | decoding. | arXiv | preprint | arXiv:2106.11170 |     | (2021) |     |
| -------- | ------- | --------- | ----- | -------- | ---------------- | --- | ------ | --- |
[28] Song, Y., Zheng, Q., Liu, B., Gao, X.: Eeg conformer: Convolutional transformer
for eeg decoding and visualization. IEEE Transactions on Neural Systems and
| Rehabilitation | Engineering |     | 31, | 710–719 | (2022) |     |     |     |
| -------------- | ----------- | --- | --- | ------- | ------ | --- | --- | --- |
[29] Sakhavi,S.,Guan,C.,Yan,S.:Learningtemporalinformationforbrain-computer
interface using convolutional neural networks. IEEE Transactions on Neural
| Networks | and Learning |     | Systems | 29(11), | 5619–5629 | (2018) |     |     |
| -------- | ------------ | --- | ------- | ------- | --------- | ------ | --- | --- |
[30] Gao, Z., Wang, X., Yang, Y., Mu, C., Cai, Q., Dang, W., Zuo, S.: Eeg-based
spatio–temporalconvolutionalneuralnetworkfordriverfatigueevaluation.IEEE
TransactionsonNeuralNetworksandLearningSystems30(9),2755–2763(2019)
[31] Wang,P.,Jiang,A.,Liu,X.,Shang,J.,Zhang,L.:Lstm-basedeegclassificationin
motor imagery tasks. IEEE Transactions on Neural Systems and Rehabilitation
24

Engineering 26(11), 2086–2095 (2018)
[32] Tsiouris, K.M., Pezoulas, V.C., Zervakis, M., Konitsiotis, S., Koutsouris, D.D.,
Fotiadis,D.I.:Alongshort-termmemorydeeplearningnetworkfortheprediction
of epileptic seizures using eeg signals. Computers in Biology and Medicine 99,
24–37 (2018)
[33] Du, X., Ma, C., Zhang, G., Li, J., Lai, Y.-K., Zhao, G., Deng, X., Liu, Y.-J.,
Wang, H.: An efficient lstm network for emotion recognition from multichannel
eegsignals.IEEETransactionsonAffectiveComputing13(3),1528–1540(2020)
[34] Phan, H., Mikkelsen, K., Ch´en, O.Y., Koch, P., Mertins, A., De Vos, M.:
Sleeptransformer: Automatic sleep staging with interpretability and uncertainty
quantification. IEEE Transactions on Biomedical Engineering 69(8), 2456–2467
(2022)
[35] Schirrmeister, R.T., Springenberg, J.T., Fiederer, L.D.J., Glasstetter, M.,
Eggensperger,K.,Tangermann,M.,Hutter,F.,Burgard,W.,Ball,T.:Deeplearn-
ingwithconvolutionalneuralnetworksforeegdecodingandvisualization.Human
Brain Mapping 38(11), 5391–5420 (2017)
[36] D´efossez,A.,Caucheteux,C.,Rapin,J.,Kabeli,O.,King,J.-R.:Decodingspeech
perception from non-invasive brain recordings. Nat. Mach. Intell. 5(10), 1097–
1107 (2023)
[37] Zhao,H.,Zheng,Q.,Ma,K.,Li,H.,Zheng,Y.:Deeprepresentation-baseddomain
adaptation for nonstationary eeg classification. IEEE Transactions on Neural
Networks and Learning Systems 32(2), 535–545 (2020)
[38] Zhang,R.,Zong,Q.,Dou,L.,Zhao,X.,Tang,Y.,Li,Z.:Hybriddeepneuralnet-
work using transfer learning for eeg motor imagery decoding. Biomedical Signal
Processing and Control 63, 102144 (2021)
[39] Lee, N., Bakas, S., Barmpas, K., Panagakis, Y., Adamos, D., Laskaris, N.,
Zafeiriou, S.: Assessing the capabilities of large brainwave foundation models. In:
International Conference on Learning Representations Workshop (2025)
[40] Liu, H., Yang, S., Zhang, Y., Wang, M., Gong, F., Xie, C., Liu, G., Liu, Z., Liu,
Y.-J.,Lu,B.-L.,etal.:Libeer:Acomprehensivebenchmarkandalgorithmlibrary
for eeg-based emotion recognition. arXiv preprint arXiv:2410.09767 (2024)
[41] Dan, J., Pale, U., Amirshahi, A., Cappelletti, W., Ingolfsson, T.M., Wang,
X., Cossettini, A., Bernini, A., Benini, L., Beniczky, S., et al.: Szcore: Seizure
community open-source research evaluation framework for the validation of
electroencephalography-based automated seizure detection algorithms. Epilepsia
(2024)
25

[42] Chevallier, S., Carrara, I., Aristimunha, B., Guetschel, P., Sedlar, S., Lopes, B.,
Velut,S.,Khazem,S.,Moreau,T.:Thelargesteeg-basedbcireproducibilitystudy
foropenscience:themoabbbenchmark.arXivpreprintarXiv:2404.15319(2024)
[43] Li, B., Ge, Y., Ge, Y., Wang, G., Wang, R., Zhang, R., Shan, Y.: Seed-
bench: Benchmarking multimodal large language models. In: Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp.
| 13299–13308 | (2024) |     |     |     |     |
| ----------- | ------ | --- | --- | --- | --- |
[44] Zhang, T., Ladhak, F., Durmus, E., Liang, P., McKeown, K., Hashimoto, T.B.:
Benchmarking large language models for news summarization. Transactions of
| the Association | for Computational |     | Linguistics | 12, 39–57 (2024) |     |
| --------------- | ----------------- | --- | ----------- | ---------------- | --- |
[45] Tong,P.,Brown,E.,Wu,P.,Woo,S.,IYER,A.J.V.,Akula,S.C.,Yang,S.,Yang,
et al.:
J., Middepogu, M., Wang, Z., Cambrian-1: A fully open, vision-centric
exploration of multimodal llms. Advances in Neural Information Processing
| Systems | 37, 87310–87356 | (2024) |     |     |     |
| ------- | --------------- | ------ | --- | --- | --- |
[46] Zheng, W., Lu, B.: Investigating critical frequency bands and channels for eeg-
based emotion recognition with deep neural networks. IEEE Transactions on
| Autonomous | Mental Development |     | 7(3), 162–175 | (2015) |     |
| ---------- | ------------------ | --- | ------------- | ------ | --- |
[47] Zheng, W.-L., Liu, W., Lu, Y., Lu, B.-L., Cichocki, A.: Emotionmeter: A
multimodal framework for recognizing human emotions. IEEE Transactions on
| Cybernetics | 49(3), 1110–1122 |     | (2018) |     |     |
| ----------- | ---------------- | --- | ------ | --- | --- |
[48] Zyma, I., Tukaev, S., Seleznov, I., Kiyono, K., Popov, A., Chernykh, M.,
Shpenkov, O.: Electroencephalograms during mental arithmetic task perfor-
| mance. | Data 4(1), 14 | (2019) |     |     |     |
| ------ | ------------- | ------ | --- | --- | --- |
[49] Goldberger, A.L., Amaral, L.A., Glass, L., Hausdorff, J.M., Ivanov, P.C., Mark,
R.G., Mietus, J.E., Moody, G.B., Peng, C.-K., Stanley, H.E.: Physiobank, phys-
iotoolkit, and physionet: components of a new research resource for complex
| physiologic | signals. Circulation |     | 101(23), | 215–220 (2000) |     |
| ----------- | -------------------- | --- | -------- | -------------- | --- |
[50] Zheng, W.-L., Lu, B.-L.: A multimodal approach to estimating vigilance using
| eeg and | forehead eog. | Journal | of Neural | Engineering 14(2), 026017 | (2017) |
| ------- | ------------- | ------- | --------- | ------------------------- | ------ |
[51] Tangermann,M.,Mu¨ller,K.-R.,Aertsen,A.,Birbaumer,N.,Braun,C.,Brunner,
C., Leeb, R., Mehring, C., Miller, K.J., Mu¨ller-Putz, G.R., et al.: Review of the
| bci competition | iv. Frontiers | in  | neuroscience | 6, 55 (2012) |     |
| --------------- | ------------- | --- | ------------ | ------------ | --- |
[52] Ma,J.,Yang,B.,Qiu,W.,Li,Y.,Gao,S.,Xia,X.:Alargeeegdatasetforstudy-
ingcross-sessionvariabilityinmotorimagerybrain-computerinterface.Scientific
| Data 9(1), | 531 (2022) |     |     |     |     |
| ---------- | ---------- | --- | --- | --- | --- |
[53] Gifford, A.T., Dwivedi, K., Roig, G., Cichy, R.M.: A large and rich eeg dataset
26

for modeling human visual object recognition. NeuroImage 264, 119754 (2022)
[54] Grootswagers,T.,Zhou,I.,Robinson,A.K.,Hebart,M.N.,Carlson,T.A.:Human
eeg recordings for 1,854 concepts presented in rapid serial visual presentation
streams. Scientific Data 9(1), 3 (2022)
[55] Li, D., Wei, C., Li, S., Zou, J., Liu, Q.: Visual decoding and reconstruction
via eeg embeddings with guided diffusion. In: Conference on Neural Information
Processing Systems (2024)
[56] Obeid, I., Picone, J.: The temple university hospital eeg data corpus. Frontiers
in Neuroscience 10, 196 (2016)
[57] Detti,P.,Vatti,G.,Lara,G.:Eegsynchronizationanalysisforseizureprediction:
Astudyondataofnoninvasiverecordings.Processes8(7)(2020)https://doi.org/
10.3390/pr8070846
[58] Alvarez-Estevez, D., Rijsman, R.M.: Inter-database validation of a deep learning
approach for automatic sleep scoring. PloS one 16(8), 0256111 (2021)
[59] Zhang, G.-Q., Cui, L., Mueller, R., Tao, S., Kim, M., Rueschman, M., Mariani,
S., Mobley, D., Redline, S.: The national sleep research resource: towards a sleep
datacommons.JournaloftheAmericanMedicalInformaticsAssociation25(10),
1351–1358 (2018)
[60] Quan, S.F., Howard, B.V., Iber, C., Kiley, J.P., Nieto, F.J., O’Connor, G.T.,
Rapoport, D.M., Redline, S., Robbins, J., Samet, J.M., et al.: The sleep heart
health study: design, rationale, and methods. Sleep 20(12), 1077–1085 (1997)
[61] Kemp,B.,Zwinderman,A.H.,Tuk,B.,Kamphuisen,H.A.,Oberye,J.J.:Analysis
of a sleep-dependent neuronal feedback loop: the slow-wave microcontinuity of
the eeg. IEEE Transactions on Biomedical Engineering 47(9), 1185–1194 (2000)
[62] Berry, R.B., Brooks, R., Gamaldo, C.E., Harding, S.M., Marcus, C., Vaughn,
B.V.,etal.:Theaasmmanualforthescoringofsleepandassociatedevents.Rules,
TerminologyandTechnicalSpecifications,Darien,Illinois,AmericanAcademyof
Sleep Medicine 176, 7 (2012)
[63] Eldele,E.,Chen,Z.,Liu,C.,Wu,M.,Kwoh,C.-K.,Li,X.,Guan,C.:Anattention-
based deep learning approach for sleep stage classification with single-channel
eeg. IEEE Transactions on Neural Systems and Rehabilitation Engineering 29,
809–818 (2021)
[64] Chen, Y., Yang, R., Huang, M., Wang, Z., Liu, X.: Single-source to single-target
cross-subject motor imagery classification based on multisubdomain adaptation
network. IEEE Transactions on Neural Systems and Rehabilitation Engineering
30, 1992–2002 (2022)
27

[65] Bigdely-Shamlo,N.,Vankov,A.,Ramirez,R.R.,Makeig,S.:Brainactivity-based
image classification from rapid serial visual presentation. IEEE Transactions on
| Neural Systems |     | and Rehabilitation |     | Engineering |     | 16(5), 432–441 | (2008) |
| -------------- | --- | ------------------ | --- | ----------- | --- | -------------- | ------ |
[66] Huang, Y., Erdogmus, D., Pavel, M., Mathan, S., Hild II, K.E.: A frame-
work for rapid visual image search using single-trial brain evoked responses.
| Neurocomputing |     | 74(12-13), | 2041–2051 |     | (2011) |     |     |
| -------------- | --- | ---------- | --------- | --- | ------ | --- | --- |
[67] Jobert, M., Wilson, F.J., Ruigt, G.S., Brunovsky, M., Prichep, L.S., Drinken-
burg, W.H., Committee, I.P.-E.G.: Guidelines for the recording and evaluation
of pharmaco-eeg data in man: the international pharmaco-eeg society (ipeg).
| Neuropsychobiology |     | 66(4), | 201–220 | (2012) |     |     |     |
| ------------------ | --- | ------ | ------- | ------ | --- | --- | --- |
[68] Saha, S., Ahmed, K.I.U., Mostafa, R., Hadjileontiadis, L., Khandoker, A.:
Evidence of variabilities in eeg dynamics during motor imagery-based mul-
ticlass brain–computer interface. IEEE Transactions on Neural Systems and
| Rehabilitation | Engineering |     | 26(2), | 371–382 | (2017) |     |     |
| -------------- | ----------- | --- | ------ | ------- | ------ | --- | --- |
[69] Chen, C.P., Chen, B., Zhang, T.: Adamgraph: Adaptive attention-modulated
graph network for eeg emotion recognition. IEEE Transactions on Cybernetics
| 55(5), 2038–2051 |     | (2025) |     |     |     |     |     |
| ---------------- | --- | ------ | --- | --- | --- | --- | --- |
[70] Radford,A.,Kim,J.W.,Hallacy,C.,Ramesh,A.,Goh,G.,Agarwal,S.,Sastry,G.,
Askell,A.,Mishkin,P.,Clark,J.,et al.:Learningtransferablevisualmodelsfrom
natural language supervision. In: International Conference on Machine Learning,
| pp. 8748–8763 | (2021) |     |     |     |     |     |     |
| ------------- | ------ | --- | --- | --- | --- | --- | --- |
[71] Zhou, K., Yang, J., Loy, C.C., Liu, Z.: Conditional prompt learning for vision-
language models. In: Proceedings of the IEEE/CVF Conference on Computer
| Cision and | Pattern | Recognition, |     | pp. 16816–16825 |     | (2022) |     |
| ---------- | ------- | ------------ | --- | --------------- | --- | ------ | --- |
[72] Kornblith, S., Shlens, J., Le, Q.V.: Do better imagenet models transfer better?
In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
| Recognition, | pp. | 2661–2671 | (2019) |     |     |     |     |
| ------------ | --- | --------- | ------ | --- | --- | --- | --- |
28