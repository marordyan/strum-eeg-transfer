Cognitive Computation (2024) 16:455–481
https://doi.org/10.1007/s12559-023-10200-0
State‑of‑the‑Art of Stress Prediction from Heart Rate Variability Using
Artificial Intelligence
Yeaminul Haque1 · Rahat Shahriar Zawad1 · Chowdhury Saleh Ahmed Rony1 · Hasan Al Banna2 · Tapotosh Ghosh3 ·
M. Shamim Kaiser4 · Mufti Mahmud5,6,7
Received: 29 March 2023 / Accepted: 3 September 2023 / Published online: 12 October 2023
© The Author(s) 2023
Abstract
Recent advancements in the manufacturing and commercialisation of miniaturised sensors and low-cost wearables
have enabled an effortless monitoring of lifestyle by detecting and analysing physiological signals. Heart rate variability
(HRV) denotes the time interval between consecutive heartbeats.The HRV signal, as detected by the sensors and devices,
has been popularly used as an indicative measure to estimate the level of stress, depression, and anxiety. For years, artificial
intelligence (AI)-based learning systems have been known for their predictive capabilities, and in recent years, AI models
with deep learning (DL) architectures have been successfully applied to achieve unprecedented accuracy. In order to deter-
mine effective methodologies applied to the collection, processing, and prediction of stress from HRV data, this work presents
an in depth analysis of 43 studies reporting the application of various AI algorithms. The methods are summarised in tables
and thoroughly evaluated to ensure the completeness of their findings and reported results. To make the work comprehensive,
a detailed review has been conducted on sensing technologies, pre-processing methods applied on multi-modal data, and
employed prediction models. This is followed by a critical examination of how various Machine Learning (ML) models,
have been utilised in predicting stress from HRV data. In addition, the reported reseults from the selected studies have been
carefully analysed to identify features that enable the models to perform better. Finally, the challenges of using HRV to
predict stress are listed, along with some possible mitigation strategies. This work aims to highlight the impact of AI-based
stress prediction methodologies from HRV data, and is expected to aid the development of more meticulous techniques.
Keywords HRV · Physiological sensors · Stress prediction · Multi-modal data · Machine Learning · Deep Learning
* Mufti Mahmud 1 Department of ICT, Bangladesh University of Professionals,
mufti.mahmud@ntu.ac.uk; mufti.mahmud@gmail.com Dhaka, Bangladesh
Yeaminul Haque 2 Department of CSE, Bangladesh University of Professionals,
yeaminbijoy1997@gmail.com Dhaka, Bangladesh
Rahat Shahriar Zawad 3 Department of CSE, United International University, Dhaka,
rahatshahriar06@gmail.com Bangladesh
Chowdhury Saleh Ahmed Rony 4 Institute of Information Technology, Jahangirnagar
rony.ict.bup@gmail.com University, Savar, Dhaka 1342, Bangladesh
Hasan Al Banna 5 Department of Computer Science, Nottingham Trent
Hasan.banna@bup.edu.bd University, Clifton Lane, Nottingham NG11 8NS, UK
Tapotosh Ghosh 6 Computing and Informatics Research Centre, Nottingham
tapotosh@cse.uiu.ac.bd; tapotoshghosh@gmail.com Trent University, Clifton Lane, NG11 8NS Nottingham, UK
M. Shamim Kaiser 7 Medical Technologies Innovation Facility, Nottingham Trent
mskaiser@juniv.edu University, Clifton Lane, NG11 8NS Nottingham, UK
Vol.:(0112 33456789)

4 56 Cognitive Computation (2024) 16:455–481
Introduction progress. Behavioural patterns, as well as physiological
data (GSR, EEG, HR), can be collected through smart-
In the human body, numerous receptors such as skin and phones, and by combining these sensor data and smart-
eyes receive external environmental stimuli, transmit the phone records (calls, locations), stress can be predicted
signal to the brain for processing, and then produce a [8]. Video cameras, accelerometers, and touch displays
corresponding response. The harmful stimuli modify the based on data can also be a stress predictor and used for
human body’s internal or external steady-state conditions model construction [9]. However, smartphone-based data
(both physical and chemical). To correct this imbalance, is not that accurate as the sensors are not medical grade.
the human body develops stress in order to maintain a Furthermore, only device-based systems have some situ-
steady state condition, also known as homeostasis [1]. ation-based constraints where it gives poor predictions.
This stress is detected by the body’s sympathetic nervous Figure 1 shows a possible representation of the AI frame-
system, which results in the secretion of hormones such work for predicting stress from multi-modal sensor data. The
as cortisol. The stress hormone increases the blood sugar, EEG parameters and stress questionnaires are the most used
alertness, and blood pressure to supply additional blood mental stress detectors for participants in a contained envi-
flow in the body [2]. ronment. The feature sets by combining EEG measurements
The heart rate (HR) is defined as the number of heart- (distraction, levels of engagement, cognitive state) with sta-
beats per minute. The discrepancy in the time intervals tistical characteristics (mean, median, mode, and variance)
between consecutive heartbeats (interbeat intervals (IBIs)) are used to categorise stress levels into high and low catego-
is considered heart rate variability (HRV). The autonomic ries [10]. But the heterogeneously collected self-reported
nervous system (ANS), a rudimentary nervous system stress questionnaires are susceptible to missing values and
component, regulates unconscious body effects such as the halo effect, which results in a defective prediction model
HR, ventilation, metabolism, mental stress, and hyperten- [7]. In addition, from a psychological point of view, self-
sion [3]. Non-invasive monitoring of HRV offers a numeri- reports are more related to current feelings.
cal metric to evaluate blood pressure [4]. Numerous HRV- Figure 2a presents the year-wise, and Fig. 2b shows the
derived parameters are used to diagnose mental stress and algorithm-wise distribution of the research works in this
are indeed a critical indicator to evaluate body and mind article.
conditions. In order to conduct this review, stress prediction studies
The resting HR of a person critically ranges from 60 that incorporate AI-based techniques, which predict HRV,
to 90 beats per minute. When a person gets stressed, their were searched in sources such as the IEEE Xplore digital
HR rises dramatically. Increased HR causes a considerable library, Science Direct, PubMed, and Google Scholar. For
increase in blood pressure, which is linked to low HRV. this purpose, 242 papers were initially found. After remov-
Thus, low HRV is a well-known indicator of stress. There- ing duplicates and reviewing the abstracts, 102 publications
fore, it clearly shows that stress is closely related to the were chosen for full-text review. After reviewing the entire
neurological system and the balance of the human body text of these publications, 56 were eliminated since they
[5]. A growing amount of data shows a rising incidence of were not stress prediction-focused studies that incorporated
stress-related health problems connected to today’s hectic both HRV and AI. Finally, we have thoroughly reviewed
lifestyle. Therefore, predicting stress has become a priority 43 articles in this research. Figure 3 depicts the process of
in order to maintain a productive and healthy lifestyle [6]. selecting articles for this study.
There is a growing demand for fast and efficient stress A population pyramid depicting the distribution of male
detection systems that can effectively help people under- and female participants in available datasets is presented in
stand and manage their stress levels. There have been Fig. 4. A word cloud representing the keywords extracted
many models developed for the prediction of stress from from article titles is presented in Fig. 5.
physiological parameters (such as electroencephalogram
(EEG), electrocardiogram (ECG), galvanic skin response
(GSR), blood pressure (BP), HRV), behavioural features
Related Works
(such as facial expression, speech, posture), and self-
reported questionnaires. In addition, current pieces of
research have emphasised the significance of monitoring Many researchers make use of machine learning (ML) and/
physiological signals in order to provide user’s brief and or rule-based (RB) methods to infer the mental state of an
effective feedback during regular tasks [7]. individual based on HRV. The HRV can be estimated using a
Collecting relevant data from cell phones is quite con- variety of physiological measures, including heart rate, gal-
venient and straightforward in this age of technological vanic skin response, body temperature, and blood pressure.
In this section, we have presented several works that provide
1 3

| Cognitive Computation (2024) 16:455–481  |     |                      |     |     |     |     | 457 |
| ---------------------------------------- | --- | -------------------- | --- | --- | --- | --- | --- |
| Fig. 1  A possible representation        |     | Placement of Sensors |     |     |     |     |     |
of AI framework for predicting
| stress from multi-modal sensor  |     |     | Brain |     |     |     |     |
| ------------------------------- | --- | --- | ----- | --- | --- | --- | --- |
data. Data collected from dif-
ferent parts of the human body
(such as the brain, chest, and
hands). The prediction model
| receives these data as input  |     |     | Heart |     |     |     |     |
| ----------------------------- | --- | --- | ----- | --- | --- | --- | --- |
signals. AI (rule-based, shallow
| machine learning, deep machine  |     | Muscle | Blood   |     |     |     |     |
| ------------------------------- | --- | ------ | ------- | --- | --- | --- | --- |
| learning)-based algorithms      |     | /Skin  | Vessels |     |     |     |     |
were taken into account in this
research to detect stress levels
Pre-processing
Wavelet Detection
|     |     | Normalization |               | Sampling SCR Detection |     |     |     |
| --- | --- | ------------- | ------------- | ---------------------- | --- | --- | --- |
|     |     |               | QRS Detection | Filtering              |     |     |     |
Noise Removal
Dimentionality Detection
Classification Algorithms
Shallow ML
Rule base
|     |     | Fuzzification | Fuzzy engine | Defuzzification | Deep ML |     |     |
| --- | --- | ------------- | ------------ | --------------- | ------- | --- | --- |
Rule Based
Stress Level
|     | Year-wise Analysis |     |     |     | Algorithm-wise Analysis |     |     |
| --- | ------------------ | --- | --- | --- | ----------------------- | --- | --- |
30
| 14  |     |     |     | 30  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12  |     |     | 25  |     |     |     |     |
25
| 10  |     |     | 20  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
20
| 8   |     |     | 15  | 15  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
6
|     |     |     | 10  | 10  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4   |     |     | 5   |     |     |     |     |
5
2
0
|                  |           |           | SVM  | 0       |              |              |         |
| ---------------- | --------- | --------- | ---- | ------- | ------------ | ------------ | ------- |
| 0                |           |           |      | SVM KNN | RF RNN DT LR | NB LVQ Fuzzy | CNN DNN |
| 2007 - 2015 2016 | 2017 2018 | 2019 2020 | 2021 |         |              |              |         |
Logic
Year
Algorithms
|     | (a) |     |     |     | (b) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Fig. 2  a The year-wise distribution of studies. We presented the num- of the articles. The bar diagram shows the most popular algorithms
ber of research papers on stress prediction using AI approaches that  found in the reviewed studies
occurred between 2016 and 2021. b The algorithm-wise distribution
1 3

4 58 Cognitive Computation (2024) 16:455–481
30
25
20
15
|              | No of papers           |                 |                    | 10  |
| ------------ | ---------------------- | --------------- | ------------------ | --- |
| Duplication  | selected for           | Abstract & text | Selected papers    |     |
| Removed: 198 | further screening: 156 | screening: 102  | in this study : 43 | 5   |
eluR
LM LD
0
Total collected article
242
Fig. 3  Reviewing research articles, we identified 242 research publications in Science Direct, PubMed, Google Scholar, and the IEEE Xplore
digital library at first. Ultimately, 43 research articles were chosen for this review after the screening process
a review of HRV-based stress prediction models with ML  of data properly. These RB systems attracted researchers
algorithms and rule-based approaches. due to their explainability and better performance for the
Panicker and Gayathri [11] proposed extensive reviews  small dataset.
on different ML algorithms such as support vector machine  Piotrowski and Szypulska [12] provided a comprehen-
(SVM), K-nearest neighbour (KNN), multilayer perceptron
sive overview of KNN, NB, and neural network (NN)-based
(MLP), long short-term memory (LSTM), decision tree  drowsiness detection methods relying on HRV data extracted
(DT), linear discriminant analysis (LDA), Naïve Bayes (NB),  from ECG, EEG, and electrooculography (EOG) readings.
logistic regression (LR), and probabilistic neural network  They reviewed several ML techniques as well as pre-press-
(PNN) to predict various emotions (fear, anger, sadness) and  ing approaches for this purpose. However, RB techniques
stress using physiological data. These data were collected  were not included in their research.
using EEG, ECG, GSR, and skin conductivity sensors. They  Can et al. [13] investigated various stress detection
investigated the connections between the biological charac- approaches using data from smartphones and wearable sen-
teristics of persons with emotional and mental stress. The  sors like ECG, EMG, electrodermal activity (EDA), EEG,
authors have ignored different state-of-the-art RB methods  GSR, and PPG. They classified the outputs into stress lev-
in their survey. They did not incorporate the pre-processing  els and classes. In their review, the authors focused more
Fig. 4  Population distribution  Population Distribution of Datasets
of datasets from the selected
|     |     | 12  | 8   |     |
| --- | --- | --- | --- | --- |
articles showing the number of
11
male and female participants
|     |     | 14   | 13     |     |
| --- | --- | ---- | ------ | --- |
|     |     | 20   | 41     |     |
|     |     | 21   | 6      |     |
|     |     | 23   | 19     |     |
|     |     | 17   | 8      |     |
|     |     | 18   | 3      |     |
|     |     | 5    | 5      |     |
|     |     | 6    | 9      |     |
|     |     | 52   | 5      |     |
|     |     | 17   | 7      |     |
|     |     | 18   | 8      |     |
|     |     | 33   | 17     |     |
|     |     | 23   | 11     |     |
|     |     | 8    | 27     |     |
|     |     | 11   | 3      |     |
|     |     | 17   | 8      |     |
|     |     | 26   | 12     |     |
|     |     | 63   | 19     |     |
|     |     | 5    | 0      |     |
|     |     | male | female |     |
1 3

