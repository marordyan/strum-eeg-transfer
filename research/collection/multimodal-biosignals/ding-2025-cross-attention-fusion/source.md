TYPEOriginalResearch
PUBLISHED11December2025
DOI10.3389/fpsyt.2025.1713559
|     | Multimodal |     |             | physiological |     |     |       | signal |     |
| --- | ---------- | --- | ----------- | ------------- | --- | --- | ----- | ------ | --- |
|     | emotion    |     | recognition |               |     |     | based |        | on  |
OPENACCESS
|     | multi-head |     |     | cross |     | attention |     |     | with |
| --- | ---------- | --- | --- | ----- | --- | --------- | --- | --- | ---- |
EDITEDBY
TaoWang,
NorthwesternPolytechnicalUniversity,China
|     | representation |     |     |     | learning |     |     |     |     |
| --- | -------------- | --- | --- | --- | -------- | --- | --- | --- | --- |
REVIEWEDBY
XiangyuKe,
ZhejiangUniversity,China
| WeiZhang, | Shihang | Ding, | Lin Ma | and Haifeng |     | Li* |     |     |     |
| --------- | ------- | ----- | ------ | ----------- | --- | --- | --- | --- | --- |
KarolinskaInstitutet(KI),Sweden
FacultyofComputing,HarbinInstituteofTechnology,Harbin,China
*CORRESPONDENCE
HaifengLi
lihaifeng@hit.edu.cn
|     | Introduction: | Physiological |     | signals | offer | a significant | advantage |     | in the field of |
| --- | ------------- | ------------- | --- | ------- | ----- | ------------- | --------- | --- | --------------- |
RECEIVED26September2025
REVISED30October2025 emotionrecognitionduetotheirobjectivenature,astheyarelesssusceptibleto
ACCEPTED06November2025 volitional control and thus provide a more veridical reflection of an individual's
PUBLISHED11December2025
trueaffectivestate.Theuseofmultimodalphysiologicalsignalsenablesamore
CITATION holistic characterization of emotions, establishing multimodal emotion
DingS,MaLandLiH(2025)Multimodal
physiologicalsignalemotionrecognition recognition as a critical area of research. However, existing multimodal fusion
basedonmulti-headcrossattentionwith methodsoftenfailtocapturethecomplex,dynamicinteractionsandcorrelations
representationlearning.
Front.Psychiatry16:1713559. between different modalities. Consequently, they exhibit limitations in fully
doi:10.3389/fpsyt.2025.1713559 leveraging complementary information from other physiological signals during
| COPYRIGHT | thefeaturelearningprocess. |     |     |     |     |     |     |     |     |
| --------- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
©2025Ding,MaandLi.Thisisanopen- Methods: To address these shortcomings, we propose a novel framework for
accessarticledistributedunderthetermsof
theCreativeCommonsAttributionLicense multimodal physiological emotion recognition. This framework is designed to
(CCBY).Theuse,distributionorreproduction comprehensively learn and extract features from multiple modalities
inotherforumsispermitted,providedthe
|     | simultaneously, |     | effectively | simulating |     | the integrative |     | process | of human |
| --- | --------------- | --- | ----------- | ---------- | --- | --------------- | --- | ------- | -------- |
originalauthor(s)andthecopyrightowner(s)
|     | emotion | perception. |     | It utilizes | a dual-branch |     | representation |     | learning |
| --- | ------- | ----------- | --- | ----------- | ------------- | --- | -------------- | --- | -------- |
arecreditedandthattheoriginalpublication
inthisjournaliscited,inaccordancewith
|     | architecture | to  | process | electroencephalography |     |     | (EEG) | and peripheral | signals |
| --- | ------------ | --- | ------- | ---------------------- | --- | --- | ----- | -------------- | ------- |
acceptedacademicpractice.Nouse,
|     | separately, | providing |     | high-quality | inputs | for | subsequent |     | feature fusion. |
| --- | ----------- | --------- | --- | ------------ | ------ | --- | ---------- | --- | --------------- |
distributionorreproductionispermitted
whichdoesnotcomplywiththeseterms. Furthermore, we employ a cross attention mechanism tailored for multimodal
signalstofullyexploittherichnessandcomplementarityoftheinformation.This
|     | approach | not        | only improves | the            | accuracy | of         | emotion | recognition | but also   |
| --- | -------- | ---------- | ------------- | -------------- | -------- | ---------- | ------- | ----------- | ---------- |
|     | enhances | robustness |               | against issues | such     | as missing |         | modalities  | and noise, |
therebyachievingpreciseclassificationofemotionsfrommultimodalsignals.
|     | Results: | Experimental |     | results on | the public | DEAP | and | SEED-IV | multimodal |
| --- | -------- | ------------ | --- | ---------- | ---------- | ---- | --- | ------- | ---------- |
confirm
|     | physiological | signal | datasets |     | that | our proposed |     | model | demonstrates |
| --- | ------------- | ------ | -------- | --- | ---- | ------------ | --- | ----- | ------------ |
superiorperformanceintheemotionclassificationtaskcomparedtootherstate-
findings
|     | of-the-art | models. | Our | prove | that | the proposed |     | model | can effectively |
| --- | ---------- | ------- | --- | ----- | ---- | ------------ | --- | ----- | --------------- |
extractandfusefeaturesfrommultimodalphysiologicalsignals.
Discussion:Theseresultsunderscorethepotentialofourmodelinthedomainof
affectivecomputingandholdsignificantimplicationsforresearchinhealthcare
andhuman-computerinteraction.
KEYWORDS
emotionrecognition,multimodal,crossattention,featurefusion,physiologicalsignal
| FrontiersinPsychiatry |     |     | 01  |     |     |     |     |     | frontiersin.org |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- |

