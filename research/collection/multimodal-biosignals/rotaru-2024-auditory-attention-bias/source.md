





|**Citation/Reference**|Rotaru I., Geirnaert S., Heintz N., Van de Ryck I., Bertrand A., Francart T.,<br>(2024)<br>**What are we really decoding? Unveiling biases in EEG-based**<br>**decoding of the spatial focus of auditory attention**<br>Journal of Neural Engineering|
|---|---|
|**Archived version**|Accepted author manuscript: the content is identical to the content of the<br>published paper, but without the final typesetting by the publisher|
|**Published version**|https://doi.org/10.1088/1741-2552/ad2214|
|**Journal homepage**|https://iopscience.iop.org/journal/1741-2552|
|**Author contact**|iustina.rotaru@kuleuven.be<br>_+ 32 467329784_|
|**Abstract**||
|**IR**|Klik hier als u tekst wilt invoeren.<br>_(article begins on next page)_|





<!-- Start of picture text -->
IR  Klik hier als u tekst wilt invoeren.<br>(article begins on next page)<br><!-- End of picture text -->

# **What are we** **_really_ decoding? Unveiling biases in EEG-based decoding of the spatial focus of auditory attention** 

**Iustina Rotaru**<sup>1</sup><sup>_,_2</sup> **, Simon Geirnaert**<sup>1</sup><sup>_,_2</sup><sup>_,_3</sup> **, Nicolas Heintz**<sup>1</sup><sup>_,_2</sup><sup>_,_3</sup> **, Iris Van de Ryck**<sup>1</sup> **, Alexander Bertrand**<sup>2</sup><sup>_,_3</sup> **, Tom Francart**<sup>1</sup><sup>_,_3</sup> 

> 1KU Leuven, Department of Neurosciences, ExpORL. Herestraat 49 bus 721, B-3000 Leuven, Belgium 

> 2KU Leuven, Department of Electrical Engineering (ESAT), Stadius Center for Dynamical Systems, Signal Processing and Data Analytics. Kasteelpark Arenberg 10, B-3001 Leuven, Belgium 

> 3Leuven.AI - KU Leuven institute for AI, Belgium 

E-mail: `iustina.rotaru@kuleuven.be, alexander.bertrand@kuleuven.be, tom.francart@kuleuven.be` 

**Abstract.** _Objective._ Spatial auditory attention decoding (Sp-AAD) refers to the task of identifying the direction of the speaker to which a person is attending in a multitalker setting, based on the listener’s neural recordings, e.g., electroencephalography (EEG). The goal of this study is to thoroughly investigate potential biases when training such Sp-AAD decoders on EEG data, particularly eye-gaze biases and latent trial-dependent confounds, which may result in Sp-AAD models that decode eye-gaze or trial-specific fingerprints rather than spatial auditory attention. _Approach._ We designed a two-speaker audiovisual Sp-AAD protocol in which the spatial auditory and visual attention were enforced to be either congruent or incongruent, and we recorded EEG data from sixteen participants undergoing several trials recorded at distinct timepoints. We trained a simple linear model for Sp-AAD based on common spatial patterns (CSP) filters in combination with either linear discriminant analysis (LDA) or k-means clustering, and evaluated them both across- and within-trial. _Main results._ We found that even a simple linear Sp-AAD model is susceptible to overfitting to confounding signal patterns such as eye-gaze and trial fingerprints (e.g., due to feature shifts across trials), resulting in artificially high decoding accuracies. Furthermore, we found that changes in the EEG signal statistics across trials deteriorate the trial generalization of the classifier, even when the latter is retrained on the test trial with an unsupervised algorithm. _Significance._ Collectively, our findings confirm that there exist subtle biases and confounds that can strongly interfere with the decoding of spatial auditory attention from EEG. It is expected that more complicated non-linear models based on deep neural networks, which are often used for Sp-AAD, are even more vulnerable to such biases. Future work should perform experiments and model evaluations that avoid and/or control for such biases in Sp-AAD tasks. 

_Keywords_ : spatial auditory attention decoding (Sp-AAD), audiovisual stimulation, eyegaze biases, feature drifts 

2 

## **1. Introduction** 

Auditory attention decoding (AAD) is a well-established term that collectively describes a series of techniques designed to discern which acoustic source a listener is attending to within a mixture of acoustic sources. This is made possible with neural recordings such as electroencephalography (EEG), magnetoencephalography (MEG) or electrocorticography (ECoG) (O’Sullivan et al. 2014, de Cheveign´e et al. 2018, Mesgarani & Chang 2012). One of the most sought-after applications of AAD algorithms is their potential to identify the attended speaker in a multi-talker setting, in order to steer the noise suppression algorithms in hearing aids (HA), which can lead to a novel tier of _neuro-steered HA_ . These devices are currently envisioned to enable effortless control by hearing-impaired users through their brain signals, whereby the attended sounds are automatically recognized and enhanced over non-target sounds, leading to improved speech intelligibility and reduced listening effort expended by the HA users (Geirnaert, Vandecappelle, Alickovic, de Cheveign´e, Lalor, Meyer, Miran, Francart & Bertrand 2021, Slaney et al. 2020). 

From the rich collection of existing AAD algorithms, two major paradigms stand out: (1) stimulus-reconstruction algorithms which correlate a temporal representation of the acoustic stimulus (e.g., the speech envelope) with neural recordings to select the attended speaker (O’Sullivan et al. 2014, de Cheveign´e et al. 2018) and (2) direct classification algorithms which rely solely on neural recordings to distinguish the direction of an attended sound stream (Geirnaert, Francart & Bertrand 2021, Vandecappelle et al. 2021, Su et al. 2022, Pahuja et al. 2023, Cai et al. 2023). The latter is referred to as spatial auditory attention decoding (Sp-AAD), and represents the main focus of this paper. In short, an Sp-AAD decoder is optimized to detect the spatial focus of attention from instantaneous neural features which reflect spatial auditory attention patterns, e.g., lateralization patterns in the spatio-temporal EEG structure. The Sp-AAD decoding paradigm was previously shown to hold two major advantages w.r.t. the traditional AAD paradigms based on stimulus reconstruction: (1) it decodes the direction of an attended sound stream directly from the user’s EEG, i.e., without requiring access to demixed and clean audio signals and (2) it operates accurately on short time-scales (within 1–5 s) (Geirnaert, Francart & Bertrand 2021). These two positive feats make Sp-AAD particularly suitable for real-time attention decoding systems, whereby HA users are exposed to complex acoustic scenes and spontaneously switch their attention between different acoustic targets, often situated at distinct locations. 

Yet despite the promising prospects, the precise decoding mechanisms of the SpAAD models have not been fully unraveled, nor was their application and generalization validated in a sufficiently realistic Sp-AAD experiment comprising diverse audiovisual scenarios. In particular, several suspicions have been raised regarding potential non- 

3 

neural biases that could interfere with decoding the direction of auditory attention from EEG (Geirnaert, Francart & Bertrand 2021). In this work, we employed a simple linear method previously introduced for the Sp-AAD task, namely the Common Spatial Pattern (CSP) filtering algorithm (Geirnaert, Francart & Bertrand 2021), in order to investigate two such distinct biases, namely eye-gaze and trial-specific biases, e.g., due to large shifts in the feature space across trials caused by subjects taking a break or ‘recalibrating’ to a new task. Additionally, we evaluated the generalization performance of CSP filters across trials and subjects and incidentally found a third bias that can be leveraged by unsupervised classifiers which aim to cope with across-trial feature shifts. Specifically, we found that even within trials (over a time of less than a few minutes), a substantial drift occurs in the feature space, which could be easily confounded with feature changes caused by changes in spatial auditory attention. Below we further elaborate on the importance and motivations behind studying these biases when it comes to decoding spatial auditory attention. 

Firstly, we investigated whether lateralized eye-gaze signals (potentially buried in the EEG) are leveraged by CSP filters, thereby influencing the decoding accuracy. As CSP filters are trained directly on EEG signals during periods of sustained attention to localized speech, it was previously hypothesized they are susceptible to pick up lateralization patterns exhibited by non-neural signals (e.g., eye-gaze, face- or ear-muscle activations) that are correlated to the spatial focus of auditory attention (Geirnaert, Francart & Bertrand 2021, Strauss et al. 2020). Furthermore, a number of recent studies point towards interactions of the oculomotor system and top-down attentionmodulated speech processing. For instance, a phenomenon called _ocular speech tracking_ was observed by Gehmacher et al. 2023, claiming that gaze activity tracks acoustic features of an attended natural speech signal more strongly than for a distracting sound. The authors also showed evidence that oculomotor activity distinctly contributes to the neural responses of sensors overlapping the auditory processing areas (temporal and parietal). In another study on spatial auditory attention, Popov et al. 2022 showed neurophysiological evidence that alpha power lateralization, an established biomarker for the top-down attention-related mechanism that suppresses distracting input from unattended directions of sound, is closely associated with lateralized oculomotor action, i.e., eye-gaze shifts. However, previous studies employing CSPs in an Sp-AAD task were not able to fully rule out potential contributions from such confounds because these were not explicitly measured or controlled for in the evaluated datasets. Specifically, in the work of Geirnaert, Francart & Bertrand 2021, the AAD dataset on which the CSP filters were evaluated potentially had a strong eye-gaze confound enabled by the presentation of visual cues on the same side with the attended acoustic target (Das et al. 2020). As such, the AAD protocol design in that dataset made it intrinsically difficult to disentangle eye-gaze and attention and draw firm conclusions on whether neural or non-neural mechanisms drive the high CSP decoding accuracies observed in both the subject-dependent and subject-independent analyses. As a follow-up to that work, we here designed a new audiovisual AAD (AV-AAD) experiment to explore whether Sp- 

