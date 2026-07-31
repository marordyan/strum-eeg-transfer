PublishedasaconferencepaperatICLR2024
| LARGE | BRAIN |     | MODEL |     |     | LEARNING |     | GENERIC |     | REP- |     |
| ----- | ----- | --- | ----- | --- | --- | -------- | --- | ------- | --- | ---- | --- |
FOR
|              |     |     |      |     | TREMENDOUS |     |     | EEG |     | DATA |     |
| ------------ | --- | --- | ---- | --- | ---------- | --- | --- | --- | --- | ---- | --- |
| RESENTATIONS |     |     | WITH |     |            |     |     |     |     |      | IN  |
BCI
Wei-BangJiang1,Li-MingZhao2∗&Bao-LiangLu12∗
| 1ShanghaiJiaoTongUniversity |     |     |     | 2ShanghaiEmotionhelperTechnologyCo.,Ltd. |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
935963004@sjtu.edu.cn,liming.zhao@emotionhelper.com,bllu@sjtu.edu.cn
4202 yaM 92  ]GL.sc[  1v56781.5042:viXra
ABSTRACT
|     | The current                          | electroencephalogram |           |          | (EEG)      | based        | deep learning             | models |       | are typi- |     |
| --- | ------------------------------------ | -------------------- | --------- | -------- | ---------- | ------------ | ------------------------- | ------ | ----- | --------- | --- |
|     | cally designed                       | for                  | specific  | datasets | and        | applications | in brain-computer         |        |       | interac-  |     |
|     | tion (BCI),                          | limiting             | the scale | of       | the models | and          | thus diminishing          |        | their | percep-   |     |
|     | tualcapabilitiesandgeneralizability. |                      |           |          | Recently,  |              | LargeLanguageModels(LLMs) |        |       |           |     |
haveachievedunprecedentedsuccessintextprocessing,promptingustoexplore
|     | the capabilities  |                 | of Large     | EEG Models | (LEMs).     |         | We hope          | that LEMs |               | can break |     |
| --- | ----------------- | --------------- | ------------ | ---------- | ----------- | ------- | ---------------- | --------- | ------------- | --------- | --- |
|     | through           | the limitations | of           | different  | task        | types   | of EEG datasets, |           | and obtain    | uni-      |     |
|     | versal perceptual |                 | capabilities | of         | EEG signals | through | unsupervised     |           | pre-training. |           |     |
Thenthemodelscanbefine-tunedfordifferentdownstreamtasks.However,com-
|     | pared to         | text data,  | the volume                                          |             | of EEG     | datasets       | is generally          | small            | and       | the for- |     |
| --- | ---------------- | ----------- | --------------------------------------------------- | ----------- | ---------- | -------------- | --------------------- | ---------------- | --------- | -------- | --- |
|     | matvarieswidely. |             | Forexample,therecanbemismatchednumbersofelectrodes, |             |            |                |                       |                  |           |          |     |
|     | unequal          | length data | samples,                                            | varied      | task       | designs,       | and low               | signal-to-noise  |           | ratio.   |     |
|     | To overcome      | these       | challenges,                                         |             | we propose | a unified      | foundation            |                  | model     | for EEG  |     |
|     | called Large     | Brain       | Model                                               | (LaBraM).   | LaBraM     |                | enables cross-dataset |                  | learning  | by       |     |
|     | segmenting       | the         | EEG signals                                         | into        | EEG        | channel        | patches.              | Vector-quantized |           | neu-     |     |
|     | ral spectrum     | prediction  | is                                                  | used        | to train   | a semantically | rich                  | neural           | tokenizer | that     |     |
|     | encodes          | continuous  | raw                                                 | EEG channel |            | patches        | into compact          | neural           | codes.    | We       |     |
thenpre-trainneuralTransformersbypredictingtheoriginalneuralcodesforthe
|     | masked   | EEG channel | patches. |             | The LaBraMs |        | were pre-trained |     | on about  | 2,500 |     |
| --- | -------- | ----------- | -------- | ----------- | ----------- | ------ | ---------------- | --- | --------- | ----- | --- |
|     | hours of | various     | types of | EEG signals | from        | around | 20 datasets      | and | validated | on    |     |
multipledifferenttypesofdownstreamtasks.Experimentsonabnormaldetection,
|     | event type                                                      | classification, |     | emotion | recognition, |     | and gait prediction |     | show | that our |     |
| --- | --------------------------------------------------------------- | --------------- | --- | ------- | ------------ | --- | ------------------- | --- | ---- | -------- | --- |
|     | LaBraMoutperformsallcomparedSOTAmethodsintheirrespectivefields. |                 |     |         |              |     |                     |     |      | Our      |     |
codeisavailableathttps://github.com/935963004/LaBraM.
1 INTRODUCTION
Electroencephalography(EEG)isamethodtorecordanelectrogramofthespontaneouselectrical
activity of the brain. It is typically non-invasive, with the EEG electrodes placed along the scalp
usingtheinternational10–20system. EEGsignalscanbeformulatedasamatrixofrealnumbers
RC×T,
X ∈ where C is the number of EEG electrodes (channels) that may vary depending on
the acquisition equipment used, and T represents the total number of samples, which is related to
thecollectiontimeandsamplingrate. Ashighlyobjectivephysiologicalsignals,EEGhasdemon-
strated remarkable potential in seizure epilepsy classification (Boonyakitanont et al., 2020), acute
stressdetection(Sharmaetal.,2022),sleepstageclassification(Aboalayonetal.,2016),motorim-
ageryrecognition(Aminetal.,2019),abnormalidentification(Royetal.,2019),emotionanalysis
(Suhaimietal.,2020),andauditoryattentiondetection(Biesmansetal.,2016).
Numerous deep learning models have been proposed to address the aforementioned tasks in their
respective fields. Some works apply convolutional neural networks (CNN) across and within raw
EEGchannelstoencodespatialandtemporalfeatures(Lawhernetal.,2018),whileothersprepro-
cessthedatausingshort-timeFouriertransform(STFT)andemployGraphNeuralNetwork(GNN)
∗Li-MingZhaoandBao-LiangLuareco-correspondingauthors.
1

PublishedasaconferencepaperatICLR2024
on the resulting spectrograms to obtain semantic features of brain area links (Song et al., 2018).
ResearchersalsosegmentthesignalanduseaCNNsegmentencoderwithadownstreamsequence
model such as recurrent neural networks (RNN) to capture temporal dynamics (Xu et al., 2020).
ThesemodelsprimarilyfocusonEEGsamplesthatadheretospecifictaskformats,mainlybecause
theequipmentusedtocollectEEGdiffersbetweendatasets,whichintroducesmismatchedchannels
andvariablelengths. Meanwhile,EEGdatacollectionisquiteexpensive,whichmakesitchalleng-
ing to build large EEG datasets specifically designed for a particular task. To prevent overfitting,
the parameters of these models need to be regulated, which in turn hampers the model’s ability to
learnEEGexpressionsandlimitsitsgeneralizability.Consequently,wediscoveredthatcurrentEEG
modelsaretypicallyproprietaryandlackthecapacitytoperformcross-tasklearning.
Recently, we have been impressed by the capabilities of LLMs (Ouyang et al., 2022; Wei et al.,
2022). Specifically,Transformer-basedmodelshavedemonstratedpromisingresultsinnaturallan-
guage processing tasks, which highlights the potential of self-supervised pre-training as a means
for harnessing large-scale data. These masked language modeling tasks involve randomly mask-
ing some proportion of tokens within a text and then recovering the masked tokens based on the
Transformerencodingresultsofthecorruptedtext. Motivatedbythesemethods,weproposetoap-
plyreconstructionideastopre-trainneuralTransformers. However,itisadauntingtasktodirectly
applyLLM-stylepre-trainingtoEEGdata. Thechallengesaresummarizedasfollows:
1)LackofsufficientEEGdata.TheacquisitionofEEGdataissignificantlychallengingcompared
tonaturallanguageandimagedata. Moreover,theannotationofEEGdatausuallyrequiresalotof
effortonthepartofexpertsinthecorrespondingfield,thusleadingtothefactthatonlysmalllabeled
datasetsexistforspecifictasksinBCI,whereEEGsignalsareoftencollectedfromasmallnumber
ofparticipants,typicallylessthantensofhoursinduration. Asaresult,thereiscurrentlynosingle
EEGdatasetthatislargeenoughtosupportthetrainingofLEMs. ItremainsproblemsQ1: howto
utilizelarge-scaleunlabeledEEGdata? andQ2: howmuchdataisneededtotrainLEMs?.
2) Diverse configurations of EEG collection. Despite the availability of the international 10-20
systemtoensurestandardizationinEEGtesting,usersmaychoosetocollectdatausingEEGcaps
withdifferentelectrodenumbersorpatchelectrodesbasedontheirpracticalapplicationneeds.Thus,
how to handle the diverse formats of EEG data in order to match the input units of neural Trans-
formersremainsasignificantresearchendeavor.
3) Lack of effective EEG representation learning paradigm. Low signal-to-noise ratio (SNR)
anddifferenttypesofnoisearethegreatestchallenges. Additionally,balancingtemporalandspatial
characteristicsiscrucialforeffectiveEEGrepresentationlearning.Despitetheavailabilityofvarious
deeplearning-basedEEGrepresentationlearningparadigms,suchasCNN,RNN,andGNN,forraw
EEGdata,manyresearchersstillprefertodesignartificialEEGfeaturesduetothesechallenges.
Inthispaper,ourobjectiveistodeviseaversatilelargeEEGmodelthatcanefficientlyhandlediverse
EEGdatasetswithvaryingchannelsandlengths. Byutilizingunsupervisedtrainingonasubstantial
amount of EEG data, we envision the model to possess universal EEG data comprehension capa-
bilities, enabling it to quickly adapt to various EEG downstream tasks. We collected over 2,500
hoursofdiverseEEGdataacrossvarioustasksandformatsfromabout20datasets. Thesedatasets
were primarily obtained from publicly available EEG datasets, as well as our own collected EEG
data. Raw EEG signals were first segmented into EEG channel patches to deal with the issues of
variant electrodes and time length. Vector-quantized neural spectrum prediction is used to train a
semantically rich neural tokenizer to generate neural vocabulary. Specifically, the tokenizer was
trainedbypredictingtheFourierspectrumoftheoriginalsignal. Duringpre-training,partofEEG
patchesaremaskedwhiletheobjectiveoftheneuralTransformeristopredictmaskedtokensfrom
visible patches. We pre-trained three models with varying parameter sizes, ranging from 5.8M to
369M,whicharethelargestmodelsinBCIever,andfine-tunedthemonfourdistincttypesofdown-
stream tasks encompassing both classification and regression. The contributions of this work are
summarizedasfollows:
• Large-scale EEG pre-training. We collected and pre-trained a large-scale neural Transformer
model on more than 2,500 hours of diverse EEG data. As far as we know, this is the first time
suchextensiveandvarieddatasetshavebeenutilizedforEEGpre-training.
• BeingcompatiblewithvariousEEGconfigurations. LaBraMsareunifiedmodelsthatareable
tohandleEEGsignalswithvariouschannelsandtimelengthswiththeassistanceoftheflexible
2

