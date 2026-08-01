1
Multimodal Brain-Computer Interface for In-Vehicle
Driver Cognitive Load Measurement: Dataset and
Baselines
Prithila Angkan, Behnam Behinaein, Zunayed Mahmud, Anubhav Bhatti, Dirk Rodenburg, Paul Hungler, Ali
Etemad, Senior Member, IEEE
Abstract—Through this paper, we introduce a novel driver In order to reduce the number of road accidents caused by
cognitiveloadassessmentdataset,CL-Drive,whichcontainsElec- high cognitive load, recent intelligent technologies integrated
troencephalogram (EEG) signals along with other physiological
into vehicles should possess the ability to measure cognitive
signals such as Electrocardiography (ECG) and Electrodermal
load and alarm the user should dangerously high amounts of
Activity (EDA) as well as eye tracking data. The data was
collected from 21 subjects while driving in an immersive vehicle it be detected. Brain-computer interfaces (BCI) have recently
simulator, in various driving conditions, to induce different gained traction in providing advanced means of communi-
levels of cognitive load in the subjects. The tasks consisted of cation between humans and machines. In particular, head-
9 complexity levels for 3 minutes each. Each driver reported
worn Electroencephalogram (EEG) devices allow for non-
their subjective cognitive load every 10 seconds throughout
invasiveyetaccuratehuman-machineinteractions.Tothisend,
the experiment. The dataset contains the subjective cognitive
load recorded as ground truth. In this paper, we also provide machine learning and deep learning techniques can be used
benchmark classification results for different machine learning to learn from datasets with various types of driver-related
and deep learning models for both binary and ternary label signals (including EEG). Additionally, these datasets require
distributions. We followed 2 evaluation criteria namely 10-fold
quantitativecognitiveloadscorestobemeasuredandprovided
and leave-one-subject-out (LOSO). We have trained our models
at frequent intervals, so that they could be used to train the
on both hand-crafted features as well as on raw data. We make
our dataset public to contribute to the field. machinelearningmodels.Whileanumberofrelevantdatasets
have been collected and published in recent years [9], [10],
Index Terms—Driver, cognitive load, wearables, brain-
[11], [12], [13], a number of problems persist. First, while
computer interfaces, deep learning.
a number of datasets for cognitive load do exist, they have
often been captured in non-vehicle scenarios. In fact, to our
I. INTRODUCTION
knowledge, only [9] has studied cognitive load in the context
A large number of accidents and collisions occur on the of driving.Second, the cognitive load ground-truth scores in
roadseveryyear.Whilemanyoftheseaccidentsarecausedby most existing datasets are generally sparse, and have been
distracteddrivers,forinstanceduetodistractionordrowsiness measured several minutes apart or upon task completion [12],
[1]. Distraction, meanwhile, can be caused by a number of [13]. This in turn makes training of machine learning models
personalorambientfactors,includinghighcognitiveloaddue more difficult and less accurate. Third, while most existing
toengagementwithsecondarytasks[2],[3],[4].Overthepast datasets on cognitive load are in fact ‘multimodal’, the notion
severalyears,muchresearchhasbeenconductedtoinvestigate of BCI with auxiliary wearable signals has not been widely
the effects of cognitive load and cognitive fatigue. Studies explored [9], [10], [11], [12], [13]. Lastly, in most existing
have demonstrated that prolonged engagement in cognitively works in the area, the focus has been solely on cognitive load
demanding tasks may lead to cognitive fatigue, a condition or distraction caused by task-irrelevant activities, overlooking
that could pose risks [5], [6]. Cognitive load refers to the the fact that performing the main task itself (in our case,
quantity of information our working memory can process at driving) can be a strong source of high cognitive load.
a given time. In other words, it is the amount of cognitive In this paper, we introduce a novel driver cognitive load
resources required to accomplish a task. In general, two assessment dataset containing EEG signals along with other
categories of cognitive load, intrinsic and extraneous, have physiological signals such as Electrocardiography (ECG) and
been described in the literature [7]. While intrinsic cognitive Electrodermal Activity (EDA) as well as eye tracking data.
load is defined as the inherent complexity of a given task, This dataset, which we name CL-Drive, is collected from
extraneous cognitive load refers to the cognitive resources 21 subjects while driving in an immersive vehicle simulator
demanded by environmental factors that are task-irrelevant in diverse situations capable of inducing various levels of
[7]. The success or failure in performance toward a particular cognitive load in the subjects. Each subject performs driving
task, on the other hand, is influenced by the amount of tasks in 9 complexity levels for 3 minutes each and reports
cognitive load experienced by the person performing the task their subjective cognitive load every 10 seconds throughout
[8]. If the cognitive load increases beyond a certain point, the experiment as ground-truth cognitive load labels. In this
the individual’s performance will degrade, which in case of paper, we also provide benchmark classification results for
driving may increase the likelihood of road accidents. differentmachinelearninganddeeplearningmodels.Bothraw
3202
ceD
12
]GL.sc[
2v37240.4032:viXra

2
signals as well as popular features supported by the literature TABLE I: PAAS subjective cognitive load scores used in this
study.
havebeenusedasinputs.Wefollowtwoimportantevaluation
| criteria, | namely 10-fold |     | and leave-one-subject-out |     |     | (LOSO). |     |                |     |             |     |     |     |
| --------- | -------------- | --- | ------------------------- | --- | --- | ------- | --- | -------------- | --- | ----------- | --- | --- | --- |
|           |                |     |                           |     |     |         |     | PAASSubjective |     | Description |     |     |     |
Our benchmarking demonstrates that cognitive load induced CognitiveLoadScores
by driving can be measured with reasonable accuracy using 1 Very,verylow
|         |           |          |          |     |     |     |     | 2   |     | Verylow |     |     |     |
| ------- | --------- | -------- | -------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
| EEG and | auxiliary | wearable | signals. |     |     |     |     |     |     |         |     |     |     |
|         |           |          |          |     |     |     |     | 3   |     | Low     |     |     |     |
Our contributions in this paper are summarized as follows: 4 Ratherlow
We collect and release a dataset, CL-Drive, that can 5 Neitherlownorhigh
•
allow researchers to evaluate driving-induced cognitive 6 High
|                                                  |                 |     |           |     |     |     |     | 7   |     | Ratherhigh    |     |     |     |
| ------------------------------------------------ | --------------- | --- | --------- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- |
| load,whichcanbeusefulfordevelopingautomatedalarm |                 |     |           |     |     |     |     | 8   |     | Veryhigh      |     |     |     |
| systems                                          | for intelligent |     | vehicles. |     |     |     |     | 9   |     | Very,veryhigh |     |     |     |
• CL-Driveprovidesdatafromvariousmodalitiesincluding
| EEG, | ECG, EDA | and | Gaze, | which is | a rich | source for |     |     |     |     |     |     |     |
| ---- | -------- | --- | ----- | -------- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
training machine learning systems capable of performing secondary tasks such as using mobile phones or performing
someotherin-vehicleactivities[2],[27],[28],[3],[29].In[2],
| cognitive | load | assessment. | To  | the best | of our | knowledge, |     |     |     |     |     |     |     |
| --------- | ---- | ----------- | --- | -------- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
thisisthefirstandonlydatasettocollectdrivercognitive the cognitive load of drivers was measured when the drivers
|      |               |      |              |     |     |     | were involved |     | in verbal | conversation | and | word games | while |
| ---- | ------------- | ---- | ------------ | --- | --- | --- | ------------- | --- | --------- | ------------ | --- | ---------- | ----- |
| load | ratings along | with | bio-signals. |     |     |     |               |     |           |              |     |            |       |
• CL-Drive contains dense and frequent subjective ratings driving.Asaresult,thecognitiveloadinducedwasduetothe
whicharespreadonly10seconds,allowingformorereli- combination of both primary as well as secondary tasks. A
|      |              |           |           |     |                  |     | remote | eye tracker | was | used to measure |     | the pupil | size of all |
| ---- | ------------ | --------- | --------- | --- | ---------------- | --- | ------ | ----------- | --- | --------------- | --- | --------- | ----------- |
| able | and frequent | automated | cognitive |     | load measurement |     |        |             |     |                 |     |           |             |
by learned models. 32participantswhichinturnwasusedtoestimatethecognitive
loadoftheparticipants.Thegroundtruthwastheperformance
| The rest | of this | paper is | summarized | as  | follows. | In Section |     |     |     |     |     |     |     |
| -------- | ------- | -------- | ---------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
II, we first provide a study of cognitive load followed by measureswhichtheycalculatedusinglanepositionanddegree
an overview of the publicly available cognitive load datasets of rotation of the steering wheel, and subsequently evaluated
|              |               |     |          |         |              |     | the relationship |     | between | the change | in  | pupil diameter | and |
| ------------ | ------------- | --- | -------- | ------- | ------------ | --- | ---------------- | --- | ------- | ---------- | --- | -------------- | --- |
| that contain | physiological |     | signals. | Section | III explains | the |                  |     |         |            |     |                |     |
experimental setup, including sensor configurations, driving driving performance.
|           |          |           |                  |     |     |              | In [30], | the | non-driving | task of | reading | was performed | by  |
| --------- | -------- | --------- | ---------------- | --- | --- | ------------ | -------- | --- | ----------- | ------- | ------- | ------------- | --- |
| simulator | details, | cognitive | load assessment, |     | and | data collec- |          |     |             |         |         |               |     |
tionprotocol.Next,wediscussthedatapre-processing,feature 18 participants in a fully automated vehicle. Two peripheral
extraction, normalization, and baseline classifiers in section information systems, one utilizing the visual modality and
|     |     |     |     |     |     |     | the other | the haptic | modality, | were | assessed | to examine | their |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --------- | ---- | -------- | ---------- | ----- |
IV.Lastly,inSectionVweprovidetheresultsanddiscussions.
|              |      |                 |     |     |     |     | impact    | on situational |          | awareness,   | mental    | workload,           | viewing |
| ------------ | ---- | --------------- | --- | --- | --- | --- | --------- | -------------- | -------- | ------------ | --------- | ------------------- | ------- |
|              |      | II. RELATEDWORK |     |     |     |     |           |                |          |              |           |                     |         |
|              |      |                 |     |     |     |     | behavior, | and            | reading  | performance. | In        | [31], a three-phase |         |
| A. Cognitive | Load | Measurement     |     |     |     |     |           |                |          |              |           |                     |         |
|              |      |                 |     |     |     |     | framework | was            | proposed | that allows  | effective | diagnosis           | of      |
Priorresearchhasshownthatmeasuringcognitiveloadfrom driver’s visual and comprehension loads in traffic scenes.
Driversfromdiversebackgroundswereassessedforvisualand
| physiological | signals | [14], | [15] continues |     | to be | a challeng- |     |     |     |     |     |     |     |
| ------------- | ------- | ----- | -------------- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
ing task [16], [17]. There are both subjective and objective comprehension load while driving simulations across various
trafficscenarios.Anotherpaper,[32],studiedtheeffectofsafe
| measures | that are | commonly | used | to evaluate | cognitive | load |     |     |     |     |     |     |     |
| -------- | -------- | -------- | ---- | ----------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
levels that involve: (i) self-reporting, (ii) dual-task measures, takeovertransitioninconditionallyautomateddrivingandused
and (iii) physiological measures [18]. The PAAS scale [19], XGBoost to evaluate their work using a dataset from a meta-
analysis study.
| shown in | Table I | is most | commonly | used | for self-reported |     |     |     |     |     |     |     |     |
| -------- | ------- | ------- | -------- | ---- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
subjective cognitive load labels. The National Aeronautics Drivingperformancewhileinteractingwithaportablemusic
and Space Association Task Load Index (NASA-TLX) [20] player was evaluated in [27]. It was observed during a multi-
is also commonly used as a self-reporting tool. Dual-task sessionsetup,thatthecognitiveloadoftheparticipantsduring
measurement involves the individual performing two tasks the first sessions was higher, hence the driving performance
at the same time. One way of designing this is to measure (e.g., perception response time (PRT) while braking and over-
knowledge gain from one task and response time for the allcontrolofthevehicle),waslowerincomparisontothelater
other task [21]. In [22], another way of implementing dual- sessions. The experiment was carried out on 19 participants
task measurement was explored, which was by performing using simulated vehicle. Next, in [28], the high cognitive load
a continuous secondary task while learning the primary task. of drivers was evaluated using EEG signals in 3 different
|     |     |     |     |     |     |     | driving | conditions, | namely: | no secondary |     | task (baseline), | low |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | ------- | ------------ | --- | ---------------- | --- |
Thereareseveralphysiologicalparametersthathavealsobeen
used as cognitive load measures in the past. This includes cognitiveloadtask,andhighcognitiveloadtask.Thelowand
variationinpupildiameterandblinkrate[23],[24],heartrate high cognitive load tasks were based on N-back tasks used
variability [25], and electrocardiogram (ECG) [26] to name a in [33], [34]. GSR, eye tracking, respiration rate (RR), and
few. accelerator release time (ART) data were collected during the
|              |      |            |     |     |     |     | experiments. | The        | data | was collected | from | 37 participants | in  |
| ------------ | ---- | ---------- | --- | --- | --- | --- | ------------ | ---------- | ---- | ------------- | ---- | --------------- | --- |
| B. Cognitive | Load | in Driving |     |     |     |     |              |            |      |               |      |                 |     |
|              |      |            |     |     |     |     | a vehicle    | simulator. | The  | NASA-TLX      | was  | used to collect | the |
In the area of driving, prior works have studied cognitive participants subjective rating at the end of the experiment. In
load mainly in the context of the driver being engaged by [3], the cognitive load of participants was evaluated using eye

3
TABLE II: Existing datasets in the literature that study cognitive load using physiological signals.
| Dataset |     | Year | Sub. | MentalState |     |     | Modalities |     |     |     | Stimuli |     |     |
| ------- | --- | ---- | ---- | ----------- | --- | --- | ---------- | --- | --- | --- | ------- | --- | --- |
DriverWorkload[9] 2013 10 Mentalworkloadofthedriver ECG,BTemp,SCR Watching driving videos, Driving
inrealenvironment
MMOD-COG[10] 2019 40 Cognitiveload ECG,EDA,Speech Arithmetic,Reading
CLAS[11] 2019 62 Cognitive Load, negative emotion ECG,PPGandEDA Math problems, Logic problems
|     |     |     |     | andmentalstress |     |     |     |     |     |     | andStrooptest |     |     |
| --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- |
CogLoad[12] 2020 23 Cognitiveload,Personalitytraits heart rate, beat to beat interval, Different cognitive load tasks (2-
|     |     |     |     |     |     |     | EDA,ST,andACC |     |     |     | back and | 3-back tasks, | visual cue |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | -------- | ------------- | ---------- |
tasketc.)
Snake[12] 2020 23 Cognitiveload heart rate, beat to beat interval, Snakegameonasmartphone
EDA,ST,andACC
| Kalatzisetal.[13] |     | 2021 | 26  | Cognitiveload |     |     | ECG,RR |     |     |     | MATB-II |     |     |
| ----------------- | --- | ---- | --- | ------------- | --- | --- | ------ | --- | --- | --- | ------- | --- | --- |
CL-Drive(ours) 2023 21 Cognitiveload EEG,ECG,EDA,Gaze Driving a simulated vehicle in
scenarioswithvariouscomplexity
levels
video data extracted from facial videos during driving. Three [49]. Prior research has also shown significant correlation
different N-back tasks were used as secondary tasks, which betweenchangesinpupilsize,blinkrate,saccade,andfixation
were also used to quantify the ground truth levels. Hidden with cognitive load [50], [51].
| Markov models | and | 3D-CNN | were | then | used to | evaluate the |     |     |     |     |     |     |     |
| ------------- | --- | ------ | ---- | ---- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
result.Inanotherpaper[29],thecognitiveloadofparticipants
|               |               |         |     |               |     |              | D. Public | Cognitive | Load | Datasets |     |           |           |
| ------------- | ------------- | ------- | --- | ------------- | --- | ------------ | --------- | --------- | ---- | -------- | --- | --------- | --------- |
| was evaluated | while         | driving | and | performing    | a   | 1-back task. |           |           |      |          |     |           |           |
|               |               |         |     |               |     |              | Previous  | research  | has  | examined | the | induction | of cogni- |
| EEG data      | was collected | from    | 36  | participants. | To  | evaluate the |           |           |      |          |     |           |           |
performance, case-based reasoning classifiers were used [35]. tive load in drivers with a subsequent evaluation of driving
|     |     |     |     |     |     |     | performance | under | varying | cognitive |     | load levels | [52], [53]. |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ------- | --------- | --- | ----------- | ----------- |
Afewotherpriorworkssuchas[2],[27],[28]haveusedmore
|                   |     |       |               |     |         |                 | Some other | publications |     | have | studied | cognitive | load under a |
| ----------------- | --- | ----- | ------------- | --- | ------- | --------------- | ---------- | ------------ | --- | ---- | ------- | --------- | ------------ |
| simple approaches |     | based | on predefined |     | metrics | (e.g., required |            |              |     |      |         |           |              |
time to break, degree of motion of the steering wheel, etc.) to variety of different experimental setups [54], [26]. There is
|                   |     |           |               |     |          |     | evidence | that affect | and | cognitive | load | are interrelated | and |
| ----------------- | --- | --------- | ------------- | --- | -------- | --- | -------- | ----------- | --- | --------- | ---- | ---------------- | --- |
| measure cognitive |     | load from | physiological |     | signals. |     |          |             |     |           |      |                  |     |
Besidescognitiveload,otherfactorssuchasdriveremotions affect has a significant impact on cognitive load [55]. Though
awiderangeofstudieshavebeendonetostudytheimpactof
[36],[37],[38]andvigilance[39],[40],[41],havebeenwidely
|            |                 |     |       |       |           |          | affect on | EEG [56], | [57], | the available |     | datasets | for cognitive |
| ---------- | --------------- | --- | ----- | ----- | --------- | -------- | --------- | --------- | ----- | ------------- | --- | -------- | ------------- |
| studies in | the literature. |     | While | these | works may | maintain |           |           |       |               |     |          |               |
some similarities to works on cognitive load, they are in fact load are indeed quite limited. In this section, we provide an
|                  |            |     |       |             |     |               | overview | of the publicly |     | available | datasets | for | cognitive load |
| ---------------- | ---------- | --- | ----- | ----------- | --- | ------------- | -------- | --------------- | --- | --------- | -------- | --- | -------------- |
| different driver | attributes |     | which | are outside | the | scope of this |          |                 |     |           |          |     |                |
study. Moreover, the notions of affect and distraction have with physiological signals. Table II presents a summary of
these datasets.
| been more  | widely    | studied  | for drivers, | as  | opposed | to cognitive |            |          |     |         |               |            |      |
| ---------- | --------- | -------- | ------------ | --- | ------- | ------------ | ---------- | -------- | --- | ------- | ------------- | ---------- | ---- |
|            |           |          |              |     |         |              | The Driver | Workload |     | dataset | [9], provides | multimodal | data |
| load which | is a less | explored | area.        |     |         |              |            |          |     |         |               |            |      |
toevaluatedriverworkloadusingECG,bodytemperature,and
|     |     |     |     |     |     |     | skin conductance |     | response | (SCR). | The | dataset | was collected |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------- | ------ | --- | ------- | ------------- |
C. BCI
|     |     |     |     |     |     |     | from 10 | participants | with | the | goal of | evaluating | cognitive |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | ---- | --- | ------- | ---------- | --------- |
BCI systems can communicate the neural activities in the load of drivers on different types of roads and in different
brain directly with an external device [8], [42]. Research driving environments. In addition to the physiological signals,
has shown that BCI can play a vital role in interpreting two cameras were also used to record the driving route as
the cognitive load induced while driving [8], [42]. This is well as the participant’s facial videos. The video data were
|            |           |     |                 |     |       |               | not made | public | for privacy | purposes. | The | data | was collected |
| ---------- | --------- | --- | --------------- | --- | ----- | ------------- | -------- | ------ | ----------- | --------- | --- | ---- | ------------- |
| due to the | fact that | the | fronto-parietal |     | brain | regions along |          |        |             |           |     |      |               |
with sub-cortical regions can be engaged while experiencing as the participants drove the car for 30 minutes. Participants
varyingamountsofcognitiveload[43].EEG,isanon-invasive subjective ratings were collected by watching videos of their
method which measures the potential difference caused by own driving at the end of the activity.
the electrical activity in the brain [44], [45]. This property The MMOD-COG [10] dataset was recorded from 40 dif-
of EEG allows it to capture changes in brain activity while ferent subjects for cognitive load assessment during reading
experiencing variations in cognitive load, which makes it a and arithmetic tasks. ECG and EDA were recorded from the
verygoodcandidateforcognitiveloadevaluation.Multimodal subjects in addition to speech. The experiment was divided
approaches have proven effective at magnifying the accuracy into reading and arithmatic segments where in the reading
of cognitive load assessment in the past [46]. Apart from segment, two separate digits were shown for 5 seconds and
EEG, research has shown that both the sympathetic nervous repeatedwithdifferentdigits20times.Thearithmeticsegment
system (SNS) which controls the skin conductance response wasdividedintohighandlowcognitiveloadlevelsandatotal
and automatic nervous system which controls the heart rate of 40 problems were asked to be solved by each participant.
variability (HRV) are impacted by cognitive load [47], [48], The CLAS dataset [11] was collected from 62 participants

4
andwasobtainedbyrecordingvariouscognitiveloadlevelsin- EEG. For collecting EEG signals the Muse S1 headband
ducedbytaskssuchasmathematicsandlogicproblemsaswell shown in Figure 1a is used. The device has 4 channels where
as the Stroop test [58]. In addition to cognitive load, audio- 2 of them are frontal electrodes located at the forehead in
visual stimuli were used to induce emotional variations in locations AF7 and AF8 (according to the international 10-
the participants. Physiological data was collected using ECG, 20 system [61], [62]) while the remaining 2 are temporal
Plethysmography(PPG),EDA,andaccelerometer(ACC)data. electrodes located behind the ears in locations TP9 and TP10.
Thenextdataset,CogLoad[12]wasalsoamultimodaldataset Figure1adepictstheMuseEEGdevicewhileinFigure2a,we
with23participantswhoperformed6differentcomputertasks presentthesensorlocationsofthisEEGheadset.Asshownin
duringthecollectionprocess.Thephysiologicaldatacollected the figure, the reference electrode is located at the middle of
was heart rate, beat to beat interval, EDA, skin temperature the forehead in location FpZ. The sampling rate of the EEG
(ST),andACC.Thetaskwasdividedintotwosegmentswhere headband is 256 Hz. Conductive gel is used to enhance the
the first segment involved understanding the participant’s de- conductivity between the electrode and the skin. We opt for
gree of cognitive resources and their personality traits using theMuseSheadbandtoensurebothcomfortandcompatibility
two N-back tasks [12], [59]. Whereas, in the second segment, with the gaze device.
6 different tasks that required varying levels of cognitive load ECG. ECG signals are collected through the Shimmer2 sen-
were performed. In addition, in order to completely occupy sors [63], which is shown in Figure 1b. As depicted in Figure
the cognitive resources of the participants, a secondary task 2b, this wearable device uses 5 standard pre-gelled adhesive
was also given to them to perform. electrodes from the chest and abdominal area. Among the 4
Another multimodal dataset consisting of heart rate, EDA, electrodes,theRightArm(RA)andLeftArm(LA)areplaced
ST, and ACC was collected from 23 participants while they on the left and right sides of the manubrium, while Right
played the Snake game on a smartphone [12]. This dataset Leg (RL) and Left Leg (LL) are placed right above the lower
named Snake [12], was collected with varying cognitive load costalmargin.ThereferenceelectrodedenotedbyVxisplaced
levels where the amount of cognitive load experienced by the slightly on the right of the sternum. The signals collected are
participantswascontrolledbythechangingspeedofthegame. LL-RA, LA-RA, and Vx-RA at a sampling frequency of 512
The task consisted of 3 complexity levels, high, medium and Hz. The Shimmer is worn by the participants using a belt and
| low, which       | lasted 2 minutes |     | each. After | the      | task completion, |     | a cradle.    |     |      |     |            |     |           |         |
| ---------------- | ---------------- | --- | ----------- | -------- | ---------------- | --- | ------------ | --- | ---- | --- | ---------- | --- | --------- | ------- |
| the participants | answered         | the | NASA        | TLX [20] | questionnaire    |     |              |     |      |     |            |     |           |         |
|                  |                  |     |             |          |                  |     | EDA. Similar | to  | ECG, | the | EDA signal | is  | collected | using a |
along with two other 7-point Likert scale questions. Finally, Shimmer wearable device [63] as shown in Figure 1c. The
Kalatzis et al. [13] presented a dataset that has been collected data is collected using 2 electrodes placed on the left side
from 26 participants. In this dataset, the cognitive load of the of the abdomen which is shown in Figure 2c. The sampling
participantswasassessedusingECGandrespirationrate(RR) frequency of the EDA Shimmer device is 128 Hz
data. High and low cognitive load data were collected as the device3
|     |     |     |     |     |     |     | Gaze Figure | 1d  | shows | a Tobii |     | used | to  | collect eye |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | ------- | --- | ---- | --- | ----------- |
participants used the MATB-II software [60] while the NASA tracking data. The device is comprised of a head unit and a
TLX[20]questionnairewasusedtocollectgroundtruthvalues recording unit. Inside the device there are 2 cameras per eye
for the two cognitive load levels. as well as a wide angle scene camera. From the eye tracking
In contrast to the above, our dataset considers driving to be device we record the specific eye movement events such as
the primary task and evaluates cognitive load induced while saccade, fixation, and others. The sampling frequency is 50
driving. Moreover, we record frequent subjective cognitive Hz. Figure 2d illustrates the placement of the eye tracking
load scores which is not the case in existing cognitive load device along with the EEG headset.
| datasets. | This allows    | us to perform | more    | accurate |     | evaluations |               |     |          |     |     |     |     |     |
| --------- | -------------- | ------------- | ------- | -------- | --- | ----------- | ------------- | --- | -------- | --- | --- | --- | --- | --- |
| and train | better machine | learning      | models. | Finally, |     | CL-Drive    |               |     |          |     |     |     |     |     |
|           |                |               |         |          |     |             | B. Experiment |     | Test-bed |     |     |     |     |     |
containsseveralmodalitiesthatenablemulti-modalstudieson
|           |       |     |     |     |     |     | In order           | to          | simulate | driving | and     | be able     | to      | control the |
| --------- | ----- | --- | --- | --- | --- | --- | ------------------ | ----------- | -------- | ------- | ------- | ----------- | ------- | ----------- |
| cognitive | load. |     |     |     |     |     |                    |             |          |         |         |             |         |             |
|           |       |     |     |     |     |     | parameters         | surrounding |          | the     | driving | experience, |         | we use a    |
|           |       |     |     |     |     |     | driving simulator4 |             | shown    | in      | Figure  | 3. The      | driving | simulator   |
III. EXPERIMENTSETUPANDDATACOLLECTION
|     |     |     |     |     |     |     | includes | elements | similar | to  | a real | car, | including | steering |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ------- | --- | ------ | ---- | --------- | -------- |
Inthissection,wediscusstheexperimentalprotocolusedin
|                   |               |           |            |             |                   |             | wheel, dashboard, |            | accelerator, |            | and      | brake.        | These         | components |
| ----------------- | ------------- | --------- | ---------- | ----------- | ----------------- | ----------- | ----------------- | ---------- | ------------ | ---------- | -------- | ------------- | ------------- | ---------- |
| the study.        | This includes | specifics | on         | the setup   | for               | the sensors |                   |            |              |            |          |               |               |            |
|                   |               |           |            |             |                   |             | combined          | with       | a motion     | system     | provides |               | participants  | with       |
| and driving       | simulator     | as well   | as details | of          | the participants, |             |                   |            |              |            |          |               |               |            |
|                   |               |           |            |             |                   |             | a more realistic  |            | driving      | sensation. |          | The motion    |               | system can |
| diving scenarios, | and           | cognitive | load       | assessment. |                   |             |                   |            |              |            |          |               |               |            |
|                   |               |           |            |             |                   |             | emulate real-life |            | motions      | up         | to 100   | Hz            | in frequency. | This       |
|                   |               |           |            |             |                   |             | includes          | vibrations | from         | road       | texture, | acceleration, |               | braking,   |
A. Sensors speeding, and turning along with other essential movements
|        |                 |       |      |              |     |            | to provide | users | with engaging |     | haptic | feedback. |     | Additionally, |
| ------ | --------------- | ----- | ---- | ------------ | --- | ---------- | ---------- | ----- | ------------- | --- | ------ | --------- | --- | ------------- |
| During | the experiments | which | will | be described |     | in Section |            |       |               |     |        |           |     |               |
III-G, we use four different sensors to collect physiological there are three 55 inch LCD screens which provide a 180
| signals from | which to | measure | cognitive | load. | Following |     | is  |     |     |     |     |     |     |     |
| ------------ | -------- | ------- | --------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1https://choosemuse.com/muse-s/
| a description | of each | sensor | type, namely | EEG, | ECG, | EDA, |     |     |     |     |     |     |     |     |
| ------------- | ------- | ------ | ------------ | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
2https://shimmersensing.com/product/shimmer3-ecg-unit-2/
| and Gaze, | in detail. Figure |     | 1 shows | the sensors | used | in our |     |     |     |     |     |     |     |     |
| --------- | ----------------- | --- | ------- | ----------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
3https://www.tobiipro.com/product-listing/tobii-pro-glasses-2/
study, while Figure 2 shows their detailed sensors placement. 4https://viragesimulation.com/vs500m-car-simulator-training-and-research/

5
TP9
(a)EEGheadband (b)ECGdevice (c)EDAdevice (d)Eyetracker
Fig. 1: Wearable EEG, ECG, EDA, and Gaze devices.
AF7 AF8
FPZ RA LA
AF7 (ref.) AF8
FPZ Vx TP10 TP9
AF7 (ref.) AF8
TP9 TP10 Wearable EEG Wearable eye
TP9 TP10 headband tracker
RL LL
EDAE D1A 1
EDAE D2A 2
(a)EEG(a) (b) (Eb)CG (c)E(cD)A (d)EEGandGaze
Fig. 2: EEG, ECG, EDA, and Gaze electrode placements.
degree view from the front, plus two additional screens for
the blind spots, together creating an immersive experience.
Each front screen has a display resolution of 1920 × 1080
pixels. Moreover, directional sound is incorporated using a
surroundsoundsystem.Thesoundisintendedtomimictypical
sounds heard while driving including the sound of the engine,
speeding and passing vehicles, and horns, among others.
Adebriefstationisdesignedtoprovideacompletevideoof
the participant and simulation screens during the experiment
along with performance graphs. There is a webcam mounted
on the top of the middle frontal screen, which has a reso-
lution of 720p. The camera records video of the participants
while driving in the simulator. The performance information
displayed in the debrief station includes driving performance
data,includingthetimerequiredforbreakingandacceleration,
possible crashes, and others. This data can also be used for
Fig. 3: The immersive vehicle simulator used in this study.
performance analysis.
C. Driving Scenarios
Thesimulatorcomeswithanumberofpre-builtdrivingsce- theparticipantsbasedonanumberofpilotteststhatwecarried
nariosinwhichthevehicletype,environmentalconditions,and out to choose these 9 from among a larger pool of possible
other factors can vary. Each scenario consists of a number of tasks. Moreover, the scenarios are structured to progressively
tasksthatneedtobeperformed,e.g.,keepingthespeedabove increase in difficulty, yet remain achievable for the average
a certain threshold. Moreover, each scenario has a designated driver. In Figure 4, we depict the heat map of the frequency
complexity level. We choose 9 different scenarios, one from oftheratingsforeachdrivingscenario.Weobservethatasthe
each complexity level. The scenarios encompass a range of scenarios progress, more and more participants select higher
commonchallengesencounteredduringeverydaydriving,such cognitive load scores, indicating that the task complexities
asdrivingonhighways,atnight-time,andinsnowyconditions do indeed increase as the scenarios progress, especially for
(scenarios 1, 2, 3 respectively), maintaining/changing speed scenarios 8 and 9.
levels(scenarios4,5,6,7and9),avoidingaccidents(scenarios The duration of each scenario is set to 3 minutes. An
4, 5, 6, 7 and 9), back-to-back turns (scenario 7), and turning orientation scenario was designed and performed by each
the car around on a narrow road using 3-point turn (scenario participant at the beginning of the session to allow each
8). The scenarios induce different levels of cognitive load in participanttoadapttothesimulator.Intheorientationsession,

6
TABLE III: Driving scenario details
Scenario/
Simulation Description
Complexity
0/Orientation Highwaydriving Maintaincentre
1 Highwaydriving 80km/h
2 Nighttimedriving 80km/h
3 Nighttimedrivinginthehighwayw/snow 80km/h
4 Tennisballchallenge Hitthetennisballwiththetire,maintainaccuracy,trytoaccelerate
5 Slalomchallenge Navigatethroughgates,maintainaccuracy,trytoaccelerate
6 Narrowpassagechallenge Navigatethroughgates,maintainaccuracy,trytoaccelerate
7 90-degreeturnchallenge Take90degreesleftandrightturns,maintainaccuracy,trytoaccelerate
8 3-pointturnchallenge Drivewhilefollowinginstructions,take3pointturn
9 Narrowalleychallenge Navigatethroughnarrowalley,maintainaccuracy,trytoaccelerate
                 
 7 D V N  & R P S O H [ L W \
 V H U R F 6  G D R /  H Y L W L Q J R &  H Y L W F H M E X 6
 
 
 
 
 
 
 
 
 
Eye
TABLE IV: SAS levels and their corresponding deMscovreimpetniton.
SASLevel Description 3 Minutes
Baseline
                           1 Feelingnoadverseeffects
2 Feelingverymilddiscomfort
Orientation
                           3 Feelingmilddiscomfort
4 Feelingmildtomoderatediscomfort
                              5 6 F F e e e e l l i i n n g g m m o o d d e e r r a a t t e e d to is p co ro m n f o o u r n t ceddiscomfort 2 B M as i e n l u in te e s (0<N<10,N+1)
                               7 Feelingpronounceddiscomfort
Session N
8 Feelingpronouncedtoseverediscomfort
                          
    9 Feelingseverediscomfort(potentialforvomiting)
                         
  
(0<N<10,N+1)
                        
  
                         3 Minutes Orientation 2 Minutes 2 Minutes Session N
   Baseline Rest Baseline
                        
Fig. 5: The experiment flow.
 
Fig. 4: Complexity vs. subjective cognitive load scores. The
1) Cool room: the simulator room must be cool and well
lighter shade means more sample.
ventilated;
2) Confidentintroduction:mustcreateacalmandrelaxed
environment;
we described the system first as the system completes a
3) Cautious alert: moving on slowly to allow the driver’s
number of steps to ensure things like the turn signals, motion
time to adjust;
sensors,brake,accelerator,ignition,emergencystop,seatbelt,
4) Careful observation: must actively look for signs and
and others function properly. Participants then began to drive
symptoms of SAS;
onthehighwaytobecomefamiliarwiththespeeddisplay,on-
5) Cease driving: must pause immediately on observing
screenarrowthatprovidescuesaboutthedirectionofdriving,
the slightest sign of SAS.
and all the other necessary indicators, while we were present
SAS can be managed by carefully monitoring the partic-
to provide help if needed and answer any questions. Table III
ipant’s level of discomfort using a Likert scale and asking
shows the description of each driving scenario along with its
the participants to do an intermittent self assessment. In our
corresponding complexity level.
case, the participants were asked to self report on their SAS
level every minute using a 9-point Likert scale as shown in
D. Simulation Adaptation Syndrome Table IV, which was made based on the Motion Sickness
Questionnaire (MSQ) [69], Simulator Sickness Questionnaire
It has been shown in prior research that Simulation Adap-
(SSQ) [70], and The Motion Sickness Assessment Question-
tation Syndrome (SAS) can affect different participants [64],
naire (MSAQ) [71]. Based on these pre-cautions and careful
[65]. SAS can range from feeling minor discomfort to severe
monitoring, SAS resulted in pausing and discontinuing only 2
symptoms such as dry mouth, dizziness, vertigo, vomiting,
participants.
nausea, and disorientation while taking part in simulations
such as driving a vehicle [66]. The main cause of SAS is
E. Participants
the discrepancy between the sensory inputs such as visual
and vestibular system (which is responsible for our sense of Data was collected from 23 participants including 17 fe-
balance [67],[68]).Oneofthechallengeswefacedduringour malesand6males.Theparticipant’sgenderwasnotcontrolled
studywasavoidingandminimizingSAS.Asrecommendedin for and we merely included volunteers regardless. We did not
the simulator instructions, we followed the following 5 steps actively seek individuals of specific genders, as it was not
to manage and reduce SAS as much as possible: a prerequisite for our study. Given that the key focus of this

