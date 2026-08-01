Review of Deep Representation Learning
Techniques for Brain-Computer Interfaces and
Recommendations
Pierre Gueschel† , Sara Ahmadi† , Michael Tangermann
DondersInstituteforBrain,CognitionandBehavior,RadboudUniversity,
Nijmegen,Netherlands
E-mail: pierre.guetschel@donders.ru.nl
Abstract.
In the field of brain-computer interfaces (BCIs), the potential for leveraging
deep learning techniques for representing electroencephalogram (EEG) signals
has gained substantial interest. This review synthesizes empirical findings from
a collection of articles using deep representation learning techniques for BCI
decoding, to provide a comprehensive analysis of the current state-of-the-art.
Each article was scrutinized based on three criteria: (1) the deep representation
learningtechniqueemployed,(2)theunderlyingmotivationforitsutilization,and
(3)theapproachesadoptedforcharacterizingthelearnedrepresentations. Among
the 81 articles finally reviewed in depth, our analysis reveals a predominance of
31articlesusingautoencoders. Weidentified13studiesemployingself-supervised
learning (SSL) techniques, among which ten were published in 2022 or later,
attesting to the relative youth of the field. However, at the time being, none
of these have led to standard foundation models that are picked up by the
BCI community. Likewise, only a few studies have introspected their learned
representations. We observed that the motivation in most studies for using
representation learning techniques is for solving transfer learning tasks, but we
alsofoundmorespecificmotivationssuchastolearnrobustnessorinvariances,as
analgorithmicbridge, orfinallytouncoverthestructureofthedata. Giventhe
potentialoffoundationmodelstoeffectivelytacklethesechallenges,weadvocate
for a continued dedication to the advancement of foundation models specifically
designed for EEG signal decoding by using SSL techniques. We also underline
the imperative of establishing specialized benchmarks and datasets to facilitate
thedevelopmentandcontinuousimprovementofsuchfoundationmodels.
Keywords: Review, EEG, BCI, Representation, Embedding, Deep Learning
Submitted to: J. Neural Eng.
† Theseauthorscontributedequallytothiswork.
4202
yaM
71
]PS.ssee[
1v54391.5042:viXra

Review of Deep Representation Learning Techniques for BCI and Recommendations 2
1. Introduction hyperparameters, trained models or other information
which had been obtained from earlier recordings or
Representing high-dimensional data elements into earlier users to a novel recording or user. Transfer
lower-dimensional vectors usually facilitates their learning is of particular interest within the BCI
processingbysubsequentmachinelearningalgorithms. community [46, 122], as it may help to solve a
This representational process is called embedding and central problem in research and clinical applications
is carried out by an embedding function. The low- of BCI: Training a decoding method from scratch
dimensional vectors obtained are called embedding for a novel user or session is challenged by a lack
vectors or embeddings also for short. In deep learning, of time. However, there are several caveats to
we typically consider that any intermediate data consider. Firstly, there may be potential changes
representation of neural networks can be regarded as in strategies between subjects. Secondly, the exact
embeddings. However, in this article, we will focus location, timing, intensities, and frequencies of neural
on studies that either explicitly introspect, or that use activity may vary between individuals, along with
algorithms that directly optimize the embedding. The their brain morphologies. Thirdly, individual lesions
termsembeddingvector andrepresentation willbeused in stroke patients and individual progress patterns
interchangeably in the following. and deficits in neurodegenerative diseases can affect
For this article, we consider embeddings in the transfer learning. Lastly, various confounding factors
context of brain-computer interfaces (BCIs). BCIs suchasmedication, sleeppatterns, impreciseelectrode
are systems that allow direct communication from a placements, artefacts and environmental factors can
subject’s brain to a computer, omitting motor output. also lead to non-stationarities in the signals.
This is realized by recording brain activity, decoding This review is motivated by observing a growing
the recorded signals and interpreting the decoded number of publications in the BCI field during
information. The decoding outcomes are interpreted recent years, which have used embedding techniques.
either as brain states of interest which are to be However, it is unclear which techniques are most
monitored over time, or as control commands that commonly used to learn embeddings for BCI. In
are send to the computer. State-of-the-art BCIs for addition, it is not established which alternative deep
controlling devices or computer applications decode learning approaches so far have remained unexplored
changes of brain activity which are a response to in BCI and which benefits they could bring. Finally,
either an external stimulus or the result of a subject it might also be valuable for the BCI community to
actively executing a mental task. As brain activity see which purposes exactly serve the different types
is predominantly recorded via electroencephalogram of embedding and how they can be benchmarked and
(EEG), we will primarily focus on this type of BCI introspected.
in this article. This recording modality has the In this review article, our focus is three-
advantage a relatively low cost compared to other fold. Firstly, we focus on the potential motivations
recordingtechniquessuchasmagnetoencephalography researchers have for using embeddings. Indeed, we
and functional magnetic resonance tomography, and observe that the use of DL-based representations in
is often preferred over local field potentials, signals BCI can be motivated by multiple different reasons.
from stereotactic EEG or electrocardiography due to Secondly,thisreviewarticleaimstodrawthespectrum
its non-invasiveness. BCIs based on EEG reflects of possible methods that can be used for embedding
electrical brain activity with minimal delay and learning, and more generally feature learning, using
a relatively high temporal resolution, allowing to deep learning (DL) for BCI applications. Lastly,
build applications which impose high demands in the we look at introspection techniques for embeddings.
temporal domain. Here, the data elements to be These techniques can be informative for comparing
represented as embedding vectors consist of short and evaluating embeddings, and reveal what type of
windows of EEG time-series signals, i.e., epochs or information can be obtained from them. Throughout
trials. this article we will explore the literature on deep
Embedding vectors serve as a fundamental representation learning for BCI. Additionally, we will
framework for transfer learning or domain adaptation. have a view on studies involving non-BCI EEG data
These terms describe the approach to employ data, with the purpose to potentially identify research gaps

Review of Deep Representation Learning Techniques for BCI and Recommendations 3
in the BCI field. Furthermore, we will also provide in the search engines.
examples from leading deep learning domains, such as We initially started by using three search engines:
computer vision, natural language processing (NLP), Web of Science, PubMed and Google Scholar.
and speech processing, to illustrate the potential of Unfortunately, Google Scholar did not allow for
deep representation learning for the field of BCI. nesting terms in parenthesis. In a second attempt,
This article is organized as follows: in Section 2, we computed the disjunctive normal form of our
our approaches for retrieving and filtering articles and expression (which removes the need for parenthesis)
for extracting information are introduced. Section 3 butitresultedina8568termsexpressionwhichhitthe
explores different possible motivations for learning an 150-wordlimitofGoogleScholar. Therefore,wehadto
embeddingorusinganalgorithmthatintrinsicallydoes dropGoogleScholarandonlyusedWebofScienceand
that. In Section 4, we will draw a list of the different PubMed. The matching articles were gathered using
approaches that have been used to learn embeddings PublishorPerish[41]andorganizedusingZotero[116].
intheBCIfield. Wewillalsoreportalgorithmsusedin We found 87 articles from Web of Science and
neighbouringfieldsfornon-BCI,butEEGdata,asthey 43 from PubMed, which resulted in 101 articles after
couldberelevantforBCI.Finally,inSection5,wewill removing duplicates. This search was conducted on
explorethedifferentmethodsthathavebeenproposed April 1st 2024. We read all the titles and found that
to benchmark, qualify, and compare the embeddings 25 were off-topic, which left us with 76. Among those,
learned. five were behind a paywall for which we did not have
|     |     |     |     |     |     | access, | three | were not | in  | English | and one | was not |
| --- | --- | --- | --- | --- | --- | ------- | ----- | -------- | --- | ------- | ------- | ------- |
2. Our Methodology available. This left us with 67 articles. We read the 67
|     |     |     |     |     |     | abstracts | and | found | that eleven | articles | were | still off- |
| --- | --- | --- | --- | --- | --- | --------- | --- | ----- | ----------- | -------- | ---- | ---------- |
With the focus of this review article being on the topic, which left us with a final selection of 56 articles.
intersectionbetweenthenotionsofdeep representation We included 25 additional articles post-search directly
|              |      |     |                |         |         | to the | final selection. |     | They | were | detected | either in |
| ------------ | ---- | --- | -------------- | ------- | ------- | ------ | ---------------- | --- | ---- | ---- | -------- | --------- |
| learning and | BCI, | the | first step has | been to | collect |        |                  |     |      |      |          |           |
articles dealing with both topics simultaneously. reference sections of the 56 articles or were selected
Unfortunately, only few articles contain these exact based on our prior knowledge of the field. These
keywords in their title or abstract and too many additional articles also include non-BCI EEG studies
contain them in the main text body. Therefore, we which have applied techniques that can be interesting
|                  |     |              |           |     |     | to the BCI | community. |     | A   | flow diagram | summarizing |     |
| ---------------- | --- | ------------ | --------- | --- | --- | ---------- | ---------- | --- | --- | ------------ | ----------- | --- |
| had to establish | a   | finer search | strategy. |     |     |            |            |     |     |              |             |     |
This strategy consisted of first creating, for both the selection process is provided by Figure 1.
of the two notions, a list of terms that were either Among the resulting 56+25 articles, many use
|            |             |     |                  |     |        | similar | techniques, | in  | particular, | 34  | articles | employed |
| ---------- | ----------- | --- | ---------------- | --- | ------ | ------- | ----------- | --- | ----------- | --- | -------- | -------- |
| equivalent | or implying |     | it. For example, | the | notion |         |             |     |             |     |          |          |
of BCI can either be replaced by equivalents such as autoencoders to learn a representation. Because
brain-computer interface,andbrain-machine interface, of such redundant approaches we refrained from
or by specific paradigms that may imply a BCI, such discussing every single paper, but maintained all of
as motor imagery or event-related potential. Similarly, them in our literature list.
|                                       |     |     |     |             |     | While | reading | the | resulting | 81  | articles, | our focus |
| ------------------------------------- | --- | --- | --- | ----------- | --- | ----- | ------- | --- | --------- | --- | --------- | --------- |
| thenotionofdeeprepresentationlearning |     |     |     | caneitherbe |     |       |         |     |           |     |           |           |
replacedbyequivalentslikedeeplearning +embedding, was on three aspects:
orbytechniquesthatinherentlyobtainadeeplearning-
|                       |     |              |                  |     |       | (i) the  | motivation(s) |     | for learning | an  | embedding, |              |
| --------------------- | --- | ------------ | ---------------- | --- | ----- | -------- | ------------- | --- | ------------ | --- | ---------- | ------------ |
| based representation, |     | such         | as autoencoders. | We  | noted |          |               |     |              |     |            |              |
|                       |     |              |                  |     |       | (ii) the | algorithms    | and | approaches   |     | used       | for learning |
| the importance        |     | of accepting | many different   |     | terms |          |               |     |              |     |            |              |
the embedding,
| that describe | potential |     | deep learning | methods | which |     |     |     |     |     |     |     |
| ------------- | --------- | --- | ------------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
can learn an embedding. To compile this list of (iii) and the methods used for characterizing and
method terms, we used the review conducted by introspecting the obtained embeddings.
Roy and colleagues [99]. The query finally used in Our findings on these three aspects are respectively
searchengineswastheconjunction(AND)betweenthe
|     |     |     |     |     |     | reported | in Section |     | 3, Section | 4 and | Section | 5. The |
| --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | ---------- | ----- | ------- | ------ |
disjunction (OR) of all the terms of the BCI list and first aspect, the motivation authors had to learn an
| the disjunction                         | of  | all the | deep representation |          | learning |                  |     |     |         |           |              |           |
| --------------------------------------- | --- | ------- | ------------------- | -------- | -------- | ---------------- | --- | --- | ------- | --------- | ------------ | --------- |
|                                         |     |         |                     |          |          | embedding,       | was | not | always  | explicit. | We           | estimated |
| terms. Thisquerycontains65termsintotal. |     |         |                     | Notethat |          |                  |     |     |         |           |              |           |
|                                         |     |         |                     |          |          | their motivation |     | by  | reading | the       | Introduction | and       |
a term can eventually contain multiple words (such as Discussion sections and by identifying the problems
| deep learning). | AND, | OR  | and the parenthesis |     | are not |       |           |     |     |          |          |     |
| --------------- | ---- | --- | ------------------- | --- | ------- | ----- | --------- | --- | --- | -------- | -------- | --- |
|                 |      |     |                     |     |         | being | addressed | in  | the | article. | However, | we  |
considered terms. We restricted our search to articles refrained from interpreting why the authors used
published after 2014 because we did not expect any a particular method or made a specific design
| earlier relevant | work | involving | both deep | learning | and |         |     |        |     |                |     |            |
| ---------------- | ---- | --------- | --------- | -------- | --- | ------- | --- | ------ | --- | -------------- | --- | ---------- |
|                  |      |           |           |          |     | choice. | The | second | and | third aspects, |     | algorithms |
BCI.Finally,werestrictedoursearchtothetitlesonly and characterisation/introspection techniques, were

Review of Deep Representation Learning Techniques for BCI and Recommendations 4
|     |     |     | Google Scholar: |     |     | 43 PubMed |     |     |     |     | 25 added |     |     |
| --- | --- | --- | --------------- | --- | --- | --------- | --- | --- | --- | --- | -------- | --- | --- |
87 Web of Science results
|     |     |     | search impossible |     |     |     | results |     |     |     | post-search |     |     |
| --- | --- | --- | ----------------- | --- | --- | --- | ------- | --- | --- | --- | ----------- | --- | --- |
Duplicate removal
101 results overall
Title screening
25 titles
76 titles on-topic
off-topic
Availability check
5 not free
|     |     |     |     | 3 not english |     |     | 67 available |     |     |     |     |     |     |
| --- | --- | --- | --- | ------------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
1 not available
Abstract screening
|     |     |     | 11 abstracts |           |     |     |     | 81 abstracts |     |     |     |     |     |
| --- | --- | --- | ------------ | --------- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
|     |     |     |              | off-topic |     |     |     | on-topic     |     |     |     |     |     |
Figure 1. Flow diagram summarizing the process for selecting which articles from the initial search results to consider in this
review. Blueboxesindicatetheinitialavailablesourcesandnumberofarticles,redboxesindicatearticleswhichwerenotconsidered
forvariousreasons(seemaintext),andthegreenboxrepresentsthefinallyconsideredarticles.
usually clearer and less prone to interpretation. Their 3. Motivations to learn embeddings
| identification |     | was done |           | by respectively |     | reading | the |         |             |             |     |       |             |
| -------------- | --- | -------- | --------- | --------------- | --- | ------- | --- | ------- | ----------- | ----------- | --- | ----- | ----------- |
|                |     |          |           |                 |     |         |     | In this | section, we | will report | on  | which | motivations |
| Methods        | and | Results  | sections. |                 |     |         |     |         |             |             |     |       |             |
Becausethegoalofanyreview,includingthisone, were identified as leading to the use of a DL-based
is to provide an overview of the state-of-the-art for a embedding or to the use of a method that inherently
|          |        |            |     |         |            |     |             | learns one. | Please | note that | the | motivations | we list |
| -------- | ------ | ---------- | --- | ------- | ---------- | --- | ----------- | ----------- | ------ | --------- | --- | ----------- | ------- |
| research | topic, | the aspect |     | (ii) on | algorithms |     | is central. |             |        |           |     |             |         |
It allows researchers entering the field to choose from in the following are not exclusive and that the authors
|              |     |       |            |     |          |              |     | of a study | can have | multiple | motivations |     | for learning |
| ------------ | --- | ----- | ---------- | --- | -------- | ------------ | --- | ---------- | -------- | -------- | ----------- | --- | ------------ |
| the complete |     | panel | of methods |     | at their | disposition. |     |            |          |          |             |     |              |
However, to choose between the algorithms presented, an embedding. Many of the motivations listed in this
researchers need to understand which needs each of section are special cases of transfer learning, which
|                 |     |            |     |           |      |        |        | turned | out to be a motivation |     | in  | the large | majority of |
| --------------- | --- | ---------- | --- | --------- | ---- | ------ | ------ | ------ | ---------------------- | --- | --- | --------- | ----------- |
| these algorithm |     | addresses, |     | i.e., for | what | reason | should |        |                        |     |     |           |             |
one algorithm be preferred over another? Hence, the the articles we reviewed for learning an embedding. In
|        |        |              |     |           |     |      |         | the following | subsections, |     | we explain | why | embeddings |
| ------ | ------ | ------------ | --- | --------- | --- | ---- | ------- | ------------- | ------------ | --- | ---------- | --- | ---------- |
| aspect | (i) on | motivations. |     | Moreover, |     | this | section |               |              |     |            |     |            |
can also be used to help researchers entering the seem specifically suited for transfer learning in BCI.
| field identify |     | their | own | motivations |     | by  | reviewing |     |     |     |     |     |     |
| -------------- | --- | ----- | --- | ----------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
a list of potential ones. Finally, the aspect (iii) 3.1. Improve classification accuracy
| on introspection |               | techniques |         | is necessary  |          | because    | the        |                            |                    |               |                        |          |                |
| ---------------- | ------------- | ---------- | ------- | ------------- | -------- | ---------- | ---------- | -------------------------- | ------------------ | ------------- | ---------------------- | -------- | -------------- |
|                  |               |            |         |               |          |            |            | Undoubtedly,               | most               | articles      | share                  | the      | objective of   |
| algorithms       | presented     |            | in this | review        | are      | quite      | specific   |                            |                    |               |                        |          |                |
|                  |               |            |         |               |          |            |            | improving                  | the classification |               | accuracy               | over     | the state of   |
| and the          | introspection |            | methods | commonly      |          | used       | in BCI     |                            |                    |               |                        |          |                |
|                  |               |            |         |               |          |            |            | the art                    | in a particular    | scenario.     |                        | However, | in some        |
| to characterise  |               | classical  | machine |               | learning | algorithms |            |                            |                    |               |                        |          |                |
|                  |               |            |         |               |          |            |            | articles                   | the reference      | to embeddings |                        | is       | only motivated |
| may be           | of            | limited    | use     | only          | in this  | BCI        | context.   |                            |                    |               |                        |          |                |
|                  |               |            |         |               |          |            |            | bythatreason(e.g.[25,69]). |                    |               | Whilethisisalegitimate |          |                |
| Additionally,    |               | most       | of the  | introspection |          |            | techniques |                            |                    |               |                        |          |                |
motivationbyitself,itdoesnottellusmuchabouthow
| presented | simply | take | embedding |     | vectors |     | as input, |     |     |     |     |     |     |
| --------- | ------ | ---- | --------- | --- | ------- | --- | --------- | --- | --- | --- | --- | --- | --- |
theembeddingislearnedorwhyaparticularalgorithm
withoutmakingassumptionsaboutthealgorithmthat
|          |      |          |     |            |     |            |     | was used. | For this reason, |     | we will | not | elaborate more |
| -------- | ---- | -------- | --- | ---------- | --- | ---------- | --- | --------- | ---------------- | --- | ------- | --- | -------------- |
| had been | used | to learn | the | embedding. |     | Therefore, | we  |           |                  |     |         |     |                |
on this motivation.
| will see  | how          | certain    | introspection |           | methods  |            | commonly  |     |     |     |     |     |     |
| --------- | ------------ | ---------- | ------------- | --------- | -------- | ---------- | --------- | --- | --- | --- | --- | --- | --- |
| paired    | with certain |            | algorithms    | can       | actually |            | be paired |     |     |     |     |     |     |
| with many | other        | algorithms |               | described |          | in Section | 4.        |     |     |     |     |     |     |

Review of Deep Representation Learning Techniques for BCI and Recommendations 5
3.2. Learning to become robust to noise 3.4. Learning from small datasets
EEG is sensitive to many sources in addition to The ability to learn from as little as possible data
the signal of interest. These additional sources can while still reaching satisfactory classification scores is
be, for example, non-physiological noise picked up desirableinBCIsystemsfortwomainreasons: First,it
by the system, muscular artefacts or other non- allows for the quick start of BCI applications because
neural biosignals, or background brain activity. These only a small amount of calibration data needs to be
additional sources are considered, in many cases, not recorded. Second, BCI datasets are quite small in
| relevant | to the | BCI task | and | typically |     | they do not | general. |     |     |     |     |     |     |
| -------- | ------ | -------- | --- | --------- | --- | ----------- | -------- | --- | --- | --- | --- | --- | --- |
help the decoding, as they may fluctuate over time, Shortening calibration times can be addressed
showingnon-stationarydistributions. Weobservethat with two different types of algorithms: algorithms
the least restrictive experimental protocols tend to be able to exploit very well the few available examples
most affected by these undesired sources. Examples of the ongoing session [106, 110], or algorithms that
are dry or water-based EEG systems that are easier can take advantage of existing data recorded before
and faster to set up than gel-based ones, but are also the current session such that only little adaptation is
more prone to noise. Similarly, real-world conditions needed for the ongoing session [37, 57]. The former is
arelessconstrainedthanlabconditionswheresubjects generally not a strong point of deep learning models
are asked not to blink and to remain still during the but rather of classical machine learning models that
recordings. Here,theformerwillleadtomoreartefacts exploit expert knowledge, e.g., in the form of domain-
and non-stationarities in the signals. Therefore, it is specific regularization approaches [104, 105, 106, 110].
desirable to have systems which have learned to be The latter is better known as transfer learning, and
robust to these additional sources. using it is nearly always motivated by the reduction of
| We  | will | see two | methods | that | allow | learning | calibration | times. |     |     |     |     |     |
| --- | ---- | ------- | ------- | ---- | ----- | -------- | ----------- | ------ | --- | --- | --- | --- | --- |
robustness. The first one, for robustness to noise Tackling small datasets essentially involves the
specifically, is denoising autoencoders [17, 91] that same principle as shortening calibration times, hence
will be explained in Paragraph 4.2.2. The second it can also be done in two different ways: either by
method is through data augmentations [96] which will simplyexploitingwellthesmallexistingdatasetsorby
be explained in Paragraph 4.3.3. pre-training models on other types of datasets.
|     |     |     |     |     |     |     | Most | of  | the algorithms |     | we will mention |     | in this |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | -------------- | --- | --------------- | --- | ------- |
3.3. Learning invariances article allow for some form of transfer learning.
|     |     |     |     |     |     |     | However, | we  | will see | in  | Paragraph | 4.0.2 | that |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- | --- | --------- | ----- | ---- |
This motivation addresses experimental scenarios or unsupervised algorithms are particularly useful for
| protocols       | which   | record                              | brain       | signals  | under       | multiple  |               |      |               |       |              |         |           |
| --------------- | ------- | ----------------------------------- | ----------- | -------- | ----------- | --------- | ------------- | ---- | ------------- | ----- | ------------ | ------- | --------- |
|                 |         |                                     |             |          |             |           | this purpose  |      | as they       | allow | the use of   | non-BCI | EEG       |
| conditions.     | Typical | conditions                          |             | are      | the subject | id, the   |               |      |               |       |              |         |           |
|                 |         |                                     |             |          |             |           | datasets      | that | are much      | more  | abundant     | [78].   | The       |
| session         | number, | or the                              | source      | dataset. | Data        | collected |               |      |               |       |              |         |           |
|                 |         |                                     |             |          |             |           | unsupervised  |      | algorithms    | will  | be described | in      | detail in |
| over conditions |         | can be                              | expected    |          | to follow   | different |               |      |               |       |              |         |           |
|                 |         |                                     |             |          |             |           | Subsections   | 4.2, | 4.3, 4.4.1    | and   | 4.5.         |         |           |
| distributions.  |         | Theconditionsusuallyareorthogonalto |             |          |             |           |               |      |               |       |              |         |           |
| the main        | BCI     | classes,                            | i.e., there | can      | be examples | with      |               |      |               |       |              |         |           |
|                 |         |                                     |             |          |             |           | 3.5. Bridging |      | heterogeneous |       | components   |         |           |
| any combination |         | of condition                        |             | and BCI  | class.      | A model   |               |      |               |       |              |         |           |
is said to be invariant with respect to a condition if Raw data elements generally have intrinsic structures:
therepresentationitproducesdoesnotdependonthat An image has a width and a height, a text has a
condition. Learning domain-invariant representations certain number of words, and an EEG recording has
is a typical approach to transfer learning because it a duration, sampling rate and a specific spatial layout
allows using the same representation on multiple data ofrecordingchannels. Theseintrinsicstructuresdefine
distributions. The notion of invariance is close to that a relation of the features contained in an example: the
ofrobustnessdescribedinSubsection3.2. However,we pixelsofanimage,thewordsofatext,andthesamples
made a distinction between the two as in the case of of an EEG recording follow specific orders. Each data
robustness, we will systematically refer to factors that type requires specialized layers in DL architectures
are only obstacles to the decoding (such as noise and and/or pre-processing steps to capture their internal
artefacts), whereas in the case of invariance, we will structures. These layers and steps are necessary to
refer to contextual information for which a conscious transform the data elements into forms that allow
choice is made to maintain invariance. for better processing by the following classifiers (or
We will see in Paragraph 4.4.2 that invariant classification layers). As explained in the Introduction
representations can be learned through an adversarial (Section 1), these forms are called embeddings, i. e.,
objective [47] or by using deep metric learning [36], collections of features, where the eventual purpose of
see Subsection 4.5. each feature is automatically defined by the training

Review of Deep Representation Learning Techniques for BCI and Recommendations 6
algorithm. We observed in the literature that an want to enforce multiple objectives simultaneously,
embedding can be used as an algorithmic bridge in for example, to both optimize the performance
multiple ways: of the model on a BCI task and to obtain a
subject-independent representation as proposed by
3.5.1. Between different types of algorithms. Because Ozdenizci and colleagues [82], see Paragraph 4.4.2,
there is no a priori hypothesis about the features or to simultaneously enforce a supervised and an
of an embedding, virtually any classification or unsupervised objective for the purpose of mitigating
regression algorithm can use embedding features as theriskofoverfittingandenhancinggeneralization,see
input. Therefore, it is common to use an embedding Li and colleagues [62] and Subsection 4.3.
as a bridge between different types of decoding
algorithms [37, 124]. A typical scenario uses a deep 3.6. Uncover the structure of the data
learning model as feature extractor and a classical
Finally,self-supervisedlearning(SSL)algorithmsdiffer
machinelearningmodeltodecodethosefeatures. This
from the aforementioned approaches by not relying
configuration can be employed for transfer learning
on labelled data (see Subsection 4.3). Instead, they
scenarios.
learn representations in a data-driven manner. As a
result, the patterns that emerge when summarizing
3.5.2. Between different data types. Because the
datasets using visualization methods such as UMAP
purpose of each feature in an embedding is learned
(see Subsection 5.3) may reveal underlying structures
automaticallybythealgorithm, itispossibletodesign
in the data, rather than simply reflecting the
the learning task such that different data types can
prior assumptions of an experimenter. In this
be projected into a common embedding space. Even
direction, Banville and colleagues demonstrated that
if every data type requires a different processing
the representations learned through SSL contained
pipeline, they can all produce an embedding of the
structures that translated physiological and clinical
same dimensionality. Then, techniques exist to align
phenomena [9]. This finding highlights the potential
theembeddingspacesofdifferentdatatypesaccording
of SSL algorithms to uncover meaningful structures in
to their semantic similarity. This so-called joint
complex data.
embedding learning is commonly used to relate image
and text data into an embedding [52, 63], but first
4. Approaches used to obtain embeddings
publications have now shown, how joint embeddings
can be learned also for EEG and MRI data [28].
Here, we will try to draw an exhaustive list of all
the algorithms and methods that can be put into
3.5.3. Between different recording systems. Despite
place to meet the objectives described in Section 3.
existing norms for EEG electrode placement, there
We distinguish two types of algorithms which learn
are many different EEG systems available, all with
representations in either a supervised or unsupervised
particularities and slight variations. Additionally, not
way.
alldatasetsarerecordedusingthesamesetoreventhe
same number of channels. To address this obstacle,
4.0.1. Supervised methods. We say an algorithm is
recent studies have begun investigating architectures
supervised when it directly exploits examples with
that can receive recordings from multiple different
human-annotated labels. In BCI, such labels can for
channel sets as input [130, 35, 120, 126, 13], see
example be the type of mental imagery task being
Paragraph4.3.2. Thesearchitecturesshowpromisefor
executed, or the stimulus attended during an epoch,
transfer learning or for handling corrupt channels.
i.e., the BCI classes. In general, such examples
have to be recorded under controlled conditions
3.5.4. To enforce multiple objectives. Finally, the
where the participant has to execute a pre-scripted
embedding can enable the combination of multiple
task, as opposed to online/free BCI control. The
high-level objectives as in the following example:
representations learned in this way are typically only
During training (in opposition to joint embeddings)
tailoredforthetaskcorrespondingtothelabelsanddo
a single processing pipeline is employed to create
not generalize well.
the embedding layer. From this point on the
Not many of the reviewed articles learn a repre-
processing can be split into multiple branches, each
sentation in this supervised manner. Nevertheless, in
computing a specific objective. Finally, the global
Subsection 4.1, we described one very simple exam-
loss would be a weighted sum of these different
ple. In Subsection 4.5, we will see how metric learning
objectives. In this scenario, the embedding provides
can also be used to learn embeddings in a supervised
a high-level representation of the data which tends
way. Yet,supervisedlearningisoftenusedtofine-tune
to satisfy all the different objectives. One could

Review of Deep Representation Learning Techniques for BCI and Recommendations 7
pre-trained models. In such a case, the supervised al- 4.1. Hidden layer of a classification network
gorithm does not properly learn the embedding but
The simplest approach one can think of to obtain an
rather uses it and eventually improves it.
embedding is to train a feed-forward neural network
with at least one hidden layer on a classification task,
4.0.2. Unsupervisedmethods. Algorithmsimplement-
i.e., using a cross-entropy loss. Here each output
ingunsupervisedlearningdonotusehuman-annotated
node of the network will correspond to a specific class.
labels [49]. This bears the advantage of being able
Receiving a novel input example, the task of each
to be trained on any raw EEG signal, i.e., not nec-
output node is to predict the probability that the
essarily recorded under a BCI protocol, which is far
true class label is that of the node in question. To
more abundant than labelled recordings of BCI ses-
obtain as many outputs as there are classes, there
sions. It is generally the class of unsupervised algo-
is usually a fully connected layer that linearly maps
rithms that is employed to train so-called foundation
the latent representation from the last hidden layer to
models, i.e., general-purpose embeddings trained from
these outputs. This last latent representation can be
large amounts of data. In a typical scenario, an un-
consideredasanembedding,anditiscommontotreat
supervised algorithm pre-trains a neural network on
it as such [37], i.e., re-using that representation for
what is called a pretext task, and a supervised algo-
other purposes, analysing the information contained
rithm later on fine-tunes it, or part of it, on what is
in this latent representation, etc. This method has
calledadownstreamtask. InthecontextofBCI,down-
theadvantageofbeingextremelysimpletoimplement.
streamtaskscanbetheclassificationofanimaginedor
In addition, it is generally more computationally
executedmovement,ofattendedvs.ignoredstimuli,of
efficient than most unsupervised methods. However,
sleepstages, thedetectionofseizures, emotions, orthe
this simple method produces representations that are
regression of the level of mental workload, of the level
very targeted, which means they are typically not
ofdrowsiness,etc. Wewillseeinthefollowingsections
transferabletoothertasksandsometimesnottoother
some pretext tasks that can or could be used in BCI.
distributions as well.
The overall goal is typically to obtain a good
To obtain more flexible representations, it is
score on the downstream task, and the goal of the
commontousemultipleobjectivessimultaneously,i.e.,
pretext task is to provide a pre-trained network
multi-task learning. For example, one can enforce the
that can already extract information relevant to the
representationtobeinvarianttothesubjectinaddition
downstream task. If the pretext task manages to
to allowing the classification of mental imagery tasks.
learn information relevant to the downstream task,
We will see in detail how such domain-invariant
the workload of the latter is alleviated. This way,
representations can be learned in Paragraph 4.4.2.
the network might need fewer examples from the
Another approach consists of representations that
downstreamtasktobefine-tuned. Becausethepretext
allow the reconstruction of the original input. This
and downstream tasks are inevitably different to some
can be achieved by combining the classifier with an
extent, the data features that must be learned to
autoencoder [24], c.f. Subsection 4.2.
solve each of them are also different. This leads to
the question of how similar a particular pretext task
4.2. Autoencoder
is compared to actual BCI tasks (i.e., downstream
tasks), or slightly rephrased, whether a given pretext Autoencoders encompass relatively well-established
task is general enough to learn a representation that methods for unsupervised representation learning [8].
is sufficiently general to contain information that is In their canonical form, their architecture can be
relevant to (various) BCI classification tasks. decomposed into two parts: an encoder and a decoder.
Many different unsupervised algorithms exist, The encoder takes as input an example X and
each with its own way of relating to the notion of an returns a hidden representation z. The decoder
embedding. In Subsection 4.2, we will review articles takes as input the representation z and returns an
realizing autoencoder paradigms and variants of it as estimation of the original input Xˆ. The objective
pretext tasks. Then, in Subsection 4.3, we will look at is to minimize the difference between the estimated
the subfield of unsupervised learning that uses pseudo and the original inputs Xˆ and X. Typically, the
labels, called self-supervised learning (SSL). In Para- dimension of the hidden representation z is smaller
graph4.4.1,wewillseehowgenerativeadversarialnet- than that of the input X such that the network learns
work (GAN) can be used for unsupervised representa- to extract important features from the input data,
tion learning. Finally, in Subsection 4.5, we will show which are necessary to reconstruct the original input.
how metric learning techniques can be realized in un- Autoencoders are unsupervised and can virtually be
supervised manners. applied to any type of input. Over the years, a
significant amount of variants were developed. This

Review of Deep Representation Learning Techniques for BCI and Recommendations 8
is reflected in the 34 studies we have found using for seizure detection. They demonstrated that the
autoencoders. joint use of these two techniques resulted in better
performance than either approach used independently.
4.2.1. VAE. Variational autoencoders (VAEs) is a TheDAEcomponentwasshowntopreventoverfitting
variant in which the latent representation predicted and improve the robustness of the model to noise,
by the encoder is not directly fed to the decoder, but while the SAE allowed for the learning of higher-level
rather used as parameters for a random distribution, features in the EEG data.
typically an isotropic Gaussian. Then, a point
sampled from this distribution is given to the decoder 4.3. Self-Supervised Learning (SSL)
as input [8]. Modelling the problem in this way
Self-supervised learning (SSL) is a form of unsuper-
allows to gain control over the meaning of a latent
visedlearningthatusespseudolabels,orautomatically
representation, which would not be possible with
generated labels, to train a network [49]. Designing
a regular autoencoder. Additionally, depending
these pseudo labels is typically done by using known
on the distribution used, it can force the hidden
propertiesofthedata,e.g.,anexampleissimilartoit-
representation to have disentangled features [43].
self, a time sample comes before the next one, samples
These reasons might explain why VAEs have been
from different channels are correlated, etc. A pseudo
well adopted by the BCI community. For example,
label could be, for example, the chronological order of
Ozdenizci et al. used them in combination with
different time windows of a recording. The unsuper-
adversarial networks (c.f. Subsection 4.4) to learn
vised learning is guided by the necessity to create pre-
subject-invariant representations of motor imagery
text tasks which either are similar to the downstream
recordings [81].
tasksorsufficientlygeneraltolearnfeaturesthatwould
be relevant for them. SSL have been extremely suc-
4.2.2. DAE and MAE. Denoising autoencoders
cessful in the fields of computer vision [16, 10], speech
(DAEs)andmaskedautoencoders(MAEs)arevariants
processing [6] and NLP [23].
wheretheinputfortheencoderiscorrupted, eitherby
As the topic is fairly new, it is still relatively
adding noise or by masking parts of it. Nevertheless,
unknown within the BCI community. Out of the 13
the output of the decoder is still compared to the
studies we found using SSL with BCI data, 10 were
original unaltered input. This way, the network can
published after 2021.
learnhowtohandlenoisyorcorruptedinputexamples.
TheseareinterestingcharacteristicsforEEGdataand
4.3.1. SSL Tasks Using Temporal Structure. In their
explain why they are commonly used [19, 123, 91, 17].
early 2021 study, Banville et al. [9] compared three
differentSSLpretexttasksthatallexploitthetemporal
4.2.3. SAE. Sparse autoencoders (SAEs) differ from
structure of EEG recordings. The first task, relative
regular autoencoders in that they enforce sparsity
positioning, consists of predicting whether two time
in the hidden representation through an additional
windows were within a certain distance or further
loss term. Sparsity means that only a small
apart. The second task, temporal shuffling, requires to
number of dimensions of the representation are
determineifthreetimewindowsareinthecorrectorder
simultaneously non-zero. The sparsity is typically
ornot. Thelasttask,contrastivepredictivecoding,uses
enforced by adding a penalty term which enforces
a number of consecutive windows and distractors that
a minimal Kullback-Leibler (KL) divergence [59]
hadbeensampledelsewhere. Thefirsttwoconsecutive
between the average activation of each hidden unit
windowsconstitutethecontext. Thetaskistopredict,
and a sparsity hyperparameter. Liu et al. [70]
for each other window, whether it is following the
proposed a deep learning architecture for EEG-based
contextorisadistractor. Asimilarapproachwastaken
emotion recognition, which consists of a convolutional
by Ou and colleagues [80].
neural network (CNN) for feature extraction, followed
by a SAE and a multilayer perceptron (MLP)
4.3.2. Masking-based SSL. Also in 2021, Kostas et
classifier. Their approach involves training the
al. [58] published an SSL method called wav2vec that
CNN in a supervised manner, then discarding the
was originally developed for speech processing [6].
linear classification layer and training the SAE in an
Wav2vec shares similarities with masked autoencoders
unsupervised way using the CNN features. Finally,
(c.f. Paragraph 4.2.2), where temporal regions of the
the MLP is trained in a supervised way using the
signal are masked, but directly optimises the distance
SAEfeatures. Theirresultssupportthattheproposed
between embedding vectors instead of going back
approach outperforms other methods, including the
to the input space. This work sparked a number
CNN part alone. Qui et al. [91] proposed an
of studies, which also experimented with temporal
approachcombiningdenoisingandsparseautoencoders
masking strategies [42, 13, 21, 62, 30].

Review of Deep Representation Learning Techniques for BCI and Recommendations 9
Most masking-based SSL studies rely on trans- unexploredinBCIbutispartofthehot topics indeep
former architectures [117]. This is because the at- learning. The BCI community would probably gain
tention mechanism of transformers allows the network much from exploring SSL further.
by design to selectively focus on the unmasked por-
tions of the signal and predict the masked portions. 4.4. Adversarial network-based training
Yang and colleagues pioneered the use of transformers
Some learning objectives are complex, i.e., non-trivial
with independent encoding of the EEG channels [126].
to compute. In other words, they can not simply be
This novel approach enables the exploration of mask-
evaluated by non-parameterised loss functions such as
ing strategies over the channels that allow to pre-train
themeansquarederror,orthecross-entropyloss. Such
an attention mechanism over the channel structure.
complex objectives may, for example, maximize the
Such pre-trainings pave the way for the development
level of realism of a generated example [27], minimize
of pre-trained models that are independent of specific
the mutual information between two embeddings [47],
channel sets. Subsequent studies by Li et al. and
orminimizetheamountofdomain-specificinformation
Guetscheletal.furtherexpandedonthisconceptwith
presentinalatentrepresentation[81]. Toenforcesuch
a domain-inspired spatial masking strategy [62, 35].
complex objectives, it is possible to utilize auxiliary
neural networks. These auxiliary networks can deliver
4.3.3. Augmentation-based contrastive SSL. As a
richer feedback to the main networks than a non-
third pioneering article (2020), Mohsenvand and
parameterized loss functions. The specificity of the
colleagues experimented with SSL based on data
methodspresentedinthissectionisthattheirauxiliary
augmentations [75], and were followed by Yand and
networksalllearntomaximizetheirobjective,whereas
colleagues [127]. The general idea of such methods
their main networks are trained to minimize it. For
is to first sample two data augmentations from a
thisreason,theseauxiliarynetworksareactuallycalled
pre-defined family of plausible augmentations. In
adversarial networks. In mathematical terms, the
the image domain such augmentations could be a
objective function being optimized is the minimum
combination of cropping, rotation, colour shift and
over the possible main networks of the maximum over
addition of noise. Sampling an augmentation would
the possible adversary networks of the loss function.
then mean sampling a set of parameters for cropping,
rotating,shiftingthecoloursandaddingnoise. Second,
4.4.1. Generative adversarial networks. A specific
the two augmentations are applied to the examples of
case an adversarial network training can be found in
thebatch,resultingintwoaugmentedversionsofevery
generative adversarial networks (GANs), where the
example. Third, the augmented examples are passed
main network is called generator and the adversary
to a network to obtain embeddings. Finally, the loss
network is called discriminator. The generators are
functionenforcestheembeddingsofthetwoversionsof
optimised for generating realistic data from random
each example to be either similar (non-contrastive) or
noise vectors, and the discriminators are trained to
to share a higher similarity with each other than with
discriminate if the examples they receive as input
the representations of the other examples in the batch
are real or have been artificially created by the
(contrastive).
generators [34].
Plausibleandefficientaugmentationsaredifferent
In the image domain, Radford et al. emphasized
for each domain. Domain knowledge about EEG
that GANs can be used to learn representations in an
signals and neural processes can guide the design
unsupervised way [92]. Indeed, the discriminators can
of novel, plausible data augmentations for BCI. For
take as input any kind of data and are trained on a
example, a slight shift in the orientation of the source
relatively high-level task (depending on how good the
dipoles [140] or of their amplitude [14] are plausible
outputsofthegeneratorare),suchthatthereisagood
and can be used as data augmentation. However,
chance to find features relevant to other learning tasks
it is not established which augmentations would be
in their hidden representations. Furthermore, it has
the most efficient for self-supervised representation
been shown by Vondrick and colleagues that relevant
learningwithBCIdataandEEGprocessingingeneral.
featurescanbelearnedfromvideodatathisway[118].
Rommeletal.[97]revieweddataaugmentationswhich
However, GANs are known to be difficult to train
have already been tested on EEG data. The authors
(longandunstable)suchthattheiruseasunsupervised
underlinethatdifferentBCItasksrequiredifferentdata
feature extractors remains marginal in general.
augmentations. They also recognize that the list of
In the context of BCIs, we did not find any
augmentations that have already been introduced for
article using them for that purpose, but it could be
or tested on EEG signals is probably not exhaustive
worth investigating this further. However, there are
and new ones could still be discovered.
many successful examples of GANs being used to
Overall, the field of SSL remains relatively

Review of Deep Representation Learning Techniques for BCI and Recommendations 10
generate fake BCI examples in the context of data by simply considering that an example is similar to
augmentation [40, 32, 27]. itself. These cases will also be referred to as SSL (see
|     |     |     |     |     |     |     | Subsection | 4.3). |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | --- | --- | --- | --- | --- | --- |
4.4.2. Domain-invariant representations. A partic- A loss function commonly used for deep metric
ular use of adversarial networks is to learn domain- learning is the triplet loss [101]. The triplet loss takes
|           |                  |     |     |     |         |         | three examples |     | as input: |     | an anchor, |     | a positive | and |
| --------- | ---------------- | --- | --- | --- | ------- | ------- | -------------- | --- | --------- | --- | ---------- | --- | ---------- | --- |
| invariant | representations. |     | In  | the | context | of BCI, | the            |     |           |     |            |     |            |     |
domains are typically the subjects or the sessions, but a negative example. The anchor and the positive
|                 |         |               |     |             |     |              | examples | are expected |     | to be    | similar,    | while | the | anchor |
| --------------- | ------- | ------------- | --- | ----------- | --- | ------------ | -------- | ------------ | --- | -------- | ----------- | ----- | --- | ------ |
| they can        | also be | the recording |     | equipment,  |     | the dataset, |          |              |     |          |             |       |     |        |
|                 |         |               |     |             |     |              | and the  | negative     |     | ones are | dissimilar. |       | The | loss   |
| the stimulation |         | parameters,   |     | or factors. |     | A domain-    |          |              |     |          |             |       |     |        |
invariant representation is particularly interesting for minimizes the distance between the representations
|     |     |     |     |     |     |     | of anchor | and | positive | and | at  | the same | time | also |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------- | --- | --- | -------- | ---- | ---- |
cross-domaintransfer,e.g.,ifwehaveadecodingmodel
pre-trained on multiple subjects and want to apply it maximizes the distance between the representations
to a novel one. Transfer learning is one of the current of anchor and negative. Most of the loss functions
|            |        |        |     |     |     |     | used for | deep | metric | learning |     | are relatively |     | similar |
| ---------- | ------ | ------ | --- | --- | --- | --- | -------- | ---- | ------ | -------- | --- | -------------- | --- | ------- |
| challenges | of BCI | [121]. |     |     |     |     |          |      |        |          |     |                |     |         |
Toenforcerepresentationstobedomain-invariant, to the triplet loss or the contrastive loss [38] which
|         |           |     |                |     |          |     | does not | involve | negative |     | examples. | A   | particularity |     |
| ------- | --------- | --- | -------------- | --- | -------- | --- | -------- | ------- | -------- | --- | --------- | --- | ------------- | --- |
| a usual | objective |     | of adversarial |     | networks |     | is to    |         |          |     |           |     |               |     |
identify from which domain the input examples of deep metric learning techniques is, that even if
come. In this context, the auxiliary networks they can be supervised, they directly optimize the
|        |               |     |      |           |        |        | representations |     | or the | embedding |     | space. |     | In other |
| ------ | ------------- | --- | ---- | --------- | ------ | ------ | --------------- | --- | ------ | --------- | --- | ------ | --- | -------- |
| taking | the adversary |     | role | are often | called | domain |                 |     |        |           |     |        |     |          |
discriminators. The objective of the main network is words, thedatarepresentationsareobtainedexplicitly
|           |          |        |               |     |     |            | andnotmerelyasaside-product. |     |     |     |     | Deepmetriclearning |     |     |
| --------- | -------- | ------ | ------------- | --- | --- | ---------- | ---------------------------- | --- | --- | --- | --- | ------------------ | --- | --- |
| partly to | fool the | domain | discriminator |     |     | by leaving | no                           |     |     |     |     |                    |     |     |
domain-specificinformationintherepresentationsthey is frequently used in computer vision for tasks such
generate and partly to complete another task such as as face recognition [101] or place recognition [2]. In
|                |      |       |     |     |     |     | these tasks, | the | class | is the | identity | of  | the person | on  |
| -------------- | ---- | ----- | --- | --- | --- | --- | ------------ | --- | ----- | ------ | -------- | --- | ---------- | --- |
| classification | [31, | 102]. |     |     |     |     |              |     |       |        |          |     |            |     |
O¨zdenizci and colleagues implemented this for the picture or the place where the photo was taken.
|                     |     |     |       |         |         |         | These tasks | have | in  | common | that | they | usually | have |
| ------------------- | --- | --- | ----- | ------- | ------- | ------- | ----------- | ---- | --- | ------ | ---- | ---- | ------- | ---- |
| subject-independent |     |     | motor | imagery | feature | extrac- |             |      |     |        |      |      |         |      |
tion [81, 82]. Their adversarial network is trained to only a few examples per class but many different
discriminatethesubjectsandispairedwithaVAE(see classes. Additionally, they require models which can
|           |         |     |     |     |     |     | workonclassesthatwereunseenduringtraining. |     |     |     |     |     |     | This |
| --------- | ------- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | ---- |
| Paragraph | 4.2.1). |     |     |     |     |     |                                            |     |     |     |     |     |     |      |
Jeon and colleagues argued that using a domain last requirement makes it impossible to use regular
discriminatorcanintroduceproblemslikediscardclass- classifiers for these tasks.
Schneideretal.[100]usedavariationofthetriplet
| relevant | information, |     | also | referred | to  | as negative |     |     |     |     |     |     |     |     |
| -------- | ------------ | --- | ---- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
transfer [83]. They instead trained their adversarial loss and introduced a novel triplet sampling scheme
|         |             |     |            |             |     |         | for learning | embeddings |     | for | neural | data | jointly | with |
| ------- | ----------- | --- | ---------- | ----------- | --- | ------- | ------------ | ---------- | --- | --- | ------ | ---- | ------- | ---- |
| network | to estimate |     | the mutual | information |     | between |              |            |     |     |        |      |         |      |
class-relevant and class-irrelevant features [47]. Their behavioural data and/or time. Triplet sampling holds
main network’s objectives are to minimize the mutual an important role in metric learning [101]. While the
|             |         |     |     |                |     |     | authorstestedtheirframeworkonlyonanimaldata, |     |     |     |     |     |     | it  |
| ----------- | ------- | --- | --- | -------------- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| information | between |     | the | class-relevant |     | and | class-                                       |     |     |     |     |     |     |     |
irrelevant features and to classify motor imagery would be interesting to investigate its use on human
|          |       |                    |     |     |           |      | data and | eventually |     | for BCI. |     |     |     |     |
| -------- | ----- | ------------------ | --- | --- | --------- | ---- | -------- | ---------- | --- | -------- | --- | --- | --- | --- |
| examples | using | the class-relevant |     |     | features. | Note | that     |            |     |          |     |     |     |     |
Jeonetal. usedthetermadversariallearning whichto For BCI data, Guetschel et al. [36] developed
ourknowledgeisslightlyunconventionalinthiscontext a variation of the triplet loss that allows creating
|          |          |           |     |         |     |        | a hierarchical |     | structure |     | in the | embedding |     | space |
| -------- | -------- | --------- | --- | ------- | --- | ------ | -------------- | --- | --------- | --- | ------ | --------- | --- | ----- |
| while it | commonly | describes |     | attacks | on  | models | (i.e.,         |     |           |     |        |           |     |       |
reverse engineering, trying to fool the models, etc.). according to metadata associated with the recordings.
|     |     |     |     |     |     |     | In their | framework, |     | the | hierarchy |     | between | the |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | --- | --------- | --- | ------- | --- |
4.5. Deep metric learning different meta-labels is defined by the researcher
|     |     |     |     |     |     |     | using expert | knowledge. |     |     | The authors |     | demonstrated |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- | --- | ----------- | --- | ------------ | --- |
Deep metric learning is a sub-field of deep learning their framework by structuring the embedding space
| focussed | on  | training | neural | networks |     | to  | embed     |        |          |     |     |       |         |       |
| -------- | --- | -------- | ------ | -------- | --- | --- | --------- | ------ | -------- | --- | --- | ----- | ------- | ----- |
|          |     |          |        |          |     |     | according | to the | subjects |     | and | motor | imagery | class |
examples into vector spaces whose metrics implement labels,butthisapproachcouldtheoreticallybeapplied
| notions | of similarity |     | between | examples. |       | A typical   |            |           |           |     |     |           |          |     |
| ------- | ------------- | --- | ------- | --------- | ----- | ----------- | ---------- | --------- | --------- | --- | --- | --------- | -------- | --- |
|         |               |     |         |           |       |             | also to    | structure | according |     | to  | sessions, | datasets | or  |
| notion  | of similarity |     | would   | be        | class | membership: | paradigms. |           |           |     |     |           |          |     |
examples from the same class would be considered Studies exploiting metadata are at the border
moresimilar,i.e.,closetoeachotherintheembedding
|     |     |     |     |     |     |     | between | supervised | and | unsupervised |     | learning |     | as they |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | ------------ | --- | -------- | --- | ------- |
space, than examples from different classes. It is effectivelyuselabels,butthesemetadatalabelsusually
possible to define notions of similarity even without come ”for free”. On the other hand, contrastive losses
| human-annotated |     | labels | by  | using | pseudo | labels | or  |     |     |     |     |     |     |     |
| --------------- | --- | ------ | --- | ----- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |

Review of Deep Representation Learning Techniques for BCI and Recommendations 11
can also be used to simply separate the classes as an trainingstrategyandtheeventualfine-tuningstrategy
alternative to a classification task [89]. of the participants.
Lookingatthesuccessfulexamplesofdeepmetric
learning techniques for face recognition, which works 5.1.1. Intertwined evaluation. In general, the perfor-
even for subjects outside the training set, we might mance score on a downstream task provides an inter-
wonder if this concept is not under-exploited for BCI twined evaluation of both the embedding method and
data. Indeed, we typically restrict ourselves to only a the fine-tuning method. Yet, the methods involved in
few classes in BCI, but the use of deep metric learning both are independent and thus should be evaluated
techniques could potentially deeply transform the BCI separately. This separation is already common in the
domain by, for example, allowing to learn from 24/7 imagedomain[10,22]. Toonlytesttheinitialtraining,
multimodal recordings with both EEG and video for i.e., compare different pretext tasks, the typical ap-
action recognition. proach is to always use the same fine-tuning strategy.
A first fine-tuning strategy is to continue the training
5. Characterizing embeddings of the whole network for a fixed number of epochs but
on the downstream task and with examples from the
In most studies, the introspection effort invested target distribution [58]. This strategy can be compu-
to characterize the learned representation is shallow tationally heavy and may easily overfit depending on
and limited to simple score comparisons with a few the amount of fine-tuning data. A second fine-tuning
baselines. This limited approach can often miss strategy also commonly used in representation learn-
important details about the learned representations. ing is to train a linear classifier on top of the frozen
Fortunately, more elaborate techniques exist for representations [49, 10]. This strategy produces re-
introspectingDL-basedembeddings,whichcanprovide producible results, and its simplicity favours methods
valuable insights into the learned representations. able to extract representations which are easy to clas-
In this section, we will stress the importance of sify according to the downstream tasks. It thus may
having common benchmarks with commonly agreed- notobtainthebestclassificationscores, butthisisnot
on fine-tuning procedures to reliably compare a novel crucialforbenchmarkingpurposes. Unfortunately,itis
technique for obtaining an embedding with other notalwayspossibletousethisso-calledlinearprobing,
existingtechniques. Wewillalsoexplainhowthescore depending on the SSL strategy used [35].
on the pretext task can be used to better understand
an embedding. Finally, we will see projection methods
5.1.2. Multiple downstream tasks. Furthermore, a
for visualizing embeddings in lower dimensions, where
singledownstreamtaskisinsufficientfortheevaluation
it can be easier for humans to obtain insights.
ofmodelsthatclaimacertaingeneralizationcharacter-
istic, e.g., a EEG representation learned by unsuper-
5.1. Score on downstream task vised methods which shall be used for different BCI
protocols as well as sleep staging, emotion recognition
While the performance an embedding enables for
etc. Instead, benchmarks containing sets of tasks are
various tasks is a very high-level characteristic, it
required, comparable to the benchmarks used in the
nevertheless is important. For testing how well an
imageorlanguagedomain. ForNLP,theGLUEbench-
embedding will perform in transfer learning scenarios
mark [119] evaluates models on a range of natural lan-
or to compare pretext tasks, specific benchmarks
guage understanding tasks, while the SQuAD bench-
are required. The MOABB library [3] allows for
mark [93] evaluates models on question-answering
rigorous benchmarking models on between-sessions
tasks. In computer vision, commonly used classifica-
and between-subject transfer scenarios with motor
tion benchmarks are ImageNet [22], Places205 [139],
imagery, event-related potential (ERP), c-VEP and
VOC07 [26], and iNat18 [115]; and for object detec-
SSVEP datasets [18]. However, these evaluations
tionorsegmentation,VOC07+12[26],andCOCO[67]
are not meant to allow fine-tuning the models on
are often used. The development of these benchmarks
the target distribution. This fine-tuning aspect was
has played a crucial role in advancing the field of NLP
addressed in the 2021 BEETL competition [121]. In
and computer vision.
thiscompetition, theparticipantshadtosolveacross-
Similar benchmarks are needed for BCI to
datasets transfer task for motor imagery BCI data.
evaluate general-purpose embeddings. In particular,
They received a few labelled examples also from the
such a benchmark would need to include all types
finaltestdataset,whichmakesthiscompetitionsimilar
of BCI tasks and should reflect a diversity of user
to a transfer-learning-with-fine-tuning task. However,
groups, noise conditions, number and placements of
the participants of the BEETL competition were
recording channels, recording qualities, number of
allowed to use the data as they wished. Therefore,
calibrationexamplesandcontaminationwithartefacts.
the challenge was simultaneously testing the initial

Review of Deep Representation Learning Techniques for BCI and Recommendations 12
Aspects like the number of calibration examples, the that the learned embeddings had good generalization
number of channels, and the presence of noise or abilities. Overall, while pretext task scores should
artefacts, can be simulated by applying corruptions not be used to compare different pre-training methods
or ablations to datasets. Such transformations are together, they are useful for introspection during the
already used in studies for testing the robustness of development of a given pre-training method.
models[77,37,19,126]. Unfortunately,theapproaches
are not consistent over publications, which makes 5.3. Introspection by lower-dimensional visualizations
comparison between studies difficult. Normalizing of the embedding vectors
these corruptions or ablations could be an option for
Embedding vectors typically have a few hundred
establishing a standardized benchmark, allowing for
dimensions. Therefore, these vectors can not directly
more consistent and comparable evaluations across
be visualised. Thus it is common to first project
studies.
embedding vectors into a two-dimensional space.
Then,alltheexamplesofthedatasetcanbevisualized
5.1.3. Community adoption. Finally, a good bench-
simultaneously as a 2D scatter plot, each point
mark is one adopted by the community. If each article
representing a different example. This type of plot
reports its results on a new benchmark, the authors
allows to obtain insights about the distribution of the
should also provide baseline performances. The high
data in the original embedding space. Additionally, it
demands on computing resources in deep learning lim-
iscommontocolourtheexamplesaccordingtoalabel,
itsthenumberofbaselinesanewapproachcanbecom-
typically the label corresponding to a downstream
pared against. Additionally, there is always a concern
task [9, 36, 37, 54, 47], but we sometimes encounter
that authors applying a method as a baseline may not
colourings corresponding to the age, gender, date,
beusingittoitsfullestpotential,whetherintentionally
presence of a pathology [9], continuous behavioural
ornot. Forinstance, abaselinemethodmaybepoorly
labels [100], the subject id [36] or other meta-data. A
optimized or implemented, leading to sub-optimal re-
colouring can be applied to investigate how difficult
sults.
it will probably be to separate the learned features
In summary, the BCI community requires bench-
according to the label. The examples can also
marks that can evaluate general-purpose embeddings
be coloured according to whether they belong to
across a full range of tasks, have a deterministic fine-
the train or the test set. A comparison of the
tuning procedure, and are widely adopted by the com-
two distributions would allow inspecting potential
munity for systematic model testing.
non-stationarities between the two sets, which may
impact the generalization abilities of the model.
5.2. Score on pretext task
Such comparison is particularly beneficial for transfer
Obtaining a score evaluating the performance of a learningscenarios. Anexampleofsuchaprojectedplot
network on a pretext task is straightforward, as can be found in Figure 2.
each task comes with its own intrinsic metric. It Naturally, some information is lost in the
can simply be the value of the loss function or projection. Thus the different projection methods
an accuracy score for tasks involving classification. are required to intrinsically make assumptions about
However, these scores are not ideal for comparing the type of information that is important and should
different pretext tasks with each other because be preserved. The following paragraphs describe the
they are heterogeneous. Nonetheless, scores on most commonly used methods for embedding vector
pretext tasks should not be disregarded, as they still projections.
provide important information which can complement
downstream task scores. In particular, they can 5.3.1. PCA.A well-established technique that
help with introspecting the embeddings learned by linearly projects data into a new coordinate system
the model and their generalization abilities. For is principal component analysis (PCA) [111]. The
example, in Banville et al. [9], plotting pretext and coordinates of the new system are arranged in
downstreamtaskperformancessimultaneouslyallowed decreasing order of the variance, which the original
for a comparison of task difficulty and downstream data displays in each novel coordinate. To reduce
benefits. Kostas et al. [58] used the score on the the dimensionality of the embeddings, one typically
pretexttasktoevaluateitsdifficultywithrespecttoits choses the first two dimensions of this new coordinate
main hyperparameter. This relation between difficulty system. Therefore, we see that PCA gives importance
andhyperparameterallowedthemtospeculateonhow to the variance of the data: only the directions with
the network was solving the task. Additionally, the the highest variance between the embedding vectors
low variability of the score on the pretext task across will be represented in the projection.
subjects, hardware, and tasks, allowed them to claim

Review of Deep Representation Learning Techniques for BCI and Recommendations 13
Becausetheprojectionislinear,theaspectsofthe subject = 1 subject = 4
originalhigh-dimensionalembeddingspacerepresented
| by it are  | faithful.   | However, |            | variance |               | as a measure | of         |     |     |     |     |     |     |     |
| ---------- | ----------- | -------- | ---------- | -------- | ------------- | ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
| importance | for         | the      | dimensions | may      | not           | be           | a relevant |     |     |     |     |     |     |     |
| criterion  | to describe |          | the        | data.    | Nevertheless, |              | PCA is     |     |     |     |     |     |     |     |
theleastcomputationallyexpensiveoneforvisualising
embeddingsoutofthethreemethodsidentifiedbythis
review [39].
| 5.3.2.                                         | t-SNE.     | The           | t-distributed |             | stochastic          |              | neighbor |     | subject = 8 |     |     |     |     |     |
| ---------------------------------------------- | ---------- | ------------- | ------------- | ----------- | ------------------- | ------------ | -------- | --- | ----------- | --- | --- | --- | --- | --- |
| embedding                                      | (t-SNE)    |               | [114,         | 44] is also | a well-established, |              |          |     |             |     |     |     |     |     |
| butnon-linearmethodfordimensionalityreduction. |            |               |               |             |                     |              | It       |     |             |     |     |     |     |     |
| first models                                   |            | the embedding |               | vectors     | as                  | a graph      | where    |     |             |     |     |     |     |     |
| each node                                      | is         | one vector    | and           | where       | edges               | represent    |          | a   |             |     |     |     |     |     |
| pairwise                                       | similarity | between       |               | vectors,    | i.e.,               | a normalized |          |     |             |     |     |     |     |     |
| version                                        | of their   | Euclidean     |               | distance.   | Then,               | it           | builds   | a   |             |     |     |     |     |     |
| low-dimensional                                |            | projection    |               | of each     | embedding           |              | vector   |     |             |     |     |     |     |     |
| along with                                     | a          | graph         | following     | similar     | principles          |              | as the   |     |             |     |     |     |     |     |
| original                                       | graph.     | The           | projections   |             | are                 | optimized    | such     |     |             |     |     |     |     |     |
thattheKullback-Leiblerdivergencesbetweentheedge Figure 2. Example of UMAP-projected visualisation of
|                |          |                 |             |       |        |             |           | embeddings.                      |               | Figure description. |         | In this                 | figure, | each point   |
| -------------- | -------- | --------------- | ----------- | ----- | ------ | ----------- | --------- | -------------------------------- | ------------- | ------------------- | ------- | ----------------------- | ------- | ------------ |
| weights        | of their | graph           | and         | those | of the | original    | graph     |                                  |               |                     |         |                         |         |              |
|                |          |                 |             |       |        |             |           | correspondstooneembeddingvector. |               |                     |         | Itscolordenotestheclass |         |              |
| are minimized, |          | i.e.,           | it enforces | the   | graphs | in          | both, the |                                  |               |                     |         |                         |         |              |
|                |          |                 |             |       |        |             |           | labels.                          | The sub-plots |                     | depict  | embedding               | vectors | obtained for |
| high- and      | the      | low-dimensional |             | space | to     | be similar. |           |                                  |               |                     |         |                         |         |              |
|                |          |                 |             |       |        |             |           | different                        | subjects,     | but all             | vectors | were generated          |         | by the same  |
Thisprocedurepreserveslocalstructures: embed- embeddingfunction. Thesub-plotoftestsubject1ismarkedby
ding vectors which are close to each other will also aredframe. Thetopographicisolinesinthebackgroundindicate
thefourclassdistributionsasderivedfromthecompletedataof
| be close | to each | other          | after | the | projection.     |     | However, |              |                                             |           |     |           |          |            |
| -------- | ------- | -------------- | ----- | --- | --------------- | --- | -------- | ------------ | ------------------------------------------- | --------- | --- | --------- | -------- | ---------- |
|          |         |                |       |     |                 |     |          | allsubjects. | Theplotsofonlythreesubjectsaredisplayedhere |           |     |           |          |            |
| with the | random  | initialisation |       | of  | the projections |     | orig-    |              |                                             |           |     |           |          |            |
|          |         |                |       |     |                 |     |          | for space    | reasons.                                    | Comments. |     | This plot | was used | to realize |
inally proposed, t-SNE does not allow to preserve the that overall, the features learned were relevant for the targeted
|                      |     |        |                              |       |        |     |            | classification |             | task, even      | for the        | test subject. | Additionally, | it            |
| -------------------- | --- | ------ | ---------------------------- | ----- | ------ | --- | ---------- | -------------- | ----------- | --------------- | -------------- | ------------- | ------------- | ------------- |
| globalstructure[56]. |     |        | Thusthedistancesbetweeneven- |       |        |     |            |                |             |                 |                |               |               |               |
|                      |     |        |                              |       |        |     |            | indicated      | a hierarchy | in              | the difficulty | to separate   |               | the different |
| tual clusters        |     | in the | projected                    | space | should |     | not be in- |                |             |                 |                |               |               |               |
|                      |     |        |                              |       |        |     |            | pairs of       | classes.    | The topographic |                | isolines      | in the        | background    |
terpreted.
servedasavisualreferencetocomparesub-plotsandallowedto
Finally, in current implementations, t-SNE is observe distribution shifts between the embeddings of different
significantly more computationally expensive than subjects. Source: Guetscheletal.2022[37].
O(n2)
| PCA. It | has | a complexity |     | of  | with | n the | number |     |     |     |     |     |     |     |
| ------- | --- | ------------ | --- | --- | ---- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
ofembeddingvectorsandassumingthatk,thenumber
|              |     |            |     |       |        |        |     | basedt-SNE(t-SNE)[68], |                                         |            |     | seemcomparabletoUMAP |      |            |
| ------------ | --- | ---------- | --- | ----- | ------ | ------ | --- | ---------------------- | --------------------------------------- | ---------- | --- | -------------------- | ---- | ---------- |
| of projected |     | dimension, | is  | small | (k ≤3) | [114]. |     |                        |                                         |            |     |                      |      |            |
|              |     |            |     |       |        |        |     | in terms               | of                                      | speed when |     | projecting           | data | into 2D or |
|              |     |            |     |       |        |        |     | 3D[55].                | Still,UMAPcaneffortlesslyscaleupwiththe |            |     |                      |      |            |
5.3.3. UMAP. Uniform manifold qpproximation and projection dimension k whereas t-SNE’s complexity
projection (UMAP) [73] is the most recent of the grows exponentially with k [73]. Increasing k is
| three methods |     | presented |     | here. | It is | very | similar to |              |     |                   |     |          |     |           |
| ------------- | --- | --------- | --- | ----- | ----- | ---- | ---------- | ------------ | --- | ----------------- | --- | -------- | --- | --------- |
|               |     |           |     |       |       |      |            | not relevant |     | for visualisation |     | purposes | but | can be if |
t-SNE, but it has been formulated using stronger we want to use these algorithms for dimensionality
| mathematical |     | principles | to   | guide      | its design | choices.    | In     |            |     |          |        |          |     |            |
| ------------ | --- | ---------- | ---- | ---------- | ---------- | ----------- | ------ | ---------- | --- | -------- | ------ | -------- | --- | ---------- |
|              |     |            |      |            |            |             |        | reduction, | for | example, | before | applying | a   | clustering |
| particular,  | it  | is better  | than | the        | original   | formulation |        | approach.  |     |          |        |          |     |            |
| of t-SNE     | at  | preserving |      | the global | structure  |             | of the |            |     |          |        |          |     |            |
originalembeddingspaceasdiscussedbyOskolkov[79]
|         |        |                |     |     |     |        |           | 5.4. Visual |     | qualitative | evaluation |     |     |     |
| ------- | ------ | -------------- | --- | --- | --- | ------ | --------- | ----------- | --- | ----------- | ---------- | --- | --- | --- |
| because | of its | initialisation |     | and | the | choice | of cross- |             |     |             |            |     |     |     |
entropy for the loss function. Also, it is less A visual qualitative evaluation of embeddings can
|                 |     |           |     |      |     |          |       | be achieved |     | using conditioned |     | generation |     | techniques. |
| --------------- | --- | --------- | --- | ---- | --- | -------- | ----- | ----------- | --- | ----------------- | --- | ---------- | --- | ----------- |
| computationally |     | expensive |     | than | the | original | t-SNE |             |     |                   |     |            |     |             |
while still being significantly more expensive than These techniques involve a neural network, typically
PCA [72]. Its complexity is O(n1.14) [73]. However, called generator, whose objective is to generate
|        |          |       |      |      |       |     |          | artificial | examples |     | (i.e., | EEG epochs) | that | are as |
| ------ | -------- | ----- | ---- | ---- | ----- | --- | -------- | ---------- | -------- | --- | ------ | ----------- | ---- | ------ |
| It was | recently | shown | [56] | that | t-SNE | can | preserve |            |          |     |        |             |      |        |
the global structure as well as UMAP if its random similar as possible to real examples. In this context,
initialisation is replaced with a PCA initialisation. the only information the generator receives about a
Also, recent optimized versions of t-SNE, such as fast target (real) example that is to be imitated, is an
Fourier transform (FFT)-accelerated interpolation- embedding vector that represents it. For this reason,

Review of Deep Representation Learning Techniques for BCI and Recommendations 14
wesaythatthegenerationprocessisconditioned byan studies that simply use the hidden layer of a classifier
embeddingvector. Assumingthegeneratorisproperly as embedding, the remaining methods were only
trained, the similarity between the artificial and the observed sporadically. This shows how little the field
real examples is limited by the information contained of deep representation learning has been explored in
in the embedding vectors which act as a bottleneck. BCI by now. Regardless, we close this paragraph
If a example is perfectly represented in its embedding by reminding the reader that we did not conduct
vector (i.e., without information loss), then a well- a systematic review so these percentages might not
trainedgeneratorwillbeabletoreconstructitexactly. reflect the real distribution of the current research on
Ifsomeinformationislostbytheembedding,however, deep representation learning for BCI; they should be
thenthegeneratorcanonly”guess”theoriginalinput. taken with a grain of salt.
Visuallycomparinganartificialexampleanditstarget In addition to these findings, we make three
is a way to evaluate which information was lost and primary observations: firstly, in very few studies
whichwasmaintainedinthecorrespondingembedding. the authors were using representations in a transfer
Views of these examples can also be visualised in the learning scenario. Yet, there is great potential:
formofspatialpatterns[64]offrequencyspectra[132]. deep learning models shine in BCI transfer learning
Autoencoders (c.f. Subsection 4.2) intrinsically scenarios [121]. Moreover, re-using a pre-trained
train a generator and allow for this type of analysis representation can completely erase (in the case of
without additional effort [64, 132]. However, this is linear probing [37]) or at least alleviate (in the case
not the case for other embedding methods. Border of fine-tuning [58]) the cost of using deep learning
et al. proposed to use diffusion models as generators techniques, which qualifies them for online BCI
and investigated this introspection method with applications. Secondly, when it comes to cross-dataset
images [12]. However, this has not been explored transfer learning, the authors of the reviewed articles
yet, to our knowledge, with EEG embeddings and all applied their own procedures for pre-training, fine-
there have only been a few studies experimenting with tuning and evaluating of models. This makes the
diffusion models and EEG signals [113, 4, 53]. comparison of methods difficult. To compare pre-
|     |     |     |     |     |     |     | training | methods, | the | twoother | steps | (fine-tuningand |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | -------- | ----- | --------------- | --- | --- |
6. Discussion and Recommendations evaluating) should be fixed and standardised. To
|                 |     |           |     |          |              |     | our knowledge |     | there         | currently | is       | only   | one standard |     |
| --------------- | --- | --------- | --- | -------- | ------------ | --- | ------------- | --- | ------------- | --------- | -------- | ------ | ------------ | --- |
|                 |     |           |     |          |              |     | benchmark     | for | cross-dataset |           | transfer | in BCI | [121]        | but |
| In the previous |     | sections, | we  | reported | as factually | as  |               |     |               |           |          |        |              |     |
possible our findings on the methods that can or it still leaves room for improvement as discussed in
could be used to learn embeddings for BCI, along Subsection 5.1. Finally, the authors often learned an
|              |     |     |     |            |     |        | embedding | as  | a side product |     | of the | method | they | use |
| ------------ | --- | --- | --- | ---------- | --- | ------ | --------- | --- | -------------- | --- | ------ | ------ | ---- | --- |
| with reasons | for | why | one | would want | to  | do so, |           |     |                |     |        |        |      |     |
and the methods available to introspect them. We ratherthanasanexplicitobjective. Inmostcases,they
will now synthesise those findings and extract the ignoretheobtainedembeddingandcontinuewiththeir
main outcomes and discuss them. We will close primary task despite the large panel of introspection
with recommendations for future research on deep techniques available, as delineated in Section 5.
|                |          |     |         |          |     |     | In  | light | of these | observations, |     | we  | proceed | to  |
| -------------- | -------- | --- | ------- | -------- | --- | --- | --- | ----- | -------- | ------------- | --- | --- | ------- | --- |
| representation | learning |     | for BCI | and EEG. |     |     |     |       |          |               |     |     |         |     |
Concerning the methods employed to learn sketch recommendations regarding the future of deep
embeddingsbythearticlesweanalysed, wefoundthat representation learning for EEG data. The first
a large majority were autoencoder-based, accounting recommendation is, when an embedding has been
for approximately half of the articles surveyed. This learned, to introspect this representation. Authors
|             |     |     |            |     |          |       | can choose | from | a number |     | of existing |     | techniques, |     |
| ----------- | --- | --- | ---------- | --- | -------- | ----- | ---------- | ---- | -------- | --- | ----------- | --- | ----------- | --- |
| observation | was | not | surprising | as  | they are | based |            |      |          |     |             |     |             |     |
on a quite straightforward principle which has been as explained in Section 5, that can all provide
in existence for a long time and as many variants valuableinsightsaboutwhathasactuallybeenlearned.
have been developed [8] even if we could reported Moreover, this additional introspection step requires
on three only in our study. Furthermore, we relatively little computational effort compared to the
|         |             |        |     |          |              |     | initial one | for | learning | the embedding. |     |     |     |     |
| ------- | ----------- | ------ | --- | -------- | ------------ | --- | ----------- | --- | -------- | -------------- | --- | --- | --- | --- |
| found a | significant | number |     | of GANs, | representing |     |             |     |          |                |     |     |     |     |
approximatelyafourthofthesurveyedarticles. Again, The second recommendation focuses on founda-
this result was expected as GANs used to be the tionmodels. Wecallfoundation model anarchitecture
state-of-the-artofgenerativemodels,beforethearrival which has been pre-trained on large amounts of data.
of diffusion models, and have been abundantly used Such models can typically produce general representa-
|         |             |          |     |      |        |          | tions of | their | input data. | Foundation |     | models | serve | as  |
| ------- | ----------- | -------- | --- | ---- | ------ | -------- | -------- | ----- | ----------- | ---------- | --- | ------ | ----- | --- |
| for EEG | generation. | However, |     | none | of the | surveyed |          |       |             |            |     |        |       |     |
articles employed GANs for the purpose of EEG starting points or as building blocks for fine-tuning on
representation learning, leaving this area open for downstream tasks. We believe that the development
|                        |     |     |          |       |       |           | of EEG-specific |     | foundation | models |     | would | offer a | great |
| ---------------------- | --- | --- | -------- | ----- | ----- | --------- | --------------- | --- | ---------- | ------ | --- | ----- | ------- | ----- |
| further investigation. |     |     | Finally, | if we | leave | aside the |                 |     |            |        |     |       |         |       |

Review of Deep Representation Learning Techniques for BCI and Recommendations 15
benefitfortheBCIcommunity. Inthecomputervision encouraged, if reviewers regularly require comparisons
domain, foundation models are typically trained using with baseline approaches.
SSL techniques [7] so this seems to be a promising av- The conceptualization and successful training
enue for BCI, too. Although the idea of developing of foundation models for EEG data processing,
foundation models for BCI or EEG has started to be potentially facilitated by novel benchmarks and
discussed [21], there currently is no such model that datasets, could revolutionize the field of BCI. In
has been widely adopted by the BCI community. particular, it would reduce the amount of data needed
Our third recommendation is about the eventual to train BCI decoding models, implying reduced
creation of novel EEG datasets for the training of calibration times for novel sessions or subjects and a
foundation models. Experience from the language facilitation of rapidly explorating novel experimental
processing and the computer vision fields has shown paradigms and user tasks. This efficiency could
that foundation models require extremely large, but accelerate research cycles, potentially catalyzing the
not necessarily labelled datasets to be trained [23, 1]. emergence of a new generation of BCI paradigms.
WeassumethiswillprobablybethecasealsoforEEG For novel application fields of BCI such as invasive
foundation models. In non-EEG domains, those large neurotechnological applications, where the small
datasets were coming from very diverse sources, which sample problems may be even more severe, this
would probably translate for EEG foundation models efficiency may even be decisive. Furthermore, the
into many different EEG recording systems, subjects generalizedEEGrepresentationswewouldobtainfrom
and recording conditions. The Temple University futurefoundationmodelscouldfacilitatethealignment
Hospital EEG data corpus [78] might be such a of brain signals with other data modalities, such
resource and has already been explored by Kostas et as subject videos or medical records. Such cross-
al.[58]totrainaSSLmodel,butwestilllackhindsight modal embedding alignments would open the door
on whether this corpus is a good dataset for training for a broader scope of predictive tasks, extending
foundation models. beyond traditional imagery- and evoked potential-
Our final recommendation is about the eventual based paradigms to directly forecast attributes or
creation of novel benchmarks for evaluating SSL states represented in other domains.
methods and foundation models for BCI. To go In summary, the advent of EEG foundation mod-
beyond the BEETL benchmark [121], we first need els could mark a paradigm shift, with implications
to establish a set of fixed fine-tuning procedures to rangingfromstreamlinedmodeltrainingandenhanced
focus on a comparison between pre-trained models cross-modalapplicabilitytotheeradicationofcumber-
and not the combinations of pre-trained models and some calibration procedures. Therefore, a focus on es-
fine-tuning procedures. The choice of such fixed fine- tablishing such models should be considered a priority
tuning procedures should be relatively deterministic withintheEEGandBCIresearchcommunitiesandfor
| and realistic |         | for BCI     | usage.  | Two   | simple  | fine-tuning | funding | decisions. |     |     |
| ------------- | ------- | ----------- | ------- | ----- | ------- | ----------- | ------- | ---------- | --- | --- |
| procedures    | could   | for         | example | be    | linear  | probing     | [37]    |            |     |     |
| and whole     | network | fine-tuning |         | [58]. | Second, | this        | new     |            |     |     |
7. Acknowledgements
benchmarkwouldneedalargediversityofdownstream
tasks. As the main purpose of foundation models This work is in part supported by the Donders Center
is to be re-used, they also need to be tested and for Cognition (DCC) and is part of the project Dutch
compared on as many re-usage scenarios as possible. Brain Interface Initiative (DBI2) with project number
For BCI, this would translate into including datasets 024.005.022oftheresearchprogramGravitationwhich
| from as        | many           | BCI          | paradigms,  | recording    |               | scenarios  |             |          |              |                  |
| -------------- | -------------- | ------------ | ----------- | ------------ | ------------- | ---------- | ----------- | -------- | ------------ | ---------------- |
|                |                |              |             |              |               |            | is (partly) | financed | by the Dutch | Research Council |
| and user       | groups         | as           | possible.   | We           | can           | even       | go a (NWO). |          |              |                  |
| step further   | and            | mention      | that        | novel        | datasets      | could      | be          |          |              |                  |
| recorded       | explicitly     | for          | this        | benchmark.   |               | As the     | goal        |          |              |                  |
| of using       | a foundation   |              | model       | is to        | reduce        | the amount |             |          |              |                  |
| of calibration |                | data needed, |             | those novel  | datasets      |            | could       |          |              |                  |
| probably       | contain        | less         | repetitions |              | per condition |            | but         |          |              |                  |
| instead        | represent      | more         | and         | diverse      | conditions.   |            | Third,      |          |              |                  |
| and finally,   | a              | benchmark    | is          | useful       | if it is      | adopted    | and         |          |              |                  |
| used by        | the community. |              | For         | this reason, |               | the needs  | of          |          |              |                  |
| the BCI        | community      |              | must        | be kept      | in mind.      | Also,      | it          |          |              |                  |
| might be       | relevant       | to           | include     | such         | a benchmark   |            | in a        |          |              |                  |
| tool already   | actively       |              | used        | by the       | community     | such       | as          |          |              |                  |
| the MOABB      |                | library      | [3]. An     | adoption     | would         | also       | be          |          |              |                  |

| Glossary |     |     |     |     |     |     |     |     |     |     |     |     | 16  |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Glossary
|     |     |     |     |     |     |     | downstream | task | Learningtaskonwhichanetwork |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | --------------------------- | --- | --- | --- | --- |
Acronyms
|     |     |     |     |     |     |     | can be | pre-trained. |     | Downstream |     | tasks | are typ- |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | --- | ---------- | --- | ----- | -------- |
BCI brain-computer interface. 1, 2, 3, 16 ically supervised. In the context of BCI, down-
|                   |                                        |              |        |          |       |     | stream          | tasks          | can be    | the classification |          |             | of imag- |
| ----------------- | -------------------------------------- | ------------ | ------ | -------- | ----- | --- | --------------- | -------------- | --------- | ------------------ | -------- | ----------- | -------- |
|                   |                                        |              |        |          |       |     | ined concepts,  |                | responses | to                 | sensory  | stimuli,    | sleep    |
| c-VEP             | code-modulatedvisuallyevokedpotential. |              |        |          |       | 11, |                 |                |           |                    |          |             |          |
| 16                |                                        |              |        |          |       |     | stages,         | emotions,      | mental    | workload,          |          | drowsiness, |          |
|                   |                                        |              |        |          |       |     | seizure,        | etc. 7,        | 11, 12,   | 14, 16             |          |             |          |
| CNN convolutional |                                        |              | neural | network. | 8, 16 |     |                 |                |           |                    |          |             |          |
|                   |                                        |              |        |          |       |     | human-annotated |                | label     | Labels             | that,    | unlike      | pseudo   |
| DAE denoising     |                                        | autoencoder. |        | 8,       | 16    |     |                 |                |           |                    |          |             |          |
|                   |                                        |              |        |          |       |     | labels, were    | manually       |           | annotated          |          | by humans   | or,      |
| DL deep           | learning.                              | 2,           | 16     |          |       |     |                 |                |           |                    |          |             |          |
|                   |                                        |              |        |          |       |     | in the context  |                | of BCI,   | that               | required | the         | subject  |
| DNN deep          | neural                                 | Network.     |        | 16       |       |     |                 |                |           |                    |          |             |          |
|                   |                                        |              |        |          |       |     | to execute      | a pre-scripted |           | task.              | Examples |             | of such  |
|                   |                                        |              |        |          |       |     | labels in       | BCI            | are the   | imagery            |          | class       | that was |
EEG electroencephalogram. 1, 2, 3, 16 executed during an epoch, the stimulus that was
ERP event-related potential. 11, 16 attended during an epoch, the sleep phase, the
reportedmentalworkload,thelevelofdrowsiness,
| FFT fast | Fourier | transform. |     | 13, | 16  |     |               |     |                                |     |     |     |     |
| -------- | ------- | ---------- | --- | --- | --- | --- | ------------- | --- | ------------------------------ | --- | --- | --- | --- |
|          |         |            |     |     |     |     | etc. However, |     | wewouldnotconsiderthesubject’s |     |     |     |     |
FIt-SNE FFT-acceleratedinterpolation-basedt-SNE. id or the electrode names as human-annotated
| 13, | 16  |     |     |     |     |     | labels. 6, | 7, 10, | 16  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | --- | --- | --- | --- | --- |
GAN generative adversarial network. 7, 9, 14, 16 pretext task Learning task on which a network
|                 |     |              |     |           |     |     | can be       | pre-trained.                       |         | Training |              | for | pretext  |
| --------------- | --- | ------------ | --- | --------- | --- | --- | ------------ | ---------------------------------- | ------- | -------- | ------------ | --- | -------- |
| ICA independent |     | component    |     | analysis. | 16  |     |              |                                    |         |          |              |     |          |
|                 |     |              |     |           |     |     | tasks is     | typically                          | done    | by       | unsupervised |     | learning |
|                 |     |              |     |           |     |     | algorithms.  | 7,                                 | 11, 12, | 16       |              |     |          |
| MAE masked      |     | autoencoder. |     | 8, 16     |     |     |              |                                    |         |          |              |     |          |
|                 |     |              |     |           |     |     | pseudo label | Pseudolabels,unlikehuman-annotated |         |          |              |     |          |
MLP multilayer perceptron. 8, 16 labels, are automatically generated labels based
ondataattributes(e.g.,chronologicalorderofthe
| NLP natural |     | language | processing. |     | 3, 8, 11, 16 |     |     |     |     |     |     |     |     |
| ----------- | --- | -------- | ----------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
timesamples,spatialpositionoftheelectrodes),or
|                     |              |           |           |           |                |       | on the meta-data |          | associated  |        | with      | the recordings, |          |
| ------------------- | ------------ | --------- | --------- | --------- | -------------- | ----- | ---------------- | -------- | ----------- | ------ | --------- | --------------- | -------- |
| PCA principal       |              | component |           | analysis. | 12, 13, 16     |       |                  |          |             |        |           |                 |          |
|                     |              |           |           |           |                |       | (i.g., subject   |          | id, subject | age,   | electrode |                 | names,   |
|                     |              |           |           |           |                |       | etc.). 7,        | 8, 10,   | 16          |        |           |                 |          |
| SAE sparse          | autoencoder. |           | 8,        | 16        |                |       |                  |          |             |        |           |                 |          |
| SSL self-supervised |              |           | learning. |           | Glossary:      | self- |                  |          |             |        |           |                 |          |
|                     |              |           |           |           |                |       | self-supervised  | learning |             | Subset | of        | the             | unsuper- |
| supervised          |              | learning, | 1,        | 6, 7, 8,  | 9, 10, 11, 15, | 16    |                  |          |             |        |           |                 |          |
|                     |              |           |           |           |                |       | vised learning   |          | algorithms  | that   | are       | trained         | with     |
SSVEP steady-statevisuallyevokedpotential. 11,16 pseudo labels [49] . 16
| SVM support |     | vector | machine. | 16  |     |     |              |          |     |                           |     |     |     |
| ----------- | --- | ------ | -------- | --- | --- | --- | ------------ | -------- | --- | ------------------------- | --- | --- | --- |
|             |     |        |          |     |     |     | unsupervised | learning |     | Machinelearningalgorithms |     |     |     |
t-SNE t-distributed stochastic neighbor embedding. that do not use human-annotated labels. 7, 8, 16
13, 16
| UMAP            | uniform | manifold     |     | qpproximation | and    | projec- |     |     |     |     |     |     |     |
| --------------- | ------- | ------------ | --- | ------------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
| tion.           | 6, 13,  | 16           |     |               |        |         |     |     |     |     |     |     |     |
| VAE variational |         | autoencoder. |     | 8,            | 10, 16 |         |     |     |     |     |     |     |     |

REFERENCES 17
References 48550/arXiv.2304.12210. arXiv: 2304.12210
[cs].
[1] J.-B. Alayrac, J. Donahue, P. Luc, A. Miech,
[8] D. Bank, N. Koenigstein, and R. Giryes.
I. Barr, Y. Hasson, K. Lenc, A. Mensch, K.
Autoencoders, Apr. 2021. arXiv: 2003.05991
Millican, M. Reynolds, R. Ring, E. Rutherford,
[cs, stat].
S. Cabi, T. Han, Z. Gong, S. Samangooei,
[9] H. Banville, O. Chehab, A. Hyv¨arinen, D.-A.
M. Monteiro, J. L. Menick, S. Borgeaud,
Engemann, and A. Gramfort. Uncovering the
A. Brock, A. Nematzadeh, S. Sharifzadeh,
structure of clinical EEG signals with self-
M. Bin´kowski, R. Barreira, O. Vinyals, A.
supervised learning. Journal of Neural Engi-
Zisserman, and K. Simonyan. Flamingo: a
neering, 18(4):046020, Aug. 2021. issn: 1741-
Visual Language Model for Few-Shot Learning.
2560, 1741-2552. doi: 10.1088/1741-2552/
Advances in Neural Information Processing
abca18.
Systems, 35:23716–23736, Dec. 2022.
[10] A. Bardes, J. Ponce, and Y. LeCun. VICReg:
[2] R.Arandjelovic,P.Gronat,A.Torii,T.Pajdla,
Variance-Invariance-Covariance Regularization
and J. Sivic. NetVLAD: CNN Architecture
for Self-Supervised Learning, Jan. 2022. doi:
for Weakly Supervised Place Recognition.
10.48550/arXiv.2105.04906. arXiv: 2105.
In Proceedings of the IEEE Conference on
04906 [cs].
Computer Vision and Pattern Recognition,
[11] P.Bashivan,I.Rish,M.Yeasin,andN.Codella.
pages 5297–5307, 2016.
LearningRepresentationsfromEEGwithDeep
[3] B. Aristimunha, I. Carrara, P. Guetschel, S.
Recurrent-ConvolutionalNeuralNetworks,Feb.
Sedlar,P.Rodrigues,J.Sosulski,D.Narayanan,
2016. doi: 10.48550/arXiv.1511.06448.
E. Bjareholt, B. Quentin, R. T. Schirrmeister,
arXiv: 1511.06448 [cs].
E. Kalunga, L. Darmet, C. Gregoire, A.
[12] F. Bordes, R. Balestriero, and P. Vincent.
Abdul Hussain, R. Gatti, V. Goncharenko, J.
High Fidelity Visualization of What Your Self-
Thielen, T. Moreau, Y. Roy, V. Jayaram, A.
Supervised Representation Knows About, Aug.
Barachant,andS.Chevallier.MotherofallBCI
Benchmarks.Zenodo,Oct.2023.doi:10.5281/ 2022. doi: 10.48550/arXiv.2112.09164.
arXiv: 2112.09164 [cs].
ZENODO.10034223.
[13] T. Bru¨sch, M. N. Schmidt, and T. S. Alstrøm.
[4] B. Aristimunha, R. Y. de Camargo, S. Cheval-
Multi-view self-supervised learning for multi-
lier, O. Lucena, A. G. Thomas, M. J. Cardoso,
variate variable-channel time series, July 2023.
W.H.L.Pinaya,andJ.Dafflon.SyntheticSleep
doi: 10.48550/arXiv.2307.09614. arXiv:
EEG Signal Generation using Latent Diffusion
2307.09614 [cs, eess, stat].
Models. In Deep Generative Models for Health
[14] S. Castan˜o-Candamil, A. Meinel, and M.
Workshop NeurIPS 2023, Oct. 2023.
Tangermann. Post-hoc Labeling of Arbitrary
[5] N. Ayoobi and E. B. Sadeghian. A subject-
M/EEG Recordings for Data-Efficient Evalu-
independent brain-computer interface frame-
ation of Neural Decoding Methods. Frontiers
work based on supervised autoencoder. In An-
in Neuroinformatics, 13, 2019. issn: 1662-5196.
nual International Conference of the IEEE
doi: 10.3389/fninf.2019.00055.
Engineering in Medicine and Biology Soci-
ety, pages 218–221, 2022. doi: 10 . 1109 / [15] H. Chen, D. Wang, M. Xu, and Y. Chen. CRE-
TSCAE: A novel classification model based
embc48229.2022.9871590.
on stacked convolutional autoencoder for dual-
[6] A. Baevski, Y. Zhou, A. Mohamed, and M.
target RSVP-BCI tasks. IEEE transactions on
Auli. Wav2vec 2.0: A Framework for Self-
bio-medical engineering, 2024. issn: 1558-2531.
SupervisedLearningofSpeechRepresentations.
doi: 10.1109/TBME.2024.3361716.
In Advances in Neural Information Processing
[16] T. Chen, S. Kornblith, M. Norouzi, and G.
Systems,volume33,pages12449–12460.Curran
Hinton. A Simple Framework for Contrastive
Associates, Inc., 2020.
Learning of Visual Representations, June 2020.
[7] R. Balestriero, M. Ibrahim, V. Sobal, A. doi: 10.48550/arXiv.2002.05709. arXiv:
Morcos,S.Shekhar,T.Goldstein,F.Bordes,A.
2002.05709 [cs, stat].
Bardes, G. Mialon, Y. Tian, A. Schwarzschild,
[17] Y.-J. Chen, P.-C. Chen, S.-C. Chen, and C.-M.
A. G. Wilson, J. Geiping, Q. Garrido, P.
Wu. Denoising autoencoder-based feature ex-
Fernandez, A. Bar, H. Pirsiavash, Y. LeCun,
traction to robust SSVEP-Based BCIs. Sensors
and M. Goldblum. A Cookbook of Self-
(Basel, Switzerland), 21(15), 2021. issn: 1424-
Supervised Learning, Apr. 2023. doi: 10 .
8220. doi: 10.3390/s21155019.

REFERENCES 18
[18] S. Chevallier, I. Carrara, B. Aristimunha, P. June 2010. issn: 1573-1405. doi: 10.1007/
Guetschel, S. Sedlar, B. Lopes, S. Velut, S. s11263-009-0275-4.
Khazem, and T. Moreau. The largest EEG- [27] F. Fahimi, S. Dosen, K. K. Ang, N. Mrachacz-
based BCI reproducibility study for open Kersting, and C. Guan. Generative adversar-
science: the MOABB benchmark, Apr. 2024. ialnetworks-baseddataaugmentationforbrain-
doi: 10.48550/arXiv.2404.15319. arXiv: computer interface. IEEE transactions on neu-
2404.15319 [cs, eess, q-bio]. ral networks and learning systems, 32(9):4039–
[19] H.-Y. S. Chien, H. Goh, C. M. Sandino, and 4051, 2021. issn: 2162-2388. doi: 10.1109/
J. Y. Cheng. MAEEG: Masked Auto-encoder tnnls.2020.3016666.
for EEG Representation Learning, Oct. 2022. [28] R. Ferri, C. Babiloni, V. Karami, A. I. Trig-
doi: 10.48550/arXiv.2211.02625. arXiv: giani, F. Carducci, G. Noce, R. Lizio, M. T.
2211.02625 [cs, eess]. Pascarelli, A. Soricelli, F. Amenta, A. Bozzao,
[20] C.-C.Chuang,C.-C.Lee,C.-H.Yeng,E.-C.So, A. Romano, F. Giubilei, C. D. Percio, F. Stoc-
B.-S. Lin, and Y.-J. Chen. Convolutional de- chi, G. B. Frisoni, F. Nobili, L. Patan`e, and
noising autoencoder based SSVEP signal en- P. Arena. Stacked autoencoders as new models
hancementtoSSVEP-basedBCIs.Microsystem for an accurate Alzheimer’s disease classifica-
Technologies-Micro-AndNanosystems-Information tion support using resting-state EEG and MRI
StorageAndProcessingSystems,28(1):237–244, measurements. Clinical neurophysiology : offi-
2022. issn: 0946-7076. doi: 10.1007/s00542- cial journal of the International Federation of
019-04654-2. Clinical Neurophysiology,132(1):232–245,2021.
[21] W. Cui, W. Jeong, P. Th¨olke, T. Medani, K. issn: 1872-8952. doi: 10.1016/j.clinph.
Jerbi, A. A. Joshi, and R. M. Leahy. Neuro- 2020.09.015.
GPT: Developing A Foundation Model for [29] R. D. Flint, M. C. Tate, K. Li, J. W.
EEG, Nov. 2023. doi: 10.48550/arXiv.2311. Templer, J. M. Rosenow, C. Pandarinath, and
03764. arXiv: 2311.03764 [cs, eess]. M. W. Slutzky. The Representation of Finger
[22] J. Deng, W. Dong, R. Socher, L.-J. Li, Movement and Force in Human Motor and
K. Li, and L. Fei-Fei. ImageNet: A large- Premotor Cortices. eNeuro, 7(4), Aug. 2020.
scale hierarchical image database. In IEEE issn: 2373-2822. doi: 10.1523/ENEURO.0063-
Conference on Computer Vision and Pattern 20.2020.
Recognition,pages248–255,June2009.doi:10. [30] N. M. Foumani, G. Mackellar, S. Ghane, S.
1109/CVPR.2009.5206848. Irtza, N. Nguyen, and M. Salehi. EEG2Rep:
[23] J. Devlin, M.-W. Chang, K. Lee, and K. EnhancingSelf-supervisedEEGRepresentation
Toutanova. BERT: Pre-training of Deep Bidi- ThroughInformativeMaskedInputs,Feb.2024.
rectional Transformers for Language Under- doi: 10.48550/arXiv.2402.17772. arXiv:
standing, May 2019. doi: 10.48550/arXiv. 2402.17772 [cs, eess].
1810.04805. arXiv: 1810.04805 [cs]. [31] Y. Ganin and V. Lempitsky. Unsupervised Do-
[24] A. Ditthapron, N. Banluesombatkul, S. Ke- main Adaptation by Backpropagation. In Pro-
trat, E. Chuangsuwanich, and T. Wilaiprasit- ceedings of the 32nd International Conference
porn. Universal Joint Feature Extraction for onMachineLearning,pages1180–1189.PMLR,
P300 EEG Classification Using Multi-Task Au- June 2015.
toencoder. IEEE Access, 7:68415–68428, 2019. [32] B.Gao,J.Zhou,Y.Yang,J.Chi,andQ.Yuan.
issn: 2169-3536. doi: 10.1109/ACCESS.2019. Generative adversarial network and convolu-
2919143. tional neural network-based EEG imbalanced
[25] H. Dose, J. S. Møller, H. K. Iversen, and classificationmodelforseizuredetection.Biocy-
S. Puthusserypady. An end-to-end deep learn- bernetics And Biomedical Engineering,42(1):1–
ing approach to MI-EEG signal classification
15,2022.issn:0208-5216.doi:10.1016/j.bbe.
for BCIs. Expert Systems with Applications, 2021.11.002.
114:532–542, Dec. 2018. issn: 0957-4174. doi: [33] H. Ghazikhani and M. Rouhani. A stacked
10.1016/j.eswa.2018.08.031. autoencoders approach for a P300 speller BCI.
[26] M.Everingham,L.VanGool,C.K.I.Williams, In 8th International Conference On Computer
J. Winn, and A. Zisserman. The Pascal Visual And Knowledge Engineering, pages 1–6, 2018.
Object Classes (VOC) Challenge. International doi: 10.1109/iccke.2018.8566534.
Journal of Computer Vision, 88(2):303–338,

|     | REFERENCES |     |     |     |     |     |     |     |     |     |     |     |     | 19  |
| --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[34] I. Goodfellow, J. Pouget-Abadie, M. Mirza, [43] I. Higgins, L. Matthey, X. Glorot, A. Pal,
B. Xu, D. Warde-Farley, S. Ozair, A. B. Uria, C. Blundell, S. Mohamed, and A.
Courville, and Y. Bengio. Generative adver- Lerchner. Early Visual Concept Learning with
doi:
sarial networks. Communications of the ACM, Unsupervised Deep Learning, Sept. 2016.
63(11):139–144, Oct. 2020. issn: 0001-0782. 10.48550/arXiv.1606.05579. arXiv: 1606.
|     | doi: | 10.1145/3422622. |     |     |     |     |     |     | 05579 [cs, | q-bio, | stat]. |     |     |     |
| --- | ---- | ---------------- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ------ | --- | --- | --- |
[35] P. Guetschel, T. Moreau, and M. Tangermann. [44] G. E. Hinton and S. Roweis. Stochastic
S-JEPA: towards seamless cross-dataset trans- Neighbor Embedding. In Advances in Neural
fer through dynamic spatial attention, Mar. Information Processing Systems, volume 15.
|     | 2024. | doi: | 10.48550/arXiv.2403.11772. |     |     |     |     |     | MIT Press, | 2002. |     |     |     |     |
| --- | ----- | ---- | -------------------------- | --- | --- | --- | --- | --- | ---------- | ----- | --- | --- | --- | --- |
arXiv: 2403.11772 [cs]. [45] J. F. Hwaidi and T. M. Chen. Classification
[36] P. Guetschel, T. Papadopoulo, and M. Tanger- of motor imagery EEG signals based on deep
mann. An embedding for EEG signals learned autoencoder and convolutional neural network
doi:
using a triplet loss, Mar. 2023. 10.48550/ approach. IEEE access : practical innovations,
ARXIV.2304.06495. arXiv: 2304.06495 [cs, open solutions, 10:48071–48081, 2022. issn:
|      | eess]. |            |     |              |     |     |         |     | 2169-3536. | doi: | 10 . 1109 | / access |     | . 2022 . |
| ---- | ------ | ---------- | --- | ------------ | --- | --- | ------- | --- | ---------- | ---- | --------- | -------- | --- | -------- |
| [37] | P.     | Guetschel, | T.  | Papadopoulo, | and | M.  | Tanger- |     | 3171906.   |      |           |          |     |          |
mann. Embedding neurophysiological signals. [46] V. Jayaram, M. Alamgir, Y. Altun, B.
In International Conference on Metrology for Scholkopf, and M. Grosse-Wentrup. Transfer
eXtended Reality, Artificial Intelligence, and learning in brain-computer interfaces. IEEE
NeuralEngineering(MetroXRAINE),pages169– ComputationalIntelligenceMagazine,11(1):20–
174, Rome. IEEE, Oct. 2022. doi: 10.1109/ 31, 2016. issn: 1556-603X. doi: 10.1109/MCI.
|     | metroxraine54828.2022.9967496. |     |     |     |     |     |     |     | 2015.2501545. |     |     |     |     |     |
| --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
[38] R. Hadsell, S. Chopra, and Y. LeCun. Dimen- [47] E.Jeon, W. Ko, J. S.Yoon, andH.-I. Suk. Mu-
sionality Reduction by Learning an Invariant tual Information-Driven Subject-Invariant and
Mapping. In IEEE Computer Society Confer- Class-Relevant Deep Representation Learning
ence on Computer Vision and Pattern Recog- inBCI.IEEE Transactions on Neural Networks
nition (CVPR’06), volume 2, pages 1735–1742, and Learning Systems:1–11, 2021. issn: 2162-
|     |     |     | doi: |     |     |     |     |     |     |     | doi: |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
June 2006. 10.1109/CVPR.2006.100. 237X, 2162-2388. 10.1109/TNNLS.2021.
3100583.
| [39] | N.  | Halko, | P. G. | Martinsson, | and | J. A. | Tropp. |     |     |     |     |     |     |     |
| ---- | --- | ------ | ----- | ----------- | --- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
Finding Structure with Randomness: Stochas- [48] R. Jiang, L. Sun, X. Wang, and Y. Xu. Appli-
tic Algorithms for Constructing Approximate cation of transformer with auto-encoder in mo-
matrix Decompositions. California Institute of tor imagery EEG signals. In 14th International
Technology, Oct. 2011. doi: 10.7907/PK8V- Conference on Wireless Communication and
isbn:
|      | V047. |              |     |       |                |     |     |     | Signal Processing, |     | pages | 631–637,           | 2022. |     |
| ---- | ----- | ------------ | --- | ----- | -------------- | --- | --- | --- | ------------------ | --- | ----- | ------------------ | ----- | --- |
|      |       |              |     |       |                |     |     |     | 978-1-66545-085-0. |     | doi:  | 10.1109/WCSP55476. |       |     |
| [40] | K.    | G. Hartmann, |     | R. T. | Schirrmeister, |     | and |     |                    |     |       |                    |       |     |
2022.10039415.
|     | T.  | Ball. | EEG-GAN: | Generative |     | adversarial |     |     |     |     |     |     |     |     |
| --- | --- | ----- | -------- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
networks for electroencephalograhic (EEG) [49] L.JingandY.Tian.Self-SupervisedVisualFea-
doi:
brain signals, June 2018. 10 . 48550 / ture Learning With Deep Neural Networks: A
arXiv.1806.01875. arXiv: 1806.01875 [cs, Survey. IEEE Transactions on Pattern Analy-
eess, q-bio, stat]. sisandMachineIntelligence,43(11):4037–4058,
|      |       |         |     |         |            |       |     |     | Nov. 2021. | issn: | 1939-3539. | doi: | 10.1109/ |     |
| ---- | ----- | ------- | --- | ------- | ---------- | ----- | --- | --- | ---------- | ----- | ---------- | ---- | -------- | --- |
| [41] | A.-W. | Harzing | -.  | Publish | or Perish, | 2007. |     |     |            |       |            |      |          |     |
TPAMI.2020.2992393.
| [42] | Y.  | He, Z. | Lu, J. | Wang, S. | Ying, | and J. | Shi. A |      |             |     |          |     |          |      |
| ---- | --- | ------ | ------ | -------- | ----- | ------ | ------ | ---- | ----------- | --- | -------- | --- | -------- | ---- |
|      |     |        |        |          |       |        |        | [50] | L. Jingwei, | C.  | Yin, and | Z.  | Weidong. | Deep |
self-supervisedlearningbasedchannelattention
MLP-Mixer network for motor imagery decod- learning EEG response representation for brain
|     |      |      |              |     |        |         |     |     | computer | interface. | In  | 2015 | 34th | Chinese |
| --- | ---- | ---- | ------------ | --- | ------ | ------- | --- | --- | -------- | ---------- | --- | ---- | ---- | ------- |
|     | ing. | IEEE | transactions | on  | neural | systems | and |     |          |            |     |      |      |         |
rehabilitation engineering, 30:2406–2417, 2022. Control Conference (CCC), pages 3518–3523,
|     | issn: |            |     | doi:                |     |     |     |     | Hangzhou,      | China. | IEEE,                    | July 2015. | isbn: | 978- |
| --- | ----- | ---------- | --- | ------------------- | --- | --- | --- | --- | -------------- | ------ | ------------------------ | ---------- | ----- | ---- |
|     |       | 1558-0210. |     | 10.1109/tnsre.2022. |     |     |     |     |                |        |                          |            |       |      |
|     |       |            |     |                     |     |     |     |     | 988-15638-9-7. |        | doi: 10.1109/ChiCC.2015. |            |       |      |
3199363.
7260182.

|     | REFERENCES |     |     |     |     |     |     |     |     |     |     |     |     | 20  |
| --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[51] Y.H.Kang,D.Kim,andS.W.Lee.Meta-BCI: [60] S. Kumaraguru and M. R. E. Jebarani. Trust
Perspectivesonaroleofself-supervisedlearning aware routing using sunflower sine cosine-based
in meta brain computer interface. In 10th stacked autoencoder approach for EEG signal
International Winter Conference On Brain- classification in WSN. Journal Of High Speed
Computer Interface (Bci2022), 2022. doi: 10. Networks,27(2):101–119,2021.issn:0926-6801.
|     | 1109/bci53720.2022.9734995. |     |     |     |     |     |     | doi: | 10.3233/jhs-210654. |     |     |     |     |     |
| --- | --------------------------- | --- | --- | --- | --- | --- | --- | ---- | ------------------- | --- | --- | --- | --- | --- |
[52] R. Kiros, R. Salakhutdinov, and R. S. Zemel. [61] D.-Y. Lee, J.-H. Jeong, B.-H. Lee, and S.-W.
Unifying Visual-Semantic Embeddings with Lee. Motor imagery classification using inter-
Multimodal Neural Language Models, 2014. task transfer learning via a channel-wise vari-
doi: 10.48550/ARXIV.1411.2539. ational autoencoder-based convolutional neu-
[53] G. Klein, P. Guetschel, G. Silvestri, and ral network. IEEE transactions on neural sys-
|     |                |     |     |              |     |         |     | tems | and | rehabilitation |     | engineering, |      | 30:226– |
| --- | -------------- | --- | --- | ------------ | --- | ------- | --- | ---- | --- | -------------- | --- | ------------ | ---- | ------- |
|     | M. Tangermann. |     |     | Synthesizing | EEG | Signals |     |      |     |                |     |              |      |         |
|     |                |     |     |              |     |         |     |      |     | issn:          |     |              | doi: |         |
from Event-Related Potential Paradigms with 237, 2022. 1558-0210. 10.1109/
|     |             |           |     |         |      |       | doi: | tnsre.2022.3143836. |     |     |     |     |     |     |
| --- | ----------- | --------- | --- | ------- | ---- | ----- | ---- | ------------------- | --- | --- | --- | --- | --- | --- |
|     | Conditional | Diffusion |     | Models, | Mar. | 2024. |      |                     |     |     |     |     |     |     |
10.48550/arXiv.2403.18486. arXiv: 2403. [62] H. Li, J. Tang, W. Li, W. Dai, Y. Liu, and Z.
18486 [cs, eess]. Zhou. Multi-task collaborative network: Bridge
[54] W.Ko,E.Jeon,S.Jeong,andH.-I.Suk.Multi- the supervised and self-supervised learning for
|     |              |     |         |     |                    |     |     | EEG | classification |     | in RSVP | tasks. | IEEE | trans- |
| --- | ------------ | --- | ------- | --- | ------------------ | --- | --- | --- | -------------- | --- | ------- | ------ | ---- | ------ |
|     | Scale Neural |     | Network | for | EEG Representation |     |     |     |                |     |         |        |      |        |
Learning in BCI. IEEE Computational Intelli- actionsonneuralsystemsandrehabilitationen-
|     |       |           |              |     |     |       | issn: | gineering, |     | 32:638–651, |     | 2024. | issn: | 1558-0210. |
| --- | ----- | --------- | ------------ | --- | --- | ----- | ----- | ---------- | --- | ----------- | --- | ----- | ----- | ---------- |
|     | gence | Magazine, | 16(2):31–45, |     | May | 2021. |       |            |     |             |     |       |       |            |
doi: 10.1109/TNSRE.2024.3357863.
|     | 1556-603X, | 1556-6048. |     | doi: | 10.1109/MCI. |     |     |     |     |     |     |     |     |     |
| --- | ---------- | ---------- | --- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2021.3061875. [63] L. H. Li, M. Yatskar, D. Yin, C.-J. Hsieh,
[55] D. Kobak and P. Berens. The art of using and K.-W. Chang. VisualBERT: A Simple and
|     |       |                 |     |                  |     |        |     | Performant |     | Baseline | for | Vision | and | Language, |
| --- | ----- | --------------- | --- | ---------------- | --- | ------ | --- | ---------- | --- | -------- | --- | ------ | --- | --------- |
|     | t-SNE | for single-cell |     | transcriptomics. |     | Nature |     |            |     |          |     |        |     |           |
doi:
Communications, 10(1):5416, Nov. 2019. issn: 2019. 10.48550/ARXIV.1908.03557.
doi:
2041-1723. 10.1038/s41467-019-13056- [64] X. Li, Z. Zhao, D. Song, Y. Zhang, C. Niu,
|     | x.  |     |     |     |     |     |     | J. Zhang, |     | J. Huo, | and | J. Li. | Variational | au- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------- | --- | ------ | ----------- | --- |
toencoderbasedlatentfactordecodingofmulti-
| [56] | D. Kobak | and | G. C. | Linderman. |     | Initialization |     |     |     |     |     |     |     |     |
| ---- | -------- | --- | ----- | ---------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
iscriticalforpreservingglobaldatastructurein channelEEGforemotionrecognition.IEEEIn-
|     |                |     |       |             |                |     |      | ternational          |     | Conference |     | On Bioinformatics |       | And        |
| --- | -------------- | --- | ----- | ----------- | -------------- | --- | ---- | -------------------- | --- | ---------- | --- | ----------------- | ----- | ---------- |
|     | both t-SNE     | and | UMAP. | Nature      | Biotechnology, |     |      |                      |     |            |     |                   |       |            |
|     |                |     |       |             |                |     |      | Biomedicine:684–687, |     |            |     | 2019.             | issn: | 2156-1125. |
|     | 39(2):156–157, |     | Feb.  | 2021. issn: | 1546-1696.     |     | doi: |                      |     |            |     |                   |       |            |
doi:
|     | 10.1038/s41587-020-00809-z. |     |     |     |     |     |     |     | 10.1109/bibm47256.2019.8983341. |     |     |     |     |     |
| --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- |
[57] R. J. Kobler, J.-i. Hirayama, Q. Zhao, and M. [65] X. Li, Z. Zhao, D. Song, Y. Zhang, J. Pan,
|     |           |     |                 |     |       |         |     | L.  | Wu, J. | Huo, | C.  | Niu, | and | D. Wang. |
| --- | --------- | --- | --------------- | --- | ----- | ------- | --- | --- | ------ | ---- | --- | ---- | --- | -------- |
|     | Kawanabe. | SPD | domain-specific |     | batch | normal- |     |     |        |      |     |      |     |          |
ization to crack interpretable unsupervised do- Latent factor decoding of multi-channel EEG
|     |                         |     |     |      |            | doi:       |     | for    | emotion | recognition |            | through | autoencoder-     |     |
| --- | ----------------------- | --- | --- | ---- | ---------- | ---------- | --- | ------ | ------- | ----------- | ---------- | ------- | ---------------- | --- |
|     | main adaptation         |     | in  | EEG, | Oct. 2022. |            | 10. |        |         |             |            |         |                  |     |
|     |                         |     |     |      |            |            |     | like   | neural  | networks.   | Frontiers  |         | in neuroscience, |     |
|     | 48550/arXiv.2206.01323. |     |     |      | arXiv:     | 2206.01323 |     |        |         |             |            |         |                  |     |
|     |                         |     |     |      |            |            |     |        |         | issn:       |            |         | doi:             |     |
|     | [cs, eess].             |     |     |      |            |            |     | 14:87, | 2020.   |             | 1662-4548. |         | 10.3389/         |     |
fnins.2020.00087.
| [58] | D. Kostas, | S.  | Aroca-Ouellette, |     | and | F. Rudzicz. |      |         |       |     |       |        |       |           |
| ---- | ---------- | --- | ---------------- | --- | --- | ----------- | ---- | ------- | ----- | --- | ----- | ------ | ----- | --------- |
|      |            |     |                  |     |     |             | [66] | Q. Lin, | S.-q. | Ye, | X.-m. | Huang, | S.-y. | Li, M.-z. |
BENDR:UsingTransformersandaContrastive
Self-Supervised Learning Task to Learn From Zhang, Y. Xue, and W.-S. Chen. Classification
|     |         |               |     |            |       |           |       | of epileptic |     | EEG   | signals | with      | stacked | sparse      |
| --- | ------- | ------------- | --- | ---------- | ----- | --------- | ----- | ------------ | --- | ----- | ------- | --------- | ------- | ----------- |
|     | Massive | Amounts       | of  | EEG        | Data. | Frontiers | in    |              |     |       |         |           |         |             |
|     |         |               |     |            |       |           |       | autoencoder  |     | based | on deep | learning. |         | Intelligent |
|     | Human   | Neuroscience, |     | 15:653659, |       | June      | 2021. |              |     |       |         |           |         |             |
issn: 1662-5161. doi: 10.3389/fnhum.2021. Computing Methodologies, 9773:802–810, 2016.
|     |     |     |     |     |     |     |     | issn: | 0302-9743. |     | doi: 10.1007/978-3-319- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | --- | ----------------------- | --- | --- | --- |
653659.
42297-8_74.
| [59] | S. Kullback | and | R.  | A. Leibler. | On  | Information |     |     |     |     |     |     |     |     |
| ---- | ----------- | --- | --- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
and Sufficiency. The Annals of Mathematical [67] T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P.
|     |             |              |     |         |        | issn:  |       | Perona,  | D.            | Ramanan,       |       | P. Doll´ar, | and        | C. L.    |
| --- | ----------- | ------------ | --- | ------- | ------ | ------ | ----- | -------- | ------------- | -------------- | ----- | ----------- | ---------- | -------- |
|     | Statistics, | 22(1):79–86, |     | Mar.    | 1951.  |        | 0003- |          |               |                |       |             |            |          |
|     |             |              |     |         |        |        |       | Zitnick. | Microsoft     |                | COCO: | Common      |            | Objects  |
|     | 4851,       | 2168-8990.   |     | doi: 10 | . 1214 | / aoms | /     |          |               |                |       |             |            |          |
|     | 1177729694. |              |     |         |        |        |       | in       | Context.      | In             | D.    | Fleet,      | T. Pajdla, | B.       |
|     |             |              |     |         |        |        |       | Schiele, | and           | T. Tuytelaars, |       | editors,    |            | Computer |
|     |             |              |     |         |        |        |       | Vision   | –             | ECCV           | 2014, | Lecture     |            | Notes in |
|     |             |              |     |         |        |        |       | Computer |               | Science,       | pages |             | 740–755,   | Cham.    |
|     |             |              |     |         |        |        |       | Springer | International |                |       | Publishing, | 2014.      | isbn:    |

REFERENCES 21
978-3-319-10602-1. doi: 10.1007/978-3-319- [77] P. Nejedly, V. Kremen, K. Lepkova, F. Mivalt,
10602-1_48. V. Sladky, T. Pridalova, F. Plesinger, P. Jurak,
[68] G. C. Linderman, M. Rachh, J. G. Hoskins, S. M. Pail, M. Brazdil, P. Klimes, and G. Worrell.
Steinerberger,andY.Kluger.Fastinterpolation- Utilization of temporal autoencoder for semi-
based t-SNE for improved visualization of supervised intracranial EEG clustering and
single-cell RNA-seq data. Nature Methods, classification.Scientificreports,13(1):744,2023.
16(3):243–245,Mar.2019.issn:1548-7105.doi: issn: 2045-2322. doi: 10.1038/s41598-023-
10.1038/s41592-018-0308-4. 27978-6.
[69] C. Liu, J. Jin, R. Xu, S. Li, C. Zuo, H. Sun, X. [78] I. Obeid and J. Picone. The Temple University
Wang,andA.Cichocki.Distinguishablespatial- Hospital EEG Data Corpus. Frontiers in
spectral feature learning neural network frame- Neuroscience, 10, May 2016. issn: 1662-453X.
work for motor imagery-based brain-computer doi: 10.3389/fnins.2016.00196.
interface. Journal of neural engineering, 18(4), [79] N. Oskolkov. tSNE vs. UMAP: Global Struc-
2021. issn: 1741-2552. doi: 10.1088/1741- ture. https://towardsdatascience.com/tsne-vs-
2552/ac1d36. umap-global-structure-4d8045acba17,Mar.2020.
[70] J. Liu, G. Wu, Y. Luo, S. Qiu, S. Yang, W. (Visited on 05/17/2024).
Li,andY.Bi.EEG-Basedemotionclassification [80] Y. Ou, S. Sun, H. Gan, R. Zhou, and Z.
using a deep neural network and sparse Yang. An improved self-supervised learning for
autoencoder.Frontiersinsystemsneuroscience, EEG classification. Mathematical Biosciences
14:43, 2020. issn: 1662-5137. doi: 10.3389/ and Engineering, 19(7):6907–6922, 2022. issn:
fnsys.2020.00043. 1551-0018. doi: 10.3934/mbe.2022325.
[71] N.Mammone,C.Ieracitano,H.Adeli,andF.C. [81] O. O¨zdenizci, Y. Wang, T. Koike-Akino, and
Morabito. AutoEncoder filter bank common D. Erdogmus. Transfer Learning in Brain-
spatial patterns to decode motor imagery from Computer Interfaces with Adversarial Varia-
EEG. IEEE journal of biomedical and health tional Autoencoders. In 2019 9th International
informatics, 27(5):2365–2376, 2023. issn: 2168- IEEE/EMBS Conference on Neural Engineer-
2208. doi: 10.1109/JBHI.2023.3243698. ing (NER), pages 207–210, San Francisco, CA,
[72] L. McInnes. Performance Comparison of Di- USA. IEEE, Mar. 2019. isbn: 978-1-5386-7921-
mension Reduction Implementations. UMAP 0. doi: 10.1109/NER.2019.8716897.
documentation.https://umap-learn.readthedocs.io/e[8n2/]latOes.t/O¨bzednecnhimzcai,rkYi.nWg.hatnmg,l.T.Koike-Akino,andD.
(Visited on 05/17/2024). Erdo˘gmu¸s. Learning Invariant Representations
[73] L. McInnes, J. Healy, and J. Melville. UMAP: From EEG via Adversarial Inference. IEEE
Uniform Manifold Approximation and Projec- Access, 8:27074–27085, 2020. issn: 2169-3536.
tion for Dimension Reduction, Sept. 2020. doi: doi: 10.1109/ACCESS.2020.2971600.
10.48550/arXiv.1802.03426. arXiv: 1802. [83] S. J. Pan and Q. Yang. A Survey on Transfer
03426 [cs, stat]. Learning. IEEE Transactions on Knowledge
[74] S.MirzaeiandP.Ghasemi.EEGmotorimagery and Data Engineering, 22(10):1345–1359, Oct.
classification using dynamic connectivity pat- 2010. issn: 1558-2191. doi: 10.1109/TKDE.
terns and convolutional autoencoder. Biomed- 2009.191.
ical Signal Processing And Control, 68, 2021.
[84] P. K. Parashiva and A. P. Vinod. A New
issn: 1746-8094. doi: 10.1016/j.bspc.2021.
Channel Selection Method using Autoencoder
102584.
for Motor Imagery based Brain Computer In-
[75] M. N. Mohsenvand, M. R. Izadi, and P. terface. In 2019 IEEE International Confer-
Maes. Contrastive Representation Learning ence on Systems, Man and Cybernetics (SMC),
for Electroencephalogram Classification. In pages 3641–3646, Bari, Italy. IEEE, Oct. 2019.
Proceedings of the Machine Learning for Health isbn: 978-1-72814-569-3. doi: 10.1109/SMC.
NeurIPS Workshop, pages 238–253. PMLR, 2019.8914251.
Nov. 2020.
[85] S. Parija, M. Sahani, R. Bisoi, and P. K. Dash.
[76] A. V. Nair, K. M. Kumar, and J. Mathew. An Autoencoder-based improved deep learning ap-
improvedapproachforEEGsignalclassification proach for schizophrenic EEG signal classifica-
using autoencoder. In 8th International Sym- tion. Pattern Analysis And Applications, 2022.
posium On Embedded Computing And System issn: 1433-7541. doi: 10.1007/s10044-022-
Design, pages 6–10, 2018. doi: 10.1109/ised. 01107-x.
2018.8704011.

REFERENCES 22
[86] D. Pei, M. Burns, R. Chandramouli, and R. [94] X. Ran, W. Chen, B. Yvert, and S. Zhang. A
Vinjamuri. Decoding asynchronous reaching in hybrid autoencoder framework of dimensional-
electroencephalography using stacked autoen- ity reduction for brain-computer interface de-
coders. IEEE access : practical innovations, coding. Computers in biology and medicine,
opensolutions,6:52889–52898,2018.issn:2169- 148:105871, 2022. issn: 1879-0534. doi: 10.
3536. doi: 10.1109/access.2018.2869687. 1016/j.compbiomed.2022.105871.
[87] V. M. Petrutiu, L. D. Palcu, C. Lemnaru, M. [95] C. Rommel, T. Moreau, and A. Gramfort.
Dinsoreanu,R.Potolea,R.Mursesan,andV.V. Deep invariant networks with differentiable
Moca.EnhancingtheClassificationofEEGSig- augmentationlayers,Oct.2022.doi:10.48550/
nals using Wasserstein Generative Adversar- arXiv.2202.02142. arXiv: 2202.02142 [cs].
ial Networks. In 2020 IEEE 16th International [96] C. Rommel, T. Moreau, J. Paillard, and
Conference on Intelligent Computer Commu- A. Gramfort. CADDA: Class-wise Automatic
nication and Processing (ICCP), pages 29–34, Differentiable Data Augmentation for EEG
Cluj-Napoca,Romania.IEEE,Sept.2020.isbn: Signals, Feb. 2022. doi: 10.48550/arXiv.
978-1-72819-080-8. doi: 10.1109/ICCP51029. 2106.13695. arXiv: 2106.13695 [cs].
2020.9266157.
[97] C. Rommel, J. Paillard, T. Moreau, and
[88] S. Phadikar, N. Sinha, and R. Ghosh. Unsu- A. Gramfort. Data augmentation for learning
pervised feature extraction with autoencoders predictive models on EEG: a systematic
for EEG based multiclass motor imagery BCI. comparison. Journal of Neural Engineering,
Expert Systems With Applications, 213, 2023. 2022. issn: 1741-2552. doi: 10.1088/1741-
issn: 0957-4174. doi: 10.1016/j.eswa.2022. 2552/aca220.
118901.
[98] S. Roy, S. Dora, K. McCreadie, and G.
[89] C. Phunruangsakao, D. Achanccaray, S.-I. Prasad. MIEEG-GAN: Generating artificial
Izumi, and M. Hayashibe. Multibranch convo- motor imagery electroencephalography signals.
lutional neural network with contrastive repre- International Joint Conference On Neural
sentation learning for decoding same limb mo- Networks,2020.issn:2161-4393.doi:10.1109/
tor imagery tasks. Frontiers in human neuro- ijcnn48605.2020.9206942.
science,16:1032724,2022.issn:1662-5161.doi:
[99] Y. Roy, H. Banville, I. Albuquerque, A. Gram-
10.3389/fnhum.2022.1032724.
fort,T.H. Falk, andJ.Faubert. Deeplearning-
[90] S. K. Prabhakar and S.-W. Lee. SASDL and based electroencephalography analysis: a sys-
RBATQ:Sparseautoencoderwithswarmbased tematic review. Journal of Neural Engineering,
deep learning and reinforcement based Q- 16(5):051001, Oct. 2019. issn: 1741-2560, 1741-
learning for EEG classification. IEEE open 2552. doi: 10.1088/1741-2552/ab260c.
journal of engineering in medicine and biology,
[100] S. Schneider, J. H. Lee, and M. W. Mathis.
3:58–68, 2022. issn: 2644-1276. doi: 10.1109/
Learnable latent embeddings for joint behav-
ojemb.2022.3161837.
ioral and neural analysis, Oct. 2022. doi: 10.
[91] Y. Qiu, W. Zhou, N. Yu, and P. Du. Denois- 48550/arXiv.2204.00673. arXiv: 2204.00673
ing sparse autoencoder-based ictal EEG classi- [cs, q-bio].
fication. IEEE transactions on neural systems
[101] F. Schroff, D. Kalenichenko, and J. Philbin.
and rehabilitation engineering, 26(9):1717–
FaceNet: A unified embedding for face recog-
1726, 2018. issn: 1558-0210. doi: 10.1109/
nition and clustering. In 2015 IEEE Confer-
tnsre.2018.2864306.
ence on Computer Vision and Pattern Recog-
[92] A.Radford,L.Metz,andS.Chintala.Unsuper- nition (CVPR), pages 815–823, Boston, MA,
vised Representation Learning with Deep Con- USA. IEEE, June 2015. isbn: 978-1-4673-6964-
volutional Generative Adversarial Networks, 0. doi: 10.1109/CVPR.2015.7298682.
Jan. 2016. doi: 10.48550/arXiv.1511.06434.
[102] D. Serdyuk, K. Audhkhasi, P. Brakel, B.
arXiv: 1511.06434 [cs].
Ramabhadran, S. Thomas, and Y. Bengio.
[93] P. Rajpurkar, J. Zhang, K. Lopyrev, and Invariant Representations for Noisy Speech
P. Liang. SQuAD: 100,000+ Questions for Recognition,Nov.2016.doi:10.48550/arXiv.
Machine Comprehension of Text, Oct. 2016. 1612.01928. arXiv: 1612.01928 [cs, stat].
doi: 10.48550/arXiv.1606.05250. arXiv:
1606.05250 [cs].

REFERENCES 23
[103] Y. Song, Q. Zheng, B. Liu, and X. Gao. EEG [112] K. Tomonaga, T. Hayakawa, and J. Kobayashi.
Conformer:ConvolutionalTransformerforEEG Experiments on classification of electroen-
DecodingandVisualization.IEEETransactions cephalography (EEG) signals in imagination
onNeuralSystemsandRehabilitationEngineer- of direction using stacked autoencoder. Jour-
ing,31:710–719,2023.issn:1558-0210.doi:10. nal Of Robotics Networking And Artificial Life,
1109/TNSRE.2022.3230250. 4(2):124–128, 2017. issn: 2352-6386. doi: 10.
[104] J.Sosulski,J.-P.Kemmer,andM.Tangermann. 2991/jrnal.2017.4.2.4.
Improving Covariance Matrices Derived from [113] S. Torma and D. L. Szegletes. EEGWave:
Tiny Training Datasets for the Classification of a Denoising Diffusion Probablistic Approach
Event-Related Potentials with Linear Discrim- for EEG Signal Generation, 2023. EasyChair:
inant Analysis. Neuroinformatics, 19(3):461– 10275.
476, July 2021. issn: 1559-0089. doi: 10.1007/ [114] L. van der Maaten and G. Hinton. Visualizing
s12021-020-09501-8. Datausingt-SNE.JournalofMachineLearning
[105] J. Sosulski and M. Tangermann. Introducing Research, 9(86):2579–2605, 2008. issn: 1533-
block-Toeplitz covariance matrices to remaster 7928.
linear discriminant analysis for event-related [115] G. Van Horn, O. Mac Aodha, Y. Song, Y. Cui,
potential brain–computer interfaces. Journal of C.Sun,A.Shepard,H.Adam,P.Perona,andS.
Neural Engineering, 19(6):066001, Nov. 2022. Belongie.TheINaturalistSpeciesClassification
issn: 1741-2552. doi: 10.1088/1741-2552/ and Detection Dataset. In Proceedings of the
ac9c98. IEEE Conference on Computer Vision and
[106] J. Sosulski and M. Tangermann. UMM: Un- Pattern Recognition, pages 8769–8778, 2018.
supervisedMean-differenceMaximization,June [116] T. E. Vanhecke. Zotero. Journal of the Medical
2023. doi: 10.48550/arXiv.2306.11830. Library Association : JMLA, 96(3):275–276,
arXiv: 2306.11830 [cs, stat]. July 2008. issn: 1536-5050. doi: 10.3163/
[107] S. Stephe, T. Jayasankar, and K. V. Kumar. 1536-5050.96.3.022.
Motor imagery EEG recognition using deep [117] A. Vaswani, N. Shazeer, N. Parmar, J. Uszko-
generative adversarial network with EMD for reit, L. Jones, A. N. Gomez, L(cid:32) . Kaiser, and I.
BCI applications. Tehnicki Vjesnik-Technical Polosukhin. Attention is All you Need. In Ad-
Gazette, 29(1):92–100, 2022. issn: 1330-3651. vances in Neural Information Processing Sys-
doi: 10.17559/tv-20210121112228. tems, volume 30. Curran Associates, Inc., 2017.
[108] C. Tan, F. Sun, B. Fang, T. Kong, and [118] C. Vondrick, H. Pirsiavash, and A. Torralba.
W. Zhang. Autoencoder-based transfer learn- Generating Videos with Scene Dynamics. In
ing in brain-computer interface for rehabilita- Advances in Neural Information Processing
tion robot. International Journal Of Advanced Systems, volume 29. Curran Associates, Inc.,
Robotic Systems, 16(2), 2019. issn: 1729-8814. 2016.
doi: 10.1177/1729881419840860.
[119] A. Wang, A. Singh, J. Michael, F. Hill, O.
[109] X. Tang, T. Wang, Y. Du, and Y. Dai. Motor Levy, and S. R. Bowman. GLUE: A Multi-
imagery EEG recognition with KNN-based Task Benchmark and Analysis Platform for
smooth auto-encoder. Artificial intelligence in Natural Language Understanding, Feb. 2019.
medicine, 101:101747, 2019. issn: 1873-2860. arXiv: 1804.07461 [cs].
doi: 10.1016/j.artmed.2019.101747.
[120] H. Wang, L. Cao, C. Huang, J. Jia, Y. Dong,
[110] J. Thielen, P. Marsman, J. Farquhar, and P. C. Fan, and V. H. C. de Albuquerque. A novel
Desain. From full calibration to zero training algorithmicstructureofEEGchannelattention
for a code-modulated visual evoked potentials combined with swin transformer for motor
forbrain–computerinterface.Journal of Neural patterns classification. IEEE transactions on
Engineering, 18(5):056007, Apr. 2021. issn: neural systems and rehabilitation engineering,
1741-2552. doi: 10.1088/1741-2552/abecef. 31:3132–3141, 2023. issn: 1558-0210. doi: 10.
[111] M. E. Tipping and C. M. Bishop. Probabilistic 1109/TNSRE.2023.3297654.
Principal Component Analysis. Journal of the [121] X. Wei, A. A. Faisal, M. Grosse-Wentrup,
Royal Statistical Society Series B: Statistical A. Gramfort, S. Chevallier, V. Jayaram, C.
Methodology, 61(3):611–622, Sept. 1999. issn: Jeunet, S. Bakas, S. Ludwig, K. Barmpas,
1369-7412, 1467-9868. doi: 10.1111/1467- M. Bahri, Y. Panagakis, N. Laskaris, D. A.
9868.00196. Adamos, S. Zafeiriou, W. C. Duong, S. M.

REFERENCES 24
Gordon, V. J. Lawhern, M. S´liwowski, V. and medicine, 109:159–170, 2019. issn: 1879-
Rouanne, and P. Tempczyk. 2021 BEETL 0534. doi: 10.1016/j.compbiomed.2019.04.
Competition: Advancing Transfer Learning for 034.
Subject Independence & Heterogenous EEG [130] X. Yao, T. Li, P. Ding, F. Wang, L. Zhao,
Data Sets. In Proceedings of the NeurIPS A. Gong, W. Nan, and Y. Fu. Emotion
2021 Competitions and Demonstrations Track, classificationbasedontransformerandCNNfor
pages 205–219. PMLR, July 2022. EEG spatial-temporal feature learning. Brain
[122] D. Wu, Y. Xu, and B.-L. Lu. Transfer Learning sciences, 14(3), 2024. issn: 2076-3425. doi: 10.
for EEG-Based Brain–Computer Interfaces: A 3390/brainsci14030268.
Review of Progress Made Since 2016. IEEE [131] Z.Yin,M.Zhao,W.Zhang,Y.Wang,Y.Wang,
Transactions on Cognitive and Developmental andJ.Zhang.Physiological-signal-basedmental
Systems, 14(1):4–19, Mar. 2022. issn: 2379- workload estimation via transfer dynamical
8939. doi: 10.1109/TCDS.2020.3007453. autoencoders in a deep learning framework.
[123] T. Xie, W. Ma, X. Li, W. Li, B. Hao, and X. Neurocomputing,347:212–229,2019.issn:0925-
Tang. Motor imagery EEG recognition based 2312. doi: 10.1016/j.neucom.2019.02.061.
onscheduledempiricalmodedecompositionand [132] Z. Yu, L. Li, W. Zhang, H. Lv, Y. Liu,
adaptivedenoisingautoencoders.IEEEChinese and U. Khalique. An adaptive EEG feature
Automation Congress:1528–1532, 2020. issn: extraction method based on stacked denoising
2688-092X. doi: 10.1109/cac51589.2020. autoencoder for mental fatigue connectivity.
9327855. Neural plasticity, 2021:3965385, 2021. issn:
[124] F. Xu, F. Rong, Y. Miao, Y. Sun, G. Dong, H. 1687-5443. doi: 10.1155/2021/3965385.
Li,J.Li,Y.Wang,andJ.Leng.Representation [133] P. Zhang, X. Wang, J. Chen, W. You, and W.
Learning for Motor Imagery Recognition with Zhang. Spectral and temporal feature learning
Deep Neural Network. Electronics, 10(2):112, with two-stream neural networks for mental
Jan. 2021. issn: 2079-9292. doi: 10.3390/ workload assessment. IEEE transactions on
electronics10020112. neural systems and rehabilitation engineering,
[125] B. Yan, Y. Wang, Y. Li, Y. Gong, L. Guan, 27(6):1149–1159, 2019. issn: 1558-0210. doi:
andS.Yu.AnEEGsignalclassificationmethod 10.1109/tnsre.2019.2913400.
based on sparse auto-encoders and support [134] X. Zhang, X. Chen, M. Dong, H. Liu, C. Ge,
vectormachine.IEEEInternationalConference and L. Yao. Multi-task Generative Adversarial
On Communications In China, 2016. issn: LearningonGeometricalShapeReconstruction
2377-8644. doi: 10.1109/iccchina.2016. from EEG Brain Signals, Feb. 2020. doi: 10.
7636897. 48550/arXiv.1907.13351. arXiv: 1907.13351
[126] C. Yang, M. B. Westover, and J. Sun. BIOT: [cs, eess].
Cross-dataBiosignalLearningintheWild,May [135] X. Zhang, L. Yao, C. Huang, S. S. Kanhere, D.
2023. doi: 10.48550/arXiv.2305.10351. Zhang, and Y. Zhang. Brain2Object: Printing
arXiv: 2305.10351 [cs, eess]. Your Mind from Brain Signals with Spatial
[127] C. Yang, D. Xiao, M. B. Westover, and J. Sun. Correlation Embedding, June 2020. doi: 10.
Self-supervised EEG Representation Learning 48550/arXiv.1810.02223. arXiv: 1810.02223
for Automatic Sleep Staging, Feb. 2023. doi: [cs].
10.48550/arXiv.2110.15278. arXiv: 2110. [136] X.Zhang,L.Yao,Q.Z.Sheng,S.S.Kanhere,T.
15278 [cs, eess]. Gu, and D. Zhang. Converting Your Thoughts
[128] J. Yang, Z. Ma, J. Wang, and Y. Fu. A to Texts: Enabling Brain Typing via Deep
NovelDeepLearningSchemeforMotorImagery Feature Learning of EEG Signals. In 2018
EEGDecodingBasedonSpatialRepresentation IEEE International Conference on Pervasive
Fusion. IEEE Access, 8:202100–202110, 2020. Computing and Communications (PerCom),
issn: 2169-3536. doi: 10.1109/ACCESS.2020. pages 1–10, Mar. 2018. doi: 10.1109/PERCOM.
3035347. 2018.8444575.
[129] S. Yang, Z. Yin, Y. Wang, W. Zhang, Y. [137] X. Zhang, Z. Lu, T. Zhang, H. Li, Y. Wang,
Wang, and J. Zhang. Assessing cognitive and Q. Tao. Realizing the application of
mental workload via EEG signals and an EEG modeling in BCI classification: Based
ensemble deep learning classifier based on on a conditional GAN converter. Frontiers in
denoising autoencoders. Computers in biology neuroscience, 15:727394, 2021. issn: 1662-4548.
doi: 10.3389/fnins.2021.727394.

REFERENCES 25
[138] X.Zhao,D.Liu,L.Ma,Q.Liu,K.Chen,S.Xie,
and Q. Ai. Deep CNN model based on serial-
parallel structure optimization for four-class
motor imagery EEG classification. Biomedical
Signal Processing And Control, 72, 2022. issn:
1746-8094. doi: 10.1016/j.bspc.2021.
103338.
[139] B. Zhou, A. Lapedriza, J. Xiao, A. Torralba,
and A. Oliva. Learning Deep Features for
Scene Recognition using Places Database. In
Advances in Neural Information Processing
Systems, volume 27. Curran Associates, Inc.,
2014.
[140] O.ZlatovandB.Blankertz.Towardsphysiology-
informed data augmentation for EEG-based
BCIs, Mar. 2022. doi: 10.48550/arXiv.2203.
14392. arXiv: 2203.14392 [cs, eess].