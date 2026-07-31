BrainWave: A Brain Signal Foundation Model for
Clinical Applications
Zhizhang Yuan1, Fanqi Shen1, Meng Li2,3, Yuguo Yu4,5, Fei Wu1,
Chenhao Tan6, Yang Yang1*
1Computer Science and Technology, Zhejiang University, Hangzhou,
Zhejiang, China.
2Shanghai Institute of Microsystem and Information Technology,
Chinese Academy of Sciences, Shanghai, China.
3INSIDE Institute for Biological and Artificial Intelligence, Street,
Shanghai, China.
4Research Institute of Intelligent and Complex Systems, State Key
Laboratory of Medical Neurobiology and MOE Frontiers Center for
Brain Science, and Institute of Science and Technology for
Brain-Inspired Intelligence, Fudan University, Shanghai, China.
5Shanghai Artificial Intelligence Laboratory, Fudan University,
Shanghai, China.
6University of Chicago, Chicago, Illinois, USA.
*Corresponding author(s). E-mail(s): yangya@zju.edu.cn;
Contributing authors: zhizhangyuan@zju.edu.cn; fanqishen@zju.edu.cn;
li.meng@mail.sim.ac.cn; yuyuguo@fudan.edu.cn; wufei@zju.edu.cn;
chenhao@uchicago.edu;
Abstract
Neural electrical activity is fundamental to brain function, and abnormal pat-
ternsofneuralsignalingoftenindicatethepresenceofunderlyingbraindiseases.
The variability among individuals, the diverse array of clinical symptoms from
various brain disorders, and the limited availability of diagnostic classifications,
have posed significant barriers to formulating reliable models of neural signals
for diverse application contexts. Here, we present BrainWave, the first founda-
tion model for both invasive and non-invasive neural recordings, pretrained on
more than 40,000 hours of electrical brain recordings (13.79 TB of data) from
1
5202
peS
1
]CN.oib-q[
7v15201.2042:viXra

| approximately   | 16,000 individuals.  |              | Our         | analysis  | show                  | that     | BrainWave      | consis-        |
| --------------- | -------------------- | ------------ | ----------- | --------- | --------------------- | -------- | -------------- | -------------- |
| tently achieves | state-of-the-art     |              | performance |           | in the identification |          | of             | neurological   |
| disorders       | across various       | experimental |             | settings. | In addition,          |          | we demonstrate | the            |
| effectiveness   | of pretraining,      | as           | BrainWave   | achieves  | strong                | few-shot |                | classification |
| performance     | without fine-tuning, |              | indicating  |           | our pretraining       |          | strategy       | extracts       |
| informative     | representations      | from         | neural      | signals.  | BrainWave             |          | is also        | evaluated in   |
real-worldclinicalscenarios,highlightingitspotentialinfacilitatingclinicalinter-
| pretation       | and decision-making. |                | We hence | believe      | that       | open-sourcing |        | BrainWave |
| --------------- | -------------------- | -------------- | -------- | ------------ | ---------- | ------------- | ------ | --------- |
| will facilitate | a wide range         | of             | clinical | applications | in         | medicine,     | paving | the way   |
| for AI-driven   | approaches           | to investigate |          | brain        | disorders. |               |        |           |
Keywords:foundationmodel,brainsignals,EEG,iEEG
1 Introduction
Electrical brain recordings, capturing the intricate patterns of the brain’s electri-
cal activities, are essential in advancing our understanding of brain across scientific
domains [1–7]. In particular, they can be used to identify medical conditions and
diagnose neurological disorders, and are thus essential for addressing major global
health challenges in developing nations [8, 9]. Scalp electroencephalography (EEG)
and intracranial electroencephalography (iEEG) are two primary methods to conduct
these types of recordings. EEG is non-invasive and economical viable, and has thus
been used in diverse applications [10–14]. In contrast, iEEG offers high signal fidelity
and spatial resolution [15], but the invasive nature limits its applicability to only the
mostseverepatientcasesandrestrictedscenarios.DuetothedistinctfeaturesofEEG
and iEEG data, such as different acquisition rates and notable variations in channel
numbers[16–18],studieshavesofarinvestigatedthemseparately.Wehypothesizethat
combining EEG and iEEG data can offer information that are not only rich in detail
but also highly generalizable across diverse neural electrical activities, and develop a
pioneeringfoundationalmodel,BrainWave,forbothEEGandiEEGdata.BrainWave
learnsrobustrepresentationsthatachievestate-of-the-artperformanceinawiderange
of tasks, demonstrating the synergy of EEG and iEEG data for the first time.
BrainWaveovercomesasuiteofinherentchallengesinconventionalsupervisedarti-
ficial intelligence (AI) models used for the analysis of brain signals. First, BrainWave
leverages self-supervised training, circumventing the need for large-scale, high-quality
manuallabeling.Inclinicalapplications,theprocessofbraindataannotationislabor-
intensive and reliant on specialized expertise [19–21], exemplified by the need for
multi-day monitoring for epilepsy patients [22] and the clinical experts’ capacity to
annotate only tens of seconds of data in a single work period. Second, BrainWave
provides much-need generalization at two levels that were not possible in supervised
training,whichrequiresanunderstandingoffundamentalandgeneralpatternsinbrain
signals.Individualvariabilityinbrainneuralactivities,aconsequenceofeachperson’s
distinctbrainstructureandfunctionalbehaviors[23],leadstomarkedlydifferentbrain
recording patterns [24]. This diversity hinders the generalizability of supervised AI
2

models, as they often struggle to extend the insights gained from a subset of patients
to a broader population, due to significant differences across individuals, as well as
variabilitythatchangeswithdifferentbehavioralstates.Moreover,therearenumerous
typesofbrain-relateddiseaseswithvariousunderlyingmechanisms [25–28],andeven
a single disease may present with multiple subtypes [29]. Supervised AI models are
task-specificandfailtoaddressadiverserangeoftasksusingbrainsignals[24,30–37].
While prior work has attempted to build foundation models for brain signals [38–
43], BrainWave offered unique technical contributions by building the largest dataset
of electrical brain recordings and developing novel techniques to integrate EEG and
iEEG data for the first time. As illustrated in Figure 1a, we collected a total of 13.79
TB of combined EEG and iEEG data over a duration of 40,907 hours, which serves
as the foundation for pretraining BrainWave. The data were obtained from 15,997
individuals,includingbothhealthyindividualsandthosewithvariousbraindisorders,
spanninganagerangefrominfancy(<1year)toover90yearsold.Thesamplingrates
vary across different brain signal datasets, with a more pronounced disparity between
EEGandiEEGdata,whichincreasesthedifficultyofunifiedmodeling.Previousworks
generally focused on modeling either EEG or iEEG alone, so they often uniformly
resampledthedatatoacommonsamplingrate[44–46].Weproposedascalealignment
layer that adapts to arbitrary temporal resolutions without the need for resampling,
thereby improving data scalability and enhancing generalization capabilities. In the
pretraining stage, we adopt a masked modeling strategy that reconstructs the time-
frequencyrepresentationsofthemaskedpatches(Fig.1b).Wealsoemployedachannel
count-agnostic approach to capture the inter-channel relationships. Empowered by
growing datasets and advances in model design, BrainWave exhibited highly robust
pretrained representations and excellent transfer learning capabilities (Fig. 1c).
TocomprehensivelyassessthecapabilitiesofBrainWaveasafoundationmodelfor
electricalbrainrecordingsinhealthcarescenarios,weconstructedabenchmarkconsist-
ingof15datasetsand20tasks.Toevaluategeneralization,wesystematicallyassessed
BrainWaveacrossdifferentcross-domainsettings,includingcross-subject(Fig.2aand
b),cross-hospital(Fig.2c)andcross-subtype(Fig.2d)tasks.Toverifytheeffectiveness
of pretraining, we introduced few-shot classification tasks to evaluate the capability
of the pretrained representations when directly applied to downstream tasks without
fine-tuning(Fig.3).BrainWaveiscomparedagainstthepreviousstate-of-the-artfoun-
dation models that are publicly available, including LaBraM [44], BrainBERT [46]
and MOMENT [47]. Figure 1d summarizes the overall results of BrainWave com-
pared with other methods, in which BrainWave attains consistently state-of-the-art
performance on all the 24 experiments, with significant improvement (p<0.001) over
the second-best method in 20 experiments, showing the versatility of BrainWave in
a wide array of tasks. To demonstrate the practical value of BrainWave, we designed
a series of clinical tasks in two real-world scenarios: seizure onset zone localization
in epilepsy, and prediction of key biomarkers and clinical scale scores in Alzheimer’s
disease, showcasing its potential in supporting clinical decision-making (Fig. 5). To
investigate the effectiveness of joint pretraining with both non-invasive and invasive
neural data, we compared BrainWave with two model variants pretrained exclusively
3

reyal
tnemngila
elacS
redocne
remrofsnarT
noitnetta
lennahC
Data processing Large data corpus Different electrical brain recordings Different data collection scenarios
Stroke Concussion
...
Sleep-disordered breathing
13.79 TB
40,907 hours
15,997 individuals
Latent representations
...
Epilepsy Al d zh is e e i a m s e e r's
EEG
Narcolepsy Pa d r i k s i e n a s s o e n's Insomnia
iEEG
Chann
C
e
h
l
a
0 nne
C
l 1 hannel 2 Channel C
xN
Signal Specgrams
patches with masks
... ... reyal
noitcejorP
skcolb
remrofsnarT
[MSK]
[MSK]
[CLS]
...
[CLS]
... noitcurtsnoceR
ssol
Reconstruct masked specgrams
redoced
thgiewthgiL
[CLS]
... ...
Pretrain
... [.C.L.S] [C[CL [C SLS] LS]]
...
...
[C[CL [C SLSL ] S] [ .] C.L.S]
...
...
a
b
c Few-shot classification with class prototypes d BrainWave LaBraM BrainBERT MOMENT
Cross-subject Cross-hospital Cross-subtype Few-shot classification
Support set Query
BrainWave BrainWave BrainWave BrainWave
Prototypes
Cross-domain transfer learning
Source subjects Hospital A Absence seizure
fine-tune fine-tune fine-tune BrainWave BrainWave BrainWave
predict predict predict
Target subjects Hospital B Clonic seizure
...
3
s
2 s 1 s
0
s
Absence-16 CHB-MIT ADHD-Child
Mayo-Clinic 97 91 81 ADHD-Adult
FNUSA 98 92 80 72 97 Schizophrenia-28
93 90 90 89
AD-65 67 60 84 76 83 75 86 81 6 7 0 0 56 64 75 82 66 78 70 79 Depression-122 MDD-64 90 82 74 52 45 67 54 50 60 83 88 92 MDD-64
66 79
Depression-122 74 70 65 60 54 61 68 76 AD-65
53 61
Schizophre A n D ia H -2 D 8 -Adul 7 t 2 91 66 80 5 6 7 9 9 0 61 60 7 5 2 4 66 75 675 6 6 4 49 58 56 5 6 5 4 66 62 74 7 7 0 2 83 83 91 9 M 4 to a y F o N M - F C U a N l S y in U o A ic S -C A li n to ic
76 78 72 78
ADHD-Child 83 83 72 68 80 A to b s A e t n o c n e ic - - 1 5 6
CHB-MIT 92 80 77 A to b s C e l n o c n e ic - - 1 6 6
Absence-16 Mayo-Clinic FNUSA
Fig. 1 Overview of BrainWave. a, Data curation for pretraining BrainWave. The pretraining
corpuscontainsbothinvasiveandnon-invasivebrainrecordingscollectedfromdiversehealthcaresce-
narios. b, The pretraining pipeline of BrainWave. BrainWave is pretrained on more than 3 billion
signalpatchesusingamaskedmodelingstrategy.c,Theevaluationtasksconsistoffew-shotclassifi-
cationandcross-domainevaluation.Weconductfew-shotclassificationwithaprototypicalnetwork
in which the we directly compare the representations of the queries with class prototypes. We per-
formthreedifferentlevelsofcross-domain analysis:cross-subject,cross-hospital, and cross-subtype.
d, The overall results of BrainWave compared to other pretrained models. BrainWave outperforms
4
othermodelsacrossallthe24experiments,withsignificantimprovement(p<0.001)in20ofthem.

|     |     | ours |     | labram | brainbert |     | moment |     |     |     |     |
| --- | --- | ---- | --- | ------ | --------- | --- | ------ | --- | --- | --- | --- |
| 1.0 |     |      |     |        | 1.0       |     |        |     |     |     |     |
| 0.9 |     |      |     |        | 0.9       |     |        |     |     |     |     |
CORUA
| 0.8 |     |     |     |     | CCAB 0.8 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
| 0.7 |     |     |     |     | 0.7      |     |     |     |     |     |     |
| 0.6 |     |     |     |     | 0.6      |     |     |     |     |     |     |
| 0.5 |     |     |     |     | 0.5      |     |     |     |     |     |     |
t i o n a nd   s is o s is o s is s i s t ion  c t i o n a nd   o s is o s is o s is o s i s a t ion
 d e te c i o n   D dia g n o a g n nia diagn D diag n o p r iv a d e te c t i o n   n D dia g n i a g n nia diagn D diag n p r iv
Epileps y e t e c t a t io n ssio n  d i H p   d e c ti o n Epileps y   d e t e z a t io A ssio n  d H e p   d e c ti o n
p s y   d c a l i z A r e p h r e A D S l e e d e t e p s y   o c a l i p r e p h r e A D S l e d e t e
| p ile O Z  l o | D e p | h i zo |     |     | E p i | le O Z  l | D e | c h i zo |     |     |     |
| -------------- | ----- | ------ | --- | --- | ----- | --------- | --- | -------- | --- | --- | --- |
| E S            |       | S c    |     |     |       | S         |     | S        |     |     |     |
a
|     |     |     |     |     | BrainWave | LaBraM | BrainBERT |     | MOMENT |     |     |
| --- | --- | --- | --- | --- | --------- | ------ | --------- | --- | ------ | --- | --- |
qr st uvwx
|     | a   |     | b   |           |     | c   |           | d   |           | e   |           |
| --- | --- | --- | --- | --------- | --- | --- | --------- | --- | --------- | --- | --------- |
|     |     |     |     | P < 0.001 |     |     | P = 0.009 |     | P < 0.001 |     | P < 0.001 |
|     |     | 1.0 |     | 1.0       |     | 1.0 |           |     | 1.0       |     | 1.0       |
P < 0.001
|     |     | 0.8 |     | 0.8 |     | 0.8 |     |     | 0.8 |     | 0.8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
CORUA
|     |     | 0.6       |     | 0.6       |         | 0.6 |            |     | 0.6         |     | 0.6       |
| --- | --- | --------- | --- | --------- | ------- | --- | ---------- | --- | ----------- | --- | --------- |
|     |     | 0.4       |     | 0.4       |         | 0.4 |            |     | 0.4         |     | 0.4       |
|     |     | AD-65     |     |           | CHB-MIT |     | Absence-16 |     | Mayo-Clinic |     | FNUSA     |
|     | f   |           | g   |           |         | h   |            | i   |             | j   |           |
|     |     | P < 0.001 |     |           |         |     | P < 0.001  |     | P < 0.001   |     |           |
|     |     | 1.0       |     | 1.0       |         | 1.0 |            |     | 1.0         |     | 1.0       |
|     |     |           |     | P < 0.001 |         |     |            |     |             |     | P < 0.001 |
|     |     | 0.8       |     | 0.8       |         | 0.8 |            |     | 0.8         |     | 0.8       |
CORUA
|     |       | 0.6       |        | 0.6            |           | 0.6    |                  |           | 0.6        |           | 0.6        |
| --- | ----- | --------- | ------ | -------------- | --------- | ------ | ---------------- | --------- | ---------- | --------- | ---------- |
|     |       | 0.4       |        | 0.4            |           | 0.4    |                  |           | 0.4        |           | 0.4        |
|     |       | MDD-64    |        | Depression-122 |           |        | Schizophrenia-28 |           | ADHD-Adult |           | ADHD-Child |
|     |       | BrainWave | LaBraM | BrainBERT      |           | MOMENT |                  | BrainWave | LaBraM     | BrainBERT | MOMENT     |
|     | k     |           |        | l              |           |        | m                |           |            | n         |            |
|     |       | P = 0.012 |        |                | P < 0.001 |        |                  | 1.0       |            |           |            |
|     |       | 1.0       |        | 1.0            |           |        |                  |           | P < 0.001  | 1.0       | P < 0.001  |
|     | CORUA | 0.8       |        | 0.8            |           |        | CORUA            | 0.8       |            | 0.8       |            |
|     |       | 0.6       |        | 0.6            |           |        |                  | 0.6       |            | 0.6       |            |
0.4
|     |     | 0.4                  |     | 0.4 |                      |     |     |                        |     | 0.4 |                        |
| --- | --- | -------------------- | --- | --- | -------------------- | --- | --- | ---------------------- | --- | --- | ---------------------- |
|     |     | Mayo-Clinic to FNUSA |     |     | FNUSA to Mayo-Clinic |     |     | Absence-16 to Clonic-6 |     |     | Absence-16 to Atonic-5 |
Fig.2 Performanceofcross-domainevaluation.a-j,BarplotscomparingtheAUROCscores
of BrainWave and competing models on cross-subject tasks. Each experiment is conducted with n-
fold cross validation (n is the number of subject groups), where we repeat five runs for each fold.
k,l,BarplotscomparingtheAUROCscoresofBrainWaveandcompetingmodelsoncross-hospital
tasks.m,n,BarplotscomparingtheAUROCscoresofBrainWaveandcompetingmodelsoncross-
subtypetasks.k-n,Thesourcedatasetisservedasthetrainingsetandthetargetdatasetisserved
astheevaluationset.Ineachexperiment,werepeatfiveruns.a-n,Dataaremean±SD.Thelisted
pvalueindicatesthesignificanceforBrainWaveoutperformingthebestcomparisonmodel,withthe
two-sidedt-test.
onEEGoriEEGdataacrossallexperiments(Fig.5a-d).TheresultsshowthatBrain-
Wave outperforms other variants in diverse tasks, highlighting the effectiveness of its
design empowered by joint pretraining. In conclusion, our study demonstrates (1) the
robustnessofthepretrainedrepresentations,(2)thepotentialofBrainWaveinclinical
|     | diagnostic | support, |     | and (3) | the | effectiveness |     | of joint | pretraining. |     |     |
| --- | ---------- | -------- | --- | ------- | --- | ------------- | --- | -------- | ------------ | --- | --- |
WewillreleaseBrainWaveasapubliclyavailablemodel,whichwillserveasabasis
for others in their own tasks, facilitating diverse clinical applications and research for
brain recordings.
5

2 Results
2.1 Cross-domain Disease Diagnosis and Detection
Cross-domainevaluationisanimportantsettingforverifyingthegeneralizationcapa-
bility of the model. Firstly, we conducted cross-subject evaluation, in which we split
the subjects into n non-overlapping groups and employed n-fold cross validation to
evaluate all models, ensuring that all subjects are included in the testing process. In
each fold, we randomly selected a subject group from the training set for validation
and repeated five runs. BrainWave was evaluated against competing methods on a
total of 10 datasets, including Alzheimer’s disease (AD), epilepsy, major depressive
disorder, schizophrenia and attention-deficit/hyperactivity disorder (ADHD). Model
performancewasreportedusingtheareaunderthereceiveroperatingcurve(AUROC)
and balanced accuracy (BACC). We calculated p values with the two-sided t−test
between BrainWave and the most competitive comparison model for each task to
check for significance. Across all experiments, BrainWave consistently outperformed
other methods with an average relative improvement of 11.93% in AUROC and
17.59% in BACC over each second-best performing model (Fig. 2a-j and Extended
Data Fig. A1). In schizophrenia diagnosis (Fig. 2h; dataset Schizophrenia-28 [48]),
BrainWaveachievedanimprovementof37.44%and41.59%comparedtothebestcom-
parison model in terms of AUROC and BACC. In seizure detection (Fig. 2b; dataset
CHB-MIT [49]), BrainWave demonstrated a 26.18% boost relative to the second best
method. The strong performance of BrainWave on both ADHD-Adult [50] (Fig. 2i)
and ADHD-Child [51] (Fig. 2j) indicated its robustness across age groups, owing to
the broad age distribution in our pretraining corpus. In conclusion, BrainWave signif-
icantlysurpassedothermodels(p<0.001)on9outofthe10datasets,demonstrating
its superiority in disease diagnosis and detection.
The promising results of BrainWave on cross-subject evaluation motivated us to
further explore its transfer capability across more divergent distributions. Thus, we
attempted two more challenging experimental setups. Under these settings, we fine-
tunedononedatasetanddirectlyapplythemodeltoanother.Thesedatasetsarenot
only collected from different individuals but also from different hospitals and collec-
tion devices, or from patients with different disease subtypes. Unlike the traditional
paradigm where fine-tuning is dataset-specific, these settings allow the model to be
seamlesslydeployedacrossdifferentdatasetsandevendifferentbutrelatedtasks.The
cross-hospital evaluation involved mutual transfer between two datasets, Mayo-Clinic
andFNUSA[52],bothcollectedfrompatientswithdrugresistantepilepsy(DRE)but
fromdifferenthospitals.Thecross-subtypeevaluationincludedthreedatasets,namely
Absence-16, Clonic-6, and Atonic-5, collected from patients with different subtypes of
seizures (absence seizure, clonic seizure, and atonic seizure), and we performed zero-
shottransferfromAbsence-16toClonic-6andAtonic-5.BrainWaveshowedpromising
results and achieved the best performance in all cross evaluations (Fig. 2m-p and
Extended Data Fig. A2). For instance, BrainWave achieved an impressive AUROC
of 93.82% in the zero-shot transfer from FNUSA to Mayo-Clinic (Fig. 2n). When
transferringacrossdifferentseizuresubtypes(Fig.2o,p),BrainWaveexhibitedaverage
improvements of 13.90% and 13.49% in terms of AUROC and BACC, respectively,
6

|     |     |     | BrainWave | LaBraM |     | BrainBERT | MOMENT |     |     |     |
| --- | --- | --- | --------- | ------ | --- | --------- | ------ | --- | --- | --- |
| a   |     | b   |           | c      |     | d         |        | e   |     |     |
1.0 AD-65 1.0 CHB-MIT 1.0 Absence-16 1.0 Mayo-Clinic 1.0 FNUSA
| CORUA 0.8 |     | 0.8 |     | 0.8 |     | 0.8 |     | 0.8 |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.6       |     | 0.6 |     | 0.6 |     | 0.6 |     | 0.6 |     |     |
| 0.4       |     | 0.4 |     | 0.4 |     | 0.4 |     | 0.4 |     |     |
3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot
| f         |        | g   |                | h   |                  | i   |            | j   |            |     |
| --------- | ------ | --- | -------------- | --- | ---------------- | --- | ---------- | --- | ---------- | --- |
|           | MDD-64 |     | Depression-122 |     | Schizophrenia-28 |     | ADHD-Adult |     | ADHD-Child |     |
| 1.0       |        | 1.0 |                | 1.0 |                  | 1.0 |            | 1.0 |            |     |
| CORUA 0.8 |        | 0.8 |                | 0.8 |                  | 0.8 |            | 0.8 |            |     |
| 0.6       |        | 0.6 |                | 0.6 |                  | 0.6 |            | 0.6 |            |     |
| 0.4       |        | 0.4 |                | 0.4 |                  | 0.4 |            | 0.4 |            |     |
3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot
| k   | BrainWave |     |     | LaBraM |     | BrainBERT |     |     | MOMENT |     |
| --- | --------- | --- | --- | ------ | --- | --------- | --- | --- | ------ | --- |
61-ecnesbA
Fig. 3 Performance and analysis of few-shot classification. a-j, Box plots comparing the
AUROC scores of BrainWave and competing models on few-shot classification. We conduct n-fold
cross validation for each experiment and repeat five runs per fold. We perform 3-shot and 8-shot
classification for each task. k, t-SNE (t-distributed Stochastic Neighbor Embedding) plots of the
pretrainedrepresentationsonAbsence-16generatedfromBrainWaveandotherpretrainedencoders.
Eachmodelcontainsfoursubplots,witheachsubplotgeneratedbyrandomlysamplingaportionof
theoriginaldataset.
compared to the second-best model. In summary, our experimental results indicated
thatBrainWaveholdsthepotentialtoreducelabelingandtrainingcostsundersimilar
scenarios, demonstrating strong transferability across disease detection tasks.
| 2.2 | Few-shot | Classification |     |     |     |     |     |     |     |     |
| --- | -------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
In clinical practice, limited availability of labeled data sometimes poses challenges for
| n   | BrainWave |     |     | LaBraM |     | BrainBERT |     |     | MOMENT |     |
| --- | --------- | --- | --- | ------ | --- | --------- | --- | --- | ------ | --- |
fine-tuning models, which 02 highlights 0.015.70.55.20.05.2-0.5-5.7-0.01- the 04030201001-02-03-04- critical importance of learning sufficiently
|     | 51  |     | 51  |     |     | 06  | 06  |     | 6   | 6   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
robustrepresentations.Consequently,weperformedfew-shotclassification,whichisan 01 0402 0402 4 4
|     | 5   |     | 01  |     |     |     |            |     | 2   | 2   |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- |
|     | 0   |     | 5   |     |     |     | 002-04-06- |     | 0   | 0   |
evaluation scheme 5- that 0 studies the generalization capabilities 002-04-06- of models on new tasks
|     | 01-51-02- |     | 5-  |     |     |     |     |     | 2-  | 2-4-6-8- |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | -------- |
given 61-ecnesbA a very limited 01-51- number of labeled examples. We adopted a direct 4- comparison
6-
| 01505-01- | 51- | 01505-01- | 51- 8 6 4 2 | 0 2- 4 6 03 02 01 | 0 01- 0 0 06 | 04 02 0 02- 04- 06- | 08 06 04 02 0 0 0 0 |     |     |     |
| --------- | --- | --------- | ----------- | ----------------- | ------------ | ------------------- | ------------------- | --- | --- | --- |
strategy for classification by comparing - - 2 - the 3 - representations of 2 - 4 - 6 - the 4 queries 2 0 2- 4- with 4 2 0 proto- 2- 4-
|     |     |     | 02  | 04030201001-02-03-04- | 04030201001-02-03-04- | 06  | 06  |     | 6   | 6   |
| --- | --- | --- | --- | --------------------- | --------------------- | --- | --- | --- | --- | --- |
type of each 02 category 5101 (Fig. 1c). The process solely involved obtaining representations 4 4
|     | 01  |     |     |     |     | 0402      | 0402       |     |     | 2        |
| --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | --- | -------- |
|     |     |     | 5   |     |     |           |            |     | 2   | 0        |
|     | 0   |     | 0   |     |     | 0         | 002-04-06- |     | 0   |          |
|     | 01- |     | 5-  |     |     | 02-04-06- |            |     | 2-  | 2-4-6-8- |
01-51-
|     | 02- |     |     |     |     |     |     |     | 4-  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | 7   |     |     |     | 6-  |     |
5101505-01- 51- 5101505-01- 51- 02 01 0 01- 02- 06 04 02 0 02- 04- 06 04 02 0 02- 04- 06- 06 04 02 0 02- 0 4 - 0 6 - 8 6 4 2 0 2- 4- 4 2 0 2- 4- 6-

from the pretrained models and computing class prototypes, without any parameter
updates or introduction of new parameters. The few-shot experiments were still con-
ductedunderthecross-subjectsettingandweemployedn-foldcrossvalidation,where
in each fold we randomly chose labeled examples from the training set as the sup-
port set. We established two sizes for the support set, with 3 and 8 labeled examples
per class (3-shot and 8-shot), respectively. Given that the performance can fluctuate
depending on the support set, we repeated experiments over five runs in each fold.
We conducted few-shot experiments (Fig. 3a-j and Extended Data Fig. A3) on
all datasets used in the cross-subject evaluation and found that BrainWave still
maintained solid performance by achieving an average improvement of 22.23% in
terms of AUROC compared to the second-best model. For instance, on Absence-
16 (Fig. 3c) and ADHD-Adult (Fig. 3i), BrainWave achieved an AUROC over 90%
(91.93% on Absence-16, 90.39% on ADHD-Adult) in 8-shot classification. On MDD-
64 [53] (Fig. 3f), the performance of 8-shot learning even nearly matched that of
full-label supervised fine-tuning (89.83% versus 91.50%). BrainWave not only outper-
formed other models by a large margin but also demonstrated greater robustness to
the selection of the support set. Specifically, we calculated the average standard devi-
ation across all few-shot experiments and found that the fluctuations in BrainWave’s
performanceare,onaverage,smallerthanthoseofthesecond-bestperformingmodels
(5.74% versus 6.06%). The poor performance of BrainBERT in few-shot classifica-
tion may be due to its limitation in supporting only fixed input length and sampling
rate.Thislimitationrequiresadditionaloperationstoaccommodatevaryingdatasets,
highlighting the importance of flexible input support for diverse tasks.
Surprisingly, we also observed that when comparing the 8-shot performance of
BrainWave with the full-label fine-tuning (i.e., with thousands or even tens of thou-
sands of labeled examples) performance of other pretrained models, our model still
outperformsonthemajorityofdatasets(ExtendedDataFig.A4).Acrossalldatasets,
BrainWaveachievedaverageAUROCimprovementsof2.27%,26.40%and14.87%over
LaBraM,BrainBERTandMOMENT,respectively.Tobetterillustratetheresults,we
visualized the representations of the pretrained models, with different colored points
representing different categories (Fig. 3k) and Extended Data Fig. A5). Even without
fine-tuning, the representations generated by BrainWave are sufficiently discrimina-
tive and enable its outstanding performance in few-shot classification. Overall, our
extensive evaluation of few-shot classification demonstrated the immense potential of
BrainWaveasafoundationalmodelthatoffersrobustandoff-the-shelfrepresentations
for electrical brain recordings.
2.3 Clinical Application
Inadditiontoitssuperiorperformanceonbraindisorderdetectionbenchmarks,Brain-
Wave demonstrates practical utility by offering valuable assistance and guidance in
real-world clinical scenarios.
Firstly, we utilized BrainWave to assist in localizing the seizure onset zone (SOZ),
whichreferstotheregionofthebrainwhereepilepticseizuresoriginate.Accurateiden-
tificationoftheSOZiscriticalforplanningsurgicaltreatmentinpatientswithDRE,as
itguidesthelocalizationoftheepileptogenicfocusandsupportsdiagnosticevaluation
8