Dingetal. 10.3389/fpsyt.2025.1713559
1 Introduction signals. This process involves collecting and processing these
signals and applying machine learning or deep learning
Emotion, a cerebral response to specific stimuli, constitutes a techniques to accurately identify and classify human emotions
crucial component of human intelligence (1). The endeavor to (19). Yin et al. (20) proposed an ensemble classifier based on a
integrateemotionasakeyfactorinHuman-ComputerInteraction multilayer-fused stacked autoencoder (MESAE) to recognize
(HCI) and to endow machines with the capacity to perceive and emotions, wherein hidden layer neurons extract high-level
understandhumanemotionshasrapidlyevolvedintoaburgeoning features from each modality, achieving good recognition
interdisciplinaryresearchfieldknownasAffectiveComputing(2). performance. Tang et al. (21) extended the traditional
Affective Computing operates at the intersection of cognitive autoencoder by proposing a bimodal deep denoising autoencoder
science and computer science, with the goal of enabling thatalso considers temporal information for multimodal emotion
computers to recognize, interpret, and even express emotions, recognition. Qiu et al. (22) introduced a multi-view emotion
thereby developing artificial intelligence capable of emotional recognition framework using Deep Canonical Correlation
perception, comprehension, and regulation (3). With the Analysis (DCCA), which jointly learns the parameters of multi-
advancement of AI, emotion recognition technologies have view nonlinear transformations to maximize their correlation,
progressed significantly, paving the way for more effective and finding that DCCA effectively learns highly correlated
intuitivehuman-computercommunication.Asaprimaryresearch representations to improve classification accuracy. Zhu et al. (23)
direction within Affective Computing, emotion recognition has employed a Multi-Hypergraph Neural Network (MHGNN) to
found extensive applications across diverse domains, including identify emotions from physiological signals, using a multi-
human-computer interaction, education and teaching, and hypergraph structure to represent inter-subject correlations and
medicalrehabilitation(4–6). generating a hypergraph for each physiological signal type, which
Traditionalmethodsforemotionrecognitionoftenrelyonovert moreaccuratelydepictedthetruebiologicalresponseprocess.Wu
cues such as facial expressions, voice, and text (7). In contrast, et al. (24) proposed an emotion-related key subnet selection
physiological signals are less susceptible to conscious control and algorithm and used DCCA to pass network features along with
influence,andtheyreflectanindividual’strueemotionalstate,thus eye-tracking features to a multimodal model, achieving accurate
affording them greater reliability and robustness in the field of miningofinter-channelinformation.Chengetal.(25)introduceda
emotion recognition (8). As emotional responses and changes are densegraphconvolutionalnetworkbasedonajointcrossattention
intrinsicallylinkedtothenervoussystem,theyinducereactionsin mechanism to integrate the spatial topology, consistency, and
various physiological signals, including electroencephalography complementarity of multimodal data within a unified network
(EEG), electromyography (EMG), galvanic skin response (GSR), framework, performing intra-modal and inter-modal cross
and electrocardiography (ECG) (9–12). Among these, EEG has attention fusion according to the characteristics of each modality.
become a primary focus for physiological signal-based emotion Their experimental results demonstrated that the model could
recognition dueto its advantages, such asbeingnon-invasive and effectivelyextractandfusemultimodalfeatures.
havingahightemporalresolution,whichallowsforbettercapture While significant progress has been made in emotion
ofthedynamicchangesinbrainactivityduringaffectiveprocessing recognition using multimodal physiological signals, several key
(13).Furthermore,sinceeye-trackingdatareflectsthebrain’svisual shortcomings persist. The evolution of emotion is manifested not
attention and cognitive load—both closely related to emotion onlyin thedynamics of asingle signal but, more critically, in the
processing—the fusion of EEG with other concurrently recorded complex synergistic changes between brain states and peripheral
modalities like eye-tracking and GSR is attracting increasing signals. Simple fusion methods, such as feature concatenation or
attention from researchers (14). Despite progress, emotion averaging,merely“stack”informationtogetherandareincapableof
recognition based on a single modality still faces significant capturing the dynamic, non-linear interactions between different
bottlenecks, as unimodal signals suffer from insufficient modalities. Furthermore, early fusion approaches, which
informational richness, signal noise, and individual differences, concatenate raw signals before feeding them into a neural
limiting the broader application of these techniques (15). Under network, produce a single mixed feature sequence. This approach
thecombinedinfluenceoffactorssuchastime,subjectvariability, failstocapturetheintricate,dynamicinteractionsandcorrelations
andemotionalstate,emotionregulationmechanismsleadtodiverse between modalities and, critically, precludes the use of more
physiological responses, corresponding to complex multimodal sophisticated fusion mechanisms. The focus of other mainstream
physiologicalsignals(16).Therefore,fusingmultiplephysiological architectures (such as GNNs) is intra-modal. They explicitly and
modalitiesiswidelyregardedasapromisingsolutionforbuilding meticulously model the spatial dependencies between EEG
robustandstableemotionrecognitionsystems(17).Byintegrating electrodes by constructing graph structures. This is undoubtedly
EEG with other physiological signals, a more comprehensive powerfulinsingle-modalityEEGanalysis.Incontrast,thefocusof
description and characterization of emotional states can be ourframeworkisinter-modal.Thecoretaskofourdesignedcross-
achieved(18). attention module is to dynamically capture the complex
Emotionrecognitionbasedonmultimodalphysiologicalsignals correlationsbetweentheEEGfeaturesequenceandtheperipheral
primarily investigates the process of analyzing an individual’s signal feature sequence. A primary advantage of our architecture
affective state through the synthesis of multiple physiological lies in its modular dual-branch design. It first respects the
FrontiersinPsychiatry 02 frontiersin.org

Dingetal. 10.3389/fpsyt.2025.1713559
heterogeneity of the different modalities by learning the temporal 2 Materials and methods
dynamic features of each modality in separate, independent
branches. The benefit of this design is that it provides two high- 2.1 Datasets
quality, information-pure, and decoupled high-order feature
sequences for the subsequent cross-attention module. This stands Toevaluatetheperformanceofourproposedmodel,weutilized
instarkcontrasttoearlyfusion(whichmixesrawsignals)orGNNs twopubliclyavailablemultimodalemotiondatasets:DEAP(26)and
(which focus on internal EEG topology). Consequently, how to SEED-IV(27).Thespecificsofthesedatasetsaredetailedbelow.
effectivelyleverageinformationfromotherphysiologicalmodalities TheDatabaseforEmotionAnalysisusingPhysiologicalSignals
for feature learning and how to optimally fuse these signals for (DEAP) is a multimodal dataset collected for emotion research
superior emotion recognition performance have become pressing through cognitive experiments. In the experimental paradigm,
challenges to be addressed. Therefore, a new fusion framework is music videos were used as stimuli to elicit emotional responses
needed—onethatcanindependentlymodeleachmodalityand,on fromparticipants.Thedatasetcomprisesphysiologicaldatafrom32
that basis, achieve deep inter-modal fusion in a more robust and participants (16 male, 16 female) across a total of 48 channels,
flexiblemanner. including electroencephal ography (EEG), electrooculography
To address the aforementioned problems in the field of (EOG), and galvanic skin response (GSR). The EEG signals were
multimodal emotion recognition, this paper proposes a method acquired at a sampling rate of 512 Hz using a 32-channel system
based on cross attention and representation learning. The overall arranged according to the international 10–20 standard. The
framework of the proposed model is illustrated in Figure 1. The remaining channels include 12 peripheral physiological signals, 3
maincontributionsofthisworkareasfollows:First,weproposea unused channels, and 1 status channel. During the experiment,
multimodal physiological emotion recognition framework that participantswereaskedtowatch40one-minute-longmusicvideos,
comprehensively learns and extracts information from multiple eachassociatedwithadifferentemotionaltone.Afterviewingeach
modalities, aiming to effectively model the processes of human video, participants performed a self-assessment, rating their levels
emotion perception and recognition. Second, we design a of valence, arousal, and other dimensions on a scale from 1 to 9.
dual-branch representation learning architecture to process Eachdatatrialis63secondsinduration,whichincludesa3-second
electroencephalography (EEG) and peripheral signals separately, baselinerecordingpriortotheformalexperimentand60secondsof
which provides ideal inputs for subsequent feature fusion and datacollectedduringthevideoviewing.
enhances the model’s interpretability through its modular design. TheSJTUEmotionEEGDatasetIV(SEED-IV)isamultimodal
Third,wedesignamulti-headcrossattentionmechanismtailored datasetcollectedbyProfessorBao-LiangLu’steamatShanghaiJiao
for multimodal signals to fully leverage the richness and TongUniversity,containingbothEEGandeye-trackingdata.The
complementarity of the information, improving emotion experimentemployedemotionalfilmclipstoinduceaffectivestates
recognition accuracy while better handling issues such as modal- inthesubjects.Comparedtootherstimulisuchasaudioormusic
specific noise and missing data to achieve accurate classification. alone,filmclipsofferasignificantadvantageastheyintegrateboth
Finally, we conducted comprehensive and rigorous comparative videoandaudiochannels,providingamoreimmersiveandrealistic
experiments against several representative baseline models. The scenario for the participants, thereby eliciting stronger and more
results demonstrate that our proposed method significantly authentic emotional and psychological changes. To ensure clarity,
improves the performance of emotion recognition from eachvideoclipwasselectedtoinduceasingle,discrete emotional
multimodal physiological signals, effectively validating the category. The stimuli for the dataset were chosen from 24 video
superiorityofourmodel. clipsofvaryingemotionalcontent,eachapproximately2minutesin
FIGURE1
Theoverallframeworkoftheproposedmodel.
FrontiersinPsychiatry 03 frontiersin.org

