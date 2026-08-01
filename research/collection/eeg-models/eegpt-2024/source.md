| EEGPT: |                             | Pretrained         |                |     | Transformer |                             | for                | Universal |     | and |
| ------ | --------------------------- | ------------------ | -------------- | --- | ----------- | --------------------------- | ------------------ | --------- | --- | --- |
|        | Reliable                    |                    | Representation |     |             |                             | of EEG             | Signals   |     |     |
|        |                             | GuagnyuWang        |                |     |             |                             | WenchaoLiu         |           |     |     |
|        |                             | FacultyofComputing |                |     |             |                             | FacultyofComputing |           |     |     |
|        | HarbinInstituteofTechnology |                    |                |     |             | HarbinInstituteofTechnology |                    |           |     |     |
|        | wangguangyu@stu.hit.edu.cn  |                    |                |     |             | 23b903096@stu.hit.edu.cn    |                    |           |     |     |
|        |                             |                    | YuhongHe       |     |             |                             |                    | CongXu    |     |     |
|        |                             | FacultyofComputing |                |     |             |                             | FacultyofComputing |           |     |     |
|        | HarbinInstituteofTechnology |                    |                |     |             | HarbinInstituteofTechnology |                    |           |     |     |
|        | 19S003002@stu.hit.edu.cn    |                    |                |     |             |                             | congxu@hit.edu.cn  |           |     |     |
HaifengLi∗
LinMa
|     |                             | FacultyofComputing  |     |     |     |                             | FacultyofComputing   |     |     |     |
| --- | --------------------------- | ------------------- | --- | --- | --- | --------------------------- | -------------------- | --- | --- | --- |
|     | HarbinInstituteofTechnology |                     |     |     |     | HarbinInstituteofTechnology |                      |     |     |     |
|     |                             | malin_li@hit.edu.cn |     |     |     |                             | lihaifeng@hit.edu.cn |     |     |     |
Abstract
Electroencephalography(EEG)iscrucialforrecordingbrainactivity,withapplica-
tionsinmedicine,neuroscience,andbrain-computerinterfaces(BCI).However,
|     | challenges                                                | such    | as low     | signal-to-noise | ratio    | (SNR),                     | high | inter-subject |            | variabil- |
| --- | --------------------------------------------------------- | ------- | ---------- | --------------- | -------- | -------------------------- | ---- | ------------- | ---------- | --------- |
|     | ity, and                                                  | channel | mismatch   | complicate      | the      | extraction                 | of   | robust,       | universal  | EEG       |
|     | representations.                                          |         | We propose |                 | EEGPT, a | novel 10-million-parameter |      |               | pretrained |           |
|     | transformermodeldesignedforuniversalEEGfeatureextraction. |         |            |                 |          |                            |      |               | InEEGPT,a  |           |
mask-baseddualself-supervisedlearningmethodforefficientfeatureextraction
|     | is designed.                                           |     | Compared | to other | mask-based | self-supervised |     | learning         | methods, |     |
| --- | ------------------------------------------------------ | --- | -------- | -------- | ---------- | --------------- | --- | ---------------- | -------- | --- |
|     | EEGPTintroducesspatio-temporalrepresentationalignment. |     |          |          |            |                 |     | Thisinvolvescon- |          |     |
structingaself-supervisedtaskbasedonEEGrepresentationsthatpossesshigh
|     | SNR | and rich | semantic | information, | rather | than | on raw | signals. | Consequently, |     |
| --- | --- | -------- | -------- | ------------ | ------ | ---- | ------ | -------- | ------------- | --- |
thisapproachmitigatestheissueofpoorfeaturequalitytypicallyextractedfrom
|     | lowSNRsignals.                                                    |             | Additionally,EEGPT’shierarchicalstructureprocessesspatial |              |                                      |     |               |                 |          |           |
| --- | ----------------------------------------------------------------- | ----------- | --------------------------------------------------------- | ------------ | ------------------------------------ | --- | ------------- | --------------- | -------- | --------- |
|     | andtemporalinformationseparately,                                 |             |                                                           |              | reducingcomputationalcomplexitywhile |     |               |                 |          |           |
|     | increasing                                                        | flexibility | and                                                       | adaptability | for                                  | BCI | applications. | By              | training | on a      |
|     | largemixedmulti-taskEEGdataset,wefullyexploitEEGPT’scapabilities. |             |                                                           |              |                                      |     |               |                 |          | The       |
|     | experiment                                                        |             | validates the                                             | efficacy     | and scalability                      |     | of EEGPT,     | achieving       |          | state-of- |
|     | the-art                                                           | performance | on                                                        | a range      | of downstream                        |     | tasks with    | linear-probing. |          | Our       |
researchadvancesEEGrepresentationlearning,offeringinnovativesolutionsfor
|     | bio-signalprocessingandAIapplications. |     |     |     |     | Thecodeforthispaperisavailableat: |     |     |     |     |
| --- | -------------------------------------- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- |
https://github.com/BINE022/EEGPT.
1 Introduction
Electroencephalography(EEG)dynamicallyreflectsthebrain’sfunctionalstatebyrecordingelectrical
signalsfromthecerebralcortex[1]. EEGisessentialforstudyingbrainactivityandispivotalin
∗Correspondingauthor
38thConferenceonNeuralInformationProcessingSystems(NeurIPS2024).

brain-computerinterface(BCI)applicationsduetoitsnon-invasiveandportablenature[2]. Despite
itspotential,EEG-basedmethodsfacepracticalchallengesduetolowsignal-to-noiseratio(SNR)
[3], high inter-subject variability, and significant task-dependent variations in EEG signals [4].
Self-supervisedlearning,asdescribedbyYannLeCuninhisAAAI2020keynote[5],hasshown
advantagesinnaturallanguageprocessing(NLP)[6],computervision(CV)[7,8],andspeechanalysis
[9]. Moreandmorestate-of-the-art(SOTA)modelsarepretrainedbyself-supervisedlearningon
largedatasetsandfine-tunedforspecificapplications,effectivelyreducingtheneedforextensive
labeleddata. Maskedautoencoders,atypeofself-supervisedlearningmethod,havebeensuccessful
inNLP[6]andCV[8]byrecoveringmaskedpatchesbasedoncontext.
RecentadvancesinEEGanalysisusingself-supervisedlearningtechniqueshaveshownpromising
results.InFalcketal.[10],aframeworkforlearningEEGrepresentationsthroughcontrastivelearning
wasproposed. ThisframeworkextendstheSimCLRframeworktotimeseriesdata,trainingachannel
featureextractor. Themodelachievedanaccuracyof85.12%ontheSleep-EDFdataset[11]butwas
onlytrainedonEEGdatacollectedduring20-secondtasks,makingitunsuitableforshortertasks
suchasmotorimagery. BENDR[12]appliedself-supervisedlearningbasedonmaskedautoencoders
and contrastive learning to EEG data. This approach addresses the challenges of multi-task and
multi-paradigm EEG data characterization, enhancing the model’s universality. BENDR uses a
convolutionalencodertoextractfeaturesfromlocaltimewindows,maskssomefeatures,andthen
atransformerdecoderpredictstheinformationinthemaskedparts. EEG2VEC[13]introduceda
self-supervisedmodelthatlearnsEEGrepresentationsbasedoncontrastivelossandreconstruction
loss. Thepretrainedmodelisusedasafeatureextractorfordownstreamtasks. BothEEG2VECand
BENDRutilizeconvolutionalneuralnetworkandtransformernetworkstolearnlocalandglobal
features. EEG2VECwasvalidatedinEEGmatch-mismatchandEEGregressiontasksoftheauditory
EEG challenge [14]. The Biosignal Transformer (BIOT) [15] model addresses the challenges of
cross-datalearningwithmismatchedchannels,variablelengths,andmissingvaluesinbiosignals
suchasEEG,ECG,andhumanactivitysensorysignals. BIOTtokenizeseachchannelseparatelyinto
fixed-lengthsegmentscontaininglocalsignalfeaturesandthenre-arrangesthesegmentstoforma
long"sentence". IntheCHB-MITseizuredetectiontask[16],thepretrainedBIOTmodelsachieved
a4%improvement. TheLargeBrainModel(LaBraM)[17]addressesEEG-baseddeeplearning
modellimitationsbyenablingcross-datasetlearning. ItsegmentsEEGsignalsintochannelpatches
andusesvector-quantizedneuralspectrumpredictionfortraininganeuraltokenizer. Thistokenizer
encodesrawEEGpatchesintoneuralcodes,whichpretraintransformerstopredicttheoriginalneural
codesformaskedpatches. LaBraMoutperformedSOTAmethodsinabnormaldetection,eventtype
classification[18],emotionrecognition[19],andgaitprediction[20].
UniversalmodelshaveclearlymadeprogressinEEGdataanalysis. However,theextremelylow
SNR of EEG signals and the complexity of brain activities during tasks make it challenging to
learnabstractfeaturesusingmaskedautoencoders,whicharecommonlyusedinNLPandCV[12].
Additionally,theinconsistentsamplingratesofdifferentEEGacquisitiondevicesandvariationsin
electrodechannellocations[15]hindertheconvolutionalencoder’sabilitytodecouplethecorrelation
betweenelectrodechannelsandEEGsignals,resultinginrobustnessandscalabilityissues.
Toaddresstheseissues, weproposeadualself-supervisedEEGuniversalrepresentationmethod
basedonthespatio-temporalconsistencyofEEGsignals[21],introducingtheEEGPretrainedTrans-
former(EEGPT)forefficientfeatureextraction. Ourmethodincludesspatio-temporalrepresentation
alignmentandmask-basedreconstruction,enhancingrepresentationqualityandmodelrobustness.
OurmethodadoptsaBERT-stylemaskedrecoverytask[22](notautoregressivetask)objectivesfor
pretraining. Beyondtheoriginalwaveformrecovery,wealignthepredictedEEGsignalfeaturesof
themaskedpartswithfullEEGsignalfeatures. Additionally,alocalspatio-temporalembedding
methodimprovescompatibilityacrossdifferentEEGacquisitiondevices.
EEGPT,withover10millionparameters,ispretrainedonamixedmulti-taskEEGdataset,including
datafromPhysioMI[23],HGD[24],andM3CV[25]. ThispretrainingenablesEEGPTtoextract
universalrepresentationsforvarioustasks.Fordownstreamtasks,weemployalinear-probingmethod,
whichachievesSOTAperformancewhilealsoreducingcomputationalresourceconsumptionand
preventingoverfitting.OurexperimentsdemonstrateEEGPT’ssuperiorperformanceinmotorimagery
classification [26], event-related potential (ERP) detection [27], and sleep stage detection [28],
showcasingitscapabilitytoextracthigh-levelabstractfeaturesacrossspatio-temporaldimensions.
2

Contributionsofthispaper:
• ProposalofEEGPT,a10-million-parametermodelforEEGuniversalfeatureextraction,
leveragingamixeddatasettoenhanceperformancesacrosstasksandsubjects.
• Developmentofadualself-supervisedmethodforEEGsignals,combiningspatio-temporal
representation alignment and mask-based reconstruction, improving feature quality and
convergence.
• Design of a hierarchical structure for decoupled processing of spatial and temporal in-
formation, reducing computational complexity and enhancing model flexibility for BCI
applications.
• Implementationofalocalspatio-temporalembeddingmethod,increasingrobustnessand
compatibilityacrossdifferentEEGacquisitiondevices.
• Conductofcomprehensiveexperimentsondownstreamdatasets,demonstratingEEGPT
significantlyoutperformsexistingmodelsacrossmultipleEEGtasksandthatlargermodels
exhibitimprovedperformance.
2 Method
Background: AccordingtoKongandZhang[29],amaskedautoencoderlearnsfeaturesthrough
aformofdenoisingautoencoder: inputsignalsoccludedwithrandompatchmasksarefedintothe
encoder,andthedecoderpredictstheoriginalembeddingsofthemaskedpatches:
min E H(d (z),x⊙(1−M)), z =f (x⊙M) (1)
ϕ θ
θ,ϕx∼D
where "⊙" denotes element-wise product; M is the patch mask; f (·) and d (·) are the encoder
θ ϕ
anddecoder,respectively;zisthelearnedrepresentation;andH(·,·)isthesimilaritymeasurement.
Byminimizingthelossfunction,themodellearnstheoptimalrepresentationzoftheinputsignal.
However,inpractice,thereisnoexplicitrepresentationz (nosplitofencoderanddecoder)inthe
BERT-style model [22], and the model must be fine-tuned to locate effective representations. In
contrast,weaddaspatio-temporalrepresentationalignmentbranchtoexplicitlyrepresentz,which
changesEquation1toEquation2(dualself-supervisedmethod):
min E H(d (z),x⊙(1−M))+H(z,f (x)), z =f (x⊙M) (2)
ϕ θ θ
θ,ϕx∼D
Thismethodencouragestheencodedrepresentationstotakeonalargerextentofsemantics,similar
totheminimalsufficientrepresentationintheMulti-ViewEntropyBottleneck(MVEB)approach
[30],therebyimprovingtheencodingqualityandgeneralization[31].
EEGPretrainedTransformer(EEGPT):ThestructureoftheEEGPTmodelisshowninFigure1,
whichincludesoperationssuchaspatching,embedding,masking,encoder,predictorandreconstructor.
First,themodelchunkstheinputEEGsignalx∈RM×T (M channelsandT timepoints)intopatches
p ,andembedseachpatchasatokentoken bylocalspatio-temporalembedding(Section2.3),
i,j i,j
followedbysplittingintomaskedpartsMandunmaskedpartsM,respectively. Then,wepretain
themodelusingadualself-supervisedlearningmethod,includingspatio-temporalrepresentation
alignment(Section2.1)andmask-basedreconstruction(Section2.2). Finally, thelinear-probing
methodisusedindownstreamtasks(Section2.4).
2.1 Spatio-temporalRepresentationAlignment
Thespatio-temporalrepresentationalignmentmethodalignsthepredictedfeatureswiththemomen-
tumencoder’soutput,enhancingtheencoder’sabilitytoextractrobustfeaturesandensuringthatthe
encoder’soutputcontainshigh-qualityglobalfeatures. Weemploytheencoderandthepredictorto
decouplespatialandtemporalfeatures,significantlyreducingcomputationalcomplexity.
Encoder:Theencoderintegratesspatialinformationfrommaskedpatches. Equation3describeshow
theencoder(ENC)processesallmaskedtoken attimej asinputandproducesthecorresponding
i,j
outputfeatureenc :
j
(cid:32) (cid:33)
enc =ENC {token } (3)
j i,j
(i,j)∈M
3