PublishedasaconferencepaperatICLR2024
time
patch
lennahc CP5
TP7
T8
C6
Conv
Group
Norm
GELU
Temporal
Embedding
Temporal Encoder Transformer Encoder
Spatial
Embedding
Q
K
V
LN
LN
Attention Add
&
Norm
Feed
Forward
Add
&
Norm
Output
Input EEG Signals Embedding
Figure 1: The overall architecture of LaBraM, i.e., neural Transformer. All input EEG signals
willfirstbesegmentedintoEEGpatchesthroughafixed-lengthtimewindow,andthenatemporal
encoderwillbeappliedtoeachpatchtoextracttemporalfeatures. Afterward,temporalandspatial
embeddings areadded to thepatch featuresto carry temporaland spatial information. Atlast, the
sequence of embeddings is passed into the Transformer encoder by patch-wise attention to obtain
thefinaloutput.
spatialandtemporalembeddings. Hence,onepre-trainedLaBraMcanadapttoanydownstream
datasetwithdifferentconfigurations.
• Effective EEG representation learning. The utilization of the neural Transformer allows the
modeltoeffectivelycapturebothtemporalandspatialfeaturesofEEGsignalswithvaryingchan-
nelsandlengths, makingitsuitableforawiderangeofdownstreamtasksinEEGanalysis. We
furtherdefineaneuralcodebookthatoffersacompact, versatile, andmeaningfulrepresentation
ofEEGsignals.WeresolveQ1byleveragingthiscodebooktopre-trainLaBraMbymaskedEEG
modeling.Theempiricalperformancedemonstratestheeffectivenessofourproposedmethodand
pavesthewayforfurtherdevelopmentinaligningthiscodebookwithnaturallanguage.
• Comprehensiveexperimentsondownstreamdatasets. WeevaluateourLaBraMsonfourrep-
resentative downstream tasks in BCI, where they surpass all SOTA methods by a large margin.
Additionally, we conduct experiments to answer Q2 by scaling the pre-training data size and
concludetheamountofpre-trainingdatarequiredformodelsofdifferentsizesinSection3.6.
2 METHOD
In this section, we detail the whole framework of LaBraM. We first formulate the multi-channel
EEGsignalsasX ∈RC×T,whereC isthenumberofEEGelectrodes(channels)andT isthetotal
timestamps. The electrode set of X is formulated as C = {c ,c ,...,c }, where C ⊆ C =
X i1 i2 iC X
{c ,c ,...,c }andC istheuniversalsetofchannelsintheinternational10-20system.
1 2 |C|
2.1 MODELARCHITECTURE
WeintroducetheneuralTransformer,ageneralarchitecturefordecodingEEGsignalsthatcandeal
with any input EEG signals with arbitrary number of channels and time length, as illustrated in
Figure1. ThekeyoperationforachievingthisissegmentingtheEEGsignalsintopatches,inspired
by patch embeddings in images (Dosovitskiy et al., 2021). Assume that the timestamp for each
sample is t and the stride is s. X can be segmented into ⌊T−t⌋ + 1 samples, and each sample
s
x∈RC×t. Weuseaw-lengthwindowwithoutoverlaptosegmenteachEEGchannelintopatches,
obtainingx = {x ∈ Rw|j = 1,2,...,C,k = 1,2,...,⌊t⌋}. Thetotalnumberofthepatchesx
cij ,k w
is|x|=C⌊t⌋.
w
TemporalEncoder. AsEEGisofhighresolutioninthetemporaldomain,itisvitaltoextracttem-
poralfeaturesbeforepatch-wiseinteractionbyself-attention. Weemployatemporalencoderwhich
consistsofseveraltemporalconvolutionblockstoencodeeachEEGpatchintoapatchembedding.
Thetemporalconvolutionblockiscomposedofa1-Dconvolutionlayer,agroupnormalizationlayer
(Wu & He, 2018), and a GELU activation function (Hendrycks & Gimpel, 2016). We denote the
outputpatchembeddingsfromthetemporalencoderas
t
e={e ∈Rd|j =1,2,...,C,k =1,2,...,⌊ ⌋}, (1)
cij ,k w
3

PublishedasaconferencepaperatICLR2024
......
| Neural Tokenizer Training | Neural Codebook |     |     |     |     |     |     |
| ------------------------- | --------------- | --- | --- | --- | --- | --- | --- |
-norm
|     |           |     | Lookup | Replace |     |                | Fourier Spectrum |
| --- | --------- | --- | ------ | ------- | --- | -------------- | ---------------- |
|     |           |     | 69 729 | 4       |     |                |                  |
| CP5 | Tokenizer |     |        |         |     |                |                  |
| TP7 | Neural    |     | 748 98 | 460     |     | Decoder Neural | Amplitude        |
-norm
| T8  |     |     | 114 603 | 139 |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- |
C6
|     |     |     | 514 7 | 53  |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- |
Phase
|     | M M |     |     |     |     | 69  | 4   |
| --- | --- | --- | --- | --- | --- | --- | --- |
CP5
|     |     | Temporal & Spatial Embedding |     |     |     | 98  |     |
| --- | --- | ---------------------------- | --- | --- | --- | --- | --- |
| TP7 | M   |                              |     |     |     |     |     |
Token Prediction Head
T8 M M Temporal Encoder Transformer Block 1 Transformer Block 2 Transformer Block L 114 139
| C6  | M   |     |     |     |     |     | 53  |
| --- | --- | --- | --- | --- | --- | --- | --- |
Mask
......
|     | M   |     |     |     |     | 729 |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
CP5
|     |     |     |     |     |     | 748 | 460 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TP7 | M M |     |     |     |     |     |     |
603
| T8  | M   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C6  | M M |     |     |     |     | 514 | 7   |
Symmetric Mask
LaBraMPre-training
Figure 2: Overview of neural tokenizer training and LaBraM pre-training. Up: We train a neural
tokenizer to discretize EEG signals into discrete neural tokens by reconstructing the Fourier spec-
trum. Down: Duringpre-training,partofEEGpatchesaremaskedwhiletheobjectiveistopredict
maskedtokensfromvisiblepatches.
wheredisthedimensionoftheembeddings.
Temporal & Spatial Embedding. In order to enable the model to be aware of the tempo-
ral and spatial information of patch embeddings, we initialize a temporal embedding list TE =
{te ,te ,...,te }andaspatialembeddinglistSE = {se ,se ,...,se },bothofwhichared-
| 1 2 | tmax |     |     | 1 2 | |C| |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- |
dimensionandaresetlearnableduringtraining. Notethattmaxisthehyperparameterdetermining
themaximumnumberoftimepatchesand⌊t⌋ ≤ tmax. Meanwhile,foreachchannelc ,wecan
i
w
finditscorrespondingspatialembeddingse i inthespatialembeddinglistSE. Thus,givenonear-
bitraryoutputembeddinge inEquation1fromthetemporalencoder,weaddthecorresponding
|     | cij ,k |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- |
temporalandspatialembeddingstoit:
t
|     | {e +te | +se  | |j =1,2,...,C,k | =1,2,...,⌊ | ⌋}, |     | (2) |
| --- | ------ | ---- | --------------- | ---------- | --- | --- | --- |
|     | cij ,k | k ij |                 |            | w   |     |     |
wheretemporalandspatialembeddingsactasabsolutepositionencoding.
Transformer Encoder. Finally, the sequence of embeddings will be directly fed into the Trans-
former encoder (Vaswani et al., 2017). To make the training of Transformer more stable and effi-
cient,weincorporatesomemodifications(Dehghanietal.,2023). First,weaddlayernormalization
tothequeriesandkeysbeforethedot-productattentionmechanism,whichavoidsover-largevalues
inattentionlogits:
LN(Q)LN(K)T
|     | Attention(Q,K,V)=softmax( |     |     | √   | )V, |     | (3) |
| --- | ------------------------- | --- | --- | --- | --- | --- | --- |
d
head
whered isthedimensionofoneheadinthemulti-headattentionandLNdenotesthelayerNorm
head
(Baetal.,2016). Next,weomitthebiasterminQKVcomputations,whichacceleratesthetraining
without performance degradation. For downstream tasks, we use average pooling on the output
embeddingsfollowedbytask-specificpredictionheads.
4