| Dingetal. |     |     |     |     |     |     |     |     |     |     |     | 10.3389/fpsyt.2025.1713559 |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- |
length. The dataset encompasses four distinct emotion classes: Independent Component Analysis (ICA) was employed to
happy, neutral, sad, and fear. A total of 15 subjects (8 female, 7 identify and remove these artifacts. Following this, the cleaned
male) participated in the experiment. EEG signals were EEG signals were decomposed into five frequency bands via
filtering:delta(d,1–4Hz),theta(q,4–8Hz),alpha(a,8–14Hz),
| continuously | recorded | at  | a sampling | rate | of 1000 | Hz using | a 64- |     |     |     |     |     |     |     |     |
| ------------ | -------- | --- | ---------- | ---- | ------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
channelNeuroscansystem,withelectrodesplacedaccordingtothe beta(b,14–31Hz),andgamma(g,31–50Hz).
standard10–20system.Eye-trackingdatawerecollectedusingSMI-
| ETG eye-tracking            |     | glasses.      | Figure                     | 2 shows   | a schematic  | diagram          | of      |                 |     |                |     |     |          |     |     |
| --------------------------- | --- | ------------- | -------------------------- | --------- | ------------ | ---------------- | ------- | --------------- | --- | -------------- | --- | --- | -------- | --- | --- |
|                             |     |               |                            |           |              |                  |         | 2.3 Dual-branch |     | representation |     |     | learning |     |     |
| the experimental            |     | procedure     | for                        | affective | EEG          | data collection. |         |                 |     |                |     |     |          |     |     |
| Figure 3 illustrates        |     | the electrode |                            | position  | distribution | for              | the two | module          |     |                |     |     |          |     |     |
| datasetsusedinthisstudy.The |     |               | detailsoftheDEAPandSEED-IV |           |              |                  |         |                 |     |                |     |     |          |     |     |
datasetarepresentedinTable1. Forthetaskofmultimodalemotionclassification,wedesigneda
dual-brancharchitecturetoextractfeaturesandrecognizeemotions
|     |     |     |     |     |     |     |     | from electroencephalography |     |     | (EEG) | and | peripheral | signals | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | ----- | --- | ---------- | ------- | --- |
2.2 Data preprocessing separatestreams.ThemodelarchitectureisillustratedinFigure1.
|         |      |          |     |              |      |               |     | It should | be noted      | that for | the DEAP | dataset, | peripheral |         | signals |
| ------- | ---- | -------- | --- | ------------ | ---- | ------------- | --- | --------- | ------------- | -------- | -------- | -------- | ---------- | ------- | ------- |
|         |      |          |     |              |      |               |     | refers to | physiological | signals  | such     | asGSR    | and EOG,   | whereas | for     |
| For the | DEAP | dataset, | we  | followed the | same | preprocessing |     |           |               |          |          |          |            |         |         |
theSEED-IVdataset,itreferstoeye-trackingsignals.Bothbranches
procedureasdescribedinLiuetal.(28).First,theinitial3-second
|                  |             |         |           |            |             |           |         | share an       | identical   | network           | architecture, |            | which  | is designed    | to  |
| ---------------- | ----------- | ------- | --------- | ---------- | ----------- | --------- | ------- | -------------- | ----------- | ----------------- | ------------- | ---------- | ------ | -------------- | --- |
| baseline period  | was         | removed | from      | the raw    | EEG         | data. The | signals |                |             |                   |               |            |        |                |     |
|                  |             |         |           |            |             |           |         | hierarchically | extract     | dynamic           | features      | indicative |        | of emotional   |     |
| were then        | downsampled |         | to        | a sampling | rate        | of        | 128 Hz. |                |             |                   |               |            |        |                |     |
|                  |             |         |           |            |             |           |         | states from    | the         | input time-series |               | data. Each | branch | receives       | a   |
| Electrooculogram |             | (EOG)   | artifacts | were       | removed     | using     | the     |                |             |                   |               |            |        |                |     |
|                  |             |         |           |            |             |           |         | preprocessed   | time-series | segment           |               | as input.  | This   | input sequence |     |
| method           | detailed    | in the  | original  | DEAP       | publication |           | (26).   |                |             |                   |               |            |        |                |     |
first
|               |     |           | filter |         |      |        |        | passes   | through    | a one-dimensional |       |          | convolutional |      | layer |
| ------------- | --- | --------- | ------ | ------- | ---- | ------ | ------ | -------- | ---------- | ----------------- | ----- | -------- | ------------- | ---- | ----- |
| Subsequently, | a   | band-pass |        | between | 4 Hz | and 45 | Hz was |          |            |                   |       |          |               |      |       |
|               |     |           |        |         |      |        |        | (Conv1D) | to capture | low-level,        | local | temporal | patterns      | from | the   |
appliedtoeliminatelow-frequencydriftandhigh-frequencynoise.
rawfeatures.ForaninputXandthej-thconvolutionalkernelW,
Finally, the preprocessed EEG signals were decomposed into four j
|     |     |     |     |     |     |     |     | the corresponding |     | output | feature | map | Y is | calculated | by  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------ | ------- | --- | ---- | ---------- | --- |
distinct frequency bands using filtering: theta (q, 4–8 Hz), alpha j
(a,8–13Hz),beta(b,13–30Hz),andgamma(g,30–45Hz). Equation 1: where s represents the activation function, and W
j
|          |          |          |     |              |                   |             |       | andb arethelearnablekernelweightsandbiastermofthelayer, |     |     |     |     |     |     |     |
| -------- | -------- | -------- | --- | ------------ | ----------------- | ----------- | ----- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| For the  | SEED-IV  | dataset, | we  | adopted      | the preprocessing |             | steps | j                                                       |     |     |     |     |     |     |     |
|          |          |          |     |              | first             |             |       | respectively.                                           |     |     |     |     |     |     |     |
| outlined | in [25]. | The raw  | EEG | signals were |                   | downsampled |       |                                                         |     |     |     |     |     |     |     |
to200Hz.Aband-passfilterfrom1Hzto70Hzwasthenapplied
|             |            |     |         |           |       |     |        |     |     | Y =s(Conv (X,W)+b) |     |     |     |     | (1) |
| ----------- | ---------- | --- | ------- | --------- | ----- | --- | ------ | --- | --- | ------------------ | --- | --- | --- | --- | --- |
|             |            |     |         |           |       |     |        |     |     | j                  |     | j   | j   |     |     |
| to the data | to isolate | the | desired | frequency | range | and | remove |     |     |                    |     |     |     |     |     |
power-line interference. As EEG signals recorded during the Thisisfollowedbyamax-poolinglayer(MaxPooling1D),which
|            |      |              |     |                 |     |            |     | serves to | increase | the receptive | field | of subsequent |     | layers | while |
| ---------- | ---- | ------------ | --- | --------------- | --- | ---------- | --- | --------- | -------- | ------------- | ----- | ------------- | --- | ------ | ----- |
| experiment | were | contaminated |     | by eye-movement |     | artifacts, |     |           |          |               |       |               |     |        |       |
FIGURE2
SEED-IVdatasetemotionperceptionexperimentalparadigm.
| FrontiersinPsychiatry |     |     |     |     |     |     |     | 04  |     |     |     |     |     | frontiersin.org |     |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |

Dingetal. 10.3389/fpsyt.2025.1713559
FIGURE3
Distributionofelectrodepositionsfortwodatasets.
reducingcomputationalcomplexity.Toimprovetrainingefficiency 2.4 Multi-head attention mechanism
and model stability, a Batch Normalization layer is incorporated.
For a given activation value x i at the input to this layer, its To facilitate the effective extraction of features from each
normalizedoutput,denotedasx^ i ,iscalculatedbyEquation2: signal modality, our model incorporates an attention mechanism,
x^ i =g p x ffi s iffiffi − ffi 2 ffiffiffi m + ffiffiBffiffi ∈ ffiffiffiffi+b (2) f c o o r m w pu h t i a c t h ion S a c l ale u d nit D . o T t- h P e ro o d u u tp ct ut A o tt f en th ti e on att s e e n r t v i e o s n a f s un th ct e io c n or i e s
B mathematicallydefinedbyEquation3:
Finally, a Dropout layer is applied to randomly deactivate a !
fraction of neurons, effectively preventing model overfitting. QKT
Attention(Q,K,V)=softmax pffiffiffiffiffi V (3)
Through the cascaded processing of three such convolutional d
k
blocks, the original features are ultimately transformed into a
where Q represents the Query matrix, K represents the Key
high-level feature sequence. This output sequence is not only
matrix,andVrepresentstheValuematrixandd isthedimension
effectively downsampled in the temporal dimension but also k
oftheK.
encapsulates key dynamic patterns from the original features
To enable the model to learn associations between different
across different time scales. This feature sequence then serves as
representation subspaces of the various modalities and to further
theinputforthesubsequentmulti-headcrossattentionmodulefor
enhance its expressive power, this study employs a multi-head
thedeepfusionofmultimodalinformation.
attentionmechanism.Thisinvolvesperformingh,independentlinear
projectionsofQ,K,V,andthenfeedingtheseprojectedversionsinto
TABLE1 DetailsoftheDEAPandSEED-IVdataset. their respective Scaled Dot-Product Attention modules in parallel,
enabling simultaneous attention to information from different
Database DEAP SEED-IV representationsubspaces.Thespecificprocessisasfollows:
Subjects 32 15 TheinputQ,K,Vareeachlinearlytransformedusinghdistinct
setsoflearnableweightmatrices
( WQ,WK,WV)
togeneratehsets
Stimulus Musicalvideos Movieclips i i i
of lower-dimensional queries, keys, and values. We obtain the
Trials 40 24
followingformulaEquation4.
Sessions 1 3
head =Attention
( QWQ,KWK,VWV)
(4)
Datamodalities 7 2 i i i i
Samplingrate 128 200
whereW
i
Q ∈Rdk =h,W
i
K ∈Rdk =h,W
i
V ∈Rdv =h Thehattention
headsthencomputetheScaledDot-ProductAttentioninparallel,
Emotionalclasses 2 4
generating h output matrices. Subsequently, the outputs of these
FrontiersinPsychiatry 05 frontiersin.org

Dingetal. 10.3389/fpsyt.2025.1713559
headsareconcatenated.Finally,theconcatenatedmatrixispassed DE features were computed using a Short-Time Fourier
throughalinearprojectionmatrixWtomapitbacktotheoriginal Transform (STFT) with a 4-second non-overlapping Hanning
model dimension, yielding the final output of the multi-head window. The other peripheral physiological signals were also
attentionlayerbyEquation5. downsampled to 128 Hz, had the initial 3-second baseline
removed, and were segmented into 60-second trials. These
MultiHead(Q,K,V)=Concat (head ,…,head ) W (5)
1 h peripheral data were consolidated into 8 channels, including 2
electrooculogram (EOG) channels, 2 electromyogram (EMG)
channels, 1 galvanic skin response (GSR) channel, 1 skin
2.5 Multimodal cross attention module temperature (SKT) channel, 1 respiration (RSP) channel, and 1
blood volume pressure (BVP) channel. For each of these 8
To capture the complex, dynamic relationships between the two peripheral channels, we calculated the mean, variance, and
signal modalities, the representation of one modality is used as the entropy, resulting in a peripheral feature vector of 24
Query to attend to relevant parts of the other modality, thereby dimensions(8channels×3features).
enabling an effective fusion of the multimodal signals. Specifically, For the SEED-IV dataset, we extracted Differential Entropy
each new feature vector in an enhanced sequence is computed by
(DE)featuresfromthefivepreprocessedEEGfrequencybands,also
takingaweightedsumofthefeaturesfromtheentireperipheralsignal usinganSTFTwitha4-secondnon-overlappingHanningwindow.
sequence. The weights are determined by the degree of relevance For the 62 EEG channels, this process resulted in a final feature
between the current EEG feature and all features in the peripheral dimension of 62 × 5 = 310. The eye-tracking features, extracted
sequence.Themultimodalcrossattentionmodulethusestablishesan from the SMI eye-tracking glasses, included both statistical and
accurate correspondence between patterns in the EEG signal and computed metrics. All 31 eye-tracking features used in this study
relevant information within the peripheral signals. Furthermore, to aredetailedinTable2.
enablethemodeltolearnassociationsfromdifferentperspectivesand DifferentialEntropy(DE)isafeaturethatisfrequentlyusedin
subspaces,amulti-headattentionmechanismisused.Theoutputsof emotionrecognition andhas demonstrated excellent classification
theindividuallycomputedattentionheadsareconcatenatedtofurther capability. DE is an extension of Shannon entropy to continuous
enhancethemodel’sexpressivepower. variables,quantifyingthetotaluncertaintyofacontinuousrandom
Let Attention represent the cross attention output derived variable’s probability distribution. It effectively reflects the
EEG
fromtheelectroencephalogram(EEG)signals,andletAttention frequency characteristics of EEG signals. An EEG signal within a
PERI
represent the cross attention output derived from the peripheral shorttimeintervalcanbeapproximatedbyaGaussiandistribution,
device signals. These two outputs are then fused to form a final and can thus be characterized by its Gaussian probability
featurerepresentationasEquations6,7. density function. The DE for an EEG signal that follows a
Gaussian distribution is approximated as the logarithm of its
Attention EEG =MultiHead(Q PERI ,K EEG ,V EEG ) (6) power spectral density within a specific frequency band.
Attention =MultiHead(Q ,K ,V ) (7)
PERI EEG PERI PERI TABLE2 Summaryofextractedeyemovementfeatures.
During model training, the resulting feature vector is passed
Eyemovement
through a fully connected layer for dimensionality reduction and is Extractedfeatures
parameters
then used to generate prediction labels and the final classification
outcome. To evaluate the classification results of our model, we use Mean,standarddeviation,
Accuracyastheperformancemetric,definedasfollowsbyEquation8: Pupildiameter(Xand DEinfourbands
Y) (0.2Hz,0.2-0.4Hz,
0.4-0.6Hz,0.6-1Hz)
(TP+TN)
Accuracy= (8)
(TP+TN+FP+FN) Disperson(XandY) Mean,standarddeviation
This formula is presented as an example for a binary Fixationduration(ms) Mean,standarddeviation
classification task. The denominator represents the total number Blinkduration(ms) Mean,standarddeviation
ofsamples,whichisthesumofTruePositives(TP),TrueNegatives
Meanandstandarddeviationofsaccadeduration
(TN), False Positives (FP), and False Negatives (FN). The Saccade (ms)andsaccadeamplitude(°)
numerator is the sum of TP and TN, which corresponds to the
Blinkfrequency
totalnumberofcorrectlypredictedsamples. fixationfrequency
fixationdurationmaximum
fixationdispersiontotal
2.6 Feature engineering Eventstatistics fixationdispersionmaximum
saccadefrequency
saccadedurationaverage
FortheDEAPdataset,weextractedDifferentialEntropy(DE) saccadeamplitudeaverage
saccadelatencyaverage
features from the four preprocessed EEG frequency bands. The
FrontiersinPsychiatry 06 frontiersin.org

