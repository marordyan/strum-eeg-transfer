Comments and Controversies
Cross-validation failure: small sample sizes lead to large error bars
Ga¨el Varoquauxa,b,∗
aParietal project-team, INRIA Saclay-ˆıle de France, France
bCEA/Neurospin bˆat 145, 91191 Gif-Sur-Yvette, France
Abstract
Predictive models ground many state-of-the-art developments in statistical brain image analysis: decoding, MVPA,
searchlight, or extraction of biomarkers. The principled approach to establish their validity and usefulness is cross-
validation, testing prediction on unseen data. Here, I would like to raise awareness on error bars of cross-validation,
which are often underestimated. Simple experiments show that sample sizes of many neuroimaging studies inherently
lead to large error bars, eg ±10% for 100 samples. The standard error across folds strongly underestimates them.
These large error bars compromise the reliability of conclusions drawn with predictive models, such as biomarkers or
methods developments where, unlike with cognitive neuroimaging MVPA approaches, more samples cannot be acquired
by repeating the experiment across many subjects. Solutions to increase sample size must be investigated, tackling
possible increases in heterogeneity of the data.
Keywords: cross-validation; statistics; decoding; fMRI; model selection; MVPA; biomarkers
1. Introduction Here, I show with very simple analyses that the ob-
served errors of cross-validation are inherent to small
In the past 15 years, machine-learning methods have number of samples. I argue that they provide loopholes
pushed forward many brain-imaging problems: decod- that are exploited in the neuroimaging literature, proba-
ing the neural support of cognition (Haynes and Rees, bly unwittingly. The problems are particularly severe for
2006), information mapping (Kriegeskorte et al., 2006), methods development and inter-subject diagnostics stud-
predictionofindividualdifferences–behavioralorclinical– ies. Conversely, cognitiveneurosciencestudiesarelessim-
(Smith et al., 2015), rich encoding models (Nishimoto pacted, as they often have access to higher sample sizes
etal.,2011), principledreverseinferences(Poldracketal., using multiple trials per subjects and multiple subjects.
2009), etc. Replacing in-sample statistical testing by pre- These issues could undermine the potential of machine-
diction gives more power to fit rich models and complex learning methods in neuroimaging and the credibility of
data(Normanetal.,2006;VaroquauxandThirion,2014). relatedpublications. Igiverecommendationsonbestprac-
Thevalidityofthesemodelsisestablishedbytheirabil- tices and explore cost-effective avenues to ensure reliable
itytogeneralize: tomakeaccuratepredictionsaboutsome cross-validation results in neuroimaging.
properties of new data. They need to be tested on data The effects that I describe are related to the “power
independent from the data used to fit them. Technically, failure” of Button et al. (2013): lack of statistical power.
this test is done via cross-validation: the available data Inthespecificcaseoftestingpredictivemodels, theshort-
is split in two, a first part, the train set used to fit the coming of small samples are more stringent and inherent
model, and a second part, the test set used to test the as they are not offset with large effect sizes. My goals
model (Pereira et al., 2009; Varoquaux et al., 2017). here are to raise awareness that studies based on predic-
Cross-validation is thus central to statistical control of tive modeling require larger sample sizes than standard
thenumerousneuroimagingtechniquesrelyingonmachine statistical approaches.
learning: decoding, MVPA (multi-voxel pattern analy-
sis), searchlight, computer aided diagnostic, etc. Varo-
2. Results: cross-validation errors
quaux et al. (2017) conducted a review of cross-validation
techniqueswithanempiricalstudyonneuroimagingdata.
2.1. Distribution of errors in cross-validation
Theseexperimentsrevealedthatcross-validationmadeer-
Cross-validation strives to measure the generalization
rors in measuring prediction accuracy typically around
±10%. Such large error bars are worrying. power of a model: how well it will predict on new data.
To simplify the discussion, I will focus on balanced clas-
sification, predicting two categories of samples; prediction
∗Correspondingauthor accuracycanthenbemeasuredinpercentsandchanceisat
50%. Thecross-validationerroristhediscrepancybetween
Preprint submitted to NeuroImage June 26, 2017
7102
nuJ
32
]MQ.oib-q[
1v18570.6071:viXra

a.Neuroimaging data LLOOOO
fMRI ­21% +18%
within subject 30
~212 samples ­24% +13%
5500 sspplliittss,, 2200%% tteesstt
LOO
fMRI ­10% +10% 100
across subject
~241 samples ­10% +8%
50 splits, 20% test
LOO 200
MEG ­16% +14%
~199 samples
­13% +10%
300
50 splits, 20% test
­30% ­15% 0% +15% +30%
Estimation error on the prediction accuracy
1000 d.Kaggle competition
­15% +14% ­30% ­15% 0% +15% +30%
Estimation error on the prediction accuracy
­45% ­30% ­15% 0% +15% +30%
Difference between public and private scores
selpmas
elbaliava
fo
rebmuN
b.Simulations LLOOOO
­20% +18%
­19% +15%
5500 sspplliittss,, 2200%% tteesstt 30
LOO
­10% +10%
­10% +8%
50 splits, 20% test 100
LOO
­7% +7%
­7% +5%
50 splits, 20% test 200
LOO
­6% +6%
­5% +4%
50 splits, 20% test 300
LOO
­3% +3%
­3% +2%
50 splits, 20% test 1000
­20% ­10% 0% +10% +20%
Distribution of errors under a binomial law
selpmas
elbaliava
fo
rebmuN
c.Binomial law
­15% +12%
­7% +7%
­5% +5%
­4% +4%
­2% +2%
Figure 1: Cross-validation errors. a – Distribution of errors between the prediction accuracy as assessed via cross-validation (average
acrossfolds)andasmeasuredonalargeindependenttestsetfordifferenttypesofneuroimagingdata. ResultsfromVaroquauxetal.(2017)
(seeAppendix B)b–Distributionoferrorsbetweenthepredictionaccuracyasassessedviacross-validationondataofvarioussamplesizes
andasmeasuredon10000newdatapointsforsimplesimulations(seeAppendix C).c–Distributionoferrorsasgivenbyabinomiallaw:
differencebetweentheobservedpredictionerrorandthepopulationvalueoftheerror,p=75%,fordifferentsamplesizes. d–Discrepancies
between private and public score. Each dot represents the difference between the accuracy of a method on the public test data and on
the private one. The scoresare retrieved fromwww.kaggle.com/c/mlsp-2014-mri, in which 144subjects were used total, 86for trainingthe
predictive model, 30 for the public test set, and 28 for the private test set. The bar and whiskers indicate the median and the 5th and 95th
percentile. Measures on cross-validation (a and b) are reported for two reasonable choices of cross-validation strategy: leave one out (leave
onerunoutorleaveonesubjectoutindatawithmultiplerunsorsubjects),or50-timesrepeatedsplittingof20%ofthedata.
the prediction accuracy measured by cross-validation and etal.(2017). Toreflectcommonpracticeinneuroimaging,
the expected accuracy on new data. Ihaveinspectedtheresultsofapublicpredictionchallenge
(Silva et al., 2014) on the Kaggle website1. The compe-
Previous results: cross-validation on brain images.
tition –predicting Schizophrenia diagnosis from functional
Varoquaux et al. (2017) used a nested cross-validation on
and structural MRI– reports two accuracy measures esti-
neuroimaging data to measure this discrepancy: we split
mated on a public (n = 30) and a private (n = 28) test
the data multiple times and compared errors (see Ap-
set.
pendix B). The strength of such an experiment is that
The accuracy scores reported on the public and the
it is applied on actual neuroimaging data, mimicking us-
privatetestsetshowalargedifference. Figure1dsumma-
agebypractitioners. Itsweaknessisthatthemodels’true
rizesthesedifferences. Computingconfidenceboundsfrom
generalization accuracy is not known and must be esti-
these discrepancies gives errors on the order of ±15%. As
mated.
neither the public nor the private test set is a gold stan-
Figure1asummarizestheresultingcross-validationer-
dard, it is reasonable to assume that errors are shared be-
rors, show a similar behavior across different reasonable
tween the two scores, and thus the actual margin of error
choices of cross-validation strategy: the common leave-
on a single measurement is smaller by a factor of two.
one-run-out,andtherecommendedrandomsplittingstrat-
egy (Varoquaux et al., 2017). The 5th and 95th per- Simple simulations also display large error bars.
centile of the distribution of errors are of particular in- To understand better the origin of these discrepancies, I
terest as they correspond to the commonly accepted .05 used simple simulations: fitting a linear SVM on a two-
threshold on p-values. The results show that these confi- classdataset,samplesdrawni.i.d. fromtwoGaussiandis-
dence bounds extends at least 10% both ways, regardless tributions with a separation tuned such that the classifier
ofthecross-validationstrategyused. Itimpliesthat,when achieves 75% accuracy. I then compare the prediction ac-
computing a given cross-validated accuracy, there is a 5% curacymeasurebycross-validationonthesedatawiththe
chance that it is 10% above the true generalization accu- accuracy that the classifier achieved on a large amount
racy, and a 5% chance this it is 10% below. (10000) new samples drawn from the same distribution.
Spread out predictions in a public challenge. There
could be something unusual in the settings of Varoquaux 1https://www.kaggle.com/c/mlsp-2014-mri
2

seiduts fo rebmuN
An important benefit of this experiment is that it shows Woo2017: Woo2017:
|                |     |         |     |                  |     |         |        |     |     |     |     | Autism   |     | Alzheimer's       |     |
| -------------- | --- | ------- | --- | ---------------- | --- | ------- | ------ | --- | --- | --- | --- | -------- | --- | ----------------- | --- |
| the difference |     | between | the | cross-validation |     | measure | of the |     |     |     |     |          |     |                   |     |
|                |     |         |     |                  |     |         |        |     |     |     |     | Woo2017: |     | Arbabshirani2017: |     |
classifier’s accuracy, and the true generalization accuracy. Depression Schizophrenia
|     |     |     |     |     |     |     |     |     |     |     |     | Woo2017: |     | Arbabshirani2017: |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----------------- | --- |
Figure 1b shows the resulting distribution of errors on Psychosis Alzheimer's
the prediction accuracy estimated by cross validation for Brown2017:
Connectome learning
different size of the data available. For 100 samples, these 5 5 0 0 0 0 0 0 0
|     |     |     |     |     |     |     |     |   5 o  1 | 1 o  5 | 5 0 1 5 | 5 5 0 | 0 0 5 0 | 0 0 0 | Wolfer2015: |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ------- | ----- | ------- | ----- | ----------- | --- |
experiments reproduces well the errors observed on neu- t t   o  1 o  5 1 1 5 5 psychiatric diagnostic
|     |     |     |     |     |     |     |     |     |     | t   | t   |   o   | o   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
roimaging data (Figure 1a and 1d). Both leave one out t t Pubmed search
|          |               |     |                  |     |     |            |         | Number of available samples |     |     |     |     |     | "fmri decoding" |     |
| -------- | ------------- | --- | ---------------- | --- | --- | ---------- | ------- | --------------------------- | --- | --- | --- | --- | --- | --------------- | --- |
| and more | sophisticated |     | cross-validation |     |     | strategies | display |                             |     |     |     |     |     |                 |     |
largeerrorbars2. Asthesamplesizeofthesimulateddata Figure 2: Sample sizes in neuroimaging studies A stacked
|               |           |       |          |           |        |     |              | histogram  | compounding     |        | sample   | sizes           | from         | multiple | sources: the  |
| ------------- | --------- | ----- | -------- | --------- | ------ | --- | ------------ | ---------- | --------------- | ------ | -------- | --------------- | ------------ | -------- | ------------- |
| goes up,      | the error | bars  | narrow   | markedly. |        |     |              |            |                 |        |          |                 |              |          |               |
|               |           |       |          |           |        |     |              | Woo et al. | (2017)          | review | paper,   | differentiating |              | Autism,  | Depression,   |
|               |           |       |          |           |        |     |              | Pyschosis, | and Alzheimer’s |        | studies, | the             | Arbabshirani |          | et al. (2017) |
| Intrinsically |           | large | sampling |           | noise. | The | data clearly |            |                 |        |          |                 |              |          |               |
reviewpaper,differentiatingSchizophreniaandAlzheimer’sstudies,
shows that the accuracy of predictive models is not well theBrownandHamarneh(2016)reviewonpredictionfromconnec-
tomes,andtheWolfersetal.(2015)reviewonpredictionforpsychi-
| measured     | in                                       | neuroimaging. |     | The    | small | sample | sizes en- |                   |     |                                           |         |       |         |             |        |
| ------------ | ---------------------------------------- | ------------- | --- | ------ | ----- | ------ | --------- | ----------------- | --- | ----------------------------------------- | ------- | ----- | ------- | ----------- | ------ |
|              |                                          |               |     |        |       |        |           | atric disorders,  | as  | well as                                   | the 100 | first | answers | to a pubmed | search |
| countered    | in                                       | neuroimaging  |     | indeed | make  | this   | task very |                   |     |                                           |         |       |         |             |        |
|              |                                          |               |     |        |       |        |           | on”fmridecoding”. |     | Thetotalhistogramcomprises642studies,with |         |       |         |             |        |
| challenging: | asIshowbelow,eveninidealsituations,there |               |     |        |       |        |           |                   |     |                                           |         |       |         |             |        |
amediannumberofsamplesof89.
is a large sampling noise in the measure. NotethatIdidnotconsidergroupsoflessthan25studies,andhence
The typical sample size of neuroimaging studies is less didnot breakup into pathologies theBrownandHamarneh (2016)
andWolfersetal.(2015)reviews.
| than 100          | observations |             | given        | to the        | classifier, | trials  | or sub-    |                  |          |          |           |            |             |                  |           |
| ----------------- | ------------ | ----------- | ------------ | ------------- | ----------- | ------- | ---------- | ---------------- | -------- | -------- | --------- | ---------- | ----------- | ---------------- | --------- |
| jects depending   |              | on          | the settings | (Figure       |             | 2). The | simplest   |                  |          |          |           |            |             |                  |           |
| model             | for the      | observed    | prediction   |               | errors      | is that | of toss-   |                  |          |          |           |            |             |                  |           |
|                   |              |             |              |               |             |         |            | 2.2. Small       | sample   | sizes    | undermine |            | statistical |                  | control   |
| ing a coin        | 100          | times       | with         | a probability |             | p of    | success at |                  |          |          |           |            |             |                  |           |
|                   |              |             |              |               |             |         |            | Underestimated   |          | errors.  |           | Not        | only        | are the          | errors of |
| each toss.        | The          | probability |              | p corresponds |             | to the  | accuracy   |                  |          |          |           |            |             |                  |           |
|                   |              |             |              |               |             |         |            | cross-validation |          | large,   | but       | it is also | easy        | to underestimate |           |
| of the classifier |              | that        | we are       | trying        | to measure. |         | The dis-   |                  |          |          |           |            |             |                  |           |
|                   |              |             |              |               |             |         |            | them, as         | when     | using    | as a null | the        | binomial    | distribution.    |           |
| tribution         | of number    |             | of successes |               | is then     | given   | by a bi-   |                  |          |          |           |            |             |                  |           |
|                   |              |             |              |               |             |         |            | The              | simplest | approach |           | to put     | error       | bars             | on cross- |
| nomial            | law (Pereira |             | and          | Botvinick,    | 2011;       | Stelzer | et al.,    |                  |          |          |           |            |             |                  |           |
validationresultsistolookatthedispersionofthepredic-
| 2013).           | With 100 | tosses,      | associated    |           | confidence |            | bounds lie  |                   |             |                                  |            |               |             |           |              |
| ---------------- | -------- | ------------ | ------------- | --------- | ---------- | ---------- | ----------- | ----------------- | ----------- | -------------------------------- | ---------- | ------------- | ----------- | --------- | ------------ |
|                  |          |              |               |           |            |            |             | tion accuracy     |             | across                           | the folds. | However       |             | as the    | predictions  |
| ±7% away         | from     | the          | true accuracy |           | p (see     | Figure     | 1c).        |                   |             |                                  |            |               |             |           |              |
|                  |          |              |               |           |            |            |             | are not           | independent |                                  | across     | folds,        | estimates   |           | of the vari- |
| This             | binomial | law          | is a          | best-case | scenario   | for        | errors on   |                   |             |                                  |            |               |             |           |              |
|                  |          |              |               |           |            |            |             | ance or           | related     | statistical                      | tests      | are           | optimistic  |           | (Bengio and  |
| the accuracy     |          | measure:     | observations  |           | are        | i.i.d.     | and there   |                   |             |                                  |            |               |             |           |              |
|                  |          |              |               |           |            |            |             | Grandvalet,2004). |             | Onthesimulateddata,formulasbased |            |               |             |           |              |
| is no additional |          | variability  |               | from      | training   | a decoder. | On          |                   |             |                                  |            |               |             |           |              |
|                  |          |              |               |           |            |            |             | on the            | standard    | error                            | to mean    | underestimate |             |           | confidence   |
| the opposite,    |          | neuroimaging |               | data      | is strife  | with       | correlation |                   |             |                                  |            |               |             |           |              |
|                  |          |              |               |           |            |            |             | bounds            | by a factor | of                               | 0.7 in     | the best      | case        | (Appendix | D).          |
| across samples   |          | and          | confounding   |           | effects,   | e.g. the   | temporal    |                   |             |                                  |            |               |             |           |              |
|                  |          |              |               |           |            |            |             | Permutation       |             | testing                          | gives      | good          | statistical |           | control on   |
structure of trials or samples drawn either from the same the prediction accuracy (Stelzer et al., 2013). Literature
| subject     | or different |         | subjects. | These  | reduce       |     | the statisti- |           |        |          |     |         |      |        |          |
| ----------- | ------------ | ------- | --------- | ------ | ------------ | --- | ------------- | --------- | ------ | -------- | --- | ------- | ---- | ------ | -------- |
|             |              |         |           |        |              |     |               | search on | Google | Scholar3 |     | suggest | that | around | a 30% of |
| cal degrees | of           | freedom | and       | create | an intrinsic |     | variance in   |           |        |          |     |         |      |        |          |
thepublicationsonMVPA(mostlysearchlight-basedanal-
| the prediction |         | accuracy        | (Saeb      | et   | al., 2017;       | Little | et al., |           |               |     |               |      |      |        |          |
| -------------- | ------- | --------------- | ---------- | ---- | ---------------- | ------ | ------- | --------- | ------------- | --- | ------------- | ---- | ---- | ------ | -------- |
|                |         |                 |            |      |                  |        |         | ysis) use | permutations, |     | but           | that | only | 15% of | the fMRI |
| 2017).         | This is | why             | we observe | that | cross-validation |        | has     |           |               |     |               |      |      |        |          |
|                |         |                 |            |      |                  |        |         | decoding  | studies       | use | permutations. |      |      |        |          |
| larger errors  |         | on neuroimaging |            | data | (Figure          | 1a)    | than on |           |               |     |               |      |      |        |          |
thesimulations(Figure1b)orwiththeidealbinomiallaw Vibration effects. Analytic pipelines come with vari-
(Figure 1c).
|             |     |     |          |      |       |           |      | ous methodological |        | choices |               | that are | hard | to settle  | a priori |
| ----------- | --- | --- | -------- | ---- | ----- | --------- | ---- | ------------------ | ------ | ------- | ------------- | -------- | ---- | ---------- | -------- |
|             |     |     |          |      |       |           |      | (Carp,             | 2012). | With a  | high-variance |          | test | statistic, | as cross |
| Simulations |     | and | a simple | null | model | therefore | show |                    |        |         |               |          |      |            |          |
validationonfewsamples,methodologicalchoicescanhave
| that the | error | bars | of cross-validation |     |     | observed | in neu- |           |        |     |             |     |        |           |      |
| -------- | ----- | ---- | ------------------- | --- | --- | -------- | ------- | --------- | ------ | --- | ----------- | --- | ------ | --------- | ---- |
|          |       |      |                     |     |     |          |         | a drastic | impact | on  | the outcome |     | of the | analysis. | This |
roimaging are perfectly expected given the sample sizes. is sometimes known as vibration, and the key quantity is
| Improvements |     | on cross-validation |     |     | such | as the | reusable |           |         |     |        |          |     |            |        |
| ------------ | --- | ------------------- | --- | --- | ---- | ------ | -------- | --------- | ------- | --- | ------ | -------- | --- | ---------- | ------ |
|              |     |                     |     |     |      |        |          | the ratio | between | the | effect | size and | the | variations | due to |
holdout (Dwork et al., 2015) cannot circumvent intrinsic analytical choices (Ioannidis, 2008). I explored vibration
| limitations | of  | small | samples | (see | Appendix | A). |     |              |          |         |        |         |            |       |            |
| ----------- | --- | ----- | ------- | ---- | -------- | --- | --- | ------------ | -------- | ------- | ------ | ------- | ---------- | ----- | ---------- |
|             |     |       |         |      |          |     |     | effects in   | decoding | using   | the    | face    | versus     | place | opposition |
|             |     |       |         |      |          |     |     | in the Haxby |          | et al.  | (2001) | data.   | I inverted | the   | labels to  |
|             |     |       |         |      |          |     |     | predict      | in one   | session | out    | of two, | to create  | a     | dataset in |
2Performing50repeatedsplitsof20%ofthedatayieldsslightly
| smaller error   | bars   | than          | leave one | out,            | and can | be significantly      | less     |                                  |     |     |     |     |                         |     |     |
| --------------- | ------ | ------------- | --------- | --------------- | ------- | --------------------- | -------- | -------------------------------- | --- | --- | --- | --- | ----------------------- | --- | --- |
| computationally |        | expensive     | for       | large datasets. |         | This cross-validation |          |                                  |     |     |     |     |                         |     |     |
|                 |        |               |           |                 |         |                       |          | 3Pubmeddoesnotdofull-textsearch. |     |     |     |     | OnGooglescholar,asearch |     |     |
| strategy        | should | be preferred, | but       | will            | not fix | the problem           | of large |                                  |     |     |     |     |                         |     |     |
for“fmridecoding”inthelast5yearsreturned15500results,while
errorbars.
|     |     |     |     |     |     |     |     | “fmridecodingpermutation”returned2380; |     |     |     |     | similarly,“fmrimvpa” |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | -------------------- | --- | --- |
return2360resultswhile“fmrimvpapermutation”return728.
3

4 first
4 last
6 first
6 last
all 12
30% 40% 50% 60% 70%
Cross­validation scores for different decoders
desu
snoisseS
Wolfer2015: Arbabshirani2017: Woo2017: Woo2017:
25% 39% Psychiatric diagnostic Alzheimer's Alzheimer's Depression 100%
n~72
40% 71%
75%
n~72
38% 57% p=.05 p=.05 p=.05 p=.05
50%
n~108
47% 57% Brown2017: Arbabshirani2017: Woo2017:
Connectome learning Schizophrenia Psychosis
100%
n~108
44% 52%
n~216 75%
p=.05 p=.05 p=.05 p=.05
50% 301003001000 301003001000 301003001000 301003001000
Figure3: Different decoders on fMRI with permuted labels
Oneachlineshowsthedistributionofcross-validationscoresforava-
rietyofdecoders(SVCandlogisticregression,withdifferentamount
of univariate feature selection and spatial smoothing); a dot is the
cross-validation score for one choice of decoder. These are applied
tothefMRIdataofthefirstsubjectinHaxbyetal.(2001),discrim-
inatingfaceviewingandplaceviewing,butwithlabelsinvertedone
sessionoutoftwo;hencetheexpectedaccuracyischance: 50%.
which fMRI should not predict the experimental condi-
tion. On this data, I ran a variety of classic decoding
pipelines, namely SVM or logistic regression, optionally
withfeatureselectionof100, 200, 500, 1000, or2000vox-
els and smoothing at 2, 4, or 6mm. These are standard
choices, but they give altogether almost 50 different re-
lated decoding pipelines. I applied all these pipelines to
various subsets of the data: the full 12 sessions, the 6 first
or 6 last, or the 4 first or 4 last sessions.
Figure 3 shows the cross-validation scores obtained
with the various pipelines. The expected prediction score
is 50%, chance. When using all 12 sessions, the observed
scores group well around 50%, with excursions ranging
from 44% to 52%. However, when using less data the ex-
cursions are much more pronounced, going up to 57% for
6 sessions and 71% for 4 sessions. In addition, the mean
observed score varies notably across subsets of the data.
Such variation can be explained by nonstationarities, e.g.
fluctuation of attention of the subject, or sampling noise
discussed above: the observations are very correlated and
thus n ∼ 100 may not represent well the faces and places
conditions.
3. Implications for neuroimaging
3.1. An open door to overfit and confirmation bias
The large error bars are worrying, whether it is for
methods development of predictive models or their use to
study the brain and the mind. Indeed, a large variance of
results combined with publication incentives weaken sci-
entific progress (Ioannidis, 2005).
With conventional statistical hypothesis testing, the
danger of vibration effects is well recognized: arbitrary
degrees of freedom in the analysis explore the variance of
the results and, as a consequence, control on false posi-
tives is easily lost (Simmons et al., 2011). (Carp, 2012)
ycarucca
detropeR
Woo2017:
Autism
Study sample size
Figure4: ReportedaccuracyandsamplesizeThevariousplots
show reported prediction accuracy as a function of sample size for
thestudiesindifferentthereviewsconsideredinFigure2. Theblack
line and grey area represent the p=0.05 threshold with a binomial
nullmodel,which,asshownintheresultssection,islikelytobeop-
timistic. ThelinesareLowessfittothedata: robustnon-parametric
localregression.
has found that the variety of analytics choices is such in
fMRIthatalmosteverypublicationusesauniquepipeline.
In predictive models, arbitrary choices can leads to artifi-
cialimprovementsinthepredictionaccuracymeasuredby
cross-validation (see section 2.2 and Skocik et al. (2016)).
Thelargeristhevarianceofthemeasureoftheprediction
score, the larger are these effects. The improvements are
meaningless as they will not carry over to predicting on
new data. The danger is well known in machine learn-
ing, where it is known as overfit. The standard remedy is
to keep a large independent test set. However it is diffi-
cult in neuroimaging, where data acquisition is costly. To
mitigate such intrinsic problems, clinical trials often use
blindanalysiswherepartofthelabelsareunknowntothe
statistician.
Scientificpublishingmakesthingsworse: theliterature
actsasafilterasonlystudiesthatreportsignificanteffects
are published. Such selective reporting can further under-
mine control of the fraction of false detections in a body
of literature (Rosenthal, 1979). It also tends to inflate the
reportedeffectsize(Vuletal.,2009). Anadditionaladan-
gerouseffectoflargevarianceisthatitenablesandjustifies
confirmation bias in publications: investigators or review-
ersaremorelikelytopublishresultsthatareinagreement
with their theory. Analysis of the literature suggests that
publications are indeed too often on the edge of signifi-
cance (Szucs and Ioannidis, 2016) and are vastly biased
by selection according to the prevailing opinions (Ioanni-
dis, 2008).
The combination of large variance and the filter effect
of publications could explain why the prediction accuracy
reported in publication often decreases as sample sizes in-
crease. Indeed, inFigure4Iplotanmetaanalysisuniting
the results discussed in several review papers. Each of
thesereviewselectavarietyofstudiesondifferentcriteria
such as methodology used or pathology studied. Overall,
4

the typical prediction accuracy reported in studies with as well as habituation effects to the paradigm. Scanning
small samples size is larger that reported in studies with many subjects may entails operational budgets beyond
many samples4. Homogeneity of the population and the that typical of a neuroimaging grant. Nevertheless, there
imagingdataishardertocontrolonlargercohorts. Hence are a variety of solutions feasible without major changes
uncontrolled heterogeneity might explain such a decrease. in the field.
However, very few studies have compared large heteroge-
Data sharing and pooling, despite heterogeneity.
neous cohorts to smaller well-controlled group with the
Reusingshareddataacrossinvestigatorscanincreasesam-
same analytic pipeline. A notable exception, Abraham
ple sizes while keeping bounds on data-acquisition costs
et al. (2017), finds that pooling data across sites leads to
(PoldrackandGorgolewski,2014). Platformstoshareneu-
better predictive biomarkers of Autism, although this is a
roimaging data are rapidly growing, as with OpenfMRI
highly-heterogeneous spectrum disorder.
(Poldrack et al., 2013) that now hosts 63 studies com-
prising 2200 subjects, or Neurovault (Gorgolewski et al.,
3.2. Cross-validation is nonetheless a crucial tool
2015) with 26000 brain maps in 1100 collection. Such
Cross-validationisnotasilverbullet. However,itisthe
sharing is easiest with harmonized protocols and conven-
best tool available, because it is the only non-parametric
tions. Yet, outside of concerted efforts, there is a mas-
method to test for model generalization. Bayesian ap-
sive amount of data potentially available: around 30000
proaches such as Bayesian model selection or Bayesian
studies using fMRI are published each year5, many with
model averaging rely on model evidence to test or select
new data. They answer a wide variety of different ques-
models (Penny et al., 2007, chap.35). However, they are
tions; still they have some overlap. This overlap provides
strongly parametric: the statistical control or the useful-
opportunity for reuse, increasing sample size. For cogni-
ness of this test collapses if the modeling assumptions are
tive neuroimaging, joint analysis is challenging due to the
wrong. Additionally,theseapproachesdonotmeasurethe
high specificity of cognitive questions studied. However,
ability of the model to predict on new data.
thesuccessofmeta-analysisinfMRIsuggeststhatpooling
Testing for generalization is central to diagnostics or
datacanbebeneficial, whetheritisbyassemblingasmall
prognosis applications, where prediction is indeed the
number of well-matched studies or over a wider coverage
question. It has also a broader importance as the abil-
of the literature (Laird et al., 2005; Costafreda, 2009). In
ity to generalize findings is central to scientific investiga-
a remarkable example of predictive models using pooled
tions. Research in psychology and neuroscience has fo-
data, Wager et al. (2013) were able to combine multiple
cused on explaining data, to seek causal mechanisms us-
pain studies to extract a neural signature specific to phys-
ingtightly-controlledexperiments,eg basedonrandomiza-
ical pain, discriminating it from social pain or warmth.
tion. However,toostrongafocusonwell-controlledexpla-
Topoolstudiesofbrainpathologies,itisofteneasierto
nationmaylimitthegeneralityoftheresults(Yarkoniand
define acommon covariateto predict acrosssubjects, typ-
Westfall, 2016). The essential aspect of cross-validation is
ically a diagnostic status. However, studies of the same
that it tests a model on observations independent from
pathology can differ in their inclusion criteria, introduc-
the data that was used to fit the model. This is the
ing heterogeneity that confounds predictions or interpre-
only assumption-free way to bound model complexity. In-
tations. Heterogeneity may be a challenge to the clini-
deed, more complex model will always fit the data better.
cal relevance of studies on heterogeneous groups, as many
There are statistical procedures to set model complexity,
neuro-psychiatric diseases are spectrum disorders that are
such as Bayesian information criterion (BIC) and the re-
likely composed of several forms of the disease. However,
lated Akaike information criterion (AIC) and minimum
biomarkers that are too specific to a certain site or a cer-
descriptor length (MDL). However, they rely on model-
tain cohort have reduced clinical value (Woo et al., 2017).
ingassumptionsuchasdatadistribution, independenceof
There are many documented successes of prediction from
the observations, and need much more observations than
heterogeneous brain imaging data. For anatomical mark-
model parameters (Hastie et al., 2009, sec.7.5).
ers of aging, Ziegler et al. (2014) show that using data
from many scanners enables to generalize to new scanner.
3.3. Looking forward: some recommendations
Yahata et al. and Abraham et al. (2017) show that, for a
Predictive models can extract richer and finer infor- disorder as heterogeneous as Autism, predicting diagnos-
mation from the complex data provided by brain imag- tic status across sites was possible. Moreover, Abraham
ing. However, best practices need to be adapted to en- etal.(2017)andDansereauetal.(2017)showthatwitha
sure enough statistical power to test these models. While large number of sites, prediction across sites performed as
larger datasets are certainly desirable, they are difficult well as prediction across subjects in the same site. Cross-
and costly to acquire. At the subject level, data accumu- validation on heterogeneous data requires some care, as
lation is limited by fatigue of the subject in the scanner prediction may be driven by a confounding covariate (Lit-
tleetal.,2017). Forinstance,whenpredictingwithseveral
4Depressionstudies,asreportedbyWooetal.(2017)donotshow
thisdecrease,howevernoneofthesehavealargesample. 5AsestimatedfromaPubMedsearchonfMRI.
5

|          |              |     |           |     |       |          |        |     | Sample | size |     | 30  | 100 | 300 | 1000 |
| -------- | ------------ | --- | --------- | --- | ----- | -------- | ------ | --- | ------ | ---- | --- | --- | --- | --- | ---- |
| sessions | per subject, |     | care must | be  | taken | to avoid | having |     |        |      |     |     |     |     |      |
different sessions of the same subject in the train and test Confidence bounds ±15% ±10% ±6% ±3%
| set, to prevent |     | subject-identification |     |     | to  | be driving | predic- |     |     |     |     |     |     |     |     |
| --------------- | --- | ---------------------- | --- | --- | --- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Table1: Confidenceboundstobeexpectedforabinaryclas-
| tion (Saeb | et al., | 2017). |     |     |     |     |     |             |             |     |             |     |                 |     |              |
| ---------- | ------- | ------ | --- | --- | --- | --- | --- | ----------- | ----------- | --- | ----------- | --- | --------------- | --- | ------------ |
|            |         |        |     |     |     |     |     | sification, | summarizing |     | experiments |     | and simulations |     | in Figure 1. |
Actualconfidenceboundsmaybesignificantlylargerinadversesit-
| Paradigms | facilitating |     | larger |     | data. | Someexperimen- |     |     |     |     |     |     |     |     |     |
| --------- | ------------ | --- | ------ | --- | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
uationssuchaswithcorrelatedobservationsorveryunstableclassi-
| tal paradigms |          | make          | it easier  | to   | accumulate |                | data, of-  | fiers.      |              |     |                  |           |     |            |          |
| ------------- | -------- | ------------- | ---------- | ---- | ---------- | -------------- | ---------- | ----------- | ------------ | --- | ---------------- | --------- | --- | ---------- | -------- |
| ten to        | the cost | relinquishing |            | fine | control    | on             | cognition. |             |              |     |                  |           |     |            |          |
| For instance, |          | to study      | cognition, |      | standard   | localizer-type |            |             |              |     |                  |           |     |            |          |
|               |          |               |            |      |            |                |            | them across | several      |     | datasets         | (Demˇsar, |     | 2006).     | With the |
| paradigms     | (Saxe    | et al.,       | 2006)      | can  | easily     | be shared      | across     |             |              |     |                  |           |     |            |          |
|               |          |               |            |      |            |                |            | sample      | size typical |     | of neuroimaging, |           | I   | personally | believe  |
manyacquisitions,leadingtolargedatabases(Pineletal.,
|     |     |     |     |     |     |     |     | that this | is the | only | sound | way | of doing | methods | devel- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ---- | ----- | --- | -------- | ------- | ------ |
2007). Naturalisticstimulienablesfasterpresentationsfor
|                                        |             |            |           |                         |           |               |              | opment. | As most   | methods |           | researchers, |      | I have  | not always |
| -------------------------------------- | ----------- | ---------- | --------- | ----------------------- | --------- | ------------- | ------------ | ------- | --------- | ------- | --------- | ------------ | ---- | ------- | ---------- |
| longertimeswithoutfatigueofthesubject. |             |            |           |                         |           | Thereforethey |              |         |           |         |           |              |      |         |            |
|                                        |             |            |           |                         |           |               |              | worked  | like this | in      | the past, | and          | some | of the  | promising  |
| can be used                            | to          | accumulate |           | subjects’               | responses |               | for rich de- |         |           |         |           |              |      |         |            |
|                                        |             |            |           |                         |           |               |              | results | that we   | have    | published | have         | not  | carried | over6.     |
| codingstudies(Kayetal.,2008).          |             |            |           | Tostudyinter-individual |           |               |              |         |           |         |           |              |      |         |            |
| differences,                           | acquisition |            | protocols |                         | that are  | comparatively |              |         |           |         |           |              |      |         |            |
universal and easy to acquire lead to large sample sizes. 4. Conclusion: improving predictive neuroimaging
| For instance | there | are | more | standard | T1  | maps | available |     |     |     |     |     |     |     |     |
| ------------ | ----- | --- | ---- | -------- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
than myelin maps. In functional imaging, resting-state With predictive models even more than with standard
|     |     |     |     |     |     |     |     | statisticssmallsamplesizesundermineaccuratetests. |     |     |     |     |     |     | The |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
fMRIacquisitionareapromisingsourceofverylargedata,
|              |             |     |         |     |         |       |          | problem | is inherent |     | to the | discriminant |     | nature | of the test, |
| ------------ | ----------- | --- | ------- | --- | ------- | ----- | -------- | ------- | ----------- | --- | ------ | ------------ | --- | ------ | ------------ |
| via post-hoc | aggregation |     | (Biswal |     | et al., | 2010; | Thompson |         |             |     |        |              |     |        |              |
et al., 2014; Di Martino et al., 2014) or large concerted measuringonlyasuccessorfailureperobservations. Esti-
|                 |     |         |       |           |     |             |     | mates | of variance | across | cross-validation |     |     | folds | give a false |
| --------------- | --- | ------- | ----- | --------- | --- | ----------- | --- | ----- | ----------- | ------ | ---------------- | --- | --- | ----- | ------------ |
| efforts (Miller |     | et al., | 2016; | Van Essen | et  | al., 2013). |     |       |             |        |                  |     |     |       |              |
senseofsecurityastheystronglyunderestimateserrorson
Cognitive neuroimaging results: at the group level. the prediction accuracy: folds are far from independent.
Rather,toavoidtheillusionofbiomarkersthatdonotgen-
| In cognitive | neuroimaging, |     |     | multi-voxel |     | pattern | analysis |     |     |     |     |     |     |     |     |
| ------------ | ------------- | --- | --- | ----------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
(MVPA) generally performs cross-validation across trials eralizeoroverly-optimisticmethodsdevelopment,ballpark
in the same subject. The number of trials cannot always estimatesofconfidenceboundssummarizedinTable1may
be easily extended, due to habituation effects or limited bemoreuseful. Atypicalsamplesizeinneuroimaging,100
time in the scanner. A more promising avenue to increase observations, leads to ±10% errors in prediction accuracy.
|        |         |            |     |             |     |          |          | Cognitive | neuroscience |     | MVPA | studies |     | often control | these |
| ------ | ------- | ---------- | --- | ----------- | --- | -------- | -------- | --------- | ------------ | --- | ---- | ------- | --- | ------------- | ----- |
| sample | size is | to exploit | the | replication |     | of these | decoding |           |              |     |      |         |     |               |       |
results across subjects. As there is significant variabil- errors by performing a group-level statistical analysis.
ity in cognitive strategy or performance across subjects, Exploring arbitrary choices in analytic pipelines eas-
pooling across subjects raises concerns. Yet, conclusions ily creates improvements in measured prediction accu-
should be drawn from the group, and not at the subject racy that will not generalize to new data. Such effect is
|              |     |       |        |      |       |               |     | a major | impediment |     | for | methods | development |     | as it be- |
| ------------ | --- | ----- | ------ | ---- | ----- | ------------- | --- | ------- | ---------- | --- | --- | ------- | ----------- | --- | --------- |
| level, where | the | small | sample | size | tends | to compromise |     |         |            |     |     |         |             |     |           |
cross-validation. There are several approaches. First, as comes challenging to ensure that improvements observed
outlinedinStelzeretal.(2013)evenwhencross-validation aremeaningful. Duetothespecificitiesofdatasets,proto-
|     |     |     |     |     |     |     |     | cols, or | pathologies, |     | there | cannot | be a | one-size-fits-all | op- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | --- | ----- | ------ | ---- | ----------------- | --- |
isperformedatthesubjectlevel,testingforsignificanceof
predictions can be done at the group level. This approach timal method for predictive modeling. However, to limit
is used by a good fraction of the MVPA studies. Another the variety of analytics pipelines, we, methods developers,
option is to predict across subjects. This requires fine- mustprovidegeneralrecommendationsvalidatedonmany
| grain matching |     | of subjects’ |     | anatomy | and | function, | yet it | datasets. |     |     |     |     |     |     |     |
| -------------- | --- | ------------ | --- | ------- | --- | --------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
Withsmallsamplesizes,researchwithpredictivemod-
| bears the | promise | of  | more | general | representations |     | of cog- |     |     |     |     |     |     |     |     |
| --------- | ------- | --- | ---- | ------- | --------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
nition (Haxby et al., 2011). els is performed blindfolded. The problem is neither new
|            |         |     |     |          |          |     |           | norspecifictoneuroimaging. |        |      |       | Ingenomics,Braga-Netoand |                  |     |           |
| ---------- | ------- | --- | --- | -------- | -------- | --- | --------- | -------------------------- | ------ | ---- | ----- | ------------------------ | ---------------- | --- | --------- |
| Evaluating | methods |     | on  | multiple | studies. |     | For meth- |                            |        |      |       |                          |                  |     |           |
|            |         |     |     |          |          |     |           | Dougherty                  | (2004) | have | asked | “Is                      | cross-validation |     | valid for |
ods development, the vibration effects observed on Fig- small-sample microarray classification?”. In neuroimag-
ure 3 are very troublesome. Indeed, the empirical work in ing, it is magnified by the intrinsic difficulty of acquiring
methods development often amounts to trying out multi- large datasets. The problem will not be fixed by better
ple approaches and publishing the one that works best. It classifiersorcross-validationapproaches. Solutionswilllie
leadsnaturallytooverfitifthedataarenotlargeenoughto
|                                         |        |        |             |     |            |            |          | in approaches |     | using | larger | samples | sizes | or preregistered |     |
| --------------------------------------- | ------ | ------ | ----------- | --- | ---------- | ---------- | -------- | ------------- | --- | ----- | ------ | ------- | ----- | ---------------- | --- |
| guarantee                               | errors | on the | measurement |     | prediction |            | accuracy |               |     |       |        |         |       |                  |     |
| smallerthanthedifferencebetweenmethods. |        |        |             |     |            | AsIoutline |          |               |     |       |        |         |       |                  |     |
6Asanexample,wewerenotabletoreproducethebenefitsofthe
| insection2.2andAppendix |     |          |         | D),itishardtomeasurethese |     |     |          |          |           |           |     |            |          |           |        |
| ----------------------- | --- | -------- | ------- | ------------------------- | --- | --- | -------- | -------- | --------- | --------- | --- | ---------- | -------- | --------- | ------ |
|                         |     |          |         |                           |     |     |          | specific | algorithm | in Michel | et  | al. (2012) | on other | datasets, | though |
| error bars              | and | they are | usually | underestimated.           |     |     | The best |          |           |           |     |            |          |           |        |
welatervalidatedsomeofthecoreideas–voxelclustering–onmany
| way to | compare | approaches |     | without | loophole |     | is to test |     |     |     |     |     |     |     |     |
| ------ | ------- | ---------- | --- | ------- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
otherdatasetsVaroquauxetal.(2012);Hoyos-Idroboetal.(2016).
6

