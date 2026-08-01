Archive ouverte UNIGE
https://archive-ouverte.unige.ch
Article scientifique Article 2012 Accepted version Public access
This is an author manuscript post-peer-reviewing (accepted version) of the original publication. The layout of
the published version may differ .
DEAP : a Database for Emotion Analysis Using Physiological Signals
Koelstra, Sander; Mühl, Christian; Soleymani, Mohammad; Lee, Jong-Seok; Yazdani, Ashkan; Ebrahimi, Touradj;
Pun, Thierry; Nijholt, Anton; Patras, Ioannis
How to cite
KOELSTRA, Sander et al. DEAP : a Database for Emotion Analysis Using Physiological Signals. In: IEEE
transactions on affective computing, 2012, vol. 3, n° 1, p. 18–31. doi: 10.1109/T-AFFC.2011.15
This publication URL: https://archive-ouverte.unige.ch/unige:47405
Publication DOI: 10.1109/T-AFFC.2011.15
© This document is protected by copyright. Please refer to copyright holder(s) for terms of use.
Last update in Archive ouverte UNIGE on 14.03.2023 23:56

| IEEETRANS.AFFECTIVECOMPUTING |     |     |          |               |     |     |     |         |     |          |     |     |     |       | 1   |
| ---------------------------- | --- | --- | -------- | ------------- | --- | --- | --- | ------- | --- | -------- | --- | --- | --- | ----- | --- |
| DEAP:                        |     | A   | Database |               |     |     | for | Emotion |     | Analysis |     |     |     | using |     |
|                              |     |     |          | Physiological |     |     |     | Signals |     |          |     |     |     |       |     |
SanderKoelstra, StudentMember, IEEE, Christian Mu¨hl, MohammadSoleymani, StudentMember, IEEE,
Jong-SeokLee,Member, IEEE, AshkanYazdani,TouradjEbrahimi, Member, IEEE,
Thierry Pun, Member, IEEE,Anton Nijholt, Member, IEEE, Ioannis Patras, Member, IEEE
Abstract—We present a multimodal dataset for the analysis of human affective states. The electroencephalogram (EEG) and
peripheral physiological signals of 32 participants were recorded as each watched 40 one-minute long excerpts of music videos.
Participants rated each video in terms of the levels of arousal, valence, like/dislike, dominance and familiarity. For 22 of the 32
participants, frontal face videowasalso recorded.Anovel method for stimuli selection isproposed usingretrieval byaffective tags
from thelast.fm website,video highlightdetection andanonlineassessment tool.Anextensive analysisofthe participants’ratings
during the experiment is presented. Correlates between the EEG signal frequencies and the participants’ ratings are investigated.
Methodsandresultsarepresentedforsingle-trialclassificationofarousal,valenceandlike/dislikeratingsusingthemodalitiesofEEG,
peripheralphysiologicalsignalsandmultimediacontentanalysis.Finally,decisionfusionoftheclassificationresultsfromthedifferent
modalitiesisperformed. The dataset ismade publiclyavailableandwe encourage otherresearchers to use itfortesting theirown
affectivestateestimationmethods.
IndexTerms—Emotionclassification,EEG,Physiologicalsignals,Signalprocessing,Patternclassification,Affectivecomputing.
F
1 INTRODUCTION
|              |           |                           |             |              |            |           |         | information    |               | retrieval. | Affective    | characteristics |             |                | of multi-  |
| ------------ | --------- | ------------------------- | ----------- | ------------ | ---------- | --------- | ------- | -------------- | ------------- | ---------- | ------------ | --------------- | ----------- | -------------- | ---------- |
|              |           |                           |             |              |            |           |         | media          | are important |            | features     | for             | describing  |                | multime-   |
| EMOTION      |           | is a psycho-physiological |             |              | process    | triggered |         |                |               |            |              |                 |             |                |            |
|              |           |                           |             |              |            |           |         | dia content    |               | and can    | be presented |                 | by          | such emotional |            |
| by           | conscious | and/or                    | unconscious |              | perception |           | of an   |                |               |            |              |                 |             |                |            |
|              |           |                           |             |              |            |           |         | tags. Implicit |               | affective  | tagging      | refers          | to          | the            | effortless |
| object or    | situation | and                       | is often    | associated   |            | with      | mood,   |                |               |            |              |                 |             |                |            |
|              |           |                           |             |              |            |           |         | generation     | of            | subjective | and/or       | emotional       |             | tags.          | Implicit   |
| temperament, |           | personality               | and         | disposition, |            | and       | motiva- |                |               |            |              |                 |             |                |            |
|              |           |                           |             |              |            |           |         | tagging        | of videos     | using      | affective    |                 | information |                | can help   |
tion.Emotionsplayanimportantroleinhumancommu-
|          |     |                  |     |        |          |     |         | recommendation |     | and | retrieval | systems | to  | improve | their |
| -------- | --- | ---------------- | --- | ------ | -------- | --- | ------- | -------------- | --- | --- | --------- | ------- | --- | ------- | ----- |
| nication | and | can be expressed |     | either | verbally |     | through |                |     |     |           |         |     |         |       |
performance[1]–[3].Thecurrentdatasetisrecordedwith
| emotional     | vocabulary, |                  | or by         | expressing     | non-verbal      |     | cues   |            |                         |          |          |           |                |           |           |
| ------------- | ----------- | ---------------- | ------------- | -------------- | --------------- | --- | ------ | ---------- | ----------------------- | -------- | -------- | --------- | -------------- | --------- | --------- |
|               |             |                  |               |                |                 |     |        | the goalof | creatinganadaptivemusic |          |          |           | videorecommen- |           |           |
| such as       | intonation  | of               | voice,        | facial         | expressions     | and | ges-   |            |                         |          |          |           |                |           |           |
|               |             |                  |               |                |                 |     |        | dation     | system.                 | In our   | proposed | music     | video          | recommen- |           |
| tures. Mostof |             | the contemporary |               | human-computer |                 |     | inter- |            |                         |          |          |           |                |           |           |
|               |             |                  |               |                |                 |     |        | dation     | system,                 | a user’s | bodily   | responses |                | will      | be trans- |
| action        | (HCI)       | systems          | are deficient |                | in interpreting |     | this   |            |                         |          |          |           |                |           |           |
latedtoemotions.Theemotionsofauserwhilewatching
informationandsufferfromthelackofemotionalintelli-
|     |     |     |     |     |     |     |     | music video |     | clips will | help | the recommender |     |     | system to |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---------- | ---- | --------------- | --- | --- | --------- |
gence.Inotherwords,theyareunabletoidentifyhuman
|                |                |              |                |             |             |              |     | first understand |              | user’s     | taste   | and           | then to      | recommend      | a       |
| -------------- | -------------- | ------------ | -------------- | ----------- | ----------- | ------------ | --- | ---------------- | ------------ | ---------- | ------- | ------------- | ------------ | -------------- | ------- |
| emotional      | states         | and          | use this       | information |             | in deciding  |     |                  |              |            |         |               |              |                |         |
|                |                |              |                |             |             |              |     | music clip       | which        | matches    |         | users current |              | emotion.       |         |
| upon proper    |                | actions      | to execute.    | The         | goal        | of affective |     |                  |              |            |         |               |              |                |         |
|                |                |              |                |             |             |              |     | The              | presented    | database   |         | explores      | the          | possibility    | to      |
| computing      | is             | to fill this | gap            | by          | detecting   | emotional    |     |                  |              |            |         |               |              |                |         |
|                |                |              |                |             |             |              |     | classify         | emotion      | dimensions |         | induced       | by           | showing        | music   |
| cues occurring |                | during       | human-computer |             | interaction |              | and |                  |              |            |         |               |              |                |         |
|                |                |              |                |             |             |              |     | videos           | to different | users.     | To      | the best      | of           | our knowledge, |         |
| synthesizing   |                | emotional    | responses.     |             |             |              |     |                  |              |            |         |               |              |                |         |
|                |                |              |                |             |             |              |     | the responses    |              | to this    | stimuli | (music        | video        | clips)         | have    |
| Characterizing |                | multimedia   |                | content     | with        | relevant,    | re- |                  |              |            |         |               |              |                |         |
|                |                |              |                |             |             |              |     | never            | been         | explored   | before, | and           | the research |                | in this |
| liable and     | discriminating |              | tags           | is          | vital for   | multimedia   |     |                  |              |            |         |               |              |                |         |
fieldwasmainlyfocusedonimages,musicornon-music
|     |     |     |     |     |     |     |     | video | segments | [4], | [5]. | In an adaptive |     | music | video |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------- | ---- | ---- | -------------- | --- | ----- | ----- |
•
The firstthree authors contributed equally to this work and are listed in recommender, an emotion recognizer trained by phys-
| alphabetical | order. |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• Sander Koelstra and Ioannis Patras are with the School of Computer iological responses to the content from similar nature,
Science and Electronic Engineering, Queen Mary University of London music videos, is better able to fulfill its goal.
(QMUL).E-mail:sander.koelstra@eecs.qmul.ac.uk
| •   |     |     |     |     |     |     |     | Variousdiscretecategorizationsofemotionshavebeen |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
ChristianMu¨hlandAntonNijholtarewiththeHumanMediaInteraction
|     |     |     |     |     |     |     |     | proposed, | such | as the | six | basic emotions |     | proposed | by  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---- | ------ | --- | -------------- | --- | -------- | --- |
Group,UniversityofTwente(UT).
• Mohammad Soleymani and Thierry Pun are with the Computer Vision EkmanandFriesen[6]andthetreestructureofemotions
andMultimediaLaboratory,UniversityofGeneva(UniGe´).
| •   |     |     |     |     |     |     |     | proposed | by  | Parrot | [7]. Dimensional |     | scales | of  | emotion |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------ | ---------------- | --- | ------ | --- | ------- |
AshkanYazdani,Jong-SeokLeeandTouradjEbrahimiarewiththeMulti-
|     |     |     |     |     |     |     |     | have also | been | proposed, |     | such | as Plutchik’s |     | emotion |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---- | --------- | --- | ---- | ------------- | --- | ------- |
mediaSignalProcessingGroup,EcolePolytechniqueFe´de´raledeLausanne
(EPFL).
|     |     |     |     |     |     |     |     | wheel   | [8] and | the valence-arousal |           |     | scale           | by Russell | [9].   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------------------- | --------- | --- | --------------- | ---------- | ------ |
|     |     |     |     |     |     |     |     | In this | work,   | we use              | Russell’s |     | valence-arousal |            | scale, |

| IEEETRANS.AFFECTIVECOMPUTING |     |     |     |     |     |     |     |     |     |     |     |     |     | 2   |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
widely used in research on affect, to quantitatively extensive review of affective audiovisual databases can
describe emotions. In this scale, each emotional state be found in [13], [19]. The MAHNOB HCI database [4]
can be placed on a two-dimensional plane with arousal consists of two experiments. The responses including,
and valence as the horizontal and vertical axes. While EEG, physiological signals, eye gaze, audio and facial
arousal and valence explain most of the variation in expressions of 30 people were recorded. The first exper-
emotional states, a third dimension of dominance can iment was watching 20 emotional video extracted from
alsobeincludedinthemodel[9].Arousalcanrangefrom movies and online repositories. The second experiment
inactive (e.g. uninterested, bored) to active (e.g. alert, was tag agreement experiment in which images and
excited), whereas valence ranges from unpleasant (e.g. shortvideoswithhumanactionswereshownthepartic-
sad,stressed)topleasant(e.g.happy,elated).Dominance ipants first without a tag and then with a displayed tag.
ranges from a helpless and weak feeling (without con- Thetagswereeithercorrectorincorrectandparticipants’
trol) to anempowered feeling (in control of everything). agreement with the displayed tag was assessed.
For self-assessment along these scales, we use the well- There has been a large number of published works
known self-assessment manikins (SAM) [10]. in the domain of emotion recognition from physiologi-
Emotion assessmentis oftencarriedout throughanal- cal signals [16], [20]–[24]. Of these studies, only a few
|         |                  |             |     |        |            |     | achieved | notable | results | using | video | stimuli. | Lisetti | and |
| ------- | ---------------- | ----------- | --- | ------ | ---------- | --- | -------- | ------- | ------- | ----- | ----- | -------- | ------- | --- |
| ysis of | users’ emotional | expressions |     | and/or | physiolog- |     |          |         |         |       |       |          |         |     |
ical signals. Emotional expressions refer to any observ- Nasoz used physiological responses to recognize emo-
able verbal and non-verbal behavior that communicates tionsinresponsetomovie scenes[23].Themoviescenes
emotion. So far, most of the studies on emotion as- were selected to elicit six emotions, namely sadness,
sessment have focused on the analysis of facial expres- amusement, fear, anger, frustration and surprise. They
|           |        |              |     |            |     |           | achieved | a high | recognition |     | rate of | 84% | for the | recog- |
| --------- | ------ | ------------ | --- | ---------- | --- | --------- | -------- | ------ | ----------- | --- | ------- | --- | ------- | ------ |
| sions and | speech | to determine |     | a person’s |     | emotional |          |        |             |     |         |     |         |        |
state. Physiological signals are also known to include nition of these six emotions. However, the classification
emotional information that can be used for emotion was based on the analysis of the signals in response to
assessment but they have received less attention. They pre-selected segments in the shown video known to be
comprisethesignalsoriginatingfromthecentralnervous related to highly emotional events.
system (CNS)and the peripheralnervous system (PNS). Some efforts have been made towards implicit affec-
Recent advances in emotion recognition have mo- tive tagging of multimedia content. Kierkels et al. [25]
tivated the creation of novel databases containing proposed a method for personalized affective tagging
emotional expressions in different modalities. These of multimedia using peripheral physiological signals.
databases mostly cover speech, visual, or audiovisual Valence and arousal levels of participants’ emotions
data (e.g. [11]–[15]). The visual modality includes facial when watching videos were computed from physiolog-
expressions and/or body gestures. The audio modality ical responses using linear regression [26]. Quantized
covers posed or genuine emotional speech in different arousal and valence levels for a clip were then mapped
languages.Manyoftheexistingvisualdatabasesinclude to emotion labels. This mapping enabled the retrievalof
only posed or deliberately expressed emotions. video clips based on keyword queries. So far this novel
|        |            |          |     |     |           |           | method | achieved | low | precision. |     |     |     |     |
| ------ | ---------- | -------- | --- | --- | --------- | --------- | ------ | -------- | --- | ---------- | --- | --- | --- | --- |
| Healey | [16], [17] | recorded | one | of  | the first | affective |        |          |     |            |     |     |     |     |
physiologicaldatasets.Sherecorded24participantsdriv- Yazdani et al. [27] proposed using a brain computer
ing around the Boston area and annotated the dataset interface (BCI) based on P300 evoked potentials to emo-
|        |                 |        |     |        |                |     | tionally | tag | videos | with | one of | the six | Ekman | basic |
| ------ | --------------- | ------ | --- | ------ | -------------- | --- | -------- | --- | ------ | ---- | ------ | ------- | ----- | ----- |
| by the | drivers’ stress | level. | 17  | Of the | 24 participant |     |          |     |        |      |        |         |       |       |
responsesarepubliclyavailable1.Herrecordingsinclude emotions [28]. Their system was trained with 8 partici-
electrocardiogram (ECG), galvanic skin response (GSR) pants and then tested on 4 others. They achieved a high
recorded from hands and feet, electromyogram (EMG) accuracy on selecting tags. However, in their proposed
fromtherighttrapeziusmuscleandrespirationpatterns. system, a BCI only replaces the interface for explicit
|        |             |            |     |          |          |        | expression | of  | emotional | tags, | i.e. | the method |     | does not |
| ------ | ----------- | ---------- | --- | -------- | -------- | ------ | ---------- | --- | --------- | ----- | ---- | ---------- | --- | -------- |
| To the | best of our | knowledge, |     | the only | publicly | avail- |            |     |           |       |      |            |     |          |
able multi-modal emotional databases which includes implicitly tag a multimedia item using the participant’s
both physiological responses and facial expressions are behavioral and psycho-physiological responses.
the enterface 2005 emotional database and MAHNOB In addition to implicit tagging using behavioral
HCI [4], [5]. The first one was recorded by Savran cues, multiple studies used multimedia content analy-
|            |               |     |          |     |       |           | sis (MCA) | for | automated |     | affective | tagging | of  | videos. |
| ---------- | ------------- | --- | -------- | --- | ----- | --------- | --------- | --- | --------- | --- | --------- | ------- | --- | ------- |
| et al [5]. | This database |     | includes | two | sets. | The first |           |     |           |     |           |         |     |         |
set has electroencephalogram (EEG), peripheral physi- Hanjalic et al. [29] introduced ”personalized content
ological signals, functional near infra-red spectroscopy delivery” as a valuable tool in affective indexing and
(fNIRS) and facial videos from 5 male participants. The retrieval systems. In order to represent affect in video,
second datasetonlyhasfNIRSandfacialvideosfrom16 they first selected video- and audio- content features
|              |         |          |      |           |     |          | based | on their | relation | to  | the valence-arousal |     |     | space. |
| ------------ | ------- | -------- | ---- | --------- | --- | -------- | ----- | -------- | -------- | --- | ------------------- | --- | --- | ------ |
| participants | of both | genders. | Both | databases |     | recorded |       |          |          |     |                     |     |     |        |
spontaneous responses to emotional images from the Then, arising emotions were estimated in this space by
international affective picture system (IAPS) [18]. An combining these features. While valence-arousal could
|     |     |     |     |     |     |     | be used | separately | for | indexing, |     | they combined |     | these |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | --------- | --- | ------------- | --- | ----- |
1.http://www.physionet.org/pn3/drivedb/ valuesbyfollowingtheirtemporalpattern.Thisallowed