PublishedasaconferencepaperatICLR2024
2.2 NEURALTOKENIZERTRAINING
Prior to pre-training LaBraM through masking and prediction, we need to tokenize the EEG into
discrete tokens. We propose the vector-quantized neural spectrum prediction, which is trained by
predicting the Fourier spectrum, as shown in Figure 2. The key components are the neural tok-
enizer which encodes EEG samples into patch representations and the neural decoder which de-
codes the Fourier spectrum from neural embeddings. The idea is basically inspired by VQ-VAE
(VanDenOordetal.,2017)whichencodesimagesintodiscretelatentrepresentations.
NeuralTokenizer. WedefineaneuralcodebookV = {v |i = 1,...,K} ∈ RK×D,whereK isthe
i
numberofthediscreteneuralembeddingsandD isthedimensionalityofeachembedding. Given
anEEGsignalsamplex,theneuraltokenizerwhosebackboneisjustdescribedinSection2.1first
C⌊t⌋.
encodeittopatchrepresentationsp = {p |i = 1,...,N},whereN = Afterthat,weutilize
|     |     |     |     |     |     | i   |     | w   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a quantizer to quantize all the patch representations into the neural codebook embeddings. The
codebooklooksupthenearestneighborofeachpatchp intheneuralcodebookV. Thisprocedure
i
canbeformulatedas
|     |     |     |     | z   | i =argmin∥ℓ | 2 (p i )−ℓ | 2 (v i )∥ | 2 , |     | (4) |
| --- | --- | --- | --- | --- | ----------- | ---------- | --------- | --- | --- | --- |
j
where ℓ represents ℓ normalization and z is the quantized vector after the quantizer. This is
|     | 2   |     | 2   |     |     | i   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
equivalent to finding the closest neural embedding by cosine similarity and such ℓ normalization
2
improvesthecodebookutilization(Pengetal.,2022).
Fourier Spectrum Prediction. Unlike images that are of high signal-to-noise ratio, EEG signals
are of low signal-to-noise ratio and have characteristics of apparent stochasticity, nonstationarity,
and nonlinearity nature, which make it hard to reconstruct the original signals well (Moss et al.,
2004).Inourpreviousexperiments,thelossfailstoconvergewhiledirectlyreconstructingrawEEG
signals. Instead, the frequency and phase distribution from the Fourier spectrum of EEG signals
reveals the underlying neurophysiological activities of the brain (Wu et al., 2022). Therefore, we
propose to reconstruct the amplitude and phase from discrete neural tokens for training the neural
tokenizerandneuraldecoder. ForanEEGpatchx = [x[1],x[2],...,x[w]]ofchannelcandtime
c,k
kinasamplex,weapplytheDiscreteFourierTransform(DFT)asfollows
|     |     |     |     |     |     | (cid:88) N | 2πj |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
x˜m
|     |     |     |     |     | =   | x[n]exp(− | mn), |     |     | (5) |
| --- | --- | --- | --- | --- | --- | --------- | ---- | --- | --- | --- |
|     |     |     |     |     | c,k |           | N    |     |     |     |
n=1
wherem∈[1,N]andj istheimaginaryunit. WerewriteEquation5usingEuler’sformulaas
N
|     |     |     |     | (cid:88) |          | 2π            |     | 2π   |     |     |
| --- | --- | --- | --- | -------- | -------- | ------------- | --- | ---- | --- | --- |
|     |     |     | x˜m | =        | x[n]cos( | mn)−jx[n]sin( |     | mn). |     | (6) |
c,k
|     |     |     |     |     |     | N   |     | N   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n=1
Notethatx˜m indicatesthespectrumofthesequenceatfrequencyω = 2πm. Consequently,the
|     | c,k |     |     |     |     |     |     | m N |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
amplitudeandphasecanbecalculatedas
(cid:113)
|     |     |     |     | Am  | =   | Re(x˜m )2+Im(x˜m | )2, |     |     | (7) |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- |
|     |     |     |     |     |     | c,k              | c,k |     |     |     |
|     |     |     |     |     |     | Im(x˜m           | )   |     |     |     |
|     |     |     |     |     | ϕm  |                  | c,k |     |     |     |
|     |     |     |     |     |     | =arctan(         |     | ),  |     | (8) |
Re(x˜m )
c,k
whereReandImstandfortherealandimaginarypartsofacomplexnumber. Itisworthwhileto
mention that we adopt z-score normalization to normalize Am and ϕm within a sample for stable
convergence.
After being tokenized by the quantizer, the normalized discrete neural embeddings {ℓ (v )|i =
2 zi
1,...,N}arepassedintotheneuraldecoderthatcomprisesseveralTransformerblocks. Theoutput
representations are aggregated by average pooling followed by two specific prediction heads to
regressthespectrumamplitudeoA andphaseoϕ,respectively. Themeansquarederror(MSE)loss
isutilizedtoguidetheprediction. Ultimately,thetotallossfortrainingthevector-quantizedneural
spectrumpredictionisdefinedas
N
|     | (cid:88)(cid:88) | ∥oA−A | ∥2+∥oϕ−ϕ |     | ∥2+∥sg(ℓ |             |         | )∥2+∥ℓ        |         | ))∥2, |
| --- | ---------------- | ----- | -------- | --- | -------- | ----------- | ------- | ------------- | ------- | ----- |
| L T | =                |       | i        |     | i        | 2 (p i ))−ℓ | 2 (v zi | 2 (p i )−sg(ℓ | 2 (v zi | (9)   |
|     |                  | i     | 2        | i   | 2        |             |         | 2             |         | 2     |
x∈Di=1
5

PublishedasaconferencepaperatICLR2024
whereDisallEEGdataandsgrepresentsthestop-gradientoperationthatisdefinedasanidentity
attheforwardpassandhaszerogradients. Tomakethecodebookupdatemorestable,weemploy
theexponentialmovingaveragestrategy(VanDenOordetal.,2017).
2.3 PRE-TRAININGLABRAM
Masked EEG Modeling. To enforce LaBraM learning generic representations with tremendous
EEGdata, weproposemaskedEEGmodeling. ThewholeprocedureispresentedinFigure2. As
formulatedinSection2.1,givenanEEGsamplex,thetemporalencoderfirsttransformsittopatch
embeddings e = {e |i = 1,...,N}. We randomly generate a mask M = {m |i = 1,...,N}
i i
where m ∈ {0,1} with r proportion of m is 1. After that, we replace the masked patches of x
i
with the learnable mask token e ∈ Rd. The corrupted EEG patches can be denoted as eM =
M
{e : m = 0|i = 1,...,N}∪{e : m = 1|i = 1,..,N}, whichwillbeaddedbytemporaland
i i M i
spatialembeddings,andthenfedintoTransformerencoder. Wedenotetheoutputhiddenvectorsas
h = {h |i = 1,...,N},whichareusedtopredictthecorrespondingneuraltokensthroughalinear
i
classifier:
p(v′|eM)=softmax(Linear(h)). (10)
Ourobjectivetraininglossis
(cid:88) (cid:88)
L =− logp(v |eM). (11)
M i
x∈Dmi=1
Symmetric Masking. We further propose a symmetric masking strategy to improve training effi-
ciency. WecalculatetheinverseofthegeneratedmaskM,obtainingM˜ = {∼ m |i = 1,...,N}.
i
Similarly, we use the new mask M˜ to perform the masked EEG modeling, obtaining the masked
EEG prediction loss Lsym. The motivation is from two aspects: 1) Since we introduce the neural
M
tokenizer, there will be an extra computation overhead, i.e., one forward pass for each EEG sam-
ple. Thus,thesymmetricmaskingreusesthesamediscreterepresentations,thusimprovingtraining
efficiency. 2) The symmetric masking provides more masking perspectives in one batch, increas-
ing the data divergency. This simple strategy boosts downstream performance as demonstrated in
AppendixI.
Finally,theoveralltrainingobjectiveforpre-trainingLaBraMis
L=L +Lsym. (12)
M M
3 EXPERIMENTS
3.1 EVALUATIONDATASETS
WesystematicallyevaluateourLaBraMonthefollowingdownstreamdatasets:
• TUAB (abnormal detection) (Obeid & Picone, 2016): A corpus of EEGs which are 23-channel
and sampled at 256 Hz. All data have been annotated as normal or abnormal. There are total
409,45510-secondsamplesthatweuseforbinaryclassificationtopredictnormal/abnormal.
• TUEV(eventtypeclassification)(Obeid&Picone,2016): ThiscorpusisasubsetofTUEGthat
containsannotationsofEEGsegmentsasoneofsixclasses: (1)spikeandsharpwave(SPSW),
(2)generalizedperiodicepileptiformdischarges(GPED),(3)periodiclateralizedepileptiformdis-
charges (PLED), (4) eye movement (EYEM), (5) artifact (ARTF) and (6) background (BCKG).
TheEEGsignalscontain23channelsat256Hzandaresegmentedinto112,4915-secondsam-
ples.
MoreexperimentalresultsonotherBCItaskscanbefoundinAppendixF.
3.2 EXPERIMENTSETUP
Model Variants. We devise three different configurations of LaBraM: LaBraM-Base, LaBraM-
Large,andLaBraM-Huge. Thenumberofparametersis5.8MforLaBraM-Base,46MforLaBraM-
Large, and 369M for LaBraM-Huge, respectively, which is increased by enlarging the depth of
6

PublishedasaconferencepaperatICLR2024
the Transformer encoder and hidden sizes. More details of the architecture settings are listed in
AppendixC.Unlessotherwisespecified,theresultsarefromLaBraM-Baseinthispaper.
Thetimewindowwofapatchissetto200(1second). Toensurestablecomputingresourceusage,
thenumberofpatches(sequencelength)islimitedto256. Thatmeans,forexample,thetimelength
ofEEGwith64(32)channelsissetto4(8)seconds. Asforthewindowstride(datastride),itisset
to4secondsinordertocoveralltrainingdataaswellasboostthetrainingspeed.
Pre-training & Fine-tuning. For pre-training LaBraM and the vector-quantized neural spectrum
prediction, we collect a total time of over 2,500 hours from public datasets and our self-collected
dataasdescribedinAppendixD.Notethatthefourdownstreamdatasetsareexcludedfromthepre-
training datasets. For the data splitting of TUAB and TUEV, we strictly follow the same strategy
as BIOT (Yang et al., 2023a) to compare all methods fairly. Specifically, as the training and test
separation is provided by the datasets, we divide the training patients into training and validation
groups by 80% and 20%, respectively. We employ binary cross-entropy (BCE) loss for TUAB
(binary classification) and cross-entropy loss for TUEV (multi-class classification), respectively.
OurexperimentsareconductedoneightA800GPUsbyPython3.11.4andPyTorch2.0.1+CUDA
11.8. The best models are trained based on the training set, selected from the validation set, and
finallyevaluatedonthetestset.Wereporttheaverageandstandarddeviationvaluesonfivedifferent
randomseedstoobtaincomparableresults. (seeAppendixCformoredetailedhyperparameters)
Preprocessing. Weonlyemployverylittleofthenecessarypreprocessing. WefirstfiltertheEEG
signalsbetween0.1Hzand75Hztoremovelow-frequencynoise. Then,anotchfilterof50Hzis
appliedtoavoidpower-lineinterference. Finally,allEEGsignalsareresampledto200Hz. Asthe
rangeofEEGvalueistypicallybetween-0.1mVto0.1mV,wenormalizeitbysettingtheunitto
0.1mVtoguaranteethevaluemainlybetween-1to1.
Baselines&Metrics. ThebaselinesarefromYangetal.(2023a),wherewechoosethebestresults
tocomparewith.Weusethefollowingmetricsforcomparison:1)BalancedAccuracy:theaverage
ofrecalloneachclass,whichisutilizedforbothbinaryandmulti-classclassification. 2)AUC-PR:
areaundertheprecision-recallcurveforbinaryclassification. 3)AUROC:areaunderthereceiver
operatingcharacteristiccurve,whichisusedforbinaryclassificationaswell. 4)Cohen’sKappa: a
measureofagreementbetweencategoricalvariablesXandY,whichiscalculatedfromtheobserved
and expected frequencies on the diagonal of a square contingency table. It is used for multi-class
classification. 5) Weighted F1: A harmonic mean of the precision and recall, where the relative
contribution of precision and recall to the F1 score are equal. We use it to evaluate multi-class
classification. WesetAUROCasthemonitorscoreforbinaryclassificationandCohen’sKappaas
themonitorscoreformulti-classclassification.
3.3 PRE-TRAININGVISUALIZATION
  
  
 
                
 ( S R F K V
 V V R /
 3 U H  W U D L Q L Q J  / R V V
 % D V H
   
 / D U J H
 + X J H
   
   
                
 ( S R F K V
 \ F D U X F F $
 0 D V N H G  ( ( *  0 R G H O L Q J  $ F F X U D F \
 % D V H
 / D U J H
 + X J H
Figure3: Thepre-traininglosscurveandmaskedEEGmodelingaccuracycurve.
Figure3comparestheconvergencecurvesofthetotalpre-traininglossandmaskedEEGmodeling
accuracy between the base, large, and huge models. We observe that a larger model with more
parameterscanconvergetoasmallerlossandhigheraccuracy. Notably,thelossofthehugemodel
seemstohaveanobviousdownwardtrendwhiletheaccuracytendstoincreaseifwetrainitlonger.
Thisobservationsuggestsscalingupthemodelsizehasthepotentialtoobtainbetterperformance.
7

PublishedasaconferencepaperatICLR2024
3.4 COMPARISONWITHSTATE-OF-THE-ART
Table1andTable2presenttheresultsofstate-of-the-artbaselinesaswellasLaBraMfromTUAB
andTUEV.TheresultsdemonstratethatourLaBraM-Basemodeloutperformedallbaselinesonvar-
iousevaluationmetricsforbothtasks. Particularlyinthemorechallengingmulti-classclassification
taskofTUEV,ourmodelachievedasignificantimprovementinperformance.Inourownmodel,we
observed that as the number of model parameters increased, the LaBraM-Huge model performed
the best, followed by the LaBraM-Large model and then the LaBraM-Base model. We attribute
this good performance to the increase in pre-training data volume and model parameters. We be-
lieve that with sufficient data volume, large-scale EEG models can learn more generalizable EEG
patterns,leadingtoimprovedperformanceonawiderangeofdownstreamtasksinEEGanalysis.
Table1: TheresultsofdifferentmethodsonTUAB.
| Methods |     | ModelSize | BalancedAccuracy | AUC-PR | AUROC |
| ------- | --- | --------- | ---------------- | ------ | ----- |
SPaRCNet(Jingetal.,2023) 0.79M 0.7896±0.0018 0.8414±0.0018 0.8676±0.0012
ContraWR(Yangetal.,2023b) 1.6M 0.7746±0.0041 0.8421±0.0104 0.8456±0.0074
CNN-Transformer(Pehetal.,2022) 3.2M 0.7777±0.0022 0.8433±0.0039 0.8461±0.0013
FFCL(Lietal.,2022) 2.4M 0.7848±0.0038 0.8448±0.0065 0.8569±0.0051
ST-Transformer(Songetal.,2021) 3.5M 0.7966±0.0023 0.8521±0.0026 0.8707±0.0019
|                       |     |      | 0.7959±0.0057 | 0.8792±0.0023 | 0.8815±0.0043 |
| --------------------- | --- | ---- | ------------- | ------------- | ------------- |
| BIOT(Yangetal.,2023a) |     | 3.2M |               |               |               |
| LaBraM-Base           |     | 5.8M | 0.8140±0.0019 | 0.8965±0.0016 | 0.9022±0.0009 |
| LaBraM-Large          |     | 46M  | 0.8226±0.0015 | 0.9130±0.0005 | 0.9127±0.0005 |
| LaBraM-Huge           |     | 369M | 0.8258±0.0011 | 0.9204±0.0011 | 0.9162±0.0016 |
Table2: TheresultsofdifferentmethodsonTUEV.
| Methods |     | ModelSize | BalancedAccuracy | Cohen’sKappa | WeightedF1 |
| ------- | --- | --------- | ---------------- | ------------ | ---------- |
SPaRCNet(Jingetal.,2023) 0.79M 0.4161±0.0262 0.4233±0.0181 0.7024±0.0104
ContraWR(Yangetal.,2023b) 1.6M 0.4384±0.0349 0.3912±0.0237 0.6893±0.0136
CNN-Transformer(Pehetal.,2022) 3.2M 0.4087±0.0161 0.3815±0.0134 0.6854±0.0293
FFCL(Lietal.,2022) 2.4M 0.3979±0.0104 0.3732±0.0188 0.6783±0.0120
ST-Transformer(Songetal.,2021) 3.5M 0.3984±0.0228 0.3765±0.0306 0.6823±0.0190
BIOT(Yangetal.,2023a) 3.2M 0.5281±0.0225 0.5273±0.0249 0.7492±0.0082
| LaBraM-Base  |     | 5.8M | 0.6409±0.0065 | 0.6637±0.0093 | 0.8312±0.0052 |
| ------------ | --- | ---- | ------------- | ------------- | ------------- |
| LaBraM-Large |     | 46M  | 0.6581±0.0156 | 0.6622±0.0136 | 0.8315±0.0040 |
| LaBraM-Huge  |     | 369M | 0.6616±0.0170 | 0.6745±0.0195 | 0.8329±0.0086 |
3.5 PRE-TRAININGWITH/WITHOUTDOWNSTREAMDATASETS
Duringthepre-trainingprocess,wehopethatthemodelcanlearngeneralEEGrepresentationsthat
arenotspecifictoanyparticulartask.Althoughnolabeldataisusedduringthepre-trainingprocess,
|        |  7 8 $ % |     |        |  7 8 ( 9 |     |
| ------ | -------- | --- | ------ | -------- | --- |
|     |          |     |     |          |     |
 S U H  W U D L Q  Z  R  ' '  S U H  W U D L Q  Z  R  ' '
 S U H  W U D L Q  Z   ' '  S U H  W U D L Q  Z   ' '
|                                 |              |            |                                 |                            |                        |
| ---------------------------------- | ------------ | ---------- | ---------------------------------- | -------------------------- | ---------------------- |
|                                 |              |            |                                 |                            |                        |
|                                 |              |            |                                 |                            |                        |
|                                 |              |            |                                 |                            |                        |
|                                 |              |            |                                 |                            |                        |
|  % D O D Q F H G  $ F F X U D F \ |  $ 8 &  3 5 |  $ 8 5 2 & |  % D O D Q F H G  $ F F X U D F \ |  & R K H Q 
 V  . D S S D |  : H L J K W H G  )  |
Figure4: Acomparisonofthemodel’sperformanceontheTUABandTUEVdatasetswhenincor-
poratingthemselvesintothepre-trainingprocessornot.
8

PublishedasaconferencepaperatICLR2024
to eliminate the influence of the pretraining data on downstream tasks, we compared the results
withorwithoutincorporatingthedownstreamtaskdatasetintothepre-trainingprocessornot. Itis
notedthattherecordingsofTUABandTUEVaredisjointfromrecordingsofpre-trainingdatasets.
AsFigure4illustrates,theperformanceofthemodelonthedownstreamtaskwasnotsignificantly
affectedbywhetherornottoincorporatethedownstreamtaskdatasetsintothemodel’spre-training
process.ThisdemonstratesthatourmodelhasthecapabilitytolearnuniversalEEGrepresentations,
andprovidesguidanceforthecollectionofmoreEEGdatainthefuture. Inotherwords,wedonot
needtoexpendasignificantamountofeffortonlabelingEEGdataduringthepre-trainingprocess.
3.6 SCALINGDATASIZE
Althoughwehavecollectedapproximately2,500hoursofEEGdata,itisstillrelativelysmallcom-
paredtothesamplesizeinnaturallanguageprocessingandimageprocessing. WeanswerQ2about
thedemandfordatasizetotrainLaBraMswithdifferentsizesbyscalingthepre-trainingdatasize.
AsillustratedinFigure5,theperformanceoftheBasemodelwith500hoursoftrainingexceedsthat
ofthe2500-hourmodelonTUAB,whileapproachingover90%ofthe2500-hourperformanceon
TUEV.FortheLargemodel, performancegenerallyimproveswithincreaseddatavolume, though
the growth rate slows after 1000 hours. In contrast, the Huge model exhibits a noticeable upward
trendinperformanceasdatasizecontinuestoexpand.Therefore,webelievethatwithfurtherexpan-
sionofthedataset,ourmodelcanachievebetterperformance. ThequestionofhowmuchEEGdata
is required for pre-training a large EEG model is undoubtedly an important issue worth exploring
inthisfield. Nevertheless, 2,500hoursisnottheanswertothisquestionatleast. Ourobservation
basicallyfollowsthescalinglaw(Kaplanetal.,2020),fromwhichwededucethattheHugemodel
wouldcontinuetoperformbetterwiththedatasizeontheorderofatleasttenthousandhours.
|          |  7 8 $ %   % D O D Q F H G  $ F F X U D F \  |          |  7 8 $ %   $ 8 &  3 5  |            |  7 8 $ %   $ 8 5 2 &  |
| -------- | ------------------------------------------------ | -------- | -------------------------- | ---------- | ------------------------ |
|      |                                                  |          |                            |        |                          |
|          |  % D V H                                         |      |  % D V H                   |  % D V H   |                          |
|      |  / D U J H                                       |          |  / D U J H                 |  / D U J H |                          |
|          |  + X J H                                         |          |  + X J H                   |  + X J H   |                          |
|      |                                                  |      |                            |        |                          |
    
|      |     |      |     |      |     |
| -------- | --- | -------- | --- | -------- | --- |
    
|      |     |      |     |      |     |
| -------- | --- | -------- | --- | -------- | --- |
    
|     |     |      |     |      |     |
| --- | --- | -------- | --- | -------- | --- |
                                                                                                  
|        |  7 L P H   K                                  |        |  7 L P H   K                          |                   |  7 L P H   K                      |
| ------ | ------------------------------------------------ | ------ | ---------------------------------------- | ----------------- | ------------------------------------ |
|        |  7 8 ( 9   % D O D Q F H G  $ F F X U D F \  |        |  7 8 ( 9   & R K H Q 
 V  . D S S D  |                   |  7 8 ( 9   : H L J K W H G  )   |
|        |                                                  |     |                                          |               |                                      |
|        |  % D V H                                         |        |  % D V H                                 |  % D V H          |                                      |
|        |  / D U J H                                       |        |  / D U J H                               |  / D U J H        |                                      |
|     |  + X J H                                         |     |  + X J H                                 |       + X J H |                                      |
|     |                                                  |        |                                          |               |                                      |
   
    
|     |     |     |     |     |     |
| ------ | --- | ------ | --- | --- | --- |
    
|     |     |     |     |     |     |
| ------ | --- | ------ | --- | --- | --- |
                                                                                                  
|     |  7 L P H   K  |     |  7 L P H   K  |     |  7 L P H   K  |
| --- | ---------------- | --- | ---------------- | --- | ---------------- |
Figure5: AcomparisonoftheperformanceoftheBasemodel, Largemodel, andHugemodelon
theTUABandTUEVdatasetsasthepre-trainingdataincreases.
4 CONCLUSION
ThispaperproposesaLargeBrainModel(LaBraM)thatlearnsuniversalembeddingsthroughunsu-
pervisedpre-trainingonover2,500hoursofdiverseEEGdata. TheLaBraMiscapableofhandling
diverseEEGdatasetsduetothesegmentationofrawEEGsignalsintochannelpatchesandtheuse
of vector-quantized neural spectrum prediction to generate a rich semantic tokenizer during pre-
training. Additionally,theneuralTransformerarchitectureenableseffectiverepresentationlearning
ofbothtemporalandspatialfeaturesofEEGsignals,makingitsuitableforawiderangeofdown-
streamtasksinEEGanalysis. TheLaBraMwasvalidatedonmultipledownstreamtasks,including
abnormaldetection,eventtypeclassification,emotionrecognition,andgaitprediction. Ourexperi-
mentsshowthattheLaBraMoutperformsallSOTAmethodsintheirrespectivefields.Intheend,we
hopeourworkcanhaveimplicationsforfuturedevelopmentsinEEG-baseddeeplearningmodels
withimprovedperceptualcapabilitiesandgeneralizability.
9

PublishedasaconferencepaperatICLR2024
ACKNOWLEDGMENTS
ThisworkwassupportedinpartbygrantsfromSTI2030-MajorProjects+2022ZD0208500,Shang-
hai Municipal Science and Technology Major Project (Grant No. 2021SHZD ZX), Medical-
Engineering Interdisciplinary Research Foundation of Shanghai Jiao Tong University “Jiao Tong
Star” Program (YG2023ZD25), and GuangCi Professorship Program of RuiJin Hospital Shanghai
JiaoTongUniversitySchoolofMedicine.
REFERENCES
Khald Ali I Aboalayon, Miad Faezipour, Wafaa S Almuhammadi, and Saeid Moslehpour. Sleep
stage classification using EEG signal analysis: a comprehensive survey and new investigation.
Entropy,18(9):272,2016.
Syed Umar Amin, Mansour Alsulaiman, Ghulam Muhammad, Mohamed Amine Mekhtiche, and
MShamimHossain. DeepLearningforEEGmotorimageryclassificationbasedonmulti-layer
CNNsfeaturefusion. FutureGenerationComputerSystems,101:542–554,2019.
Jimmy Lei Ba, Jamie Ryan Kiros, and Geoffrey E Hinton. Layer normalization. arXiv preprint
arXiv:1607.06450,2016.
AlexeiBaevski, YuhaoZhou, AbdelrahmanMohamed, andMichaelAuli. wav2vec2.0: Aframe-
work for self-supervised learning of speech representations. Advances in Neural Information
ProcessingSystems,33:12449–12460,2020.
Hubert Banville, Omar Chehab, Aapo Hyva¨rinen, Denis-Alexander Engemann, and Alexandre
Gramfort.UncoveringthestructureofclinicalEEGsignalswithself-supervisedlearning.Journal
ofNeuralEngineering,18(4):046020,2021.
Hangbo Bao, Li Dong, Songhao Piao, and Furu Wei. BEit: BERT pre-training of image trans-
formers. In International Conference on Learning Representations, 2022. URL https:
//openreview.net/forum?id=p-BhZSz59o4.
Wouter Biesmans, Neetha Das, Tom Francart, and Alexander Bertrand. Auditory-inspired speech
envelope extraction methods for improved EEG-based auditory attention detection in a cocktail
party scenario. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 25(5):
402–412,2016.
BenjaminBlankertz,GuidoDornhege,MatthiasKrauledat,Klaus-RobertMu¨ller,andGabrielCurio.
The non-invasive berlin brain–computer interface: fast acquisition of effective performance in
untrainedsubjects. NeuroImage,37(2):539–550,2007.
Poomipat Boonyakitanont, Apiwat Lek-Uthai, Krisnachai Chomtho, and Jitkomut Songsiri. A re-
viewoffeatureextractionandperformanceevaluationinepilepticseizuredetectionusingEEG.
BiomedicalSignalProcessingandControl,57:101702,2020.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal,
ArvindNeelakantan,PranavShyam,GirishSastry,AmandaAskell,etal. Languagemodelsare
few-shotlearners. AdvancesinNeuralInformationProcessingSystems,33:1877–1901,2020.
G Buckwalter, S Chhin, S Rahman, I Obeid, and J Picone. Recent advances in the TUH EEG
corpus: improving the interrater agreement for artifacts and epileptiform events. In 2021 IEEE
SignalProcessinginMedicineandBiologySymposium(SPMB),pp.1–3.IEEE,2021.
MarkChen,AlecRadford,RewonChild,JeffreyWu,HeewooJun,DavidLuan,andIlyaSutskever.
Generativepretrainingfrompixels. InInternationalConferenceonMachineLearning,pp.1691–
1703.PMLR,2020.
Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek, Justin
Gilmer, Andreas Peter Steiner, Mathilde Caron, Robert Geirhos, Ibrahim Alabdulmohsin,
Rodolphe Jenatton, Lucas Beyer, Michael Tschannen, Anurag Arnab, Xiao Wang, Carlos
Riquelme Ruiz, Matthias Minderer, Joan Puigcerver, Utku Evci, Manoj Kumar, Sjoerd Van
10

PublishedasaconferencepaperatICLR2024
Steenkiste, Gamaleldin Fathy Elsayed, Aravindh Mahendran, Fisher Yu, Avital Oliver, Fantine
Huot, Jasmijn Bastings, Mark Collier, Alexey A. Gritsenko, Vighnesh Birodkar, Cristina Nader
Vasconcelos, Yi Tay, Thomas Mensink, Alexander Kolesnikov, Filip Pavetic, Dustin Tran,
Thomas Kipf, Mario Lucic, Xiaohua Zhai, Daniel Keysers, Jeremiah J. Harmsen, and Neil
Houlsby. Scaling vision transformers to 22 billion parameters. In Andreas Krause, Emma
Brunskill,KyunghyunCho,BarbaraEngelhardt,SivanSabato,andJonathanScarlett(eds.),Pro-
ceedings of the 40th International Conference on Machine Learning, volume 202 of Proceed-
ings of Machine Learning Research, pp. 7480–7512. PMLR, 23–29 Jul 2023. URL https:
//proceedings.mlr.press/v202/dehghani23a.html.
PaoloDetti,GiampaoloVatti,andGaraziZabaloManriquedeLara. Eegsynchronizationanalysis
forseizureprediction: Astudyondataofnoninvasiverecordings. Processes,8(7):846,2020.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of deep
bidirectionaltransformersforlanguageunderstanding. arXivpreprintarXiv:1810.04805,2018.
AlexeyDosovitskiy,LucasBeyer,AlexanderKolesnikov,DirkWeissenborn,XiaohuaZhai,Thomas
Unterthiner,MostafaDehghani,MatthiasMinderer,GeorgHeigold,SylvainGelly,JakobUszko-
reit, and Neil Houlsby. An Image is Worth 16x16 Words: Transformers for Image Recogni-
tion at Scale. In International Conference on Learning Representations, 2021. URL https:
//openreview.net/forum?id=YicbFdNTTy.
Xiao Gu, Jinpei Han, Guang-Zhong Yang, and Benny Lo. Generalizable Movement Intention
Recognition with Multiple Heterogeneous EEG Datasets. In 2023 IEEE International Confer-
enceonRoboticsandAutomation(ICRA),pp.9858–9864,2023. doi:10.1109/ICRA48891.2023.
10160462.
Jinpei Han, Xiaoxi Wei, and A Aldo Faisal. EEG Decoding for Datasets with Heterogenous
Electrode Configurations using Transfer Learning Graph Neural Networks. arXiv preprint
arXiv:2306.13109,2023.
KaimingHe, XinleiChen, SainingXie, YanghaoLi, PiotrDolla´r, andRossGirshick. Maskedau-
toencodersarescalablevisionlearners. InProceedingsoftheIEEE/CVFconferenceoncomputer
visionandpatternrecognition,pp.16000–16009,2022.
YongtianHe,TrieuPhatLuu,KevinNathan,ShoNakagome,andJoseLContreras-Vidal. Amobile
brain-body imaging dataset recorded during treadmill walking with a brain-computer interface.
ScientificData,5(1):1–10,2018.
Dan Hendrycks and Kevin Gimpel. Gaussian error linear units (gelus). arXiv preprint
arXiv:1606.08415,2016.
Wei-BangJiang,Li-MingZhao,PingGuo,andBao-LiangLu. DiscriminatingSurpriseandAnger
fromEEGandEyeMovementswithaGraphNetwork. In2021IEEEInternationalConference
on Bioinformatics and Biomedicine (BIBM), pp. 1353–1357, 2021. doi: 10.1109/BIBM52615.
2021.9669637.
Wei-BangJiang,Xuan-HaoLiu,Wei-LongZheng,andBao-LiangLu. MultimodalAdaptiveEmo-
tionTransformerwithFlexibleModalityInputsonANovelDatasetwithContinuousLabels. In
Proceedingsofthe31stACMInternationalConferenceonMultimedia,MM’23,pp.5975–5984,
NewYork,NY,USA,2023.AssociationforComputingMachinery. ISBN9798400701085. doi:
10.1145/3581783.3613797. URLhttps://doi.org/10.1145/3581783.3613797.
JinJing,WendongGe,ShendaHong,MartaBentoFernandes,ZhenLin,ChaoqiYang,SungtaeAn,
AaronFStruck,AlineHerlopian,IoannisKarakis,etal. Developmentofexpert-levelclassifica-
tionofseizuresandrhythmicandperiodicpatternsduringeeginterpretation.Neurology,100(17):
e1750–e1762,2023.
Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B Brown, Benjamin Chess, Rewon Child,
Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language
models. arXivpreprintarXiv:2001.08361,2020.
11

PublishedasaconferencepaperatICLR2024
Diederik P. Kingma and Max Welling. Auto-Encoding Variational Bayes. In 2nd International
Conference on Learning Representations, ICLR 2014, Banff, AB, Canada, April 14-16, 2014,
ConferenceTrackProceedings,2014.
Louis Korczowski, Martine Cederhout, Anton Andreev, Gre´goire Cattan, Pedro Luiz Coelho Ro-
drigues, Violette Gautheret, and Marco Congedo. Brain Invaders calibration-less P300-based
BCIwithmodulationofflashdurationDataset(bi2015a).Researchreport,GIPSA-lab,July2019.
URLhttps://hal.science/hal-02172347.
DemetresKostas,StephaneAroca-Ouellette,andFrankRudzicz. BENDR:usingtransformersand
acontrastiveself-supervisedlearningtasktolearnfrommassiveamountsofEEGdata. Frontiers
inHumanNeuroscience,15:653659,2021.
VernonJLawhern,AmeliaJSolon,NicholasRWaytowich,StephenMGordon,ChouPHung,and
BrentJLance. EEGNet:acompactconvolutionalneuralnetworkforEEG-basedbrain–computer
interfaces. JournalofNeuralEngineering,15(5):056013,2018.
HongliLi,ManDing,RonghuaZhang,andChunboXiu. MotorimageryEEGclassificationalgo-
rithmbasedonCNN-LSTMfeaturefusionnetwork. BiomedicalSignalProcessingandControl,
72:103342,2022.
RuiLi,Le-DianLiu,andBao-LiangLu. DiscriminationofDecisionConfidenceLevelsfromEEG
Signals. In202110thInternationalIEEE/EMBSConferenceonNeuralEngineering(NER),pp.
946–949,2021. doi: 10.1109/NER49283.2021.9441086.
RuiLiu,YuanyuanChen,AnranLi,YiDing,HanYu,andCuntaiGuan.Aggregatingintrinsicinfor-
mationtoenhanceBCIperformance throughfederatedlearning. NeuralNetworks, pp.106100,
2024.
WeiLiu, Jie-LinQiu, Wei-LongZheng, andBao-LiangLu. ComparingRecognitionPerformance
and Robustness of Multimodal Deep Learning Models for Multimodal Emotion Recognition.
IEEETransactionsonCognitiveandDevelopmentalSystems,2021.
WeiLiu,Wei-LongZheng,ZiyiLi,Si-YuanWu,LuGan,andBao-LiangLu.Identifyingsimilarities
anddifferencesinemotionrecognitionwithEEGandeyemovementsamongChinese,German,
andFrenchPeople. JournalofNeuralEngineering,19(2):026012,2022.
MatthewDLuciw,EwaJarocka,andBenoniBEdin. Multi-channelEEGrecordingsduring3,936
graspandlifttrialswithvaryingweightandfriction. ScientificData,1(1):1–11,2014.
Shuai Luo, Yu-Ting Lan, Dan Peng, Ziyi Li, Wei-Long Zheng, and Bao-Liang Lu. Multimodal
emotionrecognitioninresponsetooilpaintings. In202244thAnnualInternationalConference
of the IEEE Engineering in Medicine & Biology Society (EMBC), pp. 4167–4170, 2022. doi:
10.1109/EMBC48229.2022.9871630.
PerrinMargaux,MabyEmmanuel,DaligaultSe´bastien,BertrandOlivier,andMattoutJe´re´mie. Ob-
jectiveandsubjectiveevaluationofonlineerrorcorrectionduringp300-basedspelling. Advances
inHuman-ComputerInteraction,2012:4–4,2012.
FrankMoss,LawrenceMWard,andWalterGSannita. Stochasticresonanceandsensoryinforma-
tionprocessing: atutorialandreviewofapplication. ClinicalNeurophysiology,115(2):267–281,
2004.
Iyad Obeid and Joseph Picone. The temple university hospital EEG data corpus. Frontiers in
Neuroscience,10:196,2016.
LongOuyang,JeffreyWu,XuJiang,DiogoAlmeida,CarrollWainwright,PamelaMishkin,Chong
Zhang,SandhiniAgarwal,KatarinaSlama,AlexRay,etal. Traininglanguagemodelstofollow
instructions with human feedback. Advances in Neural Information Processing Systems, 35:
27730–27744,2022.
WeiYanPeh, YuanyuanYao, andJustinDauwels. Transformerconvolutionalneuralnetworksfor
automatedartifactdetectioninscalpEEG. In202244thAnnualInternationalConferenceofthe
IEEEEngineeringinMedicine&BiologySociety(EMBC),pp.3599–3602.IEEE,2022.
12

PublishedasaconferencepaperatICLR2024
ZhiliangPeng,LiDong,HangboBao,QixiangYe,andFuruWei. Beitv2: Maskedimagemodeling
withvector-quantizedvisualtokenizers. arXivpreprintarXiv:2208.06366,2022.
AlecRadford,KarthikNarasimhan,TimSalimans,IlyaSutskever,etal. Improvinglanguageunder-
standingbygenerativepre-training. 2018.
AlecRadford,JeffreyWu,RewonChild,DavidLuan,DarioAmodei,IlyaSutskever,etal.Language
modelsareunsupervisedmultitasklearners. OpenAIblog,1(8):9,2019.
SubhrajitRoy,IsabellKiral-Kornek,andStefanHarrer.ChronoNet:Adeeprecurrentneuralnetwork
for abnormal EEG identification. In Artificial Intelligence in Medicine: 17th Conference on
ArtificialIntelligenceinMedicine,AIME2019,Poznan,Poland,June26–29,2019,Proceedings
17,pp.47–56.Springer,2019.
ArmanSavran,KorayCiftci,GuillameChanel,JavierCruz Mota,LuongHongViet,Bu¨lentSankur,
Lale Akarun, Alice Caplier, and Michele Rombaut. Emotion detection in the loop from brain
signalsandfacialimages. IneINTERFACE’06-SIMILARNoESummerWorkshoponMultimodal
Interfaces,2006.
Gerwin Schalk, Dennis J McFarland, Thilo Hinterberger, Niels Birbaumer, and Jonathan R Wol-
paw. BCI2000: ageneral-purposebrain-computerinterface(BCI)system. IEEETransactionson
BiomedicalEngineering,51(6):1034–1043,2004.
Vinit Shah, Eva Von Weltin, Silvia Lopez, James Riley McHugh, Lillian Veloso, Meysam Gol-
mohammadi, Iyad Obeid, and Joseph Picone. The temple university hospital seizure detection
corpus. FrontiersinNeuroinformatics,12:83,2018.
Lakhan Dev Sharma, Vijay Kumar Bohat, Maria Habib, Al-Zoubi Ala’M, Hossam Faris, and
Ibrahim Aljarah. Evolutionary inspired approach for mental stress detection using EEG signal.
ExpertSystemswithApplications,197:116634,2022.
Tengfei Song, Wenming Zheng, Peng Song, and Zhen Cui. EEG emotion recognition using dy-
namicalgraphconvolutionalneuralnetworks. IEEETransactionsonAffectiveComputing,11(3):
532–541,2018.
YonghaoSong,XueyuJia,LieYang,andLonghanXie. Transformer-basedspatial-temporalfeature
learningforEEGdecoding. arXivpreprintarXiv:2106.11170,2021.
Nazmi Sofian Suhaimi, James Mountstephens, Jason Teo, et al. EEG-based emotion recognition:
A state-of-the-art review of current trends and opportunities. Computational Intelligence and
Neuroscience,2020,2020.
Le-YanTaoandBao-LiangLu. EmotionRecognitionunderSleepDeprivationUsingaMultimodal
ResidualLSTMNetwork. In2020InternationalJointConferenceonNeuralNetworks(IJCNN),
pp.1–8,2020. doi: 10.1109/IJCNN48605.2020.9206957.
Mastaneh Torkamani-Azar, Sumeyra Demir Kanik, Serap Aydin, and Mujdat Cetin. Prediction of
reactiontimeandvigilancevariabilityfromspatio-spectralfeaturesofresting-stateEEGinalong
sustainedattentiontask. IEEEJournalofBiomedicalandHealthInformatics,24(9):2550–2558,
2020.
LoganTrujillo. RawEEGData. 2020. doi: 10.18738/T8/SS2NHB. URLhttps://doi.org/
10.18738/T8/SS2NHB.
Logan T Trujillo, Candice T Stanfield, and Ruben D Vela. The effect of electroencephalogram
(EEG) reference choice on information-theoretic measures of the complexity and integration of
EEGsignals. FrontiersinNeuroscience,11:425,2017.
Aaron Van Den Oord, Oriol Vinyals, et al. Neural discrete representation learning. Advances in
NeuralInformationProcessingSystems,30,2017.
13

PublishedasaconferencepaperatICLR2024
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez,
Ł ukasz Kaiser, and Illia Polosukhin. Attention is all you need. In I. Guyon, U. Von
Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett (eds.), Ad-
vances in Neural Information Processing Systems, volume 30. Curran Associates, Inc.,
2017. URL https://proceedings.neurips.cc/paper_files/paper/2017/
file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf.
LVeloso,JMcHugh,EvonWeltin,SLopez,IObeid,andJPicone. BigdataresourcesforEEGs:
Enablingdeeplearningresearch. In2017IEEESignalProcessinginMedicineandBiologySym-
posium(SPMB),pp.1–3.IEEE,2017.
EvavonWeltin,TameemAhsan,VinitShah,DawerJamshed,MeysamGolmohammadi,IyadObeid,
and Joseph Picone. Electroencephalographic slowing: A primary source of error in automatic
seizuredetection. In2017IEEESignalProcessinginMedicineandBiologySymposium(SPMB),
pp.1–5.IEEE,2017.
ChristopherWang,VighneshSubramaniam,AdamUriYaari,GabrielKreiman,BorisKatz,Ignacio
Cases, and Andrei Barbu. BrainBERT: Self-supervised representation learning for intracranial
recordings. InTheEleventhInternationalConferenceonLearningRepresentations,2023. URL
https://openreview.net/forum?id=xmcYx_reUn6.
Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yo-
gatama,MaartenBosma,DennyZhou,DonaldMetzler,etal.Emergentabilitiesoflargelanguage
models. arXivpreprintarXiv:2206.07682,2022.
DiWu,SiyuanLi,JieYang,andMohamadSawan. neuro2vec: Maskedfourierspectrumprediction
forneurophysiologicalrepresentationlearning. arXivpreprintarXiv:2204.12440,2022.
YuxinWuandKaimingHe. Groupnormalization. InProceedingsoftheEuropeanConferenceon
ComputerVision(ECCV),September2018.
ZhendaXie,ZhengZhang,YueCao,YutongLin,JianminBao,ZhuliangYao,QiDai,andHanHu.
Simmim: A simple framework for masked image modeling. In Proceedings of the IEEE/CVF
ConferenceonComputerVisionandPatternRecognition,pp.9653–9663,2022.
Gaowei Xu, Tianhe Ren, Yu Chen, and Wenliang Che. A one-dimensional cnn-lstm model for
epileptic seizure recognition using eeg signal analysis. Frontiers in Neuroscience, 14:578126,
2020.
ChaoqiYang, MBrandonWestover, andJimengSun. BIOT:Biosignaltransformerforcross-data
learning in the wild. In Thirty-seventh Conference on Neural Information Processing Systems,
2023a. URLhttps://openreview.net/forum?id=c2LZyTyddi.
ChaoqiYang,CaoXiao,MBrandonWestover,JimengSun,etal.Self-SupervisedElectroencephalo-
gramRepresentationLearningforAutomaticSleepStaging: ModelDevelopmentandEvaluation
Study. JMIRAI,2(1):e46769,2023b.
Ke Yi, Yansen Wang, Kan Ren, and Dongsheng Li. Learning Topology-Agnostic EEG Represen-
tations with Geometry-Aware Modeling. In Thirty-seventh Conference on Neural Information
ProcessingSystems,2023. URLhttps://openreview.net/forum?id=hiOUySN0ub.
W. Zheng, W. Liu, Y. Lu, B. Lu, and A. Cichocki. Emotionmeter: A multimodal framework for
recognizing humanemotions. IEEE Transactionson Cybernetics, pp.1–13, 2018. ISSN2168-
2267. doi: 10.1109/TCYB.2018.2797176.
Wei-LongZhengandBao-LiangLu. InvestigatingcriticalfrequencybandsandchannelsforEEG-
basedemotionrecognitionwithdeepneuralnetworks.IEEETransactionsonAutonomousMental
Development,7(3):162–175,2015. doi: 10.1109/TAMD.2015.2431497.
14

PublishedasaconferencepaperatICLR2024
| A RELATED |     | WORK |     |     |     |     |     |     |     |     |
| --------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Self-supervised Pre-training. In recent years, self-supervised pre-training has made significant
progress in natural language processing and computer vision. BERT (Devlin et al., 2018) innova-
tivelyproposedtheideaofmaskingpartoftheinputsentencesandthenreconstructingthem. The
GPT series (Radford et al., 2018; 2019; Brown et al., 2020) proposed to pre-train large language
models by a large corpus of data in an autoregressive way. Both studies improved the fine-tuning
performancesignificantlyinvariousdownstreamtasks.Incomputervision,iGPT(Chenetal.,2020)
firstly brought the idea from GPT to pre-train a vision model. BEiT (Bao et al., 2022) pioneerly
trained a vision tokenizer and leveraged BERT-like pre-training for training a vision Transformer.
MAE(Heetal.,2022)andSimMIM(Xieetal.,2022)practicedmaskedimagemodelingbysimply
reconstructingtherawpixelsandachievedappreciableimprovement.
LearningwithHeterogeneousDatasets. MMMintroducedapre-trainingframeworkbuiltonthe
unifiedtopologyandobtainedtopology-agnosticrepresentations(Yietal.,2023). Hanetal.(2023)
combinedgraphneuralnetworksandtransferlearningfornon-invasivemotorimageryEEGdecod-
ingwithheterogeneouselectrodeconfigurations. Guetal.(2023)developedtwonetworkstolearn
fromthesharedandthecompletechannelsacrossdatasets,achievingcoherentperformanceboosts.
Liuetal.(2024)proposedahierarchicalpersonalizedFederatedLearningEEGdecodingframework,
enablingdatasetswithdisparatedataformatstocollaborateinthemodeltrainingprocess.
Self-supervised Learning in BCI. Although self-supervised pre-training has achieved great suc-
cess,itspotentialinBCIisfarfrombeingexplored. BENDR(Kostasetal.,2021)adaptedWav2vec
2.0 (Baevski et al., 2020), which uses contrastive learning to learn compressed representations of
raw EEG signals. Banville et al. investigated temporal context prediction as well as contrastive
predictive coding on two clinically relevant problems (Banville et al., 2021). ContraWR (Yang
etal.,2023b), ContrastwiththeWorldRepresentation, usedglobalstatisticstodistinguishsignals
associated with different sleep stages. BrainBERT (Wang et al., 2023) masks random parts of the
stereo-electroencephalographic (SEEG) spectrogram and produce original embeddings with 43.6
hoursofdata. However,allexistingstudieseitherconcentrateonspecificBCItasksoronlyemploy
small-sizedatasetsandmodels,leavingroomforexploringlarge-scaleEEGdatatotrainlargeEEG
modelsthroughself-supervision.
| B LABRAM |     | PRE-TRAINING |     | ANALYSIS |     |     |     |     |     |     |
| -------- | --- | ------------ | --- | -------- | --- | --- | --- | --- | --- | --- |
Thepre-trainingofLaBraMcanbeinterpretedasthetrainingofavariationalautoencoder(Kingma
& Welling, 2014; Bao et al., 2022). We denote the original EEG sample as x, the corrupted EEG
|     |     | xM, |     |     |     |     |     | x˜. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
by masking as and its Fourier spectrum (amplitude and phase) as The focus is on the
evidencelowerbound(ELBO)ofthelog-likelihoodp(x˜|xM),whichinvolvesrecoveringtheFourier
spectrumoftheoriginalEEGsignalsfromthemaskedperspective:
| (cid:88)       |         |       | (cid:88)       |             |     |       |        |             |     |          |
| -------------- | ------- | ----- | -------------- | ----------- | --- | ----- | ------ | ----------- | --- | -------- |
|                | logp(x˜ | |xM)≥ |                | (E          |     | (logp | (x˜ |z | )−D (q (z|x | ),p | (z|xM)), |
|                |         | i i   |                | zi∼qϕ(z|xi) |     | ψ     | i i    | KL ϕ        | i   | θ i      |
| (xi,xM ,x˜i)∈D |         |       | (xi,xM ,x˜i)∈D |             |     |       |        |             |     |          |
| i              |         |       | i              |             |     |       |        |             |     |          |
(13)
whereq (z|x)representstheneuraltokenizerthatencodestheEEGsampleintodiscreteneuralto-
ϕ
kens,p (x˜|z)denotestheneuraldecoderpredictingtheFourierspectrumfromgivenneuraltokens,
ψ
andp (z|xM)istheLaBraMpre-trainingformaskedEEGmodeling,wheretheLaBraMencoder
θ
reconstructsneuraltokensfromthecorruptedEEGinput.
Thewholeframeworkisoptimizedthroughatwo-stageprocedureas(VanDenOordetal.,2017).
Forthefirststage,wetraintheneuraltokenizerasadiscretevariationalautoencoderbyminimizing
thereconstructionloss−E
|     |     |             | (logp | (x˜ | |z )withauniformprior. |     |     | Forthesecondstage,we |     |     |
| --- | --- | ----------- | ----- | --- | ---------------------- | --- | --- | -------------------- | --- | --- |
|     |     | zi∼qϕ(z|xi) |       | ψ   | i i                    |     |     |                      |     |     |
setq aswellasp fixedandlearnthepriorp byminimizingthelossD .Forsimplicity,q (z|x )
| ϕ   |     | ψ   |     | θ   |     |     |     | KL  |     | ϕ i |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is defined as a one-point distribution with the most likely neural tokens zˆ = argmax q (z|x ).
|     |     |     |     |     |     |     |     | i   | z   | ϕ i |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Consequently,wecanrewriteEquation13as
|     |     | (cid:88)       | (E          |     |           |           | (zˆ|xM)), |     |     |      |
| --- | --- | -------------- | ----------- | --- | --------- | --------- | --------- | --- | --- | ---- |
|     |     |                |             |     | (logp (x˜ | |z )+logp |           |     |     | (14) |
|     |     |                | zi∼qϕ(z|xi) |     | ψ         | i i       | θ         | i i |     |      |
|     |     | (xi,xM ,x˜i)∈D |             |     |           |           |           |     |     |      |
i
wherethefirsttermistheobjectiveforvector-quantizedneuralspectrumpredictionandthesecond
termistheobjectiveforLaBraMpre-training.
15

PublishedasaconferencepaperatICLR2024
| C HYPERPARAMETER |                          |                                                                     | SETTINGS                                         |             |                |              |            |             |            |
| ---------------- | ------------------------ | ------------------------------------------------------------------- | ------------------------------------------------ | ----------- | -------------- | ------------ | ---------- | ----------- | ---------- |
|                  | Table3:                  | Hyperparametersforvector-quantizedneuralspectrumpredictiontraining. |                                                  |             |                |              |            |             |            |
|                  |                          |                                                                     | Hyperparameters                                  |             |                |              | Values     |             |            |
|                  |                          |                                                                     |                                                  |             | Iputchannels   |              | {1,8,8}    |             |            |
|                  |                          |                                                                     |                                                  |             | Outputchannels |              | {8,8,8}    |             |            |
|                  |                          |                                                                     | TemporalEncoder                                  |             | Kernelsize     |              | {15,3,3}   |             |            |
|                  |                          |                                                                     |                                                  |             | Stride         |              | {8,1,1}    |             |            |
|                  |                          |                                                                     |                                                  |             | Padding        |              | {7,1,1}    |             |            |
|                  |                          |                                                                     | Transformerencoderlayers                         |             |                |              | 12         |             |            |
|                  |                          |                                                                     | Transformerdecoderlayers                         |             |                |              | 3          |             |            |
|                  |                          |                                                                     | Hiddensize                                       |             |                |              | 200        |             |            |
|                  |                          |                                                                     |                                                  | MLPsize     |                |              | 800        |             |            |
|                  |                          |                                                                     | Attentionheadnumber                              |             |                |              | 10         |             |            |
|                  |                          |                                                                     | Codebooksize                                     |             |                |              | 8192×64    |             |            |
|                  |                          |                                                                     |                                                  | Batchsize   |                |              | 1024       |             |            |
|                  |                          |                                                                     | Peaklearningrate                                 |             |                |              | 5e-5       |             |            |
|                  |                          |                                                                     | Minimallearningrate                              |             |                |              | 1e-5       |             |            |
|                  |                          |                                                                     | Learningratescheduler                            |             |                |              | Cosine     |             |            |
|                  |                          |                                                                     |                                                  | Optimizer   |                |              | AdamW      |             |            |
|                  |                          |                                                                     |                                                  | Adamβ       |                |              | (0.9,0.99) |             |            |
|                  |                          |                                                                     | Weightdecay                                      |             |                |              | 1e-4       |             |            |
|                  |                          |                                                                     | Totalepochs                                      |             |                |              | 100        |             |            |
|                  |                          |                                                                     | Warmupepochs                                     |             |                |              | 10         |             |            |
|                  |                          |                                                                     |                                                  | Datastride  |                |              | 200        |             |            |
|                  |                          |                                                                     | Table4: HyperparametersformaskedEEGpre-training. |             |                |              |            |             |            |
|                  |                          | Hyperparameters                                                     |                                                  | LaBraM-Base |                | LaBraM-Large |            | LaBraM-Huge |            |
|                  |                          |                                                                     | Iputchannels                                     |             | {1,8,8}        |              | {1,16,16}  |             | {1,32,32}  |
|                  |                          |                                                                     | Outputchannels                                   |             | {8,8,8}        |              | {16,16,16} |             | {32,32,32} |
| TemporalEncoder  |                          |                                                                     | Kernelsize                                       |             |                |              | {15,3,3}   |             |            |
|                  |                          |                                                                     | Stride                                           |             |                |              | {8,1,1}    |             |            |
|                  |                          |                                                                     | Padding                                          |             |                |              | {7,1,1}    |             |            |
|                  | Transformerencoderlayers |                                                                     |                                                  |             | 12             |              | 24         |             | 48         |
|                  |                          | Hiddensize                                                          |                                                  |             | 200            |              | 400        |             | 800        |
|                  |                          | MLPsize                                                             |                                                  |             | 800            |              | 1600       |             | 3200       |
|                  | Attentionheadnumber      |                                                                     |                                                  |             | 10             |              | 16         |             | 16         |
|                  |                          | Batchsize                                                           |                                                  |             |                |              | 512        |             |            |
|                  |                          | Peaklearningrate                                                    |                                                  |             |                |              | 5e-4       |             |            |
|                  | Minimallearningrate      |                                                                     |                                                  |             |                |              | 1e-5       |             |            |
|                  | Learningratescheduler    |                                                                     |                                                  |             |                |              | Cosine     |             |            |
|                  |                          | Optimizer                                                           |                                                  |             |                |              | AdamW      |             |            |
|                  |                          | Adamβ                                                               |                                                  |             |                |              | (0.9,0.98) |             |            |
|                  |                          | Weightdecay                                                         |                                                  |             |                |              | 0.05       |             |            |
|                  |                          | Totalepochs                                                         |                                                  |             |                |              | 50         |             |            |
|                  |                          | Warmupepochs                                                        |                                                  |             |                |              | 5          |             |            |
|                  |                          | Datastride                                                          |                                                  |             |                |              | 800        |             |            |
|                  |                          | Gradientclipping                                                    |                                                  |             |                |              | 3          |             |            |
|                  |                          | Layerscaleinit                                                      |                                                  |             | 0.1            |              | 1e-5       |             | 1e-6       |
|                  |                          | EMAweight                                                           |                                                  |             |                |              | 0.996      |             |            |
|                  |                          | Maskratio                                                           |                                                  |             |                |              | 0.5        |             |            |
16

PublishedasaconferencepaperatICLR2024
Table5: Hyperparametersfordownstreamfine-tuning.
Hyperparameters Values
Batchsize 512
Peaklearningrate 5e-4
Minimallearningrate 1e-6
Learningratescheduler Cosine
Optimizer AdamW
Adamβ (0.9,0.999)
Weightdecay 0.05
Totalepochs 50(B)30(L/H)
Warmupepochs 5(B)3(L/H)
Droppath 0.1(B/L)0.2(H)
Layer-wiselearningratedecay 0.65(B)0.8(L/H)
Labelsmoothing(multi-classclassification) 0.1
D PRE-TRAINING DATASET DESCRIPTION
WedescribethedatasetsweusefortrainingLaBraMhere.
Training datasets (for both vector-quantized neural spectrum prediction training and LaBraM pre-
training,thetotaltimeis2534.78hours):
• BCI Competition IV-1 (Blankertz et al., 2007): A motor imagery dataset containing 59 EEG
channels at 1000Hz sampling rate for 2 classes of left hand, right hand, foot (+ idle state) for 7
subjects.TherecordingwasmadeusingBrainAmpMRplusamplifiersandanAg/AgClelectrode
cap. (totaltime: 8.21hours)
• Emobrain(Savranetal.,2006): AmultimodalemotiondatasetwhereEEG(64channels, 1024
Hz)andfNIRS,arerecordedbytheBiosemiActive2acquisitionsystem,including16subjects.
TheemotionswereelicitedthroughaselectedsubsetofIAPSdataset. (totaltime: 4.94hours)
• GraspandLiftEEGChallenge(Luciwetal.,2014): AdatasetcontainingEEGrecordings(32
channels,500Hz)of12subjectsperforminggrasp-and-lift(GAL)trials. TheEEGcapwasused
inconjunctionwithaBrainAmpEEGsignalamplifier. (totaltime: 11.72hours)
• Inria BCI Challenge (Margaux et al., 2012): A P300-based spelling dataset including 26 sub-
jectswithEEGrecords(56channels,600Hz)byAg/AgClEEGsensors(VSM-CTFcompatible
system). (totaltime: 29.98hours)
• EEGMotorMovement/ImageryDataset(Schalketal.,2004):Amotorimagerydatasetconsist-
ingof109volunteersperforming2baselinetasks(eye-openandeye-closed), motormovement,
and motor imagery (both fists or both feet) with EEG records (64 channels, 160 Hz) using the
BCI2000system. (totaltime: 47.3hours)
• Raw EEG Data (Trujillo, 2020): A dataset where EEG (64 channels, 256 Hz) was recorded
duringthereportedInformation-Integrationcategorizationtaskandthereportedmultidimensional
Rule-Basedcategorizationtask. (totaltime: 34.35hours)
• Resting State EEG Data (Trujillo et al., 2017): A dataset comprising 22 subjects for a resting
taskof8minswith4minsofeyesclosedand4minsofeyesopenwith64EEGchannelsat256Hz
using active Ag/AgCl electrodes either mounted in a BioSemi electrode cap or via freestanding
electrodes. (totaltime: 3.04hours)
• SEEDSeries(Zheng&Lu,2015;Zhengetal.,2018;Liuetal.,2022): Theemotionaldatasets
includingSEED(15subjects),SEED-IV(15subjects),SEED-GER(8subjects),andSEED-FRA
(8 subjects). All EEG signals (62 channels, 1000 Hz) were recorded with the ESI NeuroScan
Systeminresponsetovideos. (totaltime: 166.75hours)
• Siena Scalp EEG Database (Detti et al., 2020): A database consisting of EEG recordings (31
channels,512Hz)of14patientsemployingEBNeuroandNatusQuantumLTMamplifiers,and
reusablesilver/goldcupelectrodes. (totaltime: 30.47hours)
17

PublishedasaconferencepaperatICLR2024
• SPIS Resting State Dataset (Torkamani-Azar et al., 2020): A dataset including 10 subjects,
2.5minutesrecordingineachstate(eyes-closedandeyes-open)priortoa105-minutesessionof
Sustained Attention to Response Task with fixed-sequence and varying ISIs. Monopolar EEG
activity(64channels,2048Hz)wascollectedvia64Ag/AgClactiveelectrodes. (totaltime: 0.83
hour)
• Target Versus Non-Target (Korczowski et al., 2019): A dataset including 50 subjects play-
ing Brain Invaders, a visual P300 Brain-Computer Interface using oddball paradigm with ada-
pative Riemannian Geometry (no-calibration). EEG signals (32 channels, 512 Hz) were ac-
quired by means of a research-grade amplifier (g.USBamp, g.tec, Schiedlberg, Austria) and the
| g.GAMMAcap. | (totaltime: | 16hours) |     |     |     |     |     |
| ----------- | ----------- | -------- | --- | --- | --- | --- | --- |
• TUAR(Buckwalteretal.,2021):ThissubsetofTUEGcontainsannotationsof5differentartifacts
| withEEGrecorded(23channels,256Hz). |     |     |     | (totaltime: | 92.22hours) |     |     |
| ---------------------------------- | --- | --- | --- | ----------- | ----------- | --- | --- |
• TUEP(Velosoetal.,2017): ThisisasubsetofTUEGthatcontains100subjectswithepilepsy
and 100 subjects without epilepsy with EEG recorded (19-23 channels, 256 Hz), as determined
| byacertifiedneurologist. |     | (totaltime: | 591.22hours) |     |     |     |     |
| ------------------------ | --- | ----------- | ------------ | --- | --- | --- | --- |
• TUSZ(Shahetal.,2018): ThiscorpushasEEGsignalsthathavebeenmanuallyannotateddata
forseizureevents(starttime,stop,channel,andseizuretype)withEEGrecorded(19-23channels,
| 256Hz). | (totaltime: | 1138.53hours) |     |     |     |     |     |
| ------- | ----------- | ------------- | --- | --- | --- | --- | --- |
• TUSL (von Weltin et al., 2017): This is another subset of TUEG that contains annotations of
slowingevents(23channels,256Hz). Thiscorpushasbeenusedtostudycommonerrormodali-
| tiesinautomatedseizuredetection. |     |     | (totaltime: | 20.59hours) |     |     |     |
| -------------------------------- | --- | --- | ----------- | ----------- | --- | --- | --- |
• Self-collectedEEGData (Jiangetal.,2023;2021;Luoetal.,2022;Lietal.,2021;Tao&Lu,
2020):WefurthercollectEEGdatafrommorethan140subjectsbyourselves(62channels,1000
| Hz)withtheESINeuroScanSystem. |     |                     | (totaltime: | 342.23hours) |        |          |     |
| ----------------------------- | --- | ------------------- | ----------- | ------------ | ------ | -------- | --- |
| E VISUALIZATION               |     | OF VECTOR-QUANTIZED |             |              | NEURAL | SPECTRUM |     |
PREDICTION
Wefurthervisualizehowtheamplitude
andphaseintheFourierdomainarere-
|               |                    |              |                 |        |  $ P S O L W X G H |  3 K D V H      |     |
| ------------- | ------------------ | ------------ | --------------- | ------ | ------------------ | --------------- | --- |
| constructed.  | As depicted        | in Figure    | 7,              |        |                    |                 |     |
|               |                    |              |                 |     |                    |              |     |
| although      | some details       | are missing, | the             |        |                    |                 |     |
| overall trend | of the amplitude   | is           | recon-  V V R / |     |                    |  V V R /     |     |
| structed      | well. In contrast, | the          | recon-          |        |                    |                 |     |
   
| struction         | of the phase  | is not as          | good     |      |                |                     |                  |
| ----------------- | ------------- | ------------------ | -------- | ------- | -------------- | ------------------- | ---------------- |
| as the amplitude. | Nevertheless, |                    | it can   |         |                |                     |                  |
|                   |               |                    |          |      |          |             |           |
| be seen           | from Figure   | 6 that there       | is still |         |                |                     |                  |
|                   |               |                    |          |         |  ( S R F K V   |  ( S R F K V        |                  |
| a stable          | decrease in   | the reconstruction |          |         |                |                     |                  |
lossduringtraining,whichindicatesthe
discretecodebookdoeslearnhigh-level Figure6: Thereconstructionlosscurveofamplitudeand
| informationfromtheFourierdomain. |     |     | phase. |     |     |     |     |
| -------------------------------- | --- | --- | ------ | --- | --- | --- | --- |
 2 U L J L Q D O  ( ( *  V L J Q D O V  2 U L J L Q D O  $ P S O L W X G H  5 H F R Q V W U X F W H G  $ P S O L W X G H  2 U L J L Q D O  3 K D V H  5 H F R Q V W U X F W H G  3 K D V H
Figure7: VisualizationofreconstructedFourierspectrum. Notethatweonlyvisualizehalfofthe
resultssinceDFTisconjugatesymmetric.
18

PublishedasaconferencepaperatICLR2024
F MORE EXPERIMENTS ON
OTHER BCI TASKS
WeconducttwoadditionalBCItasksonthefollowingdatasets:
• SEED-V(emotionrecognition)(Liuetal.,2021): AnemotionEEGdatasetcontainingfiveemo-
tion categories (happy, sad, neutral, disgust, and fear). The experiment collected EEG data (62
channels, 1000 Hz) from 20 subjects, including 10 males and 10 females. Each subject partici-
patedintheexperimentsthreetimesandeachsessionincludedfifteenvideoclipscorresponding
to the five emotions, where each video clip lasted for several minutes. The EEG signals are
segmentedinto148,0801-secondsamples.
• MoBI(gaitprediction)(Heetal.,2018): Amobilebrain-bodyimagingdatasetacquiredduring
treadmillwalkinginaBCItask, whichisalowerlimbmotorimagerydataset. Sixgoniometers
wereemployedtorecordbilateraljointanglesonthelegs(hip, knee, andankle). Theobjective
is to regress the angles for 12 targets (left leg and right leg). The data were collected from 8
healthysubjects,eachofwhomhadthreeidenticaltrials. TheEEGsignals(60channels,100Hz)
wererecordedbytheActiCapsystem. Settingthestrideto50ms, thedatasetinvolves575,830
2-secondsamples.
ForSEED-V,astherearefifteentrialsforonesession,weseparatethefifteentrialsintothreeparts
with an equal number of trials, i.e., 5:5:5. We merge each part from all sessions of subjects and
derivethetraining, validation, andtestset. AsSEED-Visoverallbalanced, weconsideraccuracy
insteadofbalancedaccuracyasametrictocompareperformance. Notethatsomeimplementation
detailsareabitdifferentfromdefaultsettingsonthisdatasetduetodifferentcharacteristics(peak
learningrate: 5e-4(L)5e-3(H);totalepochs: 50(L/H),warmupepochs: 4(L)5(H)).
ForMoBI,eachtrialconsistedofa15-minutetreadmillwalkingsession(trainingsession),followed
bya5-minutetreadmillwalkingsession(testsession)withaclosed-loopBCI.Tovalidatethemodel,
we split the training session into two parts: the first 10 minutes of EEG and its corresponding
jointdatawereusedastrainingdata,whilethelast5minutesofdatawereusedasvalidationdata.
Meanwhile,wecombinedallthetrainingdata,validationdata,andtestingdataoftheeightsubjects
toformcorrespondinglargertrainingdatasets,validationdatasets,andtestingdatasets. Sincemost
anglesaretypicallylowerthan90◦,thetargetanglesaredividedby90fornormalization. Wereport
theaveragevalueof12targetsforeachmetric.
As the task of MoBI is regression, we choose the following metrics to evaluate the performance
ofdifferentmethods: 1)Pearson’scorrelation: Pearson’scorrelationcoefficientwhichisusedto
quantify the models’ regression effect. It measures the linear correlation between two variables
XandY.2)R2score: R2 (coefficientofdetermination)regressionscorefunction,whichmeasures
howwellastatisticalmodelpredictsanoutcome.3)RMSE:RootMeanSquareErroristhestandard
deviation of the residuals (prediction errors). R2 score is utilized as the monitor to select the best
model. MSElossistheobjectivetooptimizethemodels.
TheexperimentalresultsarepresentedinFigure6. OnSEED-V,LaBraMsoutperformallbaseline
methods on all metrics. The phenomenon that the performance increases when the model gets
larger is also observed. For MoBI, our Base model archives competitive results compared to the
best baseline method. Whereas, the Large and Huge models obtain better performance among all
methods.
Table6: TheresultsofdifferentmethodsonSEED-VandMoBI.
SEED-V MoBI
Accuracy Cohen’sKappa WeightedF1 Pearson’sCorrelation R2Score RMSE↓
SPaRCNet 0.2887±0.0047 0.1032±0.0083 0.2904±0.0064 0.4561±0.0161 0.1467±0.0064 0.1344±0.0006
ContraWR 0.3603±0.0098 0.1988±0.0114 0.3590±0.0091 0.3357±0.0164 0.0743±0.0093 0.1401±0.0008
CNN-Transformer 0.3665±0.0058 0.2034±0.0060 0.3638±0.0065 0.3224±0.0109 0.0628±0.0089 0.1411±0.0007
FFCL 0.3686±0.0059 0.2094±0.0078 0.3679±0.0062 0.3158±0.0235 0.0712±0.0124 0.1396±0.0014
ST-Transformer 0.2772±0.0047 0.0783±0.0071 0.2625±0.0061 0.5442±0.0012 0.2911±0.0014 0.1222±0.0001
BIOT 0.3802±0.0094 0.2247±0.0100 0.3809±0.0114 0.2757±0.0173 0.0597±0.0069 0.1401±0.0006
LaBraM-Base 0.4095±0.0062 0.2613±0.0075 0.4120±0.0057 0.5383±0.0102 0.2876±0.0032 0.1225±0.0003
LaBraM-Large 0.4096±0.0075 0.2639±0.0090 0.4127±0.0079 0.5603±0.0020 0.3093±0.0032 0.1197±0.0003
LaBraM-Huge 0.4102±0.0037 0.2646±0.0046 0.4136±0.0047 0.5632±0.0023 0.3145±0.0032 0.1196±0.0003
19

PublishedasaconferencepaperatICLR2024
G EFFECTIVENESS OF VECTOR-QUANTIZED NEURAL SPECTRUM
PREDICTION
To verify the effectiveness of vector-quantized neural spectrum prediction, we elaborate on three
typesofexperimentalsettingsasillustratedinTable7. ThecomparisonbetweenLaBraMandSet-
ting1demonstratesthatthecodebookiseffectiveformaskedEEGmodeling. LaBraMobtainsthe
best performance on TUEV and the lowest standard deviations on TUAB. There is an interesting
observationthatmaskedEEGmodelingwiththeassistanceoftraininganauxiliaryneuraltokenizer
(LaBraM and Setting 1) performs greatly better on TUEV while the naive masked EEG modeling
(Setting2andSetting3)performsslightlybetteronTUAB.Oneexplanationforthisphenomenonis
thatlearningsemanticrepresentationsfromtheneuraltokenizerandcodebooksignificantlybenefits
high-leveldownstreamtaskslikeTUEVwhichclassifiesdifferenttypesofevents. Whereas,TUAB
isalow-leveldownstreamtaskwheretheclinicallynormal/abnormalEEGsegmentscanbeeasily
distinguishedvisually. Hence,simplyreconstructingoriginsignalsortheirFourierspectrumisable
to perform well on these low-level tasks but fails to obtain satisfying performance on high-level
tasks.
Table7: Ablationstovalidatetheeffectivenessofvector-quantizedneuralspectrumprediction.
TUAB TUEV
BalancedAccuracy AUC-PR AUROC BalancedAccuracy Cohen’sKappa WeightedF1
LaBraM 0.8140±0.0019 0.8965±0.0016 0.9022±0.0009 0.6409±0.0065 0.6637±0.0093 0.8312±0.0052
Setting1 0.8058±0.0044 0.8949±0.0037 0.8964±0.0012 0.6162±0.0174 0.6376±0.0168 0.8170±0.0058
Setting2 0.8261±0.0030 0.9150±0.0016 0.9067±0.0024 0.5630±0.0313 0.5910±0.0156 0.7979±0.0082
Setting3 0.8166±0.0073 0.9062±0.0029 0.9053±0.0026 0.5730±0.0133 0.5643±0.0089 0.7819±0.0040
Setting1: Wedirectlypredictoutputembeddingsoftheneuraltokenizerbymaximizingcosinesimilarity
insteadofpredictingthediscreteneuraltokensfromthecodebook.
Setting2: WediscardtheneuraltokenizeranddirectlyreconstructrawEEGpatchesbyminimizingMSE
loss.
Setting3: WediscardtheneuraltokenizerandreconstructtheFourierspectrum(amplitudeandphase)of
rawEEGpatchesbyminimizingMSEloss.
H ABLATION ON MASK RATIO
Inthisexperiment,weconductdifferentsettingsofthemaskratiotoexploreitsimpact. Itisnoted
that we introduce the symmetric masking strategy, so we only need to validate half of the mask
ratios. As the mask ratio is set to r, the symmetric masking will mask 1−r proportion of EEG
patches. TheablationresultsareprovidedinTable8, whereexperimentsareconductedonTUAB
andTUEV.Itcanbeinducedthatthebestmaskratiois0.4(0.6)forTUABand0.5(0.5)forTUEV.
Moreover, 0.5 (0.5) is the second-best mask ratio for TUAB while the remaining mask ratios are
incredibly close. The performance for mask ratios except 0.5 (0.5) is also similar to each other.
Notably,themaskratioof0.5(0.5)achievessmallerstandarddeviationsonbothTUABandTUEV.
Therefore,weconcludethat0.5(0.5)isarelativelygoodmaskratioforthemaskedEEGmodeling
ofLaBraMpre-training.
Table8: Performanceofdifferentmaskratios.
TUAB TUEV
MaskRatio
BalancedAccuracy AUC-PR AUROC BalancedAccuracy Cohen’sKappa WeightedF1
0.5(0.5) 0.8140±0.0019 0.8965±0.0016 0.9022±0.0009 0.6409±0.0065 0.6637±0.0093 0.8312±0.0052
0.4(0.6) 0.8145±0.0039 0.9083±0.0030 0.9049±0.0038 0.6174±0.0127 0.6123±0.0094 0.8067±0.0059
0.3(0.7) 0.7994±0.0037 0.8950±0.0006 0.8974±0.0008 0.6112±0.0216 0.6089±0.0158 0.8068±0.0086
0.2(0.8) 0.8039±0.0054 0.8990±0.0050 0.9018±0.0023 0.6054±0.0268 0.6050±0.0152 0.8024±0.0089
0.1(0.9) 0.8022±0.0041 0.8968±0.0010 0.8992±0.0007 0.6033±0.0264 0.6181±0.0178 0.8134±0.0094
20

PublishedasaconferencepaperatICLR2024
| I ABLATION | SYMMETRIC |     | MASKING |     |     |     |
| ---------- | --------- | --- | ------- | --- | --- | --- |
ON
Weconductanablationstudytoverifythecontributionofthesymmetricmaskingstrategy. Table9
reports the results on TUAB and TUEV. It is obvious that the performance of most metrics de-
creasesbyaremarkablemarginonbothdatasets,especiallyTUEV.Specifically,withoutsymmetric
masking,theperformanceofthebasemodelincreasesalittlebitonTUAB.Nevertheless,theperfor-
mancedecreasesinmostotherscenarios.Thisisbecausethedataissufficientforthebasemodel,so
thesymmetricmaskingstrategywhichactslikedataaugmentationcontributesalittletothemodel
training. For larger models like LaBraM-Huge, the symmetric masking improves the downstream
performance as it requires more data. This observation indicates that symmetric masking can not
onlyboostthedownstreamperformancebutalsoimprovestabilityandrobustness.
|     | Table9:          | Ablationstudyofsymmetricmasking(SM). |       |                  |              |            |
| --- | ---------------- | ------------------------------------ | ----- | ---------------- | ------------ | ---------- |
|     |                  | TUAB                                 |       |                  | TUEV         |            |
|     | BalancedAccuracy | AUC-PR                               | AUROC | BalancedAccuracy | Cohen’sKappa | WeightedF1 |
LaBraM-Base 0.8140±0.0019 0.8965±0.0016 0.9022±0.0009 0.6409±0.0065 0.6637±0.0093 0.8312±0.0052
w/oSM 0.8155±0.0041 0.9077±0.0069 0.9065±0.0034 0.6284±0.0175 0.6279±0.0260 0.8152±0.0105
LaBraM-Large 0.8226±0.0015 0.9130±0.0005 0.9127±0.0005 0.6581±0.0156 0.6622±0.0136 0.8315±0.0040
|     | 0.8198±0.0042 | 0.9140±0.0007 | 0.9106±0.0012 | 0.6548±0.0246 | 0.6601±0.0122 | 0.8319±0.0034 |
| --- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
w/oSM
LaBraM-Huge 0.8258±0.0011 0.9204±0.0011 0.9162±0.0016 0.6616±0.0170 0.6745±0.0195 0.8329±0.0086
w/oSM 0.8247±0.0010 0.9188±0.0005 0.9149±0.0004 0.6261±0.0178 0.6391±0.0179 0.8152±0.0085
| J LABRAM |     | PRE-TRAINING |     |     |     |     |
| -------- | --- | ------------ | --- | --- | --- | --- |
WITHOUT
In this experiment, we directly train LaBraM on the downstream datasets from scratch without
pre-trainingtovalidatetheeffectivenessofthemaskedEEGmodelingpre-training. Thesteepper-
formancedropdemonstratestheusefulnessofpre-training,asillustratedinFigure 8.
|                            |  7 8 $ % |     |        |                            |  7 8 ( 9 |     |
| -------------------------- | -------- | --- | ------ | -------------------------- | -------- | --- |
|                         |          |     |     |                            |          |     |
|  Z   S U H  W U D L Q   |          |     |        |  Z   S U H  W U D L Q   |          |     |
|  Z  R  S U H  W U D L Q |          |     |        |  Z  R  S U H  W U D L Q |          |     |
|                         |          |     |     |                            |          |     |
|                         |          |     |     |                            |          |     |
|                         |          |     |     |                            |          |     |
|                         |          |     |     |                            |          |     |
|                         |          |     |     |                            |          |     |
 % D O D Q F H G  $ F F X U D F \  $ 8 &  3 5  $ 8 5 2 &  % D O D Q F H G  $ F F X U D F \  & R K H Q 
 V  . D S S D  : H L J K W H G  ) 
|           | Figure8:    | Comparisonwithmodelwithoutpre-training. |     |     |     |     |
| --------- | ----------- | --------------------------------------- | --- | --- | --- | --- |
| K PARTIAL | FINE-TUNING |                                         |     |     |     |     |
InTable10,wereporttheresultsaboutfine-tuningpartofLaBraM.Weelaborateonseveralsettings:
fine-tuningall12Transformerblocks,fine-tuningthelast8Transformerblocks,fine-tuningthelast
4Transformerblocks,andlinearprobing. Itisnoteworthythatforlinearprobing,wesettheweight
decay to 0. One can see that on TUAB, the results of full fine-tuning, fine-tuning 12 Transformer
blocks,andfine-tuning8Transformerblocksarequitesimilar.Whenonlyfine-tuning4Transformer
blocksandlinearprobing,thereisaslightdegradationinperformance. OnTUEV,yet,fine-tuning8
Transformerblocksachievesthebestperformanceonallthreemetrics. Notably,theresultsoflinear
probingaremuchworsethanothersettings,whichstillhaveroomforimprovement.
21

PublishedasaconferencepaperatICLR2024
Table10: Resultsoffine-tuningpartofLaBraM.
TUAB TUEV
Fine-tuningPart
BalancedAccuracy AUC-PR AUROC BalancedAccuracy Cohen’sKappa WeightedF1
All 0.8140±0.0019 0.8965±0.0016 0.9022±0.0009 0.6409±0.0065 0.6637±0.0093 0.8312±0.0052
Transformer(12) 0.8141±0.0022 0.8963±0.0014 0.9022±0.0009 0.6541±0.0250 0.6782±0.0189 0.8386±0.0090
Transformer(8) 0.8134±0.0022 0.8960±0.0019 0.9020±0.0009 0.6611±0.0152 0.6820±0.0089 0.8406±0.0036
Transformer(4) 0.8074±0.0032 0.8930±0.0065 0.8967±0.0018 0.6188±0.0118 0.6560±0.0233 0.8256±0.0114
LinearProbe 0.7954±0.0059 0.8864±0.0030 0.8835±0.0028 0.3461±0.0225 0.3968±0.0329 0.6974±0.0161
L ABLATION ON SPATIAL EMBEDDINGS
Thespatialembeddingshavehelpedusaddressthechallengeofheterogeneityinelectrodeconfig-
urations. However,itisimportanttoverifytheeffectivenessofthisapproach. Duringpre-training,
we observed that the loss could not converge without spatial embeddings. This was expected, as
themodelneedsspatialembeddingstoidentifythemaskedpatchtoreconstruct. Duringfine-tuning
ondownstreamdatasets,wediscardthespatialembeddingsandnoticeasignificantdropinperfor-
mance, as shown in Table 11. This clearly demonstrates the importance of spatial embeddings in
capturingspatialinformation.
Table11: Ablationstudyofspatialembeddings(SE).
TUAB TUEV
BalancedAccuracy AUC-PR AUROC BalancedAccuracy Cohen’sKappa WeightedF1
LaBraM 0.8140±0.0019 0.8965±0.0016 0.9022±0.0009 0.6409±0.0065 0.6637±0.0093 0.8312±0.0052
w/oSE 0.8004±0.0037 0.8922±0.0023 0.8888±0.0018 0.5949±0.0423 0.6069±0.0248 0.8040±0.0111
M DISCUSSION
Limitations.Firstofall,althoughwehavecollectedthelargestEEGdataseteverofover2,500hours
and trained the largest model with 369M parameters ever for BCI, it still has a large margin from
today’slargevisionmodelsandlargelanguagemodels. Ourworkisonlythefirststeptoexplorethe
feasibilityoftrainingalargeEEGmodelforlearninggenericrepresentations. Itisdelightedtofind
thattrainingalargeEEGmodelwithtremendousEEGdatadoesworkandobtainappreciableper-
formancegaincomparedtoexistingmethodsdevelopedforspecificBCItasks. Secondly,LaBraM
needstobefullyfine-tunedtoadapttodownstreamtasks,whichmightbecomputation-costlyand
memory-costly. Finally,LaBraMistrainedwithunimodalEEGdata. Itisworthwhiletoinvestigate
traininglargeEEGmodelswithothermodalities.
Outlook. In view of the above limitations, our paradigm paves the way for further research, en-
compassing the following aspects: 1) Collecting more EEG data from a variety of BCI tasks, and
training a larger EEG model to see whether emergent abilities exist in the EEG model similar to
large language models; 2) Leveraging the parameter efficient learning methods, such as adapters,
prompttuning,andLoRA,toreducethefine-tuningoverheadandsavespacefordisks;3)Incorpo-
ratingothermodalitieslikeimage,language,speech,andotherphysiologicalsignalsintolargeEEG
models training to build new paradigms, or aligning EEG representations with other modalities in
semanticspace,whichcanbeameaningfulandchallengingdirectionforfuturework.
22