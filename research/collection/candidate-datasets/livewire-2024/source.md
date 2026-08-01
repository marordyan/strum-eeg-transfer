# Neural Dynamics of Creative Movements During the Rehearsal and Performance of "LiveWire".

Source: Europe PMC (PMC11550816), doi 10.1038/s41597-024-04010-8

## Abstract

This report contains a description of physiological and motion data, recorded simultaneously and in synchrony using the hyperscanning method from two professional dancers using wireless mobile brain-body imaging (MoBI) technology during rehearsals and public performances of “LiveWire” - a new composition comprised of five choreographed music and dance sections inspired by neuroscience principles. Brain and ocular activity were measured using 28-channel scalp electroencephalography (EEG), and 4-channel electrooculography (EOG), respectively; and head motion was recorded using an inertial measurement unit (IMU) placed on the forehead of each dancer. Video recordings were obtained for each session to allow for tagging of physiological and motion signals and for behavioral analysis. Data recordings were collected from 10 sessions over a 4-month period, in which the dancers rehearsed or performed (in front of an audience) choreographed expressive movements. A detailed explanation of the experimental set-up, the steps carried out for data collection, and an explanation on the usage are provided in this report.

Subject terms: Cooperation, Social behaviour


## Background & Summary

Human creative expression represents a multidimensional and multistage process that cannot be carried out in an isolated state; on the contrary, it’s driven by environmental stimuli like sensory inputs, experiences, arrangements of ideas and other contextual factors that could play a role in a real-life scenario1. Dance, among its many dimensions (emotional, rhythmic, interactive), involves a creative process. This creative aspect is what makes it an art (rather than just a skilled physical activity), a series of self-generated, expressive body movements and gestures through a space and whose purpose is to be appreciated by an audience2. A comprehensive look at dance from a neuroscience perspective has led to the proposal that dance involves neurobehavioral processes in seven areas: sensory, motor, cognitive, social, emotional, rhythmic and creative3. All of these processes represent intrinsic human behaviors that are present since the early stages of human development, including, for example, the movement synchrony to musical rhythms that babies exhibit when hearing pleasurable sounds, and the natural human response of moving to a beat when listening to music, which leads to a positive affective state3,4.

Understanding the human creative process from a neural perspective has been of great interest to neuroscientists, and dance provides a window to study such process. Moreover, new tools and approaches for assaying and understanding the neural bases of creative processes have emerged making it now possible to study the performing arts in “action and in context” in public settings5,6. One of such tools is mobile brain-body imaging (MoBI) technology, which is usually composed by wearable, wireless, brain activity and motion sensors. This technology allows researchers to directly study human brain activity in the performing and visual arts within unconstrained, realistic and ecological settings, while also keeping track of the context through the use of video recordings and event markers1,6.

Recent advances in the neuroscience field have unveiled new opportunities to investigate the effects of complex sensory-motor activities, such as dance, on the brain dynamics and communication. In the study by Basso et al.3, the Synchronicity Hypothesis of Dance is introduced, this hypothesis points that humans engage in dance to enhance both intra- and inter-brain synchrony. According to this hypothesis, dance may facilitate the reorganization of oscillatory brain activity, potentially leading to significant clinical improvements in conditions such as autism spectrum disorder and other disorders associated with impairments in oscillatory activity.


## Methods


### Participants

Two healthy dancers (age: 32 ± 1 years, 1 male and 1 female), referred to as D1 and D2, provided informed consent for this study, as they were the ones instrumented. Additionally, a release form was obtained from each participant from the rest of the crew, allowing the use of audio and video recordings in a non-anonymized form. Therefore, the entire crew has granted permission for the use of sound and video footage.

