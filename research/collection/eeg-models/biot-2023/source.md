BIOT: Cross-data Biosignal Learning in the Wild
ChaoqiYang1, M.BrandonWestover2,3, JimengSun1
1UniversityofIllinoisUrbana-Champaign,2HarvardMedicalSchool
3BethIsraelDeaconessMedicalCenter
{chaoqiy2}@illinois.edu
Abstract
Biologicalsignals,suchaselectroencephalograms(EEG),playacrucialrolein
numerousclinicalapplications,exhibitingdiversedataformatsandqualityprofiles.
Currentdeeplearningmodelsforbiosignalsaretypicallyspecializedforspecific
datasetsandclinicalsettings,limitingtheirbroaderapplicability. Motivatedbythe
successoflargelanguagemodelsintextprocessing,weexplorethedevelopment
of foundational models that are trained from multiple data sources and can be
fine-tunedondifferentdownstreambiosignaltasks.
Toovercometheuniquechallengesassociatedwithbiosignalsofvariousformats,
suchasmismatchedchannels,variablesamplelengths,andprevalentmissingval-
ues,weproposeaBiosignalTransformer(BIOT).TheproposedBIOTmodelcan
enablecross-datalearningwithmismatchedchannels,variablelengths,andmissing
valuesbytokenizingdiversebiosignalsintounified"biosignalsentences". Specifi-
cally,wetokenizeeachchannelintofixed-lengthsegmentscontaininglocalsignal
features,flatteningthemtoformconsistent"sentences". Channelembeddingsand
relativepositionembeddingsareaddedtopreservespatio-temporalfeatures.
TheBIOTmodelisversatileandapplicabletovariousbiosignallearningsettings
across different datasets, including joint pre-training for larger models. Com-
prehensive evaluations on EEG, electrocardiogram (ECG), and human activity
sensorysignalsdemonstratethatBIOToutperformsrobustbaselinesincommon
settingsandfacilitateslearningacrossmultipledatasetswithdifferentformats. Use
CHB-MITseizuredetectiontaskasanexample,ourvanillaBIOTmodelshows3%
improvementoverbaselinesinbalancedaccuracy,andthepre-trainedBIOTmodels
(optimizedfromotherdatasources)canfurtherbringupto4%improvements.
1 Introduction
Biosignals,suchasEEGandECG,aremulti-channeltimeseriesrecordedathighsamplingrates
(e.g.,256Hz)invarioushealthcaredomains,includingsleepmedicine,neurologicalandcardiovas-
cular disease detection, and activity monitoring. Deep learning (DL) models have demonstrated
impressivesuccessinautomatingbiosignaldiagnosisacrossdiverseapplications(Yangetal.,2021),
encompassingsleepstageclassification(Biswaletal.,2018;Yangetal.,2021;PhanandMikkelsen,
2022),emotionanalysisviaEEG(Zhangetal.,2020;Suhaimietal.,2020),actionandmotorimagery
recognition(Venkatachalametal.,2020),acutestressdetectionthroughelectrodermalactivity(Greco
etal.,2021),EEG-basedseizureepilepsyclassification(Yangetal.,2023;Jingetal.,2023),and
ECG-drivencardiacarrhythmiadetection(IsinandOzdalili,2017;Parvanehetal.,2019).
Variousdeeplearningmethodshavebeenappliedtobiosignalanalysis. Someworksuse1Dconvolu-
tionalneuralnetworks(CNN)onrawsignals(Jingetal.,2023;Nagabushanametal.,2020;Daretal.,
2020),whileotherspreprocessthedatawithshort-timeFouriertransform(STFT)andemploy2D
CNNmodelsontheresultingspectrogram(Yangetal.,2022a;Kimetal.,2020;Cuietal.,2020).
ResearchersalsosegmentthesignalanduseaCNNsegmentencoderwithadownstreamsequence
Preprint.Underreview.
3202
yaM
01
]PS.ssee[
1v15301.5032:viXra

model (Zhang et al., 2019; Biswal et al., 2018; Jing et al., 2020; Almutairi et al., 2021), such as
Transformerorrecurrentneuralnetworks(RNN),tocapturetemporaldynamics. Otherapproaches
involveensemblelearning,featurefusionfrommultipleencoders(Lietal.,2022),andmulti-level
transformersto encodespatialandtemporal featuresacrossandwithin channels(Lawhernet al.,
2018;Songetal.,2021;Liuetal.,2021).
Thesemodels(Jingetal.,2023;Yangetal.,2021;Biswaletal.,2018;Kostasetal.,2021;Duetal.,
2022;Zhangetal.,2022)predominantlyfocusonbiosignalsampleswithfixedformatsforspecific
tasks,whilereal-worlddatamayexhibitmismatchedchannels,variablelengths,andmissingvalues.
Inthispaper,ourobjectiveistodeviseaflexibletrainingstrategythatcanhandlediversebiosignal
datasetswithvaryingchannels, lengths, andlevelsofmissingness. Forexample, isitpossibleto
transfer knowledge from abnormal EEG detection (a binary classification task with 64 channels
and a 5-second duration, recorded at 256Hz) to improve another EEG task, such as seizure type
classification(amulti-classtaskwith16channelsanda10-seconddurationat200Hz)? Inreality,
such data mismatches often arise from varying devices, system errors, and recording limitations.
Additionally,itisalsoimportanttoexplorethepotentialofutilizingdifferentunlabeleddata.
To apply existing deep learning models to such settings of different biosignals, significant data
processingisrequiredtoaligntheformatsacrossmultipledatasets. Thismayinvolvetruncating
or padding signals for consistent lengths (Zhang et al., 2022), and imputing missing channels or
segments(Bahadoretal.,2021). Suchpractices,however,mayintroduceunnecessarynoiseandshift
datadistributions,leadingtopoorgeneralizationperformance. Developingaflexibleandunified
modelthataccommodatesbiosignalswithdiverseformatscanbeadvantageous.
Inourpaper,wedevelopthebiosignaltransformer(BIOT)model(summarizedinFigure1),which,to
thebestofourknowledge,isthefirstbiosignalencodingmodelthatcanhandlebiosignalsofvarious
formats. Ourmotivationstemsfromthevisiontransformer(ViT)(Dosovitskiyetal.,2020)andthe
audiospectrogramtransformer(AST)(Gongetal.,2021). TheViTmodelsplitstheimageintoa
"sentence"ofpatchesforimagerepresentation. TheASTmodelsplitstheaudiospectrograminto
"sentence"for1Daudiorepresentation. These"sentence"structurescombinedwithTransformer
(Vaswanietal.,2017)canhandlevariable-sizedinputs.
Comparedtoimages(RGBorgray),audios,ornaturallanguages,biosignalsaremorecomplicated
primarily as it has multiple channels. It is non-trivial to transform diverse biosignals of various
formatsintounified"sentence"structures. ThispaperproposesBIOTtosolvethechallengebyanovel
biosignaltokenizationmodulethatsegmentseachchannelseparatelyintotokensandthenflattens
thetokenstoformconsistentbiosignal"sentences"(illustratedinFigure2). Withthedesign,our
BIOTcanenabletheknowledgetransfercrossdifferentdatainthewildandallowjoint(pre-)training
onmultiplebiosignaldatasources. Ourcontributionsarelistedbelow.
• Biosignaltransformer(BIOT).ThispaperproposesabiosignalencodingmodelBIOTbytokeniz-
ingbiosignalsofvariousformatsintounified“sentences.”
• Knowledgetransferacrossdifferentdata. OurBIOTcanenablejoint(pre-)trainingandknowl-
edgetransferacrossdifferentbiosignaldatasetsinthewild,whichinspirestheresearchoflarge
foundationmodelsforbiosignals.
• Strongempiricalperformance. WeevaluateourBIOTonseveralunsupervisedandsupervised
EEG,ECG,andhumanactivitysensorydatasets. ResultsshowthatBIOToutperformsbaseline
modelsandcanutilizethemodelspre-trainedonotherdatatobenefitthecurrenttask.
2 BIOT:BiosignalTransformer
As shown in Figure 1, our BIOT encoder cascades two modules: (i) the biosignal tokenization
modulethattokenizesanarbitrarybiosignal(variablelengths,differentchannels,andmissingvalues)
intoa"sentence"structure.Thisdesigncanpotentiallyenablepreviouslanguagemodelingtechniques
(Devlin et al., 2018; Liu et al., 2019; OpenAI, 2023) to empower the current biosignal models;
(ii) a linear transformer module that captures complex token interactions within the "sentence"
whilemaintaininglinearcomplexity. Afterthat,wealsodiscusstheapplicationofBIOTindifferent
real-worldsettings.
2

Figure1: BiosignalTransformer(BIOT).(Upper)Givenanewdatasample, weinitiallyperform
datapreprocessing(resampling, normalization, tokenization, andflattening)tocreateabiosignal
"sentence"usingthebiosignaltokenizationmodule. Wethenlearnthecomplexinteractionswithin
the"sentence"throughthelineartransformermodule. (Lower)BIOTencoderisversatile,enabling
supervisedlearningoncompletedata, datawithmissingvalues, andpre-trainingandfine-tuning
acrossdiversedataformatsandtasks.
2.1 Module1: BiosignalTokenization
Motivation. Thegoalofthispaperistomodelheterogeneousbiosignals(e.g.,EEGsampleswith
differentchannelsfordifferenttasks)withaunifiedencodingmodel. Forexample,commonEEG
samples (Lopez et al., 2015), such as those for seizure detection, are recorded at 256Hz in the
international 10-20 system 1 for 10-second long (Klem et al., 1999). With standard 16 montage
editing,thesampleisessentiallyamulti-channeltime-series, representedasamatrixofsize(16,
2560). However, format mismatch may prevent the applications on other similar data, such as
different sampling rate (e.g., 200Hz vs 256Hz) (Jing et al., 2023), mismatched channels (i.e.,
differentdatasetshavetheirownnovelchannels),variablerecordingduration(i.e.,30spersample
vs. 10s)(Zhangetal.,2022),missingsegments(i.e.,partoftherecordingisdamagedduetodevice
error). Thus,existingmodelsmayfailtoutilizethemismatcheddatafromdifferentdatasets.
OurBIOTsolvestheabovechallengesbythefollowingsteps. IllustrationsareshowninFigure2.
Assumethemulti-channelbiosignalasS∈RI×J (useacompletesamplefortheeaseofnotation).
• Resampling. We first resample all data to the same rate (denoted by r ∈ R+, such as 200Hz)
bylinearinterpolation. Theconsistentratecouldbeselectedfollowingclinicalknowledgeofa
certainbiosignal. Forexample,thehighestfrequencyofinterestinbothEEGandECGsignalsis
commonlyaround100Hz,andthus200Hzor250HzcanbesuitablefortypicalEEGorECG
applications,accordingtoNyquist-Shannonsamplingtheorem(Nyquist,1928;Shannon,1949).
• Normalization: Toalleviatetheunitdifferenceandamplitudemismatchacrossdifferentchannels
and datasets, we use the 95-percentile of the absolute amplitude to normalize each channel.
Formally,eachchannelS[i]isnormalizedby S[i] .
percentile(|S[i]|,95%)
1https://en.wikipedia.org/wiki/10-20_system_(EEG)
3

Figure2: BiosignalTokenization(nooverlapintheexamples). Sample1hasfourchannels(Fp1,
Fp2,O1,andO2)for5seconds. Wetokenizeeachchannelintosegmentsandthenparameterizethese
20segmentswiththreeembeddings. Ontheright,weusedifferentcolorstorepresentthechannels
(blue-Fp1, brown-Fp2, green-O1, and yellow-O2). Sample 2 has mismatched channels (no O2),
variablelengths(Fp1andFp2areshorterandflipped),andmissingvalues(inO1). Usingourmethod,
wecanstilltokenizeSample2inacomparable"sentence".
• Tokenization: For handling length variation, we tokenize the recording of each channel into
t-secondtokens,andneighboringtokenscanhaveoverlapsofpseconds(p,t∈R+andp<t,e.g.,
t=1andp=0.5). Thus,thek-thtoken(k =1,2,3,...)inthei-thchannelcanberepresentedby
theslicingnotationS[i,(t−p)(k−1):(t−p)(k−1)+t]. Thenumberoftokensperchannel
islimitedbytheinequality: (t−p)(k−1)+t≤J. Here,theoverlappisessentialtomaintain
the temporal information for shorter signals. For example, if the length of signal is J = 3, a
configurationoft=1,p=0willonlygenerate3tokensforeachchannel,whileaconfigurationof
t=1,p=0.5gives5tokensperchannel. Incasesofmissingvalues,wedropthecorresponding
tokens directly (as shown in Sample 2 Figure 2). Note that, our tokenization applies to each
channel,separately,whichisdifferentfrompreviousworks(Biswaletal.,2018;Almutairietal.,
2021;Duetal.,2022)thatsplitallchannelstogether(whichcannotworkonSample2).
• Flattening: Wefinallyflattentokensfromallchannelsintoaconsistent"sentence".
Theabovestepsarenon-parametric.Tostudytheeffectofsamplingrater,tokenlengtht,andoverlap
p,weprovideablationstudiesandinsightsinAppendixB.3. Inthefollowing,wedesignthetoken
embeddingforthebiosignal"sentence",whichcombinesinformationfromthreeaspects.
• Segment embedding. We learn the segment embedding from a spectral perspective by first
extractinganenergyvectorforeachtokenS[i,(t−p)(k−1):(t−p)(k−1)+t]basedonall
frequencybands. Thisstepisenabledbyfastfouriertransform(FFT).Afullyconnectednetwork
(FCN)isthenappliedontheenergyvectortoobtainthesegmentembedding.
• Channelembedding(spatial). Welearnanembeddingtableforalldifferentchannelsandaddthe
correspondingchannelembeddingtothetoken. EachcolorrepresentsonechannelinFigure2.
• Positionalembedding(temporal). Inbiosignals,thesegmentorderwithinthechannelcaptures
temporalinformation. Wethusaddrelativepositionalembeddingtothefinaltokeembeddingby
usingthesinusoidalandcosinefunctions,whichdoesnotneedlearnableparameters.
Wedenotethefinaltokenziedbiosignal"sentence"asX∈RN×l whereN isthenumberoftokens
andlisthedimensionoftokenembedding. InFigure2,themarkedorangeareaindicatesthespatial-
or temporal-relevant tokens w.r.t. the current token (i.e., same time step or channel). Our token
embeddingscaneffectivelycapturethesegmentfeaturesaswellasthespatio-temporalfeatures.
2.2 Module2: Lineartransformer
Transformerwithlinearcomplexityforlongbiosignal"sentence".Next,wewanttoleveragethe
Transformermodel(Vaswanietal.,2017)forlearningthe"sentence"embedding.However,biosignals
usuallyhavemanychannels,whichmayleadtolong"sentences". Forexample,the"sentence"ofa
4

64-channelEEGsignalfor20seconds(withoutoverlapsp=0)canhave64×20=1280tokens,
andlongerwiththeoverlaps. GiventhattheoriginalTransformermodelisknowntohavequadratic
complexity in both time and space, we adopt the linear attention mechanism (Wang et al., 2020;
Katharopoulosetal.,2020)forbiosignallearningapplications.
Formally,letusassumeWK,WV,WQ ∈ Rl×k bethekey,value,andquerymatrices. Ourself-
attentionmoduleusesarank-dapproximationforthesoftmaxattention(N ×N)byreduced-rank
parametermatricesE(cid:62) ∈RN×d,F∈Rd×N (whered(cid:28)N). TheoutputH∈RN×k is,
H= Attention(XWQ,EXWK,FXWV) (1)
(cid:18) (XWQ)(EXWK)(cid:62)(cid:19)
= softmax √ ·FXWV . (2)
k (cid:124) (cid:123)(cid:122) (cid:125)
(cid:124) (cid:123)(cid:122) (cid:125) d×l
N×d
Themaincomponentsinourlineartransformermoduleareonelinearself-attentionlayerandonefully
connectednetwork. Toenablestabletraining,weaddlayernormalization(Baetal.,2016),residual
connection(Heetal.,2016),anddropout(Srivastavaetal.,2014)rightbeforeeachcomponent(see
Figure1),whichgreatlyacceleratestheconvergenceandimprovesthefinalperformance.
BIOTEncoder. AnillustrationofourproposedBIOTencoderisshowninFigure1(upper),which
comprisesthebiosignaltokenizationmoduleandmultipleblocksoflineartransformermodules.
Weobtainthefinalbiosignal"sentence"embeddingbyameanpoolingstepoveralltokens. Notethat
appendingaclassification[CLS]tokenatthebeginningofthe"sentence"(afterModule1)isalsoa
commonoption. However,wefindityieldsaslightlyworseperformanceinourapplication,andthus
weusemeanpoolingintheexperiments.
2.3 BiosignalLearningintheWild
OurproposedBIOTencodercanbeappliedinvariousreal-worldbiosignalapplicationsillustratedin
thelowerpartofFigure1). Theseapplicationsinclude(1)standardsupervisedlearning,(2)learning
withmissingchannelsorsegments,(3)&(4)pre-trainingononeormoredatasets,andfine-tuningon
othersimilardatasetswithdifferentinputformats.
(1)SupervisedLearningisthemostcommonsettinginthepreviousliterature(Jingetal.,2023;
Biswal et al., 2018). With the BIOT encoder, we finally apply an exponential linear unit (ELU)
activation(Clevertetal.,2015)andalinearlayerforclassificationtasks.
(2) Supervised Learning (with missing). Many real biosignal data have mismatched channels,
missingsegments,andvariablelengths,whichpreventstheapplicationsofexistingmodels(Jing
etal.,2023;Songetal.,2021). Flexibleasourmodelis,BIOTcanbeappliedinthissettingwiththe
samemodelstructureasin(1).
(3)UnsupervisedPre-training.Wecanjointlypre-trainageneral-purposeBIOTencoderonmultiple
largeunlabeleddatasets. Intheexperiments,wepre-trainanunsupervisedencoderusing5million
restingEEGsamples(16channels,10s,200Hz)and5millionsleepEEGsamples(2channels,30s,
125Hz),whichislaterutilizedtoimprovevariousdownstreamtasks.
Fortheunsupervisedpre-training,wetakethefollowingsteps(adiagramisshowninFigure1).
• AssumeSistheoriginalbiosignal. Wefirstrandomlydropoutpartofitschannelsanddropoutpart
ofthetokensfromtheremainingchannels,resultinginaperturbedsignalS˜.
• WethenobtaintheembeddingsofSandS˜ bythesameBIOTencoder. Toformtheobjective,we
wanttopredicttheembeddingoftheoriginalsignalbytheperturbedsignal. Thus,anadditioanl
predictor(i.e.,two-layerneuralnetwork)isappendedfortheperturbedsignalfollowing(Grilletal.,
2020). WeuseZandZ˜ todenotetherealembeddingofSandpredictedembeddingfromS˜.
Z= BIOT(S), Z˜ = predictor(BIOT(S˜)). (3)
• Finally,contrastiveloss(Heetal.,2020;Chenetal.,2020)isusedonSandS˜ toformtheobjective.
(cid:16) (cid:16) (cid:17) (cid:17)
L= CrossEntropyLoss softmax (cid:104)Z,Z˜(cid:62)(cid:105)/T ,I . (4)
Here,T representsthetemperature(T =0.2throughoutthepaper)andIisanidentitymatrix. Inthe
implementation,wealsoapplysample-wiseL2-normalizationonbothZandZ˜ beforesoftmax.
5

