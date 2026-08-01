2018 IEEE International Conference on Systems, Man, and Cybernetics 

# STRUM: A new Dataset for Neuroergonomics Research 

Christian A. Kothe _Intheon Labs Intheon_ San Diego, CA, USA christian.kothe@intheon.io 

Tim R. Mullen _Intheon Labs Intheon_ San Diego, CA, USA tim.mullen@intheon.io 

Scott Makeig _Swartz Center for Compuational Neuroscience Institute for Neural Computation_ La Jolla, CA, USA smakeig@ucsd.edu 

**_Abstract_ — The past decade has seen a gradual expansion of Brain-Computer Interface applications from their clinical roots into entertainment, automotive, workplace, and military domains. However, many of these new-found applications have yet to pass the prototype stage, among others due to challenges posed by real-world data noise levels and increased context variability and complexity. Tackling these challenges requires sufficiently realistic and rich datasets that allow for benchmarking competing approaches, and in this paper, we present a task battery modeled after a complex real-world scenario, together with a new open dataset for BCI research. Results from an exemplary analysis of a slice of this large trove of data are presented, and it is found that the data mirror some of the challenges encountered in real-world deployments, with various well-known BCI algorithms showing a pronounced performance differential to highly simplified lab experiments. The results also show significant performance differences among alternative methods, indicating possible trajectories for future improvements BCI methodology applied to complex real-world contexts.** 

**_Keywords—neuroergonomics, passive BCI, benchmark, dataset, experiment design_** 

## I. INTRODUCTION 

Over the past decade, numerous new applications have been found for Brain-Computer Interfaces (BCIs) outside their original field of use in clinical or rehabilitative settings [1][2]. Major thrusts along these lines have been workplace applications [3], such as driver state monitoring [4], workplace environments and entertainment [5], or military use [6]. However, BCI technology for these applications has yet to fully transition out of the lab, for reasons such as signal variability [7], depending on the type of environment, increased noise [8]. Against this background, the Cognition and Neuroergonomics Collaborative Technology Alliance (CaN CTA), a US-led research programme in Neuroergonomics, has recognized a need for publicly available datasets facilitating the development and benchmarking of BCI methods on complex, multi-faceted, and realistic tasks. Here 

Research was sponsored by the Army Research Laboratory and was accomplished under Cooperative Agreement Number W911NF-10-2-0022 (CAST 076910227001).  The views and the conclusions contained in this document are those of the authors and should not be interpreted as representing the official policies, either expressed or implied, of the Army Research Laboratory or the U.S Government.  The U.S Government is authorized to reproduce and distribute reprints for Government purposes notwithstanding any copyright notation herein. 

we present one of three large-scale datasets that were collected under the CaN CTA to address this need. In the following we summarize the task design (source code available at [9]) and data collection procedure, and then we describe an exemplary analysis on the resulting dataset. We illustrate both the challenges and opportunities opened by this new data corpus. 

## II. EXPERIMENTAL TASK 

## _A. Overview_ 

The task battery underlying this experiment was designed around a controlled but rich collection of subtasks, consisting of a sequence of foreground activities along with parallel side tasks. The experiment is loosely modeled after workloads encountered by operators of complex multi-display consoles such as those used in military vehicles (crew stations), although the stimulus material used here (graphics, sounds, text, and speech) was chosen to be generic and video game like. The task can be configured for one or two subjects, and data was collected with pairs of subjects. Note that, due to the complexity and richness of the task, some details of the design are beyond the scope of this paper and will be presented in a future article. 

## _B. Cognitive Processes of Interest_ 

The experiment is designed to elicit a variety of controlled cognitive processes in the subject, including perception, memory retrieval, decision-making, and response. The goal is to enable extensive post-hoc analysis to help answer diverse scientific questions relating to brain and behavioral states under complex settings, as well as to performance of various types of passive BCIs [10] in such scenarios. Due to its multi-task nature, the paradigm puts heavy emphasis on selective attention in visual and auditory domains. Also, throughout the experiment, task load, fatigue, and attention distribution are expected to vary, and individual tasks are designed to elicit frequent perceptual and response errors. To maximize the utility of the data, events are recorded in great detail and described using an ontology extended from the HED 1.0 event marker specification [11]. 

