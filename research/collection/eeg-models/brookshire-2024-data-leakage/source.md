TYPE BriefResearchReport
PUBLISHED 03May2024
DOI 10.3389/fnins.2024.1373515
Data leakage in deep learning
studies of translational EEG
OPENACCESS
EDITEDBY
JürgenDammers,
HelmholtzAssociationofGermanResearch GeoffreyBrookshire1*‡,JakeKasper1‡,NicholasM.Blauch1,2†,
Centres(HZ),Germany
YunanCharlesWu1,RyanGlatt3,DavidA.Merrill3,4,5,
REVIEWEDBY
SpencerGerrol1,KeithJ.Yoder1,ColinQuirk1 andChéLucero1
PhilippLohmann,
ResearchCenterJuelich,Germany
YongxiaZhou, 1SPARKNeuroInc.,NewYork,NY,UnitedStates,2NeuroscienceInstitute,CarnegieMellonUniversity,
UniversityofSouthernCalifornia, Pittsburgh,PA,UnitedStates,3PacificBrainHealthCenter,PacificNeuroscienceInstituteand
UnitedStates Foundation,SantaMonica,CA,UnitedStates,4SaintJohn’sCancerInstituteatProvidenceSaintJohn’s
HealthCenter,SantaMonica,CA,UnitedStates,5PsychiatryandBiobehavioralSciences,Semel
*CORRESPONDENCE InstituteforNeuroscienceandHumanBehavior,DavidGeffenSchoolofMedicineatUniversityof
GeoffreyBrookshire California,LosAngeles,LosAngeles,CA,UnitedStates
geoff.brookshire@sparkneuro.com
†PRESENTADDRESS
Agrowingnumberofstudiesapplydeepneuralnetworks(DNNs)torecordings
NicholasM.Blauch,
HarvardUniversity,Cambridge,MA, of human electroencephalography (EEG) to identify a range of disorders. In
UnitedStates many studies, EEG recordings are split into segments, and each segment is
‡Theseauthorshavecontributedequallyto randomly assigned to the training or test set. As a consequence, data from
thisworkandsharefirstauthorship individual subjects appears in both the training and the test set. Could high
RECEIVED19January2024 test-setaccuracyreflectdataleakagefromsubject-specificpatternsinthedata,
ACCEPTED04April2024 ratherthanpatternsthatidentifyadisease?Weaddressthisquestionbytesting
PUBLISHED03May2024
the performance of DNN classifiers using segment-based holdout (in which
CITATION segments from one subject can appear in both the training and test set), and
BrookshireG,KasperJ,BlauchNM,WuYC,
comparing this to their performance using subject-based holdout (where all
GlattR,MerrillDA,GerrolS,YoderKJ,QuirkC
andLuceroC(2024)Dataleakageindeep segmentsfromonesubjectappearexclusivelyineitherthetrainingsetorthetest
learningstudiesoftranslationalEEG. set).Intwodatasets(oneclassifyingAlzheimer’sdisease,andtheotherclassifying
Front.Neurosci.18:1373515.
epileptic seizures), we find that performance on previously-unseen subjects is
doi:10.3389/fnins.2024.1373515
stronglyoverestimatedwhenmodelsaretrainedusingsegment-basedholdout.
COPYRIGHT
©2024 Brookshire,Kasper,Blauch,Wu,Glatt, Finally,wesurveytheliteratureandfindthatthemajorityoftranslationalDNN-
Merrill,Gerrol,Yoder,QuirkandLucero.Thisis EEGstudiesusesegment-basedholdout.MostpublishedDNN-EEGstudiesmay
anopen-accessarticledistributedunderthe
dramaticallyoverestimatetheirclassificationperformanceonnewsubjects.
termsoftheCreativeCommonsAttribution
License(CCBY).Theuse,distributionor
reproductioninotherforumsispermitted,
KEYWORDS
providedtheoriginalauthor(s)andthe
copyrightowner(s)arecreditedandthatthe electroencephalography, deep neural networks, data leakage, cross-validation,
originalpublicationinthisjournaliscited,in Alzheimer’sdisease,epilepsy
accordancewithacceptedacademicpractice.
Nouse,distributionorreproductionis
permittedwhichdoesnotcomplywiththese 1 Introduction
terms.
Translationalneurosciencestudiesincreasinglyturntodeepneuralnetwork(DNN)
models to find structure in neural data. The power of DNN models comes from their
abilitytodiscoverpatternsinthedatathatresearcherswouldnothavebeenabletospecify.
DNNclassifiershavethepotentialtorevolutionizemedicalcarebyincreasingthespeed,
accuracy, and availability of diagnosis (Mall et al., 2023). DNNs have been trained on a
varietyofimagingtechniquestoidentifyawiderangeofclinicalconditions.Manyofthese
studiesuseDNNstodiagnosediseasesbasedonanatomicalneuroimaging.Forexample,
DNNmodelscanidentifyAlzheimer’sdisease(AD)usingstructuralmagneticresonance
imaging(MRI)(Wenetal.,2020),andavarietyofcancersandbraininjuriesusingCT
scans(Hosnyetal.,2018;Kakaetal.,2021).Inadditiontoanatomicaldata,alargenumber
ofstudieshaveusedDNNstoidentifydiseasesfromfunctionalneuroimagingdata.For
example,DNNswithfunctionalMRIshowpromiseforidentifyingAD,Autismspectrum
disorders,attention-deficit/hyperactivitydisorder(ADHD),andschizophrenia(Wenetal.,
2018).Furthermore,DNNshavebeenusedwithelectroencephalography(EEG)tostudya
varietyofdifferentneuralandcognitivedisorders(deBardecietal.,2021).
FrontiersinNeuroscience 01 frontiersin.org

Brookshireetal. 10.3389/fnins.2024.1373515
Deeplearninghelpstorevealpreviously-unknownpatternsin segmentisthenusedasaseparateobservationduringtrainingor
neuroimaging data, but it also presents researchers with subtle testing.ThissegmentationprocedureismeanttoensurethatDNN
pitfalls.Onesetofchallengesconcernshowthedataaresplitinto modelshaveenoughtrainingdatatolearnrobustrepresentationsof
separate training and test sets. The training set is used to fit the thepatternsthatcharacterizeadisease,andtopreparethedatafor
model’sparameters,andthetestsetisusedtoestimatethemodel’s commonly-usedmodelarchitectures.However,EEGsegmentation
performanceonnewdata(athirdsubsetofthedataisoftenheld leadstodataleakageifthesamesubjectsappearinboththetraining
asideasavalidationset,usedtotunethemodel’shyperparameters andtestsets.SegmentsofEEGfromonesubjectaremoresimilarto
andtodeterminewhentostoptrainingthemodel).Insomecases, eachotherthantosegmentsfromdifferentsubjects(Demuruand
researchers train their model on one subset of the available data, Fraschini,2020).Insteadoflearninganabstractrepresentationthat
andthenevaluatethemodel’sperformanceonaseparatetestset. would generalize to new subjects, a DNN model could therefore
Inothercases,researchersusecross-validation(CV)totrainand achievehighclassificationaccuracybyassociatingalabelwitheach
test models on multiple subsets of the data. Under both of these subject’sidiosyncraticpatternofbrainactivity.Asaconsequence,
approaches, researchers must be careful to avoid “data leakage” randomlysplittingEEGsegmentsintotrainingandtestsetsresults
when splitting the data into training and test sets. Data leakage, indataleakage,andabiasedestimateoftestperformance:accuracy
whichariseswheninformationaboutthetestsetispresentinthe ishighontheresearchers’testset,buttheclassifierwillgeneralize
training set, results in a positively-biased estimate of the model’s poorly to new subjects. In a clinical setting, this leads to an
performance(Kaufmanetal.,2012).Forexample,inadata-mining apparently-promisingdiagnostictoolthatfailswhenappliedtonew
competition focused on identifying patients with breast cancer, patients. To avoid this kind of data leakage, all segments from a
oneteamofresearchersfoundthatthepatientIDnumbercarried givensubjectmustbeassignedtoonlyasinglepartitionofthedata
predictiveinformationaboutcancerrisk(Rossetetal.,2010).These (i.e.,trainorvalidationortest).
IDnumbersmayhaveappearedaftercompilingdatafromdifferent How does leakage of subject-specific information bias the
medicalinstitutions.BecausetheIDnumberwasassignedbasedon results of translational DNN-EEG studies? Here we address this
patients’ diagnosis, it constitutes a source of data leakage (Rosset question by examining the effects of data leakage in two case
etal.,2010).Ingeneral,dataleakageoccurswhenanexperimenter studies, and then reviewing the published literature to gauge the
handles the data in a way that artificially introduces correlations prevalence of this leakage. In the case studies, we reproduce
betweenthetrainingandtestsets. two convolutional neural network (CNN) architectures used by
DNN models typically require a large amount of training published studies—both of which used a train-test split that
data to perform well, but neural datasets are usually expensive introduced data leakage. In order to focus on the ways in which
and difficult to obtain. To increase the number of observations leakageresultsfromthetrain-testsplit,andtofacilitatecomparison
availabletotrainthemodel,thesestudiesoftensplitasingleneural withpriorliterature,wereusethesepublishedmodelarchitectures
recordingintomultiplesamples,anduseeachsampleasaseparate withoutanymodification.First,weuseaCNNtoclassifysubjects
observationduringtrainingortesting.Forexample,a3Dstructural as either healthy or as having dementia due to Alzheimer’s
MR volume could be split into multiple 2D slices, and an fMRI disease. Second, we use a CNN to classify whether segments of
time-series could be split into multiple segments of time (Wen time contain an epileptic seizure. In both datasets, we find that
et al., 2020). When multiple observations from a single subject real-world performance is dramatically overestimated when data
areincludedinboththetrainingandtestsets,itconstitutesdata from individual subjects is included in both the training and
leakage: Instead of learning a generalizable pattern, these models test sets. In the literature review, we find that the majority of
couldlearncharacteristicsoftheindividualsubjectsinthetraining translational DNN-EEG studies suffer from data leakage due to
set, and then simply recognize those familiar subjects in the test data from individual subjects appearing in both the training and
set. As a result, these models perform well in the study’s test set, testsets.
leadingtheresearcherstobelievetheyhavearobustclassifier.In
newsubjects,however,themodelmayfailtogeneralize.
Prior research has shown that leakage of subject-specific
information—sometimes referred to as “identity confounding” 2 Method
(Chaibub Neto et al., 2019)—occurs in a number of different
research areas. For example, this type of data-leakage occurs in 2.1 Deep neural network analysis overview
publishedMRIstudies(Wenetal.,2020).Furthermore,leakageof
subject-specificinformationiswidespreadintranslationalstudies To investigate how segment-based holdout leads to data
usingopticalcoherencetomography(OCT),andleadstostrongly leakage, we reproduced the model architectures from two
inflated estimates of test accuracy (Tampu et al., 2022). Identity published studies (Oh et al., 2020; Rashed-Al-Mahfuz et al.,
confounding has also been demonstrated in studies that make 2021). The goal of these analyses was not to develop an optimal
clinical predictions on the basis of smartphone data, wearable architecture, but rather to evaluate the impact of different
sensordata,andaudiovoicerecordings(Saebetal.,2017;Tougui cross-validation choices on the estimated model performance.
etal.,2021). We therefore re-used the published architectures and data
Studies using DNNs with EEG are particularly susceptible processing pipelines without modification, and without any
to data leakage. In these studies, each subject’s full EEG time- model selection or hyperparameter tuning. The code necessary
series(lastingseveralminutes)iscommonlydividedupintobrief to reproduce both of these DNN models is provided in
segments (lasting several seconds) (de Bardeci et al., 2021). Each theSupplementarymaterial.
FrontiersinNeuroscience 02 frontiersin.org

