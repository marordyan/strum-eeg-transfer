| NeuralBench: |        | A   | Unifying | Framework |     | to  | Benchmark |     |
| ------------ | ------ | --- | -------- | --------- | --- | --- | --------- | --- |
| NeuroAI      | Models |     |          |           |     |     |           |     |
HubertBanville1, Stéphaned’Ascoli1, SimonDahan1, JérémyRapin1, MarlèneCareil1, Yohann
Benchetrit1, JarodLévy1,4, SaarangPanchavati1, AntoineRatouchniak1, Mingfang(Lucy)Zhang2,3,
Elisa
| Cascardi1, | KatelynBegany1, | TeonBrooks1, |     | Jean-RémiKing1 |     |     |     |     |
| ---------- | --------------- | ------------ | --- | -------------- | --- | --- | --- | --- |
1Brain & AI team, Meta FAIR, 2École Normale Supérieure, Université PSL, CNRS, 3Hospital
4MIND,
| Foundation | Adolphe | de Rothschild, |     | Inria |     |     |     |     |
| ---------- | ------- | -------------- | --- | ----- | --- | --- | --- | --- |
Deep learning and large public datasets have recently catalyzed the proliferation of AI models for
processing brain recordings. However, systematically evaluating these models remains a challenge:
6202 yaM 8  ]GL.sc[  1v59480.5062:viXra
not only do the preprocessing pipelines, training and finetuning approaches largely vary across
studies, but their downstream evaluation is often limited to small sets of tasks and/or datasets. Here,
we present NeuralBench: a unified framework for benchmarking AI models of brain activity. We
accompany this framework with NeuralBench-EEG v1.0 – a large EEG benchmark that includes
36 electroencephalography (EEG) tasks and 14 deep learning architectures, and is evaluated on 94
datasets accessed through a standardized interface. This first EEG-focused release already highlights
two main findings. First, current foundation models only marginally outperform task-specific models.
Second, a large set of tasks (e.g. cognitive decoding, clinical predictions) remain highly challenging,
evenforthebestmodels. Critically, NeuralBenchisdesignedfortheintegrationofnewtasks, datasets,
models, and neuroimaging modalities, as illustrated by preliminary extensions to MEG and fMRI
datasets and models. Through this white paper, we invite the community to expand this open-source
framework and work together toward a unified benchmarking standard for neuroimaging models.
|     | hubertjb@meta.com, |     | jeanremi@meta.com |     |     |     |     |     |
| --- | ------------------ | --- | ----------------- | --- | --- | --- | --- | --- |
Correspondence:
| Code: | https://github.com/facebookresearch/neuroai/tree/main/neuralbench-repo |     |           |     |             |     |             |     |
| ----- | ---------------------------------------------------------------------- | --- | --------- | --- | ----------- | --- | ----------- | --- |
|       | NeuralFetch                                                            |     | NeuralSet |     | NeuralTrain |     | NeuralBench |     |
Dataset definitions Data loading & extraction Models & training Benchmark orchestration
|     |     |     | 14  | 36  | 94  | 9,478 | 13,603 | 1   |
| --- | --- | --- | --- | --- | --- | ----- | ------ | --- |
NeuralBench-EEG v1.0
|     |     |     | models | tasks | datasets | subjects | hours | benchmark |
| --- | --- | --- | ------ | ----- | -------- | -------- | ----- | --------- |
Figure1 NeuralBench is a benchmarking framework for the evaluation of brain models, based on the NeuralFetch,
NeuralSet and NeuralTrain libraries, and providing a fully configurable and flexible interface. Secondrow. Contents of
| the first | release, NeuralBench-EEG |     | v1.0. |     |     |     |     |     |
| --------- | ------------------------ | --- | ----- | --- | --- | --- | --- | --- |
1 Introduction
The rise of AI models in neuroimaging. Historically focused on targeted, small-scale, and private studies
(Poldrack, 2011; Michel and Murray, 2012; Baillet, 2017), the analysis of brain activity is now rapidly shifting
toward large-scale public datasets (Van Essen et al., 2013; Harati et al., 2014; Taylor et al., 2017; Pinho et al.,
2018; Sun et al., 2025; d’Ascoli et al., 2026). On top of boosting statistical power and stimulating reproducible
research (Button et al., 2013; Poldrack et al., 2017; d’Ascoli et al., 2026), the proliferation of open datasets
has catalyzed the use of AI to process brain recordings. Specifically, the self-supervised learning methods
1

|     | A Downstream tasks |     |     |     |     |     |     | B Brain models |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- | --- | -------------- | --- | --- |
cov + proj
Cognitive Image Sentence Speech Typing Video Word Logistic/Ridge
regression
|     |     |           | M e n ta | l M o t      | o r M o t o r     |            |     |     |                      |     |
| --- | --- | --------- | -------- | ------------ | ----------------- | ---------- | --- | --- | -------------------- | --- |
|     |     | BCI c-VEP | i m ag e | ry ex ec u t | i on im a g e r y | P300 SSVEP |     |     |                      |     |
|     |     |           | 8        |              | 3                 | 18 24 8    |     |     | Handcrafted features |     |
Evoked
|     | ResponsesAudiovisual |     | ERN | MMN | N170 | N2pc N400 LRP |     |     |     |           |
| --- | -------------------- | --- | --- | --- | ---- | ------------- | --- | --- | --- | --------- |
|     |                      |     |     | 3   |      | 2             |     |     |     | Objective |
Classification
|     |     | C l in i c | al  |     |     |     |     |     |     |     |
| --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Clinical Dementia DepressionParkinson Pathology Schizophr. Seizure Task-specific
|     |             | e v e n   | t           |            |     |     |     |     |                                      | Regression |
| --- | ----------- | --------- | ----------- | ---------- | --- | --- | --- | --- | ------------------------------------ | ---------- |
|     | Int         | e r n a l |             |            |     |     |     | EEG |                                      | Retrieval  |
|     |             | Emotion   | M e n ta    | l Workload |     |     |     |     | ~ 1 . 5 K 4 . 2 M   p a r a m s      |            |
|     | S           | t a t e   | a ri th     | . 2        | 3   |     |     |     | t r a i n ed  f r o m   sc r a t c h |            |
|     | Phenotyping | Age       | P s yc h    | o - Sex    |     |     |     |     |                                      |            |
|     |             |           | p a th o lo | g y        |     |     |     |     |                                      |            |
Foundation
|     | S   | le e p S le e  | p S le e p    | Artifact | Re a ct ion |           |     |                  |                    |     |
| --- | --- | -------------- | ------------- | -------- | ----------- | --------- | --- | ---------------- | ------------------ | --- |
|     |     | M i s c a ro u | s al st a g e |          | t im e      |           |     | B r a i n        |                    |     |
|     |     |                |               |          |             |           |     | pre tr a i n ing | linear             |     |
|     |     | Classification |               |          | Regression  | Retrieval |     | data             | ~3.2M157.1M params |     |
pretrained, fine-tuned
|     | C Data diversity |     |     |     |     |       | D Data quantity |     |     |     |
| --- | ---------------- | --- | --- | --- | --- | ----- | --------------- | --- | --- | --- |
| 160 |                  |     |     |     |     | 10000 |                 |     |     |     |
140
stesatad maertsnwod #
| 120 |     |     |     |     |     |     | 8000 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
stcejbus #
| 100 |     |     |     |     |     |     | 6000 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
80
|     | 60  |     |     |     |     |     | 4000 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
40
2000
|     | 20  |     |     |     |     | Benchmark   |     |     |     | Benchmark   |
| --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | ----------- |
|     |     |     |     |     |     | Model paper |     |     |     | Model paper |
|     | 0   |     |     |     |     |             | 0   |     |     |             |
5 10 15 20 25 30 35 40 0 2000 4000 6000 8000 10000 12000 14000
|     |     |     | # downstream tasks |     |     |     |     |     | # hours of EEG data |     |
| --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | ------------------- | --- |
Figure2 Detailedoverview. A.NeuralBench-EEGv1.0currentlyincludes36decodingdownstreamtaskson94different
datasets,covering8differentcategoriessuchascognitivedecoding,brain-computerinterfacing(BCI),evokedresponses
and clinical tasks. B. Three types of models are compared: task-specific from-scratch deep learning architectures,
pretrainedfoundationmodelsandhandcraftedfeatures-basedbaselines. C-D.NeuralBench-EEGv1.0currentlycontains
more than three times the number of tasks of previous EEG downstream task benchmarks, and more than twice as
| many | individual | subjects, |     | making | it the | largest such open-source | benchmark |     | yet. |     |
| ---- | ---------- | --------- | --- | ------ | ------ | ------------------------ | --------- | --- | ---- | --- |
developed for language, speech and images (Devlin et al., 2019; Baevski et al., 2020; Oquab et al., 2024) are
now adapted for the development of brain foundation models (Yang et al., 2025; Zhou et al., 2025). These
models start to transfer to downstream tasks spanning electroencephalography (EEG) (Jiang et al., 2024;
Kostasetal.,2021;Yangetal.,2023;Wangetal.,2024;Döneretal.,2025;ElOuahidietal.,2025), functional
magnetic resonance imaging (fMRI) (Kim et al., 2023; Dong et al., 2024; Caro et al., 2023), intracranial
EEG (Wang et al., 2023; Yuan et al., 2024), structural MRI (Tak et al., 2026), electrophysiology (Azabou
| et  | al., 2023), | and | calcium | imaging | (Wang | et al., 2025a). |     |     |     |     |
| --- | ----------- | --- | ------- | ------- | ----- | --------------- | --- | --- | --- | --- |
Current benchmarking challenges. Despite these advances, the evaluation landscape is fragmented. For EEG,
the Mother of All BCI Benchmarks (MOABB)1 (Jayaram and Barachant, 2018; Aristimunha et al., 2025)
provides an extensive benchmark for brain-computer interfacing (148 datasets). However, it focuses on a
narrow set of 5 downstream tasks (e.g., left versus right motor imagery) and primarily targets handcrafted
features-based approaches, such as Riemannian geometry pipelines for trial classification (Barachant et al.,
2011; Yger et al., 2016). Building on this, Borra et al. (2024) adapted the benchmark for deep learning,
focusingspecificallyonasubsetofnineBCIdatasetfromtheMOABBandthreewell-establishedarchitectures.
In parallel, benchmarks tailored to EEG foundation models have emerged, e.g. , EEG-Bench (Kastrati et al.,
2025), EEG-FM-Bench (Xiong et al., 2025), and AdaBrain-Bench (Wu et al., 2025). However, these efforts
too are limited to a restricted set of downstream evaluations (Figure 2). This fragmentation is even more
1https://moabb.neurotechx.com/
2

pronounced in other brain recording modalities. For intracranial EEG (iEEG), Karpowicz et al. (2024)
introduced FALCON, a few-shot evaluation benchmark for invasive BCI tasks, but is limited to 5 evaluation
datasets. Elsewhere,foundationmodelsforfMRI,MEG,andothermodalitiesarestillevaluatedonhandpicked
datasets without a unified, systematic benchmark. Overall, there is currently no comprehensive framework for
standardizing and efficiently evaluating brain foundation models across neuroimaging modalities.
Contribution. Here, we introduce NeuralBench, a community-driven benchmarking framework for evaluating
foundation models on brain activity recordings. NeuralBench is designed to be:
1. Comprehensive. Asmanyrelevantdownstreamtasksaspossibleshouldbeincluded,forasmanyrelevant
brain imaging devices as possible. This helps properly support claims of models being truly foundational
and provides a more nuanced assessment of the strengths and weaknesses of different models.
2. Rigorouslyvalidated. Publicly available datasets often require careful curation and tailored onboarding
efforts so their contents can be used properly. Similarly, the framing of learning tasks requires special
care to avoid common pitfalls (e.g. leakage, overfitting, etc.) and to be maximally informative. This
also applies to foundation models – each one is trained using a specific preprocessing pipeline that needs
to be replicated to allow fair evaluation.
3. Standardized. Byprovidingaunifiedpoint-of-entryfordiversebrainimagingdevices(EEG,iEEG,MEG,
fMRI, fNIRS, etc.), NeuralBench makes it easy to build and evaluate multimodal pipelines, bringing us
closer to integrated brain modeling.
4. Flexible. NeuralBench is configurable at all levels of the neuroimaging modeling pipeline (data source,
preprocessing, architecture, optimization, metrics, etc.), offering a compact and flexible interface for
running and evaluating brain models.
The first release of NeuralBench, NeuralBench-EEG v1.0, supports 36 tasks evaluated on 94 EEG datasets
(with some tasks spanning multiple datasets), accessed through a standardized interface. This effort, which
capitalizes on the careful curation of public datasets, provides unique support for cognitive decoding tasks
(i.e., image, sentence, speech, typing, video and word decoding), which, apart from image decoding, have been
omitted in previous benchmarks. In addition, we demonstrate the versatility of this framework and seed its
expansion towards other brain imaging modalities by including a couple of illustrative MEG and fMRI tasks
and models.
Goal and overview. In the following sections, we present a technical overview of NeuralBench, followed
by initial results on NeuralBench-EEG v1.0 which highlight two main findings: current EEG foundation
models only marginally outperform task-specific baselines, and many complex tasks (e.g. , cognitive decoding,
clinicalprediction)remainchallengingevenforfoundationmodels. WethenshowhowNeuralBenchseamlessly
extends to MEG and fMRI modalities.
Toward a Community-Driven Standard. Recognizing that a unified standard is only as strong as the
community behind it, we provide the NeuralBench codebase2 as a starting point for global collaboration. We
invite researchers across tasks and modalities to co-author its evolution and join us in defining the future of
brain model evaluation.
2 Methods
In this section, we give a technical overview of NeuralBench, including its general architecture, a description
of supported downstream tasks, model architectures, adaptation strategies, and evaluation protocols. We
provide a high-level summary here and refer the reader to the package documentation for additional technical
details.
2https://github.com/facebookresearch/neuroai/tree/main/neuralbench-repo
3

2.1 Benchmarkarchitecture
NeuralBench is built on top of three main Python packages, which provide an interface with the data,
processing and modeling tools that already exist in the neuroscience software ecosystem. Specifically,
public neuroimaging datasets are accessed through NeuralFetch, which fetches curated datasets from public
repositories like OpenNeuro3, DANDI4, and NEMAR5. Then, neural data is prepared and made available as
PyTorch-ready dataloaders with NeuralSet– a package designed to efficiently leverage existing packages like
MNE-Python (Gramfort et al., 2013)6 and nilearn (Abraham et al., 2014)7 for applying classic neuroimaging
preprocessingpipelines,aswellasHuggingFace8 forextractingAImodelembeddings(e.g.onword,speechand
image modalities). Finally, NeuralTrain provides modular training code with PyTorch-Lightning9, Pydantic10
and exca (Rapin and King, 2024)11(see Figure 2D).
Once installed, NeuralBench is run with a command-line interface (CLI). For example, the following can be
used to run the audiovisual stimulus classification task on the MNE-Python sample dataset (Gramfort et al.,
2013):
1. Install NeuralBench 2. Run the audiovisual stimulus task on EEG
$pipinstallneuralbench $neuralbencheegaudiovisual_stimulus--download # Download data
$neuralbench--help # Trigger $neuralbencheegaudiovisual_stimulus--prepare # Prepare cache
interactive path configuration $neuralbencheegaudiovisual_stimulus # Run the task
On top of allowing quick sanity-checking of the codebase, this small dataset (<300 examples) is an interesting
case study for very-low-data regime downstream tasks.
Task configuration Tasks are configured through lightweight YAML files, which describe data sources,
train/validation/test splits, neural data preprocessing (filtering, scaling, windowing, etc.), target processing if
any (e.g. extracting dense representations of rich stimuli), trainer configuration (number of epochs, learning
rate, etc.), and metrics.
Example YAML configuration for audiovisual stimulus classification on EEG.
data:
study:
source.name:Mne2013SampleEeg
split:
name:SklearnSplit
valid_split_ratio:0.2
test_split_ratio:0.2
stratify_by:description
neuro.baseline:[0.0,0.2]
target:
name:LabelEncoder
event_types:Stimulus
event_field:description
return_one_hot:true
trigger_event_type:Stimulus
start:-0.2
duration:1.0
loss.name:CrossEntropyLoss
metrics:BalancedAcc
3https://openneuro.org/
4https://dandiarchive.org/
5https://nemar.org/
6https://mne.tools/
7https://nilearn.github.io/
8https://huggingface.co/
9https://lightning.ai
10https://pydantic.dev/
11https://github.com/facebookresearch/exca
4

Model configuration Similarly, deep learning architectures are defined through YAML files that configure
NeuralTrain models. Thanks to its configurable pydantic layer, NeuralTrain can transparently access models
from other libraries such as BrainDecode12 (Schirrmeister et al., 2017; Aristimunha et al., 2026).
2.2 Taskanddatasetselection
A primary objective of NeuralBench is to provide a wide coverage of downstream tasks. Focusing on EEG for
this first release, we selected a set of 36 representative downstream tasks, covering 8 categories: cognitive
decoding, brain-computer interfacing (BCI), evoked responses, clinical, internal state, sleep, phenotyping and
miscellaneous (see Figure 2A). Note that each task does not necessarily fall neatly into one of these categories,
e.g. the P300 classification task could also fall under the Evoked responses category, however since it is usually
collected as part of a P300 speller protocol we file it under BCI. Similarly, the psychopathology classification
task could go under the Clinical category, but we opt to keep it under the same Phenotyping category as
other tasks based on Shirazi et al. (2024). Nevertheless, we keep this operational organization to facilitate
interpretation.
Several inclusion criteria were considered. First, whenever possible, openly accessible datasets, rather than
datasets requiring additional manual steps, were prioritized. Second, as several EEG datasets are approaching
saturation (e.g. binary pathology detection on the TUAB dataset (Lopez et al., 2015)), we devoted special
efforts to include challenging tasks on which performance is likely to be significantly improvable. To this end,
weincludemultiplecognitive decoding tasks,wherethegoalistorecoveradenserepresentationofthestimulus
presented to participants, e.g. speech, images, words and videos (Défossez et al., 2022; Benchetrit et al., 2024;
d’Ascoli et al., 2025). Finally, we re-framed common EEG classification tasks, i.e., clinical event classification
on the TUEV dataset (Harati et al., 2015) and artifact classification on the TUAR dataset (Hamid et al.,
2020), as multilabel classification tasks to take into account that that some events can overlap.
Note on pretraining data overlap. Existing EEG foundation models are trained on custom corpora curated
by the model authors. As there is a limited set of publicly available EEG datasets, some of these models
saw (part of) the downstream datasets during pretraining. We flag these instances (e.g. with hashed bars
in Figure 4), rather than discard them, as we did not notice a clear trend suggesting pretraining “leakage”
improves downstream performance on the same data.
Finally, while we prioritized breadth over depth in our selection of datasets (i.e., most tasks rely on a single
core dataset), we also leveraged readily available datasets through MOABB13 (Aristimunha et al., 2025) to
offer multiple comparison points on a few tasks, such as motor imagery and P300 decoding. This gives
rise to two benchmark variants: NeuralBench-EEG-Core v1.0, which focuses on a single dataset per task,
and NeuralBench-EEG-Full v1.0, which has up to 24 datasets per task and therefore enables the study of
within-task variability.
In total, NeuralBench-EEG v1.0 covers 36 tasks, 94 datasets, 9,478 subjects and 13,603 hours (see Table 1).
Of note, no data is contained in the released package; datasets are accessed through the standardized interface
provided by NeuralSet and NeuralFetch (King et al., 2026). Also, all datasets sources already provide
de-identified data; as a result, the benchmark only processes de-identified subject IDs. More details on
datasets and downstream tasks can be found in Appendix A and in the benchmark documentation14.
2.3 Modelarchitectureselection
We selected commonly used EEG architectures and foundation models. First, we included 8 task-specific
neural network architectures (Table S2), i.e., models that are trained from scratch on downstream tasks,
typically with lower parameter counts. These include ShallowFBCSPNet and Deep4Net (Schirrmeister et al.,
2017), EEGNet (Lawhern et al., 2018), BDTCN (Gemein et al., 2020), ATCNet (Altaheri et al., 2022),
EEGConformer (Song et al., 2022), SimpleConvTimeAgg (El Ouahidi et al., 2023) and CTNet (Zhao et al.,
2024).
12https://braindecode.org/
13https://moabb.neurotechx.com/
14https://github.com/facebookresearch/neuroai/tree/main/neuralbench-repo
5

Tasks and datasets in NeuralBench-EEG v1.0. For each task, we indicate the Core dataset name, the machine
Table1
learning objective (reg: regression, clf: classification, retr: retrieval), the number of unique EEG channels, the number
ofuniquesubjects,thedimensionalityofthetarget(i.e.,thenumberofoutputs),andthenumberofadditionaldatasets
| in the Full     | variant, if any. |                   |           |               |                 |     |
| --------------- | ---------------- | ----------------- | --------- | ------------- | --------------- | --- |
| Task            |                  | Core dataset      | Obj. #Ch. | #Subj. #Hours | #Out. +Datasets |     |
| Age             |                  | Shirazi2024       | reg 129   | 2,858 95.3    | 1               |     |
| Artifact        |                  | Hamid2020         | clf 26    | 213 300.2     | 5               |     |
| Audiovisual     | stimulus         | MneSample2013     | clf 60    | 1 0.1         | 4               |     |
| Clinical        | event            | Harati2015        | clf 21    | 370 20.1      | 6               |     |
| C-VEP           |                  | Thielen2021       | clf       | 8 30 50.0     | 20              | 7   |
| Dementia        | diagnosis        | Miltiadous2023    | clf 19    | 88 19.5       | 3               |     |
| Depression      | diagnosis        | Mumtaz2018        | clf 19    | 64 20.4       | 2               |     |
| Emotion         |                  | Chen2023          | clf 32    | 123 28.7      | 9               |     |
| Error-related   | negativity       | Kappenman2021Ern  | clf 30    | 40 4.4        | 2               | 2   |
| Image           |                  | Gifford2022       | retr 63   | 10 230.7      | 1,536           |     |
| Mental          | arithmetic       | Zyma2019          | clf 20    | 35 2.3        | 2               | 1   |
| Mental          | imagery          | Scherer2015       | clf 30    | 9 3.9         | 5               |     |
| Mental          | workload         | Hinss2023         | clf 63    | 29 21.4       | 3               | 2   |
| Mismatch        | negativity       | Kappenman2021Mmn  | clf 30    | 40 11.1       | 2               |     |
| Motor execution |                  | Srisrisawang2024  | clf 60    | 20 16.0       | 16              | 2   |
| Motor imagery   |                  | Stieger2021       | clf 60    | 62 141.5      | 4               | 17  |
| N170            |                  | Kappenman2021N170 | clf 30    | 40 3.6        | 2               |     |
| N2pc            |                  | Kappenman2021N2pc | clf 30    | 40 3.6        | 2               | 1   |
| N400            |                  | Kappenman2021N400 | clf 30    | 40 1.3        | 2               |     |
| P300            |                  | Schreuder2010     | clf 60    | 21 70.5       | 2               | 23  |
| Parkinsons      | diagnosis        | Singh2021         | clf 60    | 129 54.9      | 2               |     |
| Pathology       |                  | Lopez2017         | clf 21    | 2,329 971.7   | 2               |     |
| Psychopathology |                  | Shirazi2024       | reg 129   | 2,820 94.0    | 1               |     |
| Reaction        | time             | Shirazi2024       | reg 129   | 1,945 70.8    | 1               |     |
Lateralized readiness poten- Kappenman2021Lrp clf 30 40 4.4 2
tial
| Schizophrenia | diagnosis       | Albrecht2019    | clf 62   | 77 34.6       | 2     |     |
| ------------- | --------------- | --------------- | -------- | ------------- | ----- | --- |
| Seizure       |                 | Dan2023         | clf 24   | 23 982.9      | 2     |     |
| Sentence      |                 | Hollenstein2018 | retr 128 | 12 21.5       | 768   |     |
| Sex           |                 | Shirazi2024     | clf 129  | 2,858 95.3    | 2     |     |
| Sleep arousal |                 | Ghassemi2018    | clf      | 6 994 7,662.3 | 2     |     |
| Sleep stage   |                 | Kemp2000        | clf      | 2 78 1,635.2  | 5     |     |
| Speech        |                 | Brennan2019     | retr 60  | 33 58.5       | 4,096 |     |
| Typing        |                 | Levy2025        | clf 61   | 20 40.7       | 29    |     |
| Video         |                 | Liu2024         | retr 62  | 20 16.3       | 1,408 |     |
| Steady-state  | visually evoked | Wang2017        | clf 64   | 34 9.1        | 40    | 6   |
potential
| Word |     | Nieuwland2018 | retr 74 | 222 441.4 | 1,024 |     |
| ---- | --- | ------------- | ------- | --------- | ----- | --- |
6

Second, we selected 6 EEG foundation models (Table S4), i.e., larger models that have been pretrained on
unlabelled data, and that are typically finetuned on downstream tasks. These are BENDR (Kostas et al.,
2021), LaBraM (Jiang et al., 2024), BIOT (Yang et al., 2023), CBraMod (Wang et al., 2025b), LUNA (Döner
et al., 2025) and REVE (El Ouahidi et al., 2025).
Third, we included representative handcrafted features-based models using sklearn-like pipelines to provide a
non-deep learning comparison point (see Table S3). These pipelines all rely on symmetric positive definite
(SPD) matrix representations of the input EEG which are fed to ‘shallow‘ predictors (logistic or Ridge
regression).
Finally,weincludechance-leveland“dummy” baselinestoofferaproperperformancefloortowhichmodelscan
be compared. Chance-level performance corresponds to the performance obtained by an untrained, randomly
initialized model. “Dummy” performance corresponds to the performance obtained by a model that predicts
either the average target for regression and retrieval tasks, the most frequent class for binary and multiclass
classification tasks, or samples class-wise labels based on training set statistics for multilabel classification
tasks. The dummy models are always fitted on the same training and validation sets as the other models.
2.4 Downstreamstrategyprotocol
The original publications presenting the EEG foundation models listed above use different adaptation recipes,
i.e., for optimization (batch size, optimizer, learning rate, scheduler, etc.), aggregation ([CLS] token, average
patch token, etc.) and projection head design (linear layer, MLP, etc.). Here, to focus the comparison on
model architecture and pretraining methodology, we adopt a shared training recipe.
Eachfoundationmodelisfinetunedend-to-end,usingalinearprojectionheadwhichreceivestheaverage-pooled
output tokens and outputs a single vector matching the target dimension. Training uses AdamW (Loshchilov
and Hutter, 2017) with a learning rate of 10−4, weight decay of 0.05, and cosine-annealing (10% warmup), for
up to 50 epochs with early stopping on the corresponding validation metric (patience=10). The sole exception
to this unified recipe is BENDR (Kostas et al., 2021), for which we lower the learning rate to 10−5 and
apply gradient clipping at 0.5 to obtain stable learning curves. Therefore, model-specific techniques from the
original papers — such as layer-wise learning rate decay, two-stage probing, or LoRA (Hu et al., 2022) — are
intentionally omitted and the comparison of downstream adaptation strategies is kept for future iterations of
NeuralBench. Finally, task-specific architectures are trained from scratch using randomly initialized weights,
using the same optimization recipe as the foundation models.
2.5 Preprocessing
We take particular care to follow the preprocessing pipelines described in the original EEG foundation model
papers, as pretrained checkpoints expect specific input statistics which require identical preprocessing. For
task-specific architectures, we use a single preprocessing configuration inspired by previous EEG decoding
work (Défossez et al., 2022; Benchetrit et al., 2024): resampling to 120 Hz, bandpass filtering between 0.1 and
75 Hz, notch filters at 50 and 60 Hz as well as their harmonics, channel-wise robust scaling at the recording
level, followed by clamping at 20. Nevertheless, it will be important, in future iterations, to systematically
evaluate the impact of preprocessing strategies on downstream evaluation.
2.6 DataSplitting
The generalization capacity of a model can be highly dependent on the task. Consequently, to split datasets
into training, validation and testing sets, we use different strategies for each task: (1) predefined splits when
provided by the authors, (2) “leave-concept-out” for cognitive decoding tasks, (3) cross-subject splits, with
optional stratification for clinical tasks, or (4) random splits when very few examples are available. We train
(or finetune) each model on each task three times, using a single train/valid/test partition but three different
random seeds for the initialization of the (non-pretrained) model weights. See Appendix C for more details.
7

2.7 Trainingandevaluationmetrics
The training, finetuning and evaluation of the models must vary depending on the task objective. In binary
and multiclass classification tasks, we use cross-entropy with optional weighing to mitigate class imbalance.
In multilabel classification tasks, we instead use binary cross-entropy per target. Regression tasks rely on the
mean squared error (MSE) loss. Finally, we also implemented retrieval tasks, where a model must recover
which candidate target out of a given retrieval set actually corresponds to the input (e.g. which image out of
a set of multiple images seen by a participant, based on an input EEG window). Retrieval is a particularly
well-posed problem for cognitive tasks, as the content of an image, text or video is neither categorical, nor
necessarily perfectly specified in a pretrained embedding. Retrieval ultimately allows future models and
approaches to be compared with one another, with little assumption on how to represent the target. For
retrieval, wehererelyontheCLIPloss(Radfordetal.,2021), usingtheconfigurationofDéfossezetal.(2022),
i.e., with the brain-to-target term only and a fixed temperature parameter τ =1:
B
|     |     |         | 1 (cid:88) | exp(s(zˆ ,z | )/τ) |     |
| --- | --- | ------- | ---------- | ----------- | ---- | --- |
|     |     | L (θ)=− | log        | i           | i    | (1) |
|     |     | CLIP    | (cid:80)B  |             |      |     |
|     |     |         | B          | exp(s(zˆ,z  | )/τ) |     |
|     |     |         | i=1        | j=1         | i j  |     |
where B is the batch size, s is the cosine similarity, and z and zˆ are the target dense embedding (e.g.
i i
DINOv2 (Oquab et al., 2024) for image retrieval) and corresponding prediction for batch element i.
2.8 Modelcomparison
To help summarize the comparison across models, we opted to report a single representative metric per task
type: i.e., balanced accuracy for binary and multiclass classification, F1-score for multilabel classification,
Pearson correlation for regression, and top-5 accuracy for retrieval15. See Appendix D for more details. We
further report normalized scores s˜to facilitate cross-task comparisons and emphasize task difficulty:
|     |     |     | s−s dummy |       |     |     |
| --- | --- | --- | --------- | ----- | --- | --- |
|     |     |     | s˜=       |       |     | (2) |
|     |     |     | s −s      |       |     |     |
|     |     |     | perfect   | dummy |     |     |
where s is the performance obtained by the dummy model on a specific dataset, and s is the
dummy perfect
metric-specific theoretical highest performance obtainable (e.g. 100% balanced accuracy for classification
tasks). Of note, due to the inherent noise in brain activity recordings, this perfect score cannot be attained in
practice. With this formulation, a value of 0 indicates dummy-level performance and a value of 1 indicates
perfect performance.
Finally, global model rankings consists of the per-task rank of each model, averaged over all tasks. On
NeuralBench-EEG-Full v1.0, we additionally use all available datasets to compute this ranking, i.e., we
| average ranks | across datasets | of the same | task first. |     |     |     |
| ------------- | --------------- | ----------- | ----------- | --- | --- | --- |
2.9 Computationalconsiderations
NeuralBench-EEG-Fullv1.0requiresrunning4,947experiments. (14models+chance,dummy&handcrafted
features baselines, 97 tasks-datasets, 3 seeds each). By default, each job uses a single GPU with at least
32 GB VRAM and 64 GB of CPU RAM, though measured peak GPU usage averages only ∼1.3 GB (max
∼30.3 GB). The full EEG benchmark requires ∼11 TB of disk space (∼3.2 TB for the raw data, 7.8 TB of
preprocessed cache, and 333 GB for logged results). Training times vary widely, with a median of 2.7 minutes
but mean of 21.7 minutes per experiment, with the longest run taking 18.2 hours. This yields an estimated
total serial runtime of ∼73 days (1,751 GPU-hours). The benchmark runs on Python >= 3.12 with PyTorch
2.6 (Paszke et al., 2019) and Pytorch-Lightning (Falcon and The PyTorch Lightning team, 2019).
15Weevaluatetop-5accuracyontheentiretestset,usingwithin-subjectaggregationofrepeatedpredictions,ifavailable.
8

Mean norm.
rank
RREEVVEE (69.2M; 2025) 0.20 Foundation
LLaaBBrraaMM (5.8M; 2024) 0.21 BENDR
BIOT
LLUUNNAA (40.4M; 2025) 0.30
LaBraM
CCTTNNeett (150K; 2024) 0.32 CBraMod
CCBBrraaMMoodd (4.9M; 2025) 0.33 LUNA
REVE
SSiimmpplleeCCoonnvvTTiimmeeAAgggg (4.2M; 2023) 0.35
SShhaalllloowwFFBBCCSSPPNNeett (36K; 2017) 0.43 Task-specific
DDeeeepp44NNeett (146K; 2017) 0.43 ShallowFBCSPNet
Deep4Net
EEEEGGCCoonnffoorrmmeerr (277K; 2022) 0.45
EEGNet
EEEEGGNNeett (1K; 2018) 0.47 BDTCN
BBEENNDDRR (157.1M; 2021) 0.57 EEGConformer
AATTCCNNeett (29K; 2022) 0.59 ATCNet
SimpleConvTimeAgg
Handcrafted 0.60 CTNet
BBIIOOTT (3.2M; 2023) 0.64
BBDDTTCCNN (27K; 2020) 0.73 Baselines
Chance
Dummy 0.92
Dummy
Chance 0.94 Handcrafted
0.00 0.25 0.50 0.75 1.00
Normalized rank (lower is better)
Figure3 Model ranking on NeuralBench-EEG-Core v1.0. Each box corresponds to the rank distribution of one model
across downstream tasks. Models are ordered by their mean normalized rank, displayed on the right hand side of
the boxes. The number of trainable parameters (excluding the last linear projection layer) and the year of original
publication are shown in parentheses next to each model name. Recent foundation models outrank most smaller
task-specific models, suggesting large self-supervised pretraining can benefit downstream performance on a varied set
of downstream tasks.
3 Results
3.1 NeuralBench-EEGv1.0: EvaluatingEEGfoundationmodelson36diversedownstream
tasks
We summarize per-model performance in Figure 3, where we order the models based on their average per-
task rank. While the highest scoring models are foundation models, i.e., REVE (El Ouahidi et al., 2025),
LaBraM (Jiang et al., 2024) and LUNA (Döner et al., 2025), some task-specific architectures trained from
scratch also perform well, e.g. CTNet (Zhao et al., 2024), SimpleConvTimeAgg (Défossez et al., 2022) and
Deep4Net (Schirrmeister et al., 2017), despite significantly lower parameter counts (e.g. 150K parameters for
CTNet vs. 69.2M for REVE). This is in line with Kastrati et al. (2025) and Wu et al. (2025) which reported
similar results. Of note, BENDR (Kostas et al., 2021) and BIOT (Yang et al., 2023) did not perform as well
overall despite their pretraining, which might in part be explained by the necessary addition of a channel
adapter linear layer to match the expected channel montage seen during pretraining, and, for BIOT, to the
use of a linear projection head rather than a large MLP head like in the original publication.
3.2 Future-proofingevaluationthroughtaskdiversityanddifficulty
DetailedperformanceresultsforeachdownstreamtaskandmodelarepresentedinFigure4andFigure5. The
resultssuggestthatperformanceoverafewcommonEEGtasksisclosetosaturation,e.g.SSVEPclassification,
pathology, seizure detection, sleep stage classification and phenotyping tasks, i.e., age regression and sex
classification.
In contrast, the cognitive decoding tasks are particularly challenging. These tasks, introduced in NeuralBench
(e.g. speech, sentence, video, word and image decoding), consist of decoding dense representations of the
stimulus or condition from the brain activity. Foundation models particularly stand out on these compared to
9

|     | Mean norm. |     | Image |     | Sentence |     | Speech |     | Typing | Video | Word |     |     |
| --- | ---------- | --- | ----- | --- | -------- | --- | ------ | --- | ------ | ----- | ---- | --- | --- |
Best rank ↑ Top-5 accuracy (per-subject) Top-5 accuracy (per-subject) Top-5 accuracy (per-subject) Balanced accuracy Top-5 accuracy (per-subject) Top-5 accuracy (per-subject)
|           | (0) |     |     |     |     |     |     | 6   |     |     | 20  |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| evitingoC |     | 75  |     | 10  |     |     |     |     |     |     |     |     |     |
|           |     |     |     |     |     | 4   |     | 4   |     | 4   |     |     |     |
50
|     |     |     |     | 5   |     | 2   |     |     |     | 2   | 10  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | 25  |     |     |     |     |     | 2   |     |     |     |     |     |
Wo ( r 1 s ) t 0 within-subject  ·  n=831K 0 within-subject  ·  n=26K 0 within-subject  ·  n=70K 0 within-subject  ·  n=147K 0 within-subject  ·  n=29K 0 within-subject  ·  n=530K
Mean norm.
rank ↑ c-VEP Mental imagery Motor execution Motor imagery P300 SSVEP
Be (0 st ) Balanced accuracy Balanced accuracy 60 Balanced accuracy Balanced accuracy 70 Balanced accuracy 100 Balanced accuracy
|     |     | 75  |     | 30  |     |     |     | 60  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
6 0
| ICB |       |     |     |     |     | 40  |     | 40  |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |       | 50  |     | 20  |     |     |     |     |     |     | 50  |     |     |
|     |       |     |     |     |     | 20  |     |     |     | 5 0 |     |     |     |
|     |       | 25  |     |     |     |     |     | 20  |     |     |     |     |     |
| Wo  | r s t |     |     | 10  |     |     |     |     |     | 40  |     |     |     |
( 1 ) 0 cross-subject  ·  n=45K 0 within-subject  ·  n=3.5K 0 cross-subject  ·  n=19K 0 cross-subject  ·  n=127K 0 cross-subject  ·  n=254K 0 cross-subject  ·  n=8.2K
|     | Mean norm. |     | Audiovisual |     | ERN |     | MMN |     | N170 | N2pc | N400 |     | LRP |
| --- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | ---- | ---- | ---- | --- | --- |
sesnopseR dekovE rank ↑ Balanced accuracy Balanced accuracy Balanced accuracy Balanced accuracy Balanced accuracy Balanced accuracy Balanced accuracy
| Be  | (0 st ) |     |     |     |     |     |     | 80  |     |     |     | 80  |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |         | 60  |     | 80  |     | 60  |     |     |     |     |     |     |     |
|     |         |     |     |     |     |     |     |     |     | 60  | 60  |     |     |
|     |         | 40  |     |     |     |     |     | 60  |     |     |     | 60  |     |
|     |         |     |     | 60  |     | 50  |     |     |     | 50  | 50  |     |     |
20
|     |       |     |     | 40  |     | 40  |     | 40  |     | 40  | 40  | 40  |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Wo  | r s t | 0   |     | 0   |     | 0   |     | 0   |     | 0   | 0   | 0   |     |
( 1 ) random  ·  n=288 cross-subject  ·  n=16K cross-subject  ·  n=40K cross-subject  ·  n=13K cross-subject  ·  n=13K cross-subject  ·  n=4.8K cross-subject  ·  n=16K
Mean norm. Clinical event Dementia Depression Parkinson's Pathology Schizophrenia Seizure
Be st rank ↑ F1 score (macro) Balanced accuracy Balanced accuracy Balanced accuracy Balanced accuracy Balanced accuracy Balanced accuracy
|          | (0 )  | 0.6 |     | 50  |     |     |     | 80  |     | 80  |     |     |     |
| -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|          |       |     |     |     |     | 80  |     |     |     |     |     | 80  |     |
| lacinilC |       | 0.4 |     | 40  |     |     |     |     |     |     | 60  |     |     |
|          |       |     |     |     |     |     |     | 60  |     | 60  |     |     |     |
|          |       |     |     |     |     | 60  |     |     |     |     |     | 60  |     |
|          |       | 0.2 |     | 30  |     |     |     |     |     |     | 40  |     |     |
|          |       |     |     |     |     | 40  |     | 40  |     | 40  |     | 40  |     |
| Wo       | r s t | 0.0 |     | 0   |     | 0   |     | 0   |     | 0   | 0   | 0   |     |
( 1 ) cross-subject  ·  n=24K cross-subject  ·  n=14K cross-subject  ·  n=15K cross-subject  ·  n=40K cross-subject  ·  n=700K cross-subject  ·  n=25K cross-subject  ·  n=708K
|      | Mean norm. |     | Emotion           |     | Mental arith.     |     | Workload          |     |     |     |     |     |     |
| ---- | ---------- | --- | ----------------- | --- | ----------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
| Best | rank ↑     |     | Balanced accuracy |     | Balanced accuracy |     | Balanced accuracy |     |     |     |     |     |     |
etatS lanretnI (0)
|     |     | 30  |     | 70  |     | 60  |     |     |     |           |     |                   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ----------------- | --- |
|     |     | 20  |     | 60  |     | 40  |     |     |     | Baselines |     | Foundation models |     |
50
|     |       | 10  |     |     |     | 20  |     |     |     | Chance |     | BENDR |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ----- | --- |
|     |       |     |     | 40  |     |     |     |     |     | Dummy  |     | BIOT  |     |
| Wo  | r s t | 0   |     | 0   |     | 0   |     |     |     |        |     |       |     |
( 1 ) cross-subject  ·  n=21K cross-subject cross-subject  ·  n=15K Handcrafted LaBraM
|     |            |     |     |     |                 |     |     |     |     | Seen during |     | CBraMod |     |
| --- | ---------- | --- | --- | --- | --------------- | --- | --- | --- | --- | ----------- | --- | ------- | --- |
|     | Mean norm. |     | Age |     | Psychopathology |     | Sex |     |     |             |     |         |     |
Be st rank ↑ Pearson R 0.15 Pearson R Balanced accuracy pretraining LUNA
gnipytonehP (0 )
|     |     | 0.6 |     |      |     | 80  |     |     |     |                      |     | REVE |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | -------------------- | --- | ---- | --- |
|     |     |     |     | 0.10 |     |     |     |     |     | Task-specific models |     |      |     |
|     |     | 0.4 |     |      |     | 60  |     |     |     | ShallowFBCSPNet      |     |      |     |
0.05
|     |     | 0.2 |     |     |     |     |     |     |     | Deep4Net |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
40
Wo ( r 1 s ) t 0.0 cross-subject  ·  n=171K 0.00 cross-subject  ·  n=169K 0 cross-subject  ·  n=171K EEGNet
BDTCN
Mean norm.
|              | rank ↑ |     | Sleep arousal     |     | Sleep stage       |     | Artifact         |     | Reaction time | EEGConformer      |     |     |     |
| ------------ | ------ | --- | ----------------- | --- | ----------------- | --- | ---------------- | --- | ------------- | ----------------- | --- | --- | --- |
| Best         | (0)    |     | Balanced accuracy |     | Balanced accuracy |     | F1 score (macro) |     | Pearson R     | ATCNet            |     |     |     |
| csiM / peelS |        | 60  |                   |     |                   |     |                  |     |               |                   |     |     |     |
|              |        |     |                   | 60  |                   | 0.4 |                  | 0.4 |               | SimpleConvTimeAgg |     |     |     |
CTNet
|     |     | 50  |     | 40  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | 0.2 |     | 0.2 |     |     |     |     |     |
20
| Wo  | r s t | 40  |                          |     |                          |     |                          |     |                          |     |     |     |     |
| --- | ----- | --- | ------------------------ | --- | ------------------------ | --- | ------------------------ | --- | ------------------------ | --- | --- | --- | --- |
|     | ( 1 ) | 0   | cross-subject  ·  n=1.8M | 0   | cross-subject  ·  n=196K | 0.0 | cross-subject  ·  n=360K | 0.0 | cross-subject  ·  n=127K |     |     |     |     |
Figure4 Performanceobtainedbythedifferenttask-specific(blue)andfoundation(orange)modelsonthe36downstream
tasks in NeuralBench-EEG-Core v1.0. Rows correspond to specific downstream task categories; the first subplot of
each row summarizes the model ranking over the corresponding task category row. Each bar corresponds to one
model, with error bars representing standard error of the mean (SEM) across seeds. Hashed bars indicate models
that were pretrained on the downstream dataset, meaning the reported performance could be overinflated since test
subjects or examples may have been seen by the model. Dummy-level performance is evaluated for each task by
predicting the majority class (classification) or the average target (regression and retrieval) computed on the training
set. Handcrafted baselines uses sklearn pipelines which ingest covariance-like features to provide a non-deep learning
baseline (see Table S3). Finally, the splitting strategy (cross-subject, within-subject or random) and the total number
| of examples |     | across | splits are | listed | under | each | subplot. |     |     |     |     |     |     |
| ----------- | --- | ------ | ---------- | ------ | ----- | ---- | -------- | --- | --- | --- | --- | --- | --- |
task-specific models, e.g. REVE leads on the sentence, speech and video decoding tasks.
Models perform significantly worse on NeuralBench’s rarer paradigms, including mental imagery, sleep
arousal, and psychopathology decoding, highlighting the difficulty of these specific decoding tasks. Moreover,
standardbenchmarktasks,i.e.,motorimagery,P300andN2pcclassification,becomeparticularlychallenging
when framed as cross-subject tasks, often yielding performance close to dummy level. Given the substantial
margin between current results and performance ceiling, these tasks represent ideal benchmarks for future-
| proofing | the | evaluation | of  | the | next generation |     | of EEG | models. |     |     |     |     |     |
| -------- | --- | ---------- | --- | --- | --------------- | --- | ------ | ------- | --- | --- | --- | --- | --- |
10

1.0
0.8
0.6
0.4
0.2
0.0
Typi S n p g eech V S id e e n o tence Wor I d mage
̃s
erocs
dezilamroN
Evoked Internal
Cognitive BCI Responses Clinical State Sleep Phenotyping Misc
Perfect
Dummy
Mental i m M a o g t e o r r y M P e 3 x o e 0 t c o 0 u r t i i m on agery c-VE S P SVEP M MN N40 A 0 u N d 2 i p o c visua N l 170 LRP ERN D C e l m in e i S c n a c t h l i a e iz v o e p n P h t a re rk n i i n a s P o a n th 's olo S g D e y e iz p u r r e e ssion E M m e o n t t i a o l n a W ri o th rk . loa S d leep aro S u l s e a e l p s P t s a y g c e hopathology Age Sex A R r e ti a fa c c ti t on ti me
Best foundation model Best task-specific model Foundation model wins
Mean over foundation models Mean over task-specific models Task-specific model wins
Figure5 Normalized performance s˜across downstream tasks, for the best and “average” foundation model (orange)
and best and “average” task-specific models (blue). A value of 0.0 corresponds to dummy-level performance, while a
value of 1.0 represents perfect (idealized) performance. Horizontal bars on the x-axis indicate which model category
yield the highest performance overall for a given task. While foundation models often outperform task-specific models,
this is not the case across all tasks, e.g. in evoked responses and clinical downstream tasks. Cognitive decoding tasks
introduced in NeuralBench-EEG v1.0 are particularly challenging, which position them well for evaluating future
iterations of EEG foundation models.
3.3 FromNeuralBench-CoretoNeuralBench-Full: Leveragingmulti-studytasksforevaluating
cross-datasetvariability
The results above focused on NeuralBench-EEG-Core v1.0, a version of the benchmark where each task is
summarized by a single representative “core” dataset. We also introduce NeuralBench-EEG-Full v1.0, an
extended version of the benchmark in which downstream tasks may include additional datasets on top of
their core dataset, which we leverage in two ways.
First, we compare models as above, but this time using dataset-averaged ranks whenever multiple datasets are
available for a task, yielding a more robust ordering of models. The “Core” and “Full” rankings are compared
in Figure 6A. A Kendall’s τ of 0.926 (p < 0.001) between the two rankings suggests the “Core” ranking is
a good proxy for the “Full” one. However, we notice that a few models swap positions in the ranking, e.g.
CTNet overtakes the LUNA foundation model as third best in the “Full” ranking. This shows the gap between
task-specific and foundation models is narrow enough that expanding dataset coverage is sufficient to change
global ranking.
Second, we evaluate within-task variability by inspecting ranking changes in NeuralBench-EEG-Full v1.0’s
multi-dataset tasks (Figure 6B). REVE and LaBraM are the most stable foundation models, with the former
experiencing the least rank variability of all models. On the task dimension, we notice strong variability
on motor imagery and SSVEP in particular. For instance, on SSVEP, performance on the core dataset
(Wang et al., 2017) and on Lee et al. (2019) is mostly dominated by foundation models (LaBraM and REVE),
task-specific models outperform all other models on Oikonomou et al. (2016) version A, and the handcrafted
features-based baseline outperforms all or most other models on Kalunga et al. (2016) and Oikonomou et al.
(2016) versions B and C (see Supplementary Figure S2 for details). This strong variability suggests that
multi-study comparisons are necessary to fully characterize the behavior of brain models.
Moving forward, the availability of multiple datasets per task will allow testing generalization and invariance
properties of foundation models over varying recording hardware, lab environments and subject populations.
It also opens the door to multi-dataset finetuning and evaluation, e.g. in which models are finetuned on a
11

A
Climbed
Dropped
Same
A g g
im e P N e t e r
|     |     |     |      |        |                      | n v T B C S    | t fo r m          |               | fte d   |     |              |
| --- | --- | --- | ---- | ------ | -------------------- | -------------- | ----------------- | ------------- | ------- | --- | ------------ |
|     |     |     |      | LaBraM | CTNet CBraM o d mple | C o o w F 4 N  | e Co n N e t ENDR | ATCNe t andcr | a BDTCN |     | Dumm y hance |
|     |     |     | REVE | LUNA   | i                    | h a ll D e e p | E G E G B         | H             | B IO T  |     | C            |
|     |     |     |      |        | S                    | S E            | E                 |               |         |     |              |
NeuralBench-EEG-Core v1.0
(1 dataset/task)
NeuralBench-EEG-Full v1.0
(All datasets)
|     |     |     | 4   | 5   | 6 7 | 8 9 | 10  | 11  | 12 13 | 14  | 15 16 17 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | -------- |
Mean rank
| B   |     |     | Task-specific |     |     |     | Foundation |     |     | Baseline |     |
| --- | --- | --- | ------------- | --- | --- | --- | ---------- | --- | --- | -------- | --- |
g g
|     |     |        | et     |         | e A        |      |       |       |         |        |            |
| --- | --- | ------ | ------ | ------- | ---------- | ---- | ----- | ----- | ------- | ------ | ---------- |
|     |     |        | N      |         | m r        |      |       |       |         |        |            |
|     |     |        | S P    |         | T i m e    |      |       |       |         |        | d          |
|     |     | wFB    | C      | mpleCon | v o r Net  |      |       |       |         |        | Handcrafte |
|     | Net |        |        |         | nf         | Net  | M     |       | Mod     | Chance | my         |
|     |     | Shallo | et DTC | N       | C o p4     | REVE | LaBra | DR OT | CBra NA |        | m ean      |
|     | ATC |        | T N    |         | E G e e EE | G    |       | BE N  | LU      | Du     |            |
|     |     |        | C B    | Si      | E D        |      |       | BI    |         |        | M          |
P300 (N=24) 1.7 1.9 2.5 2.0 3.1 1.8 2.4 2.9 3.0 2.6 2.9 1.6 3.1 2.6 2.9 1.1 3.7 2.5
c-VEP (N=8) 0.9 2.4 2.0 2.7 2.6 3.4 3.3 2.9 3.2 1.7 2.8 1.7 3.7 4.1 2.6 1.3 4.4 2.7
Motor imagery (N=18) 3.4 4.3 2.8 4.1 4.4 2.8 3.7 4.6 1.7 3.8 4.0 4.7 4.4 4.4 3.3 2.1 5.5 3.8
SSVEP (N=7) 3.4 2.5 4.4 3.6 3.1 6.0 4.8 4.3 3.8 4.1 2.5 6.0 3.0 3.7 3.5 2.0 3.4 3.8
Mean 2.4 2.8 2.9 3.1 3.3 3.5 3.6 3.7 2.9 3.0 3.0 3.5 3.6 3.7 3.1 1.6 4.3 3.2
|     |     |     |     | 0.9 |     | 3.5 |     |     | 6.0 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Rank std (↓)
Figure6 Analysingmulti-datasetperformanceonNeuralBench-EEG-Fullv1.0. A.Differenceinmodelrankingbetween
the Core and Full variants of NeuralBench-EEG v1.0. Models whose global rank improve or degrade when using the
full version of the benchmark are indicated by green or black lines, respectively. The ranking is not affected much by
the addition of multiple datasets per task, which suggests Core datasets are overall representative. Within-task
B.
model ranking variability. We report the standard deviation of each model’s ranks across the different datasets of a
task (for tasks with 5 datasets or more). Higher values indicate a model’s performance relative to the other models
varysubstantially,meaningthemodelisnotstablewhenevaluatedacrossmultipledatasetsofthesamedomain. Tasks
like motor imagery and SSVEP, and foundation models like CBraMod and LUNA, are the most unstable.
12

|     |     |     |                              |     | MEG |                   |        |                              | fMRI  |
| --- | --- | --- | ---------------------------- | --- | --- | ----------------- | ------ | ---------------------------- | ----- |
|     |     |     | Image                        |     |     |                   | Typing |                              | Image |
|     |     |     | Top-5 accuracy (per-subject) |     |     | Balanced accuracy |        | Top-5 accuracy (per-subject) |       |
|     |     |     | 80                           |     |     |                   |        | 80                           |       |
10
|     |     |     | 60  |     |     |     |     | 60  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | 40  |     |     |     |     | 40  |     |
5
|     |     |     | 20                       |     |     |                           |     | 20  |                |
| --- | --- | --- | ------------------------ | --- | --- | ------------------------- | --- | --- | -------------- |
|     |     |     | 0                        |     | 0   |                           |     | 0   |                |
|     |     |     | within-subject  ·  n=99K |     |     | within-subject  ·  n=193K |     |     | within-subject |
Baselines EEG task-specific models EEG foundation models fMRI task-specific models
|     |     | Chance      | ShallowFBCSPNet |     |     |     | BENDR   |     | FmriLinear |
| --- | --- | ----------- | --------------- | --- | --- | --- | ------- | --- | ---------- |
|     |     | Dummy       | Deep4Net        |     |     |     | BIOT    |     | FmriMlp    |
|     |     | Handcrafted | EEGNet          |     |     |     | LaBraM  |     |            |
|     |     |             | BDTCN           |     |     |     | CBraMod |     |            |
|     |     |             | EEGConformer    |     |     |     | LUNA    |     |            |
|     |     |             | ATCNet          |     |     |     | REVE    |     |            |
SimpleConvTimeAgg
CTNet
Performance obtained on MEG and fMRI downstream tasks. Each bar corresponds to one model, with
Figure7
error bars representing standard error of the mean (SEM) across seeds. See Figure 4 for more details. This first
benchmark release focuses on EEG, however, as a unified framework, NeuralBench is ready to support other brain
| imaging                                   | modalities | as well.  |               |     |               |     |            |               |     |
| ----------------------------------------- | ---------- | --------- | ------------- | --- | ------------- | --- | ---------- | ------------- | --- |
| subset of                                 | task       | datasets, | and evaluated | on  | the remaining |     | held       | out datasets. |     |
| 3.4 ExtendingNeuralBenchtomoremodalities: |            |           |               |     |               |     | MEGandfMRI |               |     |
The focus of this first NeuralBench release is EEG. However, the benchmark infrastructure already provides
support for other neuroimaging modalities, which we demonstrate by including results on two MEG and one
| fMRI downstream |     | tasks | (see Figure | 7). |     |     |     |     |     |
| --------------- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- |
For MEG, given the similarities between the two types of data (da Silva, 2013) and the common reuse of
EEG architectures on MEG (Banville et al., 2025), we evaluate the same task-specific and foundation models
as for EEG. Expectedly, some architectures yield high performance on MEG, such as SimpleConvTimeAgg
which was already shown to perform well on image decoding on the same dataset (Benchetrit et al., 2024).
More strikingly, some EEG foundation models, despite being pretrained on EEG data exclusively, perform
well on MEG, with REVE outperforming all other models on typing decoding. Finally, on fMRI, we present
results on a similar image decoding task as in EEG and MEG, but focused on two task-specific architectures
that rely on linear and convolutional layer primitives. These results exhibit the flexibility of NeuralBench,
which is ready to be extended to other modalities as well, such as iEEG, functional near-infrared spectroscopy
| (fNIRS), | and other | neural | signal | types such | as  | electromyography |     | (EMG). |     |
| -------- | --------- | ------ | ------ | ---------- | --- | ---------------- | --- | ------ | --- |
Overall, in this section, we highlighted NeuralBench’s comprehensive downstream task coverage, its versatility,
allowing easy between- and within-task performance comparisons, and its extendability to more neuroimaging
devices.
4 Discussion
EEG foundation vs. task-specific models. We introduce NeuralBench, a unifying framework to benchmark
NeuroAI models, and release v1.0, a first comprehensive benchmark evaluating existing
NeuralBench-EEG
task-specific and foundation models of EEG signals. Our results already reveal that current EEG foundation
models only marginally outperform specialized models. While self-supervised pretraining yields generalizable
representations, downstream performance gains remain limited. This modest advantage may stem from the
use of finetuning as a downstream strategy: in data-rich scenarios, specialized models likely possess sufficient
capacitytoclosetheperformancegapwithfoundationmodels. Futureevaluationsshouldthusalsoincorporate
| evaluations | in  | few-shot | and low-data | regimes | (e.g. | 5%  | of training | data). |     |
| ----------- | --- | -------- | ------------ | ------- | ----- | --- | ----------- | ------ | --- |
13

EEG task expansions. NeuralBench-EEG v1.0significantlyexpandsthediversityofdownstreamevaluations
by introducing and integrating a large set of cognitive, phenotyping, clinical and BCI “tasks”. Across most of
these tasks, performance remains modest, which leaves room for improvement in next generations of EEG
foundationmodels. Inthefuture,werecommendmaintainingadiversesetoftasks–someeasy,othersdifficult
– to validate the ability of models to extract valuable information from noisy brain signals, while ensuring that
benchmarking is representative of downstream neuroscience and clinical applications.
Unique optimization strategies. Rather than pursuing model-specific optimization, we utilize a standardized
trainingrecipetoevaluateeacharchitecture’s“out-of-the-box” utility. Thisdecisionreflectsacorerequirement
for NeuroAI foundation models: they must be easily adaptable and stable under standard configurations to
be practically useful for the broader research community.
Unique splitting strategy. We used specific splitting strategies to maintain a manageable computational
footprint while ensuring diverse task coverage. Although this choice limits the assessment of performance
variability(ascomparedtoacross-validatedapproach),itestablishesabroadbaselineforevaluatingfoundation
models. We invite the community to help incorporate stochastic partitioning in future releases to facilitate
deeper statistical validation.
Unique finetuning strategy. NeuralBench currently relies on end-to-end finetuning, which may not capture
the full potential of foundation models. Alternative strategies, such as linear probing, parameter-efficient
finetuning (Hu et al., 2022; Lester et al., 2021) and varied token aggregation methods may further improve
performance and differentiate models from one another. These dimensions should thus be studied in greater
detail in future iterations of the benchmark.
Beyond EEG. While this first release focuses on EEG – given its prominence in the brain foundation model
literature (Yang et al., 2025) – NeuralBench’s infrastructure based on the NeuralSet ecosystem (King et al.,
2026) is highly flexible. We demonstrate this with preliminary MEG and fMRI tasks, paving the way for a
truly multimodal benchmark, and strikingly, already showing promising transfer from EEG to MEG. However,
extending to new modalities requires significant data curation and introduces device-specific challenges, such
as high auto-correlation in fMRI that complicates train/test splits (Poldrack, 2006).
Beyonddecoding. Thecurrentbenchmarkisrestrictedtotheevaluationofmodelswhichreceivebrainactivity
as input, and predict a target label or embedding, i.e., decoding models. However, encoding models (Naselaris
etal.,2011),whichpredictbrainactivityfromstimuli,arealsoactivelybeingdeveloped. Existingbenchmarking
efforts in the neuroAI community, including machine learning competitions, are focused on encoding, e.g. the
Algonauts project (Cichy et al., 2021; Gifford et al., 2023, 2024) on image and video encoding in human fMRI,
the Sensorium competition (Willeke et al., 2022; Turishcheva et al., 2024) on image and video encoding in
mouse visual cortex calcium imaging, and the Brain-Score platform (Schrimpf et al., 2018, 2020) on visual and
language encoding in primate electrode recordings and human fMRI. Integrating encoding, forecasting, and
denoising tasks presents unique challenges, e.g. standardizing stimuli representations and evaluation metrics,
but can be readily accommodated within the NeuralBench framework.
Opencallforcommunitycontribution. Buildingauniversalbenchmarkforbrainactivityisavastundertaking,
unlikely to be achieved by a single team. We therefore open-source the NeuralBench codebase16 and invite
the community to contribute new datasets, tasks, models, and neuroimaging modalities.
Towards a unified modeling of brain activity. Ultimately, brain foundation models have the potential to
revolutionizebrain-computerinterfacing,neurology,andneuroscience. Movingtowardtheintegratedprocessing
ofmultimodalbraindatarequiresrigorous,reproducible,andcomprehensiveevaluation. WehopeNeuralBench
serves as a foundational tool to seed and support this community-wide effort.
16https://github.com/facebookresearch/neuroai/tree/main/neuralbench-repo
14

Acknowledgments
We thank Alexandre Gramfort, Thomas Moreau, Arnaud Delorme, Bruno Aristimunha and Pierre Guetschel
for their feedback on benchmarking best practices and the NeuroAI open-source ecosystem. We thank the
maintainers and contributors of the open-source software packages on which NeuralBench is built. Finally, we
thank the authors and participants of the datasets used in this research for their fundamental contribution to
the advancement of open NeuroAI models.
15

References
Alexandre Abraham, Fabian Pedregosa, Michael Eickenberg, Philippe Gervais, Andreas Mueller, Jean Kossaifi,
Alexandre Gramfort, Bertrand Thirion, and Gaël Varoquaux. Machine learning for neuroimaging with scikit-learn.
Frontiers in neuroinformatics, 8:14, 2014.
Laura Acqualagna and Benjamin Blankertz. Gaze-independent BCI-spelling using rapid serial visual presentation
(RSVP). Clinical Neurophysiology, 124(5):901–908, May 2013. ISSN 1388-2457. doi: 10.1016/j.clinph.2012.12.050.
http://dx.doi.org/10.1016/j.clinph.2012.12.050.
Matthew A. Albrecht, James A. Waltz, James F. Cavanagh, Michael J. Frank, and James M. Gold. Increased
Conflict-Induced slowing, but no differences in Conflict-Induced positive or negative prediction error learning in
patients with schizophrenia. Neuropsychologia, 123:131–140, February 2019. ISSN 1873-3514. doi: 10.1016/j.
neuropsychologia.2018.04.031.
Emily J Allen, Ghislain St-Yves, Yihan Wu, Jesse L Breedlove, Jacob S Prince, Logan T Dowdle, Matthias Nau, Brad
Caron, Franco Pestilli, Ian Charest, et al. A massive 7T fMRI dataset to bridge cognitive neuroscience and artificial
intelligence. Nature neuroscience, 25(1):116–126, 2022.
Hamdi Altaheri, Ghulam Muhammad, and Mansour Alsulaiman. Physics-informed attention temporal convolutional
network for eeg-based motor imagery classification. IEEE Transactions on Industrial Informatics, 2022. doi:
10.1109/TII.2022.3197419.
Pietro Aricò, Fabio Aloise, Francesca Schettini, Serenella Salinari, Donatella Mattia, and Febo Cincotti. Influence
of P300 latency jitter on event related potential-based brain–computer interface performance. Journal of Neural
Engineering, 11(3):035008, 2014. doi: 10.1088/1741-2560/11/3/035008.
Bruno Aristimunha, Igor Carrara, Pierre Guetschel, Sara Sedlar, Pedro Rodrigues, Jan Sosulski, Divyesh Narayanan,
Erik Bjareholt, Quentin Barthelemy, Robin Tibor Schirrmeister, Reinmar Kobler, Emmanuel Kalunga, Ludovic
Darmet,CattanGregoire,AliAbdulHussain,RamiroGatti,VladislavGoncharenko,AntonAndreev,JordyThielen,
Thomas Moreau, Yannick Roy, Vinay Jayaram, Alexandre Barachant, and Sylvain Chevallier. Mother of all BCI
benchmarks, 2025. https://github.com/NeuroTechX/moabb.
Bruno Aristimunha, Pierre Guetschel, Martin Wimpff, Lukas Gemein, Cedric Rommel, Hubert Banville, Maciej
Sliwowski, Daniel Wilson, Simon Brandt, Théo Gnassounou, Joseph Paillard, Aman Srivastava, Bruna Junqueira
Lopes, Sara Sedlar, Thomas Moreau, Sylvain Chevallier, Alexandre Gramfort, and Robin Tibor Schirrmeister.
Braindecode: toolbox for decoding raw electrophysiological brain data with deep learning models, 2026. https:
//github.com/braindecode/braindecode.
Mehdi Azabou, Vinam Arora, Venkataramana Ganesh, Ximeng Mao, Santosh Nachimuthu, Michael Mendelson, Blake
Richards, Matthew Perich, Guillaume Lajoie, and Eva Dyer. A unified, scalable framework for neural population
decoding. Advances in Neural Information Processing Systems, 36:44937–44956, 2023.
AlexeiBaevski,YuhaoZhou,AbdelrahmanMohamed,andMichaelAuli. wav2vec2.0: Aframeworkforself-supervised
learning of speech representations. Advances in neural information processing systems, 33:12449–12460, 2020.
SylvainBaillet. Magnetoencephalographyforbrainelectrophysiologyandimaging. Nature neuroscience,20(3):327–339,
2017.
HubertBanville,YohannBenchetrit,Stéphaned’Ascoli,JérémyRapin,andJean-RémiKing. Scalinglawsfordecoding
images from brain activity. arXiv preprint arXiv:2501.15322, 2025.
Alexandre Barachant. Robust control of an effector by an asynchronous EEG brain-machine interface. Theses,
Universite de Grenoble, March 2012. https://theses.hal.science/tel-01196752.
Alexandre Barachant and Marco Congedo. A plug&play P300 BCI using information geometry. arXiv preprint
arXiv:1409.0107, 2014.
Alexandre Barachant, Stéphane Bonnet, Marco Congedo, and Christian Jutten. Multiclass brain–computer interface
classification by Riemannian geometry. IEEE Transactions on Biomedical Engineering, 59(4):920–928, 2011.
Yohann Benchetrit, Hubert Banville, and Jean-Rémi King. Brain decoding: toward real-time reconstruction of visual
perception. In ICLR 2024, 2024.
Davide Borra, Francesco Paissan, and Mirco Ravanelli. SpeechBrain-MOABB: An open-source python library for
benchmarking deep neural networks applied to EEG signals. Computers in Biology and Medicine, 182:109097, 2024.
16

Jonathan R Brennan and John T Hale. Hierarchical structure guides rapid linguistic predictions during naturalistic
listening. PloS one, 14(1):e0207741, 2019.
Katherine S Button, John PA Ioannidis, Claire Mokrysz, Brian A Nosek, Jonathan Flint, Emma SJ Robinson, and
Marcus R Munafò. Power failure: why small sample size undermines the reliability of neuroscience. Nature reviews
neuroscience, 14(5):365–376, 2013.
Kalou Cabrera Castillos, Simon Ladouce, Ludovic Darmet, and Frédéric Dehais. Burst c-VEP based BCI: Optimizing
stimulusdesignforenhancedclassificationwithminimalcalibrationdataandimproveduserexperience. NeuroImage,
284:120446, December 2023. ISSN 1053-8119. doi: 10.1016/j.neuroimage.2023.120446. http://dx.doi.org/10.1016/j.
neuroimage.2023.120446.
JosueOrtegaCaro,AntonioHdeOFonseca,ChristopherAverill,SyedARizvi,MatteoRosati,JamesLCross,Prateek
Mittal, Emanuele Zappala, Daniel Levine, Rahul M Dhodapkar, et al. BrainLM: A foundation model for brain
activity recordings. BioRxiv, pages 2023–09, 2023.
Grégoire Cattan, Anton Andreev, Pedro L. C. Rodrigues, and Marco Congedo. Dataset of an EEG-based BCI
experiment in virtual reality and on a personal computer, 2019. https://zenodo.org/record/2605204.
Ricardo Chavarriaga and José del R. Millan. Learning from EEG Error-Related potentials in noninvasive Brain-
Computer interfaces. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 18(4):381–388, August
2010. ISSN 1558-0210. doi: 10.1109/tnsre.2010.2053387. http://dx.doi.org/10.1109/TNSRE.2010.2053387.
Jingjing Chen, Xiaobin Wang, Chen Huang, Xin Hu, Xinke Shen, and Dan Zhang. A large finer-grained affective
computing EEG dataset. Scientific Data, 10(1), October 2023. ISSN 2052-4463. doi: 10.1038/s41597-023-02650-w.
http://dx.doi.org/10.1038/s41597-023-02650-w.
HohyunCho,MinkyuAhn,SangtaeAhn,MoonyoungKwon,andChanJun,Sung. Supportingdatafor"EEGdatasets
for motor imagery brain computer interface", 2017. http://gigadb.org/dataset/100295.
Radoslaw Martin Cichy, Kshitij Dwivedi, Benjamin Lahner, Alex Lascelles, Polina Iamshchinina, Monika Graumann,
Alex Andonian, NAR Murty, K Kay, Gemma Roig, et al. The algonauts project 2021 challenge: How the human
brain makes sense of a world in motion. arXiv preprint arXiv:2104.13714, 2021.
Fernando Lopes da Silva. EEG and MEG: relevance to neuroscience. Neuron, 80(5):1112–1128, 2013.
JonathanDanandAliShoeb. BIDSCHB-MITscalpEEGdatabase,December2023. https://doi.org/10.5281/zenodo.
10259996.
Stéphane d’Ascoli, Jérémy Rapin, Yohann Benchetrit, Teon Brookes, Katelyn Begany, Joséphine
Raugel, Hubert Banville, and Jean-Rémi King. A foundation model of vision, audi-
tion, and language for in-silico neuroscience. https://ai.meta.com/research/publications/
a-foundation-model-of-vision-audition-and-language-for-in-silico-neuroscience/, 2026.
Alexandre Défossez, Charlotte Caucheteux, Jérémy Rapin, Ori Kabeli, and Jean-Rémi King. Decoding speech from
non-invasive brain recordings. arXiv preprint arXiv:2208.12266, 2022.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: Pre-training of deep bidirectional
transformers for language understanding. In Proceedings of the 2019 conference of the North American chapter of
the association for computational linguistics: human language technologies, volume 1 (long and short papers), pages
4171–4186, 2019.
Berkay Döner, Thorir Mar Ingolfsson, Luca Benini, and Yawei Li. LUNA: Efficient and topology-agnostic foundation
model for EEG signal analysis. In The Thirty-Ninth Annual Conference on Neural Information Processing Systems
(NeurIPS), 2025. https://openreview.net/forum?id=uazfjnFL0G.
ZijianDong,RuilinLi,YileiWu,ThuanTNguyen,JoannaSChong,FangJi,NathanaelRTong,ChristopherLChen,
and Juan H Zhou. Brain-JEPA: Brain dynamics foundation model with gradient positioning and spatiotemporal
masking. Advances in Neural Information Processing Systems, 37:86048–86073, 2024.
G.Dornhege,B.Blankertz,G.Curio,andK.-R.Muller. BoostingbitratesinnoninvasiveEEGsingle-trialclassifications
by feature combination and multiclass paradigms. IEEE Transactions on Biomedical Engineering, 51(6):993–1002,
June 2004. ISSN 1558-2531. doi: 10.1109/tbme.2004.827088. http://dx.doi.org/10.1109/TBME.2004.827088.
Pauline Dreyer, Aline Roc, Léa Pillette, Sébastien Rimbert, and Fabien Lotte. A large EEG database with users’
profile information for motor imagery brain-computer interface research. Scientific Data, 10(1), September 2023.
ISSN 2052-4463. doi: 10.1038/s41597-023-02445-z. http://dx.doi.org/10.1038/s41597-023-02445-z.
17

Stéphaned’Ascoli,CorentinBel,JérémyRapin,HubertBanville,YohannBenchetrit,ChristophePallier,andJean-Rémi
King. Towards decoding individual words from non-invasive brain recordings. Nature Communications, 16(1):10521,
2025.
Yassine El Ouahidi, Vincent Gripon, Bastien Pasdeloup, Ghaith Bouallegue, Nicolas Farrugia, and Giulia Lioi. A
strong and simple deep learning baseline for bci motor imagery decoding. arXiv preprint arXiv:2309.07159, 2023.
https://arxiv.org/abs/2309.07159.
Yassine El Ouahidi, Jonathan Lys, Philipp Thölke, Nicolas Farrugia, Bastien Pasdeloup, Vincent Gripon, Karim Jerbi,
andGiuliaLioi. REVE:AfoundationmodelforEEG–adaptingtoanysetupwithlarge-scalepretrainingon25,000
subjects. In The Thirty-Ninth Annual Conference on Neural Information Processing Systems (NeurIPS), 2025.
https://openreview.net/forum?id=ZeFMtRBy4Z.
WilliamFalconandThePyTorchLightningteam. PyTorchLightning,March2019. https://github.com/Lightning-AI/
lightning.
Josef Faller, Carmen Vidaurre, Teodoro Solis-Escalante, Christa Neuper, and Reinhold Scherer. Autocalibration
and recurrent adaptation: Towards a plug and play online ERD-BCI. IEEE Transactions on Neural Systems
and Rehabilitation Engineering, 20(3):313–319, May 2012. ISSN 1558-0210. doi: 10.1109/tnsre.2012.2189584.
http://dx.doi.org/10.1109/tnsre.2012.2189584.
Lukas A. W. Gemein, Robin T. Schirrmeister, Patryk Chrabaszcz, Daniel Wilson, Joschka Boedecker, Andreas
Schulze-Bonhage,FrankHutter,andTonioBall. Machine-learning-baseddiagnosticsofEEGpathology. NeuroImage,
220:117021, 2020.
Mohammad M Ghassemi, Benjamin E Moody, Li-wei H Lehman, Christopher Song, Qiao Li, Haoqi Sun, Roger G
Mark, M Brandon Westover, and Gari D Clifford. You Snooze, You Win: The PhysioNet/Computing in Cardiology
Challenge 2018. Computing in cardiology, 45:10.22489/cinc.2018.049, September 2018. ISSN 2325-8861. doi:
10.22489/cinc.2018.049.
Alessandro T. Gifford, Kshitij Dwivedi, Gemma Roig, and Radoslaw M. Cichy. A large and rich EEG dataset for
modeling human visual object recognition. Neuroimage, 264:119754, December 2022a. ISSN 1053-8119. doi:
10.1016/j.neuroimage.2022.119754. https://pmc.ncbi.nlm.nih.gov/articles/PMC9771828/.
Alessandro T Gifford, Kshitij Dwivedi, Gemma Roig, and Radoslaw M Cichy. A large and rich EEG dataset for
modeling human visual object recognition. NeuroImage, 264:119754, 2022b.
Alessandro T Gifford, Benjamin Lahner, Sari Saba-Sadiya, Martina G Vilas, Alex Lascelles, Aude Oliva, Kendrick
Kay, Gemma Roig, and Radoslaw M Cichy. The algonauts project 2023 challenge: How the human brain makes
sense of natural scenes. arXiv preprint arXiv:2301.03198, 2023.
Alessandro T Gifford, Domenic Bersch, Marie St-Laurent, Basile Pinsard, Julie Boyle, Lune Bellec, Aude Oliva,
Gemma Roig, and Radoslaw M Cichy. The algonauts project 2025 challenge: How the human brain makes sense of
multimodal movies. arXiv preprint arXiv:2501.00504, 2024.
Alexandre Gramfort, Martin Luessi, Eric Larson, Denis A. Engemann, Daniel Strohmeier, Christian Brodbeck, Roman
Goj, Mainak Jas, Teon Brooks, Lauri Parkkonen, and Matti Hämäläinen. MEG and EEG data analysis with
MNE-Python. Frontiers in Neuroscience, 7, December 2013. ISSN 1662-453X. doi: 10.3389/fnins.2013.00267.
M. Grosse-Wentrup, C. Liefhold, K. Gramann, and M. Buss. Beamforming in noninvasive Brain-Computer interfaces.
IEEE Transactions on Biomedical Engineering, 56(4):1209–1219, April 2009. ISSN 1558-2531. doi: 10.1109/tbme.
2008.2009768. http://dx.doi.org/10.1109/TBME.2008.2009768.
Christoph Guger, Shahab Daban, Eric Sellers, Clemens Holzner, Gunther Krausz, Roberta Carabalona, Furio
Gramatica, and Guenter Edlinger. How many people are able to control a P300-based brain-computer interface
(BCI)? Neuroscience Letters, 462(1):94–98, September 2009. ISSN 0304-3940. doi: 10.1016/j.neulet.2009.06.045.
http://dx.doi.org/10.1016/j.neulet.2009.06.045.
A. Hamid, K. Gagliano, S. Rahman, N. Tulin, V. Tchiong, I. Obeid, and J. Picone. The Temple University Artifact
Corpus: An annotated corpus of EEG artifacts. pages 1–4, 2020.
Amir Harati, Silvia Lopez, I Obeid, J Picone, MP Jacobson, and S Tobochnik. The TUH EEG Corpus: A big data
resource for automated EEG interpretation. In 2014 IEEE signal processing in medicine and biology symposium
(SPMB), pages 1–5. IEEE, 2014.
AmirHarati,MeysamGolmohammadi,SilviaLopez,IyadObeid,andJosephPicone. ImprovedEEGeventclassification
using differential energy. pages 1–4, 2015.
18

Stefan Haufe, Matthias S Treder, Manfred F Gugler, Max Sagebaum, Gabriel Curio, and Benjamin Blankertz. EEG
potentials predict upcoming emergency brakings during simulated driving. Journal of Neural Engineering, 8(5):
056001, July 2011. ISSN 1741-2552. doi: 10.1088/1741-2560/8/5/056001. http://dx.doi.org/10.1088/1741-2560/8/
5/056001.
MartinNHebart,OliverContier,LinaTeichmann,AdamHRockter,CharlesYZheng,AlexisKidder,AnnaCorriveau,
Maryam Vaziri-Pashkam, and Chris I Baker. THINGS-data, a multimodal collection of large-scale datasets for
investigating object representations in human brain and behavior. eLife, 12:e82580, feb 2023. ISSN 2050-084X. doi:
10.7554/eLife.82580. https://doi.org/10.7554/eLife.82580.
MarcelF.Hinss,EmilieS.Jahanpour,BertilleSomon,LouPluchon,FrédéricDehais,andRaphaëlleN.Roy. COG-BCI
database: A multi-session and multi-task EEG cognitive dataset for passive brain-computer interfaces, July 2022.
MarcelF.Hinss,EmilieS.Jahanpour,BertilleSomon,LouPluchon,FrédéricDehais,andRaphaëlleN.Roy.Openmulti-
sessionandmulti-taskEEGcognitivedatasetforpassivebrain-computerinterfaceapplications. ScientificData,10(1),
February2023. ISSN2052-4463. doi: 10.1038/s41597-022-01898-y. http://dx.doi.org/10.1038/s41597-022-01898-y.
ArthurEHoerlandRobertWKennard.Ridgeregression: Biasedestimationfornonorthogonalproblems.Technometrics,
12(1):55–67, 1970.
Ulrich Hoffmann, Jean-Marc Vesin, Touradj Ebrahimi, and Karin Diserens. An efficient P300-based brain-computer
interface for disabled subjects. Journal of Neuroscience Methods, 167(1):115–125, January 2008. ISSN 0165-0270.
doi: 10.1016/j.jneumeth.2007.03.005. http://dx.doi.org/10.1016/j.jneumeth.2007.03.005.
Nora Hollenstein, Jonathan Rotsztejn, Marius Troendle, Andreas Pedroni, Ce Zhang, and Nicolas Langer. ZuCo, a
simultaneous EEG and eye-tracking resource for natural sentence reading. Scientific Data, 5(1), December 2018.
ISSN 2052-4463.
Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Liang Wang, Weizhu Chen,
et al. LoRA: Low-rank adaptation of large language models. Iclr, 1(2):3, 2022.
Johannes Höhne. A novel 9-class auditory ERP paradigm driving a predictive text entry system. Frontiers in
Neuroscience,5,2011. ISSN1662-453X. doi: 10.3389/fnins.2011.00099. http://dx.doi.org/10.3389/fnins.2011.00099.
David Hübner. EEG data for: "Learning From Label Proportions In Brain-Computer Interfaces", 2016. https:
//zenodo.org/record/192684.
David Hübner, Thibault Verhoeven, Konstantin Schmid, Klaus-Robert Müller, Michael Tangermann, and Pieter-
Jan Kindermans. Learning from label proportions in brain-computer interfaces: Online unsupervised learning
with guarantees. PLOS ONE, 12(4):e0175856, April 2017. ISSN 1932-6203. doi: 10.1371/journal.pone.0175856.
http://dx.doi.org/10.1371/journal.pone.0175856.
Ping-Keng Jao, Ricardo Chavarriaga, and José del R. Millán. EEG-Based online regulation of difficulty in simulated
flying. IEEE Transactions on Affective Computing, 14(1):394–405, January 2023. ISSN 2371-9850. doi: 10.1109/
taffc.2021.3059688. http://dx.doi.org/10.1109/TAFFC.2021.3059688.
Vinay Jayaram and Alexandre Barachant. MOABB: trustworthy algorithm benchmarking for bcis. Journal of neural
engineering, 15(6):066011, 2018.
Wei-Bang Jiang, Li-Ming Zhao, and Bao-Liang Lu. Large brain model for learning generic representations with
tremendous EEG data in BCI. In The Twelfth International Conference on Learning Representations (ICLR), 2024.
EmmanuelK.Kalunga,SylvainChevallier,QuentinBarthélemy,KarimDjouani,EricMonacelli,andYskandarHamam.
OnlineSSVEP-basedBCIusingRiemanniangeometry. Neurocomputing,191:55–68,May2016. ISSN0925-2312. doi:
10.1016/j.neucom.2016.01.007. http://dx.doi.org/10.1016/j.neucom.2016.01.007.
Emily S. Kappenman, Jaclyn L. Farrens, Wendy Zhang, Andrew X. Stewart, and Steven J. Luck. ERP CORE: An
open resource for human event-related potential research. NeuroImage, 225:117465, January 2021. ISSN 1053-8119.
doi: 10.1016/j.neuroimage.2020.117465. http://dx.doi.org/10.1016/j.neuroimage.2020.117465.
BriannaMKarpowicz,JoelYe,ChaofeiFan,PabloTostado-Marcos,FabioRizzoglio,ClayWashington,ThiagoScodeler,
Diogo de Lucena, Samuel R Nason-Tomaszewski, Matthew J Mender, et al. Few-shot algorithms for consistent
neural decoding (FALCON) benchmark. Advances in Neural Information Processing Systems, 37:76578–76615, 2024.
Ard Kastrati, Josua Bürki, Jonas Lauer, Cheng Xuan, Raffaele Iaquinto, and Roger Wattenhofer. EEG-Bench: A
BenchmarkforEEGFoundationModelsinClinicalApplications. InNeurIPS 2025 Workshop on Foundation Models
for the Brain and Body, 2025.
19

B. Kemp, A.H. Zwinderman, B. Tuk, H.A.C. Kamphuisen, and J.J.L. Oberye. Analysis of a sleep-dependent neuronal
feedback loop: the slow-wave microcontinuity of the EEG. IEEE Transactions on Biomedical Engineering, 47(9):
1185–1194, 2000.
Peter Kim, Junbeom Kwon, Sunghwan Joo, Sangyoon Bae, Donggyu Lee, Yoonho Jung, Shinjae Yoo, Jiook Cha, and
Taesup Moon. SwiFT: Swin 4D fMRI Transformer. In A. Oh, T. Naumann, A. Globerson, K. Saenko, M. Hardt,
and S. Levine, editors, Advances in Neural Information Processing Systems, volume 36, pages 42015–42037. Curran
Associates, Inc., 2023.
Jean-Rémi King, Teon L. Brooks, Katie Begany, Lucy Zhang, Josephine Raugel, Jarod Lévy, Sophia Houhamdi, Julien
Gadonneix, Linnea Evanson, Corentin Bel, Stéphane d’Ascoli, Marlène Careil, Yohann Benchetrit, Hubert Banville,
and Jérémy Rapin. Neuralset: A high-performing python package for neuro-ai. 2026.
Simon Kojima. Replication data for: Four-class ASME BCI: investigation of the feasibility and comparison of
two strategies for multiclassing, 2024. https://dataverse.harvard.edu/citation?persistentId=doi:10.7910/DVN/
1UJDV6.
Simon Kojima and Shin’ichiro Kanoh. Replication data for: An auditory brain-computer interface based on selective
attention to multiple tone streams, 2024. https://dataverse.harvard.edu/citation?persistentId=doi:10.7910/DVN/
MQOVEY.
Louis Korczowski, Martine Cederhout, Anton Andreev, Grégoire Cattan, Pedro Luis Coelho Rodrigues, Violette
Gautheret, and Marco Congedo. Brain invaders calibration-less P300-based BCI with modulation of flash duration
dataset (bi2015a), 2019a. https://zenodo.org/record/3266930.
Louis Korczowski, Ekaterina Ostaschenko, Anton Andreev, Grégoire Cattan, Pedro Luis Coelho Rodrigues, Violette
Gautheret, and Marco Congedo. Brain invaders calibration-less P300-based BCI using dry EEG electrodes dataset
(bi2014a), 2019b. https://zenodo.org/record/3266223.
Louis Korczowski, Ekaterina Ostaschenko, Anton Andreev, Grégoire Cattan, Pedro Luis Coelho Rodrigues, Violette
Gautheret, and Marco Congedo. Brain invaders solo versus collaboration: Multi-User P300-based Brain-Computer
interface dataset (bi2014b), 2019c. https://zenodo.org/record/3267301.
Demetres Kostas, Stephane Aroca-Ouellette, and Frank Rudzicz. BENDR: Using transformers and a contrastive
self-supervised learning task to learn from massive amounts of EEG data. Frontiers in Human Neuroscience, 15:
653659, 2021.
Niklas Kueper, Kartik Chari, Judith Bütefür, Julia Habenicht, Tobias Rossol, Su Kyoung Kim, Marc Tabie, Frank
Kirchner,andElsaAndreaKirchner.EEGandEMGdatasetforthedetectionoferrorsintroducedbyanactiveorthosis
device. Frontiers in Human Neuroscience, 18, January 2024. ISSN 1662-5161. doi: 10.3389/fnhum.2024.1304311.
Vernon J. Lawhern, Amelia J. Solon, Nicholas R. Waytowich, Stephen M. Gordon, Chou P. Hung, and Brent J. Lance.
EEGNet: a compact convolutional neural network for EEG-based brain–computer interfaces. Journal of Neural
Engineering, 15(5):056013, 2018.
Min-Ho Lee, O-Yeon Kwon, Yong-Jeong Kim, Hong-Kyung Kim, Young-Eun Lee, John Williamson, Siamac Fazli, and
Seong-Whan Lee. EEG dataset and OpenBMI toolbox for three BCI paradigms: an investigation into BCI illiteracy.
GigaScience, 8(5), January 2019. ISSN 2047-217X. doi: 10.1093/gigascience/giz002. http://dx.doi.org/10.1093/
gigascience/giz002.
Robert Leeb, Felix Lee, Claudia Keinrath, Reinhold Scherer, Horst Bischof, and Gert Pfurtscheller. Brain-Computer
communication: Motivation,aim,andimpactofexploringavirtualapartment.IEEETransactionsonNeuralSystems
and Rehabilitation Engineering, 15(4):473–482, December 2007. ISSN 1558-0210. doi: 10.1109/tnsre.2007.906956.
http://dx.doi.org/10.1109/TNSRE.2007.906956.
Brian Lester, Rami Al-Rfou, and Noah Constant. The power of scale for parameter-efficient prompt tuning. In
Proceedings of the 2021 conference on empirical methods in natural language processing, pages 3045–3059, 2021.
JarodLévy, MingfangZhang, SvetlanaPinet, JérémyRapin, HubertBanville, Stéphaned’Ascoli, andJean-RémiKing.
Brain-to-text decoding: A non-invasive approach via typing. arXiv preprint arXiv:2502.17480, 2025.
Haijie Liu, Penghu Wei, Haochong Wang, Xiaodong Lv, Wei Duan, Meijie Li, Yan Zhao, Qingmei Wang, Xinyuan
Chen, Gaige Shi, Bo Han, and Junwei Hao. An EEG motor imagery dataset for brain computer interface in
acute stroke patients. Scientific Data, 11(1), January 2024a. ISSN 2052-4463. doi: 10.1038/s41597-023-02787-8.
http://dx.doi.org/10.1038/s41597-023-02787-8.
20

Xuan-Hao Liu, Yan-Kai Liu, Yansen Wang, Kan Ren, Hanwen Shi, Zilong Wang, Dongsheng Li, Bao-Liang Lu, and
Wei-Long Zheng. EEG2video: Towards decoding dynamic visual perception from EEG signals. Advances in Neural
| Information | Processing | Systems, 37:72245–72273, |     | 2024b. |     |     |
| ----------- | ---------- | ------------------------ | --- | ------ | --- | --- |
Sebas Lopez, G Suarez, D Jungreis, I Obeid, and Joseph Picone. Automated identification of abnormal adult EEGs.
In 2015 IEEE signal processing in medicine and biology symposium (SPMB), pages 1–5. IEEE, 2015.
Silvia Isabel Lopez de Diego. Automated interpretation of abnormal adult electroencephalograms. 2017. https:
//www.isip.piconepress.com/publications/ms_theses/2017/abnormal/thesis/.
Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. arXiv preprint arXiv:1711.05101, 2017.
Víctor Martínez-Cagigal. Dataset: Influence of spatial frequency in visual stimuli for cVEP-based BCIs: evaluation of
performance and user experience, 2023. https://uvadoc.uva.es/handle/10324/70973.
Víctor Martínez-Cagigal. Dataset: Non-binary m-sequences for more comfortable brain-computer interfaces based on
| c-VEPs, | 2024. https://uvadoc.uva.es/handle/10324/70945. |     |     |     |     |     |
| ------- | ----------------------------------------------- | --- | --- | --- | --- | --- |
Christoph M Michel and Micah M Murray. Towards the utilization of EEG as a brain imaging tool. Neuroimage, 61
| (2):371–385, | 2012. |     |     |     |     |     |
| ------------ | ----- | --- | --- | --- | --- | --- |
Andreas Miltiadous, Emmanouil Gionanidis, Katerina D. Tzimourta, Nikolaos Giannakeas, and Alexandros T. Tzallas.
DICE-Net: A Novel Convolution-Transformer Architecture for Alzheimer Detection in EEG Signals. IEEE Access,
| 11:71840–71858, | 2023. | ISSN 2169-3536. | doi: | 10.1109/ACCESS.2023.3294618. |     |     |
| --------------- | ----- | --------------- | ---- | ---------------------------- | --- | --- |
WajidMumtaz,SyedSaadAzharAli,MohdAzharMohdYasin,andAamirSaeedMalik. Amachinelearningframework
involving EEG-based functional connectivity to diagnose major depressive disorder (MDD). Medical & Biological
Engineering & Computing, 56(2):233–246, February 2018. ISSN 1741-0444. doi: 10.1007/s11517-017-1685-z.
Masaki Nakanishi, Yijun Wang, Yu-Te Wang, and Tzyy-Ping Jung. A comparison study of canonical correlation
analysis based methods for detecting Steady-State visual evoked potentials. PLOS ONE, 10(10):e0140703, October
2015. ISSN 1932-6203. doi: 10.1371/journal.pone.0140703. http://dx.doi.org/10.1371/journal.pone.0140703.
ThomasNaselaris,KendrickNKay,ShinjiNishimoto,andJackLGallant.EncodinganddecodinginfMRI.Neuroimage,
| 56(2):400–410, | 2011. |     |     |     |     |     |
| -------------- | ----- | --- | --- | --- | --- | --- |
Mante S Nieuwland, Stephen Politzer-Ahles, Evelien Heyselaar, Katrien Segaert, Emily Darley, Nina Kazanina, Sarah
Von Grebmer Zu Wolfsthurn, Federica Bartolozzi, Vita Kogan, Aine Ito, et al. Large-scale replication study reveals
a limit on probabilistic prediction in language comprehension. ELife, 7:e33468, 2018.
Patrick Ofner, Andreas Schwarz, Joana Pereira, and Gernot R. Müller-Putz. Upper limb movements can be decoded
from the time-domain of low-frequency EEG. PLOS ONE, 12(8):e0182578, August 2017. ISSN 1932-6203. doi:
| 10.1371/journal.pone.0182578. |     | http://dx.doi.org/10.1371/journal.pone.0182578. |     |     |     |     |
| ----------------------------- | --- | ----------------------------------------------- | --- | --- | --- | --- |
VangelisP.Oikonomou,GeorgiosLiaros,KostantinosGeorgiadis,ElisavetChatzilari,KaterinaAdam,SpirosNikolopou-
los, and Ioannis Kompatsiaris. Comparative evaluation of state-of-the-art algorithms for SSVEP-based BCIs, 2016.
https://arxiv.org/abs/1602.00904.
Maxime Oquab, Timothée Darcet, Théo Moutakanni, Huy Vo, Marc Szafraniec, Vasil Khalidov, Pierre Fernandez,
Daniel Haziza, Francisco Massa, Alaaeldin El-Nouby, et al. DINOv2: Learning robust visual features without
| supervision. | Transactions | on Machine | Learning | Research | Journal, | 2024. |
| ------------ | ------------ | ---------- | -------- | -------- | -------- | ----- |
Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory Chanan, Trevor Killeen, Zeming
Lin, Natalia Gimelshein, Luca Antiga, et al. PyTorch: An imperative style, high-performance deep learning library.
| Advances | in neural information | processing |     | systems, 32, | 2019. |     |
| -------- | --------------------- | ---------- | --- | ------------ | ----- | --- |
AnaLuísaPinho,AlexisAmadon,TorstenRuest,MurielleFabre,ElvisDohmatob,IsabelleDenghien,ChantalGinisty,
Séverine Becuwe-Desmidt, Séverine Roger, Laurence Laurier, et al. Individual Brain Charting, a high-resolution
| fMRI dataset | for cognitive | mapping. | Scientific | data, | 5(1):180105, | 2018. |
| ------------ | ------------- | -------- | ---------- | ----- | ------------ | ----- |
Russell A Poldrack. Can cognitive processes be inferred from neuroimaging data? Trends in cognitive sciences, 10(2):
59–63, 2006.
Russell A Poldrack. Inferring mental states from neuroimaging data: from reverse inference to large-scale decoding.
| Neuron, | 72(5):692–697, | 2011. |     |     |     |     |
| ------- | -------------- | ----- | --- | --- | --- | --- |
21

Russell A Poldrack, Chris I Baker, Joke Durnez, Krzysztof J Gorgolewski, Paul M Matthews, Marcus R Munafò,
Thomas E Nichols, Jean-Baptiste Poline, Edward Vul, and Tal Yarkoni. Scanning the horizon: towards transparent
and reproducible neuroimaging research. Nature reviews neuroscience, 18(2):115–126, 2017.
AlecRadford,JongWookKim,ChrisHallacy,AdityaRamesh,GabrielGoh,SandhiniAgarwal,GirishSastry,Amanda
Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, and Ilya Sutskever. Learning transferable visual models
from natural language supervision, 2021.
J. Rapin and J.-R. King. Exca - Execution and caching. https://github.com/facebookresearch/exca, 2024.
Christoph Reichert, Igor Fabian Tellez Ceja, Catherine M. Sweeney-Reed, Hans-Jochen Heinze, Hermann Hinrichs,
and Stefan Dürschmid. Impact of stimulus features on the performance of a Gaze-Independent Brain-Computer
interface based on covert spatial attention shifts. Frontiers in Neuroscience, 14, December 2020. ISSN 1662-453X.
doi: 10.3389/fnins.2020.591777. http://dx.doi.org/10.3389/fnins.2020.591777.
Angela Riccio, Luca Simione, Francesca Schettini, Alessia Pizzimenti, Maurizio Inghilleri, Marta Olivetti Belardinelli,
Donatella Mattia, and Febo Cincotti. Attention and P300-based BCI performance in people with amyotrophic
lateral sclerosis. Frontiers in Human Neuroscience, 7, 2013. ISSN 1662-5161. doi: 10.3389/fnhum.2013.00732.
http://dx.doi.org/10.3389/fnhum.2013.00732.
Bertrand Rivet, Antoine Souloumiac, Virginie Attina, and Guillaume Gibert. xDAWN algorithm to enhance evoked
potentials: applicationtobrain–computerinterface. IEEETransactionsonBiomedicalEngineering,56(8):2035–2043,
2009.
MicheleRomani, DevisZanoni,ElisabettaFarella, andLucaTurchet. BrainForm: aseriousgameforBCItrainingand
data collection, 2025. https://arxiv.org/abs/2510.10169.
Simanto Saha and Mathias Baumert. Intra-and inter-subjecct variability in EEG-based sensorimotor brain computer
interface: a review. Frontiers in computational neuroscience, 13:87, 2020.
Sulamith Schaeff, Matthias Sebastian Treder, Bastian Venthur, and Benjamin Blankertz. Exploring motion VEPs for
gaze-independent communication. Journal of Neural Engineering, 9(4):045006, July 2012. ISSN 1741-2552. doi:
10.1088/1741-2560/9/4/045006. http://dx.doi.org/10.1088/1741-2560/9/4/045006.
G. Schalk, D.J. McFarland, T. Hinterberger, N. Birbaumer, and J.R. Wolpaw. BCI2000: a general-purpose brain-
computer interface (BCI) system. IEEE Transactions on Biomedical Engineering, 51(6):1034–1043, 2004.
Reinhold Scherer, Josef Faller, David Balderas, Elisabeth V. C. Friedrich, Markus Pröll, Brendan Allison, and Gernot
Müller-Putz. Brain-computerinterfacing: morethanthesumofitsparts. Soft Computing,17(2):317–331,July2012.
ISSN 1433-7479. doi: 10.1007/s00500-012-0895-4. http://dx.doi.org/10.1007/s00500-012-0895-4.
Reinhold Scherer, Josef Faller, Elisabeth V. C. Friedrich, Eloy Opisso, Ursula Costa, Andrea Kübler, and Gernot R.
Müller-Putz. Individually adapted imagery improves Brain-Computer interface performance in End-Users with
disability. PLOS ONE, 10(5):e0123727, May 2015. ISSN 1932-6203. doi: 10.1371/journal.pone.0123727. http:
//dx.doi.org/10.1371/journal.pone.0123727.
Robin Tibor Schirrmeister, Jost Tobias Springenberg, Lukas Dominique Josef Fiederer, Martin Glasstetter, Katharina
Eggensperger, Michael Tangermann, Frank Hutter, Wolfram Burgard, and Tonio Ball. Deep learning with convolu-
tional neural networks for eeg decoding and visualization. Human Brain Mapping, aug 2017. ISSN 1097-0193. doi:
10.1002/hbm.23730. http://dx.doi.org/10.1002/hbm.23730.
Martijn Schreuder, Benjamin Blankertz, and Michael Tangermann. A new auditory Multi-Class Brain-Computer
interface paradigm: Spatial hearing as an informative cue. PLoS ONE, 5(4):e9813, April 2010. ISSN 1932-6203. doi:
10.1371/journal.pone.0009813. http://dx.doi.org/10.1371/journal.pone.0009813.
Martin Schrimpf, Jonas Kubilius, Ha Hong, Najib J Majaj, Rishi Rajalingham, Elias B Issa, Kohitij Kar, Pouya
Bashivan, Jonathan Prescott-Roy, Franziska Geiger, et al. Brain-score: Which artificial neural network for object
recognition is most brain-like? BioRxiv, page 407007, 2018.
Martin Schrimpf, Jonas Kubilius, Michael J Lee, N Apurva Ratan Murty, Robert Ajemian, and James J DiCarlo.
Integrative benchmarking to advance neurally mechanistic models of human intelligence. Neuron, 2020. https:
//www.cell.com/neuron/fulltext/S0896-6273(20)30605-X.
Andreas Schwarz, Carlos Escolano, Luis Montesano, and Gernot R. Müller-Putz. Analyzing and decoding natural
Reach-and-Grasp actions using gel, water and dry EEG systems. Frontiers in Neuroscience, 14, August 2020. ISSN
1662-453X. doi: 10.3389/fnins.2020.00849. http://dx.doi.org/10.3389/fnins.2020.00849.
22

JaeyoungShin,AlexandervonLuhmann,BenjaminBlankertz,Do-WonKim,JichaiJeong,Han-JeongHwang,andKlaus-
RobertMuller. OpenaccessdatasetforEEG+NIRSSingle-Trialclassification. IEEETransactionsonNeuralSystems
and Rehabilitation Engineering, 25(10):1735–1745, October 2017. ISSN 1558-0210. doi: 10.1109/tnsre.2016.2628057.
http://dx.doi.org/10.1109/TNSRE.2016.2628057.
SeyedYahyaShirazi,AlexandreFranco,MaurícioScopelHoffmann,NathaliaBEsper,DungTruong,ArnaudDelorme,
Michael P Milham, and Scott Makeig. HBN-EEG: The FAIR implementation of the Healthy Brain Network (HBN)
electroencephalography dataset. bioRxiv, pages 2024–10, 2024.
Arun Singh, Rachel C. Cole, Arturo I. Espinoza, Aron Evans, Scarlett Cao, James F. Cavanagh, and Nandakumar S.
Narayanan. Timing variability and midfrontal ˜4 Hz rhythms correlate with cognition in Parkinson’s disease. npj
Parkinson’s Disease, 7(1):14, February 2021. ISSN 2373-8057. doi: 10.1038/s41531-021-00158-x.
Yonghao Song, Qingqing Zheng, Bingchuan Liu, and Xiaorong Gao. EEG Conformer: Convolutional transformer for
EEGdecodingandvisualization. IEEE Transactions on Neural Systems and Rehabilitation Engineering,31:710–719,
2022. https://ieeexplore.ieee.org/document/9991178.
Jan Sosulski and Michael Tangermann. Electroencephalogram signals recorded from 13 healthy subjects during an
auditoryoddballparadigmunderdifferentstimulusonsetasynchronyconditions,2019. https://freidok.uni-freiburg.
de/data/154576.
Nitikorn Srisrisawang and Gernot R Müller-Putz. Simultaneous encoding of speed, distance, and direction in discrete
reaching: an EEG study. Journal of Neural Engineering, 21(6):066042, December 2024. ISSN 1741-2552. doi:
10.1088/1741-2552/ada0ea. http://dx.doi.org/10.1088/1741-2552/ada0ea.
James R. Stieger, Stephen A. Engel, and Bin He. Continuous sensorimotor rhythm based brain computer interface
learning in a large population. Scientific Data, 8(1), April 2021. ISSN 2052-4463. doi: 10.1038/s41597-021-00883-1.
http://dx.doi.org/10.1038/s41597-021-00883-1.
Chenxi Sun, Jin Jing, Niels Turley, Callison Alcott, Wan-Yee Kang, Andrew J Cole, Daniel M Goldenholz, Alice Lam,
Edilberto Amorim, Catherine Chu, et al. Harvard Electroencephalography Database: A comprehensive clinical
electroencephalographic resource from four boston hospitals. Epilepsia, 66(9):3411–3425, 2025.
Divyanshu Tak, Biniam A Garomsa, Anna Zapaishchykova, Tafadzwa L Chaunzwa, Juan Carlos Climent Pardo,
Zezhong Ye, John Zielke, Yashwanth Ravipati, Suraj Pai, Sri Vajapeyam, et al. A generalizable foundation model
for analysis of human brain MRI. Nature Neuroscience, pages 1–12, 2026.
Michael Tangermann, Klaus-Robert Müller, Ad Aertsen, Niels Birbaumer, Christoph Braun, Clemens Brunner,
Robert Leeb, Carsten Mehring, Kai J. Miller, Gernot R. Müller-Putz, Guido Nolte, Gert Pfurtscheller, Hubert
Preissl, Gerwin Schalk, Alois Schlögl, Carmen Vidaurre, Stephan Waldert, and Benjamin Blankertz. Review of
the BCI competition IV. Frontiers in Neuroscience, 6, 2012. ISSN 1662-4548. doi: 10.3389/fnins.2012.00055.
http://dx.doi.org/10.3389/fnins.2012.00055.
Jason R Taylor, Nitin Williams, Rhodri Cusack, Tibor Auer, Meredith A Shafto, Marie Dixon, Lorraine K Tyler,
RichardNHenson,etal.TheCambridgeCentreforAgeingandNeuroscience(Cam-CAN)datarepository: Structural
andfunctionalMRI,MEG,andcognitivedatafromacross-sectionaladultlifespansample. neuroimage,144:262–269,
2017.
Jordy Thielen, Philip van den Broek, Jason Farquhar, and Peter Desain. Broad-Band visually evoked potentials:
Re(con)volution in Brain-Computer interfacing. PLOS ONE, 10(7):e0133797, July 2015. ISSN 1932-6203. doi:
10.1371/journal.pone.0133797. http://dx.doi.org/10.1371/journal.pone.0133797.
Jordy Thielen, Pieter Marsman, Jason Farquhar, and Peter Desain. From full calibration to zero training for a
code-modulated visual evoked potentials brain computer interface. Journal of Neural Engineering, March 2021.
ISSN 1741-2552. doi: 10.1088/1741-2552/abecef. http://dx.doi.org/10.1088/1741-2552/abecef.
M S Treder, N M Schmidt, and B Blankertz. Gaze-independent brain-computer interfaces based on covert attention
and feature attention. Journal of Neural Engineering, 8(6):066003, October 2011. ISSN 1741-2552. doi: 10.1088/
1741-2560/8/6/066003. http://dx.doi.org/10.1088/1741-2560/8/6/066003.
M S Treder, H Purwins, D Miklody, I Sturm, and B Blankertz. Decoding auditory attention to instruments in
polyphonic music using single-trial EEG classification. Journal of Neural Engineering, 11(2):026009, March 2014.
ISSN 1741-2552. doi: 10.1088/1741-2560/11/2/026009. http://dx.doi.org/10.1088/1741-2560/11/2/026009.
Polina Turishcheva, Paul G Fahey, Michaela Vystrčilová, Laura Hansel, Rachel Froebe, Kayla Ponder, Yongrong Qiu,
23

Konstantin F Willeke, Mohammad Bashiri, Eric Wang, et al. The dynamic sensorium competition for predicting
large-scale mouse visual cortex activity from videos. ArXiv, 2024.
Erwan Vaineau, Alexandre Barachant, Anton Andreev, Pedro L. C. Rodrigues, Grégoire Cattan, and Marco Congedo.
Brain invaders adaptive versus Non-Adaptive P300 Brain-Computer interface dataset, 2018. https://zenodo.org/
record/1494163.
David C Van Essen, Stephen M Smith, Deanna M Barch, Timothy EJ Behrens, Essa Yacoub, Kamil Ugurbil, Wu-
Minn HCP Consortium, et al. The WU-Minn human connectome project: an overview. Neuroimage, 80:62–79,
2013.
Gijsbrecht Franciscus Petrus Van Veen, Alexandre Barachant, Anton Andreev, Grégoire Cattan, Pedro Luis
Coelho Rodrigues, and Marco Congedo. Building brain invaders: EEG data of an experimental validation,
2019. https://zenodo.org/record/2649006.
Christopher Wang, Vighnesh Subramaniam, Adam Uri Yaari, Gabriel Kreiman, Boris Katz, Ignacio Cases, and Andrei
Barbu. BrainBERT:Self-supervisedrepresentationlearningforintracranialrecordings. InTheEleventhInternational
Conference on Learning Representations, 2023.
Eric Y Wang, Paul G Fahey, Zhuokun Ding, Stelios Papadopoulos, Kayla Ponder, Marissa A Weis, Andersen Chang,
Taliah Muhammad, Saumil Patel, Zhiwei Ding, et al. Foundation model of neural activity predicts response to new
stimulus types. Nature, 640(8058):470–477, 2025a.
Guibin Wang, Wenbin Liu, Yiqun He, Cheng Xu, Li Ma, and Hong Li. EEGPT: Pretrained transformer for
universal and reliable representation of EEG signals. In Advances in Neural Information Processing Systems
(NeurIPS), volume 37, pages 39249–39280, 2024. https://proceedings.neurips.cc/paper_files/paper/2024/file/
4540d267eeec4e5dbd9dae9448f0b739-Paper-Conference.pdf.
Jiquan Wang, Sha Zhao, Zhiling Luo, Yangxuan Zhou, Haiteng Jiang, Shijian Li, Tao Li, and Gang Pan. CBraMod:
A criss-cross brain foundation model for EEG decoding. In The Thirteenth International Conference on Learning
Representations (ICLR), 2025b. https://arxiv.org/abs/2412.07236.
Yijun Wang, Xiaogang Chen, Xiaorong Gao, and Shangkai Gao. A benchmark dataset for SSVEP-Based Brain-
Computer interfaces. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 25(10):1746–1752,
October2017. ISSN1558-0210. doi: 10.1109/tnsre.2016.2627556. http://dx.doi.org/10.1109/TNSRE.2016.2627556.
Xiaoxi Wei, A Aldo Faisal, Moritz Grosse-Wentrup, Alexandre Gramfort, Sylvain Chevallier, Vinay Jayaram, Camille
Jeunet, Stylianos Bakas, Siegfried Ludwig, Konstantinos Barmpas, et al. 2021 BEETL competition: Advancing
transfer learning for subject independence and heterogenous EEG data sets. In NeurIPS 2021 Competitions and
Demonstrations Track, pages 205–219. PMLR, 2022.
Konstantin F Willeke, Paul G Fahey, Mohammad Bashiri, Laura Pede, Max F Burg, Christoph Blessing, Santiago A
Cadena, Zhiwei Ding, Konstantin-Klemens Lurz, Kayla Ponder, et al. The sensorium competition on predicting
large-scale mouse primary visual cortex activity. arXiv preprint arXiv:2206.08666, 2022.
Jiamin Wu, Zichen Ren, Junyu Wang, Pengyu Zhu, Yonghao Song, Mianxin Liu, Qihao Zheng, Lei Bai, Wanli
Ouyang,andChunfengSong. AdaBrain-Bench: Benchmarkingbrainfoundationmodelsforbrain-computerinterface
applications. arXiv preprint arXiv:2507.09882, 2025.
WeiXiong,JiangtongLi,JieLi,KunZhu,andChangjunJiang. EEG-FM-Bench: Acomprehensivebenchmarkforthe
systematic evaluation of EEG foundation models. arXiv preprint arXiv:2508.17742, 2025.
ChaoqiYang, M.BrandonWestover, andJimengSun. BIOT:Biosignaltransformerforcross-datalearninginthewild.
In Thirty-seventh Conference on Neural Information Processing Systems (NeurIPS), 2023.
Shihao Yang, Xiying Huang, Danilo Bernardo, Jun-En Ding, Andrew Michael, Jingmei Yang, Patrick Kwan, Ashish
Raj, and Feng Liu. Foundation and large-scale AI models in neuroscience: A comprehensive review. arXiv preprint
arXiv:2510.16658, 2025.
Florian Yger, Maxime Berar, and Fabien Lotte. Riemannian approaches in brain-computer interfaces: a review. IEEE
Transactions on Neural Systems and Rehabilitation Engineering, 25(10):1753–1762, 2016.
Weibo Yi, Shuang Qiu, Kun Wang, Hongzhi Qi, Lixin Zhang, Peng Zhou, Feng He, and Dong Ming. Evaluation of
EEGoscillatorypatternsandcognitiveprocessduringsimpleandcompoundlimbmotorimagery. PLoS ONE,9(12):
e114853, December 2014. ISSN 1932-6203. doi: 10.1371/journal.pone.0114853. http://dx.doi.org/10.1371/journal.
pone.0114853.
24

ZhizhangYuan,FanqiShen,MengLi,YuguoYu,ChenhaoTan,andYangYang. BrainWave: Abrainsignalfoundation
| model for clinical | applications, | 2024. https://arxiv.org/abs/2402.10251. |     |     |     |
| ------------------ | ------------- | --------------------------------------- | --- | --- | --- |
MingfangZhang,JarodLévy,Stéphaned’Ascoli,JérémyRapin,FAlario,PierreBourdillon,SvetlanaPinet,Jean-Rémi
King, et al. From thought to action: How a hierarchy of neural dynamics supports language production. arXiv
| preprint arXiv:2502.07429, |     | 2025. |     |     |     |
| -------------------------- | --- | ----- | --- | --- | --- |
Wei Zhao, Xiaolu Jiang, Baocan Zhang, Shixiao Xiao, and Sujun Weng. CTNet: a convolutional transformer network
| for EEG-based | motor imagery | classification. | Scientific reports, | 14(1):20237, | 2024. |
| ------------- | ------------- | --------------- | ------------------- | ------------ | ----- |
Bangyan Zhou, Xiaopei Wu, Zhao Lv, Lei Zhang, and Xiaojin Guo. A fully automated trial selection method for
optimizationofmotorimagerybasedBrain-Computerinterface. PLOS ONE,11(9):e0162657,September2016. ISSN
1932-6203. doi: 10.1371/journal.pone.0162657. http://dx.doi.org/10.1371/journal.pone.0162657.
Xinliang Zhou, Chenyu Liu, Zhisheng Chen, Kun Wang, Yi Ding, Ziyu Jia, and Qingsong Wen. Brain foundation
models: Asurveyonadvancementsinneuralsignalprocessingandbraindiscovery. IEEESignalProcessingMagazine,
| 42(5):22–35, | 2025. |     |     |     |     |
| ------------ | ----- | --- | --- | --- | --- |
Igor Zyma, Sergii Tukaev, Ivan Seleznov, Ken Kiyono, Anton Popov, Mariia Chernykh, and Oleksii Shpenkov.
Electroencephalograms during mental arithmetic task performance. Data, 4(1):14, January 2019. ISSN 2306-5729.
| doi: 10.3390/data4010014. |     | http://dx.doi.org/10.3390/data4010014. |     |     |     |
| ------------------------- | --- | -------------------------------------- | --- | --- | --- |
25

Appendix
A Additionaldetailsondownstreamdatasetsandtasks
WeprovidethereferencesforalldatasetsusedinNeuralBench-EEGv1.0(andtheMEGandfMRIextensions)
in Table S1. Detailed information about the Core datasets for each task can be found in Table 1. We do not
repeat references when multiple datasets come from the same paper.
Of note, these datasets sometimes contain stimuli presented to the participants (e.g. images, videos, text, etc.).
We only make use of stimuli in the cognitive decoding tasks (Gifford et al., 2022b; Hollenstein et al., 2018;
Brennan and Hale, 2019; Liu et al., 2024b; Nieuwland et al., 2018), as these tasks require the alignment of
brain data to a dense representation of the stimuli. Apart from these cases, we discard stimulus information
and only keep targets (e.g. classes for classification tasks).
Detailed and up-to-date description of the downstream tasks can be found in the benchmark documentation
at https://github.com/facebookresearch/neuroai/tree/main/neuralbench-repo.
B Task-specific architectures and foundation models for EEG downstream
tasks
We list the task-specific deep-learning architectures, handcrafted features-based sklearn baselines, and founda-
tion models used on the EEG downstream tasks in Tables S2, S3 and S4.
C Detailedsplittingstrategy
We split each dataset into a single training, validation and testing partition using a fixed seed. The way we
split depends on the datasets. When datasets explicitly provide a development and evaluation split, we use it
as is. This is the case for clinical event classification on TUEV (Harati et al., 2015), pathology detection on
TUAB (Lopez et al., 2015), image decoding on THINGS-EEG2 (Gifford et al., 2022b) and motor imagery
classification on the BEETL AI Challenge datasets (Wei et al., 2022).
For cognitive decoding experiments, we focus on “leave-concept-out” evaluation, i.e., all subjects are seen in
both training and testing splits, but a common subset of the sessions or concepts are held out for testing. In
many cases, this setting is required to obtain performance significantly above chance-level, as cross-subject
generalization is particularly challenging on these types of tasks. For speech decoding on Brennan and Hale
(2019), we keep the last 4 runs of each recording as test set. For sentence decoding on ZuCo v1 (Hollenstein
et al., 2018), we randomly hold out 20% of the sentences read by the subjects to use as test set. For word
decoding on Nieuwland et al. (2018), we randomly hold out 10% of the sentences read by the subjects to
use as test set. For video decoding on SEED-DV (Liu et al., 2024b), we keep a random 20% of the video
concepts (e.g. land animal, human, natural scene, etc.) to use as test set. For typing decoding on (Lévy
et al., 2025), sentences are clustered using their similarity in sentence embedding space (TF-IDF), and 20% of
similar sentences are held out for testing.
Most remaining tasks/datasets use a cross-subject split. For age, psychopathology, sex and reaction time
prediction, all on the HBN-EEG dataset (Shirazi et al., 2024), we leave out all recordings from release 5
(out of 11 releases) for testing, which corresponds to ∼329 held-out subjects. For other tasks, we hold out
a random 20% of the subjects for testing. Of note, this cross-subject strategy is particularly challenging
for certain tasks as inter-subject variability renders generalization difficult, e.g. in BCI (Saha and Baumert,
2020). Moreover, on clinical diagnosis tasks where subjects receive a single diagnosis (dementia, depression,
Parkinson’s disease and schizophrenia), we use stratified splits based on the diagnosis label.
A few datasets instead use a within-subject split by default to accommodate low (<10) subject counts, by
keeping the last (few) sessions or runs for testing (Zhou et al., 2016; Chavarriaga and Millan, 2010; Hoffmann
et al., 2008; Kueper et al., 2024).
26

Finally, we use fully random splits, i.e., at the example level, for three low-sample datasets: audiovisual
stimulus classification on the MNE Sample dataset (Gramfort et al., 2013) and motor imagery classification
| on the datasets |     | from Dornhege | et  | al. (2004); | Barachant |     | (2012). |     |
| --------------- | --- | ------------- | --- | ----------- | --------- | --- | ------- | --- |
Validation sets (used for early stopping) are sampled from the remaining data, using the same or a similar
splitting strategy as used for the test set, targeting another 20% of the overall dataset size. We train each
modeloneachtaskthreetimes, usingthreedifferentrandomseedsfortheinitializationofthe(non-pretrained)
model parameters.
D Performancemetrics
We pick a single representative metric per task type to report in this document. For binary and multiclass
| classification, | we  | use the | balanced | accuracy: |     |     |     |     |
| --------------- | --- | ------- | -------- | --------- | --- | --- | --- | --- |
C
|     |     |     |     |     |     |     | 1 (cid:88) TP |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- |
c
|     |     |     | Balanced |     | Accuracy= |     |          | (S1) |
| --- | --- | --- | -------- | --- | --------- | --- | -------- | ---- |
|     |     |     |          |     |           |     | C TP +FN |      |
|     |     |     |          |     |           |     | c=1 c c  |      |
where C is the number of classes, TP c is the number of true positives for class c, and FN c is the number of
| false negatives |     | for class c.    |        |           |           |          |              |      |
| --------------- | --- | --------------- | ------ | --------- | --------- | -------- | ------------ | ---- |
| For multilabel  |     | classification, | we use | the macro | F1-score: |          |              |      |
|                 |     |                 |        |           | 1         | C        | 1 C 2P R     |      |
|                 |     |                 |        |           |           | (cid:88) | (cid:88) c c |      |
|                 |     |                 | Macro  | F1=       |           | F1       | =            | (S2) |
|                 |     |                 |        |           | C         | c        | C P +R       |      |
c c
|     |     |     |     |     |     | c=1 | c=1 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
where P = T P c is the precision and R = T P c is the recall for class c.
|                | c TP | c+ F Pc     |            |         | c TPc        | + F Nc |     |     |
| -------------- | ---- | ----------- | ---------- | ------- | ------------ | ------ | --- | --- |
| For univariate |      | regression, | we use the | Pearson | correlation: |        |     |     |
(cid:80)n
|     |     |     |     |     |     | (y −y¯)(yˆ | −y¯ˆ) |      |
| --- | --- | --- | --- | --- | --- | ---------- | ----- | ---- |
|     |     |     |     | r = | i=1 | i          | i     | (S3) |
(cid:113)
|     |     |     |     | (cid:112)(cid:80)n |     |       | (cid:80)n −y¯ˆ)2 |     |
| --- | --- | --- | --- | ------------------ | --- | ----- | ---------------- | --- |
|     |     |     |     |                    | (y  | −y¯)2 | (yˆ              |     |
|     |     |     |     |                    | i=1 | i     | i=1 i            |     |
y¯ˆ
where y are the true values, yˆ are the predicted values, y¯ and are their respective means, and n is the
|          | i              |     | i             |           |     |     |     |     |
| -------- | -------------- | --- | ------------- | --------- | --- | --- | --- | --- |
| number   | of samples.    |     |               |           |     |     |     |     |
| Finally, | for retrieval, | we  | use the top-5 | accuracy: |     |     |     |     |
N
|     |     |     |     |       |           | 1   | (cid:88) (cid:104) ∈Yˆ(k) (cid:105) |      |
| --- | --- | --- | --- | ----- | --------- | --- | ----------------------------------- | ---- |
|     |     |     |     | Top-k | Accuracy= |     | 1 y                                 | (S4) |
|     |     |     |     |       |           | N   | i i                                 |      |
i=1
Yˆ(k)
with k =5, where N is the number of queries, y is the true label (or relevant item) for query i, is the
|     |     |     |     |     |     | i   | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
set of the top-k retrieved candidates for query i, and 1[·] is the indicator function.
More metrics are computed in NeuralBench, e.g. root mean-squared error (RMSE) for regression and median
| ranks for | retrieval, | but are | not reported | here | for | brevity. |     |     |
| --------- | ---------- | ------- | ------------ | ---- | --- | -------- | --- | --- |
AdditionalresultsonNeuralBench-EEG-Core v1.0
E
| Figure                                  | S1 shows | max-normalized | scores | over | core | datasets. |      |     |
| --------------------------------------- | -------- | -------------- | ------ | ---- | ---- | --------- | ---- | --- |
| AdditionalresultsonNeuralBench-EEG-Full |          |                |        |      |      |           | v1.0 |     |
F
Figure S2 shows performance on each multi-dataset downstream task included in NeuralBench-EEG-Full
v1.0.
27

|     |     |     | Evoked | Internal |     |
| --- | --- | --- | ------ | -------- | --- |
Cognitive BCI Responses Clinical State Sleep Phenotyping Misc
Task best
1.0
⋆̃s erocs dezilamroN 0.8
0.6
0.4
0.2
| 0.0 |     |     |     |     | Dummy |
| --- | --- | --- | --- | --- | ----- |
e e h yping Video Word P y on agery 0 SVEP Audiovisual ERN MN N170 N2pc N400 P t a n 's y a izure n th . d a l p stage e ology Sex t me
a g ten c eec V E e r t i P30 L R e n n t i s io o n o g ren i t i o ri loa u s A g fa c on ti
I m n p T c - m a g c u m S M inical e v m e e s in s h o l h e m o  a rk leep aro h r ti
S e S   i x e r  i D e p r r k a t o p S E t a l W o e Psychopa t A ti
|     | Ment | a l r   e o | D e P a P h i z | e n S l e | a c |
| --- | ---- | ----------- | --------------- | --------- | --- |
|     |      | o t o M o t | C l S c         | M S       | R e |
M
|     | Best foundation model       |     | Best task-specific model       | Foundation model wins    |     |
| --- | --------------------------- | --- | ------------------------------ | ------------------------ | --- |
|     | Mean over foundation models |     | Mean over task-specific models | Task-specific model wins |     |
FigureS1 Max-normalized performance s˜∗ across downstream tasks, for the best and “average” models. As in Figure 5,
but scores are normalized to be between “dummy” performance and per-task best model performance, highlighting
| variability | as compared | to the highest performing | model. |     |     |
| ----------- | ----------- | ------------------------- | ------ | --- | --- |
28

TableS1 Dataset references for all NeuralBench-EEG v1.0 tasks, grouped by category. References for the primary
| dataset are listed | first; additional |     | dataset references | follow. |            |     |     |     |     |     |     |     |
| ------------------ | ----------------- | --- | ------------------ | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| Category           | Task              |     |                    | Dataset | references |     |     |     |     |     |     |     |
Image Gifford et al. (2022a), Hebart et al. (2023), Allen et al. (2022)
|     | Sentence |     |     | Hollenstein | et       | al. (2018) |     |     |     |     |     |     |
| --- | -------- | --- | --- | ----------- | -------- | ---------- | --- | --- | --- | --- | --- | --- |
|     | Speech   |     |     | Brennan     | and Hale | (2019)     |     |     |     |     |     |     |
Cognitive
|     | Typing |     |     | Lévy et    | al. (2025); | Zhang  | et  | al. (2025) |     |     |     |     |
| --- | ------ | --- | --- | ---------- | ----------- | ------ | --- | ---------- | --- | --- | --- | --- |
|     | Video  |     |     | Liu et al. | (2024b)     |        |     |            |     |     |     |     |
|     | Word   |     |     | Nieuwland  | et al.      | (2018) |     |            |     |     |     |     |
c-VEP Cabrera Castillos et al. (2023), Martínez-Cagigal (2023), Martínez-
|     |        |         |     | Cagigal | (2024),       | Thielen | et al. | (2015), | Thielen | et al. | (2021) |     |
| --- | ------ | ------- | --- | ------- | ------------- | ------- | ------ | ------- | ------- | ------ | ------ | --- |
|     | Mental | imagery |     | Scherer | et al. (2015) |         |        |         |         |        |        |     |
BCI
Motor execution Srisrisawang and Müller-Putz (2024), Schirrmeister et al. (2017),
|     |     |     |     | Ofner et | al. (2017) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Motor imagery Stieger et al. (2021), Schalk et al. (2004), Barachant (2012), Cho
|     |     |     |     | et al. (2017), |                | Dornhege | et al.   | (2004),       | Dreyer  | et al.      | (2023),     | Faller      |
| --- | --- | --- | --- | -------------- | -------------- | -------- | -------- | ------------- | ------- | ----------- | ----------- | ----------- |
|     |     |     |     | et al. (2012), | Grosse-Wentrup |          |          | et al.        | (2009), | Lee et      | al. (2019), | Leeb        |
|     |     |     |     | et al. (2007), | Liu            | et al.   | (2024a), | Schwarz       | et      | al. (2020), |             | Shin et al. |
|     |     |     |     | (2017),        | Scherer        | et al.   | (2012),  | Tangermann    | et      | al. (2012), |             | Wei et al.  |
|     |     |     |     | (2022), Yi     | et al.         | (2014),  | Zhou     | et al. (2016) |         |             |             |             |
P300 Schreuder et al. (2010), Kappenman et al. (2021), Acqualagna and
|     |     |     |     | Blankertz | (2013), | Aricò | et al. | (2014), | Cattan | et al. | (2019), | Vaineau |
| --- | --- | --- | --- | --------- | ------- | ----- | ------ | ------- | ------ | ------ | ------- | ------- |
etal.(2018),Gugeretal.(2009),Haufeetal.(2011),Hoffmannetal.
|     |     |     |     | (2008),        | Hübner         | et al.  | (2017),      | Hübner  | (2016),      | Kojima      | and        | Kanoh   |
| --- | --- | --- | --- | -------------- | -------------- | ------- | ------------ | ------- | ------------ | ----------- | ---------- | ------- |
|     |     |     |     | (2024), Kojima |                | (2024), | Korczowski   | et      | al. (2019b), |             | Korczowski | et al.  |
|     |     |     |     | (2019c),       | Korczowski     | et      | al. (2019a), | Lee     | et al.       | (2019),     | Riccio     | et al.  |
|     |     |     |     | (2013),        | Romani         | et al.  | (2025),      | Schaeff | et al.       | (2012),     | Höhne      | (2011), |
|     |     |     |     | Sosulski       | and Tangermann |         | (2019),      | Treder  | et           | al. (2011), | Treder     | et al.  |
|     |     |     |     | (2014), Van    | Veen           | et al.  | (2019)       |         |              |             |            |         |
SSVEP Wangetal.(2017),Leeetal.(2019),Kalungaetal.(2016),Nakanishi
|     |             |          |     | et al. (2015), | Oikonomou |        | et al. | (2016) |     |     |     |     |
| --- | ----------- | -------- | --- | -------------- | --------- | ------ | ------ | ------ | --- | --- | --- | --- |
|     | Audiovisual | stimulus |     | Gramfort       | et al.    | (2013) |        |        |     |     |     |     |
Error-related negativity Kappenman et al. (2021), Kueper et al. (2024), Chavarriaga and
Millan (2010)
Evoked
|     | MMN |     |     | Kappenman | et  | al. (2021) |     |     |     |     |     |     |
| --- | --- | --- | --- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
Responses
|          | N170          |                 |           | Kappenman  | et         | al. (2021)  |          |     |            |     |     |     |
| -------- | ------------- | --------------- | --------- | ---------- | ---------- | ----------- | -------- | --- | ---------- | --- | --- | --- |
|          | N2pc          |                 |           | Kappenman  | et         | al. (2021), | Reichert | et  | al. (2020) |     |     |     |
|          | N400          |                 |           | Kappenman  | et         | al. (2021)  |          |     |            |     |     |     |
|          | Lateralized   | readiness       | potential | Kappenman  | et         | al. (2021)  |          |     |            |     |     |     |
|          | Clinical      | event detection |           | Harati et  | al. (2015) |             |          |     |            |     |     |     |
|          | Dementia      | diagnosis       |           | Miltiadous | et al.     | (2023)      |          |     |            |     |     |     |
|          | Depression    | diagnosis       |           | Mumtaz     | et al.     | (2018)      |          |     |            |     |     |     |
| Clinical | Parkinson’s   | diagnosis       |           | Singh et   | al. (2021) |             |          |     |            |     |     |     |
|          | Pathology     |                 |           | Lopez de   | Diego      | (2017)      |          |     |            |     |     |     |
|          | Schizophrenia | diagnosis       |           | Albrecht   | et al.     | (2019)      |          |     |            |     |     |     |
|          | Seizure       | detection       |           | Dan and    | Shoeb      | (2023)      |          |     |            |     |     |     |
|          | Emotion       | recognition     |           | Chen et    | al. (2023) |             |          |     |            |     |     |     |
Internal
State Mental arithmetic Zyma et al. (2019), Shin et al. (2017)
Mental workload Hinss et al. (2022), Hinss et al. (2023), Jao et al. (2023)
|     | Sleep arousal |     |     | Ghassemi | et al. | (2018) |     |     |     |     |     |     |
| --- | ------------- | --- | --- | -------- | ------ | ------ | --- | --- | --- | --- | --- | --- |
Sleep
|             | Sleep stage     |           |     | Kemp et  | al. (2000)    |     |     |     |     |     |     |     |
| ----------- | --------------- | --------- | --- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
|             | Age             |           |     | Shirazi  | et al. (2024) |     |     |     |     |     |     |     |
| Phenotyping | Psychopathology |           |     | Shirazi  | et al. (2024) |     |     |     |     |     |     |     |
|             | Sex             |           |     | Shirazi  | et al. (2024) |     |     |     |     |     |     |     |
|             | Artifact        | detection |     | Hamid et | al. (2020)    |     |     |     |     |     |     |     |
Misc
|     | Reaction | time |     | Shirazi | et al. (2024) |     |     |     |     |     |     |     |
| --- | -------- | ---- | --- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
29

TableS2 Task-specific EEG models evaluated in NeuralBench-EEG v1.0. Parameter counts are backbone-only
(excluding the task-specific output head) and are approximate as they depend on the number of input channels (we
| use a representative |     | value | of C=22)          | here. |     |          |               |                |        |     |
| -------------------- | --- | ----- | ----------------- | ----- | --- | -------- | ------------- | -------------- | ------ | --- |
|                      |     |       | Model             |       |     | # Params | Reference     |                |        |     |
|                      |     |       | ShallowFBCSPNet   |       |     | 36K      | Schirrmeister | et al.         | (2017) |     |
|                      |     |       | Deep4Net          |       |     | 146K     | Schirrmeister | et al.         | (2017) |     |
|                      |     |       | EEGNet            |       |     | 1.5K     | Lawhern       | et al. (2018)  |        |     |
|                      |     |       | BDTCN             |       |     | 27K      | Gemein        | et al. (2020)  |        |     |
|                      |     |       | EEGConformer      |       |     | 277K     | Song          | et al. (2022)  |        |     |
|                      |     |       | ATCNet            |       |     | 29K      | Altaheri      | et al. (2022)  |        |     |
|                      |     |       | SimpleConvTimeAgg |       |     | 4.2M     | El            | Ouahidi et al. | (2023) |     |
|                      |     |       | CTNet             |       |     | 150K     | Zhao          | et al. (2024)  |        |     |
TableS3 Handcrafted features-based sklearn baselines evaluated in NeuralBench-EEG v1.0. These pipelines are fit
once on the concatenation of the training and validation sets and evaluated with the exact same preprocessing and
splits as the deep learning models. A single pipeline is used per task type; see Tasks column.
| Pipeline |     | Description |     |     |     |     | Tasks |     |     | Reference |
| -------- | --- | ----------- | --- | --- | --- | --- | ----- | --- | --- | --------- |
XdawnTsLR xDAWNcovariances→shrinkage→tan- Classification: Evoked re- Rivet et al. (2009),
gentspace→standardscaling→logistic sponse and P300 Barachant and Con-
|     |     | regression | (CV-tuned | C)  |     |     |     |     |     | gedo (2014) |
| --- | --- | ---------- | --------- | --- | --- | --- | --- | --- | --- | ----------- |
CovTsLR sample covariances → shrinkage → tan- Classification: BCI (except Barachant et al.
|     |     | gentspace→standardscaling→logistic |           |     |                |     | P300andSSVEP),Internal |           |             | (2011) |
| --- | --- | ---------------------------------- | --------- | --- | -------------- | --- | ---------------------- | --------- | ----------- | ------ |
|     |     | regression                         | (CV-tuned |     | C; one-vs-rest |     | for State,             | Clinical, | Sleep, sex, |        |
|     |     | multilabel)                        |           |     |                |     | artifact               |           |             |        |
CoSpectraLogLR Welchco-spectra→upper-triangularflat- Classification: SSVEP Kalunga et al. (2016)
|     |     | ten with | log(1+x)   | on        | the diagonal | (per- |     |     |     |     |
| --- | --- | -------- | ---------- | --------- | ------------ | ----- | --- | --- | --- | --- |
|     |     | channel  | PSD) →     | standard  | scaling      | →     | lo- |     |     |     |
|     |     | gistic   | regression | (CV-tuned | C)           |       |     |     |     |     |
CovTsRidge sample covariances → shrinkage → tan- Regression: age, psy- Barachant et al.
gent space → standard scaling → ridge chopathology, reaction (2011), Hoerl and
regression (CV-tuned α) time; Retrieval (treated Kennard (1970)
|     |     |     |     |     |     |     | as     | multivariate | regression |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | ---------- | --- |
|     |     |     |     |     |     |     | here): | Cognitive    |            |     |
EEGfoundationmodelsevaluatedinNeuralBench-EEGv1.0. Parametercountsarebackbone-only(excluding
TableS4
the task-specific linear probe). Pretraining data quantities are reported as published; TUEG refers to the Temple
| University | Hospital | EEG Corpus. |          |     |             |     |     |      |     |           |
| ---------- | -------- | ----------- | -------- | --- | ----------- | --- | --- | ---- | --- | --------- |
| Model      | Variant  |             | # Params |     | Pretraining |     |     | Data |     | Reference |
BENDR — 157.1M Wav2vec-like contrastive TUEG, ∼1.5K h Kostas et al. (2021)
BIOT 6-datasets- 3.2M Contrastive+supervised 6 datasets (CHB- Yang et al. (2023)
|     | 18chs |     |     |     |     |     |     | MIT, TUAB,  | TUEV, |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | ----------- | ----- | --- |
|     |       |     |     |     |     |     |     | +3 private) |       |     |
LaBraM Base 5.8M VQ-VAE masked predic- 16 datasets, ∼2.5K h Jiang et al. (2024)
tion
CBraMod — 4.9M Maskedpatchreconstruc- TUEG, ∼27K h Wang et al. (2025b)
tion
LUNA Large 40.4M Maskedpatchreconstruc- TUEG + Siena Döner et al. (2025)
tion
REVE Base 69.2M Maskedpatchreconstruc- 92 datasets, ∼60K h El Ouahidi et al. (2025)
tion
30

over datasets
|     |     | Thielen2021 | CabreraCastillos2023CabreraCastillos2023CabreraCastillos2023CabreraCastillos2023 |     |     |     | MartinezCagigal2023 | MartinezCagigal2024 | Thielen2015 |     |
| --- | --- | ----------- | -------------------------------------------------------------------------------- | --- | --- | --- | ------------------- | ------------------- | ----------- | --- |
Be st Me r a a n n   k n   o ↑ rm. From B urstCvep100 BurstCvep40 BurstVep100 BurstVep40 Dataset Dataset Broad
|     | (0 ) | 91  | 7 9 | 87  | 82  | 81  | 44  | 15  | 7   |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
PEV-c
Worst
(1)
|     | over datasets              | Srisrisawang2024 | Ofner2017      | Schirrmeister2017 |              |            |     |                              |     |     |
| --- | -------------------------- | ---------------- | -------------- | ----------------- | ------------ | ---------- | --- | ---------------------------- | --- | --- |
|     | noitucexe rotoM Mean norm. | Simultaneous     | UpperExecution | Deep              |              |            |     |                              |     |     |
|     | rank ↑                     | 61               | 29             | 79                |              |            |     |                              |     |     |
|     | over datasets              | Stieger2021      | Barachant2012  | Cho2017           | Dornhege2004 | Dreyer2023 |     | Faller2012 GrosseWentrup2009 |     |     |
Mean norm. Continuous Robust Supporting Boosting Large Autocalibration Beamforming Lee2019EegMi Leeb2007Brain
|     | rank ↑ | 71  | 49  | 79  | 84  | 82  | 75  | 78  | 79  | 81  |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
yregami rotoM
|     |     |     | 25         | 40          | 40          | 35  | 40             | 40  | 40  | 40  |
| --- | --- | --- | ---------- | ----------- | ----------- | --- | -------------- | --- | --- | --- |
|     |     |     | Schalk2004 | Scherer2012 | Schwarz2020 |     | Tangermann2012 |     |     |     |
Liu2024Eeg Bci2000 Brain Analyzing Shin2017OpenA Review Wei2022BeetlA Wei2022BeetlB Zhou2016Fully
|     |     | 58  | 72  | 62  | 59  | 70  | 57  | 55  | 63  | 79  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | 40  |     | 40  | 25  | 40  |     | 25  | 25  |     |
over datasets
Schreuder2010 Acqualagna2013 Arico2014 Cattan2019 Hoffmann2008 Hubner2017
Mean norm. rank ↑ New Gaze Influence Dataset Guger2009How Haufe2011Eeg Efficient Hubner2016Eeg Learning
|     |     | 70  | 77  | 88  | 69  | 66  | 95  | 74  | 94  | 95  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | 40  | 40  | 40  | 40  | 40  | 40  | 40  | 40  | 40  |
Kappenman2021 Kojima2024 Kojima2024 Korczowski2019 Korczowski2019 Korczowski2019 Korczowski2019 Riccio2013
ErpP3 ReplicationA ReplicationB BrainBi2014A BrainBi2014B BrainBi2015A BrainBi2015B Lee2019EegErp Attention
|     |     | 70  | 71  | 67  | 72  | 78  | 80  | 74  | 87  | 79  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
003P
|     |     | 40         | 40          | 40                   | 40         | 40         | 40  | 40          | 40  | 40  |
| --- | --- | ---------- | ----------- | -------------------- | ---------- | ---------- | --- | ----------- | --- | --- |
|     |     | Romani2025 | Schaeff2012 | Sosulski2019         | Treder2011 | Treder2014 |     | VanVeen2019 |     |     |
|     |     | Brainform  | Exploring   | Electroencephalogram | Gaze       | Decoding   |     | Building    |     |     |
|     |     | 94         | 70          | 71                   | 80         | 63         | 70  |             |     |     |
|     |     | 40         | 40          | 40                   | 40         | 40         | 40  |             |     |     |
over datasets
|     | Mean norm. | Benchmark Wang2017 | Kalunga2016 Online | EegSsvep Lee2019 | Nakanishi2015 Comparison | Oikonomou2016 ComparativeA | Oikonomou2016 | ComparativeB Oikonomou2016 ComparativeC |     |     |
| --- | ---------- | ------------------ | ------------------ | ---------------- | ------------------------ | -------------------------- | ------------- | --------------------------------------- | --- | --- |
|     | rank ↑     | 100                | 82                 | 96               | 80                       | 58                         | 66            | 37                                      |     |     |
PEVSS
10
over datasets
|     | Mean norm. | Kappenman2021 | Chavarriaga2010 |               |     |     |     |     |     |     |
| --- | ---------- | ------------- | --------------- | ------------- | --- | --- | --- | --- | --- | --- |
|     | rank ↑     | ErpErn        | Learning        | Kueper2024Eeg |     |     |     |     |     |     |
|     |            | 87            | 84              | 100           |     |     |     |     |     |     |
NRE
|     |     | 40  | 40  | 40  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
over datasets
Kappenman2021 Reichert2020 Baselines Task-specific models Foundation models
|     | Mean norm. | ErpN2pc | Impact |     |     |        |     |                 |       |     |
| --- | ---------- | ------- | ------ | --- | --- | ------ | --- | --------------- | ----- | --- |
|     | rank ↑     | 68      | 63     |     |     | Chance |     | ShallowFBCSPNet | BENDR |     |
cp2N
|     |               |          |     |     |     | Dummy       |     | Deep4Net | BIOT    |     |
| --- | ------------- | -------- | --- | --- | --- | ----------- | --- | -------- | ------- | --- |
|     |               | 40       | 40  |     |     | Handcrafted |     | EEGNet   | LaBraM  |     |
|     |               |          |     |     |     | Seen during |     | BDTCN    | CBraMod |     |
|     | over datasets | Zyma2019 |     |     |     |             |     |          |         |     |
Mean norm.Electroencephalograms Shin2017OpenB pretraining EEGConformer LUNA
|     | .htira latneM rank ↑ | 77  | 66  |     |     |     |     |        |      |     |
| --- | -------------------- | --- | --- | --- | --- | --- | --- | ------ | ---- | --- |
|     |                      |     |     |     |     |     |     | ATCNet | REVE |     |
SimpleConvTimeAgg
|     |     | 40  | 40  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
CTNet
over datasets
|     | Mean norm. | Hinss2023Open | Hinss2021Open | Jao2023Eeg |     |     |     |     |     |     |
| --- | ---------- | ------------- | ------------- | ---------- | --- | --- | --- | --- | --- | --- |
|     | rank ↑     | 78            | 59            | 68         |     |     |     |     |     |     |
daolkroW
40
FigureS2 Performanceobtainedbythedifferenttask-specific(blue)andfoundation(orange)modelsonthemulti-dataset
| NeuralBench-EEG-Full |     |     | v1.0 downstream | tasks | (see Figure | 4’s caption |     | for details). |     |     |
| -------------------- | --- | --- | --------------- | ----- | ----------- | ----------- | --- | ------------- | --- | --- |
31