## _C. Spatial Layout_ 

The laboratory space, which includes two identical seats for the subjects, each equipped with three vertically mounted 

2577-1655/18/$31.00 ©2018 IEEE DOI 10.1109/SMC.2018.00023 

77 

Authorized licensed use limited to: Univ of  Calif San Diego. Downloaded on August 01,2026 at 18:08:31 UTC from IEEE Xplore.  Restrictions apply. 

16:9 24” touch-screen monitors is depicted in Fig. 1. The graphical layout of on-screen content, shown in Fig. 2, is as follows. The center screen holds a virtual camera viewport showing the view of a virtual robot/drone controlled by the subject; the current foreground activity largely plays out in this view. The side screens are reserved for side tasks, including two auditory tasks (represented by yellow rounded rectangles), a comm chatter task (large black text message display to the left) on the left screen, and a satellite map task (right overhead view with attached black text message display area). Touchscreen response buttons related to the side tasks are at the bottom of the respective screens. The white frame around the right yellow rectangle indicates that this side task is currently active. The virtual world displayed in the two viewports is a procedurally generated city that is traversed by each subject using virtual robot/drone controlled with a gamepad. 



Fig. 1. Laboratory space for data collection, showing seats and associated displays and loudspeakers for audio-visual stimulus presentation. 

## _D. Task Timeline_ 

The task breaks down into a pseudo-random sequence of foreground activities (balanced for repetition, difficulty, and activity type) organized into 5 blocks of 4-6 activities each, with 10-20 second long pauses between blocks during which no foreground activity is scheduled. The overall experiment takes ca. 3.5 hours to maximize the amount of data collected per subject, and also to induce a moderate degree of fatigue. Side tasks are displayed at all times (with two exceptions where a conflict with a specific foreground activity would occur), but only at most 2 tasks are “active” at any given time. The active set, that is, side tasks that subjects are instructed to interact with, changes on an pseudo-random schedule every 60120 seconds. Active-set changes are indicated audio-visually to the subject. 

## _E. Task Concurrency_ 

Side tasks progress pseudo-randomly and independently of each other to minimize statistical confounds so as to allow each task to be analyzed individually while treating the other tasks as background distractor activity. The sole form of coupling between side tasks is that a stimulus is not presented when it falls into a time window during which an ambiguity with another task would arise if the stimulus were presented in its 

given modality. The effect of this is designed to be indistinguishable from a randomly drawn long inter-stimulus interval. 



Fig. 2. Graphical arrangement the on-screen content. Note: a “skip” button was added to the right of the 3x2 grid of response buttons in the bottom left, mirroring the layout on the bottom right, and the buttons have been changed to [left, right, back], and [yes, no, report]. 

## _F. Scoring and Reward Mechanisms_ 

To maximize engagement, performance scores are tracked for each side task (green bars in Fig. 2) as well as overall (topmost green bar). The subject’s actions are rewarded/penalized with typically +2 points for correct, -2 for incorrect, -1 for skipped, and -2 for missed, along with audiovisual cues (floating numbers and “ding” or “beep” sounds). Subject bonus pay was dependent on final score (capped at $20). 

## _G. Side Tasks_ 

The side tasks in this experiment are broken down by stimulus modality (auditory/visual) and stimulus kind (verbal/non-verbal), yielding a matrix of four tasks, plus one additional task with natural visual stimuli. The common substrate of all tasks is a sequence of stimuli, of which a fraction is followed by a query to classify the preceding stimulus (which is at this point no longer displayed). The queries in each task are of the same modality and kind as the task’s stimuli. Queries require subjects to choose between two and four alternative choices, depending on task type, with an additional “skip” response option. Subjects are required to respond either via touch-screen button press, or by voice command (realized using speech recognition), and to switch between the two modes of response in a self-paced manner (a penalty applies for more than 15 successive uses of the same response modality). Inter-stimulus intervals, stimulus type, appearance of queries, type of query, and query latency are drawn pseudo-randomly for each trial from distributions specific to the side task. 