By the time the experiments took place, the participants had in average 17.5 ± 2.5 years of dance experience, and 11 ± 1 years performing professionally. D1 holds a master of Fine Arts (MFA), her background is mainly in Concert dance and the main styles she trained have been Ballet and Modern, then she transitioned into Contemporary during her BFA. With regard to D2, his early dance training was in modern dance in Japan, which typically emphasizes ballet aesthetics and technique. Professionally, D2 has worked with modern/contemporary dance companies, contemporary ballet companies, and classical ballet companies. Both participants signed an agreement to the sharing of all data obtained during the experiment including data, images, audio and video. All the experimental methods from this study were approved by the Institutional Review Board of the University of Houston (UH IRB #15457-01: Your Brain on Dance).


### Instrumentation and data collection

In this study, scalp electroencephalogram (EEG) (28 channels, 1000 Hz), electrooculography (EOG) (4 channels, 1000 Hz) and inertial measurement unit (IMU) 128 Hz (3-axis accelerometer, gyrometer, and magnetometer) wireless recordings were obtained simultaneously and in synchrony for the two participants during their dance rehearsals and performances. EEG and EOG data were recorded using Brain Products actiCAP, BrainAmpDC amplifers and MOVE transmitters (Brain Products GmbH, Germany). Electrode distribution followed the 10-20 international system (Fp1, Fp2, F7, F3, Fz, F4, F8, FC5, FC1, FC2, FC6, C3, Cz, C4, CP5, CP1, CP2, CP6, P7, P3, Pz, P4, P8, PO9, O1, Oz, O2, PO10).

Continuing with the experimental setup, EOG electrodes were positioned on the right and left temples, and above and below the right eye to record horizontal and vertical eye movement respectively. Reference electrodes were placed on both earlobes, and impedance was set to less than 50 KΩ for all electrodes before starting the experiments. The IMU Opal sensor (APDM, Portland, OR) was affixed to the forehead of each dancer. This sensor recorded data at a sampling rate of 128 Hz. For consistency with the EEG recordings, which were sampled at 1000 Hz, the IMU data was resampled to 1000 Hz during offline preprocessing. This step ensured that the sampling frequencies of the EEG and IMU data matched, facilitating the analysis.

Figure 1b) shows the setup of the equipment used in this work for both dancers. Manual triggers were used to synchronize EEG, EOG and IMU data. Rehearsals and performance sessions were video recorded for further analysis. Additionally, two Source Four LED series 2 Lust (ETC, Wisconsin) were used together with a DMX USB PRO (ENTTEC, Durham, NC) interface for real time brain to brain (B2B) synchrony-enabled light control during some rehearsals and the performances. Tables 1, 2 and 3 shows the organization of files containing data and markers from EEG, EOG and IMU respectively within the database, from all recordings.


[fig] Fig. 1 Visual summary of Data acquisition and Experimental protocol. (a) Pre and post calibration recording (EO, EC and IC) were carried out before and after each performance respectively. (b) MoBI instrumentation on the dancers, comprised by EEG, EOG and IMU. From right to left: D1 (female), D2 (male). (c) EEG electrode distribution used, following the 10-20 international system. (d) Timeline of LiveWire perfomance, each section was inspired by a neuroscience principle (stated under each section). All images have the consent of those depicted to be openly published.


[table-wrap] Table 1 Contents of EEG structure inside -Rehearsal/Performance_MMDDYY.mat/csv file.

| Rehearsal/Performance_MMDDYY.Dancerx.EEG.Dx_EEG | 28 × N matrix that contains the EEG data of the rehearsal/performance (28 EEG channels × N samples) |
| Rehearsal/Performance_MMDDYY.Dancerx.EEG.EEG_marker_times | 1 × 7 vector that contains the EEG triggers that notice when each section of the performance starts. |
| Rehearsal/Performance_MMDDYY.Dancerx.EEG.calibration_EEG_Dx | 28 × N matrix that contains the EEG calibration data (28 EEG channels × N samples) |
| Rehearsal/Performance_MMDDYY.Dancerx.EEG.Chanlocs | 1 × 28 struct that contains the spatial information about the EEG channels |