7
studyhasbeencognitiveloadduringdriving,wecontrolledfor cognitiveloadstate.Followedbytherestingperiod,a2-minute
havingadrivinglicenseandafewyearsofdrivingexperience. baseline was collected before each new scenario. The experi-
Wealsoensuredthatparticipantswerenotundertheinfluence ment flow is shown in Figure 5. During all these experiments,
of any substances at the time of data collection. The average the wearable sensors discussed earlier in Section III-A were
age of participants was 26.9. Background health information used to record the respective signals from the participants.
were not collected in this study. Figure 6 we illustrate a sample from each captured modality
Prior to the simulation, participants were provided with in both high and low cognitive load scenarios.
detailed information on the experimental process and the
research team received written consent. The study was ap-
H. Dataset Release
proved by Queen’s University’s General Research Ethics
We make the dataset public at:
Board (GREB). Among the 23 participants, 2 data collection
https://github.com/Prithila05/CL-Drive
sessions were stopped due to high levels of SAS, while the
data from another 3 sessions was incomplete due to device or
connectivity issues. Specifically, for participant 13, we only IV. DATAPROCESSING
have data for scenarios 3, 4, 5, 6, and 9, while for participant
In this section, we explain the data pre-processing steps
16, we have data for scenarios 1, 5, 6 and 9. Finally, for
for each signal type, followed by feature extraction. Next, we
participant18,wehavethedataforscenarios1to6.Whilethe
describedatanormalization,whichisfollowedbyadescription
data from the two sessions that were incomplete due to SAS
of the baseline classifiers used for benchmarking.
are not incorporated in the dataset as they were interrupted
too early in the process, the data from the three incomplete
A. Pre-processing
sessions are incorporated.
The cognitive load scores were collected at 10-second
intervals during the 3-minute driving scenarios. We segment
F. Cognitive Load Self-Assessment
each recording into 18 segments of 10 seconds each. These
Participantcognitiveloadself-assessmentratingswereused
segments will later be used for feature extraction or fed
asgroundtruthlabelsinthisstudy.AsshowninTableI,PAAS
directly into the deep learning models.
subjective cognitive load scores consist of 9 levels [72]. A
EEG. To remove noise and artifacts from EEG, we used
looping audio cue was generated every 10 seconds during the
a Butterworth 2nd order bandpass filter with a passband
experiments to prompt the participants to verbally report their
frequency of 0.4 to 75 Hz. A notch filter with a quality
cognitive load, and a member of the research team recorded
factor of 30, was used to remove the powerline noise at a
the reported scores. Figure 7 presents the distribution of the
frequency of 60 Hz. Due to some Bluetooth problems, the
recorded output scores for all the participants.
deviceexperiencedafewdisconnectionslastingapproximately
Regarding the frequency at which the responses were
30 seconds during the experiments. Given the duration of
recorded, we aimed to balance the frequency of labels for the
these gaps, using imputation methods would not be suitable.
purpose of training machine learning models, and ensuring
We therefore excluded segments with missing data from our
that the questions themselves did not impact the experiment
dataset.
significantly. Through a few pilot trials, 10 seconds was
ECG. Artifacts such as high-frequency noise, EMG noise,
found to be a reasonable interval, as longer intervals could
T noise interference, etc., were then filtered out using a
lead participants to forget their earlier experiences during
Butterworth bandpass filter with passband frequency of 5 to
that segment, while shorter intervals could interfere with the
15 Hz, which alsoenables us to obtain maximum QRS energy
experiment itself.
[73], [74]. The ECGsignals experiencedmissing valuesocca-
sionally,whichweimputedusingsimple5th orderpolynomial
G. Experiment Protocol
interpolation.
Participants were given clear descriptions about the data EDA. We then used a lowpass butterworth filter with a cut-
collection protocol and equipment. After careful sensor place- off frequency of 3 Hz to remove the unwanted noise. A
ment, participants were asked to sit in the driving seat of highpass butterworth filter with a cut-off frequency of 0.05
the simulator and the sensors were connected via Bluetooth Hz was used to decompose the filtered EDA signal to tonic
to a data collection station. First, 3 minutes of baseline data skin conductance level and phasic skin conductance response
was collected from each participant which could be used for to isolate the slow changing levels and rapid changing peaks
future normalization of the signals. To become adapted to the in the signal [75]. There were some missing values which we
simulateddrivingenvironmentandmakesurethatparticipants replaced with a sample-and-hold strategy given the simplicity
had a clear understanding about the ‘low’, ‘medium’, and of EDA signals in comparison to ECG.
‘high’ complexity levels, and also to reduce the SAS level, Gaze. The device measures saccade, fixation, pupil diameter,
participants were asked to perform the Orientation scenario blink count, and blink duration based on 2D gaze coordinates
mentioned earlier in Table III. Following every 3-minute (x,y pixel coordinates in screen space) for both left and right
driving scenario (see Table III), the participants were given eyes,3Dgazecoordinates(x,y,z coordinatesinmmincamera
a resting time of 2 minutes to allow them to rest, reduce space), 3D gaze direction (vector units), gaze velocity in
the possibility of SAS, and come back to a relatively lower degrees per second (◦/s), and gaze acceleration in degrees per

