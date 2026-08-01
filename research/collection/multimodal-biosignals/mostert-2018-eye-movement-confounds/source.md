NewResearch
Cognition and Behavior
Eye Movement-Related Confounds in Neural
Decoding of Visual Working Memory
Representations
Pim Mostert,1 Anke Marit Albers,1,2 Loek Brinkman,1,3 Larisa Todorova,1,4 Peter Kok,5,6 and
Floris P. de Lange1
DOI:http://dx.doi.org/10.1523/ENEURO.0401-17.2018
1DondersInstituteforBrain,CognitionandBehaviour,RadboudUniversity,Nijmegen6500HB,TheNetherlands,2Abteilung
AllgemeinePsychologie,Justus-Liebig-Universität,Giessen35394,Germany,3DepartmentofPsychology,UtrechtUniversity,Utrecht
3584CS,TheNetherlands,4CenterforMind/BrainSciences,UniversityofTrento,RoveretoTN38068,Italy,5PrincetonNeuroscience
Institute,PrincetonUniversity,Princeton,NJ08544,and6DepartmentofPsychology,YaleUniversity,NewHaven,CT06511
Abstract
A relatively new analysis technique, known as neural decoding or multivariate pattern analysis (MVPA), has
becomeincreasinglypopularforcognitiveneuroimagingstudiesoverrecentyears.Thesetechniquespromiseto
uncover the representational contents of neural signals, as well as the underlying code and the dynamic profile
thereof.Afieldinwhichthesetechniqueshaveledtonovelinsightsinparticularisthatofvisualworkingmemory
(VWM). In the present study, we subjected human volunteers to a combined VWM/imagery task while recording
theirneuralsignalsusingmagnetoencephalography(MEG).Weappliedmultivariatedecodinganalysestouncover
the temporal profile underlying the neural representations of the memorized item. Analysis of gaze position
however revealed that our results were contaminated by systematic eye movements, suggesting that the MEG
decoding results from our originally planned analyses were confounded. In addition to the eye movement
analyses, we also present the original analyses to highlight how these might have readily led to invalid
conclusions.Finally,wedemonstrateapotentialremedy,wherebywetrainthedecodersonafunctionallocalizer
that was specifically designed to target bottom-up sensory signals and as such avoids eye movements. We
conclude by arguing for more awareness of the potentially pervasive and ubiquitous effects of eye movement-
related confounds.
Key words: eye movements; magnetoencephalography; multivariate decoding; visual working memory
Significance Statement
Neural decoding is an important and relatively novel technique that has opened up new avenues for
cognitiveneuroscienceresearch.However,withitspromisesalsocomepotentialcaveats.Inthisstudywe
showthatneuraldecodingmaybesusceptibletoconfoundsinducedbysmalltask-andstimulus-specific
eye movements in the context of a visual working memory (VWM) task. Such eye movements during
working memory tasks have been reported before and may in fact be a common phenomenon. Given the
widespread use of neural decoding and the potentially contaminating effects of eye movements, we
therefore believe that our results are of significant relevance for the field.
July/August2018,5(4)e0401-17.20181–14

|     |     |     |     |     |     |     |     |     |     |     |     | NewResearch |     | 2of14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- |
Introduction stored in early sensory cortex (Albers et al., 2013;
|        |           |     |              |     |         |          | Sreenivasan | et       | al., 2014), | the   | activity-silent |       | coding | hy-  |
| ------ | --------- | --- | ------------ | --- | ------- | -------- | ----------- | -------- | ----------- | ----- | --------------- | ----- | ------ | ---- |
| Neural | decoding, | or  | multivariate |     | pattern | analysis |             |          |             |       |                 |       |        |      |
|        |           |     |              |     |         |          | pothesis    | (Stokes, | 2015;       | Wolff | et al.,         | 2015, | 2017;  | Rose |
(MVPA),isapopularanalysistechniquethathasobtained
considerable momentum in the field of cognitive neuro- et al., 2016; Rademaker and Serences, 2017) and the
imaging(Haxbyetal.,2014;Grootswagersetal.,2017).It dynamic coding framework (Stokes et al., 2013, 2015;
referstouncoveringafactorofinterest,forinstancestim- King et al., 2016; Spaak et al., 2017).
|                |      |              |          |     |           |         | In the | current | study, | human | volunteers |     | performed | a   |
| -------------- | ---- | ------------ | -------- | --- | --------- | ------- | ------ | ------- | ------ | ----- | ---------- | --- | --------- | --- |
| ulus identity, | from | multivariate | patterns |     | in neural | signals |        |         |        |       |            |     |           |     |
combinedVWM/imagerytask,whilewetracedtherepre-
| such as | those measured |     | by magnetoencephalography |     |     |     |     |     |     |     |     |     |     |     |
| ------- | -------------- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(MEG) or functional magnetic resonance imaging (fMRI). sentational contents of their neural activity as measured
Decoding allows one to probe the representational con- by MEG. The experiment was designed to elucidate the
tents of a neural signal, rather than overall activity levels, temporalprofileofthememorizeditem’sneuralrepresen-
|               |                 |     |          |        |             |         | tation. However, |     | control      | analyses | revealed |     | that our   | data |
| ------------- | --------------- | --- | -------- | ------ | ----------- | ------- | ---------------- | --- | ------------ | -------- | -------- | --- | ---------- | ---- |
| with superior | sensitivity.    |     | However, | this   | sensitivity | may     |                  |     |              |          |          |     |            |      |
|               |                 |     |          |        |             |         | were severely    |     | contaminated |          | by small | eye | movements. | In   |
| require       | extra vigilance | at  | the end  | of the | user,       | because |                  |     |              |          |          |     |            |      |
these analyses may also be particularly sensitive to po- thisarticle,wefirstdescribetheeyemovementanalysisto
tentially confounding factors. Here we demonstrate such show how the identity of the memorized item could be
an example, specifically in the context of visual working decoded from gaze position. Next, we present the naive
resultsastheywouldhavebeen,hadwenotbeenaware
| memory   | (VWM), where      |     | a decoding | analysis   |     | is contami- |                  |     |      |            |     |       |       |        |
| -------- | ----------------- | --- | ---------- | ---------- | --- | ----------- | ---------------- | --- | ---- | ---------- | --- | ----- | ----- | ------ |
|          |                   |     |            |            |     |             | of the confound. |     | This | highlights | how | these | could | easily |
| nated by | stimulus-specific |     | eye        | movements. |     | Given the   |                  |     |      |            |     |       |       |        |
widespread use of these techniques and its pivotal con- have been mistaken to provide genuine insight into the
tributions to contemporary VWM theories, we argue that neuralmechanismsunderlyingVWM.Finally,wepresenta
appreciation of these potential caveats is important. potential solution by training the decoders on separate
functionallocalizerblocks,whichallowedustoextractthe
| VWM | is the ability | to  | retain and | use visual |     | information |                  |     |        |           |         |     |             |     |
| --- | -------------- | --- | ---------- | ---------- | --- | ----------- | ---------------- | --- | ------ | --------- | ------- | --- | ----------- | --- |
|     |                |     |            |            |     |             | sensory-specific |     | neural | patterns, | thereby |     | effectively | by- |
abouttheworldforashortperiodoftime,evenwhenthe
original external source of that information is no longer passing the eye-movements confounds.
available.Neuraldecodinghasbeenfrequentlyappliedin
|                                                |        |              |     |        |      |           | Materials | and | Methods |     |     |     |     |     |
| ---------------------------------------------- | ------ | ------------ | --- | ------ | ---- | --------- | --------- | --- | ------- | --- | --- | --- | --- | --- |
| the study                                      | of VWM | to elucidate |     | where, | when | and how a |           |     |         |     |     |     |     |     |
| memorandumisencodedinthebrain.Thiswasfirstdem- |        |              |     |        |      |           | Subjects  |     |         |     |     |     |     |     |
onstratedbyHarrisonandTong(2009)andSerencesetal. Thirty-six human volunteers were recruited from the
| (2009), | who were | able | to decode | the | orientation | of a |     |     |     |     |     |     |     |     |
| ------- | -------- | ---- | --------- | --- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
localinstitute’ssubjectpooltoparticipateinabehavioral
| memorized | grating | from | visual cortex. | Further |     | VWM de- |     |     |     |     |     |     |     |     |
| --------- | ------- | ---- | -------------- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
screeningsession.Ofthese,24(13male;meanage:26.8
codingstudiesextendedHarrisonandTong(2009)’spar-
|     |     |     |     |     |     |     | years, range: | 18–60) | were | selected |     | to participate |     | in the |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------ | ---- | -------- | --- | -------------- | --- | ------ |
adigm in varying ways to study, among others, mental MEG experiment (see below, Experimental design and
imagery, mental transformations, and spatial working procedure). Of these 24 selected subjects, three were
| memory | (Albers et | al., | 2013; Christophel |     | et  | al., 2015, |     |     |     |     |     |     |     |     |
| ------ | ---------- | ---- | ----------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
excludedfromMEGanalysisduetopoordataqualityand
| 2017; Foster | et al., | 2016; | Gayet | et al., | 2017). | The para- |         |           |          |     |          |          |           |     |
| ------------ | ------- | ----- | ----- | ------- | ------ | --------- | ------- | --------- | -------- | --- | -------- | -------- | --------- | --- |
|              |         |       |       |         |        |           | another | four were | excluded |     | from the | analyses | regarding |     |
digmhasalsobeenportedtoelectrophysiologicalstudies
|     |     |     |     |     |     |     | eye movements, |     | because | the | eye-tracker |     | failed | to track |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------- | --- | ----------- | --- | ------ | -------- |
usingMEGorelectroencephalographytocapitalizeonthe the eye reliably in those subjects. The experiment was
hightemporalresolutionofferedbythosemethods(Wolff approved by the local ethics committee and conducted
| et al., 2015, | 2017; | Foster | et al., | 2016; King | et  | al., 2016). |           |        |            |     |     |        |            |     |
| ------------- | ----- | ------ | ------- | ---------- | --- | ----------- | --------- | ------ | ---------- | --- | --- | ------ | ---------- | --- |
|               |       |        |         |            |     |             | according | to the | guidelines | set | out | by the | committee. | All |
Theseresultshaveledtoimportantnewtheories,among
|     |     |     |     |     |     |     | participants | provided |     | written | informed | consent |     | and re- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ------- | -------- | ------- | --- | ------- |
otherstheideathathigh-fidelityVWMrepresentationsare
|                                                                |     |     |     |     |     |     | ceived either                                     | monetary |     | compensation |     | or  | course credits. |     |
| -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | -------- | --- | ------------ | --- | --- | --------------- | --- |
| ReceivedNovember21,2017;acceptedJune12,2018;FirstpublishedJuly |     |     |     |     |     |     | Stimuli                                           |          |     |              |     |     |                 |     |
| 18,2018.                                                       |     |     |     |     |     |     | Stimulationwasvisualandconsistedofsinusoidalgrat- |          |     |              |     |     |                 |     |
Theauthorsdeclarenocompetingfinancialinterests. ings with a spatial frequency of 1 cycle/°, 80% contrast
Author contributions: A.M.A., L.B., L.T., and F.P.d.L. designed research; andonerandomphaseperexperimentalblock.Thegrat-
A.M.A.andL.T.performedresearch;P.M.analyzeddata;P.M.,A.M.A.,L.B., ingsweremaskedatanouterradiusof7.5°andaninner
P.K.,adF.P.d.L.wrotethepaper.
This work was supported by The Netherlands Organisation for Scientific aperture radius of 0.7° and presented on a gray back-
ResearchandtheEuropeanResearchCouncil[NWOResearchTalentGrant ground (luminance: 186 cd/m2). Stimuli were generated
406-13-001(toP.M.);NWOBrainandCognitionGrant433-09-248(toA.M.A. andpresentedusingMATLABwiththePsychtoolboxex-
and L.B.); NWO Rubicon Grant 446-15-004 (to P.K.); and NWO Vidi Grant tension (Kleiner et al., 2007).
452-13-016,ERCStartingGrant678286,andNWOBrainandCognitionGrant
433-09-248(toF.P.d.L.)].
Acknowledgements:WethankIvanToniforusefulsuggestionsduringthe Experimental design and procedure
| designphase. |     |     |     |     |     |     | Themaintaskwastovividlyimagineandrememberan |     |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
CorrespondenceshouldbeaddressedtoFlorisP.deLangeattheabove oriented grating and, in some conditions, mentally rotate
address,E-mail:floris.delange@donders.ru.nl.
|     |     |     |     |     |     |     | this grating | over | a certain | angle. | Each | trial | began | with a |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | --------- | ------ | ---- | ----- | ----- | ------ |
DOI:http://dx.doi.org/10.1523/ENEURO.0401-17.2018
Copyright©2018 Mostertetal. dualcuethatindicatedboththeamount(presentedabove
|     |     |     |     |     |     |     |     |     |     | ((cid:2) |     |     |     | (cid:3) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | ------- |
This is an open-access article distributed under the terms of the Creative fixation) and the direction for clockwise and for
CommonsAttribution4.0Internationallicense,whichpermitsunrestricteduse,
counterclockwise,presentedbelowfixation)ofmentalro-
distributionandreproductioninanymediumprovidedthattheoriginalworkis
|     |     |     |     |     |     |     | tation (MR) | that | was to | be performed |     | in that | trial | (Fig. 1). |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ------ | ------------ | --- | ------- | ----- | --------- |
properlyattributed.
| July/August2018,5(4)e0401-17.2018 |     |     |     |     |     |     |     |     |     |     |     |     | eNeuro.org |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |

NewResearch 3of14
Figure1.Experimentalparadigm.A,InthecombinedVWM/imageryblocks,subjectswereinstructedtovividlyimagineagratingand
toeitherkeepthatinmind(VWMcondition)orrotateitmentallyoveracuednumberofdegrees(MRcondition).B,Inthefunctional
localizerblock,orientedgratingswerecontinuouslypresentedwhilethesubject’sattentionwasdrawntoataskatfixation.C,The
VWM/imageryandlocalizerblockswereperformedinalternatingorder.
Theamountcouldbeeither0°,60°,120°,or180°,ineither Interleaved with the VWM/imagery blocks, there were
clockwise or counterclockwise direction, where 0° corre- sixfunctionallocalizerblocks(Fig.1B,C).Intheseblocks,
spondedtoaVWMtask.Thisconditionwillhenceforthbe gratingsofsixdifferentorientations(15°to165°,insteps
referred to as the VWM condition, and the other three of30°)werepresentedfor250mswithanintertrialinterval
conditions, which corresponded to imagery, as the MR of750ms.Eachblockconsistedof120trials,resultingin
conditions.Thiscuelastedfor417ms,afterwhichablank atotalof120trialsperorientation.Thetaskwastopress
screenwasshownforanother417ms.Afixationdot(four a button when a brief flicker of the fixation dot occurred.
pixelsindiameter)waspresentthroughouttheentiretrial, Suchaflickeroccurredbetween8and12times(randomly
andthroughouttheentireblock.Aftertheblank,agrating selectednumber)perblock,atrandomtimes.Usingsuch
waspresentedfor217msthatcouldhaveeitherofthree ataskweensuredthatspatialattentionwasdrawnaway
orientations: 15°, 75°, or 135° (clockwise with respect to from the gratings while stimulating subjects to maintain
vertical).Next,ablankdelayperiodof8017msfollowed, fixation, allowing us to record activity that predominantly
during which subjects were required to keep the starting reflected bottom-up, sensory-specific signals (Mostert
gratinginmindand,inasubsetoftrials,mentallyrotateit. et al., 2015).
Thedelayperiodwasterminatedbythepresentationofa BeforetheMEGsession,thevolunteersparticipatedin
probe grating for 217 ms, whose orientation was slightly a behavioral screening session that served to both train
jittered (see below, Staircase procedure) with respect to the subjects on the task as well as to assess their ability
the orientation that subjects were supposed to have in to perform it. Subjects were instructed to mentally rotate
mind at that moment. Subjects then indicated with a the stimulus at an angular velocity of 30°/s by demon-
buttonpresswhethertheprobewasorientedclockwiseor strating examples of rotations on the screen. Moreover,
counterclockwise relative to their internal image. The re- during this session subjects were required to press a
sponse period lasted until 2033 ms after probe, after buttonassoonastheyachievedavividimaginationofthe
which feedback was given. There were three trials per gratingoncompletionofthecuedrotation.Thisprovided
design cell (four arcs of rotation and two directions) per aproxyofthespeedatwhichtheyactuallyperformedthe
block, resulting in 24 trials per block. In addition, there rotationandwasusedasselectioncriterionforparticipa-
weretwocatchtrialsperblock,inwhichtheprobegrating tion in the MEG session.
waspresentedatanearliermomentinthedelayintervalto
gaugeongoingrotation.Alltrialswerepresentedinpseu- Staircase procedure
dorandomizedorder.Thecatchtrialswereexcludedfrom The amount of jitter of the probe grating was deter-
further analysis, because subjects indicated to find them mined online using an adaptive staircasing procedure to
difficult and confusing. In general, each experiment con- equalize subjective task difficulty across conditions and
sistedofsixexperimentalblocks(althoughsomesubjects subjects. The starting difference was set to 15° and was
performed five, seven, or eight blocks), preceded by one increased by 1° following an incorrect response and de-
ormorepracticeblocks,resultinginatotalof144exper- creased by 0.5488 after two consecutive correct re-
imental trials for most of the participants. sponses. Such a procedure has a theoretical target
July/August2018,5(4)e0401-17.2018 eNeuro.org