4 

AAD is still possible in the case of incongruent eye-gaze. This new protocol comprises experimental conditions where various degrees of correlation were imposed between the spatial directions of to-be-attended _visual_ and _auditory_ targets, such that they were either co-located, spatially uncorrelated, or the visual stimulus was totally absent. 

Secondly, we aimed to explore whether Sp-AAD models are sensitive to overfitting to trial-specific fingerprints (other than eye-gaze) which could potentially stem from non-stationarities in the EEG data, causing the signal statistics to change across trials. This could result in a shift in the feature space when comparing the feature vectors between two EEG segments with a significant amount of time between them. As a result, different trials might populate different locations in the feature space, such that a classifier can recognize a trial based on the location of the extracted features. In a recent review study, Puffay et al. 2023 highlighted and showcased the risk of exploiting such potential trial biases, i.e., trial-specific confounds in the EEG signals that can be recognized by a classifier, allowing it to artificially increase the decoding accuracy (especially in paradigms where a single class label is present per trial). To counteract this, they stress the importance of using a proper cross-validation (CV) scheme such as between-trial data splits (e.g., leave-one-trial-out CV) as opposed to within-trial splits, as the former does not result in artificially high accuracies due to overfitting to latent trial fingerprints. Similar concerns were expressed by Li et al. 2020, who disproved a study that performed an image classification task from EEG signals by finding that a proper train-testing scheme on a block-design EEG dataset degraded the classification accuracies of the trained models to chance, whereas using block-related labels resulted in a high classification accuracy, indicative of the fact that classification pipelines on EEG are susceptible to learn arbitrary block/trial fingerprints occurring in data segments from the same EEG block/trial. Thus, the generalization performance of a model should ideally be probed on data from a held-out trial (Puffay et al. 2023) or subject (Kamrud et al. 2021). 

Naturally stemming from the previous point, we lastly evaluated the (in-)ability of the CSP-based Sp-AAD algorithm to generalize across different trials by leveraging the novel AV-AAD dataset, in which multiple EEG trials of the same condition were recorded at two distant points in time. In addition, we investigated the cross-subject generalization performance of the Sp-AAD model, which is especially useful and timeefficient in a practical setting because it would allow the creation of plug-and-play AAD algorithms (i.e., pre-trained on EEG data from previous subjects) that can directly generalize to a new subject with a minimal or even without any calibration session. However, cross-subject generalization could also be sensitive to biases such as eye-gaze, as the EEG patterns related to ocular motion or gaze direction are expected to be fairly similar across subjects. To determine whether eye-gaze signals actually contribute to the generalization performance, our novel AV-AAD paradigm allows the evaluation of generalization across trials and subjects in conditions with and without a confound of eye-gaze. A by-product of this analysis was the finding that within-trial feature drifts significantly degrade the trial generalization performance of the CSP-based Sp-AAD 

5 

## model. 

The remainder of this paper is structured as follows: Section 2 describes the experimental setup and the novel AAD audiovisual protocol, Section 3 reviews the CSPbased Sp-AAD algorithm and the hyperparameters used in this study, while Section 4 presents and discusses the obtained results. Finally, conclusions are drawn in Section 5. 

## **2. Experimental setup** 

In this section, we introduce a new dataset that was primarily designed to investigate eye-gaze-related confounds and model generalization in an Sp-AAD task. To this end, different conditions were created, in which the spatial auditory attention is either congruent or incongruent with the eye-gaze. 

## _2.1. Participants_ 

Sixteen normal-hearing participants (one male, fifteen females) were recruited to take part in the AV-AAD experiment. This research was conducted in accordance with the principles embodied in the Declaration of Helsinki and was approved by the Medical Ethics Committee of UZ Leuven, Belgium (project reference S57102). All participants signed a written informed consent for voluntarily participating in the study. They were all native Flemish speakers and their age ranged between 19-27 years (the mean age and standard deviation was 20 _._ 72 _±_ 1 _._ 00 years). Before undergoing the main EEG experiment, the participants’ normal hearing was verified by means of pure-tone audiometry. 

## _2.2. Audiovisual protocol_ 

For stimulation, we used a self-curated playlist of video clips from“Universiteit van Vlaanderen” _‡_ , a popular platform for science-outreach podcasts delivered by various researchers. 

From a database of more than 100 such videos, we pre-selected 30 male-narrated videos with the best audio and video recording quality, spanning a wide variety of scientific topics. To make the experiment as engaging as possible, we let each participant choose their 10 most and 10 least preferred podcasts (with which they were not previously familiar) from our pre-compiled list. To avoid any stimulus pre-exposure effects in the preference selection stage, the subjects were not provided with the actual videos, but only their titles, which summarized the topic. All presented videos were in the .mp4 format and had an original resolution of 1280 _×_ 720 px, but were downscaled to a smaller frame size of 640 x 360 px since smaller versions of the videos will be presented at different locations on the screen (as explained further). The audio tracks of each video were separately extracted, and the overall root-mean-square (RMS) intensity was normalized to -27 dB FS. The silence portions of the audio tracks were not removed 

_‡_ `https://www.universiteitvanvlaanderen.be/` 

6 

nor shortened in order to ensure precise synchronization with the video. Lastly, all used videos and their audio tracks were cut to a duration of 10 min in order to match the trial length. 

In total, the experiment included four conditions, each consisting of two trials of 10 min (i.e., each condition lasted for 20 min in total). In each trial, two audio stimuli were simultaneously presented via the RME Fireface UC soundcard (RME, Haimhausen, Germany) connected to two insertphones of type Etymotic ER10 (Etymotic Research, Inc., IL, USA). First, the left and right insertphones were individually calibrated to present sound at an intensity of 65 dB SPL for a frontal source (we used speech-weighted noise as calibration stimulus). To recreate an acoustic spatial impression of sounds coming from distinct left and right locations, each of the two stimuli was separately convolved with head-related impulse responses (HRIRs) corresponding to either _−_ 90<sup>_◦_</sup> or +90<sup>_◦_</sup> (the HRIRs were measured on a dummy head in an anechoic room _§_ using inthe-ear microphones, cf. Kayser et al. 2009). This yielded an interaural level difference of approximately 10.6 dB between the ears for a stimulus from +90<sup>_◦_</sup> degrees. 

We randomized the presented stimuli per participant by randomly drawing (without repetition) from the participants’ lists of _most_ and _least_ preferred podcasts one _to-beattended_ and one _to-be-ignored_ speech stimulus, respectively, per experimental trial. For all conditions, the subjects had the same task, i.e., to listen to the target speaker as indicated on the computer screen and to ignore the competing speaker. However, depending on each condition’s type, the subjects were asked to adhere to a different set of visual instructions, explicitly shown at the beginning of each trial. 

An overview of the AV-AAD experimental conditions is presented in Table 1. To probe whether eye-gaze has any influence on the CSP decoding of spatial auditory attention in various AV scenarios, these conditions were designed to have different degrees of consistency between the spatial direction of visual and auditory attention. The visual stimulation in each of the four conditions (further referred to by their acronyms) is described in more detail below: 

- In the _Moving Video (MV)_ condition, the video of the to-be-attended speaker was presented as randomly moving along a linear horizontal left-right trajectory spanning the entire screen width. The target coordinates of each new video position were randomized along the horizontal axis, and the downscaled video was programmed to move with a constant and moderate speed of 50 px/s between these target points. The random movement was balanced such that the video was presented on each half of the screen for 50% of the time within each trial. Overall, this condition was designed to have complete inconsistency between the spatial visual and auditory attention throughout the whole stimulation duration. Note that despite the lack of spatial correlation, there was still a semantic correlation 

_§_ We refrained from using HRIRs measured in a non-anechoic room (which include reverberations), because we aimed to make the task perceptually simpler for the participants and allow them to fully focus on the auditory attention lateralization task. This is in line with previous AAD datasets where also anechoic HRIRs were used (Das et al. 2016). 

7 

|**Presentation**<br>**order**|**Condition name**<br>**A**|**uditory vs. visu**<br>**attention**|**al**<br>**Visual task**|
|---|---|---|---|
|1|Moving Video<br>(MV)|Incongruent|Follow the _moving video_ of the to-be-attended speaker<br>on a randomized horizontal trajectory.|
|2|Moving Target Noise<br>(MTN)|Incongruent|Follow the _moving cross-hair_ on a randomized<br>horizontal trajectory.|
|3|No Visuals<br>(NV)|Incongruent|Fixate on an imaginary point in the center of<br>the _black_ screen and minimize eye movements.|
|4|Static Video<br>(SV)|Congruent|Fixate the _static video_ presented on the same<br>side of the screen as the to-be-attended speaker.|



**Table 1:** Overview of the AV-AAD experimental conditions 

between the target acoustic and visual stimulus, since the content of the moving video matched the content of the attended speaker. 

- The _Moving Target Noise (MTN)_ condition visually consisted of a crosshair also randomly moving on a linear horizontal trajectory at 50 px/s, spanning the entire screen width. This condition was intended to be acoustically more challenging than the former, hence background babble noise was added to each insertphone at a Signal-to-Noise Ratio (SNR) of _−_ 1 dB (relative to the joint level of both speakers). In addition, by presenting a crosshair instead of a video, the visual semantic cues were removed, in order to enforce the spatial auditory attention as dominant. Altogether, the MTN condition lacked both the spatial and semantic correlation between the audiovisual stimuli. 

- In the _No Visuals (NV)_ condition, a black screen was presented and the participants were asked to fixate their gaze on an imaginary point within the center of the screen. This was intended as a control condition for visual attention. 