| Dingetal. |     |     |     |     |     |     | 10.3389/fpsyt.2025.1713559 |     |     |
| --------- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- |
The mathematical expression of this calculation is as follows by classification task based on the combined valence-arousal
Equation9: space (HAHV, HALV, LAHV, LALV). For the SEED-IV dataset,
afour-classclassificationexperimentwasconductedtodistinguish
Z
b
=− amonghappy,neutral,sad,andfearemotionalstates.Regardingthe
| DE  | f(x)log (f(x))dx                          |                                             |         |                                                 |     |     |     |     |     |
| --- | ----------------------------------------- | ------------------------------------------- | ------- | ----------------------------------------------- | --- | --- | --- | --- | --- |
|     | a                                         |                                             |         | five-foldcross-validationondatafromallsubjects. |     |     |     |     |     |
|     | Z                                         | (cid:3)                                     | (cid:4) |                                                 |     |     |     |     |     |
|     | (x−m)2                                    | (x−m)2                                      |         |                                                 |     |     |     |     |     |
|     | b 1                                       | 1                                           |         |                                                 |     |     |     |     |     |
|     | =− pffiffiffiffiffiffiffiffiffiffiffiexp  | log  pffiffiffiffiffiffiffiffiffiffiffiexp  | dx      |                                                 |     |     |     |     |     |
|     | 2ps2 2s2                                  | 2ps2 2s2                                    |         |                                                 |     |     |     |     |     |
a
|     |     |     |     | 3.2 Results | and comparison |     |     |     |     |
| --- | --- | --- | --- | ----------- | -------------- | --- | --- | --- | --- |
=1log (2pes2)
2
(9)
TheexperimentalresultsontheDEAPdatasetarepresentedin
|               |                       |         |     | Table 3.           | The method proposed            | in       | this study | achieved     | a mean        |
| ------------- | --------------------- | ------- | --- | ------------------ | ------------------------------ | -------- | ---------- | ------------ | ------------- |
|               |                       |         |     | accuracy           | of 94.88% on the valence       |          | dimension  | and          | 95.26% on the |
| 3 Experiments | and                   | results |     |                    |                                |          |            |              |               |
|               |                       |         |     | arousal dimension. | The results                    | indicate | that       | the proposed | model         |
|               |                       |         |     | achieved           | the best performance           | among    | the        | compared     | methods.      |
| 3.1           | Experimental settings |         |     |                    |                                |          |            |              |               |
|               |                       |         |     | Figure 5           | presents the subject-dependent |          |            | recognition  | accuracy      |
resultsforthe32participantsintheDEAPdataset.
All experiments were conducted using the same hardware and Table4displaystheresultsfortheSEED-IVdataset.Four-class
softwareenvironment,datapartitioningscheme,andhyperparameter emotion recognition task (positive, neutral, and negative), the
settingstoensureconsistencyandfaircomparison.Themodelwas method proposed in this study achieved an accuracy of 89.32%.
implemented on a hardware platform consisting of a Dell desktop Asshowninthetable,thisisthebestresultreportedontheSEED-
computerequippedwithanIntelCorei5-13400@2.50GHzCPUand IV dataset to date. This demonstrates that the cross attention
anNvidiaGeForceRTX3060TiGPU.Thesoftwareenvironmentwas mechanism for multimodal signals proposed in this paper can
based on the Windows 10 operating system, with model fully leverage the informational richness and complementarity
implementationcarriedoutinPython3.9usingthePyTorch1.10.1 betweendifferentmodalities.Itnotonlyimprovestheaccuracyof
deeplearningframework.Fortheproposedmodel,thelossfunction emotionrecognitionbutalsobetterhandlesissuessuchasmissing
wasdefinedasthesumofcross-entropylossandanL2regularization modalities and noise, thereby achieving accurate emotion
classificationfrommultimodalsignals.
term,whichwasminimizedusingtheAdamoptimizer.Duringthe
trainingprocess,thelearningrateandbatchsizeweresetto0.001and To validate the efficacy of our proposed model in extracting
64,respectively.TheFigure4illustratesthetrainingperformanceof high-level, abstract features, we performed a t-SNE visualization
emotionclassificationontheDEAPdataset. analysis.Thisanalysiscomparedthetwo-dimensionaldistribution
classification
For the DEAP dataset, three distinct of Differential Entropy (DE) features from a subset of the dataset
experiments were performed: a binary classification task for beforeandafterbeingprocessedthroughourmodel,withtheresults
|     |     | classification |     |     |     |     |     | figure, |     |
| --- | --- | -------------- | --- | --- | --- | --- | --- | ------- | --- |
valence (High Valence vs. Low Valence), a binary depicted in Figure 6. As is evident in the prior to feature
task for arousal (High Arousal vs. Low Arousal), and a four-class extraction by our model, the samples corresponding to different
FIGURE4
AccuracyandlossforEEGemotionrecognition.
| FrontiersinPsychiatry |     |     |     | 07  |     |     |     |     | frontiersin.org |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- |

