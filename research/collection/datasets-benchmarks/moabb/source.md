1
| MOABB: |     | Trustworthy |     |     |     | algorithm |     |     | benchmarking |     |     |     |     | for |
| ------ | --- | ----------- | --- | --- | --- | --------- | --- | --- | ------------ | --- | --- | --- | --- | --- |
BCIs
|     |     |     |     | Vinay | Jayaram∗†, |     | Alexandre | Barachant‡ |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | ---------- | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- |
∗
Max Planck Institute for Intelligent Systems, Department Empirical Inference, Tu¨bingen, Germany
|     |     |     |     |     | Email: | vjayaram@tue.mpg.de |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
† IMPRS for Cognitive and Systems Neuroscience, University of Tu¨bingen, Tu¨bingen, Germany
‡
|     |     |     |     |        | CTRL-Labs,                    |     | New-York, | USA |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | ----------------------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | Email: | alexandre.barachant@gmail.com |     |           |     |     |     |     |     |     |     |
8102 yaM 61  ]CH.sc[  1v72460.5081:viXra
Abstract—BCI algorithm development has long been ham- Over the years many datasets have been published online,
| pered by          | two major issues: |             | Small sample |          | sets and | a lack     | of         |            |               |          |            |             |             |         |
| ----------------- | ----------------- | ----------- | ------------ | -------- | -------- | ---------- | ---------- | ---------- | ------------- | -------- | ---------- | ----------- | ----------- | ------- |
|                   |                   |             |              |          |          |            | and serve  | as         | an attractive | option   | when       | time        | or hardware | do      |
| reproducibility.  | We offer          | a solution  |              | to both  | of these | problems   |            |            |               |          |            |             |             |         |
|                   |                   |             |              |          |          |            | not permit | recording  | a             | new one. | In the     | last        | year and    | a half, |
| via a software    | suite that        | streamlines |              | both the | issues   | of finding |            |            |               |          |            |             |             |         |
|                   |                   |             |              |          |          |            | over       | a thousand | journal       | and      | conference | submissions |             | have    |
| and preprocessing | data              | in a        | reliable     | manner,  | as well  | as         | that       |            |               |          |            |             |             |         |
of using a consistent interface for machine learning methods. been written on the BCI Competition III [5, 27] and IV [32]
By building on recent advances in software for signal analysis datasets. Considering that these datasets have been available
| implementedinthe | MNEtoolkit,andthe |       |                  | unifiedframeworkfor |              |           |            |         |                |         |             |          |           |             |
| ---------------- | ----------------- | ----- | ---------------- | ------------------- | ------------ | --------- | ---------- | ------- | -------------- | ------- | ----------- | -------- | --------- | ----------- |
|                  |                   |       |                  |                     |              |           | publically | for     | over a decade, | the     | true number |          | of papers | which       |
| machine learning | offered           | by    | the scikit-learn |                     | project,     | we offer  |            |         |                |         |             |          |           |             |
|                  |                   |       |                  |                     |              |           | validate   | results | against        | them is | likely much | higher.  |           | While it is |
| a system         | that can improve  |       | BCI algorithm    |                     | development. |           | This       |         |                |         |             |          |           |             |
|                  |                   |       |                  |                     |              |           | impossible | to      | deny the       | impact  | these two   | datasets | have      | had on      |
| system is fully  | open-source       | under | the              | BSD licence         | and          | available |            |         |                |         |             |          |           |             |
athttps://github.com/NeuroTechX/moabb.Tovalidateourefforts, the field, relying so heavily on a small number of datasets –
we analyze a set of state-of-the-art decoding algorithms across with less than 50 subjects total – exposes the field to several
12 open access datasets, with over 250 subjects. Our analysis importantissues.Inparticular,overfittingtothesetupsoffered
| confirms    | that different       | datasets | can        | result       | in very | different |         |            |          |      |                  |     |              |     |
| ----------- | -------------------- | -------- | ---------- | ------------ | ------- | --------- | ------- | ---------- | -------- | ---- | ---------------- | --- | ------------ | --- |
|             |                      |          |            |              |         |           | there   | is likely. |          |      |                  |     |              |     |
| results for | identical processing |          | pipelines, | highlighting |         | the need  |         |            |          |      |                  |     |              |     |
|             |                      |          |            |              |         |           | Lastly, | and        | possibly | most | problematically, |     | the scarcity | of  |
fortrustworthyalgorithmbenchmarkinginthefieldofBCIs,and
further that many previously validated methods do not hold up available code for BCI algorithms old and new puts the
when applied across different datasets, which has wide-reaching onus on each individual lab to reproduce the code for all
implications for practical BCIs. other competing methods in order to make a claim to be
|     |     |     |     |     |     |     | comparable |          | with the | ’state-of-the-art’ |           | (SOA). | As     | a result, |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | -------- | ------------------ | --------- | ------ | ------ | --------- |
|     |     |     |     |     |     |     | the vast   | majority | of       | novel BCI          | algorithm |        | papers | compare   |
I. INTRODUCTION
|     |     |     |     |     |     |     | either | against | other work | from | the same | lab, | or  | old, easily |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ---------- | ---- | -------- | ---- | --- | ----------- |
Brain-computer interfaces (BCIs) have long presented the implementable standards such as CSP [19] or channel-level
neuroscience methods community with a unique challenge. variances combined with a classifier of choice [12].
Unlikeinvisionresearch,whereonehasadatabaseofimages Computer vision has solved this problem with enormous
and labels, a BCI is defined by a signal recorded from the datasets like Imagenet [10] bundled with machine learning
brainandfedintoacomputer,whichcanbeinfluencedinany packages(Tensorflow[1],PyTorch,andTheano[23]).However,
number of ways both by the subject and by the experimenter. generatingBCIdataisoftenaverytaxingprocessbothphysi-
As a result, validating approaches has always been a difficult callyandmentally,andsoitisnotreasonabletocreatedatasets
task. Number of channels, requested task, physical setup, and of such size. Rather, the field requires many different people
many other features vary between the numerous publically recording data in many contexts in order to create an ap-
availabledatasetsonline,nottomentionissuesofconvenience
|     |     |     |     |     |     |     | propriate | benchmark. | We  | propose | our | platform, | the | MOABB |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ------- | --- | --------- | --- | ----- |
such as file format and documentation. Because of this, the (Mother Of All BCI Benchmarks) Project, as a candidate for
BCI methods community has long done one of two things to this application. The MOABB project consists of the aggre-
validate an new approach: Recorded a new dataset, or used gation of many publicly available EEG datasets, converted to
one of few well-known, tried-and-true datasets. a common format and bundled in the software package, as
Recording a new dataset, the ideal way to show that a well as a collection of SOA algorithms. Using this system
proposed method works in practice, presents problems for researchers can to automatically benchmark those algorithms
post-hocanalysis.Withoutmakingdatapublic,itisimpossible and run an automated statistical analysis, making the process
to know whether offline classification results are convincing of validating new algorithms painless and reproducible. The
or due to some coding issue or recording artifact. Further, it sourcecodeiswritteninPythonandpublicallyavailableunder
is well-known that differences in hardware [21, 28], paradigm the BSD licence at https://github.com/NeuroTechX/moabb.
[2], and subject [2] can have large differences in the outcome As an initial validation of this project, we present results
of a BCI task, making it very difficult to generalize findings on the constrained task of binary classification in two-class
from any single dataset. imaginedmotorimagery,asthatisthemostwidelyusedmotor

2
imagery paradigm and allows us to demonstrate the process pre-processing of the continuous data, in the form of ICA
across the largest number of datasets. However, we note that cleaning, bandpass filtering, and so on. These must also be
this is only the first question we attempt to answer in this identical for valid comparisons across algorithm or datasets.
field. The format allows for many other questions, including Lastly, there are questions of how to cut the data into trials:
different channel types (EEG, fNIRS, or other), multi-class What is the trial length and overlap; or, in the case of ERP
paradigms, and also transfer learning scenarios as described paradigms, how long before and after the event marker do we
in [17]. use? The answers to all these questions are summed up in the
|     |     |     |     |     |     |     |     | paradigm       | object. |      |     |         |       |             |       |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------- | ---- | --- | ------- | ----- | ----------- | ----- |
|     |     |     |     |     |     |     |     | 2) Evaluation: |         | Once | the | data is | split | into trials | and a |
II. METHODS
|            |          |           |         |             |           |     |              | pipeline | is fixed,   | there | are many     | ways | to train | and  | test this |
| ---------- | -------- | --------- | ------- | ----------- | --------- | --- | ------------ | -------- | ----------- | ----- | ------------ | ---- | -------- | ---- | --------- |
| Any BCI    | analysis | is        | defined | by three    | elements: |     | A dataset,   |          |             |       |              |      |          |      |           |
|            |          |           |         |             |           |     |              | pipeline | to minimize |       | overfitting. | For  | datasets | with | multiple  |
| a context, | and a    | pipeline. | Here    | we describe |           | how | all of these |          |             |       |              |      |          |      |           |
subjectsrecordedonmultipledays,wemaywanttodetermine
| components | are | dealt with | within | our | framework, |     | and how |                 |     |           |      |              |     |                 |     |
| ---------- | --- | ---------- | ------ | --- | ---------- | --- | ------- | --------------- | --- | --------- | ---- | ------------ | --- | --------------- | --- |
|            |     |            |        |     |            |     |         | which algorithm |     | functions | best | in multi-day |     | classification. | Or, |
specificallywesettheoptionsfortheinitialanalysespresented
|     |     |     |     |     |     |     |     | we may | want | to determine | which | algorithm |     | is best | for small |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---- | ------------ | ----- | --------- | --- | ------- | --------- |
here.
|     |     |     |     |     |     |     |     | amounts            | of training | data. | It        | is easy | to see     | that | there are |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | ----------- | ----- | --------- | ------- | ---------- | ---- | --------- |
|     |     |     |     |     |     |     |     | many possibilities |             | for   | splitting | data    | into train | and  | test sets |
A. Datasets
|     |     |     |     |     |     |     |     | depending | on          | the question |         | to be answered, |              | and these | must  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ------------ | ------- | --------------- | ------------ | --------- | ----- |
|     |     |     |     |     |     |     |     | be fixed  | identically | for          | a given | analysis.       | Furthermore, |           | there |
PublicBCIdatasetsexistforawiderangeofuserparadigms
|               |             |     |      |            |     |       |            | is the question |     | of how | to report | results. | Multiclass |     | problems |
| ------------- | ----------- | --- | ---- | ---------- | --- | ----- | ---------- | --------------- | --- | ------ | --------- | -------- | ---------- | --- | -------- |
| and recording | conditions, |     | from | continuous |     | usage | to single- |                 |     |        |           |          |            |     |          |
session to multiple-sessions-per-subject. Within the current cannotusemetricsliketheROC-AUCwhichprovideunbiased
|     |     |     |     |     |     |     |     | estimates | of classifier | goodness |     | in binary | cases; | depending | on  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | -------- | --- | --------- | ------ | --------- | --- |
MOABBproject,wehaveunifiedtheaccesstomanydatasets,
described in Table I. things like the class balance, various other metrics have their
|             |                 |            |          |          |         |               |         | own benefits |           | and pitfalls. | Therefore |        | this must | also           | be fixed |
| ----------- | --------------- | ---------- | -------- | -------- | ------- | ------------- | ------- | ------------ | --------- | ------------- | --------- | ------ | --------- | -------------- | -------- |
| Adding      | new open-source |            | datasets |          | is also | simple        | via the |              |           |               |           |        |           |                |          |
|             |                 |            |          |          |         |               |         | across all   | datasets, | contingent    |           | on the | class     | of predictions | the      |
| MNE toolkit | [14,            | 15], which | is       | used for | all     | preprocessing | and     |              |           |               |           |        |           |                |          |
channel selection. Any dataset that can be made compatible pipelines attempt to make. We define this as our evaluation.
| with their | framework | can      | quickly      | be  | added       | to the | set of data |             |     |     |     |     |     |     |     |
| ---------- | --------- | -------- | ------------ | --- | ----------- | ------ | ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| offered    | by this   | project. | In addition, |     | the project |        | offers test | C. Pipeline |     |     |     |     |     |     |     |
functions to ensure candidate code conforms to the software We define a pipeline as the processing that takes one from
interface.
rawtrial-wisedataintolabels,takingbothspatialfilteringand
|     |     |     |     |     |     |     |     | classification |      | model fitting |     | into account. | A   | convenient | API        |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---- | ------------- | --- | ------------- | --- | ---------- | ---------- |
|     |     |     |     |     |     |     |     | for dealing    | with | this kind     | of  | processing    | is  | defined    | by scikit- |
B. Context
|           |     |         |                    |     |     |      |             | learn [24], | which   | allows      | for | easily definable |          | dimensionality |          |
| --------- | --- | ------- | ------------------ | --- | --- | ---- | ----------- | ----------- | ------- | ----------- | --- | ---------------- | -------- | -------------- | -------- |
| A context | is  | the set | of characteristics |     |     | that | defines the |             |         |             |     |                  |          |                |          |
|           |     |         |                    |     |     |      |             | reduction,  | feature | generation, |     | and model        | fitting. | To             | maximize |
preprocessingandvalidationprocedure.Togofromarecorded
reproducibilityweallowpipelinestobedefinedeitherbyyaml
| EEG time-series |     | to a pipeline |     | performance |     | value | for a given |          |         |        |       |               |     |              |     |
| --------------- | --- | ------------- | --- | ----------- | --- | ----- | ----------- | -------- | ------- | ------ | ----- | ------------- | --- | ------------ | --- |
|                 |     |               |     |             |     |       |             | files or | through | python | files | that generate |     | the objects, | but |
subjectorrecordingsession,manyparametersmustbedefined.
|               |      |       |         |        |            |     |            | force all | machine | learning | models | to  | follow | the scikit-learn |     |
| ------------- | ---- | ----- | ------- | ------ | ---------- | --- | ---------- | --------- | ------- | -------- | ------ | --- | ------ | ---------------- | --- |
| First, trials | need | to be | cut out | of the | continuous |     | signal and |           |         |          |        |     |        |                  |     |
interface.
pre-processed,whichispossibleinmanydifferentwayswhen
|                 |              |            |           |          |                |          |             | In essence, |               | the MOABB |             | combines    | the preceding |                 | compo-    |
| --------------- | ------------ | ---------- | --------- | -------- | -------------- | -------- | ----------- | ----------- | ------------- | --------- | ----------- | ----------- | ------------- | --------------- | --------- |
| taking into     | account      | parameters |           | such     | as trial       | overlap, | trial       |             |               |           |             |             |               |                 |           |
|                 |              |            |           |          |                |          |             | nents into  | a             | procedure | that        | takes a     | list of       | algorithms      | and       |
| length, imagery |              | type, and  | more.     | Once     | the continuous |          | data        | is          |               |           |             |             |               |                 |           |
|                 |              |            |           |          |                |          |             | datasets    | and trains    | each      | pipeline    | to each     | subject       | or              | recording |
| processed       | into trials, | and        | these     | trials   | are fed        | into     | a pipeline, |             |               |           |             |             |               |                 |           |
|                 |              |            |           |          |                |          |             | session     | independently |           | in order    | to generate |               | goodness-of-fit |           |
| the next        | question     | of how     | to create | training |                | and test | sets, and   |             |               |           |             |             |               |                 |           |
|                 |              |            |           |          |                |          |             | scores such | as            | accuracy  | or ROC-AUC. |             | These         | scores          | can then  |
howtoreportperformance,comesintoplay.Weseparatethese
|                |               |          |     |      |      |              |     | be visualized | and | used | for statistical | testing. |     |     |     |
| -------------- | ------------- | -------- | --- | ---- | ---- | ------------ | --- | ------------- | --- | ---- | --------------- | -------- | --- | --- | --- |
| two notions    | in our        | software | and | call | them | the paradigm | and |               |     |      |                 |          |     |     |     |
| the evaluation | respectively. |          |     |      |      |              |     |               |     |      |                 |          |     |     |     |
III. STATISTICALANALYSIS
| 1) Paradigm: |     | A paradigm | defines |     | how one | goes | from con- |     |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | ------- | --- | ------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
tinuous data to trials for a standard machine learning pipeline At the end of the MOABB procedure there are scores for
to deal with. While not an issue in image processing, as each every subject in every dataset with every pipeline. The goal
trial is just one image, it is crucial in EEG and biosignals of this project is to synthesize these numbers into an estimate
processingbecausemostdatasetsdonothaveexactlythesame of how likely it is that each pipeline out-performs the other
events defined in the continuous data. For example, many pipelines. However, even if imagery type and channel number
datasets with two-class motor imagery use left versus right were held constant, differences in trial amount, sampling rate,
hand, while some use hands versus feet; there are also many and even location and hardware mean that we cannot expect
possiblenon-motorimageries.Foranyreasonableanalysisthe subjects across datasets to be naively comparable. Therefore,
specific sort of imagery or ERP must be controlled for, as we run independent statistical tests within each dataset and
they all have different characteristics in the data and further combine the p-values afterwards. A secondary problem is that
are variably effective across subjects [2, 26]. After choosing the difference distribution for two algorithms within a given
which events or imageries are valid, the question comes to dataset is very unlikely to be Gaussian. It is well-known that

