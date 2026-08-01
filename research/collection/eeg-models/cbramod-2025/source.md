PublishedasaconferencepaperatICLR2025
CBRAMOD: A CRISS-CROSS BRAIN
FOUNDATION MODEL FOR EEG DECODING
JiquanWang1,2,ShaZhao1,2∗,ZhilingLuo3,YangxuanZhou1,2,HaitengJiang4,5,1,
ShijianLi1,2,TaoLi4,5,1,GangPan1,2,5∗
1StateKeyLaboratoryofBrain-machineIntelligence,ZhejiangUniversity
2CollegeofComputerScienceandTechnology,ZhejiangUniversity
3AlibabaGroup
4DepartmentofNeurobiology,AffiliatedMentalHealthCenter&Hangzhou
SeventhPeople’sHospital,ZhejiangUniversitySchoolofMedicine
5MOEFrontierScienceCenterforBrainScienceandBrain-machineIntegration,
ZhejiangUniversity
{wangjiquan, szhao, zyangxuan, h.jiang}@zju.edu.cn;
{shijianli, litaozjusc, gpan}@zju.edu.cn;
godot.lzl@alibaba-inc.com
ABSTRACT
Electroencephalography(EEG)isanon-invasivetechniquetomeasureandrecord
brainelectricalactivity,widelyusedinvariousBCIandhealthcareapplications.
Early EEG decoding methods rely on supervised learning, limited by specific
tasksanddatasets,hinderingmodelperformanceandgeneralizability. Withthe
successoflargelanguagemodels,thereisagrowingbodyofstudiesfocusingon
EEG foundation models. However, these studies still leave challenges: Firstly,
mostofexistingEEGfoundationmodelsemployfullEEGmodelingstrategy. It
modelsthespatialandtemporaldependenciesbetweenallEEGpatchestogether,
but ignores that the spatial and temporal dependencies are heterogeneous due
totheuniquestructuralcharacteristicsofEEGsignals. Secondly,existingEEG
foundationmodelshavelimitedgeneralizabilityonawiderangeofdownstream
BCItasksduetovaryingformatsofEEGdata,makingitchallengingtoadaptto.
Toaddressthesechallenges,weproposeanovelfoundationmodelcalledCBraMod.
Specifically, wedeviseacriss-crosstransformerasthebackbonetothoroughly
leverage the structural characteristics of EEG signals, which can model spatial
andtemporaldependenciesseparatelythroughtwoparallelattentionmechanisms.
And we utilize an asymmetric conditional positional encoding scheme which
canencodepositionalinformationofEEGpatchesandbeeasilyadaptedtothe
EEG with diverse formats. CBraMod is pre-trained on a very large corpus of
EEG through patch-basedmaskedEEG reconstruction. We evaluateCBraMod
onupto10downstreamBCItasks(12publicdatasets). CBraModachievesthe
state-of-the-art performance across the wide range of tasks, proving its strong
capabilityandgeneralizability. Thesourcecodeispubliclyavailableathttps:
//github.com/wjq-learning/CBraMod.
1 INTRODUCTION
Brain-ComputerInterface(BCI)referstoasystemthatallowsdirectcommunicationbetweenthe
brainandexternaldevicesorcomputers(Schalketal.,2004;Wuetal.,2013;Zhangetal.,2019b).
Electroencephalography(EEG)isatechniqueusedtomeasureandrecordelectricalactivityinthe
brain,whereelectrodesareplacedonthescalptodetectandamplifythebrain’selectricalsignals.
EEGplaysacrucialroleinBCIasitprovidesanon-invasiveandreal-timemeasureofbrainactivity
thatcanbeusedtodecodeandinterpretuser’sintentionsorcommands. Byanalyzingthepatterns
andfeaturesinEEGsignals,algorithmsandmodelshavebeendevelopedtodecodespecificbrain
∗Correspondingauthors:ShaZhaoandGangPan.
1
5202
voN
6
]PS.ssee[
6v63270.2142:viXra

PublishedasaconferencepaperatICLR2025
(a) EEG Patches (b)Full EEG Modeling (c)Criss-Cross EEG Modeling
Figure1: EEGpatchesanddifferentEEGmodelingstrategies.
states,includingbutnotlimitedtoemotionrecognition(Dadebayevetal.,2022;Gaoetal.,2024),
motorimageryclassification(Altaherietal.,2021;Daietal.,2020),seizuredetection(Ahmadetal.,
2022;Yıldızetal.,2022)andsleepstaging(Phan&Mikkelsen,2022;Wangetal.,2024b;Zhouetal.,
2024a).
EarlystudiesonEEGdecodingpredominantlyemployedtraditionalmachinelearningmethods(Lotte
etal.,2007). Withtherapidadvancementofdeeplearning(LeCunetal.,2015),variousdeepneural
networkshavebeendevelopedtodecodeEEGsignals(Craiketal.,2019)andperformdownstream
BCItasks(Panetal.,2018;Sekkaletal.,2022). Thesedeeplearning-basedEEGmodelsinclude
ConvolutionNeuralNetwork(CNN)(Lawhernetal.,2018;Dingetal.,2022),LongShort-Term
Memory(LSTM)(Wangetal.,2018;Phanetal.,2019),CNN-LSTM(Zhangetal.,2019a;Wang
etal.,2023a),Transformer(Songetal.,2021;Phanetal.,2022),CNN-Transformer(Songetal.,
2022;Pehetal.,2022),GraphNeuralNetworks(GNN)(Jiaetal.,2020;Dingetal.,2023)andetc.
However,mostofdeeplearningmodelsemploysupervisedlearningmethodstailoredforspecific
tasksordatasets,andlackgeneralizationability.Therearestillsignificantchallengesinimprovingthe
generalizabilityandperformanceduetomanyfactors,suchaslimiteddataamountsandsubstantial
differences in EEG signal formats. The EEG is usually collected for specific BCI tasks, and the
amountisrelativelysmall,becausecollectingandlabelingEEGisexpensiveandtime-consuming.
Meanwhile,theEEGsignalformatssignificantlydifferacrossdifferentdatasets,suchaschannel
configurationsandtimelengths.
Impressedbyself-supervisedlearning(SSL)(Liuetal.,2021c)oncomputervision(CV)andnatural
languageprocessing(NLP),somestudies(Kostasetal.,2021;Chienetal.,2022;Yangetal.,2023;
Foumanietal.,2024;Jiangetal.,2024;Wangetal.,2024a)proposeEEGfoundationmodelswhichare
pre-trainedonavastamountofEEGdatawithself-supervisedlearningandfine-tunedondownstream
datasetsforsomeclinicalorBCIapplications. MostofthesemethodssegmenttheoriginalEEG
signalsintopatchesofEEGchannelstoensurethattheneuralnetworkcandealwithEEGsignals
withdiversechannelsandtimelength,showninFigure1(a).Consistentwiththeapproachofhandling
imagepatchesusedinViT(Dosovitskiyetal.,2020),theyflattentheEEGpatchesandfeedtheminto
transformerstomodelthedependenciesamongallEEGpatches,calledfullEEGmodelingstrategy
shown in Figure 1(b). Meantime, they adopted absolute positional encoding based on electrode
numberingasachannelembeddingtoencodepositionalinformation. However,existingmethods
ignoretwocharacteristicsofEEGsignals: Uniquestructuralcharacteristics: EEGsignalshave
differentstructuralcharacteristicscomparedtoimage. Itcontainheterogeneousspatialandtemporal
dependencies,butimagescontainonlyspatialdependencies. AndthedependenciesamongEEG
patcheswithinthesamechannelortimeintervalcouldbestrongerthanthoseamongpatchesfrom
differentchannelsandtimeintervals,butsuchapriorassumptionmaynotbevalidinimage. The
fullEEGmodelingstrategymodelsthedependenciesamongallEEGpatchestogether,ignoringthe
uniquestructuralcharacteristicsofEEGsignals. Channelvariation: EEGchannelsarenotsolely
definedbyelectrodepositionbutarealsoinfluencedbythereferencingschemeused(e.g.,earlobe,
average,REST,orbipolarreferences).ExistingEEGfoundationmodels,suchasLaBraM(Jiangetal.,
2024),employabsolutepositionalencodingbasedonelectrodenumberingasachannelembedding,
butthismethodassumesafixedrelationshipbetweenEEGchannelsandelectrodepositions. As
aresult,absolutepositionalencodingstieddirectlytoelectrodenumberingmaylimitthemodel’s
adaptabilityacrosstasksanddatasetsthatvaryinspatialandreferenceproperties.
2

PublishedasaconferencepaperatICLR2025
Toaddresstheseissues,wefirstproposeacriss-crossEEGmodelingstrategytothoroughlyleverage
thestructuralcharacteristicsofEEGsignals,inspiredbysomestudies(Huangetal.,2019;Dongetal.,
2022)whichadoptsimilarstrategiesonvisionmodeling. Basedonthisstrategy,wethenproposean
EEGfoundationmodel,whichcanmodelspatialandtemporaldependenciesinparallel,asshownin
Figure1(c). Meantime,weproposeasymmetricconditionalpositionalencoding(ACPE)asamore
flexibleapproachtopositionalencoding.ACPEemploysaconvolutionalnetworktodynamicallylearn
spatialrelationshipsamongpatches,allowingthemodeltocapturerelativepositionalinformation
from various channel format. This dynamic position learning enhances the model’s adaptability,
making it better suited for downstream tasks with varying spatial configurations and reference
contexts. Ourdetailedcontributionsareasfollows:
• WeproposeanovelEEGfoundationmodel,calledCBraMod,forEEGdecodingonvariousclin-
icalandBCIapplication. CBraModispre-trainedonTempleUniversityHospitalEEGCorpus
(TUEG)forlearninggenericrepresentationsfrombothtime-domainandfrequent-domainEEG
signalsthroughpatch-basedmaskedEEGreconstruction. Tothebestofourknowledge,TUEGis
thelargestpublicEEGcorpussofar.
• For modeling effective spatial-temporal dependencies among EEG patches and adapting to
variousdownstreamdatasets,wefirstlydeviseacriss-crosstransformer,basedoncriss-cross
EEGmodelingstrategy,asthebackboneofCBraMod.Itmodelsspatialandtemporaldependencies
separatelythroughtwoparallelattentionmechanisms,spatialandtemporalattentions. Meanwhile,
weutilizeanasymmetricconditionalpositionalencoding(ACPE)schemetoencodepositional
information. ACPEcandynamicallygeneratepositionalencoding,whichcanwellbeadaptedto
arbitraryEEGformatsofdifferentdownstreamdatasets.
• WeevaluatetheperformanceofCBraModonupto10downstreamBCItasksusing12public
datasets. Themajorityofdownstreamdatasetsaresourcedfrominstitutionsdifferentfromthe
pretrainingdataset. TheexperimentalresultsdemonstratethatCBraModachievesstate-of-the-art
performanceacrossallthetasks,highlightingitssuccessfulgeneralizability. Tothebestofour
knowledge,thisisthefirststudytocomprehensivelyevaluateEEGfoundationmodelsacrosssuch
abroadrangeofdownstreamBCItasks.
Patching
ACPE
& Patch
Masking Encoding
Criss-Cross Transformer Block 1
Criss-Cross Transformer Block 2
Criss-Cross Transformer Block M
…
Learned EEG
Representations
daeH
noitcurtsnoceR
Masked EEG
Reconstruction
Figure2: CBraModpre-trainingoverview.
2 METHOD
Thepre-trainingframeworkofCBraModisshowninFigure2. Firstly,wesegmentEEGsamples
intopatchesusingafixedtimewindowandrandomlymasksomepatcheswithamasktoken. Next,
each EEG patch is fed into a patch encoding network to obtain corresponding patch embedding.
Spatial-temporalpositionalembeddingsareobtainedthroughanasymmetricconditionalpositional
encoding(ACPE)schemeandaddedtothepatchembeddings. Then,thepatchembeddingsarefed
intocriss-crosstransformerblockswithcriss-crossattentionmechanismtolearnEEGrepresentations.
Finally,areconstructionheadisutilizedtoreconstructthemaskedEEGpatchesfromthelearned
representations. WewillprovideadetaileddescriptionofCBraMod.
3

PublishedasaconferencepaperatICLR2025
Patching&Masking WedenoteanEEGsampleasS ∈RC×T,whereCisthenumberofelectrode
channelsandT isthenumberoftimestamps. Inordertoensurethattheneuralnetworkcandeal
withEEGsignalswithdiversechannelsandtimelength,wesegmenttheoriginalEEGsampleinto
patchesofEEGchannelsthroughafixed-lengthtimewindow. Specifically,wedivideS with
timewindowlengthttogetasetofpatchesX ∈RC×n×t,wheren=⌊T⌋isthenumberofpatches
t
ineachchannel,orsequencelength. ThusanEEGpatchcanbedenotedasx∈Rtandwecanget
X ={x |i∈[1,2,...,C],j ∈[1,2,...,n]}. ThetotalnumberofpatchesinX is|X|=Cn. After
i,j
EEGpatching,werandomlygenerateamaskM={m |i∈[1,2,...,C],j ∈[1,2,...,n]}froma
i,j
Bernoullidistributionofrproportion,wherem ∈{0,1}denotesthemaskindicatorofx . Then
i,j i,j
wemasktheEEGpatchesofX byreplacingtheEEGpatchx withx asfollows:
i,j M
(cid:26)x , m =0
i,j i,j
x˜ = (1)
i,j x , m =1
M i,j
X˜ ={x˜ |i∈[1,2,...,C],j ∈[1,2,...,n]} (2)
i,j
wherex ∈RtisthemasktokenandX˜ ∈RC×n×tisthesetofallEEGpatchesaftermasking.
M
Time-FrequencyPatchEncoding Inordertoextractthelocalfeaturesfromeachpatchx˜ of
i,j
X˜,wedeviseapatchencoderappliedtoeachpatch. Ourpatchencoderconsistsoftwobranches,
time-domainbranchandfrequency-domainbranch.Thetime-domainbranchcomprisesmultiple
convolutionblocksdesignedtoextracttime-domainfeatureswithineachpatch. Aconvolutionblock
consistsofanone-dimensionalconvolutionlayer,agroupnormalizationlayer,andaGELUactivation
function. We feed each EEG patch x˜ into the time-domain branch to obtain the time-domain
i,j
embeddinget ∈Rd,wheredisthedimensionoftheembedding. Thefrequency-domainbranch
i,j
comprises fast Fourier transform (FFT) and a fully-connected layer to extract frequency-domain
featuresfromeachpatch. Specifically,weleverageFFTtoextractanenergyvectorforeachpatch
x˜ whereeverydimensionindicatestheenergyofaspecificfrequency. Thenwefeedtheenergy
i,j
vectorintoafully-connectedlayertogetfrequency-domainembeddingef ∈Rd. Afterwards,we
i,j
addeachtime-domainembeddingandthecorrespondingfrequency-domainembeddingasfollows:
e =et +ef (3)
i,j i,j i,j
E ={e |i∈[1,2,...,C],j ∈[1,2,...,n]} (4)
i,j
wheree ∈Rdrepresentsthepatchembedding,E ∈RC×n×disthesetofpatchembeddings.
i,j
AsymmetricConditionalPositionalEncoding DifferingfromexistingEEGfoundationmodels
that primarily utilize an absolute positional encoding (APE) scheme, we employ an asymmetric
conditionalpositionalencoding(ACPE)schemetoencodespatialandtemporalpositionalinformation
ofEEGpatches. Thisisamodificationuponconditionalpositionalencoding(CPE)(Chuetal.,2021)
thatisappliedtoencodepositionalinformationofimagepatches. ComparedtoAPE,ACPEcan
dynamicallyencodethetemporalandspatialpositionalinformationofeachEEGpatch,improving
adaptationtodiversechannelconfigurationsandtimelengths. ComparedtoCPE,ACPEisdesigned
in an asymmetric fashion to encode short-range temporal positional information and long-range
spatial positional information. It is because EEG signals are multi-channels sequential neural
signals,requiringthemodeltoencodedifferent-rangepositionalinformationinspatialandtemporal
dimension.
Specifically,wedeviseaconvolutionlayeraspositionalencodertodynamicallygenerateACPE
from the spatial-temporal neighborhoods of an EEG patch, shown in Figure 2. The convolution
network is composed of a depthwise two-dimension convolution layer with kernel (k ,k ) and
s t
(ks
2
−1,kt
2
−1)zeropaddings,wherek
s
isthekernelsizeofspatial(channel)dimensionandk
t
isthe
kernelsizeoftemporaldimension.DifferingfromCPE,weutilizeanasymmetricconvolutionkernel
(k >k )toencodespatial-temporalpositionalinformation. Thelongersideinspatialdimensionis
s t
usedtoencodelonger-rangespatialpositionalinformation,andtheshorterintemporaldimension
isusedtoencodeshorter-rangetemporalpositionalinformation. WefeedpatchembeddingsE into
thepositionalencodertogeneratetheACPEEp = {ep |i ∈ [1,2,...,C],j ∈ [1,2,...,n]},where
i,j
Ep ∈RC×n×dandep ∈Rd. ThenweaddACPEtopatchembeddings:
i,j
Eo =E+Ep ={e +ep |i∈[1,2,...,C],j ∈[1,2,...,n]} (5)
i,j i,j
4

PublishedasaconferencepaperatICLR2025
Add
S-Attention
Feed Forward
Layer Norm
ℎ𝐾𝐾
|     |     |     |     |     | Split Head |     |     | 2 Concat |     |     |
| --- | --- | --- | --- | --- | ---------- | --- | --- | -------- | --- | --- |
|     |     | Add |     |     |            |     | ℎ1  |          |     |     |
𝐶𝐶
|     | Criss-Cross Attention |     |     |     | ℎ𝐾𝐾         |     |     |     |     | ℎ𝐾𝐾 |
| --- | --------------------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
|     |                       |     |     | 𝑛𝑛  | ℎ1          |     |     |     |     | ℎ1  |
|     | Layer Norm            |     |     |     | T-Attention |     |     |     |     |     |
ℎ𝐾𝐾
| (a) Criss-Cross Transformer Block |     |     |     |     | (b) Criss-Cross Attentℎio𝐾𝐾 |     | n+ 1Mechanism |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --------------------------- | --- | ------------- | --- | --- | --- |
2
|     |     |     | Figure3: | Criss-CrossTransformerBlock. |     |     |     |     |     |     |
| --- | --- | --- | -------- | ---------------------------- | --- | --- | --- | --- | --- | --- |
whereEo ∈RC×n×disthesetofEEGpatchembeddingswithpositionalinformation.
Criss-CrossTransformer Weproposecriss-crosstransformertocapturetheheterogeneousspatial
andtemporaldependenciesamongEEGpatches,whosearchitectureisshowninFigure3.
Criss-CrossTransformerBlock. AsshowninFigure3(a),acriss-crosstransformerblockconsists
oflayernormalizationlayer,criss-crossattention,additioncomponent,andfeedforwardlayer. In
ordertoensurethestabilityandefficiencyofthetransformertrainingprocess,weutilizethepre-norm
strategy. Weincorporatelayernormalizationtothequeriesandkeyspriortotheattentionmechanism
to prevent the occurrence of excessively large values in attention logits. This approach helps to
maintainmoreconsistentgradientsacrosslayers,resultinginbetterconvergenceduringthetraining
Here,wefeedEEGpatchembeddingsEointo
process(Xiongetal.,2020;Dehghanietal.,2023).
layernormalizationtogetnormalizedpatchembeddingE˜ ∈ RC×n×d. ThenwefeedE˜ intothe
criss-crossattentiontocapturespatial-temporaldependenciesamongEEGpatches.
Criss-CrossAttentionMechanism. Thecriss-crossattentionisshowninFigure3(b). Itconsistsof
parallelspatialattention(S-Attention)andtemporalattention(T-Attention). TheS-Attention
isusedtocapturespatialdependenciesamongEEGpatcheswithinthesametimeintervalandthe
T-AttentionisusedtocapturetemporaldependenciesamongEEGpatcheswithinthesamechannel.
Basedonthemulti-headself-attentionmechanism,theinputembeddingsE˜ ∈RC×n×dwillundergo
aninitiallinearprojectiontoK heads,andeachheadwillsubsequentlyapplyeitherS-Attentionor
T-Attention. ForS-Attention,wecanpartitionE˜ intonspatialstripesasE˜ =[E˜1,E˜2,...E˜n],where
| E˜1,...,E˜n |     | RC×d. |     |     |     |     |     |     |     |     |
| ----------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
∈ Wesupposetheprojectedqueries,keysandvaluesofthek-thheadallhave
| dimensiond |     | ,thentheprocessofS-Attentionforthek-thheadisasfollows: |     |     |     |     |     |     |     |     |
| ---------- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
k
Fj =Attention(E˜jWQ,E˜jWK,E˜jWV)
|     |     |     |     |     |     | k   | k   |     |     | (6) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | k   |     | k   |     |     |     |     |     |
(E˜)=[F1,F2,...,Fn]
|       |     |             | S-Attention |      |                  |          |     |         |        | (7)    |
| ----- | --- | ----------- | ----------- | ---- | ---------------- | -------- | --- | ------- | ------ | ------ |
|       |     |             |             |      | k k              | k        | k   |         |        |        |
|       | j ∈ | [1,2,...,n] |             | j-th |                  | WQ,WK,WV |     | ∈ Rd×dk |        |        |
| where |     |             | represents  | the  | spatial stripes, |          |     |         | is the | linear |
|       |     |             |             |      |                  | k        | k   | k       |        |        |
projectionmatricesofqueries,keysandvaluesforthek-thheadrespectively,andd k =d/K. The
processofT-AttentioncloselyresemblesthatofS-Attention. Thenweconcatenatetheoutputsof
S-AttentionandT-Attentionasfollows:
|     |     | Criss-Cross-Attention(E˜)=Concat(head |             |       |                        | ,head | ,...,head        | )   |     | (8) |
| --- | --- | ------------------------------------- | ----------- | ----- | ---------------------- | ----- | ---------------- | --- | --- | --- |
|     |     |                                       |             |       |                        | 1     | 2                | K   |     |     |
|     |     |                                       | (cid:40)    | (E˜), |                        |       |                  |     |     |     |
|     |     |                                       | S-Attention | k     |                        |       | k ∈[1,2,...,K/2] |     |     |     |
|     |     | head                                  | =           |       |                        |       |                  |     |     | (9) |
|     |     | k                                     |             | (E˜), |                        |       |                  |     |     |     |
|     |     |                                       | T-Attention |       | k ∈[K/2+1,K/2+2,...,K] |       |                  |     |     |     |
k
| wherehead |     | representstheoutputofthek-thhead. |     |     |     |     |     |     |     |     |
| --------- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
k
M
There are criss-cross transformer blocks in CBraMod. The output of criss-cross transformer
|     |     | Er {er |     |     |     |     | er  | Rd  |     |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
is denoted as = |i ∈ [1,2,...,C],j ∈ [1,2,...,n]}, where ∈ is an EEG patch
|                      |     |     | i,j                                       |     |     |     |     | i,j |     |     |
| -------------------- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| representation,andEr |     |     | ∈RC×n×disthesetofEEGpatchrepresentations. |     |     |     |     |     |     |     |
5

PublishedasaconferencepaperatICLR2025
MaskedEEGReconstruction Inordertolearnpowerfulgenericrepresentationsfromunlabeled
EEGdata,weneedtoutilizethetaskofself-supervisedrepresentationlearningtopre-trainCBraMod.
Masked autoencoder (MAE) has been proved to be a simple and effective self-supervised pre-
trainingapproachinthefieldsofnaturallanguageunderstanding,computervision,andtimeseries
forecasting(Devlinetal.,2018;Heetal.,2022;Nieetal.,2022). Weutilizepatch-basedmasked
EEGreconstructiontolearngenericrepresentationfromEEG.Specifically,areconstructionhead,
composedofafully-connectedlayer,isusedtoprojectlearnedEEGrepresentationsErintopredicted
EEGpatchesXˆ = {xˆ |i ∈ [1,2,...,C],j ∈ [1,2,...,n]},wherexˆ ∈ Rt isthepredictedEEG
i,j i,j
patchcorrespondingtooneoriginalEEGpatchx ,andXˆ ∈RC×n×tisthesetofpredictedEEG
i,j
patchescorrespondingtothesetoforiginalEEGpatchesX.
ConsistentwithmostofexistingMAEstudies(Heetal.,2022;Xieetal.,2022),weonlyreconstruct
themaskedEEGpatches. GiventhementionedmaskM={m |i∈[1,2,...,C],j ∈[1,2,...,n]},
i,j
wegetthesetofthemaskedpredictedEEGpatchesXˆM andthesetofthemaskedoriginalEEG
patchesXM asfollows:
XˆM ={xˆ |m =1,i∈[1,2,...,C],j ∈[1,2,...,n]} (10)
i,j i,j
XM ={x |m =1,i∈[1,2,...,C],j ∈[1,2,...,n]} (11)
i,j i,j
wherem ∈{0,1}denotesthemaskindicatorofx .
i,j i,j
Finally,weusethemeansquareerror(MSE)asreconstructionlossfunction:
L=∥XˆM −XM∥2 (12)
3 EXPERIMENTS
3.1 PRE-TRAINING
Pre-trainingDataset CBraModispre-trainedonaverylargepublicdataset,TempleUniversity
HospitalEEGcorpus(TUEG)(Obeid&Picone,2016). TheTUEGdatasetconsistsofadiverse
archiveof69,652clinicalEEGrecordingsfrom14,987subjectsacross26,846sessions,withatotal
duration of 27,062 hours. The archive has over 40 different channel configurations and varying
durationofrecordings. Mostoftherecordingsaresampledat256Hz. Unfortunately,theTUEG
datasetsuffersfromsignificantdatacontamination,includingasubstantialamountofunmarkednoise,
artifacts,andfaultychannels. Manualremovaloftheseinterferencefactorspresentsconsiderable
challenges. Thusweutilizearangeofautomatedtechniquestopreprocessthedata.
Preprocessing Firstly,therecordingswithatotaldurationofnomorethan5minutesareremoved,
thenthefirstoneminuteandlastoneminuteofeachrecordingarealsodiscarded,sothatwecan
remove low-quality data as much as possible. Next, we select 19 common EEG channels (Fp1,
Fp2,F7,F3,Fz,F4,F8,T3,C3,Cz,C4,T4,T5,P3,Pz,P4,T6,O1,O2)thatmeetasubsetofthe
10-20internationalelectrodeplacementsystemstandardstoobtaincleananduniformlyformatted
pre-trainingdata. Thenaband-passfiltered(0.3Hz–75Hz)isappliedtoremovethelow-frequency
andhigh-frequencynoise. Anotchfilter(60Hz)isusedtoremovethepowerlinenoise. AllEEG
signalsareresampledto200Hzandsegmentedto30-secondnon-overlappingEEGsamples.
However,theaforementionedpreprocessingstillcannotcompletelysolvethequalityissuesofEEG
data. Therefore,weadoptasimpleandautomatedEEGbadsampleremovalschemetoobtainclean
pre-training EEG data. Specifically, we regard EEG samples as bad samples in which any data
point has an absolute amplitude exceeding 100 µV, and remove them from the dataset. Finally,
we normalize EEG by setting the unit to 100 µV to guarantee the value mainly between -1 to 1,
consistentwithLaBraM(Jiangetal.,2024). Tosumup,thereare1,109,545EEGsamplesretained
for pre-training and longer than 9000 hours in total, significantly exceeding the amount of EEG
samplesusedforpretrainingLaBraM(2,534.78hours)(Jiangetal.,2024).
Pre-trainingSettings WeimplementedCBraModbasedonthePython3.11.7andPyTorch2.1.2+
CUDA12.1. WesetthetimedurationofeachEEGpatchas1second(200datapoints),andone
30-secondEEGsampleissegmentedto19×30=570EEGpatches. Forthemodelconfigurations,
thepatchencoderconsistsof3-layer1DconvolutionwithgroupnormalizationandGELUactivation.
Thepositionalencoderisanone-layer2DdepthwiseCNN.ThebackboneofCBraModisa12-layer
6

PublishedasaconferencepaperatICLR2025
criss-crosstransformerwith200hiddendimensions,800innerdimensions(feed-forward),and
8-headcriss-crossattention(4headsforS-Attentionand4headsforV-Attention). 50%ofmask
ratioisusedtorandomlymaskthepatches. Thebatchsizewassetto128andthenumberofepochs
wassetto40. ThemodelistrainedusingtheAdamWoptimizerwithdefaultsettings,thelearning
rateissetto5e-4andtheweightdecayissetto5e-2. CosineAnnealingLRwasusedtodynamically
adjustthelearningrateduringthepre-training. CBraModwaspre-trainedononemachinewithIntel
XeonGold6226RCPUandfourNVIDIARTXA5000GPUforabout5days. Moredetailscanbe
foundinAppendixB.
3.2 EXPERIMENTSETUPOFDOWNSTREAMBCITASKS
Downstream BCI Tasks and Datasets To comprehensively evaluate the performance of our
method, we select up to 10 downstream BCI tasks. All the downstream BCI tasks with the cor-
respondingdatasetsarepresentedinTable1andAppendixD.1. Forallthedownstreamdatasets,
weresampledtheEEGsignalsinto200HzandsetthetimedurationofeachEEGpatchas1
second(200datapoints),consistentwiththepre-trainingdata. Moredetailsofeachdatasetandits
preprocessingareintroducedinSection3.3andAppendixE.
Table1: OverviewofdownstreamBCItasksanddatasets.
BCITasks Datasets Rate #Channels Duration #Samples Label
I.EmotionRecognition FACED 250Hz 32 10s 10,332 9-class
SEED-V 1000Hz 62 1s 117,744 5-class
II.MotorImageryClassification PhysioNet-MI 160Hz 64 4s 9,837 4-class
SHU-MI 250Hz 32 4s 11,988 2-class
III.SleepStaging ISRUC 200Hz 6 30s 89,240 5-class
IV.SeizureDetection CHB-MIT 256Hz 16 10s 326,993 2-class
V.ImaginedSpeechClassification BCIC2020-3 256Hz 64 3s 6,000 5-class
VI.MentalDisorderDiagnosis Mumtaz2016 256Hz 19 5s 7,143 2-class
VII.VigilanceEstimation SEED-VIG 200Hz 17 8s 20,355 regression
VIII.MentalStressDetection MentalArithmetic 500Hz 20 5s 1,707 2-class
IX.EventTypeClassification TUEV 250Hz 16 5s 112,491 6-class
X.AbnormalDetection TUAB 250Hz 16 10s 409,455 2-class
Baselines WecompareCBraModwithbothnon-foundation-modelandfoundation-modelbaseline
onallthedownstreamBCItasks,forcomprehensiveevaluation. Weadoptthefollowingmethods
asnon-foundation-modelbaselines: EEGNet(Lawhernetal.,2018),EEGConformer(Songetal.,
2022),SPaRCNet(Jingetal.,2023),ContraWR(Yangetal.,2021),CNN-Transformer(Pehetal.,
2022),FFCL(Lietal.,2022),andST-Transformer(Songetal.,2021). Were-implementedabove
baselinesbasedonthepubliccodeprovidedbyBIOT(Yangetal.,2023)unlesstheirexperimental
resultshavealreadybeenreportedinexistingstudies. Besides,weuseBIOT(Yangetal.,2023)and
LaBraM(Jiangetal.,2024)asthefoundation-modelbaselines. Wefine-tuneBIOTandLaBraM
basedontheirpubliccodeandpre-trainedweights,unlesstheirexperimentalresultshavealreadybeen
reportedintheoriginalpapers. Notably,LaBraMhasthreedifferentconfigurations,LaBraM-Base,
LaBraM-LargeandLaBraM-Huge,butonlythepre-trainedweightsofLaBraM-Baseareopened
publicly. Weonlyfine-tunetheLaBraM-Baseinourexperiments.
Metrics WeadoptBalancedAccuracy,AUC-PRandAUROCasevaluationmetricsforbinary
classification, where AUROC is set as the monitor score. For multi-class classification, we use
BalancedAccuracy,Cohen’sKappaandWeightedF1forevaluation,whereCohen’sKappaisset
asthemonitorscore. Pearson’sCorrelation,R2ScoreandRMSEareusedasevaluationmetrics
forregression,whereR2scoreisutilizedasthemonitorscore. Weobtainalltheresultswithfive
differentrandomseedsandreportthemeanandstandarddeviationvalues. AppendixDshowsmore.
3.3 RESULTS
ForprovingthecapabilityandgeneralizabilityofCBraMod,weevaluateCBraModandbaselines
onupto10downstreamBCItasksusing12publiclyavailabledatasets,listedinTable1. Inallthe
experiments,weensurestrictconsistencyinthesplitsoftraining,validation,andtestsetsfor
everymethod.Inthissection,weshowtheexperimentalresultsondownstreamBCItasksofemotion
recognitionandmotorimageryclassificationon4datasets. MoreresultsareshowninAppendixE.
PerformanceComparisonwithBaselines WecompareCBraModwiththebaselinesasfollows:
7

PublishedasaconferencepaperatICLR2025
Table2: Theresultsofdifferentmethodsonemotionrecognition.
FACED,9-class SEED-V,5-class
Methods BalancedAccuracy Cohen’sKappa WeightedF1 BalancedAccuracy Cohen’sKappa WeightedF1
EEGNet 0.4090±0.0122 0.3342±0.0251 0.4124±0.0141 0.2961±0.0102 0.1006±0.0143 0.2749±0.0098
EEGConformer 0.4559±0.0125 0.3858±0.0186 0.4514±0.0107 0.3537±0.0112 0.1772±0.0174 0.3487±0.0136
SPaRCNet 0.4673±0.0155 0.3978±0.0289 0.4729±0.0133 0.2949±0.0078 0.1121±0.0139 0.2979±0.0083
ContraWR 0.4887±0.0078 0.4231±0.0151 0.4884±0.0074 0.3546±0.0105 0.1905±0.0188 0.3544±0.0121
CNN-Transformer 0.4697±0.0132 0.4017±0.0168 0.4720±0.0125 0.3678±0.0078 0.2072±0.0183 0.3642±0.0088
FFCL 0.4673±0.0158 0.3987±0.0383 0.4699±0.0145 0.3641±0.0092 0.2078±0.0201 0.3645±0.0132
ST-Transformer 0.4810±0.0079 0.4137±0.0133 0.4795±0.0096 0.3052±0.0072 0.1083±0.0121 0.2833±0.0105
BIOT 0.5118±0.0118 0.4476±0.0254 0.5136±0.0112 0.3837±0.0187 0.2261±0.0262 0.3856±0.0203
LaBraM-Base 0.5273±0.0107 0.4698±0.0188 0.5288±0.0102 0.3976±0.0138 0.2386±0.0209 0.3974±0.0111
CBraMod 0.5509±0.0089 0.5041±0.0122 0.5618±0.0093 0.4091±0.0097 0.2569±0.0143 0.4101±0.0108
EmotionRecognition. WeuseFACED(Chenetal.,2023)andSEED-V1 (Liuetal.,2021b)asthe
evaluation datasets of emotion recognition. FACED is a large finer-grained affective computing
EEGdatasetrecording32-channelEEGsignalsat250Hzsamplingratefrom123subjects,which
coversnineemotioncategoriesincludingamusement,inspiration,joy,tenderness,anger,fear,disgust,
sadness,andneutralemotion. TheEEGsignalsaresegmentedinto10,33210-secondsamplesand
resampledto200Hz. Weusesubject1to80fortraining,81to100forvalidation,and101to123for
testinFACED.SEED-VisanemotionEEGdatasetcontainingfiveemotioncategories(happy,sad,
neutral,disgust,andfear),consistingofEEGsignals(62channels,1000Hz)from16subjectsthrough
threesessionspersubject,whereonesessionhasfifteentrials. TheEEGsignalsaresegmentedinto
117,7441-secondsamplesandresampledto200Hz. Wedividethefifteentrialsofeachsessioninto
threeequalparts(5:5:5)asthetraining,validationandtestsets,respectively. Theexperimentalresults
ofemotionrecognitionarepresentedinTable2. CBraModachievesthestate-of-the-artperformance
on both FACED and SEED-V. Specifically, CBraMod obtains a great performance improvement
comparedtothebestbaselineLaBraM(0.5041v.s. 0.4698inCohen’sKappaonFACEDand0.2569
v.s. 0.2386inCohen’sKappaonSEED-V).
Table3: Theresultsofdifferentmethodsonmotorimageryclassification.
PhysioNet-MI,4-class SHU-MI,2-class
Methods BalancedAccuracy Cohen’sKappa WeightedF1 BalancedAccuracy AUC-PR AUROC
EEGNet 0.5814±0.0125 0.4468±0.0199 0.5796±0.0115 0.5889±0.0177 0.6311±0.0142 0.6283±0.0152
EEGConformer 0.6049±0.0104 0.4736±0.0171 0.6062±0.0095 0.5900±0.0107 0.6370±0.0093 0.6351±0.0101
SPaRCNet 0.5932±0.0152 0.4564±0.0234 0.5937±0.0147 0.5978±0.0097 0.6510±0.0062 0.6431±0.0082
ContraWR 0.5892±0.0133 0.4527±0.0248 0.5918±0.0116 0.5873±0.0128 0.6315±0.0105 0.6273±0.0113
CNN-Transformer 0.6053±0.0118 0.4725±0.0223 0.6041±0.0105 0.5975±0.0169 0.6412±0.0076 0.6323±0.0082
FFCL 0.5726±0.0092 0.4323±0.0182 0.5701±0.0079 0.5692±0.0252 0.5943±0.0172 0.6014±0.0168
ST-Transformer 0.6035±0.0081 0.4712±0.0199 0.6053±0.0075 0.5992±0.0206 0.6394±0.0122 0.6431±0.0111
BIOT 0.6153±0.0154 0.4875±0.0272 0.6158±0.0197 0.6179±0.0183 0.6770±0.0119 0.6609±0.0127
LaBraM-Base 0.6173±0.0122 0.4912±0.0192 0.6177±0.0141 0.6166±0.0192 0.6761±0.0083 0.6604±0.0091
CBraMod 0.6417±0.0091 0.5222±0.0169 0.6427±0.0100 0.6370±0.0151 0.7139±0.0088 0.6988±0.0068
MotorImageryClassification. WeusePhysioNet-MI(Goldbergeretal.,2000;Schalketal.,2004)
andSHU-MI(Maetal.,2022)forevaluationonmotorimageryclassification. PhysioNet-MIisan
EEGmotorimagerydatasetcollectedfrom109subjectswith64channelsand160Hzsamplingrate.
Itcoversfourmotorimageryclassesincludingleftfist,rightfist,bothfistsandbothfeet. TheEEG
signalsaredividedinto9,8374-secondsamplesandresampledto200Hz. Subject1–70, 71–89,
90–109areusedfortraining,validationandtest,respectively. SHU-MIisanEEGmotorimagery
datasetwithtwocategories(lefthandandrighthand). Itconsistsof32-channelEEGsignalswith250
Hzsamplingrate,collectedfrom25subjects. TheEEGsignalsaresegmentedinto11,988samples
andresampledto200Hz. Weusesubject1to15fortraining,subject16to20forvalidation,and
21 to 25 for test. The results are shown in Table 3. CBraMod achieves the best performance on
bothdatasets. Specifically,CBraModachievesasignificantperformancegaincomparedtothebest
baselineLaBraM(0.5222v.s. 0.4912inCohen’sKappa)onPhysioNet-MI.OnSHU-MI,CBraMod
obtainsabetterperformancecomparedtothebestbaselineBIOT(0.6988v.s. 0.6609inAUROC).
1Weusedtheopen-sourceversionofSEED-Vwith16subjects, ratherthantheprivateversionwith20
subjectsusedinLaBraM(Jiangetal.,2024).
8

PublishedasaconferencepaperatICLR2025
All the above results indicate that CBraMod can learn powerful EEG representations which are
helpfultothedownstreamBCItasksofemotionrecognitionandmotorimageryclassification.
|     |     | Ours full attention | axial attention | attention (CCNet) |     |
| --- | --- | ------------------- | --------------- | ----------------- | --- |
ycaruccA decnalaB 0.60 0.55 0.60 ycaruccA decnalaB 0.45 0.30 0.45
|      | appaK s'nehoC |             |      | appaK s'nehoC |             |
| ---- | ------------- | ----------- | ---- | ------------- | ----------- |
|      |               | 1F dethgieW |      |               | 1F dethgieW |
| 0.55 | 0.50          | 0.55        | 0.40 | 0.25          | 0.40        |
0.50 FACED, 9-class 0.45 FACED, 9-class 0.50 FACED, 9-class 0.35 SEED-V, 5-class 0.20 SEED-V, 5-class 0.35 SEED-V, 5-class
ycaruccA decnalaB 0.70 0.55 0.70 ycaruccA decnalaB 0.70 0.75 0.75
|      | appaK s'nehoC | 1F dethgieW |      |        |       |
| ---- | ------------- | ----------- | ---- | ------ | ----- |
|      |               |             |      | RP-CUA | CORUA |
| 0.65 | 0.50          | 0.65        | 0.65 | 0.70   | 0.70  |
| 0.60 | 0.45          | 0.60        | 0.60 | 0.65   | 0.65  |
PhysioNet-MI, 4-class PhysioNet-MI, 4-class PhysioNet-MI, 4-class SHU-MI, 2-class SHU-MI, 2-class SHU-MI, 2-class
|     | Figure4: | Theresultsofattentionmechanismcomparison. |     |     |     |
| --- | -------- | ----------------------------------------- | --- | --- | --- |
AttentionMechanismComparison Inordertoprovetheeffectivenessofcriss-crossattention
mechanism, wecompareitwithotherattentionmechanismsuchasfullattention(Vaswanietal.,
2017;Dosovitskiyetal.,2020),axialattention(Hoetal.,2019)andthecriss-crossattentionmodule
in CCNet (Huang et al., 2019). Full attention mechanism equally models the spatial-temporal
dependenciesamongallEEGpatchesinonetransformerblock. Axialattentionmechanismmodels
thedependenciesalongspecificaxialdimensionsofEEGpatchesinonetransformerblock. Itcan
sequentiallymodelspatialortemporaldependenciesamongEEGpatchesindifferentblocks. Inour
experiment,theaxialattentiononlymodelsthespatialdependenciesintransformerblock1–6and
modelsthetemporaldependenciesintransformerblock7–12. Thecriss-crossattentionmechanismin
CCNetisbasedontheaffinityoperation,usingasingleattentionmaptoachievecriss-crossmodeling.
Wepre-trainedandfine-tunedthemodelsbasedonthethreeattentionmechanismswiththesame
settings as CBraMod. The performance comparison on emotion recognition and motor imagery
classificationisshowninFigure4. Fullattentionachievestheworstperformanceacrossalldatasets.
ItindicatesthatfullattentionequallymodelsthedependenciesamongallEEGpatches,ignoringthe
uniquestructuralcharacteristicsofEEGsignals. Meanwhile,therearemorethan570EEGpatchesin
oneEEGsample(19channels,30seconds)inthepre-trainingdataset,whichexceedstheappropriate
modelingrangeforfullattention. Axialattentionoutperformsfullattentionbecauseitprioritizes
directlymodelingspecificaxialdimensionsofEEGpatches,whichcaneffectivelycapturethespatial-
temporal dependencies among EEG patches. But it performs worse than criss-cross attention in
CBraMod. Itindicatesthatthecriss-crossattentioncanmodelspatialandtemporaldependencies
amongEEGpatchesinparallel,whicharemoreeffectivethansequentialmodelingofaxialattention
forEEGmodeling.TheattentioninCCNetperformsslightlybetterthanfullattentionbutsignificantly
worsethatourattentionmechanism,indicatingthatthesingle-mapcriss-crossattentiondesignedfor
imageinCCNetmaybenotsuitableforEEGmodeling. EEGsignalscontainheterogeneousspatial
andtemporaldependencies. Ourmethodemploysdualparallelspatialandtemporalattentionsto
capturespatialandtemporaldependencies,whichismoresuitableforEEGmodeling.
|     |     | Ours w/o PE | w/ APE | w/ CPE |     |
| --- | --- | ----------- | ------ | ------ | --- |
ycaruccA decnalaB 0.60 0.55 0.60 ycaruccA decnalaB 0.45 0.30 0.45
|      | appaK s'nehoC | 1F dethgieW |      | appaK s'nehoC | 1F dethgieW |
| ---- | ------------- | ----------- | ---- | ------------- | ----------- |
| 0.55 | 0.50          | 0.55        | 0.40 | 0.25          | 0.40        |
| 0.50 | 0.45          | 0.50        | 0.35 | 0.20          | 0.35        |
FACED, 9-class FACED, 9-class FACED, 9-class SEED-V, 5-class SEED-V, 5-class SEED-V, 5-class
| ycaruccA decnalaB 0.70 | 0.55          | 0.70        | ycaruccA decnalaB 0.70 | 0.75   |           |
| ---------------------- | ------------- | ----------- | ---------------------- | ------ | --------- |
|                        | appaK s'nehoC | 1F dethgieW |                        |        |           |
| 0.65                   |               | 0.65        | 0.65                   | RP-CUA | CORUA 0.7 |
|                        | 0.50          |             |                        | 0.70   |           |
| 0.60                   |               | 0.60        | 0.60                   |        |           |
| 0.55                   | 0.45          | 0.55        | 0.55                   | 0.65   | 0.6       |
PhysioNet-MI, 4-class PhysioNet-MI, 4-class PhysioNet-MI, 4-class SHU-MI, 2-class SHU-MI, 2-class SHU-MI, 2-class
|     | Figure5: | Theresultsofpositionalencodingcomparison. |     |     |     |
| --- | -------- | ----------------------------------------- | --- | --- | --- |
PositionalEncodingComparison Weconductthepositionalencodingcomparisontoevaluatethe
effectivenessofasymmetricconditionalpositionalencoding(ACPE).Specifically,wecompareACPE
withfollowingsettings: 1)withoutpositionalencoding(w/oPE):donotusepositionalencodingto
encodepostionalinformation;2)withabsolutepositionalencoding(w/APE):replaceACPEwith
9