𝑟𝑒𝑐𝑖,𝑗
ReconstructionLoss
Transformer
Reconstructed EEG
𝑞𝑖𝑗
| 𝑒𝑛𝑐1𝑝𝑟𝑒𝑑2𝑒𝑛𝑐3𝑒𝑛𝑐4𝑝𝑟𝑒𝑑5𝑒𝑛𝑐6 | Reconstructor |     |     |     |
| -------------------------- | ------------- | --- | --- | --- |
+ + + + + +
𝑝𝑜𝑠1𝑝𝑜𝑠2 𝑝𝑜𝑠3𝑝𝑜𝑠4𝑝𝑜𝑠5 𝑝𝑜𝑠6
| 𝑝𝑟𝑒𝑑1𝑝𝑟𝑒𝑑2𝑝𝑟𝑒𝑑3𝑝𝑟𝑒𝑑4𝑝𝑟𝑒𝑑5𝑝𝑟𝑒𝑑6 | +      |     |     |     |
| ------------------------------ | ------ | --- | --- | --- |
| Transformer                    | Select |     |     |     |
Alignment Loss
| 𝑞 𝑞                        | Prediction |     |     |     |
| -------------------------- | ---------- | --- | --- | --- |
| 𝑒𝑛𝑐1𝑞𝑢𝑒𝑟𝑦𝑒𝑛𝑐3𝑒𝑛𝑐4𝑞𝑢𝑒𝑟𝑦𝑒𝑛𝑐6 | Predictor  |     |     |     |
+ + + + + +
𝑝𝑜𝑠1𝑝𝑜𝑠2 𝑝𝑜𝑠3𝑝𝑜𝑠4𝑝𝑜𝑠5 𝑝𝑜𝑠6
Encoded Tokens
| 𝑒𝑛𝑐𝑗 | Encoder | Momentum Encoder |     |     |
| ---- | ------- | ---------------- | --- | --- |
𝑒1 𝑒2 =
|             | Embedding |      | Embedding |     |
| ----------- | --------- | ---- | --------- | --- |
| Transformer |           | 𝑡𝑖𝑚𝑒 |           |     |
𝑐ℎ𝑎𝑛𝑛𝑒𝑙
| 𝑠1 𝑠2 |     | masked | unmasked |     |
| ----- | --- | ------ | -------- | --- |
𝑡𝑜𝑘𝑒𝑛𝑖,𝑗 𝑆𝑢𝑚𝑚𝑎𝑟𝑦
∈𝑚𝑎𝑠𝑘𝑒𝑑
𝑇𝑜𝑘𝑒𝑛𝑠
|     | Patched EEG | Patched EEG |     |     |
| --- | ----------- | ----------- | --- | --- |
Figure1: TheEEGPTstructureinvolvespatchingtheinputEEGsignalasp throughmasking(50%
i,j
timeand80%channelpatches),creatingmaskedpartMandunmaskedpartMandthenembedding
astoken bylocalspatio-temporalembedding. Theencoderprocessesthemaskedpart,extracting
i,j
features(enc )consistingof{e }S foreachtimesegmentintheMpartwithsummarytokens
j i i=1
{s }S . Thepredictorpredictsfeatures(pred )foralltimesegments,aligningwiththeMomentum
i i=1 j
Encoderoutput(menc ). Basedonfeaturesextractedbythepredictorandencoder,thereconstructor
j
generatesrec i,j toreconstructtheEEGsignaloftheMpart.
Predictor: AsinEquation4,thepredictor(PRED)utilizesfeaturesenc ofthemaskedpartfrom
j
theencoder,combinedwithtemporalpositioninformationpos ,topredictthecompleteencoded
j
feature. Embedding and unembedding [32] are performed linearly on the input and output. We
adopttherotarypositionembeddingmethod[33]togeneratepos ,introducingrelativepositional
j
andtemporalinformation. TogeneratepredictionfeaturesbelongingtoM,alearnablevectorquery
isusedasthequerytoken. Throughself-supervisedtraining,theencoderisencouragedtoextract
moreinformationaboutthecorrelationamongtokens:
|               | (cid:32)   | (cid:33) |     |     |
| ------------- | ---------- | -------- | --- | --- |
| {pred }       | =PRED {enc | +pos }   |     | (4) |
| t             |            | j j      |     |     |
| t∈{1,2,...,N} | ∃i,(i,j)∈M |          |     |     |
MomentumEncoder: Thestructureofthemomentumencoderisidenticaltothatoftheencoder.
Equation5outlineshowthemomentumencoder(MENC)processesalltoken i,j attimej asinput
andproducesthecorrespondingoutputmenc . Aftereachtrainingiteration,theparametersofthe
j
encoderareaccumulatedintothemomentumencoderwithafactorofτ =0.01.
|            | (cid:32) | (cid:33) |     |     |
| ---------- | -------- | -------- | --- | --- |
| menc =MENC | {token   | }        |     | (5) |
| j          |          | i,j      |     |     |
(i,j)∈M∪M
WeemployanalignmentlossbasedonMeanSquareError(MSE)[34]toachievespatio-temporal
representationalignment:
1 N
|        | (cid:88)          | )||2 |     |     |
| ------ | ----------------- | ---- | --- | --- |
| L A =− | ||pred j ,LN(menc | j    |     | (6) |
| N      |                   | 2    |     |     |
j=1
InEquation6,LNdenoteslayernormalization[35],whichhelpstomitigatetheeffectsofextreme
valuesandcovariateshift,allowingthemodeltofocusonmoreimportantfeatures.
2.2 Mask-basedReconstruction
Themask-basedreconstructionmethodalignsthereconstructedpatchesgeneratedbythereconstructor
withtherawpatchesp intheMpart.
i,j
4

Reconstructor: AsshowninEquation7,thereconstructor(REC)utilizesfeaturesenc fromtheM
j
partencodedbytheencoderandfeaturespred oftheMpartpredictedbythepredictor,alongwith
j
temporalpositionpos ,togeneratethereconstructedpatchrec
|     | j   |     |     |     |     |     | u,t . Weestablisha"skipconnection" |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- |
betweentheencoderandthereconstructortohelpmaintainthefeaturesandaccelerateconvergence.
|     |         |           |     | (cid:32)   |        |           | (cid:33)   |     |     |
| --- | ------- | --------- | --- | ---------- | ------ | --------- | ---------- | --- | --- |
|     | {rec    | u,t }=REC |     | {enc       | j +pos | j }∪{pred | j +pos j } |     | (7) |
|     | (u,t)∈M |           |     | ∃i,(i,j)∈M |        |           | ∀i,(i,j)∈M |     |     |
Mask-basedreconstructionisachievedusingareconstructionlossbasedontheMeanSquareError
(MSE):
1 (cid:88)
|     |     | L   | =−  |     | ||rec | ,LN(p | )||2  |     | (8) |
| --- | --- | --- | --- | --- | ----- | ----- | ----- | --- | --- |
|     |     | R   |     |     |       | i,j   | i,j 2 |     |     |
|M|
(i,j)∈M
ThecompletepretraininglossLisconstructedbysummingbothL andL :
|     |     |     |     |     |     |     | A R |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | L=L | +L  |     |     |     | (9) |
|     |     |     |     |     | A   | R   |     |     |     |
2.3 LocalSpatio-TemporalEmbedding
𝛓𝟏
|     |     |     |     |     |     | ℜ:𝑐𝑖1 | 𝑀→ 𝜍𝑖1 𝑀 𝛓𝟐 |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ----------- | --- | --- |
𝒄𝟏
𝛓𝟑
|          |     |     |     |          | patch 𝒑𝟏,𝟏  |       | Channel   |     |     |
| -------- | --- | --- | --- | -------- | ----------- | ----- | --------- | --- | --- |
|          |     |     |     | 𝒄        | 𝟐           |       | Embedding |     |     |
| slennahC |     |     |     |          | p a t ch  𝒑 |       | 𝛓𝟒        |     |     |
|          |     |     |     | Patching |             | 𝟐 , 𝟏 |           |     |     |
|          |     |     |     | 𝒄        | 𝟑           |       | +         |     |     |
|          |     |     |     |          | pa t c h  𝒑 | 𝟑 , 𝟏 |           |     |     |
𝒄𝟒
|     |     | EEG |     |     | patch 𝒑𝟒,𝟏 |     | 𝐸𝑚𝑏𝑒𝑑(𝑝𝑖,𝑗) |     |     |
| --- | --- | --- | --- | --- | ---------- | --- | ----------- | --- | --- |
Patch
|     |     |     |     |     |     |     | Embedding | Tokens |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | --- |
Figure2:Illustrationoflocalspatio-temporalembedding.TheEEGsignalisdividedintoequallysized
patchesinthespatio-temporaldimensions.Eachpatchrepresentsatimesegmentforaspecificchannel
without overlap. The patches are linearly embedded and incorporated with channel embedding
informationtoobtainacorrespondingfeature.
Thelocalspatio-temporalembeddingmethodfirstpatchesandembedstheEEGsignalinthespatio-
temporaldimensionbeforefeedingitintotheencoder,asshowninFigure2.WedenotethesetofEEG
signalchannelsas{c }M ,wherec isthenameofeachchannel. Firstly,theEEGsignalisdivided
|     | i i=1 |     | i   |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
intoequallysizedpatchesinthespatio-temporaldimensions,denotedasp i,j ,i∈{1,2,...,M},j ∈
{1,2,...,N}:
|     |     |     |     | p i,j =x |     |     |     |     | (10) |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- | ---- |
i,(j−1)d:jd
wheredrepresentspatch’stimelength,andN =T/disthenumberoftimepatches.Next,thepatches
arelinearlyembedded,combiningthechannelembeddinginformation. WeconstructaCodexbook
[36]{ς ∈ Rde}M (d istheembeddingdimension)containingalllearnablechannelembedding
| i i=1 | e   |     |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
}M }M
vectorsandamappingfromchannelnamestochannelembeddingvectorsℜ:{c i →{ς i .
i=1 i=1
ThismappingflexiblycorrespondsthechannelsoftheEEGdatatothechannelsofthemodelinputs,
allowingthemodeltoadapttomultipledatasetsandimprovechanneladaptation. Thepatch’scontent
is linearly embedded as Embed(p ) = W Tp + b , where W ∈ Rd×de and b ∈ Rde are
|     |     |     | i,j | p   | i,j | p   | p   | p   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∈Rde:
learnableparameters. Embeddedtokendenotesastoken
i,j
|     |     |     | token | =Embed(p |     | )+ς |     |     | (11) |
| --- | --- | --- | ----- | -------- | --- | --- | --- | --- | ---- |
|     |     |     |       | i,j      |     | i,j | i   |     |      |
Basedonself-supervisedlearningtask,theextractedfeaturesofpatchesaremutuallypredictableand
canignorenoisesignalsatsmallerscales. Themethodaimstoextractmacroscopicfeaturesthatspan
largerscales,whicharebelievedtobemoreeasilyrecognizableandconsideredmeaningfulfeatures.
5

Logits
FP1 FPz FP2
Linear
AF3 AF4
Features
|                      |              | F7 F5   | F3          | F6 F8       |
| -------------------- | ------------ | ------- | ----------- | ----------- |
| Encoder (Frozen)     |              |         | F1 Fz F2    | F4          |
|                      |              | FT7 FC5 |             | FC4 FC6 FT8 |
|                      |              | FC3     | FC1 FCz FC2 |             |
|                      |              | C5      | C1 Cz C2    | C4 C6       |
|                      |              | T7 C3   |             | T8          |
|                      |              | CP3     | CP1 CPz CP2 | CP4         |
|                      | Embed Tokens | TP7 CP5 |             | CP6 TP8     |
| Adapt Spatial Filter |              |         | P1 Pz P2    | P4          |
|                      |              | P7 P5   | P3          | P6 P8       |
PO3 POz PO4
|         |     | PO7 |          | PO8 |
| ------- | --- | --- | -------- | --- |
| Channel |     |     | O1 Oz O2 |     |
EEG
| Figure3: Linear-probingmethod. |     | Figure4: | Electrodelocations. |     |
| ------------------------------ | --- | -------- | ------------------- | --- |
2.4 Linear-ProbingMethod
Inthedownstreamtasks,weapplythepretrainedencoderandconcatenateadditionalmodulestosolve
classificationtasks. AsshowninFigure3,weintroducethelinear-probingmethod,whichfreezesthe
parametersinthepretrainedmodelandonlychangestheparametersintheadditionallinearmodules.
Thesemodulesincludeadaptivespatialfilters(1×1convolution)foraligningchannelsbetweenEEG
andthemodel,andalinearlayertomapthefeaturestologits. Theencoderpassestheoutputtokens
correspondingtosummarytokenstothelinearclassificationhead. Thisapproachhelpsavoidthe
overfittingproblemwhenalargeparametermodelisfine-tunedusingalimitednumberofsamples.
Sincetheadditionalmoduleisstraightforward,theperformanceissolelydeterminedbytheencoder,
allowingustoassessthemodel’scapability.
3 Experiments
3.1 DatasetsandDataProcessing
| Table1:             | Datasetsforpretraininganddownstreamtasks |           |          |         |
| ------------------- | ---------------------------------------- | --------- | -------- | ------- |
|                     | Datasets                                 | Paradigms | Subjects | Targets |
|                     | PhysioMI                                 | MI&ME     | 109      | 5       |
|                     | HGD                                      | MI        | 14       | 4       |
| pretrainingDatasets | TSU                                      | SSVEP     | 35       | 40      |
|                     | SEED                                     | EMO       | 15       | 3       |
|                     | M3CV                                     | MULTI     | 106      | -       |
|                     | BCIC-2A                                  | MI        | 10       | 4       |
|                     | BCIC-2B                                  | MI        | 10       | 2       |
|                     | Sleep-EDFx                               | SLEEP     | 197      | 5       |
| DownstreamDatasets  | KaggleERN                                | ERN       | 26       | 2       |
|                     | PhysioP300                               | P300      | 9        | 2       |
|                     | TUAB                                     | Abnormal  | 2383     | 2       |
|                     | TUEV                                     | Event     | 288      | 6       |
WecuratedEEGpublicdatasetsofvariousparadigmsformodelpretrainingasshowninTable1. It
containsmotorimagery(MI)andexecution(ME)datasetsPhysioMI[23],HGD[24],steady-state
visualevokedpotential(SSVEP)datasetTSU[37],emotionalclassificationdatasetSEED[38]and
multi-subjectmulti-sessionmulti-paradigmdatasetM3CV[25]. Toassessthepracticalutilityof
thelearnedrepresentationsindownstreamtasks,wecuratedalistofdatasetsasshowninTable1.
It contains MI datasets BCIC-2A [39], BCIC-2B [40], sleep stage detection dataset Sleep-EDFx
[11],errorrelatednegativity(ERN)datasetKaggleERN[41]andevent-relatedpotentialsdataset
PhysioP300 [23]. We also curated a dataset of abnormal EEG signals dataset TUAB and event
typeclassificationdatasetTUEVfromTempleUniversityEEGCorpus[18]. Thesediversedatasets
6

enablecomprehensiveevaluationoftheproposedEEGPTmodelacrossvarioustasks. Eachdataset
underwentsimilaranddistinctpreprocessingsteps,includingcropping(4s),re-referencing(average),
channelsselecting,scaling(mV)andresampling(256Hz). Thereare0-38HzbandpassfilteringinMI
datasetsfordownstreamtasks. MoredetailsrefertoAppendixC.
3.2 ImplementationandSettings
Modelimplementation. Theimplementationofencoder, predictorandreconstructorinEEGPT
adoptsthevisiontransformer(VIT)[42]andsetsS learnablesummarytokens(similarto[CLS]
token)forsummarizinginformationwithinthesametimepatches. Weused58electrodes(M =58),
asshowninFigure4. Theinputsignalhasasamplingrateoff =256Hz,andtheinputsignaltime
s
lengthisT =1024. Eachpatchhasatimelengthofd=64,correspondingtoa250mstimewindow.
The50%timeand80%channelpatchesofthepatchesaremaskedduringtraining.
pretrainingstrategy. Inpretraining,foreachtrainingdataset,werandomlysampled10%ofthe
samplesasthevalidationset. AsshowninTable6,wetrained8variantswithdifferentembedding
dims,layersoftransformermodels(encoder,predictor,reconstructor)andsummarytokensS. The
AdamWoptimizerwasemployedwiththeOneCyclelearningratestrategy[43](initiallearningrate
of2.5e-4,maximumof5e-4,minimumof3.13e-5). Thetrainingwasconductedfor200epochs,with
abatchsizeof64and16-bitmixedprecisiontrainingon8Nvidia3090GPUs.
Evaluationstrategy. ForthedatasplittingofTUABandTUEV,westrictlyfollowthesamestrategy
asBIOT[15]tocompareallmethodsfairly. Inotherdownstreamtasks,weusethesameexperimental
configuration as BENDR [12], in which Leave-One-Subject-Out (LOSO) validation method are
used. Specially,KaggleERNuses4-foldcross-validationwith10subjectsfortesting,Sleep-EDFx
uses10-foldcross-validationandratio6:2:2intraining,validationandtestsplitting. Weuselinear-
probingmethodfordownstreamtasks. Particularly,inthesleepstagedetectiontask,weusea4-layer
transformer encoder model as a classifier that integrates the output of our model for every 0.25s
forthepurposeofprocessingalongtaskof30s. WeusedtheoptimallargemodelinSection3.5
fortestingonalldownstreamtasks. Toensurethereliabilityoftheexperiments,werepeatedeach
experimentthreetimesandcalculatedthestandarddeviation.
Baselines&Metrics. FortheTUABandTUEVdatasets,weusethesamebaselinesfromBIOT
whicharefullyfine-tunedmodels. Inothertasks,weusethepretrainedBENDR[12],BIOT[15]and
LaBraM[17]asthebaselines. Thefollowingmetricsareusedforcomparison: 1)BalancedAccuracy
(BAC),2)AUROC,3)WeightedF1,4)Cohen’sKappa. WeuseAUROConlyforbinaryclassification
tasksandWeightedF1onlyformulti-classclassificationtasks. MoredetailsrefertoAppendixD.
3.3 DownstreamExperimentResults
Table2: TheresultsofdifferentmethodsonTUAB.
Methods ModelSize BalancedAccuracy AUROC
SPaRCNet[44] 0.79M 0.7896±0.0018 0.8676±0.0012
ContraWR[45] 1.6M 0.7746±0.0041 0.8456±0.0074
CNN-T[46] 3.2M 0.7777±0.0022 0.8461±0.0013
FFCL[47] 2.4M 0.7848±0.0038 0.8569±0.0051
ST-T[48] 3.5M 0.7966±0.0023 0.8707±0.0019
BIOT[15] 3.2M 0.7959±0.0057 0.8815±0.0043
Ours-Tiny 4.7M 0.7959±0.0021 0.8716±0.0041
Ours 25M 0.7983±0.0030 0.8718±0.0050
WeconductedacomparativeanalysiswithotherlargemodelsontheTempleUniversitydatasets,using
thesameconfigurationasBIOT[15]forexperimentsontheTUABandTUEVdatasets. Theresults
arepresentedinTables2and3. IntheTUABdataset,theperformanceofEEGPTiscomparableto
thatoftheBIOTmodel. IntheTUEVdataset,EEGPTimprovesthebalancedaccuracyby9.5%,and
theweightedF1scoreby6.9%comparedtoBIOT.
To further validate the effectiveness of our model, we conducted comparative experiments with
BENDR, BIOT, and LaBraM. The results are shown in Table 4. On the BCIC-2A and BCIC-
2B datasets for motor imagery tasks and the Sleep-EDFx dataset for sleep stage detection, our
7