| Brookshireetal. |     |     |     |     |     |     |     |     |     |     | 10.3389/fnins.2024.1373515 |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- |
2.2 Experiment 1: Alzheimer’s disease previously-publishedmodelarchitecturewithoutmodification.We
diagnosis reproducedthemodelarchitecturefromOhetal.(2020);thismodel
isa1Dconvolutionalneuralnetworktrainedtoclassifysegmentsof
| 2.2.1 EEGdata |     |     |     |     |     |     | time-seriesEEGdataasSCIorAD. |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
We analyzed EEG data that was collected for a previously Thismodellearnstemporalfiltersthatareappliedequivalently
|           |                  |     |                |       |     |            | across each | EEG | channel. | Progressing |     | through | the network, |
| --------- | ---------------- | --- | -------------- | ----- | --- | ---------- | ----------- | --- | -------- | ----------- | --- | ------- | ------------ |
| published | study (Ganapathi |     | et al., 2022). | These | EEG | recordings |             |     |          |             |     |         |              |
were provided to us by the Pacific Neuroscience Institute. All subsequent layers build more complex features that take into
|            |               |     |        |            |        |           | account | a larger temporal |     | receptive | field, | and some | invariance is |
| ---------- | ------------- | --- | ------ | ---------- | ------ | --------- | ------- | ----------------- | --- | --------- | ------ | -------- | ------------- |
| procedures | were approved |     | by the | St. John’s | Cancer | Institute |         |                   |     |           |        |          |               |
InstitutionalReviewBoard(ProtocolJWCI-19-1101)inaccordance achievedthroughpoolingovertime.Themodelconsistedoffour
withtheHelsinkiDeclarationof1975.Patientswereevaluatedbya convolutional layers,each followedby rectification,maxpooling,
andbatchnormalization;convolutionallayerswerefollowedbytwo
dementiaspecialistaspartoftheirvisittoaspecialtymemoryclinic
(Pacific Brain Health Center in Santa Monica, CA) for memory densefully-connectedlayersof20and10hiddenunits,respectively,
eachrectified,andfinallyadenseconnectivitytotheoutputlayer
complaints.Thisevaluationsincludedbehavioraltestingaswellas
EEGrecordings.Aftertheseevaluations,subjectswereselectedby with 2 units representing AD yes/no probability logits. All deep
retrospectivelyreviewingchartsforpatientsaged55andolderseen learningmodelsweretrainedwithKerasandTensorflow.Theexact
|     |     |     |     |     |     |     | Keras code | used to | specify | the architecture |     | can be | found in the |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ------- | ---------------- | --- | ------ | ------------ |
betweenJuly2018andFebruary2021.
Patients received a consensus diagnosis from a panel of Supplementarymaterial.
| board-certified | dementia  | specialists. |       | Diagnoses | were | performed    |                   |     |     |     |     |     |     |
| --------------- | --------- | ------------ | ----- | --------- | ---- | ------------ | ----------------- | --- | --- | --- | --- | --- | --- |
| using standard  | clinical  | methods      | on    | the basis | of   | neurological |                   |     |     |     |     |     |     |
| examinations,   | cognitive | testing      | (MMSE | Folstein  | et   | al., 1975    | or 2.2.3 Training |     |     |     |     |     |     |
MoCANasreddineetal.,2005),clinicalhistory(e.g.,hypertension, Modelsweretrainedfor70epochswithoutanyearlystopping
| diabetes, | head injury, | depression), |     | and laboratory |     | results (e.g., |     |     |     |     |     |     |     |
| --------- | ------------ | ------------ | --- | -------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
orhyperparametertuning.Abatchsizeof32,initiallearningrate
vitamin B-12 levels, thyroid stimulating hormone levels, and of0.0001,andtheAdamoptimizerwereusedtooptimizemodels.
rapid plasma regain testing). These tests were used to rule out Training accuracy was computed and stored online during each
| reversible | causes of | memory | loss | and to | diagnose | subjective |     |     |     |     |     |     |     |
| ---------- | --------- | ------ | ---- | ------ | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
epoch,andaveragedacrossbatchestoreportthetrainingaccuracy
cognitiveimpairment(SCI),mildcognitiveimpairment(MCI),and for each epoch. To visualize how quickly the models reached
| dementia. | EEG data | was not | included | in the | diagnostic | process. |     |     |     |     |     |     |     |
| --------- | -------- | ------- | -------- | ------ | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- |
theirfinalperformance,testsetaccuracywasalsocomputedafter
Cognitive impairment was diagnosed on the basis of MMSE each epoch, averaged across batches. Since we reused the model
[or MoCA scores converted to MMSE (Bergeron et al., 2017)], architecture from prior published work, no model selection was
withMCIdiagnosedaccordingtoestablishedcriteria(Langaand
performed;performingongoingvalidationonthetestistherefore
Levine,2014).MCIwasdistinguishedfromdementiaonthebasis not a source of data leakage. For segment-based holdout, data
| of preserved | independence |     | in functional | abilities, |     | and a lack | of  |     |     |     |     |     |     |
| ------------ | ------------ | --- | ------------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
weresplitusing10-foldcross-validation(see“Cross-validation”for
| significantimpairmentinsocialoroccupationalfunctioning.SCI |     |     |     |     |     |     | details). |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
wasdiagnosedinpatientswithsubjectivecomplaintsbutwithout
| evidence | of MCI. | Diagnostic | categorization |     | was | based on | the |     |     |     |     |     |     |
| -------- | ------- | ---------- | -------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
clinicalsyndromes(LangaandLevine,2014),anddidnotconsider
|     |     |     |     |     |     |     | 2.3 Experiment |     | 2:  | seizure | detection |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | ------- | --------- | --- | --- |
diseaseetiologyorsubtypeswithineachstage.
| EEG | data were | recorded | at 250 | Hz using | the | eVox System |     |     |     |     |     |     |     |
| --- | --------- | -------- | ------ | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
2.3.1 EEGdata
| (Evoke Neuroscience), |     | with | a cap | that included |     | 19 electrodes |     |     |     |     |     |     |     |
| --------------------- | --- | ---- | ----- | ------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
followingtheInternational10-20system(FP1,FP2,F7,F3,Fz,F4, WeanalyzeddatafromtheSienaScalpEEGDatabase(Detti,
|     |     |     |     |     |     |     | 2020; Detti | et al., 2020) | hosted | on  | PhysioNet | (Goldberger | et al., |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------- | ------ | --- | --------- | ----------- | ------- |
F8,T7,C3,Cz,C4,T8,P7,P3,Pz,P4,P8,O1,andO2).Thefull
|     |     |     |     |     |     |     | 2000). These | recordings | were | collected |     | in accordance | with the |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | ---- | --------- | --- | ------------- | -------- |
EEGsessionincludeda5-minblockofeyes-openrest,a5-minute
|     |     |     |     |     |     |     | Declaration | of Helsinki, | and | approved | by  | the Ethical | Committee |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | -------- | --- | ----------- | --------- |
blockofeyes-closedrest,anda15-mingo/no-gotask.Inthisstudy,
oftheUniversityofSiena.Participantsprovidedwritteninformed
weanalyzedonlytheeyes-openresting-statedata.Recordingswere
low-pass filtered below 125 Hz, and split into non-overlapping consent before beginning data collection. This dataset includes
|     |     |     |     |     |     |     | recordings | from 14 | epilepsy | patients | (age | 20–71 | years, nine |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | -------- | -------- | ---- | ----- | ----------- |
segmentsof2s(500samples)formodeltraining.Channelswere
|     |     |     |     |     |     |     | male) digitized | at 512 | Hz  | with electrodes |     | arranged | following the |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ------ | --- | --------------- | --- | -------- | ------------- |
stackedtoproducematricesofshape(500,19)asmodelinputs.
|     |     |     |     |     |     |     | International | 10-20 | system. | Seizures | in the | data were | labeled by |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | ------- | -------- | ------ | --------- | ---------- |
Weselectedall49subjectsinthedatasetwhowerediagnosed
|     |     |     |     |     |     |     | an expert | clinician. | This dataset | contains |     | 47 seizures | in ∼128 h |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ------------ | -------- | --- | ----------- | --------- |
withdementiaduetoAlzheimer’sdisease(18male,31female;age
73.9±6.8years).Asacomparison,weselectedanequalnumber ofrecordedEEG.Toensurethatthedatawerebalancedbetween
seizureandnon-seizureepochs,weselectednon-seizuredatafrom
| ofsubjectswithsubjectivecognitiveimpairment(SCI;n |     |     |     |     |     | = 49,18 |     |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
thebeginningofeachsubject’srecordingstomatchthedurationof
male,31female;age63.9±11.4years).
theirseizure-labeleddata.Thisledto47min21sofdataineach
condition(1h34min42sintotal).
|     |     |     |     |     |     |     | In contrast | to  | the previous | section |     | where raw | time series |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------ | ------- | --- | --------- | ----------- |
2.2.2 Architecture were used, EEG data were prepared for the classifier analysis in
Because our goal was to evaluate the effects of different the frequency domain, following the approach used by Rashed-
cross-validation strategies on generalizability, we re-used a Al-Mahfouz and colleagues (Rashed-Al-Mahfuz et al., 2021).
| FrontiersinNeuroscience |     |     |     |     |     |     | 03  |     |     |     |     |     | frontiersin.org |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- |

