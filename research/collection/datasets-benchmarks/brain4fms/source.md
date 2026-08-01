| Brain4FMs: |     | A Benchmark |     | of Foundation |     | Models | for Electrical |     |
| ---------- | --- | ----------- | --- | ------------- | --- | ------ | -------------- | --- |
Brain Signals
|     | FanqiShen            |     |     | EnhongYang         |     |     | JiaheLi            |     |
| --- | -------------------- | --- | --- | ------------------ | --- | --- | ------------------ | --- |
|     | shenfanqi@zju.edu.cn |     |     | yeh1115@zju.edu.cn |     |     | jiaheli@zju.edu.cn |     |
|     | ZhejiangUniversity   |     |     | ZhejiangUniversity |     |     | ZhejiangUniversity |     |
Hangzhou,Zhejiang,China Hangzhou,Zhejiang,China Hangzhou,Zhejiang,China
|     | JunruChen |     |     | XiaoranPan |     |     | ZhizhangYuan |     |
| --- | --------- | --- | --- | ---------- | --- | --- | ------------ | --- |
jrchen_cali@zju.edu.cn panxiaoran@zju.edu.cn zhizhangyuan@zju.edu.cn
|     | ZhejiangUniversity |     |     | ZhejiangUniversity |     |     | ZhejiangUniversity |     |
| --- | ------------------ | --- | --- | ------------------ | --- | --- | ------------------ | --- |
6202 beF 21  ]GL.sc[  1v85511.2062:viXra
Hangzhou,Zhejiang,China Hangzhou,Zhejiang,China Hangzhou,Zhejiang,China
|     |     |                                | LiMeng |     | YangYang                |     |     |     |
| --- | --- | ------------------------------ | ------ | --- | ----------------------- | --- | --- | --- |
|     |     | limeng.braindecoder@gmail.com  |        |     | yangya@zju.edu.cn       |     |     |     |
|     |     | ShanghaiInstituteofMicrosystem |        |     | ZhejiangUniversity      |     |     |     |
|     |     | andInformationTechnology,CAS   |        |     | Hangzhou,Zhejiang,China |     |     |     |
Shanghai,China
Abstract advances in neurological disease detection [86] and sleep stag-
BrainFoundationModels(BFMs)aretransformingneuroscience ing[2],thestudyofneuralmechanismsdrivesparadigmsinhuman-
byenablingscalableandtransferablelearningfromneuralsignals, technologyinteraction,includingneuralcommunication[79]and
advancingbothclinicaldiagnosticsandcutting-edgeneuroscience affectivecomputing[118].Electroencephalography(EEG)andin-
tracranialEEG(iEEG)providemillisecondtemporalresolution,high
exploration.Theiremergenceispoweredbylarge-scaleclinical
fidelityanddirectmeasurementsofneuralelectricalactivity.
recordings,particularlyelectroencephalography(EEG)andintracra-
Deeplearninghasemergedasapowerfultoolforneuralsig-
nialEEG,whichproviderichtemporalandspatialrepresentations
ofbraindynamics.However,despitetheirrapidproliferation,the nalanalysis,witharchitecturessuchasCNNs,LSTMs,andGNNs
fieldlacksaunifiedunderstandingofexistingmethodologiesand achievingpromisingresultsindecodingtasks[27,55,83].However,
relianceonsmall,task-specificlabeleddatasetslimitsgeneraliza-
astandardizedevaluationframework.Tofillthisgap,wemapthe
tion,giventhehighcostofannotationandinter-subjectvariability.
benchmarkdesignspacealongtwoaxes:(i)fromthemodelper-
Toovercometheselimitations,self-supervisedlearning(SSL)lever-
spective,weorganizeBFMsunderaself-supervisedlearning(SSL)
taxonomy;and(ii)fromthedatasetperspective,wesummarizecom- agesunlabeledneuraldataforrepresentationlearning[34].This
mondownstreamtasksandcuraterepresentativepublicdatasets shiftparallelsadvancesinNaturalLanguageProcessing(NLP)[21]
andComputerVision(CV)[24],wherelarge-scalepretrainingen-
acrossclinicalandhuman-centricneurotechnologyapplications.
abledfoundationmodels.Asimilartransitionisemerginginneuro-
Buildingonthisconsolidation,weintroduceBrain4FMs,anopen
science,withBrainFoundationModels(BFMs)servingasuniversal
evaluationplatformwithplug-and-playinterfacesthatintegrates15
representativeBFMsand18publicdatasets.Itenablesstandardized encodersthatlearnrobustrepresentationsacrosssubjectsandsup-
comparisonsandanalysisofhowpretrainingdata,SSLstrategies, portefficientadaptationtodownstreamtasks(Figure1).
|                   |        |                |                |         | Recent surveys | review | BFMs from pretraining, | architectural, |
| ----------------- | ------ | -------------- | -------------- | ------- | -------------- | ------ | ---------------------- | -------------- |
| and architectures | affect | generalization | and downstream | perfor- |                |        |                        |                |
andapplicationperspectives[3,51,56,120].However,aunified
mance,guidingmoreaccurateandtransferableBFMs.Thecodeis
SSL-centric,formulation-basedperspectiveforsystematicallyor-
availableathttps://anonymous.4open.science/r/Brain4FMs-85B8.
|     |     |     |     |     | ganizing methods | and enabling | principled comparison | remains |
| --- | --- | --- | --- | --- | ---------------- | ------------ | --------------------- | ------- |
CCSConcepts lacking.Existingbenchmarksarealsolimited,astheyeitherfocus
onspecifictasks[20,61]orlackcomprehensivecoverageofdatasets
•Computingmethodologies→Machinelearning;•Applied
andmodels[101,104].Tobridgethesegaps,weproposeaunified
computing→Healthinformatics.
operator-basedformulationforSSLpretraining(Figure1a),and
Keywords introduceacross-taskbenchmarkwithcross-subjectfinetuningfor
standardizedevaluation.Themaincontributionsofthispaperare:
BrainFoundationModel,Electroencephalography,Self-Supervised
Learning,BenchmarkingandEvaluation 1) UnifiedTaxonomyofSSLMechanisms.Wepresentanup-to-
date,SSL-centrictaxonomyforBFMsbyabstractingmethodsinto
1 Introduction aunifiedobjectiveandcategorizingthemintothreeparadigms,
enablingsystematiccomparisonoflearningmechanisms.
ExtensiveBenchmarkforBFMsEvaluation.Weconstructan
| Neuroscienceisfundamentaltounderstandingthebrainandtrans- |     |     |     |     | 2)  |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
lating insights into societal impact. Beyond supporting clinical openbenchmarkcovering11downstreamtasksacross18EEGand

Shenetal.
Figure1:OverviewofBFMs.(a)Aunifiedpretrainingpipeline.EEG/iEEGrecordingsarepreprocessed,encodedintolatentrepresentations,
andoptimizedunderdifferentSSLparadigms.(b)Modelscalestatistics.Parameter-sizebucketsbytrainingparadigmareshownforthe
reportedsubset,usingeachmodel’smaximumparametercount,alongsideyearlymodelcountsunderthesamegrouping.(c)Timeline-style
familytreeofrepresentativeBFMsfrom2021to2025,organizedbyparadigmandannotatedwithmajormethodologicalshifts.
iEEGpublicdatasets,enablingconsistentcomparisonthrougha maskingoperator,whileN isthenegativesetwhencontrastive
standardizedpreprocessingandevaluationpipeline. objectivesareemployed.Basedonthisformulation,wecategorize
3) SystematicAnalysis.Weperformacomprehensivestudyon15 BFMspretrainingstrategiesintothreeSSLparadigms.Wefocus
BFMs, analyzing how pretraining data, training strategies, and ontheunderlyinglearningmechanismsinthissection,anddefer
architecturesaffectgeneralizationanddownstreamperformance. detailedmodelinstantiationsanddevelopmentstoAppendixA.
2 ModelTaxonomy
|     |     |     |     |     | 2.1 | Contrastive-basedMethods |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- |
EEGandiEEGarenaturallymodeledasmultivariatetimeseries.We Contrastive-basedSSLdefineslearningobjectivesbycomparing
denotearecordingas𝑋 ∈R𝐶×𝑁,where𝐶isthenumberofchannels representationsofpairedinputsandcontrastingthemagainstaset
and𝑁 =𝑓 𝑠×𝑡isthenumberofsamplesoverduration𝑡atsampling ofnegatives.Thisparadigmcanbeexpressedas:
| rate𝑓 𝑠.Forelectrode-wiserepresentations,let𝜖 |     |     | ⊆{1,...,𝐶}bea |     |     |     |     |                |     |     |
| --------------------------------------------- | --- | --- | ------------- | --- | --- | --- | --- | -------------- | --- | --- |
|                                               |     |     |               |     |     |     | L𝐶  | =L(G(𝑧 ),𝑧 ,N) |     | (2) |
subsetofelectrodeswith𝐸 =|𝜖|.Thecorrespondingmultivariate 1 2
𝑒
timeseriesis𝑥𝑒 ∈R𝐸𝑒×𝑁.Wecategorizepretrainingpipelinesinto where𝑧 = F (T𝑑,𝑠(X𝑠𝑟𝑐 ,M)) and𝑧 = F (T𝑑,𝑠(X𝑡𝑔𝑡)), F (·)
|     |     |     |     |     |          | 1       | 1              | 2        | 2              | 1     |
| --- | --- | --- | --- | --- | -------- | ------- | -------------- | -------- | -------------- | ----- |
|     |     |     |     |     | produces | a query | representation | from the | causal context | while |
patch-levelandsequence-levelformulations.Inpatch-levelmodel-
|                   |                                        |     |     |     | F (·)generatesthetargetembeddingfromafuturesegment.The |     |     |     |     |     |
| ----------------- | -------------------------------------- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- |
| ing,therawsignal𝑋 | ispartitionedalongthetemporaldimension |     |     |     | 2                                                      |     |     |     |     |     |
into𝑘non-overlappingwindowsoflength𝑤 = 𝑁 .Objectivesare projectionheadG(·)mapsrepresentationsintoalatentspace.The
|     |     |     | 𝑘   |     | losscontraststhepositivepair(𝑧 |     |     | ,𝑧                            |     |     |
| --- | --- | --- | --- | --- | ------------------------------ | --- | --- | ----------------------------- | --- | --- |
|     |     |     |     |     |                                |     |     | 1 2 )withnegativesN,promoting |     |     |
definedatthepatchgranularity,andpatchesaretypicallytreated
alignmentofmatchedpairsandseparationfrommismatches.
asexchangeabletokens.Sequence-levelmodelingpreservesthe
temporalstructureandtreatstheinputasanorderedsequence.
|     |     |     |     |     | 2.1.1 | AugmentationContrast. |     | Augmentation-basedmethodcon- |     |     |
| --- | --- | --- | --- | --- | ----- | --------------------- | --- | ---------------------------- | --- | --- |
SSLderivestrainingsignalsfromthedata,enablingpretraining
structspositivepairsbyapplyingtransformationstothesameinput.
| without manual | annotations. | Most SSL methods | can be | viewed |               |     |                                         |     |     |     |
| -------------- | ------------ | ---------------- | ------ | ------ | ------------- | --- | --------------------------------------- | --- | --- | --- |
|                |              |                  |        |        | Givenaninput𝑥 |     | 𝑖 ∈X𝑠𝑟𝑐,twoaugmentedviewsaregeneratedas |     |     |     |
a s o p t i m i zi ng an o bj e c ti v e co ns tr u c te d fr o m tr a ns fo r m ati o n s a n d 𝑥 1 =T𝑠 (𝑥 𝑖)and𝑥 2 =T𝑠 (𝑥 𝑖),whereT𝑠 isanaugmentationoper-
|     |     |     |     |     | 𝑖   | 1   | 𝑖 2 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
p re d i c t io n m od ul es a p p l ie d to th e i n p ut s ig na l. W e f o rm t w o s e t s atordesignedtopreserveneuralsemantics.Thepositivepairis
f ro m i n p u t ,a so u rc e se t X 𝑠𝑟 𝑐 a n d a ta r g e t s e t X 𝑡 𝑔 𝑡 . A n e n c o d e r F ( · ) (𝑥 1 ,𝑥 2) N T𝑠 ( 𝑥 )
|     |     |     |     |     | 𝑖 𝑖 | , w h il en e | ga ti v e s | a r e o b t a i n e d | fr o m s a m p le s | 𝑗 w i th |
| --- | --- | --- | --- | --- | --- | ------------- | ----------- | --------------------- | ------------------- | -------- |
m a ps t h e i n pu t to a 𝑑 -d i m e n si o n al la t e n t r e p r e s e n t at io n , f o l lo w e d 𝑥 𝑗 𝑖
|                |        |                         |              |     | 𝑗 ∈ X | 𝑠 𝑟 𝑐 an d ≠ | . F o r ne | u r a l s i g n a l s, | e ff ec t iv e a u gm | e n t a t io n s |
| -------------- | ------ | ----------------------- | ------------ | --- | ----- | ------------ | ---------- | ---------------------- | --------------------- | ---------------- |
| by an optional | module | G(·) that serves either | as a decoder | for |       |              |            |                        |                       |                  |
mustretainphysiologicallymeaningfulpatternsratherthanin-
reconstructionorasapredictionoralignmenthead.Underthis troducingarbitraryperturbations.Beyondstandardtime-domain
formulation,SSLmethodscanbeexpressedwithaunifiedobjective: perturbations(e.g.,jittering,scaling,andtemporalshifts),workex-
| L   | =L(G(Q(F(T𝑑,𝑠(X𝑠𝑟𝑐),M))),F(T𝑑,𝑠(X𝑡𝑔𝑡)),N) |     |     | (1) |     |     |     |     |     |     |
| --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sum ploresfrequency-domaintransformationsthatselectivelysuppress
=Φ 𝑑◦𝑎
Here,T𝑑,𝑠 𝑠 denotesadeterministictransformcomposed orinjectspectralcomponents[58,115]aswellasviewconstruction
ofdomainmappingΦ
𝑑 andaugmentation𝑎 𝑠.ThetokenizerQ(·) formultichannelrecordings[71,105].Recentworkenforcessubject-
discretizescontinuouslatentrepresentations.AndM denotesa levelconsistencyviasame-subjectrepresentationalignment[94].