subject 05ZLH
| AAAAAAAAAAAAAAABBBBBBBBBBBBBBBCCCCCCCCCCCCCCCDDDDDDDDDDDEEEEEEEEEEEEEEEFFFFFFFFFFFFFFFGGGGGGGGGGGGGGGHHHHHHHHHHHHHHH 123456789111111 ---------0 AAAAAAAAA 234567891 | a          | b                                                                                                                                                                                                               |                                     |     |                                         |                                                                 |                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | --- | --------------------------------------- | --------------------------------------------------------------- | ----------------------------- |
|                                                                                                                                                                     |            |                                                                                                                                                                                                                 | Channel-level predicted probability |     | E p i l e p t                           | ic   d is c h a r g e   o c c u r r e n                         | c e Pinpoint                  |
|                                                                                                                                                                     | patient 01 | patient 03 AAAAAAAAAAAAAAABBBBBBBBBBBBBBBCCCCCCCCCCCCCCCDDDDDDDDDDDEEEEEEEEEEEEEEEFFFFFFFFFFFFFFFGGGGGGGGGGGGGGGHHHHHHHHHHHHHHH 123456789111111123456789111111 ---------02345---------02345 AAAAAAAAA 234567891 |                                     |     | 1 - A 2 2 - A 3 3 - A 4 4 - A 5 5 - A 6 | 6 - A 7 7 - A 8 8 - A 9 9 - A 1 0 0 - A 1 1 1 - A 1 2 2 - A 1 3 | 3 - A 1 4 4 - A 1 5 5 - A 1 6 |
|                                                                                                                                                                     | patient 02 | patient 04                                                                                                                                                                                                      | 011111                              |     | A 2 A 3 A 4 A 5 A 6                     | A 7 A 8 A 9 A 1 0 A 1 1 1 A 1 1 2 A 1 1 3                       | A 1 1 4 A 1 1 5 A 1 1 6       |
- A 01 1 1 - ----- A AAAAA 1 12 3456 B 1 - B B 2 - B B 3 - B B 4 - B B 5 - B B 6 - B B 7 - B B 8 - B B 9 - B B 1 0 - B B 1 1 - B B 1 2 - B B 1 3 - B B 1 4 - B B 1 5 - B
1 2345 - ---- A AAAA 1 1111 2 3456 BBBBBBBBB 234567891 C 1 - C 2 C 2 - C 3 C 3 - C 4 C 4 - C 5 C 5 - C 6 C 6 - C 7 C 7 - C 8 C 8 - C 9 C 9 - C 1 0 C 1 0 - C 1 1 C 1 1 - C 1 2 C 1 2 - C 1 3 C 1 3 - C 1 4 C 1 4 - C 1 5 C 1 5 - C 1 6
|     | 0.75 0.85 | 0.95 |     |     | D 2 D 3 D 4 D 5 D | 6 D 7 D 8 D 9 D 1 0 - D 1 1 D 1 2 |     |
| --- | --------- | ---- | --- | --- | ----------------- | --------------------------------- | --- |
123456789111111123456789111111 ---------0 BBBBBBBBB 234567891 0.95 1 - ----- B BBBBB 1 011111 12 3456 D 1 - D 2 - D 3 - D 4 - D 5 - D 6 - D 7 - D 8 - D 9 - D 1 0 D 1 1 -
|     | yticificepS | 12345678911111112345678911 ---------02345---------0 CCCCCCCCC 234567891 |             |     | E 1 - E 2 E 2 - E 3 E 3 - E 4 E 4 - E 5 E 5 - E 6 | E 6 - E 7 E 7 - E 8 E 8 - E 9 E 9 - E 1 0 E 1 0 - E 1 1 E 1 1 - E 1 2 E 1 2 - E 1 3 | E 1 3 - E 1 4 E 1 4 - E 1 5 E 1 5 - E 1 6 |
| --- | ----------- | ----------------------------------------------------------------------- | ----------- | --- | ------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------- |
|     |             |                                                                         |             |     | 1 - F 2 2 - F 3 3 - F 4 4 - F 5 5 - F 6           | 6 - F 7 7 - F 8 8 - F 9 - F 1 0 0 - F 1 1 1 - F 1 2 2 - F 1 3                       | 3 - F 1 4 4 - F 1 5 5 - F 1 6             |
|     |             | 0.85 1 - ----- C CCCCC                                                  | 1 011111 12 |     | F 2 F 3 F 4 F 5 F 6                               | F 7 F 8 F 9 F 9 1 0 F 1 1 1 F 1 1 2 F 1 1 3                                         | F 1 1 4 F 1 1 5 F 1 1 6                   |
- B 01 12 slennahC DDDDDDDDD 234567891 3456 G 1 - G G 2 - G G 3 - G G 4 - G G 5 - G G 6 - G G 7 - G G 8 - G G 9 - G G 1 0 - G G 1 1 - G G 1 2 - G G 1 3 - G G 1 4 - G G 1 5 - G
1 2345---------0 - ---- B BBBB 1 1111 3456 H 1 - H 2 H 2 - H 3 H 3 - H 4 H 4 - H 5 H 5 - H 6 H 6 - H 7 H 7 - H 8 H 8 - H 9 H 9 - H 1 0 H 1 0 - H 1 1 H 1 1 - H 1 2 H 1 2 - H 1 3 H 1 3 - H 1 4 H 1 4 - H 1 5 H 1 5 - H 1 6
- D 01 12
CCCCCCCCC 234567891 0.75 123456789111111 1 ---------02345 EEEEEEEEE - D 234567891 1 O n s e t   c h a n n e l   f r e q u e n c y
|     | Sensitivity |                                                    | 011111    |     | A 2 A 3 A 4 A 5 A 6                             | A 7 A 8 A 9 A 1 0 A 1 1 A 1 2 A 1 3                                                   | A 1 4 A 1 5 A 1 6 Pinpoint                |
| --- | ----------- | -------------------------------------------------- | --------- | --- | ----------------------------------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------- |
|     | 0.8 0.9     | 1.0 1 - ----- E EEEEE                              | 1 12 3456 |     | A 1 - A 2 - A 3 - A 4 - A 5 -                   | A 6 - A 7 - A 8 - A 9 - A 1 0 - A 1 1 - A 1 2 -                                       | A 1 3 - A 1 4 - A 1 5 -                   |
|     |             | 123456789111111 ---------02345 FFFFFFFFF 234567891 |           |     | B 1 - B 2 B 2 - B 3 B 3 - B 4 B 4 - B 5 B 5 - B | 6 B 6 - B 7 B 7 - B 8 B 8 - B 9 B 9 - B 1 0 B 1 0 - B 1 1 B 1 1 - B 1 2 B 1 2 - B 1 3 | B 1 3 - B 1 4 B 1 4 - B 1 5 B 1 5 - B 1 6 |
- C 01 12 1.0 - C 2 - C 3 - C 4 - C 5 - C 6 - C 7 - C 8 - C 9 C 1 0 - C 1 1 - C 1 2 - C 1 3 - C 1 4 - C 1 5 - C 1 6
1 2345 - ---- C CCCC 1 1111 3456 1 - ----- F FFFFF 1011111 123456 C 1 C 2 C 3 C 4 C 5 C 6 C 7 C 8 C 9 - 0 C 1 0 1 C 1 1 2 C 1 2 C 1 3 C 1 4 C 1 5
|     |     | 123456789111111 ---------02345 GGGGGGGGG | 234567891 |     | D 1 - D 2 D 2 - D 3 D 3 - D 4 D 4 - D 5 D 5 - D | 6 D 6 - D 7 D 7 - D 8 D 8 - D 9 D 9 - D 1 D 1 0 - D 1 D 1 1 - D 1 |     |
| --- | --- | ---------------------------------------- | --------- | --- | ----------------------------------------------- | ----------------------------------------------------------------- | --- |
12345678911 ---------0 DDDDDDDDD 234567891 PA 0.9 E 1 - E 2 E 2 - E 3 E 3 - E 4 E 4 - E 5 E 5 - E 6 E 6 - E 7 E 7 - E 8 E 8 - E 9 9 - E 1 0 1 0 - E 1 1 1 1 - E 1 2 1 2 - E 1 3 1 3 - E 1 4 1 4 - E 1 5 1 5 - E 1 6
|     |     | 1 - ----- G GGGGG                                  | 1011111 123456 |     | 2 3 4 5 6                                         | 7 8 9 E 1 0 E 1 1 E 1 2 E 1 3                                                       | E 1 4 E 1 5 E 1 6                         |
| --- | --- | -------------------------------------------------- | -------------- | --- | ------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------- |
|     |     | 123456789111111 ---------02345 HHHHHHHHH 234567891 |                |     | F 1 - F F 2 - F F 3 - F F 4 - F F 5 - F           | F 6 - F F 7 - F F 8 - F F 9 - F F 1 0 - F F 1 1 - F F 1 2 - F                       | F 1 3 - F F 1 4 - F F 1 5 - F             |
|     |     |                                                    |                |     | G 1 - G 2 G 2 - G 3 G 3 - G 4 G 4 - G 5 G 5 - G 6 | G 6 - G 7 G 7 - G 8 G 8 - G 9 G 9 - G 1 0 G 1 0 - G 1 1 G 1 1 - G 1 2 G 1 2 - G 1 3 | G 1 3 - G 1 4 G 1 4 - G 1 5 G 1 5 - G 1 6 |
- D 01 1 0.8 ----- HHHHH 011111 12 - H 2 - H 3 - H 4 - H 5 - H 6 - H 7 - H 8 - H 9 H 1 0 - H 1 1 - H 1 2 - H 1 3 - H 1 4 - H 1 5 - H 1 6
123456789111111 ---------0 1 EEEEEEEEE - D 234567891 1 2 AUROC 1 - H 1 3456 H 1 H 2 H 3 H 4 H 5 H 6 H 7 H 8 H 9 - H 1 0 H 1 1 H 1 2 H 1 3 H 1 4 H 1 5
Multiple epileptic seizures
|     | c Amyloid-beta deposition |     | d MMSE | e MoCA-B | f   | ROCF | g PSQI |
| --- | ------------------------- | --- | ------ | -------- | --- | ---- | ------ |
-- EE 01 123456
| 1 2345 ---- EEEE234567891 1 1111 | 1.0 | 1.0 |     | 1.0 | 1.0 |     | 1.0 |
| -------------------------------- | --- | --- | --- | --- | --- | --- | --- |
123456789111111 ---------0 FFFFFFFFF
|     | 0.9 | 0.9 |     | 0.9 | 0.9 |     | 0.9 |
| --- | --- | --- | --- | --- | --- | --- | --- |
- FF 01 123456
| 1 2345 - ---- FFFF 1 1111 | 0.8 | 0.8 |     | 0.8 | 0.8 |     | 0.8 |
| ------------------------- | --- | --- | --- | --- | --- | --- | --- |
123456789111111123456789111111 ---------0 GGGGGGGGG 234567891
|     | 0.7 Accuracy | 0.7 | Accuracy F1 score | 0.7 Accuracy | 0.7 | Accuracy | 0.7 Accuracy |
| --- | ------------ | --- | ----------------- | ------------ | --- | -------- | ------------ |
F1 score AUROC Kappa AUROC Kappa F1 score AUROC Kappa F1 score AUROC Kappa F1 score AUROC Kappa
- G 01 1
1 2345---------0 - ---- G GGGG 1 1111 2 3456
HHHHHHHHH 234567891 Fig. 4 Clinical tasks on epilepsy and AD. a, Channel-level epileptic waveform detection
on 4 patients with DRE. Sensitivity/Specificity and AUROC/AP are reported. b, The process of
01 pinpointing channels with frequent epileptic discharges and repeated involvement as seizure onset
1 2345 - - ---- H H HHHH 1 1111 1 2 3456
sites.Wecanquicklyquantifythesemetricsforeachchannelfrommodelpredictions.c-g,Predictions
of amyloid-beta deposition and a series of clinical scale scores from AD patients. Each experiment
is conducted with 5-fold cross validation, where we repeat five runs for each fold. c, Amyloid-beta
deposition prediction. d, MMSE score prediction. We divide it into 4 discrete ranges: 24-30, 21-23,
label 10-20 and 0-9. e, MoCA-B score prediction. We divide it into 4 discrete ranges: 26-30, 18-25, 10-17
| A1-A2A2-A3A3-A4A4-A5A5-A6A6-A7A7-A8A8-A9 A9-A10 A10-A11 | A11-A12 A12-A13 A13-A14 and0-9.f,ROCFscoreprediction.Wedivideitinto5discreteranges:33-36,24-32,18-23,12-17and A14-A15 A15-A16 |     |     |     |     |     |     |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
B10-B11 B11-B12 B12-B13 B13-B14 0-11.g,PSQIscoreprediction.Wedivideitinto4discreteranges:0-5,6-10,11-15and16-21. B14-B15 B15-B16
| B1-B2B2-B3B3-B4B4-B5B5-B6B6-B7B7-B8B8-B9 B9-B10         |                                         |     |     |     |     |     |     |
| ------------------------------------------------------- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
| C1-C2C2-C3C3-C4C4-C5C5-C6C6-C7C7-C8C8-C9 C9-C10 C10-C11 | C11-C12 C12-C13 C13-C14 C14-C15 C15-C16 |     |     |     |     |     |     |
| D1-D2D2-D3D3-D4D4-D5D5-D6D6-D7D7-D8D8-D9 D9-D10 D10-D11 | D11-D12                                 |     |     |     |     |     |     |
for subsequent resective surgery. Patients with DRE often require intracranial elec-
| E1-E2E2-E3E3-E4E4-E5E5-E6E6-E7E7-E8E8-E9 E9-E10 E10-E11 | E11-E12 E12-E13 E13-E14 E14-E15 E15-E16 |     |     |     |     |     |     |
| ------------------------------------------------------- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
F1-F2F2-F3F3-F4F4-F5F5-F6F6-F7F7-F8F8-F9F9-F10 F10-F11 F11-F12 F12-F13 F13-F14 trode F14-F15 F15-F16 implantation to record seizure activity. The SOZ can be localized by analyzing
| G1-G2G2-G3G3-G4G4-G5G5-G6G6-G7G7-G8G8-G9 G9-G10 G10-G11 | G11-G12 G12-G13 G13-G14 thewaveformsofdifferentchannels,whichinvolvesdistinguishingseizurepatternsona G14-G15 G15-G16 |     |     |     |     |     |     |
| ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| H1-H2H2-H3H3-H4H4-H5H5-H6H6-H7H7-H8H8-H9 H9-H10 H10-H11 | H11-H12 H12-H13 H13-H14 H14-H15 H15-H16                                                                               |     |     |     |     |     |     |
per-channelbasis.Suchaprocessdemandsmorefine-grainedandpreciseanalysisthan
merely classifying epileptic versus normal waveforms over a certain time period. As
showninFig.4a,BrainWaveisevaluatedonchannel-levelepilepticwaveformdetection
across4patientswithDRE,inwhichtheaverageSensitivity/Specificity,AUROC/Av-
erage Precision (AP) achieved 84.65%/86.87% and 93.24%/86.71% respectively. The
predictions of BrainWave helped reveal the spatial distribution of seizure activity. We
took patient 04 as an example. The heatmap shown on the left side of Fig 4b is the
channel-level predicted probabilities of multiple seizures from patient 04 provided by
BrainWave. As shown in the middle of Fig 4b, the predictions enabled us to quantify
two metrics for each channel: the probability of epileptic discharge occurrence across
multiple seizures (upper), and the number of times it serves as the seizure onset site
(lower). Higher values of these two metrics suggested a greater likelihood of the chan-
nelbeingpartoftheSOZ.AsshownontherightsideofFig4b,clinicianscanquickly
9