3
Name Imagery #Channels #Trials #Sessions #Subjects Epoch Citations
|     | Choetal.2017          |     |     |     | Right,lefthand |     | 64  | 200     |     | 1     | 49  | 0-3s   | [9]     |     |     |
| --- | --------------------- | --- | --- | --- | -------------- | --- | --- | ------- | --- | ----- | --- | ------ | ------- | --- | --- |
|     | Physionet             |     |     |     | Right,lefthand |     | 64  | 40-60   |     | 1 109 |     | 1-3s   | [13,25] |     |     |
|     | Shinetal.2017         |     |     |     | Right,lefthand |     | 25  | 60      |     | 3     | 29  | 0-10s  | [6,29]  |     |     |
|     | BNCI2014-001          |     |     |     | Right,lefthand |     | 22  | 144     |     | 2     | 9   | 2-6s   | [32]    |     |     |
|     | BNCI2014-002          |     |     |     | Righthand,feet |     | 15  | 160     |     | 1     | 14  | 3-8s   | [30]    |     |     |
|     | BNCI2014-004          |     |     |     | Right,lefthand |     | 3   | 120-160 |     | 5     | 9   | 3-7.5s | [20]    |     |     |
|     | BNCI2015-001          |     |     |     | Righthand,feet |     | 13  | 200     | 2/3 |       | 13  | 3-8s   | [11]    |     |     |
|     | BNCI2015-004          |     |     |     | Righthand,feet |     | 30  | 70-80   |     | 2     | 10  | 3-10s  | [26]    |     |     |
|     | AlexandreMotorImagery |     |     |     | Righthand,feet |     | 16  | 40      |     | 1     | 9   | 0-3s   | [3]     |     |     |
|     | Yietal.2014           |     |     |     | Right,lefthand |     | 60  | 160     |     | 1     | 10  | 3-7s   | [33]    |     |     |
|     | Zhouetal.2016         |     |     |     | Right,lefthand |     | 14  | 100     |     | 3     | 4   | 1-6s   | [35]    |     |     |
Grosse-Wentrupetal.2009 Right,lefthand 128 300 1 10 3-10s [16]
|     | Total: |     |     |     |     |       |     |                    |     | 275 |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | ----- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
|     |        |     |     |     |     | TABLE | I:  | Dataset attributes |     |     |     |     |     |     |     |
some subjects are BCI illiterate [2], which implies that no 2) Evaluation: The evaluation was chosen to be within-
pipeline can reliably out-predict another one on that subset of session, as that minimizes the effect of non-stationarity. As
subjects. Therefore, for large enough datasets, the distribution this is a binary classification task, the ROC-AUC score was
of differences in pipeline scores is very likely to be at least chosenasthemetrictoscore5-foldcrossvalidation(thesplits
bimodal. were kept identical for all pipelines in a given subject). In
To deal with this issue while also keeping the framework comparisonwiththemoreinterpretableclassificationaccuracy,
running fast enough to execute on a normal desktop, we use a the ROC-AUC is less sensitive to imbalanced classes, which
mixture of permutation and non-parametric tests. Within each is important in this case where the datasets vary heavily. In
dataset,eitheraone-tailedpermutation-basedpairedt-test(for ordertoreturnasinglescorepersubject,thescoresfromeach
datasetswithlessthan20subjects)oraWilcoxonsigned-rank session were averaged when multiple sessions were present.
| test is run | for each | pair | of pipelines, | generating |     | a p-value | for |     |     |     |     |     |     |     |     |
| ----------- | -------- | ---- | ------------- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thehypothesisthatpipelineaisbiggerthanpipelinebforeach
|                    |      |             |          |              |            |                |        | B. Pipelines |     |             |     |           |      |         |        |
| ------------------ | ---- | ----------- | -------- | ------------ | ---------- | -------------- | ------ | ------------ | --- | ----------- | --- | --------- | ---- | ------- | ------ |
| pair of pipelines. |      | These       | p-values | are combined |            | via Stouffer’s |        |              |     |             |     |           |      |         |        |
|                    |      |             |          |              |            |                |        | We implement |     | a selection | of  | pipelines | from | the BCI | liter- |
| method[31],        | with | a weighting |          | given by     | the square | root           | of the |              |     |             |     |           |      |         |        |
numberofsubjectsassuggestedin[7],toreturnafinalp-value ature, as well as the well-known standards of CSP + LDA
|          |             |       |     |            |             |     |         | and channel-level |     | variances | +   | SVM. | Specific | implemented |     |
| -------- | ----------- | ----- | --- | ---------- | ----------- | --- | ------- | ----------------- | --- | --------- | --- | ---- | -------- | ----------- | --- |
| for each | hypothesis. | Since |     | each score | is compared |     | against |                   |     |           |     |      |          |             |     |
N −1otherscoresforthesamesubject,wealsoapply pipelines are in Table II; all hyperparameters were set via
pipelines
| Bonferroni | correction |        | to protect | against     | false | positives.       | In  | cross-validation. |     |     |     |     |     |     |     |
| ---------- | ---------- | ------ | ---------- | ----------- | ----- | ---------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
| order to   | determine  | effect | size,      | we computed |       | the standardized |     |                   |     |     |     |     |     |     |     |
mean difference within datasets and combined them using the V. RESULTS
| same weighting |     | as was            | given      | to Stouffer’s | method.    |     |        |                 |         |                |          |            |               |         |        |
| -------------- | --- | ----------------- | ---------- | ------------- | ---------- | --- | ------ | --------------- | ------- | -------------- | -------- | ---------- | ------------- | ------- | ------ |
|                |     |                   |            |               |            |     |        | Figure          | 1 shows | all the        | results  | generated  |               | by this | entire |
|                |     |                   |            |               |            |     |        | processing      | chain.  | Surprisingly,  | perhaps, |            | the pipelines |         | do not |
|                |     | IV.               | EXPERIMENT |               |            |     |        |                 |         |                |          |            |               |         |        |
|                |     |                   |            |               |            |     |        | clearly cluster |         | on the dataset | level,   | making     | it            | unclear | which  |
| To show        | off | the possibilities |            | of this       | framework, |     | we ran |                 |         |                |          |            |               |         |        |
|                |     |                   |            |               |            |     |        | ones perform    | best    | from simply    |          | this plot. | What          | is very | clear, |
various well-known BCI pipelines from across many papers however, is that different datasets have very different average
| in order  | to conduct | the          | first big-data, | side-by-side  |     | analysis | of  |                    |     |              |      |     |              |      |      |
| --------- | ---------- | ------------ | --------------- | ------------- | --- | -------- | --- | ------------------ | --- | ------------ | ---- | --- | ------------ | ---- | ---- |
|           |            |              |                 |               |     |          |     | scores independent |     | of pipeline. | This | is  | particularly | true | when |
| the state | of the     | art in motor |                 | imagery BCIs. |     |          |     |                    |     |              |      |     |              |      |      |
oneconsidersthecaseof[35]versus[13]:Zhouetal[35]had
|     |     |     |     |     |     |     |     | pre-trained | subjects, | which | compared | to  | the naive | sample | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | ----- | -------- | --- | --------- | ------ | --- |
A. Context
|     |     |     |     |     |     |     |     | the Physionet |     | database makes | a   | drastic | difference. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------------- | --- | ------- | ----------- | --- | --- |
For the paradigm, we choose to look at datasets including Figure2showsthedifferencebetweenCSPandthechannel
|                |     |       |         |        |              |     |         | log-variance | and | tangent space | methods, |     | as these | are all | well- |
| -------------- | --- | ----- | ------- | ------ | ------------ | --- | ------- | ------------ | --- | ------------- | -------- | --- | -------- | ------- | ----- |
| motor imagery. |     | Motor | imagery | is the | most-studied |     | sort of |              |     |               |          |     |          |         |       |
imagery for BCIs [34], and we further limit ourselves to the knownapproachesandhavebeencomparedagainsteachother
binary case as this has not yet been solved. For evaluations, often in the past. Based on this meta-analysis, CSP reliably
we choose within-session cross-validation, as this represents out-performschannellog-variancesacrossdatasets–however,
the best-case scenario for any pipeline, with minimal non- there are datasets such as [16] and [26] in which the opposite
|     |     |     |     |     |     |     |     | trend is | shown. | Similarly, | while | the tangent | space | projection |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ---------- | ----- | ----------- | ----- | ---------- | --- |
stationarity.
1) Paradigm: As there are many methods that show that method normally out-performs CSP, that is also not true for
multiple frequency bands can lead to improved BCI perfor- half of the sampled datasets. The confidence intervals also
mance[18],andfurtherthatdiscriminativedataisconcentrated show why this is likely the case – for studies with very few
in the anatomical frequency bands, we test two preprocessing subjects,suchas[35],theconfidenceintervalsmakeevenvery
pipelines: A single bandpass containing both the alpha and strong standardized effects quite untrustworthy.
beta ranges, from 8−35Hz, and another from 8−35Hz in Figure 3 compares CSP against commonly used variants.
4Hz increments. All data was also subsampled to 128Hz, as Here, the difference is heavily dependent on dataset and no
the memory requirements became prohibitive otherwise. clear trend is visible. It is interesting to note that in the