Brain4FMs:ABenchmarkofFoundationModelsforElectricalBrainSignals
2.1.2 ContrastivePredictiveCoding. ContrastivePredictiveCoding AE-basedBFMsevolvefrommaskedreconstructioninthetime
(CPC)[80]formulatescontrastiveobjectivesoverorderedrepre- domain[18,35,41,91]todomain-awaremaskingstrategiesoperat-
sentations.InCPC-basedpretraining,anencoderproducesacon- inginspectralorlatentspace[10,90,99,100,107,113].Tobetter
textrepresentation𝑐 𝑖 = F (T𝑑,𝑠(X𝑠𝑟𝑐 ,M)),whereF (·) encodes handlemulti-electroderecordings,modelsincorporatespatialinduc-
|     |     | 1   |     | 1   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
observationsandaggregatespastinformationintoacontextual tivebiasesthroughchanneldictionaries,positionalencodings,or
state.Conditionedon𝑐 𝑖,themodelextractsatargetrepresenta- graph-structuredconnectivity,enablingmodelingofcross-channel
| tion𝑧 =F | (T𝑑,𝑠(X𝑡𝑔𝑡))fromafuturesegment.Projectionoperator |     |     |     |     |     |     |     |     |
| -------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑖 2 topology[17,25,81,93].Transformerbackbonesareincreasingly
maps𝑐
G(·) 𝑖 into a latent space, where a contrastive objective adoptedtocapturelong-rangetemporaldependenciesandspatial
alignsthecontextwithfuturerepresentation𝑧
|     |     |     | 𝑖 whilecontrasting |     | interactions | [23, 60, 92], and | masked learning | has been | further |
| --- | --- | --- | ------------------ | --- | ------------ | ----------------- | --------------- | -------- | ------- |
itagainstnegatives.CPC-basedBFMsrangefromsequence-level scaledtoiEEGandlarge-populationdatasets[31,90,107,112].
modeling[49,122]tospatio-temporalarchitectures[13]. RecentBFMsfurtherdiscretizeEEG/iEEGsignalsintotokense-
quencesviacodebookquantization,bridgingautoencodingwith
| 2.1.3 Cross-modalContrast. |     | Cross-modalcontrastivelearningaligns |     |     |     |     |     |     |     |
| -------------------------- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
token-basedgenerativemodeling.Thislineofworkprogressesfrom
representationsderivedfromcomplementaryviewsormodalities
directtemporalquantization[9]topretrainedVQ-VAEtokeniz-
thatreflectthesameneuralstate.InEEG/iEEG,twoviewsarecon- ers[16,39,40],andtowardmorestructuredcodebooks,including
structedviathecompositetransformT(·)andassignedas𝑥
|     |     |     |     | 𝑚 ∈ | time–frequencydualtokenizers[67],topology-awarehierarchical |     |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------------- | --- | --- | --- | --- |
1
X𝑠𝑟𝑐 and𝑥 𝑚 ∈X𝑡𝑔𝑡.Featuresareextractedusingmodality-specific VQ-VAEvariants[106],andresidualcodebooks[10].Codebooks
2
| encodersF | (·)andF (·).Unidirectionalalignmentisadoptedby |                      |     |                 |                                                          |     |     |     |     |
| --------- | ---------------------------------------------- | -------------------- | --- | --------------- | -------------------------------------------------------- | --- | --- | --- | --- |
|           | 1 2                                            |                      |     |                 | areobjective-agnosticandcanalsopairwithnon-AEobjectives. |     |     |     |     |
| freezing  | the target branch                              | with a stop-gradient |     | operator 𝑠𝑔[·]. |                                                          |     |     |     |     |
2.3 OtherAdvancedMethods
| Cross-modal | BFMs range | from contrasting | multiple | EEG/iEEG- |     |     |     |     |     |
| ----------- | ---------- | ---------------- | -------- | --------- | --- | --- | --- | --- | --- |
derivedviews[50,95]toaligningheterogeneousbiosignals[87,
BeyondtheSSLparadigmsdiscussedabove,BFMsexploreexplicit
111],andfurthertoEEG/iEEG–multimodalalignment[26,28].
predictiveobjectives,hybridformulations,andpost-SSLinstruction
tuning.Thesemethodsextendthepretrainingframeworkalong
2.2 Generative-basedMethods
dimensionsofsupervision,objectivedesign,andtaskalignment.
Generative-basedSSLformulatespretrainingobjectivesbyrecon-
|     |     |     |     |     | 2.3.1 | ExplicitPredictive-based. | Explicitpredictive-basedmethods |     |     |
| --- | --- | --- | --- | --- | ----- | ------------------------- | ------------------------------- | --- | --- |
structingorpredictingstructuredtargetsfromtransformedinputs,
learnrepresentationsbypredictingpredefined,interpretableat-
avoidingexplicitpairconstructionandnegativesampling[113].
tributesofthesignalderivedfromT𝑑,𝑠(·),suchastemporalorder,
ThisparadigmhasbecomeincreasinglyprevalentinrecentBFMs.
Givenatransformedinput T𝑑(𝑥),anencoder F𝜃 (·) producesa channelconfiguration,orfuturepatterns.Thesepretexttasksim-
1
continuouslatentrepresentation𝑧 =F𝜃 (T𝑑(𝑥 𝑖))where𝑥 ∈X𝑠𝑟𝑐. posesupervised-likeobjectivesgroundedinintrinsicsignalstruc-
|     |     | 𝑖   | 1   | 𝑖   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AlearnablecodebookQ𝜃 (·)discretizes𝑧 ture.Thegeneralformofthelossisgivenby:
𝑖 intoalatentembedding,
3
whichisthenprocessedbyadecoderG𝜃 (·)toreconstructatarget L =L(G𝜃2 (F𝜃1 (X𝑠𝑟𝑐 ,M)),T𝑑,𝑠(𝑥)) (4)
|     |     |     | 2   |     |     | ep  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
vieworpredictfuturecontent.Theobjectiveisdefinedas:
|     |     |     |     |     | whereG𝜃 | (·)denotesatask-specificpredictionhead,andMis |     |     |     |
| --- | --- | --- | --- | --- | ------- | --------------------------------------------- | --- | --- | --- |
2
L𝐺 =L(G𝜃2 (Q𝜃3 (F𝜃1 (T𝑑(𝑥 𝑖),M))),F𝜃1 (T𝑑(𝑥 𝑖))) (3) anoptionalmaskingoperator.InEEG/iEEGapplications,predictive
|     |     |     |     |     | targets | are often designed | to reflect neurophysiological |     | proper- |
| --- | --- | --- | --- | --- | ------- | ------------------ | ----------------------------- | --- | ------- |
Byminimizingthereconstructionorpredictionloss,themodel
ties[43,89].Suchobjectivesrelyonpredefinedpredictivetargets
learnslatentrepresentationsthatretaininformationnecessaryto
andarethereforetiedtospecificassumptionsaboutsignalstructure.
recovertheunderlyingsignalstructure.
2.3.2 Hybrid-based. HybridSSLcombinesmultipleself-supervised
| 2.2.1 Autoregressive-based. |     | Autoregressive(AR)modelinglearns |     |     |     |     |     |     |     |
| --------------------------- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- |
objectiveswithinaunifiedframeworktoexploitcomplementary
representationsbycausalpredictionoverorderedsequences[44].In learningsignals[97].RecentBFMscouplecontrastiveobjectives
BFMs,neuralsignalsarecastastokensequences,andlearningpro- withgenerativemodelingtojointlycapturecross-viewconsistency
ceedsvianext-tokenpredictionfrompastcontext.Givenanindex andsignalstructure[14,52,54,91,96].Otherapproachesintegrate
𝑖andapredictionwindowoflength𝑘,futuretokensarepredicted
reconstructionwithautoregressivepredictiontomodelbothsignal
| fromthecausalcontext𝑥 |     | ∈X𝑠𝑟𝑐 underacausalconstraint.AR- |     |     |                                                          |     |     |     |     |
| --------------------- | --- | -------------------------------- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- |
|                       |     | ≤𝑖                               |     |     | structureandtemporaldynamics[38,106],andmayfurtherincor- |     |     |     |     |
basedBFMsprogressfrompatch-levelpredictionwithGPT-stylede-
porateadversarialobjectivesfordomain-awarealignment[39,53].
coders[19,63]toricherspatio-temporalmodelingforcross-channel
dependencies[70,98,108,119].Recentworkfurtherincorporates 2.3.3 Instruction-tuned. Instructiontuningisnotaself-supervised
prompt-basedconditioningforin-contextlearning[59]. paradigm,butistypicallyappliedafterSSLpretrainingasasu-
pervisedalignmentstagetosupportmulti-taskdecoding.Inthis
2.2.2 Autoencoder-based. Autoencoder-basedmethodslearnrep- setting,EEG/iEEGfeaturesaremappedtoLLM-compatibletokens
resentationsbyreconstructingtransformedinputsthroughanen- throughanadapterortokenizerQ𝜃
,andapretrainedlanguage
coder–decoderarchitecture[68]andarewidelyusedinBFMs[47]. generatestaskoutputs𝑦conditionedonpromptsP: 2
modelG𝜃
|     | F (· ) | 𝑥   |     |     |     | 3   |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
A n en c o d e r 𝜃 m a p s t h e i n p u t 𝑖 or a n o p ti o na l tr a n s fo r m e d (X𝑠𝑟𝑐)),P),𝑦)
|           | (𝑥 1                     |                           |              |                         |     | L𝑖𝑡 =L(G𝜃2 | (Q𝜃3 (F𝜃1 |     | (5) |
| --------- | ------------------------ | ------------------------- | ------------ | ----------------------- | --- | ---------- | --------- | --- | --- |
| vi ew T 𝑑 | 𝑖 ) ) in t o a l ate n t | c o d e , a n d th e n de | c od e d b y | G 𝜃 ( ·) t o r e co n - |     |            |           |     |     |
2
structatargetview.Thereconstructionobjectiveencouragesthe Existingdesignsmainlydifferinthechoiceoftokenizationstrate-
latentspacetopreserveinformationrequiredforsignalrecovery. gies,alignmentschemes,andpromptformulations[14,37,39,109].

Shenetal.
3 Benchmark 3.2 DatasetConstruction
Topromotestandardizedandreproducibleevaluation,weintroduce Brain4FMspresentsacomprehensivebenchmarkcovering18public
Brain4FMs,acomprehensivebenchmarkforBFMs-basedelectri- datasetsacross11tasks,groupedintofourcategories:diseasediag-
calbrainsignalclassification.Itintegrates15BFMsand18public nosis,sleepstaging,communication[114],andaffectivecomputing.
datasetsforsystematiccross-taskassessment,andprovidesplug- Table2summarizeswidelyuseddatasetsthatsupportcross-subject
and-playinterfacesforaddingnewmodelsanddatasets. evaluationandcompriseEEGoriEEGrecordingscollectedacross
diverseexperimentalsettings.Mostdatasetsaredisjointfromthe
3.1 Pipeline pretrainingcorporaoftheevaluatedBFMs.Pretrainingsources,
limitedoverlap,anddatasetstatisticsareprovidedinAppendixB.
Thebenchmarkfocusesonclassificationtasks,whichaimstodi-
videtheinputelectricalbrainsignalsamples𝑋 =𝑥 1 ,𝑥 2 ,...,𝑥 𝑛into 3.2.1 DiseaseDiagnosis. Neurologicaldisordersareamajorglobal
pre-definedcategories𝐶 =𝑐 1 ,𝑐 2 ,...,𝑐 𝑚,where𝑥 𝑖representsthei-th healthburden,representingtheleadingcauseofdisabilityandthe
sample,𝑚isthenumberofcategories,and𝑐 𝑖 ′ ispredictedlabels. second leading cause of death worldwide [57]. To support clin-
Theevaluationpipelineisorganizedintotwostages:dataprepro- ically relevant evaluation, Brain4FMs groups disease diagnosis
cessing,followedbymodelfinetuningandevaluation(Figure2b). tasks,includingEpilepsy,drug-resistantepilepsy(DRE),Parkin-
Preprocessingincludesbandpassandnotchfiltering,downsampling, son’sDisease(PD),Depression,MajorDepressionDisorder(MDD),
event-alignedwindowsegmentation,channelselection,andper- SchizophreniaDisease(SD),AttentionDeficitHyperactivityDisor-
channelz-scorenormalization.Then,useBFMswithpre-trained der(ADHD)andAlzheimer’sDisease(AD).Thesetasksalignwith
weightsasthemainbackbonemodel𝑀toextracthiddenfeatures
realclinicalobjectives,featuringcross-subjectsplitsandclinically
𝑧 𝑖,andfine-tunethemodelwithtask-specificclassifiers𝐶𝑙𝑠:
groundedlabelstoenablerobust,generalizableevaluation.
𝑧 𝑖 =𝑀(𝑥 𝑖);𝑐 𝑖 ′=𝐶𝑙𝑠(𝑧 𝑖) (6) 3.2.2 SleepStaging. Sleepstagingsupportsthediagnosisandtreat-
Weadoptacross-subjectleave-subjects-outprotocolwithtrain/ mentofsleepdisorders.Manualscoringofovernightrecordingsis
valid/testsplitsofapproximately3:1:1,ensuringnodataleakage. labor-intensiveandtime-consuming,motivatingautomaticsleep
Thissetupenforcesgeneralizationtounseensubjectsandiscritical stageclassification[2].Thetaskrequiresmodelinglong-duration
forclinicalapplicabilityinneuroscience[107].Modelsareevaluated signalsandcapturingrichtime–frequencystructure,makingrobust
viagroup-wisecross-validation,withresultsreportedasthemean long-rangetemporalmodelingessential.
performanceacrossalltestfoldsforreliablecomparison.
3.2.3 Communication. Communicationmapsneuralactivityto
AssummarizedinTable1,Brain4FMsincludes15BFMsspanning
externaloutputs,enablingintentexpressionforuserswithsevere
diversepretrainingstrategiesandevaluatesthemsystematically
motor impairments. Typical tasks include Motor Imagery (MI),
acrossdatasets.Allmodelsaretestedunderidenticalprotocols,en-
MotorExecution(ME)anddecodingspeechorsemanticintent,
ablingfairandcomprehensivecomparisonacrossneuraldecoding
translatingbrainsignalsintosymbolicoutputsforspelling,typing,
tasksandsupportingrobustnessassessmentacrosssubjects.The
orcommandselection.
includedBFMsarechosenfromacceptedorhighlycitedworks
withpubliccodeandpretrainedweights. 3.2.4 Affective Computing. Affective computing infers internal
emotionalandcognitivestatesfromEEGoriEEG.Coretasksinclude
emotionrecognitionandmentalworkloadestimation(MW),which
Table1:Overviewofbenchmarkmodels,includingSSLstrategies, rely on time–frequency and spatial patterns to capture arousal,
BFMsparameters,pretrainingdatamodalitiesandfeaturedomain. valence,andcognitivedemandacrossdiversesettings.
3.3 CentralizedBenchmarkingResults
Name Strategy Param Modality Domain
Contrastive-basedMethod We evaluate 22 downstream classification tasks from 18 public
SppEEGNet[58] Aug. 138K EEG time datasets,assomedatasetscontainmultiplesubtasks.Standardmet-
BIOT[105] Aug. 3.19M EEG time,frequency ricsarereported,includingAccuracy,AUROC,F1,F2,andCohen’s𝜅,
Bendr[49] CPC 3.97M EEG time,frequency withfullresultsprovidedinAppendixD.Inourtables,C/G/O/Adv.
MBrain[13] CPC 8.34M EEG/iEEG time,frequency,space
denoteContrastive/Generative/Other/Adversarialmethods,while
Generative-basedMethod
Aug./Hyb./CBindicateaugmentation/hybrid/codebookapproaches.
Brant[112] AE 196.10M iEEG time,frequency,space Performancevariessignificantlyacrosstasks,withnosingleBFMs
BFM[9] AE 708.96M EEG time
consistentlyoutperformingothers.Tointerpretthesedifferences
Brainbert[90] AE 43.18M iEEG time,frequency
CBraMod[92] AE 4.88M EEG time,frequency,space andinformfuturedevelopment,weorganizeouranalysisalonga
NeuroGPT[19] AR 79.62M EEG time,frequency typicalpipeline,frompretrainingdataandSSLstrategiestomodel
LaBraM[40] AE 5.80M EEG time,frequency,space
designwithafocusonspatialorfrequencystructureanddiscrete
BrainWave[107] AE 102.13M EEG+iEEG time,frequency,space
REVE[81] AE 69.19M EEG time,space representations.Thismotivatesthefivequestionsbelow:
BrainOmni[103] AE 32.71M EEG time,frequency,space
Q1: HowdodatacompositionandmodalityaffectBFMsperformance?
OtherAdvancedMethod
Q2: HowdoSSLstrategiescorrelatewithcross-taskperformance?
EEGPT-1[91] G&C 51.04M EEG time,space Q3: DoBFMslearntask-relevantspatialstructure?
NeuroLM[39] G&Adv. 169.60M EEG time,frequency
Q4: HowisfrequencyinformationrepresentedinBFMsacrosstasks?

Brain4FMs:ABenchmarkofFoundationModelsforElectricalBrainSignals
Figure2:Overviewofbenchmarkpipeline.(a)Dataacquisitionscenarioscoveringsleepstaging,affectivecomputing,diseasediagnosis,
andcommunication.(b)Evaluationundercross-subjectandcross-validationprotocols,withastandardizedEEG/iEEGpreprocessingpipeline.
Q5: DocodebookdiscretizationstrategiesbenefitBFMs? stagingbenchmarks,BFMsexhibitstrongercross-subjecttransfer
underunifiedevaluationprotocols.Supervisedbaselinescanbe
3.3.1 Q1:HowdodatacompositionandmodalityaffectBFMsperfor-
competitivebuttypicallyoutperformonlyasubsetofBFMs.In
mance? Fromadataperspective,aprimaryfactoristhemodality
epilepsy,SPaRCNetoutperformsSppEEGNet,NeuroLM,andBFM
| of the pretraining | corpus. On | epilepsy datasets | (Table | 3),iEEG- |     |     |     |     |     |
| ------------------ | ---------- | ----------------- | ------ | -------- | --- | --- | --- | --- | --- |
inbothAUROCandaccuracy,whilemostBFMsstillachievehigher
pretrainedmodelstendtoperformbetteroniEEGcohorts,while overallperformance.CCNSEachievesmoderateAUROCbutlow
EEG-pretrainedmodelsfavorEEGdatasets.Forexample,Brant,
accuracy,indicatinglimitedcalibration.Incontrast,ondepression
pretrainedoniEEG,achievesstrongperformanceonMAYOand
datasetssuchasMDD-64,DeprNetremainsastrongbaselinebutis
FNUSAwithhighAUROCandAccuracy,butdegradesmarkedlyon
surpassedbyseveralBFMs(e.g.,REVE,BrainOmni,andBrainWave).
CHBMIT,revealingpronouncedmodalitydependence.Bycontrast,
Overall,theseresultsindicatethatlarge-scalepretrainingyields
BrainWave,pretrainedjointlyonEEGandiEEG,remainsrobust more transferable representations than task-specific supervised
acrosssettings,consistentwithimprovedtolerancetodomainshift.
traininginmostclinicaldiagnosissettings.
| Task-specific | supervised | baselines are | provided | as reference |     |     |     |     |     |
| ------------- | ---------- | ------------- | -------- | ------------ | --- | --- | --- | --- | --- |
Communicationandaffectivecomputingremainchallenging
points:SPaRCNet[42]forepilepsy,DeprNet[85]fordepression,
forcross-subjectgeneralization[65]duetostrongnon-stationarity
CCNSE[55]forsleepstaging,andMSCARNet[4]forcommuni-
andlargecross-subject/inter-sessionvariability(Table5).TheBCI-
cationandaffectivecomputing.Forcompleteness,wealsoreport tailoredsupervisedbaselineMSCARNetshowsstrongercross-subject
theirbestresultsonADHD,AD,andPDassupervisedreferences transferthanmostBFMs.AlthoughseveralBFMsshowimprove-
ratherthantask-optimizedbaselines.Regardingepilepsyandsleep
mentsonbenchmarks(e.g.,NeuroGPT),theiroveralltransferper-
formanceonconceptdecodingandemotionrecognitionremains
limited.Incontrast,MIandMWtasksaremoreseparable,enabling
Table2:Publicdatasetsusedinthebenchmark,includingsignal
modelssuchasREVEandNeuroGPTtoachievehigherAccuracy
type,numberofsubjects(Sub.),anddatasetcategory(Cat.),where
andAUROC,andBrainOmniperformsstronglyonEEGMMIDB.
Hdenoteshealthysubjects.
Table3:PrimaryperformancemetricsofBFMsonepilepsydatasets.
| Name | Signal | Task | Subject | Cat. |     |     |     |     |     |
| ---- | ------ | ---- | ------- | ---- | --- | --- | --- | --- | --- |
Weshowarepresentativesubsetacrossmethodtypes,C/G/O/SL
CHBMIT[30] EEG Epilepsy 23sub. 2 denotecontrastive/generative/other/supervisedmethods.
| MAYO[75]  | iEEG | DRE | 25sub. | 2   |     |     |     |     |     |
| --------- | ---- | --- | ------ | --- | --- | --- | --- | --- | --- |
| FNUSA[75] | iEEG | DRE | 14sub. | 2   |     |     |     |     |     |
Dep-BDI[36] EEG Depression 122sub. 2 Method MAYO FNUSA CHBMIT
| MDD-64[73] | EEG | MDD | 30H,43MDD | 2   |     |     |     |     |     |
| ---------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
SD-28[102] EEG SD 28sub. 2 Type Model AUROC Acc AUROC Acc AUROC Acc
UCSD[84] EEG PD 31H,15PD 2 C MBrain .92±.04 .92±.02 .91±.08 .87±.08 .71±.03 .73±.06
ADFD[69] EEG AD 88sub. 2 BIOT .90±.07 .88±.05 .87±.07 .83±.08 .56±.08 .29±.05
ADHD_Adult[7] EEG ADHD 42H37ADHD 2 SppEEGNet .56±.03 .75±.05 .64±.08 .67±.05 .43±.05 .60±.06
| ADHD_Child[72] | EEG | ADHD | 60H61ADHD | 2   |             |         |                 |         |                 |
| -------------- | --- | ---- | --------- | --- | ----------- | ------- | --------------- | ------- | --------------- |
|                |     |      |           |     | G BrainWave | .98±.01 | .93±.02 .92±.05 | .89±.06 | .90±.03 .80±.12 |
ISRUC[46] EEG SleepStage 100sub. 5 BrainBERT .97±.01 .94±.01 .90±.04 .89±.04 .78±.06 .75±.10
SleepEDFx[45] EEG SleepStage 44sub. 5 LaBraM .96±.02 .93±.02 .89±.08 .82±.10 .75±.10 .73±.10
|          |                        |     |        |     | Brant | .92±.03 | .82±.12 .87±.12 | .84±.07 | .55±.05 .70±.01 |
| -------- | ---------------------- | --- | ------ | --- | ----- | ------- | --------------- | ------- | --------------- |
| DEAP[48] | EEG EmotionRecognition |     | 32sub. | 4   |       |         |                 |         |                 |
SEED-IV[117] EEG EmotionRecognition 15sub. 4 BrainOmni .91±.06 .90±.02 .88±.07 .84±.05 .74±.13 .67±.19
|              |     |       |         |     | BFM     | .81±.08 | .68±.08 .78±.12 | .69±.11 | .74±.075 .72±.03 |
| ------------ | --- | ----- | ------- | --- | ------- | ------- | --------------- | ------- | ---------------- |
| EEGMat[123]  | EEG | MW    | 36sub.  | 2   |         |         |                 |         |                  |
|              |     |       |         |     | O EEGPT | .92±.03 | .90±.03 .90±.04 | .84±.06 | .71±.09 .67±.11  |
| EEGMMIDB[29] | EEG | MI&ME | 109sub. | 4   |         |         |                 |         |                  |
|              |     |       |         |     | NeuroLM | .64±.09 | .72±.16 .64±.14 | .72±.17 | .67±.06 .54±.20  |
| BCI-2a[11]   | EEG | MI    | 9sub.   | 4   |         |         |                 |         |                  |
Chisco[116] EEG ConceptClassification 5sub. 39 SL SPaRCNet .83±.10 .83±.08 .85±.10 .82±.11 .61±.10 .66±.05

Shenetal.
Figure3:Supplementalanalyses.(a)Boxplotsofdecision-boundarydiagnostics(q=0.10)comparingcontrastiveandgenerativemodels
oncross-subjecttasks.(b)AUROCofNeuroGPTvariantsacrosstasks.(c)SlopegraphofAUROCchangesfromoriginaltochannel-permuted,
comparingspatiallystrongandweakmodels.(d)HeatmapofSpearman’srankcorrelationbetweenband-wisepredictabilityandmodel
performancerankingsacrosstasks.Pointsin(a–c)denoten-foldcross-validationmeans;asterisksin(c-d)indicate*(p<0.05)and**(p<0.001).
These results suggest that current BFMs capture motor-related embeddingspacesandclassifierboundaries.Givenpredictedprob-
neuralpatternsmorereliablythanhigher-levelaffectiveorcommu- abilities𝑝(𝑥)andthemargin𝑚(𝑥)=𝑝 𝑖(𝑥)−𝑝 𝑗(𝑥),theboundary
|     |     |     |     | regionisdefinedasB𝑞 | =𝑥 |𝑚(𝑥) | <𝑄 𝑞(𝑚),where𝑄 | 𝑞(·)denotes |
| --- | --- | --- | --- | ------------------- | -------- | -------------- | ----------- |
nicativesemantics.Notably,evenmodelspretrainedwithemotion-
the𝑞-quantileofthemargindistribution.Relativetrendsremain
relateddata(e.g.,NeuroLM)mayperformcompetitivelyinwithin-
subjectsettingsbutstillstruggletogeneralizeacrosssubjects. stablefor𝑞 ∈0.05,0.10,0.20,𝑞=0.10isthereforeusedinthemain
text,withfullsensitivityanalysesreportedinAppendixE.The
3.3.2 Q2:HowdoSSLstrategiescorrelatewithcross-taskperfor-
|     |     |     |     | error-at-boundaryproportion𝐿𝑀 |     | andtheboundary-in-errors |     |
| --- | --- | --- | --- | ----------------------------- | --- | ------------------------ | --- |
𝐸𝑅
| mance? Aconsistentparadigm-associatedgapisobserved:contrastive- |     |     |     | proportion𝐿𝑀 |     |     |     |
| --------------------------------------------------------------- | --- | --- | --- | ------------ | --- | --- | --- |
𝐸𝑆 arethencomputedasfollows:
basedBFMstendtounderperformgenerative-basedonesonmost
downstreamtasksinthebenchmark(e.g.,seizuredetection,AD,
|     |     |     |     | |{𝑥 ∈ | B𝑞: 𝑦 ˆ( 𝑥 )≠𝑦(𝑥)}| | |{𝑥 ∈ B | 𝑞 : 𝑦ˆ (𝑥 ) ≠ 𝑦 ( 𝑥 )}| |
| --- | --- | --- | --- | ----- | ------------------- | ------- | ----------------------- |
SD,andPD).ThisgapcannotbeattributedsolelybytheSSLob- 𝐿𝑀𝐸𝑅= , 𝐿𝑀𝐸𝑆 =
|     |     |     |     |     | | B 𝑞 | | |{ 𝑥 : | 𝑦ˆ( 𝑥 ) ≠ 𝑦 (𝑥 ) } | |
| --- | --- | --- | --- | --- | ------- | ------ | -------------------- |
jective,asthemodelsalsodifferinpretrainingdata,architecture,
Toquantifyembeddingclusterstructure,theclass-separationratio
andscale.ToprobethepotentialroleofSSL,decision-boundary
𝑅 isadopted,definedastheaverageinter-classdistancedivided
| diagnosticsareconductedonthreerepresentativedatasets,com- |     |     |     | 𝑐𝑙𝑠 |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
paringcontrastiveandgenerativemodelsthroughanalysesoftheir bytheaverageintra-classdistance.Highervaluesindicatemore
compactclustersandgreaterseparationbetweenclasses.
|     |     |     |     | Across all | three datasets, a consistent | pattern | emerges. Con- |
| --- | --- | --- | --- | ---------- | ---------------------------- | ------- | ------------- |
Table4:AUROCandAccuracy(Acc)onME,MW,emotionrecog-
|     |     |     |     | trastivemodelsshowhigher𝐿𝑀 | 𝐸𝑅thangenerativemodels,indicat- |     |     |
| --- | --- | --- | --- | -------------------------- | ------------------------------- | --- | --- |
nitionandconceptdecodingdatasets.Chisco-Rresultsarereported ingmorefrequentmisclassificationinthelow-marginboundaryre-
withthreedecimalplacesforclarity.
gionandweakerdiscriminationnearthedecisionboundary.Genera-
tivemodels,inturn,achievemarkedlyhigher𝑅
𝑐𝑙𝑠,reflectingtighter
EEGMMIDB-R EEGMat DEAP Chisco-R within-classclustersandlargerinter-classseparation,correspond-
Model AUROC Acc AUROC Acc AUROC Acc Acc ingtoamoreseparablelatentgeometry.Notably,despitehigher
boundary-regionerrorrates,contrastivemodelsoftenpresentlower
| MBrain .52±.01 | .26±.01 .68±.06 | .75±.02 .51±.05 | .42±.04 .038±.004 |     |     |     |     |
| -------------- | --------------- | --------------- | ----------------- | --- | --- | --- | --- |
𝐿𝑀
BIOT .50±.01 .25±.01 .59±.08 .27±.01 .50±.03 .30±.06 .037±.003 𝐸𝑆,indicatingthattheirerrorsarelessconcentratednearthe
REVE .82±.00 .59±.01 .78±.09 .75±.08 .50±.05 .26±.05 .026±.003 boundary.Thissuggeststhatgenerativemodelsprimarilyfailon
NeuroGPT-E .77±.02 .54±.02 .70±.04 .73±.04 .49±.01 .42±.03 .047±.004 ambiguousborderlinesamples,whereascontrastivemodelsincur
| NeuroGPT-D .50±.00 | .25±.00 .51±.06 | .73±.01 .51±.03 | .44±.04 .048±.003 |     |     |     |     |
| ------------------ | --------------- | --------------- | ----------------- | --- | --- | --- | --- |
errorsfartherfromtheboundary,consistentwithlessstableglobal
| BrainOmni .74±.01 | .49±.01 .68±.07 | .60±.07 .45±.03 | .22±.03 .030±.009 |     |     |     |     |
| ----------------- | --------------- | --------------- | ----------------- | --- | --- | --- | --- |
geometryanddecisionsurfaces.ResultsaresummarizedinFig-
| CBraMod .57±.01 | .30±.02 .63±.06 | .72±.04 .51±.01 | .19±.02 .025±.009 |     |     |     |     |
| --------------- | --------------- | --------------- | ----------------- | --- | --- | --- | --- |
LaBraM .55±.02 .28±.02 .71±.03 .68±.04 .51±.02 .29±.04 .033±.007 ure3a,withfullquantitativevaluesreportedinAppendixE.
| BrainBERT .50±.01 | .25±.00 .61±.07 | .67±.06 .52±.02 | .23±.02 .032±.005 |     |     |     |     |
| ----------------- | --------------- | --------------- | ----------------- | --- | --- | --- | --- |
ContrastiveBFMsareanalyzedbydistinguishingaugmentation
| BrainWave .50±.01 | .25±.01 .66±.06 | .51±.20 .51±.03 | .27±.07 .029±.005 |     |     |     |     |
| ----------------- | --------------- | --------------- | ----------------- | --- | --- | --- | --- |
methodsfromCPCapproaches.CPC-basedmodelsshowstronger
| MSCARNet .80±.01 | .57±.01 .59±.06 | .74±.01 .51±.04 | .39±.03 .047±.004 |     |     |     |     |
| ---------------- | --------------- | --------------- | ----------------- | --- | --- | --- | --- |
robustnessandtransferabilityacrossclinicallyrelevanttasks,with

Brain4FMs:ABenchmarkofFoundationModelsforElectricalBrainSignals
Table5:Primaryperformancemetricsondiseasedisorderandsleepstaging.WeshowasubsetofBFMsacrossmethodtypesand𝑆𝐿†
denotesdataset-specificsupervisedbaselines,MSCARNetforAD/PD/SD,SPaRCNetforADHD,DeprNetforMDD,andCCNSEforSleep.
Method ADHD-Adult ADHD-Child ADFD MDD-64 SD-28 SleepEDF UCSD-ON
SSL Model AUROC Acc AUROC Acc AUROC Acc AUROC Acc AUROC Acc AUROC Acc AUROC Acc
C MBrain .95±.03 .92±.04 .69±.11 .63±.08 .53±.12 .50±.10 .93±.08 .87±.11 .58±.10 .58±.10 .94±.01 .79±.04 .49±.15 .46±.14
Bendr .62±.03 .61±.04 .53±.02 .51±.01 .52±.02 .52±.01 .78±.07 .73±.04 .49±.05 .50±.03 .91±.01 .69±.06 .51±.05 .49±.05
G REVE .96±.02 .91±.02 .79±.07 .71±.04 .84±.07 .77±.08 .97±.04 .88±.09 .81±.13 .75±.13 .78±.38 .63±.30 .63±.19 .56±.13
BrainOmni .96±.02 .91±.02 .71±.09 .62±.07 .80±.07 .71±.04 .94±.07 .85±.09 .69±.15 .69±.12 .87±.00 .63±.03 .53±.14 .49±.12
BrainWave .96±.03 .91±.04 .78±.04 .71±.04 .74±.05 .68±.05 .94±.03 .85±.02 .88±.07 .81±.06 .89±.02 .67±.05 .69±.20 .53±.08
CBraMod .95±.02 .92±.04 .64±.05 .64±.06 .55±.06 .59±.04 .90±.13 .84±.12 .54±.14 .58±.05 .93±.01 .73±.04 .60±.12 .49±.08
LaBraM .95±.04 .91±.04 .66±.12 .64±.08 .72±.07 .68±.05 .87±.12 .81±.11 .54±.07 .54±.04 .93±.01 .76±.04 .51±.22 .45±.11
BrainBERT .74±.05 .69±.05 .55±.03 .56±.03 .59±.05 .58±.05 .92±.07 .85±.07 .73±.11 .66±.15 .91±.02 .68±.07 .51±.05 .51±.06
O EEGPT .96±.03 .91±.04 .67±.13 .64±.10 .81±.05 .72±.05 .94±.05 .87±.08 .56±.21 .56±.11 .91±.00 .68±.03 .51±.21 .48±.17
NeuroLM .82±.14 .75±.07 .64±.06 .60±.05 .51±.04 .53±.03 .82±.11 .80±.06 .49±.04 .49±.05 .61±.06 .18±.04 .44±.18 .51±.18
𝑆𝐿† Dataset-spec .94±.02 .89±.03 .66±.05 .62±.03 .73±.11 .69±.08 .91±.06 .78±.04 .78±.15 .74±.09 .84±.02 .33±.04 .48±.19 .44±.08
MBrainemergingasthestrongestcontrastivebaseline,achieving (BrainBERT,NeuroGPT-E)byexaminingAUROCchangesandas-
consistentlyhigherAUROCandaccuracy.Augmentationmethods sessingstatisticalsignificanceusingpairedtestsinFigure3c.And
arenotuniformlyinferior;forexample,BIOTremainscompetitive fullresultsareinAppendixF.
forADHDandAD.Nevertheless,CPCapproachesdominateper- Itfindsthatperformancedegradationunderspatialperturbation
formanceonmostdatasets.Thistrendalignswithdifferencesin ismainlydrivenbytask-specificspatialdependence.Wedistinguish
trainingsignals.Augmentationapproachesrelyongenericpertur- spatialheterogeneity,whichcapturesregion-specificchannelsta-
bationstoformpositivepairs,whichmayintroduceboundarynoise tistics,fromspatialtopologydependence,whichrequiresmodeling
underhighinter-subjectvariability.CPCinsteadexploitstemporal relativechannelorganizationandpropagation.Channelpermu-
continuitybysegmentprediction,encouragingrepresentationsthat tationpreservesper-channeltemporalstatisticswhileremoving
preservephysiologicaldynamics.MBrainintegratesmulti-channel absolute channel ordering, enabling assessment of topology in-
CPCwithaGNNtocapturebothspatialandlong-rangetemporal variance.Epilepsyiswidelyregardedasaspatiotemporalnetwork
dependencies,benefitingtime-structuredtasks. disorderinvolvingseizureonsetandpropagationacrosscortical
Withinthegenerativefamily,mostBFMsfavorAEpretraining regions[1].Thus,itshowsstrongsensitivitytospatialtopology,
overARparadigms.Aplausibleexplanationliesinthemismatchbe- forwhichchannelpermutationcausessubstantialAUROCdrops.
tweenARobjectivesanddownstreamEEG/iEEGclassificationtasks. PDischaracterizedbyregion-specificspectralabnormalities[8]
ARmodelspredicteachstepfrompastcontext,producinginher- andpronouncedspatialheterogeneity,resultinginanintermedi-
entlyunidirectionalrepresentations[62],whereasAE-stylemodel atesensitivitytopermutation.Incontrast,ADHDexhibitsmilder
aggregatesbidirectionalcontextovertheentirewindow.Sincemost sensitivity.Althoughitssignalsareoftenlinkedtofrontalnetwork
tasksinvolveglobaldiscriminationratherthansequencegeneration dysfunction [74], performance depends less on precise channel
[110],suchbidirectional,window-levelrepresentationsaregener- adjacency,leadingtosmallerdrops.ForAD,wherebiomarkerspri-
ally more suitable for feature learning. Controlled experiments marilyreflectglobalspectralstatisticsratherthanlocalizedcortical
onNeuroGPTfurther support thisinterpretation.Twovariants patterns[5],mostmodelsremainlargelyunaffectedbychannel
arefinetuned:anencoder-onlymodel(NeuroGPT-E)andanen- permutation,withBrainWaveasanotableexception.
coder–decodermodel(NeuroGPT-D).Bothareevaluatedacross Cleararchitecturaldifferencesinrobustnessarefurtherobserved.
multipledownstreamtasks,includingepilepsy,sleepstaging,MW, Amongspatiallyweakmodels,BrainBERTdoesnotexplicitlyen-
andMIinFigure3b,andfullresultsarereportedinAppendixD. codechannelinteractionsandisthusinsensitivetochannelpermu-
NeuroGPT-EconsistentlyoutperformsNeuroGPT-D,indicatingthat tation,whereasNeuroGPT-Edegradesonsomedatasets.Andfor
finetuningperformanceinbrainsignalclassificationtasksislargely spatiallystrongmodels,BrainWave,whichusesCNNtocapture
drivenbyencoderrepresentations,whilethedecodercontributes spatialinformation,dropsonCHBMIT,ADHD-Child,andADFD,
morelimitedgainsinthissetting. suggestingitmayrelyongenericinter-channelattentionrather
thanlearningdataset-specificspatialstructure.EEGPTsimilarly
3.3.3 Q3:DoBFMslearntask-relevantspatialstructure? Severaltop- remainssensitivetochannel-identityperturbationsonspatially
performingmodelsinourbenchmark,suchasBrainWave,Brain- heterogeneoustasksdespiteimplicitchannelalignment.Incon-
Omni,andREVE,aredesignedwithaspecialstructuretocapture trast,otherspatiallystrongmodelsaremorestableacrosstasks
themulti-channelcharacteristicsofEEG/iEEGsignals.Thismo- anddatasets.Byexplicitlyencodingchanneltopologyviagraph
tivatestestingwhetherBFMsinternalizedataset-specificspatial structures,spatialembeddings,orsemanticspatialmodeling,they
structureduringtraining.Wethereforeapplychannel-permutation encouragelearningrelativespatialtopologyratherthanabsolute
perturbationstothetrain/validsplitswhilekeepingthetestsplitun- channelindices,improvingrobustnesstochannelreconfiguration.
changed.Spatiallystrongmodels(BrainWave,BrainOmni,CBraMod,
EEGPT,MBrain,REVE)arecomparedwithspatiallyweakmodels

Shenetal.
Table6:Codebooktokenusageandclassgeometryunder
3.3.4 Q4:HowisfrequencyinformationrepresentedinBFMsacross
tasks? Modelsreconstructingfrequency-domainfeatures(e.g.,Brain- different settings. We report the coverage (Cov.) and entropy
Wave,BrainBERT,LaBraM)demonstratestrongperformanceacross (Ent.)oftoken,meaninter-classsimilarity(inter),andinter-/intra-
tasks,particularlyindiseasediagnosis.Thisalignswithevidence classdistanceratio(DR)forBFM,fine-tunedandnon–fine-tuned
thatdifferentfrequencybandsencodedistinctcognitiveandpatho- LaBraM(𝐿𝑎𝐵𝑟𝑎𝑀 𝑛𝑜),andBrainOmniwithfourRVQlayers.
logicalstates[12].Comparedwithrawwaveforms,whichentangle
multipleoscillatorycomponentswithnoise,transformedrepresen- ADFD CHBMIT SD-28
tationsmaketheoscillatorystructuremoreexplicit.Reconstruction Model Cov. Ent. inter DR Cov. Ent. inter DR Cov. Ent. inter DR
in frequency domains, therefore, encourages models to capture
BFM .430 .868 .998 .002 .635 .838 .999 .001 .547 .853 .999 .001
band-structuredstatisticstiedtoneuralrhythms,whichmaybetter BrainOmni1 .997 .947 .996 .007 .988 .948 .999 .001 .964 .941 .999 .002
matchEEG/iEEGphysiologythanfittingtherawsignal. BrainOmni2 .998 .891 .928 .077 .998 .950 .966 .037 .998 .982 .994 .007
Motivatedbythis,weprobewhetherBFMsencodedominant BrainOmni3 .998 .929 .927 .076 .998 .970 .959 .043 .998 .973 .954 .049
frequencybands(sixbands;Figure3d)byfreezingthefine-tuned
BrainOmni4 .998 .946 .947 .055 .998 .988 .930 .072 .998 .972 .909 .094
LaBraM𝑛𝑜 .353 .755 .995 .006 .369 .721 .973 .038 .171 .607 .986 .022
encoderandtrainingalightweightband-wisePowerSpectralDen- LaBraM .140 .694 .267 1.155 .093 .518 -.9546.755 .043 .586 .800 .294
sity(PSD)headthatmapsembeddingstotheband-specificPSD
profilesviaseparatelinearheadsperband.Let𝑃 𝑏(𝑥) and𝑃ˆ 𝑏(𝑥)
denotetheground-truthandpredictedPSDforband𝑏.Wemeasure morepreferentialtokenusage,althoughits𝑖𝑛𝑡𝑒𝑟 and𝐷𝑅improve
bandpredictabilityby𝑟 𝑏 =corr(𝑃 𝑏(𝑥),𝑃ˆ 𝑏(𝑥)),thennormalize𝑟 𝑏 overBFM,classseparationremainsweak,indicatingthatthepre-
acrossbandstoobtaineachband’srelativepredictivestrengthas trainedcodebookcannotdirectlytransferintoclass-discriminative
𝑟𝑛,withdetailedresultsreportedinAppendixG.Finally,Spearman geometryfordownstreamtasks.Incontrast,BrainOmni’shierar-
𝑏
rankcorrelationandsignificancearecomputedbetween𝑟𝑛 and chicalRVQmaintainshightokencoverageandentropy,andasthe
𝑏
downstreamperformancerankings,primarilybasedonAUROC,to residualleveldeepens,𝐷𝑅 tendstoincrease.Thissuggeststhat
linkfrequencyencodingwithtaskperformance. coarse-to-finediscretizationcanmitigatecodebookcollapseand
Theresultsshowcleartask-dependentpatterns.InADFD,the progressivelyintroducemoreclass-discriminativestructure.Fur-
relativepredictabilityof𝛼 and𝛾 𝑙 issignificantlycorrelatedwith ther,fine-tuningLaBraM’scodebookresultsindecreasedtoken
performance ranking. In depression tasks, correlations are uni- coverageandentropy,alongsideincreasedclassseparation,indi-
formlyweakandnon-significant.InADHD-Adult,𝛽and𝛾 𝑙 show catingthatthecodebookisabletoadapttonewtasks.However,
significantpositivecorrelations,whereas𝜃 isnegativelycorrelated. reusingdiscretizationduringfinetuningstilldegradesdownstream
InADHD-Child,𝛼,𝛽,and𝛾 𝑙 areallsignificantlyassociatedwith performance,suggestingquantizationmayconstraindiscriminative
performance,with𝛽beingthestrongest.Acrossseveraldatasets, flexibilityanddiscardfine-grainedcues(AppendixH).Overall,the
band-wiserelativepredictabilityshowsaconsistentassociation resultsinTable6highlighthierarchicaldiscretizationasapromising
withperformanceranking.Clinically,ADisoftenlinkedtoele- routetobalancerobustnessandcapacityforBFMs.
vated𝛿/𝛼 and𝜃/𝛼 ratios[76],whileADHDstudieshighlightthe
relevanceof𝜃/𝛽-relatedmarkers[64].ItsuggeststhatBFMsem- 4 Conclusion
phasizedifferentfrequencybandsacrosstasks,andsomesalient Brain4FMsprovidesaunified,plug-and-playframeworkforanalyz-
bandsaretask-relevant.Thistask-adaptivefrequencyemphasis ingBFMs.WeorganizeBFMswithanSSL-centrictaxonomyand
mayhelpguideimprovementsindownstreamperformance. evaluate15modelson18publicdatasetsunderstandardizedcross-
subjectfinetuning,enablingfairandreproduciblecomparison.Our
3.3.5 Q5:DocodebookdiscretizationstrategiesbenefitBFMs? Dis-
analysesrelateperformancevariationtokeyfactors,includingpre-
cretecodebookshaverecentlybeenintroducedinBFMstoimprove
trainingdatacomposition,SSLstrategy,andmodeldesign.Together,
representationstabilityandgeneralization.Toassesstheimpact
Brain4FMsoffersasolidreferenceforfutureBFMsdevelopment
ofcodebookdesignonrepresentationusageanddiscriminability,
andsupportstransparent,comparable,andextensibleevaluationin
threebenchmarkmodelswithexplicitdiscretization(BFM,LaBraM,
thisrapidlyevolvingfield.Weplantoextendthebenchmarkwith
BrainOmni)areanalyzed.Thesemodelsadoptdistinctmechanisms.
frozen-encoder,few-shot,andzero-shotsettings,andtokeepthe
BFMappliesthetokenizerfromChronostodiscretizerawsignals
open-sourceleaderboarduptodate.
intotokenIDs.LaBraMdiscretizesencoderfeaturesduringpre-
trainingviaaVQ-VAEbutremovesthecodebookduringfinetuning. References
BrainOmni follows a similar paradigm but employs multi-layer
[1] 2020. IctalEEGsourcelocalizationinfocalepilepsy:Reviewandfutureper-
residualvectorquantization(RVQ).Weanalyzecodebookbehavior spectives.ClinicalNeurophysiology131,11(2020),2600–2616.
onthetestsetbycharacterizingtoken-embeddinggeometry,using [2] KhaldAliIAboalayon,MiadFaezipour,WafaaSAlmuhammadi,andSaeid
𝑖𝑛𝑡𝑒𝑟 to measure class-wise center similarity and distance ratio Moslehpour.2016.SleepstageclassificationusingEEGsignalanalysis:acom-
prehensivesurveyandnewinvestigation.Entropy18,9(2016),272.
(𝐷𝑅)toquantifyinter-intraclassseparation. [3] HamdiAltaheri,FakhriKarray,MdMilonIslam,SMRaju,andAmir-Hossein
It observes clear design-dependent behaviors. BFM activates Karimi.2025.BridgingBrainwithFoundationModelsthroughSelf-Supervised
Learning.arXivpreprintarXiv:2506.16009(2025).
many tokens with high coverage and entropy, yet exhibits ex- [4] DaniloAvola,LuigiCinque,AngeloDiMambro,RomeoLanzino,DanielePan-
tremelyhigh𝑖𝑛𝑡𝑒𝑟 andlow𝐷𝑅 ,suggestingthatagenerictem- none,andFrancescoScarcello.2024. Multi-stream1dCNNforEEGmotor
imageryclassificationoflimbsactivation.IEEEAccess12(2024),83940–83951.
poralcodebookfavorscross-domainrobustnessbutishardtoen-
[5] ClaudioBabiloni,RaffaeleFerri,DavideVMoretti,AndreaStrambi,Giuliano
codetask-specificEEG/iEEGsemantics.LaBraMshowssparserand Binetti,GloriaDalForno,FlorindaFerreri,BartoloLanuzza,ClaudioBonato,

Brain4FMs:ABenchmarkofFoundationModelsforElectricalBrainSignals
FlavioNobili,etal.2004.Abnormalfronto-parietalcouplingofbrainrhythms [28] SamGijsenandKerstinRitter.[n.d.].EEG-LanguagePretrainingforHighly
inmildAlzheimer’sdisease:AmulticentricEEGstudy. EuropeanJournalof Label-EfficientClinicalPhenotyping.InForty-secondInternationalConference
Neuroscience19,9(2004),2583–2590. onMachineLearning.
[6] AlexeiBaevski,YuhaoZhou,AbdelrahmanMohamed,andMichaelAuli.2020. [29] AryLGoldberger,LuisANAmaral,LeonGlass,JeffreyMHausdorff,PlamenCh
wav2vec2.0:Aframeworkforself-supervisedlearningofspeechrepresenta- Ivanov,RogerGMark,JosephEMietus,GeorgeBMoody,Chung-KangPeng,
tions.Advancesinneuralinformationprocessingsystems33(2020),12449–12460. andHEugeneStanley.2000.PhysioBank,PhysioToolkit,andPhysioNet:com-
[7] GhasemSadeghiBajestani,ShimaAbedian,FatemehMakhloughi,Motahhareh ponentsofanewresearchresourceforcomplexphysiologicsignals.circulation
Raoufitabar,andHamidSaeedi.2023.Adatasetofeegsignalsfromadultswith 101,23(2000),e215–e220.
adhdandhealthycontrols:Restingstate,cognitivefunction,andsoundlistening [30] J.Guttag.2010.CHB-MITScalpEEGDatabase(version1.0.0).
paradigm.MendeleyData(2023). [31] DannyDongyeopHan,YonghyeonGwon,AhhyunLucyLee,TaeyangLee,
[8] JacopoBaroneandHollyERossiter.2021.Understandingtheroleofsensori- SeongJinLee,JubinChoi,SebinLee,JihyunBang,SeungjuLee,DavidKeetae
motorbetaoscillations.Frontiersinsystemsneuroscience15(2021),655886. Park,etal.2025. DIVER-1:DeepIntegrationofVastElectrophysiological
[9] MohammadJavadDarvishiBayazi,HenaGhonia,RolandRiachi,BrunoAris- RecordingsatScale.arXivpreprintarXiv:2512.19097(2025).
timunha,ArianKhorasani,MdRifatArefin,AminDarabi,GuillaumeDumas, [32] AmirHarati,SilviaLopez,IObeid,JPicone,MPJacobson,andSTobochnik.2014.
andIrinaRish.[n.d.]. General-PurposeBrainFoundationModelsforTime- TheTUHEEGCORPUS:AbigdataresourceforautomatedEEGinterpretation.
SeriesNeuroimagingData.InNeurIPSWorkshoponTimeSeriesintheAgeof In2014IEEEsignalprocessinginmedicineandbiologysymposium(SPMB).IEEE,
LargeModels. 1–5.
[10] Ruggero G Bettinardi, Mohamed Rahmouni, and Ulysse Gimenez. 2025. [33] KaimingHe,XinleiChen,SainingXie,YanghaoLi,PiotrDollár,andRoss
BioSerenity-E1:aself-supervisedEEGmodelformedicalapplications.arXiv Girshick.2022.Maskedautoencodersarescalablevisionlearners.InProceedings
preprintarXiv:2503.10362(2025). oftheIEEE/CVFconferenceoncomputervisionandpatternrecognition.16000–
[11] ClemensBrunner,RobertLeeb,GernotMüller-Putz,AloisSchlögl,andGert 16009.
Pfurtscheller.2008.BCICompetition2008–GrazdatasetA.Instituteforknowl- [34] OlivierHenaff.2020.Data-efficientimagerecognitionwithcontrastivepredic-
edgediscovery(laboratoryofbrain-computerinterfaces),GrazUniversityofTech- tivecoding.InInternationalconferenceonmachinelearning.PMLR,4182–4192.
nology16,1-6(2008),34. [35] JiazhenHong,GeoffreyMackellar,andSoheilaGhane.2025.SAMBA:Toward
[12] GyorgyBuzsakiandAndreasDraguhn.2004.Neuronaloscillationsincortical aLong-ContextEEGFoundationModelviaSpatialEmbeddingandDifferential
networks.science304,5679(2004),1926–1929. Mamba.arXivpreprintarXiv:2511.18571(2025).
[13] DonghongCai,JunruChen,YangYang,TengLiu,andYafengLi.2023.Mbrain: [36] JamesFCavanaghjcavanagh@unm.edu.2021."EEG:Depressionrest".doi:10.
Amulti-channelself-supervisedlearningframeworkforbrainsignals.InPro- 18112/openneuro.ds003478.v1.1.0
ceedingsofthe29thACMSIGKDDConferenceonKnowledgeDiscoveryandData [37] JaehyunJeon,SeungwooJeong,YeajinShon,andHeung-IlSuk.[n.d.].TaKF+:
Mining.130–141. Aversatileandparameter-efficienttuningforEEGfoundationmodel.([n.d.]).
[14] Chi-ShengChen,Ying-JungChen,andAidanHung-WenTsai.2025. Large [38] MuyunJiang,ShuaileiZhang,ZhenjieYang,MengjunWu,WeibangJiang,
CognitionModel:TowardsPretrainedEEGFoundationModel.arXivpreprint ZhiweiGuo,WeiZhang,RuiLiu,ShangenZhang,YongLi,etal.2025.ELASTIQ:
arXiv:2502.17464(2025). EEG-LanguageAlignmentwithSemanticTaskInstructionandQuerying.arXiv
[15] TingChen,SimonKornblith,MohammadNorouzi,andGeoffreyHinton.2020. preprintarXiv:2509.24302(2025).
Asimpleframeworkforcontrastivelearningofvisualrepresentations.InInter- [39] Wei-BangJiang,YansenWang,Bao-LiangLu,andDongshengLi.2024.Neu-
nationalconferenceonmachinelearning.PmLR,1597–1607. roLM:AUniversalMulti-taskFoundationModelforBridgingtheGapbetween
[16] YuqiChen,KanRen,KaitaoSong,YansenWang,YifanWang,DongshengLi,and LanguageandEEGSignals.arXivpreprintarXiv:2409.00101(2024).
LiliQiu.2024.EEGFormer:Towardstransferableandinterpretablelarge-scale [40] Wei-BangJiang,Li-MingZhao,andBao-LiangLu.2024. Largebrainmodel
EEGfoundationmodel.arXivpreprintarXiv:2401.10278(2024). forlearninggenericrepresentationswithtremendousEEGdatainBCI.arXiv
[17] ZhigeChen,ChengxuanQin,WenlongYou,RuiLiu,CongyingChu,RuiYang, preprintarXiv:2405.18765(2024).
KayChenTan,andJibinWu.2025.HEAR:AnEEGFoundationModelwithHet- [41] BuJin,ShuningXue,JieJiang,LongtengGuo,XinxinZhu,JinZhou,JingLiu,
erogeneousElectrodeAdaptiveRepresentation.arXivpreprintarXiv:2510.12515 etal.[n.d.].UniEEG:AdvancingUniversalEEGRepresentationwithElectrode-
(2025). WiseTime-FrequencyPretraining.([n.d.]).
[18] Hsiang-YunSherryChien,HanlinGoh,ChristopherMSandino,andJosephY [42] JinJing,WendongGe,ShendaHong,MartaBentoFernandes,ZhenLin,Chaoqi
Cheng.2022. Maeeg:Maskedauto-encoderforeegrepresentationlearning. Yang,SungtaeAn,AaronFStruck,AlineHerlopian,IoannisKarakis,etal.2023.
arXivpreprintarXiv:2211.02625(2022). Developmentofexpert-levelclassificationofseizuresandrhythmicandperiodic
[19] WenhuiCui,WoojaeJeong,PhilippThölke,TakfarinasMedani,KarimJerbi, patternsduringEEGinterpretation.Neurology100,17(2023),e1750–e1762.
AnandAJoshi,andRichardMLeahy.2023.Neuro-gpt:Developingafoundation [43] SangminJo,JaehyunJeon,SeungwooJeong,andHeung-IlSuk.2023.Channel-
modelforeeg.arXivpreprintarXiv:2311.03764107(2023). awareself-supervisedlearningforeeg-basedbci.In202311thInternational
[20] JonathanDan,AmirhosseinShahbazinia,ChristodoulosKechris,andDavid WinterConferenceonBrain-ComputerInterface(BCI).IEEE,1–4.
Atienza.2025. SzCOREasabenchmark:reportfromtheseizuredetection [44] JatinderKaur,KulwinderSinghParmar,andSarbjitSingh.2023.Autoregressive
challengeatthe2025AIinEpilepsyandNeurologicalDisordersConference. modelsinenvironmentalforecastingtimeseries:atheoreticalandapplication
arXivpreprintarXiv:2505.18191(2025). review.EnvironmentalScienceandPollutionResearch30,8(2023),19617–19641.
[21] JacobDevlin,Ming-WeiChang,KentonLee,andKristinaToutanova.2019.Bert: [45] BobKemp,AeilkoHZwinderman,BertTuk,HilbertACKamphuisen,and
Pre-trainingofdeepbidirectionaltransformersforlanguageunderstanding.In JosefienJLOberye.2000.Analysisofasleep-dependentneuronalfeedbackloop:
Proceedingsofthe2019conferenceoftheNorthAmericanchapteroftheassociation theslow-wavemicrocontinuityoftheEEG.IEEETransactionsonBiomedical
forcomputationallinguistics:humanlanguagetechnologies,volume1(longand Engineering47,9(2000),1185–1194.
shortpapers).4171–4186. [46] SirvanKhalighi,TeresaSousa,JoséMoutinhoSantos,andUrbanoNunes.2016.
[22] AlexandruDimofte,GlennAntaBucagu,ThorirMarIngolfsson,XiayingWang, ISRUC-Sleep:Acomprehensivepublicdatasetforsleepresearchers.Computer
AndreaCossettini,LucaBenini,andYaweiLi.2025.CEReBrO:CompactEncoder methodsandprogramsinbiomedicine124(2016),180–192.
forRepresentationsofBrainOscillationsUsingEfficientAlternatingAttention. [47] DiederikPKingmaandMaxWelling.2013.Auto-encodingvariationalbayes.
arXivpreprintarXiv:2501.10885(2025). arXivpreprintarXiv:1312.6114(2013).
[23] BerkayDöner,ThorirMarIngolfsson,LucaBenini,andYaweiLi.2025.Luna: [48] SanderKoelstra,ChristianMuhl,MohammadSoleymani,Jong-SeokLee,Ashkan
Efficientandtopology-agnosticfoundationmodelforeegsignalanalysis.arXiv Yazdani,TouradjEbrahimi,ThierryPun,AntonNijholt,andIoannisPatras.
preprintarXiv:2510.22257(2025). 2011.Deap:Adatabaseforemotionanalysis;usingphysiologicalsignals.IEEE
[24] AlexeyDosovitskiy.2020.Animageisworth16x16words:Transformersfor transactionsonaffectivecomputing3,1(2011),18–31.
imagerecognitionatscale.arXivpreprintarXiv:2010.11929(2020). [49] DemetresKostas,StephaneAroca-Ouellette,andFrankRudzicz.2021.BENDR:
[25] ZitaoFang,ChenxuanLi,HongtingZhou,ShuyangYu,GuodongDu,Ashwaq Usingtransformersandacontrastiveself-supervisedlearningtasktolearn
Qasem,YangLu,JingLi,JunsongZhang,andSimKuanGoh.2025. Neuript: frommassiveamountsofEEGdata.FrontiersinHumanNeuroscience15(2021),
Foundationmodelforneuralinterfaces.arXivpreprintarXiv:2510.16548(2025). 653659.
[26] MatteoFerrante,TommasoBoccato,GrigoriiRashkov,andNicolaToschi.2024. [50] VamsiKumar,LikithReddy,ShivamKumarSharma,KamalakerDadi,Chiran-
TowardsNeuralFoundationModelsforVision:AligningEEG,MEG,andfMRI jeeviYarra,RajuSBapi,andSrijitheshRajendran.2022.mulEEG:amulti-view
RepresentationsforDecoding,Encoding,andModalityConversion. arXiv representationlearningonEEGsignals.InInternationalConferenceonMedical
preprintarXiv:2411.09723(2024). ImageComputingandComputer-AssistedIntervention.Springer,398–407.
[27] LuayFraiwanandMohanadAlkhodari.2020.Classificationoffocalandnon- [51] JiiKwonandYouminShin.2026.FoundationModelsforNeuralSignalDecoding:
focalepilepticpatientsusingsinglechannelEEGandlongshort-termmemory EEG-CenteredPerspectivesTowardUnifiedRepresentations.EuropeanJournal
learningsystem.IEEEAccess8(2020),77255–77262. ofNeuroscience63,1(2026),e70376.

Shenetal.
[52] Cheol-HuiLee,HakseungKim,ByungCYoon,andDong-JooKim.2025.To- [74] MichaelMurias,JamesMSwanson,andRameshSrinivasan.2007.Functional
wardFoundationalModelforSleepAnalysisUsingaMultimodalHybridSelf- connectivityoffrontalcortexinhealthyandADHDchildrenreflectedinEEG
SupervisedLearningFramework.arXivpreprintarXiv:2502.17481(2025). coherence.CerebralCortex17,8(2007),1788–1799.
[53] HarimLee,EunseonSeong,andDong-KyuChae.2022.Self-SupervisedLearn- [75] PetrNejedly,VaclavKremen,VladimirSladky,JanCimbalnik,PetrKlimes,Filip
ingwithAttention-basedLatentSignalAugmentationforSleepStagingwith Plesinger,FilipMivalt,VojtechTravnicek,IvoViscor,MartinPail,etal.2020.
LimitedLabeledData..InIJCAI.3868–3876. MulticenterintracranialEEGdatasetforclassificationofgraphoelementsand
[54] AngLi,ZikaiWang,LiuyinYang,ZhenyuWang,TianhengXu,HonglinHu, artifactualsignals.Scientificdata7,1(2020),179.
andMarcMVanHulle.2025.CoMET:AContrastive-MaskedBrainFoundation [76] JenniferJNewsonandTaraCThiagarajan.2019. EEGfrequencybandsin
ModelforUniversalEEGRepresentation.arXivpreprintarXiv:2509.00314(2025). psychiatricdisorders:areviewofrestingstatestudies. Frontiersinhuman
[55] FanLi,RuiYan,RezaMahini,LaiWei,ZhiqiangWang,KlausMathiak,Rong neuroscience12(2019),521.
Liu,andFengyuCong.2021. End-to-endsleepstagingusingconvolutional [77] IyadObeidandJosephPicone.2016.ThetempleuniversityhospitalEEGdata
neuralnetworkinrawsingle-channelEEG.BiomedicalSignalProcessingand corpus.Frontiersinneuroscience10(2016),196.
Control63(2021),102203. [78] MattsonOggandWilliamGCoon.2024.Self-supervisedtransformermodel
[56] HongqiLi,YitongChen,YujuanWang,WeihangNi,andHaodongZhang.2025. trainingforasleep-eegfoundationmodel.In202446thAnnualInternational
Foundationmodelsforcross-domaineeganalysisapplication:Asurvey.arXiv ConferenceoftheIEEEEngineeringinMedicineandBiologySociety(EMBC).IEEE,
preprintarXiv:2508.15716(2025). 1–6.
[57] JiaheLi,XinChen,FanqiShen,JunruChen,YuxinLiu,DaozeZhang,Zhizhang [79] BOrkanOlcayandBilgeKaraçalı.2023.Time-resolvedEEGsignalanalysisfor
Yuan,FangZhao,MengLi,andYangYang.2025. Deeplearning-powered motorimageryactivityrecognition.BiomedicalSignalProcessingandControl
electricalbrainsignalsanalysis:Advancingneurologicaldiagnostics. IEEE 86(2023),105179.
ReviewsinBiomedicalEngineering(2025). [80] AaronvandenOord,YazheLi,andOriolVinyals.2018.Representationlearning
[58] XiaominLiandVangelisMetsis.2022. Spp-eegnet:Aninput-agnosticself- withcontrastivepredictivecoding.arXivpreprintarXiv:1807.03748(2018).
supervisedeegrepresentationmodelforinter-datasettransferlearning.In [81] YassineElOuahidi,JonathanLys,PhilippThölke,NicolasFarrugia,BastienPas-
InternationalConferenceonComputingandInformationTechnology.Springer, deloup,VincentGripon,KarimJerbi,andGiuliaLioi.2025.REVE:AFoundation
173–182. ModelforEEG–AdaptingtoAnySetupwithLarge-ScalePretrainingon25,000
[59] ChenyuLiu,YuqiuDeng,TianyuLiu,JinanZhou,XinliangZhou,ZiyuJia,and Subjects.arXivpreprintarXiv:2510.21585(2025).
YiDing.2025. ECHO:TowardContextualSeq2SeqParadigmsinLargeEEG [82] AlecRadford,JeffreyWu,RewonChild,DavidLuan,DarioAmodei,Ilya
Models.arXivpreprintarXiv:2509.22556(2025). Sutskever,etal.2019.Languagemodelsareunsupervisedmultitasklearners.
[60] HanwenLiu,DanielHajialigol,BennyAntony,AiguoHan,andXuanWang. OpenAIblog1,8(2019),9.
2024.Eeg2text:Openvocabularyeeg-to-textdecodingwitheegpre-training [83] AbdellahRahmani,ArunVenkitaraman,andPascalFrossard.2023.AMeta-GNN
andmulti-viewtransformer.arXivpreprintarXiv:2405.02165(2024). approachtopersonalizedseizuredetectionandclassification.InICASSP2023-
[61] HuanLiu,ShusenYang,YuzheZhang,MengzeWang,FanyuGong,Chengxi 2023IEEEInternationalConferenceonAcoustics,SpeechandSignalProcessing
Xie,GuanjianLiu,ZejunLiu,Yong-JinLiu,Bao-LiangLu,etal.2025.Libeer: (ICASSP).IEEE,1–5.
Acomprehensivebenchmarkandalgorithmlibraryforeeg-basedemotion [84] AlexanderP.Rockhill,NickoJackson,JobiGeorge,AdamAron,andNicoleC.
recognition.IEEETransactionsonAffectiveComputing(2025). Swann.2021."UCSanDiegoRestingStateEEGDatafromPatientswithParkin-
[62] XiaoLiu,FanjinZhang,ZhenyuHou,LiMian,ZhaoyuWang,JingZhang, son’sDisease".doi:doi:10.18112/openneuro.ds002778.v1.0.5
andJieTang.2021.Self-supervisedlearning:Generativeorcontrastive.IEEE [85] AyanSeal,RishabhBajpai,JagritiAgnihotri,AnisYazidi,EnriqueHerrera-
transactionsonknowledgeanddataengineering35,1(2021),857–876. Viedma,andOndrejKrejcar.2021. DeprNet:Adeepconvolutionneuralnet-
[63] CatherineLloyd,LoicLorenteLemoine,ReiyanAl-Shaikh,KimTienLy,Hakan workframeworkfordetectingdepressionusingEEG. IEEETransactionson
Kayan,CharithPerera,andNhatPham.2024.Stress-GPT:Stressdetectionwith InstrumentationandMeasurement70(2021),1–13.
anEEG-basedfoundationmodel.InProceedingsofthe30thAnnualInternational [86] AliShoeb.2009.ApplicationofMachineLearningtoEpilepticSeizureOnsetDetec-
ConferenceonMobileComputingandNetworking.2341–2346. tionandTreatment.Ph.D.Dissertation.MassachusettsInstituteofTechnology.
[64] SandraKLoo,AlexanderCho,TSigiHale,JamesMcGough,JamesMcCracken, [87] RahulThapa,BryanHe,MagnusRuudKjaer,HMooreIV,GauriGanjoo,Em-
andSusanLSmalley.2013.CharacterizationofthethetatobetaratioinADHD: manuelMignot,andJamesZou.2024. Sleepfm:foundationmodelforsleep
identifyingpotentialsourcesofheterogeneity.Journalofattentiondisorders17, analysis.InICLRWorkshoponLearningfromTimeSeriesForHealth.
5(2013),384–392. [88] AaronVanDenOord,OriolVinyals,etal.2017.Neuraldiscreterepresentation
[65] FabienLotte,LaurentBougrain,AndrzejCichocki,MaureenClerc,MarcoCon- learning.Advancesinneuralinformationprocessingsystems30(2017).
gedo,AlainRakotomamonjy,andFlorianYger.2018.Areviewofclassification [89] NeerajWagh,JionghaoWei,SamarthRawal,BrentBerry,LelandBarnard,Ben-
algorithmsforEEG-basedbrain–computerinterfaces:a10yearupdate.Journal jaminBrinkmann,GregoryWorrell,DavidJones,andYogatheesanVaratharajah.
ofneuralengineering15,3(2018),031005. 2021.Domain-guidedself-supervisionofEEGdataimprovesdownstreamclas-
[66] WeihengLu,ChunfengSong,JiaminWu,PengyuZhu,YuchenZhou,Weijian sificationperformanceandgeneralizability.InMachineLearningforHealth.
Mai,QihaoZheng,andWanliOuyang.2025.UniMind:UnleashingthePower PMLR,130–142.
ofLLMsforUnifiedMulti-TaskBrainDecoding.arXivpreprintarXiv:2506.18962 [90] ChristopherWang,VighneshSubramaniam,AdamUriYaari,GabrielKreiman,
(2025). Boris Katz, Ignacio Cases, and Andrei Barbu. 2023. BrainBERT: Self-
[67] JingyingMa,FengWu,QikaLin,YuchengXing,ChenyuLiu,ZiyuJia,and supervisedrepresentationlearningforintracranialrecordings.arXivpreprint
MenglingFeng.2025. CodeBrain:BridgingDecoupledTokenizerandMulti- arXiv:2302.14367(2023).
ScaleArchitectureforEEGFoundationModel.arXivpreprintarXiv:2506.09110 [91] GuangyuWang,WenchaoLiu,YuhongHe,CongXu,LinMa,andHaifengLi.
(2025). 2024.Eegpt:Pretrainedtransformerforuniversalandreliablerepresentation
[68] UmbertoMichelucci.2022. Anintroductiontoautoencoders. arXivpreprint ofeegsignals. AdvancesinNeuralInformationProcessingSystems37(2024),
arXiv:2201.03898(2022). 39249–39280.
[69] AndreasMiltiadous,KaterinaD.Tzimourta,TheodoraAfrantou,Panagiotis [92] JiquanWang,ShaZhao,ZhilingLuo,YangxuanZhou,HaitengJiang,ShijianLi,
Ioannidis,NikolaosGrigoriadis,DimitriosG.Tsalikakis,PantelisAngelidis, TaoLi,andGangPan.2024.CBraMod:ACriss-CrossBrainFoundationModel
MarkosG.Tsipouras,EvripidisGlavas,NikolaosGiannakeas,andAlexandrosT. forEEGDecoding.arXivpreprintarXiv:2412.07236(2024).
Tzallas.2023."Adatasetof88EEGrecordingsfrom:Alzheimer’sdisease,Frontotem- [93] LiminWang,ToyotaroSuzumura,andHirokiKanezashi.2024.Graph-Enhanced
poraldementiaandHealthysubjects".doi:doi:10.18112/openneuro.ds004504.v1. EEGFoundationModel.arXivpreprintarXiv:2411.19507(2024).
0.2 [94] YiheWang,NanHuang,NadiaMammone,MarcoCecchi,andXiangZhang.
[70] NavidMohammadiFoumani,GeoffreyMackellar,SoheilaGhane,SaadIrtza, 2025. LEAD:LargeFoundationModelforEEG-BasedAlzheimer’sDisease
NamNguyen,andMahsaSalehi.2024.Eeg2rep:enhancingself-supervisedEEG Detection.arXivpreprintarXiv:2502.01678(2025).
representationthroughinformativemaskedinputs.InProceedingsofthe30th [95] XinxuWei,KanhaoZhao,YongJiao,NancyBCarlisle,HuaXie,GregoryA
ACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining.5544–5555. Fonzo,andYuZhang.2025. Multi-modalcross-domainself-supervisedpre-
[71] MostafaNeoMohsenvand,MohammadRasoolIzadi,andPattieMaes.2020. trainingforfMRIandEEGfusion.NeuralNetworks184(2025),107066.
Contrastiverepresentationlearningforelectroencephalogramclassification.In [96] XinxuWei,KanhaoZhao,YongJiao,NancyBCarlisle,HuaXie,andYuZhang.
MachineLearningforHealth.PMLR,238–253. 2024.Pre-TrainingGraphContrastiveMaskedAutoencodersareStrongDis-
[72] AliMotieNasrabadi,ArminAllahverdy,MehdiSamavati,andMohammadReza tillersforEEG.arXivpreprintarXiv:2411.19230(2024).
Mohammadi.2020.EEGdataforADHD/Controlchildren.doi:10.21227/rzfh- [97] WeiningWeng,YangGu,ShuaiGuo,YuanMa,ZhaohuaYang,YuchenLiu,
zn36 andYiqiangChen.2025.Self-supervisedlearningforelectroencephalogram:A
[73] WajidMumtaz.2016.MDDPatientsandHealthyControlsEEGData(New).(11 systematicsurvey.Comput.Surveys57,12(2025),1–38.
2016).doi:10.6084/m9.figshare.4244171.v2 [98] AnqiWu,YifanZhang,YangYu,andLing-LiZeng.2024. EEG-ARNet:An
AutoregressivePre-trainingModelforExtractingEEGFeatures.In20245th

Brain4FMs:ABenchmarkofFoundationModelsforElectricalBrainSignals
InternationalConferenceonComputersandArtificialIntelligenceTechnology [121] YangxuanZhou,ShaZhao,JiquanWang,HaitengJiang,ShijianLi,TaoLi,and
(CAIT).IEEE,255–259. GangPan.[n.d.].BrainUICL:Anunsupervisedindividualcontinuallearning
[99] DiWu,SiyuanLi,JieYang,andMohamadSawan.2022.neuro2vec:Masked frameworkforEEGapplications.InTheThirteenthInternationalConferenceon
fourierspectrumpredictionforneurophysiologicalrepresentationlearning. LearningRepresentations.
arXivpreprintarXiv:2204.12440(2022). [122] QiushiZhu,XiaoyingZhao,JieZhang,YuGu,ChaoWeng,andYuchenHu.2023.
[100] DiWu,SiyuanLi,JieYang,andMohamadSawan.2024.Neuro-BERT:Rethinking EEG2VEC:Self-supervisedelectroencephalographicrepresentationlearning.
MaskedAutoencodingforSelf-SupervisedNeurologicalPretraining. IEEE arXivpreprintarXiv:2305.13957(2023).
JournalofBiomedicalandHealthInformatics(2024). [123] IgorZyma,SergiiTukaev,IvanSeleznov,KenKiyono,AntonPopov,Mariia
[101] JiaminWu,ZichenRen,JunyuWang,PengyuZhu,YonghaoSong,Mianxin Chernykh,andOleksiiShpenkov.2019.Electroencephalogramsduringmental
Liu,QihaoZheng,LeiBai,WanliOuyang,andChunfengSong.2025.AdaBrain- arithmetictaskperformance.Data4,1(2019),14.
bench:Benchmarkingbrainfoundationmodelsforbrain-computerinterface
applications.arXivpreprintarXiv:2507.09882(2025). A SSLParadigm
[102] ChuqinXiang,XinruiFan,DuoBai,KeLv,andXuLei.2024."AResting-state
EEGDatasetforSleepDeprivation".doi:doi:10.18112/openneuro.ds004902.v1.0.5 A.1 Contrastive-basedMethod
[103] QinfanXiao,ZiyunCui,ChiZhang,SiqiChen,WenWu,AndrewThwaites,
AlexandraWoolgar,BowenZhou,andChaoZhang.2025. BrainOmni:A
A.1.1 Augmentationcontrast. Augmentation-basedcontrastivelearn-
BrainFoundationModelforUnifiedEEGandMEGSignals. arXivpreprint
arXiv:2505.18185(2025). ingconstructspositivepairsbyapplyingtransformationoperators
[104] WeiXiong,JiangtongLi,JieLi,andKunZhu.2025.Eeg-fm-bench:Acompre- 𝑎 𝑠 tothesameinputsignal,withrepresentationlearningdrivenby
hensivebenchmarkforthesystematicevaluationofeegfoundationmodels.
arXivpreprintarXiv:2508.17742(2025). enforcinginvarianceacrossaugmentedviews.EarlyBFMsworks
[105] ChaoqiYang,MWestover,andJimengSun.2023.Biot:Biosignaltransformer primarilyfocusedonexpandingtheeffectiveviewspaceinduced
forcross-datalearninginthewild.AdvancesinNeuralInformationProcessing by𝑎 𝑠.SeqCLR[71]adaptsSimCLR[15]tomultichannelEEGby
Systems36(2023),78240–78260.
[106] WenchaoYang,WeidongYan,WenkangLiu,YulanMa,andYangLi.2025.THD- recombiningchannelstoexpandtheaugmentation-inducedview
BAR:TopologyHierarchicalDerivedBrainAutoregressiveModelingforEEG spaceandenforceconsistencyacrossviews.SppEEGNet[58]fur-
GenericRepresentations.arXivpreprintarXiv:2511.13733(2025).
therappliesasuiteofEEG-specificaugmentationsandformspos-
[107] ZhizhangYuan,FanqiShen,MengLi,YuguoYu,ChenhaoTan,andYangYang.
2024.BrainWave:ABrainSignalFoundationModelforClinicalApplications. itivepairswithinslidingwindowsona2Dsignalrepresentation,
arXivpreprintarXiv:2402.10251(2024). whichhelpsreducecross-datasetsampling-ratemismatch.BIOT
[108] TongtianYue,ShuningXue,XuangeGao,YepengTang,LongtengGuo,JieJiang,
andJingLiu.2024.EEGPT:UnleashingthePotentialofEEGGeneralistFoun- [105]introduceschannel-levelaugmentationstailoredtobiosignals.
dationModelbyAutoregressivePre-training.arXivpreprintarXiv:2410.19779 Nevertheless,contrastiveobjectivescansufferfromfalsenegatives,
(2024).
especiallyinsleepstaging,whereadjacentsegmentsmayshare
[109] ZiyiZeng,ZhenyangCai,YixiCai,XidongWang,JunyingChen,Rongsheng
Wang,YipengLiu,SiqiCai,BenyouWang,ZhiguoZhang,etal.2025.Wavemind: labels.SSLAPP[53]addressesthisbyadversariallygeneratinghigh-
Towardsaconversationaleegfoundationmodelalignedtotextualandvisual qualitypositivesandperformingattention-guidedaugmentation
modalities.arXivpreprintarXiv:2510.00032(2025).
inlatentspace,mitigatingsemanticcollisionsinpairconstruction.
[110] GeorgeZerveas,SrideepikaJayaraman,DhavalPatel,AnuradhaBhamidipaty,
andCarstenEickhoff.2021.Atransformer-basedframeworkformultivariate Asviewconstructionstrategiesmatured,researchattentiongrad-
timeseriesrepresentationlearning.InProceedingsofthe27thACMSIGKDD uallyshiftedtowardthedesignoftheencoderF(·)tobettercap-
conferenceonknowledgediscovery&datamining.2114–2124.
[111] DaozeZhang,ZhizhangYuan,JunruChen,KeruiChen,andYangYang.2024. ture EEG dynamics. Early approaches predominantly relied on
Brant-X:AUnifiedPhysiologicalSignalAlignmentFramework.InProceedings CNN-basedarchitectures[50,58,71],whichprimarilymodello-
ofthe30thACMSIGKDDConferenceonKnowledgeDiscoveryandDataMining.
caltemporalpatterns.Recognizingtheintrinsicallynon-stationary
4155–4166.
[112] DaozeZhang,ZhizhangYuan,YangYang,JunruChen,JingjingWang,and andmulti-scalenatureofneuralsignals,laterworksincorporate
YafengLi.2023.Brant:Foundationmodelforintracranialneuralsignal.Advances temporal–spectraldualityintorepresentationlearning.TF-C[115]
inNeuralInformationProcessingSystems36(2023),26304–26321.
enforcesconsistencybetweentime-domainandfrequency-domain
[113] WenruiZhang,LingYang,ShijiaGeng,andShendaHong.2023.Self-supervised
timeseriesrepresentationlearningviacrossreconstructiontransformer.IEEE embeddingsofthesamesignal,explicitlycouplingcomplementary
TransactionsonNeuralNetworksandLearningSystems(2023). signalviews.Morerecently,transformer-basedencodershavebeen
[114] XiangZhang,LinaYao,XianzhiWang,JessicaMonaghan,DavidMcalpine,and
YuZhang.2021.Asurveyondeeplearning-basednon-invasivebrainsignals: introducedtosupportcross-datasetandcross-subjectlearningat
recentadvancesandnewfrontiers.Journalofneuralengineering18,3(2021), scale.BIOT[105]employsabiosignaltransformertounifyhetero-
031002.
geneousmodalities,whileLEAD[95]furtherregularizesrepresen-
[115] XiangZhang,ZiyuanZhao,TheodorosTsiligkaridis,andMarinkaZitnik.2022.
Self-supervisedcontrastivepre-trainingfortimeseriesviatime-frequency tationsthroughsubject-levelconsistency,encouraginginvariant
consistency.Advancesinneuralinformationprocessingsystems35(2022),3988– embeddingsacrosssamplesfromthesameindividual.
4003.
[116] ZihanZhang,XiaoDing,YuBao,YiZhao,XiaLiang,BingQin,andTingLiu. A.1.2 ContrastivePredictiveCoding. InspiredbyBERTandwav2vec
2024. Chisco:AnEEG-basedBCIdatasetfordecodingofimaginedspeech.
ScientificData11,1(2024),1265. 2.0[6],Bendr[49]encodesEEGsegmentsintoaunifiedsequenceof
[117] Wei-LongZheng,WeiLiu,YifeiLu,Bao-LiangLu,andAndrzejCichocki.2018. learnedvectorrepresentations.Maeeg[18]andGEFM[93]havesimi-
Emotionmeter:Amultimodalframeworkforrecognizinghumanemotions.IEEE
lararchitecturetoBendrwithdifferentPTmindset.AlthoughBendr
transactionsoncybernetics49,3(2018),1110–1122.
[118] Wei-LongZhengandBao-LiangLu.2015.Investigatingcriticalfrequencybands canextractfeatureswell,itignoresspatialinformation.Toaddress
andchannelsforEEG-basedemotionrecognitionwithdeepneuralnetworks. thisissue,severalmodelshavebeenproposed.GEFMaddsagraph
IEEETransactionsonautonomousmentaldevelopment7,3(2015),162–175.
structure to Bendr and proposes a sequence length adjustment
[119] JinzhaoZhou,ZehongCao,YiqunDuan,ConnorBarkley,DanielLeong,Xiaowei
Jiang,Quoc-ToanNguyen,ZiyiZhao,ThomasDo,Yu-ChengChang,etal.2025. mechanismbeforeGNNtomakeEEGsignallengthsconsistentfor
PretrainingLargeBrainLanguageModelforActiveBCI:SilentSpeech.arXiv fixed-lengthnodefeaturesinGNN.Zhuetal.[122]incorporated
preprintarXiv:2504.21214(2025).
[120] XinliangZhou,ChenyuLiu,ZhishengChen,KunWang,YiDing,ZiyuJia,and spatialinformationthroughchannel-mixingaugmentation,effec-
QingsongWen.2025.Brainfoundationmodels:Asurveyonadvancementsin tivelyenhancingdatasetdiversityandimprovingtheperformance
neuralsignalprocessingandbraindiscovery.arXivpreprintarXiv:2503.00580
ofthecontrastiveEEG2Vecframework.Anotherlineofworkex-
(2025).
tendsCPCtobetterexploitmultichannelstructureandcontinual

Shenetal.
datastreams.MBrain[13]augmentsCPCwithspatialawareness A.2.2 Autoencoder. Autoencoderisthemostcommonmethodin
byaggregatingmultichannelsemanticstopredictsingle-channel BFMspretraining.TolearninformativerepresentationsM(𝑥),AE-
localrepresentations,encouragingimplicitspatio-temporaldepen- basedBFMsrelyoncarefullydesigneddisturbancemechanisms
denciesacrosschannels.BrainUICL[121]furthercombinesCPC thatforcereconstructionfrompartialobservations.MaskedAutoen-
withreplay-basedcontinuallearning,andthecontrastivemodelis coders(MAE)[33]randomlymaskinputregionsandreconstruct
incrementallyupdatedviajointtrainingwithreplayedsamples. missingcontentfromvisiblecontext,encouragingthemodelto
captureglobalstructure.InspiredbybothBENDR[49]andMAE,
MAEEG[18]andGEFM[93]adoptmaskedreconstructionforEEG
A.1.3 Cross-modalContrast. Inspiredbymultimodalcontrastive
pretraining.UniEEG[41]furtherintroducesMaskedSignalModel-
learning,BFMsextendcross-modalalignmenttoEEG,where“modal-
ing(MSM)withelectrode-wisemasking,whileEEGPT-1[91]em-
ity”arisesfromtheinherentheterogeneityofbrainrecordings.At
bedslocalspatio-temporalpatchesastokensandproposesadual
theintra-signallevel,differentviewsofthesameEEG(e.g.,raw
SSLobjectivecombiningmask-basedreconstructionwithspatio-
waveformsvs.time–frequencyrepresentations)canserveasdis-
temporalalignment.
tinctmodalities.MuLEEG[50]followsthisparadigmbycontrasting
Beyond masking strategies, modern AE-based BFMs primar-
multi-viewrawsignalswithspectrograms.Beyondview-levelhet-
ilydifferinthedesignoftheencoderF𝜃 (·),whichmustmodel
erogeneity,MCSP[95]minescomplementaryinformationacross 1
long-rangetemporaldependencieswhilecapturingcross-channel
modalitiesandmodelslatentinteractionswithineachdomain,par-
interactions.EarlymodelssuchasBrainBERT[90]largelyencode
ticularlyspatialstructureviagraphs.Fortrulymulti-sensorset-
electrodes independently, limiting spatial coupling. Subsequent
tings,SleepFM[87]jointlyembedsthreebiosignalmodalitiesusing
worksintroducestrongerspatialinductivebiases:EEG2TEXT[60]
bothpairwisecontrastandaleave-one-outobjective,aligningeach
employs multi-view attention to reflect region-wise processing,
modalitytotheaverageoftheothers.Brant-X[111]furthertargets
whileCBraMod[92]adoptsacriss-crossencoderthatalternates
EEG–EXGcouplingbyaligningrepresentationsatbothpatchand
spatial–temporalattentionwithasymmetricconditionalpositional
sequencelevels,capturingcorrelationsatfine-andcoarse-grained
encoding.Tohandleheterogeneousmontages,LUNA[23]unifies
semanticscales.Movingtoheterogeneouscross-modalalignment
variable electrode layouts into a fixed latent space via learned
beyondbiosignals,Ferranteetal.[26]alignneuralrecordingswith
queries,andREVE[81]injectsanatomicalpriorsthrough4Dpo-
visualstimuli,demonstratingthatvisualcontentcanbedecoded
sitionalembeddingsderivedfromelectrodecoordinatesandtime
fromneuraldataandthatimagescanbemappedintoneuralrepre-
indices.Beyondattention-baseddesigns,Mamba-styleencoders
sentationspaces.
enablelinear-timesequencemodelingforlongrecordings.Synth-
SleepNet[52]introducesaMamba-basedTemporalContextMod-
uleforinter-epochdependencies,whileSAMBA[35]proposesa
A.2 Generative-basedMethods
Multi-headDifferentialMambatosuppressbackgroundnoisewhile
A.2.1 Autoregressive. Thesuccessofautoregressive(AR)language aggregatingcontextualinformation.
modelsinmodelinglong-rangedependenciesvianext-tokenpre- However,theinherentrandomness,non-stationarity,andnon-
dictionhasmotivatedtheadoptioninBFMs.Usingadecoder-only linearityofneurophysiologicalsignalsmakedirectamplitudere-
transformerarchitecture,GPT-stylemodels[82]havebeenadapted constructioninthespatiotemporaldomainsuboptimal[99].Asa
toEEGpretraininginseveralBFMs[19,63,91,108].Earlyefforts result,recentBFMsincreasinglyperformmaskingandreconstruc-
suchasNeuro-GPT[19]segmentcontinuousEEGintofixed-length tionintransformedspacesT𝑑(·) orlow-dimensionallatentvari-
chunksandtreateachchunkasatoken,enablingaGPTmodel ables𝑧 𝑖.Neuro2vec[99]pioneersdenoisingintheFourierdomain,
G𝜃 (·) to learn spatio-temporal structure by predicting masked whileCRT[113]performscross-domaindropping–reconstruction
2
segments.Buildingonthisframework,Stress-GPT[63]fine-tunes to align time- and frequency-domain representations. Building
thepretrainedmodelforstress-relatedtasks,demonstratingthe onFourier-domainMAE,Neuro-BERT[100]introducesFourier
transferabilityofAR-pretrainedrepresentations. InversionPrediction(FIP)asapretrainingobjective.Inparallel,
Subsequentworksrefinethetokenizationandpredictionstrategy spectrogram-basedreconstructionhasgainedtractionduetoits
tobetterreflectEEG-specificstructure.EEGPT-2[108]adoptsan richtime–frequencysemantics,supportingbothsignalunderstand-
electrode-wiseautoregressiveformulation,treatingeachelectrode inganddownstreamlearning[78,90,107].
signal𝑥𝑒 asabasictokenandmodelingtemporaldependencies MostAE-basedBFMsaredevelopedfornon-invasiveEEG,while
𝑖
throughanElectrodeTemporalEncoder.EEG2Rep[70]shiftstar- intracranialEEG(iEEG)remainscomparativelyunderexplored.To
getpredictionintolatentspaceviacontext-drivenmaskingand bridgethisgap,BrainBERT[90],Brant[112],andBrainwave[107]
introducesasemanticsubsequencepreservingmechanismtopro- extendAE-basedpretrainingtoSEEGrecordings.BrainBERTlever-
videmoreinformativemaskedinputs.Inspiredbylargelanguage ages SEEG data from subjects watching videos, Brant adopts a
models,NeuroLM[39]generalizesautoregressivepretrainingto dual-encoderMAEtojointlycapturetemporaldependenciesand
multi-channelEEG,explicitlymodelinginter-channeldependencies. spatialcorrelations,andBrainwavescalespretrainingtoover16,000
Morerecently,LBLM[119]unifiestemporalandspectralautore- subjects,settingnewbenchmarksfordiagnosistasks.Whilethese
gressiontocapturespectro-temporaldynamics,whileECHO[59] approachessubstantiallyimproveperformance,theyoftenincrease
constructsdiscrete,prompt-likecontextsupportsencodinghierar- model size. To address this, CEReBrO [22] proposes a compact
chicalsignal–task–labelrelations,improvingin-contextlearning
fordownstreamEEGtasks.

Brain4FMs:ABenchmarkofFoundationModelsforElectricalBrainSignals
encoderthatrepresentsbrainoscillationsthroughalternatingat- A.3.2 Hybrid-based. HybridSSLcombinesmultipleself-supervised
tention, offering a parameter-efficient alternative for AE-based objectiveswithinaunifiedframeworktoexploitcomplementary
BFMs. learningsignals[97].InEEG,Domain-guidedcontrastivelearn-
ing[89]designsSSLpretexttasksgroundedinneurophysiological
A.2.3 Codebook. Thecodebookmechanism,originallyintroduced priors,leveragingsimilarityofbrainactivityaswellasbehavioral-
byVector-QuantizedVariationalAutoencoders(VQ-VAE)[88],of- stateandage-relateddifferences.EEG-DisGCMAE[96]furtherin-
fersakeyadvantageoverstandardVAEsbydiscretizingcontinu- troducesagraph-structuredhybridthatcouplesGraphContrastive
ousrepresentationsintoafinitesetoftokens.Recently,thispar- pretrainingwithGraphMAE.LCM[14]followsadifferentroute,
adigmhasbeenadaptedtoEEGandiEEGmodeling,whereen- usingmaskedgenerativereconstructionastheprimaryobjective
coderoutputsarequantizedintodiscretecodebookentriesviaa andaddingamomentum-updatedtargetencoderwithacontrastive
quantizationoperatorQ∗𝜃 (·)priortodecoding.Suchdiscretiza- termtostabilizerepresentationlearning.Morebroadly,BFMsin-
3
tionenablestoken-basedrepresentationsofneuralsignals,bridg- creasinglypaircontrastiveobjectiveswithgenerativemodelingto
ingcontinuousbiosignalswithsequencemodelingframeworks. jointlyenforcecross-viewconsistencyandpreservesignalstruc-
Thecodebookisoptimizedusingthevector-quantizationobjective: ture[14,52,54,91].Otherhybridsintegratereconstructionwith
L𝑣𝑞 =||𝑠𝑔[Q𝜃
3
(𝑧 𝑖)]−𝑧 𝑖||2
2
+𝛽||𝑠𝑔[𝑧 𝑖]−Q𝜃
3
(𝑧 𝑖)||2
2
where𝑠𝑔[·]de- autoregressivepredictiontocapturebothlocalstructureandlong-
notesthestop-gradientoperator.Comparedtoconventionalmasked rangetemporaldynamics[38,106],andmayfurtherincorporate
reconstruction,vector-quantizedtransformersoftenlearnmoregen- adversarialobjectivesfordomain-awarealignment[39,53].
eralizableneuralrepresentationsandexhibitstrongadaptability
A.3.3 Instruction-tuned. Recent instruction-tuned BFMs bridge
acrossheterogeneousdownstreamtasks.
EEGrepresentationswithlanguagesemanticsthroughlightweight
Acentralchallengeofthisparadigmliesinlearninganeffec-
alignmentmoduleswhilekeepingLLMbackbonesmostlyfrozen.
tive quantization operator Q𝜃 (·). EEGFormer [16] first applies
3 NeuroLM[39]discretizesEEGintotemporal–frequencytokensvia
codebook-baseddiscretizationtoEEGpretraining,generatingdis-
VQencodingandalignsEEGandtextembeddingsthroughdomain-
creteindicesthatyieldtransferableandinterpretablerepresenta-
adversariallearning,followedbymulti-channelautoregressivepre-
tions.LaBraM[40]furtherintroducesaneuralcodebookthatquan-
trainingandprompt-basedmulti-taskinstructiontuning.TaKF+[37]
tizespatch-levelembeddings,withthecodebookoptimizedthrough
emphasizes parameter-efficient transfer by injecting task infor-
reconstructionintheFourierdomain.BioSerenity-E1[10]adoptsa
mationthroughadaptersandcross-attentionblocksaftermasked
transformer-basedVQ-VAEtotokenizeEEGspectraandperforms
patchpretraining.UniMind[66]proposesaNeuro-LanguageCon-
maskedtokenprediction,forcingthemodeltocapturecomplexspa-
nectorthatextractstask-relevanttemporal–spatialsemanticsus-
tiotemporaldependenciesandachievingstate-of-the-artdiagnostic
inglearnable querieswithtask-aware routing,andaligns them
performance.Beyondreconstruction-basedobjectives,NeuroLM
to the LLM latent space for instruction-conditioned generation.
[39] extends this line of work by introducing vector-quantized
WaveMind[109]combinescontrastivemultimodalalignmentwith
time–frequencypredictionandaligningEEGtokenswithtextual
CLIPandinstructiontuningonalargeEEGinstructiondataset,
representationsviaadversarialtraining.Afterdiscretization,item-
enablingconversationalEEGunderstandingacrosstasks.
ploysmulti-channelautoregressivemodeling,enablingLLMsto
predictEEGtokensinamanneranalogoustolanguagemodeling. B Dataset
Whilecodebooklearningisofteninstantiatedwithinautoencoder-
styleframeworks,itshouldbeviewedasageneralrepresentation Thissectionsummarizesadditionaldatasetcharacteristicsomitted
mechanismratherthanamethodspecifictoAE-basedBFMs.Dis- fromthemaintextforbrevity(Table7).Theseattributesreflect
creteneuraltokenscanserveasaunifyinginterfaceacrossrecon- datasetacquisitionprotocolsandareprovidedtofacilitaterepro-
struction,contrastive,andautoregressiveparadigms,motivating ducibilityandpracticalreuseofthebenchmark.Alldatasetsare
theirindependenttreatmentinthisappendix. processedunderconsistentcross-subjectandcross-validationpro-
tocols.Dataset-specificpreprocessingproceduresareimplemented
inouropen-sourcecode.Fortransparencyandreproducibility,the
A.3 OtherAdvancedMethod
completepreprocessingpipelinesforeachdatasetaredocumented
A.3.1 explicit predictive. In the context of EEG, several predic- inthedata_preprocessdirectory.AlldatasetsusedBrain4FMsare
tivetaskshavebeenspecificallyproposedbyupdatingtheform publiclyreleased;ethicsandfairnessconsiderationsaretherefore
ofG𝜃 (·) tobetteralignwithneurophysiologicalcharacteristics. limited,asnonewdatacollectionisinvolved.
2
Domain-guidedCL[89]introducesBehavioralStateEstimation, Tofurthersupporttransparentbenchmarking,pretrainingdata
whichpredictsthedelta-betaratiotocapturearousal-relatedspec- sourcesoftheevaluatedBFMsaredocumentedwheneverdisclosed
tralpatterns.TheStoppedBandPredictionpretexttask[43]focuses bytheoriginalpapersorreleasedcheckpoints.Inselectingdown-
onlearningfrequency-awarerepresentationsbyaskingthemodel streambenchmarks,overlapwithcommonlyusedpretrainingcor-
toidentifywhichfrequencybandhasbeensuppressedinthein- porawasminimizedapriori:mostdownstreamdatasetsaredis-
putsignaltocapturefrequencyinformation.AndtheTemporal jointfromthedominantpretrainingsources(e.g.,TUH[77]/TUEG
TrendIdentificationtask[43]aimstoextracttemporaldynamicsby [32] or large private collections). Potential overlap is therefore
classifyingpre-definedtrends.Althoughthesetasksareneurophys- limitedtoasmallsubsetofmodelsthatincorporateBCI-oriented
iologicallyinterpretable,theirdependenceonspecificassumptions resourcesduringpretraining(e.g.,theSEEDseriesandBCICompe-
aboutsignalbehaviorhasstilllimitedtheiradoptioninBFMs. titionIV,overlappingwithSEED-IVandBCI-2a).Inaddition,some

Shenetal.
models leverage task-related corpora for AD, SD, or sleep stag- AUROC,Accuracy,F1,andF2tocapturethreshold-freediscrimina-
ingpretraining.Thedownstreamdatasetswerecuratedtoavoid tionandpositive-classdetectionunderimbalance.Formulti-class
directdataset-levelreuseinthesecategorieswheneverpossible. tasks,wereportAccuracy,AUROC(one-vs-rest;OvR),macro-F1
Brain4FMsevaluatesmodelsasreleasedunderunifiedprotocols (MF1),andCohen’s𝜅(Kappa)tomeasureoveralldiscrimination,
ratherthanre-pretrainingleave-dataset-outvariants.Empirically, class-wiseperformance,andagreementbeyondchance.Wereport
performancedifferencescannotbeexplainedbypartialoverlap resultsasmean±standarddeviationovern-foldcross-validation,
aloneunderthestandardizedcross-subjectfine-tuningsetting,sug- andboldindicatesthebestperformancebasedonunroundedval-
ues.Allmetricsusetwodecimalplaces,exceptCohen’s𝜅,which
gestingthatpretrainingscale,datadiversity,SSLobjectives,and
architecturalchoicesalsocontribute. usesthreedecimalsduetoitssmallmagnitudeonsomedatasets.
InTables8to29,modelsaregroupedbySSLparadigmandsorted
Table7:PublicEEG/iEEGdatasetsusedinthebenchmark,listing
bytheprimarymetricwithineachgroup.
thenumberofchannels(#Ch),sequencelength(SeqLen),sampling
frequency,totalrecordingduration,anddatasetcategory.
| Name | #Ch SeqLen | Frequency | TotalTime Category |     |     |     |
| ---- | ---------- | --------- | ------------------ | --- | --- | --- |
Table8:PerformanceofBFMsontheCHBMITdataset.
| CHBMIT[30] | 23 10s | 256       | 686h 2    |            |           |       |
| ---------- | ------ | --------- | --------- | ---------- | --------- | ----- |
| MAYO[75]   | 1 3s   | 5000→1000 | 94.38h 2  |            |           |       |
|            |        |           |           | Type Model | AUROC Acc | F1 F2 |
| FNUSA[75]  | 1 3s   | 5000→1000 | 149.69h 2 |            |           |       |
Dep-BDI[36] 64 10s 500→250 31.5h 2 C MBrain .71±.03 .73±.06 .31±.15 .28±.20
|              |        |         |          | BIOT  | .56±.08 .29±.05 | .41±.03 .61±.02 |
| ------------ | ------ | ------- | -------- | ----- | --------------- | --------------- |
| Dep-STAI[36] | 64 10s | 500→250 | 31.5h 3  |       |                 |                 |
|              |        |         |          | Bendr | .55±.03 .59±.03 | .32±.02 .36±.04 |
| MDD-64[73]   | 19 10s | 256     | 20.53h 2 |       |                 |                 |
SD-28[102] 19 5s 250 958min 2 SppEEGNet .43±.05 .60±.06 .31±.04 .33±.05
UCSD-ON[84] 32 10s 512→256 220min 2 .90±.03 .80±.12 .71±.09 .78±.04
G BrainWave
UCSD-OFF[84] 32 10s 512→256 220min 2 REVE .84±.10 .78±.12 .63±.14 .66±.13
ADFD[69] 19 10s 500→250 1164min 2 NeuroGPT-E .78±.12 .75±.07 .51±.22 .63±.16
ADHD_Adult[7] 2 5s 256 423min 2 BrainBERT .78±.06 .75±.10 .58±.08 .61±.09
ADHD_Child[72] 19 5s 128 274.5min 2 LaBraM .75±.10 .73±.10 .53±.14 .57±.17
| ISRUC-G1[46] | 6 30s | 200 | 744.5h 5 |           |                 |                 |
| ------------ | ----- | --- | -------- | --------- | --------------- | --------------- |
|              |       |     |          | BrainOmni | .74±.13 .67±.19 | .51±.12 .56±.12 |
SleepEDF[45] 1 30s 100 378.7h 5 BFM .74±.05 .72±.03 .51±.09 .51±.14
DEAP[48] 32 10s 128 2133min 4 CBraMod .69±.04 .70±.08 .46±.08 .49±.14
SEED-IV[117] 62 4s 200 54h 4 NeuroGPT-D .61±.07 .73±.03 .18±.23 .19±.25
EEGMat[123] 32 10s 500→250 144min 2 Brant .55±.05 .70±.01 .00±.00 .00±.00
EEGMMIDB-R[29] 64 4s 160 2834min 4 O EEGPT .71±.09 .67±.11 .46±.06 .51±.15
| EEGMMIDB-I[29] | 64 4s    | 160 | 2834min 4 |         |                 |                 |
| -------------- | -------- | --- | --------- | ------- | --------------- | --------------- |
|                |          |     |           | NeuroLM | .67±.06 .54±.20 | .27±.23 .38±.34 |
| BCI-2a[11]     | 22 3s    | 250 | 130min 4  |         |                 |                 |
| Chisco-R[116]  | 125 3.3s | 500 | 58.6h 39  |         |                 |                 |
| Chisco-I[116]  | 125 3.3s | 500 | 58.6h 39  |         |                 |                 |
C ExperimentalSetup
Weevaluateallmodelsunderaunifiedcross-subjectprotocolwith
cross-validation,followingstandardpracticeinbenchmarks.Mod- Table9:PerformanceofBFMsontheMAYOdataset.
elsarefinetunedforupto50epochswithearlystopping(patience=
5)basedonvalidationperformance.Foroptimization,weprimarily
|     |     |     |     | Type Model | AUROC Acc | F1 F2 |
| --- | --- | --- | --- | ---------- | --------- | ----- |
useAdamorAdamW.ForasmallnumberofBFMs,weretaintheir
originaloptimizersasspecifiedbytheauthorstoavoidunintended C Bendr .93±.03 .90±.02 .69±.13 .75±.11
|     |     |     |     | MBrain | .92±.04 .92±.02 | .70±.11 .73±.09 |
| --- | --- | --- | --- | ------ | --------------- | --------------- |
performancedegradationcausedbyalteringmodelspecifictraining
|     |     |     |     | BIOT | .90±.07 .88±.05 | .63±.14 .72±.13 |
| --- | --- | --- | --- | ---- | --------------- | --------------- |
designs.Batchsizesareadjustedaccordingtomodelcapacityand SppEEGNet .56±.03 .75±.05 .34±.09 .39±.09
GPUmemoryconstraints.Toensurecomparabilityandavoidexces- .98±.01 .86±.03
|     |     |     |     | G BrainWave | .93±.02 | .81±.09 |
| --- | --- | --- | --- | ----------- | ------- | ------- |
sivetuning,weusefixedlearningratesacrossallmodels:1×10−5 BrainBERT .97±.01 .95±.01 .81±.07 .83±.07
fortheBFMsbackboneand1×10−4fortheclassifierhead. LaBraM .96±.02 .93±.02 .76±.12 .80±.09
|                   |     |     |     | NeuroGPT-E | .96±.02 .93±.02 | .71±.07 .67±.08 |
| ----------------- | --- | --- | --- | ---------- | --------------- | --------------- |
| D BenchmarkResult |     |     |     | REVE       | .92±.04 .89±.04 | .66±.13 .72±.11 |
|                   |     |     |     | Brant      | .92±.03 .82±.12 | .58±.19 .69±.14 |
Wereportthecompleteevaluationresultsofall15BFMsacross BrainOmni .91±.06 .91±.02 .67±.13 .69±.12
22downstreamclassificationtasks.ForNeuroGPT,wereportboth CBraMod .89±.04 .87±.02 .59±.12 .64±.10
|     |     |     |     | BFM | .81±.08 .68±.08 | .43±.15 .59±.14 |
| --- | --- | --- | --- | --- | --------------- | --------------- |
encoder-only(NeuroGPT-E)andencoder–decoder(NeuroGPT-D)
|     |     |     |     | NeuroGPT-D | .77±.15 .88±.03 | .23±.26 .19±.21 |
| --- | --- | --- | --- | ---------- | --------------- | --------------- |
variants,complementingtheanalysisinSection3.3.2.Fullresults
|     |     |     |     | O EEGPT | .92±.03 .90±.03 | .67±.10 .70±.07 |
| --- | --- | --- | --- | ------- | --------------- | --------------- |
providecomprehensiveevidencefortheobservedcross-taskper-
|     |     |     |     | NeuroLM | .64±.09 .72±.16 | .30±.20 .37±.26 |
| --- | --- | --- | --- | ------- | --------------- | --------------- |
formancetrendsamongdifferentBFMs.Forbinarytasks,wereport

Brain4FMs:ABenchmarkofFoundationModelsforElectricalBrainSignals
Table10:PerformanceofBFMsontheFNUSAdataset. Table13:PerformanceofBFMsontheADHD-Childdataset.
Type Model AUROC Acc F1 F2 Type Model AUROC Acc F1 F2
C MBrain .91±.08 .87±.08 .75±.13 .76±.16 C MBrain .69±.11 .63±.08 .66±.06 .66±.04
Bendr .88±.06 .84±.06 .73±.11 .77±.10 BIOT .55±.05 .75±.06 .85±.04 .93±.02
BIOT .87±.07 .83±.08 .73±.14 .77±.10 SppEEGNet .53±.05 .49±.04 .48±.07 .45±.08
SppEEGNet .64±.08 .67±.05 .48±.13 .52±.18 Bendr .53±.02 .51±.01 .52±.02 .49±.02
G BrainWave .92±.05 .89±.06 .83±.06 .83±.04 G REVE .79±.07 .71±.04 .74±.06 .74±.08
NeuroGPT-E .90±.06 .86±.05 .74±.04 .72±.11 BrainWave .78±.04 .71±.04 .74±.06 .74±.12
BrainBERT .90±.04 .89±.04 .77±.09 .79±.08 BrainOmni .71±.09 .62±.07 .63±.09 .61±.14
LaBraM .89±.08 .82±.10 .72±.15 .76±.11 BFM .69±.11 .69±.09 .75±.07 .75±.04
BrainOmni .88±.07 .84±.05 .73±.08 .75±.09 LaBraM .66±.12 .64±.08 .74±.06 .70±.07
REVE .87±.08 .82±.07 .71±.10 .74±.08 CBraMod .64±.05 .64±.06 .73±.03 .81±.05
Brant .87±.12 .84±.07 .75±.06 .79±.08 Brant .58±.07 .54±.07 .62±.15 .68±.23
BFM .78±.12 .69±.11 .62±.05 .69±.08 NeuroGPT-E .55±.02 .56±.03 .72±.02 .86±.01
NeuroGPT-D .72±.12 .77±.12 .30±.38 .27±.35 BrainBERT .55±.03 .56±.03 .56±.07 .53±.09
CBraMod .71±.13 .78±.08 .62±.13 .64±.12 NeuroGPT-D .47±.12 .56±.06 .64±.11 .69±.18
O EEGPT .90±.04 .84±.06 .75±.11 .78±.08 O EEGPT .67±.13 .64±.10 .68±.10 .68±.12
NeuroLM .64±.14 .72±.17 .37±.28 .38±.35 NeuroLM .64±.06 .60±.05 .71±.04 .80±.05
Table11:PerformanceofBFMsontheADFDdataset. Table14:PerformanceofBFMsontheUCSD-OFFdataset.
Type Model AUROC Acc F1 F2 Type Model AUROC Acc F1 F2
C BIOT .56±.17 .49±.12 .58±.14 .70±.24 C SppEEGNet .53±.07 .51±.06 .59±.15 .71±.25
MBrain .53±.12 .50±.10 .53±.12 .52±.14 Bendr .52±.04 .51±.03 .48±.05 .47±.05
Bendr .52±.02 .52±.01 .54±.05 .52±.07 BIOT .51±.19 .49±.05 .56±.27 .69±.35
SppEEGNet .52±.02 .51±.02 .51±.05 .49±.07 MBrain .50±.04 .44±.04 .32±.23 .34±.29
G REVE .84±.07 .77±.08 .79±.07 .79±.09 G BrainOmni .64±.09 .57±.06 .54±.16 .57±.26
BrainOmni .80±.07 .71±.04 .73±.05 .72±.09 CBraMod .63±.05 .58±.04 .46±.09 .40±.12
BrainWave .74±.05 .68±.05 .68±.10 .73±.10 REVE .62±.19 .58±.17 .58±.19 .60±.24
LaBraM .72±.07 .68±.05 .68±.09 .72±.07 LaBraM .59±.05 .56±.03 .57±.08 .60±.15
BrainBERT .59±.05 .58±.05 .60±.11 .64±.15 BrainWave .58±.06 .53±.10 .62±.12 .71±.19
BFM .59±.08 .58±.09 .59±.12 .61±.09 NeuroGPT-E .56±.06 .54±.05 .57±.12 .62±.22
CBraMod .55±.06 .59±.04 .41±.20 .37±.20 BFM .53±.03 .49±.12 .36±.09 .47±.17
NeuroGPT-E .51±.03 .55±.01 .71±.01 .85±.01 Brant .52±.10 .45±.22 .42±.29 .58±.35
Brant .50±.07 .54±.04 .70±.03 .84±.04 BrainBERT .51±.06 .54±.06 .49±.17 .49±.20
NeuroGPT-D .50±.03 .55±.01 .71±.01 .86±.01 NeuroGPT-D .45±.07 .51±.05 .01±.01 .00±.01
O EEGPT .81±.05 .72±.05 .73±.05 .70±.07 O EEGPT .61±.13 .55±.08 .56±.10 .58±.17
NeuroLM .51±.04 .53±.03 .63±.09 .71±.16 NeuroLM .51±.07 .50±.05 .53±.15 .61±.23
Table12:PerformanceofBFMsontheADHD-Adultdataset. Table15:PerformanceofBFMsontheUCSD-ONdataset.
Type Model AUROC Acc F1 F2 Type Model AUROC Acc F1 F2
C BIOT .96±.02 .90±.04 .89±.04 .90±.05 C Bendr .51±.05 .49±.05 .43±.05 .41±.06
MBrain .95±.03 .92±.04 .91±.04 .91±.06 SppEEGNet .49±.08 .50±.11 .46±.23 .48±.27
Bendr .62±.03 .61±.04 .60±.05 .61±.06 MBrain .49±.15 .46±.14 .37±.17 .34±.18
SppEEGNet .51±.04 .54±.06 .36±.30 .36±.35 BIOT .46±.18 .49±.05 .65±.05 .81±.04
G BrainOmni .96±.02 .91±.02 .90±.03 .89±.04 G BrainWave .69±.20 .53±.08 .60±.06 .69±.14
BrainWave .96±.03 .91±.04 .91±.04 .91±.05 REVE .63±.19 .56±.13 .45±.29 .46±.33
REVE .96±.02 .91±.02 .91±.02 .90±.05 CBraMod .60±.12 .49±.08 .18±.08 .13±.07
Brant .95±.03 .89±.04 .89±.04 .90±.05 NeuroGPT-E .56±.10 .53±.07 .58±.10 .64±.13
LaBraM .95±.04 .91±.04 .92±.04 .91±.04 Brant .56±.11 .52±.11 .29±.28 .31±.34
CBraMod .95±.02 .92±.04 .91±.04 .91±.07 BrainOmni .53±.14 .49±.12 .49±.16 .51±.20
NeuroGPT-E .91±.05 .84±.06 .83±.05 .82±.03 LaBraM .51±.22 .45±.11 .33±.19 .31±.19
BFM .88±.04 .82±.04 .80±.04 .81±.05 BrainBERT .51±.05 .51±.06 .51±.11 .54±.17
NeuroGPT-D .88±.05 .82±.05 .82±.04 .85±.03 NeuroGPT-D .46±.10 .47±.06 .29±.25 .31±.28
BrainBERT .74±.05 .69±.05 .61±.11 .57±.14 BFM .44±.08 .48±.07 .42±.17 .42±.20
O EEGPT .96±.03 .91±.04 .90±.05 .89±.08 O EEGPT .51±.21 .48±.17 .49±.15 .49±.14
NeuroLM .82±.14 .75±.07 .74±.06 .77±.11 NeuroLM .44±.18 .51±.18 .47±.24 .48±.29

Shenetal.
Table16:PerformanceofBFMsontheEEGMatdataset. Table19:PerformanceofBFMsontheDep-BDIdataset.
| Type Model | AUROC Acc | F1 F2 | Type Model | AUROC Acc | F1 F2 |
| ---------- | --------- | ----- | ---------- | --------- | ----- |
C MBrain .68±.06 .75±.02 .13±.15 .10±.11 C BIOT .60±.11 .30±.17 .11±.02 .22±.05
BIOT .59±.08 .27±.01 .42±.01 .65±.01 MBrain .59±.07 .62±.03 .24±.16 .20±.16
Bendr .54±.02 .66±.05 .34±.07 .34±.06 Bendr .54±.03 .54±.03 .45±.03 .47±.03
SppEEGNet .52±.03 .50±.07 .37±.04 .47±.09 SppEEGNet .50±.02 .49±.04 .41±.04 .45±.04
|        | .78±.09 .75±.08 |                 |             | .72±.03 | .62±.03 |
| ------ | --------------- | --------------- | ----------- | ------- | ------- |
| G REVE |                 | .39±.27 .61±.09 | G BrainWave | .66±.03 | .67±.06 |
LaBraM .71±.03 .68±.04 .48±.07 .53±.13 BrainOmni .68±.12 .63±.09 .55±.10 .58±.13
NeuroGPT-E .70±.04 .73±.04 .25±.20 .22±.20 REVE .67±.12 .65±.08 .47±.14 .45±.17
BrainOmni .68±.07 .60±.07 .48±.04 .60±.06 LaBraM .65±.10 .59±.11 .60±.09 .71±.08
BrainWave .66±.06 .51±.20 .44±.07 .55±.08 BrainBERT .64±.09 .61±.05 .48±.11 .48±.12
CBraMod .63±.06 .72±.04 .19±.18 .16±.17 BFM .62±.10 .59±.06 .48±.10 .51±.13
BrainBERT .61±.07 .67±.06 .45±.09 .50±.13 NeuroGPT-E .59±.08 .62±.01 .02±.02 .01±.01
BFM .60±.03 .66±.04 .35±.06 .36±.10 CBraMod .54±.05 .69±.14 .13±.08 .16±.10
Brant .57±.12 .75±.01 .00±.00 .00±.00 Brant .53±.09 .62±.01 .00±.00 .00±.00
NeuroGPT-D .51±.06 .73±.01 .00±.00 .00±.00 NeuroGPT-D .51±.08 .62±.01 .00±.00 .00±.00
O EEGPT .67±.04 .64±.06 .49±.02 .59±.04 O EEGPT .63±.04 .62±.05 .50±.05 .51±.11
NeuroLM .63±.08 .31±.10 .42±.04 .64±.04 NeuroLM .54±.05 .61±.02 .30±.26 .31±.31
Table17:PerformanceofBFMsontheSD-28dataset.
Table20:PerformanceofBFMsontheDep-STAIdataset.
| Type Model | AUROC Acc | F1 F2 | Type Model | AUROC Acc | MF1 Kappa |
| ---------- | --------- | ----- | ---------- | --------- | --------- |
C MBrain .58±.10 .58±.10 .64±.13 .66±.15 C BIOT .56±.09 .37±.07 .33±.07 .073±.088
| BIOT  | .56±.09 .62±.12 | .68±.18 .65±.21 |        |                 |                   |
| ----- | --------------- | --------------- | ------ | --------------- | ----------------- |
|       |                 |                 | MBrain | .55±.04 .60±.03 | .30±.05 .054±.059 |
| Bendr | .49±.05 .50±.03 | .48±.05 .45±.04 |        |                 |                   |
|       |                 |                 | Bendr  | .54±.03 .48±.03 | .36±.03 .047±.041 |
SppEEGNet .49±.03 .47±.04 .33±.06 .27±.05 SppEEGNet .51±.02 .46±.03 .33±.01 .007±.024
|     | .88±.07 .81±.06 | .83±.08 |     |     |     |
| --- | --------------- | ------- | --- | --- | --- |
G BrainWave .81±.11 G BrainWave .64±.06 .51±.05 .42±.05 .150±.053
| REVE | .81±.13 .75±.13 | .80±.10 .86±.11 |            |                 |                   |
| ---- | --------------- | --------------- | ---------- | --------------- | ----------------- |
|      |                 |                 | NeuroGPT-E | .61±.09 .55±.07 | .38±.10 .129±.155 |
NeuroGPT-D .80±.17 .77±.13 .80±.11 .84±.14 LaBraM .61±.09 .36±.10 .26±.06 .081±.093
BrainBERT .73±.11 .66±.15 .63±.26 .62±.29 BrainBERT .60±.06 .48±.11 .32±.08 .064±.126
NeuroGPT-E .72±.12 .66±.14 .73±.15 .69±.19 BrainOmni .60±.06 .53±.05 .36±.05 .105±.062
BrainOmni .69±.15 .69±.12 .73±.14 .77±.19 BFM .58±.08 .45±.09 .37±.06 .099±.117
| BFM | .69±.15 .62±.05 | .73±.04 .81±.08 |            | .61±.01 |                   |
| --- | --------------- | --------------- | ---------- | ------- | ----------------- |
|     |                 |                 | NeuroGPT-D | .57±.06 | .25±.00 .000±.000 |
CBraMod .54±.14 .58±.05 .58±.18 .58±.24 REVE .54±.11 .54±.10 .35±.08 .079±.200
LaBraM .54±.07 .54±.04 .59±.07 .59±.13 CBraMod .54±.04 .60±.02 .30±.04 .049±.052
Brant .51±.11 .46±.08 .47±.17 .50±.30 Brant .53±.03 .61±.01 .25±.00 .000±.000
O EEGPT .56±.21 .56±.11 .62±.12 .66±.15 O EEGPT .56±.06 .51±.06 .34±.06 .025±.080
NeuroLM .49±.04 .49±.05 .53±.28 .62±.35 NeuroLM .50±.04 .58±.04 .26±.02 .009±.018
Table18:PerformanceofBFMsontheMDD-64dataset.
Table21:PerformanceofBFMsontheISRUC-G1dataset.
| Type Model | AUROC Acc | F1 F2 | Type Model | AUROC Acc | MF1 Kappa |
| ---------- | --------- | ----- | ---------- | --------- | --------- |
C MBrain .93±.08 .87±.11 .89±.08 .91±.05 C MBrain .87±.04 .63±.07 .55±.07 .514±.084
| Bendr | .78±.07 .73±.04 | .75±.03 .76±.04 |       |                 |                   |
| ----- | --------------- | --------------- | ----- | --------------- | ----------------- |
|       |                 |                 | BIOT  | .78±.04 .46±.07 | .44±.02 .322±.071 |
| BIOT  | .53±.12 .33±.01 | .50±.01 .71±.00 |       |                 |                   |
|       |                 |                 | Bendr | .72±.04 .43±.07 | .39±.05 .269±.076 |
SppEEGNet .52±.02 .55±.04 .50±.05 .45±.05 SppEEGNet .53±.01 .17±.03 .15±.02 .012±.009
|           | .97±.04 .88±.09 | .90±.06 .92±.04 |           |                 |                   |
| --------- | --------------- | --------------- | --------- | --------------- | ----------------- |
| G REVE    |                 |                 | G REVE    | .92±.01 .69±.03 | .65±.05 .598±.036 |
| BrainOmni | .94±.07 .85±.09 | .87±.07 .89±.05 |           |                 |                   |
|           |                 |                 | BrainOmni | .91±.02 .68±.03 | .64±.04 .581±.030 |
BrainWave .94±.03 .85±.02 .84±.03 .81±.06 BrainWave .89±.01 .62±.05 .60±.02 .522±.064
BFM .93±.08 .86±.11 .88±.08 .91±.05 CBraMod .86±.05 .54±.08 .48±.10 .419±.094
BrainBERT .92±.07 .85±.07 .85±.06 .85±.10 LaBraM .85±.02 .61±.02 .56±.05 .502±.028
Brant .92±.09 .80±.10 .80±.14 .80±.19 Brant .84±.02 .55±.01 .50±.04 .427±.016
| CBraMod | .90±.13 .84±.12 | .86±.09 .87±.09 |            |                 |                   |
| ------- | --------------- | --------------- | ---------- | --------------- | ----------------- |
|         |                 |                 | NeuroGPT-E | .80±.02 .44±.11 | .41±.11 .319±.101 |
LaBraM .87±.12 .81±.11 .78±.09 .83±.04 BrainBERT .80±.03 .47±.05 .42±.07 .332±.058
NeuroGPT-E .87±.05 .80±.05 .84±.03 .90±.03 BFM .78±.03 .47±.04 .37±.13 .264±.148
NeuroGPT-D .70±.12 .67±.13 .77±.07 .89±.04 NeuroGPT-D .61±.07 .31±.07 .17±.08 .060±.102
| O EEGPT | .94±.05 .87±.08 | .88±.06 .90±.04 |         |                 |                   |
| ------- | --------------- | --------------- | ------- | --------------- | ----------------- |
|         |                 |                 | O EEGPT | .87±.02 .60±.05 | .57±.08 .486±.070 |
NeuroLM .82±.11 .80±.06 .80±.09 .81±.18 NeuroLM .67±.05 .27±.11 .15±.10 .074±.074

Brain4FMs:ABenchmarkofFoundationModelsforElectricalBrainSignals
Table22:PerformanceofBFMsontheSleepEDFdataset. Table25:PerformanceofBFMsontheEEGMMIDB-Rdataset.
Type Model AUROC Acc MF1 Kappa Type Model AUROC Acc MF1 Kappa
C MBrain .94±.01 .79±.04 .73±.05 .709±.059 C Bendr .55±.01 .29±.01 .29±.01 .060±.014
Bendr .91±.01 .69±.06 .65±.04 .591±.062 SppEEGNet .52±.00 .26±.01 .24±.01 .014±.008
BIOT .58±.16 .35±.16 .21±.12 .070±.145 MBrain .52±.01 .26±.01 .19±.05 .008±.016
SppEEGNet .57±.01 .22±.01 .20±.01 .104±.028 BIOT .50±.01 .25±.01 .21±.02 .003±.011
G NeuroGPT-E .94±.01 .78±.03 .70±.03 .696±.045 G REVE .82±.00 .59±.01 .58±.01 .448±.014
Brant .94±.01 .73±.07 .70±.05 .639±.083 NeuroGPT-E .77±.02 .54±.02 .53±.02 .381±.030
CBraMod .93±.01 .73±.04 .69±.04 .642±.054 BrainOmni .74±.01 .49±.01 .49±.01 .325±.014
LaBraM .93±.01 .76±.04 .68±.03 .669±.050 CBraMod .57±.01 .30±.02 .27±.03 .061±.022
BrainBERT .91±.02 .68±.07 .65±.05 .578±.079 LaBraM .55±.02 .28±.02 .23±.03 .041±.027
BrainWave .89±.02 .67±.05 .54±.08 .516±.104 BFM .52±.01 .27±.01 .26±.01 .024±.008
BFM .89±.01 .65±.04 .60±.03 .558±.053 NeuroGPT-D .50±.00 .25±.00 .14±.01 .003±.003
BrainOmni .87±.00 .63±.03 .60±.01 .506±.025 Brant .50±.01 .25±.00 .10±.00 .000±.000
REVE .78±.38 .63±.30 .60±.28 .561±.257 BrainWave .50±.01 .25±.01 .17±.02 -.004±.011
NeuroGPT-D .65±.03 .48±.04 .21±.05 .100±.068 BrainBERT .50±.01 .25±.00 .16±.03 .001±.006
O EEGPT .91±.00 .68±.03 .66±.01 .578±.026 O NeuroLM .52±.02 .26±.01 .14±.05 .009±.017
NeuroLM .61±.06 .18±.04 .11±.03 .189±.263 EEGPT .51±.01 .25±.01 .23±.03 .006±.017
Table23:PerformanceofBFMsontheBCI-2adataset. Table26:PerformanceofBFMsontheDEAPdataset.
Type Model AUROC Acc MF1 Kappa Type Model AUROC Acc MF1 Kappa
C MBrain .54±.02 .27±.02 .19±.03 .027±.023 C SppEEGNet .51±.03 .27±.06 .23±.03 .007±.027
Bendr .51±.01 .25±.01 .25±.01 .005±.011 MBrain .51±.05 .42±.04 .15±.01 .000±.000
SppEEGNet .51±.01 .25±.01 .24±.02 .003±.020 BIOT .50±.03 .30±.06 .18±.02 -.014±.030
BIOT .50±.01 .24±.02 .17±.02 -.015±.022 Bendr .50±.02 .26±.02 .24±.02 -.004±.035
G REVE .61±.01 .34±.01 .30±.02 .115±.012 G BrainBERT .52±.02 .23±.02 .18±.03 .017±.020
NeuroGPT-E .61±.02 .35±.03 .33±.02 .128±.041 NeuroGPT-D .51±.03 .44±.04 .15±.01 .000±.000
LaBraM .55±.03 .28±.02 .23±.04 .045±.027 BrainWave .51±.03 .27±.07 .23±.06 .010±.077
Brant .54±.00 .25±.00 .10±.00 .000±.000 CBraMod .51±.01 .19±.02 .14±.02 -.001±.009
BrainWave .54±.02 .27±.02 .20±.03 .031±.022 LaBraM .51±.02 .29±.04 .21±.03 .016±.014
BrainOmni .54±.01 .27±.02 .22±.02 .021±.029 REVE .50±.05 .26±.05 .21±.03 -.013±.035
CBraMod .54±.01 .27±.01 .20±.02 .022±.012 BFM .50±.02 .28±.07 .22±.02 .005±.015
BFM .51±.01 .26±.01 .25±.00 .013±.012 NeuroGPT-E .49±.01 .42±.03 .17±.03 -.004±.006
NeuroGPT-D .51±.03 .26±.01 .15±.03 .007±.019 Brant .48±.02 .34±.17 .12±.06 .000±.000
BrainBERT .50±.01 .25±.02 .23±.02 .005±.023 BrainOmni .45±.03 .22±.03 .19±.01 -.046±.022
O EEGPT .57±.03 .28±.02 .22±.01 .036±.024 O NeuroLM .51±.03 .33±.13 .13±.03 -.003±.007
NeuroLM .52±.02 .27±.01 .20±.02 .030±.018 EEGPT .50±.02 .26±.05 .22±.04 .029±.027
Table24:PerformanceofBFMsontheEEGMMIDB-Idataset. Table27:PerformanceofBFMsontheSEED-IVdataset.
Type Model AUROC Acc MF1 Kappa Type Model AUROC Acc MF1 Kappa
C Bendr .55±.01 .29±.01 .29±.01 .054±.010 C MBrain .52±.01 .26±.01 .21±.04 .014±.020
MBrain .51±.01 .26±.01 .16±.05 .009±.011 Bendr .50±.00 .25±.00 .25±.00 -.001±.005
SppEEGNet .51±.01 .26±.01 .23±.01 .008±.013 SppEEGNet .50±.00 .25±.00 .24±.00 -.001±.002
BIOT .50±.01 .25±.00 .20±.02 -.005±.004 BIOT .48±.00 .24±.01 .19±.02 -.018±.003
G REVE .82±.01 .59±.02 .59±.02 .451±.031 G NeuroGPT-E .57±.01 .30±.01 .26±.02 .003±.005
NeuroGPT-E .78±.01 .54±.01 .54±.01 .392±.019 REVE .54±.01 .28±.02 .27±.01 .039±.019
BrainOmni .76±.01 .51±.01 .51±.01 .351±.019 BrainOmni .53±.01 .28±.02 .26±.01 .035±.019
LaBraM .59±.02 .31±.02 .25±.03 .078±.032 BrainWave .53±.02 .27±.02 .22±.03 .023±.026
CBraMod .58±.02 .30±.02 .28±.04 .073±.028 BFM .52±.01 .27±.01 .24±.01 .012±.004
BFM .52±.01 .27±.01 .26±.01 .023±.009 CBraMod .51±.01 .26±.01 .21±.03 .010±.010
BrainWave .51±.01 .25±.01 .18±.01 .001±.014 BrainBERT .51±.03 .25±.02 .17±.05 .003±.012
Brant .51±.01 .25±.00 .10±.00 .000±.000 LaBraM .51±.01 .25±.01 .20±.02 .008±.014
BrainBERT .49±.00 .25±.00 .16±.02 -.003±.005 NeuroGPT-D .50±.00 .27±.00 .11±.00 .000±.000
NeuroGPT-D .49±.01 .25±.01 .16±.05 -.007±.008 Brant .50±.01 .26±.01 .10±.00 .000±.000
O EEGPT .52±.01 .27±.02 .24±.04 .023±.022 O EEGPT .51±.01 .25±.01 .22±.02 .006±.016
NeuroLM .51±.01 .25±.01 .15±.05 .005±.008 NeuroLM .50±.00 .25±.00 .13±.04 .001±.002

Shenetal.
Table28:PerformanceofBFMsontheChisco-Idataset. Table30:Fullquantitativeresultsofdecision-boundarydiag-
|     |     |     |     |     | nostics.Thetablereports𝐿𝑀 |     | 𝐸𝑅,𝐿𝑀 | 𝐸𝑆,and𝑅 𝑐𝑙𝑠 forallcontrastive- |     |
| --- | --- | --- | --- | --- | ------------------------- | --- | ----- | ------------------------------ | --- |
andgenerative-basedmodels(q=0.10).
| Type Model | AUROC   | Acc     | MF1     | Kappa      |       |             |             |             |                   |
| ---------- | ------- | ------- | ------- | ---------- | ----- | ----------- | ----------- | ----------- | ----------------- |
| C MBrain   | .50±.01 | .03±.00 | .00±.00 | .000±.001  |       |             |             |             |                   |
| Bendr      | .50±.01 | .03±.00 | .02±.00 | .000±.002  |       | ADFD        | CHBMIT      |             | SD-28             |
| SppEEGNet  | .50±.00 | .02±.00 | .01±.00 | -.000±.001 |       |             |             |             |                   |
|            |         |         |         |            | Model | 𝐿𝑀 𝐸𝑅 𝐿𝑀 𝐸𝑆 | 𝑅 𝑐𝑙𝑠 𝐿𝑀 𝐸𝑅 | 𝐿𝑀 𝐸𝑆 𝑅 𝑐𝑙𝑠 | 𝐿𝑀 𝐸𝑅 𝐿𝑀 𝐸𝑆 𝑅 𝑐𝑙𝑠 |
| BIOT       | .49±.00 | .03±.01 | .01±.00 | .000±.001  |       |             |             |             |                   |
G LaBraM .51±.01 .04±.01 .01±.00 .005±.004 SppEEGNet .497 .107 0.658 .483 .127 2.208 .490 .098 1.557
CBraMod .51±.01 .04±.01 .01±.00 .003±.003 Bendr .499 .105 0.658 .497 .117 0.962 .488 .994 0.941
BrainOmni .50±.01 .02±.00 .01±.00 .001±.001 BIOT .470 .098 2.344 .615 .087 2.328 .497 .112 2.865
BFM .50±.00 .03±.00 .01±.00 .001±.001 MBrain .526 .113 1.980 .550 .219 2.047 .480 .103 2.590
NeuroGPT-D .50±.00 .05±.00 .00±.00 .001±.004 BrainBERT .492 .126 0.842 .457 .203 2.103 .478 .157 2.091
| BrainBERT | .50±.01 | .03±.00 | .01±.01 | .001±.003 |           |           |            |            |                 |
| --------- | ------- | ------- | ------- | --------- | --------- | --------- | ---------- | ---------- | --------------- |
|           |         |         |         |           | BrainWave | .455 .172 | 2.275 .499 | .197 2.613 | .409 .179 3.229 |
| REVE      | .50±.00 | .03±.00 | .02±.00 | .000±.001 |           |           |            |            |                 |
.05±.00 CBraMod .492 .109 1.892 .445 .161 2.207 .456 .097 2.510
| NeuroGPT-E | .50±.01 |         | .00±.00 | -.000±.004 |           |           |            |            |                 |
| ---------- | ------- | ------- | ------- | ---------- | --------- | --------- | ---------- | ---------- | --------------- |
|            |         |         |         |            | BrainOmni | .487 .175 | 3.465 .469 | .173 2.558 | .376 .122 3.546 |
| BrainWave  | .50±.01 | .03±.01 | .00±.00 | .002±.003  |           |           |            |            |                 |
Brant .50±.00 .04±.01 .00±.00 .000±.000 REVE .431 .205 2.914 .447 .261 2.408 .447 .213 3.534
|         |         |         |         |            | NeuroGPT-E | .506 .193 | 3.736 .478 | .201 3.385 | .422 .219 5.577 |
| ------- | ------- | ------- | ------- | ---------- | ---------- | --------- | ---------- | ---------- | --------------- |
| O EEGPT | .50±.00 | .03±.01 | .01±.00 | .001±.003  |            |           |            |            |                 |
|         |         |         |         |            | LaBraM     | .443 .176 | 3.846 .435 | .179 2.979 | .482 .098 2.003 |
| NeuroLM | .50±.00 | .04±.01 | .00±.00 | -.001±.001 |            |           |            |            |                 |
|         |         |         |         |            | BFM        | .490 .124 | 0.815 .460 | .169 0.838 | .516 .134 1.266 |
|         |         |         |         |            | Brant      | .408 .089 | 0.730 .361 | .146 0.791 | .375 .070 1.551 |
Table29:PerformanceofBFMsontheChisco-Rdataset.
| Type Model | AUROC   | Acc     | MF1     | Kappa      |     |     |     |     |     |
| ---------- | ------- | ------- | ------- | ---------- | --- | --- | --- | --- | --- |
| C BIOT     | .50±.01 | .04±.00 | .01±.00 | -.000±.003 |     |     |     |     |     |
| MBrain     | .50±.00 | .04±.00 | .00±.00 | .000±.000  |     |     |     |     |     |
| SppEEGNet  | .50±.00 | .02±.00 | .01±.00 | .000±.003  |     |     |     |     |     |
| Bendr      | .50±.00 | .03±.00 | .02±.00 | .001±.003  |     |     |     |     |     |
.51±.02
| G BrainWave |         | .03±.01 | .00±.00 | .001±.003  |     |     |     |     |     |
| ----------- | ------- | ------- | ------- | ---------- | --- | --- | --- | --- | --- |
| BrainOmni   | .51±.01 | .03±.01 | .01±.00 | .002±.005  |     |     |     |     |     |
| LaBraM      | .51±.01 | .03±.01 | .01±.00 | .002±.004  |     |     |     |     |     |
| NeuroGPT-D  | .51±.01 | .05±.00 | .00±.00 | .002±.003  |     |     |     |     |     |
| CBraMod     | .51±.01 | .03±.01 | .01±.00 | -.000±.005 |     |     |     |     |     |
| NeuroGPT-E  | .50±.01 | .05±.00 | .00±.00 | .001±.003  |     |     |     |     |     |
| BFM         | .50±.00 | .03±.01 | .01±.00 | .001±.002  |     |     |     |     |     |
| REVE        | .50±.01 | .03±.00 | .02±.00 | .000±.003  |     |     |     |     |     |
| Brant       | .50±.00 | .04±.01 | .00±.00 | .000±.000  |     |     |     |     |     |
| BrainBERT   | .50±.00 | .03±.01 | .00±.00 | .001±.001  |     |     |     |     |     |
| O EEGPT     | .50±.01 | .03±.01 | .01±.01 | .002±.002  |     |     |     |     |     |
| NeuroLM     | .50±.00 | .03±.02 | .00±.00 | -.000±.000 |     |     |     |     |     |
E AdditionalResultsforSSLStrategyAnalysis
Thissectionreportsfullresultsandrobustnesschecksthatsupport
Figure4:Sensitivityofdecision-boundaryerrorconcentrationto
thetrendsdiscussedinSection3.3.2.Specifically,wereportthecom-
pletequantitativeresultsofthedecision-boundaryandembedding theboundarydefinition.
diagnosticsacrossallevaluatedmodels,andasensitivityanalysis
withrespecttotheboundaryquantileparameter𝑞.Table30reports
| thedecision-boundarymetrics𝐿𝑀 |     | 𝐸𝑅and𝐿𝑀 |     | andtheembedding |     |     |     |     |     |
| ----------------------------- | --- | ------- | --- | --------------- | --- | --- | --- | --- | --- |
𝐸𝑆
| class-separationratio𝑅 |     |     |     |     | F AdditionalSpatialAnalysisResults |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- |
𝑐𝑙𝑠 forallcontrastive-andgenerative-based
BFMsonthethreerepresentativedatasetsanalyzedinthemain This appendix provides detailed results supporting the spatial-
text.Thecompletetableallowsafine-grainedcomparisonbeyond
|     |     |     |     |     | structure analysis | discussed | in Section | 3.3.3. We | report the full |
| --- | --- | --- | --- | --- | ------------------ | --------- | ---------- | --------- | --------------- |
therepresentativemodelsshowninthemainpaper.
quantitativeimpactofchannel-permutationperturbationsacross
Figure4presentsasensitivityanalysisofthedecision-boundary
datasetsandmodels.Wepermutechannelsinthetrainingandvali-
| metricsunderdifferentquantilethresholds𝑞 |     |     |     | ∈ {0.05,0.10,0.20} |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
dationsplitstoprobewhetherBFMsencodedataset-specificspatial
usedtodefinethelow-marginregionB𝑞.Whileabsolutevalues structure.Allothersettingsarekeptidentical,soanyperformance
varywith𝑞,therelativetrendsbetweencontrastiveandgenerative
changeisattributabletodisruptedchanneltopology.Tables31to34
modelsremainstable.Thisconfirmsthattheconclusionsarenot
reportsallmetricsbeforeorafterpermutation.WefocusonAUROC
anartifactofaspecificboundarychoice.
inthemainanalysis,andtheseresultssupportthatsomeBFMs
internalizedataset-specificspatialstructureduringtraining.

Brain4FMs:ABenchmarkofFoundationModelsforElectricalBrainSignals
| Table | 31:         |                           |          |     | Table35:Channel-permutationperformanceonUCSD-OFF. |     |     |     |     |
| ----- | ----------- | ------------------------- | -------- | --- | ------------------------------------------------- | --- | --- | --- | --- |
|       | Performance | under channel-permutation | setting. | We  |                                                   |     |     |     |     |
reportAUROC,Accuracy,F1andF2formodelstrainedonoriginal
data(origin)andshuffleddata(shuffle)onADHD-Child.
|     |       |     |     |     |           | AUROC           | Acc             | F1                      | F2             |
| --- | ----- | --- | --- | --- | --------- | --------------- | --------------- | ----------------------- | -------------- |
|     |       |     |     |     | Model     | shuffle origin  | shuffle origin  | shuffle origin          | shuffle origin |
|     | AUROC | Acc | F1  | F2  |           |                 |                 |                         |                |
|     |       |     |     |     | BrainBERT | .52±.09 .51±.06 | .53±.06 .54±.06 | .60±.10 .49±.17 .68±.15 | .49±.20        |
Model shuffle origin shuffle origin shuffle origin shuffle origin BrainWave .49±.19 .58±.06 .56±.10 .53±.10 .43±.29 .62±.12 .44±.34 .71±.19
|           |         |                                 |                 |         | BrainOmni | .62±.07 .64±.09 | .56±.04 .57±.06 | .57±.10 .54±.16 .61±.21 | .57±.26 |
| --------- | ------- | ------------------------------- | --------------- | ------- | --------- | --------------- | --------------- | ----------------------- | ------- |
| BrainBERT | .54±.04 | .55±.03 .55±.03 .56±.03 .58±.04 | .56±.07 .58±.05 | .53±.09 |           |                 |                 |                         |         |
|           |         |                                 |                 |         | CBraMod   | .60±.05 .63±.05 | .56±.04 .58±.04 | .32±.17 .46±.09 .27±.19 | .40±.12 |
| BrainWave | .68±.04 | .78±.04 .66±.05 .71±.04 .68±.12 | .74±.06 .68±.19 | .74±.12 |           |                 |                 |                         |         |
|           |         |                                 |                 |         | EEGPT     | .62±.15 .61±.13 | .60±.12 .55±.08 | .55±.17 .56±.10 .53±.20 | .58±.17 |
| BrainOmni | .71±.09 | .71±.09 .62±.07 .62±.07 .63±.09 | .63±.09 .61±.15 | .61±.14 |           |                 |                 |                         |         |
CBraMod .60±.06 .64±.05 .57±.03 .64±.06 .72±.03 .73±.03 .85±.03 .81±.05 MBrain .48±.09 .50±.04 .44±.06 .44±.04 .35±.22 .32±.23 .38±.31 .34±.29
EEGPT .63±.11 .67±.13 .60±.10 .64±.10 .57±.28 .68±.10 .59±.32 .68±.12 NeuroGPT-E .56±.07 .56±.06 .52±.05 .54±.05 .57±.09 .57±.12 .63±.17 .62±.22
MBrain .69±.11 .69±.11 .63±.09 .63±.08 .68±.07 .66±.06 .70±.05 .66±.04 REVE .63±.11 .62±.19 .59±.13 .58±.17 .61±.13 .58±.19 .63±.16 .60±.24
| NeuroGPT-E | .55±.02 | .55±.02 .56±.03 .56±.03 .72±.02 | .72±.02 .86±.01 | .86±.01 |     |     |     |     |     |
| ---------- | ------- | ------------------------------- | --------------- | ------- | --- | --- | --- | --- | --- |
| REVE       | .71±.09 | .79±.07 .55±.11 .71±.04 .36±.31 | .74±.06 .32±.30 | .74±.08 |     |     |     |     |     |
Table32:Channel-permutationsettingperformanceonADFD.
|       | AUROC   | Acc                   | F1             | F2             | G AdditionalFrequencyAnalysisResults |     |     |     |     |
| ----- | ------- | --------------------- | -------------- | -------------- | ------------------------------------ | --- | --- | --- | --- |
| Model | shuffle | origin shuffle origin | shuffle origin | shuffle origin |                                      |     |     |     |     |
Thisappendixprovidesdetailedresultssupportingthefrequency-
BrainBERT .62±.05 .59±.05 .64±.01 .58±.05 .66±.02 .60±.11 .64±.04 .64±.15 bandanalysisdescribedinSection3.3.4.Wereportthefullquan-
| BrainWave | .62±.12 | .74±.05 .57±.09 .68±.05 .49±.26 | .68±.10 .47±.31 | .73±.10 |     |     |     |     |     |
| --------- | ------- | ------------------------------- | --------------- | ------- | --- | --- | --- | --- | --- |
titativeoutcomesoftheband-wisePSDpredictionexperiments.
| BrainOmni | .80±.07 | .80±.07 .71±.04 .71±.04 .73±.05 | .73±.05 .72±.09 | .72±.09 |     |     |     |     |     |
| --------- | ------- | ------------------------------- | --------------- | ------- | --- | --- | --- | --- | --- |
Tables36to38reportstheband-wisepredictionperformancefor
| CBraMod | .51±.02 | .55±.06 .52±.07 .59±.04 .32±.26 | .41±.20 .28±.25 | .37±.20 |     |     |     |     |     |
| ------- | ------- | ------------------------------- | --------------- | ------- | --- | --- | --- | --- | --- |
allevaluatedmodelsacrossthesixcanonicalfrequencybands.For
| EEGPT | .79±.04 | .81±.05 .72±.04 .72±.05 .72±.05 | .73±.05 .68±.07 | .70±.07 |     |     |     |     |     |
| ----- | ------- | ------------------------------- | --------------- | ------- | --- | --- | --- | --- | --- |
eachband𝑏,welistthecorrelationbetweentheground-truthPS
| MBrain | .52±.13 | .53±.12 .51±.09 .50±.10 .54±.12 | .53±.12 .54±.15 | .52±.14 |     |     |     |     |     |
| ------ | ------- | ------------------------------- | --------------- | ------- | --- | --- | --- | --- | --- |
andthepredictedPSD,aswellasthenormalizedrelativestrength
| NeuroGPT-E | .49±.05 | .51±.03 .55±.01 .55±.01 .71±.01 | .71±.01 .85±.01 | .85±.01 |     |     |     |     |     |
| ---------- | ------- | ------------------------------- | --------------- | ------- | --- | --- | --- | --- | --- |
𝑟𝑛usedinthemainanalysis.
| REVE | .79±.08 | .84±.07 .68±.07 .77±.08 .74±.05 | .79±.07 .79±.07 | .79±.09 | 𝑏   |     |     |     |     |
| ---- | ------- | ------------------------------- | --------------- | ------- | --- | --- | --- | --- | --- |
Table33:Channel-permutationsettingperformanceonCHBMIT.
|       | AUROC   | Acc                   | F1             | F2             |     |     |     |     |     |
| ----- | ------- | --------------------- | -------------- | -------------- | --- | --- | --- | --- | --- |
| Model | shuffle | origin shuffle origin | shuffle origin | shuffle origin |     |     |     |     |     |
Table36:Band-wisePSDpredictabilityacrossBFMsonADFDand
BrainBERT .79±.04 .78±.06 .80±.04 .75±.10 .59±.08 .58±.08 .59±.11 .61±.09 Dep-122,reportingnormalizedbandpredictability𝑟𝑛fordelta(d),
BrainWave .59±.14 .90±.03 .63±.09 .80±.12 .30±.11 .71±.09 .32±.15 .78±.04 𝑏
BrainOmni .74±.13 .74±.13 .67±.19 .67±.19 .51±.12 .51±.12 .56±.12 .56±.12 theta(t),alpha(a),beta(b),lowgamma(gl),andhighgamma(gh).
| CBraMod | .67±.12 | .69±.04 .67±.11 .70±.08 .42±.16 | .46±.08 .48±.23 | .49±.14 |     |             |             |                 |         |
| ------- | ------- | ------------------------------- | --------------- | ------- | --- | ----------- | ----------- | --------------- | ------- |
| EEGPT   | .69±.13 | .71±.09 .73±.10 .67±.11 .47±.16 | .46±.06 .48±.19 | .51±.15 |     |             |             |                 |         |
|         |         |                                 |                 |         |     | ADFD        |             | Dep-122         |         |
| MBrain  | .70±.08 | .71±.03 .77±.03 .73±.06 .22±.22 | .31±.15 .17±.18 | .28±.20 |     |             |             |                 |         |
|         |         |                                 |                 |         |     | 𝑟 𝑛 𝑟 𝑛 𝑟 𝑛 | 𝑟 𝑛 𝑟 𝑛 𝑟 𝑛 | 𝑟 𝑛 𝑟 𝑛 𝑟 𝑛 𝑟 𝑛 | 𝑟 𝑛 𝑟 𝑛 |
NeuroGPT-E .65±.07 .78±.12 .70±.06 .75±.07 .26±.10 .51±.22 .24±.14 .63±.16 Model 𝑑 𝑡 𝑎 𝑏 𝑔 𝑙 𝑔 ℎ 𝑑 𝑡 𝑎 𝑏 𝑔 𝑙 𝑔 ℎ
| REVE | .78±.12 | .84±.10 .59±.25 .78±.12 .53±.18 | .63±.14 .65±.12 | .66±.13 |           |             |             |                 |         |
| ---- | ------- | ------------------------------- | --------------- | ------- | --------- | ----------- | ----------- | --------------- | ------- |
|      |         |                                 |                 |         | REVE      | .85 .00 .71 | .11 .59 1.0 | .99 .00 1.0 .92 | .78 .65 |
|      |         |                                 |                 |         | EEGPT     | 1.0 .32 .36 | .20 .92 .00 | .80 .67 1.0 .67 | .13 .00 |
|      |         |                                 |                 |         | BrainOmni | .95 .00 .82 | .02 .28 1.0 | .83 .39 1.0 .81 | .35 .00 |
Table34:Channel-permutationsettingperformanceonUCSD-ON. BrainWave .63 .35 .77 .00 .14 1.0 1.0 .47 .75 .23 .00 .28
|     |     |     |     |     | LaBraM    | .08 .00 1.0 | .26 .28 .10 | .77 .36 1.0 .55 | .15 .00 |
| --- | --- | --- | --- | --- | --------- | ----------- | ----------- | --------------- | ------- |
|     |     |     |     |     | BrainBERT | .69 .08 .16 | .00 .68 1.0 | .70 .44 1.0 .00 | .27 .87 |
AUROC Acc F1 F2 BFM .89 .00 .33 .09 .27 1.0 .89 1.0 .99 .76 1.0 .71
Model shuffle origin shuffle origin shuffle origin shuffle origin BIOT .87 .00 .62 .31 .37 1.0 .80 .38 1.0 .75 .17 .00
|           |         |                                 |                 |         | CBraMod    | .84 .00 .67 | .55 .64 1.0 | .91 .00 1.0 .86 | .47 .05 |
| --------- | ------- | ------------------------------- | --------------- | ------- | ---------- | ----------- | ----------- | --------------- | ------- |
| BrainBERT | .50±.09 | .51±.05 .49±.05 .51±.06 .57±.04 | .51±.11 .64±.06 | .54±.17 |            |             |             |                 |         |
|           |         |                                 |                 |         | MBrain     | .87 .00 .42 | .15 .40 1.0 | .98 .00 1.0 .87 | .87 .61 |
| BrainWave | .50±.11 | .69±.10 .49±.12 .53±.08 .40±.28 | .60±.06 .43±.31 | .69±.14 |            |             |             |                 |         |
|           |         |                                 |                 |         | SppEEGNet  | .26 .10 .00 | .02 .27 1.0 | 1.0 .55 .94 .27 | .00 .08 |
| BrainOmni | .51±.19 | .64±.09 .46±.15 .57±.06 .44±.21 | .54±.16 .46±.26 | .57±.26 |            |             |             |                 |         |
|           |         |                                 |                 |         | NeuroLM    | .66 .89 .51 | .08 .00 1.0 | 1.0 .36 .35 .00 | .20 .05 |
| CBraMod   | .59±.08 | .60±.12 .51±.07 .49±.08 .21±.29 | .18±.08 .22±.35 | .13±.07 |            |             |             |                 |         |
|           |         |                                 |                 |         | NeuroGPT-E | .85 .13 .00 | .01 .06 1.0 | .52 .39 1.0 .00 | .06 .10 |
| EEGPT     | .63±.17 | .51±.21 .55±.14 .48±.17 .49±.16 | .49±.15 .46±.16 | .49±.14 |            |             |             |                 |         |
|           |         |                                 |                 |         | Bendr      | .74 .28 .00 | .10 .07 1.0 | 1.0 .28 .79 .44 | .00 .03 |
| MBrain    | .43±.16 | .49±.15 .46±.06 .46±.14 .49±.21 | .37±.17 .56±.28 | .34±.18 |            |             |             |                 |         |
NeuroGPT-E .55±.25 .56±.10 .53±.10 .53±.07 .51±.25 .58±.10 .57±.34 .64±.13 Brant .53 .33 .17 .08 .00 1.0 .00 .68 .33 .43 .93 1.0
REVE .58±.12 .63±.19 .58±.06 .56±.13 .53±.17 .45±.29 .53±.25 .46±.33 NeuroGPT-D .95 .23 .25 .10 .00 1.0 1.0 .30 .86 .62 .11 .00

Shenetal.
Table37:Band-wisePSDpredictabilityonSD-8andMDD-64. Table39:LaBraMcodebookanalysisonADFD,CHBMIT,andSD-
28.Wecomparestandardfinetuningwithoutcodebook(Origin)
andcodebook-enabledfinetuning(CB)underidenticalprotocols,
|     | SD-28 |     |     | MDD-64 |     |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
reportingAUROC,Accuracy,F1,andF2.
|            | 𝑛 𝑛 𝑛       | 𝑛 𝑛 𝑛       | 𝑛 𝑛     | 𝑛       | 𝑛 𝑛 𝑛   |         |       |           |        |           |     |           |
| ---------- | ----------- | ----------- | ------- | ------- | ------- | ------- | ----- | --------- | ------ | --------- | --- | --------- |
| Model      | 𝑟 𝑟 𝑡 𝑟 𝑎   | 𝑟 𝑟 𝑟       | 𝑟 𝑟 𝑡   | 𝑟 𝑎 𝑟   | 𝑟 𝑟     |         |       |           |        |           |     |           |
|            | 𝑑           | 𝑏 𝑔 𝑙 𝑔 ℎ   | 𝑑       | 𝑏       | 𝑔 𝑙 𝑔 ℎ |         |       |           |        |           |     |           |
| BrainWave  | .95 .64 1.0 | .75 .00 .22 | .89 1.0 | .89 .61 | .00 .02 |         |       |           |        |           |     |           |
|            |             |             |         |         |         |         | AUROC |           | Acc    | F1        |     | F2        |
| REVE       | 1.0 .00 .97 | .66 .67 .22 | .96 1.0 | .99 1.0 | .93 .00 |         |       |           |        |           |     |           |
|            |             |             |         |         |         | Dataset | CB    | origin CB | origin | CB origin |     | CB origin |
| NeuroGPT-E | 1.0 .87 .06 | .00 .41 .90 | .25 1.0 | .00 .62 | .60 .08 |         |       |           |        |           |     |           |
BrainBERT .82 .15 1.0 .00 .13 .29 .75 1.0 .73 .70 .80 .00 ADFD .65±.06 .77±.10 .62±.05 .72±.08 .68±.03 .75±.06 .70±.03 .75±.06
BrainOmni .86 .46 1.0 .71 .27 .00 .66 .84 1.0 .99 .74 .00 CHBMIT .77±.06 .78±.07 .75±.04 .75±.06 .60±.10 .54±.24 .55±.7 .53±.16
BFM .92 .00 1.0 .84 .90 .84 .86 1.0 .97 .97 .97 .00 SD-28 .47±.12 .54±.07 .50±.09 .54±.04 .56±.12 .59±.07 .60±.15 .59±.13
| MBrain | 1.0 .00 1.0 | .94 .83 .69 | .94 .96 | .96 1.0 | .92 .00 |     |     |     |     |     |     |     |
| ------ | ----------- | ----------- | ------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| EEGPT  | .91 .66 1.0 | .97 .38 .00 | .89 .97 | 1.0 .89 | .74 .00 |     |     |     |     |     |     |     |
| BIOT   | .68 .00 1.0 | .58 .65 .19 | .93 .97 | 1.0 .99 | .86 .00 |     |     |     |     |     |     |     |
Table40:LaBraMcodebookanalysisonSleepEDF,reportingAccu-
| NeuroGPT-D | 1.0 .00 .76 | .67 .36 .14 | .92 1.0 | .98 .71 | .67 .00 |     |     |     |     |     |     |     |
| ---------- | ----------- | ----------- | ------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
racy,AUROC(OvR),macro-F1(MF1),andCohen’s𝜅.
| CBraMod | 1.0 .25 .90 | .89 .58 .00 | .95 .96 | .98 1.0 | .90 .00 |       |     |     |     |     |       |     |
| ------- | ----------- | ----------- | ------- | ------- | ------- | ----- | --- | --- | --- | --- | ----- | --- |
| LaBraM  | .87 .44 1.0 | .70 .34 .00 | .59 .86 | .59 1.0 | .76 .00 |       |     |     |     |     |       |     |
| Brant   | .64 .00 1.0 | .71 .61 .54 | .84 .87 | .89 1.0 | .93 .00 |       |     |     |     |     |       |     |
|         |             |             |         |         |         | AUROC |     | Acc | MF1 |     | Kappa |     |
| Bendr   | 1.0 .34 .53 | .51 .01 .00 | .73 1.0 | .48 .49 | .46 .00 |       |     |     |     |     |       |     |
SppEEGNet 1.0 .16 .68 .29 .00 .02 1.0 .84 .78 .63 .51 .00 CB origin CB origin CB origin CB origin
| NeuroLM | 1.0 .31 .81 | .31 .00 .24 | .59 .86 | .59 1.0 | .76 .00 |         |         |                 |         |         |         |         |
| ------- | ----------- | ----------- | ------- | ------- | ------- | ------- | ------- | --------------- | ------- | ------- | ------- | ------- |
|         |             |             |         |         |         | .86±.02 | .93±.01 | .66±.04 .76±.04 | .61±.03 | .68±.03 | .54±.05 | .67±.05 |
Table38:Band-wisePSDpredictabilityacrossBFMsonADHD.
|            | ADHD-Adult  |             | ADHD-Child |         |         |     |     |     |     |     |     |     |
| ---------- | ----------- | ----------- | ---------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| Model      | 𝑟 𝑛 𝑟 𝑛 𝑟 𝑛 | 𝑟 𝑛 𝑟 𝑛 𝑟 𝑛 | 𝑟 𝑛 𝑟 𝑛    | 𝑟 𝑛 𝑟 𝑛 | 𝑟 𝑛 𝑟 𝑛 |     |     |     |     |     |     |     |
|            | 𝑑 𝑡 𝑎       | 𝑏 𝑔 𝑙 𝑔 ℎ   | 𝑑 𝑡        | 𝑎 𝑏     | 𝑔 𝑙 𝑔 ℎ |     |     |     |     |     |     |     |
| EEGPT      | .66 .00 .59 | 1.0 .18 .08 | .95 .82    | 1.0 1.0 | .56 .00 |     |     |     |     |     |     |     |
| BrainOmni  | .65 .00 .67 | 1.0 .32 .14 | 1.0 .86    | .99 .84 | .39 .00 |     |     |     |     |     |     |     |
| BrainWave  | .32 .00 .68 | 1.0 .80 .82 | .83 .59    | .94 1.0 | .34 .00 |     |     |     |     |     |     |     |
| BIOT       | .40 .00 .40 | 1.0 .58 .17 | .98 .89    | 1.0 .78 | .32 .00 |     |     |     |     |     |     |     |
| REVE       | .71 .00 .25 | 1.0 .53 .30 | .96 .82    | .98 1.0 | .62 .00 |     |     |     |     |     |     |     |
| MBrain     | .66 .00 .55 | 1.0 .53 .16 | 1.0 .87    | .98 1.0 | .60 .00 |     |     |     |     |     |     |     |
| Brant      | .71 .00 .33 | 1.0 .32 .08 | .89 .58    | .68 1.0 | .59 .00 |     |     |     |     |     |     |     |
| CBraMod    | .65 .19 .61 | 1.0 .52 .00 | .99 .86    | .94 1.0 | .79 .00 |     |     |     |     |     |     |     |
| LaBraM     | .76 .39 .71 | 1.0 .08 .00 | 1.0 .86    | .96 .92 | .41 .00 |     |     |     |     |     |     |     |
| NeuroGPT-E | .39 .74 .00 | 1.0 .40 .15 | .84 1.0    | .75 .37 | .00 .44 |     |     |     |     |     |     |     |
| NeuroGPT-D | .95 .00 .71 | 1.0 .16 .03 | 1.0 .70    | .83 .77 | .34 .00 |     |     |     |     |     |     |     |
| BFM        | .61 .00 .45 | 1.0 .70 .62 | .96 .83    | .94 1.0 | .67 .00 |     |     |     |     |     |     |     |
| NeuroLM    | .41 .00 .55 | 1.0 .29 .19 | 1.0 .82    | .97 .88 | .27 .00 |     |     |     |     |     |     |     |
| BrainBERT  | 1.0 .26 .91 | .84 .13 .00 | 1.0 .64    | .82 .66 | .60 .00 |     |     |     |     |     |     |     |
| SppEEGNet  | 1.0 .06 .72 | .61 .06 .00 | 1.0 .80    | .70 .64 | .31 .00 |     |     |     |     |     |     |     |
| Bendr      | 1.0 .16 .73 | .78 .03 .00 | 1.0 .62    | .83 .57 | .20 .00 |     |     |     |     |     |     |     |
H AdditionalCodebookAnalysisResults
ThissectioncomplementsthecodebookanalysisdiscussedofLaBraM
inSection3.3.5.LaBraMadoptsadiscretecodebookduringpre-
training.However,initsstandarddownstreamfinetuningprotocol,
itfinetunestheencoderandtaskheadwhilekeepingthecodebook
unused(i.e.,finetuningisperformedoncontinuousembeddings).
Toisolatetheeffectofreusingdiscretizationatfinetuningtime,
weadditionallyevaluateavariantthatenablescodebook-based
finetuning(CB)andcompareitagainstthestandardsetting(origin)
onfourrepresentativedatasets,withallothersettingsheldfixed.
Table40reportsfullresultsforbothvariants.LaBraMcodebook
analysisonADFD,CHBMIT,SleepEDF,andSD-28.WereportAU-
ROC,Accuracy,F1,andF2forthebinarydatasets,andAUROC
(OvR),Accuracy,MF1,andCohen’s𝜅forSleepEDF.