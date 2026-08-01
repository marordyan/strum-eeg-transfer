Personal and Ubiquitous Computing (2023) 27:2027–2041
https://doi.org/10.1007/s00779-020-01455-7
ORIGINALARTICLE
A framework to estimate cognitive load using physiological data
MuneebImtiazAhmad1,2 ·IngoKeller1·DavidA.Robb1·KatrinS.Lohan3,4
Received:27November2019/Accepted:5September2020/ Published online: 27 September 2020
©TheAuthor(s)2020
Abstract
Cognitive load has been widely studied to help understand human performance. It is desirable to monitor user cognitive
load in applications such as automation, robotics, and aerospace to achieve operational safety and to improve user
experience. This can allow efficient workload management and can help to avoid or to reduce human error. However,
tracking cognitive load in real time with high accuracy remains a challenge. Hence, we propose a framework to detect
cognitive load by non-intrusively measuring physiological data from the eyes and heart. We exemplify and evaluate the
framework where participants engage in a task that induces different levels of cognitive load. The framework uses a set
of classifiers to accurately predict low, medium and high levels of cognitive load. The classifiers achieve high predictive
accuracy.Inparticular,RandomForestandNaiveBayesperformedbestwithaccuraciesof91.66%and85.83%respectively.
Furthermore,wefoundthat,whilemeanpupildiameterchangeforbothrightandlefteyewerethemostprominentfeatures,
blinking rate also made a moderately important contribution to this highly accurate prediction of low, medium and high
cognitiveload.Theexistingresultsonaccuracyconsiderablyoutperformpriorapproachesanddemonstratetheapplicability
ofourframeworktodetectcognitiveload.
Keywords Cognitiveload·Framework·Physiologicaldata·Human-computerinteraction
1Introduction demanding a high amount of mental effort [4]. In general,
CL refers to the load placed on the user’s working mem-
Inthepastfewdecades,cognitiveload(CL)hasbeenshown ory, also viewed as short-term memory, during a task [53].
to negatively impact human performance in various tasks ThesignificanceofmeasuringCLhasbeenwelldescribed
inthepastduetoitsapplicationundervariouscontextssuch
(cid:2) MuneebImtiazAhmad as problem-solving, instructional design, multimedia, air-
m.ahmad@hw.ac.uk craft,andautomation[42].CLcanbemonitoredinrealtime
asamethodtocapturetheautomationexperience[15,57].
IngoKeller
Accurate measurement of CL can be used to apply mitiga-
i.keller@hw.ac.uk
tionstrategies,suchastheadaptationoftheuserinterfacein
DavidA.Robb responsetochangesinCL[36].Oneapproachistopresent
d.a.robb@hw.ac.uk
information differently for a naive user vs. an expert user.
This is needed because an expert user may view the task
KatrinLohan
k.lohan@hw.ac.uk as trivial, and this can cause boredom which may induce
cognitiveunder-load[57].Thepurposeofsuchstrategiesis
toimproveperformance,operationalefficiency,andopera-
1 EdinburghCenterforRobotics,Heriot-WattUniversity,
tional safety, while reducing failures [50]. For example, a
Edinburgh,UK
driverinanautonomousvehicleneedstomonitorandsuper-
2 DepartmentofComputerScience,SwanseaUniversity,
vise automation to achieve operational safety. However,
Swansea,UK
driversmayexperiencecognitiveunder-loadovertime.This
3 DepartmentofMathematicalandComputerScience,
raises concern about their ability to consistently monitor
Heriot-WattUniversity,Edinburgh,UK
automation, possibly resulting in an accident. Other appli-
4 EMSInstituteforDevelopmentofMechatronicSystems,
cation areas include the deployment of robots in extreme
NTBUniversityofAppliedSciencesinTechnology,
Buchs,Switzerland environmentsandinautomatedenvironmentssuchassmart

| 2028 |     |     |     |     |     |     |     |     |     |     | Pers Ubiquit Comput (2023) 27:2027–2041 |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- |
factories,wheresupervisorsobserveautonomousoperations behaviour data while automatically taking the task into
[2, 20]. As a result, intelligent user interfaces are needed account.Ourcontributionsarethreefold:
toprovidesituationawarenesstothesupervisors.Thiswill
| help them | to observe, |     | analyse, | and supervise |     | autonomous |     |     |                  |     |           |           |          |
| --------- | ----------- | --- | -------- | ------------- | --- | ---------- | --- | --- | ---------------- | --- | --------- | --------- | -------- |
|           |             |     |          |               |     |            |     |     | – We demonstrate |     | a generic | framework | to clas- |
operationssafelyandefficientlybymanagingtheirCL[35].
sifylow,mediumandhighlevelsofCL.
| CL has | been | classified | into | three | different | types: | (1) |     |     |     |     |     |     |
| ------ | ---- | ---------- | ---- | ----- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
– Wepresenttheresultsofanevaluationthrough
| intrinsic   | load,     | (2) extraneous |       | load, and | (3)           | germane    | load    |     |              |       |            |                 |             |
| ----------- | --------- | -------------- | ----- | --------- | ------------- | ---------- | ------- | --- | ------------ | ----- | ---------- | --------------- | ----------- |
|             |           |                |       |           |               |            |         |     | the creation |       | of a novel | task            | to test our |
| [52]. While | intrinsic | load           | stems | from      | the           | complexity | of      |     |              |       |            |                 |             |
|             |           |                |       |           |               |            |         |     | framework    | using | eye-       | and heart-based | data.       |
| the task    | and its   | association    | with  | the user, | extraneous    |            | load    |     |              |       |            |                 |             |
|             |           |                |       |           |               |            |         |     | To promote   |       | reuse, we  | make our        | task and    |
| is caused   | by the    | presentation   | style | of        | the material. |            | Lastly, |     |              |       |            |                 |             |
sensorapplicationcodeinadditiontothescripts
| germane    | load | refers to | the ability | of  | the       | user       | to fully |     |                |     |            |          |          |
| ---------- | ---- | --------- | ----------- | --- | --------- | ---------- | -------- | --- | -------------- | --- | ---------- | -------- | -------- |
|            |      |           |             |     |           |            |          |     | for generation |     | of stimuli | and data | analysis |
| understand | the  | material. | We believe  |     | that both | extraneous |          |     |                |     |            |          |          |
available.
| load and | germane | load | are relevant |     | factors | affecting | the |     |           |     |         |                    |     |
| -------- | ------- | ---- | ------------ | --- | ------- | --------- | --- | --- | --------- | --- | ------- | ------------------ | --- |
|          |         |      |              |     |         |           |     |     | – We make | the | dataset | publicly available | for |
operators’interaction.Forexample,aninterfacepresenting
|     |     |     |     |     |     |     |     |     | community | to  | use in | order to classify | CL. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------ | ----------------- | --- |
datainaparticularmannercanresultinanincreaseinboth
|     |     |     |     |     |     |     |     |     | We further | show | that | the evaluation | of the |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ---- | -------------- | ------ |
extraneousandgermaneload,whichcouldinducehighCL.
|               |     |         |           |     |         |          |     |     | framework | using | the | dataset achieves | high |
| ------------- | --- | ------- | --------- | --- | ------- | -------- | --- | --- | --------- | ----- | --- | ---------------- | ---- |
| Consequently, |     | we need | to reduce | CL  | through | creation | of  |     |           |       |     |                  |      |
predictiveaccuracyontheexemplartask.
intelligentuserinterfacesthatmeasureCLinrealtimeand
adjustthepresentationaccordingly.However,tothebestof
our knowledge, it remains a challenge to measure CL in a While we have used eye- and heart-based data in this
robustandnon-intrusivemanner. current work, we understand that data collected from
ToaddressthischallengeofclassifyingCL,wedesigned multiple sources synchronously can further improve the
a framework (Fig. 1) that applies machine learning to robustness and general applicability of our framework for
the physiological data gathered from available state-of- differentkindsofstimuli.
| the-art sensing |         | technologies. | The    | rationale | for         | calling | the   |     |     |     |     |     |     |
| --------------- | ------- | ------------- | ------ | --------- | ----------- | ------- | ----- | --- | --- | --- | --- | --- | --- |
| framework       | generic | lies          | in the | concept   | of avoiding |         | task- |     |     |     |     |     |     |
2Relatedwork
| or stimuli-dependent |     | physiological |     | behaviour. |     | In principle, |     |     |     |     |     |     |     |
| -------------------- | --- | ------------- | --- | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
theframeworkcanbeappliedacrossdifferentsettings.For
example, it could be used to monitor a driver’s CL in Historically,CLwasintroducedinthecontextofproblem-
an autonomous vehicle or a supervisor’s CL in a control solving and instructional design to understand its effects
room to either ensure operational safety or to reduce on learning [51]. However, CL was later studied as a
mistakes.Theframeworkincorporatesmachinelearningto constructofoperators’(e.g.pilots’)mentalworkload.Itwas
|     |     |     |     |     |     |     |     | found | that increased | CL  | has an | adverse effect | on operator |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------------- | --- | ------ | -------------- | ----------- |
understandtherelevantfeaturesinarangeofphysiological
Fig.1 Aframeworktoestimatecognitiveloadusingphysiologicaldata