| IEEETRANS.AFFECTIVECOMPUTING |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 3   |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TABLE1
| for determining |     | an  | affect | curve, shown |     | to be useful | for |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | ------ | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Databasecontentsummary
| extracting  | video      | highlights |          | in a movie | or       | sports        | video.   |               |        |                  |                                       |            |     |     |     |
| ----------- | ---------- | ---------- | -------- | ---------- | -------- | ------------- | -------- | ------------- | ------ | ---------------- | ------------------------------------- | ---------- | --- | --- | --- |
| Wang        | and        | Cheong     | [30]used | audioand   |          | videofeatures |          |               |        |                  |                                       |            |     |     |     |
|             |            |            |          |            |          |               |          |               |        | Onlinesubjective |                                       | annotation |     |     |     |
| to classify | basic      | emotions   |          | elicited   | by movie | scenes.       | Au-      |               |        |                  |                                       |            |     |     |     |
|             |            |            |          |            |          |               |          | Numberof      | videos |                  | 120                                   |            |     |     |     |
| dio was     | classified | into       | music,   | speech     | and      | environment   |          |               |        |                  |                                       |            |     |     |     |
|             |            |            |          |            |          |               |          | Videoduration |        |                  | 1minuteaffectivehighlight(section2.2) |            |     |     |     |
| signals     | and        | these were | treated  | separately |          | to            | shape an |               |        |                  |                                       |            |     |     |     |
60vialast.fmaffectivetags,
aural affective feature vector. The aural affective vector Selection method
60manuallyselected
| of each | scene    | was fused | with   | video-based |     | features | such    |                  |     |       |       |     |     |     |     |
| ------- | -------- | --------- | ------ | ----------- | --- | -------- | ------- | ---------------- | --- | ----- | ----- | --- | --- | --- | --- |
|         |          |           |        |             |     |          |         | No.of ratingsper |     | video | 14-16 |     |     |     |     |
| as key  | lighting | and       | visual | excitement  |     | to form  | a scene |                  |     |       |       |     |     |     |     |
Arousal
| feature | vector. | Finally, | using | the | scene | feature | vectors, | Ratingscales |     |     |     |     |     |     |     |
| ------- | ------- | -------- | ----- | --- | ----- | ------- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Valence
Dominance
| movie sceneswereclassified |     |     |     | andlabeledwith |     | emotions. |     |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | -------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Soleymani et. al proposed a scene affective character- Ratingvalues Discretescale of1-9
| ization     | using    | a Bayesian |         | framework        | [31].            | Arousal | and      |           |              |               |                                   |            |     |     |     |
| ----------- | -------- | ---------- | ------- | ---------------- | ---------------- | ------- | -------- | --------- | ------------ | ------------- | --------------------------------- | ---------- | --- | --- | --- |
|             |          |            |         |                  |                  |         |          |           |              | Physiological |                                   | Experiment |     |     |     |
| valence     | of each  | shot       | were    | first determined |                  | using   | linear   |           |              |               |                                   |            |     |     |     |
|             |          |            |         |                  |                  |         |          | Numberof  | participants |               | 32                                |            |     |     |     |
| regression. | Then,    | arousaland |         | valence          | valuesinaddition |         |          |           |              |               |                                   |            |     |     |     |
|             |          |            |         |                  |                  |         |          | Numberof  | videos       |               | 40                                |            |     |     |     |
| to content  | features |            | of each | scene            | were             | used to | classify |           |              |               |                                   |            |     |     |     |
|             |          |            |         |                  |                  |         |          | Selection | method       |               | Subsetofonlineannotatedvideoswith |            |     |     |     |
everyscene into threeclasses,namelycalm,excitedpos- clearestresponses(seesection2.3)
| itive andexcitednegative.The |     |     |     | Bayesianframeworkwas |     |     |     |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Arousal
able to incorporate the movie genre and the predicted Ratingscales Valence
Dominance
| emotion | from | the last | scene | or temporal |     | information | to  |     |     |     |        |                             |     |     |     |
| ------- | ---- | -------- | ----- | ----------- | --- | ----------- | --- | --- | --- | --- | ------ | --------------------------- | --- | --- | --- |
|         |      |          |       |             |     |             |     |     |     |     | Liking | (howmuchdoyoulikethevideo?) |     |     |     |
improve the classification accuracy. Familiarity(howwelldoyouknowthevideo?)
Therearealsovariousstudiesonmusic affectivechar- Familiarity:discretescaleof1-5
Ratingvalues
acterization from acoustic features [32]–[34]. Rhythm, Others:continuousscaleof1-9
tempo, Mel-frequency cepstral coefficients (MFCC), 32-channel512HzEEG
|             |          |     |      |             |        |     |          | Recordedsignals |     |     | Peripheralphysiological |     | signals |     |     |
| ----------- | -------- | --- | ---- | ----------- | ------ | --- | -------- | --------------- | --- | --- | ----------------------- | --- | ------- | --- | --- |
| pitch, zero | crossing |     | rate | are amongst | common |     | features |                 |     |     |                         |     |         |     |     |
Facevideo(for22participants)
| which have | been  | used | to          | characterize | affect | in        | music. |     |     |     |     |     |     |     |     |
| ---------- | ----- | ---- | ----------- | ------------ | ------ | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| A pilot    | study | for  | the current | work         | was    | presented | in     |     |     |     |     |     |     |     |     |
[35].Inthatstudy,6participants’EEGandphysiological
| signals | were | recordedas |     | each watched |     | 20 music | videos. |     |     |     |     |     |     |     |     |
| ------- | ---- | ---------- | --- | ------------ | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
The participants rated arousal and valence levels and physiological signals. Inaddition, itis the only database
|         |     |               |     |         |     |            |      | that uses | music | videos | as emotional | stimuli. |     |     |     |
| ------- | --- | ------------- | --- | ------- | --- | ---------- | ---- | --------- | ----- | ------ | ------------ | -------- | --- | --- | --- |
| the EEG | and | physiological |     | signals | for | each video | were |           |       |        |              |          |     |     |     |
classified into low/high arousal/valence classes. We present an extensive statistical analysis of the
In the currentwork, music video clips are used asthe participant’s ratings and of the correlates between the
|        |         |           |           |           |     |     |           | EEG signals | and | the | ratings. | Preliminary |     | single | trial |
| ------ | ------- | --------- | --------- | --------- | --- | --- | --------- | ----------- | --- | --- | -------- | ----------- | --- | ------ | ----- |
| visual | stimuli | to elicit | different | emotions. |     | To  | this end, |             |     |     |          |             |     |        |       |
a relatively large set of music video clips was gathered classification results of EEG, peripheral physiological
|          |              |     |           |         |      |             |      | signals  | and MCA   | are presented |     | and compared. |     | Finally, |     |
| -------- | ------------ | --- | --------- | ------- | ---- | ----------- | ---- | -------- | --------- | ------------- | --- | ------------- | --- | -------- | --- |
| using a  | novelstimuli |     | selection | method. |      | Asubjective | test |          |           |               |     |               |     |          |     |
|          |              |     |           |         |      |             |      | a fusion | algorithm | is utilized   |     | to combine    | the | results  | of  |
| was then | performed    |     | to select | the     | most | appropriate | test |          |           |               |     |               |     |          |     |
material. For each video, a one-minute highlight was each modality and arrive at a more robust decision.
|          |                |     |     |              |     |           |        | The layout | of  | the paper |     | is as follows. | In  | Section | 2   |
| -------- | -------------- | --- | --- | ------------ | --- | --------- | ------ | ---------- | --- | --------- | --- | -------------- | --- | ------- | --- |
| selected | automatically. |     | 32  | participants |     | took part | in the |            |     |           |     |                |     |         |     |
experiment and their EEG and peripheral physiological the stimuli selection procedure is described in detail.
|               |      |              |     |              |       |        |          | The experiment |               | setup | is covered | in     | Section | 3. Section |     |
| ------------- | ---- | ------------ | --- | ------------ | ----- | ------ | -------- | -------------- | ------------- | ----- | ---------- | ------ | ------- | ---------- | --- |
| signals       | were | recorded     | as  | they watched |       | the 40 | selected |                |               |       |            |        |         |            |     |
|               |      |              |     |              |       |        |          | 4 provides     | a statistical |       | analysis   | of the | ratings | given      | by  |
| music videos. |      | Participants |     | rated each   | video | in     | terms of |                |               |       |            |        |         |            |     |
arousal,valence,like/dislike,dominanceandfamiliarity. participants during the experiment and a validation of
|     |     |     |     |     |     |     |     | our stimuli | selection | method. |     | In Section | 5, correlatesbe- |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | ------- | --- | ---------- | ---------------- | --- | --- |
For22participants,frontalfacevideowasalsorecorded.
Thispaperaimsatintroducingthispubliclyavailable2 tween the EEG frequencies and the participants’ ratings
|     |     |     |     |     |     |     |     | are presented. |     | The method |     | and results | of  | single-trial |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------- | --- | ----------- | --- | ------------ | --- |
database.Thedatabasecontainsallrecordedsignaldata,
|         |      |           |     |           |     |              |     | classification | are | given | in Section | 6. The | conclusion |     | of  |
| ------- | ---- | --------- | --- | --------- | --- | ------------ | --- | -------------- | --- | ----- | ---------- | ------ | ---------- | --- | --- |
| frontal | face | video for | a   | subset of | the | participants | and |                |     |       |            |        |            |     |     |
subjective ratings from the participants. Also included this work follows in Section 7.
| isthe subjectiveratingsfromthe |         |     |      | initialonline |            | subjective |        |           |           |     |     |     |     |     |     |
| ------------------------------ | ------- | --- | ---- | ------------- | ---------- | ---------- | ------ | --------- | --------- | --- | --- | --- | --- | --- | --- |
| annotation                     | and     | the | list | of 120        | videos     | used.      | Due to |           |           |     |     |     |     |     |     |
|                                |         |     |      |               |            |            |        | 2 STIMULI | SELECTION |     |     |     |     |     |     |
| licensing                      | issues, | we  | are  | not able      | to include | the        | actual |           |           |     |     |     |     |     |     |
videos, butYouTube links areincluded. Table 1 gives an The stimuli used in the experiment were selected in
overview of the database contents. several steps. First, we selected 120 initial stimuli, half
|        |      |        |            |     |               |     |         | of which | were | chosen | semi-automatically |     | and | the | rest |
| ------ | ---- | ------ | ---------- | --- | ------------- | --- | ------- | -------- | ---- | ------ | ------------------ | --- | --- | --- | ---- |
| To the | best | of our | knowledge, |     | this database |     | has the |          |      |        |                    |     |     |     |      |
highest number of participants in publicly available manually. Then, a one-minute highlight part was deter-
databases for analysis of spontaneous emotions from mined for each stimulus. Finally, through a web-based
|     |     |     |     |     |     |     |     | subjective | assessment | experiment, |     | 40  | final stimuli |     | were |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | ----------- | --- | --- | ------------- | --- | ---- |
2.http://www.eecs.qmul.ac.uk/mmv/datasets/deap/ selected. Each of these steps is explained below.