|              |     | Table3: TheresultsofdifferentmethodsonTUEV. |                  |     |               |               |
| ------------ | --- | ------------------------------------------- | ---------------- | --- | ------------- | ------------- |
| Methods      |     | ModelSize                                   | BalancedAccuracy |     | WeightedF1    | Cohen’sKappa  |
| SPaRCNet[44] |     | 0.79M                                       | 0.4161±0.0262    |     | 0.7024±0.0104 | 0.4233±0.0181 |
| ContraWR[45] |     | 1.6M                                        | 0.4384±0.0349    |     | 0.6893±0.0136 | 0.3912±0.0237 |
| CNN-T[46]    |     | 3.2M                                        | 0.4087±0.0161    |     | 0.6854±0.0293 | 0.3815±0.0134 |
| FFCL[47]     |     | 2.4M                                        | 0.3979±0.0104    |     | 0.6783±0.0120 | 0.3732±0.0188 |
| ST-T[48]     |     | 3.5M                                        | 0.3984±0.0228    |     | 0.6823±0.0190 | 0.3765±0.0306 |
| BIOT[15]     |     | 3.2M                                        | 0.5281±0.0225    |     | 0.7492±0.0082 | 0.5273±0.0249 |
| Ours-Tiny    |     | 4.7M                                        | 0.5670±0.0066    |     | 0.7535±0.0097 | 0.5085±0.0173 |
| Ours         |     | 25M                                         | 0.6232±0.0114    |     | 0.8187±0.0063 | 0.6351±0.0134 |
Table4: TheresultsofuniversalEEGmodelsonvariousdatasets.
Datasets Methods BalancedAccuracy Cohen’sKappa WeightedF1/AUROC
|     | BENDR |     | 0.4899±0.0070 | 0.3199±0.0094 |     | 0.4836±0.0076 |
| --- | ----- | --- | ------------- | ------------- | --- | ------------- |
|     | BIOT  |     | 0.4590±0.0196 | 0.2787±0.0261 |     | 0.4282±0.0289 |
BCIC-2A
|     | LaBraM |     | 0.5613±0.0052 | 0.4151±0.0069 |     | 0.5520±0.0052 |
| --- | ------ | --- | ------------- | ------------- | --- | ------------- |
|     | Ours   |     | 0.5846±0.0070 | 0.4462±0.0094 |     | 0.5715±0.0051 |
|     | BENDR  |     | 0.7067±0.0011 | 0.4131±0.0022 |     | 0.7854±0.0029 |
|     | BIOT   |     | 0.6409±0.0118 | 0.2817±0.0236 |     | 0.7095±0.0141 |
BCIC-2B
|     | LaBraM |     | 0.6851±0.0063 | 0.3703±0.0125 |     | 0.7576±0.0067 |
| --- | ------ | --- | ------------- | ------------- | --- | ------------- |
|     | Ours   |     | 0.7212±0.0019 | 0.4426±0.0037 |     | 0.8059±0.0032 |
|     | BENDR  |     | 0.6655±0.0043 | 0.6659±0.0043 |     | 0.7507±0.0029 |
|     | BIOT   |     | 0.6622±0.0013 | 0.6461±0.0017 |     | 0.7415±0.0010 |
Sleep-EDFx
|     | LaBraM |     | 0.6771±0.0022 | 0.6710±0.0006 |     | 0.7592±0.0005 |
| --- | ------ | --- | ------------- | ------------- | --- | ------------- |
|     | Ours   |     | 0.6917±0.0069 | 0.6857±0.0019 |     | 0.7654±0.0023 |
|     | BENDR  |     | 0.5672±0.0020 | 0.1461±0.0037 |     | 0.6030±0.0044 |
|     | BIOT   |     | 0.5118±0.0089 | 0.0297±0.0224 |     | 0.5495±0.0167 |
KaggleERN
|     | LaBraM |     | 0.5439±0.0029 | 0.0944±0.0066 |     | 0.5693±0.0052 |
| --- | ------ | --- | ------------- | ------------- | --- | ------------- |
|     | Ours   |     | 0.5837±0.0064 | 0.1882±0.0110 |     | 0.6621±0.0096 |
|     | BENDR  |     | 0.6114±0.0118 | 0.2227±0.0237 |     | 0.6588±0.0163 |
|     | BIOT   |     | 0.5485±0.0325 | 0.0968±0.0647 |     | 0.5308±0.0333 |
PhysioP300
|     | LaBraM |     | 0.6477±0.0110 | 0.2935±0.0227 |     | 0.7068±0.0134 |
| --- | ------ | --- | ------------- | ------------- | --- | ------------- |
|     | Ours   |     | 0.6502±0.0063 | 0.2999±0.0139 |     | 0.7168±0.0051 |
modelexhibitedaccuracyimprovementsof9.4%,1.5%,2.6%,respectively,comparedtoBENDR.
ConsideringthatBENDRusedfullmodelfine-tuningwhileourmodelonlyfine-tunedanadditional
linear layer, this suggests that our model extracts richer and more universal features. We used
the linear-probing method for BIOT and LaBraM. EEGPT improved by 2.3%, 3.6%, and 1.4%,
respectively,comparedtoLaBraM,andby12.5%,and8.1%,and2.9%,respectively,comparedto
BIOT.FortheERP-typetaskdatasets,ourmodeloutperformsBENDRby2.6%and3.9%onthe
KaggleERNandPhysioP300datasets,respectively.TheperformanceofourmodelonthePhysioP300
dataset is comparable to that of LaBraM, but higher by 3.0% on KaggleERN. Our model also
outperformsBIOTontheKaggleERNandPhysioP300by7.2%and10.2%, respectively. Onall
tasks,ourmodelEEGPTachievescompetitiveresultscomparedtoBENDR,BIOT,andLaBraM.
ThisdemonstratesthatEEGPTlearnsconsistentrepresentationalfeaturesoverthetemporal-spatial
dimensions,enablingthemodeltobemorewidelyappliedtomultipleparadigmtasksandtoachieve
betterclassificationperformance.
Combiningtheaboveexperimentalresults,wedemonstratethatthemethodproposedinthispaper
addressestheissuesofpoorEEGchanneladaptability,poorqualityofEEGrepresentationsextracted
byexistingself-supervisedlearningmethods,andthelackofuniversalityofrepresentationsacross
multipleparadigms. Ourmethodeffectivelyextractshigh-qualityuniversalEEGrepresentations.
3.4 AblationExperimentResults
Weconductedablationexperimentsusingthelargemodelwithfourdifferentconfigurations,and
theresultsarepresentedinTable5. Intheabsenceofalignmentloss(L ),thereconstructionloss
A
8