| Brookshireetal. |     |     |     |     |     |     |     |     |     |     | 10.3389/fnins.2024.1373515 |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- |
Spectrogramswerecomputedwithawindowlengthof256samples constructamatrixXofEEGsegmentsofsize(n,m),andavector
(0.5 s) overlapping by 128 samples (0.25 s), using a Hann taper. y of diagnostic label of length n. The cross-validation is a simple
Spectrogramswerethendividedintosegmentsof1.5s.Asinthe partitionoftheindexvectorα = {1,2,...,n}intodisjointsubsets
α trainandα
originalstudy,weusedtheRGBrepresentationofthespectrogram test.WhereXigivestheithsegmentsofX,wethenhave
(viridis color-map), and exported as 224 × 224 × 3 images for Xtrain = {Xi }∀i ∈ α train, Xtest = {Xi }∀i ∈ α test, and y =
train
trainingandtestingwiththeCNNmodels. {y }∀i∈α train,y ={y }∀i∈α test.
|                    |     |     |     |     |     |     | i                          | test | i   |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | -------------------------- | ---- | --- | --- | --- | --- | --- | --- |
| 2.3.2 Architecture |     |     |     |     |     |     | 2.4.2 Subject-basedholdout |      |     |     |     |     |     |     |
The aim of this study was to evaluate the impact of different Subject-basedcross-validationtakesintoaccountwhichsubject
cross-validationchoices,nottoidentifyahighly-performingmodel each EEG segment comes from. This approach enforces that
architecture.Wethereforereusedthemodelarchitecturepresented eachsubjectappearsinonlyonepartitionofthecross-validation,
by Rashed-Al-Mahfuz et al. (2021) without modification. No ensuring there is no leakage of subject-level information across
model selection or hyperparameter tuning was performed. To trainingandtestsets.Tocreatethissplit,weconsideranadditional
handle 3D spectrogram data (vs. 2D time-series used in the subject vector s, which is used to constrain the partition of
previous section), a 2D convolutional neural network was used. X and y. Concretely, rather than partitioning the index vector
This model learns 2D spectrotemporal features that are applied α, we partition the unique subject vector s u, which gives the
equivalently across the spectrogram. The model contains four unique entries of s, and collect all corresponding segments
convolutional layers, each followed by rectification, pooling, and from each subject contained in train and validation partitions
|     |     |     |     |     |     |     | α   | α   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
batchnormalization,followedbytwohiddenfully-connectedlayers into train and test. This enforces the constraint that s i 6=
of 256 and 512 units each, dropout, and a final classification s ∀i ∈ α train,j ∈ α test. To perform k-fold cross-validation,
j
layer of 2 units corresponding to seizure yes/no. The exact we first divide s into k non-overlapping chunks, and each
u
Keras code used to specify the architecture can be found in the chunk to serve as the validation data in each fold of cross-
Supplementarymaterial. validation, where the remaining k − 1 chunks are reserved
fortraining.
2.3.3 Training
|            |                        |               |          |         |          |           | 2.5 Literature |     | review |     |     |     |     |     |
| ---------- | ---------------------- | ------------- | -------- | ------- | -------- | --------- | -------------- | --- | ------ | --- | --- | --- | --- | --- |
| Models     | were trained           | for 70 epochs | with     | no      | early    | stopping. |                |     |        |     |     |     |     |     |
| We used    | the RMSProp optimimzer |               | with     | a batch | size of  | 32 and    |                |     |        |     |     |     |     |     |
| a learning | rate of 0.00001.       | Training      | accuracy | was     | computed | and       |                |     |        |     |     |     |     |     |
Wesearchedtheliteratureforstudiesthatuseddeeplearning
stored online during each epoch, and averaged across batches with segments of EEG to classify a variety of diseases. We
| to report | the training accuracy |     | for each | epoch. | To  | visualize |          |                |     |        |               |     |             |     |
| --------- | --------------------- | --- | -------- | ------ | --- | --------- | -------- | -------------- | --- | ------ | ------------- | --- | ----------- | --- |
|           |                       |     |          |        |     |           | searched | Google Scholar | for | papers | investigating |     | Alzheimer’s |     |
how quickly the models reached their final performance, test set disease, Parkinson’s disease, attention-deficit/hyperactivity
accuracy was also computed after each epoch, averaged across disorder (ADHD), depression, schizophrenia, and seizures.
| batches. | Since we reused | the model | architecture |     | from | prior |         |          |                |     |          |        |     |          |
| -------- | --------------- | --------- | ------------ | --- | ---- | ----- | ------- | -------- | -------------- | --- | -------- | ------ | --- | -------- |
|          |                 |           |              |     |      |       | We then | searched | the references |     | of these | papers | to  | identify |
published work, no model selection was performed; performing additional publications for inclusion. Following this search, we
| ongoing | validation on the | test is | therefore | not | a source | of data |          |             |      |        |     |             |             |     |
| ------- | ----------------- | ------- | --------- | --- | -------- | ------- | -------- | ----------- | ---- | ------ | --- | ----------- | ----------- | --- |
|         |                   |         |           |     |          |         | included | every study | that | used a | DNN | to identify | psychiatric |     |
leakage. or neurological conditions using EEG. This non-exhaustive
|     |     |     |     |     |     |     | search included | 63        | papers,  | all of | which | were   | published      | since |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --------- | -------- | ------ | ----- | ------ | -------------- | ----- |
|     |     |     |     |     |     |     | 2018 and        | used deep | learning | to     | study | one of | the conditions |       |
2.4 Cross-validation
namedabove.
|     |     |     |     |     |     |     | Next, | we examined | how | the | training | and | test | sets were |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | --- | --- | -------- | --- | ---- | --------- |
This study is primarily concerned with the consequences of determined in these studies. If a paper specified that the EEG
different approaches to splitting the data between training and recordingsweresplitintosegments,butdidnotspecifythatthey
| test sets. | We assess two types | of  | train-test | split: | (1) holding | out |               |       |            |        |     |                |     |           |
| ---------- | ------------------- | --- | ---------- | ------ | ----------- | --- | ------------- | ----- | ---------- | ------ | --- | -------------- | --- | --------- |
|            |                     |     |            |        |             |     | used subjects | as an | organizing | factor | of  | the train-test |     | split, we |
individual segments of EEG data without regard for subject ID labeledthatstudyasusing“segment-based”holdout.Somepapers
| (“segment-based | holdout”), | and (2) | holding | out | entire | subjects, |              |             |          |      |            |     |          |      |
| --------------- | ---------- | ------- | ------- | --- | ------ | --------- | ------------ | ----------- | -------- | ---- | ---------- | --- | -------- | ---- |
|                 |            |         |         |     |        |           | specifically | stated that | segments | from | individual |     | subjects | were |
ensuring that all segments for a given subject appear in only the included in both the training and test sets (for example, studies
trainingorthetestset(“subject-basedholdout”;Figure1). thattrainedseparatemodelsforeachsubject);thesestudieswere
|     |     |     |     |     |     |     | also labeled     | as segment-based |          | holdout. | If   | a paper  | specified | that     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ---------------- | -------- | -------- | ---- | -------- | --------- | -------- |
|     |     |     |     |     |     |     | all the segments | from             | a single | subject  | were | assigned | to        | only the |
2.4.1 Segment-basedholdout
|               |                  |     |           |     |     |          | training or     | the test | set, we    | labeled | that study    | as  | using | “subject- |
| ------------- | ---------------- | --- | --------- | --- | --- | -------- | --------------- | -------- | ---------- | ------- | ------------- | --- | ----- | --------- |
| Segment-based | cross-validation |     | considers | all | EEG | segments |                 |          |            |         |               |     |       |           |
|               |                  |     |           |     |     |          | based” holdout. | If a     | study used | both    | segment-based |     | and   | subject-  |
to be equivalent, and divides them into training and validation basedholdoutindifferentanalyses,welabeledthestudyas“both".
| partitions | without considering | subject | ID. | This | segment-holdout |     |     |     |     |     |     |     |     |     |
| ---------- | ------------------- | ------- | --- | ---- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Welabeledstudiesas“unclear”ifwecouldnotdeterminewhether
approach will lead to data leakage if there is statistical non- the models were trained on segments of EEG recordings, and it
| independence | due to multiple | EEG | segments | coming | from | each |     |     |     |     |     |     |     |     |
| ------------ | --------------- | --- | -------- | ------ | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
wasnotexplicitlystatedthatsubjectswereusedasafactorinthe
| subject. | Given n segments | and m | time-points | per | segments, | we  |     |     |     |     |     |     |     |     |
| -------- | ---------------- | ----- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
holdoutprocedure.
| FrontiersinNeuroscience |     |     |     |     |     |     | 04  |     |     |     |     |     | frontiersin.org |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |

Brookshireetal. 10.3389/fnins.2024.1373515
FIGURE1
Illustrationofsegment-basedandsubject-basedholdout.Thisexampleshowscross-validationwiththreeparticipants,eachofwhomhavethree
segmentsofdata,and3-foldcross-validation(CV).EachrowshowsaseparateCVfold.EachsquareillustratesasingleEEGsegment,withblue
squaresindicatingobservationsinthetrainingsetandredsquaresindicatingobservationsinthetestset.Grayrectanglesaredrawnaround
observationsfromthesamesubject.
3 Results
| 3.1 Data | leakage leads | to biased | test-set |     |     |
| -------- | ------------- | --------- | -------- | --- | --- |
accuracy
Weanalyzetwodatasetstotesthowtheestimatedaccuracyofa
DNNclassifierdependsonthetrain-testsplit.First,weexaminethe
effectsofdataleakageinapatient-levelclassifierbytrainingamodel
todiagnoseAlzheimer’sdisease.Second,weexaminetheeffectsof
| data leakage | in a segment-level | classifier by | training | a model to |     |
| ------------ | ------------------ | ------------- | -------- | ---------- | --- |
identifyperiodsoftimethatincludeanepilepticseizure.Ineachof
theseanalyses,wereuseapublishedDNNarchitecturetoanalyze
anexistingdataset.
FIGURE2
Test-setaccuracyofCNNmodelspredictingheld-outdata,plotted
3.1.1 IdentifyingpatientswithAlzheimer’sdisease separatelyforsegment-basedholdoutandsubject-basedholdout.
(A)AccuracyformodelstrainedtoclassifyAlzheimer’sdiseasein
To determine whether segment-based holdout leads to individualsubjects.Boxesshowtheinter-quartilerange,darklines
showthemedian,andwhiskersextendtotheminimumand
| a biased | estimate of accuracy, | we first | trained | a CNN to |     |
| -------- | --------------------- | -------- | ------- | -------- | --- |
maximumpoints.(B)Accuracyformodelstrainedtoidentify
| diagnose | Alzheimer’s disease | using segments | of EEG. | When the |     |
| -------- | ------------------- | -------------- | ------- | -------- | --- |
seizuresinsegmentsofEEGdata.Detailsasin(A).
| EEG segments | were split             | into training | and test sets  | without |     |
| ------------ | ---------------------- | ------------- | -------------- | ------- | --- |
| considering  | subject ID, the        | model showed  | nearly perfect | test-   |     |
| set accuracy | of 99.8% (99.1–100.0%) | (Figure2A).   | Performance    |         |     |
3.1.2 Identifyingsegmentscontainingepileptic
| quickly                                                     | approached ceiling | within the first | 15 training | epochs   |     |
| ----------------------------------------------------------- | ------------------ | ---------------- | ----------- | -------- | --- |
| (Figure3A).Thishighaccuracyisconsistentwithpriorstudiesthat |                    |                  |             | seizures |     |
usesegment-basedholdoutandreporthighaccuracyforCNNsat Insomecases,artificialneuralnetworkmodelshavebeenused
identifyingneurologicaldisorders(Acharyaetal.,2018b;Leeetal., toidentifytime-limitedeventswithinongoingbrainactivity,such
2019;Ohetal.,2020).Couldthispatternofhighaccuracyreflect asepilepticseizures.Doessegment-basedholdoutalsoleadtodata
dataleakage,insteadofarobustandgeneralizableclassifier? leakagewhenlabelingperiodsoftimewithinsubjects?Toanswer
Whenweusedsubject-basedholdout,ensuringthatindividual thisquestion,wetrainedaCNNtoclassifysegmentsofEEGdataas
subjects’ data did not appear in both the training and test containinganepilepticseizureornot.
sets, test accuracy dropped to 53.0% (43.1–64.8%), with 95% WhentheEEGsegmentsweresplitintotrainingandtestsets
confidence intervals that included chance performance of 50%. withoutconsideringsubjectID,themodelreachedahightest-set
Performance remained low throughout the training epochs accuracyof79.1%(78.8–79.4%)(Figure2B).Accuracyleveledout
(Figure3B).Comparedwithsubject-basedholdout,segment-based within 10 training epochs (Figure3C). When individual subjects’
holdout significantly overestimates the model performance on data segments were restricted to appear in only the training or
previously-unseensubjects(WilcoxonT=0.0,p=0.002). test set, however, accuracy fell to 65.1% (61.3–69.1%). Accuracy
| FrontiersinNeuroscience |     |     |     | 05  | frontiersin.org |
| ----------------------- | --- | --- | --- | --- | --------------- |

