www.nature.com/scientificdata 



# **oPEN Mobile Brain-Body Imaging and Data DESCRIPtoR Visual Data of theatrical actors During Rehearsal and Performance** 

**Manuel Flurin Hendry**<sup>**1**</sup> **, Jesus G. Cruz-Garza**<sup>**2**</sup> **, Esther a. Delgado-Jiménez**<sup>**2,3**</sup> **, Yoshua E. Lima-Carmona**<sup>**2**</sup> **, aime J. aguilar-Herrera**<sup>**2**</sup> **, Mauricio a. Ramírez-Moreno**<sup>**2,3**</sup> **, akshay Sujatha Ravindran**<sup>**2**</sup> **, andrew Y. Paek**<sup>**2**</sup> **, Michelle Smith**<sup>**2**</sup> **, Julia Kan**<sup>**2**</sup> **, Mikayla Fors**<sup>**2**</sup> **, amirah alam**<sup>**2**</sup> **, Ruofan Liu**<sup>**2**</sup> **, adam Noble**<sup>**4**</sup> **& Jose L. Contreras-Vidal**<sup>**2**✉</sup> 

**this longitudinal Mobile Brain-Body Imaging dataset was acquired during six rehearsal sessions and three public performances of a scene from a play with highly emotional components. three student actor dyads (N=6), one theatre director (N=1) and three audience members (N=3) participated in this study. the MoBI data recorded includes mobile electroencephalography, electrooculography, blood volume pulse, heart rate, body temperature, electrodermal activity, triaxial arm and head acceleration. The visual data includes five streams of video. This article describes the experimental setup, the multimodal data streams acquired using a hyperscanning methodology, and an assessment of the data quality.** 

## **Background & Summary** 

We present a longitudinal Mobile Brain-Body Imaging (MoBI) dataset consisting of six theatre rehearsals and three theatre performances containing simultaneously recorded physiological and visual data using a hyperscanning approach based on hardware triggers. The dataset has been acquired over the course of a week in which a theatre director staged a theatre scene with three dyads of undergraduate acting students. In two rehearsal sessions, the director deployed a predefined sequence of rehearsal methods identical for each dyad. For all participants, we recorded electroencephalography (EEG), electrooculography (EOG), blood volume pulse (BVP), heart rate, body temperature, electrodermal activity (EDA), triaxial arm and head acceleration, and five streams of video. Additionally, on the day of the performance, three audience members observing the scene had their EEG and video recorded. 

Acting has been an emerging area of interest for neuroscience in recent years, as techniques such as functional Near-Infrared Spectroscopy (fNIRS) have been implemented in order to analyze neural, physiological, and behavioral signatures of pairs of actors<sup>1</sup> . Nevertheless, to our knowledge, this is the first publicly available longitudinal dataset combining MoBI and visual data of theatre student actors during rehearsals and public performances. 

It will allow researchers to quantify the synchronization of physiological activity patterns within and across all participating individuals. Furthermore, it will permit the execution of a range of functional connectivity analyses and brain mapping techniques using electroencephalographic (EEG) data. These methodologies can then be integrated with corresponding visual data to enhance the understanding of the neural correlates of theatre acting<sup>2</sup> . Previous studies have examined acting processes related to cognition and text memorization using fMRI<sup>3</sup> , a method that investigates actors in an artificial laboratory setting and prevents any physical movement or interaction with other actors. With MoBI technology, we have the opportunity to study brain activity in action and in context, associated with behavioral data in real-world settings. 

> 1institute for the Performing Arts and film, Zurich University of the Arts, Zurich, Switzerland. 2Non-Invasive Brain-Machine Interface Systems Lab, IUCRC BRAIN, University of Houston, Houston, TX, USA.<sup>3</sup> Mechatronics Department, School of Engineering and Sciences, Tecnologico de Monterrey, Monterrey, Mexico.<sup>4</sup> School of theatre and Dance, University of Houston, Houston, TX, USA.<sup>✉</sup> e-mail: jlcontreras-vidal@uh.edu 

Scientific **Data** | _(2025) 12:1421_ | https://doi.org/10.1038/s41597-025-05713-2 

1 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



<!-- Start of picture text -->
EOG_VB<br>EOG_VA<br><!-- End of picture text -->





<!-- Start of picture text -->
EOG_HL<br>IMU<br><!-- End of picture text -->



















**Fig. 1** ( **a** ) EEG setup on the actors of Dyad B. The setup includes a 32-channel EEG head cap connected to a signal transmitter (MOVE system). The transmitter is attached to the actors’ back with a belt around their waist to allow freedom of movement. Actors also wore Empatica E4 wristbands. **(b)** Channel locations of the 32-channel headset with electrodes around the eyes. **(c)** Close up view of the electrodes. Front view of the electrodes around the eyes on the acting director (top) and view of the full EEG set up on an audience member (bottom). **(d)** Stage set for the performance. 

## **Methods** 