Pers Ubiquit Comput (2023) 27:2027–2041 2029
performance[39].ThetermCL,hasbeenreferredtounder understand that identifying CL based on these behaviours
variousapplicationcontexts,withterminologysuchaswork is, perhaps, relevant but is also task dependent. Linguistic
load and mental load. However, these all refer to the same behaviours,whilenon-intrusive,areonlyrelevantinsettings
general concept [14]. In the rest of this section, we set out wherespeechinputisused.Webelievethatthesebehaviours
methodsusedinpreviousresearchtomeasureCLinhumans canbeusedinourframeworkbecausespeechinputcanbe
inexperimentalsettings. collectedunobtrusively.However,wedonotusetheminthe
currentdemonstrationoftheframeworkduetothenatureof
2.1Subjectivequestionnaire-basedmethods thetask.
Subjectiveratingquestionnaireshavebeenthemostpopular 2.4Physiologicalbehaviour-basedmethods
mechanism to measure CL, perhaps due to their ease of
use [42]. The NASA Task Load Index is one of the most The most commonly used method to measure CL is to
commonly used questionnaires to measure subjective CL observe and to report on the changes in humans’ physio-
[19]. The questionnaire consists of rating six constructs: logicalbehaviours[42].Thesephysiologicalbehavioursare
(1) mental demand, (2) physical demand, (3) temporal mostly based on changes in the measurements taken from
demand, (4) effort, (5) performance and (6) frustration, fourdifferenthumanorgans:(1)brain,throughmeasuring
each being rated from low to high [19]. Other known neurological activity via an electroencephalogram (EEG);
questionnaires include the Cognitive Load Component (2) heart, through measuring heart rate (HR), or heart rate
survey that separates the three classifications of load: variability (HRV); (3) skin, through measuring galvanic
intrinsic, extraneous, and germane load. This self-report- skin conductance (GSR); and (4) eyes, through measuring
based measure is particularly relevant to instructional eye movements, mean pupil diameter change (MPDC), or
settings [31]. It is, however, interesting to note that rating blinkingrate(BR).
scales are not generally regarded as reliable measures of Prior findings on the variation of HRV during a range
CL. Researchers are critical of using CL subjectively at ofcomputerizedtaskshaveshownthatreductioninHRVis
the end of the task because changes in CL are momentary. attributed to higher CL [40]. Cranford et al. [10] reported
Therefore,theyshouldbeestimatedinrealtime[37]. that there was an increase in HR with an increase in task
difficulty.Thissuggeststhatastaskdifficultyincreases,in
2.2Performance-basedmethods other words, as CL grows, it results in an increase in HR
and reduction in HRV. We also found several experiments
Prior findings suggest a relationship between CL and a in the literature that report an increase in MPDC in a
user’s task performance; therefore, CL can be measured situationdemandinghighermentalworkload[46,47].Past
by measuring performance [14]. Pass et al. divided findingsalsoindicatethatBRdecreasesinthecaseofhigher
performance into sub-classes: one refers to the task mental load [23]. For GSR, it has been found that GSR
performance and the other refers to the performance readings increase with an increase in CL [48]. Similarly,
measuresderivedfromtaskperformance(i.e.responsetime, the EEG theta wave activity increases in the frontal region
error-rate,oraccuracy).Passetal.believethatthesefactors with an increase in the CL [16]. In summary, there is
can contribute to estimating CL and are highly sensitive empirical evidence from past research implying that the
and reliable [42]. However, while we understand that such changes in the measurements of physiological behaviours
factors can be used in real time, these are task-dependent can be attributed both to CL, and to various levels of
measures which cannot be used generally in the case of mental processing. It is also important to note that the
adaptingtechnology. existing sensing technologies work well and provide an
accurate representation of the particular behaviours [24,
2.3Speech-basedmethods 54]. Furthermore, with the advancement of design and
technology,solutionsarenowavailabletocollectsuchdata
Human speech behaviours are observable as measures inlessinvasiveways.
of CL [58]. These include language-based and emotion- Inrelationtoourwork,theexistingliteratureshowsthat
based behaviours. The language-based behaviours include changes in one physiological behaviour may be related to
hesitations, increased use of pauses, decreased articulation another observable physiological behaviour. For instance,
rate, decreased speech rate, self-corrections and several Siegleetal.[49]showedthatthereisarelationshipbetween
others [3, 26, 29, 34]. The emotion-based behaviours MPDC and BR in a digit-sorting task. Therefore, in this
includeincreaseduseofnegativeemotions,decreaseduseof paper, we collected data on a variety of physiological
positiveemotions,andseveralotherindicators[27,28].We behaviours and used the data to classify low, medium and

| 2030 |     |     |     |     |     |     |     |     |     | Pers Ubiquit Comput (2023) 27:2027–2041 |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- |
highlevelsofCL.Therationaleforclassifyingthreelevels We also see studies that have been conducted to collect
of CL is grounded in one of the most recent works on datafromoneofthephysiologicalbehaviourssuchaseye-
predictingCLinthewild[14]. based measures, GSR measures, or speech measures to
|     |     |     |     |     |     |     |     | classify | CL [7]. Although | the results from | these studies |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------------- | ---------------- | ------------- |
Machine learning to estimate CL In the past, researchers are encouraging, the accuracy is relatively low. The most
have used machine learning-based approaches to estimate recent work on CL estimation in a driving task was based
CL[18,41,56,59].Zhangetal.[59]proposedanadaptive on using deep learning to extract the pupil size from a
support vector machine (SVM)-based method to classify video.ItthenusedaclassificationalgorithmtoclassifyCL
operator mental workload by using electroencephalogram as low, medium and high [14]. This work is closest to our
(EEG),electrocardiogramandelectrooculographysignalsin approachintermsofpredictingthreelevelsofCL,however,
a simulated human-machine system. However, three of the the method only takes pupil size as input. We understand
aforementioned papers on these techniques used data from that this method is suitable for driving but may not be
brain-specificEEGsensors[41,56,59]. suitable for other tasks, because the existing literature on
Recently, in 2018, Heard et al. [21] published a survey the CL measurement indicates that measurements of some
on workload assessment algorithms. These algorithms use physiologicalbehavioursmaynotbesuitableforsometasks
| a range     | of machine | learning   |                | methods    | to   | predict  | different | [42]. |     |     |     |
| ----------- | ---------- | ---------- | -------------- | ---------- | ---- | -------- | --------- | ----- | --- | --- | --- |
| levels of   | workload.  |            | In particular, |            | the  | survey   | enlisted  |       |     |     |     |
| 24 workload |            | assessment |                | algorithms | that | achieved | an        |       |     |     |     |
accuracy between 60 and 90%. The assessment algorithms Our approach encourages the use of a range of
establishedabaseline,orgroundtruth,forthemeasurement features (physiological behaviours collected non-
of CL by enabling participants to stare at the screen or to intrusively) and later applies feature elimination
involve them in a task inducing low CL such as adding methods to determine the indicative ones in the
twonumbers.However,itisimportanttonotethattheterm givencontext.Weshowthatthisapproachcanyield
“workload” is vast in its scope and has seven different betteraccuracyonadatasetthatisbasedonalarge
decompositions, CL or cognitive workload is one of them. cohortofparticipants.
| Our work | differs | from | prior | work | due | to the | following |     |     |     |     |
| -------- | ------- | ---- | ----- | ---- | --- | ------ | --------- | --- | --- | --- | --- |
reasons.Firstly,theaccuracyresultsarebasedonsmalluser
| groups (on | average, | 8–10 | with | lows | of  | 3 and | 4), which |     |     |     |     |
| ---------- | -------- | ---- | ---- | ---- | --- | ----- | --------- | --- | --- | --- | --- |
are known to have low statistical power when developing 3Settingandmethod
techniquesforwideruse.Secondly,onlythreestudieswere
carried out on CL-based tasks to estimate CL. Thirdly, 3.1Cognitiveloadframework
| within those | 24  | algorithms, |     | the algorithms |     | achieving | an  |     |     |     |     |
| ------------ | --- | ----------- | --- | -------------- | --- | --------- | --- | --- | --- | --- | --- |
accuracy over 90% cannot be applied in real time because The framework (Fig. 1) has three modules: (1) stimuli, (2)
they use the NASA TLX questionnaire data. Others were sensinganddatacollectionandprocessing,and(3)applying
based on predicting only two-levels of CL (low vs high). machinelearningfordetectingCL.
| Lastly, prior     | work   | uses    | SVM      | and   | suffers  | from   | overfitting. |              |     |     |     |
| ----------------- | ------ | ------- | -------- | ----- | -------- | ------ | ------------ | ------------ | --- | --- | --- |
| These highlighted |        | aspects | of       | the   | previous | work   | indicate     | 3.1.1Stimuli |     |     |     |
| that we           | should | create  | datasets | based | on       | a high | number       |              |     |     |     |
of participants to create robust measurements of CL. In The first module consists of an external stimulus or a
addition, there is a need to train a model to predict three tasktoinduceCL.Aspreviouslyhighlighted,physiological
levelsofCLinrealtime.Moreover,moreresearchisneeded behaviourstendtobetask-orstimuli-dependent.Hence,the
withfeaturesbasedonthecombinationofheartandeyedata framework does not propose a specific stimulus. Instead,
asthisisanicheareathathasnotbeenresearchedstrongly it removes the context-dependency to classify CL. This
[21].Furthermore,weneedtousearangeofphysiological suggests that the framework can, in principle, be applied
behaviours to collect data in a non-intrusive way to extend regardlessofthetask.
| their use | in real-settings. |     | In  | the real | world, | which | is the |     |     |     |     |
| --------- | ----------------- | --- | --- | -------- | ------ | ----- | ------ | --- | --- | --- | --- |
focus of our work (e.g. applications to supervise and plan 3.1.2Sensinganddataprocessing
| missions | for robots | in  | extreme | environments |     | or  | to manage |     |     |     |     |
| -------- | ---------- | --- | ------- | ------------ | --- | --- | --------- | --- | --- | --- | --- |
autonomoussystemsoperationsinsmartfactories),theuse In the sensing module, we used state-of-the-art sensing
of EEG sensors are impractical, therefore we do not use technology to collect eye- and heart-based data. It is
them. Most of the prior work described above has focused important to note that our sensing module is not limited
on them (21/24 and 3/3 for CL tasks), which also sets us to only two measurements and can accommodate other
| apart[21]. |     |     |     |     |     |     |     | physiologicalbehaviours. |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- |

| Pers Ubiquit Comput (2023) 27:2027–2041 |     |     |     |     |     | 2031 |
| --------------------------------------- | --- | --- | --- | --- | --- | ---- |
We capture the data from various sensing devices once the basic calibration was performed, the participants
consisting of raw signals. Data from these sources need to viewed a changing full-screen display of white, black,
besynchronizedandcleaned.Inthismodule,wefirsthandle and grey colors while their data on eye and heart activity
datasynchronicitythroughapplyingtime-framestoourraw was recorded. In the trial phase, participants first read an
signals and later apply various widely used techniques to introduction. Then, they were asked to undertake simpler
cleanandfilterourdata. versionsofstimuliitemsthanthosewhichtheywouldmeet
|     |     | in the | main task phase. This | was done | to familiarize | them |
| --- | --- | ------ | --------------------- | -------- | -------------- | ---- |
3.1.3Machinelearningfordetectingcognitiveload with the nature of the task. Lastly, the task phase was a
|     |     | simple | game-based task to | recognize | correct and | made-up |
| --- | --- | ------ | ------------------ | --------- | ----------- | ------- |
Thismoduleconsistsoftwosub-modules:(1)featurerefine- words,andcorrectandincorrectsentences.Ourtaskhadsix
mentand(2)supervisedlearningclassification.Thefeature differentitemtypesasshowninTable1.Eachitemtypehad
refinement module selects the best or worst performing 20wordsorsentences.Thetaskwasdesignedtoinducetwo
features.VariousalgorithmssuchasSelectKBest,recursive componentsfromcognitiveloadtheory:(1)thecomplexity
featureelimination,correlation-basedfeatureselection,and ofthetaskwasinherentlydifficult,inducingintrinsicload,
others can be used for this. It is important to use feature and (2) the presentation of the words and sentences in an
refinementmethodsasphysiologicalbehaviourstendtobe arbitraryorderinducedextraneousload.
task dependent. For instance, HR and HRV are insensi- We used the list of words from the British National
tive to the instantaneous load caused by the fluctuations Corpus[8]tocreatetheword-basedtaskitems.Wedeveloped
every time someone works on a task, hence they can be a simple script in python to select 20 words (nouns) of
task dependent [42]. Similarly, pupil diameter (PD) is sen- length 10 with frequency ranging from 1013 to 1026 in
sitive to changes in light and also varies with age [33]. the corpus. We also looked into the movie review dataset
Additionally, PD may also be unsuitable for some tasks. [44]topreparethesentence-basedtaskitems.Wedeveloped
Consequently,thefeaturerefinementsub-moduleisneeded anotherscripttoselectsentencescontaining10wordseach.
and can help improve the robustness of CL detection. Fol- We removed sentences from the dataset containing words
lowing the feature refinement step, the framework uses a having apostrophes,quotes,numbers,etc.Also,weremovedv
range of supervised learning methods such Naive Bayes, sentenceshavingveryshortwordssuchas“a”or“I”.Finally,
LogisticalRegression,SupportVectorMachine,andothers we selected the first 20 out of the remaining 54 sentences.
toclassifylow,mediumandhighlevelsofCL. It is important to add that the rationale for our choice of
|     |     | words | was based on our | understanding | of a recent | study |
| --- | --- | ----- | ---------------- | ------------- | ----------- | ----- |
3.2ApplyingtheCLdetectionframework thatindicatedthatmoresurprisingwordstakelongertoread
|     |     | and result | in increasing pupil | sizes [13]. | Therefore, | as one |
| --- | --- | ---------- | ------------------- | ----------- | ---------- | ------ |
Ourstimulihadthreephases:(1)therestphase,(2)thetrial of our features to estimate CL is pupil sizes, this justifies
phase,and(3)thetaskphase.Thesewereusedtogenerate
|     |     | our choice | of the task. Furthermore, |     | the rationale | for the |
| --- | --- | ---------- | ------------------------- | --- | ------------- | ------- |
threelevelsofCL,Low,MediumandHighrespectively.The character length of the word was based on maintaining the
data collected from these three phases were used later to difficultyofthewordsatacertainlevel.
trainandtestthemachinelearningclassifiers.Itisimportant
to note that the duration of each phase was different, We emphasise that our task is novel in terms of
therefore, we normalized all the physiological behaviour its use in inducing CL and this new task helps to
datatoavoidanybias.Oneoftheinitialstepswastoperform demonstrate the framework by the creation of a
calibration with the eye tracking device. In the rest phase, datasettoclassifythreelevelsofCL.
Table1 Taskitemoverview
| Itemtype | Content                            |     | Example    |     |     |     |
| -------- | ---------------------------------- | --- | ---------- | --- | --- | --- |
| 1        | acorrectEnglishword                |     | reluctance |     |     |     |
| 2        | as1butwiththemiddlelettersswitched |     | relutcance |     |     |     |
| 3        | as1butwithscrambledletters         |     | anctucerel |     |     |     |
| 4        | anarbitrarymnemonicword            |     | lcwvcdkxob |     |     |     |
5 acorrectEnglishsentencefromamoviereviewdataset[44] theonlyproblemscomeduringthefirstandthirdacts
6 as5butwithrearrangedwordsrenderingthemincorrect theonlyproblemscomefirstandthirdactstheduring
Boldlettersrefertothechangesinstimulusforeachitemtypeusedinthetask