_Visual/Nonverbal Task (“Satellite Map”)_ In this task, the stimulus set are icons of various types (e.g., house, packet) and four different colors that appear for a short time in a random location of the overhead map. The subsequent query can probe either the color of the preceding stimulus, or the quadrant in which the stimulus appeared, which is indicated by the 

78 

Authorized licensed use limited to: Univ of  Calif San Diego. Downloaded on August 01,2026 at 18:08:31 UTC from IEEE Xplore.  Restrictions apply. 

corresponding row of response buttons flashing repeatedly. See also Fig. 3 (right) for the response buttons corresponding to this task. To minimize ambiguity, stimuli do not appear close to quadrant boundaries. 



Fig. 3. (left) A blue icon appears on the satellite map in the east quadrant. (right) Responding to a query for the quadrant in which the icon appeared, the subject responds with ‘east’. 

_Auditory/Nonverbal Task (“Sounds”)_ This task utilizes a stimulus set of several types of sounds (e.g., car horn, motorcycle roar) that are presented from one of three directions (left, right, back). A single query stimulus (a distinctive “whoop” sound) prompts subjects to indicate the direction of the preceding sounds. The bottom right button bar is used for tactile responses. 

_Visual/Verbal Task (“Text Comms”)_ The shared feature of the two verbal tasks is that the stimulus set is a collection of ca. 200 non-repeating statement sentences, with yes/no questions matched to the preceding statements used as queries. An example stimulus/query pairing is “This weekend the Giants won by 4 to 2.” / “Were the Giants successful this time?”. To more realistically model communications chatter, statements and queries are prefixed by call-signs (e.g., Delta or Echo), and a majority of statements and queries are identified as distractors by means of having a call-sign different from the one given to the subject at the beginning of the experiment. In the visual variant of this task, statements and queries each appear as single lines in text message box as in Fig. 4. 



Fig. 4. Example of a text message query in the text communications task, to be acknowledged with “yes”, “no”, or “skip”. 

_Auditory/Verbal Task (“Audio Comms”)_ This task differs from the Text Comms task in that the stimuli and queries are pre-recorded sentences from four different human speakers that are presented acoustically. All other parameters of the task match those in the Text Comms task. 

_Visual/Natural Task (“Curbside Items”)_ The stimuli of this task are various objects (e.g., office chair, tire stack, trash can) procedurally placed on the curbs of the 3d world and shown in the central viewport. See Fig. 5 for an example. Stimuli appear naturally as a result of the subject driving past these objects. The query is generally of the form “what was the side of the last <object>?”, and refers to the street side (“left” or “right”) at which an object of the respective type has most recently gone out of view. Queries only appear if the situation is unambiguous based on multiple criteria. 



Fig. 5. Example of a stimulus in the Curbsite Items task, here a chair indicated by the red circle (red circle not displayed in the experiment). 

_Sporadic Interferences_ While not strictly side tasks, the experiment involves two sporadic interferences: (1) a warning light that occasionally turns red, prompting a button-press response by the subject with a high penalty for failure to respond in time and (2) a randomly triggered 45 to 75 second long “high stakes” period in which all penalties and rewards are multiplied by 4, which is indicated by the background color of the screen fading to dark red. 

## _H. Foreground Activities_ 

The foreground activities model a diverse set of tasks with high demands for attention that subjects may be engaged in while they are simultaneously asked to perform the aforementioned side tasks. These activities are implemented similar to short-term “objectives” in an open-world video game, and are generated procedurally and transition seamlessly without loading screens or “teleporting” the player to a new location. The center text box is used to present instructions pertaining to the currently scheduled activity. 

_Spotting Nearby Drones_ In this activity the subject is stationary but is able to rotate (pan) their stimulated vehicle’s camera in a full 360 degree circle. The objective is to report or mark, via gamepad button press, any quadcopter drones that are passing through the area that is visible from the player’s location. Penalties apply for double-reporting or not reporting a given drone. 