|          |     |       | Table5:            | Theresultsoftheablationstudy. |               |                 |
| -------- | --- | ----- | ------------------ | ----------------------------- | ------------- | --------------- |
| Variants |     | L     | L BCIC-2A-BAC      |                               | BCIC-2B-AUROC | KaggleERN-AUROC |
|          |     | A     | R                  |                               |               |                 |
| A:w/oL   |     | 37.13 | 0.57 0.5287±0.0086 |                               | 0.7264±0.0381 | 0.5752±0.0164   |
A
| B:w/oLN |     | 0.15 | 0.002 0.5567±0.0088 |     | 0.7920±0.0012 | 0.5891±0.0227 |
| ------- | --- | ---- | ------------------- | --- | ------------- | ------------- |
C:w/oskip 0.12 0.56 0.5796±0.0011 0.7702±0.0122 0.6356±0.0296
D:withall 0.24 0.56 0.5846±0.0070 0.8059±0.0032 0.6621±0.0096
|     |          |     | Table6: | Theresultsofpretrainedmodels. |                    |       |
| --- | -------- | --- | ------- | ----------------------------- | ------------------ | ----- |
|     | variants | d   | layers  | S params                      | L L BCIC-2A-BAC(%) |       |
|     |          | e   |         |                               | A R                |       |
|     | tiny1    | 64  | 2/2/4   | 1 0.4M                        | 0.32 0.60          | 49.19 |
|     | tiny2    | 64  | 2/2/4   | 4 0.5M                        | 0.36 0.60          | 50.03 |
|     | tiny3    | 64  | 8/8/8   | 4 1.6M                        | 0.17 0.59          | 51.58 |
|     | little   | 128 | 8/8/8   | 4 6.4M                        | 0.18 0.57          | 54.18 |
|     | base1    | 256 | 6/6/6   | 1 19M                         | 0.24 0.56          | 54.53 |
|     | base2    | 256 | 8/8/8   | 4 25M                         | 0.33 0.56          | 56.48 |
|     | base3    | 512 | 6/6/6   | 1 76M                         | 0.14 0.58          | 54.47 |
|     | large    | 512 | 8/8/8   | 4 101M                        | 0.24 0.56          | 58.46 |
iscomparabletothatoftheversionDmodel,butthereisasignificantperformancedegradationof
6%∼9%inthedownstreamtask. Withoutlayernormalizationonthetargetsofreconstructionloss,
theversionBmodeldemonstratedalowerpretrainlossL,butitwasaffectedbyextremevaluesand
covariateshift[35],resultingina3%,1%and7%reductionindownstreamtasksperformance. The
versionCmodel, whichremovestheskipconnectionandusesall{pred }N fromthepredictor
t t=1
asinputstothereconstructor,exhibitedloweralignmentlossandcomparablereconstructionloss
comparedtotheversionDmodel,butshoweda1%∼3%lowerperformanceinthedownstreamtask.
Theseresultssuggestthatthedualself-supervisedmethodproposedinthispaperiseffective,asthe
spatio-temporalalignmentimprovesthequalityoftheEEGrepresentationsextractedbythemodel.
3.5 PretrainExperimentResults
|     | 0.525 |     |     |     | 0.50 |     |
| --- | ----- | --- | --- | --- | ---- | --- |
0.550
0.52
|     | ycaruccA tseT 0.575 |     |     |     |     |     |
| --- | ------------------- | --- | --- | --- | --- | --- |
ssoL tseT
|     | 0.600 |     |     |     | 0.54 |     |
| --- | ----- | --- | --- | --- | ---- | --- |
0.625
|     | 0.650 |     |     |     | 0.56 |     |
| --- | ----- | --- | --- | --- | ---- | --- |
0.675
0.58
0.700
0.725
|     |     | 106 | 107    | 108 | 106    | 107  108 |
| --- | --- | --- | ------ | --- | ------ | -------- |
|     |     |     | Params |     | Params |          |
Figure5: ScalinglawswithEEGPTparametersizeN.Axesareallonalogarithmicscale.
We designed 8 variants to investigate the effects of model size (embedding size d / layers) and
e
summarytoken(S)onpretraininglossanddownstreamtaskaccuracy. Toevaluatetheperformance
of the pretrained models, we used the linear-probing method to test cross-subject classification
tasksontheBCIC-2Adataset. TheexperimentalresultsarepresentedinTable6. Asthemodelsize
(embeddingsized /layers)andsummarytokens(S)increased,thereconstructionloss(L )gradually
e R
decreased, andtheperformanceonthedownstreamtaskimproved. FormodelswiththesameS,
largermodelsexhibitedloweralignmentlossL andhigherperformance. Wealsoinvestigatedthe
A
trendsinaccuracyandreconstructionlossasthemodelsizeincreased,asshowninFigure5. These
|                                        |     |     |     | ACC=(33.6∗N)0.029andL |     | =(0.72∗N)−0.014, |
| -------------------------------------- | --- | --- | --- | --------------------- | --- | ---------------- |
| trendscanbesummarizedbythescalinglaws: |     |     |     |                       |     | R                |
where N is the parameter count of the model. The results of the downstream task experiments
indicatethatlargermodelsgenerallyachievehigheraccuracy, withthelargemodel, featuringan
8-layer, 512-embedding dimension, and 4 summary tokens, exhibiting the highest accuracy. For
simplicity,weusedtheoptimallargemodelfortestingonalldownstreamtasks.
9

4 Conclusion
In this paper, we propose a self-supervised EEG Pretrained Transformer (EEGPT) model with
over 10 million parameters for universal EEG representation learning. We employ a dual self-
supervisedapproachforpretraining,involvingspatio-temporalrepresentationalignmentandmask-
basedreconstruction. Thespatio-temporalrepresentationalignmentalignsmaskedpatches’features
with full patches’ features, enhancing the quality of EEG representations and concentrating key
informationintheencoderoutput. Themask-basedreconstructionleveragesthespatialandtemporal
consistencyexhibitedbyEEGsignalstoextractcomplementaryfeaturesinbothdimensions. We
designahierarchicalstructureforEEGPT,whichfirstextractsstablespatialrepresentationsfrom
short-termEEGsignals,thencapturesthetemporalcorrelationsamonglong-termEEGsignals. This
structurenotonlyreducescomputationalcomplexitybutalsoenhancestheflexibilityandadaptability
of EEGPT in BCI applications. Experiments demonstrate that our dual self-supervised pretrain
model significantly outperforms the popular universal feature extraction models BENDR, BIOT,
and LaBraM on tasks such as motor imagery, sleep stage detection and ERP-type classification.
ComparedwithBIOTontheTUEVdataset,weachieveda9.5%performanceimprovement. These
tasks,whichhavedifferentchannelconfigurationsandsamplingrates,suggestthatEEGPTisscalable.
Inthefuture,weplantofurtherenrichthepretrainingEEGdatasetandexpandthemodelsizeand
applicability.
References
[1] GernotRMüller-Putz. Electroencephalography. Handbookofclinicalneurology,168:249–262,
2020.
[2] Sharlene N Flesher, John E Downey, Jeffrey M Weiss, Christopher L Hughes, Angelica J
Herrera,ElizabethCTyler-Kabara,MichaelLBoninger,JenniferLCollinger,andRobertA
Gaunt. Abrain-computerinterfacethatevokestactilesensationsimprovesroboticarmcontrol.
Science,372(6544):831–836,2021.
[3] EunjinJeon,WonjunKo,JeeSeokYoon,andHeung-IlSuk. Mutualinformation-drivensubject-
invariantandclass-relevantdeeprepresentationlearninginbci. IEEETransactionsonNeural
NetworksandLearningSystems,34(2):739–749,2023. doi: 10.1109/TNNLS.2021.3100583.
[4] Christian O’Reilly, Nadia Gosselin, Julie Carrier, and Tore Nielsen. Montreal archive of
sleepstudies: anopen-accessresourceforinstrumentbenchmarkingandexploratoryresearch.
JournalofSleepResearch,23(6):628–635,2014. doi: https://doi.org/10.1111/jsr.12169. URL
https://onlinelibrary.wiley.com/doi/abs/10.1111/jsr.12169.
[5] TimothyHospedales,AntreasAntoniou,PaulMicaelli,andAmosStorkey. Meta-learningin
neuralnetworks: Asurvey. IEEETransactionsonPatternAnalysisandMachineIntelligence,
44(9):5149–5169,2022. doi: 10.1109/TPAMI.2021.3079209.
[6] JacobDevlin,Ming-WeiChang,KentonLee,andKristinaToutanova. Bert: Pre-trainingof
deepbidirectionaltransformersforlanguageunderstanding,2019.
[7] XinleiChen, SainingXie, andKaimingHe. Anempiricalstudyoftrainingself-supervised
visiontransformers,2021.
[8] KaimingHe,XinleiChen,SainingXie,YanghaoLi,PiotrDollár,andRossGirshick. Masked
AutoencodersAreScalableVisionLearners,December2021. URLhttp://arxiv.org/abs/
2111.06377. arXiv:2111.06377[cs].
[9] Alexei Baevski, Henry Zhou, Abdelrahman Mohamed, and Michael Auli. wav2vec 2.0: A
frameworkforself-supervisedlearningofspeechrepresentations,2020.
[10] Fabian Falck, Suproteem K. Sarkar, Subhrajit Roy, and Stephanie L. Hyland. Contrastive
representation learning for electroencephalogram classification. In ML4H@NeurIPS, 2020.
URLhttps://api.semanticscholar.org/CorpusID:229781944.
[11] B. Kemp, A.H. Zwinderman, B. Tuk, H.A.C. Kamphuisen, and J.J.L. Oberye. Analysis of
asleep-dependentneuronalfeedbackloop: theslow-wavemicrocontinuityoftheeeg. IEEE
TransactionsonBiomedicalEngineering,47(9):1185–1194,2000. doi: 10.1109/10.867928.
10

[12] DemetresKostas,StéphaneAroca-Ouellette,andFrankRudzicz. BENDR:UsingTransformers
andaContrastiveSelf-SupervisedLearningTasktoLearnFromMassiveAmountsofEEG
Data. FrontiersinHumanNeuroscience, 15, 2021. ISSN1662-5161. doi: 10.3389/fnhum.
2021.653659. URL https://www.frontiersin.org/articles/10.3389/fnhum.2021.
653659.
[13] Qiushi Zhu, Xiaoying Zhao, Jie Zhang, Yu Gu, Chao Weng, and Yuchen Hu. Eeg2vec:
Self-SupervisedElectroencephalographicRepresentationLearning, May2023. URLhttp:
//arxiv.org/abs/2305.13957. arXiv:2305.13957[eess].
[14] SimonGeirnaert,TomFrancart,andAlexanderBertrand. Time-adaptiveunsupervisedauditory
attentiondecodingusingeeg-basedstimulusreconstruction. IEEEJournalofBiomedicaland
HealthInformatics,26(8):3767–3778,2022.
[15] ChaoqiYang,M.BrandonWestover,andJimengSun. BIOT:Cross-dataBiosignalLearning
intheWild,May2023. URLhttp://arxiv.org/abs/2305.10351. arXiv:2305.10351[cs,
eess].
[16] AliHossamShoeb. Applicationofmachinelearningtoepilepticseizureonsetdetectionand
treatment. PhDthesis,MassachusettsInstituteofTechnology,2009.
[17] Wei-BangJiang,Li-MingZhao,andBao-LiangLu12. Largebrainmodelforlearninggeneric
rep-resentationswithtremendouseegdatainbci.
[18] IyadObeidandJosephPicone. Thetempleuniversityhospitaleegdatacorpus. Frontiersin
Neuroscience,10,2016.ISSN1662-453X.doi:10.3389/fnins.2016.00196.URLhttps://www.
frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2016.00196.
[19] WeiLiu,Jie-LinQiu,Wei-LongZheng,andBao-LiangLu.Comparingrecognitionperformance
androbustnessofmultimodaldeeplearningmodelsformultimodalemotionrecognition. IEEE
TransactionsonCognitiveandDevelopmentalSystems,14(2):715–729,2021.
[20] YongtianHe,TrieuPhatLuu,KevinNathan,ShoNakagome,andJoseLContreras-Vidal. A
mobilebrain-bodyimagingdatasetrecordedduringtreadmillwalkingwithabrain-computer
interface. Scientificdata,5(1):1–10,2018.
[21] AlexanderAFingelkurts,AndrewAFingelkurts,VictorAErmolaev,andAlexanderYaKaplan.
Stability,reliabilityandconsistencyofthecompositionsofbrainoscillations. International
JournalofPsychophysiology,59(2):116–126,2006.
[22] JacobDevlin,Ming-WeiChang,KentonLee,andKristinaToutanova. Bert:Pre-trainingofdeep
bidirectionaltransformersforlanguageunderstanding. InProceedingsofthe2019Conference
oftheNorth,Jan2019. doi: 10.18653/v1/n19-1423. URLhttp://dx.doi.org/10.18653/
v1/n19-1423.
[23] AryL.Goldberger,LuisA.N.Amaral,LeonGlass,JeffreyM.Hausdorff,PlamenCh.Ivanov,
Roger G. Mark, Joseph E. Mietus, George B. Moody, Chung-Kang Peng, and H. Eugene
Stanley. Physiobank,physiotoolkit,andphysionet. Circulation,101(23):e215–e220,2000. doi:
10.1161/01.CIR.101.23.e215. URLhttps://www.ahajournals.org/doi/abs/10.1161/
01.CIR.101.23.e215.
[24] RobinTiborSchirrmeister,JostTobiasSpringenberg,LukasDominiqueJosefFiederer,Martin
Glasstetter,KatharinaEggensperger,MichaelTangermann,FrankHutter,WolframBurgard,
and Tonio Ball. Deep learning with convolutional neural networks for eeg decoding and
visualization. HumanBrainMapping,aug2017. ISSN1097-0193. doi: 10.1002/hbm.23730.
URLhttp://dx.doi.org/10.1002/hbm.23730.
[25] GanHuang,ZhenxingHu,WeizeChen,ZhenLiang,LinlingLi,LiZhang,andZhiguoZhang.
M3CV:A Multi-subject, Multi-session, and Multi-task database for EEG-based Biometrics
Challenge. bioRxiv,2022. doi: 10.1101/2022.06.28.497624. URLhttps://www.biorxiv.
org/content/early/2022/07/03/2022.06.28.497624.
11