[table-wrap] Table 2 Contents of EOG structure inside -Rehearsal/Performance_MMDDYY.mat/csv file.

| Rehearsal/Performance_MMDDYY.Dancerx.EOG.Dx_EOG | 4 × N matrix that contains the EOG data of the rehearsal/performance (4 EOG channels × N samples) |
| Rehearsal Performance_MMDDYY.Dancerx.EOG.EOG_marker_times | 1 × 7 vector that contains the EOG triggers that notice when each section of the performance starts. |
| Rehearsal/Performance_MMDDYY.Dancerx.EOG.calibration_EOG_Dx | 4 × N matrix that contains the EOG calibration data (4 EOG channels × N samples) |
| Rehearsal/Performance_MMDDYY.Dancerx.EOG.Channels | 4 × 2 string that contains the information about the channels |


[table-wrap] Table 3 Contents of IMU structure in -IMU file.

| Rehearsal/Performance_MMDDYY.IMU | 1 × 3 structure that contains data from the accelerometer, gyroscope and magnetometer |
| Rehearsal Performance_MMDDYY.Dancerx.IMU.IMU_Triggers | 1 × 7 vector that contains the IMU triggers that notice when each section of the performance starts. |


### Experimental protocol

In every session, an eyes open (EO) followed by eyes closed (EC) 60-second conditions, as well as electrode impedance measurements, were recorded at the start and end of each rehearsal and performance. Then, dancers rehearsed/performed a 28-minute choreography entitled “LiveWire”, which is divided into 5 sections7. Each section of LiveWire was inspired by a different neuroscience concept. The first section represents the unconscious, automated sub-routines that underlie our contact with the world, as well as the ways sensory data is processed in different parts of the brain8. After a brief introduction, a musical motive represents a short neurological “signal” that behaves in controlled and predictable ways. The dance is both a visual representation of the music and the neuroscience concept. The lead dancer (wearing the brain cap) represents the sensory data and performs short movement phrases. The three subsequent dancers behind, perform only compartmentalized aspects of the movement (arms, torso, legs) and represent the sensory data being disseminated and stored in different areas of the brain. The second section (3 minutes) illustrates repetition suppression, in which our brain pays less and less attention to a stimulus that is repetitive or predictable9. Two contrasting musical ideas-one lyrical, the other aggressive-alternate and, as they become familiar, eventually wear down and fade out. The dance used the metaphor of a marital argument to demonstrate repetition suppression. Each musical outburst is matched by the male dancer. As the dance proceeds, the conflict between the duet slowly resolves. The third section (2.5 min), evokes the internal model of reality that our brain constructs, while monitoring the world for updates10. A recurring musical phrase represents the stability of the internal model. Suddenly, an incongruous cello solo disrupts that consistency. A reminiscence of the cello solo is then folded into the quartet’s recurring statement. The two dancers wearing brain caps demonstrate the inherent conflict between the internal and external model of reality. One dancer performs outwardly with occasional pauses to recalibrate and respond to what the internal dancer is doing. Eventually the dancers come into sync and perform in unison. The fourth section (8 minutes) uses a musical theme and variations to illustrate the serial order effect, in which derivations of an idea tend to get wilder and stranger as time passes11. The movement demonstrates a motive and quickly evolves into more complex movement choices that hold remnants of the original phrase. The final section (8 minutes) represents the dynamism of thought, in which various needs and desires compete for conscious attention. Musically, this movement has the most spontaneous unfolding, alternating and intertwining various themes12. The final section of the dance is a structured improvisation, allowing dancers agency to respond to their environment. This section demonstrates the capability of the brain to self-organize in real time to generate creative movements in response to the dancer’s internal states and the external world surrounding the dancer. The participants completed a total of 7 rehearsals and three performances of this choreography (and experimental protocol).


## Data Records