4
| Name |     |     | Preprocessing |     |     |     |     | Classifier |     |     |     |     |     | Introducedin |     |
| ---- | --- | --- | ------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | ------------ | --- |
CSP+LDA Trialcovariancesestimatedviamaximum-likelihood LinearDiscriminantAnalysis(LDA) [19]
|     |     |     | with unregularized |          | common   | spatial patterns | (CSP).    |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------------------ | -------- | -------- | ---------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | Features           | were log | variance | of the filters   | belonging |     |     |     |     |     |     |     |     |
tothe6mostdivergingeigenvalues
DLCSPauto+shLDA TrialcovariancesestimatedbyOAS[8]followedby LDA with Ledoit-Wolf shrinkage of the covariance [22]
|     |     |     | unregularizedCSP.Featureswerelogvarianceonthe |     |     |     |     | term |     |     |     |     |     |     |     |
| --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
6topfilters.
TRCSP+LDA CSPwithTikhonovregularization,featureswerelog LDA [22]
varianceonthe3bestfiltersforeachclass
FBCSP+optSVM Filterbankof6bandsbetween8and35Hzfollowed A linear support vector machine was trained with [18]
by OAS covariance estimation and unregularized its regularization hyperparameter set by a cross-
|     |     |     | CSP.Logvariancefromeachofthe4topfiltersfrom |      |        |             |             | validatedgrid-searchfrom[0.01100]. |     |     |     |     |     |     |     |
| --- | --- | --- | ------------------------------------------- | ---- | ------ | ----------- | ----------- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | each sub-band                               | were | pooled | and the top | 10 features |                                    |     |     |     |     |     |     |     |
chosenbymutualinformationwereused.
TS+optSVM Trial covariances estimated via OAS then projected LinearSVMwithidenticalgrid-search [4]
intotheRiemanniantangentspacetoobtainfeatures
AM+optSVM Logvarianceineachchannel LinearSVMwithgrid-search N/A
|     |     |     |     |     |     | TABLE | II: Processing | pipelines |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | -------------- | --------- | --- | --- | --- | --- | --- | --- | --- |
case of filter-bank CSP, the BNCI 2014 datasets (which are better than CSP or Riemannian methods, and that the tangent
included in the BCI Competition datasets used in [18]) show space classification pipeline is the best of the tested models
FBCSP to out-perform regular CSP while the opposite is true for single-session classification.
| for others | such              | as Physionet. |               | We further | confirm   | the           | result |               |           |        |       |             |     |           |             |
| ---------- | ----------------- | ------------- | ------------- | ---------- | --------- | ------------- | ------ | ------------- | --------- | ------ | ----- | ----------- | --- | --------- | ----------- |
|            |                   |               |               |            |           |               |        | In particular |           | in the | cases | of FBCSP    |     | and the   | regularized |
| from [22]  | that regularizing |               | the           | covariance | estimates | does          | not    |               |           |        |       |             |     |           |             |
|            |                   |               |               |            |           |               |        | approaches    | presented |        | here, | the results |     | presented | here are    |
| improve    | the results       | of            | CSP. However, |            | somewhat  | surprisingly, |        |               |           |        |       |             |     |           |             |
surprisingfindingastheygoagainsttheresultsreportedinthe
| the finding  | that         | Tikhonov | weighting |                 | increases | performance  |       |                |         |        |             |              |          |          |           |
| ------------ | ------------ | -------- | --------- | --------------- | --------- | ------------ | ----- | -------------- | ------- | ------ | ----------- | ------------ | -------- | -------- | --------- |
|              |              |          |           |                 |           |              |       | original       | papers. | In the | case of     | FBCSP,       | we       | perform  | similarly |
| was not      | validated    | in this  | analysis. |                 |           |              |       |                |         |        |             |              |          |          |           |
|              |              |          |           |                 |           |              |       | to the results | shown   | in     | [18].       | BNCI         | 2014-001 | and      | 2014-004  |
| The          | meta-effects | shown    | in        | Figures         | 2 and     | 3 are summed |       |                |         |        |             |              |          |          |           |
|              |              |          |           |                 |           |              |       | are originally | from    | the    | BCI         | competitions |          | and were | used in   |
| up in Figure | 4,           | which    | displays  | the meta-effect |           | size in      | cases |                |         |        |             |              |          |          |           |
|              |              |          |           |                 |           |              |       | the original   | paper,  | and    | our finding |              | is that  | on these | datasets  |
thatthealgorithmonthey-axissignificantlyout-performedthe
|              |            |               |             |              |              |           |          | FBCSP       | indeed out-performed |               |     | regular      | CSP.    | In the  | case of the |
| ------------ | ---------- | ------------- | ----------- | ------------ | ------------ | --------- | -------- | ----------- | -------------------- | ------------- | --- | ------------ | ------- | ------- | ----------- |
| algorithm    | on the     | x-axis        | according   | to the       | statistical  | procedure |          |             |                      |               |     |              |         |         |             |
|              |            |               |             |              |              |           |          | regularized | variants             | DLCSPauto     |     | and          | TRCSP,  | our     | results on  |
| outlined     | in Section | III,          | as well     | as the       | significance |           | denoted  |             |                      |               |     |              |         |         |             |
|              |            |               |             |              |              |           |          | the BCI     | competition          | data          | do  | not actually | follow  | the     | originally  |
| by the stars | under      | the           | meta-effect | size.        | Here         | we can    | see that |             |                      |               |     |              |         |         |             |
|              |            |               |             |              |              |           |          | reported    | trend.               | Some possible |     | for          | reasons | are the | following:  |
| all other    | algorithms | out-performed |             | log-variance |              | features  | on       |             |                      |               |     |              |         |         |             |
ouruseofsingle-sessionrecordingsignorestheinitialtraining
average(thoughwithsignificantvarianceoverdatasetsasseen
andtestdistinctionsgivenwithinthecompetition,andwealso
| in the other | figures)         |        | and that     | among     | CSP | and its variants, |     |                |             |         |          |              |              |          |            |
| ------------ | ---------------- | ------ | ------------ | --------- | --- | ----------------- | --- | -------------- | ----------- | ------- | -------- | ------------ | ------------ | -------- | ---------- |
|              |                  |        |              |           |     |                   |     | used the       | AUC-ROC     | instead | of       | the accuracy |              | that was | reported   |
| tangent      | space projection |        | is better.   |           |     |                   |     |                |             |         |          |              |              |          |            |
|              |                  |        |              |           |     |                   |     | in the initial | analysis.   |         | The full | code         | to replicate | these    | results    |
|              |                  |        |              |           |     |                   |     | is available   | publically, |         | and so   | we           | hope we      | can at   | least rule |
|              |                  | VI.    | DISCUSSION   |           |     |                   |     |                |             |         |          |              |              |          |            |
|              |                  |        |              |           |     |                   |     | out improper   | coding      | as      | a source | of           | error.       |          |            |
| We present   | a                | system | for reliably | comparing |     | BCI pipelines     |     |                |             |         |          |              |              |          |            |
that is both easily extended to incorporate new datasets and Looking at these findings, it is particularly interesting to
equippedwithanautomatedstatisticalprocedurefordetermin- look at the case of filter-bank CSP versus CSP, as in this
ing which pipelines perform best. Furthermore, this system analysis the significance goes in both directions depending on
defines a simple interface for submitting and validating new the dataset. Since datasets vary in many characteristics, such
BCI pipelines, which could serve to unify the many methods as channel number, imagery type, and trial time, it is hard to
that exist so far. To test that system, we present results using determine what exactly underlies this diverging performance
standard pipelines in contexts that have wide relevance to the – but it is likely that this is not purely by chance. With
BCI community. By looking across multiple, large datasets, it increasingnumbersofavailabledatasets,however,theanswers
is possible to make statements about how BCIs perform on tosuchdifferencesbecomepossible.Ifwehavemanydifferent
average, without any sort of expert tuning of the processing situations in which to test algorithms, we can determine what
chain, and further to see where the major pitfalls still lie. factors contribute to the differences in performance between
The results of this analysis suggest that many well-known them. It is also important to emphasize that the results shown
methods do not reliably out-perform simpler ones, despite here must be taken in context. All results were generated by
the small-scale studies done years ago to validate them. In cross-validationwithin single recordingsessions, whichlimits
particular, the world of CSP regularization literature does not the possible non-stationarity. Because of this, regularization is
appear to have the effect that was originally claimed. Rather, atitsleastuseful–whichmeansthatitwouldbeinappropriate
the major difference in BCI classification isn’t actually the to dismiss regularization in the case of CSP out of hand.
algorithm, as of now, but the recording and human paradigm Rather, this same analysis should be re-run in the case of
characteristics.Thetwomostclearfindingstocomeoutofthis cross-session classification, a task that is currently infeasible
are that log variances on the channel level are almost never due to the number of multi-session datasets.