NewResearch 4of14
performanceof(cid:4)80%correct(Garcı´´a-Pérez,1998).Four terval and there should therefore be no systematic rela-
separatestaircaseswereused,oneforeachoftheVWM tionship between the MEG data and the stimulus label.
and MR conditions. However, our rationale was that regardless of condition,
subjects need to first perceive, encode and maintain the
MEG recordings, eye-tracker recordings, and pre-
presented stimulus before they can even commence the
processing
task, be it VWM or MR. Thus, we expected to be able to
Neuralactivitywasmeasuredusingawhole-headMEG
extracttheneuralpatternofthepresentedstimulusduring
system with 275 axial gradiometers (VSM/CTF Systems)
atleastthephysicalpresentationandabriefmomentafter
situated in a magnetically shielded room. A projector
that.Thisclassifierwasthentrainedandappliedacrossall
outside the room projected via a mirror system onto the
time points, resulting in a temporal generalization matrix
screenlocatedinfrontofthesubject.Fiducialcoilsposi-
(KingandDehaene,2014).Itisimportanttonotethatwe
tioned on the nasion and in the ears allowed for online
trained the classifiers only using the labels of the pre-
monitoringofheadpositionandforcorrectioninbetween
sentedstimulusbutsortedthedatainvaryingwayswhen
blocks if necessary. Both vertical and horizontal electro-
testing the performance. For example, by looking at an
oculogram (EOG) as well as electrocardiogram were ob-
early training time point, but a late testing time point, we
tainedtoaidintherecognitionofartifacts.Allsignalswere
sampledat1200HzandanalyzedofflineusingtheField- tested whether we could decode the orientation of the
Trip toolbox (Oostenveld et al., 2011). The data were grating kept in mind near the end of the delay period, on
notch-filtered at 50 Hz and corresponding harmonics to thebasisofthepatternevokedbythepresentedstimulus
removelinenoise,andsubsequentlyinspectedinasemi- early in the trial.
automatic manner to identify irregular artifacts. After re- In the second line of analysis, we trained a continuous
jection of bad segments, independent component orientationdecoderonthefunctionallocalizer.Thelarger
analysis was used to remove components that corre- numberoforientationssampledinthefunctionallocalizer
spondedtoregularartifactssuchasheartbeat,blinksand allowed us to decode a continuous estimate of repre-
eye movements (although our results suggest that the sentedorientation,ratherthanadiscreteonefromafixed
removalofeyemovement-relatedartifactswasimperfect, numberofclasses.WeappliedthisdecodertotheVWM/
see Results and Discussion). The cleaned data were imagery task and subsequently related the decoded ori-
baseline-corrected on the interval of -200–0 ms, relative entationtothetruepresentedorientationbycalculatinga
to stimulus onset. quantity intuitively similar to a correlation coefficient (see
Gaze position and pupil dilation were continuously below, Continuous orientation decoder). Here too, we
trackedthroughouttheexperimentusinganEyelink1000
extended the procedure to include all pairwise training
(SR Researcher) eye-tracker. The eye-tracker was cali-
and testing time points, resulting in temporal generaliza-
brated before each session and signals were sampled at
tion matrices (King and Dehaene, 2014).
1200Hz.Becausewewereinterestedineye-movements
Inthecontrolanalysis,wherewetestedforasystematic
inducedbytheexperimentalstimulation,weremovedany
relationship between gaze position and VWM contents,
slow drifts in the signal by baseline-correcting the signal
werepeatedthefirstlineofanalysisdescribedabove,but
on an interval of -200–0 ms relative to cue onset.
instead used the gaze position (x- and y-coordinates) as
features rather than the MEG data.
Data sharing
All data, as well as analysis scripts required to obtain
Multi-class probabilistic classifier
the presented figures, are available from the Donders
Institute for Brain, Cognition, and Behavior repository at The three-class classifier was based on Bishop (2006,
http://hdl.handle.net/11633/di.dc- pp196–199).Briefly,theclass-conditionaldensitieswere
cn.DSC_3018016.04_526. modeled as Gaussian distributions with assumed equal
covariance.BymeansofBayes’theorem,andassuminga
Classification and decoding analyses flat prior, this model was inverted to yield the posterior
Originally,wefirstfocusedontheneuraldata.Broadly, probabilities, given the data. Specifically, let x be a col-
weconductedtwolinesofdecodinganalyses.Inthefirst, umn vector with length equal to the number of features
we focused only on the blocks in which participants per- [number of sensors for MEG data, two for gaze position
formed the combined VWM/imagery task, using 8-fold (horizontalandverticallocation)]containingthedatatobe
cross-validation. We trained a three-class probabilistic classified, then the posterior probability that the data
classifier that returns the probability that a given trial
belongs to class k is given by the following equations:
belongs to either of the three presented grating orienta-
tions.Toimprovesignal-to-noiseratio,yetretaintheabil- exp(cid:2)a(cid:3)
ity to draw firm conclusions regarding the timing of any P(cid:2)class (cid:2) k(cid:3)x (cid:2) (cid:4) k
decoded signal, we smoothed the data using a moving j
exp(cid:2)a
j
(cid:3)
average with a window of 100 ms. The classifier was
trainedacrossthespatialdimension(i.e.,usingsensorsas a(cid:2)x(cid:3) (cid:2) wTx (cid:4) w
features),ontrialsfromallconditions(i.e.,allamountsand k k k0
directionsofrotation).Thismayseemcounterproductive,
because the mental contents diverge over the delay in- w k (cid:2) S(cid:5)1m k
July/August2018,5(4)e0401-17.2018 eNeuro.org

NewResearch 5of14
(cid:3) (cid:3)
w (cid:2) (cid:5) 1 mTS(cid:5)1m (cid:9)(cid:2) z cos(cid:2)arg(cid:2)z(cid:3)(cid:3)
k0 2 k k
whereNisthenumberoftrialsand(cid:8) isthetrueorienta-
k
where m is the mean of class k and S is the common tion on trial k. The quantity (cid:9)is also known as the test
k
covariance,bothobtainedfromthetrainingset.Thelatter statistic in the V test for circular uniformity, where the
was calculated as the unweighted mean of the three orientation under the alternative hypothesis is prespeci-
covariancematricesforeachindividualclass,andsubse- fied (Berens, 2009). This quantity has properties that
quentlyregularizedusingshrinkage(Blankertzetal.,2011) make it intuitively similar to a correlation coefficient: it is
with a regularization parameter of 0.05 for the MEG data (cid:5)1whendecodedandtrueorientationsareexactlyequal,
and 0.01 for the eye-tracker analysis. -1 when they are in perfect counterphase and 0 when
there is no systematic relationship or when they are per-
fectly orthogonal.
Continuous orientation decoder
The continuous orientation decoder was based on the
Statistical testing
forward-modelingapproachasdescribedinBrouwerand
All inferential statistics were performed by means of a
Heeger (2009, 2011) but adapted for improved perfor-
permutationtestwithcluster-basedmultiplecomparisons
mance (Kok et al., 2017). The forward model postulates
correction(MarisandOostenveld,2007).Thesewereap-
that a grating with a particular orientation activates a
pliedtoeitherwholetemporalgeneralizationmatrices,or
numberofhypotheticalorientationchannels,accordingto
horizontalcross-sectionsthereof(i.e.,afixedtrainingwin-
a characteristic tuning curve, that subsequently lead to
dow).Thesematrices/cross-sectionsweretestedagainst
themeasuredMEGdata.Weformulatedamodelwith24
chance-level (33%) in the classification analysis, or
channelsspacedequallyaroundthecircle,whosetuning
against zero in the continuous decoding analysis. In the
curves were governed by a Von Mises curve with a con-
first step of each permutation, clusters were defined by
centrationparameterof5.Notethatallcircularquantities
adjacent points that crossed a threshold of p (cid:3) 0.05
in the analyses were multiplied by two, because the for-
accordingtoatwo-tailedone-sample ttest.Thetvalues
mulas we used operate on input that is periodic over a
weresummedwithineachcluster,butseparatelyforpos-
range of 360° but grating orientation only ranges from 0°
itive and negative clusters, and the largest of these were
to180°.Next,weinvertedtheforwardmodeltoobtainan
included in the permutation distributions. A cluster in the
inverse model. This model reconstructs activity of the
true data were considered significant if its p value was
orientationchannels,givensometestdata.Inthisstepwe
(cid:3)0.05. For each test, 10,000 permutations were con-
departed from Brouwer and Heeger (2009, 2011)’s origi-
ducted.
nal formulation in two aspects. First, we estimated each
channel independently from each other, allowing us to
Spatial patterns and source analysis
include more channels than there are stimulus classes.
To interpret the signals that the classifier and decoder
Second, we explicitly took into account the correlational
pick up, we looked at the corresponding spatial patterns
structureofthenoise,whichisaprominentcharacteristic
(Haufe et al., 2014). The spatial pattern is the signal that
of MEG data, to improve decoding performance
would be measured if the latent variable that is being
(Blankertzetal.,2011;Mostertetal.,2015).Forfullimple-
decoded is varied by one unit. For both the probabilistic
mentational details, see Kok et al. (2017). The decoding
classifier and the continuous orientation decoder, this
analysis yields a vector c of length equal to number of
comes down to the difference ERF between each cate-
channels (24 in our case) with the estimated channel
gory and the average across all categories. This yields
activityinatesttrial,foreachpairwisetrainingandtesting
one spatial pattern for each class, and these were sub-
time point. These channels activities were then trans-
sequentlyaveragedacrossclasses,aswellasacrosstime
formed into a single orientation estimate (cid:6)by calculating
of interest, and fed into source analysis and synthetic
the circular mean (Berens, 2009) across all the orienta-
planargradienttransformation.Thistransformationrefers
tions the channels are tuned for, weighted by each indi-
to a procedure whereby MEG data recorded with axial
vidual activation:
gradiometers is transformed as if it were measured by
(cid:5) (cid:4) (cid:6) planar gradiometers (Bastiaansen and Knösche, 2000).
(cid:6)(cid:2) arg cexp(cid:2)i(cid:7)(cid:3) The main advantage is that the spatial distribution of the
j j
j resulting data is more readily interpretable.
Forsourceanalysis,weusedatemplateanatomicscan
where the summation is over channels, (cid:7) is the orienta- provided by FieldTrip to create a volume conduction
j
tion around which the jth channel tuning curve is cen- model based on a single shell model of the inner surface
tered, and i is the imaginary unit. These decoded oftheskull.Thesourcemodelconsistedofaregulargrid
orientations can then be related to the true orientation, spaced 0.5 cm apart that encompassed the entire brain.
across trials, as follows: Leadfields were calculated and rank-reduced to two di-
mensions,toaccommodatethefactthatMEGisblindto
(cid:4)N tangential sources. The covariance of the data were cal-
1
z (cid:2) exp(cid:7)i(cid:2)(cid:6) (cid:5) (cid:8)(cid:3)(cid:8) culated over the window of 1–8 s post-stimulus and
N k k
k regularizedusingshrinkage(Blankertzetal.,2011)witha
July/August2018,5(4)e0401-17.2018 eNeuro.org

|     |     |     |     |     |     |     |     |     |     |     |     |     | NewResearch |     | 6of14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- |
regularization parameter of 0.05. The leadfields and data Then, when looking at the decoded signal within the
covariance were then used to calculate linearly con- VWM condition only, we found a sustained pattern (Fig.
| strained | minimum | variance | spatial |     | filters | (LCMV, | also |               |       |      |            |     |              |      |      |
| -------- | ------- | -------- | ------- | --- | ------- | ------ | ---- | ------------- | ----- | ---- | ---------- | --- | ------------ | ---- | ---- |
|          |         |          |         |     |         |        |      | 2A), although | again | only | marginally |     | significant. | This | sug- |
known as beamformers; Van Veen et al., 1997). Applying geststhatonperceivingandencodingthestimulus,sub-
these filters to sensor-level data yields activity estimates jects move their eyes in a way systematically related to
ofatwo-dimensionaldipoleateachgridpoint.Wefurther the identity of the stimulus and keep that gaze position
reducedtheseestimatestoascalarvaluebymeansofthe stable throughout the entire delay period.
Pythagoreantheorem.Thisleadstoapositivitybiashow-
|     |     |     |     |     |     |     |     | Contrary | to  | previously | used | paradigms, |     | where | two |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---------- | ---- | ---------- | --- | ----- | --- |
ever,thatwecorrectedforusingapermutationprocedure stimuli were displayed at the beginning of a trial and a
(Manahovaetal.,2017).Thenumberofpermutationswas retro-cue signaled the item that was to be remembered
10,000. The final result was interpolated to be projected (HarrisonandTong,2009;Albersetal.,2013;Christophel
onacorticalsurfaceandquantifiesthedegreetowhicha
|            |      |             |     |     |             |     |        | et al., 2015, | 2017),        | in  | the   | present   | experiment |     | we only  |
| ---------- | ---- | ----------- | --- | --- | ----------- | --- | ------ | ------------- | ------------- | --- | ----- | --------- | ---------- | --- | -------- |
| particular | area | contributed | to  | the | performance |     | of the |               |               |     |       |           |            |     |          |
|            |      |             |     |     |             |     |        | showed        | one stimulus. |     | It is | therefore | possible   |     | that the |
classifier/decoder. sustained decoding performance does not necessarily
reflectVWMcontents,butsimplythatthesubjectsmoved
| Results |     |     |     |     |     |     |     | theirgazeaccordingtothepresentedstimulusratherthan |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Behavioral results to their mental contents. However, if this were true, then
weshouldfindasimilareffectinthethreeMRconditions.
TheaverageaccuraciesintheMEGsessionforthefour
If,ontheotherhand,theclassifierpickeduptheitemkept
| conditions | ranged | from | 68% | to 72%, | confirming |     | that |     |     |     |     |     |     |     |     |
| ---------- | ------ | ---- | --- | ------- | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
inmind,thentheprobabilitythatatrialisassignedtothe
| subjects | were | able to | do the | task, | as well | as that | the |     |     |     |     |     |     |     |     |
| -------- | ---- | ------- | ------ | ----- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
staircase procedure was successful. The average final same class as the presented stimulus should drop over
jitterestimatefromthestaircaseprocedureforthe0°,60°, time,asthesubjectrotatesthementallyimaginedgrating
|               |      |             |      |       |              |         |       | away from   | the      | starting | orientation. |       | Our results | were    | con-   |
| ------------- | ---- | ----------- | ---- | ----- | ------------ | ------- | ----- | ----------- | -------- | -------- | ------------ | ----- | ----------- | ------- | ------ |
| 120°, and     | 180° | conditions  | were | as    | follows      | (95%-CI | in    |             |          |          |              |       |             |         |        |
|               |      |             |      |       |              |         |       | sistent     | with the | latter   | scenario     | (Fig. | 2B).        | Whereas | the    |
| parentheses): | 3.1° | (0.98-5.2), |      | 11.0° | (8.87-13.0), |         | 13.4° |             |          |          |              |       |             |         |        |
|               |      |             |      |       |              |         |       | probability | that     | the data | belong       | to    | the same    | class   | as the |
(11.35–15.52),and6.5°(4.42-8.60),respectively.Withthe
exception of the 180° condition, the rising trend in these presented stimulus stays steadily above chance in the
valuessuggeststhatsubjectsfoundthetaskmoredifficult VWM condition, it drops to lower levels in the three MR
|     |     |     |     |     |     |     |     | conditions. | Moreover, |     | we found | evidence |     | that | the gaze |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | --- | -------- | -------- | --- | ---- | -------- |
whentheamountofrotationwaslarger.Therelativelylow
movestowardapositionconsistentwiththeorientationof
| value for | the 180° | condition | however |     | indicates | that | this |     |     |     |     |     |     |     |     |
| --------- | -------- | --------- | ------- | --- | --------- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
conditionwasrelativelyeasy.Oneexplanationmaybethe thepresentedgratingplusorminus60°(dependingonthe
fact that subjects did not require the final product of the cued direction of rotation) in the MR conditions, but not
MR to perform well on the task. It is possible that they any further (Fig. 3A,B).
|                |     |           |     |          |              |     |       | Figure | 2C displays |     | the grand | average, |     | as well | as indi- |
| -------------- | --- | --------- | --- | -------- | ------------ | --- | ----- | ------ | ----------- | --- | --------- | -------- | --- | ------- | -------- |
| simultaneously |     | memorized | the | starting | orientation. |     | After |        |             |     |           |          |     |         |          |
vidualaveragegazepositionsduring0.5–1.5safterstim-
havingfinishedtheMR,regardlessofhowwelltheywere
abletodoso,theycouldsimplyreactivatetheinitialimage ulus onset, separately for each of the three stimulus
and use that in their judgment. conditions, collapsed across VWM and MR conditions.
|     |     |     |     |     |     |     |     | Although | there | is large | variability | among |     | subjects | in the |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----- | -------- | ----------- | ----- | --- | -------- | ------ |
magnitudeoftheeyemovements,ageneraltrendcanbe
| Gaze position |     | tracks | VWM contents |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Intheeyemovementanalysis,weinvestigatedwhether discerned where subjects position their gaze along the
thereisarelationbetweengazepositionandtheitemheld orientationaxisofthegrating.Themeandisparityinvisual
in VWM. We adopted the same analysis in our original angle with respect to pre-trial fixation was only 0.23°,
|               |                |           |              |               |                |             |      | which is   | in the  | same | order       | of magnitude |     | as       | reported |
| ------------- | -------------- | --------- | ------------ | ------------- | -------------- | ----------- | ---- | ---------- | ------- | ---- | ----------- | ------------ | --- | -------- | -------- |
| main analysis | (see           | Materials |              | and Methods), |                | but instead |      |            |         |      |             |              |     |          |          |
|               |                |           |              |               |                |             |      | previously | (Foster | et   | al., 2016), | although     |     | for some | sub-     |
| entered       | the horizontal |           | and vertical |               | gaze position, |             | mea- |            |         |      |             |              |     |          |          |
sured by the eye-tracker, as features in the decoding jects, it was larger, up to 1.5°.
analysis.Specifically,weconstructedathree-classprob- In short, there was a systematic relationship between
abilistic classifier that yields the posterior probabilities gaze position and stimulus orientation, after which the
|          |       |             |     |        |          |           |     | gaze position | tracked |     | the orientation |     | kept | in mind | during |
| -------- | ----- | ----------- | --- | ------ | -------- | --------- | --- | ------------- | ------- | --- | --------------- | --- | ---- | ------- | ------ |
| that any | given | data belong | to  | either | of three | presented |     |               |         |     |                 |     |      |         |        |
orientations. That is, the classifier was trained according thedelayperiod,butonlyforamaximumofapproximately
(cid:6)60°
tothelabelsofthepresentedstimulus.Theclassifierwas relative to starting orientation. These findings raise
trained on trials from all conditions (i.e., all amounts and the concern that any potential decoding of VWM items
directionsofrotation)pooledtogethertoobtainmaximum fromMEGsignals,aswastheaimofouroriginalanalysis,
couldbetheresultofstimulus-relatedeyeconfounds(for
| sensitivity | (for rationale, |     | see Materials |     | and Methods). |     | To  |     |     |     |     |     |     |     |     |
| ----------- | --------------- | --- | ------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
verifywhetherwecoulddecodestimulusidentityfromthe possible underlying mechanisms, see Discussion).
| gaze position, | we  | first | applied | the classifier |     | to the | same |     |     |     |     |     |     |     |     |
| -------------- | --- | ----- | ------- | -------------- | --- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
(pooled) data using cross-validation. We found above- Sustained decoding of VWM items from MEG signals
chance decoding in a time period of (cid:4)0.5–3.5 s post- The original aim of this study was to assess the repre-
stimulus that was marginally significant (Fig. 2, Extended sentational contents of the neural signals while the sub-
Data Fig. 2-1). This indicates that subjects moved their jects were engaged in VWM/imagery. We present these
eyes in a way consistent with the present stimulus, and results here, to demonstrate how they could easily have
kept it there for (cid:4)2–3 s. beenmistakenforgenuineresults,hadwebeenoblivious
| July/August2018,5(4)e0401-17.2018 |     |     |     |     |     |     |     |     |     |     |     |     |     | eNeuro.org |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |

|     |     |     |     |     |     |     |     |     |     |     |     | NewResearch | 7of14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- |
Figure 2. Gaze position classification results, cross-validation within VWM/imagery task. A, Temporal generalization matrix of
classificationperformanceintheVWMcondition.Thecolorscaledenotestheaverageposteriorprobabilitythatthedatabelongto
thesameclassasthepresentedstimulus.Thegrayoutlinedemarcatesanear-significantcluster(p(cid:7)0.069).Notethatthismatrix
isasymmetricbecauseonlytheVWMconditionisshown,whiletheclassifierwastrainedonthedatafromallVWM/MRconditions.
Forthisreason,thedataafter(cid:4)3sarenotexpectedtocontainsystematicpatternsandthereforethetrainingtimeaxishasbeen
truncated(ExtendedDataFig.2-1).B,Classificationperformanceaveragedoverthetrainingtimewindowof0.5–1.5s,separatelyfor
theVWMandthethreeMRconditions.Notethatthe0°conditioncorrespondsdirectlytothematrixinA.Thetwoverticaldashedlines
indicatestimulusandprobeonset.ShadedareasindicatetheSEM.Significantclustersareindicatedbythehorizontalbarsinthe
lower part of the figure. C, Average gaze position during 0.5–1.5 s after stimulus onset, separately per stimulus orientation. Each
transparent dot corresponds to an individual subject. The crosses are the grand averages, where the vertical and horizontal arms
denotetheSEM.Thethreecoloredlinesdepicttheorientationofthethreestimuli.
to the systematic eye movements. We constructed a over time in the three MR conditions (Fig. 4B). As ex-
three-class probabilistic classifier in which the MEG sen- plained in the previous paragraph, this indicates that the
| sors were | entered | as  | features. | As  | before, | the classifier |     |     |     |     |     |     |     |
| --------- | ------- | --- | --------- | --- | ------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
sustainedabove-chanceclassificationintheVWMcondi-
was trained on trials from all conditions (i.e., all amounts tioncannotbeexplainedasalong-lastingstimulus-driven
and directions of rotation) pooled together for maximum effect(e.g.,stimulusaftereffect),butmustalsoreflectthe
sensitivity (for rationale, see Materials and Methods). To memorized item to at least some degree. In the 180°
| test whether | we  | could | decode | stimulus | identity | from the |     |     |     |     |     |     |     |
| ------------ | --- | ----- | ------ | -------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
condition,theposteriorprobabilitythatthedatabelongto
MEGsignal,weappliedtheclassifiertothesame(pooled)
|     |     |     |     |     |     |     | the same | classes | as  | the | presented | stimulus | later re- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | --- | --- | --------- | -------- | --------- |
datausingcross-validationandfoundsuccessfuldecod- emerges as a rising, although nonsignificant trend. This
(cid:4)2.5
| ing during | a period | of  | up to | s   | after stimulus | onset |     |     |     |     |     |     |     |
| ---------- | -------- | --- | ----- | --- | -------------- | ----- | --- | --- | --- | --- | --- | --- | --- |
canbeexplainedbythefactthatthefinalorientationthat
| (Fig. 4, Extended |     | Data | Fig. | 4-1). The | stimulus | itself was |              |        |      |     |         |          |              |
| ----------------- | --- | ---- | ---- | --------- | -------- | ---------- | ------------ | ------ | ---- | --- | ------- | -------- | ------------ |
|                   |     |      |      |           |          |            | the subjects | should | have | in  | mind in | the 180° | condition is |
presentedforonly250ms.Therefore,thelaterpartofthis
identicaltotheorientationofthepresentedstimulusatthe
| period could  | have | be           | interpreted | as       | an endogenous | rep-          |               |        |                |     |          |          |        |
| ------------- | ---- | ------------ | ----------- | -------- | ------------- | ------------- | ------------- | ------ | -------------- | --- | -------- | -------- | ------ |
|               |      |              |             |          |               |               | start of a    | trial. |                |     |          |          |        |
| resentation,  | for  | instance     | stemming    |          | from          | active mental |               |        |                |     |          |          |        |
|               |      |              |             |          |               |               | To facilitate |        | interpretation |     | of these | results, | we in- |
| instantiation | by   | the subject, |             | although | in reality    | it is more    |               |        |                |     |          |          |        |
spectedtheclassifier’scorrespondingsensortopography
| likely to | be the    | result | of eye       | movements. |             |        |           |            |     |              |       |               |      |
| --------- | --------- | ------ | ------------ | ---------- | ----------- | ------ | --------- | ---------- | --- | ------------ | ----- | ------------- | ---- |
|           |           |        |              |            |             |        | (Fig. 4C) | and source |     | localization | (Fig. | 4D), averaged | over |
| Next,     | we looked | at     | the decoding |            | performance | in the |           |            |     |              |       |               |      |
VWM condition alone, using the classifier trained on all the training time period of 0.5–1.5 s. These indicate that
|     |     |     |     |     |     |     | both occipital |     | (Harrison | and | Tong, | 2009; Albers | et al., |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | --- | ----- | ------------ | ------- |
conditionsasdescribedabove.Wefoundthattheidentity
|                 |     |                   |     |          |        |            | 2013) and | prefrontal |             | sources | (Sreenivasan | et               | al., 2014; |
| --------------- | --- | ----------------- | --- | -------- | ------ | ---------- | --------- | ---------- | ----------- | ------- | ------------ | ---------------- | ---------- |
| of the memory   |     | item could        | be  | decoded  | during | the entire |           |            |             |         |              |                  |            |
|                 |     |                   |     |          |        |            | Spaak et  | al., 2017) | contributed |         | to           | the classifier’s | perfor-    |
| delay interval, |     | using classifiers |     | obtained | from   | a training |           |            |             |         |              |                  |            |
window of (cid:4)0.5–1.5 s (Fig. 4A). The performance stayed mance. Indeed, the prefrontal sources could in reality
above chance-level (33.3%) at a stable level of (cid:4)37% pointtoocularsources.Moreover,althoughthecontribu-
tionfromoccipitalregionsmayseemtoprovideevidence
| throughout | the | entire | interval | (Fig. 4B). |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ------ | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Again,wefoundthissustainedpatterntobespecificto that the decoder genuinely picks up visual representa-
theVWMcondition,becausetheprobabilitythatthedata tions,thesesourcescouldinfactalsobedrivenbytheeye
belongtothesameclassasthepresentedstimulusdrops movements (see Discussion).
| July/August2018,5(4)e0401-17.2018 |     |     |     |     |     |     |     |     |     |     |     |     | eNeuro.org |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- |

|     |     |     |     |     |     |     |     |     |     | NewResearch |     | 8of14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- |
Figure3.continued
orientationofthepresentedstimulus(cid:6)60°ortheorientationof
|     |     |     |     |     | the presented |     | stimulus | (cid:6)120°, | plotted | separately |     | for the four |
| --- | --- | --- | --- | --- | ------------- | --- | -------- | ------------ | ------- | ---------- | --- | ------------ |
VWM/MRconditions.Theplus/minussignisduetotheMRbeing
|     |     |     |     |     | performed | either | clockwise |     | or counterclockwise. |     |     | This figure |
| --- | --- | --- | --- | --- | --------- | ------ | --------- | --- | -------------------- | --- | --- | ----------- |
givesinsightintowhetherthefeaturepatternscorrespondingto
anyintermediateorientationsbecomeactiveduringMR,whichis
|     |     |     |     |     | particularly | relevant | for  | the              | 120° and | 180°       | conditions. | For in-     |
| --- | --- | --- | --- | --- | ------------ | -------- | ---- | ---------------- | -------- | ---------- | ----------- | ----------- |
|     |     |     |     |     | stance,      | in the   | 180° | counterclockwise |          | condition, |             | the subject |
wouldstartwithamentalimagewiththesameorientationasthe
|     |     |     |     |     | presented | stimulus, | then | pass | through, | respectively, |     | -60° and |
| --- | --- | --- | --- | --- | --------- | --------- | ---- | ---- | -------- | ------------- | --- | -------- |
-120°,ultimatelytoreachthetargetof-180°(i.e.,0°).Ifthegaze
positionscorrespondingtoalltheseorientationsbecomeactive
|     |     |     |     |     | in sequence, | one | would | first | expect | a peak | in posterior | proba- |
| --- | --- | --- | --- | --- | ------------ | --- | ----- | ----- | ------ | ------ | ------------ | ------ |
bilitythatthedatabelongtothesameclassasthestimulus(gray
line,bottomfigure),thenapeakintheprobabilityofbelongingto
|     |     |     |     |     | the presented |     | stimulus | -60° | (orange | line), | then for | -120° (blue |
| --- | --- | --- | --- | --- | ------------- | --- | -------- | ---- | ------- | ------ | -------- | ----------- |
line),andfinallyagainfor0°(grayline).Itisimportanttorealize
thatbelow-chanceprobabilitiesintheseanalysesaremeaning-
ful.Forinstance,considerA.Here,theprobabilitythatthedata
belongtothesameclassasthetargetisplotted.Hence,inthe
60°and120°conditions,theclassifiercorrectlyidentifiesthatthe
|     |     |     |     |     | data do   | not belong |           | to the  | same | class as     | the         | target in the |
| --- | --- | --- | --- | --- | --------- | ---------- | --------- | ------- | ---- | ------------ | ----------- | ------------- |
|     |     |     |     |     | beginning | of the     | interval, | because |      | the starting | orientation | was           |
different.Asanotherexample,considertheredlineinthesecond
panelinB.Thislineplotstheprobabilitythatthedatabelongto
|     |     |     |     |     | the starting | orientation |            | (cid:6)60°. | On presentation |        | of            | the starting |
| --- | --- | --- | --- | --- | ------------ | ----------- | ---------- | ----------- | --------------- | ------ | ------------- | ------------ |
|     |     |     |     |     | orientation, | the         | classifier | therefore   |                 | yields | a significant | below-       |
chanceprobability.However,asthesubjectperformsthe(cid:6)60°
|     |     |     |     |     | rotation | over the | course | of  | the trial, | the classifier |     | increasingly |
| --- | --- | --- | --- | --- | -------- | -------- | ------ | --- | ---------- | -------------- | --- | ------------ |
picksupthisrotatedimage,hencegivingabove-chanceproba-
|     |     |     |     |     | bilities. Note | that       | A, B, | as well   | asFigure | 2,     | all depict | the same     |
| --- | --- | --- | --- | --- | -------------- | ---------- | ----- | --------- | -------- | ------ | ---------- | ------------ |
|     |     |     |     |     | data but       | visualized | in    | different | manners. | Shaded |            | areas denote |
theSEMandsignificantclustersaredepictedbythethickhori-
zontallinesatthebottomofthepanels.
|     |     |     |     |     | Finally, | we  | investigated |     | whether | we  | could | decode the |
| --- | --- | --- | --- | --- | -------- | --- | ------------ | --- | ------- | --- | ----- | ---------- |
intermediate(forthe120°and180°rotations)andthefinal
|     |     |     |     |     | orientations | in  | the MR | conditions.  |     | We      | found | some indi-   |
| --- | --- | --- | --- | --- | ------------ | --- | ------ | ------------ | --- | ------- | ----- | ------------ |
|     |     |     |     |     | cation that  | the | final  | orientation, |     | but not | the   | intermediate |
ones(Fig.5B),indeedemergeshalfwaythroughthedelay
period,butthiseffectwasnotstatisticallysignificant(Fig.
5A).
|     |     |     |     |     | Decoding   | visual    | representations |            |             | from         | sensory | areas       |
| --- | --- | --- | --- | --- | ---------- | --------- | --------------- | ---------- | ----------- | ------------ | ------- | ----------- |
|     |     |     |     |     | In a third | analysis, |                 | we trained |             | a continuous |         | orientation |
|     |     |     |     |     | decoder    | (see      | Materials       | and        | Methods)    |              | on the  | functional  |
|     |     |     |     |     | localizer  | data      | (Fig. 1B,C)     |            | and applied |              | these   | decoders to |
thedatafromtheVWM/imagerytask(KingandDehaene,
|           |          |      |                         |                 | 2014). The | main | advantage |              | of this   | method    |           | is that it en- |
| --------- | -------- | ---- | ----------------------- | --------------- | ---------- | ---- | --------- | ------------ | --------- | --------- | --------- | -------------- |
|           |          |      |                         |                 | sures that | the  | decoder   | is           | primarily | sensitive |           | to sensory     |
| Figure 3. | Complete | gaze | position classification | results. Analo- |            |      |           |              |           |           |           |                |
|           |          |      |                         |                 | signals,   | and  | not to    | higher-level |           | top-down  | processes | in-            |
gouslytoFigure2,theclassifierwastrainedonthetimewindow
volvedinmentalmanipulationofanimage.Itthusallows
of0.5–1.5safterstimulusonset,andaccordingtothelabelsof
|     |     |     |     |     | us to track |     | sensory-specific |     | activation |     | throughout | the |
| --- | --- | --- | --- | --- | ----------- | --- | ---------------- | --- | ---------- | --- | ---------- | --- |
thepresentedstimulus.A,Averageposteriorprobabilitythatthe
data belong to the class of the target orientation, that is, the delayperiod(Mostertetal.,2015).Cross-validationwithin
orientationthatthesubjectsweresupposedtohaveinmindat the functional localizer confirmed that we were indeed
the end of the delay period. For both the 0° and the 180° able to reliably decode orientation-specific information
conditions,thetargetorientationwasthesameasthepresented fromactivityevokedbypassivelyperceivedgratings(Fig.
stimulus. For the 60° and 120° conditions, however, the target 6,ExtendedDataFig.6-1).Moreover,wewerenotableto
andpresentedstimulusweredifferent,hencethebelow-chance
|     |     |     |     |     | decode | grating | orientation |     | on the | basis | of gaze | position, |
| --- | --- | --- | --- | --- | ------ | ------- | ----------- | --- | ------ | ----- | ------- | --------- |
probabilitiesatthebeginningofthedelayperiod.B,Theaverage
|                                   |               |             |                  |                    | verifying        | that | the data | from              | the | functional | localizer | were       |
| --------------------------------- | ------------- | ----------- | ---------------- | ------------------ | ---------------- | ---- | -------- | ----------------- | --- | ---------- | --------- | ---------- |
| posterior                         | probabilities | that        | the data belong  | to either of three |                  |      |          |                   |     |            |           |            |
|                                   |               |             |                  |                    | not contaminated |      | by       | stimulus-specific |     |            | eye       | movements  |
| classes:                          | the same      | orientation | as the presented | stimulus, the      |                  |      |          |                   |     |            |           |            |
|                                   |               |             |                  |                    | (Extended        | Data | Fig.     | 6-2).             |     |            |           |            |
| July/August2018,5(4)e0401-17.2018 |               |             |                  |                    |                  |      |          |                   |     |            |           | eNeuro.org |

|     |     |     |     |     |     | NewResearch | 9of14 |
| --- | --- | --- | --- | --- | --- | ----------- | ----- |
Figure4.MEGclassificationresults.A,SameasinFigure2A,excepttheclassificationwasperformedonMEGdata,ratherthanon
(cid:7)
gaze position. The black outline demarcates a significant cluster (p 0.006). B, Same as in Figure 2B, except the analysis was
performedonMEGdata.Syntheticplanargradiometertopography(C)andsourcetopography(D)ofareasthatcontributedtothe
classifier.SeealsoExtendedDataFigure4-1.
In the VWM condition, the decoders trained on the averagedacrosstrainingtime90–120ms.Thesehighlight
functional localizer data could reliably decode the orien- primarilyoccipitalregionsascontributingtothedecoder’s
tationofthepresentedstimulus(Fig.6A).Moreover,fora performance, consistent with our premise that the func-
trainingtimeof(cid:4)90–120ms,wecoulddecodethestim-
|     |     |     |     | tional localizer | primarily induced | bottom-up sensory | sig- |
| --- | --- | --- | --- | ---------------- | ----------------- | ----------------- | ---- |
ulus for a prolonged time, lasting over 1 s after stimulus nals, especially during this early time interval (Mostert
| onset.Interestingly,thistrainingtimepointcoincideswith |     |     |     | et al., 2015). |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | -------------- | --- | --- | --- |
thetimeatwhichpeakperformanceisobtainedwithinthe In summary, our findings suggest that the stable, per-
localizer itself (Extended Data Fig. 6-1). Comparing the sistent representation found in our within-task MEG de-
decoding trace within this training time window with the coding result may well be attributed to stimulus-specific
three MR conditions, it can be seen that grating orienta- eyemovements,althoughthemagnitudeoftheeyemove-
tioncanbedecodedinallfourconditionsforasustained mentswereonlysmall.Incontrast,noclearevidencewas
period of (cid:4)500 ms (Fig. 6B). This is in sharp contrast to foundforsuchalong-lastingrepresentationwhentraining
the extended decoding of the presented stimulus the decoder on the functional localizer. Given that the
throughouttheentiredelayperiod,foundwithintheVWM/ localizer was not contaminated by stimulus-specific eye
imagery task using cross-validation (Fig. 4). movements, these results thus provide a more reliable
We inspected the spatial pattern (Fig. 6C) and corre- picture of the sensory representations during the delay
| sponding source                   | topography | (Fig. 6D) | for the decoders, | interval. |     |            |     |
| --------------------------------- | ---------- | --------- | ----------------- | --------- | --- | ---------- | --- |
| July/August2018,5(4)e0401-17.2018 |            |           |                   |           |     | eNeuro.org |     |

NewResearch 10of14
Figure5.CompleteMEGclassificationresults,visualizedinavarietyofways.ThisfigureisanalogoustoFigure3,excepttheclassifier
istrainedandtestedonMEGdataratherthanongazeposition.
July/August2018,5(4)e0401-17.2018 eNeuro.org

|     |     |     |     |     |     |     |     |     |     | NewResearch | 11of14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ |
Figure6.MEGdecodingresults,generalizedfromlocalizertoVWM/imagerytask.A,Temporalgeneralizationmatrixoforientation
decodingperformance,forwhichthedecoderwastrainedonalltimepointsinthefunctionallocalizerandtestedacrossalltimepoints
in the VWM/imagery task. The color scale reflects the correspondence between true and decoded orientation. The black outline
shows a significant cluster (p (cid:7) 0.04). Note that the x- and y-axis in the figure are differently scaled for optimal visualization. B,
Decoding performance over time in the VWM/imagery task, averaged over decoders trained in the window of 0.09–0.12 s in the
localizer,separatelyfortheVWMandthreeMRconditions.ShadedareasdenotetheSEM,andsignificantclustersareindicatedby
thehorizontalbars.Syntheticplanargradiometertopography(C)andsourcetopography(D)ofareasthatcontributetothedecoder.
SeealsoExtendedDataFigures6-1,6-2.
Discussion sensible, because very similar results could be obtained
|     |     |     |     |     |     |     | by considering | gaze position | only. |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------------- | ----- | --- | --- |
Neuraldecodingisapowerfulandpromisingtechnique
for neuroimaging studies (Haxby et al., 2014; Grootswa- Thereareatleastthreepossiblemechanismsviawhich
gersetal.,2017)thathasledtosubstantialadvancement stimulus-specific eye movements may confound our re-
|     |     |     |     |     |     |     | sults. First, | eye movements | are | known | to cause stereo- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------------- | --- | ----- | ---------------- |
inthefieldofVWMoverrecentyears(HarrisonandTong,
|                |     |         |       |           |            |       | typical | artifacts in MEG | recordings. | Due | to the positively |
| -------------- | --- | ------- | ----- | --------- | ---------- | ----- | ------- | ---------------- | ----------- | --- | ----------------- |
| 2009; Serences |     | et al., | 2009; | Albers et | al., 2013; | Wolff |         |                  |             |     |                   |
chargedcorneaandnegativelychargedretina,theeyeball
| et al., 2015, | 2017). | This | study | also employed |     | neural de- |         |                    |        |       |             |
| ------------- | ------ | ---- | ----- | ------------- | --- | ---------- | ------- | ------------------ | ------ | ----- | ----------- |
|               |        |      |       |               |     |            | acts as | an electromagnetic | dipole | whose | rotation is |
codingtechniques,withtheoriginalaimtoinvestigatethe
|          |          |     |         |                 |     |        | picked | up by the MEG sensors. |     | The spatial | pattern that |
| -------- | -------- | --- | ------- | --------------- | --- | ------ | ------ | ---------------------- | --- | ----------- | ------------ |
| temporal | dynamics | of  | sensory | representations |     | during |        |                        |     |             |              |
thedipoleevokesisdirectlyrelatedtoitsangle,orinother
VWM. However, we found that our data were contami- words,tothepositionofthesubject’sgaze(Plöchletal.,
| nated by | small but | systematic |     | eye movements, |     | whereby |     |     |     |     |     |
| -------- | --------- | ---------- | --- | -------------- | --- | ------- | --- | --- | --- | --- | --- |
2012).Thus,ifthesubjectmoveshis/hereyesinresponse
| gaze position | was | related | to  | the stimulus | held | in mind. |     |     |     |     |     |
| ------------- | --- | ------- | --- | ------------ | ---- | -------- | --- | --- | --- | --- | --- |
tothegratinginamannerrelatedtotheorientationofthat
Thisjeopardizedourabilitytointerprettheneuraldecod- grating,thenthiswillinduceaspecificpatternintheMEG
ing results, results that otherwise would have seemed signals, which in turn is directly related to the grating
| July/August2018,5(4)e0401-17.2018 |     |     |     |     |     |     |     |     |     |     | eNeuro.org |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- |

NewResearch 12of14
orientation. A decoding analysis applied to these signals our decoding results do in reality stem from genuine
isthenlikelytopickupthepatternsevokedbytheeyeball orientationinformationencodedintrueneuralsources.In
dipoles, confounding potential orientation-related infor- fact, we used independent component analysis in our
mation stemming from genuine neural sources. In fact, pre-processing pipeline to (presumably) remove eye-
oursourceanalysishintsatthisscenario(Fig.4D),asthe movementartifacts.However,itwouldbeverydifficult,if
contributions from presumed prefrontal sources closely notimpossible,toconvincinglyestablishthatnoartifacts
resemble an ocular source. remain and, considering the similarities between the de-
Second,iftheeyesmove,thentheprojectionfallingon codingresultsfromtheMEGdata(Fig.4A,B)andthegaze
the retina will also change, even when external visual position(Fig.2A,B),wefeelanyattemptsatthiswouldbe
stimulation remains identical. Thus, if gaze position is unwarranted.
systematically modulated by the image that is perceived Given the potential pervasiveness of systematic eye
orkeptinmind,thensoisthevisualinformationtransmit- movements in VWM/imagery tasks, and the demon-
ted to the visual cortex. For example, if a vertical grating strated susceptibility of our analysis methods to these
is presented and kept in VWM, then the subject may confounds,onewonderswhetherotherstudiesmayhave
subtlymoveherorhisgazeupward.Correspondingly,the been similarly affected. Clearly, the first mechanism de-
fixation dot is now slightly below fixation, thus leading to scribed above involving the eyeball dipole would only
visual cortex activity that is directly related to the retino- affect electrophysiological measurements like electroen-
topic position of the fixation dot. Our decoding analysis cephalographyandMEG,andhasindeedbeenaconcern
maythusactuallydecodethepositionofthefixationdot, in practice (Foster et al., 2016). The second mechanism
rather than grating orientation, potentially leading to an however, whereby stimulus identity is confounded with
incorrect conclusion. Source analysis would in this sce- theretinalpositionofvisualinput,wouldalsoaffectother
nario also point to occipital sources, similarly to what we neuroimaging techniques such as fMRI. This confound
found (Fig. 4D). Note that this mechanism is not specifi- could be particularly difficult to recognize, because it
cally dependent on the presence of a fixation dot. A would also affect activity in visual areas. Moreover, be-
systematic difference in eye position will also lead to causeeyemovementsduringimageryhavebeenfoundto
changes in the retinotopic position of, for instance, the be positively related to performance (Laeng and Teodor-
presentation display or the optically visible part of the escu, 2002), this could potentially explain correlations
MEG helmet. between VWM decoding and behavioral performance.
Third, if gaze position covaries with the mental image, Thethirdmechanism,wherebyonedirectlydecodesgaze
then decoding of the mental image will also reveal areas positionfrommotorareas,couldbeaproblemespecially
that encode eye gaze position, such as oculomotor re- forfMRIwhich,thankstoitshighspatialresolution,might
gions in parietal and prefrontal cortex. be well able to decode such subtle neural signals. This
Ourfindingsraisethequestionofwhythereweretask- concernmaybeespeciallyrelevantforstudiesthatinves-
induced eye movements that were directly related to the tigate the role of areas involved in eye movements or
gratingkeptinVWM.Infact,thereisaconsiderablemass planning thereof, such as frontal eye fields or superior
of literature that describes the role of eye movements in precentralsulcus,inthemaintenanceofworkingmemory
mental imagery. It has been found that subjects tend to items (Jerde et al., 2012; Ester et al., 2015; Christophel
make similar eye movements during imagery as during et al., 2017).
perceptionofthesamestimulus(BrandtandStark,1997; Thisleavesthequestionofhowtodealwitheyemove-
LaengandTeodorescu,2002;Laengetal.,2014).Already mentsinVWM/imagerytasks.Naturally,itisimportantto
proposedbyDonaldHebb(Hebb,1968),itisnowthought record eye movements during the experiment, for in-
that eye movements serve to guide the mental recon- stanceusinganeye-trackerorEOG.Onecanthentestfor
structionofanimaginedstimulus,possiblybydwellingon any systematic relationship and, if found, investigate
salientpartsoftheimage(SpiveyandGeng,2001;Laeng whether it could confound the main results. In our case,
et al., 2014). Moreover, the specificity of the eye move- forexample,decodingofgazepositionleadstostrikingly
ments is also related to neural reactivation (Bone et al., similar results as those obtained from the MEG data.
2017)andrecallaccuracy(LaengandTeodorescu,2002; Fosteretal.(2016)ontheotherhandfoundthatdecoding
Laeng et al., 2014; Bone et al., 2017). Our findings are in performance of working memory items decreased
accordancewiththesestudies.Subjects’gazewasposi- throughout the trial, whereas the deviation in gaze posi-
tionedalongtheorientationaxisofthegrating-thatis,the tion increased, suggesting that eye confounds cannot
visuallocationwithinthestimulusthatprovidedthehigh- explain the main findings. Another approach might be to
est information regarding its orientation and is thus ex- design the experimental task in such a way that eye
actly what one would expect given that the task was to movements are less likely. For example, by presenting
make a fine-grained orientation comparison with a probe gratings laterally (Pratte and Tong, 2014; Ester et al.,
grating.Importantly,however,subjectswereexplicitlyin- 2015; Wolff et al., 2017), and assuming that VWM items
structedtomaintainfixationthroughouttheentiretrial.We arestoredinaretinotopicallyspecificmanner(Pratteand
nevertheless observed that not all subjects adhered to Tong,2014),theinvoluntarytendencytomoveone’seyes
this requirement, albeit involuntarily. subtly along the remembered grating’s orientation axis
Despitetheseproblemsassociatedwiththesystematic may become less strong, because those gratings are
eye movements in our experiment, it is still possible that locateddistantlyfromthegaze’sinitiallocation(i.e.,cen-
July/August2018,5(4)e0401-17.2018 eNeuro.org

|     |     |     |     |     |     |     |     |     |     |     |     | NewResearch |     |     | 13of14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | ------ |
tral fixation). Finally, a powerful approach could be to decoding performance (cf. the second mechanism de-
adopt a separate functional localizer, which allows spe- scribedabove).Furthermore,itisimportanttorealizethat
|                |     |                 |     |     |         |                 |     |     | this does | not necessarily | invalidate |     | all previous |     | studies. |
| -------------- | --- | --------------- | --- | --- | ------- | --------------- | --- | --- | --------- | --------------- | ---------- | --- | ------------ | --- | -------- |
| cific decoding |     | of functionally |     |     | defined | representations |     |     |           |                 |            |     |              |     |          |
such as bottom-up, sensory-specific signals (Harrison Whilesomepreviousresultsmayhavebeenafflicted,our
andTong,2009;Serencesetal.,2009;Albersetal.,2013; current understanding of the neural underpinnings of
Mostert et al., 2015). If the localizer is well designed and VWMisstillfirmlygroundedinconvergingevidencefrom
notsystematicallycontaminatedbyeyemovements,then a wide variety of techniques, paradigms and modalities.
Nevertheless,weconcludethateyemovementconfounds
eyemovementsinthemaintaskcannothaveasystematic
effect on the decoded signal, thus effectively filtering shouldbetakenseriouslyinboththedesignaswellasthe
| them out.   |     |             |     |         |              |     |           |     | analysis | phase of future | studies. |     |     |     |     |
| ----------- | --- | ----------- | --- | ------- | ------------ | --- | --------- | --- | -------- | --------------- | -------- | --- | --- | --- | --- |
| We designed |     | a localizer |     | that is | specifically |     | sensitive | to  |          |                 |          |     |     |     |     |
References
| the neural | representations |     |     | encoded | in  | bottom-up | signals |     |     |     |     |     |     |     |     |
| ---------- | --------------- | --- | --- | ------- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
evoked by passively perceived gratings. This allowed us AlbersAM,KokP,ToniI,DijkermanHC,deLangeFP(2013)Shared
toaddressthequestionofwhethertheimaginedstimulus representationsforworkingmemoryandmentalimageryinearly
wasencodedwithasimilarneuralcodeastheperceived visualcortex.CurrBiol23:1427–1431.CrossRefMedline
gratings (Harrison and Tong, 2009; Albers et al., 2013). Bastiaansen MCM, Knösche TR (2000) Tangential derivative map-
|     |     |     |     |     |     |     |     |     | ping of | axial MEG applied | to  | event-related |     | desynchronization |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------------- | --- | ------------- | --- | ----------------- | --- |
Using this localizer, we indeed obtained MEG decoding research.ClinNeurophysiol111:1300–1305.CrossRef
resultsthatwereverydissimilarfromthoseobtainedusing BerensP(2009)CircStat:aMATLABtoolboxforcircularstatistics.J
cross-validationwithinthecombinedVWM/imagerytask. Stat Softw 31. Available at https://www.jstatsoft.org/v031/i10.
| Wenolongerfoundpersistentactivationofanorientation- |     |     |     |     |     |     |     |     | CrossRef  |                |             |     |         |           |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | ----------- | --- | ------- | --------- | --- |
|                                                     |     |     |     |     |     |     |     |     | Bishop CM | (2006) Pattern | recognition | and | machine | learning. | New |
specificrepresentationthroughouttheentiredelayperiod.
York:Springer.
Nevertheless,thesensorypatterndidremainabovebase-
BlankertzB,LemmS,TrederM,HaufeS,MüllerK-R(2011)Single-
| line for   | a period | of (cid:4)1 | s, which |           | is relatively | long     | consid- |     |                |                    |     |        |              |     |           |
| ---------- | -------- | ----------- | -------- | --------- | ------------- | -------- | ------- | --- | -------------- | ------------------ | --- | ------ | ------------ | --- | --------- |
|            |          |             |          |           |               |          |         |     | trial analysis | and classification |     | of ERP | components—a |     | tutorial. |
| ering that | the      | stimulus    | was      | presented |               | for only | 250     | ms. |                |                    |     |        |              |     |           |
Neuroimage56:814–825.CrossRefMedline
| One explanation |     | is that | the | stimulus | was | relevant | for | the |     |     |     |     |     |     |     |
| --------------- | --- | ------- | --- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
BoneMB,St-LaurentM,DangC,McQuigganDA,RyanJD,Buchs-
baumBR(2017)Eye-movementreinstatementandneuralreacti-
| task. Previous |     | work | has shown |     | that task | relevance |     | may |     |     |     |     |     |     |     |
| -------------- | --- | ---- | --------- | --- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
vationduringmentalimagery.bioRxiv107953.
| keep the    | sensory | representation |          |     | online    | for | a prolonged |     |                |                 |             |        |               |        |        |
| ----------- | ------- | -------------- | -------- | --- | --------- | --- | ----------- | --- | -------------- | --------------- | ----------- | ------ | ------------- | ------ | ------ |
|             |         |                |          |     |           |     |             |     | Brandt SA,     | Stark LW (1997) | Spontaneous |        | eye movements |        | during |
| period even | after   | the            | stimulus | is  | no longer | on  | the screen  |     |                |                 |             |        |               |        |        |
|             |         |                |          |     |           |     |             |     | visual imagery | reflect the     | content     | of the | visual        | scene. | J Cogn |
| (Mostert    | et al., | 2015).         |          |     |           |     |             |     |                |                 |             |        |               |        |        |
Neurosci9:27–38.CrossRefMedline
Itshouldbepointedoutthatusingafunctionallocalizer Brouwer GJ, Heeger DJ (2009) Decoding and reconstructing color
alsohasitsintrinsiclimitations.Themostimportantbeing from responses in human visual cortex. J Neurosci 29:13992–
that, while such an approach is primarily sensitive to a 14003.CrossRefMedline
functionally defined signal, it may at the same time be Brouwer GJ, Heeger DJ (2011) Cross-orientation suppression in
blind to other relevant signals that were not a priori in- human visual cortex. J Neurophysiol 106:2108–2119. CrossRef
Medline
cluded in the functional definition. The VWM literature Christophel TB, Cichy RM, Hebart MN, Haynes JD (2015) Parietal
itselfprovidesaninstructiveexample:whilethefunctional andearlyvisualcorticesencodeworkingmemorycontentacross
localizerapproachhasclearlydemonstratedsensoryrep- mental transformations. Neuroimage 106:198–206. CrossRef
| resentations     | of  | the memorandum |       |       | in associated |     | sensory     |     | Medline     |              |            |     |        |           |       |
| ---------------- | --- | -------------- | ----- | ----- | ------------- | --- | ----------- | --- | ----------- | ------------ | ---------- | --- | ------ | --------- | ----- |
|                  |     |                |       |       |               |     |             |     | Christophel | TB, Allefeld | C, Endisch | C,  | Haynes | JD (2017) | View- |
| cortex (Harrison |     | and            | Tong, | 2009; | Albers        | et  | al., 2013), | it  |             |              |            |     |        |           |       |
independentworkingmemoryrepresentationsofartificialshapes
| would have | missed |     | relevant | encoding |     | in other   | regions | in     |               |               |         |     |           |        |       |
| ---------- | ------ | --- | -------- | -------- | --- | ---------- | ------- | ------ | ------------- | ------------- | ------- | --- | --------- | ------ | ----- |
|            |        |     |          |          |     |            |         |        | in prefrontal | and posterior | regions | of  | the human | brain. | Cereb |
| the brain  | such   | as  | parietal |          | and | prefrontal |         | cortex |               |               |         |     |           |        |       |
Cortex28:2146–2161.
(Christopheletal.,2015,2017).Furthermore,thefactthat
EsterEF,SpragueTC,SerencesJT(2015)Parietalandfrontalcortex
thedecodersweretrainedonafunctionallydefinedsignal encodestimulus-specificmnemonicrepresentationsduringvisual
workingmemory.Neuron87:893–905.CrossRefMedline
| does not       | mean | that | they   | are necessarily  |     | insensitive |          | to  |            |                       |          |           |     |              |         |
| -------------- | ---- | ---- | ------ | ---------------- | --- | ----------- | -------- | --- | ---------- | --------------------- | -------- | --------- | --- | ------------ | ------- |
|                |      |      |        |                  |     |             |          |     | Foster JJ, | Sutterer DW, Serences |          | JT, Vogel | EK, | Awh E (2016) | The     |
| other signals, |      | such | as eye | movement-related |     |             | signals. |     |            |                       |          |           |     |              |         |
|                |      |      |        |                  |     |             |          |     | topography | of alpha-band         | activity | tracks    | the | content of   | spatial |
However,itisimportanttorealizethattheexacteffectof
workingmemory.JNeurophysiol115:168–177.CrossRefMedline
theseothersignalsonthedecoder’soutputisnotexplic-
|     |     |     |     |     |     |     |     |     | Garcı´´a-Pérez | MA (1998) | Forced-choice |     | staircases | with fixed | step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | ------------- | --- | ---------- | ---------- | ---- |
itly defined. These potential effects would therefore be sizes: asymptotic and small-sample properties. Vision Res 38:
idiosyncratic to an individual’s data and are expected to 1861–1881.CrossRef
cancel out at the group level. GayetS,GuggenmosM,ChristophelTB,HaynesJ-D,PaffenCLE,
In summary, we demonstrate a case where decoding van der Stigchel S, Sterzer P (2017) Visual working memory en-
hancestheneuralresponsetomatchingvisualinput.JNeurosci
| analyses | in a VWM/imagery |     |     | task | are heavily |     | confounded |     |     |     |     |     |     |     |     |
| -------- | ---------------- | --- | --- | ---- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
37:6638–6647.CrossRef
by systematic eye movements. Given the high potential GrootswagersT,WardleSG,CarlsonTA(2017)Decodingdynamic
benefit of decoding analyses and its widespread use in brain patterns from evoked responses: a tutorial on multivariate
the study of working memory and mental imagery, we patternanalysisappliedtotimeseriesneuroimagingdata.JCogn
argue that this problem may be more pervasive than is Neurosci29:677–697.CrossRef
HarrisonSA,TongF(2009)Decodingrevealsthecontentsofvisual
| commonly | appreciated. |     | Future | studies |     | could | target | this |     |     |     |     |     |     |     |
| -------- | ------------ | --- | ------ | ------- | --- | ----- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- |
workingmemoryinearlyvisualareas.Nature458:632–635.Cross-
questionspecificallyandinvestigatehowstrongthecon-
RefMedline
| founds | are exactly. | One | approach |     | could | be to | systemat- |     |     |     |     |     |     |     |     |
| ------ | ------------ | --- | -------- | --- | ----- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
HaufeS,MeineckeF,GörgenK,DähneS,HaynesJ-D,BlankertzB,
ically vary salient input and assess how this impacts BießmannF(2014)Ontheinterpretationofweightvectorsoflinear
| July/August2018,5(4)e0401-17.2018 |     |     |     |     |     |     |     |     |     |     |     |     |     | eNeuro.org |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |

|     |     |     |     |     |     |     |     |     |     |     | NewResearch |     | 14of14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------ |
models in multivariate neuroimaging. Neuroimage 87:96–110. Plöchl M, Ossandón JP, König P (2012) Combining EEG and eye
CrossRefMedline tracking: identification, characterization, and correction of eye
HaxbyJV,ConnollyAC,GuntupalliJS(2014)Decodingneuralrep- movement artifacts in electroencephalographic data. Front Hum
resentationalspacesusingmultivariatepatternanalysis.AnnuRev Neurosci6:278.CrossRef
Neurosci37:435–456.CrossRefMedline Pratte MS, Tong F (2014) Spatial specificity of working memory
Hebb DO (1968) Concerning imagery. In: Images, perception, and representations in the early visual cortex. J Vis 14:22. CrossRef
Medline
knowledge,pp139–153.Dordrecht:Springer.
|           |         |             |     |        |     |           |        | Rademaker | RL, Serences | JT (2017) | Pinging | the brain | to reveal |
| --------- | ------- | ----------- | --- | ------ | --- | --------- | ------ | --------- | ------------ | --------- | ------- | --------- | --------- |
| Jerde TA, | Merriam | EP, Riggall | AC, | Hedges | JH, | Curtis CE | (2012) |           |              |           |         |           |           |
hiddenmemories.NatNeurosci20:767–769.CrossRefMedline
Prioritizedmapsofspaceinhumanfrontoparietalcortex.JNeu-
RoseNS,LaRocqueJJ,RiggallAC,GosseriesO,StarrettMJ,Mey-
rosci32:17382–17390.CrossRefMedline
eringEE,PostleBR(2016)Reactivationoflatentworkingmemo-
| King JR, Dehaene |     | S (2014) | Characterizing |     | the dynamics | of  | mental |     |     |     |     |     |     |
| ---------------- | --- | -------- | -------------- | --- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- |
representations:thetemporalgeneralizationmethod.TrendsCogn ries with transcranial magnetic stimulation. Science 354:1136–
| Sci18:203–210.CrossRefMedline |     |     |     |     |     |     |     | 1139.CrossRefMedline |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- |
KingJR,PescetelliN,DehaeneS(2016)Brainmechanismsunder- Serences JT, Ester EF, Vogel EK, Awh E (2009) Stimulus-specific
lyingthebriefmaintenanceofseenandunseensensoryinforma- delayactivityinhumanprimaryvisualcortex.PsycholSci20:207–
| tion.Neuron92:1122–1134.CrossRefMedline |     |     |     |     |     |     |     | 214.CrossRefMedline |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- |
SpaakE,WatanabeK,FunahashiS,StokesMG(2017)Stableand
| Kleiner M, | Brainard | D, Pelli | D, Ingling | A,  | Murray | R, Broussard | C   |     |     |     |     |     |     |
| ---------- | -------- | -------- | ---------- | --- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- |
dynamiccodingforworkingmemoryinprimateprefrontalcortex.
(2007)What’snewinPsychtoolbox-3.Perception36:1.
JNeurosci37:6503–6516.CrossRefMedline
| Kok P, Mostert | P,      | de Lange   | FP (2017) | Prior     | expectations |         | induce |            |                |            |            |           |     |
| -------------- | ------- | ---------- | --------- | --------- | ------------ | ------- | ------ | ---------- | -------------- | ---------- | ---------- | --------- | --- |
|                |         |            |           |           |              |         |        | Spivey MJ, | Geng JJ (2001) | Oculomotor | mechanisms | activated | by  |
| prestimulus    | sensory | templates. |           | Proc Natl | Acad         | Sci USA | 114:   |            |                |            |            |           |     |
imageryandmemory:eyemovementstoabsentobjects.Psychol
10473–10478.
Res65:235–241.Medline
LaengB,TeodorescuDS(2002)Eyescanpathsduringvisualimagery
SreenivasanKK,CurtisCE,D’EspositoM(2014)Revisitingtheroleof
| reenact those | of  | perception | of the | same | visual | scene. Cogn | Sci |     |     |     |     |     |     |
| ------------- | --- | ---------- | ------ | ---- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
persistentneuralactivityduringworkingmemory.TrendsCognSci
26:207–231.CrossRef
18:82–89.CrossRef
| Laeng B, Bloem | IM, | D’Ascenzo | S,  | Tommasi | L (2014) | Scrutinizing |     |     |     |     |     |     |     |
| -------------- | --- | --------- | --- | ------- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
StokesMG(2015)‘Activity-silent’workingmemoryinprefrontalcor-
visual images: the role of gaze in mental imagery and memory. tex:adynamiccodingframework.TrendsCognSci19:394–405.
| Cognition131:263–283.CrossRefMedline |     |     |     |     |     |     |     | CrossRefMedline |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
Manahova ME, Mostert P, Kok P, Schoffelen J-M, de Lange FP StokesMG,KusunokiM,SigalaN,NiliH,GaffanD,DuncanJ(2013)
(2017)Stimulusfamiliarityandexpectationjointlymodulateneural Dynamiccodingforcognitivecontrolinprefrontalcortex.Neuron
activityinthevisualventralstream.bioRxiv192518. 78:364–375.CrossRefMedline
| Maris E, Oostenveld |     | R (2007) | Nonparametric |     | statistical | testing | of  |          |                   |             |     |           |          |
| ------------------- | --- | -------- | ------------- | --- | ----------- | ------- | --- | -------- | ----------------- | ----------- | --- | --------- | -------- |
|                     |     |          |               |     |             |         |     | Van Veen | BD, van Drongelen | W, Yuchtman |     | M, Suzuki | A (1997) |
EEG-andMEG-data.JNeurosciMethods164:177–190.CrossRef
Localizationofbrainelectricalactivityvialinearlyconstrainedmin-
Medline
|            |        |          |           |              |     |         |      | imum variance | spatial | filtering. IEEE | Trans | Biomed Eng | 44:867– |
| ---------- | ------ | -------- | --------- | ------------ | --- | ------- | ---- | ------------- | ------- | --------------- | ----- | ---------- | ------- |
| Mostert P, | Kok P, | de Lange | FP (2015) | Dissociating |     | sensory | from |               |         |                 |       |            |         |
880.CrossRefMedline
decisionprocessesinhumanperceptualdecisionmaking.SciRep
|     |     |     |     |     |     |     |     | Wolff MJ, | Ding J, Myers | NE, Stokes | MG (2015) | Revealing | hidden |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | ---------- | --------- | --------- | ------ |
5:18253.CrossRefMedline states in visual working memory using electroencephalography.
OostenveldR,FriesP,MarisE,SchoffelenJM(2011)FieldTrip:open FrontSystNeurosci9:123.
sourcesoftwareforadvancedanalysisofMEG,EEG,andinvasive WolffMJ,JochimJ,AkyürekEG,StokesMG(2017)Dynamichidden
electrophysiological data. Comput Intell Neurosci 2011:156869. statesunderlyingworking-memory-guidedbehavior.NatNeurosci
| CrossRef                          |     |     |     |     |     |     |     | 20:864–871. |     |     |     |     |            |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | ---------- |
| July/August2018,5(4)e0401-17.2018 |     |     |     |     |     |     |     |             |     |     |     |     | eNeuro.org |