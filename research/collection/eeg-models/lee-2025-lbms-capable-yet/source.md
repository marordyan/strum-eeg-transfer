Are Large Brainwave Foundation Models Capable Yet? Insights from
Fine-tuning
NaLee*12 KonstantinosBarmpas*123 YannisPanagakis234 DimitriosAdamos12 NikolaosLaskaris25
StefanosZafeiriou12
|     | Abstract |     |     | 1.Introduction |     |     |     |     |     |
| --- | -------- | --- | --- | -------------- | --- | --- | --- | --- | --- |
Foundation Models have demonstrated signifi- Brain-ComputerInterface(BCI)technologypromisesanew
5202 luJ 1  ]GL.sc[  1v69110.7052:viXra
|              |        |                 |            | way to interact | with | machines by | creating | direct commu- |     |
| ------------ | ------ | --------------- | ---------- | --------------- | ---- | ----------- | -------- | ------------- | --- |
| cant success | across | various domains | in Artifi- |                 |      |             |          |               |     |
cial Intelligence (AI), yet their capabilities for nication between the human brain and computers. This
brainwavemodelingremainunclear. Inthispa- technologyisbasedontheanalysisofbrainwavesfromelec-
per,wecomprehensivelyevaluatecurrentLarge troencephalogram(EEG)recordingsusingadvancedsignal
BrainwaveFoundationModels(LBMs)through processingand,morerecently,machinelearningtechniques.
BCItechnologyfindsapplicationinvariousareaslikeemo-
systematicfine-tuningexperimentsacrossmulti-
pleBrain-ComputerInterface(BCI)benchmark tion recognition [(Torres et al., 2020), (Xu et al., 2018)],
tasks, including memory tasks and sleep stage epilepticseizuredetection[(Alkawadri,2019),(Djoufack
Nkengfacketal.,2021)],roboticcontrol(Irimiaetal.,2012)
| classification. | Ourextensiveanalysisshowsthat |     |     |     |     |     |     |     |     |
| --------------- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
state-of-the-artLBMsachieveonlymarginalim- andvideogaming(Kerousetal.,2018). BCIscanalsoaug-
|            |             |                  |      | ment human | abilities | and have | the potential | to transform |     |
| ---------- | ----------- | ---------------- | ---- | ---------- | --------- | -------- | ------------- | ------------ | --- |
| provements | (0.9%-1.2%) | over traditional | deep |            |           |          |               |              |     |
architectureswhilerequiringsignificantlymore howweinteractwithourenvironmentandeachother,offer-
parameters (millions vs thousands), raising im- inghopetopeoplewithdisabilitiestoregainlostfunctions
|         |                 |                  |         | [(Chaudhary | et al., | 2016), (Luu | et al., 2017), | (Biasiucci |     |
| ------- | --------------- | ---------------- | ------- | ----------- | ------- | ----------- | -------------- | ---------- | --- |
| portant | questions about | their efficiency | and ap- |             |         |             |                |            |     |
plicability in BCI contexts. Moreover, through etal.,2018), (Kumarasingheetal.,2021), (Sharmaetal.,
2016)].
detailedablationstudiesandLow-RankAdapta-
tion(LoRA),wesignificantlyreducetrainablepa-
TheearlydaysoftheBCIeraplacedhumanexpertsatthe
rameterswithoutperformancedegradation,while
|     |     |     |     | centerofbrainwaveanalysis, |     | withmanualfeatureextrac- |     |     |     |
| --- | --- | --- | --- | -------------------------- | --- | ------------------------ | --- | --- | --- |
demonstratingthatarchitecturalandtraininginef-
|                                          |     |     |     | tion by neuroengineers |     | regarded | as the gold | standard | for |
| ---------------------------------------- | --- | --- | --- | ---------------------- | --- | -------- | ----------- | -------- | --- |
| ficiencieslimitLBMs’currentcapabilities. |     |     | Our |                        |     |          |             |          |     |
manyyears[(Bashashatietal.,2007),(Handy,2009),(Rao,
experimentsspanbothfullmodelfine-tuningand 2013),(Nametal.,2018),(McFarlandetal.,2006)]. How-
parameter-efficientadaptationtechniques,provid-
|              |              |                     |     | ever, these | hand-crafted | features | often fail | to generalize |     |
| ------------ | ------------ | ------------------- | --- | ----------- | ------------ | -------- | ---------- | ------------- | --- |
| ing insights | into optimal | training strategies | for |             |              |          |            |               |     |
effectivelytoreal-worlddata,limitingtheirpracticalityin
| BCIapplications. | Wepioneertheapplicationof |     |     |     |     |     |     |     |     |
| ---------------- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
everydayBCIapplications.
LoRAtoLBMs,revealingthatperformancebene-
fitsgenerallyemergewhenadaptingmultipleneu- The advent of deep learning has made the need for man-
ralnetworkcomponentssimultaneously. These ual feature extraction redundant, as new data-driven ap-
findings highlight the critical need for domain- proachesledtostate-of-the-artperformanceinvariousBCI
|     |     |     |     | paradigms[(Lawhernetal.,2018), |     |     | (Santamar´ıa-Va´zquez |     |     |
| --- | --- | --- | --- | ------------------------------ | --- | --- | --------------------- | --- | --- |
specificdevelopmentstrategiestoadvanceLBMs,
suggestingthatcurrentarchitecturesmayrequire et al., 2020), (Song et al., 2023), (Barmpas et al., 2023),
redesigntofullyleveragethepotentialoffounda- (Bakas et al., 2022), (Wei et al., 2022)]. Although deep
learningmodelshavedemonstratedimpressiveresults,they
tionmodelsinbrainwaveanalysis.
generallydemandsubstantialsupervisionandtask-specific
datacollection,makingtheprocessbothtime-intensiveand
| *Equal                                                 | 1Imperial |         | 2Cogitat |                     |     |     |     |     |     |
| ------------------------------------------------------ | --------- | ------- | -------- | ------------------- | --- | --- | --- | --- | --- |
| contribution                                           |           | College | London   |                     |     |     |     |     |     |
| 3Archimedes/AthenaResearchUnit4NationalandKapodistrian |           |         |          | resource-demanding. |     |     |     |     |     |
UniversityofAthens5AristotleUniversityofThessaloniki.Corre-
FoundationModelshaverecentlyemergedasapromising
spondenceto:NaLee<na.lee12@ic.ac.uk>.
approachtoaddresstheselimitations,showingremarkable
Proceedingsofthe42nd resultsinvariousdomains,particularlyinNaturalLanguage
InternationalConferenceonMachine
ProcessingandComputerVision[(Brownetal.,2020),(Tou-
Learning,Vancouver,Canada.PMLR267,2025.Copyright2025
bytheauthor(s).
1

AreLargeBrainwaveFoundationModelsCapableYet?InsightsfromFine-Tuning
| vronetal.,2023),(Mizrahietal.,2023),(ParaperasPapan- |     |                                   |     |     |     | 2.1.LaBraM    |               |              |                |     |
| ---------------------------------------------------- | --- | --------------------------------- | --- | --- | --- | ------------- | ------------- | ------------ | -------------- | --- |
| toniouetal.,2024)].                                  |     | Inspiredbythistremendousprogress, |     |     |     |               |               |              |                |     |
|                                                      |     |                                   |     |     |     | LaBraM (Jiang | et al., 2024) | is a unified | EEG foundation |     |
researchershavebeguntodevelopsimilarLargeBrainwave
modeldesignedtoenablecross-datasetlearningbysegment-
Models(LBMs)tothedomainofBCIs[(Jiangetal.,2024),
|     |     |     |     |     |     | ingEEGsignalsintochannel-specificpatches. |     |     | Inspiredby |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | ---------- | --- |
(Cuietal.,2024),(Wangetal.,2025),(Jiangetal.,2025)].
VQ-GAN(Esseretal.,2020),itemploysvector-quantized
Theoretically,theselargemodelsofferseveralpotentialad-
neuralspectrumpredictiontotrainasemanticallyrichneu-
| vantages: theyarecapableofidentifyingcomplexpatterns |     |     |     |     |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
raltokenizer,whichencodescontinuousrawEEGchannel
| and relationships |     | in EEG | data, | thanks to | their extensive |     |     |     |     |     |
| ----------------- | --- | ------ | ----- | --------- | --------------- | --- | --- | --- | --- | --- |
patchesintocompactneuralcodes,knownasaneuralcode-
| self-supervised | pre-training |     | on  | a wide array | of unlabeled |     |     |     |     |     |
| --------------- | ------------ | --- | --- | ------------ | ------------ | --- | --- | --- | --- | --- |
book.
datasets. Thus,theydemonstrateimprovedgeneralization,
reducingtheneedfortask-specificdatacollectionandmodel
trainingandcreatemorerobustandversatileBCIsystems
capableofadaptingtovarioususers,tasksandenvironments.
Inaddition,theirgenerativenatureequipsthesemodelswith
astrongadaptabilitytonoveldownstreamtaskswhilealso
enablingthemtogeneratehigh-qualitysyntheticdata,thus
| offering promising |     | solutions | for | predicting | brain activity |     |     |     |     |     |
| ------------------ | --- | --------- | --- | ---------- | -------------- | --- | --- | --- | --- | --- |
andreconstructingcorruptedbrainsignals(Barmpasetal.,
2024a).
|             |                                       |     |     |     |     | Figure1. | IllustrationofLaBraM’sNeuralCodebook |     |     |     |
| ----------- | ------------------------------------- | --- | --- | --- | --- | -------- | ------------------------------------ | --- | --- | --- |
| Inthiswork, | weexplorethecurrentstateofLargeBrain- |     |     |     |     |          |                                      |     |     |     |
waveModels(LBMs)forEEG-basedBCIs,adoptingastruc-
Thisneuralcodebookservesasastrongbaseforpre-training
turedmulti-stepmethodology:
|             |     |            |     |             |             | the foundation     | model. | LaBraM follows  | a two-step      | pre- |
| ----------- | --- | ---------- | --- | ----------- | ----------- | ------------------ | ------ | --------------- | --------------- | ---- |
|             |     |            |     |             |             | training approach: | first  | training of the | neural codebook |      |
| 1. We begin | by  | evaluating | the | performance | of publicly |                    |        |                 |                 |      |
available pre-trained state-of-the-art LBMs, specifi- withtargetobjectivebeingthereconstructionofthefourier
|     |     |     |     |     |     | amplitude | and phase of | the EEG patch. | Then, | the core |
| --- | --- | --- | --- | --- | --- | --------- | ------------ | -------------- | ----- | -------- |
callyLaBraM(Jiangetal.,2024)andNeuroGPT(Cui
trainingofthefoundationmodel,wherethemodellearns
etal.,2024),againsttraditionaldeeplearningmodels.
bypredictingtheoriginalneuralcodebookformaskedEEG
Thiscomparisonaimstohighlighttheadvantagesand
channelpatches.
limitationsofLBMsincomparisontowell-established
techniques.
LaBraMwaspre-trainedonapproximately2,500hoursof
|     |     |     |     |     |     | diverseEEGsignalssourcedfromaround20datasets. |     |     |     | Its |
| --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- |
2. WeinvestigatetheapplicationofLow-RankAdapta-
tion(LoRA)(Huetal.,2021),awidelyusedmethod effectivenesswasvalidatedonavarietyofdownstreamtasks,
|     |     |     |     |     |     | demonstrating | its versatility | and robustness | for different |     |
| --- | --- | --- | --- | --- | --- | ------------- | --------------- | -------------- | ------------- | --- |
forparameterefficientfine-tuning(PEFT)oflargepre-
EEG-basedapplications.
| trainedmodelsacrossdiversetasks. |     |     |     |     | Similarlytothe |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
explorationoftime-seriesfoundationmodels(Gupta
2.2.NeuroGPT
etal.,2024),throughablationstudiesandextensiveex-
perimentalanalysis,weexaminetheefficacyofLoRA
whenappliedtopre-trainedLBMs.
3. Wedemonstratethat,bycarefullyselectingLoRApa-
rameters,itispossibletosignificantlyreducethenum-
| beroftrainableparametersinpre-trainedLBMs. |     |     |     |     | No- |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tably,thisreductionisachievedwithoutcompromising
modelperformance,offeringapracticalpathtowards
moreresource-efficientapplicationsofLBMsinBCI
systems.
2.Background
Inrecentyears,severalLargeBrainwaveModels(LBMs) Figure2.IllustrationofNeuroGPT’sAuto-RegressiveTraining
| have been | introduced | that | promise | strong | generalization |     |     |     |     |     |
| --------- | ---------- | ---- | ------- | ------ | -------------- | --- | --- | --- | --- | --- |
capabilitiesacrossvariousBCIparadigms. Inthiswork,we NeuroGPT (Cui et al., 2024) is a foundation model that
willfocusmainlyontwooftheseLBMs,namelyLaBraM combinesanEEGencoderwithaGPT-basedarchitecture.
(Jiangetal.,2024)andNeuroGPT(Cuietal.,2024). TheEEGencoderdrawsinspirationfromthewidelyrecog-
2

AreLargeBrainwaveFoundationModelsCapableYet?InsightsfromFine-Tuning
| nizeddeeplearningframeworkEEGConformer(Songetal., |     |     |     |     |     |     | 3.Analysis |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
2023)thatutilizesaspatio-temporalconvolutionalfeature
3.1.DataPreprocessing
| extractionfollowedbyaseriesofself-attentionlayers. |     |     |     |     |     | The |     |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
modelleveragesGPT-styleself-supervisedtraining,employ- All models were evaluated in downstream classification
inganauto-regressiveapproach(Brownetal.,2020)where
tasksforthefollowingfivebenchmarkEEGdatasets(Lee
it predicts the next masked token based on preceding to- etal.,2025): MotorparadigminHighGamma(Schirrmeis-
kens. ThistrainingparadigmenablesNeuroGPTtocapture
teretal.,2017),theERP(Event-RelatedPotential)paradigm
complextemporalandspatialpatternsinEEGdata,making fromKoreanUniversity(Hong-Kyungetal.,2019),aWork-
itarobustfoundationmodelforavarietyofdownstream ing Memory dataset (Pavlov et al., 2022), Physionet’s
EEG-basedapplications.
sleepstagingdataset,Sleep-EDF(Kempetal.,2000)and
EyesOpenvsClosedclassificationonthePhysionetMotor
| NeuroGPT | is pre-trained |     | on recordings | from | the | Temple |     |     |     |     |     |     |     |
| -------- | -------------- | --- | ------------- | ---- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
UniversityHospital(TUH)EEGCorpus(Obeid&Picone, dataset(Schalketal.,2004). Thesetaskswereselectedto
captureadiverserangeofBCIparadigmsandthedatasets
2016),acomprehensivedatasetthatoffersdiverseandex-
werespecificallychosenfortheirminimalspuriousartifacts,
tensivedataformodeltraining.Specifically,NeuroGPTwas
|            |        |                |     |          |     |        | reducing | the likelihood |     | of specious | performance |     | during |
| ---------- | ------ | -------------- | --- | -------- | --- | ------ | -------- | -------------- | --- | ----------- | ----------- | --- | ------ |
| trained on | 20,000 | EEG recordings |     | from the | TUH | corpus |          |                |     |             |             |     |        |
training(Leeetal.,2025).
datasetwithatotaldurationof5656hours.
ForeachofthebaselineLargeBrainwaveModels,bench-
2.3.Low-RankAdaptation(LoRA) markdatawaspreprocessedtomatchtheinputdatastructure
usedduringpre-training:
Low-RankAdaptationisaPEFTtechniquethatintroduces
| low-rank   | updates | to pre-trained |     | models,     | significantly | re-      |     |     |     |     |     |     |     |
| ---------- | ------- | -------------- | --- | ----------- | ------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| ducing the | number  | of trainable   |     | parameters. | In            | standard |     |     |     |     |     |     |     |
Rd×k
fine-tuning,thefullweightmatrixW ∈ isupdated 1. ForLaBraM,asamplefrequencyof200Hzwasused,
duringtrainingwhichcanbecomputationallyexpensivefor abandpassfilterfrom0.5-45Hzwasapplied,aswell
large-scalemodels. LoRA,instead,decomposestheupdate asnotchfiltersat50Hz,60Hzand100Hztoremove
intotheproductoftwolow-rankmatrices. Mathematically: powerlinenoise. Trialswerecutinto1spatchestaken
|     |     |        |     |     |     |     | across     | channels, | to                                   | give 256 | patches        | per   | sample. In  |
| --- | --- | ------ | --- | --- | --- | --- | ---------- | --------- | ------------------------------------ | -------- | -------------- | ----- | ----------- |
|     |     |        |     |     |     |     | addition   | to        | the EEG                              | trial    | data, temporal |       | and spatial |
|     |     | ∆W=AB, |     |     |     |     | embeddings |           | for each                             | sample   | were           | given | as input to |
|     |     |        |     |     |     |     | themodel.  |           | Temporalembeddingsincludeeachpatch’s |          |                |       |             |
temporalpositionwithinthelengthofthetrial,whereas
|     | Rd×r |     | Rr×k, |     |     |     |     |     |     |     |     |     |     |
| --- | ---- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where A ∈ and B ∈ with r ≪ min(d,k). spatialembeddingsincludethepositionofthepatch’s
Duringfine-tuning,theoriginalweightmatrixWremains
|     |     |     |     |     |     |     | channel | within | a global | list | of all | known | electrodes. |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------ | -------- | ---- | ------ | ----- | ----------- |
frozen,andonlythelow-rankmatricesAandBaretrained. Onlydatafromelectrodeswhichwerepresentinthe
Theeffectiveweightbecomes:
globallistprovidedwereused.
W ′ =W+∆W=W+AB.
2. FortheNeuroGPTmodel,thedatawereresampledto
250Hzandabandpassfilterof0.05-100Hzwasapplied.
SimilarlytoLaBraM,notchfiltersat50Hz,60Hzand
Thisapproachgreatlyreducesthenumberoftrainablepa-
|                     |          |                                 |          |       |      |          | harmonicswerealsoapplied. |                                          |     |          | NeuroGPT’sinputdata |          |            |
| ------------------- | -------- | ------------------------------- | -------- | ----- | ---- | -------- | ------------------------- | ---------------------------------------- | --- | -------- | ------------------- | -------- | ---------- |
| rameters            | from d×k | to                              | r×(d+k), | where | r is | the rank |                           |                                          |     |          |                     |          |            |
|                     |          |                                 |          |       |      |          | need                      | to include                               | a   | specific | set of              | channels | in a fixed |
| ofthedecomposition. |          | Thelow-rankmatricescapturetask- |          |       |      |          |                           |                                          |     |          |                     |          |            |
|                     |          |                                 |          |       |      |          | order.                    | Therefore,foreachbenchmarkdataset,weonly |     |          |                     |          |            |
specificadaptationswhilepreservingtheoriginalmodel’s
|                       |              |                                |         |        |        |          | use           | data from | electrodes                        |     | that are | present | in the pre- |
| --------------------- | ------------ | ------------------------------ | ------- | ------ | ------ | -------- | ------------- | --------- | --------------------------------- | --- | -------- | ------- | ----------- |
| pre-trainedknowledge. |              | Forexample,intransformer-based |         |        |        |          |               |           |                                   |     |          |         |             |
|                       |              |                                |         |        |        |          | trainingdata. |           | Foranyexpectedchannelswhicharenot |     |          |         |             |
| layers, LoRA          | is typically |                                | applied | to the | weight | matrices |               |           |                                   |     |          |         |             |
includedinthebenchmarkdata,thenearestavailable
ofkey, queryorvalueprojectionsinself-attentionlayers,
electrode’sdataisused(ifthelocationiswithinafew
significantlyreducingcomputationalandmemorydemands.
centimeters),otherwisethechanneldataaresettozero.
Mathematically,duringinference,thecomputationalover-
headofLoRAisnegligiblebecausethelow-rankupdates
| ∆Warepre-computed. |     | ThisconstitutesLoRAaneffective |     |     |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
method for adapting large pre-trained models to specific For all downstream datasets, Common Average Re-
tasks,wherefine-tuningefficiencyandgeneralizationare referencing(CAR)wasappliedacrossallchannelstoreduce
| critical. |     |     |     |     |     |     | noise. |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
3

AreLargeBrainwaveFoundationModelsCapableYet?InsightsfromFine-Tuning
Table1.Classificationaccuracyoffinetunedfoundationmodelsandstandarddeeplearningarchitectures,reportedasmean(std).Each
trained/finetunedfor20epochswith10foldcross-validation. Trainableparametersincludethesizeoftheclassificationheads. Bold
valuesindicatebestperformancepertaskoroverall.
| MODEL |     | MOTOR |     | ERP |     | MEMORY |     | SLEEP |     | EYES |     | MEAN | PARAMS |     |
| ----- | --- | ----- | --- | --- | --- | ------ | --- | ----- | --- | ---- | --- | ---- | ------ | --- |
EEGNET 0.657(.087) 0.912(.009) 0.660(.022) 0.624(.037) 0.803(.061) 0.731(.024) 2,394
EEG- 0.590(.087) 0.896(.007) 0.669(.021) 0.688(.057) 0.823(.038) 0.733(.021) 22,366
INCEPTION
LABRAM 0.614(.096) 0.911(.013) 0.643(.040) 0.704(.025) 0.840(.041) 0.742(.023) 5,854,288
NEUROGPT 0.682(.083) 0.904(.012) 0.610(.052) 0.665(.030) 0.821(.052) 0.736(.025) 78,536,146
(FULL
MODEL)
NEUROGPT 0.695(.085) 0.908(.012) 0.634(.035) 0.647(.024) 0.843(.045) 0.745(.027) 717,958
(ENCODER)
Table2.P-valuesofpaired-ttestsbetweenEEGInceptionandfinetunedfoundationmodels.Boldvaluesindicatestatisticallysignificant
result(p<0.05)
|     | MODELS              |     |     |     |     |     |     | MOTOR ERP     |     | MEMORY | SLEEP  | EYES   |     |     |
| --- | ------------------- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------ | ------ | ------ | --- | --- |
|     | EEGINCEPTION/LABRAM |     |     |     |     |     |     | 0.5860 0.0123 |     | 0.1090 | 0.2995 | 0.4468 |     |     |
EEGINCEPTION/NEUROGPT(FULLMODEL) 0.0314 0.0401 0.0041 0.2226 0.8979
EEGINCEPTION/NEUROGPT(ENCODER) 0.0072 0.0051 0.0399 0.0495 0.1056
3.2.ComparingBrainwaveFoundationModelswith that no participant would be present in both the training
DeepLearningModels andvalidationsets. Toperformthedownstreamtasks,un-
trainedclassificationheadswereaddedtothepre-trained
Theperformanceoflargefoundationmodelsvariesdramat-
transformer-basedLargeBrainwaveFoundationModelsbe-
| ically between |     | domains. | In some | areas, | large-scale |     | pre- |                  |     |          |     |           |        |            |
| -------------- | --- | -------- | ------- | ------ | ----------- | --- | ---- | ---------------- | --- | -------- | --- | --------- | ------ | ---------- |
|                |     |          |         |        |             |     |      | fore finetuning. |     | The size | and | structure | of the | classifier |
traininghasrevolutionizedtaskperformancebyenabling
dependonthelatentdimensionofthemodelandthenum-
| the models   | to         | generalize  | across | a broad  | range | of applica- |     |               |         |     |           |            |     |       |
| ------------ | ---------- | ----------- | ------ | -------- | ----- | ----------- | --- | ------------- | ------- | --- | --------- | ---------- | --- | ----- |
|              |            |             |        |          |       |             |     | ber of target | classes | for | the given | benchmark. | The | exact |
| tions, often | surpassing | traditional |        | methods. |       | However,    | in  |               |         |     |           |            |     |       |
architectureoftheclassifiersisgiveninTable4:
otherdomains,foundationmodelssometimesfailtodemon-
stratesignificantadvantagesandareevenoutperformedby 1. For LaBraM, a simple dropout and fully connected
| simpler,domain-specificbaselines. |     |     |     | Itisthereforeimportant |     |     |     |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
layerwereused
tocriticallymeasuretheeffectivenessofrecentLargeBrain-
wave Foundation Models (LBMs). To achieve this, here 2. ForNeuroGPT,athree-layerMLPwithdropoutand
wesystematicallyevaluatetheperformanceoffine-tuned
ELUactivationswereused
LargeBrainwaveFoundationModelsincomparisontoother
| deeplearningarchitectures. |     |     | Bybenchmarkingonavariety |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Usingthesamefine-tuningsetup,weperformedasimilar
| of tasks | and datasets | as  | described | in  | section | 3.1, we | aim |     |     |     |     |     |     |     |
| -------- | ------------ | --- | --------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
training(fromscratch)processfortheEEGNetandEEGIn-
toassesswhetherfine-tunedLBMsconsistentlyprovidean
ceptionmodelstoprovideabasisforcomparison.Asshown
advantageovermorespecializedortraditionalapproaches.
|     |     |     |     |     |     |     |     | in Table | 1, standard | deep | learning | baselines | can | achieve |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ---- | -------- | --------- | --- | ------- |
We perform finetuning on three configurations: the pre- comparable or even superior performance to some large
| trained | LaBraM | base model, | the | pre-trained |     | NeuroGPT |     |         |                                           |     |     |     |     |     |
| ------- | ------ | ----------- | --- | ----------- | --- | -------- | --- | ------- | ----------------------------------------- | --- | --- | --- | --- | --- |
|         |        |             |     |             |     |          |     | models. | However,NeuroGPToutperformsallothermodels |     |     |     |     |     |
modelandtheencoder-onlymoduleofthepre-trainedNeu- onaverage,includingbothstandarddeeplearningbaselines
roGPT model (as discussed in (Cui et al., 2024) where andotherlargefoundationmodels. WhileNeuroGPTmight
| the authors | claim | that fine-tuning |     | the | encoder | alone | pro- |          |          |           |       |                 |     |        |
| ----------- | ----- | ---------------- | --- | --- | ------- | ----- | ---- | -------- | -------- | --------- | ----- | --------------- | --- | ------ |
|             |       |                  |     |     |         |       |      | not lead | in every | benchmark | task, | it consistently |     | demon- |
ducessimilarorimprovedresultsoverthefullmodel). Each stratesstrongaverageperformance.
| configuration |     | was trained | for 20 | epochs | (to | avoid overfit- |     |                 |     |        |         |                |     |      |
| ------------- | --- | ----------- | ------ | ------ | --- | -------------- | --- | --------------- | --- | ------ | ------- | -------------- | --- | ---- |
|               |     |             |        |        |     |                |     | Both foundation |     | models | (LaBraM | and Neuro-GPT) |     | have |
ting)andevaluatedusing10-foldsubject-independentcross-
intheirpre-trainingdatasetsparadigmsthatincludemotor-,
validation,wheresamplesweresplitonasubjectlevelsuch
|     |     |     |     |     |     |     |     | ERP-, sleep- | and | eyes-related |     | tasks. The | results | in Table |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------ | --- | ---------- | ------- | -------- |
4

AreLargeBrainwaveFoundationModelsCapableYet?InsightsfromFine-Tuning
Table3.Classificationaccuracyoffoundationmodelswhereallparametersexceptclassificationheadsarefrozen.Eachtrainedfor20
epochswith10foldcross-validation.Boldvaluesindicatebestperformancepertaskoroverall.
|     | MODEL               |     |     | MOTOR | ERP   | MEMORY SLEEP | EYES  | MEANACCURACY |     |     |
| --- | ------------------- | --- | --- | ----- | ----- | ------------ | ----- | ------------ | --- | --- |
|     | LABRAM              |     |     | 0.297 | 0.884 | 0.670 0.608  | 0.717 | 0.635        |     |     |
|     | NEUROGPT(FULLMODEL) |     |     | 0.366 | 0.884 | 0.656 0.597  | 0.734 | 0.647        |     |     |
|     | NEUROGPT(ENCODER)   |     |     | 0.431 | 0.883 | 0.655 0.602  | 0.746 | 0.663        |     |     |
nextsections.
Table4.Classificationheadsforeachmodelconfigurationwhere
n clsisthenumberofclassesforeachbenchmarktask
3.3.Low-RankAdaptationExplorationinBrainwave
FoundationModels
MODEL CLASSIFIER In this section, we investigate how fine-tuning strategies,
LABRAM Linear(200,n cls),Dropout(0.5) suchasLow-RankAdaptation,influencetheperformance
|          |     |                                        |     |     |     | of these pre-trained | large   | brainwave   | foundation  | models,  |
| -------- | --- | -------------------------------------- | --- | --- | --- | -------------------- | ------- | ----------- | ----------- | -------- |
| NEUROGPT |     | Linear(1024,256),ELU,Dropout(0.5),     |     |     |     |                      |         |             |             |          |
|          |     |                                        |     |     |     | shedding light       | on ways | to maximize | the utility | of these |
| FULL     |     | Linear(256,32),ELU,Dropout(0.3),Linear |     |     |     |                      |         |             |             |          |
MODEL (32,n cls) models across diverse domains. Specifically, we explore
theperformanceandparameterefficiencyofLoRAwhen
| NEUROGPT |     | Linear(2160,256),ELU,Dropout(0.5), |     |     |     |     |     |     |     |     |
| -------- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ENCODER Linear(256,32),ELU,Linear(32,n cls) applied in different ways to finetuning these pre-trained
largebrainwavefoundationmodels.
Inouranalysis,weusetheoriginalformulationofLoRA
1showthatfoundationmodelsachievecomparableperfor-
whereineachtargetmodule’sweightmatrixWisadapted
| mance to | baseline      | models      | in ERP, sleep | and      | eyes tasks. |                                              |     |     |     |     |
| -------- | ------------- | ----------- | ------------- | -------- | ----------- | -------------------------------------------- | --- | --- | --- | --- |
|          |               |             |               |          |             | withtwolow-rankmatricesA,Bwithachosenrank,r. |     |     |     | We  |
| NeuroGPT | significantly | outperforms |               | baseline | models      | in                                           |     |     |     |     |
choosenottoadaptanybiastermsandleavethemfrozendur-
motor. Interestingly,inthememorytask—whichwasnot
|                                           |          |                     |     |                   |          | ingfinetuning.                                | Whenadaptingattentionmoduleswetreat |     |              |       |
| ----------------------------------------- | -------- | ------------------- | --- | ----------------- | -------- | --------------------------------------------- | ----------------------------------- | --- | ------------ | ----- |
| explicitly                                | included | in the pre-training |     | datasets—baseline |          |                                               |                                     |     |              |       |
|                                           |          |                     |     |                   |          | queries,keysandvaluesasasinglecombinedmatrixW |                                     |     |              | qkv , |
| modelsslightlyoutperformfoundationmodels. |          |                     |     |                   | Although |                                               |                                     |     |              |       |
|                                           |          |                     |     |                   |          | howevertheoutputprojectionisleftfrozen.       |                                     |     | Furthermore, |       |
theperformancemarginis1.2%comparedtothenext-best
wealsoapplyLoRAtofullyconnectedandconvolutional
baselinestandarddeeplearningmodel,thisindicatesthat,
layersinouranalysistoeffectivelyevaluatetheimportance
whilethesefoundationmodelsrepresentapromisingstepto-
|     |     |     |     |     |     | oftheselayersduringthefinetuningprocess. |     |     | Inallexperi- |     |
| --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | ------------ | --- |
wardadvancingLargeBrainwaveFoundationModels,their
ments,thescalingfactorα(asdescribedin(Huetal.,2021))
substantialbenefitsovertraditionalapproacheshaveyetto
issetto8.
| befullyrealized. |     | Insummary: |     |     |     |     |     |     |     |     |
| ---------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
3.3.1.LOW-RANKADAPTATIONINALLLAYERS
Standarddeeplearningbaselinestrainedonlyon
|     |     |     |     |     |     | In this subsection, | we  | investigate | the effect | of LoRA |
| --- | --- | --- | --- | --- | --- | ------------------- | --- | ----------- | ---------- | ------- |
specifictaskscanachievecomparable
whendifferentranksareappliedtotheattentionandfully-
performancetofine-tunedpre-trainedlarge
connectedlayersofthelargebrainwavefoundationmodels.
brainwavefoundationmodelswhilehavingonlya
|     |     |     |     |     |     | Therankoftheconvolutionallayersr |     |     | c issettothemaxi- |     |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | ----------------- | --- |
fractionoftrainableparameters.
mumpowerof2whichwouldnotleadtoadapterswitha
greaternumberofparametersthantheoriginalweightma-
Testingthegeneralizationcapabilitiesoflargefoundation trices. ForLaBraMr c =4,andNeuroGPTr c =8forboth
modelsisalsocrucial. Therefore,weperformedthesame configurations,thefullmodelandencoderonly. Giventhe
| fine-tuningprocessasintheabove-mentionedtasksbutkept |     |     |     |     |     | fixedr |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
c ,weexperimentwithdifferentranksfortheattention
thepre-trainedfoundationmodelsfrozenandtrainedonly andfullyconnectedmodulesr ∈{1,2,4,8,16}.
| theclassificationheadsduringthefine-tuningstep. |     |     |     |     | From |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
theresultsinTable3,trainingjusttheclassificationheads
| yields models                          |     | that lack behind | traditional | deep | learning   |     |     |     |     |     |
| -------------------------------------- | --- | ---------------- | ----------- | ---- | ---------- | --- | --- | --- | --- | --- |
| approachesbyalargemarginofalmost8-10%. |     |                  |             |      | Thisdemon- |     |     |     |     |     |
stratesthenecessityoffull-modelfine-tuning,andinturn
| makes parameter |     | efficient fine-tuning |     | (PEFT) | techniques |     |     |     |     |     |
| --------------- | --- | --------------------- | --- | ------ | ---------- | --- | --- | --- | --- | --- |
likeLoRAextremelyvaluable,whichwewillexploreinthe
5

AreLargeBrainwaveFoundationModelsCapableYet?InsightsfromFine-Tuning
Table5.PerformanceoffoundationmodelsfinetunedusingLoRAwithvaryingranksforattentionandfullyconnectedlayers.Ranksfor
LoRAadaptersonconvolutionallayersarefixedtothemaximumpossibleforthegivenmodel.Boldvaluesindicatebestperformanceper
taskoroverall.
MODEL RANK ERP MEMORY SLEEP EYES MEANACCURACY TRAINABLEPARAMETERS
|          | 1   | 0.905 0.624 | 0.729 | 0.839 | 0.774 | 34,149    |     |
| -------- | --- | ----------- | ----- | ----- | ----- | --------- | --- |
|          | 2   | 0.902 0.643 | 0.725 | 0.836 | 0.777 | 67,749    |     |
| LABRAM   | 4   | 0.902 0.638 | 0.715 | 0.822 | 0.770 | 134,949   |     |
|          | 8   | 0.901 0.636 | 0.712 | 0.827 | 0.769 | 269,349   |     |
|          | 16  | 0.902 0.626 | 0.708 | 0.845 | 0.770 | 538,149   |     |
|          | 1   | 0.884 0.650 | 0.643 | 0.788 | 0.741 | 373,218   |     |
| NEUROGPT | 2   | 0.885 0.650 | 0.635 | 0.800 | 0.743 | 467,226   |     |
| FULL     | 4   | 0.884 0.656 | 0.643 | 0.796 | 0.745 | 655,242   |     |
| MODEL    | 8   | 0.885 0.642 | 0.642 | 0.798 | 0.742 | 1,031,274 |     |
|          | 16  | 0.884 0.646 | 0.643 | 0.791 | 0.741 | 1,783,338 |     |
|          | 1   | 0.896 0.643 | 0.643 | 0.796 | 0.744 | 573,866   |     |
|          | 2   | 0.897 0.641 | 0.643 | 0.801 | 0.746 | 577,706   |     |
NEUROGPT
|     | 4   | 0.897 0.643 | 0.644 | 0.799 | 0.746 | 585,386 |     |
| --- | --- | ----------- | ----- | ----- | ----- | ------- | --- |
ENCODER
|     | 8   | 0.897 0.643 | 0.643 | 0.806 | 0.747 | 600,746 |     |
| --- | --- | ----------- | ----- | ----- | ----- | ------- | --- |
|     | 16  | 0.894 0.642 | 0.644 | 0.801 | 0.745 | 631,466 |     |
Figure3.Numberoftrainableparametersagainstmeanaccuracy
acrossallfourdownstreamtasks.
Figure4.Meanaccuracyvsrankofattentionandfullyconnected
AsitisshowninTable5:
layers,givenfixedrankforconvolutionallayers
UsingLoRAinlargebrainwavefoundationmodels
cansignificantlyreducethenumberoftrainable
parameterswithoutcompromisingmodel performance,weperformedaseriesofablationstudiesusing
|     | performance |     |     | theLoRAtechnique. |        | Foreachofthethreemodelconfig- |                  |
| --- | ----------- | --- | --- | ----------------- | ------ | ----------------------------- | ---------------- |
|     |             |     |     | urations,         | we use | the rank that produces        | the best average |
classificationperformanceacrossallbenchmarks,denoted
|                |                 |             |             | asr′. | WethenapplyLoRAtoallpossiblecombinationsof |     |     |
| -------------- | --------------- | ----------- | ----------- | ----- | ------------------------------------------ | --- | --- |
| Theoretically, | we would expect | performance | to increase |       |                                            |     |     |
convolution,attentionandfully-connectedlayers.
| withrank.                          | ForNeuroGPT,thatassumptionholdswhilefor |     |     |                      |     |     |     |
| ---------------------------------- | --------------------------------------- | --- | --- | -------------------- | --- | --- | --- |
| LaBraMitsperformancepeaksatrank=2. |                                         |     |     | AsitisshowninTable6: |     |     |     |
3.3.2.LOW-RANKADAPTATION-ABLATIONSTUDIES
1. PerformingLoRAonlyonaspecificlayer,e.g. atten-
Inordertoperformextensiveexperimentalanalysistofur- tionorconvolution,usuallyyieldslowerperformance
therunderstandtheimportanceofeachelementofthelarge compared to a combination of two or three of these
| brainwavefoundationmodelinthefine-tuneddownstream |     |     |     | layers. |     |     |     |
| ------------------------------------------------- | --- | --- | --- | ------- | --- | --- | --- |
6

AreLargeBrainwaveFoundationModelsCapableYet?InsightsfromFine-Tuning
Table6.PerformanceoffoundationmodelsfinetunedusingLoRAadaptersondifferentcombinationsoflayertypes.Ranksofattention
andfullyconnectedlayersarefixedtothebestperformingrankr′foreachmodelconfigurationasgiveninTable5.Boldvaluesindicate
bestperformancepertaskoroverall.
MODEL LORALAYERS KUERP MEMORY SLEEP EYESOPEN/- MEAN TRAINABLE
|     |     |     |     |     | EDF |     | ACCURACY | PARAMETERS |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- |
CLOSED
|     |     | ATTENTION | 0.902 | 0.644 | 0.722 | 0.852 | 0.780 | 19,401 |
| --- | --- | --------- | ----- | ----- | ----- | ----- | ----- | ------ |
|     |     | FC        | 0.900 | 0.657 | 0.727 | 0.835 | 0.780 | 48,201 |
LABRAM
|     |     | CONV | 0.884 | 0.670 | 0.659 | 0.768 | 0.745 | 549 |
| --- | --- | ---- | ----- | ----- | ----- | ----- | ----- | --- |
r′
| =2       | ATTENTION,FC   |           | 0.899 | 0.623 | 0.717 | 0.843 | 0.770 | 67,401  |
| -------- | -------------- | --------- | ----- | ----- | ----- | ----- | ----- | ------- |
|          | ATTENTION,CONV |           | 0.904 | 0.652 | 0.729 | 0.834 | 0.780 | 19,749  |
|          |                | FC,CONV   | 0.901 | 0.659 | 0.732 | 0.828 | 0.780 | 48,549  |
|          |                | ATTENTION | 0.883 | 0.656 | 0.599 | 0.726 | 0.716 | 374,754 |
| NEUROGPT |                | FC        | 0.884 | 0.656 | 0.579 | 0.732 | 0.713 | 542,658 |
|          |                | CONV      | 0.884 | 0.657 | 0.620 | 0.772 | 0.733 | 279,210 |
FULLMODEL
| r′ =4    | ATTENTION,FC   |           | 0.883 | 0.656 | 0.594 | 0.736 | 0.717 | 646,722 |
| -------- | -------------- | --------- | ----- | ----- | ----- | ----- | ----- | ------- |
|          | ATTENTION,CONV |           | 0.882 | 0.654 | 0.635 | 0.785 | 0.739 | 383,274 |
|          |                | FC,CONV   | 0.884 | 0.646 | 0.637 | 0.788 | 0.739 | 551,178 |
|          |                | ATTENTION | 0.883 | 0.652 | 0.612 | 0.750 | 0.724 | 573,026 |
| NEUROGPT |                | FC        | 0.883 | 0.655 | 0.607 | 0.751 | 0.724 | 580,706 |
|          |                | CONV      | 0.894 | 0.644 | 0.631 | 0.801 | 0.742 | 570,026 |
ENCODER
| r′ =8 | ATTENTION,FC   |         | 0.883 | 0.647 | 0.613 | 0.749 | 0.723 | 592,226 |
| ----- | -------------- | ------- | ----- | ----- | ----- | ----- | ----- | ------- |
|       | ATTENTION,CONV |         | 0.896 | 0.639 | 0.643 | 0.800 | 0.745 | 581,546 |
|       |                | FC,CONV | 0.897 | 0.644 | 0.635 | 0.803 | 0.745 | 589,226 |
2. Thecombinationofconvolutionlayerswitheitherfully Therefore,inthissubsectionweexploretheeffectsofintro-
connectedorattentionlayershasthebestaverageper- ducingdropoutintheparameterspaceofLoRA’slow-rank
formanceacrossallbenchmarks. matrices. ToachievethisweapplyLoRAtotheLaBraM
|                   |     |                  |              |          | model, | adapting attention, | fully-connected | and convolu- |
| ----------------- | --- | ---------------- | ------------ | -------- | ------ | ------------------- | --------------- | ------------ |
| 3. Interestingly, |     | the combinations | of attention | and con- |        |                     |                 |              |
tionallayersasinTable5,withidenticalsetupexceptthis
volutionandfully-connectedandconvolutiondemon-
|     |     |     |     |     | timeintroducingadropoutforeachadapter. |     |     | Thefindingsof |
| --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | ------------- |
stratethesameperformance.Thisunveilsthatforthese
(Dettmersetal.,2023)suggestadropoutprobabilityof0.1
state-of-the-artbrainwavefoundationmodelstheatten-
whenapplyingLoRAto7Band13Bparametermodels,or
tionlayersmightnotcaptureasimportantinformation
|     |     |     |     |     | 0.05for33Band65Bmodels. |     | ThesizeofthefullLaBraM |     |
| --- | --- | --- | --- | --- | ----------------------- | --- | ---------------------- | --- |
astheirtemporalencodingparts.
basemodelisonlyaround5.8Mparameters,thereforewe
selectarelativelyhighdropoutof0.5.
Therefore,wecanconludethat:
AsitisshowninTable7:
LoRAinlargebrainwavefoundationmodelscan
1. IntroducingadropouttoLoRAadapterscanmatchor
demonstrateperformancebenefitswhenusedin improveclassificationperformance.
combinationoftwoorthreedifferenttypesof
2. Dropout’simprovementsinclassificationaccuracytyp-
layers.
icallyincreasewithrank.
3. Performanceismorepositivelyaffectedinthememory
andsleepclassificationtasks.
3.3.3.EFFECTOFDROPOUTONLOW-RANK
ADAPTATION
4.Discussion
| As demonstrated, |     | foundation models | can marginally | out- |     |     |     |     |
| ---------------- | --- | ----------------- | -------------- | ---- | --- | --- | --- | --- |
performtraditionaldeeplearningmodelsonaverageand, Foundation models have revolutionized numerous fields
whenfinetunedwithLoRA,yieldanadditionalperformance in computer science, enabling breakthroughs in natural
boost. Toinvestigatethisfurther,weaimedtodivedeeper languageprocessing,computervisionandotherdomains.
into the LoRA training process for the model with best WhileearlyeffortshavebeenmadetodevelopLargeBrain-
averageperformancefromTable6(LaBraM)andexplore waveFoundationModels(LBMs),thesemodelshaveyet
potentialstrategiesforfurtherenhancingitsperformance. toreachtheirfullpotential. Inthiswork,weinvestigated
7

AreLargeBrainwaveFoundationModelsCapableYet?InsightsfromFine-Tuning
Table7.LaBraMfinetunedusingLoRAwithvaryingranksforattentionandfullyconnectedlayeradapters.Eachvalueisthedifferencein
classificationaccuracybetweenusingadropoutwithprobability0.5vsnodropout.
|     |     | RANK | KUERP  |     | MEMORY | SLEEPEDF | EYESOPEN/CLOSED |        |     | MEAN   |     |     |     |
| --- | --- | ---- | ------ | --- | ------ | -------- | --------------- | ------ | --- | ------ | --- | --- | --- |
|     |     | 1    | -0.002 |     | +0.046 | +0.007   |                 | -0.005 |     | +0.011 |     |     |     |
|     |     | 2    | +0.003 |     | +0.025 | +0.010   |                 | +0.005 |     | +0.011 |     |     |     |
|     |     | 4    | +0.004 |     | +0.032 | +0.019   |                 | +0.012 |     | +0.017 |     |     |     |
|     |     | 8    | +0.006 |     | +0.034 | +0.024   |                 | +0.012 |     | +0.019 |     |     |     |
|     |     | 16   | +0.006 |     | +0.042 | +0.029   |                 | -0.014 |     | +0.016 |     |     |     |
fine-tuningtechniquesappliedtotwostate-of-the-artLarge willlargelyoutperformallcurrentstate-of-the-artbaselines
BrainwaveFoundationModels. invarioustaskswithminimumrequiredfine-tuning.
Ourfindingsrevealthatlargepre-trainedmodelswhichof-
5.Conclusion
ferinterpretabilityinsights(LaBraM)outperformstandard
deeplearningbaselinesandblack-boxmodels(NeuroGPT).
Inthiswork,weinvestigatefine-tuningtechniquesforlarge
However,themarginofimprovementissmallwhenconsid-
|                                   |     |     |     |                   |     |     | brainwave  | foundation | models | (LBMs),           |     | providing | a com-   |
| --------------------------------- | --- | --- | --- | ----------------- | --- | --- | ---------- | ---------- | ------ | ----------------- | --- | --------- | -------- |
| eringtherelativesizesofthemodels: |     |     |     | forexample,afully |     |     |            |            |        |                   |     |           |          |
|                                   |     |     |     |                   |     |     | prehensive | evaluation | of     | their performance |     | in a      | range of |
fine-tunedLaBraMhasover2000timesmoretrainablepa-
|     |     |     |     |     |     |     | downstreamBCIbenchmarktasks. |     |     |     | Ourexperimentsshow |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | ------------------ | --- | --- |
rametersthanEEGNet.Thisfindingsignifiestheimportance
that,despitetheirscaleandpre-training,currentfine-tuned
ofdevelopingmoreefficientlargebrainwavemodelsandthe
LBMsunderperformcomparedtostandarddeeplearning
needtodevelopnewdomain-specifictrainingtechniquesto
models,whichhavesignificantlyfewertrainableparameters.
traintheselargemodels.
Furthermore,wedemonstratethattheLow-RankAdapta-
Additionally,weconductedanin-depthstudyofthewidely tion(LoRA)fine-tuningtechniquecaneffectivelyreduce
usedLow-RankAdaptationtechnique. Ourresultsdemon- thetrainableparametersofLBMswithoutcompromising
strate that applying LoRA to large brainwave foundation performance,butusuallywhenappliedtoacombinationof
models can substantially reduce the number of trainable twoorthreedifferenttypesoflayers.
| parameters | without | sacrificing | performance. |     | However, |     |     |     |     |     |     |     |     |
| ---------- | ------- | ----------- | ------------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Tothebestofourknowledge,thisisthefirststudytoobjec-
throughaseriesofablationstudies,weuncoveredthatper-
tivelyandsystematicallyassessthefine-tunedperformance
formanceimprovementswithLoRAareachievedonlywhen
ofLBMsonadiverseandcarefullycuratedsetofBCIdown-
itisappliedtoacombinationoftwoorthreedifferenttypes
|                 |        |           |           |     |       |          | streamtasks. | Furthermore,similarlythestudyintime-series |     |     |     |     |     |
| --------------- | ------ | --------- | --------- | --- | ----- | -------- | ------------ | ------------------------------------------ | --- | --- | --- | --- | --- |
| of layers. This | raises | important | questions |     | about | the pre- |              |                                            |     |     |     |     |     |
foundationmodels(Guptaetal.,2024),thisworkpioneers
trainingprocessesusedtodeveloptheselargemodels,un-
|     |     |     |     |     |     |     | the use | of LoRA | in the | context | of brainwave | foundation |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------ | ------- | ------------ | ---------- | --- |
veilingcross-stagedependencies(ratherthanbeinglimited
|                  |         |     |            |      |                 |     | models,afieldthatremainslargelyunexplored. |     |     |     |     | Thisexten- |     |
| ---------------- | ------- | --- | ---------- | ---- | --------------- | --- | ------------------------------------------ | --- | --- | --- | --- | ---------- | --- |
| e.g to attention | layers) | and | suggesting | that | their architec- |     |                                            |     |     |     |     |            |     |
sivestudyhighlightscriticalconsiderationsfortheresearch
tureandtrainingmethodologiesmayrequirerefinementand
|                 |          |            |     |           |         |     | community, | emphasizing |     | the need | for more | efficient | and |
| --------------- | -------- | ---------- | --- | --------- | ------- | --- | ---------- | ----------- | --- | -------- | -------- | --------- | --- |
| domain-specific | training | techniques |     | to better | capture | the |            |             |     |          |          |           |     |
effectiveapproachestodevelopingandfine-tuningLarge
underlyingnatureofbrainwavesignal.
BrainwaveFoundationModels(LBMs).
| Previous works | in  | the field | of causal | reasoning | for | deep |     |     |     |     |     |     |     |
| -------------- | --- | --------- | --------- | --------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
learningbrainwavemodels(Barmpasetal.,2024b)aswell
ImpactStatement
asLBMs(Barmpasetal.,2024a)haveshowcasedimportant
trainingconsiderationsthatonemusttakeintoaccountwhen Thispaperpresentsworkwhosegoalistoadvancethefield
training LBMs. These can be used in conjunction with of Machine Learning. There are many potential societal
this work to further guide the research community in the consequences of our work, none which we feel must be
| developmentofefficientLBMs. |     |     |     |     |     |     | specificallyhighlightedhere. |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
WebelievethefutureofLBMsshouldgobeyondmerely
adoptingtransfertechniquesfromotherdomains. Instead, Acknowledgments
theyshouldintegratedomain-specificknowledge—suchas
|     |     |     |     |     |     |     | This work | was | supported | by the | EPSRC | Turing | AI Fel- |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --------- | ------ | ----- | ------ | ------- |
leveragingvariousEEGmodalities—andemploytailored
|     |     |     |     |     |     |     | lowship(GrantRef: |     | EP/Z534699/1): |     | GenerativeMachine |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | -------------- | --- | ----------------- | --- | --- |
trainingstrategies,likebrain-inspiredmaskingtechniques.
LearningModelsforDataofArbitraryUnderlyingGeome-
| These are essential |     | elements | to fully | capture | the | diverse |     |     |     |     |     |     |     |
| ------------------- | --- | -------- | -------- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
try(MAGAL).
natureofEEGandbuildanefficientandeffectiveLBMthat
8

AreLargeBrainwaveFoundationModelsCapableYet?InsightsfromFine-Tuning
References Cui,W.,Jeong,W.,Tho¨lke,P.,Medani,T.,Jerbi,K.,Joshi,
A.A.,andLeahy,R.M.Neuro-gpt:Towardsafoundation
| Alkawadri, | R.  | Brain–computer |     | interface | (bci) | applica- |     |     |     |     |     |     |
| ---------- | --- | -------------- | --- | --------- | ----- | -------- | --- | --- | --- | --- | --- | --- |
modelforeeg,2024.
| tions | in mapping | of  | epileptic | brain | networks | based on |     |     |     |     |     |     |
| ----- | ---------- | --- | --------- | ----- | -------- | -------- | --- | --- | --- | --- | --- | --- |
intracranial-eeg: Anupdate. FrontiersinNeuroscience, Dettmers,T.,Pagnoni,A.,Holtzman,A.,andZettlemoyer,
13:191,2019.ISSN1662-453X.doi:10.3389/fnins.2019. L. Qlora: Efficientfinetuningofquantizedllms,2023.
00191.
|     |     |     |     |     |     |     | DjoufackNkengfack, |     | L.C., | Tchiotsop, | D., Atangana, | R., |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ----- | ---------- | ------------- | --- |
Bakas,S.,Ludwig,S.,Barmpas,K.,Bahri,M.,Panagakis, Louis-Door,V.,andWolf,D.Classificationofeegsignals
|                                            |     |     |     |     |     |      | for | epileptic | seizures detection | and | eye states | identifi- |
| ------------------------------------------ | --- | --- | --- | --- | --- | ---- | --- | --------- | ------------------ | --- | ---------- | --------- |
| Y.,Laskaris,N.,Adamos,D.A.,andZafeiriou,S. |     |     |     |     |     | Team |     |           |                    |     |            |           |
cogitat at neurips 2021: Benchmarks for eeg transfer cation using jacobi polynomial transforms-based mea-
learningcompetition,2022. suresofcomplexityandleast-squaresupportvectorma-
|     |     |     |     |     |     |     |        | Informatics | in Medicine |     | Unlocked, |            |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | ----------- | --- | --------- | ---------- |
|     |     |     |     |     |     |     | chine. |             |             |     |           | 23:100536, |
Barmpas,K.,Panagakis,Y.,Adamos,D.A.,Laskaris,N.,
|                 |     |                          |     |     |              |     | 2021. | ISSN2352-9148. | doi:10.1016/j.imu.2021.100536. |     |     |     |
| --------------- | --- | ------------------------ | --- | --- | ------------ | --- | ----- | -------------- | ------------------------------ | --- | --- | --- |
| andZafeiriou,S. |     | Brainwave-scatteringnet: |     |     | alightweight |     |       |                |                                |     |     |     |
networkforeeg-basedmotorimageryrecognition. Jour- Esser,P.,Rombach,R.,andOmmer,B.Tamingtransformers
forhigh-resolutionimagesynthesis,2020.
| nal of | Neural | Engineering, |     | 20(5):056014, |     | September |     |     |     |     |     |     |
| ------ | ------ | ------------ | --- | ------------- | --- | --------- | --- | --- | --- | --- | --- | --- |
2023. ISSN1741-2552.
|     |     |     |     |     |     |     | Gupta,       | D., Bhatti, | A., Parmar,                         | S., Dan, | C., Liu, | Y., Shen, |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | ----------------------------------- | -------- | -------- | --------- |
|     |     |     |     |     |     |     | B.,andLee,S. |             | Low-rankadaptationoftimeseriesfoun- |          |          |           |
Barmpas,K.,Panagakis,Y.,Adamos,D.,Laskaris,N.,and
dationalmodelsforout-of-domainmodalityforecasting,
| Zafeiriou,S. |     | Acausalperspectiveinbrainwavefounda- |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2024.
| tionmodels. |     | InCausalityandLargeModels@NeurIPS |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2024,2024a.
|     |     |     |     |     |     |     | Handy,T.C. | Brainsignalanalysisadvancesinneuroelec- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------------------------------------- | --- | --- | --- | --- |
tricandneuromagneticmethods.Cambridge,Mass,MIT
| Barmpas, | K., | Panagakis, | Y., | Zoumpourlis, | G., | Adamos, |     |     |     |     |     |     |
| -------- | --- | ---------- | --- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- |
Press. 2009.
| D.A.,Laskaris,N.,andZafeiriou,S. |     |     |     |     | Acausalperspec- |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
tive on brainwave modeling for brain–computer inter- Hong-Kyung,K.,John,W.,Min-Ho,L.,O-Yeon,K.,Seong-
faces.JournalofNeuralEngineering,21(3):036001,may Whan,L.,Siamac,F.,Yong-Jeong,K.,andYoung-Eun,L.
2024b. doi: 10.1088/1741-2552/ad3eb5. Supportingdatafor”eegdatasetandopenbmitoolboxfor
|             |     |             |     |       |        |            | threebciparadigms: |     | Aninvestigationintobciilliteracy”, |     |     |     |
| ----------- | --- | ----------- | --- | ----- | ------ | ---------- | ------------------ | --- | ---------------------------------- | --- | --- | --- |
| Bashashati, | A., | Fatourechi, | M., | Ward, | R. K., | and Birch, |                    |     |                                    |     |     |     |
2019.
| G. E. | A survey | of  | signal | processing | algorithms | in  |     |     |     |     |     |     |
| ----- | -------- | --- | ------ | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
brain–computerinterfacesbasedonelectricalbrainsig- Hu,E.J.,Shen,Y.,Wallis,P.,Allen-Zhu,Z.,Li,Y.,Wang,
nals. JournalofNeuralEngineering,4(2):R32–R57,mar S.,Wang,L.,andChen,W. Lora: Low-rankadaptation
oflargelanguagemodels,2021.
| 2007. | doi: 10.1088/1741-2560/4/2/r03. |     |     |     |     |     |     |     |     |     |     |     |
| ----- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Irimia,D.,Ortner,R.,Krausz,G.,Guger,C.,andPoboro-
| Biasiucci, | A., | Leeb, R., | Iturrate, | I., | Perdikis, | S., Al- |     |     |     |     |     |     |
| ---------- | --- | --------- | --------- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- |
Khodairy, A., Corbet, T., Schnider, A., Schmidlin, T., niuc,M. Bciapplicationinroboticscontrol. IFACPro-
|     |     |     |     |     |     |     | ceedingsVolumes,45(6):1869–1874,2012. |     |     |     |     | ISSN1474- |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --------- |
Zhang,H.,Bassolino,M.,Viceic,D.,Vuadens,P.,Gug-
|          |     |              |     |                      |     |       | 6670. | doi: 10.3182/20120523-3-RO-2023.00432. |     |     |     | 14th |
| -------- | --- | ------------ | --- | -------------------- | --- | ----- | ----- | -------------------------------------- | --- | --- | --- | ---- |
| gisberg, | A., | and Milla´n, | J.  | d. R. Brain-actuated |     | func- |       |                                        |     |     |     |      |
tional electrical stimulation elicits lasting arm motor IFACSymposiumonInformationControlProblemsin
Manufacturing.
| recovery | after | stroke. | Nat | Commun, | 9,  | 2018. doi: |     |     |     |     |     |     |
| -------- | ----- | ------- | --- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
10.1038/s41467-018-04673-z.
|     |     |     |     |     |     |     | Jiang,W.,Wang,Y.,liangLu,B.,andLi,D. |     |     |     | NeuroLM:A |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --------- | --- |
universalmulti-taskfoundationmodelforbridgingthe
Brown,T.B.,Mann,B.,Ryder,N.,Subbiah,M.,Kaplan,
gapbetweenlanguageandEEGsignals.InTheThirteenth
J.,Dhariwal,P.,Neelakantan,A.,Shyam,P.,Sastry,G.,
InternationalConferenceonLearningRepresentations,
Askell,A.,Agarwal,S.,Herbert-Voss,A.,Krueger,G.,
2025.
Henighan,T.,Child,R.,Ramesh,A.,Ziegler,D.M.,Wu,
J.,Winter,C.,Hesse,C.,Chen,M.,Sigler,E.,Litwin,M., Jiang,W.-B.,Zhao,L.-M.,andLu,B.-L. Largebrainmodel
| Gray, | S., Chess, | B., | Clark, | J., Berner, | C., | McCandlish, |     |     |     |     |     |     |
| ----- | ---------- | --- | ------ | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
forlearninggenericrepresentationswithtremendouseeg
| S.,Radford,A.,Sutskever,I.,andAmodei,D. |     |     |     |     |     | Language | datainbci,2024. |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | -------- | --------------- | --- | --- | --- | --- | --- |
modelsarefew-shotlearners,2020.
Kemp,B.,Zwinderman,A.,Tuk,B.,Kamphuisen,H.,and
Chaudhary, U., Birbaumer, N., and Ramos-Murguialday, Oberye,J. Analysisofasleep-dependentneuronalfeed-
A. Brain–computer interfaces for communication and back loop: the slow-wave microcontinuity of the eeg.
rehabilitation. NatRevNeurol,12,2016. doi: 10.1038/ IEEE Transactions on Biomedical Engineering, 47(9):
| nrneurol.2016.113. |     |     |     |     |     |     | 1185–1194,2000. |     | doi: 10.1109/10.867928. |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------------------- | --- | --- | --- |
9

AreLargeBrainwaveFoundationModelsCapableYet?InsightsfromFine-Tuning
Kerous,B.,Sˇkola,F.,andLiarokapis,F.
|             |     |                  |     |                         | Eeg-basedbciand |     | Rao,R.P.N. | Brain-computerinterfacing: |     |     | anintroduction. |     |     |
| ----------- | --- | ---------------- | --- | ----------------------- | --------------- | --- | ---------- | -------------------------- | --- | --- | --------------- | --- | --- |
| videogames: |     | aprogressreport. |     | VirtualReality,22,2018. |                 |     | 2013.      |                            |     |     |                 |     |     |
doi: 10.1007/s10055-017-0328-x.
Santamar´ıa-Va´zquez,E.,Mart´ınez-Cagigal,V.,Vaquerizo-
Kumarasinghe, K., Kasabov, N., and Taylor, D. Brain- Villar, F., and Hornero, R. Eeg-inception: A novel
inspiredspikingneuralnetworksfordecodingandunder- deepconvolutionalneuralnetworkforassistiveerp-based
standingmuscleactivityandkinematicsfromelectroen- brain-computerinterfaces. IEEETransactionsonNeural
cephalographysignalsduringhandmovements. SciRep, SystemsandRehabilitationEngineering, 28(12):2773–
11,2021. doi: 10.1038/s41598-021-81805-4. 2782,2020. doi: 10.1109/TNSRE.2020.3048106.
Lawhern, V. J., Solon, A. J., Waytowich, N. R., Gor- Schalk,G.,McFarland,D.J.,Hinterberger,T.,Birbaumer,
| don, S. | M., | Hung, | C. P., | and Lance, | B. J. | Eegnet: |                   |     |     |                                 |     |     |     |
| ------- | --- | ----- | ------ | ---------- | ----- | ------- | ----------------- | --- | --- | ------------------------------- | --- | --- | --- |
|         |     |       |        |            |       |         | N.,andWolpaw,J.R. |     |     | BCI2000: ageneral-purposebrain- |     |     |     |
a compact convolutional neural network for eeg-based computerinterface(BCI)system. IEEETrans.Biomed.
brain–computerinterfaces. JournalofNeuralEngineer- Eng.,51(6):1034–1043,June2004.
| ing, 15(5):056013, |     |     | July 2018. | ISSN | 1741-2552. | doi: |     |     |     |     |     |     |     |
| ------------------ | --- | --- | ---------- | ---- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
10.1088/1741-2552/aace8c. Schirrmeister,R.T.,Springenberg,J.T.,Fiederer,L.D.J.,
Glasstetter,M.,Eggensperger,K.,Tangermann,M.,Hut-
Lee,N.,Bakas,S.,Barmpas,K.,Panagakis,Y.,Adamos,D., ter, F., Burgard, W., and Ball, T. Deep learning with
| Laskaris,N.,andZafeiriou,S. |     |     |     | Assessingthecapabilities |     |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
convolutionalneuralnetworksforeegdecodingandvi-
oflargebrainwavefoundationmodels. InWorkshopon sualization. Humanbrainmapping,38(11):5391–5420,
| Spurious | Correlation |     | and | Shortcut | Learning: | Founda- |     |     |     |     |     |     |     |
| -------- | ----------- | --- | --- | -------- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- |
2017.
tionsandSolutions,2025.
Sharma,G.,Friedenberg,D.,Annetta,N.,Glenn,B.,Bock-
| Luu, T., | Nakagome, |     | S., He, | Y., and | Contreras-Vidal, | J.  |     |     |     |     |     |     |     |
| -------- | --------- | --- | ------- | ------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
brader,M.,Majstorovic,C.,Domas,S.,Mysiw,J.,Rezai,
Real-time eeg-based brain-computer interface to a vir- A., and Bouton, C. Using an artificial neural bypass
| tualavatarenhancescorticalinvolvementinhuman. |     |     |     |     |     | Sci |            |          |         |             |           |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ------- | ----------- | --------- | --- | --- |
|                                               |     |     |     |     |     |     | to restore | cortical | control | of rhythmic | movements |     | in  |
Rep,7,2017.
doi: 10.1038/s41598-017-09187-0. a human with quadriplegia. Sci Rep, 6, 2016. doi:
McFarland, D.,Anderson,C.,Muller,K.-R., Schlogl,A., 10.1038/srep33807.
| and Krusienski, |             | D.  | Bci     | meeting    | 2005-workshop | on       |                                   |     |             |         |               |     |       |
| --------------- | ----------- | --- | ------- | ---------- | ------------- | -------- | --------------------------------- | --- | ----------- | ------- | ------------- | --- | ----- |
|                 |             |     |         |            |               |          | Song,Y.,Zheng,Q.,Liu,B.,andGao,X. |     |             |         | Eegconformer: |     |       |
| bci signal      | processing: |     | feature | extraction | and           | transla- |                                   |     |             |         |               |     |       |
|                 |             |     |         |            |               |          | Convolutional                     |     | transformer | for eeg | decoding      | and | visu- |
tion. IEEE Transactions on Neural Systems and Re- alization. IEEE Transactions on Neural Systems and
| habilitation |     | Engineering, |     | 14(2):135–138, | 2006. | doi: |                |     |              |             |     |       |      |
| ------------ | --- | ------------ | --- | -------------- | ----- | ---- | -------------- | --- | ------------ | ----------- | --- | ----- | ---- |
|              |     |              |     |                |       |      | Rehabilitation |     | Engineering, | 31:710–719, |     | 2023. | doi: |
10.1109/TNSRE.2006.875637.
10.1109/TNSRE.2022.3230250.
| Mizrahi,               | D., Bachmann, |                                  | R., | Kar, O.F.,              | Yeo, T., | Gao, M., |                      |                                 |     |                          |     |               |     |
| ---------------------- | ------------- | -------------------------------- | --- | ----------------------- | -------- | -------- | -------------------- | ------------------------------- | --- | ------------------------ | --- | ------------- | --- |
|                        |               |                                  |     |                         |          |          | Torres, E.           | P., Torres,                     | E.  | A., Herna´ndez-A´lvarez, |     | M.,           | and |
| Dehghan,A.,andZamir,A. |               |                                  |     | 4m: Massivelymultimodal |          |          |                      |                                 |     |                          |     |               |     |
|                        |               |                                  |     |                         |          |          | Yoo,S.G.             | Eeg-basedbciemotionrecognition: |     |                          |     | Asurvey.      |     |
| maskedmodeling.        |               | InThirty-seventhConferenceonNeu- |     |                         |          |          |                      |                                 |     |                          |     |               |     |
|                        |               |                                  |     |                         |          |          | Sensors,20(18),2020. |                                 |     | ISSN1424-8220.           |     | doi: 10.3390/ |     |
ralInformationProcessingSystems,2023.
s20185083.
| Nam, C. | S., Nijholt, |     | A., and | Lotte, | F. Brain–Computer |     |     |     |     |     |     |     |     |
| ------- | ------------ | --- | ------- | ------ | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Touvron,H.,Lavril,T.,Izacard,G.,Martinet,X.,Lachaux,
| InterfacesHandbook: |     |     | TechnologicalandTheoreticalAd- |     |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
M.-A.,Lacroix,T.,Rozie`re,B.,Goyal,N.,Hambro,E.,
| vances,CRCPress. |     |     | 2018. |     |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Azhar,F.,Rodriguez,A.,Joulin,A.,Grave,E.,andLam-
Obeid,I.andPicone,J. Thetempleuniversityhospitaleeg ple,G. Llama: Openandefficientfoundationlanguage
| datacorpus. |     | FrontiersinNeuroscience,10,2016. |     |     |     | ISSN | models,2023. |     |     |     |     |     |     |
| ----------- | --- | -------------------------------- | --- | --- | --- | ---- | ------------ | --- | --- | --- | --- | --- | --- |
| 1662-453X.  |     | doi: 10.3389/fnins.2016.00196.   |     |     |     |      |              |     |     |     |     |     |     |
Wang,J.,Zhao,S.,Luo,Z.,Zhou,Y.,Jiang,H.,Li,S.,Li,
Paraperas Papantoniou, F., Lattas, A., Moschoglou, S., T.,andPan,G. CBramod: Acriss-crossbrainfoundation
Deng,J.,Kainz,B.,andZafeiriou,S.Arc2face:Afounda- modelforEEGdecoding.InTheThirteenthInternational
ConferenceonLearningRepresentations,2025.
| tionmodelforid-consistenthumanfaces. |     |     |     |     | InProceedings |     |     |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
oftheEuropeanConferenceonComputerVision(ECCV),
Wei,X.,Faisal,A.A.,Grosse-Wentrup,M.,Gramfort,A.,
2024.
Chevallier,S.,Jayaram,V.,CamilleJeunet,S.B.,Ludwig,
Pavlov, Y. G., Kasanov, D., Kosachenko, A. I., and Ko- S.,Barmpas,K.,Bahri,M.,Panagakis,Y.,Laskaris,N.,
tyusov,A.I. ”eeg,pupillometry,ecgandphotoplethys- Adamos, D. A., Zafeiriou, S., Duong, W. C., Gordon,
mography,andbehavioraldatainthedigitspantaskand S.M.,Lawhern,V.J.,S´liwowski,M.,Rouanne,V.,and
rest”,2022. Tempczyk,P.2021beetlcompetition:Advancingtransfer
10

AreLargeBrainwaveFoundationModelsCapableYet?InsightsfromFine-Tuning
| learning | for subject independence | & heterogenous | eeg |
| -------- | ------------------------ | -------------- | --- |
datasets,2022.
| Xu,T.,Zhou,Y.,Wang,Z.,andPeng,Y.      |                               | Learningemotions |      |
| ------------------------------------- | ----------------------------- | ---------------- | ---- |
| eeg-basedrecognitionandbrainactivity: |                               | Asurveystudy     |      |
| onbciforintelligenttutoringsystem.    |                               | ProcediaComputer |      |
| Science,                              | 130:376–382, 2018.            | ISSN 1877-0509.  | doi: |
| j.procs.2018.04.056.                  | The9thInternationalConference |                  |      |
onAmbientSystems,NetworksandTechnologies(ANT
2018)/The8thInternationalConferenceonSustainable
EnergyInformationTechnology(SEIT-2018)/Affiliated
Workshops.
11