| IEEETRANS.AFFECTIVECOMPUTING |     |     |     |     |     |     |     |     |     |     |     |     |     | 4   |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2.1 Initialstimuliselection
|           |           |           |      |      |              |          | In order  | to extract              | a           | segment | with     | maximum    |     | emotional |
| --------- | --------- | --------- | ---- | ---- | ------------ | -------- | --------- | ----------------------- | ----------- | ------- | -------- | ---------- | --- | --------- |
|           |           |           |      |      |              |          | content,  | anaffectivehighlighting |             |         |          | algorithm  | is  | proposed. |
| Eliciting | emotional | reactions | from | test | participants | is       | a         |                         |             |         |          |            |     |           |
|           |           |           |      |      |              |          | Soleymani |                         | et al. [31] | used    | a linear | regression |     | method    |
| difficult | task and  | selecting | the  | most | effective    | stimulus |           |                         |             |         |          |            |     |           |
materials is crucial. We propose here a semi-automated to calculate arousal for each shot of in movies. In their
|     |     |     |     |     |     |     | method, | the arousaland |     | valenceof |     | shots | wascomputed |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | --- | --------- | --- | ----- | ----------- | --- |
method forstimulusselection,withthegoalofminimiz-
ing the bias arising from manual stimuli selection. using a linear regression on the content-based features.
Informativefeaturesforarousalestimationincludeloud-
| 60 of | the 120 | initially | selected | stimuli | were | selected |     |     |     |     |     |     |     |     |
| ----- | ------- | --------- | -------- | ------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
nessandenergyoftheaudiosignals,motioncomponent,
| using the | Last.fm3 | music | enthusiast |     | website. | Last.fm |     |     |     |     |     |     |     |     |
| --------- | -------- | ----- | ---------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
allows users to track their music listening habits and visualexcitementandshotduration.Thesameapproach
|         |                 |     |     |           |     |             | was used | to  | compute | valence. | There | are | other | content |
| ------- | --------------- | --- | --- | --------- | --- | ----------- | -------- | --- | ------- | -------- | ----- | --- | ----- | ------- |
| receive | recommendations |     | for | new music |     | and events. |          |     |         |          |       |     |       |         |
Additionally,itallowstheuserstoassigntagstoindivid- features such as color variance and key lighting that
ual songs, thus creating a folksonomy of tags. Many of havebeenshown to becorrelatedwith valence[30].The
|          |                 |     |           |      |     |              | detailed | description |     | of the | content | features | used | in this |
| -------- | --------------- | --- | --------- | ---- | --- | ------------ | -------- | ----------- | --- | ------ | ------- | -------- | ---- | ------- |
| the tags | carry emotional |     | meanings, | such | as  | ’depressing’ |          |             |     |        |         |          |      |         |
or ’aggressive’. Last.fm offers an API, allowing one to work is given in Section 6.2.
|          |          |        |        |     |     |     | In order | to  | find | the best | weights |     | for arousal | and |
| -------- | -------- | ------ | ------ | --- | --- | --- | -------- | --- | ---- | -------- | ------- | --- | ----------- | --- |
| retrieve | tags and | tagged | songs. |     |     |     |          |     |      |          |         |     |             |     |
A list of emotional keywords was taken from [7] and valence estimation using regression, the regressors were
expanded to include inflections and synonyms, yielding trainedonallshotsin21annotatedmoviesinthedataset
|               |     |           |      |          |               |     | presented | in [31]. | The | linear | weights | were | computed | by  |
| ------------- | --- | --------- | ---- | -------- | ------------- | --- | --------- | -------- | --- | ------ | ------- | ---- | -------- | --- |
| 304 keywords. |     | Next, for | each | keyword, | corresponding |     |           |          |     |        |         |      |          |     |
tagswerefound inthe Last.fmdatabase.For eachfound means of a relevance vector machine (RVM) from the
RVMtoolboxprovidedbyTipping[36].TheRVMisable
| affective | tag, the | ten songs | most | often | labeled | with this |     |     |     |     |     |     |     |     |
| --------- | -------- | --------- | ---- | ----- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
tag were selected. This resulted in a total of 1084 songs. torejectuninformativefeaturesduringitstraininghence
The valence-arousal space can be subdivided into 4 no further feature selection was used for arousal and
valence determination.
quadrants,namelylowarousal/lowvalence(LALV),low
arousal/highvalence(LAHV),higharousal/lowvalence The music videos were then segmented into one
(HALV) and high arousal/high valence (HAHV). In minute segments with 55 seconds overlap between seg-
order to ensure diversity of induced emotions, from the ments.Contentfeatureswereextractedandprovidedthe
1084songs,15wereselectedmanuallyforeachquadrant input for the regressors. The emotional highlight score
|           |                |           |           |               |     |          | ofthei-thsegmentei |     |     | wascomputedusingthefollowing |     |     |     |     |
| --------- | -------------- | --------- | --------- | ------------- | --- | -------- | ------------------ | --- | --- | ---------------------------- | --- | --- | --- | --- |
| according | to the         | following | criteria: |               |     |          |                    |     |     |                              |     |     |     |     |
| Does the  | tag accurately |           | reflect   | the emotional |     | content? | equation:          |     |     |                              |     |     |     |     |
Examplesofsongssubjectivelyrejectedaccordingtothis
criterium include songs that are tagged merely because ei = a2 +v 2 (1)
|          |          |        |      |             |     |             |     |     |     |     | i   | i   |     |     |
| -------- | -------- | ------ | ---- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| the song | title or | artist | name | corresponds |     | to the tag. |     |     |     |     |     |     |     |     |
q
|     |     |     |     |     |     |     | The arousal, |     | ai, and | valence, | vi, | were | centered. | There- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | -------- | --- | ---- | --------- | ------ |
Also,insomecasesthelyricsmaycorrespondtothetag,
but the actual emotional content of the song is entirely fore, a smaller emotional highlight score (ei) is closer
different (e.g. happy songs about sad topics). to the neutral state. For each video, the one minute
|            |       |           |     |           |     |     | long segmentwiththe |     |     | highestemotionalhighlight |     |     |     | score |
| ---------- | ----- | --------- | --- | --------- | --- | --- | ------------------- | --- | --- | ------------------------- | --- | --- | --- | ----- |
| Is a music | video | available | for | the song? |     |     |                     |     |     |                           |     |     |     |       |
Music videosfor the songs were automaticallyretrieved was chosen to be extracted for the experiment. For a
from YouTube, corrected manually where necessary. fewclips,theautomaticaffectivehighlightdetectionwas
However, many songs do not have a music video. manuallyoverridden.Thiswasdoneonlyforsongswith
Is the song appropriate for use in the experiment? segments that are particularly characteristic of the song,
|           |                   |     |      |        |          |      | well-known | to  | the public, |     | and most | likely | to  | elicit emo- |
| --------- | ----------------- | --- | ---- | ------ | -------- | ---- | ---------- | --- | ----------- | --- | -------- | ------ | --- | ----------- |
| Since our | test participants |     | were | mostly | European | stu- |            |     |             |     |          |        |     |             |
dents, we selected those songs most likely to elicit tional reactions. In these cases, the one-minute highlight
emotions for this target demographic. Therefore,mainly was selected so that these segments were included.
European or North American artists were selected. Given the 120 one-minute music video segments, the
In addition to the songs selected using the method final selection of 40 videos used in the experiment was
described above, 60 stimulus videos were selected man- madeon the basisofsubjective ratings byvolunteers, as
ually, with 15 videos selected for each of the quadrants described in the next section.
inthearousal/valencespace.Thegoalherewastoselect
thosevideosexpectedtoinducethemostclearemotional
2.3 Onlinesubjectiveannotation
| reactions | for each | of  | the quadrants. |     | The | combination |     |     |     |     |     |     |     |     |
| --------- | -------- | --- | -------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
of manual selection and selection using affective tags From the initial collection of 120 stimulus videos, the
produced a list of 120 candidate stimulus videos. final 40 test video clips were chosen by using a web-
|     |     |     |     |     |     |     | based subjective |     | emotion |     | assessment | interface. |     | Partici- |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------- | --- | ---------- | ---------- | --- | -------- |
2.2 Detectionofone-minutehighlights pantswatchedmusicvideosandratedthemonadiscrete
|            |     |              |          |       |         |       | 9-point    | scale | for valence,  |     | arousal  | and | dominance. | A       |
| ---------- | --- | ------------ | -------- | ----- | ------- | ----- | ---------- | ----- | ------------- | --- | -------- | --- | ---------- | ------- |
| For eachof | the | 120initially | selected | music | videos, | a one |            |       |               |     |          |     |            |         |
|            |     |              |          |       |         |       | screenshot | of    | the interface |     | is shown |     | in Fig.    | 1. Each |
minutesegmentforuseintheexperimentwasextracted.
|     |     |     |     |     |     |     | participant | watched |     | as many | videos | as  | he/she | wanted |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | --- | ------- | ------ | --- | ------ | ------ |
3.http://www.last.fm and was able toend the rating atany time. The orderof

IEEETRANS.AFFECTIVECOMPUTING 5
2
1.5
Blur
Song 2
1
0.5
0
−0.5
−1
−1.5
−2
−2 −1.5 −1 −0.5 0 0.5 1 1.5 2
Arousal score
Fig. 1. Screenshot of the web interface for subjective
emotionassessment.
the clips was randomized, but preference was given to
the clips rated by the least number of participants. This
ensured a similar number of ratings for each video (14-
16assessmentspervideowerecollected).Itwasensured
that participants never saw the same video twice.
After all of the 120 videos were rated by at least
14 volunteers each, the final 40 videos for use in the
experiment were selected. To maximize the strength of
elicited emotions, we selected those videos that had the
strongest volunteer ratingsand atthe same time a small
variation. To this end, for each video x we calculated
a normalized arousal and valence score by taking the
mean rating divided by the standard deviation (µx/σx).
Then, for each quadrant in the normalized valence-
arousal space, we selected the 10 videos that lie closest
to the extreme corner of the quadrant. Fig. 2 shows
the score for the ratings of each video and the selected
videos highlighted in green. The video whose rating
was closest to the extreme corner of each quadrant is
mentioned explicitly. Of the 40 selected videos, 17 were
selected via Last.fm affectivetags, indicating that useful
stimuli can be selected via this method.
3 EXPERIMENT SETUP
3.1 MaterialsandSetup
The experiments were performed in two laboratory
environments with controlled illumination. EEG and
peripheral physiological signals were recorded using a
BiosemiActiveTwosystem4 onadedicatedrecordingPC
(Pentium 4, 3.2 GHz). Stimuli were presented using a
dedicated stimulus PC (Pentium 4, 3.2 GHz) that sent
4.http://www.biosemi.com
erocs
ecnelaV
Louis Armstrong
What a wonderful world
Napalm death
Procrastination on the
empty vessel
Sia
Breathe me
Fig. 2. µx/σx value for the ratings of each video in
the online assessment. Videos selected for use in the
experiment are highlighted in green. For each quadrant,
themostextremevideoisdetailed withthesongtitleand
ascreenshotfromthevideo.
synchronization markers directly to the recording PC.
For presentation of the stimuli and recording the users’
ratings, the ”Presentation”softwarebyNeurobehavioral
systems5 was used. The music videos were presented
on a 17-inch screen (1280×1024, 60 Hz) and in order
to minimize eye movements, all video stimuli were
displayed at 800×600 resolution, filling approximately
2/3 of the screen. Subjects were seated approximately
1 meter from the screen. Stereo Philips speakers were
used and the music volume was set at a relatively loud
level, however each participant was asked before the
experiment whether the volume was comfortable and it
was adjusted when necessary.
EEG was recorded at a sampling rate of 512 Hz using
32 active AgCl electrodes (placed according to the inter-
national10-20system).Thirteenperipheralphysiological
signals (which will be further discussed in section 6.1)
were also recorded. Additionally, for the first 22 of the
32 participants, frontal face video was recorded in DV
quality using a Sony DCR-HC27E consumer-grade cam-
corder.Thefacevideowasnotusedintheexperimentsin
thispaper,butismadepubliclyavailablealongwiththe
restofthedata.Fig. 3illustratesthe electrodeplacement
for acquisition of peripheral physiological signals.
3.2 Experimentprotocol
32 Healthy participants (50% female), aged between 19
and 37 (mean age 26.9), participated in the experiment.
Prior to the experiment, each participant signed a con-
sentformandfilledoutaquestionnaire.Next,theywere
given a setof instructions to readinforming them of the
experiment protocol and the meaning of the different
scales used for self-assessment. An experimenter was
also present there to answer any questions. When the
5.http://www.neurobs.com

| IEEETRANS.AFFECTIVECOMPUTING |     |     |                          |     |     |                       |     |     |     |     |     |     |     |     | 6   |
| ---------------------------- | --- | --- | ------------------------ | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EXG sensors face             |     |     | EXG sensors trapezius,   |     |     | Left hand             |     |     |     |     |     |     |     |     |     |
|                              |     |     | respiration belt and EEG |     |     | physiological sensors |     |     |     |     |     |     |     |     |     |
3
GSR1 GSR2
32 EEG electrodes
| 2   |     | 1   |     | 10-20 system |     |     | Temp. |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------------ | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
Pleth.
| 4   |     | 6   |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5 ~1cm
~1cm
7
8 ~1cm
Respiration belt
| Fig. 3.        | Placement |        | of peripheral |           | physiological |             | sensors.  |                                                |     |     |     |     |     |     |     |
| -------------- | --------- | ------ | ------------- | --------- | ------------- | ----------- | --------- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| For Electrodes |           | were   | used to       | recordEOG |               | and 4       | for EMG   |                                                |     |     |     |     |     |     |     |
| (zygomaticus   |           | major  | and trapezius |           | muscles).     | In          | addition, |                                                |     |     |     |     |     |     |     |
|                |           |        |               |           |               |             |           | Fig.4. Aparticipantshortlybeforetheexperiment. |     |     |     |     |     |     |     |
| GSR, blood     |           | volume | pressure      | (BVP),    |               | temperature | and       |                                                |     |     |     |     |     |     |     |
respirationweremeasured.
instructionswerecleartotheparticipant,he/shewasled
| into theexperimentroom.Afterthesensors |                   |                                    |                   |                  |               | wereplaced    |            |     |     |     |     |     |     |     |     |
| -------------------------------------- | ----------------- | ---------------------------------- | ----------------- | ---------------- | ------------- | ------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| and their                              | signals           | checked,                           |                   | the participants |               | performed     |            | a   |     |     |     |     |     |     |     |
| practice                               | trial             | to familiarize                     |                   | themselves       |               | with the      | system.    |     |     |     |     |     |     |     |     |
| In this                                | unrecorded        |                                    | trial, a          | short            | video         | was shown,    | fol-       |     |     |     |     |     |     |     |     |
| lowed by                               | a self-assessment |                                    |                   | by the           | participant.  | Next,         | the        |     |     |     |     |     |     |     |     |
| experimenter                           |                   | started                            | the physiological |                  | signals       | recording     |            |     |     |     |     |     |     |     |     |
| andlefttheroom,                        |                   | afterwhichtheparticipantstartedthe |                   |                  |               |               |            |     |     |     |     |     |     |     |     |
| experiment                             | by                | pressing                           | a key             | on               | the keyboard. |               |            |     |     |     |     |     |     |     |     |
| The experiment                         |                   |                                    | started           | with             | a 2           | minute        | baseline   |     |     |     |     |     |     |     |     |
| recording,                             | during            | which                              | a                 | fixation         | cross         | was displayed |            |     |     |     |     |     |     |     |     |
| to the participant                     |                   | (who                               | was               | asked            | to relax      | during        | this       |     |     |     |     |     |     |     |     |
| period).                               | Then              | the 40                             | videos            | were             | presented     | in            | 40 trials, |     |     |     |     |     |     |     |     |
| each consisting                        |                   | of the                             | following         | steps:           |               |               |            |     |     |     |     |     |     |     |     |
1) A2secondscreendisplayingthecurrenttrialnum-
| ber    | to inform |          | the participants |        | of their  | progress. |     |     |     |     |     |     |     |     |     |
| ------ | --------- | -------- | ---------------- | ------ | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2) A   | 5 second  | baseline | recording        |        | (fixation | cross).   |     |     |     |     |     |     |     |     |     |
| 3) The | 1 minute  |          | display          | of the | music     | video.    |     |     |     |     |     |     |     |     |     |
4) Self-assessment for arousal, valence, liking and Fig. 5. Images used for self-assessment. from top: Va-
| dominance. |     |     |     |     |     |     |     | lenceSAM,ArousalSAM,DominanceSAM,Liking. |     |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
After20trials,theparticipantstookashortbreak.Dur-
| ing the      | break,        | they | were offered | some       | cookies | and          | non- |              |      |          |     |      |       |                |     |
| ------------ | ------------- | ---- | ------------ | ---------- | ------- | ------------ | ---- | ------------ | ---- | -------- | --- | ---- | ----- | -------------- | --- |
| caffeinated, | non-alcoholic |      |              | beverages. | The     | experimenter |      |              |      |          |     |      |       |                |     |
|              |               |      |              |            |         |              |      | Participants | were | informed |     | they | could | click anywhere |     |
thencheckedthequalityofthesignalsandtheelectrodes
|            |      |     |              |      |         |               |          | directly        | below | or in-between |     | the    | numbers, | making | the |
| ---------- | ---- | --- | ------------ | ---- | ------- | ------------- | -------- | --------------- | ----- | ------------- | --- | ------ | -------- | ------ | --- |
| placement  | and  | the | participants | were | asked   | to            | continue |                 |       |               |     |        |          |        |     |
|            |      |     |              |      |         |               |          | self-assessment |       | a continuous  |     | scale. |          |        |     |
| the second | half | of  | the test.    | Fig. | 4 shows | a participant |          |                 |       |               |     |        |          |        |     |
shortly before the start of the experiment. The valence scale ranges from unhappy or sad to
|     |     |     |     |     |     |     |     | happy or | joyful.       | The | arousal     | scale | ranges        | from | calm  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | ----------- | ----- | ------------- | ---- | ----- |
|     |     |     |     |     |     |     |     | or bored | to stimulated |     | or excited. |       | The dominance |      | scale |
3.3 Participantself-assessment
|     |     |     |     |     |     |     |     | ranges from | submissive |     | (or | ”without | control”) |     | to dom- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | --- | -------- | --------- | --- | ------- |
At the end of each trial, participants performed a self- inant (or ”in control, empowered”). A fourth scale asks
assessment of their levels of arousal, valence, liking and for participants’ personal liking of the video. This last
dominance. Self-assessment manikins (SAM) [37] were scaleshouldnotbeconfusedwiththevalencescale.This
used to visualize the scales (see Fig. 5). For the liking measureinquires aboutthe participants’tastes,not their
scale,thumbsdown/thumbsupsymbolswereused.The feelings. For example, it is possible to like videos that
manikins were displayed in the middle of the screen makeonefeelsadorangry.Finally,aftertheexperiment,
withthenumbers1-9printedbelow. Participantsmoved participantswereaskedtoratetheirfamiliaritywitheach
the mouse strictly horizontally just below the num- of the songs on a scale of 1 (”Never heard it before the
bers and clicked to indicate their self-assessment level. experiment”) to 5 (”Knew the song very well”).