8
100
75
50
25
0
25
50
75
102089.00 289.25 289.50 289.75 290.00 290.25 290.50 290.75 291.00
Timestamp (sec)
)Vu(
laitneyoP
EEG
low cognitive load 7.5
high cognitive load 7.0
6.5
6.0
5.5
5.0
4.5
4.0
125 126 127 128 129 130
Timestamp (sec)
)Vu(
laitneyoP
ECG
low cognitive load
high cognitive load
20
18
16
14
12
0 25 50 75 100 125 150 175
Timestamp (sec)
)Su(
ADE
EDA
low cognitive load 9
high cognitive load
8
7
6
5
4
3
125 126 127 128 129 130
Timestamp (sec)
)mm(
retemaid
lipuP
Gaze
low cognitive load
high cognitive load
Fig. 6: Examples of different signals in high and low cognitive load scenarios.
TABLE V: Extracted features from each modality.
Modalities Extractedfeatures Numberoffeatures
EEG PSD (absolute, mean, maximum, minimum, median power), Spectral Entropy, Hjorth mobility and 40
complexity,Lempel-ZivComplexity,Higuchifractaldimension,rawsignal(mean,minimum,maximum,
median,variance,andstandarddeviation)
ECG RMSSD,MeanNN,SDNN,SDSD,CVNN,CVSD,MedianNN,MadNN,MCVNN,IQRNN,pNN50, 53
pNN20,TINN,HTI,SD1,SD2SD1/SD2,S,CSI,CSI Modifies,CVI,PIP,IALS,PSS,PAS,GI,SI,
AI, PI, C1d, C1a, SD1d, SD1a, C2d, C2a, SD2d, SD2a, Cd, Ca, SDNNd, SDNNa, ApEn, SampEn,
mean, median, standard deviation, skewness, kurtosis, entropy, interquartile range, area under curve,
squaredareaunderthecurve,medianabsolutedeviation
EDA Mean, median, standard deviation, skewness, kurtosis, entropy, interquartile range, area under curve, 30
squared area under the curve, median absolute deviation for raw data as well as phasic and tonic
response
Gaze Pupil diameter (max, min, mean), Blink count, duration (max, mean), Fixation count, duration (max, 32
min,mean),dispersion(max,min,mean),Saccadecount,duration(max,min,mean),amplitude(max,
min, mean), peak velocity (max, min, mean), peak acceleration (max, min, mean), peak deceleration
(max,min,mean),direction(max,min,mean)
second squared (◦/s2). We directly use the high-level metrics Hz). We then measure the absolute, mean, maximum,
in our study. For the missing values in Gaze data, we used minimum, and median power of the measured PSD.
thesample-and-holdmethodsimilartothatofEDAduetothe 2) Spectralentropy:Spectralentropy(SE)ofatimeseries
straightforward nature of the signals. signal is derived from normalized Shannon’s entropy
[76] and can be used to determine the complexity
of a signal. The formula of SE can be derived from
B. Feature Extraction normalized PSD or probability distribution p(i) of the
Different features were extracted to train our machine signal as
learning algorithms. In this section, we describe the features
extracted from each modality. No feature selection methods n
(cid:88)
SE = p(i)lnp(i). (1)
were used. Given the focus of our work on BCI (other
modalities play auxiliary roles in the multimodal setups), we i=1
describe the EEG-related features in more depth below.
EEG. We extract 40 features from both time and frequency
We calculate SE for all 5 bands of EEG.
domainsfromeachchannelforeach10secondssegment.The
3) Hjorthmobilityandcomplexity:BothHjorthmobility
details of the features are given below:
andcomplexityofatimeseriessignaldetermineaspects
1) Power Spectral Density (PSD): PSD measures the of the signal complexity [77], where the variations
poweroftheEEGsignal.Tocalculatethisfeatureweuse in signal frequency and amplitude are represented by
theWelch’smethodfrom0.5Hzto75Hzfrequency,for Hjorth mobility and complexity respectively. These two
each frequency band, Delta (0.5-4 Hz), Theta (4-8Hz), measurementscanbejointlyusedtocapturethedynamic
Alpha (8-12 Hz), Beta (12-31 Hz), and Gamma (31-75 behavior of signals. Hjorth mobility and complexity are

9
40 30 20 10
0 1 2 3 4Lab5el6 7 8 9
stniopataD
Label Distribution
40 35 30 25 20 15 10 5
0 1 2 3 4Lab5el6 7 8 9
(a)Subject1
stniopataD
Label Distribution
80 70 60 50 40 30 20 10
0 1 2 3 4Lab5el6 7 8 9
(b)Subject2
stniopataD
Label Distribution
60 50 40 30 20 10
0 1 2 3 4Lab5el6 7 8 9
(c)Subject3
stniopataD
Label Distribution
40 35 30 25 20 15 10 5
0 1 2 3 4Lab5el6 7 8 9
(d)Subject4
stniopataD
Label Distribution
35 30 25 20 15 10 5
0 1 2 3 4Lab5el6 7 8 9
(e)Subject5
stniopataD
Label Distribution
40 30 20 10
0 1 2 3 4Lab5el6 7 8 9
(f)Subject6
stniopataD
Label Distribution
(g)Subject7
50 40 30 20 10
0 1 2 3 4Lab5el6 7 8 9
stniopataD
Label Distribution
30 25 20 15 10 5
0 1 2 3 4Lab5el6 7 8 9
(h)Subject8
stniopataD
Label Distribution
80 70 60 50 40 30 20 10
0 1 2 3 4Lab5el6 7 8 9
(i)Subject9
stniopataD
Label Distribution
40 30 20 10
0 1 2 3 4Lab5el6 7 8 9
(j)Subject10
stniopataD
Label Distribution
40 30 20 10
0 1 2 3 4Lab5el6 7 8 9
(k)Subject11
stniopataD
Label Distribution
35 30 25 20 15 10 5
0 1 2 3 4Lab5el6 7 8 9
(l)Subject12
stniopataD
Label Distribution
70 60 50 40 30 20 10
0 1 2 3 4Lab5el6 7 8 9
(m)Subject13
stniopataD
Label Distribution
(n)Subject14
60 50 40 30 20 10
0 1 2 3 4Lab5el6 7 8 9
stniopataD
Label Distribution
25 20 15 10 5
0 1 2 3 4Lab5el6 7 8 9
(o)Subject15
stniopataD
Label Distribution
40 30 20 10
0 1 2 3 4Lab5el6 7 8 9
(p)Subject16
stniopataD
Label Distribution
40 35 30 25 20 15 10 5
0 1 2 3 4Lab5el6 7 8 9
(q)Subject17
stniopataD
Label Distribution
25 20 15 10 5
0 1 2 3 4Lab5el6 7 8 9
(r)Subject18
stniopataD
Label Distribution
30 25 20 15 10 5
0 1 2 3 4Lab5el6 7 8 9
(s)Subject19
stniopataD
Label Distribution
50 40 30 20 10
0 1 2 3 4Lab5el6 7 8 9
(t)Subject20
stniopataD
Label Distribution
(u)Subject21
Fig. 7: Self-reported cognitive load level distribution for each participant.
Block 1 Block 2 Classification Block
EEG
E E C D G A D 1vno C N B U LeR D 1vno C N B U LeR loo P xaM D 1vno C N B U LeR D 1vno C N B U LeR loo P xaM .gvA labolG loo P C F C F tuptuO
Cognitive
load score
Gaze
Fig. 8: VGG-style network used as for benchmarking in this study.
Block 1 Block 2 Classification Block
EEG
E
E
C
D
G
A
D 1vno
C
N B U LeR N B U LeR D 1vnoC N B U LeR D 1vnoC looP xaM N B U LeR D 1vnoC N B U LeR D 1vnoC looP xaM N B U LeR CF CF CF tuptuO
Gaze Cognitive
load score
Fig. 9: ResNet-style network used as for benchmarking in this study.
respectively calculated as: 5) Higuchi fractal dimension: Higuchi fractal dimension
(HFD) is a non-linear method that can capture changes
(cid:118)
(cid:117) (cid:117)σ2(dy(t)) in time-series signals by measuring the complexity in
Hjorth =(cid:116) d(t) (2) time domain [80]. Prior studies have shown promising
M σ2(y(t))
resultusingHFDwithEEGsignalinthepast[81],[82].
6) Statistical features: In addition to the more sophisti-
and
cated features mentioned above, we also extract simple
Hjorth (dy(t))
M d(t) statistical features namely mean, minimum, maximum,
Hjorth = , (3)
C Hjorth (y(t)) and median from the signal in time domain.
M
The complete list of EEG features is summarized in Table V.
where y(t) represents the signal and σ2 is the variance
ECG. We extract various commonly used features from ECG
operator.
[83]. The full list of features extracted from ECG is presented
4) Lempel-Zivcomplexity:Lempel-Zivcomplexity(LZC)
inTableV.AllthefeaturesareextractedusingtheNeurokit25
is a measure that also determines the complexity of a
library. Please visit the library for further details.
signal [78]. To apply the LZC algorithm to an EEG
EDA. We extract a number of features from EDA. These
signal, the signal first needs to be binarized by the
include statistical features from the raw data as well as phasic
medianormeanvalueoftheentiresignal.Theresulting
and tonic responses which are calculated by decomposing the
binary sequence can then be analyzed the using LZC
algorithm to find any randomness [79]. 5https://neuropsychology.github.io/NeuroKit/functions/hrv.html