- In the _Static Video (SV)_ condition, the video of the to-be-attended speaker was statically presented on either the left or the right margin of the screen, in order to match the side of the to-be-attended acoustic stimulus _∥_ . Hence, there was both spatial and semantic correlation between the audiovisual stimuli. This condition was intended as a proxy for most scenarios in daily life, where visual and auditory attention are spatially aligned (i.e., a person directly gazes at the acoustic source they listen to). 

In the MV and MTN conditions, the range of the visual angle spanned by the participants’ eyes was geometrically determined from the screen width (47.6 cm) and the average distance from the participant’s head to the screen (45 cm). This yielded an 

_∥_ Note there is no 100% correspondence between the direction of the presented video and the direction of attended acoustic stimulus due to physical limitations (e.g., screen size and participant’s distance from the screen): the audio is presented at _±_ 90<sup>_◦_</sup> degrees, while the videos are presented at approx. _±_ 20<sup>_◦_</sup> relative to the participant’s standpoint, facing the center of the screen (considered at 0 degrees). Thus, both the audio and visual stimuli were presented to either the left or right hemifield of the participants. 

8 



<!-- Start of picture text -->
Block 1 Block 2<br>MV MTN NV SV MV MTN NV SV<br>trial 1 trial 1 trial 1 trial 1 trial 2 trial 2 trial 2 trial 2<br>Experiment timeline<br><!-- End of picture text -->

**Figure 1:** An overview of the experimental timeline in the AV-AAD dataset. A trial is hereby defined as the uninterrupted stimuli presentation for a duration of 10 minutes, during which EEG was recorded. Each color and acronym represents a specific condition, as follows: MV = Moving Video; MTN = Moving Target Noise; NV = No Visuals; SV = Static Video. A block consists of four sequential trials (recorded with small breaks in between), one for each condition type. The trials and conditions were presented in the same order for all participants. 

estimation range of ( _−_ 20<sup>_◦_</sup> _,_ +20<sup>_◦_</sup> ) relative to the screen center _¶_ . 

Time-wise, the conditions were presented in two separate blocks, i.e., the first trial of each condition were presented sequentially, followed by a second block of trials from each condition (cf. fig. 1). As such, the EEG signals belonging to the two trials of each condition were purposefully measured about 40 min apart, in order to capture the EEG non-stationarity across trials, allowing us to probe the between-trial generalization of CSP filters. The conditions were presented in the same order for all subjects (cf. fig. 1). Following preliminary pilot tests, the SV condition was subjectively rated as the least difficult, hence it was deliberately presented last. The MTN condition was not presented to the first three subjects as it was a later addition to the experiment. Hence, the total EEG recording time was 60 minutes (for 3 subjects) and 80 minutes (for the remainder 13 subjects). After every trial of 10 min, there was a short break, which ensured that the participant’s attention levels were constantly refreshed. A longer break of approximately 5 min in-between the two experimental blocks was also offered to the participants. Comprehension questions related to the content of the attended stimulus were presented at the end of each trial, in order to maintain motivation levels and attention throughout the experiment. The participants had to answer with a word or a short phrase, and their behavioral answers were further analysed to monitor task compliance (results are presented in section 4.1). 

In addition, one _spatial switch of attention_ was introduced at the midpoint of each trial (5 min), by programming both stimuli to swap sides from left (L) to right (R) or vice versa. For each subject and condition, the locus of attention in the _first_ trial was randomized between (L, R) and (R, L), while the second trial had the opposite attention pair. In conditions with visual stimulation (MV, MTN and SV), an arrow was continuously displayed on the screen, pointing to the direction of the to-be-attended acoustic stimulus. Additionally, the arrowhead changed from L to R (or reversely) after 5 min, to visually cue the participants about the spatial attention switch. Conversely, in the NV condition, the participants were only verbally cued at the beginning of the 

> _¶_ A precise measurement was not possible since the participants’ heads were not fixated. As such, they could have spontaneously, even unconsciously, changed their head position during the EEG data collection, thus slightly changing the range of the visual angle. 

9 

trial to which speaker (L or R) they had to listen first and were _a priori_ instructed to stay alert and switch their attention on the other side when they heard the two stimuli (automatically) swapping sides. 

The entire experiment was conducted in a soundproof, electromagnetically shielded room. 64-channel EEG and 4-channel electrooculography (EOG) were recorded at a sampling rate of 8192 Hz with the BioSemi ActiveTwo system (Amsterdam, The Netherlands). The EOG sensors were placed symmetrically around the eyes (cf. fig. 4 in Lopez et al. 2016). Two of the EOG sensors were placed approx. 1.5 cm above and below the right eye (aligned with the center of the eye) to measure vertical oculomotor activity (vertical saccades or blinks). The other two EOG sensors were placed approx. 1 cm right of the right eye and 1 cm left of the left eye, respectively, to measure horizontal oculomotor activity. All visual stimuli were presented on a 21.5 inch screen with a resolution of 1920 _×_ 1080 px by running custom-made Python scripts. Synchronization between the audio and video stimuli was performed with the _pygame_ module<sup>+</sup> , while synchronization between the measured EEG and the corresponding audio stimuli was achieved via squared-pulse triggers presented every second for the entire duration of each trial and recorded using the EEG system. 

## **3. Decoding spatial auditory attention with CSP filtering** 

## _3.1. CSP filtering_ 

Common spatial patterns (CSP) filtering is a technique widely used in, e.g., braincomputer interfaces (BCI) with motor imagery paradigms to discriminate left- versus right-hand motor imagery (Blankertz et al. 2008, Lotte et al. 2018). Based on previous observations that spatial auditory attention appears to be spatio-temporally encoded in the neural activity (Bednar & Lalor 2018, 2020, W¨ostmann et al. 2016, Patel et al. 2018), Geirnaert, Francart & Bertrand 2021 demonstrated the feasibility of CSP filters in an Sp-AAD paradigm to decode the directional focus of auditory attention from EEG in a competing-speaker setting. Below we briefly review the CSP filtering for the binary Sp-AAD paradigm, where the objective is to optimally discriminate between listening to the left and right. For a detailed description of the general theoretical framework of CSP filters, we refer the reader to the studies of Blankertz et al. 2008, Parra et al. 2005. 

In a nutshell, the CSP filters **W** _∈_ R<sup>_C×K_</sup> project the (zero-mean) EEG signal **x** ( _t_ ) _∈_ R<sup>_C×_1</sup> measured at a time instance _t_ from the original electrode space of _C_ channels into a surrogate subspace **y** _CSP_ ( _t_ ) = **W**<sup>⊺</sup> **x** ( _t_ ) _∈_ R<sup>_K×_1</sup> of lower dimension _K ≪ C_ , where the _K_ output channels are uncorrelated and the discrimination between the two classes is maximized. 

Mathematically, the CSP algorithm determines the orthogonal spatial filters **w** _k ∈_ R<sup>_C×_1</sup> (the columns of **W** ) which maximize the output ratio of variance between the instances of the two classes **x** 1 _/_ 2( _t_ ) _∈_ R<sup>_C×_1</sup> in the projected subspace: 

> + `https://www.pygame.org/` 

10 



where 



is the covariance matrix of class _Ci, i ∈{_ 1 _,_ 2 _}_ and _|Ci|_ denotes the number of time instances in class _Ci_ . As shown in Blankertz et al. 2008, the solution of Eq. 2 can be found by computing a generalized eigenvalue decomposition of the class-specific covariance matrices: 



By plugging Eq. 4 into Eq. 2, we obtain: 



Thus, the best discrimination between the two classes is obtained when the EEG signals are projected onto the generalized eigenvector **w** 1 corresponding to the largest generalized eigenvalue _λ_ 1. The projection **w** 1<sup>⊺</sup><sup>**x**(</sup><sup>_t_)willthenproduceavirtualchannel</sup> which will have the maximal relative difference in signal power between the two classes (as targeted in Eq. 1). By reciprocity (i.e., switching the numerator and denominator in Eq. 1), the smallest generalized eigenvector **w** _K_ corresponding to the smallest generalized eigenvalue _λK_ will achieve the same for the other class. Therefore, to select the _K_ most informative spatial filters, the generalized eigenvalues _λk_ are sorted and the corresponding first<sup>_<u>K</u>_</sup> 2<sup>andlast</sup><sup>_<u>K</u>_</sup> 2<sup>generalizedeigenvectorsarethenselectedascolumns</sup> of **W** . 

## _3.2. Classification_ 

CSPs are usually part of a larger classification pipeline to decode directional auditory attention on new EEG data (unseen in the CSP training phase). In the following, we describe the classification procedure which we used in our analysis. 

To obtain features for classification, the test EEG data is bandpass-filtered into _B_ pre-defined frequency bands and segmented into smaller time windows of length _T_ , called _decision windows_ . The classification task consists in assigning each decision window to either one of the two classes (attended left or right). To this end, the CSP filters (separately trained per frequency band) are applied per frequency band on each decision window of the test data. Finally, the log-energies of each CSP-filtered window 

11 

and frequency band are computed (using log-energy features is common in CSP-based classifiers). This results in a total of _B × K_ CSP features _fk,b_ per decision window: 



which are stacked together into one feature vector **f** _∈_ R<sup>_BK×_1</sup> . To determine the directional focus of attention, **f** is fed to the input of a binary classifier. In this work, we consider two popular classifiers: supervised linear discriminant analysis and unsupervised k-means clustering. 

_3.2.1. Supervised classification with Linear Discriminant Analysis._ Fisher’s linear discriminant analysis (LDA) is traditionally used in combination with CSP filters (Lotte et al. 2018). LDA optimizes a linear projection **v** _∈_ R<sup>_BK×_1</sup> within the feature space that maximizes the between-class scatter while minimizing the within-class scatter. This also leads to a generalized eigenvalue problem, which can be solved analytically (Bishop & Nasrabadi 2006): 



