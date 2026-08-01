Received8December2022,accepted12January2023,dateofpublication16January2023,dateofcurrentversion24January2023.
DigitalObjectIdentifier10.1109/ACCESS.2023.3237545
Multimodal Hierarchical CNN Feature
Fusion for Stress Detection
RADHIKAKUTTALA 1,RAMANATHANSUBRAMANIAN 2,(SeniorMember,IEEE),
ANDVENKATARAMANAMURTHYORUGANTI 1,(SeniorMember,IEEE)
1DepartmentofElectricalandElectronicsEngineering,AmritaSchoolofEngineering,AmritaVishwaVidyapeetham,Ettimadai,Coimbatore641112,India
2FacultyofScienceandTechnology,UniversityofCanberra,Bruce,Canberra,ACT2617,Australia
Correspondingauthor:VenkataRamanaMurthyOruganti(ovr_murthy@cb.amrita.edu)
ABSTRACT Stressisoneofthemostsevereconcernsinmodernlife.High-levelstresscancreatevarious
diseasesorlossoffocusandproductivityatwork.Beingunderstresspreventspeoplefromrecognizingtheir
stresslevels,soearlystressdetectionisessential.Recently,multimodalfusionhasenhancedtheperformance
ofstressdetectionmodelsusingDeepLearning(DL)techniques.Thelow,mid,andhigh-levelfeaturesof
a Convolutional Neural Network (CNN) are discriminative. A comprehensive feature representation can
be obtained by fusing all three levels of CNN’s features. This study mainly focuses on detecting stress
by exploiting these advantages using a multimodal hierarchical CNN feature fusion. The two multimodal
physiological signals used in this study are Electrodermal activity (EDA) and Electrocardiogram (ECG).
Wedevelopahierarchicalfeaturesetbyconcatenatingmulti-levelCNNfeaturesforeachmodality.Multi-
modalfusiononbothhierarchicalfeaturesetsisperformedusingtheMultimodalTransferModule(MMTM).
Theexperimentsarecarriedoutwithrawfrequencydomaindataandthefeaturesfromthefrequencybands
to study the effectiveness of both. The model’s performance is compared to the different combinations of
hierarchicalfeaturesfromlow,mid,andhighlevels.Toverifythegeneralizability,theproposedapproach
hasbeenevaluatedonfourbenchmarkdatasets-ASCERTAIN,CLAS,MAUS,andWAUC.Theproposed
methodshoweditseffectivenessbyoutperformingexistingmodelsby1-2%,respectively,onfrequencyband
features.Itisobservedthatthehierarchicalfeaturesetfromallthreelevelsperformedbetterthanallother
combinationsby2-4%.Asaresult,thisstrategycanbeausefuladditiontostressdetection.
INDEX TERMS Multimodal, EDA, ECG, CNN, hierarchical feature fusion, stress detection, subject-
independent.
I. INTRODUCTION capabilitiesaresufficienttomeetthechallenge[3].Negative
Stress is a way of responding to overwhelming demands or orchronicstressisthestressthatlastsforalongtimewhen
challengesfromascenariothatmanifestsasemotional,phys- achallengeexceedsanindividual’scapabilities[4].Atsome
ical,orbehaviouralchangesbythehumanbody[1].Theway pointinlife,everyindividualisexposedtoastressfulscenario
anindividualviewsthescenariohasasignificantimpacton and will react accordingly. If an individual can cope with
howstressedtheyare.Whenanindividualfacesachallengein stressfulscenarios,thenexttimeasimilarscenarioarises,the
achievingtheirgoal,theyevaluatethescenariointwostages– individualwon’thaveasmuchofastressfulimpact[5].Sim-
(i)theneedtoachievethedesiredgoaland(ii)theexternaland ilarly, if an individual cannot cope with a stressful situation
internal resources to meet the challenges [2]. Human stress andisrepeatedlyexposedtoasimilarsituation,theindividual
isclassifiedaspositiveandnegative.Positiveoracutestress willdevelopchronicstress[6].Eachtimethebodyencounters
is the stress that lasts for a short time when an individual’s a stressful scenario, the brain triggers the stress response to
visual input from the ears, nose, and eyes. This response is
The associate editor coordinating the review of this manuscript and known as ‘‘fight-or-flight’’ [7]. Instantly, the hypothalamus
approvingitforpublicationwasPaoloCrippa . receives a distress signal from the brain. The hypothalamus
VOLUME11,2023 ThisworkislicensedunderaCreativeCommonsAttribution4.0License.Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ 6867

R.Kuttalaetal.:MultimodalHierarchicalCNNFeatureFusionforStressDetection
is the brain’s command center. The hypothalamus regulates temperature, blood pressure, etc. [24]. For most physio-
involuntary body activities through the Autonomic Nervous logical signal-based stress detection research, ECG and
system(ANS)[8]. EDA signals are widely used either separately or in com-
Duringstress,mostorgansarecontrolledbyANSwithout bination [25]. The ECG signal determines the electrical
human knowledge [9]. The ANS is divided into two main activity of the heart. As the ANS directly affects the
divisions: the Sympathetic Nervous System (SNS) and the heart rate, there will be variations in the heart rate dur-
ParasympatheticNervousSystem(PNS).Thestressresponse ing stress [16]. The EDA signal determines the change
is controlled by the complementary interaction of SNS and in the electrical characteristics of the skin. During stress,
PNS in different physiological conditions [10]. The SNS the body sweats more, which leads to increased skin
initiatesthefightorflightstressresponse,whichresultsina conductance[26].
seriesofchanges,includingphysiological,behavioural,and Aninnovationthatrightawaybenefitssocietyinhealthcare
so on [11]. On the other hand, the PNS plays an essential is the growing application of machine learning (ML), deep
roleinreducingstressresponsesinindividualsbysuppress- learning (DL), and wearable technology [27]. For different
ing the SNS [12]. The initial symptoms that emerge from tasks using physiological signals, ML or DL models are
a stressful scenario are called acute stress reactions [13]. trainedusingbenchmarkphysiologicaldatasets[28].Support
These symptoms are visible within minutes during a stress- Vector Machine (SVM), random forest, K-Nearest Neigh-
ful scenario and settle down quickly. Sweating, difficulty bour,decisiontree,lineardiscriminantanalysis,etc.,arecom-
breathing, palpitations, nausea, chest pain, headaches, etc., monMLmethodsusedforthestudy[29].ML approachesare
arethephysicalsymptomsofacutestressreactions[14].Ifthe frequently employed and get state-of-the-art for most stress
symptomslastlonger,theywillcausechronicstressreactions. detection studies, whereas DL methods are less extensively
Depression,anxiety,memoryloss,heartattack,stroke,high usedbecauseoftheneedforlargedata[30].CNN,Recurrent
blood pressure, cholesterol, ulcer, weight loss, shortness of NeuralNetworks(RNN),LongShortTermMemory(LSTM),
breath, weak immune system, etc., are the long-term health etc.,aretheDLalgorithmscommonlyusedforstressdetec-
effectslinkedtochronicstress[15].Becauseofthenegative tion[31].Recently,multimodalfusionusingtheDLapproach
impacts of stress, it is crucial to build an effective stress wasfoundeffectiveforstressdetection[32].Therearethree
detection system. A timely and accurate diagnosis of stress differentlevelsofmultimodalfusion:early,late,andinterme-
canimproveanindividual’slifeasproductive,healthier,and diate[33].Theearlyfusionmethodmergesfeaturerepresen-
happier[16]. tationsofeachmodalityatthefeaturelevelandstartstraining.
Stress is detected through physiological, psychological, Afterbeingtrainedseparately,thedifferentmodelsareinte-
and behavioural markers [17]. Psychological interactions gratedatthedecisionlevelinthelatefusiontechnique[34].
include increased negative feelings like anger, anxiety, Intermediate fusion begins training by fusing higher-level
depression, etc [18]. Self-report questionnaires or an exam- feature representations of each modality from independent
inationwithapsychologistareusedtoconductapsycholog- modality models [35]. The multimodal fusion model learns
ical assessment of stress. The disadvantage of such assess- the highly linked representation across multiple modalities
mentsisthattheyareonlyperformedoncetheaffectedperson simultaneously, which enhances the model’s performance
or those around them recognize the intensity of the stress, overunimodalapproaches[36].
whichisusuallytoolate[19].Inasshortas24hours,people In the last few years, the popularity of CNN has signifi-
canexperiencememorylapsesregardingtheday’semotional cantlyincreased.CNNextractsthemostdiscriminatingchar-
mood, which lead to inaccurate stress level measurements acteristicsfromthedatawhilelearningfromit.Recentstud-
using self-reports or questionnaires [20]. An individual’s ieshaveproventhatCNNcangeneratestatisticallyrelevant
behaviourisaffectedbystress.Emotionslikeirritation,anger, resultsforvariousapplications[37].Tolinkinputlayerstothe
sadness, etc., are the resulting changes. But they are hard outputlayer,aCNNmodelconsistsofseverallayers,includ-
to measure, as individuals can hide these emotions [21]. ing convolution, pooling, dense, etc. Deep CNN’s several
Physiologicalsignalscanrevealanindividual’sinneraffect’s layerscanencodevariouslow,mid,andhigh-levelfeatures.
strength and quality without any manipulations [12]. These Thedeeplayersareusedtolearnhigh-levelfeatures,andthe
physiological changes are non-voluntary responses that are shallowerlayersareusedtodeterminelow-levelfeatures[38].
difficult to notice externally. Hence, hormone monitoring is Theavailabilityofthemostdiscriminatingfeaturesisoneof
widelyconsideredreliableforassessingstress[22]. themostimportantfactorsforincreasedclassificationaccu-
The physiological aspects have several distinct advan- racy[39].Furthermore,theprobabilityofgettingahighclas-
tages, like reliability, simplicity, continuous readings, sificationaccuracywithjustoneconventionalfeatureextrac-
cost-effectiveness, user-friendliness, non-maskability, non- tionmethodisrelativelylow.Themodel’sperformancecould
invasiveness, etc., which makes them popular among bebetterwithmore information.Researchersalsopointout
researchersforstressdetection[23].Commonphysiological thatinformationlossinthenetworkmayincreaseasthelayers
signals for stress detection are EDA, electroencephalogra- increase[40].Duetothesereasons,inrecentstudies,feature
phy (EEG), ECG, respiration pattern, electromyogram, skin fusionmethodologieslikehierarchicalfeaturesateachlevel
6868 VOLUME11,2023