10
TABLE VI: The machine learning model parameters used in
operation. These blocks are followed by two fully connected
this study.
layers and a classification layer. Cross-entropy loss with a
learning rate of 0.001 was used for training. ADAM was used
Models Parameters
as the optimizer for this network [88].
AB number of estimators: 70, learning rate: 0.1, algorithm: TheResNet-stylenetwork,similartotheVGGmodelabove,
SAMME.R consists of two blocks containing two Conv1D layers, batch
DT criterion: gini, random state: 42, maximum depth: 3, mini- normalization, and ReLU activation function in each block.
mumsamplestobeatleafnode:5 The classification block contains three fully connected layer
NB variancesmoothing:1e−09 followedbyanoutputclassificationlayer.SimilartotheVGG
network, we use cross-entropy loss and train the model with
KNN numberofneighbors:20,weights:distance,algorithm:’auto’
ADAM optimizer. Here, a learning rate of 0.01 is used. For
LDA solver:leastsquaressolution bothnetworkstrainedwithfeatures,abatchsizeof32isused.
It should be noted that most studies on BCI and EEG in
RF maximumdepth:50,numberofestimators:1000,numberof
jobs:-1,randomstate:42,classweight:balanced particular use extracted features to train deep learning models
[89], [57], which is the approach we took with the networks
SVM regularizationparameter:0.1,kernel:polynomial
described above. However, for completeness, we also train
XGB maximum depth: 20, number of estimators: 1000, learning the deep networks with raw data (after pre-processing). For
rate:0.001,uselabelencoder:False,subsample:0.5,verbose
this purpose we design a separate encoder for each modality
eval:200,booster:dart,numberofjobs:-1,numberofleaves:
50,regularizationlambda:0.0001,classweight:balanced and use feature-level fusion. We expectedly notice that the
optimum network depth used when utilizing the extracted
MLP hiddenlayersizes:(100,50),learningrate:adaptive,maxi-
mumiteration:1000 features (2 blocks) is not sufficient when using the raw data.
We therefore increase the depth by adding a third block to
obtain better results. Accordingly each encoder for the raw
EDAsignal.ThecompletelistoffeaturesextractedfromEDA data contains 3 blocks for both the VGG and ResNet-style
is presented in Table V. models.Thedetailsofthearchitectureremainmostlythesame.
Gaze.Forgazeanalysis,weextractstatisticalfeaturesforeach We present all the details of the deep networks in Table VII,
10-second segment. The details of all the features are given for both VGG and ResNet-style models, when trained with
in Table V. features or raw signals. For both networks trained with raw
data, a batch size of 256 is used.
3) Multimodal: For the multimodal setup using the clas-
C. Normalization
sical machine learning methods, we simply concatenate the
To reduce the variability between subjects, which is a
hand-crafted features, and feed the concatenated features to
common phenomenon when recording such data, we divide
each classical classifier. For multimodal learning with deep
each feature value with its corresponding average value from
neural networks (VGG and ResNet), we first feed the raw
the baseline. Second, to reduce the variability within subjects,
data from each modality to a separate network and apply
we perform z-score normalization [84] following prior works
MaxPool followed by global average pooling on the outcome.
such as [85], [86], [87].
Thefeaturesarethenfusedtogetherthroughconcatenationand
fed to the classifier block.
D. Classifiers
To evaluate the dataset and to experiment the efficacy of
building an automated cognitive load detection system using E. Training scheme
the collected data, we train several classical machine learning
and deep learning classifiers on the extracted features or raw Wetrainallthemodels(classicalmachinelearninganddeep
data. In this section, we describe these models in detail. networks)inboth10-foldcrossvalidationandthemorerigor-
1) Classical machine learning: We train a total of 9 ma- ous Leave-One-Subject Out (LOSO) scheme. We also explore
chine learning classifiers namely AdaBoost (AB), Decision bothbinaryandternaryclassificationofcognitiveload.Certain
Tree (DT), Naive Bayes (NB), K-Nearest Neighbor (KNN), individualsmaynotbeabletodistinguishcognitiveloadscores
Linear Discriminant Analysis (LDA), Random Forest (RF), to that level of detail. This is precisely why we converted the
Support Vector Machine (SVM), Extreme Gradient Boosting scores to‘binary’ (high/low) and‘ternary’ (high/medium/low)
(XGB),andMulti-LayerPerceptron(MLP).Thedetailsofthe levelsusinggroupingofthescores.Thisinitialhigh-resolution
parameters of these classifiers are presented in Table VI. scheme, however, allows for future research to focus on more
2) Deep learning: For deep learning network we use two detailed classification schemes if necessary. For binary, we
deep Convolutional Neural Networks (CNNs), a VGG-style groupthecognitiveloadratingsfrom1to4as‘low’cognitive
network as shown in Figure 8, and a ResNet-style network loadand5to9as‘high’cognitiveload.Forternary,wedivide
which is shown in Figure 9. The VGG-style network has two thecognitiveloadratingsinto3groups,1to3,4to6,and7to
main blocks where each block consist of two Conv1D layers, 9 which corresponds to ‘low’, ‘medium’, and ‘high’ cognitive
batch normalization, ReLU activation, and maximum pooling load classes respectively.