Cognitive Computation (2024) 16:455–481 459
Fig. 5 The word cloud depict-
ing retrieved keywords from the
title of the articles
on multimodal data-gathering approaches for stress detec- several ML techniques based on their stress detection abili-
tion. The authors addressed several ML and RB approaches ties for different stress levels. The use of multimodal data
like SVM, LDA, LR, AdaBoost, KNN, fuzzy logic, NB, and or RB techniques ignored stress in the detection system. In
convolutional neural networks (CNN). Smartphone sensors addition, just a few related publications were examined for
and wearable-based data were used only. They avoided the purpose of comparing ML approaches.
research challenges and different preprocessing techniques Nath et al. [17] reviewed and discussed stress detection
for the data. techniques which used ML algorithms like SVM, KNN, DT,
Bulagang et al. [14] looked into emotion categorisa- LDA, NB, ANN, and RF. In their review study, the authors
tion based on ECG and EEG sensor data. They also used identified GSR, ANS, EDA, PPG, HR, HRV, EOG, EEG,
EDA, HR sensor, GSR, etc. and reviewed some ML and ECG, EMG, EGG, and respiration-based physiological indi-
RB algorithms KNN, SVM, fuzzy logic, and random for- cators for classifying stress based on subjective and objec-
est (RF) utilising data from numerous sensors. The authors tive assessments. They compared various ML algorithms’
considered the utilisation of multimodal physiological sig- accuracy, classes, and acquisition windows. However, they
nals. They concentrated their research on several emotion did not mention data pre-processing strategies or the chal-
categories rather than stress. The paper was also lacking in lenges encountered while doing research. RB procedures
pre-processing methods and data fusion. were not included in their assessment.
Pramanta et al. [15] studied stress identification methods Smets et al. [18] compared SVM, LDA, Bayesian net-
to identify stress levels depending only on the HR data. works, DT, RF, and LR algorithms for the measurement
The authors investigated various ways of extracting prop- of stress levels based on physiological responses. Their
erties from heartbeat data collected using HRV, GSR, BP research includes data from ECG, GSR, HRV, ST, respira-
(blood pressure), and EEG sensors, as well as the perfor- tion, and EMG sensors. Rest detection rate, stress detection
mance of SVM, RF, NB, DT, and KNN approaches based rate, and average detection rate were used to compare accu-
on such data. They concentrated on classification methods racy. The authors employed questionnaires and sensors for
and overlooked multimodal and fusion-based data process- data collection, but data was used from one source. They
ing. Furthermore, RB techniques were not included in their tested six alternative ML algorithms but did not incorporate
research. Both multimodal data and RB techniques can per- multimodal data or RB detection strategies in the detection
form better when it comes to identification and classifica- system. Tonacci et al. [19] evaluated physiological data
tion tasks. linked to ANS activity, along with ECG and GSR; ANS,
Katarya and Maan [16] proposed a review of stress detec- ECG, HRV, HR, and cardiac sympathetic index (CSI) meas-
tion using SVM, KNN, LR, RF by GSR, EDA, skin tem- ures were used. The performances of SVM, KNN, DT, LDA,
perature (ST), blood volume pressure (BVP), HR, and HRV quadratic discriminant, and LR-based algorithms were com-
data collected from smartwatches. They explored various pared for physiological stress-level detection. The authors
smartwatch-based data collection methods and compared talked about what the study could be used for in the future
1 3

4 60 Cognitive Computation (2024) 16:455–481
and what problems other researchers might face. However, judgement. To evaluate stress levels, many researchers
they ignored RB approaches for their study and only consid- have utilised various sorts of phrases. Some class labels are
ered relaxation in place of stress detection. determined only by the presence of stress; others are defined
In earlier review studies, several stress prediction by stress and relaxation levels, which can be expressed as
approaches based on HRV were explored, which were done extremely stressed, mildly stressed, stressed, extremely
utilising a variety of ML techniques. The bulk of them were relaxed, relaxed, and so on [11].
targeted at utilising ML to detect and classify stress. In most For identifying stress, HRV is a crucial feature and indi-
cases, the reviews were limited to ML methods. Only a tiny cator for evaluating body and mind states. Therewith, while
fraction of their research employed RB methods. Although interpreting the relationship between HRV and stress (see
pre-processing approaches prepare data for the core clas- Fig. 6 for the relationship between brain and HRV), it is
sification, they were mostly discarded in the bulk of the critical to grasp the entire autonomic context and analyse a
literature. For enhanced and more accurate data gathering, patient’s medical and psychiatric history due to the diversity
multimodal and fusion-based sensors are essential. Even so, of possible stressors and individual stress responses [2].
the majority of the studies employed very specific types of
sensors, and review papers ignored the use of multimodal
Artificial Intelligence Algorithms
sensors. A common framework for stress detection might
be beneficial to add in review articles for possible future
studies. However, none of the studies provided a unified Recently, artificial intelligence (AI) has played a significant
framework for detecting stress. role in the methodological developments for diverse problem
There is no agreed standard for stress evaluation at pre- domains, including computational biology [21, 22], cyber
sent. This study intended to cover works that provide a basis security [23–26], disease detection [27–33] and manage-
for using HRV as a psychological stress indicator and to pro- ment [34–39], elderly care [40, 41], epidemiological study
vide a comprehensive analysis of AI-based pre-processing [42], fighting pandemic [43–49], healthcare [50–54], health-
and stress prediction models derived from HRV. Table 1 care service delivery [55–57], natural language processing
indicates the characteristics of the already available review [58–62], and social inclusion [63–65].
articles in the field of stress prediction from HRV. In this article, we categorised the algorithms found from
the different review publications as RB approaches, shallow
machine learning approaches, and deep machine learning
Stress Prediction and Heart Rate Variability
approaches. This section discusses the basic principle of
these three approaches and their pros and cons, along with
The field of stress research has a wide variety of applica- all the algorithms we have found being used by different
tions, as it has the potential to boost learning and increase articles.
work productivity. The potential applications of stress
Rule‑Based Approaches
research include the ability to enhance personal, govern-
ment, and industrial operations and the resilience of military
operations and life support systems [20]. As there may be Rule-based approach, often known as expert systems, makes
discrepancies between numerical scales suggested by vari- judgements or solves issues by using logic and previously
ous researchers, stress detection systems rely on qualitative established rules. These rules are typically created by
Table 1 Characteristics of
Ref Datatype Sensor Data set Data pre-pro- Classification
current review articles
cessing
Multi- Fusion RB ML DL
modal
[11] ✓ ✓ ✓ ✓ ✗ ✓ ✓ ✓
[12] ✓ ✗ ✓ ✗ ✓ ✗ ✗ ✗
[13] ✓ ✓ ✓ ✓ ✗ ✓ ✓ ✓
[14] ✓ ✗ ✓ ✓ ✓ ✗ ✓ ✓
[15] ✓ ✗ ✗ ✗ ✗ ✗ ✓ ✗
[16] ✓ ✗ ✓ ✗ ✗ ✗ ✓ ✗
[17] ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗
[18] ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗
This article ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓
1 3

Cognitive Computation (2024) 16:455–481 461
Fig. 6 The relation cycle of stress with HRV and relation with autonomous nervous system (ANS) is presented
experts in the field and are unique to their particular sec- neurons to automatically discover and learn hierarchical
tors. The system analyses incoming data and produces an representations of the input data. Deep learning excels in
output or recommendation by abiding by these rules. The tasks such as image and speech recognition, natural language
decision-making process for RB approaches is transpar- processing, and other complex pattern recognition tasks. It
ent. In the majority of instances, the rationale and condi- can automatically extract features from raw data, eliminat-
tions for RB approaches are clearly stated and transparent. ing the need for manual feature engineering. However, deep
Additionally, it is useful for updating guidelines or rules learning models often require substantial computational
of decision-making because they are clear and provide the resources and often lack interpretability [66–70].
approach flexibility and adaptability. On the other hand, RB
approaches have limited compatibility in complex domains Summary of AI Algorithms
and require manual effort to design the rule bases.
For stress prediction, AI algorithms have been extensively
Shallow Machine Learning Approaches
used in recent years. Table 2 described the basics of various
RB and ML techniques extensively used to predict stress
Shallow machine learning, sometimes called traditional
from HRV.
machine learning or supervised learning, encompasses
The AI algorithms which have been used throughout this
the process of training a model using labelled examples.
reviewed article are conferred in Table 2. In this section, the
Through this process, the model gains an understanding of
algorithms, along with their pros and cons with graphical
patterns and relationships within the data, enabling it to pre-
representation, have been presented. Figure 7 represents the
dict outcomes or classify new, unseen data. The emphasis
AI algorithms in pictorial form.
lies in extracting relevant features from the input data and
utilising them to guide decision-making. In shallow machine
learning, the model is required to be provided with labelled
AI for Stress Prediction
examples of inputs and their corresponding outputs. From
these examples, the model is learned to make predictions
The widespread adoption of AI can be attributed to several
on new, unseen data. However, shallow machine learning
factors, two of the most important of which are its remark-
models often offer interpretability and take less training time
able accuracy and lightning-fast response times. Addition-
than deep machine learning models. Shallow machine learn-
ally, it does an excellent job of predicting stress, which is
ing models are also easier to implement and debug.
essential to living a healthy life.
Deep Machine Learning Approaches
Rule‑Based Approach
Deep machine learning, often referred to as deep learning, is
a subset of machine learning that uses neural networks with Various types of RB systems, such as fuzzy logic, neuro-
multiple layers to learn representations of data. It involves fuzzy systems or fuzzy neural networks [83], and fuzzy
training a complex network of interconnected artificial adaptive resonance theory (ART) [84], are used in clinical
1 3