[26] AliAl-Saegh,ShefaADawwd,andJassimMAbdul-Jabbar. Deeplearningformotorimagery
eeg-based classification: A review. Biomedical Signal Processing and Control, 63:102172,
2021.
[27] FotisP.Kalaganis,ElisavetChatzilari,SpirosNikolopoulos,IoannisKompatsiaris,andNikosA.
Laskaris. Anerror-awaregaze-basedkeyboardbymeansofahybridbcisystem. Scientific
Reports, Aug 2018. doi: 10.1038/s41598-018-31425-2. URL http://dx.doi.org/10.
1038/s41598-018-31425-2.
[28] KhaldAliIAboalayon,MiadFaezipour,WafaaSAlmuhammadi,andSaeidMoslehpour. Sleep
stageclassificationusingeegsignalanalysis: acomprehensivesurveyandnewinvestigation.
Entropy,18(9):272,2016.
[29] Xiangwen Kong and Xiangyu Zhang. Understanding masked image modeling via learning
occlusioninvariantfeature,2022.
[30] LiangjianWen,XiasiWang,JianzhuangLiu,andZenglinXu. Mveb: Self-supervisedlearning
with multi-view entropy bottleneck. IEEE Transactions on Pattern Analysis and Machine
Intelligence,2024.
[31] XiaokangChen,MingyuDing,XiaodiWang,YingXin,ShentongMo,YunhaoWang,Shumin
Han, Ping Luo, Gang Zeng, and Jingdong Wang. Context autoencoder for self-supervised
representationlearning. InternationalJournalofComputerVision,132(1):208–223,2024.
[32] Mary Phuong and Marcus Hutter. Formal Algorithms for Transformers, July 2022. URL
http://arxiv.org/abs/2207.09238. Number: arXiv:2207.09238arXiv:2207.09238[cs].
[33] JianlinSu,YuLu,ShengfengPan,BoWen,andYunfengLiu. Roformer: Enhancedtransformer
withrotarypositionembedding,2021.
[34] JiaweiRen,MingyuanZhang,CunjunYu,andZiweiLiu. Balancedmseforimbalancedvisual
regression,2022.
[35] JimmyLeiBa,JamieRyanKiros,andGeoffreyE.Hinton. Layernormalization,2016.
[36] YiqunDuan,JinzhaoZhou,ZhenWang,Yu-KaiWang,andChin-TengLin. DeWave: Discrete
EEG Waves Encoding for Brain Dynamics to Text Translation, October 2023. URL http:
//arxiv.org/abs/2309.14030. arXiv:2309.14030[cs].
[37] YijunWang,XiaogangChen,XiaorongGao,andShangkaiGao. Abenchmarkdatasetforssvep-
basedbrain–computerinterfaces. IEEETransactionsonNeuralSystemsandRehabilitation
Engineering,25(10):1746–1752,2017. doi: 10.1109/TNSRE.2016.2627556.
[38] Wei-LongZhengandBao-LiangLu. Investigatingcriticalfrequencybandsandchannelsfor
eeg-basedemotionrecognitionwithdeepneuralnetworks. IEEETransactionsonAutonomous
MentalDevelopment,7(3):162–175,2015. doi: 10.1109/TAMD.2015.2431497.
[39] MichaelTangermann,Klaus-RobertMüller,AdAertsen,NielsBirbaumer,ChristophBraun,
ClemensBrunner,RobertLeeb,CarstenMehring,KaiJ.Miller,GernotR.Müller-Putz,Guido
Nolte, Gert Pfurtscheller, Hubert Preissl, Gerwin Schalk, Alois Schlögl, Carmen Vidaurre,
Stephan Waldert, and Benjamin Blankertz. Review of the bci competition iv. Frontiers in
Neuroscience,6,2012. URLhttps://api.semanticscholar.org/CorpusID:790253.
[40] David Steyrl, Reinhold Scherer, Josef Faller, and Gernot R. Müller-Putz. Random forests
in non-invasive sensorimotor rhythm brain-computer interfaces: a practical and convenient
non-linear classifier. Biomedical Engineering / Biomedizinische Technik, 61:77 – 86, 2016.
URLhttps://api.semanticscholar.org/CorpusID:7782626.
[41] PerrinMargaux,EmmanuelMaby,SébastienDaligault,OlivierBertrand,andJérémieMattout.
Objective and subjective evaluation of online error correction during p300-based spelling.
AdvancesinHuman-ComputerInteraction,2012,012012. doi: 10.1155/2012/578295.
12

[42] AlexeyDosovitskiy,LucasBeyer,AlexanderKolesnikov,DirkWeissenborn,XiaohuaZhai,
Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly,
Jakob Uszkoreit, and Neil Houlsby. An Image is Worth 16x16 Words: Transformers
for Image Recognition at Scale, June 2021. URL http://arxiv.org/abs/2010.11929.
arXiv:2010.11929[cs].
[43] LeslieN.SmithandNicholayTopin. Super-convergence: Veryfasttrainingofneuralnetworks
usinglargelearningrates,2018. URLhttps://arxiv.org/abs/1708.07120.
[44] JinJing,WendongGe,ShendaHong,MartaBentoFernandes,ZhenLin,ChaoqiYang,Sungtae
An, Aaron F Struck, Aline Herlopian, Ioannis Karakis, et al. Development of expert-level
classificationofseizuresandrhythmicandperiodicpatternsduringeeginterpretation.Neurology,
100(17):e1750–e1762,2023.
[45] ChaoqiYang,CaoXiao,MBrandonWestover,JimengSun,etal. Self-supervisedelectroen-
cephalogram representation learning for automatic sleep staging: model development and
evaluationstudy. JMIRAI,2(1):e46769,2023.
[46] WeiYanPeh,YuanyuanYao,andJustinDauwels. Transformerconvolutionalneuralnetworks
forautomatedartifactdetectioninscalpeeg. In202244thAnnualInternationalConferenceof
theIEEEEngineeringinMedicine&BiologySociety(EMBC),pages3599–3602.IEEE,2022.
[47] HongliLi, ManDing, RonghuaZhang, andChunboXiu. Motorimageryeegclassification
algorithmbasedoncnn-lstmfeaturefusionnetwork. Biomedicalsignalprocessingandcontrol,
72:103342,2022.
[48] YonghaoSong,XueyuJia,LieYang,andLonghanXie. Transformer-basedspatial-temporal
featurelearningforeegdecoding. arXivpreprintarXiv:2106.11170,2021.
[49] HeHeandDongruiWu. Transferlearningforbrain–computerinterfaces: Aeuclideanspace
dataalignmentapproach. IEEETransactionsonBiomedicalEngineering,67(2):399–410,2019.
[50] JianlinSu,YuLu,ShengfengPan,AhmedMurtadha,BoWen,andYunfengLiu. RoFormer:
EnhancedTransformerwithRotaryPositionEmbedding,August2022. URLhttp://arxiv.
org/abs/2104.09864. arXiv:2104.09864[cs].
13

A Additionalresults
Thissectionprovidesadditionalexperimentalresultstosupporttheclaimsinthemainpaper.
A.1 Ablationstudyforthepredictor
0.68
0.66
0.64
0.62
0.60
0.58
0.56
0 5000 10000 15000 20000 25000 30000 35000 40000
step
ssol
dilav
baseline
no_predictor
Figure6: Validationlosscurvesduringpretraining,where’baseline’isthestandardEEGPTmodel
and’no_predictor’isthemodelwithoutthepredictor.
Weconductedapretrainingexperimentafterremovingthepredictor,thevariationofL losswith
R
thenumberofiterationstepsduringtrainingisshowninFigure6. Inthisfigure,’baseline’isthe
standardEEGPTmodeland’no_predictor’isthemodelwithoutthepredictor. Wecanseethatthe
reconstructionlossL ofthe’no_predictor’modelafterremovingthepredictordoesnotdecrease,
R
whichindicatesthatdirectlyaligningtheoutputsoftheencoderandthemomentumencoderdoes
leadtotheproblemofrepresentationcollapse,resultinginthereconstructiontasknotbeingableto
learnmeaningfulrepresentation.
A.2 Ablationstudyforpretrainingmethods
Table7: Theresultsoftheablationstudyforpretrainingmethods.
Variants L L BCIC-2A-BAC BCIC-2B-AUROC KaggleERN-AUROC
A R
A:w/oL 37.13 0.57 0.5287±0.0086 0.7264±0.0381 0.5752±0.0164
A
B:w/oLN 0.15 0.002 0.5567±0.0088 0.7920±0.0012 0.5891±0.0227
C:w/oskip 0.12 0.56 0.5796±0.0011 0.7702±0.0122 0.6356±0.0296
D:withall 0.24 0.56 0.5846±0.0070 0.8059±0.0032 0.6621±0.0096
Intheablationexperiments,weusedtheBCIC-2A,BCIC-2BandKaggleERNdatasetstotestthe
modelwiththelinearprobingmethod,theresultsareshowninTable7. Wecanconcludethat(1)the
modelperformancedegradationonalldatasetswithoutL lossissignificant(6%to9%);(2)without
A
layernormalisationonthereconstructiontarget,theperformanceoftheversionBmodeldegradedby
3%,1%,and7%onBCIC-2A,BCIC-2B,andKaggleERN,respectively;and(3)theperformance
ofversionCmodel(removedtheskipconnection)isreducedby1%,3%and3%onthesedatasets,
respectively.
A.3 Ablationstudyforfine-tuningmethods
Wehaveaddedexperimentscomparinglinearprobingmethodandfullfine-tuningmethod,aswell
as experiments comparing with and without adaptive spatial filter. The experimental results are
displayedinTable8. InTable8,’ASF’standsforwithanadaptivespatialfilter,incontrasttofeeding
the signal directly into the model; ’L-P’ stands for using linear probing, in contrast to using full
fine-tuningofthemodel. ModelvariantsAandCarethemodelswithfullfine-tuningandlinear
probingafterexcludingtheadaptivespatialfilter,respectively. ModelvariantsBandDaremodels
14

Table8: Theresultsoftheablationstudyforfine-tuningmethods.
Variants ASF L-P BCIC-2A-BAC BCIC-2B-AUROC KaggleERN-AUROC
A 0.5774±0.0072 0.7871±0.0054 0.6078±0.0101
B ✓ 0.5183±0.0155 0.7541±0.0083 0.6110±0.0019
C ✓ 0.5586±0.0089 0.7974±0.0030 0.6463±0.0081
D ✓ ✓ 0.5846±0.0070 0.8059±0.0032 0.6621±0.0096
withfullfine-tuningandlinearprobingafterusingadaptivespatialfilter,respectively. Theresults
showthatontheBCIC-2BandKaggleERNdatasets,variantsCandDtestedwithlinearprobing
achievedbetterresultsthanvariantsAandBusingfullfine-tuning;ontheBCIC-2Adataset,variant
Awithfullfine-tuningandnoadaptivespatialfilterisclosetovariantDwithlinearprobingandan
adaptivespatialfilter,butoverallthelinearprobingusedbymodelsCandDoutperformAandB.
TheresultsshowthatvariantsBandDusingadaptivespatialfilterachievebetterresultscomparedto
variantsAandCwithoutadaptivespatialfilter.
A.4 Scalinglawsexperiments
0.235
0.240
0.245
0.250
0.255
105 106 107
Params
ycaruccA
tseT
Figure7: ResultsonTUABdataset. ScalinglawswithEEGPTparametersizeN.Axesareallona
logarithmicscale.
0.22
0.24
0.26
0.28
0.30
0.32
105 106 107
Params
CORUA
tseT
Figure8: ResultsonBCIC-2Bdataset. ScalinglawswithEEGPTparametersizeN.Axesareallona
logarithmicscale.
WeaddedtheresultsofthescalelawexperimentsontheTUABdatasetandtheBCIC-2Bdataset,
asshowninFigure7and8. TheresultsontheTUABdatasetshowthatthescalinglawofthetest
balancedaccuracymetricwithmodelsize(N)forTUABis: BAC=(0.74∗N)0.0034;theresults
15