79 

Authorized licensed use limited to: Univ of  Calif San Diego. Downloaded on August 01,2026 at 18:08:31 UTC from IEEE Xplore.  Restrictions apply. 

_Individual Driving_ The subject is asked to drive their robot through a sequence of checkpoints placed procedurally throughout the city. The next checkpoint is visually indicated by a star in the overhead map and a floating 2x2 meter 3d icon at the target location. There is a penalty for time spent in this activity by means of a periodic point deduction. 

_Cooperative Driving_ In this activity, both subjects are asked to drive through a series of checkpoints together while also staying within 15 meters of each other at all times. 

_Aerial Guidance_ In this asymmetric cooperative activity, one subject is asked to drive through a sequence of checkpoints without an overhead map or visual directions, while the other subject is equipped with an overhead map and a virtual drone with flight characteristics similar to current-generation consumer drones, and is asked to guide their partner through the checkpoint. 

_Securing the Perimeter_ In this cooperative activity the objective is to secure the perimeter around a truck positioned in the city by warning off inbound other drones by means of pressing a gamepad button while the other drone is in the field of view, causing it to temporarily retreat. Penalties apply for other drones having prolonged line-of-sight to either the truck or to one’s own back. These scoring conditions combine to encourage subjects to cooperate effectively. 

## III. DATA COLLECTION 

The STRUM dataset<sup>1</sup> (“Small Team Reconnaissance Urban Missions”) comprises data collected from 56 participants (28 pairs) under UCSD IRB approval (3 datasets were excluded due to interruptions in the experiment). Subjects were UCSD students (13 f, 49 m) with a mean age of 20.3 +/- 2.3 years. For each subject, the following sensors were utilized: a 206channel EEG montage (24-bit BioSemi amplifier, 2048 Hz resampled to 512 Hz), plus 43-channel EMG neckband, 2- channel ECG, 2-channel EOG, and 16-channel respiration belt on the same amplifier, as well as a Logitech desk microphone, an instrumented Xbox 360 game controller, two cameras (one face view, one rear view), one AMTI force plate, one custom head-mounted eye tracker and head-mounted scene camera. Hand and head positions were tracked using a room-scale PhaseSpace motion-capture system with 480 Hz sampling rate. Time synchronization was done using the Lab Streaming Layer [12]. The data for each two-participant session were recorded into a single time-synchronized file in XDF format [13]. 

## IV. DATA ANALYSIS 

Due to the rich collection of tasks in this dataset, as well as the many recorded measures, we expect most future analyses to focus on a slice of the data, for instance one side task, or one experimental manipulation, or one type of event-related process. In line with this, we present here two sample data analyses of different cognitive processes: we investigate (1) EEG event-related potentials (ERPs) of response errors, and (2) EEG oscillatory processes related to task performance over extended periods of time. We approach the data with the intent 

to model the performance of a passive BCI [10], and thus we cast each problem as that of predicting a binary cognitive state from a segment of EEG (correct vs. incorrect response and low vs. high performance). In the style of a benchmark, we quantify the attainable performance of several well-known BCI methods on these data when trained on a single subject using blockwise cross-validation (CV) matched to the 5-block structure of the session with area under the receiver operator curve (Az) as the performance metric. For hyper-parameter optimization we use a nested blockwise CV. Significance testing is done using t- tests. 

All methods were implemented in BCILAB [14]. For computational expediency, the 205-channel EEG was subsampled to a subset of 64 approximately equidistant channels and the signal was resampled to 128 Hz with the resample routine in MATLAB (The Mathworks). 

## _A. Response Error Detection_ 

For detection of response errors from EEG, we compare all methods on the same EEG time windows of -0.2 to +0.8 seconds relative to the button-press response to queries in any of the five side tasks. We compare the following methods: 

_1)_ The ERP method with shrinkage LDA (sLDA) proposed in [15], a FIR low-pass filter with a transition band of 14-16 Hz other parameters as in BCILAB, resampling to 100Hz, and seven 50ms time windows covering 250ms-600ms after the event (similar to [16]). 

