EEG Foundation Models: A Critical Review of Current
Progress and Future Directions
Gayal Kuruppu1,†,*, Neeraj Wagh2,†, Vaclav Kremen3, Sandipan Pati4, Gregory Worrell3,
and Yogatheesan Varatharajah1,2
1DepartmentofComputerScience&Engineering,UniversityofMinnesotaTwinCities,MN,USA
2DepartmentofBioengineering,UniversityofIllinoisatUrbana-Champaign,Urbana,IL,USA
3DepartmentofNeurology,MayoClinic,Rochester,MN,USA
4DepartmentofNeurology,UniversityofMinnesotaTwinCities,MN,USA
†Equalcontributions
*Correspondence: kurup016@umn.edu
ABSTRACT
Premise. Patterns of electrical brain activity recorded via electroencephalography (EEG) offer immense value
forscientificandclinicalinvestigations. TheinabilityofsupervisedEEGencoderstolearnrobustEEGpatterns
andtheirover-relianceonexpensivesignalannotationshavesparkedatransitiontowardsgeneral-purposeself-
supervisedEEGencoders,i.e.,EEGfoundationmodels(EEG-FMs),forrobustandscalableEEGfeatureextraction.
However, the real-world readiness of early EEG-FMs and the rubrics for long-term research progress remain
unclear. Objective.Inthiswork,weconductareviewoftenearlyEEG-FMstocapturecommontrendsandidentify
keydirectionsforfuturedevelopmentofEEG-FMs.Methods.WecomparativelyanalyzeeachEEG-FMusingthree
fundamentalpillarsoffoundationmodeling,namelytherepresentationofinputdata,self-supervisedmodeling,and
theevaluationstrategy. Basedonthisanalysis,wepresentacriticalsynthesisofEEG-FMmethodology,empirical
findings,andoutstandingresearchgaps. Results.WefindthatmostEEG-FMsadoptasequence-basedmodeling
schemethatreliesontransformer-basedbackbonesandthereconstructionofmaskedtemporalEEGsequences
forself-supervision. However,modelevaluationsremainheterogeneousandlargelylimited,makingitchallenging
toassesstheirpracticaloff-the-shelfutility. Inadditiontoadoptingstandardizedandrealisticevaluations,future
workshoulddemonstratemoresubstantialscalingeffectsandmakeprincipledandtrustworthychoicesthroughout
theEEGrepresentationlearningpipeline. Significance.Ourreviewindicatesthatthedevelopmentofbenchmarks,
softwaretools,technicalmethodologies,andapplicationsincollaborationwithdomainexpertsmayadvancethe
translationalutilityandreal-worldadoptionofEEG-FMs.
1 Introduction
Electroencephalography(EEG)isawidelyusedneurophysiologicalmodalityformeasuringthebrain’selectrical
activitywithhightemporalresolution[1]. Multi-channelEEGrecordingsencodecomplexneuraldynamicsacross
spatial,temporal,andspectraldimensions,necessitatinginterpretationbyhighlytrainedexperts. Despiteextensive
effortstodevelopquantitativeEEGrepresentationsusinghandcraftedfeatures, advancedsignalprocessing, and
contemporary machine learning approaches, expert visual review remains the gold standard for clinical EEG
interpretationanddecision-making. However, inthelastdecade, EEGresearchhasseensignificantadvancesin
deeplearning-basedapproachesforextractingapplication-specificfeaturesfromrawEEGdata(EEG-DL)[2,3].
AlthoughthislineofresearchheldsignificantpotentialtoaugmenttraditionalvisualEEGreview,itmetwithlimited
successduetoseveralreasons. MuchoftheEEG-DLresearchcomprisedend-to-endlearningmethodsthatreliedon
supervisedlearningandweretrainedonaverynarrowgroupofEEGtasks,i.e.,use-cases,anddatasetsthatresulted
fromlaboriousexpert-drivenannotationefforts[4]. Theseeffortswereclearlyunscalabletocoverthewiderangeof
EEGtasksthatmightbeneededinclinicalorscientificEEGreview. Furthermore,suchsupervisedEEGencoders
werehighlysusceptibletooverfittingonerroneousandnoisytraininginstances,raisingconcernsaboutrobustness
andtransferabilitytoothertasksanddatasets. Thislackofrobustnesswasfurtherexacerbatedbythevariability
1
5202
ceD
42
]PS.ssee[
3v38711.7052:viXra

ofEEGrecordingsacrossrecordingsites,acquisitionsystems,subjects,andsessions,leadingtoalackoftrustin
supervised EEGencoders [5, 6]. These limitationsemphasized the needfor EEG-DL solutionsthat relyless on
expertEEGlabelsandyieldrobust,trustworthy,andexplainablemodelswithhightranslationalvalue.
Theemergingparadigmoffoundationmodels(FMs)[7], basedonlabel-freeself-supervisedlearning(SSL)
andefficienttransferlearning,isapromisingsolutionforthesedata-relatedchallenges. Similartothemainstream
vision[8–10]andlanguage[11–13]FMs,EEGfoundationmodels(EEG-FMs)aretrainedtoidentifysalientEEG
featuresfromrawunlabeledEEGrecordingsbyusingvariousSSLpretexttasks,suchasmaskedreconstruction
ormaskedprediction,viaaprocessknownaspretraining. EEG-FMslearntorepresentEEGdataascompressed
embeddings in a latent space by leveraging the intrinsic properties found in the raw data. Pretrained EEG-FMs
canthenbeadaptedforvariousdownstreamapplicationsusingonlyverysmallamountsoflabeleddata,thereby
alleviatingtheburdenofexpertEEGannotations–themainbottleneckinsupervisedEEG-DLresearch. Assuch,
EEG-FMsholdpromiseaspowerful,off-the-shelffeatureextractors(orencoders)thatcansupportscientificresearch,
next-generationrobustbrain-computerinterfaces,andaugmentedneurologicaldecisionsupport.
Several EEG-FMs have been proposed over the last few years [14–23], whose chronological order along
with total annual Google Scholar search results for the term “EEG Foundation Model” is shown in Figure 1.
Despitethegrowinginterest,manyquestionsremainunansweredregardingthedesignchoicesinEEG-FMs,the
learnedrepresentations,performanceacrossvariousreal-worldapplications,andtheguaranteesofrobustnessand
trustworthiness. Forexample,thechoiceofEEGinputrepresentations,architecturalcomponents,andSSLpretext
taskscanvarysignificantlyacrossmodels,andtheeffectsofthosechoicesonthelearnedfeaturesareunclear. The
complexity,quality,andflexibilityoftherepresentationslearnedbyEEG-FMsandtheirrelationtobrainphysiology
havenotbeensufficientlystudied,raisingquestionsabouttheirexplainability. Furthermore,theperformanceand
generalizabilityoftheseEEG-FMsbeyondthecommonpublicdatasetsandbenchmarkshavenotbeenadequately
evaluated. ThesequestionsandconcernscallforacriticalreviewoftheearlyEEG-FMs,focusingonarchitectural
choices, pretraining approaches, evaluations, and trustworthiness, to identify rubrics for meaningful long-term
progressinEEG-FMresearchandtoadvancetheirtranslationalvalue.
Figure 1. Electroencephalographyfoundationmodel(EEG-FM)publicationtrends. ThetotalannualGoogle
Scholarsearchresultsfortheterm“EEGFoundationModel”between2021and2024(September)areshownin
blue. ThespecificEEG-FMsreviewedinthisstudy(i.e.,accordingtothesearchcriteriadescribedinsection3)are
listedinred,inchronologicalorderbytheirpreprintpublicationdates.
Tothatend,thistopicalreviewsurveystenearlyEEG-FMs(betweenJanuary2021andSeptember2024)and
critically analyzes their building blocks, identifies key takeaways and research gaps, and suggests directions for
future EEG-FM research. Recent studies have begun to survey EEG-FMs [24–26], but these reviews primarily
2/35

emphasizetechnicalcomponentssuchasmodelarchitecturesandself-supervisedlearningstrategies. Incontrast,
criticalfactorsrelatedtodatarepresentation,evaluationscope,andrigorhavereceivedrelativelylittleattention. Even
morelimitedisthediscussionofreal-worldtranslationalrequirementsandthepracticalconstraintsunderwhich
EEG-FMswillultimatelyneedtooperate. Inthisreview,weofferamoreholisticperspectiveonthedevelopment
andassessmentofEEG-FMs,adoptingadata-anddomain-centricviewpointtoevaluatetheirmaturityforclinical
translationandreal-worlduse. Wealsohighlightcomplementaryresearchdirectionsthatcanhelppositionfuture
EEG-FMs for meaningful practical impact. This review is organized as follows. Section 2 introduces the EEG
recordingprocedures,theinformationcontentofEEGs,traditionalquantitativeEEGapproachesbasedonfeature
engineering,thesourcesofdatavariability,andthedifferentfunctionalcomponentsoffoundationmodels. Section3
describesthesearchstrategyweundertooktoidentifypreviouslypublishedEEG-FMsandprovidesbriefsummaries
of those models. Section 4 provides a comprehensive analysis of each of the identified EEG-FMs along several
dimensions,includingtrainingdata,datapreprocessing,inputrepresentations,modelarchitecturalcomponents,and
modelevaluationstrategies. Section5discussesthekeytakeawaysandresearchgaps,andSection6laysoutour
viewforfuturedirectionsthatwouldfurtheradvancethecurrentstateoftheart.
2 Background
EEGisacommonneurophysiologicaltechniqueforrecordingelectricalactivitygeneratedbythebrainusingoneor
moreelectrodes. EEGemergedintheearlynineteenthcenturyandhassinceexpandedintomanyareasofscience
andmedicine. Itiswidelyusedinclinicalandresearchsettingsfordiagnosingneurologicaldisorders[27],studying
brain function [28], and developing brain-computer interfaces [29]. EEG measures voltage potentials and their
fluctuationsresultingfromioniccurrentflowmainlygeneratedbyfiringpopulationsofneurons[30]. ScalpEEGis
typicallycapturedusingelectrodesplaceddirectlyonthescalp. EEGcanalsoberecordedinvasively,withelectrodes
placedintracranially(withinthebrain)orsubdurally(undertheskin),commonlyreferredtoasintracranialEEG
(iEEG).WhileiEEGmeasuressummatedlocalfieldpotentialsgeneratedbysmallerneuronalpopulations,scalpEEG
measurestheelectricalactivitygeneratedbylargeneuronalpopulationsthatpassthroughmultiplelayersofthebrain
andhead(i.e.,cerebrospinalfluid,meninges,skull,muscles,scalp). Theconductionofneuronalactivitythrough
theselayerscausessignificantattenuationandspatialmixingoftheEEGsignal[31],includingartifactscausedby
movementsofelectrodesandmuscleactivity. Asaresult,scalpEEGhasconsiderablydifferentspatio-temporal
resolution,amplitude,frequency,andnoisecontentcomparedtointracranialEEG[32].
2.1 Contents and Sources of Variability in EEG Data
The EEG signal is a noisy, high-dimensional, spatio-temporal measurement of electrical brain activity. Several
factorsinfluencethecontentsofEEGrecordings,includingphysiological,pathological,andartifactualelements.
Physiologicalelements: MostofthephysiologicalelementspresentinEEGcanbedescribedusingthevarious
oscillatory components known as the delta, theta, alpha, beta, and gamma bands, each with distinct oscillatory
frequenciesandphysiologicalmechanisms [33]. Thegeneralattentionalstateofthesubjectduringtherecording
(awake,drowsy,asleep)influencesthespatio-temporalcharacteristicsofEEG[34]. Inaddition,EEGalsoshows
changesrelatedtonaturalaging[35]andotherbenignchangesinbrainstructureandfunction.
Pathologicalelements: TheprimarydiagnosticvalueofEEGisduetoitsabilitytocapturevariouspathological
brainactivitypatterns. Theseelectrographicpatternsincludeseizures,interictalepileptiformdischarges(e.g.,spikes
andsharpwaves),triphasicwaves,rhythmicdischarges,lateralizedperiodicdischarges,backgroundslowing,and
otherdiffuseorfocalabnormalelectroencephalogrampatterns[27].
Artifactualandnoiseelements: EEGartifactscanbeintroducedbybiologicalphenomena(e.g.,eyeblinks,head
movement,muscleactivity,cardiacsignals),recordingconditions(e.g.,signaldiscontinuities,transientfiltereffects),
or external sources (e.g., electromagnetic interference) [36]. Eye- and muscle-related activities are the primary
sourcesofartifactsinEEGs,introducingslow,high-amplitudechangesandfast,low-amplitudechanges,respectively.
Inadditiontotheseartifacts,consistentnoisefromthepowerlineanditsharmonicsmayalsobepresent. Finally,
certainmedications,suchasanti-depressantsandanti-seizuremedications,affecttheEEGaswell. Forexample,
benzodiazepinesandbarbituratesareknowntocausechangestotheEEG[37].
3/35

ThevariouspracticesandconfigurationsusedinclinicalstudiesintroducevariabilitiesacrossEEGdatasets. First,
thehardwareusedtorecordEEGscanhavepresetconfigurationsforsamplingfrequency,filtering,analog-to-digital
quantization,amplificationmagnitude,andbroadbandnoiselevels[38]. Second,theEEGexaminationprotocol
maydifferbetweenclinicalsites: therecordinglengthcouldbedifferent;recordingscanhavevariableamountsof
wake/sleepsegmentsandeyesopen/closedsegments;andtheymayincludecognitivetestsandactivationprocedures
such as sleep deprivation, photic stimulation, or hyperventilation. In addition, the EEG layout (i.e., the number
ofleadsandtheirpositions)andthereferenceleadsmayvaryacrosssites. Finally,anatomical[39],genetic[40],
and biochemical [41] differences introduce inter-individual variability. These factors make data ingestion and
standardizationnon-trivial,especiallyinintracranialEEGdatasets,whereleadlocationsaresubject-specific.
2.2 Feature Extraction from EEG Signals
CharacteristicsofclinicalEEGsareassessedvisuallybyexpertstrainedtodetectpathologicaleventsandadverse
deviationsfromhealthybrainactivity[42]. However,innon-clinicalsettings,theEEGischaracterizedbysignal
features derived computationally or analytically from the raw data. Quantitative EEG features serve as lower-
dimensionalproxiesoftherawsignal,quantifyingpertinentbrainactivityandprovidingobjectiveEEGassessments
for various applications. Classical EEG features are derived from signal processing, statistics, and information
theory domains. Examples include relative band-limited power, power ratios, independent components, sample
entropy,andkurtosis,amongothers[43]. Inselectinstances,theseEEGfeaturesisolateandquantifymeaningful
characteristicsofunderlyingbrainphysiology,suchasneuronaloscillationsandfunctionalconnectivity,andare
thereforeconsideredrobustandinterpretable. InsupervisedEEG-DLmodels,EEGfeaturesarelearneddirectlyfrom
rawEEGdatatoincreaseperformanceforaparticulartask[44]. WhileEEG-DLmodelsmaypushtheboundaries
oftaskperformance,theirblack-boxnaturemakesitnon-trivialtorelatethemtobrainphysiology. Furthermore,
EEG-DLfeaturesmayoverfitthenoiseinEEGsignals,makingthemlesslikelytogeneralizeoutofthebox. Hence,
therobustness,reliability,andinterpretabilityofEEG-DLfeatureextractorsremainopenresearchproblems.
2.3 Pillars of Foundation Modeling
Inthissection,wedeconstructtheFMmonolithintoasetofuniversal,domain-agnosticbuildingblocksorpillars.
ThesepillarsareminimallyrequiredtosystematicallycomparediverseexistingEEG-FMsandtobuildnewones.
Representationofinputdata: EEGsignalsareacquiredasaspatio-temporaldatastream. Visualreviewofclinical
EEGsisconductedprimarilyinthis‘native’view. However,thecomputationalinterpretationandanalysisofEEGs
canbenefitfromalternative,perhapsmoreinformative,representationsofrawdata. Forexample,representingEEGs
asatemporalstreamofshortspatio-spectraldatasegments(10seach)couldmakeiteasierforEEG-FMstolearn
latentfrequencypatternsandmulti-scaleinformation. Alternatively,representingEEGsusingspatialcovariance
matrices can make it easier to extract latent connectivity patterns. Broadly, the choice of data representation at
theinputstagemaygreatlyinfluencethequalityandsemanticsoflearnedlatentrepresentations[45]. Inbiosignal
domains where data are sampled from underlying physiological processes, constructing informative input data
views may itself require significant offline transformations or even domain-specific modeling, such as inverse
modeling[46]. Withouttheseofflineefforts,data-drivenlearningoflatentrepresentationsviaFMsmaybeinfeasible.
Architectural and functional design of FMs: At an architectural level, FMs are typically built from several
non-lineartransformerblocksthatcanbereadilystackedtoscalethemodeldepthandsize. Transformerblocks
themselvescontainmultiplefeed-forwardlayersfollowedbyamulti-headattentionmodule[47]. VisionFMsmay
useconvolutionalblockstoexploitthedesirablespatialinductivebiasofconvolutionaloperations[48]. Regardless
of model size or low-level architectural choices, encoder-only FMs are understood to have only two high-level
functionalcomponents: abackbonenetworkandafinalsinglefullyconnectedlayer. Thebackbonenetworkserves
asafeatureextractor,providinglow-dimensionalembeddings(orrepresentations)oftheinputdata. Thefinallayer,
referredtoasataskhead,thenusestheseembeddingsfortask-specificpurposessuchasclassificationorregression.
Self-supervised learning (SSL): In the SSL paradigm, supervision for training is derived strategically from
unlabeledinputdata(pseudo-labels)ratherthanfromhuman-curatedlabels,asinsupervisedlearning[49]. SSL
objectives(pretexttasks)arecommonlyeithercontrastiveorgenerative. Contrastivepretexttasksusemeaningfully
4/35

augmented or noisy views of the input to learn robust data representations using encoder-only backbones [50].
Generativepretexttasksmaskportionsoftheinputandreconstruct/generatethemaskedportionsusingencoderand
decoder-basedbackbones[51]. Ineithercase,SSLlearnsgeneralintrinsicrelationshipswithinthedata,thereby
creatingatask-agnosticbackbonenetworkthatservesasageneralfeatureextractor. Thestructureofrepresentations
learnedbySSLtasksandgeneralprinciplesforeffectiveSSLtaskdesignareunderactivestudy. Regardless,the
valueofSSLisparticularlyhighintheEEGdomainasitimprovesmodelgeneralizability[52]andpartiallyalleviates
theneedforexpertEEGannotationsthatareexpensivetoobtain,subjective,anderror-prone[6].
Transferlearningandmodeladaptation: Thebackbonenetworkenablesthereuse,transfer,andadaptationof
EEGfeatures(i.e.,data-drivenEEGknowledge)acrosssemanticallyoverlappingtasks[53]. Theproportionofthe
backbone adapted for a specific application is flexible. For example, the backbone may be entirely fixed/frozen
(linearprobing),partiallyupdated,orentirelyupdated(fine-tuning)[54]. Thisadaptationprocessmayuseslower
orlayer-specificlearningratestopreservepretrainedknowledgewithinthebackbone. Ineithercase,anypretext
task-specificlayersatthetoparediscardedandreplacedwithanewtrainablelinearheadthatperformsclassification
orregressionforthe‘downstream’application. Usingapplication-specificdatasplitsandhuman-curatedtask-specific
labels,themodelisthentrainedfurtheruntilconvergence. Thedevelopmentofalgorithmsforrobustandefficient
adaptationisanactiveareaofresearch. Broadly,transferlearningandmodeladaptationtechniquesobviatetheneed
totrainnewEEG-DLmodelsfromscratchbyleveragingknowledgefrompre-existingmodels.
Dataandmodelscale: Thescalingupofpretrainingdatavolume,datadiversity(i.e.,thenumberofdistinctdata
sources),andmodelsizehascontributedtowardsimprovedpretrainedlatentfeatures,increaseddownstreamtask
performance, sample efficiency, and model generalizability, among other properties [55–60]. Empirical scaling
lawshaveestablishedpower-lawrelationshipsbetweenFMerrorratesandthreekeymodelinglevers,namelythe
pretraining data size, model size, and compute [57, 61], which suggest that an exponential increase in data and
model size can indeed improve FM performance, albeit with diminishing returns. Overall, the balance between
dataandmodelsizetomaximizeperformanceunderafixedcomputebudgetremainsacriticalconsiderationinFM
research. ItisnoteworthythatvisionandlanguageFMsareoftenmulti-billion-parametermodelspretrainedonan
internet-scalecollectionofdiversedatasets[62–64]. However,therelativescarcityoflarge-scaleEEGcorporamay
limitscalingeffortsinEEG-FMresearch.
3 Review Approach & Summary of EEG-FMs
ThissectiondescribesoursearchstrategyandsummarizestheEEG-FMstodate,highlightingthedatausedtotrain
thosemodels,modelscale,architecturaldetails,andevaluations.
3.1 Search Strategy
Weconductedacomprehensivesearchacrossvariouswebplatforms,includingGoogleScholar,arXiv,DBLP,IEEE
Xplore, PubMed, bioRxiv, and medRxiv, to identify relevant research in journals, conferences, workshops, and
preprints. Welimitedoursearchquery,(“EEG”AND“FoundationModel”),toidentifyFMsthatweredeveloped
primarily for scalp or intracranial EEG modalities. Our search starts from the year 2021 – the year the term
FoundationModelwasintroduced[7]–andincludesstudiesthatwerepublishedorarchiveduntilSeptember30th,
2024. Wethenremovedduplicateinstancesandmanuallyreviewedthetitle,abstract,andintroductionsectionsto
confirmrelevantEEG-FMsbyidentifyingphrasestotheeffectof"WedevelopedanEEGfoundationmodel..."and
"TheproposedapproachformsthebasisforanEEGfoundationmodel...". Itisimportanttonotethatweexcluded
studies that, a) propose individual components that are building blocks of foundation models (e.g., pretraining
strategies,spatio-temporalfeatureencoders),butnotfunctionaloff-the-shelffoundationmodels,andb)finetune
existingEEG-FMstoderivetask-specificmodels. Furthermore,ourreviewdoesnotincludemulti-modalfoundation
modelsandsleepfoundationmodelsdevelopedusingpolysomnography(PSG)data [65,66]. Nonetheless,webriefly
discusstwosleepfoundationmodelspublishedduringthesametimeframeinthesupplementforinterestedreaders.
Using thosesearch criteria, weidentified nine EEG-FMs, Neuro-GPT [15], Brant[16], BIOT [17], EEGFormer
[18],LaBraM[19],Mentality[20],NeuroLM[21],FoME[22],andBrainWave[23]. Inaddition,wealsoincluded
BrainBERTbecauseofitscommonpresenceasabaselineinotherEEG-FMevaluations[16,18,22,23].
5/35