| 2032 |     |     |     |     |     |     |     |     |     |     | Pers Ubiquit Comput (2023) 27:2027–2041 |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- |
Thesensingmoduleusedthestate-of-the-arteyetracker the previously described cleaning, and three step filtering
- Tobii Pro Glasses 2 Eye Tracker (Eye Tracker) to collect method,tocleanandfiltertherawdata.Welatercomputed
onPDandBR.Inaddition,weusedtheEliteHRVCorSense the MPDC, for each task phase, as the ratio between the
device [25] to collect data on HR and HRV. The sensing overallmeanPD(overallthreetaskphases),andthemean
devicescanbeseeninFig.3. PD while performing each of the individual phases of the
|     |     |     |     |     |     |     |     | task. Our | method | to  | compute | the MPDC | is  | grounded in |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | --- | ------- | -------- | --- | ----------- |
Measuringpupildiameter We used the following steps to literatureasitfollowstheapproachappliedbyPalinkoetal.
[43].
| clean the | data | collected | from | the Eye | Tracker | as  | described |     |     |     |     |     |     |     |
| --------- | ---- | --------- | ---- | ------- | ------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
inpriorliterature[30].Inthefirststep,wepreparedtheraw
|         |       |          |          |           |      |     |            | Measuring | blink | rate | To calculate | BR, | we used | the Eye |
| ------- | ----- | -------- | -------- | --------- | ---- | --- | ---------- | --------- | ----- | ---- | ------------ | --- | ------- | ------- |
| data on | pupil | size for | the left | and right | eyes | in  | a standard |           |       |      |              |     |         |         |
format. The instances where the sizes contained negative Tracker to record the eye stream of the full session. We
|             |          |     |        |        |       |             |     | reused the | aforementioned |     | manual | annotation |     | to get the |
| ----------- | -------- | --- | ------ | ------ | ----- | ----------- | --- | ---------- | -------------- | --- | ------ | ---------- | --- | ---------- |
| values were | removed. |     | In the | second | step, | we filtered | the |            |                |     |        |            |     |            |
raw data by removing three types of the most frequently task segment by finding the correct frames in the front-
|           |         |       |      |          |     |          |       | view stream | and | calculating | the | corresponding |     | frame IDs |
| --------- | ------- | ----- | ---- | -------- | --- | -------- | ----- | ----------- | --- | ----------- | --- | ------------- | --- | --------- |
| occurring | invalid | pupil | size | samples: | (1) | dilation | speed |             |     |             |     |               |     |           |
outliersandedgeartifacts,(2)trend-linedeviationoutliers, for the eye stream. To detect the total number of blinks,
weappliedthefollowingmechanism:Firstly,weconverted
and(3)temporallyisolatedsamples.DilationSpeedoutliers
refer to data that consists of large pupil sizes relative to each frame into grey-scale and applied a Gaussian blur to
it.Secondly,weappliedabinarythresholdtotheframeand
theiradjacentsamples.Weusedmedianabsolutedeviation
(MAD), a commonly used technique [32] as represented used the blurred frame to find contours in it. The convex
|            |      |           |          |     |       |        |      | hull was | calculated | for | all contours. | Lastly, | we  | computed |
| ---------- | ---- | --------- | -------- | --- | ----- | ------ | ---- | -------- | ---------- | --- | ------------- | ------- | --- | -------- |
| in (1) and | (2), | to detect | outliers | and | later | remove | them |          |            |     |               |         |     |          |
from our sample. Once removed, we identified trend-line the ratio between the squared circumference and the area
|           |           |        |     |        |      |        |           | of the convex | hull | to  | remove | all non-spherical |     | hulls. We |
| --------- | --------- | ------ | --- | ------ | ---- | ------ | --------- | ------------- | ---- | --- | ------ | ----------------- | --- | --------- |
| deviation | outliers, | mostly | due | to the | gaps | in the | data that |               |      |     |        |                   |     |           |
may have been caused by blinks. We later removed these used a threshold of 150 to 1200 as a limit for the area and
valuesfrom10to17fortheratiotoexcludenon-pupilhulls.
| gaps using | the | same MAD | technique. |     | Finally, | we  | removed |     |     |     |     |     |     |     |
| ---------- | --- | -------- | ---------- | --- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
≈
the temporally isolated samples containing noise due to a Mathematically,theratiovalueshouldbe4π 12.57,but
duetonoiseinthedata,wehadtowidentheratiorange.The
momentaryeyetrackerglitch.Weusedasparsityfilterthat
splitsanypupilsizesignalthathasagapgreaterthan40ms codefordetectingblinkscanbefoundviaalinkattheend
|     |     |     |     |     |     |     |     | of this section. |     | We also | normalized | the | data by | computing |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------- | ---------- | --- | ------- | --------- |
andthenrejectsanyresultingsectionthatislessthan50ms.
Wealsoremovedpupilsizevaluesthatwerenotinsidethe the number of blinks per minute for each phase. We did
|           |        |           |              |          |            |            |          | this because | the   | duration | for       | each phase | varied      | between |
| --------- | ------ | --------- | ------------ | -------- | ---------- | ---------- | -------- | ------------ | ----- | -------- | --------- | ---------- | ----------- | ------- |
| range of  | 1.5 to | 9 mm.     | In the       | third    | step, once | our        | raw data |              |       |          |           |            |             |         |
| samples   | were   | filtered, | we performed |          | data       | sectioning | and      | individuals. |       |          |           |            |             |         |
| conducted | our    | analysis. | The          | code     | for the    | filtering  | can be   |              |       |          |           |            |             |         |
|           |        |           |              |          |            |            |          | Measuring    | heart | rate     | and heart | rate       | variability | For the |
| found on  | Github | using     | a link       | provided | at         | the end    | of this  |              |       |          |           |            |             |         |
computationofHRV,wecollecteddatafromtheCorSense
section.
|               |     |     |        |     |     |     |     | device. HRV | refers     | to          | the millisecond |       | changes     | in duration |
| ------------- | --- | --- | ------ | --- | --- | --- | --- | ----------- | ---------- | ----------- | --------------- | ----- | ----------- | ----------- |
| MAD=median(|X |     |     | −X ˜|) |     |     |     | (1) |             |            |             |                 |       |             |             |
|               |     | i   |        |     |     |     |     | between     | successive | heartbeats. |                 | These | are termed, | the R-R     |
intervals.Weusedtheinterquartilerangemethod,afunction
˜ =median(X)
| X   |     |     |     |     |     |     | (2) |              |           |     |          |            |     |            |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | --- | -------- | ---------- | --- | ---------- |
|     |     |     |     |     |     |     |     | that removes | outliers, |     | to clean | and filter | the | data [55]. |
To apply the process described above, we recorded the Afterwards,weappliedaRootMeanSquareofSuccessive
whole session, including the basic calibration with the Differences (RMSSD) calculation to the R-R intervals.
Eye Tracker followed by an additional step that presents Finally,anaturallog(ln)isappliedtotheRMSSD[24].To
computeHR,wedivide60∗1000bythemeanoftheR-R
| a changing   | full-screen |                  | display | of          | white, | black | and grey |               |     |     |     |     |     |     |
| ------------ | ----------- | ---------------- | ------- | ----------- | ------ | ----- | -------- | ------------- | --- | --- | --- | --- | --- | --- |
| to establish | a           | first estimation |         | for minimum |        | and   | maximum  | intervals[1]. |     |     |     |     |     |     |
values of PDs for both left and right eyes. We tracked To make sure that the data is collected synchronously,
PD during this calibration, during the explanation of the we compared time stamps and used them to compute the
task, and during the task itself. Afterwards, we manually values of PD, BR, HR, and HRV while the participant is
annotated the start and end of the task by finding the performing a specific task. Once the data was cleaned and
corresponding frames from the front-view camera stream. corrected, we created three levels in our dataset based on
Segmentationofthepupildatawasdonebyconvertingthe the previously indicated three phases in our stimuli. These
frame IDs to time stamps. We used these to determine the levelswereindicativeofthelow,mediumandhighCL.
start and the end of the task segment in the PD readings In the machine learning module, we applied a feature
as provided by the glasses. To account for different pupil elimination method. In this step, we conducted statistical
sizes, we extracted the raw data for both eyes. We applied tests to select those features that have the strongest