| IEEETRANS.AFFECTIVECOMPUTING |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 7   |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4 ANALYSIS
OF SUBJECTIVE RATINGS low arousal. The distribution of the individual rat-
|         |         |             |            |            |          |           |          | ings per | conditions  |           | (see Fig. | 7) shows | a                | large | variance |
| ------- | ------- | ----------- | ---------- | ---------- | -------- | --------- | -------- | -------- | ----------- | --------- | --------- | -------- | ---------------- | ----- | -------- |
| In this | section | we describe |            | the effect | the      | affective | stim-    |          |             |           |           |          |                  |       |          |
|         |         |             |            |            |          |           |          | within   | conditions, | resulting |           | from     | between-stimulus |       | and      |
| ulation | had     | on the      | subjective | ratings    | obtained |           | from the |          |             |           |           |          |                  |       |          |
-participantvariations,possiblyassociatedwithstimulus
| participants. |     | Firstly, | we will | provide    | descriptive |     | statis-  |                 |     |                     |     |     |             |     |       |
| ------------- | --- | -------- | ------- | ---------- | ----------- | --- | -------- | --------------- | --- | ------------------- | --- | --- | ----------- | --- | ----- |
|               |     |          |         |            |             |     |          | characteristics |     | or inter-individual |     |     | differences | in  | music |
| tics for      | the | recorded | ratings | of liking, | valence,    |     | arousal, |                 |     |                     |     |     |             |     |       |
taste,generalmood,orscaleinterpretation.However,the
dominance,andfamiliarity.Secondly,wewilldiscussthe
significantdifferencesbetweentheconditionsintermsof
| covariation |      | of the different    |     | ratings | with     | each   | other.   |             |            |          |             |     |             |                |     |
| ----------- | ---- | ------------------- | --- | ------- | -------- | ------ | -------- | ----------- | ---------- | -------- | ----------- | --- | ----------- | -------------- | --- |
|             |      |                     |     |         |          |        |          | the ratings | of valence |          | and arousal |     | reflect     | the successful |     |
| Stimuli     | were | selected            | to  | induce  | emotions | in     | the four |             |            |          |             |     |             |                |     |
|             |      |                     |     |         |          |        |          | elicitation | of the     | targeted | affective   |     | states (see | Table          | 2). |
| quadrants   | of   | the valence-arousal |     |         | space    | (LALV, | HALV,    |             |            |          |             |     |             |                |     |
LAHV,HAHV).Thestimulifromthesefouraffectelicita-
TABLE2
tionconditionsgenerallyresultedintheelicitationofthe
Themeanvalues(andstandarddeviations)ofthe
targetemotionaimedforwhenthestimuliwereselected,
differentratingsofliking(1-9),valence(1-9),arousal
| ensuring | that | large | parts | of the | arousal-valence |     | plane |                                  |     |     |     |     |                    |     |     |
| -------- | ---- | ----- | ----- | ------ | --------------- | --- | ----- | -------------------------------- | --- | --- | --- | --- | ------------------ | --- | --- |
|          |      |       |       |        |                 |     |       | (1-9),dominance(1-9),familiarity |     |     |     |     | (1-5)foreachaffect |     |     |
(AVplane)arecovered(seeFig.6).Wilcoxonsigned-rank
elicitationcondition.
| tests showed |     | that low | and | high arousal |     | stimuli | induced |     |     |     |     |     |     |     |     |
| ------------ | --- | -------- | --- | ------------ | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
differentvalenceratings(p<.0001andp<.00001).Sim-
|         |         |      |          |         |         |     |           | Cond. | Liking |     | Valence | Arousal | Dom. |     | Fam. |
| ------- | ------- | ---- | -------- | ------- | ------- | --- | --------- | ----- | ------ | --- | ------- | ------- | ---- | --- | ---- |
| ilarly, | low and | high | valenced | stimuli | induced |     | different |       |        |     |         |         |      |     |      |
arousal ratings (p<.001 and p<.0001). LALV 5.7(1.0) 4.2(0.9) 4.3(1.1) 4.5(1.4) 2.4(0.4)
|     |     |     |     |     |     |     |     | HALV | 3.6(1.3) |     | 3.7(1.0) | 5.7(1.5) | 5.0(1.6) | 1.4(0.6) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------- | --- | -------- | -------- | -------- | -------- | --- |
LAHV
|     |     |     |     |     |     |     |     |     | 6.4(0.9) |     | 6.6(0.8) | 4.7(1.0) | 5.7(1.3) | 2.4(0.4) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- | -------- | -------- | -------- | --- |
Stimulus locations, dominance, and liking in Arousal−Valence space HAHV 6.4(0.9) 6.6(0.6) 5.9(0.9) 6.3(1.0) 3.1(0.4)
8
| 7   | LLAAHHVV |     |     |     | HHAAHHVV |     |     |                  |          |     |           |                   |                 |         |          |
| --- | -------- | --- | --- | --- | -------- | --- | --- | ---------------- | -------- | --- | --------- | ----------------- | --------------- | ------- | -------- |
|     |          |     |     |     |          |     |     | The distribution |          | of  | ratings   | for the           | differentscales |         | and      |
|     |          |     |     |     |          |     |     | conditions       | suggests |     | a complex | relationship      |                 | between | rat-     |
|     |          |     |     |     |          |     |     | ings. We         | explored | the | mean      | inter-correlation |                 | of      | the dif- |
6
ferentscalesoverparticipants(seeTable3),astheymight
ecnelaV be indicative of possible confounds or unwanted effects
5
|     |          |     |     |     |          |     |     | of habituation |         | or fatigue. | We         | observed     |         | high     | positive |
| --- | -------- | --- | --- | --- | -------- | --- | --- | -------------- | ------- | ----------- | ---------- | ------------ | ------- | -------- | -------- |
|     |          |     |     |     |          |     |     | correlations   | between |             | liking     | and valence, |         | and      | between  |
|     |          |     |     |     |          |     |     | dominance      | and     | valence.    | Seemingly, |              | without | implying |          |
| 4   | LLAALLVV |     |     |     | HHAALLVV |     |     |                |         |             |            |              |         |          |          |
anycausality,peoplelikedmusicwhichgavethemapos-
|     |      |     |     |     |     |     |     | itive feelingand/orafeelingofempowerment.         |            |         |          |      |         |             | Medium   |
| --- | ---- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | ---------- | ------- | -------- | ---- | ------- | ----------- | -------- |
| 3   | LALV |     |     |     |     |     |     |                                                   |            |         |          |      |         |             |          |
|     | LAHV |     |     |     |     |     |     | positivecorrelationswereobservedbetweenarousaland |            |         |          |      |         |             |          |
|     | HALV |     |     |     |     |     |     | dominance,                                        | and        | between | arousal  | and  | liking. | Familiarity |          |
|     | HAHV |     |     |     |     |     |     | correlated                                        | moderately |         | positive | with | liking  | and         | valence. |
2
| 2   |     | 3   | 4   | 5   | 6   |     | 7   | 8          |          |     |        |     |           |         |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | ------ | --- | --------- | ------- | --- |
|     |     |     |     |     |     |     |     | As already | observed |     | above, | the | scales of | valence | and |
Arousal
|     |     |     |     |     |     |     |     | arousal | are not | independent, |     | but | their positive |     | correla- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------------ | --- | --- | -------------- | --- | -------- |
Fig. 6. The mean locations ofthe stimuli on the arousal- tion is ratherlow, suggesting thatparticipantswereable
valence plane for the 4 conditions (LALV, HALV, LAHV, to differentiate between these two important concepts.
HAHV). Liking is encoded by color: dark red is low liking Stimulus order had only a small effect on liking and
andbrightyellowishighliking.Dominanceisencodedby
|     |     |     |     |     |     |     |     | dominance | ratings, | and | no significant |     | relationship |     | with |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --- | -------------- | --- | ------------ | --- | ---- |
symbolsize:smallsymbolsstandforlowdominance and the other ratings, suggesting that effects of habituation
bigforhighdominance. and fatigue were kept to an acceptable minimum.
|     |     |     |     |     |     |     |     | In summary, |     | the affect | elicitation |     | was in | general | suc- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---------- | ----------- | --- | ------ | ------- | ---- |
The emotion elicitation worked specifically well for cessful, though the low valence conditions were par-
the high arousing conditions, yielding relative extreme tially biased by moderate valence responses and higher
valence ratings for the respective stimuli. The stimuli arousal. High scale inter-correlations observed are lim-
in the low arousing conditions were less successful in ited to the scale of valence with those of liking and
the elicitation of strong valence responses. Furthermore, dominance, and might be expected in the context of
some stimuli of the LAHV condition induced higher musical emotions. The restof the scale inter-correlations
arousal than expected on the basis of the online study. aresmallormediuminstrength,indicatingthatthescale
Interestingly, this results in a C-shape of the stimuli concepts were well distinguished by the participants.
| on the    | valence-arousal |      | plane | also              | observed  | in        | the well- |              |     |     |        |     |         |     |     |
| --------- | --------------- | ---- | ----- | ----------------- | --------- | --------- | --------- | ------------ | --- | --- | ------ | --- | ------- | --- | --- |
| validated | ratings         | for  | the   | international     | affective |           | picture   |              |     |     |        |     |         |     |     |
|           |                 |      |       |                   |           |           |           | 5 CORRELATES |     |     | OF EEG | AND | RATINGS |     |     |
| system    | (IAPS)          | [18] | and   | the international |           | affective | dig-      |              |     |     |        |     |         |     |     |
ital sounds system (IADS) [38], indicating the general For the investigation of the correlates of the subjective
difficulty to induce emotions with strong valence but ratingswiththeEEGsignals,theEEGdatawascommon

IEEETRANS.AFFECTIVECOMPUTING 8
8
6
4
2
L V A D F L V A D F L V A D F L V A D F
tnemssessa
fleS
Rating distributions for the emotion induction conditions
LALV HALV LAHV HAHV
Scales by condition
Fig.7. Thedistributionoftheparticipants’subjectiveratingsperscale(L-generalrating,V-valence,A-arousal,D-
dominance,F-familiarity)forthe4affectelicitationconditions(LALV,HALV,LAHV,HAHV).
TABLE4
Theelectrodesforwhichthecorrelationswiththescaleweresignificant(*=p<.01,**=p<.001).Alsoshownisthe
meanofthesubject-wisecorrelations(R¯),themostnegative(R −),andthemostpositivecorrelation(R+).
Theta Alpha Beta Gamma
Elec. R ¯ R− R+ Elec. R ¯ R− R+ Elec. R ¯ R− R+ Elec. R ¯ R− R+
Arousal CP6* -0.06 -0.47 0.25 Cz* -0.07 -0.45 0.23 FC2* -0.06 -0.40 0.28
Oz** 0.08 -0.23 0.39 PO4* 0.05 -0.26 0.49 CP1** -0.07 -0.49 0.24 T7** 0.07 -0.33 0.51
PO4* 0.05 -0.26 0.49 Oz* 0.05 -0.24 0.48 CP6* 0.06 -0.26 0.43
FC6* 0.06 -0.52 0.49 CP2* 0.08 -0.21 0.49
Valence Cz* -0.04 -0.64 0.30 C4** 0.08 -0.31 0.51
T8** 0.08 -0.26 0.50
FC6** 0.10 -0.29 0.52
F8* 0.06 -0.35 0.52
C3* 0.08 -0.35 0.31 AF3* 0.06 -0.27 0.42 FC6* 0.07 -0.40 0.48 T8* 0.04 -0.33 0.49
Liking
F3* 0.06 -0.42 0.45
TABLE3
fivesecondsbeforeeachvideowasextractedasbaseline.
Themeansofthesubject-wiseinter-correlationsbetween
The frequency power of trials and baselines between
thescalesofvalence,arousal,liking,dominance,
3 and 47 Hz was extracted with Welch’s method with
familiarity andtheorderofthepresentation(i.e.time)for
windows of 256 samples. The baseline power was then
all40stimuli.Significantcorrelations(p<.05)according
subtracted from the trial power, yielding the change of
toFisher’smethodareindicatedbystars.
powerrelativetothepre-stimulusperiod.Thesechanges
of power were averaged over the frequency bands of
Scale Liking Valence Arousal Dom. Fam. Order theta (3 - 7 Hz), alpha (8 - 13 Hz), beta (14 - 29 Hz),
Liking 1 0.62* 0.29* 0.31* 0.30* 0.03* and gamma (30 - 47 Hz). For the correlation statistic,
Valence 1 0.18* 0.51* 0.25* 0.02 we computed the Spearman correlated coefficients be-
Arousal 1 0.28* 0.06* 0.00
tweenthepowerchangesandthesubjectiveratings,and
Dom. 1 0.09* 0.04*
Fam. 1 - computed the p-values for the left- (positive) and right-
Order 1 tailed (negative) correlation tests. This was done for
eachparticipantseparatelyand,assumingindependence
[39], the 32 resulting p-values per correlation direction
(positive/negative), frequency band and electrode were
averagereferenced,down-sampled to 256Hz, and high-
then combined to one p-value via Fisher’s method [40].
pass filtered with a 2 Hz cutoff-frequency using the
Fig. 8 shows the (average) correlations with signifi-
EEGlab6 toolbox. We removedeye artefactswith a blind
cantly(p<.05)correlatingelectrodeshighlighted.Below
source separation technique7. Then, the signals from
we will report and discuss only those effects that were
the last 30 seconds of each trial (video) were extracted
significant with p < .01. A comprehensive list of the
for further analysis. To correct for stimulus-unrelated
effects can be found in Table 4.
variations in power over time, the EEG signal from the
For arousal we found negative correlations in the
theta, alpha, and gamma band. The centralalpha power
6.http://sccn.ucsd.edu/eeglab/
7.http://www.cs.tut.fi/∼gomezher/projects/eeg/aar.htm decrease for higher arousal matches the findings from