| 3.2 EEG-FM | Summaries |     |     |     |     |     |
| ---------- | --------- | --- | --- | --- | --- | --- |
Table1summarizesalltenEEG-FMs. AlthoughalltheEEG-FMssharemanycommonalities,eachFMisuniquein
itsownright. InordertohighlightthebuildingblocksofeachFMandtheiruniquestrengths,belowwesummarize
each FM considering several factors, such as the amount of training data (in channel-hours, calculated as the
totalrecordingdurationmultipliedbythenumberofEEGchannels; seeSupplementTable1fordetails), model
size (in terms of the number of trainable parameters), the types of EEG data (scalp EEG and/or iEEG), the way
inputsareconfigured(rawtimeseries,powerspectra,ortime-frequencyrepresentation),architecturalcomponents
(convolutionaland/ortransformerblocks),theSSLtasksusedforpretraining(maskedreconstruction,auto-regressive
modeling,and/orcontrastivelearning),andtheevaluationsperformed.
Table1. Briefmodelsummaries. WeprovidebriefsummariesoftheEEGfoundationmodels(EEG-FMs)basedon
trainingdatasize,modelsize,inputconfigurations,inputdatatype,architecturalcomponents,andtheself-supervised
learning(SSL)tasksusedforpretraining. Hyperlinkspointtocodeandmodelweights,ifavailable. N/Arepresents
caseswherechannel-hoursormodelsizecouldnotbedetermined.
Training
Number
|     | Data |     | Input |     | Architectural |     |
| --- | ---- | --- | ----- | --- | ------------- | --- |
Model (channel- ofParam- Configuration DataType Components SSLTasks
eters
hours)
|           |      |        | Single-channel |              | Transformerencoderand |                |
| --------- | ---- | ------ | -------------- | ------------ | --------------------- | -------------- |
| BrainBERT |      |        |                | Intracranial |                       | Masked         |
|           | 4.5k | 43.18M | spectrogram    |              | shallowdecoderwithtwo |                |
| [link]    |      |        |                | EEG          |                       | reconstruction |
|           |      |        | data           |              | linearlayers          |                |
|           |      |        |                |              | Encoderwithboth       | Masked         |
Fixed
| Neuro-GPT |     |     |     |     | convolutionand | reconstruction |
| --------- | --- | --- | --- | --- | -------------- | -------------- |
[link] 541k 79.53M multi-channel ScalpEEG transformerlayersand (causallymasked
timeseriesdata
|     |     |      |     |     | GPT-2asthedecoder | latentembeddings) |
| --- | --- | ---- | --- | --- | ----------------- | ----------------- |
|     |     | 68M, |     |     | Twotransformer    |                   |
Variable
|             |      | 104M,   |               | Intracranial | encodersfortimeand | Masked         |
| ----------- | ---- | ------- | ------------- | ------------ | ------------------ | -------------- |
| Brant[link] | 281k |         | multi-channel |              |                    |                |
|             |      | 249Mand |               | EEG          | spaceandalinear    | reconstruction |
timeseriesdata
|     |     | 506M |     |     | decoder |     |
| --- | --- | ---- | --- | --- | ------- | --- |
Variable
BIOT[link] 312k 3.3M multi-channel ScalpEEG Lineartransformer, Contrastivelearning
encoder-onlyarchitecture
spectraldata
Atransformerencoder
|           |      |     | Multi-channel |          |                        | Codebook-based |
| --------- | ---- | --- | ------------- | -------- | ---------------------- | -------------- |
| EEGFormer | 541k | N/A |               | ScalpEEG | andashallowtransformer |                |
|           |      |     | spectraldata  |          |                        | reconstruction |
decoder
Convolutionaltemporal
encoderandtransformer
|     |     | 5.8M, | Fixed |     | encoderlayersanda | Masked |
| --- | --- | ----- | ----- | --- | ----------------- | ------ |
LaBraM[link] 80k 46Mand multi-channel ScalpEEG reconstruction
lineardecoder.A
|     |     | 369M | timeseriesdata |     |     | (token-level) |
| --- | --- | ---- | -------------- | --- | --- | ------------- |
separatedecoderfor
tokenization.
|     |     |     | Fixed |     | Convolutionallayersand |     |
| --- | --- | --- | ----- | --- | ---------------------- | --- |
Masked
Mentality N/A N/A multi-channel ScalpEEG Mambablocksinboth reconstruction
|     |     |     | timeseriesdata |     | encoderanddecoder |     |
| --- | --- | --- | -------------- | --- | ----------------- | --- |
Vectorquantizationfor
|     |     | 250M, | Variable |     | tokenizationwith | Autoregressive |
| --- | --- | ----- | -------- | --- | ---------------- | -------------- |
NeuroLM
546k 500Mand multi-channel ScalpEEG convolutionaltemporal reconstruction
[link]
|     |     | 1.7B | timeseriesdata |     | encoderandtransformer | (token-level) |
| --- | --- | ---- | -------------- | --- | --------------------- | ------------- |
spatialencoder
|      |     | 476Mand | Variable       | ScalpEEGand  | TemporalandSpatial    | Maskedsignal   |
| ---- | --- | ------- | -------------- | ------------ | --------------------- | -------------- |
| FoME | N/A |         | multi-channel  | intracranial | transformerencoderand |                |
|      |     | 745M    |                |              |                       | reconstruction |
|      |     |         | timeseriesdata | EEG          | alineardecoder        |                |
Variable
|     |     |     |     | ScalpEEGand | Transformerencoder | Masked |
| --- | --- | --- | --- | ----------- | ------------------ | ------ |
multi-channel
BrainWave 878k N/A intracranial withchannelattention reconstruction
spectrogram
|     |     |     | data | EEG | andalightweightdecoder | (wholespectrogram) |
| --- | --- | --- | ---- | --- | ---------------------- | ------------------ |
BrainBERT[14]: AsthefirstreleasedEEG-FM,BrainBERTisrelativelysmallerthanothers,with43.18Mparame-
ters,andwaspretrainedusingamodestdatasetof4.5kchannel-hoursofiEEGdata. Theinputswererepresented
aschannel-wisespectrograms,andaBidirectionalEncoderRepresentationsfromTransformers(BERT,[67])-type
modelwaspretrainedtopredictmaskedpatchesfordifferenttypesofspectrogramsbasedontheShort-TimeFourier
6/35

Transform(STFT,[68])andSuperlets[69]. Themodelcomprisedatransformerencoderandashallowdecoderwith
twolinearlayers. Evaluationsfocusedonevokedbrainresponseswhilewatchingmovies[70]anddemonstrated
generalizability to unseen subjects and electrode locations; however, the test data were drawn from the same
distributionasthetrainingdata. Theevaluationsalsoshowedthatlinear-probedBrainBERTperformancematched
that of randomly initialized supervised deep neural networks (DNNs) across most evaluation tasks. Additional
evaluationsshowedthatfine-tunedBrainBERTperformancecouldmatchthatofarandomlyinitializedDNNwith
aslittleas15%ofthetrainingdataforonetask. Atask-agnosticintrinsicdimensionality[71](ID)-basedanalysis
showedthattheBrainBERTembeddingsofdifferentbrainregionshaddistinctIDs,whereasthedistributionacross
electrodeswasrelativelyconstantunderrandomlyinitializedweights.
Neuro-GPT[15]: Thismid-sizeEEG-FMwith79.53MparameterswaspretrainedentirelyusingscalpEEGdata
fromthefullTempleUniversityHospital(TUH)EEGCorpus[72],whichincluded541kchannel-hoursofclinical
scalpEEGdata. Themodeltakesrawtimeseriesofthe22EEGchannelsinthestandard10-20layoutasinputand
learnsEEGrepresentationsusingacombinationofconvolutionalandtransformerlayers. Thoserepresentationsare
thenusedasinputtoaGenerativePretrainedTransformer(GPT-2,[73])decoder,whichautoregressivelypredicts
themaskedlatents. Itisnoteworthythatthedecoderhasmoreparametersthantheencoderinthissetup,whichis
notcommoninotherEEG-FMs. ThismodelwasevaluatedonEEGdatafroma4-classBrain-ComputerInterface
(BCI)motorimagerytaskwithadifferentchannelconfigurationthanthepretrainingdata. However,thedownstream
dataweretransformedtotheoriginalpretrainingconfigurationusinganinverse-forwardapproach[74]. Theresults
showedthatfine-tuningorlinearprobingthepretrainedmodelperformedbetterthanmodelstrainedfromscratch,
includingsomefully-supervisedEEG-DLapproaches.
Brant[16]: BrantisarelativelylargerFMwith500Mparametersandwaspretrainedusing281kchannel-hoursof
iEEGdata. However,itspretrainingdatawerelimitedtoasingledatasetcomprising9subjects. Thismodelaccepts
rawEEGtimeserieswithdifferentchannelconfigurationsasinput. Themodelconsistedofatemporalencoder
thatlearnslong-termtemporaldependencies,aspatialencoderthatlearnsspatialcorrelations,andasimplelinear
decoder. Thespatialencoderusedinthismodeltocapturespatialrelationshipsisanovelcontributioncompared
topreviousEEG-FMs. Thismodelincludesthreescaled-downversionswith68M,104M,and249Mparameters,
respectively, all pretrained on the same data. These models were evaluated on short-term and long-term signal
forecasting,frequency-phaseforecasting,imputation,seizuredetection,andpathologydetectiontasks. Theresults
showedthatBrantperformsbetterthanbaselinesinlimited-labelsettings.
BIOT [17]: This is the smallest of the ten reviewed EEG-FMs, with only 3.3M parameters, and was pretrained
usingacontrastivelearningobjective. TheBIOTmodelintroducedanovelapproachtohandlinginputdatawith
variablelengthsandvariablenumbersofchannels: ittokenizeseachchannelintofixed-lengthsegmentsrepresenting
frequencyvectors,organizestheminto‘sentences’,anduseschannelandpositionembeddingstopreservespatio-
temporal information. BIOT used linear transformers to reduce training time and was evaluated across multiple
clinicaltasks,includingseizuredetectionandseizuretypeclassification. BIOTshowedsuperiorperformanceeven
withoutpretrainingandevenbetterperformancewithpretraining,comparedtoprevioussupervisedEEG-DLmodels.
EEGFormer[18]: ThismodelwasalsopretrainedonthefullTUHcorpus,whichincludesapproximately541k
channel-hoursofclinicalscalpEEGdata. Itincludedatransformer-basedencoderandshallowdecoder,andwas
pretrainedwithamaskedreconstructionobjective. LatentfeaturesofinputEEGpatchesgeneratedbytheencoderare
usedtotrainavectorquantizertomatchneuralcodesgeneratedbyaneuralcodebook. Thedecoderthenreconstructs
theoriginalEEGpatchesusingtheseneuralcodes. Evaluationsincludedseveraldownstreamtasksderivedfromthe
TUHcorpusandanout-of-distribution(OOD)evaluationforneonatalseizuredetection. Additionalexperiments
includedaninterpretabilityanalysisusingthelearnedcodebook.
LaBraM [19]: This model used a relatively smaller dataset collected from multiple sources for pretraining,
comprising 80k channel-hours of scalp EEG data. It was developed at three parameter scales: 5.8M, 46M, and
369M, respectively. The LaBraM pretrained model consisted of two parts, the neural tokenizer and the neural
transformer. The neural tokenizer is first trained to learn a codebook that accurately predicts the amplitude and
phaseoftherawtimeseriesdata. Then,withthecodebookfrozen,theneuraltransformerispretrainedtopredict
thecodebook-basedcodesforthemaskedinputpatches. Notethatthisdiffersfromtypicalpretrainingprocedures,
7/35

where the goal is to reconstruct masked patches in the time-domain itself. This transformer model consists of a
convolutionaltemporalencoderandasetoftransformerblocks,withtemporalandspatialpositionalencodingsused
tolearnrelativerelationshipsbetweeninputpatches. Althoughtheevaluationsdemonstratedperformancegainsin
varioussubsetsoftheTUHcorpus,itisunclearwhethertheseresultsgeneralizetoout-of-distributiondata.
Mentality [20]: This model aims to capture the complex spatio-temporal dynamics of EEG signals using a
Mamba[75]-basedstate-spacemodel. ThearchitectureofMentalitydrewinspirationfromothermodelssuchas
SaShiMi[76],U-Net[77],andEEGNet[78]withtheinclusionofMambablocks. However,themodelwastrained
andevaluatedexclusivelyonasubsetoftheTUHcorpus.
NeuroLM[21]: ThismodelwasinspiredbyapreviousEEG-FM,LaBraM.However,NeuroLMwastrainedon
7x more data and is one of the largest EEG-FMs, with 1.7B parameters. Smaller model variants include 250M-
and500M-parameterversions. Theneuraltokenizerisfirsttrainedtolearnacodebookthatisbothalignedwitha
textembeddingspaceandcanaccuratelyreconstructtheinputtimeseriesdatainbothtimeandfrequencydomains.
These codes are then fed into a large language model for multi-channel autoregressive pretraining. Finally, this
pretrained model is adapted via joint multi-task instruction tuning, enabling a single model to perform diverse
EEGtaskswithouttask-specificfine-tuning. However,despitethenovelEEG-textalignmentandjointadaptation,
NeuroLMperformedworseondownstreamtasksthanLaBraMandotherstate-of-the-artmodels.
FoME [22]: This model included two versions with 476M and 745M parameters, respectively. The size of the
training data was not provided in the manuscript. The model takes masked time series patches and their power
spectraldensitiesasinput,whicharethentransformedbyatemporalencoder. Theoutputsofthetemporalencoder
arethenreorganizedbychannelandfedtoaspatialencodertoreconstructmaskedtimepatches. FoMEwasevaluated
acrossmultipledownstreamtasks,includingclassification,forecasting,andimputation;however,theevaluations
wereconductedonin-distributiondata,limitingbroaderconclusions.
BrainWave[23]: Thismodelwaspretrainedusingalargedatasetofsize878kchannel-hours,includingbothscalp
EEGandiEEG.ItincludesatransformerencoderandachannelattentionmodulethattransformEEGspectrograms
intolatentrepresentations,whicharethendecodedbyalightweightdecoder. Thisencoder-decoderarchitecturewas
trainedusingamasked-reconstructionobjective. BrainWaveisoneofthefewEEG-FMstrainedandevaluatedon
bothscalpEEGandiEEGsignals,demonstratingthebenefitsofjointpretrainingoverunimodalapproaches. The
modelhasbeenextensivelyevaluatedunderdifferentsettings,suchascross-subject,cross-hospital,cross-subtype
andfew-shotclassification,showcasingthegeneralizabilityandrobustnessacrossvariousclinicaltasks.
4 Comparative Analysis of EEG-FMs
ThissectionsurveysthetenEEG-FMsandcomparestheirdesignandconstructionalongthreemajoraxescovering
thepillarsoffoundationmodelingdescribedinsection2: a)preparationandrepresentationofinputdata,b)model
architectureandself-supervisedpretraining,andc)modelevaluations. Thevariousconsiderationsalongtheseaxes
areillustratedinFigure2.
4.1 Preparation and Representation of Input Data
Datasets: Pretraining data functions as the knowledge base of an FM, making it a highly crucial component.
Key factors, such as diversity, data volume, relevance, and, most importantly, data quality, can influence the
generalizabilityofthepatternslearnedbyanEEG-FM.Table2showsthedatasetsthatwereusedinthepretraining
andevaluationphasesofthetenEEG-FMsreviewedinthisarticle.
MostEEG-FMs(e.g.,LaBraM,EEGFormer,Neuro-GPT,Mentality,BIOT,andNeuroLM)weretrainedonlyon
scalpEEGdata,althoughsome(e.g.,BrantandBrainBERT)weretrainedexclusivelyoniEEGdata. TwoEEG-FMs,
FoMEandBrainWave,weretrainedonbothscalpandintracranialEEGdata. Alargeportionofthepretrainingdata
inthemodelsusedscalpEEGsfromtheTempleUniversityHospital(TUH)EEGcorpus[4],whichcomprises541k
channel-hoursofscalpEEGdata. Thiscorpusalsoincludedsmallerderivedsubsetscontainingexpertannotationsfor
EEGabnormalities(TUAB),seizures(TUSZ),andevents(TUEV). OtherscalpEEGdatasetsusedforpretraining
includeCHB-MIT[79]andsmallresearchdatasets. SomeFMsutilizedEEGdataavailablewithinPSGdatasetssuch
asSHHS[80],Sleep-EDF[81],andCAPSleep[82]. Additionally,publicorprivateiEEGdataaccountedforalarge
8/35