identify the corresponding brain regions based on the statistical results, facilitating
surgical planning.
Secondly, BrainWave can predict clinical assessment indicators for AD based on
EEG signals. The diagnosis of AD involves a series of physiological examinations
and cognitive scale tests. The results of these assessments serve as important refer-
ences for the clinical diagnosis of AD. We conducted experiments on 6 patients, using
their recorded EEG data to predict amyloid-beta deposition and a range of clinical
scale scores (Supplementary Tables 17), including Mini-Mental State Examination
(MMSE), Montreal Cognitive Assessment-Basic (MoCA-B), Rey–Osterrieth Complex
FigureTest(ROCF),andPittsburghSleepQualityIndex(PSQI).Amyloid-betadepo-
sition is one of the key biomarkers in the diagnosis of AD, which is often detected
by Positron Emission Tomography (PET) imaging. MMSE, MoCA-B, and ROCF are
cognitive assessment tests, and PSQI is used to evaluate sleep quality. For the clini-
cal scale scores, we divided the scores into several discrete ranges for prediction. Each
range represents an evaluation category, such as normal, mild cognitive impairment,
moderate cognitive impairment, severe cognitive impairment, and so on. We split the
data into 5 groups and utilized a 5-fold cross validation. Each fold was repeated 5
runs. Fig 4c-g shows the results, in which BrainWave achieved an average accuracy
closetoorexceeding95%acrossalltasks,alongwithanaverageCohen’sKappaabove
0.9. BrainWave’s predictions exhibited strong consistency with established clinical
evaluation outcomes, highlighting its great potential to support clinical diagnosis.
2.4 Analysis of Joint Pretraining
To the best of our knowledge, BrainWave is the first foundational model that com-
bines invasive and non-invasive neural data. We next examine the effectiveness of
this joint pretraining strategy to determine whether it is more effective to pretrain a
separate model for each recording type and apply it for corresponding downstream
tasks with the same recording type, or to utilize a joint pretraining approach. To
this end, we separately pretrained two model variants, namely BrainWave-EEG and
BrainWave-iEEG, using EEG and iEEG data, respectively, while keeping the model
and pretraining configurations (Supplementary Tables 18 and 19) identical to Brain-
Wave.ThenumbersofpatchesforpretrainingBrainWave-EEGandBrainWave-iEEG
are relatively balanced (1.74 billion versus 1.42 billion). Subsequently, we conducted
cross-domain evaluation and few-shot classification on both model variants, in which
BrainWave-EEGwasevaluatedonEEGdatasetsandBrainWave-iEEGwasevaluated
on iEEG datasets.
Through a series of experiments, we observed that BrainWave outperformed the
other two variants in almost all tasks and experimental settings (Fig. 5a-d and
Extended Data and Figs. A6 and A7), except in experiment Absence-16 to Atonic-5
where BrainWave is slightly lower than BrainWave-EEG in terms of BACC (44.55%
versus 47.23%). From the overall results, we discovered that the integration of iEEG
during joint pretraining enhanced the performance on downstream tasks based on
EEG data and vice versa, suggesting that BrainWave is able to capture fundamental
insights about brain activities by combining two distinct types of signals. In compari-
sontotheaverageimprovementovertwomodelvariants(Fig.5e),theimprovementof
10