| Brookshireetal. |     |     |     |     |     | 10.3389/fnins.2024.1373515 |     |     |
| --------------- | --- | --- | --- | --- | --- | -------------------------- | --- | --- |
FIGURE3
Test-setaccuracyofCNNmodelsplottedasafunctionofthetrainingepoch.Graylinesshowaccuracyinindividualcross-validationfolds,andred
linesshowtheaverageacrossfolds.(A)AccuracyformodelstrainedtoclassifyAlzheimer’sdiseaseusingsegment-basedholdout.(B)Accuracyfor
modelstrainedtoclassifyAlzheimer’sdiseaseusingsubject-basedholdout.(C)Accuracyformodelstrainedtoidentifyseizuresusing
segment-basedholdout.(D)Accuracyformodelstrainedtoidentifyseizuresusingsubject-basedholdout.
|     | 3.2 Data     | leakage |               | in published |         | EEG    | studies |          |
| --- | ------------ | ------- | ------------- | ------------ | ------- | ------ | ------- | -------- |
|     | Do published |         | translational | EEG          | studies | suffer | from    | subject- |
specificdataleakage,ordotheyavoiditbycomputingtheirtest-set
|     | accuracy | on held-out | subjects? |     | We examined | the | train-test | split |
| --- | -------- | ----------- | --------- | --- | ----------- | --- | ---------- | ----- |
strategiesinpublishedstudiesthatattemptedtoidentifyaclinical
disorderusingDNNswithEEGrecordings.Outofthe63relevant
|     | papers we | found, | only 17 | (27.0%) | unambiguously |     | avoided | this |
| --- | --------- | ------ | ------- | ------- | ------------- | --- | ------- | ---- |
typeofdataleakage(Figure4;Table1).Leakageofsubject-specific
informationispervasiveinthetranslationalEEGliterature.
4 Discussion
FIGURE4
Numberofstudiesusingeachtypeoftest-split.“Segments”: In EEG studies using deep learning, data leakage can occur
SegmentsofEEGdatawereassignedtothetrainingandtestsets
whensegmentsofdatafromthesamesubjectsareincludedinboth
withoutregardtosubject;thisapproachleadstodataleakage.
|     | the training | and | test sets. | Here | we demonstrate |     | that leakage | of  |
| --- | ------------ | --- | ---------- | ---- | -------------- | --- | ------------ | --- |
“Subjects”:Eachsubject’sdataappearedinonlythetrainingsetor
thetestset.“Both”:BoththeSubjectsandSegmentsapproaches subject-specificinformationcandramaticallyoverestimatethereal-
wereusedindifferentanalyses.“Unclear”:Wecouldnotdetermine
|     | world clinical | performance |     | of a | DNN classifier. |     | Our Alzheimer’s |     |
| --- | -------------- | ----------- | --- | ---- | --------------- | --- | --------------- | --- |
whichapproachwasusedfortrain-testsplits.
|     | CNN classifier | appeared      |     | to have  | an  | accuracy | of above    | 99% |
| --- | -------------- | ------------- | --- | -------- | --- | -------- | ----------- | --- |
|     | when using     | segment-based |     | holdout, | but | its true | performance | on  |
previously-unseensubjectswasindistinguishablefromchance.We
foundthisbiasintest-setperformancebothinabetween-subjects
|     | task (identifying |     | patients | with Alzheimer’s |     | disease | in Experiment |     |
| --- | ----------------- | --- | -------- | ---------------- | --- | ------- | ------------- | --- |
1)andinawithin-subjectstask(identifyingsegmentsthatcontain
remainedlowthroughouttrainingepochs(Figure3D).Evenwhen a seizure in Experiment 2). Next, we show that this type of data
themodelistaskedwithlabelingperiodsofactivitywithinsubjects, leakage appears in the majority of published translational DNN-
segment-basedholdoutsignificantlyoverestimatesperformanceon EEG studies we examined. Together, these results illustrate how
previously-unseensubjects(WilcoxonT=0.0,p=0.0001). an improperly-designed training-test split can bias the results of
| FrontiersinNeuroscience | 06  |     |     |     |     |     | frontiersin.org |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --------------- | --- |

| Brookshireetal.                                           |        |           |     |                    |     |     |        | 10.3389/fnins.2024.1373515 |     |           |     |
| --------------------------------------------------------- | ------ | --------- | --- | ------------------ | --- | --- | ------ | -------------------------- | --- | --------- | --- |
| TABLE1 PriortranslationalstudiesusingdeeplearningwithEEG. |        |           |     | TABLE1 (Continued) |     |     |        |                            |     |           |     |
| Article                                                   | Target | Testsplit |     | Article            |     |     | Target |                            |     | Testsplit |     |
Ahmadietal.(2021) ADHD Segments Acharyaetal.(2018a) Seizure Segments
BakhtyariandMirzaei(2022) ADHD Segments Avcuetal.(2019) Seizure Subjects
Changetal.(2022) ADHD Subjects Choietal.(2019) Seizure Subjects
Chenetal.(2019a) ADHD Segments DaoudandBayoumi(2019) Seizure Segments
Chenetal.(2019b) ADHD Segments Emamietal.(2019) Seizure Subjects
Dubreuil-Valletal.(2020) ADHD Subjects Fürbassetal.(2020) Seizure Subjects
MafiandRadfar(2022) ADHD Segments Gaoetal.(2020) Seizure Segments
Moghaddarietal.(2020) ADHD Segments Husseinetal.(2019) Seizure Segments
TaghiBeyglouetal.(2022) ADHD Subjects IešmantasandAlzbutas(2020) Seizure Subjects
| Tosun(2021) | ADHD | Segments |     | Janaetal.(2020) |     |     | Seizure |     |     | Segments |     |
| ----------- | ---- | -------- | --- | --------------- | --- | --- | ------- | --- | --- | -------- | --- |
Vahidetal.(2019) ADHD Subjects Khanetal.(2017) Seizure Segments
Zhouetal.(2022) ADHD Unclear LiY.etal.(2020) Seizure Segments
Kimetal.(2018) Alcoholism Segments Liangetal.(2020) Seizure Segments
BiandWang(2019) Alzheimer’s Segments Raghuetal.(2020) Seizure Unclear
Gkeniosetal.(2022) Alzheimer’s Both Rashed-Al-Mahfuzetal.(2021) Seizure Segments
Hugginsetal.(2021) Alzheimer’s Segments Truongetal.(2018) Seizure Segments
Ieracitanoetal.(2019) Alzheimer’s Both Ullahetal.(2018) Seizure Segments
| KimandKim(2018) | Alzheimer’s | Subjects |     |                |     |     |         |     |     |          |     |
| --------------- | ----------- | -------- | --- | -------------- | --- | --- | ------- | --- | --- | -------- | --- |
|                 |             |          |     | Weietal.(2018) |     |     | Seizure |     |     | Segments |     |
Morabitoetal.(2016) Alzheimer’s Subjects Weietal.(2019) Seizure Segments
Youetal.(2020) Alzheimer’s Segments Zhaoetal.(2020) Seizure Segments
ZhaoandHe(2015) Alzheimer’s Segments Zhouetal.(2018) Seizure Segments
Acharyaetal.(2018b) Depression Segments Bouallegueetal.(2020) Seizureandautism Segments
Ayetal.(2019) Depression Segments EachlineinthetabledescribesonepublishedtranslationalstudyusingaDNNwithEEGdata.
The“Target”columnholdstheclinicalconditionbeingclassified.The“Testsplit”column
Kwonetal.(2019) Depression Subjects showstheapproachusedtodeterminehowthedataweredividedintotrainingandtestsets.
“Segments”:SegmentsofEEGdatawereassignedtothetrainingandtestsetswithoutregard
| Lietal.(2019) | Depression | Subjects |     |     |     |     |     |     |     |     |     |
| ------------- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tosubject;thisapproachleadstodataleakage.“Subjects”:Eachsubject’sdataappearedinonly
LiX.etal.(2020) Depression Subjects thetrainingsetorthetestset.“Both”:BoththeSubjectsandSegmentsapproacheswereusedin
differentanalyses.“Unclear”:Wecouldnotdeterminewhichapproachwasusedfortrain-test
splits.
| MumtazandQayyum(2019) | Depression | Segments |     |     |     |     |     |     |     |     |     |
| --------------------- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Uyulanetal.(2021)     | Depression | Unclear  |     |     |     |     |     |     |     |     |     |
| Xieetal.(2020)        | Depression | Unclear  |     |     |     |     |     |     |     |     |     |
DNNstudies,andshowthatbiasedresultsarewidespreadinthe
| Zhangetal.(2020) | Depression | Segments |     |     |     |     |     |     |     |     |     |
| ---------------- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
publishedliterature.
Khareetal.(2021) Parkinson’s Segments To be useful in a clinical setting, a diagnostic classifier must
Leeetal.(2019) Parkinson’s Segments be able to identify a disease in new patients. Models trained
usingsegment-basedholdout,however,stronglyoverestimatetheir
| Lohetal.(2021) | Parkinson’s | Segments |     |            |         |      |                |       |        |     |       |
| -------------- | ----------- | -------- | --- | ---------- | ------- | ---- | -------------- | ----- | ------ | --- | ----- |
|                |             |          |     | ability to | perform | this | task. Instead, | these | models | may | learn |
Ohetal.(2020) Parkinson’s Segments patterns associated with individual subjects, and then associate
|                      |             |          |     | those idiosyncratic |               | patterns     | with        | a diagnosis.  | As       | a consequence, |     |
| -------------------- | ----------- | -------- | --- | ------------------- | ------------- | ------------ | ----------- | ------------- | -------- | -------------- | --- |
| Shaban(2021)         | Parkinson’s | Segments |     |                     |               |              |             |               |          |                |     |
|                      |             |          |     | performance         | of            | these models | drops       | precipitously |          | when they      | are |
| ShabanandAmara(2022) | Parkinson’s | Subjects |     |                     |               |              |             |               |          |                |     |
|                      |             |          |     | tested in           | new subjects, | and          | performance | is            | unlikely | to generalize  |     |
Shietal.(2019) Parkinson’s Subjects toanewdataset.WhentrainingatranslationalDNNclassifier,the
Ahmedt-Aristizabaletal.(2020) Schizophrenia Subjects modelmustbetestedwithsubjectswhowerenotincludedinthe
trainingset.
| Chuetal.(2017) | Schizophrenia | Segments |     |             |                  |      |               |                          |      |          |     |
| -------------- | ------------- | -------- | --- | ----------- | ---------------- | ---- | ------------- | ------------------------ | ---- | -------- | --- |
|                |               |          |     | Our results | show             | that | segment-based | cross-validationinflates |      |          |     |
| Ohetal.(2019)  | Schizophrenia | Both     |     |             |                  |      |               |                          |      |          |     |
|                |               |          |     | estimates   | of out-of-sample |      | model         | performance              | when | training | on  |
Shalbafetal.(2020) Schizophrenia Segments segmentsfromresting-stateEEG.However,thesameprinciplesof
|                         |     | (Continued) |     | data leakage | will | apply to | task-based | EEG; | providing | a classifier    |     |
| ----------------------- | --- | ----------- | --- | ------------ | ---- | -------- | ---------- | ---- | --------- | --------------- | --- |
| FrontiersinNeuroscience |     |             | 07  |              |      |          |            |      |           | frontiersin.org |     |