Figure 2. ComparativeanalysisofEEGfoundationmodels(EEG-FMs). OurreviewanalyzesEEG-FMsalong
threemajordimensions;inputdataconfiguration,modeling,andevaluation(topfigure). Asummaryofthevarious
approachesundertakenbytheEEG-FMstoaddressthosecomponentsisshowninthebottomfigure. EEGdatais
representedinoneofthreeforms: rawtimeseries,magnitudepowerspectrum,andtime-frequencyrepresentation.
Modelarchitecturemayincludeconvolutionalblockstolearnlow-levelpatternsand/ortransformerblockstolearn
higher-levelrelationships. Modelsarepretrainedprimarilyusingself-supervisedlearning(SSL)approaches;the
commonSSLapproachesusedaremaskedreconstruction,auto-regressivemodeling,andcontrastivelearning. The
pretrainedmodelsarethenevaluatedonvariousdownstreamtasks,includingclinicalandnon-clinicaltasks.
portionofthetrainingdatainsomemodels,suchasBrantandBrainWave. ThecommonpubliclyavailableiEEG
datasetsusedforpretrainingwereMAYO [83],FNUSA [83],BrainTreeBank[70],andCCEP [84]. Trainingdata
volumerangedfrom4.5kchannel-hoursinBrainBERTto878kchannel-hoursinBrainWave. BrainWaveutilizedthe
mostdiversepretrainingdataset,includingclinicalscalpEEGdatasets,sleepEEGdatasets,varioussmaller-scale
scalpEEGrepositories,andseveraliEEGdatasets. LaBraMandNeuroLMalsousedmoderatelydiversepretraining
datasets,butwerelimitedtothescalpEEGmodality.
Preprocessing and normalization: The content of EEG data is highly sensitive to the preprocessing and nor-
malizationstepsperformedbeforemodeltrainingorevaluation. Thechoicesmadeforresampling,bandpassand
notch filtering, artifact removal, and temporal data segmentation into patches or epochs can directly impact the
representationslearnedbyanEEG-FM.Althoughsomemodelsdidnotcomprehensivelydescribethepreprocessing
steps,mostappliedstandardproceduressuchasbandpassfiltering(0.5Hztoahighercutofffrequency),powerline
interferenceremovalvianotchfilters(50Hzor60Hz,includingharmonics),anddownsamplingto200Hzor250
Hztostandardizesamplingratesacrossdatasets. EEGsignalsarethensegmentedintosmallerepochs,typically
1-10secondslong. However,noneoftheEEG-FMsperformedexplicitartifactremovaloroutlierexclusion,except
incasesofexpertlylabeledbaddataormissingchannels. Other,lesscommonstepsincludedDCoffsetremovaland
lineartrendremovalbyFoMEandNeuro-GPT.Datanormalizationpracticesafterpreprocessingwerenotdescribed
inseveralmanuscripts. Neuro-GPTappliedthecommonlyusedz-transformalongthetimedimensiontonormalize
EEGsignals,whereasNeuroLM,BIOT,andLaBraMusedaconstantscalingfactorbasedontheinputrange.
Input representation: EEG is naturally a spatio-temporal data modality recorded using multiple channels. In
additiontospatialandtemporalinformation,spectralinformationisusefulforinterpretingEEGdata,whichismost
oftenusedasexpert-derivedfeaturesinstatisticalmachinelearning(ML)models. Furthermore, time-frequency
9/35

representations,suchasspectrogramsandwavelet[85]transforms,arealsousedtopreserveinformationinallthree
domains. AllEEG-FMsusedoneoracombinationoftheserepresentationsasinput.
Themostwidelyusedinputrepresentationisthemultivariatetime-seriesformat,adoptedbysixofthetenEEG-
FMs. Withtheadoptionofatransformerarchitecture,thewindowssegmentedfromtheoriginalrecordingrequire
furthersegmentationintosmallerpatches,alsoknownastokens. Thesepatchesortokenscanthenbeaugmented
withtemporalandspatialinformationviapositionalencodings,allowingthemodelstobetrainedonEEGdatawith
differentchannelconfigurations. ThisapproachwasadoptedbymodelssuchasBrant, NeuroLM,andFoMEto
pretrainondatasetswithvaryingchannelcounts. Twomodels,BIOTandEEGFormer,usedpower-spectraldataas
inputinsteadoftheoriginaltime-seriespatches,whiletwoothermodels,BrantandFoME,addedpower-spectral
data to complement the raw time-series inputs. Some EEG-FMs, such as LaBraM, Neuro-GPT, and Mentality,
standardizeddifferentEEGdatasetswithdifferentchannelconfigurationstoafixedsetofinputchannels. Twoother
models,BrainBERTandBrainWave,utilizedchannel-wisetime-frequencyrepresentationsof1-5secondsofEEG
dataasinput. BrainBERTevaluationsutilizedspectrogramsgeneratedusingclassicalmethodslikeSTFT,aswellas
scalograms[85]generatedusingmodernmethodssuchasSuperlets.
4.2 Modeling and Pretraining
Patchingandcontextlength: Thetemporalresolutionoftokensorpatches,i.e.,howmuchEEGdataeachpatch
contains,variesbetweenmodels,reflectingdifferentdesignchoicesinmodelarchitectureandtargettasks. Brant
and FoME used patches corresponding to six seconds of EEG, while BrainBERT used 5-second STFT/Superlet
windows. ModelssuchasLaBraM,NeuroLM,BIOT,andBrainWaveadoptedafinerresolution,using1-second
segmentsperpatch,whereasNeuro-GPTutilizedapatchsizeoftwoseconds. Similarly,contextlengthalsovaried
amongEEG-FMs. FoMEwastrainedon90-secondsegments,eachrepresentedbyasequenceof15tokens. LaBraM
couldtakeupto256tokensasinput,withthenumberoftemporaltokensdependingonthenumberofchannelsused.
Neuro-GPTutilizeda32-tokencontextwindowwithoverlappingsegments,covering∼57.8secondsofEEG.BIOT
utilized19tokensperchannelandEEGFormerutilized12secondsofEEGcontextasinput.
Architecturalcomponents: Themodelarchitectureandtrainingobjectivesplayacentralroleindeterminingthe
effectivenessofafoundationmodelinextractinginformationfromtheinputdata[7]. EEG-FMsutilizedvarious
componentsatdifferentstagesofthepipeline,includingtokenizers,localrepresentationlearningmodules,spatial
and/or temporal attention modules to learn dependencies, and task heads. Almost all the EEG-FMs we review
in this article are transformer-based, except Mentality, which uses a combination of convolutional layers and a
mamba-based architecture. In the transformer-based models, the input signal is divided into a fixed number of
small patches/tokens to construct the input sequence. Some models that used raw time-series inputs leveraged
convolutionallayerstolearnmorphologicalfeatures(e.g.,Neuro-GPT,LaBraM,Mentality,NeuroLM).
Neural tokenizers: Some models, such as LaBraM, NeuroLM, and EEGFormer, integrated separate tokenizers
to transform the input signals into discrete tokens or codes. These EEG-FMs adapted a VQ-VAE [125]-like
architecturetotrainaneuraltokenizer,whichmappedinputpatchesintoafixedsetofdiscreteembeddingscalledthe
codebook. Duringtokenizertraining,latentfeaturesaremappedtonearest-neighborembeddingsfromthecodebook
toreconstructknownfeaturesoftheinput,suchaspowerandphaseinLaBraM,andtemporalandspectralfeatures
in NeuroLM. The models used neural codebooks to reconstruct raw time-series inputs using a transformer-like
architecture. WhileNeuroLMandEEGFormerusedcodebookembeddingstomapencoderoutputstodiscretecodes
priortodecoding,LaBraMusedcodebookembeddingsofmaskedinputpatchesastargetsduringmodelpretraining.
Spatialencoding: EEG-FMsimplementeddifferentspatialencodingstrategies,althoughtheydifferinhowexplicitly
theyhandlespatialinformation. BrantandFoME,forexample,usedtransformerencoderswithspatialattention
but without dedicated spatial positional encodings. In contrast, LaBraM, BIOT, and NeuroLM injected spatial
informationthroughexplicitspatialencodingstoenhancepositionalencodingandcapturethetopographiclayoutof
EEGchannels. Amongthem,onlyBIOTsupportedmultipleelectrodeconfigurations,whileLaBraMandNeuroLM
arelimitedtoafixed10–20layoutforspatialencoding. ModelssuchasNeuro-GPTandMentalitylearnedspatial
dependenciesimplicitlyusingconvolutionallayers,withoutdedicatedspatialembeddings. BrainWaveincorporated
spatialattentionmechanismstomodelinter-channeldependenciesdirectly. Incontrast,BrainBERTandEEGFormer
10/35

Table 2. Datasetsusedforpretrainingandevaluation. Herewelistthediversesetofdatasetsandtasksthat
wereusedtopretrainandevaluateEEGfoundationmodels(EEG-FMs). Wehighlightdatasetsthatarenotpublicly
availableinbold,clinicalandnon-clinicaldatasetsinpinkandbluebackgrounds,respectively,andusesuperscripts
∗and#todenotein-distributionandout-of-distributionevaluations,respectively.
Dataset/EEG-FM BrainBERT Neuro-GPT Brant BIOT EEGFormer LaBraM Mentality NeuroLM FoME BrainWave
ScalpEEG
| TUEG[72] | train | train       |       | train train | train |
| -------- | ----- | ----------- | ----- | ----------- | ----- |
|          |       | eval# eval∗ | eval∗ | eval∗       |       |
TUAB(Abnormal/normalclassification-binary)
eval∗
| TUAR(EEGartifactclassification-multiclass) |     |     | train |     |     |
| ------------------------------------------ | --- | --- | ----- | --- | --- |
| TUEP(Epilepsyclassification-binary)        |     |     | train |     |     |
TUEV(EEGEventsclassification-multiclass) eval# eval∗ eval∗ eval∗
| TUSL(EEGslowingclassification-multiclass) |     | eval∗ | train | eval∗ |     |
| ----------------------------------------- | --- | ----- | ----- | ----- | --- |
TUSZ(Seizuretypeclassification-multiclass) eval∗ train train/eval∗
CHB-MIT[79](Peadiatricseizuredetection-binary) eval# train eval#
Sleep-EDFx[81](Sleepstageclassification-multiclass) train/eval∗ train
SienaScalpEEG[86](Seizureclassification-binary) train train train
| SHHS[87][80](Sleepstageclassification-multiclass)    |     | train |     |       |       |
| ---------------------------------------------------- | --- | ----- | --- | ----- | ----- |
| PREST(Abnormaleventdetection-binary)                 |     | train |     |       |       |
| CAPSleep[82](Sleepstageclassification-multiclass)    |     |       |     |       | train |
| HMC[88](Sleepstageclassification-multiclass)         |     |       |     | eval# | train |
| SRM[89](RestingstateEEGdata)                         |     |       |     |       | train |
| Schizophrenia-81(Schizophreniaclassification-binary) |     |       |     |       | train |
| Stroke-50[90](Handmovementclassification-binary)     |     |       |     |       | train |
train
PD-31[91](Parkinsondiseaseclassification-binary)
| IowaDataset[92](Unknowntask/s)                        |     |       |     |     | train |
| ----------------------------------------------------- | --- | ----- | --- | --- | ----- |
| UNMDataset[93](Parkinsondiseaseclassification-binary) |     |       |     |     | train |
| AD-184[94](Alzheimer’sdiseaseclassification-binary)   |     |       |     |     | train |
| Neonatedataset[95](Seizuredetection-binary)           |     | eval# |     |     |       |
| IIICSeizure[96](IIICpatternclassification)-multiclass |     | eval# |     |     |       |
| Absence-16(Seizuretypeclassification-multiclass)      |     |       |     |     | eval# |
| Clonic-6(Seizuretypeclassification-multiclass)        |     |       |     |     | eval# |
eval#
Atonic-5(Seizuretypeclassification-multiclass)
| DRE-Clinical(Seizuredetectionandlocalization-binary) |     |     |     |     | eval# |
| ---------------------------------------------------- | --- | --- | --- | --- | ----- |
| SD-71[97](Sleepdeprivationdetection-binary)          |     |     |     |     | eval# |
| ADHD-Adult[98](ADHDclassification-binary)            |     |     |     |     | eval# |
| ADHD-Child[99](ADHDclassification-binary)            |     |     |     |     | eval# |
Schizophrenia-28[100](Schizophreniaclassification-binary) eval#
eval#
Depression-122[101](Depressionclassification-binary)
eval#
MDD-64[102](Majordepressiondetection-binary)
| AD-65[103](Alzheimer’sdiseaseclassification-binary) |     |     |     |     | eval# |
| --------------------------------------------------- | --- | --- | --- | --- | ----- |
BCICompetitionIV-1[104](Movementclassification-binary) train train
| Emobrain[105](Emotionclassification-multiclass) |     |     | train | train |     |
| ----------------------------------------------- | --- | --- | ----- | ----- | --- |
Grasp/LiftChallenge[106](Graspclassification/regression) train train
InriaBCIChallenge[107](Nextletterprediction-multiclass) train train
EEGMotorImagery[108](Classification-multiclass) train train train
VisualCategorizationEEG[109](Classification-multiclass) train train
Resting-stateEEG[110](Eyestateclassification-binary) train train
SEEDSeries[111–113](Emotionclassification-multiclass) train/eval∗ train/eval∗ train/eval∗
| SPISRestingStateEEG[114](CVSandHRTregression)    |       |     | train | train |     |
| ------------------------------------------------ | ----- | --- | ----- | ----- | --- |
| Brain-Invaders[115](Targetclassification-binary) |       |     | train | train |     |
| Multipledatasources[116–120](Unknowntasks)       |       |     | train | train |     |
| MoBI[121](Gaitangleregression)                   |       |     | eval# |       |     |
| BCICompetitionIVDataset2a[122]                   | eval# |     |       |       |     |
eval#
Workload[123](Workloadclassification-binary)
IntracranialEEG
BrainTreeBank[70](EEGclassification-multiclass) train/eval∗
| Privatesingledatasetwithoutsource(Unknown)     | train/eval∗ |     |     |     |       |
| ---------------------------------------------- | ----------- | --- | --- | --- | ----- |
| Privatedatasetcollectionwithoutsource(Unknown) |             |     |     |     | train |
MAYO[124](Pathologydetection&eventsclassification) eval# train/eval∗ eval#
FNUSA[124](Pathologydetection&eventsclassification) eval# train/eval∗ eval#
| CCEP[84](Seizureonsetzonelocalization-binary) |     |     |     |     | train |
| --------------------------------------------- | --- | --- | --- | --- | ----- |
11/35

omitspatialmodelingaltogether,usingonlytransformerlayerswithoutconvolutionorspatialpriors.
Self-supervision: SSLapproachesarekeycomponentsthatenablethedevelopmentoffoundationmodelsusing
massiveunlabeleddatasets[7]. MostEEG-FMs(sevenoutoften)employedreconstructionofmaskeddataasthe
primarySSLapproach. EEGFormermodelwaspretrainedbyminimizingthereconstructionlossbetweeninput
signalsandsignalsdecodedfromcodebookmappingsoftransformer-encodedinputpatches. NeuroLMemployedan
autoregressiveapproachtopredictfuturepatchesfrompastpatches,includinganEEG-textalignmentobjective,
andBIOTadoptedacontrastivelearningapproachwheretheembeddingsofmaskedinputsandthesameinputs
with different augmentations are minimized (i.e., the SimCLR [50] pretraining approach). Only one model —
Neuro-GPT—employedmaskeddatareconstructioninthelatentspace. Additionally,theLaBraMmodelemployed
a masked-signal reconstruction approach; however, the codebook embeddings of masked input patches from a
previouslytrainedneuraltokenizerwereusedasreconstructiontargets.
Masking: ThegranularityofthelearnedrepresentationsintheEEG-FMsisinfluencedbythetypeandextentof
maskingusedduringself-supervisedpretraining[126]. Inmodelsbasedonmasked-signalreconstruction,maskingis
typicallyappliedtorandompatchesacrosstemporalandspatialdimensions,asopposedtomaskingentirechannels
orfulltimesegments. Forexample,BrantandFoMEapplieda∼40%uniformrandommasking,zeroingoutthe
masked input signal patches across time and channel dimensions. LaBraM similarly utilized a 50% patch-level
masking,whileBrainWave,despiteoperatinginthespectrogramdomain,performedmaskingentirespectrogramsof
severalchannels. Ontheotherhand,BrainBERTappliedamorefine-grainedmaskingstrategy,masking5%from
thetimedomainand5%fromthefrequencydomain,effectivelymasking∼10%oftheinputspectrogram. Mentality
appliedrandomchannelmasking,targetingspecificchannelsratherthanpatches. NeuroLMintroducedastair-step
masking scheme, in which next token is auto-regressively predicted in a channel-conditioned manner, whereas
Neuro-GPTutilizedacausalmaskingapproachinthelatentspace,consistentwithautoregressivegeneration.
Model scale: The number of trainable parameters (or weights) varied significantly between the ten EEG-FMs,
ranging from 3.3M in BIOT to 1.7B in NeuroLM, although most models fall within the 200-500M parameter
range. SomeEEG-FMs,suchasFoME,LaBraM,andNeuroLM,weredevelopedatmultiplescaleswiththesame
architecture,allowinguserstochooseamodelscaleaccordingtotheirspecificresourceconstraints.
4.3 Model Evaluations
Downstreamtaskevaluations: Performanceondownstreamtaskspost-adaptationwastheprimarymetricusedfor
evaluationinalltheEEG-FMs. However,theclinicalandnon-clinicaldownstreamtasksusedforevaluationandthe
adaptationtechniquesvariedsignificantlybetweenthem. ThevariousdatasetsusedforevaluationareshowninTable
2. WhilemostEEG-FMevaluationswererestrictedtoeitherscalporintracranialEEG,twomodels,namelyFoME
andBrainWave,wereevaluatedonbothmodalities. Furthermore,mostFMsusedcommonadaptationtechniques,
namelylinearprobingandfine-tuning,whilesomeusedprototype-basedfew-shotevaluationandinstructiontuning.
AlmostallEEG-FMs,exceptMentality,investigatedfine-tuningfordownstreamtaskevaluations,inwhichthe
pretexttaskdecoderisdiscardedbuttheencoderistrainedfurtherusingtask-specificlabels. Ontheotherhand,
fiveEEG-FMs(i.e.,Brant,BrainBERT,LaBraM,EEGFormer,andNeuro-GPT)evaluatedlinearprobing,where
theencoderistypicallyfrozen,andadditionaltask-specificheadsontopoftheencoderaretrainedusinglabeled
downstreamdata. TheBrainWavemodelwasevaluatedusingaprototype-basedfew-shotlearningapproach,where
classprototypeswerecreatedbyaveragingthelatentrepresentationsofafewexamplesperclass,anddownstream
classificationwasperformedbymeasuringsimilaritytothoseprototypesinthelearnedlatentspace. Furthermore,
NeuroLM, which was pretrained with an EEG-text alignment objective, was evaluated using a text-prompting
approach. Themodelwasfine-tuned(instruction-tuned)usinganauto-regressivepredictiontaskutilizingEEG-text
combined tokens, where the text tokens contained both class prompts and labels. Subsequently, the model was
evaluatedonvarioustasksbyprovidingqueriescontainingEEGtokensandprompts,forwhichthemodelpredicted
theclasslabels. Inthefollowing,webrieflysummarizetheevaluationsperformedbyeachEEG-FMandtheresults.
BrainBERT: This model was trained and evaluated on the same intracranial EEG dataset, Brain TreeBank. The
downstreamtaskfocusedonpredictingthefeaturesofthemoviesthatthesubjectswerewatchingduringtheEEG
recording. Fine-tuningthepretrainedBrainBERTmodelonthistasksubstantiallyoutperformedfully-supervised
12/35

