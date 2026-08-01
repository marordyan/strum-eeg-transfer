ORIGINALRESEARCH
published:23June2021
doi:10.3389/fnhum.2021.653659
BENDR: Using Transformers and a
Contrastive Self-Supervised Learning
Task to Learn From Massive
Amounts of EEG Data
DemetresKostas1,2*,StéphaneAroca-Ouellette1,2andFrankRudzicz1,2,3
1DepartmentComputerScience,UniversityofToronto,Toronto,ON,Canada,2VectorInstituteforArtificialIntelligence,
Toronto,ON,Canada,3LiKaShingKnowledgeInstitute,St.Michael’sHospital,Toronto,ON,Canada
Deepneuralnetworks(DNNs)usedforbrain–computerinterface(BCI)classificationare
commonlyexpectedtolearngeneralfeatureswhentrainedacrossavarietyofcontexts,
suchthatthesefeaturescouldbefine-tunedtospecificcontexts.Whilesomesuccessis
foundinsuchanapproach,wesuggestthatthisinterpretationislimitedandanalternative
would better leverage the newly (publicly) available massive electroencephalography
(EEG) datasets. We consider how to adapt techniques and architectures used for
language modeling (LM) that appear capable of ingesting awesome amounts of data
Editedby:
toward the development of encephalography modeling with DNNs in the same vein.
SungChanJun,
GwangjuInstituteofScienceand We specifically adapt an approach effectively used for automatic speech recognition,
Technology,SouthKorea
which similarly (to LMs) uses a self-supervised training objective to learn compressed
Reviewedby:
representations of raw data signals. After adaptation to EEG, we find that a single
DalinZhang,
AalborgUniversity,Denmark pre-trainedmodeliscapableofmodelingcompletelynovelrawEEGsequencesrecorded
TomaszMaciejRutkowski, with differing hardware, and different subjects performing different tasks. Furthermore,
RIKENCenterforAdvanced
both the internal representations of this model and the entire architecture can be
IntelligenceProject(AIP),Japan
fine-tuned to a variety of downstream BCI and EEG classification tasks, outperforming
*Correspondence:
DemetresKostas priorworkinmoretask-specific(sleepstageclassification)self-supervision.
demetres@cs.toronto.edu
Keywords: brain computer interface, deep learning - artificial neural network, transformers, semi-supervised
Specialtysection: learning,contrastivelearning,convolutionalneuralnetwork,sequencemodeling
Thisarticlewassubmittedto
Brain-ComputerInterfaces,
asectionofthejournal 1. INTRODUCTION
FrontiersinHumanNeuroscience
Toclassifyrawelectroencephalography(EEG)usingdeepneuralnetworkmodels(DNNs),these
Received:14January2021
Accepted:23April2021 models need to both develop useful features from EEG signals and subsequently classify those
Published:23June2021 features. This frames both the promise and the challenge of using DNNs for supervised EEG
classification. On the one hand, it promises to almost entirely circumvent the need for feature
Citation:
KostasD,Aroca-OuelletteSand engineering, but on the other hand, both feature discovery and classification need to be learned
RudziczF(2021)BENDR:Using from a limited1 supply of (relevant) high-dimensional data. A paradigmatic way in which we
TransformersandaContrastive observethischallengeiswithbrain–computerinterface(BCI)applications2(Lotteetal.,2018;Roy
Self-SupervisedLearningTaskto etal.,2019;KostasandRudzicz,2020b).Shallowerneuralnetworkmodelshavetendedtobemore
LearnFromMassiveAmountsofEEG
Data. 1Considerthedifficultyofcollectingandlabeling100moreBCItrialsascomparedtothesamefor100moreimages.
Front.Hum.Neurosci.15:653659. 2ThoughwebelievethatitislikelythatasimilartendencytowhatwecharacterizehereinholdsformostapplicationsofDNNs
doi:10.3389/fnhum.2021.653659 outsideoftheircoreartificialintelligenceapplications.
FrontiersinHumanNeuroscience|www.frontiersin.org 1 June2021|Volume15|Article653659