PublishedasaconferencepaperatICLR2025
APE;3)withconditionalpositionalencoding(w/CPE):replaceACPEwithCPE.Theresultsare
showninFigure5. CBraModwithoutPEperformstheworst,indicatingthatpositionalencoding
isimportantinEEGmodeling. APEperformsbetterthanw/oPEbutworsethanCPEandACPE,
indicatingthatAPEisnotsoeffectiveasCPEinadaptingtodifferentEEGformats. CPE,usually
usedforimagepatches,performsslightlyworsecomparedtoACPEinCBraMod,indicatingthatthe
asymmetricdesignsareslightlybetterthansymmetricdesignsinEEGmodeling. Itmaybebecause
thatEEGpatchesexhibitdifferentdependenciesinspatial(channel)andtemporaldimension,which
aredifferentfromthedependenciesbetweenimagepatches.
Table4: Theresultsofablationstudyonpre-training.
FACED,9-class SEED-V,5-class
Settings BalancedAccuracy Cohen’sKappa WeightedF1 BalancedAccuracy Cohen’sKappa WeightedF1
cleanpre-training 0.5509±0.0089 0.5041±0.0122 0.5618±0.0093 0.4091±0.0097 0.2569±0.0143 0.4101±0.0108
dirtypre-training 0.5319±0.0245 0.4768±0.0348 0.5397±0.0219 0.3914±0.0217 0.2224±0.0318 0.3894±0.0243
w/opre-training 0.5232±0.0216 0.4615±0.0289 0.5304±0.0187 0.3902±0.0241 0.2211±0.0384 0.3879±0.0225
PhysioNet-MI,4-class SHU-MI,2-class
Settings BalancedAccuracy Cohen’sKappa WeightedF1 BalancedAccuracy AUC-PR AUROC
cleanpre-training 0.6417±0.0091 0.5222±0.0169 0.6427±0.0100 0.6370±0.0151 0.7139±0.0088 0.6988±0.0068
dirtypre-training 0.6245±0.0153 0.5063±0.0256 0.6223±0.0167 0.6301±0.0189 0.7026±0.0176 0.6895±0.0131
w/opre-training 0.6196±0.0143 0.4994±0.0289 0.6157±0.0145 0.6289±0.0179 0.7032±0.0145 0.6878±0.0166
AblationStudyonPre-training Tofurtherevaluatetheeffectivenessofpre-training,weconduct
anablationstudyonpre-training. Thepre-trainingablationexperimentisdesignedasfollows: 1)w/o
pre-training: directlytrainingCBraModondownstreamdatasets;2)dirtypre-training: pre-training
CBraMod on TUEG corpus without bad samples dropping. 3) clean pre-training: pre-training
CBraMod on TUEG corpus with bad samples dropping. The results are presented in Table 4.
Obviously, clean pre-training achieves the best performance, obtaining significant performance
increases compared to dirty pre-training and w/o pre-training. Besides, the performance has a
smallervariancecomparedtodirtypre-trainingandw/opre-training. Theseindicatethatourpre-
trainingstrategycanhelpCBraModlearngenericrepresentationsfromEEG,whichcanimprove
thegeneralizabilityandstabilityofCBraModondownstreamdatasets. Dirtypre-trainingperforms
slightlybetterthanw/opre-training,indicatingthatalargeamountofdirtydataintheoriginaldataset
canweakentheeffectivenessofpre-training.
4 CONCLUSION
In this paper, we propose an EEG foundation model called CBraMod, which can learn generic
representationsofEEGsignalsthroughpatch-basedmaskedEEGreconstruction. Specifically,we
devise a criss-cross transformer as the backbone of CBraMod to model the spatial and temporal
dependenciesbetweenEEGpatchesinparallel,andanasymmetricconvolutionalpositionalencoding
scheme to encode spatial-temporal positional information of EEG signals with diverse formats.
CBraMod is pre-trained on TUEG, a very large corpus of EEG. CBraMod achieves the state-of-
the-artperformanceacrossupto10downstreamBCItasks(12publicdatasets),provingitsstrong
capabilityandgeneralizability.Wehopethattheproposedmodelingapproachandpositionalencoding
schemecanprovidemeaningfulinsightsforbuildingEEGfoundationmodels,therebyadvancingthe
developmentofreal-worldBCIsystems.
ACKNOWLEDGMENTS
ThisworkwassupportedbySTI2030MajorProjects(2021ZD0200400),NaturalScienceFoundation
of China (No. 61925603) and the Key Program of the Natural Science Foundation of Zhejiang
Province,China(No. LZ24F020004). ThecorrespondingauthorsareDr. ShaZhaoandDr. Gang
Pan.
REFERENCES
AhmedAbdelhameedandMagdyBayoumi.Adeeplearningapproachforautomaticseizuredetection
inchildrenwithepilepsy. FrontiersinComputationalNeuroscience,15:650050,2021.
10