(4)SupervisedPre-trainingaimstopre-trainamodelbysupervisedlearningononetaskandthen
generalizeandfine-tunetheencoderonanewtask. Thegoalistotransferknowledgeamongdifferent
datasetsandgainimprovementsonthenewtaskcomparedtotrainingfromscratch. OurBIOTmodel
allowsthenewdatasetstohavemismatchedchannelsanddifferentlengths.
3 Experiments
This section shows the strong performance of BIOT on several EEG, ECG and sensory datasets.
Section3.2,3.3compareBIOTwithbaselinesonsupervisedlearningandlearningwithmissing
settings. Section 3.4, 3.5, 3.6 show the that BIOT can be flexibly pre-trained on other datasets
(supervisedorunsupervised)toimprovethecurrenttaskwithdifferentsampleformats. Wereleased
thecodebaseandthepre-trainedmodelsinGitHub2.
3.1 ExperimentalSetups
BiosignalDatasets. Weconsiderthefollowingdatasetsintheevaluation: (i)SHHS(Zhangetal.,
2018; Quan et al., 1997) is a large sleep EEG corpus from patients aged 40 years and older. (ii)
PRESTisalargeunlabeledproprietaryrestingEEGdataset;(iii)Cardiology(Aldayetal.,2020)
isacollectionoffiveECGdatasets(initiallycontainssix,butweexcludethePTB-XLintroduced
below). (iv)TheCHB-MITdatabase(Shoeb,2009)iscollectedfrompediatricpatientsforepilepsy
seizuredetection. (v)IIICSeizuredatasetisfromGeetal.(2021);Jingetal.(2023)fordetecting
oneofthesixictal-interictal-injury-continuum(IIIC)seizurepatterns(OTH,ESZ,LPD,GPD,LRDA,
GRDA);(vi)TUHAbnormalEEGCorpus(TUAB)(Lopezetal.,2015)isanEEGdatasetthathas
beenannotatedasnormalorabnormal; (vii)TUHEEGEvents(TUEV)(Haratietal.,2015)isa
corpusofEEGthatcontainsannotationsofEEGsegmentsasoneofsixeventtypes: spikeandsharp
wave(SPSW),generalizedperiodicepileptiformdischarges(GPED),periodiclateralizedepileptiform
discharges(PLED),eyemovement(EYEM),artifact(ARTF)andbackground(BCKG);(viii)PTB-
XL(Wagneretal.,2020)isanECGdatasetwith12-leadrecordingsfordiagnosisprediction,andwe
useditforarrhythmiasphenotypinginthispaper;(ix)HAR(Anguitaetal.,2013)isahumanaction
recognitiondatasetusingsmartphoneaccelerometerandgyroscopedata.
Table1: DatasetStatistics
Datasets Type(subtype) #Recordings Rate Channels Duration #Sample Tasks
SHHS EEG(sleep) 5,445 125Hz C3-A2,C4-A1 30seconds 5,093,522 Unsupervisedpre-training
PREST EEG(resting) 6,478 200Hz 16montages 10seconds 5,110,992 Unsupervisedpre-training
Cardiology ECG 21,264 500Hz 6or12ECGleads 10seconds 495,970 Unsupervisedpre-training
CHB-MIT EEG(resting) 686 256Hz 16montages 10seconds 326,993 Binary(seizureornot)
IIICSeizure EEG(resting) 2,702 200Hz 16montages 10seconds 165,309 Multi-class(6seizuretypes)
TUAB EEG(unknown) 2,339 256Hz 16montages 10seconds 409,455 Binary(abnormalornot)
TUEV EEG(both) 11,914 256Hz 16montages 5seconds 112,491 Multi-class(6eventtypes)
PTB-XL ECG 21,911 500Hz 12ECGleads 5seconds 65,511 Binary(arrhythmiasornot)
HAR Wearablesensors 10,299 50Hz 9coordinates 2.56seconds 10,299 Multi-class(6actions)
DatasetProcessing. Thefirstthreedatasetsareusedentirelyforunsupervisedpre-training. Thenext
fourdatasetsareusedforsupervisedlearning,andweusedthecommon16bipolarmontagechannels
intheinternational10-20system. ForCHB-MIT(containing23patients),wefirstusepatient1to
19fortraining, 20,21forvalidation, and22,23fortest. Then, weflipthevalidationandtestsets
andconducttheexperimentsagain. Wereporttheaverageperformanceonthesetwosettings. For
IIICseizure,wedividepatientgroupsintotraining/validation/testsetsby60%:20%:20%. ForTUAB
andTUEV,thetrainingandtestseparationisprovidedbythedataset. Wefurtherdividethetraining
patientsintotrainingandvalidationgroupsby80%:20%. ForPTB-XL,wedividepatientgroupsinto
training/validation/testsetsby80%:10%:10%. ThetrainandtestsetofHARisprovided,andwe
furtherdividethetestpatientsintovalidation/textby50%:50%. Forallthedatasets,afterassigning
thepatientstoeithertraining,validation,ortestgroups,wewillfurthersplitthepatient’srecordingto
samples,andthesampledurationaccordstotheannotationfiles. Thedatasetstatisticscanbefound
inTable1,andweprovidesmoredescriptionsandprocessingdetailsinAppendixA.1.
Baseline. Weconsiderthefollowingrepresentativemodels: (i)SPaRCNet(Jingetal.,2023)isa
1D-CNNbasedmodelwithdenseresidualconnections,moreadvancedthanthepopularConvNet
(Schirrmeister et al., 2017), CSCM (Sakhavi et al., 2018); (ii) ContraWR’s (Yang et al., 2021)
2https://github.com/ycq091044/BIOT
6