11
TABLE VII: Architectural details of the VGG-style and ResNet-style networks used in this study for both features and raw
signals.
Modules Parameters VGG(feat.) ResNet(feat.) VGG(raw) ResNet(raw)
| Conv1D              | Kernelsize     | -    | 1×3    | -    |     | 1×32   |
| ------------------- | -------------- | ---- | ------ | ---- | --- | ------ |
|                     | Filtersize     | -    | 32     | -    |     | 64     |
| ConvBlock1          | Architecture   | VGG  | ResNet | VGG  |     | ResNet |
|                     | Activation     | ReLU | ReLU   | ReLU |     | ReLU   |
|                     | Kernelsize     | 1×3  | 1×3    | 1×32 |     | 1×32   |
|                     | Filtersize     | 64   | 32     | 64   |     | 64     |
|                     | Dropoutrate    | -    | 0.5    | -    |     | 0.5    |
| ConvBlock2          | Architecture   | VGG  | ResNet | VGG  |     | ResNet |
|                     | Activation     | ReLU | ReLU   | ReLU |     | ReLU   |
|                     | Kernelsize     | 1×3  | 1×3    | 1×16 |     | 1×16   |
|                     | Filtersize     | 128  | 32     | 128  |     | 128    |
|                     | Dropoutrate    | -    | 0.5    | -    |     | 0.5    |
| ConvBlock3          | Architecture   | -    | -      | VGG  |     | ResNet |
|                     | Activation     | -    | -      | ReLU |     | ReLU   |
|                     |                |      |        | 1×8  |     | 1×8    |
|                     | Kernelsize     | -    | -      |      |     |        |
|                     | Filtersize     | -    | -      | 256  |     | 256    |
|                     | Dropoutrate    | -    | -      | -    |     | 0.5    |
| ClassificationBlock | Layertype      | FC   | FC     | FC   |     | FC     |
|                     | Numberoflayers | 2    | 3      | 2    |     | 3      |
|                     | Dropoutrate    | 0.25 | -      | 0.25 |     | 0.25   |
|                     | Activation     | ReLU | ReLU   | ReLU |     | ReLU   |
TABLE VIII: The accuracy and F1 scores for the classifiers in 10-fold binary setup.
Modalities
Models EEG EEG,ECG EEG,EDA EEG,Gaze EEG,ECG EEG,ECG EEG,EDA EEG,ECG Mean
|     |     |     | EDA | Gaze | Gaze | EDA,Gaze |
| --- | --- | --- | --- | ---- | ---- | -------- |
AB 67.17(55.37) 73.26(68.43) 71.09(66.53) 70.13(61.29) 73.84(69.85) 74.36(69.75) 73.36(69.07) 75.35(71.80) 72.32(66.51)
DT 65.31(63.04) 72.77(71.15) 69.61(67.93) 68.17(66.48) 73.02(71.41) 73.12(71.52) 72.39(70.75) 73.98(72.40) 71.05(69.34)
NB 48.68(46.54) 51.80(50.48) 51.39(49.97) 49.95(48.22) 53.73(52.87) 52.46(51.35) 52.39(51.23) 54.42(53.65) 51.85(50.54)
KNN 70.61(68.49) 69.34(67.40) 71.78(70.16) 77.00(74.65) 70.64(69.16) 74.60(71.97) 77.72(75.46) 74.97(72.50) 73.33(71.22)
LDA 66.83(62.45) 72.74(70.65) 71.19(68.45) 69.65(66.24) 74.73(72.94) 73.70(71.61) 72.95(70.62) 75.83(74.04) 72.20(69.63)
RF 77.41(73.39) 79.34(76.27) 79.48(76.47) 79.89(76.31) 81.26(78.8) 80.82(77.94) 80.65(77.83) 81.71(79.23) 80.07(77.03)
SVM 61.88(38.29) 62.08(38.89) 61.88(38.29) 63.46(43.86) 64.35(46.59) 71.54(65.23) 67.14(54.32) 73.70(68.98) 65.75(49.31)
XGB 77.38(73.72) 82.95(81.25) 80.06(77.67) 80.75(78.06) 82.61(80.94) 83.02(81.22) 82.12(80.08) 83.67(82.05) 81.57(79.37)
MLP 74.32(72.36) 74.22(72.31) 76.31(74.02) 75.18(73.46) 76.00(74.54) 75.83(74.55) 77.11(75.47) 77.69(76.19) 75.83(74.11)
VGG(feat.) 75.56(73.21) 77.57(75.8) 78.99(76.94) 78.78(76.74) 78.78(77.22) 78.82(77.23) 80.17(78.39) 80.66(79.17) 78.67(68.31)
ResNet(feat.) 69.38(65.26) 74.27(71.48) 71.74(68.46) 72.85(69.15) 75.49(72.71) 74.65(71.83) 73.61(70.67) 76.39(74.28) 73.55(70.48)
VGG(raw) 63.83(63.23) 67.73(66.97) 66.95(66.11) 67.62(66.95) 70.12(69.2) 71.45(70.5) 71.76(71.07) 73.87(73.00) 69.17(68.38)
ResNet(raw) 61.95(59.75) 64.49(62.14) 60.90(57.45) 66.68(64.85) 64.41(62.82) 70.04(67.69) 68.71(66.37) 69.96(67.04) 65.89(63.51)
Mean 67.72(62.70) 70.97(61.92) 70.11(66.03) 70.78(66.64) 72.23(58.91) 73.42(70.95) 73.08(70.10) 74.78(72.64)
| TABLE | IX: The accuracy | and F1 scores | for the classifiers | in LOSO | binary | setup. |
| ----- | ---------------- | ------------- | ------------------- | ------- | ------ | ------ |
Modalities
Models EEG EEG,ECG EEG,EDA EEG,Gaze EEG,ECG EEG,ECG EEG,EDA EEG,ECG Mean
|     |     |     | EDA | Gaze | Gaze | EDA,Gaze |
| --- | --- | --- | --- | ---- | ---- | -------- |
AB 62.30(46.81) 66.58(59.47) 63.01(54.57) 64.81(53.53) 67.86(62.22) 66.80(60.05) 66.92(59.68) 69.14(63.60) 65.93(57.49)
DT 54.63(49.73) 60.33(54.82) 57.94(53.07) 57.57(53.77) 60.97(56.91) 62.13(57.25) 61.19(56.73) 62.00(57.02) 59.60(54.91)
NB 47.80(43.54) 48.94(45.80) 48.16(44.71) 49.00(45.06) 49.85(47.52) 49.85(47.11) 49.15(45.71) 50.35(48.06) 49.14(45.94)
KNN 58.21(53.11) 61.45(58.09) 60.83(56.10) 66.03(61.42) 62.51(59.51) 65.55(61.10) 67.06(62.48) 65.60(61.36) 63.40(59.15)
LDA 57.06(49.61) 59.87(55.67) 62.95(56.99) 60.45(54.25) 63.15(58.60) 61.88(57.75) 64.45(58.97) 64.73(60.26) 61.82(56.51)
RF 63.82(50.97) 65.76(56.84) 66.64(56.73) 65.79(54.20) 67.95(59.92) 66.50(57.90) 68.94(60.48) 70.15(62.39) 66.94(57.43)
SVM 62.01(37.65) 59.85(37.84) 61.80(37.91) 62.56(42.96) 61.48(45.71) 66.26(59.40) 65.94(51.89) 68.53(62.79) 63.55(47.02)
XGB 62.98(52.34) 66.61(60.53) 66.39(59.34) 66.67(59.96) 69.37(64.01) 68.81(63.20) 69.73(64.01) 71.48(66.07) 67.76(61.18)
MLP 57.86(51.98) 63.64(57.90) 63.44(58.13) 61.45(57.43) 64.48(60.33) 61.32(57.15) 65.72(60.94) 64.51(59.41) 62.80(57.91)
VGG(feat.) 70.70(64.22) 74.72(70.68) 73.01(68.08) 74.68(69.91) 76.17(71.72) 76.04(71.83) 75.49(71.34) 75.52(72.44) 74.54(70.03)
ResNet(feat.) 67.45(61.39) 75.90(71.62) 72.20(66.48) 72.85(67.53) 74.23(69.28) 74.42(70.32) 74.89(69.49) 74.59(69.55) 73.32(68.21)
VGG(raw) 65.00(58.92) 63.67(57.59) 67.18(60.78) 65.37(59.81) 67.37(60.84) 64.97(58.51) 66.47(61.79) 67.18(61.37) 65.90(59.95)
ResNet(raw) 65.79(57.58) 63.99(56.73) 69.03(61.67) 68.03(61.12) 68.74(61.88) 66.67(59.63) 66.50(62.16) 67.69(61.88) 67.06(60.33)
Mean 61.20(52.14) 63.95(57.20) 64.04(56.50) 64.25(57.00) 65.70(59.88) 65.48(60.09) 66.34(60.44) 67.04(62.02)

12
TABLE X: The accuracy and F1 scores for the classifiers in 10-fold ternary setup.
Modalities
EEG,ECG EEG,ECG EEG,EDA EEG,ECG
Models EEG EEG,ECG EEG,EDA EEG,Gaze Mean
EDA Gaze Gaze EDA,Gaze
AB 46.20(38.35) 51.84(48.65) 51.56(48.78) 50.12(44.48) 53.52(51.62) 54.66(51.69) 52.56(49.66) 55.31(53.15) 51.97(48.30)
DT 48.95(48.77) 56.03(56.08) 52.08(51.85) 52.70(52.26) 57.48(57.36) 58.82(58.88) 56.14(55.85) 58.13(58.16) 55.04(54.90)
NB 34.93(29.77) 37.13(33.00) 37.47(33.77) 36.58(31.86) 39.50(36.55) 38.78(35.06) 38.64(35.23) 40.50(37.74) 37.94(34.12)
KNN 54.59(53.95) 51.60(50.81) 56.34(55.90) 62.22(62.01) 52.46(51.67) 57.06(56.33) 63.05(62.87) 58.61(57.93) 56.99(56.43)
LDA 53.01(51.93) 58.27(58.09) 58.13(57.82) 54.93(54.33) 61.02(61.00) 59.43(59.23) 58.03(57.89) 61.84(61.84) 58.08(57.77)
RF 63.56(63.04) 68.41(68.42) 69.34(69.17) 68.30(68.03) 71.57(71.63) 70.40(70.39) 71.67(71.76) 72.67(72.86) 69.49(69.41)
SVM 41.01(21.66) 46.58(37.78) 41.73(24.17) 48.75(42.59) 48.40(41.25) 53.01(50.34) 50.39(45.38) 53.83(51.60) 47.96(39.35)
XGB 64.49(64.14) 70.78(71.01) 71.74(71.69) 71.19(71.22) 73.50(73.76) 72.91(73.15) 73.60(73.61) 74.08(74.26) 71.54(71.61)
MLP 58.44(57.72) 61.50(60.64) 61.12(60.90) 62.63(62.22) 62.80(62.66) 63.08(63.09) 63.84(63.83) 63.25(63.26) 62.08(61.79)
VGG(feat.) 62.12(60.92) 62.85(62.21) 64.44(63.91) 65.38(64.88) 65.76(65.37) 64.03(63.43) 67.12(66.72) 66.67(66.04) 64.80(64.19)
ResNet(feat.) 47.19(44.61) 55.52(53.74) 51.91(50.66) 51.39(49.41) 56.15(55.48) 54.86(53.88) 53.19(52.24) 55.63(54.67) 53.23(51.84)
VGG(raw) 47.85(43.7) 55.43(51.37) 56.48(51.61) 56.68(52.24) 61.76(57.96) 62.89(58.3) 63.44(59.41) 66.33(62.93) 58.86(54.69)
ResNet(raw) 50.82(37.41) 56.56(50.09) 53.67(44.25) 56.37(49.93) 60.62(54.07) 59.38(54.49) 61.05(56.39) 64.84(60.60) 57.91(50.90)
Mean 51.78(47.38) 56.35(53.99) 55.85(52.65) 56.71(54.27) 58.81(56.95) 59.18(57.56) 59.44(57.76) 60.90(59.62)
TABLE XI: The accuracy and F1 scores for the classifiers in LOSO ternary setup.
Modalities
EEG,ECG EEG,ECG EEG,EDA EEG,ECG
Models EEG EEG,ECG EEG,EDA EEG,Gaze Mean
EDA Gaze Gaze EDA,Gaze
AB 37.79(27.09) 42.13(34.39) 42.56(36.04) 43.88(36.63) 44.26(38.46) 45.42(37.95) 46.03(39.76) 47.65(41.81) 43.15(35.76)
DT 35.83(33.35) 40.15(37.63) 37.37(34.68) 37.69(34.8) 35.77(33.02) 40.32(37.76) 37.58(35.42) 39.15(37.17) 37.82(35.24)
NB 33.28(26.3) 33.81(27.37) 33.02(27.85) 34.27(28.04) 33.23(28.40) 34.71(28.59) 33.93(29.18) 34.08(29.40) 33.75(27.96)
KNN 35.19(32.87) 39.19(37.06) 37.40(34.97) 44.03(41.90) 39.24(37.31) 41.51(39.82) 44.78(42.45) 41.69(40.04) 40.19(38.05)
LDA 36.18(33.64) 40.23(37.02) 40.33(37.61) 38.43(36.29) 42.31(39.07) 40.02(37.22) 40.96(38.78) 41.03(38.45) 39.78(37.09)
RF 37.02(32.58) 40.15(37.54) 39.97(36.05) 43.03(39.93) 42.28(40.15) 43.11(40.13) 45.31(42.38) 44.96(42.76) 41.55(38.39)
SVM 38.48(20.41) 39.66(31.73) 38.42(21.00) 42.46(34.15) 39.83(33.22) 44.69(40.43) 43.13(35.87) 45.05(41.22) 40.95(30.97)
XGB 36.09(32.83) 40.06(38.11) 41.63(38.50) 43.26(41.51) 44.48(42.31) 43.44(40.82) 46.14(43.77) 47.10(44.68) 42.16(39.69)
MLP 38.30(34.11) 39.30(36.70) 41.44(36.83) 44.23(41.10) 42.04(38.88) 41.68(38.99) 46.05(42.65) 42.94(40.38) 41.86(38.47)
VGG(feat.) 49.21(43.75) 54.34(48.93) 51.83(47.64) 54.67(49.85) 54.39(50.96) 53.64(49.99) 56.16(52.17) 56.88(52.98) 53.46(49.04)
ResNet(feat.) 47.30(42.08) 52.82(49.44) 53.44(47.1) 50.23(46.15) 55.31(50.65) 53.81(49.49) 53.26(49.16) 55.70(51.02) 52.31(47.72)
VGG(raw) 57.91(44.12) 60.84(47.61) 58.86(44.83) 58.08(44.08) 61.29(49.18) 63.04(49.47) 57.01(45.06) 63.56(49.39) 59.58(46.34)
ResNet(raw) 58.13(42.54) 60.86(47.30) 58.22(43.81) 60.37(45.90) 60.12(46.68) 64.53(51.40) 58.65(46.27) 61.55(49.93) 60.13(46.27)
Mean 41.59(34.28) 44.89(39.29) 44.19(37.45) 45.74(40.03) 45.73(40.64) 46.92(41.70) 46.85(41.76) 47.80(43.02)
V. BENCHMARKINGRESULTS all4modalities,followedbythetri-modal,bi-modal,anduni-
Here, we present the results of the benchmarking study for modal setups respectively. From the average values for each
binary and ternary classification in both validation schemes. model, we can deduce that the VGG-style model trained on
We also present a comparison for the different multimodal featuresperformsthebest,followedbytheResNet-stylemodel
setupsinourexperiments.Thedetailedresultsarepresentedin trained on features.
TablesVIII,IX,X,andXI.Inthesetables,boldvaluesdenote We present the results for the ternary 10-fold setup in
the highest, while underline represents the second-highest. As Table X, and we observe that the best result of 74.08% is
we observe in Table VIII, for 10-fold cross-validation in the achievedwiththemachinelearningclassifier,XGB.Thisresult
binary setup, we obtain the highest accuracy of 83.67% with is obtained when EEG is trained along with all 3 auxiliary
the XGB classifier. This performance is achieved when all 4 modalities. The second best accuracy of 73.60% is obtained
modalitiesareused.Thisisfollowedby83.02%asthesecond with the same classifier when EEG, EDA, and Gaze are used
best obtained with EEG with ECG and Gaze by the same together. Comparing the average results for each modality
classifier.Comparingtheaveragevaluesobtainedfordifferent setup, we find that as expected, the using all 4 modalities
modality setups indicates that as expected, EEG, ECG, EDA, outperforms the rest while the best performing average result
and Gaze altogether outperform the rest, followed by tri- is achieved by the XGB classifier. Among the 4 deep learning
modal, bi-modal, and uni-modal setups, respectively. Looking models, the VGG-style model outperforms the other 3 when
at the average values for all the models we observe that the trained with features. Here, the highest accuracy of 67.12%
XGBclassifiergenerallyoutperformstherestfollowedbyRF. is obtained when trained with 3 modalities EEG, EDA, and
Amongthe4differentdeeplearningvariantsinthissetup,we Gaze.
notice that VGG trained with features from all 4 modalities Lastly, Table XI shows us the result in the LOSO ternary
outperforms the other 3 scenarios. setup. The highest result obtained is 64.53% when using
In Table IX, for the binary LOSO evaluation scheme, we the ResNet-style network trained with the raw data with
observe that the highest accuracy of 76.17% is obtained by 3 modalities namely EEG, ECG, and Gaze. Following, the
theVGG-stylenetworktrainedwithfeatures.Thisaccuracyis second highest accuracy of 63.56% is obtained by the VGG-
obtained using 3 modalities, namely EEG, ECG and EDA. style network trained on raw data from all 4 modalities.
The second best accuracy, 76.04%, is achieved with the The average results of various modality setups show that the
combinationofEEG,ECG,andGaze.Comparingtheaverage multimodal setup with all 4 modalities achieves the highest
values from different modality setups, we observe that the accuracy. The average highest accuracy is obtained using the
highest accuracy is obtained by the multimodal scenario with ResNet-style model followed by the VGG-style model both