Here, **Σw** _∈_ R<sup>_KB×KB_</sup> is the joint covariance matrix of the features **f** from both classes and **_µ_** 1 _/_ 2 _∈_ R<sup>_BK×_1</sup> are the features’ means across all decision windows in each class. The LDA decision boundary is given by: 



where **v** is defined in Eq. 7, and _b_ is the classifier’s bias or threshold, expressed as the mean of the LDA-projected class means: 



Eventually, **f** is classified into class _C_ 1 if _D_ ( **f** ) _>_ 0 and into class _C_ 2 if _D_ ( **f** ) _<_ 0. 

Note that both CSP and LDA are data-driven and supervised, as they require ground-truth-labeled data to be trained on. 

_3.2.2. Unsupervised classification with k-means._ As noted by Lotte et al. 2018, Huang et al. 2010, using CSPs in combination with LDA classifiers in BCIs could suffer from generalization problems across experimental trials and/or subjects. The potential inability to generalize has been generally attributed to EEG non-stationarities which are unavoidable during long and separate measurement sessions due to changes in the subject’s brain processes, attention and fatigue levels, different artifactual patterns (Blankertz et al. 2007) (e.g., frowning, blinking, swallowing, or yawning) or changes in the experimental conditions (interfering equipment and noise sources). 

In an attempt to overcome potential problems with train-test generalization generated by EEG data captured at different time points, we here take a different approach and aim to directly classify the test CSP features in an unsupervised way, thus 

12 

bypassing any train-data biases in the LDA step. To this end, we replace the supervised LDA with k-means clustering, an _unsupervised_ classification algorithm(Bishop & Nasrabadi 2006). In short, k-means finds the optimal partitioning of a given set of observations into K clusters by assigning each observation to the cluster with the nearest centroid (the mean of all points in the cluster) in an iterative process, without needing any _a priori_ label/class information. 

We note that unsupervised clustering can be performed directly on the test data, i.e., it does not need to be trained on a separate training set (as opposed to CSP and LDA). As a result, it adds flexibility to adapt the classifier to individual (test) trials. However, without further context, it is impossible to then determine which cluster belongs to which class. In Section 3.4, we explain the workaround we employed in computing accuracies for the k-means clustering analyses. 

## _3.3. Practical implementation_ 

_3.3.1. Data preprocessing._ The EEG was initially downsampled using an anti-aliasing filter from 8192 Hz to 256 Hz to decrease the processing time. The EEG trials were then filtered between 1-40 Hz using a zero-phase Chebyshev filter (type II, with 80 dB attenuation at 10% outside the passband) and subsequently re-referenced to the common average of all channels. Afterwards, additional downsampling to 128 Hz was performed to speed up the training of attention decoders. Note that we intentionally refrained from applying z-scoring or any time-related normalization per trial in order to avoid contamination of preprocessing signatures that could be picked up by CSP filters when pooling neighboring data segments across trials, e.g., for CV purposes (see also Section 3.4). 

_3.3.2. Hyperparameter choices._ The CSP filters are usually trained and applied on EEG data filtered in a single frequency band of interest or across a pre-selected range of frequency bands that are relevant to the analysis at hand. In this work, we adopted the so-called filterbank CSP (as in Geirnaert, Francart & Bertrand 2021), which entails that EEG is first filtered into _B_ different frequency bands and the CSP filters are then trained and applied per frequency band, resulting in a total of _B_ CSP filter matrices **W** _b_ , with _b_ = 1 _, ..., B_ . We considered a filterbank of _B_ = 14 overlapping bands spanning a wide frequency range: [1-4], [2-6], ..., [24-28], [26-30] Hz. Thus, we intentionally avoided to manually pick a single frequency band, in favor of allowing the classification algorithm to decide which bands are most relevant for distinguishing between left (L) vs right (R) auditory attention. 

The number of CSP filters (per frequency band), i.e., _K_ , is another tunable hyperparameter. Too many filters are not desirable, as the number of filter weights to optimize increases, and with it, the risk of overfitting. Too few filters are neither optimal, as they might not accurately capture the discrimination between the two classes. Thus, following the conventional CSP recipes from the BCI literature (Blankertz et al. 2008), 

13 

we chose to train a moderate number of _K_ = 6 CSP filters per frequency band. 

Before the CSP training step (Eq. 4), we regularized the large-dimensional covariance matrices of each class ( **R** _C_ 1 _/_ 2) using diagonal loading, i.e., by computing a weighted combination of the sample covariance matrix (potentially poorly-conditioned, but unbiased) and the identity matrix (well-conditioned, but uninformative). The weights of both matrices were automatically determined via the Ledoit-Wolf criterion (Ledoit & Wolf 2004, Geirnaert, Francart & Bertrand 2021). 

Finally, as the generalized eigenvalues represent the ratio between class-specific energies of each spatially filtered signal (cf. Eq. 2), they can become corrupted by outlier segments with a high variance. To avoid this issue, the most discriminative CSP filters were selected based on the ratio of median output energies (RMOE) between both classes, cf. Blankertz et al. 2008, (instead of the sorted generalized eigenvalues in Eq. 4), taken over all training windows of length equal to the maximal decision window length that is used in the analysis. 

## _3.4. Performance evaluation_ 

The CSP filters were trained and evaluated per experimental condition both within subjects (subject-specifically) as well as across subjects (subject-independently). As evaluation metric, we reported the _decoding accuracy_ , i.e., the percentage of correctly classified decision windows averaged across all CV test folds, CV repetitions and tested subjects. We used several variations of CV schemes in order to discover different biases in the data (see below). In each experiment, the CSP filters and LDA were always trained together on the same subset of data. For different analyses, we used different sets of labels to compute the accuracy (summarized in fig. 2): for probing the eye-gaze bias in Section 4.2, we used labels informative of spatial auditory attention, further denoted as _attention_ labels (indicating whether the subject attended to the _L_ or _R_ speaker); for probing the trial fingerprint bias in Section 4.3, we used labels distinguishing each specific trial, further denoted as _trial_ labels (i.e., the EEG segments belonging to the first and second trial of each condition were labelled as 1 and 2, respectively); for probing trial generalization, we used both attention labels and labels informative of feature drift (further details are presented in Section 4.5). 

14 



**Figure 2:** A summary of the different class labels used per condition and trial in different cross-validation (CV) settings. The “ _|_ ” sign delimits the labels assigned to data segments from the first and second half of each trial, respectively. As previously, the colors denote the condition type of each trial. 

For the _subject-specific_ decoding (further denoted as CSP-SS), separate CSP filters and LDA classifiers were trained per subject and per experimental condition with random 5-fold CV. To this end, the two trials of each condition were concatenated and the resulting EEG data was split into segments of 60 s, which were then randomly shuffled in one of the 5 CV folds, while ensuring a balanced amount of L- and R-labelled segments both in the train and test splits. In order to compute the accuracy obtained with different decision window lengths (WLs), the EEG segments of each test fold were further split up into smaller windows ranging from 1 to 60 s. Per subject, average accuracies were computed across the 5 CV test folds, and across 3 repetitions of the random CV scheme (re-shuffling the 60sec segments into different CV folds). Given that CSP-based classifiers perform comparably well across WLs (Geirnaert, Francart & Bertrand 2021), and that small WLs are required for fast decoding, we used the median accuracies obtained with a WL of 5 s to perform all the statistical analyses presented in Section 4, unless stated otherwise. 

We also trained _subject-independent_ CSP filters (further denoted as CSP-SI) and LDA classifiers by implementing leave-one-subject-out CV per condition. However, the CSP filters are known to work less well in the subject-independent setting because of the high variability of signals in different frequency bands across subjects (Geirnaert, Francart & Bertrand 2021). Therefore, exclusively for the CSP-SI analysis, the EEG data was bandpass-filtered into one single broadband frequency range (1-30 Hz), and a bias update was applied to the LDA classifier as a normalization step to improve generalization across subjects (details in Geirnaert, Francart & Bertrand 2021). 

Furthermore, we investigated CSP generalization across trials by evaluating the CSP-SS decoder with a 2-fold leave-one- _trial_ -out CV scheme per condition, leveraging the fact that the two trials of each condition were recorded roughly 40 min apart. Trial generalization was evaluated both with a supervised LDA classifier and with an unsupervised k-means classifier directly applied on the test features in an attempt to compensate for feature drift (in both cases, accuracy was computed based on L/R attention ground-truth labels). 

For the classification with k-means clustering, we used _K_ = 2 clusters, 

15 

corresponding to the two attended locations. The cluster centroids were initialized with the (non-deterministic) k-means++ algorithm (Arthur & Vassilvitskii 2006), hence we performed 10 repetitions and up to 1000 iterations to re-update the centroids per repetition. From these 10 repetitions, we selected as final classifier the k-means model with the smallest sums of point-to-centroid distances within-cluster. Notably, k-means is an unsupervised algorithm that assigns arbitrary numerical labels to each cluster (being agnostic to the ground-truth labels), hence it is likely that comparing the clustering output labels to the ground-truth labels results in a low accuracy, which can be attributed to an overall label mismatch. To counteract this, both cluster assignments are tested (i.e., cluster 1 = _L_ -attended, cluster 2 = _R_ -attended, and vice versa), and the assignment that gives the highest accuracy is retained. Note that this implies we use ground-truth labels, and therefore these results based on k-means classification should not be viewed as representative of a realistic Sp-AAD pipeline. In practice, other heuristics can be used to do this label-to-cluster assignment without the use of the ground-truth labels<sup>_∗_</sup> , yet this is beyond the scope of this study, in particular since we will show that even when using this ground truth information, the k-means algorithm is not able to accurately perform Sp-AAD. 