linearandmulti-layerneuralnetworkmodels. LinearprobingalsoachievedAreaUndertheReceiverOperating
CharacteristicCurve(AUC)valuessimilartothoseofthefullysupervisedmodels.
Neuro-GPT: ThismodelwasevaluatedonasinglescalpEEGdatasetthatwasnotusedduringpretraining,with
thedownstreamtaskbeing4-classmotor-imageryclassification. Thefully-supervisedbaselinesconsideredinthis
studyincludeBENDR[127],SVM[128],EEGNet[78],CTCNN[129],CCNN[130],andNG-CRAM[131]. When
usedinasupervisedsettingwithoutanypretraining,thismodelperformedsimilarlytoothersupervisedbaselines.
However,whenthepretrainedmodelwasfine-tunedforthedownstreamtask,itprovidedsignificantimprovements
incertainconfigurations. Incontrast,linearprobingperformedworsethanfully-supervisedbaselines.
Brant: ThismodelwasevaluatedonthreeunseenintracranialEEGdatasets,includingoneprivateandtwopublic
datasets (MAYO and FNUSA). The downstream tasks evaluated include signal forecasting, imputation, seizure
detection,andpathologydetection. Forallthesetasks,thepretrainedmodelwasfine-tunedorlinear-probedusingtask
labels. Theself-supervisedpretrainedbaselinesconsideredinthisstudyincluded(RP,TS,CPC)[6],BENDR[127],
MVTS[132],andBrainBERTthataredesignedforbrainsignals,andCoST[133],TF-C[134],PatchTST[135],
TS-TCC[136]thataredesignedforgeneraltimeseries. Fully-supervisedbaselineswithoutanypretrainingincluded
handcraftedfeatures-basedmethodssuchasspectralpower[137],rhythmicityspectrogram[138],andamplitude-
integrated EEG [139] along with SEEG-Net [140]. In signal forecasting and imputation tasks, fine-tuned Brant
consistentlyoutperformedseveraltimeseriesbaselinesanditsownlinearprobingversion. Intheseizuredetection
andpathologydetectiontasks,boththefine-tunedandlinearprobedversionsofBrantoutperformedothersupervised
andEEG-FMbaselines,includingBrainBERT.Theseobservationsheldtrueinlow-labeledsettingsaswell.
BIOT: ThismodelwasevaluatedentirelyonscalpEEGdatasetsonvariousclinicaltasks. Thesupervisedbaselines
consideredinthisstudyincludedSPaRCNet[141],ContraWR[142],CNN-Transformer[143],FFCL[144],ST-
Transformer [145]. Evaluations showed that the finetuned BIOT encoder outperformed several fully-supervised
baselinesinCHB-MITseizuredetectionandTUABnormal/abnormalclassification. Intwoothertasks,namelyIIIC
seizureclassificationandTUEVeventclassification,boththevanillauntrainedBIOTinthefullysupervisedsetting
andthepretrainedBIOTmodelinthefine-tuningsettingoutperformedallsupervisedbaselines.
EEGFormer: The three variants of EEGFormer were evaluated against four fully-supervised models (i.e., EEG-
Net[78],TCN[146],EEG-GNN[147],andGraphS4mer[148])andBrainBERTasbaselines,usingfivedifferent
scalpEEGdatasets/tasks. Fine-tunedEEGFormeroutperformedallbaselinesinallthetasksexceptone,where
its performance was marginally lower than EEG-GNN. Their evaluations also showed that a smaller version of
EEGFormerdemonstratedlessvariabilityinsomedownstreamevaluations.
LaBraM: This model was evaluated on four scalp EEG datasets: two clinical (TUAB and TUEV) and two non-
clinical(SEED-VandMoBI),withMoBIastheonlyexternaldataset. Theevaluationsconsideredseveralsupervised
models,SPaRCNet[141],ContraWR[142],CNN-Transformer[143],FFCL[144],ST-Transformer[145],andBIOT
asbaselines. AllvariationsofLaBraM(base,large,andhuge)withfine-tuningoutperformedbaselinesinalltasks.
Mentality: ThismodelwasevaluatedontheTUSZseizuredetectiondataset,whichwasalsousedforpretraining.
The evaluation compared an untrained Mentality model trained in a fully supervised setting with a pretrained
Mentalitymodellinearlyprobedwithtwolinearlayers,showingthatpretrainingisbeneficialforthistask.
NeuroLM: This model was fine-tuned jointly on six tasks and was compared against seven baselines fine-tuned
individually per task. The evaluations considered supervised models SPaRCNet [141], ContraWR [142], CNN-
Transformer [143], FFCL [144], ST-Transformer [145], BIOT, and LaBraM as baselines. Evaluations showed
thatjointfine-tuningwithpromptingisfeasibleandachievesreasonableperformanceacrossalltasks. However,
NeuroLMdidnotperformaswellastheLaBraMmodelonanyofthetasks,whereLaBraMwasfine-tunedseparately
foreachtask. EvaluationsshowedthattheTUABandTUEVperformanceofNeuroLMvariantswasnotsensitiveto
modelsize,whereastheperformanceonHMCandWorkloadtasksdecreasedwithlargervariants.
FoME: This model was evaluated on 7 tasks across 4 datasets (MAYO, FNUSA, SEED, SleepEDFx), and eval-
uationsconsideredseveralfully-supervisedmodels(LSTM[149],ConvNeXt[150]),generaltimeseriesmodels
(PatchTST,TimesNet),andsomeEEG-FMs(BrainBERT,Neuro-GPT,LaBraM)asbaselines. Evaluationsshowed
that,inemotionclassification,sleepstaging,eventsclassification,andpathologydetectiontasks,FoMEperformed
competitivelyorbetterthanallbaselines,whereasitsperformancewassignificantlybetterinsignalforecastingtasks.
13/35

Interestingly,theevaluationsalsodemonstratedthatgeneraltime-seriesmodels,suchasPatchTSTandTimesNet,
performreasonablywellonpathologydetectionafterfine-tuning,despitenotbeingpretrainedonbrainsignals.
BrainWave: This model was evaluated using multiple scalp and intracranial EEG datasets and was compared
againstLaBraM–ascalp-EEG-FM,BrainBERT–anintracranialEEG-FM,andMOMENT[151]–ageneraltime
series FM. Evaluations considered different criteria, including class prototype-based few-shot classification and
cross-domain transfer learning across subjects, sites, and diagnostic subtypes. Results showed that BrainWave
significantlyoutperformedallthebaselinesinallsettings,withanaverageimprovementof0.21AUCpointsacross
12tasks,establishingitssuperiorityinchallengingout-of-distributionevaluations.
Evaluationsoncommontasks: Weobservedthattwodatasets,TUABforabnormalEEGclassification(twoclasses)
andTUEVforEEGeventdetection(sixclasses),havebeenwidelyutilizedfordownstreamevaluation. Notethat
both TUAB and TUEV are scalp EEG datasets derived from the larger TUH EEG corpus. In Figure 3a-3b, we
comparetheperformancesreportedonthesecommontasks. Wealsoanalyzedtheimpactofthepretrainingdatasize
onthex-axis. Forcomparison,weuseAUCandF1scoresasperformancemetrics,astheyarethemostcommonly
reportedmetricsforthesetwotasks. LinearprobingresultswereavailableonlyinLaBraMandareindicatedbya
triangleinthefigure. Theremainingresultsarebasedonfine-tuningexperimentsconductedbyLaBraM,NeuroLM,
EEGFormer,andBIOT.WefindthatAUCvaluesranged0.86−0.92forTUABabnormalEEGclassificationand
F1-scoresranged0.70−0.83forTUEVeventclassification,highlightingsignificantperformancevariationacross
models. Thesecomparisonsalsosuggestedthatincreasingthesizeofthepretrainingdatasetdidnotnecessarily
improvemodelperformanceonthesetwotasks.
(a)TUAB:normalvs. abnormalclassification. (b)TUEV:six-classeventclassification.
Figure3. Performancesoncommontasks. HerewecompareEEGfoundationmodelsbasedontheirperformance
onthecommonTempleUniversityEEGCorpustasks–TUAB(abnormalEEGclassification)andTUEV(event
classification)–alongwiththesizeofthedatasetusedforpretraining. TheperformanceofFoMEin3bisshown
asalinebecausethepretrainingdatasizewasunavailable. Channel-hoursareona103 scale. Allscoresrepresent
fine-tunedmodelperformance,exceptforthetriangularmarkers,whichrepresentlinear-probedmodelperformance.
Apart from downstream task evaluations, some models performed additional evaluations focused on model
interpretability,pretrainingquality,andablations. Webrieflysummarizethoseevaluationsbelow.
Interpretabilityanalyses: AnanalysisperformedinBrainBERTusedtheintrinsicdimensionality(ID)measureto
assesstask-specificembeddingspost-finetuning. IDisageometricmeasurethatquantifiestheminimumnumberof
parametersrequiredtorepresentembeddings[71]. Theyshowedthat,intheirmodel,theelectrodeIDdistributionlies
inalower-dimensionalspacecomparedtoarandomlyinitializedmodel. Furthermore,theyshowedthatelectrodesin
thetop10thpercentileofIDsmainlyfallinbrainregionsassociatedwiththetask. Similarly,EEGFormer,oneofthe
threemodelsthatutilizedavectorquantizertotrainaneuralcodebook,analyzedthelearnedcodebooktoattribute
14/35

partsoftheinputEEGdatatodownstreamtaskpredictions. Intheiranalysis,codesmostlikelytopredictseizures
weremappedbacktotheEEGtracestovisualizewherethemodelfocused. Thesehighlightedregionscorresponded
toknownepileptiformpatterns,indicatingthatthemodel’sdecisionsalignedwithmeaningfulclinicalmarkers.
Pretrainingquality: Somemodelsevaluatedpretrainingqualitythroughqualitativeandquantitativeassessments.
Most qualitative assessments were based on visualizations of data reconstructed by the specific models, which
wereruninMentality,LaBraM,andBrainBERT.Quantitativeassessmentsfocusedonreconstructionerror(e.g.,
Mentality)andperformanceonforecastingandimputationtasks(e.g.,Brant,FoME).
Ablations: Fewmodelsevaluatedthecontributionsofvariousmodelcomponentsordatasetstotaskperformance
via ablations. An experiment in Neuro-GPT, which combined a convolutional transformer and a GPT decoder,
showedthatremovingtheGPTdecodersignificantlyimproveddownstreamperformance. ExperimentsinBrant
evaluatedthecontributionsoftemporal,spatial,andfrequencyencodersanddemonstratedthat,whileallcomponents
werevaluableforlearningEEGrepresentations,thetemporalencodermadethegreatestcontribution. Additionally,
LaBraMshowedthatspatialembeddingsarecrucialforpretrainingtoconvergeandfordownstreamperformance.
Furthermore, LaBraM studied the effect of the codebook during pretraining by replacing the neural tokenizer
withtraditionaltime-andfrequency-domainmaskedreconstructionandshowedthatthisdegradedperformance
for complex downstream tasks such as TUEV. NeuroLM showed that different neural tokenizer training tasks
(frequencyvs. temporalvs. frequencyandtemporalreconstruction)canbebeneficialfordifferentdownstreamtasks.
Additionally,NeuroLMexaminedtheimpactofmodelpretrainingdurationbyfine-tuningdifferentcheckpoints,but
theresultswereinconclusive. AnexperimentinBrainWaveperformeddataablationbytrainingseparatemodelswith
scalpandintracranialEEGandcomparedtheirperformancewithjointscalp-iEEGtraining. Theirresultsindicated
thatjointtraininggenerallyimproveddownstreamperformanceinalltasks,exceptone.
5 Key Takeaways and Research Gaps
This section presents several key observations made across the preceding comparative analyses (Section 4) and
highlightstheresearchgapsthatremain. WebelievethataddressingthesegapswouldmakefutureEEG-FMsmore
principledintheirmethodologyandtrustworthyforscientificandclinicalinvestigations.
5.1 Key Takeaways
Diversity of pretraining data: Several EEG-FMs (LaBraM, NeuroLM, FoME, and BrainWave) leveraged a
diversesetofEEGdomainsspanningclinical,sleep,andtask-basedBCI.Notwithstandingpotentialconfounders
such as preprocessing, data splits, and model adaptation strategies, LaBraM’s lead in the TUAB and TUEV
evaluations(Figure3)mayhaveemergedfromitshigherdiversityinpretrainingdata,i.e.,thenumberofdistinct
datasources,comparedtoEEGFormerandBIOT.LaBraMalsoperformedcompetitivelyinseizuredetectionand
eventsclassificationtasksontheMAYOandFNUSAdatasetsasreportedinFoME’sevaluations. NotethatLaBraM
waspretrainedonsignificantlyfewerchannel-hoursofscalpEEGdataandwhileTUABandTUEVevaluationsare
bothin-distributionassessments,MAYO-FNUSAevaluationsarebothiEEGdatasets. Themixeduseofscalpand
iEEG,asdoneinFoMEandBrainWave,canbeconsideredasanotherformofdatadiversity. Usingdataablations
(scalp EEG vs. iEEG), BrainWave demonstrated that joint pretraining (scalp EEG + iEEG) boosts downstream
taskperformanceandtransfertounseendatatypes(electrocardiograms). Overall,thenotionofdatadiversity,in
conjunctionwithdatavolume,mayinfluencetheperformance,generalizability,andtransferabilityofEEG-FMs.
Minimal data preprocessing: Most EEG-FMs perform minimal and simple data preprocessing steps, namely
filteringandresampling,tostandardizeEEGsfromvarioussources. Notably,theremovalofnoise-relatedoutliers,
suppressionofEEGartifacts,andsite-relatedharmonizationwerenotexplicitlypursued. Moreover,datanormal-
izationstrategiesthatproducetraining-readysampleswerenotsufficientlydescribedinmoststudies. Itremains
unclearwhetherorhowvariousofflinedatahandlingstrategiesimpactEEG-FMpretraininganddownstreamtask
performance,particularlywithout-of-distributiontestdata.
MultivariatetimeseriesEEGrepresentation: AllbutfourEEG-FMsutilizedthenativemultivariatetimeseries
representationofEEG,whiletwomodelsutilizedthespectralrepresentations. Twoothermodelscombinedtime-
seriesandspectralrepresentationsasinput,whiletheremainingtwomodelsexclusivelyadoptedtime-frequency
15/35

(a)Impactofprogressivelearningparadigms(A→D)ondownstreamEEGclassifications.
(b)Modelscalingandperformancegains.
Figure 4. Theimpactoflearningparadigmandmodelscalingontaskperformance. In4a,wecomparethe
impact of learning paradigms – feature-based statistical machine learning (ML), supervised deep learning, and
self-supervised pretraining (proposed EEG-FMs and other baselines) – on task performance. For each model, a
specifictaskisrepresentedusingauniquecolor,andfinetuningandlinear-probingevaluationsarerepresentedusing
⃝and△, respectively. Notethatdownstreamtasksandthemetricsdifferacrossmodels. In4b, weanalyzethe
impactofmodelscalingontaskperformance. Althoughmodelsizesarespecifictoeachstudy,weuse‘Sm.’,‘Md.’,
‘Lg.’,torepresentthesmallest,intermediate,andthelargestvariants,respectively. Withineachmodel,aspecifictask
isrepresentedusingauniquecolor.
representations. Subsequently,therespectiveEEGinputswerepositionallyencodedwiththeirspatialandtemporal
order. Due to a lack of shared downstream evaluations and ablation studies, it is difficult to assess the relative
contributions of different EEG input representations and spatial positional encoding schemes. Furthermore, the
context length of the EEG-FMs did not exceed 90 seconds (FoME), and as such, they may struggle to capture
long-rangeEEGpatterns,relationships,ordependencies.
Temporalsequencemodeling: Sequence-basedtransformerblocksweretheprimaryworkhorseofrepresentation
learninginmostEEG-FMs,withtheexceptionofMentality,whichwasbasedonaMamba-basedarchitecture. Afew
models(NeuroLM,Neuro-GPT)utilizedconvolutionstocapturelow-levelmorphologicalfeaturesoftime-domain
EEG.However,themodelingofspatialEEGrelationshipswaseitherignoredorlimitedtothepositionalencoding
step. BrainWave, a notable exception in this trend, integrated a spatial attention mechanism. Supporting such
emphasisontemporalmodeling,theablationexperimentsinBrantshowedthattheirtemporalencoderprovidedthe
largestcontributiontodownstreamtaskperformance,comparedtothespatialencoderandfrequencyencoding.
Pretrainingusingmaskedreconstruction: ReconstructionofmaskedtemporalEEGsequenceswasthepredomi-
16/35

nantEEG-FMpretrainingparadigm,albeitwithvaryingstrategiesformaskingofsequencetokens/patches. Despite
itsoriginsinvisionandlanguagedomains,thisSSLstrategyseeminglyholdsmeritintheEEGdomain. However,
thegeneralizabilityofrepresentationslearnedduringpretrainingisgenerallyunclearsincemostevaluationswere
performed after fine-tuningon downstream data. In addition, several studies (LaBraM, NeuroLM, EEGFormer)
employedalearneddiscreteneuralcodebooktofurtherfacilitatethepretrainingprocess. Inauxiliaryefforts,this
codebookcansupportinterpretability(EEGFormer)andinterfacewithdiscretelanguagevocabularies(NeuroLM).
Limitedmodelevaluations: Taskperformanceafterfine-tuningwastheprimaryparadigmofEEG-FMevaluation.
However, in four of the ten reviewed studies (BrainBERT, Mentality, NeuroLM, and FoME), the downstream
evaluationdatasetswerealreadyusedforpretraining,i.e.,theevaluationswerein-distribution. However,notably,
BrainWaveandBrantaretheonlystudiestohaveperformedout-of-distributionevaluationsusingunseendatasets
(seeSupplementaryTable2). DirectmodelrankingsbeyondtheTUABandTUEVtasksaredifficulttodetermine
duetoheterogeneousselectionsofdownstreamtasksacrossmostEEG-FMs(seeTable2). Evenwhenconsidering
theTUABandTUEVtasks,onlyfouroutofthetenEEG-FMscanberanked,asdepictedonthey-axisinFigures
3aand3b,respectively. Inaddition,linearprobingandfew-shotevaluationswererarelyreported(seeFig. 4aand
SupplementaryTable2,respectively). Overall,thenumberofmeaningfulEEGclassificationtasksevaluatedineach
studyrangedfrom1(Mentality)to12(BrainWave),withmoststudiesevaluatingproposedEEG-FMsonatmost
5tasks. Overall,theuniversalityandrobustnessofEEG-FMshavenotbeenconvincinglydemonstratedinmost
studies,withBrainWavebeinganotableexception.
Modelscalingandtaskperformance: InFigure4b,weanalyzetheimpactofmodelscalingontaskperformance
using studies with at least two model variants. Each line plot indicates a specific downstream task and the x-
axis shows model variants, which were typically classified as small, intermediate, and large. Some marginal
improvementscanbeobservedforcertaintasksandmodels,althoughthesevariantsweredevelopedwithafixed
amount of pretraining data and were evaluated within study-specific experimental and methodological contexts.
Notably,LaBraMinvestigatedthecombinedeffectsofpretrainingdataandmodelscaleondownstreamTUAB/TUEV
classifications. Overall,itisunclearwhetheraclearandstrongtrendexistswithmodelscaling,especiallywithinthe
currentEEG-FMparameterregimerangingfrom3.3M(BIOT)to1.7B(NeuroLM,largestvariant).
Performanceofgeneral-purposetimeseriesmodels: Interestingly,weobservedthatgeneraltimeseriesfoundation
models,suchasTimesNet[152],performedreasonablywellonseveralEEGtasksafterfine-tuningandsometimes
outperformedEEG-FMs(e.g.,sleep-stageclassificationinFoME).Additionally,experimentsinBrainWaveshow
thatatimeseriesFM–MOMENT[151]–outperformedEEG-FMsinspecifictasks,suchasseizuredetectionand
pathology detection. Experiments in Brant show that general time series architectures, such as PatchTST [153]
and CoST [133], perform relatively better on some tasks, such as short- and long-term signal forecasting and
imputation, respectively, than some EEG-specific architectures. However, other results reported in BrainWave
and FoME suggest that EEG-specific inductive biases and modeling choices (e.g., spatial modeling, multi-scale
modelingofintracranialandscalpdata,time-frequencyrepresentations,diverseclinicalcharacteristics)canindeed
helpEEG-FMsoutperformgeneraltime-seriesFMs(TS-FMs)inEEG-specifictasks. Overall,thesefindingsindicate
thatTS-FMsmayprovidemoderatevalueincertainEEGtasksduetoefficientmodeladaptationviafine-tuningor
larger-scalegeneralpretrainingontimeseriescontainingricherandmorediversesemanticsthanEEG.
Data scaling and task performance: The trend along the x-axis of Figures 3a and 3b suggests that scaling up
pretrainingdatamaynotnecessarilyincreasedownstreamtaskperformance,evenwithsignificantmodelscale-up
(e.g.,LaBraMvs. EEGFormer/NeuroLM).Notably,LaBraMdemonstratedthattheeffectsofpretrainingdatascaling
onTUABandTUEVclassificationsaresharpestunder∼1000hoursofdataandbegintoplateauthereafter. Overall,
theevidencefordatascalingisweak,ifany,basedonthelimitedsharedtasksandmodelsevaluatedthusfar.
Advance over other feature paradigms: In Figure 4a, we compare progressive feature paradigms (i.e., expert
features,supervisedEEG-DLfeatures,SSLbaselines,andproposedEEG-FMs)onvarioustasks. Inamajorityof
tasks,proposedEEG-FMs(‘D’)providedatleastsomeimprovementafterfine-tuning,ifnotdrastic,overprevious
DL(‘B’)andself-supervisedbaselines,includingpreviousEEG-FMs(‘C’).Linearprobingresults,however,were
relatively worse. Fine-tuned EEG-FMs showed substantial improvements over classical machine learning (ML)
modelswithexpertfeatures(‘A’),althoughsuchassessmentswerereportedinonlyfourstudies.
17/35