1.0
0.8
0.6
AD-65 CHB-MIT Absence-16 Mayo-Clinic FNUSA MDD
D
-
e
6
p
4 ression
S
-1
c
2
h
2 izophrenia-2
A
8 DHD-Adul
A
t DHD-Child AD-65 CHB-MIT Absence-16 Mayo-Clinic FNUSA MDD
D
-6
e
4 pression-
S
1
c
2
h
2 izophrenia-2
A
8 DHD-Adult ADHD-Child
1.0 AD-65 1.0 CHB-MIT 1.0 Absence-16 1.0 Mayo-Clinic 1.0 FNUSA
0.8 0.8 0.8 0.8 0.8
0.6 0.6 0.6 0.6 0.6
0.4 0.4 0.4 0.4 0.4
3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot
MDD-64 Depression-122 Schizophrenia-28 ADHD-Adult ADHD-Child
1.0 1.0 1.0 1.0 1.0
0.8 0.8 0.8 0.8 0.8
0.6 0.6 0.6 0.6 0.6
0.4 0.4 0.4 0.4 0.4
3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot
AUROC BACC
cross-domain cross-domain
evaluation evaluation
cla fe ss w if - i s c h a o ti t on cla fe ss w if - i s c h a o ti t on
0 0.03 0.06 0.09 0 0.03 0.06 0.09 0.12
CORUA
1.0
0.8
0.6
CCAB
P < 0.001 P = 0.014 P = 0.032 P = 0.010 P < 0.001 P < 0.001 P < 0.001 P = 0.080
CORUA CORUA
1.0
0.8
0.6
CCAB
a
b BrainWave BrainWave-iEEG c BrainWave BrainWave-EEG
1.0 1.0 1.0 1.0 1.0
0.8
0.8 0.8 0.8 0.8 0.6
0.4
0.6 0.6 0.6 0.6
0.2
Mayo-Clinic to FNUSA to Absence-16 to Absence-16 to Absence-16 to
FNUSA Mayo-Clinic Clonic-6 Atonic-5 Clonic-6
d
e f
Average improvement over BrainWave-EEG Average improvement over BrainWave-iEEG BrainWave BrainWave-EEG BrainWave-iEEG
1.0
0.8
0.6
CCAB
1.0 1.0 1.0
0.8
0.8 0.8 0.6
0.6 0.6 0.4
0.4 0.4 0.2
Mayo-Clinic to FNUSA to Absence-16 to
FNUSA Mayo-Clinic Atonic-5
CORUA
CORUA
CCAB
CORUA
BrainWave (EEG dataset) BrainWave (iEEG dataset) BrainWave-EEG BrainWave-iEEG
BrainWave BrainWave-EEG BrainWave-iEEG
Apnea-ECG
Fig.5 Analysisofjointpretraining. a,ScatterplotscomparingtheAUROCandBACCscores
ofBrainWave,BrainWave-EEGandBrainWave-iEEGoncross-subjecttasks.b,Barplotscomparing
the AUROC and BACC scores of BrainWave and BrainWave-iEEG on cross-hospital tasks. c, Bar
plotscomparingtheAUROCandBACCscoresofBrainWaveandBrainWave-EEGoncross-subtype
tasks. b,c, The source dataset is served as the training set and the target dataset is served as the
evaluation set. In each experiment, we repeat five runs. Data are mean ± SD. The listed p value
indicatesthesignificanceforBrainWaveoutperformingthebestcomparisonmodel,withthetwo-sided
t-test. d, Box plots comparing the AUROC scores of BrainWave, BrainWave-EEG and BrainWave-
iEEG on few-shot classification. We perform 3-shot and 8-shot classification for each dataset. e,
Average improvement of BrainWave over BrainWave-EEG and BrainWave-iEEG on cross-domain
evaluationandfew-shotclassification.Wefirstcalculatetherelativeimprovementforeachexperiment
and then compute the average of them. f, Bar plots comparing the AUROC and BACC scores of
BrainWave,BrainWave-EEGandBrainWave-iEEGonout-of-domainrecordingtypeevaluation.We
collectaECGdataset(Apnea-ECG)withasleepapneadetectiontask.Dataaremean±SD.a,d,f,
Eachexperimentisconductedwithn-foldcrossvalidation(nisthenumberofsubjectgroups),where
werepeatfiverunsforeachfold.
11

theBrainWaveoverBrainWave-EEGwasmoresignificantthantheimprovementover
BrainWave-iEEG (7.25% versus 2.05% on cross-domain evaluation and 8.30% versus
4.98% on few-shot classification in terms of AUROC). The phenomenon suggested
that the boost in performance achieved by incorporating iEEG data in the pretrain-
ingwasmorepronounced,whichmightbeattributedtothelowersignal-to-noiseratio
and higher accuracy of intracranial neural signals.
Given that joint pretraining leads to increase in performance, we further explored
the underlying reasons by analyzing the representations learned by the models. First,
we validated whether joint pretraining can learn more enriched information. For
this purpose, we performed principal component analysis (PCA) to the pretrained
representations, selecting principal components until 99% of the variance could be
explained. We conducted analysis on 12 datasets and recorded the number of prin-
cipal components k of each dataset. On 11 out 12 datasets, BrainWave yielded a
higher k value (Supplementary Tables 20 and 21), indicating that BrainWave demon-
strated the ability to extract more enriched information from downstream datasets.
Furthermore, we conducted an additional experiment by evaluating the performance
of the BrainWave versus other variants on another type of biosignal, electrocardio-
gram(ECG),throughwhichweaimedtoverifyifjointpretrainingresultsinastronger
adaptabilityonnewtasksduetotheacquisitionofmoregeneralpatterns.Theresults
(Fig. 5f) showed that BrainWave achieves an improvement of 9.90% and 19.48% in
terms of AUROC over BrainWave-iEEG and BrainWave-EEG, respectively, demon-
strating that joint pretraining enables better generalization to unseen data types. To
summarize,BrainWavelearnedrichersemanticinformationandmoregeneralpatterns
of the data than other model variants with only one type of data. This finding opens
up possibilities for expanding signal types and developing more versatile foundational
models for biosignals.
3 Discussion
We have introduced BrainWave, a brain signal foundation model that learns robust
representationsofelectricalbrainrecordingsforabroadrangeofclinicalapplications.
To the best of our knowledge, BrainWave is the first model pretrained on a large-
scale dataset composed of recordings from both invasive and non-invasive modalities,
which comprised more than 3 billion signal patches from approximately 16,000 indi-
viduals. The architectural design accommodated brain recordings of varying lengths,
sampling rates, and electrode counts, thereby enhancing the flexibility of BrainWave
forjointpretraininganddeploymentonEEGandiEEGdata.Weemployedamasked
modelingstrategytopretrainBrainWave,enablingthemodeltoreconstructthecom-
plete sequence from partial observations. In comprehensive experiments involving
cross-domain evaluation and few-shot classification, we demonstrated the versatility
of BrainWave across a wide array of brain disorder detection tasks under diverse
conditions. We also applied BrainWave to real-world clinical scenarios, suggesting
that BrainWave holds significant potential to support clinical diagnostics and the
identification of health conditions.
12

Beyond its practical value, BrainWave yields valuable insights into the funda-
mental model governing multimodal neural electrical signals. The present study
represents the initial investigation to utilize joint pretraining with both EEG and
iEEG data. Through rigorous assessment, we demonstrated the effectiveness of this
novel methodological approach. The results of our study demonstrate a significant
performance boost derived from the joint pretraining approach, compared to control
modelconfigurations.Additionally,we have elucidatedthefactors contributingto the
enhanced performance associated with joint training. Future investigations can build
upon our findings to examine whether comparable performance enhancements can be
attained with other neural data types or even cross-domain data encompassing varied
physiological signals.
As an exciting interdisciplinary research direction between neuroscience and arti-
ficial intelligence, BrainWave may also provide a new approach to deciphering the
mechanisms of brain information processing. A key challenge in neuroscience research
involves analyzing and elucidating the fundamental operating principles govern-
ing population-level neural networks, as derived from high-volume neural recording
data. Large language models have demonstrated its capacity to extract fundamental
attributes of human cognition by compressing substantial human linguistic data ??.
Similarly, the impressive performance of BrainWave, as shown in the present study,
may be attributed to their ability to thoroughly comprehend and effectively extract
features of brain neural activity. Analyzing the network properties of BrainWave
couldpotentiallyofferinsightstoguideresearchonbiologicalneuralnetworks.Specifi-
cally,bymodulatingvariousparametersofBrainWave,analogousmodelsrepresenting
diverse brain disorders can be generated, thereby establishing a novel experimental
framework for neuroscience and brain disease research.
Despitethepromisingresults,thereisawealthofpotentialforfurtherdevelopment
andadvancement.Firstly,BrainWavecannothandledatafromothermodalities,such
as magnetic resonance imaging (MRI), which can provide higher spatial resolution
compared to electrical signals and is widely used in healthcare applications. Conse-
quently,ourultimateobjectiveistodevelopamodelframeworkthatcanaccommodate
various data modalities. Secondly, diverse medical scenarios collect various physiolog-
ical signals, with diagnoses sometimes relying on multiple signal types. For instance,
stroke diagnosis and rehabilitation often require the recording of EEG and EMG
(Electromyography)[54]. To enhance suitability for a more expansive set of health-
care applications, the model should possess the capability to accommodate a more
diverse array of biosignals. This investigation involved initial efforts utilizing electro-
cardiogram data, which indicates that additional advancements are necessary before
constructing a comprehensive model able to accommodate a variety of physiological
measurements.
13