The dataset is hosted on FigShare (https://figshare.com) under the terms of the Attribution 4.0 International Creative Commons License (http://creativecommons.org/licenses/by/4.0/). The files are primarily organized by the day (session) they were collected, and are categorized by whether the session was a rehearsal or a performance (10.6084/m9.figshare.c.6274752).13 Every day of recording was archived in a single file. mat/csv and organized with the following naming convention:


### Rehearsal_MMDDYY.mat/csv or Performance_MMDDYY.mat/csv

Where MMDDYY represents the month, day and year respectively, in which each recording took place. The Rehearsal_MMDDYY.mat/csv or Performance_MMDDYY.mat/csv13 contain two structures, the first one includes all the data collected from D1 (Dancer 1 structure), and the second corresponds to the data collected from D2 (Dancer 2 structure).


### Dancer 1 and Dancer 2 structures

Inside Dancer 1 structure, three structures can be found, the first one contains data collected from EEG (EEG structure), the second one from EOG (EOG structure) and the third from IMU (IMU structure). This same organization can be found inside the Dancer 2 structure. Inside each of these files, the next structures can be found:


### EEG structure

The EEG structure includes the EEG data from the participants (D1_EEG/D2_EEG). In this file, EEG data from the 28 channels can be found. EEG_marker_times contains the markers’ times in which each section from the rehearsal/performance started. The calibration data (calibration_EEG _D1/calibration_EEG_D2) includes two minutes of EEG signals recorded in the pre-calibration EO and EC blocks. The Chanlocs variable (Chanlocs) provides the spatial locations of the EEG channels (Table 1).


### EOG structure

The EOG structure contains the EOG data from the participants (D1_EOG/D2_EOG). In this file, EOG data from 4 channels can be found. Channels 1 and 2 correspond to vertical EOG up (VEOGU) and down (VEOGD), and channels 3 and 4 to horizontal EOG left (HEOGL) and right (HEOGR) respectively. This organization description can also be found in this EOG file inside Channels. The EOG marker times (EOG_marker_times) has the same purpose as the one inside the EEG structure, and has the same information. Calibration data (calibration_EOG_D1/calibration_EOG_D2) includes two minutes of EOG signals corresponding to the pre-calibration EO and EC blocks (Table 2).


### IMU structure

The IMU structure can be found inside each participant’s main file, the path to access this data is shown in Table 3. The data in this file includes a 1 × 3 IMU structure where the first cell contains the acceleration data collected from the IMU recording. Acceleration data is composed of three columns, representing acceleration in x, y and z axes respectively. Going back to the IMU structure, the second cell in the structure corresponds to the data coming from the gyroscope, with three columns that represent the x, y and z axis from the recording respectively. The third cell on IMU contains the data recorded from the magnetometer, similarly with three columns to represent three-axial data. The IMU triggers (IMU_Triggers) are the markers in which each section from the rehearsal or the performance started, in 128 Hz sampling rate.


### Video records

The corresponding video recordings for each day are also situated in the Brain on Dance collection with the following structure: “VID_MM_DD_YY_X.mp4”, where MM, DD, and YY correspond to the month, day and year in which the video was recorded (Table 4). The last character X is either an “R” or “P” for rehearsal or performance respectively. Due to technical difficulties, there are two missing video recordings (January 22nd and April 9th).


[table-wrap] Table 4 Contents of video recordings in .mp4 files.

| VID_MM_DD_YY_X.mp4 | 24 frames per second video for each dance performance and rehearsal containing the 5 choreographic sections |


## Technical Validation


### Data synchronization

The data files shared contain data from different devices, consisting of the EEG recording device, IMU recording device, and video recording device. In order to properly synchronize this data, external hardware was required. This hardware consisted of a custom trigger-button electronic box connected to the EEG and IMU recording devices. Using this trigger, digital pulses were placed manually to mark the data on the beginning of each section of the choreography. Regarding the synchronization with the video, the timestamps provided by the video recording allowed to synchronize the events with the trigger device. The (raw) data files provided in the data-set are aligned to these triggers in order to allow the users to process and analyze as needed. Figure 2a shows a representative 25-second block of synchronized EOG, EEG, and head acceleration signals, for each dancer, from section 1 of the performance of January 21st of both dancers.


[fig] Fig. 2 Time-synchronized subset of EOG, EEG, and motion data; Channel impedances (KΩ) of the 28-channel EEG. (a) shows the time series from EOGH (horizontal), EOGV (vertical), and some representative channels from the 28-channel EEG and IMU data for 25 seconds of the recording from section 4. (b) Impedance values (KΩ) of the 28-channel EEG for each of the two dancers prior to the beginning of the experiment and at the end for the 10 data set recordings from the rehearsals and performances.


### Electrode impedance data

The impedance check (IC) blocks during pre and post calibration were carried out to ensure a good quality of EEG/EOG recordings and to track possible changes in electrode impedance during the rehearsals and performances. For each EEG/EOG electrode, the researcher monitored the impedance value and worked the syringe with the gel to target a maximum impedance value of 50 KΩ prior to start the experiment. Figure 2b depicts the electrode impedance values obtained during pre- and post calibration for four different days, of D1 and D2. Table 5 shows the organization of electrode impedance data in the database, from all recordings.


[table-wrap] Table 5 Contents inside the impedance.mat/csv files.

| Impedance.IMP_MMDDYY.EEG_IMP | 28 × 5 table that contains in the first column the names of the 28 EEG channels used and on the other 4 columns can the impedance values obtained from preand post calibration impedance values from both dancers. |
| Impedance.IMP_MMDDYY.EOG_IMP | 4 × 5 table containing in the fist column the names of the 4 EOG channels, and in the other 4 columns it can be found the pre and post calibrationimpedance values from the EOG channels from both dancers. |


## Usage Notes

All the datasets provided in this paper are raw data. To process the data, the authors recommend using MATLAB R2021a (MathWorks, MA)14 and/or the MATLAB toolbox EEGLAB15 for processing and analysis of the multimodal data. De-noising algorithms have been proposed for identifying and removing physiological and non-physiological artifacts, including motion artifacts from the EEG data16–18.


## Acknowledgements

This research is partly supported by NSf IUCRC BRAIN Award #2137255 at the University of Houston and the NSF AccelNet #2412731. The authors would like to acknowledge the NEA Research Lab at Rice University, the IUCRC BRAIN International Affiliate Site at Tecnologico de Monterrey, along with the Shepherd School of Music at Rice University, the Musiqa String Quartet and the NobleMotion Dance Company. We would like to thank Rachel Culver, LaRodney Freeman, Shohei Iwahama, Colette Kerwick, Lindsey McGill, Tyler Orcutt, Abigail Schafer, Lauren Serrano and Evelyn Toh dancers from the NobleMotion Dance Company, we thank Bryan Ealey, Emily Fens, Pierre Jalbert, Bree Ahern, Evie Chen, Jacob Schafer and Sebastian Stefanovic as part of the music and lighting team from the Musiqa String Quartet.


## Author contributions

A.B., J.L.C.V., A.N., and D.N. conceived the idea for this project. A.B. wrote the music, A.N. and D.N. choreographed the dance, J.L.C.V. directed the neuroengineering component of the project, M.A.R.M., K.K. and N.R. carried out the data collection, M.A.P.R., M.A.R.M. and D.H. wrote the manuscript of this data descriptor. All authors reviewed and edited the manuscript.


## Code availability

No custom code is needed to access the data.


## Competing interests

The authors declare no competing interests.


## Footnotes

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.


## Contributor Information

Maxine Annel Pacheco-Ramírez, Email: mpachec4@cougarnet.uh.edu.

Jose L. Contreras-Vidal, Email: jlcontreras-vidal@uh.edu


## References


## Associated Data


### Data Availability Statement

No custom code is needed to access the data.