R.Kuttalaetal.:MultimodalHierarchicalCNNFeatureFusionforStressDetection
areintegratedandusedfortraining.Therelevantinformation Organization:Theremainderofthispaperisorganizedas
can be retained, and information loss is minimized by this follows. Section II examines recent works on hierarchical
hierarchical feature fusion [41]. In most end-to-end CNN feature fusion and the identified research gap. Details of
networks, the last convolution layer’s feature maps, mainly the proposed framework are provided in Section III. The
globalfeatureswithouthierarchyfeatures,serveasdiscrim- experimentresultsarepresentedinSectionIVandcompared
inative features. However, low and mid-level features from with existing works. The paper is concluded in Section V.
theinitiallayershavediscriminativefeatures.Themodelcan We have defined the key terms used in this paper for better
learnmoreefficientquality-awarefeaturerepresentationwith understanding and clarity. The list of abbreviations used in
the help of hierarchical features (low, mid, and high-level thepaperisshowninTable1.
features)[42].
Recent research shows that integrating features are often
TABLE1. Listofabbrevations.
more efficient than independent features. This motivates us
to apply the concept of feature fusion to enhance the effi-
ciency of CNN-based stress detection models. We propose
a multimodal hierarchical CNN feature fusion model that
usescomplementaryfeaturesfromvariouslayerstoenhance
theperformance rateof stressdetection models.To thebest
of our knowledge, the proposed methodology has not yet
been systematically addressed for stress detection. Hence,
this paper presents a multimodal hierarchical CNN feature
fusion model for stress detection using EDA and ECG sig-
nals. Initially, frequency domain features from EDA and
ECGfrequencybandsortherawfrequencydomaindataare
given as input to the CNN model. Inspired by the effec-
tiveness of hierarchical feature fusion on CNN from the
literature’s [38], [39], [40], [41], [42], we concatenate the
high, mid, and low-level features from the convolutional
layers of EDA and ECG separately to form a hierarchical
feature set. Unlike single-level fusion, gradual fusion has
shownbetterperformance[43].So,eachhierarchicalfeature
set is used for multimodal fusion using MMTM (gradual
fusion). Finally, we perform late fusion on the classifica-
tionprobabilitiesofeachmodality.Thisstudyalsoexplores
the performance of the distinct combination of hierarchical II. RELATEDWORKS
features concatenation from the low, mid, and high-level Recently,hierarchicalCNNfeaturefusionmethodswerefre-
features.Theproposedmethodisexaminedonfourstandard quently used in image classification tasks. An overview of
datasets- CLAS [44], ASCERTAIN [45], MAUS [46], and such works and it’s effectiveness is briefly discussed in this
WAUC[47] section.
Thefollowingfourfoldsprovideasummaryofthemajor In order to classify fruit diseases, Akram et al. [38] pro-
contributionsofthisstudy: posed a hierarchical pipeline for deep feature fusion and
1) Multimodal hierarchical CNN feature fusion: The selection.Pre-trained models were used to extract deep fea-
low,mid, andhigh-level featuresfrom theinitialcon- tures,whichwerethenfine-tunedviatransferlearning.Multi-
volutional layers are concatenated separately for each level fusion was performed before feature selection. Fruit
modality, and multimodal fusion is performed on the diseaseswereclassifiedwithMulti-SVMusingtheselected
hierarchicalfeaturesetusingMMTM. features from the plant village dataset [48]. The proposed
2) Combinationsofhierarchicalfeatures:Examinethe method’sefficiencywasrevealedintheclassificationresults
performance of the concatenated distinct combina- in terms of accuracy as 97.8%, sensitivity, G-measure and
tion of hierarchical features from the low, mid, and precisionas97.6%.
high-level. A face recognition algorithm with hierarchical feature
3) Rawdataandfrequencybandfeature: Comparethe fusion was proposed by Zhang et al. [41]. The proposed
effectivenessoftherawfrequencydomaindata,andthe framework learned shallow and deep facial aspects using
featuresfromthefrequencybands. supervisory information. The features are combined to
4) Generalizationability:Toensuregeneralizability,the enhance face recognition efficiency in the face of occlusion
proposed stress detection model has been evaluated and illumination. The visual geometry group network and
on four benchmark datasets- CLAS, ASCERTAIN, lightenedCNNarebothalteredusingthismethod.Thepro-
WAUCandMAUS. posed approach provided significant recognition results in
VOLUME11,2023 6869

R.Kuttalaetal.:MultimodalHierarchicalCNNFeatureFusionforStressDetection
boththeARfacedatabase[49]andthelabelledfacesinthe noted that the suggested model outperforms conventional
wild[50]database. methodsforskin-lesionsegmentationintermsofsegmenta-
Inthewildimages,blindqualityassessmentusinghierar- tionperformance.
chical feature fusion was proposed by Sun et al. [42]. The Li et al. [59] proposed a hierarchical feature aggregation
features from the intermediate layers to the final feature networkfordeepimagecompression.Twoapproaches—inter
representationwerehierarchicallyintegratedusingastaircase and intra-stage feature aggregation—are put forth. Incorpo-
structure. The proposed method allowed the model to fully rating multiscale data into the inter-stage feature aggrega-
use visual data at all levels, from low to high. An iterative tion results in the production of more contextual features.
mixed database training approach was proposed to train the Toenhancerepresentationsofasingleresolution,intra-stage
model simultaneously on multiple datasets. The proposed aggregation joins features from the same stage. According
model benefited from the additional training samples and toextensiveexperiments,theproposedmethodoutperformed
the capacity to learn a more generic feature representation. SOAmethods,showingitseffectiveness.
Experimentswereconductedonsixreal-worldimagequality Forrobustcross-resolutionfacerecognition,arepresenta-
assessmentdatasets,andtheresultsrevealedthattheproposed tionlearningmethodusingahierarchicaldeepCNNfeature
modelperformedsignificantlybetterthanotherstate-of-the- set is proposed by Gao et al. [60]. The proposed approach
artmodels. adaptivelyfusesthecontextualfeaturesfromdifferentlayers
A multiple hierarchical feature fusion for an end-to-end tolearnmorereliableanddiscriminativefeatures.Afeature
steel surface flaw detection is presented by He et al. [51]. set-basedrepresentationlearningtechniquewasdevelopedto
ThedevelopedmethodusesabaselineCNNtoproducefea- collectively describe the hierarchical features for improved
turemapstoattaingoodclassificationabilitiesateachlevel. recognitiontoexploitcontextualinformationeffectively.The
Afeaturefusionnetworkwithmultiplelevelsmergesseveral hierarchicalrecognitionoutputsfromseveralphasesarecom-
hierarchical features into a single feature with more details. bined to enhance recognition performance. Experimental
A region proposal network creates regions of interest based resultsonseveralfacedatasetshaveprovedtheefficiencyof
onthesemultilayerproperties.Thefinaldetectionresultsare theproposedapproach.
generatedforeachROIbyadetectorcomposedofabounding Inlightofthestudiesabove,hierarchicalfeaturefusionand
box regressor and a classifier. A defect detection dataset multimodalfeaturefusioneffectivelyenhancemodelperfor-
called NEU-DET [52] is compiled to evaluate the proposed mance. Recent research on hierarchical CNN feature fusion
method. Using baseline networks, the proposed technique hasalsodemonstratedthesuperiorityoffusionfeaturesover
yields 74.8/82.3 mean average precision on the NEU-DET individualfeatures.However,mosthierarchicalCNNfeature
dataset. fusion-basedexperimentsareconductedonlyonimage-based
A selective feature connection mechanism for concate- tasks, and other modalities have received less attention.
nating CNN features from multiple layers is proposed by This inspired us to propose a multimodal hierarchical CNN
Du et al. [53]. A feature selector created by high-level feature fusion using physiological signals. We aim to take
features links low-level features to high-level features. The advantageofbothhierarchicalfeaturefusionandmultimodal
proposed method shows universal acceptance, superiority, featurefusion.Weintendtobenefitfromthecomplementarity
and efficacy on various challenging computer vision tasks. betweenhigh-levelandlow-levelfeaturesthroughhierarchi-
Maetal.[54]proposedamulti-layerfeaturefusiononCNN calfeaturefusion.Byimplementingmultimodalfusionatthe
to classify satellite image scenes. Since combining feature intermediate level, we intend to enhance the efficiency of
mapsofvariousscalesisnotpractical,theproposedmethod thestressdetectionmodel.Hence,weproposeahierarchical
firsttransformseachfeaturemaptofititsdimensions.Instead CNNfeaturefusionforstressdetectionusingEDAandECG
of just the final convolution layer, two methods for fusion signals.
werecreatedtocombinefeaturemapsofvariouslayers,and
these features were given to the next layer or a classifier. III. METHODOLOGY
Empirical findings showed that the proposed methods per- Figure 1 depicts the novelty of this study on hierarchical
formefficientlyonpublicdatasets. featurefusion.Figure1-(a)showsthetraditionalend-to-end
A multiscale and hierarchical feature aggregation net- deep learning approach. Features from the very last layer
work is proposed for segmenting medical images by areonlyusedastheidentificationfeatureinend-to-endnet-
Yamanakkanavaretal.[55].Twomodulesforfeatureaggre- works. These features are frequently more general features
gation are used to effectively combine data across end-to- withoutusinghierarchicalfeatures.Forthisreason,webuilta
endnetworklayers:HierarchicalFeatureAggregation(HFA) hierarchicalfeaturelearningmodelforstressdetectionusing
andMultiscaleFeatureAggregation(MFA).Tolearndeeper physiologicalsignals.AsshowninFigure1-(b),wecombined
fusionsofthefeaturehierarchy,theHFAmoduleblendsthe deep and shallow features to suit a hierarchical feature set.
features iteratively and hierarchically, and the MFA module Later, these hierarchical features are used for multimodal
graduallyaccumulatesfeaturesandenrichesfeaturerepresen- fusion.Wefirstdescribethedatasetsusedforthisstudyinthe
tation.Havinga0.97averageaccuracyscoreontheUFBA- followingsubsections.Inthefollowingsubsections,wefirst
UESC, PH2, and ISIC-2018 datasets [56], [57], [58], it is give details about the datasets used for this study. Then we
6870 VOLUME11,2023