5.2 Current Research Gaps
Dataandmodelscaling: Thescalingupofdataandmodelsisadefiningprincipleoffoundationmodeling. However,
empiricalevidenceofscalinginEEG-FMshasbeeneitherweak,limited,orinconclusive. Investigationsthatscale
updatavolume(channel-hours),modelsize(trainableparameters),andevaluateonanexpansivesetofdownstream
tasksarelackingincurrentEEG-FMs,particularlyatsufficientlylargescaleswhereeffectsareclearanddiscernible.
Preprocessingandnormalizationeffects: EEGdatasetscanrequiresignificantofflinepreprocessingtomanage
dataqualityandsuppressartifacts. Sincecurrentstudiesperformminimalprocessing,itisunclearwhetherortowhat
extentdataoutliersandnoiseimpactEEG-FMpretrainingandtaskperformance. EvencleanEEGdatasetsrequire
carefulconsiderationofnormalizationstrategiesasEEGcanvaryacrosschannels,subjects,andacquisitionsites[5].
Thechoiceofinputrepresentationcanfurthercomplicatedecisionsrelatedtopreprocessingandnormalization. As
such,thereisaneedtobetterunderstandtheimpactofthesechoicesondownstreamEEG-FMmodeling.
Model ablations: EEG-FM design involves two significant choices: the input representations and the internal
architecturalcomponents. However,thelackofsystematicexplorationoftheeffectsofthesechoicesinexisting
EEG-FMliteraturepreventsprincipledchoicesinEEG-FMdesign. Therelativemeritsoftime-domainandtime-
frequency domain inputs remain unclear, although both appear to be effective. The contributions of positional
encodingschemes,bothtemporalandspatial,canbebetterunderstood. Similarly,theeffectsoftime-domainand
channel-domainspatialattentionmechanismsonlearnedpatternsremainpoorlyunderstood.
Longtemporalcontextandspatialmodeling: Slowvariationsoverlongtimescalescanbeobservedinmulti-day
intracranialandscalpEEGs[154]. Additionally,thereissubstantialspatialandtemporalvariationinEEGacross
behavioralstates(e.g.,deepsleepversuswake,eyesopenversuseyesclosed). However,currentEEG-FMscanonly
processpatternswithinEEGsequencesspanning90secondsorless. Thereisaneedforsolutionsthatexpandthe
effectivecontextlengthofEEG-FMs. Moreover,theexplicitmodelingofspatialorinter-channelrelationshipsand
theircontributionsrelativetotemporalmodelingremainstobeinvestigated.
Qualityofpretrainingstrategy: EEG-FMlinearprobingevaluationsreportedbysomestudieshaveperformed
significantlyworsethanfine-tunedversionsandotherbaselinesinseveralinstances(seeFigure4a). However,some
gains can be observed when FMs are fine-tuned on task data compared to fully supervised training on the same
data. Thiscontrastingobservationcastsdoubtonthequalityoftherepresentationslearnedviaself-supervisionin
EEG-FMs. FurtherinvestigationsintotheeffectsofSSLpretrainingondownstreamevaluationsareneededtofully
understandtheextentoftransferabilityachievedthroughSSL.BeyondtheSSLstrategyitself,theeffectsofdata
diversity,datavolume,andmodelscaleonthequalityofEEG-FMpretrainingremainunknown.
Practically relevant evaluations and metrics: Current fine-tuning evaluations are limited in their ability to
assess the practical utility of EEG-FMs in real-world settings. There is a need to adopt evaluation schemes and
task metrics that capture the reality of EEG research and clinical use. Evaluations on out-of-distribution data
and novel tasks are required to assess the off-the-shelf value of EEG-FMs. Few-shot or low-label performance,
whenmeasuredinabsolutetermsratherthanpercentages,cancapturehowefficientlyEEG-FMsleveragelabels
that are typically expensive and laborious to collect. Out-of-distribution performance on a known task without
fine-tuningcanhelpunderstandEEG-FMrobustnesstotheidiosyncraticcross-subjectandcross-sitevariabilityof
EEG. Furthermore, application-specific, practically relevant metrics, such as false positives per hour for seizure
detection,andcomparisonswithexpertfeaturescanclarifythereal-worldutilityofEEG-FMs. Finally,evaluations
must account for the unbalanced nature of physiological data and its influence on metrics and model outcomes.
Forexample,inseizuredetectionsettings,patientdataconsistsmostlyofinterictalsegments,withseizureevents
occurringrarely. Evaluationsmustreflectthisnaturalimbalancetoassessthemodel’sreal-worldutilityfaithfully.
Standardizedbenchmarkingtasks: Thecomparativeanalysisrevealedsignificantheterogeneityinthetasksused
forEEG-FMevaluation(seeTable2). ThelackofcommontasksacrossEEG-FMevaluationsmakesitchallenging
tounderstandthestateoftheartandhighlightstheneedtoidentifyacommoncoresetofevaluationsforfuture
EEG-FMdevelopment. Thissetmustcovermultipletasktypesandincludebothclassificationandregressiontasks,
withdense(onelabelperEEGrecording)andsparse(onelabelperEEGsegment)labels. Additionally,thetasks
mustbechallengingenoughforpreviousgenerationsofEEG-DLmodels,withampleroomforimprovement,unlike
TUAB,whereperformancemayalreadyhavesaturated(85-87%accuracy)withtraditionalapproaches[155]. Finally,
18/35

thetasksmustreflectthedataheterogeneityencounteredinclinicalsettings,includingwakeandsleeppatientstates.
Trustworthymodeling: Despitetheimportanceofexplainabilityanduncertaintyhandlinginthehigh-risk,expert-
centricdomainofmedicine, experimentsprobingtrust-relatedaspectsofEEG-FMshavebeenlimited. Notably,
preliminaryinterpretabilityanalysesbasedonintrinsicdimensionalityandcodebookswereconductedforBrainBERT
andEEGFormer,respectively. However,studiesthatfurtherdemystifytheEEG-FMblackboxareneededtogain
insight into the knowledge learned by EEG-FMs (EEG patterns, dependencies, relationships) and the practical
robustnessoftheirdecision-makingprocessfordownstreamapplications. Connectionstoknownpatternsofbrain
physiologyorpathologymaybenecessarytomakeEEG-FMstrustworthyintheeyesofexpertandclinicalusers.
6 Proposed Future Directions
Fromatimeseriesperspective,EEGsignalsaredistinctfromgeneralsignalsorsequencesduetotheirnon-linearity
[156],non-stationarity[156],complexspatialrelationships,and1/fspectralcharacteristics[157]. Thesepeculiarities
would suggest that foundation modeling for EEG signals requires domain-specific inductive biases. Indeed, we
havecultivatedanEEGdata-centricanddomain-sensitiveperspectivethroughoutthisreview. However,counter-
intuitively,EEG-FMshaveenjoyedsomesuccessindrawingfromvisionandlanguagedomainsintheiradoption
ofpatch-basedsequencesandtransformerarchitecturedesign(transformer[47],visiontransformer[64]),masked
reconstruction-based SSL (masked autoencoders [126]), and discrete neural codebooks (VQ-VAE [125], BEiT
v2[158]). Moreover, timeseriesFMspretrainedongeneric, non-neuraltimeserieshaveperformedsimilarlyto
EEG-FMsoncertainEEGtasks. Therefore,itislikelythatfutureEEG-FMscouldbenefitfromembracingboth
domain-specificinsightsandinnovationsfromexternaldatadomains. Thesedomainsmaybesemanticallydistantto
EEG,suchasvisionandnaturallanguage,orlooselyrelated,suchasnon-neuraltimeseries,audio,speech,orother
biosignals. Below,weoutlinethefutureresearchdirectionsthatwebelievecouldsupportmeaningfulandsustained
progressintheEEG-FMresearchdomain. AsillustratedinFigure5,theserecommendationsareorganizedunder
threebroadthemesofdevelopmentspanningbenchmarksandsoftwaretools,technicaladvances,andreal-world
applications. Thesesuggestionsbuildupontheresearchgapsidentifiedearlierandprovideadditionalguidancefor
advancingandacceleratingEEG-FMresearchandadoption.
Figure5. Suggestedfuturedirections. (I)Benchmarksandtools:futureEEGfoundationmodelscanbecompared
usingstandardizedbenchmarksagainstprevailingfeatureparadigmsandparticipateincommunity-specificEEG
challengestoestablishtheirreal-worldutility. Frictionlessanduser-friendlysoftwaretoolsareneededtoquickly
adoptandexperimentwithoff-the-shelfmodels. (II)Technicalmodeling:holisticevaluationframeworksthattest
embeddingspacesemantics,robustness,andtransferefficiencycanmeaningfullytrackthestateoftheart. Advanced
representationlearningtechniques,suchasfederatedormulti-modallearning,canenhancelarge-scalepretraining.
(III)Applications:collaborationswithdomainexpertscaninspirenovelapplications. Strategiesthathelpidentify
suitableoff-the-shelfmodelsforaparticulartaskandaddresstranslationalhurdles,suchasclinicalinterpretability,
prospectivevalidation,andoperationalfeasibility,canincreaseadoptionandimpact.
19/35

6.1 Benchmarks and Tools
Benchmarking against prevailing feature paradigms: Quantitative EEG research currently employs two ML
featureparadigms: expert-crafted EEGfeatures andtask-specificsupervised features. Assuch, data-driven self-
supervisedfeatures,suchasthoseprovidedbyEEG-FMs,remainintheirinfancy. Therefore,toestablishacompelling
case for EEG-FM adoption, studies proposing novel EEG-FMs should evaluate against the prevailing feature
paradigms. Indoingso,statisticaltestsofsuperiorperformancemustbepresentedwhennecessary. Additionally,
identicalsubject-levelsplitsmustbeusedtocontrolforinter-subjectvariability,andtemporalpast/futuresplitsmust
beusedtoaccountforthetemporalorderofeventsinlonger-termEEGdata.
Standardizedcommunity-specificbenchmarks: TheprimaryfailuremodeofEEGencodersremainstheirinability
tolearnrobustlatentfeaturesthatgeneralizeacrossrealisticEEGdistributionshifts,includingthoseseenacross
subjects,agegroups,acquisitionsetups,andexperimentalorclinicalconditions,amongotherfactors. However,each
EEGusercommunity(e.g.,clinicians,braincomputerinterfaceusers,neuroscientists)mayhavedifferentpractical
requirementsordefinitionsofmodelrobustnessandgeneralization. Therefore,futureworkcandesigncommunity-
specificEEG-FMbenchmarkswithcleartaskdefinitions,realisticperformancecriteriabeyondtraditionalmetrics,
real-world datasets, and expert baselines. In doing so, EEG researchers can draw inspiration from existing FM
benchmarksinotherdatadomains. Standardizedbenchmarkstailoredtoeachcommunity’sneedscansignificantly
boostthechancesofreal-worldtranslationandadoptionofEEG-FMs.
Ranking EEG-FMs in global EEG competitions: Novel EEG-FM methodology can leverage international
predictivemodelingcompetitionstoestablishreal-worldperformanceandutility,asthosecompetitionscanhighlight
the most significant empirical challenges or milestones within the field. Such competitions have already been
developed for time series [159], electrocardiograms [160], and speech [161] domains. Notably, within the EEG
domain, previous competitions have highlighted issues with transfer learning under distribution shifts [162],
abnormalitydetection[163],comaprognosis[164],seizuredetection[165],andseizureforecasting[166].
Frictionlesssoftware: Severalsoftwaremodificationsandcodedebuggingarerequiredtorunthecurrentlyavailable
EEG-FMs. ThedeeptechnicalnatureofEEG-FMsandthecomputingskillsrequiredtorunthesemodelsposea
significantentrybarrierfornon-technicalornon-computationalresearchers. Futurestudieswillneedtoensurethat
EEG-FMscanbeusedasoff-the-shelffeature-extractiontools,withnotechnicalmodificationsrequired. Graphical
softwareforplug-and-playEEG-FManalytics,suchassimplebinaryclassifications,cangreatlyincreasereal-world
EEG-FMadoption,testing,andexperimentation. Encouragingly,amatureecosystemforlarge-scaleEEGanalytics
alreadyexistsinPython[167–169]andcansupportthedevelopmentoffrictionlessEEG-FMsoftware.
6.2 Technical Development
Holisticevaluationschemes: Futurestudiesmaybenefitfromfocusingspecificallyonout-of-distributionevalua-
tions,astheycandirectlyassesstheeffectivenessofEEG-FMpretrainingandperformanceinrealistic,off-the-shelf,
and low-label scenarios. Furthermore, evaluating EEG-FMs based on their task performance on a narrow set of
commonlyavailableEEGdatasets/tasksisinsufficienttomeasuretheirreal-worldreadiness. Novelevaluationand
modelrankingschemescanbedesignedtoassessthecomputationalcosts,semanticEEG-FMembeddingquality,
transferefficiency,androbustnesstoreal-worldEEGvariabilityandnoisesources.
Privacy-preserving learning: EEG datasets required for large-scale EEG-FM pretraining can be siloed due to
patientprivacyandlegalconcerns. Researchcollaborationsinvolvingmultipleclinicalsitescanutilizefederated
learning[170]techniquestotrainEEG-FMswithoutrequiringcentralizeddataaccessorsharing. Suchtechniques
mayalsosupportthederivationofpersonalized,i.e.,patient-specific,modelsfromEEG-FMs.
Multi-modallearning: Latentrepresentationslearnedduringpretrainingmaybenefitfromcross-modalsupervision
fromtextreports,videorecordings,orotherbiosignals,suchaselectrocardiograms. Someofthesemodalitiesare
jointlyrecordedwithEEGsinmanyclinicalandscientificrecordingsettings. Notably,downstreamapplicationscan
reaptheperformancebenefitsofmulti-modalpretrainingwithoutrequiringthosemodalitiesduringevaluation.
Reasoningandagenticcapabilities: FutureEEG-FMscouldbefine-tunedtomimicexpertreasoningprocesses,
adheretoexpertgradingcriteria[171]orinstructions,andautonomouslyretrieverelevantevidencefromverified
medicalliteraturerepositoriesandknowledgebases. Augmentedhealthcareworkflowscouldleverageinsightsfrom
20/35

multiplespecializedmodality-specificagentstoinformclinicaldecisions.
Scalingdowntask-specificEEG-FMs: FMsmayrequiremodelparameterscalingtoobtainsuperiorpretrained
features. However,largeEEG-FMsmaynotbesuitableforapplicationsinvolvingstreamingEEGdata,real-time
EEGprocessing,ordeploymentinresource-constrainedsettings,suchasbrain-computerinterfaces,medicaldevices,
and clinical environments. In such contexts, knowledge distillation [172], pruning [173], or quantization [174]
techniquescandeliversmaller,computationallyinexpensivemodelsthatmaintainhightaskperformance.
TimeseriesFMs,tasksemantics,andinductivebiases: Therelativematurityofgeneraltime-seriesFMs(TS-FMs)
can serve as a source of inspiration for EEG-FM development. For example, an understanding of how TS-FMs
learn effectively from large, diverse datasets across economic, energy, traffic, climate, and industrial domains
may improve EEG-FM scaling. TS-FM performance may be particularly instructive when an EEG task shares
underlyingsemanticswithmoregeneraltime-seriestasks,suchasforecastingoranomalydetection. Theremay
existopportunitiesto‘specialize’TS-FMsbyinjectingEEG-specificbiasesintodatarepresentation,modeldesign,
andtheself-supervisedlearningobjective. FutureEEG-FMstudiescanassesstheutilityofsuchbiasesinadapting
TS-FMsforEEGtasksandtherelativemeritsandweaknessesofTS-FMs.
6.3 Application Development
Cross- and inter-disciplinary collaboration: The technical development of EEG-FMs should involve close
collaborationwithscientificandclinicalexperts. Suchcollaborationscanproductivelyconstrainandinspirenovel
modeling decisions, identify novel research gaps, establish clear criteria for real-world success or progress, and
facilitateEEG-FMexperimentationamongnicheapplication-specificaudiences.
ModelcardstoguideEEG-FMselection: TheavailabilityofmultipleEEG-FMs,eachpurportedlyanoff-the-
shelftool,posesapracticaldilemmafordomainexpertswhomustmakeaprincipledselectionfortheirresearch.
Comprehensivecomparisonsofallavailableoptionsmaynotbefeasibleindiscovery-basedresearch. Therelease
of model cards [175] that summarize an EEG-FM’s functional strengths and weaknesses, inherent or dominant
inductivebiases,computerequirements,andevaluationscopeandrankingscouldinformthemodelselectionprocess.
Clinicalapplications: ThereisasubstantialopportunityforEEG-FMstoaugmenttheclinicalEEGreviewprocess
inbothshort-andextended-durationmonitoringsettings. EEG-FMscouldspeedupreviewbyguidingthereviewer’s
attentiontonoteworthytemporalsegments,brainregions,orchannelsdistinctfrombackgroundactivity,especiallyin
longerrecordings,suchasinepilepsy-orsleep-relatedapplications. Basedontheseclues,anEEG-FMcoupledwith
atextdecodercouldsummarizetheclinicallyrelevantfindingsasastructuredtextreport. Additionally,EEG-FMs
couldsupportcase-basedclinicalreasoningbysurfacinghistoricalrecordswithsharedEEGphenotypes. Finally,
EEG-FMscouldimprovetheperformanceofspikeandseizuredetectionsgeneratedbyEEGreviewingsoftware.
Translationalhurdles: SeveralhurdlesandconsiderationspreventthetranslationandadoptionofEEG-FMsin
clinicalpractice. Testingandvalidation.Prospectivepilottestingforspecificusecasesusingsite-specificpatientdata
canprovideactionableevidenceonthefeasibilityofmodeldeploymentanditsbenefitstoclinicalstakeholders. The
gracefulhandlingofdatanoise,corruption,andmissingvaluesisrequiredforoperationalsuccess. Interpretability.
Interfaces that relate EEG-FM outputs to clinical domain knowledge and patient-specific physiological factors
couldincreasecliniciantrustandadoption. Reproducibility.Developersmusttransparentlyreportandreleasethe
data sources, data splits, patient characteristics, and computational pipeline configurations that were utilized to
buildtheEEG-FMtomaintainreproducibility. Regulatoryconsiderations.EEG-FMsandtask-specificfine-tuned
modelswillbetreatedassafety-criticalmedicalartificialintelligence(AI)systemsthatmustadheretostringent
nationalorinternationalguidelines. Therefore,clinicalusersshouldfocusondefiningclearintendeduse,rigorous
validation,andcontrolleddeployment. Attentionshouldbegiventodocumentingdataprovenance,identifyingknown
limitationsandexpectedfailuremodes,andestablishinghuman-AIteamingprotocolsthatkeepcliniciansinthe
loop. Clinicaladoptionshouldfollowmedical-deviceregulatorypathways,includingriskassessment,post-market
monitoring,andpredefinedchange-controlprocedurestomanagemodelupdatesasdatadistributionsevolve.
21/35