| IEEETRANS.AFFECTIVECOMPUTING |     |        |     |     |     |         |     |          |     |     |     |          |     | 9   |
| ---------------------------- | --- | ------ | --- | --- | --- | ------- | --- | -------- | --- | --- | --- | -------- | --- | --- |
|                              |     | 4-7 Hz |     |     |     | 8-13 Hz |     | 14-29 Hz |     |     |     | 30-47 Hz |     |     |
Arousal
Valence
Liking
Fig.8. Themeancorrelations(overallparticipants)ofthevalence,arousal,andgeneralratingswiththepowerinthe
broad frequency bands of theta (4-7 Hz), alpha (8-13 Hz), beta (14-29 Hz) and gamma (30-47 Hz). The highlighted
sensorscorrelatesignificantly(p<.05)withtheratings.
our earlier pilot study [35] and an inverse relationship quency bands. For theta and alpha power we observed
between alpha power and the general level of arousal increases over left fronto-central cortices. Liking might
has been reported before [41], [42]. be associated with an approach motivation. However,
|               |           |             |                  |              |           |                 | the         | observation | of                 | an increase |               | of left  | alpha           | power for |
| ------------- | --------- | ----------- | ---------------- | ------------ | --------- | --------------- | ----------- | ----------- | ------------------ | ----------- | ------------- | -------- | --------------- | --------- |
| Valence       | showed    | the         | strongest        | correlations |           | with EEG        |             |             |                    |             |               |          |                 |           |
|               |           |             |                  |              |           |                 | a higher    |             | liking conflicts   |             | with findings |          | of a left       | frontal   |
| signals       | and       | correlates  | were             | found        | in all    | analysed fre-   |             |             |                    |             |               |          |                 |           |
|               |           |             |                  |              |           |                 | activation, |             | leadingtolower     |             | alphaover     |          | this region,    | often     |
| quency        | bands.    | In the      | low frequencies, |              | theta     | and alpha,      |             |             |                    |             |               |          |                 |           |
|               |           |             |                  |              |           |                 | reportedfor |             | emotions           | associated  |               | with     | approachmotiva- |           |
| an increase   | of        | valence     | led to           | an increase  |           | of power. This  |             |             |                    |             |               |          |                 |           |
|               |           |             |                  |              |           |                 | tions       | [47].       | This contradiction |             | might         | be       | reconciled      | when      |
| is consistent |           | with the    | findings         | in           | the pilot | study. The      |             |             |                    |             |               |          |                 |           |
|               |           |             |                  |              |           |                 | taking      | into        | account            | that        | it is well    | possible |                 | that some |
| location      | of these  | effectsover |                  | occipital    | regions,  | thus over       |             |             |                    |             |               |          |                 |           |
|               |           |             |                  |              |           |                 | disliked    |             | pieces induced     | an          | angry         | feeling  | (due            | to having |
| visual        | cortices, | might       | indicate         | a relative   |           | deactivation,   |             |             |                    |             |               |          |                 |           |
|               |           |             |                  |              |           |                 | to          | listen      | to them,           | or simply   | due           | to       | the content     | of the    |
| or top-down   |           | inhibition, | of               | these        | due       | to participants |             |             |                    |             |               |          |                 |           |
focusing on the pleasurable sound [43]. For the beta lyrics), which is also related to an approach motivation,
|             |           |            |              |            |           |                 | and          | might | hence result | in        | a left-ward |              | decrease   | of alpha. |
| ----------- | --------- | ---------- | ------------ | ---------- | --------- | --------------- | ------------ | ----- | ------------ | --------- | ----------- | ------------ | ---------- | --------- |
| frequency   | band      | we found   |              | a central  | decrease, | also ob-        |              |       |              |           |             |              |            |           |
|             |           |            |              |            |           |                 | The          | right | temporal     | increases |             | found        | in the     | beta and  |
| served      | in the    | pilot, and | an occipital |            | and       | right temporal  |              |       |              |           |             |              |            |           |
|             |           |            |              |            |           |                 | gamma        | bands | are          | similar   | to those    | observed     | for        | valence,  |
| increase    | of power. | Increased  |              | beta power |           | over right tem- |              |       |              |           |             |              |            |           |
|             |           |            |              |            |           |                 | and          | the   | same caution | should    | be          | applied.     | In general | the       |
| poral sites | was       | associated | with         | positive   |           | emotional self- |              |       |              |           |             |              |            |           |
|             |           |            |              |            |           |                 | distribution |       | of valence   | and       | liking      | correlations |            | shown in  |
inductionandexternalstimulationby[44].Similarly,[45]
|              |     |            |             |     |            |           | Fig. | 8 seem             | very similar, |     | which      | might     | be a result | of the |
| ------------ | --- | ---------- | ----------- | --- | ---------- | --------- | ---- | ------------------ | ------------- | --- | ---------- | --------- | ----------- | ------ |
| has reported |     | a positive | correlation |     | of valence | and high- |      |                    |               |     |            |           |             |        |
|              |     |            |             |     |            |           | high | inter-correlations |               | of  | the scales | discussed |             | above. |
frequencypower,includingbetaandgammabands,em-
| anating     | from       | anterior     | temporal | cerebral         |     | sources. Corre- |               |           |            |       |              |           |              |        |
| ----------- | ---------- | ------------ | -------- | ---------------- | --- | --------------- | ------------- | --------- | ---------- | ----- | ------------ | --------- | ------------ | ------ |
|             |            |              |          |                  |     |                 | Summarising,  |           | we         | can   | state that   | the       | correlations | ob-    |
| spondingly, | we         | observed     | a highly | significant      |     | increase of     |               |           |            |       |              |           |              |        |
|             |            |              |          |                  |     |                 | served        | partially | concur     | with  | observations |           | made         | in the |
| left and    | especially | right        | temporal | gamma            |     | power. How-     |               |           |            |       |              |           |              |        |
|             |            |              |          |                  |     |                 | pilot         | study     | and in     | other | studies      | exploring | the          | neuro- |
| ever, it    | should     | be mentioned |          | that EMG(muscle) |     | activity        |               |           |            |       |              |           |              |        |
|             |            |              |          |                  |     |                 | physiological |           | correlates | of    | affective    | states.   | They         | might  |
isalsoprominentinthehighfrequencies,especiallyover
thereforebetakenasvalidindicatorsofemotionalstates
| anterior | and | temporal | electrodes | [46]. |     |     |                                              |     |     |     |     |     |     |      |
| -------- | --- | -------- | ---------- | ----- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- |
|          |     |          |            |       |     |     | inthecontextofmulti-modalmusicalstimulation. |     |     |     |     |     |     | How- |
The liking correlates were found in all analysed fre- ever,the meancorrelationsareseldombiggerthan±0.1,

| IEEETRANS.AFFECTIVECOMPUTING |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 10  |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
which might be due to high inter-participant variability where F is the set of features and C the classes.
in terms of brain activations, as individual correlations p(Fi = fi|C = c) is estimated by assuming Gaussian
between ±0.5 were observed for a given scale correla- distributions of the features and modeling these from
tion at the same electrode/frequency combination. The the training set.
presenceofthishighinter-participantvariabilityjustifies The following section explains the feature extraction
a participant-specific classification approach, as we em- steps for the EEG and peripheral physiological signals.
ploy it, rather than a single classifier for all participants. Section 6.2 presents the features used in MCA classifi-
|     |     |     |     |     |     |     |     | cation. | In section | 6.3 | we explain |     | the method |     | used for |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | ---------- | --- | ---------- | --- | -------- |
6 SINGLE
TRIAL CLASSIFICATION decisionfusionoftheresults.Finally,section6.4presents
|           |              |     |                |                          |             |     |        | the classification                        |     | results. |     |     |     |     |     |
| --------- | ------------ | --- | -------------- | ------------------------ | ----------- | --- | ------ | ----------------------------------------- | --- | -------- | --- | --- | --- | --- | --- |
| In this   | section      | we  | present        | the methodology          |             | and | re-    |                                           |     |          |     |     |     |     |     |
| sults of  | single-trial |     | classification | of                       | the videos. |     | Three  |                                           |     |          |     |     |     |     |     |
|           |              |     |                |                          |             |     |        | 6.1 EEGandperipheralphysiologicalfeatures |     |          |     |     |     |     |     |
| different | modalities   |     | were           | used for classification, |             |     | namely |                                           |     |          |     |     |     |     |     |
EEG signals, peripheralphysiological signals and MCA. Most of the current theories of emotion [48], [49] agree
Conditions for all modalities were kept equal and only thatphysiological activityis animportant component of
|             |            |     |      |         |     |     |     | an emotion. | For | instance | several |     | studies | have | demon- |
| ----------- | ---------- | --- | ---- | ------- | --- | --- | --- | ----------- | --- | -------- | ------- | --- | ------- | ---- | ------ |
| the feature | extraction |     | step | varies. |     |     |     |             |     |          |         |     |         |      |        |
Three different binary classification problems were strated the existence of specific physiological patterns
posed: the classification of low/high arousal, low/high associated with basic emotions [6].
Thefollowingperipheralnervoussystemsignalswere
| valence | and | low/high | liking. | To this | end, | the | partici- |     |     |     |     |     |     |     |     |
| ------- | --- | -------- | ------- | ------- | ---- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
pants’ ratings during the experiment are used as the recorded: GSR, respiration amplitude, skin temperature,
|        |        |     |         |          |          |        |     | electrocardiogram, |     | blood | volume |     | by plethysmograph, |     |     |
| ------ | ------ | --- | ------- | -------- | -------- | ------ | --- | ------------------ | --- | ----- | ------ | --- | ------------------ | --- | --- |
| ground | truth. | The | ratings | for each | of these | scales | are |                    |     |       |        |     |                    |     |     |
thresholded into two classes (low and high). On the 9- electromyograms of Zygomaticus and Trapezius mus-
point rating scales, the threshold was simply placed in cles, and electrooculogram (EOG). GSR provides a mea-
sureoftheresistanceoftheskinbypositioningtwoelec-
| the middle. | Note | that | for | some subjects | and | scales, | this |     |     |     |     |     |     |     |     |
| ----------- | ---- | ---- | --- | ------------- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
leads to unbalanced classes. To give an indication of trodes on the distal phalanges of the middle and index
|                |     |     |         |          |      |              |     | fingers. | This resistance |     | decreases |     | due to | an increase | of  |
| -------------- | --- | --- | ------- | -------- | ---- | ------------ | --- | -------- | --------------- | --- | --------- | --- | ------ | ----------- | --- |
| how unbalanced |     | the | classes | are, the | mean | and standard |     |          |                 |     |           |     |        |             |     |
deviation (over participants) of the percentageof videos perspiration, which usually occurs when one is experi-
belonging to the high class per rating scale are: arousal encing emotions such as stress or surprise. Moreover,
|           |         |         |     |            |           |     |     | Lang et | al. discovered |     | that | the mean | value | of  | the GSR |
| --------- | ------- | ------- | --- | ---------- | --------- | --- | --- | ------- | -------------- | --- | ---- | -------- | ----- | --- | ------- |
| 59%(15%), | valence | 57%(9%) |     | and liking | 67%(12%). |     |     |         |                |     |      |          |       |     |         |
Inlightofthisissue,inordertoreliablyreportresults, is related to the level of arousal [20].
we report the F1-score, which is commonly employed A plethysmograph measures blood volume in the
|                |     |           |     |           |           |     |         | participant’sthumb. |     | This | measurementcanalsobeused |     |     |     |     |
| -------------- | --- | --------- | --- | --------- | --------- | --- | ------- | ------------------- | --- | ---- | ------------------------ | --- | --- | --- | --- |
| in information |     | retrieval |     | and takes | the class |     | balance |                     |     |      |                          |     |     |     |     |
into account, contrary to the mere classification rate. to compute the heart rate (HR) by identification of local
|              |     |        |          |       |             |     |        | maxima | (i.e. | heart beats), | inter-beat |     | periods, | and | heart |
| ------------ | --- | ------ | -------- | ----- | ----------- | --- | ------ | ------ | ----- | ------------- | ---------- | --- | -------- | --- | ----- |
| In addition, |     | we use | a na¨ıve | Bayes | classifier, | a   | simple |        |       |               |            |     |          |     |       |
and generalizable classifier which is able to deal with ratevariability(HRV).BloodpressureandHRVcorrelate
unbalanced classes in small training sets. with emotions, since stress can increase blood pressure.
|        |                 |     |     |                |     |              |     | Pleasantness |     | of stimuli | can | increase | peak | heart | rate |
| ------ | --------------- | --- | --- | -------------- | --- | ------------ | --- | ------------ | --- | ---------- | --- | -------- | ---- | ----- | ---- |
| First, | the featuresfor |     | the | given modality |     | areextracted |     |              |     |            |     |          |      |       |      |
for each trial (video). Then, for each participant, the response [20]. In addition to the HR and HRV features,
F1 measure was used to evaluate the performance of spectral features derived from HRV were shown to be a
emotionclassificationinaleave-one-outcrossvalidation useful feature in emotion assessment [50].
scheme. At each step of the cross validation, one video Skin temperature and respiration were recorded since
theyvarieswithdifferentemotionalstates.Slowrespira-
| was used | as  | the test-set |     | and the | rest were | used | as  |     |     |     |     |     |     |     |     |
| -------- | --- | ------------ | --- | ------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
training-set. We use Fisher’s linear discriminant J for tionislinkedtorelaxationwhileirregularrhythm,quick
feature selection: variations, and cessation of respiration correspond to
|     |     |     |     |     |     |     |     | more aroused |     | emotions | like | anger | or fear. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | ---- | ----- | -------- | --- | --- |
|µ1−µ2|
|     |     |     |       |         |     |     |     | Regarding                                          |     | the EMG | signals, | the | Trapezius |     | muscle |
| --- | --- | --- | ----- | ------- | --- | --- | --- | -------------------------------------------------- | --- | ------- | -------- | --- | --------- | --- | ------ |
|     |     |     | J(f)= |         |     |     | (2) |                                                    |     |         |          |     |           |     |        |
|     |     |     |       | σ 2+σ 2 |     |     |     | (neck)activitywasrecordedtoinvestigatepossiblehead |     |         |          |     |           |     |        |
|     |     |     |       | 1 2     |     |     |     |                                                    |     |         |          |     |           |     |        |
where µ and σ are the mean and standard deviation movements during music listening. The activity of the
for feature f. We calculate this criterion for each feature Zygomaticus major was also monitored, since this mus-
|          |       |     |           |           |     |           |     | cle is activated |     | when | the participant |     | laughs | or  | smiles. |
| -------- | ----- | --- | --------- | --------- | --- | --------- | --- | ---------------- | --- | ---- | --------------- | --- | ------ | --- | ------- |
| and then | apply | a   | threshold | to select | the | maximally |     |                  |     |      |                 |     |        |     |         |
discriminating ones. This threshold was empirically de- Most of the power in the spectrum of an EMG during
musclecontractionisinthefrequencyrangebetween4to
| termined | at 0.3. |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
A Gaussian na¨ıve Bayesclassifier was used to classify 40 Hz. Thus, the muscle activity features were obtained
the test-set as low/high arousal, valence or liking. from the energy of EMG signals in this frequency range
|     |     |     |     |     |     |     |     | for the | different | muscles. | The | rate | of eye | blinking | is  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | -------- | --- | ---- | ------ | -------- | --- |
The na¨ıveBayesclassifierGassumesindependenceof
the features and is given by: another feature, which is correlated with anxiety. Eye-
|     |     |     |     |     |     |     |     | blinking | affects | the | EOG signal |     | and results | in  | easily |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | --- | ---------- | --- | ----------- | --- | ------ |
n
G(f1,..,fn)=argmaxp(C =c) p(Fi =fi|C =c) (3) detectable peaks in that signal. For further reading on
|     |     | c   |     |     |     |     |     | psychophysiologyofemotion,wereferthereaderto[51]. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
i=1
Y

