IEEETRANSACTIONSONAFFECTIVECOMPUTING,VOL.?,NO.?,?? 1
AMIGOS: A Dataset for Affect, Personality and
Mood Research on Individuals and Groups
Juan Abdon Miranda-Correa, Student Member, IEEE, Mojtaba Khomami Abadi, Student Member, IEEE,
Nicu Sebe, Senior Member, IEEE, and Ioannis Patras, Senior Member, IEEE
Abstract—WepresentAMIGOS–AdatasetforMultimodalresearchofaffect,personalitytraitsandmoodonIndividualsandGrOupS.
Differenttootherdatabases,weelicitedaffectusingbothshortandlongvideosintwosocialcontexts,onewithindividualviewersandone
withgroupsofviewers.Thedatabaseallowsthemultimodalstudyoftheaffectiveresponses,bymeansofneuro-physiologicalsignals
ofindividualsinrelationtotheirpersonalityandmood,andwithrespecttothesocialcontextandvideos’duration.Thedataiscollected
intwoexperimentalsettings.Inthefirstone,40participantswatched16shortemotionalvideos.Inthesecondone,theparticipants
watched4longvideos,someofthemaloneandtherestingroups.Theparticipants’signals,namely,Electroencephalogram(EEG),
Electrocardiogram(ECG)andGalvanicSkinResponse(GSR),wererecordedusingwearablesensors.Participants’frontalHDvideo
andbothRGBanddepthfullbodyvideoswerealsorecorded.Participantsemotionshavebeenannotatedwithbothself-assessmentof
affectivelevels(valence,arousal,control,familiarity,likingandbasicemotions)feltduringthevideosaswellasexternal-assessmentof
levelsofvalenceandarousal.Wepresentadetailedcorrelationanalysisofthedifferentdimensionsaswellasbaselinemethodsand
resultsforsingle-trialclassificationofvalenceandarousal,personalitytraits,moodandsocialcontext.Thedatabaseismadepublicly
available.
IndexTerms—EmotionClassification,EEG,Physiologicalsignals,Signalprocessing,Personalitytraits,Mood,AffectSchedules,
Patternclassification,AffectiveComputing.
(cid:70)
1 INTRODUCTION commonly engaged by groups of people together). In such
contexts,theindividualexperiencesdonotdependonlyon
Affective computing aims for the detection, modeling and
theuserandthecontent,butalsoontheimplicitandexplicit
synthesis of human emotional cues in Human-Computer
interactions that can occur between the personalities, reac-
Interaction[1].Inthisfield,anincreasinginteresthasarisen
tions, moods and emotions of other group members. Ad-
forconsideringtheuser’saffectiveresponseswhenmaking
ditionally, different aspects of affect and personality could
computationaldecisions.Forinstance,Chaneletal[2]mod-
be inhibited or amplified depending on the social context
ified the difficulty of a video game according to the user’s
of a person. Therefore, current databases have ignored an
affective(emotional)statetomaintainhighengagement.In
importantdimensionforthestudyofaffect.
a hypothetical scenario, the time-line of a movie could be
Databases for personality research have considered in-
adaptedtoelicitspecificaffectivestates,takingintoaccount
formation related to linguistics in written text [8], social
factorssuchastheviewer’spredictedemotions,personality
networks activity [9], and behavior in group activities [10].
andmood.Hence,inthesescenarios,itisveryimportantto
Howevertheyhavelargelyignoredthestudyofboth,affect
reliablypredictsuchfactors.
and personality, through the use of physiological signals,
Advancesonthepredictionofaffectivestateshavebeen
which have shown to carry valuable information for per-
boostedbytheavailabilityofannotatedaffectivedatabases,
sonalityrecognition[11],[12].
which act as benchmark for many researchers to develop
Therefore, there is a need of multimodal databases for
their methodologies. These databases have used stimuli,
thestudyofpeople’semotions,personalityandmood,with
such as music videos [1], short videos [3], [4], and diverse
subjects in both alone and group settings. The multimodal
emotion elicitation methods [5]. They include information
frameworkwouldbenefitfromtheinclusionofneurological
fromdifferentmodalities(e.g.EEG,facialexpression).
andperipheralphysiologicalsignals.
Available multimodal affective databases have focused
Our contribution to the field is A dataset for Multi-
on the study of affective responses of participants in in-
modal research of affect, personality traits and mood on
dividual [1], [6], or pairs of people/limited agent settings
Individuals and GrOupS (AMIGOS) by means of neuro-
[7]. However, in real life, affective experiences are often
physiological signals. The dataset consists of multimodal
performed in social contexts (e.g. movies and games are
recordings of participants and their responses to emotional
Juan Abdon Miranda-Correa and Ioannis Patras are with the School of fragments of movies. In our dataset: (i) The participants
Computer Science and Electronic Engineering, Queen Mary University of took part in two experiments. In each of them, the par-
London,UK.E-mail:{j.a.mirandacorrea,i.patras}@qmul.ac.uk.
ticipants watched one of two sets of stimuli, one of short
MojtabaKhomamiAbadiandNicuSebearewiththeDepartmentofInforma-
videos and one of long videos, while their implicit re-
tionEngineeringandComputerScience,UniversityofTrento,Italy.E-mail:
{khomamiabadi,sebe}@disi.unitn.it. sponses, namely, Electroencephalogram (EEG), Electrocar-
7102
rpA
31
]CN.oib-q[
3v01520.2071:viXra

| 2   |     |     |     |     |     |     |     | IEEETRANSACTIONSONAFFECTIVECOMPUTING,VOL.?,NO.?,?? |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
diogram (ECG), Galvanic Skin Response (GSR), frontal HD onesofextraversion,agreeableness,emotionalstabilityand
video, and both RGB and depth full body videos were openness, and significant positive correlations between the
recorded.Therecordingshavebeenpreciselysynchronized scores of agreeableness and both extraversion and positive
to allow the study of affective responses, personality and affect (PA), between consciousness and emotional stability,
mood from the different modalities simultaneously. (ii) In and between PA and arousal. Finally, (v) our method for
thefirstexperiment,allparticipantswatchedthesetofshort personalitytraits,moodandsocialcontextpredictionbased
videosinindividualsetting.Inthesecondexperiment,some onneuro-physiologicalsignalsofshortandlongvideosout-
oftheparticipantstookpartinindividualsettingandsome performsapreviousstudy[11]inpredictionofextroversion,
ofthemingroupsettings.Thentheywatchedthesetoflong emotionalstability,PAandNAusignEEGandinprediction
videos. (iii) The participants have been profiled according ofconscientiousness,opennessandconscientiousnessusing
to their personality through the Big-Five personality traits physiologicalsignals(ECGandGSR).
model, and according to their mood through the Positive In section 2, works related to the modeling and assess-
Affect and Negative Affect Schedules (PANAS). (iv) Affec- ment of affect, personality and mood are discussed, and
tive annotation has been obtained with both internal and a survey of the main multimodal databases available for
externalannotations.Intheinternalannotation,participants affect and personality research and a comparison with our
performed self-assessment of their affective levels at the arepresented.Section3presentstheexperimentalscenarios,
beginning of each experiment and immediately after each stimuli selection, modalities and equipment used to record
video. In the external annotation, the recordings of both the implicit responses. Then, an overview of the experi-
sets of videos were off-line annotated by 3 annotators on mental setup for both experiments and the methods em-
both valence and arousal scales, using a method that al- ployedforassessmentofaffect,personalitytraitsandmood
lows the direct comparison of the affective responses from (PANAS)aredescribed.InSection4,thedataobtainedfrom
| both experiments. |     | (v) | The physiological |     | signals | have | been |               |             |     |     |           |         |     |          |
| ----------------- | --- | --- | ----------------- | --- | ------- | ---- | ---- | ------------- | ----------- | --- | --- | --------- | ------- | --- | -------- |
|                   |     |     |                   |     |         |      |      | the different | experiments |     | is  | analyzed. | Section | 5   | presents |
recorded using commercial wearable sensors that allow our method for single trial valence and arousal recognition
more freedom for the participants than conventional labo- as well as our approach for personality traits, PANAS and
ratoryequipment(e.g.BiosemiActiveTwo1)usedin[1],[3],
socialcontextrecognitionusingneuro-physiologicalsignals.
[6] and of better quality than the equipment used in [12]. The results are then presented and discussed. Finally, we
Thedatabaseisavailabletotheacademiccommunity2. concludeinsection6.
| In this  | work,        | we  | present     | a comparison |         | between | the      |     |     |     |     |     |     |     |     |
| -------- | ------------ | --- | ----------- | ------------ | ------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| internal | and external |     | annotations | of           | valence | and     | arousal. |     |     |     |     |     |     |     |     |
We then perform a detailed correlation analysis between 2 RELATED WORKS
theaffectiveresponseselicitedbytheshortandlongvideos
Inthissection,wemakeareviewoftheworksrelatedwith
| with respect      | of   | social      | context | (whether        | a   | participant | was     |          |      |            |              |         |             |      |       |
| ----------------- | ---- | ----------- | ------- | --------------- | --- | ----------- | ------- | -------- | ---- | ---------- | ------------ | ------- | ----------- | ---- | ----- |
|                   |      |             |         |                 |     |             |         | modeling | and  | assessment | of           | affect, | personality | and  | mood. |
| alone or          | in a | group       | during  | the experiment) |     | and         | between |          |      |            |              |         |             |      |       |
|                   |      |             |         |                 |     |             |         | Next, we | make | a review   | of important |         | databases   | that | study |
| the participants’ |      | personality |         | traits, PANAS   |     | and social  | con-    |          |      |            |              |         |             |      |       |
affect,personalityandmood.
| text. We                  | also           | present    | baseline | methodologies |     | and      | results  |                               |     |     |     |     |     |     |     |
| ------------------------- | -------------- | ---------- | -------- | ------------- | --- | -------- | -------- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- |
| for single-trial          |                | prediction | of       | valence       | and | arousal, | and for  |                               |     |     |     |     |     |     |     |
| prediction                | of personality |            | traits,  | PANAS         | and | social   | context, |                               |     |     |     |     |     |     |     |
|                           |                |            |          |               |     |          |          | 2.1 Affect,PersonalityandMood |     |     |     |     |     |     |     |
| using neuro-physiological |                |            | signals  | (EEG,         | ECG | and      | GSR) as  |                               |     |     |     |     |     |     |     |
singlemodalitiesandfusionofthem. Plutchnik [13] has defined emotion as a complex chain of
Ourmainfindingsareasfollows:(i)Weshowthatthere loosely connected events that begins with a stimulus and
includesfeelings,psychologicalchanges,impulsestoaction
| is significant | correlation |     | between | the | internal | and | external |     |     |     |     |     |     |     |     |
| -------------- | ----------- | --- | ------- | --- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
annotation of valence and arousal for the short videos andspecific,goal-directedbehavior.Themostcommonap-
experiment, which indicates that external annotation is a proaches to model affect are categorical and dimensional.
good predictor of the affective state of participants. (ii) We The first approach claims that there exists a small number
|          |             |     |          |        |          |              |     | of emotions | that | are basic | and | recognized | universally; |     | The |
| -------- | ----------- | --- | -------- | ------ | -------- | ------------ | --- | ----------- | ---- | --------- | --- | ---------- | ------------ | --- | --- |
| show, by | correlation |     | analysis | of the | external | annotations, |     |             |      |           |     |            |              |     |     |
thatintheeyesoftheannotators,participantsseemtohave most common of these models is the Six Basic Emotions
low arousal in low valence moments and high arousal for model, presented by Ekman et al [14], that categorizes
|     |     |     |     |     |     |     |     | emotions | into fear, | anger, | disgust, | sadness, |     | happiness | and |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ------ | -------- | -------- | --- | --------- | --- |
highvalencemoments.(iii)Wefoundsignificantdifferences
in the distribution of valence and arousal, externally anno- surprise. The dimensional approach considers that affec-
tated,betweentheparticipantsthatwerealonecomparedto tive states are inter-related in a systematic way (e.g. the
|     |     |     |     |     |     |     |     | Plutchik’s | emotion | wheel | [13]). | Russell | [15] | introduced | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ----- | ------ | ------- | ---- | ---------- | --- |
theparticipantsthatwereingroupsduringthelongvideos
experiment.Itwasdifferentfortheshortvideosexperiment CircumplexModelofAffect,whereaffectivestatesarerepre-
where the distribution of arousal and valence for the 2 sets sentedinatwodimensionalspacewitharousal(thedegree
|                 |     |         |               |     |           | (p  | > 0.05). | anemotionfeelsactive)andvalence(thedegreeanemotion |     |     |     |     |     |     |     |
| --------------- | --- | ------- | ------------- | --- | --------- | --- | -------- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| of participants |     | are not | statistically |     | different |     |          |                                                    |     |     |     |     |     |     |     |
This result was expected since, as stated before, all the feelspleasant)asthemaindimensions.
participantswatchedtheshortvideoswithinthesamesocial Affective experiences are also modulated by people’s
context (alone). (iv) We found significant negative correla- internalfactors,suchasmoodandpersonality[16].Person-
tions between the scores of negative affect (NA) and the ality refers to stable individual characteristics, that explain
|     |     |     |     |     |     |     |     | and predict | behavior    |     | [17]. The | Big-Five | factor | model        | [18] |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | --- | --------- | -------- | ------ | ------------ | ---- |
|     |     |     |     |     |     |     |     | describes   | personality |     | in terms  | of five  | traits | (dimensions) |      |
1.http://www.biosemi.com/
|     |     |     |     |     |     |     |     | namely | Extraversion | (sociable |     | vs reserved), |     | Agreeableness |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | --------- | --- | ------------- | --- | ------------- | --- |
2.http://www.eecs.qmul.ac.uk/mmv/datasets/amigos/

MIRANDA-CORREAETAL:AMIGOS:ADATASETFORMOOD,PERSONALITYANDAFFECTRESEARCHONINDIVIDUALSANDGROUPS 3
(compassionatevsdispassionateandsuspicious),Conscien- RA, ST, ECG, blood volume, Zygomaticus and Trapezius
tiousness (dutiful vs easy-going), Emotional stability (ner- muscles Electromyogram and Electrooculogram) research.
vous vs confident) and Openness to experience (curious vs It consists of video and signals’ recordings of 32 partici-
cautious). The common method to measure these dimen- pantswhilewatching40musicvideoclips.Itincludesself-
sions is the use of questionnaires such as the Neuroticism, assessmentofarousal,valence,liking,dominanceandfamil-
ExtraversionandOpenessFiveFactorInventory(NEO-FFI) iarity.AsimilardatabasethatusesMagnetoencephalogram
[19]andtheBig-FiveMarkerscale(BFMS)[18]. (MEG) is the DECAF database, which includes recordings
Mood refers to baseline levels of affect that define peo- of30participantsinresponseto40one-minutemusicvideo
ples experiences. It is commonly modeled using the two and 36 movie clips. More recently, Zhang et al [5] collected
dimensions called Positive Affect (PA) and Negative Affect the Multimodal Spontaneous Emotion Corpus for Human
(NA) scales [20]. PA and NA are related to corresponding BehaviorAnalysis.Itincludes140participantsfromvarious
affectivetraitdimensionsofpositiveandnegativeemotion- ethnic origins. They used 10 different emotion elicitation
ality [20]. PA reflects the extent to which a person feels methods for specific target emotions (ee.gg. surprise, dis-
enthusiastic, active and alert. In contrast, NA is a general gust, fear). Recorded signals are 3D and 2D videos, ther-
dimension of subjective distress and unpleasant engage- mal sensing, electrical conductivity of the skin, respiration,
ment.In order to measure these two dimensions (PA and blood pressure and hearth rate. It includes annotations of
NA),Watsonetal[21]developedthePositiveandNegative the occurrence and intensity of AUs. These databases have
AffectSchedules(PANAS)thatconsistoftwo10-itemmood notconsideredstudyingparticipantsingroupsetting.
scales;Thesescheduleshaveshowntobeinternallyconsis-
Oneofthefirstdatabasesforpersonalityresearchusing
tent,uncorrelatedandstableovera2-monthtimeperiod. video modality, is the Mission Survival II corpus [10]. It
|     |     |     |     |     |     |     |     | is a multimodal |     | annotated | collection |     | of video | and audio |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | ---------- | --- | -------- | --------- |
2.2 DatabasesforAffectiveComputing
|     |     |     |     |     |     |     |     | recordings | (using | 4 cameras | and | 17 microphones) |     | of four |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | --------- | --- | --------------- | --- | ------- |
Databases for the study of affective computing have been meetings, of 4 participants engaging in a mission survival
developedtoallowresearcherstocompareresults.Here,we task. Participants were profiled in terms of the Ten Item
|             |           |     |          |        |              |     |         | Personality | Inventory |     | [24] to | account | for their | personality |
| ----------- | --------- | --- | -------- | ------ | ------------ | --- | ------- | ----------- | --------- | --- | ------- | ------- | --------- | ----------- |
| will review | databases |     | based on | video, | neurological |     | signals |             |           |     |         |         |           |             |
and/orphysiologicalsignalsmodalities.Asfarasweknow, states (moments where participants act more or less intro-
thereisnotasingledatabasedevelopedformoodresearch. vert/extravert,creative,ect).Thisdatasetisnotintendedfor
Databases for the study of affect recognition based on affect research. A recent multi-modal database for implicit
videohavefocusedmainlyontheanalysisoffacialexpres- personalityandaffectrecognitionistheASCERTAIN[25].It
sions. One of the main examples is the Sustained Emotion- includesrecordingsoftheEEG,ECG,GSRandfacialvideo
ally Colored Machine-human Interaction using Nonverbal of 58 users, while viewing short movie clips. They showed
Expression (SEMAINE) database [7]. It consists of high- that personality differences are better revealed while com-
quality, multimodal recordings of 150 participants in emo- paring user responses to emotionally homogeneous videos
tionally colored conversations. It is annotated for valence, (videosthatsharethesamequadrantofthevalence-arousal
arousal and Facial Action Coding System (FACS) action space). This database only includes participants in individ-
units (AUs). Another example is the Affectiva-MIT Facial ual configuration and does not share data about mood of
| ExpressionDataset(AM-FED)[22].Itisalabeleddatasetof |     |     |     |     |     |     |     | participants. |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
spontaneousfacialresponsesrecordedinnaturalsettingson Tothebestofourknowledgetherearenotdatabasesfor
theInternet.Thedatasetconsistsof242facialvideos,labels personalityresearchbasedonneurologicalorphysiological
ofthepresenceof10symmetricaland4asymmetricalAUs, signalsandthatstudiesparticipantsinbothindividualand
2 head movements, smile, general expressiveness, feature groupsettings.InTable1,wesummarizethecharacteristics
tracker fails, gender, location of 22 automatically detected oftherevieweddatabasesandcomparethemtoours.
| landmark   | points | and      | self-report | responses |        | of familiarity, |     |                |     |     |       |     |     |     |
| ---------- | ------ | -------- | ----------- | --------- | ------ | --------------- | --- | -------------- | --- | --- | ----- | --- | --- | --- |
| liking and | desire | to watch | again.      | The       | Denver | Intensity       | of  |                |     |     |       |     |     |     |
|            |        |          |             |           |        |                 |     | 3 EXPERIMENTAL |     |     | SETUP |     |     |     |
SpontaneousFacialAction(DISFA)database[23]consistsof
labeledstereovideorecordingsof27adultswhilewatching In this section, the experimental scenarios are described.
| a video | clip. Labels | consist | of  | presence, | absence | and | inten- |          |         |          |     |               |     |            |
| ------- | ------------ | ------- | --- | --------- | ------- | --- | ------ | -------- | ------- | -------- | --- | ------------- | --- | ---------- |
|         |              |         |     |           |         |     |        | Then the | process | followed | for | the selection | of  | stimuli is |
sityof12facialAUs. explained, and the modalities and equipment used are
Databases for affect research based on physiological presented. Then, the experimental protocol is described
signals include the MAHNOB-HCI [6]. It is a multimodal in detail. Finally, the procedures for internal and external
| database | that | consists | of synchronized |     | recordings |     | of face |            |     |            |     |               |             |     |
| -------- | ---- | -------- | --------------- | --- | ---------- | --- | ------- | ---------- | --- | ---------- | --- | ------------- | ----------- | --- |
|          |      |          |                 |     |            |     |         | annotation | of  | affect and | for | participants’ | personality | and |
video, audio signals, eye gaze data and physiological sig- moodassessmentareintroduced.
| nals (ECG, | GSR,    | respiration | amplitude |              | (RA), | skin   | temper-  |                           |     |     |     |     |     |     |
| ---------- | ------- | ----------- | --------- | ------------ | ----- | ------ | -------- | ------------------------- | --- | --- | --- | --- | --- | --- |
| ature (ST) | and     | EEG)        | of 27     | participants |       | while  | watching |                           |     |     |     |     |     |     |
|            |         |             |           |              |       |        |          | 3.1 Experimentalscenarios |     |     |     |     |     |     |
| first, 20  | videos, | and second, | short     | videos       | and   | images | with     |                           |     |     |     |     |     |     |
relevant/non-relevant tags. It includes the self-reports of The main objective of this work is to study the person-
the felt emotions using arousal, valence, dominance, pre- ality, mood and affective responses of people engaging
dictability scales, emotional keywords and agreement or with multimedia content in two social contexts, (i) when
disagreementwiththetags.KoelstraetalpresenttheDEAP they are alone (individual setting), and (ii) when they are
database [1], with the purpose of implicit affective tag- part of an audience (group setting). At the same time, we
ging from EEG and peripheral physiological signals (GSR, study people’s affective response to two types of eliciting

4 IEEETRANSACTIONSONAFFECTIVECOMPUTING,VOL.?,NO.?,??
TABLE1
Summaryofcharacteristicsofdatabasesforaffectandpersonality.Lastrowisourdatabase.
Database No. Individual Purpose Modalities Annotations
Part. vs.Group
SEMAINE[7] 150 Individual Emotionrecognitionbasedon AudioandVisual Valence,arousalandFACS.
facialexpressions
AM-FED [22] 242 Individual Spontaneousfacialexpression Visual 14AUs,2headmovements,smile,expressive-
recognition”In-the-Wild” nessand22landmarkpoints.Self-assessment
offamiliarity,likinganddesiretowatchagain.
DISFA [23] 27 Individual Spontaneous facial action Visual 12AUs.
recognition
MAHNOB-HCI[6] 27 Individual Emotion recognition and im- Visual,Audio,EyeGaze,ECG,GSR, Self-assessment of valence, dominance, pre-
plicittagging RespirationAmplitude,Skintempera- dictability and emotional keywords. Agree-
ture,EEG ment/disagreementwithtags.
DEAP[1] 32 Individual Implicitaffectivetaggingfrom EEG, GSR, Respiration Amplitude, Self-assessment of arousal, valence, liking,
EEG and peripheral physio- Skin Temperature, Blood Volume, dominanceandfamiliarity.
logicalsignals Electromyogram and Electrooculo-
gram.Visualfor22participants.
DECAF[3] 30 Individual Affectrecognition MEG,Near-infra-redfacialvideo,hor- Self-assessmentofvalence,arousalanddomi-
izontal Electrooculogram, ECG and nance.Continuousannotationofvalenceand
trapezius-Electromyogram. arousalofthestimuli.
Zhangetalcorpus[5] 140 Individual Emotionalbehaviourresearch 3D dynamic imaging, Visual, Ther- OccurrenceandintensityofAUs.Featuresfrom
malsensing,EDA,Respiration,Blood 3D,2DandInfra-redsensors.
PressureandHearthRate
MissionSurvivalII 16 4 people Personalitystatesresearch AudioandVisual PersonalitystatesbytheTenItemPersonality
[10] group Inventory.
ASCERTAIN[25] 58 Individual PersonalityandAffect EEG,ECG,GSRandVisual Big-Five personality traits, self-assessment of
valenceandarousal.
AMIGOS 40 Individual Affect,personality,moodand Audio,Visual,Depth,EEG,GSRand Big-Five personality traits and PANAS. Self-
& 4 people socialcontextrecognition ECG assessmentofvalence,arousal,dominance,lik-
group ing, familiarity and basic emotions. External
annotationofvalenceandarousal.
content. The first type consists of short emotional videos TABLE2
(duration<250s) selected to elicit specific affective states in Theshortvideoslistedwiththeirsources(VideoIDsarestatedin
parentheses).Inthecategorycolumn,H,L,AandVstandforhigh,low,
the participants. The second type consists of long videos
arousalandvalencerespectively.
(duration>14min), that present situations that could elicit
various affective states over their duration and where the
Category Excerpt’ssource
story and the narrative could give context to the affective HAHV Airplane(4),WhenHarryMetSally(5),HotShots(9),LoveActually
responses. Therefore, we have designed two experiments, (80)
LAHV AugustRush(10),LoveActually(13),HouseofFlyingDaggers(18),
in the first one (Short videos experiment), all participants MrBeans’Holiday(58)
watched short affective videos in individual setting. In the LALV Exorcist(19),Mygirl(20),MyBodyguard(23),TheThinRedLine
(138)
secondexperiment(Longvideosexperiment),thesamepar-
HALV SilentHill(30),Prestige(31),PinkFlamingos(34),BlackSwan(36)
ticipants watched long videos, but this time some of them
diditinindividualsetting,whiletheothersdiditingroup TABLE3
SelectedLongVideoswithTheirID,Source(Movietitle.Director.
setting.
Producercompany.ReleasedYear.)andExcerptDuration.
ID Source Duration
3.2 Stimuliselection N1 TheDescent.Dir.NeilMarshall.Lionsgate.2005. 23:35.0
BacktoSchoolMr.Bean.Dir.JohnBirkin.TigerAspectProduc-
P1 18:43.0
Emotion elicitation depends greatly on a careful selection tions.1994.
B1 TheDarkKnight.Dir.ChristopherNolan.WarnerBross.2008. 23:30.0
of the stimuli, which needs to be suitable for the objective
Up.Dirs.PeteDocterandBobPeterson.WaltDisneyPictures
U1 14:06.0
of the study and allow for consistent results among trials andPixarAnimationStudios.2009.
[1].Inthiswork,weselectedtwosetsofvideosforemotion
elicitation. The first one consists of short emotional videos Forthesecondsetofvideos,weinitiallyselected8video
and the second one of long videos. For the first set, 72 vol- extracts from movies based on their score in the IMDb Top
unteers annotated, on the valence and arousal dimensions, Rated Movies list3. We selected movies that could allow us
the set of 36 videos used in [3]. We then classified each of to extract a long segment (≈ 20min) which could be self-
thevideosintooneoffourquadrantsofthevalence-arousal contained, did not require previous knowledge from the
(VA) space, namely HVHA, HVLA, LVHA and LVLA (H, participants to be understood and with strongly affective
L,AandVstandforhigh,low,arousalandvalencerespec- multimediacontent(goodcombinationofmusicandcolors
tively). From each quadrant, we selected the three videos [26]). Four researchers classified them as belonging to one
thatlayfurthertotheoriginofthescale,totaling12videos. or more quadrants of the VA space. Finally, 4 videos were
Additionally, from the videos used in [6], we selected four selected favoring the extracts that could evoke emotions in
videos, each corresponding to one of the four quadrants. different quadrants of the VA space, and making sure all
The total number of selected short videos is 16, 4 for each thequadrantswerecovered.Theselectedlongvideos(14.1-
quadrantoftheVAspace.WehavepreservedtheIDsused 23.58min,µ=20.0,σ =4.5)withtheircorrespondingvideo
in the original datasets. The selected short videos (51-150s ID,sourceanddurationarelistedinTable3.
long,µ=86.7,σ =27.8)withtheircorrespondingcategory
ontheVAspaceandtheirIDsarelistedinTable2. 3. http://www.imdb.com/chart/top

MIRANDA-CORREAETAL:AMIGOS:ADATASETFORMOOD,PERSONALITYANDAFFECTRESEARCHONINDIVIDUALSANDGROUPS 5
3.3 Neuro-PhysiologicalSignalsandInstruments 3.5 SynchronizationandStimuliDisplayPlatform
Werecordedthreemainneuralandperipheralphysiological One PC (Intel Core i7, 3.4 GHz) was used to (i) present the
signalsnamelyElectroencephalogram(EEG),Electrocardio- stimuli, (ii) get and synchronize signals, and, in the case of
gram(ECG)andGalvanicSkinResponse(GSR),whichhave theshortvideosexperiment,(iii)obtaintheself-assessment
shown good performance in affect estimation studies [27]– of participants. Shimmer sensors were paired to the PC
[29].Belowwegiveanintroductionofeachofthem. using the bluetooth standard, while the Emotiv headset
EEG:Electroencephalogramisarecordingoftheelectri-
|     |     |     |     |     |     |     |     | was paired | using | a   | proprietary |     | wireless | standard. | Videos |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | --- | ----------- | --- | -------- | --------- | ------ |
calactivityalongthescalp.Itmeasuresvoltagefluctuations were presented in a 40-inch screen (1280×1024), each of
resulting from ionic current flows within the brain [30]. themwasdisplayedpreservingtheoriginalaspectratioand
| EEG signals | carry | valuable | information |     | about | the | person’s |          |     |         |             |     |           |     |           |
| ----------- | ----- | -------- | ----------- | --- | ----- | --- | -------- | -------- | --- | ------- | ----------- | --- | --------- | --- | --------- |
|             |       |          |             |     |       |     |          | covering | the | highest | screen-area |     | possible. | The | remaining |
affectivestate[1],[31]. areawasfilledwithblackbackground.Subjectswereseated
GSR:Galvanicskinresponse,alsoknownaselectroder- approximately 2 meter from the screen. Stereo speakers
mal activity (EDA), measures the electrical conductance of were used and the sound volume was set at a relatively
the skin [32], usually performed with one or two sensors loudlevel,howeveritwasadjustedwhennecessary.
attachedtosomepartofthehandorfoot[33].Skinconduc-
tivityvarieswithchangesinskinmoisturelevel(sweating)
|           |        |         |     |             |     |         |        | 3.6 ShortVideosExperimentProtocol |     |     |     |     |     |     |     |
| --------- | ------ | ------- | --- | ----------- | --- | ------- | ------ | --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| which can | reveal | changes | in  | sympathetic |     | nervous | system |                                   |     |     |     |     |     |     |     |
related to arousal [29], [34]. Changes in GSR are related to Recordings were performed in a laboratory environment
thepresenceofemotionssuchasstressorsurprise[34]. with controlled illumination. 40 healthy participants (13
ECG: Electrocardiogram is a recording of the electrical female), aged between 21 and 40 (mean age 28.3), took
|     |     |     |     |     |     |     |     | part in | the experiment. |     | Prior | to  | the recording | session, | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | --- | ----- | --- | ------------- | -------- | --- |
activityoftheheart.Itisdetectedbyelectrodesattachedto
theskinsurface,whichpickupelectricalimpulsesgenerated participantsreadandsignedaconsentform.Thentheyread
by the polarization and depolarization of cardiac tissue. a sheet with instructions about the experiment, and an ex-
perimenteransweredtheirquestions.Whentheinstructions
ECGcanrevealchangesoftheautonomousnervoussystem
relatedtoaffectiveexperiencesandstress[27]. were clear, the participants were led into the experiment
In previous databases, neuro-physiological signals have room. After that, the experimenter explained the affective
been recorded using laboratory equipment (e.g. Biosemi scales used in the experiment and how to fill in the self-
ActiveTwo)whichisexpensiveandlimitsthemobilityofthe assessment form (See 3.8.1). Next, the sensors were placed
participants. In this database, the neuro-physiological sig- andtheirsignalscheckedwithatestrecordingtoassessthe
nals have been recorded using wearable sensors that allow qualityofthesignals.Finally,theexperimenterlefttheroom
morefreedomgiventhattheyusewirelesstechnology.EEG andtherecordingsessionbegan.
was recorded using the Emotiv EPOC Neuroheadset4 (14 The participants performed an initial self-assessment
channel,128Hz,14bitresolution).EEGchannelsaccording for arousal, valence and dominance, as well as selection
to the 10-20 [28] system are: AF3, F7, F3, FC5, T7, P7, O1, of basic emotions (Neutral, Happiness, Sadness, Surprise,
O2, P8, T8, FC6, F4, F8, AF4. ECG was recorded using the Fear,AngerandDisgust)theyfeltbeforeanystimulushave
Shimmer2R5platformextendedwithanECGmoduleboard been shown. Next, 16 videos were presented in a random
orderin16trials,eachconsistingof:(1)A5secondbaseline
| (256 Hz, | 12 bit | resolution), |     | which | uses | three | electrodes, |     |     |     |     |     |     |     |     |
| -------- | ------ | ------------ | --- | ----- | ---- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
two of them are placed at the right and left arm crooks recordingshowingafixationcross.(2)Thedisplayofasmall
and the third one at the internal face of the left ankle as video. (3) Self-assessment of arousal, valence, dominance,
reference. This set-up allows precise identification of heart likingandfamiliarityas wellasselectionofbasicemotions
beats as well as the full ECG QRS complex. GSR signal (See3.8.1).Afterthe16trials,therecordingsessionended.
| recorded   | using | the Shimmer |     | 2R platform |              | extended | with     | a                                |     |     |     |     |     |     |     |
| ---------- | ----- | ----------- | --- | ----------- | ------------ | -------- | -------- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| GSR module | board | (128        | Hz, | 12 bit      | resolution), |          | with two |                                  |     |     |     |     |     |     |     |
|            |       |             |     |             |              |          |          | 3.7 LongVideosExperimentProtocol |     |     |     |     |     |     |     |
electrodesplacedatthemiddlephalangesofthelefthand’s
middleandindexfingers. The participants that took part in the short videos ex-
|     |     |     |     |     |     |     |     | periment,  | performed |       | the long  | videos | experiment |          | in either |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ----- | --------- | ------ | ---------- | -------- | --------- |
|     |     |     |     |     |     |     |     | individual | or        | group | settings. | In the | individual | setting, | par-      |
3.4 VideoRecordings
ticipantsperformedtheexperimentalone.Inthegroupset-
| Frontal       | face video | was     | recorded   |       | in HD      | quality | using       | a                  |               |           |               |                 |            |          |             |
| ------------- | ---------- | ------- | ---------- | ----- | ---------- | ------- | ----------- | ------------------ | ------------- | --------- | ------------- | --------------- | ---------- | -------- | ----------- |
|               |            |         |            |       |            |         |             | ting, participants |               | performed |               | the             | experiment | together | with        |
| JVC GY-HM150E |            | camera, | positioned |       | just below |         | the screen. |                    |               |           |               |                 |            |          |             |
|               |            |         |            |       |            |         |             | 3 other            | participants. |           | Only          | 37 participants |            | took     | part in the |
| Additionally, | both       | RGB     | and        | depth | full body  | videos  | were        |                    |               |           |               |                 |            |          |             |
|               |            |         |            |       |            |         |             | long videos        | experiment    |           | (participants |                 | 8, 24      | and 28   | were not    |
V16
| recorded | using | a Microsoft’s |     | Kinect | placed |     | at the top |     |     |     |     |     |     |     |     |
| -------- | ----- | ------------- | --- | ------ | ------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
available),17oftheminindividualsettingand20ingroup
| of the screen. |     | Though | this | study | does not | use | the visual |     |     |     |     |     |     |     |     |
| -------------- | --- | ------ | ---- | ----- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
setting(5groupsof4people).Inordertomaximizeinterac-
| modality, | Mou | et al | [35], [36] | have | explored |     | the visual |     |     |     |     |     |     |     |     |
| --------- | --- | ----- | ---------- | ---- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
tions,groupswereformedtoincludepeoplethatkneweach
| modality | on our | dataset | for | prediction | of affect, |     | social con- |     |     |     |     |     |     |     |     |
| -------- | ------ | ------- | --- | ---------- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
other,beingeitherfriends,colleagues,orpeoplewithsimilar
| text and          | group | belonging. | A       | participant |              | during | the short |                   |            |         |           |     |                 |     |           |
| ----------------- | ----- | ---------- | ------- | ----------- | ------------ | ------ | --------- | ----------------- | ---------- | ------- | --------- | --- | --------------- | --- | --------- |
|                   |       |            |         |             |              |        |           | cultural          | background |         | [37]. The | IDs | of participants |     | that were |
| videos experiment |       | and        | a group | of          | participants | during | the       |                   |            |         |           |     |                 |     |           |
|                   |       |            |         |             |              |        |           | in the individual |            | setting | and       | in  | each group      | of  | the group |
longvideosexperimentcanbeobservedinFig.1.
settingarelistedinTable4.
|     |     |     |     |     |     |     |     | During | the | recording |     | sessions, | the | participant(s) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --------- | --- | --------- | --- | -------------- | --- |
4. http://www.emotiv.com/
|     |     |     |     |     |     |     |     | was(were) | led | to the | recording |     | room. While | the | different |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------ | --------- | --- | ----------- | --- | --------- |
5. http://www.shimmersensing.com/
sensorsweresetup,experimentersexplainedthedifferences
6. http://developer.microsoft.com/windows/kinect/hardware

6 IEEETRANSACTIONSONAFFECTIVECOMPUTING,VOL.?,NO.?,??
(a) (b) (c) (d) (e) (f)
Fig.1.Participantinexperimentconditionsduringtheshortvideosexperimentrecordedin(a)FrontalHDvideo,(b)fullbodyRGBvideoviaKinect,
(c)fullbodydepthvideoviaKinect;andgroupof4participantsduringthelongvideosexperimentrecordedin(d)frontalHDvideo,(e)fullbody
RGBvideoviaKinectand(f)fullbodydepthvideoviaKinect.
TABLE4 3.8.1 Participant’sAffectSelf-assessment
ParticipantIDsforIndividualandGroupSettingsofthelongvideos
At the beginning of the recording session of the short
experiment.Inthegroupsetting,theIDsorderrepresenttheorderin
whichparticipantswereseated,fromafrontview,fromlefttoright. videos experiment, and of each of the two recording sub-
sessions of the long videos experiment, participants per-
Part.ID Part.ID
formed a self-assessment of their levels of arousal, valence
Group1 7,1,2,16 Group5 15,11,12,10
Group2 6,32,4,3 and dominance, and were asked to select basic emotions
Individual 9,13,19,20,23,25,26,30,21,
Group3 29,5,27,21 Participants 33,34,35,36,37,38,39,40 that described what they were feeling at the start of each
Group4 18,14,17,22
session/sub-session. Then, at the end of each trial, partici-
pantsperformedaself-assessmentofthesamedimensionas
of the protocol compared to the short videos experiment.
the initial self-assessment, and of the liking and familiarity
Every participant was given a set of self-assessment paper
thatdescribedwhattheyfeltduringeachvideo.
forms (See 3.8.1) and a pen, that were used to assess their
The self-assessment form used for the short videos ex-
affectivestateatthebeginningandattheendofeachvideo.
periment can be seen in Fig. 2. Self-assessment manikins
Experimentersavoidedtomentionwhethertheparticipants
(SAM) [41] were used to visualize the scales of va-
could talk during the experiment, for the interactions to be
lence, arousal and dominance. For the liking scale, thumbs
spontaneous. Once the sensors had been tested, the experi-
down/thumbs up symbols were used. This inquires the
menterslefttheroomandtherecordingsessionstarted.
participants’ tastes, not feelings. The fifth scale asks the
Theexperimentconsistedofthedisplayof4longvideos
participantstoratetheirfamiliaritywiththevideo.Arousal
inrandomorder.Videoswereshownintworecordingsub-
scale ranges from “very calm” (1) to “very excited” (9).
sessions, each consisting of: (1) initial self-assessment (45s)
Valence from “very negative” (1) to “very positive” (9).
of arousal, valence, dominance and selection of basic emo-
Dominance from “overwhelmed with emotions” (1) to “in
tions.(2)thedisplay,intwotrials,oftwolongvideos,each
full control of emotions” (9). The fourth scale ranges from
followed by (3) self-assessment (45s) of arousal, valence,
disliking (1) to liking (9) the video. The familiarity scale
dominance, liking and familiarity, and selection of basic
ranges from “Never seen it before” (1) to “Know the video
emotions (See 3.8.1). After the first sub-session a break of
very well” (9). Participants moved a continuous slider,
15 minutes was given for the participants to rest. During
placed at the bottom of each scale, to specify their self-
this time they were offered refreshments. After the break,
assessment level. They were informed they could move
sensors’signalswerecheckedandthesecondrecordingsub-
the slider anywhere directly below or in-between of the
sessionstarted,afterwhichtheexperimentended.
manikins. Finally, participants were asked to select at least
After the long videos experiment, participants were
one of the basic emotions (Neutral, Disgust, Happiness,
asked to fill in as soon as possible, on-line forms with Per-
Surprise,Anger,FearandSadness[14]),orasmanyasthey
sonalityTraits[38]andPANAS[21]questionnaires(See3.9).
felt during the video (a participant can consider a video to
Participantstook2daysonaveragetofillintheforms.Once
bebothsurprisingandsad).
theyfilledinallrequiredforms,theyweregivenmugsand
Inthelongvideosexperiment,havingadigitalformfor
universitygadgetsinreturnfortheirparticipation.
every participant of the groups was not practical, therefore
weoptedtouseapaperversionoftheforminFig.2inboth
3.8 AffectiveAnnotation
individual and group setting recordings, in order to keep
Internal annotation (self-assessment) is the process were a consistenttheself-assessmentbetweensettings.
subject directly assess its affective state while performing a In total, for the short videos experiment 17 annotations
task[39].Ithastheadvantageofbeinganeasy,andpossibly, were obtained from each participant (1 at the beginning of
the most direct way to assess affective states. At the same theexperimentand1aftereachofthe16shortvideos),and
time, it is an intrusive process, subjects could be unreliable 6annotationsinthecaseofthelongvideosexperiment(1at
at reporting their emotions or they could hide their real beginning of the first recording sub-session, 1 after each of
emotions [40]. External annotation (implicit assessment) is the two long videos of the first recording sub-session, 1 at
a process that intends to assess a person’s affective state thebeginningofthesecondrecordingsub-sessionjustafter
without it being actively involved in the process. The as- the15minutebreakand1aftereachofthetwolongvideos
sessmentisperformedbyexternalmeanssuchasanalyzing ofthesecondrecordingsub-session).Itisimportanttonote
theperson’sbehaviorand/oritsphysiologicalresponses[6]. that this annotation gives information related only to the
We have performed both internal and external annotations participants’initialandfinalaffectivestates,notforspecific
toassesstheparticipants’affectivestate. instantsduringthevideos.

MIRANDA-CORREAETAL:AMIGOS:ADATASETFORMOOD,PERSONALITYANDAFFECTRESEARCHONINDIVIDUALSANDGROUPS 7
|     |     |     |     |     |     |     |     | 3.9 PersonalityandMoodAssessment |        |             |        |       |               |      |          |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | ------ | ----------- | ------ | ----- | ------------- | ---- | -------- |
|     |     |     |     |     |     |     |     | The Big-Five                     |        | personality | traits | were  | measured      | with | an on-   |
|     |     |     |     |     |     |     |     | line form                        | of the | big-five    | marker | scale | questionnaire |      | [18], in |
which,foreachpersonalitytrait,usingthebasicquestion“I
seemyselfasaperson:”,tendescriptiveadjectivesarerated
witha7-point-likert-scale[42]andameaniscalculated.
Moodwasassessedonthepositiveaffect(PA)andneg-
|     |     |     |     |     |     |     |     | ative affect | (NA) | schedules |     | (PANAS) | [43] | model, | using an |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | --------- | --- | ------- | ---- | ------ | -------- |
on-lineformofthegeneralPANASquestionnaire[43]which
consistsoftwo10questionssets,eachtoaccessthePAand
|     |     |     |     |     |     |     |     | NArespectively. |     | Participantsrated |     |     | theirgeneral |     | feelingsin |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------------- | --- | --- | ------------ | --- | ---------- |
a5-pointintensityscaleusingquestionslike“Doyoufeelin
general...?”(e.g.active,afraidSee[43]).PANASiscalculated
|     |     |     |     |     |     |     |     | by summing |     | the ratings | of  | all 10 | questions | for PA | and NA |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----------- | --- | ------ | --------- | ------ | ------ |
respectively,resultinginvaluesbetween10and50.
|     |     |     |     |     |     |     |     | The | distribution |     | of the | Big-Five | personality |     | traits, PA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------ | -------- | ----------- | --- | ---------- |
andNA,over(i)the37participantsthattookpartinthelong
videosexperiment,(ii)the17participantsoftheindividual
setting,and(iii)the20participantsofthegroupsetting,are
|     |     |     |     |     |     |     |     | presented | in  | Figure | 3. Note | that | PA and | NA scores | have |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------ | ------- | ---- | ------ | --------- | ---- |
beenscaledbya0.1factor.Thedifferenceofdistributionof
Fig. 2. Self-Assessment Form for Assessment of Arousal, Valence, ratings,foreachofthesevendimensionsofpersonalityand
Dominance,Liking,FamiliarityandBasicEmotions. PANAS, between the participants of individual and group
settings,isnotsignificant(p>0.1accordingtoatwosample
t-testforeverydimension).
3.8.2 ExternalAffectAnnotation
Inordertostudythetemporalevolutionofaffect,thefrontal
|     |     |     |     |     |     |     |     | 4 DATA | ANALYSIS |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- |
videosofeachparticipantrecordedduringthedisplayofthe
stimuli of both experiments were off-line annotated on the In this section, we present a detailed analysis of the data
valanceandarousaldimensionsasfollows. gatheredinbothexperiments.
| First, | the videos | of  | a given | participant |     | recorded | during |     |     |     |     |     |     |     |     |
| ------ | ---------- | --- | ------- | ----------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
|        |            |     | 20      |             |     | (16      |        |     |     |     |     |     |     |     |     |
the display of each of the stimuli videos short and 4.1 Self-AssessmentvsExternalAnnotation
| 4 long), | were manually |        | cropped   | in       | order | to show  | only   | a            |     |             |      |           |     |              |     |
| -------- | ------------- | ------ | --------- | -------- | ----- | -------- | ------ | ------------ | --- | ----------- | ---- | --------- | --- | ------------ | --- |
|          |               |        |           |          |       |          |        | The external |     | annotations | were | validated |     | by assessing | the |
| squared  | region        | around | the face, | covering |       | from the | top of |              |     |             |      |           |     |              |     |
the head to the start of the shoulders. Then each of the inter-annotator agreement. For this, the annotations corre-
spondingtoeachparticipantperformedbyeveryannotator
participants’facevideosweresplitinto20secondclips.For
weremappedtothe[0,1]range,where0correspondstolow
this,thefirst20secondsofeachvideo,including5seconds
|             |                  |          |           |                               |        |           |           | and 1 to   | high  | valence(arousal), |                  | then     | the      | Cronbach’s  | α [44]    |
| ----------- | ---------------- | -------- | --------- | ----------------------------- | ------ | --------- | --------- | ---------- | ----- | ----------------- | ---------------- | -------- | -------- | ----------- | --------- |
| prior to    | the presentation |          | of the    | stimuli,                      | were   | extracted | as        |            |       |                   |                  |          |          |             |           |
|             |                  |          |           | 5s                            |        |           |           | statistic  | among | annotators,       |                  | commonly | used     | for         | agreement |
| first clip, | then,            | starting | from      | the                           | of the | video     | (instant  |            |       |                   |                  |          |          |             |           |
|             |                  |          |           |                               |        |           |           | assessment | on    | continuous        | scales           |          | [7], was | calculated. | Mean      |
| in which    | the stimuli      |          | started), | n = (cid:98)(D)/(20s)(cid:99) |        |           | non over- |            |       |                   |                  |          |          |             |           |
|             |                  |          |           |                               |        |           |           | Cronbach’s | αs    | over              | all participants |          | of 0.98  | for valence | and       |
| lapping     | segments         | of       | 20s were  | extracted,                    | with   | D         | being the |            |       |                   |                  |          |          |             |           |
0.96
durationofthestimulivideoinseconds.Finally,thelast20 for arousal were obtained, which indicates a very
stronginterannotatorreliabilityforbothdimensions.
| seconds | of the video |     | were extracted |     | as final | clip. | For every |      |     |           |         |     |      |         |            |
| ------- | ------------ | --- | -------------- | --- | -------- | ----- | --------- | ---- | --- | --------- | ------- | --- | ---- | ------- | ---------- |
|         |              |     |                |     |          |       |           | With | the | objective | to test | at  | what | degree, | the affec- |
participant,{6,7,5,6,4,5,8,5,7,5,9,5,5,4,6,7,72,58,72
and44}clipswereobtainedrespectivelyfromvideos{4,5, tive state of participants assessed through self-assessment,
9,10,13,18,19,20,23,30,31,34,36,58,80,138,N1,P1,B1
andU1},totaling340clipsperparticipant,94corresponding
totheshortand246tothelongvideosexperiment.
Threeannotatorsratedonthevalenceandarousalscales
theclipsofalltheparticipants(340clips×37participants=
| 12580 clips). | Both             | scales | were | continuous | and               | ranged | from |     |     |     |     |     |     |     |     |
| ------------- | ---------------- | ------ | ---- | ---------- | ----------------- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| −1            |                  |        |      | 1          |                   |        |      |     |     |     |     |     |     |     |     |
| (low          | valence/arousal) |        | to   | (high      | valence/arousal). |        | The  |     |     |     |     |     |     |     |     |
340clipsofagivenparticipant,wereannotatedinthesame
| random           | order by  | each        | annotator, | however,     |             | the order       | of the |         |              |     |              |             |     |        |                |
| ---------------- | --------- | ----------- | ---------- | ------------ | ----------- | --------------- | ------ | ------- | ------------ | --- | ------------ | ----------- | --- | ------ | -------------- |
| clips was        | different | for         | each       | participant. | Since       | samples         | of     |         |              |     |              |             |     |        |                |
| both experiments |           | were        | randomly   | shown        | to          | the annotators, |        |         |              |     |              |             |     |        |                |
| labels of        | the two   | experiments |            | are directly | comparable. |                 | The    |         |              |     |              |             |     |        |                |
|                  |           |             |            |              |             |                 |        | Fig. 3. | Distribution | of  | the Big-Five | Personality |     | Traits | (Extraversion, |
pipelineoftheannotationconsistedofthedisplayofaran-
Agreeableness,Conscientiousness,EmotionalStabilityandOpenness)
| domly selected |     | clip followed |     | by the | annotation | performed |     |     |     |     |     |     |     |     |     |
| -------------- | --- | ------------- | --- | ------ | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andPositiveAffectandNegativeAffectSchedules(PAandNA)for(i)All,
by the annotator, first, of valence and then of arousal. This (ii) Individual setting, and (iii) Group setting participants of the Long
processwasrepeateduntilallclipswereannotated. VideosExperiments.PAandNAarescaledbya0.1factor.

| 8   |     |     |     |     |     |     |     | IEEETRANSACTIONSONAFFECTIVECOMPUTING,VOL.?,NO.?,?? |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     | 4.2 AnalysisofValenceandArousalforIndividualand    |     |     |     |     |     |     |     |
GroupSettings
|         |     |     |     |         |     |     |     | The external  |          | annotations | of  | both         | experiments | have      | been   |
| ------- | --- | --- | --- | ------- | --- | --- | --- | ------------- | -------- | ----------- | --- | ------------ | ----------- | --------- | ------ |
| lasuorA |     |     |     | lasuorA |     |     |     |               |          |             |     |              |             |           |        |
|         |     |     |     |         |     |     |     | analyzed      | to test  | if valence  |     | and arousal, |             | expressed | by the |
|         |     |     |     |         |     |     |     | participants, | differed | depending   |     | on           | the social  | context.  | Two    |
setsofparticipantswereconsidered.Thefirstset(individual
|     |     |     |     |     |     |     |     | set) corresponds |     | to the | 17 participants |     | that | took part | in the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------ | --------------- | --- | ---- | --------- | ------ |
longvideosexperimentinindividualsetting,andthesecond
|     |     |     |     |     |     |     |     | set (group | set) | corresponds | to  | the | 20 participants |     | took part |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ----------- | --- | --- | --------------- | --- | --------- |
ingroupsetting.
|     |     | Valence |     |     |     | Valence |     |     |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(a) (b) In Fig. 5, the differences in annotations of valence and
arousalfortheindividualsetincomparisonwiththegroup
Fig.4.DistributionofratingsofValencevsArousal,for(a)participants’ set for both short and long videos experiments are shown.
self-assessmentofthe16shortvideosexperiment,and(b)meanexter-
nalannotationsoverallannotatorsfor94twenty-secondsegmentsofthe Fig. 5(a) and (d) show the mean valence and arousal anno-
videosoftheshortvideosexperiment.Smallcirclesindicatethemean tations for (i) the individual set (red curve), (ii) the group
scores over all participants for each of the videos (video ID indicated set (blue curve), and (iii) all participants (black dashed
| through | arrows). | Circles | are color | coded | according | to  | the expected |     |     |     |     |     |     |     |     |
| ------- | -------- | ------- | --------- | ----- | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
affective response (See Table 2). H, L, V and A, refer to high, low, curve), for each of the 340 20s clips. The clips are shown
valenceandarousal. by the video they are part of and ordered according their
|     |     |     |     |     |     |     |     | appearance | in  | the video.       | In  | the       | figure, | clips where | the       |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---------------- | --- | --------- | ------- | ----------- | --------- |
|     |     |     |     |     |     |     |     | difference | in  | the distribution |     | of scores |         | for the     | group set |
is represented by the external annotations, a comparison are significantly lower or higher (p < 0.05 according to a
between the self-assessment and external annotations of two sample t-test) with respect to the one of the individual
valence and arousal, for the short videos experiment, was set are marked with black points and have been shadowed
performed. For each participant, the Spearman correlation (orange for group scores < individual scores and gray for
coefficientaswellasthep-valueforthepositivecorrelation groupscores>individualscores).Fig.5(b)and(e),showthe
|      |      |            |         |                     |     |     |           | mean annotations |     | of valence |     | and arousal, |     | for the | same sets |
| ---- | ---- | ---------- | ------- | ------------------- | --- | --- | --------- | ---------------- | --- | ---------- | --- | ------------ | --- | ------- | --------- |
| test | were | calculated | between | the self-assessment |     |     | scores of |                  |     |            |     |              |     |         |           |
each video and the mean external annotation over all the of participants, of the clips of the short videos experiment,
annotatorsandsegmentsofeachvideo.Assumingindepen- whereas Fig. 5(c) and (f) present the mean annotations for
dence,theresultingp-valueswerecombinedtoonep-value the clips of the long videos experiment. In the (b), (c), (e)
using Fisher’s method [45]. For valence, the mean correla- and (f) graphs, samples are ordered according to the mean
tionoverallparticipantsis0.44(p<.05),and0.15(p<.05) scoreoverallparticipants(dashedblackcurve).Theclipsfor
for arousal. These correlations are statistically significant whichthedifferencebetweenthedistributionofscoresfrom
individualandgroupsetsissignificant(p<0.05according
| which | indicates |     | that the external | annotation |     | is a | good pre- |     |     |     |     |     |     |     |     |
| ----- | --------- | --- | ----------------- | ---------- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
dictor of the affective state of participants, though for the toatwosamplet-test)aremarkedwithblackpoints.
| arousal | dimension |     | the correlation | is  | low | which | shows that |      |      |          |        |        |          |      |          |
| ------- | --------- | --- | --------------- | --- | --- | ----- | ---------- | ---- | ---- | -------- | ------ | ------ | -------- | ---- | -------- |
|         |           |     |                 |     |     |       |            | From | Fig. | 5(a) and | (d) it | can be | observed | that | both the |
itiseasiertoexternallyassessvalencethanarousal. high and low areas of the valence and arousal dimensions
In Figure 4(a), the distribution of the self-assessment of are covered between all the videos. Comparing the graphs
|         |     |         |        |              |     |           |        | of the short | videos | experiment |     | (Fig. | 5(b) | and (e)) | with the |
| ------- | --- | ------- | ------ | ------------ | --- | --------- | ------ | ------------ | ------ | ---------- | --- | ----- | ---- | -------- | -------- |
| valence | and | arousal | of all | participants | for | the short | videos |              |        |            |     |       |      |          |          |
experiments (16 samples per participant) can be observed. onesofthelongvideosexperiment(Fig.5(c)and(f)),itcan
Annotations of each participant have been mapped to the be observed that in the short videos experiment, where all
[−1,1] participants were alone, 21.3% of the clips present signif-
|     | range. | The | graph | includes | circles | representing | the |     |     |     |     |     |     |     |     |
| --- | ------ | --- | ----- | -------- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mean scores, over all participants, of each video. It can be icant differences in valence between group and individual
observed that in general valence elicitation worked better participants, and they are concentrated in the low valence
|      |          |         |     |              |            |     |         | region, | and 2.1% | of the | clips | present | significant | differences |     |
| ---- | -------- | ------- | --- | ------------ | ---------- | --- | ------- | ------- | -------- | ------ | ----- | ------- | ----------- | ----------- | --- |
| than | arousal, | showing | a   | well defined | separation |     | between |         |          |        |       |         |             |             |     |
low and high valence stimuli. Even though the separation inarousal.Inthelongvideosexperiment,wheresomepar-
of arousal is not as prominent, still there is a difference ticipants were in groups, 25.6% of the clips present signifi-
between low and high arousal stimuli. Figure 4(b) shows cant difference of valence between groups and individuals.
48%
the distribution of the external annotations of valence and It is important to note that the clips with significant
arousal over the 16 videos of the short videos experiment differencesappearinthehighvalenceregion(meanvalence
(94 samples by participant). The mean scores, over all the > 0). For arousal, 26.4% of the clips present significant
|           |     |       |               |     |         |              |     | differences | between | groups |     | and | individuals. | In  | Fig. 5(f), |
| --------- | --- | ----- | ------------- | --- | ------- | ------------ | --- | ----------- | ------- | ------ | --- | --- | ------------ | --- | ---------- |
| 20-second |     | clips | of each video | and | all the | participants | are |             |         |        |     |     |              |     |            |
markedwithcircles.Itcanbeobservedthatthedatashows where it is observed that in the long videos experiment,
a V-shape relating valence and arousal, which is a result of group participants showed lower levels of arousal for low
|     |     |     |     |     |     |     |     | arousal | clips | as well | as higher | levels | of  | arousal | for high |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ------- | --------- | ------ | --- | ------- | -------- |
thedifficultyofelicitinghigh-levelsofarousalwithneutral
valence, and high/low levels of valence with low arousal. arousalclipsthanindividuals.
It can also be observed that in general participants showed The Spearman correlation coefficient ρ and the p-value
theexpectedaffectivestates(e.g.participantsshowedhigher were calculated between the social context label and the
valence(arousal)withhighvalence(arousal)contentincom- mean external annotations for valence and arousal, for the
parisonto low valence(arousal) content),though thediffer- clipsofthelongvideosexperiments.Thesocialcontextlabel
enceisnotasclearasinself-assessment(Fig.4(a)). wasconsidered0iftheparticipantwasinindividualsetting

MIRANDA-CORREAETAL:AMIGOS:ADATASETFORMOOD,PERSONALITYANDAFFECTRESEARCHONINDIVIDUALSANDGROUPS 9
VH→−ecnelaV−←VL
4 5 9 01 31 81 91 02 32 03 13 43 63 85 08 831
0.4 Individual 0.4 0.4
Group
0.2 0.2 0.2
All
0.0 0.0 0.0
-0.2 -0.2 -0.2
-0.4 -0.4 -0.4
N1 P1 B1 U1 0 20 40 60 80 0 50 100 150 200 250
(a) (b) (c)
AH→−lasuorA−←AL
4 5 9 01 31 81 91 02 32 03 13 43 63 85 08 831
0.4 0.4 0.4
0.2 0.2 0.2
0.0 0.0 0.0
-0.2 -0.2 -0.2
-0.4 -0.4 -0.4
N1 P1 B1 U1 0 20 40 60 80 0 50 100 150 200 250
(d) (e) (f)
Fig. 5. Mean external annotations of Valence (V, upper graphs (a), (b) and (c)) and Arousal (A, lower graphs (d), (e), and (f)), over individual
participants(redcurve),groupparticipants(bluecurve)andallparticipants(dashedblackcurve),forthevideosof((a)and(d))bothshortandlong
videosexperiments(340segments),((b)and(e))theshortvideosexperiment(94segments),and((c)and(f))thelongvideosexperiment(246
segments).Clipswherethedistributionofscoresofindividualparticipantsissignificantlydifferentthantheoneofgroupparticipants(p < 0.05
accordingtoatwosamplet-test),aremarkedwithblackpoints.Inthecaseof(a)and(d),videoIDsareindicatedinthecaptions.Clipswherethe
distributionofscoresofindividualparticipantsissignificantlyhigherthantheoneofgroupparticipants(p<0.05),arehighlightedinorange.Clips
wherethedistributionofscoresofgroupparticipantsissignificantlyhigherthantheoneofindividualparticipantsarehighlightedingray.Inthecase
of(b),(c),(d)and(f)thehorizontalaxisrepresentthenumberofclips.Originofvalenceandarousal(horizontalaxisat(V =0)and(A=0))divides
thescaleintohigh-valence(HV:V >0)andlow-valence(LV:V <0),andintohigh-arousal(HA:A>0)andlow-arousal(LA:A<0).
and 1 if it was in group setting. Significant positive corre- TABLE5
lation (ρ = 0.37, p < 0.05) was found between the social Inter-correlationBetweentheDimensionsofPersonality,PANAS,
SocialContextintheLongVideosExperiment,andBy-participant
context and the mean valence. This significant correlation
MeanExternalAnnotationsforValenceandArousalofShortVideos
implies that, in the long videos experiment, participants andLongVideos.Significantcorrelations(p<0.05)areinbold.Ag.
in group setting showed higher valence than the ones in Co.E.S.,Op.andS.C.refertoAgreeableness,Conscientiousness,
EmotionalStability,OpennessandSocialContextrespectively.
individual setting. Significant correlation was not found
betweensocialcontextandarousalscores(p>0.05),which
suggest that social context does not have a common effect Dims. Ag. Co. E.S. Op. PA NA S.C. Valence Arousal
Short Long Short Long
inthearousalexpressedbytheparticipantsforallclips.
Ex. 0.44* 0.09 0.21 0.13 0.32 -0.48* 0.20 -0.01 0.02 0.05 0.18
Fig. 5 (c) and (f) show that the scores for clips with Ag. - 0.34* 0.14 0.24 0.43* -0.41* 0.18 -0.21 0.00 0.13 0.21
low levels of valence(arousal), present a different behavior Co. - - 0.35* -0.01 0.26 -0.26 0.07 -0.12 0.14 0.13 0.19
than the ones with high levels. Therefore, analyses have E.S. - - - 0.24 -0.12 -0.64* 0.03 0.21 0.11 -0.18 -0.15
Op. - - - - 0.20 -0.35* -0.04 0.23 0.13 0.06 0.02
been independently performed for the low and high va-
PA - - - - - -0.06 -0.03 -0.03 0.16 0.30 0.61*
lence(arousal)clipsofthelongvideosexperiment.Foreach NA - - - - - - -0.01 -0.28 -0.02 -0.12 0.04
ofthetwodimensions(valenceandarousal),theclipswere
sorted based on their score in increasing order, then half
of the clips with the lower scores were classified as low
For personality and PANAS, positive significant cor-
class (e.g. low valence) and the other half as high class
relations (p < 0.05) were obtained between extraversion
(e.g. high valence). A two sample t-test of the mean scores
and agreeableness, agreeableness and both conscientious-
ofvalence(arousal)wereperformedbetweentheindividual
nessandPA,andconscientiousnessandemotionalstability.
and group settings for the clips of low and high classes
NA is negatively correlated to all personality and PA di-
of valence(arousal). Significant difference was found be-
mensions. For social context, significant differences in per-
tween individual and group settings for the high valence
sonality and PANAS distribution between individual and
(p < 0.001), low arousal (p < 0.001) and high arousal
groupparticipantswerenotobtained,whichimplythatthe
clips (p < 0.05), but not for low valence clips (p = 0.90).
groupandindividualparticipantshavesimilardistribution
Therefore, social context has an important effect on the
ofpersonalities(e.g.individualandgroupparticipantshave
valenceandarousalexpressedbytheparticipants.
similar levels of extraversion). In general, correlations be-
tween personality and PANAS with respect to valence and
4.3 Affect,Personality,MoodandSocialContext
arousalwerenotsignificant,whichimpliesthatpersonality
In Table 5, the Spearman inter-correlations observed be- andmooddonotnecessarilyaffectthelevelsofvalenceand
tween the dimensions of personality, PANAS and social arousalexpressedbytheparticipants,withtheexceptionof
context in the long videos experiment are shown. It also PAwhichshowedsignificantpositivecorrelation(0.61)with
shows the inter-correlations that those dimensions have respect to arousal of the long videos, which indicates that
withthemeanexternalannotationsofvalenceandarousal, high-PA participants showed higher levels of arousal (they
oftheclipsoftheshortandlongvideosexperiments. showedmoreactiveemotions)thanlow-PAparticipants.

10 IEEETRANSACTIONSONAFFECTIVECOMPUTING,VOL.?,NO.?,??
5 AFFECT, PERSONALITY AND PANAS RECOGNI- TABLE6
TION FROM NEURO-PHYSIOLOGICAL SIGNALS ExtractedAffectiveFeaturesforeachModality(featuredimension
statedinparenthesis).Computedstatisticsare:mean,standard
In this section, our baseline methods and results for pre- deviation(std),skewness,kurtosisoftherawfeatureovertimeand%
oftimesthefeaturevalueisabove/belowmean±std.
diction of affect (valence and arousal), personality, PANAS
andsocialcontextusingneuro-physiologicalsignalsarepre- Modality Extractedfeatures
sented.First,thefeaturesextractedfromtheusedmodalities EEG(105) 5 bands (theta, slow alpha, alpha, beta and gamma) PSD
foreachelectrode.Thespectralpowerasymmetrybetween
are described. Next, our method for single modality and 7pairsofelectrodesinthefivebands.
fusion of modalities for single-trial classification of affect is ECG(77) RootmeansquareofthemeansquaredofIBIs,meanIBI,60
spectralpowerinthebandsfrom[0-6]Hzcomponentofthe
presented.Then,ourmethodforsingle-trialclassificationof ECGsignal,lowfrequency[0.01,0.08]Hz,mediumfrequency
[0.08,0.15]andhightfrequency[0.15,0.5]Hzcomponentsof
personality traits, PANAS and social context, using single
HRVspectralpower,HRandHRVstats.
modalitiesanddifferentschemesforfusionofmodalitiesis GSR(31) Meanskinresistanceandmeanofderivative,meandiffer-
entialfornegativevaluesonly(meandecreaserateduring
presented.Finally,ourresultsarepresentedanddiscussed.
decaytime),proportionofnegativederivativesamples,num-
beroflocalminimaintheGSRsignal,averagerisingtimeof
theGSRsignal,spectralpowerinthe[0-2.4]Hzband,zero
5.1 EEG,ECGandGSRFeatures crossingrateofskinconductanceslowresponse(SCSR)[0-
0.2] Hz, zero crossing rate of skin conductance very slow
response(SCVSR)[0-0.08]Hz,meanSCSRandSCVSRpeak
The neuro-physiological modalities of EEG, ECG and GSR
magnitude.
were used to record the participants’ implicit responses to
affective content. Below, the extracted features from the
employed modalities are described. All the features were were mapped to the [−1,1] range in order to avoid the
calculatedusingthesignalsrecordedduringeachofthe340 baseline differences that are natural to different recording
twenty-second clips described in section 3.8.2. Different to sessions. This was done for every participant, considering
other studies that use the concatenation of ECG and GSR each of the 4 long videos as a recording session and the
as one modality, we study each of them independently to recordings of the 16 videos of the short videos experiment
account for the contribution of each one to the recognition asafifthsession.Foreachofthemodalities(EEG,ECGand
task.ThesummaryoffeaturesislistedinTable6. GSR), three scenarios were tested. The first one considers
EEG: Following [1], power spectral density (PSD) fea- to train and test the system only with the samples of the
tureswereextractedfromtheEEGsignals.Forthis,theEEG short videos experiment (94 samples by participant). The
datawasprocessedusingthesamplingfrequencyof128Hz. secondconsidersonlythesamplesofthelongvideosexper-
The signals were average-referenced and high-pass filtered iment(246samplesbyparticipant).Thethirdoneconsiders
with a 2 Hz cut-off frequency. Eye artefacts were removed the combination of the samples of all the videos of both
withablindsourceseparationtechnique[46].Byemploying experiments (340 samples by participant), giving in total 9
the Welch method with windows of 128 samples (1.0s), recognitiontasksforeveryaffectdimension.
PSDs,between3and47Hz,ofthesignalsofeveryclipwere Leave-one-participant-out cross validation was used, in
calculated for each of the 14 EEG channels. The obtained which,inordertopredicteachaffectdimensionj label,for
PSDs were then averaged over the frequency bands of eachparticipantiaGaussian(G)Na¨ıveBayes(NB)classifier
theta (3-7 Hz), slow alpha (8-10 Hz), alpha (8-13 Hz), beta is trained. A NB G assumes independence of the features
(14-29 Hz) and gamma (30-47 Hz), and their logarithms andisgivenby:
were obtained as features. Additionally, the spectral power G(f ,...,f )=argmax p(C =c) (cid:81)n p(F =f |C =c)
1 n c i=1 i i
asymmetry between the 7 pairs of symmetrical electrodes,
in the five bands, was calculated. 105 PSD features were
whereF isthesetoffeaturesandC theclasses.p(F
i
=
obtained(14channel*5bandsand7symmetricalchannels f i |C = c) is estimated by assuming Gaussian distributions
of the features and modeling these from the training set.
*5bands)foreverysample(SeeTable6).
In each step of the cross validation, from the N available
ECG: Following [47], the heart beats were accurately
participants, the samples of one participant are used as the
localizedinECGsignals(R-peaks)tocalculatetheinterbeat
testsetandthesamplesoftheremainingN−1participants
intervals (IBI). Using IBI values, the heart rate (HR) and
areusedasthetrainingset.
heartratevariability(HRV)timeserieswerecalculated.Fol-
For feature selection, Fisher’s linear discriminant J [48]
lowing[6]and[47]77featureswereextracted(SeeTable6).
|µ −µ |
GSR: Following the method of Kim [47], the skin con- defined as J(f) = 1 0 is calculated for each feature
σ2+σ2
ductance(SC)wascalculatedfromtheGSRandthentheSC 1 0
from the training samples. Features are then sorted in de-
signalwasnormalized.Thenormalizedsignalwaslow-pass
creasingorderaccordingtotheirJ valueandwithasecond
filteredwith0.2Hzand0.08Hzcut-offfrequenciestogetthe
10-fold cross-validation over the training set, the optimal
lowpass(LP)andverylowpass(VLP)signals,respectively.
[1 : h] most discriminative features are selected. Then, the
Then, the filtered signals were de-trended by removing the
classifier is trained over all the samples of the training set
continuouspiecewiselineartrendinthetwosignals.31GSR
usingtheselectedfeatures,thenitistestedinthetestset.
featuresemployedin[1],[6]werecalculated(SeeTable6).
For each of the three scenarios (short, long and all
videos), feature level fusion of modalities has also been
5.2 Single Trial Classification of Affect in Short and
explored, in which, previous to feature selection, we con-
LongVideos
catenated all the features of the three modalities, then we
For single trial affect (valence and arousal) classification, performedfeatureselectionandtrainedtheclassifierinthe
the features of every modality for each recording session samewayasforthesinglemodalities.

MIRANDA-CORREAETAL:AMIGOS:ADATASETFORMOOD,PERSONALITYANDAFFECTRESEARCHONINDIVIDUALSANDGROUPS 11
| 5.3 Classification |     | of  | Personality, |     | PANAS | and | Social |     |     |     | TABLE7 |     |     |     |     |
| ------------------ | --- | --- | ------------ | --- | ----- | --- | ------ | --- | --- | --- | ------ | --- | --- | --- | --- |
ContextfromShortandLongVideos MeanF1-scores(meanF1-scorefornegativeandpositiveclass)over
participantsforrecognitionofValenceandArousal.Boldvalues
indicatewhethertheF1-scoredistributionoversubjectsissignificantly
5.3.1 SingleModalityClassification
higherthan0.5accordingtoanindependentone-samplet-test
Forpersonalitytraits,PANASandsocialcontextprediction, (p<.01).Analyticalresultsforvotingatrandomareshown.
| 7 scenarios | have | been | tested. The | different |     | scenarios | have |     |     |     |     |     |     |     |     |
| ----------- | ---- | ---- | ----------- | --------- | --- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
been selected to show how the different stimuli as well Short Long All
Modality
as their combination perform in the recognition tasks. The Valence Arousal Valence Arousal Valence Arousal
first 4 scenarios (Video-N1, Video-P1, Video-B1 and Video- EEG 0.576* 0.592** 0.557** 0.571** 0.564** 0.577**
|               |          |     |          |         |     |         |       | GSR |     | 0.531 | 0.548 | 0.528 0.536*   | 0.528   | 0.541** |     |
| ------------- | -------- | --- | -------- | ------- | --- | ------- | ----- | --- | --- | ----- | ----- | -------------- | ------- | ------- | --- |
| U1 scenarios) | consider |     | only the | samples | of  | each of | the 4 |     |     |       |       |                |         |         |     |
|               |          |     |          |         |     |         |       | ECG |     | 0.535 | 0.550 | 0.550** 0.543* | 0.545** | 0.551** |     |
longvideosforprediction.Thefifth(Short-videosscenario) Fusion 0.570* 0.585** 0.551** 0.569** 0.560** 0.564**
| considers | only the     | samples | of the    | 16 short  | videos | together.   |     |        |     |       |       |             |       |       |     |
| --------- | ------------ | ------- | --------- | --------- | ------ | ----------- | --- | ------ | --- | ----- | ----- | ----------- | ----- | ----- | --- |
|           |              |         |           |           |        |             |     | Random |     | 0.500 | 0.500 | 0.500 0.500 | 0.500 | 0.500 |     |
| The sixth | (Long-videos |         | scenario) | considers | all    | the samples |     |        |     |       |       |             |       |       |     |
of the 4 long videos together. And the seventh (All-videos Following [52], a meta-classification of class labels (M-
scenario) considers the samples of all the 20 videos (short CLASS) was implemented in which a linear SVM classifier
and long). The concatenation of the features of all the sam- is trained over the probabilistic outputs of the training
plesofeachscenarioandeachofthemodalities(EEG,ECG samplesandthetraininglabels.Thetrainedclassifieristhen
andGSR),wereassociatedtothelabelsofpersonalitytraits, usedtopredictthelabelofthetestsample.
| PA, NA | and social | context | dimensions. |     | The | dimensionality |     |     |     |     |     |     |     |     |     |
| ------ | ---------- | ------- | ----------- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ofthefeaturevectorofeachscenarioisdifferent,forinstance
|     |     |     |     |     |     |     |     | 5.4 ResultsandDiscussion |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- |
theVideoN1scenariowiththeEEGmodalityhasafeature
vector with dimensionality of 7560 features (72 samples × In Table 7, the mean F1-scores (mean F1-score for both
105features)foreachparticipant. classes)overallparticipants,forclassificationofvalenceand
For each scenario and participant, 8 support vector ma- arousal, using the Gaussian Na¨ıve Bayes classifier, are pre-
|     |     |     |     |     |     |     |     | sented for | the different |     | modalities. | Three | scenarios |     | are in- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | --- | ----------- | ----- | --------- | --- | ------- |
chine(SVM)classifierswithlinearkernel[49]weretrained,
one for each of the 5 personality traits, 2 for mood dimen- cluded,thefirstconsidersonlytheshortvideosexperiment
sionsofPAandNAand1forsocialcontextprediction.The samples, the second the long videos experiment samples
labels for personality and mood dimensions are divided andthethirdallthesamplesofbothexperiments.Resultsfor
into high and low classes using the median value of each featurelevelfusionofthethreemodalitiesarealsoincluded.
personality and mood dimensions as threshold. In the case Randombaselineresults(analyticallydetermined)obtained
ofsocialcontext,iftheparticipantwasinagroupduringthe byassigninglabelsrandomlyarealsoincluded.
|             |            |     |        |            |     |          |       | Random | levels | for | all | the scenarios | for | valence | and |
| ----------- | ---------- | --- | ------ | ---------- | --- | -------- | ----- | ------ | ------ | --- | --- | ------------- | --- | ------- | --- |
| long videos | experiment |     | it was | considered | as  | positive | class |        |        |     |     |               |     |         |     |
andnegativeifitwasinindividualconfiguration.Notethat arousalhad0.5meanF1-scoreeach.Significanthigherthan
socialcontextpredictionwasnotimplementedfortheShort- chance(p < .01accordingtoanindependentone-samplet-
test)F1-scoreswereobtainedforallthescenariosusingthe
videosscenariosimplybecauseitisnotapplicable.
To test the method we use leave-one-participant-out EEG modality, for the long videos and all videos scenarios
cross-validation, in which, during training, principal com- using ECG, and only for arousal recognition in the long
|         |          |       |         |           |      |              |     | videos and | all | videos | scenarios | using | GSR. | In  | general, |
| ------- | -------- | ----- | ------- | --------- | ---- | ------------ | --- | ---------- | --- | ------ | --------- | ----- | ---- | --- | -------- |
| ponents | analysis | (PCA) | [50] is | performed | over | the features |     |            |     |        |           |       |      |     |          |
of all the participants resulting in a reduction to 36 PCA arousal recognition got higher performance than valence,
channels. Next, inspired by [51], channels were selected by except for ECG modality in the long videos experiment.
|            |            |     |         |             |             |     | (ρ) | For all scenarios |     | of valence |     | and arousal | recognition, |     | EEG |
| ---------- | ---------- | --- | ------- | ----------- | ----------- | --- | --- | ----------------- | --- | ---------- | --- | ----------- | ------------ | --- | --- |
| clustering | them using |     | Pearson | correlation | coefficient |     | as  |                   |     |            |     |             |              |     |     |
distancemeasure.ThisisdonebyrankingthePCAchannels got significantly higher performance than ECG and GSR
according to their Fisher’s linear discriminant J calculated (p < 0.0001 for both), resulting in a mean improvement,
overthethreescenarios,of2.2%and3.2%forrecognitionof
| for the | training | set over | each | channel | with | respect | to the |     |     |     |     |     |     |     |     |
| ------- | -------- | -------- | ---- | ------- | ---- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
valenceandarousalovertheECG.ECGisstillsignificantly
| labels. | Channels | with | J < 0.1 | are | discarded. | Next, | the |     |     |     |     |     |     |     |     |
| ------- | -------- | ---- | ------- | --- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
channel with the highest J is selected. By calculating the ρ better(p<0.05)thantheGSRmodality.Featurelevelfusion
coefficient between the selected channel and the remaining does not improve the results but they are still significantly
|           |           |          |     |             |     |               |     | higher than | chance | (p  | < 0.01). | Prediction |     | of valence | and |
| --------- | --------- | -------- | --- | ----------- | --- | ------------- | --- | ----------- | ------ | --- | -------- | ---------- | --- | ---------- | --- |
| channels, | redundant | channels |     | are removed |     | by discarding |     |             |        |     |          |            |     |            |     |
channels with ρ > 0.5. From the remaining channels the arousal in short videos was better than in the long videos
one with the highest J is then selected and the process but the differences are not significant (p = 0.32 for valence
andp=0.19forarousal).Resultsforrecognitionofvalence
| is continued | until | all | the channels | are | either | selected | or  |     |     |     |     |     |     |     |     |
| ------------ | ----- | --- | ------------ | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
discarded. With the selected PCA channels, an SVM with and arousal using the videos of both experiments are not
linearkernelistrainedoverthetrainingsetandtestedover better than for each experiment alone. Our baseline results
|          |          |                |     |           | C   |        |        | showaverageperformancecomparedwiththeliteraturefor |     |     |     |     |     |     |     |
| -------- | -------- | -------------- | --- | --------- | --- | ------ | ------ | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| the test | set. The | regularization |     | parameter |     | of the | linear |                                                    |     |     |     |     |     |     |     |
SVMwasempiricallysetto0.25. recognitionofvalenceandarousal[1],[3],[6].
InTable8,themeanF1-scoreofthepositiveandnegative
|     |     |     |     |     |     |     |     | classes over | all | participants |     | for binary | classification |     | of per- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------ | --- | ---------- | -------------- | --- | ------- |
5.3.2 FusionofModalities
sonalitytraits,PANASandsocialcontextispresented.Inthe
In order to use complementary information from different table,thesevenscenariosdescribedinSec.5.3.1areincluded.
modalities, decision level fusion of the three modalities We have also implemented the baseline method proposed
(EEG, ECG and GSR) was implemented for each scenario. by Abadi et al [11], based on a linear regression model for

| 12  |     |        |     |     |     |     |     | IEEETRANSACTIONSONAFFECTIVECOMPUTING,VOL.?,NO.?,?? |     |     |        |     |     |     |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | ------ | --- | --- | --- | --- |
|     |     | TABLE8 |     |     |     |     |     |                                                    |     |     | TABLE9 |     |     |     |     |
MeanF1-score(meanF1-scorefornegativeandpositiveclass)over MeanF1-score(meanF1-scorefornegativeandpositiveclass)over
participants,forpersonalitytraits(Extraversion,Agreeableness, participants,forrecognitionofpersonalitytraits,PANASandsocial
Conscientiousness,EmotionalStabilityandOpenness),PANAS(PA context,forfusionofmodalities(See5.3.2).Boldvaluesindicate
andNA)andsocialcontextrecognition(numberof20-ssegments whethertheF1-scoredistributionoversubjectsissignificantlyhigher
statedinparenthesis).BoldvaluesindicatewhethertheF1-score than0.5accordingtoanindependentone-samplet-test(p<.001).The
distributionoversubjectsissignificantlyhigherthan0.5accordingtoan bestperformingsinglemodalityisalsoincluded.
independentone-samplet-test(p<.001).Resultsobtainedwitha
baselinemethod[11],forpredictionofpersonalityandPANASusing
theshortvideosexperimentareincludedforcomparison.Empirical Scenario Fusion Extr. Agre. Cons. Emot. Open. PA. NA. S.C.
resultsforvotingatrandomarealsoshown. M-CLASS 0.431 0.485 0.513 0.539 0.377 0.431 0.178 0.510
VideoN1
|             |          |             |             |             |         |       |         | Bestsinglemodality |         | 0.675 | 0.699 0.728 | 0.595 | 0.621 | 0.567 0.327 | 0.644 |
| ----------- | -------- | ----------- | ----------- | ----------- | ------- | ----- | ------- | ------------------ | ------- | ----- | ----------- | ----- | ----- | ----------- | ----- |
|             |          |             |             |             |         |       |         |                    | M-CLASS | 0.431 | 0.135 0.510 | 0.432 | 0.675 | 0.621 0.699 | 0.431 |
| Scenario    | Modality | Extr. Agre. | Cons. Emot. | Open.       | PA. NA. | S.C.  | VideoP1 |                    |         |       |             |       |       |             |       |
|             |          |             |             |             |         |       |         | Bestsinglemodality |         | 0.590 | 0.405 0.649 | 0.619 | 0.756 | 0.648 0.648 | 0.648 |
|             | EEG      | 0.535 0.459 | 0.728 0.595 | 0.426 0.567 | 0.234   | 0.401 |         |                    |         |       |             |       |       |             |       |
|             |          |             |             |             |         |       |         |                    | M-CLASS | 0.535 | 0.728 0.674 | 0.695 | 0.405 | 0.324 0.552 | 0.426 |
| VideoN1(72) | GSR      | 0.675 0.699 | 0.284 0.405 | 0.459 0.431 | 0.327   | 0.644 | VideoB1 |                    |         |       |             |       |       |             |       |
|             |          |             |             |             |         |       |         | Bestsinglemodality |         | 0.675 | 0.730 0.728 | 0.837 | 0.648 | 0.593 0.745 | 0.539 |
|             | ECG      | 0.401 0.351 | 0.702 0.593 | 0.621 0.322 | 0.316   | 0.383 |         |                    |         |       |             |       |       |             |       |
|             |          |             |             |             |         |       |         |                    | M-CLASS | 0.162 | 0.459 0.584 | 0.730 | 0.322 | 0.615 0.770 | 0.348 |
|             | EEG      | 0.590 0.262 | 0.271 0.378 | 0.621 0.648 | 0.584   | 0.648 | VideoU1 |                    |         |       |             |       |       |             |       |
|             |          |             |             |             |         |       |         | Bestsinglemodality |         | 0.431 | 0.675 0.750 | 0.730 | 0.560 | 0.565 0.750 | 0.560 |
| VideoP1(58) | GSR      | 0.485 0.162 | 0.649 0.405 | 0.756 0.401 | 0.648   | 0.405 |         |                    |         |       |             |       |       |             |       |
ECG 0.431 0.405 0.619 0.619 0.431 0.648 0.584 0.405 M-CLASS 0.649 0.459 0.560 0.405 0.567 0.362 0.540 -
Short
|     |     |             |             |             |       |       |     | Bestsinglemodality |     | 0.730 | 0.513 0.655 | 0.567 | 0.699 | 0.565 0.598 | -   |
| --- | --- | ----------- | ----------- | ----------- | ----- | ----- | --- | ------------------ | --- | ----- | ----------- | ----- | ----- | ----------- | --- |
|     | EEG | 0.675 0.619 | 0.644 0.324 | 0.135 0.401 | 0.745 | 0.449 |     |                    |     |       |             |       |       |             |     |
VideoB1(72) GSR 0.316 0.730 0.728 0.473 0.648 0.322 0.251 0.539 M-CLASS 0.648 0.510 0.268 0.513 0.535 0.449 0.699 0.725
Long
ECG 0.552 0.595 0.584 0.837 0.480 0.593 0.670 0.439 Bestsinglemodality 0.756 0.674 0.539 0.567 0.782 0.485 0.619 0.835
EEG 0.080 0.432 0.495 0.619 0.105 0.565 0.750 0.348 M-CLASS 0.297 0.703 0.401 0.459 0.417 0.644 0.446 0.648
All
VideoU1(44) GSR 0.431 0.675 0.348 0.730 0.560 0.485 0.598 0.401 Bestsinglemodality 0.485 0.837 0.535 0.621 0.648 0.674 0.590 0.728
|     | ECG | 0.189 0.378 | 0.750 0.504 | 0.316 0.560 | 0.644 | 0.560 |     |     |     |     |     |     |     |     |     |
| --- | --- | ----------- | ----------- | ----------- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
EEG 0.730 0.351 0.347 0.567 0.486 0.565 0.598 - outperforms [11] in prediction of extroversion, emotional
Short(94) GSR 0.268 0.510 0.655 0.362 0.699 0.238 0.461 - stability, PA and NA. It is interesting to note that both
|     | ECG | 0.621 0.513 | 0.590 0.140 | 0.483 0.426 | 0.362 | -     |         |      |         |               |     |     |         |        |      |
| --- | --- | ----------- | ----------- | ----------- | ----- | ----- | ------- | ---- | ------- | ------------- | --- | --- | ------- | ------ | ---- |
|     |     |             |             |             |       |       | methods | seem | to work | complementary |     |     | to each | other. | Both |
|     | EEG | 0.756 0.405 | 0.271 0.539 | 0.378 0.485 | 0.619 | 0.528 |         |      |         |               |     |     |         |        |      |
Long(246) GSR 0.567 0.674 0.539 0.565 0.782 0.485 0.584 0.835 methodsfailtopredictagreeablenessandconscientiousness
ECG 0.619 0.486 0.339 0.567 0.306 0.405 0.288 0.510 fromEEG.Usingphysiologicalsignals(ECGandGSR),our
|     | EEG | 0.135 0.648 | 0.485 0.270 | 0.401 0.674 | 0.405 | 0.456 |     |     |     |     |     |     |     |     |     |
| --- | --- | ----------- | ----------- | ----------- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
methodoutperforms[11]inpredictionofconscientiousness
| All(340)      | GSR     | 0.371 0.837 | 0.535 0.621 | 0.371 0.649 | 0.547 | 0.702 |             |             |            |                  |     |               |             |          |         |
| ------------- | ------- | ----------- | ----------- | ----------- | ----- | ----- | ----------- | ----------- | ---------- | ---------------- | --- | ------------- | ----------- | -------- | ------- |
|               |         |             |             |             |       |       | and         | openness    | using      | the GSR          | and | in prediction |             | of       | consci- |
|               | ECG     | 0.485 0.567 | 0.449 0.189 | 0.648 0.459 | 0.590 | 0.728 |             |             |            |                  |     |               |             |          |         |
|               |         |             |             |             |       |       | entiousness |             | using      | ECG. Considering |     | the           | GSR         | modality | of      |
| [11]Abadietal | EEG     | 0.410 0.480 | 0.500 0.510 | 0.600 0.460 | 0.360 | -     |             |             |            |                  |     |               |             |          |         |
|               |         |             |             |             |       |       | the         | Long-videos | scenarios, |                  | our | method        | outperforms |          | [11]    |
| [11]Abadietal | ECG+GSR | 0.670 0.570 | 0.530 0.640 | 0.500 0.500 | 0.560 | -     |             |             |            |                  |     |               |             |          |         |
Random - 0.500 0.500 0.500 0.500 0.500 0.500 0.500 0.500 in prediction of agreeableness, conscientiousness, openness
andNA.
|     |     |     |     |     |     |     | Table | 9   | presents | the mean | F1-score |     | over all | participants |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | -------- | -------- | -------- | --- | -------- | ------------ | --- |
predictionsusingtwophysiologicalmodalities,namelyEEG
andphysiologicalsignals(ECG+GSR).In[11],theyuseonly for binary classification of personality traits, PANAS and
shortvideosand35participants.Forthesakeofcomparison, socialcontext,forthedecisionlevelfusionschemedescribed
|     |     |     |     |     |     |     | in 5.3.2. | The | same | scenarios | as  | for | the single | modality |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---- | --------- | --- | --- | ---------- | -------- | --- |
weappliedtheirmethodoverthesame37participantsused
in this study in the short videos experiment. Empirically experimentsareincluded.Theresultsofthebestperforming
estimated baseline results obtained by randomly assigning singlemodalitiesforeachscenarioarealsoincluded.
the labels according to the class ratio of the population are We can see from Table 9 that feature level fusion only
alsoreported. outperformed the best single modality in a few cases. The
Random mean F1-score is 0.5 for all the scenarios and difference is only significant for prediction of NA in the
dimensions (personality traits, PANAS and social context). Video-P1 and Long-videos scenarios and for prediction of
Different significant (p < 0.001) F1-scores are observed PA in the Video-U1 scenario. In the remaining cases, the
for all the scenarios. Single long videos (Video-N1, Video- weakest modalities seem to undermine the performance of
P1, Video-B1 and Video-U1 scenarios) show to be relevant the best modality, but still it is possible to predict con-
|                    |              |     |             |         |            |     | scientiousness |     | and | NA in | 5 scenarios. |     | It is | interesting | to  |
| ------------------ | ------------ | --- | ----------- | ------- | ---------- | --- | -------------- | --- | --- | ----- | ------------ | --- | ----- | ----------- | --- |
| for the prediction | of different |     | personality | traits. | Consistent |     |                |     |     |       |              |     |       |             |     |
significantresultsoverthethreemodalitiesareobservedfor note that, though individual long videos do not perform
NA prediction in the Video-P1 and Video-U1 scenarios; for well for social context prediction, using the samples of the
|               |                   |     |     |              |           |     | 4 long | videos | experiment |     | together | (Long-videos |     | scenario) |     |
| ------------- | ----------------- | --- | --- | ------------ | --------- | --- | ------ | ------ | ---------- | --- | -------- | ------------ | --- | --------- | --- |
| agreeableness | and consciousness |     | in  | the Video-B1 | scenario; |     |        |        |            |     |          |              |     |           |     |
0.725.
and emotional stability in the Video-U1 scenario. When performs relatively well with mean F1-score of The
considering the Short-videos scenario various modalities All-videos scenario which includes samples of both short
andlongvideosdoesnotleadtobetterperformance.
showcontrastingperformance.IntheLong-videosscenario,
consistent significant results are obtained for extroversion, Webelievethattheseresultscanbeimprovedbytheuse
emotional stability and social context. In this scenario, the of different feature extraction and selection methods, such
|              |           |      |             |     |         |     | as deep | belief | networks. |     | We encourage |     | researchers |     | to try |
| ------------ | --------- | ---- | ----------- | --- | ------- | --- | ------- | ------ | --------- | --- | ------------ | --- | ----------- | --- | ------ |
| GSR modality | shows the | best | performance | on  | average | for |         |        |           |     |              |     |             |     |        |
the different dimensions than all other modalities and sce- andusethischallengingdataset.
| narios with | a mean F1-score    |     | of 0.623.       | In the | All-videos  |     |     |             |     |     |     |     |     |     |     |
| ----------- | ------------------ | --- | --------------- | ------ | ----------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| scenario,   | only agreeableness |     | gets consistent |        | performance |     |     |             |     |     |     |     |     |     |     |
|             |                    |     |                 |        |             |     | 6   | CONCLUSIONS |     |     |     |     |     |     |     |
overeachofthemodalities.
In comparison with the baseline method [11], using Inthiswork,wepresentedadatasetformultimodalresearch
only the short videos with the EEG modality, our method of affect, personality traits and mood on individuals and

MIRANDA-CORREAETAL:AMIGOS:ADATASETFORMOOD,PERSONALITYANDAFFECTRESEARCHONINDIVIDUALSANDGROUPS 13
groups by means of neuro-physiological signals. We found [12] J.Wache,R.Subramanian,M.K.Abadi,R.-L.Vieriu,N.Sebe,and
significantcorrelationsbetweeninternalandexternalaffect S. Winkler, “Implicit User-centric Personality Recognition Based
|     |     |     |     |     |     |     |     | on Physiological | Responses | to Emotional |     | Videos,” | in Proc. | of the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --------- | ------------ | --- | -------- | -------- | ------ |
annotationsofvalenceandarousal,indicatingthatexternal
|            |      |                |     |     |               |       |         | ACMICMI. | NewYork,NY,USA:ACM,2015,pp.239–246. |     |     |     |     |     |
| ---------- | ---- | -------------- | --- | --- | ------------- | ----- | ------- | -------- | ----------------------------------- | --- | --- | --- | --- | --- |
| annotation | is a | good predictor |     | of  | the affective | state | of par- |          |                                     |     |     |     |     |     |
[13] R.Plutchik,“TheNatureofEmotions,”AmericanScientist,vol.89,
ticipants. We showed that social context has an important no.4,pp.344+,2001.
[14] P.EkmanandW.Friesen,Unmaskingtheface:Aguidetorecognizing
| effect on | the valence |     | and arousal |     | expressed | by  | the partici- |                          |     |                            |     |     |     |     |
| --------- | ----------- | --- | ----------- | --- | --------- | --- | ------------ | ------------------------ | --- | -------------------------- | --- | --- | --- | --- |
|           |             |     |             |     |           |     |              | emotionsfromfacialclues. |     | Oxford:Prentice-Hall,1975. |     |     |     |     |
pants,giventhatgroupparticipantsshowedlowerlevelsof
[15] J.Russell,“Acircumplexmodelofaffect,”Jrnl.ofPersonalityand
arousalforlowarousalclips,andhigherlevelsofarousalfor
SocialPsychology,vol.39,pp.1161–1178,1980.
higharousalclipsandingeneralhighervalencethanwhen
|     |     |     |     |     |     |     |     | [16] P. Chevalier, | J. C. Martin, | B. Isableu, | and | A. Tapus, | “Impact | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | ------------- | ----------- | --- | --------- | ------- | --- |
theyarealone.PAshowedtobesignificantlycorrelatedwith personality on the recognition of emotion expressed via human,
virtual,androboticembodiments,”inRobotandHumanInteractive
| arousal expressed |     | during | long | videos. |     | EEG was | the best |     |     |     |     |     |     |     |
| ----------------- | --- | ------ | ---- | ------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
Communication(RO-MAN),201524thIEEEInt’lSymposiumon,Aug
modalityforpredictionofvalenceandarousal,whilefeature
2015,pp.229–234.
level fusion did not improve the results. For prediction of [17] G. Matthews, I. Deary, and M. Whiteman, Personality Traits, ser.
personality traits, PANAS and social context, GSR of long PersonalityTraits. CambridgeUniversityPress,2003.
videosisthebestmodalityoveralldimensionswithamean [18] M.PeruginiandL.D.Blas,“Analyzingpersonality-relatedadjec-
F1-scoreof0.623.Finally,featurelevelfusionimprovedthe tives from an etic-emic perspective: The Big Five Marker Scales
(BFMS)andtheItalianAB5Ctaxonomy,”BigFiveAssess.,pp.281–
| results for | NA  | and PA | prediction. |     | The database |     | is publicly | 304,2002. |     |     |     |     |     |     |
| ----------- | --- | ------ | ----------- | --- | ------------ | --- | ----------- | --------- | --- | --- | --- | --- | --- | --- |
available. [19] P. T. Costa and R. R. McCrea, Revised NEO Personality Inventory
|     |     |     |     |     |     |     |     | (NEO PI-R) | and NEO | Five-Factor | Inventory | (NEO-FFI). |     | Odessa, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ----------- | --------- | ---------- | --- | ------- |
Fla.:PsychologicalAssessmentResources,1992.
7 ACKNOWLEDGMENTS [20] D. Watson and A. Tellegen, “Toward a consensual structure of
mood.”Psychologicalbulletin,vol.98,no.2,pp.219–235,Sep.1985.
[21] D.Watson,L.a.Clark,andA.Tellegen,“Developmentandvalida-
| The first | author | acknowledges |     | support |     | from | CONACyT, |     |     |     |     |     |     |     |
| --------- | ------ | ------------ | --- | ------- | --- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- |
tionofbriefmeasuresofpositiveandnegativeaffect:thePANAS
| Mexico, through |     | a scholarship |     | to  | pursue | graduate | studies |     |     |     |     |     |     |     |
| --------------- | --- | ------------- | --- | --- | ------ | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
scales.”JPersSocPsychol,vol.54,no.6,pp.1063–70,Jun.1988.
atQueenMaryUniversityofLondon.
|            |     |     |     |     |     |     |     | [22] D. McDuff,                             | R. Kaliouby,    | T. Senechal, |             | M. Amr, | J. Cohn,  | and  |
| ---------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --------------- | ------------ | ----------- | ------- | --------- | ---- |
|            |     |     |     |     |     |     |     | R. Picard,                                  | “Affectiva-MIT  | Facial       | Expression  | Dataset | (AM-FED): |      |
|            |     |     |     |     |     |     |     | Naturalistic                                | and Spontaneous | Facial       | Expressions |         | Collected | ”In- |
| REFERENCES |     |     |     |     |     |     |     | the-Wild”,”inCVPRWorkshops,2013,pp.881–888. |                 |              |             |         |           |      |
[23] S.Mavadati,M.Mahoor,K.Bartlett,P.Trinh,andJ.Cohn,“Disfa:
[1] S. Koelstra, C. Muehl, M. Soleymani, J. Lee, A. Yazdani, A spontaneous facial action intensity database,” IEEE Trans. on
T.Ebrahimi,T.Pun,A.Nijholt,andI.Patras,“DEAP:Adatabase AffectiveComputing,vol.4,no.2,pp.151–160,2013.
foremotionanalysisusingphysiologicalsignals,”IEEETrans.on
|     |     |     |     |     |     |     |     | [24] S. D. Gosling, | P. J. Rentfrow, | and | W.  | B. Swann, | “A very | brief |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --------------- | --- | --- | --------- | ------- | ----- |
AffectiveComputing,vol.3,no.1,pp.18–31,2012.
measureoftheBig-Fivepersonalitydomains,”Jrnl.ofResearchin
[2] G. Chanel, C. Rebetez, M. Btrancourt, and T. Pun, “Emotion Personality,vol.37,no.6,pp.504–528,Dec.2003.
Assessment From Physiological Signals for Adaptation of Game [25] R. Subramanian, J. Wache, M. Abadi, R. Vieriu, S. Winkler, and
Difficulty.” IEEE Trans. on Systems, Man, and Cybernetics, Part A, N. Sebe, “Ascertain: Emotion and personality recognition using
vol.41,no.6,pp.1052–1063,2011.
commercialsensors,”IEEETrans.onAffectiveComputing,vol.PP,
[3] M.K.Abadi,R.Subramanian,S.M.Kia,P.Avesani,I.Patras,and
no.99,pp.1–1,2016.
N.Sebe,“DECAF:MEG-BasedMultimodalDatabaseforDecod-
|     |     |     |     |     |     |     |     | [26] M. Soleymani, | G. Chanel, | J. J. M. | Kierkels, | and | T. Pun, | Affective |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | ---------- | -------- | --------- | --- | ------- | --------- |
ing Affective Physiological Responses,” IEEE Trans. on Affective CharacterizationofMovieScenesBasedonMultimediaContentAnaly-
Computing,vol.6,no.3,pp.209–222,July2015. sisandUser’sPhysiologicalEmotionalResponses,ser.TenthIEEEInt’l
[4] S.Koelstra,C.Muehl,andI.Patras,“Eeganalysisforimplicittag- SymposiumonMultimediaMultimedia,ISM2008. Instituteof
gingofvideodata,”inAffectiveComputingandIntelligentInteraction
ElectricalandElectronicsEngineers(IEEE),2008,pp.228–235.
| andWorkshops,2009.ACII2009.3rdInt’lConferenceon. |     |     |     |     |     |     | IEEE,2009, |                  |                |     |            |          |     |          |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ---------- | ---------------- | -------------- | --- | ---------- | -------- | --- | -------- |
|                                                  |     |     |     |     |     |     |            | [27] S. Z. Bong, | M. Murugappan, | and | S. Yaacob, | Analysis | of  | Electro- |
pp.1–6.
cardiogram(ECG)SignalsforHumanEmotionalStressClassification.
[5] Z. Zhang, J. M. Girard, Y. Wu, X. Zhang, P. Liu, U. Ciftci, Berlin,Heidelberg:SpringerBerlinHeidelberg,2012,pp.198–205.
S. Canavan, M. Reale, A. Horowitz, H. Yang et al., “Multimodal [28] F.AhmadandO.Olakunle,“Discretewaveletpackettransformfor
| spontaneous |     | emotion  | corpus     | for human |          | behavior | analysis,”  | in                         |                       |         |             |            |        |            |
| ----------- | --- | -------- | ---------- | --------- | -------- | -------- | ----------- | -------------------------- | --------------------- | ------- | ----------- | ---------- | ------ | ---------- |
|             |     |          |            |           |          |          |             | electroencephalogram-based |                       | emotion | recognition |            | in the | valence-   |
| Proceedings | of  | the IEEE | Conference | on        | Computer | Vision   | and Pattern |                            |                       |         |             |            |        |            |
|             |     |          |            |           |          |          |             | arousal                    | space,” in Proceeding | of      | 3rd Int’l   | Conference | on     | Artificial |
Recognition,2016,pp.3438–3446.
IntelligenceandComputerScience2015,2015,pp.122–132.
| [6] M. Soleymani, |     | J. Lichtenauer, |     | T. Pun, | and | M. Pantic, | “A Multi- |     |     |     |     |     |     |     |
| ----------------- | --- | --------------- | --- | ------- | --- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- |
[29] P.J.Lang,M.M.Bradley,andB.N.Cuthbert,“Emotion,attention,
modalDatabaseforAffectRecognitionandImplicitTagging.”T.
AffectiveComputing,vol.3,no.1,pp.42–55,2012. and the startle reflex.” Psychological review, vol. 97, no. 3, p. 377,
1990.
[7] G.McKeown,M.Valstar,R.Cowie,M.Pantic,andM.Schroder,
|      |         |           |     |           |            |     |         | [30] H.Friedman,EncyclopediaofMentalHealth. |     |     |     | ElsevierScience,2015. |     |     |
| ---- | ------- | --------- | --- | --------- | ---------- | --- | ------- | ------------------------------------------- | --- | --- | --- | --------------------- | --- | --- |
| “The | SEMAINE | Database: |     | Annotated | Multimodal |     | Records | of                                          |     |     |     |                       |     |     |
[31] A.R.Damasio,T.J.Grabowski,A.Bechara,H.Damasio,L.L.B.
EmotionallyColoredConversationsbetweenaPersonandaLim-
Ponto,J.Parvizi,andR.D.Hichwa,“Subcorticalandcorticalbrain
itedAgent,”IEEETrans.onAffectiveComputing,vol.3,no.1,pp.
5–17,2012. activity during the feeling of self-generated emotions,” Nature
[8] M. Wilson, “Mrc psycholinguistic database: Machine-usable dic- Neuroscience,vol.3,no.10,pp.1049–1056,102000.
tionary, version 2.00,” Behavior Research Methods, Instruments, & [32] W.Boucsein,ElectrodermalActivity,ser.AdvancesinArchaeologi-
|     |     |     |     |     |     |     |     | calandMuseumScience. |     | PlenumPress,1992. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ----------------- | --- | --- | --- | --- |
Computers,vol.20,no.1,pp.6–10,1988.
[33] N.Nourbakhsh,Y.Wang,F.Chen,andR.A.Calvo,“Usinggal-
[9] M.Kosinski,S.C.Matz,S.D.Gosling,V.Popov,andD.Stillwell,
“Facebook as a research tool for the social sciences: Opportuni- vanicskinresponseforcognitiveloadmeasurementinarithmetic
ties,challenges,ethicalconsiderations,andpracticalguidelines,” andreadingtasks,”inProceedingsofthe24thAustralianComputer-
AmericanPsychologist,vol.70,no.6,pp.543–556,Sep.2015. HumanInteractionConference,ser.OzCHI’12. NewYork,NY,USA:
[10] F.Pianesi,M.Zancanaro,B.Lepri,andA.Cappelletti,“Amulti- ACM,2012,pp.420–423.
modalannotatedcorpusofconsensusdecisionmakingmeetings,” [34] P. J. Lang, M. M. Bradley, and B. N. Cuthbert, “International
LanguageResourcesandEvaluation,vol.41,no.3,pp.409–429,2007. affectivepicturesystem(IAPS):Affectiveratingsofpicturesand
[11] M. Abadi, J. Correa, J. Wache, H. Yang, I. Patras, and N. Sebe, instructionmanual,”UniversityofFlorida,Gainesville,FL,Tech.
| “Inferenceofpersonalitytraitsandaffectschedulebyanalysisof |     |     |     |     |     |     |     | Rep.A-8,2008. |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
spontaneousreactionstoaffectivevideos,”in11thIEEEInt’l.Conf. [35] W. Mou, H. Gunes, and I. Patras, “Alone versus in-a-group: A
onAutomaticFaceandGestureRecog.,vol.1,May2015,pp.1–8. comparativeanalysisoffacialaffectrecognition,”inProceedingsof

14 IEEETRANSACTIONSONAFFECTIVECOMPUTING,VOL.?,NO.?,??
the2016ACMonMultimediaConference,ser.MM’16. NewYork, MojtabaKhomamiAbadiisaPhDcandidateat
NY,USA:ACM,2016,pp.521–525. theDepartmentofInformationEngineeringand
[36] ——, “Automatic recognition of emotions and membership in Computer Science, University of Trento, Italy.
|       |          |        |      |            |             |     |            | Mojtaba is | also the CTO | of Sensaura | Inc., a |
| ----- | -------- | ------ | ---- | ---------- | ----------- | --- | ---------- | ---------- | ------------ | ----------- | ------- |
| group | videos,” | in The | IEEE | Conference | on Computer |     | Vision and |            |              |             |         |
PatternRecognition(CVPR)Workshops,June2016. Canadian startup on real-time and multimodal
[37] R.Buck,J.Losow,M.Murphy,andP.Costanzo,“Socialfacilitation emotion recognition technologies. His research
andinhibitionofemotionalexpressionandcommunication.”Jrnl. interestsinclude:usercentricaffectivecomput-
ofPersonalityandSocialPsych.,vol.63,no.1,pp.962–968,1992. inginhumancomputerinteractionandaffective
multimediaanalysis.
[38] R.McCraeandO.John,“Anintroductiontothefive-factormodel
anditsapplications.”Jrnl.ofpersonality,vol.60,no.2,pp.175–215,
1992.
[39] S.Koelstra,A.Yazdani,M.Soleymani,C.Mu¨hl,J.-L.Lee,A.Ni-
jholt,T.Pun,T.Ebrahimi,andI.Patras,“SingleTrialClassification
| of EEG   | and     | Peripheral | Physiological |          | Signals        | for Recognition | of       |     |     |     |     |
| -------- | ------- | ---------- | ------------- | -------- | -------------- | --------------- | -------- | --- | --- | --- | --- |
| Emotions | Induced | by         | Music         | Videos,” | in Proceedings |                 | on Brain |     |     |     |     |
Informatics.,vol.6334,2010,pp.89–100.
[40] M.SoleymaniandM.Pantic,“Human-centeredimplicittagging:
| Overviewandperspectives.”inSMC. |     |     |     |     | IEEE,2012,pp.3304–3309. |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
[41] J.Morris,“Observations:SAM:TheSelf-AssessmentManikin;An
| Efficient | Cross-Cultural |     | Measurement |     | of Emotional | Response,” |     |     |     |     |     |
| --------- | -------------- | --- | ----------- | --- | ------------ | ---------- | --- | --- | --- | --- | --- |
Jrnl.ofAdvertisingResearch,vol.35,no.8,pp.63–38,1995.
| [42] R. Likert, | A   | Technique       | for the | Measurement |            | of Attitudes, | ser. A |     |     |     |     |
| --------------- | --- | --------------- | ------- | ----------- | ---------- | ------------- | ------ | --- | --- | --- | --- |
| Technique       | for | the Measurement |         | of          | Attitudes. | publisher     | not    |     |     |     |     |
identified,1932,no.nos.136-165.
[43] D.WatsonandL.Clark,“ThePANAS-X:Manualforthepositive
andnegativeaffectschedule-expandedform,”TheUniversityof
Iowa,Tech.Rep.,1999.
NicuSebereceivedthePhDdegreefromLeiden
[44] L. J. Cronbach, “Coefficient alpha and the internal structure of University,TheNetherlands,in2001.Currently,
tests,”Psychometrika,vol.16,no.3,pp.297–334,1951. he is with the Department of Information En-
[45] T.Loughin,“Asystematiccomparisonofmethodsforcombining
|     |     |     |     |     |     |     |     | gineering | and Computer | Science, | University of |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | -------- | ------------- |
p-valuesfromindependenttests,”ComputationalStatisticsandData
|     |     |     |     |     |     |     |     | Trento, Italy, | where he is | leading | the research |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ----------- | ------- | ------------ |
Analysis,vol.47,no.3,pp.467–485,2004.
|     |     |     |     |     |     |     |     | in the areas | of multimedia | information | retrieval |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | ----------- | --------- |
[46] G.Gomez-Herrero,K.Rutanen,andK.Egiazarian,“BlindSource and human behavior understanding. He was a
SeparationbyEntropyRateMinimization,”IEEESignalProcessing generalco-chairofFG2008andACMMultime-
Letters,vol.17,no.2,pp.153–156,Feb2010.
|     |     |     |     |     |     |     |     | dia 2013, | and a program | chair of | CIVR 2007 |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | -------- | --------- |
[47] J.KimandE.Andr,“Emotionrecognitionbasedonphysiological
and2010,andACMMultimedia2007and2011.
| changes | in music | listening,” |     | IEEE Trans. | on Pattern | Analysis | and |     |     |     |     |
| ------- | -------- | ----------- | --- | ----------- | ---------- | -------- | --- | --- | --- | --- | --- |
HeisaprogramchairofECCV2016andICCV
MachineIntelligence,vol.30,no.12,pp.2067–2083,Dec2008. 2017.HeisaseniormemberoftheIEEEandACMandafellowofIAPR.
[48] F.Song,D.Mei,andH.L.,“FeatureSelectionBasedonLinearDis-
| criminant | Analysis,” |     | in Intelligent | System | Design | and Engineering |     |     |     |     |     |
| --------- | ---------- | --- | -------------- | ------ | ------ | --------------- | --- | --- | --- | --- | --- |
Application(ISDEA),2010Int’l.Conf.,vol.1,Oct2010,pp.746–749.
[49] N.CristianiniandJ.Shawe-Taylor,AnIntroductiontoSupportVector
| Machines:AndOtherKernel-basedLearningMethods. |     |     |     |     |     | NewYork,NY, |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
USA:CambridgeUniversityPress,2000.
| [50] I.Jolliffe,PrincipalComponentAnalysis. |                |            |          |               | SpringerVerlag,1986. |            |         |     |     |     |     |
| ------------------------------------------- | -------------- | ---------- | -------- | ------------- | -------------------- | ---------- | ------- | --- | --- | --- | --- |
| [51] J. Bins                                | and B.         | A. Draper, | “Feature | selection     |                      | from huge  | feature |     |     |     |     |
| sets,”                                      | in Proceedings | Eighth     | IEEE     | International |                      | Conference | on Com- |     |     |     |     |
puterVision.ICCV2001,vol.2,2001,pp.159–165vol.2.
[52] S.KoelstraandI.Patras,“FusionoffacialexpressionsandEEGfor
implicitaffectivetagging,”ImageVisionComput.,vol.31,no.2,pp.
164–174,2013.
|     |     |     |     |     |     |     |     | Ioannis Patras | received                  | the PhD         | degree from |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------------------------- | --------------- | ----------- |
|     |     |     |     |     |     |     |     | the Delft      | University of Technology, |                 | The Nether- |
|     |     |     |     |     |     |     |     | lands, in      | 2001. He is a             | senior lecturer | in com-     |
|     |     |     |     |     |     |     |     | puter vision   | in Queen Mary,            | University      | of Lon-     |
don.HewasintheorganizingcommitteeofIEEE
SMC2004,FGR2008,ICMR2011,ACMMM2013
andwasthegeneralchairofWIAMIS2009.His
JuanAbdonMirandaCorreareceivedtheMSc
researchinterestsincludecomputervision,pat-
degreeinelectronicssystemsfromTecnolo´gico
|     |     |     |     |     |     |     |     | tern recognition | and multimodal | HCI. | He is a |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | -------------- | ---- | ------- |
deMonterrey,CampusToluca,Mexico,in2012.
He is now working towards the PhD degree at seniormemberoftheIEEE.
theSchoolofElectronicEngineeringandCom-
|     |     | puter | Science, | Queen    | Mary      | University | of Lon- |     |     |     |     |
| --- | --- | ----- | -------- | -------- | --------- | ---------- | ------- | --- | --- | --- | --- |
|     |     | don,  | UK. His  | research | interests | include:   | multi-  |     |     |     |     |
modalaffectrecognitioninhumancomputerin-
|     |     | teraction, | analysis | of  | social | interaction | in affec- |     |     |     |     |
| --- | --- | ---------- | -------- | --- | ------ | ----------- | --------- | --- | --- | --- | --- |
tivemultimediaanddeeplearning.