5
001-2014
001-2015
002-2014
004-2014
004-2015
Alexandre
Cho2017
Grosse-Wentrup
Physionet
Shin2017A
Weibo 2014
Zhou 2016
0.0 0.2 0.4 0.6 0.8 1.0
score
tesatad
Scores per dataset and algorithm
pipeline
AM + optSVM
CSP + LDA
DLCSPauto + shLDA
FBCSP + optSVM
TRCSP + LDA
TS + optSVM
Fig. 1: Visualization of all generated scores, across all datasets. The dotted line corresponds to a chance level performance of
0.5

| REFERENCES |     |     |     |     |     |     |     |     |     |     |     |     | 6   |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
< AM + optSVM better                                   < TS + optSVM better
                                    CSP + LDA better >                                     CSP + LDA better >
|     |                |     |                              |     |     |     | p-value  |                |     |                              |         |             | p-value  |
| --- | -------------- | --- | ---------------------------- | --- | --- | --- | -------- | -------------- | --- | ---------------------------- | ------- | ----------- | -------- |
|     | Zhou 2016      |     |                              |     |     |     |          | Zhou 2016      |     |                              |         |             |          |
|     | Weibo 2014     |     |                              |     |     |     | 9.77e-04 | Weibo 2014     |     |                              |         |             |          |
|     | Shin2017A      |     |                              |     |     |     | 1.65e-04 | Shin2017A      |     |                              |         |             |          |
|     |                |     |                              |     |     |     | 1.92e-08 |                |     |                              |         |             | 2.42e-08 |
|     | Physionet      |     |                              |     |     |     |          | Physionet      |     |                              |         |             |          |
|     | Grosse-Wentrup |     |                              |     |     |     |          | Grosse-Wentrup |     |                              |         |             | 9.77e-04 |
|     | Cho2017        |     |                              |     |     |     | 2.32e-05 | Cho2017        |     |                              |         |             | 7.53e-05 |
|     | Alexandre      |     |                              |     |     |     | 3.12e-02 | Alexandre      |     |                              |         |             |          |
|     | 004-2015       |     |                              |     |     |     |          | 004-2015       |     |                              |         |             | 3.52e-02 |
|     | 004-2014       |     |                              |     |     |     | 2.15e-02 | 004-2014       |     |                              |         |             |          |
|     | 002-2014       |     |                              |     |     |     | 6.00e-04 | 002-2014       |     |                              |         |             |          |
|     | 001-2015       |     |                              |     |     |     | 4.88e-04 | 001-2015       |     |                              |         |             | 7.81e-03 |
|     | 001-2014       |     |                              |     |     |     | 3.91e-03 | 001-2014       |     |                              |         |             |          |
|     | Meta-effect    |     |                              |     |     |     | 3.58e-21 | Meta-effect    |     |                              |         |             | 8.57e-13 |
|     |                | 2   | 1                            | 0   | 1   | 2   |          |                | 2.0 | 1.5 1.0                      | 0.5 0.0 | 0.5 1.0 1.5 | 2.0      |
|     |                |     | Standardized Mean Difference |     |     |     |          |                |     | Standardized Mean Difference |         |             |          |
Fig. 2: Meta-analysis style plots showing the performance of log variance features (A) and tangent space features (B) both
compared against CSP. The effect sizes shown are standardized mean differences, with p-values corresponding to the one-
tailed Wilcoxon signed-rank test for the hypothesis given at the top of the plot and 95% interval denoted by the grey bar.
Stars correspond to ***=p<0.001, **=p<0.01, *=p<0.05. The meta-effect is shown at the bottom of the plot. While there is a
significant amount of variance between datasets–variance that could give contradictory results if these datasets were evaluated
in isolation–the overall trend shows that CSP is on average better than channel log-variances and worse than tangent space
projection.
< DLCSPauto + shLDA better                             < TRCSP + LDA better                                   < FBCSP + optSVM better
                                    CSP + LDA better > p-value                                     CSP + LDA better > p-value                                     CSP + LDA better > p-value