ontheBCIC-2BdatasetshowthatthescalinglawoftheAUROCmetricwithmodelsize(N)for
BCIC-2Bis: AUROC=(0.61∗N)0.0157.
A.5 Effectofpretraindatasize
0.54
0.56
ycaruccA tseT
0.58
0.60
0.62
0.64
|     | 2×101 | 3×1014×101 6×101 | 100 |
| --- | ----- | ---------------- | --- |
Data Size
Figure9: ResultsonBCIC-2Adataset. ScalinglawswithpretraindatasizeD.Axesareallona
logarithmicscale.
0.22
0.24
CORUA tseT
0.26
0.28
0.30
|     | 2×101 | 3×1014×101 6×101 | 100 |
| --- | ----- | ---------------- | --- |
Data Size
Figure10: ResultsonBCIC-2Bdataset. ScalinglawswithpretraindatasizeD.Axesareallona
logarithmicscale.
Weaddedpretrainingexperimentsusing100%,50%,25%,and12.5%ofthetrainingdataandtested
themonthedownstreamtasksofBCIC-2AandBCIC-2B.TheresultsarepresentedinFigure9and
10. Theresultsshowthatthescalinglawofthebalancedaccuracymetricwiththetotalamountof
(0.58∗D)0.0461;
dataD (thepercentageofthetrainingdataused)forBCIC-2Ais: ACC = and
thescalinglawoftheAUROCmetricwiththetotalamountofdataDforBCIC-2Bis:AUROC=
(0.79∗D)0.0325.
A.6 ResultsofLaBraMonTUABandTUEV
| Table9:    | TheresultsofdifferentmethodsonTUAB. |                  |               |
| ---------- | ----------------------------------- | ---------------- | ------------- |
| Methods    | ModelSize                           | BalancedAccuracy | AUROC         |
| BIOT[15]   | 3.2M                                | 0.7959±0.0057    | 0.8815±0.0043 |
| LaBraM[17] | 5.8M                                | 0.8140±0.0019    | 0.9022±0.0009 |
| Ours-Tiny  | 4.7M                                | 0.7959±0.0021    | 0.8716±0.0041 |
| Ours       | 25M                                 | 0.7983±0.0030    | 0.8718±0.0050 |
16

|            | Table10:  | TheresultsofdifferentmethodsonTUEV. |     |               |               |
| ---------- | --------- | ----------------------------------- | --- | ------------- | ------------- |
| Methods    | ModelSize | BalancedAccuracy                    |     | WeightedF1    | Cohen’sKappa  |
| BIOT[15]   | 3.2M      | 0.5281±0.0225                       |     | 0.7492±0.0082 | 0.5273±0.0249 |
| LaBraM[17] | 5.8M      | 0.6409±0.0065                       |     | 0.8312±0.0052 | 0.6637±0.0093 |
| Ours-Tiny  | 4.7M      | 0.5670±0.0066                       |     | 0.7535±0.0097 | 0.5085±0.0173 |
| Ours       | 25M       | 0.6232±0.0114                       |     | 0.8187±0.0063 | 0.6351±0.0134 |
LaBraMemploysalargerpretrainingdatasetthanours,whichalsocontainstheTUEGdatasetthat
issimilartotheTUABandTUEVdistributions,andwhosepaperillustratesthescaleeffectofthe
amountofpretrainingdata,whichmayhavefacilitatedthelearningofaricherandmoredownstream
task-adaptablerepresentationforLaBraM.
A.7 Ablationstudyofself-supervisedlearningonTUAB
|                    | Table11: | TheresultsofdifferentmethodsonTUAB. |                  |     |               |
| ------------------ | -------- | ----------------------------------- | ---------------- | --- | ------------- |
| Methods            |          | ModelSize                           | BalancedAccuracy |     | AUROC         |
| BIOT[15]           |          | 3.2M                                | 0.7959±0.0057    |     | 0.8815±0.0043 |
| Ours(nopretrained) |          | 25M                                 | 0.7553±0.0014    |     | 0.8260±0.0018 |
| Ours               |          | 25M                                 | 0.7983±0.0030    |     | 0.8718±0.0050 |
Wetestedthemodelwithrandomlyinitializedparameters(nopretrainedmodel)ontheTUABdataset
andthetestresultsareshowninTable11. InTable11,’Ours(nopretrained)’representsthemodel
thatisnotloadedwithpretrainedparameters. Bycomparison,weseethatthemodelwithoutusing
self-supervisedpretraininghastheworstperformanceonTUAB,witha4%reductioninbalance
accuracyanda5%reductioninAUROCcomparedtothemodelloadedwithpretrainingparameters.
B CODEACCESS
| Thecodeforthispaperisavailableat: |     | https://github.com/BINE022/EEGPT. |     |     |     |
| --------------------------------- | --- | --------------------------------- | --- | --- | --- |
C DATASETDESCRIPTION
C.1 PRETRAININGDATASETDESCRIPTION
| C.1.1 MotorImageryandMotorExecutiontasks: |     |     |     | PhysioNetMI[23] |     |
| ----------------------------------------- | --- | --- | --- | --------------- | --- |
ThePhysioNetMIdataset2consistsofover1500one-minuteandtwo-minuteEEGrecordingsobtained
from109volunteers. Subjectsperformeddifferentmotorexecution/imagerytaskswhilerecording
64-channelEEGusingtheBCI2000system.
Preprocessing: Alleighttaskswereusedduringthepretrainingofthispaper,usingaglobalaverage
reference,interceptingdatafrom0to6safterthestartofeachtrial,andrandomlyinterceptingdata
froma4stimewindowoftheseduringpretraining.
| C.1.2 MotorImagerytask: |     | HGD[24] |     |     |     |
| ----------------------- | --- | ------- | --- | --- | --- |
TheHGDdataset,a128-electrodedataset,wastakenfrom14healthysubjectswithapproximately
1,000trialseach. Thefour-secondexecutivemovementtrialsweredividedinto13runs. Thefour
typesofmovementswereleft-handedmovements,right-handedmovements,bipedalmovements,and
rest. Thetrainingsetconsistedofapproximately880trialsforallbutthelasttworuns,andthetest
setconsistedofapproximately160trialsforthelasttworuns. WeaccessthisdatasetbyMOABB3.
Preprocessing: Allfourtaskswereusedinthepretrainingprocessofthispaper,firstdownsampled
to256HzandthenstandardizedtomV,usingaglobalaveragereferencetointerceptthedatafrom0
2https://physionet.org/content/eegmmidb/1.0.0/
3https://neurotechx.github.io/moabb/dataset_summary.html
17

to10safterthestartofeachtrial,andrandomlyinterceptingthedatafroma4-stimewindowofthese
duringpretraining.
C.1.3 SSVEPtask: TSU[37]
TheTSUdataset4isabenchmarkdatasetforbrain-computerinterfacesbasedonsteady-statevisual
evokedpotentials(TSUBenckmark). ThisdatasetcollectsSSVEP-BCIrecordingsfrom35healthy
subjects using a brain-computer interface (BCI) speller with 40 characters for experimental data
acquisition. SSVEP-BCIrecordingsweremadefor40charactersthatflashedatdifferentfrequencies
(8-15.8Hzwith0.2Hzintervals).
Stimuli: Each trial began with a visual cue (red square) indicating the target stimulus. The cue
appearedonthescreenfor0.5seconds. Subjectswereaskedtoshifttheireyestothetargetassoonas
possiblewithinthecueduration. Afterthecuewasoffset,allstimulibeganflashingonthescreen
simultaneouslyfor5seconds. Afterthestimulusoffset,thescreenwasblankedfor0.5seconds,and
thenthenexttrialbegan,whichallowedsubjectstohaveashortrestperiodbetweensuccessivetrials.
Signal: EEGof35subjects(64channels,250Hz). Eachsubject’sexperimentconsistedof6blocks.
Each blockcontained 40trials correspondingto all40 charactersdisplayed inrandomized order.
Total: 35personsx6blocksx40trials.
Preprocessing: All40taskswereusedinthepretrainingprocessofthispaper,firstdownsampledto
256Hz,andthenstandardizedtomV,usingagloballyaveragedreferencetointerceptthedatafrom0
to4safterthestartofeachtrialforpretraining.
C.1.4 EmotionRecognitiontask: SEED[38]
TheSEEDdataset,ShanghaiJiaoTongUniversityEmotionEEGdataset(SEED)5,isanEEGdataset
providedbytheBCMIlabledbyProf. BaoliangLu.
Stimuli: 15four-minutelongmovieclipsfromsixChinesemovies.
Signal: EEG (62 channels, 200 Hz) from 15 subjects and eye movement data from 12 subjects.
Threeexperimentswereconductedpersubject,eachapproximatelyoneweekapart,foratotalof15
subjectsx3sessions=45subjects.
Scores: Positive(1),negative(-1),andneutral(0).
Preprocessing: Allthreetaskswereusedinthepretrainingprocessofthispaper,firstdownsampled
to256HzandthenstandardizedtomV,usingaglobalaveragereferencetointerceptthedatafrom0
to10safterthestartofeachtrialforpretraining.
C.1.5 Identificationtask: M3CV[25]
TheM3CVdataset6 isareliablebrainprintidentificationsystemdesignedtowithstandchangesin
thementalstateofthesubjects(cross-paradigmtest)andsuccessfullyidentifyindividualsevenafter
severaldays(cross-sessiontest). TheMulti-SessionMulti-ParadigmEEGdatabase(Multi-Subject
Multi-SessionMulti-ParadigmCommonalityandVariability(M3CV))contains106healthysubjects,
twosessions,andsixtypesofEEGparadigms.
Experimental paradigms: Resting state, event-related potentials, evoked stimuli, P300, motor
execution,andSSVEP.
Preprocessing: The full task-state data were used in the pretraining process of this paper, first
upsampledto256Hz,andthenstandardizedtomV,usingagloballyaveragedreference,intercepting
datafrom0to4safterthestartofeachtrialforpretraining.
4http://bci.med.tsinghua.edu.cn/download.html
5https://bcmi.sjtu.edu.cn/home/seed/
6https://aistudio.baidu.com/competition/detail/315/0/related-material
18