7 Conclusion
ThepromiseofEEGfoundationmodels,inprinciple,liesineffectiveandrobustfeaturelearning,featurere-usability,
and label efficiency. Our critical analysis of ten early EEG-FMs indicates that these efforts, inspired by their
counterpartsinthemainstreamvisionandlanguagedomains,havemademoderatestridesinrealizingthispromise
fortheEEGdomain. However,todevelopuniversal,robust,andgeneral-purposeEEGfeatureextractors,future
EEG-FMs must prioritize substantial scaling efforts, principled and trustworthy self-supervised representation
learning, and practically relevant evaluations. In addition to technical modeling, we believe that future research
shouldalsopursuethecollaborativedevelopmentofmeaningfulEEGbenchmarks,includingstandardizeddatasets,
applications,andholisticmodelevaluationschemesthatcanmeasurablytrackthereal-worldreadinessandimpact
of EEG-FMs. With sustained efforts in these directions, EEG-FMs are poised to advance scientific research,
brain-computerinterfaces,andclinicaldecisionsupportsystems.
8 Acknowledgments
WewouldliketothankMarioSerraferoandSaeidCheshmiforfruitfuldiscussionsonfoundationmodeling.
9 Funding
ThisstudywassupportedinpartbytheMayoClinic&IllinoisAllianceFellowshipforTechnology-basedHealthcare
Research, the Edward Heiken Interdisciplinary Health Sciences Institute Fund, and NSF grants IIS-2105233,
IIS-2344731,andIIS-2337909.
10 Data Availability
Thisreviewdidnotgenerateanynewdata. AvisualsummaryoftheEEG-FMsincludedinthisreviewandlinksto
theiroriginalcoderepositorieswillbemadeavailableviaapubliclyaccessiblerepositoryuponacceptance.
11 Conflicts of Interest
None.
22/35

References
1. Mushtaq,F.,Welke,D.,Gallagher,A.,Pavlov,Y.G.,Kouara,L.,Bosch-Bayard,J.,vandenBosch,J.J.F.,
Arvaneh,M.,Bland,A.R.,Chaumon,M.,etal.OneHundredYearsofEEGforBrainandBehaviourResearch.
NatureHumanBehaviour8,1437–1443. ISSN:2397-3374.(2025)(Aug.2024).
2. Roy,Y.,Banville,H.,Albuquerque,I.,Gramfort,A.,Falk,T.H.&Faubert,J.DeepLearning-BasedElectroen-
cephalographyAnalysis:ASystematicReview.JournalofNeuralEngineering16,051001. ISSN:1741-2552.
(2025)(Aug.2019).
3. Craik,A.,He,Y.&Contreras-Vidal,J.L.DeepLearningforElectroencephalogram(EEG)Classification
Tasks:AReview.JournalofNeuralEngineering16,031001. ISSN:1741-2552.(2025)(Apr.2019).
4. Obeid,I.&Picone,J.ThetempleuniversityhospitalEEGdatacorpus.Frontiersinneuroscience10,196
(2016).
5. Wagh, N., Wei, J., Rawal, S., Berry, B. M. & Varatharajah, Y. Evaluating latent space robustness and
uncertaintyofEEG-MLmodelsunderrealisticdistributionshifts.AdvancesinNeuralInformationProcessing
Systems35,21142–21156(2022).
6. Banville, H., Chehab, O., Hyvärinen, A., Engemann, D.-A. & Gramfort, A. Uncovering the structure of
clinicalEEGsignalswithself-supervisedlearning.JournalofNeuralEngineering18,046020(2021).
7. Bommasani, R., Hudson, D. A., Adeli, E., Altman, R., Arora, S., von Arx, S., Bernstein, M. S., Bohg,
J., Bosselut, A., Brunskill, E., et al. On the opportunities and risks of foundation models. arXiv preprint
arXiv:2108.07258(2021).
8. Yuan,L.,Chen,D.,Chen,Y.-L.,Codella,N.,Dai,X.,Gao,J.,Hu,H.,Huang,X.,Li,B.,Li,C.,etal.Florence:
Anewfoundationmodelforcomputervision.arXivpreprintarXiv:2111.11432(2021).
9. Kirillov,A.,Mintun,E.,Ravi,N.,Mao,H.,Rolland,C.,Gustafson,L.,Xiao,T.,Whitehead,S.,Berg,A.C.,
Lo,W.-Y.,etal.SegmentanythinginProceedingsoftheIEEE/CVFinternationalconferenceoncomputer
vision(2023),4015–4026.
10. Radford,A.,Kim,J.W.,Hallacy,C.,Ramesh,A.,Goh,G.,Agarwal,S.,Sastry,G.,Askell,A.,Mishkin,P.,
Clark, J., et al. Learning transferable visual models from natural language supervision in International
conferenceonmachinelearning(2021),8748–8763.
11. Chowdhery,A.,Narang,S.,Devlin,J.,Bosma,M.,Mishra,G.,Roberts,A.,Barham,P.,Chung,H.W.,Sutton,
C., Gehrmann, S., et al. Palm: Scaling language modeling with pathways. Journal of Machine Learning
Research24,1–113(2023).
12. Touvron,H.,Lavril,T.,Izacard,G.,Martinet,X.,Lachaux,M.-A.,Lacroix,T.,Rozière,B.,Goyal,N.,Hambro,
E.,Azhar,F.,etal.Llama:Openandefficientfoundationlanguagemodels.arXivpreprintarXiv:2302.13971
(2023).
13. Achiam, J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I., Aleman, F. L., Almeida, D., Altenschmidt, J.,
Altman,S.,Anadkat,S.,etal.Gpt-4technicalreport.arXivpreprintarXiv:2303.08774(2023).
14. Wang,C.,Subramaniam,V.,Yaari,A.U.,Kreiman,G.,Katz,B.,Cases,I.&Barbu,A.BrainBERT:Self-
supervisedrepresentationlearningforintracranialrecordings.arXivpreprintarXiv:2302.14367 (2023).
15. Cui, W., Jeong, W., Thölke, P., Medani, T., Jerbi, K., Joshi, A. A. & Leahy, R. M. Neuro-gpt: Towards a
foundationmodelforeegin2024IEEEInternationalSymposiumonBiomedicalImaging(ISBI)(2024),1–5.
16. Zhang,D.,Yuan,Z.,Yang,Y.,Chen,J.,Wang,J.&Li,Y.Brant:Foundationmodelforintracranialneural
signal.AdvancesinNeuralInformationProcessingSystems36(2024).
17. Yang,C.,Westover,M.&Sun,J.Biot:Biosignaltransformerforcross-datalearninginthewild.Advancesin
NeuralInformationProcessingSystems36(2024).
23/35

18. Chen,Y.,Ren,K.,Song,K.,Wang,Y.,Wang,Y.,Li,D.&Qiu,L.EEGFormer:Towardstransferableand
interpretablelarge-scaleEEGfoundationmodel.arXivpreprintarXiv:2401.10278(2024).
19. Jiang, W.-B., Zhao, L.-M. & Lu, B.-L. Large Brain Model for Learning Generic Representations with
TremendousEEGDatainBCI en.arXiv:2405.18765[cs].May2024.http://arxiv.org/abs/2405.
18765(2024).
20. Panchavati, S. & Speier, W. Mentality in ICLR 2024 Workshop on Learning from TimeSeries For Health
(2024).https://openreview.net/forum?id=O6T38rRiFp.
21. Jiang,W.-B.,Wang,Y.,Lu,B.-L.&Li,D.NeuroLM:AUniversalMulti-taskFoundationModelforBridging
theGapbetweenLanguageandEEGSignalsarXiv:2409.00101[cs,eess].Aug.2024.http://arxiv.
org/abs/2409.00101(2024).
22. Shi, E., Zhao, K., Yuan, Q., Wang, J., Hu, H., Yu, S. & Zhang, S. FoME: A Foundation Model for EEG
using Adaptive Temporal-Lateral Attention Scaling en. arXiv:2409.12454 [cs, eess]. Sept. 2024. http:
//arxiv.org/abs/2409.12454(2024).
23. Yuan,Z.,Shen,F.,Li,M.,Yu,Y.,Tan,C.&Yang,Y.BrainWave:ABrainSignalFoundationModelforClinical
Applications2024.arXiv:2402.10251[q-bio.NC].https://arxiv.org/abs/2402.10251.
24. Yuxuan,Y.,Hongbo,W.,Li,C.,Yiheng,P.&Luo,J.FoundationmodelsforEEGdecoding:currentprogress
andprospectiveresearch.JournalofNeuralEngineering(2025).
25. Zhou,X.,Liu,C.,Chen,Z.,Wang,K.,Ding,Y.,Jia,Z.&Wen,Q.Brainfoundationmodels:Asurveyon
advancementsinneuralsignalprocessingandbraindiscovery.arXivpreprintarXiv:2503.00580(2025).
26. Weng,W.,Gu,Y.,Guo,S.,Ma,Y.,Yang,Z.,Liu,Y.&Chen,Y.Self-supervisedlearningforelectroencephalo-
gram:Asystematicsurvey.ACMComputingSurveys57,1–38(2025).
27. Tatum,W.O.,Rubboli,G.,Kaplan,P.W.,Mirsatari,S.,Radhakrishnan,K.,Gloss,D.,Caboclo,L.,Drislane,
F.,Koutroumanidis,M.,Schomer,D.,etal.ClinicalutilityofEEGindiagnosingandmonitoringepilepsyin
adults.ClinicalNeurophysiology129,1056–1082(2018).
28. DaSilva,F.L.EEGandMEG:relevancetoneuroscience.Neuron80,1112–1128(2013).
29. Värbu, K., Muhammad, N. & Muhammad, Y. Past, present, and future of EEG-based BCI applications.
Sensors22,3331(2022).
30. Buzsáki,G.,Anastassiou,C.A.&Koch,C.Theoriginofextracellularfieldsandcurrents—EEG,ECoG,
LFPandspikes.Naturereviewsneuroscience13,407–420(2012).
31. Brunner,C.,Billinger,M.,Seeber,M.,Mullen,T.R.&Makeig,S.Volumeconductioninfluencesscalp-based
connectivityestimates.Frontiersincomputationalneuroscience10,121(2016).
32. Petroff,O.A.,Spencer,D.D.,Goncharova,I.I.&Zaveri,H.P.Acomparisonofthepowerspectraldensity
ofscalpEEGandsubjacentelectrocorticograms.ClinicalNeurophysiology127,1108–1112(2016).
33. Klimesch, W. Memory processes, brain oscillations and EEG synchronization. International journal of
psychophysiology24,61–100(1996).
34. Oken,B.S.,Salinsky,M.C.&Elsas,S.-M.Vigilance,alertness,orsustainedattention:physiologicalbasis
andmeasurement.Clinicalneurophysiology117,1885–1901(2006).
35. Perinelli,A.,Assecondi,S.,Tagliabue,C.F.&Mazza,V.Powershiftandconnectivitychangesinhealthy
agingduringresting-stateEEG.NeuroImage256,119247(2022).
36. Amin, U., Nascimento, F. A., Karakis, I., Schomer, D. & Benbadis, S. R. Normal variants and artifacts:
importanceinEEGinterpretation.Epilepticdisorders25,591–648(2023).
37. Blume,W.T.DrugeffectsonEEG.JournalofClinicalNeurophysiology23,306–311(2006).
24/35

38. Li,B.,Cheng,T.&Guo,Z.AreviewofEEGacquisition,processingandapplicationinJournalofPhysics:
ConferenceSeries1907(2021),012045.
39. Céspedes-Villar,Y.,Martinez-Vargas,J.D.&Castellanos-Dominguez,G.InfluenceofPatient-SpecificHead
ModelingonEEGSourceImaging.ComputationalandMathematicalMethodsinMedicine2020,5076865
(2020).
40. Smit,D.J.,Boomsma,D.I.,Schnack,H.G.,Pol,H.E.H.&deGeus,E.J.IndividualdifferencesinEEG
spectralpowerreflectgeneticvarianceingrayandwhitemattervolumes.Twinresearchandhumangenetics
15,384–392(2012).
41. Gao,R.,Peterson,E.J.&Voytek,B.Inferringsynapticexcitation/inhibitionbalancefromfieldpotentials.
Neuroimage158,70–78(2017).
42. TatumIV,W.O.HandbookofEEGinterpretation(SpringerPublishingCompany,2021).
43. Popa, L. L., Dragos, H., Pantelemon, C., Rosu, O. V. & Strilciuc, S. The role of quantitative EEG in the
diagnosisofneuropsychiatricdisorders.Journalofmedicineandlife13,8(2020).
44. Roy,Y.,Banville,H.,Albuquerque,I.,Gramfort,A.,Falk,T.H.&Faubert,J.Deeplearning-basedelectroen-
cephalographyanalysis:asystematicreview.Journalofneuralengineering16,051001(2019).
45. Neumann, O., Ludwig, N., Turowski, M., Heidrich, B., Hagenmeyer, V. & Mikut, R. Smart data repre-
sentations: impact on the accuracy of deep neural networks in Proceedings 31 workshop computational
intelligence(2021),113–130.
46. Michel, C. M. & Brunet, D. EEG source imaging: a practical review of the analysis steps. Frontiers in
neurology10,325(2019).
47. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł. & Polosukhin, I.
Attentionisallyouneed.Advancesinneuralinformationprocessingsystems30(2017).
48. Wu,H.,Xiao,B.,Codella,N.,Liu,M.,Dai,X.,Yuan,L.&Zhang,L.Cvt:Introducingconvolutionstovision
transformersinProceedingsoftheIEEE/CVFinternationalconferenceoncomputervision(2021),22–31.
49. Ericsson,L.,Gouk,H.,Loy,C.C.&Hospedales,T.M.Self-supervisedrepresentationlearning:Introduction,
advances,andchallenges.IEEESignalProcessingMagazine39,42–62(2022).
50. Chen, T., Kornblith, S., Norouzi, M. & Hinton, G. A simple framework for contrastive learning of visual
representationsinInternationalconferenceonmachinelearning(2020),1597–1607.
51. Zhang, C., Zhang, C., Song, J., Yi, J. S. K. & Kweon, I. S. A Survey on Masked Autoencoder for Visual
Self-supervisedLearning.inIJCAI (2023),6805–6813.
52. Wagh, N., Wei, J., Rawal, S., Berry, B., Barnard, L., Brinkmann, B., Worrell, G., Jones, D. & Varathara-
jah,Y.Domain-guidedself-supervisionofeegdataimprovesdownstreamclassificationperformanceand
generalizabilityinMachineLearningforHealth(2021),130–142.
53. Thrun,S.&Pratt,L.inLearningtolearn3–17(Springer,1998).
54. Kumar,A.,Raghunathan,A.,Jones,R.,Ma,T.&Liang,P.Fine-tuningcandistortpretrainedfeaturesand
underperformout-of-distribution.arXivpreprintarXiv:2202.10054(2022).
55. Sun,C.,Shrivastava,A.,Singh,S.&Gupta,A.Revisitingunreasonableeffectivenessofdataindeeplearning
erainProceedingsoftheIEEEinternationalconferenceoncomputervision(2017),843–852.
56. Dehghani,M.,Djolonga,J.,Mustafa,B.,Padlewski,P.,Heek,J.,Gilmer,J.,Steiner,A.P.,Caron,M.,Geirhos,
R.,Alabdulmohsin,I.,etal.Scalingvisiontransformersto22billionparametersinInternationalconference
onmachinelearning(2023),7480–7512.
57. Kaplan,J.,McCandlish,S.,Henighan,T.,Brown,T.B.,Chess,B.,Child,R.,Gray,S.,Radford,A.,Wu,J.&
Amodei,D.Scalinglawsforneurallanguagemodels.arXivpreprintarXiv:2001.08361(2020).
25/35

58. Yao,Q.,Yang,C.-H.H.,Jiang,R.,Liang,Y.,Jin,M.&Pan,S.TowardsNeuralScalingLawsforTimeSeries
FoundationModels.arXivpreprintarXiv:2410.12360(2024).
59. Isik,B.,Ponomareva,N.,Hazimeh,H.,Paparas,D.,Vassilvitskii,S.&Koyejo,S.Scalinglawsfordownstream
task performance of large language models in ICLR 2024 Workshop on Mathematical and Empirical
UnderstandingofFoundationModels(2024).
60. Edwards, T. D., Alvey, J., Alsing, J., Nguyen, N. H. & Wandelt, B. D. Scaling-laws for large time-series
models.arXivpreprintarXiv:2405.13867 (2024).
61. Rosenfeld,J.S.,Rosenfeld,A.,Belinkov,Y.&Shavit,N.Aconstructivepredictionofthegeneralization
erroracrossscales.arXivpreprintarXiv:1909.12673(2019).
62. Oquab, M., Darcet, T., Moutakanni, T., Vo, H., Szafraniec, M., Khalidov, V., Fernandez, P., Haziza, D.,
Massa,F.,El-Nouby,A.,etal.Dinov2:Learningrobustvisualfeatureswithoutsupervision.arXivpreprint
arXiv:2304.07193(2023).
63. Wenzek, G., Lachaux, M.-A., Conneau, A., Chaudhary, V., Guzmán, F., Joulin, A. & Grave, E. CCNet:
Extractinghighqualitymonolingualdatasetsfromwebcrawldata.arXivpreprintarXiv:1911.00359(2019).
64. Dosovitskiy,A.,Beyer,L.,Kolesnikov,A.,Weissenborn,D.,Zhai,X.,Unterthiner,T.,Dehghani,M.,Minderer,
M.,Heigold,G.,Gelly,S.,etal.Animageisworth16x16words:Transformersforimagerecognitionatscale.
arXivpreprintarXiv:2010.11929(2020).
65. Thapa, R., He, B., Kjaer, M. R., Moore IV, H., Ganjoo, G., Mignot, E. & Zou, J. Y. SleepFM: Multi-
modalRepresentationLearningforSleepacrossECG,EEGandRespiratorySignalsinAAAI2024Spring
SymposiumonClinicalFoundationModels(2024).
66. Ogg, M. & Coon, W. G. Self-supervised transformer model training for a sleep-EEG foundation model
in202446thAnnualInternationalConferenceoftheIEEEEngineeringinMedicineandBiologySociety
(EMBC)(2024),1–6.
67. Devlin, J., Chang,M.-W.,Lee, K. &Toutanova, K. Bert:Pre-training ofdeep bidirectional transformers
for language understanding in Proceedings of the 2019 conference of the North American chapter of the
associationforcomputationallinguistics:humanlanguagetechnologies,volume1(longandshortpapers)
(2019),4171–4186.
68. Gabor, D. Theory of communication. Part 1: The analysis of information. Journal of the Institution of
ElectricalEngineers-partIII:radioandcommunicationengineering93,429–441(1946).
69. Moca,V.V.,Bârzan,H.,Nagy-Da˘bâcan,A.&Muresan,R.C.Time-frequencysuper-resolutionwithsuperlets.
,
Naturecommunications12,337(2021).
70. Wang,C.,Yaari,A.,Singh,A.,Subramaniam,V.,Rosenfarb,D.,DeWitt,J.,Misra,P.,Madsen,J.,Stone,S.,
Kreiman,G.,etal.Braintreebank:Large-scaleintracranialrecordingsfromnaturalisticlanguagestimuli.
AdvancesinNeuralInformationProcessingSystems37,96505–96540(2024).
71. Ansuini,A.,Laio,A.,Macke,J.H.&Zoccolan,D.Intrinsicdimensionofdatarepresentationsindeepneural
networks.AdvancesinNeuralInformationProcessingSystems32(2019).
72. Obeid,I.&Picone,J.ThetempleuniversityhospitalEEGdatacorpus.Frontiersinneuroscience10,196
(2016).
73. Radford,A.,Wu,J.,Child,R.,Luan,D.,Amodei,D.,Sutskever,I.,etal.Languagemodelsareunsupervised
multitasklearners.OpenAIblog1,9(2019).
74. Mosher, J. C., Leahy, R. M. & Lewis, P. S. EEG and MEG: forward solutions for inverse methods. IEEE
Transactionsonbiomedicalengineering46,245–259(2002).
75. Gu, A. & Dao, T. Mamba: Linear-time sequence modeling with selective state spaces. arXiv preprint
arXiv:2312.00752(2023).
26/35

