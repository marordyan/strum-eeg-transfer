DATAREPORT
published:13May2016
doi:10.3389/fnins.2016.00196
The Temple University Hospital EEG
Data Corpus
IyadObeid*andJosephPicone
ElectricalandComputerEngineering,TempleUniversity,Philadelphia,PA,USA
Keywords:EEG,database,machinelearning,clinicaltrialsastopic,bigdata
INTRODUCTION
Theelectroencephalogram(EEG)isanexcellenttoolforprobingneuralfunction,bothinclinical
and research environments, due to its low cost, non-invasive nature, and pervasiveness. In the
clinic,theEEGisthestandardtestfordiagnosingandcharacterizingepilepsyandstroke,aswell
asahostofothertraumaandpathologyrelatedconditions(Tatumetal.,2007;YamadaandMeng,
2009).Inresearchlaboratories,EEGisusedtostudyneuralresponsestoexternalstimuli,motor
planningandexecution,andbrain-computerinterfaces(LebedevandNicolelis,2006;Wangetal.,
2013).WhilehumaninterpretationisstillthegoldstandardforEEGanalysisintheclinic,ahostof
softwaretoolsexisttofacilitatetheprocessortomakepredictiveanalysessuchasseizureprediction.
Recently,aconfluenceofeventshasunderscoredtheneedforrobustEEGtools.First,therehas
been a renewed push via the White House BRAIN initiative to understand neural function and
Editedby:
disease (Weiss, 2013). Secondly, there is an increased awareness on brain injury owing to both
MikhailLebedev,
DukeUniversity,USA theinfluxofinjuredwarfightersandnumeroushigh-profileathletesfoundtohavechronicbrain
damage(McKeeetal.,2009;Sternetal.,2011).Andthirdly,awaveofconsumergradescalpsensors
Reviewedby:
hasenteredthemarket,allowingenduserstomonitorsleep,arousal,andmood(Liaoetal.,2012).
DuyguKuzum,
UniversityofCalifornia,SanDiego, Inalltheseapplications,thereisaneedforrobustsignalprocessingtoolstoanalyzetheEEG
USA data. Historically, EEG signal processing tools have been devised using either ad hoc heuristic
ErvinSejdic, methods, or by training pattern recognition engines on small data sets (Gotman, 1982). These
UniversityofPittsburgh,USA methods have yielded limited results, owing mostly to the fact that brain signals (and EEG
IvanSelesnick,
in particular) are characterized by great variability, which can only be properly interpreted by
NewYorkUniversity,USA
buildingstatisticalmodelsusingmassiveamountsofdata(Alotaibyetal.,2014;Ramgopaletal.,
XiaomuSong,
2014). Unfortunately, despite EEG being perhaps the most pervasive modality for acquiring
WidenerUniversity,USA
ZhanpengJin, brain signals, there is a severe lack of data in the public domain. For example, the “EEG
BinghamtonUniversity,USA MotorMovement/ImageryDataset”(http://www.physionet.org/pn4/eegmmidb/)contains∼1500
*Correspondence: recordingsof1or2mindurationapiecefrom109subjects(Goldbergeretal.,2000;Schalketal.,
IyadObeid 2004). The CHB-MIT database contains data from 22 subjects, mostly pediatric (Shoeb, 2009).
iobeid@temple.edu A database from Karunya University contains 175 16-channel EEGs of duration 10s (Selvaraj
etal.,2014).OneofthemostextensivedatabasesforsupportingepilepsyresearchistheEuropean
Specialtysection: Epilepsy Database (http://epilepsy-database.eu/), which contains 250 datasets from 30 unique
Thisarticlewassubmittedto patients,butsellsfore3000.Otherdatabases,suchasieee.org,containawealthofdatafrommore
NeuralTechnology,
invasivemodalitiessuchaselectrocorticogram,butlittleornoEEG.
asectionofthejournal
ThislackofpublicallyavailabledataisironicconsideringthathundredsofthousandsofEEGs
FrontiersinNeuroscience
are administered annually in clinical settings around the world. Relatively little of this data is
Received:29February2016
publiclyavailabletotheresearchcommunityinaformthatisusefultomachinelearningresearch.
Accepted:20April2016
MassiveamountsofEEGdatawouldallowtheuseofstate-of-the-artmachinelearningalgorithms
Published:13May2016
to discover new diagnostics and validate clinical practice. Furthermore, it is desirable that such
Citation:
databecollectedinclinicalsettings,asopposedtotightlycontrolledresearchenvironments,since
ObeidIandPiconeJ(2016)The
“clinical-grade” data is inherently more variable with respect to parameters such as electrode
TempleUniversityHospitalEEGData
Corpus.Front.Neurosci.10:196. location, clinical environment, equipment, and noise. Capturing this variability is critical to the
doi:10.3389/fnins.2016.00196 developmentofrobust,highperformancetechnologythathasreal-worldimpact.
FrontiersinNeuroscience|www.frontiersin.org 1 May2016|Volume10|Article196

| ObeidandPicone |     |     |     |     |     | TempleUniversityHospitalEEGCorpus |     |     |
| -------------- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- |
In this work, we describe a new corpus, the TUH-EEG theneurologistafteranalyzingtheEEGscanandaretheofficial
Corpus, which is an ongoing data collection effort that has hospital summary of the clinical impression. These reports
recentlyreleased14yearsofclinicalEEGdatacollectedatTemple are comprised of unstructured text that describes the patient,
University Hospital. The records have been curated, organized, relevant history, medications, and clinical impression. Reports
andpairedwithtextualclinicianreportsthatdescribethepatients wereminedfromthehospital’scentralelectronicmedicalrecords
and scans. The corpus is publicly available from the Neural archivesandtypicallyconsistedofimagescansofprintedreports.
EngineeringDataConsortium(www.nedcdata.org)(Piconeand Various levels of image processing were employed to improve
Obeid,2016). the image quality before applying optical character recognition
|     |     |     |     | (OCR) to | convert the | images into | text. A combination | of  |
| --- | --- | --- | --- | -------- | ----------- | ----------- | ------------------- | --- |
METHODS softwareandmanualeditingwasusedtoscrubprotectedhealth
|     |     |     |     | information | (PHI) from | the reports | and to correct | errors |
| --- | --- | --- | --- | ----------- | ---------- | ----------- | -------------- | ------ |
Clinical EEG data were collected from archival records at in OCR transcription. Only sessions with both an EEG and
TempleUniversityHospital(TUH).Allworkwasperformedin a corresponding clinician report were included in the final
| accordance | with the Declaration | of Helsinki | and with the full | corpus. |     |     |     |     |
| ---------- | -------------------- | ----------- | ----------------- | ------- | --- | --- | --- | --- |
approvaloftheTempleUniversityIRB.Allpersonnelincontact ThecorpuswasdefinedwithahierarchicalUnix-stylefiletree
withprivilegedpatientinformationwerefullytrainedonpatient structure. The top folder, edf, contains 109 numbered folders,
privacyandwerecertifiedbytheTempleIRB. eachofwhichcontainnumberedfoldersforupto100patients.
Eachofthesepatientfolderscontainssub-foldersthatcorrespond
| Archival | EEG signal data | were recovered | from CD-ROMs. |     |     |     |     |     |
| -------- | --------------- | -------------- | ------------- | --- | --- | --- | --- | --- |
Files were converted from their native proprietary file format toindividualrecordingsessions.Thosefoldernamesreflectthe
(Nicolet’s NicVue) to an open format EDF standard. Data was session number and date of recording. Finally, each session
thenrigorously de-identifiedto conform totheHIPAAPrivacy folder includes one or more EEG (.edf) data files as well
Rule by eliminating 18 potential identifiers including patient as the clinician report in .txt format. Figure1 summarizes
namesanddatesofbirth.Patientmedicalrecordnumberswere the corpus file structure and gives examples of text and
| replacedwithrandomizeddatabaseidentifiers,withakeytothat |                         |                    |                  | signaldata. |     |     |     |     |
| -------------------------------------------------------- | ----------------------- | ------------------ | ---------------- | ----------- | --- | --- | --- | --- |
| mapping                                                  | being saved to a secure | off-line location. | Importantly,     |             |     |     |     |     |
| our process                                              | captured instances      | in which           | the same patient | RESULTS     |     |     |     |     |
| received                                                 | multiple EEGs over      | time and assigned  | database IDs     |             |     |     |     |     |
accordingly.Datade-identificationwasperformedbycombining The completed corpus comprises 16,986 sessions from 10,874
automatedcustom-designedsoftwaretoolswithmanualediting uniquesubjects.EachofthesesessionscontainsatleastoneEDF
and proofreading. All storage and manipulation of source files file(moreinthecaseoflongtermmonitoringsessionsthatwere
wasconductedondedicatednon-networkconnectedcomputers broken into multiple files) and one physician report. Corpus
that were physically located within the TUH Department of metrics are summarized in Figure2. Subjects were 51% female
Neurology. and ranged in age from less than 1 year to over 90 (average
We also manually paired each retrieved EEG with its 51.6,stdev55.9;seeFigure2bottomleft).Theaveragenumberof
corresponding clinician report. These reports are generated by sessionsperpatientwas1.56,althoughasmanyas37EEGswere
FIGURE1|DirectoryandfilestructureoftheTUH-EEGdatabase.Dataisorganizedbypatient(orange)andthenbysession(yellow).Eachsessioncontains
oneormoresignal(edf)andphysicianreport(txt)files.Toaccommodatefilesystemmanagementissues,patientsaregroupedintosetsofabout100(blue).
FrontiersinNeuroscience|www.frontiersin.org 2 May2016|Volume10|Article196

ObeidandPicone TempleUniversityHospitalEEGCorpus
FIGURE2|MetricsdescribingtheTUH-EEGcorpus.[Topleft]histogramshowingnumberofsessionsperpatient;[topright]histogramshowingnumberof
sessionsrecordedpercalendaryear;[bottomleft]histogramofpatientages;[bottomright]histogramshowingnumberofEEG-onlychannels(purple);andtotal
channels(green).
recorded for asingle patientover an8-month period (Figure2 drive to the authors in order to avoid the downloading
topleft).Thenumberofsessionsperyearvariesfrom∼1000to process.
2500(withtheexceptionofyears2000–2002,and2005,inwhich
limitednumbersofcompletereportswerefoundinthevarious DISCUSSION
electronicmedicalrecordarchives;seeFigure2topright).
Therewasasubstantialdegreeofvariabilitywithrespecttothe Thisworkpresentstheworld’slargestpublicallyavailablecorpus
numberofchannelsincludedinthecorpus(seeFigure2bottom of clinical EEG data, representing a grand total of 29.1 years
right).EDFfilestypicallycontainedbothEEG-specificchannels (totaldurationsummedoverallEEGchannels)ofEEGdata.In
aswellassupplementarychannelssuchasdetectedbursts,EKG, additiontoitssize,thiscorpusfeaturesawidevariationofpatient
EMG, and photic stimuli. The most common number of EEG- ages,diagnoses,medications,channelcounts,andsamplingrates.
onlychannelsperEDFfilewas31,althoughtherewerecaseswith Furthermore, the corpus continues to be expanded at a rate
asfewas20.AmajorityoftheEEGdatawassampledat250Hz of∼2500newsessionsperyear.
(87%)withtheremainingdatabeingsampledat256Hz(8.3%), Biomedicine is entering a new age of data-driven discovery
400Hz(3.8%),and512Hz(1%). drivenbyubiquitouscomputingpower,inexpensivedatastorage,
An initial analysis of the physician reports reveals a wide the machine learning revolution, and high speed internet
rangeofmedicationsandmedicalconditions.Unsurprisingly,the connections. Access to massive quantities of properly curated
mostcommonlistedmedicationswereanti-convulsantssuchas dataisnowthecriticalbottlenecktoadvancementinmanyareas
KeppraandDilantin,aswellasbloodthinnerssuchasLovenox ofbiomedicalresearch.Ironically,doctorsandcliniciansgenerate
andheparin.Approximately87%ofthereportsincludedthetext enormous quantities of data every day, but that information is
string“epilep,”andabout12%included“stroke.”Only48 almostexclusivelysequesteredinsecurearchiveswhereitcannot
totalreportsincludedthestring“concus.” be used for research by the biomedical research community.
The TUH-EEG corpus v0.6.0 has been released and is The quantity, quality, and variability of such data represent
freelyavailableonlineatwww.nedcdata.org.Usersmustregister a significant unrealized potential, which is doubly unfortunate
with a valid email address. The uncompressed EDF files considering that the cost of generating that data has already
and reports together comprise 572GB. For convenience, the been borne. Although, there has been some advancement with
website stores all data from each patient as individual gzip respect to publishing databases of patient metadata, curated
files with a median filesize of 4.1 MB; all 10,874 gzips signaldatabasesaremuchlesscommonlyavailable,especiallyin
together comprise 330GB. Users wanting to access the entire quantities that would be sufficient to train most contemporary
database are encouraged to physically mail a USB hard machinelearningengines.
FrontiersinNeuroscience|www.frontiersin.org 3 May2016|Volume10|Article196

| ObeidandPicone |     |     |     |     |     |     |     | TempleUniversityHospitalEEGCorpus |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- |
In this work, we have endeavored to achieve two goals. The by a human domain expert, or automatically with a bootstrap-
first is to create a corpus of clinical EEG signals and their stylealgorithm.InadditiontotheEEGdataitself,wearereleasing
correspondingphysicianreports.Thesecondistoestablishbest acollectionofannotationswhichmaybedownloadedseparately
practicesforthecurationandpublicationofclinicalsignaldata, iftheyareofinteresttotheuser.Theannotationscontainthestart
which is an inherently different entity than discrete metadata. andstoptimeandaneventlabelandarespecifictoeachchannel.
The EEG corpus we present here is the first of its kind, Six classes of events are included: (1) spike and/or sharp waves
both in terms of volume and heterogeneity, both of which are (SPSW),(2)periodiclateralizedepileptiformdischarges(PLED),
criticalfactorsfortrainingmachinelearningengines.Typically, and (3) generalized periodic epileptiform discharges (GPED).
“research-grade” data is created by tightly controlling as many SPSW events are epileptiform transients that are typically
external factors as possible. In contrast, “clinical-grade” data is observedinpatientswithepilepsy.PLEDeventsareindicativeof
| inherently | heterogeneous | with respect | to  | those same | external |     |     |     |     |     |     |
| ---------- | ------------- | ------------ | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- |
EEGabnormalitiesandoftenmanifestthemselveswithrepetitive
factors. Whereas certain classes of research questions can only spikeorsharpwavedischargesthatcanbefocalorlateralizedover
be answered using well-controlled data, others benefit from one hemisphere. These signals display quasi-periodic behavior.
| variability. | For example, | an epilepsy | detection | algorithm | that |     |     |     |     |     |     |
| ------------ | ------------ | ----------- | --------- | --------- | ---- | --- | --- | --- | --- | --- | --- |
GPEDeventsaresimilartoPLEDs,andmanifestthemselvesas
is trained using 31 specific EEG channels may not be effective periodicshort-intervaldiffusedischarges,periodiclong-interval
if one or more of those channels are not connected, or if diffuse discharges and suppression-burst patterns according to
the electrodes are improperly located or affixed to the scalp. the interval between the discharges. Triphasic waves, which
| Algorithms | that must | be sufficiently | robust | to function | under |     |     |     |     |     |     |
| ---------- | --------- | --------------- | ------ | ----------- | ----- | --- | --- | --- | --- | --- | --- |
manifestthemselvesasdiffuseandbilaterallysynchronousspikes
a plurality of conditions must be trained with data that is withbifrontalpredominance,typicallyatarateof1–2Hz,arealso
| sufficientlyheterogeneous. |           |                |          |        |         | includedinthisclass. |     |     |     |     |     |
| -------------------------- | --------- | -------------- | -------- | ------ | ------- | -------------------- | --- | --- | --- | --- | --- |
| Our work                   | has shown | that, although | clinical | signal | data is |                      |     |     |     |     |     |
Threeeventsareusedtomodelbackgroundnoise:(1)artifacts
ubiquitous and inherently valuable to the research community, (ARTF) are recorded electrical activity that is not of cerebral
it requires substantial manipulation before it can be released origin,suchasthoseduetotheequipment,patientbehavioror
as an adequately curated data corpus. This effort is non-trivial, theenvironment;(2)eyemovement(EYEM)arecommonevents
both in terms of time and cost. Our team’s activities ranged thatcanoftenbeconfusedwithaspike;(3)background(BCKG)
fromthemundane(e.g.,manuallycopyingarchivalhospitaldata isusedforallothersignals.
from over 1500 CD-ROMs) to more technical challenges (e.g., Thesesixclasses(threesignalclassesandthreenoiseclasses)
developingsoftwarefordetectingdataentryerrorsintheclinical
|     |     |     |     |     |     | were arrived | at through | several iterations | of  | a study | conducted |
| --- | --- | --- | --- | --- | --- | ------------ | ---------- | ------------------ | --- | ------- | --------- |
records).Physicianreportshadtobelocatedthroughoneoffive with Temple University Hospital neurologists. Automatic
different EMR portals, often manually. A battery of tests was labeling of these events allows a neurologist to rapidly search
createdtovalidatethateachrecordwascomplete,unique,error- long-term EEG recordings for anomalous behavior. However,
free, and completely free of privileged patient information. A therearemanymoreannotationsthatneedtobedevelopedfor
rigorousaccountingsystemwascreatedtotrackandorganizethe this data. For example, we are currently developing technology
tensofthousandsoffilesandtheirstatus. toautomaticallyannotateseizures.Therearemanyotherevents
ThecosttodeveloptheTUHEEGCorpushasbeenrelatively
|     |     |     |     |     |     | of interest | that need annotation | (e.g., | sleep | states). | We expect |
| --- | --- | --- | --- | --- | --- | ----------- | -------------------- | ------ | ----- | -------- | --------- |
low,totalinglessthan$100Kindirectcharges.Asmedicalrecord to be continually enhancing the value of the TUH EEG
| technology | improves, | the cost of | thiscollection | can | be reduced | Corpus. |     |     |     |     |     |
| ---------- | --------- | ----------- | -------------- | --- | ---------- | ------- | --- | --- | --- | --- | --- |
evenfurther.Onthebalance,thesetypesoflarge-scalecollections
areaworthwhileinvestment,sincecostsareminorrelativetothe AUTHOR CONTRIBUTIONS
| cost of acquiring | the | data or conducting | research |     | on the data. |     |     |     |     |     |     |
| ----------------- | --- | ------------------ | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
Ingeneral,theauthorsexpectthatadedicatedcommunity-wide JPledthedatabasecreationeffortandco-wrotethemanuscript.
datafacilitywouldbebestsuitedtocuratedataofthemagnitude IO contributed to the database creation effort, performed data
andcomplexitydescribedherebecausetherearesignificanton- metrics,andco-wrotethemanuscript.
goingcostsassociatedwithsuchanactivity.
| Anexampleoftheseon-goingcostsisannotationofthedata— |             |          |           |     |            | FUNDING |     |     |     |     |     |
| --------------------------------------------------- | ----------- | -------- | --------- | --- | ---------- | ------- | --- | --- | --- | --- | --- |
| a critical issue                                    | for machine | learning | research. | In  | most semi- |         |     |     |     |     |     |
supervisedmachinelearningapplications,oneofthefirststepsis This work has been supported by DARPA award D13AP00065,
toannotatethedata,aprocessinwhichimportantelementsofthe NSF awards 1305190 and 1458411, and by the Research Office
signalaremarkedassuch.Thiscanbeperformedeithermanually andDeanofEngineeringatTempleUniversity.
REFERENCES
|     |     |     |     |     |     | Goldberger, | A. L., Amaral, | L. A., Glass,  | L., Hausdorff, | J.             | M., Ivanov, |
| --- | --- | --- | --- | --- | --- | ----------- | -------------- | -------------- | -------------- | -------------- | ----------- |
|     |     |     |     |     |     | P. C.,      | Mark, R. G.,   | et al. (2000). | Physiobank,    | physiotoolkit, | and         |
Alotaiby,T.N.,Alshebeili,S.A.,Alshawi,T.,Ahmad,I.,andAbdEl-Samie,F.E. physionet components of a new research resource for complex
(2014).EEGseizuredetectionandpredictionalgorithms:asurvey.EURASIPJ. physiologic signals. Circulation 101, e215–e220. doi: 10.1161/01.CIR.101.
| Adv.SignalProcess.2014:183.doi:10.1186/1687-6180-2014-183 |     |     |     |     |     | 23.e215 |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
FrontiersinNeuroscience|www.frontiersin.org 4 May2016|Volume10|Article196

ObeidandPicone TempleUniversityHospitalEEGCorpus
Gotman, J. (1982). Automatic recognition of epileptic seizures in the EEG. Shoeb, A. (2009). Application of Machine Learning to Epileptic Seizure Onset
Electroencephalogr. Clin. Neurophysiol. 54, 530–540. doi: 10.1016/0013- DetectionandTreatment.Cambridge,MA:MIT.
4694(82)90038-4 Stern,R.A.,Riley,D.O.,Daneshvar,D.H.,Nowinski,C.J.,Cantu,R.C.,and
Lebedev,M.,andNicolelis,M.(2006).Brain–machineinterfaces:past,presentand McKee, A. C. (2011). Long-term consequences of repetitive brain trauma:
future.TrendsNeurosci.29,536–546.doi:10.1016/j.tins.2006.07.004 chronic traumatic encephalopathy. PM R (10 Suppl. 2), S460–S467. doi:
Liao, L. D., Lin, C. T., McDowell, K., Wickenden, A. E., Gramann, K., 10.1016/j.pmrj.2011.08.008
Jung, T. P., et al. (2012). Biosensor technologies for augmented brain – Tatum,W.,Husain,A.,Benbadis,S.,andKaplan,P.(2007).HandbookofEEG
computerinterfacesinthenextdecades.Proceed.IEEE100,1553–1566.doi: Interpretation.NewYork,NY:DemosMedicalPublishing.
10.1109/JPROC.2012.2184829 Wang, W., Collinger, J. L., Degenhart, A. D., Tyler-Kabara, E. C., Schwartz,
McKee, A. C., Cantu, R. C., Nowinski, C. J., Hedley-Whyte, E. T., Gavett, A. B., Moran, D. W., et al. (2013). An electrocorticographic brain
B. E., Budson, A. E., et al. (2009). Chronic traumatic encephalopathy interface in an individual with tetraplegia. PLoS ONE 8:e55344. doi:
in athletes: progressive tauopathy after repetitive head injury. J. 10.1371/journal.pone.0055344
Neuropathol. Exp. Neurol. 68, 709–35. doi: 10.1097/NEN.0b013e3181 Weiss,P.S.(2013).PresidentobamaannouncestheBRAINinitiative.ACSNano
a9d503 7,2873–2874.doi:10.1021/nn401796f
Picone,J.,andObeid,I.(2016).TempleUniversityHospitalEEGCorpus,Neural Yamada,T.,andMeng,E.(2009).PracticalGuideforClinicalNeurophysiologic
EngineeringDataConsortium,v0.6.3.Availableonlineat:www.nedcdata.org Testing:EEG.Philadelphia,PA:LippincottWilliams&Wilkins.
Ramgopal,S.,Thome-Souza,S.,Jackson,M.,Kadish,N.E.,SánchezFernández,
I., Klehm, J., et al. (2014). Seizure detection, seizure prediction, and Conflict of Interest Statement: The authors declare that the research was
closed-loop warning systemsin Epilepsy. Epilepsy Behav. 37, 291–307. doi: conductedintheabsenceofanycommercialorfinancialrelationshipsthatcould
10.1016/j.yebeh.2014.06.023 beconstruedasapotentialconflictofinterest.
Schalk, G., McFarland, D. J., Hinterberger, T., Birbaumer, N., and Wolpaw,
J. R. (2004). BCI2000: a general-purpose Brain-Computer Interface (BCI) Copyright © 2016 Obeid and Picone. This is an open-access article distributed
system.IEEETrans.BioMed.Eng.51,1034–1043.doi:10.1109/TBME.2004. underthetermsoftheCreativeCommonsAttributionLicense(CCBY).Theuse,
827072 distribution or reproduction in other forums is permitted, provided the original
Selvaraj,T.G.,Ramasamy,B.,Jeyaraj,S.J.,andSuviseshamuthu,E.S.(2014).EEG author(s)orlicensorarecreditedandthattheoriginalpublicationinthisjournal
databaseofseizuredisordersforexpertsandapplicationdevelopers.Clin.EEG is cited, in accordance with accepted academic practice. No use, distribution or
Neurosci.45,304–309.doi:10.1177/1550059413500960 reproductionispermittedwhichdoesnotcomplywiththeseterms.
FrontiersinNeuroscience|www.frontiersin.org 5 May2016|Volume10|Article196