encodermodelfirsttransformsthebiosignalsintomulti-channelspectrogramandthenuses2D-CNN
basedResNet(Heetal.,2016);(iii)CNN-Transformer(Pehetal.,2022)issuperiortoCNN-LSTM
models(Zhangetal.,2019);(iv)FFCL(Lietal.,2022)combinesembeddingsfromCNNandLSTM
encodersforfeaturefusion;(v)ST-TransformerSongetal.(2021)proposesanmulti-levelEEG
transformerforlearningspatial(S)andtemporal(T)featuressimultaneously,empiricallybetterthan
EEGNetLawhernetal.(2018). OurBIOTmodeltrainedfromscratchisdenotedby(vanilla).
Environments and Settings. The experiments are implemented by Python 3.9.12, Torch
1.13.1+cu117, Pytorch-lightning 1.6.4 on a Linux server with 512 GB memory, 128-core CPUs
andeightRTXA6000GPUs. Allthemodelsareoptimizedontrainingsetandevaluatedonthetest
set. Thebestmodelandhyperparametercombinationsareselectedbasedonthevalidationset. For
Table2andTable3,weobtainfivesetsofresultswithdifferentrandomseedsandreportthemean
andstandarddeviationvalues. ForFigure3andFigure4,wereporttheresultsunderthreerandom
seeds. MoreexperimentalandimplementationdetailscanrefertoAppendixA.2.
3.2 Setting(1)-standardsupervisedlearning
ThissectionshowsthatBIOTiscomparableorbetterthanbaselinesinthesupervisedlearningsettings.
• FourEEGTasks. BothCHB-MITandTUABaredesignedtopredictbinaryoutput,andweuse
binarycrossentropy(BCE)forTUABandthefocalloss(Linetal.,2017)forCHB-MITdueto
itsimbalances(around0.6%positiveratiointrainingset). Weusebalancedaccuracy(Balanced
Acc.),areaunderprecision-recallcurve(AUC-PR)andAUROCasthemetrics. BothIIICSeizure
andTUEVaremulti-classclassificationtaskswithcrossentropyloss. WeemployBalancedAcc.,
Cohen’sKappa,andWeightedF1asthemulti-classevaluation. Tosavespace,weonlyshowthe
performanceonCHB-MITandIIICSeizureinTable2andmovetheothertwotoAppendixB.1.
• ECGandSensoryTasks. PTB-XLisformulatedasabinaryclassificationondetectingarrhyth-
miasphenotypes. WeusetheBCElossandbinaryevaluationmetrics. HAR(classifyingactions)
usesthecrossentropylossandisevaluatedbymulti-classmetrics. ResultsarereportedinTable3.
Table2and3showthatourmodelhassuperiorperformanceoverbaselinesinmosttasks,especially
onCHB-MIT,IIICSeizure,andHAR.Thereasonmightbethatthefrequencyfeaturesaremoreuseful
inthesethreedatasetsasourBIOTextractsthemainfeaturesfromspectralperspective. SPaRCNetis
astrongmodelamongallthebaselinesexceptontheCHB-MITtask. Themodelmightbevulnerable
intheimbalancedclassificationsettingevenwiththefocalloss. Thepre-trainingmodelsattheendof
thetableswillbeintroducedandexplainedinSection3.4,3.6.
Table2: EEGclassificationtasks(ResultsofTUABandTUEVareinAppendixB.1)
CHB-MIT(seizuredetection) IIICSeizure(seizuretypeclassification)
Models
BalancedAcc. AUC-PR AUROC BalancedAcc. Cohen’sKappa WeightedF1
SPaRCNet(Jingetal.,2023) 0.5876±0.0191 0.1247±0.0119 0.8143±0.0148 0.5546±0.0161 0.4679±0.0228 0.5569±0.0184
ContraWR(Yangetal.,2021) 0.6344±0.0002 0.2264±0.0174 0.8097±0.0114 0.5519±0.0058 0.4623±0.0148 0.5486±0.0137
CNN-Transformer(Pehetal.,2022) 0.6389±0.0067 0.2479±0.0227 0.8662±0.0082 0.5476±0.0103 0.4481±0.0139 0.5346±0.0127
FFCL(Lietal.,2022) 0.6262±0.0104 0.2049±0.0346 0.8271±0.0051 0.5617±0.0117 0.4704±0.0130 0.5617±0.0171
ST-Transformer(Songetal.,2021) 0.5915±0.0195 0.1422±0.0094 0.8237±0.0491 0.5423±0.0056 0.4492±0.0056 0.5440±0.0014
(Vanilla)BIOT 0.6640±0.0037 0.2573±0.0088 0.8646±0.0030 0.5762±0.0034 0.4932±0.0046 0.5773±0.0031
PretrainedBIOT(PREST) 0.6942±0.0431 0.3072±0.1187 0.8679±0.0106 0.5787±0.0066 0.4980±0.0054 0.5828±0.0049
PretrainedBIOT(PREST+SHHS) 0.6788±0.0036 0.3090±0.0003 0.8752±0.0022 0.5800±0.0004 0.5040±0.0041 0.5878±0.0015
PretrainedBIOT(6EEGdatasets) 0.7068±0.0457 0.3277±0.0460 0.8761±0.0284 0.5779±0.0087 0.4949±0.0103 0.5737±0.0088
1.Allmodelsusethesametrainingsetofthetask,whilethepre-trainedBIOTmodelsareinitiallypre-trainedonotherdatasources(seeSection3.4,3.6).
2.Boldforthebestmodel(trainedfromscratch)and box forthebestpre-trainedmodels.
3.3 Setting(2)-learningwithmissingchannelsandsegments
ThesectionsimulatestheTUEVdatasettomimicthesettingofsupervisedlearningwithmissing
channelsandsegmentsandshowthestrongperformanceofBIOT.Weconsiderthreemissingcases:
• Missingsegments: Randomlymaskoutasegments(eachsegmentspansfor0.5seconds),a =
0,1,2,3,4,5withequalprobability. Thesegmentmaskingisappliedseparatelyforeachchannel.
• Missingchannels: Randomlymaskoutbchannels,b = 0,1,2,3,4withequalprobability. We
assumethatthemaskingwillnotaltertheunderlyinglabels(thesameassumptionforothercases).
• Missingbothchannelsandsegments: CombiningCase2&3simultaneously.
7