13
when trained with raw data. both LOSO as well as k-fold evaluation schemes. The CL-
In the end, to summarize our findings above, we observe Drive dataset can have various applications in the field of
thatbothclassicalmachinelearninganddeeplearningmodels transportation, driver safety, and human-machine interaction.
|         |             |     |                |     |         |           |        | The dataset | can | be used | to assess | the | cognitive | workload |     |
| ------- | ----------- | --- | -------------- | --- | ------- | --------- | ------ | ----------- | --- | ------- | --------- | --- | --------- | -------- | --- |
| possess | the ability |     | to distinguish |     | between | different | levels |             |     |         |           |     |           |          |     |
of driver cognitive loads. As expected, we find that ternary experienced by drivers in various driving scenarios, such as
classification is more challenging than binary, while LOSO high-traffic conditions, adverse weather, or during complex
on the other hand proves more difficult than 10-fold. In maneuvers. Overall, the CL-Drive dataset has the potential to
termsofmodalities,multimodalsetupsgenerallyprovidemore improveroadsafety,enhancedriverexperience,andcontribute
|             |           |     |        |           |       |           |      | to the development |     | of  | more intelligent |     | and human-centered |     |     |
| ----------- | --------- | --- | ------ | --------- | ----- | --------- | ---- | ------------------ | --- | --- | ---------------- | --- | ------------------ | --- | --- |
| information | regarding |     | driver | cognitive | load, | with EEG, | ECG, |                    |     |     |                  |     |                    |     |     |
EDA and Gaze showing the best performances. transportation systems.
VII. ACKNOWLEDGEMENT
A. Limitations
While our work makes significant contributions to the area, We would like to thank the Innovation for Defence Excel-
|               |       |              |          |           |            |              |           | lence and | Security | (IDEaS) | program     | under | the      | Department | of  |
| ------------- | ----- | ------------ | -------- | --------- | ---------- | ------------ | --------- | --------- | -------- | ------- | ----------- | ----- | -------- | ---------- | --- |
| there exist   | a few | areas        | in which | our       | work could | be           | improved. |           |          |         |             |       |          |            |     |
|               |       |              |          |           |            |              |           | National  | Defence  | (DND)   | for funding | this  | project. |            |     |
| For instance, |       | using a      | driving  | simulator | versus     | real         | vehicles  |           |          |         |             |       |          |            |     |
| offers a      | safe  | alternative, | reduces  |           | the risk   | of accidents | and       |           |          |         |             |       |          |            |     |
REFERENCES
injuries,andallowsustodesignveryspecificdrivingscenarios
bycontrollingtheweather,timeofday,roadconditions,obsta- [1] M.Miyaji,H.Kawanaka,andK.Oguri,“Driver’scognitivedistraction
detectionusingphysiologicalfeaturesbytheadaboost,”in12thInterna-
cles,numberofcarsontheroad,etc.,thatareapplicableacross
|         |               |     |     |       |           |              |     | tionalIEEEConferenceonIntelligentTransportationSystems. |     |     |     |     |     |     | IEEE, |
| ------- | ------------- | --- | --- | ----- | --------- | ------------ | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- |
| all the | participants. | On  | the | other | hand, the | disadvantage | of  |                                                         |     |     |     |     |     |     |       |
2009,pp.1–6.
usingasimulatoristhepossibilityofparticipantsexperiencing [2] O. Palinko, A. L. Kun, A. Shyrokov, and P. Heeman, “Estimating
cognitiveloadusingremoteeyetrackinginadrivingsimulator,”inPro-
| SAS, as  | well     | as limited | motion |           | and the        | use of | generated |          |        |           |                 |     |          |                 |     |
| -------- | -------- | ---------- | ------ | --------- | -------------- | ------ | --------- | -------- | ------ | --------- | --------------- | --- | -------- | --------------- | --- |
|          |          |            |        |           |                |        |           | ceedings | of the | Symposium | on Eye-tracking |     | Research | & Applications, |     |
| graphics | that may | not        | fully  | replicate | the experience |        | of real-  |          |        |           |                 |     |          |                 |     |
2010,pp.141–144.
world driving. [3] L.Fridman,B.Reimer,B.Mehler,andW.T.Freeman,“Cognitiveload
estimationinthewild,”inProceedingsoftheChiConferenceonHuman
| The number |     | of participants |     | (6M+15F | =   | total of | 21) in our |     |     |     |     |     |     |     |     |
| ---------- | --- | --------------- | --- | ------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
FactorsinComputingSystems,2018,pp.1–9.
study is in line with other datasets such as SEED (7M+8F [4] A. Yu¨ce, H. Gao, G. L. Cuendet, and J.-P. Thiran, “Action units and
= total of 15), SEED-IV (7M+8F = total of 15), SEED-VIG theircross-correlationsforpredictionofcognitiveloadduringdriving,”
(11M+12F = total of 23), and others. However, we acknowl- IEEETransactionsonAffectiveComputing,vol.8,no.2,pp.161–175,
2016.
edge that adding more participants and further balancing the [5] E. Q. Wu, D. Hu, P.-Y. Deng, Z. Tang, Y. Cao, W.-M. Zhang, L.-
demographics in terms of factors such as gender can help M. Zhu, and H. Ren, “Nonparametric bayesian prior inducing deep
networkforautomaticdetectionofcognitivestatus,”IEEETransactions
| increase | generalization |     | of the | findings | and | improve | diversity |     |     |     |     |     |     |     |     |
| -------- | -------------- | --- | ------ | -------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
onCybernetics,vol.51,no.11,pp.5483–5496,2020.
inthedata,whichcanleadtomoreeffectivemachinelearning
[6] E.Q.Wu,Z.Tang,Y.Yao,X.-Y.Qiu,P.-Y.Deng,P.Xiong,A.Song,L.-
models. M.Zhu,andM.Zhou,“Scalablegamma-drivenmultilayernetworkfor
brainworkloaddetectionthroughfunctionalnear-infraredspectroscopy,”
| Lastly, | another | area | that | could | be discussed |     | is the use |     |     |     |     |     |     |     |     |
| ------- | ------- | ---- | ---- | ----- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
IEEETransactionsonCybernetics,vol.52,no.11,pp.12464–12478,
| of participant-reported |     |     | subjective | measurements |     | for | cognitive |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | ---------- | ------------ | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
2021.
|     |     |     |     |     |     |     |     |     |     |     |     | Psychology |     | of Learning | and |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----------- | --- |
load. It should be noted that while advanced brain scanning [7] J. Sweller, “Cognitive load theory,” in
|              |       |               |      |            |           |              |           | Motivation. | Elsevier,2011,vol.55,pp.37–76. |             |            |            |        |                   |     |
| ------------ | ----- | ------------- | ---- | ---------- | --------- | ------------ | --------- | ----------- | ------------------------------ | ----------- | ---------- | ---------- | ------ | ----------------- | --- |
| technologies | could | be            | used | to measure | cognitive |              | load more |             |                                |             |            |            |        |                   |     |
|              |       |               |      |            |           |              |           | [8] R. Das, | D. Chatterjee,                 |             | D. Das, A. | Sinharay,  | and A. | Sinha, “Cognitive |     |
| objectively, | such  | self-reported |      | methods    | are       | consistently | relied    |             |                                |             |            |            |        |                   |     |
|              |       |               |      |            |           |              |           | load        | measurement-a                  | methodology |            | to compare | low    | cost commercial   |     |
upon in the literature to obtain labels or scores with which eeg devices,” in International Conference on Advances in Computing,
CommunicationsandInformatics.
to train machine learning models. Additionally, the fact that IEEE,2014,pp.1188–1194.
|     |     |     |     |     |     |     |     | [9] S. Schneegass, |     | B. Pfleging, | N. Broy, | F. Heinrich, | and | A. Schmidt, | “A  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------------ | -------- | ------------ | --- | ----------- | --- |
the trained models are capable of making strong predictions, datasetofrealworlddrivingtoassessdriverworkload,”inProceedings
points to the reliability of the output labels. To reduce the ofthe5thInternationalConferenceonAutomotiveUserInterfacesand
possible subjectivity of self-reported scores, larger datasets InteractiveVehicularApplications,2013,pp.150–157.
I.Mijic´,M.Sˇarlija,andD.Petrinovic´,“Mmod-cog:Adatabaseformul-
[10]
may be used, in addition to deep learning paradigms such timodalcognitiveloadclassification,”in11thInternationalSymposium
as weakly supervised or partial-label learning. onImageandSignalProcessingandAnalysis. IEEE,2019,pp.15–20.
|     |     |     |     |     |     |     |     | [11] V.Markova,T.Ganchev,andK.Kalinkov,“Clas:Adatabaseforcogni- |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
tiveload,affectandstressrecognition,”inInternationalConferenceon
BiomedicalInnovationsandApplications.
|     |     |     | VI. CONCLUSION |     |     |     |     |                   |     |          |          |              | IEEE,2019,pp.1–4. |              |     |
| --- | --- | --- | -------------- | --- | --- | --- | --- | ----------------- | --- | -------- | -------- | ------------ | ----------------- | ------------ | --- |
|     |     |     |                |     |     |     |     | [12] M. Gjoreski, | T.  | Kolenik, | T. Knez, | M. Lusˇtrek, | M. Gams,          | H. Gjoreski, |     |
In this paper, we presented CL-Drive, a new multimodal and V. Pejovic´, “Datasets for cognitive load inference using wearable
|           |      |         |           |        |           |          |     | sensors | and psychological |     | traits,” | Applied Sciences, | vol. | 10, no. | 11, p. |
| --------- | ---- | ------- | --------- | ------ | --------- | -------- | --- | ------- | ----------------- | --- | -------- | ----------------- | ---- | ------- | ------ |
| cognitive | load | dataset | collected | during | simulated | driving. | Our |         |                   |     |          |                   |      |         |        |
3843,2020.
dataset,whichwemadepublic,containsEEG,ECG,EDA,and
|     |     |     |     |     |     |     |     | [13] A. Kalatzis, | A.       | Teotia,        | V. G. Prabhu, | and L.                  | Stanley, | “A database | for      |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | -------- | -------------- | ------------- | ----------------------- | -------- | ----------- | -------- |
|     |     |     |     |     |     |     |     | cognitive         | workload | classification |               | using electrocardiogram |          | and         | respira- |
Gazedatafrom21participantsinavarietyofdifferentdriving
|     |     |     |     |     |     |     |     | tion | signal,” in | International | Conference | on  | Applied | Human | Factors |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----------- | ------------- | ---------- | --- | ------- | ----- | ------- |
conditions.Subjectiveself-reportedcognitiveloadscoreswere
|          |              |     |           |            |     |                 |     | andErgonomics.  |     | Springer,2021,pp.509–516. |             |               |     |             |     |
| -------- | ------------ | --- | --------- | ---------- | --- | --------------- | --- | --------------- | --- | ------------------------- | ----------- | ------------- | --- | ----------- | --- |
| recorded | at 10-second |     | intervals | throughout |     | the experiment, |     |                 |     |                           |             |               |     |             |     |
|          |              |     |           |            |     |                 |     | [14] P. Sarkar, | K.  | Ross, A.                  | J. Ruberto, | D. Rodenbura, |     | P. Hungler, | and |
makingitaveryrichanddensedatasetintermsofbothmodal- A.Etemad,“Classificationofcognitiveloadandexpertiseforadaptive
simulationusingdeepmultitasklearning,”in8thInternationalConfer-
| ities and   | labels. | We          | also provided |             | benchmarks | by            | evaluating |                                                    |     |     |     |     |     |            |     |
| ----------- | ------- | ----------- | ------------- | ----------- | ---------- | ------------- | ---------- | -------------------------------------------------- | --- | --- | --- | --- | --- | ---------- | --- |
|             |         |             |               |             |            |               |            | enceonAffectiveComputingandIntelligentInteraction. |     |     |     |     |     | IEEE,2019, |     |
| our dataset | in      | both binary |               | and ternary | label      | distributions | for        | pp.1–7.                                            |     |     |     |     |     |            |     |

