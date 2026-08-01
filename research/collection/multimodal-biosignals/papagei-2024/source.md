PublishedasaconferencepaperatICLR2025
|         | PAPAGEI: |               | OPEN |     | FOUNDATION |         | MODELS |     | FOR |     |
| ------- | -------- | ------------- | ---- | --- | ---------- | ------- | ------ | --- | --- | --- |
| OPTICAL |          | PHYSIOLOGICAL |      |     |            | SIGNALS |        |     |     |     |
ArvindPillai2∗,DimitrisSpathis1,3,FahimKawsar1,4,MohammadMalekzadeh1
1NokiaBellLabs,Cambridge,UK,2DartmouthCollege,NH,USA,
3UniversityofCambridge,UK,4UniversityofGlasgow,Scotland,UK
ABSTRACT
5202 beF 5  ]GL.sc[  2v24502.0142:viXra
Photoplethysmography(PPG)istheleadingnon-invasivetechniqueformonitor-
|     | ing                                                       | biosignals  | and             | cardiovascular |                                           | health, with | widespread               | adoption        | in            | both clin- |
| --- | --------------------------------------------------------- | ----------- | --------------- | -------------- | ----------------------------------------- | ------------ | ------------------------ | --------------- | ------------- | ---------- |
|     | ical                                                      | settings    | and consumer    |                | wearable                                  | devices.     | While                    | machine         | learning      | models     |
|     | trained                                                   | on PPG      | signals         | have           | shown                                     | promise,     | they tend                | to be           | task-specific | and        |
|     | struggle                                                  | with        | generalization. |                | Current                                   | research     | is limited               | by              | the use       | of single- |
|     | device                                                    | datasets,   | insufficient    |                | exploration                               | of           | out-of-domain            | generalization, |               | and a      |
|     | lack                                                      | of publicly | available       |                | models,                                   | which        | hampers reproducibility. |                 | To            | address    |
|     | theselimitations,wepresent                                |             |                 |                | PAPAGEI,thefirstopenfoundationmodelforPPG |              |                          |                 |               |            |
|     | signals.                                                  | The         | model           | is pre-trained |                                           | on over      | 57,000 hours             | of data,        | comprising    | 20         |
|     | millionunlabeledPPGsegmentsfrompubliclyavailabledatasets. |             |                 |                |                                           |              |                          |                 | Weintroducea  |            |
novelrepresentationlearningapproachthatleveragesdomainknowledgeofPPG
|     | signal | morphology |     | across | individuals, | enabling | the capture | of  | richer representa- |     |
| --- | ------ | ---------- | --- | ------ | ------------ | -------- | ----------- | --- | ------------------ | --- |
tionscomparedtotraditionalcontrastivelearningmethods.WeevaluatePAPAGEI
|     | against | state-of-the-art |     | time-series |     | foundation | models | and self-supervised |     | learn- |
| --- | ------- | ---------------- | --- | ----------- | --- | ---------- | ------ | ------------------- | --- | ------ |
ingbenchmarksacross20tasksfrom10diversedatasets,spanningcardiovascular
|     | health, | sleep        | disorders, | pregnancy |              | monitoring, | and wellbeing |                | assessment. | Our     |
| --- | ------- | ------------ | ---------- | --------- | ------------ | ----------- | ------------- | -------------- | ----------- | ------- |
|     | model   | demonstrates |            | superior  | performance, |             | improving     | classification | and         | regres- |
sionmetricsby6.3%and2.9%respectivelyinatleast14tasks.Notably,PAPAGEI
achievestheseresultswhilebeingmoredata-andparameter-efficient,outperform-
|     | ingmodelsthatare70×larger. |     |     |     | Beyondaccuracy,weexaminemodelrobustness |     |     |     |     |     |
| --- | -------------------------- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- |
acrossdifferentskintones,establishingabenchmarkforbiasevaluationinfuture
|     | models. | PAPAGEIcanserveasbothafeatureextractorandanencoderformulti- |     |     |     |     |     |     |     |     |
| --- | ------- | ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
modalmodels,openingupnewopportunitiesformultimodalhealthmonitoring1.
1 INTRODUCTION
Photoplethysmography(PPG),anon-invasiveopticalsensingtechnique,iswidelyusedtomonitor
cardiovascular health and physiological signals in both clinical and consumer health applications
(Charlton et al., 2023). From hospital pulse oximeters to smartwatches, PPG enables continuous
health monitoring in various settings, bridging acute medical care and long-term health manage-
ment. PPG signals help in tracking a diverse range of health indicators, including cardiovascular
health,bloodpressure,mood,andsleepdisorders(Sadadetal.,2022;Aveetal.,2015;Reissetal.,
2019;Liangetal.,2018a;Haddadetal.,2021;Schrumpfetal.,2021). Despiteitswidespreadadop-
tion,PPGposessubstantialchallengesformachinelearningapplications. Aprimaryobstacleisthe
highcostofdataannotation,whichrequiresspecializeddomainexpertise. Thischallengeispartic-
ularly pronounced in consumer health applications, where varying sensing conditions and diverse
userpopulationscreateadditionalcomplexity. PPGsignalsaresusceptibletonoiseandmotionarti-
facts(AfandizadehZargarietal.,2023),aswellasinherentvariabilityduetofactorslikeskintone
andbodycomposition(Bentetal.,2020). ThesecomplicatethedevelopmentofgeneralizableML
modelsforPPG.Consequently,existingPPGdatasetsareoftensmall,task-specific,andlimitedin
their generalizability, posing a major obstacle to the development of robust and widely applicable
modelsthatcouldfullyleveragethepotentialofPPGtechnology.
∗Workhasbeendoneduringtheauthor’sinternshipatNokiaBellLabs.
1Models,data,andcodeareavailableat:github.com/nokia-bell-labs/papagei-foundation-model
1

PublishedasaconferencepaperatICLR2025
Figure1: PAPAGEIOverview. WecuratepublicdatasetsofdiversePPGsignals,andtrainafounda-
tionmodelleveraginganovelmorphology-awarecontrastivelearningapproach. Toevaluateitsef-
fectiveness,weapplytheembeddingsgeneratedbyPAPAGEIto20tasksfrom10differentdatasets.
The PPG domain, unlike language or vision domains, lacks general-purpose foundation models
(FMs),withmostcurrentworksfocusedonsingle-datasettask-specificmodels. AlthoughPPGcan
detectvitalsignslikeheartratevariabilityandbloodoxygensaturation,theabsenceofgeneralizable
pre-trainedmodelslimitsprogress(Abbaspourazadetal.,2023). Despitetheongoingchallengesof
acquiringlarge-scale,high-qualitydata,recentexpansionsindiversePPGdatasetshavecreatednew
opportunities(Johnsonetal.,2016;Zhangetal.,2018;Leeetal.,2022).Toaddressthesechallenges,
we introduce PAPAGEI, a set of robust, pre-trained models capable of serving as a backbone for
variousPPG-relatedtasks,capturingrichPPGrepresentationsthroughlarge-scalepre-training.
ThekeycontributionsofPAPAGEIare:
(1)Large-scalepre-trainingforPPGsignals: Toourknowledge,PAPAGEIisthefirstopenfoun-
dationmodelpre-trainedonPPGsignals,using57,000hoursofdatafrom20millionsignalssourced
entirelyfrompublicdatasets. Thisestablishesanewbenchmarkforlarge-scalemodeldevelopment
inwearableandclinicalhealthmonitoring.
(2)PPG-awareself-supervisedlearning(SSL)framework:WeintroduceanovelSSLframework
with a unique PPG signal morphology augmentation module. Our approach optimizes agreement
betweenPPGsignalswithsimilarbloodvolumechangeswhilepointingthemodeltopayattention
tothechangesaroundthesystolicpeakanddicroticnotch(keyPPGmarkers).
(3)Comprehensiveevaluationacrossdiverseout-of-domainhealthtasks:WeevaluatePAPAGEI
across20tasks,includingcardiovascularhealth,sleepdisorders,pregnancymonitoring,andoverall
well-being. Our results show that the model embeddings contain rich and predictive information
applicabletovarioushealthconditions,outperformingexistingbenchmarks.
(4)Extensiverobustnessstudies: Weconductablationstudiestoassesstheimpactofkeycompo-
nents,includingsignalmorphologyaugmentation,comparisonswithestablishedcontrastivelearning
approaches,modelsize,dataefficiency,andtheeffectofskintone.
2 RELATED WORK
Self-supervisedlearninghasbecomeaprominentparadigmforlearninggeneralrepresentationsfrom
unlabeleddatasets, withapplicationsinphysiologicalsignalanalysisincludinghealth, fitness, and
brain signals (Tonekaboni et al., 2021; Zhang et al., 2022; Chen et al., 2021; Ye`che et al., 2021;
Spathisetal.,2021;Chengetal.,2020;Kiyassehetal.,2021;Sarkar&Etemad,2020). Despiteits
popularity,therearenowidelyusedmodelsforPPGsignalspre-trainedthroughSSL.Recently,Ab-
baspourazadetal.(2023)demonstratedthatembeddingsderivedfromPPGsignalscanpredictover
45 diverse downstream health-related tasks using proprietary Apple Watch data. Their approach
uses an SSL framework based on patient-level positive pair contrastive learning. Similarly, (Yun
etal.,2024)showedthatembeddingPPGsignalscanimprovegeneticdiscoveryandriskprediction
outcomesusingtheUKBiobankdataset. Otherworks(Wengetal.,2024;Dingetal.,2024;Zhou
etal.,2024)exploredPPGembeddingsforvariousapplications. However,thesestudiesoftenused
proprietarydatasets, didnotexploreout-of-domaingeneralization, ordidnotreleasetheirmodels,
highlightingtheneedforopenlyavailable,pre-trainedPPGFMs(Table17).Forexample,incontrast
to(Abbaspourazadetal.,2023),ourworkexclusivelyusespublicdatasetsforlarge-scalePPGtrain-
ingandintroducesanovelSSLframeworktoincorporatePPGmorphology. WhileAbbaspourazad
et al. (2023) evaluate a single proprietary dataset, we validate on 10 diverse downstream datasets,
showcasinggreatergeneralizabilityandrobustnessacrossvariedreal-worldscenarios.
2

PublishedasaconferencepaperatICLR2025
IPA
SVRI
SQI
Similar Dissimilar Inflection Point Loss Contrastive Loss Signal Quality Loss
Figure 2: Overview of PAPAGEI-S. The process begins by computing three morphology metrics
(IPA,SVRI,andSQI)foreachPPGsegment. TherawPPGsignalsarethenprocessedthroughan
encoder(E)togenerateembeddings(H).Thesesameembeddingsfeedintothreespecializedheads:
aprojectionhead(P)thatcontrastsPPGsignalsbasedonsVRIvalues,andtwomixture-of-expert
heads(M andM )thatrefinetheembeddingsbypredictingIPAandSQIvalues.
1 2
Generic time-series FMs, like Chronos (Ansari et al., 2024) and Moment (Goswami et al., 2024),
lackphysiologicaldatarepresentation. Thereisgrowinginterestinmodality-specificFMstailored
tophysiologicalsignals(Songetal.,2024;Laietal.,2023)andhumanactivity(Yuanetal.,2024a).
Knowledgetransferfromtime-seriesFMsmightbenefitPPGtasks,buttheirperformanceislimited
comparedtoPPG-specificFMs. Adaptingotherdomain-specificmodels,likeECG(McKeenetal.,
2024;Songetal.,2024)orEEG(Yuanetal.,2024b),ischallengingduetodistinctsignalcharacter-
istics. WespecificallydesignFMsforPPGsignals, contributingtothegrowingmovementtoward
foundationmodelstailoredtoindividualmodalities. SeeAppendix§Hforanextendeddiscussion.
3 METHODS
Given a dataset D = {p1,p2,··· ,pS} representing diverse PPG signals from S participants, a
PPG signal ps ∈ Rn is defined as a time-series that captures variations in light intensity caused
byarterialbloodflow. TomodelgranularchangesinPPGsignalofeachsubjects,wesegmentps
without overlap to obtain Xs = {xs,xs,···xs }. Here, the number of segments N depends on
1 2 N
thesamplingfrequency(f)andthedesiredlengthoftimewindow. Totrainourfoundationmodels,
PAPAGEI-PemploysapatientcontrastiveSSLapproachthatmaximizesagreementbetweensignals
fromthesamesubject. Importantly,wepropose PAPAGEI-S,amorphology-awareself-supervised
approachthatmaximizesagreementbetweenPPGsegmentswithsimilarmorphology.
3.1 PARTICIPANT-AWAREOBJECTIVE: PAPAGEI-P
In PAPAGEI-P, we train an SSL model to maximize agreement between the embeddings of PPG
signals from the same subject. While previous studies have demonstrated the effectiveness of this
strategy for physiological signals (Kiyasseh et al., 2021; Abbaspourazad et al., 2023), our work
represents the first attempt to train and evaluate a foundation model using publicly available PPG
datasets.
Training. We define a positive pair as any two distinct segments of PPG signals from the same
subject, denoted as {(xs,xs)|i ̸= j}. Next, we apply a series of time-series augmentations such
i j
as random cropping, adding Gaussian noise, time flipping, negation, and magnitude scaling (Tang
et al., 2020), each applied with a predefined probability during training. Each augmentation in-
cludes hyper-parameters that control the intensity of the data transformation. During training, the
augmentedversionofarandomlysampledpositivepair(xs,xs)ispassedthroughtheencoderE,
i j
and subsequently projection P, to obtain an embeddings pair denoted by (zs,zs). Given a batch
i j
of embeddings from N positive pairs of the form (z ,z ), the model optimizes the normalized
i j
temperature-scaledcrossentropy(NT-Xent)loss(Sohn,2016;Oordetal.,2018;Chenetal.,2020)
3

PublishedasaconferencepaperatICLR2025
givenby:L = 1(ℓ (i,j)+ℓ (j,i)),whereℓ (i,j)=−1 (cid:80)N log exp(sim(zu i ,zu j )/τ)
p 2 p p p N u=1 (cid:80)2N 1[v̸=u]exp(sim(zu,zv)/τ)
v=1 i j
andsim(·,·)isthecosinesimilarity.Incontrast,vanillaSimCLR(Chenetal.,2020)wouldusepos-
itivepairsasaugmentedversionsofrandomlysampledPPGsegments.
3.2 MORPHOLOGY-AWAREOBJECTIVE: PAPAGEI-S
InPAPAGEI-S,weleveragethePPGsignalmorphologytotrainaSSLmodelthatmaximizesagree-
mentbetweensimilarphysiologicalfeaturesofPPGsignalsacrossparticipants.
PPGMorphology.Totalperipheralresistance(TPR)—theforceexertedbythebody’sbloodvessels
on circulating blood—varies under certain medical conditions, such as hypertension and diabetes
(Trammel & Sapra, 2020). Variations in TPR are reflected in PPG signals, presenting as distinct
regionswithinthewaveform. Tocapturethesevariations,weintroduceamorphologyaugmentation
modulebeforetraining,whichcomputesthreekeyPPGmetrics(Figure2,left): (1)stress-induced
VascularResponseIndex(sVRI)(Lyuetal.,2015;Zhangetal.,2019): theratioofmeanPPGsig-
nalbetweenpost-topre-systolicphases,(2)InflectionPointArearatio(IPA)(Wangetal.,2009):
the ratio of systolic to diastolic areas defined by the dicrotic notch, and (3) Signal Quality Index
(SQI):skewnessofthesignalasanindicatorofquality(Elgendi,2016). Priorstudieshaveshown
thatincorporatingthePPGsignalqualityduringtrainingyieldspositiveresults(Dingetal.,2024).
We selected these metrics for their complementary nature: sVRI captures variations in amplitude,
whileIPAmeasuressignalwidth.ToaddressscenarioswherecomputingIPAischallengingbecause
ofnoisysignalsordifferentmorphology,weincorporateSQI.Inparticular,weempiricallyfindthat
SQIissignificantlylarger(p<0.05)insignalswithadicroticnotch(Appendix§D.5).
sVRI(x)= sys (cid:80)n i=sys x i , IPA(x)= (cid:82) 0 nˆ xdn , and SQI(x)= 1 (cid:88) m 3 , (1)
(n−sys) (cid:80)s
i=
ys
1
x
i
(cid:82)
nˆ
n xdn W
w
m3
2
/2
wherex ∈ RN isthePPGsegment,sysisthesystolicpeak,nisthelengthoftimeseries,andnˆ is
thedicroticnotch.ForSQI,wedividexinto5secondwindows(w;totalwindowsW)andcompute
theskewnessm = 1 (cid:80)5×f(x[j]−µ [j])i,whichgivesthebestsignalqualitydiscrimination.
i 5×f j=1 x
Training. Before training, the morphology augmentation module takes an augmented input, by
applying Gaussian noise and cropping to time series x, and outputs y = {ysvri,yipa,ysqi} ∈ R3
(Figure 2 middle). Next, we discretize ysvri into a predefined set of b = 8 bins to denote pos-
itive pairs, where ysvri ∈ {1,...,b}. We define positive pairs based on the sVRI labels as
{(x ,x )|ysvri =ysvri,i̸=j}. Notethatpositivepairsarenotdefinedbasedonparticipants.
i j i j
exp(sim(z ,z )/τ)
ℓ (i,j)=−log i j (2)
s (cid:80)2N 1[k ̸=i]exp(sim(z ,z )/τ)
k=1 i k
N
1 (cid:88)
L = [ℓ(2k−1,2k)+ℓ(2k,2k−1)] (3)
svri 2N
k=1
1 (cid:88) N (cid:12) (cid:12) 1 (cid:88) N (cid:12) (cid:12)
L = (cid:12)yipa−yˆipa(cid:12) L = (cid:12)ysqi−yˆsqi(cid:12) (4)
ipa N (cid:12) i i (cid:12) sqi N (cid:12) i i (cid:12)
i=1 i=1
L =αL +(1−α)(L +L ),whereα∈[0,1] (5)
s svri ipa sqi
GivenabatchofN PPGsignalsandtheirmorphology,weoptimizethreeheadsusingtheencoder
(E)embeddingsH = {h ,h ,··· ,h }. First,weextracttheembeddingsZ = {z ,z ,··· ,z }
1 2 N 1 2 N
fromtheprojection(P),andcomputethecontrastivelossforsVRI(equation3). Next,weusethe
embeddingsH topredicttheIPA(yˆipa ∈ RN)andSQI(yˆsqi ∈ RN)usingthemixtureofexpert
(MoE) heads M and M . Each MoE head is composed of three fully connected neural networks
1 2
(FCNNs), with the head’s output calculated as a weighted sum of the FCNNs, using softmax to
determinetheweights. Theseheadsareoptimizedusingthemeanabsoluteerror(equation4). The
morphologyindicesencapsulatevariousPPGcharacteristics. OurrationaleforutilizingMoEisthat
eachexpertcanspecializeinlearningdistinctpropertiesthatcontributetotheoverallindex. Finally,
theoverallPAPAGEI-Strainingobjectiveisgiveninequation5.
4

PublishedasaconferencepaperatICLR2025
4 EXPERIMENTS
4.1 PRE-TRAINING
Datasets. Wepre-train PAPAGEI onthreedatasets: (1)VitalDB(Leeetal.,2022),whichincludes
PPGsignalscollectedduringsurgeryfromthepatient’sfinger(f=500Hz),(2)theMIMIC-IIIwave-
form database matched subset (Johnson et al., 2016), where finger-tip PPG data is collected from
anICUmonitor(f=125Hz),and(3)theMulti-EthnicStudyofAtherosclerosis(MESA)sleepsub-
study(Zhangetal.,2018;Chenetal.,2015),whichprovidesPPGdataobtainedthroughfinger-tip
polysomnography(f=256Hz). Intotal,wehave13.5Kparticipantswith20Msegments(Table1).
| Pre-processing. |     | To  | curate single-channel |     |     | PPG sig- |     |     |
| --------------- | --- | --- | --------------------- | --- | --- | -------- | --- | --- |
nals across all datasets, we perform the following Table1: PAPAGEI’spre-trainingdatasets.
| steps: (1)         | Apply   | a 4th-order | Chebyshev     |            | bandpass | fil-      |               |                  |
| ------------------ | ------- | ----------- | ------------- | ---------- | -------- | --------- | ------------- | ---------------- |
| ter with           | low and | high        | pass cut-offs |            | set at   | 0.5Hz and |               |                  |
|                    |         |             |               |            |          | Dataset   | #Participants | #Segments Hours  |
| 12Hz, respectively |         | (Lapitan    | et            | al., 2024; | Liang    | et al.,   |               |                  |
|                    |         |             |               |            |          | VitalDB   | 5,866         | 6,248,100 17,355 |
2018c); (2) Segment the signal into 10-second win- MIMIC-III 5,596 7,196,401 19,990
dows ((Orphanidou, 2018; Koteska et al., 2022) use MESA 2,055 7,306,705 20,296
| 10s windows   |          | whereas  | larger        | studies    | use    | 30s (Ding |        |                   |
| ------------- | -------- | -------- | ------------- | ---------- | ------ | --------- | ------ | ----------------- |
|               |          |          |               |            |        | Total     | 13,517 | 20,751,206 57,641 |
| et al., 2024) | and      | 60s      | Abbaspourazad |            | et al. | (2023));  |        |                   |
| (3) Detect    | flatline | segments |               | and remove |        | any seg-  |        |                   |
ment where more than 25% of the data is flat (BioBSS Documentation, 2023); (4) Nor-
malize the segments using Z-score (Temko, 2017; Zhou et al., 2017); and (5) Resample
the segments to 125Hz (the lowest sampling rate of our pre-training datasets, MIMIC-III).
| Implementation. |     |     | We adopt |     |     |     |     |     |
| --------------- | --- | --- | -------- | --- | --- | --- | --- | --- |
a ResNet-style CNN encoder, Table 2: PAPAGEI’s evaluation datasets. Gray lines are unseen
following (Ding et al., 2024). duringtraining(out-of-domain). Forthoseusedforpre-training,
Abbaspourazad et al. (2023) we keep a held-out test-sets and use labels. Task Types are:
alsoutilizeanEfficientNet-style
B=binary,R=regression,M-#classes=muticlassclassification.
CNN.Ourmodelhas18convo-
| lutional | blocks, | starting | with | a   |         |     |                |                |
| -------- | ------- | -------- | ---- | --- | ------- | --- | -------------- | -------------- |
|          |         |          |      | #ID | Dataset |     | Task(TaskType) | #Subj.(#Samp.) |
filter size of 32, which doubles T1 VitalDB(Leeetal.,2022) ICUadmission(B) 5866
| every 4 | blocks. | The | projection | T2  |                            |     | OperationType(M-9) | 5866 |
| ------- | ------- | --- | ---------- | --- | -------------------------- | --- | ------------------ | ---- |
|         |         |     |            | T3  | MIMIC-III(Moodyetal.,2020) |     | Mortality(B)       | 5596 |
layerisasingleFClayer,gener-
|                       |          |       |            | T4  | MESA(Zhangetal.,2018)    |     | Smoker(B)             | 2055       |
| --------------------- | -------- | ----- | ---------- | --- | ------------------------ | --- | --------------------- | ---------- |
| atinga512-dembedding. |          |       | Inthe      | T5  |                          |     | AHI>3%OxygenDesat.(R) | 2055       |
| PAPAGEI-S             | variant, |       | the expert | T6  |                          |     | AHI>4%OxygenDesat.(R) | 2055       |
|                       |          |       |            | T7  | nuMom2B(Faccoetal.,2015) |     | Pregnancystage(B)     | 3163(5337) |
| block (M              | 1 &      | M 2 ) | uses three | T8  |                          |     | GestationAge(R)       | 3163(5337) |
|                       |          |       |            | T9  | VV(SkinTone)(Toye,2023)  |     | SystolicBP*(R)        | 231        |
| parallel              | FCNNs,   | each  | with two   |     |                          |     |                       |            |
|                       |          |       |            | T10 |                          |     | DiastolicBP*(R)       | 231        |
FC layers, resulting in a 128- T11 PPG-BP(Liangetal.,2018a) SystolicBP(R) 219
| d embedding. |     | For | augmenta- | T12 |     |     | DiastolicBP(R)      | 219 |
| ------------ | --- | --- | --------- | --- | --- | --- | ------------------- | --- |
|              |     |     |           | T13 |     |     | AverageHeartRate(R) | 219 |
tions,PAPAGEI-Pusescropping
|                  |     |         |          | T14 |                      |     | Hypertension(B)             | 219 |
| ---------------- | --- | ------- | -------- | --- | -------------------- | --- | --------------------------- | --- |
|                  |     |         |          | T15 | SDB(Gardeetal.,2014) |     | SleepDisorderedBreathing(B) | 146 |
| (0.50), negation |     | (0.20), | flipping |     |                      |     |                             |     |
|                  |     |         |          | T16 | ECSMP(Gaoetal.,2021) |     | MoodDisturbance(B)          | 89  |
(0.20), and scaling (0.40). PA- T17 WESAD(Schmidtetal.,2018) Valence(B) 15(4497)
| PAGEI-S      | uses   | cropping      | (0.25) | T18 |                            |     | Arousal(B)    | 15(4497)  |
| ------------ | ------ | ------------- | ------ | --- | -------------------------- | --- | ------------- | --------- |
|              |        |               |        | T19 | PPG-DaLiA(Reissetal.,2019) |     | HeartRate(R)  | 15(64697) |
| and Gaussian | noise  | (0.25).       | PA-    |     |                            |     |               |           |
|              |        |               |        | T20 |                            |     | Activity(M-9) | 15(64697) |
| PAGEI-S      | avoids | augmentations |        |     |                            |     |               |           |
| that alter   | PPG’s  | morphology.   |        |     |                            |     |               |           |
10−4),
We set α = 0.6 and train on eight V100 GPUs for 15,000 steps (lr= with PAPAGEI-P
and PAPAGEI-S having 5M and 5.7M parameters, respectively, while previous works use model
sizesof3.3M(Abbaspourazadetal.,2023)(westudyscalinginSection5.2).
4.2 DOWNSTREAMTASKS
Toevaluatetheeffectivenessof PAPAGEI,webenchmarkitagainstadiversesetofdatasets,tasks,
andbaselines,chosenfortheirlargesizeandclinicalrelevance(whereapplicable)2.Adescriptionof
thetaskswiththeircorresponding#IDisprovidedinTable2,withfurtherdetailsinAppendix§B.
As a motivation, identifying patient risk factors is crucial for hospitals to allocate resources ef-
fectively. To address this, we evaluate several indicators, including ICU admission (T1), type of
operation(T2), mortality(T3), andsmokingstatus(T4). Forsleepapneadiagnosis, theAmerican
2https://peterhcharlton.github.io/post/ppg_datasets/
5

PublishedasaconferencepaperatICLR2025
REGLE Chronos Moment Stat. Features
Smoker Smoker Smoker Smoker
Pregnancy Pregnancy Pregnancy Pregnancy
0.82 0.64Mortality 0.82 0.64Mortality 0.82 0.64Mortality 0.82 0.64Mortality
Hypertension 0.7 Hypertension 0.7 Hypertension 0.7 Hypertension 0.7
0.78 0.78 0.78 0.78
0.8ICU 0.8ICU 0.8ICU 0.8ICU
0.7 0.7 0.7 0.7
Apnea 0.6 Apnea 0.6 Apnea 0.6 Apnea 0.6
0.6 0.58 Arousal 0.6 0.58 Arousal 0.6 0.58 Arousal 0.6 0.58 Arousal
Mood Valence Mood Valence Mood Valence Mood Valence
SimCLR BYOL TF-C PaPaGei (Ours)
Smoker Smoker Smoker Smoker
Pregnancy Pregnancy Pregnancy Pregnancy
0.82 0.64Mortality 0.82 0.64Mortality 0.82 0.64Mortality 0.82 0.64Mortality
Hypertension 0.7 Hypertension 0.7 Hypertension 0.7 Hypertension 0.7
0.78 0.78 0.78 0.78
0.8ICU 0.8ICU 0.8ICU 0.8ICU
0.7 0.7 0.7 0.7
Apnea 0.6 Apnea 0.6 Apnea 0.6 Apnea 0.6
0.6 0.58 Arousal 0.6 0.58 Arousal 0.6 0.58 Arousal 0.6 0.58 Arousal
Mood Valence Mood Valence Mood Valence Mood Valence
REGLE Chronos Moment Stat. Features
Gestation Gestation Gestation Gestation
Sys. BP* Sys. BP* Sys. BP* Sys. BP*
18.0 8.0AHI > 4% 18.0 8.0AHI > 4% 18.0 8.0AHI > 4% 18.0 8.0AHI > 4%
13.0 13.0 13.0 13.0
Dia. BP*12.0 Dia. BP*12.0 Dia. BP*12.0 Dia. BP*12.0
16.0AHI > 3% 16.0AHI > 3% 16.0AHI > 3% 16.0AHI > 3%
18.0 18.0 18.0 18.0
Sys. BP 17.0 Sys. BP 17.0 Sys. BP 17.0 Sys. BP 17.0
12.0 10.0 HR 12.0 10.0 HR 12.0 10.0 HR 12.0 10.0 HR
Dia. BPAvg. HR Dia. BPAvg. HR Dia. BPAvg. HR Dia. BPAvg. HR
SimCLR BYOL TF-C PaPaGei (Ours)
Gestation Gestation Gestation Gestation
Sys. BP* Sys. BP* Sys. BP* Sys. BP*
18.0 8.0AHI > 4% 18.0 8.0AHI > 4% 18.0 8.0AHI > 4% 18.0 8.0AHI > 4%
13.0 13.0 13.0 13.0
Dia. BP*12.0 Dia. BP*12.0 Dia. BP*12.0 Dia. BP*12.0
16.0AHI > 3% 16.0AHI > 3% 16.0AHI > 3% 16.0AHI > 3%
18.0 18.0 18.0 18.0
Sys. BP 17.0 Sys. BP 17.0 Sys. BP 17.0 Sys. BP 17.0
12.0 10.0 HR 12.0 10.0 HR 12.0 10.0 HR 12.0 10.0 HR
Dia. BPAvg. HR Dia. BPAvg. HR Dia. BPAvg. HR Dia. BPAvg. HR
Figure3: Radarchartsofdownstreamtasks. (Top)ClassificationperformanceinAUROC(larger
area is better). (Bottom) Regression performance in MAE (smaller area is better). Pre-trained
modelsinpurple: REGLE,Chronos,&Moment. Statisticalfeaturebaselineingray. SSLmethods
ingreen: SimCLR,BYOL,&TF-C.PAPAGEI(ours),inpink. DetailsareinTables3&4.
AcademyofSleepMedicinerecommendsusingtheApnea/HypopneaIndex(AHI)withatleast3%
or4%oxygendesaturationasakeymetric(Ruehlandetal.,2009). Thus,wepredictAHIat3%and
4%desaturationthresholds(T5&T6)andclassifysleep-disorderedbreathing(T15). Forpregnancy
outcomes,changesingestationalageandpregnancystagearelinkedtoriskslikehypertensivedis-
orders and small-for-gestational-age delivery (Bouariu et al., 2022; Wu et al., 2020; Crump et al.,
2023),enablingustoclassifypregnancystage(T7)andpredictgestationalage(T8).Incardiovascu-
larhealth,weestimatesystolic(T9&T11)anddiastolic(T10&T12)bloodpressure(BP)usingtwo
datasets. WhilePPG-BP(T11&T12)provideshigh-frequency,shortPPGsignals,theVVdataset
helps explore skin tone’s influence on BP estimation. We also assess hypertension classification
(T14),averageseatedheartrate(T13),andcontinuousheartrateduringactivities(T19),alongwith
activityclassification(T20). Intheemotiondomain,weclassifyPPGsignalsintomooddisturbance
levels(T16),valence(T17),andarousal(T18).
4.3 BASELINES
We benchmark PAPAGEI’s performance against competitive baselines. As open-source founda-
tion models designed for physiological signals, PAPAGEI is compared to recent time-series FMs:
Chronos (Ansari et al., 2024) and MOMENT (Goswami et al., 2024). To evaluate the merits of
ourSSLframework,wealsocomparePAPAGEIwithcommonSSLmethods(trainedfromscratch)
such as SimCLR (Chen et al., 2020), BYOL (Grill et al., 2020), and TF-C (Zhang et al., 2022).
Inaddition,toassessmodelgeneralizabilityonPPGsignals,wecompareagainstREGLE,amodel
pre-trainedonUKBiobank’sPPGsignals(Yunetal.,2024).Asasimplebaseline,weemployaran-
domforesttrainedonstatisticalfeaturesextractedfromthePPGsignal,includingmean,median,
maximum,minimum,andthe25th,50th,and75thpercentiles(”Stat. Features”). Thistask-specific
approachservesasabenchmarkforcomparisonwithmoreadvancedtechniques.
6

PublishedasaconferencepaperatICLR2025
Table3: Downstreamcomparisonagainstpre-trainedmodels. Featureextractionparametersare
indicatednexttoeachname. 95%CIsarereportedinsquarebracketsandthebestvalueisbolded.
|                         |     | REGLE(0.07M)    |     | Chronos(200M)      | Moment(385M)        | PAPAGEI-P(5M) | PAPAGEI-S(5M) |
| ----------------------- | --- | --------------- | --- | ------------------ | ------------------- | ------------- | ------------- |
| Classification-AUROC(↑) |     | (Yunetal.,2024) |     | (Ansarietal.,2024) | (Goswamietal.,2024) |               |               |
ICUAdmission 0.57[0.52-0.62] 0.73[0.68-0.80] 0.72[0.70-0.80] 0.73[0.67-0.78] 0.79[0.75-0.82]
Mortality 0.55[0.52-0.59] 0.68[0.65-0.71] 0.67[0.63-0.71] 0.67[0.63-0.71] 0.67[0.63-0.70]
Smoker 0.54[0.47-0.59] 0.62[0.57-0.67] 0.62[0.56-0.67] 0.64[0.58-0.69] 0.61[0.56-0.66]
Pregnancystage 0.64[0.57-0.63] 0.81[0.79-0.82] 0.76[0.74-0.78] 0.74[0.72-0.76] 0.78[0.75-0.80]
Hypertension 0.47[0.34-0.58] 0.57[0.43-0.71] 0.75[0.64-0.85] 0.74[0.55-0.90] 0.77[0.68-0.87]
SleepDisorderedBreathing 0.45[0.30-0.61] 0.58[0.35-0.82] 0.45[0.23-0.66] 0.54[0.23-0.66] 0.70[0.57-0.84]
MoodDisturbance 0.41[0.16-0.66] 0.43[0.21-0.68] 0.55[0.33-0.78] 0.53[0.27-0.78] 0.56[0.33-0.77]
Valence 0.55[0.52-0.57] 0.56[0.53-0.59] 0.57[0.54-0.59] 0.53[0.51-0.56] 0.56[0.54-0.59]
Arousal 0.51[0.52-0.58] 0.57[0.54-0.60] 0.56[0.53-0.58] 0.58[0.55-0.61] 0.55[0.52-0.57]
| Average |     | 0.52±0.06 |     | 0.62±0.10 | 0.63±0.09 | 0.63±0.08 | 0.67±0.09 |
| ------- | --- | --------- | --- | --------- | --------- | --------- | --------- |
Regression-MAE(↓)
Apnea/HypopneaIndex>3% 15.54[14.20-16.69] 14.06[13.05-15.16] 14.23[13.04-15.42] 13.85[12.43-15.49] 12.97[11.87-14.05]
Apnea/HypopneaIndex>4% 12.64[11.47-13.78] 11.57[10.51-12.72] 11.80[10.79-12.93] 11.24[9.71-12.87] 10.56[9.59-11.62]
GestationAge 7.28[7.16-7.39] 5.69[5.54-5.85] 6.24[6.10-6.37] 6.40[6.21-6.59] 6.05[5.91-6.17]
SystolicBP(VV) 15.88[13.67-18.36] 17.24[14.57-20.13] 14.71[12.38-17.29] 19.11[16.26-22.23] 14.65[12.50-16.78]
DiastolicBP(VV) 8.65[7.16-10.27] 10.53[8.91-12.19] 10.53[8.91-12.19] 10.87[9.10-12.98] 8.29[6.61-10.22]
SystolicBP(PPG-BP) 16.32[13.87-19.13] 16.91[13.31-19.34] 14.50[11.98-17.31] 13.60[10.65-16.51] 14.39[12.53-16.45]
DiastolicBP(PPG-BP) 9.30[7.94-10.87] 10.26[8.13-12.57] 9.53[8.28-10.96] 8.88[7.33-10.76] 8.71[7.18-10.01]
AverageHR 6.88[5.81-8.12] 8.51[7.05-10.07] 4.41[3.48-5.48] 3.47[2.74-4.32] 4.00[3.34-4.67]
HR 16.35[16.20-16.50] 9.65[9.50-9.79] 8.82[8.68-8.96] 10.92[10.80-11.04] 11.53[11.40-11.66]
AverageMAE(sMAPE) 12.09±3.83(15.23%) 11.60±3.60(14.20%) 10.43±3.46(13.82%) 10.92±4.25(14.09%) 10.12±3.47(13.34%)
4.4 LINEAREVALUATION
Initially, we split the in-domain and out-of-domain datasets into training, validation, and test sets
at80/10/10and60/20/20ratios. Thesplittingisperformedatthesubjectlevelensuringnooverlap
betweenindividualsacrossthesets. Themodelsareevaluatedbyextractingfeaturerepresentations
from resampled data (125Hz) and applying linear probing for each task. For binary classification
tasks, we employ a logistic regression model, with performance measured by the AUROC score.
Forregressiontasks,ridgeregressionisused,andperformanceisevaluatedbasedonthemeanab-
soluteerror(MAE).Regressiontasksareaggregatedusingthesymmetricmeanabsolutepercentage
error(sMAPE).Multi-classclassificationtasksaretrainedusingarandomforestmodel,withaccu-
racyastheevaluationmetric. Toensurerobustness,wecompute95%confidenceintervalsthrough
bootstrapping(500samplingrunswithreplacement).MoredetailsareprovidedintheAppendix§A.
5 RESULTS
5.1 OVERALLPERFORMANCE
Ingeneral,fromFigure3,weobservethat PAPAGEI ismoreaccurateacrossmanytasksindicated
by the larger AUROC area and smaller MAE area. Table 3 presents a more detailed comparison
betweenPAPAGEIandotherpre-trainedmodels.
| Forclassificationtasks, |     | PaPaGei-Sachievesthe |     |     |     |                |        |
| ----------------------- | --- | -------------------- | --- | --- | --- | -------------- | ------ |
|                         |     |                      |     |     |     | PaPaGei-S TF-C | Moment |
highestaverageAUROCof0.67,outperforming
|                  |            |           |              |              | 0.66    | 12.5         |              |
| ---------------- | ---------- | --------- | ------------ | ------------ | ------- | ------------ | ------------ |
| other models     | across     | several   | tasks,       | particularly | CORUA   | EAM          |              |
|                  |            |           |              |              | 0.64    | 11.5         |              |
|                  |            |           |              |              | 0.62    | 10.5         |              |
| in ICU Admission |            | (0.79),   | Hypertension | (0.77),      |         |              |              |
|                  |            |           |              |              | 0.60    | 9.5          |              |
| and Sleep        | Disordered | Breathing | (0.70).      | In re-       |         |              |              |
|                  |            |           |              |              | 25% 50% | 75% 100% 25% | 50% 75% 100% |
gression tasks, PaPaGei-S again demonstrates Downstream labelled data Downstream labelled data
| strong performance, |     | achieving | the | lowest aver- |                      |                 |           |
| ------------------- | --- | --------- | --- | ------------ | -------------------- | --------------- | --------- |
|                     |     |           |     |              | Figure 4: Downstream | data-efficiency | analysis. |
ageMAE(10.12),particularlyintasksrelatedto
Resultsareaveragedoverallbinaryclassification
| Apnea/Hypopnea |         | Index | and BP measurements. |             |                       |                |           |
| -------------- | ------- | ----- | -------------------- | ----------- | --------------------- | -------------- | --------- |
|                |         |       |                      |             | (left) and regression | tasks (right). | PAPAGEI-S |
| REGLE,         | a small | model | trained on           | a large PPG |                       |                |           |
performsbetterwithincreasedlabelavailability.
| dataset, generally |            | underperforms |             | compared | to  |     |     |
| ------------------ | ---------- | ------------- | ----------- | -------- | --- | --- | --- |
| other models,      | suggesting |               | its compact | size may |     |     |     |
limit learning complex patterns. Chronos obtains good performance in predicting mortality, preg-
nancystage,andsmoking,likelyduetotheirslowerrateofchangeandreducedrelianceongranular
PPG-specific features. General-purpose models suffice for these high-level outcomes. However,
tasksrequiringfinerPPG-specificgranularity,suchasheartrateprediction,bloodpressureestima-
tion, or sleep apnea, benefit from PAPAGEI’s specialized feature extraction. Notably, PAPAGEI-S
consistentlyoutperforms PAPAGEI-P,highlightingtheadvantagesofsignalmorphologyobjectives
inenhancingpredictiveaccuracy.
7

PublishedasaconferencepaperatICLR2025
Table4: DownstreamcomparisonagainstbaselineandSSLmethods. Featureextractionparam-
etersareindicatednexttoeachname. 95%CIsarereportedinsquarebracketsandthebestvalueis
bolded. ImplementationdetailsareinAppendix§A.
Stat.Features SimCLR(5M) BYOL(5M) TF-C(10M) PAPAGEI-P(5M) PAPAGEI-S(5M)
Classification-AUROC(↑) (Chenetal.,2020) (Grilletal.,2020) (Zhangetal.,2022)
ICUAdmission 0.71[0.65-0.78] 0.75[0.72-0.79] 0.78[0.73-0.81] 0.71[0.67-0.75] 0.73[0.67-0.78] 0.79[0.75-0.82]
Mortality 0.57[0.54-0.61] 0.67[0.63-0.70] 0.67[0.64-0.71] 0.67[0.63-0.70] 0.67[0.63-0.71] 0.67[0.63-0.70]
Smoker 0.63[0.58-0.67] 0.62[0.57-0.68] 0.62[0.57-0.68] 0.61[0.56-0.67] 0.64[0.58-0.69] 0.61[0.56-0.66]
Pregnancystage 0.64[0.62-0.67] 0.74[0.72-0.75] 0.62[0.57-0.68] 0.74[0.72-0.76] 0.74[0.72-0.76] 0.78[0.75-0.80]
Hypertension 0.66[0.47-0.83] 0.75[0.64-0.86] 0.74[0.64-0.84] 0.76[0.63-0.86] 0.74[0.55-0.90] 0.77[0.68-0.87]
SDB 0.32[0.14-0.55] 0.61[0.46-0.76] 0.59[0.42-0.74] 0.58[0.44-0.73] 0.54[0.23-0.66] 0.70[0.57-0.84]
MoodDisturbance 0.54[0.31-0.77] 0.32[0.12-0.55] 0.46[0.21-0.71] 0.59[0.33-0.84] 0.53[0.27-0.78] 0.56[0.33-0.77]
Valence 0.52[0.49-0.55] 0.52[0.49-0.55] 0.53[0.50-0.56] 0.57[0.54-0.59] 0.53[0.51-0.56] 0.56[0.54-0.59]
Arousal 0.55[0.53-0.58] 0.55[0.52-0.58] 0.54[0.30-0.78] 0.55[0.52-0.58] 0.58[0.55-0.61] 0.55[0.52-0.57]
Average 0.57±0.11 0.61±0.13 0.62±0.10 0.64±0.07 0.63±0.08 0.67±0.09
Regression-MAE(↓)
Apnea/HypopneaIndex>3% 15.31[13.63-17.14] 14.17[13.04-15.38] 14.26[13.10-15.57] 15.10[13.84-16.40] 13.85[12.43-15.49] 12.97[11.87-14.05]
Apnea/HypopneaIndex>4% 12.52[10.92-14.14] 11.76[10.65-12.89] 11.88[10.71-13.05] 12.41[11.33-13.49] 11.24[9.71-12.87] 10.56[9.59-11.62]
GestationAge 7.15[6.99-7.34] 6.28[6.21-6.49] 6.24[6.09-6.38] 6.35[6.21-6.49] 6.40[6.21-6.59] 6.05[5.91-6.17]
SystolicBP(VV) 15.76[13.67-18.36] 16.18[13.73-18.85] 15.01[12.32-17.80] 15.70[13.23-18.13] 19.11[16.26-22.23] 14.65[12.50-16.78]
DiastolicBP(VV) 9.75[7.16-11.27] 9.15[7.65-10.65] 8.91[7.48-10.43] 9.15[7.65-10.65] 10.87[9.10-12.98] 8.29[6.61-10.22]
SystolicBP(PPG-BP) 15.50[11.68-20.25] 14.38[11.80-16.88] 14.99[13.03-17.38] 14.45[12.20-17.00] 13.60[10.65-16.51] 14.39[12.53-16.45]
DiastolicBP(PPG-BP) 9.35[7.44-11.66] 9.01[7.90-10.60] 9.16[8.00-10.50] 9.20[7.90-10.60] 8.88[7.33-10.76] 8.71[7.18-10.01]
AverageHR 7.01[5.48-8.89] 4.65[3.99-5.39] 4.78[3.88-5.93] 3.58[2.90-4.21] 3.47[2.74-4.32] 4.00[3.34-4.67]
HR 13.07[12.90-13.23] 11.59[11.46-11.72] 12.80[12.66-12.94] 9.99[9.86-10.12] 10.92[10.80-11.04] 11.53[11.40-11.66]
AverageMAE(sMAPE) 11.60±3.41(15.12%) 10.79±3.63(13.91%) 10.89±3.58(14.05%) 10.65±3.88(14.07%) 10.92±4.25(14.09%) 10.12±3.47(13.34%)
Table4presentsacomparisonagainstthreeSSLmethodsandabaselinemodeltrainedonstatistical
features.Inclassificationtasks,PaPaGei-SagainshowsthehighestaverageAUROC,outperforming
allothers. SimCLR,BYOL,andTF-Cgenerallyoutperformthestatisticalfeaturebaselinebutfall
short of PaPaGei-S’s performance. TF-C shows competitive results in some tasks, achieving the
highestAUROCforMoodDisturbanceandValence.Forregressiontasks,PaPaGei-Sagainachieves
thelowestaverageMAE.SimCLR,BYOL,andTF-Cshowmixedresults,aseachexcelsindifferent
tasks.SimCLRcomessecondinestimatingAvgHR,whileBYOLdoessoinSystolicBP(VV).The
statisticalfeaturebaselinegenerallyunderperformscomparedtotheadvancedmethodsacrossmost
tasks. PaPaGei-P, while not consistently outperforming PaPaGei-S, shows strong results that are
often competitive with or better than other contrastive learning methods. Overall, both PaPaGei
variantsofferrobustperformanceacrossawiderangeoftasks.
5.2 ABLATIONSTUDIES
Pre-training data ablation. We evaluate PAPAGEI-S using different pre-training data
0.8
0.6
V M M-III
V
+
M
+
M-III
+
M-IIIAll
V M
CORUA 0*.6*2 0*.6*2 0*.6*1 0*.6*4 0.64 0*.6*4 0.67 15
10
5
V M M-III
V
+
M
+
M-III
+
M-IIIAll
V M
EAM
combinations. As shown in Fig-
ure 5, performance on downstream
tasks improves with more upstream 12*.*29 11 * . * 60 12*.*01 11*.*61 11*.*69 11*.*36 10.13
data, with the best results achieved
when using all three datasets. No-
tably, MESA outperforms the oth-
ers despite having the fewest par-
ticipants but the highest number of
segments. This supports findings Figure 5: Ablation on pre-training data. Average perfor-
from language models (Dubey et al., manceacrosstasksformodelstrainedon: V(VitalDB),M
2024)andwearablesensingresearch (MESA), and M-III (MIMIC-III). The mean value is dis-
(Narayanswamy et al., 2024), indi- played above the plots. The Wilcoxon signed rank test is
cating that the volume of segments appliedtoevaluatesignificancebetweentheAlldatasetand
or hours contributes more to perfor- therest(∗∗:p<0.05and∗:0.05≤p<0.10).
mancethanthenumberofusers.
PAPAGEI-S component ablation. We assess the impact of PAPAGEI-S components. Figure 6
shows that the full model (0.67, 10.12) consistently outperforms individual components in both
meanandmedianmetrics. Onaverage,sVRI(0.64,10.35)outperformsthecombinationsofsVRI+
SQI(0.62,10.80)andsVRI+IPA(0.64,10.73). OurresultsindicatethatcombiningSQIandIPA
yieldsgreaterbenefitscomparedtotheirindividualcontributions.
Downstream data-efficiency analysis. For limited-data scenarios, we assess the performance of
downstreamlinearprobingacrossvaryinglevelsoflabeleddataavailability. Wecomparetothesec-
ondbest-performingbaselinesfromTables3&4,namelyTF-CandMoment. AsshowninFigure
4, the classification performance of PAPAGEI-S steadily improves as more labeled data becomes
8

PublishedasaconferencepaperatICLR2025
available. WhileTF-CandMomentalsoshowperformancegainsbetween25%and100%labeled
data,theirimprovementsarelessconsistentandsmallerthan PAPAGEI-S.Inregressiontasks, PA-
PAGEI-S achieves the lowest MAE at both 25% and 100% data availability, consistently reducing
errors. Atthemiddlebreakpoints,theresultsaremixedwithTF-CandMomentbeingcompetitive.
**
|     |     | *   |     |     | **  |              |     |     |     | Rank 1 |
| --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | ------ |
|     |     | **  | 20  |     | **  | PaPaGei-S-5M |     |     |     | Rank 2 |
|     |     | **  |     |     |     | **           |     |     |     |        |
0.64 0.62 0.64 0.67 10.35 10.80 10.73 10.12 PaPaGei-S-35M Rank 3
15
| CORUA 0.7 |     |     | EAM |     |     | PaPaGei-S-139M |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
10
0.6 UCI ytilatroM rekomS ycnangerP noisnetrepyH BDS dooM ecnelaV lasuorA %3 > IHA %4 > IHA noitatseG *PB .syS *PB .aiD PB .syS PB .aiD RH .gvA RH
| 0.5  |                      |     |      | 5                         |     |      |     |     |     |     |
| ---- | -------------------- | --- | ---- | ------------------------- | --- | ---- | --- | --- | --- | --- |
| 0.4  |                      |     |      | 0                         |     |      |     |     |     |     |
| sVRI | sVRI + SQIsVRI + IPA |     | Full | sVRI sVRI + SQIsVRI + IPA |     | Full |     |     |     |     |
|      | PaPaGei Components   |     |      | PaPaGei Components        |     |      |     |     |     |     |
|      | (a)                  |     |      |                           | (b) |      |     | (c) |     |     |
Figure6: PAPAGEI-Scomponentablationstudy(a,b)andscalinganalysis(c). (Left)Theboxplot
showstheperformanceofPAPAGEI-Scomponentsacrossalltasks. TheWilcoxonsignedranktest
is applied to evaluate pair-wise significance (∗∗ : p < 0.05 and ∗ : 0.05 ≤ p < 0.10). (Right)
Heatmap ranks of PAPAGEI-S models with 5M, 35M, and 139M parameters (rank 1 denotes the
| bestperformance). |     | DetailedresultsinTable13. |     |     |     |     |     |     |     |     |
| ----------------- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Model size and scaling analysis. We investigated the impact of model size on performance by
training PAPAGEI-S-35M and PAPAGEI-S-139M with 35M and 139M parameters, respectively.
| Both models |          | share the | same        | number     | of       | layers, but |     |     |        |     |
| ----------- | -------- | --------- | ----------- | ---------- | -------- | ----------- | --- | --- | ------ | --- |
| the 35M     | model    | uses      | a 32-filter | size       | while    | the 139M    |     |     |        |     |
| model       | uses 64. | As shown  |             | in 6c, the | smallest | model       | 0.8 |     | SimCLR |     |
(5M parameters) consistently outperformed larger ytisneD 0.6 BYOL
TF-C
0.4
| models | on all | but one | task. | This | suggests | the 5M |     |     | PaPaGei-S |     |
| ------ | ------ | ------- | ----- | ---- | -------- | ------ | --- | --- | --------- | --- |
0.2
| model | is better | suited | for | our pre-training |     | datasets, |     |     |     |     |
| ----- | --------- | ------ | --- | ---------------- | --- | --------- | --- | --- | --- | --- |
0.0
aligning with prior findings on the proportionality 0 2 4 6 8 10 12
Pair-wise distances across participants in SDB
| between | data | and model | size | (Narayanswamy |     | et al., |     |     |     |     |
| ------- | ---- | --------- | ---- | ------------- | --- | ------- | --- | --- | --- | --- |
2024). Whilethe139Mmodelsurpassedthe35M,it Figure7:Pair-wiseinter-participantembed-
| stilllaggedbehindthe5M,indicatingthatwidermod- |         |             |     |                   |     | dingdistancesforSDB. |     |     |     |     |
| ---------------------------------------------- | ------- | ----------- | --- | ----------------- | --- | -------------------- | --- | --- | --- | --- |
| els may                                        | improve | performance |     | in classification |     | tasks,               |     |     |     |     |
likely due to the contrastive learning objective. Nevertheless, our scaling analysis shows a non-
monotonictrend,indicatingotherfactorsstronglyinfluenceperformance.
EffectofDemographics. Weevaluatetheeffectofdemographics(age,sex)andPPG-specificfea-
tures(sVRI,IPA,SQI)inAppendix§E.Indemographicsprediction(Table16),PAPAGEI-Sachieves
7.78MAEinageregression, 0.85accuracyinageclassification, and0.79accuracyinsexclassifi-
cation. While our results trail larger closed studies (Abbaspourazad et al., 2023) by 2.18, 0.05,
and0.13forsegment-levelSSL,andby5.59,0.12,and0.25forpatient-levelSSL,theymarkanad-
vancementinopen-sourceefforts.Thesefindingsindicatethatpatient-levelpositivepairselectionin
SSLbettercapturesdemographic-relatedfeaturesfordownstreamprediction.Moreover,thereduced
performanceofPAPAGEI-Scanbeattributedtoevaluationsconductedondiversedevicesetups,as
opposedtoasingledeviceconfiguration. Ourablationstudy(Table15)showsthatPAPAGEI-Sout-
performsthedemo+PPGin14outof18tasks,particularlyintaskswithreal-timedependencesuch
as heart rate estimation. Importantly, including demographics in addition to PAPAGEI-S creates a
stronger model. These findings emphasize that demographic features complement rather than
compete with PAPAGEI-S, showcasing the potential of integrating PAPAGEI’s advanced feature
extractioncapabilitieswithdemographiccontexttoimprovetaskoutcomes.
5.3 CASESTUDIES
Inter-participantembeddings. Figure7showsthedistributionofpair-wiseembeddingdistances
acrossparticipantsintheSDBdataset(Kiyassehetal.,2021). SimCLRandBYOLexhibitsharper
peaksatlowerdistances, indicatingthatparticipantsaremorecloselyclusteredwithintheembed-
ding space. This could be interpreted as a mild form of mode collapse, where the model does not
fully capture the individual differences between participants. TF-C demonstrates a more balanced
distribution,withbothlargeandsmallpeaks,suggestingitcapturesbothsimilaritiesandsomevari-
ationbetweenparticipants. Incontrast, PAPAGEI-Sprovidesthewidestdispersionofembeddings,
9

PublishedasaconferencepaperatICLR2025
|     | %3 > IHA detciderP | Chronos |     | SimCLR |     |            | PaPaGei-S |     |     |     |
| --- | ------------------ | ------- | --- | ------ | --- | ---------- | --------- | --- | --- | --- |
|     | 100 m=0.18         |         | 100 | m=0.19 |     | 100 m=0.28 |           |     |     |     |
R2=0.18
|     | 75  |     | 75  | R2=0.16 |     | 75 R2=0.29 |     |      |     | True AHI > 3% |
| --- | --- | --- | --- | ------- | --- | ---------- | --- | ---- | --- | ------------- |
|     |     |     |     |         |     |            |     | 0.04 |     | Chronos       |
ytisneD
|     | 50  |     | 50  |     |     | 50  |     |      |     | SimCLR    |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --------- |
|     |     |     |     |     |     |     |     | 0.02 |     | PaPaGei-S |
|     | 25  |     | 25  |     |     | 25  |     |      |     |           |
0
|     |               |     | 0   |               |        | 0             |        | 0.00 |             |         |
| --- | ------------- | --- | --- | ------------- | ------ | ------------- | ------ | ---- | ----------- | ------- |
|     | 0             | 50  | 100 | 0             | 50 100 | 0             | 50 100 | 20 0 | 20 40 60 80 | 100 120 |
|     | True AHI > 3% |     |     | True AHI > 3% |        | True AHI > 3% |        |      | AHI > 3%    |         |
Figure8: Regressionplotsandpredictiondistributionofdifferentmodelscomparedtogroundtruth
| forAHI>3%. |     | R2isthecoefficientofdeterminationandmisthecorrelationslope. |     |     |     |     |     |     |     |     |
| ---------- | --- | ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
highlightingitsabilitytocaptureabroaderrangeoffeaturesthatmaybevaluablefordistinguishing
betweenparticipants’medicalconditions.
Regressionpredictions. FromFigure8,comparedtothepre-trainedandSSLbaseline,PAPAGEI-
S demonstrates steeper slopes (m) and higher R2 values, reflecting a stronger alignment between
predictionsandtruevalues. Additionally,thepredictiondistributionforAHIindicatesthatSimCLR
andChronostendtoregressmoretowardthemean,whilePAPAGEI-Sachievesawiderdistribution
base,highlightingitscapacitytocapturelefttailbetter. AdditionalplotsareshowninAppendix§F.
Skintoneanalysis. WeexamineBPestimationperformanceacrossskintonesbecauseitiscrucial
forpracticaluse(Bentetal.,2020). AsshowninFigure9(MoredetailsinFigure26),PAPAGEI-S
achieves the best BP estimation across light tones. Across dark tones, we notice that BYOL and
REGLE obtain the lowest MAE for Systolic BP and Diastolic BP. However, identifying a single
modelthatperformsbestacrossallskintonesremainschallenging. While PAPAGEI-Sobtainsthe
bestoverallperformance,additionalworkisnecessarytoimproverobustnessondarkerskintones.
| 6   | DISCUSSION |           | &            | CONCLUSION     |             |     |            |       |             |           |
| --- | ---------- | --------- | ------------ | -------------- | ----------- | --- | ---------- | ----- | ----------- | --------- |
| Our | results    | show      | that PAPAGEI |                | outperforms |     | baselines  |       |             |           |
| in  | at least   | 14 tasks, | with         | classification |             | and | regression |       |             |           |
|     |            |           |              |                |             |     |            | REGLE | Moment BYOL | PaPaGei-P |
improvements of 4.7%-6.3% and 2.9%-4.9%, respec- Chronos SimCLR TF-C PaPaGei-S
tively. PAPAGEI-Sexcelledincardiovasculartaskslike Systolic BP (VV)
| BP, | Hypertension, |     | and | HR, which | can | be attributed | to  |     |     |     |
| --- | ------------- | --- | --- | --------- | --- | ------------- | --- | --- | --- | --- |
20
| the | sVRI | and IPA | objectives, |     | and PAPAGEI-P |     | outper- |     |     |     |
| --- | ---- | ------- | ----------- | --- | ------------- | --- | ------- | --- | --- | --- |
EAM
| formedbaselineslikeMoment,excellingintaskssuchas |       |              |           |          |            |           |       | 10  |     |     |
| ------------------------------------------------ | ----- | ------------ | --------- | -------- | ---------- | --------- | ----- | --- | --- | --- |
| Smoking                                          |       | and Arousal. |           | Ablation | studies    | confirmed | that  |     |     |     |
| the                                              | model | with         | all three | SSL      | objectives | performs  | best, | 0   |     |     |
withsVRIhighlightedasakeycomponentandIPAand Diastolic BP (VV)
| SQIprovidingpositiveknowledgetransferinmulti-task |     |     |     |     |     |     |     | 12  |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
EAM 9
| setups. | To  | assess | performance |     | under | class imbalance, |     |     |     |     |
| ------- | --- | ------ | ----------- | --- | ----- | ---------------- | --- | --- | --- | --- |
6
| we  | examined | the | F1-score. | PaPaGei | achieves |     | the high- |     |     |     |
| --- | -------- | --- | --------- | ------- | -------- | --- | --------- | --- | --- | --- |
3
| est | F1 in | 6 out of | 9 classification |     | tasks, | demonstrating |     |     |     |     |
| --- | ----- | -------- | ---------------- | --- | ------ | ------------- | --- | --- | --- | --- |
0
itseffectivenessinhandlingdataimbalance. Forregres- Light Tones (<=3) Dark Tones (>3)
sion,PaPaGei-SachievesthehighestR2 in7tasks(Ap- Fitzpatrick Skin Tone
pendix§D),reflectingbetteralignmentwiththetruedis- Figure 9: Skin tone analysis for Blood
tribution. Theseresultshighlighttherobustnessandver- Pressureestimation(VVdataset)
| satilityofPaPaGei-Sacrossclassificationandregression |         |     |         |       |                    |     |       |     | .   |     |
| ---------------------------------------------------- | ------- | --- | ------- | ----- | ------------------ | --- | ----- | --- | --- | --- |
| tasks.                                               | PAPAGEI |     | is both | data- | and size-efficient |     | (5M), |     |     |     |
making it ideal for medical applications where large models (200M+) are impractical due to on-
devicelimitationsordataprivacyconcernswithcloudmodelinference.WhilecombiningPAPAGEI-
PandPAPAGEI-Sobjectivesintoonemodelmightseemintuitive,itisimpracticalbecauseitwould
constrainpositivepairsonbothsVRIandthenumberofparticipants,resultingintoomanyunique
labelswithlimitedsamplesperlabel. Ourcasestudiesalsoshowedthat PAPAGEI-Scapturedper-
sonalmedicalinformationduetowell-dispersedembeddings,comparedtobaselines. Futurework
shouldfocusondiversifyingtrainingdata,investigatingsamplingrateeffects,andexploringmulti-
modalapproachesoralternativearchitectures. Additionally,asextractingPPGfeaturesfordifferent
morphologies is non-trivial, future work benefit from systematic evaluation of PPG features and
modeling. Inconclusion, PAPAGEI representsasignificantadvancementinfoundationmodelsfor
analyzing PPG signals in resource-constrained medical environments, with its open-source nature
encouragingfurtherresearchanddevelopmentinhealthcareapplications.
10

PublishedasaconferencepaperatICLR2025
REPRODUCIBILITY STATEMENT
Models,data,andcodearepubliclyavailableforreproducibilityandfutureresearch.Weexclusively
utilizepubliclyaccessibledatasets,whichcanberequestedordownloadedfromtherespectivestudy
group websites, allowing others to easily obtain the data for their own analyses. In §4 and Ap-
pendix §B, we provide comprehensive descriptions of the datasets, ground-truth annotations, and
data pre-processing methods used in our experiments, ensuring transparency in our data handling
procedures. Thecodetorunourmodelispublishedwithuser-friendlyexamples. Wehaveprovided
adetailedoverviewofthemodelarchitectureanditshyperparametersin§3,§4.1,andAppendix§A.
Thus,ourworkisdesignedtobereproducible,enablingfutureresearchtobuilduponourfindings.
ETHICS STATEMENT
Ourresearchon PAPAGEI,utilizingpubliclyavailablePPGdatasets,adherestodataprivacyregu-
lationsandpromotestransparencythroughopen-sourcereleases. Weacknowledgepotentialbiases
in the training data and have evaluated performance across diverse datasets, particularly regarding
skin tone variations. While PaPaGei offers significant potential for improving non-invasive health
monitoring,werecognizetheneedtoaddresspotentialmisuse(Perez-Pozueloetal.,2021). Exam-
plesofmisusecouldincludeunauthorizedhealthmonitoring,discriminatorypracticesininsurance
oremployment,unfaircreditscoring,orexploitingpersonalhealthdatafortargetedmarketing. We
stronglyadvocateresponsibleusesolelyforbeneficialhealthcareapplications. Ourstudyfollowed
established research ethics guidelines, and we declare no conflicts of interest. We encourage on-
goinginterdisciplinarydialoguetoaddresspotentialrisksandensureresponsibledevelopmentand
deploymentofsuchtechnologies,recognizingthebroadersocietalimpactsofAIinhealthcare. We
remaincommittedtoethicalAIadvancementandwelcomefurtherdiscussiononthecriticalissues,
includingthedevelopmentofgovernanceframeworkstopreventmisuseandprotectdataprivacy.
REFERENCES
SalarAbbaspourazad,OussamaElachqar,AndrewCMiller,SabaEmrani,UdhyakumarNallasamy,
and Ian Shapiro. Large-scale training of foundation models for wearable biosignals. arXiv
preprintarXiv:2312.05409,2023.
Amir Hosein Afandizadeh Zargari, Seyed Amir Hossein Aqajari, Hadi Khodabandeh, Amir Rah-
mani,andFadiKurdahi. Anaccuratenon-accelerometer-basedppgmotionartifactremovaltech-
niqueusingcyclegan. ACMTransactionsonComputingforHealthcare,4(1):1–14,2023.
AbdulFatirAnsari,LorenzoStella,CanerTurkmen,XiyuanZhang,PedroMercado,HuibinShen,
OleksandrShchur,SyamaSundarRangapuram,SebastianPinedaArango,ShubhamKapoor,etal.
Chronos: Learningthelanguageoftimeseries. arXivpreprintarXiv:2403.07815,2024.
ArrozaqAve, HamdanFauzan, SRhandyAdhitya, andHasballahZakaria. Earlydetectionofcar-
diovasculardiseasewithphotoplethysmogram(ppg)sensor. In2015internationalconferenceon
electricalengineeringandinformatics(ICEEI),pp.676–681.IEEE,2015.
AnastasiyaBelyaeva,JustinCosentino,FarhadHormozdiari,KrishEswaran,ShravyaShetty,Greg
Corrado,AndrewCarroll,CoryYMcLean,andNicholasAFurlotte. Multimodalllmsforhealth
groundedinindividual-specificdata. InWorkshoponMachineLearningforMultimodalHealth-
careData,pp.86–102.Springer,2023.
BrinnaeBent,BenjaminAGoldstein,WarrenAKibbe,andJessilynPDunn. Investigatingsources
ofinaccuracyinwearableopticalheartratesensors. NPJdigitalmedicine,3(1):18,2020.
BioBSS Documentation. Biobss: Biosignal processing toolbox. https://biobss.
readthedocs.io/en/latest/,2023. Accessed: 2024-09-10.
Alexandra Bouariu, Anca Maria Panaitescu, and Kypros H Nicolaides. First trimester prediction
of adverse pregnancy outcomes—identifying pregnancies at risk from as early as 11–13 weeks.
Medicina,58(3):332,2022.
11

PublishedasaconferencepaperatICLR2025
Margaret M Bradley and Peter J Lang. Measuring emotion: the self-assessment manikin and the
semantic differential. Journal of behavior therapy and experimental psychiatry, 25(1):49–59,
1994.
PeterHCharlton,JohnAllen,RaquelBailo´n,StephanieBaker,JoachimABehar,FeiChen,GariD
Clifford,DavidAClifton,HarryJDavies,ChengDing,etal. The2023wearablephotoplethys-
mographyroadmap. Physiologicalmeasurement,44(11):111001,2023.
Hugh Chen, Scott M Lundberg, Gabriel Erion, Jerry H Kim, and Su-In Lee. Forecasting adverse
surgical events using self-supervised transfer learning for physiological signals. NPJ Digital
Medicine,4(1):167,2021.
TingChen,SimonKornblith,MohammadNorouzi,andGeoffreyHinton. Asimpleframeworkfor
contrastivelearningofvisualrepresentations. Internationalconferenceonmachinelearning,pp.
1597–1607,2020.
Xiaoli Chen, Rui Wang, Phyllis Zee, Pamela L Lutsey, Sogol Javaheri, Carmela Alca´ntara, Chan-
draLJackson, MichelleAWilliams, andSusanRedline. Racial/ethnicdifferencesinsleepdis-
turbances: themulti-ethnicstudyofatherosclerosis(mesa). Sleep,38(6):877–888,2015.
Joseph Y Cheng, Hanlin Goh, Kaan Dogrusoz, Oncel Tuzel, and Erdrin Azemi. Subject-aware
contrastivelearningforbiosignals. arXivpreprintarXiv:2007.04871,2020.
Wei-ShengChung,Pei-TsengKung,Hui-YunChang,andWen-ChenTsai. Demographicsandmed-
icaldisordersassociatedwithsmoking: apopulation-basedstudy. BMCPublicHealth, 20:1–8,
2020.
Casey Crump, Jan Sundquist, Mary Ann McLaughlin, Siobhan M Dolan, Usha Govindarajulu,
WeivaSieh,andKristinaSundquist. Adversepregnancyoutcomesandlongtermriskofischemic
heartdiseaseinmothers: nationalcohortandco-siblingstudy. bmj,380,2023.
JanezDemsˇar. Statisticalcomparisonsofclassifiersovermultipledatasets. TheJournalofMachine
learningresearch,7:1–30,2006.
Cheng Ding, Zhicheng Guo, Zhaoliang Chen, Randall J Lee, Cynthia Rudin, and Xiao Hu.
Siamquality:aconvnet-basedfoundationmodelforphotoplethysmographysignals.Physiological
Measurement,45(8):085004,2024.
AbhimanyuDubey,AbhinavJauhri,AbhinavPandey,AbhishekKadian,AhmadAl-Dahle,Aiesha
Letman,AkhilMathur,AlanSchelten,AmyYang,AngelaFan,etal. Thellama3herdofmodels.
arXivpreprintarXiv:2407.21783,2024.
MohamedElgendi. Optimalsignalqualityindexforphotoplethysmogramsignals. Bioengineering,
3(4):21,2016.
FrancescaLFacco,CoretteBParker,UmaMReddy,RobertMSilver,JudetteMLouis,RobertC
Basner, Judith H Chung, Frank P Schubert, Grace W Pien, Susan Redline, et al. Numom2b
sleep-disordered breathing study: objectives and methods. American journal of obstetrics and
gynecology,212(4):542–e1,2015.
Mohammad Feli, Iman Azimi, Fatemeh Sarhaddi, Zahra Sharifi-Heris, Hannakaisa Niela-Vilen,
Pasi Liljeberg, Anna Axelin, and Amir M Rahmani. Preterm birth risk stratification through
longitudinalheartrateandhrvmonitoringindailylife. 2024.
Zhilin Gao, Xingran Cui, Wang Wan, Wenming Zheng, and Zhongze Gu. Ecsmp: A dataset on
emotion, cognition, sleep, and multi-model physiological signals. Data in Brief, 39:107660,
2021.
Ainara Garde, Parastoo Dehkordi, Walter Karlen, David Wensley, J Mark Ansermino, and Guy A
Dumont. Development of a screening tool for sleep disordered breathing in children using the
phoneoximeter™. PloSone,9(11):e112959,2014.
12

PublishedasaconferencepaperatICLR2025
Mononito Goswami, Konrad Szafer, Arjun Choudhry, Yifu Cai, Shuo Li, and Artur Dubrawski.
Moment: A family of open time-series foundation models. arXiv preprint arXiv:2402.03885,
2024.
Jean-Bastien Grill, Florian Strub, Florent Altche´, Corentin Tallec, Pierre H Richemond, Elena
Buchatskaya,CarlDoersch,BernardoAvilaPires,ZhaohanDanielGuo,MohammadGheshlaghi
Azar, etal. Bootstrapyourownlatent-anewapproachtoself-supervisedlearning. Advancesin
neuralinformationprocessingsystems,33:21271–21284,2020.
NateGruver,MarcFinzi,ShikaiQiu,andAndrewGWilson. Largelanguagemodelsarezero-shot
timeseriesforecasters. AdvancesinNeuralInformationProcessingSystems,36,2024.
Serj Haddad, Assim Boukhayma, and Antonino Caizzone. Continuous ppg-based blood pressure
monitoringusingmulti-linearregression. IEEEjournalofbiomedicalandhealthinformatics,26
(5):2096–2105,2021.
Kaiming He, Haoqi Fan, Yuxin Wu, Saining Xie, and Ross Girshick. Momentum contrast for
unsupervised visual representation learning. In Proceedings of the IEEE/CVF conference on
computervisionandpatternrecognition,pp.9729–9738,2020.
Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr Dolla´r, and Ross Girshick. Masked
autoencodersarescalablevisionlearners. ProceedingsoftheIEEE/CVFconferenceoncomputer
visionandpatternrecognition,pp.16000–16009,2022.
Alistair EW Johnson, Tom J Pollard, Lu Shen, Li-wei H Lehman, Mengling Feng, Mohammad
Ghassemi,BenjaminMoody,PeterSzolovits,LeoAnthonyCeli,andRogerGMark. Mimic-iii,
afreelyaccessiblecriticalcaredatabase. Scientificdata,3(1):1–9,2016.
Dani Kiyasseh, Girmaw Abebe Tadesse, Louise Thwaites, Tingting Zhu, David Clifton, et al.
Plethaugment:Gan-basedppgaugmentationformedicaldiagnosisinlow-resourcesettings.IEEE
journalofbiomedicalandhealthinformatics,24(11):3226–3235,2020.
DaniKiyasseh,TingtingZhu,andDavidAClifton. Clocs: Contrastivelearningofcardiacsignals
across space, time, and patients. In International Conference on Machine Learning, pp. 5606–
5615.PMLR,2021.
BojanaKoteska,AnaMadevskaBodanova,HristinaMitrova,MarijaSidorenko,andFedorLehocki.
Adeeplearningapproachtoestimatespo2fromppgsignals. InProceedingsofthe9thInterna-
tionalConferenceonBioinformaticsResearchandApplications,pp.142–148,2022.
JieweiLai,HuixinTan,JinliangWang,LeiJi,JunGuo,BaoshiHan,YajunShi,QianjinFeng,and
WeiYang. Practicalintelligentdiagnosticalgorithmforwearable12-leadecgviaself-supervised
learningonlarge-scaledataset. NatureCommunications,14(1):3741,2023.
DenisGLapitan,DmitryARogatkin,ElizavetaAMolchanova,andAndreyPTarasov. Estimation
ofphasedistortionsofthephotoplethysmographicsignalindigitaliirfiltering. ScientificReports,
14(1):6546,2024.
Hyung-ChulLee,YoonsangPark,SooBinYoon,SeongMiYang,DongnyeokPark,andChul-Woo
Jung. Vitaldb,ahigh-fidelitymulti-parametervitalsignsdatabaseinsurgicalpatients. Scientific
Data,9(1):279,2022.
Yongbo Liang, Zhencheng Chen, Guiyong Liu, and Mohamed Elgendi. A new, short-recorded
photoplethysmogram dataset for blood pressure monitoring in china. Scientific data, 5(1):1–7,
2018a.
Yongbo Liang, Zhencheng Chen, Rabab Ward, and Mohamed Elgendi. Hypertension assessment
using photoplethysmography: a risk stratification approach. Journal of clinical medicine, 8(1):
12,2018b.
YongboLiang, MohamedElgendi, ZhenchengChen, andRababWard. Anoptimalfilterforshort
photoplethysmogramsignals. Scientificdata,5(1):1–12,2018c.
13

PublishedasaconferencepaperatICLR2025
YongqiangLyu,XiaominLuo,JunZhou,ChunYu,CongcongMiao,TongWang,YuanchunShi,and
Ken-ichi Kameyama. Measuring photoplethysmogram-based stress-induced vascular response
indextoassesscognitiveloadandstress. InProceedingsofthe33rdannualACMconferenceon
humanfactorsincomputingsystems,pp.857–866,2015.
KadenMcKeen,LauraOliva,SameerMasood,AugustinToma,BarryRubin,andBoWang.Ecg-fm:
Anopenelectrocardiogramfoundationmodel. arXivpreprintarXiv:2408.05178,2024.
Benjamin Moody, George Moody, Mauricio Villarroel, Gari D. Clifford, and Ikaro Silva. Mimic-
iii waveform database matched subset (version 1.0), 2020. URL https://doi.org/10.
13026/c2294b.
SeungwhanMoon,AndreaMadotto,ZhaojiangLin,TusharNagarajan,MattSmith,ShashankJain,
Chun-Fu Yeh, Prakash Murugesan, Peyman Heidari, Yue Liu, et al. Anymal: An efficient and
scalableany-modalityaugmentedlanguagemodel. arXivpreprintarXiv:2309.16058,2023.
GirishNarayanswamy,XinLiu,KumarAyush,YuzheYang,XuhaiXu,ShunLiao,JakeGarrison,
ShyamTailor,JakeSunshine,YunLiu,etal. Scalingwearablefoundationmodels. arXivpreprint
arXiv:2410.13638,2024.
AaronvandenOord,YazheLi,andOriolVinyals. Representationlearningwithcontrastivepredic-
tivecoding. arXivpreprintarXiv:1807.03748,2018.
ChristinaOrphanidou. Qualityassessmentforthephotoplethysmogram(ppg). SignalQualityAs-
sessmentinPhysiologicalMonitoring: StateoftheArtandPracticalConsiderations,pp.41–63,
2018.
Nisha I Parikh, Juan M Gonzalez, Cheryl AM Anderson, Suzanne E Judd, Kathryn M Rexrode,
MarkAHlatky,EricaPGunderson,JenniferJStuart,DhananjayVaidya,AmericanHeartAsso-
ciationCouncilonEpidemiology,ThrombosisPrevention;CouncilonArteriosclerosis,Vascular
Biology; Council on Cardiovascular, Stroke Nursing;, and the Stroke Council. Adverse preg-
nancyoutcomesandcardiovasculardiseaserisk: uniqueopportunitiesforcardiovasculardisease
preventioninwomen:ascientificstatementfromtheamericanheartassociation.Circulation,143
(18):e902–e916,2021.
AdamPaszke,SamGross,FranciscoMassa,AdamLerer,JamesBradbury,GregoryChanan,Trevor
Killeen,ZemingLin,NataliaGimelshein,LucaAntiga,etal. Pytorch: Animperativestyle,high-
performancedeeplearninglibrary. Advancesinneuralinformationprocessingsystems,32,2019.
Ignacio Perez-Pozuelo, Dimitris Spathis, Jordan Gifford-Moore, Jessica Morley, and Josh Cowls.
Digitalphenotypingandsensitivehealthdata: Implicationsfordatagovernance. Journalofthe
AmericanMedicalInformaticsAssociation,28(9):2002–2008,2021.
Attila Reiss, Ina Indlekofer, Philip Schmidt, and Kristof Van Laerhoven. Deep ppg: Large-scale
heartrateestimationwithconvolutionalneuralnetworks. Sensors,19(14):3079,2019.
Ken Rice. Linear Models and Generalized Linear Models, 2008. URL https://faculty.
washington.edu/kenrice/sisg/SISG-08-06.pdf. SISG-08.
WarrenRRuehland,PeterDRochford,FergalJO’Donoghue,RobertJPierce,ParmjitSingh,and
AndrewTThornton.Thenewaasmcriteriaforscoringhypopneas:impactontheapneahypopnea
index. sleep,32(2):150–157,2009.
TariqSadad,SyedAhmadChanBukhari,AsimMunir,AnwarGhani,AhmedMEl-Sherbeeny,and
Hafiz Tayyab Rauf. Detection of cardiovascular disease based on ppg signals using machine
learningwithcloudcomputing. ComputationalIntelligenceandNeuroscience,2022(1):1672677,
2022.
PritamSarkarandAliEtemad. Self-supervisedecgrepresentationlearningforemotionrecognition.
IEEETransactionsonAffectiveComputing,13(3):1541–1554,2020.
PhilipSchmidt, AttilaReiss, RobertDuerichen, ClausMarberger, andKristofVanLaerhoven. In-
troducingwesad,amultimodaldatasetforwearablestressandaffectdetection. InProceedingsof
the20thACMinternationalconferenceonmultimodalinteraction,pp.400–408,2018.
14

PublishedasaconferencepaperatICLR2025
FabianSchrumpf,PatrickFrenzel,ChristophAust,GeorgOsterhoff,andMircoFuchs. Assessment
of deep learning based blood pressure prediction from ppg and rppg signals. In Proceedings of
theIEEE/CVFconferenceoncomputervisionandpatternrecognition,pp.3820–3830,2021.
Kihyuk Sohn. Improved deep metric learning with multi-class n-pair loss objective. Advances in
neuralinformationprocessingsystems,29,2016.
JunhoSong,Jong-HwanJang,ByeongTakLee,DongGyunHong,Joon-myoungKwon,andYong-
YeonJo. Foundationmodelsforelectrocardiograms. arXivpreprintarXiv:2407.07110,2024.
DimitrisSpathisandFahimKawsar. Thefirststepisthehardest: Pitfallsofrepresentingandtok-
enizingtemporaldataforlargelanguagemodels. JournaloftheAmericanMedicalInformatics
Association,31(9):2151–2158,2024.
DimitrisSpathis, IgnacioPerez-Pozuelo, SorenBrage, NicholasJWareham, andCeciliaMascolo.
Self-supervisedtransferlearningofphysiologicalrepresentationsfromfree-livingwearabledata.
InProceedingsoftheConferenceonHealth,Inference,andLearning,pp.69–78,2021.
DimitrisSpathis, IgnacioPerez-Pozuelo, TomasIGonzales,YuWu, SorenBrage, NicholasWare-
ham,andCeciliaMascolo. Longitudinalcardio-respiratoryfitnesspredictionthroughwearables
infree-livingenvironments. NPJDigitalMedicine,5(1):176,2022.
ChiIanTang,IgnacioPerez-Pozuelo,DimitrisSpathis,andCeciliaMascolo. Exploringcontrastive
learninginhumanactivityrecognitionforhealthcare. arXivpreprintarXiv:2011.11542,2020.
AndriyTemko. Accurateheartratemonitoringduringphysicalexercisesusingppg. IEEETransac-
tionsonBiomedicalEngineering,64(9):2016–2024,2017.
Sana Tonekaboni, Danny Eytan, and Anna Goldenberg. Unsupervised representation learning for
timeserieswithtemporalneighborhoodcoding. arXivpreprintarXiv:2106.00750,2021.
Pieter-JanToye. Vitalvideos: Adatasetofvideoswithppgandbloodpressuregroundtruths. arXiv
preprintarXiv:2306.11891,2023.
JacobETrammelandAmitSapra. Physiology,systemicvascularresistance. 2020.
LWang,EmmaPickwell-MacPherson,YPLiang,andYuanTingZhang.Noninvasivecardiacoutput
estimationusinganovelphotoplethysmogramindex. In2009annualinternationalconferenceof
theIEEEengineeringinmedicineandbiologysociety,pp.1746–1749.IEEE,2009.
Wei-HungWeng,SebastienBaur,MayankDaswani,ChristinaChen,LaurenHarrell,SujayKakar-
math,MariamJabara,BabakBehsaz,CoryYMcLean,YossiMatias,etal. Predictingcardiovas-
culardiseaseriskusingphotoplethysmographyanddeeplearning. PLOSGlobalPublicHealth,
4(6):e0003204,2024.
YuelinWu,ShengWan,ShengyiGu,ZhengqianMou,LinglingDong,ZhongchengLuo,JunZhang,
andXiaolinHua. Gestationalweightgainandadversepregnancyoutcomes: aprospectivecohort
study. BMJopen,10(9):e038187,2020.
HugoYe`che, GideonDresdner, FrancescoLocatello, MatthiasHu¨ser, andGunnarRa¨tsch. Neigh-
borhood contrastive learning applied to online patient monitoring. In International Conference
onMachineLearning,pp.11964–11974.PMLR,2021.
HangYuan,ShingChan,AndrewPCreagh,CatherineTong,AidanAcquah,DavidAClifton,and
Aiden Doherty. Self-supervised learning for human activity recognition using 700,000 person-
daysofwearabledata. NPJdigitalmedicine,7(1):91,2024a.
ZhizhangYuan,DaozeZhang,JunruChen,GeifeiGu,andYangYang. Brant-2: Foundationmodel
forbrainsignals. arXivpreprintarXiv:2402.10251,2024b.
TaedongYun,JustinCosentino,BabakBehsaz,ZacharyRMcCaw,DavinHill,RobertLuben,Dong-
bingLai,JohnBates,HowardYang,Tae-HwiSchwantes-An,etal. Unsupervisedrepresentation
learning on high-dimensional clinical data improves genomic discovery and prediction. Nature
Genetics,pp.1–10,2024.
15

PublishedasaconferencepaperatICLR2025
Guo-QiangZhang,LicongCui,RemoMueller,ShiqiangTao,MatthewKim,MichaelRueschman,
SaraMariani,DanielMobley,andSusanRedline. Thenationalsleepresearchresource: towards
asleepdatacommons. JournaloftheAmericanMedicalInformaticsAssociation,25(10):1351–
1358,2018.
Xiang Zhang, Ziyuan Zhao, Theodoros Tsiligkaridis, and Marinka Zitnik. Self-supervised con-
trastivepre-trainingfortimeseriesviatime-frequencyconsistency. AdvancesinNeuralInforma-
tionProcessingSystems,35:3988–4003,2022.
XiaoZhang,YongqiangLyu,TongQu,PengfeiQiu,XiaominLuo,JingyuZhang,ShunjieFan,and
YuanchunShi. Photoplethysmogram-basedcognitiveloadassessmentusingmulti-featurefusion
model. ACMTransactionsonAppliedPerception(TAP),16(4):1–17,2019.
JianlongZhou,SyedZArshad,SimonLuo,KunYu,ShlomoBerkovsky,andFangChen. Indexing
cognitive load using blood volume pulse features. In Proceedings of the 2017 CHI Conference
ExtendedAbstractsonHumanFactorsinComputingSystems,pp.2269–2275,2017.
YuchenZhou,JustinCosentino,TaedongYun,MahanteshIBiradar,JacquelineShreibati,Dongbing
Lai, Tae-HwiSchwantes-An, RobertLuben, ZacharyMcCaw, JorgenEngmann, etal. Utilizing
multimodalaitoimprovegeneticanalysesofcardiovasculartraits. medRxiv,2024.
16

PublishedasaconferencepaperatICLR2025
APPENDIX
| A TRAINING | INFERENCE | DETAILS |     |     |
| ---------- | --------- | ------- | --- | --- |
AND
Architecture & Pre-training. The architecture of our ResNet 18-block encoder is described in
Tables 5, 6, and 7. Each 1D convolution layer is configured with a kernel size of 3 and a stride
of 2, while the max-pooling layer utilizes a kernel size of 3 with a stride of 1. We start with a
filter size of 32, which doubles every 4 blocks to capture progressively more complex features.
Dropout is applied with a probability of 0.5 to prevent overfitting. This backbone architecture is
used across different methods in our experiments to ensure consistency and make for a fair com-
parison during evaluation. Additionally, our SSL baselines use the same batch size, learning rate,
inputsamplingfrequency,andtrainingstepsasPAPAGEI. Weusethesameaugmentationtypesand
intensityforBYOL(Grilletal.,2020),SimCLRChenetal.(2020),andPAPAGEI-P.Furthermore,
we investigated 0.07 and 0.5 temperatures as MoCo (He et al., 2020) and SimCLR (Chen et al.,
2020), respectively. In contrast to a smaller embedding size of 256 adopted by (Abbaspourazad
etal.,2023),weprojectthelearnedrepresentationstoa512-dimensionalembeddingafterthecon-
volutional block (we investigated larger embedding sizes of 768 and 1024 and found no signifi-
cantperformancechanges). ThisembeddingisthenpassedthroughtwoMixtureofExperts(MoE)
blocks, each containing three experts. Each expert block consists of two sequential linear layers,
with sizes 256 and 1, which are used for IPA and SQI prediction tasks. It is noteworthy that both
BYOLandTF-Crequiremultipleencodersanddifferentprojectionheads,resultinginvariationsin
Forthesemethods,weuseexistingimplementationsavailableonline34,butapplyour
modelsizes.
encoderasthebackbonetoensureconsistency. Ourmodelsarepre-trainedfor15,000stepsusing
the Adam optimizer, with a learning rate of 10−4. We use a batch size of 128 for training since
aftervarioustrialswedidnotobservesignificantdifferencesinperformancewithbatchsizesof64
and 256. We performed five iterations of pre-training and selected the best-performing model for
eachdownstreamtask. ForSimCLRandPAPAGEI-P,asinglemodelconsistentlyachievesthebest
performance across all tasks. For BYOL, we select two models that perform best across all tasks.
Similarly,forTF-CandPAPAGEI-S,wechoosethreemodelswiththehighestperformance. Weuse
this approach as some models excel in certain task groups while others perform better in the rest.
Note that a more robust approach would involve broader hyperparameter tuning with k-fold vali-
dationtoobtaintheoptimalmodel. However,thisrequiressubstantialcomputationalresourcesfor
pre-training. Additionally, we did not perform an exhaustive evaluation of different augmentation
settingsbutinsteadusedtransformationsandvaluesbasedonpriorresearch(Abbaspourazadetal.,
2023;Tangetal.,2020). Formodeltraining,weprimarilyusedPyTorch(Paszkeetal.,2019). The
NTXentLossimplementationwassourcedfromthePyTorchMetricLearningpackage5.
| Table 5: ResNet-style | CNN encoder | architec- |     |     |
| --------------------- | ----------- | --------- | --- | --- |
tureusedinPAPAGEI.
Table 7: Basic Block
Type2
| Layer | OutputShape |     |     |     |
| ----- | ----------- | --- | --- | --- |
Table 6: Basic Block
Type1
| Conv1     | [32,32,1250] |     |     | Layer |
| --------- | ------------ | --- | --- | ----- |
| BatchNorm | [32,32,1250] |     |     |       |
BatchNorm
| ReLU | [32,32,1250] |     | Layer |     |
| ---- | ------------ | --- | ----- | --- |
ReLU
| BasicBlockType1     | [32,32,1250] |     |           |           |
| ------------------- | ------------ | --- | --------- | --------- |
|                     |              |     | Conv1D    | Dropout   |
| (BasicBlockType2)×3 | [32,32,313]  |     |           |           |
|                     |              |     | BatchNorm | Conv1D    |
| (BasicBlockType2)×4 | [32,64,79]   |     |           |           |
|                     |              |     | ReLU      | BatchNorm |
| (BasicBlockType2)×4 | [32,128,20]  |     |           |           |
|                     |              |     | Dropout   | ReLU      |
| (BasicBlockType2)×4 | [32,256,5]   |     |           |           |
|                     |              |     | Conv1D    | Dropout   |
| (BasicBlockType2)×2 | [32,512,3]   |     |           |           |
Conv1D
| BatchNorm | [32,512,3] |     |     |     |
| --------- | ---------- | --- | --- | --- |
Maxpool
| ReLU   | [32,512,3] |     |     |     |
| ------ | ---------- | --- | --- | --- |
| Linear | [32,512]   |     |     |     |
3https://github.com/chengding0713/SiamQuality
4https://github.com/mims-harvard/TFC-pretraining
5https://github.com/KevinMusgrave/pytorch-metric-learning
17

PublishedasaconferencepaperatICLR2025
Parameters: TrainingandInference. Thissectionoutlinesthetrainingandinferenceparameters
| usedinourmethods. | Inferenceparametersarethoseutilizedforfeatureextraction. |     |     |     |
| ----------------- | -------------------------------------------------------- | --- | --- | --- |
• PAPAGEI-P(5M)andSimCLR(5M):Bothtrainingandinferenceinvolve5Mparameters.
ForSimCLR,itisworthnotingthatweusetheprojectionfeaturesduringinferenceinstead
ofusingtheencoderonly.
• BYOL(5M):Duringtraining,theonlineandtargetencoderseachhave5Mparameters,and
theprojectoris800K.Atinference,onlytheonlineencoderisusedforfeatureextraction,
totaling5Mparameters.
• TF-C (10M): The time and frequency encoders each have 5M parameters, followed by a
smallerprojector(<100K).Sincebothencodersandprojectorsarerequiredforinference,
thetotalparametercountis10M.
• PAPAGEI-S (5M): The encoder consists of 5M parameters, while the expert heads con-
tributeapproximately400Keach. Astheexpertheadsarenotusedforfeatureextraction,
theinferenceparametertotalremains5M.
Feature Extraction & Linear Evaluation We extracted the projected embedding for linear eval-
uation. For Moment and Chronos, we extract the default embedding size, which is 1024 and 768,
respectively.Weusecross-validatedgridsearchtoidentifythebestparametersforourlinearprobes.
The hyperparameters chosen for each model are as follows: (1) Logistic Regression: {’penalty’:
[’l1’, ’l2’], ’C’: [0.01, 0.1, 1, 10, 100], ’solver’: [’lbfgs’], ’max iter’: [100, 200]}. (2) Linear Re-
gression: {’alpha’: [0.1,1.0,10.0,100.0],’solver’: [’auto’,’cholesky’,’sparse cg’]}. (3)Random
Forest: {’n estimators’: [100, 200], ’max features’: [’sqrt’, ’log2’], ’max depth’: [10, 20, 30],
| ’min samples | split’: [2,5],’min | samples leaf’: | [1,2]} |     |
| ------------ | ------------------ | -------------- | ------ | --- |
| B DATASETS   | AND                | TASKS          |        |     |
Table8:ThetaskevaluationbenchmarkofPAPAGEI.Datasetshighlightedingrayareunseenduring
training, thus, the corresponding tasks are out-of-domain. The rest were used for pre-training but
theirtestsetsandlabelsareheldout.Fortasktype,B/M/RrefertoBinaryclassification,Multi-class
classification(#classes),andRegression,respectively.
#ID Dataset SR(Hz) Collectedby Task TaskType #Participants(#Samples)
T1 VitalDB(Leeetal.,2022) 500 ICUmonitor ICUadmission(Yes/No) B 5866
| T2  |     |     | OperationType | M(11) 5866 |
| --- | --- | --- | ------------- | ---------- |
T3 MIMIC-III(Moodyetal.,2020) 125 ICUMonitor Mortality B 5596
T4 MESA(Zhangetal.,2018) 256 Polysomnographyfinger Smoker B 2055
| T5  |     |     | AHI>3%OxygenDesat. | R 2055 |
| --- | --- | --- | ------------------ | ------ |
| T6  |     |     | AHI>4%OxygenDesat. | R 2055 |
T7 nuMom2B(Faccoetal.,2015) 75 Polysomnographyfinger Pregnancystage(early/late) B 3163(5337)
| T8                         |     |           | GestationAge | R 3163(5337) |
| -------------------------- | --- | --------- | ------------ | ------------ |
| T9 VV(SkinTone)(Toye,2023) |     | 60 Finger | SystolicBP   | R 231        |
| T10                        |     |           | DiastolicBP  | R 231        |
T11 PPG-BP(Liangetal.,2018a) 1000 FingerPulseOx SystolicBP R 219
| T12 |     |     | DiastolicBP      | R 219 |
| --- | --- | --- | ---------------- | ----- |
| T13 |     |     | AverageHeartRate | R 219 |
| T14 |     |     | Hypertension     | B 219 |
T15 SDB(Gardeetal.,2014) 62.5 FingerPulseOx SleepDisorderedBreathing B 146
| T16 ECSMP(Gaoetal.,2021)     |     | 64 Wrist | MoodDisturbance | B 89       |
| ---------------------------- | --- | -------- | --------------- | ---------- |
| T17 WESAD(Schmidtetal.,2018) |     | 64 Wrist | Valence         | B 15(4497) |
| T18                          |     |          | Arousal         | B 15(4497) |
T19 PPG-DaLiA(Reissetal.,2019) 64 Wrist HeartRate R 15(64697)
| T20 |     |     | Activity | M(9) 15(64697) |
| --- | --- | --- | -------- | -------------- |
VitalDB.TheVitalDBdatasetprovidescomprehensivemonitoringofvitalsignsandphysiological
parametersfrom6,388surgicalcases. Thishigh-resolutiondatasetincludesawiderangeofintraop-
erativemonitoringvariablessuchasheartrate,bloodpressure,oxygensaturation,andothercritical
physiologicalsignals,collectedatfrequentintervalsthroughoutsurgery. Thesurgicaloperationbe-
longstooneoftheelevencategories: colorectal,biliary/pancreas,stomach,majorresection,minor
resection,breast,transplantation,thyroid,hepatic,vascular,andothers. Afterthedatacleaningpro-
cess,wenarrowedthedatasetdownto5,866participantswithcompleteandusableinformation. As
depicted in Figure 10, we observe that the gender distribution is relatively balanced, with nearly
equalrepresentationofmaleandfemalepatients. Additionally,themajorityoftheparticipantsfall
18

PublishedasaconferencepaperatICLR2025
withintheagerangeof50to70,withasignificantproportionbeingaround60yearsold. TheICU
labelcorrespondstowhetherthepersonwasadmittedtotheICUornot.
VitalDB
500
| 400 |     |     | VitalDB | VitalDB |
| --- | --- | --- | ------- | ------- |
tnuoC
3000
300
4000
tnuoC 2000 tnuoC
200
2000
100 1000
0
|      |       | 0   | 0   |     |
| ---- | ----- | --- | --- | --- |
| 0 20 | 40 60 | 80  |     |     |
|      |       |     | M F | 0 1 |
age
|     |           |                                      | sex | ICU |
| --- | --------- | ------------------------------------ | --- | --- |
|     | Figure10: | VitalDBdatasetdescriptivestatistics. |     |     |
MIMIC-III.Inouranalysis, weutilizetheMIMIC-IIIwaveformdatabasematchedsubset, which
comprises data from 10,282 ICU patients. From this dataset, we focus specifically on extracting
photoplethysmogram(PPG)data,provideditisavailableforeachpatient. Toensurethequalityof
the data, we set a criterion of at least 1 minute of usable PPG signal that must be present. After
performing a thorough data cleaning process, we end up with a cohort of 5,596 participants with
reliablePPGdata. AsillustratedinFigure11,thedatasetshowsagenderimbalance,withahigher
proportionofmalepatientscomparedtofemalepatients. Additionally,themajorityofparticipants
are aged 60 years or older, reflecting a typical ICU population that often includes elderly patients
withcriticalhealthconditions.
MESA. The Multi-Ethnic Study of Atherosclerosis (MESA) sleep sub-study gathered data from
2,237participantsthroughovernight,unattendedpolysomnographytoassessvarioussleepparame-
ters.Afterthedatacleaningprocess,weretained2,055participantsforanalysis.AsshowninFigure
12,thedatasetshowsaslightlylargerproportionoffemaleparticipants. Theagedistributionreveals
thatmostparticipantsarebetween60and80yearsold,reflectinganolderadultpopulation,which
iscommonlystudiedconcerningsleepdisordersandcardiovascularrisks.
Inthisstudy,weusetheApnea-HypopneaIndex(AHI)withatleast3%and4%oxygendesaturation
astheprimarymeasurefordiagnosingsleepapnea,asrecommendedbytheAmericanAcademyof
SleepMedicine(Ruehlandetal.,2009). Thesethresholdsindicatetheseverityofsleepapnea,with
oxygendesaturationduringapneas/hypopneasbeingacriticalfactor. WepredicttheseAHIvalues
directlyinourregressionmodels.Additionally,weclassifyparticipantswithanyhistoryofsmoking
as smokers. This approach allows us to account for both current and former smokers, capturing a
broaderrangeofsmoking-relatedhealthriskswithinouranalysis.
NuMoM2B.Changesingestationalageandpregnancystageareriskfactorsassociatedwithadverse
pregnancyoutcomessuchashypertensivedisordersandsmall-for-gestational-agedelivery(Bouariu
et al., 2022; Parikh et al., 2021; Wu et al., 2020; Crump et al., 2023). These diseases affect heart
MIMIC-III
400
MIMIC-III
| 300 |     |     | 3000 |     |
| --- | --- | --- | ---- | --- |
tnuoC
tnuoC
| 200  |           |                                        | 2000 |     |
| ---- | --------- | -------------------------------------- | ---- | --- |
| 100  |           |                                        | 1000 |     |
| 0    |           |                                        | 0    |     |
| 0 20 | 40 60     | 80                                     | M    | F   |
|      | age       |                                        | sex  |     |
|      | Figure11: | MIMIC-IIIdatasetdescriptivestatistics. |      |     |
19

PublishedasaconferencepaperatICLR2025
150
100
50
0
60 70 80 90
age
tnuoC
MESA
200
150
100
50
0
0 25 50 75 100
AHI > 3%
tnuoC
MESA
400
300
200
100
0
0 20 40 60 80 100
AHI > 4%
tnuoC
MESA
1000
500
0
female male
sex
tnuoC
MESA
1000
500
0
yes no not reported
Smoking
tnuoC
MESA
Figure12: MESAdatasetdescriptivestatistics.
300
200
100
0
20 30 40
age
tnuoC
NuMoM2B
1250
1000
750
500
250
0
10 20 30
Gestation Age
tnuoC
NuMoM2B
3000
2000
1000
0
1 3
Pregnancy Stage
tnuoC
NuMoM2B
Figure13: NuMoM2Bdatasetdescriptivestatistics.
functionthatcanbemeasuredusingthePPGsensor(Felietal.,2024). TheNulliparousPregnancy
Outcomes Study: monitoring mothers-to-be (nuMoM2B) sub-study examines the relationship be-
tweenadversepregnancyoutcomesandsleepdisorders. Inparticular,anovernightpolysomnograph
thatcollectsPPGdataisadministeredtothewomenattheirhomesduring6-15weeks(early)and
22-31 weeks (late) of pregnancy. Therefore, our tasks are to classify between early and late-stage
pregnancyaswellaspredictthegestationageofthefetus. InFigure13,weobservethatmaternal
agepeaksaround28years. Thegestationalagedistributionisbimodal,whichweuseasapredictor
inourregressiontask. Forpregnancystage,weclassifyvisit1asearlyandvisit3aslate.
VitalVideos (VV) (Skin Tone). The Vital Videos study is an ongoing project that collects data
on vital signs, videos, and blood pressure across a variety of conditions, including variations in
lighting,background,andskintone. Forouranalysis,weuseddatafromtwogroups,totalling231
participants,fromEuropeandSub-SaharanAfrica. AsshowninFigure14,mostparticipantshavea
Fitzpatrickskintoneof5or6,indicatingdarkerskin. Thedatasetisprimarilycomposedoffemale
participants,withanagerangebetween40and60years. Additionally,themajorityofparticipants
had asystolic bloodpressure ofaround 125and a diastolic pressure ofaround 80, suggesting that
mostindividualsinthestudywererelativelyhealthy.
PPG-BP.ThePPG-BPconsistsofshortPPGrecordingsfrom219participantscollectedat1000Hz.
For each subject, there are three 2.1s recordings. For our analysis, we zero pad them to 10s. In
Figure15, theagedistributionshowsthatmostparticipantsarebetween40and80yearsold, with
fewerparticipantsunder40. Furthermore, themajorityofindividualshavehypertension. Interms
of gender, the dataset has slightly more females than males. The distribution of systolic blood
pressure is centered around 120-140, indicating a population with normal to moderately elevated
blood pressure, while diastolic blood pressure predominantly falls between 70 and 90. Lastly, the
averageheartrateformostparticipantsrangesbetween70and90beatsperminute.
20

PublishedasaconferencepaperatICLR2025
Vital Videos (VV)
Vital Videos (VV)
40
75
30
| tnuoC |     |     |     |     |     |     |     | tnuoC |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
50
20
25
10
0
0
|     | 20  | 40  | 60  | 80  |     |     |     |     | 1 2               | 3 4 5 6 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ------- |
|     |     |     | age |     |     |     |     |     | Fitzpatrick Scale |         |
Vital Videos (VV)
150
| tnuoC |     |     |     |     | Vital Videos (VV) |     |     |     |                   |     |
| ----- | --- | --- | --- | --- | ----------------- | --- | --- | --- | ----------------- | --- |
| 100   |     |     |     | 40  |                   |     |     |     | Vital Videos (VV) |     |
40
30
|     |     |     |     | tnuoC |     |     | tnuoC |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | ----- | --- | --- | --- |
| 50  |     |     |     |       |     |     |       | 30  |     |     |
20
20
10
| 0   |     |           |     |                                          |             |         |     | 10  |              |             |
| --- | --- | --------- | --- | ---------------------------------------- | ----------- | ------- | --- | --- | ------------ | ----------- |
|     |     | F         | M   | 0                                        |             |         |     | 0   |              |             |
|     |     |           |     |                                          | 100 125 150 | 175 200 |     |     |              |             |
|     |     | sex       |     |                                          |             |         |     | 60  | 80           | 100 120 140 |
|     |     |           |     |                                          | Systolic BP |         |     |     | Diastolic BP |             |
|     |     | Figure14: |     | VitalVideosdatasetdescriptivestatistics. |             |         |     |     |              |             |
PPG-BP
|     |     |     |     |     | PPG-BP |     |     |     |     | PPG-BP |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | ------ |
30
| tnuoC |     |     |     |           |     |     |       | 100 |     |     |
| ----- | --- | --- | --- | --------- | --- | --- | ----- | --- | --- | --- |
|       |     |     |     | tnuoC 100 |     |     | tnuoC |     |     |     |
20
|     |     |     |     | 50  |     |     |     | 50  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
10
| 0     |     |        |     | 0        |              |     |       | 0   |        |      |
| ----- | --- | ------ | --- | -------- | ------------ | --- | ----- | --- | ------ | ---- |
| 20    | 40  | 60     | 80  |          |              |     |       |     |        |      |
|       |     |        |     |          | 0            | 1   |       |     | Female | Male |
|       |     | age    |     |          | Hypertension |     |       |     |        | sex  |
|       |     | PPG-BP |     |          | PPG-BP       |     |       |     | PPG-BP |      |
| 30    |     |        |     | 40       |              |     |       | 30  |        |      |
| tnuoC |     |        |     | tnuoC 30 |              |     | tnuoC |     |        |      |
20
20
20
| 10  |     |     |     |     |     |     |     | 10  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
10
| 0        |                  |         |           | 0                                   |                  |     |     | 0     |         |           |
| -------- | ---------------- | ------- | --------- | ----------------------------------- | ---------------- | --- | --- | ----- | ------- | --------- |
| 80       | 100 120          | 140 160 | 180       |                                     | 60 80            | 100 |     | 50 60 | 70      | 80 90 100 |
|          | Systolic BP      |         |           |                                     | Diastolic BP     |     |     |       | Avg. HR |           |
|          |                  |         | Figure15: | PPG-BPdatasetdescriptivestatistics. |                  |     |     |       |         |           |
| SDB. The | sleep-disordered |         | breathing |                                     | dataset includes |     |     |       |         |           |
SDB
| data from | 146 | children, | collected | through | polysomnog- |     |     |     |     |     |
| --------- | --- | --------- | --------- | ------- | ----------- | --- | --- | --- | --- | --- |
75
| raphy with | finger | recordings |     | lasting | over three hours. |     | tnuoC |     |     |     |
| ---------- | ------ | ---------- | --- | ------- | ----------------- | --- | ----- | --- | --- | --- |
50
GroundtruthlabelsareprovidedasApnea-HypopneaIn-
| dex (AHI)                                    | values, | categorized |     | into four | levels: 0 (nor- |     | 25  |     |     |     |
| -------------------------------------------- | ------- | ----------- | --- | --------- | --------------- | --- | --- | --- | --- | --- |
| mal),1(mild,AHIbetween5and15),2(moderate,AHI |         |             |     |           |                 |     |     | 0   |     |     |
|                                              |         |             |     |           |                 |     |     | 0   | 1   | 2 3 |
Sleep Disordered Breathing
between15and30),and3(severe,AHIover30)asshown
| inFigure16. | Forourclassificationtask,wegroupAHI0 |     |     |     |     |        |     |     |         |             |
| ----------- | ------------------------------------ | --- | --- | --- | --- | ------ | --- | --- | ------- | ----------- |
|             |                                      |     |     |     |     | Figure | 16: | SDB | dataset | descriptive |
asindicatingnosleepbreathingdisorder,whileAHIlev-
statistics.
| els 1 through | 3   | are classified |     | as the presence | of a sleep |     |     |     |     |     |
| ------------- | --- | -------------- | --- | --------------- | ---------- | --- | --- | --- | --- | --- |
breathingdisorder.
21

PublishedasaconferencepaperatICLR2025
ECSMP. The ECSMP dataset was gathered to study the relationship between emotion, cognition,
and sleep in 89 participants. As shown in Figure 17, the majority of the participants are young
adult females, with an average age of around 25 years. Mood disturbances were measured using
the Profile of Mood States (POMS) scale, which captures various aspects of emotional states. To
classifyparticipantsintohighversuslowmooddisturbancecategories,webinarizedtheTotalMood
Disturbance(TMD)valuesbyusingthemedianasthecutoffpoint.
|     | ECSMP |     | ECSMP |     |     |       |
| --- | ----- | --- | ----- | --- | --- | ----- |
| 20  |       |     |       |     |     | ECSMP |
15
40
| tnuoC 15 |     |     | tnuoC |     |       |     |
| -------- | --- | --- | ----- | --- | ----- | --- |
|          |     |     | 10    |     | tnuoC |     |
10
20
| 5     |       |           | 5                                  |             |     |     |
| ----- | ----- | --------- | ---------------------------------- | ----------- | --- | --- |
| 0     |       |           | 0                                  |             | 0   |     |
| 18 20 | 22 24 | 26 28     | 100 120                            | 140 160 180 | F   | M   |
|       | age   |           | Mood Disturbance                   |             |     | sex |
|       |       | Figure17: | ECSMPdatasetdescriptivestatistics. |             |     |     |
WESAD. The wearable stress and affect detection dataset is a multi-modal dataset collected from
15 participants using various sensor modalities. In this study, participants were exposed to videos
designed to elicit different affective states, such as amusement, meditation, stress, and baseline
conditions. Following each session, participants completed the Self-Assessment Manikins (SAM)
questionnaire (Bradley & Lang, 1994), which provided the ground-truth values for valence and
arousal. In our analysis, we binarized these values by categorizing valence and arousal as low (1)
when less than 5 and high (0) otherwise. Then, we perform regression at the segment level. As
showninFigure18,arousallevelsaregenerallylow,whilevalencetendstobehighinmostcases.
|            |     | WESAD |     |       | WESAD |     |
| ---------- | --- | ----- | --- | ----- | ----- | --- |
| 1500       |     |       |     | 1500  |       |     |
| tnuoC 1000 |     |       |     | tnuoC |       |     |
1000
| 500 |     |     |     | 500 |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| 0   |     |     |     | 0   |     |     |
1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0 1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0
|     |     | Arousal   |                                    |     | Valence |     |
| --- | --- | --------- | ---------------------------------- | --- | ------- | --- |
|     |     | Figure18: | WESADdatasetdescriptivestatistics. |     |         |     |
PPG-DaLiA.ThisdatasetcollectsPPGsignalsfrom15participantsforheartrateestimationwhile
performing various daily activities. These activities include sitting, ascending/descending stairs,
tablesoccer,cycling,driving,lunchbreak,walking,andworking. Asaresult,thedatasetcapturesa
widerangeofheartrates,varyingfrom60to150beatsperminute,dependingonthespecificactivity
beingperformed. ToalignthePPGsignalwiththeactivitylabels,weusea8swindowwith6sand
2soverlapandshift,respectively. Afterthis,weresampleandpadthesignaltofacilitatemodeling.
DaLiA
2000
1500
|       |     | DaLiA |     | tnuoC |     |     |
| ----- | --- | ----- | --- | ----- | --- | --- |
| 15000 |     |       |     | 1000  |     |     |
tnuoC
10000
500
5000
0
0
|     |         |             |                                        |     | 50 100 | 150 |
| --- | ------- | ----------- | -------------------------------------- | --- | ------ | --- |
| 0.0 | 1.0 2.0 | 3.0 4.0 5.0 | 6.0 7.0 8.0                            |     |        |     |
|     |         | Activity    |                                        |     |        | HR  |
|     |         | Figure19:   | PPG-DaLiAdatasetdescriptivestatistics. |     |        |     |
22

PublishedasaconferencepaperatICLR2025
| C REPRESENTATIVE | SIGNALS | PRE-TRAINING | DATASETS |     |
| ---------------- | ------- | ------------ | -------- | --- |
FROM
VitalDB @ 500Hz
25
0
|     | 0 1000 | 2000 | 3000 4000 | 5000 |
| --- | ------ | ---- | --------- | ---- |
MESA @ 256Hz
0
250
|     | 0 500 | 1000 | 1500 2000 | 2500 |
| --- | ----- | ---- | --------- | ---- |
MIMIC-III @ 125Hz
0.25
0.00
|     | 0 200 | 400 600 | 800 1000 | 1200 |
| --- | ----- | ------- | -------- | ---- |
Figure20:Representative10-secondrawPPGsegmentsfromVitalDB,MESA,andMIMIC-III.We
observethateachsignal’samplitude(y-axis)andsamplingratediffer.
VitalDB @ 125Hz
2.5
0.0
|     | 0 200 | 400 600 | 800 1000 | 1200 |
| --- | ----- | ------- | -------- | ---- |
MESA @ 125Hz
0
2
|     | 0 200 | 400 600 | 800 1000 | 1200 |
| --- | ----- | ------- | -------- | ---- |
MIMIC-III @ 125Hz
2
0
|     | 0 200 | 400 600 | 800 1000 | 1200 |
| --- | ----- | ------- | -------- | ---- |
Figure 21: Normalized and resampled 10-second pre-processed PPG segments from VitalDB,
MESA, and MIMIC-III. These signals represent the final form before being fed to our models.
Weobservethatthesignalcharacteristicsacrossdatasetsaremoreconsistent.
23

PublishedasaconferencepaperatICLR2025
| D ADDITIONAL | RESULTS |     |     |     |     |
| ------------ | ------- | --- | --- | --- | --- |
D.1 MULTI-CLASSCLASSIFICATION
Table 9: Multi-class classification comparison against pre-trained models. Feature extraction
parametersareindicatednexttoeachname.. 95%CIsarereportedinsquarebracketsandthebest
valueisbolded.
|                       | REGLE(0.07M)    | Chronos(200M)      | Moment(385M)        | PAPAGEI-P(5M) | PAPAGEI-S(5M) |
| --------------------- | --------------- | ------------------ | ------------------- | ------------- | ------------- |
| Classification-ACC(↑) | (Yunetal.,2024) | (Ansarietal.,2024) | (Goswamietal.,2024) |               |               |
OperationType 0.21[0.18-0.23] 0.25[0.22-0.29] 0.27[0.23-0.31] 0.30[0.26-0.33] 0.30[0.27-0.32]
Activity 0.29[0.28-0.29] 0.41[0.40-0.42] 0.41[0.40-0.42] 0.38[0.37-0.39] 0.37[0.36-0.37]
|     | 0.25±0.04 | 0.33±0.08 | 0.34±0.07 | 0.34±0.04 | 0.33±0.03 |
| --- | --------- | --------- | --------- | --------- | --------- |
Average
Table10: Multi-classclassificationcomparisonagainstCLmethods. Featureextractionparame-
tersareindicatednexttoeachname.. 95%CIsarereportedinsquarebracketsandthebestvalueis
bolded.
|                       | Stat.Features | SimCLR(5M) BYOL(5M)                | TF-C(10M)         | PAPAGEI-P(5M) | PAPAGEI-S(5M) |
| --------------------- | ------------- | ---------------------------------- | ----------------- | ------------- | ------------- |
| Classification-ACC(↑) |               | (Chenetal.,2020) (Grilletal.,2020) | (Zhangetal.,2022) |               |               |
OperationType 0.27[0.24-0.32] 0.27[0.24-0.29] 0.310.27-0.34 0.27[0.27-0.29] 0.30[0.26-0.33] 0.30[0.27-0.32]
Activity 0.37[0.36-0.38] 0.36[0.35-0.37] 0.34[0.33-0.35] 0.37[0.36-0.38] 0.38[0.37-0.39] 0.37[0.36-0.37]
Average 0.32±0.05 0.31±0.04 0.32±0.01 0.32±0.05 0.34±0.04 0.33±0.03
| D.2 F1-SCOREANDR2 | EVALUATIONMETRICS. |     |     |     |     |
| ----------------- | ------------------ | --- | --- | --- | --- |
Table 11: Downstream comparison against pre-trained models (additional metrics: F1-score
andR2).
Featureextractionparametersareindicatednexttoeachname. 95%CIsarereportedin
squarebracketsandthebestvalueisbolded.
|     | REGLE(0.07M) | Chronos(200M) | Moment(385M) | PAPAGEI-P(5M) | PAPAGEI-S(5M) |
| --- | ------------ | ------------- | ------------ | ------------- | ------------- |
Classification-F1-Score(↑)
|     | (Yunetal.,2024) | (Ansarietal.,2024) | (Goswamietal.,2024) |     |     |
| --- | --------------- | ------------------ | ------------------- | --- | --- |
ICUAdmission 0.00[0.00-0.00] 0.20[0.11-0.30] 0.12[0.04-0.20] 0.12[0.04-0.20] 0.26[0.18-0.33]
Mortality 0.00[0.00-0.00] 0.14[0.09-0.19] 0.16[0.11-0.21] 0.22[0.16-0.27] 0.17[0.13-0.22]
Smoker 0.16[0.10-0.23] 0.51[0.44-0.58] 0.40[0.33-0.47] 0.45[0.38-0.51] 0.45[0.37-0.50]
Pregnancystage 0.49[0.47-0.52] 0.69[0.67-0.71] 0.63[0.60-0.65] 0.62[0.59-0.64] 0.65[0.62-0.67]
Hypertension 0.77[0.70-0.84] 0.68[0.58-0.77] 0.75[0.66-0.84] 0.84[0.72-0.92] 0.78[0.70-0.86]
SleepDisorderedBreathing 0.00[0.00-0.00] 0.33[0.00-0.60] 0.22[0.00-0.47] 0.32[0.00-0.60] 0.47[0.23-0.67]
MoodDisturbance 0.00[0.00-0.00] 0.36[0.10-0.59] 0.23[0.00-0.47] 0.37[0.00-0.66] 0.32[0.00-0.58]
Valence 0.00[0.00-0.00] 0.10[0.07-0.14] 0.12[0.09-0.16] 0.17[0.13-0.21] 0.03[0.01-0.04]
Arousal 0.83[0.81-0.84] 0.82[0.80-0.83] 0.81[0.79-0.82] 0.81[0.79-0.82] 0.83[0.81-0.84]
| Average | 0.25±0.33 | 0.42±0.24 | 0.38±0.26 | 0.43±0.25 | 0.44±0.25 |
| ------- | --------- | --------- | --------- | --------- | --------- |
Regression-R2(↑)
Apnea/HypopneaIndex>3% 0.02[0.00-0.03] 0.18[0.08-0.26] 0.14[0.06-0.22] 0.15[0.05-0.24] 0.29[0.22-0.36]
Apnea/HypopneaIndex>4% 0.01[0.00-0.03] 0.16[0.08-0.22] 0.13[0.05-0.20] 0.12[0.03-0.22] 0.28[0.20-0.34]
GestationAge 0.04[0.02-0.06] 0.28[0.24-0.31] 0.20[0.17-0.23] 0.18[0.14-0.22] 0.22[0.19-0.25]
SystolicBP(VV) -0.03[-0.18-0.01] -0.24[-0.72-0.03] 0.06[-0.25-0.28] -0.41[-0.77-(-0.15)] 0.15[-0.09-0.30]
DiastolicBP(VV) 0.01[-0.09-0.06] -0.29[-0.87-(-0.01)] 0.01[-0.25-0.14] -0.48[-1.02-(-0.20)] 0.10[-0.11-0.23]
SystolicBP(PPG-BP) -0.07[-0.21-0.04] -0.13[-0.36-0.06] 0.07[-0.31-0.31] 0.36[0.16-0.49] 0.20[0.02-0.31]
DiastolicBP(PPG-BP) 0.01[-0.05-0.02] -0.10[-0.45-0.07] -0.03[-0.31-0.13] 0.22[-0.13-0.40] 0.08[-0.07-0.17]
AverageHR 0.37[0.17-0.51] 0.02[-0.16-0.17] 0.68[0.45-0.80] 0.79[0.57-0.90] 0.78[0.69-0.83]
HR 0.00[0.00-0.01] 0.57[0.56-0.59] 0.63[0.61-0.64] 0.52[0.51-0.53] 0.48[0.42-0.46]
| Average | 0.04±0.12 | 0.05±0.25 | 0.21±0.24 | 0.16±0.38 | 0.28±0.20 |
| ------- | --------- | --------- | --------- | --------- | --------- |
D.3 ABLATIONRESULTS
In this section, weprovide the numeric results for thescaling analysis (Table 13) and PAPAGEI-S
componentanalysis(Table14).
24

PublishedasaconferencepaperatICLR2025
Table12: DownstreamcomparisonagainstCLmodels(additionalmetrics: F1-scoreandR2).
Feature extraction parameters are indicated next to each name. 95% CIs are reported in square
bracketsandthebestvalueisbolded.
| Stat.Features | SimCLR(5M) BYOL(5M) | TF-C(10M) | PAPAGEI-P(5M) | PAPAGEI-S(5M) |
| ------------- | ------------------- | --------- | ------------- | ------------- |
Classification-F1-Score(↑)
ICUAdmission 0.30[0.18-0.40] 0.19[0.12-0.26] 0.17[0.11-0.22] 0.10[0.05-0.16] 0.12[0.04-0.20] 0.26[0.18-0.33]
Mortality 0.03[0.01-0.06] 0.15[0.10-0.20] 0.13[0.08-0.17] 0.15[0.10-0.20] 0.22[0.16-0.27] 0.17[0.13-0.22]
Smoker 0.47[0.40-0.53] 0.43[0.35-0.49] 0.49[0.42-0.56] 0.37[0.30-0.44] 0.45[0.38-0.51] 0.45[0.37-0.50]
Pregnancystage 0.43[0.41-0.47] 0.60[0.57-0.63] 0.60[0.57-0.63] 0.59[0.56-0.62] 0.62[0.59-0.64] 0.65[0.62-0.67]
Hypertension 0.73[0.58-0.85] 0.82[0.73-0.89] 0.81[0.73-0.88] 0.81[0.72-0.89] 0.84[0.72-0.92] 0.78[0.70-0.86]
SleepDisorderedBreathing 0.00[0.00-0.00] 0.46[0.21-0.64] 0.45[0.23-0.62] 0.19[0.00-0.36] 0.32[0.00-0.60] 0.47[0.23-0.67]
MoodDisturbance 0.21[0.00-0.47] 0.21[0.00-0.44] 0.37[0.00-0.67] 0.56[0.27-0.80] 0.37[0.00-0.66] 0.32[0.00-0.58]
Valence 0.04[0.02-0.07] 0.09[0.06-0.12] 0.01[0.00-0.03] 0.07[0.04-0.09] 0.17[0.13-0.21] 0.03[0.01-0.04]
Arousal 0.82[0.81-0.83] 0.81[0.79-0.82] 0.83[0.81-0.84] 0.81[0.80-0.83] 0.81[0.79-0.82] 0.83[0.81-0.84]
Average 0.33±0.28 0.42±0.26 0.43±0.27 0.40±0.27 0.43±0.25 0.44±0.25
Regression-R2(↑)
Apnea/HypopneaIndex>3% -0.00[-0.06-0.03] 0.16[0.07-0.23] 0.16[0.08-0.22] 0.06[-0.00-0.13] 0.15[0.05-0.24] 0.29[0.22-0.36]
Apnea/HypopneaIndex>4% -0.01[-0.07-0.03] 0.13[0.06-0.21] 0.13[0.05-0.19] 0.13[-0.06-0.26] 0.12[0.03-0.22] 0.28[0.20-0.34]
GestationAge 0.07[0.04-0.10] 0.19[0.15-0.21] 0.19[0.15-0.22] 0.18[0.15-0.21] 0.18[0.14-0.22] 0.22[0.19-0.25]
SystolicBP(VV) -0.10[-0.51-0.10] -0.05[-0.44-0.21] -0.03[-0.37-0.18] -0.05[-0.36-0.12] -0.41[-0.77-(-0.15)] 0.15[-0.09-0.30]
DiastolicBP(VV) -0.15[-0.31-0.11] -0.14[-0.29-0.08] -0.01[-0.40-0.20] -0.09[-0.45-0.16] -0.48[-1.02-(-0.20)] 0.10[-0.11-0.23]
SystolicBP(PPG-BP) 0.12[-0.04-0.21] 0.09[-0.20-0.31] 0.10[-0.16-0.30] 0.13[-0.06-0.26] 0.36[0.16-0.49] 0.20[0.02-0.31]
DiastolicBP(PPG-BP) 0.01[-0.18-0.14] 0.00[-0.20-0.18] 0.05[-0.11-0.17] 0.02[-0.15-0.12] 0.22[-0.13-0.40] 0.08[-0.07-0.17]
AverageHR 0.15[-0.10-0.33] 0.74[0.64-0.80] 0.65[0.50-0.77] 0.82[0.73-0.88] 0.79[0.57-0.90] 0.78[0.69-0.83]
HR 0.34[0.32-0.36] 0.45[0.44-0.47] 0.36[0.35-0.37] 0.54[0.53-0.55] 0.52[0.51-0.53] 0.48[0.42-0.46]
Average 0.05±0.14 0.17±0.25 0.18±0.20 0.19±0.28 0.16±0.38 0.28±0.20
Table 13: Scaling: Downstream comparison for different PAPAGEI-S models. 95% CIs are
reportedinsquarebracketsandthebestvalueisbolded.
|     | PAPAGEI-S-5M | PAPAGEI-S-35M | PAPAGEI-S-139M |     |
| --- | ------------ | ------------- | -------------- | --- |
Classification-AUROC(↑)
| ICUAdmission             | 0.79[0.75-0.82] | 0.72[0.68-0.75] | 0.77[0.73-0.80] |     |
| ------------------------ | --------------- | --------------- | --------------- | --- |
| Mortality                | 0.67[0.63-0.70] | 0.66[0.63-0.70] | 0.66[0.63-0.69] |     |
| Smoker                   | 0.61[0.56-0.66] | 0.58[0.52-0.64] | 0.59[0.54-0.65] |     |
| Pregnancystage           | 0.78[0.75-0.80] | 0.77[0.75-0.79] | 0.76[0.74-0.78] |     |
| Hypertension             | 0.77[0.68-0.87] | 0.75[0.64-0.85] | 0.77[0.65-0.87] |     |
| SleepDisorderedBreathing | 0.70[0.57-0.84] | 0.59[0.44-0.74] | 0.62[0.46-0.78] |     |
| MoodDisturbance          | 0.56[0.33-0.77] | 0.53[0.30-0.73] | 0.54[0.29-0.78] |     |
| Valence                  | 0.56[0.54-0.59] | 0.53[0.50-0.56] | 0.54[0.51-0.56] |     |
| Arousal                  | 0.55[0.52-0.57] | 0.52[0.49-0.55] | 0.55[0.52-0.58] |     |
| Average                  | 0.67±0.09       | 0.63±0.09       | 0.63±0.10       |     |
Regression-MAE(↓)
| Apnea/HypopneaIndex>3% | 12.97[11.87-14.05] | 13.07[11.92-14.25] | 12.86[11.79-13.94] |     |
| ---------------------- | ------------------ | ------------------ | ------------------ | --- |
| Apnea/HypopneaIndex>4% | 10.56[9.59-11.62]  | 10.79[9.85-11.83]  | 10.65[9.62-11.68]  |     |
| GestationAge           | 6.05[5.91-6.17]    | 6.10[5.94-6.24]    | 6.17[6.02-6.30]    |     |
| SystolicBP(VV)         | 14.65[12.50-16.78] | 15.10[13.10-17.21] | 14.95[12.87-17.01] |     |
| DiastolicBP(VV)        | 8.29[6.61-10.22]   | 9.20[6.93-11.12]   | 8.95[6.72-10.95]   |     |
| SystolicBP(PPG-BP)     | 14.39[12.53-16.45] | 16.70[14.25-19.38] | 16.20[13.73-18.85] |     |
| DiastolicBP(PPG-BP)    | 8.71[7.18-10.01]   | 9.48[8.24-10.90]   | 9.32[7.90-10.69]   |     |
| AverageHR              | 4.00[3.34-4.67]    | 4.76[3.94-5.86]    | 4.71[3.86-5.60]    |     |
| HR                     | 11.53[11.40-11.66] | 12.86[12.73-12.99] | 12.20[12.07-12.34] |     |
| Average                | 10.12±3.47         | 10.89±3.73         | 10.76±3.57         |     |
D.4 STATISTICALSIGNIFICANCEOFMODELCOMPARISON
Inadditiontoconfidenceintervals,weperformthefollowingstepstoevaluatethesignificanceacross
modelsonapertaskbasis(Tables3&4).First,werantheFriedmannChiSquaretest,andidentified
statistically significant differences across PAPAGEI and the baseline models at p < 0.05. Next,
we created critical difference (CD) diagrams to rank the best performing models, as suggested by
the literature to compare models over multiple datasets6 (Demsˇar, 2006). The CDs indicate that
PAPAGEI performs the best across both classification and regression tasks. Furthermore, it has a
statisticallysignificantaveragerankasindicatedbythelackofhorizontalline.
6https://scikit-posthocs.readthedocs.io/en/latest/tutorial.html#
critical-difference-diagrams
25

PublishedasaconferencepaperatICLR2025
| Table14: | PAPAGEIcomponentablationstudyresults. |      |          |          |      |
| -------- | ------------------------------------- | ---- | -------- | -------- | ---- |
|          |                                       | sVRI | sVRI+SQI | sVRI+IPA | Full |
Classification-AUROC(↑)
| ICUAdmission   |     | 0.79 | 0.75 | 0.78 | 0.79 |
| -------------- | --- | ---- | ---- | ---- | ---- |
| Mortality      |     | 0.67 | 0.65 | 0.67 | 0.67 |
|                |     |      | 0.61 |      | 0.61 |
| Smoker         |     | 0.59 |      | 0.60 |      |
| Pregnancystage |     | 0.78 | 0.73 | 0.72 | 0.78 |
| Hypertension   |     | 0.77 | 0.72 | 0.75 | 0.77 |
0.70
| SleepDisorderedBreathing |     | 0.62 | 0.53 | 0.64 |      |
| ------------------------ | --- | ---- | ---- | ---- | ---- |
| MoodDisturbance          |     | 0.53 | 0.56 | 0.55 | 0.56 |
| Valence                  |     | 0.54 | 0.55 | 0.53 | 0.56 |
| Arousal                  |     | 0.44 | 0.51 | 0.49 | 0.55 |
Regression-MAE(↓)
| Apnea/HypopneaIndex>3% |     | 13.36 | 13.74 | 13.42 | 12.97 |
| ---------------------- | --- | ----- | ----- | ----- | ----- |
| Apnea/HypopneaIndex>4% |     | 11.01 | 11.43 | 11.29 | 10.56 |
| GestationAge           |     | 6.18  | 6.32  | 6.15  | 6.05  |
| SystolicBP(VV)         |     | 14.62 | 15.97 | 15.33 | 14.65 |
| DiastolicBP(VV)        |     | 8.32  | 8.76  | 9.04  | 8.29  |
| SystolicBP(PPG-BP)     |     | 15.03 | 14.39 | 16.15 | 14.39 |
| DiastolicBP(PPG-BP)    |     | 9.12  | 8.76  | 9.06  | 8.71  |
| AverageHR              |     | 4.00  | 5.88  | 4.26  | 4.00  |
| HR                     |     | 11.51 | 11.97 | 11.88 | 11.53 |
Classification: Critical difference diagram of average score ranks
| 0.2 0.3      | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 0.9       |
| ------------ | --- | --- | --- | --- | ------------- |
| Regle (0.22) |     |     |     |     | (0.9) PaPaGei |
Stat. Features (0.4) (0.66) Chronos
| BYOL (0.51)   |     |     |     |     | (0.65) Moment |
| ------------- | --- | --- | --- | --- | ------------- |
| SimCLR (0.54) |     |     |     |     | (0.62) TF-C   |
Figure22: CriticalDifferenceDiagramforClassificationTasks. Theaxisrepresentstheaverage
rank of the model. The horizontal connector lines indicate no significant differences between the
models.
From the critical difference diagrams we observe that PAPAGEI is significantly better across clas-
sification(Figure22)andregression(Figure23)tasks. ThisarisesbecausePAPAGEIisthehighest
rankingmodelacrossmosttasks. Furthermore,weobserveMomentisastrongmodelacrossboth
classificationandregressiontasks. WhereasChronosandTF-Cperformwellforclassificationtasks
only.
We conduct additional statistical significance comparisons using a structured approach. First, we
randomlysampleascorefromwithintheconfidenceintervalsforeachtaskacrossallmodels. Next,
Regression: Critical difference diagram of average score ranks
| 0.2 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 |
| ------- | --- | --- | --- | --- | --- |
PaPaGei (0.19) (0.81) Stat. Features
SimCLR (0.48) (0.81) Regle
Moment (0.5) (0.65) Chronos
BYOL (0.53) (0.53) TF-C
Figure 23: Critical Difference Diagram for Regression Tasks. The axis represents the average
rank of the model. The horizontal connector lines indicate no significant differences between the
models.
26

PublishedasaconferencepaperatICLR2025
weapplytheCDrankingproceduretothesampledscores.Thisprocessisrepeated1,000times,and
theranksareaveraged. TheentireexperimentisconductedfivetimesforTables3and4, withthe
results presented in Figure 24. The colored cells indicate that PAPAGEI is statistically significant
comparedtotherespectivemodelatp<0.05.OurfindingsshowthatPaPaGeiconsistentlyachieves
the best average rank, ranging between 0.82-0.90 for AUROC and 0.19-0.25 for MAE. Across 35
comparisons(PaPaGeivs. theothermodels,repeatedfivetimes),PaPaGeidemonstratessignificant
improvementsin30outof35AUROCcomparisonsand32outof35MAEcomparisons. Among
the baseline models, we acknowledge that Chronos and TF-C are strong competitors capable of
performingcomparablytoPAPAGEI.
serutaeF
.tatS
ELGER sonorhC tnemoM RLCmiS LOYB C-FT ieGaPaP
Methods (AUROC)
stnemirepxE
I
II
III
VI
V
0.46 0.26 0.57 0.53 0.54 0.6 0.65 0.89
0.38 0.21 0.67 0.58 0.5 0.69 0.65 0.84
0.34 0.23 0.77 0.65 0.56 0.54 0.5 0.87
0.54 0.19 0.63 0.61 0.54 0.45 0.61 0.9
0.47 0.26 0.68 0.57 0.5 0.51 0.68 0.82
serutaeF
.tatS
ELGER sonorhC tnemoM RLCmiS LOYB C-FT ieGaPaP
Methods (MAE)
stnemirepxE
I
II
III
VI
V
0.61 0.76 0.65 0.57 0.56 0.51 0.61 0.19
0.61 0.77 0.68 0.59 0.58 0.59 0.4 0.25
0.67 0.81 0.47 0.47 0.51 0.72 0.6 0.25
0.58 0.8 0.6 0.53 0.6 0.61 0.53 0.25
0.65 0.78 0.65 0.56 0.56 0.64 0.43 0.24
Figure24: Bootstraprankingrepeatedforfiveexperiments: AUROC(left)andMAE(right). Col-
oredcellsindicatethatPAPAGEIissignificanttothebaselineatp<0.05.
D.5 STATISTICALASSESSMENTBETWEENIPAANDSQI
Recall that we incorporate SQI to handle situations where the dicrotic notch cannot be computed
duetopoor-signalqualityordifferentmorphologies. Weperformedapermutationtest(Rice,2008)
to statistically evaluate PPG segments where IPA is unavailable. By splitting SQI values into no
IPAandIPAgroupsandtestingsignificanceover1000permutations,weobservedstatisticallysig-
nificantdifferences(p < 0.05)inbothmean(+0.18)andmedian(+0.32)SQIvalues,withtheIPA
group having larger SQI. These findings empirically motivate SQI’s ability to handle limited PPG
morphology.
E ADDITIONAL BASELINES: DEMOGRAPHICS & PPG MORPHOLOGY
FEATURES
In this section, we evaluate the effectiveness of demographics (Demo: age, sex) and PPG mor-
phology(sVRI,IPA,SQI)topredictbothregression(ridge)andclassification(logisticregression)
tasks: (1)AblationStudy: WecomparedPaPaGeiwiththreebaselines—demographicsalone,PPG
features alone, and demographics + PPG features. Our results show that while demographics is a
stronger baseline than statistical features, PaPaGei outperforms the demographics + PPG baseline
in14outof18tasks. (2)EffectofDemographics: WetrainedamodelcombiningPaPaGei-Swith
demographics. TheresultsindicatethatincorporatingdemographicfeatureswithPaPaGei-Screates
astrongermodelthanusingPaPaGei-Salone.
From Table 15, we observe the following classification performance (Positive is better): ICU
(+0.13), Mortality (+0.01), Smoker (-0.02), Pregnancy Stage (+0.22), Hypertension (0.00), SDB
(nodemographics),MoodDisturbance(-0.08),Valence(-0.01),Arousal(+0.04). RegressionTasks
(Negativeisbetter): AHI>3%(-1.43),AHI>4%(-1.61),gestationage(-1.54),SBP-VV(-0.31),
DBP-VV (-0.46), SBP (-0.11) , DBP (-0.65), Avg. HR (-4.07), HR (-2.93). PaPaGei-S performs
better for real-time sleep and cardiovascular outcomes such as sleep apnea, heart rate and blood
pressure,respectively. Inparticular,wenoticethatoutcomessuchasheartratebenefitsubstantially
from PPG rather than demographics. Demographics are useful in tasks without real-time depen-
dencesuchassmoking,whichisestablishedtobeassociatedwithageandsex(Chungetal.,2020).
27

PublishedasaconferencepaperatICLR2025
Table15: Demographics&PPGMorphologyBaselineResults.
Stat.Features Demo PPG Demo+PPG PAPAGEI-Sor-P PAPAGEI-S+Demo
Classification-AUROC(↑)
ICUAdmission 0.71[0.65-0.78] 0.64[0.60-0.68] 0.59[0.54-0.64] 0.66[0.61-0.70] 0.79[0.75-0.82] 0.77[0.74-0.81]
Mortality 0.57[0.54-0.61] 0.66[0.61-0.69] 0.57[0.53-0.61] 0.66[0.61-0.69] 0.67[0.63-0.70] 0.70[0.67-0.74]
Smoker 0.63[0.58-0.67] 0.64[0.59-0.70] 0.56[0.52-0.62] 0.66[0.61-0.71] 0.64[0.58-0.69] 0.62[0.56-0.68]
Pregnancystage 0.64[0.62-0.67] 0.52[0.50-0.55] 0.55[0.53-0.57] 0.56[0.53-0.58] 0.78[0.75-0.80] 0.78[0.76-0.80]
Hypertension 0.66[0.47-0.83] 0.77[0.65-0.88] 0.53[0.40-0.68] 0.77[0.65-0.88] 0.77[0.68-0.87] 0.80[0.70-0.89]
SDB 0.32[0.14-0.55] – 0.46[0.31-0.62] – 0.70[0.57-0.84] –
MoodDisturbance 0.54[0.31-0.77] 0.54[0.30-0.80] 0.64[0.42-0.85] 0.63[0.36-0.87] 0.56[0.33-0.77] 0.52[0.25-0.78]
Valence 0.52[0.49-0.55] 0.57[0.54-0.60] 0.44[0.41-0.47] 0.57[0.54-0.60] 0.56[0.54-0.59] 0.55[0.53-0.58]
Arousal 0.55[0.53-0.58] 0.54[0.52-0.58] 0.51[0.48-0.54] 0.54[0.52-0.58] 0.58[0.55-0.61] 0.58[0.54-0.59]
Regression-MAE(↓)
Apnea/HypopneaIndex>3% 15.31[13.63-17.14] 14.53[13.29-15.84] 15.09[14.01-16.54] 14.40[13.12-15.61] 12.97[11.87-14.05] 12.35[11.27-13.46]
Apnea/HypopneaIndex>4% 12.52[10.92-14.14] 12.28[11.19-13.39] 12.65[11.57-13.83] 12.17[11.10-13.39] 10.56[9.59-11.62] 10.47[9.53-11.50]
GestationAge 7.15[6.99-7.34] 7.69[7.61-7.77] 7.61[7.51-7.70] 7.59[7.51-7.68] 6.05[5.91-6.17] 6.02[5.88-6.17]
SystolicBP(VV) 15.76[13.67-18.36] 14.96[13.21-17.35] 15.82[13.48-18.31] 15.01[13.30-17.86] 14.65[12.50-16.78] 14.27[11.92-16.44]
DiastolicBP(VV) 9.75[7.16-11.27] 8.75[6.48-9.77] 9.20[7.21-10.71] 8.78[7.10-10.25] 8.29[6.61-10.22] 8.26[6.64-10.16]
SystolicBP(PPG-BP) 15.50[11.68-20.25] 13.71[11.33-15.95] 15.76[13.36-18.30] 13.74[11.37-16.09] 13.60[10.65-16.51] 13.20[11.47-15.66]
DiastolicBP(PPG-BP) 9.35[7.44-11.66] 9.26[7.89-10.68] 9.36[7.95-10.92] 9.28[8.00-10.56] 8.71[7.18-10.01] 8.61[7.34-9.88]
AverageHR 7.01[5.48-8.89] 9.12[7.86-10.61] 8.07[6.60-9.71] 8.23[6.82-9.78] 3.47[2.74-4.32] 4.00[3.35-4.73]
HR 13.07[12.90-13.23] 15.18[15.03-15.33] 16.75[16.60-16.90] 14.46[14.32-14.62] 10.92[10.80-11.04] 12.38[11.90-12.96]
Importantly, demographics do not add much to already homogeneous populations. For example,
consider the NuMoM2B dataset which has women within a specific age range. Here, we observe
thatPaPaGeiobtainsmuchhigherAUROCandMAEthanthesupervisedbaselines.
Furthermore, We observe that adding demographics to PaPaGei-S embeddings improves over Pa-
PaGeiinthefollowingtasks: Mortality(+0.03),Hypertension(+0.03),AHI>3%(-0.62),AHI>
4%(-0.09),gestationage(-0.03),SBPVV(-0.38),DBPVV(-0.03),SBP(0.40),DBP(0.10).Based
on these results, PaPaGei-S + Demois a stronger modelin many cases. Importantly, these results
indicatethatPaPaGei-Sembeddingslearnfeaturesthatarecomplementarytodemographicsarenot
simplyproxiesforageorsex. However,itisimportanttonotethatwhiledemographicfeaturescan
bevaluableforpersonalization,theymaynotalwaysbereadilyavailable,andinreality,wecannot
usetheminisolationtopredictreal-timeoutcomessuchasbloodpressureorheartrate. Therefore,
ourPaPaGeimodelsaredesignedtofunctioneffectivelywithreal-timesensordataalone,ensuring
theirapplicabilityinsituationswherecompletedemographicinformationisnotaccessible.
Thesefindingsunderscoreanimportantpoint: demographicfeaturesarenotcompetingwithPa-
PaGeibutrathercomplementit,aspreviouslyestablishedinstudiesincludingdemographicswith
sensordata(Spathisetal.,2022). ThishighlightsthesynergisticpotentialofcombiningPaPaGei’s
advancedfeatureextractionwithdemographiccontextforimprovedtaskperformance.
Predicting Demographics Targets. Using the PAPAGEI features, we predict downstream demo-
graphics such as age and sex (Table 16). PAPAGEI-S achieves 7.78 MAE in age regression, 0.85
accuracy in age classification, and 0.79 accuracy in sex classification. Although our results trail
larger closed studies (Abbaspourazad et al., 2023) by 2.18, 0.05, and 0.13 for segment-level SSL,
and by 5.59, 0.12, and 0.25 for patient-level SSL, they mark an advancement in open-source ef-
forts. The superior performance of Abbaspourazad et al. (2023) can be attributed to two primary
factors. First,thepatient-levelpositivepairstrategyachievesthebestperformanceacrossalltasks.
This approach encourages the model to form distinct clusters for each patient, effectively captur-
ing demographic factors such as age and sex. In contrast, a segment-level approach pushes the
modeltoclustersimilarsegmentsacrossindividualswithvaryingdemographics,potentiallymixing
demographic-specific information. Second, the single-device setup with a larger dataset is useful
foreffectivemodeltraining(Table17). Conversely, ourevaluation, whichspansthreedevicesand
utilizessmallerdatasets,musthandlegreaterdataheterogeneity,thusmakingitmorechallenging.
F ADDITIONAL PREDICTION PLOTS
TheregressionplotstoevaluatetheagreementbetweentrueandpredictedvaluesinshowninFigure
25. FromtheFigure,weobservethatPAPAGEI’spredictionsaremorealignedtothetruevaluesfor
AHI > 3% (R2 = 0.28), Avg. HR (R2 = 0.79), gestation age (R2 = 0.28), SBP (R2 = 0.36),
andDBP(R2 =0.22). Moreover,fromthedistributionplotsinFigure25,wenoticethatPAPAGEI
hasstrongeroverlapforAHI>4%,Avg. HRandDBP,indicatingitsabilitytocapturethetailsfor
28

PublishedasaconferencepaperatICLR2025
Table16: Predictingpersonalcharacteristicswithembeddings. Downstreampredictiononage
regression, age classification, and sex classification in our pre-training datasets (VitalDB, MESA,
MIMIC-III).TheregressionandclassificationtasksarereportedusingMAEandAUROC,respec-
tively. Note: trainingandtestingareconductedwithcompletelydifferentcohortsinthetwostudies,
hencecomparisonsaredifficult.
Study AgeRegression(↓) AgeClassification(↑) SexClassification(↑)
| Abbaspourazadetal.(2023)(Patient) |     | 3.19 | 0.97 | 0.99 |
| --------------------------------- | --- | ---- | ---- | ---- |
| Abbaspourazadetal.(2023)(Segment) |     | 6.60 | 0.90 | 0.87 |
PAPAGEI-S(Ours) 8.78[8.47-8.09] 0.85[0.83-0.87] 0.74[0.72-0.76]
Table17:Comparisonoflarge-scalePPGstudies. *indicatespartialavailability. Theparticipants
andhoursindicatepre-trainingdata.
Study #Participants(#Hours) #Devices(Types) OpenData OpenWeights OpenCode #Tasks(#Datasets)
|                          |                   |                                  | ✗ ✗  | ✗        |
| ------------------------ | ----------------- | -------------------------------- | ---- | -------- |
| Abbaspourazadetal.(2023) | 141,207(333K)     | 1(Smartwatch)                    |      | >46(1)   |
| Dingetal.(2024)          | 28,539(300K)      | 5-6(ICU,Smartwatch)              | ✗* ✗ | ✓ 4(7)   |
| Yunetal.(2024)           | 170,714(Varying)7 | 1(Finger)                        | ✗ ✓  | ✓* 2(4)  |
|                          |                   | 7 ( I C U , S m a rt w at c h    | ,    |          |
| PAPAGEI(Ours)            | 13,517(57K)       |                                  | ✓ ✓  | ✓ 20(10) |
|                          |                   | F i n g e r, ” P ho n e O x . ”) |      |          |
thesetasks. Interestingly,wenoticethatallmodelsareunabletocapturethebi-modalnatureofthe
gestationagemeasurements. Here,Chronosperformsbetterthanothermethodstocapturereadings
fromthefirstvisit.
| G EFFECT OF | SKIN TONE |     |     |     |
| ----------- | --------- | --- | --- | --- |
We present the skin tone analysis in a more granular way in Figure 26. Here, PAPAGEI-S clearly
performs better than PAPAGEI-P in most cases. Overall, we notice that PAPAGEI-S is good for
lighter skin tones in the 1-2 range for SBP and 2-3 range for DBP. While PAPAGEI-S does not
performthebestfordarkerskintones,it’sperformanceiscomparabletoothermodelsforskintone
ratings of 4 and 5. Overall, these results indicate that PAPAGEI-S is relatively robust to skin tone
variations,andthatadditionalfutureworkisneededtomakeitbetterdarkerskintones.
| H EXTENDED | RELATED WORK |     |     |     |
| ---------- | ------------ | --- | --- | --- |
Self-supervisedlearning(SSL)isthemostprominentparadigmforlearninggeneralrepresentations
from large unlabeled datasets, including methods like SimCLR (Chen et al., 2020), BYOL (Grill
etal.,2020),andmaskedautoencoders(MAE)(Heetal.,2022). Timeseries-specificobjectiveslike
TNC and TF-C have also shown promise (Tonekaboni et al., 2021; Zhang et al., 2022). SSL has
gained traction in the domain of physiological signal analysis, with applications to health records
(Chenetal.,2021;Ye`cheetal.,2021),fitnessandpersonalization(Spathisetal.,2021),aswellas
brain(Chengetal.,2020)andheartsignals(Kiyassehetal.,2021;Sarkar&Etemad,2020).
However, despite the popularity of SSL, there are no widely used FMs for PPG data. While (Ab-
baspourazad et al., 2023) showcased the potential of foundation models for physiological signals,
it was based on a single proprietary dataset and device (Apple Watch) while the models were not
released,limitingitspracticaluseintheresearchcommunity. Similarly,REGLE’swork(Yunetal.,
2024)ontheUKBiobankdatasetshowedthatembeddingPPGsignalscanimprovegeneticdiscov-
eryandriskpredictionoutcomes.Althoughpartsofthatmodelandpipelinearepublic,thedatasetis
notopenlyaccessible,andtheprimarygoalwasnottocreateafoundationmodelforPPGbutrather
tofocusongenetics. AnotherworkonthesamedatashowedthatPPGembeddingsarepromising
forcardiovascularriskprediction(Wengetal.,2024). SiamQuality(Dingetal.,2024)alsotrained
anunreleasedmodelon36millionPPGsignalsusingproprietarydata. Importantly, mostofthese
workspre-trainedonasingle-devicedatasetanddidnotexploreout-of-domaindatasetsorconduct
transferlearningexperiments,whicharecrucialforassessingthetruegeneralizabilityoffoundation
7https://biobank.ndph.ox.ac.uk/crystal/field.cgi?id=4205
29

PublishedasaconferencepaperatICLR2025
|     | Chronos |     | SimCLR |     | PaPaGei-S |     |     |     |     |     |     |
| --- | ------- | --- | ------ | --- | --------- | --- | --- | --- | --- | --- | --- |
%4 > IHA detciderP
100
|     |     |     | 100 |     | 100 |     | 0.06 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
AHI > 4%
|     | m=0.16     |     | m=0.14  |     | m=0.27  |     |              |     |     |     | Chronos |
| --- | ---------- | --- | ------- | --- | ------- | --- | ------------ | --- | --- | --- | ------- |
|     | 50 R2=0.16 |     | R2=0.13 |     | R2=0.28 |     | ytisneD 0.04 |     |     |     |         |
|     |            |     | 50      |     | 50      |     |              |     |     |     | SimCLR  |
PaPaGei-S
0.02
|     | 0   |     | 0   |     | 0   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.00
|     | 0 50          | 100 | 0             | 50 100 | 0             | 50 100 | 20  | 0 20 | 40 60    | 80 100 | 120 |
| --- | ------------- | --- | ------------- | ------ | ------------- | ------ | --- | ---- | -------- | ------ | --- |
|     | True AHI > 4% |     | True AHI > 4% |        | True AHI > 4% |        |     |      | AHI > 4% |        |     |
(a)AHI>4%predictions
Moment
| RH .gva detciderP | 100     |     | 100 BYOL |     | 100 PaPaGei-P |     |              |     |     |     |         |
| ----------------- | ------- | --- | -------- | --- | ------------- | --- | ------------ | --- | --- | --- | ------- |
|                   | m=0.68  |     | m=0.67   |     | m=0.92        |     |              |     |     |     |         |
|                   | R2=0.68 |     |          |     |               |     | 0.04         |     |     |     | Avg. HR |
|                   |         |     | R2=0.65  |     | R2=0.79       |     |              |     |     |     |         |
|                   | 80      |     | 80       |     | 80            |     | ytisneD 0.03 |     |     |     | Moment  |
BYOL
|     |     |     |     |     |     |     | 0.02 |     |     |     | PaPaGei-P |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --------- |
|     | 60  |     | 60  |     | 60  |     | 0.01 |     |     |     |           |
0.00
|     | 60           | 80 100 | 60           | 80 100 | 60           | 80  | 100 40 | 50 60 | 70 80   | 90  | 100 110 |
| --- | ------------ | ------ | ------------ | ------ | ------------ | --- | ------ | ----- | ------- | --- | ------- |
|     | True avg. HR |        | True avg. HR |        | True avg. HR |     |        |       | Avg. HR |     |         |
(b)Avg.HRpredictions
|                         |         |     | BYOL    |     | PaPaGei-S |               |     |     |     |     |               |
| ----------------------- | ------- | --- | ------- | --- | --------- | ------------- | --- | --- | --- | --- | ------------- |
| egA noitatseG detciderP |         | 50  |         | 50  |           |               |     |     |     |     |               |
| 50                      | Chronos |     | m=0.22  |     | m=0.25    |               |     |     |     |     |               |
|                         | m=0.31  | 40  |         | 40  |           |               |     |     |     |     |               |
| 40                      |         |     | R2=0.19 |     | R2=0.28   |               |     |     |     |     |               |
|                         | R2=0.28 | 30  |         | 30  |           | 0.100         |     |     |     |     | Gestation Age |
| 30                      |         |     |         |     |           |               |     |     |     |     | Chronos       |
|                         |         | 20  |         | 20  |           | ytisneD 0.075 |     |     |     |     |               |
| 20                      |         |     |         |     |           |               |     |     |     |     | BYOL          |
|                         |         | 10  |         | 10  |           | 0.050         |     |     |     |     | PaPaGei-S     |
10
0.025
|     | 0                  | 0   |                    | 0   |                    | 0.000 |                    |       |     |     |     |
| --- | ------------------ | --- | ------------------ | --- | ------------------ | ----- | ------------------ | ----- | --- | --- | --- |
|     | 0 20               | 40  | 0 20               | 40  | 0 20 40            |       |                    |       |     |     |     |
|     | True Gestation Age |     | True Gestation Age |     | True Gestation Age |       | 10 0 Gestation Age | 10 20 | 30  | 40  |     |
(c)GestationAge
| )PB-GPP( PBS detciderP | Moment            |     |                   |      |                   |     |              |                      |     |                      |     |
| ---------------------- | ----------------- | --- | ----------------- | ---- | ----------------- | --- | ------------ | -------------------- | --- | -------------------- | --- |
|                        | 180               |     | 180               | TF-C | 180 PaPaGei-P     |     |              |                      |     |                      |     |
|                        | 160 m=0.31        |     | 160               |      | 160               |     |              |                      |     |                      |     |
|                        |                   |     | m=0.19            |      | m=0.29            |     | 0.04         |                      |     | Systolic BP (PPG-BP) |     |
|                        | 140 R2=0.07       |     | R2=0.13           |      | R2=0.36           |     |              |                      |     |                      |     |
|                        |                   |     | 140               |      | 140               |     | ytisneD 0.03 |                      |     | Moment               |     |
|                        | 120               |     |                   |      |                   |     |              |                      |     | TF-C                 |     |
|                        |                   |     | 120               |      | 120               |     | 0.02         |                      |     | PaPaGei-S            |     |
|                        | 100               |     | 100               |      | 100               |     | 0.01         |                      |     |                      |     |
|                        | 80                |     | 80                |      | 80                |     | 0.00         |                      |     |                      |     |
|                        | 100               | 150 | 100               | 150  | 100               | 150 |              |                      |     |                      |     |
|                        | True SBP (PPG-BP) |     |                   |      |                   |     | 60           | 80 100 120           | 140 | 160 180              | 200 |
|                        |                   |     | True SBP (PPG-BP) |      | True SBP (PPG-BP) |     |              | Systolic BP (PPG-BP) |     |                      |     |
(d)SystolicBP(PPG-BP)
)PB-GPP( PBD detciderP
|     | 120 Moment |      | BYOL    |     | PaPaGei-P |     |       |     |     |                       |     |
| --- | ---------- | ---- | ------- | --- | --------- | --- | ----- | --- | --- | --------------------- | --- |
|     |            |      | 120     |     | 120       |     |       |     |     |                       |     |
|     | m=0.15     |      | m=0.08  |     | m=0.25    |     |       |     |     |                       |     |
|     | 100 R2=    | 0.03 | R2=0.05 |     | R2=0.22   |     | 0.100 |     |     |                       |     |
|     |            |      | 100     |     | 100       |     |       |     |     | Diastolic BP (PPG-BP) |     |
|     |            |      |         |     |           |     | 0.075 |     |     | Moment                |     |
ytisneD
|     | 80  |     | 80  |     | 80  |     | 0.050 |     |     | BYOL |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ---- | --- |
PaPaGei-P
|     | 60  |     | 60  |     | 60  |     | 0.025 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
0.000
|     | 50 75             | 100 | 50 75             | 100 | 50 75             | 100 | 40  | 60                    | 80  | 100 | 120 |
| --- | ----------------- | --- | ----------------- | --- | ----------------- | --- | --- | --------------------- | --- | --- | --- |
|     | True DBP (PPG-BP) |     | True DBP (PPG-BP) |     | True DBP (PPG-BP) |     |     | Diastolic BP (PPG-BP) |     |     |     |
(e)DiastolicBP(PPG-BP)
Figure 25: Regression plots and prediction distribution of different models compared to ground
truthfor(a)Apnea/HypopneaIndex>4%,(b)AverageHeartRate,(c)GestationAge,(d)Systolic
BP(PPG-BP),and(e)DiastolicBP(PPG-BP).R2
isthecoefficientofdeterminationandmisthe
correlationslope.
30

PublishedasaconferencepaperatICLR2025
30
25
20
15
10
5
0
1 (Pale white) 2 (Fair) 3 (Darker White)4 (Light Brown) 5 (Brown) 6 (Black)
Fitzpatrick Skin Tone Scale
EAM
Systolic BP (VV)
REGLE
Chronos
Moment
SimCLR
BYOL
TF-C
PaPaGei-P
PaPaGei-S
12.5
10.0
7.5
5.0
2.5
0.0
1 (Pale white) 2 (Fair) 3 (Darker White)4 (Light Brown) 5 (Brown) 6 (Black)
Fitzpatrick skin tone scale
EAM
Diastolic BP (VV)
REGLE
Chronos
Moment
SimCLR
BYOL
TF-C
PaPaGei-P
PaPaGei-S
Figure26: DetailedskintoneanalysisforBloodPressureestimation(VVdataset).
models. ThesestudieshighlightthepotentialofPPG-basedfoundationmodelsbutalsounderscore
theneedforopenlyavailable,pre-trainedmodelsthatcanbewidelyusedandadaptedbytheresearch
community.
Ontheotherhand,generictimeseriesfoundationmodelshavebeguntogainpopularity,mirroring
thetrendseeninLargeLanguageModels(LLMs).Thesemodelsarepre-trainedonmassivecorpora
of diverse time series data, aiming to learn universal representations that can be applied across
variousdomains.Forinstance,Chronos(Ansarietal.,2024)wastrainedonanimpressive84billion
observations (analogous to tokens in NLP) from 28 distinct datasets. However, it’s notable that
this diverse collection does not include physiological data. Similarly, Moment (Goswami et al.,
2024) was trained on billions of observations from a wide-ranging dataset that includes weather,
traffic,energy,andotherdomains. WhileMomentdoesincorporateasmallamountofECGdata,it
comprisesonlyatinypercentageoftheoveralldatapool.
Incontrasttothesegenericapproaches,ourworktakesadomain-specificfocus. Wecuratealarge
pre-trainingandevaluationbenchmarkdedicatedexclusivelytoPPGdata. Whileknowledgegained
from generic time series foundation models may transfer to domain-specific tasks like PPG, we
expect the performance to be limited compared to a model trained specifically on PPG data. Fur-
thermore,foundationmodelsforECG(McKeenetal.,2024;Songetal.,2024)orEEG(Yuanetal.,
2024b)haveshownpromisebuttransferringfromonedomain-specificmodel(e.g.,ECG)toanother
(PPG) is likely to be even more challenging, as the underlying signal characteristics can be quite
different. Forinstance, Laietal.(2023)trainedalarge-scale12-leadECGmodelfordetecting60
diagnostic terms, while McKeen et al. (2024) developed an open-source ECG FM using 1.6 mil-
lion12-leadsignals. Inbrainsignalanalysis, Yuanetal.(2024b)introducedBrant-2, anEEGand
SEEG model supporting tasks like sleep staging and seizure detection. Building on this progress,
weadoptadomain-specificapproachfocusedonphotoplethysmography(PPG)signals.Buildingon
the increasing interest in modality-specific foundation models, our specialized approach allows us
tocapturenuancesandcomplexitiesspecifictoPPGsignals.
An increasingly popular approach involves feeding timeseries data and prompts directly to Large
LanguageModels(LLMs)(Gruveretal.,2024). However,despitepromisingresults,LLMsstrug-
glewithhigh-dimensionalsignalsduetotheirtext-basedprocessing(Spathis&Kawsar,2024). A
modality-specific encoder like PAPAGEI addresses this limitation by providing representations of
31

PublishedasaconferencepaperatICLR2025
raw signals (Belyaeva et al., 2023), which can be combined with text and fed into more powerful
multimodalfoundationmodels,suchasAnyMAL(Moonetal.,2023). Thisapproachoffersseveral
advantages: computational efficiency through a fixed LLM, flexibility due to the modular design
ofencoder,adapter,andLLMcomponents,andinteroperabilitywithotherhigh-performingmodels
(e.g., a state-of-the-art IMU encoder (Yuan et al., 2024a)). Crucially, this encoder-LLM approach
doesnotrequirepaireddatawithothermodalitiestotrainasinglemultimodalmodel. However,it
may introduce complexity by limiting end-to-end gradient propagation and reduce interpretability
in encoder-LLM communication compared to natural language prompts. Despite these trade-offs,
PAPAGEIservesdualpurposes: asagenericfeatureextractorforvariousPPGsignalsandapplica-
tions,andasamodalityencoderinnext-generationfrontiermodels. Thisversatilitypositionsitasa
valuabletoolforadvancingmultimodalsensoryAIsystems.
I EXTENDED DISCUSSION
In§5.1,weobservedthatPAPAGEIoutperformsbaselinesinatleast14outof20tasks,withaverage
classificationandregressionimprovementsof4.7%-6.3%and2.9%-4.9%,respectively. PAPAGEI-
S performed best for cardiovascular parameters like BP, Hypertension, and Avg. HR, which are
closely linked to metrics such as sVRI and IPA (Liang et al., 2018b). Additionally, PAPAGEI-P
surpassedbaselinesFMslikeMomentandiswell-suitedfortaskssuchasSmokingandArousal.
By ablating different components of PAPAGEI-S (Section 5.2), we found that the full model per-
forms best, with sVRI contributing the most. Adding IPA or SQI separately did not improve per-
formance, suggesting that (a) IPA and SQI positively transfer in a multi-task setup, and (b) our
designchoicetoincludebothtocompensateforsituationswhereIPAcannotbecomputediseffec-
tive(Section3.2). WhilecombiningPAPAGEI-PandPAPAGEI-Smayseemintuitive,constraining
positivepairsonbothsVRIandparticipantsleadstotoomanyuniquelabelswithlimitedsamples.In
ourscalabilityanalysis,weobservedthatthesmallestmodel(5Mparameters)outperformedothers,
aligningwithotherstudiesusingCNNswith3.3Mparametersforbiosignals(Abbaspourazadetal.,
2023),likelyduetothesizeofPPGdatasets.LargermodelslikeChronosorMomentareimpractical
forwearablesduetotheirsizeandprivacyconcernswithcloud-basedinferenceforhealthdata. Ad-
ditionally,PAPAGEI-Sismoredata-efficientforlinearprobing,showinggreaterperformancegains
withincreaseddataavailability,makingitapromisingbackboneforsmallstudiesinfutureresearch.
Our studies in Section 5.3 reveal that PAPAGEI-S embeddings are more dispersed across partici-
pants,enhancingperformance,whileregressionpredictionsmoreaccuratelyreflectthetruedistribu-
tion. Weattributethistoourpositivepairselection,whichchoosespositivepairsacrossindividuals
basedonsVRI.Moreover,ourskintoneanalysisshowsthatthemethodperformsbetteronlighter
skintones,likelyduetothemodelbeingtrainedpredominantlyonsuchdata. Fordarkerskintones,
performancewassimilaracrossmodelsfordiastolicBP,withREGLEandBYOLperformingbest,
highlightingtheneedforfutureworkcreatingmorerobustmodelsfordiverseskintones.
To provide future direction regarding the use of PAPAGEI, we provide some suggestions. For in-
stance,let’sconsiderthenuMoM2Bdatasetwhichconsistsofpregnantwomen. PAPAGEI-Sobtains
anAUROCof0.78inpregnancystageclassificationand6.05isgestationageclassification. Com-
paredtothepre-trainingpopulationwithdiverseageandgender,thenuMoM2Bconsistsofwomen
generallyagedbetween20-35. Furthermore,thegestationagereadingsarecollectedapproximately
aroundthefirstandthirdtrimester. Giventhesefactors,thetargetnuMoM2Bdatasethasmanyvari-
ablescontributingtowarddistributionshift. Therefore,PaPaGei-Scanbefine-tunedtoaddressthe
shiftinthefollowingways: (1)Wecanalignthepre-trainedembeddingstothenuMoM2Bembed-
dingusingunsupervisedorsemi-superviseddomainadaptation. (2)DomainGeneralizationisalso
anoptionduringthetrainingphasetoimprovegeneralizationrobustness. (3)Newermethodssuch
asLoRAcanprovideanotherwaytoquicklyfine-tune. (4)Importantly,giventhatmorewomenare
present in the first visit compared to the third visit, we can optimize different metrics to improve
accuracyundertheimbalance. Forexample,AUPRCcanbeoptimizedinsteadofAUROC.Fairness
ofclassificationacrossgenderscanalsobeconsideredduringtraining. Exploringtheseavenuesto
further enhance the performance and applicability of PaPaGei is a promising direction for future
studies. Moreover, future work may benefit from exploring PPG specific augmentations such as
GAN-basedapproaches(Kiyassehetal.,2020); andsystematicallyevaluatingdifferentaugmenta-
tionstoprovideinsightsintousefulPPGaugmentations.
32