analyses. Overall, exploring larger datasets is a promis- Hastie,T.,Tibshirani,R.,Friedman,J.,2009. Theelementsofsta-
ing future for neuroimaging (Poldrack et al., 2017). Their tisticallearning. Springer.
richness is best captured by multivariate models (Miller Haxby, J.V., Gobbini, I.M., Furey, M.L., et al., 2001. Distributed
|                |     |            |              |     |      |             | and overlapping |     | representations  |     | of faces | and | objects | in ventral |
| -------------- | --- | ---------- | ------------ | --- | ---- | ----------- | --------------- | --- | ---------------- | --- | -------- | --- | ------- | ---------- |
| et al., 2016). | For | predictive | applications |     | such | as biomark- |                 |     |                  |     |          |     |         |            |
|                |     |            |              |     |      |             | temporalcortex. |     | Science293,2425. |     |          |     |         |            |
ers,largerdatasetsleadtobetterpredictiononhardprob- Haxby,J.V.,Guntupalli,J.S.,Connolly,A.C.,Halchenko,Y.O.,Con-
|            |     |          |              |              |     |     | roy, B.R., | Gobbini, | M.I., | Hanke, | M., | Ramadge, | P.J., | 2011. A |
| ---------- | --- | -------- | ------------ | ------------ | --- | --- | ---------- | -------- | ----- | ------ | --- | -------- | ----- | ------- |
| lems, even | in  | the face | of increased | variability. |     |     |            |          |       |        |     |          |       |         |
common,high-dimensionalmodeloftherepresentationalspacein
|     |     |     |     |     |     |     | humanventraltemporalcortex. |     |     |     | Neuron72,404–416. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | ----------------- | --- | --- | --- |
Acknowledgments
|     |     |     |     |     |     |     | Haynes, J.D., | Rees, | G., 2006. | Decoding |     | mental | states | from brain |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | --------- | -------- | --- | ------ | ------ | ---------- |
Computing resources were provided by the NiConnect activityinhumans. Nat.Rev.Neurosci.7,523.
|          |                   |       |        |             |                  |             | Hoyos-Idrobo, | A.,           | Varoquaux,    | G.,      | Kahn,   | J., Thirion,    | B.,              | 2016. Re-   |
| -------- | ----------------- | ----- | ------ | ----------- | ---------------- | ----------- | ------------- | ------------- | ------------- | -------- | ------- | --------------- | ---------------- | ----------- |
| project  | (ANR-11-BINF-0004 |       |        | NiConnect). | I                | am grateful |               |               |               |          |         |                 |                  |             |
|          |                   |       |        |             |                  |             | cursive       | nearest       | agglomeration |          | (rena): | fast clustering |                  | for approx- |
| to Aaron | Schurger,         | Steve | Smith, | and         | Russell Poldrack | for         |               |               |               |          |         |                 |                  |             |
|          |                   |       |        |             |                  |             | imation       | of structured |               | signals. | arXiv   | preprint        | arXiv:1609.04608 |             |
.
| feedback | on the | manuscript. |     | I would | also like | to thank |     |     |     |     |     |     |     |     |
| -------- | ------ | ----------- | --- | ------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Ioannidis,J.P.,2005.Whymostpublishedresearchfindingsarefalse.
| Alexandra | Elbakyan |     | for help | with | the literature | review, |     |     |     |     |     |     |     |     |
| --------- | -------- | --- | -------- | ---- | -------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
PLosmed2,e124.
| as well as | Colin | Brown | and Choong-Wan |     | Woo | for sharing |            |       |           |      |            |      |              |     |
| ---------- | ----- | ----- | -------------- | --- | --- | ----------- | ---------- | ----- | --------- | ---- | ---------- | ---- | ------------ | --- |
|            |       |       |                |     |     |             | Ioannidis, | J.P., | 2008. Why | most | discovered | true | associations | are |
data of their review papers. inflated. Epidemiology19,640–648.
|            |     |     |     |     |     |     | Kay, K.N.,    | Naselaris, | T.,     | Prenger,        | R.J.,       | Gallant,  | J.L.,  | 2008. Iden-  |
| ---------- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | ------- | --------------- | ----------- | --------- | ------ | ------------ |
|            |     |     |     |     |     |     | tifying       | natural    | images  | from human      | brain       | activity. |        | Nature 452,  |
| References |     |     |     |     |     |     | 352–355.      |            |         |                 |             |           |        |              |
|            |     |     |     |     |     |     | Kriegeskorte, | N.,        | Goebel, | R., Bandettini, |             | P., 2006. |        | Information- |
|            |     |     |     |     |     |     | based         | functional | brain   | mapping.        | Proceedings |           | of the | National     |
Abraham,A.,Milham,M.P.,DiMartino,A.,Craddock,R.C.,Sama-
AcademyofSciencesoftheUnitedStatesofAmerica103,3863.
| ras,D., | Thirion,B., | Varoquaux,G., |     | 2017. | Derivingreproducible |     |     |     |     |     |     |     |     |     |
| ------- | ----------- | ------------- | --- | ----- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Laird,A.R.,Fox,P.M.,Price,C.J.,Glahn,D.C.,Uecker,A.M.,Lan-
| biomarkers | from                   | multi-site | resting-state |     | data: An | autism-based |                                                        |     |     |     |     |     |     |     |
| ---------- | ---------------------- | ---------- | ------------- | --- | -------- | ------------ | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|            |                        |            |               |     |          |              | caster,J.L.,Turkeltaub,P.E.,Kochunov,P.,Fox,P.T.,2005. |     |     |     |     |     |     | Ale |
| example.   | NeuroImage147,736–745. |            |               |     |          |              |                                                        |     |     |     |     |     |     |     |
Arbabshirani, M.R., Plis, S., Sui, J., Calhoun, V.D., 2017. Single meta-analysis: Controllingthefalsediscoveryrateandperforming
subject prediction of brain disorders in neuroimaging: Promises statisticalcontrasts. Humanbrainmapping25,155–164.
andpitfalls. NeuroImage145,137–165. Little, M.A., Varoquaux, G., Saeb, S., Lonini, L., Jayaraman, A.,
Arlot,S.,Celisse,A.,2010. Asurveyofcross-validationprocedures Mohr, D., Kording, K.P., 2017. Using and understanding cross-
formodelselection. Statisticssurveys4,40. validationstrategies.perspectivesonSaebetal. GigaScience,in
| Bengio, Y., | Grandvalet, |                   | Y., 2004. | No unbiased | estimator  | of the   | press.      |           |     |            |     |           |     |              |
| ----------- | ----------- | ----------------- | --------- | ----------- | ---------- | -------- | ----------- | --------- | --- | ---------- | --- | --------- | --- | ------------ |
|             |             |                   |           |             |            |          | Michel, V., | Gramfort, | A., | Varoquaux, |     | G., Eger, | E., | Keribin, C., |
| variance    | of k-fold   | cross-validation. |           | Journal     | of machine | learning |             |           |     |            |     |           |     |              |
Thirion,B.,2012.Asupervisedclusteringapproachforfmri-based
research5,1089.
|             |         |     |          |        |            |                | inferenceofbrainstates. |     |     | PatternRecognition45,2041–2049. |     |     |     |     |
| ----------- | ------- | --- | -------- | ------ | ---------- | -------------- | ----------------------- | --- | --- | ------------------------------- | --- | --- | --- | --- |
| Biswal, B., | Mennes, | M., | Zuo, X., | Gohel, | S., Kelly, | C., Smith, S., |                         |     |     |                                 |     |     |     |     |
Beckmann, C., et al., 2010. Toward discovery science of human Miller, K.L., Alfaro-Almagro, F., Bangerter, N.K., Thomas, D.L.,
brainfunction. ProcNtlAcadSci107,4734. Yacoub,E.,Xu,J.,Bartsch,A.J.,Jbabdi,S.,Sotiropoulos,S.N.,
Braga-Neto, U.M., Dougherty, E.R., 2004. Is cross-validation valid Andersson,J.L.,etal.,2016. Multimodalpopulationbrainimag-
for small-sample microarray classification? Bioinformatics 20, ing in the uk biobank prospective epidemiological study. Nature
| 374–380. |     |     |     |     |     |     | Neuroscience. |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Brown,C.J.,Hamarneh,G.,2016. Machinelearningonhumancon- Nishimoto, S., Vu, A.T., Naselaris, T., Benjamini, Y., Yu, B., Gal-
|                                |                 |          |                   |             |                  |            | lant, J.L.,                                        | 2011. | Reconstructing                        |     | visual                 | experiences |     | from brain |
| ------------------------------ | --------------- | -------- | ----------------- | ----------- | ---------------- | ---------- | -------------------------------------------------- | ----- | ------------------------------------- | --- | ---------------------- | ----------- | --- | ---------- |
| nectomedatafrommri.            |                 |          | arXiv:1611.08699. |             |                  |            |                                                    |       |                                       |     |                        |             |     |            |
|                                |                 |          |                   |             |                  |            | activityevokedbynaturalmovies.                     |       |                                       |     | CurrentBiology21,1641. |             |     |            |
| Button, K.S.,                  | Ioannidis,      | J.P.,    | Mokrysz,          | C.,         | Nosek, B.A.,     | Flint, J., |                                                    |       |                                       |     |                        |             |     |            |
|                                |                 |          |                   |             |                  |            | Norman,K.A.,Polyn,S.M.,Detre,G.J.,Haxby,J.V.,2006. |       |                                       |     |                        |             |     | Beyond     |
| Robinson,                      | E.S.,           | Munaf`o, | M.R.,             | 2013. Power | failure:         | why small  |                                                    |       |                                       |     |                        |             |     |            |
|                                |                 |          |                   |             |                  |            | mind-reading:                                      |       | multi-voxelpatternanalysisoffMRIdata. |     |                        |             |     | Trends     |
| sample                         | size undermines |          | the reliability   |             | of neuroscience. | Nature     |                                                    |       |                                       |     |                        |             |     |            |
| ReviewsNeuroscience14,365–376. |                 |          |                   |             |                  |            | incognitivesciences10,424.                         |       |                                       |     |                        |             |     |            |
Carp, J., 2012. The secret lives of experiments: methods reporting Penny, W.D., Friston, K.J., Ashburner, J.T., Kiebel, S.J., Nichols,
inthefmriliterature. Neuroimage63,289–300. T.E., 2007. Statistical Parametric Mapping: The Analysis of
Costafreda, S.G., 2009. Pooling fmri data: meta-analysis, mega- FunctionalBrainImages. AcademicPress,London.
analysisandmulti-centerstudies. Frontiersinneuroinformatics3, Pereira,F.,Botvinick,M.,2011. Informationmappingwithpattern
|     |     |     |     |     |     |     | classifiers: | acomparativestudy. |     |     | Neuroimage56,476. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------------ | --- | --- | ----------------- | --- | --- | --- |
33.
|             |     |            |                 |             |           |              | Pereira,                              | F., Mitchell, | T., | Botvinick, | M., | 2009.              | Machine | learning |
| ----------- | --- | ---------- | --------------- | ----------- | --------- | ------------ | ------------------------------------- | ------------- | --- | ---------- | --- | ------------------ | ------- | -------- |
| Dansereau,  | C., | Benhajali, | Y., Risterucci, |             | C., Pich, | E.M., Orban, |                                       |               |     |            |     |                    |         |          |
|             |     |            |                 |             |           |              | classifiersandfMRI:atutorialoverview. |               |     |            |     | Neuroimage45,S199. |         |          |
| P., Arnold, | D., | Bellec,    | P., 2017.       | Statistical | power and | prediction   |                                       |               |     |            |     |                    |         |          |
Pinel,P.,Thirion,B.,Meriaux,S.,Jobert,A.,Serres,J.,LeBihan,
| accuracyinmultisiteresting-statefmriconnectivity. |     |     |     |     |     | NeuroImage |     |     |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
149,220–232. D., Poline, J.B., Dehaene, S., 2007. Fast reproducible identifica-
Demˇsar,J.,2006. Statisticalcomparisonsofclassifiersovermultiple tion and large-scale databasing of individual functional cognitive
datasets. JournalofMachinelearningresearch7,1–30. networks. BMCneuroscience8,91.
Di Martino, A., Yan, C.G., Li, Q., Denio, E., Castellanos, F.X., Poldrack, R., Baker, C.I., Durnez, J., Gorgolewski, K., Matthews,
Alaerts, K., Anderson, J.S., Assaf, M., Bookheimer, S.Y., P.M.,Munafo,M.,Nichols,T.,Poline,J.B.,Vul,E.,Yarkoni,T.,
Dapretto, M., et al., 2014. The autism brain imaging data ex- 2017. Scanning the horizon: Future challenges for neuroimaging
|         |                                                     |     |     |     |     |     | research. | NatureReviewsNeuroscience18,115. |     |     |     |     |     |     |
| ------- | --------------------------------------------------- | --- | --- | --- | --- | --- | --------- | -------------------------------- | --- | --- | --- | --- | --- | --- |
| change: | towardsalarge-scaleevaluationoftheintrinsicbrainar- |     |     |     |     |     |           |                                  |     |     |     |     |     |     |
Poldrack,R.A.,Barch,D.M.,Mitchell,J.,Wager,T.,Wagner,A.D.,
| chitectureinautism. |     | Molecularpsychiatry19,659–667. |     |     |     |     |         |       |            |         |     |         |           |        |
| ------------------- | --- | ------------------------------ | --- | --- | --- | --- | ------- | ----- | ---------- | ------- | --- | ------- | --------- | ------ |
|                     |     |                                |     |     |     |     | Devlin, | J.T., | Cumba, C., | Koyejo, | O., | Milham, | M., 2013. | Toward |
Dwork,C.,Feldman,V.,Hardt,M.,Pitassi,T.,Reingold,O.,Roth,
A., 2015. The reusable holdout: Preserving validity in adaptive opensharingoftask-basedfmridata: theopenfmriproject. Fron-
| dataanalysis. |     | Science349,636. |     |     |     |     | tiersinneuroinformatics7,12. |     |     |     |     |     |     |     |
| ------------- | --- | --------------- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
Gorgolewski, K.J., Varoquaux, G., Rivera, G., Schwarz, Y., Ghosh, Poldrack,R.A.,Gorgolewski,K.J.,2014.Makingbigdataopen: data
S.S., Maumet, C., Sochat, V.V., Nichols, T.E., Poldrack, R.A., sharinginneuroimaging. Natureneuroscience17,1510–1517.
Poline,J.B.,etal.,2015. Neurovault.org: aweb-basedrepository Poldrack,R.A.,Halchenko,Y.O.,Hanson,S.J.,2009. Decodingthe
for collecting and sharing unthresholded statistical maps of the large-scalestructureofbrainfunctionbyclassifyingmentalstates
|             |     |                                 |     |     |     |     | acrossindividuals. |     | PsychologicalScience20,1364. |     |     |     |     |     |
| ----------- | --- | ------------------------------- | --- | --- | --- | --- | ------------------ | --- | ---------------------------- | --- | --- | --- | --- | --- |
| humanbrain. |     | Frontiersinneuroinformatics9,8. |     |     |     |     |                    |     |                              |     |     |     |     |     |
7

Rosenthal,R.,1979. Thefiledrawerproblemandtolerancefornull inelderlysubjects. NeuroImage97,333–348.
results. Psychologicalbulletin86,638.
Saeb,S.,Lonini,L.,Jayaraman,A.,Mohr,DavidandKording,K.P.,
2017. The need to approximate the use-case in clinical machine Appendix A. Additional considerations on uncer-
learning. GigaScience,inpress.
tainty in prediction accuracy
Saxe, R., Brett, M., Kanwisher, N., 2006. Divide and conquer: a
defenseoffunctionallocalizers. Neuroimage30,1088–1096.
Appendix A.1. The reusable holdout
Silva, R.F., Castro, E., Gupta, C.N., Cetin, M., Arbabshirani, M.,
Potluru, V.K., Plis, S.M., Calhoun, V.D., 2014. The tenth an- Dwork et al. (2015) propose an elegant technique to reuse
nual mlsp competition: schizophrenia classification challenge, in: a given holdout set while avoiding overfitting it. However, the
Machine Learning for Signal Processing (MLSP), 2014 IEEE In-
technique relies on jittering the measure of prediction error
ternationalWorkshopon,IEEE.pp.1–6.
when it is below a threshold7. The technique does not fix the
Simmons, J.P., Nelson, L.D., Simonsohn, U., 2011. False-positive
psychology: Undisclosedflexibilityindatacollectionandanalysis intrinsicuncertaintyinthemeasurementofthepredictionaccu-
allows presenting anything as significant. Psychological science racy–atasklikelyimpossible–butitembedsthisuncertaintyin
22,1359. thevalidationprocedure,refusingtoconcludebeyondathresh-
Skocik, M., Collins, J., Callahan-Flintoft, C., Bowman, H., Wyble, old directly related to confidence intervals of the prediction
B., 2016. I tried a bunch of things: the dangers of unexpected
(Dworketal.,2015,suppmat). Agivencontrolongeneraliza-
overfittinginclassification. bioRxiv,078816.
tionperformancerequiressettingthethresholdproportionalto
Smith, S.M., Nichols, T.E., Vidaurre, D., Winkler, A.M., Behrens, √
n. Thereusableholdoutisabeautifulimprovementtocross-
T.E., Glasser, M.F., Ugurbil, K., Barch, D.M., Van Essen, D.C.,
Miller,K.L.,2015.Apositive-negativemodeofpopulationcovari- validation, that is however aligned with the main point that I
ationlinksbrainconnectivity,demographicsandbehavior.Nature ammaking: measuringpredictionaccuracyisnotreliablewith
neuroscience18,1565–1567. small samples.
Stelzer,J.,Chen,Y.,Turner,R.,2013.Statisticalinferenceandmul-
tipletestingcorrectioninclassification-basedmulti-voxelpattern
Appendix A.2. Confidence bounds for varying expected ac-
analysis (mvpa): random permutations and cluster size control.
Neuroimage65,69–82. curacy
Szucs, D., Ioannidis, J.P., 2016. Empirical assessment of published The experiments performed so far are for a chance level
effect sizes and power in the recent cognitive neuroscience and
of 50% and an average prediction accuracy of 75%. While
psychologyliterature. bioRxiv,071530.
thesenumbersaretypicalinmanydecodingexperiments,some
Thompson, P.M., Stein, J.L., Medland, S.E., Hibar, D.P., Vasquez,
experiments probe multiclass decoding, sometimes with many
A.A., Renteria, M.E., Toro, R., Jahanshad, N., Schumann, G.,
Franke, B., et al., 2014. The enigma consortium: large-scale classes,inwhichcasetheaccuracyunderchanceaswellasthe
collaborative analyses of neuroimaging and genetic data. Brain observed accuracy may be much lower. In such situations, the
imagingandbehavior8,153–182. mechanisms driving estimation errors in cross-validation are
VanEssen,D.C.,Smith,S.M.,Barch,D.M.,Behrens,T.E.,Yacoub, thesame, henceabinomiallawstillgivealower-boundonthe
E.,Ugurbil,K.,Consortium,W.M.H.,etal.,2013. Thewu-minn
distribution of errors. The binomial must be adapted to be
humanconnectomeproject: anoverview. Neuroimage80,62–79.
centered on the expected accuracy, whether it is to compute
Varoquaux,G.,Gramfort,A.,Thirion,B.,2012. Small-samplebrain
mapping: sparserecoveryonspatiallycorrelateddesignswithran- the null distribution or to evaluate confidence bounds on ob-
domizationandclustering. ICML,1375. servedvalues. FigureA1showsdifferentbinomialdistributions
Varoquaux,G.,Raamana,P.R.,Engemann,D.A.,Hoyos-Idrobo,A.,
Schwartz, Y., Thirion, B., 2017. Assessing and tuning brain de-
coders: cross-validation,caveats,andguidelines.NeuroImage145, 7Technically,thejitterisperformedwhentrainandtesterrorsare
166–179.
veryclosetoeachother. Optimally-tunedpredictorsstrikeabalance
Varoquaux,G.,Thirion,B.,2014. Howmachinelearningisshaping
between over and under fit and hence have close error rates on the
cognitiveneuroimaging. GigaScience3,28.
trainandtestset.
Vul, E., Harris, C., Winkielman, P., Pashler, H., 2009. Puzzlingly
highcorrelationsinfmristudiesofemotion,personality,andsocial
cognition. Perspectivesonpsychologicalscience4,274.
Wager, T.D., Atlas, L.Y., Lindquist, M.A., Roy, M., Woo, C.W.,
Kross, E., 2013. An fMRI-based neurologic signature of physical
pain. NewEnglandJournalofMedicine368,1388.
Wolfers,T.,Buitelaar,J.K.,Beckmann,C.F.,Franke,B.,Marquand, 30
A.F.,2015.Fromestimatingactivationlocalitytopredictingdisor-
der: areviewofpatternrecognitionforneuroimaging-basedpsy-
chiatric diagnostics. Neuroscience & Biobehavioral Reviews 57,
328.
100
Woo,C.W.,Chang,L.J.,Lindquist,M.A.,Wager,T.D.,2017.Build-
ing better biomarkers: brain models in translational neuroimag-
ing. NatureNeuroscience20,365–377.
Yahata, N., Morimoto, J., Hashimoto, R., Lisi, G., Shibata, K.,
Kawakubo,Y.,Kuwabara,H.,Kuroda,M.,Yamada,T.,Megumi, 300
F.,etal.,.Asmallnumberofabnormalbrainconnectionspredicts
0% 20% 40% 60% 80% 100%
adultautismspectrumdisorder. NATURE7,1.
Distribution of errors under a binomial law
Yarkoni,T.,Westfall,J.,2016.Choosingpredictionoverexplanation
inpsychology: Lessonsfrommachinelearning. figsharepreprint.
Ziegler, G., Ridgway, G.R., Dahnke, R., Gaser, C., Initiative,
A.D.N.,etal.,2014.Individualizedgaussianprocess-basedpredic-
tion and detection of local and global gray matter abnormalities
selpmas
elbaliava
fo
rebmuN
10% 25% 50% 75% 90%
FigureA1: VaryingexpectedaccuracyBinomialdistributionsfor
varying expected accuracy and number of samples. These indicate
the shape of sampling noise, whether it is for a null distribution or
theobservedvalues.
8

| Expected |             |            | 5%–95%      | confidence | bounds |             |         |                  |             |             |            |     |     |     |     |
| -------- | ----------- | ---------- | ----------- | ---------- | ------ | ----------- | ------- | ---------------- | ----------- | ----------- | ---------- | --- | --- | --- | --- |
| accuracy |             | 30 samples | 100         | samples    |        | 300         | samples |                  |             |             |            |     |     |     |     |
|          |             |            |             |            |        |             |         | Figure A3:       | 2D          | view on     | simu-      |     |     |     |     |
| 10.0%    | 3.3%–20.0%  |            | 5.0%–15.0%  |            |        | 7.3%–13.0%  |         |                  |             |             |            |     |     |     |     |
|          |             |            |             |            |        |             |         | lated data       | The         | two classes | are        |     |     |     |     |
| 25.0%    | 13.3%–40.0% |            | 18.0%–32.0% |            |        | 21.0%–29.0% |         |                  |             |             |            |     |     |     |     |
|          |             |            |             |            |        |             |         | represented      | in red      | and         | blue cir-  | 2X  |     |     |     |
| 50.0%    | 36.7%–63.3% |            | 42.0%–58.0% |            |        | 45.3%–54.7% |         |                  |             |             |            |     |     |     |     |
|          |             |            |             |            |        |             |         | cles. Here,      | to simplify |             | visualiza- |     |     |     |     |
| 75.0%    | 60.0%–86.7% |            | 68.0%–82.0% |            |        | 71.0%–79.0% |         |                  |             |             |            |     |     |     |     |
|          |             |            |             |            |        |             |         | tion, the        | data are    | generated   | in         |     |     |     |     |
| 90.0%    | 80.0%–96.7% |            | 85.0%–95.0% |            |        | 87.0%–92.7% |         |                  |             |             |            |     |     |     |     |
|          |             |            |             |            |        |             |         | 2D (2 features), |             | unlike      | the actual |     |     |     |     |
experiments,whichareperformed
on300features.
TableA1: Confidenceboundsforavaryingexpectedaccuracyand
varyingnumberofsamples,the5and95%percentileofthebinomial
X1
| distribution,     | giving   | a lower-bound |              | on the | confidence   |                | bounds as it |             |     |          |              |     |            |           |     |
| ----------------- | -------- | ------------- | ------------ | ------ | ------------ | -------------- | ------------ | ----------- | --- | -------- | ------------ | --- | ---------- | --------- | --- |
| is a conservative |          | distribution  | of           | errors | (see Figure  | A5).           | Not that     |             |     |          |              |     |            |           |     |
| experiments       | revealed | that          | the binomial |        | distribution | underestimates |              |             |     |          |              |     |            |           |     |
|                   |          |               |              |        |              |                |              | The classes | are | centered | respectively |     | on vectors | (µ,...,µ) | and |
errors,henceactualconfidenceboundsarelikelytobehigher.
|     |     |     |     |     |     |     |     | (−µ,...,−µ)  | where    | µ            | is a parameter |        | adjusted    | to           | control the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | ------------ | -------------- | ------ | ----------- | ------------ | ----------- |
|     |     |     |     |     |     |     |     | separability | of       | the classes. | With           | larger | µ           | the expected | pre-        |
|     |     |     |     |     |     |     |     | dictive      | accuracy | would        | be higher.     |        | The samples |              | are gener-  |
forvariousvaluesofexpectedaccuracyandnumberofsamples.
|              |          |     |          |       |       |                   |     | ated i.i.d., | with | is a | simplification |     | compared | to  | time-series, |
| ------------ | -------- | --- | -------- | ----- | ----- | ----------------- | --- | ------------ | ---- | ---- | -------------- | --- | -------- | --- | ------------ |
| For expected | accuracy |     | close to | 0% or | 100%, | the distributions |     |              |      |      |                |     |          |     |              |
narrowandbecomesasymmetricduetothecensoringeffectof as in decoding, where there often is a dependence between
theselimits. Withlargesamplesizes,thedistributionsaremore neighboring observations, or in the same session. I chose the
|                                       |     |     |     |     |                    |     |     | separability | µ empirically |       | to have   | a   | classification    | accuracy | of    |
| ------------------------------------- | --- | --- | --- | --- | ------------------ | --- | --- | ------------ | ------------- | ----- | --------- | --- | ----------------- | -------- | ----- |
| narrow,andtheseeffectsarelessvisible. |     |     |     |     | TableA1givescorre- |     |     |              |               |       |           |     |                   |          |       |
|                                       |     |     |     |     |                    |     |     | 75%. Figure  | A3            | shows | a 2D view | of  | the corresponding |          | data. |
sponding5and95%confidenceboundsandshowsthatindeed,
|     |     |     |     |     |     |     |     | Code to | reproduce | the | simulations |     | can be | found | on  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --- | ----------- | --- | ------ | ----- | --- |
the confidence bounds are tighter near 0% or 100% prediction https:
accuracy. //github.com/GaelVaroquaux/cross_validation_failure.
|     |     |     |     |     |     |     |     | Appendix | C.2. | Experiments | on  | simulated |     | data |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ----------- | --- | --------- | --- | ---- | --- |
Appendix B. Experiments of Varoquaux 2017 Unlikewithabrainimagingdatasets,simulationsopenthe
doortomeasuringtheactualpredictionperformanceofaclassi-
To facilitate reading this paper, I summarize here the ex- fier,andthereforecomparingittothecross-validationmeasure.
| perimentalprotocolusedinVaroquauxetal.(2017). |     |     |     |     |     |     | Theprin- |     |               |     |            |                       |     |     |      |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | --- | ------------- | --- | ---------- | --------------------- | --- | --- | ---- |
|                                               |     |     |     |     |     |     |          | For | this purpose, |     | I generate | a pseudo-experimental |     |     | data |
cipleoftheexperimentisthatthedataaresplittwice(seeFig-
|     |     |     |     |     |     |     |     | with a varying |     | number | of train | samples, | and | a separate | very |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------ | -------- | -------- | --- | ---------- | ---- |
ureA2): firstinadecodingsetandavalidationset;thencross-
|            |              |     |        |          |     |         |             | large test | set, with | 10000 | samples. |     | The train | samples | corre- |
| ---------- | ------------ | --- | ------ | -------- | --- | ------- | ----------- | ---------- | --------- | ----- | -------- | --- | --------- | ------- | ------ |
| validation | is performed |     | on the | decoding | set | results | in an esti- |            |           |       |          |     |           |         |        |
spondtothedataavailableduringaneuroimagingexperiment,
mate of prediction accuracy –as in any cross-validation based and I perform cross-validation on these. I then apply the de-
| study–;      | finally | this estimate | is           | compared | to         | the prediction | ac-         |                    |        |                                     |       |       |            |         |             |
| ------------ | ------- | ------------- | ------------ | -------- | ---------- | -------------- | ----------- | ------------------ | ------ | ----------------------------------- | ----- | ----- | ---------- | ------- | ----------- |
|              |         |               |              |          |            |                |             | coderonthetestset. |        | Thelargenumberoftestsamplesprovides |       |       |            |         |             |
| curacy       | of the  | models        | on the       | left-out | validation | set.           | To give     |                    |        |                                     |       |       |            |         |             |
|              |         |               |              |          |            |                |             | a good measure     |        | of prediction                       | power | of    | the        | decoder | (Arlot and  |
| a good       | measure | of accuracy   | on           | the      | validation | set,           | this set is |                    |        |                                     |       |       |            |         |             |
|              |         |               |              |          |            |                |             | Celisse,           | 2010). | As a decoder,                       |       | I use | a linear   | SVM     | with C=1,   |
| taken large, | as      | large as      | the decoding |          | set. The   | estimation     | error       |                    |        |                                     |       |       |            |         |             |
|              |         |               |              |          |            |                |             | as it is           | common | in neuroimaging.                    |       | To    | accumulate |         | measures, I |
ofcross-validationisthenmeasuredbythediscrepancybetween repeat the whole procedure 1000 times.
| the prediction |     | accuracy | on the | validation       | set, | and       | the predic- |     |     |     |     |     |     |     |     |
| -------------- | --- | -------- | ------ | ---------------- | ---- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| tion accuracy  |     | obtained | by the | cross-validation |      | procedure | on          |     |     |     |     |     |     |     |     |
the decoding set. Varoquaux et al. (2017) applied such exper- Appendix D. Results on the standard error of the
iments on a variety of neuroimaging decoding datasets, within mean
| and across | subjects, | in       | fMRI,             | VBM | (Voxel | Based | Morphome- |          |          |          |            |        |      |                  |     |
| ---------- | --------- | -------- | ----------------- | --- | ------ | ----- | --------- | -------- | -------- | -------- | ---------- | ------ | ---- | ---------------- | --- |
|            |           |          |                   |     |        |       |           | A common |          | approach | to give    | error  | bars | is to compute    | the |
| try) and   | MEG       | (Magneto | EncephaloGraphy). |     |        |       |           |          |          |          |            |        |      |                  |     |
|            |           |          |                   |     |        |       |           | standard | error of | the      | mean (SEM) | across | the  | cross-validation |     |
Full data folds. For samples drawn from a normal distribution, the dis-
|     |     |     |     |     |     |     |     | tance from | the | mean | of the upper | and | lower | 95% | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---- | ------------ | --- | ----- | --- | ---------- |
Outer loop limit is given by 1.64SEM 8. The SEM is also the quantity
|     |     |     |     |     |     |     |     | thatappearsinaTtest. |     |     | Onthesimulations,Icomparedsuch |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ------------------------------ | --- | --- | --- | --- |
confidencelimitscomputedfromtheSEMtotheobservedper-
|     |     | Decoding set |     |     | Validation set |     |     |            |        |     |     |     |     |     |     |
| --- | --- | ------------ | --- | --- | -------------- | --- | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- |
|     |     |              |     |     |                |     |     | centile of | Figure | A4. |     |     |     |     |     |
Nested loop
|     |     |     |     |     |     |     |     | Using | the standard |     | formula | based | on  | the SEM | under- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------------ | --- | ------- | ----- | --- | ------- | ------ |
Train set Test set estimatesactualconfidenceboundsbyafactorof0.73forleave
|     |     |     |     |     |     |     |     | one out | and 0.26 | for | repeated | train-test | split | with | 20% left |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | --- | -------- | ---------- | ----- | ---- | -------- |
FigureA2: Splittingthedatatwice: firstinvalidationanddecoding out and 50 splits. There is indeed a wide difference is how
set,andthenperformingcross-validationonthedecodingset. much different folds are correlated in a cross-validation strat-
|     |     |     |     |     |     |     |     | egy. To | give a more | precise | estimation |     | of prediction |     | accuracy, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | ------- | ---------- | --- | ------------- | --- | --------- |
repeatedrandomsplitscreatemorecorrelationsacrossfold,and
Appendix C. Details on the simulations hencestandardSEMcomputationthatignoresthiscorrelation
|                                                        |      |           |            |      |     |          |          | is more  | severely | incorrect. |     |            |       |     |          |
| ------------------------------------------------------ | ---- | --------- | ---------- | ---- | --- | -------- | -------- | -------- | -------- | ---------- | --- | ---------- | ----- | --- | -------- |
| Appendix                                               | C.1. | Dataset   | simulation |      |     |          |          |          |          |            |     |            |       |     |          |
| I generate                                             |      | data with | samples    | from | two | classes, | each de- |          |          |            |     |            |       |     |          |
|                                                        |      |           |            |      |     |          |          | 8If the  | test is  | two-sided, | the | confidence | bound | are | given by |
| scribedbyaGaussianofidentitycovariancein100dimensions. |      |           |            |      |     |          |          | 1.96SEM. |          |            |     |            |       |     |          |
9

|     |  MES morf timil ecnedifnoc %59 | +20% | SEM over­estimates error bars |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------------------------ | ---- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
srab rorre setamitse­rednu MES
Cross­validation
+15% strategy
LOO
50 splits
|     |     | +10% | 20% test |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
+5%
 0%
|     |     |  0% | +5% | +10% | +15% | +20% |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
95 percentile on the observed error
|     | CV       |     | train | SEM    | empirical |        |     |     |     |     |     |     |     |     |
| --- | -------- | --- | ----- | ------ | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
|     | strategy |     | size  | error  | bar error | bar    |     |     |     |     |     |     |     |     |
|     |          |     | 30    | ±13.8% |           | ±18.9% |     |     |     |     |     |     |     |     |
Perfect
|     |     |     | 100  | ±7.4% |     | ±10.3% |     |     |                                 |      |     |     | LLOOOO |     |
| --- | --- | --- | ---- | ----- | --- | ------ | --- | --- | ------------------------------- | ---- | --- | --- | ------ | --- |
|     | LOO |     |      |       |     |        |     |     | predictor                       |      |     |     |        |     |
|     |     |     |      | ±4.1% |     | ±5.9%  |     |     |                                 |      |     |     |        |     |
|     |     |     | 300  |       |     |        |     |     |                                 | ­11% |     | +8% |        |     |
|     |     |     |      |       |     |        |     |     | selpmas elbaliava fo rebmuN 100 |      |     |     |        |     |
|     |     |     | 1000 | ±2.2% |     | ±2.9%  |     |     |                                 |      |     |     |        |     |
|     |     |     |      |       |     |        |     |     |                                 | ­10% |     | +8% |        |     |
30 ±3.4% ±15.3% 5500  sspplliittss,,  2200%%  lleefftt  oouutt
|     | 50  | splits, | 100 | ±2.0% |     | ±8.1% |     |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
LOO
|     | 20% | test | 300  | ±1.1% |     | ±4.1% |     |     |     |     |     |     |     |     |
| --- | --- | ---- | ---- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |      |      |       |     |       |     |     |     |     | ­6% | +5% |     |     |
|     |     |      |      | ±0.6% |     | ±2.1% |     |     |     |     |     |     |     |     |
|     |     |      | 1000 |       |     |       |     |     | 300 |     |     |     |     |     |
|     |     |      |      |       |     |       |     |     |     |     | ­6% | +6% |     |     |
Figure A4: Error bars: SEM estimates versus observed In 50 splits, 20% left out
conventional models, the confidence limits are a factor 1.64 of the LOO
standarderrorofthemean(SEM).Thisfigurerepresentssuchconfi-
dencelimitsoncross-validationestimatedfromSEMacrossthefolds ­3% +3%
900
| as a function | of  | the actual | estimation | error      | observed |         | in the     | simula- |     |     |     |     |     |     |
| ------------- | --- | ---------- | ---------- | ---------- | -------- | ------- | ---------- | ------- | --- | --- | --- | --- | --- | --- |
|               |     |            |            |            |          |         |            |         |     |     | ­3% | +3% |     |     |
| tions. Using  | the | standard   | formula    | to compute |          | the 95% | confidence |         |     |     |     |     |     |     |
limitunder-estimatesitsignificantlycomparedtotheactual95per- 50 splits, 20% left out
centile of the observed error, thought the two different choices of ­15% ­10% ­5%  0% +5% +10%+15%
cross-validationstrategy,leaveoneout,and50-timesrepeatedsplit- Error on the estimation of prediction accuracy
| tingof20%ofthedata, |     |     | givedifferentunder-estimation: |     |     |     | afactorof |     |     |     |     |     |     |     |
| ------------------- | --- | --- | ------------------------------ | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
0.73forleaveoneout,and0.26for50repeatsplits.
|          |     |                |     |      |     |         |         |     | FigureA5: Cross-validationerrorwiththeperfectpredictor. |     |                      |              |                  |           |
| -------- | --- | -------------- | --- | ---- | --- | ------- | ------- | --- | ------------------------------------------------------- | --- | -------------------- | ------------ | ---------------- | --------- |
|          |     |                |     |      |     |         |         |     | Given a data-independent                                |     | optimal predictor,   | distribution |                  | of errors |
| Appendix |     | E. Experiments |     | with | the | perfect | predic- |     |                                                         |     |                      |              |                  |           |
|          |     |                |     |      |     |         |         |     | between the prediction                                  |     | accuracy as assessed | via          | cross-validation | on        |
tor dataofvarioussamplesizesandtheexpectederrorofthepredictor.
Thebarandwhiskersindicatethemedianandthe5thand95thper-
To fully rule out that the errors witnessed on cross- centile. Thedistributionsarereportedfortworeasonablechoicesof
validationareduetoinstabilitiesofthepredictivemodel,Ire- cross-validation strategy: leave one out, or 50-times repeated split-
tingof20%ofthedata.
peatedtheexperimentswithapredictorindependentfromthe
data. Specifically,Iusedtheknowledgeofthedata-generating
| process  | to create | a classifier     |               | making      | best         | decision  | possible.   | I   |     |     |     |     |     |     |
| -------- | --------- | ---------------- | ------------- | ----------- | ------------ | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| then ran | the       | cross-validation |               | experiments |              | with this | classifier. |     |     |     |     |     |     |     |
| Figure   | A5 gives  | the              | corresponding |             | distribution |           | of mismatch |     |     |     |     |     |     |     |
betweentheaccuracymeasuredbycross-validationandtheac-
| tually accuracy |          | of the      | classifier. |                    |              |            |             |         |     |     |     |     |     |     |
| --------------- | -------- | ----------- | ----------- | ------------------ | ------------ | ---------- | ----------- | ------- | --- | --- | --- | --- | --- | --- |
| The             | results  | with        | the perfect | predictor          |              | are very   | similar     | to      |     |     |     |     |     |     |
| those using     | an       | actual      | decoder     | trained            | on the       | data9      | (Figure     | 1b      |     |     |     |     |     |     |
| using a         | linear   | SVM).       | Given       | that the           | classifier   | is         | independent |         |     |     |     |     |     |     |
| of the data,    | the      | variability | observed    |                    | here can     | clearly    | be          | traced  |     |     |     |     |     |     |
| to sampling     | noise    | in          | the test    | set. Leave-one-out |              |            | and random  |         |     |     |     |     |     |     |
| splits with     | 20%      | of the      | data        | give the           | same errors. |            |             |         |     |     |     |     |     |     |
| 9Note           | that     | I set the   | separation  | in                 | the data     | generation |             | to have |     |     |     |     |     |     |
| a prediction    | accuracy |             | of 75%.     | As the             | perfect      | predictor  | is a        | better  |     |     |     |     |     |     |
predictorthanalinearSVC,experimentswiththeperfectpredictor
aredonewithalargeseparation.
10