C.2 DOWNSTREAMDATASETDESCRIPTION
C.2.1 MotorImageryTask: BCIC-2A[39]
Thisdataset7consistsofEEGdatafrom10subjectsandincludesfourdifferentmotorimagerytasks:
motorimageryofthelefthand(Class1),righthand(Class2),feet(Class3),andtongue(Class4).
Eachsubjectperformedtwosessionsondifferentdays,withatotalof288trialspersession.
Preprocessing:Uniformunits;0to38Hzfilteringwasused;resamplingto256Hz;EAnormalization
[49]wasusedforeachsession. EAnormalizationisacommonnormalizationmethodappliedtodata
frommotionimagerytaskssuchasBCIC2A.
ExperimentalConfiguration: ExperimentsusingtheLOSOmethod. IntheBCIC2Adataset4-
categorycross-subjectexperiment,theaccuracyofthemodelinthispaperislowerthanthatofthe
task-specificSOTAmodel. ThismayberelatedtothehighindividualvariabilityoftheBCIC2Adata.
Thefine-tuningmethodofcombiningthetask-specificmodelwiththemodelinthispaperwasused
fortesting. TheMSConvNetmodel,whichhasamulti-scaleconvolutionalEEGNet-likestructure,
wasusedasthemotorimagerytask-specificmodel. Themodelbranchfirstmapstheinput22-channel
EEGsignalinto10-20systemstandardchanneldatausinganadaptivespatialfilter(convolution);
thena pretrainedencoder isusedto extract thegenericrepresentations; andafter collocatingthe
generic representations and the in-domain representations of Wenchao’s model branch, they are
mappedintocategorylogitsusingalinearlayer. TrainingisperformedusingtheAdamWoptimizer,
OneCyclelearningratestrategy[43](startinglearningrate5e-4,maximum1e-3,minimum4.22e-7),
100roundsoftraining,andbatchsizeof72.
C.2.2 MotorImageryTask: BCIC-2B[40]
Thisdataset8consistsofEEGdatafrom10subjects.Eachsubjectwasgivenfivetrainingopportunities,
thefirsttwoofwhichweretrainingdatawithoutfeedback(screening)andthelastthreewithfeedback.
Thethreebipolarrecordings(C3,Cz,andC4)weresampledatafrequencyof250Hz. Thedataset
consisted of motor imagery (MI) for two categories: left-handed (category 1) and right-handed
(category2). Eachsubjectparticipatedintwosessionswithoutfeedbackrecordingsontwodifferent
dayswithinatwo-weekperiod. Eachsessionconsistedof120category-balancedtrials.
Preprocessing:Uniformunits;0to38Hzfilteringwasused;resamplingto256Hz;EAnormalization
[49]wasusedforeachsession. EAnormalizationisacommonnormalizationmethodappliedtodata
frommotionimagerytaskssuchasBCIC2A.
ExperimentalConfiguration: ExperimentusingLOSOvalidationmethod. Thefine-tunedmodeling
approachwasusedtotestacross-subject2-categorizationtaskontheBCIC2Bdatasetforthemotor
imagerytask. Theinputdataare3-channel(C3,Cz,andC4channels)EEGdatawith4s,256Hz
samplingrate;tofullyutilizethefeatureextractioncapabilityofthemodel,spatialfilters(convolution)
wereusedtomapthe3-channelsoftheinputdatainto7-channels, whichcorrespondstotheC5,
C3,C1,CZ,C2,C4,andC6channelsofthepretrainedencoder;thefeaturesareextractedusingthe
pretrainedencoderandthenmappedinto7channelsusingthelinearlayermappedtocategorylogits.
ThetrainingprocessisperformedusingAdamWoptimizer,OneCyclelearningratestrategy[43]
(startinglearningrate1.6e-5,maximum4e-4,minimum1.51e-7),100roundsoftraining,andbatch
sizeof64.
C.2.3 SleepStageDetectionTask: Sleep-EDFx[11]
Thisdataset9 givesfurtherinsightintothegeneralizabilityofthemodel,asBCIdataaretypically
categorizedinthecontextofaspecifictrialorevent,whereasSSCisamuchmorecontinuousproblem
thatrequires labelingthe specificsleepstage thata subject isin over along periodoftime. The
Sleep-EDFxdatasetcontains197(78healthysubjects)all-nightsleeprecordings,whichincludeEEG,
electrooculogram,chinEMG,andeventmarkers.
Preprocessing: The preprocessing method of Banville et al. (2020) was referred to, which first
converts the data unit to mV, and then uses a 30Hz low-pass filter, intercepts the samples in 30s
7https://www.bbci.de/competition/iv/#datasets
8https://www.bbci.de/competition/iv/#datasets
9https://physionet.org/content/sleep-edfx/1.0.0/
19

non-overlappingwindows,andusesachannel-wise(channel-independent)z-scorenormalizationfor
eachsample.
ExperimentalConfiguration: Subjectswererandomlydividedaccordingtotheratioof60
C.2.4 ERNtask: KaggleERN[41]
In this dataset10, each subject is presented with letters and numbers (showing 36 possible items
onamatrix)tospellwords. Eachitemofthewordisflashedinarandomordergroupedtogether
and selected one at a time. The selected item is the one that the online algorithm is most likely
torecognizeasatypicaltargetresponse. Thegoalofthischallengewastodeterminewhetherthe
selecteditemswerecorrectbyanalyzingthebrainsignalsofsubjectsafterreceivingfeedback. Two
transcription-spellingconditionswereused: afastmodewithmoreerrors(4blinksperitem);anda
slower,lesserror-pronecondition(8blinksperitem).
Preprocessing: Uniformunits;downsamplingto256Hz;globalaveragingreference;intercepting2
sofdatastartingat-0.7sbeforetheonsetofflicker.
Experimental Configuration: For comparison with the BENDR paper, 10 of the subject data
wereusedasthetestdataset,andtheremainingsubjectdatawasusedfor4-foldcross-validation
methodtraining. KaggleERNusesfine-tuningmethod1,withaslidingwindowof125msinsteps,
tofirstlymapthe56channelstothe19-channelEEGdataofthe10-20systembyadaptivespatial
filters(convolution),andthenfeaturesareextractedusingapretrainedencoder,andfinallymapped
intoclassificationlogitsusingalinearlayer. ThetrainingprocessisperformedusingtheAdamW
optimizer,theOneCyclelearningratestrategy[43](startinglearningrateof1.6e-5,maximumof
4e-4,andminimumof1.51e-7),and100roundsoftrainingwithabatchsizeof64.
C.2.5 P300task: PhysioNetP300[23]
Inthisdataset11,eachparticipantwasaskedtospellatotalof20charactersusingatraditionalmatrix
speller(Donchinspeller). Thetargetcharacterswererandomlyselectedbeforethestartoftherun.
Eachrowandcolumnofastandard6x6charactermatrixwasrandomlyaugmentedfor100msat
50msintervalswithapproximately20flashes. Duringthistime,subjectswereaskedtofocustheir
attentiononthetargetcharacterandmentallycountthenumberoftimesthetargetcharacterwas
highlighted.
Preprocessing: Uniformunits;120Hzlow-passfilteringwasused;downsamplingto256Hz;and2s
ofdatastartingat-0.7sbeforetheonsetoftheflickerwasintercepted.
ExperimentalConfiguration: ForcomparisonwiththeBENDRpaper,subjects8,10,and12were
removedandthedatafromtheremaining9subjectswereretained. Experimentswereperformed
using the LOSO cross-validation method. The PhysioNetP300 uses a fine-tuning method with a
slidingwindowof125msstepsize,usingallchannelsusedinthepretrainingphase;thedatafrom
eachEEGchannelisfirstadaptivelyscaledbyanadaptivespatialfilter(learnablescalingfactor),
thenfeaturesareextractedusingthepretrainingencoder,andfinallymappedusingthelinearlayer
mappingforclassificationlogits. ThetrainingprocessusesAdamWoptimizer,OneCyclelearning
ratestrategy[43](startinglearningrate3.2e-5,maximum8e-4,minimum3.02e-7),100roundsof
training,andbatchsizeof64.
C.2.6 TUAB(abnormaldetection)andTUEV(eventtypeclassification)[18]
TUAB12 is a corpus of EEGs which are 23-channel and sampled at 256 Hz. All data have been
annotatedasnormalorabnormal. Therearetotal409,45510-secondsamplesthatweuseforbinary
classificationtopredictnormal/abnormal.
TUEV13isasubsetofTUEGthatcontainsannotationsofEEGsegmentsasoneofsixclasses: (1)
spikeandsharpwave(SPSW),(2)generalizedperiodicepileptiformdischarges(GPED),(3)periodic
lateralizedepileptiformdischarges(PLED),(4)eyemovement(EYEM),(5)artifact(ARTF)and
10https://www.kaggle.com/c/inria-bci-challenge/data
11https://physionet.org/content/erpbci/1.0.0/
12https://isip.piconepress.com/projects/tuh_eeg/html/downloads.shtml
13https://isip.piconepress.com/projects/tuh_eeg/html/downloads.shtml
20

(6)background(BCKG).TheEEGsignalscontain23channelsat256Hzandaresegmentedinto
112,4915-secondsamples.
We conducted experiments using linear-probing on these two datasets. Since these datasets use
differentelectrodesandsamplingratescomparedtothemodelpretraining,weusedtwolayersof
convolution(spatialconvolutionandtemporalconvolution)toadaptivelyfitthedata. Thespatial
convolutionuseda1x1convolution,andthetemporalconvolutionuseddepthwiseconvolution. The
convolutionkernelsizeforTUABwas(1,15),andforTUEV,itwas(1,55). Bothexperimentsused
thesameoptimizerandalearningrateof5e-4. DuetoGPUmemorylimitations,thebatchsizefor
TUABwas100,andforTUEV,itwas500.
Table12: ModeldesignforTUABdataset.
| InputSize | Operator       | kernel stride | groups padding |
| --------- | -------------- | ------------- | -------------- |
| 23×2000   | conv1d         | 1 1           | 1 0            |
| 20×2000   | batchnorm,gelu | - -           | - -            |
| 20×2000   | conv1d         | 15 1          | 20 7           |
| 20×2000   | batchnorm,gelu | - -           | - -            |
| 20×2000   | dropout(0.25)  | - -           | - -            |
| 20×2000   | eegpt-encoder  | 64 64         | - -            |
| 31×4×512  | flatten,linear | - -           | - -            |
| 1         | output         | - -           | - -            |
Table13: ModeldesignforTUEVdataset.
| InputSize | Operator       | kernel stride | groups padding |
| --------- | -------------- | ------------- | -------------- |
| 23×1000   | conv1d         | 1 1           | 1 0            |
| 20×1000   | batchnorm,gelu | - -           | - -            |
| 20×1000   | conv1d         | 55 1          | 20 27          |
| 20×1000   | batchnorm,gelu | - -           | - -            |
| 20×1000   | dropout(0.5)   | - -           | - -            |
| 20×1000   | eegpt-encoder  | 64 64         | - -            |
| 15×4×512  | flatten,linear | - -           | - -            |
| 6         | output         | - -           | - -            |
ThedetailedmodellingstructureusedinthedownstreamtasksispresentedinTable12andTable13.
The23-channelinputisfirsttoreducethenumberofchannelsto20bytheconvolution. Then,the
eegpt-encoderusesthefollowing20channelembeddingsastheinputs’channelembeddings: [FP1,
FPZ,FP2,F7,F3,FZ,F4,F8,T7,C3,CZ,C4,T8,P7,P3,PZ,P4,P8,O1,O2]. Theeegpt-encoder
maps 64-length window segments of the input signals to 4 (number of summary tokens) × 512-
dimensionalfeatures. Finally,theflattenandlinearlayersareusedtooutputthefinalclassification
score.
D METRICSDESCRIPTION
Thefollowingmetricsareusedforcomparison:1)BalancedAccuracy(BAC):Themeanrecallacross
allclasses,applicabletobothbinaryandmulti-classclassification. 2)AUROC:Theareaunderthe
receiveroperatingcharacteristiccurve,primarilyusedforbinaryclassification. 3)WeightedF1: The
harmonicmeanofprecisionandrecall,withequalemphasisonbothmetrics,employedforevaluating
multi-classclassification. 4)Cohen’sKappa:Astatisticmeasuringtheagreementbetweencategorical
variablesXandY,derivedfromtheobservedandexpectedfrequenciesinthediagonalofasquare
contingencytable. WesetAUROCasthemonitorscoreforbinaryclassificationandCohen’sKappa
asthemonitorscoreformulti-classclassification.
21

E MOREIMPLEMENTATIONDESCRIPTION
Formodelimplementation,theBENDRcodeisdownloadedandmodifieduponthegithub14,the
BENDRcodeisdownloadedandmodifieduponthisgithub15,andtheLaBraMcodeisdownloaded
andmodifieduponthisgithub16. OtherbaselinesimplementationsontheTUABandTUEVdatasets
arealsoreferredtothisrepo17. TheEEGPTstructureimplementationismainlymodifieduponthe
github18,andalsoreferencesthecodeofBENDR.TheROPEembeddingisimplementedusingthe
codeofRoformer[50]ingithub19.
WemainlyuseMNEpackage20,braindecodepackage21,andtorcheegpackage22toloadandprepro-
cessthedata.
F MOREEXPERIMENTRESULTSDESCRIPTION
Inthecomparativeexperiments,thebaselinemodelBIOTdemonstratedanaccuracyof54%inthe
binaryclassificationtaskofEEGP300signalsonPhysioP300dataset4,suggestingitsineffectiveness.
TheP300signalisanevent-relatedpotential(ERP)componentcommonlyobservedinEEGrecord-
ings. Itischaracterizedbyapositivedeflectioninvoltageoccurringapproximately300milliseconds
afterthepresentationofastimulus. TheP300componentisprimarilyconcentratedaroundthe300
msmarkandiscrucialfortasksinvolvingattentionandstimulusevaluation.
OneplausiblereasonforthesuboptimalperformanceoftheBIOTmodelistheinherentnatureofthe
P300signalclassificationtask,whichpredominantlyreliesontime-domainwaveformfeatures. The
BIOTmodel,however,appliesafastFouriertransform(FFT)totheinputsignals,therebyprimarily
extractingfrequency-domainfeatures. Thisfundamentaldiscrepancybetweenthefeaturedomain
utilizedbythemodelandthedomainthatismostpertinenttotheclassificationtasklikelyaccounts
fortheobservedlackofefficacy. Additionally,whiletheP300componentisconcentratedaroundthe
300msmark,theBIOTmodelappliesanFFTon1-secondlengthpatches,whichisoverlyextensive
andresultsinsignificantinformationloss. The"significantinformationloss"ismainlyreflectedinthe
factthattheBIOTmodelonlyretainsthespectralenergyinformationfor1sofeachpatchafterthe
FFT,anddiscardsthephaseinformation. Asimilarsituationalsooccursinthebinaryclassification
taskforERNsignals[27]ontheKaggleERNdataset.
G VISUALIZATION
G.1 ChannelRelationshipVisualization
To further demonstrate the effectiveness of the model implementation, this paper visualizes the
trainedmodel. Duringthepretrainingprocess,channelinformationisencodedthroughlearnable
channelembeddings. Thissectionvisualizesthesimilaritybetweenpositionalencodingstoshowthe
relationshipinformationlearnedbythemodelfromthedata.
Figure 11(a) shows the channel relationship diagram after model pretraining, using the cosine
similaritybetweenchannelembeddingstorepresenttherelationshipsbetweenchannels. Theleft
figureshowsrelationshipswithsimilaritygreaterthan0.5,wherechannelsareclusteredbasedon
theirfront,back,left,andrightpositions. Therightfigureshowsrelationshipswithsimilaritygreater
than0.4,revealingnotonlynearbyrelationshipsbutalsolong-distancerelationshipsacrossbrain
regions.
14https://github.com/SPOClab-ca/BENDR
15https://github.com/ycq091044/BIOT
16https://github.com/935963004/LaBraM
17https://github.com/ycq091044/BIOT
18https://github.com/google-research/vision_transformer
19https://github.com/ZhuiyiTechnology/roformer
20https://github.com/mne-tools/mne-python
21https://github.com/braindecode/braindecode
22https://github.com/torcheeg/torcheeg
22