_2)_ A variant of the Hierarchical Discriminant Component Analysis (HDCA) method proposed in [17] using the same time windows, FIR filter, and resampling as (1), and also using the same sLDA estimator as in (1) for the regressions. 

_3)_ The dual-spectral regularized logistic regression (DSLR) method proposed in [18], with data further resampled to 60 Hz. The regularization parameter was searched over the range {2^4, 2^3.75, 2^3.5, …, 2^-3}. 

## _B. Task performance over Time_ 

For estimation of task performance from EEG, we compare all methods on the same EEG time windows of 8 seconds length, overlapped by 3 seconds, and  excluding windows between blocks. Ground-truth high and low performance states were constructed from response event markers by applying Gaussian kernel smoothing [19] to the point-process data to obtain smooth time-varying estimates of the probability of the user committing an error at a given time. The probability for each window was thresholded at below 40% and above 60% respectively to arrive at binary high/low performance classes. We compare the following methods: 

_1)_ The well-known Common Spatial Pattern (CSP) algorithm as in [20], using 3 pairs of filters, applied to data that has been bandpass filtered to the 7-30 Hz band using a minimum-phase FIR filter and resampled to 100 Hz. 

_2)_ A variant of CSP with diagonal-loading (shrinkage) regularization (DLCSPcv), where the regularization parameter was searched via cross-validation (cv) over the interval {0, 

1 Available from http://headit.ucsd.edu/ 

80 

Authorized licensed use limited to: Univ of  Calif San Diego. Downloaded on August 01,2026 at 18:08:31 UTC from IEEE Xplore.  Restrictions apply. 

0.1, …, 0.9}, as in [21] and otherwise using the same parameters as (1). 

3) The Spectrally weighted Common Spatial Pattern (Spec-CSP) algorithm [22], applied to a signal band-pass filtered to 7-33 Hz using a minimum-phase FIR filter and resampled to 100 Hz, and using a 7-30Hz hard spectral prior, with parameters p’ and q’ set to 0 and 1, respectively, and 3 spatio-spectral iterations (these parameters closely match the setup in Tomioka et al.). 

4) A variant of the Filter-Bank Common Spatial Pattern (FBCSP) algorithm [23], using frequency bands of 4-7 Hz, 8- 12 Hz, 13-30 Hz, and 31-42 Hz, respectively, resampling to 200 Hz, and using a feature-selecting elastic-net regularized logistic regression as in [14] with alpha parameter fixed at ½ and the lambda parameter searched over the regularization path using GLMNET [24]. 

## V. RESULTS 

_Response Error Detection_ In this task, all tested methods performed significantly above chance level (0.5 Az). Marked differences were seen between individual methods on the same data, with the DSLR method leading the comparison with an Az of 0.75 +/- 0.13, and the plain LDA method trailing with an Az of 0.63 +/- 0.07. HDCA reached an intermediate Az of 0.71 +/- 0.10. Differences between DSLR the other two methods were highly significant at p<0.01. Of note, the highestperforming methods prominently depend on artifactual EEG sources, specifically frontal patterns typical for eye activity for some subjects as can be seen Fig. 6, and temporal-lobe patterns typical of muscle activity for some other subjects (not shown). 

of 0.56 +/- 0.07 and 0.59 +/- 0.07, respectively. All scores are above the chance level of 0.5 at p<0.01. However, only the difference between DLCSPcv and CSP was significant at p<0.05. In contrast to the Response error predictors, task performance predictive models depend on spatial patterns localizable to neocortical locations, as seen in Fig. 7, including typical bilateral and unilateral occipital components with clear dipolarity which were associated with ca. 10 Hz alpha oscillations (bottom row). Other components picked up bilateral frontal beta activity (top row, left plot). 





Fig. 7. Subset of spatio-spectral patterns for two exemplary subjects (top and bottom row, respectively) as used for predicting task performance over time from EEG. Line plots show frequency weightings and scalp maps show associated spatial patterns (spatial filter inverses). 