PublishedasaconferencepaperatICLR2025
JoshAchiam,StevenAdler,SandhiniAgarwal,LamaAhmad,IlgeAkkaya,FlorenciaLeoniAleman,
DiogoAlmeida,JankoAltenschmidt,SamAltman,ShyamalAnadkat,etal. Gpt-4technicalreport.
arXivpreprintarXiv:2303.08774,2023.
IjazAhmad,XinWang,MingxingZhu,ChengWang,YaoPi,JavedAliKhan,SiyabKhan,Oluwaro-
timiWilliamsSamuel,ShixiongChen,andGuanglinLi. Eeg-basedepilepticseizuredetection
via machine/deep learning approaches: A systematic review. Computational Intelligence and
Neuroscience,2022,2022.
Ali Al-Saegh, Shefa A Dawwd, and Jassim M Abdul-Jabbar. Deep learning for motor imagery
eeg-basedclassification: Areview. BiomedicalSignalProcessingandControl,63:102172,2021.
HamdiAltaheri,GhulamMuhammad,MansourAlsulaiman,SyedUmarAmin,GhadirAliAltuwaijri,
WadoodAbdul,MohamedABencherif,andMohammedFaisal. Deeplearningtechniquesfor
classification of electroencephalogram (eeg) motor imagery (mi) signals: A review. Neural
ComputingandApplications,pp.1–42,2021.
Hubert Banville, Omar Chehab, Aapo Hyva¨rinen, Denis-Alexander Engemann, and Alexandre
Gramfort. Uncoveringthestructureofclinicaleegsignalswithself-supervisedlearning. Journal
ofNeuralEngineering,18(4):046020,2021.
AliBashashati,MehrdadFatourechi,RababKWard,andGaryEBirch. Asurveyofsignalprocessing
algorithms in brain–computer interfaces based on electrical brain signals. Journal of Neural
engineering,4(2):R32,2007.
RishiBommasani, DrewAHudson, EhsanAdeli, RussAltman, SimranArora, SydneyvonArx,
MichaelSBernstein,JeannetteBohg,AntoineBosselut,EmmaBrunskill,etal. Ontheopportuni-
tiesandrisksoffoundationmodels. arXivpreprintarXiv:2108.07258,2021.
Tim Brooks, Bill Peebles, Connor Holmes, Will DePue, Yufei Guo, Li Jing, David Schnurr, Joe
Taylor, Troy Luhman, Eric Luhman, Clarence Ng, Ricky Wang, and Aditya Ramesh. Video
generation models as world simulators. 2024. URL https://openai.com/research/
video-generation-models-as-world-simulators.
Clemens Brunner, Robert Leeb, Gernot Mu¨ller-Putz, Alois Schlo¨gl, and Gert Pfurtscheller. Bci
competition2008–grazdataseta. Instituteforknowledgediscovery(laboratoryofbrain-computer
interfaces),GrazUniversityofTechnology,16:1–6,2008.
JingjingChen,XiaobinWang,ChenHuang,XinHu,XinkeShen,andDanZhang. Alargefiner-
grainedaffectivecomputingeegdataset. ScientificData,10(1):740,2023.
MouxiangChen,LefeiShen,ZhuoLi,XiaoyunJoyWang,JianlingSun,andChenghaoLiu. Visionts:
Visual masked autoencoders are free-lunch zero-shot time series forecasters. arXiv preprint
arXiv:2408.17253,2024.
Hsiang-Yun Sherry Chien, Hanlin Goh, Christopher M Sandino, and Joseph Y Cheng. Maeeg:
Maskedauto-encoderforeegrepresentationlearning. arXivpreprintarXiv:2211.02625,2022.
XiangxiangChu,ZhiTian,BoZhang,XinlongWang,andChunhuaShen. Conditionalpositional
encodingsforvisiontransformers. arXivpreprintarXiv:2102.10882,2021.
AlexanderCraik,YongtianHe,andJoseLContreras-Vidal. Deeplearningforelectroencephalogram
(eeg)classificationtasks: areview. Journalofneuralengineering,16(3):031001,2019.
Didar Dadebayev, Wei Wei Goh, and Ee Xion Tan. Eeg-based emotion recognition: Review of
commercial eeg devices and machine learning techniques. Journal of King Saud University-
ComputerandInformationSciences,34(7):4385–4401,2022.
GuanghaiDai,JunZhou,JiahuiHuang,andNingWang. Hs-cnn: acnnwithhybridconvolution
scaleforeegmotorimageryclassification. Journalofneuralengineering,17(1):016025,2020.
MuhammadNajamDar,MuhammadUsmanAkram,SajidGulKhawaja,andAmitNPujari. Cnn
andlstm-basedemotionchartingusingphysiologicalsignals. Sensors,20(16):4551,2020.
11

PublishedasaconferencepaperatICLR2025
MostafaDehghani,JosipDjolonga,BasilMustafa,PiotrPadlewski,JonathanHeek,JustinGilmer,
AndreasSteiner,MathildeCaron,RobertGeirhos,IbrahimAlabdulmohsin,etal. Scalingvision
transformersto22billionparameters. InProceedingsofthe40thInternationalConferenceon
MachineLearning,pp.7480–7512,2023.
GuifengDeng,MengfanNiu,YuxiLuo,ShuyingRao,JingSun,JunyiXie,ZhengheYu,WenjuanLiu,
ShaZhao,GangPan,XiaojingLi,WeiDeng,WanjuanGuo,TaoLi,andHaitengJiang. Lpsgm:
A unified flexible large psg model for sleep staging and mental disorder diagnosis. medRxiv,
2024. doi: 10.1101/2024.12.11.24318815. URLhttps://www.medrxiv.org/content/
early/2024/12/11/2024.12.11.24318815.
JacobDevlin,Ming-WeiChang,KentonLee,andKristinaToutanova. Bert: Pre-trainingofdeep
bidirectionaltransformersforlanguageunderstanding. arXivpreprintarXiv:1810.04805,2018.
YiDing,NeethuRobinson,SuZhang,QiuhaoZeng,andCuntaiGuan.Tsception:Capturingtemporal
dynamicsandspatialasymmetryfromeegforemotionrecognition. IEEETransactionsonAffective
Computing,2022.
YiDing,NeethuRobinson,ChengxuanTong,QiuhaoZeng,andCuntaiGuan.Lggnet:Learningfrom
local-global-graphrepresentationsforbrain–computerinterface. IEEETransactionsonNeural
NetworksandLearningSystems,pp.1–14,2023.
XiaoyiDong,JianminBao,DongdongChen,WeimingZhang,NenghaiYu,LuYuan,DongChen,
andBainingGuo. Cswintransformer: Ageneralvisiontransformerbackbonewithcross-shaped
windows. InProceedingsoftheIEEE/CVFconferenceoncomputervisionandpatternrecognition,
pp.12124–12134,2022.
AlexeyDosovitskiy,LucasBeyer,AlexanderKolesnikov,DirkWeissenborn,XiaohuaZhai,Thomas
Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, et al. An
image is worth 16x16 words: Transformers for image recognition at scale. arXiv preprint
arXiv:2010.11929,2020.
YangDu,YonglingXu,XiaoanWang,LiLiu,andPengchengMa. Eegtemporal–spatialtransformer
forpersonidentification. ScientificReports,12(1):14378,2022.
YassineElOuahidi,VincentGripon,BastienPasdeloup,GhaithBouallegue,NicolasFarrugia,and
GiuliaLioi. Astrongandsimpledeeplearningbaselineforbcimotorimagerydecoding. IEEE
transactionsonneuralsystemsandrehabilitationengineering,32:3338–3347,2024.
EmadeldeenEldele,MohamedRagab,ZhenghuaChen,MinWu,CheeKeongKwoh,XiaoliLi,and
CuntaiGuan. Time-seriesrepresentationlearningviatemporalandcontextualcontrasting. arXiv
preprintarXiv:2106.14112,2021.
NavidMohammadiFoumani,GeoffreyMackellar,SoheilaGhane,SaadIrtza,NamNguyen,and
MahsaSalehi. Eeg2rep: Enhancingself-supervisedeegrepresentationthroughinformativemasked
inputs. arXivpreprintarXiv:2402.17772,2024.
PengxuanGao,TianyuLiu,Jia-WenLiu,Bao-LiangLu,andWei-LongZheng. Multimodalmulti-
viewspectral-spatial-temporalmaskedautoencoderforself-supervisedemotionrecognition. In
ICASSP2024-2024IEEEInternationalConferenceonAcoustics,SpeechandSignalProcessing
(ICASSP),pp.1926–1930.IEEE,2024.
AryLGoldberger,LuisANAmaral,LeonGlass,JeffreyMHausdorff,PlamenChIvanov,RogerG
Mark,JosephEMietus,GeorgeBMoody,Chung-KangPeng,andHEugeneStanley. Physiobank,
physiotoolkit,andphysionet: componentsofanewresearchresourceforcomplexphysiologic
signals. circulation,101(23):e215–e220,2000.
Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image
recognition. InProceedingsoftheIEEEconferenceoncomputervisionandpatternrecognition,
pp.770–778,2016.
Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr Dolla´r, and Ross Girshick. Masked
autoencodersarescalablevisionlearners.InProceedingsoftheIEEE/CVFconferenceoncomputer
visionandpatternrecognition,pp.16000–16009,2022.
12

PublishedasaconferencepaperatICLR2025
JonathanHo,NalKalchbrenner,DirkWeissenborn,andTimSalimans. Axialattentioninmultidi-
mensionaltransformers. arXivpreprintarXiv:1912.12180,2019.
ZilongHuang,XinggangWang,LichaoHuang,ChangHuang,YunchaoWei,andWenyuLiu. Ccnet:
Criss-crossattentionforsemanticsegmentation. InProceedingsoftheIEEE/CVFinternational
conferenceoncomputervision,pp.603–612,2019.
ConradIber,SoniaAncoli-Israel,AndrewL.Chesson,andStuartF.Quan. TheAmericanAcademy
ofSleepMedicine(AASM)ManualfortheScoringofSleepandAssociatedEvents: Rules,Termi-
nologyandTechnicalSpecifications,volume1. AmericanacademyofsleepmedicineWestchester,
IL,2007.
Ji-Hoon Jeong, Jeong-Hyun Cho, Young-Eun Lee, Seo-Hyun Lee, Gi-Hwan Shin, Young-Seok
Kweon, Jose´ del R Milla´n, Klaus-Robert Mu¨ller, and Seong-Whan Lee. 2020 international
brain–computerinterfacecompetition: Areview. FrontiersinHumanNeuroscience,16:898300,
2022.
ZiyuJia,YoufangLin,JingWang,RonghaoZhou,XiaojunNing,YuanlaiHe,andYaoshuaiZhao.
Graphsleepnet: Adaptivespatial-temporalgraphconvolutionalnetworksforsleepstageclassifica-
tion. InIJCAI,volume2021,pp.1324–1330,2020.
ZiyuJia, YoufangLin, JingWang, XiaojunNing, YuanlaiHe, RonghaoZhou, YuhanZhou, and
HLehmanLi-wei. Multi-viewspatial-temporalgraphconvolutionalnetworkswithdomaingener-
alizationforsleepstageclassification. IEEETransactionsonNeuralSystemsandRehabilitation
Engineering,29:1977–1986,2021.
WeibangJiang,LimingZhao,andBaoliangLu. Largebrainmodelforlearninggenericrepresenta-
tionswithtremendousEEGdatainBCI. InTheTwelfthInternationalConferenceonLearning
Representations,2024. URLhttps://openreview.net/forum?id=QzTpTRVtrP.
JinJing,WendongGe,ShendaHong,MartaBentoFernandes,ZhenLin,ChaoqiYang,SungtaeAn,
AaronFStruck,AlineHerlopian,IoannisKarakis,etal. Developmentofexpert-levelclassification
ofseizuresandrhythmicandperiodicpatternsduringeeginterpretation. Neurology,2023.
SirvanKhalighi,TeresaSousa,Jose´MoutinhoSantos,andUrbanoNunes. Isruc-sleep: Acomprehen-
sivepublicdatasetforsleepresearchers. Computermethodsandprogramsinbiomedicine,124:
180–192,2016.
AlexanderKirillov,EricMintun,NikhilaRavi,HanziMao,ChloeRolland,LauraGustafson,Tete
Xiao,SpencerWhitehead,AlexanderCBerg,Wan-YenLo,etal.Segmentanything.InProceedings
oftheIEEE/CVFInternationalConferenceonComputerVision,pp.4015–4026,2023.
DemetresKostas,StephaneAroca-Ouellette,andFrankRudzicz. Bendr: usingtransformersanda
contrastiveself-supervisedlearningtasktolearnfrommassiveamountsofeegdata. Frontiersin
HumanNeuroscience,15:653659,2021.
VernonJLawhern,AmeliaJSolon,NicholasRWaytowich,StephenMGordon,ChouPHung,and
BrentJLance. Eegnet: acompactconvolutionalneuralnetworkforeeg-basedbrain–computer
interfaces. Journalofneuralengineering,15(5):056013,2018.
YannLeCun,YoshuaBengio,andGeoffreyHinton. Deeplearning. nature,521(7553):436–444,
2015.
HongliLi,ManDing,RonghuaZhang,andChunboXiu. Motorimageryeegclassificationalgorithm
basedoncnn-lstmfeaturefusionnetwork. Biomedicalsignalprocessingandcontrol,72:103342,
2022.
JiyaoLiu,LiZhang,HaoWu,andHuanZhao. Transformersforeegemotionrecognition. arXiv
preprintarXiv:2110.06553,2021a.
WeiLiu,Jie-LinQiu,Wei-LongZheng,andBao-LiangLu. Comparingrecognitionperformance
androbustnessofmultimodaldeeplearningmodelsformultimodalemotionrecognition. IEEE
TransactionsonCognitiveandDevelopmentalSystems,14(2):715–729,2021b.
13