| Dingetal. |     |     |     |     |     |     |     | 10.3389/fpsyt.2025.1713559 |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- |
TABLE3 Comparisonofmeanaccuraciesforvalenceandarousal cross attention mechanism. The experimental results on two
classificationontheDEAPdataset.
|     |     |     |     | benchmark | multimodal  | physiological |          | signal | datasets,   | SEED-IV  |
| --- | --- | --- | --- | --------- | ----------- | ------------- | -------- | ------ | ----------- | -------- |
|     |     |     |     | and DEAP, | demonstrate |               | that our | model  | outperforms | existing |
Accuracy(%)
Method methods and achieves state-of-the-art results. On the DEAP
Valence Arousal dataset, we extracted features from the electroencephalography
|     |          |       |       | (EEG) and | peripheral | physiological |     | signals, | which | were then fed |
| --- | -------- | ----- | ----- | --------- | ---------- | ------------- | --- | -------- | ----- | ------------- |
|     | BDAE[29] | 85.20 | 80.50 |           |            |               |     |          |       |               |
intothedual-brancharchitecturetolearnhigh-levelrepresentations
|     | DCCA[28] | 85.62 | 84.33 |          |           |               |     |                |       |           |
| --- | -------- | ----- | ----- | -------- | --------- | ------------- | --- | -------------- | ----- | --------- |
|     |          |       |       | for each | modality. | Subsequently, |     | the multi-head | cross | attention |
HC-MFB[30] 90.46 93.22 mechanism was employed to fully leverage the richness and
|     |               |       |       | complementarity |             | of the information, |             | enabling      | accurate | emotion      |
| --- | ------------- | ----- | ----- | --------------- | ----------- | ------------------- | ----------- | ------------- | -------- | ------------ |
|     | MMResLSTM[31] | 92.30 | 92.87 |                 |             |                     |             |               |          |              |
|     |               |       |       | recognition.    | The         | model’s             | efficacy    | was validated | through  | binary       |
|     | Ours          | 94.88 | 95.26 | classification  |             |                     |             |               |          |              |
|     |               |       |       |                 | experiments |                     | on the      | dimensions    | of       | valence and  |
|     |               |       |       | arousal, where  | it          | achieved            | the highest | recognition   |          | performance. |
emotional categories were severely intermingled and lacked clear On the SEED-IV dataset, using EEG and eye-tracking signals as
separability. In stark contrast, following the deep feature input,ourmodelalsoattainedthebestrecognitionperformanceina
classification
extraction process, the sample distribution became highly four-class task (happy, neutral, sad, and fear). The
structured. The data points formed distinct, well-defined clusters, results across all subjects indicate that our proposed model can
leadingtoasignificantreductioninsampleconfusion.Thisvisual
|     |     |     |     | effectively | process | the multimodal |     | data | for every | participant. |
| --- | --- | --- | --- | ----------- | ------- | -------------- | --- | ---- | --------- | ------------ |
evidence powerfully substantiates our model’s capability to learn Furthermore,theconfusionmatricesprovidedaclearcomparison
classification
and extract potent, discriminative features that are strongly between the results and the ground-truth labels for
correlatedwithemotionalstates. eachdataset.Theaforementionedexperimentalresultscollectively
To intuitively display the prediction performance for each prove that our proposed model can effectively process EEG,
emotion category across the different datasets, and to provide a eye-tracking, and other peripheral physiological signals,
model’s
clear comparison between the predictions and the true successfully extracting salient features and fully utilizing both
labelsforadeeperunderstandingofitsperformance,wecomputed intra-modal and complementary information to achieve accurate
confusionmatricesfortheresultsofourproposedmodel,asshown emotionrecognition.
inFigure7.Inaconfusionmatrix,thesumofelementsineachrow Theefficacyofthisframeworkstemsfromitshierarchicaland
represents the total number of samples for an actual class. The decoupled design philosophy. The dual-branch representation
diagonal elements indicate the percentage of samples correctly learning module first focuses on modeling intra-modal dynamics,
classified
for each emotion, while the off-diagonal elements providing high-quality feature sequences as input for the
representthepercentageofmisclassifiedsamples. subsequent stage. On this foundation, the multi-head cross
|     |     |     |     | attention | module | then focuses | on  | modeling | inter-modal | dynamic |
| --- | --- | --- | --- | --------- | ------ | ------------ | --- | -------- | ----------- | ------- |
interactions.Theeffectivenessofthedual-brancharchitectureliesin
| 4   | Discussion | and conclusion |     |     |     |     |     |     |     |     |
| --- | ---------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
itsabilitytoensurethattheintrinsiccharacteristicsofeachmodality
|     |     |     |     | are optimally | and | specifically | extracted | prior | to fusion, | thereby |
| --- | --- | --- | --- | ------------- | --- | ------------ | --------- | ----- | ---------- | ------- |
In this paper, we have proposed a novel framework for providing high-quality representations for subsequent
|            |               |                     |               | computations. | Unlike | methods |     | that output | only | static feature |
| ---------- | ------------- | ------------------- | ------------- | ------------- | ------ | ------- | --- | ----------- | ---- | -------------- |
| multimodal | physiological | emotion recognition | that combines | a             |        |         |     |             |      |                |
dual-branch representation learning module with a multi-head vectors, each branch in our model outputs a complete feature
FIGURE5
ComparisonofrecognitionresultsforvalenceandarousalacrossallsubjectsintheDEAPdataset.
| FrontiersinPsychiatry |     |     |     | 08  |     |     |     |     |     | frontiersin.org |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- |

| Dingetal. |     |     |     | 10.3389/fpsyt.2025.1713559 |     |
| --------- | --- | --- | --- | -------------------------- | --- |
TABLE4 Comparisonofmeanaccuraciesforemotionrecognitionon sequence that preserves temporal information, laying a solid
theSEED-IVdataset.
|     | foundation | for capturing inter-modal |           | correlations. The | multi- |
| --- | ---------- | ------------------------- | --------- | ----------------- | ------ |
|     | head cross | attention mechanism       | overcomes | the limitations   | of     |
Method Accuracy(%)
|     | traditional | fusion methods, such | as feature | concatenation | or  |
| --- | ----------- | -------------------- | ---------- | ------------- | --- |
DCCA[28] 78.74 averaging. It allows one modality’s representation sequence to
EmotionMeter[27] 85.11 adaptivelyquery another,dynamically assigning attention weights
|     | to precisely | capture the synergistic | activities | that occur during | a   |
| --- | ------------ | ----------------------- | ---------- | ----------------- | --- |
MFFNN[32] 87.06
|     | genuine emotional | response. | Each attention | head focuses | on  |
| --- | ----------------- | --------- | -------------- | ------------ | --- |
Ours 89.12 learning a specific type of cross-modal dependency, and by
|     | integrating | these diverse and complementary |     | correlation patterns, |     |
| --- | ----------- | ------------------------------- | --- | --------------------- | --- |
FIGURE6
FeaturevisualizationbeforeandaftertrainingontheDEAPdataset.
FIGURE7
ConfusionmatrixoftheclassificationresultsontheDEAPdataset.
| FrontiersinPsychiatry | 09  |     |     | frontiersin.org |     |
| --------------------- | --- | --- | --- | --------------- | --- |