## VI. DISCUSSION 



Fig. 6. Three spatio-temporal components of a DSLR classifier; line plots show weighting across time relative to button press (at time point 0) and scalp maps show associated spatial patterns (spatial filter inverses) modulated by the weighting, exhibiting prominent frontal features. 

_Task Performance over Time_ In the task performance estimation problem, predictive performance Az scores ranges from 0.55 +/- 0.06 for plain CSP to 0.61 +/- 0.08 for the DLCSPcv method. Spec-CSP and FBCSP resulted in Az scores 

The results show that there is information in the EEG about both cognitive variables, allowing for better-than-chance prediction accuracies. In some cases, the measures can plausibly be employed for real-world uses, e.g., when combined with other measures. However, as can be seen, the accuracies attained with the tested methods are below the levels expected from simplified laboratory experiments (e.g., [10, 16]), which is likely due to a confluence of increased task variability, noise caused by artifacts during task performance, and divided attention of the subject. This indicates a need for further work on methods that can operate under such settings, such as robust signal processing and statistics. It should be noted that the complexity of the STRUM task holds potential pitfalls, such as, for instance, artifacts that may be correlated with user state, and which may be mistaken for brain signatures, as mentioned in the case of response errors. 

## VII. CONCLUSION 

We have presented a dataset of simulated multi-tasking behavior in a setting that model  real-world scenarios in terms of complexity, variety of participant behaviors, noise and artifacts. In combination with the fairly high degree of realism, the detailed multi-modal instrumentation, and the size of the dataset, these data open up an unprecedented window in brain/body dynamics associated with task performance in relevant settings. As such, the data are expected to serve as a testbench for a wide range of BCI methods, which we hope 

81 

Authorized licensed use limited to: Univ of  Calif San Diego. Downloaded on August 01,2026 at 18:08:31 UTC from IEEE Xplore.  Restrictions apply. 

will yield valuable insight into subject behavior and failure modes in simulated realistic settings. 

## ACKNOWLEDGMENT 

We thank Jason Metcalfe, and Stephen Gordon from DCS Corp. and Marissa Westerfield for input during the experiment design, Matthew Grivich for heroic efforts during experiment setup, as well as the experimenters at Swartz Center for many months of running the experiment. 

## REFERENCES 

- [1] L.A. Farwell and E. Donchin, “Talking off the top of your head: toward a mental prosthesis utilizing event-related brain potentials,” _Electroencephalography and Clinical Neurophysiology_ , vol. 70, no. 6, pp. 510-523, 1988. 

- [2] N.Birbaumer et al., “A spelling device for the paralysed,”, _Nature_ , vol. 398, no. 6725, p. 297, 1999. 

- [3] D. Tan and A. Nijholt, _Brain-computer interfaces and human-computer interaction_ , London: Springer, 2010. 

- [4] C.T. Lin, R.C. Wu, S.F. Liang, W.H. Chao, Y.J. Chen, and T.P. Jung, “EEG-based drowsiness estimation for safety driving using independent component analysis,” _IEEE Transactions on Circuits and Systems I: Regular Papers_ , vol. 52, no. 12, pp. 2726-2738, 2005. 

- [5] J. van Erp, F. Lotte, and M. Tangermann, “Brain-computer interfaces: beyond medical applications,” _Computer_ , vol. 45, no. 4, pp. 26-34, 2012. 

- [6] K. McDowell, C.T. Lin, K.S. Oie, T.P. Jung, S. Gordon, K.W. Whitaker, S.Y. Li, S.W. Lu, and W.D. Hairston, “Real-World Neuroimaging Technologies,” _IEEE Access_ , vol. 1, pp. 131-149, 2013. 

- [7] S.L. Klosterman, J.R. Estepp, J.W. Monnin, and J.C. Christensen, “Dayto-day variability in hybrid, passive brain-computer interfaces: Comparing two studies assessing cognitive workload,” in _Engineering in Medicine and Biology Society (EMBC), 2016 IEEE 38th Annual International Conference of the_ , 2016, pp. 1584-1590. 