Table3: ECGandhumanactivitysensoryclassificationtasks
PTB-XL(arrhythmiasphenotypeprediction) HAR(huamnactionrecognition)
Models
BalancedAcc. AUC-PR AUROC BalancedAcc. Cohen’sKappa WeightedF1
SPaRCNet(Jingetal.,2023) 0.8275±0.0047 0.9040±0.0067 0.7550±0.0073 0.9371±0.0160 0.9236±0.0189 0.9365±0.0155
ContraWR(Yangetal.,2021) 0.6341±0.0883 0.6795±0.1083 0.4433±0.1557 0.9068±0.0164 0.8879±0.0201 0.9055±0.0182
CNN-Transformer(Pehetal.,2022) 0.6650±0.0459 0.7175±0.0558 0.4996±0.0936 0.8690±0.0839 0.8273±0.0953 0.8352±0.1166
FFCL(Lietal.,2022) 0.7034±0.0052 0.7088±0.0053 0.5127±0.0051 0.8519±0.0148 0.8216±0.0177 0.8508±0.0138
ST-Transformer(Songetal.,2021) 0.7238±0.0083 0.7775±0.0153 0.6003±0.0179 0.9336±0.0063 0.9213±0.0076 0.9337±0.0068
(Vanilla)BIOT 0.8315±0.0008 0.8978±0.0020 0.7493±0.0167 0.9461±0.0134 0.9351±0.0160 0.9458±0.0136
PretrainedBIOT(Cardiology-6) 0.8350±0.0073 0.9128±0.0094 0.7671±0.0116 / / /
PretrainedBIOT(Cardiology-12) 0.8421±0.0030 0.9221±0.0075 0.7659±0.0076 / / /
*Boldforthebestmodel.Allmodelsusethesametrainingsetofthetask.ThePretrainedBIOT(Cardiology-6)andPretrainedBIOT(Cardiology-12)
arepre-trainedonCardiologydata(seeSection3.4),andtheydonotapplytoHARdata(duetodifferentbiosignaltypes).
Figure3: Supervisedlearningwithmissingchannelsorsegments(onTUEVandIIICSeizure)
Toenablethebaselinemodelscompatiblewiththesetting,weuseallzerostoimputethemasked
regions. The comparison is plotted in Figure 3, which shows that (i) all models decrease the
performancewithmoremissingswhileBIOTandthepre-trainedBIOTarelessimpacted(especially
onKappaandWeightedF1);(ii)"Missingchannels"affectstheperformancemorethan"Missing
segments",whichmakessenseassegmentmaskingstillpreservesinformationfromallchannels.
3.4 Setting(3)-unsupervisedpre-training
Inthissection,weshowthatBIOTenablesunsupervisedpre-trainingonexistingwithvariousformats.
• Pre-trained(PREST):Thismodelispre-trainedon5millionrestingEEGsamples(PREST)with
2,048asthebatchsize. Wesavethepre-trainedmodelatthe100-thepoch.
• Pre-trained(PRESET+SHHS):Thismodelisjointlypre-trainedon5MPRESTand5MSHHS
EEGsamples. Thoughtwodatasetshavedifferentsampleformats,ourmodelisabletoencode
themregardless. Also,weuse2048asthebatchsizeandsavemodelatthe100-thepoch.
• Pre-trained (Cardiology-12) is jointly pre-trained on raw data of five datasets in Cardiology
corpus(detailsinAppendixA.1). Weuse1024asbatchsizeandsavemodelatthe100-thepoch.
• Pre-trained(Cardiology-6)ispre-trainedsimilarlyasPre-trained(Cardiology-12),whileweonly
utilizethefirst6ECGleads. Bycontast,Pre-trained(Cardiology-12)usesfull12leads.
Wefine-tunethefirsttwopre-trainedEEGmodelsonfourEEGtasksandappendtheresultstoTable2
(alsoinAppendixB.1). Wefine-tunethelasttwopre-trainedECGmodelsonPTB-XLdatasetsin
Table3. Theresultsshowthatthepre-trainedmodelsgreatlyimprovesthefinalperformanceonthe
downstreamtasksinTable2andTable3.
8

3.5 Setting(4)-supervisedpre-trainingonothertasks
ThissectionshowsthatBIOTallowsknowledgetransferfromonetasktoanothersimilartaskwith
differentsampleformats. Wepre-trainonthetrainingsetofCHB-MIT,IIICSeizure,TUABand
fine-tunesonTUEV(whichhas16channelsand5sduration). Alldatasetsuse200Hzsamplingrate.
Wedesignthreesetsofconfigurationsforthepre-traineddatasets:Format(i)usesthefirst8channels
and10sduration;Format(ii)usesthefull16channelsbutonlythefirst5srecording;Format(iii)
usesfull16channelsandfull10srecording. Duringfine-tuning,wethenremovethepredictionlayers
fromthesepre-trainedmodelandaddanewpredictionlayertofittheTUEVdataset.
Figure4: Fine-tunedonTUEVfromdifferentsupervisedpre-trainedmodels(bestnumberinbold).
Similarsupervisedfine-tuninganalysisonCHB-MITdatasetisshowninAppendixB.2.
The results are shown in Figure 4 where we also add the vanilla BIOT (trained from scratch) for
references. Wefindthat(i)themodelpre-trainedonIIICSeizureandTUABaregenerallybeneficial
for the event classification task on TUEV. The reason might be that TUAB and TUEV are both
recordedfromTempleUniversityandsharesomecommoninformation,whileIIICseizureandTUEV
are both related to seizure detection and may share some latent patterns. (ii) More pre-training
datawillbebeneficialinthedownstreamtask. Thoughthepre-trainingconfiguration(16channels,
5 seconds) aligns better with the TUEV data formats, the results show that configuration of (16
channels,10seconds)encodeslongerdurationandworksconsistentlybetter. (iii)Comparedtothe
TUEVresultsinAppendixB.1,wealsofindthatoftentimesthesupervisedpre-training(e.g.,onIIIC
seizureorTUAB)canbemoreeffectivethanunsupervisedpre-training(e.g.,onSHHSandPREST).
3.6 Pre-trainedonallEEGdatasets
Inthissection,weshowthatBIOTcanleverageallsixEEGresourcesconsideredinthepaper. We
obtainaPre-trained(6EEGdatasets)modelbyloadingthePre-trained(PREST+SHHS)model
andfurthertrainitonthetrainingsetsofCHB-MIT,IIICSeizure,TUAB,andTUEV.Weaddseparate
classificationlayersforfourtasks. Essentially,thismodelispre-trainedonallsixEEGdatasets. To
usethemodel,westillfine-tuneitonthetrainingsetofdownstreamtasksandappendtheresultsto
Table2andAppendixB.1. Apparently,Pre-trained(sixEEGdatasets)outperformsthevanillaBIOT
andisgenerallybetterthantheunsupervisedandthesupervisedpre-trainedBIOT.
4 Conclusion
Thispaperproposesanewbiosignaltransformermodel(BIOT)thatlearnsembeddingsforbiosignals
withvariablelengths,channelsandmissingvalues. BIOTcanenableeffectiveknowledgetransfer
acrossdifferentdataandallowjointtrainingonmultiplesources. Weconductextensiveevaluations
ontwolargeEEGcorpus(5Meach)forunsupervisedpre-training,andseveralEEG,ECG,human
actionsensorydatasetsforsupervisedlearning. TheresultsshowthatourBIOToutperformsstrong
baselinesinstandardsupervisedlearningandcaneffectivelyhandlethelearningsettingswithmissing
values. Thepre-trainedBIOTmodelsalsoshowsignificantimprovementsonvariousdownstream
classificationtasks. Intheend,wehopeourworkcaninspiremorefollow-upresearchesoflarge
foundationalmodelsforbiosignals.
9