| Brookshireetal. |     |     |     |     |     |     |     |     |     |     |     | 10.3389/fnins.2024.1373515 |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- |
with person-specific information enables it to artificially inflate intomultiplesegments.Inthispaper,weshowedhowdataleakage
performance. can arise when a long recording is split into multiple shorter
Although this study focused on Alzheimer’s Disease and segments.However,thesameprinciplesapplytoanyothermethod
epileptic seizures, our findings are not particular those diseases. thatintroducesstatisticalnon-independencebetweenthetraining
Classification studies will overestimate model generalization and test sets. For example, some EEG-based DNNs treat every
wheneverdatafromindividualparticipantsispresentinboththe channelindependently,anduseinformationfromeachchannelas
training and test sets. Prior review articles have summarized the a separate observation (Loh et al., 2021). Those studies are likely
details and idiosyncrasies of DNN models in the context of AD tosufferfromsubstantialdataleakage,sincephysiologicalsources
(Cassanietal.,2018;Wenetal.,2020)andseizures(Rasheedetal., ofelectricalactivityappearredundantlyacrossmultipleEEGscalp
| 2020;Shoeibietal.,2021). |     |     |     |     |     |     |     | electrodes(MichelandHe,2019). |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- |
Theseprinciplesalsoapplytoothermedicalimagingmethods
|     |     |     |     |     |     |     |     | and classifiers. | Similar | patterns | of  | “identity | confounding” |     | data |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ------- | -------- | --- | --------- | ------------ | --- | ---- |
4.1 Data leakage in between- and leakage have been documented in studies using functional (Wen
within-subjects designs et al., 2018) and anatomical (Wen et al., 2020) MRI, optical
coherencetomography(OCT)(Tampuetal.,2022),accelerometer
|             |           |                       |     |                  |              |               |     | and gyroscope | recordings  |          | from smartphones |       | (Saeb      | et al., | 2017),  |
| ----------- | --------- | --------------------- | --- | ---------------- | ------------ | ------------- | --- | ------------- | ----------- | -------- | ---------------- | ----- | ---------- | ------- | ------- |
| We          | find that | segment-based         |     | cross-validation |              | overestimates |     |               |             |          |                  |       |            |         |         |
|             |           |                       |     |                  |              |               |     | audio voice   | recordings  | (Chaibub | Neto             | et    | al., 2019; | Tougui  | et al., |
| performance | for       | both between-subjects |     |                  | (Alzheimer’s | disease,      |     |               |             |          |                  |       |            |         |         |
|             |           |                       |     |                  |              |               |     | 2021), and    | performance | on       | motor            | tasks | (Chaibub   | Neto    | et al., |
| Experiment  | 1)        | and within-subjects   |     | comparisons      |              | (seizures,    |     |               |             |          |                  |       |            |         |         |
Experiment 2). However, the magnitude of this overestimate was 2019). Furthermore, data leakage due to identity confounding is
notlimitedtodeepneuralnetworks,andhasbeenuncoveredusing
| smaller in | a within-subjects |     | comparison | (Figure2). |     | What | leads |     |     |     |     |     |     |     |     |
| ---------- | ----------------- | --- | ---------- | ---------- | --- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
randomforests(Saebetal.,2017;ChaibubNetoetal.,2019;Tougui
| to this difference |     | in the size | of the | effect between |     | the two | tasks? |     |     |     |     |     |     |     |     |
| ------------------ | --- | ----------- | ------ | -------------- | --- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
etal.,2021)andsupportvectormachines(Touguietal.,2021).
| In a between-subjects |                 | task, | the classifier | can  | simply          | associate | a     |     |     |     |     |     |     |     |     |
| --------------------- | --------------- | ----- | -------------- | ---- | --------------- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| label with            | each individual |       | participant.   | In a | within-subjects |           | task, |     |     |     |     |     |     |     |     |
however,thisshortcutisnotavailabletothemodel.Instead,itmust
|                        |     |     |                   |     |                  |     |      | 4.4 Caveats |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | ----------------- | --- | ---------------- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| learn a representation |     | of  | the labels—albeit |     | a representation |     | that |             |     |     |     |     |     |     |     |
maybecontaminatedbymultiplesegmentscomingfromthesame
|     |     |     |     |     |     |     |     | We find | that | segment-based |     | cross-validation |     | leads | to data |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---- | ------------- | --- | ---------------- | --- | ----- | ------- |
event,oronethatmaybespecifictoagivenparticipant.
leakage,andthistypeofcross-validationiscommonintranslational
|          |         |     |      |             |     |        |     | EEG studies. | This      | conclusion |       | mirrors | results | from       | studies |
| -------- | ------- | --- | ---- | ----------- | --- | ------ | --- | ------------ | --------- | ---------- | ----- | ------- | ------- | ---------- | ------- |
|          |         |     |      |             |     |        |     | examining    | a variety | of other   | types | of data | and     | classifier | models  |
| 4.2 Data | leakage |     | when | identifying |     | events |     |              |           |            |       |         |         |            |         |
within subjects (Saebetal.,2017;Wenetal.,2018,2020;ChaibubNetoetal.,2019;
Touguietal.,2021;Tampuetal.,2022).Thepreciseamountofdata
leakageandthebiasthatitintroduces,however,arelikelytodiffer
| Instead | of identifying |     | a disease | in each | subject, | some | studies |     |     |     |     |     |     |     |     |
| ------- | -------------- | --- | --------- | ------- | -------- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
basedonthedetailsoftheexperiment.Forexample,ifastudytrains
attempttoidentifyadiseasedprocessineachsegmentoftime(see
aclassifiertoidentifyindividualsubjectswithadisease,thenthere
Table1).DNNmodelsofepilepsy,forexample,oftenaimtoclassify
|              |         |      |         |            |                 |     |     | may be stronger | bias | when | the study | involves | fewer | participants |     |
| ------------ | ------- | ---- | ------- | ---------- | --------------- | --- | --- | --------------- | ---- | ---- | --------- | -------- | ----- | ------------ | --- |
| the segments | of data | that | contain | a seizure. | We demonstrated |     | in  |                 |      |      |           |          |       |              |     |
(Saebetal.,2017).Themodelarchitecturemayalsoinfluencethe
| Experiment       | 2 that  | those studies | are      | not immune | to       | data        | leakage |                  |                 |     |       |          |          |             |        |
| ---------------- | ------- | ------------- | -------- | ---------- | -------- | ----------- | ------- | ---------------- | --------------- | --- | ----- | -------- | -------- | ----------- | ------ |
|                  |         |               |          |            |          |             |         | amount of        | data leakage:   | a   | model | that can | more     | effectively | learn  |
| in training-test | splits: | the           | accuracy | in novel   | subjects | is strongly |         |                  |                 |     |       |          |          |             |        |
|                  |         |               |          |            |          |             |         | subject-specific | representations |     | could | show     | stronger | bias        | than a |
overestimatedwhenthetestsetincludessubjectswhowerealsoin
modelthatcannotlearnsubject-specificpatterns.
thetrainingset.Thisresultcouldariseifthemodelusesdifferent
patternstoidentifyseizuresineachsubject.
| Subject-specificstudiesindicatethatabespokeclassifiercould |     |     |     |     |     |     |     | 5 Conclusion |     |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
betrainedtoidentifyseizuresineachnewpatient(Janaetal.,2020;
Liangetal.,2020;LiY.etal.,2020).However,thiswouldrequire
|     |     |     |     |     |     |     |     | Data leakage | occurs | when | EEG | segments | from | one | subject |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | ---- | --- | -------- | ---- | --- | ------- |
everypatienttohavealargedatasetofrecordingsthathavealready appear in the both the training and test sets. As a result, the test
| been labeled, | which | limits | the clinical | utility | of this | approach. | A   |     |     |     |     |     |     |     |     |
| ------------- | ----- | ------ | ------------ | ------- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
setaccuracydramaticallyoverestimatestheclassifier’sperformance
morerealisticapproachistotrainDNNmodelstoidentifyevents
innewsubjects.Thistypeofdataleakageiscommoninpublished
inunseenpatients. studiesusingDNNsandtranslationalEEG.Toaccuratelyestimate
amodel’sperformance,researchersmustensurethateachsubject’s
dataisincludedinonlythetrainingorthetestset,butnotboth.
| 4.3 Data | leakage |     | in other | methods |     |     |     |                   |     |     |           |     |     |     |     |
| -------- | ------- | --- | -------- | ------- | --- | --- | --- | ----------------- | --- | --- | --------- | --- | --- | --- | --- |
|          |         |     |          |         |     |     |     | Data availability |     |     | statement |     |     |     |     |
Instudieswhichhaveonlyoneobservationpersubject,cross-
| validation | is trivial | – single | observations | are | simply | assigned | to  |     |     |     |     |     |     |     |     |
| ---------- | ---------- | -------- | ------------ | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thetrainingortestset.However,inEEGandmanyothermedical Publicly available datasets were analyzed in this study. This
imagining methods, the data from each subject is routinely split datacanbefoundhere:EEGdataforexperiment1wereprovided
| FrontiersinNeuroscience |     |     |     |     |     |     | 08  |     |     |     |     |     |     | frontiersin.org |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |

| Brookshireetal. |     |     |     |     |     |     |     |     |     |     |     | 10.3389/fnins.2024.1373515 |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- |
bythePacificNeuroscienceInstitute.Thesedataaredescribedby
|           |         |         |            |             |                |           |        | the writing  | of this | article, | or the | decision | to  | submit | it for |
| --------- | ------- | ------- | ---------- | ----------- | -------------- | --------- | ------ | ------------ | ------- | -------- | ------ | -------- | --- | ------ | ------ |
| Ganapathi | et al.  | (2022), | and can    | be accessed | through        | agreement |        | publication. |         |          |        |          |     |        |        |
| with the  | authors | of that | study. EEG | data        | for experiment |           | 2 were |              |         |          |        |          |     |        |        |
downloadedfromthepublicly-availableSienaScalpEEGDatabase
Acknowledgments
| hosted on | PhysioNet | (https://physionet.org/content/siena-scalp- |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | --------- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
eeg/1.0.0/).
|        |           |     |     |     |     |     |     | The contents | of         | this manuscript |         | have                      | previously | appeared |     |
| ------ | --------- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | --------------- | ------- | ------------------------- | ---------- | -------- | --- |
|        |           |     |     |     |     |     |     | online as    | a preprint | on              | medRxiv | (https://www.medrxiv.org/ |            |          |     |
| Ethics | statement |     |     |     |     |     |     |              |            |                 |         |                           |            |          |     |
content/10.1101/2024.01.16.24301366v1).
| Ethical | approval      | was  | not required |                   | for the | study             | involving |          |             |     |     |     |     |     |     |
| ------- | ------------- | ---- | ------------ | ----------------- | ------- | ----------------- | --------- | -------- | ----------- | --- | --- | --- | --- | --- | --- |
|         |               |      |              |                   |         |                   |           | Conflict | of interest |     |     |     |     |     |     |
| humans  | in accordance | with | the          | local legislation |         | and institutional |           |          |             |     |     |     |     |     |     |
requirements.Writteninformedconsenttoparticipateinthisstudy
was not required from the participants or the participants’ legal GB,JK,NB,YW,SG,KY,CQ,andCLwereemployedatSPARK
guardians/next of kin in accordance with the national legislation NeuroInc.,amedicaltechnologycompanydevelopingdiagnostic
andtheinstitutionalrequirements. aids to help clinicians identify and assess neurodegenerative
disease.
Theremainingauthorsdeclarethattheresearchwasconducted
| Author | contributions |     |     |     |     |     |     |                |        |            |     |           |               |     |      |
| ------ | ------------- | --- | --- | --- | --- | --- | --- | -------------- | ------ | ---------- | --- | --------- | ------------- | --- | ---- |
|        |               |     |     |     |     |     |     | in the absence | of any | commercial | or  | financial | relationships |     | that |
couldbeconstruedasapotentialconflictofinterest.
GB:Conceptualization,Formalanalysis,Visualization,Writing
| – original | draft. | JK: Data | curation, | Formal | analysis, |     | Software, |     |     |     |     |     |     |     |     |
| ---------- | ------ | -------- | --------- | ------ | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Visualization,Writing–review&editing.NB:Software,Writing–
|     |     |     |     |     |     |     |     | Publisher’s | note |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | --- | --- | --- | --- | --- | --- |
originaldraft,Writing–review&editing.YW:Conceptualization,
| Software, | Writing  | – review       | & editing. | RG:          | Resources, |         | Writing  | –           |                    |     |              |       |        |                  |        |
| --------- | -------- | -------------- | ---------- | ------------ | ---------- | ------- | -------- | ----------- | ------------------ | --- | ------------ | ----- | ------ | ---------------- | ------ |
|           |          |                |            |              |            |         |          | All claims  | expressed          | in  | this article | are   | solely | those            | of the |
| review &  | editing. | DM: Resources, |            | Supervision, |            | Writing | – review |             |                    |     |              |       |        |                  |        |
|           |          |                |            |              |            |         |          | authors and | do not necessarily |     | represent    | those | of     | their affiliated |        |
&editing.SG:Fundingacquisition,Supervision,Writing–review
|     |     |     |     |     |     |     |     | organizations, | or those | of  | the publisher, |     | the editors | and | the |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | --- | -------------- | --- | ----------- | --- | --- |
&editing.KY:Writing–review&editing.CQ:Conceptualization,
|     |     |     |     |     |     |     |     | reviewers. | Any product | that | may be | evaluated | in  | this article, | or  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | ---- | ------ | --------- | --- | ------------- | --- |
Datacuration,Writing–review&editing.CL:Conceptualization,
claimthatmaybemadebyitsmanufacturer,isnotguaranteedor
Fundingacquisition,Writing–review&editing.
endorsedbythepublisher.
Funding
|     |           |         |           |         |     |          |         | Supplementary |     | material |     |     |     |     |     |
| --- | --------- | ------- | --------- | ------- | --- | -------- | ------- | ------------- | --- | -------- | --- | --- | --- | --- | --- |
| The | author(s) | declare | financial | support | was | received | for the |               |     |          |     |     |     |     |     |
research,authorship,and/orpublicationofthisarticle.Thiswork The Supplementary Material for this article can be found
wassupportedbySPARKNeuro,Inc.Thefunderwasnotinvolved online at: https://www.frontiersin.org/articles/10.3389/fnins.2024.
in the study design, collection, analysis, interpretation of data, 1373515/full#supplementary-material
References
Acharya, U. R., Oh, S. L., Hagiwara, Y., Tan, J. H., and Adeli, H. Ay, B., Yildirim, O., Talo, M., Baloglu, U. B., Aydin, G., Puthankattil, S. D.,
(2018a). Deep convolutional neural network for the automated detection and etal.(2019).Automateddepressiondetectionusingdeeprepresentationandsequence
diagnosis of seizure using EEG signals. Comput. Biol. Med. 100, 270–278. learningwithEEGsignals.J.Med.Syst.43,1–12.doi:10.1007/s10916-019-1345-y
doi:10.1016/j.compbiomed.2017.09.017
Bakhtyari,M.,andMirzaei,S.(2022).ADHDdetectionusingdynamicconnectivity
Acharya, U. R., Oh, S. L., Hagiwara, Y., Tan, J. H., Adeli, H., and Subha, patternsofEEGdataandconvlstmwithattentionframework.Biomed.SignalProcess.
D. P. (2018b). Automated EEG-based screening of depression using deep Control76:103708.doi:10.1016/j.bspc.2022.103708
| convolutional | neural | network. | Comput. Methods | Programs | Biomed. | 161, | 103–113. |     |     |     |     |     |     |     |     |
| ------------- | ------ | -------- | --------------- | -------- | ------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Bergeron,D.,Flynn,K.,Verret,L.,Poulin,S.,Bouchard,R.W.,Bocti,C.,etal.
doi:10.1016/j.cmpb.2018.04.012 (2017).MulticentervalidationofanMMSE-MoCAconversiontable.J.Am.Geriatr.
Ahmadi, A., Kashefi, M., Shahrokhi, H., and Nazari, M. A. (2021). Computer Soc.65,1067–1072.doi:10.1111/jgs.14779
aideddiagnosissystemusingdeepconvolutionalneuralnetworksforADHDsubtypes. Bi, X., and Wang, H. (2019). Early Alzheimer’s disease diagnosis based
Biomed.SignalProcess.Control63:102227.doi:10.1016/j.bspc.2020.102227
|     |     |     |     |     |     |     |     | on EEG spectral | images | using | deep learning. | Neural | Netw. | 114, | 119–135. |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------ | ----- | -------------- | ------ | ----- | ---- | -------- |
doi:10.1016/j.neunet.2019.02.005
| Ahmedt-Aristizabal, |     | D., Fernando, | T., | Denman, | S., Robinson, | J. E., | Sridharan, |     |     |     |     |     |     |     |     |
| ------------------- | --- | ------------- | --- | ------- | ------------- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
S.,Johnston,P.J.,etal.(2020).Identificationofchildrenatriskofschizophrenia Bouallegue,G.,Djemal,R.,Alshebeili,S.A.,andAldhalaan,H.(2020).Adynamic
via deep learning and EEG responses. IEEE J. Biomed. Health Inf. 25, 69–76. filteringDF-RNNdeep-learning-basedapproachforEEG-basedneurologicaldisorders
doi:10.1109/JBHI.2020.2984238 diagnosis.IEEEAccess8,206992–207007.doi:10.1109/ACCESS.2020.3037995
Avcu, M. T., Zhang, Z., and Chan, D. W. S. (2019). “Seizure detection using Cassani, R., Estarellas, M., San-Martin, R., Fraga, F. J., and Falk, T. H.
least EEG channels by deep convolutional neural network,” in ICASSP 2019-2019 (2018). Systematic review on resting-state EEG for Alzheimer’s disease diagnosis
IEEEInternationalConferenceonAcoustics,SpeechandSignalProcessing(ICASSP) and progression assessment. Dis. Mark. 2018:5174815. doi: 10.1155/2018/51
| (Brighton:IEEE),1120–1124. |     |     |     |     |     |     |     | 74815 |     |     |     |     |     |                 |     |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --------------- | --- |
| FrontiersinNeuroscience    |     |     |     |     |     |     |     | 09    |     |     |     |     |     | frontiersin.org |     |