| IEEETRANS.AFFECTIVECOMPUTING |     |     |        |     |     |     |     |     |                 |     |     |     |     |     | 11  |
| ---------------------------- | --- | --- | ------ | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
|                              |     |     | TABLE5 |     |     |     |     |     | 6.2 MCAFeatures |     |     |     |     |     |     |
FeaturesextractedfromEEGandphysiologicalsignals.
|        |           |     |          |     |     |     |     |     | Music videos   | were encoded     |              | into the | MPEG-1    |         | format to |
| ------ | --------- | --- | -------- | --- | --- | --- | --- | --- | -------------- | ---------------- | ------------ | -------- | --------- | ------- | --------- |
|        |           |     |          |     |     |     |     |     | extract motion | vectors          | and I-frames |          | for       | further | feature   |
|        |           |     |          |     |     |     |     |     | extraction.    | The video        | stream       | has been | segmented |         | at the    |
| Signal | Extracted |     | features |     |     |     |     |     |                |                  |              |          |           |         |           |
|        |           |     |          |     |     |     |     |     | shot level     | using the method |              | proposed | in        | [55].   |           |
GSR average skin resistance, average of derivative, average From a movie director’s point of view, lighting key
ofderivativefornegativevaluesonly(averagedecrease
rateduringdecaytime),proportionofnegativesamples [30], [56] and color variance [30] are important tools
inthederivativevs.allsamples,numberoflocalminima to evoke emotions. We therefore extracted lighting key
in the GSR signal, average rising time of the GSR from frames in the HSV space by multiplying the aver-
|     | signal, | 10  | spectral | power | in the | [0-2.4]Hz | bands, | zero |           |            |        |          |     |           |        |
| --- | ------- | --- | -------- | ----- | ------ | --------- | ------ | ---- | --------- | ---------- | ------ | -------- | --- | --------- | ------ |
|     |         |     |          |       |        |           |        |      | age value | V (in HSV) | by the | standard |     | deviation | of the |
crossingrateofSkinconductanceslowresponse(SCSR)
[0-0.2]Hz, zero crossing rate of Skin conductance very values V (in HSV). Color variance was obtained in the
|     | slow | response | (SCVSR) |     | [0-0.08]Hz, | SCSR | and SCVSR |     |         |             |              |     |     |             |     |
| --- | ---- | -------- | ------- | --- | ----------- | ---- | --------- | --- | ------- | ----------- | ------------ | --- | --- | ----------- | --- |
|     |      |          |         |     |             |      |           |     | CIE LUV | color space | by computing |     | the | determinant | of  |
meanofpeaksmagnitude
|       |                                              |     |     |     |     |     |     |     | the covariance | matrix | of L, U, | and | V.  |     |     |
| ----- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------ | -------- | --- | --- | --- | --- |
| Blood | AverageandstandarddeviationofHR,HRV,andinter |     |     |     |     |     |     |     |                |        |          |     |     |     |     |
HanjalicandXu[29]showedtherelationshipbetween
| volume | beatintervals,energyratiobetweenthefrequencybands |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------ | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
pressure [0.04-0.15]Hz and [0.15-0.5]Hz, spectral power in the video rhythm and affect. The average shot change rate,
bands ([0.1-0.2]Hz, [0.2-0.3]Hz, [0.3-0.4]Hz), low fre- and shot length variance were extracted to characterize
|     | quency | [0.01-0.08]Hz, |     | medium | frequency |     | [0.08-0.15]Hz |     |     |     |     |     |     |     |     |
| --- | ------ | -------------- | --- | ------ | --------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
and high frequency [0.15-0.5]Hz components of HRV videorhythm.Fastmovingscenesorobjects’movements
powerspectrum. in consecutive frames are also an effective factor for
Respiration bandenergyratio(differencebetweenthelogarithmof evoking excitement. To measure this factor, the motion
| pattern | energybetweenthelower(0.05-0.25Hz)andthehigher |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
componentwasdefinedastheamountofmotionincon-
|     | (0.25-5Hz) |     | bands), | average | respiration | signal, | mean | of  |          |                 |     |              |     |            |     |
| --- | ---------- | --- | ------- | ------- | ----------- | ------- | ---- | --- | -------- | --------------- | --- | ------------ | --- | ---------- | --- |
|     |            |     |         |         |             |         |      |     | secutive | frames computed | by  | accumulating |     | magnitudes |     |
derivative(variationoftherespirationsignal),standard
deviation, range or greatest breath, breathing rhythm of motion vectors for all B- and P-frames.
(spectralcentroid),breathingrate,10spectralpowerin
Colorsandtheirproportionsareimportantparameters
thebandsfrom0to2.4Hz,averagepeaktopeaktime,
|     |     |     |     |     |     |     |     |     | to elicit emotions | [57]. | A 20 | bin color | histogram |     | of hue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | ----- | ---- | --------- | --------- | --- | ------ |
medianpeaktopeaktime
Skin tem- average,averageofitsderivative,spectralpowerinthe andlightnessvaluesintheHSVspacewascomputedfor
perature bands([0-0.1]Hz,[0.1-0.2]Hz) eachI-frameandsubsequentlyaveragedoverallframes.
| EMG and | eyeblinkingrate,energyofthesignal,meanandvari- |     |     |     |     |     |     |     |                 |              |      |      |         |        |          |
| ------- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------------ | ---- | ---- | ------- | ------ | -------- |
|         |                                                |     |     |     |     |     |     |     | The resulting   | bin averages | were | used | as      | video  | content- |
| EOG     | anceofthesignal                                |     |     |     |     |     |     |     |                 |              |      |      |         |        |          |
|         |                                                |     |     |     |     |     |     |     | based features. | The median   | of   | the  | L value | in HSL | space    |
EEG theta, slow alpha, alpha, beta, and gamma Spectral wascomputedtoobtainthemedianlightnessofaframe.
powerforeachelectrode.Thespectralpowerasymme-
trybetween14pairsofelectrodesinthefourbandsof Finally, visual cues representing shadow proportion,
alpha,beta,thetaandgamma. visual excitement, grayness and details were also deter-
|     |     |     |     |     |     |     |     |     | mined according | to the                | definition  |        | given      | in [30].   |           |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --------------------- | ----------- | ------ | ---------- | ---------- | --------- |
|     |     |     |     |     |     |     |     |     | Sound           | also has an important |             | impact | on         | affect.For | ex-       |
|     |     |     |     |     |     |     |     |     | ample, loudness | of speech             | (energy)    |        | is related |            | to evoked |
|     |     |     |     |     |     |     |     |     | arousal,        | while rhythm          | and average |        | pitch      | in speech  | sig-      |
nalsarerelatedtovalence[58].Theaudiochannelsofthe
| All the | physiological |      | responses |       | were         | recorded |          | at a |             |           |             |     |      |      |        |
| ------- | ------------- | ---- | --------- | ----- | ------------ | -------- | -------- | ---- | ----------- | --------- | ----------- | --- | ---- | ---- | ------ |
|         |               |      |           |       |              |          |          |      | videos were | extracted | and encoded |     | into | mono | MPEG-3 |
| 512Hz   | sampling      | rate | and       | later | down-sampled |          | to 256Hz |      |             |           |             |     |      |      |        |
toreduceprcoessingtime.ThetrendoftheECGandGSR format at a sampling rate of 44.1 kHz. All audio signals
|         |     |         |     |             |     |              |     |     | were normalized | to the | same | amplitude |     | range | before |
| ------- | --- | ------- | --- | ----------- | --- | ------------ | --- | --- | --------------- | ------ | ---- | --------- | --- | ----- | ------ |
| signals | was | removed | by  | subtracting |     | the temporal |     | low |                 |        |      |           |     |       |        |
frequency drift. The low frequency drift was computed furtherprocessing.Atotalof53low-levelaudiofeatures
bysmoothingthesignalsoneachECGandGSRchannels were determined for each of the audio signals. These
|        |            |        |     |          |     |     |     |     | features, | listed in Table | 6, are | commonly |     | used | in audio |
| ------ | ---------- | ------ | --- | -------- | --- | --- | --- | --- | --------- | --------------- | ------ | -------- | --- | ---- | -------- |
| with a | 256 points | moving |     | average. |     |     |     |     |           |                 |        |          |     |      |          |
andspeechprocessingandaudioclassification[59],[60].
| In total          | 106     | features   | were  | extracted |          | from     | peripheral |      |                                    |                 |           |     |         |         |       |
| ----------------- | ------- | ---------- | ----- | --------- | -------- | -------- | ---------- | ---- | ---------------------------------- | --------------- | --------- | --- | ------- | ------- | ----- |
|                   |         |            |       |           |          |          |            |      | MFCC, formants                     | and             | the pitch | of  | audio   | signals | were  |
| physiological     |         | responses  | based | on        | the      | proposed | features   |      |                                    |                 |           |     |         |         |       |
|                   |         |            |       |           |          |          |            |      | extracted                          | using the PRAAT | software  |     | package |         | [61]. |
| in the literature |         | [22],      | [26], | [52]–[54] | (see     | also     | Table      | 5).  |                                    |                 |           |     |         |         |       |
| From              | the EEG | signals,   |       | power     | spectral | features |            | were |                                    |                 |           |     |         |         |       |
|                   |         |            |       |           |          |          |            |      | 6.3 Fusionofsingle-modalityresults |                 |           |     |         |         |       |
| extracted.        | The     | logarithms |       | of the    | spectral |          | power      | from |                                    |                 |           |     |         |         |       |
theta(4-8Hz),slowalpha(8-10Hz),alpha(8-12Hz),beta Fusion of the multiple modalities explained above aims
(12-30Hz) and gamma (30+ Hz) bands were extracted atimprovingclassificationresultsbyexploitingthecom-
from all 32 electrodes as features. In addition to power plementarynatureofthedifferentmodalities.Ingeneral,
spectral features the difference between the spectral approaches for modality fusion can be classified into
power of all the symmetrical pairs of electrodes on two broad categories, namely, feature fusion (or early
the right and left hemisphere was extracted to measure integration)anddecisionfusion(orlateintegration)[63].
the possible asymmetry in the brain activities due to In feature fusion, the features extracted from signals of
emotional stimuli. The total number of EEG features of different modalities are concatenated to form a com-
a trial for 32 electrodes is 216. Table 5 summarizes the posite feature vector and then inputted to a recognizer.
list of features extracted from the physiological signals. In decision fusion, on the other hand, each modality

IEEETRANS.AFFECTIVECOMPUTING 12
TABLE6 TABLE7
Low-levelfeaturesextractedfromaudiosignals. Averageaccuracies(ACC)andF1-scores(F1,average
ofscoreforeachclass)overparticipants.Starsindicate
whethertheF1-scoredistribution oversubjectsis
Featurecategory Extracted features
significantlyhigherthan0.5accordingtoanindependent
MFCC MFCC coefficients (13 features) [59], Deriva- one-samplet-test(∗∗=p<.01,∗=p<.05).For
tiveofMFCC(13features),Autocorrelationof comparison,expectedresultsaregivenforclassification
MFCC(13features)
basedonrandomvoting,votingaccordingtothemajority
Energy Averageenergyofaudiosignal[59]
classandvotingwiththeratiooftheclasses.
Formants Formants up to 5500Hz (female voice) (five
features)
Time frequency MSpectrumflux,Spectralcentroid,Deltaspec- Arousal Valence Liking
trummagnitude,Bandenergyratio[59],[60]
Modality ACC F1 ACC F1 ACC F1
Pitch Firstpitchfrequency
Zerocrossingrate Average,Standarddeviation[59] EEG 0.620 0.583** 0.576 0.563** 0.554 0.502
Peripheral 0.570 0.533* 0.627 0.608** 0.591 0.538**
Silenceratio Proportionofsilenceinatimewindow[62]
MCA 0.651 0.618** 0.618 0.605** 0.677 0.634**
Random 0.500 0.483 0.500 0.494 0.500 0.476
Majority class 0.644 0.389 0.586 0.368 0.670 0.398
Class ratio 0.562 0.500 0.525 0.500 0.586 0.500
is processed independently by the corresponding clas-
sifier and the outputs of the classifiers are combined
to yield the final result. Each approach has its own
advantages.Forexample,implementingafeaturefusion- each modality and each rating scale. We compare the
basedsystemisstraightforward,whileadecisionfusion- results to the expected values (analytically determined)
based system can be constructed by using existing uni- of voting randomly, voting according to the majority
modal classification systems. Moreover, feature fusion class in the training data, and voting for each class
canconsidersynchronous characteristicsofthe involved with the probability of its occurrence in the training
modalities, whereas decision fusion allows us to model data. For determining the expected values of majority
asynchronous characteristics of the modalities flexibly. voting and class ratio voting, we used the class ratio of
An important advantage of decision fusion over fea- eachparticipant’sfeedbackduringtheexperiment.These
turefusionisthat,sinceeachofthesignalsareprocessed results are slightly too high, as in reality the class ratio
and classified independently in decision fusion, it is wouldhavetobeestimatedfromthetrainingsetineach
relatively easy to employ an optimal weighting scheme fold of the leave-one-out cross-validation.
to adjust the relative amount of the contribution of each Voting according to the class ratio gives an expected
modality to the final decisionaccordingtothe reliability F1-score of 0.5 for each participant. To test for signifi-
ofthemodality.Theweightingschemeusedinourwork cance,anindependentone-samplet-testwasperformed,
can be formalized as follows: For a given test datum X, comparing the F1-distribution over participants to the
the classification result of the fusion system is 0.5 baseline. As can be seen from the table, 8 out of
the 9 obtained F1-scores are significantly better than the
M
c
∗
=argmax Pi(X|λm)
αm
(4)
class ratio baseline. The exception is the classification
i of liking using EEG signals (p = 0.068). When voting
(m=1 )
Y accordingtothemajorityclass,relativelyhighaccuracies
where M is the number of modalities considered for
are achieved, due to the imbalanced classes. However,
fusion, λm is the classifier for the m-th modality, and
this voting scheme also has the lowest F1-scores.
Pi(X|λm) is its output for the i-th class. The weighting
M Overall, classification using the MCA features fares
factorsαm,which satisfy0≤αm ≤1and
m=1
αm =1,
significantly better than EEG and peripheral (p<0.0001
determine how much each modality contributes to the
for both), while EEG and peripheral scores are not sig-
P
final decision and represent the modality’s reliability.
nificantly different (p = 0.41) (tested using a two-sided
We adopt a simple method where the weighting fac-
repeated samples t-test over the concatenated results
tors are fixed once their optimal values are determined
from each rating scale and participant).
from the training data. The optimal weight values are
The modalities can be seen to perform moderately
estimated by exhaustively searching the regular grid
complementary, where EEG scores best for arousal, pe-
space, where each weight is incremented from 0 to 1
ripheralforvalenceandMCAforliking.Ofthedifferent
by 0.01 and the weighting values producing the best
rating scales, valence classification performed best, fol-
classification results for the training data are selected.
lowed by liking and lastly arousal.
Table 8 gives the results of multi-modal fusion. Two
6.4 ResultsandDiscussion
fusionmethodswereemployed;themethoddescribedin
Table 7 shows the average accuracies and F1-scores section 6.3 and the basic method where each modality
(average F1-score for both classes) over participants for isweighed equally.Thebestresultswereobtainedwhen

