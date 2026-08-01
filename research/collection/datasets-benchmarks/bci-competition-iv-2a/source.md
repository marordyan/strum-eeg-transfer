REVIEWARTICLE
published:13July2012
doi:10.3389/fnins.2012.00055
Review of the BCI competition IV
MichaelTangermann1*,Klaus-RobertMüller1,2,AdAertsen3,NielsBirbaumer4,5,ChristophBraun6,7,
ClemensBrunner8,9,RobertLeeb10,CarstenMehring3,11,12,KaiJ.Miller13,GernotR.Müller-Putz8,
GuidoNolte14,GertPfurtscheller8,HubertPreissl6,15,GerwinSchalk16,17,18,19,20,AloisSchlögl21,
CarmenVidaurre1,StephanWaldert3,6,22 andBenjaminBlankertz23
1MachineLearningLaboratory,BerlinInstituteofTechnology,Berlin,Germany
2DepartmentofBrainandCognitiveEngineering,KoreaUniversity,Seoul,Korea
3FacultyofBiology,BernsteinCenterFreiburgandUniversityofFreiburg,Freiburg,Germany
4InstituteofMedicalPsychologyandBehavioralNeurobiology,UniversityofTübingen,Tübingen,Germany
5OspedaleSanCamillo,IstitutodiRicoveroeCuraaCarattereScientifico,Venezia,Italy
6MEG-Center,UniversityofTübingen,Tübingen,Germany
7CenterofMind/BrainSciences,UniversityofTrento,Trento,Italy
8InstituteforKnowledgeDiscovery,GrazUniversityofTechnology,Graz,Austria
9SwartzCenterforComputationalNeuroscience,InstituteforNeuralComputation,UniversityofCaliforniaSanDiego,LaJolla,CA,USA
10ÉcolePolytechniqueFédéraledeLausanne,Lausanne,Switzerland
11DepartmentofBioengineering,ImperialCollegeLondon,London,UK
12DepartmentofElectricalandElectronicEngineering,ImperialCollegeLondon,London,UK
13Physics,NeurobiologyandBehavior,Medicine,UniversityofWashington,Seattle,WA,USA
14InstituteforNeurophysiologyandPathophysiology,UniversityMedicalCenterHamburg-Eppendorf,Hamburg,Germany
15DepartmentofObstetricsandGynecology,UniversityofArkansasforMedicalSciences,LittleRock,AR,USA
16Brain-ComputerInterfaceR&DProgram,WadsworthCenter,NewYorkStateDepartmentofHealth,Albany,NY,USA
17DepartmentofNeurology,AlbanyMedicalCollege,Albany,NY,USA
18DepartmentofNeurologicalSurgery,SchoolofMedicine,WashingtonUniversity,St.Louis,MO,USA
19DepartmentofBiomedicalEngineering,RensselaerPolytechnicInstitute,Troy,NY,USA
20DepartmentofBiomedicalSciences,SchoolofPublicHealth,StateUniversityofNewYork,Albany,NY,USA
21InstituteforScienceandTechnologyAustria,MariaGugging,Austria
22SobellDepartmentofMovementNeuroscienceandMovementDisorders,InstituteofNeurology,UniversityCollegeLondon,London,UK
23NeurotechnologyGroup,BerlinInstituteofTechnology,Berlin,Germany
Editedby: The BCI competition IV stands in the tradition of prior BCI competitions that aim to pro-
EilonVaadia,TheHebrewUniversity, vide high quality neuroscientific data for open access to the scientific community. As
Israel
experiencedalreadyinpriorcompetitionsnotonlyscientistsfromthenarrowfieldofBCI
Reviewedby:
compete,butscholarswithabroadvarietyofbackgroundsandnationalities.Theyinclude
KenjiKansaku,ResearchInstituteof
NationalRehabilitationCenterfor highspecialistsaswellasstudents.ThegoalsofallBCIcompetitionshavealwaysbeento
PersonswithDisabilities,Japan challengewithrespecttonovelparadigmsandcomplexdata.Wereportonthefollowing
JoseL.“Pepe”Contreras-Vidal, challenges:(1)asynchronousdata,(2)synthetic,(3)multi-classcontinuousdata,(4)session-
UniversityofHouston,USA
to-session transfer, (5) directionally modulated MEG, (6) finger movements recorded by
*Correspondence:
ECoG. As after past competitions, our hope is that winning entries may enhance the
MichaelTangermann,Machine
LearningLaboratory,BerlinInstitute analysismethodsoffutureBCIs.
ofTechnology,FR6-9,Franklinstr.
Keywords:brain-computerinterface,BCI,competition
28/29,10587Berlin,Germany.
e-mail:michael.tangermann@
tu-berlin.de
1. INTRODUCTION Apart from communication and control, recently more and
Brain-computer interfacing (BCI) is an approach to establish a morealternativeapplicationsofBCItechnologyarebeingexplored
novelcommunicationchannelfrommentomachines.Thecru- (Blankertz et al., 2010). These include enhancement of human
cial idea is to directly tap the communication at its very origin: performance(Haufeetal.,2011)andassessingsubconsciousper-
the human brain. BCI technology is used to date primarily for ception (Porbadnigk et al.,2010,2011). Data from those recent
intentional control. This branch of BCI research aims at the developments have not yet been included in the BCI competi-
(partial) restoration and rehabilitation of lost functions in par- tions, but may pose interesting and novel challenges for future
alyzed patients (Kübler et al., 2001; Wolpaw et al., 2002). The competitions.
focus of the fourth BCI competition was on BCI systems that
are based on the motor and sensorimotor system of the brain. 1.1. RELEVANCEOFBCICOMPETITIONS
In line with the past three BCI competitions, this fourth BCI The impact of the past three competitions on the field of BCI
competition strives to help the field of BCI prosper by eliciting researchismanifoldandthusworthacloserlook.Oneindicator
solutions for hard data analysis problems appearing in current of the overall relevance of the BCI competitions for the scien-
BCIresearch. tificcommunityisthenumberof citations.Figure1showshow
www.frontiersin.org July2012|Volume6|Article55|1

Tangermannetal. ReviewoftheBCIcompetitionIV
30
25
20
15
10
5
0
2003 2004 2005 2006 2007 2008 2009 2010 2011
Year
snoitatic
fo
rebmuN
I
II
III
FIGURE1|Citationsoftheoverviewarticlesonprevious
competitions.Thehistogramshowshowmanytimestheeditorialarticles
onBCIcompetitionsI(Sajdaetal.,2003),II(Blankertzetal.,2004),andIII
(Blankertzetal.,2006)havebeencitedinISI-indexedjournals.Datawere
retrievedfromtheISIWebofKnowledgeonDecember1st2011.
80
60
40
20
0
2004 2005 2006 2007 2008 2009 2010 2011
Year
snoitatic
fo
rebmuN
theiralgorithmsisindependentlyvalidatedthroughthecompeti-
tionprocess.Thisisanattractiveopportunityevenforresearchers
whodonothaveaccesstoanacquisitiondeviceforbrainsignals
orafullyrunningBCIsystem.Additionally,someresearchersof
thebetterperformingteamswerehiredorhostedbyBCIgroups
(inparticulartheonecontributingdatasetstothecompetition).
Most important,the results of the BCI competitions provide
anindicationofwhattypeofmethodsareeffective.Agoodexam-
ple of such a lesson that can be learned from the competitions
isthatcommonspatialpatternanalysis(CSP/CSSD;Koles,1991;
Ramoseretal.,2000;Blankertzetal.,2008b)anditsvariantsare
arobusttoolforexploitingERD/ERSeffects(Pfurtschellerandda
Silva,1999):AlmostalldatasetsthroughoutallBCIcompetitions
inwhichCSPwasreasonablyapplicable(e.g.,formulti-channel
recordingsorforparadigmsinwhichdifferentialERD/ERSeffects
areexpected)havebeenwonbyanalgorithminvolvingavariant
ofCSP:competitionII(2a,4);competitionIII(1,3,4a,4c);com-
petitionIV(1,2a,2b).ThesuccessoftheCSP-basedmethodsin
theBCIcompetitionsmayhaveapromotingfactorfortheflour-
ishingdevelopmentofvariantsofCSPanalysis(LotteandGuan,
2011;Nikulinetal.,2011;Sannellietal.,2011).
In contrast, the application of principle component analysis
II
(PCA)orindependentcomponentanalysis(ICA),whicharevery
successfulpreprocessingmethodsinotherapplicationfields,seem
tobealesseffectiveingredienttoimprovetheclassificationper-
formanceinBCI(butnote,thatICAwasusedinXuetal.,2004).
This advance of CSP compared to PCA and ICA may to a large
extendbeexplainedbythedifferentstrategiesconcerningtheuse
of classlabels.WhileCSPexploitstheinformationcontainedin
thelabelsinasupervisedmanner,ICAandPCAareunsupervised
methods.
In this context,we would like to stress that the competitions
arebynomeansasystematicevaluationofallavailablealgorithms.
Therefore,wewouldstillliketoencouragetoexplorethefullrealm
FIGURE2|Citationsofthearticlesbythecompetitionwinners.The
histogramshowshowmanytimesthearticlesofthewinningteamsofBCI ofsignalprocessingandpatternrecognitionalgorithmsforBCI.
competitionII(describingthewinningalgorithms)havebeencitedin
ISI-indexedjournals.DatawereretrievedfromtheISIWebofKnowledge 1.2. THEROLEOFOPENDATA
onDecember1st2011.
BCIresearchiscomplex,andtodesignanonlineBCIexperiment
orsuccessfullyrunaBCIapplicationinvolvesthecooperationof
specialists from various disciplines. The availability of BCI data
oftenthethreeoverviewarticlesonthepastBCIcompetitionsI from past competitions is an important contribution to stimu-
(Sajdaetal.,2003),II(Blankertzetal.,2004),andIII(Blankertz latetheinterdisciplinaryengagementofstudentsandresearchers
etal.,2006)havebeencitedinISI-indexedjournalsandconfer- fromneighboringresearchareas,whocanenrichthefieldofBCI.
ence proceedings. The overall sum is 255. From competition II Thisisespeciallytrueforscientistsspecializedinsignalprocess-
on,the concept was introduced to have publications of all win- ing,dataanalysis,andmachinelearning,butalsoforresearchers
ningalgorithmswithinoneissueof ajournal.Thisworkedvery fromthefieldofhuman-computerinteraction(HCI).Whilethese
wellintheBCIcompetitionIIwhereallwinnerarticleshavebeen specialistshavethepotentialtoimprovetheprogressofBCIwith
published in volume 51 of IEEE Trans Biomed Eng (Blanchard newalgorithmicmethodsorimprovedusabilityof BCIapplica-
and Blankertz, 2004; Bostanov, 2004; Kaper et al., 2004; Lemm tions,thefieldofBCIneedstoprovidethefuel,thatisdata.Data,
etal.,2004;Menshetal.,2004;Wangetal.,2004;Xuetal.,2004). thatontheonehandistypicallynoisy,high-dimensional,shows
Suchconcertedpublicationleadstogoodvisibility,andasacon- non-stationarycharacteristics,andthusprovidesachallengingtest
sequencetosubstantialcitations,seeFigure2.(IncompetitionIII groundespeciallyforthesignalprocessingandmachinelearning
onlysomewinningalgorithmswerepublishedspreadcrosssev- community. On the other hand, BCI data represents – if inter-
eraljournals;Weietal.,2006;Galanetal.,2007;Zhangetal.,2007; pretedasasignalforcommunicationandcontrol–aninherently
RakotomamonjyandGuigue,2008.) unreliableandslowcommunicationchannel.Fromtheviewpoint
Moreover,researchgroupsthatarerelativelynewtothefieldof ofHCI,thefieldofBCIcanbeconsideredachallengeasitrequires
BCIcanattractattentionandgetrenownediftheperformanceof highlyrobustinteractionmodelsinordertocopewiththeabove
FrontiersinNeuroscience|Neuroprosthetics July2012|Volume6|Article55|2

| Tangermannetal. |     |     |     |     |     |     |     | ReviewoftheBCIcompetitionIV |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- |
mentionedchallenges.Finally,anysuccessstoryfortheinteraction clearlyrelevantasthesesingle-trialdataanalysismethodsprovide
designinBCImightbetransferableintotheotherfieldslikeusabil- apossibilitytomonitortheactingandbehavingbrain.Thisisa
ity of mobile devices or gesture controlled applications, which prerequisitetostudythedynamicsofbrainprocesses,andeventu-
sharesomeoftheseinterestingcharacteristics. allydevelopnewreactiveexperimentalparadigms,thatvary,e.g.,
|                                         |     |     |     | stimulus | conditions | depending | on  | the current | state | in a closed |
| --------------------------------------- | --- | --- | --- | -------- | ---------- | --------- | --- | ----------- | ----- | ----------- |
| 1.3. NOTESONTHEUSEOFBCI-COMPETITIONDATA |     |     |     | loop.    |            |           |     |             |       |             |
Despite of a number of high quality algorithmic solutions pro- Thedatasetsofthiscompetitionalldealwithmotorparadigms,
posed by the competition winners in the following sections,the andmorespecificallywithoscillatorysignalswhicharerelatedto
| actual learning | problems | posed in this competition | are surely |     |     |     |     |     |     |     |
| --------------- | -------- | ------------------------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
imaginedmotoractionsormotorexecution.Asanexample,direct
of interest in the future, and the proposal of new methods for clinicalrelevanceofBCItechnologycanbeexpectedforthesup-
their solution can enhance the field of BCI. For this reason,the port of rehabilitation training in patients suffering from stroke
competitiondatasetshavebeenprovidedonlineasopendata.Fur-
(Silvonietal.,2011)incorticalmotorareas.However,aschanges
thermore,thelabelsofthetestdata,whichhavenotbeenavailable of oscillatoryprocessesarenotuniquelyobservedduringmotor
totheparticipantsoftheBCIcompetitionIV,havebeenpublished activities,butrepresentarathergeneralhigh-levelcharacteristicof
inaddition. manybrainprocesses,thebenefitofthisBCIcompetitionshould
Wewouldliketoencouragetheuseofthisdataandthepublica-
extendfrommotorsystemresearchtootherfields.
tionsofanyresultsandinsights.Uponpublicationofsuchresults, Dataset1of theBCIcompetitionIVaddressesthechallenge
however,wewouldliketodrawyourattentiontothreeimportant tocorrectlydealwithintendednon-controlperiodsanduncued
aspects:
periodsofcontrolactivity.Thisisofhighclinicalrelevance,asany
First, any performance improvement over the competition practicalapplicationofamotorimageryBCIsystemwillrequire
results,shouldbereportedwithanoteofcaution,asitcouldmerely thattheBCIsystemrecognizesperiodsofrestingandcomingback
reflect random fluctuations. Ideally, the performance should be toactiveBCIcontrol.
reportedforlargeramountsoftestdata.
|     |     |     |     | Data set | 2a enlarges | the | number | of control | classes | from two |
| --- | --- | --- | --- | -------- | ----------- | --- | ------ | ---------- | ------- | -------- |
Second,acomparisonwiththeperformanceofthecompetitors to four. Compared to the simpler setting of only two motor
shouldbedrawncarefullyonly,asanypost-competitionworkon imagery classes, this enlargement contains the risk of a reduc-
thesamedatahasbeenperformedundertheadvantageofknow-
tioninclassificationaccuracy.However,italsooffersthepotential
ingthecompetitionoutcome,knowingthespecificshortcomings ofhigherinformationtransferrates,andmorenaturalinteraction
ofthesubmittedalgorithms,andhavinginsightintowhichclasses paradigms between user and application. In combination with
ofalgorithmsperformbetterorworseonthatdata.
|            |             |                          |                | the continuous | classification |     | setting, | this is | clearly | of practical |
| ---------- | ----------- | ------------------------ | -------------- | -------------- | -------------- | --- | -------- | ------- | ------- | ------------ |
| Third,even | so the test | data labels are publicly | available now, | relevance.     |                |     |          |         |         |              |
theiruseshouldberestrictedtofinallydeterminetheperformance Data set 2b challenges the session-to-session transfer of clas-
ofamethod.Thetestdatashouldnotbetouchedatallduringthe sificationmodels.Avoidingthetime-consumingre-calibrationof
algorithmdesignprocessandthedeterminationofhyperparame-
theBCIsystem,suchapproachesareofhighpracticalimportance
ters,asthiscanleadtoasubstantialamountofoverfitting(Lemm forend-users,whowanttouseaBCIonadailybasis.
etal.,2011). Dataset3isacollectionof magnetoencephalography(MEG)
signals.Whilemostmotorparadigmsinnon-invasiveBCImake
1.4. RELEVANCEOFTHEDATASETS
|     |     |     |     | useof thelateralizationof |     | motor-relatedsignals(e.g.,ERD/ERS |     |     |     |     |
| --- | --- | --- | --- | ------------------------- | --- | --------------------------------- | --- | --- | --- | --- |
Foranoverview,alistofdatasetsandthecorrespondingwinning effectsoverthelefthandandrighthandcortex),thisdatasetseeks
teamsissummarizedinTables1and2. to extract a multi-class decision from a single hand only. Com-
TheBCIcompetitionfostersalgorithmicsolutions,whichallow
|     |     |     |     | parable to | data set | 2a, the expansion |     | from two | to more | classes |
| --- | --- | --- | --- | ---------- | -------- | ----------------- | --- | -------- | ------- | ------- |
forasingle-trialassessmentofmentalstates.Fortheneurosciences,
hasthepotentialtoboosttheinformationtransferrateofaBCI.
suchdevelopmentsinsignalprocessingandmachinelearningare Furthermorethedatasetisanexampleforthepossibilitytoinfer
handmovementdirectionsnotonlyfromsinglecellspikingactiv-
|     |     |     |     | ity (e.g., | by intra-cortical | single | unit | recordings; | Georgopoulos |     |
| --- | --- | --- | --- | ---------- | ----------------- | ------ | ---- | ----------- | ------------ | --- |
Table1|OverviewofthedatasetsofBCIcompetitionIV.
|     |     |     |     | et al., 1982; | Velliste | et al., 2008), | which | are | known | to realize a |
| --- | --- | --- | --- | ------------- | -------- | -------------- | ----- | --- | ----- | ------------ |
directionalcoding,butalsofromnon-invasivemeasurementsof
| # Lab | #Channels | Paradigmandchallenge |     |                                                |     |     |     |     |     |              |
| ----- | --------- | -------------------- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | ------------ |
|       |           |                      |     | largerpopulations(Waldertetal.,2008).Despiteof |     |     |     |     |     | itspractical |
1 Berlin 64EEG 2-Classmotorimagery,uncued restrictions (an MEG system is neither practical nor affordable
forpatients),thisMEG-BCIcouldstillbeappliedinconjunction
classifierapplication
2a Graz 22EEG 4-Classmotorimagery,continuous withonlinefeedback,e.g.,forstrokerehabilitationattempts(Buch
|     |     | classifierapplication |     | etal.,2008)orforprosthesistraining. |     |     |     |     |     |     |
| --- | --- | --------------------- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
2b Graz 3EEG Motorimagery,session-to-session Thegoalfordataset4oftheBCIcompetitionIVwastoinfer
|     |     |     |     | the flexion | of individual | fingers | from | signals | recorded | from the |
| --- | --- | --- | --- | ----------- | ------------- | ------- | ---- | ------- | -------- | -------- |
transferandeyeartifacts
3 Freiburg 10MEG Decodingdirectionsof surfaceofthebrainviaelectrocorticography(ECoG).Determin-
finger/hand/wristmovements ingtherelationshipofECoGsignalswithfingerflexionprovides
|                     |        |                             |     | new neuroscientific                     |     | understanding, |     | and may                      | eventually | lead to |
| ------------------- | ------ | --------------------------- | --- | --------------------------------------- | --- | -------------- | --- | ---------------------------- | ---------- | ------- |
| 4 Seattle/Albany    | 64ECoG | Discriminationofmovementsof |     |                                         |     |                |     |                              |            |         |
|                     |        | individualfinders           |     | improvedbrain-computerinterfacesystems. |     |                |     |                              |            |         |
| www.frontiersin.org |        |                             |     |                                         |     |                |     | July2012|Volume6|Article55|3 |            |         |

| Tangermannetal. |     |     |     |     |     |     |     |     |     | ReviewoftheBCIcompetitionIV |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- |
Table2|ThisTableliststhewinningteamsforallcompetitiondatasets.
| Dataset Researchlab |     |     |     |     |     | Contributor(s) |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
1 InstituteforInfocommResearch,Singapore ZhangHaihong,AngKaiKeng,GuanCuntai,WangChuanchu,Chin
ZhengYang
2a InstituteforInfocommResearch,Singapore KaiKengAng,ZhengYangChin,ChuanchuWang,CuntaiGuan,
HaihongZhang,KokSoonPhua,BrahimHamadicharef,KengPeng
Tee
2b InstituteforInfocommResearch,Singapore ZhengYangChin,KaiKengAng,ChuanchuWang,CuntaiGuan,
HaihongZhang,KokSoonPhua,BrahimHamadicharef,KengPeng
Tee
3 BiomedicalSignalandImageProcessingLaboratory(BiSIPL),Sharif SepidehHajipour,MohammadBagherShamsollahi
UniversityofTechnology,Tehran,Iran
4 CortexTeam,ResearchCentreINRIA,France NanyingLiang,LaurentBougrain
| 1.5. OVERVIEWOFTHEARTICLE |     |     |     |     |     | 2.3. CAUSALITYOFMETHODS |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
AftersomegeneralremarksconcerningtheconceptandtheBCI Asthefulltestsetisavailabletotheparticipantsfromthebegin-
competitionsinSection2,thesubsequentfivesections,willchar- ningandnot(asinarealonlineexperiment)incrementally,the
acterizeeachdatasetcontainedintheBCIcompetitionIVindetail, participants could in principle exploit the structure of the full
includinganassessmentofitsrelevancetothefield,experimental (unlabeled) data already in advance in order to improve their
details,thedataformat,theappliedevaluationcriterionforsub- label estimate even for the first trials. The organizers are aware
missions,and a brief outcome. The article closes with a section of the problem, that this use of data is non-causal and unreal-
abouttheoverallresultsofthecompetitionandadiscussion.The istic.Consequentlyitwasnotallowedforparticipantstoexploit
latterincludesprospectivetopicsofsubsequentcompetitions. thisunrealisticadvantage,thattheycouldgaincomparedtoaBCI
| The winning | labs | published | individual | articles | on their | practitioner. |     |     |     |     |     |     |
| ----------- | ---- | --------- | ---------- | -------- | -------- | ------------- | --- | --- | --- | --- | --- | --- |
approaches,see(Angetal.,2012;FlamaryandRakotomamonjy, However,the distribution of test data is simplified to a large
2012;SardouieandShamsollahi,2012;Zhangetal.,2012). extend,ifitcanbeprovidedenbloc.Inordertoensurecausalpro-
|     |     |     |     |     |     | cessingdespiteof |         | thisdistributionmethod,theparticipantshad |        |           |                 |     |
| --- | --- | --- | --- | --- | --- | ---------------- | ------- | ----------------------------------------- | ------ | --------- | --------------- | --- |
|     |     |     |     |     |     | to submit        | a short | description                               | of the | developed | data processing |     |
2. GENERALSTRUCTUREOFTHEDATASETSANDTHE
routines.Incaseofunclearcausalitytheparticipantshadtoprove
MACHINELEARNINGTASK
|                  |        |     |                 |           |         | that their | approach | is causal | by handing | in the | data processing |     |
| ---------------- | ------ | --- | --------------- | --------- | ------- | ---------- | -------- | --------- | ---------- | ------ | --------------- | --- |
| Challenges posed | within | the | BCI competition | typically | contain |            |          |           |            |        |                 |     |
routinesinadditiontothelabels.
| a problem description,a                                  |     | training | data set,a | test | data set,and | a           |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | -------- | ---------- | ---- | ------------ | ----------- | --- | --- | --- | --- | --- | --- |
| descriptionoftheevaluationmetricthatisappliedtodetermine |     |          |            |      |              | 3. DATASET1 |     |     |     |     |     |     |
theperformanceofcontributedalgorithms.
Dataset1AsynchronousMotorImageryisprovidedbyB.Blankertz,
|     |     |     |     |     |     | C. Vidaurre | and | K.-R. Müller | from | Berlin | (Germany). | It can |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ------------ | ---- | ------ | ---------- | ------ |
befreelyassessedviahttp://www.bbci.de/competition/iv/withthe
2.1. TRAININGDATA
This collection of data (also called calibration data) comprises only restriction that the present article is referenced upon any
publicationofresults.
thedataepochsfromEEG,MEG,orECoGrecordings,thelabels
ormarkersthatdescribethetasksthatweretobeperformedby
3.1. MOTIVATION
| subjects at recording |     | time, and | the cues | which | had been pre- |                     |     |               |     |        |                     |     |
| --------------------- | --- | --------- | -------- | ----- | ------------- | ------------------- | --- | ------------- | --- | ------ | ------------------- | --- |
|                       |     |           |          |       |               | Most demonstrations |     | of algorithms |     | on BCI | data are evaluating |     |
sentedtothem.Inaddition,thegroupsprovidingthetrainingdata
classificationofEEGtrials,i.e.,segmentsofEEGsignalsofafixed
describethespecificperformancemetricaccordingtowhichany
length,whereeachtrialcorrespondstoaspecificmentalstate.But
participant’scompetitionentrywillberated.Participantsusedthis
inBCIapplicationswithasynchronousfeedback,e.g.,cursorcon-
informationtodevelopaprocessingmethodthatwasabletoesti-
|     |     |     |     |     |     | trol, one | is faced | with the | problem that | the | classifier has | to be |
| --- | --- | --- | --- | --- | --- | --------- | -------- | -------- | ------------ | --- | -------------- | ----- |
matelabelsbasedondata.Anymethodcouldonlybesuccessful,
appliedcontinuouslytotheincomingEEGwithouthavingcuesof
ifitgeneralizedwellonnewtestdata.
whenthesubjectisswitchingher/hisintention.Thisdatasetposes
thechallengeofapplyingaclassifiertocontinuousEEGforwhich
| 2.2. TESTDATA |     |     |     |     |     | nocueinformationisgiven. |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
This data set (also called evaluation data) contains data epochs, Anotherissuethatisaddressedinthisdatasetisthatthetest
butnolabelsormarkers.Thelabelsdoexistbutweresecrettothe datacontainsperiodsinwhichtheuserhasnocontrol intention.
participants.Thetaskofparticipantswastoestimatethelabelsof Duringthoseintervalstheclassifierissupposedtoreturnto0(no
thetestdataandsendthemin.Thedataprovidinggroupevalu- affiliationtooneofthetargetclasses).
ated the labels according to the predefined performance metric, Asaspecialfeature,someofthedatasetswereartificiallygen-
thathadbeenpublishedtogetherwiththetrainingdata. erated.TheideawastohaveameansforgeneratingartificialEEG
FrontiersinNeuroscience|Neuroprosthetics July2012|Volume6|Article55|4