Pers Ubiquit Comput (2023) 27:2027–2041 2033
relationship with the classifications (Low, Medium and Table2 Participantdemographics
High). This suggested that the features that were not
Participants 41
statistically significant to our classification could be
Gender 20female/21male
droppedfromthefeatureset.Toachievethis,wemanually
Age 18–37(mean:23.3,
conducted a one-way analysis of variance (ANOVA) with
twounreported)
the feature set (MPDC, BR, HR, HRV) as the list of
SD:4.53
dependent variables and the classification of CL as the
Nativeenglishspeakers Yes:23,No:18
independent variable. We then performed feature selection
Readingdifficulties Yes:2,No:39
usingSelectKBestandremovedallbutthekbestperforming
Wearglasses Yes:15,No:26
features. We used the chi-squared test to choose the
top performing features. In essence, this identifies the
features that have the strongest relationship with the
output variable. Once our feature set was finalized, we in an English speaking country, hence, they were highly
usedthefollowingclassificationalgorithms(orclassifiers): proficient in English language. As our participants were
AdaBoost (AB), Decision Tree (DT), Naive Bayes (NB), required to wear eye tracking glasses, we asked if they
Logistical Regression (LR), Random Forest (RF), Support usually wear glasses. We were not able to capture eye
Vector Machine (SVM) and k-Nearest Neighbour (kNN). tracking data for one of the participants, therefore, we are
The goal of the classification algorithm was to predict the reportinganalysisof40participants.
traitclass,i.e.topredictthelow,mediumandhighlevelsof Thestudywasconductedinthefollowingsteps:
CL. To apply the classifiers, we first used Stratified KFold
1. Participantreadsaninformationsheetandcompletesa
tocreatefivedifferentsplitsinourdataset.Later,weapplied
consentform.
all of the classifiers, one after the other, to compute their
2. Participant completes (a) a questionnaire to report
accuracy in predicting the level of CL. Lastly, we used a
informationonage,numberoflanguages,andwhether
classificationreporttogenerateF1-scores.
theyhavereadingdifficultiesand(b)aphysicalactivity
questionnaire [12] to control for any bias in HR and
3.3Datacollectionandevaluationsetting
HRVmeasurements.
3. Participant puts the CorSense Heart-Rate device on
3.3.1Researchaims
theirfinger(ringfingeroflefthand)andwearstheEye
Tracker.
Our research attempted to answer the following questions
4. Participantperformsthetaskconsistingofthreephases.
(Q):
(a) Intheone-minutefirstphase,participantviewsthe
black,greyandwhitecolorchangingscreen.
– Q1-Didourexperiment’smaintaskinduceCL
(b) In the two-minute second phase, participant spots
asevidencedbyparticipants’subjectiveratings
the correct and incorrect trial words such as
andtaskperformance?
“which”,“lagrat”,“should”,“aryst”andothers.
– Q2 - Did we observe differences for the
(c) Inthefive-minutethirdphase,participantperforms
three task phases for physiological behaviours
the main task of playing the spot the correct or
(MPDC for left and right eyes, BR, HR, &
incorrect(made-up)wordsandsentencesgametask
HRV)?
(seeTable1forthetaskexamplesanddescription).
– Q3 - Which classification method should be
usedtodetectCL? 5. ThephysiologicaldatawasrecordedusingEyeTracker
– Q4-Whichfeaturesarepredictiveofeachlevel (BR, PD), Heart Rate Monitor (HR, HRV), and
(low,mediumandhigh). Webcamfacingtheparticipantthroughoutthecomplete
task.
6. ParticipantcompletestheNASATLXQuestionnaireto
record their subjective ratings of CL. It is important
3.3.2Participantsandprocedure
to note that the participants were asked to give their
subjective rating specifically and only about the third
Weconductedourstudywith41participants(demographics
phase(4(c)above).
as shown in Table 2). We asked participants about any
readingdifficultiesandiftheywerenativeEnglishlanguage Participants were entered in a prize draw for shopping
speakers as the task was based on reading. It is important vouchersasarewardforparticipation.Ethicalapprovalwas
to note that all the participants were attending university obtainedfromourinstitution.

| 2034 |     |     |     |     |     |     |          |          |             | Pers Ubiquit Comput (2023) 27:2027–2041 |               |         |                  |      |
| ---- | --- | --- | --- | --- | --- | --- | -------- | -------- | ----------- | --------------------------------------- | ------------- | ------- | ---------------- | ---- |
|      |     |     |     |     |     |     | question | if it is | not         | taken                                   | into account. |         | This IPAQ        | data |
|      |     |     |     |     |     |     | provided | us with  | reassurance |                                         | that          | none of | the participants |      |
wereinvolvedinhighlyphysicalactivityortrainingbefore
performingthetask.
|     |     |     |     |     |     |     | To analyse | the         | data    | collected | from      | the      | Eye Tracker, | we         |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | ------- | --------- | --------- | -------- | ------------ | ---------- |
|     |     |     |     |     |     |     | created    | application | program |           | interface | software |              | that eases |
theaccesstothedataandallowsrunningthesameanalysis
overallparticipants.
|     |     |     |     |     |     |     | The                       | software | can    | be found | on   | GitHub      | at https:// |      |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | -------- | ------ | -------- | ---- | ----------- | ----------- | ---- |
|     |     |     |     |     |     |     | github.com/BrutusTT/tobii |          |        |          | api. | The scripts | for         | the  |
|     |     |     |     |     |     |     | generation                |          | of the | stimuli  | and  | analysis    | of the      | data |
Fig.2 Setup—aparticipantreadytoperformthetask
|     |     |     |     |     |     |     | in this     | paper | can                  | be found | at  | https://github.com/ |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | -------------------- | -------- | --- | ------------------- | --- | --- |
|     |     |     |     |     |     |     | BrutusTT/ml |       | study/tree/master/ml |          |     | study/stimuli.      |     |     |
3.3.3Setupandmaterials
|           |        |         |             |     |               |     | Additionally, |         | the                  | dataset | with | three levels           | of  | CL  |
| --------- | ------ | ------- | ----------- | --- | ------------- | --- | ------------- | ------- | -------------------- | ------- | ---- | ---------------------- | --- | --- |
|           |        |         |             |     |               |     | can           | also be | foundonGitHub        |         |      | at https://github.com/ |     |     |
| The setup | (shown | in Fig. | 2) involved |     | a participant |     |               |         |                      |         |      |                        |     |     |
|           |        |         |             |     |               |     | BrutusTT/ml   |         | study/tree/master/ml |         |      | study/modal.           |     |     |
performingthewordgametaskonacomputerscreenwhile
|         |                    |         |       |      |          |     | More | details | can | be found | in the | included | Readme |     |
| ------- | ------------------ | ------- | ----- | ---- | -------- | --- | ---- | ------- | --- | -------- | ------ | -------- | ------ | --- |
| wearing | Tobii eye tracking | glasses | along | with | CorSense |     |      |         |     |          |        |          |        |     |
files.
Heart-Ratedevice.
PsychoPy,1
| We used    |                  | an open-source |         | application, |           | to  |                          |     |     |     |     |     |     |     |
| ---------- | ---------------- | -------------- | ------- | ------------ | --------- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- |
| programme  | our experiment.  | To             | collect | data on      | changes   | in  |                          |     |     |     |     |     |     |     |
|            |                  |                |         |              | pro2      |     | 3.4Summaryofmeasurements |     |     |     |     |     |     |     |
| eye and    | heart behaviour, | we used        | Eye     | Tracker      |           | and |                          |     |     |     |     |     |     |     |
| a CorSense | HRV device3      | respectively.  |         | We           | also used | an  |                          |     |     |     |     |     |     |     |
external webcam to collect additional data on the BR as Insummary,wecollectedthefollowingmeasuresduringthe
shown in Fig. 3. However, in the end, we did not use the experiment. Physiological measures: These were BR, PD,
HR,andHRV.Theseareusedintheframework.Validation
| recorded | videos to calculate | BR  | due | to low | quality | of the |     |     |     |     |     |     |     |     |
| -------- | ------------------- | --- | --- | ------ | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
recorded data and unsatisfactory rate of robustly detecting measures: These were Physical Activity index (IPAQ pre-
|                  |               |            |     |     |          |     | task), task | performance |     | score, | and | subjective |     | task load |
| ---------------- | ------------- | ---------- | --- | --- | -------- | --- | ----------- | ----------- | --- | ------ | --- | ---------- | --- | --------- |
| blinks. Instead, | as previously | described, |     | we  | used the | Eye |             |             |     |        |     |            |     |           |
Tracker’s eye stream for both BR and PD analysis. During (NASATLXpost-task).Thesewereusedascontrolsandfor
validatingthatthetaskinducedCL.
thetask,wealsocollecteddataonthetaskperformanceof
theparticipants(ascorebasedonthenumberofcorrectlyor
incorrectlycategorizedwordsandsentences)toinvestigate
| the relationship | between | their | task performance |     | and | their | 4Results |     |     |     |     |     |     |     |
| ---------------- | ------- | ----- | ---------------- | --- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
subjectiveratingofCL.
The NASA Task Load Index questionnaire4 [19] was 4.1DidthemaintaskinduceCL?
| used to | collect subjective | ratings | of  | the amount |     | of CL |     |     |     |     |     |     |     |     |
| ------- | ------------------ | ------- | --- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
generated by the task [42]. In addition, we used the To answer Q1 we made use of the performance scores,
International Physical Activity Questionnaire (IPAQ)5 [9] which were collected from the third phase of the task, and
to get relevant data on health-related physical activity. We the NASA TLX ratings which we asked participants to
collectedthisdataonphysicalactivitybecausetheliterature provide specifically about their subjective task load during
suggeststhatparticipants’physicalactivityindexcancreate thatsamethirdphase.Thus,wehaveasetofSubjectiveCL
an experimental bias [17], bringing heart rate results into ratingsandanassociatedsetofPerformancescores.Based
|     |     |     |     |     |     |     | on the         | empirical | evidence       |     | in literature, | as     | CL              | increases, |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | -------------- | --- | -------------- | ------ | --------------- | ---------- |
|     |     |     |     |     |     |     | we would       | expect    | performance    |     | to             | reduce | (see Subsection |            |
|     |     |     |     |     |     |     | 2.2 in Section |           | 2). Therefore, |     | we would       | expect | there           | to be      |
1PsychoPy-https://www.psychopy.org
|            |                  |                                         |     |     |     |     | a negative | correlation |     | between | third | phase | Performance, |     |
| ---------- | ---------------- | --------------------------------------- | --- | --- | --- | --- | ---------- | ----------- | --- | ------- | ----- | ----- | ------------ | --- |
| 2Tobii eye | tracking glasses | pro - https://www.tobiipro.com/product- |     |     |     |     |            |             |     |         |       |       |              |     |
whichshouldvarywithCL,andthirdphaseSubjectiveCL,
listing/tobii-pro-glasses-2/
fromtheTLXratings.
3CorSenseEliteHRVDevice-https://elitehrv.com/corsense
|     |     |     |     |     |     |     | We ran | a Pearson |     | correlation |     | between | Subjective | CL  |
| --- | --- | --- | --- | --- | --- | --- | ------ | --------- | --- | ----------- | --- | ------- | ---------- | --- |
4NASATaskLoadIndexQuestionnaire-https://ntrs.nasa.gov/archive/
|     |     |     |     |     |     |     | and Performance. |     | We  | found | that | there | was a | negative |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | ----- | ---- | ----- | ----- | -------- |
nasa/casi.ntrs.nasa.gov/20000021488.pdf
5InternationalPhysicalActivityQuestionnaire-https://www.sdp.univ. correlation between Subjective CL and Performance,
|                                 |     |         |            |          |     |     | r(41) = | −.456, | p < | .00. This | is between |     | a medium | and a |
| ------------------------------- | --- | ------- | ---------- | -------- | --- | --- | ------- | ------ | --- | --------- | ---------- | --- | -------- | ----- |
| fvg.it/sites/default/files/IPAQ |     | English | self-admin | long.pdf |     |     |         |        |     |           |            |     |          |       |