4 Methods
4.1 Technique details
Fig.1bshowstheoverallarchitectureofBrainWave,whichiscomposedofthreemain
components: scale alignment layer, Transformer encoder and channel attention. This
section aims to introduce the details of these components.
Scale alignment layer. One of the largest challenges in modeling brain signals
by a unified model is the diversity of sampling rates, which leads to inconsistent
temporal resolutions. Previous works often address this issue by resampling all the
signals into a common frequency. However, such a strategy becomes ineffective when
dealing with both iEEG and EEG data. As sampling rates of iEEG and EEG differ
greatly,resamplingthemtoasharedscaleisnotonlyinflexiblebutmayleadtoaloss
of signal fidelity. To overcome this problem, we propose a novel embedding approach
which maps signals with arbitrary sampling rates into a space with a unified scale.
The scale alignment layer of BrainWave projects the original signals into latent
embeddings, in which each channel is operated independently. Given a single-channel
brainrecording,wefirstdividedthesignalintoaseriesofconsecutivenon-overlapping
1-second patches P ∈RN×P, where N is the number of patches, P is the number of
i
timestamps in each 1-second patch, and i is the channel index. Then we calculated
the time-frequency representations of each patch, in which we chose the spectrograms
with Gaussian window. By keeping the ratio of the window size and the hop size to
the patch length P constant, we can align recordings with different sampling rates
onto spectrograms with consistent temporal and frequency resolutions. Specifically,
we set the window size equal to P and the hop size equal to P, and the resulting
4 8
spectrogramsaredenotedasS ∈RN×T×F,whereT isthelengthofthetimeaxisand
i
F is the length of the frequency axis. We convolved S using 2D convolutional kernels
i
toobtainthefeaturemapsM
i
∈RN×Cout×Tout×Fout,whereC
out
istheoutputchannels
and T ×F is the size of the feature maps. Since our design ensured that data
out out
with different sampling rates have the same temporal and frequency resolution, the
length of the time axis T in the resulting feature maps was the same (because the
out
durationofallpatchesis1second),whilethelengthofthefrequencyaxisF varied.
out
Therefore, we performed padding or truncation on the frequency axis to standardize
the size of the feature maps. Then we flattened the standardized feature maps and
projected them with a linear layer to derive the input embeddings E ∈RN×D, where
i
D is the hidden size.
Transformer encoder. The Transformer encoder is composed of stacked Trans-
former blocks with bidirectional self-attention, which captures the temporal rela-
tionship among the patches within a sequence. We first concatenated the input
embeddings E with a [CLS] token, then added a set of learnable positional embed-
i
dings PE ∈ R(N+1)×D to obtain the input of the Transformer encoder. Like the
i
embedding layer, the Transformer encoder encoded each channel independently and
generated a set of outputs O ,O ,...,O , where C is the number of channels. We
1 2 C
derived the whole output O∈RC×(N+1)×D by concatenating the outputs together.
Channel attention. The channel attention module aims at capturing the corre-
lation between different channels. Specifically, the input Oj ∈ RC×D,j = 0,1,...,N
14

contained C different patches at the same time, which was then performed with a
bidirectionalself-attentionoperation.Theoutputofthechannelattention,denotedas
Z ∈ RC×(N+1)×D, served as the latent representation of BrainWave, where Z0 were
sequence-level representations (representations of [CLS] tokens) and Z1,Z2,...,ZN
were patch-level representations.
4.2 Pretraining
Data curation. Wecuratedlargecollectionsofunannotatedelectricalbrainrecord-
ingsforpretraining,totaling13.79TBdataoveradurationof40,907hours.TheiEEG
data were obtained from CCEP [55] and a private corpus collected by ourselves, com-
prising 10.63 TB of data. The recordings spanned a duration of 5231 hours and were
collectedfrom91subjects,ranginginagefrom4to51years.Thesamplingrateranged
from 1000 Hz to 4096 Hz, and the number of channels varied from 48 to 238. The
EEG recordings consisted of CAP [56], HMC [57], Siena [58], SRM [59], TUEG [60],
Schizophrenia-81, Sleep-EDF [61], Stroke-50 [62], PD-31 [63], IowaDataset, UNM-
Dataset,AD-184[64],andaprivateEEGcorpus,withatotalof3.16TBofdata.The
recording duration of the data reached 35,675.5 hours and involved 15,906 subjects,
ranging in age from less than 1 year to over 90 years. The sampling rate ranged from
100 Hz to 1024 Hz, and the number of channels varied from 1 to 64.
The preprocessing of the pretraining data primarily involved channel selection
and filtering. Due to potential equipment issues during the data collection process,
theremightbeinvalidchannelswherenovalidbrainsignalswerecaptured.Therefore,
we needed to perform channel selection, in which we visualized the recordings and
manually selected the valid channels. Because data acquisition may be affected by
power line interference, we apply a 50 Hz or 60 Hz notch filter to remove power
line noise. Since the AC power grid frequency varies across countries and regions
(commonly 50 Hz or 60 Hz), the notch filter frequency is determined by the local
power line frequency where the data is collected.
Pretraining details. The main backbone of BrainWave is the RoBERTa [65]
encoder architecture. The model had a hidden size of 768 and an intermediate size of
2048, with 10 layers and 16 attention heads. We applied absolute positional encod-
ing with a maximum sequence length of 61 (60 signal patches along with a [CLS]
token).WepretrainedBrainWaveonatotalof3,162,233,694signalpatches,including
1,739,447,411 EEG data patches and 1,422,786,283 iEEG data patches. BrainWave
was trained using the AdamW optimizer [66], with β = 0.9, β = 0.95, eps = 10−5.
1 2
For the learning rate scheduling, we utilized a linear warmup of 1000 steps to reach a
peak learning rate of 1.0×10−5, followed by a cosine decay of 30,000 steps to decay
the final learning rate to 0. The total training steps of BrainWave was 16,600. We
employed gradient accumulation during pretraining, where we accumulated gradients
for 16 times of forward and backward before performing a parameter update. The
trainingprocesswasconductedon4×A100GPUswithaglobalbatchsizeof2,560,000
(patches) and the entire process took 100 hours.
15

4.3 Downstream evaluation
Competing methods. We compared BrainWave to 3 publicly available models:
LaBraM [44], BrainBERT [46] and MOMENT [47]. LaBraM is an open-weight model
pretrained on more than 2500 hours of EEG data. It tokenized the EEG into discrete
tokensbytraininganeuraltokenizer,andwaspretrainedwithsymmetricmaskedmod-
eling. BrainBERT is a reusable, off-the-shelf, subject-agnostic, and electrode-agnostic
model that provides embeddings for intracranial recordings. It was pretrained on 43.7
hours of iEEG data recorded from 10 subjects. During pretraining, it masked multi-
ple continuous bands of random frequencies and time intervals in the time-frequency
representations. MOMENT is a family of open-source foundation models for general-
purposetimeseriesanalysis.Itwaspretrainedonalargecollectionofpubliclyavailable
datasets from 13 different domains, which included 20.085 GB (≈ 0.02 TB) worth
of 13 million unique time series and 1.23 billion timestamps (0.15 billion patches).
MOMENT also adopted a masked modeling strategy by masking and reconstructing
the original time series.
Evaluation datasets. The evaluation benchmark comprised 13 distinct datasets.
Alzheimer’sdisease:AD-65[67]containstheEEGrestingstate-closedeyesrecord-
ings from 88 subjects in total (44 males, ages 53–79; and 44 females, ages 44–79). For
theparticipants,36werediagnosedwithAlzheimer’sdisease(ADgroup),23werediag-
nosedwithFrontotemporalDementia(FTDgroup)and29werehealthysubjects(CN
group). We randomly split the subjects from AD group and CN group into 5 groups.
The data comprised 19 channels with a sampling rate of 250 Hz. After processing, we
obtained a total of 5349 samples and each sample contains a 10-second data segment.
Epilepsy: The CHB-MIT [49, 68] database consists of EEG recordings from 22
pediatric subjects (5 males, ages 3–22; and 17 females, ages 1.5–19) with intractable
seizures.Werandomlysplitthesubjectsinto5groups.Thedatacomprised23channels
withasamplingrateof256Hz.Wesplitthedatainto10-secondsegmentsandobtained
4148 samples in total. Absence-16, Clonic-6 and Atonic-5 are 3 private datasets that
werecollectedfrompatientswithabsenceseizures,clonicseizuresandatonicseizures,
respectively. The annotations were divided into three categories: epileptic waveforms,
normal waveforms, and Interictal epileptiform discharge (IED). The recordings com-
prised 19 channels with a sampling rate of 256 Hz. After processing the data into
4-secondsegments,weobtainedatotalof8016samplesfromAbsence-16,2426samples
from Clonic-6, and 1587 samples from Atonic-5. We randomly divided the 16 patients
in Absence-16 into 5 groups. The Mayo-Clinic [52] data were collected between 1 AM
and3AMfrom25patientswithDREundergoingevaluationforepilepsysurgery.The
FNUSA [52] dataset is made up of iEEG data collected in awake resting state from
14 patients diagnosed with DRE. We split Mayo-Clinic and FNUSA into 6 and 5 sub-
jectgroups,respectively.BothMayo-ClinicandFNUSAweresegmentedinto3-second
dataclipsanddownsampledto1000Hz.InordertolocatetheSOZ,annotationswere
made for each channel. We preserved the data segments annotated with physiological
activity,pathological(epileptic)activityandartifacts.Intotal,Mayo-Cliniccontained
113,260 samples and FNUSA contained 179,629 samples.
16

Depression: MDD-64 [53] contains EEG recordings from 64 subjects with 34 of
them diagnosed with Major Depressive Disorder (MDD). We randomly split the sub-
jects into 5 groups. The data comprised 19 channels with a sampling rate of 256
Hz. We split the data into 10-second segments and obtained 7309 samples in total.
Depression-122[69]consistsofrestingEEGdatawith122college-ageparticipants(47
males, ages 18–24; 74 females, ages 18–23; and 1 unknown) with their scores in Beck
Depression Inventory (BDI). According to [70], participants with BDI scores > 13
were considered depressed. Healthy controls had stable low BDI scores (< 7) and no
self-reported history or symptoms of anxiety disorder. The data comprised 64 chan-
nels with a sampling rate of 500 Hz. We split the data into 10-second segments and
obtained 5836 samples in total.
Schizophrenia: Schizophrenia-28 [48] comprises 14 patients with paranoid
schizophrenia and 14 healthy controls. Data were acquired with the sampling fre-
quency of 250 Hz using the standard 10-20 EEG montage with 19 EEG channels. We
randomly split the subjects into 5 groups. For the EEG recordings, we split the data
into 10-second segments and obtained 5744 samples.
Attention deficit hyperactivity disorder (ADHD): ADHD-Adult [50] was collected
from79participants,including42healthyadultsand37adultswithADHD(age20-68
years;male/female:56/23).Thedatasetcontained256HzEEGsignalsrecordedfrom
five channels, including O1, F3, F4, Cz, and Fz, with each subject recorded with two
channels. The subjects were randomly split into 5 groups. We split the data into 5-
second segments and obtained 5056 samples in total. ADHD-Child [51] contains EEG
data collected from 121 children (ages 7-12), including 61 with ADHD and 60 healthy
controls.TheEEGrecordingswereperformedbasedon10-20standardby19channels
at 128 Hz sampling frequency. We randomly split the subjects into 5 groups. After
processing, we obtained a total of 3322 samples and each sample contains a 5-second
data segment.
Sleep Apnea: Apnea-ECG [71] is an annotated database with 70 nighttime ECG
recordings.EachrecordingincludedacontinuousdigitizedECGsignalwithasampling
rate of 100 Hz. We divided the recordings into 5 groups, split the data into 60-second
segments, and obtained 34,271 samples in total.
Cross-subject evaluation. The cross-subject evaluation involved experiments
on 10 datasets: AD-65 (Alzheimer’s disease diagnosis), CHB-MIT (seizure detec-
tion), Absence-16 (seizure detection), Mayo-Clinic (seizure detection), FNUSA
(seizure detection), MDD-64 (MDD diagnosis), Depression-122 (depression diagno-
sis),Schizophrenia-28(schizophreniadiagnosis),ADHD-Adult(ADHDdiagnosis)and
ADHD-child (ADHD diagnosis). We used the AdamW optimizer for fine-tuning, with
β = 0.9, β = 0.95, eps = 10−5. For all the models, we fine-tuned the pretrained
1 2
encoderandtheclassificationheadwithalearningrateof1×10−5 and1×10−4.The
models were trained for up to 30 epochs, and then the best-performing models on the
validation set were selected for testing.
Cross-hospital and cross-subtype evaluation. The cross-hospital evaluation
involvedMayo-ClinicandFNUSA,andthecross-subtypeevaluationinvolvedAbsence-
16,Clonic-6,andAtonic-5.Intheexperiments,wefine-tunedthemodelsonthesource
dataset with a fixed number of epochs and directly evaluated on the target dataset.
17