Kostasetal. BENDR
effective classifiers than their deeper counterparts in BCI task) when considering raw data. In other words, the very
(markedly so when trained independently for each user) effort of selecting different features for different tasks (rather
(Schirrmeister et al., 2017; Lawhern et al., 2018; Lotte et al., than only changing classifier) is recognition of a difference in
2018; Roy et al., 2019; Kostas and Rudzicz, 2020b). With domain.Furthermore,wehavefoundinpreviousworkthatthe
these shallower networks, the range of learnable features is differentdomainsrepresentedbyparticularindividualsseemto
relatively limited. By design, they employ constrained linear be readily4 identifiable from arbitrary raw sequences of EEG
operations, and a limited few include non-linear activations usingDNNs(KostasandRudzicz,2020a).Insummary,aDNN
between subsequent layers (Kostas and Rudzicz, 2020b), an trained with a certain set of contexts (e.g., subjects), intent
otherwise crucial feature of DNN complexity. In prior work, on transferable performance to novel contexts (e.g., an unseen
we observed that if some inter-personal variability had been subject), is required to develop some universal features and/or
adjusted, the performance of shallower models more quickly classifier for possible novel target domains from the sources it
saturated to lower performance levels as compared to a deeper was prepared with. Some have argued that this universality is
networkalternative(KostasandRudzicz,2020b),suggestingthat achievable through the selection of the right DNN, or DNN
more complex raw-BCI-trial features could be developed using layers(CimtayandEkmekcioglu,2020;Zhangetal.,2020a),but
deeperneuralnetworkswhenusingtrainingdatathatwasmore throughaquestioningoftheapparentidealapproachestoTLin
consistent.Understooddifferently,overcomingthelimitationsof thewiderDNNliterature(presentedinsection1.1),wearguethat
shallowernetworksinfavorofdeeperDNNsthatcould surpass the development of such universal features requires developing
feature engineering approaches likely requires addressing the pre-trainingproceduresthattransferfromgeneraltaskstospecific
largevariabilitybetweendifferentcontexts. onesinstead.
A natural framework to understand this problem is transfer The interest in these universal, or invariant features are
learning (TL), which is an area of machine learning that aims not however limited to better classification performance, but
to leverage knowledge learned from one context such that it may be of wider importance. While it may be difficult to
maybeusefulinadifferentone.Considerasupervisedlearning determine within a DNN when “features” start and “classifier”
problem,whichconsistsoffirst,adomainD = {X,P(X)},itself begins, in applications such as computer vision there is a clear
arepresentationofafeaturespaceX (e.g.,thesetofallpossible understanding that nearly all transferrable DNNs have tended
rawEEGrecordingsofacertainlength)andtheprobabilityP(X) tolearn“low-level”featuresinearlierlayers(e.g.,edge-detector-
ofobservingaparticularconfigurationoffeatures(x ∈ X,e.g., like primitives) (Krizhevsky et al., 2012; Yosinski et al., 2015;
a particular observation of a raw EEG recording). Second, a Raghuetal.,2019).Thepromiseofsomesuchtransferableearly
taskT = {Y,f(x)},arepresentationofthepossiblelabelsfora layers or operations that are easily extended to any subject,
particular task,and a mapping f :X →Y thatmaps individual session, or task may open valuable lines of inquiry, or novel
instances to the correct labels. TL means to break down a explicit (rather than implicitly learned) methods (say if these
problemintosourceandtargetproblems,withD 6=D (and/)or earlylayersdoordonotcorrespondtoexistingmethodologies,
S T
T 6=T . respectively)ofanalysis.Importantly,thedeterminationofwhich
S T
EvidenceaboundsinBCIandEEGgenerallythatdifferences “low-level” features DNNs developed in computer vision was
in domain are a critical challenge. For example, under the revealedthroughmodelsthathadtransferableperformancefrom
sensory motor rhythm (SMR) BCI paradigm, different subjects generaltospecifictasks(Yosinskietal.,2015;Raghuetal.,2019).
exhibit extremely different capacities at performing this task, Inthiswork,wearguethatself-supervisedsequencelearning
and even different sessions from the same users can exhibit is such a general task. It would be an effective approach for
enough variation that classifiers trained in one session are ill- developing and deploying more complex and universal DNNs
suitedtothenext(VidaurreandBlankertz,2010;AhnandJun, inBCIandinpotentiallywiderEEG-basedanalysis.Wepresent
2015; Sannelli et al., 2019). This indicates that (at least for the a methodology that can learn from many people, sessions, and
feature representations being considered) the domain of each tasksusingunlabeled data;inotherwords,itsamplesthemore
person and even session differs. Beyond these inter- and intra- generaldistributionofEEGdata.Thus,weattempttolearnD
EEG
personal variations, different features are relevant for different withself-descriptivefeatures,withthegoalthattheyexhibitlittle
BCI tasks. Hand-selected features (sets possibly pruned later variability across typical context boundaries (invariant between
on) are also typically distinct under different BCI paradigms, expected domains) like dataset and subjects. More specifically,
as different features better discriminate different tasks3 (Lotte we investigate techniques inspired by language modeling (LM)
et al., 2018), e.g., P300 vs. SMR. Thus, an explicit imposition that have found recent success in self-supervised end-to-end
of difference in domain is imposed between different BCI task speechrecognitionandimagerecognitioninanefforttodevelop
paradigms (as their feature spaces are distinct, e.g., X 6= encephalography models (EM). We first begin by investigating
SMR
X ), which to us implies that it is fair to expect that this fully supervised transfer learning (which has been frequently
P300
is indicative of strong differences in domain (and of course looked to as an EEG/BCI TL solution), finding inconsistency
in the extension of computer vision-style pre-training to BCI
3While this is typical, some procedures, like covariance-based Riemannian
classificationschemes,donotnecessarilyneeddifferentfeaturesfordifferenttasks 4Withastronglatentrepresentation,anearest-neighborslabelingissufficienttobe
(Lotteetal.,2018;Zaninietal.,2018).Theseareaveryinterestingexceptiontothe nearly100%accurateforsomedatasets,despitebeingrecordingsmadeondifferent
argumentwedevelop. hardware(KostasandRudzicz,2020a).
FrontiersinHumanNeuroscience|www.frontiersin.org 2 June2021|Volume15|Article653659

| Kostasetal. |     |     |     |     |     |     |     |     |     |     |     |     |     | BENDR |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
tasks7.
(and by extension the data domain of EEG). We then evaluate This is noteworthy, as this is what makes ImageNet a
a simple adaptation of previous work in self-supervised speech general task. Evidence suggests that pre-training label diversity
recognitioncalledwav2vec 2.0(Baevskietal.,2020)toEEG. isimportantforeffectiveImageNettransferlearning(Huhetal.,
With this framework, arbitrary EEG segments are encoded as 2016),thoughanexcesscouldbedetrimental(Huhetal.,2016;
a sequence of learned vectors we call BErt-inspired Neural Ngiametal.,2018).Furthermore,thisgeneraltaskappearstobe
Data Representations (or “BENDR”). We ask whether BENDR responsible for developing the transferable early layers (Raghu
are transferable to unseen EEG datasets recorded from unseen etal.,2019;Neyshaburetal.,2020)thatwouldseemtoembody
subjects, different hardware, and different tasks, and how the desired goal of overcoming “hand-crafted” or developing
generally suitable BENDR are (both as-is or fine-tuned) to a “invariant” features, and partially appear to be learning data
batteryofdownstreamEEGclassificationtaskswithrespecttothe statistics (Neyshabur et al., 2020) [i.e., P(X); recall this as one
samearchitecturewithoutfirstbeingtrainedwithmoregeneral aspectofadomainforasupervisedlearningproblem,theother
EEGdata(i.e.,“pre-training”). isthefeaturerepresentation].Morefundamentally,however,this
|                   |     |     |      |      |     |     |     | pre-training | paradigm |         | has begun | to be       | questioned  | altogether, |
| ----------------- | --- | --- | ---- | ---- | --- | --- | --- | ------------ | -------- | ------- | --------- | ----------- | ----------- | ----------- |
|                   |     |     |      |      |     |     |     | with some    | work     | finding | that      | it does not | necessarily | improve     |
| 1.1. Pre-training |     |     | With | DNNs |     |     |     |              |          |         |           |             |             |             |
downstreamperformance,wherecommonlyithasbeenassumed
| For inspiration |         | on tackling | DNN        | transfer    |     | learning | in BCI,  |                |     |           |         |        |           |               |
| --------------- | ------- | ----------- | ---------- | ----------- | --- | -------- | -------- | -------------- | --- | --------- | ------- | ------ | --------- | ------------- |
|                 |         |             |            |             |     |          |          | that it should |     | (e.g., in | medical | images | or object | localization; |
| one can         | look to | other       | successful | approaches, |     | starting | with the |                |     |           |         |        |           |               |
thoughitspeedsuptrainingconsiderably)(Ngiametal.,2018;He
modern deeplearning(DL)“revolution,”whichwasusheredin
etal.,2019;Kornblithetal.,2019;Raghuetal.,2019).
| on the back   | of         | computer | vision | and image | recognition |            | (LeCun      |          |       |               |        |                |     |                |
| ------------- | ---------- | -------- | ------ | --------- | ----------- | ---------- | ----------- | -------- | ----- | ------------- | ------ | -------------- | --- | -------------- |
| et al., 2015; | Sejnowski, |          | 2020). | The       | successes   | of         | DL in these |          |       |               |        |                |     |                |
|               |            |          |        |           |             |            |             | 1.2. Are | There | Alternatives? |        |                |     |                |
| applications  | have       | stemmed  | from   | a lineage |             | of massive | labeled     |          |       |               |        |                |     |                |
|               |            |          |        |           |             |            |             | What has | begun | to            | emerge | as a potential |     | alternative in |
| datasets      | (LeCun     | et al.,  | 2015), | such      | as the      | ImageNet   | dataset     |          |       |               |        |                |     |                |
computervision—andmarkedlysowhenthereislimitedlabeled
| (Deng et | al., 2009). | These | datasets | were | (and | are) used | to train |     |     |     |     |     |     |     |
| -------- | ----------- | ----- | -------- | ---- | ---- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
deep convolutional neural networks, often one of the variants downstreamdata—isself-supervisedlearning(Chenetal.,2016;
or progeny of ResNet (He et al., 2016) and DenseNet (Huang vandenOordetal.,2018;Grilletal.,2020;Hénaff,2020)8.These
|                |            |     |       |             |           |     |            | works are | inspired | by  | the recent | success | in natural | language |
| -------------- | ---------- | --- | ----- | ----------- | --------- | --- | ---------- | --------- | -------- | --- | ---------- | ------- | ---------- | -------- |
| et al., 2017). | Crucially, |     | these | are labeled | datasets, |     | featuring— |           |          |     |            |         |            |          |
especially in the case of ImageNet—an enormous number of processing (NLP) using LMs, which can be used to greatly
uniquepossibleclassificationlabels(orequivalentlytargets,with affect the transfer learning, but also for few-shot and zero-shot
ImageNet5, learning(Brownetal.,2020;Raffeletal.,2020).Thesemodelsare
| 1000 being | common |     | when using |     |     | but | more are |     |     |     |     |     |     |     |
| ---------- | ------ | --- | ---------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
understoodtoworkbymakingaverygeneralmodeloflanguage
| possible6). | Leveraging |     | labeled | data | (especially | for | a singular |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | ------- | ---- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
domain such as a single subject, session and task) of a similar and appear even immediately capable of performing tasks they
werenotexplicitlytrainedtoaccomplish.WeproposethatDNN
| scale in | BCI is     | impractical | but,    | despite    | this,    | a sizeable | amount |          |          |        |     |              |          |           |
| -------- | ---------- | ----------- | ------- | ---------- | -------- | ---------- | ------ | -------- | -------- | ------ | --- | ------------ | -------- | --------- |
|          |            |             |         |            |          |            |        | transfer | learning | in BCI | and | neuroimaging | analysis | generally |
| of prior | work tries | to          | fashion | a transfer | learning | strategy   | after  |          |          |        |     |              |          |           |
the successes of ImageNet “pre-training.” These take the form couldfollowasimilarline,withencephalographymodels(EM)in
oftransferringknowledgefromanetworkpre-trainedwithmore placeofLMs.Theimportantquestionbeinghowbesttoconstruct
suchanEMsothatitlearnsfeaturesthataregeneralenough,while
| data, typically | more | subjects, | to  | a target | domain | with | less data, |     |     |     |     |     |     |     |
| --------------- | ---- | --------- | --- | -------- | ------ | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
remainingusableforanyanalysistask?
typicallyasinglesubject(LinandJung,2017;Doseetal.,2018;
Schwemmer et al., 2018; Fahimi et al., 2019; Xu et al., 2019; To our knowledge, the most similar prior work to this line
|        |                  |     |       |        |     |          |        | of inquiry | has   | been the | approaches     | developed |         | for (EEG) self- |
| ------ | ---------------- | --- | ----- | ------ | --- | -------- | ------ | ---------- | ----- | -------- | -------------- | --------- | ------- | --------------- |
| Cimtay | and Ekmekcioglu, |     | 2020; | Kostas | and | Rudzicz, | 2020b; |            |       |          |                |           |         |                 |
|        |                  |     |       |        |     |          |        | supervised | sleep | stage    | classification | (SSC)     | through | contrastive     |
Zhangetal.,2020a),withsomeworktransferringbetweenentire
datasetsofthesameparadigm,ratherthansubjects(Ditthapron learning (Banville et al., 2019). Contrastive learning is a
et al., 2019). On the surface, these embody a general-to-specific more particular, yet generally applicable training process that
|            |          |          |        |     |             |     |          | consists | of identifying |     | positive | representations |     | from a set that |
| ---------- | -------- | -------- | ------ | --- | ----------- | --- | -------- | -------- | -------------- | --- | -------- | --------------- | --- | --------------- |
| supervised | transfer | learning | scheme |     | reminiscent | of  | ImageNet |          |                |     |          |                 |     |                 |
pre-training where models trained on an ImageNet problem also includes incorrect or negative distractor representations
areadaptedtoanovel(butrelated)application.However,these (Arora et al., 2019). Banville et al. proposed two potential
|                |          |          |           |           |     |           |              | contrastive  | learning |        | tasks—a   | “relative  | positioning” | task and          |
| -------------- | -------- | -------- | --------- | --------- | --- | --------- | ------------ | ------------ | -------- | ------ | --------- | ---------- | ------------ | ----------------- |
| particular     | framings | lack     | the label | diversity |     | when      | pre-training |              |          |        |           |            |              |                   |
|                |          |          |           |           |     |           |              | an extension | they     | termed | “temporal | shuffling” |              | (Banville et al., |
| with ImageNet. |          | In other | words,    | a narrow  | set | of labels | are used     |              |          |        |           |            |              |                   |
to pre-train a model, and these simply overlap with the target 2019). Underlying both tasks is the notion that neighboring
| context, | i.e., Y | = Y | . This approach |     | is in | fact distinct | from |     |     |     |     |     |     |     |
| -------- | ------- | --- | --------------- | --- | ----- | ------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
S T
the approach taken as inspiration where Y S 6= Y T (or possibly 7Itisalsoworthnotingthatourownpriorworkdoesnotconsideroridentifythis.
YS ⊂ Y ). We remain unaware of any work that pre-trains a 8Terminologyherecanbesomewhatfuzzy.Whatismeantbyself-supervisionisa
T
DNNusingawidegamutofBCI-relevanttargetsintheservices supervision-liketaskthatrequiresdomain-relevantunderstandinginsomesense.
Sometimes,“semi-supervised”isusedinstead,asitisoftenalsoasemi-supervised
ofamorenarrowtargetset,aswouldbemoreanalogoustousing
procedure(Chenetal.,2016),sincethetaskislearnedinanunsupervisedfashion
ImageNetaspre-trainingtowardmorespecificcomputervision
firstandthenclassicsupervisedlearningisusedwithlabels.Typically,though,
|     |     |     |     |     |     |     |     | semi-supervision          | involves | inferring | labels               | for unlabeled | data              | during training. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | -------- | --------- | -------------------- | ------------- | ----------------- | ---------------- |
|     |     |     |     |     |     |     |     | Instead, self-supervision |          | is        | loosely a particular | case          | of representation | learning,        |
5image-net.org/challenges/LSVRC/2012/
whichisnothistoricallyuncommoninBCI(Zhangetal.,2020b).Thoughthis
6https://www.image-net.org/index.php
workisdifferentgiventhattypicallythelossisdomainordataagnostic.
FrontiersinHumanNeuroscience|www.frontiersin.org 3 June2021|Volume15|Article653659

Kostasetal. BENDR
representations share a label. The representations themselves sub-word Aroca-Ouellette and Rudzicz, 2020) given previous
are a learned mapping (in their case, a convolutional neural (or, in some cases, also subsequent) tokens, a MLM scheme
network, but ostensibly arbitrary) of raw EEG time-windows insteadlearnstoreconstructlanguagetoken(s)givensurrounding
to a feature vector. This assumption of similar neighboring context (fashioned after the Cloze task). This family of models
labels is fair for SSC, where sleep stages change slowly, and may deploy a variety of auxiliary tasks (Aroca-Ouellette and
is generally reasonable for continuous problems, where some Rudzicz, 2020) for transfer learning capabilities, but the task
notionofsmoothnesscanbeassumed.Theirproposed“relative currentlyattheheartofthisfamilyisasfollows:givenasequence
positioning”taskisabinaryclassificationproblemdistinguishing ofN tokenst ,...t ,andasubsetoftokenindexesI ,foreach
1 N m
whether a pair of representations are within a local or positive tokenindexi∈I ,tokensaremaskedwithsomemaskMsothat:
m
window τ , or outside a long-range or negative window τ
pos neg
(whenτ neg > τ pos ,thosefallingwithinτ neg butoutsideτ pos are q = M;i∈I m ,∀i∈N (1)
ignored). Their alternative “temporal shuffling” method adds a i (t
i
;otherwise
third window or representation with which to contrast that is
within τ of one (arbitrary) window called the “anchor,” and A transformer encoder (Vaswani et al., 2017; Devlin et al.,
pos
again learns the representations through a binary classification 2019)thenreconstructstheoriginalsequenceoftokensfromthe
task. In this case, the classification determines whether the maskedsequence[t andq,∀i∈N,respectively,inEquation(1)].
i i
three representations are ordered sequentially, or are out of M could be a single learned token (Baevski et al., 2020), or in
order. Downstream (loose terminology used to mean the step thecaseof BERT: 80%of thetimea fixed[MASK]token,10%
after pre-training when a model is leveraged and evaluated for arandomtokenor10%theoriginaltoken(with15%oftokens
a particular task), both contrastive learning tasks ultimately maskedwithineachsequence)(Devlinetal.,2019).
improvedSSCclassificationperformanceoverthesamenetwork CouldanEMbedevelopedinthisvein,usingsay,individual
trainedinafullysupervisedmannerfromscratch(withrandomly samples rather than tokens (i.e., could a direct application of
initialized weights rather than those that accomplish the self- the above be done with raw EEG)? Unfortunately, the highly
supervisedtask)andtheirresultsfurtheragreewiththecommon correlated nature of neighboring samples in EEG (or most
findingthatself-supervisionappearsdistinctlybetterwithlimited other continuous data for that matter) is not conducive to
fine-tuning9 data (Brown et al., 2020; Chen et al., 2020). this approach. The likely result would be that, instead of an
Furthermore,self-supervisedpre-trainingalsooutperformedan EM, a method for interpolation would be learned, the model
autoencoder-based pretraining, an alternative and historically wouldsimplylearnhowtoaverageneighboringsamples,ashas
common pretraining option where a network is pretrained to been argued in similar work in self-supervised learning with
reconstruct its original input. “Relative positioning” performed speech (Jiang et al., 2020). In other words, the smoothness
betteronaverage(andnostatisticalsignificanceexpressed)when of these data would make it hard to produce general features
comparedtoitscounterpart,butalinearclassificationofsimple simplythroughrecoveringmissingindividualsamples.Masking
hand-craftedfeatureswasstillhighestperformingoverall.These a contiguous span of tokens instead, which is beneficial in
resultsdemonstratethepromiseofself-supervisedlearningwith NLP (Joshi et al., 2020; Raffel et al., 2020), could avoid simply
DNNs for EEG over a supervised approach, but contextualize learning to interpolate missing samples, but the reconstruction
them as early in development. This is perhaps best seen by of time-series data is difficult, due to the challenge (among
considering the lengths of the time windows (τ and τ ). other things) of capturing the degree of error in time (within
pos neg
The shortest windows employed in this particular investigation contiguous sequences) (Rivest and Kohar, 2020). The losses
were2minforτ andτ ,whichseemsprohibitivelylongfor used for such reconstruction, commonly mean squared error
pos neg
most immediate applications outside of SSC. As it is assumed (or mean absolute error), erroneously assume independence in
that representations within τ are similarly labeled, it may be the error between elements in the series, causing inappropriate
pos
difficulttoexpandtheuseofthistechniquetotimescalescloser error signals when (among other things) simply shifting a
to that of say, a BCI trial (across any paradigm), which tend reconstructionintime(RivestandKohar,2020).
to be no more than several seconds at most. In this work, we Contrastive predictive coding (CPC), is a particular
focusoureffortsonadaptingarelevantstrategyfromthewider contrastive learning approach that is intended for sequence
MLliteraturethatcoulddevelopfeaturesonsmallertimescales learning. With CPC, the correct learned representation for a
effectiveforBCItrialsaswellastimescalesappropriateforSSC. particular sequence offset is predicted relative to distractor
ReturningtoaconsiderationofhowonemightadaptLMpre- representations, typically those of other positions in the
training to EM, the masked language model (MLM) is a slight same sequence (van den Oord et al., 2018). What is notable
variationonthetypicalLMthathasbeenessentialtothesuccess about this is that it is not as susceptible to degeneration
of recent LMs like BERT (Devlin et al., 2019) and its lineage into interpolation, nor is it similarly affected by the issues of
(Raffel et al., 2020) of similar models. Where a LM estimates time-series reconstruction (van den Oord et al., 2018). This
the probability of encountering a language token (a word or task enables learning both a good feature representation and
an understanding of the sequence of data by modeling the
progression of the representations, learned with a single loss
9Asisperhapsobviousinthename,thoughpotentiallymisleading.Fine-tuning
function. Indeed, the RP and TS tasks discussed above for SSC
istheprocessoffurthertrainingonareservedportionofatargetdataset,unless
statedotherwise,thisistypicallythroughstandardsupervisedtraining. can be understood as special cases of the more general CPC,
FrontiersinHumanNeuroscience|www.frontiersin.org 4 June2021|Volume15|Article653659

| Kostasetal. |     |     |     |     |     |     |     |     |     |     |     | BENDR |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
thoughperformanceappearslargelysimilarwhencomparingall data classification tasks—or downstream tasks—summarized in
three(Banvilleetal.,2020). Table1.MostofthesewereBCItaskdatasets,whichcouldreadily
Priorworkinself-supervisedspeechrecognitionhasbegunto becomparedtopreviousworkwithDNNstrainedwithoutany
synthesize parts of CPC and MLM to produce methodologies additional unlabeled data (Lawhern et al., 2018; Kostas and
for self-learning with raw waveforms (van den Oord et al., Rudzicz,2020b).WealsoincludedoneoftheSSCtasksusedby
2018; Baevski and Mohamed, 2020; Baevski et al., 2020; Banvilleetal.(2019)intheirworkonsleepstageself-supervision
Chung et al., 2020; Jiang et al., 2020). In our work, we describedabove,forcomparison.Thisparticulardatasetafforded
|     |     |     | wav2vec |     | 2.0 |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
adapt one of these approaches called (Baevski some further insight into generality, as BCI data are typically
et al., 2020) (its particular formulation is detailed in section classifiedinthecontextofparticulartrialsorevents,andSSCis
2.4.1) to EEG. We consider how efficient the approach is at a more continuous problem, requiring that large spans of time
developing representations (BENDR), and how general these arelabeledwiththeparticularsleepstageasubjectisundergoing.
andtheaccompanyingsequencemodelareacrossmultipletask These segments are distinctly longer than the BCI trials we
paradigms/datasets (not seen during pre-training) and across considered in the remaining battery (an order of magnitude
the subjects that constitute them. Since interestingly, both the difference in our case when compared to the largest BCI task
representationsalone(Chenetal.,2020),andtheadditionofthe sequencelength),andaredistinctlycloserinlengthtothewaythe
sequence model (Baevski et al., 2020) have proven potentially pre-trainingtaskisformulated(seesection2.4.1).Wespecifically
useful for supervised fine-tuning after pre-training, we then segmented these sequences into periods of 30 s to be classified
characterizeavarietyof“fine-tuning”approaches“downstream.” into5sleepstagesasinpriorwork(Banvilleetal.,2019;Mousavi
Inotherwords,finally,wecomparewhichaspectofouroverall etal.,2019).AnotherpotentiallynotabledifferencewiththeSSC
schemeisbestleveragedandhowtowardclassifyingavarietyof dataset was the scale of available labels, which seems to have
publiclyavailableEEGclassificationtaskdatasets. enabledpriorworktoconsiderdeeperandmorecomplexmodels
(Mousavietal.,2019).
| 2. MATERIALS |     | AND | METHODS |     |     |     |     |     |     |     |     |     |
| ------------ | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2.2. Preprocessing
Allexperimentsareimplementedusingthedeepneuralnetworks
|                      |     |       |                       |      |          | The focus | of the | preprocessing | stage | was to | create a maximally |     |
| -------------------- | --- | ----- | --------------------- | ---- | -------- | --------- | ------ | ------------- | ----- | ------ | ------------------ | --- |
| for neurophyisiology |     | (DN3) | library10. The source | code | and pre- |           |        |               |       |        |                    |     |
trained BENDR models can be found at https://github.com/ consistent representation of EEG sequences across datasets
|     |     |     |     |     |     | (which implied |     | differences | in hardware), | so  | that a pre-trained |     |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | ------------- | --- | ------------------ | --- |
SPOClab-ca/BENDR.
networkwaswellsuitedtothedownstreamtasks.Moreorless,
|     |     |     |     |     |     | this amounted |     | to modifying | downstream | datasets | to match | the |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ------------ | ---------- | -------- | -------- | --- |
2.1. Datasets
2.1.1.Pre-training configuration of the pre-training dataset. The first aspect of
|           |              |              |          |             |           | this was      | to remove | spurious | differences  | in  | channel amplitude. |     |
| --------- | ------------ | ------------ | -------- | ----------- | --------- | ------------- | --------- | -------- | ------------ | --- | ------------------ | --- |
| We intend | to learn     | our proposed | general  | task across | a large   |               |           |          |              |     |                    |     |
|           |              |              |          |             |           | Each sequence |           | gathered | for training | was | linearly scaled    | and |
| number    | of typically | confounding  | domains, | which       | means the |               |           |          |              |     |                    |     |
idealpre-trainingdatasetforourpurposeswouldfeaturemany shifted (a weight and offset for each sequence adjusts every
|            |           |                |                |       |            | sample in     | the sequence) |               | so that the | maximum | and minimum        |     |
| ---------- | --------- | -------------- | -------------- | ----- | ---------- | ------------- | ------------- | ------------- | ----------- | ------- | ------------------ | --- |
| subjects,  | each      | recorded over  | many sessions. | These | sessions   |               |               |               |             |         |                    |     |
|            |           |                |                |       |            | values within | each          | sequence      | equal 1     | and     | −1, respectively.  | To  |
| would also | ideally   | be distributed | across large   | time  | scales and |               |               |               |             |         |                    |     |
|            |           |                |                |       |            | account       | for the       | lost relative | (to the     | entire  | dataset) amplitude |     |
| consist of | a variety | of performed   | tasks. In      | other | words, the |               |               |               |             |         |                    |     |
pre-training dataset should consist of a representative sample information, a single channel was added with the constant
|     |     |     |     |     |     | value m | a x ( s i ) − m | i n ( si ) , where | S is | the set | of all samples | in  |
| --- | --- | --- | --- | --- | --- | ------- | --------------- | ------------------ | ---- | ------- | -------------- | --- |
of EEG data. This also means that these data should include m ax ( S ) − m i n ( S s) ds
d s d
multiple different recording hardware and configurations. The the dataset and s ⊂ S is a particular sub-sequence (i.e.,
|     |     |     |     |     |     |     |     | i   | ds  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
closestpubliclyaccessibledataset,toourcurrentknowledge,was trial). We additionally addressed the differences in sampling
|     |     |     |     |     |     | frequency | and | electrode | sets of the | different | dataset. | Our |
| --- | --- | --- | --- | --- | --- | --------- | --- | --------- | ----------- | --------- | -------- | --- |
theTempleUniversityHospitalEEGCorpus(TUEG)(Obeidand
Picone, 2016). It consists of clinical recordings using a mostly solutions to these problems were similarly minimalist and
conventionalrecordingconfiguration(monopolarelectrodesina were achieved using standard features in DN3 (Kostas and
|     |     |     |     |     |     | Rudzicz, | 2020a). | Specifically, | we over- | or  | undersampled | (by |
| --- | --- | --- | --- | --- | --- | -------- | ------- | ------------- | -------- | --- | ------------ | --- |
10–20configuration)ofover10,000people,somewithrecording
sessions separated by as much as 8 months apart. The subjects whole multiples, for lower and higher sampling frequencies,
were 51% female, and ages range from under 1 years old to respectfully) to get nearest to the target sampling frequency
over 90 (Obeid and Picone, 2016). We focused specifically of 256 Hz. Then, nearest-neighbor interpolation was used to
on versions 1.1 and 1.2 of this dataset which amounted to obtain the precise frequency (as was done in prior work
approximately 1.5 TB of European-data-format (EDF) EEG Kostas and Rudzicz, 2020a). Additionally, the P300 dataset
recordingsbeforepreprocessing. was low-pass filtered below 120 Hz to avoid aliasing due
|     |     |     |     |     |     | to its higher | sampling |     | rate (and | associated | higher | original |
| --- | --- | --- | --- | --- | --- | ------------- | -------- | --- | --------- | ---------- | ------ | -------- |
2.1.2.Downstream
|     |     |     |     |     |     | low-pass | filter). | Furthermore, | the | SSC dataset | featured | two |
| --- | --- | --- | --- | --- | --- | -------- | -------- | ------------ | --- | ----------- | -------- | --- |
Toinvestigatethepracticalutilityofthelearnedrepresentations, bi-polar electrodes: FPz-Cz and Pz-Oz, which were simply
wecompiledanon-exhaustivebatteryofpubliclyaccessibleEEG mapped to FPz and Pz, respectively. The TUEG dataset itself
|     |     |     |     |     |     | featured | some higher | sampling | rate | signals; | we included | those |
| --- | --- | --- | --- | --- | --- | -------- | ----------- | -------- | ---- | -------- | ----------- | ----- |
10https://github.com/SPOClab-ca/dn3
|     |     |     |     |     |     | with low-pass | filters | that | did not violate | the | Nyquist | criterion |
| --- | --- | --- | --- | --- | --- | ------------- | ------- | ---- | --------------- | --- | ------- | --------- |
FrontiersinHumanNeuroscience|www.frontiersin.org 5 June2021|Volume15|Article653659

| Kostasetal. |     |     |     |     |     |     |     |     |     |     | BENDR |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
TABLE1|Summaryofdownstreamdatasetbatteryandnumberofcross-validationfoldsused.
| Dataset |     |     | Paradigm |     | sfreq.Hz |     | #Ch. |     | Subjects | Targets | Folds |
| ------- | --- | --- | -------- | --- | -------- | --- | ---- | --- | -------- | ------- | ----- |
MMIGoldbergeretal.(2000),Schalketal.(2004) MI(L/R) 160 64 105 2 5
| BCICTangermannetal.(2012) |     |     | MI(L/R/F/T) |     | 250 |     | 22  |     | 9   |     | 4 9 |
| ------------------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
ERNMargauxetal.(2012) Errorrelatednegativity 200 56 26(10) 2 4
P300Goldbergeretal.(2000),Citietal.(2010,2014) Donchinspeller 2,048 64 9 2 9
SSCGoldbergeretal.(2000),Kempetal.(2000,2018) SleepStaging 100 2 83 5 10
Cross-validationsplitswereinaleave-multiple-subjects-outconfigurationifFolds<Subjects,orleave-one-subject-outifFolds=Subjects(asinpriorworkKostasandRudzicz,2020b).
TheERNdatasetwasfeaturedinanonlinecompetition11whichfeatured10held-outtestsubjects(notusedduringtraining),whichweusedasatestdatasetforallfourvalidationsplits
ofthisdataset.
TABLE2|Performancesofdownstreamdatasets.
| Dataset |     | Start(s) | Length(s) |     | Metric   |     |     | Best |     |     | Modelconfig. |
| ------- | --- | -------- | --------- | --- | -------- | --- | --- | ---- | --- | --- | ------------ |
| MMI     |     | 0        | 6         |     | BAC      |     |     | 86.7 |     |     | Linear(2.)   |
| BCIC    |     | –2       | 6         |     | Accuracy |     |     | 42.6 |     |     | Linear(2.)   |
| ERN     |     | –0.7     | 2         |     | AUROC    |     |     | 0.65 |     |     | Linear(2.)   |
| SSC     |     | 0        | 30        |     | BAC      |     |     | 0.72 |     |     | Linear(2.)   |
| P300    |     | –0.7     | 2         |     | AUROC    |     |     | 0.72 |     |     | BENDR(1.)    |
Startandlengthrefertolengthoftrialsandstartwithrespecttoeventmarkersinseconds.Bestperformancespecifiesaverageperformanceacrossallsubjects(andthereforefolds)for
bestperformingmodelconfiguration.BAC:classbalancedaccuracy;AUROC:areaunderthereceiveroperatingcharacteristiccurve.Modelconfigurationsarenumberedinaccordance
withthelistpresentedinsection2.4.2.
(and subsequently re-sampled them as above), and ignored stages.Afirststagetakesrawdataanddramaticallydownsamples
therest. it to a new sequence of vectors using a stack of short-receptive
Deep1010
A reduced subset of the channel mapping from field1Dconvolutions.Theproductofthisstageiswhatwecall
DN3 (Kostas and Rudzicz, 2020a) was used throughout. This BENDR (specifically in our case, when trained with EEG). A
ensured that particular channels were mapped to a consistent second stage uses a transformer encoder (Vaswani et al., 2017)
indexforeachloadedtrial.Theoriginalmappingwasdesigned (layered,multi-headself-attention)tomapBENDRtosomenew
to be more inclusive, and thus assumed up to 77 possible EEG sequencethatembodiesthetargettask.
electrodes.Intheinterestofminimizingunnecessaryelectrodes Raw data are downsampled through the stride (number of
foranalreadyhigh-dimensionalproblem,wefocusedonthe19 skipped samples) of each convolution block in the first stage
EEGchannelsoftheunambiguouslyillustrated10/20channelset (rather than pooling, which would require greater memory
(UI10/20)(Jurcaketal.,2007),astheTUEGdatasetrecordings requirements).Eachofourconvolutionblockscomposedofthe
were done using a roughly 10/20 channel scheme. We simply sequence: 1D convolution, GroupNorm (Wu and He, 2020),
ignoredreferenceelectrodes,electro-oculograms,andanyother and GELU activation (Hendrycks and Gimpel, 2016). Our own
auxiliary channels. When also accounting for the additional encoderfeaturessixsequentialblocks,eachwithreceptivefields
relative amplitude channel described above, every sequence of 2, except for the first block, which has 3. Strides match the
fromeverydatasetused20channels.Allsurpluschannelswere length of the receptive field for each block. Thus, the effective
(≈
ignored,andmissingchannelssetto0. sampling frequency of BENDR is 96 times smaller 2.67
During pre-training, we extracted sequences of 60 s (every Hz)thantheoriginalsamplingfrequency(256Hz).Eachblock
60 s) from each usable sequence, which amounted to 15,360 consistsof512filters,meaningeachresultingvectorhasalength
| samplespersubsequence.Weobservedinearlytestingthatthere |     |     |     | of512. |     |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
was better performance with larger sequences (see Figure4 for The transformer follows the standard implementation of
more). As can be seen in Table2, the downstream datasets all Vaswani et al. (2017), but with internal batch normalization
classifiedsequencelengthsshorterthanthis,butthearchitecture layersremovedandwithanaccompanyingweightinitialization
weemployed(seesection2.3)wasostensiblyagnostictosequence scheme known as T-Fixup (Huang et al., 2020). Our particular
length(seesection4forcaveats). transformer architecture uses 8 layers, with 8 heads, model
|            |              |     |     | dimension |          | of 1536 | and     | an internal | feed-forward |          | dimension   |
| ---------- | ------------ | --- | --- | --------- | -------- | ------- | ------- | ----------- | ------------ | -------- | ----------- |
| 2.3. Model | Architecture |     |     |           |          |         | wav2vec | 2.0,        |              |          |             |
|            |              |     |     | of        | 3076. As | with    |         |             | we           | use GELU | activations |
ThemodelarchitecturedisplayedinFigure1closelyfollowsthat (Hendrycks and Gimpel, 2016) in the transformer, and
ofwav2vec 2.0(Baevskietal.,2020)andiscomposedoftwo additionally include LayerDrop (Fan et al., 2019) and Dropout
|     |     |     |     | at  | probabilities | 0.01 | and | 0.15, respectively, |     | during | pre-training |
| --- | --- | --- | --- | --- | ------------- | ---- | --- | ------------------- | --- | ------ | ------------ |
11https://www.kaggle.com/c/inria-bci-challenge but neither during fine-tuning. We represent position using an
FrontiersinHumanNeuroscience|www.frontiersin.org 6 June2021|Volume15|Article653659

| Kostasetal. |     |     |     |     |     |     |     |     |     |     |     |     |     |     | BENDR |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
additive (grouped) convolution layer (Mohamed et al., 2019; representations (in our case BENDR) that summarizes the
Baevski et al., 2020) with a receptive field of 25 and 16 groups originalinput.Aninputtokenisprependedtothissequence(a
before the input to the transformer. This allows the entire BENDR-lengthedvectorfilledwith−5),andcontiguousspansof
architecturetobesequence-lengthindependent,althoughitmay the remaining sequence are masked. This modified sequence is
comeattheexpenseofnotproperlyunderstandingpositionfor providedasinputtothetransformerstage,whichisexpectedto
shortsequences. developoutputsthataremostsimilartotheun-maskedinputat
Originally, the downstream target of the wav2vec 2.0 apositiont.Specifically,weusetheself-supervisedlossfunction
processwasaspeechrecognitionsequence(itwasfine-tunedon foramaskedtokenlocalizedatt:
| a sequence | of  | characters | or phonemes) |     | (Baevski | et al., | 2020). |     |     |     |     |     |     |     |     |
| ---------- | --- | ---------- | ------------ | --- | -------- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
exp(cossim(c,b))/κ
Instead,heretheentiresequenceisclassified.Todothisusinga L=−log t t (2)
transformer,weadoptthecommonpractice(Devlinetal.,2019) exp(cossim(c,b))/κ t i
bi∈BD
offeedingafixedtoken(a.k.a.[CLS]inthecaseofBERTor,in istheoutputPofthetransformeratpositiont,b
|                                                          |     |     |     |     |     |     |     | wherec                                            |     |     |     |     |     |     | isthe |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- |
| ourcase,avectorfilledwithanarbitraryvaluedistinctfromthe |     |     |     |     |     |     |     | t                                                 |     |     |     |     |     |     | i     |
|                                                          |     |     |     |     |     |     |     | (original/un-masked)BENDRvectoratsomeoffseti,andB |     |     |     |     |     |     | isa   |
input signal range, in this case: −5) as the first sequence input D
setof20uniformlyselecteddistractors/negativesfromthesame
| (prepended | to  | BENDR). | The transformer |     | output | of this | initial |           |      |         |         |        |            |             |     |
| ---------- | --- | ------- | --------------- | --- | ------ | ------- | ------- | --------- | ---- | ------- | ------- | ------ | ---------- | ----------- | --- |
|            |     |         |                 |     |        |         |         | sequence, | plus | b. t We | use the | cosine | similarity | cossim(x,y) | =   |
positionwasnotmodifiedduringpre-training,andonlyusedfor
xTy/(|x||y|)functiontodeterminehowsimilarvectorsare,and
downstreamtasks.
|                    |     |     |                                |     |     |     |     | the sensitivity | of  | this is | adjusted | by a | temperature | factor | κ, set |
| ------------------ | --- | --- | ------------------------------ | --- | --- | --- | --- | --------------- | --- | ------- | -------- | ---- | ----------- | ------ | ------ |
| Themostfundamental |     |     | differencesinourworkascompared |     |     |     |     |                 |     |         |          |      |             |        |        |
to0.1.Thislossisexpectedtooperatebyadjustingtheoutputof
| to that     | of the   | speech-specific | architecture |       | that     | inspired  | it are |                 |     |             |      |            |         |                 |         |
| ----------- | -------- | --------------- | ------------ | ----- | -------- | --------- | ------ | --------------- | --- | ----------- | ---- | ---------- | ------- | --------------- | ------- |
|             |          |                 |              |       |          |           |        | the transformer |     | at position | t    | to be most | similar | to the          | encoded |
| as follows: | (1)      | we do not       | quantize     | BENDR | for      | creating  | pre-   |                 |     |             |      |            |         |                 |         |
|             |          |                 |              |       |          |           |        | representation  | at  | t, despite  | that | this input | to      | the transformer | is      |
| training    | targets, | and (2)         | we have      | many  | incoming | channels. | In     |                 |     |             |      |            |         |                 |         |
masked.Thismeansthetransformermustlearnageneralenough
| wav2vec | 2.0,asinglechannelofrawaudiowasused.While |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
modelofBENDR(notEEGperse)suchthattheentiresequence
| a good | deal of | evidence | (Schirrmeister |     | et al., | 2017; Chambon |     |          |     |              |          |     |         |         |         |
| ------ | ------- | -------- | -------------- | --- | ------- | ------------- | --- | -------- | --- | ------------ | -------- | --- | ------- | ------- | ------- |
|        |         |          |                |     |         |               |     | of BENDR | can | characterize | position |     | t well. | We also | add the |
etal.,2018;Lawhernetal.,2018;Lotteetal.,2018;Kostasetal.,
|              |           |          |                 |             |         |            |     | mean squared    |          | activation   | of the      | BENDR      | to     | the loss   | to keep |
| ------------ | --------- | -------- | --------------- | ----------- | ------- | ---------- | --- | --------------- | -------- | ------------ | ----------- | ---------- | ------ | ---------- | ------- |
| 2019; Kostas | and       | Rudzicz, | 2020b)          | supports    | the     | advantage  | of  |                 |          |              |             |            |        |            |         |
|              |           |          |                 |             |         |            |     | the activations |          | from growing |             | too large, | as was | similarly  | done    |
| temporally   | focused   | stages   | (no             | EEG channel | mixing) | separate   |     |                 |          |              |             |            |        |            |         |
|              |           |          |                 |             |         |            |     | previously      | (Baevski | et           | al., 2020), | but        | we set | the weight | of this |
| from a       | stage (or | more)    | that integrates | channels,   |         | we elected | to  |                 |          |              |             |            |        |            |         |
additionaltermto1(ratherthan10).
| preserve | the 1D | convolutions | of  | the original | work | to minimize |     |     |     |     |     |     |     |     |     |
| -------- | ------ | ------------ | --- | ------------ | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Contiguoussequencesof10BENDRaremaskedbeforeinput
anyadditionalconfoundandtoreducecomplexity(computeand
|                     |     |     |                   |     |     |          |       | tothetransformerwithprobabilityp |     |     |     |      | = 0.065,suchthat,for |     |     |
| ------------------- | --- | --- | ----------------- | --- | --- | -------- | ----- | -------------------------------- | --- | --- | --- | ---- | -------------------- | --- | --- |
| memoryutilization∝N |     |     | with2Dratherthan∝ |     |     | Nfilters | for1D |                                  |     |     |     | mask |                      |     |     |
filters eachsample,thelikelihoodofbeingthebeginningofacontiguous
NEEG
convolutions).Thisseemedfair,asthereisalsoevidencethat1D sectionwasp ,andoverlapisallowed.Welearnasinglemask
mask
convolutionsareeffectivefeatureextractorsforEEG,particularly
|            |         |     |              |     |            |        |     | vector during | pre-training |     | of  | the same | length | as each | BENDR |
| ---------- | ------- | --- | ------------ | --- | ---------- | ------ | --- | ------------- | ------------ | --- | --- | -------- | ------ | ------- | ----- |
| with large | amounts | of  | data (Gemein | et  | al., 2020; | Kostas | and |               |              |     |     |          |        |         |       |
vector,andusethisasthetransformerinputtomaskedpositions;
Rudzicz, 2020a). Notably, wav2vec 2.0 downsampled raw masking is done by replacing a masked BENDR with a learned
audiosignalsbyamuchlargerfactor(320)thanourownscheme,
|            |             |     |              |         |        |             |     | vector. The | number | of  | negatives/distractors |     |     | was set | to 20 and |
| ---------- | ----------- | --- | ------------ | ------- | ------ | ----------- | --- | ----------- | ------ | --- | --------------------- | --- | --- | ------- | --------- |
| but speech | information |     | is localized | at much | higher | frequencies |     |             |        |     |                       |     |     |         |           |
uniformlysampledfromthesamesequenceasthemaskedvector,
thanencephalographicdataareexpectedtobe.Theneweffective i.e.,negativesdonotcrosstrialsorsequences.
| samplingrateofBENDRis≈ |     |     | 2.67Hz,orafeature-window(no |     |     |     |     |             |     |                   |     |     |          |       |     |
| ---------------------- | --- | --- | --------------------------- | --- | --- | --- | --- | ----------- | --- | ----------------- | --- | --- | -------- | ----- | --- |
|                        |     |     |                             |     |     |     |     | To evaluate |     | how generalizable |     | the | sequence | model | and |
overlap)of≈375ms.Weselectedthisdownsamplingfactorasit
|     |     |     |     |     |     |     |     | vectors | were to | unseen | data | after pre-training, |     | we  | evaluated |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------ | ---- | ------------------- | --- | --- | --------- |
remainedstable(i.e.,itdidnotdegeneratetoaninfiniteloss,or
|     |     |     |     |     |     |     |     | the contrastive |     | task, expressed |     | as the | transformer |     | accuracy |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------------- | --- | ------ | ----------- | --- | -------- |
simplymemorizeeverythingimmediately)duringtraining. in constructing c to be most similar to b rather than the
|               |     |     |            |     |     |     |     |                        |     | t          |         |           |         | t        |           |
| ------------- | --- | --- | ---------- | --- | --- | --- | --- | ---------------------- | --- | ---------- | ------- | --------- | ------- | -------- | --------- |
|               |     |     |            |     |     |     |     | distractors/negatives, |     | with       | respect | to unseen |         | data (in | this case |
| 2.4. Training |     | and | Evaluation |     |     |     |     |                        |     |            |         |           |         |          |           |
|               |     |     |            |     |     |     |     | the downstream         |     | datasets). | Note    | here      | that no | further  | training  |
WeusedtheAdam(KingmaandBa,2015)optimizerthroughout
|             |         |              |        |             |              |            |        | or any evaluation |      | with     | respect | to downstream |     | task labels | was    |
| ----------- | ------- | ------------ | ------ | ----------- | ------------ | ---------- | ------ | ----------------- | ---- | -------- | ------- | ------------- | --- | ----------- | ------ |
| training    | (during | pre-training | and    | fine-tuning | with         | downstream |        |                   |      |          |         |               |     |             |        |
|             |         |              |        |             |              |            |        | performed.        | This | was done | to      | evaluate      | the | variability | of the |
| data), with | weight  | decay        | set to | 0.01. We    | additionally |            | used a |                   |      |          |         |               |     |             |        |
representationsafterpre-training.Duringthisevaluationstep,we
| cosine learning |     | rate decay | with | linear warm-up |     | for 5 and | 10% |     |     |     |     |     |     |     |     |
| --------------- | --- | ---------- | ---- | -------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
maskedhalftheamountexpectedduringtraining,butdidsosuch
oftotaltrainingsteps(batches)forpre-trainingandfine-tuning, thatmaskedspanswereevenlyspacedthroughthesequence(so
respectively.Thepeaklearningrateitselfvariedbydataset;this
thattherewerenooverlappingsequences,andsufficientcontext
| and other  | variable | hyperparameters |     | are | further | documented | in  |                 |        |     |                |     |           |           |          |
| ---------- | -------- | --------------- | --- | --- | ------- | ---------- | --- | --------------- | ------ | --- | -------------- | --- | --------- | --------- | -------- |
|            |          |                 |     |     |         |            |     | was available). | That   | is, | for a sequence |     | length    | of N , we | masked   |
| AppendixA. |          |                 |     |     |         |            |     |                 |        |     |                |     |           | S         |          |
|            |          |                 |     |     |         |            |     | 0.5 × N         | × p    | =   | N contiguous   |     | sequences | (of       | 10), and |
|            |          |                 |     |     |         |            |     |                 | S mask |     | m              |     |           |           |          |
2.4.1.Pre-training spaced them every NS steps (starting at the first sample).
Nm
Thepre-trainingprocedurelargelyfollowswav2vec 2.0but N first remained ajt 15,k360 (60 s as in training, no overlap
S
we make some notable hyperparameter changes documented between subsequent sequence representations) for all datasets
below.Theprocedureitselfisasfollows:first,theconvolutional except P300, where sessions were too short and instead 5,120
stage of the overall architecture develops a sequence of (20s) was used. We then evaluated the change in performance
FrontiersinHumanNeuroscience|www.frontiersin.org 7 June2021|Volume15|Article653659

Kostasetal. BENDR
FIGURE1|TheoverallarchitectureusedtoconstructBENDR.LossLiscalculatedforamaskedBErt-inspiredNeuralDataRepresentations(BENDR)bt(after
masking,itisreplacedbythelearnedmaskM),itselfproducedfromtheoriginalrawEEG(bottom)viaaprogressionofconvolutionstages.Thetransformerencoder
attemptstoproducecttobemoresimilartobt(despitethatitismasked)thanitistoarandomsamplingofoverBENDR.
across the downstream datasets, excluding P300, as N varied withrespecttothisconcatenatedvectorofaveragedBENDRs
S
from20to60s. (showninFigure2.2).
3. The same as Figure2.1, but perform no pre-training; start
2.4.2.DownstreamFine-Tuning witharandomlyinitializedDNN,asshowninFigure2.3.
Ultimately, our aims for subject-, session-, and dataset- 4. ThesameasFigure2.1,butkeeptheBENDR(convolutional
generalizablerepresentationswerenotsimplytoaccuratelyselect stage)fixedandcontinuetrainingthetransformer(andstart
for the correct input (what was evaluated of the pre-training training the new classification layer) to classify downstream
BENDR and sequence model), but with the intent that these targets,asshowninFigure2.4.
representations (BENDR)—and potentially the sequence model 5. The same as Figure2.2, but perform no pre-training; start
itself—could be effectively transferred to specific and arbitrary with randomly initialized convolution stage, as shown in
tasks. We considered six different variations of TL across the Figure2.5.
battery of downstream EEG classification tasks (classification 6. The same as Figure2.2, but keep the first stage weights
taskslistedinTable1): fixedandtrainonlythenewclassificationlayer,asshownin
Figure2.6.
1. Addanewlinearlayerwithsoftmaxactivation(classification
layer) to the first (recall this position was pre-pended with Figure2providessomeillustrationofeachvariation,wherethe
an input value of −5 to the BENDR) output token of respective indexed subfigures correspond to the list numbers
the transformer. Then, fine-tune the entire model (continue above.Thesewereconsideredsothatwecouldspeaktotheeffect
training the pre-trained model and start training the new each stage had on downstream performance, at least to some
layer)to classifythedownstream targets using theoutput of degree.Wewereinterestedin(1)determiningwhetherthenew
thislayer(ignoringtheremainingsequenceoutputs)(shown sequence representation (BENDR) contained valuable features
inFigure2.1). as-is(astheyappeartobeforspeechBaevskietal.,2020)orifthey
2. Ignorethepre-trainedtransformerentirely,anduseonlythe requiredspecificadaptation,and(2)whetherthesequencemodel
pre-trained convolutional stage (i.e., only use the BENDR). learned characteristics of the BENDR that were informative to
Create a consistent-length representation by dividing the theclassificationtask.Finally,ignoringpre-trainingall-together,
BENDR into four contiguous sub-sequences, average each ofcourse,wastoexaminehoweffectivethenetworkwouldbeat
sub-sequenceandconcatenatethem12.Addanewlinearlayer learningthetaskotherwise,withoutthegeneralpre-trainingtask.
with softmax activation to classify the downstream targets At this stage, we also included the sequence regularization
proposed by wav2vec 2.0 (Baevski et al., 2020), although
12Theselectionoffourherewasarbitrary. we adjusted it for our more varied trial lengths. That is, in
FrontiersinHumanNeuroscience|www.frontiersin.org 8 June2021|Volume15|Article653659

| Kostasetal. |     |     |     |     |     |     |     |     |     |     |     |     | BENDR |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
FIGURE2|Sixdifferentpermutationsofthemodelarchitectureweretrainedwithconventionalfullysupervisedtraining(inaleave-one/multi-subject-outfashion,see
Table1)foreachdownstreamtask.Indicatedhereistheportionoftheoverallarchitecturesused(seeFigure1),andhowpre-trainingmodelweightswereleveraged
forafour-wayclassificationtask(rectanglewithfourcirclesinit).Fourtasks(lefthalf)leveragedmodelweightsthatwerefirstdevelopedthroughpre-training.Allyellow
moduleshereindicaterandomlyinitializedweights.Colorthatprogressesinintensity(frompre-trainingtodownstream)indicatesfurthertraining,whileaddedbars
indicateweightsthatwerekeptunchangedduringthattrainingstage.
all 6 fine-tuning configurations, contiguous sections of 10% of 3. RESULTS
| the entire | BENDR | of a | trial were | masked | with the | mask | token             |     |                |     |     |     |     |
| ---------- | ----- | ---- | ---------- | ------ | -------- | ---- | ----------------- | --- | -------------- | --- | --- | --- | --- |
|            |       |      |            |        |          |      | 3.1. Pre-training |     | Generalization |     |     |     |     |
learnedduringpre-training(notchangedafterpre-training)ata
|             |          |          |        |      |         |            | Figure3   | shows | how accurate  | the     | transformer |       | stage is at |
| ----------- | -------- | -------- | ------ | ---- | ------- | ---------- | --------- | ----- | ------------- | ------- | ----------- | ----- | ----------- |
| probability | of 0.01. | In other | words, | this | was the | likelihood | of a      |       |               |         |             |       |             |
|             |          |          |        |      |         |            | producing | an    | appropriately | similar | BENDR.      | There | are two     |
samplebeingthebeginningofacontiguousmaskedsection,asin
|               |              |     |        |           |             |     | key observations |        | in this   | figure, the    | first is | that there | is little   |
| ------------- | ------------ | --- | ------ | --------- | ----------- | --- | ---------------- | ------ | --------- | -------------- | -------- | ---------- | ----------- |
| pre-training. | Additionally |     | across | the BENDR | (throughout |     | each             |        |           |                |          |            |             |
|               |              |     |        |           |             |     | variability      | across | the first | four datasets, | and      | within     | each of the |
vectorinthesequence),asimilarproceduredroppedfeaturesto
|          |            |          |     |        |              |      | five datasets. | The      | latter point | implies            | that | this accuracy | is not     |
| -------- | ---------- | -------- | --- | ------ | ------------ | ---- | -------------- | -------- | ------------ | ------------------ | ---- | ------------- | ---------- |
| 0, where | contiguous | sections | of  | 10% of | the channels | (51) | were           |          |              |                    |      |               |            |
|          |            |          |     |        |              |      | radically      | variable | across       | different subjects |      | (though,      | when fine- |
droppedwithaprobabilityof0.005.
|           |      |     |              |     |                |     | tuning for | classification, |             | this variability | returns; | see        | Figure5). |
| --------- | ---- | --- | ------------ | --- | -------------- | --- | ---------- | --------------- | ----------- | ---------------- | -------- | ---------- | --------- |
| The P300, | ERN, | and | SSC datasets | all | had imbalanced |     | class      |                 |             |                  |          |            |           |
|           |      |     |              |     |                |     | This could | be              | because (a) | the transformer  |          | adequately | learns a  |
distributions;duringtraining,weadjustedfortheseimbalances
|                 |     |                                         |     |     |     |     | general | model | of how BENDR | sequences | of  | novel | persons and |
| --------------- | --- | --------------------------------------- | --- | --- | --- | --- | ------- | ----- | ------------ | --------- | --- | ----- | ----------- |
| byundersampling |     | pointsuniformlyofthemorefrequentclasses |     |     |     |     |         |       |              |           |     |       |             |
equipmentprogressed;(b)theBENDRthemselvesareinvariant
| with replacement |          | so that     | the number | of            | samples    | drawn—per   |              |            |                  |            |           |          |               |
| ---------------- | -------- | ----------- | ---------- | ------------- | ---------- | ----------- | ------------ | ---------- | ---------------- | ---------- | --------- | -------- | ------------- |
|                  |          |             |            |               |            |             | to different | people,    | hardware,        | and tasks; | (c)       | some     | combination   |
| epoch—of         | each     | class was   | equal      | to the number |            | of examples | of           |            |                  |            |           |          |               |
|                  |          |             |            |               |            |             | of the last  | two        | possibilities;   | or (d) the | problem   | is       | being solved  |
| the least        | frequent | target      | class. As  | the test      | conditions | then        | were         |            |                  |            |           |          |               |
|                  |          |             |            |               |            |             | via some     | non-signal | characteristics. |            | We return | to       | this question |
| imbalanced,      | test     | performance | was        | evaluated     | using      | metrics     | that         |            |                  |            |           |          |               |
|                  |          |             |            |               |            |             | shortly.     | The second | observation      | was        | already   | alluded: | the P300      |
accounted for this, and followed previous work (Baevski et al., datasetdistinctlyunder-performstheotherdownstreamdatasets.
2020;KostasandRudzicz,2020b).Metricsarespecifiedbydataset However, this coincided with the shortest evaluation sequence.
inTable2.
LookingatFigure4,weseethatallfivedatasetshaveconsistently
FrontiersinHumanNeuroscience|www.frontiersin.org 9 June2021|Volume15|Article653659

Kostasetal. BENDR
FIGURE3|Violinplot(innerlinesforquartiledivisions)oftestsubject-wiseaccuracyforeachdownstreamdataset.Specifically,accuracyofthesequencemodel
(transformerstage)atcreatingarepresentationthatisclosesttothecorrectrepresentationatmaskedsequencepositions.TheP300datasetisdistinctlylower
performing(notetheadjustedY-axis)thantheremainingdatasets,thoughthiswaslikelyduetoitsshorterevaluationcontext(seeFigure4).Nonetheless,thereis
minimaltestsubject-wisevariation,particularlywhencomparedtoclassifierperformancegenerally.
similarperformancewhenevaluatedwith20sofdata,sothedip
in P300 performance of Figure3 seems less remarkable. Taken
together, Figures3, 4 clearly indicate that a longer evaluation
contextmakesthecontrastivetaskeasier.Thissuggeststhatthe
contrastive task is, in fact, solved by learning signal-relevant
features,ratherthansomemorecrudesolutionlikeinterpolation,
or by simply creating a sequence of recognizable position
representations (both of which have no reason to exhibit this
dependenceonsequencelength).Webelievethatthemostlikely
explanation for the rise in performance with more context is
thatlocalrepresentationsaremoredifficultdistractors,implying
that the new effective sampling rate remains too high (and
there is still redundant information encoded in local BENDR).
Notwithstanding, there is a strong uniformity of performance
across datasets and subjects (in both Figures3, 4), meaning
thisschemedevelopsfeatures(whetherthroughthetransformer
itself,ortheBENDR)thatgeneralizetonovelsubjects,hardware,
and tasks, though their applicability to downstream contexts FIGURE4|Contrastiveaccuracyvs.evaluationlengthinseconds(x-axis
logarithmic).Performanceisdistinctlysimilarforalldatasets,risingforlonger
remainstobeseen.
sequences.Wesuggestthatthisimpliesthatsamplesthatarefurtherapartare
easiertodistinguishbetweenthanneighboringsamples.Thus,while
BErt-inspiredNeuralDataRepresentations(BENDR)encodelocalsignal
3.2. Downstream Fine-Tuning
characteristicswell,thereisredundancy.
Figure5andTable2presentapictureofhoweffectivelyBENDR
couldbeadaptedtospecifictasks.Overall,thefine-tunedlinear
classification(thedownstreamconfigurationinFigure2.2)that
bypassedthetransformerentirelyafterpre-trainingwashighest generallyineffective,thoughthiswasnotthecasewiththeSSC
performingfouroutoffivetimes,althoughusingthetransformer dataset, which may have been due to the larger amount of
for classification (Figure2.1) performed consistently similarly dataavailableforfullysupervisedlearning.Infact,forboththe
(confidence intervals always overlapped), and surpassed the full and linear model architectures trained with the SSC data,
bypassed transformer (Figure2.2) with the P300 dataset (and fine-tuning the pre-trained model is mostly on par with the
was highest performing for this dataset). Deploying the full fully supervised counterpart. Considering our results with the
network(initialstageandtransformer)withoutpre-training was SSC data relative to those of Banville et al. (2019) proposed
FrontiersinHumanNeuroscience|www.frontiersin.org 10 June2021|Volume15|Article653659

Kostasetal. BENDR
FIGURE5|Performanceofalldownstreamdatasetsforeachofthesixmodelconfigurationsconsidered.Metricsvarybydataset,seeTable2.Metricswere
normalizedtorangefromchance(0)toperfect(1).Individualtranslucentpointsareperformancesofsinglesubjects(withineachtestfold),soliddiamondsindicate
meanperformanceacrossallsubjects/folds,withsurroundingbarsshowing0.95confidenceintervalsusingn=1000bootstrapsampling.Thediscretizedpatternof
theMMIdatasetisduetothelimitedtrialspersubject,whichresultedinlimiteddistributionofperformancelevels.Notablyhere,(1)or(2)wasconsistentlyamongthe
bestperforming,yetbothremainedwithintheconfidencelevelsofeachotherandasidefromafewcaseswiththeERNdatasetdidnotresultinsubjectperformances
thatwereworsethanchance.(3)andespecially(4)and(6)oftenstayedmarginallyabovechance,indicatingthatthepre-trainedfeatureswerenotsufficientwithout
furthertraining.Therandomlyinitializedaverage-pooledBENDRwithlinearclassifier(5)alsoperformedwell,thoughlessconsistently,suggestingpre-trainingwas
neededforconsistentperformance.Modelconfigurationsarenumberedinaccordancewiththelistpresentedinsection2.4.2.
contrastivelearningforsleepstaging(describedinsection1.1), for fine-tuning). Despite that these results were not necessarily
their reported results show that the fine-tuned variants of our stateoftheart,thissinglepre-trainingschemenonethelessshows
ownmodel(1and2)achievedahighermeanbalancedaccuracy a breadth of transferability that is apparently unique, and aside
relative to their two proposed schemes. Taken in concert with from the SSC dataset, consistently here outperforms the fully
our own approach’s wider applicability and more fine-grained supervisedcounterparts.
temporalfeaturedevelopment,webelievethisdemonstratesthat
ours is a promising alternative. Interestingly, with and without 4. DISCUSSION
pre-training (Figure2.2,2.5) achieved similar performance to
Banvilleetal.’sfullysupervisedresults(whereourconfigurations We are unaware of any prior work assessing transformer-
and their architecture employ similar 1D convolution-based based (Vaswani et al., 2017) DNNs with EEG data (raw or
schemes), which is notable as with this dataset, both their otherwise). This is perhaps consistent with the ineffectiveness
“temporal-shuffling” and “relative-positioning” tasks under- we observed with the randomly initialized full architecture
performed this full supervision performance level (though we (Figure2.3) and could imply thateffectiveuse of this powerful
cannotspeaktostatisticalsignificanceofthiscomparison). emerging architecture requires pre-training (or at least enough
Our fine-tuned approaches similarly appear reasonably data, given the better looking SSC performance). This may be
competitive with prior work on the MMI dataset (Dose et al., duetothelargenumberofparametersthatthesemodelsrequire,
2018;KostasandRudzicz,2020b),particularlywhenconsidering making training difficult without sufficient hardware resources.
that only 19 channels (rather than the full set of 64) were The total number of parameters trained in configuration (1) is
being used. Outside of the MMI and SSC dataset, remaining over one billion parameters. Future work should continue to
resultsarenotcompetitivewithmoretargetedsolutions(Kostas evaluate this architecture, particularly as it appears to be more
and Rudzicz, 2020b). Whenever pre-training was not used, widely applicable than the NLP applications it was originally
despite heavy regularization (and the very low learning rates) proposedfor(Baevskietal.,2020;Dosovitskiyetal.,2020).
the randomly initialized parameters were consistently prone to We believe that our approach can be improved through
overfitting, all the more so with the full model architecture. adjusting the neural network architecture and pre-training
Conversely, the pre-trained networks were slow to fit to the configuration such that it becomes more data-domain (EEG)
downstreamtrainingdata(undertheexactsametrainingscheme appropriate. Future work will prioritize effective integration of
FrontiersinHumanNeuroscience|www.frontiersin.org 11 June2021|Volume15|Article653659

| Kostasetal. |     |     |     |     |     |     |     |     |     |     |     | BENDR |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
spatialinformation,likelybybetterisolatingtemporalandspatial into better weight initialization, or integration of explicit early
operations. Evaluation using large downstream datasets that layers similar to Raghu et al. (2019) (one could also argue
also feature many channels, such as the Montreal Archive of that SincNet layers Ravanelli and Bengio, 2018 are some such
SleepStudies(MASS)13 willbeconsidered.Thoughavailablefor layersthatcouldfactorhere).Additionally,astemporallyminded
publicaccessatthetimeofwriting,thesedatawereunavailable reconstruction losses continue to develop (Rivest and Kohar,
while experiments were prepared and conducted. Prior work 2020), reconsidering the effectiveness of signal reconstruction
shows that DNN approaches effective for EEG leverage spatial asapre-trainingobjective(and/orregularization)iswarranted,
information (Chambon et al., 2018), and it is presently unclear whetherthisiswithinanMLM-likeschemesimilartoBENDR,
to what degree this is the case with BENDR. In terms of data- oraseq2seqmodel(Graves,2012).
appropriatetemporalmodeling,whichwehaveconsideredwith
relativelymorezealinthiswork,recallthatFigure4presentsthe 5. CONCLUSION
possibilitythatlocalrepresentationsmayberetainingredundant
information, further improvements therefore may be found in We have proposed MLM-like training as a self-supervised pre-
better compressing the temporal resolution of BENDR. Future training step for BCI/EEG DNNs. This is in the interest of
work will consider larger downsampling factors in the initial diversifying the investigations into successful transfer learning
stage,alongwithlongersequences,balancingthemoredifficult schemes for DNNs applied to BCI and EEG with possible
problem of summarizing more data (in effect, further data applicability to neuroimaging more generally. While previous
| compression), | with | the apparent |     | increased | effectiveness |     | of the |     |     |     |     |     |
| ------------- | ---- | ------------ | --- | --------- | ------------- | --- | ------ | --- | --- | --- | --- | --- |
approachesfashionedDNNtransferlearningafterImageNetpre-
contrastive task (as observed in Figure4) on longer sequences. training, we find this approach inadequate as there is limited
Asmallbutpotentiallyfruitfulavenueforfurtherimprovement applicable data availability and it is questionably analogous to
includes reconsidering the additive convolutional layer as a its forebear. While our proposed alternative might similarly
substitute for explicit position encodings, which are in fact suffer from this latter point to some degree (the most distinct
more common (Vaswani et al., 2017; Devlin et al., 2019; Raffel MLM success is with discrete sequences, not continuous
et al., 2020). Recall that this was originally for two reasons: ones), it is more conducive to leveraging potentially immense
| wav2vec | 2.0didthesame,andwefeltitbesttolimitexcessive |     |     |     |     |     |         |              |       |                   |     |              |
| ------- | --------------------------------------------- | --- | --- | --- | --- | --- | ------- | ------------ | ----- | ----------------- | --- | ------------ |
|         |                                               |     |     |     |     |     | amounts | of unlabeled | data, | it is not limited |     | to long-term |
changestothearchitectureonafirstiteration,andalsobecause feature developments as with previous proposals, and it seems
it seamlessly supported flexible input lengths. This latter point to produce representations equally suited to different users
comeshowever,withatrade-off:ourparticularpositionencoder
|     |     |     |     |     |     |     | and sessions, | which is | a problem | previous | work | appears less |
| --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | --------- | -------- | ---- | ------------ |
had a receptive field of 25 (stride of 1), which means a little suited to solving. In summary, we see strong paths for the
over 9 s of input. While it seems that convolutional position effective deployment of powerful computation and massive
encodings offer better performance (Mohamed et al., 2019), data scales with EEG and BCI. Effective solutions in these
this input width exceeded the entire length of all but the sleep specific applications could help drive application and analysis
classification task (the length we chose was optimized for pre- solutions in neuroimaging and perhaps physiological signal
| trainingbehavior). |             |                 |                |         |          |               | analysisgenerally. |               |           |        |       |              |
| ------------------ | ----------- | --------------- | -------------- | ------- | -------- | ------------- | ------------------ | ------------- | --------- | ------ | ----- | ------------ |
| After              | considering | these           | possible       | avenues |          | for improving |                    |               |           |        |       |              |
| BENDR,             | we still    | do not          | fully discount | the     | validity | of some       | of                 |               |           |        |       |              |
|                    |             |                 |                |         |          |               | DATA               | AVAILABILITY  | STATEMENT |        |       |              |
| the transfer       | learning    | paths           | we appear      | to      | exclude  | above         | in our             |               |           |        |       |              |
| introduction.      | We          | will reconsider |                | these   | paths in | future        | work.              |               |           |        |       |              |
|                    |             |                 |                |         |          |               | The original       | contributions | presented | in the | study | are included |
Particularly,giventhesuccesswehadincrossingboundariesof
|     |     |     |     |     |     |     | in the article/supplementary |     | material, | further | inquiries | can be |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --------- | ------- | --------- | ------ |
hardwareinthiswork,andinpriorwork(KostasandRudzicz,
directedtothecorrespondingauthor/s.
| 2020a),   | it may    | be possible | to construct   |     | an aggregate |        | dataset |               |     |     |     |     |
| --------- | --------- | ----------- | -------------- | --- | ------------ | ------ | ------- | ------------- | --- | --- | --- | --- |
| featuring | a variety | of EEG      | classification |     | tasks        | toward | better  |               |     |     |     |     |
|           |           |             |                |     |              |        | AUTHOR  | CONTRIBUTIONS |     |     |     |     |
ImageNet-likepre-training.Theconstructionofamorecoherent
| label set | that crosses | several | BCI | paradigms | would | no  | doubt |     |     |     |     |     |
| --------- | ------------ | ------- | --- | --------- | ----- | --- | ----- | --- | --- | --- | --- | --- |
be a significant effort (e.g., problems may include: is a rest DK conceived of the presented idea, designed experiments,
|     |     |     |     |     |     |     | performed | the analysis, | drafted | the manuscript, |     | and designed |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | ------- | --------------- | --- | ------------ |
periodbeforeonetaskparadigmthesameasrestbeforeanother?
thefigures.DKdevelopedimplementationwithassistancefrom
Whataboutwakefulperiodsinsleep?).Thiswouldnodoubtbe
imbalanced; the labels would be distributed in a long-tailed or SA-O.SA-OandFReditedmanuscript.FRprovidedsupervision
throughout.Allauthorscontributedtothearticleandapproved
| Zipfian                                                   | distribution | that          | would likely | require | well     | thought-out  |                      |     |     |     |     |     |
| --------------------------------------------------------- | ------------ | ------------- | ------------ | ------- | -------- | ------------ | -------------------- | --- | --- | --- | --- | --- |
|                                                           |              |               |              |         | 2020).13 |              | thesubmittedversion. |     |     |     |     |     |
| adjustment                                                | (Cao         | et al., 2019; | Tang         | et al., |          | Furthermore, |                      |     |     |     |     |     |
| the value                                                 | of ImageNet  | pre-training  |              | seems   | to       | be localized | to                   |     |     |     |     |     |
| veryearlylayersandtheinternalizationofdomain-relevantdata |              |               |              |         |          |              | FUNDING              |     |     |     |     |     |
| statistics                                                | (Raghu       | et al., 2019; | Neyshabur    |         | et al.,  | 2020).       | Future               |     |     |     |     |     |
work could look into which of these may be leveraged with a This work was supported by grants from the Electronics
newaggregate(multiplesubjectsandtasks)pre-training,orthe and Telecommunications Research Institute (South Korea)
common subject-specific fine-tuning. This may provide insight [20ZS1100, Core Technology Research for Self-Improving
IntegratedArtificialIntelligenceSystem]andNSERCDiscovery
13http://massdb.herokuapp.com/en/ [435874].RudziczholdsaCIFARChairinAI.
FrontiersinHumanNeuroscience|www.frontiersin.org 12 June2021|Volume15|Article653659

Kostasetal. BENDR
REFERENCES
edsJ.Burstein,C.Doran,andT.Solorio(Minneapolis,MN:Associationfor
ComputationalLinguistics),4171–4186.doi:10.18653/v1/n19-1423
Ahn, M., and Jun, S. C. (2015). Performance variation in motor imagery Ditthapron, A., Banluesombatkul, N., Ketrat, S., Chuangsuwanich, E., and
brain-computerinterface:abriefreview.J.Neurosci.Methods243,103–110. Wilaiprasitporn,T.(2019).UniversaljointfeatureextractionforP300EEG
doi:10.1016/j.jneumeth.2015.01.033 classification using multi-task autoencoder. IEEE Access 7, 68415–68428.
Aroca-Ouellette, S., and Rudzicz, F. (2020). “On Losses for Modern Language doi:10.1109/ACCESS.2019.2919143
Models,”inProceedingsofthe2020ConferenceonEmpiricalMethodsinNatural Dose,H.,Møller,J.S.,Iversen,H.K.,andPuthusserypady,S.(2018).Anend-to-
Language Processing (EMNLP) (Association for Computational Linguistics), enddeeplearningapproachtoMI-EEGsignalclassificationforBCIs.Exp.Syst.
4970–4981. Available online at: https://www.aclweb.org/anthology/2020. Appl.114,532–542.doi:10.1016/j.eswa.2018.08.031
emnlp-main.403 Dosovitskiy,A.,Beyer,L.,Kolesnikov,A.,Weissenborn,D.,Zhai,X.,Unterthiner,
Arora,S.,Khandeparkar,H.,Khodak,M.,Plevrakis,O.,andSaunshi,N.(2019). T., et al. (2020). An image is worth 16x16 words: transformers for image
“Atheoreticalanalysisofcontrastiveunsupervisedrepresentationlearning,”in recognitionatscale.arXivarXiv:2010.11929.
36thInternationalConferenceonMachineLearning,ICML2019(LongBeach, Fahimi,F.,Zhang,Z.,Goh,W.B.,Lee,T.-S.,Ang,K.K.,andGuan,C.(2019).Inter-
CA),Vol.2019-June,9904–9923. subjecttransferlearningwithanend-to-enddeepconvolutionalneuralnetwork
Baevski, A., and Mohamed, A. (2020). “Effectiveness of self-supervised pre- forEEG-basedBCI.J.NeuralEng.16:026007.doi:10.1088/1741-2552/aaf3f6
training for ASR,” in ICASSP 2020-2020 IEEE International Conference on Fan, A., Grave, E., and Joulin, A. (2019). Reducing transformer depth on
Acoustics,SpeechandSignalProcessing(ICASSP)(Barcelona:IEEE),7694–7698. demandwithstructureddropout.arXiv103,1–15.Availableonlineat:https://
Baevski, A., Zhou, Y., Mohamed, A., and Auli, M. (2020). “wav2vec 2.0: openreview.net/forum?id=SylO2yStDr
a framework for self-supervised learning of speech representations,” Gemein, L. A., Schirrmeister, R. T., Chraba¸szcz, P., Wilson, D., Boedecker, J.,
in Advances in Neural Information Processing Systems 33: Annual Schulze-Bonhage,A.,etal.(2020).Machine-learning-baseddiagnosticsofEEG
Conference on Neural Information Processing Systems 2020, NeurIPS pathology.Neuroimage220:17021.doi:10.1016/j.neuroimage.2020.117021
2020, eds H. Larochelle, M. Ranzato, R. Hadsell, M. F. Balcan, and H. T. Goldberger,A.L.,Amaral,L.A.,Glass,L.,Hausdorff,J.M.,Ivanov,P.C.,Mark,
Lin. Available online at: https://proceedings.neurips.cc/paper/2020/hash/ R.G.,etal.(2000).PhysioBank,physioToolkit,andphysioNet:componentsof
92d1e1eb1cd6f9fba3227870bb6d7f07-Abstract.html anewresearchresourceforcomplexphysiologicsignals.Circulation101:E215–
Banville, H., Albuquerque, I., Hyvarinen, A., Moffat, G., Engemann, D.-A., E220.doi:10.1161/01.cir.101.23.e215
and Gramfort, A. (2019). “Self-supervised representation learning from Graves,A.(2012).SupervisedSequenceLabellingwithRecurrentNeuralNetworks.
electroencephalographysignals,”in2019IEEE29thInternationalWorkshopon Berlin;NewYork:Springer,c2012.
MachineLearningforSignalProcessing(MLSP)(Pittsburgh,PA:IEEE),1–6. Grill, J. B., Strub, F., Altché, F., Tallec, C., Richemond, P. H., Buchatskaya,
Banville, H., Chehab, O., Hyvärinen, A., Engemann, D.-A., and Gramfort, A. E., et al. (2020). “Bootstrap your own latent - a new approach to self-
(2020).UncoveringthestructureofclinicalEEGsignalswithself-supervised supervisedlearning,”AdvancesinNeuralInformationProcessingSystems33:
learning.J.NeuralEng.18:046020.doi:10.1088/1741-2552/abca18 AnnualConferenceonNeuralInformationProcessingSystems2020,NeurIPS
Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., et 2020, eds H. Larochelle, M. Ranzato, R. Hadsell, M. F. Balcan, and H.
al. (2020). “Language models are few-shot learners,” in Advances in Neural T. Lin. Available online at: https://proceedings.neurips.cc/paper/2020/hash/
InformationProcessingSystems33:AnnualConferenceonNeuralInformation f3ada80d5c4ee70142b17b8192b2958e-Abstract.html
Processing Systems 2020, NeurIPS 2020, eds H. Larochelle, M. Ranzato, R. He,K.,Girshick,R.,andDollar,P.(2019).“RethinkingimageNetpre-training,”in
Hadsell,M.F.Balcan,andH.T.Lin.Availableonlineat:https://proceedings. ProceedingsoftheIEEEInternationalConferenceonComputerVision(Seoul),
neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract. 4917–4926.
html He, K., Zhang, X., Ren, S., and Sun, J. (2016). “Deep residual learning for
Cao,K.,Wei,C.,Gaidon,A.,Arechiga,N.,andMa,T.(2019).Learningimbalanced imagerecognition,”in2016IEEEConferenceonComputerVisionandPattern
datasetswithlabel-distribution-awaremarginloss.Adv.NeuralInf.Proc.Syst. Recognition(CVPR)2016(LasVegas,NV:IEEEComputerSociety),770–778.
32,1–18.Availableonlineat:https://proceedings.neurips.cc/paper/2019/hash/ doi:10.1109/CVPR.2016.90
621461af90cadfdaf0e8d4cc25129f91-Abstract.html Hénaff,O.J.(2020).“Data-efficientimagerecognitionwithcontrastivepredictive
Chambon,S.,Galtier,M.N.,Arnal,P.J.,Wainrib,G.,andGramfort,A.(2018). coding,” in Proceedings of the 37th International Conference on Machine
A deep learning architecture for temporal sleep stage classification using Learning,ICML2020,Vol.119(PMLR),4182–4192.Availableonlineat:http://
multivariateandmultimodaltimeseries.IEEETrans.NeuralSyst.Rehabil.Eng. proceedings.mlr.press/v119/henaff20a.html
26,758–769.doi:10.1109/TNSRE.2018.2813138 Hendrycks, D., and Gimpel, K. (2016). Bridging nonlinearities and
Chen,K.,Wang,J.,Chen,L.-C.,Gao,H.,Xu,W.,andNevatia,R.(2016).ABC- stochastic regularizers with Gaussian error linear units. arXiv arXiv:1606.
CNN: an attention based convolutional neural network for visual question 08415.
answering.arXiv. Huang,G.,Liu,Z.,vanderMaaten,L.,andWeinberger,K.Q.(2017).“Densely
Chen, T., Kornblith, S., Swersky, K., Norouzi, M., and Hinton, G. (2020). Big connected convolutional networks,” in 2017 IEEE Conference on Computer
self-supervisedmodelsarestrongsemi-supervisedlearners.arXiv1–18. VisionandPatternRecognition,CVPR2017 (Honolulu,HI:IEEEComputer
Chung, Y.-A.,Tang,H.,and Glass,J.(2020).“Vector-quantized autoregressive Society),2261–2269.doi:10.1109/CVPR.2017.243
predictivecoding,”inInterspeech2020,Vol.arXiv(Shanghai:ISCA),3760– Huang,X.S.,Perez,F.,Ba,J.,andVolkovs,M.(2020).“Improvingtransformer
3764. optimizationthroughbetterinitialization,”inProceedingsofMachineLearning
Cimtay, Y., and Ekmekcioglu, E. (2020). Investigating the use of pretrained andSystems2020,9868–9876.
convolutionalneuralnetworkoncross-subjectandcross-dataseteegemotion Huh,M.,Agrawal,P.,andEfros,A.A.(2016).WhatmakesimageNetgoodfor
recognition.Sensors 20,1–20.doi:10.3390/s20072034 transferlearning?CoRR1–10.
Citi,L.,Poli,R.,andCinel,C.(2010).Documenting,modellingandexploitingP300 Jiang,D.,Li,W.,Zhang,R.,Cao,M.,Luo,N.,Han,Y.,etal.(2020).Afurtherstudy
amplitudechangesduetovariabletargetdelaysinDonchinsspeller.J.Neural ofunsupervisedpre-trainingfortransformerbasedspeechrecognition.arXiv
Eng.7:056006.doi:10.1088/1741-2560/7/5/056006 arXiv:2005.09862.
Citi, L., Poli, R., and Cinel, C. (2014). Erp-based brain-computer interface Joshi,M.,Chen,D.,Liu,Y.,Weld,D.S.,Zettlemoyer,L.,andLevy,O.(2020).
recordings.doi:10.13026/C2101S SpanBERT: improving pre-training by representing and predicting spans.
Deng,J.,Dong,W.,Socher,R.,Li,L.-J.,Li,K.,andFei-Fei,L.(2009).“ImageNet:a Trans.Assoc.Comput.Linguist.8,64–77.doi:10.1162/tacl_a_00300
large-scalehierarchicalimagedatabase,”inCVPR09(MiamiBeach,FL). Jurcak,V.,Tsuzuki,D.,andDan,I.(2007).10/20,10/10,and10/5systemsrevisited:
Devlin,J.,Chang,M.W.,Lee,K.,andToutanova,K.(2019).“BERT:pre-training theirvalidityasrelativehead-surface-basedpositioningsystems.Neuroimage
ofdeepbidirectionaltransformersforlanguageunderstanding,”inProceedings 34,1600–1611.doi:10.1016/j.neuroimage.2006.09.024
ofthe2019ConferenceoftheNorthAmericanChapteroftheAssociationfor Kemp,B.,Zwinderman,A.,Tuk,B.,Kamphuisen,H.,andOberyé,J.(2018).The
ComputationalLinguistics:HumanLanguageTechnologies,NAACL-HLT2019, sleep-edfdatabase[expanded].doi:10.13026/C2X676
FrontiersinHumanNeuroscience|www.frontiersin.org 13 June2021|Volume15|Article653659

Kostasetal. BENDR
Kemp, B., Zwinderman, A. H., Tuk, B., Kamphuisen, H. A., and Oberyé, J. J. Sannelli, C., Vidaurre, C., Müller, K.-R., and Blankertz, B. (2019). A large
(2000).Analysisofasleep-dependentneuronalfeedbackloop:theslow-wave scale screening study with a SMR-based BCI: categorization of BCI
microcontinuity of the EEG. IEEE Trans. Biomed. Eng. 47, 1185–1194. users and differences in their SMR activity. PLoS ONE 14:e0207351.
doi:10.1109/10.867928 doi:10.1371/journal.pone.0207351
Kingma, D. P., and Ba, J. L. (2015). “Adam: a method for stochastic Schalk,G.,Mcfarland,D.J.,Hinterberger,T.,Birbaumer,N.,Wolpaw,J.R.,and
optimization,”3rdInternationalConferenceonLearningRepresentations,ICLR Technology,A.B.-C.I.B.C.I.(2004).BCI2000:ageneral-purposebrain-
2015-ConferenceTrackProceedings(SanDiego,CA),1–15. computerinterface(BCI)system.IEEETrans.Biomed.Eng.51,1034–1043.
Kornblith,S.,Shlens,J.,andLe,Q.V.(2019).“Dobetterimagenetmodelstransfer doi:10.1109/TBME.2004.827072
better?”inProceedingsoftheIEEEComputerSocietyConferenceonComputer Schirrmeister, R. T., Springenberg, J. T., Fiederer, L. D. J., Glasstetter, M.,
VisionandPatternRecognition(LongBeach,CA),2656–2666. Eggensperger, K., Tangermann, M., et al. (2017). Deep learning with
Kostas,D.,Pang,E.W.,andRudzicz,F.(2019).MachinelearningforMEGduring convolutionalneuralnetworksforEEGdecodingandvisualization.Hum.Brain
speechtasks.Sci.Rep.9:1609.doi:10.1038/s41598-019-38612-9 Mapp.38,5391–5420.doi:10.1002/hbm.23730
Kostas,D.,andRudzicz,F.(2020a).Dn3:anopen-sourcepythonlibraryforlarge- Schwemmer, M. A., Skomrock, N. D., Sederberg, P. B., Ting, J. E., Sharma,
scalerawneurophysiologydataassimilationformoreflexibleandstandardized G.,Bockbrader,M.A.,etal.(2018).Meetingbrain-computerinterfaceuser
deeplearning.bioRxiv.doi:10.1101/2020.12.17.423197 performanceexpectationsusingadeepneuralnetworkdecodingframework.
Kostas, D., and Rudzicz, F. (2020b). Thinker invariance: enabling deep Nat.Med.24,1669–1676.doi:10.1038/s41591-018-0171-y
neural networks for BCI across more people. J. Neural Eng. 17:56008. Sejnowski, T. J. (2020). The unreasonable effectiveness of deep learning
doi:10.1088/1741-2552/abb7a7 in artificial intelligence. Proc. Natl. Acad. Sci. U.S.A. 117, 30033–30038.
Krizhevsky,A.,Sutskever,I.,andHinton,G.E.(2012).“ImageNetclassification doi:10.1073/pnas.1907373117
with deep convolutional neural Networks,” in Proceedings of the 25th Tang,K.,Huang,J.,andZhang,H.(2020).Long-tailedclassificationbykeepingthe
International Conference on Neural Information Processing Systems, Vol. 1, goodandremovingthebadmomentumcausaleffect.NeurIPS1–12.
NIPS’12(LakeTahoe:CurranAssociatesInc.),1097–1105. Tangermann,M.,Müller,K.R.,Aertsen,A.,Birbaumer,N.,Braun,C.,Brunner,
Lawhern, V. J., Solon, A. J., Waytowich, N. R., Gordon, S. M., Hung, C., et al. (2012). Review of the BCI competition IV. Front. Neurosci. 6:55.
C. P., and Lance, B. J. (2018). EEGNet: a compact convolutional neural doi:10.3389/fnins.2012.00055
networkforEEG-basedbrain-computerinterfaces.J.NeuralEng.15:aace8c. vandenOord,A.,Li,Y.,andVinyals,O.(2018).Representationlearningwith
doi:10.1088/1741-2552/aace8c contrastivepredictivecoding.arXivarXiv:1807.03748.
LeCun,Y.,Bengio,Y.,andHinton,G.(2015).Deeplearning.Nature521,436–444. Vaswani,A.,Shazeer,N.,Parmar,N.,Uszkoreit,J.,Jones,L.,Gomez,A.N.,et
doi:10.1038/nature14539 al. (2017). “Attention is all you need,” in Advances in Neural Information
Lin,Y.-P.,andJung,T.-P.(2017).ImprovingEEG-basedemotionclassification Processing Systems 30: Annual Conference on Neural Information Processing
using conditional transfer learning. Front. Hum. Neurosci. 11:334. Systems 2017, eds I. Guyon, U. von Luxburg, S. Bengio, H. M. Wallach,
doi:10.3389/fnhum.2017.00334 R. Fergus, S. V. N. Vishwanathan, and R. Garnett (Long Beach, CA),
Lotte,F.,Bougrain,L.,Cichocki,A.,Clerc,M.,Congedo,M.,Rakotomamonjy, 5998–6008. Available online at: https://proceedings.neurips.cc/paper/2017/
A., et al. (2018). A review of classification algorithms for EEG-based hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html
brain-computer interfaces: a 10 year update. J. Neural Eng. 15:031005. Vidaurre,C.,andBlankertz,B.(2010).TowardsacureforBCIilliteracy.Brain
doi:10.1088/1741-2552/aab2f2 Topography23,194–198.doi:10.1007/s10548-009-0121-6
Margaux, P., Emmanuel, M., Sébastien, D., Olivier, B., and Jérémie, M. Wu,Y.,andHe,K.(2020).Groupnormalization.Int.J.Comput.Vis.128,742–755.
(2012). Objective and subjective evaluation of online error correction doi:10.1007/s11263-019-01198-w
during P300-Based spelling. Adv. Hum. Comput. Interact. 2012, 1–13. Xu, G., Shen, X., Chen, S., Zong, Y., Zhang, C., Yue, H., et al. (2019).
doi:10.1155/2012/578295 A deep transfer convolutional neural network framework for EEG signal
Mohamed, A., Okhonko, D., and Zettlemoyer, L. (2019). Transformers with classification. IEEE Access 7, 112767–112776. doi: 10.1109/ACCESS.2019.29
convolutionalcontextforASR.arXiv. 30958
Mousavi,S.,Afghah,F.,andAcharya,U.R.(2019).SleepEEGNet:automatedsleep Yosinski, J., Clune, J., Nguyen, A. M., Fuchs, T. J., and Lipson, H.
stagescoringwithsequencetosequencedeeplearningapproach.PLoSONE (2015). Understanding neural networks through deep visualization. arXiv
14:e0216456.doi:10.1371/journal.pone.0216456 arXiv:1506.06579.
Neyshabur,B.,Sedghi,H.,andZhang,C.(2020).“Whatisbeingtransferredin Zanini, P., Congedo, M., Jutten, C., Said, S., and Berthoumieu, Y. (2018).
transferlearning?,”inAdvancesinNeuralInformationProcessingSystems33: Transfer learning: a riemannian geometry framework with applications
AnnualConferenceonNeuralInformationProcessingSystems2020,NeurIPS to brain-computer interfaces. IEEE Trans. Biomed. Eng. 65, 1107–1116.
2020, eds H. Larochelle, M. Ranzato, R. Hadsell, M. F. Balcan, and H. doi:10.1109/TBME.2017.2742541
T. Lin. Available online at: https://proceedings.neurips.cc/paper/2020/hash/ Zhang,D.,Chen,K.,Jian,D.,andYao,L.(2020a).Motorimageryclassification
0607f4c705595b911a4f3e7a127b44e0-Abstract.html via temporal attention cues of graph embedded EEG signals. IEEE
Ngiam,J.,Peng,D.,Vasudevan,V.,Kornblith,S.,Le,Q.V.,andPang,R.(2018). J. Biomed. Health Informat. 24, 2570–2579. doi: 10.1109/JBHI.2020.2
Domainadaptivetransferlearningwithspecialistmodels.arXiv. 967128
Obeid,I.,andPicone,J.(2016).ThetempleuniversityhospitalEEGdatacorpus. Zhang, X., Yao, L., Wang, X., Monaghan, J. J. M., Mcalpine, D., and
Front.Neurosci.10:196.doi:10.3389/fnins.2016.00196 Zhang, Y. (2020b). A survey on deep learning-based non-invasive brain
Raffel,C.,Shazeer,N.,Roberts,A.,Lee,K.,Narang,S.,Matena,M.,etal.(2020). signals: recent advances and new frontiers. J. Neural Eng. 18:031002.
Exploringthelimitsoftransferlearningwithaunifiedtext-to-texttransformer. doi:10.1088/1741-2552/abc902
J.Mach.Learn.Res.21,140:1–140:67.
Raghu, M., Zhang, C., Kleinberg, J., and Bengio, S. (2019). Transfusion: ConflictofInterest:Theauthorsdeclarethattheresearchwasconductedinthe
Understandingtransferlearningformedicalimaging.arXiv. absenceofanycommercialorfinancialrelationshipsthatcouldbeconstruedasa
Ravanelli, M., and Bengio, Y. (2018). Interpretable convolutional filters with potentialconflictofinterest.
sincNet.Arxiv.
Rivest, F., and Kohar, R. (2020). A new timing error cost function for binary Copyright©2021Kostas,Aroca-OuelletteandRudzicz.Thisisanopen-accessarticle
time series prediction. IEEE Trans. Neural Netw. Learn. Syst. 31, 174–185. distributedunderthetermsoftheCreativeCommonsAttributionLicense(CCBY).
doi:10.1109/TNNLS.2019.2900046 Theuse,distributionorreproductioninotherforumsispermitted,providedthe
Roy, Y., Banville, H., Albuquerque, I., Gramfort, A., Falk, T. H., and original author(s) and the copyright owner(s) are credited and that the original
Faubert, J. (2019). Deep learning-based electroencephalography analysis: publicationinthisjournaliscited,inaccordancewithacceptedacademicpractice.
a systematic review. J. Neural Eng. 16:051001. doi: 10.1088/1741-2552/ Nouse,distributionorreproductionispermittedwhichdoesnotcomplywiththese
ab260c terms.
FrontiersinHumanNeuroscience|www.frontiersin.org 14 June2021|Volume15|Article653659

Kostasetal. BENDR
APPENDIX
| Downstream | hyperparameters |     |     |
| ---------- | --------------- | --- | --- |
TABLEA1|Hyperparametersthatvariedbetweendatasets,andthesewerenot
changedbetweendifferentmodelconfigurations(seelistinsection2.4.2).
| Dataset | BatchSize | Epochs | LearningRate |
| ------- | --------- | ------ | ------------ |
| MMI     | 4         | 7      | 1×10−5       |
| BCIC    | 60        | 15     | 5×10−5       |
| ERN     | 32        | 15     | 1×10−5       |
| P300    | 80        | 20     | 1×10−5       |
5×10−5
| SSC | 64  | 40  |     |
| --- | --- | --- | --- |
FrontiersinHumanNeuroscience|www.frontiersin.org 15 June2021|Volume15|Article653659