R.Kuttalaetal.:MultimodalHierarchicalCNNFeatureFusionforStressDetection
FIGURE1. Traditionalandproposeddeeplearningtechniquesaredepictedin(a)and(b),respectively.
go into detail about multimodal hierarchical CNN feature N-thnumberbeforethestimulationnumber,thesubjectwas
fusion’sarchitectureandfeatureextraction. asked to reply by touching the space bar on the computer
|     |     |     |     |     |     | keypad. | After a | short rest | period, | the N-back |     | task with six |
| --- | --- | --- | --- | --- | --- | ------- | ------- | ---------- | ------- | ---------- | --- | ------------- |
A. DATASETDETAILS testing cases was completed. The complexity of the task
This research makes use of the following four bench- servesasthegroundtruth[46].
| mark datasets-ASCERTAIN |     | [45], CLAS | [44], | MAUS | [46], |     |     |     |     |     |     |     |
| ----------------------- | --- | ---------- | ----- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- |
WAUC[47],whichcontainmultimodalphysiologicalsignals
|     |     |     |     |     |     | 4) WAUC |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
suchasECGandEDA.Adetailedexplanationofeachdataset
|     |     |     |     |     |     | The study | included | 48 subjects | who | did | activities | at three |
| --- | --- | --- | --- | --- | --- | --------- | -------- | ----------- | --- | --- | ---------- | -------- |
isgivenbelow.
differentlevelsofexercise.Thespeedofanon-rotatingcycle
orrowingmachinewaschangedtomanipulatephysiological
1) ASCERTAIN tasks.Duringtheexercise,sensorysignalswerecaptured.The
| The dataset | contains | 58 subjects physiological |     | signals | and |     |     |     |     |     |     |     |
| ----------- | -------- | ------------------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
subject’sresponsestotheNASATaskLoadIndexquestion-
face activity recordings. The physiological signals of the naire were encoded into binary values. They are classified
| subjects | were captured | while they watched |     | emotional | video |         |        |           |            |     |      |            |
| -------- | ------------- | ------------------ | --- | --------- | ----- | ------- | ------ | --------- | ---------- | --- | ---- | ---------- |
|          |               |                    |     |           |       | as high | or low | cognitive | load using | the | mean | score as a |
clips.Emotionalvideoclipsof36from[61]wereusedinthe
|     |     |     |     |     |     | cutoff provided |     | in the dataset. | After | removing |     | those sub- |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --------------- | ----- | -------- | --- | ---------- |
study.Basedonthepreviousstudiesofstressdetectionusing jects that didn’t have all the information, we were left with
theASCERTAINdataset[62],wealsousedsubjectiveratings
45subjects[47].
ofvalenceandarousalforstresslabelling.Inthe2-Dvalence To increase the sample count, each signal (EDA/ECG) is
| arousal | plane, high | arousal values along | with | low | valence |     |     |     |     |     |     |     |
| ------- | ----------- | -------------------- | ---- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
splitintofive-secondsegments.SubjectIDswereestablished
valuesareconsideredstressedandothersasunstressed[63]. fortrainingandtestingtoensuresubjectindependence.The
The average of the valence and arousal scores are used to first36,18,43and42subjectsamplesfromWAUC,MAUS,
decidewhetherit’shighorlow[45].
|     |     |     |     |     |     | CLAS and  | ASCERTAIN | datasets |     | are used | for | training. The |
| --- | --- | --- | --- | --- | --- | --------- | --------- | -------- | --- | -------- | --- | ------------- |
|     |     |     |     |     |     | remaining | 9 WAUC,   | 4 MAUS   | and | 16 CLAS  | and | ASCER-        |
2) CLAS
TAINsubjectsamplesareemployedforthetesting.
The dataset contains 62 subjects’ physiological data. Emo- The class imbalance affects the CLAS, ASCERTAIN,
tional video clips were used to evoke the subject’s physio- WAUC,andMAUSdatasets.Real-worlddatasetsfrequently
logical signals. Emotional video clips of 16 from [64] were have a class imbalance when one class has fewer samples
used in the study. After removing those subjects that didn’t than the other class [65]. For more than two decades, this
haveallthedata,wewereleftwith59subjects.Stresslabels
|     |     |     |     |     |     | has been | a topic | of interest. | To  | solve | this problem, | con- |
| --- | --- | --- | --- | --- | --- | -------- | ------- | ------------ | --- | ----- | ------------- | ---- |
havebeen fixedusingthestimulus annotationsdescribedin tinuous enhancement is carried out at the data level, algo-
thedataset[44]. rithmic level, and through hybrid methods [66]. Sampling
|         |     |     |     |     |     | techniques                                           | have | received | more attention |     | in the | data-level |
| ------- | --- | --- | --- | --- | --- | ---------------------------------------------------- | ---- | -------- | -------------- | --- | ------ | ---------- |
| 3) MAUS |     |     |     |     |     | approachtoenhanceclassificationperformance.Undersam- |      |          |                |     |        |            |
The dataset has recorded physiological data under differ- plingandoversamplingaretwocategoriesofsamplingmeth-
ent cognitive circumstances. The N-back task was used on ods[67].Sinceoversamplingcreatesadditionalsamplesfrom
22 participants to generate a cognitive load. At the start of the minority class to compensate for the lack of samples,
the trial, there was a five-minute rest interval. The N-back it is the most effective technique among these [68]. One
taskrequiredtheparticipanttorecallthelastNsinglenumber of the most popular techniques in the literature to generate
fromrapidlydisplayeddigits.Wheneverasignalmatchedthe these new samples is the Synthetic Minority over-sampling
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     |     |     | 6871 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |

R.Kuttalaetal.:MultimodalHierarchicalCNNFeatureFusionforStressDetection
Technique(SMOTE)[69],[70],[71].It’sbasedonthesimple features (low, mid and high-level) from the convolutional
generation of data points on the line segment joining a ran- layers.Ineachmodality,hierarchicalfeaturesfromdifferent
domlychosendatapoint,andoneofitsK-nearestneighbours levelsofconvolutionallayersareconcatenatedandgivenas
was used to sample data from the minority class [72]. This input to MMTM [43] for multimodal fusion. Multimodal
strategy is widely used since it is pretty simple and works feature information is combined, and the features are recal-
incredibly well in reality [73], [74]. We also used SMOTE ibratedusingMMTM.MMTMmakesadvantageofthecom-
to train data in line with the literature to address the class putationallyefficientandlight-weightsqueezeandexcitation
imbalance. block[33].AjointrepresentationisgeneratedintheMMTM
|     |     |     |     |     |     |     | module | by combining | ECG | and | EDA | hierarchical | features. |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | --- | --- | --- | ------------ | --------- | --- |
B. FEATUREEXTRACTION Thejointrepresentationisusedtopredicttheexcitationsig-
Thefollowingsubsectionsexplainthefrequencydomainfea- nals,asexplainedin[43].Fortheexcitation,twoindependent,
fullyconnectedlayersareusedforeachmodality.Onefully
| tures of | EDA and | ECG | on raw | data | and in the | frequency |     |     |     |     |     |     |     |     |
| -------- | ------- | --- | ------ | ---- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
bands. connected layer uses ReLU activation, while the other uses
sigmoidactivation.Theexcitationoutputismultipliedbythe
1) RAWDATA originalfeaturesofeachmodality,whichwegaveasinputto
| TheDiscreteCosineTransform(DCT)convertstherawEDA |     |     |     |     |     |     | themodule. |     |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Fourconvolutionlayersconsistoffilters32,64,128,and
| and ECG | dataset | to the | frequency | domain. | Using | the DCT |     |     |     |     |     |     |     |     |
| ------- | ------- | ------ | --------- | ------- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
256with3×3askernelsizeandReLuasactivationfunction.
| method,           | a signal | can     | be broken | down   | into      | essential fre- |         |               |                   |     |         |           |              |     |
| ----------------- | -------- | ------- | --------- | ------ | --------- | -------------- | ------- | ------------- | ----------------- | --- | ------- | --------- | ------------ | --- |
|                   |          |         |           |        |           |                | Batch   | Normalisation | (BN)              | and | Max     | Pool (MP) | layers       | are |
| quency components |          | [75].   | The       | input  | signal is | more specifi-  |         |               |                   |     |         |           |              |     |
|                   |          |         |           |        |           |                | applied | after         | the convolutional |     | layers. | The       | architecture | is  |
| cally encoded     | in       | the DCT | as a      | linear | sequence  | of weighted    |         |               |                   |     |         |           |              |     |
basisfunctionsconnectedtoitsfrequencyelements.TheDCT completed by fully connected FC1 and FC2 and a sigmoid
|     |     |     |     |     |     |     | output | layer. | The Adam | optimizer | is  | used | for the | model |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------ | -------- | --------- | --- | ---- | ------- | ----- |
isgivenasinputtothemodel.
training,withthedefaultlearningrateandabatchsizeof64.
|     |     |     |     |     |     |     | Asthelossfunction,BinaryCross-Entropyisused.An |     |     |     |     |     |     | early- |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | ------ |
2) FREQUENCYBANDFEATURES
|          |          |          |     |             |     |              | stopping | strategy | is used | to shorten |     | the training | period | if  |
| -------- | -------- | -------- | --- | ----------- | --- | ------------ | -------- | -------- | ------- | ---------- | --- | ------------ | ------ | --- |
| Based on | previous | research |     | [76], [77], | we  | have identi- |          |          |         |            |     |              |        |     |
fied three main bands in the frequency spectrum for ECG, after 30 epochs in a sequence the loss does not decrease.
|     |     |     |     |     |     |     | The maximum |     | classification | probabilities |     | from | each | model |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------------- | ------------- | --- | ---- | ---- | ----- |
asfollows:
areusedtoperformthelatefusion.
1) 0.0–0.04HzVery-low-frequencyband
|     |     |     |     |     |     |     | Based | on  | our previous | study | [82], | we perform | a   | multi- |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | ------------ | ----- | ----- | ---------- | --- | ------ |
2) 0.04–0.15HzLow-frequencyband
|     |     |     |     |     |     |     | modal | hierarchical | feature | fusion | on  | the highest | performed |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------------ | ------- | ------ | --- | ----------- | --------- | --- |
3) 0.15–0.40HzHigh-frequencyband
featurebandofECG((0.15–0.40Hz–High-frequencyband))
Accordingtotheliterature[78],[79],wealsonoticedfive
|     |     |     |     |     |     |     | and EDA | ((0.15–0.25 | Hz–band |     | b). For | the experiments, |     | the |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | ------- | --- | ------- | ---------------- | --- | --- |
mainbandsinthefrequencyspectrumofEDA
architecturefollowsthesameasshowninFigure2excluding
1) 0.05–0.15Hz–banda
themax-poolingandthekernelsizeas2×2.
2) 0.15–0.25Hz–bandb
3) 0.25–0.35Hz–bandc
IV. RESULTSANDDISCUSSION
4) 0.35–0.45Hz–bandd The experimental findings are presented and discussed in
5) 0.45-0.50Hz–bande
|     |     |     |     |     |     |     | this section. |     | We ran | our studies | on  | raw | data and | fre- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------ | ----------- | --- | --- | -------- | ---- |
Thelow-frequencyandhigh-frequencybandsareimpacted quency band features, since we considered their effects.
by ANS activities. Therefore, these bands’ features will be Theproposedmodel’sperformanceisevaluatedusingaccu-
| useful for | stress | detection | [80]. | The | power spectral | density |      |               |          |     |           |     |        |        |
| ---------- | ------ | --------- | ----- | --- | -------------- | ------- | ---- | ------------- | -------- | --- | --------- | --- | ------ | ------ |
|            |        |           |       |     |                |         | racy | and F1-score, | as shown | in  | equations | 1   | and 2. | In our |
oftheHeartRateVariability(HRV)derivedfromeachband first set of experiments, we compared the performance of
| of the ECG | is  | calculated | (using | Welch’s | technique). | The |          |         |           |      |           |         |          |     |
| ---------- | --- | ---------- | ------ | ------- | ----------- | --- | -------- | ------- | --------- | ---- | --------- | ------- | -------- | --- |
|            |     |            |        |         |             |     | raw data | against | frequency | band | features. | Results | obtained |     |
frequency module pyHRV [81] from the Python library is fromdifferentconcatenationcombinationsonASCERTAIN,
used for this purpose. We collected 51 frequency-domain CLAS, MAUS, and WAUC datasets are shown in Table 2.
| measures | from | these PSDs, | including |     | a relative, | absolute, |        |        |                     |     |     |             |     |        |
| -------- | ---- | ----------- | --------- | --- | ----------- | --------- | ------ | ------ | ------------------- | --- | --- | ----------- | --- | ------ |
|          |      |             |           |     |             |           | In our | second | set of experiments, |     | the | performance |     | of the |
peak,andsoon.Thefulllistofmeasuresispresentedin[81]. highest-performing band features of the ECG and EDA on
EachEDA’spowerspectraldensitybandiscalculated(using
|                                                           |     |     |     |     |     |     | the proposed |     | models using | the | WAUC | dataset | is  | shown |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------ | --- | ---- | ------- | --- | ----- |
| Welch’stechnique).Weretrieved40statisticalcharacteristics |     |     |     |     |     |     | inTable3.    |     |              |     |      |         |     |       |
fromthesePSDs(5bandswitheightfeatureseach),including
TP+TN
max, min, standard deviation, variance, skewness, kurtosis, Accuracy= ×100 (1)
|     |     |     |     |     |     |     |     |     | TP+TN |     | +FP+FN |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ------ | --- | --- | --- |
medianandmin.
TP
|     |     |     |     |     |     |     |     | F1score= |     |     |     | ×100 |     | (2) |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | ---- | --- | --- |
TP+1/2(FP+FN)
C. ARCHITECTUREDETAILS
The proposed architecture for stress detection is shown in TP, FP, TN, and FN are True Positive, False Positive, True
Figure 2. Phases 1, 2 and 3 are the different levels of NegativeandFalseNegative.
| 6872 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME11,2023 |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

R.Kuttalaetal.:MultimodalHierarchicalCNNFeatureFusionforStressDetection
FIGURE2. ArchitecturedetailsoftheproposedmultimodalhierarchicalCNNfeaturefusionframework.Ahierarchicalfeaturesetmadeupoflow,
mid,andhigh-levelfeaturesiscreatedandusedasinputtotheMMTMformultimodalfusion.Latefusionisusedtocategorisesubjectsasstressedor
unstressedafterfeaturesarerecalibratedusingMMTM.
A. MULTIMODALHIERARCHICALCNNFEATUREFUSION model is stable and to identify the best hierarchical CNN
Hierarchical feature fusion and multimodal fusion are the featurecombination.Thefeaturesofeachconvolutionallayer
twofundamentalprocessesthatcomposetheproposedmulti- areutilizedintheproposedarchitecturetoextracttheshallow,
modalhierarchicalCNNfeaturefusionmodel.Convolutional intermediate, and deep features. As shown in Table 2 and
layers encode information at various levels using different Table3,first,whencomparingtheperformancefromphase1
layers; for hierarchical feature fusion, we use this concept. tophase1,2and3(concatenationcombinations),weobserve
As shown in Table 2 and Table 3, the result shows the aconsistentincreaseinperformanceasthefeaturesextracted
effectivenessoftheproposedmethodologybecausethecom- from phase 1 to phase 3 are added in sequence to the
plementarity between low-level information and high-level model. Concatenating all level features (phases 1, 2, and 3)
informationiscompletelyutilizedbyourefficienthierarchi- enhanced the model’s overall performance more than other
cal feature fusion method. It also proves that, besides the combinations(phases1,2,and3aloneanditscombinations)
hierarchicalfeaturefusion,themultimodalfusionongradual by12-15%onrawdata,9-15%onbandfeaturesand12.15%
levelanddecisionlevelhelpedtoenhancethemodel’sperfor- onhighestbandfeaturesofECGandEDAonWAUCdataset.
mance by learning across modalities. The promising results This proves that shallow features are also important to end-
suggestthatclinicalpractitionerscanusetheproposedmodel to-end networks, along with deep features, and the features
forstressdetection. extracted from all stages make contributions to enhance the
model’sperformance.
B. DIFFERENTCOMBINATIONSOFHIERARCHICAL
FEATURES C. RAWDATAANDFREQUENCYBANDFEATURES
WeperformedtheproposedmultimodalCNNfeaturefusion We compared the performance of raw data and frequency
on all hierarchical CNN feature fusion combinations. This bandfeaturesontheproposedmodel.Intheoverallstudy,itis
experimentationphaseisessentialtoshowthattheproposed observed that the frequency domain features retrieved from
VOLUME11,2023 6873