PublishedasaconferencepaperatICLR2025
Xiao Liu, Fanjin Zhang, Zhenyu Hou, Li Mian, Zhaoyu Wang, Jing Zhang, and Jie Tang. Self-
supervisedlearning: Generativeorcontrastive. IEEEtransactionsonknowledgeanddataengi-
neering,35(1):857–876,2021c.
FabienLotte,MarcoCongedo,AnatoleLe´cuyer,FabriceLamarche,andBrunoArnaldi. Areviewof
classificationalgorithmsforeeg-basedbrain–computerinterfaces. Journalofneuralengineering,
4(2):R1,2007.
JunMa,BanghuaYang,WenzhengQiu,YunzheLi,ShouweiGao,andXinxingXia. Alargeeeg
datasetforstudyingcross-sessionvariabilityinmotorimagerybrain-computerinterface. Scientific
Data,9(1):531,2022.
Dennis J McFarland, Charles W Anderson, K-R Muller, Alois Schlogl, and Dean J Krusienski.
Bcimeeting2005-workshoponbcisignalprocessing: featureextractionandtranslation. IEEE
transactionsonneuralsystemsandrehabilitationengineering,14(2):135–138,2006.
LelandMcInnes,JohnHealy,andJamesMelville. Umap: Uniformmanifoldapproximationand
projectionfordimensionreduction. arXivpreprintarXiv:1802.03426,2018.
JianliangMin,PingWang,andJianfengHu. Driverfatiguedetectionthroughmultipleentropyfusion
analysisinaneeg-basedsystem. PLoSone,12(12):e0188756,2017.
Wajid Mumtaz. MDD Patients and Healthy Controls EEG Data (New). 11 2016. doi:
10.6084/m9.figshare.4244171.v2. URLhttps://figshare.com/articles/dataset/
EEG_Data_New/4244171.
YuqiNie,NamHNguyen,PhanwadeeSinthong,andJayantKalagnanam. Atimeseriesisworth64
words: Long-termforecastingwithtransformers. arXivpreprintarXiv:2211.14730,2022.
Iyad Obeid and Joseph Picone. The temple university hospital eeg data corpus. Frontiers in
neuroscience,10:196,2016.
GangPan,Jia-JunLi,YuQi,HangYu,Jun-MingZhu,Xiao-XiangZheng,Yue-MingWang,and
Shao-MinZhang. Rapiddecodingofhandgesturesinelectrocorticographyusingrecurrentneural
networks. Frontiersinneuroscience,12:555,2018.
SamanParvaneh,JonathanRubin,SaeedBabaeizadeh,andMinnanXu-Wilson. Cardiacarrhythmia
detectionusingdeeplearning: Areview. Journalofelectrocardiology,57:S70–S74,2019.
WeiYanPeh,YuanyuanYao,andJustinDauwels. Transformerconvolutionalneuralnetworksfor
automatedartifactdetectioninscalpeeg. In202244thAnnualInternationalConferenceofthe
IEEEEngineeringinMedicine&BiologySociety(EMBC),pp.3599–3602.IEEE,2022.
MathiasPerslev,SuneDarkner,LykkeKempfner,MikiNikolic,PoulJørgenJennum,andChristian
Igel. U-sleep: resilienthigh-frequencysleepstaging. NPJdigitalmedicine,4(1):72,2021.
Huy Phan and Kaare Mikkelsen. Automatic sleep staging of eeg signals: recent development,
challenges,andfuturedirections. PhysiologicalMeasurement,2022.
HuyPhan,FernandoAndreotti,NavinCooray,OliverYChe´n,andMaartenDeVos. Seqsleepnet:
end-to-endhierarchicalrecurrentneuralnetworkforsequence-to-sequenceautomaticsleepstaging.
IEEETransactionsonNeuralSystemsandRehabilitationEngineering,27(3):400–410,2019.
HuyPhan,KaareMikkelsen,OliverYChe´n,PhilippKoch,AlfredMertins,andMaartenDeVos.
Sleeptransformer: Automaticsleepstagingwithinterpretabilityanduncertaintyquantification.
IEEETransactionsonBiomedicalEngineering,69(8):2456–2467,2022.
YuQi,BinLiu,YuemingWang,andGangPan. Dynamicensemblemodelingapproachtononsta-
tionaryneuraldecodinginbrain-computerinterfaces. InProceedingsofthe33rdInternational
ConferenceonNeuralInformationProcessingSystems,pp.6089–6098,2019.
14

PublishedasaconferencepaperatICLR2025
AlecRadford, JongWookKim, ChrisHallacy, AdityaRamesh, GabrielGoh, SandhiniAgarwal,
GirishSastry,AmandaAskell,PamelaMishkin,JackClark,etal. Learningtransferablevisual
modelsfromnaturallanguagesupervision. InMarinaMeilaandTongZhang(eds.),Proceedingsof
the38thInternationalConferenceonMachineLearning,volume139ofProceedingsofMachine
LearningResearch,pp.8748–8763.PMLR,18–24Jul2021.
SiavashSakhavi,CuntaiGuan,andShuichengYan.Learningtemporalinformationforbrain-computer
interfaceusingconvolutionalneuralnetworks. IEEEtransactionsonneuralnetworksandlearning
systems,29(11):5619–5629,2018.
Gerwin Schalk, Dennis J McFarland, Thilo Hinterberger, Niels Birbaumer, and Jonathan R Wol-
paw. Bci2000: ageneral-purposebrain-computerinterface(bci)system. IEEETransactionson
biomedicalengineering,51(6):1034–1043,2004.
Robin Tibor Schirrmeister, Jost Tobias Springenberg, Lukas Dominique Josef Fiederer, Martin
Glasstetter,KatharinaEggensperger,MichaelTangermann,FrankHutter,WolframBurgard,and
TonioBall. Deeplearningwithconvolutionalneuralnetworksforeegdecodingandvisualization.
Humanbrainmapping,38(11):5391–5420,2017.
RymNihelSekkal,FethiBereksi-Reguig,DanielRuiz-Fernandez,NabilDib,andSamiraSekkal.
Automaticsleepstageclassification: Fromclassicalmachinelearningmethodstodeeplearning.
BiomedicalSignalProcessingandControl,77:103751,2022.
RamprasaathRSelvaraju,MichaelCogswell,AbhishekDas,RamakrishnaVedantam,DeviParikh,
andDhruvBatra. Grad-cam: Visualexplanationsfromdeepnetworksviagradient-basedlocal-
ization. InProceedingsoftheIEEEinternationalconferenceoncomputervision,pp.618–626,
2017.
AliHossamShoeb.Applicationofmachinelearningtoepilepticseizureonsetdetectionandtreatment.
PhDthesis,MassachusettsInstituteofTechnology,2009.
YonghaoSong,XueyuJia,LieYang,andLonghanXie. Transformer-basedspatial-temporalfeature
learningforeegdecoding. arXivpreprintarXiv:2106.11170,2021.
YonghaoSong,QingqingZheng,BingchuanLiu,andXiaorongGao. Eegconformer: Convolutional
transformer for eeg decoding and visualization. IEEE Transactions on Neural Systems and
RehabilitationEngineering,31:710–719,2022.
Akara Supratak, Hao Dong, Chao Wu, and Yike Guo. Deepsleepnet: A model for automatic
sleepstagescoringbasedonrawsingle-channeleeg. IEEETransactionsonNeuralSystemsand
RehabilitationEngineering,25(11):1998–2008,2017.
AshishVaswani,NoamShazeer,NikiParmar,JakobUszkoreit,LlionJones,AidanNGomez,Łukasz
Kaiser,andIlliaPolosukhin. Attentionisallyouneed. Advancesinneuralinformationprocessing
systems,30,2017.
ChristopherWang,VighneshSubramaniam,AdamUriYaari,GabrielKreiman,BorisKatz,Ignacio
Cases, and Andrei Barbu. Brainbert: Self-supervised representation learning for intracranial
recordings. InTheEleventhInternationalConferenceonLearningRepresentations,2022.
GuangyuWang,WenchaoLiu,YuhongHe,CongXu,LinMa,andHaifengLi. EEGPT:Pretrained
transformerforuniversalandreliablerepresentationofEEGsignals. InTheThirty-eighthAnnual
ConferenceonNeuralInformationProcessingSystems,2024a. URLhttps://openreview.
net/forum?id=lvS2b8CjG5.
JialingWang,ShiweiCheng,JiemingTian,andYuefanGao. A2dcnn-lstmhybridalgorithmusing
timeseriessegmentsofeegdataformotorimageryclassification. BiomedicalSignalProcessing
andControl,83:104627,2023a.
JiquanWang,ShaZhao,YangxuanZhou,HaitengJiang,ZhengheYu,TaoLi,ShijianLi,andGang
Pan. Narcolepsydiagnosiswithsleepstagefeaturesusingpsgrecordings. IEEETransactionson
NeuralSystemsandRehabilitationEngineering,2023b.
15

PublishedasaconferencepaperatICLR2025
JiquanWang,ShaZhao,HaitengJiang,ShijianLi,TaoLi,andGangPan. Generalizablesleepstaging
viamulti-leveldomainalignment. InProceedingsoftheAAAIConferenceonArtificialIntelligence,
volume38,pp.265–273,2024b.
JiquanWang,ShaZhao,HaitengJiang,YangxuanZhou,ZhengheYu,TaoLi,ShijianLi,andGang
Pan. Caresleepnet: Ahybriddeeplearningnetworkforautomaticsleepstaging. IEEEJournalof
BiomedicalandHealthInformatics,2024c.
PingWang,AiminJiang,XiaofengLiu,JingShang,andLiZhang. Lstm-basedeegclassificationin
motorimagerytasks. IEEEtransactionsonneuralsystemsandrehabilitationengineering,26(11):
2086–2095,2018.
GeraldWoo, Chenghao Liu, AkshatKumar, Caiming Xiong, Silvio Savarese, andDoyen Sahoo.
Unifiedtrainingofuniversaltimeseriesforecastingtransformers.arXivpreprintarXiv:2402.02592,
2024.
ZhaohuiWu,GangPan,andNengganZheng. Cyborgintelligence. IEEEIntelligentSystems,28(5):
31–33,2013.
ZhendaXie,ZhengZhang,YueCao,YutongLin,JianminBao,ZhuliangYao,QiDai,andHanHu.
Simmim: Asimpleframeworkformaskedimagemodeling. InProceedingsoftheIEEE/CVF
conferenceoncomputervisionandpatternrecognition,pp.9653–9663,2022.
Ruibin Xiong, Yunchang Yang, Di He, Kai Zheng, Shuxin Zheng, Chen Xing, Huishuai Zhang,
YanyanLan,LiweiWang,andTie-YanLiu. Onlayernormalizationinthetransformerarchitecture.
In Proceedings of the 37th International Conference on Machine Learning, pp. 10524–10533,
2020.
ChaoqiYang,DanicaXiao,MBrandonWestover,andJimengSun.Self-supervisedeegrepresentation
learningforautomaticsleepstaging. arXivpreprintarXiv:2110.15278,2021.
ChaoqiYang,ZhenbangWu,PatrickJiang,ZhenLin,andJimengSun. Pyhealth: Adeeplearning
toolkitforhealthcarepredictivemodeling,092022. URLhttps://github.com/sunlabuiuc/PyHealth,
2022.
ChaoqiYang,MWestover,andJimengSun. Biot: Biosignaltransformerforcross-datalearningin
thewild. InAdvancesinNeuralInformationProcessingSystems,volume36,pp.78240–78260,
2023.
˙IlkayYıldız,RachaelGarner,MatthewLai,andDominiqueDuncan. Unsupervisedseizureidentifica-
tiononeeg. Computermethodsandprogramsinbiomedicine,215:106604,2022.
ZhizhangYuan,DaozeZhang,JunruChen,GeifeiGu,andYangYang. Brant-2: Foundationmodel
forbrainsignals. arXivpreprintarXiv:2402.10251,2024.
Daoze Zhang, Zhizhang Yuan, Yang Yang, Junru Chen, Jingjing Wang, and Yafeng Li. Brant:
Foundationmodelforintracranialneuralsignal. InAdvancesinNeuralInformationProcessing
Systems,2023.
Daoze Zhang, Zhizhang Yuan, Junru Chen, Kerui Chen, and Yang Yang. Brant-x: A unified
physiologicalsignalalignmentframework. InProceedingsofthe30thACMSIGKDDConference
onKnowledgeDiscoveryandDataMining,pp.4155–4166,2024.
RuilongZhang,QunZong,LiqianDou,andXinyiZhao. Anovelhybriddeeplearningschemefor
four-classmotorimageryclassification. Journalofneuralengineering,16(6):066004,2019a.
ShaominZhang,ShengYuan,LipengHuang,XiaoxiangZheng,ZhaohuiWu,KediXu,andGang
Pan. Human mind control of rat cyborg’s continuous locomotion with wireless brain-to-brain
interface. Scientificreports,9(1):1321,2019b.
XiangZhang,ZiyuanZhao,TheodorosTsiligkaridis,andMarinkaZitnik. Self-supervisedcontrastive
pre-trainingfortimeseriesviatime-frequencyconsistency.InS.Koyejo,S.Mohamed,A.Agarwal,
D. Belgrave, K. Cho, and A. Oh (eds.), Advances in Neural Information Processing Systems,
volume35,pp.3988–4003.CurranAssociates,Inc.,2022.
16

PublishedasaconferencepaperatICLR2025
Yangxuan Zhou, Sha Zhao, Jiquan Wang, Haiteng Jiang, Benyan Luo, Tao Li, Gang Pan, et al.
Personalizedsleepstagingleveragingsource-freeunsuperviseddomainadaptation. arXivpreprint
arXiv:2412.12159,2024a.
Yangxuan Zhou, Sha Zhao, Jiquan Wang, Haiteng Jiang, Zhenghe Yu, Shijian Li, Tao Li, and
GangPan. Simplifyingmultimodalwithsingleeogmodalityforautomaticsleepstaging. IEEE
TransactionsonNeuralSystemsandRehabilitationEngineering,32:1668–1678,2024b.
IgorZyma,SergiiTukaev,IvanSeleznov,KenKiyono,AntonPopov,MariiaChernykh,andOleksii
Shpenkov. Electroencephalograms duringmental arithmetic task performance. Data, 4(1):14,
2019.
17

PublishedasaconferencepaperatICLR2025
A RELATED WORK
EEG Decoding. EEG is a non-invasive technique to measure brain activity. Early studies on
EEGdecodingpredominantlyemployedtraditionalmachinelearningmethods(Bashashatietal.,
2007;McFarlandetal.,2006;Lotteetal.,2007;Qietal.,2019), whichusuallydependonhand-
craftedfeaturesthatrequirelotsofpriorknowledgeandcouldhaveweakgeneralizability. Withthe
developmentofdeeplearning(LeCunetal.,2015)techniques,anincreasingnumberofresearchers
areshiftingtheirfocustostudyingEEGdecodingmethodsbasedondeeplearning(Parvanehetal.,
2019;Craiketal.,2019;Al-Saeghetal.,2021;Sekkaletal.,2022;Yangetal.,2022). Forexample,
somestudiesutilizeconvolutionalneuralnetwork(CNN)toextracttemporalandspatialfeatures
fromEEGfordifferentBCItaskslikemotorimageryclassification,emotionrecognitionandseizure
detection (Schirrmeister et al., 2017; Sakhavi et al., 2018; Lawhern et al., 2018; Abdelhameed
& Bayoumi, 2021; Ding et al., 2022). Long Short-Term Memory (LSTM) is also used for EEG
featureextractionandclassificationonBCItaskssuchasmotorimageryclassificationandsleep
staging (Wang et al., 2018; Phan et al., 2019). Some researchers propose CNN-LSTM to learn
EEG features for motor imagery classification, emotion recognition and sleep staging (Supratak
et al., 2017; Zhang et al., 2019a; Dar et al., 2020; Li et al., 2022; Wang et al., 2023a), where
CNNisusuallyusedtoextractlocalfeaturesandLSTMisutilizedtocaptureglobaldependencies.
Transformerarchitectureisalsoutilizedtolearnspatial-temporalfeatureforBCItasksincluding
emotionrecognition,sleepstagingandpersonidentification(Songetal.,2021;Liuetal.,2021a;Du
etal.,2022;Phanetal.,2022). TocombinethestrengthsofCNNandtransformer,someworksdevise
aCNN-TransformernetworkforEEGclassification(Songetal.,2022;Pehetal.,2022;Wangetal.,
2023b;Zhouetal.,2024b;Wangetal.,2024c). Inaddition,somestudiesusegraphneuralnetworks
learnspatial-temporalfeaturesfrommulti-channelEEGforvariousBCItasks(Jiaetal.,2020;2021;
Dingetal.,2023). Thesemethodsperformwellonspecifictasksordatasets,butcollectinglabeled
EEG data is costly and labor-intensive. Meantime, the variations in EEG signal formats across
differentdatasetsposechallengesforenhancingmodelperformanceandgeneralizability.
BrainFoundationModel. Afoundationmodel(Bommasanietal.,2021)isadeeplearningmodel
trainedonextensivedata,typicallyusingself-supervisionatalargescale,andcanbeadapted,such
asthroughfine-tuning,forvariousdownstreamtasks. Foundationmodels,suchasBERT(Devlin
et al., 2018), MAE (He et al., 2022), CLIP (Radford et al., 2021), GPT-4 (Achiam et al., 2023),
SAM(Kirillovetal.,2023)andSORA(Brooksetal.,2024),haveachievedremarkablesuccessin
computervision,naturallanguage,andmultimodal,butthereisstillavastunexploredpotentialfor
foundationmodelsinbrainsignals. Somestudiesproposetimeseriespre-trainedmodels(Eldele
etal.,2021;Zhangetal.,2022;Wooetal.,2024;Chenetal.,2024;Dengetal.,2024)basedon
contrastivelearningorothersformanyscenarios(e.g.,weather,trafficflow,exchangerates),one
ofwhichisbrainsignals. SomestudieslearnunsupervisedrepresentationsfromEEGbyutilizing
self-supervised learning pretext tasks to uncover the structure of clinical EEG signals (Banville
etal.,2021). BENDER(Kostasetal.,2021)isproposedtoaddresstheproblemoflimitedlabeled
data on EEG by using a contrastive self-supervised learning task to learn generic EEG represen-
tations. MAEEG (Chien et al., 2022) is masked auto-encoder for learning EEG representations
byreconstruction-basedself-supervisedlearning. BrainBERT(Wangetal.,2022)isapre-training
modelforintracranialrecordings,whichlearnsacomplexnon-lineartransformationofneuraldata
byconstructionofthemaskedstereo-electroencephalographic(SEEG)spectrogram. Brant(Zhang
etal.,2023)isafoundationmodelforintracranialneuralsignalswhichattendslong-termdependency
andcapturesspatialcorrelationacrosschannels. Brant-2(Yuanetal.,2024)representsanimproved
versionofBrant,tailoredfortheintegrationofscalpEEGandintracranialEEG.Brant-X(Zhangetal.,
2024)extendsthisframeworktoachievealignmentbetweendifferentphysiologicalsignalsandEEG.
BIOT(Yangetal.,2023)isagenericbiosignallearningmodelwhichenablesjointpre-trainingand
knowledgetransferacrossdifferentbiosignaldatasetsinthewild. EEG2Rep(Foumanietal.,2024)
isaself-predictionapproachforself-supervisedrepresentationlearningfromEEG,whichpredicting
maskedinputsinthelatentrepresentationspace. LaBraM(Jiangetal.,2024)isalargebrainmodel,
whichlearnsEEGgenericrepresentationsbypredictingthecorrespondingneuraltokensofmasked
EEGpatches. EEGPT(Wangetal.,2024a)isapretrainedtransformermodeldesignedforuniversal
EEGfeatureextraction,basedonamask-baseddualself-supervisedlearningmethodforefficient
feature extraction. However, most of existing EEG foundational model the spatial and temporal
dependenciesbetweenallEEGpatchestogether, ignoringtheuniquestructuralcharacteristicsof
18

