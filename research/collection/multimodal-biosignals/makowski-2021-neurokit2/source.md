Behavior Research Methods (2021) 53:1689–1696
https://doi.org/10.3758/s13428-020-01516-y
| NeuroKit2: | A Python | toolbox | for neurophysiological |     |     | signal |     |     |     |     |     |
| ---------- | -------- | ------- | ---------------------- | --- | --- | ------ | --- | --- | --- | --- | --- |
processing
Makowski1·Tam Pham1·Zen Lau1·Jan Brammer2·Franc¸ois Lespinasse3,4·Hung Pham5·
| Dominique |     |     | J.  | C.  |     |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ChristopherScho¨lzel6·S.H.AnnabelChen1,7,8
Accepted:19November2020/ Published online: 2 February 2021
©ThePsychonomicSociety,Inc.2021
Abstract
NeuroKit2 is an open-source, community-driven, and user-centered Python package for neurophysiological signal
processing. It provides a comprehensive suite of processing routines for a variety of bodily signals (e.g., ECG, PPG,
EDA, EMG, RSP). These processing routines include high-level functions that enable data processing in a few lines of
codeusingvalidatedpipelines,whichweillustrateintwoexamplescoveringthemosttypicalscenarios,suchasanevent-
relatedparadigmandaninterval-relatedanalysis.Thepackagealsoincludestoolsforspecificprocessingstepssuchasrate
extractionandfilteringmethods,offeringatrade-offbetweenhigh-levelconvenienceandfine-tunedcontrol.Itsgoalisto
improve transparency and reproducibility in neurophysiological research, as well as foster exploration and innovation. Its
designphilosophyiscentredonuser-experienceandaccessibilitytobothnoviceandadvancedusers.
| Keywords Neurophysiology·Biosignals·Python·ECG·EDA·EMG |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Neurophysiological measurements increasingly gain popu- as practical reasons. The latter include low costs (espe-
larity in the study of cognition and behavior. These mea- cially compared with other imaging techniques, such as
surements include electroencephalography (EEG), electro- MRI or MEG), ease of use (e.g., portability, setup speed),
cardiography (ECG), electromyography (EMG) and elec- and the increasing availability of recording devices (e.g.,
trodermal activity (EDA). Their popularity is driven by wearables; Yuehong et al., 2016). Moreover, the extraction
theoretical motivations (e.g., the growth of embodied or ofmeaningfulinformationfromneurophysiologicalsignals
affectiveneuroscience;KiversteinandMiller,:2015)aswell isfacilitatedbycurrentadvancesinsignalprocessingalgo-
rithms(Cliftonetal.,2012;Royetal.,2019).Unfortunately,
(cid:2) these algorithms are often not distributed in a usable way
DominiqueMakowski
dmakowski@ntu.edu.sg (i.e., in the form of packaged code) which makes them
|     |     |     |     | inaccessible | to           | researchers | who   | do not    | have | the time | or  |
| --- | --- | --- | --- | ------------ | ------------ | ----------- | ----- | --------- | ---- | -------- | --- |
| 1   |     |     |     | experience   | to implement |             | them. | Moreover, | many | software |     |
SchoolofSocialSciences,NanyangTechnologicalUniversity,
toolsforneurophysiologicalanalysesarelimitedtoasingle
HSS04-19,48NanyangAvenue,Singapore,Singapore
| 2   |     |     |     | type of signal |     | (for instance | ECG). | This | makes | it inconve- |     |
| --- | --- | --- | --- | -------------- | --- | ------------- | ----- | ---- | ----- | ----------- | --- |
BehaviouralScienceInstitute,RadboudUniversity,
|     |     |     |     | nient for | researchers | who | might | have | to concurrently |     | rely |
| --- | --- | --- | --- | --------- | ----------- | --- | ----- | ---- | --------------- | --- | ---- |
Nijmegen,Netherlands
| 3   |     |     |     | on a number | of  | software | packages | to process |     | and analyze |     |
| --- | --- | --- | --- | ----------- | --- | -------- | -------- | ---------- | --- | ----------- | --- |
De´partementdepsychologie,Universite´deMontre´al,
multimodaldata.
Montre´al,Canada
| 4   |     |     |     | Additionally,psychologyandneurosciencefacea“repro- |     |     |     |     |     |     |     |
| --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
CentredeRecherchedel’InstitutUniversitaireGeriatriquede
|     |     |     |     | ducibility | crisis” | (Maizey | &   | Tzavella, | 2019; | Miłkowski |     |
| --- | --- | --- | --- | ---------- | ------- | ------- | --- | --------- | ----- | --------- | --- |
Montre´al,Montre´al,Canada
| 5   |     |     |     | et al., 2018; | Nosek | et  | al., 2015; | Topalidou |     | et al., | 2015) |
| --- | --- | --- | --- | ------------- | ----- | --- | ---------- | --------- | --- | ------- | ----- |
EurekaRobotics,Singapore,Singapore
whichhasleadtoaprofoundreassessmentofresearchprac-
6
LifeScienceInformatics,THMUniversityofApplied
|     |     |     |     | tices (by | researchers, | publishers, |     | funding | agencies, |     | etc.). |
| --- | --- | --- | --- | --------- | ------------ | ----------- | --- | ------- | --------- | --- | ------ |
Sciences,Giessen,Germany
Theopacityofdataprocessing,suchasill-specified,orinac-
7
CentreforResearchandDevelopmentinLearning,Nanyang
|     |     |     |     | cessible | analysis | pipelines, | plays | a major | role | in the | crisis. |
| --- | --- | --- | --- | -------- | -------- | ---------- | ----- | ------- | ---- | ------ | ------- |
TechnologicalUniversity,Singapore,Singapore
|     |     |     |     | This issue | could | in part | be alleviated |     | by making | analyses |     |
| --- | --- | --- | --- | ---------- | ----- | ------- | ------------- | --- | --------- | -------- | --- |
8
LeeKongChianSchoolofMedicine,NanyangTechnological code an integral part of scientific publications, rather than
University,Singapore,Singapore