R.Kuttalaetal.:MultimodalHierarchicalCNNFeatureFusionforStressDetection
TABLE2. Classificationresults.
TABLE3. ClassificationresultsWAUCdatasetonhighestperformedband modelling. The validity and generalizability of a model
ofECGandEDA. are being given more consideration as the development of
DL-based models continues to advance. In the healthcare
industry, this is particularly important because algorithmic
results directly impact patient treatment and clinical judge-
ment. We proposed a subject-independent multimodal hier-
archical CNN feature fusion stress detection model. Four
benchmark datasets gathered from four separate scenarios
are used to validate and examine the generalizability of the
proposed methodology. As shown in Table 2, the results
theEDAandECGfrequencybandsinfluencedmoreforthe
provethatthepresentedframeworkdoesnotoverfitadataset
performanceenhancementofthemodelmorethanrawdata.
obtainedinaspecificsetting.Inallfourdatasets,weobserved
AsshowninTable2,inallthedatasets,wehaveobservedthe
asimilarperformanceshift.
sameshiftintheperformanceofrawdataandfrequencyband
featuresby2-4%,respectively.Wealsomadeaperformance
comparisononthehighestperformedbandfeaturesofEDA E. T-SNEVISUALIZATION
andECGwiththelatestdataset-WAUC.AsshowninTable3, InDL,wekeepseekingdatainsights;toachievethat,wevisu-
the results were not encouraging compared to the whole alizethedata.Tovisualizetheimpactoftheproposedmodels,
frequency band features. This suggests that features across we qualitatively evaluate the proposed hierarchical fusion
the entire frequency band influence performance enhance- strategy with the network’s feature visualization. This part
mentmorethanthehighest-performingEDAandECGband uses t-distributed stochastic neighbor embedding (tSNE) to
features. assess the network’s visual cognition. Features from the
FC-16 layers of the frequency band of ECG modality are
D. GENERALIZATIONABILITY taken and used for visualization. It is evident from figure 3
Applying DL techniques in the healthcare industry has that the hierarchical features of the ECG following multi-
several benefits, especially when it comes to predictive modal fusion are discriminatory enough to classify stressed
6874 VOLUME11,2023

R.Kuttalaetal.:MultimodalHierarchicalCNNFeatureFusionforStressDetection
FIGURE3. tSNEvisualizationofECGfeaturesfromthefrequencybandofallthedatasets.Here,reddotsindicatethestressclass,andgreendots
indicatetheunstressedclass.Aclearseparationbetweenthetwoclassesisvisibleinallthedatasets.
andunstressed.Wecanseesimilarclustersinallthedatasets. TABLE4. Comparisontostate-of-artfindings.
The plot demonstrates the groups created based on simi-
larity, illustrating the potential capability of the proposed
approachforstressdetection.Thecriticalt-SNEvisualization
map’shighlightedadistinctseparationbetweenstressedand
unstressedconditions.Wehavealsonoticedsimilarclusters
forEDAfrequencybandfeatures.
F. COMPARISONSTUDY
Nowadays, a critical healthcare challenge is the quick and
precise diagnosis of stress. Accurate stress detection is a
challengethathasbeenaddressedusingvarioustechniques.
The traditional DL and ML approaches have shown to be
the most successful. This work mainly focused on detect-
ing stress using physiological signals–ECG and EDA using
DL.WeproposedanefficientmultimodalhierarchicalCNN
feature fusion model for stress detection and compared its
performancewithseveralclassicalMLandDLtechniques.
Thissectionanalyzestheproposedmethod’sfindingswith
those of existing stress detection research using the four
datasets. Table 4 shows a summary of the performance
measures. Only a few studies have used the most recent
datasets,WAUCandMAUS,intheiranalyses.Existingworks
show that the majority of the works are carried on time-
frequency domain [44], [62], [83], [84], [85], [86], [87],
[88], subject dependent [44], [62], [77], [83], [84], [89],
and using machine learning models [44], [62], [83], [84],
[89], [90]. Few researchers used traditional deep learning features. The proposed approach performs better than all
techniques [82], [85], [86], [87], [88]. Compared with the thereportedstate-of-the-artsubject-independentandsubject-
existing works, our work focused on utilizing the full fea- dependentstudies,exceptfortheCLASdataset.Theresults
tures of an end-to-end network, not only on the last layer of our predictions confirm that our multimodal hierarchical
VOLUME11,2023 6875