76. Goel,K.,Gu,A.,Donahue,C.&Ré,C.It’sraw!audiogenerationwithstate-spacemodelsinInternational
conferenceonmachinelearning(2022),7616–7633.
77. Ronneberger,O.,Fischer,P.&Brox,T.U-net:Convolutionalnetworksforbiomedicalimagesegmentationin
Medicalimagecomputingandcomputer-assistedintervention–MICCAI2015:18thinternationalconference,
Munich,Germany,October5-9,2015,proceedings,partIII18(2015),234–241.
78. Lawhern,V.J.,Solon,A.J.,Waytowich,N.R.,Gordon,S.M.,Hung,C.P.&Lance,B.J.EEGNet:acompact
convolutionalneuralnetworkforEEG-basedbrain–computerinterfaces.Journalofneuralengineering15,
056013(2018).
79. Guttag,J.CHB-MITscalpEEGdatabase(version1.0.0).PhysioNet(2010).
80. Zhang,G.-Q.,Cui,L.,Mueller,R.,Tao,S.,Kim,M.,Rueschman,M.,Mariani,S.,Mobley,D.&Redline,S.
TheNationalSleepResearchResource:towardsasleepdatacommons.JournaloftheAmericanMedical
InformaticsAssociation25,1351–1358(2018).
81. Kemp,B.,Zwinderman,A.H.,Tuk,B.,Kamphuisen,H.A.&Oberye,J.J.Analysisofasleep-dependent
neuronal feedback loop: the slow-wave microcontinuity of the EEG. IEEE Transactions on Biomedical
Engineering47,1185–1194(2000).
82. Terzano,M.G.,Parrino,L.,Sherieri,A.,Chervin,R.,Chokroverty,S.,Guilleminault,C.,Hirshkowitz,M.,
Mahowald,M.,Moldofsky,H.,Rosa,A.,etal.Atlas,rules,andrecordingtechniquesforthescoringofcyclic
alternatingpattern(CAP)inhumansleep.Sleepmedicine2,537–554(2001).
83. Nejedly, P., Kremen, V., Sladky, V., Cimbalnik, J., Klimes, P., Plesinger, F., Mivalt, F., Travnicek, V.,
Viscor, I., Pail, M., et al. Multicenter intracranial EEG dataset for classification of graphoelements and
artifactualsignals.en.ScientificData7.Publisher:NaturePublishingGroup,179.ISSN:2052-4463.https:
//www.nature.com/articles/s41597-020-0532-5(2024)(June2020).
84. VanBlooijs,D.,vandenBoom,M.,vanderAar,J.,Huiskamp,G.,Castegnaro,G.,Demuru,M.,Zweiphenning,
W., van Eijsden, P., Miller, K. J., Leijten, F., et al. "CCEP ECoG dataset across age 4-51" (OpenNeuro,
2023).
85. Grossmann,A.&Morlet,J.DecompositionofHardyfunctionsintosquareintegrablewaveletsofconstant
shape.SIAMjournalonmathematicalanalysis15,723–736(1984).
86. Detti,P.,Vatti,G.&ZabaloManriquedeLara,G.EEGsynchronizationanalysisforseizureprediction:A
studyondataofnoninvasiverecordings.Processes8,846(2020).
87. Quan, S. F., Howard, B. V., Iber, C., Kiley, J. P., Nieto, F. J., O’Connor, G. T., Rapoport, D. M., Redline,
S.,Robbins,J.,Samet,J.M.,etal.Thesleephearthealthstudy:design,rationale,andmethods.Sleep20,
1077–1085(1997).
88. Alvarez-Estevez,D.&Rijsman,R.M.Inter-databasevalidationofadeeplearningapproachforautomatic
sleepscoring.PloSone16,e0256111(2021).
89. Hatlestad-Hall,C.,Rygvold,T.W.&Andersson,S.BIDS-structuredresting-stateelectroencephalography
(EEG)dataextractedfromanexperimentalparadigm.DatainBrief 45,108647(2022).
90. Liu,H.,Wei,P.,Wang,H.,Lv,X.,Duan,W.,Li,M.,Zhao,Y.,Wang,Q.,Chen,X.,Shi,G.,etal.AnEEG
motorimagerydatasetforbraincomputerinterfaceinacutestrokepatients.ScientificData11,131(2024).
91. Rockhill,A.P.,Jackson,N.,George,J.,Aron,A.&Swann,N.C."UCSanDiegoRestingStateEEGData
fromPatientswithParkinson’sDisease"(OpenNeuro,2021).
92. Anjum,M.F.,Dasgupta,S.,Mudumbai,R.,Singh,A.,Cavanagh,J.F.&Narayanan,N.S.Linearpredictive
coding distinguishes spectral EEG features of Parkinson’s disease. Parkinsonism & related disorders 79,
79–85(2020).
27/35

93. Cavanagh,J.F.,Kumar,P.,Mueller,A.A.,Richardson,S.P.&Mueen,A.DiminishedEEGhabituationto
noveleventseffectivelyclassifiesParkinson’spatients.ClinicalNeurophysiology129,409–418(2018).
94. Vicchietti,M.L.,Ramos,F.M.,Betting,L.E.&Campanharo,A.S.ComputationalmethodsofEEGsignals
analysisforAlzheimer’sdiseaseclassification.ScientificReports13,8184(2023).
95. Stevenson,N.J.,Tapani,K.,Lauronen,L.&Vanhatalo,S.AdatasetofneonatalEEGrecordingswithseizure
annotations.Scientificdata6,1–8(2019).
96. Ge,W.,Jing,J.,An,S.,Herlopian,A.,Ng,M.,Struck,A.F.,Appavu,B.,Johnson,E.L.,Osman,G.,Haider,
H.A.,etal.DeepactivelearningforinterictalictalinjurycontinuumEEGpatterns.Journalofneuroscience
methods351,108966(2021).
97. Xiang, C., Fan, X., Bai, D., Lv, K. & Lei, X. A resting-state EEG datasetfor sleep deprivation. Scientific
Data11,427(2024).
98. Trinh,N.,Whelan,R.,Ward,T.&Derosiere,G.Task-relatedandresting-stateEEGclassificationofadult
patientswithADHDusingmachinelearningin2023IEEE19thInternationalConferenceonBodySensor
Networks(BSN)(2023),1–4.
99. Motie Nasrabadi, A., Allahverdy, A., Samavati, M. & Mohammadi, M. R. EEG data for ADHD/Control
children.(NoTitle)(2020).
100. Olejarczyk,E.&Jernajczyk,W.Graph-basedanalysisofbrainconnectivityinschizophrenia.PloSone12,
e0188629(2017).
101. jcavanagh@unm.edu,J.F.C."EEG:Depressionrest"(OpenNeuro,2021).
102. Mumtaz,W.MDDpatientsandhealthycontrolsEEGdata(new).figshare,Dataset(2016).
103. Miltiadous,A.,Tzimourta,K.D.,Afrantou,T.,Ioannidis,P.,Grigoriadis,N.,Tsalikakis,D.G.,Angelidis,P.,
Tsipouras,M.G.,Glavas,E.,Giannakeas,N.,etal.AdatasetofscalpEEGrecordingsofAlzheimer’sdisease,
frontotemporaldementiaandhealthysubjectsfromroutineEEG.Data8,95(2023).
104. Blankertz, B., Dornhege, G., Krauledat, M., Müller, K.-R. & Curio, G. The non-invasive Berlin brain–
computerinterface:fastacquisitionofeffectiveperformanceinuntrainedsubjects.NeuroImage37,539–550
(2007).
105. Savran,A.,Ciftci,K.,Chanel,G.,CruzMota,J.,Viet,L.H.,Sankur,B.,Akarun,L.,Caplier,A.&Rombaut,
M.EmotiondetectionintheloopfrombrainsignalsandfacialimagesinSummerWorkshoponMultimodal
Interfaces(eINTERFACE2006)(2006),69–80.
106. Luciw,M.D.,Jarocka,E.&Edin,B.B.Multi-channelEEGrecordingsduring3,936graspandlifttrialswith
varyingweightandfriction.Scientificdata1,1–11(2014).
107. Margaux,P.,Emmanuel,M.,Sébastien,D.,Olivier,B.&Jérémie,M.ObjectiveandSubjectiveEvaluation
ofOnlineErrorCorrectionduringP300-BasedSpelling.AdvancesinHuman-ComputerInteraction2012,
578295(2012).
108. Schalk,G.,McFarland,D.J.,Hinterberger,T.,Birbaumer,N.&Wolpaw,J.R.BCI2000:ageneral-purpose
brain-computerinterface(BCI)system.IEEETransactionsonbiomedicalengineering51,1034–1043(2004).
109. Trujillo,L.T.Mentaleffortandinformation-processingcostsareinverselyrelatedtoglobalbrainfreeenergy
duringvisualcategorization.Frontiersinneuroscience13,1292(2019).
110. Trujillo,L.T.,Stanfield,C.T.&Vela,R.D.Theeffectofelectroencephalogram(EEG)referencechoiceon
information-theoreticmeasuresofthecomplexityandintegrationofEEGsignals.Frontiersinneuroscience
11,425(2017).
111. Zheng, W.-L. & Lu, B.-L. Investigating critical frequency bands and channels for EEG-based emotion
recognitionwithdeepneuralnetworks.IEEETransactionsonautonomousmentaldevelopment7,162–175
(2015).
28/35

112. Zheng, W.-L., Liu, W., Lu, Y., Lu, B.-L. & Cichocki, A. Emotionmeter: A multimodal framework for
recognizinghumanemotions.IEEEtransactionsoncybernetics49,1110–1122(2018).
113. Liu, W., Zheng, W.-L., Li, Z., Wu, S.-Y., Gan, L. & Lu, B.-L. Identifying similarities and differences in
emotionrecognitionwithEEGandeyemovementsamongChinese,German,andFrenchPeople.Journalof
NeuralEngineering19,026012(2022).
114. Torkamani-Azar, M., Kanik, S. D., Aydin, S. & Cetin, M. Prediction of reaction time and vigilance vari-
abilityfromspatio-spectralfeaturesofresting-stateEEGinalongsustainedattentiontask.IEEEjournalof
biomedicalandhealthinformatics24,2550–2558(2020).
115. Korczowski, L., Cederhout, M., Andreev, A., Cattan, G., Rodrigues, P. L. C., Gautheret, V. & Congedo,
M. Brain Invaders calibration-less P300-based BCI with modulation of flash duration Dataset (bi2015a)
PhDthesis(GIPSA-lab,2019).
116. Jiang, W.-B., Zhao, L.-M., Guo, P. & Lu, B.-L. Discriminating surprise and anger from EEG and eye
movementswithagraphnetworkin2021IEEEInternationalConferenceonBioinformaticsandBiomedicine
(BIBM)(2021),1353–1357.
117. Jiang,W.-B.,Liu,X.-H.,Zheng,W.-L.&Lu,B.-L.Multimodaladaptiveemotiontransformerwithflexible
modality inputs on a novel dataset with continuous labels in proceedings of the 31st ACM international
conferenceonmultimedia(2023),5975–5984.
118. Luo,S.,Lan,Y.-T.,Peng,D.,Li,Z.,Zheng,W.-L.&Lu,B.-L.Multimodalemotionrecognitioninresponseto
oilpaintingsin202244thAnnualInternationalConferenceoftheIEEEEngineeringinMedicine&Biology
Society(EMBC)(2022),4167–4170.
119. Li,R.,Liu,L.-D.&Lu,B.-L.DiscriminationofdecisionconfidencelevelsfromEEGsignalsin202110th
InternationalIEEE/EMBSConferenceonNeuralEngineering(NER)(2021),946–949.
120. Tao, L.-Y. & Lu, B.-L. Emotion recognition under sleep deprivation using a multimodal residual LSTM
networkin2020InternationalJointConferenceonNeuralNetworks(IJCNN)(2020),1–8.
121. He,Y.,Luu,T.P.,Nathan,K.,Nakagome,S.&Contreras-Vidal,J.L.Amobilebrain-bodyimagingdataset
recordedduringtreadmillwalkingwithabrain-computerinterface.Scientificdata5,1–10(2018).
122. Brunner,C.,Leeb,R.,Müller-Putz,G.,Schlögl,A.&Pfurtscheller,G.BCICompetition2008–Grazdataset
A.Instituteforknowledgediscovery(laboratoryofbrain-computerinterfaces),GrazUniversityofTechnology
16,34(2008).
123. Zyma,I.,Tukaev,S.,Seleznov,I.,Kiyono,K.,Popov,A.,Chernykh,M.&Shpenkov,O.Electroencephalo-
gramsduringmentalarithmetictaskperformance.Data4,14(2019).
124. Nejedly,P.,Kremen,V.,Sladky,V.,Cimbalnik,J.,Klimes,P.,Plesinger,F.,Mivalt,F.,Travnicek,V.,Viscor,
I.,Pail,M.,etal.MulticenterintracranialEEGdatasetforclassificationofgraphoelementsandartifactual
signals.Scientificdata7,179(2020).
125. VanDenOord,A.,Vinyals,O.,etal.Neuraldiscreterepresentationlearning.Advancesinneuralinformation
processingsystems30(2017).
126. He,K.,Chen,X.,Xie,S.,Li,Y.,Dollár,P.&Girshick,R.Maskedautoencodersarescalablevisionlearnersin
ProceedingsoftheIEEE/CVFconferenceoncomputervisionandpatternrecognition(2022),16000–16009.
127. Kostas,D.,Aroca-Ouellette,S.&Rudzicz,F.BENDR:Usingtransformersandacontrastiveself-supervised
learning task to learn from massive amounts of EEG data. Frontiers in Human Neuroscience 15, 653659
(2021).
128. Oikonomou,V.P.,Georgiadis,K.,Liaros,G.,Nikolopoulos,S.&Kompatsiaris,I.Acomparisonstudyon
EEGsignalprocessingtechniquesusingmotorimageryEEGdatain2017IEEE30thinternationalsymposium
oncomputer-basedmedicalsystems(CBMS)(2017),781–786.
29/35

129. Schirrmeister,R.T.,Springenberg,J.T.,Fiederer,L.D.J.,Glasstetter,M.,Eggensperger,K.,Tangermann,M.,
Hutter,F.,Burgard,W.&Ball,T.DeeplearningwithconvolutionalneuralnetworksforEEGdecodingand
visualization.Humanbrainmapping38,5391–5420(2017).
130. Amin,S.U.,Alsulaiman,M.,Muhammad,G.,Mekhtiche,M.A.&Hossain,M.S.DeepLearningforEEG
motorimageryclassificationbasedonmulti-layerCNNsfeaturefusion.FutureGenerationcomputersystems
101,542–554(2019).
131. Zhang,D.,Chen,K.,Jian,D.&Yao,L.Motorimageryclassificationviatemporalattentioncuesofgraph
embeddedEEGsignals.IEEEjournalofbiomedicalandhealthinformatics24,2570–2579(2020).
132. Potter, I. Y., Zerveas, G., Eickhoff, C. & Duncan, D. Unsupervised multivariate time-series transformers
for seizure identification on eeg in 2022 21st IEEE International Conference on Machine Learning and
Applications(ICMLA)(2022),1304–1311.
133. Woo,G.,Liu,C.,Sahoo,D.,Kumar,A.&Hoi,S.Cost:Contrastivelearningofdisentangledseasonal-trend
representationsfortimeseriesforecasting.arXivpreprintarXiv:2202.01575(2022).
134. Zhang,X.,Zhao,Z.,Tsiligkaridis,T.&Zitnik,M.Self-supervisedcontrastivepre-trainingfortimeseriesvia
time-frequencyconsistency.Advancesinneuralinformationprocessingsystems35,3988–4003(2022).
135. Nie, Y., Nguyen, N. H., Sinthong, P. & Kalagnanam, J. A Time Series Is Worth 64 Words: Long-term
ForecastingwithTransformersMar.2023.arXiv:2211.14730[cs].(2025).
136. Eldele,E.,Ragab,M.,Chen,Z.,Wu,M.,Kwoh,C.K.,Li,X.&Guan,C.Time-seriesrepresentationlearning
viatemporalandcontextualcontrasting.arXivpreprintarXiv:2106.14112(2021).
137. Zhang, Z. & Parhi, K. K. Low-complexity seizure prediction from iEEG/sEEG using spectral power and
ratiosofspectralpower.IEEEtransactionsonbiomedicalcircuitsandsystems10,693–706(2015).
138. Handa,P.&Goel,N.Epilepticseizuredetectionusingrhythmicityspectrogramandcross-patienttestsetin
20218thinternationalconferenceonsignalprocessingandintegratednetworks(SPIN)(2021),898–902.
139. Kadivar,M.,Moghadam,E.M.,ShervinBadv,R.,Sangsari,R.&Saeedy,M.Acomparisonofconventional
electroencephalographywithamplitude-integratedEEGindetectionofneonatalseizures.MedicalDevices:
EvidenceandResearch,489–496(2019).
140. Wang,Y.,Yang,Y.,Cao,G.,Guo,J.,Wei,P.,Feng,T.,Dai,Y.,Huang,J.,Kang,G.&Zhao,G.SEEG-Net:An
explainableanddeeplearning-basedcross-subjectpathologicalactivitydetectionmethodfordrug-resistant
epilepsy.ComputersinBiologyandMedicine148,105703(2022).
141. Jing,J.,Ge,W.,Hong,S.,Fernandes,M.B.,Lin,Z.,Yang,C.,An,S.,Struck,A.F.,Herlopian,A.,Karakis,I.,
etal.Developmentofexpert-levelclassificationofseizuresandrhythmicandperiodicpatternsduringEEG
interpretation.Neurology100,e1750–e1762(2023).
142. Yang,C.,Xiao,D.,Westover,M.B.&Sun,J.Self-supervisedEEGrepresentationlearningforautomatic
sleepstaging.arXivpreprintarXiv:2110.15278(2021).
143. Peh,W.Y.,Yao,Y.&Dauwels,J.Transformerconvolutionalneuralnetworksforautomatedartifactdetection
inscalpEEGin202244thAnnualInternationalConferenceoftheIEEEEngineeringinMedicine&Biology
Society(EMBC)(2022),3599–3602.
144. Li,H.,Ding,M.,Zhang,R.&Xiu,C.MotorimageryEEGclassificationalgorithmbasedonCNN-LSTM
featurefusionnetwork.Biomedicalsignalprocessingandcontrol72,103342(2022).
145. Song,Y.,Jia,X.,Yang,L.&Xie,L.Transformer-basedspatial-temporalfeaturelearningforEEGdecoding.
arXivpreprintarXiv:2106.11170(2021).
146. Bai,S.,Kolter,J.Z.&Koltun,V.Anempiricalevaluationofgenericconvolutionalandrecurrentnetworks
forsequencemodeling.arXivpreprintarXiv:1803.01271(2018).
30/35