| Pers Ubiquit Comput (2023) 27:2027–2041 |     |     |     |     |     |     |     |     |     |     |     |     |     | 2035 |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
Fig.3 TobiiEyeTrackingGlasses(left),Webcam(middle),andCorSenseHeart-rateMonitor(right)
largeeffect,butclosertoalargeeffect[11].6TheMandSD low level. HR did not show differences for all the levels
values for NASA TLX and performance are M: 50.96 and from the three stimulus phases. However, HRV slightly
SD: 16.96 and M: 111.62 and SD: 5.77, respectively. This declined across all the levels (this is discussed further
correlation result motivated us to conduct a simple linear in Section 4.5). It is also notable that the range for BR
regressionofSubjectiveCLwithPerformance.Asignificant (between0and52)inourdataisinlinewithpreviouswork
=
regression model was found (F 1,39 10.162, p < .00), whichsuggeststhatthemeanBRisgenerallybetween2and
| with an | R2 = .207, | adjusted |     | R2 = .186, | β = | −.456. Thus, | 50[38]. |     |     |     |     |     |     |     |
| ------- | ---------- | -------- | --- | ---------- | --- | ------------ | ------- | --- | --- | --- | --- | --- | --- | --- |
forourtaskahigherparticipants’SubjectiveCLratingdoes
predict lower Performance. We understand that it has also 4.3Didweobservechangesinphysiological
behavioursacrossthethreelevels?
| been shown | in  | numerous | studies | that | a high | CL adversely |     |     |     |     |     |     |     |     |
| ---------- | --- | -------- | ------- | ---- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
impactsuser’staskperformance[4,14,39].
ToanswerQ2,weconductedaone-way,between-subjects,
|     |     |     |     |     |     |     | ANOVA |     | to compare | the | effect | of the | three phases | on all |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | ---------- | --- | ------ | ------ | ------------ | ------ |
Hence,weconcludethatthisnegativecorrelation
thephysiologicalbehaviours(MPDCforleftandrighteye,
| between | Subjective |     | CL  | and Performance |     | in our |     |     |          |         |        |     |          |             |
| ------- | ---------- | --- | --- | --------------- | --- | ------ | --- | --- | -------- | ------- | ------ | --- | -------- | ----------- |
|         |            |     |     |                 |     |        | BR, | HR, | and HRV) | in low, | medium |     | and high | conditions. |
experiment,demonstratesandvalidatesthatour
|            |      |         |        |     |      |            | There   | was   | a significant |        | effect | of the | phases on  | MPDC for   |
| ---------- | ---- | ------- | ------ | --- | ---- | ---------- | ------- | ----- | ------------- | ------ | ------ | ------ | ---------- | ---------- |
| task       | does | in fact | induce | CL. | This | positively |         |       |               |        |        |        |            |            |
|            |      |         |        |     |      |            | left    | (F    | = 139.75,     | p      | < .00) | and    | right eyes | (F =       |
| answersQ1. |      |         |        |     |      |            |         | 2,119 |               |        |        |        |            | 2,119      |
|            |      |         |        |     |      |            | 149.50, |       | p < .00),     | and BR | (F     | =      | 3.475, p   | < .04). We |
2,119
|     |     |     |     |     |     |     | did | not observe | a   | significant | effect | of  | HR (F | = .09, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | ------ | --- | ----- | ------ |
2,119
|     |     |     |     |     |     |     | p   | <.91)andHRV(F |     |     | =1.364,p |     | <.26). |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | -------- | --- | ------ | --- |
2,119
4.2Descriptivestatisticsforthefeaturestoclassify We also conducted a post hoc test to observe the
| CL  |     |     |     |     |     |     | significant |     | difference | among | the | three | phases. | We found |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---------- | ----- | --- | ----- | ------- | -------- |
thattheMPDCforbothleftandrighteyeswerestatistically
We present descriptive statistics based on the three phases significant (p < .00) for all three levels of CL. This
ofourstimuliforallthe40participantsinTable3.Thetable suggests that MPDC for both left and right eyes increased
showsoverallminimumandmaximumvalues(range)along significantly from low to medium, and from medium to
withmean(M)andstandarddeviation(SD)inthecomplete high levels of CL as indicated in Table 3. On the other
dataset based on all the phases of the stimulus. From the hand,BRwasmarginallysignificant(p <.07)betweenlow
data gathered in the three individual stimulus phases, we andmedium,andbetweenlowandhighlevelsofCL.This
were able to define the three classifications (low, medium suggests that as the CL increased, there was a decrease in
and high). This was based on the significant difference, therateofblinking.Theparticipantsblinkedtheleastwhile
| presented | in the | next | subsection |     | for the | physiological | underhighCL. |     |     |     |     |     |     |     |
| --------- | ------ | ---- | ---------- | --- | ------- | ------------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
behavioursobserved in thethree phases. We also show the Theaboveanalysisshowsthatourresultshereareinline
ranges for all the features, for these three classes, along with the findings reported in prior literature. That is, there
with their M and SD in the data. It can be seen that isanincreaseinPDwithanincreaseinthelevelofCL[46,
MPDCforbothleftandrighteyeincreaseaccordingtoeach 47]andBRdeclineswithanincreaseinthelevelofCL[23].
classification. On the contrary, BR declines from high to We conjecture that, although we did not find a significant
|     |     |     |     |     |     |     | difference |     | for HR | and HRV, | nonetheless, |     | HRV | marginally |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------ | -------- | ------------ | --- | --- | ---------- |
declinedasCLincreased[40]andHRmarginallyincreased
6Field[11]suggests0.3isamediumeffectwhile0.5isalargeeffect. asCLincreased[10].

