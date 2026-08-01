ORIGINALRESEARCHARTICLE
published:14October2014
doi:10.3389/fnins.2014.00322
Combining and comparing EEG, peripheral physiology and
eye-related measures for the assessment of mental
workload
MaartenA.Hogervorst*,Anne-MarieBrouwer andJanB.F.vanErp
TNOHumanFactors,NetherlandsOrganisationforAppliedScientificResearch,Soesterberg,Netherlands
Editedby: While studies exist that compare different physiological variables with respect to their
CuntaiGuan,InstituteforInfocomm association with mental workload, it is still largely unclear which variables supply the
Research,Singapore best information about momentary workload of an individual and what is the benefit of
Reviewedby: combining them. We investigated workload using the n-back task, controlling for body
ReinholdScherer,GrazUniversityof
movementsandvisualinput.WerecordedEEG,skinconductance,respiration,ECG,pupil
Technology,Austria
MinnaHuotilainen,FinnishInstitute sizeandeyeblinksof14subjects.Variousvariableswereextractedfromtheserecordings
ofOccupationalHealth,Finland andusedasfeaturesinindividuallytunedclassificationmodels.Onlineclassificationwas
*Correspondence: simulatedbyusingthefirstpartofthedataastrainingsetandthelastpartofthedatafor
MaartenA.Hogervorst,TNO testingthemodels.TheresultsindicatethatEEGperformsbest,followedbyeyerelated
HumanFactors,Netherlands
measures and peripheral physiology. Combining variables from different sensors did not
OrganisationforAppliedScientific
Research,POBox23,3769ZG significantly improve workload assessment over the best performing sensor alone. Best
Soesterberg,Netherlands classification accuracy, a little over 90%, was reached for distinguishing between high
e-mail:maarten.hogervorst@tno.nl and low workload on the basis of 2min segments of EEG and eye related variables. A
similar and not significantly different performance of 86% was reached using only EEG
fromsingleelectrodelocationPz.
Keywords:EEG,physiology,eye,workload,classification,combination,ECG,skinconductance
INTRODUCTION individual.Ontheotherhand,physiologicalresponsestowork-
In the literature, mental workload has been associated with a loadmaybeconsistentwithinandnotbetweenindividuals,which
range of physiological variables. These include heart rate (e.g., would result in variables that are seemingly non-responsive to
studies as reviewed byVogt et al., 2006 ), different types of workload at a group level while they are actually valuable for
heartratevariability(reviewedbyHancocketal.,1985;Aasman assessingworkloadonanindividualbasis.Finally,manyworkload
et al., 1987), pupil size (reviewed by Beatty, 1982; May et al., studiessufferfromexperimentalflawsinwhichworkloadlevels
1990; Porter et al., 2007; Hampson et al., 2010), eye blink fre- are confounded with for instance body movements (potentially
quencyandduration(WilsonandFisher,1991;Brookingsetal., affecting heart rate and related variables) or visual information
1996;VeltmanandGaillard,1996,1998),electrodermalmeasures processing (potentially affecting eye- and EEG based variables).
(Kohlisch and Schaefer, 1996;Reimer and Mehler, 2011), respi- We here aim to provide an overview of the workload assess-
rationfrequency(Wientjes,1992;Mehleretal.,2009;Karavidas ment performance of a rather broad range of variables within
etal.,2010)andvariousvariablesderivedfromEEG(mostpromi- the context of an experiment in which visual input and the
nentlypowerinthealphaandthetaband—reviewedbyBrouwer amount of body movements are constant across workload lev-
etal.(2012). els. Classification analyses are used to get an impression of the
A question that arises when one aims to put this knowledge qualityofworkloadestimationwithinanindividual.Whileanal-
into practical use is which variable(s) one should measure in ysesareperformedoffline,wesimulateanonline1situation,where
ordertogetthebestworkloadassessmentforaspecificindivid- ourclassificationmodelsaretrainedondataacquiredatthestart
ual. It is not easy to answer this question based on the current oftheexperimentandtestedondataacquiredattheendofthe
literaturebecauseofseveralcomplications.Firstly,onlyalimited experiment, therewith avoiding inflation of classification accu-
setofvariablesisrecordedandanalyzedineachstudy,precluding racyduetotimedependencies.Thesamedatahavebeenanalyzed
easycomparisonofperformanceacrossvariables.Secondly,vari- on a group level in Brouwer et al. (2014). That study gives an
ablesareoftenanalyzedandreportedatagrouplevelratherthan overviewofthegeneralmagnitudeanddirectionofeffectsofthe
used to assess workload in an individual. Associations between differentconditionsonthestudiedvariables.
physiologicalvariablesandworkloadasfoundusingagrouplevel
analysis may not generalize to thecase of assessingworkload in 1Notethathere“online”and“realtime”refertousinginformationascollected
an individual since they may not be sufficiently strong to reli- overthelasthalf-orseveralminutes.Especiallyforcertainnon-EEGmeasures,
ably assess workload at a certain moment in time for a single itisnotpossibletoretrievereliableinformationfromveryshortintervals.
www.frontiersin.org October2014|Volume8|Article322|1

Hogervorstetal. WorkloadfromEEG,physiology,andeyesignals
Besides examining how well different variables can be used COMBININGVARIABLES-PROCESSESUNDERLYINGTHE
to estimate workload on their own, we examine to what extent ASSOCIATIONBETWEENWORKLOADANDPHYSIOLOGICAL
combination of different variables improves performance. As VARIABLES
discussed later, while some studies seem to suggest that assess- Beinginterestedincombiningphysiologicalvariablesinorderto
ment of mental state improves when combining physiological arriveatabetterassessmentofworkload,itisofspecialimpor-
variables,reportedimprovementsoftenaremodestandnotstatis- tance to examine the background of the association between
ticallysignificantornotstatisticallytested.Weexaminedifferent the variables and workload. This is because using a combina-
waysofcombiningvariables.Belowwereviewtheliteratureand tion of variables reflecting workload is especially expected to
formulatehypothesesastowhatweexpecttofind. improveworkloadassessmentifthesevariablesarenotallassoci-
atedwiththesamebutratherwithdifferentaspectsofworkload.
SENSITIVITYOFSINGLEVARIABLESTOWORKLOAD Asdescribedbelow,highworkloadlikelygoeshandinhandwith
Studieson(neuro)physiologicalcorrelatesofworkload(ormen- increasedcognitiveprocessing,increased(emotional)arousaland
tal load) go back to at least the early sixties (Kalsbeek and increasedenergydemand;aspectsofworkloadthatarepresum-
Ettema,1963).Arangeofvariableshasbeenexaminedoverthe ably reflected by different physiological variables that have all
years such as heart rate, different types of heart rate variabil- beenassociatedwithworkloadbefore.
ity, pupil size, eye blink frequency and duration, saccade and
fixation related measures, electrodermal measures, respiration, COGNITIVEPROCESSING—EEG
blood pressure, chemical measures, EMG and neurophysiologi- EEGalphaactivity(powerinthe8–12Hzband)hasbeenlinked
calvariablesderivedfromEEG.Toourknowledge,asubstantial, to idling (Pfurtscheller et al., 1996), default mode brain activ-
recent review of physiological responses to workload is lack- ity (Laufs et al., 2003; Jann et al., 2009) and cortical inhibition
ing. There does not seem to be an obvious “winning” variable (Foxeetal.,1998;vanDijketal.,2008;Brouweretal.,2009).This
that can effectively be used to determine workload. One review suggeststhatthismeasurewouldreflectdifferentlevelsofwork-
study (Hancock et al., 1985) suggested heart rate variability as load, with high alpha for low levels of workload which indeed
the most reliable measure, whereas another (Vogt et al., 2006) wasreportedinseveralworkloadstudies(e.g.,Finketal.,2005;
reviewed19studiesinwhichheartratevariabilitywasnoteven Brouwer et al., 2012). Another EEG frequency band that has
recorded.Inthesestudies,heartrateseemedtoberelativelyreli- been related to workload associated processes is theta (4–8Hz).
able.MoststudiesthatexaminedEEGspectralvariablesnextto Evidenceforanassociationbetweenthetaandworkingmemory
physiological variables such as different eye and heart related processesormentalefforthasbeensummarizedinseveralreviews
measures,concludedorsuggestedEEGtobethemostsensitiveor byKlimesch(1996,1997,1999).Thetaincreasesastaskrequire-
promising indicator of workload (Brookings et al., 1996; Taylor mentsincrease(e.g.,Miyataetal.,1990;Raghavacharietal.,2001;
et al., 2010; Christensen et al., 2012). The study by Christensen Jensen and Tesche, 2002; Esposito et al., 2009). A number of
etal.(2012)showedthatclassificationaccuracyusingonlyEEG studiesonworkloadreported bothalphaandthetaeffects(e.g.,
datawasonlymarginallylowercomparedtoaddinginformation Gundel and Wilson, 1992; Brookings et al., 1996; Gevins et al.,
aboutheartrate,blinkrate,blinkamplitude,blinkdurationand 1998;Fournieretal.,1999).
EOG. Berka et al. (2007) argue in their introduction that EEG NotonlyEEGspectralvariables,alsoEvent-Related-Potentials
is the only physiological signal that has been shown to accu- (ERPs) have been found to reflect different levels of workload.
rately reflect subtle shifts in workload. However, in the three The P300 component ofthe ERPisa peak occurring 300ms or
studies favoring EEG just mentioned, as well as in many other somewhatlaterafteranattendedstimulushasbeenpresented.It
workload studies, workload was manipulated in the context of is thought to reflect attentional and working memory processes
simulated realistic tasks involving potential confounds such as (Polich and Kok, 1995; Polich, 2007) and it is in particular this
speech,bodymovementandvisualinformation.Inarecentstudy component that has been reported to decrease with increasing
(Brouwer et al., 2014) we examined effects of workload and levels of memory or workload (Watter et al., 2001; Kida et al.,
time using a task that controls for these kinds of confounds. 2004; Raabe et al., 2005; Allison and Polich, 2008; Evans et al.,
Repeated measures ANOVA analyses did not mark EEG as the 2011; Pratt et al., 2011). Besides the P300, earlier ERP compo-
sourceofinformationthat“best”indicatedworkload.Highlysig- nentsliketheN100(Krameretal.,1995;Ullspergeretal.,2001;
nificant effects of workload were found for EEG in the alpha AllisonandPolich,2008)theN200(Krameretal.,1995),theP1
frequency band but also for mean and minimum skin con- (Pratt et al., 2011) and a positive-negative component between
ductance level, respiration frequency, heart rate, high frequency 140and280ms(Missonnieretal.,2003,2004)havebeenfound
heart rate variability and pupil size. No significant effects were to respond to task difficulty or workload. Finally, late positive
foundforEEGinthethetafrequencyband,midfrequencyheart or negative slow waves have been related to high memory load
rate variability, number of blinks and blink duration. Still, this (Ruchkinetal.,1990)andamountofresourceallocation(Rösler
study does not indicate which variables would be most useful etal.,1997).
forassessingworkloadbasedonalimitedamountofphysiolog-
ical data of a single individual. This is especially the case since AROUSALANDENERGYDEMAND—PERIPHERALPHYSIOLOGY
Brouweretal.(2014)highlighted(strong)effectsoftimeonmost High mental workload is associated with high mental effort
of the measured variables which could potentially complicate (Hockey, 1986; Gaillard and Wientjes, 1994). Mental work-
theiruse. load or mental effort is associated with a decrease of the
FrontiersinNeuroscience|Neuroprosthetics October2014|Volume8|Article322|2

Hogervorstetal. WorkloadfromEEG,physiology,andeyesignals
parasympathetic (“rest or digest”) autonomous nervous system THREESENSORGROUPS
activityandanincreaseinsympathetic(“fightorflight”)activity In sum, we can loosely divide physiological variables found to
(MulderandMulder,1987;Gawronetal.,1989).Thesechanges be associated with workload into three, what we call “sensor
inautonomousnervoussystemactivitycanbeestimatedthrough groups” that are assumed to reflect different aspects of work-
several peripheral physiological measures such as skin conduc- load. EEG measures are expected to mainly reflect cognitive
tance(Roth,1983),heartrateandheartratevariability(Berntson processes. Peripheral physiological measures reflect arousal and
etal.,1997). energy demand. The third group of eye related measures have
Electrical skin conductance varies with the moisture level of probablypartlybeenfoundtocovarywithworkloadduetothe
theskin.Sincethesweatglandsarecontrolledbythesympathetic often occurring confound of the amount of visual information,
partoftheautonomousnervoussystem(Roth,1983),electroder- butforpupildilation,thereasonforitsassociationwithworkload
malmeasuresindicatethelevelofsympatheticactivityorarousal. isunclear.Consideringtheideathattheyreflectdifferentaspects
Alargebodyofliteraturedescribesthepositiveeffectofarousalon ofworkload,combinationofthesegroupsisexpectedtoleadto
skinconductance(e.g.,Wintonetal.,1984;Greenwaldetal.,1989; better classification accuracy than either group alone, especially
Boucsein, 1992, 1999; Brouwer et al., 2013). While increases in forthecombinationofEEGandperipheralphysiology.
skinconductancemaybeviewedasreflectingsympatheticactiv-
ityasaconsequenceofarousalduetomentaleffort,Reimerand COMBININGVARIABLES—FUSIONTECHNIQUES
Mehler (2011) and Kohlisch and Schaefer (1996) interpret their Inpreviousworkloadstudies,EEGhasbeencombinedwithother
findingsofheightenedskinconductancewithincreasedworkload physiologicalsignalsforassessingworkload.Coffeyetal.(2012)
asreflectingemotionalarousal. found that classification of workload based on EEG was more
Heartrateanditsvariabilityareaffectedbyactivationandsup- accurate than when based on fNIRS (functional Near Infrared
pression of both the sympathetic and parasympathetic nervous Spectroscopy),andthatcombiningthetwodidnotincreaseclas-
systems(Berntsonetal.,1997).Atnormalbreathingfrequencies, sificationperformance.WilsonandRussell(2003,2007)combine
fastchangesinheartrate(0.15–0.50Hz)reflecttheadjustmentof respiration(WilsonandRussell,2003),EEG,EOGandheartrate
heartratetobreathing:breathingcauseschangesinbloodpres- in their classification models to assess workload in simulated
sureandbyadaptingheartrate,bloodpressureiskeptarounda aviation-relatedtasks.However,theydonotreportontherelative
certainpoint(Mulder,1980;Aasmanetal.,1987).Also,theadap- contribution of these different signals to classification perfor-
tationtobreathingfacilitatesgasexchangebetweenthelungsand mance.Christensenetal.(2012)assessedworkloadinsimulated
the blood (Grossman and Taylor, 2007). High frequency heart remotepiloting.TheirclassificationmodelswerebasedonEEG,
rate variability reflects only the (fast) parasympathetic nervous EOG,heartrate,blinkrate,blinkamplitude,andblinkduration.
system(Berntsonetal.,1997).Mentalefforthasbeenreportedto They did not extensively report on the relative contribution of
havethelargesteffectuponthemid-band(0.07–0.14Hz;Mulder, these variables, but mention that when classification was per-
1980;Aasmanetal.,1987).Thisbandreflectsnotonlyparasym- formed on the basis of EEG only, classification accuracy hardly
pathetic but also sympathetic activity (Berntson et al., 1997; decreased (about 2%). Chanel et al. (2006) studied the relative
Veltman and Gaillard, 1998). For both bands, suppression of contribution of EEG and peripheral physiological signals (skin
parasympatheticactivity(associatedwithhighworkload)results conductance,heartrate,bloodpressure,respirationandtempera-
inloweradaptationtochangesinbloodpressureandhenceless ture)onclassifyingmentalstatesaselicitedbyemotionalpictures.
heartratevariability. TheyalsodidnotfindastrongadvantageoffusionofEEGand
Mentalworkloadbeingassociatedwithincreasedarousaland physiologyoverEEGalone.
neuralactivityincreasesmetabolicdemand,whichisprobablythe In all of these studies, combination of variables from differ-
causeofobservedincreasesinheartrateandrespirationfrequency entdomainswasachievedbysimpleconcatenationoftheinput
withworkload(VeltmanandGaillard,1998). featurevectors.However,whencombiningEEGdatawithphys-
iology,thelargedifferenceinlengthofthefeaturevectorsforms
EYE-RELATEDMEASURES apotentialproblem.WhileEEGspectralfeaturesarecapturedby
Pupildilationisnotonlycausedbydecreasingluminancebutalso powervaluesindifferentfrequencybandsatdifferentelectrodes
by increasing workload (Beatty, 1982; May et al., 1990; Porter amounting to a large number of features, physiological or eye
et al., 2007; Hampson et al., 2010). Consistent with this, the relatedfeaturessuchaspupilsizeandheartratearetypicallyeach
frontalcortexisinvolvedincontrollingpupildilation(Hampson representedbyjustone(average)value.Thiscouldleadtoapriori
et al., 2010). The underlying function is unclear, but the fact smalladdedvalueofthesefeatures.Apossiblesolutionistouse
thattheeffecthasbeenobservedinstudiesthatvariedtaskdif- higherordercombinationofinformationbycombingtheassess-
ficulty without varying the visual environment (Kahneman and mentsbasedonthevarioustypesoffeatures.Suchamethodwas
Beatty,1966;Kahnemanetal.,1969)indicatesthatitdoesnotpri- usedbyChaneletal.(2009)whostudiedclassificationofdifferent
marilyservepurposesrelatedtovisualperception.Reductionof emotionsaselicitedbyemotionalrecall.Classificationdecisions
blinkfrequencyanddurationwithworkloadcouldbeattributed weremadebytwodifferentEEGbasedclassifiersandoneclassifier
to maximizing detection of visual information (Bauer et al., based on physiology (skin conductance, heart rate, blood pres-
1987; Fogarty and Stern, 1989). In this sense, the sensitivity of sure and respiration) and these decisions were then combined.
theseparameterscanoftenbeexplainedbyhighworkloadbeing AddingtheworstperformingEEGsettothebestperformingone
confoundedbythepresenceofmuchvisualinformation. increased classification accuracy (that was generally between 70
www.frontiersin.org October2014|Volume8|Article322|3

| Hogervorstetal. |     |     |     |     |     |     |     | WorkloadfromEEG,physiology,andeyesignals |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- |
and80%foratwoclassproblem)withabout2–4%,andadding determinedfromECG).Whilethesearenotexpectedtostrongly
physiologyontopofthatresultedinanadditionalincreaseofup improveclassificationperformancesincetheyareprobablylargely
toalmost3%.Therewasnodirectcomparisonwiththeconcate- reflectingthesameunderlyingprocess,wethinkitisworthtrying
nation method (using all features as input to a single classifier) for the practical reason that these features are available without
thoughtheauthorsmentionthatthismethoddidnotleadtoan additionalcosts(i.e.,withouthavingtouseanadditionalsensor).
increaseinaccuracy. Subsequently,wecombinefeaturesfromdifferentsensorgroups
The improvements in classification accuracy as found by “EEG,” “Physiology,” and “Eyes.” Especially the combination of
Chaneletal.(2009)arerelativelysmallandareprobablynotsta- EEGwithPhysiologyisexpectedtoimproveclassificationperfor-
tisticallysignificant.However,thetrendispositiveandwethink mancesincethesegroupsareassumedtoreflectdifferentgeneral
itisworthwhiletoexaminethecaseforworkloadwhereEEGand physiologicalprocessesassociatedwithworkload.Foranalysesat
othertypesofsignalsareexpectedtocomplementeachother.We thesensorgrouplevel,wecheckwhethertakingtimeintoaccount
willcomparethediscussedwaysofcombininginformation,i.e., improvesclassificationperformance.Animprovementofinclud-
fusion at the feature level or at the decision level. When com- ing information about time of measurement may be expected
biningdecisionsfromdifferentclassifiers,aconfidencemeasure basedonfindinggeneraleffectsoftimeonphysiologicalvariables
of the decision is useful. Such a confidence measure is given by (e.g.,Faircloughetal.,2005;Brouweretal.,2014).Foranalysesat
an elastic net model with logistic regression (Friedman et al., thesensorgrouplevel,wealsocomparefusionatthefeaturelevel
2010). Therefore, besides using linear Support Vector Machine tofusionatthedecisionlevel.WeusebothSVMandelasticnet
asthemorestandardclassificationmodel,wealsouseanelastic classificationmodels.
| net model. | This enables | us to | weigh information |     | of the dif- |     |     |     |     |     |     |
| ---------- | ------------ | ----- | ----------------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
ferent sources before averaging (a similar method was used by MATERIALSANDMETHODS
| Chaneletal.,2009).Thepotentialadvantageoffusionatadeci- |                |         |                    |     |              | PARTICIPANTS |                 |     |             |             |              |
| ------------------------------------------------------- | -------------- | ------- | ------------------ | --- | ------------ | ------------ | --------------- | --- | ----------- | ----------- | ------------ |
| sionlevel                                               | isthat smaller | feature | vectors reflecting |     | physiologyor |              |                 |     |             |             |              |
|                                                         |                |         |                    |     |              | Data of      | 14 participants | are | analyzed in | this study. | Participants |
eye related measures do not run the risk to be “flooded” by were aged between 23 and 40 years (mean age 27.9), 8 female
EEG—the disadvantage of fusion at the decision level is that and 6 male. The experiment was performed in accordance with
interactions between different features or feature sets may be thelocalethicsguidelinesandparticipantsgavewritteninformed
consent2.
missed.
MATERIALS
CURRENTSTUDY:OVERVIEWANDHYPOTHESES
We study workload in an experiment in which we control for Stimuli(letters),subjectiveworkloadscalesandannouncements
visual input and the amount of body movements by using an aboutthetypeofthen-backtasktofollowwerepresentedona
TobiiT60EyeTrackermonitor,atadistanceofabout50cmfrom
| n-back task | to vary workload. | This | task | requires | participants | to  |     |     |     |     |     |
| ----------- | ----------------- | ---- | ---- | -------- | ------------ | --- | --- | --- | --- | --- | --- |
indicate of each of successively presented letters whether it is a theparticipants’eyes.Feedbackabouttaskperformancewaspre-
target or not. Workload is low when the target letter is an “x” sented through Labtec LCS-1050 speakers in the form of beeps.
(0-back), intermediate when the target letter is the same as the Participants used a keyboard to indicate whether presented let-
|     |     |     |     |     |     | ters were | targets or | non-targets. | Which | of the keys | (1 or 2 on |
| --- | --- | --- | --- | --- | --- | --------- | ---------- | ------------ | ----- | ----------- | ---------- |
onebefore(1-back)andhighwhenthetargetletteristhesameas
twolettersbefore(2-back).Inthistask,visualinputandnumber the numerical pad) indicated “target” and which “non-target”
ofbuttonpressesarethesameacrossworkloadlevels.Thismeans wascounterbalancedbetweenparticipants.Participantsusedthe
mousetoratesubjectiveworkloadonascale(RSME)betweenthe
thateffectsofworkloadcanreallybeattributedtodifferencesin
| mentalprocessesandcannotbeduetodifferentamountsofhand |     |     |     |     |     | stimulusblocks. |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
oreyemovementsinthehighworkloadconditioncomparedto EEG (electro encephalogram) was recorded through a g.tec
thelowworkloadcondition. USBampandg.tecAuelectrodesplacedatFz,FCz,Pz,C3,C4,F3,
andF4,referencedtolinkedmastoidelectrodes.Agroundelec-
| We determine | the value | of  | individual | features | and combi- |     |     |     |     |     |     |
| ------------ | --------- | --- | ---------- | -------- | ---------- | --- | --- | --- | --- | --- | --- |
5k(cid:2).
nations for the assessment of individual workload level using trode was placed at FPz. Impedance was kept below EEG
individuallytrainedclassificationmodels.Wesimulateanon-line data were filtered by a 0.1Hz high pass- and a 100Hz low pass
|           |                  |         |       |            |            | filter and | sampled | with a frequency | of 256Hz | (USB | Biosignal |
| --------- | ---------------- | ------- | ----- | ---------- | ---------- | ---------- | ------- | ---------------- | -------- | ---- | --------- |
| situation | in which a model | istuned | to an | individual | using data |            |         |                  |          |      |           |
fromthefirstpartoftheexperimentandinwhichtheworkloadis Amplifier,g.tecmedicalengineeringGmbH).
predictedforthelastpartoftheexperiment.WerecordEEG,skin ECG (electro cardiogram) and skin conductance were
|     |     |     |     |     |     | recorded | using a MindWare |     | BioNex 8-slot | chassis | with a 3- |
| --- | --- | --- | --- | --- | --- | -------- | ---------------- | --- | ------------- | ------- | --------- |
conductance,respiration,ECG,pupilsizeandeyeblinks.Various
channelBio-PotentialandGSRamplifier.A4-channeltransducer
variablesareextractedfromthesemeasurementsandusedasfea-
turesinclassificationmodels.Firstly,weexaminehowwellclassi- amplifier was used to measure respiration. For ECG measure-
(cid:2)(cid:2)
ficationmodelsbasedonthevariousindividualfeaturesperform. ment, self-adhesive 1 1/2 electrodes with 7% chloride wet gel
| We expect       | EEG features | to perform | best       | given indications | from       |             |                 |      |                      |            |           |
| --------------- | ------------ | ---------- | ---------- | ----------------- | ---------- | ----------- | --------------- | ---- | -------------------- | ---------- | --------- |
| earlier studies | and given    | the fact   | that EEGis | expected          | to reflect |             |                 |      |                      |            |           |
|                 |              |            |            |                   |            | 2A total of | 35 participants | took | part in the original | experiment | (see also |
whatcanbeconsideredtobethecoreofmentalworkload,namely
Brouweretal.,2012,2014).However,wehereonlyconsideredparticipants
cognitive processing.Next,wewilllookatcombinationsoffea- withcompletedatasets.Wealsoperformedsimilaranalysesforallpartici-
tures.Westartbycombiningfeaturesoriginatingfromthesame pantsforwhichasubsetofdatawasavailable.Theresultsfromsuchpartial
sensor(e.g.,heartrateandheartratevariabilitythatcanbothbe analysesshowedthesamepatternsaspresentedhere.
FrontiersinNeuroscience|Neuroprosthetics October2014|Volume8|Article322|4

| Hogervorstetal.                                          |     |     |     |     |     |        |     |     | WorkloadfromEEG,physiology,andeyesignals |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | ------ | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- |
| wereattachedjustbelowtherightcollarbone,justbelowtheleft |     |     |     |     |     | DESIGN |     |     |                                          |     |     |     |     |     |
lower rib and above the right hip. To record skin conductance, Thethreeconditions(0-back,1-back,2-back)werepresentedin
(cid:2)(cid:2)
twoself-adhesive15/8 electrodeswith1%chloridewetgelwere 2-minblocksdividedacrossfoursessions.Eachsessionconsisted
attachedtothepalmofthelefthandthatwasnotusedforpressing of two repetitions of each of the three blocks. Thus,for each of
| the keys—one | below the | thumb | and one | below | the little fin- |                                                  |     |     |     |     |     |     | ∗        |     |
| ------------ | --------- | ----- | ------- | ----- | --------------- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | -------- | --- |
|              |           |       |         |       |                 | thethreeconditionsparticipantsperformed4sessions |     |     |     |     |     |     | 2repeti- |     |
tions=8blocks.Ineachblock,48letterswerepresented,16of
| ger. Respiration | was recorded | using | an elastic | band | around the |     |     |     |     |     |     |     |     |     |
| ---------------- | ------------ | ----- | ---------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
waistattheheightofthelowersideofthesternum.MindWare’s whichweretargets.Theblockswerepresentedinpseudorandom
BioLab software was used to acquire ECG, skin conductance order, such that each condition was presented once in the first
and respiration. These signals were sampled with a frequency halfofthesessionandonceinthesecondhalfofthesession,and
of 300Hz. They were acquired with a gain setting of 1000, 10, that blocks of the same condition never occurred directly after
and 500 and filtered with a 0.5, 1, and 5Hz high-pass filters, eachother.Beforeeachsessionwasabaselineblockof2minin
respectively. whichtheparticipantquietlyfixatedacrossonthescreen.With
|     |     |     |     |     |     |     | ∗   |     | ∗   |     |     |     | ∗   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Pupilsize,blinkrateandblinkdurationweremeasuredusing 4sessions 2repetitions 3conditions,plus4sessions 1baseline
(cid:2)(cid:2)
a Tobii T60 Eye Tracker that was integrated into an 17 moni- block,thetotaldurationofthen-backtaskwas56min.
tor.Recordingfrequencywas60Hz.Allsignalsweresynchronized
| usingtheTCAPsignalfromTheObserverXT(Zimmermanetal., |     |     |     |     |     | PROCEDURE |     |     |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
2009). Afterenteringthelab,participantsreadandwereexplainedabout
WeusedtheRSMEscale(RatingScaleMentalEffort,Zijlstra,
theexperimentalprocedure.Theythensignedaninformedcon-
1993) to measure subjectively experienced mental effort. This sentform.ThephysiologicalsensorswereattachedandtheTobii
scalerunsfrom0to150withhighervaluesreflectinghigherwork- eye tracker was calibrated. The three conditions were practiced
load.Ithasninedescriptorsalongtheaxis,e.g.,“noteffortful”at up to the point that the participant was familiar with the task.
| value 2 and | “rather effortful” | at value | 58. | Verwey | and Veltman |            |     |       |                  |     |           |     |           |       |
| ----------- | ------------------ | -------- | --- | ------ | ----------- | ---------- | --- | ----- | ---------------- | --- | --------- | --- | --------- | ----- |
|             |                    |          |     |        |             | Regardless | of  | this, | all participants |     | completed | at  | least one | block |
(1996)concludedthissimpleone-dimensionalscaletobemore ofthe2-backtaskinordertoalsopracticetheRSMEratingthat
sensitive than the often-used NASA-TLX (Hart and Staveland, appearedattheendoftheblock.Itwasstressedthatthe2-back
1988).
taskcouldbedifficult,butthatevenwhentheparticipantthought
|      |     |     |     |     |     | it was                                                | too difficult |     | he or | she should | keep | trying | to do | as well |
| ---- | --- | --- | --- | --- | --- | ----------------------------------------------------- | ------------- | --- | ----- | ---------- | ---- | ------ | ----- | ------- |
| TASK |     |     |     |     |     | aspossible.Participantswereaskedtoavoidmovementasmuch |               |     |       |            |      |        |       |         |
Participantsviewedletters,successivelypresentedonascreen.For as possible while performing the task and to use the breaks in
eachletter,theypressedabuttontoindicatewhethertheletterwas between the blocks to make necessary movements. Before the
atargetoranon-target.Inthe0-backcondition,theletterxisthe startofeachblock,theparticipantwasinformedaboutthenature
target.Inthe1-backcondition,aletterisatargetwhenitisthe of the block (rest, 0-back, 1-back, or 2-back) via the monitor.
sameastheonebefore.Inthe2-backcondition,aletterisatarget After each block, the RSME scale was presented and the partic-
whenitisthesameastwolettersbefore.Withthisversionofthe ipant rated subjective mental effort by clicking the appropriate
n-backtask,thelevelofworkloadisvariedwithoutvaryingvisual location on the scale using the mouse. The next block started
inputorfrequencyandtypeofmotoroutput(buttonpresses).A
|     |     |     |     |     |     | after | the participant |     | indicated | to  | be ready | by pressing | a   | button. |
| --- | --- | --- | --- | --- | --- | ----- | --------------- | --- | --------- | --- | -------- | ----------- | --- | ------- |
3-backconditionwasnotused,duetoevidencethatmanypartic- Between sessions, participants had longer breaks, chatting with
ipantsfindittoodifficultandtendtogiveup(Ayazetal.,2007; theexperimentleaderorhavingadrink.
Izzetogluetal.,2007).
Participants were informed after every button press whether DEFINITIONOFFEATURES
itwasacorrectdecisionbyahigh(correct)oralow(incorrect) EEG data were filtered by a 0.1Hz high pass- and a 100Hz low
pitchedtone. Thiswasintended tohelptheparticipant, whoin passfilterandsampledwithafrequencyof256Hz(USBBiosignal
ourexperimentswitchedratheroftenbetweenn-backconditions, Amplifier,g.tecmedicalengineeringGmbH).Afterwardsdatawas
and to increase the likelihood that participants would decide to processed and analyzed using Matlab and the FieldTrip open
invest effort since the participant knew the experiment leader sourceMatlabtoolbox(Oostenveldetal.,2011).Epochsstarting
wouldhearthesoundsaswell.
|     |     |     |     |     |     | at 500ms | before | stimulus |      | onset and | ending      | 2000ms | after | were   |
| --- | --- | --- | --- | --- | --- | -------- | ------ | -------- | ---- | --------- | ----------- | ------ | ----- | ------ |
|     |     |     |     |     |     | shifted  | such   | that the | mean | of the    | first 500ms | was    | zero. | No eye |
STIMULI blinkartifactswereremovedbeforeclassificationwhichmakesthe
Thelettersusedinthen-backtaskwereblack(fontstyle:Matlab implementationofonlineclassificationeasier.Ourpreviousanal-
standard,approximately3cmhigh)andwerepresentedonalight ysis (Brouwer et al., 2012) showed that with EOG performance
graybackground.Theletterswerepresentedfor500msfollowed was not better or contribute to EEG-based workload classifica-
bya2000-msinter-stimulusintervalduringwhichtheletterwas tion, indicating that performance is only expected to get better
replacedbyafixationcross.Inallconditions,33%ofletterswere when removing them. Over each block and each of the 7 EEG-
targets.Exceptfortheletterxinthe0-backtask,letterswereran- channels(C3,F3,C4,F4,Fz,Pz,FCz)wecalculatedtheaverage
domlyselectedfromEnglishconsonants.Vowelswereexcludedto ERPoveralltrialsafterresamplingthedatato100Hz.The(N =
reducethelikelinessofparticipantsdevelopingchunkingstrate- 101)samplesbetween0to1sasERP-features.Similarly,foreach
gies which reduce mental effort, as suggested in Grimes et al. ofthetrialsandchannelsthespectralpowerovercompletetrials
| (2008).             |     |     |     |     |     | (from−0.5to+2.0s)wascalculatedin(N |     |     |     |                                  |     | =37)bandsranging |     |     |
| ------------------- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | -------------------------------- | --- | ---------------- | --- | --- |
| www.frontiersin.org |     |     |     |     |     |                                    |     |     |     | October2014|Volume8|Article322|5 |     |                  |     |     |

Hogervorstetal. WorkloadfromEEG,physiology,andeyesignals
from2to20Hz(instepsof0.5Hz)followinganFFTapproach successiveframes(i.e.,33ms)andmaximally25successiveframes
using a single Hanning taper. Next, the average spectral power (416ms),thiswasconsideredtobeablink.Foreachblink,blink
wasdeterminedforeachblockandchannel(byaveragingoverall duration was determined. Blink rate is the average number of
trials withina block). Trials withextreme variance in the signal blinksperminute.
asdefinedbyastandarddeviationabove100µVwerediscarded The feature “time” was operationalized as the mid-time of
before calculating the average ERP and spectral power features thecorrespondingdatasegmentinsecondsfromthestartofthe
(1% of the data). Apart from using the “raw” ERP and power experiment,discardingbreaksandperiodsinbetweenblocksin
spectra of the various EEG-channels we also used alpha power whichtheRSMEwasregistered.Forinstance,themid-timeofthe
and theta power as feature input for classification. As a mea- first2-minworkloadblockis60sandthatofthesecondis180s.
sure of alpha power we used the average over the natural log Physiological features that were considered with respect to
transformed power within the frequency band ranging from 8 theircapacitytoestimateworkloadinthisstudyaresummarized
to13Hz.Asameasureofthetapowerweusedtheaverageover inTable1.Thistablealsoindicatesthelengthofthecorrespond-
thenaturallogtransformedpoweroffrequenciesbetween4and ingfeaturevector(“Dimension”),aswellasthesinglesensorsand
8Hz. Models that included alpha power and/or theta power as thesensorgroupsthatthefeaturesbelongto.Forexaminingthe
featuresdidnotalsoincludetherawpowervalues.Additionally, usabilityofdifferentvariablesforassessingworkload,wefollow
we examined alpha power of EEG as only recorded at Pz, theta thelistoffeaturesassummedupinTable1.OnlyforEEG,fea-
power as only recorded at Fz and ERP as only recorded at Pz tures can consist of multiple values (dimension larger than 1).
since it would be practical to attach only one electrode to the Therationalebehindthisisthatthementionedfeaturesarethe
scalp, and those are the location-feature combinations that we smallestpossiblepiecesofinformationthatareexpectedtoreflect
a priori expect to produce the clearest results. Effects of work- workload.ForexaminingEEGsensors“allelectrodes,”“Pz,”and
loadonthealphabandareparticularlyexpectedaroundPz(for “Fz,” we only include features reflecting both ERP and spectral
effortfulandattentiveprocessingalphareductionisobservedat properties of the EEG signal as printed in italics. The EEG sen-
parietalregions—(Klimeschetal.,2000;Keiletal.,2006).Effects sorgrouponlyincludesERPandspectralpowerfeaturesof“All
ofworkloadonthethetabandareparticularlyexpectedaround electrodes.”
frontal electrode locations such as Fz (e.g., Miyata et al., 1990;
Raghavacharietal.,2001;JensenandTesche,2002;Espositoetal., CLASSIFICATIONANALYSIS
2009).TheP300isexpectedtobemostclearlyvisibleatPz(e.g., Thefirstthreesessions,eachcontainingtwoblocksofeachn-back
Ravden and Polich, 1999; Srinivasan, 2007). Since a priori Pz condition, were used to train the model parameters to indi-
seemstobethemostinformativeelectrode,wealsolookedatEEG vidual participants. The last session was used to evaluate the
dataingeneralcomingonlyfromthiselectrode. model’s classification accuracy. This simulates estimating work-
Skinconductancelevelwasdeterminedbyaveragingskincon- load online, using model parameters that are adjusted to the
ductanceovereachblock.Inspectionoftherawdatashowedthat individualparticipantinatrainingphase.Asadefault,theclassi-
frequently, skin conductance peaks around the onset of a block ficationmodelsweretrainedandappliedtodistinguishbetween
(i.e.,afterratingsubjectiveworkloadofthepreviousblock)after 0- and 2-back blocks, each containing 2min of data or 48 tri-
which skin conductance rapidly decreases and remains around als(letters).Averageclassificationperformance(fractioncorrect
thesamelevel.Thisledustoalsouseminimumskinconductance in the last session) over all participants was used as measure of
ofeachblockasafeature. modelperformance.
Asameasureofheartrate,wedeterminedthemeanRRIfor Featurevectorswereconstructedforeachofthedatasegments.
eachblock.RRIistheintervalbetweensuccessiveheartbeatsor Forinstance,thefeaturevectorsusedforthemodelthatincludes
more precisely, the interval between subsequent R-peaks in the all spectral power values over 120s blocks of data contains 259
ECG.Threemeasuresofheartratevariabilitywerecomputed.The features(powerat37frequencies×7channels,seeTable1second
rootmeansquaredsuccessivedifference(RMSSD:Goedhartetal., row)×16blocks(4sessions×4blocks).Thedatafromthefirst
2007) between the RRIs reflects high frequency heart rate vari- 3sessionswasusedtotrainaclassifiermodelforeachindividual
ability.High-frequency heartrate variabilitywasalsocomputed participant.Thefeatureswerestandardizedtohavemean0and
asthepowerinthehighfrequencyrange(0.15–0.5Hz)oftheRRI standard deviation 1 on the basis of data from the training set.
overtimeusingWelch’smethodappliedaftersplineinterpolation; Thesamestandardizationtransformationwasappliedtothetest
similarly,formid-frequencyheartratevariabilitythepowerinthe data(thedataofthe4thsession).Aftertrainingthemodelusing
frequencyrangeof0.07–0.15Hzwasused. thetrainingdata(12blocksof259featuresintheexampleabove),
The respiration signal was filtered using a running Gaussian theclassificationwasappliedtothetestdataandtheperformance
blurring window (with a kernel width of 0.39s). Subsequently score of each of the individual models was determined. Finally,
peaksandthroughsweredetectedusingthederivativeofthesig- overallperformanceiscalculatedbytakingtheaveragescoreover
nal. Breathing frequency was defined as the mean time interval allindividualmodels.
betweenthepeaks.Modulationdepthwasdefinedastheaverage Classification accuracy was determined for a range of mod-
differencebetweenpeakandthrough. els differing in the (types of) features that were included in the
Pupil size as determined by the Tobii Eyetracker and the model, differing in the type of classifier and differing in the
ClearViewalgorithmswasaveragedforeachblock.Whentheeye- fusion rule that was used. Classification was performed using
trackerdidnotdetectthepupilforbotheyesforminimallytwo the Donders machine learning toolbox (DMLT) developed by
FrontiersinNeuroscience|Neuroprosthetics October2014|Volume8|Article322|6

| Hogervorstetal. |     |     |     |     |     |     |     | WorkloadfromEEG,physiology,andeyesignals |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- |
Table1|Examined(neuro)physiologicalfeatures,sensorsandsensor STATISTICALANALYSIS
groups. We used one-tailed binomial tests to determine whether clas-
|        |        |         |     |           | sification | accuracy | was significantly | higher            | than | chance,     | which  |
| ------ | ------ | ------- | --- | --------- | ---------- | -------- | ----------------- | ----------------- | ---- | ----------- | ------ |
| Sensor | Sensor | Feature |     | Dimension |            |          |                   |                   |      |             |        |
|        |        |         |     |           | works as   | follows. | In the            | default situation | of   | classifying | the 2- |
group
minhighandlowworkloadblocks(2-vs.0-back),classification
EEG Allelectrodes ERP(0–1sfromstimulus 707 accuracy per participant could only take values of 0, 0.25, 0.50,
onset) 0.75, and 1 (correct classification of 0–4 blocks in the last ses-
|     |     |                       |     |     | sion). To | test whether | on  | the whole, | classification | performance |     |
| --- | --- | --------------------- | --- | --- | --------- | ------------ | --- | ---------- | -------------- | ----------- | --- |
|     |     | Spectralpower(2–20Hz) |     | 259 |           |              |     |            |                |             |     |
Alphapower(8–13Hz) 7 isabovechance,wecomputetheaveragedscoreoverall14indi-
Thetapower(4–8Hz) 7 vidual models as a measure of performance. This average score
ERP+Spectralpower can take on values between 0/56, 1/56, 2/56,...1 (resolution of
966
∗
features 1/56 where 56 is 4 possible scores higher than zero 14 partici-
|     |            |                      |     |     | pants). To  | determine | whether      | this average | score       | is significantly |          |
| --- | ---------- | -------------------- | --- | --- | ----------- | --------- | ------------ | ------------ | ----------- | ---------------- | -------- |
|     | Pz(single  | ERP(0–1sfromstimulus |     | 101 |             |           |              |              |             |                  |          |
|     |            |                      |     |     | higher than | chance    | we calculate | the          | chance that | a this           | score or |
|     | electrode) | onset)               |     |     |             |           |              |              |             |                  |          |
higherisobtainedwhenusingarandomclassificationmodel(i.e.,
|     |     | Alphapower(8–13Hz) |     | 1   |     |     |     |     |     |     |     |
| --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ERP+Spectralpower withaprobabilityofclassifyingablockasoneortheotherwith
138
|     |     |     |     |     | a probability | of  | 0.5). In | this way, one | can determine |     | that the |
| --- | --- | --- | --- | --- | ------------- | --- | -------- | ------------- | ------------- | --- | -------- |
features
|     |     |     |     |     | chance of | obtaining | a value | of 0.61 or | higher | given a probabil- |     |
| --- | --- | --- | --- | --- | --------- | --------- | ------- | ---------- | ------ | ----------------- | --- |
Fz(single Thetapower(4–8Hz) 1 ityof50%isequalto0.05(thelevelcorrespondingtop=0.05
electrode)
ine.g.,Figure1).WealsocalculatedBonferronicorrectedlevels
percomparison/figure,andfoundthatwhenthep=0.05signifi-
| Physiology | Skin | Meanskinconductancelevel |     | 1   |     |     |     |     |     |     |     |
| ---------- | ---- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
conductance canceleveliscorrectedformultipletesting(usingBonferroni)this
Minimumskinconductance 1 levelgoesuptothesamelevelastheuncorrectedp=0.01level.
electrodes
level
|     |     |     |     |     | This means | that | the conditions | that | reach an | uncorrected | level |
| --- | --- | --- | --- | --- | ---------- | ---- | -------------- | ---- | -------- | ----------- | ----- |
Respirationbelt Respirationfrequency 1 ofp=0.01maintainsignificanceafterBonferronicorrection(at
|     |     | Respirationmodulationdepth |     | 1   | p=0.05). |     |     |     |     |     |     |
| --- | --- | -------------------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
Pairwisecomparisontestswereusedtodeterminewhethertwo
|     | ECGelectrodes | HR(heartrate—RRI) |     | 1   |     |     |     |     |     |     |     |
| --- | ------------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
accuraciesweresignificantlydifferentfromeachother.Toindicate
|     |     | RMSSD |     | 1   |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thelevelofsignificancechanceandalphalevelsareshowninthe
|     |     | MidfrequencyHRV |     | 1   |     |     |     |     |     |     |     |
| --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
variousfigures.Thefiguresalsoincludeestimatesofthestandard
|     |     | HighfrequencyHRV |     | 1   |     |     |     |     |     |     |     |
| --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
errorinthefractionscorrectbasedonabinomialdistribution.We
didnotcorrectformultipletestingwhichmeansthatestimatesof
| Eye | Eyecamera | Pupilsize |     | 1   |                                    |     |     |     |     |     |     |
| --- | --------- | --------- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
|     |           | Blinkrate |     | 1   | significancelevelsareonthelowside. |     |     |     |     |     |     |
Blinkduration 1 SincetheresultssuggestedthatEEGmodelsmightperformat
|     |     |     |     |     | ceiling level | and | that we | could get a | higher benefit | of combin- |     |
| --- | --- | --- | --- | --- | ------------- | --- | ------- | ----------- | -------------- | ---------- | --- |
ForEEG,thesensors“Allelectrodes,”“Pz”and“Fz”areexaminedusingthefea-
ingvariablesforamoredifficultcasewhereworkloadassessment
turesasdefinedbyERPandspectralpower(printedinitalics).TheEEGsensor
didnotreachceiling,wealsoanalyzedperformanceforclassifying
grouponlyincludesERPandspectralpowerfeaturesof“Allelectrodes.”
smallerworkloaddifferences(2-vs.1-backand1-vs.0-back)and
forclassifying30ratherthan120ssegmentsofdata.Inthelatter
van Gerven et al. (2013).Two types of classifiers were used. We case two of the participants’ data were incomplete due to seg-
used a linear Support Vector Machine as representing a more mentswithoutblinksresultinginundefinedblinkdurationand
|     |     |     |     |     | were discarded | (leaving | 12  | participants). | Using | parts of | blocks |
| --- | --- | --- | --- | --- | -------------- | -------- | --- | -------------- | ----- | -------- | ------ |
standardmodeland,inordertoobtainconfidencemeasuresthat
canbeusedtofuseinformation,weusedanelasticnetmodelwith ratherthancompleteblocksresultedinhaving16datasets(each
logisticregression(Friedmanetal.,2010). 30slong)perparticipantavailabletotestthetrainedclassification
modelratherthan4(each2minlong).
Forcombininginformationacrosssensorgroups,bothfusion
atfeaturelevelandfusionatthedecisionlevelwereinvestigated.
| In the | first (default) | case the concatenated | feature | vector con- | RESULTS |     |     |     |     |     |     |
| ------ | --------------- | --------------------- | ------- | ----------- | ------- | --- | --- | --- | --- | --- | --- |
taining all features was used as the input to a single model. In Taskdifficultyandsubjectiveeffort(workload)weresuccessfully
thelattercase,thefinaldecisionwasbasedontheaverageofthe manipulatedasindicatedbytheexpectedeffectsofn-backlevel
probabilityestimatessuppliedbythelogisticregressionfromthe on performance and subjective ratings (Brouwer et al., 2012).
differentelasticnetmodels,eachbasedontheindividualfeatures Thedifferentn-backlevelsresultedintheexpecteddifferencesin
(one model output for each feature). For instance, if estimated performanceforthe14subjectswithdecreasingfractioncorrect
probabilities on high workload would be based on mean heart (0.96, 0.94, and 0.90 for the 0-back, 1-back, and 2-back con-
rate, mean skin conductance and blink rate with model output ditions) and increasing response times (560, 616, and 730ms
probabilitiesofp1=0.2,p2=0.6,p3=0.5,theaverageprobabil-
|     |     |     |     |     | respectively). | Perceived | mental | effort | as measured | by  | RSME |
| --- | --- | --- | --- | --- | -------------- | --------- | ------ | ------ | ----------- | --- | ---- |
ityofthecombinationmodelis0.43.Thus,thesedatawouldbe increasedwithn-backlevel(31,39,and55forthe0-back,1-back,
assessedtoreflectlowworkload. and2-backconditionsrespectively).
| www.frontiersin.org |     |     |     |     |     |     |     | October2014|Volume8|Article322|7 |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- |

Hogervorstetal. WorkloadfromEEG,physiology,andeyesignals
FIGURE1|Classificationperformance(2-vs.0-back,120s)forseparate (middle)and0.01significancelevel(top).Differentshadesinthebackground
featuresasresultingfromSVMandelasticnetclassificationmodels.The indicatethethreedifferentsensorgroupsEEG,PhysiologyandEye.Errorbars
horizontallinesindicatechancelevel(bottom),0.05significancelevel indicateestimatesofthevariance(s.e.m.s)basedonthebinomialdistribution.
SINGLEVARIABLES Incomparison,modelsbasedoneyemeasuresshowrelatively
Figure1 shows the performance of models that include a sin- goodperformancewithaclassificationaccuracyof0.75forpupil
gle variable or feature (as defined in the second column of size. Blink rate significantly performs above chance as well but
Table1), separately for the SVM and elastic net classification blinkdurationdoesnot.
approaches(seebelow“ClassificationApproach”).Thehorizontal
lines indicate chance level, and levels corresponding to a sig- SINGLESENSORS
nificant difference from chance, for p=0.05 and p=0.01. In Figure2 shows the performance of the “single sensor” models,
general,performanceofmodelsbasedonEEGvariablesismuch i.e., the models that include all features belonging to a certain
betterthanmodelsbasedontheother(single)variables. sensor. Also shown is the performance of the best performing
ERP and spectral power (when using SVM) lead to approxi- single variable model for each sensor type (in which ERP and
mately the same high classification performance of over 0.85 as spectralpowerareregardedasthecorrespondingsinglefeatures
using all EEG features. Moreover, when reducing information forEEGandEEG_Pz.Skinconductancereachesthesignificance
from using EEG or ERP as recorded at all electrodes to only Pz level when features are combined using the elastic net model,
classificationperformanceremainsatthesamelevel.Also,when whileitremainsbelowsignificancelevelforeachindividualfea-
instead of using all frequency bands only alpha is used, perfor- ture.However,andashypothesized,performanceofmodelsusing
mance doesnot deteriorate. Using onlyPz for alpha alone does combinations of features from a single sensor do not perform
reduceperformancerelativetousingallelectrodes(p<0.05).A significantly better compared to using only the best performing
modelbasedonthethetabandalonedoesnotperformaswellas singlefeatureforanyofthesensors.Again,theEEGmodelshows
usingallfrequencies(p<0.05),indicatingthatthethetabandis thebestperformance(withanaccuracyof0.86forbothclassifi-
lessinformativeinourcase(incorrespondencewithourprevious cationapproaches).Secondbestistheperformanceofthemodels
findings,seeBrouweretal.,2012). based on eye measures (accuracy of 0.75 for SVM). Also the
Modelsbasedonthephysiologicalvariablesperformrelatively modelbasedonrespirationreachesarelativelyhighperformance
poorly with respiration frequency being the only feature that level(accuracyof0.70forbothclassificationapproaches).Models
reachesthe0.01significancelevelwithanaccuracyof0.68.High basedonskinconductance(accuracyof0.63forelasticnet)and
frequency HRV (as defined by RMSSD and spectrally defined) ECG(accuracyof0.61forelasticnet)showrelativelypoorperfor-
is the only other physiological feature that, depending on the mance,justreachingalevelthatissignificantlyhigherthanchance
classificationapproach,justreachessignificance(p<0.05). (p<0.05).Pairwisecomparisontests(usingtheSVM-data)show
FrontiersinNeuroscience|Neuroprosthetics October2014|Volume8|Article322|8

Hogervorstetal. WorkloadfromEEG,physiology,andeyesignals
givesusanimpressionofhowmuchlowerclassificationperfor-
mance is under these circumstances. Shorter time segments are
expected to be more difficult to classify because the extraction
information will be less reliable. This is especially obvious for
someofthenon-EEGmeasures(e.g.,forhighfrequencyheartrate
variabilityminimumdurationsof1minareadvised:TaskForceof
theEuropeanSocietyofCardiologytheNorthAmericanSociety
ofPacingElectrophysiology,1996;Berntsonetal.,1997).
Figure3Bshowstheperformanceofthemodelsforclassifying
datasegmentsof30sinsteadof120s.Notethatthisincludesdata
from12insteadof14participants(seeMaterialsandMethods).
Thethresholdsforsignificancedecreaseinthiscasesincethetest
setcontains16samplesinsteadof4.Asexpected,performancefor
classifying 30s segments is lower than for classifying 120s seg-
ments, with a performance that is (on average) 8% (SVM) and
5%(elasticnet)lower.Still,performanceformodelsthatinclude
EEGisaround0.8orhigherfortheelasticnetmodel.Thepattern
ofresultsishighlysimilartothatforclassifying120ssegments—
thus,theredoesnotseemtobealargerbenefitofsensorgroup
FIGURE2|Classificationperformance(2-vs.0-back,120s)forseparate combinationthaninthepreviouscase,suggestingthatthelackof
sensors.ConventionsasinFigure1.Forcomparison,performanceofthe
improvementofaddingnon-EEGvariablestotheEEGmodelis
bestperformingfeatureforeachofsensorisdepicted.
notduetoaceilingeffect.
Figure3C shows classification performance for classifying 2-
that the EEG models are significantly different from the other backvs.1-backusing2-minblocks.Figure3Dshows1-backvs.
models (p<0.01), and that performance of the eye model is 0-backclassificationperformance.Asexpected,performancefor
significantly better than that of the skin conductance and ECG discriminatingsmallerdifferencesinworkloadislowerthanfor
models(p<0.05). discriminating2-backvs.0-back.Performanceisonaverage10%
(SVM)and6%(elasticnet)lowerfor2vs.1-back,withperfor-
COMBINATIONSACROSSSENSORGROUPS mance around 0.85 for elastic net models including EEG. It is
Figure3 shows the results for different (combinations of) sen- 22% (SVM) and 18% (elastic net) lower for 1 vs. 0-back, with
sor groups of SVM and elastic net, as well as the outcome of performancejustbelow0.70forelasticnetmodelsincludingEEG.
combiningtheoutputsofdifferentelasticnetmodels(“decision Thissuggestsalargerincreaseinworkloadfrom1-backto2-back
level”). Shown are the results for the default case of classifying than from 0-back to 1-back in accordance with earlier findings
2 vs. 0-back over 2min. data segments (a) as well as for more (Brouwer et al., 2012, 2014). Again, models that include EEG
difficult cases: using 30s data segments (b), or classifying 2 vs. variables show the best performance. Performance of classifica-
1-back (c), or 1 vs. 0-back (d). Comparing performance in the tion models based on Physiology is not significantly different
defaultcase(Figure3A)withthatofseparatesensors(Figure2) from chance for both small workload differences, and the Eye
showsthatforPhysiology,combiningthethreesensorsleadstoa basedmodeldropstochancelevelwhendistinguishing1-from
(non-significant) increase in performance (accuracy of 0.75 for 0-back.
SVM, compared to 0.70 for the best performing single physi- AlsoincludedinFigure3istheperformanceofthe“decision
ological sensor respiration). Models that include EEG perform level” model that combines the output of different elastic net
significantlybetterthanphysiologyandeyemodels(SVM,pair- models (based on single features). We did not find any signifi-
wisecomparisons,p<0.05).Addingsensorgroupstothealready cant differences between performance of the elastic net models
well performing EEG improves classification accuracy by 3–5% thatusethetwotypesoffusion;trendsindicateanadvantageof
(for adding Physiology or Eye variables with elastic net). For fusionatthefeaturelevelcomparedtofusionatthedecisionlevel.
SVM, the combination of physiology and eye measures tends Figure4showstheeffectofaddingthefeaturetime(i.e.,the
to improve performance relative to either one alone by 7% as time of measurement, since the start of the experiment) to the
well. However, all of these improvements do not reach statisti- model input for the default case (2- vs. 1-back, 120s of data).
calsignificance.Usingtheassumptionofabinomialdistribution, Adding time leads to an increase in performance of 9% (sig-
significance(p<0.05)isreachedfordifferencesofaround10%. nificant at p<0.05) and 5% (not significant) for respectively
Wemaynotobservealarger,statisticallysignificantimprove- physiological and eye sensor group models (SVM) when classi-
ment of combining EEG with physiology (as we had hypoth- fying 2- vs. 0-back using 120s of data. For EEG and “All” the
esized) because EEG alone is already performing very well. inclusion of time information does not improve performance.
Therefore,weperformedthesameanalysesonmorechallenging Furtheranalysisofthedatashowsthatwhenclassificationismore
classificationtasks,namelyclassificationofshortertimesegments difficult due to shorter time intervals or smaller workload dif-
(30sratherthan120s)andclassificationofmoresimilarwork- ferences (see Figures3B–D), the potentially beneficial effect of
loadlevels(2-vs.1-backand1-backvs.0-back).Inaddition,this includingtimedecreases.
www.frontiersin.org October2014|Volume8|Article322|9

Hogervorstetal. WorkloadfromEEG,physiology,andeyesignals
FIGURE3|Classificationperformanceforseparateandcombinedsensor thedefaultcondition(2-vs.0-back,120sofdata,(B)forcomparing2-vs.
groupsforSVM,elasticnetandamodelthatcombinestheoutputs 0-backover30sofdata,(C)forcomparing2-vs.1-back(120sofdata),(D)for
fromdifferentsinglefeaturemodels(“decisionlevel”).(A)performancein comparing1-vs.0-back(120sofdata).
CONCLUSIONANDDISCUSSION 70 and 75% accuracy. As hypothesized, the difference in clas-
SUMMARYOFFINDINGS sification accuracy between models based on EEG variables on
Inthisstudy,wecomparedhowwelldifferentphysiologicalvari- the one hand, and models based on peripheral physiology and
ablescanbeusedtoassessworkloadin(simulated)realtimefora eye-related variables on the other hand was statistically signif-
singleindividual,whentheamountofbodymovementandvisual icant. The best performing single variable was ERP at Pz with
informationarecontrolledfor.Wealsoexaminedtowhatextent 88% accuracy (elastic net). All EEG variables (except power in
(differentwaysof)combininginformationleadstobetterclassi- thethetabandmeasuredatFz)performedwellabovechance(p<
ficationperformance,aswellaswhethertakingtimeintoaccount 0.01).Theonlynon-EEGvariablesexceedingthe0.01chancelevel
improvesperformance. wererespirationfrequency (69%accuracy) andpupilsize(75%
Classificationmodelsbasedondatafromeachofthethreesen- accuracy).
sorgroupsperformabovechance(distinguishinghighfromlow Ashypothesized,combiningvariablesrecordedusingasingle
workload)ata0.01significancelevel,whereEEGreachedaround sensor(i.e.,onlytheEEGelectrodes,electrodePz,skinconduc-
86% classification accuracy and classification models based on tance electrodes, respiration belt, ECG electrodes or eye cam-
peripheralphysiologyandeye-relatedvariablesreachedbetween era) does not significantly improve performance over the best
FrontiersinNeuroscience|Neuroprosthetics October2014|Volume8|Article322|10

| Hogervorstetal. |     |     |     |     |     |     |     |     |     |     | WorkloadfromEEG,physiology,andeyesignals |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- |
physiologicalandeyedata,performedlowerthanEEGvariables.
|     |     |     |     |     |     |     |     | Giving more | weight | to  | variables | with a | lower | performance | is  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | --- | --------- | ------ | ----- | ----------- | --- |
notnecessarilybeneficial.Inaddition,classificationmodelsbased
|     |     |     |     |     |     |     |     | on concatenation |     | may be | making | more optimal |     | use of interac- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------ | ------ | ------------ | --- | --------------- | --- |
tionsbetweenvariablesthataremissedwhenfusionoccursatthe
decisionlevel.
|     |     |     |     |     |     |     |     | Including      | the               | time of     | measurement | relative      |               | to the start   | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ----------------- | ----------- | ----------- | ------------- | ------------- | -------------- | --- |
|     |     |     |     |     |     |     |     | the experiment | as                | a parameter |             | leads to      | statistically | significant    |     |
|     |     |     |     |     |     |     |     | improvements   | of                | up to       | 9% for      | physiological | variables.    | Adding         |     |
|     |     |     |     |     |     |     |     | time did       | not significantly |             | improve     | performance   |               | of classifiers |     |
basedonEEG,eye-relatedvariablesorcombinationsofvariables.
Thelattercannotbeattributedtoaceilingeffect,asindicatedby
analysisofdatafromshortertimesegmentsorsmallerworkload
differences.
COMBINATIONOFINFORMATION
|     |     |     |     |     |     |     |     | The notion | that combining |     | physiological |     | variables | that reflect | a   |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------------- | --- | ------------- | --- | --------- | ------------ | --- |
certainmentalstatewillresultinamoreaccurateassessmentof
thismentalstatecomparedtousingthesevariablesontheirown
seemsverysensibleandhasfrequentlybeensuggestedinthelit-
|     |     |     |     |     |     |     |     | erature as | a potential | way | to improve | mental | state | assessment. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | ---------- | ------ | ----- | ----------- | --- |
However,wearenotawareofstudiesthattriedthisandshowed
|     |     |     |     |     |     |     |     | a statistically | reliable | and | strong | improvement. |     | A few | studies |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | -------- | --- | ------ | ------------ | --- | ----- | ------- |
FIGURE4|Classificationperformanceinthedefaultcondition(2-vs.
|     |     |     |     |     |     |     |     | explicitly | mention | that | combination | of physiological |     | informa- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ---- | ----------- | ---------------- | --- | -------- | --- |
0-back,120s)forthedifferentsensortypesandusingallavailable
input.Thestripedbarsshowtheeffectofaddingthetimefeature. tion did not result in reliable improvement (e.g., Christensen
ConventionsasinFigure1. et al., 2012; Coffey et al., 2012; Severens et al., 2013) or only to
|     |     |     |     |     |     |     |     | a modest     | degree  | in one | of multiple | conditions     | (Brouwer    |     | et al., |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | ------ | ----------- | -------------- | ----------- | --- | ------- |
|     |     |     |     |     |     |     |     | 2012). Other | studies | report | that        | classification | performance |     | of      |
performing single variable from that sensor. Variables from the models combining information increases classification accuracy
samesensorarelikelyhighlycorrelatedand,inourexperiment, (by a small amount) but do not provide statistical evidence to
showthattheeffectisreliable(e.g.,Chaneletal.,2009).Wehad
| combining | them | has no | added | value. For | four | out of | the six |     |     |     |     |     |     |     |     |
| --------- | ---- | ------ | ----- | ---------- | ---- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
sensors the trend was even that performance worsened when anticipated that our study could provide clear evidence for the
combiningdata. benefit of combination given the nature of workload, which is
Combining variables of the three physiological sensors (skin a mental state that involves multiple processes that are presum-
|             |             |     |             |      |         |             |     | ably reflected | by  | different | types | of physiological |     | variables | (e.g., |
| ----------- | ----------- | --- | ----------- | ---- | ------- | ----------- | --- | -------------- | --- | --------- | ----- | ---------------- | --- | --------- | ------ |
| conductance | electrodes, |     | respiration | belt | and ECG | electrodes) |     |                |     |           |       |                  |     |           |        |
resulted in a modest, non-significant improvement to around cognitiveprocessesbyEEGandarousalbyperipheralphysiolog-
75% classification accuracy with respect to the best perform- icalmeasures).Also,whilemoststudiescombineinformationby
fusionatthefeaturelevel,wethoughtthatfusionofinformation
| ing single | physiological |     | sensor | (respiration—around |     | 70%). | In  |     |     |     |     |     |     |     |     |
| ---------- | ------------- | --- | ------ | ------------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
contrasttowhatweexpected,combiningEEGwithanothersen- at the decision level could have contributed to finding a strong
sor group (physiology and eyes) does not lead to a significant reliable advantage of combining information. However, we did
improvement in classification accuracy over EEG alone. Using not find significant differences between the two methods, with
elasticnet,weonlyfoundnon-significanttrendsofbetterperfor- theoveralltrendindicatingworseratherthanbetterperformance
manceforEEGcombinedwitheyedata(91%accuracy)andEEG for fusion at the decision. The fact that with this study, there is
combined with physiology (89%) than EEG alone (86% accu- still no evidence of large benefits when combining physiologi-
calvariablesreflectingworkloadsuggeststhattheyaretoohighly
| racy). Adding | physiology |     | to fused | EEG | and eye | data does | not |     |     |     |     |     |     |     |     |
| ------------- | ---------- | --- | -------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
further improve, or tend to improve, performance. Analysis of relatedtogainabenefitofcombination.Itcouldbethecasethat
datafromshortertimesegmentsorsmallerworkloaddifferences meta-analysesorastudysuchasoursincludingmoreparticipants
wouldturnnon-significanttrendsoffusionbenefitsintostatisti-
| indicatesthatthefact |     | thatwedidnotgetastronger, |     |     |     | significant |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | ------------------------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
improvement of adding physiological or eye data to EEG is not cally significant effects. However, if present at all, the effects of
causedbyaceilingeffect. data fusion are at least small. Also, it may be the case that for
Fusionofvariablesbyconcatenatingfeaturevectorscouldnot other tasks (perhaps involving more strong emotional process-
ingbesidescognitiveprocesses)benefitsoffeaturefusioncanbe
| be improved | by fusing | variables |     | at the decision |     | level. The | latter |     |     |     |     |     |     |     |     |
| ----------- | --------- | --------- | --- | --------------- | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
approach results in a more balanced weighting of the different foundmoreeasily.
| indicators | compensating |     | for the | low number | of  | features | from |     |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | ------- | ---------- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
physiologicalandeye-basedvariablesrelativetoEEG,andcould WORKLOADASSESSMENTPERFORMANCE
thereforehaveimprovedclassification.Asitturnedout,thevari- Classificationaccuracyfordistinguishing2-minsegmentsofhigh
ablesthatmayhaveprofitedofthedecisionlevelapproach,i.e., vs.lowworkloadforasingleindividualisrelativelyhigh(withan
| www.frontiersin.org |     |     |     |     |     |     |     |     |     |     | October2014|Volume8|Article322|11 |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- |

Hogervorstetal. WorkloadfromEEG,physiology,andeyesignals
averageoverparticipantsupto91%),especiallywhenconsidering minorimprovementinperformancebyfusingdifferentworkload
the fact that the amount of movements and visual informa- measuresmayhavebeenthattheexperimentcontrolledformany
tionwasthesameacrossworkloadlevels,andthatclassification ofsuchconfoundingfactors,thusdecreasingtheadditionalben-
simulatedarealtimesituation. efit of recording various physiological measures. In this way we
When the duration of to be classified data segments was werebetterabletodeterminewhichfactorsdirectlyreflectmental
decreased to 30s, this resulted in a relatively small decrease in workload. However, in practical situations, physiological mea-
performance, of on average 5% (elastic net) to 8% (SVM). The suresmaysupplyinformationaboutthecontextandcontribute
resultsfurthershowthatdiscriminationbetweenmoresubtledif- to workload assessment in a more indirect way, i.e., via the
ferences in workload is possible as well. These results are good confounds. In such a case one should determine whether phys-
newsforpotentialuseinapplications.Anotherfindingthatisuse- iological measures are the most convenient measures to supply
fulforpracticalapplicationsisthatperformancebasedonasingle workload information, or whether task or behavioral measures
Pz-channelwasfoundtobecomparabletothatofamodelusing (such as the detection of speech through audio sensors with
all EEG-channels. This means that in our case a single channel respecttoourpreviousATCexample)aremoresuitable.
sufficestocharacterizetheEEG.
Asreported,wefoundEEGvariablestobemostinformative
ACKNOWLEDGMENTS
whenassessingworkload.However,wealsofoundpupilsizeand
We would like to thank Pjotr van Amerongen, Rob van de
blink rate to reflect workload. This is interesting given the fact
Pijpekamp, Tobias Heffelaar and Patrick Zimmerman (Noldus)
thatlightingconditionsandvisualinputwerestrictlycontrolled
for technical assistance, Marcel van Gerven and Jason Farquar
inourexperiment.Theseresultsthusindicatethatnotonlypupil
for contributions to the multivariate analysis tools and the
sizebutalsoblinkrateisaffectedbymentalworkloadlevelapart
SVM method in the FieldTrip toolbox, Boris Reuderink
fromvisualdemands.
and Robert Oostenveld for fruitful discussions. This research
has been supported by the GATE project, funded by the
GROUPvs.INDIVIDUALLEVEL
Netherlands Organization for Scientific Research (NWO) and
In the present study, we examine how well different variables
the Netherlands ICT Research and Innovation Authority (ICT
can be used to assess workload in real time for a single indi-
Regie).Furthermore,theauthorsgratefullyacknowledgethesup-
vidual by training classification models on different types of
portoftheBrainGainSmartMixProgrammeoftheNetherlands
information and comparing performance. Sensitivity of physio-
Ministry of Economic Affairs and the Netherlands Ministry of
logicalvariablesisoftenexaminedusinggrouplevelanalyses(e.g.,
Education,CultureandScience.
usingrepeatedmeasuresANOVAs).However,forvariousreasons
(seeIntroduction)onecannotdrawstraightforwardconclusions
aboutassessingworkloadonanindividuallevelfromtheresults REFERENCES
on a group level. For instance, in the current study we found Aasman, J., Mulder, G., and Mulder, L. J. M. (1987). Operator effort and the
measurementofheartratevariability.Hum.Factors29,161–170.
that classification models based on heart rate performed badly,
Allison, B. Z., and Polich, J. (2008). Workload assessment of computer gam-
while,forbasicallythesamesetofdata,thisvariablewasfound ingusingasingle-stimulusevent-relatedpotentialparadigm.Biol.Psychol.77,
to be among the ones most strongly associated with workload 277–283.doi:10.1016/j.biopsycho.2007.10.014
inarepeatedmeasuresANOVA(Brouweretal.,2014).Brouwer Ayaz,H.,Izzetoglu,M.,Bunce,S.,Heiman-Patterson,T.,andOnaral,B.(2007).
“Detectingcognitiveactivityrelatedhemodynamicsignalforbraincomputer
et al. (2014) also found that heart rate strongly decreased over
interface using functional near infrared spectroscopy,” in 3rd International
thetimecourseoftheexperiment.Sincewepresentedworkload
IEEE/EMBSConferenceonNeuralEngineering(KohalaCoast,HI),342–345.
conditionsin2-minsegmentsequallydispersedovertime,even Bauer, L. O., Goldstein, R., and Stern, J. A. (1987). Effects of information-
strongtimeeffectsareaveragedoutinrepeatedmeasureANOVAs processing demands on physiological response patterns. Hum. Factors 29,
whereas they could overrule the comparatively small workload 213–234.
Beatty,J.(1982).Task-evokedpupillaryresponses,processingload,andthestruc-
effectsinclassificationtypeofanalyses,especiallywhenclassifica-
ture of processing resources. Psychol. Bull. 91, 276–292. doi: 10.1037/0033-
tionmodelsaretrainedondataacquiredatthestartoftheexperi-
2909.91.2.276
mentandtestedondataattheend.Thus,cautionshouldbetaken Berka,C.,Levendowski,D.J.,Lumicao,M.N.,Yau,A.,Davis,G.,Zivkovic,V.T.,
whengeneralizingresultsfromstudiesusinggrouplevelanalysis etal.(2007).EEGcorrelatesoftaskengagementandmentalworkloadinvig-
tosituationswheremomentarydataofindividualsisused. ilance,learning,andmemorytasks.Aviat.SpaceEnviron.Med.78(5Suppl.),
B231–B244.
Berntson, G. G., Bigger, J. T., Eckberg, D. L., Grossman, P., Kaufmann, P. G.,
NOISEANDCONFOUNDSINREALLIFE Malik,M.,etal.(1997).Heartratevariability:origins,methods,andinterpretive
Inreal-life,out-of-the-labsituations,thepresenceoffactorslike caveats.Psychophysiology34,623–648.doi:10.1111/j.1469-8986.1997.tb02140.x
body movement and varying light conditions may act as noise, Boucsein,W.(1992).ElectrodermalActivity.NewYork,NY:PlenumPress.
Boucsein,W.(1999).Electrodermalactivityasanindicatorofemotionalprocesses.
therewith diminishing the value of certain variables (e.g., pupil
J.Sci.Emot.Sensib.2,1–25.
size). Also, levels of workload can be confounded with differ-
Brookings, J. B., Wilson, G. F., and Swain, C. R. (1996). Psychophysiological
entlevelsofstimulusprocessingormotoractions.Forexample, responses to changes in workload during simulated air traffic control. Biol.
workload in Air Traffic Control may be confounded by speech, Psychol.42,361–377.doi:10.1016/0301-0511(95)05167-8
where controllers talking more during high than during low Brouwer, A.-M., Hogervorst, M. A., Herman, P., and Kooi, F. (2009). “Are
you really looking? Finding the answer through fixation patterns and EEG.
workloadsituations.Suchconfoundsmayaffectphysiology(e.g.,
Lecture notes in artificial intelligence, Vol. 5638,” in Proceedings of the 5th
speech affects respiration), resulting in improved classification
International Conference on Foundations of Augmented Cognition (Berlin;
accuracy. One of the reasons for the fact that we only found a Heidelberg:Springer),329–338.
FrontiersinNeuroscience|Neuroprosthetics October2014|Volume8|Article322|12

Hogervorstetal. WorkloadfromEEG,physiology,andeyesignals
Brouwer,A.-M.,Hogervorst,M.A.,Holewijn,M.,andvanErp,J.B.F.(2014). Grimes,D.,Tan,D.S.,Hudson,S.E.,Shenoy,P.,andRao,R.P.(2008).“Feasibility
Evidenceforeffectsoftaskdifficultybutnotlearningonneurophysiological andpragmaticsofclassifyingworkingmemoryloadwithanelectroencephalo-
variablesassociatedwitheffort.Int.J.Psychophysiol.93,242–252.doi:10.1016/ graph,”inProceedingoftheTwenty-SixthAnnualSIGCHIConferenceonHuman
j.ijpsycho.2014.05.004 FactorsinComputingSystems(Florence:ACM),835–844.
Brouwer,A.-M.,Hogervorst,M.A.,vanErp,J.B.F.,Heffelaar,T.,Zimmerman, Grossman,P.,andTaylor,E.W.(2007).Towardunderstandingrespiratorysinus
P. H., and Oostenveld, R. (2012). Estimating workload using EEG spectral arrhythmia:relationstocardiacvagaltone,evolutionandbiobehavioralfunc-
powerandERPsinthen-backtask.J.NeuralEng.9:045008.doi:10.1088/1741- tions.Biol.Psychol.74,263–285.doi:10.1016/j.biopsycho.2005.11.014
2560/9/4/045008 Gundel, A., and Wilson, G. F. (1992). Topographical changes in the ongoing
Brouwer,A.-M.,vanWouwe,N.,Mühl,C.,vanErp,J.B.F.,andToet,A.(2013). EEG related to the difficulty of mental task. Brain Topogr. 5, 17–25. doi:
Perceivingblocksofemotionalpicturesandsounds:effectsonphysiological 10.1007/BF01129966
variables.Front.Hum.Neurosci.7:295.doi:10.3389/fnhum.2013.00295 Hampson,R.E.,Opris,I.,andDeadwyler,S.A.(2010).Neuralcorrelatesoffast
Chanel,G.,Kierkels,J.J.M.,Soleymani,M.,andPun,T.(2009).Short-termemo- pupildilationinnonhumanprimates:relationtobehavioralperformanceand
tionassessmentinarecallparadigm.Int.J.Hum.Comput.St.67,607–627.doi: cognitiveworkload.Behav.BrainRes.212,1–11.doi:10.1016/j.bbr.2010.03.011
10.1016/j.ijhcs.2009.03.005 Hancock,P.A.,Meshkati,N.,andRobertson,M.M.(1985).Physiologicalreflec-
Chanel, G., Kronegg, J., Grandjean, D., and Pun, T. (2006). “Emotion assess- tionsofmentalworkload.Aviat.SpaceEnviron.Med.56,1110–1114.
ment:arousalevaluationusingEEG’sandperipheralphysiologicalsignals,”in Hart,S.G.,andStaveland,L.E.(1988).“Developmentofamulti-dimensional
MultimediaContentRepresentationClassificationandSecurity.SpringerLecture workloadratingscale:resultsofempiricalandtheoreticalresearch,”inHuman
Notes in Computer Sciences, Vol. 4105, eds B. Gunsel, A. M. Tekalp, A. K. MentalWorkload,edsP.A.HancockandN.Meshkati(Amsterdam:Elsevier),
Jain, and B. Sankur (Berlin; Heidelberg: Springer), 530–537. doi: 10.1007/ 139–183.
11848035_70 Hockey,G.R.J.(1986).“Changesinoperatorefficiencyasafunctionofenviron-
Christensen,J.C.,Estepp,J.R.,Wilson,G.F.,andRussell,C.A.(2012).Theeffects mentalstress,fatigue,andcircadianrhythms,”inHandbookofPerceptionand
ofday-to-dayvariabilityofphysiologicaldataonoperatorstateclassification. HumanPerformance,Vol.2,edsK.R.Boff,L.Kaufman,andJ.P.Thomas(New
Neuroimage59,57–63.doi:10.1016/j.neuroimage.2011.07.091 York,NY:JohnWiley),44.1–44.49.
Coffey,E.B.J.,Brouwer,A.M.,andvanErp,J.B.F.(2012).Measuringwork- Izzetoglu,M.,Bunce,S.C.,Izzetoglu,K.,Onaral,B.,andPourrezaei,A.K.(2007).
loadusingacombinationofelectroencephalographyandnearinfraredspec- Functionalbrainimagingusingnear-infraredtechnology.IEEEEng.Med.Biol.
troscopy. Proc. Hum. Factors Ergon. Soc. Annu. Meet. 56, 1822–1826. doi: Mag.26,38–46.doi:10.1109/MEMB.2007.384094
10.1177/1071181312561367 Jann,K.,Dierks,T.,Boesch,C.,Kottlow,M.,Strik,W.,andKoenig,T.(2009).BOLD
Esposito, F., Aragri, A., Piccoli, T., Tedeschi, G., Goebel, R., and Di Salle, F. correlatesofEEGalphaphase-lockingandthefMRIdefaultmodenetwork.
(2009). Distributed analysis of simultaneous EEG-fMRI time-series: mod- Neuroimage45,903–916.doi:10.1016/j.neuroimage.2009.01.001
eling and interpretation issues. Magn. Reson. Imaging 27, 1120–1130. doi: Jensen,O.,andTesche,C.D.(2002).Frontalthetaactivityinhumansincreaseswith
10.1016/j.mri.2009.01.007 memoryloadinaworkingmemorytask.Eur.J.Neurosci.15,1395–1399.doi:
Evans,J.L.,Selinger,C.,andPollak,S.D.(2011).P300asameasureofprocessing 10.1046/j.1460-9568.2002.01975.x
capacityinauditoryandvisualdomainsinspecificlanguageimpairment.Brain Kahneman,D.,andBeatty,J.(1966).Pupildiameterandloadonmemory.Science
Res.1389,93–102.doi:10.1016/j.brainres.2011.02.010 154,1583–1585.doi:10.1126/science.154.3756.1583
Fairclough, S. H., Venables, L., and Tattersall, A. (2005). The influence of task Kahneman,D.,Tursky,B.,Shapiro,D.,andCrider,A.(1969).Pupillary,heartrate,
demandandlearningonthepsychophysiologicalresponse.Int.J.Psychophysiol. andskinresistancechangesduringamentaltask.J.Exp.Psychol.79,164–167.
56,171–184.doi:10.1016/j.ijpsycho.2004.11.003 doi:10.1037/h0026952
Fink,A.,Grabner,R.H.,Neuper,C.,andNeubauer,A.C.(2005).EEGalphaband Kalsbeek,J.W.H.,andEttema,J.(1963).Scoredregularityoftheheartratepattern
dissociationwithincreasingtaskdemands.Cogn.BrainRes.24,252–259.doi: andthemeasurementofperceptualormentalload.Ergonomics6:306.
10.1016/j.cogbrainres.2005.02.002 Karavidas, M. K., Lehrer, P. M., Lu, S.-E., Vaschillo, E., Vaschillo, B., and
Fogarty,C.,andStern,J.A.(1989).Eyemovementsandblinks:theirrelationship Cheng, A. (2010). The effects of workload on respiratory variables in
tohighercognitiveprocesses.Int.J.Psychophysiol.8,35–42.doi:10.1016/0167- simulated flight: a preliminary study. Biol. Psychol. 84, 157–160. doi:
8760(89)90017-2 10.1016/j.biopsycho.2009.12.009
Fournier,L.R.,Wilson,G.F.,andSwain,C.R.(1999).Electrophysiological,behav- Keil,A.,Mussweiler,T.,andEpstude,K.(2006).Alpha-bandactivityreflectsreduc-
ioral, and subjective indexes of workload when performing multiple tasks: tionofmentaleffortinacomparisontask:asourcespaceanalysis.BrainRes.
manipulationsoftaskdifficultyandtraining.Int.J.Psychophysiol.31,129–145. 1121,117–127.doi:10.1016/j.brainres.2006.08.118
doi:10.1016/S0167-8760(98)00049-X Kida,T.,Nishihira,Y.,Hatta,A.,Wasaka,T.,Tazoe,T.,Sakajiri,Y.,etal.(2004).
Foxe,J.J.,Simpson,G.V.,andAhlfors,S.P.(1998).Parieto-occipital∼10Hzactiv- ResourceallocationandsomatosensoryP300amplitudeduringdualtask:effects
ityreflectsanticipatorystateofvisualattentionmechanisms.Neuroreport 9, oftrackingspeedandpredictabilityoftrackingdirection.Clin.Neurophysiol.
3929–3933.doi:10.1097/00001756-199812010-00030 115,2616–2628.doi:10.1016/j.clinph.2004.06.013
Friedman,J.,Hastie,T.,andTibshirani,R.(2010).Regularizationpathsforgener- Klimesch, W., Doppelmayr, M., Röhm, D., Pöllhuber, D., and Stadler, W.
alizedlinearmodelsviacoordinatedescent.J.Stat.Softw.33,1–22. (2000).Simultaneousdesynchronizationandsynchronizationofdifferentalpha
Gaillard, A. W. K., and Wientjes, C. J. E. (1994). Mental load and work responsesinthehumanelectroencephalograph:aneglectedparadox?Neurosci.
stress as two types of energy mobilization. Work Stress 8, 141–152. doi: Lett.284,97–100.doi:10.1016/S0304-3940(00)00985-X
10.1080/02678379408259986 Klimesch,W.(1996).Memoryprocesses,brainoscillationsandEEGsynchroniza-
Gawron, V. J., Schiflett, S. G., and Miller, J. C. (1989). “Measures of in-flight tion.Int.J.Psychophysiol.24,61–100.doi:10.1016/S0167-8760(96)00057-8
workload,” in Aviafion Psychology, ed R. S. Jensen (Aldershot: Brookfield), Klimesch, W. (1997). EEG-alpha rhythms and memory processes. Int. J.
240–287. Psychophysiol.26,319–340.doi:10.1016/S0167-8760(97)00773-3
Gevins, A., Smith, M. E., Leong, H., McEvoy, L., Whitfield, S., Du, R., Klimesch,W.(1999).EEGalphaandthetaoscillationsreflectcognitiveandmem-
et al. (1998). Monitoring working memory load during computer-based oryperformance:areviewandanalysis.BrainRes.BrainRes.Rev.29,169–195.
tasks with EEG pattern recognition methods. Hum. Factors 40, 79–91. doi: doi:10.1016/S0165-0173(98)00056-3
10.1518/001872098779480578 Kohlisch,O.,andSchaefer,F.(1996).Physiologicalchangesduringcomputertasks:
Goedhart,A.D.,vanderSluis,S.,Houtveen,J.H.,Willemsen,G.,anddeGeus, responsestomentalloadortomotordemands?Ergonomics39,213–224.doi:
E.J.(2007).ComparisonoftimeandfrequencydomainmeasuresofRSAin 10.1080/00140139608964452
ambulatoryrecordings.Psychophysiology44,203–215.doi:10.1111/j.1469-8986. Kramer, A. F., Trejo, L. J., and Humphrey, D. (1995). Assessment of mental
2006.00490.x workloadwithtask-irrelevantauditoryprobes.Biol.Psychol.40,83–100.doi:
Greenwald,M.K.,Cook,E.W.,andLang,P.J.(1989).Affectivejudgmentand 10.1016/0301-0511(95)05108-2
psychophysiological response: dimensional covariation in the evaluation of Laufs,H.,Krakow,K.,Sterzer,P.,Eger,E.,Beyerle,A.,Salek-Haddadi,A.,etal.
pictorialstimuli.J.Psychophysiol.3,51–64. (2003).Electroencephalographicsignaturesofattentionalandcognitivedefault
www.frontiersin.org October2014|Volume8|Article322|13

Hogervorstetal. WorkloadfromEEG,physiology,andeyesignals
modesinspontaneousbrainactivityfluctuationsatrest.Proc.Natl.Acad.Sci. measurement, physiological interpretation and clinical use. Circulation 93,
U.S.A.100,11053–11058.doi:10.1073/pnas.1831638100 1043–1065.doi:10.1161/01.CIR.93.5.1043
May,J.G.,Kennedy,R.S.,Williams,M.C.,Dunlap,W.P.,andBrannan,J.R. Taylor, G., Reinerman-Jones, L. E., Cosenzo, K., and Nicholson, D. (2010).
(1990).Eyemovementindicesofmentalworkload.ActaPsychol.75,75–89.doi: “Comparisonofmultiplephysiologicalsensorstoclassifyoperatorstateinadap-
10.1016/0001-6918(90)90067-P tiveautomationsystems,”inProceedingsoftheHumanFactorsandErgonomics
Mehler,B.,Reimer,B.,Coughlin,J.F.,andDusek,J.A.(2009).Impactofincremen- SocietyAnnualMeetingSeptember2010.Vol.54(SanFrancisco,CA:Human
talincreasesincognitiveworkloadonphysiologicalarousalandperformancein FactorsandErgonomicsSociety),195–199.
youngadultdrivers.Transport.Res.Rec.2138,6–12.doi:10.3141/2138-02 Ullsperger,P.,Freude,G.,andErdmann,U.(2001).Auditoryprobesensitivityto
Missonnier,P.,Gold,G.,Leonards,U.,Costa-Fazio,L.,Michel,J.-P.,Ibáñez,V., mentalworkloadchanges-anevent-relatedpotentialstudy.Int.J.Psychophysiol.
etal.(2004).Agingandworkingmemory:earlydeficitsinEEGactivationof 40,201–209.doi:10.1016/S0167-8760(00)00188-4
posteriorcorticalareas.J.NeuralTransm.111,1141–1154.doi:10.1007/s00702- van Dijk, H., Schoffelen, J. M., Oostenveld, R., and Jensen, O. (2008). Pre-
004-0159-2 stimulus oscillatory activity in the alpha band predicts visual discrimi-
Missonnier,P.,Leonards,U.,Gold,G.,Palix,J.,Ibáñez,V.,andGiannakopoulos,P. nation ability. J. Neurosci. 28, 1816–1823. doi: 10.1523/JNEUROSCI.1853-
(2003).Anewelectrophysiologicalindexforworkingmemoryloadinhumans. 07.2008
Neuroreport14,1451–1455.doi:10.1097/00001756-200308060-00009 vanGerven,M.,Bahramisharif,A.,Farquhar,J.,andHeskes,T.(2013).Donders
Miyata,Y.,Tanaka,Y.,andHono,T.(1990).LongtermobservationonFm-theta Machine Learning Toolbox (DMLT) for Matlab Version 26/06/2013. Available
duringmentaleffort.Neuroscience16,145–148. onlineat:https://github.com/distrep/DMLT.
Mulder,G.(1980).TheHeartofMentalEffort.Thesis,UniversityofGroningen, Veltman, J. A., and Gaillard, A. W. K. (1996). Physiological indices of work-
Groningen. loadinasimulatedflighttask.Biol.Psychol.42,323–342.doi:10.1016/0301-
Mulder,L.J.M.,andMulder,G.(1987).“Cardiovascularreactivityandmental 0511(95)05165-1
workload,”inTheBeat-by-BeatInvestigationofCardiovascularFunction,edsR. Veltman, J. A., and Gaillard, A. W. K. (1998). Physiological workload reac-
I.KitneyandO.Rompelman(Oxford:ClarendonPress),216–253. tions to increasing levels of task difficulty. Ergonomics 41, 656–669. doi:
Oostenveld,R.,Fries,P.,Maris,E.,andSchoffelen,J.M.(2011).FieldTrip:open 10.1080/001401398186829
sourcesoftwareforadvancedanalysisofMEG,EEG,andinvasiveelectrophysi- Verwey,W.B.,andVeltman,H.A.(1996).DetectingShortPeriodsofElevated
ologicaldata.Comput.Intell.Neurosci.2011:156869.doi:10.1155/2011/156869 Workload:acomparisonofnineworkloadassesmenttechniques.J.Exp.Psychol.
Pfurtscheller,G.,Stancak,A.Jr.,andNeuper,C.(1996).Event-relatedsynchroniza- 2,270–285.
tion(ERS)inthealphaband:anelectrophysiologicalcorrelateofcorticalidling Vogt,J.,Hagemann,T.,andKastner,M.(2006).Theimpactofworkloadonheart
[review].Int.J.Psychophysiol.24,39–46.doi:10.1016/S0167-8760(96)00066-9 rateandbloodpressureinen-routeandtowerairtrafficcontrol.J.Psychophysiol.
Polich, J., and Kok, A. (1995). Cognitive and biological determinants of 20,297–314.doi:10.1027/0269-8803.20.4.297
P300: an integrative review. Biol. Psychol. 41, 103–146. doi: 10.1016/0301- Watter,S.,Geffen,G.M.,andGeffen,L.B.(2001).Then-backasadual-task:
0511(95)05130-9 P300morphologyunderdividedattention.Psychophysiology38,998–1003.doi:
Polich, J. (2007). Updating P300: an integrative theory of P3a and P3b. Clin. 10.1111/1469-8986.3860998
Neurophysiol.118,2128–2148.doi:10.1016/j.clinph.2007.04.019 Wientjes,C.J.E.(1992).Respirationinpsychophysiology:methodsandapplica-
Porter,G.,Troscianko,T.,andGilchrist,I.D.(2007).Effortduringvisualsearch tions.Biol.Psychol.34,179–204.doi:10.1016/0301-0511(92)90015-M
andcounting:insightsfrompupillometry.Q.J.Exp.Psychol.60,211–229.doi: Wilson,G.F.,andFisher,F.(1991).Theuseofcardiacandeyeblinkmeasuresto
10.1080/17470210600673818 determineflightsegmentinF4crews.Aviat.SpaceEnviron.Med.62,959–961.
Pratt,N.,Willoughby,A.,andSwick,D.(2011).Effectsofworkingmemoryloadon Wilson,G.F.,andRussell,C.A.(2003).Operatorfunctionalstateclassification
visualselectiveattention:behavioralandelectrophysiologicalevidence.Front. usingmultiplepsychophysiologicalfeaturesinanairtrafficcontroltask.Hum.
Hum.Neurosci.5:57.doi:10.3389/fnhum.2011.00057 Factors45,381–389.doi:10.1518/hfes.45.3.381.27252
Raabe,M.,Rutschmann,R.M.,Schrauf,M.,andGreenlee,M.W.(2005).“Neural Wilson, G. F., and Russell, C. A. (2007). Performance enhancement in a UAV
correlatesofsimulateddriving:auditoryoddballresponsesdependentonwork- taskusingpsychophysiologicaldeterminedadaptiveaiding.Hum.Factors49,
load,”inFoundationsofAugmentedCognition,edD.D.Schmorrow(Mahwah, 1005–1019.doi:10.1518/001872007X249875
NJ:LawrenceErlbaumAssociates,Inc.),1067–1076. Winton,W.M.,Putnam,L.E.,andKrauss,R.M.(1984).Facialandautonomic
Raghavachari, S., Kahana, M. J., Rizzuto, D. S., Caplan, J. B., Kirschen, M. P., manifestationsofthedimensionalstructureofemotion.J.Exp.Soc.Psychol.20,
Bourgeois,B.,etal.(2001).Gatingofhumanthetaoscillationsbyaworking 195–216.doi:10.1016/0022-1031(84)90047-7
memorytask.J.Neurosci.21,3175–3183. Zijlstra,F.R.H.(1993).EfficiencyinWorkBehaviour.ADesignApproachforModern
Ravden,D.,andPolich,J.(1999).OnP300measurementstability:habituation, Tools.Ph.D.thesis,DelftUniversityofTechnology,DelftUniversityPress,Delft.
intra-trialblockvariation,andultradianrhythms.Biol.Psychol.51,59–76.doi: Zimmerman,P.H.,Bolhuis,J.E.,Willemsen,A.,Meyer,E.S.,andNoldus,L.P.
10.1016/S0301-0511(99)00015-0 (2009).TheObserverXT:atoolfortheintegrationsandsynchronizationof
Reimer,B.,andMehler,B.(2011).Theimpactofcognitiveworkloadonphysio- multimodalsignals.Behav.Res.Methods41,731–735.doi:10.3758/BRM.41.
logicalarousalinyoungadultdrivers:afieldstudyandsimulationvalidation. 3.731
Ergonomics54,932–942.doi:10.1080/00140139.2011.604431
Rösler,F.,Heil,M.,andRöder,B.(1997).Slownegativebrainpotentialsasreflec- ConflictofInterestStatement:Theauthorsdeclarethattheresearchwascon-
tionsofspecificmodularresourcesofcognition.Biol.Psychol.45,109–141.doi: ductedintheabsenceofanycommercialorfinancialrelationshipsthatcouldbe
10.1016/S0301-0511(96)05225-8 construedasapotentialconflictofinterest.
Roth,W.T.(1983).“AcomparisonofP300andtheskinconductanceresponse,”in
TutorialsinERPResearch—EndogenousComponents,edsA.W.K.Gaillardand Received:29January2014;accepted:25September2014;publishedonline:14October
W.Ritter(Amsterdam:North-Holland),177–199. 2014.
Ruchkin, D. S., Johnson, R. Jr., Canoune, H., and Ritter, W. (1990). Short- Citation:HogervorstMA,BrouwerA-MandvanErpJBF(2014)Combiningand
term memory storage and retention: an event-related brain potential comparingEEG,peripheralphysiologyandeye-relatedmeasuresfortheassessment
study.Electroencephalogr.Clin.Neurophysiol.76,419–439.doi:10.1016/0013- ofmentalworkload.Front.Neurosci.8:322.doi:10.3389/fnins.2014.00322
4694(90)90096-3 ThisarticlewassubmittedtoNeuroprosthetics,asectionofthejournalFrontiersin
Severens,M.,Farquhar,J.,Duysens,J.,andDesain,P.(2013).Amulti-signature Neuroscience.
brain-computerinterface:useoftransientandsteady-stateresponses.J.Neural. Copyright © 2014 Hogervorst,BrouwerandvanErp.Thisisanopen-accessarticle
Eng.10:026005.doi:10.1088/1741-2560/10/2/026005 distributedunderthetermsoftheCreativeCommonsAttributionLicense(CCBY).
Srinivasan,N.(2007).Cognitiveneuroscienceofcreativity:EEGbasedapproaches. The use, distribution or reproduction in other forums is permitted, provided the
Methods42,109–116.doi:10.1016/j.ymeth.2006.12.008 originalauthor(s)orlicensorarecreditedandthattheoriginalpublicationinthis
TaskForceoftheEuropeanSocietyofCardiologytheNorthAmericanSociety journaliscited,inaccordancewithacceptedacademicpractice.Nouse,distributionor
of Pacing Electrophysiology. (1996). Heart rate variability: standards of reproductionispermittedwhichdoesnotcomplywiththeseterms.
FrontiersinNeuroscience|Neuroprosthetics October2014|Volume8|Article322|14