References
Alday,E.A.P.,Gu,A.,Shah,A.J.,Robichaux,C.,Wong,A.-K.I.,Liu,C.,Liu,F.,Rad,A.B.,Elola,
A.,Seyedi,S.,etal.(2020). Classificationof12-leadecgs: thephysionet/computingincardiology
challenge2020. Physiologicalmeasurement,41(12):124003.
Almutairi,H.,Hassan,G.M.,andDatta,A.(2021). Detectionofobstructivesleepapnoeabyecg
signalsusingdeeplearningarchitectures. In202028thEuropeansignalprocessingconference
(EUSIPCO),pages1382–1386.IEEE.
Anguita,D.,Ghio,A.,Oneto,L.,Parra,X.,Reyes-Ortiz,J.L.,etal.(2013). Apublicdomaindataset
forhumanactivityrecognitionusingsmartphones. InEsann,volume3,page3.
Ba, J. L., Kiros, J. R., and Hinton, G. E. (2016). Layer normalization. arXiv preprint
arXiv:1607.06450.
Bahador, N., Jokelainen, J., Mustola, S., and Kortelainen, J. (2021). Reconstruction of missing
channelinelectroencephalogramusingspatiotemporalcorrelation-basedaveraging. Journalof
NeuralEngineering,18(5):056045.
Biswal,S.,Sun,H.,Goparaju,B.,Westover,M.B.,Sun,J.,andBianchi,M.T.(2018). Expert-level
sleepscoringwithdeepneuralnetworks. JournaloftheAmericanMedicalInformaticsAssociation,
25(12):1643–1650.
Chen,T.,Kornblith,S.,Norouzi,M.,andHinton,G.(2020). Asimpleframeworkforcontrastive
learningofvisualrepresentations. InInternationalconferenceonmachinelearning,pages1597–
1607.PMLR.
Clevert,D.-A.,Unterthiner,T.,andHochreiter,S.(2015). Fastandaccuratedeepnetworklearningby
exponentiallinearunits(elus). arXivpreprintarXiv:1511.07289.
Cui,H.,Liu,A.,Zhang,X.,Chen,X.,Wang,K.,andChen,X.(2020).Eeg-basedemotionrecognition
usinganend-to-endregional-asymmetricconvolutionalneuralnetwork.Knowledge-BasedSystems,
205:106243.
Dar,M.N.,Akram,M.U.,Khawaja,S.G.,andPujari,A.N.(2020). Cnnandlstm-basedemotion
chartingusingphysiologicalsignals. Sensors,20(16):4551.
Devlin,J.,Chang,M.-W.,Lee,K.,andToutanova,K.(2018). Bert: Pre-trainingofdeepbidirectional
transformersforlanguageunderstanding. arXivpreprintarXiv:1810.04805.
Dosovitskiy,A.,Beyer,L.,Kolesnikov,A.,Weissenborn,D.,Zhai,X.,Unterthiner,T.,Dehghani,M.,
Minderer,M.,Heigold,G.,Gelly,S.,etal.(2020). Animageisworth16x16words: Transformers
forimagerecognitionatscale. arXivpreprintarXiv:2010.11929.
Du,Y.,Xu,Y.,Wang,X.,Liu,L.,andMa,P.(2022). Eegtemporal–spatialtransformerforperson
identification. ScientificReports,12(1):14378.
Ge,W.,Jing,J.,An,S.,Herlopian,A.,Ng,M.,Struck,A.F.,Appavu,B.,Johnson,E.L.,Osman,G.,
Haider,H.A.,etal.(2021). Deepactivelearningforinterictalictalinjurycontinuumeegpatterns.
Journalofneurosciencemethods,351:108966.
Gong,Y.,Chung,Y.-A.,andGlass,J.(2021). Ast: Audiospectrogramtransformer. arXivpreprint
arXiv:2104.01778.
Greco,A.,Valenza,G.,Lázaro,J.,Garzón-Rey,J.M.,Aguiló,J.,De-laCamara,C.,Bailón,R.,and
Scilingo,E.P.(2021). Acutestressstateclassificationbasedonelectrodermalactivitymodeling.
IEEETransactionsonAffectiveComputing.
Grill,J.-B.,Strub,F.,Altché,F.,Tallec,C.,Richemond,P.,Buchatskaya,E.,Doersch,C.,AvilaPires,
B.,Guo, Z.,GheshlaghiAzar,M., etal.(2020). Bootstrapyourownlatent-anewapproachto
self-supervisedlearning. Advancesinneuralinformationprocessingsystems,33:21271–21284.
10

Harati,A.,Golmohammadi,M.,Lopez,S.,Obeid,I.,andPicone,J.(2015). Improvedeegevent
classificationusingdifferentialenergy. In2015IEEESignalProcessinginMedicineandBiology
Symposium(SPMB),pages1–4.IEEE.
He, K., Fan, H., Wu, Y., Xie, S., andGirshick, R.(2020). Momentumcontrastforunsupervised
visualrepresentationlearning. InProceedingsoftheIEEE/CVFconferenceoncomputervision
andpatternrecognition,pages9729–9738.
He,K.,Zhang,X.,Ren,S.,andSun,J.(2016). Deepresiduallearningforimagerecognition. In
ProceedingsoftheIEEEconferenceoncomputervisionandpatternrecognition,pages770–778.
Isin,A.andOzdalili,S.(2017).Cardiacarrhythmiadetectionusingdeeplearning.Procediacomputer
science,120:268–275.
Jing,J.,d’Angremont,E.,Zafar,S.,Rosenthal,E.S.,Tabaeizadeh,M.,Ebrahim,S.,Dauwels,J.,and
Westover,M.B.(2018). Rapidannotationofseizuresandinterictal-ictalcontinuumeegpatterns.
In201840thAnnualInternationalConferenceoftheIEEEEngineeringinMedicineandBiology
Society(EMBC),pages3394–3397.IEEE.
Jing,J.,Ge,W.,Hong,S.,Fernandes,M.B.,Lin,Z.,Yang,C.,An,S.,Struck,A.F.,Herlopian,A.,
Karakis,I.,etal.(2023). Developmentofexpert-levelclassificationofseizuresandrhythmicand
periodicpatternsduringeeginterpretation. Neurology.
Jing,J.,Sun,H.,Kim,J.A.,Herlopian,A.,Karakis,I.,Ng,M.,Halford,J.J.,Maus,D.,Chan,F.,
Dolatshahi,M.,etal.(2020). Developmentofexpert-levelautomateddetectionofepileptiform
dischargesduringelectroencephalograminterpretation. JAMAneurology,77(1):103–108.
Katharopoulos, A., Vyas, A., Pappas, N., and Fleuret, F. (2020). Transformers are rnns: Fast
autoregressivetransformerswithlinearattention. InProceedingsoftheInternationalConference
onMachineLearning(ICML).
Kim, M.-G., Ko, H., and Pan, S. B. (2020). A study on user recognition using 2d ecg based on
ensembleofdeepconvolutionalneuralnetworks. JournalofAmbientIntelligenceandHumanized
Computing,11:1859–1867.
Klem,G.H.,Lüders,H.,Jasper,H.H.,andElger,C.E.(1999). Theten-twentyelectrodesystemof
theinternationalfederation.theinternationalfederationofclinicalneurophysiology. Electroen-
cephalographyandclinicalneurophysiology.Supplement,52:3–6.
Kostas,D.,Aroca-Ouellette,S.,andRudzicz,F.(2021). Bendr: usingtransformersandacontrastive
self-supervised learning task to learn from massive amounts of eeg data. Frontiers in Human
Neuroscience,15:653659.
Lawhern,V.J.,Solon,A.J.,Waytowich,N.R.,Gordon,S.M.,Hung,C.P.,andLance,B.J.(2018).
Eegnet: acompactconvolutionalneuralnetworkforeeg-basedbrain–computerinterfaces. Journal
ofneuralengineering,15(5):056013.
Li,H.,Ding,M.,Zhang,R.,andXiu,C.(2022). Motorimageryeegclassificationalgorithmbased
oncnn-lstmfeaturefusionnetwork. Biomedicalsignalprocessingandcontrol,72:103342.
Lin,T.-Y.,Goyal,P.,Girshick,R.,He,K.,andDollár,P.(2017). Focallossfordenseobjectdetection.
InProceedingsoftheIEEEinternationalconferenceoncomputervision,pages2980–2988.
Liu,J.,Zhang,L.,Wu,H.,andZhao,H.(2021). Transformersforeegemotionrecognition. arXiv
preprintarXiv:2110.06553.
Liu,Y.,Ott,M.,Goyal,N.,Du,J.,Joshi,M.,Chen,D.,Levy,O.,Lewis,M.,Zettlemoyer,L.,and
Stoyanov,V.(2019). Roberta: Arobustlyoptimizedbertpretrainingapproach. arXivpreprint
arXiv:1907.11692.
Lopez, S., Suarez, G., Jungreis, D., Obeid, I., and Picone, J. (2015). Automated identification
ofabnormaladulteegs. In2015IEEESignalProcessinginMedicineandBiologySymposium
(SPMB),pages1–5.IEEE.
11

Nagabushanam, P., George, S.T., Davu, P., Bincy, P., Naidu, M., andRadha, S.(2020). Artifact
removalusingellipticfilterandclassificationusing1d-cnnforeegsignals.In20206thInternational
Conference on Advanced Computing and Communication Systems (ICACCS), pages 551–556.
IEEE.
Nyquist,H.(1928). Certaintopicsintelegraphtransmissiontheory. TransactionsoftheAmerican
InstituteofElectricalEngineers,47(2):617–644.
OpenAI(2023). Gpt-4technicalreport.
Parvaneh,S.,Rubin,J.,Babaeizadeh,S.,andXu-Wilson,M.(2019). Cardiacarrhythmiadetection
usingdeeplearning: Areview. Journalofelectrocardiology,57:S70–S74.
Peh, W. Y., Yao, Y., and Dauwels, J. (2022). Transformer convolutional neural networks for
automatedartifactdetectioninscalpeeg. In202244thAnnualInternationalConferenceofthe
IEEEEngineeringinMedicine&BiologySociety(EMBC),pages3599–3602.IEEE.
Phan,H.andMikkelsen,K.(2022). Automaticsleepstagingofeegsignals: recentdevelopment,
challenges,andfuturedirections. PhysiologicalMeasurement.
Quan, S. F., Howard, B.V., Iber, C., Kiley, J.P., Nieto, F.J., O’Connor, G. T., Rapoport, D. M.,
Redline,S.,Robbins,J.,Samet,J.M.,etal.(1997). Thesleephearthealthstudy: design,rationale,
andmethods. Sleep,20(12):1077–1085.
Sakhavi, S., Guan, C., and Yan, S. (2018). Learning temporal information for brain-computer
interfaceusingconvolutionalneuralnetworks. IEEEtransactionsonneuralnetworksandlearning
systems,29(11):5619–5629.
Schirrmeister, R. T., Springenberg, J. T., Fiederer, L. D. J., Glasstetter, M., Eggensperger, K.,
Tangermann,M.,Hutter,F.,Burgard,W.,andBall,T.(2017). Deeplearningwithconvolutional
neuralnetworksforeegdecodingandvisualization. Humanbrainmapping,38(11):5391–5420.
Shannon,C.E.(1949).Communicationinthepresenceofnoise.ProceedingsoftheIRE,37(1):10–21.
Shoeb, A. H. (2009). Application of machine learning to epileptic seizure onset detection and
treatment. PhDthesis,MassachusettsInstituteofTechnology.
Song,Y.,Jia,X.,Yang,L.,andXie,L.(2021). Transformer-basedspatial-temporalfeaturelearning
foreegdecoding. arXivpreprintarXiv:2106.11170.
Srivastava,N.,Hinton,G.,Krizhevsky,A.,Sutskever,I.,andSalakhutdinov,R.(2014). Dropout: a
simplewaytopreventneuralnetworksfromoverfitting. Thejournalofmachinelearningresearch,
15(1):1929–1958.
Suhaimi,N.S.,Mountstephens,J.,Teo,J.,etal.(2020). Eeg-basedemotionrecognition: Astate-of-
the-artreviewofcurrenttrendsandopportunities. Computationalintelligenceandneuroscience,
2020.
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., and
Polosukhin, I. (2017). Attention is all you need. Advances in neural information processing
systems,30.
Venkatachalam,K.,Devipriya,A.,Maniraj,J.,Sivaram,M.,Ambikapathy,A.,andIraj,S.A.(2020).
Anovelmethodofmotorimageryclassificationusingeegsignal. Artificialintelligenceinmedicine,
103:101787.
Wagner,P.,Strodthoff,N.,Bousseljot,R.-D.,Kreiseler,D.,Lunze,F.I.,Samek,W.,andSchaeffter,T.
(2020). Ptb-xl,alargepubliclyavailableelectrocardiographydataset. Scientificdata,7(1):154.
Wang,S.,Li,B.Z.,Khabsa,M.,Fang,H.,andMa,H.(2020). Linformer: Self-attentionwithlinear
complexity. arXivpreprintarXiv:2006.04768.
Yang, C., Qian, C., Singh, N., Xiao, C. D., Westover, M., Solomonik, E., and Sun, J. (2022a).
Atd: Augmentingcptensordecompositionbyselfsupervision. AdvancesinNeuralInformation
ProcessingSystems,35:32039–32052.
12

Yang,C.,Westover,M.B.,andSun,J.(2023). Manydg: Many-domaingeneralizationforhealthcare
applications. InTheEleventhInternationalConferenceonLearningRepresentations.
Yang, C., Wu, Z., Jiang, P., Lin, Z., and Sun, J. (2022b). Pyhealth: A deep learning toolkit for
healthcarepredictivemodeling,092022. URLhttps://github.com/sunlabuiuc/PyHealth.
Yang,C.,Xiao,D.,Westover,M.B.,andSun,J.(2021). Self-supervisedeegrepresentationlearning
forautomaticsleepstaging. arXivpreprintarXiv:2110.15278.
Zhang,G.-Q.,Cui,L.,Mueller,R.,Tao,S.,Kim,M.,Rueschman,M.,Mariani,S.,Mobley,D.,and
Redline,S.(2018). Thenationalsleepresearchresource: towardsasleepdatacommons. Journal
oftheAmericanMedicalInformaticsAssociation,25(10):1351–1358.
Zhang, R., Zong, Q., Dou, L., and Zhao, X. (2019). A novel hybrid deep learning scheme for
four-classmotorimageryclassification. Journalofneuralengineering,16(6):066004.
Zhang,X.,Zhao,Z.,Tsiligkaridis,T.,andZitnik,M.(2022). Self-supervisedcontrastivepre-training
fortimeseriesviatime-frequencyconsistency. arXivpreprintarXiv:2206.08496.
Zhang,Y.,Chen,J.,Tan,J.H.,Chen,Y.,Chen,Y.,Li,D.,Yang,L.,Su,J.,Huang,X.,andChe,W.
(2020). Aninvestigationofdeeplearningmodelsforeeg-basedemotionrecognition. Frontiersin
Neuroscience,14:622759.
A DetailsofDatasetsandExperimentalSettings
A.1 MoreforDatasetsandProcessings
Weprovidemoredescriptionsoneachdatasetinthissection.
ForEEGdatasets. First,the16montages(in10-20internationalsystem)are"FP1-F7","F7-T7",
"T7-P7","P7-O1","FP2-F8","F8-T8","T8-P8","P8-O2","FP1-F3","F3-C3","C3-P3","P3-O1",
"FP2-F4","F4-C4","C4-P4","P4-O2".
• Sleep Heart Health Study (SHHS) (Zhang et al., 2018; Quan et al., 1997) is a multi-center
cohortstudyfromtheNationalHeartLung&BloodInstituteassembledtostudysleep-disordered
breathing,whichcontains5,445recordings. Thedataisaccessibleuponrequestintheirwebsite3.
Eachrecordinghas14Polysomnography(PSG)channels,andtherecordingfrequencyis125.0Hz.
WeusetheC3/A2andC4/A1EEGchannels. Thedatasetisreleasedwithsleepannotations. We
usetheexistingcodes4 andspliteachrecordingsinto30-secondsamples. Inthisstudy,weuse
SHHSsamplesforunsupervisedpre-trainingwithoutitoriginallabels.
• PRESTisaprivatedatasetrecordedinhospitalsleeplab,primarilyforseizureandabnormalEEG
detectionpurpose(suchasspikes). ThelocalIRBwaivedtherequirementforinformedconsent
forthisretrospectiveanalysisofEEGdata. Wefollowtheclinician’sinstructionsandspliteach
recordingsinto10secondswithoutlabels. Intheexperiment,weuseitforEEGmodelpre-training.
• TheCHB-MITdatabase5(Shoeb,2009)ispubliclyavailable,whichiscollectedattheChildren’s
HospitalBoston,consistsofEEGrecordingsfrompediatricsubjectswithintractableseizures. The
datasetisunderOpenDataCommonsAttributionLicensev1.06 andisusedtopredictwhether
theEEGrecordingscontainseizuresignals. Eachrecordinginitiallycontains23bipolarchannels
andweselectthe16standardmontagesintheexperiments. Weutilizetheexistingpreprocessing7
andfollowthetypicalpracticestofurtherspliteachrecordingsinto10-secondnon-overlapping
samplesbydefault. Sincethedatasetishighlyimbalanced,weuse5secondsasoverlapstosplit
theseizureregions(whichcouldpotentiallydoublethepositivesamples). Afterprocessing,the
positiveratiointhetrainingsetisaround0.6%.
3https://sleepdata.org/datasets/shhs
4https://github.com/ycq091044/ContraWR/tree/main/preprocess
5https://physionet.org/content/chbmit/1.0.0/
6https://physionet.org/content/chbmit/view-license/1.0.0/
7https://github.com/bernia/chb-mit-scalp
13

• IIIC Seizure is requested from Jing et al. (2018); Ge et al. (2021); Jing et al. (2023), and we
followthelicenseandusagestatementsinJingetal.(2023). Thesamplesfollow16montages
andspan10-secondsignalsat200Hz. Thisdatasetisusedforpredictingoneofthesixclasses:
lateralizedperiodicdischarges(LPD),generalizedperiodicdischarges(GPD),lateralizedrhythmic
deltaactivity(LRDA),generalizedrhythmicdeltaactivity(GRDA),Seizuretypes,andOther.
• TUHAbnormalEEGCorpus(TUAB)(Lopezetal.,2015)andTUHEEGEvents(TUEV)(Harati
et al., 2015) is accessible upon request at Temple University Electroencephalography (EEG)
Resources8. Weprocessbothdatasetstofollowthe16EEGmontages.
ForECGdatasets. WeusetheCardiologycollectiontopre-traintheECGmodelsandapplyiton
downstreamsupervisdPTB-XLtask.
• The Cardiology collection (Alday et al.,2020) ispublicly availableat physionet 9, which was
usedinthePhysioNet/ComputinginCardiologyChallenge2020. ThiscollectionisunderCreative
CommonsAttribution4.0InternationalPublicLicense10. Inthisstudy,weusefivesetsfromthe
trainingportionofthecollection(Ithasintotalsixsets. AnotheroneoverlapswiththePTB-XL
dataset,andthuswedropitinthepre-training),whichcontainsrecordingsfromCPSC2018(6,877
recordings), CPSC2018Extra (China 12-Lead ECG Challenge Database – unused CPSC 2018
data,3,453recordings),StPetersburgIncart(12-leadArrhythmiaDatabase,74recordings),ptb
(DiagnosticECGDatabase,516recordings),Georgia(12-LeadECGChallengeDatabase,10,344
recordings). Forpreprocessing,weextract10-secondsamplesfromeachrecordingwith0.5sasthe
overlappingwindow. Allthesamplesaremergedtogetherasanunsupervisedpre-trainingECG
corpusofnearly0.5millionsamples. Wepre-trainaPre-trainedBIOT(Cardiology-12)onallthe
channelsandaPre-trainedBIOT(Cardiology-6)onthefirst6-channelsofallsamples. Thesample
sizesaredifferentfromthebelowPTB-XLdataset.
• Physikalisch-TechnischeBundesanstalt(PTB-XL)11(Wagneretal.,2020)isapubliclyavailable
largedatasetof12-leadECGsfrom18885patients. ItisundertheCreativeCommonsAttribution
4.0InternationalPublicLicense12.Therawwaveformdatawasannotatedbyuptotwocardiologists,
who assigned potentially multiple ECG statements to each record up to 27 diagnoses: 1:1st
degree AV block, 2:Atrial fibrillation, 3:Atrial flutter, 4:Bradycardia, 5:Complete right bundle
branch block, 6:Incomplete right bundle branch block, 7:Left anterior fascicular block, 8:Left
axisdeviation,9:Leftbundlebranchblock,10:LowQRSvoltages,11:Nonspecificintraventricular
conductiondisorder,12:Pacingrhythm,13:Prematureatrialcontraction,14:Prematureventricular
contractions,15:ProlongedPRinterval,16:ProlongedQTinterval,17:Qwaveabnormal,18:Right
axisdeviation,19:Rightbundlebranchblock,20:Sinusarrhythmia,21:Sinusbradycardia,22:Sinus
rhythm,23:Sinustachycardia,24:Supraventricularprematurebeats,25:Twaveabnormal,26:T
waveinversion, 27:Ventricularprematurebeats. Wefollowingclinicalknowledgesandfurther
groupsthemintosixbroadercategories: Arrhythmias,Bundlebranchblocksandfascicularblocks,
Axis deviations, Conduction delays, Wave abnormalities, Miscellaneous. Each recordings can
beassociatedtomultiplecategories. Inthispaper,weconductthe"Arrhythmias"phenotyping
predictiontask. IftherecordingshaveatleastonediagnosisbelongingtotheArrhythmiasgroup,
thenwelabelthemaspositive,otherwiseasnegative.
Forhumanactivitysensorydata. Humanactivityrecognition(HAR)dataset13 (Anguitaetal.,
2013)ispubliclyavailableatUCImachinelearningrepository.Thedataiscollectedfromsmartphone
accelerometer and gyroscope data with 3D coordinates to detect six actions: walking, walking
upstairs,walkingdownstairs,sitting,standing,laying. Thesamplesarealreadysplittedandprovided
intheoriginaldatasets.
8https://isip.piconepress.com/projects/tuh_eeg/html/downloads.shtml
9https://physionet.org/content/challenge-2020/1.0.2/
10https://physionet.org/content/challenge-2020/view-license/1.0.2/
11https://physionet.org/content/ptb-xl/1.0.1/
12https://physionet.org/content/ptb-xl/view-license/1.0.1/
13https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones
14

A.2 MoreforExperimentalSettings
Formodelimplementation, theSPaRCNetcodeisrequestedfromtheauthors(Jingetal.,2023),
the ContraWR code isdownloaded and modified uponthe github 14, CNN-Transformer is easily
implementedfollowingtheFig. 3oftheoriginalpaper(Pehetal.,2022), FFCL(Lietal.,2022)
combinesaCNNmodelandaLSTMmodelforlearningsepareterepresentationsandthenmerges
thembeforethefinalpredictionlayer,theimplementationofST-Transformerrefertothisrepo15.
Thelinear-complexityattentionmoduleisreferredtothisrepo16inourBIOTimplementation.
ForallEEGtasks,weresamplethedatasetsinto200Hz. TheECGtasksuse500Hz,andtheHAR
tasksuse50Hzbydefault. Foreachspecifictasks,wehavetoadjustthebaselinemodelarchitectures
(e.g,numberoflayers,inputchannelsizes,etc)accordinglysincetheinputdatahavevariousformats.
WhileforourBIOT,weonlyadjustthefftsizebasedontheirsamplingrate(200pointsforEEG,
1000 points for ECG, 100 points for HAR) and use 100 points, 200 points, and 10 points as the
hoplength(i.e.,overlaps)inthreesignaltypes. Theseconfigurationsarechosenbytestingseveral
other combinations based on the validation performance. For our BIOT model, we use 8 as the
numberofhead,4asthenumberoftransformerlayers,andT =2asthetemperatureinunsupervised
pre-training by default. We use the Adam optimizer with learning rate 1×10−3 and 1×10−5
asthecoefficientforL2regularizationbydefault. Weusethepytorchlightningframework(with
100 as the max epoch) to handle the training, validation, and test pipeline by setting AUROC as
the monitoring metirc for binary classification and Coken’s Kappa as the monitoring metric for
multi-classclassification. MoredetailscanrefertoourSupplementarycodes. Below,weprovide
thedefinitionofeachmetricusedinthepaper,andweusepyhealth.metrics17 Yangetal.(2022b)
modulefortheimplementation.
BalancedAccuracyisdefinedastheaverageofrecallobtainedoneachclass. Itisusedforboth
binaryclassificationandmulti-classclassification.
AUC-PRistheareaundertheprecisionrecall(PR)curveforbinaryclassificationtask.
AUROCistheareaundertheROCcurve,summarizingtheROCcurveintoansinglenumberthat
describestheperformanceofamodelformultiplethresholdsatthesametime. Itisusedforbinary
classification.
Coken’s Kappa is a statistic that measures inter-annotator agreement, which is usually used for
imbalancedmulti-classclassificationtask. Thecalculationcanrefertosklearnmetrics18.
Weighted F1 is used for multi-class classification in this paper, which is a weighted average of
individualF1-scoresfromeachclass, witheachscoreweightedbythenumberofsamplesinthe
correspondingclass.
B AdditionalResults
Thissectionprovidesadditionalexperimentalresultstosupportclaimsinthemainpaper.
B.1 AdditionalExperimentsonTUEVandTUAB
WehaveprovidedthesupervisedlearningresultsonEEGdatasetIIICSeizureandCHB-MITinthe
maintext. Forcompleteness,weprovidesimilarcomparisonresultsonTUABandTUEVbelow
inTable45,whichshowasimilartrendthatourBIOTshowsbetterperformanceagainstbaseline
models,andthepre-trainedBIOTmodelscanbringsignificantimprovementsontwodownstream
tasks,especiallyonTUEV.ForTUEV,wealsoappendtheresultsofalldifferentpre-trainedmodels
(e.g.,trainfromscratch,supervisedtraining,unsupervisedtraining,etc)intheendinTable5.
14https://github.com/ycq091044/ContraWR
15https://github.com/eeyhsong/EEG-Transformer
16https://github.com/lucidrains/linear-attention-transformer
17https://pyhealth.readthedocs.io/en/latest/api/metrics.html
18https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html
15

Table4: AdditionalSupervisedLearningResultsonTUAB
TUAB(abnormaldetection)
Models
|          | BalancedAcc.  | AUC-PR        | AUROC         |     |
| -------- | ------------- | ------------- | ------------- | --- |
| SPaRCNet | 0.7896±0.0018 | 0.8414±0.0018 | 0.8676±0.0012 |     |
|          | 0.7746±0.0041 | 0.8421±0.0104 | 0.8456±0.0074 |     |
ContraWR
| CNN-Transformer               | 0.7777±0.0022 | 0.8433±0.0039 | 0.8461±0.0013 |     |
| ----------------------------- | ------------- | ------------- | ------------- | --- |
| FFCL                          | 0.7848±0.0038 | 0.8448±0.0065 | 0.8569±0.0051 |     |
| ST-Transformer                | 0.7966±0.0023 | 0.8521±0.0026 | 0.8707±0.0019 |     |
| (Vanilla)BIOT                 | 0.7925±0.0035 | 0.8707±0.0087 | 0.8691±0.0033 |     |
| Pre-trainedBIOT(PREST)        | 0.7907±0.0050 | 0.8752±0.0051 | 0.8730±0.0021 |     |
| Pre-trainedBIOT(PREST+SHHS)   | 0.8019±0.0021 | 0.8749±0.0054 | 0.8739±0.0019 |     |
| Pre-trainedBIOT(6EEGdatasets) | 0.7959±0.0057 | 0.8792±0.0023 | 0.8815±0.0043 |     |
*Boldforthebestmodel(trainedfromscratch)and box forthebestpre-trainedmodels.
Table5: AdditionalSupervisedLearningResultsonTUEV(All-in-one-tablecomparison)
TUEV(eventtypeclassification)
Models
|     |     | BalancedAcc. | Coken’sKappa | WeightedF1 |
| --- | --- | ------------ | ------------ | ---------- |
(TrainingfromscratchinSection3.2
| SPaRCNet |     | 0.4161±0.0262 | 0.4233±0.0181 | 0.7024±0.0104 |
| -------- | --- | ------------- | ------------- | ------------- |
| ContraWR |     | 0.4384±0.0349 | 0.3912±0.0237 | 0.6893±0.0136 |
|          |     | 0.4087±0.0161 | 0.3815±0.0134 | 0.6854±0.0293 |
CNN-Transformer
| FFCL           |     | 0.3979±0.0104 | 0.3732±0.0188 | 0.6783±0.0120 |
| -------------- | --- | ------------- | ------------- | ------------- |
| ST-Transformer |     | 0.3984±0.0228 | 0.3765±0.0306 | 0.6823±0.0190 |
| (Vanilla)BIOT  |     | 0.4682±0.0125 | 0.4482±0.0285 | 0.7085±0.0184 |
(Unsupervisedpre-trainedmodelsinSection3.4):
Pre-trainedBIOT(PREST) 0.5207±0.0285 0.4932±0.0301 0.7381±0.0169
Pre-trainedBIOT(PREST+SHHS) 0.5149±0.0292 0.4841±0.0309 0.7322±0.0196
(Supervisedpre-trainedmodelsinSection3.5):
Pre-trainedBIOT(pre-trainedonCHB-MITwith8channelsand10s) 0.4123±0.0087 0.4285±0.0065 0.6989±0.0015
Pre-trainedBIOT(pre-trainedonCHB-MITwith16channelsand5s) 0.4218±0.0117 0.4427±0.0093 0.7147±0.0058
Pre-trainedBIOT(pre-trainedonCHB-MITwith16channelsand10s) 0.4344±0.0065 0.4719±0.0231 0.7280±0.0126
Pre-trainedBIOT(pre-trainedonIIICseizurewith8channelsand10s) 0.4956±0.0552 0.4719±0.0475 0.7214±0.0220
Pre-trainedBIOT(pre-trainedonIIICseizurewith16channelsand5s) 0.4894±0.0189 0.4881±0.0045 0.7348±0.0056
Pre-trainedBIOT(pre-trainedonIIICseizurewith16channelsand10s) 0.4935±0.0288 0.5316±0.0176 0.7555±0.0111
Pre-trainedBIOT(pre-trainedonTUABwith8channelsand10s) 0.4980±0.0384 0.4487±0.0535 0.7044±0.0365
Pre-trainedBIOT(pre-trainedonTUABwith16channelsand5s) 0.4954±0.0305 0.5053±0.0079 0.7447±0.0049
Pre-trainedBIOT(pre-trainedonTUABwith16channelsand10s) 0.5256±0.0348 0.5187±0.0160 0.7504±0.0102
(Supervised+unsupervisedpre-trainedmodelinSection3.6):
Pre-trainedBIOT(ultimate) 0.5281±0.0225 0.5273±0.0249 0.7492±0.0082
B.2 AdditionalExperimentsonCHB-MIT
ThissectionperformsasimilarexperimentonCHB-MIT,similartoSection3.2. Wepre-trainonthe
trainingsetofIIICSeizure(whichhas16channelsand10sduration),TUAB(whichhas16channels
and 10s duration), TUEV (which has 16 channels and 5s duration) and fine-tunes on CHB-MIT
(whichhas16channelsand10sduration). Alldatasetsuse200Hzsamplingrate. Wedesignfivesets
ofconfigurationsforthepre-traineddatasets: Format(i)usesthefirst8channelsand10sduration;
Format(ii)usesthefull16channelsbutonlythefirst5srecording;Format(iii)usesfull16channels
andfull10srecording;Format(iv)uses8channelsand5srecording,andFormat(v)usesfull16
channelsand2.5srecording. ThelasttwoareonlyfortheTUEVdataset. Duringfine-tuning,we
thenremovethepredictionlayersfromthesepre-trainedmodelandaddanewpredictionlayertofit
theCHB-MITdataset.
The results are reported in Figure 5, which shows that the supervised pre-training on both IIIC
seizureandTUEVcanhelpimprovethedownstreamperformanceonCHB-MITtaskcomparedto
trainingfromscratch. ThereasonisthatIIICSeizureisonmultipleseizuretypeclassificationwhile
CHB-MITisonbinaryseizureornotclassification,andthecontextofbothtasksarefairlyrelated.
AlthoughTUEVisnotentirelyonseizurerelatedclassification,someclassesinTUEVareseizure
subtypes(suchasGPED,PLED),andthusitssupervisdpre-trainedmodelscanalsobringbenefits
fortheCHB-MITtask.
16

Figure5: Fine-tunedonCHB-MITfromdifferentsupervisedpre-trainedmodels. IIICSeizureand
TUAVdatasetsfollowFormat(i)(ii)(iii),whileTUEVfollowstheFormat(iv)(v)(ii).
B.3 AblationStudiesonHyperparameters
Thissectionprovidesablationstudiesonthreehyperparametersindataprocessing: targetsampling
rate,tokenduration,andtheoverlapsizebetweentwoneighboringtokens. WeusetwoEEGdatasets
asexample: IIICSeizureandTUAB.Thedefaultconfigurationinthemainpaperis(1)sampling:
200Hz,(2)tokenlength: 1s,(3)overlaps: 0.5sasreference.
B.3.1 AblationStudyonTargetSamplingRater
Inthisexperiments,wefix(2)(3)andconductablationstudyonthetargetsamplingrate. Theoriginal
IIICSeizuredataisat200HzandtheTUABdataisat256Hz. ForIIICSeizure,wevarythesampling
rate to 26Hz, 50Hz, 100Hz, 150Hz, and 200Hz. For TUAB, we vary the sampling rate to 50Hz,
100Hz, 150Hz, 200Hz, 250Hz, and 300Hz. The evaluations are conducted under three different
randomseedsandthemeanandstandarddeviationvaluesarereported.
ForIIICSeizure,wecanobservethatahighersamplingratecouldgiveslightlybetterperformance,
especially on balanced acc. and coken’s kappa. The reason is that higher sampling rate can pre-
servemoredetailed(high-frequency)biosignalinformation. TheresultsonTUABshowsthatthe
performancesaresimilaronallsamplingrates. Weconjecturethatdifferenttasksmighthavediverse
sensitivitytothethefrequencybands. Forexample,thetaskonIIICseizureistoclassifydifferent
seizuretypes,whichmayneedtocaptureminorcluesfromhigh-frequencywaves(suchasGamma
waves(30-100Hz)),whiletheTUABdatasetisforabnormaldetection,andusingbrainwavesunder
50Hzmightbeenoughforthetask. Insum,thetargetsamplingrateshouldbeselectedbasedonthe
predictingtargets.
B.3.2 AblationStudyonTokenLengthst
Inthisexperiments,wefix(1)(3)andconductablationstudyonthetokenlength. Bothdatasetshave
10sastheentiresamplelengthand0.5sastheoverlaplengths. Forbothofthem,wevarythetoken
lengthsto0.75s,1s,1.5s,2s,2.5s,5s. Theevaluationsareconductedunderthreedifferentrandom
seedsandthemeanandstandarddeviationvaluesarereported.
Foreachconfiguration,wealsovarythefftsizetomatchthetokenlength,whichmeansthat5stoken
lengthcanextractmorefrequencyinformation. However,wefindthatbyincreasingthetokenlengths,
themodelperformancestartstodecrease. PerformancesonIIICSeizurestartstodecreaseafter1s
whiletheperformanceonTUABdecreasesafter2s. Thereasoncouldbethatgiventheincreaseing
tokenlengthst,thetotalbiosignal"sentence"length,whichis J −t +1= 10−t +1,willdecrease
t−p t−0.5
(here, J isthechannelbiosignalduration, tisthetokenlength, pistheoverlappinglength). For
example,withx=5asthetokenlengths,thefinal"sentence"lengthbecomes11whileitis19inthe
17

Figure6: AblationStudyonTargetSamplingRater
defaultconfigurationwithx=1s. Theperformancedropsisduetotransformermodelswillbeless
beneficialinshorter"sentence"s.
Figure7: AblationStudyonTokenLengthst
B.3.3 AblationStudyonOverlappingLengthsp
Inthisexperiments,wefix(1)(2)andconductablationstudyontheoverlaplengths. Bothdatasets
have 10s as the entire sample length and 1s as the token lengths. For both of them, we vary the
overlaplengthsto0.875s,0.75s,0.5s,0.25s,0s. Theevaluationsareconductedunderthreedifferent
randomseedsandthemeanandstandarddeviationvaluesarereported.
Basedonthe"sentence"lengthformula J−t+1,smalleroverlaplengthswilldecreasethe"sentence"
t−p
length. Onbothdatasets,wefindthatlargeroverlapscanbringsslightlybetterresultsduetothat
thebiosignal"sentence"becomeslonger. Anotherreasonisthatwithlargeroverlaps,neighboring
tokenscancapturemoretransitioninginformationandhelpthetransformermodeltobettercapture
thetemporalinformation.
18

Figure8: AblationStudyonOverlappingLengthspBetweenTokens
19