R.Kuttalaetal.:MultimodalHierarchicalCNNFeatureFusionforStressDetection
featurefusionmodelishighlyeffectivefordetectingstressin [10] J. Suurland, K. B. van der Heijden, S. C. J. Huijbregts,
asubject-independentway. S. H. M. van Goozen, and H. Swaab, ‘‘Infant parasympathetic and
|     |     |     |     |     |     |     | sympathetic | activity | during    | baseline, | stress   | and recovery: | Interactions      |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --------- | --------- | -------- | ------------- | ----------------- | --- |
|     |     |     |     |     |     |     | with        | prenatal | adversity | predict   | physical | aggression    | in toddlerhood,’’ |     |
V. CONCLUSION
J.AbnormalChildPsychol.,vol.46,no.4,pp.755–768,May2018.
This paper presents a multimodal hierarchical CNN feature [11] B.Chu,K.Marwaha,T.Sanvictores,andD.Ayers,‘‘Physiology,stress
reaction,’’inStatPearls[Internet].StatPearlsPublishing,2021.
| fusion for | stress | detection. | EDA | and ECG | signals | raw data |                |            |     |       |          |           |             |      |
| ---------- | ------ | ---------- | --- | ------- | ------- | -------- | -------------- | ---------- | --- | ----- | -------- | --------- | ----------- | ---- |
|            |        |            |     |         |         |          | [12] D. Ayata, | Y. Yaslan, | and | M. E. | Kamasak, | ‘‘Emotion | based music | rec- |
andfrequencydomainfeaturesareusedutilizedinthisstudy.
ommendationsystemusingwearablephysiologicalsensors,’’IEEETrans.
For identification tasks, the convolutional layer’s shallow Consum.Electron.,vol.64,no.2,pp.196–203,May2018.
feature as well as deep feature are useful. We integrate the [13] C. Regehr and V. R. LeBlanc, ‘‘PTSD, acute stress, performance and
decision-makinginemergencyserviceworkers,’’J.Amer.Acad.Psychiatry
featuresoneachphaseoftheend-to-endnetworktoincrease Law,vol.45,no.2,pp.184–192,2017.
efficiency and better utilise the retrieved features in each [14] L.A.Wright,M.Sijbrandij,R.Sinnerton,C.Lewis,N.P.Roberts,and
phase. Low, mid, and high-level features of convolutional J. I. Bisson, ‘‘Pharmacological prevention and early treatment of post-
traumaticstressdisorderandacutestressdisorder:Asystematicreview
layersareconcatenatedtoobtaindifferentcombinations,and
andmeta-analysis,’’Transl.Psychiatry,vol.9,no.1,pp.1–10,Dec.2019.
| multimodal | fusion | is  | conducted | on each | hierarchical | fea- |     |     |     |     |     |     |     |     |
| ---------- | ------ | --- | --------- | ------- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
[15] S.J.Lupien,R.-P.Juster,C.Raymond,andM.-F.Marin,‘‘Theeffectsof
chronicstressonthehumanbrain:Fromneurotoxicity,tovulnerability,to
tureset.Additionally,thecombinationoffeaturescanmore
opportunity,’’FrontiersNeuroendocrinol.,vol.49,pp.91–105,Apr.2018.
| effectively | convey | the | characteristics | of  | the physiological |     |     |     |     |     |     |     |     |     |
| ----------- | ------ | --- | --------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[16] M.Gjoreski,H.Gjoreski,M.Luštrek,andM.Gams,‘‘Continuousstress
| signals. | The proposed |     | approach | is tested | on four | bench- |           |       |         |         |               |          |         |          |
| -------- | ------------ | --- | -------- | --------- | ------- | ------ | --------- | ----- | ------- | ------- | ------------- | -------- | ------- | -------- |
|          |              |     |          |           |         |        | detection | using | a wrist | device: | In laboratory | and real | life,’’ | in Proc. |
mark datasets - ASCERTAIN, CLAS, MAUS and WAUC. ACM Int. Joint Conf. Pervasive Ubiquitous Comput., Adjunct, 2016,
pp.1185–1193.
| Experimental | results | show | that | the proposed | approach | out- |     |     |     |     |     |     |     |     |
| ------------ | ------- | ---- | ---- | ------------ | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
[17] S.S.PanickerandP.Gayathri,‘‘Asurveyofmachinelearningtechniques
performs previous studies in terms of stress detection in a inphysiologybasedmentalstressdetectionsystems,’’Biocybern.Biomed.
subject independent manner. Among the different combina- Eng.,vol.39,no.2,pp.444–469,Apr.2019.
tions, concatenating all the phases (low, mid and high-level [18] E. Turcan, S. Muresan, and K. McKeown, ‘‘Emotion-infused models
|     |     |     |     |     |     |     | for explainable |     | psychological | stress | detection,’’ | in Proc. | Conf. | North |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------------- | ------ | ------------ | -------- | ----- | ----- |
features)yieldsoptimalperformance.Theproposedapproach Amer.ChapterAssoc.Comput.Linguistics:Hum.Lang.Technol.,2021,
to feature fusion is a general one that works well in end-to- pp.2895–2909.
endnetworks.Toenhancetheabilityoffeatureextractionin [19] A.Teilegen,‘‘Structuresofmoodandpersonalityandtheirrelevanceto
assessinganxiety,withanemphasisonself-report,’’inAnxietyandthe
| neural networks, |     | we can | use | the end-to-end | networks | deep, |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------ | --- | -------------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
AnxietyDisorders.Evanston,IL,USA:Routledge,2019,pp.681–706.
| medium | and shallow | features |     | of end-to-end | networks | and |                         |     |     |              |     |                     |     |     |
| ------ | ----------- | -------- | --- | ------------- | -------- | --- | ----------------------- | --- | --- | ------------ | --- | ------------------- | --- | --- |
|        |             |          |     |               |          |     | [20] J. Rodríguez-Arce, |     | L.  | Lara-Flores, | O.  | Portillo-Rodríguez, |     | and |
R.Martínez-Méndez,‘‘Towardsananxietyandstressrecognitionsystem
| perform | feature | integration. |     | Thus, in the | future, | we intend |              |              |     |       |                  |             |     |         |
| ------- | ------- | ------------ | --- | ------------ | ------- | --------- | ------------ | ------------ | --- | ----- | ---------------- | ----------- | --- | ------- |
|         |         |              |     |              |         |           | for academic | environments |     | based | on physiological | features,’’ |     | Comput. |
| to: (i) | expand  | the studies  | on  | hierarchical | feature | fusion    |              |              |     |       |                  |             |     |         |
MethodsProgramsBiomed.,vol.190,Jul.2020,Art.no.105408.
andiidifferentmulti-modalfusiontechniquesonhierarchical
|     |     |     |     |     |     |     | [21] M. Granovetter, |     | ‘‘The sociological |     | and economic | approaches |     | to labor |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ------------------ | --- | ------------ | ---------- | --- | -------- |
features. marketanalysis:Asocialstructuralview,’’inIndustries,Firms,andJobs,
2017,pp.187–216.
[22] Y.S.Can,N.Chalabianloo,D.Ekiz,andC.Ersoy,‘‘Continuousstress
REFERENCES detectionusingwearablesensorsinreallife:Algorithmicprogramming
[1] G.RussellandS.Lightman,‘‘Thehumanstressresponse,’’NatureRev. contestcasestudy,’’Sensors,vol.19,no.8,p.1849,Apr.2019.
Endocrinol.,vol.15,no.9,pp.525–534,2019. [23] L. Shu, J. Xie, M. Yang, Z. Li, Z. Li, D. Liao, X. Xu, and X. Yang,
[2] G.S.EverlyandJ.M.Lating,‘‘Theanatomyandphysiologyofthehuman ‘‘Areviewofemotionrecognitionusingphysiologicalsignals,’’Sensors,
vol.18,no.7,p.2074,2018.
| stressresponse,’’in |     | AClinicalGuidetotheTreatmentoftheHumanStress |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[24] S.PourmohammadiandA.Maleki,‘‘StressdetectionusingECGandEMG
Response.NewYork,NY,USA:Springer,2019,pp.19–56.
[3] N.Rohleder,‘‘Stressandinflammation—Theneedtoaddressthegapin signals:Acomprehensivestudy,’’Comput.MethodsProgramsBiomed.,
thetransitionbetweenacuteandchronicstresseffects,’’Psychoneuroen- vol.193,Sep.2020,Art.no.105482.
docrinology,vol.105,pp.164–171,Jul.2019. [25] P.Zontone,A.Affanni,R.Bernardini,A.Piras,andR.Rinaldo,‘‘Stress
[4] A. P. Cruz, A. Pradeep, K. R. Sivasankar, and K. S. Krishnaveni, detection through electrodermal activity (EDA) and electrocardiogram
(ECG)analysisincardrivers,’’inProc.27thEur.SignalProcess.Conf.
‘‘AdecisiontreeoptimisedSVMmodelforstressdetectionusingbiosig-
nals,’’inProc.Int.Conf.Commun.SignalProcess.(ICCSP),Jul.2020, (EUSIPCO),Sep.2019,pp.1–5.
pp.0841–0845. [26] R.Sánchez-Reolid,M.T.López,andA.Fernández-Caballero,‘‘Machine
[5] S.S.Machiraju,N.Konijeti,A.Batchu,andN.Tata,‘‘Stressdetection learning for stress detection from electrodermal activity: A scoping
| usingadaptivethresholdmethodology,’’inProc.5thInt.Conf.Commun. |     |     |     |     |     |     | review,’’2020. |     |     |     |     |     |     |     |
| -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
Electron.Syst.(ICCES),Jun.2020,pp.889–894. [27] P.BobadeandM.Vani,‘‘Stressdetectionwithmachinelearninganddeep
|     |     |     |     |     |     |     | learning | using | multimodal | physiological | data,’’ | in Proc. | 2nd | Int. Conf. |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ---------- | ------------- | ------- | -------- | --- | ---------- |
[6] K.A.Demin,A.S.Taranov,N.P.Ilyin,A.M.Lakstygal,A.D.Volgin,
M.S.deAbreu,T.Strekalova,andA.V.Kalueff,‘‘Understandingneurobe- InventiveRes.Comput.Appl.(ICIRCA),Jul.2020,pp.51–57.
havioraleffectsofacuteandchronicstressinzebrafish,’’Stress,vol.24, [28] O. Faust, Y. Hagiwara, T. J. Hong, O. S. Lih, and U. R. Acharya,
no.1,pp.1–18,Jan.2021. ‘‘Deep learning for healthcare applications based on physiological sig-
[7] R. McCarty, ‘‘The fight-or-flight response: A cornerstone of stress nals:Areview,’’Comput.MethodsProgramsBiomed.,vol.161,pp.1–13,
Jul.2018.
research,’’inStress:Concepts,Cognition,Emotion,andBehavior.Ams-
terdam,TheNetherlands:Elsevier,2016,pp.33–37. [29] S.ElzeinyandM.Qaraqe,‘‘Machinelearningapproachestoautomatic
[8] A.AgorastosandG.P.Chrousos,‘‘Theneuroendocrinologyofstress:The stressdetection:Areview,’’inProc.IEEE/ACS15thInt.Conf.Comput.
stress-relatedcontinuumofchronicdiseasedevelopment,’’Mol.Psychia- Syst.Appl.(AICCSA),Oct.2018,pp.1–6.
try,vol.27,no.1,pp.502–513,Jan.2022. [30] C.-Y.Liao,R.-C.Chen,andS.-K.Tai,‘‘Emotionstressdetectionusing
[9] L. Becker, H. C. Kaltenegger, D. Nowak, N. Rohleder, and M. Weigl, EEGsignalanddeeplearningtechnologies,’’inProc.IEEEInt.Conf.Appl.
Syst.Invention(ICASI),Apr.2018,pp.90–93.
| ‘‘Differences |     | in stress system | (re-)activity | between | single | and dual-or |     |     |     |     |     |     |     |     |
| ------------- | --- | ---------------- | ------------- | ------- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
multitasking in healthy adults: A systematic review and meta-analysis: [31] L. Shu, J. Xie, M. Yang, Z. Li, Z. Li, D. Liao, X. Xu, and X. Yang,
Physiologicalstressandmultitasking,’’HealthPsychol.Rev.,pp.1–45, ‘‘Areviewofemotionrecognitionusingphysiologicalsignals,’’Sensors,
| 2022. |     |     |     |     |     |     | vol.18,no.7,p.2074,Jun.2018. |     |     |     |     |     |               |     |
| ----- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | ------------- | --- |
| 6876  |     |     |     |     |     |     |                              |     |     |     |     |     | VOLUME11,2023 |     |