|                | Zhou 2016  |     |     |     |          | Zhou 2016      |     |     |          | Zhou 2016      |     |     |          |
| -------------- | ---------- | --- | --- | --- | -------- | -------------- | --- | --- | -------- | -------------- | --- | --- | -------- |
|                | Weibo 2014 |     |     |     | 6.84e-03 | Weibo 2014     |     |     | 9.77e-04 | Weibo 2014     |     |     |          |
|                | Shin2017A  |     |     |     |          | Shin2017A      |     |     | 3.22e-02 | Shin2017A      |     |     | 8.18e-03 |
|                | Physionet  |     |     |     |          | Physionet      |     |     |          | Physionet      |     |     | 1.82e-04 |
| Grosse-Wentrup |            |     |     |     |          | Grosse-Wentrup |     |     |          | Grosse-Wentrup |     |     | 5.86e-03 |
|                | Cho2017    |     |     |     |          | Cho2017        |     |     |          | Cho2017        |     |     | 1.93e-02 |
|                | Alexandre  |     |     |     |          | Alexandre      |     |     |          | Alexandre      |     |     |          |
|                | 004-2015   |     |     |     |          | 004-2015       |     |     |          | 004-2015       |     |     |          |
|                | 004-2014   |     |     |     |          | 004-2014       |     |     |          | 004-2014       |     |     |          |
|                | 002-2014   |     |     |     |          | 002-2014       |     |     | 3.34e-02 | 002-2014       |     |     |          |
|                | 001-2015   |     |     |     |          | 001-2015       |     |     | 2.44e-04 | 001-2015       |     |     | 6.35e-03 |
|                | 001-2014   |     |     |     | 4.69e-02 | 001-2014       |     |     | 1.95e-03 | 001-2014       |     |     |          |
Meta-effect 4.85e-02 Meta-effect 3.02e-02 Meta-effect 2.59e-03
1.5 1.0 0.5 0.0 0.5 1.0 1.5 2.0 1.5 1.0 0.5 0.0 0.5 1.0 1.5 2.0 1.5 1.0 0.5 0.0 0.5 1.0 1.5
Standardized Mean Difference Standardized Mean Difference Standardized Mean Difference
Fig. 3: Meta-analysis style plots showing the performance of CSP versus CSP variants: DLCSPauto(A), TRCSP (B), and
filter-bank CSP (C). The effect sizes shown are standardized mean differences, with p-values corresponding to the one-tailed
Wilcoxon signed-rank test for the hypothesis given at the top of the plot and 95% interval denoted by the grey bar. Stars
correspond to ***=p<0.001, **=p<0.01, *=p<0.05. The meta-effect is shown at the bottom of the plot. While there is a
significant amount of variance between datasets–variance that could give contradictory results if these datasets were evaluated
in isolation–the overall trend shows that CSP out-performs the other algorithms in this setting.
VII. CONCLUSION a system for testing algorithms, we hope that this platform in
|        |               |            |                |     |         |          |            | the coming | years | can help | to solve | it. |     |
| ------ | ------------- | ---------- | -------------- | --- | ------- | -------- | ---------- | ---------- | ----- | -------- | -------- | --- | --- |
|        | Meta-analysis | is a       | well-described |     | tool    | in other | scientific |            |       |          |          |     |     |
| fields | to            | attempt to | synthesize     | the | effects | of many  | different  |            |       |          |          |     |     |
ACKNOWLEDGEMENTS
| studies | that | all bear | on the | same, | or very | similar | hypotheses. |     |     |     |     |     |     |
| ------- | ---- | -------- | ------ | ----- | ------- | ------- | ----------- | --- | --- | --- | --- | --- | --- |
Though its use in BCIs has been hampered by the difficulties We would like to extend our thanks to Dr. Marco Congedo
involvedingatheringthedataandalgorithmsinasingleplace,
|     |     |     |     |     |     |     |     | for his | valuable | input regarding |     | the appropriate | statistical |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | --------------- | --- | --------------- | ----------- |
the MOABB project has the potential to offer a solution to procedure for this analysis, and also to the NeuroTechX
| this      | problem. | The analysis         |            | here, | though | done with | over 250    |           |             |     |          |                  |     |
| --------- | -------- | -------------------- | ---------- | ----- | ------ | --------- | ----------- | --------- | ----------- | --- | -------- | ---------------- | --- |
|           |          |                      |            |       |        |           |             | community | for helping | to  | get this | project started. |     |
| subjects, |          | is still only        | a fraction |       | of the | number    | of subjects |           |             |     |          |                  |     |
| recorded  |          | for BCI publications |            | over  | the    | years.    | With more   |           |             |     |          |                  |     |
papers that describe more varied setups, the power of this correspondingauthor:VinayJayaram(email:vjayaram@tue.mpg.de)
| system  | can   | only grow,      | and  | what      | this analysis |      | shows most     |     |     |     |     |     |     |
| ------- | ----- | --------------- | ---- | --------- | ------------- | ---- | -------------- | --- | --- | --- | --- | --- | --- |
| clearly | is    | that the sample | size | problem   | in            | BCIs | is bigger than |     |     |     |     |     |     |
| we      | might | have expected.  | By   | gathering | the           | data | and offering   |     |     |     |     |     |     |