For the reported accuracies obtained with LDA classification, the significance level was determined with the inverse binomial distribution, taking into account the total amount of available test data and a significance threshold of _α_ = 0 _._ 05 (O’Sullivan et al. 2014, Geirnaert, Francart & Bertrand 2021). As the different CV schemes or different WLs have a distinct number of test samples, this results in different significance levels. For k-means clustering, our manipulation of the L/R attended label assignment to each cluster leads to an inherent bias because it “artificially” pulls all the accuracies above 50%, thus also affecting the significance level. To compensate for this bias, exclusively for the k-means classification accuracy, we compute the significance level as the 97.5th percentile of the inverse binomial distribution (which is mathematically equivalent to the 95th percentile of the _folded_ inverse binomial distribution, i.e., the true distribution of the biased accuracies - details omitted). 

## **4. Results and Discussion** 

## _4.1. Behavioral results_ 

The subjects’ answers to the comprehension questions were analysed by direct comparison to the correct answers of the attended story in each trial. An average score of 76% correct responses was obtained across all subjects, conditions and trials, indicating a relatively high compliance with the auditory attention task. Per condition, the correct response scores were 75%, 79%, 78% and 71% (across all subjects) for MV, MTN, NV and SV conditions, respectively. 

> _∗_ e.g., by combining it with a (slower) stimulus reconstruction approach, or based on speaker localization in combination with speaker activity detection. 

16 

_4.2. Eye-gaze biases: CSP decoders achieve the highest accuracies in conditions with eye-gaze confounds_ 

The subject-specific CSP (CSP-SS) decoding accuracies following LDA classification with _attention_ labels and random 5-fold CV within condition are illustrated in fig. 3a for various WLs. For a WL of 5 s, the obtained median accuracies are 66 _._ 4% _,_ 63 _._ 8% _,_ 69 _._ 6% _,_ 71 _._ 4% for the MV, MTN, NV and SV conditions, respectively (fig. 3c). We investigated the effect of condition type on accuracy by means of a Linear Mixed Effects (LME) model where the _condition_ was considered as fixed effect and the _subject_ as random effect. The LME was fitted to maximize the restricted log-likelihood, and the residuals were checked for normality. Since we were primarily interested in how the audiovisual congruence impacts the decoding accuracy (hence comparing between audiovisual congruent and incongruent conditions), we assigned corresponding contrasts in the model (0.75 for the SV and -0.25 for each of the other conditions). The results revealed that decoding accuracies for the SV condition are significantly higher than for the other conditions (p = 0.002, b = 0.08, CI = [0.03 - 0.13]). This suggests that CSP filters can exploit eye-gaze-related signal components to infer the location of the attended speaker. 

Additionally, the subject-independent (CSP-SI) decoding results with LDA classification are depicted in fig. 3b. The obtained median accuracies with a leaveone-subject-out CV and a WL of 5 s are 56 _._ 9% _,_ 50% _,_ 51 _._ 1% _,_ 69 _._ 5% for the MV, MTN, NV and SV conditions respectively (fig. 3d). In stark contrast to the CSP-SS decoder, the CSP-SI decoder scores below significance in all audiovisually-incongruent conditions (MV, MTN and NV). In general, poorer performance for a subject-independent model is somewhat expected, as it is more difficult to generalize across subjects than within subject, given the heterogeneous EEG and idiosyncratic CSP feature distributions. Nevertheless, the significant accuracy in the SV condition seems to suggest that CSP is able to capture a dominant subject-independent signal component that is probably related to the eye-gaze direction. An LME model fitted on the CSP-SI accuracies with the same fixed and random effects as for the CSP-SS revealed a similar trend: the accuracy in the audiovisual-congruent SV condition is significantly higher than in the other conditions ( _p ≤_ 0 _._ 001, b = 0.18, CI = [0.13 - 0.23]). Remarkably, the CSP-SS and CSP-SI accuracies in the SV condition are _not_ significantly different (Wilcoxon signed rank test: W=31.5, N=15, p=0.12), possibly suggesting that the eye-gaze signal components are captured similarly well by both the subject-specific and subjectindependent decoders. Still, one must interpret this non-significant result with caution, as the underlying amount of training data for the CSP-SI decoders is much higher (300 min, aggregated across subjects) than for the CSP-SS (15 min per train CV fold). As such, it would not be unreasonable to expect that with more training data available, the CSP-SS would score even better than the CSP-SI for the SV condition. 

The beneficial effect of the eye-gaze directional information observed in the SV condition could have three possible reasons. Firstly, this result is in line with previous 

17 



<!-- Start of picture text -->
1.0 1.0<br>0.9 0.9<br>0.8 0.8<br>0.7 0.7<br>0.6 0.6<br>MovingVideo<br>0.5 MovingTargetNoise 0.5<br>NoVisuals<br>0.4 StaticVideo 0.4<br>Significance level<br>0.3 0.3<br>0 10 20 30 40 50 60 0 10 20 30 40 50 60<br>Decision window length (sec) Decision window length (sec)<br>(a) CSP-SS (b) CSP-SI<br>1.0 ** 1.0 ***<br>0.9 0.9<br>0.8 0.8<br>0.7 0.7<br>0.6 0.6<br>0.5 0.5<br>0.4 0.4<br>Significance level Significance level<br>0.3 0.3<br>MovingVideo MovingTarget NoVisuals StaticVideo MovingVideo MovingTarget NoVisuals StaticVideo<br>Noise Noise<br>condition condition<br>(c) CSP-SS, WL = 5 s (d) CSP-SI, WL = 5 s<br>Decoding Accuracy Decoding Accuracy<br>Decoding Accuracy Decoding Accuracy<br><!-- End of picture text -->

**Figure 3:** Attention decoding accuracy with subject-specific (CSP-SS) and subjectindependent (CSP-SI) decoders peaks for the spatially-congruent audiovisual presentation (SV condition). _Top_ : median decoding accuracies for all tested window lengths (WL), with shaded areas representing the 95% confidence interval. _Bottom_ : decoding results for WL = 5 s, with each dot representing the accuracy of one subject. Notably, the significance level is reduced for the CSP-SI as more test data was available than for the CSP-SS. The statistical contrast between StaticVideo vs. other conditions’ accuracies was tested with a Linear Mixed Effects (LME) model, whereby (**) marks significant differences for _p ∈_ (1e _−_ 3 _,_ 1e _−_ 2] and (***) for _p ∈_ (1e _−_ 4 _,_ 1e _−_ 3]. 

18 

studies, where the spatial alignment of eye-gaze and auditory attention was found to enhance the auditory percept, the behavioral performance in auditory target detection tasks and the discrimination of interaural time and level differences, which are crucial cues for sound localization (Maddox et al. 2014, Pomper & Chait 2017, Best et al. 2007, Andersen et al. 2009). A recent study (Best et al. 2023) showed that gaze direction alone had a strong effect on speech intelligibility: the recall of digit sequences in a competing multi-talker spatial acoustic scene was significantly better when the look direction coincided with the auditory target direction. Moreover, Gehmacher et al. 2023 showed evidence that _ocular speech tracking_ (i.e., the phenomenon in which eyegaze tracks prioritized acoustic features such as the acoustic envelope and acoustic onsets) is more pronounced for an acoustically attended target than for a distractor, thus advocating for a joint network of auditory selective attention and eye movement control. Extrapolating these findings to our Sp-AAD task, it is probable that a visual target spatially aligned with an attended acoustic stimulus enhances the neural auditory attention patterns exploited by CSPs. 

Secondly, the AV incongruence, which is artificially enforced in all conditions except in SV, might have made the attention task much harder for the participants to follow. In essence, the incongruent AV conditions are a dual task, with a different visual and auditory spatial focus, which could thus partly explain the significantly lower accuracies observed both for CSP-SS and CSP-SI decoders. 

Lastly, it is remarkable that the CSP-SS and CSP-SI accuracies both culminate in the SV condition, and particularly that CSP-SI accuracies are only significant in the SV condition, despite a comparable amount of training data for all conditions. These results thus reinforce the suspicion that CSP decoding is predominantly driven by signal components that originate from the motion of the eyeballs (i.e., EOG-related components), and therefore have no neurological component whatsoever. Assuming this is true, when the look direction does not match with the direction of auditory attention (used as ground truth), the CSP decoding accuracies are expected to drop, which is what we observe in the AV-incongruent conditions. In an additional analysis, we further evaluated this hypothesis by training new CSP-SS filters exclusively on the four external EOG channels (using a similar 5-fold random CV scheme). According to fig. 4, the median decoding accuracies based on EOG channels (with two CSP filters) are consistently lower than those obtained on the standard, 64-channel EEG, regardless of condition. This is confirmed by a non-parametric Wilcoxon signed-rank test (obtained p-values are 0 _._ 001 _,_ 0 _._ 15 _,_ 0 _._ 03 and 0 _._ 04 for MV, MTN, NV and SV respectively). While the EOG-based CSP accuracies are barely significant in the AV-incongruent conditions (as expected, since eye-gaze shifts in those conditions are random), they are above the significance level in the SV condition. This supports the hypothesis that CSP filters do leverage explicit eye-gaze directivity patterns present in both EOG and EEG signals. 

While these results make it clear that EOG-related components allow CSP-based decoders to achieve higher accuracies in AV-congruent settings, it remains nevertheless remarkable that decoding accuracies above the significance threshold also occur in 

19 

conditions without any spatial overlap between the visual and auditory attention (MV, MTN and NV), albeit only in the subject-specific case (fig. 3a, 3c). This suggests that neural patterns purely reflecting the spatial lateralization of _auditory_ attention could still be driving the decoding performance in AV-incongruent conditions. 