We used the AdamW optimizer, with β =0.9, β =0.95, eps=10−5. We fine-tuned
1 2
the pretrained encoder and the classification head for 5 epochs with a learning rate of
1×10−5 and 1×10−4.
Few-shotclassification. Thedatasetsusedforfew-shotclassificationwereidentical
tothoseusedforcross-subjectevaluation.Weclassifiedthequeriesbycomparingwith
prototypes. Specifically, in K-shot, M-class classification, given the representations
of the support set {uj|i = 1,2,...,K;j = 1,2,...,M}, we obtained the prototypes for
i
each class as the mean of the examples: {vj = 1 (cid:80)K uj|j =1,2,...,M}. Given the
K i=1 i
representation of a query z ∈ RC×D, where C is the number of channels and D is
the hidden size, we calculated the channel-wise cosine similarities between the query
representationandprototypes:{simj =cos(z,vj)∈RC|j =1,2,...,M}.Thescoresof
the query were the mean of channel-wise similarities and we chose the class with the
highestscoreastheprediction:y =argmax([s1,s2,...,sM]),wheresj = (cid:80)C simj.
pred c=1 c
SOZ localization. The SOZ localization was conducted on 4 patients with DRE
implanted with 4 to 10 electrodes (47 to 120 channels). The data contain channel-
level annotations. The sampling rate is 500 Hz and we split the data into 3-second
segments. For a patient experienced N seizures, BrainWave provided channel-level
predicted probabilities p = {pc,t ∈ [0,1]|i = 1,2...,N;c = 1,2,...,C;t = 1,2,...,T },
i i
where C is the number of channels and T is the number of segments during i’th
i
seizure. For each channel, we calculated two metrics based on the predictions: the
probability of epileptic discharge occurrence, and the number of times it serves as the
seizure onset site. The first metric was obtained by a mean pooling of p along the
channel axis: 1 (cid:80)N (cid:80)Ti pc,t ∈ RC. The second metric was counted across
(cid:80)N
i=1
Ti i=1 t=1 i
N seizures. For each seizure, we smoothed the probabilities with median filtering
alongthetimeaxis.Thenweidentifiedtheearliestchannel(s)thatgeneratedepileptic
waveforms, defined as: c∗ = argmin t, where S is the set of (c,t) pairs that
(c,t)∈Si i
satisfyMedianFilter(pc,t)≥0.5.Wecountedtheoccurrencesofeachidentifiedchannel
i
across N seizures.
Prediction of clinical assessment scores in AD patients. The clinical scale
scores we predicted in Sec. 2.3 included MMSE, MoCA-B, ROCF, and PSQI. We
divided these scores into several discrete ranges. MMSE: 24-30, 21-23, 10-20 and 0-
9. MoCA-B: 26-30, 18-25, 10-17 and 0-9. ROCF: 33-36, 24-32, 18-23, 12-17 and 0-11.
PSQI: 0-5, 6-10, 11-15 and 16-21.
4.4 Data Availability
This study utilized the following publicly available datasets for downstream
benchmarking: AD-65 (https://openneuro.org/datasets/ds004504/versions/1.0.2),
CHB-MIT (https://physionet.org/content/chbmit/1.0.0/), Mayo-Clinic (https:
//springernature.figshare.com/collections/Multicenter intracranial EEG dataset
for classification of graphoelements and artifactual signals/4681208), FNUSA
(https://springernature.figshare.com/collections/Multicenter intracranial EEG
dataset for classification of graphoelements and artifactual signals/4681208), MDD-
64 (https://figshare.com/articles/dataset/EEG Data New/4244171), Depression-122
(https://openneuro.org/datasets/ds003478/versions/1.1.0, Schizophrenia-28
18

(https://repod.icm.edu.pl/dataset.xhtml?persistentId=doi:10.18150/repod.0107441),
ADHD-Adult (https://data.mendeley.com/datasets/6k4g25fhzg/1), ADHD-Child
(https://ieee-dataport.org/open-access/eeg-data-adhd-control-children),
4.5 Code Availability
Wewillreleasethemodelweights,pretrainingcode,andusagecodeuponpublication.
References
[1] Barborica, A., Mindruta, I., L´opez-Madrona, V.J., Alario, F.-X., Tr´ebuchon, A.,
Donos, C., Oane, I., Pistol, C., Mihai, F., B´enar, C.G.: Studying memory pro-
cesses at different levels with simultaneous depth and surface eeg recordings.
FrontiersinHumanNeuroscience17(2023)https://doi.org/10.3389/fnhum.2023.
1154038
[2] Jiang, S., Patel, D.C., Kim, J., et al.: Spatially expandable fiber-based probes
as a multifunctional deep brain interface. Nature Communications 11(1), 6115
(2020) https://doi.org/10.1038/s41467-020-19946-9
[3] Engel, A.K., Moll, C.K., Fried, I., Ojemann, G.A.: Invasive recordings from the
human brain: clinical insights and beyond. Nature Reviews Neuroscience 6(1),
35–47 (2005)
[4] Pesaran, B., Vinck, M., Einevoll, G.T., Sirota, A., Fries, P., Siegel, M., Truc-
colo,W.,Schroeder,C.E.,Srinivasan,R.:Investigatinglarge-scalebraindynamics
using field potential recordings: analysis and interpretation. Nature neuroscience
21(7), 903–919 (2018)
[5] Urai,A.E.,Doiron,B.,Leifer,A.M.,Churchland,A.K.:Large-scaleneuralrecord-
ings call for new insights to link brain and behavior. Nature neuroscience 25(1),
11–19 (2022)
[6] Khodagholy, D., Gelinas, J.N., Thesen, T., Doyle, W., Devinsky, O., Malliaras,
G.G., Buzs´aki, G.: Neurogrid: recording action potentials from the surface of the
brain. Nature neuroscience 18(2), 310–315 (2015)
[7] Horejs, C.M.: Long-term recording of electrical activity in brain organoids.
Nature Reviews Bioengineering 2, 200 (2024) https://doi.org/10.1038/
s44222-024-00164-7
[8] Shih,J.J.,Krusienski,D.J.,Wolpaw,J.R.:Brain-computerinterfacesinmedicine.
Mayo Clinic Proceedings 87(3), 268–279 (2012) https://doi.org/10.1016/j.
mayocp.2011.12.008
[9] Feigin,V.L.,Vos,T.,Nichols,E.,al.:Theglobalburdenofneurologicaldisorders:
translating evidence into policy. Lancet Neurology 19(3), 255–265 (2020) https:
19

//doi.org/10.1016/S1474-4422(19)30411-9
[10] Soufineyestani, M., Dowling, D., Khan, A.: Electroencephalography (eeg) tech-
nology applications and available devices. Applied Sciences 10(21) (2020) https:
//doi.org/10.3390/app10217453
[11] V¨arbu, K., Muhammad, N., Muhammad, Y.: Past, present, and future of EEG-
Based BCI applications. Sensors (Basel) 22(9), 3331 (2022) https://doi.org/10.
3390/s22093331 . Published 2022 Apr 26
[12] Jadhav,C.,Kamble,P.,Mundewadi,S.,et al.:ClinicalapplicationsofEEGasan
excellent tool for event related potentials in psychiatric and neurotic disorders.
International Journal of Physiology, Pathophysiology and Pharmacology 14(2),
73–83 (2022). Published 2022 Apr 15
[13] Silva,C.,Tedesco,S.,O’Flynn,B.:Eegdatasetsforhealthcare:Ascopingreview.
IEEE Access PP, 1–1 (2024) https://doi.org/10.1109/ACCESS.2024.3376254
[14] Amer,N.S.,Belhaouari,S.B.:Eegsignalprocessingformedicaldiagnosis,health-
care, and monitoring: A comprehensive review. IEEE Access 11, 143116–143142
(2023) https://doi.org/10.1109/ACCESS.2023.3341419
[15] Yamada, L., Oskotsky, T., Nuyujukian, P., Center, S.C.E., Center, S.P.E.: A
scalable platform for acquisition of high-fidelity human intracranial EEG with
minimal clinical burden. PLOS ONE 19(6), 0305009 (2024) https://doi.org/10.
1371/journal.pone.0305009 . Published 2024 Jun 13
[16] Dasgupta, D., Miserocchi, A., McEvoy, A.W., Duncan, J.S.: Previous, current,
and future stereotactic eeg techniques for localising epileptic foci. Expert Review
of Medical Devices 19, 571–580 (2022)
[17] Parvizi,J.,Kastner,S.:Promisesandlimitationsofhumanintracranialelectroen-
cephalography. Nature Neuroscience 21(4), 474–483 (2018) https://doi.org/10.
1038/s41593-018-0108-2
[18] Lachaux, J.P., Rudrauf, D., Kahane, P.: Intracranial eeg and human brain
mapping. Journal of Physiology-Paris 97(4-6), 613–628 (2003)
[19] Mesk´o, B.: Data annotators are the unsung heroes of medicine’s artificial
intelligence revolution. Journal of Medical Artificial Intelligence 3(0) (2019)
[20] Pascual, D., Aminifar, A., Atienza, D.: A self-learning methodology for epilep-
tic seizure detection with minimally-supervised edge labeling. In: 2019 Design,
Automation & Test in Europe Conference & Exhibition (DATE), pp. 764–769
(2019). https://doi.org/10.23919/DATE.2019.8714995
[21] Zhao, X., Zhao, Q., Tanaka, T., al.: Classification of the epileptic seizure onset
20

zone based on partial annotation. Cognitive Neurodynamics 17(3), 703–713
(2023) https://doi.org/10.1007/s11571-022-09857-4
[22] Friedman,D.E.,Hirsch,L.J.:Howlongdoesittaketomakeanaccuratediagnosis
in an epilepsy monitoring unit? Journal of Clinical Neurophysiology 26(4), 213–
217 (2009) https://doi.org/10.1097/WNP.0b013e3181b2f2da
[23] Brown, T.T.: Individual differences in human brain development. Wiley Inter-
disciplinary Reviews: Cognitive Science 8(1-2), 1389 (2017) https://doi.org/10.
1002/wcs.1389
[24] Yuan, Z., Zhang, D., Yang, Y., Chen, J., Li, Y.: PPi: Pretraining brain signal
model for patient-independent seizure detection. In: Thirty-seventh Conference
on Neural Information Processing Systems (2023)
[25] Clemente-Su´arez,V.J.,Redondo-Fl´orez,L.,Beltr´an-Velasco,A.I.,Ramos-Campo,
D.J., Belinch´on-deMiguel, P., Martinez-Guardado, I., Dalamitros, A.A., Y´an˜ez-
Sepu´lveda, R., Mart´ın-Rodr´ıguez, A., Tornero-Aguilera, J.F.: Mitochondria and
braindisease:acomprehensivereviewofpathologicalmechanismsandtherapeutic
opportunities. Biomedicines 11(9), 2488 (2023)
[26] McEwen, B.S., Bowles, N.P., Gray, J.D., Hill, M.N., Hunter, R.G., Karatsoreos,
I.N., Nasca, C.: Mechanisms of stress in the brain. Nature neuroscience 18(10),
1353–1363 (2015)
[27] Delgado-Morales, R., Ag´ıs-Balboa, R.C., Esteller, M., Berdasco, M.: Epigenetic
mechanisms during ageing and neurogenesis as novel therapeutic avenues in
human brain disorders. Clinical epigenetics 9, 1–18 (2017)
[28] Gaiteri, C., Ding, Y., French, B., Tseng, G.C., Sibille, E.: Beyond modules and
hubs: the potential of gene coexpression networks for investigating molecular
mechanisms of complex brain disorders. Genes, brain and behavior 13(1), 13–24
(2014)
[29] Yang, S., Zhang, Z., Chen, H., Meng, Y., Li, J., Li, Z., Xu, Q., Zhang, Q., Fan,
Y.-S., Lu, G., et al.: Temporal variability profiling of the default mode across
epilepsy subtypes. Epilepsia 62(1), 61–73 (2021)
[30] Guo,J.,Li,H.,Sun,X.,Qi,L.,Qiao,H.,Pan,Y.,Xiang,J.,Ji,R.:Detectinghigh
frequencyoscillationsforstereoelectroencephalographyinepilepsyviahypergraph
learning. IEEE Transactions on Neural Systems and Rehabilitation Engineering
29, 587–596 (2021)
[31] Wang,Y.,Yang,Y.,Cao,G.,Guo,J.,Wei,P.,Feng,T.,Dai,Y.,Huang,J.,Kang,
G., Zhao, G.: Seeg-net: An explainable and deep learning-based cross-subject
pathological activity detection method for drug-resistant epilepsy. Computers in
BiologyandMedicine148,105703(2022)https://doi.org/10.1016/j.compbiomed.
21

2022.105703
[32] Chen, J., Yang, Y., Yu, T., Fan, Y., Mo, X., Yang, C.: Brainnet: Epileptic wave
detection from seeg with hierarchical graph diffusion learning. In: Proceedings of
the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining,
pp. 2741–2751 (2022)
[33] Bagherzadeh, S., Shahabi, M.S., Shalbaf, A.: Detection of schizophrenia using
hybrid of deep learning and brain effective connectivity image from electroen-
cephalogram signal. Computers in Biology and Medicine 146, 105570 (2022)
https://doi.org/10.1016/j.compbiomed.2022.105570
[34] Sahu,G.,Karnati,M.,Gupta,A.,Seal,A.:Scz-scan:Anautomatedschizophrenia
detection system from electroencephalogram signals. Biomedical Signal Process-
ing and Control 86, 105206 (2023) https://doi.org/10.1016/j.bspc.2023.105206
[35] Miltiadous, A., Gionanidis, E., Tzimourta, K.D., Giannakeas, N., Tzallas, A.T.:
Dice-net: A novel convolution-transformer architecture for alzheimer detection
in eeg signals. IEEE Access 11, 71840–71858 (2023) https://doi.org/10.1109/
ACCESS.2023.3294618
[36] Vicchietti, M.L., Ramos, F.M., Betting, L.E., et al.: Computational methods of
EEG signals analysis for Alzheimer’s disease classification. Scientific Reports 13,
8184 (2023) https://doi.org/10.1038/s41598-023-32664-8
[37] Sun,X.,Xu,Y.,Zhao,Y.,Zheng,X.,Zheng,Y.,Cui,L.:Multi-granularitygraph
convolutionnetworkformajordepressivedisorderrecognition.IEEETransactions
on Neural Systems and Rehabilitation Engineering 32, 559–569 (2024) https:
//doi.org/10.1109/TNSRE.2023.3311458
[38] Zhou, Y., Chia, M.A., Wagner, S.K., et al.: A foundation model for generalizable
disease detection from retinal images. Nature 622, 156–163 (2023) https://doi.
org/10.1038/s41586-023-06555-x
[39] Chen, R.J., Ding, T., Lu, M.Y., et al.: Towards a general-purpose foundation
model for computational pathology. Nature Medicine 30, 850–862 (2024) https:
//doi.org/10.1038/s41591-024-02857-3
[40] Xu,H.,Usuyama,N.,Bagga,J.,et al.:Awhole-slidefoundationmodelfordigital
pathology from real-world data. Nature 630, 181–188 (2024) https://doi.org/10.
1038/s41586-024-07441-w
[41] Pai, S., Bontempi, D., Hadzic, I., et al.: Foundation model for cancer imaging
biomarkers. Nature Machine Intelligence 6, 354–367 (2024) https://doi.org/10.
1038/s42256-024-00807-9
[42] Zhang,K.,Zhou,R.,Adhikarla,E.,etal.:Ageneralistvision–languagefoundation
22

model for diverse biomedical tasks. Nature Medicine (2024) https://doi.org/10.
1038/s41591-024-03185-2
[43] Hao, M., Gong, J., Zeng, X., et al.: Large-scale foundation model on single-cell
transcriptomics.NatureMethods21,1481–1491(2024)https://doi.org/10.1038/
s41592-024-02305-7
[44] Jiang, W., Zhao, L., Lu, B.-l.: Large brain model for learning generic repre-
sentations with tremendous EEG data in BCI. In: The Twelfth International
Conference on Learning Representations (2024)
[45] Zhang, D., Yuan, Z., Yang, Y., Chen, J., Wang, J., Li, Y.: Brant: Foundation
model for intracranial neural signal. In: Thirty-seventh Conference on Neural
Information Processing Systems (2023)
[46] Wang,C.,Subramaniam,V.,Yaari,A.U.,Kreiman,G.,Katz,B.,Cases,I.,Barbu,
A.: BrainBERT: Self-supervised representation learning for intracranial record-
ings. In: The Eleventh International Conference on Learning Representations
(2023)
[47] Goswami, M., Szafer, K., Choudhry, A., Cai, Y., Li, S., Dubrawski, A.:
MOMENT: A family of open time-series foundation models. In: Forty-first
International Conference on Machine Learning (2024)
[48] Olejarczyk,E.,Jernajczyk,W.:EEGinSchizophrenia.https://doi.org/10.18150/
repod.0107441
[49] Guttag, J.: CHB-MIT Scalp EEG Database. PhysioNet (2010). https://doi.org/
10.13026/C2K01R
[50] SadeghiBajestani,G.,Abedian,S.,Makhloughi,F.,Raoufitabar,M.,Saeedi,H.:
ADatasetofEEGSignalsfromAdultswithADHDandHealthyControls:Resting
State,Cognitivefunction,andSoundListeningParadigm.MendeleyData(2023).
https://doi.org/10.17632/6k4g25fhzg.1
[51] Motie Nasrabadi, A., Allahverdy, A., Samavati, M., Mohammadi, M.R.: EEG
Data for ADHD / Control Children. https://doi.org/10.21227/rzfh-zn36
[52] Nejedly, P., Kremen, V., Sladky, V., Cimbalnik, J., Klimes, P., Plesinger, F.,
Mivalt, F., Travnicek, V., Viscor, I., Pail, M., et al.: Multicenter intracranial eeg
datasetforclassificationofgraphoelementsandartifactualsignals.Scientificdata
7 (2020)
[53] Mumtaz, W.: MDD Patients and Healthy Controls EEG Data (New). figshare.
Dataset (2016). https://doi.org/10.6084/m9.figshare.4244171.v2 . https://doi.
org/10.6084/m9.figshare.4244171.v2
23

[54] Jo, S., Jung, J.H., Yang, M.J., Lee, Y., Jang, S.J., Feng, J., Heo, S.H., Kim, J.,
Shin, J.H., Jeong, J., Park, H.S.: Eeg-emg hybrid real-time classification of hand
grasp and release movements intention in chronic stroke patients. In: 2022 IEEE
International Conference on Rehabilitation Robotics (ICORR), pp. 1–6 (2022).
https://doi.org/10.1109/ICORR55369.2022.9896592
[55] Blooijs, D., Boom, M.A., Aar, J.F., Huiskamp, G.J.M., Castegnaro, G., Demuru,
M., Zweiphenning, W.J.E.M., Eijsden, P., Miller, K.J., Leijten, F.S.S., Her-
mes, D.: ”CCEP ECoG Dataset Across Age 4-51”. https://doi.org/10.18112/
openneuro.ds004080.v1.2.4
[56] Terzano, M.G., Parrino, L., Sherieri, A., Chervin, R., Chokroverty, S., Guillem-
inault, C., Hirshkowitz, M., Mahowald, M., Moldofsky, H., Rosa, A., Thomas,
R., Walters, A.: Atlas, rules, and recording techniques for the scoring of cyclic
alternating pattern (cap) in human sleep. Sleep Medicine 2(6), 537–553 (2001)
https://doi.org/10.1016/s1389-9457(01)00149-6 . Erratum in: Sleep Med. 2002
Mar;3(2):185
[57] Alvarez-Estevez, D., Rijsman, R.M.: Inter-database validation of a deep learning
approach for automatic sleep scoring. PLoS ONE 16(8), 0256111 (2021) https:
//doi.org/10.1371/journal.pone.0256111
[58] Detti,P.,Vatti,G.,Lara,G.:Eegsynchronizationanalysisforseizureprediction:
Astudyondataofnoninvasiverecordings.Processes8(7)(2020)https://doi.org/
10.3390/pr8070846
[59] Hatlestad-Hall, C., Rygvold, T.W., Andersson, S.: ”SRM Resting-state EEG”.
https://doi.org/10.18112/openneuro.ds003775.v1.2.1
[60] Harati,A.,Lopez,S.,Obeid,I.,Picone,J.,Jacobson,M.,Tobochnik,S.:Thetuh
eeg corpus: A big data resource for automated eeg interpretation. In: 2014 IEEE
Signal Processing in Medicine and Biology Symposium (SPMB) (2014)
[61] Kemp, B., Zwinderman, A.H., Tuk, B., Kamphuisen, H.A.C., Oberye, J.J.L.:
Analysis of a sleep-dependent neuronal feedback loop: the slow-wave microconti-
nuityoftheeeg.IEEETransactionsonBiomedicalEngineering47(9),1185–1194
(2000) https://doi.org/10.1109/10.867928
[62] Liu, H., Lv, X.: EEG datasets of stroke patients (2022) https://doi.org/10.6084/
m9.figshare.21679035.v5
[63] Rockhill, A.P., Jackson, N., George, J., Aron, A., Swann, N.C.: ”UC San Diego
Resting State EEG Data from Patients with Parkinson’s Disease”. https://doi.
org/10.18112/openneuro.ds002778.v1.0.5
[64] Vicchietti,M.L.,Ramos,F.M.,Betting,L.E.,Campanharo,A.S.:Computational
methods of eeg signals analysis for alzheimer’s disease classification. Scientific
24

| Reports | 13(1), 8184 (2023) |     |     |     |     |
| ------- | ------------------ | --- | --- | --- | --- |
[65] Liu, Y., Ott, M., Goyal, N., Du, J., Joshi, M., Chen, D., Levy, O., Lewis,
M., Zettlemoyer, L., Stoyanov, V.: RoBERTa: A Robustly Optimized BERT
| Pretraining | Approach (2019). | https://arxiv.org/abs/1907.11692 |     |     |     |
| ----------- | ---------------- | -------------------------------- | --- | --- | --- |
[66] Loshchilov, I., Hutter, F.: Decoupled Weight Decay Regularization (2019). https:
//arxiv.org/abs/1711.05101
[67] Miltiadous,A.,Tzimourta,K.D.,Afrantou,T.,Ioannidis,P.,Grigoriadis,N.,Tsa-
likakis,D.G.,Angelidis,P.,Tsipouras,M.G.,Glavas,E.,Giannakeas,N.,Tzallas,
A.T.: ”A Dataset of 88 EEG Recordings From: Alzheimer’s Disease, Frontotem-
poral Dementia and Healthy Subjects”. https://doi.org/10.18112/openneuro.
ds004504.v1.0.2
[68] Shoeb, A.H.: Application of machine learning to epileptic seizure onset detection
| and treatment. | PhD thesis, | Massachusetts | Institute | of Technology | (2009) |
| -------------- | ----------- | ------------- | --------- | ------------- | ------ |
[69] jcavanagh@unm.edu,J.F.C.:”EEG:DepressionRest”.https://doi.org/10.18112/
openneuro.ds003478.v1.1.0
[70] Chang,J.,Choi,Y.:Depressiondiagnosisbasedonelectroencephalographypower
| ratios. Brain | and Behavior | 13(8), 3173 | (2023) |     |     |
| ------------- | ------------ | ----------- | ------ | --- | --- |
[71] Penzel, T., Moody, G.B., Mark, R.G., Goldberger, A.L., Peter, J.H.: The apnea-
ecg database. In: Computers in Cardiology 2000. Vol.27 (Cat. 00CH37163), pp.
| 255–258 | (2000). https://doi.org/10.1109/CIC.2000.898505 |     |     |     |     |
| ------- | ----------------------------------------------- | --- | --- | --- | --- |
25

| Appendix |     | A   | Extended  |        | Data      |        |     |     |     |
| -------- | --- | --- | --------- | ------ | --------- | ------ | --- | --- | --- |
|          |     |     | BrainWave | LaBraM | BrainBERT | MOMENT |     |     |     |
P < 0.001
|     | 1.0 | 1.0 | P < 0.001 | 1.0 | P < 0.001 | 1.0 |     | 1.0 | P < 0.001 |
| --- | --- | --- | --------- | --- | --------- | --- | --- | --- | --------- |
P < 0.001
|     | 0.8 | 0.8 |     | 0.8 |     | 0.8 |     | 0.8 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
CCAB
|     | 0.6       | 0.6 |         | 0.6 |            | 0.6 |             | 0.6 |       |
| --- | --------- | --- | ------- | --- | ---------- | --- | ----------- | --- | ----- |
|     | 0.4       | 0.4 |         | 0.4 |            | 0.4 |             | 0.4 |       |
|     | AD-65     |     | CHB-MIT |     | Absence-16 |     | Mayo-Clinic |     | FNUSA |
|     | P < 0.001 |     |         |     | P < 0.001  |     | P < 0.001   |     |       |
|     | 1.0       | 1.0 |         | 1.0 |            | 1.0 |             | 1.0 |       |
P < 0.001
P < 0.001
|     | 0.8 | 0.8 |     | 0.8 |     | 0.8 |     | 0.8 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
CCAB
0.6
|     | 0.6    | 0.6 |                | 0.6 |                  | 0.6 |            |     |            |
| --- | ------ | --- | -------------- | --- | ---------------- | --- | ---------- | --- | ---------- |
|     | 0.4    | 0.4 |                | 0.4 |                  | 0.4 |            | 0.4 |            |
|     | MDD-64 |     | Depression-122 |     | Schizophrenia-28 |     | ADHD-Adult |     | ADHD-child |
Fig. A1 Performance of cross-subject tasks. Bar plots comparing the BACC scores of
BrainWave and competing models on cross-subject tasks. Data are mean ± SD. Each experiment
is conducted with n-fold cross validation (n is the number of subject groups), where we repeat five
runsforeachfold.ThelistedpvalueindicatesthesignificanceforBrainWaveoutperformingthebest
comparisonmodel,withthetwo-sidedt-test.
26

| a                |                  | b                |                  |
| ---------------- | ---------------- | ---------------- | ---------------- |
| BrainWave LaBraM | BrainBERT MOMENT | BrainWave LaBraM | BrainBERT MOMENT |
| 1.0              | 1.0 P < 0.001    | 1.0              | 1.0              |
P < 0.001
|          |     | 0.8  | 0.8 |
| -------- | --- | ---- | --- |
| CCAB 0.8 | 0.8 | CCAB |     |
P < 0.001
|     |     | 0.6 | 0.6 P < 0.001 |
| --- | --- | --- | ------------- |
| 0.6 | 0.6 |     |               |
|     |     | 0.4 | 0.4           |
| 0.4 | 0.4 |     |               |
Mayo-Clinic to FNUSA FNUSA to Mayo-Clinic Absence-16 to Clonic-6 Absence-16 to Atonic-5
Fig.A2 Performanceofcross-hospitalandcross-subtypetasks. a,Barplotscomparingthe
BACC scores of BrainWave and competing models on cross-hospital tasks. b, Bar plots comparing
theBACCscoresofBrainWaveandcompetingmodelsoncross-subtypetasks.Dataaremean±SD.
Each experiment is repeated five runs. The listed p value indicates the significance for BrainWave
outperformingthebestcomparisonmodel,withthetwo-sidedt-test.
27

|     | BrainWave | LaBraM BrainBERT | MOMENT |     |
| --- | --------- | ---------------- | ------ | --- |
1.0 AD-65 1.0 CHB-MIT 1.0 Absence-16 1.0 Mayo-Clinic 1.0 FNUSA
| 0.8 | 0.8 | 0.8 | 0.8 | 0.8 |
| --- | --- | --- | --- | --- |
CCAB
| 0.6 | 0.6 | 0.6 | 0.6 | 0.6 |
| --- | --- | --- | --- | --- |
| 0.4 | 0.4 | 0.4 | 0.4 | 0.4 |
3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot
1.0 MDD-64 1.0 Depression-122 1.0 Schizophrenia-28 1.0 ADHD-Adult 1.0 ADHD-Child
| 0.8 | 0.8 | 0.8 | 0.8 | 0.8 |
| --- | --- | --- | --- | --- |
CCAB
| 0.6 | 0.6 |     |     | 0.6 |
| --- | --- | --- | --- | --- |
|     |     | 0.6 | 0.6 |     |
| 0.4 | 0.4 |     |     | 0.4 |
|     |     | 0.4 | 0.4 |     |
3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot 3-shot 8-shot
Fig. A3 Performance of few-shot classification. Box plots comparing the BACC scores of
BrainWave and competing models on few-shot classification. We conduct n-fold cross validation for
each experiment and repeat five runs per fold. We perform 3-shot and 8-shot classification for each
task.
28

|           |     | BrainWave |     | LaBraM |     | BrainBERT | MOMENT |     |     |
| --------- | --- | --------- | --- | ------ | --- | --------- | ------ | --- | --- |
| 1.0       |     | 1.0       |     |        | 1.0 | 1.0       |        | 1.0 |     |
| CORUA 0.8 |     | 0.8       |     |        | 0.8 | 0.8       |        | 0.8 |     |
| 0.6       |     | 0.6       |     |        | 0.6 | 0.6       |        | 0.6 |     |
| 0.4       |     | 0.4       |     |        | 0.4 | 0.4       |        | 0.4 |     |
Absence-16
|     | AD-65 |     | CHB-MIT |     |     |     | Mayo-Clinic |     | FNUSA |
| --- | ----- | --- | ------- | --- | --- | --- | ----------- | --- | ----- |
| 1.0 |       | 1.0 |         |     | 1.0 | 1.0 |             | 1.0 |       |
| 0.8 |       | 0.8 |         |     | 0.8 | 0.8 |             | 0.8 |       |
CCAB
| 0.6       |        | 0.6 |                |       | 0.6              | 0.6 |             | 0.6 |            |
| --------- | ------ | --- | -------------- | ----- | ---------------- | --- | ----------- | --- | ---------- |
| 0.4       |        | 0.4 |                |       | 0.4              | 0.4 |             | 0.4 |            |
|           | AD-65  |     | CHB-MIT        |       | Absence-16       |     | Mayo-Clinic |     | FNUSA      |
| 1.0       |        | 1.0 |                |       | 1.0              | 1.0 |             |     |            |
|           |        |     |                | CORUA | 0.8              | 0.8 |             |     |            |
| CORUA 0.8 |        | 0.8 |                |       |                  |     |             | 0.8 |            |
|           |        |     |                |       | 0.6              | 0.6 |             | 0.6 |            |
| 0.6       |        | 0.6 |                |       |                  |     |             |     |            |
| 0.4       |        | 0.4 |                |       | 0.4              | 0.4 |             | 0.4 |            |
|           | MDD-64 |     | Depression-122 |       | Schizophrenia-28 |     | ADHD-Adult  |     | ADHD-Child |
| 1.0       |        | 1.0 |                |       | 1.0              | 1.0 |             | 1.0 |            |
| 0.8       |        | 0.8 |                |       | 0.8              | 0.8 |             | 0.8 |            |
CCAB
|     |        |     |                |     | 0.6              | 0.6 |            |     |            |
| --- | ------ | --- | -------------- | --- | ---------------- | --- | ---------- | --- | ---------- |
| 0.6 |        | 0.6 |                |     |                  |     |            | 0.6 |            |
|     |        |     |                |     | 0.4              | 0.4 |            | 0.4 |            |
| 0.4 |        | 0.4 |                |     |                  |     |            |     |            |
|     |        |     |                |     | Schizophrenia-28 |     | ADHD-Adult |     | ADHD-Child |
|     | MDD-64 |     | Depression-122 |     |                  |     |            |     |            |
Fig.A4 Comparisonbetweenfew-shotclassificationwithBrainWaveandfull-labelfine-
tuning of competing models.BoxplotscomparingtheAUROCandBACCscoresofBrainWave
on8-shotclassificationandotherpretrainedmodelsonfull-labelfine-tuning.Forallthemodels,we
conductn-foldcrossvalidationineachexperimentandrepeatfiverunsperfold.
|     |     |     | BrainWave | LaBraM |     | BrainBERT | MOMENT |     |     |
| --- | --- | --- | --------- | ------ | --- | --------- | ------ | --- | --- |
29

|     | BrainWave |     | LaBraM |     | BrainBERT |     | MOMENT |     |
| --- | --------- | --- | ------ | --- | --------- | --- | ------ | --- |
tludA-DHDA
|     | BrainWave |     | LaBraM |     | BrainBERT |     | MOMENT |     |
| --- | --------- | --- | ------ | --- | --------- | --- | ------ | --- |
46-DDM
Fig. A5 t-SNE analysis of few-shot classification. t-SNEplotsofthepretrainedrepresenta-
tionsonADHD-AdultandMDD-64generatedfromBrainWaveandotherpretrainedencoders.Each
model contains four subplots, with each subplot generated by randomly sampling a portion of the
originaldataset.
|            | BrainWave                    |       | LaBraM |     | BrainBERT |     | MOMENT   |        |
| ---------- | ---------------------------- | ----- | ------ | --- | --------- | --- | -------- | ------ |
|            | 0.015.70.55.20.05.2-0.5-5.7- |       |        | 51  |           |     | 8        | 5101   |
|            |                              | 01    | 01     |     | 01        | 01  | 6        |        |
|            |                              |       |        | 01  |           |     | 4        |        |
|            |                              | 5     | 5      | 5   | 5         | 5   | 2        | 5      |
|            |                              | 0     |        |     |           |     | 0        | 0      |
|            |                              |       | 0      | 0   | 0         | 0   |          | 5-     |
|            |                              | 5-01- | 5-     |     |           |     | 2-4-6-8- |        |
| tludA-DHDA |                              |       |        | 5-  | 5-        | 5-  |          | 01-51- |
|            |                              |       | 01-    | 01- |           |     |          |        |
|            |                              | 51-   |        |     | 01-       | 01- |          |        |
5 1 0 1 5 0 5- 01- 0 . 0 5 . 7 0 . 5 5 . 2 0 . 0 5 . 2 0 . 5 5 . 7 0 . 0 0 1 5 0 5- 0 1 5 1 5 0 5 0 5 0 5 01 5 0 5 0 5 0 5 - 01- 0 2 5 1 0 1 5 0 5 - 0 1 5 1 01 5 0 5 - 0 1- 51-
|     | 1   | - - - 1 - | - - 1 1 | - 1 - 1 - | - 1- |     | - -      |           |
| --- | --- | --------- | ------- | --------- | ---- | --- | -------- | --------- |
|     |     | 01        | 51      | 51        |      | 51  | 8        |           |
|     | 01  |           | 01      |           | 01   | 01  | 6        | 51015     |
|     |     | 5         |         | 01        |      |     | 4        |           |
|     | 5   |           | 5       | 5         | 5    | 5   | 2        |           |
|     | 0   | 0         |         |           | 0    |     | 0        | 0         |
|     |     | 5-        | 0       | 0         |      | 0   | 2-4-6-8- | 5-        |
|     | 5-  |           | 5-      | 5-        | 5-   | 5-  |          | 01-51-02- |
|     | 01- | 01-       |         |           | 01-  |     |          |           |
|     |     |           | 01-     | 01-       |      | 01- |          |           |
|     |     | 51-       |         |           | 51-  |     |          |           |
0 1 5 0 5 - 01- 0 1 5 0 5 - 0 1- 5 1 0 1 5 0 5 - 0 1- 0 1 5 0 5 - 0 1 5 1 01 5 0 5 - 0 1- 0 1 5 0 5 - 01- 5 1 0 1 5 0 5 - 0 1 - 5 1 - 0 2 - 6 4 2 0 2 - 4 - 6-
|     |           |     |        | 30 - - |           |     |        |     |
| --- | --------- | --- | ------ | ------ | --------- | --- | ------ | --- |
|     | BrainWave |     | LaBraM |        | BrainBERT |     | MOMENT |     |
5.70.55.20.05.2-0.5-5.7-0.01-
|        | 5101      | 01    | 025101   |     | 8         | 6   | 51  | 01  |
| ------ | --------- | ----- | -------- | --- | --------- | --- | --- | --- |
|        |           |       |          |     | 6         |     | 01  |     |
|        | 5         | 5     |          |     | 4         | 4   |     | 5   |
|        | 0         | 0     | 5        |     | 2         | 2   | 5   |     |
|        | 5-        |       | 0        |     | 02-4-6-8- | 0   | 0   | 0   |
|        |           | 5-01- |          |     |           |     |     | 5-  |
|        | 01-51-02- |       | 5-01-51- |     |           | 2-  | 5-  |     |
| 46-DDM |           | 51-   |          |     |           | 4-  | 01- | 01- |
51-
5 . 2 0 . 0 5 . 7 0 . 5 5. 2 0 . 0 5 . 2- 0 . 5 5 . 7 0 . 0 5 . 7 0 . 5 5. 2 0 . 0 5 . 2 0 . 5 5 . 7 0 . 5 . 0 . 5 . 0 . 5 . 0 . 5 . 0 2 5 1 0 1 5 0 5 - 0 1 5 1 8 6 4 2 0 2 4 6 5 0 5. 0 5 0 5.7- 6- 01 5 0 5 0 5 . 0 . 5 . 0 . 5 . 0 . 5 . 0 . 5.7-
1 1 - - 1 - - - 0 1 7 5 2 0 2 - 5 - 7 - - - - - - . 7 . 5 2 . 0 . 2 - . 5 - - 1- 2 1 0 1 7 5 2 0 2 - 5 -
5.210.015.70.55.20.05.2-0.5-5.7- 8 01 8 5.70.55.20.05.2-0.5-5.7- 01 01
|     |     | 6      |           | 0251015  | 6      |     |     |     |
| --- | --- | ------ | --------- | -------- | ------ | --- | --- | --- |
|     |     | 4      | 5         |          | 4      |     | 5   | 5   |
|     |     | 2      | 0         |          |        |     |     |     |
|     |     | 0      |           |          | 2      |     | 0   | 0   |
|     |     |        | 5-        | 0        | 0      |     | 5-  |     |
|     |     | 2-4-6- | 01-51-02- | 5-01-51- | 2-4-6- |     |     | 5-  |
|     |     |        |           |          |        |     | 01- | 01- |
5 0 5 0 5 01- 0 5 0 5 0 5 0 5 0 0 5 0 5 0 0 8 6 4 2 0 2 4 6 5 0 5 0 5 0 5 0.01-
1 1 - 2 1 1 - 1 - 1 - 2 - 1 - 1- 1 - - - 6 4 2 0 2 - 4 - 6 - 8 - 8 6 4 2 0 2 - 4 - 6 - 8 - 01 5 0 5 - 0 1- . 7 . 5 . 2 . 0 . 2 - . 5 - . 7 -

|     | BrainWave | BrainWave-iEEG | BrainWave-EEG |           |
| --- | --------- | -------------- | ------------- | --------- |
|     |           | P < 0.001      | P = 0.200     |           |
|     | P < 0.001 |                |               | P = 0.033 |
| 1.0 | 1.0       | 1.0            | 1.0           | 1.0       |
P < 0.001
| CORUA 0.8 | 0.8           | 0.8        | 0.8         | 0.8           |
| --------- | ------------- | ---------- | ----------- | ------------- |
| 0.6       | 0.6           | 0.6        | 0.6         | 0.6           |
| 0.4       | 0.4           | 0.4        | 0.4         | 0.4           |
| AD-65     | CHB-MIT       | Absence-16 | Mayo-Clinic | FNUSA         |
|           |               | P < 0.001  | P < 0.001   |               |
| 1.0       | 1.0 P < 0.001 | 1.0        | 1.0         | 1.0 P = 0.002 |
P < 0.001
| CCAB 0.8 | 0.8     | 0.8        | 0.8         | 0.8   |
| -------- | ------- | ---------- | ----------- | ----- |
| 0.6      | 0.6     | 0.6        | 0.6         | 0.6   |
| 0.4      | 0.4     | 0.4        | 0.4         | 0.4   |
| AD-65    | CHB-MIT | Absence-16 | Mayo-Clinic | FNUSA |
P = 0.003
| P < 0.001 |                | P < 0.001        |            |            |
| --------- | -------------- | ---------------- | ---------- | ---------- |
| 1.0       | 1.0            | 1.0              | 1.0        | 1.0        |
|           | P < 0.001      |                  |            | P < 0.001  |
| CORUA 0.8 | 0.8            | 0.8              | 0.8        | 0.8        |
| 0.6       | 0.6            | 0.6              | 0.6        | 0.6        |
| 0.4       | 0.4            | 0.4              | 0.4        | 0.4        |
| MDD-64    | Depression-122 | Schizophrenia-28 | ADHD-Adult | ADHD-child |
P < 0.001
| 1.0 P = 0.017 | 1.0 | 1.0 P < 0.001 | 1.0 |     |
| ------------- | --- | ------------- | --- | --- |
1.0
P < 0.001
P < 0.001
| 0.8 | 0.8 | 0.8 | 0.8 | 0.8 |
| --- | --- | --- | --- | --- |
CCAB
| 0.6    | 0.6            | 0.6              | 0.6        | 0.6        |
| ------ | -------------- | ---------------- | ---------- | ---------- |
| 0.4    | 0.4            | 0.4              | 0.4        | 0.4        |
| MDD-64 | Depression-122 | Schizophrenia-28 | ADHD-Adult | ADHD-child |
Fig.A6 Performanceofcross-subjectevaluationwithBrainWave,BrainWave-EEGand
BrainWave-iEEG.BarplotscomparingtheAUROCandBACCscoresofBrainWave,BrainWave-
EEG and BrainWave-iEEG on cross-subject tasks. Each experiment is conducted with n-fold cross
validation(nisthenumberofsubjectgroups),wherewerepeatfiverunsforeachfold.
31

|     |       |     | BrainWave |     | BrainWave-iEEG |     | BrainWave-EEG |     |       |
| --- | ----- | --- | --------- | --- | -------------- | --- | ------------- | --- | ----- |
|     | AD-65 |     | CHB-MIT   |     | Absence-16     |     | Mayo-Clinic   |     | FNUSA |
| 1.0 |       | 1.0 |           | 1.0 |                | 1.0 |               | 1.0 |       |
| 0.8 |       | 0.8 |           | 0.8 |                | 0.8 |               | 0.8 |       |
CCAB
| 0.6 |     | 0.6 |     | 0.6 |     | 0.6 |     | 0.6 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.4
| 0.4 |               |     |                | 0.4 |               | 0.4 |               | 0.4 |                  |
| --- | ------------- | --- | -------------- | --- | ------------- | --- | ------------- | --- | ---------------- |
|     | 3-shot 8-shot |     | 3-shot 8-shot  |     | 3-shot 8-shot |     | 3-shot 8-shot |     | 3-shot 8-shot    |
|     | MDD-64        |     |                |     | ADHD-Adult    |     | ADHD-Child    |     | Schizophrenia-28 |
| 1.0 |               | 1.0 | Depression-122 | 1.0 |               | 1.0 |               | 1.0 |                  |
| 0.8 |               |     |                | 0.8 |               | 0.8 |               | 0.8 |                  |
0.8
CCAB
0.6
| 0.6 |     | 0.6 |     | 0.6 |     |     |     | 0.6 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.4
| 0.4 |               | 0.4 |               | 0.4 |               |     |               | 0.4 |               |
| --- | ------------- | --- | ------------- | --- | ------------- | --- | ------------- | --- | ------------- |
|     | 3-shot 8-shot |     | 3-shot 8-shot |     | 3-shot 8-shot |     | 3-shot 8-shot |     | 3-shot 8-shot |
Fig. A7 Performance of few-shot classification with BrainWave, BrainWave-EEG and
BrainWave-iEEG. Box plots comparing the BACC scores of BrainWave, BrainWave-EEG and
BrainWave-iEEGonfew-shotclassification.Weperform3-shotand8-shotclassificationforeachtask.
Dataaremean±SD.ThelistedpvalueindicatesthesignificanceforBrainWaveoutperformingthe
bestcomparisonmodel,withthetwo-sidedt-test.
32