REFERENCES 7
Algorithm comparison
AM + optSVM
0.76 0.17 0.03 0.32
CSP + LDA
p=4e-21 p=5e-02 p=3e-03 p=3e-02
0.72 0.20
DLCSPauto + shLDA
p=6e-21 p=2e-01
0.63 0.06 0.11
FBCSP + optSVM
p=2e-13 p=1e+00 p=1e+00
0.53
TRCSP + LDA
p=3e-19
1.32 0.46 0.54 0.54 0.72
TS + optSVM
p=3e-42 p=9e-13 p=2e-16 p=2e-19 p=9e-19
M A o P P S
A L D a u t C S C S T
+ S P F B T R
P C
S L
C D
Fig. 4: Ranking of algorithms in performance across all datasets with statistics generated as defined in section III. As all
p-values are single-sided, in the case that the effect goes in the opposite direction of the hypothesis the values are removed
for clarity. The values correspond to the standardized mean difference of the algorithm in the y-axis minus that in the x-axis
and the associated p-value
REFERENCES [5] BBlankertzetal.“TheBCICompetitionIII:Validating
[1] Martn Abadi et al. Tensorflow: Large-scale machine Alternative Approaches to Actual BCI Problems”. In:
IEEE Transactions on Neural Systems and Rehabilita-
learning on heterogeneous distributed systems. 2016.
tion Engineering 14.2 (2006), pp. 153–159.
URL: https://www.tensorflow.org/.
[6] B Blankertz, G Dornhege, M Krauledat, K R Mu¨ller,
[2] Brendan Allison et al. “BCI demographics: How many
andGCurio.“Thenon-invasiveBerlinBrain-Computer
(andwhatkindsof)peoplecanuseanSSVEPBCI?”In:
Neural Systems and Rehabilitation Engineering, IEEE Interface: Fast acquisition of effective performance
Transactions on 18.2 (2010), pp. 107–116. in untrained subjects”. In: NeuroImage 37.2 (2007),
pp. 539–550.
[3] Alexandre Barachant. “Commande robuste d’un ef-
[7] L Bovino et al. “On the combination of”. In: Analysis
fecteur par une interface cerveau machine EEG asyn-
5.33 (2003), pp. 42–54.
chrone”. In: (2012). URL: https://tel.archives-ouvertes.
[8] Yilun Chen, Ami Wiesel, Yonina C. Eldar, and Al-
fr/tel-01196752/.
fred O. Hero. “Shrinkage Algorithms for MMSE Co-
[4] Alexandre Barachant, Ste´phane Bonnet, Marco Con-
variance Estimation”. In: IEEE Transactions on Signal
gedo,andChristianJutten.“Classificationofcovariance
matrices using a Riemannian-based kernel for BCI
Processing 58.10 (2010), pp. 5016–5029. ISSN: 1053-
applications”.In:Neurocomputing112(2013),pp.172– 587X. DOI: 10.1109/TSP.2010.2053029. URL: http:
//ieeexplore.ieee.org/document/5484583/.
178. ISSN:0925-2312. DOI:10.1016/J.NEUCOM.2012.
[9] Hohyun Cho, Minkyu Ahn, Sangtae Ahn, Moonyoung
12.039. URL: https://www.sciencedirect.com/science/
Kwon, and Sung Chan Jun. “EEG datasets for motor
article/pii/S0925231213001574.