| Dingetal. |     |     |     |     |     |     |     |     |     | 10.3389/fpsyt.2025.1713559 |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- |
the model constructs a comprehensive and robust cross-modal specific layers of the model, enabling it to rapidly adapt to their
representation,significantlyenhancingitsexpressivepower.
uniquephysiologicalpatterns.
| In summary, |     | we have | proposed | a   | multimodal | physiological |     |     |     |     |     |
| ----------- | --- | ------- | -------- | --- | ---------- | ------------- | --- | --- | --- | --- | --- |
emotionrecognitionframeworkthatcomprehensivelylearnsfrom
andextractsinformationacrossmultiplemodalities.Wedesigneda Data availability statement
| dual-branch | representation |     | learning | architecture |     | to process | EEG |     |     |     |     |
| ----------- | -------------- | --- | -------- | ------------ | --- | ---------- | --- | --- | --- | --- | --- |
and peripheral signals in separate streams, providing ideal, This study is an experimental analysis of publicly
decoupled inputs for feature fusion. We also introduced a cross available datasets. The SEED-IV data can be found at this web
attention mechanism tailored for multimodal signals, which page: https://bcmi.sjtu.edu.cn/home/seed/seed-iv.html and The
leverages informational richness and complementarity toimprove DEAPdatacanbefoundatthiswebpage:https://www.eecs.qmul.
recognition accuracy while enhancing robustness to noise and ac.uk/mmv/datasets/deap/.
| missing data. | The     | experimental |     | results on | the DEAP | and      | SEED-    |                      |     |     |     |
| ------------- | ------- | ------------ | --- | ---------- | -------- | -------- | -------- | -------------------- | --- | --- | --- |
| IV datasets   | confirm | that         | our | proposed   | model    | exhibits | superior |                      |     |     |     |
|               |         |              |     |            |          |          |          | Author contributions |     |     |     |
performancecomparedtoexistingmodelsinmultimodalemotion
| classification | tasks.The |     | DEAPand | SEED-IVdatasets |     | used | inthis |     |     |     |     |
| -------------- | --------- | --- | ------- | --------------- | --- | ---- | ------ | --- | --- | --- | --- |
|                |           |     |         |                 |     |      |        |     | –   | –   |     |
study were both collected in controlled laboratory environments. SD: Writing original draft. LM: Writing review & editing.
The emotions induced via videos/music in such settings differ HL:Writing–review&editing.
significantly
|             | from | the        | complex,   | spontaneous |         | emotions    |     |     |     |     |     |
| ----------- | ---- | ---------- | ---------- | ----------- | ------- | ----------- | --- | --- | --- | --- | --- |
| experienced | in   | real life. | Therefore, | the         | model’s | performance | in  |     |     |     |     |
Funding
| real-world | scenarios     | remains |       | to be validated. | We  | have             | added a |     |     |     |     |
| ---------- | ------------- | ------- | ----- | ---------------- | --- | ---------------- | ------- | --- | --- | --- | --- |
| discussion | acknowledging |         | that, | as observed      | in  | our experimental |         |     |     |     |     |
results,themodel’sperformancefluctuatesacrossdifferentsubjects. financial
|     |     |     |     |     |     |     |     | The author(s) | declare | support was | received for the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | ----------- | ---------------- |
This indicates that achieving high-accuracy, subject-independent research and/or publication of this article. This work is supported
emotionrecognitionremainsasignificantchallenge,andthemodel
inpartbyspecialfundsoftheNationalNaturalScienceFoundationof
proposed inthispaper hasnotyetfully overcometheproblem of China under Grant 32441112, the National Key R&D Program of
individualdifferences.Ourfindingsdemonstratethattheproposed
China(2022YFC3301800).
| model achieves |     | effective | extraction | and | fusion | of multimodal |     |     |     |     |     |
| -------------- | --- | --------- | ---------- | --- | ------ | ------------- | --- | --- | --- | --- | --- |
model’s
| physiological | features. |     | These | results | underscore | the |     |     |     |     |     |
| ------------- | --------- | --- | ----- | ------- | ---------- | --- | --- | --- | --- | --- | --- |
Conflict
significant potential in the field of emotion recognition and hold of interest
| important | implications |     | for affective | computing, |     | healthcare, | and |     |     |     |     |
| --------- | ------------ | --- | ------------- | ---------- | --- | ----------- | --- | --- | --- | --- | --- |
human-computer interaction research. The insights gained from The authors declare that the research was conducted in the
absenceofanycommercialorfinancialrelationshipsthatcouldbe
| this work | may provide |     | a valuable | reference | for | future studies | in  |     |     |     |     |
| --------- | ----------- | --- | ---------- | --------- | --- | -------------- | --- | --- | --- | --- | --- |
multimodal physiological signal analysis and affective Brain- construedasapotentialconflictofinterest.
| Computer | Interfaces | (BCI). | Despite | the | outstanding | performance |     |     |     |     |     |
| -------- | ---------- | ------ | ------- | --- | ----------- | ----------- | --- | --- | --- | --- | --- |
achievedinthisstudy,thereremainsroomforimprovement.Inour
|     |     |     |     |     |     |     |     | Generative | AI statement |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | --- | --- |
futurework,wewillexplorealternativefeatureextractionmethods
andthefusionofanevenwiderrangeofsignalmodalitiestofurther
model’s
enhance the adaptability and performance. While this The author(s) declare that no Generative AI was used in the
paper validates the effectiveness of the multi-head cross-attention creationofthismanuscript.
Anyalternativetext(alttext)providedalongsidefiguresinthis
mechanismforfusingEEGandperipheralsignals,wewillnotstop
at merely using it as a “black box.” A key future direction is to articlehasbeengeneratedbyFrontierswiththesupportofartificial
conductin-depthvisualizationandqualitative/quantitativeanalysis intelligence and reasonable efforts have been made to ensure
ofthelearnedcross-attentionweightmatrices.Thisaimstoexplore, accuracy, including review by the authors wherever possible.
specific
for emotional states, which dynamic patterns in the EEG Ifyouidentifyanyissues,pleasecontactus.
| signal the | model | has | learned | to strongly | associate | with | which |     |     |     |     |
| ---------- | ----- | --- | ------- | ----------- | --------- | ---- | ----- | --- | --- | --- | --- |
responsesfromtheperipheralsignals.Thisapproachwillenhance
Publisher’s
the model’s interpretability. Exploring Personalized Transfer note
reaffirm
| Learning | to Address | Subject | Variability. |     | Our results |     | that |     |     |     |     |
| -------- | ---------- | ------- | ------------ | --- | ----------- | --- | ---- | --- | --- | --- | --- |
“inter-subjectvariability”isacorechallengeinthisfield.Afuture All claims expressed in this article are solely those of the
affiliated
direction is to leverage the model proposed in this paper as a authors and do not necessarily represent those of their
powerful general feature extractor and specifically investigate organizations, or those of the publisher, the editors and the
personalized transfer learning or domain adaptation techniques. reviewers. Any product that may be evaluated in this article, or
Forexample,whenencounteringanewsubject,weaimtoseeifwe claimthatmaybemadebyitsmanufacturer,isnotguaranteedor
canuseonlyaminimalamountoftheircalibrationdatatofine-tune
endorsedbythepublisher.
| FrontiersinPsychiatry |     |     |     |     |     |     | 10  |     |     |     | frontiersin.org |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- |