Brookshireetal. 10.3389/fnins.2024.1373515
ChaibubNeto,E.,Pratap,A.,Perumal,T.M.,Tummalacherla,M.,Snyder,P.,Bot, basedon2D-spectralrepresentationofEEGrecordings.Neurocomputing323,96–107.
B.M.,etal.(2019).Detectingtheimpactofsubjectcharacteristicsonmachinelearning- doi:10.1016/j.neucom.2018.09.071
baseddiagnosticapplications.NPJDigit.Med.2:99.doi:10.1038/s41746-019-0178-x
Iešmantas,T.,andAlzbutas,R.(2020).Convolutionalneuralnetworkfordetection
Chang,Y.,Stevenson,C.,Chen,I.-C.,Lin,D.-S.,andKo,L.-W.(2022).Neurological andclassificationofseizuresinclinicaldata.Med.Biol.Eng.Comp.58,1919–1932.
statechangesindicativeofADHDinchildrenlearnedviaEEG-basedLSTMnetworks. doi:10.1007/s11517-020-02208-7
J.NeuralEng.19:016021.doi:10.1088/1741-2552/ac4f07
Jana,R.,Bhattacharyya,S.,andDas,S.(2020).“Patient-specificseizureprediction
Chen,H.,Song,Y.,andLi,X.(2019a).Adeeplearningframeworkforidentifying using the convolutional neural networks,” in Intelligence Enabled Research, eds. S.
childrenwithADHDusinganEEG-basedbrainnetwork.Neurocomputing356,83–96. Bhattacharyya,S.Mitra,andP.Dutta(Springer),51–60.
doi:10.1016/j.neucom.2019.04.058
Kaka,H.,Zhang,E.,andKhan,N.(2021).Artificialintelligenceanddeeplearning
Chen,H.,Song,Y.,andLi,X.(2019b).Useofdeeplearningtodetectpersonalized in neuroradiology: exploring the new frontier. Can. Assoc. Radiol. J. 72, 35–44.
spatial-frequency abnormalities in EEGs of children with ADHD. J. Neural Eng. doi:10.1177/0846537120954293
16:066046.doi:10.1088/1741-2552/ab3a0a
Kaufman, S., Rosset, S., Perlich, C., and Stitelman, O. (2012). Leakage in data
Choi,G.,Park,C.,Kim,J.,Cho,K.,Kim,T.-J.,Bae,H.,etal.(2019).“Anovelmulti- mining:Formulation,detection,andavoidance.ACMTransact.Knowl.Discov.Data
scale3DCNNwithdeepneuralnetworkforepilepticseizuredetection,”in2019IEEE 6,1–21.doi:10.1145/2382577.2382579
InternationalConferenceonConsumerElectronics(ICCE)(LasVegas,NV:IEEE),1–2.
Khan,H.,Marcuse,L.,Fields,M.,Swann,K.,andYener,B.(2017).Focalonset
Chu,L.,Qiu,R.,Liu,H.,Ling,Z.,Zhang,T.,andWang,J.(2017).Individual seizure prediction using convolutional networks. IEEE Transact. Biomed. Eng. 65,
recognitioninschizophreniausingdeeplearningmethodswithrandomforestand 2109–2118.doi:10.1109/TBME.2017.2785401
votingclassifiers:InsightsfromrestingstateEEGstreams.arXiv[preprint].
Khare, S. K., Bajaj, V., and Acharya, U. R. (2021). PDCNNet: an automatic
Daoud, H., and Bayoumi, M. A. (2019). Efficient epileptic seizure prediction frameworkforthedetectionofParkinson’sdiseaseusingEEGsignals.IEEESens.J.
based on deep learning. IEEE Trans. Biomed. Circuits Syst. 13, 804–813. 21,17017–17024.doi:10.1109/JSEN.2021.3080135
doi:10.1109/TBCAS.2019.2929053
Kim,D.,andKim,K.(2018).“DetectionofearlystageAlzheimer’sdiseaseusing
de Bardeci, M., Ip, C. T., and Olbrich, S. (2021). Deep learning applied to EEGrelativepowerwithdeepneuralnetwork,”in201840thAnnualInternational
electroencephalogram data in mental disorders: a systematic review. Biol. Psychol. ConferenceoftheIEEEEngineeringinMedicineandBiologySociety(EMBC)(Honolulu,
162:108117.doi:10.1016/j.biopsycho.2021.108117 HI),352–355.
Demuru, M., and Fraschini, M. (2020). EEG fingerprinting: subject-specific Kim, S., Kim, J., and Chun, H.-W. (2018). Wave2vec: vectorizing
signaturebasedontheaperiodiccomponentofpowerspectrum.Comput.Biol.Med. electroencephalography bio-signal for prediction of brain disease. Int. J. Environ.
120:103748.doi:10.1016/j.compbiomed.2020.103748 Res.PublicHealth15:1750.doi:10.3390/ijerph15081750
Detti, P. (2020). Siena Scalp EEG Database (version 1.0.0). PhysioNet. Kwon,H.,Kang,S.,Park,W.,Park,J.,andLee,Y.(2019).“Deeplearningbased
doi:10.13026/5d4a-j060 pre-screeningmethodfordepressionwithimageryfrontalEEGchannels,”in2019
InternationalConferenceonInformationandCommunicationTechnologyConvergence
Detti,P.,Vatti,G.,andZabaloManriquedeLara,G.(2020).EEGsynchronization
(ICTC)(Jeju:IEEE),378–380.
analysisforseizureprediction:astudyondataofnoninvasiverecordings.Processes
8:846.doi:10.3390/pr8070846 Langa, K. M., and Levine, D. A. (2014). The diagnosis and management of
mild cognitive impairment: a clinical review. J. Am. Med. Assoc. 312, 2551–2561.
Dubreuil-Vall, L., Ruffini, G., and Camprodon, J. A. (2020). Deep learning
doi:10.1001/jama.2014.13806
convolutional neural networks discriminate adult ADHD from healthy
individuals on the basis of event-related spectral EEG. Front. Neurosci. 14:251. Lee,S.,Hussein,R.,andMcKeown,M.J.(2019).“Adeepconvolutional-recurrent
doi:10.3389/fnins.2020.00251 neuralnetworkarchitectureforParkinson’sdiseaseEEGclassification,”in2019IEEE
GlobalConference on Signal and InformationProcessing (GlobalSIP)(Ottawa,ON:
Emami, A., Kunii, N., Matsuo, T., Shinozaki, T., Kawai, K., and Takahashi,
IEEE),1–4.
H. (2019). Seizure detection by convolutional neural network-based analysis
of scalp electroencephalography plot images. NeuroImage Clin. 22:101684. Li, X., La, R., Wang, Y., Hu, B., and Zhang, X. (2020). A deep learning
doi:10.1016/j.nicl.2019.101684 approach for mild depression recognition based on functional connectivity using
electroencephalography.Front.Neurosci.14:192.doi:10.3389/fnins.2020.00192
Folstein,M.F.,Folstein,S.E.,andMcHugh,P.R.(1975).“Mini-mentalstate”:a
practicalmethodforgradingthecognitivestateofpatientsfortheclinician.J.Psychiatr. Li,X.,La,R.,Wang,Y.,Niu,J.,Zeng,S.,Sun,S.,etal.(2019).EEG-basedmild
Res.12,189–198.doi:10.1016/0022-3956(75)90026-6 depressionrecognitionusingconvolutionalneuralnetwork.Med.Biol.Eng.Comp.57,
1341–1352.doi:10.1007/s11517-019-01959-2
Fürbass,F.,Kural,M.A.,Gritsch,G.,Hartmann,M.,Kluge,T.,andBeniczky,S.
(2020).Anartificialintelligence-basedEEGalgorithmfordetectionofepileptiform Li, Y., Liu, Y., Cui, W.-G., Guo, Y.-Z., Huang, H., and Hu, Z.-Y. (2020).
EEGdischarges:validationagainstthediagnosticgoldstandard.Clin.Neurophysiol. EpilepticseizuredetectioninEEGsignalsusingaunifiedtemporal-spectralsqueeze-
131,1174–1179.doi:10.1016/j.clinph.2020.02.032 and-excitation network. IEEE Transact. Neural Syst. Rehabil. Eng. 28, 782–794.
doi:10.1109/TNSRE.2020.2973434
Ganapathi,A.S.,Glatt,R.M.,Bookheimer,T.H.,Popa,E.S.,Ingemanson,M.
L.,Richards,C.J.,etal.(2022).Differentiationofsubjectivecognitivedecline,mild Liang,W.,Pei,H.,Cai,Q.,andWang,Y.(2020).ScalpEEGepileptogeniczone
cognitive impairment, and dementia using qEEG/ERP-based cognitive testing and recognition and localization based on long-term recurrent convolutional network.
volumetricMRIinanoutpatientspecialtymemoryclinic.J.AlzheimersDis.90,1–9. Neurocomputing396,569–576.doi:10.1016/j.neucom.2018.10.108
doi:10.3233/JAD-220616
Loh,H.W.,Ooi,C.P.,Palmer,E.,Barua,P.D.,Dogan,S.,Tuncer,T.,etal.(2021).
Gao, Y., Gao, B., Chen, Q., Liu, J., and Zhang, Y. (2020). Deep convolutional GaborPDNet:gabortransformationanddeepneuralnetworkforParkinson’sdisease
neural network-based epileptic electroencephalogram (EEG) signal classification. detectionusingEEGsignals.Electronics10:1740.doi:10.3390/electronics10141740
Front.Neurol.11:375.doi:10.3389/fneur.2020.00375
Mafi,M.,andRadfar,S.(2022).Highdimensionalconvolutionalneuralnetwork
Gkenios,G.,Latsiou,K.,Diamantaras,K.,Chouvarda,I.,andTsolaki,M.(2022). forEEGconnectivity-baseddiagnosisofADHD.J.Biomed.Phys.Eng.12,645–654.
“Diagnosis of Alzheimer’s disease and mild cognitive impairment using EEG and doi:10.31661/jbpe.v0i0.2108-1380
recurrentneuralnetworks,”in202244thAnnualInternationalConferenceoftheIEEE
Mall,P.K.,Singh,P.K.,Srivastav,S.,Narayan,V.,Paprzycki,M.,Jaworska,T.,
EngineeringinMedicine&BiologySociety(EMBC)(Glasgow:IEEE),3179–3182.
etal.(2023).Acomprehensivereviewofdeepneuralnetworksformedicalimage
Goldberger,A.L.,Amaral,L.A.,Glass,L.,Hausdorff,J.M.,Ivanov,P.C.,Mark, processing:recentdevelopmentsandfutureopportunities.Healthc.Anal.4:100216.
R. G., et al. (2000). PhysioBank, PhysioToolkit, and PhysioNet: components of a doi:10.1016/j.health.2023.100216
newresearchresourceforcomplexphysiologicsignals.Circulation101,e215—220.
Michel,C.M.,andHe,B.(2019).EEGsourcelocalization.Handb.Clin.Neurol.160,
doi:10.1161/01.CIR.101.23.e215
85–101.doi:10.1016/B978-0-444-64032-1.00006-0
Hosny, A., Parmar, C., Quackenbush, J., Schwartz, L. H., and Aerts, H.
Moghaddari, M., Lighvan, M. Z., and Danishvar, S. (2020). Diagnose
J. (2018). Artificial intelligence in radiology. Nat. Rev. Cancer 18, 500–510.
ADHD disorder in children using convolutional neural network based on
doi:10.1038/s41568-018-0016-5
continuous mental task EEG. Comput. Methods Programs Biomed. 197:105738.
Huggins,C.J.,Escudero,J.,Parra,M.A.,Scally,B.,Anghinah,R.,VitóriaLacerdaDe doi:10.1016/j.cmpb.2020.105738
Araújo,A.,etal.(2021).Deeplearningofresting-stateelectroencephalogramsignalsfor
Morabito,F.C.,Campolo,M.,Ieracitano,C.,Ebadi,J.M.,Bonanno,L.,Bramanti,
three-classclassificationofAlzheimer’sdisease,mildcognitiveimpairmentandhealthy
A., et al. (2016). “Deep convolutional neural networks for classification of mild
ageing.J.NeuralEng.18:046087.doi:10.1088/1741-2552/ac05d8
cognitiveimpairedandAlzheimer’sdiseasepatientsfromscalpEEGrecordings,”in
Hussein,R.,Palangi,H.,Ward,R.K.,andWang,Z.J.(2019).Optimizeddeepneural 2016 IEEE 2nd International Forum on Research and Technologies for Society and
networkarchitectureforrobustdetectionofepilepticseizuresusingEEGsignals.Clin. IndustryLeveragingaBetterTomorrow(RTSI)(Bologna),1–6.
Neurophysiol.130,25–37.doi:10.1016/j.clinph.2018.10.010
Mumtaz, W., and Qayyum, A. (2019). A deep learning framework for
Ieracitano, C., Mammone, N., Bramanti, A., Hussain, A., and Morabito, F. C. automatic diagnosis of unipolar depression. Int. J. Med. Inform. 132:103983.
(2019).AConvolutionalNeuralNetworkapproachforclassificationofdementiastages doi:10.1016/j.ijmedinf.2019.103983
FrontiersinNeuroscience 10 frontiersin.org