147. Tang, S., Dunnmon, J. A., Saab, K., Zhang, X., Huang, Q., Dubost, F., Rubin, D. L. & Lee-Messer, C.
Self-supervisedgraphneuralnetworksforimprovedelectroencephalographicseizureanalysis.arXivpreprint
arXiv:2104.08336(2021).
148. Tang,S.,Dunnmon,J.A.,Liangqiong,Q.,Saab,K.K.,Baykaner,T.,Lee-Messer,C.&Rubin,D.L.Modeling
multivariate biosignals with graph neural networks and structured state space models in Conference on
health,inference,andlearning(2023),50–71.
149. Hochreiter,S.&Schmidhuber,J.Longshort-termmemory.Neuralcomputation9,1735–1780(1997).
150. Liu,Z.,Mao,H.,Wu,C.-Y.,Feichtenhofer,C.,Darrell,T.&Xie,S.Aconvnetforthe2020sinProceedings
oftheIEEE/CVFconferenceoncomputervisionandpatternrecognition(2022),11976–11986.
151. Goswami,M.,Szafer,K.,Choudhry,A.,Cai,Y.,Li,S.&Dubrawski,A.Moment:Afamilyofopentime-series
foundationmodels.arXivpreprintarXiv:2402.03885(2024).
152. Wu,H.,Hu,T.,Liu,Y.,Zhou,H.,Wang,J.&Long,M.Timesnet:Temporal2d-variationmodelingforgeneral
timeseriesanalysis.arXivpreprintarXiv:2210.02186(2022).
153. Nie,Y.,Nguyen,N.H.,Sinthong,P.&Kalagnanam,J.Atimeseriesisworth64words:Long-termforecasting
withtransformers.arXivpreprintarXiv:2211.14730(2022).
154. Mivalt,F.,Kremen,V.,Sladky,V.,Cui,J.,Gregg,N.M.,Balzekas,I.,Marks,V.,StLouis,E.K.,Croarkin,P.,
Lundstrom,B.N.,etal.Impedancerhythmsinhumanlimbicsystem.JournalofNeuroscience43,6653–6666
(2023).
155. Kiessner, A.-K., Schirrmeister, R. T., Boedecker, J. & Ball, T. Reaching the ceiling? Empirical scaling
behaviourfordeepEEGpathologyclassification.ComputersinBiologyandMedicine178,108681(2024).
156. Klonowski,W.EverythingyouwantedtoaskaboutEEGbutwereafraidtogettherightanswer.Nonlinear
biomedicalphysics3,1–5(2009).
157. Donoghue,T.,Haller,M.,Peterson,E.J.,Varma,P.,Sebastian,P.,Gao,R.,Noto,T.,Lara,A.H.,Wallis,J.D.,
Knight,R.T.,etal.Parameterizingneuralpowerspectraintoperiodicandaperiodiccomponents.Nature
neuroscience23,1655–1665(2020).
158. Peng,Z.,Dong,L.,Bao,H.,Ye,Q.&Wei,F.Beitv2:Maskedimagemodelingwithvector-quantizedvisual
tokenizers.arXivpreprintarXiv:2208.06366(2022).
159. Wang,Y.,Wu,H.,Dong,J.,Liu,Y.,Long,M.&Wang,J.Deeptimeseriesmodels:Acomprehensivesurvey
andbenchmark.arXivpreprintarXiv:2407.13278(2024).
160. Wan,Z.,Yu,Q.,Mao,J.,Duan,W.&Ding,C.Openecg:Benchmarkingecgfoundationmodelswithpublic
1.2millionrecords.arXivpreprintarXiv:2503.00711(2025).
161. Arora,S.,Pasad,A.,Chien,C.-M.,Han,J.,Sharma,R.,Jung,J.-w.,Dhamyal,H.,Chen,W.,Shon,S.,Lee,
H.-y.,etal.Ontheevaluationofspeechfoundationmodelsforspokenlanguageunderstanding.arXivpreprint
arXiv:2406.10083(2024).
162. Wei, X., Faisal, A. A., Grosse-Wentrup, M., Gramfort, A., Chevallier, S., Jayaram, V., Jeunet, C., Bakas,
S., Ludwig, S., Barmpas, K., et al. 2021 BEETL competition: Advancing transfer learning for subject
independenceandheterogenousEEGdatasetsinNeurIPS2021CompetitionsandDemonstrationsTrack
(2022),205–219.
163. Jing, J., Lin, Z., Yang, C., Chow, A., Dane, S., Sun, J. & Westover, M. B. HMS - Harmful Brain Activity
Classification https://kaggle.com/competitions/hms-harmful-brain-activity-
classification.Kaggle.2024.
164. Reyna,M.A.,Amorim,E.,Sameni,R.,Weigle,J.,Elola,A.,Rad,A.B.,Seyedi,S.,Kwon,H.,Zheng,W.-L.,
Ghassemi, M. M., et al. Predicting neurological recovery from coma after cardiac arrest: The George B.
MoodyPhysioNetChallenge2023in2023ComputinginCardiology(CinC)50(2023),1–4.
31/35

165. Dan,J.,Pale,U.,Amirshahi,A.,Cappelletti,W.,Ingolfsson,T.M.,Wang,X.,Cossettini,A.,Bernini,A.,
Benini,L.,Beniczky,S.,etal.SzCORE:SeizureCommunityOpen-SourceResearchEvaluationframework
forthevalidationofelectroencephalography-basedautomatedseizuredetectionalgorithms.Epilepsia(2024).
166. Brinkmann, B. H., Wagenaar, J., Abbot, D., Adkins, P., Bosshard, S. C., Chen, M., Tieng, Q. M., He, J.,
Muñoz-Almaraz,F.,Botella-Rocamora,P.,etal.Crowdsourcingreproducibleseizureforecastinginhuman
andcanineepilepsy.Brain139,1713–1722(2016).
167. Gramfort,A.,Luessi,M.,Larson,E.,Engemann,D.A.,Strohmeier,D.,Brodbeck,C.,Goj,R.,Jas,M.,Brooks,
T.,Parkkonen,L.,etal.MEGandEEGdataanalysiswithMNE-Python.FrontiersinNeuroinformatics7,
267(2013).
168. Schirrmeister,R.T.,Springenberg,J.T.,Fiederer,L.D.J.,Glasstetter,M.,Eggensperger,K.,Tangermann,M.,
Hutter,F.,Burgard,W.&Ball,T.DeeplearningwithconvolutionalneuralnetworksforEEGdecodingand
visualization.HumanBrainMapping.ISSN:1097-0193.http://dx.doi.org/10.1002/hbm.23730
(Aug.2017).
169. Schiratti,J.-B.,LeDouget,J.-E.,LeVanQuyen,M.,Essid,S.&Gramfort,A.Anensemblelearningapproach
todetectepilepticseizuresfromlongintracranialEEGrecordingsin2018IEEEInternationalConferenceon
Acoustics,SpeechandSignalProcessing(ICASSP)(2018),856–860.
170. McMahan,B.,Moore,E.,Ramage,D.,Hampson,S.&yArcas,B.A.Communication-efficientlearningof
deepnetworksfromdecentralizeddatainArtificialintelligenceandstatistics(2017),1273–1282.
171. Tatum IV, W. O., Selioutski, O., Ochoa, J. G., Clary, H. M., Cheek, J., Drislane, F. W. & Tsuchida, T. N.
Americanclinicalneurophysiologysocietyguideline7:guidelinesforEEGreporting.TheNeurodiagnostic
Journal56,285–293(2016).
172. Hinton,G.,Vinyals,O.&Dean,J.Distillingtheknowledgeinaneuralnetwork.arXivpreprintarXiv:1503.02531
(2015).
173. Han,S.,Mao,H.&Dally,W.J.Deepcompression:Compressingdeepneuralnetworkswithpruning,trained
quantizationandhuffmancoding.arXivpreprintarXiv:1510.00149(2015).
174. Gong,Y.,Liu,L.,Yang,M.&Bourdev,L.Compressingdeepconvolutionalnetworksusingvectorquantiza-
tion.arXivpreprintarXiv:1412.6115(2014).
175. Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D. &
Gebru,T.ModelcardsformodelreportinginProceedingsoftheconferenceonfairness,accountability,and
transparency(2019),220–229.
176. Hsu,W.-N.,Bolte,B.,Tsai,Y.-H.H.,Lakhotia,K.,Salakhutdinov,R.&Mohamed,A.Hubert:Self-supervised
speech representation learning by masked prediction of hidden units. IEEE/ACM transactions on audio,
speech,andlanguageprocessing29,3451–3460(2021).
32/35

Supplement
Sleep Foundation Models
OurliteraturesearchyieldedtwosleepFMsthatwereexcludedfromthemainreviewscope. Below,wesummarize
theirsalientaspectsforinterestedreaders.
SleepFM [65]: Data. SleepFM is a large-scale multi-modal sleep foundation model trained on over 100,000
hoursofpolysomnographydatafrom14,000participants. Themodalitiesincludebrainactivity(EEG),eyeactivity
(EOG),muscletone(EMG),cardiacsignals(EKG),andrespiratorysignals. Thedataareminimallypreprocessed
and segmented into 30-second clips aligned with expert annotation boundaries. Modeling. SleepFM uses three
modality-specific1DEfficientNet-basedencoders. Themodelispretrainedwithbothpairwisecontrastivelearning
andanovelleave-one-outcontrastivestrategythatalignseachmodalitywiththejointrepresentationoftheothers.
SleepFM supports flexible inference, allowing downstream classifiers to use any subset of the input modalities.
Evaluation. Theresultingembeddingsareevaluatedthroughcross-modalretrieval,demographicprediction,and
sleep-relatedclassifications,includingsleepstagingandsleepdisorderedbreathingdetection. Resultsshowthat
SleepFM consistently outperforms supervised convolutional baselines. Ablations demonstrate that multi-modal
pretrainingthatincludesEEGissuperiortosingle-modalitypretraining. Additionally,SleepFMdemonstratedstrong
out-of-distributiongeneralizationtoanunseensitewithadifferentchannelconfiguration.
Self-Supervised Transformer Model Training for a Sleep-EEG Foundation Model [66]: Data. The model
is pretrained on 10,897 sleep sessions from 9,013 individuals sourced from multiple public datasets. A single
centralEEGchannel(C3/C4)isresampledto100Hz,normalized,clipped,andsegmentedinto30-secondepochs.
Sequences of 101 epochs with 25% overlap are constructed for subsequent modeling. Modeling. Unsupervised
k-meansclustering(300clusters)onspectrogramfeaturesprovidespseudo-labelsforself-supervision. Theapproach
follows a HuBERT [176]-style masked prediction framework, where the model learns to infer hidden k-means
label sequences. The architecture consists of a 7-layer 1D convolutional encoder, a projection layer, positional
encoding,anda4-layertransformerencoder(28.5Mparameters). Maskingisappliedin10epochblocks,andthe
modelistrainedfor40epochs. Evaluation. Afterpretraining,themodelisadaptedforthetasksofsleepstaging,
subjectidentification,andageprediction. Thepretrainedmodelachievesstrongrepresentationlearningandrapid
convergence,outperformingsupervisedbaselinesinlow-labelsleepstaging. Experimentswithfrozenembeddings,
i.e.,linearprobing,suggestthatthemodelcangeneralizeacrossmontagesandtasks. Additionally,themaskingand
k-means-basedpseudo-labelingprocesswereshowntosupportgeneralizationtotheexternalSleep-EDFdataset.
33/35

Table 1. Pretrainingdatavolume. Channel-hourswereusedtorepresentandcomparethedatascaleatwhichthe
EEGfoundationmodelswerepretrained. Inmostcases,channel-hoursperdatasetwerecalculatedastheproduct
ofthenumberofchannelsandtherecordingdurations(inhours)obtainedfromtheoriginalstudies. ScalpEEG
datasets had a fixed channel count across subjects, whereas intracranial EEG datasets used in BrainBERT and
Branthadasubject-specificchannelcount. ForNeuro-GPTandEEGFormer,channel-hourswerecomputedfrom
publiclyavailabledatasetstatisticsandwereassumedtobeapplicabletobothstudies. ForBrainBERT,weused
thechannel-hoursreportedbytheauthors. ForBrainWave,thetotalpatchcountreportedwasusedtocalculatethe
channel-hoursbyconvertingthepatchsize(1second)tohours. Channel-hourspooledacrossallpretrainingdata
sourcesarehighlightedinbold. N/Arepresentscaseswherechannel-hourscouldnotbedetermined.
EEG-FM PretrainingDataset Number TotalLengthof Channel-Hours Total
|           |                   |     | ofChan- | Recordings | (=NumberofChannels×RecordingLength) |         | Channel-Hours |         |
| --------- | ----------------- | --- | ------- | ---------- | ----------------------------------- | ------- | ------------- | ------- |
|           |                   |     | nels    | (Hours)    |                                     |         |               |         |
| BrainBERT | BrainTreeBank[70] |     | -       | -          |                                     | 4,551   |               | 4,551   |
| Neuro-GPT | TUEG[72]          |     | 20      | 27,063     |                                     | 541,260 |               | 541,260 |
Brant Privatedataset(unknownsource) - - (124×235.34)+(52×82.39)+(120×393.09)+ 281,860.10
(133×137.45)+(116×214.22)+(101×386.70)+
(67×111.55)+(47×207.42)+(134×759.80)
| BIOT      | SHHS[80,87]                 |     | 2   | 42,446 |     | 84,892   |     |         |
| --------- | --------------------------- | --- | --- | ------ | --- | -------- | --- | ------- |
|           | PREST                       |     | 16  | 14,197 |     | 227,152  |     | 312,044 |
| EEGFormer | TUEG                        |     | 20  | 27,063 |     | 541,260  |     | 541,260 |
| LaBraM    | BCICompetitionIV-1[104]     |     | 59  | 8.21   |     | 484.39   |     |         |
|           | Emobrain[105]               |     | 64  | 4.94   |     | 316.16   |     |         |
|           | Grasp/LiftEEGChallenge[106] |     | 32  | 11.72  |     | 375.04   |     |         |
|           | InriaBCIChallenge[107]      |     | 56  | 29.98  |     | 1,678.88 |     |         |
|           | EEGMotorImageryDataset[108] |     | 64  | 47.3   |     | 3,027.2  |     |         |
|           | VisualCategorizationEEG     |     | 64  | 34.35  |     | 2,198.4  |     |         |
Data[109]
|           | RestingStateEEGData          | [110] | 64  | 3.04     |     | 194.56    |            |           |
| --------- | ---------------------------- | ----- | --- | -------- | --- | --------- | ---------- | --------- |
|           | SEEDSeries[111–113]          |       | 62  | 166.75   |     | 10,338.5  |            |           |
|           | SienaScalpEEGDatabase[86]    |       | 31  | 30.47    |     | 944.57    |            |           |
|           | SPISRestingStateDataset[114] |       | 64  | 0.83     |     | 53.12     |            |           |
|           | Brain-Invaders[115]          |       | 32  | 16       |     | 512       |            |           |
|           | TUAR[72]                     |       | 23  | 92.22    |     | 2,121.06  |            |           |
|           | TUEP[72]                     |       | 21  | 591.22   |     | 12,415.62 |            |           |
|           | TUSZ[72]                     |       | 21  | 1,138.53 |     | 23,909.13 |            |           |
|           | TUSL[72]                     |       | 23  | 20.59    |     | 473.57    |            |           |
|           | Multipledatasources[116–120] |       | 62  | 342.23   |     | 21,218.26 |            | 80,260.46 |
| Mentality | TUSZ                         |       | N/A | N/A      |     | N/A       |            | N/A       |
| NeuroLM   | TUEG                         |       | 21  | 24,000   |     | 504,000   |            |           |
|           | SEEDSeries                   |       | 62  | 170.54   |     | 10,573.48 |            |           |
|           | BCICompetitionIV-1           |       | 59  | 8.21     |     | 484.39    |            |           |
|           | Emobrain                     |       | 64  | 4.94     |     | 316.16    |            |           |
|           | Grasp/LiftEEGChallenge       |       | 32  | 11.72    |     | 375.04    |            |           |
|           | InriaBCIChallenge            |       | 56  | 29.98    |     | 1,678.88  |            |           |
|           | MotorMovement/ImageryDataset |       | 64  | 47.3     |     | 3,027.2   |            |           |
|           | RawEEGData                   |       | 64  | 34.35    |     | 2,198.4   |            |           |
|           | RestingStateEEGData          |       | 64  | 3.04     |     | 194.56    |            |           |
|           | SienaScalpEEGDatabase        |       | 31  | 30.47    |     | 944.57    |            |           |
|           | SPISRestingStateDataset      |       | 64  | 0.83     |     | 53.12     |            |           |
|           | Brain-Invaders               |       | 32  | 16       |     | 512       |            |           |
|           | Multipledatasources[116–120] |       | 62  | 342.23   |     | 21,218.26 | 545,576.06 |           |
| FoME      | Multipledatasets             |       | N/A | N/A      |     | N/A       |            | N/A       |
BrainWave Multipledatasets - - 3,162,233,694×(1÷3,600) 878,398.25
34/35

Table 2. EEGfoundationmodelevaluationstrategies. VarioustechniqueswereusedtoevaluateEEGfoundation
models: a)zero-shottransferlearning(ZSTL,inblue)withpriortaskknowledgebutnoaccesstodataandlabels
fromthetargetsetting;b)few-shotlearning(FSL,ingreen)withnopriortaskknowledgebutaccesstoafewlabels
fromthetargetsetting;c)linearprobing(LP,inpink)whereaclassifierheadisadaptedusinglabelsfromthetarget
setting;andd)fine-tuning(FT,inyellow)wherethebackboneandheadtogetherareadaptedusinglabelsfromthe
targetsetting. Evaluationscoresestimatedbasedonthegraphicsinthepaperaredenotedusingsuperscript∗.
|                                     | In-Distribution   | Out-of-Distribution |                     |
| ----------------------------------- | ----------------- | ------------------- | ------------------- |
| EEG-FM Task                         | LP FT             | FSL ZSTL            | LP FT               |
| BrainBERT BrainTreeBank             | AUC-0.59 AUC-0.83 |                     |                     |
| Neuro-GPT BCICompetitionIVDataset2a |                   |                     | Acc.-44.3 Acc.-64.5 |
Private(PathologyDetection) Acc.-91.17
Brant
MAYO(PathologyDetection) Acc.-89.40
FNUSA(PathologyDetection) Acc.-83.51
TUAB AUC-0.8815 AUC-0.8739
| BIOT TUEV | W.F1-0.7504 |     | W.F1-0.7322 |
| --------- | ----------- | --- | ----------- |
CHB-MIT AUC-0.8761 AUC-0.8752
IIICSeizure W.F1-0.5737 W.F1-0.5878
TUAB AUC-0.876
| EEGFormer TUAR | AUC-0.827 AUC-0.852 |     |     |
| -------------- | ------------------- | --- | --- |
TUSL AUC-0.657 AUC-0.679
TUSZ AUC-0.883
NeonateDataset AUC-0.842
TUAB AUC-0.8835 AUC-0.9162
| LaBraM TUEV | B.Acc-34.61 B.Acc-66.16 |     |     |
| ----------- | ----------------------- | --- | --- |
SEEDSeries Acc.-41.02
MoBI RMSE-0.1196
Mentality TUSZ AUC-0.72
TUAB AUC-0.7884
TUEV B.Acc-0.4679
NeuroLM
TUSL B.Acc-0.6845
HMC B.Acc-0.6188
SEEDSeries B.Acc-0.6034
Workload B.Acc-0.6345
F1-46.00∗
TUEV F1-79.00
Sleep-EDFx F1-99.10
SEEDSeries F1-57.89
FoME
MAYO(EventsClassification) F1-78.80 F1-87.78
MAYO(PathologyDetection) F1-95.13
FNUSA(EventsClassification) F1-77.44 F1-85.44
FNUSA(PathologyDetection) F1-91.81
CHB-MIT AUC-0.90∗
Clonic-6 AUC-0.79∗
Atonic-5 AUC-0.77∗
|     |     | AUC-0.90∗ | AUC-0.96∗ |
| --- | --- | --------- | --------- |
Absence-16
| DRE-Clinical |     | AUC-0.75∗ | AUC-0.85∗ |
| ------------ | --- | --------- | --------- |
BrainWave
| SD-71      |     | AUC-0.63∗ | AUC-0.70∗ |
| ---------- | --- | --------- | --------- |
| ADHD-Adult |     | AUC-0.90∗ | AUC-0.96∗ |
| ADHD-Child |     | AUC-0.77∗ | AUC-0.80∗ |
|            |     | AUC-0.72∗ | AUC-0.88∗ |
Schizophrenia-28
| Depression-122 |     | AUC-0.75∗ | AUC-0.78∗ |
| -------------- | --- | --------- | --------- |
| MDD-64         |     | AUC-0.90∗ | AUC-0.92∗ |
|                |     | AUC-0.63∗ | AUC-0.76∗ |
AD-65
| MAYO(EventsClassification) |     | AUC-0.81∗ AUC-0.93∗ | AUC-0.97∗ |
| -------------------------- | --- | ------------------- | --------- |
|                            |     | AUC-0.78∗ AUC-0.91∗ | AUC-0.91∗ |
FNUSA(EventsClassification)
35/35