REFERENCES 8
imagerybrain-computerinterface”.In:GigaScience6.7 6. DOI: 10.1109/IJCNN.2008.4634130. URL: http:
(2017), pp. 1–8. ISSN: 2047-217X. DOI: 10.1093/ //ieeexplore.ieee.org/document/4634130/.
gigascience/gix034. URL: http://academic.oup.com/ [19] Zoltan J Koles, Michael S Lazar, and Steven Z Zhou.
gigascience/article/6/7/1/3796323/EEG-datasets-for- “Spatial patterns underlying population differences in
motor-imagery-braincomputer. thebackgroundEEG”.In:BrainTopography2.4(1990),
[10] Jia Deng et al. “Imagenet: A large-scale hierarchical pp. 275–284.
image database”. In: Computer Vision and Pattern [20] R. Leeb et al. “Brain-Computer Communication: Moti-
Recognition, 2009. CVPR 2009. IEEE Conference on. vation, Aim, and Impact of Exploring a Virtual Apart-
2009, pp. 248–255. ment”. In: IEEE Transactions on Neural Systems and
[11] J.Faller,C.Vidaurre,T.Solis-Escalante,C.Neuper,and Rehabilitation Engineering 15.4 (2007), pp. 473–482.
R. Scherer. “Autocalibration and Recurrent Adaptation: ISSN: 1534-4320. DOI: 10.1109/TNSRE.2007.906956.
Towards a Plug and Play Online ERD-BCI”. In: IEEE URL: http://ieeexplore.ieee.org/document/4359220/.
TransactionsonNeuralSystemsandRehabilitationEn- [21] Miguel Angel Lopez-Gordo, Daniel Sanchez-Morillo,
gineering 20.3 (2012), pp. 313–319. ISSN: 1534-4320. and F Pelayo Valle. “Dry EEG electrodes”. In: Sensors
DOI: 10.1109/TNSRE.2012.2189584. URL: http:// 14.7 (2014), pp. 12847–12870.
ieeexplore.ieee.org/document/6177271/. [22] F Lotte and C Guan. “Regularizing common spatial
[12] D. Garrett, D.A. A Peterson, C.W. W Anderson, and patterns to improve BCI designs: unified theory and
M.H. H Thaut. “Comparison of linear, nonlinear, and new algorithms”. In: IEEE Transactions on Biomedical
featureselectionmethodsforEEGsignalclassification”. Engineering 58.2 (2011), pp. 355–362.
In: IEEE Transactions on Neural Systems and Reha- [23] Adam Paszke et al. Automatic differentiation in Py-
bilitation Engineering 11.2 (2003), pp. 141–144. ISSN: Torch. 2017. URL: https://openreview.net/forum?id=
1534-4320. DOI: 10.1109/TNSRE.2003.814441. URL: BJJsrmfCZ.
http://ieeexplore.ieee.org/document/1214704/. [24] FabianPedregosaetal.“Scikit-learn:MachineLearning
[13] Ary L Goldberger et al. “PhysioBank, PhysioToolkit, in Python”. In: Journal of Machine Learning Research
and PhysioNet”. In: Circulation 101.23 (2000), e215 12.Oct (2011), pp. 2825–2830. ISSN: ISSN 1533-7928.
LP –e220. URL: http://circ.ahajournals.org/content/101/ URL: http://jmlr.csail.mit.edu/papers/v12/pedregosa11a.
23/e215.abstract. html.
[14] AlexandreGramfortetal.“MEGandEEGdataanalysis [25] G. Schalk, D.J. McFarland, T. Hinterberger, N. Bir-
with MNE-Python”. In: Frontiers in Neuroscience 7 baumer, and J.R. Wolpaw. “BCI2000: A General-
(2013), p. 267. ISSN: 1662453X. DOI: 10.3389/fnins. Purpose Brain-Computer Interface (BCI) System”. In:
2013.00267. URL: http://journal.frontiersin.org/article/ IEEE Transactions on Biomedical Engineering 51.6
10.3389/fnins.2013.00267/abstract. (2004),pp.1034–1043.ISSN:0018-9294.DOI:10.1109/
[15] Alexandre Gramfort et al. “MNE software for pro- TBME.2004.827072. URL: http://www.ncbi.nlm.
cessing MEG and EEG data”. In: NeuroImage 86 nih.gov/pubmed/15188875http://ieeexplore.ieee.org/
(2014), pp. 446–460. ISSN: 10538119. DOI: 10.1016/ document/1300799/.
j.neuroimage.2013.10.027. URL: http://www. [26] Reinhold Scherer et al. “Individually Adapted Im-
ncbi.nlm.nih.gov/pubmed/24161808http://www. agery Improves Brain-Computer Interface Performance
pubmedcentral . nih . gov / articlerender. fcgi ? artid = in End-Users with Disability”. In: PLOS ONE 10.5
PMC3930851http://linkinghub.elsevier.com/retrieve/ (2015). Ed. by Luigi Bianchi, e0123727. ISSN: 1932-
pii/S1053811913010501. 6203. DOI: 10.1371/journal.pone.0123727. URL: http:
[16] M. Grosse-Wentrup, C. Liefhold, K. Gramann, and //dx.plos.org/10.1371/journal.pone.0123727.
M.Buss.“BeamforminginNoninvasiveBrainComputer [27] A Schloegl. Results of the BCI Competition 2005 for
Interfaces”.In:IEEETransactionsonBiomedicalEngi- data set IIIa and IIIb. Tech. rep. Institute for Human-
neering 56.4 (2009), pp. 1209–1219. ISSN: 0018-9294. Computer Interfaces - BCI Lab, University of Technol-
DOI: 10.1109/TBME.2008.2009768. URL: http:// ogy Graz, Austria, 2005.
ieeexplore.ieee.org/document/4694120/. [28] A Searle and L Kirkup. “A direct comparison of wet,
[17] VinayJayaram,MortezaAlamgir,YaseminAltun,Bern- dry and insulating bioelectric recording electrodes”. In:
hard Scho¨lkopf, and Moritz Grosse-Wentrup. “Transfer Physiological measurement 21.2 (2000), p. 271.
Learning in Brain-Computer Interfaces”. In: Computa- [29] Jaeyoung Shin et al. “Open Access Dataset for
tionalIntelligenceMagazine,IEEE11.1(2016),pp.20– EEG+NIRS Single-Trial Classification”. In: IEEE
31. TransactionsonNeuralSystemsandRehabilitationEn-
[18] Kai Keng Ang, Zhang Yang Chin, Haihong Zhang, gineering 25.10 (2017), pp. 1735–1745. ISSN: 1534-
andCuntaiGuan.“FilterBankCommonSpatialPattern 4320. DOI: 10.1109/TNSRE.2016.2628057. URL: http:
(FBCSP) in Brain-Computer Interface”. In: 2008 IEEE //ieeexplore.ieee.org/document/7742400/.
International Joint Conference on Neural Networks [30] DavidSteyrl,ReinholdScherer,JosefFaller,andGernot
(IEEE World Congress on Computational Intelligence). R. Mu¨ller-Putz. “Random forests in non-invasive sen-
IEEE, 2008, pp. 2390–2397. ISBN: 978-1-4244-1820- sorimotor rhythm brain-computer interfaces: a practical
and convenient non-linear classifier”. In: Biomedical