Tangermannetal. ReviewoftheBCIcompetitionIV
signalswithspecifiedpropertiesthataresorealisticthattheycan
be used to evaluate and compare analysis techniques. The com-
petition is a possibility to verify whether the applied methods
perform comparably on artificial and real data. The only infor-
mationprovidedtothecompetitorswasthatthereisatleastone
realandatleastoneartificialdataset,whilethetruedistribution
remainedundiscloseduntilthesubmissiondeadline.Forcompe-
titionpurpose,onlyresultsfortherealdataset(s)wereconsidered,
but results for artificial data were also reported for comparison.
SeethesubsequentSection4foradetaileddescriptionofthegen-
erationoftheartificialdataandacomparisonofthecompetition
resultsobtainedonrealvs.artificialdata.
3.2. MATERIALSANDSUBJECTS
Thesedatasetswererecordedexclusivelyforthepurposeof the
FIGURE3|(Dataset1–trialstructure).Trainingdatawascollectedinthe
competition. Four healthy participants served as experimental
calibrationruns.Arrowspointingleft,right,ordownhavebeenpresentedas
subjects.Inthewholesessionmotorimagerywasperformedwith- cuesforimagininglefthand,righthand,orfootmovements.Afterafixation
outfeedback.Foreachparticipanttwoclasses of motorimagery crosswaspresentedfor2s,thedirectionalcuewasoverlaidfor4s.Then
wereselectedfromthethreeclasseslefthand,righthand,andfoot thescreenwasblankfor2s.Inthetestrunsusedforevaluation,spoken
wordshavebeenpresentedascues.
(sidechosenbytheindividual;optionallyalsobothfeet).
3.2.1. Experimentalparadigm 3.2.2.2. Testdata. Then4runsfollowedwhichwereusedfor
The recording was made using BrainAmp MR plus amplifiers evaluatingthesubmissionstothecompetitions.Here,themotor
(BrainProductsGmbH,Munich,Germany)andaAg/AgClelec- imagerytaskswerecuedbyacousticstimuli(wordsleft,right,and
trodecap(EASYCAPGmbH).Signalsfrom59EEGpositionswere foot)forperiodsofvaryinglengthbetween1.5and8s.Theendof
measured that were most densely distributed over sensorimotor themotorimageryperiodwasindicatedbythewordstop.Intermit-
areas. Signals were band-pass filtered between 0.05 and 200Hz tingperiodshadalsoavaryingdurationof1.5–8s.Theacoustical
andthendigitizedat1000Hzwith16bit(0.1µV)accuracy.Also cues were soft-spoken it order to avoid that acoustically evoked
aversionofthedatawasprovidedthatwassubsampledat100Hz potentialscouldbedetectedtosegmentthedataintocontroland
[firstlow-passfilteringtheoriginaldata(ChebyshevTypeIIfilter no-controlintervals(oreventodecodethecueinformation).In
oforder10withstopbandripple50dBdownandstopbandedge eachrun,30trialsforeachclasshavebeenrecordedresultingin
frequency 49Hz) and then calculating the mean of consecutive atotalof240trials.Afterevery30trialsabreakof15swasgiven
blocksof10samples]. for relaxation. Between the runs there were longer breaks of 5–
15min.Competitorswereinformedthatthenumberoftrialsfrom
eachconditionwasnotnecessarilyequal.Duetotheexperimental
3.2.2. Protocol
design,thereweretwiceasmuchperiodsofnocontrolasperiods
The session was divided into two parts: recording of training
ofeachcondition.
dataandrecordingoftestdata.Trainingdatawereprovidedwith
Additionally,weintroducedakindofnon-stationarityintothe
complete marker information such that it could be used by the
testdatabychangingtheenvironmentalconditions.Occasionally
competitorsforadaptingtheparametersofthemethods/models.
during the runs music (2 times) or videos (2 times) have been
In contrast,the test data which was provided to the competitor
played,ortheparticipantwasinstructedtocloseher/hiseyes(2
only consisted of the EEG signals. The corresponding markers
times).Eachofthoseperiods(duringwhichthecuepresentation
havebeenkeptsecretuntilthesubmissiondeadlineandhavebeen
wasnotpaused)lastedabout2min.
usedtoevaluatethesubmissions.
3.3. INVESTIGATIONOFTHEDATASET
3.2.2.1. Trainingdata. In the first two runs,arrows pointing The most stable effect of motor imagery is a modulation of the
left,right,ordownwerepresentedasvisualcuesonacomputer sensorimotor rhythms (SMRs), see (Pfurtscheller and da Silva,
screen.Cuesweredisplayedforaperiodof 4sduringwhichthe 1999).ForhandmotorimageryanattenuationoftheSMRampli-
subjectwasinstructedtoperformthecuedmotorimagerytask. tudeoverthecontralateralmotorareaisexpected.Theeffectof
These periods were interleaved with 2s of blank screen and 2s footimageryismorediverse.AnattenuationoftheSMRoverthe
withafixationcrossshowninthecenterofthescreen.Thefixa- footarea,whichisonthemidlineof themotorcortexcouldbe
tioncrosswassuperimposedonthecues,i.e.,itwasshownfor6s, expected,butisrarelyobservedanddoesnotappearinthedata
seeFigure3.Ineachrun50trialsofeachofthechosentwoclasses set.Inmostofthesubjects,anincreaseoftheSMRamplitudeover
havebeenpresented,resultinginatotalof200trials.Afterevery thehandareasisobserved.Thisisalsothecaseforthetwopar-
15trialsabreakof15swasgivenforrelaxation.Betweentheruns ticipants(a andf)of thisdataset,whoperformedfootimagery.
therewerelongerbreaksof5–15min. Figure4 gives an overview,of how this effect is reflected in the
www.frontiersin.org July2012|Volume6|Article55|5

| Tangermannetal. |        |           |        |         |        |        |          |     |         |        |        |        | ReviewoftheBCIcompetitionIV |        |     |
| --------------- | ------ | --------- | ------ | ------- | ------ | ------ | -------- | --- | ------- | ------ | ------ | ------ | --------------------------- | ------ | --- |
|                 | a      |           | b      |         | c      |        | d        |     |         | e      |        | f      |                             | g      |     |
|                 | C3 lap |           | C3 lap |         | C4 lap |        | F C3 lap |     |         | C3 lap |        | C4 lap |                             | C4 lap |     |
| [d B 8 ]        |        | [ d B 2 ] |        | [ d B ] |        | [d B ] |          | [d  | 1 B 0 ] |        | [d B ] |        |                             | [d B ] |     |
| 4 6             |        | 0         |        | 5       |        |        |          |     | 6 8     |        |        |        |                             | 1 5    |     |
| 2               |        | − − 4 2   |        | 0       |        | 5      |          |     | 4       |        | 5      |        |                             | 1 0    |     |
| − 0 2           |        | − 6       |        | − 5     |        | 0      |          |     | 0 2     |        | 0      |        |                             | 5      |     |
| − 4             |        | − − 1 0 8 |        |         |        |        |          |     | − 2     |        |        |        |                             | 0      |     |
| − 6             |        | − 1 2     |        | − 1 0   |        | − 5    |          |     | − 4     |        | − 5    |        |                             |        |     |
5 10 15 20 25 30 35 [Hz] 5 10 15 20 25 30 35 [Hz] 5 10 15 20 25 30 35 [Hz] 5 10 15 2 0 25 30 35 [Hz] 5 10 15 20 25 30 35 [Hz] 5 10 15 20 25 30 35 [Hz] 5 10 15 20 25 30 35 [Hz]
|           |     | [u V ]  |     | [u V ]  |     |        |     |     |         |     | [u V ]      |     |     | [u V ]  |     |
| --------- | --- | ------- | --- | ------- | --- | ------ | --- | --- | ------- | --- | ----------- | --- | --- | ------- | --- |
| [u V ]    |     |         |     | 0 . 1   |     | [u V ] |     |     | [u V ]  |     | 0 . 3       |     |     | 1 . 5 1 |     |
| 0 . 1     |     | 0 . 0 5 |     | 0 . 0 5 |     | 0 . 2  |     |     | 0 . 0 5 |     | 0 0 . . 1 2 |     |     | 0 . 5   |     |
| 0 . 0 5 0 |     | 0       |     | 0       |     | 0 . 1  |     |     | 0       |     | 0           |     |     | 0       |     |
− 0 . 0 5 − 0 . 0 5 − 0 . 0 5 0 − 0 . 0 5 − 0 . 1 − 0 − . 5 1
| − 0 . 1 |     |     |     | − 0 . 1 |     | − 0 . 1 |     |     | − 0 . 1 |     | − 0 . 2 |     |     | − 1 . 5 |     |
| ------- | --- | --- | --- | ------- | --- | ------- | --- | --- | ------- | --- | ------- | --- | --- | ------- | --- |
0 1000 2000 3000 4000 [ms] − 0 . 1 0 1000 2000 3000 4000 [ms] − 0 . 1 5 0 1000 2000 3000 4000 [ms] 0 1000 2000 3000 4000 [ms] 0 1000 2000 3000 4000 [ms] − 0 . 3 0 1000 2000 3000 4000 [ms] − 2 0 1000 2000 3000 4000 [ms]
L − F sgn r 2 L − R sgn r2 L − R sgn r 2 L − R sgn r0 2 .5 L − R sgn r 2 L − F sgn r 2 L − R sgn r 2
|     |     | 0 .1 |     |     |     | 0 .05 |     |     |     | 0   | .04 |     | 0 .2 |     | 0 .1 |
| --- | --- | ---- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | ---- | --- | ---- |
0.05
|     |     | 0.05  |     |       |     |       |     |      |     | 0.02  |     |     | 0.1  |     | 0.05  |
| --- | --- | ----- | --- | ----- | --- | ----- | --- | ---- | --- | ----- | --- | --- | ---- | --- | ----- |
|     |     | 0     |     | 0     |     | 0     |     | 0    |     | 0     |     |     | 0    |     | 0     |
|     |     | −0.05 |     | −0.05 |     |       |     |      |     | −0.02 |     |     | −0.1 |     | −0.05 |
|     |     | −0.1  |     |       |     | −0.05 |     |      |     |       |     |     | −0.2 |     |       |
|     |     |       |     |       |     |       |     | −0.5 |     | −0.04 |     |     |      |     | −0.1  |
FIGURE4|(Dataset1–glanceattheneurophysiology).Thefirstrow spectrashownaboveisshaded.Thebottommostrowdisplaysthe(signed)
displaystheaveragedspectraofthetwochosenmotorimagerytasks(red: r2-differenceinlogband-powerbetweentheindividuallychosenmotor
lefthand,green:righthand;blue:foot)inthetrainingdata.Aselected imagerytasksasscalpmaps.Band-powerwascalculatedinthefrequency
subject-specificfrequencybandisshadedingray.Thesecondrowshowsthe bandthatisshowninthetopmostrowandaveragedacrossthetimeinterval
averageamplitudeenvelopeofthatfrequencybandwith0beingthetime thatisindicatedinthemiddlerow.Threeofthosesevendatasetshavebeen
pointofcuepresentation.Thetimeintervalwhichwasusedtocalculatethe artificiallygenerated,seemaintext.
competitiondataset.Foreachparticipant,anindividualchannel, CSPwascombinedwithafilterbank.Acriterionbasedonmutual
timeinterval,andfrequencybandwasselectedtodisplaythedif- information was used to select those features that were to be
ferentialmodulationsoftheSMRs.Class-wiseaveragedfrequency fedintoaradialbasisfunctionbasedneuralnetwork.Usingthis
spectraareplottedintheupperrow.Thesecondrowshowsthe approach, they obtained a mean squared error (MSE) of 0.382
timecourseofband-poweraveragedacrossalltrials.Thebottom- (averaged across the four real data sets). For further details of
mostrowdisplaysthedifferenceinlogband-powerbetweenthe theirmethodsee(Zhangetal.,2012).Thewinnersareveryclosely
twomotorimageryconditionsasscalptopographies. followed by Dieter Devlaminck and colleagues from the Uni-
Datasetsc,d,andewereartificiallygenerated. versity of Ghent, from the Psychiatric Institute of Guislain and
|     |     |     |     |     |     |     |     | from the | University | Hospital |     | Ghent, | who | obtained an | MSE of |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | -------- | --- | ------ | --- | ----------- | ------ |
3.4. CHALLENGE 0.383.Theyemployedmulti-classCSPwithasubject-specificfre-
|     |     |     |     |     |     |     |     | quency band | and | a multi-class |     | support | vector | machine | (SVM) |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------- | --- | ------- | ------ | ------- | ----- |
Thesubmissionswereevaluatedinviewofaonedimensionalcur-
sorcontrolapplicationwithrangefrom−1to1.Thementalstate withordinalregression.Theresultsranked3rdto5thhavebeen
of class one is used to position the cursor at −1,and the men- achievedbyKaiKengAnnandcolleagues(InstituteforInfocomm
talstateof classtwoisusedtopositionthecursornear1.Inthe Research,Singapore); Liu Guangquan and colleagues (Shanghai
absenceofthosementalstates(intermittingintervals)thecursor JiaoTongUniversity,China),andAbdulSattiandcolleagues(Uni-
shouldbeatposition0.Notethatitisunknowntothecompetitors versity of Ulster). All those three competitors also used CSP as
atwhichintervalsthesubjectisinadefinedmentalstate.Com- a pivotal step in combination with a filter bank (rank 3) or
petitors had to submit classifier outputs for all time points. To withasubject-specificfrequencyband(ranks4and5).Figure5
measure the performance,the squared error with respect to the shows histograms of the results of those five highest ranked
| targetvector–thatis−1forclassone,1forclasstwo,and0other- |     |     |     |     |     |     |     | submissions. |     |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
wise–averagedacrosstimepointswascalculated.Sincethemental Toassesstheresults,ithastobetakenintoaccountthataclas-
stateof theuserdoesnotabruptlychangewithcueappearance, sifier that gives the constant output zero has an MSE of about
timepointsduringtransientperiods(1sstartingfromeachcue) 0.5. The exact value varies between data sets since the length
werediscardedfromevaluation. of the motor imagery and no-control period was chosen ran-
Asstatedabove,itwasdeclaredthatforcompetitionpurpose, domly. Figure6 gives a more detailed view on the performance
onlyresultsfortherealdatasetswereconsidered,butresultsfor of thewinningalgorithm.Itshowsforthefourdatasets(rows)
artificialdatawerealsoreportedforcomparison. normalized histograms of the classifier outputs – separately for
|     |     |     |     |     |     |     |     | periods of | the three | mental | states. |     | In the | left column | the true |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ------ | ------- | --- | ------ | ----------- | -------- |
Additionally,participantswereaskedtooptionallyjudgewhich
−1
ofthedatasetsweretheartificiallygeneratedones. label is (first motor imagery class), in the middle column
|     |     |     |     |     |     |     |     | the true | label is   | 0 (no | control | intention), |         | and in the  | right col- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ----- | ------- | ----------- | ------- | ----------- | ---------- |
|     |     |     |     |     |     |     |     | umn the  | true label | is 1  | (second | motor       | imagery | condition). | The        |
3.5. OUTCOMEINBRIEF
There were 24 submissions to data set 1. The winning team is value of the true label is indicated by a blue triangle in each
ZhangHaihongandcolleaguesfromtheInstituteforInfocomm subplot. This figure makes clear that this data set poses really a
Research, Singapore. They approached the task as a three class big challenge. Even for the best method among 24 submissions,
|     |     |     |     |     |     |     |     | the results | are not | very | satisfying. | Interestingly, |     | the no-control |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ---- | ----------- | -------------- | --- | -------------- | --- |
problemwiththerestclassbeingthethirdclass.Forclassification,
FrontiersinNeuroscience|Neuroprosthetics July2012|Volume6|Article55|6