**Participants.** Ten healthy individuals (six males, four females; ages 21-47 years old) with no history of neurological disorder participated in this study. For data collection purposes in the experiment, one individual participated as director, six individuals participated as student actors (three male, three female), and three as audience members. All participants provided written informed consent for their participation in the study, including explicit permission for the open publication of their identities, video footage, and associated data on a credible public data repository. The experimental protocol, informed consent form, and image release documentation were reviewed and signed by each participant. Additionally, all members of the recording crew granted permission for the use of the captured video material. All published data have been de-identified where applicable, except in cases where participants consented to identifiable publication. The protocol forms were approved by the Institutional Review Board of the University of Houston (UH IRB #14415-01: NCS-FO: Assaying neural individuality and variation in freely behaving people based on qEEG). All procedures were performed in accordance with the 45 Code of Federal Regulations (CFR) part 46 (“The Common Rule”), specifically addressing the protection of human study subjects as promulgated by the U.S. Department of Health and Human Services (DHHS). 

**Instrumentation and Data Collection.** The actors, the director, and the audience members were instrumented with a 32-channel mobile EEG cap (BrainAmpDC with actiCAP and MOVE, Brain Products GmbH, Germany) sampled at 500 Hz. Four electrodes from the EEG cap were used for EOG recording. The actors were fitted with E4 Empatica wristband (Empatica Inc.) used to measure BVP sampled at 64 Hz, heart rate calculated from the BVP at 1 Hz, temperature sampled at 4 Hz, EDA sampled at 4 Hz, and triaxial arm acceleration sampled at 32 Hz<sup>4</sup> . Head movement was recorded by attaching an Inertial Measurement Unit (IMU) device on each actors’ headset. These units used wireless Magnetic, Angular Rate, and Gravity (MARG) sensors (OPAL, APDM Inc., Portland, OR) with a sampling rate of 128 Hz. Each IMU provided 9-axis data, consisting of three-axis accelerometer, three-axis magnetometer, and three-axis gyroscope measurements. Figure 1 shows the MoBI instrumentation on the participants, and Fig. 2 displays all data simultaneously collected from one of the participants. 

The head circumference of each participant was measured before the experiment to select an EEG cap of appropriate fit<sup>5</sup> . A 32-channel Ag/AgCl active electrode EEG cap was used to record from the face and scalp. The data were recorded using the BrainVision Recorder software (Brain Products GmbH, Germany). Four EEG electrodes were removed from the cap and used for EOG to capture blinks and eye movements (Fig. 1c). The remaining 28 electrodes were arranged according to the international 10-20 system. The vertical EOG electrodes were positioned 1 cm above (EOG_VA) and below (EOG_VB) to the right eye, while the horizontal EOG 

Scientific **Data** | _(2025) 12:1421_ | https://doi.org/10.1038/s41597-025-05713-2 

2 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



**Fig. 2** All data collected from one participant (P01 - Dyad C) during the performance: EEG data (32 channels: 28 channels for EEG and the remaining 4 channels for EOG), Empatica data for left and right hand (acceleration in x, y and z, BVP, heart rate, EDA and temperature) and IMU sensor data (head and body acceleration in x, y and z). The EEG and EOG signals have a scale of 150 _μ_ V, and the signals from Empatica and IMU have a scale of 30 units according to their respective measuring units. 

electrodes were placed 1 cm on the left (EOG_HL) and right (EOG_HR) temples on the sides of the face. The electrode locations used for recording are shown in Fig. 1b. 

The participants were asked to refrain from using products in their hair that may increase the impedance at the scalp electrode interface. Prior to donning the cap, the skin on the face around the eyes, the temples, and the earlobes were gently cleaned with alcohol wipes to remove any dirt and decrease impedance. A conductive electrolyte gel was applied between the electrode tips and the scalp to reduce the interface impedance. The impedance was maintained below 50 kΩ and in most cases reduced to below 20 kΩ before the start of the experiment recording sessions for each participant. The channel impedance values were recorded prior to the start of the experiment and after the end of the experiment. 

The video streams were recorded with four tripod-mounted cameras: two Sony EX1, one Sony EX3, and one Canon G1X Mark II. The default camera positions are shown in Fig. 3. For some sequences, one of the four cameras was dismounted from the tripod and used for hand-held recording. The frame rate varied between 24 fps and 30 fps, and resolutions ranged from 720p to 4K. Although the audio is not included in the shared dataset due to copyright restrictions, it was recorded with two Tascam DR-05 field recorders in stereo mode at 48kHz / 24 bit. In post-production - using the AVID Media Composer software - the camera source files were converted to 1080p / 25 fps. The video and audio streams were synchronized using the recorded UTC time screen, audiovisual hand clap cues and - where necessary - manual alignment based on visual cues and audio information from the discarded camera microphones. The aligned video streams were then merged by resizing them into a four-quadrant, single-stream video representing four camera perspectives. The four (2 × 2) audio channels were merged and mixed down to 2-channel stereo, discarding duplicate channels to avoid noise. Still images of the videos are shown in Fig. 4. 

Scientific **Data** | _(2025) 12:1421_ | https://doi.org/10.1038/s41597-025-05713-2 

3 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 





<!-- Start of picture text -->
a<br>C<br>D D<br>C<br>B<br><!-- End of picture text -->



<!-- Start of picture text -->
b<br>C<br>C<br><!-- End of picture text -->



<!-- Start of picture text -->
M<br>N<br><!-- End of picture text -->



<!-- Start of picture text -->
O<br><!-- End of picture text -->



<!-- Start of picture text -->
D<br><!-- End of picture text -->



<!-- Start of picture text -->
F<br>G<br>H<br><!-- End of picture text -->



<!-- Start of picture text -->
L<br>K<br><!-- End of picture text -->



<!-- Start of picture text -->
Labels<br>A  Set<br>B  Research Station<br>C  Cameras x4<br>D Live view of EEG signals and<br>audio recorders<br>E  Hotel desk, chair, and telephone<br>F  Hotel Bathroom Door<br>G  Dan (Male Actor)<br>H  Alice (Female Actress)<br>I  Hotel bed<br>J   Hotel lounge chair<br>K  Dan's pants<br>L  Hotel room door<br>M  EEG cap (32 channel)<br>N  Belt to secure EEG<br>O  Wireless transmitter<br>P  EEG wireless transmitter<br><!-- End of picture text -->





<!-- Start of picture text -->
I<br>J<br><!-- End of picture text -->

**Fig. 3** ( **a** ) Top view of Quintero Theatre located in the University of Houston. **(b)** Right view of Quintero Theatre with the actors. Section highlighted in blue shows what will be captured by the bottom right camera, as displayed in Fig. 3c. **(c)** View from the bottom right camera. Two actors, Alice and Dan, act out an emotional scene. The scene takes place in a hotel room set. **(d)** EEG setup on 3 participants (2 actors and 1 director/audience member). Setup includes a 32 channel electrode cap (M), secure belt (N), and EEG wireless transmitter (O). 



<!-- Start of picture text -->
Dyad A Dyad B Dyad C<br><!-- End of picture text -->

**Fig. 4** MoBI data from all actors was collected from both rehearsals and performance. **(Rehearsal I)** The actors gave table readings of the script and conducted partial rehearsals under the guidance of the director. **(Rehearsal II)** The actors improvised and performed Meisner repetition exercises. The director provided feedback between and during partial and full rehearsals. **(Performance)** The actors performed the scene in front of an audience. MoBI data was also collected from three audience members. 

Scientific **Data** | _(2025) 12:1421_ | https://doi.org/10.1038/s41597-025-05713-2 

4 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

|**Day**|**Date**|**Sessions**|**Time**|**Dyad**|**Director/ Audience Member**|
|---|---|---|---|---|---|
|I|Wed, January 16 2019|Rehearsal I|5:30 pm - 10:00 pm|A B C|Director|
|II|Tu, January 17 2019|Rehearsal II|5:30 pm - 10:00 pm|A B C|Director|
|III|Fri, January 18 2019|Rehearsal III<br>(Unrecorded)|6:00 pm - 10:00 pm|A B C|Director|
|IV|Sat, January 19 2019|Performance|2:30 pm - 6:00 pm|A B C|Audience Member A, Audience Member B, Audience Member C|



**Table 1.** Itinerary followed during the experiment. 

The data streams of the video, the wireless EEG, and head IMU device were time synchronized using a custom hardware trigger and aligned using MATLAB R2019a (The Mathworks Inc., Natick, MA). The video recordings captured a computer screen displaying UTC time as streamed through www.time.gov(The National Institute of Standards and Technology, US Department of Commerce). This time recording allowed the E4 Empatica data to be synchronized by matching the corresponding Unix time stamps in the data stream using MATLAB R2019a. 

**Experimental Protocol.** The experiment was conducted over the course of four days at the Quintero Theater (Kathrine G. McGovern College of the Arts, University of Houston). Each rehearsal session lasted for about one hour per dyad, all led by the same director. The actor dyads did not witness the rehearsal sessions of the other dyads. The full scene itself lasted about 7 minutes. Table 1 shows the itinerary followed during the experiment. 

On the rehearsal days, the director staged an emotionally charged scene from Patrick Marber’s stage play “Closer”<sup>6</sup> (scene 11) with three dyads (A, B and C) of two acting students each: a female playing the character “Alice”, and a male playing the character “Dan”. The scene progresses from harmony through disagreement to violent altercation. Each rehearsal session was conducted as a sequence of predefined rehearsal methods. These rehearsal methods included: table readings, improvisations, physical blocking, scene rehearsals, and Meisner repetition exercises<sup>8</sup> . MoBI data was gathered from all six actors during rehearsals and the performance. During rehearsals, MoBI data from the director was also gathered. On the day of the performance, MoBI data was collected from the six acting students, and from three audience members. The performances of the three dyads took place sequentially on the same day, in front of a live audience. On a screen to the side of the stage, out of sight for the actors, a visual representation of the actors’ brain activity was displayed in real time for the audience. After the performance, an open question and answer session between the audience members, the acting students, the director, and the research team ensued. 

Each participant wore a 32-channel EEG headset and wireless signal transmitter secured by a belt on their waist as they continued with the experiment. Raw EEG data was compiled for each participant member for each dyad (A, B and C) into one large file for each day (rehearsal-day 1, rehearsal-day 2, performance-day 3). P01 corresponds to the actor playing the character “Dan”, P02 the actress playing the character “Alice”, and P03 the director (in days 1 and 2) and a distinct audience member (in day 3). There are 27 individual datasets corresponding to: each participant (three participants) on each dyad (three dyads) on each day (three days). P01 on Dyads A/B/C included 31 EEG channels (27 EEG, 4 EOG), instead of 32, due to error with the electrode CP6, which had to be removed. P02 and P03 include 32 EEG channels (28 EEG, 4 EOG). 

**assessment of Data Quality.** Custom MATLAB R2021a software and functions from EEGLAB<sup>9</sup> (https:// sccn.ucsd.edu/eeglab/index.php) were used to assess the quality of the data. This assessment included impedance check, assessment of motion artifacts, line noise and physiological artifacts such as eye movement and muscle activity. An automated process for the removal of bad channels and timepoints was implemented. Figure 5 shows the pre-processing steps suggested, with their respective parameters, for a de-noising approach for each performance data set. 

EEG data was pre-processed using EEGLAB<sup>9</sup> . By downsampling the EEG data to 240 Hz (EEGLAB pop_resample plugin), video and EEG data simultaneous visualization was integrated as that frequency is a multiple of the video resolution (24 fps) without a significant loss of data. 

Noisy data portions were identified visually in the EEG and video, and timestamps were extracted for rejected 1-second segments that were observed with large motion artifacts. The remaining data with clean epochs was concatenated and moved to the preprocessing stage. In order to remove ocular activity obtained with the four _H_<sup>_∞_</sup> EOG channels, EEG was filtered with the filter considering the parameters of how rapidly the weights vary with time (q = 1e-10), the initial noise covariance matrix (p0 = 0.5), and the maximum bound on _H_<sup>_∞_</sup> gain ( _γ_ = 1.15)<sup>10</sup> . 

EEG data was then re-referenced to the average using robust re-referencing though the PREP pipeline<sup>11</sup> , and band-pass filtered using a 5th order Butterwoth FIR filter in [0.01 - 50] Hz range. In addition, for the purpose of removing motion-related noise, a Motion Artifact Filter was implemented at second order (N = 2), using similar parameters to the _H_<sup>_∞_</sup> filter, including q = 1e-10 and _γ_ = 1.5, with three sam= ples time taps and f 1 Hz. This frequency was identified from the visualization of the power spectrum density of the gravity-compensated acceleration<sup>12</sup> . After motion artifact removal, the Artifact Subspace Reconstruction (ASR) algorithm was applied to the data<sup>13,14</sup> . It was used to reconstruct data periods on each channel that are contaminated by an artifact, which amplitude is higher than _κ_ = 10 standard deviations. 

Scientific **Data** | _(2025) 12:1421_ | https://doi.org/10.1038/s41597-025-05713-2 

5 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



<!-- Start of picture text -->
Multimodal Data<br>E4 Empatica: IMU (128 Hz)<br>Video Raw EEG (500 Hz) Raw EOG (500 Hz) Temperature (4 Hz) 3 magnetometer axes<br>(24 fps) 28 channels 4 channels Triaxial Acc (32 Hz) 3 acceleration axes<br>BVP(64 Hz)-EDA(4 Hz) 3 gyroscope axes<br>Artifact Removal Stage 1<br>Gravity<br>compensation<br>Data resampling using<br>Data Labelling pop_resample<br>from EEGLAB (250 Hz)<br>Acceleration<br>(x, y, z axis)<br>Removal of rejected 1-second<br>segments based on timestamps<br>Artifact Removal Stage 0 Artifact Removal Stage 2<br>Data resampling using Robust Re-Referencing<br>pop_resample Clean epochs<br>from EEGLAB (240 Hz)<br>Bandpass Filter<br>(0.01 - 50 Hz)<br>Concatenation of<br>Video & EEG data visualization data vectors<br>H ∞ Motion Artifact Filter<br>H ∞ Filter<br>Identification of noisy Artifact Subspace<br>data portions Reconstruction (ASR)<br>Timestamps for rejected 28 EEG channels 28 EEG channels<br>1-second segments<br>Artifact Removal Stage 3<br>Independent Component<br>Dipole fitting MNI standard template<br>Analysis (ICA)<br>Clean 28 EEG<br>K-Means clustering Artifactual dipoles removal<br>channels<br><!-- End of picture text -->

**Fig. 5** Suggested EEG-denoising preprocessing pipeline. The steps only apply to EEG data. They can be split into two sections: video plus EEG data visualization, and cleanup of the EEG data. 

Finally, Extended Infomax Independent Component Analysis (ICA)<sup>15</sup> was applied to decompose data into independent sources using the principal component analysis option to compensate for the maximum number of components to the data rank reduction caused by the interpolation and re-referencing. ICA was used to detect independent components (ICs) of artifacts mixed with the EEG signals, such as ocular, muscle, electrocardiography, and power lines artifacts<sup>16</sup> . 

Subsequently, the standard template from the Montreal Neurological Institute (MNI) was used for dipole fitting and improvement of artifactual ICs removal by identifying the scalp projection for each of them. A K-means clustering algorithm within EEGLAB was applied to group all the scalp projections of each IC across all subjects, considering their spatial coordinate and distribution. Components with under 10% residual scalp map variance from the projection of the best-fitting equivalent dipole were kept. The optimal number of clusters, determined as 5 in this case, was identified using the Silhouette method<sup>17</sup> . ICs from subjects not assigned to any cluster, as well as those with spatial coordinates distant from the clusters centroid and power spectra indicative of non-brain artifacts, were excluded from the EEG data. A group of experienced researchers evaluated the independent components and removed those that they identified as artifacts. An example of the 

6 

Scientific **Data** | _(2025) 12:1421_ | https://doi.org/10.1038/s41597-025-05713-2 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



**Fig. 6** Example of decomposed artifacts that affect EEG signals from P01 - Dyad C during Performance, such as muscle, ocular, and other type of artifacts. 

identified artifactual components from the EEG data are shown in Fig. 6. Figure 7 shows a sample output of the EEG pre-processing sequence. 

## **Data Records** 

All data files are available at FigShare<sup>18</sup> . The data are archived in a single file set and organized with the following naming convention: 

BOA_recordingX_P0X_DyadX_suffix 

- BOA: Brain on Acting 

- recording1: Day 1 of rehearsal, first EEG recording of the experiment (roughly an hour long) 

- recording2: Day 2 of rehearsal, second EEG recording of the experiment (roughly an hour long) 

- • recording3: Final performance of scene on Day 4, final EEG recording of the experiment (roughly 7 minutes long) 

- P01: Actor on Dyad X for Dan 

- P02: Actor on Dyad X for Alice 

- P03: Same acting director for all dyads(for recording1 and recording2) or Audience member watching Dyad X (for recording3) 

- DyadA: Data collected for Dyad A 

- DyadB: Data collected for Dyad B 

- DyadC: Data collected for Dyad C 

- _suffix: Type of data 

**_EEG.mat.** The _EEG.mat file contains a 1 × 3 structure (described in Table 2; variable name: EEG) with electroencephalographic data collected by EEG sensors. The first element in the structure corresponds with the recording 1 (day 1 of rehearsal); the second element in the structure corresponds with the recording 2 (day 2 of rehearsal) and the third element corresponds with the recording 3 (final performance). The structure contains multiple fields corresponding to each dyad (A,B and C) and each subject (P01, P02 and P03). Table 2 breaks down the information contained within these fields. 

**_opals.mat.** The _opals.mat file contains a 1 × 2 structure (described in Table 3; variable name: opals) with kinematic data collected by opal sensors. The first element in the structure corresponds with the head sensor; the 3 second element in the structure corresponds with the body sensor. The structure contains multiple fields. Table breaks down the information contained within these fields. In recording 3 for dyad A, there are two minutes of data missing from the end due to a technical error. 

**_empatica.mat.** The _empatica.mat file contains a 1 × 2 structure (described in Table 4; variable name: empatica) with kinematic and bodily data collected by the Empatica E4. The first element in the structure corresponds with the left-hand sensor; the second element in the structure corresponds with the right-hand sensor. 4 The structure contains multiple fields. Table breaks down the information contained within these fields. 

**CSV Files.** CSV versions of the data files are included in the repository, following the same naming convention defined previously. All data have been organized into folders within a ZIP file for easier access and download. 

Scientific **Data** | _(2025) 12:1421_ | https://doi.org/10.1038/s41597-025-05713-2 

7 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



<!-- Start of picture text -->
75 μV<br>2 s<br><!-- End of picture text -->

**Fig. 7** Comparison of EEG signals (P01 - Dyad C during Performance) before (EEG and EOG) and after (EEG only) the pre-processing steps were implemented in the data. 



<!-- Start of picture text -->
EEG.setname Name defined for the dataset<br>EEG.filename Name defined for the file<br>EEG.subject Subject ID according to data records (P01, P02 or P03))<br>EEG.group Dyad ID according to data records (DyadA, DyadB or DyadC)<br>EEG.session Recording ID according to data records (recording1, recording2, recording3)<br>EEG.comments Name of the original file from which the data was extracted<br>EEG.nbchan Scalar value indicating number of channels used in EEG acquisition. For each subject a total of<br>32 channels were used; nevertheless, due to the complexity of the experiment, for some subjects<br>it was necessary to remove 1 or 2 channels.<br>EEG.trials Number of times the experiment was conducted<br>EEG.pnts Scalar value indicating vector length of each EEG signal acquired by each channel<br>EEG.srate Scalar value indicating sample rate of system (500 Hz)<br>EEG.xmin Start time of the data recording<br>EEG.xmax End time of the data recording<br>EEG.times 1xN vector containing timestamps at each timepoint N for EEG data.<br>EEG.data KxN matrix containing EEG data vector (channels-K) at each time point N (units: microvolts)<br>EEG.chanlocs 1xN vector containing the spatial location of each channel N according to the international 10-20 system<br>EEG.ref Channel referencing to the common average<br><!-- End of picture text -->

**Table 2.** Description of the fields contained within the _EEG.mat file structure. 

**Video records.** The video recordings corresponding to each day are included in the repository and are named according to the convention: “DyadX_Y_MMDDYY.mp4”, where X refers to the dyad identifier (A, B, or C), Y indicates the session type ("Rehearsal” or “Performance”), and MMDDYY denotes the date of the recording (month, day, year), as detailed in Table 1. Due to copyright restrictions associated with the script content<sup>7</sup> , these videos are provided without audio. 

_Call Sheet and Planning._ Refer to supplementary material document A for the call sheet and planning document for each rehearsal and performance. 

8 

Scientific **Data** | _(2025) 12:1421_ | https://doi.org/10.1038/s41597-025-05713-2 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

|**opals.sensor_name**|**Identifcation of subject and body part of sensor**|
|---|---|
|opals.srate|Scalar value indicating sampling rate of system (128 Hz)|
|opals.ts_tstamps|Unix timestamps in microseconds|
|opals.accel_calib|Nx3 matrix containing calibrated acceleration vector(x,y,z) from triaxial accelerometer at each time point<br>N (units: m/s<sup>2</sup>)|
|opals.ang_velo_calib|Nx3 matrix containing calibrated angular velocity vector(x,y,z) from triaxial gyroscope at each time point<br>N (units: rad/s)|
|opals.magn_fux_calib|Nx3 matrix containing calibrated magnetic fux vector(x,y,z) from triaxial magnetometer at each time point<br>N (units: microtesla)|
|opals.quarternion|Nx4 matrix containing orientation quarternion(q1,q2,q3,q4) at each time point N|
|opals.temperature|Nx1 vector containing temperature at each time point N (units: degrees Celsius)|
|opals.Tb2n|3×3xN tensor containing the transformation matrix to change the frame of reference from body to<br>navigation at each time point N|
|opals.accel_gravcomp|Nx3 matrix containing calibrated acceleration vector(x,y,z) that has had the efects of acceleration due to<br>gravity removed|



**Table 3.** Description of the fields contained within the _opals.mat file structure. 

|**empatica.sensor_location**|**Identifcation of subject and hand where sensor is located**|
|---|---|
|empatica.Accel|Nx3 matrix containing acceleration vector(x,y,z) from triaxial accelerometer at|
||each time point N (units: 1/64g)|
|empatica.Accel_tstamps|Nx1 vector containing unix timestamps in seconds at each time point N for acceleration data|
|empatica.Accel_srate|Scalar value indicating sampling rate of accelerometer (32 Hz)|
|empatica.BVP|Nx1 vector containing blood volume pulse vector from photoplethysmograph at each time point N<br>(no units given)|
|empatica.BVP_tstamps|Nx1 vector containing unix timestamps in seconds at each time point N for blood volume pulse data|
|empatica.BVP_srate|Scalar value indicating sampling rate of photoplethysmograph (64 Hz)|
|empatica.elec_dermal|Nx1 vector containing electrodermal activity vector from electrodermal activity sensor at each time<br>point N (units: microsiemens)|
|empatica.elec_dermal_tstamps|Nx1 vector containing unix timestamps in seconds at each time point N for electrodermal activity data|
|empatica.elec_dermal_srate|Scalar value indicating sampling rate of electrodermal activity sensor (4 Hz)|
|empatica.heart_rate|Nx1 vector containing heart rate vector extracted from BVP signal at each time point N|
|empatica.heart_rate_tstamps|Nx1 vector containing unix timestamps in seconds at each time point N for heart rate data|
|empatica.heart_rate_srate|Scalar value indicating sample rate of extracted heart rates (1 Hz)|
|empatica.temperature|Nx1 vector containing temperature at each time point N (units: degrees Celsius)|
|empatica.temperature_tstamps|Nx1 vector containing unix timestamps in seconds at each time point N for temperature data|
|empatica.temperature_srate|Scalar value indicating sampling rate of temperature sensor (4 Hz)|



**Table 4.** Description of the fields contained within the _empatica.mat file structure. 

_Annotation Script._ The six rehearsal videos and three performance videos were annotated in Microsoft Excel to provide an instant-by-instant account of the activities observed. These annotations facilitate the navigation and filtering of activities and events. The annotation format is also included in the public data repository mentioned in Data Records. To link the annotation file to the datasets, the multi-modal data was synchronized based on a shared timeline. This file includes a dedicated section specifying the data positions, defined as Segmentation, for the start and end of each annotated event. These positions refer to the exact sample numbers for each recorded modality, enabling precise identification and extraction of the corresponding segments from the raw data. This structure ensures a direct and consistent correspondence between the annotations and the dataset entries throughout the six rehearsals and three performances. 

## **technical Validation** 

**Data Synchronization.** The EEG, Empatica and OPALs data were synchronized with the rehearsal and performance video files. A four second subset of the time-synchronized data was chosen for further analysis, as shown in Fig. 8. During the experiment, the participants were asked to clap and clench their teeth at the same time. The research assistant added an event into the EEG data stream at the same time so that the claps could act as a marker for the start and end of the experiment. 

## **Usage Notes** 

All the datasets provided in this study consist of raw data. For data preprocessing and analysis, the authors recommend using MATLAB R2021a (The Mathworks Inc., Natick, MA) and/or EEGLAB<sup>9</sup> (https://sccn.ucsd.edu/ eeglab/index.php). De-noising algorithms have been suggested for identifying and removing both physiological and non-physiological artifacts from the EEG data, see Fig. 5. 

Scientific **Data** | _(2025) 12:1421_ | https://doi.org/10.1038/s41597-025-05713-2 

9 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



**Fig. 8** ( **a** ) A short sample of time-synchronized subset of raw EEG, EOG, ACC, and BVP data for Dyad B and one member of the audience during Performance. The timeseries EOGv (vertical) and EOGh (horizontal) are computed as bipolar signals for the vertical and horizontal EOG channels. **(b)** Dyad B during the performance in front of an audience. 

A key limitation of the dataset is the absence of audio in the video recordings. While audio was originally captured during data collection, it is not included in the shared dataset due to copyright restrictions<sup>7</sup> . Researchers intending to pursue audio-dependent analyses should be aware of this constraint. To maintain transparency, we have retained a description of the audio recording methodology in the Methods section, despite the unavailability of the audio files. 

## **Code availability** 

No custom code is needed to access the data. However, due to the large size and complexity of the datasets, opening the CSV files can be computationally intensive. We recommend using programming environments such as Python or MATLAB for accessing and analyzing the data, as Microsoft Excel may not efficiently handle the volume of information and could limit visualization capabilities. Based on internal testing, the time required to open individual CSV files ranged from approximately 12 minutes on a high-performance workstation (270 GB RAM, AMD®Ryzen Threadripper PRO 5975WX) to 50 minutes on a laptop (32 GB RAM and an Intel Core Ultra 9 processor). 

Received: 26 December 2024; Accepted: 29 July 2025; Published: xx xx xxxx 



<!-- Start of picture text -->
Published: xx xx xxxx<br><!-- End of picture text -->

## **References** 

> 1. Greaves, D. A. _et al_ . Exploring Theater Neuroscience: Using Wearable Functional Near-infrared Spectroscopy to Measure the Sense of Self and Interpersonal Coordination in Professional Actors. _Journal of Cognitive Neuroscience_ **34** , 2215–2236, https://doi.org/ 10.1162/jocn_a_01912 (2022). 

> 2. McDonald, B., Goldstein, T. & Kanske, P. Could Acting Training Improve Social Cognition and Emotional Control. _Frontiers in Human Neuroscience_ **14** , 1–5, https://doi.org/10.3389/fnhum.2020.00348 (2020). 

Scientific **Data** | _(2025) 12:1421_ | https://doi.org/10.1038/s41597-025-05713-2 

10 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

3. Brown, s., Cockett, P. & Yuan, Y. The neuroscience of Romeo and Juliet: an fMRI study of acting. _Royal Society Open Science_ **6** , 3, https://doi.org/10.1098/rsos.181908 (2019). 

4. Garbarino, M., Lai, M., Tognetti, S., Picard, R. & Bender, D. Empatica E3 - A wearable wireless multi-sensor device for real-time computerized biofeedback and data acquisition. _Proceedings of the 4th International Conference on Wireless Mobile Communication and Healthcare - Transforming healthcare through innovations in mobile and wireless technologies_ . 3–6, 2014. https://doi.org/10.4108/ icst.mobihealth.2014.257418 

5. Cruz-Garza, J. G. _et al_ . A novel experimental and analytical approach to the multimodal neural decoding of intent during social interaction in freely-behaving human infants. _Journal of Visualized Experiments: JoVE_ 104, https://doi.org/10.3791/53406 (2015). 

6. Marber, P. Closer. _Grove Press_ , 1999. 

7. Marber, P. Scene 11. In Closer. _Grove Press_ , 1999. 

8. Meisner, S., Longwell, D. & Pollack, S. Sanford Meisner on Acting. _Vintage Books_ , 1987. 

9. Delorme, A. & Makeig, S. EEGLAB: An open source toolbox for analysis of single-trial EEG dynamics including independent component analysis. _Journal of Neuroscience Methods_ **134** , 9–21, https://doi.org/10.1016/j.jneumeth.2003.10.009 (2004). 

10. Kilicarslan, A., Grossman, R. & Contreras-Vidal, J. L. A robust adaptive denoising framework for real-time artifact removal in scalp EEG measurements. _Journal of Neural Engineering_ **13** , 2, https://doi.org/10.1088/1741-2560/13/2/026013 (2016). 

11. Bigdely-Shamlo, N., Mullen, T., Kothe, C., Su, K. & Robbins, K. The PREP pipeline: Standardized preprocessing for large-scale EEG analysis. _Frontiers in Neuroinformatics_ **9** , 1–19, https://doi.org/10.3389/fninf.2015.00016 (2015). 

12. Kilicarslan, A. & Contreras-Vidal, J. L. Characterization and real-time removal of motion artifacts from EEG signals. _Journal of Neural Engineering_ **16** , 5, https://doi.org/10.1088/1741-2552/ab2b61 (2019). 

13. Kothe, C. A. E. & Jung, T. P. Artifact removal techniques with signal reconstruction. _Google Patents_ **11** , 417–441 (2016). 

14. Mullen, T. R. _et al_ . Real-time neuroimaging and cognitive monitoring using wearable dry EEG. _IEEE Transactions on Biomedical Engineering_ **62** , 2553–2567, https://doi.org/10.1109/TBME.2015.2481482 (2015). 

15. Lee, T. W., Girolami, M. & Sejnowski, T. J. Independent component analysis using an extended infomax algorithm for mixed subgaussian and supergaussian sources. _Neural computation_ **11** , 417–441, https://doi.org/10.1162/089976699300016719 (1999). 

16. Rejer, I. & Gorski, P.Benefits of ICA in the Case of a Few Channel EEG. _Proceedings of the Annual International Conference of the IEEE Engineering in Medicine and Biology Society, EMBS_ , 7434–7437, https://doi.org/10.1109/EMBC.2015.7320110 (2015) 

17. Baarsch, J. & Celebi, M. Investigation of internal validity measures for K-means clustering. _Proceedings of the International MultiConference of Engineers and Computer Scientists_ (2012). 

18. Hendry, M. F. _et al_ . Mobile Brain-Body Imaging and Visual Data of Theatrical Actors During Rehearsal and Performance. _FigShare_ Collection, https://doi.org/10.6084/m9.figshare.c.7271338.v4 (2024) 

## **acknowledgements** 

This research is partly supported by National Science Foundation (NSF) REU Award #1757949, NSF IUCRC BRAIN Site award #2137255, NSF AccelNet #2412731, and a research grant by the Zurich University of the Arts (ZHdK), Institute for the Performing Arts and Film, Zurich University of the Arts, Zurich, Switzerland. The authors would like to thank the University of Houston School of Theatre and Dance: Rachel Cendrick, Josh Rahman, Clare Keating, Sophie Mobbs, Tony Shortt, Leo Rojas, Olivia Swasey, Michael Duran, and Shelby Kesler for their insights in follow-up transdisciplinary discussions of the experiment. Students of the Jack J. Valenti School of Communications recorded the video data: Alexander Brovig, Guillermo Alán Cantú, Richard Davis, Devin Pruitt and Liana Rawley. At ZHdK, Prof. Anton Rey and Dr. Miriam Loertscher provided input for the experiment protocol, and Norbert Kottmann synchronized the audio/video data. Students at the Laboratory for Noninvasive Brain-Machine Interface Systems at the University of Houston assisted with logistics and data collection: Devon Bellman, Ryan Thankson, Kevin C. Nathan, Justin A. Brantley, Alexander Craik. Fangshi Zhu assisted with video data collection. 

## **author contributions** 

Manuel Flurin Hendry: Conceptualization, Methodology, Validation, Investigation, Data Curation, Writing - Review & Editing, Visualization, Supervision, Project administration. Jesus G. Cruz-Garza: Methodology, Software, Validation, Formal Analysis, Investigation, Data Curation, Visualization, Writing - Review & Editing. Esther A. Delgado-Jimenez: Software, Validation, Formal Analysis, Investigation, Data Curation, Visualization, Writing - Original Draft. Yoshua E. Lima Carmona: Software, Validation, Formal Analysis, Investigation, Data Curation, Visualization, Writing - Original Draft. Aime J. Aguilar-Herrera: Software, Validation, Formal Analysis, Investigation, Data Curation, Visualization, Writing - Review & Editing. Mauricio A. Ramirez-Moreno: Software, Validation, Formal Analysis, Investigation, Data Curation, Writing - Review & Editing. Akshay Sujatha Ravindran: Investigation, Writing - Review & Editing. Andrew Y. Paek: Investigation, Writing - Review & Editing. Michelle Smith: Investigation, Writing - Review & Editing. Julia Kan: Formal Analysis, Data Curation, Visualization, Writing - Review & Editing. Mikayla Fors: Formal Analysis, Data Curation, Writing - Review & Editing. Amirah Alam: Formal Analysis, Data Curation, Writing - Review & Editing. Ruofan Liu: Formal Analysis, Data Curation, Writing - Review & Editing. Adam Noble: Methodology, Writing - Review & Editing. Jose L. Contreras-Vidal: Conceptualization, Methodology, Software, Validation, Formal Analysis, Investigation, Resources, Data Curation, Writing - Review & Editing, Visualization, Supervision, Project administration, and Funding acquisition. 

## **Competing interests** 

The authors declare no competing interests. 

## **additional information** 

**Supplementary information** The online version contains supplementary material available at https://doi.org/ 10.1038/s41597-025-05713-2. 

**Correspondence** and requests for materials should be addressed to J.L.C.-V. 

**Reprints and permissions information** is available at www.nature.com/reprints. 

Scientific **Data** | _(2025) 12:1421_ | https://doi.org/10.1038/s41597-025-05713-2 

11 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

**Open Access** This article is licensed under a Creative Commons Attribution-NonCommercialNoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/. 

- © The Author(s) 2025 

Scientific **Data** | _(2025) 12:1421_ | https://doi.org/10.1038/s41597-025-05713-2 

12 