| IEEETRANS.AFFECTIVECOMPUTING |     |     |     |     |     |     |     |     |     |     |     |     |     | 13  |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TABLE8
F1-scoresforfusionofthebesttwomodalities andallthreemodalities usingtheequalweightsandoptimalweights
scheme.Forcomparison,theF1-scoreforthebestsinglemodalityisalsogiven.
|     |     |     |     | Arousal |     |     |     | Valence |     |     |     |     | Liking |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | ------- | --- | --- | --- | --- | ------ | --- |
Modality Optimalw. Equalw. Modality Optimalw. Equalw. Modality Optimalw. Equalw.
| Bestsinglemodality |     | MCA |     | 0.618 |     | —–  | PER | 0.608 |     | —–  |     | MCA | 0.634 | —–  |
| ------------------ | --- | --- | --- | ----- | --- | --- | --- | ----- | --- | --- | --- | --- | ----- | --- |
Besttwomodalities EEG,MCA 0.631 0.629 MCA,PER 0.638 0.652 MCA,PER 0.622 0.642
Allthreemodalities All 0.616 0.618 All 0.647 0.640 All 0.618 0.607
only the two best-performing modalities were consid- Multimodal Information Management (IM2). The au-
ered. Though fusion generally outperforms the single thors also thank Sebastian Schmiedeke and Pascal Kelm
modalities,itisonlysignificantforthecaseofMCA,PER at the Technische Universita¨t Berlin for performing the
weighted equally in the valence scale (p=0.025). shot boundary detection on this dataset.
| While       | the presented |                 | results | are   | significantly |      | higher |     |     |     |     |     |     |     |
| ----------- | ------------- | --------------- | ------- | ----- | ------------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
| than random |               | classification, |         | there | remains       | much | room   |     |     |     |     |     |     |     |
REFERENCES
| for improvement. |     | Signal  | noise,  | individual          |     | physiological |      |                                                           |     |     |     |     |     |     |
| ---------------- | --- | ------- | ------- | ------------------- | --- | ------------- | ---- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| differencesand   |     | limited | quality | of self-assessments |     |               | make |                                                           |     |     |     |     |     |     |
|                  |     |         |         |                     |     |               |      | [1] M.K.Shan,F.F.Kuo,M.F.Chiang,andS.Y.Lee,“Emotion-based |     |     |     |     |     |     |
single-trial classification challenging. music recommendation by affinity discovery from film music,”
|     |     |     |     |     |     |     |     | ExpertSyst.Appl.,vol.36,no.4,pp.7666–7674, |     |     |     |     | September2009. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | -------------- | --- |
7 CONCLUSION [2] M.Tkalcˇicˇ,U.Burnik,andA.Kosˇir,“Usingaffectiveparametersin
acontent-basedrecommendersystemforimages,”UserModeling
andUser-AdaptedInteraction,pp.1–33–33,September2010.
| In this  | work,          | we have | presented |     | a database |          | for the |                                                           |            |     |             |     |            |                  |
| -------- | -------------- | ------- | --------- | --- | ---------- | -------- | ------- | --------------------------------------------------------- | ---------- | --- | ----------- | --- | ---------- | ---------------- |
|          |                |         |           |     |            |          |         | [3] J.J.M.Kierkels,M.Soleymani,andT.Pun,“Queriesandtagsin |            |     |             |     |            |                  |
| analysis | of spontaneous |         | emotions. |     | The        | database | con-    |                                                           |            |     |             |     |            |                  |
|          |                |         |           |     |            |          |         | affect-based                                              | multimedia |     | retrieval,” | in  | Proc. Int. | Conf. Multimedia |
tainsphysiologicalsignalsof32participants(andfrontal
|     |     |     |     |     |     |     |     | andExpo. | NewYork,NY,USA:IEEEPress,2009,pp.1436–1439. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------------------------------------- | --- | --- | --- | --- | --- |
face video of 22 participants), where each participant [4] M. Soleymani, J. Lichtenauer, T. Pun, and M. Pantic, “A multi-
modalAffectiveDatabaseforAffectRecognitionandImplicitTag-
| watched | and | rated their | emotional |     | response | to  | 40 mu- |     |     |     |     |     |     |     |
| ------- | --- | ----------- | --------- | --- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
ging,”IEEETrans.AffectiveComputing,SpecialIssueonNaturalistic
sic videos along the scales of arousal, valence, and AffectResourcesforSystemBuildingandEvaluation, underreview.
dominance, as well as their liking of and familiarity [5] A.Savran,K.Ciftci,G.Chanel,J.C.Mota,L.H.Viet,B.Sankur,
with the videos. We presented a novel semi-automatic L.Akarun,A.Caplier,andM.Rombaut,“Emotiondetectioninthe
|     |     |     |     |     |     |     |     | loop from | brainsignals |     | andfacial | images,”inProc.eNTERFACE |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | --------- | ------------------------ | --- | --- |
stimuli selectionmethod usingaffectivetags,whichwas 2006Workshop,Dubrovnik,Croatia,Jul.2006.
validated by an analysis of the ratings participants gave [6] P. Ekman,W. V. Friesen, M. O’Sullivan, A. Chan, I. Diacoyanni-
|     |     |     |     |     |     |     |     | Tarlatzis, | K. Heider, |     | R. Krause, | W.  | A. LeCompte, | T. Pitcairn, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | ---------- | --- | ------------ | ------------ |
duringtheexperiment.Significantcorrelateswerefound
|     |     |     |     |     |     |     |     | and P. | E. Ricci-Bitti, |     | “Universals | and | cultural differences | in the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------------- | --- | ----------- | --- | -------------------- | ------ |
between the participant ratings and EEG frequencies. judgmentsoffacialexpressionsofemotion.”JournalofPersonality
Single-trialclassificationwasperformedfor the scalesof andSocialPsychology, vol.53,no.4,pp.712–717,Oct.1987.
|     |     |     |     |     |     |     |     | [7] W. G. | Parrott, | Emotions | in  | Social Psychology: | Essential | Readings. |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | -------- | --- | ------------------ | --------- | --------- |
arousal,valenceandlikingusingfeaturesextractedfrom
Philadelphia:PsychologyPress,2001.
| the EEG,   | peripheral |                  | and MCA | modalities. |      | The    | results |                                                                |     |     |     |     |     |     |
| ---------- | ---------- | ---------------- | ------- | ----------- | ---- | ------ | ------- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|            |            |                  |         |             |      |        |         | [8] R.Plutchik,“Thenatureofemotions,”AmericanScientist,vol.89, |     |     |     |     |     |     |
| were shown | to         | be significantly |         | better      | than | random | clas-   |                                                                |     |     |     |     |     |     |
p.344,2001.
|     |     |     |     |     |     |     |     | [9] J.A.Russell,“Acircumplexmodelofaffect,”JournalofPersonality |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
sification.Finally,decisionfusionoftheseresultsyielded
|                    |     |     |                                   |     |     |     |     | andSocialPsychology, |         |     | vol.39,no.6,pp.1161–1178,1980. |            |          |           |
| ------------------ | --- | --- | --------------------------------- | --- | --- | --- | --- | -------------------- | ------- | --- | ------------------------------ | ---------- | -------- | --------- |
| a modestincreasein |     |     | the performance,indicatingatleast |     |     |     |     |                      |         |     |                                |            |          |           |
|                    |     |     |                                   |     |     |     |     | [10] M. M.           | Bradley | and | P. J. Lang,                    | “Measuring | emotion: | the self- |
some complementarity to the modalities. assessmentmanikinandthesemanticdifferential.”J.Behav.Ther.
The database is made publicly available and it is our Exp.Psychiatry,vol.25,no.1,pp.49–59,Mar.1994.
|           |       |             |     |          |       |         |     | [11] M. Pantic,   | M.  | Valstar,   | R. Rademaker, |                            | and L. Maat, | “Web-based |
| --------- | ----- | ----------- | --- | -------- | ----- | ------- | --- | ----------------- | --- | ---------- | ------------- | -------------------------- | ------------ | ---------- |
| hope that | other | researchers |     | will try | their | methods | and |                   |     |            |               |                            |              |            |
|           |       |             |     |          |       |         |     | databaseforfacial |     | expression |               | analysis,”inProc.Int.Conf. |              | Multi-     |
algorithms on this highly challenging database. mediaandExpo,Amsterdam,TheNetherlands,2005,pp.317–321.
|     |     |     |     |     |     |     |     | [12] E.Douglas-Cowie, |     | R.  | Cowie, | andM.Schro¨der,“Anewemotion |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | ------ | --------------------------- | --- | --- |
ACKNOWLEDGMENTS database:Considerations,sourcesandscope,”inProc.ISCAWork-
shoponSpeechandEmotion,2000,pp.39–44.
|     |     |     |     |     |     |     |     | [13] H. Gunes | and | M. Piccardi, |     | “A bimodal | face and | body gesture |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------ | --- | ---------- | -------- | ------------ |
Theresearchleadingtotheseresultshasbeenperformed
|                                                 |     |     |          |             |     |     |         | database     | for | automatic      | analysis | of human             | nonverbal | affective        |
| ----------------------------------------------- | --- | --- | -------- | ----------- | --- | --- | ------- | ------------ | --- | -------------- | -------- | -------------------- | --------- | ---------------- |
| in the frameworks                               |     | of  | European | Community’s |     |     | Seventh |              |     |                |          |                      |           |                  |
|                                                 |     |     |          |             |     |     |         | behavior,”in |     | Proc.Int.Conf. |          | Pattern Recognition, |           | vol. 1,2006, pp. |
| FrameworkProgram(FP7/2007-2011)undergrantagree- |     |     |          |             |     |     |         | 1148–1153.   |     |                |          |                      |           |                  |
ment no. 216444 (PetaMedia). Furthermore, the authors [14] G.Fanelli,J.Gall,H.Romsdorfer,T.Weise,andL.VanGool,“A
3-Daudio-visualcorpusofaffectivecommunication,”IEEETrans.
| gratefully | acknowledge |     | the | support | of  | the BrainGain |     |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | --- | ------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Multimedia,vol.12,no.6,pp.591–598,Oct.2010.
Smart Mix Programme of the Netherlands Ministry of [15] M.Grimm,K.Kroschel,andS.Narayanan,“Theveraammittag
Economic Affairs, the Netherlands Ministry of Educa- german audio-visual emotional speech database,” in Proc. Int.
Conf.MultimediaandExpo,2008,pp.865–868.
tion, Culture and Science and the Swiss National Foun- [16] J.A.Healey,“Wearableandautomotivesystemsforaffectrecog-
dation for Scientific Research and the NCCR Interactive nitionfromphysiology,”Ph.D.dissertation,MIT,2000.

| IEEETRANS.AFFECTIVECOMPUTING |     |     |     |     |     |     |     |     |     |     |     |     |     | 14  |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[17] J. A. Healey and R. W. Picard, “Detecting stress during real- [39] Lazar,N.,“CombiningBrains:ASurveyofMethodsforStatistical
world driving tasks using physiological sensors,” IEEE Trans. Pooling ofInformation,” NeuroImage,vol. 16, no.2, pp.538–550,
| Intell.Transp.Syst.,vol.6,no.2,pp.156–166,2005. |     |     |     |     |     |     | June2002. |     |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
[18] P.Lang,M.Bradley,andB.Cuthbert,“Internationalaffectivepic- [40] T. M. Loughin, “A systematic comparison of methods for com-
ture system (IAPS): Affective ratings of pictures and instruction bining p-valuesfrom independenttests,”Computational Statistics
manual,”UniversityofFlorida,USA,Tech.Rep.A-8,2008. &DataAnalysis,vol.47,pp.467–485,2004.
[19] Z. Zeng, M. Pantic, G. I. Roisman, and T. S. Huang, “A survey [41] R. J. Barry, A. R. Clarke, S. J. Johnstone, C. A. Magee, and J. A.
|           |             |     |          |        |         |                 | Rushby, | “EEG | differences | between | eyes-closed |     | and eyes-open |     |
| --------- | ----------- | --- | -------- | ------ | ------- | --------------- | ------- | ---- | ----------- | ------- | ----------- | --- | ------------- | --- |
| of affect | recognition |     | methods: | Audio, | visual, | and spontaneous |         |      |             |         |             |     |               |     |
expressions,”IEEETrans.PatternAnal.Mach.Intell.,vol.31,no.1, resting conditions,”Clinical Neurophysiology, vol.118, no.12, pp.
| pp.39–58,Mar.2009. |     |     |     |     |     |     | 2765–2773, | Dec.2007. |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | --- | --- | --- | --- | --- |
[20] P. Lang, M. Greenwald, M. Bradely, and A. Hamm, “Looking [42] R.J.Barry,A.R.Clarke, S.J.Johnstone,andC.R.Brown,“EEG
at pictures - affective, facial, visceral, and behavioral reactions,” differencesinchildrenbetweeneyes-closedandeyes-openresting
|                   |     |                                 |     |     |     |     | conditions,” |     | Clinical | Neurophysiology, | vol. | 120, no. | 10, pp. | 1806– |
| ----------------- | --- | ------------------------------- | --- | --- | --- | --- | ------------ | --- | -------- | ---------------- | ---- | -------- | ------- | ----- |
| Psychophysiology, |     | vol.30,no.3,pp.261–273,May1993. |     |     |     |     |              |     |          |                  |      |          |         |       |
1811,Oct.2009.
[21] J.KimandE.Andre´,“Emotionrecognitionbasedonphysiological
changesinmusiclistening,”IEEETrans.PatternAnal.Mach.Intell., [43] W. Klimesch, P. Sauseng, and S. Hanslmayr, “EEG alpha oscil-
vol.30,no.12,pp.2067–2083, 2008. lations:theinhibition-timinghypothesis.”BrainResearchReviews,
[22] J.WangandY.Gong,“Recognitionofmultipledrivers’emotional vol.53,no.1,pp.63–88,Jan.2007.
[44] H.ColeandW.J.Ray,“EEGcorrelatesofemotionaltasksrelated
| state,”inProc.Int.Conf.PatternRecognition, |             |           |        |             | 2008,pp.1–4. |               |                                     |     |     |     |         |     |                   |     |
| ------------------------------------------ | ----------- | --------- | ------ | ----------- | ------------ | ------------- | ----------------------------------- | --- | --- | --- | ------- | --- | ----------------- | --- |
|                                            |             |           |        |             |              |               | toattentionaldemands,”International |     |     |     | Journal | of  | Psychophysiology, |     |
| [23] C. L.                                 | Lisetti and | F. Nasoz, | “Using | noninvasive |              | wearable com- |                                     |     |     |     |         |     |                   |     |
puterstorecognizehumanemotionsfromphysiologicalsignals,” vol.3,no.1,pp.33–41,Jul.1985.
EURASIPJ. Appl. Signal Process.,vol. 2004, no. 1, pp.1672–1687, [45] J.OntonandS.Makeig,“High-frequencybroadbandmodulations
Jan.2004. of electroencephalographic spectra,” Frontiers in Human Neuro-
science,vol.3,2009.
| [24] G. Chanel, | J.  | Kierkels, | M. Soleymani, |     | and T. | Pun, “Short-term |     |     |     |     |     |     |     |     |
| --------------- | --- | --------- | ------------- | --- | ------ | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
[46] I.Goncharova,D.J.McFarland,J.R.Vaughan,andJ.R.Wolpaw,
emotionassessmentinarecallparadigm,”InternationalJournalof
“EMGcontaminationofEEG:spectralandtopographicalcharac-
Human-ComputerStudies,vol.67,no.8,pp.607–627,Aug.2009.
[25] J.Kierkels,M.Soleymani,andT.Pun,“Queriesandtagsinaffect- teristics,” Clinical Neurophysiology, vol.114, no.9, pp. 1580–1593,
| based | multimedia | retrieval,” | in  | Proc. | Int. Conf. | Multimedia and | Sep.2003. |     |     |     |     |     |     |     |
| ----- | ---------- | ----------- | --- | ----- | ---------- | -------------- | --------- | --- | --- | --- | --- | --- | --- | --- |
[47] E.Harmon-Jones,“Clarifyingtheemotivefunctionsofasymmet-
Expo,SpecialSessiononImplicitTagging,NewYork,USA,Jun.2009,
|     |     |     |     |     |     |     | rical | frontalcortical | activity,”Psychophysiology, |     |     | vol.40,no.6,pp. |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --------------- | --------------------------- | --- | --- | --------------- | --- | --- |
pp.1436–1439.
|     |     |     |     |     |     |     | 838–848, | 2003. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- |
[26] M.Soleymani,G.Chanel,J.J.M.Kierkels,andT.Pun,“Affective
characterization of movie scenes based on content analysis and [48] R. R. Cornelius, The Science of Emotion. Research and Tradition in
|               |     |           |               |         |     |                  | thePsychologyofEmotion. |     |     | UpperSaddleRiver,NJ:Prentice-Hall, |     |     |     |     |
| ------------- | --- | --------- | ------------- | ------- | --- | ---------------- | ----------------------- | --- | --- | ---------------------------------- | --- | --- | --- | --- |
| physiological |     | changes,” | International | Journal | of  | Semantic Comput- |                         |     |     |                                    |     |     |     |     |
1996.
| ing,vol.3,no.2,pp.235–254, |     |     | Jun.2009. |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[49] D.Sander,D.Grandjean,andK.R.Scherer,“Asystemsapproach
[27] A.Yazdani,J.-S.Lee,andT.Ebrahimi,“Implicitemotionaltagging
|     |     |     |     |     |     |     | to appraisal |     | mechanisms | in  | emotion,” | Neural Networks, |     | vol. 18, |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------- | --- | --------- | ---------------- | --- | -------- |
ofmultimediausingEEGsignalsandbraincomputerinterface,”
inProc.SIGMMWorkshoponSocialmedia,2009,pp.81–88. no.4,pp.317–352,2005.
[50] R.McCraty,M.Atkinson,W.Tiller,G.Rein,andA.Watkins,“The
| [28] P. Ekman, | W.  | Friesen, | M. Osullivan, | A.  | Chan, | I. Diacoyannitar- |         |             |     |               |       |          |          |     |
| -------------- | --- | -------- | ------------- | --- | ----- | ----------------- | ------- | ----------- | --- | ------------- | ----- | -------- | -------- | --- |
|                |     |          |               |     |       |                   | effects | of emotions |     | on short-term | power | spectrum | analysis | of  |
latzis,K.Heider,R.Krause,W.Lecompte,T.Pitcairn,P.Riccibitti,
|     |     |     |     |     |     |     | heartratevariability,”TheAmerican |     |     |     | JournalofCardiology, |     |     | vol.76, |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | -------------------- | --- | --- | ------- |
K.Scherer,M.Tomita,andA.Tzavaras,“Universalsandcultural-
no.14,pp.1089–1093,1995.
| differences | in  | the judgments | of  | facial | expressions | of emotion,” |     |     |     |     |     |     |     |     |
| ----------- | --- | ------------- | --- | ------ | ----------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
[51] S.D.Kreibig,“Autonomicnervoussystemactivityinemotion:A
JournalofPersonalityandSocialPsychology,vol.53,no.4,pp.712– review,”Biological Psychology,vol.84,no.3,pp.394–421,2010.
717,Oct.1987.
[52] G.Chanel,J.J.M.Kierkels,M.Soleymani,andT.Pun,“Short-term
[29] A.HanjalicandL.-Q.Xu,“Affectivevideocontentrepresentation
emotionassessmentinarecallparadigm,”InternationalJournalof
andmodeling,”IEEETrans.Multimedia,vol.7,no.1,pp.143–154,
Human-ComputerStudies,vol.67,no.8,pp.607–627,Aug.2009.
2005.
[53] J.KimandE.Andre´,“Emotionrecognitionbasedonphysiological
[30] H.L.WangandL.-F.Cheong,“Affectiveunderstandinginfilm,” changesinmusiclistening,”IEEETrans.PatternAnal.Mach.Intell.,
| IEEE | Trans. Circuits | Syst. | Video | Technol., |          |                |                              |     |     |     |       |     |     |     |
| ---- | --------------- | ----- | ----- | --------- | -------- | -------------- | ---------------------------- | --- | --- | --- | ----- | --- | --- | --- |
|      |                 |       |       |           | vol. 16, | no. 6, pp. 689 | – vol.30,no.12,pp.2067–2083, |     |     |     | 2008. |     |     |     |
704,Jun.2006.
|                    |     |              |            |     |        |                  | [54] P. Rainville, |     | A. Bechara, | N.  | Naqvi, and | A. R. | Damasio, | “Basic |
| ------------------ | --- | ------------ | ---------- | --- | ------ | ---------------- | ------------------ | --- | ----------- | --- | ---------- | ----- | -------- | ------ |
| [31] M. Soleymani, |     | J. Kierkels, | G. Chanel, |     | and T. | Pun, “A Bayesian |                    |     |             |     |            |       |          |        |
emotionsareassociatedwithdistinctpatternsofcardiorespiratory
| framework | forvideoaffective |     |     | representation,”in |     | Proc. Int. Conf. |     |     |     |     |     |     |     |     |
| --------- | ----------------- | --- | --- | ------------------ | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
activity.”InternationalJournalofPsychophysiology,vol.61,no.1,pp.
| Affective | ComputingandIntelligentinteraction, |     |     |     | Sep.2009,pp.1–7. |     | 5–18,Jul.2006. |     |     |     |     |     |     |     |
| --------- | ----------------------------------- | --- | --- | --- | ---------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
[32] D.Liu,“Automaticmooddetectionfromacousticmusicdata,”in [55] P.Kelm,S.Schmiedeke,andT.Sikora,“Feature-basedvideokey
| Proc.Int.Conf.MusicInformation |              |     |                                  | Retrieval,2003,pp.13–17. |     |     |       |            |     |             |       |             |          |      |
| ------------------------------ | ------------ | --- | -------------------------------- | ------------------------ | --- | --- | ----- | ---------- | --- | ----------- | ----- | ----------- | -------- | ---- |
|                                |              |     |                                  |                          |     |     | frame | extraction | for | low quality | video | sequences,” | in Proc. | Int. |
| [33] L.Lu,D.                   | Liu,andH.-J. |     | Zhang,“Automaticmooddetectionand |                          |     |     |       |            |     |             |       |             |          |      |
WorkshoponImageAnalysisforMultimediaInteractiveServices,May
| tracking | of music | audio | signals,” | IEEE | Transactions | on Audio, |     |     |     |     |     |     |     |     |
| -------- | -------- | ----- | --------- | ---- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
2009,pp.25–28.
SpeechandLanguageProcessing,vol.14,no.1,pp.5–18,Jan.2006. [56] Z.Rasheed,Y.Sheikh,andM.Shah,“On theuseofcomputable
[34] Y.-H. Yang and H. H. Chen, “Music emotion ranking,” in Proc. features for film classification,” IEEE Trans. Circuits Syst. Video
Int. Conf. Acoustics, Speechand Signal Processing, ser. ICASSP ’09, Technol.,vol.15,no.1,pp.52–64,2005.
Washington,DC,USA,2009,pp.1657–1660.
|     |     |     |     |     |     |     | [57] P. Valdez | and | A. Mehrabian, |     | “Effects of | color | on emotions.” | J.  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------- | --- | ----------- | ----- | ------------- | --- |
[35] S.Koelstra,A.Yazdani,M.Soleymani,C.Mu¨hl,J.-S.Lee,A.Ni- Exp.Psychol.Gen.,vol.123,no.4,pp.394–409,Dec.1994.
jholt,T.Pun,T.Ebrahimi,andI.Patras,“Singletrialclassification [58] R.W.Picard,Affective Computing. MITPress,Sep.1997.
of EEG and peripheral physiological signals for recognition of [59] D.Li,I.K.Sethi,N.Dimitrova,andT.McGee,“Classification of
emotions induced by music videos,” in Brain Informatics, ser. general audio data for content-based retrieval,” Pattern Recogn.
| Lecture | Notes | in Computer | Science, | Y.  | Yao, R. | Sun, T. Poggio, |                               |     |     |     |       |     |     |     |
| ------- | ----- | ----------- | -------- | --- | ------- | --------------- | ----------------------------- | --- | --- | --- | ----- | --- | --- | --- |
|         |       |             |          |     |         |                 | Lett.,vol.22,no.5,pp.533–544, |     |     |     | 2001. |     |     |     |
J.Liu,N.Zhong,andJ.Huang,Eds. Berlin,Heidelberg:Springer [60] L. Lu, H. Jiang, and H. Zhang, “A robust audio classification
Berlin/Heidelberg,2010,vol.6334,ch.9,pp.89–100. and segmentation method,” in Proc. ACM Int. Conf. Multimedia,
[36] M.E.Tipping,“Sparsebayesianlearningandtherelevancevector Ottawa,Canada,2001,pp.203–211.
machine,”JournalofMachineLearningResearch,vol.1,pp.211–244, [61] P. Boersma, “Praat, a system for doing phonetics by computer,”
Jun.2001.
|     |     |     |     |     |     |     | GlotInternational, |     | vol.5,no.9/10,pp.341–345,2001. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------------------------------ | --- | --- | --- | --- | --- |
[37] J. D. Morris, “SAM: the self-assessment manikin. An efficient [62] L.Chen,S.Gunduz,andM.Ozsu,“Mixedtypeaudioclassifica-
cross-cultural measurement of emotional response,” Journal of tionwithsupport vectormachine,”inProc.Int.Conf. Multimedia
AdvertisingResearch,vol.35,no.8,pp.63–68,1995. andExpo,Toronto,Canada,Jul.2006,pp.781–784.
[38] M.BradleyandP.Lang,“Internationalaffectivedigitizedsounds [63] J.-S.LeeandC.H.Park,“Robustaudio-visualspeechrecognition
(iads): Stimuli, instruction manual and affective ratings,” The basedonlateintegration,”IEEETrans.Multimedia, vol.10,no.5,
Center for Research in Psychophysiology, University of Florida, pp.767–779,2008.
Gainesville,Florida,US,Tech.Rep.B-2,1999.