Tangermannetal. ReviewoftheBCIcompetitionIV
stateisquitewelldetectedintheseconddataset(participantb). mentalstate(bluebars)andtheclassifieroutputof thewinning
The overall best performance was achieved in the forth data set algorithm(redline).
(participantg). Aguessonthequestionwhichdatasetswereartificiallygen-
Figure7givesabetterintuitionofhowwelltheobtainedcon- erated was submitted by 16 out of 23 competitors. The correct
trol actually is. It shows for a selected segment of 100s the true categorization was revealed by two competitors (Astrid Zeman
and Manuel Moebius), 8 more competitors revealed 2 of the 3
artificialsubjects,butoneof thosealsoconsideredonerealdata
setasartificial.
a
0.5 b
f 4. DATASET1(ARTIFICIALLYGENERATED)
0.45 g The subset of Data set 1 that was artificially generated is pro-
videdbyC.VidaurreandG.NoltefromBerlin(Germany).Itcan
0.4
befreelyassessedviahttp://www.bbci.de/competition/iv/withthe
0.35 only restriction that the present article is referenced upon any
publicationofresults.
0.3
4.1. MOTIVATION
0.25
TheBCIcompetitionIVincludedanoriginalingredientcompared
topastevents:partofthedatasetsoftheBBCIgroupwereartifi-
0.2
ciallygenerated.Themotivationofthisworkwastocheckwhether
rank1 rank2 rank3 rank4 rank5
ornotEEGdatacanbecreatedtohavespecificpropertiesinorder
to test new machine learning methods. If this was the case,the
FIGURE5|(Dataset1–histogramofresults).Performanceofthefirst
fiverankedsubmissionsisshownintermsoftheirmeansquarederror algorithms applied to both,synthetic and real EEG,would pro-
(MSE)wrt.thetruelabels.Onlyresultsforthereal(i.e.,notartificially ducecomparableresults.Totestthishypothesisweanalyzedthe
generated)datasetsareshown.Themeanacrossthefourdatasetsis rankingoftheparticipantsandtheperformanceofthemethodsin
plottedasahorizontalredline.TheMSEforconstantpredictionoutputof0
realandsyntheticEEG.BraindatalikeEEGisoftennoisyandits
are0.507,0.515,0.491,0.524fordatasetsa,b,f,g,respectively.
variablescannotbecontrolledeasily.Syntheticallygenerateddata
)404.0=ESM(
a
)224.0=ESM(
b
)614.0=ESM(
f
−1 0 1
)782.0=ESM(
g
−1 0 1 −1 0 1
FIGURE6|(Dataset1–distributionofclassifieroutputs).These columnisahistogramforthosetimepointsinwhichthetruelabelis−1,for
(normalized)histogramsdisplaythedistributionoftheclassifieroutputsofthe themiddlecolumnitis0(nocontrol),andfortherightcolumnitis1.Thetrue
winningalgorithm.Eachrowcorrespondstoonedataset(a,b,f,g).Theleft labelisindicatedbythebluetriangle.
www.frontiersin.org July2012|Volume6|Article55|7

| Tangermannetal. |     |     |     |     |     |     |     |     | ReviewoftheBCIcompetitionIV |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- |
1
0.5
0
−0.5
−1
|     |     | 1300 | 1310 | 1320 | 1330 | 1340 | 1350 1360 | 1370 1380 | 1390 1400 |     |     |
| --- | --- | ---- | ---- | ---- | ---- | ---- | --------- | --------- | --------- | --- | --- |
time  [s]
FIGURE7|(Dataset1–traceofclassifieroutputs).Thelabelsof selectedsegmentof100stakenfromdatasetginwhichthe
thetruementalstatearedisplayedinblue.Theredlineshowsthe classificationisquitesuccessful.TheMSEintheshownsegment
| classifieroutputsofthewinningalgorithm.Thisexampleisa |     |     |     |     |     |     | is0.171. |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
mayovercomethesedifficulties,andbesidesitiseasyandcheapto withA(f)definedbythedecomposition1 C(f)=A(f)A(f) † with
†denotingtransposeandcomplexconjugation:
produce.
| 4.2. MATERIAL     |     |        |            |     |              |         | y(f)=A(f)x(f) |     |     |     | (2) |
| ----------------- | --- | ------ | ---------- | --- | ------------ | ------- | ------------- | --- | --- | --- | --- |
| In the following, | the | single | components | of  | (artificial) | EEG are |               |     |     |     |     |
described separately. We start with the generation of artificial Finally,thesimulatednoisedatainthechanneli iscalculatedas
EEG noise, which we divided into background noise and base- theinverseFouriertransformofy(f).Theresultingbackground
i
line drifts. Then we describe the generation of the µ (and β as noise was a superposition of different amounts of each type of
| afirstharmonicof | µ)rhythmanditsdesynchronization(ERD) |     |     |     |     |     |     |     |     |     |     |
| ---------------- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
noise,dependingonthecondition.Figure8depictsnoiseincon-
duetotheonsetof motorimagerytasks.Afterthat,wedescribe ditionseyesopenandeyesclosed atthe10-Hzfrequency.Onecan
theartifactsthathavebeenaddedtothedata(eyeblinksandeye observethatthepoweratthisfrequencyisvaryingintheoccipital
movements)toincludesomemorerealisticnoiseinoursignals. region,asexpectedinrealEEGdata.
| OursyntheticEEGiscomputedasasuperpositionof |     |     |     |     |     | potentials |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
from these three different systems (ongoing background noise, 4.2.2. Baselinedrifts
taskdependentrhythmicactivitygeneratedonthemotorcortex Baseline drifts are typically observable in unfiltered electroen-
andeyerelatednoise,eyeblinks,andeyemovements)whichhave
|     |     |     |     |     |     |     | cephalographic | signals (cf. Simons | et al., 1981; Henninghausen |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------------------- | --------------------------- | --- | --- |
qualitativelydifferentstatisticalandspatialproperties. etal.,1993)andthisisalsothecasefortheBCI-competitiondata.
Afteranalyzingthereal“raw”EEGofthecompetition,weobserved
4.2.1. Backgroundnoise both,relativelyfastandslowdriftsofthesignal(showninFigure9)
BackgroundnoiseinEEGcanreasonablybeassumedtobeGauss-
andaccordinglycreatedtwotypesofartificialdrifts.Thesedrifts
iandistributed.Thespatialandtemporalcharacteristics,however, weregeneratedusingthecross-spectrumofthebackgroundnoise,
areingeneraltoocomplextobeadequatelymodeledusingasim- butsimulatingahighersamplingfrequency,whichhadtheeffectof
| ple parametric | model | (Huizenga | et  | al.,2002; | Bijma | et al.,2003; |     |     |     |     |     |
| -------------- | ----- | --------- | --- | --------- | ----- | ------------ | --- | --- | --- | --- | --- |
producingaslowersignal(noise)thanthebackgrounditself.The
| Freeman, | 2004a,b, 2005, | 2006). | To  | solve this | difficulty, | we first |     |     |     |     |     |
| -------- | -------------- | ------ | --- | ---------- | ----------- | -------- | --- | --- | --- | --- | --- |
selectedfrequenciesforthiscomputationwere150and300kHz,
estimatedthecross-spectrumfromrealEEGdataineyesopenand respectively(theoriginalsamplingfrequencywas1kHz).
eyesclosedconditionsandthengeneratedanarbitraryamountof
dataaccordingtotheestimated(complex)cross-spectralmatrix
|     |     |     |     |     |     |     | 4.2.3. Event-relateddesynchronization |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- |
inthefollowingway: ForwardcalculationForthegenerationofERDweassumedfixed
Letx (f)betheFouriertransformofsimulatedwhiteGaussian spatialpatternscalculatedaspotentialmapsfromdipolarsources
i
| noiseforN | datapointsforchanneli |     |     | withi=1...M.Sincetyp- |     |     |             |                       |                    |          |     |
| --------- | --------------------- | --- | --- | --------------------- | --- | --- | ----------- | --------------------- | ------------------ | -------- | --- |
|           |                       |     |     |                       |     |     | within left | and right motor areas | (Geselowitz,1967). | Again,we |     |
ically(andinthecaseofourdata)theestimatedcross-spectrum
assumedthatthedataisGaussiandistributed.Thefrequencycon-
C(f i ) at discrete frequencies f i is based on averages of relatively tent,however,wasrestrictedtoasinglefrequency(chosentobe
shorttimewindows(duration:1s)andN denotesthelengthof 12Hz)withawidthδf=1Hz.Weassumedthatthegeneratorsof
| the complete | data set,the | frequency |     | resolution | of the | measured |     |     |     |     |     |
| ------------ | ------------ | --------- | --- | ---------- | ------ | -------- | --- | --- | --- | --- | --- |
thisrhythmwereradialdipoleswiththeoriginstobe3cmbelow
cross-spectraismuchlowerthanthefrequencyresolutionofx i (f). electrodes C3 and C4 for the left and right side activity,respec-
WeestimateC(f)asalinearinterpolation: tively (see Figures 10 and 11). The directions“radial”and also
“below”werechosenaccordingtothesurfacenormalsatelectrodes
| (cid:0) (cid:1)≡= | f −f | (cid:0) (cid:1)+ | f −f (cid:0) | (cid:1) |     |     |     |     |     |     |     |
| ----------------- | ---- | ---------------- | ------------ | ------- | --- | --- | --- | --- | --- | --- | --- |
C f 1 C f 2 C f (1) C3 and C4. For the forward calculation we assumed a realistic
|     | −f  | 1   | −f  | 2   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
f 2 1 f 2 1 volume conductor consisting of three shells (scalp,skull,brain)
| with f 1 | (f 2 ) being | the largest | (smallest) | value | of  | the set (f) | i   |     |     |     |     |
| -------- | ------------ | ----------- | ---------- | ----- | --- | ----------- | --- | --- | --- | --- | --- |
(f),...,x
lower(higher)thanf.Thenwescalex≡(x 1 (f),x 2 M (f))T 1Thedecompositionisnotuniquebutanywilldo.
FrontiersinNeuroscience|Neuroprosthetics July2012|Volume6|Article55|8

| Tangermannetal. |     |     |     |                                          |     |     | ReviewoftheBCIcompetitionIV |     |
| --------------- | --- | --- | --- | ---------------------------------------- | --- | --- | --------------------------- | --- |
|                 |     |     |     | 4.2.4. Harmonicoscillationsinthebetaband |     |     |                             |     |
Aharmoniccomponentofthesubject-specificµrhythmcanoften
beobservedintheβband(Huberetal.,1971;Pfurtscheller,1981;
Pfurtschelleretal.,1996;PfurtschellerandLopesdaSilva,1999;
|     |     |     |     | Carlqvist | et al., 2004; Nikulin | et al., | 2007). In our | data sets we |
| --- | --- | --- | --- | --------- | --------------------- | ------- | ------------- | ------------ |
haveincludedsuchaharmoniccomponentwithdifferentlevelsof
amplitudeinrelationtotheµrhythm,varyingfrom15to1%(see
Figure12).
|     |     |     |     | 4.2.5. Asymmetryintheamplitudeoftherhythms |     |     |     |     |
| --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- |
Typically,onecanobservesomeasymmetryinthestrengthofthe
|     |     |     |     | desynchronizationineachof |     | thehemispheres(McFarlandetal., |     |     |
| --- | --- | --- | --- | ------------------------- | --- | ------------------------------ | --- | --- |
2000;MazaheriandJensen,2008;Nikulinetal.,2010).Inapairof
datasetsandinordertocreateamorerealisticEEGweaddedthis
asymmetryintherhythmsthatwegenerated.
|     |     |     |     | 4.2.6. Generationofartifacts |     |     |     |     |
| --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- |
Bothforeyeblinksandeyemovementsweassumedthegenerators
tobecurrentdipolesplacedwithintheeyes.Thedipolesintheleft
andrighteyewereactivatedsimultaneouslyinarandomlychosen
superpositionofaverticalandhorizontaldirection.Thepotentials
FIGURE8|(DataSet1–artificial).Left:spectraofthesignalatallchannel duetoverticaldipoleswereonaverage10timesstrongerthanthe
locationsforthetwoconditions,eyesopenandeyesclosed.Right:scalp
onesfromhorizontaldirection.Thetopographiesofverticaland
plotofthesignalpowerat10Hzforthetwoconditions(eyesopenand
horizontaldipolesareshownintheupperpanelsofFigure13.
closed).Theactualnoiseoftheartificialdatavariedlinearlyintimebetween
Whilethespatialpatternswere(onaverage)identicalforeye
bothconditions,dependingofthetaskoftheBCIuser.
|     |     |     |     | movement | and eye blinks, | the time | courses were | chosen differ- |
| --- | --- | --- | --- | -------- | --------------- | -------- | ------------ | -------------- |
ently.Timecoursesofeyemovementsweremodeledasconstants
withcontinuouson-andoffsetsasshowninthelowerleftpanelof
  Figure13.Thedurationoftheconstantwassetrandomlybetween
100
0and2s.
Thetimecourseofeyeblinkswaschosenas
80
|     |     |     |     |         | (cid:18) t2 | (cid:19) |     |     |
| --- | --- | --- | --- | ------- | ----------- | -------- | --- | --- |
|     |     |     |     | x(t)=(t | +ξ)exp      |          |     |     |
|     |     |     |     |         | −           |          |     | (3) |
| 60  |     |     |     |         | 2σ2         |          |     |     |
t
stlov µ
σ =31ms
| 40  |     |     |     | with a width                                            | set to t | according | to real | eye blinks and |
| --- | --- | --- | --- | ------------------------------------------------------- | -------- | --------- | ------- | -------------- |
|     |     |     |     | withxi beingaGaussiandistributedrandomvariablewithstan- |          |           |         |                |
Slow Baseline drift darddeviationequalto20ms.Anexampletimecourseisgivenin
20
thelowerrightpanelofFigure13.
0
|     |     | Fast Baseline drift |     | 4.2.7. Combiningtheingredients |     |     |     |     |
| --- | --- | ------------------- | --- | ------------------------------ | --- | --- | --- | --- |
Foreachdataset,thefinalEEGwasgeneratedbythelinearcom-
−20
|         |         |         |         | binationofeachelement(backgroundnoise,baselinedrifts,ERD, |     |     |     |     |
| ------- | ------- | ------- | ------- | --------------------------------------------------------- | --- | --- | --- | --- |
| 870 880 | 890 900 | 910 920 | 930 940 | 950                                                       |     |     |     |     |
|         |         | Time    |         | andeyeartifacts).Thebackgroundnoisewasasuperpositionof    |     |     |     |     |
thecross-spectraintheconditionseyesopenandeyesclosed.The
|     |     |     |     | amount of | each type of cross-spectrum |     | depended | on the“envi- |
| --- | --- | --- | --- | --------- | --------------------------- | --- | -------- | ------------ |
FIGURE9|(DataSet1–artificial).Exampleoffastandslowbaseline
driftsthatareobservableinunfilteredBCIcompetitionIVdata.Thefigure ronmental”conditionsinwhichthevirtualuserwassupposedto
depictsthetimecourseoftheamplitudeoftheEEGinonechannel. be immersed: visual load (large amount of eyes open condition
|                   |                  |             |           | andsmallamountof | eyesclosed                          | condition),auditiveload(small |     |            |
| ----------------- | ---------------- | ----------- | --------- | ---------------- | ----------------------------------- | ----------------------------- | --- | ---------- |
|                   |                  |             |           | amountof         | eyesopen conditionandlargeramountof |                               |     | eyesclosed |
| with conductivity | ratios 1:0.02:1. | The Maxwell | equations | were condition). |                                     |                               |     |            |
solved using an analytic expansion of the EEG lead field (Nolte The ERD frequency was randomly chosen between 10 and
andDassios,2005). 12Hz for each user and a harmonic in the beta band (by dou-
blingtheµrhythmfrequency)wasaddedaswell.Thepositionof
| Both left | and right rhythmic | activity | was present in | all con- |     |     |     |     |
| --------- | ------------------ | -------- | -------------- | -------- | --- | --- | --- | --- |
ditions. However, during left hand movements the right side thedipolesgeneratingtheoscillatoryactivitycouldvaryslightly
rhythmicactivitywasreducedbyatleast50%(itchangedslightly andrandomlyforeachuser.Asalreadydescribed,wealsoallowed
asymmetryoftheµrhythmamplitudeineachhemisphere.
foreachdataset)andviceversa.
| www.frontiersin.org |     |     |     |     |     |     | July2012|Volume6|Article55|9 |     |
| ------------------- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- |

Tangermannetal. ReviewoftheBCIcompetitionIV
FIGURE10|(DataSet1–artificial).Locationanddirectionofselecteddipolesinthehead.
Thentheeyemovementsandeyeblinkswereaswellsuperim-
posedto thesignal. One randomtime coursewas generatedfor
eachofthedatasets.Finally,thebaselinedriftswereaddedtothe
total.
For the calculation, each element (ERD, background noise,
etc.)wasnormalizedbyitstraceandthecoefficientmultiplying
eachof themwasmanuallyselected,bycomputingtheexpected
performance using baseline methods (frequency band and time
intervalsubject-selected,thenCSPcomputedusingtrainingdata
and applied to test data). For more information please refer to
(Blankertzetal.,2008b).
4.3. CHALLENGE
FIGURE11|(DataSet1–artificial).Powertopographiesattheµrhythm
Asitwasnotrevealedwhichofthedatasetswererealandwhich
frequencygeneratedbythedipoles.
wereartificiallygenerated.Thechallengeandevaluationcriterion
wasidentical,seeSection3.4.
positivebias(0.02),whichshowsthattheperformancemeasure-
4.4. OUTCOMEINBRIEF ment(meansquarederror)wasslightlyhigherforthesynthetic
A comparison of the similarity of real and synthetic data EEG(thesedatasetswereabitnoisierthantherealones).
was performed based on the result ranking (available via Summarizing,thosealgorithmsdoingwellintherealdatasets
http://bbci.de/competition/iv/results/). First, we analyzed the alsoperformedhigherintheartificialdataandviceversa.
positionoftheparticipantsintheranking.Wecalculatedthecor-
relation coefficient of the participants’ positions in both of the 4.5. DISCUSSION
datasetsandobtainedaresultof0.89,meaningthattheposition In this section we gave a description of the generation of syn-
of a participant in both rankings was highly correlated: a good thetic EEG. We have described all its components,documented
rankintherealdataanalysisyieldedagoodrankintheartificial ourdecisions,anddetailedthecalculationofeachelement.
data analysis and vice versa. Also,we analyzed the performance We emphasize that more sophisticated EEG forward models
of the participants in the same way. We obtained a correlation wouldincludeCSFasafourthlayerandthatnewresearchindicates
coefficientof0.93,meaningthattheperformanceofaparticipant thatthechosenconductivityratio(1:50)mightbetoohigh.While
inbothdatasetswasverysimilar.Thelinearfittinghadaslight thesimulationcouldbeimproved,almostallBCImethodswork
FrontiersinNeuroscience|Neuroprosthetics July2012|Volume6|Article55|10

| Tangermannetal. |     |     |     |     | ReviewoftheBCIcompetitionIV |
| --------------- | --- | --- | --- | --- | --------------------------- |
entirelyinsensorspaceandtheexactdetailsofthetopographies data under controlled conditions,in order to test new methods
willhardlyaffecttheresultsoftheBCItask. beforeperformingactualexperimentsandthiswayboostingthe
We have analyzed the results of the BCI competition IV and probabilityofsuccessofnewanalysismethodsinneuroscience.
shownthehighcorrelationbetweentherankingandtheperfor- Inthefuturewewillworkontheimprovementoftheartifact
mancemeasureintherealandartificialEEGinFigure14.Inthis generation methods and develop an automatic way to combine
specificcontext,thecreationofsyntheticEEGdatasetshasproven allthecomponentsofoursyntheticelectroencephalogram.Addi-
tobeuseful. tionally,moretestsshouldbedonewiththeartificiallygenerated
ArtificiallygeneratedEEGcanbegeneratedinlargeamounts. data,toassurethatthecorrelationbetweenrealandsyntheticEEG
Usingitnotonlyavoidsperformingrealrecordings,itcanalsobe isashighasshowninthisreport.
| fine-tuned, e.g.,to | contain a controlled | amount of certain | arti- |     |     |
| ------------------- | -------------------- | ----------------- | ----- | --- | --- |
facts.Bothcharacteristicsarebeneficialforaninitialperformance
5. DATASET2A
evaluationofnewalgorithmicmethods. Data set 2a Continuous Multi-class Motor Imagery is provided
Althoughthiswasourfirsttrytogenerateartificialdataandthe
byC.Brunner,R.Leeb,G.R.Müller-Putz,G.Pfurtscheller,and
methodscanbefurtherdeveloped,wehaveshownawaytocreate

| C3  | CFC6 | left |     |     |     |
| --- | ---- | ---- | --- | --- | --- |
right
sgn r2
0.1
 +
|     |     |  5 dB | 0   |     |     |
| --- | --- | ----- | --- | --- | --- |
10 Hz
−0.1
FIGURE12|(DataSet1–artificial).SpectraoftheEEGsignalintwo
discriminativechannels.Thediscriminabilitybetweentheclassesisshown
FIGURE13|(DataSet1–artificial).Toprow:scalpplotsofoneeye
atthebottomofeachspectrum.ThisFigureillustratesanexampleof
movementandoneeyeblinkgeneratedforthesyntheticEEGdatasetsof
asymmetryoftheµrhythmpeakineachhemisphere.Alsotheharmonicof theBCIcompetitionIV.Bottomrow:correspondingtimecourseofeye
| theµrhythmisobservableinthebetaband. |                 |     | movementsandblinks. |     |     |
| ------------------------------------ | --------------- | --- | ------------------- | --- | --- |
|                                      | 24              |     |                     |     |     |
|                                      | y=1.402+0.888*x |     | 1.3                 |     |     |
|                                      | 22              |     | y = 0.0169+0.8803*x |     |     |
|                                      | R = 0.888       |     | 1.2                 |     |     |
|                                      | 20              |     | R = 0.9338          |     |     |
1.1
18
|     | GEE laicifitrA knaR |     | GEE laicifitrA ESM 1 |     |     |
| --- | ------------------- | --- | -------------------- | --- | --- |
16
0.9
14
0.8
12
|     | 10  |     | 0.7 |     |     |
| --- | --- | --- | --- | --- | --- |
0.6
8
|     | 6   |               | 0.5       |              |     |
| --- | --- | ------------- | --------- | ------------ | --- |
|     | 4   |               | 0.4       |              |     |
|     | 2   |               | 0.3       |              |     |
|     |     |               |   0.4 0.6 | 0.8 1        | 1.2 |
|     | 5   | 10 15         | 20        |              |     |
|     |     | Rank Real EEG |           | MSE Real EEG |     |
FIGURE14|(DataSet1–artificial).Linearregressionoftherankposition(left)andperformanceofthemethod(right).Thex-axiscorrespondstotheresults
submittedfortherealEEGdatasets,whereasy-axiscorrespondstothoseofthesyntheticEEG.
| www.frontiersin.org |     |     |     |     | July2012|Volume6|Article55|11 |
| ------------------- | --- | --- | --- | --- | ----------------------------- |

Tangermannetal. ReviewoftheBCIcompetitionIV
A. Schlögl from Graz (Austria). It can be freely assessed via Figure17,left.Allsignalswererecordedmonopolarlywiththeleft
http://www.bbci.de/competition/iv/withtheonlyrestrictionthat mastoidservingasreferenceandtherightmastoidasground.The
thepresentarticleisreferenceduponanypublicationofresults. signalsweresampledwith250Hzandbandpassfilteredbetween
0.5and100Hz.Thesensitivityoftheamplifierwassetto100µV.
5.1. MOTIVATION Anadditional50Hznotchfilterwasenabledtosuppresslinenoise.
Thisdatasetchallengesthesession-to-sessiontransferofathree Inadditiontothe22EEGchannels,3monopolarEOGchannels
classmotorimagerytask.Comparedtoothersynchronousmotor wererecordedandalsosampledwith250Hz(seeFigure17,right).
imagerydatasets,acontinuousestimationofmotorimageryclass Theywerebandpassfilteredbetween0.5and100Hz(withthe50-
labelsisrequired.Thisrepresentsarealisticsettingforanonline Hznotchfilterenabled),andthesensitivityof theamplifierwas
controlofacontinuousoutputparameter. setto1mV.TheEOGchannelsareprovidedforthesubsequent
applicationofartifactprocessingmethods(Fatourechietal.,2007)
5.2. MATERIALSANDSUBJECTS andmustnotbeusedforclassification.
Thisdatasetcompriseselectroencephalographic(EEG)datafrom Avisualinspectionofalldatasetswascarriedoutbyanexpert
9subjects. andtrialscontainingartifactsweremarked.Eightoutofthetotal
ofninedatasetswereanalyzedinNaeemetal.(2006)andBrunner
5.2.1. Experimentalparadigm etal.(2007,2011).
The cue-based BCI paradigm consisted of four different motor Alldatasetsarestoredinthegeneraldataformatforbiomed-
imagery tasks,namely the imagination of movement of the left icalsignals(GDF),onefilepersubjectandsession.However,only
hand(class1),righthand(class2),bothfeet(class3),andtongue onesessioncontainstheclasslabelsforalltrials,whereastheother
(class 4). Two sessions on different days were recorded for each sessions are used to test the classifier and hence to evaluate the
subject. Each session is comprised of 6 runs separated by short performance.Fordetailsonthedataset,theGDFfilescontained,
breaks.Onerunconsistsof48trials(12foreachofthefourpossible markersandfunctionsprovidedforloadingandevaluation,please
classes),yieldingatotalof288trialspersession. seeSectionA.1inAppendix.
5.2.2. Protocol 5.4. CHALLENGE
Atthebeginningofeachsession,werecordedapproximately5min Participantswereaskedtoprovideacontinuousclassificationout-
of EEG data to estimate the EOG influence. This recording was put for each sample in the form of class labels (1–4),including
dividedinto3blocks:(1)2minwitheyesopen(lookingatafix- labeledtrialsandtrialsmarkedasartifact.Aconfusionmatrixwas
ation cross on the screen), (2) 1min with eyes closed, and (3) then built from all artifact-free trials for each time point. From
1minwitheyemovements.Thetimingschemeofonesessionis theseconfusionmatrices,thetimecourseoftheaccuracyaswell
illustratedinFigure15.Notethatduetotechnicalproblems,the asthekappacoefficientwasobtained(Schlögletal.,2007b).The
EOGblockisshorterforsubjectA04Tandcontainsonlytheeye
chancelevelwasatκ=0.Thealgorithmusedforthisevaluation
movement condition (see Table A1 inAppendix for a list of all wasprovidedinBioSig.Thealgorithmachievingthelargestkappa
subjects). valuewasdeclaredthewinner.
All subjects were sitting in a comfortable armchair in front Duetothefactthatthetestdatasetswerenotdistributeduntil
of acomputerscreen.Atthebeginningof atrial(t=0s),afix- theendofthecompetition,softwarehadtobesubmitted.Ithad
ation cross appeared on the black screen. In addition, a short tobecapabletoprocessEEGdatafilesofthesameformatasused
acousticwarningtonewaspresented.After2s(t=2s),acuein foralltrainingsets2)andproducetheaforementionedclasslabel
theformof anarrowpointingeithertotheleft,right,down,or vector.
up(correspondingtooneofthefourclasseslefthand,righthand, Since three EOG channels were provided, the software was
foot, or tongue) appeared and stayed on the screen for 1.25s. requiredtoremoveEOGartifactsbeforethesubsequentdatapro-
Thispromptedthesubjectstoperformthedesiredmotorimagery cessingusingartifactremovaltechniquessuchashighpassfiltering
task.Nofeedbackwasprovided.Thesubjectswereinstructedto
carry out the motor imagery task until the fixation cross disap-
2Onetestdatasetisdistributedfromthebeginningofthecompetitiontoenable
pearedfromthescreenatt=6s.Ashortbreakwithablackscreen
participantstotesttheirprogramandtoensurethatitproducesthedesiredoutput.
followed.TheparadigmisillustratedinFigure16.
5.3. DATAFORMAT
Twenty-twoAg/AgClelectrodes(withinter-electrodedistancesof
3.5cm) were used to record the EEG; the montage is shown in
FIGURE15|(DataSet2a).Timingschemeofonesession. FIGURE16|(DataSet2a).Timingschemeoftheparadigm.
FrontiersinNeuroscience|Neuroprosthetics July2012|Volume6|Article55|12

| Tangermannetal. |     |     |     |     |     | ReviewoftheBCIcompetitionIV |     |
| --------------- | --- | --- | --- | --- | --- | --------------------------- | --- |
FIGURE17|(DataSet2a).Left:electrodemontagecorrespondingtotheinternational10–20system.Right:electrodemontageofthethreemonopolarEOG
channels.
orlinearregression(Schlögletal.,2007a).Theuseof othercor- Table3|(DataSet2a).Contributionswithfinalresult(kappa).
rectionmethodswaspossible,butitwasrequestedthatartifacts
hadnoinfluenceontheclassificationresults. Contributor Kappa Lab
| All algorithms    | had to be                          | causal, meaning | that the classifica- |              |                                        |                        |                                |
| ----------------- | ---------------------------------- | --------------- | -------------------- | ------------ | -------------------------------------- | ---------------------- | ------------------------------ |
|                   |                                    |                 |                      | K.K.Ang 0.57 | InstituteforInfocommResearch,Agencyfor |                        |                                |
| tionoutputattimek | wasallowedonlytodependonthecurrent |                 |                      |              |                                        |                        |                                |
|                   |                                    |                 |                      |              | S c ie n c e , Te                      | c h n o lo g y a n d R | e s e a r c h S i n g a p o re |
| and past samples  | x ,x ,...,x                        | . In order      | to check whether     | the          |                                        |                        |                                |
k k−1 0 L.Guangquan 0.52 S ch o o l o f M e c h a n ic a l E ng in e e r i n g , S h a n g h a i
causalitycriterionandtheartifactprocessingrequirementswere
JiaoTongUniversity,China
| fulfilled, all submissions | had        | to be open  | source, including | all         |                                       |     |     |
| -------------------------- | ---------- | ----------- | ----------------- | ----------- | ------------------------------------- | --- | --- |
|                            |            |             |                   | W.Song 0.31 | CollegeofInf.ScienceandTechn.,Beijing |     |     |
| additional libraries,      | compilers, | programming | languages,        | and so      |                                       |     |     |
NormalUniversity,ChinaandNationalKey
on(forexample,Octave/FreeMat,C++,Python,etc.).Notethat
Lab.orCog.Neurosc.andLearning,Beijing
submissionscouldalsobewrittenintheclosed-sourcedevelop-
NormalUniv.,China
mentenvironmentMATLABaslongasthecodewasexecutablein
|     |     |     |     | D.Coyle 0.30 | IntelligentSystemsResearchCentre,School |     |     |
| --- | --- | --- | --- | ------------ | --------------------------------------- | --- | --- |
Octave.Similarly,C++programscouldbewrittenandcompiled
ofComputingandIntell.Systems,Facultyof
withaMicrosoftorIntelcompiler,butthecodehadtocompile
| alsowithg++. |     |     |     |     | ComputingandEng.,MageeCampus, |     |     |
| ------------ | --- | --- | --- | --- | ----------------------------- | --- | --- |
UniversityofUlster,UK
|                     |     |     |     | J.Wu 0.29 | NationalKeyLab.forCogn.Neurosc.and   |     |     |
| ------------------- | --- | --- | --- | --------- | ------------------------------------ | --- | --- |
| 5.5. OUTCOMEINBRIEF |     |     |     |           | Learning,BeijingNormalUniv.,Chinaand |     |     |
Therewerefivesubmissionsforthisdataset(seeTable3).Allof CollegeofInf.ScienceandTechn.,Beijing
themusedCSPfeatures.Thewinningalgorithmwassubmittedby NormalUniversity,China
K.K.Ang,Z.Y.Chin,C.Wang,C.Guan,H.Zhang,K.S.Phua,
B.Hamadicharef,andK.P.TeefromtheInstituteforInfocomm
Research,AgencyforScience,TechnologyandResearchSingapore. isbasedonthefilterbankcommonspatialpattern(FBCSP)vari-
Detailsof theirapproacharedescribedinAngetal.(2012).The ant (Ang et al., 2008). It was extended to the multi-class case
performancemeasurekappawas0.57averagedoverallninesub- with one-versus-the-rest classifiers. First,artifacts were removed
jects. The other four submissions attained kappa values of 0.52, by bandpass filters. Each classifier selected discriminative CSP
0.31,0.30,and0.29andthuswerewellabovechancelevelofκ=0. features using the Mutual Information Best Individual Features
Thewinningalgorithmperformedbestinsevenoutofninesub- (MIBIF4) algorithm (Ang and Quek, 2006) before Naive Bayes
jects;intwosubjects,thealgorithmthatoverallrankedsecondbest ParzenWindowclassifiers(AngandQuek,2006)wereused.The
reachedevenslightlyhigherkappavalues. classifier with the highest probability yielded the overall classi-
The winning algorithm requires MATLAB, but also runs on ficationresult.Duetothecomputationallyintensivealgorithms,
Octave.ItusestheBioSigtoolboxtoloadthedata.Thealgorithm classification was performed every ten samples (in combination
| www.frontiersin.org |     |     |     |     |     | July2012|Volume6|Article55|13 |     |
| ------------------- | --- | --- | --- | --- | --- | ----------------------------- | --- |

| Tangermannetal. |     |     |     |     |     |     |     |     |     |     |     | ReviewoftheBCIcompetitionIV |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- |
withazero-orderholdforthesamplesinbetween).Asthealgo-
rithmused2sofEEGdata,theclassificationoutputwasdelayed
by2s.
5.6. DISCUSSION
FIGURE18|(DataSet2b).Timingschemeofonesession(forscreening
| All five | submissions | yielded | results | well | above | chance | level. As |     |     |     |     |     |     |     |     |
| -------- | ----------- | ------- | ------- | ---- | ----- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
andfeedbacksessions).
| a side note, | four | contributions |     | were submitted |     | by Asian-Pacific |     |     |     |     |     |     |     |     |     |
| ------------ | ---- | ------------- | --- | -------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
groups.Asalreadymentionedabove,allcontributionsusedCSP
features.
Thereweretwomajorchallengesinthisdataset.First,thecon-
taminationwitheyemovementartifactscouldaffectclassification
accuracy;thereforeweprovidedadditionalEOGchannels.Second,
theclassifierstrainedonthetrainingsessionsshouldgeneralizeon
unseendatarecordedonadifferentday.Thewinningalgorithm
addressedthefirstissuewithasimplebandpassfilter.Obviously,
themethodisstablebecauseityieldedgoodresultsonthetestdata.
However,theclassificationoutputisdelayedby2s,whichcould
beaprobleminonlineBCIsthatincorporatereal-timefeedback.
6. DATASET2B
| Data set       | 2b Session-to-Session |                  |     | Transfer    | of a Motor | Imagery | BCI   |     |     |     |     |     |     |     |     |
| -------------- | --------------------- | ---------------- | --- | ----------- | ---------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| under Presence |                       | of Eye Artifacts |     | is provided | by R.      | Leeb,C. | Brun- |     |     |     |     |     |     |     |     |
ner,G.R.Müller-Putz,andG.PfurtschellerfromGraz(Austria).
It can be freely assessed via http://www.bbci.de/competition/iv/ FIGURE19|(DataSet2b).Electrodemontageofthethreemonopolar
| withtheonlyrestrictionthatthepresentarticleisreferencedupon |     |     |     |     |     |     |     | EOGchannels. |     |     |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
anypublicationofresults.
wasperformedtoestimatetheEOGinfluence.Therecordingwas
6.1. MOTIVATION
dividedinto3blocks:(1)2minwitheyesopen(lookingatafix-
Thisdatasetfocusesontheclassificationofelectroencephalogram
(EEG) signals affected by eye movement artifacts. Furthermore ation cross on the screen), (2) 1min with eyes closed, and (3)
|     |     |     |     |     |     |     |     | 1min with | eye movements. |     | The | artifact | block was | divided | into |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | --- | --- | -------- | --------- | ------- | ---- |
thesession-to-sessiontransferofthealgorithmshastobetakenin
|     |     |     |     |     |     |     |     | four sections | (15s | artifacts | with | 5s resting | in between) |     | and the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | --------- | ---- | ---------- | ----------- | --- | ------- |
consideration,becausealltrainingandtestdatasetsarerecorded
|     |     |     |     |     |     |     |     | subjects | were instructed | with | a text | on  | the monitor | to  | perform |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | ---- | ------ | --- | ----------- | --- | ------- |
onfivedifferentdays.
eithereyeblinking,rolling,up-down,orleft-rightmovements.At
Thedataset2bcontainstheelectroencephalogram(EEG)and
thebeginningandattheendofeachtaskalowandhighwarning
| electrooculogram |     | (EOG) | activity | of nine | subjects. | Technically |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | ----- | -------- | ------- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tonewerepresented,respectively.Notethatduetotechnicalprob-
| speaking, | each | data set | consists | of single-trials |     | of spontaneous |     |     |     |     |     |     |     |     |     |
| --------- | ---- | -------- | -------- | ---------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
brain activity during motor imagery, one part labeled (training lemsnoEOGblockisavailableinsessionB0102TandB0504E(see
TableA3inAppendixforalistofallsubjects).
data)andanotherpartunlabeled(testdata),andaperformance
measure.Thegoalistoinferlabels(ortheirprobabilities)forthe
|     |     |     |     |     |     |     |     | 6.2.2. Protocol |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
testdatasetsfromtrainingdatathatmaximizetheperformance
|             |         |                   |     |                 |          |              |        | Three bipolar | recordings |     | (C3, Cz, | and            | C4) were | recorded      | with |
| ----------- | ------- | ----------------- | --- | --------------- | -------- | ------------ | ------ | ------------- | ---------- | --- | -------- | -------------- | -------- | ------------- | ---- |
| measure     | for the | true (but         | to  | the competitors | unknown) |              | labels |               |            |     |          |                |          |               |      |
|             |         |                   |     |                 |          |              |        | a sampling    | frequency  | of  | 250Hz.   | The recordings |          | had a dynamic |      |
| of the test | data    | (this information |     | is now,after    | the      | competition, |        |               |            |     |          |                |          |               |      |
rangeof±100µVforthescreeningand±50µVforthefeedback
availableaswell).
sessions.Theywerebandpassfilteredbetween0.5and100Hz,and
6.2. MATERIALSANDSUBJECTS a notch filter at 50Hz was enabled. The placement of the three
bipolarrecordings(largeorsmalldistances,moreanteriororpos-
| This data | set consists |     | of EEG | data from | 9 subjects | of  | a study |     |     |     |     |     |     |     |     |
| --------- | ------------ | --- | ------ | --------- | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
terior)wereslightlydifferentforeachsubject(formoredetailssee
publishedinLeebetal.(2007).Thesubjectswereright-handed,
hadnormalorcorrected-to-normalvisionandwerepaidforpar- Leebetal.,2007).TheelectrodepositionFzservedasEEGground.
InadditiontotheEEGchannels,theelectrooculogram(EOG)
| ticipating | in the   | experiments. |             | All volunteers | were   | sitting       | in an |              |      |       |           |            |     |             |     |
| ---------- | -------- | ------------ | ----------- | -------------- | ------ | ------------- | ----- | ------------ | ---- | ----- | --------- | ---------- | --- | ----------- | --- |
|            |          |              |             |                |        |               |       | was recorded | with | three | monopolar | electrodes |     | (see Figure | 19, |
| armchair,  | watching | a            | flat screen | monitor        | placed | approximately |       |              |      |       |           |            |     |             |     |
1m away at eye level. For each subject 5 sessions are provided, left mastoid serving as reference) using the same amplifier set-
wherebythefirsttwosessionscontaintrainingdatawithoutfeed- tings, but with a dynamic range of ±1mV. The EOG channels
|                      |     |     |          |                |      |          |      | are provided | for         | the subsequent |              | application | of artifact |        | process- |
| -------------------- | --- | --- | -------- | -------------- | ---- | -------- | ---- | ------------ | ----------- | -------------- | ------------ | ----------- | ----------- | ------ | -------- |
| back (screening),and |     |     | the last | three sessions | were | recorded | with |              |             |                |              |             |             |        |          |
|                      |     |     |          |                |      |          |      | ing methods  | (Fatourechi |                | et al.,2007) | and         | must        | not be | used for |
feedback.
classification.
6.2.1. Experimentalparadigm Thecue-basedscreeningparadigm(seeFigure20A)consisted
Eachsessionconsistsof severalruns,illustratedinFigure18.At oftwoclasses,namelythemotorimagery(MI)oflefthand(class1)
thebeginningofeachsession,arecordingofapproximately5min andrighthand(class2).Eachsubjectparticipatedintwoscreening
FrontiersinNeuroscience|Neuroprosthetics July2012|Volume6|Article55|14

Tangermannetal. ReviewoftheBCIcompetitionIV
A Screening
Imagination of
left hand movement
Imagination of
right hand movement
beep
Fixation cross Cue Imagery Period Pause
0 1 2 3 4 5 6 7 8 9
time in s
B Smiley Feedback
beep
Cue
Smiley (grey) Feedback Period (Smiley) Pause
0 1 2 3 4 5 6 7 8 9 time in s
FIGURE20|(DataSet2b).Timingschemeoftheparadigm.(A)Thefirsttwosessions(01T,02T)containtrainingdatawithoutfeedback,and(B)thelastthree
sessions(03T,04E,05E)withsmileyfeedback.
sessionswithoutfeedbackrecordedontwodifferentdayswithin accordingtotheintegratedclassificationoutputoverthepast2s
2weeks.Eachsessionconsistedofsixrunswithtentrialseachand (moredetailsseeLeebetal.,2007).Furthermore,theclassifierout-
twoclassesofimagery.Thisresultedin20trialsperrunand120 putwasalsomappedtothecurvatureof themouthcausingthe
trials per session. Data of 120 repetitions of each MI class were smileytobehappy(cornersofthemouthupwards)orsad(cor-
availableforeachpersonintotal.Priortothefirstmotorimagery nersofthemouthdownward).Atsecond7.5thescreenwentblank
trainingthesubjectexecutedandimagineddifferentmovements andarandomintervalbetween1.0and2.0swasaddedtothetrial.
foreachbodypartandselectedtheonewhichtheycouldimagine Thesubjectwasinstructedtokeepthesmileyonthecorrectside
best(e.g.,squeezingaballorpullingabrake). foraslongaspossibleandthereforetoperformtheMIaslongas
Eachtrialstartedwithafixationcrossandanadditionalshort possible.
acousticwarningtone(1kHz,70ms).Somesecondslateravisual
cue(anarrowpointingeithertotheleftorright,accordingtothe 6.3. DATAFORMAT
requested class) was presented for 1.25s.Afterward the subjects Alldatasetsarestoredinthegeneraldataformatforbiomedical
hadtoimaginethecorrespondinghandmovementoveraperiod signals(GDF),onefilepersubjectandsession.However,onlythe
of 4s. Each trial was followed by a short break of at least 1.5s. first three sessions contain the class labels for all trials,whereas
Arandomizedtimeof upto1swasaddedtothebreaktoavoid theremainingtwosessionsareusedtotesttheclassifierandhence
adaptation. toevaluatetheperformance.Fordetailsonthedataset,theGDF
For the three online feedback sessions four runs with smi- filescontained,markersandfunctionsprovidedforloadingand
ley feedback were recorded (see Figure 20B),whereby each run evaluation,pleaseseeSectionA.2inAppendix.
consistedoftwentytrialsforeachtypeofmotorimagery.Atthe
beginningofeachtrial(second0)thefeedback(agraysmiley)was 6.4. CHALLENGE
centeredonthescreen.Atsecond2,ashortwarningbeep(1kHz, Participantswereaskedtoprovideacontinuousclassificationout-
70ms)wasgiven.Thecuewaspresentedfromseconds3to7.5. put for each sample in the form of class labels (1,2),including
Depending on the cue, the subjects were required to move the labeled trials and trials marked as artifacts. A confusion matrix
smileytowardtheleftorrightsidebyimaginingleftorrighthand wasthenbuiltbasedonartifact-freetrialsonlyandforeachtime
movements,respectively.Duringthefeedbackperiodthesmiley point.Fromtheseconfusionmatrices,thetimecourseoftheaccu-
changedtogreenwhenmovedinthecorrectdirection,otherwise racyaswellasthekappacoefficientwasobtained(Schlögletal.,
itbecamered.Thedistanceofthesmileyfromtheoriginwasset 2007b), which had a chance level of κ=0. The algorithm used
www.frontiersin.org July2012|Volume6|Article55|15

Tangermannetal. ReviewoftheBCIcompetitionIV
for this evaluation was provided in BioSig. The winner was the CSP (FBCSP) using mutual information rough set reduction
algorithmwiththelargestkappavalue. (MIRSR).ClassificationofselectedCSPfeatureswasperformed
Duetothefactthattheevaluationdatasetswerenotdistributed usingtheNaïveBayesParzenWindowclassifier.Amoredetailed
untiltheendofthecompetition,softwarehadtobesubmitted.It explanationofthewinningalgorithmisgiveninaseparatepaper
hadtobecapabletoprocessEEGdatafilesofthesameformatas (Angetal.,2012).
usedforalltrainingsets3)andproducetheaforementionedclass Methods participant ID-2: The EEG was bandpass filtered in
labelvector. differentfrequencybandsandtheEOGartifactswereremoved
Since three EOG channels were provided, the software was afterward. Common spatial subspace decomposition (CSSD)
requiredtoremoveEOGartifactsbeforethesubsequentdatapro- wereextractedfromthepreprocessedsignalswithoptimizedwin-
cessingusingartifactremovaltechniquessuchashighpassfiltering dowsizesandaLDAdiscriminatefunctionwasmadeforeach
orlinearregression(Schlögletal.,2007a).Theuseof othercor- timepoint.
rectionmethodswaspossible,butitwasrequestedthatartifacts MethodsparticipantID-3:CSPonspectrallyfilteredneuraltime
hadnoinfluenceontheclassificationresults. seriespredictionpreprocessing(NTSPP)signalswasappliedto
Allalgorithmswererequiredtobecausal,meaningthattheclas- allsignalsallsubjectsusingtheself-organizingfuzzyneuralnet-
sificationoutputattimek mayonlydependonthecurrentand work (SOFNN). Furthermore the log variance of each filtered
pastsamplesx k ,x k−1 ,...,x 0 .Inordertocheckwhetherthecausal- channelwascalculatedwitha1-sslidingwindow.Thebestclas-
itycriterionandtheartifactprocessingrequirementswerefulfilled, sifieramong3variantsofLDAand2variantsofSVMwaschosen
allsubmissionshadtobesubmittedasopensource,includingall foreachsubjectindividually.
additional libraries, compilers, programming languages, and so MethodsparticipantID-4:Waveletpackettransformwasapplied
on(forexample,Octave/FreeMat,C++,Python,etc.).Notethat only on electrodes C3 and C4 (Cz was ignored). Selected
submissionscouldalsobewrittenintheclosed-sourcedevelop- frequency bands were extracted and concatenated to form a
mentenvironmentMATLABaslongasthecodewasexecutablein multidimensionalvectorandclassifiedwithLDA.
Octave.Similarly,C++programscouldbewrittenandcompiled MethodsparticipantID-5:EOGwasremovedwithlinearregres-
withaMicrosoftorIntelcompiler,butthecodehadtocompile sionandthesignalshighpassfilteredwith4Hz.Thealgorithm
alsowithg++. usedspectralfeaturesinthemuandbetabands(fromelectrode
C3andC4)asinputsforaneuralnetworkclassifier.
6.5. SUBMISSIONSANDALGORITHMS MethodsparticipantID-6:EOGwasremovedwithlinearregres-
Sixgroupssubmittedtheirparticipationforthisdataset.Thegiven sion.Band-powerfeaturesin75frequencybandsforeachchannel
listisinwinningorderandthisIDwillbeusedfurtheron: were extracted and selected with recursive feature elimination
(RFE).Theremaining6featureswereclassifiedwithaBayesian
ID-1:ZhengYangChin,KaiKengAng,ChuanchuWang,Cuntai LDA.
Guan,HaihongZhang,KokSoonPhua,BrahimHamadicharef,
and Keng Peng Tee from the Institute for Infocomm Research, 6.6. RESULTS
AgencyforScience,Technology,andResearchinSingapore. In total six submissions were received and most were of high
ID-2:HuangGan,LiuGuangquan,andZhuXiangyangfromthe quality. As defined above in section evaluation the kappa value
SchoolofMechanicalEngineering,ShanghaiJiaoTongUniversity waschosenastheperformancemeasure.Remember,theexpected
inChina. kappavalue,ifclassificationismadebychance,is0.InTable4the
ID-3:Damien Coyle,Abdul Satti,and Martin McGinnity from firstcolumnshowstheaveragekappaacrossallsubjects,columns
the Intelligent Systems Research Centre,School of Computing 2–10showtheresultsfortheindividualsubjects.Foursubmissions
andIntelligentSystems,FacultyofComputingandEngineering, achievedameankappaofmorethan0.4onthetestset.Further-
MageeCampus,UniversityofUlsterintheUnitedKingdom. morethetwobestapproaches(ID-1andID-2;Angetal.,2012)
ID-4:ShaunLodderandJohanduPreezfromtheE&EEngineer- achievednearlysimilarresults(meanof 0.60and0.58).Actually
ing,UniversityofStellenboschinSouthAfrica. approachID-2couldachievethebestsinglesubjectperformances
ID-5:JaimeFernandoDelgadoSaafromtheRobóticaySistemas for4subjectsandID-1“just”for3subjects,butwasalwaysvery
Inteligentes,UniversidaddelNorteinColombia. close to the best ones on a single subject level. Only subject 2
ID-6:YangPing,XuLei,andYaoDezhongfromthePerception- causedtroublestothesealgorithms.Interestinglyisthatapproach
Motor Interaction Lab,School of Life Science and Technology, ID-4achievedincrediblegoodresultsherecomparedtotheother
UniversityofElectronicScienceandTechnologyinChina. approaches.Generallythedatafromsubject8andsubject4could
beidentifiedbest,wherebysubjects3,2,and1werechallenging.
Foreachmethodtheappliedpreprocessing,featureextraction, Thesefindingsareconsistentoverallapproaches,ifthestandard
andclassificationstepsarebrieflygiven. deviationovertheapproachesistakenintoconsideration.
MethodsparticipantID-1:TheyauthorsremovedtheEOGwith
6.7. DISCUSSION
a bandpass filter and extracted their features via a Filter Bank Twomajorchallengeshadtobeaddressedinthisdataset.Thefirst
onewastheinfluenceofeyemovementartifactsontheEEGand
3Onetestdatasetisdistributedfromthebeginningofthecompetitiontoenable thesecondonethegeneralizationoftheselectedfeaturestobesuc-
participantstotesttheirprogramandtoensurethatitproducesthedesiredoutput. cessfulonthesession-to-sessiontransfer.Likeinrealconditions
FrontiersinNeuroscience|Neuroprosthetics July2012|Volume6|Article55|16