<!-- Start of picture text -->
1.1<br>*<br>1.0<br>*<br>0.9 **<br>n.s.<br>0.8<br>EEG (64 channels)<br>0.7 EOG (4 channels)<br>Significance level<br>0.6<br>0.5<br>0.4<br>0.3<br>MovingVideo MovingTarget NoVisuals StaticVideo<br>Noise<br>condition<br>Decoding Accuracy<br><!-- End of picture text -->

**Figure 4:** Attention decoding accuracy scores for CSP-SS decoding (with an LDA classifier) on 64 EEG channels vs. 4 EOG channels obtained with random 5-fold CV per condition. To enable a direct comparison between the EEG- and EOG-based CSP decoders, only two CSP filters were trained per frequency band (instead of 6), using attention labels. Statistical significance based on a Wilcoxon signed-rank test is marked with (*) for _p ∈_ (1e _−_ 2 _,_ 0 _._ 05] and with (**) for _p ∈_ (1e _−_ 3 _,_ 1e _−_ 2]. n.s. = not significant. 

## _4.3. Trial biases: CSP filters can easily discriminate between data coming from distinct trials_ 

fig. 5 illustrates the subject-specific (CSP-SS) decoding accuracies following LDA classification with random 5-fold CV on a WL of 5 s, using _trial_ labels (i.e., both the CSP filters and LDA were trained to distinguish between data originating from the two distinct trials of each condition). The median obtained accuracies are 100%, 99.9%, 99.7% and 99.6% for MV, MTN, NV and SV conditions, respectively. 

These results confirm the hypothesis that the EEG signals contain trial-specific signatures that can be discriminated by an LDA classifier. The accuracies in fig. 5 are significantly higher than those obtained with attention labels in fig. 3c (Wilcoxon signed rank test: _p_ = 3e _−_ 5 _,_ 2 _._ 5e _−_ 4 _,_ 3e _−_ 5 and 6 _._ 1e _−_ 5 for MV, MTN, NV and SV conditions, respectively), suggesting that trial fingerprints are even more dominant than spatial auditory attention patterns. This implies a strong feature drift over time, since the two trials of each condition were recorded with considerable time in between. 

In line with the observations in Puffay et al. 2023, these results mark a red flag for the interpretation of accuracies obtained with random CV, especially when there is a single attention label per trial, which could be easily confounded with the trial label (Su 

20 

et al. 2022, Pahuja et al. 2023). If the L/R attention labels are balanced within a trial, then one might expect no effect from such biases. However, if there is also a significant feature drift _within_ a trial, the classifier can recognize which part of a trial a feature vector comes from, as long as there was training data from a nearby time point. 

Note that the benefits from the aforementioned biases are caused by the improper validation based on random CV, in which different short-term windows within a trial are randomly divided between the test and train set. As a result, there is always a high probability that there is one or a few training segments that are close (in time) to the test segment, and therefore have similar time-specific fingerprints that can help to discover the attention label of the test segment. Therefore, in the next subsection, we investigate the Sp-AAD performance in a more correct CV scheme that specifically evaluates across-trial generalization. 



<!-- Start of picture text -->
1.0<br>0.9<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>Significance level<br>0.3<br>MovingVideo MovingTarget NoVisuals StaticVideo<br>Noise<br>condition<br>Decoding Accuracy<br><!-- End of picture text -->

**Figure 5:** CSP filters in combination with an LDA classifier can discriminate trial fingerprints in all experimental conditions. Depicted are accuracy scores obtained with a CSP-SS decoder and LDA classifier evaluated with random 5-fold CV within condition using _trial_ labels (as opposed to _attention_ labels) for a WL of 5 s. Each data point corresponds to the CSP-SS accuracy of one subject. 

## _4.4. Time-related biases: feature shift across trials and feature drift within trials_ 

The results of the CSP trial generalization analysis with supervised LDA and unsupervised k-means are depicted in fig. 6. The median accuracies for the leaveone-trial out evaluation with LDA are largely non-significant (44.6%, 44.26%, 41.45% and 43.3% for MV, MTN, NV and SV conditions respectively, cf. fig. 6a), suggesting that either the CSP or LDA cannot generalize across two separate trials of the same condition and subject. One factor potentially explaining the low accuracies could be the insufficient amount of training data. As each train fold only contains data from one trial (i.e., 10 min), it is rather plausible that a single trial does not display diverse enough EEG signal patterns to enable CSPs to generalize to a similar experimental trial 

21 

recorded at a later time (despite the fact that the amount of time instances with L/R attention is balanced across trials). 

Nonetheless, the results from fig. 6b confirm that despite the limited amount of train data per condition, the unsupervised k-means classifier is able to restore the median accuracies above the significance threshold, vastly outperforming LDA (the median accuracies obtained with k-means are 65.2%, 77%, 71.9% and 72.9% for MV, MTN, NV and SV conditions, respectively). Thus, it seems that trial generalization with k- means clustering works in all experimental conditions, independently of the presence or absence of the eye-gaze confound. One possible reason is that the k-means algorithm is able to cope with the feature shifts between the training and test trial, as the clustering is performed on the test trial itself. This is further investigated next. 

In fig. 7 we present a series of exemplifying CSP feature distributions from the leave-one-trial-out evaluation, showing a 2D projection of the original high-dimensional CSP feature space following principal component analysis (PCA). It is noteworthy that the trained LDA boundary manages to separate the CSP features of the train trial, but fails to do so for the CSP features of the test trial, as they are shifted or rotated with reference to the features of the train trial. On the other hand, both the train and test feature clouds, if taken separately, still exhibit distinct, well-separable clusters for each class. It thus becomes clear why k-means clustering resulted in the significant accuracies observed in fig. 6b: as k-means is directly applied on the test features, it is completely agnostic to any potential biases from the train data, and can fully leverage the distinct configuration of the test features. 

Therefore, if one makes abstraction of the shift between the train and test features, it could be argued that it is possible to create clusters discriminative of spatial auditory attention when trained on one trial from a specific condition and applied to a distinct (test) trial from the same condition, which can be leveraged by an unsupervised clustering algorithm. Yet on a closer look, the CSP features in fig. 7 sometimes appear to drift away in different directions, instead of clustering together in a particular area of the feature space. In fact, depicting the CSP test features as a function of time (fig. 8) reveals that the observed feature drifts are generated by a smooth time-dependent drift in the data. Thus, another potential confound of spatial attention when only considering the features of a single trial are the feature drifts within that trial. With the present dataset, it is unfortunately not possible to conclude if the good k-means accuracies obtained for trial generalization are due to spatial attention (which was alternated only once within any test trial) or due to the time-related feature drifts naturally occurring within that trial. 

To rule out the hypothesis that k-means actually clusters the CSP features’ timerelated drifts, one could, for instance, apply k-means on EEG trials where spatial attention is swapped more often than once, and obtain similarly high accuracies as in fig. 6b (when using attention-related labels). Although the trials in our dataset were not designed with frequent switches in spatial attention, this represents a good design feature for future protocols focused on decoding spatial attention. In the following section, we 

22 

present an alternative analysis meant to probe whether within-trial feature drifts can be classified, thereby introducing yet another potential bias in Sp-AAD studies. 



<!-- Start of picture text -->
1.0 1.0<br>Significance level<br>0.9 0.9<br>0.8 0.8<br>0.7 0.7<br>0.6 0.6<br>0.5 0.5<br>0.4 0.4<br>0.3 0.3<br>Significance level<br>0.2 0.2<br>MovingVideo MovingTarget NoVisuals StaticVideo MovingVideo MovingTarget NoVisuals StaticVideo<br>Noise Noise<br>condition condition<br>(a) LDA classification (b) k-means classification<br>Decoding Accuracy Decoding Accuracy<br><!-- End of picture text -->

**Figure 6:** Trial generalization results for decoding the spatial auditory attention with CSPSS decoders and two different classifiers, i.e., supervised LDA ( _left)_ and unsupervised k-means ( _right_ ). Each data point represents the accuracy of an individual subject obtained with leaveone-trial-out evaluation per condition (WL = 5 s; _attention_ labels are used to train the LDA and to compute the final accuracies for both classifiers). 

## _4.5. Unsupervised classifiers can leverage within-trial feature drift_ 

To evaluate whether within-trial EEG feature drift can be exploited by unsupervised classifiers, one could in principle apply a classifier on EEG trials recorded during a baseline task, where there is no direct relationship between the time progression and spatial attention, and subsequently compute the accuracy based on labels informative of time progression (e.g., by assigning distinct labels to data segments originating from the _first_ and _second half_ of each trial, respectively). Since our dataset did not consist of trials that satisfy this condition, we performed this analysis on a separate, publiclyavailable dataset, namely SparrKULee (Bollens et al. 2023, Accou et al. 2023). 

SparrKULee consists of EEG trials recorded from a large sample of 85 normalhearing subjects, who each performed a basic listening task of attending to continuous single-speaker speech (hence with no alternations in spatial attention). For each participant, a different number of EEG trials with varying lengths were originally recorded. From those, only trials with a duration greater that 10 min were selected and their length was trimmed to exactly 10 min (in order to replicate the experimental conditions in our dataset). These trials were subsequently preprocessed with the same parameters used in our own dataset, as described in Section 3.3.1. 

23 