| Brookshireetal. |     |     |     |     |     |     | 10.3389/fnins.2024.1373515 |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- |
Nasreddine, Z. S., Phillips, N. A., Bédirian, V., Charbonneau, S., Whitehead, applications. Healthc. Inform. Res. 27, 189–199. doi: 10.4258/hir.2021.27.
| V., Collin,    | I., et al. (2005). The | montreal    | cognitive assessment, | MoCA: a           | brief 3.189 |     |     |     |     |
| -------------- | ---------------------- | ----------- | --------------------- | ----------------- | ----------- | --- | --- | --- | --- |
| screening tool | for mild cognitive     | impairment. | J. Am. Geriatr.       | Soc. 53, 695–699. |             |     |     |     |     |
doi:10.1111/j.1532-5415.2005.53221.x Truong, N. D., Nguyen, A. D., Kuhlmann, L., Bonyadi, M. R., Yang, J.,
|     |     |     |     |     | Ippolito, S., | et al. (2018). Convolutional | neural networks | for | seizure prediction |
| --- | --- | --- | --- | --- | ------------- | ---------------------------- | --------------- | --- | ------------------ |
Oh,S.L.,Hagiwara,Y.,Raghavendra,U.,Yuvaraj,R.,Arunkumar,N.,Murugappan, using intracranial and scalp electroencephalogram. Neur. Netw. 105, 104–111.
M.,etal.(2020).AdeeplearningapproachforParkinson’sdiseasediagnosisfromEEG doi:10.1016/j.neunet.2018.04.018
signals.Neur.Comp.Appl.32,10927–10933.doi:10.1007/s00521-018-3689-5
|     |     |     |     |     | Ullah, I., | Hussain, M., Aboalsamh, | H., et al. (2018). | An automated | system for |
| --- | --- | --- | --- | --- | ---------- | ----------------------- | ------------------ | ------------ | ---------- |
Oh,S.L.,Vicnesh,J.,Ciaccio,E.J.,Yuvaraj,R.,andAcharya,U.R.(2019).Deep epilepsydetectionusingEEGbrainsignalsbasedondeeplearningapproach.Expert
convolutionalneuralnetworkmodelforautomateddiagnosisofschizophreniausing Syst.Appl.107,61–71.doi:10.1016/j.eswa.2018.04.021
EEGsignals.Appl.Sci.9:2870.doi:10.3390/app9142870 Uyulan,C.,Ergüzel,T.T.,Unubol,H.,Cebi,M.,Sayar,G.H.,NezhadAsad,M.,
Raghu,S.,Sriraam,N.,Temel,Y.,Rao,S.V.,andKubben,P.L.(2020).EEGbased etal.(2021).Majordepressivedisorderclassificationbasedondifferentconvolutional
multi-classseizuretypeclassificationusingconvolutionalneuralnetworkandtransfer neural network models: deep learning approach. Clin. EEG Neurosci. 52, 38–51.
learning.Neur.Netw.124,202–212.doi:10.1016/j.neunet.2020.01.017 doi:10.1177/1550059420916634
Rashed-Al-Mahfuz,M.,Moni,M.A.,Uddin,S.,Alyami,S.A.,Summers,M.A., Vahid,A.,Bluschke,A.,Roessner,V.,Stober,S.,andBeste,C.(2019).Deeplearning
andEapen,V.(2021).Adeepconvolutionalneuralnetworkmethodtodetectseizures basedonevent-relatedEEGdifferentiateschildrenwithADHDfromhealthycontrols.
andcharacteristicfrequenciesusingepilepticelectroencephalogram(EEG)data.IEEE J.Clin.Med.8:1055.doi:10.3390/jcm8071055
J.Transl.Eng.HealthMed.9,1–12.doi:10.1109/JTEHM.2021.3050925
Wei,X.,Zhou,L.,Chen,Z.,Zhang,L.,andZhou,Y.(2018).Automaticseizure
Rasheed,K.,Qayyum,A.,Qadir,J.,Sivathamboo,S.,Kwan,P.,Kuhlmann,L.,etal. detection using three-dimensional CNN based on multi-channel EEG. BMC Med.
(2020).MachinelearningforpredictingepilepticseizuresusingEEGsignals:areview. Inform.Decis.Mak.18,71–80.doi:10.1186/s12911-018-0693-8
IEEERev.Biomed.Eng.14,139–155.doi:10.1109/RBME.2020.3008792
|     |     |     |     |     | Wei, X., Zhou, | L., Zhang, Z., | Chen, Z., and Zhou, | Y. (2019). | Early prediction |
| --- | --- | --- | --- | --- | -------------- | -------------- | ------------------- | ---------- | ---------------- |
Rosset, S., Perlich, C., S´wirszcz, G., Melville, P., and Liu, Y. (2010). Medical ofepilepticseizuresusingalong-termrecurrentconvolutionalnetwork.J.Neurosci.
datamining:insightsfromwinningtwocompetitions.DataMin.Knowl.Discov.20, Methods327:108395.doi:10.1016/j.jneumeth.2019.108395
439–468.doi:10.1007/s10618-009-0158-x Wen, D., Wei, Z., Zhou, Y., Li, G., Zhang, X., and Han, W. (2018). Deep
Saeb,S.,Lonini,L.,Jayaraman,A.,Mohr,D.C.,andKording,K.P.(2017).The learning methods to process fMRI data and their application in the diagnosis of
needtoapproximatetheuse-caseinclinicalmachinelearning.Gigascience6:gix019. cognitiveimpairment:abriefoverviewandouropinion.Front.Neuroinform.12:23.
| doi:10.1093/gigascience/gix019 |     |     |     |     | doi:10.3389/fninf.2018.00023 |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- |
Shaban,M.(2021).“AutomatedscreeningofParkinson’sdiseaseusingdeeplearning Wen, J., Thibeau-Sutre, E., Diaz-Melo, M., Samper-González, J., Routier, A.,
basedelectroencephalography,”in202110thInternationalIEEE/EMBSConferenceon Bottani,S.,etal.(2020).ConvolutionalneuralnetworksforclassificationofAlzheimer’s
NeuralEngineering(NER),158–161. disease: overview and reproducible evaluation. Med. Image Anal. 63:101694.
Shaban, M., and Amara, A. W. (2022). Resting-state electroencephalography doi:10.1016/j.media.2020.101694
baseddeep-learningforthedetectionofParkinson’sdisease.PLoSONE17:e0263159. Xie,Y.,Yang,B.,Lu,X.,Zheng,M.,Fan,C.,Bi,X.,etal.(2020).“Anxietyand
doi:10.1371/journal.pone.0263159
|     |     |     |     |     | depression diagnosis | method based | on brain networks | and convolutional | neural |
| --- | --- | --- | --- | --- | -------------------- | ------------ | ----------------- | ----------------- | ------ |
networks,”in202042ndAnnualInternationalConferenceoftheIEEEEngineeringin
Shalbaf,A.,Bagherzadeh,S.,andMaghsoudi,A.(2020).Transferlearningwithdeep
convolutionalneuralnetworkforautomateddetectionofschizophreniafromEEG Medicine&BiologySociety(EMBC)(Montreal,QC:IEEE),1503–1506.
signals.Phys.Eng.Sci.Med.43,1229–1239.doi:10.1007/s13246-020-00925-9 You,Z.,Zeng,R.,Lan,X.,Ren,H.,You,Z.,Shi,X.,etal.(2020).Alzheimer’s
Shi,X.,Wang,T.,Wang,L.,Liu,H.,andYan,N.(2019).“Hybridconvolutional diseaseclassificationwithacascadeneuralnetwork.Front.PublicHealth8:584387.
doi:10.3389/fpubh.2020.584387
recurrentneuralnetworksoutperformCNNandRNNintask-stateEEGdetectionfor
Parkinson’sdisease,”in2019Asia-PacificSignalandInformationProcessingAssociation
|     |     |     |     |     | Zhang, X., | Li, J., Hou, K., Hu, | B., Shen, J., and | Pan, J. (2020). | “EEG-based |
| --- | --- | --- | --- | --- | ---------- | -------------------- | ----------------- | --------------- | ---------- |
AnnualSummitandConference(APSIPAASC)(Lanzhou:IEEE),939–944.
depressiondetectionusingconvolutionalneuralnetworkwithdemographicattention
Shoeibi,A.,Khodatars,M.,Ghassemi,N.,Jafari,M.,Moridian,P.,Alizadehsani,R., mechanism,”in202042ndAnnualInternationalConferenceoftheIEEEEngineeringin
etal.(2021).Epilepticseizuresdetectionusingdeeplearningtechniques:areview.Int. Medicine&BiologySociety(EMBC)(Montreal,QC:IEEE),128–133.
J.Environ.Res.PublicHealth18:5780.doi:10.3390/ijerph18115780 Zhao,W.,Zhao,W.,Wang,W.,Jiang,X.,Zhang,X.,Peng,Y.,etal.(2020).Anovel
TaghiBeyglou, B., Shahbazi, A., Bagheri, F., Akbarian, S., and Jahed, M. deepneuralnetworkforrobustdetectionofseizuresusingEEGsignals.Comput.Math.
MethodsMed.2020:9689821.doi:10.1155/2020/9689821
| (2022). Detection | of ADHD        | cases using       | CNN and classical             | classifiers of | raw |     |     |     |     |
| ----------------- | -------------- | ----------------- | ----------------------------- | -------------- | --- | --- | --- | --- | --- |
| EEG. Comp.        | Methods Progr. | Biomed. 2:100080. | doi: 10.1016/j.cmpbup.2022.10 |                |     |     |     |     |     |
Zhao,Y.,andHe,L.(2015).“DeeplearningintheEEGdiagnosisofAlzheimer’s
0080
disease,”inComputerVision-ACCV2014Workshops,LectureNotesinComputer
Tampu,I.E.,Eklund,A.,andHaj-Hosseini,N.(2022).Inflationoftestaccuracydue Science, eds C. Jawahar, and S. Shan (Cham: Springer International Publishing),
| todataleakageindeeplearning-basedclassificationofOCTimages.Sci.Data9:580. |     |     |     |     | 340–353. |     |     |     |     |
| ------------------------------------------------------------------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
doi:10.1038/s41597-022-01618-6
|     |     |     |     |     | Zhou, D., | Liao, Z., and Chen, | R. (2022). Deep | learning enabled | diagnosis of |
| --- | --- | --- | --- | --- | --------- | ------------------- | --------------- | ---------------- | ------------ |
Tosun,M.(2021).EffectsofspectralfeaturesofEEGsignalsrecordedwithdifferent children’sADHDbasedonthebigdataofvideoscreenlong-rangeEEG.J.Healthc.
channelsandrecordingstatusesonADHDclassificationwithdeeplearning.Phys.Eng. Eng.2022:5222136.doi:10.1155/2022/5222136
Sci.Med.44,693–702.doi:10.1007/s13246-021-01018-x
Zhou,M.,Tian,C.,Cao,R.,Wang,B.,Niu,Y.,Hu,T.,etal.(2018).Epileptic
Tougui, I., Jilbab, A., and El Mhamdi, J. (2021). Impact of the choice of seizure detection based on EEG signals and CNN. Front. Neuroinform. 12:95.
cross-validation techniques on the results of machine learning-based diagnostic doi:10.3389/fninf.2018.00095
| FrontiersinNeuroscience |     |     |     |     | 11  |     |     |     | frontiersin.org |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- |