PublishedasaconferencepaperatICLR2025
EEGsignals. Meanwhile,existingEEGfoundationmodelshavelimitedgeneralizability,performing
wellonlyonalimitedrangeofdownstreamtasks.
| B MORE | DETAILS FOR | EXPERIMENTAL | SETTINGS | ON PRE-TRAINING |
| ------ | ----------- | ------------ | -------- | --------------- |
Here,weintroducemoredetailsforexperimentalsettingsonCBraModpre-training.
Forpreprocessingofpre-trainingdataset,asCBraModadoptscriss-crossEEGmodelingwhichcan
addressEEGsignalswithlongtimedurationwell, wesegmentallEEGrecordingsto30-second
EEGsamples, whichislongerthanthetimedurationofpre-trainingsamplesonexistingstudies
suchasBIOT(Yangetal.,2023)(10seconds)andLaBraM(Jiangetal.,2024)(4or8seconds).
Wechoosethistimedurationfortwomainreasons: 1)longersegmentsmayhelpthemodellearn
morelong-termdependencies,potentiallyimprovingperformanceondownstreamtasks,asnotedin
BENDER(Kostasetal.,2021);2)30secondsgenerallycoversthelengthofEEGsamplesegments
forallthedownstreamtasksinthiswork. MorehyperparametersarelistedinTable5.
|     | Table5: | HyperparametersforCBraModpre-training. |                 |          |
| --- | ------- | -------------------------------------- | --------------- | -------- |
|     |         |                                        | Hyperparameters | Settings |
|     |         |                                        | Channels        | 19       |
|     |         |                                        | Timepoints      | 6000     |
|     |         |                                        | Patchdimension  | 200      |
EEGsample
|     |                         |     | Sequencelength       | 6000/200=30    |
| --- | ----------------------- | --- | -------------------- | -------------- |
|     |                         |     | Maskratio            | 0.5            |
|     |                         |     | Masktoken            | Fullzero       |
|     |                         |     | Inputdimension       | {1,25,25}      |
|     | PatchEncoder            |     | Outputdimension      | {25,25,25}     |
|     | (Time-DomainBranch,     |     | Kernelsize           | {49,3,3}       |
|     | 3-layer1DCNN)           |     | Stride               | {25,1,1}       |
|     |                         |     | Padding              | {24,1,1}       |
|     | PatchEncoder            |     | FFTfunction          | torch.fft.rfft |
|     | (Frequency-DomainBranch |     | Fully-connectedlayer | (101,200)      |
|     |                         |     | Inputdimension       | 200            |
|     | PositionalEncoder       |     | Outputdimension      | 200            |
|     | (1-layer2DDepthwiseCNN) |     | Kernelsize           | (19,7)         |
|     |                         |     | Stride               | (1,1)          |
|     |                         |     | Padding              | (9,3)          |
|     |                         |     | Layers               | 12             |
|     |                         |     | Hiddendimension      | 200            |
|     |                         |     | Heads                | 8              |
Criss-crosstransformer
|                |               |     | S-Attentionheads      | 4                    |
| -------------- | ------------- | --- | --------------------- | -------------------- |
|                |               |     | T-Attentionheads      | 4                    |
|                |               |     | Feed-forwarddimension | 800                  |
|                |               |     | Epochs                | 40                   |
|                |               |     | Batchsize             | 128                  |
|                |               |     | Dropout               | 0.1                  |
|                |               |     | Optimizer             | AdamW                |
|                |               |     | Learningrate          | 5e-4                 |
|                |               |     | Adamβ                 | (0.9,0.999)          |
|                | Pre-training  |     | Adamϵ                 | 1e-8                 |
|                |               |     | Weightdecay           | 5e-2                 |
|                |               |     | Scheduler             | CosineAnnealingLR    |
|                |               |     | Cosinecycleepochs     | 40                   |
|                |               |     | Minimallearningrate   | 1e-5                 |
|                |               |     | Clippinggradientnorm  | 1                    |
|                |               |     | Weightsinit           | Kaimingnormalization |
| C PRE-TRAINING | VISUALIZATION |     |                       |                      |
ThepretraininglosscurveofCBraModispresentedinFigure6. Fromthecurve,itisevidentthat
during the 40-epoch pretraining process, the loss function generally follows a downward trend,
withminorfluctuationsobservedbetweenepochs10and14. Theoveralltrendsuggeststhatour
modeliseffectivelylearningfromthepretrainingdata, leadingtotheextractionofreliableEEG
representations.
19

PublishedasaconferencepaperatICLR2025
0.006
0.005
0.004
0.003
0.002
0 10 20 30 40
Epoch
ssoL
Figure6: Thepre-traininglosscurveofCBraMod.
D MORE DETAILS FOR EXPERIMENTAL SETTINGS ON DOWNSTREAM BCI
TASKS
WeprovidemoredetailsforexperimentsettingsondownstreamBCItasks.
D.1 MOREDETAILSFORDOWNSTREAMTASK
I.EmotionRecognitionreferstodetectingandinterpretingemotionalstatesorpatternsbasedon
EEG.WechooseFACED(Chenetal.,2023)andSEED-V(Liuetal.,2021b)asdownstreamdatasets
forthistask.
II.MotorImageryClassificationisaprocessthatinvolvesdecodingorclassifyingmotorimagery
tasksbasedonbrainactivitypatternscapturedthroughEEG.WeusePhysioNet-MI(Schalketal.,
2004)andSHU-MI(Maetal.,2022)toevaluatetheperformanceofCBraModonthistask.
III.SleepStaging, alsoknownassleepstageclassification, categorizesdifferentstagesofsleep
basedonphysiologicalsignals(e.g. EEG)recordedduringsleep. ISRUC(Khalighietal.,2016)isa
commonlyusedbenchmarkforsleepstaging.
IV.SeizureDetectionreferstotheprocessofidentifyingandrecognizingepilepticseizuresbasedon
physiologicalsignals,suchasEEG.Here,CHB-MIT(Shoeb,2009)ischoosedforthistask.
V.ImaginedSpeechClassificationinvolvestheidentificationandinterpretationofimaginedspeech
orcovertspeechintentionsbasedonbrainactivitypatternssuchasEEG.BCIC2020-3(Jeongetal.,
2022)isadatasetforthistaskon2020internationalbrain–computerinterfacecompetition.
VI.MentalDisorderDiagnosisreferstotheprocessofidentifyingandcategorizingmentalhealth
statesbasedonEEG.Mumtaz2016(Mumtaz,2016)isanEEGdatasetcollectedfrompatientswith
majordepressivedisorderandnormalcontrols.
VII. Vigilance Estimation refers to the assessment and measurement of an individual’s level of
vigilanceorsustainedattentionfromEEG.SEED-VIG(Minetal.,2017)isdatasetusedtoassessthe
levelofvigilance.
VIII.MentalStressDetectioninvolvesusingEEGtoidentifyanindividual’slevelofstress. Menta-
lArithmetic(Zymaetal.,2019)isadatasetcontainingEEGrecordingsofsubjectsbeforeandduring
theperformanceofmentalarithmetictasks.
IX.EEGEventsClassificationinvolvesthecategorizationandidentificationofspecificeventsor
patternsinEEG.WechooseTUEV(Obeid&Picone,2016)forevaluation,whichwasconsistent
withBIOT(Yangetal.,2023)andLaBraM(Jiangetal.,2024).
20

PublishedasaconferencepaperatICLR2025
X.AbnormalDetectionreferstotheprocessofidentifyinganddetectingabnormalpatternsorevents
inEEG.Similarly,TUAB(Obeid&Picone,2016)isusedforevaluation,consistentwithBIOT(Yang
etal.,2023)andLaBraM(Jiangetal.,2024).
D.2 BASELINES
Here,weintroducethedetailsofthebaselinesforperformanceevaluation.
EEGNet(Lawhernetal.,2018)isacompactconvolutionalneuralnetworkbasedondepthwiseand
separableconvolutions.
EEGConformer(Songetal.,2022)isEEGmodelusingCNNtolearnlow-levellocalfeaturesand
self-attentiontoextracttheglobalcorrelationwithinthelocaltemporalfeatures.
SPaRCNet (Jing et al., 2023) is a deep neural network based on 1D CNN with dense residual
connections.
ContraWR(Yangetal.,2021)isaCNNbasedmodel,whichfirsttransformsthebiosignalsinto
multi-channelspectrogramandthenuses2D-CNNbasedResNet(Heetal.,2016)toextractfeatures
fromspectrogram.
CNN-Transformer(Pehetal.,2022)ismodelutilizingCNNtoextractlocalfeaturesandusing
transformertocaptureglobaldependencies.
FFCL(Lietal.,2022)isneuralnetworkcombiningCNNandLSTMinparallel,wheretheCNN
extractsspatialfeaturesandtheLSTMextractstemporalfeatures.
ST-TransformerSongetal.(2021)isatransformerbasednetworkwhichreliesontheattention
mechanismtolearnthespatialandtemporalfeaturesofEEGsignals.
BIOT(Yangetal.,2023)isanEEGfoundationmodelwhichlearnsEEGgenericrepresentations
basedonlineartransformerandsupervised-unsupervised-combinedpre-training. Itisworthnoting
thatthepre-trainedBIOTcanonlyacceptEEGsignalswithamaximumof18channelsasinput.
Therefore,forEEGsignalswithmorethan18channels,wewillusemultipleBIOTmodelstoprocess
differentsetsofchannels.
LaBraM (Jiang et al., 2024) is a large brain model, which learns EEG generic representations
by predicting the corresponding neural tokens of masked EEG patches based on full-attention
transformer.
D.3 METRICS
In this section, we introduce the details of the metrics used in the paper. Consistent with
LaBraM(Jiangetal.,2024),weadoptthefollowingmetrics:
BalancedAccuracyisaperformancemetricthatconsiderstheaccuracyofeachclassinimbalanced
datasets,whichisdefinedastheaverageofrecallobtainedoneachclass. Weuseitforbothbinary
classificationandmulti-classclassification.
AUC-PRisaperformancemetriccalculatingtheareaundertheprecisionrecall(PR)curveforbinary
classificationtask.
AUROCisawidelyusedstatisticcalculatingtheareaunderthereceiveroperatingcharacteristic
(ROC)curve. Weuseitforbinaryclassification.
Coken’sKappaisastatisticalmeasureusedtoassesstheagreementbetweentworatersorclassifiers
incategoricalclassificationtasks,whichisusuallyusedforimbalancedmulti-classclassificationtask.
WeightedF1isaweightedaverageofindividualF1-scoresfromeachclass,witheachscoreweighted
bythenumberofsamplesinthecorrespondingclass,whichprovidesareliablemeasureinmulti-class
classificationtasks.
Pearson’scorrelationisastatisticalmeasurethatquantifiesthelinearrelationshipbetweentwo
continuousvariables,whichcanbeusedtoquantifytheperformanceofaregressionmodel.
21

PublishedasaconferencepaperatICLR2025
R2score,alsoknownasthecoefficientofdetermination,isastatisticalmeasurecommonlyusedto
evaluatethegoodnessoffitofaregressionmodel.
RMSE(RootMeanSquareError)isacommonlyusedperformancemetricinregressiontasksto
measuretheaveragemagnitudeoftheerrorsmadebyaregressionmodel,whichcalculatesthesquare
rootoftheaverageofthesquareddifferencesbetweenthepredictedvaluesandthetruevalues.
D.4 FINE-TUNING
|     |                                           | Table6: HyperparametersforCBraModfine-tuning. |                   |     |
| --- | ----------------------------------------- | --------------------------------------------- | ----------------- | --- |
|     | Hyperparameters                           |                                               | Settings          |     |
|     | Epochs                                    |                                               | 50                |     |
|     | Batchsize                                 |                                               | 64                |     |
|     | Dropout                                   |                                               | 0.1               |     |
|     | Optimizer                                 |                                               | AdamW             |     |
|     | Learningrate                              |                                               | 1e-4              |     |
|     | Adamβ                                     |                                               | (0.9,0.999)       |     |
|     | Adamϵ                                     |                                               | 1e-8              |     |
|     | Weightdecay                               |                                               | 5e-2              |     |
|     | Scheduler                                 |                                               | CosineAnnealingLR |     |
|     | Cosinecycleepochs                         |                                               | 50                |     |
|     | Minimallearningrate                       |                                               | 1e-6              |     |
|     | Clippinggradientnorm                      |                                               | 1                 |     |
|     | Labelsmoothing(multi-classclassification) |                                               | 0.1               |     |
Weloadthepre-trainedweightsofCBraModandreplacethereconstructionheadwithatask-specific
head which is composed of multi-layer perceptrons. Here the learned EEG representations are
flattenedandfedintothetask-specificheadfordownstreamtasks. Thenwefine-tuneCBraModin
downstreamdatasets. Weemploybinarycross-entropy(BCE)lossforbinaryclassification,cross-
entropylossformulti-classclassification,andmean-square-errorlossfunctionforregression.
MorehyperparametersforCBraModfine-tuningondownstreamdatasetsareshowninTable6.
| E MORE | RESULTS | ON OTHER DOWNSTEAM | BCI TASKS |     |
| ------ | ------- | ------------------ | --------- | --- |
Inthissection,wereportmoreresultsofCBraModandbaselinesonotherdownstreamBCItasks.
E.1 SLEEPSTAGING
Table7: Theresultsofdifferentmethodsonsleepstaging(ISRUC,5-class).
| Methods      |     | Params BalancedAccuracy | Cohen’sKappa  | WeightedF1    |
| ------------ | --- | ----------------------- | ------------- | ------------- |
| EEGNet       |     | 0.003M 0.7154±0.0121    | 0.7040±0.0173 | 0.7513±0.0124 |
| EEGConformer |     | 0.55M 0.7400±0.0133     | 0.7143±0.0162 | 0.7634±0.0151 |
| SPaRCNet     |     | 0.79M 0.7487±0.0075     | 0.7097±0.0132 | 0.7624±0.0092 |
| ContraWR     |     | 1.6M 0.7402±0.0126      | 0.7178±0.0156 | 0.7610±0.0137 |
CNN-Transformer 3.2M 0.7363±0.0087 0.7129±0.0121 0.7719±0.0105
| FFCL |     | 2.4M 0.7277±0.0182 | 0.7016±0.0291 | 0.7614±0.0197 |
| ---- | --- | ------------------ | ------------- | ------------- |
ST-Transformer 3.5M 0.7381±0.0205 0.7013±0.0352 0.7681±0.0175
| DeepSleepNet |     | 21M 0.7419±0.0144  | 0.7036±0.0241 | 0.7643±0.0122 |
| ------------ | --- | ------------------ | ------------- | ------------- |
| USleep       |     | 1.1M 0.7586±0.0116 | 0.7209±0.0143 | 0.7805±0.0105 |
| BIOT         |     | 3.2M 0.7527±0.0121 | 0.7192±0.0231 | 0.7790±0.0146 |
| LaBraM-Base  |     | 5.8M 0.7633±0.0102 | 0.7231±0.0182 | 0.7810±0.0133 |
| CBraMod      |     | 4.0M 0.7865±0.0110 | 0.7442±0.0152 | 0.8011±0.0099 |
ISRUC(Khalighietal.,2016)isasleepdataset,whichcomprises100all-nightPSGrecordingsof
100adults. Inourexperiments,weusedPSGrecordingsinSub-group1toevaluateourmethod. The
22

PublishedasaconferencepaperatICLR2025
EEGsignalsofISRUCarecollectedwith6channels(F3-A2,C3-A2,O1-A2,F4-A1,C4-A1,O2-A1)
and200Hzsamplingrate. AllEEGsignalsaresegmentedinto89,24030-secondsamples,whichare
classifiedintofivedifferentsleepstages(Wake,N1,N2,N3,REM)bysleepexpertsaccordingtothe
AmericanAcademyofSleepMedicine(AASM)sleepstandard(Iberetal.,2007). Inourexperiment,
wesetsubject1to80astrainingset,subject81to90asvalidationsetandsubject91to100astestset.
Notably,accordingtoAASMstandard(Iberetal.,2007),expertsusuallyidentifythecurrentstage
basedonthetransitionpatterns,combiningthesleepstagesofothersamplesinasleepsequence
together. Thetransitionpatternsofsleepstagesbetweenepochsplayacriticalroleinautomaticsleep
staging. Existingworksonsleepstaging(Phan&Mikkelsen,2022)usuallyregardsleepstaging
asasequence-to-sequenceclassificationtaskandset20asthesequencelength, whereonesleep
sequencehas2030-secondsamples. Therefore,inexperimentonsleepstaging,weseteachcompared
modelassampleencoder,anduseaone-layertransformerassequenceencoder. Specifically,we
includedtwowidelyrecognizedbaselineinthefieldofsleepstaging,DeepSleepNet(Suprataketal.,
2017)andUSleep(Perslevetal.,2021), tocomparetheperformanceofourmethodwiththatof
classicalgorithmsinthefield. AsshowninTable7,CBraModoutperformsallbaselines. Specifically,
CBraModobtainsignificantlybetterperformancecomparedtoexistingbestmethodLaBraM(0.7442
v.s. 0.7231inCohen’sKappa).
E.2 SEIZUREDETECTION
Table8: Theresultsofdifferentmethodsonseizuredetection(CHB-MIT,2-class).
Methods Params BalancedAccuracy AUC-PR AUROC
EEGNet 0.003M 0.5658±0.0106 0.1914±0.0182 0.8048±0.0136
EEGConformer 0.55M 0.5976±0.0141 0.2209±0.0215 0.8226±0.0170
SPaRCNet 0.79M 0.5876±0.0191 0.1247±0.0119 0.8143±0.0148
ContraWR 1.6M 0.6344±0.0002 0.2264±0.0174 0.8097±0.0114
CNN-Transformer 3.2M 0.6389±0.0067 0.2479±0.0227 0.8662±0.0082
FFCL 2.4M 0.6262±0.0104 0.2049±0.0346 0.8271±0.0051
ST-Transformer 3.5M 0.5915±0.0195 0.1422±0.0094 0.8237±0.0491
BIOT 3.2M 0.7068±0.0457 0.3277±0.0460 0.8761±0.0284
LaBraM-Base 5.8M 0.7075±0.0358 0.3287±0.0402 0.8679±0.0199
CBraMod 4.0M 0.7398±0.0284 0.3689±0.0382 0.8892±0.0154
CHB-MIT(Goldbergeretal.,2000;Shoeb,2009)isadatabase,collectedattheChildren’sHospital
Boston,consistingofEEGrecordingsfrom23pediatricsubjectswithintractableseizures. Subjects
weremonitoredforuptoseveraldaysfollowingwithdrawalofanti-seizuremedicationinorderto
characterizetheirseizuresandassesstheircandidacyforsurgicalintervention. AllEEGsignalsare
collectedbasedontheinternational10-20systemofEEGelectrodepositionsandaresampledat
256Hz,withbinaryclasses(seizureornot). Inourexperiment,wepreprocesstheEEGsignalsof
CHB-MIT based on the strategy consistent with BIOT (Yang et al., 2023). We use the common
16bipolarmontagechannelsforCHB-MITdataset. AllEEGsignalsareresampledto200Hzand
divided326,99310-secondsamples. Weusesubject1to19fortraining,subject20,21forvalidation,
andsubject22,23fortest. TheresultsofseizuredetectionareshowninTable8. CBraModachieves
thestate-of-the-artperformance.
E.3 IMAGINEDSPEECHCLASSIFICATION
BCIC2020-3(Jeongetal.,2022)isadatasetforimaginedspeechclassificationon2020international
brain–computer interface competition. During the data collection experiment, 15 subjects were
seatedinacomfortablechairinfrontofa24-inchLCDmonitorscreen. Thesubjectswereinstructed
to imagine the silent pronunciation of the given word as if they were performing real speech,
withoutmovinganyarticulatorsnormakingthesound. EEGsignalsoffive-classimaginedspeech
words/phrases(“hello”,“helpme”,“stop”,“thankyou”and“yes”)wererecordedat64channels
and256Hzsamplingrate. Training,validationandtestsetareprovidedbythedataset. Specifically,
60trialsperclassarereleasedfortrainingpurpose, 10trialsperclassarereleasedforvalidation
purposeand10trialsperclassarereleasedfortestpurpose. Thesumoftrialsis80×5×15=6000.
23

PublishedasaconferencepaperatICLR2025
Table9: Theresultsofdifferentmethodsonimaginedspeechclassification(BCIC2020-3,5-class).
| Methods      | Params BalancedAccuracy | Cohen’sKappa  | WeightedF1    |
| ------------ | ----------------------- | ------------- | ------------- |
| EEGNet       | 0.003M 0.4413±0.0096    | 0.3016±0.0123 | 0.4413±0.0102 |
| EEGConformer | 0.55M 0.4506±0.0133     | 0.3133±0.0183 | 0.4488±0.0154 |
| SPaRCNet     | 0.79M 0.4426±0.0156     | 0.3033±0.0233 | 0.4420±0.0108 |
| ContraWR     | 1.6M 0.4257±0.0162      | 0.3078±0.0218 | 0.4407±0.0182 |
CNN-Transformer 3.2M 0.4533±0.0092 0.3166±0.0118 0.4506±0.0127
| FFCL | 2.4M 0.4678±0.0197 | 0.3301±0.0359 | 0.4689±0.0205 |
| ---- | ------------------ | ------------- | ------------- |
ST-Transformer 3.5M 0.4126±0.0122 0.2941±0.0159 0.4247±0.0138
| BIOT        | 3.2M 0.4920±0.0086 | 0.3650±0.0176 | 0.4917±0.0079 |
| ----------- | ------------------ | ------------- | ------------- |
| LaBraM-Base | 5.8M 0.5060±0.0155 | 0.3800±0.0242 | 0.5054±0.0205 |
| CBraMod     | 4.0M 0.5373±0.0108 | 0.4216±0.0163 | 0.5383±0.0096 |
Onetrialisa3-secondEEGsignal,whichisregardasonesample. Thusweget6,00064-channel
3-secondEEGsamples,whichareresampledto200Hz. Theexperimentalresultsofimaginedspeech
classificationareshowninTable9. CBraModachievesagreatperformanceincreasescomparedto
thebestbaselineLaBraM(0.4216v.s. 0.3800inCohen’sKappa).
E.4 MENTALDISORDERDIAGNOSIS
Table10: Theresultsofdifferentmethodsonmentaldisorderdiagnosis(Mumtaz2016,2-class).
| Methods      | Params BalancedAccuracy | AUC-PR        | AUROC         |
| ------------ | ----------------------- | ------------- | ------------- |
| EEGNet       | 0.003M 0.9232±0.0104    | 0.9626±0.0095 | 0.9639±0.0093 |
| EEGConformer | 0.55M 0.9308±0.0117     | 0.9684±0.0105 | 0.9702±0.0101 |
| SPaRCNet     | 0.79M 0.9316±0.0095     | 0.9754±0.0065 | 0.9781±0.0083 |
| ContraWR     | 1.6M 0.9195±0.0115      | 0.9589±0.0102 | 0.9621±0.0092 |
CNN-Transformer 3.2M 0.9305±0.0068 0.9757±0.0074 0.9742±0.0059
| FFCL | 2.4M 0.9314±0.0038 | 0.9717±0.0021 | 0.9753±0.0033 |
| ---- | ------------------ | ------------- | ------------- |
ST-Transformer 3.5M 0.9135±0.0103 0.9578±0.0086 0.9594±0.0059
| BIOT        | 3.2M 0.9358±0.0052 | 0.9736±0.0034 | 0.9758±0.0042 |
| ----------- | ------------------ | ------------- | ------------- |
| LaBraM-Base | 5.8M 0.9409±0.0079 | 0.9798±0.0093 | 0.9782±0.0057 |
| CBraMod     | 4.0M 0.9560±0.0056 | 0.9923±0.0032 | 0.9921±0.0025 |
Mumtaz2016(Mumtaz,2016)isanEEGdatasetcollectedfrom34patientswithmajordepressive
disorder(MDD)and30normalcontrols(NCs). AllEEGsignalsrecordedfrom19electrodesplaced
according to the international 10-20 system. The sampling rate is 256 Hz. The data collection
experimentcomprisesthreesessionsincludingeyes-opensession,eyes-closssessionandtasksession.
Inourexperiment,weonlyuseeyes-openandeyes-closesessions. 24MDDpatientsand19NCs
areusedfortraining,5MDDpatientsand4NCsareusedforvalidation,and5MDDpatientsand
5NCsareusedfortest. EEGsignalsareband-passfiltered(0.3Hz–75Hz)toremovelowandhigh
frequencynoise,notchfiltered(50Hz)toremovepowerlinenoiseandresampledto200Hz. Then
wesegmentallEEGsignalsinto7,1435-secondsamples. AsshowninTable10,CBraModachieve
thestate-of-the-artperformance. Specifically,CBraModperforms1.4%bettercomparedtothebest
baselineLaBraM(0.9560v.s.0.9409inbalancedaccuracy,0.9923v.s.0.9798inAUC-PRand0.9921
v.s. 0.9782inAUROC).
E.5 VIGILANCEESTIMATION
SEED-VIG(Minetal.,2017)isdatasetorientedatexploringthevigilanceestimationproblem. In
thedatacollectionexperiment,theresearchersbuiltavirtualdrivingsystem,inwhichanenormous
screen is placed in front of a real car. Subjects can play a driving game in the car, as if they are
drivinginthereal-worldenvironment. TheSEED-VIGdatasetiscollectedwhenthesubjectsdrive
inthesystem. ThevigilancelevelislabeledwiththePERCLOSindicatorbytheSMIeye-tracking
glasses. AllEEGsignalsarerecordedfrom23subjectsat17channelsand200Hzsamplingrate,and
24

PublishedasaconferencepaperatICLR2025
Table11: Theresultsofdifferentmethodsonvigilanceestimation(SEED-VIG,regression).
| Methods      | Params | Pearson’sCorrelation | R2Score       | RMSE↓         |
| ------------ | ------ | -------------------- | ------------- | ------------- |
| EEGNet       | 0.003M | 0.5701±0.0167        | 0.2366±0.0084 | 0.2828±0.0074 |
| EEGConformer | 0.55M  | 0.5750±0.0139        | 0.2344±0.0091 | 0.2850±0.0083 |
| SPaRCNet     | 0.79M  | 0.5715±0.0163        | 0.2433±0.0055 | 0.2798±0.0043 |
| ContraWR     | 1.6M   | 0.5854±0.0142        | 0.2453±0.0062 | 0.2782±0.0056 |
CNN-Transformer 3.2M 0.5714±0.0172 0.2371±0.0052 0.2805±0.0039
| FFCL | 2.4M | 0.5647±0.0097 | 0.2301±0.0035 | 0.2914±0.0052 |
| ---- | ---- | ------------- | ------------- | ------------- |
ST-Transformer 3.5M 0.5752±0.0127 0.2366±0.0071 0.2838±0.0036
| BIOT        | 3.2M | 0.5996±0.0182 | 0.2543±0.0073 | 0.2742±0.0029 |
| ----------- | ---- | ------------- | ------------- | ------------- |
| LaBraM-Base | 5.8M | 0.5931±0.0098 | 0.2432±0.0085 | 0.2762±0.0048 |
| CBraMod     | 4.0M | 0.6459±0.0098 | 0.3365±0.0068 | 0.2587±0.0039 |
aresegmentedinto20,3558-secondsamples. Inourexperiment,weusesubject1to15fortraining,
subject 16 to 19 for validation and subject 20 to 23 for test. The experiment results of vigilance
estimationarepresentedinTable11. Obviously,CBraModobtainsagreatperformanceincreases
comparedtothebestbaselineBIOT(0.5996v.s. 0.6459inPearson’scorrelation,0.3365v.s. 0.2543
| inR2scoreand0.2587v.s. | 0.2742inRMSE). |     |     |     |
| ---------------------- | -------------- | --- | --- | --- |
E.6 MENTALSTRESSDETECTION
Table12: Theresultsofdifferentmethodsonmentalstressdetection(MentalArithmetic,2-class).
| Methods      | Params | BalancedAccuracy | AUC-PR        | AUROC         |
| ------------ | ------ | ---------------- | ------------- | ------------- |
| EEGNet       | 0.003M | 0.6770±0.0116    | 0.5763±0.0102 | 0.7321±0.0108 |
| EEGConformer | 0.55M  | 0.6805±0.0123    | 0.5829±0.0134 | 0.7424±0.0128 |
| SPaRCNet     | 0.79M  | 0.6879±0.0107    | 0.5825±0.0193 | 0.7418±0.0132 |
| ContraWR     | 1.6M   | 0.6631±0.0097    | 0.5787±0.0164 | 0.7332±0.0082 |
CNN-Transformer 3.2M 0.6779±0.0268 0.5777±0.0285 0.7258±0.0336
| FFCL | 2.4M | 0.6798±0.0142 | 0.5786±0.0266 | 0.7330±0.0198 |
| ---- | ---- | ------------- | ------------- | ------------- |
ST-Transformer 3.5M 0.6631±0.0173 0.5672±0.0259 0.7132±0.0174
| BIOT        | 3.2M | 0.6875±0.0186 | 0.6004±0.0195 | 0.7536±0.0144 |
| ----------- | ---- | ------------- | ------------- | ------------- |
| LaBraM-Base | 5.8M | 0.6909±0.0125 | 0.5999±0.0155 | 0.7721±0.0093 |
| CBraMod     | 4.0M | 0.7256±0.0132 | 0.6267±0.0099 | 0.7905±0.0073 |
MentalArithmetic(Goldbergeretal.,2000;Zymaetal.,2019)isadatasetcontainingEEGrecordings
of36subjectsbeforeandduringtheperformanceofmentalarithmetictasks. EEGrecordingsbefore
mental arithmetic tasks are classified into the label of “without mental stress” and ones during
mental arithmetic tasks are classified into the label of “with mental stress”. All EEG signals are
recordedfrom20electrodesplacedaccordingtotheinternational10-20systemat500Hzsampling
rate. Band-passfiltering(0.5Hz–45Hz)areusedtoremovelowandhighfrequencynoise. Inour
experiment,weresampleEEGsignalsto200Hzandsegmenttheminto1,7075-secondsamples.
Subject 1 to 28 are set to training set, subject 29 to 32 are set to validation set and subject 33 to
36aresettotestset. AsshowninTable12, CBraModachievesthestate-of-the-artperformance.
Specifically,CBraModperforms2.5%bettercomparedtothebestbaselinesLaBraM(0.7256v.s.
0.6909inbalancedaccuracy,0.6267v.s. 0.5999inAUC-PRand0.7905v.s. 0.7721inAUROC).
E.7 EVENTTYPECLASSIFICATION
TUEV(Obeid&Picone,2016)isEEGcorpusthatcontainsannotationsofEEGsegmentsasone
ofsixclasses: (1)spikeandsharpwave(SPSW),(2)generalizedperiodicepileptiformdischarges
(GPED),(3)periodiclateralizedepileptiformdischarges(PLED),(4)eyemovement(EYEM),(5)
artifact(ARTF)and(6)background(BCKG),whichisusuallyusedbyexistingstudies(Yangetal.,
2023;Jiangetal.,2024). TheEEGsignalsarerecordedat23channelsand250Hzsamplingrate. For
faircomparisonwithreportedresultsbyBIOT(Yangetal.,2023)andLaBraM(Jiangetal.,2024),
25

PublishedasaconferencepaperatICLR2025
Table13: Theresultsofdifferentmethodsoneventtypeclassification(TUEV,6-class).
| Methods      | Params BalancedAccuracy | Cohen’sKappa  | WeightedF1    |
| ------------ | ----------------------- | ------------- | ------------- |
| EEGNet       | 0.003M 0.3876±0.0143    | 0.3577±0.0155 | 0.6539±0.0120 |
| EEGConformer | 0.55M 0.4074±0.0164     | 0.3967±0.0195 | 0.6983±0.0152 |
| SPaRCNet     | 0.79M 0.4161±0.0262     | 0.4233±0.0181 | 0.7024±0.0104 |
| ContraWR     | 1.6M 0.4384±0.0349      | 0.3912±0.0237 | 0.6893±0.0136 |
CNN-Transformer 3.2M 0.4087±0.0161 0.3815±0.0134 0.6854±0.0293
| FFCL | 2.4M 0.3979±0.0104 | 0.3732±0.0188 | 0.6783±0.0120 |
| ---- | ------------------ | ------------- | ------------- |
ST-Transformer 3.5M 0.3984±0.0228 0.3765±0.0306 0.6823±0.0190
| BIOT         | 3.2M 0.5281±0.0225 | 0.5273±0.0249 | 0.7492±0.0082 |
| ------------ | ------------------ | ------------- | ------------- |
| LaBraM-Base  | 5.8M 0.6409±0.0065 | 0.6637±0.0093 | 0.8312±0.0052 |
| LaBraM-Large | 46M 0.6581±0.0156  | 0.6622±0.0136 | 0.8315±0.0040 |
| LaBraM-Huge  | 369M 0.6616±0.0170 | 0.6745±0.0195 | 0.8329±0.0086 |
CBraMod(excludingTUEV) 4.0M 0.6659±0.0124 0.6744±0.0121 0.8331±0.0071
| CBraMod | 4.0M 0.6671±0.0107 | 0.6772±0.0096 | 0.8342±0.0064 |
| ------- | ------------------ | ------------- | ------------- |
we adopt a similar preprocessing strategy as theirs. Specifically, we use the common 16 bipolar
montagechannelsintheinternational10-20systemforTUEV.Aband-passfiltered(0.3Hz–75Hz)
wasappliedtoremovethelow-frequencyandhigh-frequencynoise. Anotchfilter(60Hz)wasused
toremovethepowerlinenoise. AllEEGsignalsareresampledto200Hzanddividedinto112,491
5-secondsamples. Theoriginaldatasetprovidethetrainingandtestsplits. Wefurtherdividethe
trainingsubjectsintotrainingandvalidationsetby80%:20%,consistentwithBIOT.Giventhatthe
TUEVdatasetisasubsetofthepretrainingdatasetTUEG,weintroducedanadditionalexperimental
setup, CBraMod (excluding TUEV), to eliminate potential effects of data leakage. In this setup,
weexcludedTUEVfromthepretrainingprocess,re-pretrainedanewinstanceofCBraMod,and
subsequentlyevaluateditonTUEV.Theexperimentalresultsofeventtypeclassificationareshown
in Table 13. LaBraM-Huge achieves good performance with such a large number of parameters
(369M),butCBraModstillperformsslightlybettercomparedtoit(0.6671v.s. 0.6616inbalanced
accuracy,0.6772v.s. 0.6745inCohen’sKappaand0.8342v.s. 0.8329inweightedF1). CBraMod
(excludingTUEV)exhibitsslightfluctuationscomparedtoCBraMod,yetitremainscompetitive.
ThisindicatesthatourmethodsuccessfullylearnsagenericEEGrepresentationthroughpre-training,
therebyenhancingtheperformanceondatasetsunseenduringpre-training.
E.8 ABNORMALDETECTION
Table14: Theresultsofdifferentmethodsonabnormaldetection(TUAB,2-class).
| Methods         | Params BalancedAccuracy | AUC-PR        | AUROC         |
| --------------- | ----------------------- | ------------- | ------------- |
| EEGNet          | 0.003M 0.7642±0.0036    | 0.8299±0.0043 | 0.8412±0.0031 |
| EEGConformer    | 0.55M 0.7758±0.0049     | 0.8427±0.0054 | 0.8445±0.0038 |
| SPaRCNet        | 0.79M 0.7896±0.0018     | 0.8414±0.0018 | 0.8676±0.0012 |
| ContraWR        | 1.6M 0.7746±0.0041      | 0.8421±0.0104 | 0.8456±0.0074 |
|                 | 0.7777±0.0022           | 0.8433±0.0039 | 0.8461±0.0013 |
| CNN-Transformer | 3.2M                    |               |               |
|                 | 0.7848±0.0038           | 0.8448±0.0065 | 0.8569±0.0051 |
| FFCL            | 2.4M                    |               |               |
|                 | 0.7966±0.0023           | 0.8521±0.0026 | 0.8707±0.0019 |
| ST-Transformer  | 3.5M                    |               |               |
|                 | 0.7959±0.0057           | 0.8792±0.0023 | 0.8815±0.0043 |
| BIOT            | 3.2M                    |               |               |
|                 | 0.8140±0.0019           | 0.8965±0.0016 | 0.9022±0.0009 |
| LaBraM-Base     | 5.8M                    |               |               |
| LaBraM-Large    | 46M 0.8226±0.0015       | 0.9130±0.0005 | 0.9127±0.0005 |
| LaBraM-Huge     | 369M 0.8258±0.0011      | 0.9204±0.0011 | 0.9162±0.0016 |
CBraMod(excludingTUAB) 4.0M 0.8249±0.0025 0.9221±0.0015 0.9156±0.0017
| CBraMod | 4.0M 0.8289±0.0022 | 0.9258±0.0008 | 0.9227±0.0011 |
| ------- | ------------------ | ------------- | ------------- |
We use TUAB (Obeid & Picone, 2016) for evaluation on abnormal detection consistent with
BIOT (Yang et al., 2023) and LaBraM (Jiang et al., 2024). TUAB is an EEG corpus that have
beenannotatedasnormalorabnormal. SimilartoTUEV,theEEGsignalsofTUABarerecorded
at23channelsand250Hzsamplingrate. Forfaircomparison,wealsoadoptasimilarpreprocess-
26

PublishedasaconferencepaperatICLR2025
ingstrategyasBIOTandLaBraM.Thecommon16bipolarmontagechannelsintheinternational
10-20 system are used for TUAB. We utilize a band-pass filtered (0.3 Hz–75 Hz) to remove the
low-frequencyandhigh-frequencynoise,anduseanotchfilter(60Hz)toremovethepowerline
noise. ThenallEEGsignalsareresampledto200Hzanddividedinto409,45510-secondsamples,
whichareusedforbinaryclassificationtopredictnormal/abnormal. Theoriginaldatasetprovidethe
trainingandtestsplits. BesameasBIOT,wefurtherdividethetrainingsubjectsintotrainingand
validationsetby80%:20%. ConsideringthattheTUABdatasetisasubsetofthepretrainingdataset
TUEG,weimplementedanadditionalexperimentalsetup,CBraMod(excludingTUAB),tomitigate
potentialdataleakageeffects. Inthissetup,TUABwasexcludedfromthepre-trainingprocess,a
newinstanceofCBraModwasre-pretrained,anditsperformancewassubsequentlyevaluatedon
TUAB.AsshowninTable14,CBraModachievesthestate-of-the-artperformance,obtainingslightly
betterresultscomparedtoLaBraM-Huge. CBraMod(excludingTUAB)exhibitsslightfluctuations
comparedtoCBraModbutremainscompetitive,demonstratingitscapabilitytolearngenericEEG
representationsthatenhanceperformanceondatasetsnotencounteredduringpre-training.
E.9 MOTORIMAGERYCLASSIFICATION
Table15: Theresultsofdifferentmethodsonmotorimageryclassification(BCIC-IV-2a,4-class).
Methods Params BalancedAccuracy Cohen’sKappa WeightedF1
EEGNet 0.003M 0.4482±0.0094 0.2693±0.0121 0.4226±0.0108
EEGConformer 0.55M 0.4696±0.0106 0.2924±0.0141 0.4533±0.0128
SPaRCNet 0.79M 0.4635±0.0117 0.2847±0.0147 0.4432±0.0126
ContraWR 1.6M 0.4678±0.0125 0.2905±0.0160 0.4413±0.0142
CNN-Transformer 3.2M 0.4600±0.0108 0.2800±0.0148 0.4460±0.0114
FFCL 2.4M 0.4470±0.0143 0.2627±0.0176 0.4238±0.0139
ST-Transformer 3.5M 0.4575±0.0145 0.2733±0.0198 0.4471±0.0142
BIOT 3.2M 0.4748±0.0093 0.2997±0.0139 0.4607±0.0125
LaBraM-Base 5.8M 0.4869±0.0085 0.3159±0.0154 0.4758±0.0103
CBraMod 4.0M 0.5138±0.0066 0.3518±0.0094 0.4984±0.0085
TofurthervalidatetheperformanceofCBraModonthemotorimagerytasks,weconductedadditional
experimentsontheBCIC-IV-2a(Brunneretal.,2008)dataset2. TheBCICompetitionIVDataset2a,
providedbyGrazUniversityofTechnology,comprisesEEGrecordingsfrom9subjectsperforming4
motorimagerytasks: imaginingmovementsofthelefthand,righthand,bothfeet,andtongue. Data
werecollectedovertwosessionsonseparatedaysusing22Ag/AgClelectrodesatasamplingrateof
250Hz. Eachsessionconsistedof288EEGtrials,with72trialspertask. Weused[2,6]seconds
ofeachtrial. Aband-passfiltered(0.3Hz–40Hz)wasappliedtoremovethelow-frequencyand
high-frequencynoise. WeresampletheEEGsignalsto200Hzandobtain5,0884-secondsamples.
Weuseastrictsubject-indenpendenttrain/validation/teststrategyasotherMIdatasetsinourpaper.
Subject1-5,6-7,8-9areusedfortraining,validation,andtest,respectively. Theresultsareshownin
Table15. CBraModcontinuestooutperformexistingmethodsonthisdataset,furtherreinforcingthe
generalizabilityofourmethod.
AlltheresultsacrosssuchwiderangeofdownstreamBCItasksindicatethatCBraModcanlearn
genericEEGrepresentations,whichcontributestoitsstrongcapabilityandgeneralizability.
F SCALING DATA SIZE AND MODEL SIZE
Given the positioning of this work as a foundational model, we conduct experiments to explore
whetherscalinglawsholdatboththedatascaleandmodelsizelevels. Specifically,inthedatascale
experiments,weexaminehowtheperformanceofCBraModvarieswithdifferentpretrainingdata
sizes,rangingfrom1hourto9000hours. Forthemodelsizeexperiments,wedesignmultiplevariants
2Asthereviewersuggested,wehaveaddedanadditionalcomparisonexperimentusingtheBCIC-IV-2a
dataset.Forthesakeofnarrativeclarity,wedidnotincludethisdatasetinthecountofthe12publiclyavailable
downstreamdatasetspresentedinthemaintext.Includingthisdataset,wehaveactuallyevaluatedatotalof13
downstreamdatasets.
27

PublishedasaconferencepaperatICLR2025
|     |      |     | FACED (9-class) |     |     |      |     | FACED (9-class) |     |
| --- | ---- | --- | --------------- | --- | --- | ---- | --- | --------------- | --- |
|     | 0.52 |     |                 |     |     | 0.52 |     |                 |     |
|     | 0.51 |     |                 |     |     | 0.50 |     |                 |     |
0.50
0.48
0.49
| appaK s'nehoC |     |     |     |     |     | appaK s'nehoC 0.46 |     |     |     |
| ------------- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- |
0.48
0.44
|     | 0.47 |     |          |      |           | 0.42    |     |            |       |
| --- | ---- | --- | -------- | ---- | --------- | ------- | --- | ---------- | ----- |
|     | 0.46 |     |          |      |           | 0.40    |     |            |       |
|     | 0.45 |     |          |      |           | 0.38    |     |            |       |
|     | 0.44 |     |          |      |           | 0.36    |     |            |       |
|     | 1 10 | 100 | 500 1000 | 2000 | 5000 9000 | 0.1 0.4 | 0.8 | 1.2 1.5    | 2 3 4 |
|     |      |     | Time (h) |      |           |         |     | Params (M) |       |
(a)Performancecomparisonasthepre-trainingdataincreases. (b)Performancecomparisonasthemodelsizeincreases.
|     |     |     | Figure7: | ScalingDataSizeandModelSize. |     |     |     |     |     |
| --- | --- | --- | -------- | ---------------------------- | --- | --- | --- | --- | --- |
ofCBraModwithvaryingmodelsizes(0.1Mto4Mparameters)andevaluatetheirperformanceon
downstreamtasks. TheresultsoftheseexperimentsarepresentedinTable7. AsshowninTable7(a),
theperformanceofCBraModimprovesasthescaleofpretrainingdataincreases,althoughtherate
of improvement slows beyond 1000 hours. Similarly, Table 7(b) demonstrates that larger model
sizesleadtobetterperformanceindownstreamtasks. Nevertheless,the9000-hourpretrainingdata
and 4M model size explored in this study do not represent the upper bounds of scaling laws. In
thedomainoflargelanguagemodels, bothdatascaleandmodelsizehavealreadysurpassedthe
billion-levelthreshold. Whilecomputationalconstraintshavelimitedourexplorationtothisrange,
priorstudies(Jiangetal.,2024)onscalinglawssuggestthatlargermodelsizescouldfurtherimprove
performanceinEEGdownstreamtasks.
| G   | ARCHITECTURE |     | COMPARISON |                | ON         | OUR PRE-TRAINING |     | DATASETS     |     |
| --- | ------------ | --- | ---------- | -------------- | ---------- | ---------------- | --- | ------------ | --- |
|     |              |     | CBraMod    | BIOT(original) | BIOT(ours) | LaBraM(original) |     | LaBraM(ours) |     |
ycaruccA decnalaB 0.60 appaK s'nehoC 0.60 ycaruccA decnalaB 0.45 appaK s'nehoC 0.30 0.45
|     |      |     |     | 1F dethgieW |     |      |      |     | 1F dethgieW |
| --- | ---- | --- | --- | ----------- | --- | ---- | ---- | --- | ----------- |
|     | 0.55 | 0.5 |     |             |     |      | 0.25 |     |             |
|     |      |     |     | 0.55        |     | 0.40 |      |     | 0.40        |
|     | 0.50 |     |     |             |     |      | 0.20 |     |             |
0.45 FACED, 9-class 0.4 FACED, 9-class 0.50 FACED, 9-class 0.35 SEED-V, 5-class 0.15 SEED-V, 5-class 0.35 SEED-V, 5-class
| ycaruccA decnalaB | 0.70 | 0.55 |     | 0.70 |     | ycaruccA decnalaB 0.70 | 0.75 |     |     |
| ----------------- | ---- | ---- | --- | ---- | --- | ---------------------- | ---- | --- | --- |
appaK s'nehoC
|     |      |      |     | 1F dethgieW |     |      | RP-CUA |     |           |
| --- | ---- | ---- | --- | ----------- | --- | ---- | ------ | --- | --------- |
|     | 0.65 |      |     | 0.65        |     | 0.65 |        |     | CORUA 0.7 |
|     |      | 0.50 |     |             |     |      | 0.70   |     |           |
|     | 0.60 |      |     | 0.60        |     | 0.60 |        |     |           |
0.55 PhysioNet-MI, 4-class 0.45 PhysioNet-MI, 4-class 0.55 PhysioNet-MI, 4-class 0.55 SHU-MI, 2-class 0.65 SHU-MI, 2-class 0.6 SHU-MI, 2-class
Figure8: PerformancecomparisonwitharchitecturesofexistingEEGfoundationmodelsonour
pre-trainingdatasets.
Inthispaper,weusedifferentmodelarchitectureandpre-trainingdatasetcomparedtoBIOT(Yang
etal.,2023)andLaBraM(Jiangetal.,2024). Tofurtherevaluatewhetherthemodelarchitectureor
thepre-trainingdatasetcontributesmoretoperformanceimprovement,weconductacomparison
experiment. Specifically,wepre-trainedthearchitectureofBIOTandLaBraMonourpre-training
datasetwiththesamesettingsasCBraMod,andcomparedtheperformancewithBIOT(original),
LaBraM(original)andCBraModondownstreamdatasets. Theexperimentalresultsareshownin
Figure8.
BIOT(ours)andBIOT(original)exhibitverysimilarperformance. LaBraM(ours)generallyachieves
slightlybetterperformancethanLaBraM(original),particularlyontheFACEDdataset.ButCBraMod
performssignificantlybetterthanLaBraM(ours)onalldatasets. Allresultsempiricallyprovethat
themodelarchitecturecontributesmoretotheperformanceimprovementcomparedtothelargersize
ofpretrainingdataset.
28

PublishedasaconferencepaperatICLR2025
H COMPARISON ON SEGMENT LENGTH
Table16: Performancecomparisononsegmentlengthofpre-trainingdata. Boldindicatesthebest.
Underlineindicatesthesecondbest.
FACED,9-class SEED-V,5-class
Methods BalancedAccuracy Cohen’sKappa WeightedF1 BalancedAccuracy Cohen’sKappa WeightedF1
BIOT 0.5118±0.0118 0.4476±0.0254 0.5136±0.0112 0.3837±0.0187 0.2261±0.0262 0.3856±0.0203
LaBraM 0.5273±0.0107 0.4698±0.0188 0.5288±0.0102 0.3976±0.0138 0.2386±0.0209 0.3974±0.0111
CBraMod(4s) 0.5448±0.0112 0.4938±0.0132 0.5541±0.0125 0.4086±0.0136 0.2539±0.0171 0.4097±0.0126
CBraMod(8s) 0.5453±0.0092 0.4950±0.0119 0.5534±0.0108 0.4083±0.0144 0.2573±0.0186 0.4112±0.0131
CBraMod(30s) 0.5509±0.0089 0.5041±0.0122 0.5618±0.0093 0.4091±0.0097 0.2569±0.0143 0.4101±0.0108
PhysioNet-MI,4-class SHU-MI,2-class
Methods BalancedAccuracy Cohen’sKappa WeightedF1 BalancedAccuracy AUC-PR AUROC
BIOT 0.6153±0.0154 0.4875±0.0272 0.6158±0.0197 0.6179±0.0183 0.6770±0.0119 0.6609±0.0127
LaBraM 0.6173±0.0122 0.4912±0.0192 0.6177±0.0141 0.6166±0.0192 0.6761±0.0083 0.6604±0.0091
CBraMod(4s) 0.6360±0.0113 0.5149±0.0185 0.6374±0.0128 0.6340±0.0196 0.7089±0.0110 0.6951±0.0105
CBraMod(8s) 0.6392±0.0104 0.5189±0.0198 0.6398±0.0096 0.6338±0.0182 0.7098±0.0105 0.6946±0.0089
CBraMod(30s) 0.6417±0.0091 0.5222±0.0169 0.6427±0.0100 0.6370±0.0151 0.7139±0.0088 0.6988±0.0068
Weconductanexperimenttofurtherevaluatetheimpactofsegmentlength. Specifically,wepre-
trainedCBraModin4sor8ssegmentlengthonourpre-trainingdatasetandcomparedtheresultswith
BIOT,LaBraMandCBraMod(30s). Onmostdatasets,CBraMod(4sor8s)performsslightlyworse
thanCBraMod(30s),butsignificantlybetterthanBIOTandLaBraM.Itindicatesthatthesegment
lengthhasanimpactonperformanceimprovement,buttheeffectisrelativelyminor.
I ABLATION STUDY ON TIME-DOMAIN AND FREQUENCY-DOMAIN SIGNALS
Table17: Theresultsofablationstudyontime-domainandfrequency-domainsignals.
FACED,9-class SEED-V,5-class
Settings BalancedAccuracy Cohen’sKappa WeightedF1 BalancedAccuracy Cohen’sKappa WeightedF1
Combining 0.5509±0.0089 0.5041±0.0122 0.5618±0.0093 0.4091±0.0097 0.2569±0.0143 0.4101±0.0108
Time-domain 0.5435±0.0078 0.4956±0.0134 0.5531±0.0085 0.4078±0.0134 0.2548±0.0204 0.4077±0.0123
Frequency-domain 0.5205±0.0157 0.4652±0.0241 0.5218±0.0143 0.3987±0.0184 0.2356±0.0315 0.3975±0.0201
PhysioNet-MI,4-class SHU-MI,2-class
Settings BalancedAccuracy Cohen’sKappa WeightedF1 BalancedAccuracy AUC-PR AUROC
Combining 0.6417±0.0091 0.5222±0.0169 0.6427±0.0100 0.6370±0.0151 0.7139±0.0088 0.6988±0.0068
Time-domain 0.6324±0.0097 0.5108±0.0175 0.6333±0.0086 0.6302±0.0145 0.7015±0.0104 0.6879±0.0094
Frequency-domain 0.6158±0.0076 0.4898±0.0138 0.6149±0.0094 0.6181±0.0167 0.6817±0.0125 0.6659±0.0113
CBraModcombinesbothtime-domainandfrequency-domainsignalstolearngenericrepresentation.
Here, we conduct an ablation study to verify the effectiveness of time-domain and frequency-
domain signals. The results are shown in Table 17. It is obvious that combining time-domain
andfrequency-domainsignalsachievesabetterperformancecomparedtoonlyusingtime-domain
featuresorfrequency-domainsignals,indicatingthatbothtime-domainandfrequency-domainsignals
areimportantforlearningEEGrepresentations. Notably,onlyusingtime-domainsignalsperforms
significantlybettercomparedtofrequency-domainsignals,andslightlyworsecomparedtocombining
time-domainandfrequency-domainsignals. Thereasoncouldbethattime-domainsignalscontain
frequency-domain information, which can be implicitly captured by neural networks. However,
frequency-domainsignalslacktime-domaininformationduetotheFFTprocess,leadingtoadecrease
inperformance.
J ABLATION STUDY ON FINE-TUNING
In this section, we conduct an ablation study on fine-tuning to explore the impact of fine-tuning.
Theexperimentisdesignedasfollows: 1)CBraMod: adjustingallparametersofCBraModduring
trainingondownstreamdatasets;2)CBraMod(fixed): fixingthepre-trainedparametersofCBraMod
andonlyadjustingtheparametersoftheclassifierduringtrainingondownstreamdatasets. 3)BIOT
(fixed): fixingthepre-trainedparametersofBIOTandonlyadjustingtheparametersoftheclassifier
29