<!-- Start of picture text -->
subject 15, NoVisuals<br>train trial 1, test trial 2 train trial 2, test trial 1<br>train L<br>70 train R 56<br>test L<br>68 test R 54<br>LDA boundary<br>52<br>66<br>50<br>64<br>48<br>62<br>46<br>60<br>44<br>58<br>42<br>2 4 6 8 10 12 14 -14 -12 -10 -8 -6 -4 -2 0<br>PC 1 PC 1<br>subject 10, MovingVideo<br>train trial 1, test trial 2 train trial 2, test trial 1<br>train L<br>78<br>58 train R<br>test L<br>test R 76<br>56 LDA boundary<br>74<br>54 72<br>52 70<br>68<br>50<br>66<br>48<br>64<br>6 8 10 12 14 16 18 20 -12 -10 -8 -6 -4 -2 0 2 4 6<br>PC 1 PC 1<br>subject 10, MovingTargetNoise<br>train trial 1, test trial 2 train trial 2, test trial 1<br>78<br>train L<br>52 train R<br>test L 76<br>50 test R<br>LDA boundary<br>48 74<br>46<br>72<br>44<br>70<br>42<br>40 68<br>38<br>66<br>-15 -10 -5 0 5 8 10 12 14 16 18 20 22<br>PC 1 PC 1<br>PC 2 PC 2<br>PC 2 PC 2<br>PC 2 PC 2<br><!-- End of picture text -->

**Figure 7:** Representative examples of CSP-SS feature shifts and rotations across trials. For 2D visualization, Principal Component Analysis (PCA) was applied on the original CSP features to obtain the first two principal components (PCs) explaining the most variance in the original feature space. Each data point thus corresponds to the first two PCs of every decision window of 5 s. The data points belonging to the train and test sets are marked with circles and diamonds, respectively. The color denotes attention to the left (L) or right (R) speaker. The plotted LDA boundary (solid black line) was obtained after training LDA on the PCs obtained from the CSP train features. 

24 



<!-- Start of picture text -->
subject 10, MovingVideo<br>300 test trial 2 (first attention: R) test trial 1 (first attention: L) 300<br>59 74<br>250 58 73 250<br>57 72<br>200 56 71 200<br>55<br>70<br>150 54 150<br>69<br>53<br>68<br>100 52 100<br>51 67<br>50 50 66 50<br>49 65<br>10 12 14 16 18 20 -8 -6 -4 -2 0<br>PC 1<br>subject 10, MovingTargetNoise<br>300 test trial 2 (first attention: R) test trial 1 (first attention: L) 300<br>76<br>53<br>250 75 250<br>52<br>74<br>51<br>200 73 200<br>50<br>72<br>150 49 150<br>71<br>48<br>70<br>100 47 100<br>69<br>46<br>68<br>50 50<br>45 67<br>44<br>-15 -14 -13 -12 -11 -10 -9 -8 -7 -6 10 12 14 16 18 20 22<br>PC 1<br>PC 2<br>Time progression of features in class 'Left' (sec) Time progression of features in class 'Right' (sec)<br>PC 2<br>Time progression of features in class 'Left' (sec) Time progression of features in class 'Right' (sec)<br><!-- End of picture text -->

**Figure 8:** Within-trial feature drifts over time are prevalent in the CSP feature space and they represent a strong confound of the spatial auditory attention in our dataset. The _left_ and _right_ plots illustrate the 2D-projected CSP features of trial 2 and trial 1, respectively, of two illustrative conditions of subject 10. These features correspond to the _test_ CSP features of the latter two conditions plotted in fig. 7. However, they are here color-coded based on their corresponding timestamp within the trial. Thus, features with a lighter color hue (in each attention class) belong to later timestamps, i.e., they occur later in the respective trial. To clarify the relationship between time and attention, we mention as a reference the initial attended location in each trial, and remind the reader that the attended location always changed mid-trial (from _L_ to _R_ and vice-versa). 

Thereafter, we probed whether k-means can distinguish the feature drift withintrial, namely whether it can separately cluster the CSP features from the first and second half of each test trial. To this end, we applied a similar methodology as in Section 4.4: leave-one-trial-out CV based on pairs of 10-min trials per subject (i.e., one trial acts as training data and the other as test data). Concretely, we train CSP filters on the _training_ trial, and apply k-means on the resulting CSP features in the _test_ trial. For both the training and the classification step, we use labels informative of the feature drift within-trial, i.e., labels that distinguish between data segments originating in the first vs. second half of the trial (cf. last row of fig. 2). We note that the CSP training step is rather artificial in this context, as it is only meant to define some arbitrary CSP 

25 



<!-- Start of picture text -->
1.0<br>Significance level 10 min<br>0.9<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>SparrKULee dataset<br>(4-8 trials/subject)<br>Decoding Accuracy<br><!-- End of picture text -->

**Figure 9:** k-means clustering of CSP-SS features can significantly classify feature drifts within-trial on the SparrKULee dataset, which has no confound of spatial auditory attention (the participants underwent multiple trials in which they listened to single-speaker speech). Each dot represents the leave-one-trial-out accuracy of an individual subject for a WL of 5 s, computed based on labels informative of feature drift within-trial. 

filters which are applied on the test trial, resulting in test CSP features to be classified by k-means. To obtain pairs of trials which are far away from each other in time (similar to our own dataset), the trials from the first half of the experimental session were paired with the trials from the second half of the experimental session, in chronological order, such that any particular trial occurred only once across all trial pairs. 

Fig. 9 reports the average accuracies obtained with k-means clustering over all test trials and across all pairs (per subject), computed in reference to labels informative of within-trial feature drift, for a WL of 5 s. In addition, time-progressive feature drifts similar to those in fig. 8 were also observed in this dataset (figures omitted). The significant accuracies confirm the hypothesis that k-means is able to pick up on feature drifts within-trial that create spurious clusters in the feature space, this being consistent across a large sample of subjects. Extrapolating this interpretation to the previous results on our dataset, it is likely that the significant k-means accuracies obtained in fig. 6b were also driven by the underlying within-trial feature drifts and not by neural patterns related to spatial auditory attention. However, we reiterate that time-related feature drifts and spatial attention cannot be fully disentangled when classifying data from single trials on our dataset, hence the latter claim remains mainly speculative. 

The main overarching implication of this analysis is that the feature drift withintrial can be decoded and could potentially become a problematic confound when decoding spatial auditory attention across trials with an unsupervised classifier. One way to avoid this confound right from the data collection stage could be through (1) a proper randomization of the order of spatial auditory attention labels across trials and (2) a reduction in the length of segments with sustained attention such that time-related 

26 

fingerprints are minimally informative for the attention labels. 

## **5. Conclusion** 

In summary, we designed an audiovisual AAD protocol to probe whether spurious signals of non-neural origin interfere with the decoding of spatial auditory attention (Sp-AAD) from EEG. The dataset, comprising EEG recordings from sixteen normalhearing participants undergoing a spatial auditory attention task, was primarily meant to probe for eye-gaze bias and generalization performance across trials and subjects. 

We found that CSP filters trained across- and within-trial are susceptible to capture a whole range of confounding signal patterns. In particular, we showed that lateralized eye-gaze congruent with the spatial target of auditory attention can contaminate EEG signals with such dominant patterns that can be accurately decoded both within and across subjects. Moreover, trial fingerprints and feature drifts within-trial are additional confounds of spatial auditory attention that can be decoded with highly significant accuracies by linear supervised and unsupervised classifiers, such as LDA and k-means clustering. In light of the current results, it still remains an open question whether neural patterns that encode the spatial focus of attention are actually decodable, as the cooccurrence and interplay between these different confounds can profoundly impact even a simple classifier and prevent it from finding EEG signal patterns solely informative of spatial auditory attention. 

In order to rule out contributions from such task-irrelevant signals, one would need to design an Sp-AAD protocol where none of these confounds is present, yet this is quite impractical (if not impossible) and will render ecologically invalid and artificial conditions. For instance, spatial alignment between a visual and acoustic target is naturally present in most everyday listening scenarios, while trial fingerprints and entanglement of feature drifts due to either time progression or attention shifts are intrinsic to the measured EEG data. Nonetheless, future work should take measures to mitigate these biases to the best possible extent, such as: inclusion of more frequent switches in spatial attention to ensure a balanced distribution of spatial attention labels per experimental trial; inclusion of explicit EEG preprocessing steps for ocular artifact rejection in order to suppress eye-gaze components from the EEG signals (preferably combined with incongruent audio-visual conditions); proper model evaluation with leave-one-trial/subject-out CV in order to avoid trial-related biases. 

While we demonstrated these biases with linear CSP filters and linear classifiers, we believe that more advanced (non-linear) models for decoding spatial auditory attention, such as deep neural networks, can suffer from similar biases, possibly even more due to their higher sensitivity to overfitting (Puffay et al. 2023, Li et al. 2020). Future work developing methodologies for the Sp-AAD task based on EEG should thus be aware of and seek solutions to address these biases before declaring their feasibility and effectiveness. 

_REFERENCES_ 

27 

## **6. Acknowledgements** 

The authors are grateful to all the participants in this study, and to Anouck Jaspers and Koen van den Eeckhout for their help with data collection. The authors would also like to thank Debora Fieberg for the early brainstorming sessions and for providing the audio stimuli used in this study. Financial support was provided by the Research Foundation Flanders (FWO) (SBO mandate 1S14922N for I. Rotaru, SBO mandate 1S31522N for N. Heintz, SBO mandate 1S34821N for I. Van de Ryck and FWO project G0A4918N), by KU Leuven through a PDM mandate (for S. Geirnaert, No. PDMT1/22/009), and by the European Research Council (ERC) under the European Union’s Horizon 2020 Research and Innovation Programme (Grant Agreements No. 637424 and 802895 for T. Francart and A. Bertrand, respectively). The authors declare no conflicts of interest. 

## **References** 