| 4 62 |     |     |     | Cognitive Computation (2024) 16:455–481 |     |     |
| ---- | --- | --- | --- | --------------------------------------- | --- | --- |
 cigol elur NEHT-FI ,level-hgih ’smetsys lortnoc yzzuf sdnelB  detadpu si ti dna ,euqinhcet siht ni ledom eht sa sevres elbat  .]67[ ecnamrofrep tset rof enilesab eht gnissessa nehw setar  elpmas tcnitsid lareves etareneg ot dohtem gniggab eht sesil  sesaib dna sthgiew lacitnedi gningissa yB .]97[ noitcnuf tup
|     |  ,setats owt naht erom gniredisnoc gnikniht namuh etacilper -xefl fo ticfied eht sevloser mhtirogla sihT .]17[ seitilibapac |     |  eht hcihw ni ,noitatneserper eert a gnisu devlos si melborp  fo edon eroc eht dna lebal ssalc a ot sdnopserroc edon fael |  atad ro atad hserf ni stcejbo ot atad gniniart ralimis tsesolc  gnisirogetac rof yradnuob noisiced lamitpo eht senimreteD |  tniop ertnec s’retsulc eht fo eulav laitini ehT .K retsulc otni |     |
| --- | --------------------------------------------------------------------------------------------------------------------------- | --- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | --- |
 nac cigol yzzuf saerehw ,setats owt ylno sesingocer cigol  noitceles eht dna gnikam-noisiced rebmun yzzuf ni ytilibi -irepxe trepxe tneserper ot elba era hcihw sepahs yzzuf fo  eht dna ycneuqerf gnitaluclac fo scisab eht swollof ylpmiS  eht ni stcejbo K fo puorg a rof gnirolpxe yb enod si NNK  neewteb enalprepyh gnitarapes yllaedi na yfitnedi ot skeeS -itU .]77[ tluser elgnis a etareneg ot seert noisiced lareves -tuo dna noitisnart a gninfied yb detcurtsnoc yllanoitnevnoC
 naelooB .smelborp dlrow-laer ni ytniatrecnu setaroprocnI  gnitupmoc dna gninrael level-wol ’skrowten laruen htiw  ytilibaborp A .]37[ tesatad a morf seulav fo noitanibmoc  ti gnippam dna rebmun eulav lautca yna gnisu fo elbapaC  noitacfiissalc mumixam dna egareva eht etaluclac ot desU  .elpicnirp noitasiminim ksir larutcurts eht gnisu sessalc  dellebalnu sefiissalc taht hcaorppa gniretsulc evitareti nA  atad tes morf gnittilps yb sretsulc tnereffid otni stesatad  fo sgnidnfi eht setagergga refiissalc elbmesne desab-TD A
 ehT .elbairav tegrat eht stciderp taht ledom a stcurtsnoC
snoitavitca tnedneped setaerc ,sreyal eht fo lla ot
]47[ tes atad gniniart eht morf stcejbo
|     | seerged pihsrebmem sa denfied |     | ]57[ serutaef sesserpxe eert eht |     | noitacfiitnedi retsulc secneuflni |     |
| --- | ----------------------------- | --- | -------------------------------- | --- | --------------------------------- | --- |
]47[ atad gniniart gnisu
]27[ yltcerroc secne
eulav 1-0 eht otni
| noitpircseD |     |     |     | ]57[ gnitset |     |     |
| ----------- | --- | --- | --- | ------------ | --- | --- |
]87[ stes
.selbairav lacirogetac fo esac ni eussi ycneuqerf orez saH •
|     | -terpretni yletelpmoc ton si NN yzzuf a fo erutcurts ehT • |  ni elbissopmi si hcihw ,srotciderp tnednepedni semussA • |     |     |     |     |
| --- | ---------------------------------------------------------- | --------------------------------------------------------- | --- | --- | --- | --- |
-ogla desab-eert rehto naht etarucca ssel ylevitarapmoC •
.stupni esicerpmi no lamitpo ton si ycarucca ehT •
sraey tnecer ni noitciderp sserts rof desu smhtirogla IA tnereffid fo snoitpircsed dna ,snoc ,sorp fo yrammus A  2 elbaT
.selbairav erutaef etaruccani ot elbatcepsuS •
.segnahc larutcurts ot dael segnahc llamS •
.smelborp raenilnon evloser tonnaC •
|     |     |     |     | .atad gib ni llew mrofrep ton seoD • | .gnivlos-melborp emit-laer rof toN • |     |
| --- | --- | --- | --- | ------------------------------------ | ------------------------------------ | --- |
.sretsulc fo seulav tcaxe seriuqeR •
|     |     | .eulaV 1-0 ni tluser spam ylnO • |     |     | .elbatsnu eb nac gnipuorg ataD • |     |
| --- | --- | -------------------------------- | --- | --- | -------------------------------- | --- |
.tsoc lanoitatupmoc egral saH •
.metsys tnerrucnoc a toN •
.elbatsnu ylevitarapmoC • .pu kcats ot elbissop toN • .rewols si emit gniniarT •
|     |     |     |     | .hgih si emit gniniarT • | .gnitupmoc ni rewolS • |     |
| --- | --- | --- | --- | ------------------------ | ---------------------- | --- |
.atad efil-laer
.smhtir
.elba
snoC
.metsys eht otni egdelwonk trepxe fo noitargetni swollA • -borp desab-noisserger dna noitacfiissalc htob evlos naC • .noitacfiissalc oediv dna noitingocer hceeps mrofrep naC •
 etercsid dna suounitnoc eht morf atad wen yfissalc naC •
.cigoL yzzuf dna NN htob fo shtgnerts eht senibmoC • .stesatad deulav-suounitnoc dna etercsid htob stpeccA • .smelborp noitacfiissalc dna noisserger htob no kroW •
.sessalc neewteb ytilibarapes raenil eriuqer ton seoD •
.seussi noitacfiissalc dna noisserger htob evlos naC •
.ecaps erutaef lanoisnemid hgih ot tupni srefsnarT •
.deniart eb atad hcum taht eriuqer ton seoD •
.atad eugav ro esicerpmi ,detrotsid eldnah •
.noitacfiissalc raenilnon tcudnoc naC •
.sksat noitacfiissalc gnivlos ni retteB •
.niart dna tnemelpmi ot elpmiS • .semoctuo elbissop lla redisnoC •
.atad wen ot tpada ylisae naC •
|     |     |     |     |     | .gnittfirevo fo ksir rewoL • | .pool kcabdeef a ni skroW • |
| --- | --- | --- | --- | --- | ---------------------------- | --------------------------- |
.elbixefl era sledom LF •
.tesatad
.smel
sorP
|      |     |       | NNK | MVS | CMK |     |
| ---- | --- | ----- | --- | --- | --- | --- |
| epyT | NNF |       |     |     |     | NNR |
| LF   |     | BN RL | TD  |     | FR  |     |
1 3

Cognitive Computation (2024) 16:455–481 463
applications where the knowledge of different experts are
converted into a set of “if-then” rules. Many researchers
have utilised fuzzy logic to assess stress from HRV.
Kumar et al. [85] developed a fuzzy theoretic nonpara-
metric deep model for predicting stress based on heartbeat
analysis. In addition to the stress value, the authors cre-
ated weights for subjective stress evaluation and empirical
HRV analysis to illustrate the explainability of the pro-
posed model.
El-Samahy et al. [83] proposed Mamdani fuzzy infer-
ence systems to find mental stress using heart rate and
diameter of the pupil. The authors carried out a closed-
loop experiment between two personal computers, one for
imposing mental stress and the other for monitoring and
managing the human mental state.
Ranganathan et al. [86] proposed a stress assessment
approach that analyses heart rate signals using a wavelet
transform and a neural fuzzy model. Techniques such as
wavelet decomposition and reconstruction were employed
to minimise noise and recover specific time-frequency fea-
tures that were previously lost. It is necessary to apply
neural fuzzy training in order to recognise spectral fea-
tures, and fuzzy clustering techniques are used to evaluate
mental stress. They kept track of the heart rate recordings
and used the wavelet transform to evaluate the data (WT).
Neuro-fuzzy evaluation approaches were used to improve
the reliability of HRV analysis and to track the activity of
the autonomic nervous system (ANS) under a variety of
stress conditions.
Kumar et al. [87] developed a novel heart rate variabil-
ity analysis technique for measuring mental stress based
on fuzzy clustering. An accurate and dependable fuzzy
identification technique was used to deal with the uncer-
tainties created by individual differences in the assessment
of mental stress levels. Their method requires the con-
tinuous monitoring of heart rate signals over the Internet.
Later, the signals are processed by means of a continuous
wavelet transform in order to recover the local features of
HRV in the time-frequency domain.
Wang et al. [84] presented a pattern recognition sys-
tem for learning complicated HRV-salivary stress cor-
relations. In order to predict salivary response given a
set of ECG measurements, the researchers used a fuzzy
ARTMAP (FAM) classifier. They improved FAM utilis-
ing GA ensembles, which improved the training cycle
order and ARTMAP parameters. They also devised a sys-
tem for simultaneously collecting heart rate and salivary
data under various stress induction strategies. A sum-
mary of used algorithms, pre-processing, sensors, and
features by RB stress prediction approaches is presented
in Table 3.
1 3
)deunitnoc(
2
elbaT
noitpircseD
snoC
sorP
epyT
dna
tupni
eht
neewteb
ni
sreyal
neddih
elpitlum
sah
NND
.ssecorp
gninrael
wolS
•
.gnissecorp
level-itlum
od
naC
•
NND
atad
morf
serutaef
tcartxe
ot
ytiliba
eht
sah
tI
.sreyal
tuptuo
.atad
fo
tnuoma
egral
a
seriuqeR
•
.noitatneserper
erutaef
detacilpmoc
htiw
krow
naC
•
cimim
sNND
.smhtirogla
noitcartxe
erutaef
yna
tuohtiw
lacitroC
yb
noisiv
fo
msinahcem
gnissecorp
levelitlum
eht
]08[
niarb
eht
fo
saera
tI
.sreyal
elpitlum
fo
gnitsisnoc
krowten
noitagaporpkcaB
.sNND
naht
gniniart
ni
rewolS
•
.gnissecorp-erp
no
ecnailer
elttiL
•
NNC
,dlefi
evitpecer
eht
:saedi
larutcetihcra
eerht
senibmoc
-niart
lufsseccus
rof
regral
hcum
eb
ot
sdeen
tes
gniniarT
•
.stluser
etarucca
erom
edivorP
•
fo
erutcetihcra
ehT
.]18[
gnilpmasbus
dna
,sthgiew
derahs
.gni
]28[
sgnieb
namuh
fo
xetroc
lausiv
eht
no
desab
si
NNC
FR
,gniretsulc
snaem-K
CMK
,enihcam
rotcev
troppus
MVS
,sruobhgien
tseraen-K
NNK
,eert
noisiced
TD
,noisserger
citsigol
RL
,seyaB
evian
BN
,krowten
laruen
yzzuf
NNF
,cigol
yzzuf
LF
krowten
laruen
lanoitulovnoc
NNC
,krowten
laruen
peed
NND
,krowten
laruen
tnerrucer
NNR
,tserof
modnar

| 4 64 |     | Cognitive Computation (2024) 16:455–481 |     |     |
| ---- | --- | --------------------------------------- | --- | --- |
|      | (A) | (B)                                     |     |     |
Fuzzy Rule Base
|     | Input data                    | Output data |     |     |
| --- | ----------------------------- | ----------- | --- | --- |
|     | Fuzzification Defuzzification |             |     |     |
Fuzzy Output Engine
|     | (C) | (D) | (E) |     |
| --- | --- | --- | --- | --- |
|     | (F) | (G) | (H) |     |
Gap
Class 1 Class 2
|     | (I) | (J) | (K) |     |
| --- | --- | --- | --- | --- |
Hidden Layer 1
|     |              | Pixels of image |     | Circle |
| --- | ------------ | --------------- | --- | ------ |
|     | Hidden Layer | fed as input    |     |        |
Output Layer
|     | reyaL tupnI |     |     | Cube |
| --- | ----------- | --- | --- | ---- |
Output Layer
Square
Input Layer
|     |     | Hidden Layer 2 | Input Layer | O u t p u t  |
| --- | --- | -------------- | ----------- | ------------ |
Hidden Layers L a y e r
Fig. 7  AI/ML techniques used in recent research. A Fuzzy logic, B fuzzy neural network, C naive Bayes, D logistic regression, E decision tree,
F random forest, G support vector machine, H K-means cluster, I RNN, J DNN, and K CNN
Shallow Machine Learning Approaches contains a list of studies which utilises shallow ML meth-
ods to predict stress.
In shallow ML, the training process is carried out using data  Sriramprakash et al. [88] extracted the most important
with predefined features where it is necessary to perform  and overlapping characteristics from physiological sensors in
feature extraction by hand, as the use of domain knowledge  order to identify stress in working individuals. The authors
is essential. Shallow ML includes well-known algorithms  extracted time- and frequency-domain features as well as
such as RF, NB, DT, SVM, KNN, and LR. This section  physiological features (HR, HRV, GSR, and so on) from the
Table 3  A summary of used algorithms, pre-processing, sensors, and features by rule-based stress prediction approaches
| Ref. Model                          | Pre-processing | Sensors | Features     |     |
| ----------------------------------- | -------------- | ------- | ------------ | --- |
| [85] Fuzzy theoretic nonparametric  | -              | PPG     | R-R Features |     |
deep model
| [83] Mamdani fuzzy | Downsampling | Ohmeda 2300 Finap- | HRV2, mPD |     |
| ------------------ | ------------ | ------------------ | --------- | --- |
ress, Gazepoint GP3
eye tracker
[86] Sugeno neuro fuzzy Wavelet transformation, noise removal ECG Time-frequency features
[87] Sugeno fuzzy clustering Continuous wavelet transformation Polar S810i HR, Mw, 1/a, p1,p2,p3
[84] Fuzzy ARTMAP Dimensionality reduction, normalisation ECG, microtiter plate  Alpha amylase, cortisol,
spectrophotometer R-R intervals
1 3

Cognitive Computation (2024) 16:455–481 465
physiological data. They employed SVM and KNN classi- the individualised baseline of each phase in developing the
fiers to detect stress and assess the validity of the retrieved stress model, the retrieved HRV features were converted cor-
features for stress detection. respondingly using the pairwise transformation.
Huang et al. [89] recruited 35 participants who wore Castaldo et al. [95] used linear and non-linear HRV char-
wearable devices to collect ECG from the participants. acteristics extracted during an oral test (stress) and during
In this experiment, the authors collected 8 HRV features, rest after a holiday to detect mental stress. They showed
namely RMSSD, PNN50, TP, HF, LF, VLF, and the LF/HF that nonlinear ultrashort-term (3 min) HRV features might
ratio and transmitted these collected data to a smartphone automatically predict mental stress in healthy participants.
via Bluetooth interface. SVM, KNN, NB, and LR were used ECG sensor data was used to extract HRV features, which
to train the model that automatically detected the fatigue were then evaluated using Kubios software tools. Following
state. that, the HRV properties were applied to statistical and data
Wu et al. [90] attempted to overcome the challenge of mining analysis.
identifying physiological stress caused by engaging in physi- Delmastro et al. [96] examine the impact of a specific
cal activities. They used wristband sensors to capture biosig- training procedure on the cognitive function and stress
nals. GSR, BVP, HR, ACC, and ST sensors were employed response of a group of MCI-fragile older persons. They
to acquire physiological data in this investigation. The tested a stress detection system based on different ML algo-
authors utilised KNN, SVM, DT, NB, ensemble learning rithms to see how well they performed on a real-world data-
(EL), and DL models to categorise physical activities and set. They also proposed a mobile system architecture for
acute physical stress. online stress monitoring that can infer the amount of tension
Sevil et al. [75] reported models to detect stress and during a session.
awareness levels in knowledge workers using biometric Lima et al. [97] developed a model that can predict
sensors. The authors used wristbands to collect biosignals how people will react using HRV characteristics and EDA
like GSR, BVP, ST, and HR from knowledge workers. For signals, which were extracted using a wearable device to
the purpose of detecting stress levels and awareness, they provide continuous monitoring. Participants were placed
used ML models, such as KNN, SVM, NB, DT, and DNN. through a mental arithmetic stress test to extract the HRV
The performance of these algorithms was compared with the and EDA characteristics.
state-of-the-art techniques. Yu et al. [98] propose a new way to track office work-
Pourmohammadi and Maleki [91] compare the efficacy ers’ behaviour and HRV. They used ML techniques to create
of the EMG signal and the ECG signal in detecting mental a classification model that could distinguish distinct work
stress. This work examines the EMG signal of the right and behaviours (moving the body, typing, talking, and reading)
left trapezius and the right and left erector spinal muscles from sensor data. The system utilised a lightweight EMFi
in depth for multi-level stress recognition. To create stress sensor for measuring the changes in pressure induced by
in the laboratory, mental arithmetic, the Stroop colour word human motions and heartbeat in office chairs.
test, time constraints, and a stressful atmosphere were used. Padmaja et al. [99] proposed a model based on four
The effectiveness of EMG signals for stress detection was major well-being dimensions. The stress level of a person
tested using an ECG signal. is determined by combining their HRV, sleeping pattern,
Maldonado et al. [92] introduced an expert system that social behaviour, and physical activity. They developed
used an SVM-based features selection method to analyse DetectStress, a cognitive stress-level detection system that
the mental workload of individuals while performing daily uses smartphone daily activity data and data from a wireless
tasks. The authors used multiple mobile devices to capture physical activity tracker to evaluate an individual’s stress
HR, blood oxygen saturation (SpO2), and temperature to levels in an unobtrusive manner (FITBIT).
construct a system for mental stress analysis. Can et al. [100] developed an autonomous stress detection
Pluntke et al. [93] introduced a framework that uses HRV system that relies on physiological information collected
analysis to detect and classify physical and mental stress from discreet smart wearable gadgets that people can take
in real time without interfering with the person’s activities. about with them. This system has modality-specific artefact
HRV data was labelled and gathered in controlled situations removal and feature extraction techniques for real-world
where subjects were subjected to physical, psychological, settings.
and combination stressors. They used SVM and C5 DT to Chen et al. [101] investigated consumer-grade wrist-based
segregate and identify distinct stress kinds and the relation- PPG sensors, which are as cheap, convenient, and accurate
ship between HRV data and stress levels. as consumer ECG sensors. They created an individual stress
Giannakakis et al. [94] examines the effects of stress on prediction model to assess the performance of different PPG
HRV parameters and seeks to discover the best mix of HRV LED lights and the suitable window widths. To extract ten
features for reliably detecting stress. In order to account for HRV characteristics, the authors utilised half-overlapping
1 3

4 66 Cognitive Computation (2024) 16:455–481
moving windows (1/3/5 min). They find that a 3-min interval Ahmad et al. [109] reported a study on stress-level assess-
is adequate to distinguish between a stressful mental state ment in virtual reality environments. They collected ECG
and illustrate how to utilise ML methods to combine HRV signals from subjects under VR influence. They transformed
features for reliable stress identification. the collected data into 1-D and 2-D forms to create a mul-
Koldijk et al. [102] discover that addressing individual timodal fusion of ECG data. Using this multimodal deep
variations is especially important when assessing mental fusion model and RF, KNN, SVM, and XGBoost classi-
states. The authors explored several ML techniques for infer- fier (XGB) algorithms, they evaluated the performances for
ring working circumstances and mental states from a mul- stress-level detection from 1-s windows.
timodal set of sensor data, including computer logs, facial Dalmeida and Masala [110] developed a comparative
expressions, posture, and physiology. They discovered that study that tests the compatibility of HRV features as physi-
sensor data can better predict the subjective variable “mental ological data to accurately classify the level of stress. This
effort” than it can predict “felt stress”. was achieved by extracting HRV parameters from ECG sen-
Ciabattoni et al. [103] proposed a smart-watch-based sys- sor data and selecting the more relevant features using Pear-
tem for collecting and analysing biosignal data in order to son’s correlation, recursive feature elimination (RFE), and
detect mental stress in the course of daily activities. Using extra tree classifier. They used different ML methodologies
data from a commercial wristwatch, they classified stress such as KNN, SVM, MLP, RF, and gradient boosting (GB)
using GSR, RR interval, and body temperature (BT). Data to test and develop the best model for the purpose.
from smartwatches is filtered and adjusted to smooth down Sandulescu et al. [111] presented an SVM-based stress
noise and motion distortions. detection approach from data collected through wearable
Attaran et al. [104] presented a design for a multi-modal sensors on people. They collected the PPG value, PPG auto-
stress monitoring system. They extracted 17 different fea- correlation value, HRV value, and EDA value for each state
tures from ECG, accelerometer, SpO2, EDA, and respira- to be determined. The model they proposed was demon-
tory sensor to explore them for maximising the detection strated to detect real-time stress levels in people.
accuracy of SVM and KNN classifiers. Finally, they used Munla et al. [112] investigated stress-level detection
the results to implement a low-power-consuming ASIC of drivers in a real-world driving situation. The authors
implementation of the SVM classifier in stress monitoring. extracted HRV features using domain analysis approaches
Castaldo et al. [105] suggested a method using mental stress such as time, frequency, time-frequency, or non-linear meth-
assessment to identify the extent of ultra-short HRV as a ods using wavelet and STFT. They built a feature vector out
valid replacement for short HRV features. They extracted of the extracted parameters and tested KNN, RBF, and SVM
23 ultra-short HRV features and used SVM and DT classi- ML approaches. A summary of used algorithms, pre-pro-
fiers to identify their validity in the case of automatic stress cessing, sensors, and features by shallow ML-based stress
assessment. prediction approaches is presented in Tables 4, 5, 6, and 7.
Hantono et al. [106] targeted to analyse the stress level
Deep Machine Learning Approaches
of people while using smartphones. They used PPG heart
rate sensing on mobile devices to record the heart rate of the
subjects while they were doing different tasks. Finally, they de Vries et al. [113] used learning vector quantisation (LVQ)
compared NN, discriminant analysis, NB, and KNN algo- to classify stress and relaxation from different physiological
rithms while doing time- and frequency-domain analysis- signals. To create the stress classifier, the authors collected
based classifications. features from ECG, GSR, and RSP data and observed car-
Tiwari et al. [107] explored an SVM-based prediction diac activity. To train the LVQ classifier, the authors experi-
model of mental stress and workload. The authors extracted mented with different very high-frequency band features in
HRV and breathing signals for computing ultra-short-term addition to common properties of these signals.
segments of the signals to use them as features. The system Son [114] created a model to forecast mood changes con-
was developed to provide a fast prediction of stress and men- nected to LSTM, RNN, and LSTM-RNN in order to provide
tal workload depending on frequency- and time-domain fea- a framework that will estimate the mood based on a particu-
tures from less than 5 min segments of the sensor readings. lar detail of people’s qualitative ability to adapt. Variations
Clark et al. [108] presented an RF classifier-based model in moods, such as his cognitive activity in response to his
for the prediction of people’s stress levels at least one minute activities, surroundings, environment, HR, HRV, and other
prior to the event. They extracted 42 features from GSR, states, might be easily justified with this feature-rich wear-
respiration, and ECG sensors and expanded to 252 features. able device in a consecutive time domain.
These features were used to identify whether the stress level Rastgoo et al. [115] assessed a driver’s critical situa-
of the subject would rise to a higher level in the coming tion, and the authors utilised CNN and LSTM. To construct
scenarios. this predictor, parameters were taken from ECG, vehicle
1 3

Cognitive Computation (2024) 16:455–481 467
Table 4 A summary of used algorithms, pre-processing, sensors, and features by Shallow ML-based stress prediction approaches
Ref. Model Pre-processing Sensors Features
[88] SVM, KNN - Kinect 3D sensor, ECG sensor RMSSD, AVNN, SDANN, SDNN,
NN50, PNN50, LF, HF, LF/HF
[89] SVM, KNN, NB, LR - ECG NN.Mean, PNN50, rMSSD, TP,
LF, HF, VLF, LF/HF
[90] k-NN, SVM, DT, NB SG-filter, BWF, ANC algorithm GSR, BVP, ST, 3-D ACC, HR Time-domain, frequency-domain,
and distribution features of BVP,
ACC, GSR, and HR
[75] KNN, SVM, NB, DT and DNN - Biometric Sensors Statistical Features of RR
[91] SVM FIR filters, IIR filters, EMD and ECG v.12 devices, SX230 sur- Statistical and time-domain fea-
DWT face electrode, Skintact F-55 tures of RR
electrode
[92] SVM Canny’s edge detection algo- Pulse oximeter, ST, ECG, and HRV, HR, PS, temperature, SpO2
rithm, LPFr eye tracker
[93] SVM, C4.5 DT 3-sigma rule ECG, Polar H7 chest strap Statistical features of RR;
frequency-domain features of RR
[94] RF, SVM time series polynomial fit and ECG Time-domain features of RR, HRV
bandpass filtered triangular index, ECG envelope,
frequency-domain features of RR
[95] NB, SVM, MLP, AB, C4.5 DT QRS detector, PhysioNet’s ECG Statistical features of RR, absolute
WAVE power, frequency-domain fea-
tures of RR, SampEn, D2, fa1,
dfa2, ShanEn
[96] BN, SVM, k-NN, C4.5 DT Lomb-Scargle algorithm, LPF, Zephyr BioHarness34, Shim- Statistical features of RR, tot spec-
CDA mer3 GSR + Development trum power, frequency-domain
Kit5 features of RR, Amps, ISCR,
mean SCL, mean EDA, max
EDA deflection
In pre-processing column: PPG-PD PPG peak detection, HR heart rate, RR-ISF RR-interval series filtering, HRV and EDA electrodermal activ-
ity features extraction, BCG ballistocardiography, SG-Filter Savitzky-Golay filter, BWF Butterworth filter, ANC adaptive noise cancellation,
EMD empirical mode decomposition, FIR finite impulse response, IIR infinite impulse response, LPF low pass filter, CDA continuous deconvo-
lution analysis
In sensor column: SCR skin conductance response, SCL skin conductance level, RiseT rise time, ST skin temperature, ECG ecocardiogram, GSR
galvanic skin response, ACC accelerometer
characteristics, and relevant information and then input into spectrum properties were determined in a comprehensible
separate CNNs as the driver’s stress-level components were fashion of frequency domain to construct the frequency-
classified into low, medium, and high categories and then based ML technique.
merged into a two-layer LSTM. He et al. [118] used CNN technique on various physio-
Akbulut et al. [116] provided a model to allow the simu- logical signals to assess chronic perceptual anxiety and tran-
lation of stress as well as a variety of mood shifts based quillity. To construct this model, the researchers analysed
on physiological factors. The researchers used ECG, GSR, characteristics from ECG, EEG, and EMG readings, along
body temperature, blood pressure, glucose level, and SpO2 with observed heart activity. The scientists used several
information to construct this framework, along with observ- really quiet frequency band components as well as common
ing changes in behaviour and quantifying HRV according aspects of these transmissions to develop the CNN-based
to stress levels. In addition to determining similar traits of analyser.
these signals, the authors examined other often quite fre- Qin et al. [119] assessed the BP feed-forward approach
quency band features as well as time-domain and variational for the relaxed state, low stress, medium stress, high stress,
analytic factors. and other metabolic variables. The authors had to obtain
Coutts et al. [117] used an LSTM system to capture HRV information from GSR or skin temperature and BVP to
signals from a wrist device that can monitor inter-beat inter- design an assessment technique to determine HRV charac-
vals using mean, standard deviation, and root mean square teristics. HRV features obtained from time- and frequency-
successive difference. Physiological signals and character- domain evaluation of R-R intervals recorded during the
istics were acquired to use this sensor reading device. The enhanced practice session are the most efficient and precise
1 3

4 68 Cognitive Computation (2024) 16:455–481
Table 5 A summary of used algorithms, pre-processing, sensors, and features by shallow ML-based stress prediction approaches
Ref. Model Pre-processing Sensors Features
[97] SVM; LR; RF PPG-PD; HR; RR-ISF; HRV; EDA DA wrist, PPG, Spare, TVOC, CO2, Statistical features of RR, SCR, SCL;
TEMP RiseT
[98] SVM; KNN; EnL BCG processing EMFi sensor Statistical features
[99] NB; DT Normalization and transformation Fitbit Tracker Number of calls, duration, no. of SMS,
the app usage information
[100] PCA, SVM, Artefact-(interpolation/removal) 3D accelerometer (ACC), PPG, EDA Statistical and frequency-domain
KNN, LR, RF, features of RR
MLP
[101] RF Filtering using BWBPF Wristband device, Polar H10 SD1, SD2, RMSSD, SDNN, MHR,
MRRI, TP, VLP, LF, HF
[102] NB, SVM, KNN, - ECG and skin conductance Facial expressions, head orientation
Bayes Net, RF; action units, emotion, body postures,
DT; MLP joint angles, HR, HRV, skin conduct-
ance
[103] KNN Artefacts and noise removal HR, GSR and BT RR, GSR, BT
In pre-processing column: PPG-PD PPG peak detection, HR heart rate, RR-ISF RR-interval series filtering, HRV and EDA electrodermal activ-
ity features extraction, BCG ballistocardiography, BWBPF high-order Butterworth bandpass filter
In sensor column: SCR skin conductance response, SCL skin conductance level, RiseT rise time, GSR galvanic skin response, PPG photoplethys-
mogram, EDA electrodermal activity, EMFi electro-mechanical film
indicators of ANS at the time of constructing the artificial performing a hand grip strength task. The author extracted
neural network algorithm. time- and frequency-domain features of HR and HRV to
Ding et al. [120] proposed a study that uses multimodal perform the identification of stress and no-stress states. They
measurements to measure mental workload and validates proposed an optimised ANN model to identify the states
the features for mental workload estimation. The authors and proposed the effects of this model for a better stress
created a backpropagation neural network (BPNN) classifier management system.
to evaluate the workload using physiological data (HR, HRV, Dhaouadi and Ben Khelifa [122] utilised LSTM and deep
EMG, ETA, and respiration), subjective ratings of mental neural networks (DNN) to assess legitimate anxiety levels as
exertion (NASA Task Load Index), and task performance well as detect other lifestyle patterns in young gamers based
metrics. They compared the BPNN’s performance against on physiological measurements. To establish such models,
KNN, SVM, medium tree, and LDA algorithms. researchers gathered the required characteristics from ECG,
Kalatzis et al. [121] conducted a study that determines EEG, EDA, and EMG recordings and estimated emotional
stress levels of older adults from ECG signals while state variations. As a result, to construct the frameworks
Table 6 A summary of used algorithms, pre-processing, sensors, and features by shallow ML-based stress prediction approaches
Ref. Model Pre-processing Sensors Features
[104] KNN, SVM HR, accelerometer, Statistical features of HR and RR, mean SpO2
EDA, Resp. Rate,
SpO2
[105] SVM, DT RR-SE and Corr ECG Statistical features of NN, dfa1, dfa2, RPlmean, RPlmax, REC, RPadet,
ShanEn
[106] NN, KNN, DA, NB Corr PPG mHR, RR, SDHR, SDRR, CVRR, RMSSD, pRR20, and pRR50. ULF,
VLF, LF, HF
[107] SVM BPF (5–25 Hz) BioHarness 3, Zephyr Time-domain and frequency-domain features of HRV
[108] RF classifier Normalising, BWF GSR, ECG, Resp Time-domain and frequency-domain features of GSR respiration: the
mean and variance time-domain and frequency-domain features of
HRV
In pre-processing column: HR heart rate, RR-SE RR-interval series extraction, Corr correlation, BPF bandpass filter, BWF Butterworth filter
In sensor column: SCR skin conductance response, HR heart rate, ECG ecocardiogram, PPG photoplethysmogram, EDA electrodermal activity,
Resp respiration
1 3

Cognitive Computation (2024) 16:455–481 469
Table 7 A summary of used algorithms, pre-processing, sensors, and features by shallow ML-based stress prediction approaches
Ref. Model Pre-processing Sensors Features
[109] RF, KNN, SVM, and XGB LS-method ECG, EMG, PPG Time-domain and frequency-domain
features of HRV
[110] KNN, SVM, MLP, RF, and GB WQRS tool PhysioNet HRV Apple watch HR, AVNN, SDNN, RMSSD, pNN50, TP,
toolkit, pyhrv, data normali- and VLF
zation
[111] SVM Downsampling, noise removal BioNomadix module from ppgt, ppgaut, HRV t, EDA t
Biopac, model BN-
PPGED
[112] SVM, KNN Filtering, derivative, SW inte- ECG sensor Time-domain and frequency-domain
gration, QRS detection features of RR
In pre-processing column: SW squaring and window integration, LS-method Lomb-Scargle method
In sensor column: EMG electromyography, HR heart rate, ECG ecocardiogram
(LSTM and DNN), the scholars had to conduct several inves- Performance Analysis and Discussion
tigations and frequency variations to determine the frequent
and unusual properties. Rule‑Based Approaches
Stewart et al. [123] suggests neural processes as a tech-
nique for developing personalised models and addressing Kumar et al. [85] addressed the issue of explainability of
individual interactions with physiological processes. They fuzzy theoretic nonparametric deep model applications in
used standard ML models (such as SVM, KNN) and neural biology and medicine. They used one previously studied
processes to develop stress classifiers which were compared dataset of 50 subjects and a new dataset of 100 subjects
on two datasets using leave-one-participant cross-validation. and obtained (Pearson’s correlation coefficient (r): 0.8162
Silva et al. [124] compared baseline and stress situations (old dataset) vs 0.6809 (new dataset), RMSE: 6.8382 (old
to look at HR and HRV indicators. The authors used sev- dataset) vs 9.4872 (new dataset)).
eral statistical tests and ML models, both shallow (which El-Samahy et al. [83] found a close match between
includes SVM, KNN, and RF) and deep, to build a predictive the measurement of the proposed system and the actual
model for stress monitoring, evaluation, and chronic stress measurements acquired from human volunteers. The sys-
prediction. tem was built and evaluated using heart rate and pupil
A summary of used algorithms, pre-processing, sensors, diameter data collected from 5 people. To compare the
and features by deep ML-based stress prediction approaches achievements of subjects 1 and 2, an evaluation index (EI)
is presented in Tables 8 and 9.
Table 8 A summary of used algorithms, pre-processing, sensors, and features by deep ML-based stress prediction approaches
Ref. Model Pre-processing Sensors Features
[113] LVQ R-PD, IBI outlier removal, and SCRG ECG, GSR, RSP Time-domain, frequency-domain, and
method distribution features of ECG, GSR, RSP
[114] LSTM-RNN All features are normalised into a range A Tizen component on smart-watch HR avg, HRV arg, HR min, HR max,
of [-1,1] SDHR, SDHRV, hr diff avg, hr diff var
[115] CNN-LSTM A Butterworth band-pass filter (5–15 ECG Mean, standard deviation, mean of the
Hz), R-peaks are extracted, Pan-Tomp- first difference of HRV, average normal-
kins algorithm to-normal (NN) and intervals, SDNN,
RMSSD, PNN50
[116] FFNN DWT, Pan-Tompkins algorithm, down CVDiMo wearable sensor Statistical and frequency-domain features
sampling of RR
[117] LSTM Noise filtering The bio beam band Statistical and frequency-domain features
of RR
[118] CNN Bandpass filter ECG HR, LH, SDNN, SD2, pQ
In pre-processing column: SCRG SCRGauge method, HR heart rate, RR-SE RR-interval series extraction; Corr correlation, BPF bandpass filter,
BWF Butterworth filter; DWT discrete wavelet transformation, IBI inter-beat interval
In sensor column: GSR galvanic skin response, HR heart rate, ECG ecocardiogram, RSP respiration
1 3

4 70 Cognitive Computation (2024) 16:455–481
Table 9 A summary of used algorithms, pre-processing, sensors, and features by deep ML-based stress prediction approaches
Ref. Model Pre-processing Sensors Features
[119] NN - Pulse oximeter MEAN, SDNN, SDANN, RMSSD, TF,
VLF, LF, HF, LF/HF
[120] BPNN, SVM, KNN WD and HP, LP, ECG, EDA, EMG, respiration sensors AVHR, LF/HF, Yrm, MF, SC mean,
and RMS filtering respiration
[121] ANN WT ECG probe, BIOPAC ECG100C Time-domain and frequency-domain
features of NN
[122] LSTM, DNN Transfer function, Polar H10, Actigraph wGT3X-BT HR and HRV features
biosppy and pyhrv
libraries
[123] NP, SVC, KNN HT algorithm, BWF ECG, GSR Time-domain and frequency-domain
features of HR, time-domain features of
GSR
[124] LR, NB, NN, SVM, RF, KNN - PPG Mean RR, Min RR, Max RR, Median RR,
SDNN, RMSSD, pNN50
In pre-processing column: HR heart rate, WD wavelet denoising, BPF bandpass filter, BWF Butterworth filter, WT wavelet transformation, HT
Hamilton-Tompkin, HP high pass, LP low pass;
In sensor column: GSR galvanic skin response, HR heart rate, ECG ecocardiogram, EMG electrmyogram, EDA electrodermal activity, PPG pho-
toplethysmogram
was produced for each of them. During levels 1–3, subject Shallow Machine Learning Approaches
1 had a high EI of over 90%. On the other hand, subject 2
showed an EI between 60 and 90% throughout the whole Sriramprakash et al. [88] used ECG, skin conductance, and
experiment, which means the levels of mental stress will Kinect 3D sensor to collect data from selected individuals.
be unchanged. The SWELL-KW dataset was used for classification (149
Ranganath et al. [86], using their proposed wavelet trans- features and 2688 instances in total) and got accuracies:
form and neuro-fuzzy inference system, evaluate stress using 66.52% (KNN) vs 72.83% (SVM-RBF kernel).
HRV. To investigate the activity of the ANS, the authors Huang et al. [89] demonstrated that the mental fatigue of
performed a time-frequency analysis (TFA) of HRV, which the samples could be accurately identified with a wearable
can be used to quantify mental stress. The authors studied ECG device. They collected 58 samples of ECG signals and
20 physically fit adults at two points in time: before and after compared SVM, NB, KNN, and LR algorithms to obtain
they began smoking and acquired a spectral decomposition accuracy (57.08% 9(SVM) vs 48.84% (NB) vs 65.37%
of HRV. These were used to build the proposed NF-based (KNN) vs 59.71% (LR)) and area under the curve (AUC)
model. (0.68 (SVM) vs 0.64 (NB) vs 0.74 (KNN) vs 0.65 (LR)).
Kumar et al. [87] proposed a fuzzy clustering method Wu et al. [90] combined HRV sensors and accelerometers
which helped to quantify mental stress and demonstrate to develop a model for monitoring the perceived stress levels
a direct functional link between ANS activities and men- in daily life. They collected data from 8 participants for their
tal stress. The researchers used NASA Task Load Index daily life in about 2 weeks and compared the performances
to examine subjective ratings of mental workload in 38 of NB, J48, RF, and bagging algorithms where accuracy
physically fit volunteers in air traffic management task 0.730 (NB) vs 0.819 (J48) vs 0.832 (RF) vs 0.8392 (bagging)
simulations. were obtained.
Wang et al. [84] provided a way for utilising HRV to cor- Sevil et al. [75] addressed the problem of detecting psy-
relate the human body’s salivary response to stress. They chological stress (APS) using data collected from wrist-
used 176 ECG recordings and 264 salivary samples from bands. They collected data from 34 samples doing 166
22 people. They have generated six datasets (3-amylase, clinical experiments and compared different classification
3-cortisol) using alpha-amylase and cortisol measurements algorithms: KNN, SVM, DT, NB, EL, LD, and DL, where
to label ECG feature vectors. The final classifier system cor- SVM had the highest accuracy of 99.1%.
rectly classified salivary cortisol based on ECG characteris- Pourmohammadi and Maleki [91] collected EMG and
tics with an accuracy of 80%, compared to 75% for salivary ECG signals concurrently from 34 healthy students (23
alpha-amylase. A summary of used algorithms, datasets, females and 11 males, ages 20 to 37). They used LIBSVM
evaluation metrics, and obtained outcomes of RB stress (a library for SVM) with RBF (radial basis function) ker-
prediction research is presented in Table 10. nel for training the model. Sequentially, stress identification
1 3

Cognitive Computation (2024) 16:455–481 471
Table 10 A summary of used algorithms, datasets, evaluation metrics, and obtained outcomes of rule-based stress prediction research
Ref. Models Dataset Evaluation metrics Performance
[85] Fuzzy theoretic nonpara- Private/100 subjects RMSE PCC: 0.8162 (old dataset) vs 0.6809 (new dataset), RMSE: 6.8382
metric deep model (old dataset) vs 9.4872 (new dataset)
[83] Mamdani fuzzy model Private/3 subjects EI EI = 2.9412 (Subject 1), 1 (Subject 2)
for training and
2 subjects for
testing
[86] Sugeno neuro-fuzzy model Private/20 subjects - Established a direct functional relationship between heart rate vari-
ability and mental stress
[87] Sugeno fuzzy clustering Private/26 males, - Minimised the worst-case influence of uncertainty on fuzzy param-
12 females, aged eter identification performance
18–29 years
[84] Fuzzy ARTMAP Private/22 subjects Acc Acc = 80% (ECG characteristics),75% (salivary alpha-amylase)
In evaluation metrics column: PCC Pearson’s correlation coefficient, EI evaluation index
In performance column: PCC Pearson’s correlation coefficient, EI evaluation index
accuracy was 100%, 97.6%, and 96.2 % for the two, three, AB learning schemes outperform the other classifier learn-
and four levels. Maldonado et al. [92] collected data from ing methods (accuracy: 87% for RF and 88.2% for AB).
50 engineering students in Chile, with a total of 33 men and Lima et al. [97] gathered information using some sen-
17 women aged 22.4 ± 2.8 years. They took HR, SpO2, and sors (such as PPG, Spare, TVOC) from a group of willing
temperature readings to utilise in their SVM model, which participants (15 participants, ranging in age from 21 to 55
yielded an AUC of 0.994 with a variable collecting cost of years old (9 females and 6 males)). While under stress, the
16. model had an accuracy of about 80% in terms of HRV fea-
Pluntke et al. [93] acquired HRV data from subjects in a tures in baseline and about 77 % in terms of HRV and EDA
laboratory setting, and SVM and DT were used to train the simultaneous baseline characteristics.
model. A set of labelled RR-interval signals was collected as Yu et al. [98] used the ensemble learning technique to
a training set. They used an H7 chest strap sensor to collect create a classifier that incorporates three separate work
data from 26 male and female participants ranging in age activities: body movement, typing, and browsing. These
from 23 to 59. A precision, recalling, and F-score of almost can be identified with 94.2%, 93.2%, and 91.2% accuracy,
90% were shown in the best model based on a DT of C5. correspondingly. They gathered information from ten office
Giannakakis et al. [94] evaluated 24 participants and 11 workers, all of whom were around 31 years old.
tasks, performing a research protocol for about 45 min. They Padmaja et al. [99] collected data from a smartphone and
used KNN, generalised linear model (GLM), NB, linear dis- a Fitbit and then preprocessed and normalised it. They used
criminant analysis (LDA), SVM, and RF classifiers, where NB (accuracy: 72%) and DT (accuracy: 62%) for classifica-
RF excels with a classification accuracy of 75.1% above any tion. DetectStress has a 72% accuracy rate in recognising
other classification method. 84.4% classification accuracy in perceived stress utilising data from both smartphones and
a 10-fold method is the best result in the proposal of stress wireless fitness trackers.
recognition simply by using hRV characteristics. Can et al. [100] collected physiological signal and ques-
Castaldo et al. [95] used a 3-lead electrocardiogram tionnaire data from the 21 participants by using Samsung
(ECG) to collect data from 42 students on two distinct days, Gear S and S2 and Empatica E4 sensors. From HR and ACC
including during an oral examination (stress) and during rest signals acquired using Empatica E4, the MLP algorithm
following a holiday. They employed five distinct algorithms produced the best results (92.19%), while the RF algorithm
(NB, SVM, MLP, AB, and C4.5 (DT)). With sensitivity, produced the best classification accuracy (88.26%) with HR
specificity, and accuracy rates of 78%, 80%, and 79%, cor- and ACC data collected from all devices.
respondingly, the C4.5 tree algorithm was the best ML tech- Chen et al. [101] collected data from PPG and Polar
nique for distinguishing between stress and rest. H10 sensors, used RF as a classifier, and compared it
Delmastro et al. [96] collected data conducting a ran- with the SVM, Naïve Bayes, and MLP model. In the
domised cross-over observational study where Zephyr Bio- PPG dataset, their approach obtains an overall leave-
Harness34 device was used for ECG monitoring and Shim- one-participant-out F1-score of 80%, while the ground
mer3 GSR+Development Kit5 for EDA. Some algorithms truth ECG scores 79.7%. Koldijk et al. [102] used the
(BN, SVM, k-NN, C4.5 DT, AB) were used where RF and SWELL-KW dataset (149 features and 2688 instances in
1 3

4 72 Cognitive Computation (2024) 16:455–481
total) and compared SVM (accuracy: 90.0298%) with 7 Dalmeida et al. [110] investigated the role of HRV fea-
other algorithms, which includes NB (64.7693%), K-star tures stress predicted from ECG, EMG, GSR, and respira-
(65.8110%), Bayes net (69.0848%), J48 (78.1994%), IBk tion sensor data. They used a dataset collected by MIT and
(nearest neighbour with euclidean distance (84.5238%)), available in Physionet. They tested different ML models such
RF(87.0908%), and MLP (88.5417%). as KNN, SVM, MLP, RF, and GB. MLP was considered
Ciabattoni et al. [103] utilised KNN to classify stress an appropriate stress classification method with an 80%
using uniform precedence probability and Euclidean dis- sensitivity score. HRV features such as the AVNN, SDNN,
tance metrics with one neighbour. An accuracy of 84.5% and RMSSD were found to be relevant aspects for stress
has been determined altogether. In recognition of stress, identification.
a 26% misclassification error was detected when the indi- Sandulescu et al. [111] present an SVM-based approach
vidual was calm. for stress prediction by collecting PPG, HRV, and EDA sen-
Attaran et al. [104] utilised the ThreatFire belt for sor data from 5 participants. The results showed 82% accu-
data collection and employed several physiological and racy on two participants and more than 80% precision level
behavioural factors with both SVM and KNN classifiers for all the participants.
to increase the detection accuracy. The best classification Munla et al. [112] intended to study stress-level detec-
accuracy to identify stress was observed for the heart rate tion from HRV features extracted from 16 different subjects
(HR) and accelerometer characteristics. For hardware from the Stress Recognition in Automobile Driver database
implementation, the SVM classification was utilised, and (DRIVEDB). They used three ML models and achieved
this system has an overall classification accuracy of 96%. accuracies: KNN (66.66%) vs SVM (83.33%) and SVM with
Castaldo et al. [105] collected 23 ultra-short HRV fea- RBF kernel (83.3%).
tures from 42 healthy subjects. They found six out of 23 A summary of used algorithms, datasets, evaluation met-
ultra-short HRV features (MeanNN, StdNN, MeanHR, rics, and obtained outcomes of shallow ML-based stress pre-
StdHR, HF, and SD2) displaying consistency in the detec- diction research is presented in Tables 11, 12, and 13.
tion of stress. The authors employed 5 ML algorithms and
Deep Machine Learning Approaches
found their accuracies: MLP (98%) vs SVM (88%) vs C4.5
DT(94%) vs IBK (94%) vs LDA (94%).
Hantono et al. [106] recorded heart rate data using PPG de Vries et al. [113] collected GSR, RSP, and ECG sensor
sensors in smartphones from 41 subjects. They analysed data from 61 participants from the age of 18 to 28 years
the data and extracted HRV features to detect mental to perform stress and relaxation classification. They used
stress. The authors employed NN, KNN, DA, and NB algo- learning vector quantisation to achieve an accuracy of 88%
rithms to find the accuracies: NN (73%) vs KNN (82%) vs for the classification.
DA (66%) vs NB (60%). Rastgoo et al. [115] collected ECG, vehicle, and envi-
Tiwari et al. [107] collected ECG and breathing data ronmental data from 27 participants in a vehicle simulator.
from 27 police trainees over the course of 15 weeks. They They proposed a CNN and LSTM-based multimodal fusion
extracted ultra-short-term HRV and breathing features model, which showed an accuracy of 92.8%, sensitivity of
from the data and predicted stress. Results suggested that 94.13%, specificity of 97.37%, and precision of 95.00%.
ultra-short-term analysis for stress prediction results in Akbulut et al. [116] developed a stress model that incor-
performance losses lower than 7% when compared to porates an algorithm for detecting affective states based on
short-term analysis. They used an SVM classifier with HRV analysis, emotion recognition, and other statistical
RBF kernel, resulting in 80% performance accuracy. data. They collected the dataset conducted with 30 volun-
Clark et al. [108] proposed a model for driver stress teers and named it CVDiMo. In categorising the stress levels
prediction. They collected data from 17 subjects using of all patients, their suggested method had a 90.5% accuracy
ECG, GSR, and respiration sensors after they completed rate. The average success rate of MES patients was found
a 20-mile drive. The authors extracted 42 features from the to be 92%, which is greater than the general performance of
data to use in an RF classifier which achieved an average healthy people.
accuracy of 94%. Ahmad et al. [109] collected the dataset Coutts et al. [117] recorded HRV features from 652 par-
named Ryerson Multimedia Research Laboratory (RML), ticipants using a wearable sensor. They employed an LSTM
which was recorded by physiological signals using 9 par- network for the detection of stress, anxiety, and depression
ticipants and measured ECG, GSR, and respiration signals. levels, finding 85% classification accuracy.
They used raw data, which is procured from the ECG sig- He et al. [118] used ECG sensor data from 20 partici-
nal. For the proposed fusion model, they got 66.6% and pants to extract six HRV features (HR, LH, pQ, SD2, SDNN,
72.7% in the RML and WESAD datasets, respectively. Comb). They used SVM, LDA, and CNN-based models
to detect cognitive stress from these models, where CNN
1 3

Cognitive Computation (2024) 16:455–481  473
Table 11  A summary of used algorithms, datasets, evaluation metrics, and obtained outcomes of Shallow ML-based stress prediction research
| Ref. Models      | Dataset  | Evaluation metrics | Performance   |
| ---------------- | -------- | ------------------ | ------------- |
| [88] SVM and KNN | SWELL-KW | Acc                | Acc of 0.9275 |
[89] SVM, KNN, NB, and LR Private/35 participant (mean age  AUC  Acc = 0.755 AUC = 0.74
of 23 ± 4 years and a male-to-
female ratio of 1:1.3)
[90] NB, J48, RF and bagging Private/8 participants Acc prediction Acc = 0.857
[75] KNN, SVM, DT, NB Private/34 participants Acc Acc = 0.991
[91] SVM Private/34 students (23 females and  Acc The accuracies two level = 1.0,
|     | 11 males, aged 20–37 years) |     | three level = 0.976, and four  |
| --- | --------------------------- | --- | ------------------------------ |
levels were 0.962
[92] SVM Private/50 participants (33 men &  AUC, variable collection cost AUC = 0.994, Vcost = 16
17 women)
| [93] SVM, C5 DT | Private                         | Pre, Rec f1, Acc | 88% Acc, all |
| --------------- | ------------------------------- | ---------------- | ------------ |
| [94] RF, SVM    | Private/24 participants ageing  | Acc              | Acc = 0.844  |
47.3±9.3 years
[95] NB, SVM, MLP, AB, Dt C4.5 Private/42 participants Sen, Spe and Acc Sen=0.78, Spe=0.80 and Acc
rate=0.79
[96] BN, SVM, k-NN, C4.5 DT, AB Private/9 older adults Acc; Pre; Rec; AUPRC RF (Acc =87.0%; Pre =92.4%;
Rec=88.2%; AUPRC =0.97) and
AB (Acc=88.2%; Pre =92.3%;
Rec=92.0%; AUPRC =0.92)
In evaluation metrics column: Acc accuracy, AUC  area under the ROC curve, Vcost variable collection cost, Pre precision, Rec recall, Sen sensi-
tivity, Spe specificity
In performance column: Acc accuracy, AUC  area under the ROC curve, Vcost variable collection cost, Pre precision, Rec recall, Sen sensitivity,
Spe specificity
Table 12  A summary of used algorithms, datasets, evaluation metrics, and obtained outcomes of Shallow ML-based stress prediction research
| Ref. Models      | Dataset | Evaluation metrics | Performance                    |
| ---------------- | ------- | ------------------ | ------------------------------ |
| [97] SVM, LR, RF | Private | Acc                | 80% accuracy for HRV features  |
in baseline and about 77% for
HRV and EDA simultaneous
features
[98] SVM, KNN, and EnL 15 office workers (five female,  Acc Accuracies of up to 91%
five males, age: 31 ± 5.3)
[99] NB, DT 35 young adults Sen, Spe, Acc, Pearson’s cor- NB classifier has 72% accuracy
relation
[100] PCA, SVM, KNN, LR, RF,  21 participants (18 males and 3  Acc, f-Measure, Pre, Rec Obtained 92.15% accuracy maxi-
MLP females with an average age  mum three-level classification
of 20)
[101] RF 6 healthy participants ages  Acc 10-fold accuracy of stress state is
|     | 21–40 years old |     | 98%, and F1-score reaches 80% |
| --- | --------------- | --- | ----------------------------- |
[102] NB, SVM, KNN, BN, RF, DT,  25 participants (8 female, aver- Acc Best results were obtained
| MLP | age age 25, stdv 3.25) |     | with an SVM (RBF kernel):  |
| --- | ---------------------- | --- | -------------------------- |
90.0298%
[103] KNN Private/10 young subjects (mean  Acc, Error Acc = 0.845, misclassification
|                | age 24; 5 female) |     | Error = 0.26                     |
| -------------- | ----------------- | --- | -------------------------------- |
| [104] KNN, SVM | Private           | Acc | The overall classification accu- |
racy of this system is 96%
In evaluation metrics column: Acc accuracy, AUC  area under the ROC curve, Vcost variable collection cost, Pre precision, Rec recall, Sen sensi-
tivity, Spe specificity
In performance column: Acc accuracy, AUC  area under the ROC curve, Vcost variable collection cost, Pre precision, Rec recall, Sen sensitivity,
Spe specificity
1 3

4 74 Cognitive Computation (2024) 16:455–481
Table 13 A summary of used algorithms, datasets, evaluation metrics, and obtained outcomes of Shallow ML-based stress prediction research
Ref. Models Dataset Evaluation metrics Performance
[105] SVM, DT ECG from 42 healthy subjects (19 AUC, Sen, Spe, Acc Achieved good performance accu-
female, 23 male) racy above 88%
[106] NN, KNN, DT, NB 41 students AUC, ROC, Acc, confusion -
matrix
[107] SVM Data was collected from 27 (6 BAC In HRV segments BAC =0.579 for
females) police 300 s window duration
[108] RFr Private Acc Acc = 94%
[109] RF, KNN, SVM, XGB RML, WESAD Acc., precision, recall, F1-Score Acc. = 66.6 (RML dataset), Acc. =
72.7 (WESAD dataset)
[110] KNN, SVM, MLP, RF, GB PhysioNet AUROC MLP, RF and GB yielded an
AUROC of 83%, 85%, and 85%,
respectively
[111] SVM Private/5 participants aged 18 Acc, Pre Best Acc and Pre for P3:83.08(Acc)
to 39 & 83.87(Pre)
[112] SVM-RBF, KNN DRIVEDB Acc Acc = 83%
In evaluation metrics column: Acc accuracy, AUROC area under the ROC curve, Vcost variable collection cost, Pre precision, Rec recall, Sen
sensitivity, Spe specificity, BAC balanced accuracy
(17.3%) outperformed LDA (25.1 ± 14.2%) and SVM (24.5 accuracy at 96.4% but 78.3% when taking physiological
± 13.2%) according to detection error rate. features only.
Qin et al. [119] used 10 HRV features extracted from Kalatzis et al. [121] recruited 57 participants to extract
56 samples of R-R intervals recorded during the modified time- and frequency-domain features of HR and HRV
Stroop test. They used 40 samples as training data and 16 as using ECG sensors. They used an ANN-based model to
testing for a stress evaluation system based on the BP neural classify stress and no-stress states, achieving a 90.83%
network, which could detect different levels of stress with an accuracy level.
accuracy rate of 93.75%. Dhaouadi and Ben Khelifa [122] used ECG, EDA, and
Ding et al. [120] recruited 18 healthy individuals to col- EMG measures taken by wearable devices from 15 young
lect heart rate, heart rate variability, electromyography, gamers in order to stress monitoring in real time. They
electrodermal activity, and respiration physiological data explored LSTM and DNN networks where the DNN model
to measure changes in physiological activity with varied obtained the best accuracy of 65% at 15 and 30 epochs,
levels of tasks. While combining physiological signals and but LSTm achieved the best accuracy of 95% at 30 epochs.
task performance, their classification models could achieve Stewart et al. [123] used two publicly available data-
accuracy at 96.4% but 78.3% when taking physiological fea- sets, which include drivedb and WESAD. Data was col-
tures only. lected from both datasets using multiple sensor recordings,
Kalatzis et al. [121] recruited 57 participants to extract including ECG and GSR. They used shallow ML models
time- and frequency-domain features of HR and HRV using (such as KNN, SVM, and LR). Neural processes mod-
ECG sensors. They used an ANN-based model to classify els outperformed those models (WESAD: 0.957 (average
stress and no-stress states, achieving a 90.83% accuracy precision), drivedb: 0.804 (average precision)) and had
level. the best performance when using periods of stress and
Qin et al. [119] used 10 HRV features extracted from baseline as context.
56 samples of R-R intervals recorded during the modified Silva et al. [124] monitored the stress of 83 medical stu-
Stroop test. They used 40 samples as training data and 16 as dents by comparing stress levels during academic exams
testing for a stress evaluation system based on the BP neural and a regular week. Data was collected from wearable sen-
network, which could detect different levels of stress with an sors such as Microsoft Smart band 2 and PPG. The neural
accuracy rate of 93.75%. network revealed better performance (model-1: sensitiv-
Ding et al. [120] recruited 18 healthy individuals to ity, 75.2%; specificity, 77.9%. Model-2: sensitivity, 74.2%;
collect heart rate, heart rate variability, electromyography, specificity, 78.1%.) where two models were established to
electrodermal activity, and respiration physiological data predict stress comparing shallow ML algorithms (such as
to measure changes in physiological activity with varied SVM, KNN, LR, RF). A summary of used algorithms, data-
levels of tasks. While combining physiological signals and sets, evaluation metrics, and obtained outcomes of deep ML-
task performance, their classification models could achieve based stress prediction research is presented in Table 14.
1 3

Cognitive Computation (2024) 16:455–481 475
Table 14 A summary of used algorithms, datasets, evaluation metrics, and obtained outcomes of deep ML-based stress prediction research
Ref. Models Dataset Evaluation metrics Performance
[113] LVQ Private/61 (20 male, 41 female) Acc RSP = 0.71, ECG = 0.834, Acc = 0.877
[115] LSTM-RNN Private/a group of Vietnamese students Framework proposed -
[114] CNN-LSTM Private/27 participants aged 21–40 years Acc Sen Spe: Pre Acc: 0.928, Sen: 0.9413, Spe: 0.9737 and
(55% male) Pre: 0.95
[116] FFNN CVDiMo/conducted with 30 volunteers AUC, Acc AUC = 0.978, Acc= 0.92
[117] LSTM Private/for trial-1: 91 participants (62% ACC Acc = 0.85
female, 38% male); for trial-2: 600 (72%
female, 28% male)
[118] CNN Private/20 healthy subjects, aged from 18 ER, FAR, and FRR CNN ER=17.3 FAR= 0.01 FRR = 32.1
to 35
[119] NN 56 samples Acc 93.75% accuracy
[120] BPNN, SVM, KNN 18 right-handed, healthy individuals, 20.1 ± Acc, Rec, Pre Accuracy can reach 96.4% and 78.3%
0.94 years
[121] ANN Private/57 participants, and all are above 65 acc Acc = 90.83%
years
[122] LSTM, DNN Private/15 gamers Age of 10 to 22 acc Acc = 64% (DNN) vs 92% (LSTM)
[123] LR, SVM, KNN Drivedb, WESAD Avg precision, AUC WESAD: 0.957 average precision, same-
participant vs 0.780 other-participant,
drivedb: 0.804 vs 0.757
[124] LR, NN, NB, SVM, Private/63 (76.8%) were female, and 19 Sen, Spe For Model 1, Sen = 0.752 and Spe = 0.779.
RF, and KNN (23.2%) were male aged 17 to 38 years For Model 2, Sen = 0.742 and Spe =
0.781
In evaluation metrics column: Acc accuracy, AUC area under the ROC curve, Vcost variable collection cost, Pre precision, Rec recall, Sen sensi-
tivity, Spe specificity, FAR false acceptance rate, FRR false rejection rate
Discussion to quantify psychological stress and attained 99.1% accuracy
using the SVM classifier, which is also the highest among all
Stress can lead to a variety of psychological issues. Many the publications reviewed in this review article. For deep ML
disorders are more likely to develop in a stressful environ- techniques, Ding et al. [120] used a BPNN classifier to assess
ment, particularly if the stress is intense and long-lasting stress based on physiological activity with varying levels of
[125]. Therefore, being able to predict stress in an effective tasks and achieved high accuracy. Their classification models
manner is a crucial fact. In this research, we observed HRV have a 96.4% accuracy rate.
characteristics as physiological indicators for stress detection Another performance metric for assessing classification
based on a review of 43 studies published between 2016 and errors is the AUC. This review article contained 5 studies that
2021. RMSSD, SDNN, pNN50, and AVNN are determined employed the AUC measure, a two-dimensional area beneath
to be the most often utilised HRV features in our tables. the ROC curve. The highest AUC value for deep ML tech-
ECG, PPG, and GSR are the most deployed sensors for data niques was attained by Akbulut et al. [116], as shown in Fig. 9.
collection. They created a stress model based on HRV analysis, emo-
In AI, accuracy is one of the most important performance tion recognition, and other statistical data from the CVDiMo
indicators. The present research has been examined in this dataset, which includes an algorithm for recognising affective
article in order to provide a full understanding of the field states. Using FFNN, they were able to attain an AUC of 0.97.
of stress prediction via HRV. Maldonado et al. [92] used shallow ML to get the best AUC
According to Fig. 8 displaying the performance compari- value of 0.99 for stress detection, which is significantly higher
son of the papers based on accuracy level, only one article by than other models that use AUC as a performance indicator.
Wang et al. [84] employed accuracy as a performance meas-
ure for RB techniques. Using the fuzzy ARTMAP classifier,
Challanges and Future Scope
they explored the stress association between HRV and sali-
vary, achieving an overall accuracy of 80% for ECG records.
In the case of shallow ML approaches, Sevil et al. [75] Due to a lack of quality data, data collection procedures,
achieved the highest accuracy among the 21 studies utilising detection methodology selection, and other factors, research
accuracy as a performance measure. They used wristband data for predicting and detecting mental stress confront numerous
1 3

| 4 76 |     |     |     |     |     |     | Cognitive Computation (2024) 16:455–481 |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- |
99
| 100 |     |       |     | 98  | 96    |       |     |      | 96.4    |
| --- | --- | ----- | --- | --- | ----- | ----- | --- | ---- | ------- |
|     |     |       |     |     | 94    |       |     | 93.7 |         |
|     | 92  |       | 91  | 92  | 90.03 |       | 92  | 92   | 90.8 92 |
|     |     | 88    | 88  |     | 88    |       | 87  |      |         |
|     |     | 85 84 |     |     | 84    |       |     | 85   |         |
| 80  |     |       | 80  |     |       | 83.08 | 83  |      |         |
79
| 80  |     | 75  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | 72  |     |     | 72  |     |     |     |
)%( ycaruccA
60
40
20
0
|     |     |     | Rule-based | Shallow ML | Deep ML |     |     |     |     |
| --- | --- | --- | ---------- | ---------- | ------- | --- | --- | --- | --- |
Fig. 8  Performance comparison of the articles based on accuracy level. The different algorithm types are presented using different colours
challenges. In this section, we will discuss the difficulties  mones, and blood pressure largely affect the measure of
that stress researchers face and how to overcome them,  HRV. So, the consideration of baseline mood and health
which might be very useful for future researchers.  issues of the individual under observation needs to be
considered during data collection.
1.  Effect of individual moods and health  2.  Controlled environment and biased dataset
    HRV is very much dependent on the change in ANS      Most of the datasets for stress prediction from HRV are
activity. In fact, HRV is controlled by ANS, a primi- collected inside a controlled environment inside the labo-
tive part of the nervous system. As a result, individuals’  ratory setup, and as a result, the effect of real-life scenarios
native mood and health issues like blood sugar, hor- is missing, which can be overcome by collecting data from
Fig. 9  Performance comparison
of the articles based on AUC
|     |     | Stewart et al. |     |     |     |     |     | 0.95 |     |
| --- | --- | -------------- | --- | --- | --- | --- | --- | ---- | --- |
level. The different algorithm
types are presented using differ-
ent colours
|     |     |                  | Akbulut et al |     |         |     |      |      | 0.97  |
| --- | --- | ---------------- | ------------- | --- | ------- | --- | ---- | ---- | ----- |
|     |     | Dalmeida et al.  |               |     |         |     |      | 0.85 |       |
|     |     | Maldonado et al. |               |     |         |     |      |      | 0.99  |
|     |     |                  | Huang et al.  |     |         |     | 0.74 |      |       |
|     |     |                  | 0             |     | 0.2 0.4 | 0.6 | 0.8  |      | 1 1.2 |
AUC
|     |     |     |     |     |     |     | Shallow ML | Deep ML |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | --- |
1 3

Cognitive Computation (2024) 16:455–481 477
the real-world office or driving situations. Moreover, the 9. Differences in evaluation metrics
dataset largely comprises male participants. As a result, Researchers have utilised a variety of metrics to demon-
the data are more biased towards male participants and strate the performance of their stress prediction or detec-
can show poor performance in female-centric data. tion system in various studies. As a result, new research-
3. Lack of large benchmark dataset ers and explorers in this sector are finding it increasingly
Much research included in this article has used its own difficult to compare these approaches to find one more
dataset, but most of which is not publicly available. But appropriate. Setting a very acceptable and benchmark
datasets that were publicly available were collected from evaluation metric could be a solution to this issue.
a small number of participants. As a result, the data is
not that generalised. So, there is not really a benchmark
dataset that can be used for all AI approaches to make a Conclusion
performance comparison among them.
4. Sensor quality and multimodal sensors Stress has become an inevitable element of our daily rou-
Data collection is the most important part of any tines. It has resulted in an alarming scenario for adolescent
research process. For HRV-based stress prediction, and juvenile mental health throughout the world. Controlling
ECG, EMG, GSR, etc., sensors are used in different stress has become a critical issue since it directly impacts
articles reviewed earlier, but the quality of sensors used physical and mental health. It has a negative influence on a
and fusion of the right sensors are very important in country’s socioeconomic condition. The growing AI disci-
this case. A multimodal dataset with data collected from pline can provide effective solutions for stress prediction.
high-quality and suitable sensors can produce a better In this study, we have conducted a comprehensive survey of
and more fitting dataset for future research. the sensors employed for acquiring HRV data and their fea-
5. Real-time stress monitoring tures, AI models applied on those data and their performance
In real life, stress has been described in various ways, assessed using avialable evaluation metrics, pre-processing
but it has been established that any stress leads to an methods applied on multi-modal data, and existing datasets.
unbalanced bodily and mental situation. This can lead The identified approaches have been summarised in tables
to productivity loss, diminished work abilities, and a and explored and their results were compared in depth.
slew of other health issues. However, a real-time stress Stated outcomes of the methodologies, used datasets, and
monitoring system is rarely investigated. As a result, a applied evaluation criteria were also presented.
real-time stress monitoring system could be a promising
future study topic.
6. Fusion of hybrid architectures Author Contribution This work was carried out in close collabora-
tion between all co-authors. They first defined the research theme and
Many ML and DL approaches have been used in the
contributed an early design of the system, further implemented and
reviewed research in this article, but there have not been refined the system development, and wrote the paper. All authors have
cases where hybrid architecture has been used to develop contributed to, seen, and approved the final manuscript.
the stress detection or prediction model. Even though
Data Availability The datasets generated during and/or analysed dur-
hybrid architectures can be a promising future prospect
ing the current study are available from the corresponding author upon
for accurate results. reasonable request.
7. Exploration of HRV features
Declarations
The majority of datasets utilised in recent studies have
employed the same HRV features to identify stress in
Ethical Approval All procedures performed in studies involving human
individuals, more or less. However, more noteworthy
participants were in accordance with the ethical standards of the insti-
statistical, frequency-domain, and time-domain features tutional and/or national research committee and with the 1964 Helsinki
could be investigated to provide effective stress predic- Declaration and its later amendments or comparable ethical standards.
tion datasets.
Informed Consent Informed consent was obtained from all individual
8. Less use of rule-based approaches
participants included in the study.
Throughout stress-related research, very rarely fuzzy
and researchers have used other RB approaches to
Conflict of Interest The authors declare no competing interests.
develop stress prediction systems. But due to human-like
inference ability and understandability, RB approaches Open Access This article is licensed under a Creative Commons Attri-
can be applied to develop a more suitable decision bution 4.0 International License, which permits use, sharing, adapta-
tion, distribution and reproduction in any medium or format, as long
support system. So, fuzzy-based stress management
as you give appropriate credit to the original author(s) and the source,
and decision support systems can be a possible future provide a link to the Creative Commons licence, and indicate if changes
research topic. were made. The images or other third party material in this article are
1 3

4 78 Cognitive Computation (2024) 16:455–481
included in the article's Creative Commons licence, unless indicated 17. Nath RK, Thapliyal H, Caban-Holt A, Mohanty SP. Machine
otherwise in a credit line to the material. If material is not included in learning based solutions for real-time stress monitoring. IEEE
the article's Creative Commons licence and your intended use is not Consum Electron Mag. 2020;9(5):34–41.
permitted by statutory regulation or exceeds the permitted use, you will 18. Smets E, Casale P, Großekathöfer U, Lamichhane B, De Raedt
need to obtain permission directly from the copyright holder. To view a W, Bogaerts K, et al. Comparison of machine learning techniques
copy of this licence, visit http://c reati vecom mons.o rg/l icens es/b y/4.0 /. for psychophysiological stress detection. In: International Sym-
posium on Pervasive Computing Paradigms for Mental Health.
Springer; 2015. p. 13–22.
19. Tonacci A, Dellabate A, Dieni A, Bachi L, Sansone F, Conte
References R, et al. Can machine learning predict stress reduction based on
wearable sensors’ data following relaxation at workplace? A pilot
study. Processes. 2020;8(4):448.
1. Acharya UR, Joseph KP, Kannathal N, Lim CM, Suri JS.
20. Sharma N, Gedeon T. Objective measures, sensors and computa-
Heart rate variability: a review. Med Biol Eng Compu.
tional techniques for stress recognition and classification: a sur-
2006;44(12):1031–51.
vey. Comput Methods Programs Biomed. 2012;108(3):1287–301.
2. Kim HG, Cheon EJ, Bai DS, Lee YH, Koo BH. Stress and heart
21. Rahman MA. Gaussian process in computational biology: covari-
rate variability: a meta-analysis and review of the literature. Psy-
ance functions for transcriptomics [phd]. University of Sheffield;
chiatry Investig. 2018;15(3):235.
2018. Available from: https://e these s.w hiter ose.a c.u k/1 9460/.
3. Sztajzel J, et al. Heart rate variability: a noninvasive electrocar-
22. Rakib AB, Rumky EA, Ashraf AJ, Hillas MM, Rahman MA.
diographic method to measure the autonomic nervous system.
Mental healthcare chatbot using sequence-to-sequence learning
Swiss Med Wkly. 2004;134(35–36):514–22.
and BiLSTM. In: Mahmud M, Kaiser MS, Vassanelli S, Dai Q,
4. Shaffer F, Ginsberg JP. An overview of heart rate variability met-
Zhong N, editors. Brain Informatics. Cham: Springer Interna-
rics and norms. Front Public Health. 2017:258.
tional Publishing; 2021. p. 378–87.
5. Mohan PM, Nagarajan V, Das SR. Stress measurement from
23. Islam N, et al. Towards machine learning based intrusion detec-
wearable photoplethysmographic sensor using heart rate vari-
tion in IoT networks. Comput Mater Contin. 2021;69(2):1801–21.
ability data. In: 2016 International Conference on Communica-
24. Farhin F, Kaiser MS, Mahmud M. Secured smart healthcare sys-
tion and Signal Processing (ICCSP). IEEE; 2016. p. 1141–4.
tem: blockchain and Bayesian inference based approach. In: Proc.
6. Oskooei A, Chau SM, Weiss J, Sridhar A, Martínez MR, Michel
TCCE. 2021. p. 455–65.
B. Destress: deep learning for unsupervised identification of
25. Ahmed S, et al. Artificial intelligence and machine learning for
mental stress in firefighters from heart-rate variability (HRV)
ensuring security in smart cities. In: Data-driven mining, learning
data. In: Explainable AI in Healthcare and Medicine. Springer;
and analytics for secured smart cities. Springer; 2021. p. 23–47.
2021. p. 93–105.
26. Zaman S, et al. Security threats and artificial intelligence based
7. Maxhuni A, Hernandez-Leal P, Sucar LE, Osmani V, Morales
countermeasures for Internet of Things networks: a comprehen-
EF, Mayora O. Stress modelling and prediction in presence of
sive survey. IEEE Access. 2021;9:94668–90.
scarce data. J Biomed Inform. 2016;63:344–56.
27. Noor MBT, Zenia NZ, Kaiser MS, Mamun SA, Mahmud M.
8. Bauer G, Lukowicz P. Can smartphones detect stress-related
Application of deep learning in detecting neurological disorders
changes in the behaviour of individuals? In: 2012 IEEE Interna-
from magnetic resonance images: a survey on the detection of
tional Conference on Pervasive Computing and Communications
Alzheimer’s disease, Parkinson’s disease and schizophrenia.
Workshops. IEEE; 2012. p. 423–6.
Brain Inform. 2020;7(1):1–21.
9. Carneiro D, Castillo JC, Novais P, Fernández-Caballero A, Neves
28. Ghosh T, Al Banna MH, Rahman MS, Kaiser MS, Mahmud M,
J. Multimodal behavioral analysis for non-invasive stress detec-
Hosen AS, et al. Artificial intelligence and Internet of Things in
tion. Expert Syst Appl. 2012;39(18):13376–89.
screening and management of autism spectrum disorder. Sustain
10. Gaurav AR, Kumar V. EEG-metric based mental stress detection.
Cities Soc. 2021;74.
Netw Biol. 2018;8(1):25–34.
29. Biswas M, Kaiser MS, Mahmud M, Al Mamun S, Hossain M,
11. Panicker SS, Gayathri P. A survey of machine learning tech-
Rahman MA, et al. An XAI based autism detection: The con-
niques in physiology based mental stress detection systems. Bio-
text behind the detection. In: Proc. Brain Informatics. 2021. p.
cybern Biomed Eng. 2019;39(2):444–69.
448–59.
12. Piotrowski Z, Szypulska M. Classification of falling
30. Wadhera T, Mahmud M. Computing hierarchical complexity of
asleep states using HRV analysis. Biocybern Biomed Eng.
the brain from electroencephalogram signals: a graph convolu-
2017;37(2):290–301.
tional network-based approach. In: Proc. IJCNN. 2022. p. 1–6.
13. Can YS, Arnrich B, Ersoy C. Stress detection in daily life scenar-
31. Wadhera T, Mahmud M. Influences of social learning in indi-
ios using smart phones and wearable sensors: a survey. J Biomed
vidual perception and decision making in people with autism: a
Inform. 2019;92.
computational approach. In: Proc. Brain Inform. 2022. p. 50–61.
14. Bulagang AF, Weng NG, Mountstephens J, Teo J. A review of
32. Wadhera T, Mahmud M. Brain networks in autism spectrum
recent approaches for emotion classification using electrocardi-
disorder, epilepsy and their relationship: a machine learning
ography and electrodermography signals. Inform Med Unlocked.
approach. In: Artificial Intelligence in Healthcare: Recent Appli-
2020;20:100363.
cations and Developments. Springer; 2022. p. 125–42.
15. Pramanta SA, Prihatmanto AS, Park MG. A study on the stress
33. Wadhera T, Mahmud M. Brain functional network topology in
identification using observed heart beat data. In: 2016 6th Inter-
autism spectrum disorder: a novel weighted hierarchical com-
national Conference on System Engineering and Technology
plexity metric for electroencephalogram. IEEE J Biomed Health
(ICSET). IEEE; 2016. p. 149–52.
Inform. 2023:1–8.
16. Katarya R, Maan S. Stress detection using smartwatches with
34. Sumi AI, et al. fASSERT: a fuzzy assistive system for children
machine learning: a survey. In: 2020 International Conference on
with autism using Internet of Things. In: Proc. Brain Inform.
Electronics and Sustainable Communication Systems (ICESC).
2018. p. 403–12.
IEEE; 2020. p. 306–10.
1 3

Cognitive Computation (2024) 16:455–481 479
35. Akhund NU, et al. ADEPTNESS: Alzheimer’s disease patient in Intelligent Systems and Computing. Singapore: Springer;
management system using pervasive sensors-early prototype and 2021. p. 291–301.
preliminary results. In: Proc. Brain Inform. 2018. p. 413–22. 54. Rahman MA, Brown DJ, Mahmud M, Shopland N, Haym N,
36. Al Banna M, Ghosh T, Taher KA, Kaiser MS, Mahmud M, et al. Sumich A, et al. Biofeedback towards machine learning driven
A monitoring system for patients of autism spectrum disorder self-guided virtual reality exposure therapy based on arousal
using artificial intelligence. In: Proc. Brain Informatics; 2020. state detection from multimodal data. In: Proc. BI2022; 2022.
p. 251–62. p. 1–12.
37. Jesmin S, Kaiser MS, Mahmud M. Artificial and Internet of 55. Farhin F, Kaiser MS, Mahmud M. Towards secured service pro-
Healthcare Things based Alzheimer care during COVID 19. In: visioning for the Internet of Healthcare Things. In: Proc. AICT;
Proc. Brain Inform.; 2020. p. 263–74. 2020. p. 1–6.
38. Ahmed S, Hossain M, Nur SB, Shamim Kaiser M, Mahmud M, 56. Kaiser MS, et al. 6G access network for intelligent Internet of
et al. Toward machine learning-based psychological assessment Healthcare Things: opportunity, challenges, and research direc-
of autism spectrum disorders in school and community. In: Proc. tions. In: Proc. TCCE; 2021. p. 317–28.
TEHI; 2022. p. 139–49. 57. Biswas M, et al. ACCU3RATE: a mobile health application rat-
39. Mahmud M, Kaiser MS, Rahman MA, Wadhera T, Brown DJ, ing scale based on user reviews. PLoS ONE. 2021;16(12).
Shopland N, et al. Towards explainable and privacy-preserving 58. Rabby G, et al. A flexible keyphrase extraction technique for
artificial intelligence for personalisation in autism spectrum academic literature. Procedia Comput Sci. 2018;135:553–63.
disorder. In: Universal Access in Human-Computer Interac- 59. Rabby G, Azad S, Mahmud M, Zamli KZ, Rahman MM. TeKET:
tion. User and Context Diversity: 16th International Confer- a tree-based unsupervised keyphrase extraction technique. Cogn
ence, UAHCI 2022, Held as Part of the 24th HCI International Comput. 2020;12(4):811–33.
Conference, HCII 2022, Virtual Event, June 26–July 1, 2022, 60. Adiba FI, Islam T, Kaiser MS, Mahmud M, Rahman MA. Effect
Proceedings, Part II. Springer; 2022. p. 356–70. of corpora on classification of fake news using naive Bayes clas-
40. Nahiduzzaman M, et al. Machine learning based early fall detec- sifier. International Journal of Automation, Artificial Intelligence
tion for elderly people with neurological disorder using multi- and Machine Learning. 2020 Oct;1(1):80-92. Number: 1. Avail-
modal data fusion. In: Proc. Brain Inform.; 2020. p. 204–14. able from: https://r esear chlak ejour nals.c om/i ndex.p hp/A AIML/
41. Biswas M, et al. Indoor navigation support system for patients articl e/v iew/4 5.
with neurodegenerative diseases. In: Proc. Brain Inform.; 2021. 61. Das S, Yasmin MR, Arefin M, Taher KA, Uddin MN, Rahman
p. 411–22. MA. Mixed Bangla-English spoken digit classification using
42. Sadik R, Reza ML, Al Noman A, Al Mamun S, Kaiser MS, Rahman convolutional neural network. In: Kaiser MS, Kasabov N,
MA. COVID-19 pandemic: a comparative prediction using machine Iftekharuddin K, Zhong N, editors. Mahmud M. Applied
learning. International Journal of Automation, Artificial Intelligence Intelligence and Informatics. Communications in Computer and
and Machine Learning. 2020;1(1):1–16. Information Science. Cham: Springer International Publishing;
43. Mahmud M, Kaiser MS. Machine learning in fighting pandemics: 2021. p. 371–83.
a COVID-19 case study. In: COVID-19: prediction, decision- 62. Nawar A, Toma NT, Al Mamun S, Kaiser MS, Mahmud M,
making, and its impacts. Springer; 2021. p. 77–81. Rahman MA. Cross-content recommendation between movie and
44. Kumar S, et al. Forecasting major impacts of COVID-19 pan- book using machine learning. In: 2021 IEEE 15th International
demic on country-driven sectors: challenges, lessons, and future Conference on Application of Information and Communication
roadmap. Pers Ubiquitous Comput. 2021:1–24. Technologies (AICT); 2021. p. 1–6.
45. Bhapkar HR, et al. Rough sets in COVID-19 to predict sympto- 63. Rahman MA, Brown DJ, Shopland N, Burton A, Mahmud M.
matic cases. In: COVID-19: Prediction, Decision-Making, and Explainable multimodal machine learning for engagement analy-
its Impacts. Springer; 2021. p. 57–68. sis by continuous performance test. In: Stephanidis C, Antona
46. Satu MS, et al. Short-term prediction of COVID-19 cases using M, editors. Universal Access in Human-Computer Interaction.
machine learning models. Appl Sci. 2021;11(9):4266. User and Context Diversity. Lecture Notes in Computer Science.
47. Prakash N, et al. Deep transfer learning for COVID-19 detection Cham: Springer International Publishing; 2022. p. 386–99.
and infection localization with superpixel based segmentation. 64. Rahman MA, Brown DJ, Shopland N, Harris MC, Turabee ZB,
Sustain Cities Soc. 2021;75: 103252. Heym N, et al. Towards machine learning driven self-guided
48. AlArjani A, et al. Application of mathematical modeling in pre- virtual reality exposure therapy based on arousal state detection
diction of COVID-19 transmission dynamics. Arab J Sci Eng. from multimodal data. In: Mahmud M, He J, Vassanelli S, van
2022:1–24. Zundert A, Zhong N, et al., editors. Brain Informatics. Cham:
49. Paul A, et al. Inverted bell-curve-based ensemble of deep learn- Springer International Publishing; 2022. p. 195–209.
ing models for detection of COVID-19 from chest X-rays. Neural 65. Mahmud M, Kaiser MS, Rahman MA. Towards explainable and
Comput Appl. 2022:1–15. privacy-preserving artificial intelligence for personalisation in
50. Mahmud M, Kaiser MS, Rahman MM, Rahman MA, Shabut A, autism spectrum disorder. In: Stephanidis C, Antona M, editors.
Al-Mamun S, et al. A brain-inspired trust management model to Universal Access in Human-Computer Interaction. User and
assure security in a cloud based IoT framework for neuroscience Context Diversity. Lecture Notes in Computer Science. Cham:
applications. Cogn Comput. 2018;10(5):864–73. Springer International Publishing; 2022. p. 356–70.
51. Mahmud M, Kaiser MS, Hussain A, Vassanelli S. Applications 66. Tasnim N, Al Mamun S, Shahidul Islam M, Kaiser MS, Mahmud
of deep learning and reinforcement learning to biological data. M. Explainable mortality prediction model for congestive heart
IEEE Trans Neural Netw Learn Syst. 2018;29(6):2063–79. failure with nature-based feature selection method. Appl Sci.
52. Mahmud M, Kaiser MS, McGinnity TM, Hussain A. Deep learn- 2023;13(10):6138.
ing in mining biological data. Cogn Comput. 2021;13(1):1–33. 67. Banerjee JS, Mahmud M, Brown D. Heart rate variability-
53. Nasrin F, Ahmed NI, Rahman MA. Auditory attention state based mental stress detection: an explainable machine learning
decoding for the quiet and hypothetical environment: a compari- approach. SN Comput Sci. 2023;4(2):176.
son between bLSTM and SVM. In: Kaiser MS, Bandyopadhyay 68. Vimbi V, Shaffi N, Mahmud M, Subramanian K, Hajamohideen
A, Mahmud M, Ray K, editors. Proceedings of TCCE. Advances F. Application of explainable artificial intelligence in Alzheimer’s
1 3

4 80 Cognitive Computation (2024) 16:455–481
disease classification: a systematic review. Cogn. Comput. 90. Wu M, Cao H, Nguyen HL, Surmacz K, Hargrove C. Modeling
2023:1–27. [ePub Ahead of Print]. perceived stress via HRV and accelerometer sensor streams.
69. Banerjee JS, Chakraborty A, Mahmud M, Kar U, Lahby M, In: 2015 37th Annual International Conference of the IEEE
Saha G. Explainable artificial intelligence (XAI) based analysis Engineering in Medicine and Biology Society (EMBC). IEEE;
of stress among tech workers amidst COVID-19 pandemic. In: 2015. p. 1625–8.
Advanced AI and Internet of Health Things for Combating Pan- 91. Pourmohammadi S, Maleki A. Stress detection using ECG and
demics. Springer; 2023. p. 151–74. EMG signals: a comprehensive study. Comput Methods Pro-
70. Hassija V, Chamola V, Mahapatra A, Singal A, Goel D, Huang grams Biomed. 2020;193.
K, et al. Interpreting black-box models: a review on explainable 92. Maldonado S, López J, Jimenez-Molina A, Lira H. Simultane-
artificial intelligence. Cogn. Comput. 2023:1–30. [ePub Ahead ous feature selection and heterogeneity control for SVM classi-
of Print.]. fication: an application to mental workload assessment. Expert
71. Lohani A, Kumar R, Singh R. Hydrological time series mode- Syst Appl. 2020;143.
ling: a comparison between adaptive neuro-fuzzy, neural network 93. Pluntke U, Gerke S, Sridhar A, Weiss J, Michel B. Evalua-
and autoregressive techniques. J Hydrol. 2012;442:23–35. tion and classification of physical and psychological stress in
72. Kuo R, Hong S, Huang Y. Integration of particle swarm optimi- firefighters using heart rate variability. In: 2019 41st Annual
zation-based fuzzy neural network and artificial neural network International Conference of the IEEE Engineering in Medicine
for supplier selection. Appl Math Model. 2010;34(12):3976–90. and Biology Society (EMBC). IEEE; 2019. p. 2207–12.
73. Dimitoglou G, Adams JA, Jim CM. Comparison of the C4. 5 94. Giannakakis G, Marias K, Tsiknakis M. A stress recognition
and a Naïve Bayes classifier for the prediction of lung cancer system using HRV parameters and machine learning tech-
survivability. arXiv:1 206.1 121 [Preprint]. 2012. niques. In: 2019 8th International Conference on Affective
74. Ray S. A quick review of machine learning algorithms. In: 2019 Computing and Intelligent Interaction Workshops and Demos
International conference on machine learning, big data, cloud (ACIIW). IEEE; 2019. p. 269–72.
and parallel computing (COMITCon). IEEE; 2019. p. 35–9. 95. Castaldo R, Xu W, Melillo P, Pecchia L, Santamaria L, James
75. Sevil M, Rashid M, Hajizadeh I, Askari MR, Hobbs N, Brandt R, C. Detection of mental stress due to oral academic examina-
et al. Discrimination of simultaneous psychological and physical tion via ultra-short-term HRV analysis. In: 2016 38th Annual
stressors using wristband biosignals. Comput Methods Programs International Conference of the IEEE Engineering in Medicine
Biomed. 2021;199: 105898. and Biology Society (EMBC). IEEE; 2016. p. 3805–8.
76. Tang C, Chen F, Li X. Perceptron implementation of triple- 96. Delmastro F, Di Martino F, Dolciotti C. Cognitive training and
valued logic operations. IEEE Trans Circuits Syst II Express stress detection in MCI frail older people through wearable
Briefs. 2011;58(9):590–4. sensors and machine learning. IEEE Access. 2020;8:65573–90.
77. Alzubi J, Nayyar A, Kumar A. Machine learning from theory 97. Lima R, de Noronha Osório DF, Gamboa H. Heart rate vari-
to algorithms: an overview. In: Journal of Physics: Conference ability and electrodermal activity in mental stress aloud: pre-
Series, vol. 1142. IOP Publishing; 2018. p. 012012. dicting the outcome. In: Biosignals. 2019. p. 42–51.
78. Liu Y. Random forest algorithm in big data environment. Com- 98. Yu B, Zhang B, An P, Xu L, Xue M, Hu J. An unobtrusive
puter Modelling & New Technologies. 2014;18(12A):147–51. stress recognition system for the smart office. In: 2019 41st
79. Pascanu R, Gulcehre C, Cho K, Bengio Y. How to construct deep Annual International Conference of the IEEE Engineering
recurrent neural networks. arXiv:1 312.6 026 [Preprint]. 2013. in Medicine and Biology Society (EMBC). IEEE; 2019. p.
80. Schmidhuber J. Deep learning in neural networks: an overview. 1326–9.
Neural Netw. 2015;61:85–117. 99. Padmaja B, Prasad VR, Sunitha K, Reddy NCS, Anil C. Detect-
81. LeCun Y, Bengio Y, et al. Convolutional networks for images, Stress: a novel stress detection system based on smartphone and
speech, and time series. The Handbook of Brain Theory and wireless physical activity tracker. In: First international confer-
Neural Networks. 1995;3361(10):1995. ence on artificial intelligence and cognitive computing. Springer;
82. Shrestha A, Mahmood A. Review of deep learning algorithms 2019. p. 67–80.
and architectures. IEEE Access. 2019;7:53040–65. 100. Can YS, Chalabianloo N, Ekiz D, Ersoy C. Continuous stress
83. El-Samahy E, Mahfouf M, Torres-Salomao L, Anzurez-Marin J. A detection using wearable sensors in real life: algorithmic pro-
new computer control system for mental stress management using gramming contest case study. Sensors. 2019;19(8):1849.
fuzzy logic. In: 2015 IEEE International Conference on Evolving 101. Chen C, Li C, Tsai CW, Deng X. Evaluation of mental stress
and Adaptive Intelligent Systems (EAIS). IEEE; 2015. p. 1–7. and heart rate variability derived from wrist-based photoplethys-
84. Wang J, Belatreche A, Maguire LP, McGinnity TM. SpikeTemp: mography. In: 2019 IEEE Eurasia Conference on Biomedical
an enhanced rank-order-based learning approach for spiking neu- Engineering, Healthcare and Sustainability (ECBIOS). IEEE;
ral networks with adaptive structure. IEEE Trans Neural Netw 2019. p. 65–8.
Learn Syst. 2015;28(1):30–43. 102. Koldijk S, Neerincx MA, Kraaij W. Detecting work stress in
85. Kumar M, Zhang W, Weippert M, Freudenthaler B. An explainable offices by combining unobtrusive sensors. IEEE Trans Affect
fuzzy theoretic nonparametric deep model for stress assessment Comput. 2016;9(2):227–39.
using heartbeat intervals analysis. IEEE Trans Fuzzy Syst. 2020. 103. Ciabattoni L, Ferracuti F, Longhi S, Pepa L, Romeo L, Verdini F.
86. Ranganathan G, Rangarajan R, Bindhu V. Estimation of heart Real-time mental stress detection based on smartwatch. In: 2017
rate signals for mental stress assessment using neuro fuzzy tech- IEEE International Conference on Consumer Electronics (ICCE).
nique. Appl Soft Comput. 2012;12(8):1978–84. IEEE; 2017. p. 110–1.
87. Kumar M, Weippert M, Vilbrandt R, Kreuzfeld S, Stoll R. Fuzzy 104. Attaran N, Brooks J, Mohsenin T. A low-power multi-
evaluation of heart rate signals for mental stress assessment. physiological monitoring processor for stress detection. In: 2016
IEEE Trans Fuzzy Syst. 2007;15(5):791–808. IEEE Sensors. IEEE; 2016. p. 1–3.
88. Sriramprakash S, Prasanna VD, Murthy OR. Stress detection in 105. Castaldo R, Montesinos L, Melillo P, James C, Pecchia L. Ultra-
working people. Procedia Comput Sci. 2017;115:359–66. short term HRV features as surrogates of short term HRV: a case
89. Huang S, Li J, Zhang P, Zhang W. Detection of mental fatigue study on mental stress detection in real life. BMC Med Inform
state with wearable ECG devices. Int J Med Informatics. Decis Mak. 2019;19(1):1–13.
2018;119:39–46.
1 3

Cognitive Computation (2024) 16:455–481 481
106. Hantono BS, Nugroho LE, Santosa PI. Mental stress detection 117. Coutts LV, Plans D, Brown AW, Collomosse J. Deep learning
via heart rate variability using machine learning. Int J Electr Eng with wearable based heart rate variability for prediction of men-
Inform. 2020;12(3):431–44. tal and general health. J Biomed Inform. 2020;112: 103610.
107. Tiwari A, Cassani R, Gagnon JF, Lafond D, Tremblay S, Falk 118. He J, Li K, Liao X, Zhang P, Jiang N. Real-time detection of
TH. Prediction of stress and mental workload during police acad- acute cognitive stress using a convolutional neural network from
emy training using ultra-short-term heart rate variability and electrocardiographic signal. IEEE Access. 2019;7:42710–7.
breathing analysis. In: 2020 42nd Annual International Confer- 119. Qin Z, Li M, Huang L, Zhao Y. Stress level evaluation using
ence of the IEEE Engineering in Medicine & Biology Society BP neural network based on time-frequency analysis of HRV.
(EMBC). IEEE; 2020. p. 4530–3. In: 2017 IEEE International Conference on Mechatronics and
108. Clark J, Nath RK, Thapliyal H. Machine learning based predic- Automation (ICMA). IEEE; 2017. p. 1798–803.
tion of future stress events in a driving scenario. arXiv:2 106. 120. Ding Y, Cao Y, Duffy VG, Wang Y, Zhang X. Measurement and
07542 [Preprint]. 2021. identification of mental workload during simulated computer
109. Ahmad Z, Rabbani S, Zafar MR, Ishaque S, Krishnan S, Khan tasks with multimodal methods and machine learning. Ergonom-
N. Multi-level stress assessment from ECG in a virtual reality ics. 2020;63(7):896–908.
environment using multimodal fusion. arXiv:2 107.0 4566 [Pre- 121. Kalatzis A, Stanley L, Karthikeyan R, Mehta RK. Mental stress
print]. 2021. classification during a motor task in older adults using an artifi-
110. Dalmeida KM, Masala GL. HRV features as viable physiologi- cial neural network. In: Adjunct Proceedings of the 2020 ACM
cal markers for stress detection using wearable devices. Sensors. International Joint Conference on Pervasive and Ubiquitous
2021;21(8):2873. Computing and Proceedings of the 2020 ACM International
111. Sandulescu V, Andrews S, Ellis D, Bellotto N, Mozos OM. Stress Symposium on Wearable Computers; 2020. p. 244–8.
detection using wearable physiological sensors. In: International 122. Dhaouadi S, Ben Khelifa MM. A multimodal physiological-
work-conference on the interplay between natural and artificial based stress recognition: deep Learning models’ evaluation in
computation. Springer; 2015. p. 526–32. gamers’ monitoring application. In: 2020 5th International Con-
112. Munla N, Khalil M, Shahin A, Mourad A. Driver stress level ference on Advanced Technologies for Signal and Image Process-
detection using HRV analysis. In: 2015 International Confer- ing (ATSIP). IEEE; 2020. p. 1–6.
ence on Advances in Biomedical Engineering (ICABME). IEEE; 123. Stewart CL, Folarin A, Dobson R. Personalized acute stress
2015. p. 61–4. classification from physiological signals with neural pro-
113. de Vries JJG, Pauws SC, Biehl M. Insightful stress detection cesses. arXiv:2 002.0 4176 [Preprint]. 2020.
from physiology modalities using learning vector quantization. 124. Silva E, Aguiar J, Reis LP, e Sá JO, Gonçalves J, Carvalho V.
Neurocomputing. 2015;151:873–82. Stress among Portuguese medical students: the EuStress solution.
114. Son HH. Toward a proposed framework for mood recognition J Med Syst. 2020;44(2):1–6.
using LSTM recurrent neuron network. Procedia Computer Sci- 125. Yaribeygi H, Panahi Y, Sahraei H, Johnston TP, Sahebkar A.
ence. 2017;109:1028–34. The impact of stress on body function: a review. EXCLI J.
115. Rastgoo MN, Nakisa B, Maire F, Rakotonirainy A, Chandran 2017;16:1057.
V. Automatic driver stress level classification using multimodal
deep learning. Expert Syst Appl. 2019;138: 112793. Publisher's Note Springer Nature remains neutral with regard to
116. Akbulut FP, Ikitimur B, Akan A. Wearable sensor-based evalua- jurisdictional claims in published maps and institutional affiliations.
tion of psychosocial stress in patients with metabolic syndrome.
Artif Intell Med. 2020;104: 101824.
1 3