PublishedasaconferencepaperatICLR2025
Table18: Theresultsofablationstudyonfine-tuning. Boldindicatesthebest. Underlineindicates
thesecondbest.
FACED,9-class SEED-V,5-class
Settings BalancedAccuracy Cohen’sKappa WeightedF1 BalancedAccuracy Cohen’sKappa WeightedF1
CBraMod 0.5509±0.0089 0.5041±0.0122 0.5618±0.0093 0.4091±0.0097 0.2569±0.0143 0.4101±0.0108
CBraMod(Fixed) 0.3146±0.0346 0.2579±0.0542 0.3077±0.0298 0.2536±0.0257 0.0842±0.0384 0.2568±0.0275
BIOT(Fixed) 0.2775±0.0318 0.1839±0.0512 0.2599±0.0271 0.2461±0.0287 0.0798±0.0361 0.2489±0.0257
LaBraM(Fixed) 0.3004±0.0458 0.2377±0.0617 0.2943±0.0375 0.2521±0.0267 0.0854±0.0342 0.2543±0.0265
PhysioNet-MI,4-class SHU-MI,2-class
Settings BalancedAccuracy Cohen’sKappa WeightedF1 BalancedAccuracy AUC-PR AUROC
CBraMod 0.6417±0.0091 0.5222±0.0169 0.6427±0.0100 0.6370±0.0151 0.7139±0.0088 0.6988±0.0068
CBraMod(Fixed) 0.3845±0.0345 0.2983±0.0498 0.3946±0.0378 0.5217±0.0247 0.5304±0.0253 0.5238±0.0317
BIOT(Fixed) 0.3698±0.0371 0.2703±0.0472 0.3723±0.0364 0.5123±0.0206 0.5215±0.0197 0.5146±0.0264
LaBraM(Fixed) 0.3715±0.0432 0.2814±0.0586 0.3796±0.0472 0.5233±0.0272 0.5329±0.0284 0.5218±0.0275
duringtrainingondownstreamdatasets. 4)LaBraM(fixed): fixingthepre-trainedparametersof
LaBraMandonlyadjustingtheparametersoftheclassifierduringtrainingondownstreamdatasets.
The results are shown in Table 18. Obviously, fixing the pre-trained parameters during training
ondownstreamdatasetswillleadtoaverylargeperformancedecline. ItindicatesthatCBraMod
cannotcurrentlyserveasafixed-parameterfeatureextractorlikeCLIP(Radfordetal.,2021)and
SAM(Kirillovetal.,2023),andfine-tuningisstillnecessary. Notably,CBraMod(fixed)outperforms
BIOT(fixed)andLaBraM(fixed),indicatingthatCBraModhasbettergeneralizabilityonunseen
datasetscomparedexistingmethodsonthefixingsetting.
K LOW-RESOURCE COMPARISON WITH EXISTING METHODS
Table19: Performancecomparisononlow-resourcesettingswith30%offine-tuningdata. Bold
indicatesthebest. Underlineindicatesthesecondbest.
FACED,9-class SEED-V,5-class
Methods BalancedAccuracy Cohen’sKappa WeightedF1 BalancedAccuracy Cohen’sKappa WeightedF1
CBraMod(fulldata) 0.5509±0.0089 0.5041±0.0122 0.5618±0.0093 0.4091±0.0097 0.2569±0.0143 0.4101±0.0108
CBraMod(30%) 0.4035±0.0233 0.3239±0.0265 0.4056±0.0256 0.3877±0.0236 0.2291±0.0246 0.3886±0.0255
BIOT(30%) 0.3428±0.0329 0.2573±0.0346 0.3501±0.0341 0.3505±0.0375 0.1775±0.0425 0.3492±0.0416
LaBraM(30%) 0.3513±0.0315 0.2672±0.0371 0.3548±0.0325 0.3686±0.0305 0.2044±0.0384 0.3700±0.0321
PhysioNet-MI,4-class SHU-MI,2-class
Methods BalancedAccuracy Cohen’sKappa WeightedF1 BalancedAccuracy AUC-PR AUROC
CBraMod(fulldata) 0.6417±0.0091 0.5222±0.0169 0.6427±0.0100 0.6370±0.0151 0.7139±0.0088 0.6988±0.0068
CBraMod(30%) 0.5613±0.0162 0.4150±0.0267 0.5621±0.0184 0.6231±0.0198 0.6901±0.0134 0.6754±0.0105
BIOT(30%) 0.5189±0.0312 0.3477±0.0371 0.5201±0.0308 0.5419±0.0345 0.6260±0.0273 0.6021±0.0301
LaBraM(30%) 0.5269±0.0237 0.3598±0.0342 0.5288±0.0225 0.5636±0.0289 0.6519±0.0227 0.6467±0.0274
In practical applications, obtaining labeled data for brain-computer interface (BCI) systems or
clinicalstudiesoftendemandssubstantialtimeandfinancialresources. Thislimitationhighlights
the critical need for developing and investigating EEG foundational models, which can reduce
relianceonextensivelabeleddatasets. Toillustratethepracticalutilityofourapproach,wecompare
CBraMod with existing foundational models across multiple datasets with limited labeled data
availability. Specifically, wefine-tuneCBraMod, BIOT,andLaBraMusing30%oflabeleddata.
TheresultsarepresentedinTable19. TheresultsclearlydemonstratethatCBraModconsistently
outperforms existing foundational models in low-resource settings across these datasets. This
observationunderscoresCBraMod’ssuperiorcapabilitytoeffectivelycaptureandleveragegeneric
EEG representations, even when the availability of labeled data is limited. Importantly, when
wecomparethelow-resourceresultswiththeresultsoffull-datafine-tuning,weobservethatthe
performance of CBraMod in low-resource scenarios is only marginally lower than the full-data
performancewhentrainedonSEED-VandSHU-MI.Thisfindingfurtherhighlightsthepractical
utilityofCBraMod,showcasingitsabilitytosustainstrongperformanceevenwithlimitedlabeled
data. Thisempiricallydemonstratesthatourmodelcaneffectivelymitigatethechallengesposedby
limiteddownstreamtasktrainingdatatosomeextent,offeringsignificantadvantagesforreal-world
applicationswherelabeleddataisoftenscarce.
30