- Accou, B., Bollens, L., Gillis, M., Verheijen, W., Van hamme, H. & Francart, T. (2023), ‘Sparrkulee: A speech-evoked auditory response repository of the ku leuven, containing eeg of 85 participants’, _bioRxiv_ pp. 2023–07. 

- Andersen, T. S., Tiippana, K., Laarni, J., Kojo, I. & Sams, M. (2009), ‘The role of visual spatial attention in audiovisual speech perception’, _Speech Communication_ **51** (2), 184–193. 

- Arthur, D. & Vassilvitskii, S. (2006), k-means++: The advantages of careful seeding, Technical report, Stanford. 

- Bednar, A. & Lalor, E. C. (2018), ‘Neural tracking of auditory motion is reflected by delta phase and alpha power of EEG’, _NeuroImage_ **181** , 683–691. 

- Bednar, A. & Lalor, E. C. (2020), ‘Where is the cocktail party? Decoding locations of attended and unattended moving sound sources using EEG’, _NeuroImage_ **205** (116283). 

- Best, V., Boyd, A. D. & Sen, K. (2023), ‘An effect of gaze direction in cocktail party listening’, _Trends in Hearing_ **27** , 23312165231152356. 

- Best, V., Ozmeral, E. J. & Shinn-Cunningham, B. G. (2007), ‘Visually-guided attention enhances target identification in a complex auditory scene’, _JARO - Journal of the Association for Research in Otolaryngology_ **8** (2), 294–304. 

- Bishop, C. M. & Nasrabadi, N. M. (2006), _Pattern recognition and machine learning_ , Vol. 4, Springer. 

- Blankertz, B., Kawanabe, M., Tomioka, R., Hohlefeld, F., M¨uller, K.-r. & Nikulin, V. (2007), ‘Invariant common spatial patterns: Alleviating nonstationarities in braincomputer interfacing’, _Advances in neural information processing systems_ **20** . 

- Blankertz, B., Tomioka, R., Lemm, S., Kawanabe, M. & M¨uller, K. R. (2008), ‘Optimizing spatial filters for robust EEG single-trial analysis’, _IEEE Signal Processing Magazine_ **25** (1), 41–56. 

28 

_REFERENCES_ 

- Bollens, L., Accou, B., Van hamme, H. & Francart, T. (2023), ‘SparrKULee: A Speechevoked Auditory Response Repository of the KU Leuven, containing EEG of 85 participants’. 

   - **URL:** _https://doi.org/10.48804/K3VSND_ 

- Cai, S., Schultz, T. & Li, H. (2023), ‘Brain topology modeling with eeg-graphs for auditory spatial attention detection’, _IEEE Transactions on Biomedical Engineering_ . 

- Das, N., Biesmans, W., Bertrand, A. & Francart, T. (2016), ‘The effect of head-related filtering and ear-specific decoding bias on auditory attention detection’, _Journal of Neural Engineering_ **13** (056014). 

- Das, N., Francart, T. & Bertrand, A. (2020), ‘Auditory attention detection dataset kuleuven’, _Zenodo_ . 

- de Cheveign´e, A., Wong, D. D., Di Liberto, G. M., Hjortkjær, J., Slaney, M. & Lalor, E. C. (2018), ‘Decoding the auditory brain with canonical component analysis’, _NeuroImage_ **172** , 206–216. 

- Gehmacher, Q., Schubert, J., Schmidt, F., Hartmann, T., Reisinger, P., Roesch, S., Schwarz, K., Popov, T., Chait, M. & Weisz, N. (2023), ‘Eye movements track prioritized auditory features in selective attention to natural speech’, _bioRxiv_ pp. 2023–01. 

- Geirnaert, S., Francart, T. & Bertrand, A. (2021), ‘Fast EEG-based decoding of the directional focus of auditory attention using common spatial patterns’, _IEEE Transactions on Biomedical Engineering_ **68** (5), 1557–1568. 

- Geirnaert, S., Vandecappelle, S., Alickovic, E., de Cheveign´e, A., Lalor, E., Meyer, B. T., Miran, S., Francart, T. & Bertrand, A. (2021), ‘Electroencephalography-based auditory attention decoding: Toward neurosteered hearing devices’, _IEEE Signal Processing Magazine_ **38** (4), 89–102. 

- Huang, G., Liu, G., Meng, J., Zhang, D. & Zhu, X. (2010), ‘Model based generalization analysis of common spatial pattern in brain computer interfaces’, _Cognitive neurodynamics_ **4** (3), 217–223. 

- Kamrud, A., Borghetti, B. & Schubert Kabban, C. (2021), ‘The effects of individual differences, non-stationarity, and the importance of data partitioning decisions for training and testing of eeg cross-participant models’, _Sensors_ **21** (9), 3225. 

- Kayser, H., Ewert, S. D., Anem¨uller, J., Rohdenburg, T., Hohmann, V. & Kollmeier, B. (2009), ‘Database of multichannel in-ear and behind-the-ear head-related and binaural room impulse responses’, _EURASIP Journal on advances in signal processing_ **2009** , 1– 10. 

- Ledoit, O. & Wolf, M. (2004), ‘A well-conditioned estimator for large-dimensional covariance matrices’, _Journal of multivariate analysis_ **88** (2), 365–411. 

- Li, R., Johansen, J. S., Ahmed, H., Ilyevsky, T. V., Wilbur, R. B., Bharadwaj, H. M. & Siskind, J. M. (2020), ‘The perils and pitfalls of block design for eeg 

29 

_REFERENCES_ 

   - classification experiments’, _IEEE Transactions on Pattern Analysis and Machine Intelligence_ **43** (1), 316–333. 

- Lopez, A., Ferrero, F. J., Valledor, M., Campo, J. C. & Postolache, O. (2016), A study on electrode placement in eog systems for medical applications, _in_ ‘2016 IEEE International symposium on medical measurements and applications (MeMeA)’, IEEE, pp. 1–5. 

- Lotte, F., Bougrain, L., Cichocki, A., Clerc, M., Congedo, M., Rakotomamonjy, A. & Yger, F. (2018), ‘A review of classification algorithms for EEG-based brain-computer interfaces: A 10 year update’, _Journal of Neural Engineering_ **15** (3). 

- Maddox, R. K., Pospisil, D. A., Stecker, G. C. & Lee, A. K. (2014), ‘Directing eye gaze enhances auditory spatial cue discrimination’, _Current Biology_ **24** (7), 748–752. 

- Mesgarani, N. & Chang, E. F. (2012), ‘Selective cortical representation of attended speaker in multi-talker speech perception’, _Nature_ **485** , 233–236. 

- O’Sullivan, J. A., Power, A. J., Mesgarani, N., Rajaram, S., Foxe, J. J., ShinnCunningham, B. G., Slaney, M., Shamma, S. A. & Lalor, E. C. (2014), ‘Attentional Selection in a Cocktail Party Environment Can Be Decoded from Single-Trial EEG’, _Cerebral Cortex_ **25** (7), 1697–1706. 

- Pahuja, S., Cai, S., Schultz, T. & Li, H. (2023), Xanet: Cross-attention between eeg of left and right brain for auditory attention decoding, _in_ ‘2023 11th International IEEE/EMBS Conference on Neural Engineering (NER)’, IEEE, pp. 1–4. 

- Parra, L. C., Spence, C. D., Gerson, A. D. & Sajda, P. (2005), ‘Recipes for the linear analysis of eeg’, _Neuroimage_ **28** (2), 326–341. 

- Patel, P., Long, L. K., Herrero, J., Mehta, A. D. & Mesgarani, N. (2018), ‘Joint Representation of Spatial and Phonetic Features in the Human Core Auditory Cortex’, _Cell Reports_ **24** (8), 2051–2062.e2. 

- Pomper, U. & Chait, M. (2017), ‘The impact of visual gaze direction on auditory object tracking’, _Scientific Reports_ **7** (1), 1–16. 

- Popov, T., Gips, B., Weisz, N. & Jensen, O. (2022), ‘Brain areas associated with visual spatial attention display topographic organization during auditory spatial attention’, _Cerebral Cortex_ **1** , 12. 

- Puffay, C., Accou, B., Bollens, L., Monesi, M. J., Vanthornhout, J., hamme, H. V. & Francart, T. (2023), ‘Relating eeg to continuous speech using deep neural networks: a review’, _Journal of Neural Engineering_ **20** (4), 041003. **URL:** _https://dx.doi.org/10.1088/1741-2552/ace73f_ 

- Slaney, M., Lyon, R. F., Garcia, R., Kemler, B., Gnegy, C., Wilson, K., Kanevsky, D., Savla, S. & Cerf, V. G. (2020), ‘Auditory Measures for the Next Billion Users’, _Ear and hearing_ **41** , 131S–139S. 

- Strauss, D. J., Corona-Strauss, F. I., Schroeer, A., Flotho, P., Hannemann, R. & Hackley, S. A. (2020), ‘Vestigial auriculomotor activity indicates the direction of auditory attention in humans’, _eLife_ **9** (e54536). 

_REFERENCES_ 

30 

- Su, E., Cai, S., Xie, L., Li, H. & Schultz, T. (2022), ‘STAnet: A Spatiotemporal Attention Network for Decoding Auditory Spatial Attention from EEG’, _IEEE Transactions on Biomedical Engineering_ . 

- Vandecappelle, S., Deckers, L., Das, N., Ansari, A. H., Bertrand, A. & Francart, T. (2021), ‘EEG-based detection of the locus of auditory attention with convolutional neural networks’, _eLife_ **10** (e56481). 

- W¨ostmann, M., Herrmann, B., Maess, B. & Obleser, J. (2016), ‘Spatiotemporal dynamics of auditory attention synchronize with speech’, _Proceedings of the National Academy of Sciences of the United States of America_ **113** (14), 3873–3878. 