| Tangermannetal. |     |     |     |     |     |     |     | ReviewoftheBCIcompetitionIV |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- |
Table4|(DataSet2b).DetailedresultsfromtheBCIcompetitionIV.
| Part.ID | Mean |      |      |      |      | Subject |      |      |      |      |
| ------- | ---- | ---- | ---- | ---- | ---- | ------- | ---- | ---- | ---- | ---- |
|         |      | 1    | 2    | 3    | 4    | 5       | 6    | 7    | 8    | 9    |
| ID-1    | 0.60 | 0.40 | 0.21 | 0.22 | 0.95 | 0.86    | 0.61 | 0.56 | 0.85 | 0.74 |
| ID-2    | 0.58 | 0.43 | 0.21 | 0.14 | 0.94 | 0.71    | 0.62 | 0.61 | 0.84 | 0.78 |
| ID-3    | 0.46 | 0.19 | 0.12 | 0.12 | 0.77 | 0.57    | 0.49 | 0.38 | 0.85 | 0.61 |
| ID-4    | 0.43 | 0.23 | 0.31 | 0.07 | 0.91 | 0.24    | 0.43 | 0.41 | 0.74 | 0.53 |
| ID-5    | 0.37 | 0.20 | 0.16 | 0.16 | 0.73 | 0.21    | 0.21 | 0.39 | 0.86 | 0.44 |
| ID-6    | 0.25 | 0.02 | 0.09 | 0.07 | 0.43 | 0.25    | 0.00 | 0.14 | 0.76 | 0.47 |
Kappavaluesforeachsubjectandthemeankappaforallparticipatinggroups.
thedatawerefromdifferentsessionsrecordedondifferentdays. An intuitive way to realize a brain-machine interface (BMI) is
Lookingattheresultsitisinterestingtocomparetheperformance toaccesstheneuralcorticalactivitythatcontrollednaturalhand
achievedondatasetsofdifferentsubjects,whileapplyingthesame movements and translate this activity into commands that pro-
signalprocessingalgorithms.Nomethodachievedgoodresultson duceequivalentmovementsofexternaleffectors(e.g.,prosthetic
allsubjects.Especiallythesession-to-sessiontransfercouldhave arm/hand,computercursor).SuchdirectmotorBMIsrequirethat
beenasourcefortheoccurredproblems.Althoughweprovided kinematicparametersofthemovement(e.g.,movementdirection
trainingdatasetsfromthreedifferentdays,2trainingdatasetswere orvelocity)canbeinferredfromthemeasuredneuronalsignals.
recordedwithoutfeedbackandjust1datasetwithfeedbackwere OnlinedirectmotorBMIshaveuntilrecentlyonlybeenreal-
given,butofcoursewewantedtoseetheperformanceononline ized using spiking activity [single- (SUA) or multi-unit activity
datasetswithfeedbackrecordedlaterondifferentdays.Thewin- (MUA), e.g., Hochberg et al., 2006; Velliste et al., 2008]. Only
ningalgorithmscouldfosterthisproblembest,butunfortunately in the last decade, it has been shown that not only spiking
their method needed a 2-s delay to the predicted classification but also neuronal population activity (Figure 21) is tuned to
output to achieve a better performance. This approach is very the direction of hand movements. Tuning of neuronal popu-
usefulifofflineclassificationisperformed,butforonlinecontrol lation signals has been demonstrated in several studies using
applicationssuchadelaycausesalotofproblemsfortheBCIuser. either(a)invasiverecordings(localfieldpotentials,LFP;Mehring
Like in all the BCI competitions before,the data set and the et al., 2003) and electrocorticogram (ECoG; Leuthardt et al.,
descriptionwillcontinuetobeavailableonthecompetitionweb 2004;Schalketal.,2007;Pistohletal.,2008)or(b)non-invasive
pagehttp://www.bbci.de/competition/iv/.Otherresearchersinter- recordings (electroencephalogram, EEG; Hammon et al., 2008;
estedinEEGsingle-trialanalysisarewelcometotesttheiralgo- Waldertetal.,2008;Bradberryetal.,2010;Lvetal.,2010;Wang
rithms on these data sets and to report their results. To imitate and Makeig, 2010) and magnetoencephalogram (MEG; Geor-
competition conditions, all selections of method, features, and gopoulos et al., 2005; Waldert et al., 2008; Bradberry et al.,
modelparametersmustbeconfinedtothetrainingsets.However, 2009; Wang et al., 2010). Very recently, online direct motor
duetothecurrentavailabilityofthelabelsofthetestdataandthe BMI control based on decoding movement direction was real-
publicationof thoroughanalysesof thesedata,futureclassifica- izedusingMEG(Witteetal.,2010)andECoG(Milekovicetal.,
| tionresultsofthecompetitiondatacannotfairlybecomparedto |     |     |     |     | 2012). |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
theoriginalsubmissions. Amongallthesestudies,intra-corticalrecordings(SUA,MUA,
|     |     |     |     |     | LFP) | yield the highest | amount | of information | to be extracted |     |
| --- | --- | --- | --- | --- | ---- | ----------------- | ------ | -------------- | --------------- | --- |
7. DATASET3 aboutmovementdirection(Waldertetal.,2009).However,these
signalsrequiretheimplantationofmicro-electrodesintothecor-
| Data set 3 | Directionally | modulated | MEG activity | is provided by |     |     |     |     |     |     |
| ---------- | ------------- | --------- | ------------ | -------------- | --- | --- | --- | --- | --- | --- |
S. Waldert, C. Braun, H. Preissl, N. Birbaumer,A. Aertsen, and tex and long-term stable recording of spiking activity remains
C. Mehring from Freiburg (Germany), Tübingen (Germany), a difficult problem. Non-invasive EEG and MEG provide less
Trento (Italy), and London (UK). It was recorded in a col- information,butallowforaneasyaccesstohumanneuralactivity
laboration of the Institute of Biology I, the Bernstein Center withoutanymedicalriskforthesubject.Obviously,currentMEG
Freiburg (both at the University of Freiburg), the MEG-Center systemscannotbeabasisforreal-worlddirectmotorBMI.How-
andtheInstituteofMedicalPsychologyandBehavioralNeurobi- ever, MEG is convenient for BMI training and rehabilitation
|     |     |     |     |     | attempts | in patients | (e.g., in | stroke patients; | Buch et al., | 2008). |
| --- | --- | --- | --- | --- | -------- | ----------- | --------- | ---------------- | ------------ | ------ |
ology(bothUniversityofTübingen).Itcanbefreelyaccessedvia
http://www.bbci.de/competition/iv/withtheonlyrestrictionthat In this context, optimized algorithms for inferring kinematic
the present article as well as (Waldert et al.,2008) is referenced parameters from MEG signals could facilitate BMI training and
uponanypublicationofresults. increasetheperformanceofnon-invasivedirectmotorBMIs.To
encouragethedevelopmentofnewalgorithms,wecontributedto
7.1. BACKGROUND theBCIcompetitionIVadatasetcontainingMEGsignalsrecorded
Spinal injury patients rank the loss of hand function as one of whilesubjectsperformedhand/wristmovementsinfourdifferent
| the most debilitating |     | features of their | injury (Anderson, | 2004). | directions. |     |     |                               |     |     |
| --------------------- | --- | ----------------- | ----------------- | ------ | ----------- | --- | --- | ----------------------------- | --- | --- |
| www.frontiersin.org   |     |                   |                   |        |             |     |     | July2012|Volume6|Article55|17 |     |     |

| Tangermannetal. |     |     |     |     |     |     |     |     | ReviewoftheBCIcompetitionIV |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- |
FIGURE21|(DataSet3).SchematicoverviewofdifferentrecordingtechniquesforBMIs(fromWaldertetal.,2009withpermission).
7.2. MATERIALSANDSUBJECT
| The data | set contained | the signals | of  | 10 MEG | sensors | (VSM |     |     |     |     |
| -------- | ------------- | ----------- | --- | ------ | ------- | ---- | --- | --- | --- | --- |
MedTech,Vancouver)abovecentralareasmeasuredat625Hzsam-
| plingrateduringwristmovementsof |     |     |     | twohealthy,right-handed |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
subjects.ThesubjectsatrelaxedinanMEGchair,theelbowrested
onapillowtopreventupperarmandshouldermovements,and
theheadwasstabilizedbysmallpillows.Thetaskwastomovea
joystickfromacentralrestingpositiontowardoneoffourtargets
| (right,left,forward,backward) |     |     | using exclusively |     | the right | hand |     |     |     |     |
| ----------------------------- | --- | --- | ----------------- | --- | --------- | ---- | --- | --- | --- | --- |
andwrist.Movementamplitudewas4.5cm.Ineachtrial,thetar-
| get was self-chosen | by the         | subject,i.e.,no |      | directional |     | visual cue |     |     |     |     |
| ------------------- | -------------- | --------------- | ---- | ----------- | --- | ---------- | --- | --- | --- | --- |
| was provided.       | Visual trigger | signals         | were | presented   | on  | a screen   |     |     |     |     |
infrontofthesubjecttostartatrialortoindicatepossibletime
violations.Atrialstartedwiththejoystickinthecenterposition FIGURE22|(DataSet3).Timecourseofatrialwithtimeconstraints(from
Waldertetal.,2008withpermission).
| andtheappearanceof | agraycircle.Afteravariabledelay(1–2s, |     |     |     |     |     |     |     |     |     |
| ------------------ | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure22),thedisappearanceofthecircleindicatedthe“go”sig-
nal(cuedmovementonset).Then,within0.75sthesubjecthad
tostartthemovementandreachthetarget.Foratrialtobevalid, inapseudo-randomorder.Thenumberof trialspermovement
|             |             |         |            |        |       |           | direction | was unequal | but similar. The movement | directions of |
| ----------- | ----------- | ------- | ---------- | ------ | ----- | --------- | --------- | ----------- | ------------------------- | ------------- |
| the subject | also had to | rest at | the target | for at | least | 1s. These |           |             |                           |               |
thesetesttrialswerenotgivenbuthadtobepredictedfromthe
| time constraints | allowed | for temporal |     | consistency | across | trials |     |     |     |     |
| ---------------- | ------- | ------------ | --- | ----------- | ------ | ------ | --- | --- | --- | --- |
MEGsignalsandsubmittedtothecompetition.Basedonthesub-
| and the hold | period at | the target | prevented | interference |     | of in- |                                           |     |     |                 |
| ------------ | --------- | ---------- | --------- | ------------ | --- | ------ | ----------------------------------------- | --- | --- | --------------- |
|              |           |            |           |              |     |        | mittedlabels,wecalculatedtheperformanceof |     |     | thecompetitor’s |
andoutwardmovements.Aredcrosswaspresentedcontinuously
algorithmsasthepercentageofcorrectlyclassifiedtrials(decoding
forfixation.
accuracy).
7.3. DATAFORMATANDPERFORMANCECRITERIA
Trialswerecuttocontaindatafrom0.4sbeforeto0.6saftermove- 7.4. SUBMISSIONSANDALGORITHMS
mentonset.Thesignalswereband-passfiltered(0.5–100Hz)and Wereceivedfoursubmissions(ID-1toID-4)forthisdataset.The
resampledat400Hz. submissionshowingbestperformancewaswellabovechancelevel
ThedatawereprovidedastwoMatlab“mat”-files,forsubject fortheunlabeledtestdata.Itwassubmittedby
one“S1.mat”andforsubjecttwo“S2.mat.”Both filescontained ID-1:SepidehHajipourSardouie,MohammadBagherSham-
the variable Info, which provided a detailed description of the sollahi. Biomedical Signal and Image Processing Lab (BiSIPL),
data.Thesecondvariable,training_data,contained40labeledtri- Schoolof ElectricalEngineering,Sharif Univ.of Techn.,Tehran,
| als per movement | direction. | These | 160 | trials were | provided |     | to Iran. |     |     |     |
| ---------------- | ---------- | ----- | --- | ----------- | -------- | --- | -------- | --- | --- | --- |
train and evaluate the decoding algorithms. The third variable, Thefollowingshortsummaryoftheappliedalgorithmsisbased
test_data,contained74(forS-1)or73(forS-2)unlabeledtrials onthedescriptionsprovidedbythecompetitors:
FrontiersinNeuroscience|Neuroprosthetics July2012|Volume6|Article55|18