PublishedasaconferencepaperatICLR2025
| L COMPARISON | SPLIT RATIO | CRISS-CROSS | ATTENTION |
| ------------ | ----------- | ----------- | --------- |
|              | ON          | OF          |           |
Table20: Performancecomparisononsplitratioofcriss-crossattention.
|     | FACED,9-class |     | SEED-V,5-class |
| --- | ------------- | --- | -------------- |
Settings BalancedAccuracy Cohen’sKappa WeightedF1 BalancedAccuracy Cohen’sKappa WeightedF1
CBraMod(2:6) 0.5405±0.0096 0.4921±0.0134 0.5526±0.0106 0.4046±0.0105 0.2438±0.0155 0.4062±0.0101
CBraMod(4:4) 0.5509±0.0089 0.5041±0.0122 0.5618±0.0093 0.4091±0.0097 0.2569±0.0143 0.4101±0.0108
CBraMod(6:2) 0.5413±0.0124 0.4910±0.0145 0.5531±0.0128 0.4033±0.0093 0.2410±0.0166 0.4051±0.0119
|     | PhysioNet-MI,4-class |     | SHU-MI,2-class |
| --- | -------------------- | --- | -------------- |
Settings BalancedAccuracy Cohen’sKappa WeightedF1 BalancedAccuracy AUC-PR AUROC
CBraMod(2:6) 0.6253±0.0105 0.4995±0.0176 0.6271±0.0129 0.6205±0.0170 0.6904±0.0090 0.6751±0.0088
CBraMod(4:4) 0.6417±0.0091 0.5222±0.0169 0.6427±0.0100 0.6370±0.0151 0.7139±0.0088 0.6988±0.0068
CBraMod(6:2) 0.6268±0.0102 0.5013±0.0188 0.6291±0.0104 0.6210±0.0139 0.6897±0.0115 0.6764±0.0072
Ourcriss-crosstransformermodelsspatialandtemporaldependenciesseparatelythroughtwoparallel
attentionmechanisms: spatialandtemporalattention. Itsplitsthe8headsoftheintermediatelayer
embeddingsintotwoequalparts(spatialheads: temporalheads=4:4),whicharethenprocessed
bythespatialandtemporalattentionmechanisms,respectively,ensuringthemodelassignsequal
emphasistospatialandtemporaldependencies. Inthissection,weadjustthesplitratioofheads
andobservehowthedecodingperformanceondownstreamtasksvarieswhenthemodelprioritizes
spatial dependencies or temporal dependencies. The experimental results are shown in Table 20.
Evidently,themodel’sperformanceshowsanoticeabledeclinewhenitprioritizeseitherspatial(6:2)
ortemporal(2:6)dependenciesovertreatingthemequally. Thisindicatesthatspatialandtemporal
dependenciesareequallyimportantinEEGrepresentationlearning,providingempiricalevidencefor
thevalidityofourcriss-crossattentionmechanism.
| M MASK RATIO | ANALYSIS |     |     |
| ------------ | -------- | --- | --- |
0.27
0.51
0.26
| appaK s'nehoC |     | appaK s'nehoC |     |
| ------------- | --- | ------------- | --- |
| 0.50          |     | 0.25          |     |
| 0.49          |     | 0.24          |     |
0.23
0.48
0.22
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9
|          | Mask Ratio |      | Mask Ratio |
| -------- | ---------- | ---- | ---------- |
| (a)FACED |            |      | (b)SEED-V  |
| 0.54     |            | 0.71 |            |
0.53
| appaK s'nehoC |     | 0.70  |     |
| ------------- | --- | ----- | --- |
| 0.52          |     | CORUA |     |
0.51
0.69
0.50
| 0.49 |     | 0.68 |     |
| ---- | --- | ---- | --- |
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9
|                 | Mask Ratio |     | Mask Ratio |
| --------------- | ---------- | --- | ---------- |
| (c)PhysioNet-MI |            |     | (d)SHU-MI  |
Figure9: Performancecomparisononmaskratio.
Inthissection,weconductcomparisonexperimentonmaskratiotoexploreitsimpactonperformance
ofCBraModondownstreamdatasets.TheresultsareasshowninFigure9.CBraModusuallyachieves
abetterperformancewhentherangeofmaskratiois0.3to0.7. OnFACED,CBraModperformsthe
bestwhenmaskratioissetto0.5,showninFigure9(a). AsshowninFigure9(b),CBraModachieves
thebestperformanceonSEED-Vasmaskratiois0.6and0.5maskratiofollows0.6. InFigure9(c)
wecanseethat0.2maskratioisthebestonPhysioNet-MI,and0.5maskratioperformthesecond
best. Finally,onSHU-MI,0.4isthebestmaskratioandperformanceof0.5maskratioiscloseto0.4
31

PublishedasaconferencepaperatICLR2025
maskratio,showninFigure9(d). Insummary,0.5maskratioisaveryappropriatechoicetoachieve
goodperformanceonmultipledownstreamdatasets.
N MASK TOKEN COMPARISON
Table21: Theresultsofmasktokencomparison.
FACED,9-class SEED-V,5-class
Methods BalancedAccuracy Cohen’sKappa WeightedF1 BalancedAccuracy Cohen’sKappa WeightedF1
Full-zerotoken 0.5509±0.0089 0.5041±0.0122 0.5618±0.0093 0.4091±0.0097 0.2569±0.0143 0.4101±0.0108
Learnabletoken 0.5527±0.0096 0.5033±0.0131 0.5627±0.0094 0.4078±0.0105 0.2517±0.0148 0.4089±0.0123
PhysioNet-MI,4-class SHU-MI,2-class
Methods BalancedAccuracy Cohen’sKappa WeightedF1 BalancedAccuracy AUC-PR AUROC
Full-zerotoken 0.6417±0.0091 0.5222±0.0169 0.6427±0.0100 0.6370±0.0151 0.7139±0.0088 0.6988±0.0068
Learnabletoken 0.6399±0.0112 0.5211±0.0215 0.6433±0.0175 0.6349±0.0142 0.7156±0.0101 0.7012±0.0096
Inthissection,wecomparetheperformanceoffull-zeromasktokenandlearnablemasktokenof
exploretheeffectivenessofmasktokentype. Theexperimentisdesignedasfollows: 1)Full-zero
token: utilizingafull-zerovectorwiththesamedimensionaspatchembeddingstomasktheEEG
patches;2)Learnabletoken: usingavectorwhoseparametersarelearnabletomasktheEEGpatches.
TheresultsofmasktokencomparisonarepresentedinTable21. Thereisnosignificantperformance
differencebetweenfull-zeroandlearnablemasktoken,indicatingthattheircapabilitiesaresimilar.
O PARAMETERS AND FLOPS COMPARISON
Table22: ParametersandFLOPscomparisononCHB-MIT(16channels,10seconds).
Methods Params FLOPs
EEGNet 0.003M 8.9M
Conformer 0.55M 29.6M
SPaRCNet 0.79M 65.7M
ContraWR 1.6M 66.4M
CNN-Transformer 3.2M 79.1M
FFCL 2.4M 209.9M
ST-Transformer 3.5M 42.1M
BIOT 3.2M 483.3M
LaBraM-Base 5.8M 483.0M
LaBraM-Large 46M 3.06G
LaBraM-Huge 369M 22.8G
CBraMod(fullattention) 4.1M 469.4M
CBraMod(axialattention) 4.0M 334.7M
CBraMod(attentionofCCNet) 4.0M 354.6M
CBraMod(criss-crossattention) 4.0M 318.9M
Inthissection,takingtheCHB-MITdatasetasanexample,wecomparetheparametercountsand
FLOPs of CBraMod with existing methods and CBraMod with other attention mechanism. The
numbers of parameters in baselines are provided by LaBraM (Jiang et al., 2024), and others are
calculatedbyThop3. TheresultsareshowninTable22. TheparametersandFLOPsoffoundation
modelsaremorethanthenon-foundation-modelbaselinesbecausethefoundationmodelusually
needtobelargeforlearninggenericrepresentations. LaBraM-LargeandLaBraM-Hugeachievea
goodperformanceonsomedownstreamdatasets,buttheirparametersandFLOPsaresignificantly
morethanCBraMod. CBraModhasfewerFLOPscomparedtothefoundationmodelswithsimilar
parametercounts,BIOTandLaBraM-Base. Moreover,theCBraModbasedoncriss-crossattention
hasthefewestFLOPscomparedtootherattentionmechanism. ItindicatesthatCBraModachieves
lowercomputationalcomplexitybyourcriss-crossEEGmodeling.
3https://github.com/Lyken17/pytorch-OpCounter
32