14
[15] K.Ross,P.Sarkar,D.Rodenburg,A.Ruberto,P.Hungler,A.Szulewski, [38] S.Zepf,J.Hernandez,A.Schmitt,W.Minker,andR.W.Picard,“Driver
D. Howes, and A. Etemad, “Toward dynamically adaptive simulation: emotionrecognitionforintelligentvehicles:Asurvey,”ACMComputing
Multimodal classification of user expertise using wearable devices,” Surveys(CSUR),vol.53,no.3,pp.1–30,2020.
JournalofSensors,vol.19,no.19,p.4270,2019. [39] G. Zhang and A. Etemad, “Capsule attention for multimodal eeg-eog
[16] R. Brunken, J. L. Plass, and D. Leutner, “Direct measurement of cog- representationlearningwithapplicationtodrivervigilanceestimation,”
nitive load in multimedia learning,” Educational Psychologist, vol. 38, IEEETransactionsonNeuralSystemsandRehabilitationEngineering,
| no.1,pp.53–61,2003. |     |     |     |     |     |     | vol.29,pp.1138–1149,2021. |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- |
[17] R. E. Mayer and R. Moreno, “Aids to computer-based multimedia [40] L. M. Bergasa, J. Nuevo, M. A. Sotelo, R. Barea, and M. E. Lopez,
learning,”LearningandInstruction,vol.12,no.1,pp.107–119,2002. “Real-timesystemformonitoringdrivervigilance,”IEEETransactions
[18] M.Klepsch,F.Schmitz,andT.Seufert,“Developmentandvalidationof onIntelligentTransportationSystems,vol.7,no.1,pp.63–77,2006.
twoinstrumentsmeasuringintrinsic,extraneous,andgermanecognitive [41] C.-T.Lin,C.-H.Chuang,C.-S.Huang,S.-F.Tsai,S.-W.Lu,Y.-H.Chen,
andL.-W.Ko,“Wirelessandwearableeegsystemforevaluatingdriver
load,”FrontiersinPsychology,vol.8,p.1997,2017.
[19] F.G.Paas,“Trainingstrategiesforattainingtransferofproblem-solving vigilance,” IEEE Transactions on Biomedical Circuits and Systems,
skill in statistics: a cognitive-load approach,” Journal of Educational vol.8,no.2,pp.165–176,2014.
Psychology,vol.84,no.4,p.429,1992. [42] Z. Emami and T. Chau, “The effects of visual distractors on cognitive
[20] S. G. Hart and L. E. Staveland, “Development of nasa-tlx (task load load in a motor imagery brain-computer interface,” Behavioural Brain
Research,vol.378,p.112240,2020.
| index): | Results | of empirical | and theoretical | research,” |     | in Advances | in  |     |     |     |     |     |     |
| ------- | ------- | ------------ | --------------- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Psychology. [43] W. J. Chai, A. I. Abd Hamid, and J. M. Abdullah, “Working mem-
Elsevier,1988,vol.52,pp.139–183.
[21] R. Bru¨nken, S. Steinbacher, J. L. Plass, and D. Leutner, “Assessment ory from the psychological and neurosciences perspectives: a review,”
ofcognitiveloadinmultimedialearningusingdual-taskmethodology.” FrontiersinPsychology,vol.9,p.401,2018.
ExperimentalPsychology,vol.49,no.2,p.109,2002. [44] S. Siuly, Y. Li, and Y. Zhang, “Eeg signal analysis and classification,”
IEEETransactionsonNeuralSystemsandRehabilitationEngineering,
| [22] B. Park | and | R. Bru¨nken, | “The rhythm | method: | A new | method for |     |     |     |     |     |     |     |
| ------------ | --- | ------------ | ----------- | ------- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- |
vol.11,pp.141–144,2016.
| measuring | cognitive | load—an | experimental |     | dual-task | study,” Applied |     |     |     |     |     |     |     |
| --------- | --------- | ------- | ------------ | --- | --------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
CognitivePsychology,vol.29,no.2,pp.232–243,2015. [45] W. Klimesch, “Eeg alpha and theta oscillations reflect cognitive and
[23] P.W.VanGerven,F.Paas,J.J.VanMerrie¨nboer,andH.G.Schmidt, memoryperformance:areviewandanalysis,”BrainResearchReviews,
vol.29,no.2–3,pp.169–195,1999.
| “Memory | load | and the | cognitive pupillary |     | response | in aging,” Psy- |               |             |     |            |               |             |      |
| ------- | ---- | ------- | ------------------- | --- | -------- | --------------- | ------------- | ----------- | --- | ---------- | ------------- | ----------- | ---- |
|         |      |         |                     |     |          |                 | [46] K. Ross, | P. Hungler, | and | A. Etemad, | “Unsupervised | multi-modal | rep- |
chophysiology,vol.41,no.2,pp.167–174,2004.
resentationlearningforaffectivecomputingwithmulti-corpuswearable
[24] S.ChenandJ.Epps,“Usingtask-inducedpupildiameterandblinkrate
|                  |           |        |                |              |     |              | data,”Journalof |     | AmbientIntelligence |     | andHumanizedComputing,pp. |     |     |
| ---------------- | --------- | ------ | -------------- | ------------ | --- | ------------ | --------------- | --- | ------------------- | --- | ------------------------- | --- | --- |
| to infer         | cognitive | load,” | Human–Computer | Interaction, |     | vol. 29, no. | 4,              |     |                     |     |                           |     |     |
| pp.390–413,2014. |           |        |                |              |     |              | 1–26,2021.      |     |                     |     |                           |     |     |
[47] R.Xiong,F.Kong,X.Yang,G.Liu,andW.Wen,“Patternrecognition
[25] F.G.PaasandJ.J.VanMerrie¨nboer,“Variabilityofworkedexamples
ofcognitiveloadusingeegandecgsignals,”JournalofSensors,vol.20,
| and transfer | of  | geometrical | problem-solving |     | skills: A | cognitive-load |     |     |     |     |     |     |     |
| ------------ | --- | ----------- | --------------- | --- | --------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
no.18,p.5122,2020.
| approach,” | Journal | of Educational | Psychology, |     | vol. 86, | no. 1, p. 122, |     |     |     |     |     |     |     |
| ---------- | ------- | -------------- | ----------- | --- | -------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
[48] A.M.Hughes,G.M.Hancock,S.L.Marlow,K.Stowers,andE.Salas,
1994.
|     |     |     |     |     |     |     | “Cardiac | measures | of  | cognitive | workload: | a meta-analysis,” | Human |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | --------- | --------- | ----------------- | ----- |
[26] P. Antonenko, F. Paas, R. Grabner, and T. Van Gog, “Using elec- Factors,vol.61,no.3,pp.393–414,2019.
troencephalographytomeasurecognitiveload,”EducationalPsychology
|     |     |     |     |     |     |     | [49] E. Johannessen, |     | A. Szulewski, | N.  | Radulovic, | M. White, | H. Braund, |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ------------- | --- | ---------- | --------- | ---------- |
Review,vol.22,no.4,pp.425–438,2010.
D.Howes,D.Rodenburg,andC.Davies,“Psychophysiologicmeasures
[27] S.Chisholm,J.K.Caird,andJ.Lockhart,“Theeffectsofpracticewith
ofcognitiveloadinphysicianteamleadersduringtraumaresuscitation,”
mp3playersondrivingperformance,”AccidentAnalysis&Prevention,
ComputersinHumanBehavior,vol.111,p.106393,2020.
vol.40,no.2,pp.704–713,2008. [50] J.Zagermann,U.Pfeil,andH.Reiterer,“Measuringcognitiveloadusing
| [28] D. He, | B. Donmez, | C. C. | Liu, and K. | N. Plataniotis, |     | “High cognitive |     |     |     |     |     |     |     |
| ----------- | ---------- | ----- | ----------- | --------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
eyetrackingtechnologyinvisualcomputing,”inProceedingsofthe6th
loadassessmentindriversthroughwirelesselectroencephalographyand
WorkshoponBeyondTimeandErrorsonNovelEvaluationMethodsfor
thevalidationofamodifiedn-backtask,”IEEETransactionsonHuman-
Visualization,2016,pp.78–85.
MachineSystems,vol.49,no.4,pp.362–371,2019.
|     |     |     |     |     |     |     | [51] S. T. Iqbal, | P.  | D. Adamczyk, | X.  | S. Zheng, | and B. P. | Bailey, “Under- |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------------ | --- | --------- | --------- | --------------- |
[29] S.Barua,M.U.Ahmed,andS.Begum,“Classifyingdrivers’cognitive standingchangesinmentalworkloadduringtaskexecution,”Tech.Rep.,
loadusingeegsignals.”inpHealth,2017,pp.99–106.
2004.
[30] N.M.Yusof,J.Karjanto,M.Z.Hassan,J.Terken,F.Delbressine,and
[52] J.Engstro¨m,G.Markkula,T.Victor,andN.Merat,“Effectsofcognitive
M.Rauterberg,“Readingduringfullyautomateddriving:astudyofthe
loadondrivingperformance:Thecognitivecontrolhypothesis,”Human
effectofperipheralvisualandhapticinformationonsituationawareness Factors,vol.59,no.5,pp.734–764,2017.
and mental workload,” IEEE transactions on intelligent transportation [53] P. Sena, M. d’Amore, M. Pappalardo, A. Pellegrino, A. Fiorentino,
systems,vol.23,no.10,pp.19136–19144,2022.
|     |     |     |     |     |     |     | and F. | Villecco, | “Studying | the influence |     | of cognitive | load on driver’s |
| --- | --- | --- | --- | --- | --- | --- | ------ | --------- | --------- | ------------- | --- | ------------ | ---------------- |
[31] Z.Jiang,X.He,C.Lu,B.Zhou,X.Fan,C.Wang,X.Ma,E.C.Ngai,
performancesbyafuzzyanalysisoflanekeepinginadrivesimulation,,”
| and L. | Chen, | “Understanding | drivers’ | visual | and comprehension | loads |     |     |     |     |     |     |     |
| ------ | ----- | -------------- | -------- | ------ | ----------------- | ----- | --- | --- | --- | --- | --- | --- | --- |
IFACProceedingsVolumes,vol.46,no.21,pp.151–156,2013.
intrafficviolationhotspotsleveragingcrowd-baseddrivingsimulation,” [54] L. Caban˜ero, R. Herva´s, I. Gonza´lez, J. Fontecha, T. Monde´jar, and
IEEEtransactionsonintelligenttransportationsystems,vol.23,no.12, J. Bravo, “Analysis of cognitive load using eeg when interacting with
pp.23369–23383,2022. mobiledevices,”MultidisciplinaryDigitalPublishingInstituteProceed-
[32] J.Ayoub,N.Du,X.J.Yang,andF.Zhou,“Predictingdrivertakeover
ings,vol.31,no.1,p.70,2019.
timeinconditionallyautomateddriving,”IEEEtransactionsonintelli-
[55] I.Volman,K.Roelofs,S.Koch,L.Verhagen,andI.Toni,“Anteriorpre-
genttransportationsystems,vol.23,no.7,pp.9580–9589,2022. frontalcortexinhibitionimpairscontroloversocialemotionalactions,”
[33] B. Mehler, B. Reimer, J. F. Coughlin, and J. A. Dusek, “Impact of Currentbiology,vol.21,no.20,pp.1766–1770,2011.
incrementalincreasesincognitiveworkloadonphysiologicalarousaland [56] G.ZhangandA.Etemad,“Deeprecurrentsemi-supervisedeegrepresen-
| performance | in  | young adult | drivers,” | Transportation | Research | Record, |     |     |     |     |     |     |     |
| ----------- | --- | ----------- | --------- | -------------- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
tationlearningforemotionrecognition,”in9thInternationalConference
vol.2138,no.1,pp.6–12,2009.
|                                                                    |     |     |     |     |     |     | on Affective | Computing |     | and Intelligent | Interaction. |     | IEEE, 2021, pp. |
| ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------------ | --------- | --- | --------------- | ------------ | --- | --------------- |
| [34] B.Mehler,B.Reimer,andJ.F.Coughlin,“Sensitivityofphysiological |     |     |     |     |     |     | 1–8.         |           |     |                 |              |     |                 |
measuresfordetectingsystematicvariationsincognitivedemandfrom [57] G. Zhang, V. Davoodnia, and A. Etemad, “Parse: Pairwise alignment
a working memory task: an on-road study across three age groups,” ofrepresentationsinsemi-supervisedeeglearningforemotionrecogni-
HumanFactors,vol.54,no.3,pp.396–412,2012. tion,”IEEETransactionsonAffectiveComputing,2022.
| [35] J. L. | Kolodner, | “An introduction | to  | case-based | reasoning,” | Artificial |     |     |     |     |     |     |     |
| ---------- | --------- | ---------------- | --- | ---------- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
[58] J.R.Stroop,“Studiesofinterferenceinserialverbalreactions.”Journal
IntelligenceReview,vol.6,no.1,pp.3–34,1992. ofExperimentalPsychology,vol.18,no.6,p.643,1935.
[36] M. Braun, J. Schubert, B. Pfleging, and F. Alt, “Improving driver [59] F. Schmiedek, M. Lo¨vde´n, and U. Lindenberger, “A task is a task
emotions with affective strategies,” Multimodal Technologies and In- is a task: putting complex span, n-back, and other working memory
teraction,vol.3,no.1,p.21,2019. indicatorsinpsychometriccontext,”FrontiersinPsychology,vol.5,p.
| [37] C. Nass, | I.-M. | Jonsson, | H. Harris, B. | Reaves, | J. Endo, | S. Brave, and | 1475,2014. |     |     |     |     |     |     |
| ------------- | ----- | -------- | ------------- | ------- | -------- | ------------- | ---------- | --- | --- | --- | --- | --- | --- |
L. Takayama, “Improving automotive safety by pairing driver emotion [60] Y.Santiago-Espada,R.R.Myer,K.A.Latorella,andJ.R.ComstockJr,
and car voice emotion,” in CHI’05 Extended Abstracts on Human “Themulti-attributetaskbatteryii(matb-ii)softwareforhumanperfor-
FactorsinComputingSystems,2005,pp.1973–1976. manceandworkloadresearch:Auser’sguide,”Tech.Rep.,2011.