| Tangermannetal. |                 |             |     |                |     |           |            |     |     | ReviewoftheBCIcompetitionIV |     |     |
| --------------- | --------------- | ----------- | --- | -------------- | --- | --------- | ---------- | --- | --- | --------------------------- | --- | --- |
| ID-1:           | A comprehensive |             | set | of statistical |     | features, | frequency- |     |     |                             |     |     |
| domain          | features        | and wavelet |     | coefficients   | was | extracted | from 12    |     |     |                             |     |     |
channels(10realchannelsplus2artificialbipolarchannels).The
| number | of features | was | reduced | using | a supervised |     | algorithm. |     |     |     |     |     |
| ------ | ----------- | --- | ------- | ----- | ------------ | --- | ---------- | --- | --- | --- | --- | --- |
Then,ageneticalgorithmselectedfeaturestooptimizetheclas-
sificationaccuracy.Theclassifierconsistedofacombinationofa
| linearSVMandLDA.Detailsof |     |     |     | thisalgorithmarepublishedin |     |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
(SardouieandShamsollahi,2012).
ID-2:First,alow-passfilter(cutoff8Hz)wasusedtofilterthe
timesignal.Secondly,thetimesegment(0–0.5s)wasselected,that
| is points | 160–360. | Third,the |     | first three | and | five principal | com- |     |     |     |     |     |
| --------- | -------- | --------- | --- | ----------- | --- | -------------- | ---- | --- | --- | --- | --- | --- |
ponentsoftheabsandangleofthe128FFTofeachchanneland
eachsamplewereused.Then,Fisherdiscriminantanalysis(FDA)
| was applied | to  | the frequency |     | features | to reduce | the | dimension- |     |     |     |     |     |
| ----------- | --- | ------------- | --- | -------- | --------- | --- | ---------- | --- | --- | --- | --- | --- |
ality.Fourthly,thesignalweresubsampledto20Hz.Then,FDA
wasappliedtothetimefeaturestoreducedimensionality.Finally,
| Fisher discriminant |     | functions |     | were used | for | classification | using |     |     |     |     |     |
| ------------------- | --- | --------- | --- | --------- | --- | -------------- | ----- | --- | --- | --- | --- | --- |
thecombinationoftimeandfrequencyfeatures.
ID-3:Preprocessingunknown.Thefeaturesetconsistedofsta-
FIGURE23|(DataSet3).ResultsoftheBCIcompetitionIVand,for
| tistical, | temporal, | parametric |     | and wavelet |     | coefficients | and was |     |     |     |     |     |
| --------- | --------- | ---------- | --- | ----------- | --- | ------------ | ------- | --- | --- | --- | --- | --- |
comparison,theaverageresultofapplyingaRLDAandlinearSVMtothe
reducedbyPCAandageneticalgorithm.Theclassifierwasalinear
low-passfilteredandresampledactivityofthedata.
SVM.
| ID-4: | First, a | low-pass | filter | (cutoff | 8Hz) | was | used to filter |     |     |     |     |     |
| ----- | -------- | -------- | ------ | ------- | ---- | --- | -------------- | --- | --- | --- | --- | --- |
thetimesignal.Secondly,thetimesegment(0–0.5s)wasselected, higher average accuracy of 53% (significantly higher than ID-
that is points 160–360. Third, the first three and five principal 2/3/4(p<0.01),notsignificantlyhigherthanID-1,Fisher’sexact
test).
| components | of  | the abs | and angle | of  | the 128 | FFT of | each chan- |     |     |     |     |     |
| ---------- | --- | ------- | --------- | --- | ------- | ------ | ---------- | --- | --- | --- | --- | --- |
nelandeachsamplewereused.Then,FDAwasappliedtoreduce ID-2andID-4obtainedmuchhigheraccuraciesonthetraining
dimensionality. Finally,Fisher discriminant functions were used data(98%and73%)thanforthetestdata,whichwasclassifiedat
chancelevel.Thisresultindicatesthatthelowaccuraciesforthe
forclassificationusingthefrequencyfeature.
testdataareduetoapoorgeneralization.Possiblythesamereason
7.5. OUTCOME explainsthelowaccuracyforID-3.However,theperformanceon
AllcontributorsappliedeitherlinearSVM,thelinearFisherdis- thetrainingdatawasnotavailableforthisgroup.
|     |     |     |     |     |     |     |     | Compared | to the results | of the winning | group (ID-1), | the |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | -------------- | ------------- | --- |
criminantanalysis(LDA),oracombinationofboth.Algorithms
mainlydifferedinfeatureselection.Threecompetitors(ID-2/3/4) higher(RLDA)andequal(SVM)accuraciesforthetwostandard
achieveddecodingaccuraciesaroundchancelevelof25%onlyfor linearclassifierswithoutsophisticatedfeatureselectionmightbe
explainedbythefactthatthelow-passfilteredactivity–whichwas
thetestdata(seeFigure23).
The winner applied a combined linear discriminant analysis usedin(Waldertetal.,2008)andwhichwas,duetotheapplied
(LDA) and linear support vector machine (SVM) on features band-passfilter(0.5–100Hz,seeDataFormat),alsoavailableinthe
selected from a large feature set by scattering matrices and a datasetcontributedtotheBCIcompetition–wasnotincluded
inthepredefinedfeaturesetusedbythewinninggroup.Itisnot
| genetic | algorithm. | The | feature | set comprised |     | features | extracted |     |     |     |     |     |
| ------- | ---------- | --- | ------- | ------------- | --- | -------- | --------- | --- | --- | --- | --- | --- |
fromthetimedomain(e.g.,ARcoefficients,formfactor),thefre- clear which decoding accuracies could have been achieved with
quencydomain(e.g.,energyindifferentfrequencybands,mean thealgorithmof thecompetitionwinnerif thelow-passfiltered
activitywereincluded.Especiallythissignalcomponentcontains
frequency),andthetime-frequencydomain(waveletcoefficients),
but not the low-pass filtered signals that were used in (Waldert substantialinformationaboutmovementkinematicsandprovides
et al., 2008). Obtained accuracies on the test data were 59.5% highperformancefordecodingofneuralpopulationsignals:LFP
and 34.3% for subjects 1 and 2, respectively, and 46.9% on (Mehring et al.,2003; Rickert et al.,2005),ECoG (Schalk et al.,
|     |     |     |     |     |     |     |     | 2007; Pistohl | et al.,2008; | Ball et al.,2009),EEG | (Waldert | et al., |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------------ | --------------------- | -------- | ------- |
average.
|     |     |     |     |     |     |     |     | 2008; Bradberry | et al., 2010; | Lv et al., 2010; | Wang and | Makeig, |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------------- | ---------------- | -------- | ------- |
7.6. DISCUSSION 2010),andMEG(Jerbietal.,2007;Waldertetal.,2008;Bradberry
etal.,2009;Wangetal.,2010).
| The performance |     | of the | competitors |     | algorithms | was | lower than |     |     |     |     |     |
| --------------- | --- | ------ | ----------- | --- | ---------- | --- | ---------- | --- | --- | --- | --- | --- |
thatofanestablisheddecodingalgorithm:theapplicationofareg-
| ularizedlineardiscriminantanalysis(RLDA,alsousedinWaldert |     |     |     |     |     |     |     | 8. DATASET4 |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
etal.,2008)tothelow-passfilteredandresampledsignalsofthe Dataset4FingerMovementsinECoG isprovidedbyK.J.Miller
BCI-competition data resulted in a significantly higher average and G. Schalk from Seattle andAlbany (USA). The data set can
accuracy of 62% (average across both subjects; p<0.01 com- befreelyassessedviahttp://www.bbci.de/competition/iv/withthe
pared to the competition winner ID-1,Fisher’s exact test). Also only restriction that the present article is referenced upon any
a linear SVM using the same low-pass filtered signals yielded a publicationofresults.
| www.frontiersin.org |     |     |     |     |     |     |     |     |     | July2012|Volume6|Article55|19 |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- |

Tangermannetal. ReviewoftheBCIcompetitionIV
8.1. MOTIVATION inthiscontext,because,asanareathatisevolutionarilyspecial-
The goal for data set 4 of the BCI competition IV was to infer izedfortooluse,itmayprovideanintuitivebasisforcontrolling
the flexion of individual fingers from signals recorded from the prosthetichandsorothermanipulandums.
surfaceof thebrain(electrocorticography,ECoG).Comparedto Electrocorticography(ECoG)isthemeasurementofmesoscale
EEG,whereahigherspatialblurringpreventsthedetailedlocal- electricpotentials(1–5mm)fromthesubduralbrainsurface.In
izationinsingletrialonthefingerlevel,theECoGsignalsprovide thedatasetprovidedfortheBCIcompetition,allthreesubjects
a much higher spatial resolution. This data set contained ECoG whoparticipatedwereepilepticpatientsreceivingECoGmonitor-
signalsfromthreesubjects,aswellasthetimecoursesoftheflex- ingforthelocalizationofseizurefoci(Figure24).Inthissetting,
ion of each of five fingers. The task in the competition was to ECoGhasproventobeapowerfultoolforbrain-computerinter-
use the ECoG signals and flexion information in a training set facing(Leuthardtetal.,2004;Schalketal.,2008),andcapableof
topredictfingerflexionforaprovidedtestset.Theperformance augmentingactivityinthebrain(Milleretal.,2010).
of that prediction was evaluated by calculating the average cor- Several features can be extracted from the ECoG data that
relationcoefficientr betweenactualandpredictedfingerflexion. maycorrelatewithbehavior.Motor-relatedevent-relatedpoten-
Wereceivedfivesubmissionsforthisdataset.Theresultsofthese tials can be extracted from the raw time series (Figure 25D).A
submissionsandrecentlypublishedstudiesdemonstratethatthe runningaverageoftherawsignal,termedthelocalmotorpoten-
timinganddegreeoffingerflexioncanbeaccuratelyinferredfrom tial(LMP;Schalketal.,2007)hasbeenshowntobeinformative
ECoGinsingletrials. about task-related brain activity in motor cortex (Schalk et al.,
Finger flexion is a simple parameter to correlate with an 2007; Kubanek et al., 2009; Figure 26). In addition, frequency-
extracted brain state, and thus can serve as a good test bed for domain features have been shown to robustly capture shifts in
algorithmdevelopment.Therearemanypotentialimplicationsof behavioralstate(Croneetal.,1998a,b;Milleretal.,2007).Shifts
successfulalgorithmicdecodingof brainstates:neuralprosthet- indifferentfrequencyrangesoftenhavedifferentspatialpatterns.
ics,communicationdevices,handicappedvehiclecontrol(wheel- Thereisacharacteristicdecreaseinpoweratlowfrequenciesand
chairs,etc.),andpotentiallyrehabilitationofthebrain.Theuseof increaseinpowerathighfrequenciesthataccompaniesmovement
motorareasrelatedtohandmovementsisparticularlycompelling (Figure27).Thedecreasesinlowfrequencypowerhavespatially
FIGURE24|(DataSet4).TheECoGsignalsintrain_data(time,channel)andtest_data(time,channel)wereacquiredfromeachelectrodewithrespecttoa
scalpreferenceandgroundbeforere-referencingwithrespecttothecommonaverage.
FrontiersinNeuroscience|Neuroprosthetics July2012|Volume6|Article55|20

Tangermannetal. ReviewoftheBCIcompetitionIV
FIGURE26|(DataSet4).Timecoursesoffingerflexion,broadband,LMP,
andtherawelectricpotential.TheLMP(Schalketal.,2007;Kubaneketal.,
2009)hasbeenshowntoholdinformationaboutdifferentmotorbehaviors.
Spectrallybroadbandchange,correspondingto1/ftypechangeinthe
electricpotentialpowerspectrum(Milleretal.,2009a,b),canbecaptured
asanotherpowerfulcorrelateofmotorbehavior.Bysynthesizingdifferent
features,morepowerfulbrain-computerinterfacingalgorithmsmaybe
obtained.
neuronalpopulationbeneaththeelectrode(Milleretal.,2009a,b).
When captured, this broadband feature has been demonstrated
tobearobustcorrelateoffingermovementatindividualsitesin
motorcortex(Milleretal.,2009b;Figures26and30).
Inthiscompetition,participantsuseddifferenttechniquesthat
capitalized on different aspects of these signals to predict the
flexionofindividualfingersfromtheECoGsignals.
8.2. MATERIALSANDSUBJECTS
ThethreesubjectsinthedatasetwereepilepticpatientsatHar-
borview Hospital in Seattle,Washington. Each patient had elec-
trode grids placed subdurally on the surface of the brain for
FIGURE25|(DataSet4–event-relatedpotential).Illustrationthatthe
the purpose of extended clinical monitoring and localization
characteristicchangesinthepowerspectraldensitychangeswithactivity
arenotduetoanreproducibleevent-relatedpotentialshift(ERP).Two of seizure foci. Each subject gave informed consent to partic-
adjacentelectrodesareshownin(A).OnehasanERP,andonedoesnot, ipate in this study, which was approved by the internal review
butbothhavethecharacteristicperi-movementspectralchanges.(B) board(IRB)of HarborviewHospital.Allpatientdatahavebeen
Individual(gray)andaveragedthumbmovement(black,left)orindexfinger
anonymizedaccordingtoIRBprotocolinaccordancewithHIPAA
movement(black,right),lockedtothefirstmovementfromtheappropriate
movementcue.(C)Thenormalizedpowerspectraldensity(“PSD”)asa regulations.
functionoftime.Itdemonstratestheclassicspectralchangesjustpriorto
movementonsetforboththumbandindexfinger.Notethatthedecreasein 8.2.1. Experimentalparadigm
poweratlowerfrequencies(α/β/µrange),andtheincreaseinpowerat
Signals from the electrode grid were amplified and digitized
higherfrequencies(aboveabout40Hz)bothbeginbeforemovementonset.
using Synamps2 amplifiers (Neuroscan,El Paso,TX,USA). The
(D)Individualandaveragedrawpotentialtracesaroundeachofthefirst
movementsfromappropriatethumborindexfingermovementepochs. general-purpose BCI system BCI2000 (Schalk et al., 2004) pro-
Thereisnosignificantevent-relatedpotential(ERP)effectforthumb,but vided visual stimuli to the patient, acquired brain signals from
thereisfortheindexfinger. the Synamps2 system, and also recorded the flexion of individ-
ual fingers (on the hand contralateral to the implanted grid)
using a data glove (Fifth Dimension Technologies, Irvine, CA,
broaddistributions,andpowerincreasesathighfrequencieshave USA). BCI2000 stored the brain signals, the timing of stim-
spatially more confined distributions (Figure28). Different fin- ulus presentation, and the flexion of each of the fingers in a
gershavespatiallydifferentrepresentationsonthebrainsurface, data file. Data files were converted to MATLAB format for this
and this can be used to help distinguish which finger might be competition. Each patient had subdural electrode arrays (Ad-
movingatanyparticulartime(Figures28–30). Tech, Racine, WI, USA) implanted. Each array contained 48–
Time-frequencyestimatesofpowerchangecanserveasrobust 64 platinum electrodes that were configured in 8×6 or 8×8
correlates of behavior (Figures 25 and 27). Recent studies have arrangements. The electrodes had a diameter of 4mm (2.3mm
demonstrated that what had been perceived as a spatially focal exposed), 1cm inter-electrode distance, and were embedded
highfrequencyphenomenonwasreallyareflectionofabroadband in silastic. Electrocorticographic (ECoG) signals (i.e., 62, 48,
feature,likelycorrespondingtoaveragefiringpotentialrateofthe and 64 channels from subjects 1, 2, and 3, respectively), were
www.frontiersin.org July2012|Volume6|Article55|21

Tangermannetal. ReviewoftheBCIcompetitionIV
FIGURE27|(DataSet4).Examplesofthenormalizedpowerspectral samples(lighttrace)andrestsamples(blacktrace).(B)Average
density(PSD)ofthepotentialtimeseriesaroundfingerflexion.The time-varyingPSD(scaledaspercentageofmeanpowerateach
PSDwascalculatedfrom1swindowscenteredattimesofmaximum frequency)withrespecttofirstindexfingermovementfromeach
flexionandalsoduringrest.(A)MeanPSDofindexfingermovement movementcue.
FIGURE28|(DataSet4).Corticalactivationmapsformovementof spatiallymuchmorebroad,correspondingtofluctuationsintheclassic
differentfingersinonesubject.Thechangesinpowerbetween126and motorrhythms.Figure29showsthatthespatialrepresentationsfor
150Hzarefocusedintheclassichandareaofthebrain.Thespatial highfrequenciesareverydifferentfordifferentfingermovementtypes,
distributionfor76–100Hzarenearlyidentical,asmightbeexpected withinageneralhandregion.Electrodepositionsareshownwithwhite
sincebotharereflectionsofthebroadbandfeaturehighlightedin dots,andpowerchangewithlightanddarkgraypatchesonthebrain
recentliterature(Milleretal.,2009b).Lowfrequencychangesare surface.
acquiredwithrespecttoascalpreferenceandground(Figure24), 8.3. DATAFORMAT
band-pass filtered between 0.15 and 200Hz, and sampled at ThedataforeachsubjectwascontainedinaseparateMATLABfile
1000Hz. thatwasnamed“subX_comp.mat”where“X”denotesthesubject
number.Eachfilecontainedthreevariables:
8.2.2. Protocol • “train_data”– this variable,in time×channels,gave the first
Thesubjectswerecuedtomoveaparticularfingerbydisplaying 2/3(6min,40s)ofrecordedECoGsignals(400,000samplesat
thecorrespondingword(e.g.,“thumb”)onacomputermonitor 1kHzsamplingrateperchannel)fromthespecifiedexperiment,
placed at the bed-side (Figure 30). Each cue lasted 2s and was foreverychannel.
followedbya2-srestperiodduringwhichthescreenwasblank. • “train_dg” – this variable, in time×finger was the first 2/3
Duringeachcue,thesubjectstypicallymovedtherequestedfinger (6min, 40s) of recorded finger position [thumb – index –
3–5times.Thisnumbervariedacrosssubjectsandfingers.There middle–ring–little;400,000samples(super-sampledto1kHz)
were 30 movement stimulus cues for each finger (i.e.,a total of perfinger]fortheassociatedexperiment.
150cuepresentationsandabout90–150flexionsofeachfinger); • “test_data” – this variable, in time×channels, gave the last
stimuluscueswereinterleavedrandomly.Thisexperimentlasted 1/3 (3min, 20s) of recorded ECoG signals (200,000 sam-
10minforeachsubject. ples at 1kHz sampling rate per channel) from the specified
Subsequentofflineanalysesshowedthatring(4th)fingermove- experiment, for every channel. These data were used to pre-
mentswerecorrelatedwitheithermiddle(3rd)orlittle(5th)finger dict the final 1/3 (3min, 20s) of recorded finger position
movements.Thus,whilethisringfingerpositionwasincludedwith (thumb – index – middle – ring – little) for the associated
thetrainingdata,itwasnotusedforevaluation. experiment.
FrontiersinNeuroscience|Neuroprosthetics July2012|Volume6|Article55|22

Tangermannetal. ReviewoftheBCIcompetitionIV
Thechannelorderwasscrambledsothatthepredictiontaskinthe • “eval_dg”–thisvariable,intime×channels,gavethelast1/3
competitionwasrestrictedtoalgorithmicoptimizationsonly. (3min,20s)ofpredictedfingerflexionforeachofthefivefin-
gers(thumb–index–middle–ring–little)fortheassociated
8.4. CHALLENGE experiment(200,000samplesperfinger).
Eachparticipatinggroupsubmittedthreefilestitled“sub1_eval,”
“sub2_eval,” and “sub3_eval, ” corresponding to subjects 1–3, The evaluation criteria was as follows: for each subject, the
respectively.Eachof thesecontainedasinglevariable,“eval_dg,” received variable “eval_dg” was compared with the actual fin-
withdimensions200,000×5: gerpositionsin“test_dg,”whichwaswithheld.Wecalculatedthe
correlationcoefficientr betweentheactualandthepredictedfin-
gerflexionsforeachsubjectandfinger.Wedidnotcalculatethe
correlationcoefficientforthe4th(ring)finger,becausetheflex-
ionof thisfingerwastypicallycorrelatedwiththeflexionof the
3rd(middle)or5th(little)finger.Thefinalscorewascalculated
as the arithmetic mean of the 12 correlation coefficients (4 per
subject,3 subjects). The submission with the highest score won
thecompetition.
8.5. SUBMISSIONSANDALGORITHMS
Fivegroupssubmittedacontribution(S-1toS-5),withthreeof
them (S-1, S-2, S-4) showing a performance well above chance
levelontheunseentestset.
FIGURE29|(DataSet4).Ablow-upofthesensorimotorregionforhigh S-1: RemiFlamary,AlainRakotomamonjy,LITISINSAdeRouen,
frequenciesfromFigure28.Notethatthisvariabilityacrosselectrodes France
allowsforrobustsegregationofdifferentfingermovementsduring
S-2: NanyingLiangandLaurentBougrain,CortexTeam,Research
classification.
CentreINRIA,Nancy-GrandEst,France
AA B
2 3
1
2s
C
Thumb Position
1
Index Finger Position
2
Little Finger Position
3
0 10 20 30 40
Time (s)
FIGURE30|(DataSet4).TimecourseofECoGinadjacentelectrodes onemovementtype(r=0.46forbroadbandfromelectrode1with
revealsindividualdigitrepresentation.(A)X-rayoftheECoGarray thumbposition;r=0.47forelectrode2withindexfinger;r=0.29for
insitu,withthreeelectrodeslabeled,correspondingtothenumbersin electrode3withlittlefinger;cross-combinationshadamean
(C).(B)Flexiontimecourseofeachfinger.(C)Projectionsofthe correlationof−0.09,indicatinglighthyperextensionofotherfingers
time-frequencyrepresentationtobroadbandspectralchange(Miller whileflexingtheappropriatefingerinthissubject),over10minof
etal.,2009b).Eachelectrodeisspecificallyandstronglycorrelatedwith continuousdata(3.6×106samples).
www.frontiersin.org July2012|Volume6|Article55|23