IEEETRANS.AFFECTIVECOMPUTING 15
SanderKoelstra(S’09)receivedtheB.Sc.and Touradj Ebrahimi (M’92) received his M.Sc.
M.Sc. degrees in Computer Science from the and Ph.D., both in electrical engineering, from
DelftUniversityofTechnology,TheNetherlands, theSwissFederalInstituteofTechnologyinLau-
in2006and2008,respectively.Heiscurrentlya sanne (EPFL), Lausanne, Switzerland, in 1989
PhDstudentwiththeSchoolofElectronicEngi- and 1992,respectively. From1989 to 1992,he
neeringandComputerScience atQueenMary was a research assistant at the Signal Pro-
University of London.Hisresearch interests lie cessing Laboratory of EPFL. In 1990, he was
intheareasofbrain-computerinteraction,com- a visiting researcher at the Signal and Image
putervisionandpatternrecognition. Processing Institute of the University of South-
ernCalifornia,LosAngeles,California.In1993,
|     |     |     |     |     |     |     | he was | a research | engineer |     | at the Corporate |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | -------- | --- | ---------------- | --- |
ResearchLaboratoriesofSonyCorporationinTokyo.In1994,heserved
|     |     |     |     |     | as a research | consultant | at  | AT&T Bell | Laboratories. |     | He is currently | a   |
| --- | --- | --- | --- | --- | ------------- | ---------- | --- | --------- | ------------- | --- | --------------- | --- |
ProfessorheadingMultimediaSignalProcessingGroupatEPFL,where
|           |          |       |            |        | he is involved | with | various | aspects | of digital | video | and multimedia |     |
| --------- | -------- | ----- | ---------- | ------ | -------------- | ---- | ------- | ------- | ---------- | ----- | -------------- | --- |
| Christian | Mu¨hl is | a PhD | researcher | at the |                |      |         |         |            |       |                |     |
applications.Heis(co-)authorofover100papersandholds10patents.
| Human-Media     | Interaction | group        | of    | the Univer- |     |     |     |     |     |     |     |     |
| --------------- | ----------- | ------------ | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| sity of Twente, | The         | Netherlands. | After | receiv-     |     |     |     |     |     |     |     |     |
ingaM.Sc.CognitiveScienceattheUniversity
| of Osnabrueck, | Germany, | in  | 2007, | working on |     |     |     |     |     |     |     |     |
| -------------- | -------- | --- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
neurophysiologicalmechanismsofcross-modal
|            |            |     |                       |     |     |     | Thierry | Pun   | (IEEE Member, |        | EE Eng.  | 1979,  |
| ---------- | ---------- | --- | --------------------- | --- | --- | --- | ------- | ----- | ------------- | ------ | -------- | ------ |
| attention, | he focuses | now | on the identification |     |     |     |         |       |               |        |          |        |
|            |            |     |                       |     |     |     | PhD     | 1982) | is head       | of the | Computer | Vision |
ofaffectivestatesbyneurophysiologicalsignals
|            |           |           |             |     |     |     | and | Multimedia | Laboratory, | Computer | Science |     |
| ---------- | --------- | --------- | ----------- | --- | --- | --- | --- | ---------- | ----------- | -------- | ------- | --- |
| in various | induction | contexts. | Especially, | he  | is  |     |     |            |             |          |         |     |
interested in the differential effects of auditory Department,UniversityofGeneva,Switzerland.
andvisualaffectivestimulationontheactivityof He received his Ph.D. in image processing for
|     |     |     |     |     |     |     | the development |     | of a | visual | prosthesis | for the |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ---- | ------ | ---------- | ------- |
thebrainasmeasuredviaelectroencephalography.
|     |     |     |     |     |     |     | blind          | in 1982, | at the    | Swiss        | Federal Institute |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | --------- | ------------ | ----------------- | --- |
|     |     |     |     |     |     |     | of Technology, |          | Lausanne, | Switzerland. | He                | was |
visitingfellowfrom1982to1985attheNational
InstitutesofHealth,Bethesda,USA.Afterbeing
|     |     |     |     |     |     |     | CERN | Fellow | from 1985 | to  | 1986 in Geneva, |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------ | --------- | --- | --------------- | --- |
Mohammad Soleymani (S’05) received both Switzerland, he joined the University of Geneva, in 1986, where he
his B.Sc. and M. Sc. from department of Elec- currentlyisfullprofessorattheComputerScienceDepartment.Hehas
| trical and | Computer | Engineering, | University |     | of  |     |     |     |     |     |     |     |
| ---------- | -------- | ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
authoredorco-authoredabout300fullpapersaswellaseightpatents.
| Tehran, in | 2003 and | 2006. | He is | now a doc- |                    |     |                              |     |     |                  |     |     |
| ---------- | -------- | ----- | ----- | ---------- | ------------------ | --- | ---------------------------- | --- | --- | ---------------- | --- | --- |
|            |          |       |       |            | Hiscurrentresearch |     | interests,relatedtoaffective |     |     | computingandmul- |     |     |
toralstudentandresearchassistantattheCom- timodalinteraction,concern:physiologicalsignalsanalysisforemotion
puterVisionandMultimediaLaboratory(CVML), assessment and brain-computer interaction, multimodal interfaces for
Computer Science Department, University of blindusers,datahiding,multimediainformationretrievalsystems.
Geneva.Hisresearchinterestsinclude:affective
computing,andmultimediainformationretrieval.
Hehasbeenco-organizingtheMediaEvalmulti-
mediabenchmarkinginitiativesince2010.
AntonNijholtisfullprofessorofHumanMedia
InteractionattheUniversityofTwente(NL).His
mainresearchinterestsaremultimodalinterac-
tion,brain-computerinterfacing,virtualhumans,
Jong-Seok Lee (M’06) received his Ph.D. de- affectivecomputing,andentertainmentcomput-
| gree in electrical |     | engineering | and | computer |     |     |      |        |              |      |             |     |
| ------------------ | --- | ----------- | --- | -------- | --- | --- | ---- | ------ | ------------ | ---- | ----------- | --- |
|                    |     |             |     |          |     |     | ing. | He has | co-organized | many | conferences |     |
science in 2006 from KAIST, Daejeon, Korea, (e.g., IVA 2009 and ACII 2009) and satellite
where he worked as a postdoctoral researcher workshops(e.g.,onaffectivebrain-computerin-
and an adjunct professor. He is now working terfacing) and has been guest-editor of many
as a research scientist in the Multimedia Sig- journalsforspecialissuesdevotedtoselections
nalProcessingGroupatSwissFederalInstitute
|                    |             |                    |           |           |               |     | of updates | of  | papers | from these | conferences |     |
| ------------------ | ----------- | ------------------ | --------- | --------- | ------------- | --- | ---------- | --- | ------ | ---------- | ----------- | --- |
| of Technology      | in Lausanne |                    | (EPFL),   | Lausanne, | andworkshops. |     |            |     |        |            |             |     |
| Switzerland.       | His current | research           | interests | in-       |               |     |            |     |        |            |             |     |
| clude audio-visual |             | signal processing, |           | multime-  |               |     |            |     |        |            |             |     |
diaqualityassessmentandmultimodalhuman-
computerinteraction.Heis(co-)authorofmorethan50publications.
|     |     |     |     |     |     |     | Ioannis | (Yiannis) | Patras | (S’97, | M’02, SM’11) |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ------ | ------ | ------------ | --- |
receivedthethePh.D.degreefromtheDepart-
|     |     |     |     |     |     |     | ment           | of Electrical | Engineering,     |     | Delft University |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------------- | ---------------- | --- | ---------------- | --- |
|     |     |     |     |     |     |     | of Technology, |               | The Netherlands, |     | in 2001.         | He  |
AshkanYazdanireceivedhisM.Sc.inelectrical is a Senior Lecturer in Computer Vision in the
engineering from University of Tehran, Iran in SchoolofElectronicEngineeringandComputer
2007. From 2006 to 2007, he worked as re- Science in the Queen Mary, University of Lon-
search assistant in the Brain Signal Process- don.Heis/hasbeenintheorganizingcommittee
| ing Group | at University | of  | Tehran, | on the top- |     |     |         |     |            |     |                |     |
| --------- | ------------- | --- | ------- | ----------- | --- | --- | ------- | --- | ---------- | --- | -------------- | --- |
|           |               |     |         |             |     |     | of IEEE | SMC | 2004, Face | and | Gesture Recog- |     |
ics of EEG-based person identification, brain- nition 2008, ICMR2011, ACM Multimedia 2013
computer interfacing and fMRI signal process- andwasthegeneralchairofWIAMIS2009.He
ing.HeiscurrentlyaPhDcandidateattheMul- is associate editor in the Image and Vision Computing Journal. His
timedia Signal Processing Group, Swiss Fed- research interests lie in the areas of Computer Vision and Pattern
eralInstituteofTechnologyinLausanne(EPFL),
|     |     |     |     |     | Recognition, | with | emphasis | on Human | Sensing | and | its applications |     |
| --- | --- | --- | --- | --- | ------------ | ---- | -------- | -------- | ------- | --- | ---------------- | --- |
Lausanne,Switzerland.Hismainresearchinter- in Multimedia Retrieval and Multimodal Human Computer Interaction.
estsincludeEEG-basedbrain-computerinterfacesystemsandbiomed- Currently,heisinterestedinBrainComputerInterfacesandtheanalysis
icalsignalprocessing. offacialandbodygestures.