(a) ChannelEmbeddingSimilarity≥0.5 (b) ChannelEmbeddingSimilarity≥0.4
Figure11: ChannelEmbeddingSimilarityRelationships
Figure12: ChannelEmbeddingSimilarityConnectionDiagram
23

Figure12showsthecosinesimilarityrelationshipsbetweenchannelembeddings, withelectrode
positionsplacedaccordingtotheiractuallocations. Solidlinesindicaterelationshipswithsimilarity
greaterthan0.3,whiledashedlinesindicaterelationshipswithsimilaritybetween0.1and0.3. Itcan
beseenthatchannelsincloseproximityhavehighersimilarity,andthereisalsosignificantsimilarity
betweendistantelectrodesonoppositesides.
G.2 BCIC2AExperimentResultsVisualization
Figure13: BCIC2AChannelandClassPearsonCorrelationDiagram
Figure 13 shows the correlation between channels and motor imagery classes detected using the
channelperturbationmethodaftertrainingontheBCIC2Adataset. Gaussianmultiplicativerandom
noise is randomly added to the signal amplitude of each channel, and the Pearson correlation
between the noise intensity and the changes in the corresponding class logits is calculated and
presentedasaheatmap. Symmetricrelationshipsareobservedforelectrodesrelatedtoleftandright
handmovements,withbilateralelectrodescorrespondingtofootmovements,anddistinctchannels
correspondingtothefourdifferentclasses.
Figure14: BCIC2At-SNEDiagram
Figure14showsthet-SNEdiagramoffeatureslearnedbythemodel. Itcanbeseenthatthefeatures
ofthefourclassesareclusteredinfourdifferentregions,demonstratinglinearseparability.
Figure15showstheconfusionmatrix,indicatingthattherecognitionperformanceforfootmovements
isthebest,whilesamplesfromotherclassesareoftenmisclassifiedasfootmovements.
24

Figure15: BCIC2AConfusionMatrixDiagram
Figure16: P300spatio-temporalAttentionDiagram
G.3 PhysioP300ExperimentResultsVisualization
Figure16showsthemodel’sattentiondistributionfortheP300task. Fortemporalattention, the
modelfocusesmoreonthe-0.1to1stimeperiod. Forspatialattention,themodelfocusesmoreon
thesignalsfromtheF1,FZ,F2,andFCZchannels.
Figure17: P300t-SNEDiagram
Figure17showsthet-SNEdiagramoffeaturesextractedbythemodelforthetwoclassesofsamples.
Thefeaturesofthetwoclassesaredistributedontwosides,withaconfusionbeltinthemiddle,but
overalltheclassesarelinearlyseparable.
25

Figure18: P300ConfusionMatrixDiagram
Theconfusionmatrixshowsthattheperformanceforthenon-targetclassisbetter.
H LIMITATIONS
Firstly,althoughwehavecollectedalarge-scalemulti-taskmixedEEGdatasetandutilizedamodel
structurewithextensiveparametersduringthepretrainingphase,thereremainsasignificantdisparity
comparedtotoday’slargevisionandlanguagemodels. Ourworkisstillintheexploratoryphaseof
traininglargeEEGmodelstolearngeneralrepresentations. Encouragingly,ourexperimentshave
shownthatlargeEEGmodelscancontinuetobeoptimized,achievingconsiderableperformance
improvementscomparedtoexistingmethodsdevelopedforspecificBCItasksandgenerallargeEEG
models. Secondly,whileEEGPTrequiresonlylinear-probingtoadapttosmall-scaledownstream
tasks,itmaystillresultinhighmemorycosts. Finally,EEGPTwaspretrainedusing4sEEGdata.
Thismaystrictmodel’scapability. ItisworthexploringthetrainingoflargeEEGmodelswithlong
recordings.
26

NeurIPSPaperChecklist
1. Claims
Question: Dothemainclaimsmadeintheabstractandintroductionaccuratelyreflectthe
paper’scontributionsandscope?
Answer: [Yes]
Justification: We clearly state the claims made, including the contributions made in the
paperandimportantassumptionsandlimitations.
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
Justification: Wepointoutthelimitationsoftheworkandexplainwhytheyareimportantto
considerinH.
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
• Whiletheauthorsmightfearthatcompletehonestyaboutlimitationsmightbeusedby
reviewersasgroundsforrejection,aworseoutcomemightbethatreviewersdiscover
limitationsthataren’tacknowledgedinthepaper. Theauthorsshouldusetheirbest
judgmentandrecognizethatindividualactionsinfavoroftransparencyplayanimpor-
tantroleindevelopingnormsthatpreservetheintegrityofthecommunity. Reviewers
willbespecificallyinstructedtonotpenalizehonestyconcerninglimitations.
3. TheoryAssumptionsandProofs
Question: Foreachtheoreticalresult,doesthepaperprovidethefullsetofassumptionsand
acomplete(andcorrect)proof?
27

Answer: [NA]
Justification: Thepaperdoesnotincludetheoreticalresults.
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
4. ExperimentalResultReproducibility
Question: Doesthepaperfullydisclosealltheinformationneededtoreproducethemainex-
perimentalresultsofthepapertotheextentthatitaffectsthemainclaimsand/orconclusions
ofthepaper(regardlessofwhetherthecodeanddataareprovidedornot)?
Answer: [Yes]
Justification:Thispaperhasdetailedinstructionsonhowtoreproducethemainexperimental
results.
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
28

Question: Doesthepaperprovideopenaccesstothedataandcode,withsufficientinstruc-
tionstofaithfullyreproducethemainexperimentalresults,asdescribedinsupplemental
material?
Answer: [Yes]
Justification: Wereleaseallcodeanddatapreprocessscriptsinthesupplementalmaterial
andfigshareB.
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
6. ExperimentalSetting/Details
Question: Doesthepaperspecifyallthetrainingandtestdetails(e.g.,datasplits,hyper-
parameters, how they were chosen, type of optimizer, etc.) necessary to understand the
results?
Answer: [Yes]
Justification: Thepaperspecifyallthetrainingandtestdetailsin3.2.
Guidelines:
• TheanswerNAmeansthatthepaperdoesnotincludeexperiments.
• Theexperimentalsettingshouldbepresentedinthecoreofthepapertoalevelofdetail
thatisnecessarytoappreciatetheresultsandmakesenseofthem.
• Thefulldetailscanbeprovidedeitherwiththecode,inappendix,orassupplemental
material.
7. ExperimentStatisticalSignificance
Question:Doesthepaperreporterrorbarssuitablyandcorrectlydefinedorotherappropriate
informationaboutthestatisticalsignificanceoftheexperiments?
Answer: [Yes]
Justification: Theresultsareaccompaniedbyerrorbars,confidenceintervals,orstatistical
significancetests.
Guidelines:
• TheanswerNAmeansthatthepaperdoesnotincludeexperiments.
• Theauthorsshouldanswer"Yes"iftheresultsareaccompaniedbyerrorbars,confi-
denceintervals,orstatisticalsignificancetests,atleastfortheexperimentsthatsupport
themainclaimsofthepaper.
• Thefactorsofvariabilitythattheerrorbarsarecapturingshouldbeclearlystated(for
example,train/testsplit,initialization,randomdrawingofsomeparameter,oroverall
runwithgivenexperimentalconditions).
29

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
8. ExperimentsComputeResources
Question: Foreachexperiment,doesthepaperprovidesufficientinformationonthecom-
puterresources(typeofcomputeworkers,memory,timeofexecution)neededtoreproduce
theexperiments?
Answer: [Yes]
Justification: Thepaperprovidesufficientinformationonthecomputerresourcesin3.2.
Guidelines:
• TheanswerNAmeansthatthepaperdoesnotincludeexperiments.
• ThepapershouldindicatethetypeofcomputeworkersCPUorGPU,internalcluster,
orcloudprovider,includingrelevantmemoryandstorage.
• Thepapershouldprovidetheamountofcomputerequiredforeachoftheindividual
experimentalrunsaswellasestimatethetotalcompute.
• Thepapershoulddisclosewhetherthefullresearchprojectrequiredmorecompute
thantheexperimentsreportedinthepaper(e.g.,preliminaryorfailedexperimentsthat
didn’tmakeitintothepaper).
9. CodeOfEthics
Question: Doestheresearchconductedinthepaperconform, ineveryrespect, withthe
NeurIPSCodeofEthicshttps://neurips.cc/public/EthicsGuidelines?
Answer: [Yes]
Justification: The research conducted in the paper conform, in every respect, with the
NeurIPSCodeofEthics.
Guidelines:
• TheanswerNAmeansthattheauthorshavenotreviewedtheNeurIPSCodeofEthics.
• IftheauthorsanswerNo,theyshouldexplainthespecialcircumstancesthatrequirea
deviationfromtheCodeofEthics.
• Theauthorsshouldmakesuretopreserveanonymity(e.g.,ifthereisaspecialconsid-
erationduetolawsorregulationsintheirjurisdiction).
10. BroaderImpacts
Question: Does the paper discuss both potential positive societal impacts and negative
societalimpactsoftheworkperformed?
Answer: [Yes]
Justification: Thepaperdiscussesthepotentialpositivesocietalimpacts,suchasadvance-
mentsinEEG-baseddiagnosticsandtherapeuticapplications,whichcouldimprovehealth-
careoutcomes.
Guidelines:
• TheanswerNAmeansthatthereisnosocietalimpactoftheworkperformed.
• IftheauthorsanswerNAorNo,theyshouldexplainwhytheirworkhasnosocietal
impactorwhythepaperdoesnotaddresssocietalimpact.
30

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
Answer: [NA]
Justification: Thepaperposesnosuchrisks.
Guidelines:
• TheanswerNAmeansthatthepaperposesnosuchrisks.
• Releasedmodelsthathaveahighriskformisuseordual-useshouldbereleasedwith
necessarysafeguardstoallowforcontrolleduseofthemodel,forexamplebyrequiring
thatusersadheretousageguidelinesorrestrictionstoaccessthemodelorimplementing
safetyfilters.
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
Justification: Wecitetheoriginalpaperofexistingassets.
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
31

• Forexistingdatasetsthatarere-packaged,boththeoriginallicenseandthelicenseof
thederivedasset(ifithaschanged)shouldbeprovided.
• Ifthisinformationisnotavailableonline,theauthorsareencouragedtoreachoutto
theasset’screators.
13. NewAssets
Question:Arenewassetsintroducedinthepaperwelldocumentedandisthedocumentation
providedalongsidetheassets?
Answer: [Yes]
Justification: Wereleaseourcode.
Guidelines:
• TheanswerNAmeansthatthepaperdoesnotreleasenewassets.
• Researchersshouldcommunicatethedetailsofthedataset/code/modelaspartoftheir
submissions via structured templates. This includes details about training, license,
limitations,etc.
• Thepapershoulddiscusswhetherandhowconsentwasobtainedfrompeoplewhose
assetisused.
• Atsubmissiontime,remembertoanonymizeyourassets(ifapplicable). Youcaneither
createananonymizedURLorincludeananonymizedzipfile.
14. CrowdsourcingandResearchwithHumanSubjects
Question: Forcrowdsourcingexperimentsandresearchwithhumansubjects,doesthepaper
includethefulltextofinstructionsgiventoparticipantsandscreenshots,ifapplicable,as
wellasdetailsaboutcompensation(ifany)?
Answer: [NA]
Justification: Thepaperdoesnotinvolvecrowdsourcingnorresearchwithhumansubjects.
Guidelines:
• TheanswerNAmeansthatthepaperdoesnotinvolvecrowdsourcingnorresearchwith
humansubjects.
• Includingthisinformationinthesupplementalmaterialisfine,butifthemaincontribu-
tionofthepaperinvolveshumansubjects,thenasmuchdetailaspossibleshouldbe
includedinthemainpaper.
• AccordingtotheNeurIPSCodeofEthics,workersinvolvedindatacollection,curation,
orotherlaborshouldbepaidatleasttheminimumwageinthecountryofthedata
collector.
15. InstitutionalReviewBoard(IRB)ApprovalsorEquivalentforResearchwithHuman
Subjects
Question: Doesthepaperdescribepotentialrisksincurredbystudyparticipants,whether
suchrisksweredisclosedtothesubjects,andwhetherInstitutionalReviewBoard(IRB)
approvals(oranequivalentapproval/reviewbasedontherequirementsofyourcountryor
institution)wereobtained?
Answer: [NA]
Justification: Thepaperdoesnotinvolvecrowdsourcingnorresearchwithhumansubjects.
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
32