R.Kuttalaetal.:MultimodalHierarchicalCNNFeatureFusionforStressDetection
[32] M.N.Rastgoo,B.Nakisa,F.Maire,A.Rakotonirainy,andV.Chandran, [54] C.Ma,X.Mu,andD.Sha,‘‘Multi-layersfeaturefusionofconvolutional
‘‘Automaticdriverstresslevelclassificationusingmultimodaldeeplearn- neuralnetworkforsceneclassificationofremotesensing,’’IEEEAccess,
ing,’’ExpertSyst.Appl.,vol.138,Dec.2019,Art.no.112793. vol.7,pp.121685–121694,2019.
[33] F.Liu,J.Chen,W.Tan,andC.Cai,‘‘Amulti-modalfusionmethodbasedon [55] N.Yamanakkanavar,J.Y.Choi,andB.Lee,‘‘Multiscaleandhierarchical
higher-orderorthogonaliterationdecomposition,’’Entropy,vol.23,no.10, feature-aggregation network for segmenting medical images,’’ Sensors,
p.1349,Oct.2021. vol.22,no.9,p.3440,Apr.2022.
[34] C.I.Patel,S.Garg,T.Zaveri,A.Banerjee,andR.Patel,‘‘Humanaction [56] G.Silva,L.Oliveira,andM.Pithon,‘‘AutomaticsegmentingteethinX-ray
recognitionusingfusionoffeaturesforunconstrainedvideosequences,’’ images:Trends,anoveldataset,benchmarkingandfutureperspectives,’’
Comput.Electr.Eng.,vol.70,pp.284–301,Aug.2018. ExpertSyst.Appl.,vol.107,pp.15–31,Oct.2018.
[35] S.Y.Boulahia,A.Amamra,M.R.Madi,andS.Daikh,‘‘Early,interme- [57] T.Mendonca,M.Celebi,T.Mendonca,andJ.Marques,‘‘Ph2:Apublic
diateandlatefusionstrategiesforrobustdeeplearning-basedmultimodal databasefortheanalysisofdermoscopicimages,’’inDermoscopyImage
actionrecognition,’’Mach.Vis.Appl.,vol.32,no.6,pp.1–18,Nov.2021. Analysis,2015.
[36] J.Aigrain,M.Spodenkiewicz,S.Dubuisson,M.Detyniecki,D.Cohen,and [58] N. Codella, V. Rotemberg, P. Tschandl, M. Emre Celebi, S. Dusza,
M.Chetouani,‘‘Multimodalstressdetectionfrommultipleassessments,’’ D.Gutman,B.Helba,A.Kalloo,K.Liopyris,M.Marchetti,H.Kittler,
IEEETrans.Affect.Comput.,vol.9,no.4,pp.491–506,Oct.2018. andA.Halpern,‘‘Skinlesionanalysistowardmelanomadetection2018:A
challengehostedbytheinternationalskinimagingcollaboration(ISIC),’’
[37] L.K.SinghandM.Khanna,‘‘Anovelmultimodalitybaseddualfusion
2019,arXiv:1902.03368.
integrated approach for efficient and early prediction of glaucoma,’’
Biomed.SignalProcess.Control,vol.73,Mar.2022,Art.no.103468. [59] W.Li,Z.Du,H.He,J.Tang,andG.Wu,‘‘Hierarchicalfeatureaggregation
networkfordeepimagecompression,’’inProc.IEEEInt.Conf.Acoust.,
[38] M.A.Khan,T.Akram,M.Sharif,andT.Saba,‘‘Fruitsdiseasesclassi-
SpeechSignalProcess.(ICASSP),May2022,pp.1875–1879.
fication:Exploitingahierarchicalframeworkfordeepfeaturesfusionand
selection,’’MultimediaToolsAppl.,vol.79,nos.35–36,pp.25763–25783, [60] G.Gao,Y.Yu,J.Yang,G.-J.Qi,andM.Yang,‘‘HierarchicaldeepCNN
Sep.2020. featureset-basedrepresentationlearningforrobustcross-resolutionface
recognition,’’IEEETrans.CircuitsSyst.VideoTechnol.,vol.32,no.5,
[39] M. Abdar, S. Salari, S. Qahremani, H.-K. Lam, F. Karray,
pp.2550–2560,May2022.
S.Hussain,A.Khosravi,U.RajendraAcharya,V.Makarenkov,andS.
[61] M. K. Abadi, R. Subramanian, S. M. Kia, P. Avesani, I. Patras, and
Nahavandi,‘‘UncertaintyFuseNet:Robustuncertainty-awarehierarchical
N.Sebe,‘‘DECAF:MEG-basedmultimodaldatabasefordecodingaffec-
featurefusionmodelwithensembleMonteCarlodropoutforCOVID-19
tivephysiologicalresponses,’’IEEETrans.Affect.Comput.,vol.6,no.3,
detection,’’2021,arXiv:2105.08590.
pp.209–222,Jul.2015.
[40] X. Li, D. Song, and Y. Dong, ‘‘Hierarchical feature fusion network
[62] V. Markova and T. Ganchev, ‘‘Three-step attribute selection for stress
for salient object detection,’’ IEEE Trans. Image Process., vol. 29,
detectionbasedonphysiologicalsignals,’’inProc.IEEEXXVIIInt.Sci.
pp.9165–9175,2020.
Conf.Electron.(ET),Sep.2018,pp.1–4.
[41] J.Zhang,X.Yan,Z.Cheng,andX.Shen,‘‘Afacerecognitionalgorithm
[63] M. Dahmane, J. Alam, P.-L. St-Charles, M. Lalonde, K. Heffner, and
basedonfeaturefusion,’’ConcurrencyComput.,Pract.Exper.,vol.34,
S. Foucher, ‘‘A multimodal non-intrusive stress monitoring from the
no.14,p.e5748,Jun.2022.
pleasure-arousal emotional dimensions,’’ IEEE Trans. Affect. Comput.,
[42] W.Sun,X.Min,G.Zhai,andS.Ma,‘‘Blindqualityassessmentforin-the-
vol.13,no.2,pp.1044–1056,Apr.2022.
Wildimagesviahierarchicalfeaturefusionanditerativemixeddatabase
[64] S.Koelstra,C.Muhl,M.Soleymani,J.-S.Lee,A.Yazdani,T.Ebrahimi,
training,’’2021,arXiv:2105.14550.
T.Pun,A.Nijholt,andI.Patras,‘‘DEAP:Adatabaseforemotionanalysis;
[43] H.R.VaeziJoze,A.Shaban,M.L.Iuzzolino,andK.Koishida,‘‘MMTM:
usingphysiologicalsignals,’’IEEETrans.Affect.Comput.,vol.3,no.1,
MultimodaltransfermoduleforCNNfusion,’’inProc.IEEE/CVFConf.
pp.18–31,Jan./Mar.2011.
Comput.Vis.PatternRecognit.(CVPR),Jun.2020,pp.13289–13299.
[65] J.L.Leevy,T.M.Khoshgoftaar,R.A.Bauder,andN.Seliya,‘‘Asurvey
[44] V.Markova,T.Ganchev,andK.Kalinkov,‘‘CLAS:Adatabaseforcogni- onaddressinghigh-classimbalanceinbigdata,’’J.BigData,vol.5,no.1,
tiveload,affectandstressrecognition,’’inProc.Int.Conf.Biomed.Innov.
pp.1–30,2018.
Appl.(BIA),Nov.2019,pp.1–4.
[66] S.Sharma,A.Gosain,andS.Jain,‘‘Areviewoftheoversamplingtech-
[45] R.Subramanian,J.Wache,M.K.Abadi,R.L.Vieriu,S.Winkler,and niquesinclassimbalanceproblem,’’inProc.Int.Conf.Innov.Comput.
N.Sebe,‘‘ASCERTAIN:Emotionandpersonalityrecognitionusingcom- Commun.Singapore:Springer,2022,pp.459–472.
mercialsensors,’’IEEETrans.Affect.Comput.,vol.9,no.2,pp.147–160,
[67] D. Elreedy and A. F. Atiya, ‘‘A comprehensive analysis of synthetic
Apr./Jun.2018.
minorityoversamplingtechnique(SMOTE)forhandlingclassimbalance,’’
[46] W.-K. Beh, Y.-H. Wu, and A.-Y. Wu, ‘‘MAUS: A dataset for men- Inf.Sci.,vol.505,pp.32–64,Dec.2019.
tal workload assessmenton N-back task using wearable sensor,’’ 2021,
[68] A. Amin, S. Anwar, A. Adnan, M. Nawaz, N. Howard, J. Qadir,
arXiv:2111.02561.
A. Hawalah, and A. Hussain, ‘‘Comparing oversampling techniques to
[47] I.Albuquerque,A.Tiwari,M.Parent,R.Cassani,J.-F.Gagnon,D.Lafond, handletheclassimbalanceproblem:Acustomerchurnpredictioncase
S.Tremblay,andT.H.Falk,‘‘WAUC:Amulti-modaldatabaseformental study,’’IEEEAccess,vol.4,pp.7940–7957,2016.
workloadassessmentunderphysicalactivity,’’FrontiersNeurosci.,vol.14,
[69] N.V.Chawla,K.W.Bowyer,L.O.Hall,andW.P.Kegelmeyer,‘‘Smote:
Dec.2020,Art.no.549524. Syntheticminorityover-samplingtechnique,’’J.Artif.Intell.Res.,vol.16,
[48] D.P.HughesandM.Salathe,‘‘Anopenaccessrepositoryofimageson pp.321–357,Dec.2002.
planthealthtoenablethedevelopmentofmobilediseasediagnostics,’’ [70] N. Noorhalim, A. Ali, and S. M. Shamsuddin, ‘‘Handling imbalanced
2015,arXiv:1511.08060. ratioforclassimbalanceproblemusingSMOTE,’’inProc.3rdInt.Conf.
[49] G.B.Huang,M.Mattar,T.Berg,andE.Learned-Miller,‘‘Labeledfaces Comput.,Math.Statist.(iCMS).Singapore:Springer,2019,pp.19–30.
in the wild: A database forstudying face recognition in Unconstrained [71] V. Rupapara, F. Rustam, H. F. Shahzad, A. Mehmood, I. Ashraf, and
environments,’’inProc.WorkshopFaces‘Real-Life’Images:Detection, G. S. Choi, ‘‘Impact of SMOTE on imbalanced text features for toxic
Alignment,Recognit.,2008,pp.1–15. comments classification using RVVC model,’’ IEEE Access, vol. 9,
[50] A. Martinez and R. Benavente, ‘‘The ar face database: CVC,’’ pp.78621–78634,2021.
Tech.Rep.24,1998. [72] S. Wang, Y. Dai, J. Shen, and J. Xuan, ‘‘Research on expansion and
[51] Y.He,K.Song,Q.Meng,andY.Yan,‘‘Anend-to-endsteelsurfacedefect classificationofimbalanceddatabasedonSMOTEalgorithm,’’Sci.Rep.,
detectionapproachviafusingmultiplehierarchicalfeatures,’’IEEETrans. vol.11,no.1,pp.1–11,Dec.2021.
Instrum.Meas.,vol.69,no.4,pp.1493–1504,Apr.2020. [73] A. Özdemir, K. Polat, and A. Alhudhaif, ‘‘Classification of imbal-
[52] K.SongandY.Yan,‘‘Anoiserobustmethodbasedoncompletedlocal ancedhyperspectralimagesusingSMOTE-baseddeeplearningmethods,’’
binarypatternsforhot-rolledsteelstripsurfacedefects,’’Appl.Surf.Sci., ExpertSyst.Appl.,vol.178,Sep.2021,Art.no.114986.
vol.285,no.21,pp.858–864,Nov.2013. [74] M. Shuja, S. Mittal, and M. Zaman, ‘‘Effective prediction of type
[53] C.Du,Y.Wang,C.Wang,C.Shi,andB.Xiao,‘‘Selectivefeatureconnec- II diabetes mellitus using data mining classifiers and SMOTE,’’ in
tionmechanism:Concatenatingmulti-layerCNNfeatureswithafeature Advances in Computing And Intelligent Systems. Singapore: Springer,
selector,’’PatternRecognit.Lett.,vol.129,pp.108–114,Jan.2020. 2020,pp.195–211.
VOLUME11,2023 6877