1690 Behav Res (2021) 53:1689–1696
treating a paper as the sole and most important part of the signals; epoch extraction, signal processing (e.g., filtering,
research project. However, distributing the analysis script resampling, rate computation using different published
alongside the paper poses new challenges: Scripts must be algorithms detailed in the package’s documentation);
shareable (not always feasible with closed-source and pro- spectral analyses; complexity and entropy analyses; and
prietary software or programming languages), accessible convenient statistical methods (e.g., K-means clustering,
(well-documented and organized scripts) and reproducible ICAorPCA).Avarietyofplottingfunctionsallowforquick
(which is difficult for software relying on graphical user andexpressivevisualizationofthesignalprocessingandthe
interfaces - GUI - in which the manual point-and-click resultingfeatures.
sequencecanbehardtoautomate). The package is implemented in Python 3 (Van Rossum
NeuroKit2,addressesthesechallengesbyofferingafree, & Drake, 2009), which means that NeuroKit2’s users
user-centered, and comprehensive solution for neurophysi- benefit from an large number of learning resources and
ologicaldataprocessing,withaninitialfocusonbodilysig- a vibrant community. The package depends on relatively
nalsincludingECG(electrocardiographyisusedtomeasure few,wellestablishedandrobustpackagesfromthenumeric
cardiac activity), PPG (photoplethysmogram is an optical Python ecosystem such as NumPy (Harris et al., 2020),
measurement of blood flow), RSP (respiration measures), pandas (McKinney & et al. 2010), SciPy (Virtanen et al.,
EDA (electrodermal activity measuring the electrical con- 2020),scikit-learn(Pedregosaetal.,2011)andMatplotLib
ductance of the skin), EMG (electromyography measuring (Hunter, 2007) (with an additional system of optional
muscular activity) and EOG (electrooculography measur- dependencies), making NeuroKit2 a viable dependency for
ingeyemovements).Italsoprovidesmodality-independent otherpackages.
functionsthatcanbeusedforothermodalitiessuchasEEG NeuroKit2’ssourcecodeisavailableundertheMITlicense
(electroencephalographymeasuringelectricalactivityofthe onGitHub(https://github.com/neuropsychology/NeuroKit).
brain),forwhichmorespecificsupportisindevelopment. Its documentation (https://neurokit2.readthedocs.io/)
The open-source Python package is developed by a is automatically built and rendered from the code and
multi-disciplinary team that actively invites new collab- includes guides for installation and contribution, a
orators. The target audience of NeuroKit2 includes both description of the package’s functions, as well as several
experienced and novice programmers. Although being a “hands-on” examples and tutorials (e.g., how to extract
programming-basedtool,usersnotfamiliarwithPythonor and visualize individual heartbeats, how to analyze event-
other languages can start using the software (and improve relateddataetc.).Importantly,userscanaddnewexamples
their programming skills along the way) by following our by simply submitting a Jupyter notebook (Kluyver et al.,
step-by-step examples. Moreover, we also include a thor- 2016) to the GitHub repository. The notebook will auto-
oughtutorialonPythoninstallation,aswellasa“10minutes matically be displayed on the website, ensuring easily
introductiontoPython”inthedocumentation.Whilemany accessible and evolving documentation. Moreover, users
of the existing software caters to a single signal modal- cantryouttheexamplenotebooksdirectlyintheirbrowser
ity (e.g., KUBIOS©(Tarvainen et al., 2014), HeartPy (van via a cloud-based Binder environment (Jupyter et al.,
Gent et al., 2019) andpyHRV (Gomes et al., 2019) for 2018). Finally, the issue tracker on GitHub offers a con-
ECG, cvxEDA (Greco et al., 2015), Ledalab (Benedek & venient and public forum that allows users to report bugs,
Kaernbach, 2010), and SCRalyze (Bach, 2014) for EDA), get help and gain insight into the development of the
NeuroKit2 provides support for various signals and allows package. Our active collaborators range from academics,
its users to process signals from multiple physiological professionals and practitioners in the life sciences and
modalities with a uniform application programming inter- engineering fields (See the “authors” section on the pack-
face (API). It aims at being accessible, well-documented, age’s documentation). Based on community feedback
well-tested,cutting-edge,flexibleandefficient.Thelibrary that we received (social networks, GitHub issues), Neu-
allows users to select from a wide range of validated anal- roKit2hasattractedusersofdifferentprofiles,rangingfrom
ysis pipelines and to create custom pipelines tailored to those who are new to signal processing and programming
specific analyses requirements. Historically, NeuroKit2 is tomoreexperiencedusers.
there-forgedsuccessorofNeuroKit“1”(Makowski,2020), NeuroKit2 aims at being reliable and trustworthy,
takingoveritsmostsuccessfulfeaturesanddesignchoices, includingimplementationsofprocessingpipelinesthathave
andre-implementingtheminawaythatadherestocurrent been described in peer-reviewed publications. Details and
bestpracticesinopensourcesoftwaredevelopment. references regarding those pipelines are available in the
NeuroKit2 offers a breadth of functionalities which package’sdocumentation.Manypipelineshavebeentested
includes, but is not limited to, signal simulation; data against established software such as BioSPPy (Carreiras
management (e.g., downloading existing datasets, reading et al., 2015), hrv (Bartels & Pecanha, 2020), PySiology
andformattingfilesintoadataframe);eventextractionfrom (Gabrieli et al., 2019), HeartPy (van Gent et al., 2019),

| Behav Res (2021) 53:1689–1696 |     |     |     |     |     |     |     | 1691 |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | ---- |
systole(Legrand&Allen,2020)ornolds(Scho¨lzel,2019). phase classification or rate computation. Critically, for
Additionally, the repository leverages a comprehensive each type of signal, uniform function names are used (in
test suite (using pytest) and continuous integration (using the form signaltype functiongoal()) to achieve
Travis-CI and GitHub actions) to ensure software stability equivalent goals, e.g., * clean(), * findpeaks(),
and quality. The test coverage and build status can * process(), * plot(), making the implementation
transparentlybetrackedviatheGitHubrepository.Thanks intuitiveandconsistentacrossdifferentmodalities.
to its collaborative and open development, NeuroKit2 can For example, the rsp clean() function uses
remain cutting-edge and continuously evolve, adapt, and signal filter() and signal detrend(), with
integratenewmethodsastheyareemerging. different sets of default parameters that can be switched
Finally, we believe that the design philosophy of with a “method” argument (corresponding to different
NeuroKit2 contributes to an efficient (i.e., allowing to published or established pipelines). For instance, setting
achievealotwithfewfunctions)yetflexible(i.e.,enabling method="khodadad2018"willusethecleaningwork-
fine control and precision over what is done) UI. We will flow described in Khodadad et al. (2018). However, if a
illustrate these claims with two examples of common use- user wants to build their own custom cleaning pipeline,
cases(theinterval-relatedanalysisonrestingstatedataand they can use the cleaning function as a template, and
theevent-relatedanalysis),andwillconcludebydiscussing tweaktheparameterstotheirdesiresinthelow-levelsignal
how NeuroKit2 contributes to neurophysiological research processingoperations.
| by raising | the standards | for validity, | reproducibility | and |     |     |     |     |
| ---------- | ------------- | ------------- | --------------- | --- | --- | --- | --- | --- |
High-levelwrappersforprocessingandanalysis
accessibility.
|     |     |     |     | The mid-level | functions | are assembled | in high-level |     |
| --- | --- | --- | --- | ------------- | --------- | ------------- | ------------- | --- |
Designphilosophy wrappers, that are convenient entry points for new
ecg process()
|     |     |     |     | users. For | instance, the |     | function | inter- |
| --- | --- | --- | --- | ---------- | ------------- | --- | -------- | ------ |
NeuroKit2 aims at being accessible to beginners and, at nally chains the mid-level functions ecg clean(),
|          |                |           |                  | ecg peaks(),ecg | quality(),ecg |     | delineate(), |     |
| -------- | -------------- | --------- | ---------------- | --------------- | ------------- | --- | ------------ | --- |
| the same | time, offering | a maximal | level of control | to              |               |     |              |     |
experienced users. This is achieved by allowing beginning and ecg phase(), as shown in Fig. 1. A specific pro-
cessingpipelinecanbeselectedwiththemethodargument
| users to implement | complex | processing | pipelines | with |     |     |     |     |
| ------------------ | ------- | ---------- | --------- | ---- | --- | --- | --- | --- |
a few functions, while still providing experienced users that is then propagated throughout the internal functions.
with fine-tuned control over arguments and parameters. In Easily switching between processing pipelines allows for
concreteterms,thistrade-offisenabledbyanAPIstructure the comparison of different methods, and streamlines crit-
organizedinthreelayers. ical but time-consuming steps in reproducible research,
|     |     |     |     | such as | the validation | of data preparation | and | qual- |
| --- | --- | --- | --- | ------- | -------------- | ------------------- | --- | ----- |
Low-level:Baseutilitiesforsignalprocessing ity control (Quintana et al., 2016). Finally, the package
|     |     |     |     | includes convenience-functions |     | (e.g., | bio process) | that |
| --- | --- | --- | --- | ------------------------------ | --- | ------ | ------------ | ---- |
Thebasicbuildingblocksarefunctionsforgeneralsignalpro- enable the combined processing of multiple types of sig-
cessing,i.e.,filtering,resampling,interpolation,peakdetec- nals at once (e.g., bio process(ecg=ecg signal,
tion, etc. These functions are modality-independent, and eda=eda signal)).
include several parameters(e.g., onecanchangethefiltering Performing an entire set of operations with sensible
method, frequencies, and order, by overwriting the default default parameters in one function can be rewarding, espe-
arguments).Mostofthesefunctionsarebasedonestablished cially for beginners, allowing them to perform cutting-edge
algorithms implemented in scipy (Virtanen et al., 2020). processing or replication of research steps without requir-
Examples of such functions include signal filter(), ing much programming expertise. Moreover, it contributes
signal interpolate(), signal resample(), to the demystification of the usage of programming tools
signal detrend(),andsignal findpeaks(). (as opposed to GUI-based software such as SPSS, Kubios,
|     |     |     |     | or Acqknowledge), | providing | a welcoming | framework | to  |
| --- | --- | --- | --- | ----------------- | --------- | ----------- | --------- | --- |
Mid-level:Neurophysiologicalprocessingsteps further explore physiological data processing. Importantly,
|     |     |     |     | more advanced | users can | build custom | analysis pipelines |     |
| --- | --- | --- | --- | ------------- | --------- | ------------ | ------------------ | --- |
Thebaseutilitiesareusedbymid-levelfunctionsspecificto by using the low- and mid-level functions, allowing for
thedifferentphysiologicalmodalities(i.e.,ECG,RSP,EDA, finercontrolovertheprocessingparameters.Webelievethat
EMG, PPG). These functions carry out modality-specific this implementation is a well-calibrated trade-off between
signal processing steps, such as cleaning, peak detection, flexibilityanduser-friendliness.

| 1692 |     |     |     |     |     | Behav Res (2021) 53:1689–1696 |     |
| ---- | --- | --- | --- | --- | --- | ----------------------------- | --- |
Fig.1 IllustrationoftheNeuroKit2packagearchitecture,inthecaseofECGsignalprocessing
InstallingNeuroKit2 (not necessarily tied to a specific and sudden event)
|     |     |     |     | are extracted. | The second | example presents | an event- |
| --- | --- | --- | --- | -------------- | ---------- | ---------------- | --------- |
NeuroKit2 is available on PyPI, a repository of software related paradigm, in which the interest lies in shorter-term
forthePythonprogramminglanguage.andcanbeinstalled physiologicalchangesrelatedtospecificevents(seeFig.1
using pip (via “pip install neurokit2” command). Detailed and Table 1). The example datasets are available with
data()
instructions on how to install Python are also available in the package and can be downloaded using the
theinstallationsectionofthepackage’sdocumentation. function. This utility reads comma separated values files
|     |     |     |     | (.csv) with | the Pandas function       | pd.read  | csv(), where each |
| --- | --- | --- | --- | ----------- | ------------------------- | -------- | ----------------- |
|     |     |     |     | column      | is a different biosignal. | Each row | is a sample that  |
Examples
|     |     |     |     | correspond | to signals’ value | at a given | point in time. All |
| --- | --- | --- | --- | ---------- | ----------------- | ---------- | ------------------ |
examplesusethe0.0.41versionreleaseofNeuroKit2.
| In this section, | we present | two examples | that illustrate |     |     |     |     |
| ---------------- | ---------- | ------------ | --------------- | --- | --- | --- | --- |
the most common use-cases (Fig. 2). Both examples can Interval-relatedparadigm
| be accessed | in an interactive | format (without | any prior |     |     |     |     |
| ----------- | ----------------- | --------------- | --------- | --- | --- | --- | --- |
installation) via a Binder environment. The first example Thefirstdatasetcorrespondsto5minutesofphysiological
illustratesaninterval-relatedparadigmwherecharacteristics activity of a human participant at rest (eyes-closed in a
of physiological activity during a certain time interval seated position), with no specific instructions. It contains
Table1 Examplesoffeaturescomputedindifferentdomains
| Interval-relatedFeatures |     |     | Event-relatedFeatures |     |     |     |     |
| ------------------------ | --- | --- | --------------------- | --- | --- | --- | --- |
ECGRateCharacteristics(Mean,Amplitude) ECGRateChanges(Min,Mean,Max,TimeofMin,Max,Trend)
HeartRateVariability(HRV)indices RSPRateChanges(Min,Mean,Max,TimeofMin,Max)
RespiratoryRateVariability(RRV)indices RSPAmplitudeMeasures(Min,Mean,Max)
RespiratorySinusArrhythmia(RSA)indices ECGandRSPPhase(Inspiration/Expiration,Systole/Diastole,Completion)
NumberofSCRPeaksandmeanamplitude SCRpeakanditscharacteristics(amplitude,risetime,recoverytime)

| Behav Res (2021) 53:1689–1696 |     |     |     |     |     |     |     |     |     |     |     | 1693 |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
threechannels(ECG,PPGandRSP)sampledatafrequency rate is lower than usually required, see Quintana et al.
of100Hz. (2016), in order to be able to include the example data
|     |     |     |     |     |     |     | in  | the NeuroKit2 | distribution). | It has 4 | channels | including |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------------- | -------- | -------- | --------- |
threephysiologicalsignals,andonecorrespondingtoevents
markedwithaphotosensor(signalstrengthdecreaseswhen
astimulusappearsonthescreen).
| Here, the                              | aim was     | to illustrate |                     | a type        | of physiological |            |     |     |     |     |     |     |
| -------------------------------------- | ----------- | ------------- | ------------------- | ------------- | ---------------- | ---------- | --- | --- | --- | --- | --- | --- |
| analysis that                          | we refer    | to            | as interval-related |               | (or              | resting-   |     |     |     |     |     |     |
| state paradigm,                        | as opposed  |               | to an               | event-related |                  | paradigm). |     |     |     |     |     |     |
| After loading                          | the package |               | and the             | example       | dataset,         | each       |     |     |     |     |     |     |
| physiologicalsignalisprocessedusingbio |             |               |                     |               | process().       |            |     |     |     |     |     |     |
Aswewanttocomputefeaturesrelatedtotheentiredataset
| (see Table        | 2), we | can directly | pass    | the | whole            | dataframe |     |     |     |     |     |     |
| ----------------- | ------ | ------------ | ------- | --- | ---------------- | --------- | --- | --- | --- | --- | --- | --- |
| to bio analyze(), |        | and          | compute | the | interval-related |           |     |     |     |     |     |     |
features.Userscanchooseaspecifictimeintervalfromtheir
dataset.
| Interval-related |                | analyses | compute  | features |       | of signal |     |     |     |     |     |     |
| ---------------- | -------------- | -------- | -------- | -------- | ----- | --------- | --- | --- | --- | --- | --- | --- |
| variability      | and activation |          | patterns | over a   | given | period of |     |     |     |     |     |     |
time,includingaverageheartandbreathingrate,aswellas
indicesofheartratevariability(HRV)andrespiratorysinus
| arrhythmia      | (RSA). | NeuroKit2    | allows | for       | the fast    | creation |     |     |     |     |     |     |
| --------------- | ------ | ------------ | ------ | --------- | ----------- | -------- | --- | --- | --- | --- | --- | --- |
| of standardized | and    | reproducible |        | pipelines | to describe | this     |     |     |     |     |     |     |
kindofphysiologicalactivity.
|     |     |     |     |     |     |     |     | In this example, | the steps | of the analysis   |     | are identical |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --------- | ----------------- | --- | ------------- |
|     |     |     |     |     |     |     | to  | the previous     | example,  | including loading |     | the package,  |
Event-relatedParadigm the dataset and processing the data. The difference is
|     |     |     |     |     |     |     | that | stimulus | onsets in | the photosensor |     | are detected |
| --- | --- | --- | --- | --- | --- | --- | ---- | -------- | --------- | --------------- | --- | ------------ |
ThisexampledatasetcontainsECG,RSPandEDAsignals separately with events find(). Once we have the
of one participant who was presented with four emotional preprocessed signals and the location of events, we use
images(fromtheNAPSdatabase;Marchewkaetal.,2014) epochs create() to slice the data into segments
in a typical (albeit shortened) experimental psychology corresponding to a time window (ranging from -0.1 to 4
paradigm. seconds)aroundeachstimulus.Finally,relevantfeaturesare
The signals are 2.5 minutes (150 seconds) long and are computed for each epoch (i.e., each stimulus) by passing
recorded at a frequency of 100Hz (note that the sampling themtobio analyze().
Table2 Subsetofpropertiescharacterizingthephysiologicalactivityoveraperiodof5minutesofresting-state
| ECG Rate | Mean |     |     | HRV   | RMSSD |     |     | RSP   | Rate Mean |     | RSA  | P2T Mean |
| -------- | ---- | --- | --- | ----- | ----- | --- | --- | ----- | --------- | --- | ---- | -------- |
| 86.39    |      |     |     | 38.84 |       |     |     | 15.74 |           |     | 0.07 |          |

| 1694 |     |     |     | Behav Res (2021) 53:1689–1696 |     |
| ---- | --- | --- | --- | ----------------------------- | --- |
Table3 Subsetoftheouputrelatedtoevent-relatedanalysischaracterizingthepatternofphysiologicalchangesrelatedtospecificstimuli
| Condition |     | ECG Rate | Mean | RSP Rate Mean | EDA Peak Amplitude |
| --------- | --- | -------- | ---- | ------------- | ------------------ |
|           |     | −2.01    |      | −0.15         |                    |
| Negative  |     |          |      |               | 0.93               |
| Neutral   |     | −3.13    |      | 1.40          | 0.41               |
−0.34
| Neutral  |     | 1.34  |     |      | 0.02 |
| -------- | --- | ----- | --- | ---- | ---- |
| Negative |     | −3.55 |     | 1.97 | 1.06 |
Notably, the features include the changes in rate of isrelatedtostrongercardiacdeceleration,higherskincon-
ECGandRSPsignals(e.g.maximum,minimumandmean ductanceresponse,andacceleratedbreathingrate(notethat
rate after stimulus onset, and the time at which they thisdescriptiveinterpretationisgivensolelyforillustrative
| occur),andthepeakcharacteristicsoftheEDAsignal(e.g., |                     |          |                    | purposes). |     |
| ---------------------------------------------------- | ------------------- | -------- | ------------------ | ---------- | --- |
| occurrence                                           | of skin conductance | response | (SCR), and if      |            |     |
| SCR is present,                                      | its corresponding   | peak     | amplitude, time of |            |     |
Discussion
| peak, rise | and recovery time). | In addition, | respiration and |     |     |
| ---------- | ------------------- | ------------ | --------------- | --- | --- |
cardiaccyclephasesareextracted(i.e.,therespirationphase
-inspiration/expiration-andcardiacphase-systole/diastole NeuroKit2isaneurophysiologicalsignalprocessinglibrary
-occurringattheonsetofevent). accessibletopeopleacrossdifferentlevelsofprogramming
We hope that these examples demonstrate how straight- experience and backgrounds. For users who are novice
forward the process of extracting features of physiological programmers or are new to neurophysiology, the package
responses can be with NeuroKit2. This pipeline can easily presents an ideal opportunity for exploration and learning.
scaleuptogroup-levelanalysesbyaggregatingtheaverage The experienced programmer is encouraged to choose
of features across participants. In addition to streamlin- and validate the preprocessing and analysis pipelines most
ing data analyses, NeuroKit2 aims to allow researchers to appropriatefortheirdata.Suggestionsforimprovementsor
extract an extensive suite of features that can be linked to additions to the library are welcome and openly discussed
neurocognitive processes. In this example (see Table 3), in the community. Overall, the development of NeuroKit2
exposuretonegativestimuli,ascomparedtoneutralstimuli, is focused on creating an intuitive user-experience, as well
Fig. 2 Plot window displaying a period of raw electrocardiogram orange highlighted sections spanning 0.1s before the onset of each
(ECG in red), respiration (RSP in blue) and electrodermal activity eventandending4saftertheevent,representperiodicregionsofinter-
(EDAinpurple)data.Thegreenhighlightedsection,spanningfrom0 est during event-related analysis. The link for generating the figure
to20s,representstheperiodicregionofinterestduringinterval-related can be found on NeuroKit2’s GitHubrepository (https://github.com/
analysis. The 3 event markers are indicated by dotted lines, and the neuropsychology/NeuroKit/blob/master/paper/make figures.Rmd)

| Behav Res (2021) 53:1689–1696 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 1695 |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
asbuildingacollaborativecommunity.Itsmodularstructure EGG, electrooculography - EOG) and plan to optimize
and organization not only facilitate the use of existing computational efficiency on large datasets. We also plan
and validated processing pipelines, but also create a fertile to further validate the available processing pipelines using
groundforexperimentationandinnovation. public databases. In line with this objective, the support of
The library is also a pragmatic answer to the standardizeddatastructureformats(e.g.WFDB,BIDS,...)
broader need for transparent and reproducible methods in couldbeextended.
neurophysiology. The impact of our package on repro- Inconclusion,webelievethatNeuroKit2providesuseful
ducibility in research is two-fold: firstly, while black-box toolsforanyonewhoisinterestedinanalyzingphysiologi-
software can be easy and convenient to use, users do not caldatacollectedwithresearch-gradehardwareorwearable
have access to the source code, making processing results “smart health devices”. By increasing the autonomy of
subjecttounknownidiosyncrasiesoftheunderlyingimple- researchers and practitioners, and by shortening the delay
mentation of processing routines. This makes it difficult between data collection and results acquisition, NeuroKit2
to identify the source of potential discrepancies in results could be useful beyond academic research in neuroscience
obtainedwithothersoftwareandcanleadtoirreproducible and psychology, including applications such as personal
findings.Incontrast,NeuroKit2documentseachstepofthe physiological monitoring and exercise science. Finally, we
implementation along with the analysis method, allowing hope that NeuroKit2 encourages users to become part of a
userstopin-pointtheanalysisstepswheredifferencesmight supportive open-science community with diverse areas of
arise.Whilemaintainingafocusonoveralluser-experience, expertise rather than relying on closed-source and propri-
the open-source nature of NeuroKit2 encourages indepen- etary software, thus shaping the future of neurophysiology
dent researchers to cross-validate research findings. Sec- anditsrelatedfields.
ondly,notonlydoesNeuroKit2implementseveralmethods
|               |     |             |     |                |     |            |     | Acknowledgments |         | We would | like       | to thank     | Prof. | C. F. Xavier        | for |
| ------------- | --- | ----------- | --- | -------------- | --- | ---------- | --- | --------------- | ------- | -------- | ---------- | ------------ | ----- | ------------------- | --- |
| for analysis, | it  | also allows | for | the comparison |     | of differ- |     |                 |         |          |            |              |       |                     |     |
|               |     |             |     |                |     |            |     | inspiration,    | all the | current  | and future | contributors |       | (https://neurokit2. |     |
ent algorithms. For instance, using a suite of open-source readthedocs.io/en/latest/authors.html),andtheusersfortheirsupport.
databases, different algorithms for ECG R-peak detection Additionally, Franc¸ois Lespinasse would like to thank the Courtois
|     |     |     |     |     |     |     |     | Foundation | for its | support | through | the | Courtois-NeuroMod |     | project |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ------- | ------- | --- | ----------------- | --- | ------- |
havebeencomparedfortheirrobustness(numberoferrors
(https://cneuromod.ca)
| encountered), | efficiency |     | (computation | time) | and | accuracy |     |     |     |     |     |     |     |     |     |
| ------------- | ---------- | --- | ------------ | ----- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(absolutedistancefromtrueR-peaklocation),documented CompliancewithEthicalStandards
inthe“Studies”sectionofthepackage’sdocumentation.As
|     |     |     |     |     |     |     |     | Conflict of | interests | The | authors | declare | that | the research | was |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | --- | ------- | ------- | ---- | ------------ | --- |
NeuroKit2continuestoworkonbenchmarking,wehopeto
conductedintheabsenceofcommercialorfinancialrelationshipsthat
supportusersinmakingmoreinformeddecisionsregarding
couldconstituteaconflictofinterest.
whichmethodismostsuitedfortheirspecificrequirements.
| NeuroKit2  | also        | prioritizes       | a          | high standard |           | of quality |     |            |            |     |              |            |     |             |     |
| ---------- | ----------- | ----------------- | ---------- | ------------- | --------- | ---------- | --- | ---------- | ---------- | --- | ------------ | ---------- | --- | ----------- | --- |
| control    | during      | code development. |            | This          | is done   | through    |     | References |            |     |              |            |     |             |     |
| automated  | testing     | using             | continuous | integration,  |           | as well    | as  |            |            |     |              |            |     |             |     |
| striving   | for code    | simplicity        | and        | readability.  |           | The API    | is  |            |            |     |              |            |     |             |     |
|            |             |                   |            |               |           |            |     | Bach, D.   | R. (2014). | A   | head-to-head | comparison |     | of scralyze | and |
| thoroughly | documented, |                   | including  | working       | examples. |            | We  |            |            |     |              |            |     |             |     |
ledalab,twomodel-basedmethodsforskinconductanceanalysis.
ensurethatthedocumentationevolvesalongsidethecodeby
BiologicalPsychology,103,63–68.
includingitinourcontinuousintegration.WhileNeuroKit2 Bartels,R.,&Pecanha,T.(2020).HRV:Apythonicpackageforheart
currently has a fairly comprehensive documentation, more ratevariabilityanalysis.JournalofOpenSourceSoftware,5(51),
1867.https://doi.org/10.21105/joss.01867
examplesandtutorialswillbeaddedasthepackagegrows
|     |     |     |     |     |     |     |     | Benedek, | M., & | Kaernbach, | C.  | (2010). | A continuous | measure | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ---------- | --- | ------- | ------------ | ------- | --- |
andexpands.Additionally,weprovidethoroughguidelines
|         |              |     |      |               |     |      |     | phasicelectrodermal |     |     | activity.Journal |     | ofNeuroscience |     | Methods, |
| ------- | ------------ | --- | ---- | ------------- | --- | ---- | --- | ------------------- | --- | --- | ---------------- | --- | -------------- | --- | -------- |
| for new | contributors | who | wish | to contribute |     | code | or  | 190(1),80–91.       |     |     |                  |     |                |     |          |
documentation. Carreiras,C.,Alves,A.P.,Lourenc¸o,A.,Canento,F.,Silva,H.,Fred,
|           |     |           |        |           |     |              |     | A., & | et al | (2015). | BioSPPy: | Biosignal | processing | in  | Python. |
| --------- | --- | --------- | ------ | --------- | --- | ------------ | --- | ----- | ----- | ------- | -------- | --------- | ---------- | --- | ------- |
| We expect | the | package’s | future | evolution |     | to be driven |     |       |       |         |          |           |            |     |         |
Retrievedfromhttps://github.com/PIA-Group/BioSPPy/
| by the | communities’ | needs | and | the advances |     | in related |     |             |     |          |             |     |               |     |         |
| ------ | ------------ | ----- | --- | ------------ | --- | ---------- | --- | ----------- | --- | -------- | ----------- | --- | ------------- | --- | ------- |
|        |              |       |     |              |     |            |     | Clifton, D. | A., | Gibbons, | J., Davies, | J., | & Tarassenko, | L.  | (2012). |
fields.Forinstance,althoughNeuroKit2alreadyimplements Machinelearningandsoftwareengineeringinhealthinformatics.
a lot of useful functions for EEG processing (such as 2012 first international workshop on realizing ai synergies in
softwareengineering(raise)(pp37–41).IEEE.
| entropy  | and fractal | dimensions |      | quantification), |      | its support |     |           |             |     |               |         |             |            |        |
| -------- | ----------- | ---------- | ---- | ---------------- | ---- | ----------- | --- | --------- | ----------- | --- | ------------- | ------- | ----------- | ---------- | ------ |
|          |             |            |      |                  |      |             |     | Gabrieli, | G., Azhari, | A., | & Esposito,   |         | G. (2019).  | PySiology: | A      |
| could be | further     | improved   | (for | example          | with | high-level  |     |           |             |     |               |         |             |            |        |
|          |             |            |      |                  |      |             |     | python    | package     | for | physiological | feature | extraction. | In         | Neural |
functions built on top of utilities provided by the leading approaches to dynamics of signal exchanges (pp. 395–402).
EEG Python software, namely MNE, Gramfort et al. Springer Singapore. https://doi.org/10.1007/978-981-13-8950-4
35
| (2013).     | Additionally, | in             | the future | we                  | strive | to support |     |                                   |     |       |             |                          |         |           |      |
| ----------- | ------------- | -------------- | ---------- | ------------------- | ------ | ---------- | --- | --------------------------------- | --- | ----- | ----------- | ------------------------ | ------- | --------- | ---- |
|             |               |                |            |                     |        |            |     | Gomes,P.,Margaritoff,P.,&Silva,H. |     |       |             | (2019).pyHRV:Development |         |           |      |
| other types | of            | bodily signals | (e.g.,     | electrogastrography |        |            | -   |                                   |     |       |             |                          |         |           |      |
|             |               |                |            |                     |        |            |     | and evaluation                    |     | of an | open-source | python                   | toolbox | for heart | rate |

| 1696 |     |     |     |     |     |     |     |     | Behav Res (2021) 53:1689–1696 |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- |
variability (hrv). Proc. Int’l conf On electrical, electronic and Miłkowski, M., Hensel, W. M., & Hohol, M. (2018). Replicability
computingengineering(icetran),822–828. or reproducibility? on the replication crisis in computational
Gramfort,A.,Luessi,M.,Larson,E.,Engemann,D.A.,Strohmeier, neuroscience and sharing only relevant detail. Journal of
D.,Brodbeck,C.,&etal.(2013).MEGandeegdataanalysiswith ComputationalNeuroscience,45(3),163–172.
mne-python.FrontiersinNeuroscience,7,267. Nosek, B. A., Cohoon, J., Kidwell, M., & Spies, J. R. (2015).
Greco,A.,Valenza,G.,Lanata,A.,Scilingo,E.P.,&Citi,L.(2015). Estimatingthereproducibilityofpsychologicalscience.Science,
| CvxEDA:Aconvexoptimizationapproachtoelectrodermalactiv- |     |     |     |     |     | 349(6251),aac4716. |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
ity processing. IEEE Transactions on Biomedical Engineering, Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion,
63(4),797–804. B., Grisel, O., & Duchesnay, E. (2011). Scikit-learn: Machine
Harris, C. R., Millman, K. J., Van der Walt, S. J., Gommers, R., learning in Python. Journal of Machine Learning Research, 12,
| Virtanen,P.,Cournapeau,D.,&etal.(2020).Arrayprogramming |     |     |     |     |     | 2825–2830. |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
withnumpy.Nature,585(7825),357–362. Quintana, D., Alvares, G. A., & Heathers, J. (2016). Guidelines
Hunter, J. D. (2007). Matplotlib: a 2D graphics environment. for reporting articles on psychiatry and heart rate variability
ComputinginScience&Engineering,9(3),90–95. (graph): Recommendations to advance research communication.
Jupyter,B.,Forde,F.,Granger,H.W.,Akici,F.,Lippa,D.,Niederhut, TranslationalPsychiatry,6(5),e803–e803.
D., & Pacer, M. (2018). Binder 2.0 - Reproducible, interactive, Roy, Y., Banville, H., Albuquerque, I., Gramfort, A., Falk, T. H., &
sharableenvironmentsforscienceatscale.InProceedingsofthe Faubert, J. (2019). Deep learning-based electroencephalography
17thPythoninScienceConference.https://doi.org/%2010.25080/ analysis: A systematic review. Journal of Neural Engineering,
| Majora-4af1f417-011%20,(pp.113–120). |     |     |     |     |     | 16(5),051001. |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
Khodadad,D.,Nordebo,S.,Mueller,B.,Waldmann,A.,Yerworth,R., Scho¨lzel, Nonlinear measures for dynamical systems.
|     |     |     |     |     |     |     | C. (2019). |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
Becher,T.,&etal.(2018).Optimizedbreathdetectionalgorithm
Zenodo.https://doi.org/10.5281/zenodo.3814723
inelectricalimpedancetomography.PhysiologicalMeasurement,
Tarvainen,M.P.,Niskanen,J.-P.,Lipponen,J.A.,Ranta-Aho,P.O.,&
39(9),094001.
Karjalainen,P.(2014).AKubioshrv–heartratevariabilityanalysis
| Kiverstein, | J., & Miller, | M. (2015). The          | embodied | brain:       | Towards |           |          |         |              |     |              |
| ----------- | ------------- | ----------------------- | -------- | ------------ | ------- | --------- | -------- | ------- | ------------ | --- | ------------ |
|             |               |                         |          |              |         | software. | Computer | Methods | and Programs | in  | Biomedicine, |
| a radical   | embodied      | cognitive neuroscience. |          | Frontiers in | Human   |           |          |         |              |     |              |
113(1),210–220.
Neuroscience,9,237.
Topalidou,M.,Leblois,A.,Boraud,T.,&Rougier,N.(2015).PAlong
Kluyver,T.,Ragan-Kelley,B.,Pe´rez,F.,Granger,B.E.,Bussonnier,
|     |     |     |     |     |     | journey | into reproducible | computational |     | neuroscience. | Frontiers |
| --- | --- | --- | --- | --- | --- | ------- | ----------------- | ------------- | --- | ------------- | --------- |
M.,Frederic,J.,&etal.(2016).Jupyternotebooks-apublishing
inComputationalNeuroscience,9,30.
| format | for reproducible | computational | workflows. | ELPUB, | 87– |           |            |              |       |           |            |
| ------ | ---------------- | ------------- | ---------- | ------ | --- | --------- | ---------- | ------------ | ----- | --------- | ---------- |
|        |                  |               |            |        |     | van Gent, | P., Farah, | H., van Nes, | N., & | van Arem, | B. (2019). |
90.
|     |     |     |     |     |     | HeartPy: | A novel | heart rate algorithm | for | the analysis | of noisy |
| --- | --- | --- | --- | --- | --- | -------- | ------- | -------------------- | --- | ------------ | -------- |
Legrand,N.,&Allen,M.(2020).Systole:Apythontoolboxforprepro-
signals.TransportationResearchPartF:TrafficPsychologyand
| cessing, | analyzing, | and synchronizing | cardiac | data. | Retrieved |     |     |     |     |     |     |
| -------- | ---------- | ----------------- | ------- | ----- | --------- | --- | --- | --- | --- | --- | --- |
Behaviour,66,368–378.https://doi.org/10.1016/j.trf.2019.09.015
fromhttps://github.com/embodied-computation-group/systole
Maizey, L., & Tzavella, L. (2019). Barriers and solutions for early VanRossum,G.,&Drake,F.L.(2009).Python3referencemanual.
careerresearchersintacklingthereproducibilitycrisisincognitive CreateSpace:ScottsValley.
neuroscience.Cortex,113,357–359. Virtanen,P.,Gommers,R.,Oliphant,T.E.,Haberland,M.,Reddy,T.,
Makowski, D. (2020). Neurokit: A python toolbox for statistics Cournapeau,D.,&Contributors,S.(2020).SciPy1.0:Fundamen-
andneurophysiologicalsignalprocessing(eeg,eda,ecg,emg...). talAlgorithmsforScientificComputinginPython.NatureMeth-
Retrievedfromhttps://github.com/neuropsychology/NeuroKit.py ods,17,261–272.https://doi.org/10.1038/s41592-019-0686-2
Marchewka, A., Z˙urawski, J. K., & Grabowska, A. (2014). The Yuehong, Y., Zeng, Y., Chen, X., & Fan, Y. (2016). The internet
nencki affective picture system (naps): Introduction to a novel, of things in healthcare: An overview. Journal of Industrial
standardized,wide-range,high-quality,realisticpicturedatabase. InformationIntegration,1,3–13.
BehaviorResearchMethods,46(2),596–610.
McKinney,W.,etal.(2010).Datastructuresforstatisticalcomputing Publisher’s note Springer Nature remains neutral with regard to
in python. Proceedings of the 9th python in science conference jurisdictionalclaimsinpublishedmapsandinstitutionalaffiliations.
(vol.445,pp.51–56).Austin.