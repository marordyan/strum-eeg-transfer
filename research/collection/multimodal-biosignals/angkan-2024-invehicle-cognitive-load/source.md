1 

# Multimodal Brain-Computer Interface for In-Vehicle Driver Cognitive Load Measurement: Dataset and Baselines 

Prithila Angkan, Behnam Behinaein, Zunayed Mahmud, Anubhav Bhatti, Dirk Rodenburg, Paul Hungler, Ali Etemad, _Senior Member, IEEE_ 

**_Abstract_ —Through this paper, we introduce a novel driver cognitive load assessment dataset, CL-Drive, which contains Electroencephalogram (EEG) signals along with other physiological signals such as Electrocardiography (ECG) and Electrodermal Activity (EDA) as well as eye tracking data. The data was collected from 21 subjects while driving in an immersive vehicle simulator, in various driving conditions, to induce different levels of cognitive load in the subjects. The tasks consisted of 9 complexity levels for 3 minutes each. Each driver reported their subjective cognitive load every 10 seconds throughout the experiment. The dataset contains the subjective cognitive load recorded as ground truth. In this paper, we also provide benchmark classification results for different machine learning and deep learning models for both binary and ternary label distributions. We followed 2 evaluation criteria namely 10-fold and leave-one-subject-out (LOSO). We have trained our models on both hand-crafted features as well as on raw data. We make our dataset public to contribute to the field.** 

**_Index Terms_ —Driver, cognitive load, wearables, braincomputer interfaces, deep learning.** 

## I. INTRODUCTION 

A large number of accidents and collisions occur on the roads every year. While many of these accidents are caused by distracted drivers, for instance due to distraction or drowsiness [1]. Distraction, meanwhile, can be caused by a number of personal or ambient factors, including high cognitive load due to engagement with secondary tasks [2], [3], [4]. Over the past several years, much research has been conducted to investigate the effects of cognitive load and cognitive fatigue. Studies have demonstrated that prolonged engagement in cognitively demanding tasks may lead to cognitive fatigue, a condition that could pose risks [5], [6]. Cognitive load refers to the quantity of information our working memory can process at a given time. In other words, it is the amount of cognitive resources required to accomplish a task. In general, two categories of cognitive load, intrinsic and extraneous, have been described in the literature [7]. While intrinsic cognitive load is defined as the inherent complexity of a given task, extraneous cognitive load refers to the cognitive resources demanded by environmental factors that are task-irrelevant [7]. The success or failure in performance toward a particular task, on the other hand, is influenced by the amount of cognitive load experienced by the person performing the task [8]. If the cognitive load increases beyond a certain point, the individual’s performance will degrade, which in case of driving may increase the likelihood of road accidents. 

In order to reduce the number of road accidents caused by high cognitive load, recent intelligent technologies integrated into vehicles should possess the ability to measure cognitive load and alarm the user should dangerously high amounts of it be detected. Brain-computer interfaces (BCI) have recently gained traction in providing advanced means of communication between humans and machines. In particular, headworn Electroencephalogram (EEG) devices allow for noninvasive yet accurate human-machine interactions. To this end, machine learning and deep learning techniques can be used to learn from datasets with various types of driver-related signals (including EEG). Additionally, these datasets require quantitative cognitive load scores to be measured and provided at frequent intervals, so that they could be used to train the machine learning models. While a number of relevant datasets have been collected and published in recent years [9], [10], [11], [12], [13], a number of problems persist. First, while a number of datasets for cognitive load do exist, they have often been captured in non-vehicle scenarios. In fact, to our knowledge, only [9] has studied cognitive load in the context of driving.Second, the cognitive load ground-truth scores in most existing datasets are generally sparse, and have been measured several minutes apart or upon task completion [12], [13]. This in turn makes training of machine learning models more difficult and less accurate. Third, while most existing datasets on cognitive load are in fact ‘multimodal’, the notion of BCI with auxiliary wearable signals has not been widely explored [9], [10], [11], [12], [13]. Lastly, in most existing works in the area, the focus has been solely on cognitive load or distraction caused by task-irrelevant activities, overlooking the fact that performing the main task itself (in our case, driving) can be a strong source of high cognitive load. 

In this paper, we introduce a novel driver cognitive load assessment dataset containing EEG signals along with other physiological signals such as Electrocardiography (ECG) and Electrodermal Activity (EDA) as well as eye tracking data. This dataset, which we name CL-Drive, is collected from 21 subjects while driving in an immersive vehicle simulator in diverse situations capable of inducing various levels of cognitive load in the subjects. Each subject performs driving tasks in 9 complexity levels for 3 minutes each and reports their subjective cognitive load every 10 seconds throughout the experiment as ground-truth cognitive load labels. In this paper, we also provide benchmark classification results for different machine learning and deep learning models. Both raw 

2 

signals as well as popular features supported by the literature have been used as inputs. We follow two important evaluation criteria, namely 10-fold and leave-one-subject-out (LOSO). Our benchmarking demonstrates that cognitive load induced by driving can be measured with reasonable accuracy using EEG and auxiliary wearable signals. 

Our contributions in this paper are summarized as follows: 

- We collect and release a dataset, CL-Drive, that can allow researchers to evaluate driving-induced cognitive load, which can be useful for developing automated alarm systems for intelligent vehicles. 

- CL-Drive provides data from various modalities including EEG, ECG, EDA and Gaze, which is a rich source for training machine learning systems capable of performing cognitive load assessment. To the best of our knowledge, this is the first and only dataset to collect driver cognitive load ratings along with bio-signals. 

- CL-Drive contains dense and frequent subjective ratings which are spread only 10 seconds, allowing for more reliable and frequent automated cognitive load measurement by learned models. 

The rest of this paper is summarized as follows. In Section II, we first provide a study of cognitive load followed by an overview of the publicly available cognitive load datasets that contain physiological signals. Section III explains the experimental setup, including sensor configurations, driving simulator details, cognitive load assessment, and data collection protocol. Next, we discuss the data pre-processing, feature extraction, normalization, and baseline classifiers in section IV. Lastly, in Section V we provide the results and discussions. 

## II. RELATED WORK 

## _A. Cognitive Load Measurement_ 

Prior research has shown that measuring cognitive load from physiological signals [14], [15] continues to be a challenging task [16], [17]. There are both subjective and objective measures that are commonly used to evaluate cognitive load levels that involve: ( _i_ ) self-reporting, ( _ii_ ) dual-task measures, and ( _iii_ ) physiological measures [18]. The PAAS scale [19], shown in Table I is most commonly used for self-reported subjective cognitive load labels. The National Aeronautics and Space Association Task Load Index (NASA-TLX) [20] is also commonly used as a self-reporting tool. Dual-task measurement involves the individual performing two tasks at the same time. One way of designing this is to measure knowledge gain from one task and response time for the other task [21]. In [22], another way of implementing dualtask measurement was explored, which was by performing a continuous secondary task while learning the primary task. There are several physiological parameters that have also been used as cognitive load measures in the past. This includes variation in pupil diameter and blink rate [23], [24], heart rate variability [25], and electrocardiogram (ECG) [26] to name a few. 

## _B. Cognitive Load in Driving_ 

In the area of driving, prior works have studied cognitive load mainly in the context of the driver being engaged by 

TABLE I: PAAS subjective cognitive load scores used in this study. 

|**PAAS Subjective**<br>**Cognitive Load Scores**|**Description**|
|---|---|
|1|Very, very low|
|2|Very low|
|3|Low|
|4|Rather low|
|5|Neither low nor high|
|6|High|
|7|Rather high|
|8|Very high|
|9|Very, very high|



secondary tasks such as using mobile phones or performing some other in-vehicle activities [2], [27], [28], [3], [29]. In [2], the cognitive load of drivers was measured when the drivers were involved in verbal conversation and word games while driving. As a result, the cognitive load induced was due to the combination of both primary as well as secondary tasks. A remote eye tracker was used to measure the pupil size of all 32 participants which in turn was used to estimate the cognitive load of the participants. The ground truth was the performance measures which they calculated using lane position and degree of rotation of the steering wheel, and subsequently evaluated the relationship between the change in pupil diameter and driving performance. 

In [30], the non-driving task of reading was performed by 18 participants in a fully automated vehicle. Two peripheral information systems, one utilizing the visual modality and the other the haptic modality, were assessed to examine their impact on situational awareness, mental workload, viewing behavior, and reading performance. In [31], a three-phase framework was proposed that allows effective diagnosis of driver’s visual and comprehension loads in traffic scenes. Drivers from diverse backgrounds were assessed for visual and comprehension load while driving simulations across various traffic scenarios. Another paper, [32], studied the effect of safe takeover transition in conditionally automated driving and used XGBoost to evaluate their work using a dataset from a metaanalysis study. 

Driving performance while interacting with a portable music player was evaluated in [27]. It was observed during a multisession setup, that the cognitive load of the participants during the first sessions was higher, hence the driving performance (e.g., perception response time (PRT) while braking and overall control of the vehicle), was lower in comparison to the later sessions. The experiment was carried out on 19 participants using simulated vehicle. Next, in [28], the high cognitive load of drivers was evaluated using EEG signals in 3 different driving conditions, namely: no secondary task (baseline), low cognitive load task, and high cognitive load task. The low and high cognitive load tasks were based on N-back tasks used in [33], [34]. GSR, eye tracking, respiration rate (RR), and accelerator release time (ART) data were collected during the experiments. The data was collected from 37 participants in a vehicle simulator. The NASA-TLX was used to collect the participants subjective rating at the end of the experiment. In [3], the cognitive load of participants was evaluated using eye 

3 

TABLE II: Existing datasets in the literature that study cognitive load using physiological signals. 

|**Dataset**|**Year**|**Sub.**|**Mental State**|**Modalities**|**Stimuli**|
|---|---|---|---|---|---|
|Driver Workload [9]|2013|10|Mental workload of the driver|ECG, BTemp, SCR|Watching driving videos, Driving<br>in real environment|
|MMOD-COG [10]|2019|40|Cognitive load|ECG, EDA, Speech|Arithmetic, Reading|
|CLAS [11]|2019|62|Cognitive Load, negative emotion<br>and mental stress|ECG, PPG and EDA|Math problems, Logic problems<br>and Stroop test|
|CogLoad [12]|2020|23|Cognitive load, Personality traits|heart rate, beat to beat interval,<br>EDA, ST, and ACC|Different cognitive load tasks (2-<br>back and 3-back tasks, visual cue<br>task etc.)|
|Snake [12]|2020|23|Cognitive load|heart rate, beat to beat interval,<br>EDA, ST, and ACC|Snake game on a smartphone|
|Kalatzis et al. [13]|2021|26|Cognitive load|ECG, RR|MATB-II|
|CL-Drive (ours)|2023|21|Cognitive load|EEG, ECG, EDA, Gaze|Driving a simulated vehicle in<br>scenarios with various complexity<br>levels|



video data extracted from facial videos during driving. Three different N-back tasks were used as secondary tasks, which were also used to quantify the ground truth levels. Hidden Markov models and 3D-CNN were then used to evaluate the result. In another paper [29], the cognitive load of participants was evaluated while driving and performing a 1-back task. EEG data was collected from 36 participants. To evaluate the performance, case-based reasoning classifiers were used [35]. A few other prior works such as [2], [27], [28] have used more simple approaches based on predefined metrics (e.g., required time to break, degree of motion of the steering wheel, etc.) to measure cognitive load from physiological signals. 

Besides cognitive load, other factors such as driver emotions [36], [37], [38] and vigilance [39], [40], [41], have been widely studies in the literature. While these works may maintain some similarities to works on cognitive load, they are in fact different driver attributes which are outside the scope of this study. Moreover, the notions of affect and distraction have been more widely studied for drivers, as opposed to cognitive load which is a less explored area. 

## _C. BCI_ 

BCI systems can communicate the neural activities in the brain directly with an external device [8], [42]. Research has shown that BCI can play a vital role in interpreting the cognitive load induced while driving [8], [42]. This is due to the fact that the fronto-parietal brain regions along with sub-cortical regions can be engaged while experiencing varying amounts of cognitive load [43]. EEG, is a non-invasive method which measures the potential difference caused by the electrical activity in the brain [44], [45]. This property of EEG allows it to capture changes in brain activity while experiencing variations in cognitive load, which makes it a very good candidate for cognitive load evaluation. Multimodal approaches have proven effective at magnifying the accuracy of cognitive load assessment in the past [46]. Apart from EEG, research has shown that both the sympathetic nervous system (SNS) which controls the skin conductance response and automatic nervous system which controls the heart rate variability (HRV) are impacted by cognitive load [47], [48], 

[49]. Prior research has also shown significant correlation between changes in pupil size, blink rate, saccade, and fixation with cognitive load [50], [51]. 

## _D. Public Cognitive Load Datasets_ 

Previous research has examined the induction of cognitive load in drivers with a subsequent evaluation of driving performance under varying cognitive load levels [52], [53]. Some other publications have studied cognitive load under a variety of different experimental setups [54], [26]. There is evidence that affect and cognitive load are interrelated and affect has a significant impact on cognitive load [55]. Though a wide range of studies have been done to study the impact of affect on EEG [56], [57], the available datasets for cognitive load are indeed quite limited. In this section, we provide an overview of the publicly available datasets for cognitive load with physiological signals. Table II presents a summary of these datasets. 

The Driver Workload dataset [9], provides multimodal data to evaluate driver workload using ECG, body temperature, and skin conductance response (SCR). The dataset was collected from 10 participants with the goal of evaluating cognitive load of drivers on different types of roads and in different driving environments. In addition to the physiological signals, two cameras were also used to record the driving route as well as the participant’s facial videos. The video data were not made public for privacy purposes. The data was collected as the participants drove the car for 30 minutes. Participants subjective ratings were collected by watching videos of their own driving at the end of the activity. 

The MMOD-COG [10] dataset was recorded from 40 different subjects for cognitive load assessment during reading and arithmetic tasks. ECG and EDA were recorded from the subjects in addition to speech. The experiment was divided into reading and arithmatic segments where in the reading segment, two separate digits were shown for 5 seconds and repeated with different digits 20 times. The arithmetic segment was divided into high and low cognitive load levels and a total of 40 problems were asked to be solved by each participant. The CLAS dataset [11] was collected from 62 participants 

4 

and was obtained by recording various cognitive load levels induced by tasks such as mathematics and logic problems as well as the Stroop test [58]. In addition to cognitive load, audiovisual stimuli were used to induce emotional variations in the participants. Physiological data was collected using ECG, Plethysmography (PPG), EDA, and accelerometer (ACC) data. The next dataset, CogLoad [12] was also a multimodal dataset with 23 participants who performed 6 different computer tasks during the collection process. The physiological data collected was heart rate, beat to beat interval, EDA, skin temperature (ST), and ACC. The task was divided into two segments where the first segment involved understanding the participant’s degree of cognitive resources and their personality traits using two N-back tasks [12], [59]. Whereas, in the second segment, 6 different tasks that required varying levels of cognitive load were performed. In addition, in order to completely occupy the cognitive resources of the participants, a secondary task was also given to them to perform. 

Another multimodal dataset consisting of heart rate, EDA, ST, and ACC was collected from 23 participants while they played the Snake game on a smartphone [12]. This dataset named Snake [12], was collected with varying cognitive load levels where the amount of cognitive load experienced by the participants was controlled by the changing speed of the game. The task consisted of 3 complexity levels, high, medium and low, which lasted 2 minutes each. After the task completion, the participants answered the NASA TLX [20] questionnaire along with two other 7-point Likert scale questions. Finally, Kalatzis et al. [13] presented a dataset that has been collected from 26 participants. In this dataset, the cognitive load of the participants was assessed using ECG and respiration rate (RR) data. High and low cognitive load data were collected as the participants used the MATB-II software [60] while the NASA TLX [20] questionnaire was used to collect ground truth values for the two cognitive load levels. 

In contrast to the above, our dataset considers driving to be the primary task and evaluates cognitive load induced while driving. Moreover, we record frequent subjective cognitive load scores which is not the case in existing cognitive load datasets. This allows us to perform more accurate evaluations and train better machine learning models. Finally, CL-Drive contains several modalities that enable multi-modal studies on cognitive load. 

## III. EXPERIMENT SETUP AND DATA COLLECTION 

In this section, we discuss the experimental protocol used in the study. This includes specifics on the setup for the sensors and driving simulator as well as details of the participants, diving scenarios, and cognitive load assessment. 

## _A. Sensors_ 

During the experiments which will be described in Section III-G, we use four different sensors to collect physiological signals from which to measure cognitive load. Following is a description of each sensor type, namely EEG, ECG, EDA, and Gaze, in detail. Figure 1 shows the sensors used in our study, while Figure 2 shows their detailed sensors placement. 

**EEG.** For collecting EEG signals the Muse S<sup>1</sup> headband shown in Figure 1a is used. The device has 4 channels where 2 of them are frontal electrodes located at the forehead in locations AF7 and AF8 (according to the international 1020 system [61], [62]) while the remaining 2 are temporal electrodes located behind the ears in locations TP9 and TP10. Figure 1a depicts the Muse EEG device while in Figure 2a, we present the sensor locations of this EEG headset. As shown in the figure, the reference electrode is located at the middle of the forehead in location FpZ. The sampling rate of the EEG headband is 256 _Hz_ . Conductive gel is used to enhance the conductivity between the electrode and the skin. We opt for the Muse S headband to ensure both comfort and compatibility with the gaze device. 

**ECG.** ECG signals are collected through the Shimmer<sup>2</sup> sensors [63], which is shown in Figure 1b. As depicted in Figure 2b, this wearable device uses 5 standard pre-gelled adhesive electrodes from the chest and abdominal area. Among the 4 electrodes, the Right Arm (RA) and Left Arm (LA) are placed on the left and right sides of the manubrium, while Right Leg (RL) and Left Leg (LL) are placed right above the lower costal margin. The reference electrode denoted by Vx is placed slightly on the right of the sternum. The signals collected are LL-RA, LA-RA, and Vx-RA at a sampling frequency of 512 _Hz_ . The Shimmer is worn by the participants using a belt and a cradle. 

**EDA.** Similar to ECG, the EDA signal is collected using a Shimmer wearable device [63] as shown in Figure 1c. The data is collected using 2 electrodes placed on the left side of the abdomen which is shown in Figure 2c. The sampling frequency of the EDA Shimmer device is 128 _Hz_ 

**Gaze** Figure 1d shows a Tobii device<sup>3</sup> used to collect eye tracking data. The device is comprised of a head unit and a recording unit. Inside the device there are 2 cameras per eye as well as a wide angle scene camera. From the eye tracking device we record the specific eye movement events such as saccade, fixation, and others. The sampling frequency is 50 _Hz_ . Figure 2d illustrates the placement of the eye tracking device along with the EEG headset. 

## _B. Experiment Test-bed_ 

In order to simulate driving and be able to control the parameters surrounding the driving experience, we use a driving simulator<sup>4</sup> shown in Figure 3. The driving simulator includes elements similar to a real car, including steering wheel, dashboard, accelerator, and brake. These components combined with a motion system provides participants with a more realistic driving sensation. The motion system can emulate real-life motions up to 100 _Hz_ in frequency. This includes vibrations from road texture, acceleration, braking, speeding, and turning along with other essential movements to provide users with engaging haptic feedback. Additionally, there are three 55 inch LCD screens which provide a 180 

> 1https://choosemuse.com/muse-s/ 

> 2https://shimmersensing.com/product/shimmer3-ecg-unit-2/ 

> 3https://www.tobiipro.com/product-listing/tobii-pro-glasses-2/ 

> 4https://viragesimulation.com/vs500m-car-simulator-training-and-research/ 

5 











<!-- Start of picture text -->
(c) EDA device<br>and Gaze devices.<br><!-- End of picture text -->

Fig. 1: Wearable EEG, ECG, EDA, and Gaze devices. 



<!-- Start of picture text -->
FPZ RA LA<br>AF7 (ref.) AF8 Vx<br>TP9 TP10<br>RL LL<br>(a) EEG (b) ECG<br><!-- End of picture text -->



<!-- Start of picture text -->
EDA 1<br>EDA 2<br><!-- End of picture text -->



<!-- Start of picture text -->
AF7 AF8<br>TP10 TP9<br>Wearable EEG  Wearable eye<br>headband tracker<br><!-- End of picture text -->

Fig. 2: EEG, ECG, EDA, and Gaze electrode placements. 

degree view from the front, plus two additional screens for the blind spots, together creating an immersive experience. Each front screen has a display resolution of 1920 _×_ 1080 pixels. Moreover, directional sound is incorporated using a surround sound system. The sound is intended to mimic typical sounds heard while driving including the sound of the engine, speeding and passing vehicles, and horns, among others. 

A debrief station is designed to provide a complete video of the participant and simulation screens during the experiment along with performance graphs. There is a webcam mounted on the top of the middle frontal screen, which has a resolution of 720p. The camera records video of the participants while driving in the simulator. The performance information displayed in the debrief station includes driving performance data, including the time required for breaking and acceleration, possible crashes, and others. This data can also be used for performance analysis. 



Fig. 3: The immersive vehicle simulator used in this study. 

## _C. Driving Scenarios_ 

The simulator comes with a number of pre-built driving scenarios in which the vehicle type, environmental conditions, and other factors can vary. Each scenario consists of a number of tasks that need to be performed, e.g., keeping the speed above a certain threshold. Moreover, each scenario has a designated complexity level. We choose 9 different scenarios, one from each complexity level. The scenarios encompass a range of common challenges encountered during everyday driving, such as driving on highways, at night-time, and in snowy conditions (scenarios 1, 2, 3 respectively), maintaining/changing speed levels (scenarios 4, 5, 6, 7 and 9), avoiding accidents (scenarios 4, 5, 6, 7 and 9), back-to-back turns (scenario 7), and turning the car around on a narrow road using 3-point turn (scenario 8). The scenarios induce different levels of cognitive load in 

the participants based on a number of pilot tests that we carried out to choose these 9 from among a larger pool of possible tasks. Moreover, the scenarios are structured to progressively increase in difficulty, yet remain achievable for the average driver. In Figure 4, we depict the heat map of the frequency of the ratings for each driving scenario. We observe that as the scenarios progress, more and more participants select higher cognitive load scores, indicating that the task complexities do indeed increase as the scenarios progress, especially for scenarios 8 and 9. 

The duration of each scenario is set to 3 minutes. An orientation scenario was designed and performed by each participant at the beginning of the session to allow each participant to adapt to the simulator. In the orientation session, 

6 

TABLE III: Driving scenario details 

|**Scenario/**<br>**Complexity**|**Simulation**|**Description**|
|---|---|---|
|0/Orientation|Highway driving|Maintain centre|
|1|Highway driving|80km/h|
|2|Night time driving|80km/h|
|3|Night time driving in the highway w/ snow|80km/h|
|4|Tennis ball challenge|Hit the tennis ball with the tire, maintain accuracy, try to accelerate|
|5|Slalom challenge|Navigate through gates, maintain accuracy, try to accelerate|
|6|Narrow passage challenge|Navigate through gates, maintain accuracy, try to accelerate|
|7|90-degree turn challenge|Take 90 degrees left and right turns, maintain accuracy, try to accelerate|
|8|3-point turn challenge|Drive while following instructions, take 3 point turn|
|9|Narrow alley challenge|Navigate through narrow alley, maintain accuracy, try to accelerate|



|TABLE IV: SAS levels and their corresponding description.<br>**SAS Level**<br>**Description**|
|---|
|200<br>1<br>Feeling no adverse effects<br>2<br>Feeling very mild discomfort|
|175<br>3<br>Feeling mild discomfort|
|4<br>Feeling mild to moderate discomfort|
|150<br>5<br>Feeling moderate discomfort|
|6<br>Feeling moderate to pronounced discomfort|
|125<br>7<br>Feeling pronounced discomfort|
|8<br>Feeling pronounced to severe discomfort|
|100<br>9<br>Feeling severe discomfort (potential for vomiting)|
|50<br>75<br>_(0<N<10, N+1)_|
|25<br>3 Minutes<br>Baseline<br>Orientation<br>2 Minutes<br>Baseline<br>Session N<br>2 Minutes<br>Rest<br>|





<!-- Start of picture text -->
210 105 11 0 5 8 0 6 0 200<br>53 61 25 2 7 23 9 11 1 175<br>51 64 36 34 25 18 20 26 9 150<br>16 40 42 53 49 23 42 12 11 125<br>23 37 65 54 67 70 60 35 39<br>100<br>0 25 67 70 71 48 58 62 41<br>75<br>2 8 49 59 71 44 40 52 64<br>50<br>0 0 15 31 29 18 34 51 59<br>25<br>0 0 39 39 38 22 17 49 79<br>0<br>1 2 3 4 5 6 7 8 9<br>Task Complexity<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>Subjective Cognitive Load Scores 8<br>9<br><!-- End of picture text -->

Fig. 5: The experiment flow. 

Fig. 4: Complexity vs. subjective cognitive load scores. The lighter shade means more sample. 

- 1) **Cool room:** the simulator room must be cool and well ventilated; 

- 2) **Confident introduction:** must create a calm and relaxed environment; 

we described the system first as the system completes a number of steps to ensure things like the turn signals, motion sensors, brake, accelerator, ignition, emergency stop, seat belt, and others function properly. Participants then began to drive on the highway to become familiar with the speed display, onscreen arrow that provides cues about the direction of driving, and all the other necessary indicators, while we were present to provide help if needed and answer any questions. Table III shows the description of each driving scenario along with its corresponding complexity level. 

## _D. Simulation Adaptation Syndrome_ 

It has been shown in prior research that Simulation Adaptation Syndrome (SAS) can affect different participants [64], [65]. SAS can range from feeling minor discomfort to severe symptoms such as dry mouth, dizziness, vertigo, vomiting, nausea, and disorientation while taking part in simulations such as driving a vehicle [66]. The main cause of SAS is the discrepancy between the sensory inputs such as visual and vestibular system (which is responsible for our sense of balance [67], [68]). One of the challenges we faced during our study was avoiding and minimizing SAS. As recommended in the simulator instructions, we followed the following 5 steps to manage and reduce SAS as much as possible: 

- 3) **Cautious alert:** moving on slowly to allow the driver’s time to adjust; 

- 4) **Careful observation:** must actively look for signs and symptoms of SAS; 

- 5) **Cease driving:** must pause immediately on observing the slightest sign of SAS. 

SAS can be managed by carefully monitoring the participant’s level of discomfort using a Likert scale and asking the participants to do an intermittent self assessment. In our case, the participants were asked to self report on their SAS level every minute using a 9-point Likert scale as shown in Table IV, which was made based on the Motion Sickness Questionnaire (MSQ) [69], Simulator Sickness Questionnaire (SSQ) [70], and The Motion Sickness Assessment Questionnaire (MSAQ) [71]. Based on these pre-cautions and careful monitoring, SAS resulted in pausing and discontinuing only 2 participants. 

## _E. Participants_ 

Data was collected from 23 participants including 17 females and 6 males. The participant’s gender was not controlled for and we merely included volunteers regardless. We did not actively seek individuals of specific genders, as it was not a prerequisite for our study. Given that the key focus of this 

7 

study has been cognitive load during driving, we controlled for having a driving license and a few years of driving experience. We also ensured that participants were not under the influence of any substances at the time of data collection. The average age of participants was 26.9. Background health information were not collected in this study. 

Prior to the simulation, participants were provided with detailed information on the experimental process and the research team received written consent. The study was approved by Queen’s University’s General Research Ethics Board (GREB). Among the 23 participants, 2 data collection sessions were stopped due to high levels of SAS, while the data from another 3 sessions was incomplete due to device or connectivity issues. Specifically, for participant 13, we only have data for scenarios 3, 4, 5, 6, and 9, while for participant 16, we have data for scenarios 1, 5, 6 and 9. Finally, for participant 18, we have the data for scenarios 1 to 6. While the data from the two sessions that were incomplete due to SAS are not incorporated in the dataset as they were interrupted too early in the process, the data from the three incomplete sessions are incorporated. 

## _F. Cognitive Load Self-Assessment_ 

Participant cognitive load self-assessment ratings were used as ground truth labels in this study. As shown in Table I, PAAS subjective cognitive load scores consist of 9 levels [72]. A looping audio cue was generated every 10 seconds during the experiments to prompt the participants to verbally report their cognitive load, and a member of the research team recorded the reported scores. Figure 7 presents the distribution of the recorded output scores for all the participants. 

Regarding the frequency at which the responses were recorded, we aimed to balance the frequency of labels for the purpose of training machine learning models, and ensuring that the questions themselves did not impact the experiment significantly. Through a few pilot trials, 10 seconds was found to be a reasonable interval, as longer intervals could lead participants to forget their earlier experiences during that segment, while shorter intervals could interfere with the experiment itself. 

## _G. Experiment Protocol_ 

Participants were given clear descriptions about the data collection protocol and equipment. After careful sensor placement, participants were asked to sit in the driving seat of the simulator and the sensors were connected via Bluetooth to a data collection station. First, 3 minutes of baseline data was collected from each participant which could be used for future normalization of the signals. To become adapted to the simulated driving environment and make sure that participants had a clear understanding about the ‘low’, ‘medium’, and ‘high’ complexity levels, and also to reduce the SAS level, participants were asked to perform the _Orientation_ scenario mentioned earlier in Table III. Following every 3-minute driving scenario (see Table III), the participants were given a resting time of 2 minutes to allow them to rest, reduce the possibility of SAS, and come back to a relatively lower 

cognitive load state. Followed by the resting period, a 2-minute baseline was collected before each new scenario. The experiment flow is shown in Figure 5. During all these experiments, the wearable sensors discussed earlier in Section III-A were used to record the respective signals from the participants. Figure 6 we illustrate a sample from each captured modality in both high and low cognitive load scenarios. 

## _H. Dataset Release_ 

We make the dataset public at: https://github.com/Prithila05/CL-Drive 

## IV. DATA PROCESSING 

In this section, we explain the data pre-processing steps for each signal type, followed by feature extraction. Next, we describe data normalization, which is followed by a description of the baseline classifiers used for benchmarking. 

## _A. Pre-processing_ 

The cognitive load scores were collected at 10-second intervals during the 3-minute driving scenarios. We segment each recording into 18 segments of 10 seconds each. These segments will later be used for feature extraction or fed directly into the deep learning models. 

**EEG.** To remove noise and artifacts from EEG, we used a Butterworth 2<sup>nd</sup> order bandpass filter with a passband frequency of 0.4 to 75 _Hz_ . A notch filter with a quality factor of 30, was used to remove the powerline noise at a frequency of 60 _Hz_ . Due to some Bluetooth problems, the device experienced a few disconnections lasting approximately 30 seconds during the experiments. Given the duration of these gaps, using imputation methods would not be suitable. We therefore excluded segments with missing data from our dataset. 

**ECG.** Artifacts such as high-frequency noise, EMG noise, T noise interference, etc., were then filtered out using a Butterworth bandpass filter with passband frequency of 5 to 15 _Hz_ , which also enables us to obtain maximum _QRS_ energy [73], [74]. The ECG signals experienced missing values occasionally, which we imputed using simple 5<sup>th</sup> order polynomial interpolation. 

**EDA.** We then used a lowpass butterworth filter with a cutoff frequency of 3 _Hz_ to remove the unwanted noise. A highpass butterworth filter with a cut-off frequency of 0.05 _Hz_ was used to decompose the filtered EDA signal to tonic skin conductance level and phasic skin conductance response to isolate the slow changing levels and rapid changing peaks in the signal [75]. There were some missing values which we replaced with a sample-and-hold strategy given the simplicity of EDA signals in comparison to ECG. 

**Gaze.** The device measures saccade, fixation, pupil diameter, blink count, and blink duration based on 2D gaze coordinates ( _x_ , _y_ pixel coordinates in screen space) for both left and right eyes, 3D gaze coordinates ( _x_ , _y_ , _z_ coordinates in mm in camera space), 3D gaze direction (vector units), gaze velocity in degrees per second (<sup>_◦_</sup> /s), and gaze acceleration in degrees per 

8 



<!-- Start of picture text -->
EEG ECG<br>10075 low cognitive loadhigh cognitive load 7.57.0 low cognitive loadhigh cognitive load<br>50<br>6.5<br>25<br>6.0<br>0<br>5.5<br>25<br>5.0<br>50<br>4.5<br>75<br>4.0<br>100289.00 289.25 289.50 289.75 290.00 290.25 290.50 290.75 291.00 125 126 127 128 129 130<br>Timestamp (sec) Timestamp (sec)<br>EDA Gaze<br>20<br>low cognitive load 9 low cognitive load<br>high cognitive load high cognitive load<br>18 8<br>7<br>16<br>6<br>14 5<br>4<br>12<br>3<br>0 25 50 75 100 125 150 175 125 126 127 128 129 130<br>Timestamp (sec) Timestamp (sec)<br>Poyential (uV) Poyential (uV)<br>EDA (uS)<br>Pupil diameter (mm)<br><!-- End of picture text -->

Fig. 6: Examples of different signals in high and low cognitive load scenarios. 

TABLE V: Extracted features from each modality. 

|**Modalities**|**Extracted features**|**Number of features**|
|---|---|---|
|EEG|PSD (absolute, mean, maximum, minimum, median power), Spectral Entropy, Hjorth mobility and<br>complexity, Lempel-Ziv Complexity, Higuchi fractal dimension, raw signal (mean, minimum, maximum,<br>median, variance, and standard deviation)|40|
|ECG|RMSSD, MeanNN, SDNN, SDSD, CVNN, CVSD, MedianNN, MadNN, MCVNN, IQRNN, pNN50,<br>pNN20, TINN, HTI, SD1, SD2 SD1/SD2, S, CSI, CSI<br>Modifes, CVI, PIP, IALS, PSS, PAS, GI, SI,<br>AI, PI, C1d, C1a, SD1d, SD1a, C2d, C2a, SD2d, SD2a, Cd, Ca, SDNNd, SDNNa, ApEn, SampEn,<br>mean, median, standard deviation, skewness, kurtosis, entropy, interquartile range, area under curve,<br>squared area under the curve, median absolute deviation|53|
|EDA|Mean, median, standard deviation, skewness, kurtosis, entropy, interquartile range, area under curve,<br>squared area under the curve, median absolute deviation for raw data as well as phasic and tonic<br>response|30|
|Gaze|Pupil diameter (max, min, mean), Blink count, duration (max, mean), Fixation count, duration (max,<br>min, mean), dispersion (max, min, mean), Saccade count, duration (max, min, mean), amplitude (max,<br>min, mean), peak velocity (max, min, mean), peak acceleration (max, min, mean), peak deceleration<br>(max, min, mean), direction (max, min, mean)|32|



second squared (<sup>_◦_</sup> / _s_<sup>2</sup> ). We directly use the high-level metrics in our study. For the missing values in Gaze data, we used the sample-and-hold method similar to that of EDA due to the straightforward nature of the signals. 

## _B. Feature Extraction_ 

Different features were extracted to train our machine learning algorithms. In this section, we describe the features extracted from each modality. No feature selection methods were used. Given the focus of our work on BCI (other modalities play auxiliary roles in the multimodal setups), we describe the EEG-related features in more depth below. **EEG.** We extract 40 features from both time and frequency domains from each channel for each 10 seconds segment. The details of the features are given below: 

- 1) **Power Spectral Density (PSD):** PSD measures the power of the EEG signal. To calculate this feature we use the Welch’s method from 0.5 _Hz_ to 75 _Hz_ frequency, for each frequency band, Delta (0.5-4 _Hz_ ), Theta (4-8 _Hz_ ), Alpha (8-12 _Hz_ ), Beta (12-31 _Hz_ ), and Gamma (31-75 

_Hz_ ). We then measure the absolute, mean, maximum, minimum, and median power of the measured PSD. 

- 2) **Spectral entropy:** Spectral entropy (SE) of a time series signal is derived from normalized Shannon’s entropy [76] and can be used to determine the complexity of a signal. The formula of SE can be derived from normalized PSD or probability distribution _p(i)_ of the signal as 



We calculate _SE_ for all 5 bands of EEG. 

- 3) **Hjorth mobility and complexity:** Both Hjorth mobility and complexity of a time series signal determine aspects of the signal complexity [77], where the variations in signal frequency and amplitude are represented by Hjorth mobility and complexity respectively. These two measurements can be jointly used to capture the dynamic behavior of signals. Hjorth mobility and complexity are 

9 



<!-- Start of picture text -->
40302010 Label Distribution 403530252015105 Label Distribution 8070605040302010 Label Distribution 605040302010 Label Distribution 403530252015105 Label Distribution 3530252015105 Label Distribution 40302010 Label Distribution<br>0 1 2 3 4 Label5 6 7 8 9 0 1 2 3 4 Label5 6 7 8 9 0 1 2 3 4 Label5 6 7 8 9 0 1 2 3 4 Label5 6 7 8 9 0 1 2 3 4 Label5 6 7 8 9 0 1 2 3 4 Label5 6 7 8 9 0 1 2 3 4 Label5 6 7 8 9<br>(a) Subject 1 (b) Subject 2 (c) Subject 3 (d) Subject 4 (e) Subject 5 (f) Subject 6 (g) Subject 7<br>Label Distribution Label Distribution Label Distribution Label Distribution Label Distribution Label Distribution Label Distribution<br>5040302010 30252015105 8070605040302010 40302010 40302010 3530252015105 70605040302010<br>0 1 2 3 4 Label5 6 7 8 9 0 1 2 3 4 Label5 6 7 8 9 0 1 2 3 4 Label5 6 7 8 9 0 1 2 3 4 Label5 6 7 8 9 0 1 2 3 4 Label5 6 7 8 9 0 1 2 3 4 Label5 6 7 8 9 0 1 2 3 4 Label5 6 7 8 9<br>(h) Subject 8 (i) Subject 9 (j) Subject 10 (k) Subject 11 (l) Subject 12 (m) Subject 13 (n) Subject 14<br>605040302010 Label Distribution 252015105 Label Distribution 40302010 Label Distribution 403530252015105 Label Distribution 252015105 Label Distribution 30252015105 Label Distribution 5040302010 Label Distribution<br>0 1 2 3 4 Label5 6 7 8 9 0 1 2 3 4 Label5 6 7 8 9 0 1 2 3 4 Label5 6 7 8 9 0 1 2 3 4 Label5 6 7 8 9 0 1 2 3 4 Label5 6 7 8 9 0 1 2 3 4 Label5 6 7 8 9 0 1 2 3 4 Label5 6 7 8 9<br>(o) Subject 15 (p) Subject 16 (q) Subject 17 (r) Subject 18 (s) Subject 19 (t) Subject 20 (u) Subject 21<br>Datapoints Datapoints Datapoints Datapoints Datapoints Datapoints Datapoints<br>Datapoints Datapoints Datapoints Datapoints Datapoints Datapoints Datapoints<br>Datapoints Datapoints Datapoints Datapoints Datapoints Datapoints Datapoints<br><!-- End of picture text -->

Fig. 7: Self-reported cognitive load level distribution for each participant. 



<!-- Start of picture text -->
Block 1 Block 2 Classification Block<br>EEG<br>ECG<br>EDA Cognitive<br>load score<br>Gaze<br>Conv1D BN ReLU Conv1D BN ReLU MaxPool Conv1D BN ReLU Conv1D BN ReLU MaxPool Pool FC FC Output<br>Global Avg.<br><!-- End of picture text -->

Fig. 8: VGG-style network used as for benchmarking in this study. 



<!-- Start of picture text -->
Block 1 Block 2 Classification Block<br>EEG<br>ECG<br>EDA<br>Gaze Cognitive<br>load score<br>Conv1D BN ReLU BN ReLU Conv1D BN ReLU Conv1D MaxPool BN ReLU Conv1D BN ReLU Conv1D MaxPool BN ReLU FC FC FC Output<br><!-- End of picture text -->

Fig. 9: ResNet-style network used as for benchmarking in this study. 

respectively calculated as: 



and 



where _y_ ( _t_ ) represents the signal and _σ_<sup>2</sup> is the variance operator. 

- 4) **Lempel-Ziv complexity:** Lempel-Ziv complexity (LZC) is a measure that also determines the complexity of a signal [78]. To apply the LZC algorithm to an EEG signal, the signal first needs to be binarized by the median or mean value of the entire signal. The resulting binary sequence can then be analyzed the using LZC algorithm to find any randomness [79]. 

- 5) **Higuchi fractal dimension:** Higuchi fractal dimension (HFD) is a non-linear method that can capture changes in time-series signals by measuring the complexity in time domain [80]. Prior studies have shown promising result using HFD with EEG signal in the past [81], [82]. 

- 6) **Statistical features:** In addition to the more sophisticated features mentioned above, we also extract simple statistical features namely mean, minimum, maximum, and median from the signal in time domain. 

The complete list of EEG features is summarized in Table V. **ECG.** We extract various commonly used features from ECG [83]. The full list of features extracted from ECG is presented in Table V. All the features are extracted using the Neurokit2<sup>5</sup> library. Please visit the library for further details. 

**EDA.** We extract a number of features from EDA. These include statistical features from the raw data as well as phasic and tonic responses which are calculated by decomposing the 

5https://neuropsychology.github.io/NeuroKit/functions/hrv.html 

10 

TABLE VI: The machine learning model parameters used in this study. 

|**Models**|**Parameters**|
|---|---|
|AB|number of estimators: 70, learning rate: 0.1, algorithm:<br>SAMME.R|
|DT|criterion: gini, random state: 42, maximum depth: 3, mini-<br>mum samples to be at leaf node: 5|
|NB|variance smoothing: 1e<sup>_−_09</sup>|
|KNN|number of neighbors: 20, weights: distance, algorithm: ’auto’|
|LDA|solver: least squares solution|
|RF|maximum depth: 50, number of estimators: 1000, number of<br>jobs: -1, random state: 42, class weight: balanced|
|SVM|regularization parameter: 0.1, kernel: polynomial|
|XGB|maximum depth: 20, number of estimators: 1000, learning<br>rate: 0.001, use label encoder: False, subsample: 0.5, verbose<br>eval: 200, booster: dart, number of jobs: -1, number of leaves:<br>50, regularization lambda: 0.0001, class weight: balanced|
|MLP|hidden layer sizes: (100, 50), learning rate: adaptive, maxi-<br>mum iteration: 1000|



EDA signal. The complete list of features extracted from EDA is presented in Table V. 

**Gaze.** For gaze analysis, we extract statistical features for each 10-second segment. The details of all the features are given in Table V. 

## _C. Normalization_ 

To reduce the variability _between subjects_ , which is a common phenomenon when recording such data, we divide each feature value with its corresponding average value from the baseline. Second, to reduce the variability _within subjects_ , we perform z-score normalization [84] following prior works such as [85], [86], [87]. 

operation. These blocks are followed by two fully connected layers and a classification layer. Cross-entropy loss with a learning rate of 0.001 was used for training. ADAM was used as the optimizer for this network [88]. 

The ResNet-style network, similar to the VGG model above, consists of two blocks containing two Conv1D layers, batch normalization, and ReLU activation function in each block. The classification block contains three fully connected layer followed by an output classification layer. Similar to the VGG network, we use cross-entropy loss and train the model with ADAM optimizer. Here, a learning rate of 0.01 is used. For both networks trained with features, a batch size of 32 is used. 

It should be noted that most studies on BCI and EEG in particular use extracted features to train deep learning models [89], [57], which is the approach we took with the networks described above. However, for completeness, we also train the deep networks with raw data (after pre-processing). For this purpose we design a separate encoder for each modality and use feature-level fusion. We expectedly notice that the optimum network depth used when utilizing the extracted features (2 blocks) is not sufficient when using the raw data. We therefore increase the depth by adding a third block to obtain better results. Accordingly each encoder for the raw data contains 3 blocks for both the VGG and ResNet-style models. The details of the architecture remain mostly the same. We present all the details of the deep networks in Table VII, for both VGG and ResNet-style models, when trained with features or raw signals. For both networks trained with raw data, a batch size of 256 is used. 

_3) Multimodal:_ For the multimodal setup using the classical machine learning methods, we simply concatenate the hand-crafted features, and feed the concatenated features to each classical classifier. For multimodal learning with deep neural networks (VGG and ResNet), we first feed the raw data from each modality to a separate network and apply MaxPool followed by global average pooling on the outcome. The features are then fused together through concatenation and fed to the classifier block. 

## _D. Classifiers_ 

To evaluate the dataset and to experiment the efficacy of building an automated cognitive load detection system using the collected data, we train several classical machine learning and deep learning classifiers on the extracted features or raw data. In this section, we describe these models in detail. 

_1) Classical machine learning:_ We train a total of 9 machine learning classifiers namely AdaBoost (AB), Decision Tree (DT), Naive Bayes (NB), K-Nearest Neighbor (KNN), Linear Discriminant Analysis (LDA), Random Forest (RF), Support Vector Machine (SVM), Extreme Gradient Boosting (XGB), and Multi-Layer Perceptron (MLP). The details of the parameters of these classifiers are presented in Table VI. 

_2) Deep learning:_ For deep learning network we use two deep Convolutional Neural Networks (CNNs), a VGG-style network as shown in Figure 8, and a ResNet-style network which is shown in Figure 9. The VGG-style network has two main blocks where each block consist of two Conv1D layers, batch normalization, ReLU activation, and maximum pooling 

## _E. Training scheme_ 

We train all the models (classical machine learning and deep networks) in both 10-fold cross validation and the more rigorous Leave-One-Subject Out (LOSO) scheme. We also explore both binary and ternary classification of cognitive load. Certain individuals may not be able to distinguish cognitive load scores to that level of detail. This is precisely why we converted the scores to ‘binary’ (high/low) and ‘ternary’ (high/medium/low) levels using grouping of the scores. This initial high-resolution scheme, however, allows for future research to focus on more detailed classification schemes if necessary. For binary, we group the cognitive load ratings from 1 to 4 as ‘low’ cognitive load and 5 to 9 as ‘high’ cognitive load. For ternary, we divide the cognitive load ratings into 3 groups, 1 to 3, 4 to 6, and 7 to 9 which corresponds to ‘low’, ‘medium’, and ‘high’ cognitive load classes respectively. 

11 

TABLE VII: Architectural details of the VGG-style and ResNet-style networks used in this study for both features and raw signals. 

|**Modules**|**Parameters**|**VGG (feat.)**|**ResNet (feat.)**|**VGG (raw)**|**ResNet (raw)**|
|---|---|---|---|---|---|
|Conv1D|Kernel size<br>Filter size|-<br>-|1_×_3<br>32|-<br>-|1_×_32<br>64|
|Conv Block 1|Architecture<br>Activation<br>Kernel size|VGG<br>ReLU<br>1_×_3|ResNet<br>ReLU<br>1_×_3|VGG<br>ReLU<br>1_×_32|ResNet<br>ReLU<br>1_×_32|
||Filter size<br>Dropout rate|64<br>-|32<br>0.5|64<br>-|64<br>0.5|
|Conv Block 2|Architecture|VGG|ResNet|VGG|ResNet|
||Activation|ReLU|ReLU|ReLU|ReLU|
||Kernel size|1_×_3|1_×_3|1_×_16|1_×_16|
||Filter size|128|32|128|128|
||Dropout rate|-|0.5|-|0.5|
|Conv Block 3|Architecture|-|-|VGG|ResNet|
||Activation|-|-|ReLU|ReLU|
||Kernel size|-|-|1_×_8|1_×_8|
||Filter size|-|-|256|256|
||Dropout rate|-|-|-|0.5|
|Classifcation Block|Layer type|FC|FC|FC|FC|
||Number of layers<br>Dropout rate|2<br>0.25|3<br>-|2<br>0.25|3<br>0.25|
||Activation|ReLU|ReLU|ReLU|ReLU|



TABLE VIII: The accuracy and F1 scores for the classifiers in 10-fold binary setup. 

|||||Mod|alities|||||
|---|---|---|---|---|---|---|---|---|---|
|**Models**|EEG|EEG, ECG|EEG, EDA|EEG, Gaze|EEG, ECG<br>EDA|EEG, ECG<br>Gaze|EEG, EDA<br>Gaze|EEG, ECG<br>EDA, Gaze|Mean|
|AB|67.17 (55.37)|73.26 (68.43)|71.09 (66.53)|70.13 (61.29)|73.84 (69.85)|74.36 (69.75)|73.36 (69.07)|75.35 (71.80)|72.32 (66.51)|
|DT|65.31 (63.04)|72.77 (71.15)|69.61 (67.93)|68.17 (66.48)|73.02 (71.41)|73.12 (71.52)|72.39 (70.75)|73.98 (72.40)|71.05 (69.34)|
|NB|48.68 (46.54)|51.80 (50.48)|51.39 (49.97)|49.95 (48.22)|53.73 (52.87)|52.46 (51.35)|52.39 (51.23)|54.42 (53.65)|51.85 (50.54)|
|KNN|70.61 (68.49)|69.34 (67.40)|71.78 (70.16)|77.00 (74.65)|70.64 (69.16)|74.60 (71.97)|77.72 (75.46)|74.97 (72.50)|73.33 (71.22)|
|LDA|66.83 (62.45)|72.74 (70.65)|71.19 (68.45)|69.65 (66.24)|74.73 (72.94)|73.70 (71.61)|72.95 (70.62)|75.83 (74.04)|72.20 (69.63)|
|RF|**77.41 (73.39)**|79.34 (76.27)|79.48 (76.47)|79.89 (76.31)|81.26 (78.8)|80.82 (77.94)|80.65 (77.83)|81.71 (79.23)|80.07 (77.03)|
|SVM|61.88 (38.29)|62.08 (38.89)|61.88 (38.29)|63.46 (43.86)|64.35 (46.59)|71.54 (65.23)|67.14 (54.32)|73.70 (68.98)|65.75 (49.31)|
|XGB|77.38 (73.72)|**82.95 (81.25)**|**80.06 (77.67)**|**80.75 (78.06)**|**82.61 (80.94)**|**83.02 (81.22)**|**82.12 (80.08)**|**83.67 (82.05)**|81.57 (79.37)|
|MLP|74.32 (72.36)|74.22 (72.31)|76.31 (74.02)|75.18 (73.46)|76.00 (74.54)|75.83 (74.55)|77.11 (75.47)|77.69 (76.19)|75.83 (74.11)|
|VGG (feat.)|75.56 (73.21)|77.57 (75.8)|78.99 (76.94)|78.78 (76.74)|78.78 (77.22)|78.82 (77.23)|80.17 (78.39)|80.66 (79.17)|78.67 (68.31)|
|ResNet (feat.)|69.38 (65.26)|74.27 (71.48)|71.74 (68.46)|72.85 (69.15)|75.49 (72.71)|74.65 (71.83)|73.61 (70.67)|76.39 (74.28)|73.55 (70.48)|
|VGG (raw)|63.83 (63.23)|67.73 (66.97)|66.95 (66.11)|67.62 (66.95)|70.12 (69.2)|71.45 (70.5)|71.76 (71.07)|73.87 (73.00)|69.17 (68.38)|
|ResNet (raw)|61.95 (59.75)|64.49 (62.14)|60.90 (57.45)|66.68 (64.85)|64.41 (62.82)|70.04 (67.69)|68.71 (66.37)|69.96 (67.04)|65.89 (63.51)|
|Mean|67.72 (62.70)|70.97 (61.92)|70.11 (66.03)|70.78 (66.64)|72.23 (58.91)|73.42 (70.95)|73.08 (70.10)|74.78 (72.64)||



TABLE IX: The accuracy and F1 scores for the classifiers in LOSO binary setup. 

|||||Mod|alities|||||
|---|---|---|---|---|---|---|---|---|---|
|**Models**|EEG|EEG, ECG|EEG, EDA|EEG, Gaze|EEG, ECG<br>EDA|EEG, ECG<br>Gaze|EEG, EDA<br>Gaze|EEG, ECG<br>EDA, Gaze|Mean|
|AB|62.30 (46.81)|66.58 (59.47)|63.01 (54.57)|64.81 (53.53)|67.86 (62.22)|66.80 (60.05)|66.92 (59.68)|69.14 (63.60)|65.93 (57.49)|
|DT|54.63 (49.73)|60.33 (54.82)|57.94 (53.07)|57.57 (53.77)|60.97 (56.91)|62.13 (57.25)|61.19 (56.73)|62.00 (57.02)|59.60 (54.91)|
|NB|47.80 (43.54)|48.94 (45.80)|48.16 (44.71)|49.00 (45.06)|49.85 (47.52)|49.85 (47.11)|49.15 (45.71)|50.35 (48.06)|49.14 (45.94)|
|KNN|58.21 (53.11)|61.45 (58.09)|60.83 (56.10)|66.03 (61.42)|62.51 (59.51)|65.55 (61.10)|67.06 (62.48)|65.60 (61.36)|63.40 (59.15)|
|LDA|57.06 (49.61)|59.87 (55.67)|62.95 (56.99)|60.45 (54.25)|63.15 (58.60)|61.88 (57.75)|64.45 (58.97)|64.73 (60.26)|61.82 (56.51)|
|RF|63.82 (50.97)|65.76 (56.84)|66.64 (56.73)|65.79 (54.20)|67.95 (59.92)|66.50 (57.90)|68.94 (60.48)|70.15 (62.39)|66.94 (57.43)|
|SVM|62.01 (37.65)|59.85 (37.84)|61.80 (37.91)|62.56 (42.96)|61.48 (45.71)|66.26 (59.40)|65.94 (51.89)|68.53 (62.79)|63.55 (47.02)|
|XGB|62.98 (52.34)|66.61 (60.53)|66.39 (59.34)|66.67 (59.96)|69.37 (64.01)|68.81 (63.20)|69.73 (64.01)|71.48 (66.07)|67.76 (61.18)|
|MLP|57.86 (51.98)|63.64 (57.90)|63.44 (58.13)|61.45 (57.43)|64.48 (60.33)|61.32 (57.15)|65.72 (60.94)|64.51 (59.41)|62.80 (57.91)|
|VGG (feat.)|**70.70 (64.22)**|74.72 (70.68)|**73.01 (68.08)**|**74.68 (69.91)**|**76.17 (71.72)**|**76.04 (71.83)**|**75.49 (71.34)**|**75.52 (72.44)**|74.54 (70.03)|
|ResNet (feat.)|67.45 (61.39)|**75.90 (71.62)**|72.20 (66.48)|72.85 (67.53)|74.23 (69.28)|74.42 (70.32)|74.89 (69.49)|74.59 (69.55)|73.32 (68.21)|
|VGG (raw)|65.00 (58.92)|63.67 (57.59)|67.18 (60.78)|65.37 (59.81)|67.37 (60.84)|64.97 (58.51)|66.47 (61.79)|67.18 (61.37)|65.90 (59.95)|
|ResNet (raw)|65.79 (57.58)|63.99 (56.73)|69.03 (61.67)|68.03 (61.12)|68.74 (61.88)|66.67 (59.63)|66.50 (62.16)|67.69 (61.88)|67.06 (60.33)|
|Mean|61.20 (52.14)|63.95 (57.20)|64.04 (56.50)|64.25 (57.00)|65.70 (59.88)|65.48 (60.09)|66.34 (60.44)|67.04 (62.02)||



12 

TABLE X: The accuracy and F1 scores for the classifiers in 10-fold ternary setup. 

|||||Mod|alities|||||
|---|---|---|---|---|---|---|---|---|---|
|**Models**|EEG|EEG, ECG|EEG, EDA|EEG, Gaze|EEG, ECG<br>EDA|EEG, ECG<br>Gaze|EEG, EDA<br>Gaze|EEG, ECG<br>EDA, Gaze|Mean|
|AB|46.20 (38.35)|51.84 (48.65)|51.56 (48.78)|50.12 (44.48)|53.52 (51.62)|54.66 (51.69)|52.56 (49.66)|55.31 (53.15)|51.97 (48.30)|
|DT|48.95 (48.77)|56.03 (56.08)|52.08 (51.85)|52.70 (52.26)|57.48 (57.36)|58.82 (58.88)|56.14 (55.85)|58.13 (58.16)|55.04 (54.90)|
|NB|34.93 (29.77)|37.13 (33.00)|37.47 (33.77)|36.58 (31.86)|39.50 (36.55)|38.78 (35.06)|38.64 (35.23)|40.50 (37.74)|37.94 (34.12)|
|KNN|54.59 (53.95)|51.60 (50.81)|56.34 (55.90)|62.22 (62.01)|52.46 (51.67)|57.06 (56.33)|63.05 (62.87)|58.61 (57.93)|56.99 (56.43)|
|LDA|53.01 (51.93)|58.27 (58.09)|58.13 (57.82)|54.93 (54.33)|61.02 (61.00)|59.43 (59.23)|58.03 (57.89)|61.84 (61.84)|58.08 (57.77)|
|RF|63.56 (63.04)|68.41 (68.42)|69.34 (69.17)|68.30 (68.03)|71.57 (71.63)|70.40 (70.39)|71.67 (71.76)|72.67 (72.86)|69.49 (69.41)|
|SVM|41.01 (21.66)|46.58 (37.78)|41.73 (24.17)|48.75 (42.59)|48.40 (41.25)|53.01 (50.34)|50.39 (45.38)|53.83 (51.60)|47.96 (39.35)|
|XGB|**64.49 (64.14)**|**70.78 (71.01)**|**71.74 (71.69)**|**71.19 (71.22)**|**73.50 (73.76)**|**72.91 (73.15)**|**73.60 (73.61)**|**74.08 (74.26)**|71.54 (71.61)|
|MLP|58.44 (57.72)|61.50 (60.64)|61.12 (60.90)|62.63 (62.22)|62.80 (62.66)|63.08 (63.09)|63.84 (63.83)|63.25 (63.26)|62.08 (61.79)|
|VGG (feat.)|62.12 (60.92)|62.85 (62.21)|64.44 (63.91)|65.38 (64.88)|65.76 (65.37)|64.03 (63.43)|67.12 (66.72)|66.67 (66.04)|64.80 (64.19)|
|ResNet (feat.)|47.19 (44.61)|55.52 (53.74)|51.91 (50.66)|51.39 (49.41)|56.15 (55.48)|54.86 (53.88)|53.19 (52.24)|55.63 (54.67)|53.23 (51.84)|
|VGG (raw)|47.85 (43.7)|55.43 (51.37)|56.48 (51.61)|56.68 (52.24)|61.76 (57.96)|62.89 (58.3)|63.44 (59.41)|66.33 (62.93)|58.86 (54.69)|
|ResNet (raw)|50.82 (37.41)|56.56 (50.09)|53.67 (44.25)|56.37 (49.93)|60.62 (54.07)|59.38 (54.49)|61.05 (56.39)|64.84 (60.60)|57.91 (50.90)|
|Mean|51.78 (47.38)|56.35 (53.99)|55.85 (52.65)|56.71 (54.27)|58.81 (56.95)|59.18 (57.56)|59.44 (57.76)|60.90 (59.62)||



TABLE XI: The accuracy and F1 scores for the classifiers in LOSO ternary setup. 

|||||Mod|alities|||||
|---|---|---|---|---|---|---|---|---|---|
||||||EEGECG|EEGECG|EEGEDA|EEGECG||
|**Models**|EEG|EEG, ECG|EEG, EDA|EEG, Gaze|, <br>EDA|, <br>Gaze|, <br>Gaze|, <br>EDA, Gaze|Mean|
|AB|37.79 (27.09)|42.13 (34.39)|42.56 (36.04)|43.88 (36.63)|44.26 (38.46)|45.42 (37.95)|46.03 (39.76)|47.65 (41.81)|43.15 (35.76)|
|DT|35.83 (33.35)|40.15 (37.63)|37.37 (34.68)|37.69 (34.8)|35.77 (33.02)|40.32 (37.76)|37.58 (35.42)|39.15 (37.17)|37.82 (35.24)|
|NB|33.28 (26.3)|33.81 (27.37)|33.02 (27.85)|34.27 (28.04)|33.23 (28.40)|34.71 (28.59)|33.93 (29.18)|34.08 (29.40)|33.75 (27.96)|
|KNN|35.19 (32.87)|39.19 (37.06)|37.40 (34.97)|44.03 (41.90)|39.24 (37.31)|41.51 (39.82)|44.78 (42.45)|41.69 (40.04)|40.19 (38.05)|
|LDA|36.18 (33.64)|40.23 (37.02)|40.33 (37.61)|38.43 (36.29)|42.31 (39.07)|40.02 (37.22)|40.96 (38.78)|41.03 (38.45)|39.78 (37.09)|
|RF|37.02 (32.58)|40.15 (37.54)|39.97 (36.05)|43.03 (39.93)|42.28 (40.15)|43.11 (40.13)|45.31 (42.38)|44.96 (42.76)|41.55 (38.39)|
|SVM|38.48 (20.41)|39.66 (31.73)|38.42 (21.00)|42.46 (34.15)|39.83 (33.22)|44.69 (40.43)|43.13 (35.87)|45.05 (41.22)|40.95 (30.97)|
|XGB|36.09 (32.83)|40.06 (38.11)|41.63 (38.50)|43.26 (41.51)|44.48 (42.31)|43.44 (40.82)|46.14 (43.77)|47.10 (44.68)|42.16 (39.69)|
|MLP|38.30 (34.11)|39.30 (36.70)|41.44 (36.83)|44.23 (41.10)|42.04 (38.88)|41.68 (38.99)|46.05 (42.65)|42.94 (40.38)|41.86 (38.47)|
|VGG (feat.)|49.21 (43.75)|54.34 (48.93)|51.83 (47.64)|54.67 (49.85)|54.39 (50.96)|53.64 (49.99)|56.16 (52.17)|56.88 (52.98)|53.46 (49.04)|
|ResNet (feat.)|47.30 (42.08)|52.82 (49.44)|53.44 (47.1)|50.23 (46.15)|55.31 (50.65)|53.81 (49.49)|53.26 (49.16)|55.70 (51.02)|52.31 (47.72)|
|VGG (raw)|57.91 (44.12)|60.84 (47.61)|**58.86 (44.83)**|58.08 (44.08)|**61.29 (49.18)**|63.04 (49.47)|57.01 (45.06)|**63.56 (49.39)**|59.58 (46.34)|
|ResNet (raw)|**58.13 (42.54)**|**60.86 (47.30)**|58.22 (43.81)|**60.37 (45.90)**|60.12 (46.68)|**64.53 (51.40)**|**58.65 (46.27)**|61.55 (49.93)|60.13 (46.27)|
|Mean|41.59 (34.28)|44.89 (39.29)|44.19 (37.45)|45.74 (40.03)|45.73 (40.64)|46.92 (41.70)|46.85 (41.76)|47.80 (43.02)||



## V. BENCHMARKING RESULTS 

Here, we present the results of the benchmarking study for binary and ternary classification in both validation schemes. We also present a comparison for the different multimodal setups in our experiments. The detailed results are presented in Tables VIII, IX, X, and XI. In these tables, bold values denote the highest, while underline represents the second-highest. As we observe in Table VIII, for 10-fold cross-validation in the binary setup, we obtain the highest accuracy of 83.67% with the XGB classifier. This performance is achieved when all 4 modalities are used. This is followed by 83.02% as the second best obtained with EEG with ECG and Gaze by the same classifier. Comparing the average values obtained for different modality setups indicates that as expected, EEG, ECG, EDA, and Gaze altogether outperform the rest, followed by trimodal, bi-modal, and uni-modal setups, respectively. Looking at the average values for all the models we observe that the XGB classifier generally outperforms the rest followed by RF. Among the 4 different deep learning variants in this setup, we notice that VGG trained with features from all 4 modalities outperforms the other 3 scenarios. 

In Table IX, for the binary LOSO evaluation scheme, we observe that the highest accuracy of 76.17% is obtained by the VGG-style network trained with features. This accuracy is obtained using 3 modalities, namely EEG, ECG and EDA. The second best accuracy, 76.04%, is achieved with the combination of EEG, ECG, and Gaze. Comparing the average values from different modality setups, we observe that the highest accuracy is obtained by the multimodal scenario with 

all 4 modalities, followed by the tri-modal, bi-modal, and unimodal setups respectively. From the average values for each model, we can deduce that the VGG-style model trained on features performs the best, followed by the ResNet-style model trained on features. 

We present the results for the ternary 10-fold setup in Table X, and we observe that the best result of 74.08% is achieved with the machine learning classifier, XGB. This result is obtained when EEG is trained along with all 3 auxiliary modalities. The second best accuracy of 73.60% is obtained with the same classifier when EEG, EDA, and Gaze are used together. Comparing the average results for each modality setup, we find that as expected, the using all 4 modalities outperforms the rest while the best performing average result is achieved by the XGB classifier. Among the 4 deep learning models, the VGG-style model outperforms the other 3 when trained with features. Here, the highest accuracy of 67.12% is obtained when trained with 3 modalities EEG, EDA, and Gaze. 

Lastly, Table XI shows us the result in the LOSO ternary setup. The highest result obtained is 64.53% when using the ResNet-style network trained with the raw data with 3 modalities namely EEG, ECG, and Gaze. Following, the second highest accuracy of 63.56% is obtained by the VGGstyle network trained on raw data from all 4 modalities. The average results of various modality setups show that the multimodal setup with all 4 modalities achieves the highest accuracy. The average highest accuracy is obtained using the ResNet-style model followed by the VGG-style model both 

13 

when trained with raw data. 

In the end, to summarize our findings above, we observe that both classical machine learning and deep learning models possess the ability to distinguish between different levels of driver cognitive loads. As expected, we find that ternary classification is more challenging than binary, while LOSO on the other hand proves more difficult than 10-fold. In terms of modalities, multimodal setups generally provide more information regarding driver cognitive load, with EEG, ECG, EDA and Gaze showing the best performances. 

## _A. Limitations_ 

While our work makes significant contributions to the area, there exist a few areas in which our work could be improved. For instance, using a driving simulator versus real vehicles offers a safe alternative, reduces the risk of accidents and injuries, and allows us to design very specific driving scenarios by controlling the weather, time of day, road conditions, obstacles, number of cars on the road, etc., that are applicable across all the participants. On the other hand, the disadvantage of using a simulator is the possibility of participants experiencing SAS, as well as limited motion and the use of generated graphics that may not fully replicate the experience of realworld driving. 

The number of participants (6M+15F = total of 21) in our study is in line with other datasets such as SEED (7M+8F = total of 15), SEED-IV (7M+8F = total of 15), SEED-VIG (11M+12F = total of 23), and others. However, we acknowledge that adding more participants and further balancing the demographics in terms of factors such as gender can help increase generalization of the findings and improve diversity in the data, which can lead to more effective machine learning models. 

Lastly, another area that could be discussed is the use of participant-reported subjective measurements for cognitive load. It should be noted that while advanced brain scanning technologies could be used to measure cognitive load more objectively, such self-reported methods are consistently relied upon in the literature to obtain labels or scores with which to train machine learning models. Additionally, the fact that the trained models are capable of making strong predictions, points to the reliability of the output labels. To reduce the possible subjectivity of self-reported scores, larger datasets may be used, in addition to deep learning paradigms such as weakly supervised or partial-label learning. 

## VI. CONCLUSION 

In this paper, we presented CL-Drive, a new multimodal cognitive load dataset collected during simulated driving. Our dataset, which we made public, contains EEG, ECG, EDA, and Gaze data from 21 participants in a variety of different driving conditions. Subjective self-reported cognitive load scores were recorded at 10-second intervals throughout the experiment, making it a very rich and dense dataset in terms of both modalities and labels. We also provided benchmarks by evaluating our dataset in both binary and ternary label distributions for 

both LOSO as well as k-fold evaluation schemes. The CLDrive dataset can have various applications in the field of transportation, driver safety, and human-machine interaction. The dataset can be used to assess the cognitive workload experienced by drivers in various driving scenarios, such as high-traffic conditions, adverse weather, or during complex maneuvers. Overall, the CL-Drive dataset has the potential to improve road safety, enhance driver experience, and contribute to the development of more intelligent and human-centered transportation systems. 

## VII. ACKNOWLEDGEMENT 

We would like to thank the Innovation for Defence Excellence and Security (IDEaS) program under the Department of National Defence (DND) for funding this project. 

## REFERENCES 

- [1] M. Miyaji, H. Kawanaka, and K. Oguri, “Driver’s cognitive distraction detection using physiological features by the adaboost,” in _12th International IEEE Conference on Intelligent Transportation Systems_ . IEEE, 2009, pp. 1–6. 

- [2] O. Palinko, A. L. Kun, A. Shyrokov, and P. Heeman, “Estimating cognitive load using remote eye tracking in a driving simulator,” in _Proceedings of the Symposium on Eye-tracking Research & Applications_ , 2010, pp. 141–144. 

- [3] L. Fridman, B. Reimer, B. Mehler, and W. T. Freeman, “Cognitive load estimation in the wild,” in _Proceedings of the Chi Conference on Human Factors in Computing Systems_ , 2018, pp. 1–9. 

- [4] A. Y¨uce, H. Gao, G. L. Cuendet, and J.-P. Thiran, “Action units and their cross-correlations for prediction of cognitive load during driving,” _IEEE Transactions on Affective Computing_ , vol. 8, no. 2, pp. 161–175, 2016. 

- [5] E. Q. Wu, D. Hu, P.-Y. Deng, Z. Tang, Y. Cao, W.-M. Zhang, L.M. Zhu, and H. Ren, “Nonparametric bayesian prior inducing deep network for automatic detection of cognitive status,” _IEEE Transactions on Cybernetics_ , vol. 51, no. 11, pp. 5483–5496, 2020. 

- [6] E. Q. Wu, Z. Tang, Y. Yao, X.-Y. Qiu, P.-Y. Deng, P. Xiong, A. Song, L.M. Zhu, and M. Zhou, “Scalable gamma-driven multilayer network for brain workload detection through functional near-infrared spectroscopy,” _IEEE Transactions on Cybernetics_ , vol. 52, no. 11, pp. 12 464–12 478, 2021. 

- [7] J. Sweller, “Cognitive load theory,” in _Psychology of Learning and Motivation_ . Elsevier, 2011, vol. 55, pp. 37–76. 

- [8] R. Das, D. Chatterjee, D. Das, A. Sinharay, and A. Sinha, “Cognitive load measurement-a methodology to compare low cost commercial eeg devices,” in _International Conference on Advances in Computing, Communications and Informatics_ . IEEE, 2014, pp. 1188–1194. 

- [9] S. Schneegass, B. Pfleging, N. Broy, F. Heinrich, and A. Schmidt, “A data set of real world driving to assess driver workload,” in _Proceedings of the 5th International Conference on Automotive User Interfaces and Interactive Vehicular Applications_ , 2013, pp. 150–157. 

- [10] I. Miji´c, M. Sarlija, and D. Petrinovi´c, “Mmod-cog: A database for mul-<sup>ˇ</sup> timodal cognitive load classification,” in _11th International Symposium on Image and Signal Processing and Analysis_ . IEEE, 2019, pp. 15–20. 

- [11] V. Markova, T. Ganchev, and K. Kalinkov, “Clas: A database for cognitive load, affect and stress recognition,” in _International Conference on Biomedical Innovations and Applications_ . IEEE, 2019, pp. 1–4. 

- [12] M. Gjoreski, T. Kolenik, T. Knez, M. Luˇstrek, M. Gams, H. Gjoreski, and V. Pejovi´c, “Datasets for cognitive load inference using wearable sensors and psychological traits,” _Applied Sciences_ , vol. 10, no. 11, p. 3843, 2020. 

- [13] A. Kalatzis, A. Teotia, V. G. Prabhu, and L. Stanley, “A database for cognitive workload classification using electrocardiogram and respiration signal,” in _International Conference on Applied Human Factors and Ergonomics_ . Springer, 2021, pp. 509–516. 

- [14] P. Sarkar, K. Ross, A. J. Ruberto, D. Rodenbura, P. Hungler, and A. Etemad, “Classification of cognitive load and expertise for adaptive simulation using deep multitask learning,” in _8th International Conference on Affective Computing and Intelligent Interaction_ . IEEE, 2019, pp. 1–7. 

14 

- [15] K. Ross, P. Sarkar, D. Rodenburg, A. Ruberto, P. Hungler, A. Szulewski, D. Howes, and A. Etemad, “Toward dynamically adaptive simulation: Multimodal classification of user expertise using wearable devices,” _Journal of Sensors_ , vol. 19, no. 19, p. 4270, 2019. 

- [16] R. Brunken, J. L. Plass, and D. Leutner, “Direct measurement of cognitive load in multimedia learning,” _Educational Psychologist_ , vol. 38, no. 1, pp. 53–61, 2003. 

- [17] R. E. Mayer and R. Moreno, “Aids to computer-based multimedia learning,” _Learning and Instruction_ , vol. 12, no. 1, pp. 107–119, 2002. 

- [18] M. Klepsch, F. Schmitz, and T. Seufert, “Development and validation of two instruments measuring intrinsic, extraneous, and germane cognitive load,” _Frontiers in Psychology_ , vol. 8, p. 1997, 2017. 

- [19] F. G. Paas, “Training strategies for attaining transfer of problem-solving skill in statistics: a cognitive-load approach,” _Journal of Educational Psychology_ , vol. 84, no. 4, p. 429, 1992. 

- [20] S. G. Hart and L. E. Staveland, “Development of nasa-tlx (task load index): Results of empirical and theoretical research,” in _Advances in Psychology_ . Elsevier, 1988, vol. 52, pp. 139–183. 

- [21] R. Br¨unken, S. Steinbacher, J. L. Plass, and D. Leutner, “Assessment of cognitive load in multimedia learning using dual-task methodology.” _Experimental Psychology_ , vol. 49, no. 2, p. 109, 2002. 

- [22] B. Park and R. Br¨unken, “The rhythm method: A new method for measuring cognitive load—an experimental dual-task study,” _Applied Cognitive Psychology_ , vol. 29, no. 2, pp. 232–243, 2015. 

- [23] P. W. Van Gerven, F. Paas, J. J. Van Merri¨enboer, and H. G. Schmidt, “Memory load and the cognitive pupillary response in aging,” _Psychophysiology_ , vol. 41, no. 2, pp. 167–174, 2004. 

- [24] S. Chen and J. Epps, “Using task-induced pupil diameter and blink rate to infer cognitive load,” _Human–Computer Interaction_ , vol. 29, no. 4, pp. 390–413, 2014. 

- [25] F. G. Paas and J. J. Van Merri¨enboer, “Variability of worked examples and transfer of geometrical problem-solving skills: A cognitive-load approach,” _Journal of Educational Psychology_ , vol. 86, no. 1, p. 122, 1994. 

- [26] P. Antonenko, F. Paas, R. Grabner, and T. Van Gog, “Using electroencephalography to measure cognitive load,” _Educational Psychology Review_ , vol. 22, no. 4, pp. 425–438, 2010. 

- [27] S. Chisholm, J. K. Caird, and J. Lockhart, “The effects of practice with mp3 players on driving performance,” _Accident Analysis & Prevention_ , vol. 40, no. 2, pp. 704–713, 2008. 

- [28] D. He, B. Donmez, C. C. Liu, and K. N. Plataniotis, “High cognitive load assessment in drivers through wireless electroencephalography and the validation of a modified n-back task,” _IEEE Transactions on HumanMachine Systems_ , vol. 49, no. 4, pp. 362–371, 2019. 

- [29] S. Barua, M. U. Ahmed, and S. Begum, “Classifying drivers’ cognitive load using eeg signals.” in _pHealth_ , 2017, pp. 99–106. 

- [30] N. M. Yusof, J. Karjanto, M. Z. Hassan, J. Terken, F. Delbressine, and M. Rauterberg, “Reading during fully automated driving: a study of the effect of peripheral visual and haptic information on situation awareness and mental workload,” _IEEE transactions on intelligent transportation systems_ , vol. 23, no. 10, pp. 19 136–19 144, 2022. 

- [31] Z. Jiang, X. He, C. Lu, B. Zhou, X. Fan, C. Wang, X. Ma, E. C. Ngai, and L. Chen, “Understanding drivers’ visual and comprehension loads in traffic violation hotspots leveraging crowd-based driving simulation,” _IEEE transactions on intelligent transportation systems_ , vol. 23, no. 12, pp. 23 369–23 383, 2022. 

- [32] J. Ayoub, N. Du, X. J. Yang, and F. Zhou, “Predicting driver takeover time in conditionally automated driving,” _IEEE transactions on intelligent transportation systems_ , vol. 23, no. 7, pp. 9580–9589, 2022. 

- [33] B. Mehler, B. Reimer, J. F. Coughlin, and J. A. Dusek, “Impact of incremental increases in cognitive workload on physiological arousal and performance in young adult drivers,” _Transportation Research Record_ , vol. 2138, no. 1, pp. 6–12, 2009. 

- [34] B. Mehler, B. Reimer, and J. F. Coughlin, “Sensitivity of physiological measures for detecting systematic variations in cognitive demand from a working memory task: an on-road study across three age groups,” _Human Factors_ , vol. 54, no. 3, pp. 396–412, 2012. 

- [35] J. L. Kolodner, “An introduction to case-based reasoning,” _Artificial Intelligence Review_ , vol. 6, no. 1, pp. 3–34, 1992. 

- [36] M. Braun, J. Schubert, B. Pfleging, and F. Alt, “Improving driver emotions with affective strategies,” _Multimodal Technologies and Interaction_ , vol. 3, no. 1, p. 21, 2019. 

- [37] C. Nass, I.-M. Jonsson, H. Harris, B. Reaves, J. Endo, S. Brave, and L. Takayama, “Improving automotive safety by pairing driver emotion and car voice emotion,” in _CHI’05 Extended Abstracts on Human Factors in Computing Systems_ , 2005, pp. 1973–1976. 

- [38] S. Zepf, J. Hernandez, A. Schmitt, W. Minker, and R. W. Picard, “Driver emotion recognition for intelligent vehicles: A survey,” _ACM Computing Surveys (CSUR)_ , vol. 53, no. 3, pp. 1–30, 2020. 

- [39] G. Zhang and A. Etemad, “Capsule attention for multimodal eeg-eog representation learning with application to driver vigilance estimation,” _IEEE Transactions on Neural Systems and Rehabilitation Engineering_ , vol. 29, pp. 1138–1149, 2021. 

- [40] L. M. Bergasa, J. Nuevo, M. A. Sotelo, R. Barea, and M. E. Lopez, “Real-time system for monitoring driver vigilance,” _IEEE Transactions on Intelligent Transportation Systems_ , vol. 7, no. 1, pp. 63–77, 2006. 

- [41] C.-T. Lin, C.-H. Chuang, C.-S. Huang, S.-F. Tsai, S.-W. Lu, Y.-H. Chen, and L.-W. Ko, “Wireless and wearable eeg system for evaluating driver vigilance,” _IEEE Transactions on Biomedical Circuits and Systems_ , vol. 8, no. 2, pp. 165–176, 2014. 

- [42] Z. Emami and T. Chau, “The effects of visual distractors on cognitive load in a motor imagery brain-computer interface,” _Behavioural Brain Research_ , vol. 378, p. 112240, 2020. 

- [43] W. J. Chai, A. I. Abd Hamid, and J. M. Abdullah, “Working memory from the psychological and neurosciences perspectives: a review,” _Frontiers in Psychology_ , vol. 9, p. 401, 2018. 

- [44] S. Siuly, Y. Li, and Y. Zhang, “Eeg signal analysis and classification,” _IEEE Transactions on Neural Systems and Rehabilitation Engineering_ , vol. 11, pp. 141–144, 2016. 

- [45] W. Klimesch, “Eeg alpha and theta oscillations reflect cognitive and memory performance: a review and analysis,” _Brain Research Reviews_ , vol. 29, no. 2–3, pp. 169–195, 1999. 

- [46] K. Ross, P. Hungler, and A. Etemad, “Unsupervised multi-modal representation learning for affective computing with multi-corpus wearable data,” _Journal of Ambient Intelligence and Humanized Computing_ , pp. 1–26, 2021. 

- [47] R. Xiong, F. Kong, X. Yang, G. Liu, and W. Wen, “Pattern recognition of cognitive load using eeg and ecg signals,” _Journal of Sensors_ , vol. 20, no. 18, p. 5122, 2020. 

- [48] A. M. Hughes, G. M. Hancock, S. L. Marlow, K. Stowers, and E. Salas, “Cardiac measures of cognitive workload: a meta-analysis,” _Human Factors_ , vol. 61, no. 3, pp. 393–414, 2019. 

- [49] E. Johannessen, A. Szulewski, N. Radulovic, M. White, H. Braund, D. Howes, D. Rodenburg, and C. Davies, “Psychophysiologic measures of cognitive load in physician team leaders during trauma resuscitation,” _Computers in Human Behavior_ , vol. 111, p. 106393, 2020. 

- [50] J. Zagermann, U. Pfeil, and H. Reiterer, “Measuring cognitive load using eye tracking technology in visual computing,” in _Proceedings of the 6th Workshop on Beyond Time and Errors on Novel Evaluation Methods for Visualization_ , 2016, pp. 78–85. 

- [51] S. T. Iqbal, P. D. Adamczyk, X. S. Zheng, and B. P. Bailey, “Understanding changes in mental workload during task execution,” Tech. Rep., 2004. 

- [52] J. Engstr¨om, G. Markkula, T. Victor, and N. Merat, “Effects of cognitive load on driving performance: The cognitive control hypothesis,” _Human Factors_ , vol. 59, no. 5, pp. 734–764, 2017. 

- [53] P. Sena, M. d’Amore, M. Pappalardo, A. Pellegrino, A. Fiorentino, and F. Villecco, “Studying the influence of cognitive load on driver’s performances by a fuzzy analysis of lane keeping in a drive simulation,,” _IFAC Proceedings Volumes_ , vol. 46, no. 21, pp. 151–156, 2013. 

- [54] L. Caba˜nero, R. Herv´as, I. Gonz´alez, J. Fontecha, T. Mond´ejar, and J. Bravo, “Analysis of cognitive load using eeg when interacting with mobile devices,” _Multidisciplinary Digital Publishing Institute Proceedings_ , vol. 31, no. 1, p. 70, 2019. 

- [55] I. Volman, K. Roelofs, S. Koch, L. Verhagen, and I. Toni, “Anterior prefrontal cortex inhibition impairs control over social emotional actions,” _Current biology_ , vol. 21, no. 20, pp. 1766–1770, 2011. 

- [56] G. Zhang and A. Etemad, “Deep recurrent semi-supervised eeg representation learning for emotion recognition,” in _9th International Conference on Affective Computing and Intelligent Interaction_ . IEEE, 2021, pp. 1–8. 

- [57] G. Zhang, V. Davoodnia, and A. Etemad, “Parse: Pairwise alignment of representations in semi-supervised eeg learning for emotion recognition,” _IEEE Transactions on Affective Computing_ , 2022. 

- [58] J. R. Stroop, “Studies of interference in serial verbal reactions.” _Journal of Experimental Psychology_ , vol. 18, no. 6, p. 643, 1935. 

- [59] F. Schmiedek, M. L¨ovd´en, and U. Lindenberger, “A task is a task is a task: putting complex span, n-back, and other working memory indicators in psychometric context,” _Frontiers in Psychology_ , vol. 5, p. 1475, 2014. 

- [60] Y. Santiago-Espada, R. R. Myer, K. A. Latorella, and J. R. Comstock Jr, “The multi-attribute task battery ii (matb-ii) software for human performance and workload research: A user’s guide,” Tech. Rep., 2011. 

15 

- [61] A. Morley, L. Hill, and A. Kaditis, “10-20 system eeg placement,” _European Respiratory Society, European Respiratory Society_ , 2016. 

- [62] V. Jurcak, D. Tsuzuki, and I. Dan, “10/20, 10/10, and 10/5 systems revisited: their validity as relative head-surface-based positioning systems,” _Neuroimage_ , vol. 34, no. 4, pp. 1600–1611, 2007. 

- [63] A. Burns, B. R. Greene, M. J. McGrath, T. J. O’Shea, B. Kuris, S. M. Ayer, F. Stroiescu, and V. Cionca, “SHIMMER–a wireless sensor platform for noninvasive biomedical research,” _IEEE Sensors Journal_ , vol. 10, no. 9, pp. 1527–1534, 2010. 

- [64] M. Rizzo, P. A. Sheffield, L. Stierman, and J. Dawson, “Demographic and driving performance factors in simulator adaptation syndrome,” in _Driving Assesment Conference_ , vol. 2, no. 2003. University of Iowa, 2003. 

- [65] J. G. Reed-Jones, W. J. Reed-Jones, L. M. Trick, R. Toxopeus, and L. A. Vallis, “Comparing techniques to reduce simulator adaptation syndrome and improve naturalistic behaviour during simulated driving,” in _Driving Assesment Conference_ , vol. 5, no. 2009. University of Iowa, 2009. 

- [66] T. G. Dobie, _Motion sickness: a motion adaptation syndrome_ . Springer, 2019, vol. 6. 

   - [85] I. Kalamaras, A. Zamichos, A. Salamanis, A. Drosou, D. D. Kehagias, G. Margaritis, S. Papadopoulos, and D. Tzovaras, “An interactive visual analytics platform for smart intelligent transportation systems management,” _IEEE Transactions on Intelligent Transportation Systems_ , vol. 19, no. 2, pp. 487–496, 2017. 

   - [86] Z. Li, G. Xiong, Y. Tian, Y. Lv, Y. Chen, P. Hui, and X. Su, “A multistream feature fusion approach for traffic prediction,” _IEEE transactions on intelligent transportation systems_ , vol. 23, no. 2, pp. 1456–1466, 2020. 

   - [87] Y. Chen, T. Shu, X. Zhou, X. Zheng, A. Kawai, K. Fueda, Z. Yan, W. Liang, I. Kevin, and K. Wang, “Graph attention network with spatial-temporal clustering for traffic flow forecasting in intelligent transportation system,” _IEEE Transactions on Intelligent Transportation Systems_ , 2022. 

   - [88] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,” _International Conference on Learning Representations_ , 2015. 

   - [89] W.-L. Zheng, W. Liu, Y. Lu, B.-L. Lu, and A. Cichocki, “Emotionmeter: A multimodal framework for recognizing human emotions,” _IEEE Transactions on Cybernetics_ , vol. 49, no. 3, pp. 1110–1122, 2018. 

- [67] S. V. Cobb, S. Nichols, A. Ramsey, and J. R. Wilson, “Virtual realityinduced symptoms and effects (vrise),” _Presence: Teleoperators & Virtual Environments_ , vol. 8, no. 2, pp. 169–186, 1999. 

- [68] G. G´alvez-Garc´ıa, J. Albayay, L. Rehbein, and F. Tornay, “Mitigating simulator adaptation syndrome by means of tactile stimulation,” _Applied Ergonomics_ , vol. 58, pp. 13–17, 2017. 

- [69] L. Frank, R. S. Kennedy, R. S. Kellogg, and M. E. McCauley, “Simulator sickness: A reaction to a transformed perceptual world. 1. scope of the problem,” ESSEX CORP ORLANDO FL, Tech. Rep., 1983. 

- [70] R. S. Kennedy, N. E. Lane, K. S. Berbaum, and M. G. Lilienthal, “Simulator sickness questionnaire: An enhanced method for quantifying simulator sickness,” _The International Journal of Aviation Psychology_ , vol. 3, no. 3, pp. 203–220, 1993. 

- [71] P. J. Gianaros, E. R. Muth, J. T. Mordkoff, M. E. Levine, and R. M. Stern, “A questionnaire for the assessment of the multiple dimensions of motion sickness,” _Aviation, Space, and Environmental Medicine_ , vol. 72, no. 2, p. 115, 2001. 

- [72] F. G. Paas, “Training strategies for attaining transfer of problem-solving skill in statistics: a cognitive-load approach.” _Journal of Educational Psychology_ , vol. 84, no. 4, p. 429, 1992. 



**Prithila Angkan** Prithila Angkan is currently pursuing her Ph.D. at Queen’s University in Canada in the Department of Electrical and Computer Engineering. She received her master’s degree from the same department at Queen’s University and her bachelor’s from BRAC University, Bangladesh. Currently, she is a member of Ambient Intelligence and Interactive Machines Laboratory (Aiim Lab) and Ingenuity Labs Research Institute at Queen’s University. Her research focuses on Brain-Computer Interface, Artificial Intelligence, Cognitive Load Analysis, Affective Computing, and Deep Learning utilizing Electroencephalogram (EEG) signals. 

- [73] N. Thakor, J. Webster, and W. Tompkins, “Optimal qrs detector,” _Medical and Biological Engineering and Computing_ , vol. 21, no. 3, pp. 343–350, 1983. 

- [74] H. G. Goovaerts, H. H. Ros, T. J. Van Den Akker, and H. Schneider, “A digital qrs detector based on the principle of contour limiting,” _IEEE Transactions on Biomedical Engineering_ , no. 2, pp. 154–160, 1976. 

- [75] C. L. Lim, C. Rennie, R. J. Barry, H. Bahramali, I. Lazzaro, B. Manor, and E. Gordon, “Decomposing skin conductance into tonic and phasic components,” _International Journal of Psychophysiology_ , vol. 25, no. 2, pp. 97–109, 1997. 

- [76] C. E. Shannon, “A mathematical theory of communication,” _The Bell System Technical Journal_ , vol. 27, no. 3, pp. 379–423, 1948. 

- [77] B. Hjorth, “Eeg analysis based on time domain properties,” _Electroencephalography and Clinical Neurophysiology_ , vol. 29, no. 3, pp. 306– 310, 1970. 

- [78] A. Lempel and J. Ziv, “On the complexity of finite sequences,” _IEEE Transactions on Information Theory_ , vol. 22, no. 1, pp. 75–81, 1976. 



**Behnam Behinaein** Behnam Behinaein received his PhD from Queen’s University in 2016 and was a post-doctoral fellow in QDES and Aiim Labs. He is currently with Huawei Canada. His research interests include affect computing, wearable technologies, and the application of deep learning in analyzing sequential data. 

- [79] F. Kaspar and H. Schuster, “Easily calculable measure for the complexity of spatiotemporal patterns,” _Physical Review A_ , vol. 36, no. 2, p. 842, 1987. 

- [80] T. Higuchi, “Approach to an irregular time series on the basis of the fractal theory,” _Physica D: Nonlinear Phenomena_ , vol. 31, no. 2, pp. 277–283, 1988. 

- [81] A. H. Al-Nuaimi, E. Jammeh, L. Sun, and E. Ifeachor, “Higuchi fractal dimension of the electroencephalogram as a biomarker for early detection of alzheimer’s disease,” in _39th Annual International Conference of the IEEE Engineering in Medicine and Biology Society_ . IEEE, 2017, pp. 2320–2324. 

- [82] E. Shamsi, M. A. Ahmadi-Pajouh, and T. S. Ala, “Higuchi fractal dimension: An efficient approach to detection of brain entrainment to theta binaural beats,” _Biomedical Signal Processing and Control_ , vol. 68, p. 102580, 2021. 

- [83] F. Shaffer and J. P. Ginsberg, “An overview of heart rate variability metrics and norms,” _Frontiers in Public Health_ , p. 258, 2017. 

- [84] P. Sarkar and A. Etemad, “Self-supervised ecg representation learning for emotion recognition,” _IEEE Transactions on Affective Computing_ , 2020. 

**Zunayed Mahmud** Zunayed Mahmud received the M.A.Sc. degree from the Department of Electrical and Computer Engineering at Queen’s University, Canada, in 2022. Concurrently, he served as a Student Researcher at the Ingenuity Labs Research Institute, Canada. He earned his bachelor’s degree from the Department of Electrical and Electronic Engineering at BRAC University, Bangladesh, in 2015. He is currently working as an Associate Researcher at Huawei Technologies Canada. His research interests include computer vision, deep learning, 2D/3D object detection and recognition, 3D reconstruction, and gaze estimation. 

16 

**Anubhav Bhatti** Anubhav Bhatti is a machine learning engineer at SpassMed Inc. His journey in machine learning previously led him to the Vector Institute as a Machine Learning Associate. He received his Master’s in Artificial Intelligence from the Electrical and Computer Engineering Department at Queen’s University, Canada, and his bachelor’s in electrical engineering from the National Institute of Technology, India. In his research work at Vector Institute and SpassMed, he leverages his expertise in Large Language Models, Generative AI, and Time Series Forecasting in designing and implementing deep-learning models for the early detection of critical events in patients. While at Queen’s University and Ingenuity Labs Research Institute, he extensively researched multimodal time-series physiological data fusion techniques and affective computing. 



**Dirk Rodenburg** Dr. Rodenburg is an Adjunct Professor with the Queen’s University Smith School of Engineering’s Department of Chemical Engineering, and the Faculty of Arts and Science. Dirk’s research interests include human performance, expertise, cognition, real time data analytics, data feedback, human-computer interaction, and ethics and privacy. In addition to his academic background, he has twenty years of experience as a software entrepreneur and consultant within academia, educational technology, financial services, biotechnology and scientific instruments, and has played an integral role in the launch of three highly innovative startups. Dirk holds an MA in Adult Education from the University of British Columbia and a PhD from the Faculty of Information from the University of Toronto. 



**Paul Hungler** Dr. Paul Hungler is an Associate Professor in the Department of Chemical Engineering and Ingenuity Labs at Smith Engineering, Queen’s University. Dr. Hungler’s research is focused on the development of intelligent, dynamically adaptive simulation to enhance education and training. 

**Ali Etemad** Dr. Etemad is an Associate Professor at the Department of Electrical and Computer Engineering, Queen’s University. He holds an endowed professership of Mitchell Professor in AI for Human Sensing and Understanding. He leads the Ambient Intelligence and Interactive Machines (Aiim) lab. He received his M.A.Sc. and Ph.D. degrees in Electrical and Computer Engineering from Carleton University, Ottawa, Canada, in 2009 and 2014, respectively. His main areas of research are machine learning and deep learning focused on human-centered applications with wearables, smart devices, and smart environments. Prior to joining Queen’s, he held several industrial positions as lead scientist. He has published over 160 papers in top venues in the area, is a co-inventor of 10 patents, and has given over 25 invited talks at different venues. Dr. Etemad is an Associate Editor for IEEE Transactions on Affective Computing and IEEE Transactions on Artificial Intelligence. He has served as a PC member/reviewer, and has held organizing roles at various venues. He has received a number of awards including Supervisor of the Year Award (at Queen’s), Instructor of the Year Award (at Queen’s), and several Best Paper Awards (e.g., at ACM ICMI’23). Dr. Etemad’s lab and research program have been funded by the Natural Sciences and Engineering Research Council (NSERC) of Canada, Ontario Centers of Excellence (OCE), Canadian Foundation for Innovation (CFI), Mitacs, and other organizations, as well as the private sector. 