| Tangermannetal. |     |     |     |     |     |     |     |     |     | ReviewoftheBCIcompetitionIV |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- |
S-4: MathewSalvaris,UniversityofEssex,Colchester,UK
Table5|(DataSet4).Performanceofthefivesubmissions.
Thefollowingshortsummaryoftheappliedalgorithmsisbased Submission r
onthedescriptionsprovidedbythecompetitors:
|                                                     |     |     |     |     |     | S-2 |     |     |     |     |     | 0.46 |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
| S-1                                                 |     |     |     |     |     | S-1 |     |     |     |     |     | 0.42 |
| FlamaryandRakotomamojyemployedaswitchingmodeltopre- |     |     |     |     |     | S-4 |     |     |     |     |     | 0.27 |
|                                                     |     |     |     |     |     | S-3 |     |     |     |     |     | 0.10 |
dictfingerflexion.Thismethodassumedthattheoutputflexionof
thefingersislinearandthatthetransferfunctionbetweenECoG S-5 0.05
| signals and | finger position | depended | on an internal | state | k that |     |     |     |     |     |     |     |
| ----------- | --------------- | -------- | -------------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
representsthefingermoving(1–5)ornofingermovingatall(6).
|     |     |     |     |     |     | an average | correlation | coefficient |     | of 0.46, and | thereby | won this |
| --- | --- | --- | --- | --- | --- | ---------- | ----------- | ----------- | --- | ------------ | ------- | -------- |
Theyusedridgeregressiontocomputethetransferfunctionand
competition.Therunner-upcontributionofFlamaryandRako-
sparselinearregressiontoderivethestateestimation.Inbrief,sig-
tomamojyperformedsimilarlywellwithacorrelationcoefficient
nalswerefirstdown-sampledbyafactorof4.Thefeaturesforthe
|     |     |     |     |     |     | of 0.42. Details | of  | the two | approaches | are described |     | in Flamary |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | ------- | ---------- | ------------- | --- | ---------- |
lineartransferfunctionswereobtainedwithaSavitsky-Golayfilter
andRakotomamonjy(2012)andLiangandBougrain(2012).
(0.4s,3rdorder).ThefeaturesusedforthestateestimatorwereAR
|     |     |     |     |     |     | While it | is difficult | to assess | the | difference | in  | performance |
| --- | --- | --- | --- | --- | --- | -------- | ------------ | --------- | --- | ---------- | --- | ----------- |
coefficientscomputedonamovingwindowof300points.Once
betweenthedifferentmethods,itisinterestingthatmethodsthat
theinternalstatewasestimated,fingerflexionwascomputedby
aresimilarinsimplicitytothoseusedinSchalketal.(2007)and
| multiplyingthefeaturesatatimet |     |     | bythelineartransferfunction |     |     |            |            |     |          |              |          |        |
| ------------------------------ | --- | --- | --------------------------- | --- | --- | ---------- | ---------- | --- | -------- | ------------ | -------- | ------ |
|                                |     |     |                             |     |     | Kubanek et | al. (2009) | can | reliably | and robustly | estimate | finger |
correspondingtothestatekattimet.
flexionfromECoGsignals.Thatbeingthecase,itmayalsobepos-
S-2 siblethatmoresophisticatedmethodsthatexplicitlyincorporate
LiangandBougrainfirstextracted,fromeachlocation,thetime- physiologicalorphysicalconstraintsinthecomputationalmodel
mightfurtherimproveperformance.
varyingactivityinthreefrequencybands:1–60,60–100,and100–
| 200Hz. | Then,the power | in each | bin was accumulated |     | in 40ms |               |     |     |     |     |     |     |
| ------ | -------------- | ------- | ------------------- | --- | ------- | ------------- | --- | --- | --- | --- | --- | --- |
|        |                |         |                     |     |         | 9. DISCUSSION |     |     |     |     |     |     |
timebins.Thesizeofthetimebinwaschosensothattheresulting
TheBCIcompetitionwascreatedinordertosupportthedevel-
amplitudemodulationfeatureinputshadthesamesamplingrate
|     |     |     |     |     |     | opmentof | algorithmicsolutionsfortypicalBCIproblems.Does |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | ---------------------------------------------- | --- | --- | --- | --- | --- |
(i.e.,25Hz)asthatofthefingerflexionvalues.Initialevaluations
itliveuptoitspromise?Thefollowingsectionsattempttogivean
foundthateachfingerflexionwascorrelatedtofeaturesfromonly
two or three particular locations. Therefore,features were auto- answertothevariousaspectsofthisquestion.
maticallyselected(separatelyforeachfingerandsubject)usinga
|     |     |     |     |     |     | 9.1. RESTCLASSPROBLEMREMAINSACHALLENGE |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- |
stepwisefeatureselectionprocedurebasedonthetrainandvali-
|                         |     |                                 |     |     |     | Movingfromanartificiallabsituationtotheevery-dayuseof |     |     |     |     |     | a   |
| ----------------------- | --- | ------------------------------- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| dationmethod(i.e.,2/3of |     | traindatawereusedfortrainingand |     |     |     |                                                       |     |     |     |     |     |     |
BCIintroducesanewchallenge:periodsofnon-control,wherea
1/3forvalidation).Theresultingfeatureswerethensubmittedto
BCIuserisvoluntarilyswitchingtoanother(non-BCI)actionor
aWienerfilterwith25tap-delays(i.e.,usingthepresentinputand
isinvoluntarilydistractedfromthecontrolinterface.Thedistrac-
theprevious1-sinputsforpredictingthepresentfingerflexion).
torcanbeanotheractivetask(e.g.,communicationviaadifferent
S-4 channel,theperceptionandprocessingofcontent,reasoningabout
adecisiontotake)orsimplytakingarest.Thebasicproblemabout
| Salvaris | first re-referenced | signals | to the common | average, | and |     |     |     |     |     |     |     |
| -------- | ------------------- | ------- | ------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
thendown-sampledsignalsto500Hz.Bandpowerfeatureswere restclassdetectioningeneralis,thattherestingstateisnotwell-
extracted by wavelet packets with sym9 wavelet and the average definedatall,andthusthereisnoreliabletrainingdataavailable
ofthetimeseries.FeatureswerethenselectedusingWEKA’sCFS thatcanbeusedtocalibratetheBCIsystem.
Inthiscompetition,thedetectionofsucharestclasswaschal-
algorithm.TheselectedfeatureswereusedtotraintheSVRalgo-
rithm implemented in LibSVM. The parameters for SVR were lenged with data set 1. The results for this motor imagery data
tunedthrough5-foldcrossvalidation.TheresultingSVRmodel set revealed, that most competitors had problems in correctly
|     |     |     |     |     |     | identifying | time periods | of  | the rest | class. Even | considering | the |
| --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | -------- | ----------- | ----------- | --- |
wasthenusedtoclassifythetestdata.
performanceofthecompetitionwinner(Figure6)thereremains
| 8.6. RESULTS |     |     |     |     |     | thewishforfurtherimprovement. |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- |
Thegoalofthisportionofthecompetitionwastopredictfinger
flexionforfourofthefivefingersonatestset(3min20s)usinga 9.2. TRANSFERABILITYTOONLINEBCIs
classifierthatwastrainedonatrainingset(6min40s).Thefidelity Thewinningmethodsofthisorearliercompetitionsarenotneces-
ofthepredictionwasassessedbycomputingthecorrelationcoef- sarilytransferabletobeusedinanonlineclosed-loopBCIsystem.
ficientbetweentheactualfingerflexionvaluesandthesubmitted Whiletheruntimesof algorithmsarenotareallimitation,non-
fingerflexionvalues.Theresultofaparticularsubmissionwasthe causalfiltersandtimedelaysareproblematic.Asanexample,the
arithmeticmeanof12correlationcoefficients(i.e.,3subjectsand winningalgorithmof dataset2bpredictedtheclasslabelsquite
4fingers). accurately,butintroducedadelayof2sduringthepreprocessing
Twoofthefivesubmissionsachievedparticularlystrongpredic- eyeartifacts.Thisisatrade-offthathastobeconsideredforeach
tions(seeTable5).NanyingLiangandLaurentBougrainachieved specificapplication.
FrontiersinNeuroscience|Neuroprosthetics July2012|Volume6|Article55|24