- [8] B.J. Lance, S.E. Kerick, A.J. Ries, K.S. Oie, and K. McDowell, “Brain– computer interface technologies in the coming decades,” _Proceedings of the IEEE_ , vol. 100, pp. 1585-1599, 2012. 

- [9] LSE Software Development Kit, ftp://sccn.ucsd.edu/pub/software/LSESDK/ 

- [10] T.O. Zander, and C. Kothe, “Towards passive brain–computer interfaces: applying brain–computer interface technology to human– machine systems in general,” Journal of Neural Eengineering, vol. 8, no. 2, p. 025005, 2011. 

- [11] N. Bigdely-Shamlo, K. Kreutz-Delgado, K. Robbins, M. Miyakoshi, M. Westerfield, T. Bel-Bahar, C. Kothe, J. Hsi, and S. Makeig, “Hierarchical event descriptor (HED) tags for analysis of event-related EEG studies,” in _Global Conference on Signal and Information Processing (GlobalSIP), 2013_ IEEE, 2013, pp. 1-4. 

- [12] The Lab Streaming Layer, https://github.com/sccn/labstreaminglayer 

- [13] Extensible Data Format, https://github.com/sccn/xdf 

- [14] C.A. Kothe, and S. Makeig, “BCILAB: a platform for brain–computer interface development,” _Journal of Neural Engineering_ , vol. 10, no. 5, p. 056014, 2013. 

- [15] B. Blankertz, S. Lemm, M. Treder, S. Haufe, and K.R. Müller, “Singletrial analysis and classification of ERP components—a tutorial,” NeuroImage, vol. 5, no. 2, pp. 814-825, 2011. 

- [16] T.O. Zander, C. Kothe, S. Jatzev, and M. Gaertner, “Enhancing humancomputer interaction with input from active and passive brain-computer interfaces,” in _Brain-computer Interfaces_ , London: Springer, 2010, pp. 181-199. 

- [17] P. Sajda, et al., “In a blink of an eye and a switch of a transistor: cortically coupled computer vision,” _Proceedings of the IEEE_ , vol. 98, no. 3, pp. 462-478, 2010. 

- [18] R. Tomioka, and K.R. Müller, “A regularized discriminative framework for EEG analysis with application to brain–computer interface,” _NeuroImage_ , vol. 49, no. 1, pp. 415-432, 2010. 

- [19] H. Shimazaki, and S. Shinomoto, “Kernel bandwidth optimization in spike rate estimation,” _Journal of Computational Neuroscience_ , vol. 29, no. 1-2, pp. 171-182, 2010. 

- [20] H. Ramoser, J. Müller-Gerking, and G. Pfurtscheller, “Optimal spatial filtering of single trial EEG during imagined hand movement,” _IEEE Transactions on Rehabilitation Engineering_ , vol. 8, no. 4, pp. 441-446, 2000. 

- [21] F. Lotte, and C. Guan, “Regularizing common spatial patterns to improve BCI designs: unified theory and new algorithms,” _IEEE Transactions on Biomedical Engineering_ , vol. 58, no. 2, pp. 355-362, 2011. 

- [22] R. Tomioka, G. Dornhege, K. Aihara, and K.R. Müller, “An iterative algorithm for spatio-temporal filter optimization,” in _Verlag der Technischen Universität Graz_ , 2006. 

- [23] K.K. Ang, Z.Y. Chin, H. Zhang, and C. Guan, ”Filter bank common spatial pattern (FBCSP) in brain-computer interface,” in _Neural Networks, IJCNN 2008 (IEEE World Congress on Computational Intelligence). IEEE International Joint Conference on_ , 2008, pp. 23902397. 

- [24] J. Friedman, T. Hastie, and R. Tibshirani, “Regularization paths for generalized linear models via coordinate descent,” _Journal of Statistical Software_ , vol. 33, no. 1, p. 1, 2010. 

82 

Authorized licensed use limited to: Univ of  Calif San Diego. Downloaded on August 01,2026 at 18:08:31 UTC from IEEE Xplore.  Restrictions apply. 