R.Kuttalaetal.:MultimodalHierarchicalCNNFeatureFusionforStressDetection
[75] S.BanerjeeandG.K.Singh,‘‘AnewapproachofECGsteganographyand RADHIKA KUTTALA received the master’s
predictionusingdeeplearning,’’Biomed.SignalProcess.Control,vol.64, degreeincomputersciencefromAmritaVishwa
Feb.2021,Art.no.102151. Vidyapeetham, India, in 2018, where she is
[76] O.Kwon,J.Jeong,H.B.Kim,I.H.Kwon,S.Y.Park,J.E.Kim,and currently pursuing the Ph.D. degree with
Y. Choi, ‘‘Electrocardiogram sampling frequency range acceptable for the Department of Electrical and Electron-
heartratevariabilityanalysis,’’HealthcareInformat.Res.,vol.24,no.3,
|     |     |     |     |     |     |     |     | ics Engineering. | Her | research | interests | include |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------- | --------- | ------- |
pp.198–206,Jul.2018.
|     |     |     |     |     |     |     |     | multi-modal | interactions | and | deep learning | for |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | ------------- | --- |
[77] R.Rakshit,V.R.Reddy,andP.Deshpande,‘‘Emotiondetectionandrecog-
applicationsinaffectivecomputing.
| nition | using | HRV features | derived | from photoplethysmogram |     |     | signals,’’ |     |     |     |     |     |
| ------ | ----- | ------------ | ------- | ----------------------- | --- | --- | ---------- | --- | --- | --- | --- | --- |
inProc.2ndWorkshopEmotionRepresent.ModelingCompanionSyst.,
Nov.2016,pp.1–6.
| [78] J. Shukla, | M.  | Barreda-Angeles, |     | J. Oliver, | G. C. Nandi, | and | D. Puig, |     |     |     |     |     |
| --------------- | --- | ---------------- | --- | ---------- | ------------ | --- | -------- | --- | --- | --- | --- | --- |
‘‘Featureextractionandselectionforemotionrecognitionfromelectro-
dermalactivity,’’IEEETrans.Affect.Comput.,vol.12,no.4,pp.857–869,
Oct.2021.
[79] P.GhaderyanandA.Abbasi,‘‘Anefficientautomaticworkloadestimation
methodbasedonelectrodermalactivityusingpatternclassifiercombina-
tions,’’Int.J.Psychophysiol.,vol.110,pp.91–101,Dec.2016.
|              |       |              |          |             |             |     |            | RAMANATHAN    |          | SUBRAMANIAN |              | (Senior |
| ------------ | ----- | ------------ | -------- | ----------- | ----------- | --- | ---------- | ------------- | -------- | ----------- | ------------ | ------- |
| [80] J. Cui, | U. A. | Leuenberger, | F. Aziz, | J. C. Luck, | J. Stavres, |     | D. J. Kim, |               |          |             |              |         |
|              |       |              |          |             |             |     |            | Member, IEEE) | received | the         | Ph.D. degree | in      |
Z.Gao,C.Blaha,A.Cauffman,andL.I.Sinoway,‘‘Autonomicresponses
toacutehyperoxiaareimpairedinpatientswithperipheralarterydisease,’’ electrical and computer engineering from NUS,
FASEBJ.,vol.36,no.S1,May2022. in 2008. His past affiliations include IHPC,
[81] P.Gomes,P.Margaritoff,andH.Silva,‘‘pyHRV:Developmentandevalu- Singapore; University of Glasgow, Singapore;
ationofanopen-sourcePythontoolboxforheartratevariability(HRV),’’ IIIT Hyderabad, India; IIT Ropar, India; and
inProc.Int.Conf.Electr.,Electron.Comput.Eng.,2019,pp.822–828. UIUC-ADSC,Singapore.HeiscurrentlyanAsso-
[82] K. Radhika, R. Subramanian, and V. R. M. Oruganti, ‘‘Joint modality ciate Professor with the University of Canberra,
featuresinfrequencydomainforstressdetection,’’IEEEAccess,vol.10,
|     |     |     |     |     |     |     |     | Australia. His | research | interests | include | human- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | --------- | ------- | ------ |
pp.57201–57211,2022.
|     |     |     |     |     |     |     |     | centered computing, |     | interactive | analytics, | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ----------- | ---------- | --- |
[83] V.MarkovaandT.Ganchev,‘‘Automatedrecognitionofaffectandstress
explainablemachinelearning.HeisaSeniorMemberofACMandAAAC.
| evoked | by audio-visual |     | stimuli,’’ | in Proc. | 7th Balkan | Conf. | Lighting |     |     |     |     |     |
| ------ | --------------- | --- | ---------- | -------- | ---------- | ----- | -------- | --- | --- | --- | --- | --- |
(BalkanLight),Sep.2018,pp.1–4.
[84] V.MarkovaandT.Ganchev,‘‘Constrainedattributeselectionforstress
| detection | based | on physiological |     | signals,’’ | in Proc. | Int. Conf. | Sensors, |     |     |     |     |     |
| --------- | ----- | ---------------- | --- | ---------- | -------- | ---------- | -------- | --- | --- | --- | --- | --- |
SignalImageProcess.,Oct.2018,pp.41–45.
| [85] K. Radhika |     | and V. R. | M. Oruganti, | ‘‘Transfer | learning | for | subject- |     |     |     |     |     |
| --------------- | --- | --------- | ------------ | ---------- | -------- | --- | -------- | --- | --- | --- | --- | --- |
independentstressdetectionusingphysiologicalsignals,’’inProc.IEEE
17thIndiaCouncilInt.Conf.(INDICON),Dec.2020,pp.1–6.
[86] K.RadhikaandV.R.M.Oruganti,‘‘Deepmultimodalfusionforsubject-
| independent |     | stress detection,’’ | in  | Proc. 11th | Int. Conf. | Cloud | Comput., |         |        |        |          |     |
| ----------- | --- | ------------------- | --- | ---------- | ---------- | ----- | -------- | ------- | ------ | ------ | -------- | --- |
|             |     |                     |     |            |            |       |          | VENKATA | RAMANA | MURTHY | ORUGANTI |     |
DataSci.Eng.(Confluence),Jan.2021,pp.105–109.
(SeniorMember,IEEE)receivedthemaster’sand
[87] K.RadhikaandV.R.M.Oruganti,‘‘StressdetectionusingCNNfusion,’’
inProc.IEEERegion10Conf.(TENCON),Dec.2021,pp.492–497. Ph.D. degrees in electrical engineering from IIT
|     |     |     |     |     |     |     |     | Delhi, India. | His past | affiliations | include | NUS, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | ------------ | ------- | ---- |
[88] K.RadhikaandV.R.M.Oruganti,‘‘Crossdomainfeaturesforsubject-
|             |     |                     |     |            |        |          |       | Singapore; | NTU, Singapore; |     | the University | of  |
| ----------- | --- | ------------------- | --- | ---------- | ------ | -------- | ----- | ---------- | --------------- | --- | -------------- | --- |
| independent |     | stress detection,’’ | in  | Proc. IEEE | Region | 10 Symp. | (TEN- |            |                 |     |                |     |
Canberra,Australia;andCarnegieMellonUniver-
SYMP),Jul.2022,pp.1–6.
sity,USA.HeiscurrentlyanAssistantProfessor
| [89] K. Kalinkov, |     | T. Ganchev, | and V. | Markova, | ‘‘Adaptive | feature | selection |                     |     |               |     |           |
| ----------------- | --- | ----------- | ------ | -------- | ---------- | ------- | --------- | ------------------- | --- | ------------- | --- | --------- |
|                   |     |             |        |          |            |         |           | with the Department |     | of Electrical | and | Electron- |
throughFisherdiscriminantratio,’’inProc.Int.Conf.Biomed.Innov.Appl.
(BIA),Nov.2019,pp.1–4. ics Engineering, Amrita Vishwa Vidyapeetham,
[90] M. Kang, S. Shin, G. Zhang, J. Jung, and Y. T. Kim, ‘‘Mental stress India.Hisresearchinterestsincludemedicalimage
classificationbasedonasupportvectormachineandnaiveBayesusing processingandaffectivecomputing.HeisamemberofACM.
electrocardiogramsignals,’’Sensors,vol.21,no.23,p.7916,Nov.2021.
| 6878 |     |     |     |     |     |     |     |     |     |     | VOLUME11,2023 |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |