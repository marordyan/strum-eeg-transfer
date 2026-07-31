| REVE:       |          | A   | Foundation  |        | Model |        | for      | EEG |
| ----------- | -------- | --- | ----------- | ------ | ----- | ------ | -------- | --- |
|             | Adapting |     |             | to Any | Setup |        | with     |     |
| Large-Scale |          |     | Pretraining |        | on    | 25,000 | Subjects |     |
YassineElOuahidi1∗,JonathanLys1,PhilippThölke2,NicolasFarrugia1,
BastienPasdeloup1,VincentGripon1,KarimJerbi2,3,4,GiuliaLioi1∗
5202 tcO 42  ]GL.sc[  1v58512.0152:viXra
1IMTAtlantique,Lab-STICC,UMRCNRS6285,F-29238Brest,France
2PsychologyDepartment,UniversitédeMontréal,Montreal,QC,Canada
3Mila(QuebecAIresearchinstitute),Montreal,QC,Canada
4UNIQUE(QuebecNeuro-AIresearchcenter),QC,Canada
Abstract
| Foundation     | models      | have   | transformed  |     | AI by reducing       | reliance | on       | task-specific    |
| -------------- | ----------- | ------ | ------------ | --- | -------------------- | -------- | -------- | ---------------- |
| data through   | large-scale |        | pretraining. |     | While successful     | in       | language | and vision,      |
| their adoption |             | in EEG | has lagged   | due | to the heterogeneity |          | of       | public datasets, |
whicharecollectedundervaryingprotocols,devices,andelectrodeconfigurations.
| Existing | EEG foundation |     | models | struggle | to generalize |     | across these | variations, |
| -------- | -------------- | --- | ------ | -------- | ------------- | --- | ------------ | ----------- |
oftenrestrictingpretrainingtoasinglesetup,resultinginsuboptimalperformance,
| inparticularunderlinearprobing. |     |     |     | WepresentREVE(RepresentationforEEGwith |     |     |     |     |
| ------------------------------- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- |
VersatileEmbeddings),apretrainedmodelexplicitlydesignedtogeneralizeacross
| diverseEEGsignals. |       | REVEintroducesanovel4Dpositionalencodingscheme |         |              |        |     |           |              |
| ------------------ | ----- | ---------------------------------------------- | ------- | ------------ | ------ | --- | --------- | ------------ |
| that enables       | it to | process                                        | signals | of arbitrary | length | and | electrode | arrangement. |
Usingamaskedautoencodingobjective,wepretrainREVEonover60,000hoursof
EEGdatafrom92datasetsspanning25,000subjects,representingthelargestEEG
| pretrainingefforttodate. |     |     | REVEachievesstate-of-the-artresultson10downstream |     |     |     |     |     |
| ------------------------ | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- |
EEGtasks,includingmotorimageryclassification,seizuredetection,sleepstaging,
| cognitiveloadestimation,andemotionrecognition. |     |        |                 |     |             | Withlittletonofine-tuning, |     |           |
| ---------------------------------------------- | --- | ------ | --------------- | --- | ----------- | -------------------------- | --- | --------- |
| it demonstrates                                |     | strong | generalization, |     | and nuanced | spatio-temporal            |     | modeling. |
Wereleasecode,pretrainedweights,andtutorials2tosupportstandardizedEEG
researchandaccelerateprogressinclinicalneuroscience.
1 Introduction
Electroencephalography (EEG) is a non-invasive technique widely used to study brain activity,
withapplicationsspanningbrain-computerinterfaces(BCIs),clinicaldiagnostics,andneuroscience
research. Despiteitspotential,theadoptionofEEG-basedtechnologiesremainslimited(Lotteetal.,
2018). A key challenge is developing models that generalize effectively to new subjects. EEG
data varies widely in electrode configurations, recording conditions, and subject-specific factors,
complicatingmodeltransferability. Thisheterogeneityhasledtoafragmentedecosystemofdatasets
andtask-specificmodels,manyofwhichstruggletogeneralizeacrosssettings.
Foundationmodelshavetransformednaturallanguageprocessing(Achiametal.,2023;Dubeyetal.,
2024;Warneretal.,2024)andcomputervision(Radfordetal.,2021;Caronetal.,2021;Kirillov
etal.,2023)byleveraginglarge-scalepretrainingtoenabletransferwithminimalsupervision. Their
∗Correspondingauthors:yassine.elouahidi@mistral.ai,giulia.lioi@imt-atlantique.fr
2Projectpage:https://brain-bzh.github.io/reve/
39thConferenceonNeuralInformationProcessingSystems(NeurIPS2025).

abilitytoproducegeneral-purposerepresentationshassparkedgrowinginterestinbuildingsimilar
modelsforEEG(Yangetal.,2024;Wangetal.,2024b;Jiangetal.,2024;Cuietal.,2024;Yuan
etal.,2024b;Wangetal.,2024a). Yet,EEGposesuniquechallengesincludingdataheterogeneity,
lowsignal-to-noiseratio,andthelackofstandardizedpositionalencodingtoaccommodatevarying
electrodeconfigurations.
Recent EEG foundation models such as BIOT (Yang et al., 2024), Labram (Jiang et al., 2024),
CBraMod (Wang et al., 2024b), and NeuroGPT (Cui et al.,2024) adopt self-supervised learning
(SSL)techniquesforpretraining. Whilepromising,manyofthesemodelsrelysolelyontheTUH
database(ObeidandPicone,2016)whichusesafixed19or21-channelmontage. Asaresult,they
oftenfailtogeneralizetodatasetswithdifferentelectrodelayoutsorrecordingsetups. Furthermore,
existing positional encoding schemes, whether absolute (Yang et al., 2024; Jiang et al., 2024) or
convolutional (Wang et al., 2024b), lack the flexibility to accommodate spatial diversity, often
necessitatingfullfine-tuningfortransfer.
ToaddressthelimitationsincurrentEEGfoundationmodels,weconsiderthreecorecontributions
thatenablescalable,generalizablerepresentationlearningacrossdiverse,large-scaleEEGdatasets.
First, weproposeanovel4DpositionalencodingschemethatenablesflexiblemodelingofEEG
signalswithvaryingtemporallengthsandelectrodeconfigurations. Unlikeexistingabsoluteorcon-
volutionalencodings,ourformulationnaturallysupportsspatialandtemporalvariability,eliminating
theneedforfixedmontagesorfine-tuningofpositionalpriors.
Thankstothisflexiblepositionalencodingmethod,weareabletotrainwithawiderrangeofEEG
configurations,allowingtoscaletolargerandmoreheterogeneousdatasets. Tothisend,wecuratethe
largestandmostdiverseEEGcorpustodate,comprisingover60,000hoursofdatafrom92datasets
and25,000subjects. Thisdiversecollectionspansclinical,BCI,andresearchdomains,providingthe
scaleanddiversitynecessaryforrobustpretraining.
Combiningarchitecturalflexibilitywithlarge-scaledataresultsinREVE(RepresentationforEEG
withVersatileEmbeddings),aspatio-temporaltransformermodeltrainedwithamodifiedmasked
autoencoder(MAE)(Heetal.,2022)objectivethatpromoteslearningbetterrepresentationsinthe
model. REVElearnsgeneral-purposeEEGrepresentationsthattransfereffectivelyacrossawide
rangeofdownstreamtasks.
REVEachievesstate-of-the-artperformanceacrossnumerousbenchmarks,includingBCIandclinical
datasets,outperformingpriorEEGfoundationmodels. Ourscalingstudiesfurthershowimproved
generalizationwithlargermodelsizes,reinforcingthebenefitsoflarge-scalepretraining. Tosupport
adoption,wereleaseopen-sourcecode,pretrainedmodelsofmultiplesizes,anddetailedtutorialsfor
applyingREVEtovariousEEGtasks. ByaddressingtheuniquechallengesofEEGwithscalable
architecturesandflexiblespatialencoding,REVEestablishesaunifiedfoundationforEEGanalysis
andpavesthewayfornewadvancesinneuroscienceandclinicalapplications.
2 Methods
Wepretrainourencoderusingamaskedautoencoderobjective.TheREVEencoderconsistsofapatch
embeddingmodule,a4Dpositionencodingmodule,andatransformerbackbone. Duringpretraining,
weapplyspatio-temporalcontiguousmaskingtothepatchembeddingsandjointlytraintheencoder
anddecodertoreconstructthemissingsegmentsofEEG,enablingtheencodertolearnrobustfeature
representations. SubsequenthyperparametervaluesarelistedinTable5intheAppendix.
2.1 EEGRepresentationandBlockMaskingstrategy
Werepresentmulti-channelEEGdataasX ∈ RC×T,whereC isthenumberofelectrodesandT
thenumberoftimesamples,electrodepositionsaregivenbyP∈RC×3,correspondingtotheir3D
coordinates. Toprocessthedata,wesegmenteachchannelintopatchesofsizew withoverlapo,
(cid:108) (cid:109)
followingBIOT(Yangetal.,2024). Thisyieldsp= T−w +1[(T −w)mod(w−o)̸=0]non-
w−o
overlappingpatches(discardinganyincompleteones),andreshapesXintoXp∈RC×p×w. Each
patchislinearlyembedded,resultinginE∈RC×p×DE,whereD
E
istheembeddingdimension.
2

Figure 1: Overview of the REVE pretraining framework. The model processes multi-channel
EEGdatathroughalinearPatchEmbeddingwheresignalsaredividedintooverlappingtemporal
patchesforeachchannelandembeddedwithalinearlayer. 4DSpatio-TemporalPositionEncoding
combinesspatialcoordinatesofelectrodeswithtemporalpatchindices,augmentedwithnoisefor
robust generalization. A Block Masking Strategy masks contiguous regions across spatial and
temporaldimensionstosimulaterealisticdisruptions. Thetransformerencoderprocessesunmasked
embeddings.Updatedembeddingsarejoinedwithlearnableplaceholdersforthemaskedtokens,from
whichrawEEGisreconstructedusingthedecoder. ThePrimaryTaskpredictsrawEEGsignals
directly,whiletheSecondaryTasktrainsasingleglobaltokenviaattentionpoolingtosummarize
theinput. BothtasksminimizeanL reconstructionloss.
1
Toenhancelearningduringpretraining,weapplyajointspatio-temporalblockmaskingstrategythat
masksstructuredregionsacrossbothspatialandtemporaldimensions. Randommasking,proposed
forEEGbyChienetal.(2022),waslaterimprovedthroughspatialmasking(MohammadiFoumani
etal.,2024;Guetscheletal.,2024). Inthiswork,weextendthemaskingstrategytothetemporal
domain.Thisbuildsoninsightsfromimagemodeling,wherestructuredmaskingoutperformsrandom
masking(Xieetal.,2022),atrendalsosupportedbyourablationresults(Table18,Appendix). As
neighboring segments of EEG, in both spatial and temporal domain, are typically similar, naive
randommaskingcouldleaveredundantinformationexposed,reducingthedifficultyofreconstruction.
Incontrast,blockmaskingbetterdisruptsthesepatterns,encouragingmoreeffectivelearning.
Ourblockmaskingstrategyisgovernedbythefollowingparameters:ThemaskingRatioM controls
r
theoverallproportionofmaskedtokens. ThespatialMaskingRadiusR andTemporalMasking
s
RadiusR respectivelydefinethespatialextent(aroundaselectedchannel)andthetimewindow
t
(aroundaselectedtoken)tobemasked. Similarly,theDropoutRatioD setsthefractionofmasked
r
tokensforwhichtheentiretimeseriesofthecorrespondingchannelisdropped,whilethedropout
RadiusR determinesthespatialneighborhoodaffectedbydropout.Fortokensnotdropped,temporal
d
masking is applied within radius R . This process yields a binary mask B ∈ RC×p, containing
t
N =⌊(1−M )·C·p⌋maskedentries(zeros)andN =C·p−N unmaskedentries(ones).
m r m¯ m
2.2 4DPositionEncodingStrategy
Unlikepriorworksthatrelyonlearnedembeddingtablesforspatialencodingvectors(Jiangetal.,
2024;Wangetal.,2024b),wedirectlygeneratepositionencodingsfromthespatio-temporalcoor-
dinatesofthetokens,allowingtheprocessingofsignalsofanylengthorEEGlayoutandenabling
bettergeneralizationtounseensetups. Morespecifically,ourmethodusesatransformationapplicable
toeachposition,utilizingtheactual3DcoordinatesandtimestepofeachEEGpatch,enablingthe
modeltohandlearbitraryelectrodeconfigurationsandsequencelengthswithoutrelyingonlearned
embeddings.
4DPositionalEncodingandSpatialAugmentation. Westartwiththespatialpositionsofthe
EEGelectrodesP ∈ RC×3,whereeachrowofPcontainsthe(x,y,z)coordinatesofachannel,
to which we add Gaussian noise with standard deviation σ . This improves generalization to
noise
diverseelectrodepositionsandensuresrobustnesstovariabilityinheadsizeorelectrodeplacement.
WeextendPwithatemporalcomponent,resultinginP ∈ RC×p×4,wherepisthenumberof
ext
3

patchesobtainedfromsegmentingEEGsignal,asdefinedinSection2.1. Thetemporaldimensionis
representedasdiscretevaluesfrom1top,scaledbyafactors toensureascalesimilartothespatial
t
dimensions.
4DFourier-BasedPositionEncoding. Buildingonthe2DapproachproposedbyDéfossezetal.
(2023),weextendtheFourierpositionalencodingmethodto4Dinourencodingstrategy,asfollows.
Eachpositionalcomponent(x,y,z,t)ofP isprojectedintoamulti-frequencyspace,usingn
ext freq
frequenciesperdimension. ThefrequencyassignmentfollowsaCartesianproductstructure,i.e.,all
combinationsoffrequenciesacrossthefourdimensionscontributetotheencoding,resultingina
flattenedvectorofdimensionn4 . Ahierarchicalperiodicityemerges: theperiodofxisn1 ,of
freq freq
yisn2 ,ofzisn3 ,andoftisn4 . Then,applyingsineandcosinetransformationsdoublesthe
freq freq freq
embeddingsize,producingapositionalvectorofdimension2·n4 . Weensurethattheembedding
freq
dimensionmatchesthehiddensizerequiredbythe4DPEmodule,withn ∈ {3,4,5}resulting
freq
inthefinalembeddingF
pe
∈RC×p×DE. The4Dencodingaddsminimalcomputeoverhead,with
sinusoidalcomputationsandasmalllinearlayer. Computationalcostscaleslinearlywiththenumber
ofinputtokens(channels×temporalpatches)andisnegligiblerelativetothetransformerbackbone.
FinalAdjustedPositionEncoding. TocomplementthefixedFourierfeatures,wealsoprocessP
ext
throughalinearlayerfollowedbyGELU(HendrycksandGimpel,2016)andLayerNorm(LeiBa
etal.,2016), producingalearnablerepresentationF
lin
∈ RC×p×DE. Thiscomponentadaptsthe
positionalencodingtothespecificdatasetandtask,andcancompensateforanytruncationinthe
Fourierbasis. ThefinalpositionalencodingisgivenbyP =LayerNorm(F +F ),combining
enc pe lin
the structured inductive bias of Fourier features with the flexibility of learned adaptation. This
vectorisaddedtothenon-maskedpatchembeddingsbeforebeingpassedtothetransformerencoder
similarly to MAE (He et al., 2022), and is consistent with standard absolute positional encoding
practices(Vaswani,2017). TheablationstudyinTable19confirmsthatthismethodoutperforms
bothfixedlearnableandpurelyMLP-basedpositionalencodingschemes.
2.3 Transformer
OurmodelextendsthestandardTransformerarchitecture(Vaswani,2017)withenhancementsthat
improveefficiencyandstability.WeuseRMSNorm(ZhangandSennrich,2019)inlieuofLayerNorm
asanormalizationlayerforbettertrainingstability,andchooseGEGLU(Shazeer,2020)asthe
activation function in the feed-forward network (FFN) layers as it outperforms standard GELU
throughmoreexpressivegatingmechanisms(GeipingandGoldstein,2023). Thischoiceisfurther
supportedbytheablationresultsinTable20. OurFFNlayersfollowatwo-layerstructurewith
anexpansionratioof 8,consistentwithdesignsfromLLaMA(Touvronetal.,2023),Qwen(Bai
3
etal.,2023)orMistral(Jiangetal.,2023). FollowingDaymaetal.(2021),weremovebiasterms
fromalllinearlayersexceptthefinaldecoderlayer. Thisreallocatestheparameterbudgettolinear
transformations, improvingefficiency. WeuseFlashAttentionv2(Dao,2024)formemoryand
computationalefficiencyintheattentionasitreducesthesoftmaxoverheadandensuresscalabilityto
longsequences,whilemaintainingthecoretransformerformulation.
2.4 MaskedEEGReconstructionMethodology
Duringpretraining,ourmodelreconstructsEEGsignalofmaskedpatchesusinginformationfrom
thevisible,unmaskedpatches. TheoverallpretrainingframeworkisillustratedinFigure1.
LetP
m
∈RNm×w,andP
m
∈RNm×w denotethemaskedandvisiblepatches,respectively,withN
m
andN asdefinedinSection2.1. TheassociatedpatchembeddingsaredenotedasE formasked
m m
patchesandE forvisiblepatches.
m
WeadopttheMAEstructurefromHeetal.(2022),withalargerencoderandalighterdecodereach
following the architecture described in Section 2.3. Only the embeddings of the visible patches
E , enriched with their positional encodings are passed through the encoder, to produce latent
m
representationsF . Maskedpatchesarerepresentedusingalearnedembedding,repeatedN times
m m
andalsoaugmentedwithpositionalencodings. Beforeenteringthedecoder,positionalencodings
arere-addedtobothvisibleandmaskedlatentpatches. Together,theyformthedecoderinputfrom
whichtherawEEGsignalofthemaskedpatchesisreconstructed.
4

UnliketheoriginalMAE,whichusesaseparatesetoffixedpositionalencodingsforthedecoder,
wereusethesameencodingforboththeencoderanddecoder. Thisdesignensuresflexibilityfor
processingEEGsignalswithvaryingtemporallengthsandelectrodeconfigurations.
Theoutputofthedecodertransformer,ispassedthroughalinearprojectionlayerthatmapslatent
patches back into the signal space, reconstructing the raw EEG signal of the masked patches.
ReconstructedpatchesminimizetheL lossrelativetotheoriginalrawEEGpatches:
1
1 (cid:88) (cid:13) (cid:13)
L= (cid:13)Pˆ(i)−P(i)(cid:13) (1)
|P m | (cid:13) m m (cid:13) 1
i∈Pm
wherePˆ(i)representsthereconstructedsignalforpatchi,andP(i)istheoriginalsignal. Wechose
m m
L lossoverL duetotheinherentlynoisynatureofEEGsignals. WhileL amplifiestheinfluence
1 2 2
ofnoise,L lossoffersgreaterrobustnessbyreducingtheimpactofoutliers.
1
Inadditiontothemainreconstructionloss,weintroduceasecondarytaskthatreconstructsmasked
patchesfromacompactglobalrepresentation. Weapplyattentionpoolingovertheoutputsofall
Multi-HeadAttention(MHA)layersintheencoder: theoutputtokens(afterFFN)fromeachMHA
blockareconcatenatedandattendedbyalearnedquerytoken. Thispooledtokenisthenrepeated,
enrichedwithpositionalencodings,andpassedthrougha2-layerFFNtoreconstructthemasked
patches. Aswiththeprimaryloss,weuseL lossforreconstruction. Thetotallossisaweighted
1
sum: Loss=PrimaryLoss+λ·SecondaryLoss
Thissecondarylossencouragestheencodertodistributeusefulinformationacrossalllayers,mitigat-
ingover-specializationinthefinallayerandyieldingmoregeneralizablerepresentations.
ThesecondarylossmitigatesalimitationoftheMAEframework: thefinalencoderlayercanoverfit
tothereconstructiontask,especiallywithashallowdecoder(Heetal.,2022). Bypoolingfeatures
acrossalltransformerlayers(Alkinetal.,2024),thelearnedtokencapturesacompact,globalEEG
representation,encouragingmorebalanceduseoftheencoderdepth. Thisleadstostronger,more
generalizable features for downstream tasks like linear probing, few-shot learning, and transfer
withoutfine-tuning.
Afterthepretrainingphase,thedecoderisdiscarded,andonlytheencoderisused. Inthiscase,no
embeddingsaremasked,i.e.,P =E =∅. Allpatchesareprocessedasusualbyretainingtheir
m m
associatedpositionalencoding.
Toavoidconfusionregardingterminology,weclarifythattheterms“encoder”and“decoder”are
used here in the context of masked auto-encoders (MAE), not in the autoregressive Transformer
sense. AllTransformerblocksinREVEarenon-causalandoperatewithinastandardencoder-style
attentionpattern;noautoregressivetrainingisinvolved.The“decoder”referssolelytothelightweight
reconstructionheadusedtorecovermaskedEEGsegmentsduringself-supervisedpretraining.
3 Experiments
3.1 Pretraining
Thissectionoutlinesthedatasourcesandpreprocessingstepsusedforpretraining,followedbyour
strategyforscalableandeffectiverepresentationlearningacrossdiversedatasets.
3.1.1 DatasetCollection&Preprocessing
Toenablelarge-scalepretraining,weassembledamassiveanddiversecollectionofEEGrecordings
fromopen-sourceorrequest-accessibledatasets. Itcomprises19TBofrawdata,spanning24,274
subjects,150,833uniquesessions,and61,415hoursofrecordingsdrawnfrom92differentsources,
includingOpenNeuro(Markiewiczetal.,2021),MOABB(Aristimunhaetal.,2023),andTUH(Obeid
andPicone,2016). Toourknowledge,thisisthelargestandmostdiverseEEGdatasetassembled
fortrainingafoundationmodel. Themostextensiveprioreffort,byYuanetal.(2024a),comprised
approximately40,000hoursofrecordings,butprimarilyreliedonintracranialEEG(iEEG)rather
thannon-invasiveEEG.Asummaryofthedatasetcompositionandafulllistofincludedsourcesare
providedinAppendixB.WhilethemajorityofthedataconsistsofclinicalEEGrecordings,wealso
includeasubstantialsubsetofcognitiveandBCI-relateddatawhich,althoughsmallerinproportion,
5

tendtobecleanerandmorediverse. Wealsocollectedelectrodepositionalinformationforeach
recording. When3Dcoordinateswereavailable,theywereuseddirectly;otherwise,positionswere
inferredfromstandardlabels. Channelswithoutidentifiablenamesorpositionaldatawereexcluded.
ThedatasetspansawiderangeofEEGsystemsandformats—includingBrainVision,BioSemi,EDF,
GDF,andEEGLAB,withmostrecordingsadheringtothe10-5system(OostenveldandPraamstra,
2001). Intotal,thedatasetincludes396uniqueelectrodenames.
Ourpreprocessingpipelineisdesignedtopreservesignaldiversityandprioritizerobustnesswhen
scaling. Weonlyremovedrecordingsshorterthan10seconds,andthoseusedindownstreamtasks.
Remainingsignalswereresampledto200Hz,band-passfiltered(0.5–99.5Hz),andconvertedto
float32,resultingina6TBdataset. Toaddressamplitudevariationsacrossrecordings,weapplied
Z-scorenormalizationwithstatisticscomputedacrosstherecordingsessionstoensurerobuststatistics.
After normalization, values exceeding 15 standard deviations were clipped, as in Défossez et al.
(2023). UnlikeCBraMod(Wangetal.,2024b),whichexcludedsignalsabove100µV,ourapproach
retainsthem,resultinginabout60,000hoursofEEG,comparedto9,000inCBraModand2,534in
LaBraM.
3.1.2 PretrainingStrategy&Scaling
3.2 TrainingandScalingStrategy
WepresentthetrainingprocedureusedforpretrainingtheSmallmodelanddetailhowitscalesto
largerarchitecturesunderconstrainedresources. Ourtrainingframeworkbuildsuponrecentadvances
instate-of-the-artNLPmethodologies(Warneretal.,2024). WeusetheStableAdamW(Wortsman
et al., 2023) optimizer, designed for low precision frameworks and improved stability, thanks to
theAdafactor-stylegradientclipping(ShazeerandStern,2018). Table5oftheAppendixliststhe
optimizerhyperparameters.
ThelearningratefollowsaWarmupStableDecay(trapezoidal)schedule(Huetal.,2024),knownfor
itsrobustnesstolearningratevariations(Hägeleetal.,2024).Weusealinearwarmupover10%ofthe
firstepoch,followedby80%atpeakLR,andalineardecayto1%ofthemaximum. Unlikeone-cycle
schedulesthatreseteveryepoch, ourcyclictrapezoidalvariantallowsmultiplecooldownphases
acrossepochs, particularlybeneficialforEEGtrainingwheremaskedtokensamplingintroduces
variability. WeapplyMegatron-styleinitialization(Shoeybietal.,2019)withastandarddeviationof
0.02foralltransformerlayersandthemasktoken,ensuringstabledynamics. Otherparametersuse
PyTorch’sdefaultinitializations.
Akeyfactorforthesuccessoffoundationmodelsisthesimultaneousscalingofbothtrainingdatasets
andmodelarchitectures(Touvronetal.,2023). Wedescribeourscalingmethodologytomaximize
computationalefficiencyandaccommodatelargermodelswithinconstrainedresources. Toscale
modelcapacity,weadjustdepth,width,andnumberofattentionheadswhilemaintainingafixed
FFNratio. Table6oftheAppendixsummarizestheseconfigurations. Thisscalingstrategyenables
efficientcapacityexpansionwhilepreservingarchitecturalconsistencyacrossmodelsizes.
RecentadvancesinNLPprovidestrongtheoreticalandempiricalevidencefortheexistenceofscaling
laws(Kaplanetal.,2020;Hoffmannetal.,2022), whichgoverntherelationshipbetweenmodel
size,trainingdynamics,optimizationandinitializationhyperparameters. Wefollowthepowerlaw
η ∝DαD,withα
D
=−0.90andDthemodeldimension,forthelearningrate,asderivedinEverett
etal.(2024). TheoptimalLRisfirstsweptonthesmallmodelandthenscaledaccordingly.
Toefficientlytrainmodels,weusedataparallelism,maintainingaconstantbatchsizebyreducing
per-GPUloadsforlargemodels. Aload-awaredata-shufflingstrategygroupssamplesbyelectrode
count,shuffleswithinandacrossbuckets,andbalancesbatchesacrossGPUstoavoidbottlenecks,for
constantoptimizationstepsandmaximizedthroughput.
AlthoughscalinglawsexistforadjustingAdamWmomentumterms(Malladietal.,2022),ouruse
ofaconstanteffectivebatchsizeacrossmodelsallowsustofixβ andβ . Regardinginitialization,
1 2
whileHägeleetal.(2024)suggestsscalingσ ∝ D−0.5,ourwidthincrease(from200to1,216)
init
leadsustokeepσ =0.02fixedacrossscales.
init
3.3 Downstreamtasks
Downstreamtaskdatasets ToevaluatetheperformanceandgeneralizabilityofourEEGfounda-
tionmodel,weperformextensiveassessmentsacross10diversedownstreamtasks,selectedtoensure
6

comparabilitywithexistingmodelsinthefield. ThesetasksspanavarietyofEEG-basedapplications,
includingsleepstaging,emotionandeventclassification,detectionofstressandmentaldisorder,
acrossthefollowingdatasets: PhysioNet-MI(Goldbergeretal.,2000),BCIC-IV-2a(Tangermann
etal.,2012),TUEV(ObeidandPicone,2016),TUAB(ObeidandPicone,2016),HMC(Alvarez-
Estevez and Rijsman, 2021), ISRUC (Khalighi et al., 2016), FACED (Chen et al., 2023), Mum-
taz(Mumtaz,2016),MentalArithmetic(MAT)(Zymaetal.,2019),andBCI2020-IV-3(Jeongetal.,
2022). AsummaryofthesedatasetsisprovidedinTable1,withamoredetaileddescriptionavailable
intheAppendix.
Table1: Overviewofdownstreamtasksanddatasets.
| Task               | Dataset      | #Channels | Duration | #Samples | Rate  | #Classes |
| ------------------ | ------------ | --------- | -------- | -------- | ----- | -------- |
| MotorImagery       | PhysioNet-MI | 64        | 4s       | 9,837    | 160Hz | 4        |
|                    | BCIC-IV-2a   | 22        | 4s       | 5,184    | 250Hz | 4        |
| EventType          | TUEV         | 16        | 5s       | 112,491  | 256Hz | 6        |
| Abnormaldetection  | TUAB         | 16        | 10s      | 409,455  | 256Hz | 2        |
| Sleepstaging       | HMC          | 4         | 30s      | 137,243  | 256Hz | 5        |
|                    | ISRUC        | 6         | 30s      | 89,240   | 200Hz | 5        |
| Emotionrecognition | FACED        | 32        | 10s      | 10,332   | 250Hz | 9        |
| Mentaldisorder     | Mumtaz       | 19        | 5s       | 7,143    | 256Hz | 2        |
| Mentalstress       | MAT          | 20        | 5s       | 1,707    | 500Hz | 2        |
| Imaginedspeech     | BCIC2020-3   | 64        | 3s       | 6,000    | 256Hz | 5        |
Our evaluation process maintains strict consistency with prior works by adhering to the same
train/val/testsplitsusedinearlierstudies,ensuringthatourresultsaredirectlycomparabletobaseline
models. Specifically,wefollowtheprotocolsfromCBraMod(Wangetal.,2024b),LaBraM(Jiang
etal.,2024),andBIOT(Yangetal.,2024),guaranteeingfaircomparisonsacrosstasks. Forfairness
inpreprocessing,weadoptthesamepipelineasthebaselines. Anotablecorrectionwasmadeforthe
ISRUCdataset,whereweidentifiedandremovedabuginthebaselinecodeinvolvingtheinclusion
ofachinelectrodeinsteadofanEEGelectrode. OurresultsforREVEexcludethechinelectrode,
aligningwithproperelectrodeplacement.
Finetuning Fine-tuningEEG-basedmodelspresentsuniquechallengesduetothesmallsizeof
availabledatasetsandthehighnoiselevelsinEEGrecordings.Unlikelarge-scalevisiondatasets,EEG
datasetsareoftenlimitedinsize,subject-dependent,andpronetodistributionshiftsacrossdifferent
recordingsetups. Effectivefine-tuningmustthereforemaximizegeneralizationwhilemitigatingthe
riskofoverfitting. Toaddressthis,weadoptatwo-stepfine-tuningstrategy,incorporatingtechniques
specificallydesignedtoenhancestabilityandadaptability.Thisincludestheuseofparameter-efficient
fine-tuningtechniques(Suzumuraetal.,2024)tailoredtothisdomain.
Fordownstreamclassificationtasks,thetwo-stepstrategy,inspiredbyKumaretal.(2022),goesas
follow: Wefirsttrainalinearprobewhilekeepingtheencoderfrozen,aligningtheclassifierwith
the pretrained feature space. Next, we unfreeze the encoder and fine-tune the entire network for
task-specificadaptation,preservingtherobustnessofthepretrainedmodel. Importantly,thistwo-step
strategyisimplementedasasinglecontinuoustrainingrun,wherethebackboneisinitiallyfrozen
(i.e.,onlytheheadistrained)andlaterunfrozen. Thisapproachiswell-suitedforEEGdata,where
distributionscanshiftsignificantlyacrossdatasets. WeemploydropoutandMixup(Zhangetal.,
2018)asdataaugmentationforimprovedrobustness. Tofurthermitigatecatastrophicforgettingand
improveefficiency,weintegrateLow-RankAdaptation(LoRA)intotheattentionblocks,withinthe
query, key, value, and output (QKVO) projection layers. Instead of fine-tuning the entire model,
LoRAintroducestrainablelow-rankmatricesthatenableeffectiveadaptationwhilepreservingthe
integrityofthepretrainedmodel’sknowledge(Huetal.,2022).
Eachtrainingstepincludesawarmupphase(KalraandBarkeshli,2024)followedbyacooldown
phase. ThecooldownphaseemploysaReduce-on-Plateaulearningratescheduler,whichdynamically
lowersthelearningratewhentrainingconvergenceslowstopreventingoverfitting.
Tofurtherenhancerobustness,weexploremodelsouping(Wortsmanetal.,2022),whichaverages
the weights of multiple fine-tuning runs to improve accuracy. Given the stochasticity and noise
inherentinEEGdatasets,soupingsmoothsgradientsandreducesvarianceacrossdifferentfine-tuning
7

trajectories. Ourexperimentsconfirmthatthisapproachenhancesgeneralizationandproducesmore
stableperformanceacrossdiverseEEGtasks.
Byintegratingstructuredfine-tuningwithdataaugmentation,LoRAandmodelsouping,ourapproach
effectivelyaddressesthesmall-scaleandnoisynatureofEEGdatasets. Thesetechniqueseffectively
ensurerobustandgeneralizedadaptationtodownstreamtasks.
4 ResultsandDiscussion
WeevaluateREVEagainstnon-foundationandfoundationmodelbaselinesonthepreviouslydis-
cusseddatasets.
Non-FoundationModels: WecomparetoEEGNet(Lawhernetal.,2018),EEGConformer(Song
etal.,2022),SPaRCNet(Jingetal.,2023),ContraWR(Yangetal.,2021),CNN-Transformer(Peh
etal.,2022),FFCL(Lietal.,2022),andST-Transformer(Songetal.,2021).
FoundationModels: WecomparetoBIOT(Yangetal.,2024),LaBraM(Jiangetal.,2024)and
CBraMod(Wangetal.,2024b). Wereportresultsdisplayedinexistingstudies.
Wereportthebalancedaccuracyforeachdatasetandprovideadditionalevaluationmetricsinthe
appendix.
Table2: Balancedaccuracy(±std)ofdifferentmethodsacross9EEGclassificationtask
Methods TUAB TUEV PhysioNetMI BCI-IV-2a FACED
EEGNet 0.7642±0.0036 0.3876±0.0143 0.5814±0.0125 0.4482±0.0094 0.4090±0.0122
EEGConformer 0.7758±0.0049 0.4074±0.0164 0.6049±0.0104 0.4696±0.0106 0.4559±0.0125
SPaRCNet 0.7896±0.0018 0.4161±0.0262 0.5932±0.0152 0.4635±0.0117 0.4673±0.0155
ContraWR 0.7746±0.0041 0.4384±0.0349 0.5892±0.0133 0.4678±0.0125 0.4887±0.0078
CNN-Transformer 0.7777±0.0022 0.4087±0.0161 0.6053±0.0118 0.4600±0.0108 0.4697±0.0132
FFCL 0.7848±0.0038 0.3979±0.0104 0.5726±0.0092 0.4470±0.0143 0.4673±0.0158
ST-Transformer 0.7966±0.0023 0.3984±0.0228 0.6035±0.0081 0.4575±0.0145 0.4810±0.0079
BIOT 0.7959±0.0057 0.5281±0.0225 0.6153±0.0154 0.4748±0.0093 0.5118±0.0118
LaBraM-Base 0.8140±0.0019 0.6409±0.0065 0.6173±0.0122 0.4869±0.0085 0.5273±0.0107
CbraMod 0.8289±0.0022 0.6671±0.0107 0.6417±0.0091 0.5138±0.0066 0.5509±0.0089
REVE-Base 0.8315±0.0014 0.6759±0.0229 0.6480±0.0140 0.6396±0.0095 0.5646±0.0164
ISRUC Mumtaz MAT BCI-2020-3 Average
EEGNet 0.7154±0.0121 0.9232±0.0104 0.6770±0.0116 0.4413±0.0096 0.5941±0.0037
EEGConformer 0.7400±0.0133 0.9308±0.0117 0.6805±0.0123 0.4506±0.0133 0.6128±0.0044
SPaRCNet 0.7487±0.0075 0.9316±0.0095 0.6879±0.0107 0.4426±0.0156 0.6156±0.0047
ContraWR 0.7402±0.0126 0.9195±0.0115 0.6631±0.0097 0.4257±0.0162 0.6119±0.0053
CNN-Transformer 0.7363±0.0087 0.9305±0.0068 0.6779±0.0268 0.4533±0.0092 0.6133±0.0045
FFCL 0.7277±0.0182 0.9314±0.0038 0.6798±0.0142 0.4678±0.0197 0.6085±0.0044
ST-Transformer 0.7381±0.0205 0.9135±0.0103 0.6631±0.0173 0.4126±0.0122 0.6071±0.0048
BIOT 0.7527±0.0121 0.9358±0.0052 0.6875±0.0186 0.4920±0.0086 0.6438±0.0044
LaBraM-Base 0.7633±0.0102 0.9409±0.0079 0.6909±0.0125 0.5060±0.0155 0.6653±0.0031
CBraMod 0.7865±0.0110 0.9560±0.0056 0.7256±0.0132 0.5373±0.0108 0.6898±0.0031
REVE-Base 0.7819±0.00783 0.9644±0.0097 0.7660±0.0355 0.5635±0.0123 0.7150±0.0057
Table2showsthatREVEachievesstate-of-the-artperformanceonthedownstreamtasksinthisstudy,
withanaveragegainof2.5%,comparedtoCBraModthehighestperformingbaseline. Theresultson
ISRUCandHMC(AppendixC.6)showthatthemodeleffectivelygeneralizesbeyondthe10-second
segmentsitwaspretrainedon,performingwellontaskswith30-secondinputs,whichhighlights
thestrengthofourpositionalencodingmethod. TheresultsonTUEVhighlightthemodel’sability
togeneralizetounseenelectrodeconfigurations,includingbipolarsetupsneverencounteredduring
training.
InadditiontothedetailedevaluationmetricsprovidedinAppendixC,wereporttheperformance
of the Large model across our downstream tasks in Table 4. We observe that the Large model
consistentlyproducesricherembeddings,leadingtoimprovedlinearprobingperformancecompared
totheBasemodel. Modelsoupingconsistentlyimprovedperformance,averaginga1.5%gainwhen
3NB:ourpreprocessingpipelineisdifferentfromthebaselineandfixesapotentialbug
8

Table3: Impactofpretraining(PT)andweightfreezingonREVEandbaselinesforPhysioNet-MI
PhysioNet-MI,4-class
| Settings |     | BalancedAccuracy | Cohen’sKappa  |     | WeightedF1    |     |
| -------- | --- | ---------------- | ------------- | --- | ------------- | --- |
|          |     | 0.6417±0.0091    | 0.5222±0.0169 |     | 0.6427±0.0100 |     |
CBraMod(w/PT)
|     |     | 0.6153±0.0154 | 0.4875±0.0272 |     | 0.6158±0.0197 |     |
| --- | --- | ------------- | ------------- | --- | ------------- | --- |
BIOT(w/PT)
|     |     | 0.6173±0.0122 | 0.4912±0.0192 |     | 0.6177±0.0141 |     |
| --- | --- | ------------- | ------------- | --- | ------------- | --- |
LaBraM-Base(w/PT)
|     |     | 0.6480±0.0140 | 0.5306±0.0187 |     | 0.6484±0.0170 |     |
| --- | --- | ------------- | ------------- | --- | ------------- | --- |
REVE-Base(w/PT)
| CBraMod(w/oPT) |     | 0.6196±0.0143 | 0.4994±0.0289 |     | 0.6289±0.0179 |     |
| -------------- | --- | ------------- | ------------- | --- | ------------- | --- |
|                |     | 0.5409±0.0094 | 0.3879±0.0125 |     | 0.5421±0.0101 |     |
REVE-Base(w/oPT)
| Cbramod(Frozen)   |     | 0.3845±0.0345 | 0.2983±0.0498 |     | 0.3946±0.0378 |     |
| ----------------- | --- | ------------- | ------------- | --- | ------------- | --- |
| BIOT(Frozen)      |     | 0.3698±0.0318 | 0.2703±0.0472 |     | 0.3723±0.0364 |     |
| LaBraM(Frozen)    |     | 0.3715±0.0458 | 0.2814±0.0586 |     | 0.3796±0.0472 |     |
| REVE-Base(Frozen) |     | 0.5371±0.0052 | 0.3827±0.0070 |     | 0.5376±0.0033 |     |
Table4: LinearprobingresultsondownstreamtasksforREVEandCBraModmodelswith(Pool)
andwithoutpoolingacrossmultipleEEGdownstreamtasks. Bestresultsarehighlightedinbold. To
ensureafaircomparison,wereproducedCBraMod(Wangetal.,2024b)usingtheirofficialcode
andpretrainedcheckpoint,carefullyfollowingtheirclassificationpipeline(notably,nopooling)and
matchedarchitecturaldetailstoavoidanybias.
Dataset REVE-B(Pool) REVE-B REVE-L(Pool) REVE-L CBraMod(Pool) CBraMod
Mumtaz 0.962±0.003 0.931±0.021 0.985±0.006 0.980±0.009 0.859±0.009 0.907±0.027
M.Arithmetic 0.725±0.010 0.740±0.073 0.712±0.008 0.665±0.103 0.500±0.000 0.605±0.020
TUAB 0.810±0.007 0.809±0.004 0.821±0.004 0.809±0.004 0.500±0.000 0.500±0.000
PhysioNetMI 0.537±0.005 0.510±0.012 0.551±0.001 0.617±0.000 0.256±0.002 0.531±0.015
BCIC-IV-2a 0.432±0.004 0.517±0.015 0.534±0.001 0.603±0.011 0.287±0.023 0.376±0.006
ISRUC 0.697±0.011 0.662±0.030 0.743±0.004 0.758±0.001 0.407±0.049 0.430±0.043
HMC 0.647±0.008 0.604±0.008 0.703±0.003 0.710±0.007 0.368±0.001 0.538±0.009
BCIC2020-3 0.234±0.009 0.390±0.017 0.274±0.001 0.378±0.021 0.214±0.003 0.374±0.007
TUEV 0.592±0.008 0.508±0.073 0.630±0.003 0.550±0.014 0.219±0.009 0.482±0.037
Faced 0.240±0.010 0.422±0.028 0.283±0.003 0.469±0.007 0.117±0.005 0.261±0.013
| Avg. | 0.586 | 0.609 | 0.623 | 0.654 | 0.373 | 0.501 |
| ---- | ----- | ----- | ----- | ----- | ----- | ----- |
combiningatleast5BaseorLargemodels. Forexample, REVE-Baseachieved69.6%balanced
accuracyonTUEVusingthe10modelsfromTable2. However,soupingshowedlimitedbenefitsfor
thesmallmodelsandsometimesledtonegativeoutcomes.
Table 3 highlights the importance of REVE’s pretraining phase. Without pretraining, CBraMod
outperforms REVE by at least 8%. However, pretraining improves REVE-Base by 11%, while
CBraMod gains only 2%, a trend also observed in the LaBraM paper. This suggests that REVE
benefitsmoresignificantlyfrompretraining,whereasothermodelsderivemostoftheirperformance
fromarchitecturaldesignratherthanpretraininglearnedrepresentations. AkeyadvantageofREVE
isitsabilitytoproducehigh-qualitylatentspaceswithoutheavyfine-tuning,asevidencedbylinear
probingresultsinTable4: REVEconsistentlyoutperformsCBraModacrossalldownstreamtasks
andmodelsizes,withREVE-Largeachievingnearly17%higherperformance. Theseresultsalso
highlightREVE’sabilitytoscaleeffectivelywithmodelsize,yieldingricherandmoregeneralizable
embeddingsascapacityincreases. Providingrich,ready-to-useembeddingsiscrucialforenabling
zero-shotanalysis,fasterBCIcalibration,andimprovedperformanceinlow-dataorsparselyannotated
settings. REVEalsobenefitsfromitsspatialencodingstrategy,whichenablestransferacrossdiverse
EEG configurations. In Appendix D, we further demonstrate the contribution of our secondary
lossfunction,anovelcomponentofourframework,whichprovesparticularlyeffectiveinfrozen-
featurescenarios. Thesecondaryobjectivereconstructsmaskedtokensusingacompressed,global
representationfromattentionpooling. Thispoolingactsasaninformationbottleneck,forcingthe
modeltodistillkeyinformationfromtheentireinputsequenceintoasinglevector. Asshownby
Table17,thesecondarylossmainlyimprovesthequalityofthefrozenembeddingsofthemodel.
9

5 LimitationsandFutureWork
Themodelhassomelimitations, requiringsignalstobeatleastonesecondandmultiplesofone
second. Awaytoaddressthiscouldbetoleveragepaddingwithcausalmasking.
WhilethefocushasbeenoncollectinglargeEEGdatasetsforpretraining,animportantnextstepcould
betocuratethisdatamoreselectively. Thisincludesremovinglow-qualityrecordings,balancing
distributions,andidentifyingrepresentativesubsets,especiallygiventheinherentlynoisynatureof
EEGsignals. Ourcurrentpretrainingcorpusaggregates92publiclyavailableEEGdatasetsspanning
over25,000subjects, whichhelpsreduceoverfittingtoanysinglesource. However, mostpublic
EEGdataoriginatesfromNorthAmericaandEurope,resultinginlimiteddemographicdiversity—a
key limitation that calls for broader, more equitable data collection efforts. To partially mitigate
suchimbalances,weleverageself-supervisedlearning(MAE),whichhasbeenshowntoberobust
tolong-tailedandheterogeneousdatadistributions(Xuetal.,2023). Targetedselectionstrategies,
combinedwithrobustSSLobjectives,couldhelpfocusonthemostinformativeandcomplementary
dataforbuildingstronger,fairer,andmoreefficientfoundationmodels. Thankstoitsflexibilityin
handlinganyEEGconfiguration,REVEcoulditselfguidethiscurationprocess.
We also plan to extend our study to diverse tasks, including zero-/few-shot regimes. This first
iterationusesasimpleMAEapproachandastandardtransformer,butfutureimprovementscould
leveragemoreadvancedSSLtechniquesandarchitectures. Wereleasethemodel’scode,weights
andguidelinesforadaptingittomainstreamEEGtasks. Inparallel,ourfindingspointtowardthe
presenceofscalingeffectsinEEGfoundationmodels. Identifyingprecisescalinglawsthatcapture
howmodelsize,datavolume,anddownstreamperformanceinteractwouldbevaluableforfuture
work.
6 Conclusion
EEGresearchhaslackedafoundationmodelthattransfersrobustlyacrossdevices,montages,and
tasks—especiallyunderlinearprobing. REVEcontributestobridgingthisgap. Trainedon 60,000
hoursfrom92datasetsand 25,000subjects,REVEcombinesa4DFourierpositionalencodingthat
nativelysupportsarbitraryelectrodelayoutsandsequencelengthswithmaskedautoencodingen-
hancedbyspatio-temporalblockmaskingandaglobal-tokensecondaryloss. Across10benchmarks,
itsetsanewstateoftheart(average+2.5%balancedaccuracyoverpriorfoundationmodels),delivers
upto 17%gainsinlinearprobing,andgeneralizestounseen/bipolarmontagesandlongerinputs
than used in pretraining. These properties enable faster BCI calibration, more reliable cross-site
clinical deployment, and standardized embeddings for downstream analytics. We release code,
weights,loadersforarbitrary3Dcoordinates,andtraining/evalrecipes. Weinvitethecommunity
toextendREVEtobroaderpopulationsandmodalities(MEG/iEEG/OPM-MEG),andtoco-builda
cross-montagebenchmarkforfair,scalableEEGevaluation.
7 Acknowledgments
ThisresearchwassupportedbytheFrenchNationalResearchAgency(ANR)throughitsAI@IMT
program and grant ANR-24-CE23-7365, as well as by a grant from the Brittany region. Further
supportwasprovidedbyaDiscoveryGrantfromtheNaturalSciencesandEngineeringResearch
CouncilofCanada(NSERC),byfundingfromtheCanadaResearchChairsprogramandtheFonds
derechercheduQuébec–Natureettechnologies(FRQ-NT).Thisworkwasgrantedaccesstothe
HPCresourcesofIDRISundertheallocation2024-AD011015237R1madebyGENCI,aswellas
HPCprovidedbyDigitalAllianceCanada.
10

References
BerndAccou,LiesBollens,MarliesGillis,WendyVerheijen,HugoVanhamme,andTomFrancart.
SparrKULee: ASpeech-EvokedAuditoryResponseRepositoryoftheKULeuven,Containing
EEGof85Participants. BioRxiv,pages2023–07,2023.
JoshAchiam,StevenAdler,SandhiniAgarwal,LamaAhmad,IlgeAkkaya,FlorenciaLeoniAleman,
DiogoAlmeida, JankoAltenschmidt, SamAltman, ShyamalAnadkat, etal. GPT-4Technical
Report. ArXivPreprintArXiv:2303.08774,2023.
Blanca Aguado-Lopez, Ana F. Palenciano, Jose M. G. Penalver, Paloma Diaz-Gutierrez, David
Lopez-Garcia, Chiara Avancini, Luis F. Ciria, and Maria Ruz. "Proactive Selective Attention
AcrossCompetitionContexts",2024.
Lindsay M Alexander, Jasmine Escalera, Lei Ai, Charissa Andreotti, Karina Febre, Alexander
Mangone, Natan Vega-Potler, Nicolas Langer, Alexis Alexander, Meagan Kovacs, et al. An
OpenResourceforTransdiagnosticResearchinPediatricMentalHealthandLearningDisorders.
ScientificData,4(1):1–26,2017.
Benedikt Alkin, Lukas Miklautz, Sepp Hochreiter, and Johannes Brandstetter. MIM-Refiner: A
Contrastive Learning Boost from Intermediate Pre-Trained Representations. ArXiv Preprint
ArXiv:2402.10093,2024.
DiegoAlvarez-EstevezandRoselyneMRijsman. Inter-DatabaseValidationofaDeepLearning
ApproachforAutomaticSleepScoring. PLOSOne,16(8):e0256111,2021.
Edilberto Amorim, Wei-Long Zheng, Jong Woo Lee, Susan Herman, Mohammad Ghas-
semi, Adithya Sivaraju, Nicolas Gaspard, Jeannette Hofmeijer, Michel JAM van Putten,
Matthew Reyna, et al. I-CARE: International Cardiac Arrest Research Consortium Database.
https://physionet.org/content/i-care/2.0,2023.
CarlosValleAraya,CarolinaMendez-Orellana,andMariaRodriguez-Fernandez. "LargeSpanish
EEG",2023.
PietroAricò,FAloise,FrancescaSchettini,SerenellaSalinari,DMattia,andFeboCincotti. Influence
ofP300LatencyJitteronEventRelatedPotential-BasedBrain–ComputerInterfacePerformance.
JournalofNeuralEngineering,11(3):035008,2014.
Bruno Aristimunha, Igor Carrara, Pierre Guetschel, Sara Sedlar, Pedro Rodrigues, Jan Sosulski,
DivyeshNarayanan,ErikBjareholt,BarthelemyQuentin,RobinTiborSchirrmeister,Emmanuel
Kalunga,LudovicDarmet,CattanGregoire,AliAbdulHussain,RamiroGatti,VladislavGon-
charenko,JordyThielen,ThomasMoreau,YannickRoy,VinayJayaram,AlexandreBarachant,and
SylvainChevallier. MotherofAllBCIBenchmarks,2023. URLhttps://moabb.neurotechx.
com/docs/index.html.
Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge,
YuHan,FeiHuang,etal. QwenTechnicalReport. ArXivPreprintArXiv:2309.16609,2023.
Imad J. Bajwa1, Andre S. Nilsen1, 3 René Skukies1, Arnfinn Aamodt1, Gernot Ernst2, Johan F.
Storm1,and2BjørnE.Juel1."ARepeatedAwakeningStudyExploringtheCapacityofComplexity
MeasurestoCaptureDreamingDuringPropofolSedation",2024.
AlexandreBarachant. CommandeRobusted’unEffecteurparuneInterfaceCerveauMachineEEG
Asynchrone. PhDthesis,UniversitédeGrenoble,2012.
CemreBaykanandAlexanderC.Schütz. "ElectroencephalographicResponsestotheNumberof
ObjectsinPartiallyOccludedandUncoveredScenes",2024.
OleBialas,EmilyTeoh,AndrewAnderson,andEdmundLalor. "InvariantEncodingofPhonemesin
NeuralResponsestoContinuousSpeech",2023.
MathildeCaron,HugoTouvron,IshanMisra,HervéJégou,JulienMairal,PiotrBojanowski,and
ArmandJoulin. EmergingPropertiesinSelf-SupervisedVisionTransformers. InProceedingsof
theIEEE/CVFInternationalConferenceonComputerVision,pages9650–9660,2021.
11

JamesFCavanaghandTrevorCJJackson. "MoodManipulationandPST,Experiment1",2022.
LuisAlbertoBarradasChacónandSelinaC.Wriessnegger. "Toonfaces",2023.
JingjingChen,XiaobinWang,ChenHuang,XinHu,XinkeShen,andDanZhang. ALargeFiner-
GrainedAffectiveComputingEEGDataset. ScientificData,10(1):740,2023.
Hsiang-Yun Sherry Chien, Hanlin Goh, Christopher Michael Sandino, and Joseph Yitan Cheng.
MaEEG:MaskedAuto-EncoderforEEGRepresentationLearning. InNeurIPS2022Workshopon
LearningfromTimeSeriesforHealth,2022.
HohyunCho,MinkyuAhn,SangtaeAhn,MoonyoungKwon,andSungChanJun. EEGDatasetsfor
MotorImageryBrain–ComputerInterface. Gigascience,6(7):gix034,2017.
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam
Roberts,PaulBarham,HyungWonChung,CharlesSutton,SebastianGehrmann,etal. PaLM:
ScalingLanguageModelingwithPathways. JournalofMachineLearningResearch, 24(240):
1–113,2023.
Jose Cordoba-Silva, Rafael Maya, Mario Valderrama, Luis Felipe Giraldo, William Betancourt-
Zapata,AndrésSalgado-Vascob,JulianaMarín-Sánchez,VivianaGómez-Ortega,andMarkEtten-
berger. "DatasetofElectrophysiologicalSignals(EEG,ECG,EMG)DuringMusicTherapywith
AdultBurnPatientsintheIntensiveCareUnit",2023.
WenhuiCui,WoojaeJeong,PhilippThölke,TakfarinasMedani,KarimJerbi,AnandAJoshi,and
RichardMLeahy. Neuro-GPT:TowardsaFoundationModelforEEG. In2024IEEEInternational
SymposiumonBiomedicalImaging(ISBI),pages1–5.IEEE,2024.
IanDaly,NicolettaNicolaou,DuncanWilliams,FaustinaHwang,AlexisKirke,EduardoMiranda,
andSlawomirJ.Nasuto. "AnEEGDatasetRecordedDuringAffectiveMusicListening",2020.
Tri Dao. FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning. In
InternationalConferenceonLearningRepresentations(ICLR),2024.
BorisDayma,SurajPatil,PedroCuenca,KhalidSaifullah,TanishqAbraham,PhúcLêKhac,Luke
Melas,andRitobrataGhosh. Dall·EMini,72021. URLhttps://github.com/borisdayma/
dalle-mini.
AlexandreDéfossez,CharlotteCaucheteux,JérémyRapin,OriKabeli,andJean-RémiKing. Decod-
ingSpeechPerceptionfromNon-InvasiveBrainRecordings. NatureMachineIntelligence,5(10):
1097–1107,2023.
ArnaudDelormeandClaireBraboszcz. "MeditationVsThinkingTask",2021.
ArnaudDelormeandTracyBrandmeyer. "EEGMeditationStudy",2024.
ArnaudDelormeandMicheleFabre-Thorpe. "Go-NogoCategorizationandDetectionTask",2020.
PaoloDetti. SienaScalpEEGDatabase. Physionet.Doi,10:493,2020.
PaoloDetti,GiampaoloVatti,andGaraziZabaloManriquedeLara. EEGSynchronizationAnalysis
forSeizurePrediction: AStudyonDataofNoninvasiveRecordings. Processes,8(7):846,2020.
PaulineDreyer,AlineRoc,LéaPillette,SébastienRimbert,andFabienLotte. ALargeEEGDatabase
withUsers’ProfileInformationforMotorImageryBrain-ComputerInterfaceResearch. Scientific
Data,10(1):580,2023.
AbhimanyuDubey,AbhinavJauhri,AbhinavPandey,AbhishekKadian,AhmadAl-Dahle,Aiesha
Letman,AkhilMathur,AlanSchelten,AmyYang,AngelaFan,etal. TheLlama3HerdofModels.
ArXivPreprintArXiv:2407.21783,2024.
YassineElOuahidi,VincentGripon,BastienPasdeloup,GhaithBouallegue,NicolasFarrugia,and
Giulia Lioi. A Strong and Simple Deep Learning Baseline for BCI Motor Imagery Decoding.
IEEETransactionsonNeuralSystemsandRehabilitationEngineering,2024.
12

PabloRodríguez-SanEsteban,AnaB.Chica,andJoséA.González-López. "NeuralRepresentation
ofConsciouslySeenandUnseenInformation",2024.
KatieEEverett,LechaoXiao,MitchellWortsman,AlexanderAAlemi,RomanNovak,PeterJLiu,
IzzeddinGur,JaschaSohl-Dickstein,LesliePackKaelbling,JaehoonLee,andJeffreyPennington.
Scaling Exponents Across Parameterizations and Optimizers. In Ruslan Salakhutdinov, Zico
Kolter,KatherineHeller,AdrianWeller,NuriaOliver,JonathanScarlett,andFelixBerkenkamp,
editors,Proceedingsofthe41StInternationalConferenceonMachineLearning,volume235of
ProceedingsofMachineLearningResearch,pages12666–12700.PMLR,21–27Jul2024. URL
https://proceedings.mlr.press/v235/everett24a.html.
Josef Faller, Carmen Vidaurre, Teodoro Solis-Escalante, Christa Neuper, and Reinhold Scherer.
Autocalibration and Recurrent Adaptation: Towards a Plug and Play Online ERD-BCI. IEEE
TransactionsonNeuralSystemsandRehabilitationEngineering,20(3):313–319,2012.
LukasGehrke,SezenAkman,AlbertChen,PedroLopes,andKlausGramann. "PredictionError",
2024.
JonasGeipingandTomGoldstein. Cramming: TrainingaLanguageModelonaSingleGPUinOne
Day. InInternationalConferenceonMachineLearning,pages11117–11143.PMLR,2023.
AlessandroTGifford,KshitijDwivedi,GemmaRoig,andRadoslawMCichy. ALargeandRich
EEGDatasetforModelingHumanVisualObjectRecognition. NeuroImage,264:119754,2022.
AryLGoldberger,LuisANAmaral,LeonGlass,JeffreyMHausdorff,PlamenChIvanov,RogerG
Mark,JosephEMietus,GeorgeBMoody,Chung-KangPeng,andHEugeneStanley. Physiobank,
Physiotoolkit,andPhysionet: ComponentsofaNewResearchResourceforComplexPhysiologic
Signals. Circulation,101(23):e215–e220,2000.
Tijl Grootswagers, IvyZhou, Amanda Robinson, Martin Hebart, andThomas Carlson. "Human
Electroencephalography Recordings from 50 Subjects for 22,248 Images from 1,854 Object
Concepts",2022.
TijlGrootswagers, AmandaRobinson, SofiaShatek, andThomasCarlson. "EEG-attention-rsvp-
exp1",2023a.
TijlGrootswagers, AmandaRobinson, SofiaShatek, andThomasCarlson. "EEG-attention-rsvp-
exp2",2023b.
TijlGrootswagers,AmandaRobinson,SofiaShatek,andThomasCarlson. "Features-EEG",2024.
PierreGuetschel,ThomasMoreau,andMichaelTangermann. S-JEPA:TowardsSeamlessCross-
DatasetTransferThroughDynamicSpatialAttention. ArXivPreprintArXiv:2403.11772,2024.
ChristophGuger,ShahabDaban,EricSellers,ClemensHolzner,GuntherKrausz,RobertaCarabalona,
FurioGramatica,andGuenterEdlinger. HowManyPeopleAreAbleToControlaP300-Based
Brain–ComputerInterface(BCI)? NeuroscienceLetters,462(1):94–98,2009.
AlexanderHägele,ElieBakouch,AtliKosson,LoubnaBenAllal,LeandroVonWerra,andMartin
Jaggi. ScalingLawsandCompute-OptimalTrainingBeyondFixedTrainingDurations. ArXiv
PreprintArXiv:2405.18392,2024.
CameronD.Hassall,YanYan,andLaurenceT.Hunt. "DrumTrainer",2022a.
CameronD.Hassall,YanYan,andLaurenceT.Hunt. "SteertheShip",2022b.
CameronD.Hassall,LaurenceT.Hunt,andClayB.Holroyd. "AverageTaskValue",2024.
ChristofferHatlestad-Hall,TrineWaageRygvold,andSteinAndersson. "SRMResting-StateEEG",
2022.
Marleen Haupt, Monika Graumann, Santani Teng, Carina Kaltenbach, and Radoslaw M. Cichy.
"BrailleLetters-EEG",2024.
13

HeHeandDongruiWu. TransferLearningforBrain–ComputerInterfaces: AEuclideanSpaceData
AlignmentApproach. IEEETransactionsonBiomedicalEngineering,67(2):399–410,2019.
Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr Dollár, and Ross Girshick. Masked
Autoencoders Are Scalable Vision Learners. In Proceedings of the IEEE/CVF Conference on
ComputerVisionandPatternRecognition,pages16000–16009,2022.
JasonHelbing,DejanDraschkow,andMelissaL.-H.Võ. "SearchSuperiorityRecollectionFamiliar-
ity",2024.
Dan Hendrycks and Kevin Gimpel. Gaussian Error Linear Units (GELUs). ArXiv Preprint
ArXiv:1606.08415,2016.
Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza
Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, et al.
TrainingCompute-OptimalLargeLanguageModels. ArXivPreprintArXiv:2203.15556,2022.
UlrichHoffmann,Jean-MarcVesin,TouradjEbrahimi,andKarinDiserens. AnEfficientP300-Based
Brain–Computer Interface for Disabled Subjects. Journal of Neuroscience Methods, 167(1):
115–125,2008.
EdwardJHu,YelongShen,PhillipWallis,ZeyuanAllen-Zhu,YuanzhiLi,SheanWang,LuWang,
andWeizhuChen. LoRA:Low-RankAdaptationofLargeLanguageModels. InInternational
ConferenceonLearningRepresentations,2022. URLhttps://openreview.net/forum?id=
nZeVKeeFYf9.
ShengdingHu,YugeTu,XuHan,GanquCui,ChaoqunHe,WeilinZhao,XiangLong,ZhiZheng,
Yewei Fang, Yuxiang Huang, Xinrong Zhang, Zhen Leng Thai, Chongyi Wang, Yuan Yao,
Chenyang Zhao, Jie Zhou, Jie Cai, Zhongwu Zhai, Ning Ding, Chao Jia, Guoyang Zeng, da-
haili,ZhiyuanLiu,andMaosongSun. MiniCPM:UnveilingthePotentialofSmallLanguage
ModelswithScalableTrainingStrategies. InFirstConferenceonLanguageModeling,2024. URL
https://openreview.net/forum?id=3X2L2TFr0f.
Ji-Hoon Jeong, Jeong-Hyun Cho, Young-Eun Lee, Seo-Hyun Lee, Gi-Hwan Shin, Young-Seok
Kweon, José del R Millán, Klaus-Robert Müller, and Seong-Whan Lee. 2020 International
Brain–ComputerInterfaceCompetition: AReview. FrontiersinHumanNeuroscience,16:898300,
2022.
AlbertQJiang,AlexandreSablayrolles,ArthurMensch,ChrisBamford,DevendraSinghChaplot,
DiegodelasCasas,FlorianBressand,GiannaLengyel,GuillaumeLample,LucileSaulnier,etal.
Mistral7B. ArXivPreprintArXiv:2310.06825,2023.
WeibangJiang,LimingZhao,andBaoliangLu. LargeBrainModelforLearningGenericRepresen-
tationswithTremendousEEGDatainBCI. InTheTwelfthInternationalConferenceonLearning
Representations,2024.
JinJing,WendongGe,ShendaHong,MartaBentoFernandes,ZhenLin,ChaoqiYang,SungtaeAn,
AaronFStruck,AlineHerlopian,IoannisKarakis,etal. DevelopmentofExpert-LevelClassifica-
tionofSeizuresandRhythmicandPeriodicPatternsDuringEEGInterpretation. Neurology,100
(17):e1750–e1762,2023.
MichaelJ.Kahana,JosephH.Rudoler,LynnJ.Lohnas,KarlHealey,AdaAka,AdamBroitman,
ElizabethCrutchley,PatrickCrutchley,KylieH.Alm,BrandonS.Katerman,NicoleE.Miller,
JoelR.Kuhn,YuxuanLi,NicoleM.Long,JonathanMiller,MadisonD.Paron,JesseK.Pazdera,
IsaacPedisich,andChristophT.Weidemann. "PennElectrophysiologyofEncodingandRetrieval
Study(Peers)",2023.
DayalSinghKalraandMaissamBarkeshli. WhyWarmuptheLearningRate? UnderlyingMecha-
nismsandImprovements. ArXivPreprintArXiv:2406.09405,2024.
EmmanuelKKalunga,SylvainChevallier,andQuentinBarthélemy. UsingRiemannianGeometry
forSSVEP-BasedBrainComputerInterface. ArXivPreprintArXiv:1501.03227,2015.
14

JaredKaplan,SamMcCandlish,TomHenighan,TomBBrown,BenjaminChess,RewonChild,Scott
Gray,AlecRadford,JeffreyWu,andDarioAmodei. ScalingLawsforNeuralLanguageModels.
ArXivPreprintArXiv:2001.08361,2020.
ZoltanKekecsandYeganehFarahzadi. "OTKAPLB-HYPStudy1",2024.
SirvanKhalighi,TeresaSousa,JoséMoutinhoSantos,andUrbanoNunes. Isruc-Sleep: ACompre-
hensivePublicDatasetforSleepResearchers. ComputerMethodsandProgramsinBiomedicine,
124:180–192,2016.
HassanAqeelKhan,RahatUlAin,AwaisMehmoodKamboh,HammadTanveerButt,SaimaShafait,
WasimAlamgir, DidierStricker, andFaisalShafait. TheNMTScalpEEGDataset: AnOpen-
SourceAnnotatedDatasetofHealthyandPathologicalEEGRecordingsforPredictiveModeling.
FrontiersinNeuroscience,15:755817,2022.
AlexanderKirillov,EricMintun,NikhilaRavi,HanziMao,ChloeRolland,LauraGustafson,Tete
Xiao, SpencerWhitehead, AlexanderCBerg, Wan-YenLo, etal. SegmentAnything. InPro-
ceedings of the IEEE/CVF International Conference on Computer Vision, pages 4015–4026,
2023.
LouisKorczowski,MartineCederhout,AntonAndreev,GrégoireCattan,PedroLuizCoelhoRo-
drigues,VioletteGautheret,andMarcoCongedo. BrainInvadersCalibration-LessP300-Based
BCIWithModulationofFlashDurationDataset(Bi2015A). PhDthesis,GIPSA-lab,2019a.
LouisKorczowski, EkaterinaOstaschenko, AntonAndreev, GrégoireCattan, PedroLuizCoelho
Rodrigues,VioletteGautheret,andMarcoCongedo. BrainInvadersCalibration-LessP300-Based
BCIUsingDryEEGElectrodesDataset(Bi2014A). PhDthesis,GIPSA-lab,2019b.
LouisKorczowski, EkaterinaOstaschenko, AntonAndreev, GrégoireCattan, PedroLuizCoelho
Rodrigues,VioletteGautheret,andMarcoCongedo. BrainInvadersSoloVersusCollaboration:
Multi-UserP300-BasedBrain-ComputerInterfaceDataset(Bi2014B). PhDthesis,GIPSA-lab,
2019c.
AnanyaKumar,AditiRaghunathan,RobbieMatthewJones,TengyuMa,andPercyLiang. Fine-
TuningCanDistortPretrainedFeaturesandUnderperformOut-Of-Distribution. InInternational
ConferenceonLearningRepresentations,2022. URLhttps://openreview.net/forum?id=
UYneFzXSJWh.
Vernon J Lawhern, Amelia J Solon, Nicholas R Waytowich, Stephen M Gordon, Chou P Hung,
andBrentJLance. EEGnet: ACompactConvolutionalNeuralNetworkforEEG-BasedBrain–
ComputerInterfaces. JournalofNeuralEngineering,15(5):056013,2018.
Min-HoLee,O-YeonKwon,Yong-JeongKim,Hong-KyungKim,Young-EunLee,JohnWilliamson,
SiamacFazli,andSeong-WhanLee.EEGDatasetandOpenBMIToolboxforThreeBCIParadigms:
AnInvestigationIntoBCIIlliteracy. Gigascience,8(5):giz002,2019.
RobertLeeb,FelixLee,ClaudiaKeinrath,ReinholdScherer,HorstBischof,andGertPfurtscheller.
Brain–ComputerCommunication: Motivation,Aim,andImpactofExploringaVirtualApartment.
IEEETransactionsonNeuralSystemsandRehabilitationEngineering,15(4):473–482,2007.
JimmyLeiBa,JamieRyanKiros,andGeoffreyEHinton. LayerNormalization. ArXive-Prints,
pagesArXiv–1607,2016.
Hongli Li, Man Ding, Ronghua Zhang, and Chunbo Xiu. Motor Imagery EEG Classification
AlgorithmBasedonCNN-LSTMFeatureFusionNetwork. BiomedicalSignalProcessingand
Control,72:103342,2022.
WeilongLiandJiaxinZhao. "PerceiveImagine",2024.
HaijieLiu,PenghuWei,HaochongWang,XiaodongLv,WeiDuan,MeijieLi,YanZhao,Qingmei
Wang, Xinyuan Chen, Gaige Shi, et al. An EEG Motor Imagery Dataset for Brain Computer
InterfaceinAcuteStrokePatients. ScientificData,11(1):131,2024.
15

FabienLotte,LaurentBougrain,AndrzejCichocki,MaureenClerc,MarcoCongedo,AlainRakotoma-
monjy,andFlorianYger. AReviewofClassificationAlgorithmsforEEG-BasedBrain–Computer
Interfaces: A10YearUpdate. JournalofNeuralEngineering,15(3):031005,2018.
BenjaminLowe,JonathanRobinson,NaohideYamamoto,HinzeHogendoorn,andPatrickJohnston.
"VisualAttribute-SpecificContextualTrajectoryParadigm",2023.
DominiqueMakowski,An-ShuTe,StephanieKirk,andZiLiangNgoi. "FakeFaceEmoData",2023.
SadhikaMalladi,KaifengLyu,AbhishekPanigrahi,andSanjeevArora. OntheSDEsandScaling
RulesforAdaptiveGradientAlgorithms. AdvancesinNeuralInformationProcessingSystems,35:
7697–7711,2022.
Christopher J Markiewicz, Krzysztof J Gorgolewski, Franklin Feingold, Ross Blair, Yaroslav O
Halchenko,EricMiller,NellHardcastle,JoeWexler,OscarEsteban,MathiasGoncavles,etal. The
OpenNeuroResourceforSharingofNeuroscienceData. eLife,10:e71774,2021.
DoniaMetwalli,EslamAhmed,AntonyEmil,YousefA.Radwan,MariamBarakat,andAnasAhmed.
"ArEEG:ArabicInnerSpeechEEGDataset",2024.
DeniseMoerel,TijlGrootswagers,AmandaRobinson,SophiaShatek,AlexandraWoolgar,Thomas
Carlson,andAninaRich. "TheTime-CourseofFeature-BasedAttentionEffectsDissociatedfrom
TemporalExpectationandTarget-RelatedProcesses",2022.
NavidMohammadiFoumani,GeoffreyMackellar,SoheilaGhane,SaadIrtza,NamNguyen,and
MahsaSalehi. EEG2Rep: EnhancingSelf-SupervisedEEGRepresentationThroughInformative
MaskedInputs. InProceedingsofthe30thACMSIGKDDConferenceonKnowledgeDiscovery
andDataMining,pages5544–5555,2024.
WajidMumtaz. MDDPatientsandHealthyControlsEEGData(New). Figshare,Dataset,2016.
MasakiNakanishi,YijunWang,Yu-TeWang,andTzyy-PingJung.AComparisonStudyofCanonical
CorrelationAnalysisBasedMethodsforDetectingSteady-StateVisualEvokedPotentials. PLOS
One,10(10):e0140703,2015.
IyadObeidandJosephPicone. TheTempleUniversityHospitalEEGDataCorpus. Frontiersin
Neuroscience,10:196,2016.
PatrickOfner,AndreasSchwarz,JoanaPereira,andGernotRMüller-Putz. UpperLimbMovements
CanBeDecodedFromtheTime-DomainofLow-FrequencyEEG. PLOSOne,12(8):e0182578,
2017.
JulieOntonandScottMakeig. "ImaginedEmotionStudy",2022.
RobertOostenveldandPeterPraamstra. TheFivePercentElectrodeSystemforHigh-Resolution
EEGandERPMeasurements. ClinicalNeurophysiology,112(4):713–719,2001.
TasosPapastylianou,RodrigoRamele,LucaCiti,CaterinaCinel,andRiccardoPoli."PES-Pandemic
EmergencyScenario",2023.
WeiYanPeh,YuanyuanYao,andJustinDauwels. TransformerConvolutionalNeuralNetworksfor
AutomatedArtifactDetectioninScalpEEG. In202244thAnnualInternationalConferenceofthe
IEEEEngineeringinMedicine&BiologySociety(EMBC),pages3599–3602.IEEE,2022.
AlecRadford, JongWookKim, ChrisHallacy, AdityaRamesh, GabrielGoh, SandhiniAgarwal,
GirishSastry,AmandaAskell,PamelaMishkin,JackClark,etal. LearningTransferableVisual
ModelsfromNaturalLanguageSupervision. InInternationalConferenceonMachineLearning,
pages8748–8763.PMLR,2021.
ShankerRam,SambhuGanesan,andYajatNagarajKiran. HarmfulBrainActivityClassification
ofSpectrogramswithTransferDeepLearning. In2024IEEE7thInternationalConferenceon
MultimediaInformationProcessingandRetrieval(MIPR),pages499–502.IEEE,2024.
MariaJ.RibeiroandMiguelCastelo-Branco. "EEG,ECGandPupilDatafromYoungandOlder
Adults: RestandAuditoryCuedReactionTimeTasks",2021.
16

Angela Riccio, Luca Simione, Francesca Schettini, Alessia Pizzimenti, Maurizio Inghilleri,
Marta Olivetti Belardinelli, Donatella Mattia, and Febo Cincotti. Attention and P300-Based
BCIPerformanceinPeoplewithAmyotrophicLateralSclerosis.FrontiersinHumanNeuroscience,
7:732,2013.
AlexanderP.Rockhill,NickoJackson,JobiGeorge,AdamAron,andNicoleC.Swann. "UCSan
DiegoRestingStateEEGDatafromPatientswithParkinson’sDisease",2020.
Joseph H. Rudoler, Matthew R. Dougherty, Brandon S. Katerman, James P. Bruska, Woohyeuk
Chang,DavidJ.Halpern,NicholasB.Diamond,andMichaelJ.Kahana. "SpatialMemoryand
Non-InvasiveClosed-LoopStimulusTiming",2023.
ReinholdScherer,JosefFaller,ElisabethVCFriedrich,EloyOpisso,UrsulaCosta,AndreaKübler,
andGernotRMüller-Putz. IndividuallyAdaptedImageryImprovesBrain-ComputerInterface
PerformanceinEnd-UserswithDisability. PLOSOne,10(5):e0123727,2015.
Robin Tibor Schirrmeister, Jost Tobias Springenberg, Lukas Dominique Josef Fiederer, Martin
Glasstetter,KatharinaEggensperger,MichaelTangermann,FrankHutter,WolframBurgard,and
TonioBall. DeepLearningwithConvolutionalNeuralNetworksforEEGDecodingandVisualiza-
tion. HumanBrainMapping,38(11):5391–5420,2017.
Tong Shan, Madeline S. Cappelloni, and Ross K. Maddox. "Music and Speech Elicit Similar
SubcorticalResponsesinHumanListeners",2022.
SophiaM.Shatek,AmandaK.Robinson,TijlGrootswagers,andThomasA.Carlson. "Capacity
forMovementIsaMajorOrganisationalPrincipleinObjectRepresentations: EEGDatafrom
Experiment2",2021.
SophiaM.Shatek,AmandaK.Robinson,TijlGrootswagers,andThomasA.Carlson. "Capacityfor
MovementIsanOrganisationalPrincipleinObjectRepresentations: EEGDatafromExperiment
2",2023.
NoamShazeer. GLUVariantsImproveTransformer. ArXivPreprintArXiv:2002.05202,2020.
NoamShazeerandMitchellStern. Adafactor: AdaptiveLearningRateswithSublinearMemoryCost.
InInternationalConferenceonMachineLearning,pages4596–4604.PMLR,2018.
JaeyoungShin,AlexandervonLühmann,BenjaminBlankertz,Do-WonKim,JichaiJeong,Han-Jeong
Hwang,andKlaus-RobertMüller. OpenAccessDatasetforEEG+NirsSingle-TrialClassification.
IEEETransactionsonNeuralSystemsandRehabilitationEngineering,25(10):1735–1745,2016.
SeyedYahyaShirazi,AlexandreFranco,MaurícioScopelHoffmann,NathaliaB.Esper,DungTruong,
ArnaudDelorme,MichaelMilham,andScottMakeig. "HealthyBrainNetwork(HBN)EEG-
Release4",2024a.
SeyedYahyaShirazi,AlexandreFranco,MaurícioScopelHoffmann,NathaliaBEsper,DungTruong,
ArnaudDelorme,MichaelPMilham,andScottMakeig. HBN-EEG:TheFairImplementation
oftheHealthyBrainNetwork(HBN)ElectroencephalographyDataset. BioRxiv,pages2024–10,
2024b.
SeyedYahyaShirazi,AlexandreFranco,MaurícioScopelHoffmann,NathaliaB.Esper,DungTruong,
ArnaudDelorme,MichaelMilham,andScottMakeig. "HealthyBrainNetwork(HBN)EEG-
Release5",2025.
Mohammad Shoeybi, Mostofa Patwary, Raul Puri, Patrick LeGresley, Jared Casper, and Bryan
Catanzaro. Megatron-LM: Training Multi-Billion Parameter Language Models Using Model
Parallelism. ArXivPreprintArXiv:1909.08053,2019.
Elizabeth M. Siefert, Sindhuja Uppuluri, Jianing Mu, Marlie C. Tandoc, James W. Antony, and
AnnaC.Schapiro. "Siefert2024",2024.
YonghaoSong,XueyuJia,LieYang,andLonghanXie. Transformer-BasedSpatial-TemporalFeature
LearningforEEGDecoding. ArXivPreprintArXiv:2106.11170,2021.
17

YonghaoSong,QingqingZheng,BingchuanLiu,andXiaorongGao. EEGConformer:Convolutional
TransformerforEEGDecodingandVisualization. IEEETransactionsonNeuralSystemsand
RehabilitationEngineering,31:710–719,2022.
Jan Sosulski, David Hübner, Aaron Klein, and Michael Tangermann. Online Optimization of
Stimulation Speed in an Auditory Brain-Computer Interface Under Time Constraints. ArXiv
PreprintArXiv:2109.06011,2021.
ToyotaroSuzumura,HirokiKanezashi,andShotaroAkahori. GraphAdapterofEEGFoundation
ModelsforParameterEfficientFineTuning. ArXivPreprintArXiv:2411.16155,2024.
MichaelTangermann,Klaus-RobertMüller,AdAertsen,NielsBirbaumer,ChristophBraun,Clemens
Brunner,RobertLeeb,CarstenMehring,KaiJMiller,GernotRMüller-Putz,etal. Reviewofthe
BCICompetitionIV. FrontiersinNeuroscience,6:55,2012.
JackE.Taylor, RasmusSinn, CosimoIaia, andChristianJ.Fiebach. "AlphabeticDecisionTask
(ArialLightFont)",2024.
HugoTouvron,ThibautLavril,GautierIzacard,XavierMartinet,Marie-AnneLachaux,Timothée
Lacroix, BaptisteRozière, NamanGoyal, EricHambro, FaisalAzhar, etal. Llama: Openand
EfficientFoundationLanguageModels. ArXivPreprintArXiv:2302.13971,2023.
HannekeVanDijk,GuidoVanWingen,DamiaanDenys,SebastianOlbrich,RosalindeVanRuth,and
MartijnArns. TheTwoDecadesBrainclinicsResearchArchiveforInsightsinNeurophysiology
(TDBRAIN)Database. ScientificData,9(1):333,2022.
AVaswani. AttentionIsAllYouNeed. AdvancesinNeuralInformationProcessingSystems,2017.
J.Veillette,S.Heald,B.Wittenbrink,andH.Nusbaum. "EEG-Neuroforecasting",2022.
JohnVeillette,PedroLopes,andHowardNusbaum. "IllusionofAgencyOverElectrically-Actuated
Movements",2023.
GuangyuWang,WenchaoLiu,YuhongHe,CongXu,LinMa,andHaifengLi. EEGPT:Pretrained
Transformer for Universal and Reliable Representation of EEG Signals. In The Thirty-Eighth
AnnualConferenceonNeuralInformationProcessingSystems,2024a.
JiquanWang,ShaZhao,ZhilingLuo,YangxuanZhou,HaitengJiang,ShijianLi,TaoLi,andGang
Pan. CBraMod: A Criss-Cross Brain Foundation Model for EEG Decoding. ArXiv Preprint
ArXiv:2412.07236,2024b.
YulinWang,WeiDuan,DeboDong,LihongDing,andXuLei. "ATest-RetestRestingandCognitive
StateEEGDataset",2022.
Benjamin Warner, Antoine Chaffin, Benjamin Clavié, Orion Weller, Oskar Hallström, Said
Taghadouini,AlexisGallagher,RajaBiswas,FaisalLadhak,TomAarsen,etal. Smarter,Better,
Faster,Longer: AModernBidirectionalEncoderforFast,MemoryEfficient,andLongContext
FinetuningandInference. ArXivPreprintArXiv:2412.13663,2024.
MitchellWortsman,GabrielIlharco,SamirYaGadre,RebeccaRoelofs,RaphaelGontijo-Lopes,AriS
Morcos,HongseokNamkoong,AliFarhadi,YairCarmon,SimonKornblith,andLudwigSchmidt.
ModelSoups: AveragingWeightsofMultipleFine-TunedModelsImprovesAccuracyWithout
IncreasingInferenceTime. InKamalikaChaudhuri,StefanieJegelka,LeSong,CsabaSzepesvari,
GangNiu,andSivanSabato,editors,Proceedingsofthe39thInternationalConferenceonMachine
Learning,volume162ofProceedingsofMachineLearningResearch,pages23965–23998.PMLR,
17–23Jul2022. URLhttps://proceedings.mlr.press/v162/wortsman22a.html.
MitchellWortsman,TimDettmers,LukeZettlemoyer,AriMorcos,AliFarhadi,andLudwigSchmidt.
StableandLow-PrecisionTrainingforLarge-ScaleVision-LanguageModels. AdvancesinNeural
InformationProcessingSystems,36:10271–10298,2023.
ChuqinXiang,XinruiFan,DuoBai,KeLv,andXuLei. "AResting-StateEEGDatasetforSleep
Deprivation",2024.
18

ZhendaXie,ZhengZhang,YueCao,YutongLin,JianminBao,ZhuliangYao,QiDai,andHanHu.
SimMIM:ASimpleFrameworkforMaskedImageModeling. InProceedingsoftheIEEE/CVF
ConferenceonComputerVisionandPatternRecognition,pages9653–9663,2022.
ZhengzhuoXu,RuikangLiu,ShuoYang,ZenghaoChai,andChunYuan. LearningImbalancedData
withVisionTransformers. InProceedingsoftheIEEE/CVFConferenceonComputerVisionand
PatternRecognition,pages15793–15803,2023.
ChaoqiYang,DanicaXiao,MBrandonWestover,andJimengSun. Self-SupervisedEEGRepresen-
tationLearningforAutomaticSleepStaging. ArXivPreprintArXiv:2110.15278,2021.
ChaoqiYang,MWestover,andJimengSun. BIOT:BiosignalTransformerforCross-DataLearning
intheWild. AdvancesinNeuralInformationProcessingSystems,36,2024.
WeiboYi,ShuangQiu,KunWang,HongzhiQi,LixinZhang,PengZhou,FengHe,andDongMing.
Evaluation of EEG Oscillatory Patterns and Cognitive Process During Simple and Compound
LimbMotorImagery. PLOSOne,9(12):e114853,2014.
ZhizhangYuan, FanqiShen, MengLi, YuguoYu, ChenhaoTan, andYangYang. BrainWave: A
BrainSignalFoundationModelforClinicalApplications,2024a. URLhttps://arxiv.org/
abs/2402.10251.
ZhizhangYuan,DaozeZhang,JunruChen,GeifeiGu,andYangYang. Brant-2: FoundationModel
forBrainSignals. ArXivPreprintArXiv:2402.10251,2024b.
Biao Zhang and Rico Sennrich. Root Mean Square Layer Normalization. Advances in Neural
InformationProcessingSystems,32,2019.
HongyiZhang,MoustaphaCisse,YannN.Dauphin,andDavidLopez-Paz.Mixup:BeyondEmpirical
Risk Minimization. In International Conference on Learning Representations, 2018. URL
https://openreview.net/forum?id=r1Ddp1-Rb.
Bangyan Zhou, Xiaopei Wu, Zhao Lv, Lei Zhang, and Xiaojin Guo. A Fully Automated Trial
SelectionMethodforOptimizationofMotorImageryBasedBrain-ComputerInterface. PLOS
One,11(9):e0162657,2016.
NataliaZhozhikashvili,MariaProtopova,TatianaShkurenko,MarieArsalidou,IlyaZakharov,Boris
Kotchoubey,SergeyMalykh,andYuriPavlov. "SternbergDifficult",2024.
IgorZyma,SergiiTukaev,IvanSeleznov,KenKiyono,AntonPopov,MariiaChernykh,andOleksii
Shpenkov. ElectroencephalogramsDuringMentalArithmeticTaskPerformance. Data,4(1):14,
2019.
19

Appendix
A Configurations
WereportthehyperparametersusedtotraintheREVEsuiteofmodels,includingdatapreprocessing
steps,self-supervisedmaskingconfigurations,andoptimizersettingsgoverningthetrainingdynamics.
Notationsareconsistentwiththoseinthemaintext.
| Table5: Exhaustivelistofallhyperparametervalues |     |       |     |
| ----------------------------------------------- | --- | ----- | --- |
| Variable Meaning                                |     | Value |     |
Datapreprocessing
| w Windowsize       |     | 1s     |     |
| ------------------ | --- | ------ | --- |
| o Overlap          |     | 0.1s   |     |
| σ Positionnoisestd |     | 0.25cm |     |
noise
Maskingparameters
| M Totalmaskingratio |     | 55% |     |
| ------------------- | --- | --- | --- |
r
| R Spatialmaskingradius |     | 3cm |     |
| ---------------------- | --- | --- | --- |
s
| R   |     | 3seconds |     |
| --- | --- | -------- | --- |
t Temporalmaskingradius
| D r Dropoutratio       |     | 10% |     |
| ---------------------- | --- | --- | --- |
| R Dropoutspatialradius |     | 4cm |     |
d
Trainingdynamics
| Optimizer |     | StableAdamW       |     |
| --------- | --- | ----------------- | --- |
| Scheduler |     | WarmupStableDecay |     |
=2.4·10−4
| η Peaklearningrate     |     | η        |     |
| ---------------------- | --- | -------- | --- |
| β ,β Momentumconstants |     | 0.9,0.95 |     |
1 2
| ε Numericalstabilitybias |     | 10−9 |     |
| ------------------------ | --- | ---- | --- |
| σ Initializationstd      |     | 0.02 |     |
init
| Batchsize                 |     | 4,096 |     |
| ------------------------- | --- | ----- | --- |
| λ Secondarylossmultiplier |     | 0.1   |     |
Wereporthowthescalednumberofparametersisallocatedacrossourmodels. Wealsoindicatethe
numberofFourierfrequenciesencoded(seeSection2.2). Notethatnofrequencytruncationwas
required,aswecloselymatchedthehiddendimensionofourmodelstothenumberofcomponents
generatedbythe4DPEmodule.
Table6: Summaryofencoderconfigurationsfordifferentsizes
| Size depth | n_heads dim | params(M) | n freq |
| ---------- | ----------- | --------- | ------ |
| Small 4    | 8 512       | 12        | 4      |
| Base 22    | 8 512       | 69        | 4      |
| Large 22   | 19 1250     | 408       | 5      |
B Pretrainingdataset
Weincludeasummarizeddescriptionofthepretrainingdatasetcomposition,groupedbycategory,
platformoforiginandnumberofchannels. Thefinaldatasetspans61,415hoursofrecordingsfrom
92datasetsencompassing24,274subjects.
20

| Table7: | Detailedoverviewofthepretrainingdatasets. |          |     |
| ------- | ----------------------------------------- | -------- | --- |
| Group   | Subjects Duration(hours)                  | Datasets |     |
Category
| BCI       | 791    | 457    | 28  |
| --------- | ------ | ------ | --- |
| Cognition | 4,193  | 10,376 | 56  |
| Clinic    | 19,290 | 50,581 | 8   |
Platform
| TUH       | 14,987 | 26,847 | 1   |
| --------- | ------ | ------ | --- |
| Physionet | 607    | 22,707 | 2   |
| OpenNeuro | 4153   | 10,194 | 56  |
| MOABB     | 711    | 384    | 27  |
| Other     | 3,802  | 1,250  | 6   |
Channels
| [3−30[   | 19,871 | 50,870 | 31  |
| -------- | ------ | ------ | --- |
| [30−80[  | 1,781  | 1,516  | 48  |
| [80−129] | 2,622  | 9,027  | 13  |
| Total    | 24,274 | 61,415 | 92  |
We provide and exhaustive list of the datasets in the pretraining set, along with their respective
licenses.
MOABB (Aristimunha et al., 2023): AlexMI (Barachant, 2012), BNCI2014004 (Leeb et al.,
2007),BNCI2015001(Falleretal.,2012),BNCI2015004(Schereretal.,2015),Cho2017(Choetal.,
2017),Lee2019MI(Leeetal.,2019),Liu2024(Liuetal.,2024),Ofner2017(Ofneretal.,2017),
Shin2017A(Shinetal.,2016),Weibo2014(Yietal.,2014),Zhou2016(Zhouetal.,2016),Schirrmeis-
ter2017(Schirrmeisteretal.,2017),Kalunga2016(Kalungaetal.,2015),Lee2019SSVEP(Leeetal.,
2019),Nakanishi2015(Nakanishietal.,2015),BI2014a(Korczowskietal.,2019b),BI2014b(Ko-
rczowski et al., 2019c), BNCI2014008 (Riccio et al., 2013), BNCI2014009 (Aricò et al., 2014),
BNCI2015003(Gugeretal.,2009),EPFLP300(Hoffmannetal.,2008),BI2015a(Korczowskietal.,
2019a),BI2015b(Korczowskietal.,2019c),Sosulski2019(Sosulskietal.,2021),Lee2019ERP(Lee
etal.,2019)
MOABBisunderaBSD3-ClauseLicense.
Physionet(Goldbergeretal.,2000): Siena(Detti,2020;Dettietal.,2020),undertheCreative
Commons Attribution 4.0 International Public License, ICARE (Amorim et al., 2023) under the
CreativeCommonsAttribution-NonCommercial-ShareAlike4.0InternationalPublicLicense,
OpenNeuro: ds004706(Rudoleretal.,2023),ds004582(Makowskietal.,2023),ds004356(Shan
et al., 2022), ds004817 (Grootswagers et al., 2023b), ds005189 (Helbing et al., 2024),
ds003887 (Shatek et al., 2023), ds004043 (Moerel et al., 2022), ds003885 (Shatek et al., 2021),
ds004357(Grootswagersetal.,2024),ds003825(Grootswagersetal.,2022),ds004816(Grootswa-
gers et al., 2023a), ds004840 (Cordoba-Silva et al., 2023), ds005262 (Metwalli et al., 2024),
ds004477 (Papastylianou et al., 2023), ds005273 (Esteban et al., 2024), ds004561 (Veillette
et al., 2023), ds004951 (Haupt et al., 2024), ds004324 (Chacón and Wriessnegger, 2023),
ds005095 (Zhozhikashvili et al., 2024), ds005509 (Shirazi et al., 2025), ds005505, ds005506,
ds005507, ds005510, ds005511, ds005512, ds005514 (Shirazi et al., 2024b; Alexander et al.,
2017)ds001787(DelormeandBrandmeyer,2024),ds003690(RibeiroandCastelo-Branco,2021),
ds004603 (Lowe et al., 2023), ds003969 (Delorme and Braboszcz, 2021), ds004147 (Hassall
etal.,2024),ds003004(OntonandMakeig,2022),ds002721(Dalyetal.,2020),ds004152(Has-
sall et al., 2022a) , ds005089 (Aguado-Lopez et al., 2024), ds004264 (Hassall et al., 2022b),
ds004315 (Cavanagh and Jackson, 2022), ds004408 (Bialas et al., 2023), ds005121 (Siefert
et al., 2024), ds003775 (Hatlestad-Hall et al., 2022), ds004572 (Kekecs and Farahzadi, 2024),
ds002778 (Rockhill et al., 2020), ds003846 (Gehrke et al., 2024), ds004279 (Araya et al.,
2023), ds004148 (Wang et al., 2022), ds004902 (Xiang et al., 2024), ds002680 (Delorme
and Fabre-Thorpe, 2020), ds004284 (Veillette et al., 2022), ds004395 (Kahana et al., 2023),
21

ds005508(Shirazietal.,2024a),ds005697(LiandZhao,2024),ds005620(Bajwa1etal.,2024),
ds005594 (Taylor et al., 2024), ds005586 (Baykan and Schütz, 2024). OpenNeuro is under the
CreativeCommonsCC0license.
Othersources: NMT(Khanetal.,2022)undertheCreativeCommonsAttributionLicense(CC
BY),HMS(Rametal.,2024)undertheAttribution-NonCommercial4.0International(CC-BY-NC-
4.0), SparrKULee (Accou et al., 2023) under the Attribution-Non Commercial 4.0 International
(CC-BY-NC-4.0), Inria Large (Dreyer et al., 2023) the data on Zenodo being under the Creative
CommonsAttribution4.0International,THINGS2(Giffordetal.,2022),undertheCC-ByAttribution
4.0Internationallicense,TDBRAIN(VanDijketal.,2022),undertheGPL-3.0license,TUH(Obeid
andPicone,2016),freelyavailablewithregistrationrequired.
C Detailedresults
Thissectionpresentsdetailedresultsondownstreamtasksalongwithconcisedescriptionsofthe
datasets.
C.1 EmotionRecognition
FACED(Chenetal.,2023)WeevaluateontheFACEDdataset,whichcontains32-channelEEG
recordings(originallyat250Hz,resampledto200Hz)from123subjectsacrossnineemotionclasses.
Thedataissegmentedinto10,332samplesof10secondseach. Wefollowthestandardsplit: subjects
1–80fortraining,81–100forvalidation,and101–123fortesting.
Table8: Theresultsofdifferentmethodsonemotionrecognition(FACED,9-class).
| Methods         | BalancedAccuracy | Cohen’sKappa  | WeightedF1    |
| --------------- | ---------------- | ------------- | ------------- |
| EEGNet          | 0.4090±0.0122    | 0.3342±0.0251 | 0.4124±0.0141 |
| EEGConformer    | 0.4559±0.0125    | 0.3858±0.0186 | 0.4514±0.0107 |
| SPaRCNet        | 0.4673±0.0155    | 0.3978±0.0289 | 0.4729±0.0133 |
| ContraWR        | 0.4887±0.0078    | 0.4231±0.0151 | 0.4884±0.0074 |
| CNN-Transformer | 0.4697±0.0132    | 0.4017±0.0168 | 0.4720±0.0125 |
| FFCL            | 0.4673±0.0158    | 0.3987±0.0383 | 0.4699±0.0145 |
| ST-Transformer  | 0.4810±0.0079    | 0.4137±0.0133 | 0.4795±0.0096 |
| BIOT            | 0.5118±0.0118    | 0.4476±0.0254 | 0.5136±0.0112 |
| LaBraM-Base     | 0.5273±0.0107    | 0.4698±0.0188 | 0.5288±0.0102 |
| CBraMod         | 0.5509±0.0089    | 0.5041±0.0122 | 0.5618±0.0093 |
| REVE-Base(ours) | 0.5646±0.0164    | 0.5080±0.0191 | 0.5659±0.0172 |
C.2 MentalDisorderDiagnosis
Mumtaz(Mumtaz,2016)WeusetheMumtaz2016dataset,whichincludesEEGrecordingsfrom
34individualswithmajordepressivedisorder(MDD)and30healthycontrols, acquiredfrom19
electrodes(10–20system)at256Hz. Onlytheeyes-openandeyes-closedsessionsareused. Signals
areband-passfiltered(0.3–75Hz),notchfilteredat50Hz,resampledto200Hz,andsegmentedinto
7,143samplesof5secondseach. Thesplitincludes24MDDand19controlsubjectsfortraining,5
MDDand4controlsforvalidation,and5MDDand5controlsfortesting. ThedatasetisunderCC
BY4.0.
22

Table9: Theresultsofdifferentmethodsonmentaldisorderdiagnosis(Mumtaz2016,2-class).
| Methods | BalancedAccuracy | AUC-PR        | AUROC         |
| ------- | ---------------- | ------------- | ------------- |
| EEGNet  | 0.9232±0.0104    | 0.9626±0.0095 | 0.9639±0.0093 |
|         | 0.9308±0.0117    | 0.9684±0.0105 | 0.9702±0.0101 |
EEGConformer
|     | 0.9316±0.0095 | 0.9754±0.0065 | 0.9781±0.0083 |
| --- | ------------- | ------------- | ------------- |
SPaRCNet
|     | 0.9195±0.0115 | 0.9589±0.0102 | 0.9621±0.0092 |
| --- | ------------- | ------------- | ------------- |
ContraWR
|     | 0.9305±0.0068 | 0.9757±0.0074 | 0.9742±0.0059 |
| --- | ------------- | ------------- | ------------- |
CNN-Transformer
|     | 0.9314±0.0038 | 0.9717±0.0021 | 0.9753±0.0033 |
| --- | ------------- | ------------- | ------------- |
FFCL
| ST-Transformer | 0.9135±0.0103 | 0.9578±0.0086 | 0.9594±0.0059 |
| -------------- | ------------- | ------------- | ------------- |
|                | 0.9358±0.0052 | 0.9736±0.0034 | 0.9758±0.0042 |
BIOT
|     | 0.9409±0.0079 | 0.9798±0.0093 | 0.9782±0.0057 |
| --- | ------------- | ------------- | ------------- |
LaBraM-Base
|     | 0.9560±0.0056 | 0.9923±0.0032 | 0.9921±0.0025 |
| --- | ------------- | ------------- | ------------- |
CBraMod
| REVE-Base(ours) | 0.9644±0.0097 | 0.9961±0.0013 | 0.9957±0.0015 |
| --------------- | ------------- | ------------- | ------------- |
C.3 MentalStressDetection
MAT(Zymaetal.,2019)TheMentalArithmeticdatasetcontainsEEGrecordingsfrom36subjects,
labeledas“with”or“without”mentalstressdependingonwhetheramentalarithmetictaskwas
beingperformed. Signalswererecordedfrom20electrodes(10–20system)at500Hz,band-pass
filtered(0.5–45Hz),resampledto200Hz,andsegmentedinto1,707samplesof5seconds. Subjects
1–28areusedfortraining,29–32forvalidation,and33–36fortesting. TheMentalArithmeticdataset
isundertheOpenDataCommonsAttributionLicensev1.0.
Table10: Theresultsofdifferentmethodsonmentalstressdetection(MAT,2-class).
| Methods         | BalancedAccuracy | AUC-PR        | AUROC         |
| --------------- | ---------------- | ------------- | ------------- |
| EEGNet          | 0.6770±0.0116    | 0.5763±0.0102 | 0.7321±0.0108 |
| EEGConformer    | 0.6805±0.0123    | 0.5829±0.0134 | 0.7424±0.0128 |
| SPaRCNet        | 0.6879±0.0107    | 0.5825±0.0193 | 0.7418±0.0132 |
| ContraWR        | 0.6631±0.0097    | 0.5787±0.0164 | 0.7332±0.0082 |
| CNN-Transformer | 0.6779±0.0268    | 0.5777±0.0285 | 0.7258±0.0336 |
| FFCL            | 0.6798±0.0142    | 0.5786±0.0266 | 0.7330±0.0198 |
| ST-Transformer  | 0.6631±0.0173    | 0.5672±0.0259 | 0.7132±0.0174 |
| BIOT            | 0.6875±0.0186    | 0.6004±0.0195 | 0.7536±0.0144 |
| LaBraM-Base     | 0.6909±0.0125    | 0.5999±0.0155 | 0.7721±0.0093 |
| CBraMod         | 0.7256±0.0132    | 0.6267±0.0099 | 0.7905±0.0073 |
| REVE-Base(ours) | 0.7660±0.0355    | 0.7470±0.0807 | 0.8450±0.0514 |
C.4 ImaginedSpeech
BCIC2020-3(Jeongetal.,2022)BCIC2020-3isanimaginedspeechEEGdatasetfrom15subjects,
recordedwith64channelsat256Hzwhilesubjectssilentlyimaginedfivephrases(“hello”,“help
me”, “stop”, “thank you”, “yes”) without any articulation. Each phrase has 80 trials per subject,
totaling6,0003-secondsamples. Thedataisresampledto200Hz. Theofficialsplitincludes60
trialsperclassfortraining,10forvalidation,and10fortesting. BCIC2020-3isundertheCreative
CommonsAttributionNoDerivativeslicense(CCBY-ND4.0).
23

Table11: Theresultsofdifferentmethodsonimaginedspeechclassification(BCIC2020-3,5-class).
| Methods | BalancedAccuracy | Cohen’sKappa  |     | WeightedF1    |     |
| ------- | ---------------- | ------------- | --- | ------------- | --- |
| EEGNet  | 0.4413±0.0096    | 0.3016±0.0123 |     | 0.4413±0.0102 |     |
|         | 0.4506±0.0133    | 0.3133±0.0183 |     | 0.4488±0.0154 |     |
EEGConformer
|     | 0.4426±0.0156 | 0.3033±0.0233 |     | 0.4420±0.0108 |     |
| --- | ------------- | ------------- | --- | ------------- | --- |
SPaRCNet
|     | 0.4257±0.0162 | 0.3078±0.0218 |     | 0.4407±0.0182 |     |
| --- | ------------- | ------------- | --- | ------------- | --- |
ContraWR
|     | 0.4533±0.0092 | 0.3166±0.0118 |     | 0.4506±0.0127 |     |
| --- | ------------- | ------------- | --- | ------------- | --- |
CNN-Transformer
|     | 0.4678±0.0197 | 0.3301±0.0359 |     | 0.4689±0.0205 |     |
| --- | ------------- | ------------- | --- | ------------- | --- |
FFCL
| ST-Transformer | 0.4126±0.0122 | 0.2941±0.0159 |     | 0.4247±0.0138 |     |
| -------------- | ------------- | ------------- | --- | ------------- | --- |
|                | 0.4920±0.0086 | 0.3650±0.0176 |     | 0.4917±0.0079 |     |
BIOT
|     | 0.5060±0.0155 | 0.3800±0.0242 |     | 0.5054±0.0205 |     |
| --- | ------------- | ------------- | --- | ------------- | --- |
LaBraM-Base
|     | 0.5373±0.0108 | 0.4216±0.0163 |     | 0.5383±0.0096 |     |
| --- | ------------- | ------------- | --- | ------------- | --- |
CBraMod
| REVE-Base(ours) | 0.5635±0.0123 | 0.4543±0.0154 |     | 0.5633±0.0124 |     |
| --------------- | ------------- | ------------- | --- | ------------- | --- |
C.5 MotorImageryClassification
PhysioNet-MI(Goldbergeretal.,2000)isusedformotorimageryclassification. Itcontainsrecord-
ingswith64channelsata160Hzsamplingrateandincludes4classes: leftfist,rightfist,bothfists,
andfeet. AsinCBraMod, weselect4-secondsamplesofthesignals, resultingin9,837samples.
FollowingCBraMod’sprotocol,subjects1–70areusedfortraining,71–89forvalidation,and90–109
fortesting. Weretainallsubjectsandusefull4-secondwindowstostayconsistentwithCBraMod. To
handlelowersamplingratesinsomerecordings,weloadalldataat128Hz(usinga64Hzlow-pass
filter)beforeresamplingto200Hz. Physionet-MIisundertheOpenDataCommonsAttribution
Licensev1.0.
BCIC-IV-2a(Tangermannetal.,2012)isalsousedformotorimageryclassification. ItcontainsEEG
recordingsfrom9subjectsperforming4motorimagerytasks: lefthand,righthand,bothfeet,and
tongue. Datawerecollectedover2sessionswith22electrodesat250Hz. Eachsessionincludes288
trials(72pertask). Weusethe[2,6]secondwindowfromeachtrial,applya0.5–99.5Hzband-pass
filter,resampleto200Hz,andapplyEuclideanAlignment(HeandWu,2019),proventobeeffective
onthistask(ElOuahidietal.,2024),resultingin51844-secondsamples.
Table12: TheresultsofdifferentmethodsonMotorImageryclassification.
|     | PhysioNet-MI,4-class |     |     | BCIC-IV-2a,4-class |     |
| --- | -------------------- | --- | --- | ------------------ | --- |
Methods BalancedAccuracy Cohen’sKappa WeightedF1 BalancedAccuracy Cohen’sKappa WeightedF1
EEGNet 0.5814±0.0125 0.4468±0.0199 0.5796±0.0115 0.4482±0.0094 0.2693±0.0121 0.4226±0.0108
EEGConformer 0.6049±0.0104 0.4736±0.0171 0.6062±0.0095 0.4696±0.0106 0.2924±0.0141 0.4533±0.0128
SPaRCNet 0.5932±0.0152 0.4564±0.0234 0.5937±0.0147 0.4635±0.0117 0.2847±0.0147 0.4432±0.0126
ContraWR 0.5892±0.0133 0.4527±0.0248 0.5918±0.0116 0.4678±0.0125 0.2905±0.0160 0.4413±0.0142
| 0.6053±0.0118 | 0.4725±0.0223 | 0.6041±0.0105 | 0.4600±0.0108 | 0.2800±0.0148 | 0.4460±0.0114 |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
(CNN-Transformer
FFCL 0.5726±0.0092 0.4323±0.0182 0.5701±0.0079 0.4470±0.0143 0.2627±0.0176 0.4238±0.0139
ST-Transformer 0.6035±0.0081 0.4712±0.0199 0.6053±0.0075 0.4575±0.0145 0.2733±0.0198 0.4471±0.0142
BIOT 0.6153±0.0154 0.4875±0.0272 0.6158±0.0197 0.4748±0.0093 0.2997±0.0139 0.4607±0.0125
LaBraM-Base 0.6173±0.0122 0.4912±0.0192 0.6177±0.0141 0.4869±0.0085 0.3159±0.0154 0.4758±0.0103
CBraMod 0.6417±0.0091 0.5222±0.0169 0.6427±0.0100 0.5138±0.0066 0.3518±0.0094 0.4984±0.0085
REVE-Base(ours) 0.6480±0.0140 0.5306±0.0187 0.6484±0.0170 0.6396±0.0095 0.5194±0.0126 0.6339±0.0110
C.6 SleepStaging
ISRUC(Khalighietal.,2016)WeusethesleepstagingtaskontheISRUCdataset(Subgroup1),
whichcontainsPSGrecordingsfrom100subjects. OnlyEEGsignalsareused(6channels,sampled
at 200 Hz), segmented into 89,240 30-second epochs, each labeled with one of five sleep stages
followingAASMstandards. Subjects1–80areusedfortraining,81–90forvalidation,and91–100
fortesting. Asinpriorwork,thetaskisframedasasequence-to-sequenceclassificationproblem,
usingsequencesof20consecutiveepochstomodelstagetransitions. ISRUCisfreelyaccessible
online.
24

*Inthebaselinecode,
Table13: Theresultsofdifferentmethodsonsleepstaging(ISRUC,5-class).
achinelectrodemighthavebeenusedinsteadofanEEGone;REVEresultsarereportedwithoutit.
| Methods         | BalancedAccuracy | Cohen’sKappa  | WeightedF1    |
| --------------- | ---------------- | ------------- | ------------- |
| EEGNet          | 0.7154±0.0121    | 0.7040±0.0173 | 0.7513±0.0124 |
| EEGConformer    | 0.7400±0.0133    | 0.7143±0.0162 | 0.7634±0.0151 |
| SPaRCNet        | 0.7487±0.0075    | 0.7097±0.0132 | 0.7624±0.0092 |
| ContraWR        | 0.7402±0.0126    | 0.7178±0.0156 | 0.7610±0.0137 |
| CNN-Transformer | 0.7363±0.0087    | 0.7129±0.0121 | 0.7719±0.0105 |
| FFCL            | 0.7277±0.0182    | 0.7016±0.0291 | 0.7614±0.0197 |
| ST-Transformer  | 0.7381±0.0205    | 0.7013±0.0352 | 0.7681±0.0175 |
| DeepSleepNet    | 0.7419±0.0144    | 0.7036±0.0241 | 0.7643±0.0122 |
| USleep          | 0.7586±0.0116    | 0.7209±0.0143 | 0.7805±0.0105 |
| BIOT            | 0.7527±0.0121    | 0.7192±0.0231 | 0.7790±0.0146 |
| LaBraM-Base     | 0.7633±0.0102    | 0.7231±0.0182 | 0.7810±0.0133 |
| CBraMod         | 0.7865±0.0110    | 0.7442±0.0152 | 0.8011±0.0099 |
| REVE-Base*      | 0.7819±0.0078    | 0.7500±0.0156 | 0.8005±0.0135 |
HMC (Alvarez-Estevez and Rijsman, 2021). The Haaglanden Medisch Centrum (HMC) Sleep
StagingDatabaseisasleepstagedetectiondataset,consistingof151full-nightpolysomnographic
(PSG)recordingscollectedfrompatientsreferredforsleepstudies. ThedataincludesEEG,EOG,
EMG, and ECG channels, with a sampling rate of 256 Hz, and annotations for five sleep stages
(Wake,N1,N2,N3,REM)manuallyscoredbytrainedsleeptechnicians. HMCisundertheCreative
CommonsAttribution4.0InternationalPublicLicense.
Table14: Theresultsofdifferentmethodsonsleepstaging(HMC,5-class).
| Methods         | BalancedAccuracy | Cohen’sKappa  | WeightedF1    |
| --------------- | ---------------- | ------------- | ------------- |
| SPaRCNet        | 0.4756±0.1109    | 0.3147±0.1315 | 0.4108±0.1310 |
| ContraWR        | 0.4242±0.0541    | 0.2340±0.0554 | 0.2987±0.0288 |
| CNN-Transformer | 0.6573±0.0141    | 0.5961±0.0105 | 0.6896±0.0065 |
| FFCL            | 0.4427±0.0702    | 0.2542±0.0654 | 0.2902±0.0485 |
| ST-Transformer  | 0.2559±0.0141    | 0.0503±0.0183 | 0.1428±0.0122 |
| BIOT            | 0.6862±0.0041    | 0.6295±0.0113 | 0.7091±0.0147 |
| LaBraM-Base     | 0.7286±0.0101    | 0.6812±0.0073 | 0.7554±0.0024 |
| REVE-Base       | 0.7401±0.0075    | 0.6982±0.0078 | 0.7638±0.0074 |
C.7 EventTypeClassification
TUEV (Obeid and Picone, 2016) is an EEG dataset with six annotated classes: spike and sharp
wave,generalizedperiodicepileptiformdischarges,periodiclateralizedepileptiformdischarges,eye
movement,artifact,andbackground. Therecordingsuse23channelsata256Hzsamplingrate. For
consistencywithCBraMod,BIOT,andLaBraM,weusedBIOT’sprocessingscriptswhichpreprocess
the dataset using 16 common bipolar montage channels in the 10-20 system, apply a 0.3–75 Hz
band-passfilter,removepowerlinenoisewitha60Hznotchfilter,andresampleto200Hz. The
datasetissplitinto112,4915-secondsamples. Wefollowtheoriginaltraining-testsplitandfurther
dividethetrainingsetinto80%trainingand20%validation,matchingBIOTsetting. Toprovideour
modelwiththeelectrodepositions,weusedtheaveragepositionofeachbipolarmontage. TUEVis
partoftheTUHdataset,whichisfreelyavailablewithregistrationrequired.
25

Table15: Theresultsofdifferentmethodsoneventtypeclassification(TUEV,6-class).
| Methods | BalancedAccuracy | Cohen’sKappa  | WeightedF1    |
| ------- | ---------------- | ------------- | ------------- |
| EEGNet  | 0.3876±0.0143    | 0.3577±0.0155 | 0.6539±0.0120 |
|         | 0.4074±0.0164    | 0.3967±0.0195 | 0.6983±0.0152 |
EEGConformer
|     | 0.4161±0.0262 | 0.4233±0.0181 | 0.7024±0.0104 |
| --- | ------------- | ------------- | ------------- |
SPaRCNet
|     | 0.4384±0.0349 | 0.3912±0.0237 | 0.6893±0.0136 |
| --- | ------------- | ------------- | ------------- |
ContraWR
|     | 0.4087±0.0161 | 0.3815±0.0134 | 0.6854±0.0293 |
| --- | ------------- | ------------- | ------------- |
CNN-Transformer
|     | 0.3979±0.0104 | 0.3732±0.0188 | 0.6783±0.0120 |
| --- | ------------- | ------------- | ------------- |
FFCL
| ST-Transformer | 0.3984±0.0228 | 0.3765±0.0306 | 0.6823±0.0190 |
| -------------- | ------------- | ------------- | ------------- |
|                | 0.5281±0.0225 | 0.5273±0.0249 | 0.7492±0.0082 |
BIOT
|     | 0.6409±0.0065 | 0.6637±0.0093 | 0.8312±0.0052 |
| --- | ------------- | ------------- | ------------- |
LaBraM-Base
|     | 0.6581±0.0156 | 0.6622±0.0136 | 0.8315±0.0040 |
| --- | ------------- | ------------- | ------------- |
LaBraM-Large
|     | 0.6616±0.0170 | 0.6745±0.0195 | 0.8329±0.0086 |
| --- | ------------- | ------------- | ------------- |
LaBraM-Huge
| CBraMod | 0.6671±0.0107 | 0.6772±0.0096 | 0.8342±0.0064 |
| ------- | ------------- | ------------- | ------------- |
|         | 0.6759±0.0229 | 0.6783±0.0199 | 0.8451±0.0129 |
REVE-Base(ours)
C.8 AbnormalDetection
TUAB(ObeidandPicone,2016)isusedforabnormalEEGdetection,whererecordingsarelabeled
asnormalorabnormal. Itsharesthesame23-channel,256HzformatasTUEV.Thedatasetissplit
into409,45510-secondsamplesforbinaryclassification. Wefollowtheprovidedtraining-testsplit
andapplyan80%-20%training-validationsplit, consistentwithBIOT.Weresampledat200Hz,
band-passat0.5-99.5Hz,anddirectlyusedallchannelsandtheirpositions. TUABispartofthe
TUHdataset,whichisfreelyavailablewithregistrationrequired.
Table16: Theresultsofdifferentmethodsonabnormaldetection(TUAB,2-class).
| Methods         | BalancedAccuracy | AUC-PR        | AUROC         |
| --------------- | ---------------- | ------------- | ------------- |
| EEGNet          | 0.7642±0.0036    | 0.8299±0.0043 | 0.8412±0.0031 |
| EEGConformer    | 0.7758±0.0049    | 0.8427±0.0054 | 0.8445±0.0038 |
| SPaRCNet        | 0.7896±0.0018    | 0.8414±0.0018 | 0.8676±0.0012 |
| ContraWR        | 0.7746±0.0041    | 0.8421±0.0104 | 0.8456±0.0074 |
| CNN-Transformer | 0.7777±0.0022    | 0.8433±0.0039 | 0.8461±0.0013 |
| FFCL            | 0.7848±0.0038    | 0.8448±0.0065 | 0.8569±0.0051 |
| ST-Transformer  | 0.7966±0.0023    | 0.8521±0.0026 | 0.8707±0.0019 |
| BIOT            | 0.7959±0.0057    | 0.8792±0.0023 | 0.8815±0.0043 |
| LaBraM-Base     | 0.8140±0.0019    | 0.8965±0.0016 | 0.9022±0.0009 |
| LaBraM-Large    | 0.8226±0.0015    | 0.9130±0.0005 | 0.9127±0.0005 |
| LaBraM-Huge     | 0.8258±0.0011    | 0.9204±0.0011 | 0.9162±0.0016 |
| CBraMod         | 0.8289±0.0022    | 0.9258±0.0008 | 0.9227±0.0011 |
| REVE-Base(ours) | 0.8315±0.0014    | 0.9281±0.0009 | 0.9245±0.0013 |
D AblationontheSSLMethod
Thefinalpretraininghyperparameterswereselectedbasedonaseriesofablationstudies,theresults
ofwhicharepresentedinthissection.
Table17reportstheimpactofthesecondarypretraininglossoneightdownstreamtasksusingREVE-
Small, evaluated under frozen-backbone, linear probing (LP), and full fine-tuning (FT) settings.
Resultsobtainedwithbothlossesarecomparedtothoseusingonlytheprimaryloss. Thesecondary
lossconsistentlyimprovesperformanceacrossnearlyalldatasets,enhancingresultsinbothLPand
FTsettings,whileitsremovalleadstoasubstantialdrop,underscoringitsimportanceforthemodel
toproducestrongembeddings.
TheresultsinTable18showthatablockmaskingratioof55%yieldsthebestoverallperformance,
providing stable results across both fine-tuned and frozen settings and eight datasets (Mumtaz,
TUAB,ISRUC,HMC,BCIC2020-3,TUEV,PhysioNetMI,andFaced). Incontrast,randommasking
26

Table 17: Effect of 2nd loss during pretraining and finetuning. The reported metric is balanced
accuracy. Bestresultsperdatasetareinbold.
|             |     |             |     | LP          |     |             | FT          |
| ----------- | --- | ----------- | --- | ----------- | --- | ----------- | ----------- |
| Dataset     |     | No2ndloss   |     | +2ndloss    |     | No2ndloss   | +2ndloss    |
| Mumtaz      |     | 0.818±0.043 |     | 0.920±0.018 |     | 0.818±0.043 | 0.922±0.018 |
| TUAB        |     | 0.797±0.004 |     | 0.802±0.005 |     | 0.803±0.003 | 0.810±0.005 |
| ISRUC       |     | 0.699±0.006 |     | 0.625±0.003 |     | 0.777±0.002 | 0.770±0.002 |
| HMC         |     | 0.598±0.008 |     | 0.591±0.005 |     | 0.713±0.011 | 0.723±0.005 |
| BCIC2020-3  |     | 0.234±0.009 |     | 0.237±0.008 |     | 0.390±0.017 | 0.481±0.008 |
| TUEV        |     | 0.442±0.060 |     | 0.520±0.005 |     | 0.533±0.024 | 0.623±0.011 |
| PhysioNetMI |     | 0.379±0.058 |     | 0.533±0.019 |     | 0.563±0.011 | 0.583±0.009 |
| Faced       |     | 0.220±0.008 |     | 0.233±0.004 |     | 0.302±0.016 | 0.410±0.004 |
| Avg.        |     | 0.523       |     | 0.558       |     | 0.612       | 0.665       |
Table18: Performancecomparisonacrossdifferentmaskingratios(0.25,0.55,0.75)betweenblock
maskingstrategyandrandommasking,evaluatedforfullfine-tuningversusfrozenembeddings. We
displaytheaveragebalancedaccuracyonthesmallmodelovereightdownstreamtasks.
|     |              |      |     | Frozen |       | FullFine-Tuning |       |
| --- | ------------ | ---- | --- | ------ | ----- | --------------- | ----- |
|     | MaskingRatio |      |     | Random | Block | Random          | Block |
|     |              | 0.25 |     | 0.523  | 0.513 | 0.612           | 0.602 |
|     |              | 0.55 |     | 0.550  | 0.558 | 0.643           | 0.665 |
|     |              | 0.75 |     | 0.519  | 0.546 | 0.606           | 0.655 |
favorssmallerratios(25%),butitsunstructurednatureleadstohighlyredundantinputs,makingthe
reconstructiontaskartificiallyeasier. ThesefindingsalignwithablationresultsreportedinCbramod,
Labram,andBIOT.
Table19: AblationstudyonPhysioNetMIandMentalArithmeticdatasets. Thereportedmetricis
balancedaccuracy,withtheaveragecomputedacrossbothtasks,withtheBasemodel.
*Notethatthelearnablepositionalencodingmatchesthebaseline,butdoesnotallowfortheextension
tolargertimewindowsorunseenspatialconfigurations.
| Ablatedcomponent     |     |     | PhysionetMI   |     | MentalArithmetic |              | Average      |
| -------------------- | --- | --- | ------------- | --- | ---------------- | ------------ | ------------ |
| LearnablePE*         |     |     | 0.650±0.0113  |     |                  | 0.752±0.0421 | 0.701±0.0218 |
| MLP4D                |     |     | 0.637±0.0056  |     |                  | 0.717±0.0425 | 0.677±0.0214 |
| Positionnoise        |     |     | 0.628±0.0084  |     |                  | 0.692±0.0665 | 0.660±0.0335 |
| Dropoutblockmasking  |     |     | 0.645±0.0155  |     |                  | 0.678±0.0521 | 0.662±0.0272 |
| Temporalblockmasking |     |     | 0.646±0.0155  |     |                  | 0.723±0.0422 | 0.685±0.0225 |
| BasePerformance      |     |     | 0.6480±0.0140 |     | 0.7660±0.0355    |              | 0.707±0.0191 |
Table 19 presents an ablation study on two downstream tasks to assess the contribution of each
componentinourSSLpipeline. Allcomponentsappeartocontributepositivelytoperformance. The
“LearnablePE”lineisnotatrueablation,butratheravariantusinglearnablepositionalembeddings,
whereaseparateembeddingislearnedforeachelectrodeandtimeindexobservedduringpretraining.
Althoughthisapproachperformswell,itislimitedtothespatialandtemporalconfigurationsseen
duringtraining(approximately400uniqueelectrodenames,over10-secondwindows)anddoesnot
generalizetolongersequencesorunseenelectrodelayouts,unlikeREVE’s4Dpositionalencoding.
Table 20 presents an ablation study on the choice of activation and normalization functions, an
importantdesignfactorintransformer-basedfoundationmodels. WecompareGEGLU+RMSNorm,
GELU + RMSNorm, and GEGLU + LayerNorm configurations during pretraining, and report
downstreamperformanceafterfine-tuningonthreedatasetsusingtheREVE-Smallmodel.
27

Table 20: Ablation study on activation functions and normalization layers (GEGLU vs. GELU,
RMSNormvs. LayerNorm). WereportdownstreambalancedaccuracyafterpretrainingtheREVE-
Smallmodelwitheachconfiguration.
| Dataset     | GEGLU+RMSNorm |             |     | GELU+RMSNorm |     | GEGLU+LayerNorm |
| ----------- | ------------- | ----------- | --- | ------------ | --- | --------------- |
| BCIC-IV-2a  |               | 0.581±0.012 |     | 0.560±0.018  |     | 0.537±0.018     |
| TUEV        |               | 0.623±0.011 |     | 0.592±0.010  |     | 0.577±0.034     |
| PhysioNetMI |               | 0.583±0.009 |     | 0.586±0.009  |     | 0.559±0.007     |
| Avg.        |               | 0.596       |     | 0.579        |     | 0.558           |
TheGEGLU+RMSNormcombinationachievesthebestaverageperformance(0.596),outperforming
the others on BCIC-IV-2a and TUEV. GELU + RMSNorm performs similarly but only leads on
PhysioNetMI. In contrast, GEGLU + LayerNorm consistently underperforms, highlighting the
effectivenessofRMSNormoverLayerNormandthebenefitsofgatedactivationslikeGEGLUinthis
context.
E Additionalresults
Thissectionpresentssupplementaryexperimentsthatfurthersupportthemainresults,focusingon
few-shotperformanceandevaluationunderreduced-electrodeconfigurations.
E.1 Sparsesetups
Table 21: Performance of REVE-Base under sparse input configurations. Balanced accuracy is
reportedforPhysionetMI(Left–Right)andimaginedspeechtasksasthenumberofEEGchannelsis
progressivelyreduced.
|     |     | Channels | PhysionetMIL-R |     | Speech      |     |
| --- | --- | -------- | -------------- | --- | ----------- | --- |
|     |     | 64       | 0.824±0.008    |     | 0.565±0.016 |     |
|     |     | 32       | 0.808±0.007    |     | 0.490±0.094 |     |
|     |     | 16       | 0.787±0.008    |     | 0.469±0.014 |     |
|     |     | 8        | 0.781±0.006    |     | 0.294±0.063 |     |
|     |     | 4        | 0.728±0.009    |     | 0.258±0.019 |     |
|     |     | 2        | 0.700±0.025    |     | 0.228±0.006 |     |
|     |     | 1        | 0.660±0.019    |     | 0.209±0.008 |     |
Table21reportsREVE-Base’sperformanceunderincreasinglysparseinputconfigurations. Onthe
PhysionetMIL-Rtask,accuracydegradesgracefullyfrom0.824with64channelsto0.660with
asinglechannel,demonstratingrobustnesstoreducedspatialcoverage. Incontrast,theimagined
speechtaskismoresensitivetochannelsparsity,withperformancedroppingfrom0.565to0.258
withfourchannelsand0.209withone,closetorandomchance. Theseresultsconfirmthatwhile
REVEgeneralizeswellunderlimitedinput,tasksrequiringbroadspatialinformationremainmore
challenging.
E.2 Few-shotexperiments
We conducted few-shot (FS) experiments to simulate realistic BCI usage scenarios. Tasks were
constructedfromtheBCIIV-2adatasetusingtwomotorimageryclasses(Left–Right). Foreach
subject, multiple inductive FS runs were performed. In each run, N labeled samples per class
(“shots”)wererandomlyselectedwithinasessionfortraining,whiletheremainingsamplesfrom
bothsessionswereusedforevaluation.
Classification was done using a Nearest Class Mean (NCM) classifier. Each configuration was
repeated20timespersubject,andwereporttheaveragebalancedaccuracyacrosssubjectsandruns.
WeevaluatedtwoconfigurationsofREVE-Base:
28

• REVE-Base (PT): directly after self-supervised pretraining, with no further supervised
adaptation.
• REVE-Base (XFT): after cross-dataset fine-tuning on multiple labeled Left–Right MI
datasets ((Schirrmeister et al., 2017), (Cho et al., 2017), (Goldberger et al., 2000), (Lee
etal.,2019),(Yietal.,2014)). REVE’s4Dpositionalencodingenablesjointtrainingacross
diverseelectrodeconfigurationswithoutrequiringchannelalignmentorselection.
Table22: Few-shotperformanceofREVE-BaseonBCIIV-2adataset
| N-shots | 1   | 2   | 5   | 10  | 20  |
| ------- | --- | --- | --- | --- | --- |
REVE-Base(PT) 0.588±1.45 0.601±0.001 0.652±0.013 0.688±0.010 0.723±0.010
REVE-Base(XFT) 0.605±1.12 0.645±0.009 0.705±0.009 0.768±0.009 0.817±0.004
Table22showsthatREVE-Baseachievescompetitiveaccuracyevenwithoutsupervisedadaptation,
demonstratingthatitspretrainedembeddingscanbeeffectivelyleveragedfordownstreamBCItasks.
Aftercross-datasetfine-tuning,performanceimprovesconsistentlyacrossallshotcounts,withgains
reaching+10%at20shots. ThisindicatesthatREVEtransferswellacrosssubjectsanddatasets,
whilebenefitingfromminimalsupervisedadaptation. SuchgeneralizationisuncommonamongBCI
embeddingmodels,whichtypicallyrequiretaskorsubject-specificretraining.
F Experimentdetails
F.1 Computeresources
Weincludedetailsaboutthecomputenodesthatwereusedforpretraining.
| • ComputeType:        | GPU-acceleratednodes   |     |     |     |     |
| --------------------- | ---------------------- | --- | --- | --- | --- |
| • GPUModel:           | NVIDIAA100             |     |     |     |     |
| • CPUModel:           | IntelCascadeLakeSP6248 |     |     |     |     |
| • CPUCoresperNode:    | 40cores                |     |     |     |     |
| • TotalMemoryperNode: | 192GB                  |     |     |     |     |
• Storage: Accesstoasharedfull-flashparallelfilesystembasedonIBMSpectrumScale
| • JobScheduler: | Slurm |     |     |     |     |
| --------------- | ----- | --- | --- | --- | --- |
Wealsoestimatethenumberoffloating-pointoperations(FLOPs)requiredtotraintheREVE-Base
model,followingtheformulationfromChowdheryetal.(2023):
D·(6N +12LHQT)
|     | τ   | =   |     |     |     |
| --- | --- | --- | --- | --- | --- |
P ·η
whereτ denotesthetrainingtime(inseconds),D =60k×3600×1.1×68×17isthetotalnumber
of tokens seen during pretraining (corresponding to 60k hours of EEG, an overlap coefficient of
1.1,68averagechannels,and17epochs),N = 72Misthenumberofmodelparameters,L = 23
the number of encoder-decoder layers, H = 8 the number of attention heads, Q = 64 the head
dimension,andT =68×11theaveragenumberoftokenspersequence(channels×patches).
ThepeakthroughputisP =312TFLOPsathalfprecision,achievableonA100GPUs,andthemodel
| FLOPsutilizationissettoη | =0.5(50%). |     |     |     |     |
| ------------------------ | ---------- | --- | --- | --- | --- |
Thisconfigurationyieldsanestimated260A100GPUhoursforasinglepretrainingrun. Theformula
canbedirectlyadaptedforothermodelsizesorhardwareconfigurations.
F.2 UseofExistingAssets
We used Python (Python Software Foundation License), and some associated libraries for the
implementation:
29

1. PyTorch(BSD-3License)
2. NumPy(NumPylicense)
3. scikit-learn(BSDlicense)
4. Pandas(BSD3-ClauseLicense)
5. HuggingFace’sAccelerate(ApacheLicense2.0)
30

NeurIPSPaperChecklist
1. Claims
Question: Dothemainclaimsmadeintheabstractandintroductionaccuratelyreflectthe
paper’scontributionsandscope?
Answer: [Yes]
Justification: The claims in the abstract and introduction accurately reflect the paper’s
contributions. TheintroductionclearlystatesthegoalsofREVE:buildingafoundation
model for EEG that generalizes across datasets, durations, and electrode configurations.
Theseclaimsaresupportedby:
• Anovel4Dpositionalencoding(Section2.2),validatedbytransfertounseensetups.
• Pretrainingon92datasets(Section3.1),thelargestEEGcorpustodate.
• Extensiveevaluationsacross10downstreamtasks,showingconsistentgainsinfull
fine-tuningandlinearprobing(Section4,Tables2–16).
Guidelines:
• The answer NA means that the abstract and introduction do not include the claims
madeinthepaper.
• Theabstractand/orintroductionshouldclearlystatetheclaimsmade,includingthe
contributionsmadeinthepaperandimportantassumptionsandlimitations. ANoor
NAanswertothisquestionwillnotbeperceivedwellbythereviewers.
• Theclaimsmadeshouldmatchtheoreticalandexperimentalresults,andreflecthow
muchtheresultscanbeexpectedtogeneralizetoothersettings.
• Itisfinetoincludeaspirationalgoalsasmotivationaslongasitisclearthatthesegoals
arenotattainedbythepaper.
2. Limitations
Question: Doesthepaperdiscussthelimitationsoftheworkperformedbytheauthors?
Answer: [Yes]
Justification: ThepaperincludesadedicatedLimitationsandFutureWorksectionoutlining
keyconstraintsofREVE,suchasfixedinputdurationrequirements,positionalencoding
limitations,andthelimiteddatasetcurationandselection. Wealsoacknowledgethatwhile
scalingeffectsareobserved,identifyingprecisescalinglawsremainsfuturework. These
pointsreflectaclearunderstandingofthemethod’scurrentboundariesandopportunitiesfor
improvement.
Guidelines:
• TheanswerNAmeansthatthepaperhasnolimitationwhiletheanswerNomeansthat
thepaperhaslimitations,butthosearenotdiscussedinthepaper.
• Theauthorsareencouragedtocreateaseparate"Limitations"sectionintheirpaper.
• Thepapershouldpointoutanystrongassumptionsandhowrobusttheresultsareto
violationsoftheseassumptions(e.g.,independenceassumptions,noiselesssettings,
modelwell-specification,asymptoticapproximationsonlyholdinglocally).Theauthors
shouldreflectonhowtheseassumptionsmightbeviolatedinpracticeandwhatthe
implicationswouldbe.
• Theauthorsshouldreflectonthescopeoftheclaimsmade,e.g.,iftheapproachwas
onlytestedonafewdatasetsorwithafewruns. Ingeneral,empiricalresultsoften
dependonimplicitassumptions,whichshouldbearticulated.
• Theauthorsshouldreflectonthefactorsthatinfluencetheperformanceoftheapproach.
Forexample,afacialrecognitionalgorithmmayperformpoorlywhenimageresolution
isloworimagesaretakeninlowlighting. Oraspeech-to-textsystemmightnotbe
usedreliablytoprovideclosedcaptionsforonlinelecturesbecauseitfailstohandle
technicaljargon.
• Theauthorsshoulddiscussthecomputationalefficiencyoftheproposedalgorithms
andhowtheyscalewithdatasetsize.
• If applicable, the authors should discuss possible limitations of their approach to
addressproblemsofprivacyandfairness.
31

• Whiletheauthorsmightfearthatcompletehonestyaboutlimitationsmightbeusedby
reviewersasgroundsforrejection,aworseoutcomemightbethatreviewersdiscover
limitationsthataren’tacknowledgedinthepaper. Theauthorsshouldusetheirbest
judgmentandrecognizethatindividualactionsinfavoroftransparencyplayanimpor-
tantroleindevelopingnormsthatpreservetheintegrityofthecommunity. Reviewers
willbespecificallyinstructedtonotpenalizehonestyconcerninglimitations.
3. Theoryassumptionsandproofs
Question: Foreachtheoreticalresult,doesthepaperprovidethefullsetofassumptionsand
acomplete(andcorrect)proof?
Answer: [NA]
Justification: Thepaperdoesnotincludetheoreticalresults,asitisfocusedonapplications
ofafoundationmodelforEEGanddoesnotdelveintotheoreticalproofsorassumptions.
Guidelines:
• TheanswerNAmeansthatthepaperdoesnotincludetheoreticalresults.
• Allthetheorems, formulas, andproofsinthepapershouldbenumberedandcross-
referenced.
• Allassumptionsshouldbeclearlystatedorreferencedinthestatementofanytheorems.
• Theproofscaneitherappearinthemainpaperorthesupplementalmaterial, butif
theyappearinthesupplementalmaterial,theauthorsareencouragedtoprovideashort
proofsketchtoprovideintuition.
• Inversely,anyinformalproofprovidedinthecoreofthepapershouldbecomplemented
byformalproofsprovidedinappendixorsupplementalmaterial.
• TheoremsandLemmasthattheproofreliesuponshouldbeproperlyreferenced.
4. Experimentalresultreproducibility
Question: Doesthepaperfullydisclosealltheinformationneededtoreproducethemainex-
perimentalresultsofthepapertotheextentthatitaffectsthemainclaimsand/orconclusions
ofthepaper(regardlessofwhetherthecodeanddataareprovidedornot)?
Answer: [Yes]
Justification: Thepaperprovidesacomprehensivedescriptionofthemodelarchitecture,the
trainingdatasources,andtheroutinesforbothpretrainingandfine-tuning. Thehyperparam-
etersofthemodelarereported.
Guidelines:
• TheanswerNAmeansthatthepaperdoesnotincludeexperiments.
• Ifthepaperincludesexperiments,aNoanswertothisquestionwillnotbeperceived
well by the reviewers: Making the paper reproducible is important, regardless of
whetherthecodeanddataareprovidedornot.
• Ifthecontributionisadatasetand/ormodel,theauthorsshoulddescribethestepstaken
tomaketheirresultsreproducibleorverifiable.
• Dependingonthecontribution,reproducibilitycanbeaccomplishedinvariousways.
Forexample,ifthecontributionisanovelarchitecture,describingthearchitecturefully
mightsuffice,orifthecontributionisaspecificmodelandempiricalevaluation,itmay
benecessarytoeithermakeitpossibleforotherstoreplicatethemodelwiththesame
dataset,orprovideaccesstothemodel. Ingeneral. releasingcodeanddataisoften
onegoodwaytoaccomplishthis,butreproducibilitycanalsobeprovidedviadetailed
instructionsforhowtoreplicatetheresults,accesstoahostedmodel(e.g.,inthecase
ofalargelanguagemodel),releasingofamodelcheckpoint,orothermeansthatare
appropriatetotheresearchperformed.
• WhileNeurIPSdoesnotrequirereleasingcode,theconferencedoesrequireallsubmis-
sionstoprovidesomereasonableavenueforreproducibility,whichmaydependonthe
natureofthecontribution. Forexample
(a) Ifthecontributionisprimarilyanewalgorithm,thepapershouldmakeitclearhow
toreproducethatalgorithm.
(b) Ifthecontributionisprimarilyanewmodelarchitecture,thepapershoulddescribe
thearchitectureclearlyandfully.
32

(c) Ifthecontributionisanewmodel(e.g.,alargelanguagemodel),thenthereshould
eitherbeawaytoaccessthismodelforreproducingtheresultsorawaytoreproduce
themodel(e.g.,withanopen-sourcedatasetorinstructionsforhowtoconstruct
thedataset).
(d) We recognize that reproducibility may be tricky in some cases, in which case
authorsarewelcometodescribetheparticularwaytheyprovideforreproducibility.
Inthecaseofclosed-sourcemodels,itmaybethataccesstothemodelislimitedin
someway(e.g.,toregisteredusers),butitshouldbepossibleforotherresearchers
tohavesomepathtoreproducingorverifyingtheresults.
5. Openaccesstodataandcode
Question: Doesthepaperprovideopenaccesstothedataandcode,withsufficientinstruc-
tionstofaithfullyreproducethemainexperimentalresults,asdescribedinsupplemental
material?
Answer: [Yes]
Justification: The authors provide full access to the code required for reproducing the
experiments. Detailed instructions are included, outlining the necessary commands and
environmentsettingstofaithfullyreproducetheresults.
Guidelines:
• TheanswerNAmeansthatpaperdoesnotincludeexperimentsrequiringcode.
• Please see the NeurIPS code and data submission guidelines (https://nips.cc/
public/guides/CodeSubmissionPolicy)formoredetails.
• Whileweencouragethereleaseofcodeanddata,weunderstandthatthismightnotbe
possible,so“No”isanacceptableanswer. Paperscannotberejectedsimplyfornot
includingcode,unlessthisiscentraltothecontribution(e.g.,foranewopen-source
benchmark).
• Theinstructionsshouldcontaintheexactcommandandenvironmentneededtorunto
reproducetheresults. SeetheNeurIPScodeanddatasubmissionguidelines(https:
//nips.cc/public/guides/CodeSubmissionPolicy)formoredetails.
• Theauthorsshouldprovideinstructionsondataaccessandpreparation,includinghow
toaccesstherawdata,preprocesseddata,intermediatedata,andgenerateddata,etc.
• Theauthorsshouldprovidescriptstoreproduceallexperimentalresultsforthenew
proposedmethodandbaselines. Ifonlyasubsetofexperimentsarereproducible,they
shouldstatewhichonesareomittedfromthescriptandwhy.
• Atsubmissiontime, topreserveanonymity, theauthorsshouldreleaseanonymized
versions(ifapplicable).
• Providingasmuchinformationaspossibleinsupplementalmaterial(appendedtothe
paper)isrecommended,butincludingURLstodataandcodeispermitted.
6. Experimentalsetting/details
Question: Doesthepaperspecifyallthetrainingandtestdetails(e.g.,datasplits,hyper-
parameters, how they were chosen, type of optimizer, etc.) necessary to understand the
results?
Answer: [Yes]
Justification: Thepaperprovidesallnecessarydetailsregardingtheexperimentalsetting,
includingthedatasplits,thehyperparameters,andthetypeofoptimizerused. Thesedetails
areprovidedinthemaintext,withfurtherspecificsavailableinthesupplementalmaterial
andthereleasedcode.
Guidelines:
• TheanswerNAmeansthatthepaperdoesnotincludeexperiments.
• Theexperimentalsettingshouldbepresentedinthecoreofthepapertoalevelofdetail
thatisnecessarytoappreciatetheresultsandmakesenseofthem.
• Thefulldetailscanbeprovidedeitherwiththecode,inappendix,orassupplemental
material.
7. Experimentstatisticalsignificance
33

Question:Doesthepaperreporterrorbarssuitablyandcorrectlydefinedorotherappropriate
informationaboutthestatisticalsignificanceoftheexperiments?
Answer: [Yes]
Justification: Thepaperreportsbalancedaccuracyastheprimarymetric,alongwiththe
meanandstandarddeviation. Thesemetricsareusedtomatchthebaselines,providinga
measureofvariabilityintheresults. Thisresultsina68%CIundernormalityassumption.
Guidelines:
• TheanswerNAmeansthatthepaperdoesnotincludeexperiments.
• Theauthorsshouldanswer"Yes"iftheresultsareaccompaniedbyerrorbars,confi-
denceintervals,orstatisticalsignificancetests,atleastfortheexperimentsthatsupport
themainclaimsofthepaper.
• Thefactorsofvariabilitythattheerrorbarsarecapturingshouldbeclearlystated(for
example,train/testsplit,initialization,randomdrawingofsomeparameter,oroverall
runwithgivenexperimentalconditions).
• Themethodforcalculatingtheerrorbarsshouldbeexplained(closedformformula,
calltoalibraryfunction,bootstrap,etc.)
• Theassumptionsmadeshouldbegiven(e.g.,Normallydistributederrors).
• Itshouldbeclearwhethertheerrorbaristhestandarddeviationorthestandarderror
ofthemean.
• It is OK to report 1-sigma error bars, but one should state it. The authors should
preferablyreporta2-sigmaerrorbarthanstatethattheyhavea96%CI,ifthehypothesis
ofNormalityoferrorsisnotverified.
• Forasymmetricdistributions,theauthorsshouldbecarefulnottoshowintablesor
figuressymmetricerrorbarsthatwouldyieldresultsthatareoutofrange(e.g. negative
errorrates).
• Iferrorbarsarereportedintablesorplots,Theauthorsshouldexplaininthetexthow
theywerecalculatedandreferencethecorrespondingfiguresortablesinthetext.
8. Experimentscomputeresources
Question: Foreachexperiment,doesthepaperprovidesufficientinformationonthecom-
puterresources(typeofcomputeworkers,memory,timeofexecution)neededtoreproduce
theexperiments?
Answer: [Yes]
Justification: The paper discusses the use of NVIDIA A100 GPUs while estimating the
amountofGPUhoursusedforeachexperiment.
Guidelines:
• TheanswerNAmeansthatthepaperdoesnotincludeexperiments.
• ThepapershouldindicatethetypeofcomputeworkersCPUorGPU,internalcluster,
orcloudprovider,includingrelevantmemoryandstorage.
• Thepapershouldprovidetheamountofcomputerequiredforeachoftheindividual
experimentalrunsaswellasestimatethetotalcompute.
• Thepapershoulddisclosewhetherthefullresearchprojectrequiredmorecompute
thantheexperimentsreportedinthepaper(e.g.,preliminaryorfailedexperimentsthat
didn’tmakeitintothepaper).
9. Codeofethics
Question: Doestheresearchconductedinthepaperconform, ineveryrespect, withthe
NeurIPSCodeofEthicshttps://neurips.cc/public/EthicsGuidelines?
Answer: [Yes]
Justification: The research aligns with the NeurIPS Code of Ethics by ensuring respon-
sible and ethical practices in all aspects of the research process, as discussed in ethical
considerationssection.
Guidelines:
• TheanswerNAmeansthattheauthorshavenotreviewedtheNeurIPSCodeofEthics.
34

• IftheauthorsanswerNo,theyshouldexplainthespecialcircumstancesthatrequirea
deviationfromtheCodeofEthics.
• Theauthorsshouldmakesuretopreserveanonymity(e.g.,ifthereisaspecialconsid-
erationduetolawsorregulationsintheirjurisdiction).
10. Broaderimpacts
Question: Does the paper discuss both potential positive societal impacts and negative
societalimpactsoftheworkperformed?
Answer: [Yes]
Justification: Thepaperdiscussesboththepotentialpositiveandnegativesocietalimpacts
ofthework. Onthepositiveside,themodelcangreatlybenefithealthcarebyimproving
theaccuracyandefficiencyofEEG-basedapplicationssuchasbrain-computerinterfaces
anddiagnostictools. Onthenegativeside,themodel’sdecoder,whichcouldpotentially
reconstructrawEEGdata,posesaprivacyrisk. Tomitigatethis,thedecoderisnotbeing
released,thusreducingthepotentialformisuseingeneratingsensitiveorprivateinformation.
Thepaperemphasizestheresponsibleandethicaluseofthetechnology,withawarenessof
itspotentialrisks.
Guidelines:
• TheanswerNAmeansthatthereisnosocietalimpactoftheworkperformed.
• IftheauthorsanswerNAorNo,theyshouldexplainwhytheirworkhasnosocietal
impactorwhythepaperdoesnotaddresssocietalimpact.
• Examplesofnegativesocietalimpactsincludepotentialmaliciousorunintendeduses
(e.g.,disinformation,generatingfakeprofiles,surveillance),fairnessconsiderations
(e.g.,deploymentoftechnologiesthatcouldmakedecisionsthatunfairlyimpactspecific
groups),privacyconsiderations,andsecurityconsiderations.
• Theconferenceexpectsthatmanypaperswillbefoundationalresearchandnottied
toparticularapplications,letalonedeployments. However,ifthereisadirectpathto
anynegativeapplications,theauthorsshouldpointitout. Forexample,itislegitimate
topointoutthatanimprovementinthequalityofgenerativemodelscouldbeusedto
generatedeepfakesfordisinformation. Ontheotherhand,itisnotneededtopointout
thatagenericalgorithmforoptimizingneuralnetworkscouldenablepeopletotrain
modelsthatgenerateDeepfakesfaster.
• Theauthorsshouldconsiderpossibleharmsthatcouldarisewhenthetechnologyis
being used as intended and functioning correctly, harms that could arise when the
technologyisbeingusedasintendedbutgivesincorrectresults,andharmsfollowing
from(intentionalorunintentional)misuseofthetechnology.
• Iftherearenegativesocietalimpacts,theauthorscouldalsodiscusspossiblemitigation
strategies (e.g., gated release of models, providing defenses in addition to attacks,
mechanismsformonitoringmisuse,mechanismstomonitorhowasystemlearnsfrom
feedbackovertime,improvingtheefficiencyandaccessibilityofML).
11. Safeguards
Question: Doesthepaperdescribesafeguardsthathavebeenputinplaceforresponsible
releaseofdataormodelsthathaveahighriskformisuse(e.g.,pretrainedlanguagemodels,
imagegenerators,orscrapeddatasets)?
Answer: [Yes]
Justification: To mitigate privacy risks, the decoder of the MAE model, which could
reconstructrawEEGdata,isnotbeingreleased. Thissafeguardreducesthepotentialfor
misusewhileallowingresponsibleaccesstothemodel’sembeddings.
Guidelines:
• TheanswerNAmeansthatthepaperposesnosuchrisks.
• Releasedmodelsthathaveahighriskformisuseordual-useshouldbereleasedwith
necessarysafeguardstoallowforcontrolleduseofthemodel,forexamplebyrequiring
thatusersadheretousageguidelinesorrestrictionstoaccessthemodelorimplementing
safetyfilters.
35

• DatasetsthathavebeenscrapedfromtheInternetcouldposesafetyrisks. Theauthors
shoulddescribehowtheyavoidedreleasingunsafeimages.
• Werecognizethatprovidingeffectivesafeguardsischallenging,andmanypapersdo
notrequirethis,butweencourageauthorstotakethisintoaccountandmakeabest
faitheffort.
12. Licensesforexistingassets
Question: Arethecreatorsororiginalownersofassets(e.g.,code,data,models),usedin
thepaper,properlycreditedandarethelicenseandtermsofuseexplicitlymentionedand
properlyrespected?
Answer: [Yes]
Justification: Seethesectionaboutexistingassetsintheappendix.
Guidelines:
• TheanswerNAmeansthatthepaperdoesnotuseexistingassets.
• Theauthorsshouldcitetheoriginalpaperthatproducedthecodepackageordataset.
• Theauthorsshouldstatewhichversionoftheassetisusedand,ifpossible,includea
URL.
• Thenameofthelicense(e.g.,CC-BY4.0)shouldbeincludedforeachasset.
• Forscrapeddatafromaparticularsource(e.g.,website),thecopyrightandtermsof
serviceofthatsourceshouldbeprovided.
• If assets are released, the license, copyright information, and terms of use in the
packageshouldbeprovided. Forpopulardatasets,paperswithcode.com/datasets
hascuratedlicensesforsomedatasets. Theirlicensingguidecanhelpdeterminethe
licenseofadataset.
• Forexistingdatasetsthatarere-packaged,boththeoriginallicenseandthelicenseof
thederivedasset(ifithaschanged)shouldbeprovided.
• Ifthisinformationisnotavailableonline,theauthorsareencouragedtoreachoutto
theasset’screators.
13. Newassets
Question:Arenewassetsintroducedinthepaperwelldocumentedandisthedocumentation
providedalongsidetheassets?
Answer: [Yes]
Justification: Ananonymizedrepositorycontainingthecodeforthemodel,itspretraining
andfine-tuningisreleased.
Guidelines:
• TheanswerNAmeansthatthepaperdoesnotreleasenewassets.
• Researchersshouldcommunicatethedetailsofthedataset/code/modelaspartoftheir
submissions via structured templates. This includes details about training, license,
limitations,etc.
• Thepapershoulddiscusswhetherandhowconsentwasobtainedfrompeoplewhose
assetisused.
• Atsubmissiontime,remembertoanonymizeyourassets(ifapplicable). Youcaneither
createananonymizedURLorincludeananonymizedzipfile.
14. Crowdsourcingandresearchwithhumansubjects
Question: Forcrowdsourcingexperimentsandresearchwithhumansubjects,doesthepaper
includethefulltextofinstructionsgiventoparticipantsandscreenshots,ifapplicable,as
wellasdetailsaboutcompensation(ifany)?
Answer: [NA]
Justification: Thepaperdoesnotinvolvenewcrowdsourcingexperimentsordirectresearch
withhumansubjects.Weusepre-existingEEGdatasets,andassuch,therearenoinstructions
orcompensationdetailstoreport. Thedatasetsusedhavebeenethicallysourced,withthe
originalcollectionprotocolsensuringparticipantconsentandprivacyinlinewithethical
guidelines.
36

Guidelines:
• TheanswerNAmeansthatthepaperdoesnotinvolvecrowdsourcingnorresearchwith
humansubjects.
• Includingthisinformationinthesupplementalmaterialisfine,butifthemaincontribu-
tionofthepaperinvolveshumansubjects,thenasmuchdetailaspossibleshouldbe
includedinthemainpaper.
• AccordingtotheNeurIPSCodeofEthics,workersinvolvedindatacollection,curation,
orotherlaborshouldbepaidatleasttheminimumwageinthecountryofthedata
collector.
15. Institutional review board (IRB) approvals or equivalent for research with human
subjects
Question: Doesthepaperdescribepotentialrisksincurredbystudyparticipants,whether
suchrisksweredisclosedtothesubjects,andwhetherInstitutionalReviewBoard(IRB)
approvals(oranequivalentapproval/reviewbasedontherequirementsofyourcountryor
institution)wereobtained?
Answer: [NA]
Justification: The paper does not involve new research with human subjects, as it relies
onpre-existingEEGdatasets. Therefore,nopotentialriskstoparticipantswereincurred,
andnonewIRBapprovalsorequivalentreviewswererequired. Thedatasetsusedhave
beenethicallysourced,withtheoriginalstudiesobtainingnecessaryparticipantconsentand
privacyprotections.
Guidelines:
• TheanswerNAmeansthatthepaperdoesnotinvolvecrowdsourcingnorresearchwith
humansubjects.
• Dependingonthecountryinwhichresearchisconducted,IRBapproval(orequivalent)
mayberequiredforanyhumansubjectsresearch. IfyouobtainedIRBapproval,you
shouldclearlystatethisinthepaper.
• Werecognizethattheproceduresforthismayvarysignificantlybetweeninstitutions
andlocations,andweexpectauthorstoadheretotheNeurIPSCodeofEthicsandthe
guidelinesfortheirinstitution.
• Forinitialsubmissions,donotincludeanyinformationthatwouldbreakanonymity(if
applicable),suchastheinstitutionconductingthereview.
16. DeclarationofLLMusage
Question: Does the paper describe the usage of LLMs if it is an important, original, or
non-standardcomponentofthecoremethodsinthisresearch? NotethatiftheLLMisused
onlyforwriting,editing,orformattingpurposesanddoesnotimpactthecoremethodology,
scientificrigorousness,ororiginalityoftheresearch,declarationisnotrequired.
Answer: [NA]
Justification: [NA]
Guidelines:
• The answer NA means that the core method development in this research does not
involveLLMsasanyimportant,original,ornon-standardcomponents.
• PleaserefertoourLLMpolicy(https://neurips.cc/Conferences/2025/LLM)
forwhatshouldorshouldnotbedescribed.
37