2036 Pers Ubiquit Comput (2023) 27:2027–2041
| ehtdna,)muideM(esahplairteht,)woL(esahptsereht(sesahpsulumitseerhtehtotgnidnopserrocsnoitacifissalceerhtehtfosegnarehtdnaserusaemllarevorofscitsitatsevitpircseD |     | 91.31:DS,87.08:M,]76.911,61.25[ |            |     |        |          |             |     |         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | ------------------------------- | ---------- | --- | ------ | -------- | ----------- | --- | ------- |
|                                                                                                                                                                  |     |                                 | Revisiting |     | Q2, we | observed | significant |     | differ- |
71.0:DS,82.1:M,]27.1,79.0[ 61.0:DS,92.1:M,]76.1,40.1[ 51.11:DS,58.21:M,]0.35,0.0[ 54.0:DS,36.3:M,]47.4,37.2[ encesforthethreephasesforMPDCforleftand
|     |     |     | right | eyes. | We observed |     | marginally | significant |     |
| --- | --- | --- | ----- | ----- | ----------- | --- | ---------- | ----------- | --- |
differencesforlowtomediumandlowtohighfor
)DS,M,egnar(hgiH
BRforleftandrighteyes.
4.4Classifierperformance
|     |     |     | Addressing     | Q3, | to investigate |     | the most        | suitable | classifi-      |
| --- | --- | --- | -------------- | --- | -------------- | --- | --------------- | -------- | -------------- |
|     |     |     | cation method, |     | we used        | the | seven different |          | classifiers to |
13.31:DS,35.97:M,]83.521,48.25[
comparetheirperformancetopredictthelow,mediumand
highlevelsofCLinourdataset.WeusedStratifiedKFold,
70.0:DS,79.0:M,]91.1,97.0[ 70.0:DS,69.0:M,]21.1,96.0[ 38.8:DS,18.21:M,]0.93,5.1[
|     |     | 54.0:DS,77.3:M,]5.4,34.2[ | createdfivedifferentsplitsand,finally,computedthemean |     |     |     |     |     |     |
| --- | --- | ------------------------- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
accuracyofallsevenclassifiers.TheseareshowninTable4.
)DS,M,egnar(muideM
Ingeneral,weobtainedahighpredictiveaccuracyformost
oftheclassifiers.However,RFoutperformedtheotherswith
ameanaccuracyof91.66%followedbyNB,DT,andSVM.
WealsofoundthatLRandABperformedmoderately,with
ameanaccuracyof77.5%and69.16%respectively.Onthe
contrary,weobtainedsubstantiallylowerperformancefrom
|     |     |     | the KNN            | with a | mean   | accuracy | of 45.83%. | Table       | 5 shows  |
| --- | --- | --- | ------------------ | ------ | ------ | -------- | ---------- | ----------- | -------- |
|     |     |     | the classification |        | report | for the  | seven      | classifiers | and also |
34.31:DS,68.97:M,]18.521,84.35[
illustratestheF1-scoresforeachclass(low,medium,high)
28.31:DS,36.81:M,]0.24,0.0[ of CL. It can be seen that the RF classifier resulted in the
|     | 61.0:DS,57.0:M,]80.1,93.0[ 62.0:DS,57.0:M,]31.1,24.0[ | 44.0:DS,87.3:M,]84.4,46.2[ |          |              |          |          |          |            |             |
| --- | ----------------------------------------------------- | -------------------------- | -------- | ------------ | -------- | -------- | -------- | ---------- | ----------- |
|     |                                                       |                            | highest  | F1-score     | for each | class    | followed | by         | NB. We also |
|     |                                                       |                            | observed | a relatively | lower    | F1-score | for      | the medium | class       |
)DS,M,egnar(woL ofCLcomparedwiththeothertwoclasses.Nonetheless,in
general,ahighF1-scorewasachieved.
LCfosleveL The results show that RF and NB performed well, with
thefeatureselectionbasedonSelectKBest.Thisselectsthe
|     |     |     | features | that have | a strong | relationship |     | with | the CL level. |
| --- | --- | --- | -------- | --------- | -------- | ------------ | --- | ---- | ------------- |
ThebasicideabehindRFisthatitoperatesasanensemble.
|     |     |     | The algorithm |     | creates | trees        | (models) | that output | a class    |
| --- | --- | --- | ------------- | --- | ------- | ------------ | -------- | ----------- | ---------- |
|     |     |     | prediction.   | The | model   | is predicted | based    | on the      | class with |
06.11 60.31
|     | 62.0 72.0 | 64.0 |                                                    |         |     |        |               |     |               |
| --- | --------- | ---- | -------------------------------------------------- | ------- | --- | ------ | ------------- | --- | ------------- |
| DS  |           |      | themostvotes.Thekeytobetterperformanceliesinthelow |         |     |        |               |     |               |
|     |           |      | correlation                                        | between | the | trees. | We understand |     | that the high |
predictiveaccuracyofDTreflectedontheRFperformance,
)M(naeM
|     |     |     | as the trees | created | by  | the RF, | as an ensemble, |     | may have |
| --- | --- | --- | ------------ | ------- | --- | ------- | --------------- | --- | -------- |
67.41 70.08 enhanced the predictive performance of the classifier. On
|     | 10.1 10.1 | 47.3 |           |       |            |          |             |     |               |
| --- | --------- | ---- | --------- | ----- | ---------- | -------- | ----------- | --- | ------------- |
|     |           |      | the other | hand, | one reason | for      | relatively  | low | accuracy of   |
|     |           |      | AB could  | have  | been the   | presence | of outliers |     | in one of the |
]28.521,61.25[ features,asitcanbeseenthatforBR,wehadawiderange
|     | ]17.1,93.0[ ]76.1,24.0[ | ]47.4,44.2[ | ofdatainourdataset. |     |     |     |     |     |     |
| --- | ----------------------- | ----------- | ------------------- | --- | --- | --- | --- | --- | --- |
]0.35,0.0[
egnaR
Table4 Themeanaccuracy(%)forthesevenclassifierstopredictCL
| ))hgiH(esahpksat |     |     | Classifier | AB  | NB  | DT  | SVM | LR  | RF KNN |
| ---------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | ------ |
eyethgirCDPM
eyetfelCDPM
|     |     |     | Accuracy | 69.16 | 85.83 | 85.00 | 82.50 | 77.50 | 91.66 45.83 |
| --- | --- | --- | -------- | ----- | ----- | ----- | ----- | ----- | ----------- |
serutaeF
3elbaT
Boldvaluessignifytheclassifierthatachievedhighaccuracy
VRH
|     | RB  | RH  | indetectingCognitiveload |     |     |     |     |     |     |
| --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |

| Pers Ubiquit Comput (2023) 27:2027–2041 |     |     |     |     |     |     |     |     |     |     |     |     |     | 2037 |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
Table5 F1-scoresforthesevenclassifiertopredictlow,mediumand computed the F1-score for each level of CL. The rationale
highlevelsofCL was to investigatethe effectiveness of allthe features indi-
viduallytowardsaccuratelyclassifyingacertainlevelofCL
| CognitiveLoad |     |     | Classifier |     |     | F1-score |     |     |     |     |     |     |     |     |
| ------------- | --- | --- | ---------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
inourdataset.Below,weonlyreportthefeatureimportance
Low AB 0.62 perlevelofCLfortheRFclassifier,becauseitwasthebest
|     |     |     | NB  |     |     | 0.87 | performingclassifiertopredictthelevelsofCL. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
DT 0.84 Figure 4 illustrates the feature importance for the RF
SVM 0.83 classifiers based on the F1-scores of each level of CL. In
LR 0.80 general, it highlights that MPDC for left and right eyes,
|     |     |     | RF  |     |     | 0.91 | werethebestperformingfeaturesforalllevelsofCLforthe |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
KNN 0.48 RF classifier. In the case of RF, we observed that, for the
lowCLclass,BRwasrelativelyimportantasitgenerateda
| Medium |     |     | AB  |     |     | 0.71 |     |     |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
NB 0.81 relatively good F1-score. Lastly, HRV and HR were found
|     |     |     |     |     |     |      | to be the               | least | important | features |     | for the | RF classifier | to  |
| --- | --- | --- | --- | --- | --- | ---- | ----------------------- | ----- | --------- | -------- | --- | ------- | ------------- | --- |
|     |     |     | DT  |     |     | 0.80 |                         |       |           |          |     |         |               |     |
|     |     |     | SVM |     |     | 0.77 | predictthelowclassofCL. |       |           |          |     |         |               |     |
LookingatthepredictionsofthemediumlevelofCL,we
|     |     |     | LR  |     |     | 0.64 |                                                    |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | RF  |     |     | 0.85 | observethatBRwasdeemedafairlysignificantfeaturefor |     |     |     |     |     |     |     |
theRFclassifier.WealsorecognizethatHRandHRVwere
|     |     |     | KNN |     |     | 0.51 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
High AB 0.75 comparativelylessimportantfeaturestopredictmediumCL
|     |     |     |     |     |     |      | than to predict |     | low CL. | Overall, | they | both | were | found to |
| --- | --- | --- | --- | --- | --- | ---- | --------------- | --- | ------- | -------- | ---- | ---- | ---- | -------- |
|     |     |     | NB  |     |     | 0.90 |                 |     |         |          |      |      |      |          |
DT 0.84 be less critical as compared with other features (MPDC,
|     |     |     |     |     |     |      | BR). Lastly, | to  | predict | high | CL, | BR was | found | to be |
| --- | --- | --- | --- | --- | --- | ---- | ------------ | --- | ------- | ---- | --- | ------ | ----- | ----- |
|     |     |     | SVM |     |     | 0.88 |              |     |         |      |     |        |       |       |
LR 0.85 less important. In general, however, HR and HRV features
|     |     |     |     |     |     |      | were relatively |     | more | influential | in  | low and | medium | levels |
| --- | --- | --- | --- | --- | --- | ---- | --------------- | --- | ---- | ----------- | --- | ------- | ------ | ------ |
|     |     |     | RF  |     |     | 0.95 |                 |     |      |             |     |         |        |        |
ofCL.
|     |     |     | KNN |     |     | 0.37 |               |     |      |         |     |        |        |        |
| --- | --- | --- | --- | --- | --- | ---- | ------------- | --- | ---- | ------- | --- | ------ | ------ | ------ |
|     |     |     |     |     |     |      | We understand |     | that | perhaps | due | to the | nature | of our |
BoldRFistheclassifierthatachievesthehighestaccuracy task,HRandHRVwerenotamongthecriticallyimportant
|     |     |     |     |     |     |     | features | in our | dataset. | The | time | pressures |     | from the |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | -------- | --- | ---- | --------- | --- | -------- |
It is recognized that NB performs best if the input presentation of tasks or stimuli or the display of data at a
|          |     |             |         |        |      |          | faster rate | may | have | induced | differences |     | in the | heart data |
| -------- | --- | ----------- | ------- | ------ | ---- | -------- | ----------- | --- | ---- | ------- | ----------- | --- | ------ | ---------- |
| features | are | independent | of each | other, | i.e. | are less |             |     |      |         |             |     |        |            |
correlated with each other. It is also known that NB [22]. We compared the F1-scores of individual features,
|     |     |     |     |     |     |     | with the | case where | the | F1-scores | were | computed |     | through |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | --------- | ---- | -------- | --- | ------- |
performsrelativelybetterthanLRandsimilarmodelswhen
that is true. Consequently, we speculate that these are the using all the features, as shown in Table 5. We observe
thattheF1-scores(91%,85%,and95%)topredictthelow,
| reasons | for the | better | performance | of  | NB here. | On the |        |          |        |     |          |     |              |      |
| ------- | ------- | ------ | ----------- | --- | -------- | ------ | ------ | -------- | ------ | --- | -------- | --- | ------------ | ---- |
|         |         |        |             |     |          |        | medium | and high | levels | of  | CL using | all | the features | were |
otherhand,KNNdemonstratedthelowestperformance.We
higherthantheF1-scoreoftheindividualfeaturesforeach
understandthatKNNisaclustering-basedmethod,andthe
|     |     |     |     |     |     |     | of the low, | medium | and | high | levels | of CL | (as | shown in |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | --- | ---- | ------ | ----- | --- | -------- |
resultssuggestthatthedatasetdidnotfindproperclusters.
Fig.4).ItisalsoimportanttonotethatforhighCL,theF1-
| In other | words, | the data | was relatively | hard | to  | separate in |              |       |      |      |     |           |      |         |
| -------- | ------ | -------- | -------------- | ---- | --- | ----------- | ------------ | ----- | ---- | ---- | --- | --------- | ---- | ------- |
|          |        |          |                |      |     |             | score, after | using | only | MPDC | for | the right | eye, | was 94% |
thecaseoftheKNNclassifier.
and87%respectively.Thisshowsthatforthehighlevelof
| In general, |     | these classifier |     | results | suggest | that our |     |     |     |     |     |     |     |     |
| ----------- | --- | ---------------- | --- | ------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
CL,MPDCwasthemostimportantfeatureinourdataset.In
approachyieldedpromisingfindings.
otherwords,itshowsthatotherfeatureswerenotimportant
|     |     |     |     |     |     |     | for the high | level | of  | CL; however, |     | we want | to  | emphasise |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | --- | ------------ | --- | ------- | --- | --------- |
ToanswerQ3,weconcludeRandomForestasthe
thatallfeaturesindifferentwaysplayedaroletoachievea
mostappropriateoftheclassifierstoclassifythe highF1-scoreforalowandmediumlevelofCL.Nonethe
threelevelsofCL.
less,thisallshowsthepotentialoftheideaofusingvarious
|     |     |     |     |     |     |     | physiological |        | behaviours | as            | features | in    | our framework |           |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------ | ---------- | ------------- | -------- | ----- | ------------- | --------- |
|     |     |     |     |     |     |     | because       | it can | make       | the detection |          | of CL | less          | dependent |
4.5FeatureimportanceperlevelofCL
|     |     |     |     |     |     |     | on the       | task. | Also,      | it highlights |           | the need | to     | conduct |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | ---------- | ------------- | --------- | -------- | ------ | ------- |
|     |     |     |     |     |     |     | more studies | in    | the future |               | and shows | that     | it can | indeed  |
Toinvestigatewhichfeaturesarepredictiveofeachclassof
|           |          |         |     |         |           |           | improve | the | accuracy | of  | predicting |     | the three | levels |
| --------- | -------- | ------- | --- | ------- | --------- | --------- | ------- | --- | -------- | --- | ---------- | --- | --------- | ------ |
| CL in our | dataset, | we used | one | feature | at a time | and later |         |     |          |     |            |     |           |        |
ofCL.

| 2038 |     |     |     |     |     | Pers Ubiquit Comput (2023) 27:2027–2041 |     |     |
| ---- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- |
Fig.4 Featureimportancefor
theRFclassifierbasedonthe
F1-scoresforeachlevelofCL.
Thex-axisshowsallthe
physiologicalbehaviourswhile
they-axisshowstheaccuracies
achievedbyeachphysiological
behaviourasonefeatureto
predictlow,mediumandhigh
levelsofCL
|     |     |     |     | 71.2% and      | 40.4% respectively | [6]. Other      | recent work  | [14]   |
| --- | --- | --- | --- | -------------- | ------------------ | --------------- | ------------ | ------ |
|     |     |     |     | on classifying | low,               | medium and high | levels of CL | during |
AnsweringQ4,weconcludethatMPDCforboth
|     |     |     |     | a driving | task, achieved | a considerably | high accuracy | of  |
| --- | --- | --- | --- | --------- | -------------- | -------------- | ------------- | --- |
rightandlefteyewerethemostnotablefeatures,
|     |     |     |     | 86.1% on | a dataset | based on pupil | sizes. However, | to the |
| --- | --- | --- | --- | -------- | --------- | -------------- | --------------- | ------ |
andBRwasalsoviewedasmoderatelyimportant
|     |     |     |     | best of | our knowledge, | our CL classification | framework, |     |
| --- | --- | --- | --- | ------- | -------------- | --------------------- | ---------- | --- |
forpredictinglow,mediumandhighCL.
|     |     |     |     | which gathers | data | from various physiological |     | measures |
| --- | --- | --- | --- | ------------- | ---- | -------------------------- | --- | -------- |
synchronously,andachievesanaccuracyofnearly92%,has
|     |     |     |     | notably      | outperformed | previous classification | accuracies. |         |
| --- | --- | --- | --- | ------------ | ------------ | ----------------------- | ----------- | ------- |
|     |     |     |     | Furthermore, | our dataset  | had a larger            | number      | of sub- |
5Discussion jects than the previous works [21]. Beside the notable
|     |     |     |     | performance, | we emphasise | that there | is a need to | conduct |
| --- | --- | --- | --- | ------------ | ------------ | ---------- | ------------ | ------- |
Our work presents a framework to detect three levels of more demonstrations of the framework with a variety of
|                 |               |            |             | tasks, and | under different | settings, to | further establish | the |
| --------------- | ------------- | ---------- | ----------- | ---------- | --------------- | ------------ | ----------------- | --- |
| CL by analysing | physiological | data based | on eyes and |            |                 |              |                   |     |
heart when exposed to a task. Our findings show that the robustnessandvalueoftheframework.Weplantodemon-
RFclassificationalgorithm,incombinationwithunivariate strate the framework in different setups in which drivers
featureselection,considerablyoutperformedotherclassifi- monitorautonomousvehicleoperationsandinwhichsuper-
cation algorithms. Overall, by using the RF classification, visors or operators monitor and observe the autonomous
low and high levels of CL were predicted with F1-scores operationsofrobotsdeployedinoffshoreenvironments[20]
higher than 90% and the medium level of CL was pre- andsmartfactories[57].Weconjecturethattheframework
dicted with F1-score of 85%. Other classifiers such as NB canestimateCLrobustlyandaccuratelyunderdifferentset-
and DT also predicted the three levels of CL with a high tings in principle. Hence, it can potentially be applied in a
F1-score of over 80%. As stated earlier, prior work has number of domains such as the aerospace domain. In the
classified two and four levels of CL and they have used aerospacedomain,itcanhelptocreateasystemthatdynam-
one kind of physiological behaviour based on either eyes, ically adapts the workflow and facilitates the automatic
or skin conductance, or brain. Nonetheless, it is impor- assignment of tasks to supervisors that operate in the con-
tant to compare our results with the past classifications of trol rooms of space stations based on their CL. We believe
CL [7, 14]. For instance, Chen et al. [7] have reported suchasystemcanenhancetheproductivityofthesupervi-
several studies to classify CL using eye- and GSR-based sorsandconsequentlyreduceerrorsthatcould,potentially,
measurements individually. Their classification accuracy, havevastlyexpensiveconsequences[21].Furthermore,such
basedontwoandfourlevelsoftaskdifficulty,onadataset asystemhasawiderimplicationinmaintainingthesupervi-
based on the pupillary response, was able to achieve an sor’smentalhealthandwell-being,asaresultofmanaging
accuracy of 79.3% and 45% respectively [5]. Additionally, theirCL.Insummary,thedescribedframeworkcan,poten-
the accuracy achieved on the dataset based on GSR data tially, be applied in different settings in a non-intrusive
for classifying two and four levels of CL, was equal to manner, while collecting the physiological data from high

| Pers Ubiquit Comput (2023) 27:2027–2041 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 2039 |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
definition cameras to record the heart-based [45] and eye- We demonstrated the framework in the lab under a
baseddata[54]. controlled environment. Therefore, more testing under
|     |     |     |     |     |     |     |     | various           | tasks is | needed       | to further | establish | the | conformity   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | -------- | ------------ | ---------- | --------- | --- | ------------ | --- |
|     |     |     |     |     |     |     |     | of the framework. |          | Furthermore, |            | the pool  | of  | participants |     |
In summary, the framework to detect CL works in had both native and non-native English language speakers.
Althoughtheywerealluniversitystudents,whohadpassed
| principle. |     | We further | show | that | the synchronous |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ---------- | ---- | ---- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
collection of data based on various physiological an English language test and achieved an appropriate
|            |     |          |        |                 |     |          |     | standard | to gain | university |     | admission, | we  | might | get |
| ---------- | --- | -------- | ------ | --------------- | --- | -------- | --- | -------- | ------- | ---------- | --- | ---------- | --- | ----- | --- |
| behaviours |     | , is the | key to | its performance |     | in terms |     |          |         |            |     |            |     |       |     |
ofclassificationaccuracyforlowandhighlevelsof differentresultswithallnative,orallnon-nativeparticipant
|     |     |     |     |     |     |     |     | groups | for this | task. | Nonetheless, | the | paper | investigated |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ----- | ------------ | --- | ----- | ------------ | --- |
CL.
|     |     |     |     |     |     |     |     | the framework |     | to classify | CL  | and we | recognize | that | more |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | --- | ------ | --------- | ---- | ---- |
testingisneededtofurtherestablishitsrobustness.
|     |     |     |     |     |     |     |     | Our | future work | is  | focused | on the | following | aspects. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | ------ | --------- | -------- | --- |
6Conclusion Firstly, we plan to gather data during more diverse tasks.
|     |     |     |     |     |     |     |     | These tasks | could | consist | of  | playing games. |     | Additionally, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ------- | --- | -------------- | --- | ------------- | --- |
In this paper, we present our work on the detection of it could be an interface showing data in different
cognitive load (CL) using physiological responses based visualizations and asking individuals to perform various
oneye-andheart-relateddata.Inparticular,weintroduced tasksonthem.Theideaistomakethedatasetrichenoughto
a framework that consists of the following steps to detect classifyCLrobustlyinvarioussettings.Secondly,weintend
CL. First, we collect physiological measurements with to measure physiological behaviours based on skin and
state-of-the-art, off-the-shelf, sensing technologies, during brain, to further improve the robustness of the framework
a task. Second, we apply supervised machine learning to detect CL. We also intend to use speech-based features
algorithms, along with feature elimination. We applied in the framework. Thirdly, we also intend to address the
our framework during an experimental setting, in which limitationsnotedaboveinourfuturework.Lastly,ourlong-
participants played a game to spot correct and incorrect term goal is to adapt systems based on the measurement
wordsandsentenceswhilewecollectedtheireyeandheart of CL in real time. Therefore, we plan to employ our
measurements. Our work confirms that CL was detected measurement of CL to create adaptive interfaces, which
withhighaccuracy.Thissuggestsitspotentialuseinvarious manages user CL and help improve user performance in
practical applications, particularly for the purpose of the variousenvironments.
| adaptation | of  | interfaces, | to improve |     | user experience, |     | user |     |     |     |     |     |     |     |     |
| ---------- | --- | ----------- | ---------- | --- | ---------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
performance,andtohelpreducehumanerrors. Acknowledgements Theauthorswouldliketothankandacknowledge
Consideringourresearchquestions,weconcludethat(1) the reviewers for their insightful comments that have certainly
improvedthequalityoftheworkdescribedinthispaper.
| our task   | was able | to induce |          | CL in the | participants, |      | (2) we   |     |     |     |     |     |     |     |     |
| ---------- | -------- | --------- | -------- | --------- | ------------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| found that | mean     | pupil     | diameter | change    | for           | both | left and |     |     |     |     |     |     |     |     |
righteyesincreaseswitheachlevelofCL,(3)theblinking Funding This work received financial support from the ORCA
HubEPSRC(EP/R026173/1,2017-2021)andconsortiumpartners.
| rate decreases |     | fromlowtohighlevelsofCL,(4)Random |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Forestwasthemostaccurateclassificationmethod,and(5)
Compliancewithethicalstandards
| mean pupil | diameter    |       | changes  | for left | and       | right eyes | and      |                    |     |            |        |        |                   |     |        |
| ---------- | ----------- | ----- | -------- | -------- | --------- | ---------- | -------- | ------------------ | --- | ---------- | ------ | ------ | ----------------- | --- | ------ |
| blinking   | rate were   | among | the      | most     | important | features   | to       |                    |     |            |        |        |                   |     |        |
|            |             |       |          |          |           |            |          | Conflictofinterest |     | The fourth | author | is one | of the recipients |     | of the |
| classify   | low, medium |       | and high | levels   | of CL.    | Our        | findings |                    |     |            |        |        |                   |     |        |
EPSRCgrant.Thefirstthreeauthorsdeclarethattheyhavenoconflict
achievedbetteraccuracytoclassifyCLincomparisonwith
ofinterest.
previouswork.
|     |     |     |     |     |     |     |     | Open Access | This              | article | is licensed | under | a Creative | Commons       |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------------- | ------- | ----------- | ----- | ---------- | ------------- | --- |
|     |     |     |     |     |     |     |     | Attribution | 4.0 International |         | License,    | which | permits    | use, sharing, |     |
7Limitationsandfuturework adaptation,distributionandreproductioninanymediumorformat,as
|     |     |     |     |     |     |     |     | long as you | give | appropriate | credit | to the original | author(s) |     | and the |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ----------- | ------ | --------------- | --------- | --- | ------- |
source,providealinktotheCreativeCommonslicence,andindicate
| Our work | has | the following |     | limitations. |     | In general, | our |            |            |     |        |          |             |          |     |
| -------- | --- | ------------- | --- | ------------ | --- | ----------- | --- | ---------- | ---------- | --- | ------ | -------- | ----------- | -------- | --- |
|          |     |               |     |              |     |             |     | if changes | were made. | The | images | or other | third party | material | in  |
method to detect blinks is effective, however, we intend this article are included in the article’s Creative Commons licence,
to improve blink detection when there is more noise in unlessindicatedotherwiseinacreditlinetothematerial.Ifmaterial
|           |       |               |     |         |     |           |      | is not included | in         | the article’s | Creative | Commons   | licence    | and        | your |
| --------- | ----- | ------------- | --- | ------- | --- | --------- | ---- | --------------- | ---------- | ------------- | -------- | --------- | ---------- | ---------- | ---- |
| the data. | Also, | we understand |     | that we | had | a shorter | data |                 |            |               |          |           |            |            |      |
|           |       |               |     |         |     |           |      | intended        | use is not | permitted     | by       | statutory | regulation | or exceeds |      |
gatheringtimefortherestphaseinthisstudyandwebelieve
|     |     |     |     |     |     |     |     | the permitted | use, | you will | need | to obtain permission |     | directly | from |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | -------- | ---- | -------------------- | --- | -------- | ---- |
thatrecordingdataforalongerdurationinthatphasewould the copyright holder. To view a copy of this licence, visit http://
| yieldbetteraccuracy. |     |     |     |     |     |     |     | creativecommonshorg/licenses/by/4.0/. |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- |

2040 Pers Ubiquit Comput (2023) 27:2027–2041
References 19. HartSG(2006)Nasa-taskloadindex(nasa-tlx);20yearslater.In:
Proceedingsofthehumanfactorsandergonomicssocietyannual
meeting, vol 50. Sage Publications Sage CA, Los Angeles, pp
1. AgaA,ChanA,NarasimhanR(2019)Measuringpsychological
904–908
stress from cardiovascular and activity signals. US Patent App.
20. HastieH,RobbDA,LopesJ,AhmadM,BrasPL,LiuX,Petrick
10/213,146
R,LohanK,ChantlerMJ(2019)Challengesincollaborativehri
2. Bahrin MAK, OthmanMF, Azli NN, Talib MF(2016) Industry
forremoterobotteams.arXiv:1905.07379
4.0: a review on industrial automation and robotic. Jurnal
21. Heard J, Harriott CE, Adams JA (2018) A survey of workload
Teknologi78(6-13):137–143
assessment algorithms. IEEE Transactions on Human-Machine
3. BertholdA,JamesonA(1999)Interpretingsymptomsofcognitive
Systems48(5):434–451
loadinspeechinput.In:UM99usermodeling.Springer,pp235–
22. Hjortskov N, Risse´n D., Blangsted AK, Fallentin N, Lundberg
244
U, Søgaard K (2004) The effect of mental stress on heart rate
4. ChandlerP,SwellerJ(1996)Cognitiveloadwhilelearningtouse
variability and blood pressure during computer work. European
a computer program. Applied Cognitive Psychology 10(2):151–
JournalofAppliedPhysiology92(1-2):84–89
170
23. HollandMK,TarlowG(1972)Blinkingandmentalload.Psychol
5. ChenF,ZhouJ,WangY,YuK,ArshadSZ,KhawajiA,Conway
Rep31(1):119–127
D(2016)Eye-basedmeasures.SpringerInternationalPublishing,
24. HRV E (2018) How do you calculate the hrv score? Webpage.
Cham,pp75–85.https://doi.org/10.1007/978-3-319-31700-7 4
https://help.elitehrv.com/article/54-how-do-you-calculate-the-hrv-
6. ChenF,ZhouJ,WangY,YuK,ArshadSZ,KhawajiA,ConwayD
score
(2016)Galvanicskinresponse-basedmeasures.SpringerInterna-
25. HRV E(2019) Corsense heart rate variability. Webpage.https://
tional Publishing, Cham, pp 87–99. https://doi.org/10.1007/978-
elitehrv.com/corsense
3-319-31700-7 5
26. Jameson A, Kiefer J, Mu¨ller C, Großmann-hutter B, Wittig F,
7. ChenF,ZhouJ,WangY,YuK,ArshadSZ,KhawajiA,ConwayD
Rummer R (2010) Assessment of a user’s time pressure and
(2016)Robustmultimodalcognitiveloadmeasurement.Springer,
cognitive load on the basis of features of speech. In: Resource-
Berlin
adaptivecognitiveprocesses.Springer,pp171–204
8. Consortium BNC et al (2007) British national corpus version 3
27. Khawaja MA, Chen F, Marcus N (2010) Using language
(bnc xml edition). Distributed by Oxford University Computing
complexity to measure cognitive load for adaptive interaction
Services on behalf of the BNC Consortium. Retrieved February
design. In: Proceedings of the 15th international conference on
13,2012
intelligentuserinterfaces.ACM,pp333–336
9. Craig CL, Marshall AL, Sjo¨stro¨m M, Bauman AE, Booth ML,
28. KhawajaMA,ChenF,MarcusN(2012)Analysisofcollaborative
Ainsworth BE, Pratt M, Ekelund U, Yngve A, Sallis JF et al
communication for linguistic cues of cognitive load. Human
(2003) International physical activity questionnaire: 12-country
factors54(4):518–529
reliabilityandvalidity.Medicine&ScienceinSports&Exercise
29. Khawaja MA, Ruiz N, Chen F (2008) Think before you
35(8):1381–1395
talk: an empirical study of relationship between speech pauses
10. Cranford KN, Tiettmeyer JM, Chuprinko BC, Jordan S, Grove
and cognitive load. In: Proceedings of the 20th Australasian
NP(2014)Measuringloadonworkingmemory:theuseofheart
conferenceoncomputer-humaninteraction:designingforhabitus
rateasameansofmeasuringchemistrystudents’cognitiveload.J
andhabitat.ACM,pp335–338
ChemEduc91(5):641–647
11. FieldA(2009)DiscoveringstatisticsusingSPSS,3rdedn.Sage, 30. Kret ME, Sjak-Shie EE (2019) Preprocessing pupil size data:
London guidelines and code. Behavior Research Methods 51(3):1336–
12. Fogelholm M, Malmberg J, Suni J, Santtila M, Kyro¨la¨inen 1342
H, Ma¨ntysaari M, Oja P (2006) International physical activity 31. Leppink J, Paas F, Van der Vleuten CP, Van Gog T, Van
questionnaire: validity against fitness. Medicine and Science in Merrie¨nboer JJ (2013) Development of an instrument for
SportsandExercise38(4):753–760 measuring different types of cognitive load. Behavior Research
13. FrankS,ThompsonR(2012)Earlyeffectsofwordsurprisalon Methods45(4):1058–1072
pupilsizeduringreading.In:Proceedingsoftheannualmeeting 32. Leys C, Ley C, Klein O, Bernard P, Licata L (2013) Detecting
ofthecognitivesciencesociety,vol34 outliers: do not use standard deviation around the mean, use
14. FridmanL,ReimerB,MehlerB,FreemanWT(2018)Cognitive absolute deviation around the median. J Exp Soc Psychol
load estimation in the wild. In: Proceedings of the 2018 CHI 49(4):764–766
conferenceonhumanfactorsincomputingSystems.ACM,p652 33. Lobato-Rinco´n LL, Cabanillas-Campos MDC, Bonnin-Arias C,
15. Fro¨hlich P, Baldauf M, Meneweger T, Erickson I, Tscheligi M, Chamorro-Gutie´rrezE,Murciano-CespedosaA,Sa´nchez-Ramos
Gable T, de Ruyter B, Paterno` F (2019) Everyday automation RodaC(2014)Pupillarybehaviorinrelationtowavelengthand
experience:non-expertusersencounteringubiquitousautomated age.FrontiersinHumanNeuroscience8:221
systems. In: Extended abstracts of the 2019 CHI conference on 34. LopesJ,LohanK,HastieH(2018)Symptomsofcognitiveload
humanfactorsincomputingsystems,pp1–8 in interactions with a dialogue system. In: Proceedings of the
16. Gevins A, Smith ME, Leong H, McEvoy L, Whitfield S, Du workshoponmodelingcognitiveprocessesfrommultimodaldata.
R, Rush G (1998) Monitoring working memory load during ACM,p4
computer-based tasks with eeg pattern recognition methods. 35. Lopes J, Robb DA, Ahmad M, Liu X, Lohan K, Hastie H
HumanFactors40(1):79–91 (2019) Towards a conversational agent for remote robot-human
17. Gregoire J, Tuck S, Hughson RL, Yamamoto Y (1996) Heart teaming. In: 2019 14th ACM/IEEE international conference on
ratevariabilityatrestandexercise:influenceofage,gender,and human-robotinteraction(HRI).IEEE,pp548–549
physicaltraining.CanJApplPhysiol21(6):455–470 36. MayerRE,MorenoR(2003)Ninewaystoreducecognitiveload
18. Haapalainen E, Kim S, Forlizzi JF, Dey AK (2010) Psycho- inmultimedialearning.EducationalPsychologist38(1):43–52
physiologicalmeasuresforassessingcognitiveload.In:Proceed- 37. Mital A, Govindaraju M (1999) Is it possible to have a
ings of the 12th ACM international conference on ubiquitous single measure for all work? International Journal of Industrial
computing.ACM,pp301–310 Engineering-TheoryApplicationsandPractice6(3):190–195

Pers Ubiquit Comput (2023) 27:2027–2041 2041
38. Monster A, Chan H, O’Connor D (1978) Long-term trends 49. Siegle GJ, Ichikawa N, Steinhauer S (2008) Blink before and
in human eye blink rate. Biotelemetry and Patient Monitoring afteryouthink:blinksoccurpriortoandfollowingcognitiveload
5(4):206–222 indexedbypupillaryresponses.Psychophysiology45(5):679–687
39. MorrisCH,LeungYK(2006)Pilotmentalworkload:howwelldo 50. Stapel J, Mullakkal-Babu FA, Happee R (2019) Automated
pilotsreallyperform?Ergonomics49(15):1581–1596 drivingreducesperceivedworkload,butmonitoringcauseshigher
40. Mukherjee S, Yadav R, Yung I, Zajdel DP, Oken BS (2011) cognitiveloadthanmanualdriving.TransportationResearchPart
Sensitivity to mental effort and test–retest reliability of heart F:TrafficPsychologyandBehaviour60:590–605
rate variability measures in healthy seniors. Clin Neurophysiol 51. SwellerJ(1988)Cognitiveloadduringproblemsolving:effects
122(10):2059–2066 onlearning.CognitiveScience12(2):257–285
41. Noel JB, Bauer KW Jr, Lanning JW (2005) Improving pilot 52. Sweller J (1994) Cognitive load theory, learning difficulty, and
mental workload classification through feature exploitation and instructionaldesign.Learningandinstruction4(4):295–312
combination: a feasibility study. Computers & Operations 53. Sweller J, Van Merrienboer JJ, Paas FG (1998) Cognitive
Research32(10):2713–2730 architecture and instructional design. Educational Psychology
42. PaasF,TuovinenJE,TabbersH,VanGervenPW(2003)Cognitive Review10(3):251–296
loadmeasurement asameans toadvance cognitiveloadtheory. 54. TommasoDD(2018)Tobiiproglasses2pythoncontroller.Web-
EducationalPsychologist38(1):63–71 page.https://github.com/ddetommaso/TobiiProGlasses2 PyCtrl
43. Palinko O, Kun AL, Shyrokov A, Heeman P (2010) Estimating 55. Wan X, Wang W, Liu J, Tong T (2014) Estimating the sample
cognitive load using remote eye tracking in a driving simulator. meanandstandarddeviationfromthesamplesize,median,range
In:Proceedingsofthe2010symposiumoneye-trackingresearch and/orinterquartilerange.BMCMedicalResearchMethodology
&applications.ACM,pp141–144 14(1):135
44. PangB,LeeL(2004)Asentimentaleducation:sentimentanalysis 56. Wilson GF, Russell CA (2003) Real-time assessment of mental
using subjectivity summarization based on minimum cuts. In: workload using psychophysiological measures and artificial
ProceedingsoftheACL neuralnetworks.Humanfactors45(4):635–644
45. RapczynskiM,WernerP,Al-HamadiA(2019)Effectsofvideo 57. Wurhofer D, Meneweger T, Meschtscherjakov A, Gerdenitsch
encoding on camera-based heart rate estimation. IEEE Trans C, Tscheligi M Experiencing automation in the factory and
BiomedEng66(12):3360–3370 automotive domain: differences, similarities, and challenges
46. ReillyJ,KellyA,KimSH,JettS,ZuckermanB(2018)Thehuman workshop proceedings everyday automation experience’19 in
task-evoked pupillary response function is linear: implications conjunction with chi’19, May 5th, 2019, Glasgow, UK website:
forbaselineresponsescalinginpupillometry.BehaviorResearch http://everyday-automation.tech-experience.at
Methods,pp1–14 58. Yin B, Chen F, Ruiz N, Ambikairajah E (2008) Speech-based
47. SabyrulyY,BrozF,KellerI,LohanK(2015)Gazeandattention cognitive load monitoring system. In: 2008 IEEE international
during an hri storytelling task. In: Artificial intelligence for conferenceonacoustics,speechandsignalprocessing.IEEE,pp
human-robot interaction: AAAI 2015 fall symposium series, 2041–2044
AI-HRI 2015; Conference date: 12-11-2015 through 14-11- 59. ZhangJ,YinZ,WangR(2015)Recognitionofmentalworkload
2015 levels under complex human–machine collaboration by using
48. Shi Y, Ruiz N, Taib R, Choi E, Chen F (2007) Galvanic skin physiological features and adaptive support vector machines.
response(gsr)asanindexofcognitiveload.In:CHI’07extended IEEETransactionsonHuman-MachineSystems45(2):200–214
abstracts on human factors in computing systems, CHI EA ’07.
ACM, New York, pp 2651–2656. https://doi.org/10.1145/12408 Publisher’s note Springer Nature remains neutral with regard to
66.1241057 jurisdictionalclaimsinpublishedmapsandinstitutionalaffiliations.