9
Engineering 61.1 (2016), pp. 77–86. ISSN: 1862-278X.
DOI: 10.1515/bmt-2014-0117. URL: http://www.
degruyter.com/view/j/bmte.2016.61.issue-1/bmt-
2014-0117/bmt-2014-0117.xml.
[31] Samuel A. Stouffer, Edward A. Suchman, Leland C.
Devinney, Shirley A. Star, and Robin M. Williams Jr.
The American soldier: Adjustment during army life.
(Studies in social psychology in World War II). Oxford,
England: Princeton University Press, 1949. URL: http:
//psycnet.apa.org/record/1950-00790-000.
[32] MichaelTangermannetal.“ReviewoftheBCICompe-
titionIV”.In:FrontiersinNeuroscience6(2012),p.55.
ISSN:1662-4548.DOI:10.3389/fnins.2012.00055.URL:
http://journal.frontiersin.org/article/10.3389/fnins.2012.
00055/abstract.
[33] WeiboYietal.“EvaluationofEEGOscillatoryPatterns
and Cognitive Process during Simple and Compound
Limb Motor Imagery”. In: PLoS ONE 9.12 (2014).
Ed.byNatashaM.Maurits,e114853. ISSN:1932-6203.
DOI: 10.1371/journal.pone.0114853. URL: http://dx.
plos.org/10.1371/journal.pone.0114853.
[34] Han Yuan and Bin He. “Brain-computer interfaces
using sensorimotor rhythms: current state and future
perspectives.” In: IEEE Transactions on Biomedical
Engineering 61.5 (2014), pp. 1425–35. ISSN: 1558-
2531. DOI: 10.1109/TBME.2014.2312397. URL: http:
//www.ncbi.nlm.nih.gov/pubmed/24759276http://
www.pubmedcentral.nih.gov/articlerender.fcgi?artid=
PMC4082720.
[35] Bangyan Zhou, Xiaopei Wu, Zhao Lv, Lei Zhang,
and Xiaojin Guo. “A Fully Automated Trial Selection
Method for Optimization of Motor Imagery Based
Brain-ComputerInterface”.In:PLOSONE11.9(2016).
Ed. by Bin He, e0162657. ISSN: 1932-6203. DOI: 10.
1371/journal.pone.0162657. URL: http://dx.plos.org/10.
1371/journal.pone.0162657.