15
[61] A. Morley, L. Hill, and A. Kaditis, “10-20 system eeg placement,” [85] I.Kalamaras,A.Zamichos,A.Salamanis,A.Drosou,D.D.Kehagias,
EuropeanRespiratorySociety,EuropeanRespiratorySociety,2016. G.Margaritis,S.Papadopoulos,andD.Tzovaras,“Aninteractivevisual
[62] V.Jurcak,D.Tsuzuki,andI.Dan,“10/20,10/10,and10/5systemsrevis- analyticsplatformforsmartintelligenttransportationsystemsmanage-
ited: their validity as relative head-surface-based positioning systems,” ment,”IEEETransactionsonIntelligentTransportationSystems,vol.19,
Neuroimage,vol.34,no.4,pp.1600–1611,2007. no.2,pp.487–496,2017.
[63] A. Burns, B. R. Greene, M. J. McGrath, T. J. O’Shea, B. Kuris, [86] Z.Li,G.Xiong,Y.Tian,Y.Lv,Y.Chen,P.Hui,andX.Su,“Amulti-
streamfeaturefusionapproachfortrafficprediction,”IEEEtransactions
S.M.Ayer,F.Stroiescu,andV.Cionca,“SHIMMER–awirelesssensor
platform for noninvasive biomedical research,” IEEE Sensors Journal, on intelligent transportation systems, vol. 23, no. 2, pp. 1456–1466,
| vol.10,no.9,pp.1527–1534,2010. |     |     |     |     |     |     |     |     | 2020. |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
[64] M. Rizzo, P. A. Sheffield, L. Stierman, and J. Dawson, “Demographic [87] Y. Chen, T. Shu, X. Zhou, X. Zheng, A. Kawai, K. Fueda, Z. Yan,
and driving performance factors in simulator adaptation syndrome,” in W. Liang, I. Kevin, and K. Wang, “Graph attention network with
|         |           |             |     |         |           |            |     |       | spatial-temporal | clustering | for traffic flow forecasting | in intelligent |
| ------- | --------- | ----------- | --- | ------- | --------- | ---------- | --- | ----- | ---------------- | ---------- | ---------------------------- | -------------- |
| Driving | Assesment | Conference, |     | vol. 2, | no. 2003. | University | of  | Iowa, |                  |            |                              |                |
2003. transportationsystem,”IEEETransactionsonIntelligentTransportation
| [65] J.G.Reed-Jones,W.J.Reed-Jones,L.M.Trick,R.Toxopeus,andL.A. |     |     |     |     |     |     |     |     | Systems,2022. |     |     |     |
| --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- |
Vallis,“Comparingtechniquestoreducesimulatoradaptationsyndrome [88] D.P.KingmaandJ.Ba,“Adam:Amethodforstochasticoptimization,”
andimprovenaturalisticbehaviourduringsimulateddriving,”inDriving InternationalConferenceonLearningRepresentations,2015.
[89] W.-L.Zheng,W.Liu,Y.Lu,B.-L.Lu,andA.Cichocki,“Emotionmeter:
| AssesmentConference,vol.5,no.2009. |     |     |     |     | UniversityofIowa,2009. |     |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
T.G.Dobie,Motionsickness:amotionadaptationsyndrome. A multimodal framework for recognizing human emotions,” IEEE
| [66] |     |     |     |     |     |     | Springer, |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
2019,vol.6. TransactionsonCybernetics,vol.49,no.3,pp.1110–1122,2018.
[67] S.V.Cobb,S.Nichols,A.Ramsey,andJ.R.Wilson,“Virtualreality-
| induced | symptoms | and | effects | (vrise),” | Presence: | Teleoperators |     | &   |     |     |     |     |
| ------- | -------- | --- | ------- | --------- | --------- | ------------- | --- | --- | --- | --- | --- | --- |
VirtualEnvironments,vol.8,no.2,pp.169–186,1999.
| [68] G. Ga´lvez-Garc´ıa, |     | J. Albayay, |     | L. Rehbein, | and | F. Tornay, | “Mitigating |     |     |     |     |     |
| ------------------------ | --- | ----------- | --- | ----------- | --- | ---------- | ----------- | --- | --- | --- | --- | --- |
simulatoradaptationsyndromebymeansoftactilestimulation,”Applied
Ergonomics,vol.58,pp.13–17,2017.
[69] L.Frank,R.S.Kennedy,R.S.Kellogg,andM.E.McCauley,“Simulator PrithilaAngkanPrithilaAngkaniscurrentlypursu-
sickness:Areactiontoatransformedperceptualworld.1.scopeofthe ingherPh.D.atQueen’sUniversityinCanadainthe
problem,”ESSEXCORPORLANDOFL,Tech.Rep.,1983. DepartmentofElectricalandComputerEngineering.
[70] R. S. Kennedy, N. E. Lane, K. S. Berbaum, and M. G. Lilienthal, She received her master’s degree from the same
“Simulatorsicknessquestionnaire:Anenhancedmethodforquantifying departmentatQueen’sUniversityandherbachelor’s
simulator sickness,” The International Journal of Aviation Psychology, from BRAC University, Bangladesh. Currently, she
vol.3,no.3,pp.203–220,1993. is a member of Ambient Intelligence and Interac-
[71] P. J. Gianaros, E. R. Muth, J. T. Mordkoff, M. E. Levine, and R. M. tiveMachinesLaboratory(AiimLab)andIngenuity
|     |     |     |     |     |     |     |     |     |     | Labs Research | Institute at Queen’s | University. Her |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------------------- | --------------- |
Stern,“Aquestionnairefortheassessmentofthemultipledimensionsof
motionsickness,”Aviation,Space,andEnvironmentalMedicine,vol.72, researchfocusesonBrain-ComputerInterface,Arti-
no.2,p.115,2001. ficial Intelligence, Cognitive Load Analysis, Affec-
[72] F.G.Paas,“Trainingstrategiesforattainingtransferofproblem-solving tive Computing, and Deep Learning utilizing Electroencephalogram (EEG)
| skill | in statistics: | a cognitive-load |     | approach.” |     | Journal | of Educational |     | signals. |     |     |     |
| ----- | -------------- | ---------------- | --- | ---------- | --- | ------- | -------------- | --- | -------- | --- | --- | --- |
Psychology,vol.84,no.4,p.429,1992.
| [73] N. Thakor, | J.  | Webster,   | and         | W. Tompkins, | “Optimal       |     | qrs detector,” |        |     |     |     |     |
| --------------- | --- | ---------- | ----------- | ------------ | -------------- | --- | -------------- | ------ | --- | --- | --- | --- |
| Medical         | and | Biological | Engineering |              | and Computing, |     | vol. 21,       | no. 3, |     |     |     |     |
pp.343–350,1983.
| [74] H. G. | Goovaerts, | H. H. | Ros, T. | J. Van | Den Akker, | and | H. Schneider, |     |     |     |     |     |
| ---------- | ---------- | ----- | ------- | ------ | ---------- | --- | ------------- | --- | --- | --- | --- | --- |
“Adigitalqrsdetectorbasedontheprincipleofcontourlimiting,”IEEE
TransactionsonBiomedicalEngineering,no.2,pp.154–160,1976.
[75] C.L.Lim,C.Rennie,R.J.Barry,H.Bahramali,I.Lazzaro,B.Manor,
andE.Gordon,“Decomposingskinconductanceintotonicandphasic BehnamBehinaeinBehnamBehinaeinreceivedhis
components,”InternationalJournalofPsychophysiology,vol.25,no.2, PhD from Queen’s University in 2016 and was a
| pp.97–109,1997. |     |     |     |     |     |     |     |     |     | post-doctoralfellowinQDESandAiimLabs.Heis |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- |
currentlywithHuaweiCanada.Hisresearchinterests
| [76] C. E. | Shannon, | “A mathematical |     | theory | of communication,” |     | The | Bell |     |     |     |     |
| ---------- | -------- | --------------- | --- | ------ | ------------------ | --- | --- | ---- | --- | --- | --- | --- |
SystemTechnicalJournal,vol.27,no.3,pp.379–423,1948. include affect computing, wearable technologies,
[77] B.Hjorth,“Eeganalysisbasedontimedomainproperties,”Electroen- and the application of deep learning in analyzing
cephalography and Clinical Neurophysiology, vol. 29, no. 3, pp. 306– sequentialdata.
310,1970.
| [78] A. Lempel | and | J. Ziv, | “On the | complexity | of  | finite sequences,” |     | IEEE |     |     |     |     |
| -------------- | --- | ------- | ------- | ---------- | --- | ------------------ | --- | ---- | --- | --- | --- | --- |
TransactionsonInformationTheory,vol.22,no.1,pp.75–81,1976.
[79] F.KasparandH.Schuster,“Easilycalculablemeasureforthecomplexity
| of spatiotemporal |     | patterns,” | Physical | Review | A,  | vol. 36, | no. 2, | p. 842, |     |     |     |     |
| ----------------- | --- | ---------- | -------- | ------ | --- | -------- | ------ | ------- | --- | --- | --- | --- |
1987.
| [80] T. Higuchi, | “Approach |         | to an irregular |     | time series | on   | the basis | of the |     |     |     |     |
| ---------------- | --------- | ------- | --------------- | --- | ----------- | ---- | --------- | ------ | --- | --- | --- | --- |
| fractal          | theory,”  | Physica | D: Nonlinear    |     | Phenomena,  | vol. | 31, no.   | 2, pp. |     |     |     |     |
277–283,1988.
[81] A.H.Al-Nuaimi,E.Jammeh,L.Sun,andE.Ifeachor,“Higuchifractal Zunayed Mahmud ZunayedMahmudreceivedthe
dimensionoftheelectroencephalogramasabiomarkerforearlydetec- M.A.Sc. degree from the Department of Electrical
tionofalzheimer’sdisease,”in39thAnnualInternationalConferenceof and Computer Engineering at Queen’s University,
theIEEEEngineeringinMedicineandBiologySociety. IEEE,2017, Canada,in2022.Concurrently,heservedasaStu-
| pp.2320–2324. |     |     |     |     |     |     |     |     |     | dent Researcher | at the Ingenuity | Labs Research |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ---------------- | ------------- |
[82] E. Shamsi, M. A. Ahmadi-Pajouh, and T. S. Ala, “Higuchi fractal Institute, Canada. He earned his bachelor’s degree
dimension: An efficient approach to detection of brain entrainment to fromtheDepartmentofElectricalandElectronicEn-
thetabinauralbeats,”BiomedicalSignalProcessingandControl,vol.68, gineeringatBRACUniversity,Bangladesh,in2015.
| p.102580,2021. |     |     |     |     |     |     |     |     |     | HeiscurrentlyworkingasanAssociateResearcher |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- |
atHuaweiTechnologiesCanada.Hisresearchinter-
| [83] F. Shaffer | and | J. P. Ginsberg, |     | “An overview |     | of heart | rate variability |     |     |     |     |     |
| --------------- | --- | --------------- | --- | ------------ | --- | -------- | ---------------- | --- | --- | --- | --- | --- |
metricsandnorms,”FrontiersinPublicHealth,p.258,2017. estsincludecomputervision,deeplearning,2D/3D
[84] P. Sarkar and A. Etemad, “Self-supervised ecg representation learning objectdetectionandrecognition,3Dreconstruction,andgazeestimation.
| for emotion | recognition,” |     | IEEE | Transactions | on  | Affective | Computing, |     |     |     |     |     |
| ----------- | ------------- | --- | ---- | ------------ | --- | --------- | ---------- | --- | --- | --- | --- | --- |
2020.

16
Anubhav Bhatti Anubhav Bhatti is a machine
learning engineer at SpassMed Inc. His journey in
machine learning previously led him to the Vector
Institute as a Machine Learning Associate. He re-
ceivedhisMaster’sinArtificialIntelligencefromthe
ElectricalandComputerEngineeringDepartmentat
Queen’s University, Canada, and his bachelor’s in
electricalengineeringfromtheNationalInstituteof
Technology, India. In his research work at Vector
InstituteandSpassMed,heleverageshisexpertisein
Large Language Models, Generative AI, and Time
Series Forecasting in designing and implementing deep-learning models for
theearlydetectionofcriticaleventsinpatients.WhileatQueen’sUniversity
andIngenuityLabsResearchInstitute,heextensivelyresearchedmultimodal
time-seriesphysiologicaldatafusiontechniquesandaffectivecomputing.
Dirk Rodenburg Dr. Rodenburg is an Adjunct
ProfessorwiththeQueen’sUniversitySmithSchool
ofEngineering’sDepartmentofChemicalEngineer-
ing, and the Faculty of Arts and Science. Dirk’s
research interests include human performance, ex-
pertise, cognition, real time data analytics, data
feedback, human-computer interaction, and ethics
andprivacy.Inadditiontohisacademicbackground,
he has twenty years of experience as a software
entrepreneurandconsultantwithinacademia,educa-
tional technology, financial services, biotechnology
and scientific instruments, and has played an integral role in the launch of
threehighlyinnovativestartups.DirkholdsanMAinAdultEducationfrom
theUniversityofBritishColumbiaandaPhDfromtheFacultyofInformation
fromtheUniversityofToronto.
PaulHunglerDr.PaulHunglerisanAssociatePro-
fessor in the Department of Chemical Engineering
and Ingenuity Labs at Smith Engineering, Queen’s
University. Dr. Hungler’s research is focused on
thedevelopmentofintelligent,dynamicallyadaptive
simulationtoenhanceeducationandtraining.
Ali Etemad Dr. Etemad is an Associate Professor
attheDepartmentofElectricalandComputerEngi-
neering, Queen’s University. He holds an endowed
professershipofMitchellProfessorinAIforHuman
Sensing and Understanding. He leads the Ambient
IntelligenceandInteractiveMachines(Aiim)lab.He
receivedhisM.A.Sc.andPh.D.degreesinElectrical
and Computer Engineering from Carleton Univer-
sity,Ottawa,Canada,in2009and2014,respectively.
Hismainareasofresearcharemachinelearningand
deep learning focused on human-centered applica-
tionswithwearables,smartdevices,andsmartenvironments.Priortojoining
Queen’s,heheldseveralindustrialpositionsasleadscientist.Hehaspublished
over160papersintopvenuesinthearea,isaco-inventorof10patents,and
hasgivenover25invitedtalksatdifferentvenues.Dr.EtemadisanAssociate
EditorforIEEETransactionsonAffectiveComputingandIEEETransactions
on Artificial Intelligence. He has served as a PC member/reviewer, and has
heldorganizingrolesatvariousvenues.Hehasreceivedanumberofawards
including Supervisor of the Year Award (at Queen’s), Instructor of the Year
Award(atQueen’s),andseveralBestPaperAwards(e.g.,atACMICMI’23).
Dr. Etemad’s lab and research program have been funded by the Natural
Sciences and Engineering Research Council (NSERC) of Canada, Ontario
Centers of Excellence (OCE), Canadian Foundation for Innovation (CFI),
Mitacs,andotherorganizations,aswellastheprivatesector.