Tangermannetal. ReviewoftheBCIcompetitionIV
High robustness and generalizability of a winning algorithm 10.2. NON-STATIONARITY
is another characteristic, that supports the applicability of an SeverefortheuseofdryEEGsensors,butnotrestrictedtothissig-
algorithmforthefeedbackcase.ComparabletoearlierBCIcompe- naltype,istheproblemofnon-stationarityinbrainsignals.Inthe
titions,againvariantsofCSPruledtherankings.Ofspecialinterest contextofBCI,itismostlyobservedduringthetransitionfromthe
istheoutcome,thattheSingaporegrouphasscoredexceptionally initialcalibrationphasetotheonlineuseofaBCI(Shenoyetal.,
highforseveralof thedatasets.Asthesubmittedalgorithmsof 2006;Sugiyamaetal.,2007),butalsowithinperiodsofonlineuse,
this group used similar concepts, this is a strong indicator for wherenoobviouschangeofthetaskorparadigmtakesplace.
robustness. Thereasonsfornon-stationarityinbraindatacanrangefrom
Assomeofthewinningalgorithmsofearliercompetitionshave external noise, over effects caused by high dimensionality and
indeedbeenadoptedintothestandardcanonforBCIonlinecon- robustestimationproblems(Sannellietal.,2008;Abrahamsenand
trol,webelieve,thatthiswillalsohappenforsomealgorithmsof Hansen,2011; task-unrelated) changes in the background brain
thepresentcompetition. activityofBCIusers(e.g.,duetofatigueorartifacts;Winkleretal.,
2011,learning effects or adaptive behavior of the users;Ramsey
9.3. USEFULNESSOFSYNTHETICDATA
et al., 2009, or even co-adaptation of users and the BCI system
ThemostreliablewayoftestingnewalgorithmicideasforBCIis
Vidaurreetal.,2011).
toimplementtheminanonlineexperiment,ifpossiblewithusers
Non-stationaritycansometimesbeobservedevenbybareeyein
matching the target group. But even when testing with healthy
therawdata,whereitispresentintheformofslowdrifts,changes
users,thetestingeffortishugeandcannotbeinvestedforevery
inoscillatorysources,orchangesinthenoiselevelofelectrodes.If
changeofthealgorithmicmodel.
processedwithanautomaticclassificationorregressionmethod
SyntheticEEGdataaspresentedindataset1-artificialmight
asinBCI,thisprocessingcanbeharmedalsobysubtlebiasshifts,
offerapartialremedytothisproblem.Ithasproventoberealistic
covariancedriftsorchangesof thecovariancestructure,oreven
inthesensethatthesubmittedalgorithmsperformedverysimilar
morecomplexchangesofthedatadistributions.
onthesyntheticandtherealEEGdata.Asitischeaptogeneratea
Althoughanumberof methodshavebeenproposedtomiti-
largeamountofthisdata,atleastinitialalgorithmictestbedscan
gatethisproblemeitherbyfindingaglobalstablesubspaceforthe
bebasedonit.Precautions,ofcourse,havetobetakeninorderto
datarepresentation(Krauledatetal.,2007;Blankertzetal.,2008a;
avoidthatthepriorsusedfortheEEGgenerationarenotknownor
von Bünau et al., 2009; Wojcikiewicz et al., 2011), or by adapt-
explicitlyexploitedbythealgorithmsundertestandtheircreators.
ingtheonlineprocessingtocompensateforongoingchanges(see
AssimulatedBCIclassifieroutputhasalreadysuccessfullybeen
VidaurreandSchlögl,2008;BlankertzandVidaurre,2009;Sannelli
applied for the fine-tuning of BCI user interfaces (Quek et al.,
et al., 2011) for adaptation in motor-related tasks, and (Dähne
2011),thenextstepisonthehorizon:tousesimulatedEEGthat–
etal.,2011)foradaptationinERPparadigms),itstillisthesource
certainlyonlytoalimitedextend–modelstheuserbehavior,in
of major problems in the online use of BCI. This qualifies the
ordertotestBCIsystemsonlineinaclosedloop.
problemofnon-stationarityforbecomingatargetinfutureBCI
10. FURTHERTOPICSCONCERNINGFUTURE competitions.
COMPETITIONS
10.3. MULTIMODALSIGNALS/HYBRIDBCIs
Due to the development of the field of BCI, new data analytic
Consideringthepredominantuseofnon-invasiveBCIsystems,it
problemswereidentified,thataresuitableforaddressingthemin
is worth to briefly review the development of BCI performance
aBCIcompetition.
(e.g.,intermsofcommunicationrates)overtime.Onthepositive
10.1. WIRELESSANDDRYEEGSIGNALS side,newBCIsystemsbasedonexternalstimulihaverecentlybeen
We currently observe the upcoming of easy-to-mount dry elec- reported,thatemployednovelparadigmsforauditory(Schreuder
trode caps as either research prototypes (Popescu et al., 2007; etal.,2010,2011;Höhneetal.,2011)andforvisualERPsetups(Liu
Gargiulo et al., 2010; Luo and Sullivan, 2010; Saab et al., 2011; etal.,2010;AcqualagnaandBlankertz,2011;Schaeffetal.,2011;
Zanderetal.,2011)orpurchasableproducts(e.g.,Saharadrycap Tangermannetal.,2011;Trederetal.,2011).Theyimproveover
bygTec,MindsetbyNeuroSky,orEmotivcap).Assomeofthem long-used standard stimulation paradigms or can provide solu-
providewirelesstransmissionprotocols,theyopenupthepossi- tionsforpatientsthathavelosteyegazecontrol.Incontrary,the
bilitytomonitortheactingbrainduringreal-lifesituationsrather improvementsreportedforBCIsystemsbasedonmotorimagery
thanunderartificiallabconditions. andERD/ERSeffectshavebeensloweroverthelastyears,despite
Thesignalsofthesedryelectrodes,however,currentlystillsuf- ofadrasticinitialperformanceboostwhichwasmadepossibleby
ferfromanumberof artifacts,whicharetypicallymuchweaker the introduction of machine learning methods (Blankertz et al.,
or not present at all in wet electrode recordings. Examples are 2003,2011;Schröderetal.,2003).
inductive artifacts by persons moving in the same room, drifts Thenextboostof BCIperformancecanbeexpectedforpar-
andsaturationeffects,orfrictionartifactsuponelectrodemove- adigms,thatareabletocombineindependentinformationfrom
ments.Whileanoverallhighernoiselevelofdryelectrodesmight differentsourcesinordertoimprovetheBCIcontrolqualityover
bedifficulttoovercome,someartifactsmightbealleviatedbysuit- thelevelofatraditionalsingle-sourceBCI.InanERPsetup,such
abledataprocessing.AfutureBCIdatacompetitionshouldthus approaches could combine stimuli of different sensory modali-
includeanumberof drysensordatasetstodeterminethemost ties(Aloiseetal.,2007).Inmotorimagery,theuseof ERD/ERS
effectiveapproaches. effects together with slower motor-related potentials (Dornhege
www.frontiersin.org July2012|Volume6|Article55|25

Tangermannetal. ReviewoftheBCIcompetitionIV
etal.,2004)canincreaseinformationrates.Abstractingthiscon- potentially be misleading with respect to the overall quality of
cepttothenextlevel,EEGsignalscouldbecombinedwithother eventhebest-rankedentry.Forthisreason,itisplannedtointro-
brainsignalsourceslikefNIRS(Fazlietal.,2012),withnon-neural duceaperformancethresholdinfutureBCIcompetitions.Itwill
butphysiologicalsignals(e.g.,heartratevariability,galvanicskin bedeterminedbasedonthetestdata.Allentrieshavetopassthis
resistance,pupildilation,etc.)orinahybridsetup(Millánetal., thresholdbeforetheycanentertheofficialranking.Thethreshold
2010; Pfurtscheller et al.,2010; Müller-Putz et al.,2011) e.g.,in istobedefinedbythedataissuinggroupandshouldrepresentthe
combinationwithnon-BCIassistivetechnology. state-of-the-artperformancethatcanbegainedwithestablished
WecurrentlyobserveanexpansionofBCItechnologytoother analysis methods. The threshold is published together with the
fields. As it gives access to the real-time monitoring of mental performancemetricandwithashortdescriptionofthestandard
states(Mülleretal.,2008),itisinterestingforneuro-ergonomic methodthatleadstothisperformance.
interface-andproductdesign(Blankertzetal.,2010;Porbadnigk Wethinkthatthisactionwillcontributetowardassessingthe
etal.,2010).Furthermore itstartsbecoming atoolfor theneu- absolute quality of a competition entry rather than the relative
rosciences, where the use of multiple sources of information is quality only. On the long run the introduction of a threshold
aninvitingpossibility.Allthesefieldscanprofitfromprocessing canincreasetheperceivedreliabilityofnovelmethodsbroughtto
methods,that are capable of linking brain data with behavioral the BCI community via a BCI competition, and speed up their
dataorwithnon-neuralphysiologicalsignaltypes. adoptionbyBCIpractitioners.
The challenge in processing signals from multiple sources is
torepresent,combineandconvergeinformationinaway,thatis ACKNOWLEDGMENTS
independent of different sampling rates (Bießmann et al.,2009; The studies were in part or completely supported by the
Biessmann et al., 2011), SNR-levels or varying levels of non- Bundesministerium für Bildung und Forschung (BMBF), Fkz
stationarity. It is a great challenge with multiple facets. A next 01IB001A,01GQ0850,bytheGermanScienceFoundation(DFG,
BCIcompetitioncouldcontributetotheexplorationofatleasta contractMU987/3-2),bytheEuropeanICTProgrammeProjects
fewoftheseaspects. FP7-224631 and 216886, the World Class University Program
through the National Research Foundation of Korea funded by
PERFORMANCEBASELINEFORPARTICIPATION theMinistryofEducation,Science,andTechnology(GrantR31-
The results of competition IV and the three past competitions 10008),theUSArmyResearchOffice[W911NF-08-1-0216(Ger-
have shown,that the number of entries per data set varies to a win Schalk) and W911NF-07-1-0415 (Gerwin Schalk)] and the
largeextent,probablyduetodifferinglevelsofeffortthathaveto NIH[EB006356(GerwinSchalk)andEB000856(GerwinSchalk),
beinvested.Participantstendtosubmitmoreentriesforstandard the WIN-Kolleg of the Heidelberg Academy of Sciences and
learningproblems,e.g.,classificationproblemswherethepercent- Humanities,GermanFederalMinistryofEducationandResearch
ageofcorrectclassificationsisthemetricofchoice.Non-standard grants 01GQ0420,01GQ0761,01GQ0762,and 01GQ0830,Ger-
learningproblems,eventhoughrepresentingimportantproblems manResearchFoundationgrants550/B5andC6,andbyascholar-
inthefieldofBCI,tendtogainlessattention. shipfromtheGermanNationalAcademicFoundation.Thispaper
As the success of a participant is finally expressed as a rank onlyreflectstheauthors’viewsandfundingagenciesarenotliable
among all submitted entries, the small sample ranking can foranyusethatmaybemadeoftheinformationcontainedherein.
REFERENCES Proceedings of the IEEE Interna- analysisanditsapplicationinmulti- based on single-trial EEG analysis.
Abrahamsen,T. J.,and Hansen,L. K. tional Joint Conference on Neural modalneuronaldataanalysis.Mach. IEEETrans.NeuralSyst.Rehabil.Eng.
(2011).Acureforvarianceinflation Networks (IJCNN’08),Hong Kong, Learn.79,5–27. 11,127–131.
inhighdimensionalkernelprincipal 2391–2398. Biessmann,F.,Plis,S.,Meinecke,F.C., Blankertz,B.,Kawanabe,M.,Tomioka,
componentanalysis.J.Mach.Learn. Ang,K.,andQuek,C.(2006).“Rough Eichele,T.,andMüller,K.-R.(2011). R., Hohlefeld, F., Nikulin, V., and
Res.12,2027–2044. set-based neuro-fuzzy system,” in Analysisofmultimodalneuroimag- Müller, K.-R. (2008a). “Invariant
Acqualagna, L., and Blankertz, B. ProceedingsoftheIEEEInternational ingdata.IEEERev.Biomed.Eng.4, commonspatialpatterns:alleviating
(2011).Agazeindependentspeller JointConferenceonNeuralNetworks 26–58. nonstationaritiesinbrain-computer
basedonrapidserialvisualpresenta- (IJCNN’06),Vancouver,742–749. Bijma,F.,deMunck,J.,Huizenga,H., interfacing,”in Advances in Neural
tion.Conf.Proc.IEEEEng.Med.Biol. Ang, K. K., Chin, Z. Y., Wang, C., and Heethaar, R. (2003). A math- Information Processing Systems 20,
Soc.2011,4560–4563. Guan, C., and Zhang, H. (2012). ematical approach to the tempo- edsJ.Platt,D.Koller,Y.Singer,and
Aloise, F., Lasorsa, I., Schettini, F., Filterbankcommonspatialpattern ralstationarityofbackgroundnoise S. Roweis (Cambridge, MA: MIT
Brouwer,A.,Mattila,D.,Babiloni,F., algorithm on BCI competition iv in MEG/EEG measurements. Neu- Press),113–120.
Salinari,S.,Marciani,M.,andCin- datasets2aand2b.Front.Neurosci. roimage20,233–243. Blankertz,B.,Tomioka,R.,Lemm,S.,
cotti,F.(2007).Multimodalstimu- 6:39.doi:10.3389/fnins.2012.00039 Blanchard,G.,andBlankertz,B.(2004). Kawanabe, M., and Müller, K.-R.
lationforaP300-basedBCI.Int.J. Ball,T.,Schulze-Bonhage,A.,Aertsen, BCI competition 2003 – data set (2008b). Optimizing spatial filters
Bioelectromagn.9,128–130. A.,andMehring,C.(2009).Differ- IIa:spatialpatternsofself-controlled for robust EEG single-trial analy-
Anderson,K.(2004).Targetingrecov- entialrepresentationofarmmove- brain rhythm modulations. IEEE sis. IEEE Signal Process. Mag. 25,
ery: priorities of the spinal cord- mentdirectioninrelationtocortical Trans.Biomed.Eng.51,1062–1066. 41–56.
injuredpopulation.J.Neurotrauma anatomyandfunction.J.NeuralEng. Blankertz,B.,Dornhege,G.,Schäfer,C., Blankertz, B., Lemm, S., Treder, M.
21,11371–11383. 6,016006. Krepki,R.,Kohlmorgen,J.,Müller, S., Haufe, S., and Müller, K.-R.
Ang, K., Chin, Z. Y., Zhang, H., Bießmann,F.,Meinecke,F.C.,Gretton, K.-R.,Kunzmann,V.,Losch,F.,and (2011). Single-trial analysis and
and Guan, C. (2008).“Filter bank A.,Rauch,A.,Rainer,G.,Logothetis, Curio,G.(2003).Boostingbitrates classification of ERP compo-
common spatial pattern (FBCSP) N.,andMüller,K.-R.(2009).Tem- anderrordetectionfortheclassifica- nents – a tutorial. Neuroimage 56,
in brain-computer interface,” in poral kernel canonical correlation tionoffast-pacedmotorcommands 814–825.
FrontiersinNeuroscience|Neuroprosthetics July2012|Volume6|Article55|26

Tangermannetal. ReviewoftheBCIcompetitionIV
Blankertz,B.,Müller,K.-R.,Curio,G., A.,andBirbaumer,N.(2008).Think activity.Part1.Analyticamplitude. Huber, P., Kleiner, B., Gasser, T., and
Vaughan, T. M., Schalk, G., Wol- to move: a neuromagnetic brain- Clin.Neurophysiol.115,2077–2089. Dumermuth, G. (1971). Statisti-
paw,J. R.,Schlögl,A.,Neuper,C., computerinterface(BCI)systemfor Freeman, W. (2004b). Origin, struc- calmethodsforinvestigatingphase
Pfurtscheller, G., Hinterberger, T., chronikstroke.Stroke39,910–917. ture,and role of background EEG relations in stationary stochastic
Schröder, M., and Birbaumer, N. Carlqvist, H., Nikulin, V., Ström- activity.Part2.Analyticphase.Clin. processes. IEEE Trans. Acoust. 19,
(2004).TheBCIcompetition2003: berg, J., and Brismar, T. (2004). Neurophysiol.115,2089–2107. 78–86.
progressandperspectivesindetec- Amplitude and phase relationship Freeman,W.(2005).Origin,structure, Huizenga,H.,de Munck,J.,Waldorp,
tionanddiscriminationofEEGsin- betweenalphaandbetaoscillations androleofbackgroundEEGactivity. L., Grasman„ and R. P. (2002).
gletrials.IEEETrans.Biomed.Eng. in the human electroencephalo- Part3.Neuralframeclassification. Spatiotemporal EEG/MEG source
51,1044–1051. gram.J.Med.Biol.Eng.Comput.43, Clin.Neurophysiol.116,1118–1129. analysisbasedonaparametricnoise
Blankertz, B., Müller, K.-R., Krusien- 599–607. Freeman,W.(2006).Origin,structure, covariancemodel.IEEETrans.Bio-
ski, D., Schalk, G., Wolpaw, J. R., Crone, N. E., Miglioretti, D. L., Gor- androleofbackgroundEEGactiv- med.Eng.49,533–539.
Schlögl, A., Pfurtscheller, G., Mil- don, B., and Lesser, R. P. (1998a). ity.Part4.Neuralframesimulation. Jerbi,K.,Lachaux,J.,N’Diaye,K.,Pan-
lánJdel,R.,Schröder,M.,andBir- Functionalmappingofhumansen- Clin.Neurophysiol.117,572–589. tazis,D.,Leahy,R.,Garnero,L.,and
baumer,N. (2006). The BCI com- sorimotor cortex with electrocor- Galan, F., Oliva, F., and Guardia, J. Baillet, S. (2007). Coherent neural
petition III: validating alternative ticographic spectral analysis. II. (2007). Using mental tasks transi- representation of hand speed in
approachstoactualBCIproblems. Event-relatedsynchronizationinthe tionsdetectiontoimprovesponta- humansrevealedbyMEGimaging.
IEEETrans.NeuralSyst.Rehabil.Eng. gamma band. Brain 121(Pt 12), neousmentalactivityclassification. Proc. Natl. Acad. Sci. U.S.A. 104,
14,153–159. 2301–2315. Med.Biol.Eng.Comput.45,603–609. 7676–7681.
Blankertz,B.,Tangermann,M.,Vidau- Crone,N.,Miglioretti,D.,Gordon,B., Gargiulo,G.,Calvo,R.A.,Bifulco,P., Kaper,M.,Meinicke,P.,Grossekathoe-
rre,C.,Fazli,S.,Sannelli,C.,Haufe, Sieracki, J., Wilson, M., Uematsu, Cesarelli,M.,Jin,C.,Mohamed,A., fer, U., Lingner, T., and Ritter, H.
S.,Maeder,C.,Ramsey,L.E.,Sturm, S., and Lesser, R. (1998b). Func- and van Schaik,A. (2010). A new (2004).BCIcompetition2003–data
I., Curio, G., and Müller, K.-R. tional mapping of human senso- EEGrecordingsystemforpassivedry setIIb:supportvectormachinesfor
(2010).TheBerlinbrain-computer rimotorcortexwithelectrocortico- electrodes. Clin. Neurophysiol. 121, the P300 speller paradigm. IEEE
interface:non-medicalusesof BCI graphic spectral analysis. I. Alpha 686–693. Trans.Biomed.Eng.51,1073–1076.
technology. Front. Neurosci. 4:198. and beta event-related desynchro- Georgopoulos, A., Langheim, F., Koles, Z. J. (1991). The quantitative
doi:10.3389/fnins.2010.00198 nization.Brain121,2271. Leuthold,A.,andMerkle,A.(2005). extraction and topographic map-
Blankertz,B.,andVidaurre,C.(2009). Dähne,S.,Höhne,J.,andTangermann, Magnetoencephalographic signals pingoftheabnormalcomponentsin
Towards a cure for BCI illiteracy: M. (2011). “Adaptive classification predict movement trajectory in theclinicalEEG.Electroencephalogr.
machine-learningbasedco-adaptive improves control performance in space.Exp.BrainRes.167,132–135. Clin.Neurophysiol.79,440–447.
learning. BMC Neurosci. 10(Suppl. ERP-based BCIs,”in Proceedings of Georgopoulos, A. P., Kalaska, J. F., Krauledat, M., Shenoy, P., Blankertz,
1),P85.doi:10.1186/1471-2202-10- the5thInternationalBCIConference, Caminiti, R., and Massey, J. T. B., Rao, R. P. N., and Müller,
S1-P85 Graz,92–95. (1982).Ontherelationsbetweenthe K.-R. (2007).“Adaptation in CSP-
Bostanov,V. (2004). BCI competition Millán, J. D., Rupp, R., Müller-Putz, direction of two-dimensional arm based BCI systems,” in Toward
2003 – data sets Ib and IIb: fea- G.,Murray-Smith,R.,Giugliemma, movementsandcelldischargeinpri- Brain-Computer Interfacing,eds G.
ture extraction from event-related C., Tangermann, M.,Vidaurre, C., mate motor cortex. J. Neurosci. 2, Dornhege, R. Millán Jdel T. Hin-
brainpotentialswiththecontinuous Cincotti, F., Kübler, A., Leeb, R., 1527–1537. terberger, D. McFarland, and K.-
wavelet transform and the t-value Neuper,C.,Müller,K.-R.,andMat- Geselowitz, D. (1967). On bioelectric R. Müller (Cambridge, MA: MIT
scalogram.IEEETrans.Biomed.Eng. tia, D. (2010). Combining brain- potentialsinaninhomogeneousvol- Press),305–309.
51,1057–1061. computer interfaces and assistive umeconductor.Biophys.J.7,1–11. Kubanek, J., Miller, K., Ojemann, J.,
Bradberry, T., Gentili, R., and technologies: state-of-the-art and Hammon, P., Makeig, S., Poizner, H., Wolpaw,J.,and Schalk,G. (2009).
Contreras-Vidal, J. (2010). Recon- challenges. Front. Neurosci. 4:161. Todorov, E., and de Sa,V. (2008). Decodingflexionofindividualfin-
structing three-dimensional hand doi:10.3389/fnins.2010.00161 Predicting reaching targets from gersusingelectrocorticographicsig-
movements from noninvasive Dornhege,G.,Blankertz,B.,Curio,G., human EEG. IEEE Signal Process. nals in humans. J. Neural Eng. 6,
electroencephalographic signals. J. and Müller, K.-R. (2004). Boost- Mag.25,69–77. 066001.
Neurosci.30,3432–3437. ing bit rates in non-invasive EEG Haufe, S., Treder, M. S., Gugler, M. Kübler, A., Kotchoubey, B., Kaiser,
Bradberry,T.,Rong,F.,andContreras- single-trialclassificationsbyfeature F., Sagebaum, M., Curio, G., and J., Wolpaw, J., and Birbaumer, N.
Vidal, J. (2009). Decoding center- combination and multi-class para- Blankertz, B. (2011). EEG poten- (2001).Brain-computercommuni-
out hand velocity from MEG sig- digms.IEEETrans.Biomed.Eng.51, tials predict upcoming emergency cation:unlockingthelockedin.Psy-
nalsduringvisuomotoradaptation. 993–1002. brakingsduringsimulateddriving. chol.Bull.127,358–375.
Neuroimage47,1691–1700. Fatourechi,M.,Bashashati,A.,Ward,R. J.NeuralEng.8,056001. Leeb,R.,Lee,F.,Keinrath,C.,Scherer,
Brunner, C., Billinger, M., Vidaurre, K., and Birch, G. E. (2007). EMG Henninghausen,E.,Heil,M.,andRösler, R.,Bischof,H.,andPfurtscheller,G.
C.,andNeuper,C.(2011).Acom- and EOG artifacts in brain com- F.(1993).Acorrectionmethodfor (2007).Brain-computercommuni-
parisonofunivariate,vector,bilin- puter interface systems: a survey. dcdriftartifacts.Electroencephalogr. cation:motivation,aimandimpact
earautoregressive,andbandpower Clin.Neurophysiol.118,480–494. Clin.Neurophysiol.86,199–204. of exploring a virtual apartment.
features for brain-computer inter- Fazli, S., Mehnert, J., Steinbrink, J., Hochberg,L.,Serruya,M.,Friehs,G., IEEETrans.NeuralSyst.Rehabil.Eng.
faces. Med. Biol. Eng. Comput. 49, Curio, G., Villringer, A., Müller, Mukand, J., Saleh, M., Caplan,A., 15,473–482.
1337–1346. K. R., and Blankertz, B. (2012). Branner, A., Chen, D., Penn, R., Lemm,S.,Blankertz,B.,Dickhaus,T.,
Brunner, C., Naeem, M., Leeb, R., Enhancedperformancebyahybrid and Donoghue, J. (2006). Neu- andMüller,K.-R.(2011).Introduc-
Graimann,B.,andPfurtscheller,G. NIRS-EEG brain computer inter- ronalensemblecontrolofprosthetic tiontomachinelearningforbrain
(2007).Spatialfilteringandselection face.Neuroimage59,519–529. devicesbyahumanwithtetraplegia. imaging.Neuroimage56,387–399.
of optimized components in four Flamary, R., and Rakotomamonjy, A. Nature442,164–171. Lemm, S., Schafer, C., and Curio, G.
classmotorimageryEEGdatausing (2012).Decodingfingermovements Höhne, J., Schreuder, M., Blankertz, (2004).BCIcompetition2003–data
independent components analysis. fromECoGsignalsusingswitching B., and Tangermann, M. (2011). setIII:probabilisticmodelingofsen-
PatternRecognit.Lett.28,957–964. linearmodels.Front.Neurosci.6:29. A novel 9-class auditory ERP par- sorimotor mu rhythms for classi-
Buch,E.,Weber,C.,Cohen,L.,Braun, doi:10.3389/fnins.2012.00029 adigm driving a predictive text fication of imaginary hand move-
C.,Dimyan,M.,Ard,T.,Mellinger, Freeman, W. (2004a). Origin, struc- entrysystem.Front.Neurosci.5:99. ments.IEEETrans.Biomed.Eng.51,
J.,Caria,A.,Soekadar,S.,Fourkas, ture,and role of background EEG doi:10.3389/fnins.2011.00099 1077–1080.
www.frontiersin.org July2012|Volume6|Article55|27

Tangermannetal. ReviewoftheBCIcompetitionIV
Leuthardt, E., Schalk, G., Wolpaw, motor movement. J. Neurosci. 27, Pfurtscheller,G.,Allison,B.Z.,Bauern- II-ensembleofSVMsforBCIP300
J., Ojemann, J., and Moran, D. 2424. feind, G., Brunner, C., Escalante, speller.IEEETrans.Biomed.Eng.55,
(2004).Abrain-computerinterface Miller,K.,Schalk,G.,Fetz,E.,denNijs, T. S., Scherer, R., Zander, T. 1147–1154.
using electrocorticographic signals M.,Ojemann,J.,andRao,R.(2010). O., Mueller-Putz, G., Neuper, C., Ramoser, H., Müller-Gerking, J., and
inhumans.J.NeuralEng.1,63–71. Corticalactivityduringmotorexe- and Birbaumer, N. (2010). The Pfurtscheller, G. (2000). Optimal
Liang, N., and Bougrain, L. (2012). cution,motorimagery,andimagery- hybrid BCI. Front. Neurosci. 4:30. spatial filtering of single trial EEG
Decoding finger flexion from based online feedback. Proc. Natl. doi:10.3389/fnpro.2010.00003 during imagined hand movement.
band-specific ECoG signals in Acad.Sci.U.S.A.107,4430. Pfurtscheller, G., and da Silva, F. H. IEEETrans.Rehabil.Eng.8,441–446.
humans. Front. Neurosci. 6:29. Miller, K., Sorensen, L., Ojemann, L.(1999).Event-relatedEEG/MEG Ramsey,L.,Tangermann,M.,Haufe,S.,
doi:10.3389/fnins.2012.00029 J., and Den Nijs, M. (2009a). synchronizationanddesynchroniza- and Blankertz, B. (2009). Practic-
Liu,T.,Goldberg,L.,Gao,S.,andHong, Power-law scaling in the brain tion: basic principles. Clin. Neuro- ingfast-decisionBCIusinga“goal-
B.(2010).Anonlinebrain-computer surface electric potential. PLoS physiol.110,1842–1857. keeper” paradigm. BMC Neurosci.
interface using non-flashing visual Comput. Biol. 5, e1000609. Pfurtscheller, G., and Lopes da Silva, 10(Suppl.1),P69.doi:10.1186/1471-
evokedpotentials.J.NeuralEng.7, doi:10.1371/journal.pcbi.1000609 F. (1999). “Functional meaning 2202-10-S1-P69
036003. Miller, K., Zanos, S., Fetz, E., den of event-related desynchronization Rickert, J., Cardoso de Oliveira, S.,
Lotte,F.,and Guan,C. (2011). Regu- Nijs,M.,andOjemann,J.(2009b). (ERD)andsynchronization(ERS),” Vaadia, E., Aertsen, A., Rotter, S.,
larizingcommonspatialpatternsto Decouplingthecorticalpowerspec- inEvent-RelatedDesynchronization. andMehring,C.(2005).Encoding
improve BCI designs: unified the- trum reveals real-time representa- HandbookofElectroencephalography ofmovementdirectionindifferent
oryandnewalgorithms.IEEETrans. tion of individual finger move- andClinicalNeurophysiology,Vol.6, frequencyrangesof motorcortical
Biomed.Eng.58,355–362. ments in humans. J. Neurosci. 29, eds G. Pfurtscheller and F. Lopes localfieldpotentials.J.Neurosci.25,
Luo, A., and Sullivan, T. J. (2010). 3132–3137. da Silva (Amsterdam: Elsevier), 8815–8824.
Auser-friendlySSVEP-basedbrain- Müller,K.-R.,Tangermann,M.,Dorn- 51–66. Saab, J., Battes, B., and Grosse-
computer interface using a time- hege,G.,Krauledat,M.,Curio,G., Pfurtscheller, G., Stancak, A. Jr., and Wentrup, M. (2011). Simultaneous
domain classifier. J. Neural Eng. 7, and Blankertz,B. (2008). Machine Neuper, C. (1996). Event-related EEG Recordings with Dry and Wet
26010. learning for real-time single-trial synchronization(ERS)inthealpha elecTrodes in Motor-Imagery. Graz:
Lv,J.,Li,Y.,andGu,Z.(2010).Decod- EEG-analysis:frombrain-computer band–anelectrophysiologicalcorre- Verlag der Technischen Universität
ing hand movement velocity from interfacing to mental state mon- lateofcorticalidling:areview.Int.J. Graz,312–315.
electrocorticogramsignalsduringa itoring. J. Neurosci. Methods 167, Psychophysiol.24,39–46. Sajda, P., Gerson, A., Müller, K.-R.,
drawingtask.Biomed.Eng.Online9, 82–90. Pistohl,T.,Ball,T.,Schulze-Bonhage,A., Blankertz,B.,andParra,L.(2003).A
1–21. Müller-Putz, G. R., Breitwieser, C., Aertsen,A.,andMehring,C.(2008). dataanalysiscompetitiontoevaluate
Mazaheri, A., and Jensen, O. (2008). Tangermann, M., Schreuder, M., Prediction of arm movement tra- machinelearningalgorithmsforuse
Asymmetricamplitudemodulations Tavella, M., Leeb, R., Cincotti, F., jectories from ECoG-recordings in inbrain-computerinterfaces.IEEE
of brain oscillations generate slow Leotta, F., and Neuper, C. (2011). humans. J. Neurosci. Methods 167, Trans.NeuralSyst.Rehabil.Eng.11,
evoked responses. J. Neurosci. 28, TobihybridBCI:principleofanew 105–114. 184–185.
7781–7787. assistive method. Int. J. Bioelectro- Popescu, F., Fazli, S., Badower, Y., Sannelli, C., Braun, M., Tangermann,
McFarland,D.,Miner,L.A.,Vaughan, magn.13,144–145. Blankertz, B., and Müller, K.-R. M.,andMüller,K.-R.(2008).“Esti-
T. M.,and Wolpaw,J. (2000). Mu Naeem, M., Brunner, C., Leeb, R., (2007).Singletrialclassificationof matingnoiseanddimensionalityin
andbetarhythmtopographiesdur- Graimann,B.,andPfurtscheller,G. motor imagination using 6 dry BCI data sets: towards BCI illiter-
ingmotorimageryandactualmove- (2006). Seperability of four-class EEGelectrodes.PLoSONE2,e637. acycomprehension,”inProceedings
ments.BrainTopogr.12,177–186. motorimagerydatausingindepen- doi:10.1371/journal.pone.0000637 of the 4th International Brain-
Mehring,C.,Rickert,J.,Vaadia,E.,Car- dentcomponentsanalysis.J.Neural Porbadnigk, A. K., Antons, J.-N., Computer Interface Workshop and
dosodeOliveira,S.,Aertsen,A.,and Eng.3,208–216. Blankertz,B.,Treder,M. S.,Schle- Training Course 2008, Verlag der
Rotter,S.(2003).Inferenceofhand Nikulin,V.V.,Linkenkaer-Hansen,K., icher,R.,Möller,S.,and Curio,G. TechnischenUniversitätGraz,Graz,
movementsfromlocalfieldpoten- Nolte, G., and Curio, G. (2010). (2010).UsingERPsforassessingthe 26–31.
tialsinmonkeymotorcortex.Nat. Non-zeromeanandasymmetryof (sub)consciousperceptionofnoise. Sannelli,C.,Vidaurre,C.,Müller,K.-R.,
Neurosci.6,1253–1254. neuronaloscillationshavedifferent Conf.Proc.IEEEEng.Med.Biol.Soc. andBlankertz,B.(2011).Common
Mensh,B.D.,Werfel,J.,andSeung,H. implications for evoked responses. 2010,2690–2693. spatial pattern patches – an opti-
S.(2004).BCIcompetition2003– Clin.Neurophysiol.121,186–193. Porbadnigk, A. K., Scholler, S., mized filter ensemble for adaptive
datasetIa:combininggamma-band Nikulin,V.V.,Linkenkaer-Hansen,K., Blankertz, B., Ritz, A., Born, M., brain-computerinterfaces.J.Neural
power with slow cortical poten- Nolte, G., Lemm, S., Müller, K.- Scholl,R.,Müller,K.-R.,Curio,G., Eng.8,025012.
tials to improve single-trial classi- R., Ilmoniemi, R. J., and Curio, andTreder,M.S.(2011).Revealing Sardouie, S. H., and Shamsollahi, M.
ficationofelectroencephalographic G.(2007).Anovelmechanismfor theneuralresponsetoimperceptible B.(2012).Discriminatingmegsig-
signals.IEEETrans.Biomed.Eng.51, evoked responses in human brain. peripheral flicker with machine nals recorded during hand move-
1052–1056. Eur.J.Neurosci.25,3146–3154. learning.Conf.Proc.IEEEEng.Med. ments using selection of effi-
Milekovic, T., Fischer, J., Pistohl, T., Nikulin, V. V., Nolte, G., and Curio, Biol.Soc.2011,3692–3695. cientfeatures.Front.Neurosci.6:42.
Ruescher, J., Schulze-Bonhage, A., G.(2011).Anovelmethodforreli- Quek, M., Boland, D., Williamson, doi:10.3389/fnins.2012.00042
Aertsen,A.,Rickert,J.,Ball,T.,and able and fast extraction of neu- J., Murray-Smith, R., Tavella, M., Schaeff,S.,Treder,M.,Venthur,B.,and
Mehring,C.(2012).Anonlinebrain- ronalEEG/MEGoscillationsonthe Perdikis, S., Schreuder, M., and Blankertz,B.(2011).Motion-based
machine interface using decoding basisofspatio-spectraldecomposi- Tangermann,M. (2011).“Simulat- ERP spellers in a covert attention
of movement direction from the tion.Neuroimage55,1528–1535. ingthefeelofbrain-computerinter- paradigm.Neurosci.Lett.500,e11.
humanelectrocorticogram.J.Neural Nolte,G.,andDassios,G.(2005).Ana- faces for design, development and Schalk, G., Kubánek, J., Miller, K.,
Eng. 9,046003. doi:10.1088/1741- lytic expansion of the EEG lead social interaction,” in Proceedings Anderson, N., Leuthardt, E., Oje-
2560/9/4/046003 fieldforrealisticvolumeconductors. of the 2011 Annual Conference on mann,J.,Limbrick,D.,Moran,D.,
Miller, K., Leuthardt, E., Schalk, G., Phys.Med.Biol.50,3807–3823. Human Factors in Computing Sys- Gerhardt,L.,andWolpaw,J.(2007).
Rao, R., Anderson, N., Moran, Pfurtscheller, G. (1981). Central beta tems,CHI’11,NewYork,NY:ACM, Decoding two-dimensional move-
D., Miller, J., and Ojemann, J. rhythmduringsensorimotoractivi- 25–28. ment trajectories using electrocor-
(2007). Spectral changes in cor- tiesinman.Electroencephalogr.Clin. Rakotomamonjy, A., and Guigue, V. ticographic signals in humans. J.
tical surface potentials during Neurophysiol.51,253–264. (2008).BCIcompetitionIII:dataset NeuralEng.4,264–275.
FrontiersinNeuroscience|Neuroprosthetics July2012|Volume6|Article55|28

Tangermannetal. ReviewoftheBCIcompetitionIV
Schalk,G.,McFarland,D.,Hinterberger, progress. Clin. EEG Neurosci. 42, MEG and EEG. J. Neurosci. 28, Zander, T. O., Lehne, M., Ihme,
T., Birbaumer, N., and Wolpaw, J. 245–252. 1000–1008. K., Jatzev, S., Correia, J., Kothe,
(2004).BCI2000:ageneral-purpose Simons,R.,Miller,G.,Weerts,T.,and Wang, W., Sudre, G. P., Xu, Y., Kass, C., Picht, B., and Nijboer, F.
brain-computerinterface(BCI)sys- Lang,P.J.(1981).Correctingbase- R. E., Collinger, J. L., Degenhart, (2011).A dry EEG-system for sci-
tem. IEEE Trans. Biomed. Eng. 51, line drift artifact in slow poten- A. D., Bagic, A. I., and Weber, entificresearchandbrain-computer
1034–1043. tialrecording.Psychophysiology 19, D. J. (2010). Decoding and corti- interfaces. Front. Neurosci. 5:53.
Schalk, G., Miller, K., Anderson, 691–700. calsourcelocalizationforintended doi:10.3389/fnins.2011.00053
N., Wilson, J., Smyth, M., Oje- Sugiyama, M., Krauledat, M., and movement direction with MEG. J. Zhang, D., Wang, Y., Gao, X., Hong,
mann, J., Moran, D., Wolpaw, J., Müller,K.-R.(2007).Covariateshift Neurophysiol.104,2451–2461. B., and Gao, S. (2007). An algo-
and Leuthardt, E. (2008). Two- adaptationbyimportanceweighted Wang,Y.,andMakeig,S.(2010).Pre- rithm for idle-state detection
dimensional movement control crossvalidation.J.Mach.Learn.Res. dicting intended movement direc- in motor-imagery-based brain-
using electrocorticographic signals 8,1027–1061. tionusingEEGfromhumanposte- computer interface. Comput.
inhumans.J.NeuralEng.5,75. Tangermann,M.,Schreuder,M.,Dähne, riorparietalcortex.Lect.NotesArtif. Intell Neurosci. 2007, 39714. doi:
Schlögl, A., Keinrath, C., Zimmer- S., Höhne, J., Regler, S., Ram- Int.5638,437–446. 10.1155/2007/39714
mann,D.,Scherer,R.,Leeb,R.,and say, A., Quek, M., Williamson, J., Wang,Y.,Zhang,Z.,Li,Y.,Gao,X.,Gao, Zhang, H., Guan, C., Ang, K. K.,
Pfurtscheller, G. (2007a). A fully andMurray-Smith,R.(2011).Opti- S.,andYang,F.(2004).BCIcompeti- and Chin, Z. Y. (2012). Learn-
automated correction method of mizedstimulationeventsforavisual tion2003–datasetIV:analgorithm ingdiscriminativepatternsforself-
EOG artifacts in EEG recordings. ERPBCI.Int.J.Bioelectromagn.13, basedonCSSDandFDAforclas- paced EEG-based motor imagery
Clin.Neurophysiol.118,98–104. 119–120. sifyingsingle-trialEEG.IEEETrans. detection. Front. Neurosci. 6:7.
Schlögl, A., Kronegg, J., Huggins, J., Treder, M. S., Schmidt, N. M., Biomed.Eng.51,1081–1086. doi:10.3389/fnins.2012.00007
and Mason, S. (2007b). “Evalua- and Blankertz, B. (2011). Gaze- Wei,Q.,Gao,X.,andGao,S.(2006).Fea-
tion criteria in BCI research,” in independentbrain-computerinter- tureextractionandsubsetselection
TowardBrain-ComputerInterfacing, facesbasedoncovertattentionand forclassifyingsingle-trialECoGdur- Conflict of Interest Statement: The
Chapt.19,edsG.Dornhege,J.Mil- feature attention. J. Neural Eng. 8, ingmotorimagery.Conf.Proc.IEEE authors declare that the research was
lán,T.Hinterberger,D.J.McFarland, 066003. Eng.Med.Biol.Soc.1,1589–1592. conductedintheabsenceofanycom-
andK.-R.Müller(Cambridge:MIT Velliste,M.,Perel,S.,Spalding,M.,Whit- Winkler,I.,Haufe,S.,andTangermann, mercial or financial relationships that
Press),327–342. ford, A., and Schwartz, A. (2008). M.(2011).Automaticclassification couldbeconstruedasapotentialcon-
Schreuder, M., Blankertz, B., and Cortical control of a prosthetic of artifactual ICA-components for flictofinterest.
Tangermann, M. (2010). A arm for self-feeding. Nature 453, artifact removal in EEG signals.
new auditory multi-class brain- 1098–1101. Behav.BrainFunct.7,30. Received:17December2011;paperpend-
computer interface paradigm: Vidaurre, C., Sannelli, C., Müller, K.- Witte,M.,Galan,F.,Waldert,S.,Aertsen, ingpublished:15January2012;accepted:
spatial hearing as an informa- R., and Blankertz, B. (2011). Co- A.,Rotter,S.,Birbaumer,N.,Braun, 30March2012;publishedonline:13July
tive cue. PLoS ONE 5, e9813. adaptive calibration to improve C.,andMehring,C.(2010).“Anon- 2012.
doi:10.1371/journal.pone.0009813 BCI efficiency. J. Neural Eng. 8, lineBCIsystemusinghandmove- Citation:Tangermann M,Müller K-R,
Schreuder, M., Rost, T., and Tanger- 025009. ment recognition from MEG,” in AertsenA,BirbaumerN,BraunC,Brun-
mann, M. (2011). Listen, you Vidaurre, C., and Schlögl, A. (2008). 4thInternationalBCIMeeting2010, ner C,Leeb R,Mehring C,Miller KJ,
are writing! Speeding up online “Comparison of adaptive features Asilomar. Müller-Putz GR,Nolte G,Pfurtscheller
spelling with a dynamic audi- withlineardiscriminantclassifierfor Wojcikiewicz, W., Vidaurre, C., and G, Preissl H, Schalk G, Schlögl A,
tory BCI. Front. Neurosci. 5:112. BrainComputerInterfaces,”inPro- Kawanabe, M. (2011). “Stationary Vidaurre C, Waldert S and Blankertz
doi:10.3389/fnins.2011.00112 ceedingsofthe30thAnnualInterna- common spatial patterns: towards B (2012) Review of the BCI compe-
Schröder, M., Bogdan, M., Rosenstiel, tionalConferenceoftheIEEEEngi- robustclassificationofnon-station- tition IV. Front. Neurosci. 6:55. doi:
W.,Hinterberger,T.,andBirbaumer, neeringinMedicineandBiologySoci- aryeegsignals,”inAcoustics,Speech 10.3389/fnins.2012.00055
N.(2003).“AutomatedEEGfeature ety2008,173–176. andSignalProcessing(ICASSP),2011 ThisarticlewassubmittedtoFrontiersin
selectionforbraincomputerinter- vonBünau,P.,Meinecke,F.C.,Király, IEEE International Conference on, Neuroprosthetics,aspecialtyofFrontiers
faces,” in Proceedings of the First F.,andMüller,K.-R.(2009).Find- Prague,577–580. inNeuroscience.
International IEEE EMBS Confer- ing stationary subspaces in multi- Wolpaw,J. R.,Birbaumer,N.,McFar- Copyright © 2012 Tangermann,
ence on Neural Engineering, Capri, variate time series. Phys. Rev. Lett. land, D. J., Pfurtscheller, G., and Müller, Aertsen, Birbaumer, Braun,
626–629. 103,214101. Vaughan, T. M. (2002). Brain- Brunner,Leeb,Mehring,Miller,Müller-
Shenoy, P., Krauledat, M., Blankertz, Waldert,S.,Pistohl,T.,Braun,C.,Ball, computer interfaces for communi- Putz, Nolte, Pfurtscheller, Preissl,
B., Rao, R. P. N., and Müller, K.- T., Aertsen, A., and Mehring, C. cationandcontrol.Clin.Neurophys- Schalk, Schlögl, Vidaurre, Waldert
R.(2006).Towardsadaptiveclassi- (2009). A review on directional iol.113,767–791. and Blankertz. This is an open-access
fication for BCI. J. Neural Eng. 3, information in neural signals for Xu,N.,Gao,X.,Hong,B.,Miao,X.,Gao, articledistributedunderthetermsofthe
R13–R23. brain-machineinterfaces.J.Physiol. S.,andYang,F.(2004).BCIcompe- CreativeCommonsAttributionLicense,
Silvoni, S., Ramos-Murguialday, A., Paris103,244–254. tition2003–datasetIIb:enhanc- which permits use, distribution and
Cavinato, M.,Volpato, C., Cisotto, Waldert, S., Preissl, H., Demandt, E., ingP300wavedetectionusingICA- reproduction in other forums, provided
G.,Turolla,A.,Piccione,F.,andBir- Braun,C.,Birbaumer,N.,Aertsen, basedsubspaceprojectionsforBCI theoriginalauthorsandsourcearecred-
baumer,N.(2011).Brain-computer A.,and Mehring,C. (2008). Hand applications. IEEE Trans. Biomed. itedandsubjecttoanycopyrightnotices
interface in stroke: a review of movementdirectiondecodedfrom Eng.51,1067–1072. concerninganythird-partygraphicsetc.
www.frontiersin.org July2012|Volume6|Article55|29

| Tangermannetal. |          |     |     |     |       |                       |     | ReviewoftheBCIcompetitionIV |     |     |     |
| --------------- | -------- | --- | --- | --- | ----- | --------------------- | --- | --------------------------- | --- | --- | --- |
| A.              | APPENDIX |     |     |     | [s,h] | = sload(’A01T.gdf’,0, |     |                             |     |     |     |
A.1. DATASET2A
AllfilesarelistedinTableA1.Notethatthetestsetswillbemade ’OVERFLOWDETECTION:OFF’);
availableafterthedeadlineofthecompetition(exceptforonefile
from subject A01, which serves as an example). The GDF files The workspace will then contain two variables, namely the
| can      | be loaded                          | using the open-source | toolbox BioSig, | available    |           |                        |        |         |          |          |      |
| -------- | ---------------------------------- | --------------------- | --------------- | ------------ | --------- | ---------------------- | ------ | ------- | -------- | -------- | ---- |
|          |                                    |                       |                 |              | signals s | and a header structure |        | h. The  | signal   | variable | con- |
| for free | at http://biosig.sourceforge.net/. |                       | There are       | versions for |           |                        |        |         |          |          |      |
|          |                                    |                       |                 |              | tains 25  | channels (the first    | 22 are | EEG and | the last | 3 are    | EOG  |
Octave1/FreeMat2/MATLAB3aswellasalibraryforC/C++.
|     |     |     |     |     | signals). | The header structure | contains | event | information |     | that |
| --- | --- | --- | --- | --- | --------- | -------------------- | -------- | ----- | ----------- | --- | ---- |
AGDFfilecanbeloadedwiththeBioSigtoolboxwiththefol-
describesthestructureofthedataovertime.Thefollowingfields
lowingcommandinOctave/FreeMat/MATLAB(forC/C++,the
|     |     |     |     |     | provide important | information | for | the evaluation |     | of this | data |
| --- | --- | --- | --- | --- | ----------------- | ----------- | --- | -------------- | --- | ------- | ---- |
correspondingfunctionHDRTYPE∗sopenandsize_tsreadmust
set:
becalled):
| [s,h] | = sload(’A01T.gdf’); |     |     |     | h.EVENT.TYP |     |     |     |     |     |     |
| ----- | -------------------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
h.EVENT.POS
h.EVENT.DUR
Notethattherunsareseparatedby100missingvalues,which
areencodedasnot-a-numbers(NaN)bydefault.Alternatively,this
behaviorcanbeturnedoffandthemissingvalueswillbeencoded
|     |     |     |     |     | The position | of an event | in  | samples | is  | contained | in  |
| --- | --- | --- | --- | --- | ------------ | ----------- | --- | ------- | --- | --------- | --- |
asthenegativemaximumvaluesasstoredinthefilewith:
|     |     |     |     |     | h.EVENT.POS. | The corresponding |     | type | can | be found | in  |
| --- | --- | --- | --- | --- | ------------ | ----------------- | --- | ---- | --- | -------- | --- |
h.EVENT.TYP,andthedurationofthatparticulareventisstored
inh.EVENT.DUR.Thetypesusedinthisdatasetaredescribedin
1http://www.gnu.org/software/octave/
2http://freemat.sourceforge.net/ TableA2(hexadecimalvalues,decimalnotationinparentheses).
3TheMathWorks,Inc.,Natick,MA,USA Note that the class labels (i.e.,1,2,3,4 corresponding to event
types769,770,771,772)areonlyprovidedforthetrainingdata
TableA1|(DataSet2a).Listofallfilescontainedinthedataset2a,the
andnotforthetestingdata.
strikedouttestdatasetswereprovidedonlyafterthedeadlineofthe The trials containing artifacts as scored by experts
competition. are marked as events with the type 1023. In addition,
h.ArtifactSelectioncontainsalistofalltrials,with0cor-
| ID  |     | Training |     | Test |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
respondingtoacleantrialand1correspondingtoatrialcontaining
anartifact.
| 1   |     | A01T.gdf |     | A01E.gdf |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
2 A02T.gdf A02E.gdf SigViewer0.2(orhigher)canbeusedtoviewandannotateGDF
3 A03T.gdf A03E.gdf files.SigViewerisavailableathttp://sigviewer.sourceforge.net/.
| 4   |     | A04T.gdf |     | A04E.gdf |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
| 5   |     | A05T.gdf |     | A05E.gdf |     |     |     |     |     |     |     |
A.2. DATASET2B
| 6   |     | A06T.gdf |     | A06E.gdf |              |                     |         |     |         |           |     |
| --- | --- | -------- | --- | -------- | ------------ | ------------------- | ------- | --- | ------- | --------- | --- |
|     |     |          |     |          | All files    | are listed in Table | A3.     | The | GDF     | files can | be  |
| 7   |     | A07T.gdf |     | A07E.gdf |              |                     |         |     |         |           |     |
|     |     |          |     |          | loaded using | the open-source     | toolbox |     | BioSig, | available | for |
| 8   |     | A08T.gdf |     | A08E.gdf |              |                     |         |     |         |           |     |
| 9   |     | A09T.gdf |     | A09E.gdf |              |                     |         |     |         |           |     |
TableA3|(DataSet2b).Listofallfilescontainedinthedataset2b,the
NotethatduetotechnicalproblemstheEOGblockisshorterforsubjectA04T strikedouttestdatasetswillbeprovidedafterthedeadlineofthe
| andcontainsonlytheeyemovementcondition. |     |     |     |     | competition. |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
TableA2|(DataSet2a).Listofeventtypesindataset2a(thefirst ID Training Test
columncontainsdecimalvaluesandthesecondhexadecimalvalues).
|     |           |        |                       |     | 1   | B0101T,B0102T,B0103T |     |     |     | B0104E,B0105E |     |
| --- | --------- | ------ | --------------------- | --- | --- | -------------------- | --- | --- | --- | ------------- | --- |
|     | Eventtype |        | Description           |     | 2   | B0201T,B0202T,B0203T |     |     |     | B0204E,B0205E |     |
|     |           |        |                       |     | 3   | B0301T,B0302T,B0303T |     |     |     | B0304E,B0305E |     |
| 276 |           | 0×0114 | IdlingEEG(eyesopen)   |     |     |                      |     |     |     |               |     |
|     |           |        |                       |     | 4   | B0401T,B0402T,B0403T |     |     |     | B0404E,B0405E |     |
| 277 |           | 0×0115 | IdlingEEG(eyesclosed) |     |     |                      |     |     |     |               |     |
|     |           |        |                       |     | 5   | B0501T,B0502T,B0503T |     |     |     | B0504E,B0505E |     |
0×0300
| 768 |     |        | Startofatrial          |     | 6   | B0601T,B0602T,B0603T |     |     |     | B0604E,B0605E |     |
| --- | --- | ------ | ---------------------- | --- | --- | -------------------- | --- | --- | --- | ------------- | --- |
| 769 |     | 0×0301 | Cueonsetleft(class1)   |     |     |                      |     |     |     |               |     |
|     |     |        |                        |     | 7   | B0701T,B0702T,B0703T |     |     |     | B0704E,B0705E |     |
| 770 |     | 0×0302 | Cueonsetright(class2)  |     |     |                      |     |     |     |               |     |
|     |     |        |                        |     | 8   | B0801T,B0802T,B0803T |     |     |     | B0804E,B0805E |     |
| 771 |     | 0×0303 | Cueonsetfoot(class3)   |     |     |                      |     |     |     |               |     |
|     |     |        |                        |     | 9   | B0901T,B0902T,B0903T |     |     |     | B0904E,B0905E |     |
| 772 |     | 0×0304 | Cueonsettongue(class4) |     |     |                      |     |     |     |               |     |
783 0×030F Cueunknown Thefirsttwosessions(...01T,...02T)containtrainingdatawithoutfeedback,and
1023 0×03FF Rejectedtrial thelastthreesessions(...03T,...04E,...05E)withsmileyfeedback.Note:Due
0×0430
1072 Eyemovements totechnicalproblemsnorecordingforEOGestimation(eyesopen,closed,eye
32766 0×7FFE Startofanewrun movements)existsinsessionB0102TandB0504E.
FrontiersinNeuroscience|Neuroprosthetics July2012|Volume6|Article55|30

| Tangermannetal.                         |     |     |     |       |     |          |     |     |     |     |     | ReviewoftheBCIcompetitionIV |     |
| --------------------------------------- | --- | --- | --- | ----- | --- | -------- | --- | --- | --- | --- | --- | --------------------------- | --- |
| free at http://biosig.sourceforge.net/. |     |     |     | There | are | versions | for |     |     |     |     |                             |     |
TableA4|(DataSet2b).Listofeventtypesindataset2b(thefirst
Octave4/MATLAB5aswellasalibraryforC/C++.
columncontainsdecimalvaluesandthesecondhexadecimalvalues).
| A GDF | file can | be loaded | with | the BioSig | toolbox | with | the |     |     |     |     |     |     |
| ----- | -------- | --------- | ---- | ---------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
followingcommandinOctave/MATLAB(forC/C++,thecorre- Eventtype Description
spondingfunctionHDRTYPE∗sopenandsize_tsreadmustbe
0×0114
|     |     |     |     |     |     |     |     | 276 |     |     |     | IdlingEEG(eyesopen) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- |
called):
|         |                      |     |     |     |     |     |     | 277 |     | 0×0115 |     | IdlingEEG(eyesclosed) |     |
| ------- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --------------------- | --- |
|         |                      |     |     |     |     |     |     | 768 |     | 0×0300 |     | Startofatrial         |     |
| [s,h] = | sload(’B0101T.gdf’); |     |     |     |     |     |     |     |     |        |     |                       |     |
|         |                      |     |     |     |     |     |     | 769 |     | 0×0301 |     | Cueonsetleft(class1)  |     |
Notethattherunsareseparatedby100missingvalues,which 770 0×0302 Cueonsetright(class2)
|     |     |     |     |     |     |     |     | 781 |     | 0×030D |     | BCIfeedback(continuous) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ----------------------- | --- |
areencodedasnot-a-numbers(NaN)bydefault.Alternatively,this
|     |     |     |     |     |     |     |     | 783 |     | 0×030F |     | Cueunknown |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ---------- | --- |
behaviorcanbeturnedoffandthemissingvalueswillbeencoded
0×03FF
asthenegativemaximumvaluesasstoredinthefilewith: 1023 Rejectedtrial
|                           |                     |     |     |     |     |     |     | 1077  |     | 0×0435 |     | Horizontaleyemovement |     |
| ------------------------- | ------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | ------ | --- | --------------------- | --- |
|                           |                     |     |     |     |     |     |     | 1078  |     | 0×0436 |     | Verticaleyemovement   |     |
| [s,h] =                   | sload(’AO1T.gdf’,0, |     |     |     |     |     |     |       |     |        |     |                       |     |
|                           |                     |     |     |     |     |     |     | 1079  |     | 0×0437 |     | Eyerotation           |     |
| ’OVERFLOWDETECTION:OFF’); |                     |     |     |     |     |     |     | 1081  |     | 0×0439 |     | Eyeblinks             |     |
|                           |                     |     |     |     |     |     |     | 32766 |     | 0×7FFE |     | Startofanewrun        |     |
Theworkspacewillthencontaintwovariables,namelythesig-
| nals s and | the header | structure | h.  | The signal | variable | contains |     |     |     |     |     |     |     |
| ---------- | ---------- | --------- | --- | ---------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
h.EVENT.TYP,andthedurationofthatparticulareventisstored
| 6 channels | (the first | 3 are EEG | and | the last | 3 are | EOG signals). |     |     |     |     |     |     |     |
| ---------- | ---------- | --------- | --- | -------- | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- |
inh.EVENT.DUR.Thetypesusedinthisdatasetaredescribed
| The header     | structure                                 | contains | event | information |     | that describes |     |            |              |                |     |          |              |
| -------------- | ----------------------------------------- | -------- | ----- | ----------- | --- | -------------- | --- | ---------- | ------------ | -------------- | --- | -------- | ------------ |
|                |                                           |          |       |             |     |                |     | in TableA4 | (hexadecimal | values,decimal |     | notation | in parenthe- |
| thestructureof | thedataovertime.Thefollowingfieldsprovide |          |       |             |     |                |     |            |              |                |     |          |              |
ses).Notethattheclasslabels(i.e.,1and2,correspondingtoevent
importantinformationfortheevaluationofthisdataset:
types769and770)areonlyprovidedforthetrainingdataandnot
| h.EVENT.TYP |     |     |     |     |     |     |     | forthetestingdata. |            |     |           |           |            |
| ----------- | --- | --- | --- | --- | --- | --- | --- | ------------------ | ---------- | --- | --------- | --------- | ---------- |
|             |     |     |     |     |     |     |     | The trials         | containing |     | artifacts | as scored | by experts |
h.EVENT.POS
|     |     |     |     |     |     |     |     | are marked | as  | events with | the | type 1023. | In addition, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----------- | --- | ---------- | ------------ |
h.EVENT.DUR
h.ArtifactSelectioncontainsalistofalltrials,with0cor-
The position of an event in samples is contained in respondingtoacleantrialand1correspondingtoatrialcontaining
| h.EVENT.POS. |     |                   |     |      |     |          |     | anartifact. |           |         |           |             |                |
| ------------ | --- | ----------------- | --- | ---- | --- | -------- | --- | ----------- | --------- | ------- | --------- | ----------- | -------------- |
|              |     | The corresponding |     | type | can | be found | in  |             |           |         |           |             |                |
|              |     |                   |     |      |     |          |     | In order    | to view   | the GDF | files,    | the viewing | and scoring    |
|              |     |                   |     |      |     |          |     | application | SigViewer | v0.2    | or higher | (part of    | BioSig) can be |
4http://www.gnu.org/software/octave/
used.
5TheMathWorks,Inc.,Natick,MA,USA
| www.frontiersin.org |     |     |     |     |     |     |     |     |     |     |     | July2012|Volume6|Article55|31 |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- |


==============================================================================
APPENDED SECOND SOURCE (not part of the Frontiers article above)
Official BCI Competition IV data set 2a description, `desc_2a.pdf`,
retrieved 2026-07-31 from https://www.bbci.de/competition/iv/desc_2a.pdf
Brunner C, Leeb R, Muller-Putz GR, Schlogl A, Pfurtscheller G.
'BCI Competition 2008 -- Graz data set A'.
Appended because the Frontiers review does not carry the per-dataset
recording parameters this strand's card schema requires.
==============================================================================

| BCI          | Competition | 2008  | – Graz         | data set      | A      |
| ------------ | ----------- | ----- | -------------- | ------------- | ------ |
| C. Brunner1, | R. Leeb1,   | G. R. | Mu¨ller-Putz1, | A. Schl¨ogl2, | and G. |
Pfurtscheller1
1Institute for Knowledge Discovery, Graz University of Technology,
Austria
| 2Institute   | for Human-Computer |             | Interfaces, | Graz University | of  |
| ------------ | ------------------ | ----------- | ----------- | --------------- | --- |
|              |                    | Technology, | Austria     |                 |     |
| Experimental | paradigm           |             |             |                 |     |
This data set consists of EEG data from 9 subjects. The cue-based BCI
paradigm consisted of four different motor imagery tasks, namely the imag-
ination of movement of the left hand (class 1), right hand (class 2), both
feet (class 3), and tongue (class 4). Two sessions on different days were
recorded for each subject. Each session is comprised of 6 runs separated by
short breaks. One run consists of 48 trials (12 for each of the four possible
| classes), yielding | a total | of 288 trials | per session. |     |     |
| ------------------ | ------- | ------------- | ------------ | --- | --- |
At the beginning of each session, a recording of approximately 5 minutes
was performed to estimate the EOG influence. The recording was divided
into 3 blocks: (1) two minutes with eyes open (looking at a fixation cross
on the screen), (2) one minute with eyes closed, and (3) one minute with
eye movements. The timing scheme of one session is illustrated in Figure 1.
Note that due to technical problems the EOG block is shorter for subject
and contains only the eye movement condition (see Table 1 for a list
A04T
of all subjects).
The subjects were sitting in a comfortable armchair in front of a com-
puter screen. At the beginning of a trial (t = 0s), a fixation cross appeared
on the black screen. In addition, a short acoustic warning tone was pre-
sented. After two seconds (t = 2s), a cue in the form of an arrow pointing
either to the left, right, down or up (corresponding to one of the four classes
|     | Figure | 1: Timing | scheme of | one session. |     |
| --- | ------ | --------- | --------- | ------------ | --- |
1

Figure 2: Timing scheme of the paradigm.
left hand, right hand, foot or tongue) appeared and stayed on the screen for
1.25s. This prompted the subjects to perform the desired motor imagery
task. No feedback was provided. The subjects were ask to carry out the
motor imagery task until the fixation cross disappeared from the screen at
t = 6s. A short break followed where the screen was black again. The
paradigm is illustrated in Figure 2.
Data recording
Twenty-two Ag/AgCl electrodes (with inter-electrode distances of 3.5cm)
were used to record the EEG; the montage is shown in Figure 3 left. All
signals were recorded monopolarly with the left mastoid serving as reference
and the right mastoid as ground. The signals were sampled with 250Hz and
bandpass-filteredbetween0.5Hzand100Hz. Thesensitivityoftheamplifier
was set to 100µV. An additional 50Hz notch filter was enabled to suppress
line noise.
Figure 3: Left: Electrode montage corresponding to the international 10-20
system. Right: Electrode montage of the three monopolar EOG channels.
In addition to the 22 EEG channels, 3 monopolar EOG channels were
2

recorded and also sampled with 250Hz (see Figure 3 right). They were
bandpass filtered between 0.5Hz and 100Hz (with the 50Hz notch filter
enabled), and the sensitivity of the amplifier was set to 1mV. The EOG
channels are provided for the subsequent application of artifact processing
| methods | [1] | and | must | not be | used for classification. |     |
| ------- | --- | --- | ---- | ------ | ------------------------ | --- |
A visual inspection of all data sets was carried out by an expert and
trials containing artifacts were marked. Eight out of the total of nine data
| sets | were analyzed |             | in [2, | 3]. |     |     |
| ---- | ------------- | ----------- | ------ | --- | --- | --- |
| Data | file          | description |        |     |     |     |
All data sets are stored in the General Data Format for biomedical signals
(GDF), one file per subject and session. However, only one session contains
the class labels for all trials, whereas the other session will be used to test
the classifier and hence to evaluate the performance. All files are listed
in Table 1. Note that the evaluation sets will be made available after the
deadlineofthecompetition(exceptforonefilefromsubjectA01whichserves
as an example). The GDF files can be loaded using the open-source toolbox
BioSig, available for free at http://biosig.sourceforge.net/. There are
versions for Octave1/FreeMat2/MATLAB3 as well as a library for C/C++.
|     |     |     |     | ID  | Training Evaluation |     |
| --- | --- | --- | --- | --- | ------------------- | --- |
|     |     |     |     | 1   | A01T.gdf A01E.gdf   |     |
|     |     |     |     | 2   | A02T.gdf A02E.gdf   |     |
|     |     |     |     | 3   | A03T.gdf A03E.gdf   |     |
|     |     |     |     | 4   | A04T.gdf A04E.gdf   |     |
|     |     |     |     | 5   | A05T.gdf A05E.gdf   |     |
|     |     |     |     | 6   | A06T.gdf A06E.gdf   |     |
|     |     |     |     | 7   | A07T.gdf A07E.gdf   |     |
|     |     |     |     | 8   | A08T.gdf A08E.gdf   |     |
|     |     |     |     | 9   | A09T.gdf A09E.gdf   |     |
Table 1: List of all files contained in the data set, the striked out evaluation
data sets will be provided after the deadline of the competition. Note that
due to technical problems the EOG block is shorter for subject A04T and
| contains | only | the | eye movement |     | condition. |     |
| -------- | ---- | --- | ------------ | --- | ---------- | --- |
A GDF file can be loaded with the BioSig toolbox with the following
command in Octave/FreeMat/MATLAB (for C/C++, the corresponding
| function | HDRTYPE* |     | sopen              | and | size t sread | must be called): |
| -------- | -------- | --- | ------------------ | --- | ------------ | ---------------- |
|          | [s, h]   | =   | sload(’A01T.gdf’); |     |              |                  |
1http://www.gnu.org/software/octave/
2http://freemat.sourceforge.net/
3The
|     | MathWorks, |     | Inc., | Natick, | MA, USA |     |
| --- | ---------- | --- | ----- | ------- | ------- | --- |
3

|     | Event | type   | Description   |              |           |
| --- | ----- | ------ | ------------- | ------------ | --------- |
|     | 276   | 0x0114 | Idling        | EEG (eyes    | open)     |
|     | 277   | 0x0115 | Idling        | EEG (eyes    | closed)   |
|     | 768   | 0x0300 | Start of      | a trial      |           |
|     | 769   | 0x0301 | Cue onset     | left (class  | 1)        |
|     | 770   | 0x0302 | Cue onset     | right (class | 2)        |
|     | 771   | 0x0303 | Cue onset     | foot (class  | 3)        |
|     | 772   | 0x0304 | Cue onset     | tongue       | (class 4) |
|     | 783   | 0x030F | Cue unknown   |              |           |
|     | 1023  | 0x03FF | Rejected      | trial        |           |
|     | 1072  | 0x0430 | Eye movements |              |           |
|     | 32766 | 0x7FFE | Start of      | a new run    |           |
Table 2: List of event types (the first column contains decimal values and
| the second | hexadecimal | values). |     |     |     |
| ---------- | ----------- | -------- | --- | --- | --- |
Notethattherunsareseparatedby100missingvalues,whichareencodedas
not-a-numbers (NaN) by default. Alternatively, this behavior can be turned
off and the missing values will be encoded as the negative maximum values
| as stored | in the file with:      |     |     |                           |     |
| --------- | ---------------------- | --- | --- | ------------------------- | --- |
| [s,       | h] = sload(’A01T.gdf’, |     | 0,  | ’OVERFLOWDETECTION:OFF’); |     |
The workspace will then contain two variables, namely the signals s and
a header structure h. The signal variable contains 25 channels (the first 22
are EEG and the last 3 are EOG signals). The header structure contains
event information that describes the structure of the data over time. The
followingfieldsprovideimportantinformationfortheevaluationofthisdata
set:
h.EVENT.TYP
h.EVENT.POS
h.EVENT.DUR
The position of an event in samples is contained in h.EVENT.POS. The cor-
responding type can be found in h.EVENT.TYP, and the duration of that
particular event is stored in h.EVENT.DUR. The types used in this data set
are described in Table 2 (hexadecimal values, decimal notation in parenthe-
ses). Note that the class labels (i.e., 1, 2, 3, 4 corresponding to event types
769, 770, 771, 772) are only provided for the training data and not for the
testing data.
The trials containing artifacts as scored by experts are marked as events
with the type 1023. In addition, h.ArtifactSelection contains a list of all
trials, with 0 corresponding to a clean trial and 1 corresponding to a trial
| containing | an artifact. |     |     |     |     |
| ---------- | ------------ | --- | --- | --- | --- |
4

In order to view the GDF files, the viewing and scoring application
SigViewer v0.2 or higher (part of BioSig) can be used.
Evaluation
Participants should provide a continuous classification output for each sam-
ple in the form of class labels (1, 2, 3, 4), including labeled trials and trials
marked as artifact. A confusion matrix will then be built from all artifact-
free trials for each time point. From these confusion matrices, the time
course of the accuracy as well as the kappa coefficient will be obtained [5].
The algorithm used for this evaluation will be provided in BioSig. The
winner is the algorithm with the largest kappa value X.KAP00.
Duetothefactthattheevaluationdatasetswillnotbedistributeduntil
the end of the competition, the submissions must be programs that accept
EEGdata(thestructureofthisdatamustbethesameasusedinalltraining
sets4) as input and produce the aforementioned class label vector.
Since three EOG channels are provided, it is required to remove EOG
artifacts before the subsequent data processing using artifact removal tech-
niques such as highpass filtering or linear regression [4]. In order to enable
the application of other correction methods, we have opted for a maximum
transparency approach and provided the EOG channels; at the same time
we request that artifacts do not influence the classification result.
All algorithms must be causal, meaning that the classification output at
time k may only depend on the current and past samples x ,x ,...,x .
k k−1 0
In order to check whether the causality criterion and the artifact processing
requirements are fulfilled, all submissions must be open source, including
all additional libraries, compilers, programming languages, and so on (for
example, Octave/FreeMat, C++, Python, ...). Note that submissions can
also be written in the closed-source development environment MATLAB as
long as the code is executable in Octave. Similarily, C++ programs can be
written and compiled with a Microsoft or Intel compiler, but the code must
also compile with g++.
References
[1] M. Fatourechi, A. Bashashati, R. K. Ward, G. E. Birch. EMG and
EOG artifacts in brain computer interface systems: a survey. Clinical
Neurophysiology 118, 480–494, 2007.
4Oneevaluationdatasetisdistributedfromthebeginningofthecompetitiontoenable
participants to test their program and to ensure that it produces the desired output.
5

[2] M. Naeem, C. Brunner, R. Leeb, B. Graimann, G. Pfurtscheller. Seper-
ability of four-class motor imagery data using independent components
| analysis. | Journal of Neural | Engineering | 3, 208–216, | 2006. |
| --------- | ----------------- | ----------- | ----------- | ----- |
[3] C. Brunner, M. Naeem, R. Leeb, B. Graimann, G. Pfurtscheller. Spa-
tial filtering and selection of optimized components in four class motor
imagery data using independent components analysis. Pattern Recog-
| nition Letters | 28, 957–964, | 2007. |     |     |
| -------------- | ------------ | ----- | --- | --- |
[4] A. Schl¨ogl, C. Keinrath, D. Zimmermann, R. Scherer, R. Leeb, G.
Pfurtscheller. A fully automated correction method of EOG artifacts in
| EEG recordings. | Clinical | Neurophysiology | 118, 98–104, | 2007. |
| --------------- | -------- | --------------- | ------------ | ----- |
[5] A. Schl¨ogl, J. Kronegg, J. E. Huggins, S. G. Mason. Evaluation criteria
in BCI research. In: G. Dornhege, J. del R. Mill´an, T. Hinterberger,
D. J. McFarland, K.-R. Mu¨ller (Eds.). Toward brain-computer inter-
| facing, MIT | Press, 327–342, | 2007. |     |     |
| ----------- | --------------- | ----- | --- | --- |
6