Dingetal. 10.3389/fpsyt.2025.1713559
References
1. Wu D, Lu BL, Hu B, Zeng Z. Affective brain–computer interfaces (abcis): A 16. PillalamarriR,ShanmugamU.AreviewonEEG-basedmultimodallearning
tutorial.ProcIEEE.(2023)111:1314–32.doi:10.1109/JPROC.2023.3277471 for emotion recognition. Artif. Intell. Rev. (2025) 58:131. doi: 10.1007/s10462-025-
11126-9
2. PicardRW.Affectivecomputing.Cambridge,Massachusetts:MITpress(2000).
3. KaurS,KulkarniN.Recenttrendsandchallengesinhumancomputerinteraction 17. UdahemukaG,DjouaniK,KurienAM.Multimodalemotionrecognitionusing
usingautomaticemotionrecognition:areview. Int.J.Biometrics.(2024)16:16–43. visual,vocalandphysiologicalsignals:areview.ApplSci.(2024)14:8071.doi:10.3390/
doi:10.1504/IJBM.2024.135160 app14178071
4. MoiseG,DragomirEG,ȘchiopuD,IancuLA.Towardsintegratingautomatic 18. LiuH,LouT,ZhangY,WuY,XiaoY,JensenCS,etal.EEG-basedmultimodal
emotionrecognitionineducation:Adeeplearningmodelbasedon5EEGchannels. emotion recognition: a machine learning perspective. IEEE Trans. Instrum. Meas.
Int.J.Comput.Intell.Syst.(2024)17:230.doi:10.1007/s44196-024-00638-x
(2024)73:1–29.doi:10.1109/TIM.2024.3369130
5. CiraoloD,FazioM,CalabròRS,VillariM,CelestiA.Facialexpressionrecognition 19. LiQ,LiuY,YanF,ZhangQ,LiuC.Emotionrecognitionbasedonmultiple
basedonemotionalartificialintelligencefortele-rehabilitation.Biomed.SignalProcess. physiologicalsignals.Biomed.SignalProcess.Control(2023)85:104989.doi:10.1016/
Control(2024)92:106096.doi:10.1016/j.bspc.2024.106096 j.bspc.2023.104989
6. Panda D, Chakladar DD, Rana S, Parayitam S. An EEG-based neuro- 20. Yin Z, Zhao M, Wang Y, Yang J, Zhang J. Recognition of emotions
recommendation system for improving consumer purchase experience. J. Consum. using multimodal physiological signals and an ensemble deep learning
Behav.(2024)23:61–75.doi:10.1002/cb.2142 model. Comput. Methods Programs Biomed. (2017) 140:93–110. doi: 10.1016/
j.cmpb.2016.12.005
7. ThanapattheerakulT,MaoK,AmorantoJ,ChanJH.Emotioninacentury:A
review of emotion recognition, in: IAIT '18: proceedings of the 10th international 21. TangH,LiuW,ZhengWL,LuBL.(2017).Multimodalemotionrecognition
conferenceonadvancesininformationtechnology.NewYork,NY,USA:Associationfor using deep neural networks, in: Neural Information Processing: 24th International
ComputingMachinery(2018)1–8. Conference,ICONIP2017,Guangzhou,China,November14–18,2017,Proceedings,
PartIVVol.24.pp.811–9.Springer.
8. PanB,HirotaK,JiaZ,DaiY.Areviewofmultimodalemotionrecognitionfrom
datasets, preprocessing, features, and fusion methods. Neurocomputing. (2023) 22. Qiu JL, Liu W, Lu BL. (2018). Multi-view emotion recognition using deep
561:126866.doi:10.1016/j.neucom.2023.126866 canonicalcorrelationanalysis,in:NeuralInformationProcessing:25thInternational
9. DharaT,SinghPK,MahmudM.Afuzzyensemble-baseddeeplearningmodelfor
Conference,ICONIP2018,SiemReap,Cambodia,December13–16,2018,Proceedings,
EEG-based emotion recognition. Cogn. Comput. (2024) 16:1364–78. doi: 10.1007/
PartVVol.25.pp.221–31.Springer.
s12559-023-10171-2 23. ZhuJ,ZhaoX,HuH,GaoY.(2019).Emotionrecognitionfromphysiological
10. MaityS,VeerK.Anapproachforevaluationandrecognitionoffacialemotions signals using multi-hypergraph neural networks, in: 2019 IEEE International
usingEMGsignal.Int.J.Sens.Wirel.Commun.Control(2024)14:113–21.doi:10.2174/ ConferenceonMultimediaandExpo(ICME),.pp.610–5.IEEE.
0122103279260571231213053403 24. WuX,ZhengWL,LiZ,LuBL.InvestigatingEEG-basedfunctionalconnectivity
11. KumarPS,RonickomJFA.Optimalelectrodermalactivitysegmentforenhanced patterns for multimodal emotion recognition. J. Neural Eng. (2022) 19:016012.
emotionrecognitionusingspectrogrambasedfeatureextractionandmachinelearning. doi:10.1088/1741-2552/ac49a7
Int.J.NeuralSyst.(2024)34:2450027–2450027.doi:10.1142/S0129065724500278
25. ChengC,LiuW,FengL,JiaZ.Densegraphconvolutionalwithjointcross-
12. Fang A,Pan F, Yu W,YangL,HeP.ECG-basedemotionrecognitionusing attentionnetworkformultimodalemotionrecognition.IEEETrans.Comput.Soc.Syst.
randomconvolutionalkernelmethod.Biomed.SignalProcess.Control(2024)91:105907. (2024)11:6672–6683.doi:10.1109/TCSS.2024.3412074
doi:10.1016/j.bspc.2023.105907 26. KoelstraS,MuhlC,SoleymaniM,LeeJS,YazdaniA,EbrahimiT,etal.Deap:A
13. QiuS,ChenY,YangY,WangP,WangZ,ZhaoH,etal.Areviewonsemi- databaseforemotionanalysis;usingphysiologicalsignals.IEEETransAffectcomputing.
supervisedlearningforEEG-basedemotionrecognition.Inf.Fusion(2024)104:102190. (2011)3:18–31.
doi:10.1016/j.inffus.2023.102190
27. ZhengWL,LiuW,LuY,LuBL,CichockiA.Emotionmeter:Amultimodal
14. GeethaA,MalaT,PriyankaD,UmaE.Multimodalemotionrecognitionwith frameworkforrecognizinghumanemotions.IEEETrans.Cybern.(2018)49:1110–22.
deep learning: advancements, challenges, and future directions. Inf. Fusion (2024) doi:10.1109/TCYB.2018.2797176
105:102218.doi:10.1016/j.inffus.2023.102218
28. Liu W, Qiu JL, Zheng WL, Lu BL. Comparing recognition performance
15. Tang J, Ma Z, Gan K, Zhang J, Yin Z. Hierarchical multimodal-fusion of and robustness of multimodal deep learning models for multimodal emotion
physiologicalsignalsforemotionrecognitionwithscenarioadaptionandcontrastive recognition. IEEE Trans. Cogn. Dev. Syst. (2021) 14:715–29. doi: 10.1109/
alignment.Inf.Fusion(2024)103:102129.doi:10.1016/j.inffus.2023.102129 TCDS.2021.3071170
FrontiersinPsychiatry 11 frontiersin.org