PublishedasaconferencepaperatICLR2025
P INTERPRETABILITY ANALYSIS
P.1 TOPOGRAPHYVISUALIZATION
(a)RawEEGtopography
(b)ClassActivationTopographyofCBraMod
Figure10: Topographyvisualizationonmotorimageryclassification(PhysioNet-MI).
Inthissection,weprovideatopographyvisualizationonmotorimageryclassification. Thesetup
ofvisualizationanalysisareasfollows: RawEEGtopography: Wecomputedtheenergyintensity
oftherawEEGsignalsforeachchannelandvisualizedtheresultsusingatopographicmap. Class
ActivationTopographyofCBraMod: WeutilizedGrad-CAM(Gradient-weightedClassActivation
Mapping)(Selvarajuetal.,2017)tocomputethecontributionofeachchannelinthelearnedrepre-
sentationsofCBraModtotheclassificationoutcomes,visualizingtheresultsasaClassActivation
Topography. ThevisualizationresultsareshowninFigure10. Electrodesrelatedtoleftandrightfist
movementsexhibitsymmetricpatterns,whilebilateralelectrodesarelinkedtobothfistsandboth
feetmovements,withdistinctchannelscorrespondingtoeachofthefourclasses. Comparedtothe
rawEEGsignals,therepresentationslearnedbyCBraModexhibitmorepronounceddifferencesin
theimportanceassignedtovariouschannelsfordifferentclasses.
P.2 REPRESENTATIONVISUALIZATIONSONDOWNSTREAMDATASETS
In this section, we provide a representation visualization analysis on downstream datasets using
UMAP(McInnesetal.,2018)dimensionalityreduction. Theexperimentalsetupisasfollows: 1)
RawEEGsampleofadownstreamdataset: wedirectlyvisualizetherawEEGsamplefroma
downstreamdataset. 2)CBraMod(w/ofine-tuning)onadownstreamdataset: wevisualizethe
representations of the pre-trained CBraMod without fine-tuning on the test set of a downstream
dataset. 3) CBraMod (w/ fine-tuning) on a downstream dataset: we fine-tune the pre-trained
CBraModonthetrainingsetofadownstreamdatasetandvisualizeitsrepresentationsonthetestset.
ThevisualizationresultsareasshowninFigure11. Itisevidentthattherepresentationdistributions
in Figure 11(b) and (e) exhibit better clustering effects compared to the distribution of the raw
EEGsamples. Itindicatesthatpre-trainingenablesCBraModtolearngenericEEGrepresentations,
allowingittocapturelabel-relatedfeaturesofdownstreamdatasetstosomeextent,evenwithout
fine-tuning. Additionally,therepresentationdistributionsinFigure11(c)and(f)alsoexhibitbetter
clusteringeffectscomparedtotherepresentationsdistributionwithoutfine-tuning. Itreflectstherole
offine-tuningonthedownstreamdata.
33

PublishedasaconferencepaperatICLR2025
|     |       | FACED |     | 8   | FACED |     |     |     | FACED |     |     |
| --- | ----- | ----- | --- | --- | ----- | --- | --- | --- | ----- | --- | --- |
|     | Anger |       |     |     |       |     | 7   |     |       |     |     |
6 Disgust Fear
|     | Sadness |     |     | 7   |     |     | 6   |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Neutral
| 5                | Amusement I n s piration |     |     |                  |     |     | 5                |     |     |     |     |
| ---------------- | ------------------------ | --- | --- | ---------------- | --- | --- | ---------------- | --- | --- | --- | --- |
|                  | J o y                    |     |     | 6                |     |     |                  |     |     |     |     |
| 2 tnenopmoC pamU | Tenderness               |     |     | 2 tnenopmoC pamU |     |     | 2 tnenopmoC pamU |     |     |     |     |
| 4                |                          |     |     | 5                |     |     | 4                |     |     |     |     |
3
| 3   |     |                  |     | 4 Anger                      |                  |          |     | Anger           |                  |     |     |
| --- | --- | ---------------- | --- | ---------------------------- | ---------------- | -------- | --- | --------------- | ---------------- | --- | --- |
|     |     |                  |     | Disgust                      |                  |          | 2   | Disgust         |                  |     |     |
|     |     |                  |     | Fear                         |                  |          |     | Fear            |                  |     |     |
| 2   |     |                  |     | 3 S N a e d u n tr e a s l s |                  |          | 1   | Sadness Neutral |                  |     |     |
|     |     |                  |     | Amusement                    |                  |          |     | Amusement       |                  |     |     |
|     |     |                  |     | I n s piration               |                  |          | 0   | Inspiration     |                  |     |     |
| 1   |     |                  |     | 2 J Tenderness o y           |                  |          |     | Joy Tenderness  |                  |     |     |
|     | 3 2 | 1 0              | 1   | 2 3 6                        | 7 8 9            | 10 11 12 | 13  | 2 1             | 0 1              | 2 3 | 4 5 |
|     |     | Umap Component 1 |     |                              | Umap Component 1 |          |     |                 | Umap Component 1 |     |     |
(a)RawEEGsampleofFACED (b)CBraMod(w/ofine-tuning)onFACED (c)CBraMod(w/fine-tuning)onFACED
|     |     | PhysioNet-MI |     |     | PhysioNet-MI |     |     |     |     |     |     |
| --- | --- | ------------ | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
PhysioNet-MI
| 8   | left fist |     |     |     |     |     | left fist 13 |     |     |     | left fist |
| --- | --------- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --------- |
right fist both fists right fist both fists right fist both fists
|     | both feet |     |     | 8   |     |     | both feet |     |     |     | both feet |
| --- | --------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --------- |
| 7   |           |     |     |     |     |     | 12        |     |     |     |           |
11
| 2 tnenopmoC pamU |     |     |     | 2 tnenopmoC pamU 6 |     |     | 2 tnenopmoC pamU |     |     |     |     |
| ---------------- | --- | --- | --- | ------------------ | --- | --- | ---------------- | --- | --- | --- | --- |
| 6                |     |     |     |                    |     |     | 10               |     |     |     |     |
4
| 5   |     |     |     |     |     |     | 9   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
8
| 4   |     |     |     | 2   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
7
6
| 3   |     |     |     | 0   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1 0 Umap Component 1 1 2 3 2 0 2 Umap Component 1 4 6 8 10 12 0 2 4 Umap Component 1 6 8 10 12
(d)RawEEGsampleofPhysioNet-MI (e)CBraMod(w/ofine-tuning)onPhysioNet-MI (f)CBraMod(w/fine-tuning)onPhysioNet-MI
|              |         | Figure11: |              | Representationvisualizationsondownstreamdatasets. |              |         |     |              |         |     |     |
| ------------ | ------- | --------- | ------------ | ------------------------------------------------- | ------------ | ------- | --- | ------------ | ------- | --- | --- |
| T 3          | Layer 1 |           | T 3          | Layer 2                                           | T 3          | Layer 3 |     | T 3          | Layer 4 |     |     |
| FF 87        |         |           | FF 87        |                                                   | FF 87        |         |     | FF 87        |         |     |     |
| FF PP 21     |         |           | FF PP 21     |                                                   | FF PP 21     |         |     | FF PP 21     |         |     |     |
| FF 43        |         |           | FF 43        |                                                   | FF 43        |         |     | FF 43        |         |     |     |
| slennahC C 3 |         |           | slennahC C 3 |                                                   | slennahC C 3 |         |     | slennahC C 3 |         |     | 1.0 |
| C F ZZ Z     |         |           | C F ZZ Z     |                                                   | C F ZZ Z     |         |     | C F ZZ Z     |         |     |     |
| CP 4         |         |           | CP 4         |                                                   | CP 4         |         |     | CP 4         |         |     |     |
| PP 43        |         |           | PP 43        |                                                   | PP 43        |         |     | PP 43        |         |     |     |
| OO 21        |         |           | OO 21        |                                                   | OO 21        |         |     | OO 21        |         |     |     |
| TTT 654      |         |           | TTT 654      |                                                   | TTT 654      |         |     | TTT 654      |         |     |     |
0.8
0 5 10 15 20 25 0 5 10 15 20 25 0 5 10 15 20 25 0 5 10 15 20 25
|           | Time Segments |     |           | Time Segments |           | Time Segments |     |           | Time Segments |     |     |
| --------- | ------------- | --- | --------- | ------------- | --------- | ------------- | --- | --------- | ------------- | --- | --- |
|           | Layer 5       |     |           | Layer 6       |           | Layer 7       |     |           | Layer 8       |     |     |
| T FF 87 3 |               |     | T FF 87 3 |               | T FF 87 3 |               |     | T FF 87 3 |               |     |     |
| FF PP 21  |               |     | FF PP 21  |               | FF PP 21  |               |     | FF PP 21  |               |     |     |
| FF 43     |               |     | FF 43     |               | FF 43     |               |     | FF 43     |               |     | 0.6 |
slennahC C F Z 3 slennahC C F Z 3 slennahC C F Z 3 slennahC C F Z 3 rabroloC
| C CP ZZ |     |     | C CP ZZ |     | C CP ZZ |     |     | C CP ZZ |     |     |     |
| ------- | --- | --- | ------- | --- | ------- | --- | --- | ------- | --- | --- | --- |
| PP 4 43 |     |     | PP 4 43 |     | PP 4 43 |     |     | PP 4 43 |     |     |     |
| OO 21   |     |     | OO 21   |     | OO 21   |     |     | OO 21   |     |     |     |
| TTT 654 |     |     | TTT 654 |     | TTT 654 |     |     | TTT 654 |     |     | 0.4 |
0 5 10 15 20 25 0 5 10 15 20 25 0 5 10 15 20 25 0 5 10 15 20 25
|              | Time Segments |     |              | Time Segments |              | Time Segments |     |              | Time Segments |     |     |
| ------------ | ------------- | --- | ------------ | ------------- | ------------ | ------------- | --- | ------------ | ------------- | --- | --- |
| T 3          | Layer 9       |     | T 3          | Layer 10      | T 3          | Layer 11      |     | T 3          | Layer 12      |     |     |
| FF 87        |               |     | FF 87        |               | FF 87        |               |     | FF 87        |               |     |     |
| FF PP 21     |               |     | FF PP 21     |               | FF PP 21     |               |     | FF PP 21     |               |     |     |
| FF 43        |               |     | FF 43        |               | FF 43        |               |     | FF 43        |               |     | 0.2 |
| slennahC C 3 |               |     | slennahC C 3 |               | slennahC C 3 |               |     | slennahC C 3 |               |     |     |
| C F ZZ Z     |               |     | C F ZZ Z     |               | C F ZZ Z     |               |     | C F ZZ Z     |               |     |     |
| CP 4         |               |     | CP 4         |               | CP 4         |               |     | CP 4         |               |     |     |
| PP 43        |               |     | PP 43        |               | PP 43        |               |     | PP 43        |               |     |     |
| OO 21        |               |     | OO 21        |               | OO 21        |               |     | OO 21        |               |     |     |
| TTT 654      |               |     | TTT 654      |               | TTT 654      |               |     | TTT 654      |               |     |     |
0 5 10 15 20 25 0 5 10 15 20 25 0 5 10 15 20 25 0 5 10 15 20 25
|     | Time Segments |     |     | Time Segments |     | Time Segments |     |     | Time Segments |     |     |
| --- | ------------- | --- | --- | ------------- | --- | ------------- | --- | --- | ------------- | --- | --- |
Figure12: Visualizationofpatchrelationshipsfromeachcriss-crosstransformerlayer.
P.3 VISUALIZATIONOFPATCHRELATIONSHIPSFROMEACHCRISS-CROSSTRANSFORMER
LAYER
Inthissection,weprovideavisualizationanalysisforcriss-crossEEGmodeling. Specifically,we
feedEEGsamples(19channels×30seconds)ofTUEGintothepre-trainedCBraModtoobtain
the output of each criss-cross transformer layer, E ∈ RC×n×d, where m ∈ [1,2,...,12] is the
m
layer number, C = 19 is the number of channels, n = 30 is the number of time segments and
d=200isthedimensionofpatchembedding. Thus,E consistsof19×30EEGpatches. Without
m
lossofgenerality,weselectthe16-thpatchoftheCzchannelasthecentralpatch,thencalculate
the correlation coefficient between the embedding of this patch and the embeddings of all other
patches. The results are visualized in the form of a heatmap, as shown in the Figure 12. In the
Figure 12, the channels are arranged in a sequence corresponding to the anterior brain, Cz, and
posteriorbrainregions. Itisevidentthatthecorrelationcoefficientsbetweentheotherpatchesand
34

PublishedasaconferencepaperatICLR2025
thecentralpatchexhibitacriss-crossshape. Itindicatesthattheproposedmethodhassuccessfully
learnedthecriss-crossspatial-temporaldependenciespatternbetweenpatchesintheEEGsignal.
Furthermore,inthedeepertransformerlayers,weobservethattheassociationsbetweenallpatches
andthecentralpatcharestronger. Thissuggeststhatthecriss-crosstransformerisalsocapableof
learningnon-criss-crossdependenciesthroughitsmulti-layeredstructure. Allofthesevisualizations
provideinterpretabilityforthecriss-crossEEGmodelingapproachwepropose.
Q A LEAVE-ONE-SUBJECT-OUT COMPARISON WITH EEG-SIMPLECONV ON
BCIC-IV-2A
Table23: TheresultsoftheLOSOcomparisonwithEEG-SimpleConv(BCIC-IV-2a,4-class).
Methods BalancedAccuracy AUC-PR AUROC
EEG-SimpleConv(w/oKeyIngredients) 0.5650±0.0989 0.4201±0.1319 0.5484±0.1047
CBraMod(w/oKeyIngredients) 0.5968±0.0816 0.4558±0.1088 0.5889±0.0875
EEG-SimpleConv(w/KeyIngredients) 0.7221±0.0768 0.5765±0.1069 0.6977±0.0918
CBraMod(w/KeyIngredients) 0.7405±0.0635 0.5997±0.0833 0.7195±0.0682
Specifically, we included the performance comparison with the strong baseline, EEG-
SimpleConv(ElOuahidietal.,2024),undertheleave-one-subject-out(LOSO)protocolonBCIC-
IV-2a. In EEG-SimpleConv paper, the reported performance of 72.1 ± 7.3 accuracy under the
leave-one-subject-out(LOSO)protocolreliesheavilyonseveraladvancedpreprocessingandtraining
techniquesreferredtoas”KeyIngredients,”includingEuclideanAlignment(EA),sessionstatistics,
Mixup,andsubject-wiseregularization. Whenthesetechniquesarenotemployed,EEG-SimpleConv
achievessignificantlylowerperformance: 56.4±9.0accuracy,reportedintheoriginalpaper.
Toprovideamorerigorousandfairevaluation,weconductedexperimentsunderthesameLOSO
protocolusedbyEEG-SimpleConv,bothwithandwithoutincorporatingthe”KeyIngredients.”The
resultsaresummarizedasshowninTable23. Theseresultsdemonstratethat: 1)Ourreproduction
ofEEG-SimpleConvmatchestheoriginalpaper’sfindings. 2)CBraModconsistentlyoutperforms
EEG-SimpleConv under both settings, achieving higher balanced accuracy, Cohen’s Kappa, and
weightedF1scoreswhilealsodemonstratinglowerinter-subjectvariance,highlightingitsrobustness
andeffectiveness.
R COMPARISON ON CONVERGENCE SPEED WITH SUPERVISED MODEL
0.5
0.4
0.3
0.2
0.1
0.0
0 10 20 30 40 50
Epoch
appaK
s'nehoC
CBraMod
EEGConformer
Figure13: Performancecurvescomparisonfordownstreamtaskfine-tuninginFACED.
Inthissection,wecomparedtheperformancecurvesofourmethodwithexistingsupervisedlearning
modelsduringdownstreamtasktraining(usingEEGConformerontheFACEDdatasetasanexample).
Specifically,wefine-tunedthepretrainedCBraModontheFACEDtrainingset,testingitsperformance
onthevalidationsetattheendofeachepoch. Wethenplottedtheperformancevariationcurveand
compared it with the performance curve of EEGConformer. The results are shown in Figure 13.
35

PublishedasaconferencepaperatICLR2025
Obviously,CBraModcanachieveadecentresultwithinthefirstepochandconvergewithin10epochs.
However,EEGConformerachievesaCohen’sKapparesultcloseto0inthefirstepoch,anditonly
reachesconvergenceafterapproximately30epochs. Theseresultsdemonstratethatourpretrained
modelachievesfasterconvergenceondownstreamtasks,furtherprovingthatourmethodiscapable
oflearninggenericEEGrepresentationsthatcaneffectivelyadapttodownstreamtasks.
S DISCUSSION
S.1 IMPLICATION
NovelInsightsforEEGFoundationModelConstruction Theproposedcriss-crossEEGmodel-
ingstrategyandasymmetricconditionalpositionalencoding(ACPE)schemeofferprofoundinsights
intotheconstructionofEEGfoundationmodels. TraditionalEEGmodelingapproachesoftenover-
looktheuniquestructuralcharacteristicsofEEGsignals,whichexhibitheterogeneousspatialand
temporaldependencies. Bydevisingacriss-crosstransformerthatmodelsthesedependenciesin
parallel,ourapproachcapturestheintricaterelationshipswithinEEGdatamoreeffectively. This
strategynotonlyenhancesthemodel’sabilitytogeneralizeacrossdiverseEEGformatsbutalso
provides a more nuanced understanding of the underlying brain dynamics. The ACPE scheme
furtheraugmentsthiscapabilitybydynamicallyencodingpositionalinformation,makingthemodel
adaptabletovaryingchannelconfigurationsandreferencecontexts. Thisflexibilityiscrucialfor
EEGfoundationmodels, asitallowsthemtobeappliedacrossawiderangeofclinicalandBCI
applications. Thesuccessofourapproachunderscorestheimportanceoftailoredmodelingstrategies
forEEGdata,settinganewbaselineforfutureresearchinthisdomain.
Real-WorldBCISystemDevelopment TheexplorationofEEGfoundationmodels,asexemplified
byourwork,holdssignificantpromiseforthedevelopmentofpracticalBCIsystems,particularlyin
thecontextofuniversalBCIsystems. Byleveraginglarge-scalepre-trainingonlargeEEGcorpora,
ourmodelcanlearngenericrepresentationsthatarerobustandadaptabletovariousdownstream
tasks. ThiscapabilityisessentialforbuildingBCIsystemsthatcanbedeployedacrossdifferent
userpopulationsandclinicalsettings,therebyenhancingtheiraccessibilityandutility. Moreover,
thestronggeneralizationabilityofourmodelreducesthedependencyontask-specificlabeleddata,
whichisoftenscarceandexpensivetoobtain. Thisisparticularlybeneficialinreal-worldapplications
wheredatacollectioncanbechallengingandresource-intensive. Theabilitytofine-tunethemodelon
limiteddatawhilemaintaininghighperformanceisacriticalsteptowardstherealizationofuniversal
BCIsystemsthatcanbewidelyadoptedinclinicalpractice.
Insummary,thenovelmodelingstrategiesandthedemonstratedgeneralizabilityofourEEGfoun-
dationmodelprovidevaluableinsightsandpracticalbenefitsforthedevelopmentofadvancedBCI
systems. TheseadvancementsnotonlypushtheboundariesofcurrentEEGdecodingtechniquesbut
alsopavethewayformoreinclusiveandeffectivebrain-computerinterfacesinthefuture.
S.2 LIMITATION
Ourworkstillhassomelimitations.Firstly,TUEGcorpusisaverylargedatasetwithahighamountof
dirtydata. Weemployedarathercrudeapproachtofilteroutcleandataforpre-training,whichhelped
addresstheissueofhavingahighamountofdirtydata. However,italsoresultedinasignificant
reductionintheamountofavailablepre-trainingdata. Secondly,ourmethodhasachievedsuccess
onmultipledownstreamdatasetsandhaslowercomputationalcomplexitycomparedtootherEEG
Foundationmodels,butitstillhasahigherparametercountandcomputationalcomplexitycompared
tonon-foundationmodels. Thehighparametercountandcomputationalcomplexityresultinahigher
usagethresholdforEEGfoundationmodelsandmakesitdifficulttodeploythemondeviceswith
lowercomputationalpower. Next,duetolimitedcomputationalresources,wehavenotyetanalyzed
thepotentialscalinglawsforEEGpre-traininginalargerscale(e.g. billionlevel). Finally,large
modelshaveachievedtremendoussuccessinfieldssuchasvisionandlanguage. However,thereis
stillalackofsufficientexplorationonhowtoutilizethesepre-trainedlargemodelsinotherfieldsfor
understandingEEGsignalsandvariousotherbrainsignals.
36

PublishedasaconferencepaperatICLR2025
S.3 FUTUREWORK
Givingtheabovelimitations,ourfutureworksareasfollows: 1)AlargerandcleanerEEGcorpusis
essentialtotrainabetterEEGfoundationmodel. WewillcollectmoreEEGcorpusandexploremore
automatedandeffectivedatapreprocessingmethodsforlearningmorepowerfulrepresentations. 2)
WewillexplorewaystodevelopaneffectiveandefficientEEGfoundationmodel. Forexample,we
candirectlytrainasmallerEEGfoundationmodelorutilizetechniquessuchasknowledgedistillation
toobtainasmallerEEGfoundationmodelfromapre-trainedlargeEEGfoundationmodel. 3)We
willexploreusinglargerpretrainingdatasetsandmodelsize,tofurtherenhancetheperformance
oftheEEGfoundationmodelandanalyzethepotentialscalinglawsforEEGpre-training. 4)We
willexploreestablishingconnectionsbetweenlargemodelsinotherfields(e.g. visionandlanguage)
andbrainsignals,utilizingtheknowledgefromthesemodelstodecodebrainsignals. Itmayinvolve
techniquessuchastransferlearning.
37