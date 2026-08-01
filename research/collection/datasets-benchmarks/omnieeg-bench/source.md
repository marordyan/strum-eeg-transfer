OmniEEG-Bench: A Standardized Evaluation
Benchmark for EEG Foundation Models
ZilingLu1† ZongshengLi2,1† XinkeShen1† KexinLou1,3† YingyueXin1
XiaoqiChen1 ShinanWang1 XiangChen1 JiahaoFan1 ChenyuHuang1
XinXu1 ZhoujieHou1 ChenWei1,3* QuanyingLiu1,3,4*
1DepartmentofBiomedicalEngineering,SouthernUniversityofScienceandTechnology,Shenzhen,China
2SchoolofComputerScienceandEngineering,TheChineseUniversityofHongKong,Shenzhen,China
3Omni-Intelligence,Shenzhen,China
4ShenzhenLoopAreaInstitute,Shenzhen,China
†Equalcontribution
*Correspondingauthors:liuqy@sustech.edu.cn; chen.wei@omni-intel.cn
3
4
5
6
7
8
9
1 3 5 10 20 50 100
# Pretrained datasets
)retteb
si
rewol(
knar
egarevA
a Performance vs. Dataset diversity
CBraMod BrainOmni
REVE
FEMBA BIOT LaBraM
NeuroLM
NeuroGPT EEGMamba
Per-dataset median ρ=-0.27,
BENDR Wilcoxon p=1.1e-07
3 5 10 20 50 100 200
# Parameters
)retteb
si
rewol(
knar
egarevA
b Performance vs. Model size
CBraMod BrainOmni
REVE
FEMBA BIOT LaBraM
NeuroLM
EEGMamba NeuroGPT
Per-dataset median ρ=-0.21,
BENDR Wilcoxon p=7.0e-04
Figure1: Scalinglawofpretrainingdatadiversity(a)andmodelsize(b)forlinear-probing
generalizationofEEGfoundationmodels. TestsonOmniEEG-Benchwith58datasetsshowthat
EEGfoundationmodelspretrainedonagreaternumberofdatasetsandmodelswithalargernumber
ofparameterstendtoachieveloweraverageranks(i.e.,betterperformance).
Abstract
Electroencephalography (EEG) supports a variety of brain-computer interface
(BCI) tasks ranging from brain-state monitoring to human-LLM interactions.
EEG foundation models are emerging, but evaluation remains fragmented due
to heterogeneous datasets and inconsistent task protocols. Here, we introduce
OmniEEG-Bench,aunifiedbenchmarkanddownstreamtaskroadmapforEEG
foundationmodels(FMs). ItorganizesevaluationofEEGFMsintosixtaskfami-
liesspanning(i)signalreliability,(ii)biometricsanddisease,(iii)consciousness
andstate,(iv)cognitionandemotion,(v)naturalisticstimulusdecoding,and(vi)
motorandinteraction,introducinganewgenerationoftasksnotsystematically
benchmarkedinpriorEEGFMwork. OmniEEG-Benchstandardizesmodelde-
ployment, task definitions, and metrics through a task-card specification, and
unifies54EEGdatasetswithconsistentevaluationprotocols. Webenchmark10
representative EEG foundation models and report a leaderboard that covers di-
verse evaluation settings. Both pretraining dataset diversity and model size are
significantlyassociatedwithbetteraverageranksacrossdatasets,revealingscaling-
law behavior in EEG foundation models (Figure 1). These results suggest that
scaling EEG foundation models requires not only larger architectures but also
broaderandmorediversepretrainingdata. Thebenchmarkcodeisavailableat
https://github.com/ncclab-sustech/omni-eegbench.git.
6202
yaM
03
]GL.sc[
1v51800.6062:viXra

1 Introduction
EEGfoundationmodelsarerapidlyemergingasanewparadigmforbraindecoding: bypretraining
on large-scale, heterogeneous EEG, a single model can be adapted to many downstream tasks,
with the long-term promise of capturing universal EEG representations and enabling practical
“reading the brain” [1, 2, 3]. Recent models, such as BIOT [4], LaBraM [5] and BrainOmni [6],
explicitlypursueuniversalandtransferableEEGrepresentationsviaself-supervisedpretrainingsuch
asmaskedautoencodingandcontrastivelearning. However,thefieldlacksafairwaytocompare
them: eachmodelisevaluatedondifferentdatasets,tasks,andsplitsintermsofdecodingabilityand
generalizability,andevenforthesametask,evaluationsettingscansubstantiallyaltertheresults.
Thisfragmentationobscureswhatfoundationmodelstrulyimprove,andhindersthedevelopmentof
robustandgeneralizablebraindecodingsystems.
Thislackofcomparabilityisnotonlyaprotocolissue. Italsoreflectstheabsenceofasharedview
ofwhatEEGfoundationmodelsshouldbegoodat. Differentworkimplicitlyprioritizesdifferent
taskfamilies,making“general-purposeEEGrepresentation”difficulttooperationalize. Acoherent
task roadmap is therefore a prerequisite for fair evaluation: it makes the capability axes explicit
andencouragesmodelstobeassessedacrossabroadspectrumofEEGobjectivesratherthanafew
isolatedsettings. EEGtasksspanawiderangeofregimes,fromclinicalabnormalitydetection[7]to
globalstatemonitoring(suchassleepstaging)[8]andfast,low-latencyBCIcontrol[9]. Meanwhile,
recentopendatasetsincreasinglycaptureEEGundermorenaturalistic,high-dimensionalsensory
contexts—suchasviewingrichvisualscenes[10]orlisteningtocontinuousspeech[11,12]—where
thestimulusspaceiscomplex[13]. However,mostEEGfoundationmodelsarestillevaluatedona
narrowsubsetofcontrolledparadigms,andarerarelytestedinastandardizedwayonthesenaturalistic-
contextdatasets. Therefore,abenchmarkshouldreflectthefield’sevolutionfromtightlycontrolled
experimentstowardnaturalistic,interaction-centricparadigms,whilemaintainingstandardization
throughwell-definedtasks.
WeintroduceOmniEEG-Bench,astandardizedevaluationbenchmarkforEEGfoundationmodels.
OmniEEG-Benchorganizesdownstreamevaluationintosixtaskfamilies: (i)signalreliability,(ii)
biometrics and disease, (iii) consciousness and state, (iv) cognition and emotion, (v) naturalistic
stimulusdecoding,and(vi)motorandinteraction. Thistaxonomyisorganizedbythreedimensions:
fromstabletraitstotransientstates,fromslow-tofast-changingtemporalscales,andfrompassive
monitoringtoactiveinteraction. Westandardizepreprocessing,taskdefinitions,andmetricsthrough
a task-card specification. We benchmark 10 EEG foundation models on 54 EEG datasets with a
protocolsuitethatprobesfourcomplementarycapabilities:(i)multi-subjectcross-trialadaptation,(ii)
cross-subjecttransfer,(iii)label-efficiencyviazero-/few-shotadaptation,and(iv)noiserobustness
undersensordegradationviachannelcorruption. Ourcontributionsarethreefold:
• AunifiedtaskroadmapforEEGfoundationmodels. WeorganizeEEGdownstream
evaluationintosixtasktaxonomiesandformalizeeachtaskwithatask-cardspecification
thatstandardizespreprocessing,inputs/outputs,andmetrics.
• Standardizedevaluationprotocolsthatprobetransfer,dataefficiency,androbustness.
We report results under multi-subject (trial-level splits with pooled subjects) and cross-
subject(held-outsubjects)settings,andfurtherincludezero-shot/few-shotadaptationand
channel corruption tests. These tests systematically characterize the transferability and
robustnessofpretrainedrepresentations.
• Large-scale,reproduciblebenchmarkingwithdiagnosticinsights. Webenchmark10
EEGfoundationmodelson54EEGdatasets,releaseapublicleaderboard,andidentifythe
predictivefactorsthatinfluencethemodel’sdownstreamperformance.
2 EEGTaskTaxonomyandDatasetOrganization
OmniEEG-Benchadoptsacapability-driventasktaxonomythatorganizesdownstreamEEGtasksinto
acontinuoustaskspace,asillustratedinFig.2. Weusethreebroadorganizingdimensionstoguide
thisdesign.First,tasksdifferintheextenttowhichtheyreflectstablesubject-specificcharacteristics
ortransientbrainstates,consistentwiththeviewthatEEGmeasurementscancontainbothtrait-like
andstate-dependent components[14]. Biometricsand clinicalphenotyping emphasizerelatively
2

Figure 2: Task taxonomy of OmniEEG-Bench. We organize 58 tasks (from 54 datasets) into 6
categories: signalreliability,biometricsanddisease,consciousnessandstate,cognitionandemotion,
naturalisticstimulusdecoding,andmotorandinteraction.
stableindividualvariability,whereassleepstaging,vigilance,emotionrecognition,andtask-context
decodingemphasizetime-varyingneuraldynamics. Second,tasksdifferintemporalscale,ranging
fromslowglobalstateestimationtofasterperceptual,cognitive,andinteraction-relateddecoding.
Thisdimensionseparatestasksthatcanbecharacterizedoverextendedwindowsfromthoserequiring
more temporally precise predictions. Naturalistic stimulus decoding is included as an important
dynamicregimebecausenaturalisticstimuliprovidericherandmorecontinuoussensorycontexts
thanclassicalcontrolledparadigms[13]. Third,tasksdifferintheirinteractionregime,frompassive
monitoringtoactivebrain-computerinteraction.Inpassivesettings,EEGisusedtomonitorcognitive,
affective,orbrain-statevariableswithoutrequiringtheusertoactivelygeneratecontrolsignals. In
activesettings,theuserintentionallymodulatesmentalactivity,suchasmotorimagery,andmodel
predictionsmaysupportclosed-loopcontrol[15].
Underthisframing,thesixOmniEEG-BenchfamiliescovercomplementarytaskregionsofEEG:
signal reliability assesses artifact sensitivity and session consistency, biometrics and disease
capturestrait-likeindividualandclinicalvariability,consciousnessandstatetargetsglobalbrain-
statedynamics,cognitionandemotioncoversaffectiveandcognitivechangesatintermediatetime
scales,naturalisticstimulusdecodingevaluatesperceptualandsemanticdecodingunderdynamic
real-worldstimuli,andmotorandinteractionfocusesontime-sensitiveintentdecodingandcontrol.
Type-I:Signalreliability. Thisfamilyprobesartifact-awareandsession-consistentrepresentations.
Weinclude(i)ocularartifact/noiseidentification(EEGDenoiseNet)and(ii)longitudinalstability,
whererepresentationsofthesameparticipantshouldremainconsistentacrosssessions(Longitudinal
test-retest).
3

Type-II:Biometricsanddisease. Thisfamilyevaluatesclinicallyandbiologicallymeaningful
individualdifferences.Subtypesinclude(i)stabletraits(MPI-LEMONderivedage/gender/personality
splits),(ii)epilepsyandabnormalities(HFO,TUAB,TUEP,TUSL,TUEV,andSienaEEG),(iii)
neurodevelopmentaldisorders(ADHD),(iv)neurodegenerativedisorders(AD65, PD31, andPD
mortalityprognosis),and(v)mentaldisorders(MDD,TDBRAIN,Depressionresting,andMODMA).
Type-III:Consciousnessandstate. Thisfamilytargetsglobalbrainstateandslow-to-intermediate
dynamics. Subtypesinclude(i)consciousnessleveldetection(Awakening),(ii)sleepstaging(e.g.,
ISRUC-SleepI/II/III,Sleep-EDF,andHMC),and(iii)cognitivetaskidentification(e.g.,HBN-EEG,
PEARL-Neuro,RestCog).
Type-IV:Cognitionandemotion. Thisfamilycoversaffectiveandcognitivelabelswithmorerapid
dynamics. Weinclude(i)vigilancedetection(SEED-VIG),(ii)emotionrecognitionacrossdiverse
elicitationsettingsandlabelgranularities,rangingfromvideo-drivenaffectinduction(DEAP,SEED,
SEED-IV,SEED-V,SEED-VII,andSEED-FRA,EEG-SVRec,FACED)tomusic(MusicEEG)and
conversational(CIRE)contexts,withlabelspacesspanningbinaryvalenceorarousalclassification
(DEAP),mid-granularitycategoricalemotion(SEED/SEED-IV/SEED-V/SEED-VII,3–7classes),
andmorefine-grainedcategories(FACED,9classes),and(iii)cognitiveloadassessment(EEGMAT
andWorkload).
Type-V:Naturalisticstimulusdecoding. Thisfamilytargetsfast-timescaledecodingundernatu-
ralisticstimuli,wherelabelscorrespondtostimulusattributesornaturallistening/reading/viewing
context. Weinclude(i)naturalspeechperceptionandauditoryattention,encompassingmulti-class
speechphrasediscrimination(BCISpeech),selectiveattentiontocompetingspeakers(Broderick,
cocktailparty),andforwardversusreversedspeechdiscrimination(Broderick,reverse);(ii)natural
readingwithtonaldiscrimination(ChineseEEG2readingaloudcondition,fourMandarintones);and
(iii)visualsemanticcategorization(ThingsEEG2,biologicalvs. non-biological).
Type-VI: Motor and interaction. This family focuses on active intent decoding for control
andinteraction-centricmonitoring. Subtypesinclude(i)motorimagery(BCIC-IV-2a,BCIC-IV-1,
PhysioNet-MI,andSHU-MI),(ii)SSVEPcontrol(BETA-SSVEP,Benchmark-SSVEP,Dual-Freq-
SSVEP,SSVEP-9-chn),(iii)error-relatedpotentialfeedbackdecoding(MonitoringErrP),and(iv)
closed-loopassistivecontrol(EEG-controlledexoskeleton).
SeeAppendixAfordetailsandreferencesofthe58tasksinOmniEEG-Bench.
3 EvaluationProtocols
To systematically assess the transferability, data efficiency, and robustness of EEG foundation
models, we implement four complementary evaluation paradigms: (i) cross-subject transfer, (ii)
multi-subject adaptation, (iii) few-shot adaptation, and (iv) channel masking robustness (Fig. 3).
Theseconfigurationsarematerializedthroughflexibledataloadingstrategies,includingcross-subject
splits,cross-trialsplits,few-shotdownsampling,andchannelmasking. Wepreprocessthe54EEG
datasetsthroughastandardizedpipelineofdownsampling,band-passandnotchfiltering,common
averagereferencing,andwindowsegmentation(SeeAppendixIfordetails). Tofacilitateefficient
benchmarking while maintaining statistical reliability, we randomly select up to 40 samples per
subjectperclassforlinearprobing(determinedbyvariancestabilizationanalysisinAppendixD),
fromwhichallsubsequentsplitsderive.
AllbackbonearchitecturesarewrappedinacommoninterfacethatacceptsanEEGsamplex∈RC×T
andoutputsarepresentationz = f (x). Alightweightlinearclassifierg(·)mapsz totasklogits.
θ
Weadoptlinearprobingastheprimaryevaluationmethod—freezingthepretrainedbackboneθand
trainingonlytheclassificationhead. Thisprotocolenablesheterogeneousmodelstobeevaluated
under consistent input specifications and optimization settings. To characterize the performance
ceilingofeacharchitecture,weadditionallyperformfullfine-tuningonallthedatasetsfromeachtask
categoryunderthecross-subjectsetting. WebenchmarktenrepresentativeEEGfoundationmodels:
BENDR,BIOT,LaBraM,CBraMod,BrainOmni,FEMBA,Neuro-GPT,NeuroLM,EEGMamba,
andREVE.Wereportresultsaveragedovermultipleindependentruns,eachusingapre-generated,
fixeddatasplitderivedfromadifferentrandomseed. Threerunswereemployedforcross-subject
4

Figure 3: OmniEEG-Bench evaluation pipeline, equipped with four evaluation protocols: cross-
subjecttransfer,multi-subjecttrial-leveladaptation,zero-/few-shotadaptation,andchannel-masking
robustness.
transferandmulti-subjectadaptation,andfiveforzero-/few-shotadaptationandchannelmasking.
This ensures fair and comparable performance estimates in the benchmark. The four evaluation
protocolsaredetailedbelow:
Cross-subjecttransferandprimaryleaderboard. Inthecross-subjectsetting,splitsaremadeat
thesubjectlevel: subjectsarepartitionedintotrain/validation/testgroupswitharatioof8:1:1. For
theprimaryleaderboard,weusecross-subjecttransferwheneversubject-levelsplittingismeaningful.
Forthesignal-reliabilitytask(Longitudinaltest-retest)thatdonotadmitastandardheld-out-subject
formulation,weusethecorrespondingmulti-subjectprotocolasafallbackandincludetheminthe
mainleaderboardfortaskcoverage.
Multi-subjectadaptation. Inthemulti-subjectsetting,samplesfromeachsubjectaresplitinto
train/validation/testwithan8:1:1ratioovertrialsandpooledacrosssubjects. Thissettingrequiresthe
modeltogeneralizetounseentrials,measuringadaptationwhentrainingdataspansmultiplesubjects.
Zero-shotandfew-shotadaptation. Toquantifydataefficiency,weevaluatefew-shotadaptation
bysamplinglabeledexamplesofratiokperclassfromthetrainingsplit(k ∈{0.02,0.05,0.1,0.3}).
Zero-shot is treated as the k = 0 special case with no dataset-specific supervised training. We
computethepairwisecosinesimilaritybetweensampleembeddings. Foreachsamplefromthetest
split,weidentifyitsmostsimilarsamplefromthevalidationsplit(toavoidinformationleakage)in
theembeddingspaceandcheckwhetherthetwosamplessharethesameclasslabel. Thepredictionis
countedascorrectifthelabelsmatchandincorrectotherwise. Thedatasplitfollowsthecross-subject
setting.
Channelmaskingrobustness. Tomeasurethemodel’srobustnesstomissingordegradedsensors,
we apply channel masking in linear probing: For each sample, a random subset of channels is
5

Figure4: Primarycross-subject-prioritizedleaderboardoftenEEGfoundationmodels.
6

zero-maskedwithacorruptionratiop∈{20%,40%,60%,80%}. Wereporttheperformancewith
increasing channel corruptions, using fixed corruption seeds across models. The data split also
followsthecross-subjectsetting.
4 Results
4.1 Primarycross-subjecttransferbenchmark
Intheprimarylinear-probingbenchmark,weprioritizecross-subjecttransferbecauseEEGfoundation
modelsareexpectedtolearnrepresentationsthatgeneralizetounseenindividuals. Forthedataset
wherecross-subjectevaluationisnotmeaningfulornotapplicable(Longitudinaltest-retest),weuse
thecorrespondingmulti-subjectevaluationasafallback.Underthiscross-subject-prioritizedprotocol,
BrainOmniachievesthebestoverallaveragerank,followedbyCBraModandREVE(Fig.4;see
SupplementaryTable5fordetailedaccuracy).
Across tasks, the majority of models achieve above-chance performance. Several tasks are es-
peciallydifficult, includingParkinson’sdetection(PD31), arousalclassification(DEAP-arousal),
speechattentiondetection(Broderick-Cocktail-party),natural-versus-reversedspeechclassification
(Broderick-reverse),imageconceptidentification(ThingsEEG2),anderror-relatedpotentialdetection
(Monitoring-Errp). Overall,naturalisticstimulusdecodingemergesasoneofthemostchallenging
taskcategoriesforcurrentEEGfoundationmodels.
Underfullfine-tuning,themodelrankingschangesubstantiallycomparedwithlinearprobing,with
CBraMod,LaBraM,andFEMBAachievingthetopthreeoverallrankswithaverageranksof4.51,
4.88,and5.42,respectively(SupplementaryFig. 3;seeSupplementaryTable7fordetailedaccuracy).
Thissuggeststhatthesemodelscanbenefitsubstantiallyfromtask-specificend-to-endoptimization.
WefurthercompareEEGfoundationmodelswithtwotask-specificbaselines,EEGConformerand
EEGNet. Underfullfine-tuning,sevenfoundationmodelsoutperformEEGConformer(avg. rank
7.25) and nine outperform EEGNet (avg. rank 8.24), highlighting the advantage of pretrained
modelsaftertask-specificadaptation. Incontrast,underlinearprobing,onlyfivefoundationmodels
surpassEEGConformer(avg. rank6.66),whilefivefallbehindthisbaseline(SupplementaryFig. 5),
indicatingthatfrozenpretrainedrepresentationsremainsubstantiallylimitedfordirecttransfer.
4.2 Zero-shotandfew-shotlearning
Underfew-shotadaptation,BrainOmniexhibitssteeperperformancescalingwithsamplesize,indicat-
ingsuperiorsampleefficiencyduringlinearprobing(Fig.5). Taskcategoriesdisplayheterogeneous
scaling behaviors: Longitidinal test-retest and HMC datasets show gradual, monotonic gains as
training data increases. By contrast, most models plateau in FACED, AD65, and Physionet-MI
datasetsoncethefew-shotratioexceeds0.05. Notably, severalmodelslikeBrainOmnidefythis
saturation trend in FACED as well as Physionet-MI datasets, continuing to improve beyond this
threshold.
4.3 Robustnesstochannelcorruptions
Onthelongitudinaltest-retestdataset,mostmodelsexhibitrobustnesstochannelcorruption,except
forBrainOmni(Fig.6). Onothertasks,performancedegradesgraduallyaschanneldropoutincreases.
Notably,BIOTsustainsstableperformanceundermoderatecorruption(ratiosof0.2and0.4). At
severecorruptionlevels(ratiosof0.6and0.8),mostmodelscollapsetonear-chanceperformance.
4.4 Predictivefactorsofmodelperformance
ToidentifythekeyfactorsthatinfluencethegeneralizationperformanceofEEGfoundationmodels,
wesystematicallyanalyzedtherelationshipsbetweenmodelperformanceandthenumberofpre-
trainingdatasets,numberoftrainingsubjects,traininghours,modelsize,publicationyear,model
architecture,pretrainingparadigm,tokenizationstrategy,andspatialmodelingdesign. First,Fig.1
showsthatboththenumberofpretrainingdatasetsandmodelsizearesignificantlyassociatedwith
betteraverageranksacrossdatasets. Specifically,modelspretrainedonmoredatasetstendtoachieve
loweraverageranks,suggestingthatdatasetdiversityisanimportantfactorforimprovinggeneraliza-
tion. Meanwhile,largermodelsalsoshowbetteroverallrankings,indicatingemergingscaling-law
7

Figure5: Theperformanceofzero-shotandfew-shotlearning.
Figure6: Therobustnessofmodelperformanceonchannelmasking.
behaviorinEEGfoundationmodels. Furtherper-datasetSpearmancorrelationanalysessupportthis
trend. Foreachdataset,wecomputedtheSpearmancorrelationbetweeneachmodelfactorandthe
modelrank,andthenusedaWilcoxonsigned-ranktesttoassesswhethertheresultingcorrelations
weresystematicallydifferentfromzero. Becauselowerranksindicatebetterperformance,anegative
correlation means that a larger value of the corresponding factor is associated with better model
performance. Thenumberofpretrainingdatasetsshowsamediancorrelationofρ=−0.27witha
Wilcoxonp=1.1×10−7,indicatingthattheassociationbetweendatasetdiversityandimproved
performanceisconsistentacrossmultipledatasets.
Fig.7furthercomparestheeffectsofdifferentmodelfactorsonperformance. Amongquantitative
factors, publication year, model size, and the number of pretraining datasets are all significantly
associatedwithbetterper-datasetranks,withpublicationyearshowingthestrongestcorrelation. This
suggeststhatmorerecentEEGfoundationmodelstendtobenefitfromlargermodelcapacity,richer
pretrainingdata,andupdatedmodelingdesigns. Incontrast,traininghoursandthenumberoftraining
subjects show weaker associations with performance, suggesting that simply increasing training
time or the number of subjects does not necessarily lead to stable improvements in downstream
generalization. Qualitativearchitectureanalysesshowthatmaskedreconstructionpretraining,VQ-
basedtokenization,andCriss-Crossspatialmodelingeachsignificantlyoutperformtheirrespective
8

| a         | Factor-performance correlations |     |     |     | b Model pretraining/design profiles |     |     |     |
| --------- | ------------------------------- | --- | --- | --- | ----------------------------------- | --- | --- | --- |
| Publica t | io n -0.40 ****                 |     |     |     | 1.0                                 |     |     |     |
Y e a r
rotcaf ngised dezilamroN
0.8
| log(# Params) |     | -0.21 *** |     |     |     |     |     |     |
| ------------- | --- | --------- | --- | --- | --- | --- | --- | --- |
0.6
| Tra in | in g | -0.08 |     |     |     |     |     |     |
| ------ | ---- | ----- | --- | --- | --- | --- | --- | --- |
H ou r s
0.4
| #  T ra i n | i n g | -0.10 |     |     |     |     |     |     |
| ----------- | ----- | ----- | --- | --- | --- | --- | --- | --- |
S u b j e c t s
0.2
| # Pre tr a in | i n g -0.27 **** |     |     | P e r - d a t a s e t  median rho |     |     |     |     |
| ------------- | ---------------- | --- | --- | --------------------------------- | --- | --- | --- | --- |
| D a ta s      | e t s            |     |     | A v g - r a n k   rh o            | 0.0 |     |     |     |
-1.00 -0.75 -0.50 -0.25 0.00 0.25 0.50 0.75 1.00 Dataset Training Model size Publication
|     |     | Spearman ρ (negative = better rank) |     |     | diversity | subjects | (log params) | year |
| --- | --- | ----------------------------------- | --- | --- | --------- | -------- | ------------ | ---- |
Model
|     |                                 |     |     |     |                            | BrainOmni REVE | BIOT NeuroLM EEGMamba |     |
| --- | ------------------------------- | --- | --- | --- | -------------------------- | -------------- | --------------------- | --- |
|     |                                 |     |     |     |                            | CBraMod FEMBA  | LaBraM NeuroGPT BENDR |     |
| c   | Architecture factor comparisons |     |     |     | d Dataset diversity effect |                |                       |     |
|     | 0                               |     |     |     |                            |                | ***                   |     |
per-DS p=1.7e-04
| )retteb si rewol( knaR gvA | 2   |     |     | **** | 2   |     |     |     |
| -------------------------- | --- | --- | --- | ---- | --- | --- | --- | --- |
per-DS p=1.1e-08
knar tesatad-reP
CrissCross
|     | 4 * | per-DS  * p * = ** 4.8e-08 | per-DS p | * =1.3e-02 | 4   |     |     |     |
| --- | --- | -------------------------- | -------- | ---------- | --- | --- | --- | --- |
per-DS p=2.4e-02
|     | Transformer-family | Masked Recon. | VQ-based |     |     |     |     |     |
| --- | ------------------ | ------------- | -------- | --- | --- | --- | --- | --- |
Non-VQ
|     | 6 Mamba |     |     | Others | 6   |     |     |     |
| --- | ------- | --- | --- | ------ | --- | --- | --- | --- |
Contrastive
8
8
10
10
|     | Backbone | Pretrain | Tokenization | Spatial  |     | Single-dataset | Multi-dataset |     |
| --- | -------- | -------- | ------------ | -------- | --- | -------------- | ------------- | --- |
|     |          | Paradigm |              | Modeling |     | 4 models       | 6 models      |     |
Figure7: Pretrainingdesignfactorsandcross-subjectlinear-probingperformanceofEEGfoundation
models. Quantitative factors are evaluated via per-dataset Spearman correlations with Wilcoxon
signed-ranktests(a,b). Per-datasetmedianrhorepresentsthemediancorrelationsofmodelranks
andthepredictivefactoroneachdataset. Avg-rankrhorepresentsthecorrelationofaveragemodel
ranksandthepredictivefactor. QualitativefactorsarecomparedusingpairedWilcoxontestsbetween
modelgroups(c),andsingle-versusmulti-datasetpretrainingiscomparedviaMann–WhitneyUtest
(d).
alternatives, indicating that effective architectural and training-objective designs remain critical
determinants of performance. Finally, models pretrained on multiple datasets outperform those
pretrainedonasingledatasetoverall,furthersupportingtheimportanceofdatasetdiversityforEEG
foundationmodelgeneralization.Overall,theseresultsindicatethatimprovementsinEEGfoundation
modelsarenotdrivenbyasinglefactor,butbythejointeffectsofpretrainingdatadiversity,model
scale,temporalprogressinmodeldevelopment,andarchitecturaldesign.
5 Conclusion
Inthiswork,wepresentOmniEEG-Bench,acomprehensivebenchmarkforevaluatingEEGfounda-
tionmodelsacross54datasetsand58tasks. ByorganizingdownstreamEEGevaluationintosixtask
familiesandstandardizingpreprocessing,taskdefinitions,andevaluationprotocols,OmniEEG-Bench
providesaunifiedtestbedforassessingthetransferability,dataefficiency,androbustnessofEEG
foundationmodels.
Our results show that EEG foundation models can benefit substantially from task-specific fine-
tuning, whereas frozen representations remain limited under direct linear probing. Performance
also varies markedly across task families, with naturalistic stimulus decoding posing one of the
greatest challenges for current models. Beyond the leaderboard, our diagnostic analyses reveal
scaling-law-liketrends: modelspretrainedonmorediversedatasetsandmodelswithlargerparameter
countstendtoachievebetteraverageranksacrossdatasets. Thesefindingssuggestthatimproving
EEGfoundationmodelsmayrequirenotonlylargerarchitectures,butalsobroaderandmorediverse
pretrainingdata. Inaddition,VQ-basedtokenizationandcriss-crossspatialmodelingareassociated
9

withstrongerdownstreamperformance,indicatingthatarchitecturalandpretraining-designchoices
remaincriticalforgeneralization.
Byprovidingapublicleaderboard,standardizedtaskcards,andtransparentevaluationprotocols,
OmniEEG-BenchaimstosupportmorereproducibleandcomparableresearchonEEGfoundation
models. Wehopethatthisbenchmarkwillserveasafoundationfortrackingprogress,diagnosing
modellimitations,andguidingthedevelopmentofmoregeneralizableEEGrepresentationlearning
methods.
6 Limitations
In this work, the evaluation is limited to linear probing and full fine-tuning without exploring
parameter-efficienttransferstrategies.Additionally,the54datasets,whilediverse,donotexhaustively
coverallclinicalpopulations,recordingcontexts,orgeographicregions,andthechannelcorruption
simulationsimplifiesreal-worldsensordegradationpatterns.
ImpactStatement
The goal of this paper is to advance the field of brain-computer interfaces through standardized
benchmarkingofEEGfoundationmodels. EEGdatahavediverseapplicationsinclinicalmonitoring,
assistivetechnologies,andneuroscienceresearch,andourworkaimstosupportprogressintheseareas
throughsystematic,rigorousevaluations. Therearepotentialsocietalconsequencesofimprovements
in EEG-based modeling, including enhanced diagnostic tools and accessible neurotechnologies.
However,thesedevelopmentsalsoraiseconsiderationsarounddataprivacy,equitableaccess,and
responsibledeployment. Althoughourbenchmarkitselfdoesnotintroducenewmodelingtechniques,
itcanaccelerateresearchthatimpactsusersacrossclinicalandconsumerdomains. Weencourage
carefulconsiderationofethical,privacy,andsocietalimplicationsinsubsequentresearchthatbuilds
uponthisbenchmark.
10

References
[1] GayalKuruppu,NeerajWagh,VaclavKremen,SandipanPati,GregoryWorrell,andYogatheesanVarathara-
jah. Eegfoundationmodels:Acriticalreviewofcurrentprogressandfuturedirections. arXivpreprint
arXiv:2507.11783,2025.
[2] XinliangZhou,ChenyuLiu,ZhishengChen,KunWang,YiDing,ZiyuJia,andQingsongWen. Brain
foundationmodels: Asurveyonadvancementsinneuralsignalprocessingandbraindiscovery. arXiv
preprintarXiv:2503.00580,2025.
[3] Jiamin Wu, Zichen Ren, Junyu Wang, Pengyu Zhu, Yonghao Song, Mianxin Liu, Qihao Zheng, Lei
Bai,WanliOuyang,andChunfengSong. Adabrain-bench:Benchmarkingbrainfoundationmodelsfor
brain-computerinterfaceapplications. arXivpreprintarXiv:2507.09882,2025.
[4] ChaoqiYang,MWestover,andJimengSun. Biot: Biosignaltransformerforcross-datalearninginthe
wild. AdvancesinNeuralInformationProcessingSystems,36:78240–78260,2023.
[5] Wei-BangJiang,Li-MingZhao,andBao-LiangLu. Largebrainmodelforlearninggenericrepresentations
withtremendousEEGdatainBCI. InTheTwelfthInternationalConferenceonLearningRepresentations,
2024.
[6] QinfanXiao,ZiyunCui,ChiZhang,SiqiChen,WenWu,AndrewThwaites,AlexandraWoolgar,Bowen
Zhou,andChaoZhang. Brainomni:Abrainfoundationmodelforunifiedeegandmegsignals. InThe
Thirty-ninthAnnualConferenceonNeuralInformationProcessingSystems,2025.
[7] HaoZhang,Qing-QiZhou,HeChen,Xiao-QingHu,Wei-GuangLi,YangBai,Jun-XiaHan,YaoWang,
Zhen-HuLiang,DanChen,etal. Theappliedprinciplesofeeganalysismethodsinneuroscienceand
clinicalneurology. MilitaryMedicalResearch,10(1):67,2023.
[8] HuyPhanandKaareMikkelsen. Automaticsleepstagingofeegsignals:recentdevelopment,challenges,
andfuturedirections. PhysiologicalMeasurement,43(4):04TR01,2022.
[9] Kaido Värbu, Naveed Muhammad, and Yar Muhammad. Past, present, and future of eeg-based bci
applications. Sensors,22(9):3331,2022.
[10] TijlGrootswagers,IvyZhou,AmandaKRobinson,MartinNHebart,andThomasACarlson. Humaneeg
recordingsfor1,854conceptspresentedinrapidserialvisualpresentationstreams. ScientificData,9(1):3,
2022.
[11] MichaelPBroderick,AndrewJAnderson,GiovanniMDiLiberto,MichaelJCrosse,andEdmundCLalor.
Electrophysiologicalcorrelatesofsemanticdissimilarityreflectthecomprehensionofnatural,narrative
speech. CurrentBiology,28(5):803–809,2018.
[12] SitongChen,BeiqianyiLi,CuilinHe,DongyangLi,MingyangWu,XinkeShen,SongWang,XuetaoWei,
XindiWang,HaiyanWu,etal. Aneegdatasetformultimodalsemanticalignmentandneuraldecoding
duringreadingandlistening. ScientificData,2025.
[13] SaurabhSonkusare,MichaelBreakspear,andChristineGuo.Naturalisticstimuliinneuroscience:critically
acclaimed. Trendsincognitivesciences,23(8):699–714,2019.
[14] TimMartin,EricaHolliday,CyrilOkhio,AlexisNewman,LamarLaTella,MakaylaMcginnis,Bruno
Giordani,VoykoKavcic,etal. States,traits,andtherestingstateeegtaskaftereffect. InternationalJournal
ofPsychophysiology,210:112523,2025.
[15] XiaorongGao,YijunWang,XiaogangChen,andShangkaiGao. Interface,interaction,andintelligencein
generalizedbrain–computerinterfaces. Trendsincognitivesciences,25(8):671–684,2021.
[16] HaomingZhang,MingqiZhao,ChenWei,DanteMantini,ZheruiLi,andQuanyingLiu. Eegdenoisenet:
a benchmark dataset for deep learning solutions of eeg denoising. Journal of Neural Engineering,
18(5):056057,2021.
[17] ShantanuSarkar,KevinNathan,andJoseL.Contreras-Vidal. "dataset: Eeg-controlledexoskeletonfor
walkingandstanding-alongitudinalstudyofhealthyindividuals",2025.
[18] AnahitBabayan,MirayErbey,DenizKumral,JanisDReinelt,AndreaMFReiter,JosefinRöbbig,HLina
Schaare,MarieUhlig,AlfredAnwander,Pierre-LouisBazin,etal. Amind-brain-bodydatasetofmri,eeg,
cognition,emotion,andperipheralphysiologyinyoungandoldadults. Scientificdata,6(1):1–21,2019.
[19] DorottyaCserpan,EceBoran,RichardRosch,SanPietroLoBiundo,GeorgiaRamantani,andJohannes
Sarnthein. "datasetofeegrecordingsofpediatricpatientswithepilepsybasedonthe10-20system",2021.
11

[20] IyadObeidandJosephPicone. Thetempleuniversityhospitaleegdatacorpus. FrontiersinNeuroscience,
Volume10-2016,2016.
[21] AmirHarati,MeysamGolmohammadi,SilviaLopez,IyadObeid,andJosephPicone. Improvedeegevent
classificationusingdifferentialenergy. InIEEESignalProcessinginMedicineandBiologySymposium
(SPMB),2015.
[22] NeuralEngineeringDataConsortium. Templeuniversityeegcorpus-downloads,2026.
[23] PaoloDetti. Sienascalpeegdatabase. PhysioNet,2020.
[24] GhasemSadeghiBajestani,ShimaAbedian,FatemehMakhloughi,MotahharehRaoufitabar,andHamid
Saeedi. Adatasetofeegsignalsfromadultswithadhdandhealthycontrols: Restingstate,cognitive
function,andsoundlisteningparadigm. MendeleyData,2023.
[25] AndreasMiltiadous,KaterinaDTzimourta,TheodoraAfrantou,PanagiotisIoannidis,NikolaosGrigoriadis,
DimitriosGTsalikakis,PantelisAngelidis,MarkosGTsipouras,EuripidisGlavas,NikolaosGiannakeas,
etal. Adatasetofscalpeegrecordingsofalzheimer’sdisease, frontotemporaldementiaandhealthy
subjectsfromroutineeeg. Data,8(6):95,2023.
[26] AlexanderP.Rockhill,NickoJackson,JobiGeorge,AdamAron,andNicoleC.Swann. "ucsandiego
restingstateeegdatafrompatientswithparkinson’sdisease",2021.
[27] SiminJamshidi,ArturoEspinoza,SouraDasgupta,andNandakumarNarayanan. "eegmortalitydatasetin
parkinson’sdisease",2025.
[28] WajidMumtaz. MDDPatientsandHealthyControlsEEGData(New). 112016.
[29] HannekeVanDijk,GuidoVanWingen,DamiaanDenys,SebastianOlbrich,RosalindeVanRuth,and
MartijnArns. Thetwodecadesbrainclinicsresearcharchiveforinsightsinneurophysiology(tdbrain)
database. Scientificdata,9(1):333,2022.
[30] JamesFCavanaghjcavanagh@unm.edu. "eeg:Depressionrest",2021.
[31] HanshuCai,YiwenGao,ShutingSun,etal.Modmadataset:amulti-modalopendatasetformental-disorder
analysis. CoRR,abs/2002.09283,2020.
[32] ImadJBajwa,AndreSNilsen,RenéSkukies,ArnfinnAamodt,GernotErnst,JohanFStorm,andBjørnE
Juel. Arepeatedawakeningstudyexploringthecapacityofcomplexitymeasurestocapturedreaming
duringpropofolsedation. ScientificReports,15(1):32746,2025.
[33] SirvanKhalighi,TeresaSousa,JoséMoutinhoSantos,andUrbanoNunes. Isruc-sleep:Acomprehensive
publicdatasetforsleepresearchers. Computermethodsandprogramsinbiomedicine,124:180–192,2016.
[34] BobKemp,AeilkoHZwinderman,BertTuk,HilbertACKamphuisen,andJosefienJLOberye.Analysisof
asleep-dependentneuronalfeedbackloop:theslow-wavemicrocontinuityoftheeeg. IEEETransactions
onBiomedicalEngineering,47(9):1185–1194,2000.
[35] DiegoAlvarez-EstevezandRoselyneRijsman. Haaglandenmedischcentrumsleepstagingdatabase.
PhysioNet,2022.
[36] SeyedYahyaShirazi,AlexandreFranco,MaurícioScopelHoffmann,NathaliaBEsper,DungTruong,
ArnaudDelorme,MichaelPMilham,andScottMakeig. Hbn-eeg:Thefairimplementationofthehealthy
brainnetwork(hbn)electroencephalographydataset. bioRxiv,pages2024–10,2024.
[37] LindsayMAlexander,JasmineEscalera,LeiAi,CharissaAndreotti,KarinaFebre,AlexanderMangone,
Natan Vega-Potler, Nicolas Langer, Alexis Alexander, Meagan Kovacs, et al. An open resource for
transdiagnosticresearchinpediatricmentalhealthandlearningdisorders. Scientificdata,4(1):1–26,2017.
[38] PatrycjaDzianokandEwaKublik.Pearl-neurodatabase:Eeg,fmri,healthandlifestyledataofmiddle-aged
peopleatriskofdementia. ScientificData,11(1):276,2024.
[39] IanDaly,NicolettaNicolaou,DuncanWilliams,FaustinaHwang,AlexisKirke,EduardoMiranda,and
SlawomirJ.Nasuto. "aneegdatasetrecordedduringaffectivemusiclistening",2024.
[40] Wei-LongZhengandBao-LiangLu.Amultimodalapproachtoestimatingvigilanceusingeegandforehead
eog. Journalofneuralengineering,14(2):026017,2017.
12

[41] Sander Koelstra, Christian Muhl, Mohammad Soleymani, Jong-Seok Lee, Ashkan Yazdani, Touradj
Ebrahimi,ThierryPun,AntonNijholt,andIoannisPatras. Deap:Adatabaseforemotionanalysis;using
physiologicalsignals. IEEEtransactionsonaffectivecomputing,3(1):18–31,2011.
[42] JingjingChen,XiaobinWang,ChenHuang,XinHu,XinkeShen,andDanZhang. Alargefiner-grained
affectivecomputingeegdataset. ScientificData,10(1):740,2023.
[43] Ruo-Nan Duan, Jia-Yi Zhu, and Bao-Liang Lu. Differential entropy feature for eeg-based emotion
classification. In20136thinternationalIEEE/EMBSconferenceonneuralengineering(NER),pages
81–84.IEEE,2013.
[44] Wei-LongZheng,WeiLiu,YifeiLu,Bao-LiangLu,andAndrzejCichocki. Emotionmeter:Amultimodal
frameworkforrecognizinghumanemotions. IEEEtransactionsoncybernetics,49(3):1110–1122,2018.
[45] WeiLiu,Jie-LinQiu,Wei-LongZheng,andBao-LiangLu. Comparingrecognitionperformanceand
robustnessofmultimodaldeeplearningmodelsformultimodalemotionrecognition. IEEETransactions
onCognitiveandDevelopmentalSystems,14(2):715–729,2021.
[46] Wei-BangJiang,Xuan-HaoLiu,Wei-LongZheng,andBao-LiangLu. Seed-vii:Amultimodaldataset
ofsixbasicemotionswithcontinuouslabelsforemotionrecognition. IEEETransactionsonAffective
Computing,2024.
[47] SyedAnasImtiazandEstherRodriguez-Villegas.Anopen-sourcetoolboxforstandardizeduseofphysionet
sleepedfexpandeddatabase. In201537thAnnualInternationalConferenceoftheIEEEEngineeringin
MedicineandBiologySociety(EMBC),pages6014–6017.IEEE,2015.
[48] ShaorunZhang,ZhiyuHe,ZiyiYe,PeijieSun,QingyaoAi,MinZhang,andYiqunLiu. Eeg-svrec:An
eegdatasetwithusermultidimensionalaffectiveengagementlabelsinshortvideorecommendation. In
Proceedingsofthe47thInternationalACMSIGIRConferenceonResearchandDevelopmentinInformation
Retrieval,pages698–708,2024.
[49] ShengruiHe,ZhongjieLi,JianwuDang,YingyiLuo,andGaoyanZhang. Cire:Achineseeegdatasetfor
decodingspeechintentionmodulatedbyprosodicemotion. ScientificData,12(1):1664,2025.
[50] XinXu,XinkeShen,XuyangChen,QingzhuZhang,SitianWang,YihanLi,ZongshengLi,DanZhang,
MingmingZhang,andQuanyingLiu. Amulti-contextemotionaleegdatasetforcross-contextemotion
decoding. ScientificData,12(1):1142,2025.
[51] Igor Zyma, Sergey Tukaev, Ivan Seleznov, Ken Kiyono, Anton Popov, Mariia Chernykh, and Olexii
Shpenkov. Electroencephalogramsduringmentalarithmetictaskperformance. Data,4(1):14,2019.
[52] Marcel F. Hinss, Emilie S. Jahanpour, Bertille Somon, et al. Open multi-session and multi-task eeg
cognitivedatasetforpassivebrain-computerinterfaceapplications. ScientificData,10:85,2023.
[53] Seong-WhanLee,Klaus-RobertMüller,andJosédelR.Millán. 2020bcicompetition,track3,2020.
[54] AlessandroTGifford,KshitijDwivedi,GemmaRoig,andRadoslawMCichy. Alargeandricheegdataset
formodelinghumanvisualobjectrecognition. NeuroImage,264:119754,2022.
[55] Benjamin Blankertz, Guido Dornhege, Matthias Krauledat, Klaus-Robert Müller, and Gabriel Curio.
Thenon-invasiveberlinbrain–computerinterface:fastacquisitionofeffectiveperformanceinuntrained
subjects. NeuroImage,37(2):539–550,2007.
[56] ClemensBrunner,RobertLeeb,GernotMüller-Putz,AloisSchlögl,andGertPfurtscheller.Bcicompetition
2008–grazdataseta. Instituteforknowledgediscovery(laboratoryofbrain-computerinterfaces),Graz
UniversityofTechnology,16(1-6):34,2008.
[57] Gerwin Schalk, Dennis J McFarland, Thilo Hinterberger, Niels Birbaumer, and Jonathan R Wolpaw.
Bci2000: ageneral-purposebrain-computerinterface(bci)system. IEEETransactionsonbiomedical
engineering,51(6):1034–1043,2004.
[58] JunMa,BanghuaYang,WenzhengQiu,YunzheLi,ShouweiGao,andXinXingXia. SHUMulti-session
Dataset. 82022.
[59] Bingchuan Liu, Xiaoshan Huang, Yijun Wang, Xiaogang Chen, and Xiaorong Gao. Beta: A large
benchmarkdatabasetowardssvep-bciapplication. Frontiersinneuroscience,14:627,2020.
[60] YijunWang,XiaogangChen,XiaorongGao,andShangkaiGao.Abenchmarkdatasetforssvep-basedbrain-
computerinterfaces. IEEETransactionsonNeuralSystemsandRehabilitationEngineering,25(10):1746–
1752,2017.
13

[61] YikeSun,YuhanLi,YuzhenChen,etal. Efficientdual-frequencyssvepbrain-computerinterfacesystem
exploitinginterocularvisualresourcedisparities. ExpertSystemswithApplications,252:124144,2024.
[62] OpenNeuro. Amultimodalneuroimagingdatasettostudyspatiotemporaldynamicsofbrainactivityand
gaitduringreal-worldwalkingwithandwithoutalower-limbexoskeleton,2025.
[63] RicardoChavarriagaandJosédelRMillán. Monitoringerror–relatedpotentials.
[64] NadideGulsahGulencandMahmutOzturk. Diagnosisofmajordepressivedisorderusingeegsignals. In
2024InnovationsinIntelligentSystemsandApplicationsConference(ASYU),pages1–6.IEEE,2024.
[65] AnnaTegon,ThorirMarIngolfsson,XiayingWang,LucaBenini,andYaweiLi. Femba: Efficientand
scalableeeganalysiswithabidirectionalmambafoundationmodel. arXivpreprintarXiv:2502.06438,
2025.
[66] Wei-BangJiang, YansenWang, Bao-LiangLu, andDongshengLi. Neurolm: Auniversalmulti-task
foundationmodelforbridgingthegapbetweenlanguageandeegsignals.arXivpreprintarXiv:2409.00101,
2024.
[67] JiquanWang,ShaZhao,ZhilingLuo,YangxuanZhou,HaitengJiang,ShijianLi,TaoLi,andGangPan.
Cbramod:Acriss-crossbrainfoundationmodelforeegdecoding. arXivpreprintarXiv:2412.07236,2024.
[68] JiquanWang,ShaZhao,ZhilingLuo,YangxuanZhou,ShijianLi,andGangPan. Eegmamba: Aneeg
foundationmodelwithmamba. NeuralNetworks,page107816,2025.
[69] WenhuiCui,WoojaeJeong,PhilippThölke,TakfarinasMedani,KarimJerbi,AnandAJoshi,andRichardM
Leahy. Neuro-gpt: Towardsafoundationmodelforeeg. In2024IEEEInternationalSymposiumon
BiomedicalImaging(ISBI),pages1–5.IEEE,2024.
[70] YassineElOuahidi,JonathanLys,PhilippThölke,NicolasFarrugia,BastienPasdeloup,VincentGripon,
KarimJerbi,andGiuliaLioi. Reve:Afoundationmodelforeeg–adaptingtoanysetupwithlarge-scale
pretrainingon25,000subjects. arXivpreprintarXiv:2510.21585,2025.
[71] Demetres Kostas, Stephane Aroca-Ouellette, and Frank Rudzicz. Bendr: Using transformers and a
contrastiveself-supervisedlearningtasktolearnfrommassiveamountsofeegdata. FrontiersinHuman
Neuroscience,15:653659,2021.
14

A Tasksanddatasets
ThissupplementarysectionprovidesacompleteinventoryofthedatasetsincludedinOmniEEG-Bench.Supple-
mentaryTable1summarizes,foreachdataset,itsassignedtaxonomyandsubtype,thenumberofsubjectsand
channels,andaconcisedescriptionofthecorrespondingclassificationobjective. Seereferencesfordetailed
informationonthedatasets.
|          | SupplementaryTable1. |     |                    | OmniEEG-Benchdatasetinventory. |                 |
| -------- | -------------------- | --- | ------------------ | ------------------------------ | --------------- |
| Tasktype | Datasets             |     | #Subjects#Channels | Sample                         | Taskdescription |
length
Type-I:Signalreliability
Artifact 1.EEGDenoiseNet[16] 1 1 2s Single-channelnoise-relatedbinaryclassification(2
| identification |     |     |     |     | classes). |
| -------------- | --- | --- | --- | --- | --------- |
Test-retest
|             | 2.Longitudinaltest-retest[17] |     | 45  | 60 2s | Cross-sessionsubjectidentification(2classesinthe |
| ----------- | ----------------------------- | --- | --- | ----- | ------------------------------------------------ |
| reliability |                               |     |     |       | currentmountedversion).                          |
Type-II:Biometricsanddisease
|            | 3.MPI-LEMON-age[18] |     | 203 | 64 1s | AgegroupclassificationderivedfromtheMPI- |
| ---------- | ------------------- | --- | --- | ----- | ---------------------------------------- |
| Biometrics |                     |     |     |       | LEMONcohort(4groupsinthecurrentmounted   |
version).
|     | 4.MPI-LEMON-gender[18] |     | 203 | 64 1s | GenderclassificationderivedfromtheMPI-LEMON |
| --- | ---------------------- | --- | --- | ----- | ------------------------------------------- |
cohort(2classes).
|     | 5.MPI-LEMON-extraversion |     | 203 | 64 1s | Extraversionclassification(2classes). |
| --- | ------------------------ | --- | --- | ----- | ------------------------------------- |
[18]
6.HFO[19] 30 18 2s High-frequencyoscillationrelatedbinaryclassification
(2classes).
Epilepsyand 7.TUAB[20] 325 23 10s Clinicalnormalvs.abnormalEEGclassification(2
| abnormalities |                 |     |     |        | classes).                                      |
| ------------- | --------------- | --- | --- | ------ | ---------------------------------------------- |
|               | 8.TUEV[21]      |     | 370 | 32 5s  | EEGeventclassification(6classes).              |
|               | 9.TUEP[20]      |     | 200 | 32 10s | Seizure-relatedbinaryclassification(2classes). |
|               | 10.TUSL[22]     |     | 38  | 32 10s | Sleep-stateclassification(3classes).           |
|               | 11.SienaEEG[23] |     | 14  | 31 10s | Seizure-relatedbinaryclassification(2classes). |
Neurodevelopmenta1l2.AdultADHD[24] 121 64 2s Healthyvs.ADHDclassification(2classes).
disorders
|     | 13.AD65 [25] |     | 88  | 19 10s | Neurodegenerativediseaseclassification(3classes). |
| --- | ------------ | --- | --- | ------ | ------------------------------------------------- |
Neurodegenerative
|           | 14.PD31 [26]    |      | 31  | 64 1s | Healthyvs.Parkinson’sdiseaseclassification(2  |
| --------- | --------------- | ---- | --- | ----- | --------------------------------------------- |
| disorders |                 |      |     |       | classes).                                     |
|           | 15.PD-Mortality | [27] | 94  | 64 2s | Mortalityvs.survivalclassification(2classes). |
16.MDD[28] 63 22 5s Healthyvs.majordepressivedisorderclassification(2
classes).
Mentaldisorders
|     | 17.TDBRAIN[29] |     | 285 | 26 2s | Psychiatricphenotypeclassification(4classesinthe |
| --- | -------------- | --- | --- | ----- | ------------------------------------------------ |
currentmountedversion).
|     | 18.Depressionresting[30] |     | 122 | 67 1s   | DepressionseveritygroupingviaBDI.            |
| --- | ------------------------ | --- | --- | ------- | -------------------------------------------- |
|     | 19.MODMA[31]             |     | 53  | 128 20s | Depression/patientvs.controlclassification(2 |
classes).
Type-III:Consciousnessandstate
Consciousness 20.Awakening[32] 21 65 10s Awakevs.sedationstateclassification(2classes).
leveldetection
|     | 21.ISRUC-SleepSubgroupI |     | 57  | 6 30s | Sleepstageclassification(5classes). |
| --- | ----------------------- | --- | --- | ----- | ----------------------------------- |
[33]
Sleepstaging 22.ISRUC-SleepSubgroupII 8 6 30s Sleepstageclassification(5classes).
[33]
|     | 23.ISRUC-SleepSubgroup |     | 10  | 6 30s | Sleepstageclassification(5classes). |
| --- | ---------------------- | --- | --- | ----- | ----------------------------------- |
III [33]
|     | 24.Sleep-EDF | [34] | 153 | 2 30s | Sleepstageclassification(5classes). |
| --- | ------------ | ---- | --- | ----- | ----------------------------------- |
|     | 25.HMC[35]   |      | 124 | 8 30s | Sleepstageclassification(5classes). |
26.HBN-EEG [36,37] 136 129 2s Multi-contexttask-typeclassification(13classesinthe
Cognitivetask
| identification |     |     |     |     | currentmountedversion). |
| -------------- | --- | --- | --- | --- | ----------------------- |
27.PEARL-Neuro [38] 79 128 1s Context/taskdiscriminationclassification(3classesin
thecurrentmountedversion).
|     | 28.RestCog | [39] | 60  | 61 1s | Task-typeclassification(5classes). |
| --- | ---------- | ---- | --- | ----- | ---------------------------------- |
Type-IV:Cognitionandemotion
Vigilancedetec- 29.SEED-VIG [40] 21 17 8s Vigilancestateclassification(3classesinthecurrent
| tion |                 |      |     |        | mountedversion).                               |
| ---- | --------------- | ---- | --- | ------ | ---------------------------------------------- |
|      | 30.DEAP-arousal | [41] | 32  | 32 10s | High/lowarousalclassification(2classes).       |
|      | 31.DEAP-valence | [41] | 32  | 32 10s | High/lowvalenceclassification(2classes).       |
|      | 32.FACED        | [42] | 123 | 32 10s | Fine-grainedemotionclassification(9classes).   |
|      | 33.SEED [43]    |      | 15  | 62 10s | Positive/negative/neutralvideo-elicitedemotion |
classification(3classes).
| Emotion | 34.SEED-IV | [44] | 15  | 62 4s | Emotionclassification(4classes). |
| ------- | ---------- | ---- | --- | ----- | -------------------------------- |
recognition 35.SEED-V [45] 16 62 1s Audio-visualelicitedemotionclassification(5classes).
36.SEED-VII [46] 20 62 10s Audio-visualelicitedemotionclassification(7classes).
15

| Tasktype | Tasks |     | #Subjects#Channels |     | Sample | Taskdescription |
| -------- | ----- | --- | ------------------ | --- | ------ | --------------- |
Length
|     | 37.SEED-FRA | [47] | 8   | 60  | 10s | EmotionclassificationwithFrenchmoviestimuli(3 |
| --- | ----------- | ---- | --- | --- | --- | --------------------------------------------- |
classes).
|     | 38.EEG-SvRec | [48] | 30  | 69  | 1s  | Affective/preferencerelatedbinaryclassification(2 |
| --- | ------------ | ---- | --- | --- | --- | ------------------------------------------------- |
classesinthecurrentmountedversion).
39.CIRE [49] 38 128 2s Speech-relatedaffectiveclassification(2classesinthe
currentmountedversion).
|     | 40.MusicEEG[39] |      | 31  | 19  | 1s  | Music-evokedemotionclassification(2classes). |
| --- | --------------- | ---- | --- | --- | --- | -------------------------------------------- |
|     | 41.EmoEEG-MC    | [50] | 53  | 64  | 5s  | Multi-contextemotionclassification.          |
Workload 42.EEGMAT [51] 36 21 5s Cognitiveworkload/task-stateclassification(2
| detection |             |      |     |     |     | classes).                              |
| --------- | ----------- | ---- | --- | --- | --- | -------------------------------------- |
|           | 43.Workload | [52] | 12  | 61  | 2s  | Workloadlevelclassification(3classes). |
Type-V:Naturalisticstimulusdecoding
Imaginedspeech 44.BCI-speech[53] 45 64 3s Speechintention/keywordclassification(5classes).
|     | 45.Broderick(cocktail |     | 33  | 69  | 2s  | Left–rightauditoryattentionclassification(2classes). |
| --- | --------------------- | --- | --- | --- | --- | ---------------------------------------------------- |
Listening
party)[11]
|     | 46.Broderick(reverse)[11] |     | 19  | 69  | 2s  | Naturalvs.time-reversedspeechclassification(2 |
| --- | ------------------------- | --- | --- | --- | --- | --------------------------------------------- |
classes).
| Reading | 47.ChineseEEG2 | [12] | 4   | 128 | 2s  | Toneclassification(4classes). |
| ------- | -------------- | ---- | --- | --- | --- | ----------------------------- |
Visual 48.Things-EEG2[54] 10 17 1s Animatevs.inanimateconceptclassification(2
classes).
Type-VI:Motorandinteraction
|     | 49.BCICompetitionIV- |     | 7   | 59  | 4s  | Motorimageryclassification(2classes). |
| --- | -------------------- | --- | --- | --- | --- | ------------------------------------- |
1[55]
Motorimagery 50.BCICompetitionIV- 9 22 4s Motorimageryclassification(4classes).
2A[56]
|     | 51.PhysioNet-MI[57] |      | 109 | 64  | 4s  | Motorimageryclassification(4classes). |
| --- | ------------------- | ---- | --- | --- | --- | ------------------------------------- |
|     | 52.SHU-MI[58]       |      | 25  | 32  | 4s  | Motorimageryclassification(2classes). |
|     | 53.BETA[59]         |      | 70  | 64  | 1s  | SSVEPtargetclassification(40classes). |
|     | 54.Benchmark-SSVEP  | [60] | 35  | 64  | 2s  | SSVEPtargetclassification(40classes). |
SSVEP
|     | 55.Dual-Freq-SSVEP[61] |     | 14  | 64  | 1s  | Dual-frequencySSVEPtargetclassification(40 |
| --- | ---------------------- | --- | --- | --- | --- | ------------------------------------------ |
classes).
|     | 56.SSVEP-9-ch[62] |     | 20  | 9   | 3s  | SSVEPtargetclassification(160classes). |
| --- | ----------------- | --- | --- | --- | --- | -------------------------------------- |
ErrPfeedback 57.MonitoringErrP[63] 6 64 1s Error-relatedpotentialclassification(2classesinthe
currentmountedversion).
Closed-loop 58.EEG-ControlledExoskele- 7 60 1s Closed-loopcontrolofwalkingandstopping(2
| assistivecontrol | ton[17] |     |     |     |     | classes). |
| ---------------- | ------- | --- | --- | --- | --- | --------- |
B Therationaleofdatawindowing
BecauseOmniEEG-Benchintegratesdatasetswithheterogeneousexperimentaldesigns,samplelengthwas
determinedatthedatasetlevelratherthanfixedglobally.Whenadatasetorclinicalconventiondefinesastandard
epoch, we follow that convention. Sleep-staging datasets are segmented into 30-s epochs, consistent with
standardsleep-scoringpracticeandtheannotationsusedinISRUC-SleepandSleep-EDF.EEGDenoiseNetis
keptatitsnative2-ssegmentlength.Formotorimagerydatasets,weusethetask-relevantimageryintervalwhen
available,suchasthe4-scueorimageryperiodinBCICompetitionIVdatasets.
Fordatasetswithlongercontinuousrecordingsbutnosinglecanonicaltriallength,wechoosewindowsaccording
tothedominanttemporalscaleofthedownstreamtask.Resting-stateandclinical-statedatasetsaresegmented
intowindowslongenoughtocapturestablespectralorstate-levelfeatureswhileremainingapproximately
stationary.Forexample,MODMAuseslongerwindows(20s)followingpriordepression-classificationpractice
withlongresting-statesegments[64]. Fornaturalisticlanguageandspeechdatasets,suchasChineseEEG2
andBroderick,thewindowlength(2s)isdesignedtoretainlocallinguisticorprosodiccontextwhileavoiding
excessivemixingacrossadjacentwords,sentences,orstimulusevents.ForSSVEPandclosed-loopBCItasks,
weuseshortwindowstoemphasizelow-latencydecoding.
Allsegmentationchoicesarefixedbeforemodelevaluationandareappliedidenticallytoallmodelswithineach
dataset.
C BenchmarkedEEGfoundationmodels
WeselectedEEG-FMstoprovidearepresentativeandreproduciblecoverageofcurrentfoundation-modeldesigns
forEEG.Modelswereincludediftheyprovideaccessiblepretrainedweightsorreproducibleimplementations,
are intended for general-purpose or cross-dataset EEG representation learning, and can be adapted to the
unifiedOmniEEG-Benchevaluationinterface.Theselectedmodelsspanseveralmajormethodologicalfamilies:
Transformer-basedmaskedmodeling,state-spaceorMamba-basedsequencemodeling,contrastivebiosignal
representationlearning,andmulti-taskortask-alignedpretraining.Theyalsodiffersubstantiallyinpretraining
16

scale,datadiversity,inputmodality,channel-processingstrategy,andmodelsize.ThisdiversityallowsOmniEEG-
Benchtoevaluatenotonlywhichmodelperformsbest,butalsowhichdesignfactorsareassociatedwithstronger
transferacrossheterogeneousEEGtasks. SupplementaryTable2summarizescharacteristicsofEEG-FMs
includedinOmniEEG-Bench.Becausepapersoftendifferinhowtheyreportdatavolumeandparametercounts
(e.g.,multiplemodelsizesorpartiallyreportedhours),wekeepthetablefaithfultotheoriginaldisclosuresand
markunreportedfieldsaccordingly. Theunderlinedparametersizeisthatofthe"base"modelandisusedin
ourbenchmark.Toquantifythedatadiversityusedinthepre-trainingofeachmodelandexcludethetraining
datasetsfromevaluation,welistthepre-trainingdatasetsforeachmodelinSupplementaryTable3.Toensure
reproducibility,wesummarizetheimplementationdetailsofeachmodelinSupplementaryTable4,including
thetargetsamplingrate,inputshape,channelinputpolicy,andnormalizationstrategy.Notably,modelsdiffer
substantiallyinhowtheyhandlechannelconfigurations:someacceptarbitrarylayoutsviaadaptiveencoding
(CBraMod)orcoordinate-basedmapping(BrainOmni),whileothersrequirefixedmontagessuchasthe10–20
system(LaBraM,NeuroLM)orpredefinedbipolarderivations(FEMBA,Neuro-GPT,BIOT).
D ValidityoftheDownsampledEvaluationProtocol
Tojustifytheuseofadownsampledevaluationprotocolinlinearprobing,weprovidetwocomplementary
analyses.Wefirstdetermineanappropriatenumberoftrainingsamplesperclassbyexamininghowperformance
anditsvarianceevolvewithincreasingsamplesize.AsshowninSupplementaryFig.1,performancestabilizes
beyond approximately 40 samples per class, after which variance across repeated subsampling runs also
diminishes. Thissupportsthechoiceof40samplespersubjectperclassasareliableoperatingpoint. We
thenverifythatthisdownsampledprotocolpreservestherelativerankingofmodelscomparedtousingthefull
dataset,asshowninSupplementaryFig. 2. Modelrankingsunderbothprotocolsremainlargelyconsistent
acrosstaskcategoriesandevaluationsettings,confirmingthatdownsamplingdoesnotintroducesystematicbias
incomparativeevaluation.
target number target number
SupplementaryFig. 1. Modelperformanceasafunctionofthenumberoftrainingsamplesperclass
underthedownsampledlinearprobingsetting,shownfortworepresentativedatasets(ISRUC-S1and
HMC).Errorbarsdenotestandarddeviationacross15randomsubsamplingruns.
E FullFine-tuningResults
Wereportfullfine-tuningresultsunderthecross-subjectsettinginSupplementaryFig.4.Notethattheseresults
areobtainedunderthesamedownsampledevaluationprotocol(40samplespersubjectperclass)asdescribedin
SupplementarySectionD.Comparedtolinearprobing,modelrankingsshiftsubstantiallyunderfullfine-tuning,
withLaBraM,NeuroLM,andFEMBAachievingthetopthreeoverallranks.Notably,EEGConformer,included
asatask-specificbaseline,rankscompetitivelyamongfoundationmodels,highlightingthebenefitofend-to-end
optimizationfortask-specificadaptation.
F Multi-subjectadaptation
Inthelinearprobingsettingformulti-subjectadaptation,CBraMod,REVE,andBrainOmniachievethetop
threeoverallrankswithaverageranksof2.76,3.25,and4.36,respectively(Fig.11;seeSupplementaryTable6
fordetailedaccuracy).Themodelrankingisbroadlyconsistentwiththatobservedinthecross-subjectsetting—
whereBrainOmni,CBraMod,andREVEalsooccupiedthetopthreepositions—withonlyminorreordering,
suggestingthatstrongerpretrainedrepresentationstendtoperformwellunderbothcross-trialadaptationand
cross-subjecttransfer. Severaltasksremaindifficultinthemulti-subjectsetting. Eightmodelsperformnear
17

SupplementaryFig. 2. Rankconsistencybetweenfull-sampleanddownsampledevaluationsettings.
Top:Scatterplotscomparingmodelranksundercross-subject(left)andmulti-subject(right)protocols,
whereeachpointencodesamodel(shape)andtaskcategory(color). Bottom: Overallmodelranking
curvesundercross-subject(left)andmulti-subject(right)protocols;thebluesolidlineandshaded
banddenotethemeanandmin–maxrangeacrossthreeseedsunderthedownsampledsetting,andthe
reddashedlinedenotesthefull-samplerank.
chanceonChinesetoneclassification(ChineseEEG2-RA-Tone),andsevenmodelsperformnearchanceon
workloadclassification(Workload),indicatingthatcurrentEEGfoundationmodelsstillhavelimitedcross-trial
discriminabilityforthesetasks.
18

SupplementaryFig. 3. Fullfine-tuningresultsunderthecross-subjectsetting. Top: Averagerank
across all datasets for each model. Bottom: Per-dataset rank heatmap; lower rank (darker color)
indicatesbetterperformance. “PT”denotesthatthedatasetwasusedinthemodel’spretrainingandis
excludedfromranking.
19

SupplementaryFig. 4. Multi-subjecttransferranksoftenEEGfoundationmodelsusingOmniEEG-
Bench.
20

G ComparisonbetweenFullFine-tuningandLinearProbing
Wecomparemodelperformanceunderfullfine-tuningandlinearprobinginSupplementaryFig.5.Task-specific
baselines(EEGConformerandEEGNet,highlightedinblue)areincludedforreference.
Underfullfine-tuning,themajorityoffoundationmodelsoutperformbothtask-specificbaselines,suggesting
thatpretrainedrepresentationscanbeeffectivelyadaptedthroughend-to-endoptimization.Incontrast,under
linearprobing,theadvantageoffoundationmodelsdiminishessignificantly.Manyfoundationmodelsfailto
matchorsurpassthetask-specificbaselineEEGConformer(averagerankof6.66),withonlyfivetop-performing
modelsoutperformingit.Thisclearperformancedropindicatesthatwhilesomeadvancedmodelsshowpromise,
manycurrentEEGfoundationmodelsstillstruggletoprovidesufficientlystrongfrozenrepresentationsthat
transferacrossheterogeneousdatasetswithouttask-specificadaptation.
Full fine tuning
Linear probing
j
SupplementaryFig. 5. Modelranksinfullfinetuningandlinearprobing.
H Averagemodelranksoneachtasktaxonomy
SupplementaryFig. 6summarizestheaveragerankofeachmodelacrossdifferenttaskfamiliesunderboth
evaluationprotocols(wherepointsclosertotheouteredgeindicatebetterranks).
Undermulti-subjectadaptation(left),CBraModandREVEexhibitthemostconsistentlystrongperformance,
formingtheoutermostboundariesoftheradarchart.Specifically,CBraModdemonstratesexceptionalstrength
inmotor&interactionandcognition&emotiontasks,whileREVEexcelsinsignalreliabilityandnaturalistic
stimulusdecoding.
Under cross-subject transfer (right), the performance landscape shifts, revealing distinct category-specific
strengths.BrainOmniemergesashighlycompetitive,achievingtopranksinmotor&interactionandnaturalistic
stimulusdecoding. Othermodelsalsodisplaytargetedadvantages: BIOTnotablyspikestothetoprankin
biometrics&disease,REVEmaintainsdominanceinconsciousness&state,andCBraModremainsastrong
contenderincognition&emotion.
Notably,nosinglemodeldominatesuniformlyacrossalltaskaxesineithersetting.Thevaryingshapesofthe
radarwebsemphasizethatdifferentmodelarchitecturescapturecomplementaryaspectsofEEGrepreseantations,
andtheirrelativeadvantagesdependheavilyonthespecificcharacteristicsofthedownstreamtask.
21

Signal Reliability Biometrics & Disease
| Motor &               | Consciousness &     | Motor &                | Consciousness &     |
| --------------------- | ------------------- | ---------------------- | ------------------- |
| Interaction           | State               | Interaction            | State               |
| Naturalistic Stimulus |                     | Naturalistic Stimulus  |                     |
|  Decoding             | Cognition & Emotion | Decoding               | Cognition & Emotion |
Multi-Subject Cross-Subject
SupplementaryFig. 6. Averagemodelranksoneachtasktaxonomy. Left: multi-subjectadaptation;
Right: cross-subjecttransfer.
22

SupplementaryTable2. Summaryof10EEGfoundationmodelsincludedinthebenchmark.
#Training
| Model |     |     | #Params1 Input | Pre-training | Backbone | Channel |
| ----- | --- | --- | -------------- | ------------ | -------- | ------- |
subj.
|     |     | Trainingdata |     | paradigm |     | processing |
| --- | --- | ------------ | --- | -------- | --- | ---------- |
(h)
BrainOmni[6] 6550 1,997(EEG)+ 8.4M, EEG/MEGMasked Criss-Cross SensorEncoder
|     |     | 656(MEG) | 37.7M | reconstruction | Transformer |     |
| --- | --- | -------- | ----- | -------------- | ----------- | --- |
(temporal)
| FEMBA[65] | 14,987 | 27,062 | 7.8M, EEG | Masked         | Mamba | fixedchannel |
| --------- | ------ | ------ | --------- | -------------- | ----- | ------------ |
|           |        |        | 16.1M,    | reconstruction |       | (10/20)      |
|           |        |        | 77.8M,    | (temporal)     |       |              |
389M
NeuroLM[66] 15,444 27,762 255.1M, EEG Multi-task/ Transformer Unifiedchannel
|     |     |     | 500M, | autoregressive |     | vocabulary    |
| --- | --- | --- | ----- | -------------- | --- | ------------- |
|     |     |     | 1.69B |                |     | (10–20-based) |
CBraMod[67] 14,987 27,062 5.0M EEG Masked Criss-Cross Asymmetric
|     |     |     |     | reconstruction | Transformer | Conditional |
| --- | --- | --- | --- | -------------- | ----------- | ----------- |
|     |     |     |     | (temporal)     |             | Positional  |
Encoding
EEGMamba[68]Unreported 16,724 3.3M EEG Masked Mamba ST-Adaptive
|     |     |     |     | reconstruction |     | Module |
| --- | --- | --- | --- | -------------- | --- | ------ |
(temporal)
LaBraM[5] Unreported 2534.78 5.8M EEG Masked Transformer Unifiedchannel
|         |        |        |           | reconstruction |       | vocabulary    |
| ------- | ------ | ------ | --------- | -------------- | ----- | ------------- |
|         |        |        |           | (frequency)    |       | (10–20-based) |
| Neuro-  | 14,987 | 27,062 | 78.4M EEG | Masked         | GPT-2 | fixedchannel  |
| GPT[69] |        |        |           | reconstruction |       | (10/20)       |
(temporal)
REVE[70] 24,274 61,415 69.2M EEG Masked Transformer Unifiedchannel
|     |     |     |     | Autoencoder |     | embedding |
| --- | --- | --- | --- | ----------- | --- | --------- |
BIOT[4] Unreported Unreported 3.2M EEG/ECGContrastive Linear fixedchannel
|     |     |     |     | learning | Transformer | (18-channel |
| --- | --- | --- | --- | -------- | ----------- | ----------- |
bipolar
montage)
BENDR[71] 14,987 27,062 4.0M EEG Contrastive Transformer fixedchannel
|     |     |     |     | predictive |     | (10/20) |
| --- | --- | --- | --- | ---------- | --- | ------- |
coding
I Datapreprocessing
AsEEGsignalsareinherentlynoisyandcomplex,rigorousdatapreprocessingiscriticaltoenhancesignal
qualityandmitigateartifacts.Toensureconsistencyacrossheterogeneousdatasetsandfacilitateefficienttraining
offoundationmodels,wedevelopedaunifiedHDF5-basedbenchmarkinginfrastructure. Thestandardized
pipelineincludesfiltering,resampling,segmentation,andhierarchicalstorage.
Band-passandnotchfiltering.
EEGsignalsspanawidefrequencyrange,butonlyspecificbandsare
relevanttocognitiveandemotionaldecodingtasks. Weemployastandard0.1–75Hzband-passfilterusing
MNE-Python,preservingcrucialtask-relevantfrequencycomponents(fromδtoγbands)whilesuppressing
low-frequencydriftsandhigh-frequencynoise.Inaddition,anotchfilterisdynamicallyconfigured(typically60
Hzor50Hz)basedonthedatacollectionenvironment,effectivelyattenuatingmainshum.The0.1–75band-pass
filterisemployedintheoriginalimplementationofamajorityofEEGfoundationmodels.
23

SupplementaryTable3. Pre-trainingdatasetsofthefoundationmodels.
Model Pre-trainingDataset(s)
BrainOmni EEG:Go-Nogo,MusicEEG,HFO,SRM,RestCog,HBNEO/EC,Features-EEG,
PEARL-Neuro,HBN-EEG,Awakening
MEG:MEG-MASC,MEG-Narrative-Dataset,OMEGA,CC700,AversiveMEG,MIND,
SMN4Lang,THINGS-MEG,ASWR-MEG,ImageLine,NeuroMorph,Kymata-SOTO.
Totalnumber:22
FEMBA TUEG.Totalnumber:1
NeuroLM TUEG,SEED-IV,SEED-V,SEED-GER,SEED-FRA,BCICompetitionIV-1,Emobrain,
GraspandLift,InriaBCI,MotorMovement/Imagery,RawEEGData,RestingState,Siena
ScalpEEGDatabase,SPISRestingState,TargetVersusNon-Target,Self-collectedEEG
corpus.Totalnumber:16
CBraMod TUEG.Totalnumber:1
EEGMamba TUEG(cleansubset),PhysioNet2018,RawEEGData,SienaScalpEEGDatabase,B-
SNIP1(cleansubset).Totalnumber:5
LaBraM BCICompetitionIV-1,Emobrain,GraspandLiftEEGChallenge,InriaBCIChallenge,
EEGMotorMovement/ImageryDataset,RawEEGData,RestingStateEEGData,SEED,
SEED-IV,SEED-GER,SEED-FRA,SienaScalpEEGDatabase,SPISRestingStateDataset,
TargetVersusNon-Target,TUAR,TUEP,TUSZ,TUSL,Self-collectedEEGData
Totalnumber:19
Neuro-GPT TUEG.Totalnumber:1
REVE TUH,Physionet,OpenNeuro(),MOABB.Totalnumber:92
BIOT EEG:SHHS,PREST
ECG:Cardiology
Totalnumber:3
BENDR TUEG.Totalnumber:1
Resampling. RawEEGrecordingsfromdifferentdatasetsaretypicallyacquiredatvaryingsamplingrates
(rangingfrom128Hzto1000Hz).WeresampletheEEGsignalsaccordingtotherequirementofeachfoundation
model(250HzforNeuro-GPT,256HzforBrainOmniandBENDR,and200Hzforothers,Supplementary
Table4).
Windowingandsegmentation. Thedataaresegmentedtogeneratefixed-lengthinputsforthemodel.We
employaslidingwindowstrategywithadataset-specificwindowrangingfrom1sto30s(non-overlapping).See
SupplementaryTable1fordetails.
Unifieddatastorage. Toresolvethedisparityinrawdataformats(e.g.,.mat,.edf),allpreprocesseddata
areorganizedintoastandardizedHDF5schema.Therootlevelstoressubject-specificattributes(e.g.,montage,
samplingrate),trialgroupsorganizerecordingsessions,andsegmentgroupscontaintheactualpreprocessed
EEGmatricesandsynchronizedlabels,minimizingI/Olatencywhilesupportingflexibledatasplittingstrategies
duringtraining.Thedataaresplitintotrain/val/testsetsseparately.
J Detailedresults
We report the means and standard deviations of balanced accuracy across three runs for linear probing of
cross-subjecttransferandmulti-subjectadaptationinSupplementaryTables5and6,respectively.Thecross-
subject full-finetuning results are reported in Supplementary Table 7. In each table, bold entries indicate
thebest-performingmodelperdataset,underlinedentriesindicatethesecondbest,anditalicentriesindicate
performancebelowthechancelevel.“–”indicatesthatthemodelisincompatiblewiththedatasetduetochannel
configurationconstraints.
24

SupplementaryTable4. Implementationdetailsofthe10EEGfoundationmodelsincludedinthe
benchmark.
|           | Target | Bandpass   |                     |               | Sequence |
| --------- | ------ | ---------- | ------------------- | ------------- | -------- |
| Model     |        |            | ChannelPolicy       | Normalization |          |
|           | SR(Hz) | Filter(Hz) |                     |               | Length   |
| BrainOmni | 256    | 0.1–96     | Mapsinputchannelsto | Z-score       | Any      |
standardelectrodepositions
via3Dcoordinates
FEMBA 200 0.1–75 Interpolatesto22-channel IQRnormalization 1280pts
TUEGbipolarmontagevia
SSI
NeuroLM 200 0.1–75 Retainschannelsmatching ÷100(µVto 200pts/patch
|     |     |     | the10–20system | 0.1mV) |     |
| --- | --- | --- | -------------- | ------ | --- |
vocabulary
CBraMod 200 0.3–75 Acceptsarbitrarychannel ÷100(µVto 200pts/patch
|     |     |     | configurationsviaACPE | 0.1mV) |     |
| --- | --- | --- | --------------------- | ------ | --- |
adaptivepositional
encoding
| EEGMamba | 200 | 0.1–50 | Reordersto19-channel | Identity | 6000pts |
| -------- | --- | ------ | -------------------- | -------- | ------- |
standardlayout;missing
channelszero-padded
LaBraM 200 0.1–75 Mapschannelsvia10–20 ÷100(µVto 200pts/patch
|     |     |     | systemvocabulary;requires | 0.1mV) |     |
| --- | --- | --- | ------------------------- | ------ | --- |
channelIDasinput
Neuro-GPT 250 0.5–100 Interpolatesto22-channel Z-score 500pts/chunk
standardmontageviaSSI
| REVE | 256 | 0.5–99.5 | Mapschannelsviaunified | Z-score | Any |
| ---- | --- | -------- | ---------------------- | ------- | --- |
channelembedding;accepts
variableconfigurations
| BIOT | 200 | –   | Constructs18-channel     | P95absolute | Any |
| ---- | --- | --- | ------------------------ | ----------- | --- |
|      |     |     | bipolarmontage(BIOT-18); | scaling     |     |
missingchannels
zero-padded
| BENDR | 256 | 0.1–100 | Mapsto19standard | Identity(internal | Any |
| ----- | --- | ------- | ---------------- | ----------------- | --- |
|       |     |         | channelsplusone  | min-max)          |     |
relative-amplitudeauxiliary
channel
25

SupplementaryTable5. Cross-subjecttransferresults(balancedaccuracy,mean±stdover3runs).
Dataset #Classes BrainOmni CBraMod REVE FEMBA BIOT LaBraM NeuroLM NeuroGPT EEGMamba BENDR
Type-I
Longitudinaltest-retest 2 0.755±0.006 0.743±0.020 0.725±0.025 0.683±0.038 0.677±0.005 0.745±0.018 0.703±0.005 0.695±0.022 0.639±0.014 0.500±0.000
Type-II
MPI-LEMON-age 4 0.479±0.018 0.462±0.048 0.498±0.030 0.480±0.025 0.477±0.033 0.439±0.048 0.403±0.052 0.426±0.046 0.332±0.001 0.333±0.000
MPI-LEMON-gender 2 0.532±0.020 0.644±0.048 0.599±0.030 0.569±0.058 0.587±0.060 0.571±0.073 0.553±0.052 0.545±0.055 0.499±0.001 0.500±0.000
MPI-LEMON-extraversion 2 0.536±0.013 0.481±0.017 0.505±0.026 0.490±0.012 0.463±0.013 0.509±0.039 0.518±0.026 0.464±0.026 0.504±0.005 0.500±0.000
HFO 2 – 0.563±0.026 0.608±0.016 0.525±0.011 0.586±0.029 0.541±0.015 0.537±0.009 0.544±0.010 0.580±0.022 0.500±0.000
TUAB 2 0.727±0.034 – – – 0.793±0.006 0.732±0.009 – – – –
TUEV 6 0.467±0.034 – – – 0.683±0.075 0.417±0.056 – – – –
TUEP 2 0.596±0.053 – – – 0.588±0.031 – – – – –
TUSL 3 0.450±0.051 – – – 0.645±0.055 – – – – –
SienaEEG 2 0.694±0.086 0.755±0.171 0.419±0.178 0.439±0.206 0.691±0.080 – – 0.479±0.106 – 0.333±0.236
ADHD 2 0.627±0.076 0.666±0.077 0.626±0.059 0.602±0.018 0.535±0.035 0.580±0.084 0.662±0.057 0.673±0.110 0.552±0.082 0.500±0.000
AD65 3 0.462±0.111 0.582±0.130 0.527±0.153 0.470±0.056 0.491±0.089 0.457±0.081 0.339±0.025 0.410±0.071 0.390±0.060 0.333±0.000
PD31 2 0.406±0.128 0.369±0.167 0.459±0.076 0.511±0.140 0.544±0.129 0.280±0.062 0.414±0.126 0.323±0.135 0.336±0.136 0.333±0.236
PD-motaility 2 0.501±0.003 0.530±0.016 0.568±0.045 0.500±0.010 0.623±0.049 0.516±0.017 0.560±0.075 0.530±0.046 0.501±0.003 0.500±0.000
MDD 2 0.993±0.008 0.826±0.121 0.948±0.063 0.742±0.058 0.861±0.075 0.743±0.133 0.883±0.090 0.640±0.055 0.701±0.045 0.500±0.000
TDBRAIN 4 0.413±0.007 0.446±0.023 0.437±0.019 0.396±0.018 0.393±0.030 0.391±0.027 0.413±0.006 0.362±0.008 0.323±0.021 0.278±0.039
Depression-resting 2 0.501±0.001 0.509±0.009 0.511±0.000 0.522±0.017 0.505±0.006 0.500±0.000 0.503±0.002 0.503±0.003 0.499±0.001 0.500±0.000
MODMA 2 0.657±0.152 0.500±0.000 0.572±0.076 0.773±0.072 0.500±0.000 0.500±0.000 – 0.544±0.000 0.610±0.000 0.500±0.000
Type-III
Awakening 2 – 0.890±0.046 0.962±0.026 0.961±0.026 0.973±0.019 0.934±0.041 0.811±0.023 0.781±0.089 0.833±0.024 0.500±0.000
ISRUC-S1 5 0.615±0.021 0.570±0.030 0.658±0.018 0.586±0.010 0.557±0.017 0.558±0.032 0.562±0.084 0.549±0.026 0.501±0.046 0.200±0.000
ISRUC-S2 5 0.282±0.010 0.206±0.006 0.249±0.023 0.242±0.016 0.250±0.014 0.189±0.012 0.207±0.008 0.266±0.011 0.197±0.007 0.200±0.000
ISRUC-S3 5 0.345±0.014 0.319±0.021 0.374±0.025 0.321±0.010 0.345±0.033 0.304±0.008 0.298±0.002 0.289±0.030 0.306±0.010 0.200±0.000
SleepEDF 5 0.667±0.019 0.690±0.016 0.681±0.009 0.625±0.014 0.200±0.000 0.693±0.008 0.685±0.015 0.638±0.018 0.526±0.010 0.200±0.000
HMC 5 0.664±0.017 0.658±0.005 0.682±0.017 0.611±0.012 0.569±0.018 0.630±0.011 0.615±0.021 0.572±0.020 0.551±0.014 0.200±0.000
HBNEEG 13 – 0.136±0.007 0.158±0.004 0.118±0.006 0.133±0.012 0.114±0.007 0.090±0.004 0.103±0.004 0.100±0.003 0.077±0.000
PEARL-Neuro 3 – 0.535±0.006 0.484±0.014 0.465±0.005 0.462±0.012 0.478±0.017 0.438±0.013 0.437±0.012 0.419±0.008 0.333±0.000
RestCog 5 – 0.368±0.029 0.346±0.027 0.308±0.024 0.350±0.025 0.318±0.023 0.309±0.024 0.276±0.017 0.229±0.006 0.200±0.000
Type-IV
SEED-VIG 3 0.432±0.014 0.440±0.035 0.418±0.064 0.414±0.026 0.333±0.000 0.437±0.025 0.360±0.028 0.432±0.028 0.350±0.059 0.333±0.000
DEAP-arousal 2 0.505±0.024 0.515±0.021 0.508±0.029 0.503±0.005 0.484±0.031 0.478±0.007 0.500±0.017 0.510±0.011 0.487±0.025 0.500±0.000
DEAP-valence 2 0.530±0.011 0.519±0.020 0.521±0.008 0.517±0.020 0.498±0.049 0.507±0.033 0.500±0.014 0.494±0.023 0.533±0.005 0.500±0.000
SEED 3 0.492±0.013 0.525±0.027 0.543±0.010 0.434±0.008 0.430±0.015 – 0.399±0.015 0.466±0.035 0.471±0.012 0.333±0.000
SEED-IV 4 0.316±0.017 0.334±0.005 0.297±0.013 0.303±0.009 0.259±0.029 – – 0.292±0.006 0.288±0.008 0.250±0.000
SEED-V 5 0.235±0.003 0.234±0.008 0.257±0.007 0.290±0.006 0.257±0.010 0.241±0.010 – 0.242±0.011 0.204±0.006 0.200±0.000
SEED-VII 7 0.185±0.008 0.176±0.009 0.191±0.006 0.189±0.015 0.159±0.006 0.187±0.018 0.161±0.005 0.176±0.008 0.181±0.013 0.143±0.000
SEED-FRA 3 0.425±0.011 0.417±0.013 0.353±0.006 0.398±0.023 0.385±0.013 – – 0.366±0.014 0.409±0.003 0.333±0.000
EEG-SVRec 2 0.511±0.003 0.508±0.012 0.499±0.002 0.506±0.002 0.503±0.003 0.510±0.005 0.501±0.009 0.500±0.004 0.504±0.005 0.500±0.000
FACED 9 0.204±0.002 0.481±0.034 0.203±0.016 0.174±0.014 0.156±0.006 0.155±0.020 0.170±0.022 0.146±0.004 0.151±0.011 0.111±0.000
MusicEEG 2 – 0.591±0.012 0.528±0.059 0.486±0.023 0.475±0.014 0.524±0.032 0.519±0.031 0.480±0.039 0.528±0.045 0.500±0.000
EmoEEG-MC 10 0.322±0.015 0.340±0.017 0.305±0.035 0.326±0.010 0.332±0.017 0.340±0.017 0.327±0.009 0.328±0.013 0.346±0.020 0.333±0.000
CIRE 2 0.531±0.017 0.526±0.018 0.538±0.017 0.532±0.029 0.513±0.012 0.535±0.025 0.523±0.022 0.524±0.036 0.528±0.021 0.500±0.000
EEGMAT 2 0.485±0.022 0.500±0.000 0.499±0.013 0.602±0.021 0.549±0.079 0.495±0.007 0.616±0.082 0.522±0.035 0.503±0.004 0.498±0.002
Workload 3 0.444±0.007 0.470±0.042 0.409±0.046 0.411±0.016 0.466±0.009 0.478±0.028 0.496±0.019 0.358±0.023 0.406±0.022 0.333±0.000
Type-V
BCI-Speech 5 0.225±0.010 0.289±0.033 0.223±0.009 0.210±0.013 0.204±0.014 0.203±0.011 0.211±0.004 0.212±0.008 0.197±0.012 0.200±0.000
Broderick-Cocktail-party 2 0.516±0.004 0.384±0.052 0.399±0.068 0.358±0.039 0.346±0.085 0.465±0.042 0.443±0.061 0.336±0.229 0.425±0.092 0.333±0.236
Broderick-reverse 2 0.466±0.046 0.580±0.049 0.710±0.138 0.499±0.001 0.481±0.026 0.464±0.052 0.492±0.058 0.465±0.049 0.500±0.000 0.500±0.000
ChineseEEG2-RA-Tone 4 0.252±0.002 0.253±0.004 0.250±0.005 0.250±0.001 0.253±0.002 0.250±0.003 0.252±0.001 0.250±0.004 0.252±0.001 0.250±0.000
ThingsEEG2 2 0.504±0.001 0.500±0.000 0.500±0.000 0.500±0.000 0.500±0.000 0.500±0.000 0.500±0.000 0.502±0.002 0.500±0.000 0.500±0.000
Type-VI
BCIC-IV-2a 4 0.303±0.028 0.329±0.006 0.298±0.009 0.256±0.002 0.250±0.000 – – 0.283±0.016 0.289±0.009 0.250±0.000
BCIC-IV-1 2 0.510±0.011 0.552±0.031 0.525±0.035 0.507±0.005 0.505±0.004 0.513±0.008 0.503±0.015 0.463±0.009 0.508±0.010 0.500±0.000
Physionet-MI 4 0.307±0.011 0.499±0.007 – 0.293±0.007 0.256±0.008 0.280±0.011 0.312±0.016 0.305±0.016 – 0.250±0.000
SHU-MI 2 0.533±0.018 0.515±0.009 0.523±0.003 0.511±0.002 0.519±0.014 0.507±0.011 0.504±0.012 0.504±0.002 0.490±0.012 0.500±0.000
BETA-SSVEP 40 0.037±0.004 0.103±0.014 0.043±0.006 0.040±0.007 0.031±0.004 0.032±0.004 0.033±0.004 0.030±0.005 0.028±0.008 0.025±0.000
Benchmark-SSVEP 40 0.078±0.021 0.425±0.103 0.056±0.008 0.051±0.009 0.065±0.019 0.033±0.003 0.032±0.002 0.026±0.005 0.033±0.006 0.025±0.000
Dual-Freq-SSVEP 40 0.050±0.004 0.079±0.006 0.035±0.005 0.030±0.003 0.023±0.006 0.028±0.003 0.027±0.005 0.033±0.008 0.032±0.003 0.025±0.000
SSVEP-9-chn 160 0.016±0.006 0.029±0.002 0.032±0.001 0.008±0.002 0.006±0.000 0.007±0.001 0.013±0.004 0.009±0.002 0.011±0.002 0.006±0.000
Monitoring-Errp 2 0.532±0.022 0.498±0.008 0.497±0.006 0.493±0.014 0.498±0.002 0.518±0.014 0.487±0.004 0.482±0.014 0.510±0.014 0.500±0.000
EEG-ControlledExoskeleton 2 0.523±0.001 0.513±0.021 0.509±0.016 0.502±0.009 0.488±0.057 0.492±0.016 0.518±0.028 0.522±0.023 0.491±0.017 0.500±0.000
K RegressionTasks
WeevaluateonSEED-VIG,avigilanceestimationdatasetcontaining20,355EEGsegmentsfrom21subjects,
where the label is a per-segment continuous value (ratio of eye closure, range [0.02,1.00]). As shown in
Table11,mostmodelsyieldnear-zeroornegativeR2withhighvarianceacrossseeds,indicatingthatfrozen
EEGrepresentationsgeneralizepoorlytocross-subjectpredictionwithcontinuouslabels.
26

SupplementaryTable6. Multi-subjectadaptationresults(balancedaccuracy,mean±stdover3runs).
Dataset #Classes CBraMod REVE BrainOmni FEMBA LaBraM NeuroLM BIOT NeuroGPT EEGMamba BENDR
Type-I
Longitudinaltest-retest 2 0.755±0.006 0.743±0.020 0.725±0.025 0.683±0.038 0.677±0.005 0.745±0.018 0.703±0.005 0.695±0.022 0.639±0.014 0.500±0.000
Type-III
Awakening 2 0.888±0.049 0.976±0.008 – 0.927±0.025 0.854±0.077 0.823±0.086 0.964±0.005 0.776±0.067 0.707±0.066 0.500±0.000
HMC 5 0.664±0.003 0.684±0.005 0.657±0.001 0.588±0.005 0.643±0.005 0.620±0.004 0.575±0.001 0.575±0.006 0.570±0.001 0.200±0.000
HBNEEG 13 0.087±0.004 0.138±0.006 – 0.108±0.009 0.117±0.006 0.088±0.003 0.120±0.005 0.097±0.006 0.108±0.006 0.079±0.003
RestCog 5 0.413±0.001 0.362±0.004 – 0.321±0.001 0.339±0.002 0.334±0.002 0.367±0.002 0.293±0.001 0.234±0.003 0.200±0.000
Type-IV
DEAP-arousal 2 0.513±0.004 0.514±0.009 0.502±0.017 0.484±0.009 0.495±0.010 0.512±0.010 0.511±0.020 0.505±0.006 0.483±0.005 0.500±0.000
DEAP-valence 2 0.516±0.016 0.524±0.014 0.505±0.013 0.531±0.004 0.506±0.007 0.504±0.003 0.524±0.004 0.504±0.021 0.509±0.009 0.500±0.000
SEED 3 0.546±0.055 0.576±0.070 0.518±0.102 0.457±0.129 – 0.438±0.041 0.474±0.090 0.433±0.039 0.420±0.070 0.333±0.000
SEED-IV 4 0.341±0.014 0.340±0.023 0.305±0.013 0.300±0.020 – – 0.303±0.006 0.287±0.002 0.278±0.005 0.250±0.000
SEED-V 5 0.263±0.032 0.251±0.029 0.243±0.018 0.229±0.007 0.211±0.033 – 0.216±0.005 0.219±0.021 0.214±0.013 0.200±0.000
SEED-VII 7 0.191±0.008 0.212±0.021 0.210±0.008 0.194±0.006 0.191±0.009 0.154±0.019 0.164±0.006 0.185±0.017 0.175±0.011 0.143±0.000
SEED-FRA 3 0.441±0.004 0.350±0.012 0.422±0.009 0.421±0.028 – – 0.440±0.007 0.372±0.016 0.376±0.001 0.333±0.000
FACED 9 0.484±0.023 0.197±0.010 0.194±0.018 0.170±0.004 0.145±0.006 0.171±0.016 0.147±0.009 0.151±0.004 0.144±0.004 0.111±0.000
MusicEEG 2 0.480±0.034 0.468±0.019 – 0.458±0.024 0.465±0.015 0.470±0.020 0.462±0.022 0.453±0.039 0.490±0.010 0.500±0.000
CIRE 2 0.545±0.014 0.535±0.028 0.554±0.021 0.553±0.018 0.509±0.056 0.518±0.019 0.537±0.034 0.549±0.025 0.519±0.064 0.500±0.000
Workload 3 0.315±0.032 0.242±0.081 0.313±0.029 0.318±0.022 0.335±0.002 0.356±0.024 0.297±0.053 0.259±0.073 0.334±0.002 0.333±0.000
Type-V
BCI-Speech 5 0.321±0.011 0.225±0.013 0.198±0.022 0.214±0.014 0.229±0.011 0.226±0.005 0.213±0.007 0.210±0.003 0.219±0.010 0.200±0.000
Broderick-Cocktail-party 2 0.804±0.006 0.616±0.010 0.525±0.000 0.540±0.005 0.582±0.009 0.558±0.002 0.588±0.004 0.506±0.001 0.502±0.005 0.500±0.000
Broderick-reverse 2 0.838±0.017 0.769±0.017 0.554±0.013 0.570±0.015 0.573±0.007 0.634±0.014 0.527±0.017 0.506±0.002 0.500±0.001 0.500±0.000
ChineseEEG2-RA-Tone 4 0.248±0.007 0.253±0.002 0.247±0.010 0.248±0.002 0.245±0.004 0.248±0.004 0.248±0.001 0.250±0.006 0.247±0.004 0.250±0.000
Type-VI
BCIC-IV-2a 4 0.401±0.020 0.335±0.005 0.308±0.005 0.300±0.019 – – 0.250±0.000 0.284±0.011 0.291±0.005 0.250±0.000
Physionet-MI 4 0.490±0.016 – 0.291±0.010 0.264±0.015 0.263±0.016 0.285±0.026 0.236±0.011 0.279±0.016 – 0.250±0.000
SHU-MI 2 0.589±0.011 0.538±0.013 0.557±0.027 0.535±0.019 0.506±0.015 0.501±0.013 0.528±0.008 0.497±0.012 0.507±0.003 0.500±0.000
BETA-SSVEP 40 0.097±0.003 0.037±0.006 0.035±0.004 0.038±0.006 0.029±0.003 0.027±0.001 0.033±0.003 0.025±0.006 0.026±0.001 0.025±0.000
Dual-Freq-SSVEP 40 0.087±0.002 0.036±0.009 0.052±0.007 0.032±0.005 0.020±0.011 0.025±0.005 0.031±0.006 0.023±0.003 0.023±0.004 0.025±0.000
SSVEP-9-chn 160 0.023±0.006 0.043±0.002 0.018±0.003 0.006±0.001 0.007±0.002 0.011±0.003 0.006±0.000 0.007±0.003 0.012±0.003 0.006±0.000
Monitoring-Errp 2 0.540±0.014 0.503±0.016 0.509±0.008 0.502±0.013 0.519±0.006 0.509±0.012 0.480±0.018 0.501±0.007 0.507±0.010 0.500±0.000
EEG-ControlledExoskeleton 2 0.544±0.004 0.516±0.004 0.519±0.009 0.519±0.008 0.528±0.003 0.518±0.003 0.546±0.003 0.513±0.018 0.505±0.005 0.500±0.000
SupplementaryTable7. Cross-subjectfull-finetuningresults(balancedaccuracy,mean±stdover3
runs).
Dataset #Classes CBraMod LaBraM FEMBA NeuroGPT NeuroLM BIOT BrainOmni REVE EEGMamba EEGConformer EEGNet BENDR
Type-II
MPI-LEMON-age 4 0.581±0.051 0.518±0.031 0.540±0.010 0.537±0.019 0.582±0.030 0.485±0.008 0.527±0.007 0.457±0.021 0.502±0.004 0.343±0.028 0.333±0.000 0.333±0.000
MPI-LEMON-gender 2 0.692±0.022 0.682±0.006 0.587±0.023 0.636±0.010 0.569±0.027 0.593±0.052 0.587±0.002 0.533±0.011 0.564±0.031 0.578±0.033 0.513±0.000 0.500±0.000
MPI-LEMON-extraversion 2 0.552±0.010 0.556±0.033 0.531±0.000 0.562±0.014 0.541±0.002 0.463±0.000 0.502±0.000 0.508±0.017 0.506±0.015 0.486±0.041 0.471±0.033 0.500±0.000
HFO 2 0.603±0.016 0.688±0.004 0.546±0.012 0.545±0.015 0.595±0.000 0.647±0.030 – 0.528±0.022 0.596±0.009 0.535±0.012 0.529±0.014 0.500±0.000
TUAB 2 – 0.767±0.009 – – – 0.761±0.016 0.703±0.021 – – 0.687±0.037 0.666±0.015 –
TUEV 6 – 0.606±0.032 – – – 0.707±0.014 0.615±0.046 – – 0.506±0.110 0.434±0.117 –
TUEP 2 – – – – – 0.623±0.022 0.634±0.013 – – 0.634±0.021 0.585±0.011 –
TUSL 3 – – – – – 0.742±0.066 0.624±0.180 – – 0.425±0.066 0.287±0.005 –
SienaEEG 2 0.742±0.041 – 0.733±0.151 0.491±0.082 – 0.795±0.033 0.445±0.129 0.573±0.022 – 0.715±0.117 0.632±0.158 0.750±0.250
ADHD 2 0.640±0.093 0.718±0.099 0.728±0.017 0.714±0.127 0.713±0.093 0.593±0.004 0.702±0.055 0.565±0.035 0.645±0.108 0.593±0.060 0.627±0.022 0.500±0.000
AD65 3 0.612±0.048 0.631±0.136 0.616±0.133 0.405±0.105 0.499±0.096 0.567±0.001 0.423±0.064 0.421±0.048 0.546±0.192 0.364±0.044 0.380±0.044 0.333±0.000
PD31 2 0.563±0.000 0.585±0.000 0.745±0.000 0.764±0.000 0.098±0.000 0.602±0.000 0.651±0.000 0.537±0.000 0.188±0.000 0.377±0.190 0.272±0.179 0.000±0.000
PD-motaility 2 0.664±0.106 0.642±0.033 0.545±0.040 0.506±0.008 0.518±0.018 0.683±0.047 0.499±0.014 0.561±0.042 0.579±0.006 0.499±0.003 0.500±0.000 0.500±0.000
MDD 2 0.736±0.259 0.773±0.173 0.775±0.145 0.885±0.048 0.961±0.036 0.853±0.010 0.977±0.015 0.901±0.003 0.870±0.083 0.927±0.045 0.947±0.028 0.500±0.000
TDBRAIN 4 0.370±0.002 0.421±0.009 0.448±0.044 0.385±0.011 0.423±0.069 0.392±0.034 0.378±0.008 0.345±0.000 0.381±0.021 0.389±0.013 0.379±0.024 0.250±0.000
Depression-resting 2 0.704±0.000 0.519±0.000 0.562±0.000 0.531±0.000 0.580±0.000 0.613±0.000 0.537±0.000 0.519±0.000 0.572±0.000 0.500±0.000 0.500±0.000 0.500±0.000
Type-III
Awakening 2 0.979±0.010 0.992±0.008 0.975±0.006 0.975±0.009 0.893±0.051 0.986±0.014 – 0.982±0.014 0.955±0.033 0.805±0.001 0.668±0.008 0.500±0.000
ISRUC-S1 5 0.586±0.026 0.653±0.051 0.691±0.001 0.666±0.005 0.551±0.089 0.650±0.032 0.629±0.030 0.654±0.016 0.633±0.053 0.495±0.027 0.453±0.033 0.200±0.000
ISRUC-S2 5 0.218±0.002 0.196±0.012 0.235±0.015 0.240±0.012 0.199±0.004 0.265±0.036 0.276±0.000 0.242±0.013 0.241±0.019 0.227±0.024 0.206±0.007 0.200±0.000
ISRUC-S3 5 0.233±0.011 0.327±0.010 0.333±0.064 0.304±0.020 0.298±0.048 0.355±0.039 0.326±0.001 0.303±0.021 0.335±0.010 0.290±0.017 0.255±0.029 0.200±0.000
SleepEDF 5 0.733±0.011 0.745±0.015 0.736±0.002 0.703±0.015 0.740±0.006 0.200±0.000 0.700±0.003 0.733±0.008 0.677±0.001 0.631±0.009 0.587±0.018 0.200±0.000
RestCog 5 0.389±0.023 0.400±0.026 0.351±0.021 0.390±0.033 0.345±0.016 0.396±0.030 – 0.289±0.014 0.345±0.020 0.284±0.004 0.267±0.008 0.200±0.000
Type-IV
SEED-VIG 3 0.458±0.008 0.479±0.031 0.321±0.065 0.406±0.013 0.439±0.012 0.333±0.000 0.505±0.007 0.392±0.003 0.396±0.025 0.340±0.008 0.342±0.000 0.333±0.000
EEG-SVRec 2 0.503±0.001 0.497±0.003 0.502±0.006 0.498±0.000 0.499±0.001 0.499±0.005 0.498±0.003 0.497±0.003 0.500±0.001 0.498±0.004 0.492±0.005 0.500±0.000
MusicEEG 2 0.556±0.027 0.454±0.008 0.492±0.067 0.485±0.031 0.532±0.074 0.378±0.068 – 0.499±0.038 0.471±0.045 0.546±0.005 0.595±0.030 0.500±0.000
CIRE 2 0.524±0.006 0.551±0.007 0.515±0.010 0.528±0.041 0.506±0.017 0.523±0.013 0.523±0.009 0.511±0.001 0.544±0.031 0.517±0.002 0.519±0.001 0.500±0.000
Workload 3 0.400±0.011 0.437±0.020 0.395±0.013 0.404±0.010 0.492±0.021 0.447±0.037 0.473±0.018 0.360±0.003 0.400±0.015 0.476±0.012 0.402±0.013 0.333±0.000
Type-V
BCI-Speech 5 0.262±0.010 0.225±0.003 0.249±0.003 0.210±0.022 0.207±0.005 0.267±0.025 0.199±0.007 0.208±0.012 0.200±0.008 0.222±0.022 0.206±0.009 0.200±0.000
Broderick-Cocktail-party 2 0.400±0.144 0.332±0.061 0.432±0.028 0.202±0.202 0.255±0.255 0.388±0.051 0.431±0.113 0.410±0.015 0.421±0.064 0.514±0.002 0.503±0.004 0.250±0.250
Broderick-reverse 2 0.688±0.116 0.656±0.035 0.566±0.067 0.570±0.051 0.570±0.029 0.459±0.002 0.443±0.035 0.918±0.049 0.392±0.108 0.496±0.003 0.500±0.000 0.500±0.000
ChineseEEG2-RA-Tone 4 0.253±0.003 0.251±0.003 0.252±0.002 0.251±0.001 0.251±0.001 0.252±0.002 0.246±0.000 0.250±0.001 0.255±0.007 0.253±0.005 0.252±0.003 0.250±0.000
ThingsEEG2 2 0.500±0.000 0.500±0.000 0.498±0.002 0.500±0.000 0.500±0.000 0.498±0.002 0.502±0.002 0.500±0.000 0.500±0.000 0.498±0.002 0.498±0.002 0.500±0.000
Type-VI
BCIC-IV-2a 4 0.372±0.005 – 0.391±0.016 0.309±0.026 – 0.250±0.000 0.338±0.011 0.273±0.007 0.324±0.010 0.374±0.004 0.348±0.023 0.250±0.000
BCIC-IV-1 2 0.517±0.022 0.507±0.028 0.527±0.033 0.502±0.013 0.487±0.003 0.458±0.043 0.482±0.028 0.515±0.015 0.490±0.000 0.502±0.007 0.495±0.030 0.500±0.000
Physionet-MI 4 0.549±0.000 0.501±0.022 0.519±0.020 0.480±0.007 0.508±0.004 0.261±0.001 0.387±0.017 – – 0.489±0.015 0.437±0.016 0.250±0.000
SHU-MI 2 0.520±0.018 0.525±0.009 0.544±0.002 0.500±0.002 0.502±0.000 0.527±0.013 0.536±0.021 0.536±0.019 0.481±0.015 0.525±0.034 0.530±0.012 0.500±0.000
BETA-SSVEP 40 0.150±0.009 0.100±0.010 0.041±0.000 0.095±0.005 0.082±0.003 0.044±0.009 0.081±0.001 0.100±0.022 0.037±0.005 0.027±0.000 0.028±0.001 0.025±0.000
Benchmark-SSVEP 40 0.678±0.090 0.701±0.096 0.291±0.078 0.617±0.090 0.340±0.065 0.310±0.048 0.268±0.011 0.674±0.140 0.116±0.002 0.036±0.004 0.062±0.006 0.025±0.000
Dual-Freq-SSVEP 40 0.173±0.027 0.057±0.012 0.033±0.005 0.052±0.002 0.037±0.007 0.043±0.010 0.067±0.013 0.089±0.009 0.033±0.002 0.033±0.005 0.027±0.004 0.025±0.000
SSVEP-9-chn 160 0.227±0.001 0.016±0.004 0.005±0.002 0.015±0.001 0.140±0.026 0.006±0.000 0.043±0.010 0.110±0.009 0.020±0.009 0.008±0.001 0.010±0.000 0.006±0.000
Monitoring-Errp 2 0.527±0.006 0.491±0.015 0.510±0.006 0.515±0.003 0.509±0.006 0.501±0.007 0.493±0.017 0.507±0.008 0.502±0.006 0.542±0.038 0.513±0.019 0.500±0.000
27

SupplementaryTable8.LinearprobingonSEED-VIGvigilanceregression(cross-subject,mean±std
over3seeds).
R2
| Model     | ↑            | r↑           | RMSE↓       |
| --------- | ------------ | ------------ | ----------- |
| BENDR     | −0.009 ±.008 | 0.042 ±.038  | 0.257 ±.039 |
| BIOT      | −0.064 ±.080 | −0.082 ±.008 | 0.270 ±.032 |
| BrainOmni | −0.073 ±.277 | 0.428 ±.239  | 0.259 ±.047 |
| CBraMod   | −0.023 ±.433 | 0.548 ±.207  | 0.242 ±.028 |
| EEGMamba  | −0.002 ±.272 | 0.463 ±.139  | 0.247 ±.025 |
| FEMBA     | +0.054 ±.190 | 0.441 ±.167  | 0.242 ±.032 |
| LaBraM    | −0.033 ±.340 | 0.458 ±.207  | 0.252 ±.032 |
| NeuroGPT  | +0.076 ±.100 | 0.443 ±.204  | 0.238 ±.043 |
| NeuroLM   | −0.019 ±.335 | 0.550 ±.113  | 0.249 ±.021 |
| REVE      | −0.296 ±.905 | 0.559 ±.167  | 0.270 ±.059 |
28