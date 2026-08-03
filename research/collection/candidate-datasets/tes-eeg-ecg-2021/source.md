www.nature.com/scientificdata 



# **OPEN Dataset of concurrent EEG, ECG, and behavior with multiple doses of transcranial electrical stimulation** 

## **Data DESCriPtOr** 

**Nigel Gebodh**<sup>**1,2**✉</sup> **, Zeinab Esmaeilpour**<sup>**1**</sup> **, abhishek Datta**<sup>**2**</sup> **& Marom Bikson**<sup>**1**</sup> 

**We present a dataset combining human-participant high-density electroencephalography (EEG) with physiological and continuous behavioral metrics during transcranial electrical stimulation (tES). Data include within participant application of nine High-Definition tES (HD-tES) types, targeting three cortical regions (frontal, motor, parietal) with three stimulation waveforms (DC, 5 Hz, 30 Hz); more than 783 total stimulation trials over 62 sessions with EEG, physiological (ECG, EOG), and continuous behavioral vigilance/alertness metrics. Experiment 1 and 2 consisted of participants performing a continuous vigilance/alertness task over three 70-minute and two 70.5-minute sessions, respectively. Demographic data were collected, as well as self-reported wellness questionnaires before and after each session. Participants received all 9 stimulation types in Experiment 1, with each session including three stimulation types, with 4 trials per type. Participants received two stimulation types in Experiment 2, with 20 trials of a given stimulation type per session. Within-participant reliability was tested by repeating select sessions. this unique dataset supports a range of hypothesis testing including interactions of tDCS/taCS location and frequency, brain-state, physiology, fatigue, and cognitive performance.** 

### **Background & Summary** 

Transcranial electrical stimulation (tES), including its variants: transcranial Direct Current Stimulation (tDCS) and transcranial Alternating Current Stimulation (tACS), allows for testing of causal relationship between brain function and cognition<sup>1–3</sup> . In recent years, hundreds of tES trials have broadly impacted fields of cognitive neuroscience and behavioral performance<sup>4,5</sup> , alongside intensive testing as clinical treatments<sup>6–8</sup> . tES efficacy is rationalized to depend on waveform (AC frequency or DC) and targeted brain region. The use of High-Definition tES (HD-tES) allows for localized targeting of cortical regions<sup>9</sup> , which can be combined with variations in stimulation waveform<sup>10–12</sup> . 

The combination of tES with brain imaging techniques<sup>13–17</sup> , notably EEG, allows for verification of neural target engagement<sup>7,8,18</sup> , optimization of interventions<sup>10,19</sup> , and powerful analysis of brain structure and functional relationships<sup>3</sup> . Analysis of online tES-EEG experiments are not without technical challenges<sup>20–23</sup> . 

In the field of brain stimulation or neuromodulation, the development of open-source tools for modeling pipelines<sup>24–28</sup> and signal processing<sup>29</sup> have far surpassed the availability of data. With rare exceptions<sup>30–32</sup> , available brain stimulation datasets are centered on validating current flow<sup>33,34</sup> , providing anatomical templates<sup>35,36</sup> , or are derived from animal models<sup>37</sup> . The lack of raw data sharing and availability in the neuromodulation field can lead to decreased transparency when it comes to examining tES-EEG relationships, verifying analyses or analysis-dependent<sup>38</sup> relationships in tES-EEG outcomes, as well as a decrease in the democratization of algorithmic development, especially when it comes to enhancing algorithms geared toward closed-loop tES. 

The effects of tES on attention and vigilance<sup>17,39–41</sup> have been extensively studied, and are of universal interest with regard to tES, since they impact applications such as accelerated learning<sup>42</sup> , neurorehabilitation<sup>6,43</sup> and neuro-psychiatric treatment<sup>44–46</sup> . An openly available dataset with continuous metrics of vigilance/attention, over an extended period of time, paired with concurrent EEG and physiologic metrics, during varied types of tES would present as a significant contribution to the field of neuromodulation. 

To test how vigilant/attentional states are acutely altered by specific tES types, over an extended period (~70 mins) of behavioral task performance, and how temporal sensitivity to stimulation is modulated by or 

1The Department of Biomedical Engineering, The City College of New York, The City University of New York, New York, USA.<sup>2</sup> Soterix Medical Inc., New York, USA.<sup>✉</sup> e-mail: ngebodh01@citymail.cuny.edu 

Scientific **Data** | _(2021) 8:274_ | https://doi.org/10.1038/s41597-021-01046-y 

1 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

reflected in brain/physiological state: our multimodal dataset combines human-participant, concurrent multichannel tES; multichannel EEG (sampled at 2 kHz), bipolar ECG and EOG monitoring; and continuous (in time and score) vigilance/alertness behavioral metrics. We apply 9 different electrical stimulation montages (3 stimulation locations and 3 frequencies), with each stimulation type applied 4-20 times per experimental session, in a repeated-measures crossover design – with additional repetitions for within-participant reliability. A verified<sup>47–53</sup> compensatory tracking task (CTT) allowed for the assessment of vigilance/attention on the scale of milliseconds, facilitating its acquisition concurrency with dynamic EEG, ECG, and EOG. These multimodal assessments allow for the testing of 1) how variations in brain state (e.g. baseline vigilance) or physiology impact sensitivity to tES; and 2) how tES changes brain state or physiology (e.g. autonomic function as indicated by heart rate variability) along with changes in performance. 

Our approach varies from typical tES interventions in applying stimulation since we utilize short stimulation (30 sec) epochs, in contrast to tens of minutes. Although it has been observed that tens of minutes of stimulation enhances the detection of stimulation related after-effects<sup>54–57</sup> such effects come on the heels of and are resultant from an accumulation of online (immediate) effects<sup>58–61</sup> , which are currently challenging to directly observe. Modulatory EEG effects are typically rapid, on the order of milliseconds<sup>10,18,20,23,62</sup> , as are cellular responses in animal models<sup>63–67</sup> . Similarly, ongoing changes in brain state, physiology, and performance (e.g. fatigue/vigilance shift) can be rapid<sup>68–72</sup> too. Closed-loop stimulation approaches require the use of transient biomarkers. Ultimately, our selection of short stimulation epochs was driven by: 1) the aforementioned mechanistic factors; 2) the value of increasing statistical power (repetitions) and signal to noise ratio (e.g. minimizing drift over time); as well as supporting algorithm development for 3) data cleaning (e.g. online EEG artifact correction<sup>21,22</sup> ) and 4) closed-loop (e.g. machine learning) optimization - noting any sufficiently large open-loop experiments can be analyzed as closed-loop<sup>73–75</sup> interventions. The complete dataset and assessments are provided without restriction under the Creative Commons with Attribution 4.0 license and is detailed in this manuscript. We hope the availability of this dataset will alleviate barriers in the field of tES and allow for the exploration and testing of multiple hypotheses associated with the design of optimized stimulation interventions. 

### **Methods** 

**Participants.** A total of twenty neurologically typical individuals (7 females, 13 males) between the ages of 19 − 43 (median age: 30; mean age: 29.10 ± 6.75) were recruited from the New York metropolitan area. Before enrolment, participants underwent a tES eligibility screening procedure where they were asked questions regarding their medical history, psychiatric history, and prior drug use (non/illicit) including history of seizures, depression, surgeries, pain, ear trauma, heart conditions, skin allergies, implantable medical devices (non/metallic), alcohol dependency, brain lesions, loss of consciousness, sleep disorders, and fainting at the sight of blood. Participants who met the eligibility criteria were then enrolled (see Fig. 1a,b). After passing the eligibility screening, informed consent was obtained for each participant. Experimental procedures were reviewed and approved by the Western Institutional Review Board and all procedures were conducted in accordance with the ethical guidelines set forth by the Declaration of Helsinki in 1964 and its later amendments. All participants were financially compensated for their participation. 

Prior to each experimental session participants were asked to maintain their normal sleep-wake cycle, refrain from consuming alcohol or overly caffeinated foods/ beverages at least 4 h before their session, and refrain from eating any heavy meals at least 3 h before their visit. In order to facilitate expeditious EEG set-up, participants were also asked to refrain from wearing any heavy make-up or facial moisturizer, and refrain from wearing any hair products or scalp treatments<sup>76</sup> . 

One participant was excluded from the experiments (participant 17) due to inability to follow instructions in performing the experiment’s behavioral task (see Table 1). Four participants (participant number: 12, 15, 21, 22) were invited back to repeat both their experimental sessions for Experiment 2 (see _Experimental Overview_ ). Upon returning to repeat Experiment 2, returning participants were assigned a new participant number based on the incremental sequence of participant number assignment (i.e. 1<sup>st</sup> participant enrolled assigned to participant number 01, 2<sup>nd</sup> participant enrolled assigned to participant number 02, etc.). Participant 12 returned once and was assigned an updated participant number: 19; participant 15 returned once and was assigned an updated participant number: 18; participant 21 returned twice and was assigned updated participant numbers: 25 and 26; and participant 22 returned twice and was assigned updated participant numbers: 23 and 24 (see Table 2). 

**Questionnaires.** Upon enrollment participants completed a demographic questionnaire to assess their age, gender, height, weight, years of education, handedness, English proficiency, typical exercise time each week, history of electrical stimulation, and sleep quality (quantified with the Pittsburgh Sleep Quality Index; PSQI<sup>77</sup> ). These questionnaires were only administered once upon participant’s enrollment on their initial session (hence empty cells in _GX_Subject Info & Behavioral Data.xlsx_ for participants who repeated Experiment 2; see _Demographics, PSQI, and Pre Post Questionnaires_ ). 

At the beginning of each session participants completed a prequestionnaire consisting of questions regarding their activities in the past 24 h (see _GX_Demo_PreQuest_Scales.pdf_ , page 2), in addition, they also completed assessment scales immediately before and after each session (Fig. 1c–h). These scales included assessments of sleepiness (Karolinska Sleepiness Scale; a 9-point scale ranging from 1-Extremely alert to 9-Very sleepy, great effort to keep awake, fighting sleep), discomfort scale (ranging from 1-No discomfort to 9-Extreme discomfort), pain (numeric pain scale; ranging from 0-No pain to 10-Worst possible pain), mood (ranging 1-Saddest to 9-Happiest), anxiety (ranging 1-Most relaxed to 9-Most tense), and energy level (ranging 1-Most tired to 9-Most energetic). Wellness scales were modeled after the standardized English version of the Karolinka Sleepiness Scale (KSS)<sup>78–80</sup> , which range from 1 to 9; and the pain scale utilized was modeled after standard Numeric Rating Scales (NRS) or Numeric Pain Scales (NPS) that conventionally range from 0 to 10<sup>81,82</sup> . 

Scientific **Data** | _(2021) 8:274_ | https://doi.org/10.1038/s41597-021-01046-y 

2 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



<!-- Start of picture text -->
a b c d<br>Group Mean Males Mean<br>Group Median Females Mean<br>40 100 10<br>8<br>35 90 8<br>30 80 6<br>70 6<br>25 4<br>60<br>20 4<br>15 N=12 N=7 N=19 50 2<br>Males Females All Subjects 160 170 180 190 4 6 8 10 2 4 6 8<br>Gender Height (cm) Sleep Hours KSS Pre<br>e f g h<br>8 7 3<br>8<br>7<br>5 6 2<br>6<br>3 4 1<br>5<br>2<br>4 1 0<br>4 5 6 7 8 9 2 4 6 3 4 5 6 7 8 0 0.5 1 1.5 2<br>Mood Pre Anxiety Pre Energy Pre Pain Pre<br>Age(years) Weight (kg) Sleep Quality KSS Post<br>Mood Post Anxiety Post Energy Post Pain Post<br><!-- End of picture text -->

**Fig. 1** Demographic and questionnaire summary. ( **a** ) Included participants’ ages ranged from 19-43 years old with a mean age of 28.79 years. ( **b** ) Included participants’ mean height and weight were 169.50 cm and 69.11 kg, respectively. ( **c** ) The mean sleep hours and sleep quality ratings were 6.45 hrs and 6.57 (5-Normal Quality), respectively. ( **d** ) The mean sleepiness ratings (KSS) before ( _KSS Pre_ ) and after ( _KSS Post_ ) each session was 4.01 and 5.70, respectively. ( **e** ) The mean mood ratings before ( _Mood Pre_ ) and after ( _Mood Post_ ) each session was 5.50 and 5.70 (5-Usual self), respectively. ( **f** ) The mean anxiety ratings before ( _Anxiety Pre_ ) and after ( _Anxiety Post_ ) each session were 3.77 and 3.45 (5-Usual self), respectively. ( **g** ) The mean energy ratings before ( _Energy Pre_ ) and after ( _Energy Post_ ) each session were 3.77 and 3.45 (5-Usual self), respectively. ( **h** ) The mean pain ratings before ( _Pain Pre_ ) and after ( _Pain Post_ ) each session was 0.18 and 0.39 (0-No pain, 10-Worst possible pain), respectively. For panels ( **c–h** ) data are illustrated for the aggregate of all sessions (including participants’ repeated sessions) and for ( **b–h** ) gray lines extending from each group mean indicate one standard deviation. 

**Behavioral task.** Participants were seated in a dimly lit (~10 lux) room and some were offered foam in-ear ear plugs to aid in sound attenuation. Participants were seated ~57 cm in front of a 17-inch LCD monitor (Model: E173FPb; Dell Corp., Texas, USA; set at a 60 Hz refresh rate) and were asked to continuously perform a Compensatory Tracking Task (CTT) over the course of each session. On-screen task instructions presented to participants stated: _Your goal in this task is to keep the ball near the target using your mouse or pointing device. The ball moves on its own, but is impacted by how you move the mouse. If possible, keep the ball in the center of the ring, or as close as possible to the inner circle as you can_ . The goal of the 2-dimensional task was to keep a moving circle constantly constrained near an annulus at the center of the screen (Fig. 2a). The circle was endowed with several kinematic properties including oscillatory and dampening forces<sup>47</sup> . The CTT was sourced and administered through the open source PEBL software version 2.1, an experimental psychology task program built upon C++<sup>83</sup> . Participants provided task input through their dominant hand via a trackball (Logitech TrackMan Marble Mouse; Model: 904360-0403; Logitech International S.A., Lausanne, Switzerland) and were left uninterrupted throughout the duration of the task (even in cases where participants were in visible hypnagogic states; consistent with prior CTT designs). Before the start of each session participants performed a short practice session that lasted between 1-3 mins. The duration of the task was set to 70 mins for both Experiment 1 and 2 (extended for an additional 0.5 mins). The CTT ran continuously and uninterrupted over the duration of both experiments and participants were blinded to each experiment’s block design and stimulation type. 

**EEG data acquisition.** EEG data were acquired using a wired Waveguard cap containing 32 Ag/AgCl recording channels (ANT Neuro, Hengelo, The Netherlands) and 29 interleaved plastic HD-holders (Soterix Medical Inc., New York, USA). The HD-holders were used to house the stimulation materials including conductive gel and stimulation electrodes (see _HD-tES_ ). For both stimulation and recording, conductive gel (SignaGel, Parker Laboratories Inc., New Jersey, USA) was placed between electrodes and the scalp using blunt tip (15-gauge; Cortech Solutions Inc., North Carolina, USA) syringes. 

EEG recording electrodes were located at standard locations following the 10/10 international placement system (Fig. 2b). Signals were sampled at 2 kHz, referenced relative to CPz, online grounded at AFz, and amplified with an eego sport amplifier (ANT Neuro, Hengelo, The Netherlands). The amplifier bandwidth was set between 0-520 Hz and the acquisition voltages range was set to 1 V peak-to-peak. Prior to each recording, scalp impedances were monitored to ensure impedance levels were below 20 kΩ. To time-lock the CTT with the concurrent 

Scientific **Data** | _(2021) 8:274_ | https://doi.org/10.1038/s41597-021-01046-y 

3 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

|||**File**||||||||||**Stim Typ**|**e**||**Stim Am**|**plitude (**|**mA)**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Sub#**|**Session**|**Num**|**F0**|**M0**|**P0**|**F5**|**M5**|**P5**|**F30**|**M30**|**P30**|**Block 1**|**Block 2**|**Block 3**|**Block 1**|**Block 2**|**Block 3**|
||01|0101|1||||||7|8||M30|F30|F0<sup>♦</sup>|1|1|1|
||02|0102|1||||||7|8||M30|F30|F0<sup>♦</sup>|0.5|0.5|0.5|
||03|0103|||3|||6|||9|P30|P0|P5|0.5|0.5|0.5|
|**01**|04|0104||2||4|5|||||F5|M5|M0|0.5|0.5|0.5|
||05|0105||2||4|5|||||F5|M5|M0|1|1|1|
||06|0106|||3|||6|||9|P30|P0|P5|1|1|1|
|**02**|01|0201||||4|||7||9|F30<sup>♦</sup>|F5|P30|0.5|0.5|0.5|
||02|0202|||3||5|||8||P0|M5|M30|0.5|0.5|0.5|
||01|0301||2|3||||7|||M0|P0|F30|0.5|0.5|0.5|
|**03**|02|0302||||4||6|||9|F5|P5|P30|0.5|0.5|0.5|
||03|0303|1||||5|||8||M5|F0|M30|0.5|0.5|0.5|
||01|0401||||4||||8|9|P30|M30|F5|0.5|0.5|0.5|
|**04**|02|0402|1|2|3|||||||P0|F0|M0|1|1|1|
||03|0403|||||5|6|7|||F30|M5|P5|1|1|1|
||01|0501|||3||5|6||||M5|P0|P5|0.5|1|1|
|**05**|04|0504||2||||||8|9|P30|M30|M0|1|1|1|
||05|0505|1|||4|||7|||F30|F0|F5|1|1|0.5|
||01|0601|1|||4||6||||F0|F5|P5|1|0.5|1|
|**06**|02|0602|||||||7|8|9|F30|M30|P30|0.5|1|1|
||03|0603||2|3||5|||||P0|M5|M0|1|1|1|
||01|0701||||4|5|6||||P5|F5|M5|0.5|0.5|0.5|
|**07**|02|0702|1|2|3|||||||M0|P0|F0|0.5|0.5|0.5|
||03|0703|||||||7|8|9|F30|P30|M30|0.5|0.5|0.5|
||01|0801||||4|5|||8||F5|M30|M5|1|1|1|
|**08**|02|0802|1||3||||||9|P30|F0|P0|1|1|1|
||03|0803||2||||6|7|||P5|F30|M0|1|1|1|
||01|0901|1|||4|||||9|P30|F5|F0|0.5|0.5|1|
|**09**|02|0902|||3||5||7|||M5|F30|P0|0.5|1|1|
||03|0903||2||||6||8||P5|M0|M30|1|1|1|
||01|1001||2|3||5|||||M0|P0|M5|1|1|1|
|**10**|02|1002|1||||||7||9|F0|P30|F30|1|1|1|
||03|1003||||4||6||8||F5|M30|P5|1|1|1|



**Table 1.** Summary of all participant sessions for Experiment 1 including stimulation condition and stimulation intensity. Columns indicate participant number ( _Sub #_ ), each participant’s session number ( _Session_ ), the corresponding file number for each session ( _File Num_ ), a detailed breakdown of stimulation conditions that were applied for each session across stimulation blocks ( _Stim Type_ ), and the corresponding stimulation amplitude ( _Stim Amplitude_ ) that was applied for each stimulation condition. Blocks with trials that encountered technical errors are indicated with black diamonds (♦) under the _Stim Type_ section. 

EEG a trigger was sent to the EEG amplifier at the start of the CTT (see _Data Records_ ). Following data acquisition, data were exported to a _.cnt_ file. 

**Physiological monitoring.** Cardiac activity was acquired with a lead I electrocardiogram (ECG) configuration and ocular motor activity with horizontal electrooculogram (EOG) configuration. Both were acquired with bipolar snap electrodes, concurrently with EEG and HD-tES. For lead I ECG, bipolar snap electrodes were placed on participants’ chest approximately 5 cm below the center of their left (anode) and right (cathode) clavicle bone. A ground electrode was placed on participants’ left hip, in close proximity to participants’ iliac crest. For horizontal EOG, electrodes were placed at the outer canthus of the participants’ left (anode) and right (cathode) eye. Prior to all peripheral electrode placement, the application sites on the skin were gently swabbed with alcohol pads (BD Alcohol Swabs, Becton Dickinson, New Jersey, USA) to increase electrode adhesion and contact quality. 

**HD-tES.** HD-tES was applied for 30-sec epochs per trial with an additional 5-sec ramp-up/down period, at 3 different cephalic locations with 3 different stimulation waveforms. The 9 stimulation doses (combination of stimulation location: 3; frequency: 3; duration: 1) were characterized by the cephalic area of stimulation: frontal, motor, and parietal; as well as the frequency of the stimulation current applied: 0 (DC), 5, and 30 Hz. Each combination of stimulation location and frequency was denoted with the first letter of the stimulation location in combination with the Arabic numeral denoting the frequency. As such, the nine possible dose combinations were as follows: frontal DC (F0), frontal 5 Hz (F5), frontal 30 Hz (F30), motor DC (M0), motor 5 Hz (M5), motor 30 Hz (M30), parietal DC (P0), parietal 5 Hz (P5), parietal 30 Hz (P30). 

Scientific **Data** | _(2021) 8:274_ | https://doi.org/10.1038/s41597-021-01046-y 

4 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

|**Sub#**|**Session**|**File Num**|**F30**|**M30**|**Stim Type**|**Stim Amplitude (mA)**|
|---|---|---|---|---|---|---|
|**11**|01|1101|7||F30|1|
||02|1102||8|M30|1|
|**12**<sup>■</sup>|01|1201||8|M30|1|
||02|1202|7||F30|1|
|**13**|01|1301|7||F30|1|
||02|1302||8|M30|1|
|**14**|01|1401||8|M30|1|
||02|1402|7||F30|1|
|**15**<sup>▲</sup>|01|1501|7||F30|1|
||02|1502||8|M30|1|
|**16**|01|1601||8|M30|1|
||02|1602|7||F30|1|
|**17**|01|1701|7||F30|1|
|**18**<sup>▲</sup>|01|1801||8|M30|1|
||02|1802|7||F30|1|
|**19**<sup>■</sup>|01|1901|7||F30|1|
||02|1902||8|M30|1|
|**20**|01|2001|7||F30|1|
||02|2002||8|M30|1|
|**21**<sup>**♦**</sup>|01|2101|7||F30|1|
||02|2102||8|M30|1|
|**22**<sup>**∙**</sup>|01|2201||8|M30|1|
||02|2202|7||F30|1|
|**23**<sup>**∙**</sup>|01|2301|7||F30|1|
||02|2302||8|M30|1|
|**24**<sup>**∙**</sup>|01|2401||8|M30|1|
||02|2402|7||F30|1|
|<sup>**♦**</sup>|01|2501||8|M30|1|
|**25**|02|2502|7||F30|1|
|<sup>**♦**</sup>|01|2601|7||F30|1|
|**26**|02|2602||8|M30|1|



**Table 2.** Summary of all participant sessions for Experiment 2 including stimulation condition and stimulation intensity. Columns indicate participant number ( _Sub #_ ), each participant’s session number ( _Session_ ), the corresponding file number for each session ( _File Num_ ), a detailed breakdown of stimulation conditions that were applied for each session across stimulation trials ( _Stim Type_ ), and the corresponding stimulation amplitude ( _Stim Amplitude_ ) that was applied for each stimulation condition. Matching symbols next to participants’ numbers indicate the same individual who returned for additional sessions and was assigned a new subject number. Participant 12 retuned once and was assigned a new number: 19 (■). Participant 15 returned and was assigned a new number: 18 (▲). Participant 21 returned twice and was assigned new numbers: 25 and 26 ( **♦** ). Participant 22 returned twice and was assigned new numbers: 23 and 24 ( **∙** ). 

A total of 9 Ag/AgCl sintered ring stimulation electrodes (Soterix Medical Inc., New York, USA) were placed at standard EEG 10/10 locations in manner forming three possible Nx1 HD-tES<sup>84</sup> ; where N = 3, 4, 4 for frontal, motor, and parietal, respectively. For each montage, N electrodes were selected for the outer (surround) ring electrode, and one electrode was selected as the center electrode. Note, some electrode locations were shared across montages with varied “ring” or “center” assignments. In this way, a single 9 electrode position HD-tES set-up = was prepared for all experiments. For frontal stimulation, outer or surround electrodes (N 3) were placed at AF3, FT7, FC3 and the return or center electrode was placed at F5 (Fig. 2b,c). For motor stimulation outer or surround electrodes (N = 4) were placed at FT7, FC3, CP3, TP7, and the return or center electrode was placed at C5 (Fig. 2b,c). For parietal stimulation outer or surround electrodes (N = 4) were placed at C5, C1, P1, TP7 and the return or center electrode was placed at CP3 (Fig. 2b,c). To visualize stimulation electrode placement in realistic 3D space, an MRI-derived head model was used together with the ROAST toolbox<sup>27,85</sup> in MATLAB (2018b and 2019b; MathWorks, Massachusetts, USA). Each montage shared stimulation sites and no two stimulation montages were applied at the same time. 

In terms of stimulation waveforms, a monophasic DC (0 Hz) or biphasic sinusoidal waveform (5 or 30 Hz) was applied. For DC, for each cephalic location (frontal, motor, parietal) the respective center electrode was used as the cathode with the surround electrodes as anodes. For biphasic sinusoidal stimulation all electrodes switched between being an anode and cathode at a rate set by the frequency of stimulation (i.e. 5 Hz or 30 Hz). 

Using conventional procedures<sup>86</sup> , stimulation electrodes were placed in plastic HD-holders (Soterix Medical Inc., New York, USA), which were embedded in the EEG cap (interleaved with EEG electrode positions). To 

Scientific **Data** | _(2021) 8:274_ | https://doi.org/10.1038/s41597-021-01046-y 

5 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



<!-- Start of picture text -->
a b Fpz c<br>C1<br>Fp1 Fp2 AF3 FC3<br>10<br>AF3<br>F5 CP3 P1<br>F7 F5 F8<br>Fz<br>F3 F4 C5<br>FT7 FC5 FC3 FC6<br>20 FC1 FC2<br>40 C5 C3 C1 C4 FT7<br>60 T7 T8<br>Cz<br>CP5 CP6 TP7<br>TP7 CP3 CP1 CP2<br>M1 P3 P1 Pz P4 M2<br>P7 P8<br>POz<br>Frontal Motor Parietal<br>O1 Oz O2 EEG electrode Center electrode Surround electrode<br>d e<br>Task & Stimulation Control Computer<br>Stim Stim Stim Stim Stim Stim Stim<br>Off Enabled Off Enabled Off Enabled Off<br>PEBL MATLAB NI Time<br>f<br>Stim Start Stim Stop<br>Data Acquisition Computer Block Start Code:16 Code:32 30 sec ON<br>Code:02<br>Trigger  EEG & Physio,  OFF<br>Box Trigger Data Stim Off Block Stim Enabled Block<br>10 mins 10 mins<br>EEG &<br> Physio g<br>Amplifier Stim Stim Stim Stim Stim Stim<br>Off Enabled Enabled Enabled Enabled Enabled<br>Time<br>Stimulation<br>h<br>Stim Start Stim Stop<br>MXN Task Display Block Start Code:16 Code:32 30 sec ON<br>Code:02<br>OFF<br>Behavior Stim Off Block Stim Enabled Block<br>Trackball 20 mins 10 mins<br><!-- End of picture text -->

**Fig. 2** Behavioral task, EEG and stimulation montage, hardware setup, and experimental overview. ( **a** ) The CTT behavioral task where the objective was to maintain the moving circle (~10 pixels) near the center of the middle annulus (~20 pixels) over the course of the experiment (70 mins). The ball was endowed with inherent motion, and oscillatory and dampening forces. Note, only the white ball and gray annulus were visible to participants, in the panel additional rings and distances are for illustrative purposes. ( **b** ) EEG locations (light blue) interleaved with stimulation sites for frontal (orange), motor (purple), and parietal (magenta) stimulation. For each stimulation montage, center electrodes are indicted by a star and surrounding electrodes by circles. Note, by design some electrode locations may serve as a center electrode for one montage and outer electrodes for another montage. ( **c** ) MRI-derived 3D head model with the stimulation locations placed on the scalp to visualize electrode placement. ( **d** ) Data acquisition and stimulation hardware setup in relation to participants’ input and output. ( **e** ) Experiment 1 and ( **g** ) Experiment 2 block design as programed to be executed within the hardware and software setup in panel ( **d** ). Experiments were divided into _stimulation off_ blocks ( _Stim Off_ ) without tES and _stimulation enabled_ blocks ( _Stim Enabled_ ) within which the selected tES stimulation condition was applied 4 times. ( **f** ) Experiment 1 and ( **h** ) Experiment 2 detailed block design with corresponding EEG triggers (dashed vertical line) and trigger codes. Note that the block design is not drawn to scale. Simultaneous _EEG and Physio_ (EEG, ECG, and EOG; teal); and _Behavior_ (CTT, red) were acquired with concurrent _Stimulation_ (gold). Note, _EEG and Physio_ acquisition started several seconds before any trigger delivery; and ( **e,f** ) are designed to illustrate the experimental design as programmed to be executed. 

prepare for electrode placement, participants’ hair was parted with a blunt Q-tip or blunt tip syringe at each stimulation location through the annulus of the plastic HD-holders, then the HD-holders were slowly backfilled with ~15 mL of HD gel (Soterix Medical Inc., New York, USA). The stimulation electrodes were then placed in the HD-holders and were fully submerged in electrolyte gel, then the plastic holder was covered with the associated plastic covering to secure the electrode in place. 

Stimulation was delivered using the MxN 9-channel high-definition transcranial electrical stimulation stimulator (Soterix Medical Inc., New York, USA). The multichannel stimulation device supplied a current controlled current source where the current amplitude of each individual stimulation channel could be adjusted. Stimulation channel impedances were measured relative to F5, prior to the commencement of stimulation. During each session, the stimulator was triggered using a pulse generated in MATLAB and relayed to a National Instruments (NI) -DAQmx device (National Instruments Inc., Texas, USA). A corresponding trigger was sent to the EEG amplifier to time-lock stimulation and EEG (Fig. 2d). For details on stimulation settings for each stimulation dose see Table 3. 

6 

Scientific **Data** | _(2021) 8:274_ | https://doi.org/10.1038/s41597-021-01046-y 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

|||**Frontal**||**Motor**||**Parietal**||
|---|---|---|---|---|---|---|---|
|**Waveform**||Sinusoid*||Sinusoid*||Sinusoid*||
|**Polarity**||Biphasic||Biphasic||Biphasic||
|**Frequency (Hz)**||0 | 5 | 30||0 | 5 | 30||0 | 5 | 30||
|**Ramp Duration (secs)**||5||5||5||
|**Center Electrode**||F5||C5||CP3||
||**_Channel_**|**_Intensity_**<br>**_(1 mA)_**|**_Intensity_**<br>**_(0.5 mA)_**|**_Intensity_**<br>**_(1 mA)_**|**_Intensity_**<br>**_(0.5 mA)_**|**_Intensity_**<br>**_(1 mA)_**|**_Intensity_**<br>**_(0.5 mA)_**|
||**1 (AF3)**|−0.33|−0.17|0|0|0|0|
||**2 (FT7)**|−0.33|−0.17|−0.25|−0.13|0|0|
||**3 (FC3)**|−0.33|−0.17|−0.25|−0.13|0|0|
||**4 (C5)**|0|0|+1.00|+0.52|−0.25|−0.13|
|**Channel Settings For Total**<br>**Current at 1 and 0.5 mA**|**5 (TP7)**|0|0|−0.25|−0.13|−0.25|−0.13|
||**6 (C1)**|0|0|0|0|−0.25|−0.13|
||**7 (CP3)**|0|0|−0.25|−0.13|+1.00|+0.52|
||**8 (P1)**|0|0|0|0|−0.25|−0.13|
||**9 (F5)**<sup>**$**</sup>|+0.99|+0.51|0|0|0|0|
||**Net Amplitude**<br>**Delivered (mA)**|**0.99**|**0.51**|**1**|**0.52**|**1**|**0.52**|



**Table 3.** Stimulation device (MxN) settings used for each stimulation dose. Each row indicates an aspect of programing the MxN stimulator. For setting stimulation frequency, either 0, 5 or 30 was selected based on the intended frequency of stimulation. The ramp duration setting was identical for stimulation ramp-up as well as stimulation ramp-down. *The MxN accepts 0 Hz as a monophasic DC.<sup>$</sup> Channel 9 was automatically set to the residual sum of the programable channels (channels 1-8). 

Prior to the start of each session participants underwent a pre stimulation test to determine their tolerance and comfort with each stimulation montage. Stimulation was delivered for approximately 20 secs (5-sec ramp-up/ down) at an initial net current of 1 mA (peak-to-peak) and 0.5 mA (peak-to-peak) for Experiment 1 and 2, respectively. Participants were then asked to rate the level of pain/discomfort on a numeric pain scale (0-No pain/ discomfort to 10-Worst pain you’ve ever felt). For Experiment 1, if participants rated a 5 or above, the stimulation intensity was halved (0.5 mA minimum amplitude); whereas for Experiment 2 if participants rated below 5, the stimulation intensity was increased to 1 mA. In both experiments the adjusted stimulation intensity was 0.5 mA at minimum and was retested to ensure that it was well tolerated. All participants in Experiment 2 received 1 mA of stimulation (see Table 2) whereas stimulation intensities for Experiment 1 were either 0.5 or 1 mA, based on pre stimulation testing (see Table 1). 

**Experimental overview.** In Experiment 1, each participant engaged in three 70-min sessions whereas in Experiment 2 participants engaged in two 70.5-min sessions. Prior to and after each session (for both Experiment 1 and 2), participants completed a series of pre- and post-questionnaires (see _GX_Demo_PreQuest_Scales.pdf_ ). For each session participants performed the CTT continuously over the course of 70 mins (or 70.5 mins) while EEG and physiology (ECG, EOG) were recorded. For Experiment 1, nine different stimulation conditions were used (F0, F5, F30, M0, M5, M30, P0, P5, P30), whereas for Experiment 2, two different stimulation conditions were used (F30, M30). 

For Experiment 1, each session (of the 3 sessions per participant) consisted of three stimulation enabled blocks (10 mins each) interleaved with four stimulation off blocks (10 mins each). For each session, three of the nine total stimulation conditions were pseudo-randomly assigned to stimulation enabled blocks - to ensure participants received each of the nine stimulation conditions across the nine total stimulation enabled blocks in Experiment 1. During each stimulation enabled block the assigned stimulation condition was administered as 4 consecutive stimulation trials (see Fig. 2e,f). Each stimulation trial consisted of a 5-sec ramp-up period, 30-sec stimulation period, and a 5-sec ramp down period. 

For Experiment 2, each of the two sessions (one session for F30 and one session for M30) consisted of one stimulation off blocks (20 mins), which was followed by five consecutive stimulation enabled blocks (10 mins each; Fig. 2g,h). For each session, only one of the two stimulation conditions (F30 or M30) were pseudo-randomly assigned to be administered during the five stimulation enabled blocks. The assigned stimulation condition was administered as 4 consecutive trials during each stimulation enabled blocks. Thus, a total of 20 trials of stimulation (30 secs each plus 5-sec ramp up and down) were delivered for each session in Experiment 2. 

A precise experimental sequence with EEG (channel Cz), behavioral timeseries, and associated triggers are illustrated for Experiment 1 and Experiment 2 (Fig. 3) for exemplary participants 10 and 24, respectively. This demonstrates participant-wise implementation of the block design in Fig. 2e–h from the data collection perspective. In all experiments, participants continuously performed a task, with associated performance, EEG, and physiology recorded. 

At their first session of Experiment 1 (Fig. 3b), participant 10 was pseudo-randomly assigned to receive stimulation conditions M0, P0, and M5 (indicated by insets). Each stimulation condition was repeated over 4 

Scientific **Data** | _(2021) 8:274_ | https://doi.org/10.1038/s41597-021-01046-y 

7 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



<!-- Start of picture text -->
a Stim Trial #: 1 2 3 4 Max Stim Current 1 2 3 4 Max Stim Current 1 2 3 4 Max Stim Current<br>Stim Off Stim Enabled Stim Off Stim Enabled Stim Off Stim Enabled Stim Off Time<br>b 500 EEG -Cz<br>CTT<br>Block Start Code: 02<br>Stim Start Code: 16<br>Stim Stop Code: 32<br>400<br>0 0<br>02 02 02 02 02 02 02 02<br>M0 P0 M5<br>-500<br>c 6,000<br>400<br>0 0<br>02 02 02 02 02 02 02 02<br>F0 P30 F30<br>-6,000<br>d 8,000<br>1 00<br>0 0<br>02 02 02 02 02 02 02 02<br>F5 M30 P5 FrontalMotor<br>Parietal<br>-8,000<br>0 10 20 30 40 50 60 70<br>Time (mins)<br>e Max Stim<br>Stim Trial #: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 Current<br>Stim Off Stim Enabled Stim Enabled Stim Enabled Stim Enabled Stim Enabled Time<br>f 600 EEG -Cz<br>CTT<br>Block Start Code: 02<br>Stim Start Code: 16<br>Stim Stop Code: 32 400<br>0 0<br>02 02 02<br>M30<br>-600<br>g 1,500<br>200<br>0 0<br>02 02 02<br>Frontal F30<br>Motor<br>-1,500<br>16 16 16 16 16 16 16 16 16 16 16 16<br>Voltage (μV)<br>32 32 32 32 32 32 32 32 32 32 32 32 32<br>16 16 16 16 16 16 16 16 16 16 16 16<br>Deviation<br>32 32 32 32 32 32 32 32 32 32 32 32 32<br>16 16 16 16 16 16 16 16 16 16 16 16<br>32 32 32 32 32 32 32 32 32 32 32 32 32<br>16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16<br>Voltage (μV)<br>32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 Deviation<br>16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16<br>32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32<br><!-- End of picture text -->

**Fig. 3** Block implementation with timeseries of a complete experimental series for exemplary participants. ( **a** ) Session design for Experiment 1. Each session consisted of four 10-min _Stim Off_ periods interleaved with three 10-min _Stim Enabled_ periods A given stimulation condition was assigned to each _Stim Enabled_ period, and applied in 4 consecutive 30 sec trials (Stim Trial # 1, 2, 3, 4). Experimental implementation, including EEG (Cz electrode) and CTT timeseries, for participant 10’s ( **b** ) first, ( **c** ) second, and ( **d** ) third sessions of Experiment 1. ( **e** ) Session design for Experiment 2. EEG and CTT timeseries for participant 24’s ( **f** ) first and ( **g** ) second session implementation. One stimulation condition (either M30 or F30; cartoon insets) was repeatedly applied during each session. In each session of Experiment 2, an initial 20-min _Stim Off_ period, was followed by 50-min _Stim Enabled_ period which included 20 trials of stimulation. Timeseries triggers in EEG data (vertical dashed lines) are marked with trigger codes. Across all sessions, for both experiments, EEG (teal) and CTT performance (pink), as well as physiology (not illustrated), were acquired continuously. 

8 

Scientific **Data** | _(2021) 8:274_ | https://doi.org/10.1038/s41597-021-01046-y 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

consecutive trials in a block ( _Stim Enabled)_ ; for each trial current was ramped up (over 5 secs), sustained for 30 secs at a maximum designated current intensity (0.5 or 1 mA; _Max Stim Current_ ), then ramped back down. Session 2 of Experiment 1, for participant 10, continued similarly with F0, P30, and F30 stimulation applied during the stimulation enabled blocks (Fig. 3c). Session 3 of Experiment 1, for participant 10, also continued similarly with F5, M30, and P5 stimulation applied during the stimulation enabled blocks (Fig. 3d). 

In session 1 of Experiment 2 (Fig. 3f), participant 24 received the M30 stimulation condition (indicated by insets). The M30 stimulation condition was repeated over 20 consecutive trials divided across five consecutive stimulation enabled blocks ( _Stim Enabled)_ ; for each trial current was ramped up (over 5 secs), sustained for 30 secs at a maximum designated current intensity (0.5 or 1 mA; _Max Stim Current_ ), then ramped back down. Session 2 of Experiment 2, for participant 24, continued similarly with the F30 stimulation condition applied during the stimulation enabled blocks (Fig. 3g). 

The band-pass filtering applied in Fig. 3 for display purposes, produces large voltage artifacts in the EEG during ramp-up and ramp-down, as well as removing DC voltage artifacts, which is present in unfiltered EEG-stimulation data<sup>21</sup> . 

### **Data Records** 

All raw data described in the text<sup>87</sup> can be accessed directly at: https://doi.org/10.5281/zenodo.3837212. The main data repository contains raw data for Experiment 1 and 2, in _.cnt_ format (see _EEG and Behavioral Data_ )<sup>87</sup> ; in addition, down sampled data for Experiment 1 and 2 are indexed in linked repositories<sup>88,89</sup> in _.mat_ format, which is compatible with MATLAB and Python. The dataset is also provided according to the Brain Imaging Data Structure (BIDS)<sup>90</sup> specifications and can be accessed directly at: https://doi.org/10.18112/openneuro.ds003670. v1.1.0. Trial-wise plots of data are fully indexed for EEG PSDs<sup>91</sup> : https://doi.org/10.6084/m9.figshare.14810517.v1, spectrograms<sup>92</sup> : https://doi.org/10.6084/m9.figshare.14810442.v1, and topoplots<sup>93</sup> : https://doi.org/10.6084/ . m9.figshare.14810478 

All experimental sessions and applied stimulation conditions are summarized in Table 1 and Table 2 for Experiment 1 and Experiment 2, respectively (see also the _Sessions Summay.xlsx_ file in the main data repository). The _Sessions Summay.xlsx_ file contains the participant numbers ( _Sub#_ ), participant session label, participants’ session number, stimulation conditions used for each session ( _Arms_ ), date of the session (in month/date/year), and associated file number for each session ( _File Num_ ). The _Sessions Summay.xlsx_ file also breaks down which condition out of 9 (F0, M0, P0, F5, M5, P5, F30, M30, P30) were applied for each session, which block the stimulation type was applied in ( _Stim Block 1, Stim Block 2, Stim Block 3_ ), as well as the stimulation amplitude (in mA) used for each session and each block ( _Stim Amp Block1, Stim Amp Block 2, Stim Amp Block 3_ ). For Experiment 2 the montage and stimulation intensity were used across all respective stimulation blocks (Listed under _Stim Block 1_ and _Stim Amp Block1_ ). 

**Demographics, PSQI, and Pre Post questionnaires.** The _GX_Subject Info & Behavioral Data. xlsx_ file contains paginated and tabulated participant-reported information on demographics ( _Demographic_ ), PSQI responses ( _PSQI_ ), and pre- and post-session questionnaires ( _All Behavioral_ ). Data were digitized and hand-imputed from paper records and repeated participants were indicated by notes made on each participant number and color-coding indicated repeated participants with their updated participant numbers. 

Within the _Demographic_ page of the _GX_Subject Info & Behavioral Data.xlsx_ file the columns indicated each participants’ (rows) participant number ( _Sub#_ ), date of data collection (month/date/year), age (in years), gender (Male or Female), height (in cm), weight (in kg), ethnicity, race, years of education, handedness (left or right handed), whether English was their first language, their proficiency in English, whether they exercise or not, how many hours they exercise, if they’ve ever had electrical stimulation before, and how recently have they had electrical stimulation. 

Within the _PSQI_ page of the _GX_Subject Info & Behavioral Data.xlsx_ file the data were arranged by participant (rows) and PSQI questions (columns). Each column other than participant number ( _Subj#_ ) and date, are labeled according to their correspondence to each PSQI question. For example, _PSQI-5-a_ corresponds to PSQI question number 5, part a, asking: _During the past month, how often have you had trouble sleeping because you cannot get to sleep within 30 minutes?_ Notes were made when participants indicated responses that were outside the scope of the questionnaire or if decisions were made to average or quantize participants’ responses, when appropriate. The full list of PSQI questions as well as scoring the PSQI can be found here<sup>94</sup> . 

Within the _All Behavioral_ page of the _GX_Subject Info & Behavioral Data.xlsx_ file data were arranged according to participant number ( _Sub#_ ), session label, session number, file number ( _File Num_ ), a count of all records, date of data collection, presumed start and end times of each session, stimulation amplitude used for each session and each montage (one number indicates that a single stimulation amplitude was applied for all stimulation montages within a session), session type/montage order ( _Arms_ ), responses to all questions in the Pre-Questionnaire (PQ, numbered by question), pre and post responses to adverse events form (ADpre- for pre stimulation and ADpost- for post stimulation), and all of the pre post rating scales (all called _Karl_ to indicate a Karolinska-like scale was administered) including sleepiness ( _Karol-Sleep-Pre_ or _Post_ ), discomfort ( _Karol-Disc-Pre_ or _Post_ ), pain ( _Karol-Pain-Pre_ or _Post_ ), mood ( _Karol-Mood-Pre_ or _Post_ ), anxiety ( _Karol-Anx-Pre_ or _Post_ ), and energy ( _Karol-Energy-Pre_ or _Post_ ). A full list of the questions asked before and after each experimental session can be found in _GX_Demo_PreQuest_Scales.pdf_ . 

**EEG and Behavioral data.** All data records are arranged by experiment (Experiment 1 and Experiment 2). The raw data are sorted by each experimental session. The experimental sessions are named according to the 

Scientific **Data** | _(2021) 8:274_ | https://doi.org/10.1038/s41597-021-01046-y 

9 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

participants’ assigned number and that participant’s experimental session number. For example, for participant 6, session 2 the corresponding folder will be 0602. 

Within each session folder is the raw EEG, ECG, and EOG data. These data were exported to _.cnt_ format and accompanying _.evt_ file, without any applied filters or data augmentation. Each _.cnt_ file is labeled with a project pseudonym ( _GX_ ) followed by the participant number, year of data acquisition, month of acquisition, date of acquisition and end time of acquisition in 24-hour clock notation. For example, _GX_07_2019-11-15_20-06-07. cnt_ indicates that this data file was collected from participant 7, on November (11) 15<sup>th</sup> , 2019 and the recording _mat txt_ ended at 20:06:07 hrs (08:06:07 PM). The session folder also contains a. file and a. file. These files contain session timers as well as the montage/s entered for each session. Within the MATLABfilestream < participant number > .mat files relevant variables include _Montages_ , and _stim_ . For Experiment 1 the _Montages_ variable contains the three stimulation conditions that were applied for the defined session. For example, for participant 8 the _Montages_ file for session 2 (0802) indicates ‘P30’,’F0’,’P0’. This indicates that the P30 stimulation was applied in stimulation block 1, whereas F0 was applied during stimulation block 2, and P0 was applied during stimulation block 3 (see Fig. 3a _Stim Enabled_ time periods). For Experiment 2 the _Montages_ variable contains the single stimulation condition that was applied for the whole session, the stimulation condition was repeated three times within the variable for code execution dependencies. For example, for participant 19 the _Montages_ file for session 2 (1902) indicates ‘M30’, ‘M30’,’M30’. This indicates that the M30 stimulation condition was applied for all stimulation trials (20 trials total) during session 2 (see Fig. 3e _Stim Enabled_ time periods). The _stim_ variable within the MATLABfilestream < participant number > .mat files on the other hand kept track of parameters that were passed to PEBL and variables defined within MATLAB for file execution. The _amp_ variable defined the stimulation amplitude that was intended to be applied during each session (see Table 1, 2 for stimulation amplitudes applied). The _blocklenmins_ and the _blocklen_ variables defined the length of each block as outlined in Fig. 2e,g in units of mins and secs, respectively. The variables _timeon_ , _rampup_ , _rampdown_ , and _repeat_ defined the length of time stimulation was applied for, the ramp up and ramp down times, and the amount of times stimulation was repeated within a block (Fig. 2f,h), respectively. Other variables within the _stim variable_ and within the MATLABfilestream < participant number > .mat files contained parameters that tracked parallel experimental timelines. The text files, MATLABfilestream < participant number > .txt were used as additional time parameter trackers and were not pertinent to any study outcome. Within each session folder is also a folder with identical session naming. This subfolder contains the exported CTT data as well as a CTT summary in _.csv_ and _.txt_ formats, respectively. The. _cnt_ and. _evt_ can be used in both MATLAB and python using free and open access accompanying libraries<sup>95</sup> . 

The CTT data are located within each session’s folder in a subfolder with an identical name. For example, for participant 19 session 2, their CTT data can be found by navigating through _1902 > 1902 > ptracker-1902. csv_ . The ptracker- < participant number + session number > .csv file contains metrics collected from the trackball. Some of these useful metrics include the participant number ( _subnum_ ), the time stamp (time), the cursor’s x-position ( _posX_ ), the cursor’s y-position ( _posY_ ), the change in time steps in ms ( _timeDelta_ ), and the cursor’s radial deviation from the center of the screen ( _deviation_ ). For additional details on CTT output see PEBL’s ptracker documentation. 

The physiological (EEG, ECG, EOG) and the behavioral (CTT) data can be time aligned by using triggers sent to the EEG amplifier. The start of the CTT is indicated by the first _Block Start_ trigger (code:02), which can be found in the EEG data once it has been imported for post processing. The start of each stimulation trial is indicated with a stimulation start trigger (code:16). After the stimulation start trigger was delivered, to the stimulator and EEG amplifier, the stimulation current was ramped up over the course of 5 secs until it reached the desired intensity. After 30 secs of stimulation at the desired intensity a stimulation stop trigger (code:32) was delivered to the stimulator and EEG amplifier, and the stimulation intensity was ramped down over the course of 5 secs. This process repeated 4 times for each stimulation enabled block. 

### **technical Validation** 

Our technical validation consisted of consulting computational current flow modeling, quality control of behavioral metrics, and quality control of EEG and ECG voltage changes. 

A high-resolution finite element model (FEM) was generated based on an MR image (1 mm<sup>3</sup> voxel size) in order to predict current flow pattern in three different montages used in the study (i.e. frontal, motor, parietal). The head model consisted of seven different tissues layers with conductivities assigned to each: skin (0.465 S/m), skull (0.01 S/m), fat (0.025 S/m), CSF (1.65 S/m), air (10<sup>−15</sup> S/m), gray matter (0.276 S/m) and white matter (0.126 S/m). The resulting masks were then meshed using ScanFE (Simpleware, LTD, Exeter, UK) and solved in a FEM solver (COMSOL, Burlington, MA, USA). The total stimulating current in each montage (i.e. frontal, motor, parietal) was applied at the center electrode and the four (three for frontal) surrounding electrodes were assigned as ground. The FEM model predicted the expected magnitude of current (electric fields) reaching underlying brain tissue and that electrode montages encapsulated the 3 brain regions of interest (frontal, motor, parietal; Fig. 4a–f). Mean EEG recordings of scalp voltages during stimulation, were in accord with the magnitude and spatial distribution of FEM model predictions of scalp voltage for each montage (Fig. 4d–f). To examine the designated frequency of stimulation applied during each stimulation trial, the Welch power spectral density (PSD; Fig. 4g); during stimulation topoplots; and time-frequency spectrograms (Fig. 4k–p) for EEG data were computed for pre, during, and post stimulation, accordingly, for all participants. Together these metrics aided in corroborating the applied stimulation frequency (with the PSD and spectrograms) as well as the stimulation’s spatial location (with the topoplots). The stimulation voltage artifacts in the trial-wise timeseries data (Fig. 4k,n) also aided in stimulation montage and frequency corroboration. These participant and trial-wise data are fully indexed for EEG PSDs<sup>91</sup> : https://doi.org/10.6084/m9.figshare.14810517.v1, spectrograms<sup>92</sup> : https:// doi.org/10.6084/m9.figshare.14810442.v1, and topoplots<sup>93</sup> : https://doi.org/10.6084/m9.figshare.14810478. 

Scientific **Data** | _(2021) 8:274_ | https://doi.org/10.1038/s41597-021-01046-y 

10 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



<!-- Start of picture text -->
a d g 150 F0 Pre Stim. F5 F30 M0 M5 M30 P0 P5 P30<br>Frontal 100 During Stim.Post Stim.<br>25 50<br>0 mV 0<br>0.29 -25 -50100 10¹ 10² 100 10¹ 10² 100 10¹ 10² 100 10¹ 10² 100 10¹ 10² 100 10¹ 10² 100 10¹ 10² 100 10¹ 10² 100 10¹ 10²<br>Frequency(Hz)<br>V/m h F0 F5 F30 M0 M5 M30 P0 P5 P30 j F30 M30<br>0  1 45.9 9.8 28.8 3.1 -2.9 21.4 5 4.4 29.2 60 11 ±50 20±<br> 2 NaN 5.9 4.8 NaN -70.3 -64 -23.7 NaN 16<br>b e  3 -5.8 5.7 4.4 6.8 -5.4 7.9 12.7 3.8 -17 12 20 20<br>Motor  4 34 -24.7 -21 -0.3 -7.7 -5.5 2.8 -13.8 -0.8 13 10 50<br>15  5 -2.8 -10.3 4.8 -1.3 2.9 -1.8 -0.2 -2.4 -4.7 0 14 50 20<br> 6 4.2 -3.9 -0.6 3.2 -1 11.9 -0.4 -12 -2.3<br>0.22 0 mV  7 2.8 -2.8 3.8 -1.8 -0.8 -16.5 -0.9 6.4 9.2 15 40 50<br>V/m -15  8 -19 16.1 -4.1 -31.3 38.2 25.7 -23.7 -9.1 -20.7 16 20 40<br> 9 6.7 8.1 16 -8.5 -5 21 -32.4 1.7 -6.8<br>0 10 6.2 3.8 10 3.6 9.2 2.5 -3.9 -2 -6 -60 18 50 50<br>i F30 M30 19 40 20<br>c f 1112 17.491.48 -3.5112.9 50 20 20 20<br>Parietal 1314 -6.650.15 -3.968.52 21 50 50<br>15 -2.2 -15.12<br>16 -1.09 -5.68 22 50 20<br>15 18 -9.46 1.95<br>0.23 0 mV 1920 27.756.37 27.33.26 0 23 50 50<br>V/m -15 2122 34.0745.13 34.573.57 24 20 50<br>0 23 22.42 29.43 25 50 50<br>24 14.76 34.81<br>2526 50.8642.83 37.4451.04 -50 26 %50 %50<br>5 10 15 20 5 10 15 20<br>Stimulation Conditions Trials<br>k EEG-C3ECG 50± n 50± q 60 22 90 23 30 24<br>CTT Mean<br>F30 M30 150 50 70 26<br>50 40 22<br>50<br>-100 -50 0 50 100 150 0 -100 -50 0 50 100 150 0 30 18<br>l 40 2EEG-C30 0 -20 -40 -60 PSD(dB/Hz) o EEG-C3 Time (sec) 1020 F30 3010 1014<br>Pre During Post Pre During Post Pre During Post<br>20 Currentrampup Stim.on Currentrampdown Stim.on r 35 22 40 23 90 24 20<br>35<br>30 70<br>0 -100 -50 0 50 100 150 -100 -50 0 50 100 150 30<br>m During Stim.Post Stim.Pre Stim. p Time (sec) 2520 2520 5030 10<br>15<br>15<br>10 M30 10 10 1<br>Pre During Post Pre During Post Pre During Post<br>0 10 20 30 40 50 60 70 80 90 0 10 20 30 40 50 60 70 80 90 Time Period<br>Deviation<br>Model<br>PSD (dB/Hz)<br>EEG<br>Model Participants<br>Deviation Change(%)<br>EEG<br>Participants<br>Model<br>Participants<br>Deviation Change(%)<br>EEG<br>6,000± 15,000±<br>0 0<br>Voltage (μV)<br>Deviation Deviation<br>Trial Number<br>Frequency (Hz)<br><!-- End of picture text -->

**Fig. 4** Technical validations. ( **a–c** ) A high-resolution MRI-derived finite element method (FEM) model computed for frontal, motor, and parietal stimulation montages. These quasi-static models are generalizable to 0, 5, and 30 Hz. ( **d–f** ) FEM model-predicted voltage topography ( _Model_ ) during stimulation compared with single-participant (participant 10) peak scalp voltage ( _EEG_ ) for frontal, motor, and parietal stimulation. ( **g** ) Baseline corrected EEG Welch power spectral density (PSD) computed over 30-sec periods pre, during, and post stimulation for participant 10 over all 9 stimulation conditions. ( **h** ) Percent change in deviation for behavioral (CTT) results for Experiment 1 averaged across 4 trials of each indicated stimulation condition. Data are summarized across participants and stimulation montages. Blacked out boxes indicate missing data. ( **i** ) Percent change in deviation for behavioral (CTT) results for Experiment 2 averaged across 20 trials of each indicated stimulation montage. Data are summarized across participants and stimulation montages. ( **j** ) Percent change in deviation for Experiment 2 across participants on a trial level for each of the 20 stimulation trials. Colorbars indicate the minimum (red), maximum (blue), and no change (white) in mean CTT deviation during 30 sec of stimulation compared to 30 secs before stimulation. For panels ( **i** ) and ( **j** ) repeated participants are indicated with individual colors and linked gray bars. Exemplary timeseries trials (trial 1) for an ( **k** ) F30 and ( **n** ) M30 session. Timeseries indicates combined EEG (channel C3), ECG, and CTT data (raw and moving average) before, during, and after stimulation; with an expanded view (inset) of EEG and ECG data. Spectrogram for an ( **l** ) F30 stimulation trial, derived from the EEG timeseries trial in panel ( **k** ) and spectrogram for an ( **o** ) M30 stimulation trial, derived from the EEG timeseries trial in panel ( **n** ). One trial of behavioral (CTT) data, for an ( **m** ) F30 and ( **p** ) M30 stimulation trial, comparing 30 secs before ( _Pre_ ), during, and after ( _Post_ ) stimulation. Mean deviation is indicated by dashed vertical lines. Panels ( **k–p** ) all show exemplary data for participant 24. ( **q,r** ) Behavioral (CTT) deviation from the center of the annulus, for one participant who repeated Experiment 2, three times with F30 and M30 montages. Each experimental run is indicated with a different participant number (1st run = _22_ , 2nd run = _23_ , 3rd run = _24_ ). Deviation scores are indicted for 30 secs pre, during, and post stimulation. Mean deviation is indicated in orange, median is indicated in yellow, and each trial is indicted in shades of blue. 

Scientific **Data** | _(2021) 8:274_ | https://doi.org/10.1038/s41597-021-01046-y 

11 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

|||**CTT De**|**viation Ch**|**ange (%)**|**EEG PSD**|**(dB/Hz)**||
|---|---|---|---|---|---|---|---|
|**Experiment**<br>**Stim Type**|**Sample Size**|**Mean**|**Std**|**95% CI (+/−)**|**Mean**|**Std**|**95% CI (+/−)**|
|F0|9|8.02|19.98|15.36|146.01|10.66|8.19|
|F5|10|0.77|11.72|8.38|145.15|10.53|7.53|
|F30|10|4.69|12.93|9.25|149.61|9.90|7.08|
|M0|9|−2.94|11.50|8.84|157.31|7.51|5.77|
|1<br>M5|10|−4.28|26.74|19.13|145.97|7.57|5.42|
|M30|10|0.26|26.18|18.73|145.94|7.56|5.41|
|P0|10|−6.47|14.78|10.57|160.78|11.46|8.20|
|P5|9|−2.56|7.47|5.74|155.26|11.06|8.50|
|P30|10|−0.39|14.98|10.72|148.55|9.87|7.06|
|F30|9|9.67|17.17|13.20|152.04|9.15|7.04|
|2<br>M30|9|8.42|16.38|12.59|155.57|3.50|2.69|



**Table 4.** Experiment 1 and 2 group-wise CTT deviation change and EEG PSD. The EEG PSD (dB/Hz) at the most dominant frequency during stimulation at electrode FC5 for frontal stimulation, C3 for motor stimulation, and CP5 for parietal stimulation; as well as the CTT deviation change (%) is tabulated across participants and all trials for each stimulation condition. The sample size, mean, standard deviation ( _Std_ ), and 95% confidence interval ( _95% CI_ (+/−)) for each metric is also tabulated. 

In addition, we extracted and tabulated the PSD at the most dominant frequency during stimulation for all participants and all trials, across both experiments (see Online-only Table 1 for Experiment 1 and Online-only Table 2 for Experiment 2). All dominant frequencies matched the frequency of programmed stimulation (i.e. 0 Hz for F0, M0, P0; 5 Hz for F5, M5, P5; and 30 Hz for F30, M30, P30). These are tabulated together with behavioral data (CTT deviation change) for each trial of all participants across both experiments. These tabulated data also contain trial-wise means and standard deviations, whereas group-wise sample sizes, means, standard deviations, and confidence intervals can be found in Table 4. Metrics for participants who repeated the experiment were averaged across repeats before being added to group-wise metrics. 

CTT data were examined after each experimental session to ensure data were a continuous stream that approximated the time of the EEG, ECG and EOG recordings. Since CTT data were sampled at the frequency of the experimental monitor’s screen refresh rate, data were sometimes nonuniformly sampled at 60 Hz. This nonuniformity was eliminated _post hoc_ with uniform sampling using the _resample_ function in MATLAB. The CTT data were then examined 30 secs before, during, and after stimulation. The mean across trials for each time period was computed for each stimulation montage across participants for both Experiment 1 and 2 (Fig. 4h,i). For Experiment 2, we examined the average percent change in deviation (taken over 20 trials) for each participant and each stimulation type (F30 and M30; Fig. 4i). We then expanded our examination to look at each participants’ performance (percent change in deviation) on a trial-to-trial level for each stimulation type (F30 and M30; Fig. 4j). Four of the participants who repeated the experiments were denoted with unique participant numbers including participant number 12,19; participant number 15, 18; participant number 21, 25, 26; and participant number 22, 23, 24 (Fig. 4i,j). Two trials for session 1 and 2 for participant 24 are examined in detail from different perspectives including as a timeseries signal plotted with concurrent CTT (Fig. 4k,n); as a time-frequency breakdown (spectrogram) of the EEG voltage from C3 (Fig. 4l,o), and as behavioral comparison of CTT data pre, during, and post stimulation (Fig. 4m,p). Behavioral CTT data for all three repeats for participant number 22, 23, 24 were examined in detail for F30 and M30 stimulation montages (Fig. 4q,r). 

During EEG, ECG, and EOG data collection; data were monitored in real time to ensure continuous data streaming. For participant 01 session 01 and session 02, data collection was halted at the end of the sessions (0101 and 0102) due to a technical error. Session 0101 contained 1 trial of F0 for ~2 mins, whereas session 0102 contained 1 trial of F0 for 30 sec. For participant 02 session 01 (data record 0201), the first trial of F30 contained a ramp-up/down time of 30 secs rather than 5 secs. Subsequent trials for 0201 contained a 5 sec ramp-up/down time. EEG amplitudes over time were examined to confirm expected stimulation-generated scalp voltage (voltage artifact see<sup>21,22</sup> ) during stimulation and concurrency with ECG and CTT data (Fig. 4k,n). EEG spectra during stimulation were examined to ensure that they contained significant power at the frequencies of stimulation (0 Hz, 5 Hz, 30 Hz; Fig. 4l,o). The CTT deviations, for the aforementioned examinations, were computed and its distributions were examined on a trial-by-trial basis (Fig. 4q,r). 

### **Code availability** 

The latest version of all accompanying code for this dataset can be acquired within this repository: https://github. com/ngebodh/GX_tES_EEG_Physio_Behavior. MATLAB, version 2018b and 2019b were utilized with functions from EEGlab<sup>96</sup> , Raincloud plots toolbox<sup>97</sup> , and ANT neuro’s import functions<sup>95</sup> . 

Received: 27 January 2021; Accepted: 25 August 2021; Published: xx xx xxxx 



<!-- Start of picture text -->
Published: xx xx xxxx<br><!-- End of picture text -->

Scientific **Data** | _(2021) 8:274_ | https://doi.org/10.1038/s41597-021-01046-y 

12 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

### **References** 

1. Gözenman, F. & Berryhill, M. E. Working memory capacity differentially influences responses to tDCS and HD-tDCS in a retro-cue task. _Neuroscience Letters_ **629** , 105–109, https://doi.org/10.1016/j.neulet.2016.06.056 (2016). 

2. Chua, E. F., Ahmed, R. & Garcia, S. M. Effects of HD-tDCS on memory and metamemory for general knowledge questions that vary by difficulty. _Brain Stimulation_ **10** , 231–241, https://doi.org/10.1016/j.brs.2016.10.013 (2017). 

3. Clancy, K. J. _et al_ . Lasting connectivity increase and anxiety reduction via transcranial alternating current stimulation. _Social Cognitive and Affective Neuroscience_ **13** , 1305–1316, https://doi.org/10.1093/scan/nsy096 (2018). 

4. Coffman, B. A., Clark, V. P. & Parasuraman, R. Battery powered thought: enhancement of attention, learning, and memory in healthy adults using transcranial direct current stimulation. _NeuroImage_ **85** , 895–908, https://doi.org/10.1016/j. neuroimage.2013.07.083 (2014). Pt 3. 

5. Morya, E. _et al_ . Beyond the target area: an integrative view of tDCS-induced motor cortex modulation in patients and athletes. _Journal of Neuroengineering and Rehabilitation_ **16** , 141, https://doi.org/10.1186/s12984-019-0581-1 (2019). 

6. Cole, L. _et al_ . Effects of high-definition and conventional transcranial direct-current stimulation on motor learning in children. _Frontiers in Neuroscience_ **12** , 787, https://doi.org/10.3389/fnins.2018.00787 (2018). 

7. Bikson, M. _et al_ . Rigor and reproducibility in research with transcranial electrical stimulation: an NIMH-sponsored workshop. _Brain Stimulation_ **11** , 465–480, https://doi.org/10.1016/j.brs.2017.12.008 (2018). 

8. Castillo-Saavedra, L. _et al_ . Clinically effective treatment of Fibromyalgia pain with high-definition transcranial direct current stimulation: phase II open-label dose optimization. _The Journal of Pain: Official Journal of the American Pain Society_ **17** , 14–26, https://doi.org/10.1016/j.jpain.2015.09.009 (2016). 

9. Datta, A. _et al_ . Gyri-precise head model of transcranial direct current stimulation: improved spatial focality using a ring electrode versus conventional rectangular pad. _Brain Stimulation_ **2** , 201–207, https://doi.org/10.1016/j.brs.2009.03.005 (2009). 207.e201. 

10. Reinhart, R. M. G. & Nguyen, J. A. Working memory revived in older adults by synchronizing rhythmic brain circuits. _Nature Neuroscience_ **22** , 820–827, https://doi.org/10.1038/s41593-019-0371-x (2019). 

11. Nguyen, J., Deng, Y. & Reinhart, R. M. G. Brain-state determines learning improvements after transcranial alternating-current stimulation to frontal cortex. _Brain Stimulation_ **11** , 723–726, https://doi.org/10.1016/j.brs.2018.02.008 (2018). 

12. Lang, S., Gan, L. S., Alrazi, T. & Monchi, O. Theta band high definition transcranial alternating current stimulation, but not transcranial direct current stimulation, improves associative memory performance. _Scientific Reports_ **9** , 8562, https://doi. org/10.1038/s41598-019-44680-8 (2019). 

13. Abellaneda-Pérez, K. _et al_ . Differential tDCS and tACS effects on working memory-related neural activity and resting-state connectivity. _Frontiers in Neuroscience_ **13** , 1440, https://doi.org/10.3389/fnins.2019.01440 (2019). 

14. Jog, M. _et al_ . Concurrent imaging of markers of current flow and neurophysiological changes during tDCS. _Frontiers in Neuroscience_ **14** , 374, https://doi.org/10.3389/fnins.2020.00374 (2020). 

15. Esmaeilpour, Z. _et al_ . Methodology for tDCS integration with fMRI. _Human Brain Mapping_ **41** , 1950–1967, https://doi.org/10.1002/ hbm.24908 (2020). 

16. Zheng, X., Alsop, D. C. & Schlaug, G. Effects of transcranial direct current stimulation (tDCS) on human regional cerebral blood flow. _NeuroImage_ **58** , 26–33, https://doi.org/10.1016/j.neuroimage.2011.06.018 (2011). 

17. McDermott, T. J. _et al_ . tDCS modulates behavioral performance and the neural oscillatory dynamics serving visual selective attention. _Human Brain Mapping_ **40** , 729–740, https://doi.org/10.1002/hbm.24405 (2019). 

18. Baxter, B. S., Edelman, B. J., Sohrabpour, A. & He, B. Anodal transcranial direct current stimulation increases bilateral directed brain connectivity during motor-imagery based brain-computer interface control. _Frontiers in Neuroscience_ **11** , 691, https://doi. org/10.3389/fnins.2017.00691 (2017). 

19. Dmochowski, J. P., Koessler, L., Norcia, A. M., Bikson, M. & Parra, L. C. Optimal use of EEG recordings to target active brain areas with transcranial electrical stimulation. _NeuroImage_ **157** , 69–80, https://doi.org/10.1016/j.neuroimage.2017.05.059 (2017). 

20. Lazarev, V. V., Gebodh, N., Tamborino, T., Bikson, M. & Caparelli-Daquer, E. M. Experimental-design specific changes in spontaneous EEG and during intermittent photic stimulation by high definition transcranial direct current stimulation. _Neuroscience_ **426** , 50–58, https://doi.org/10.1016/j.neuroscience.2019.11.016 (2020). 

21. Gebodh, N. _et al_ . Inherent physiological artifacts in EEG during tDCS. _Neuroimage_ **185** , 408–424, https://doi.org/10.1016/j. neuroimage.2018.10.025 (2019). 

22. Noury, N., Hipp, J. F. & Siegel, M. Physiological processes non-linearly affect electrophysiological recordings during transcranial electric stimulation. _NeuroImage_ **140** , 99–109, https://doi.org/10.1016/j.neuroimage.2016.03.065 (2016). 

23. Roy, A., Baxter, B. & He, B. High-definition transcranial direct current stimulation induces both acute and persistent changes in broadband cortical synchronization: a simultaneous tDCS-EEG study. _IEEE transactions on bio-medical engineering_ **61** , 1967–1978, https://doi.org/10.1109/TBME.2014.2311071 (2014). 

24. Baniasadi, M., Proverbio, D., Gonçalves, J., Hertel, F. & Husch, A. FastField: an open-source toolbox for efficient approximation of deep brain stimulation electric fields. Preprint at https://doi.org/10.1101/2020.03.03.974642 (2020). 

25. Lauro, P. M., Lee, S., Ahn, M., Barborica, A. & Asaad, W. F. DBStar: an open-source tool kit for imaging analysis with patientcustomized deep brain stimulation platforms. _Stereotactic and Functional Neurosurgery_ **96** , 13–21, https://doi.org/10.1159/000486645 (2018). 

26. Lauro, P. M. _et al_ . DBSproc: an open source process for DBS electrode localization and tractographic analysis. _Human Brain Mapping_ **37** , 422–433, https://doi.org/10.1002/hbm.23039 (2016). 

27. Huang, Y., Datta, A., Bikson, M. & Parra, L. C. Realistic volumetric-approach to simulate transcranial electric stimulation— ROAST—a fully automated open-source pipeline. _Journal of Neural Engineering_ **16** , 056006, https://doi.org/10.1088/1741-2552/ ab208d (2019). 

28. Saturnino, G. B. _et al_ . _SimNIBS 2.1: a comprehensive pipeline for individualized electric field modelling for transcranial brain stimulation_ . (Springer, 2019). 

29. Lio, G., Thobois, S., Ballanger, B., Lau, B. & Boulinguez, P. Removing deep brain stimulation artifacts from the electroencephalogram: issues, recommendations and an open-source toolbox. _Clinical Neurophysiology: Official Journal of the International Federation of Clinical Neurophysiology_ **129** , 2170–2185, https://doi.org/10.1016/j.clinph.2018.07.023 (2018). 

30. Hussain, S. Single-pulse open-loop TMS-EEG dataset. _OpenNeuro_ https://openneuro.org/datasets/ds002094/versions/1.0.0 (2019). 31. Reteig, L. C., Newman, L. A., Ridderinkhof, K. R. & Slagter, H. A. EEG study of the attentional blink; before, during, and after transcranial direct current stimulation (tDCS). _OpenNeuro_ https://doi.org/10.18112/openneuro.ds001810.v1.1.0 (2019). 

32. Holgado, D. M. _et al_ . tDCS over the left prefrontal cortex does not affect time-trial self-paced cycling performance: evidence from oscillatory brain activity and power output. Preprint at https://doi.org/10.1101/341388 (2018). 

33. Mikulan, E. _et al_ . Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. _Scientific Data_ **7** , 127, https://doi.org/10.1038/s41597-020-0467-x (2020). 

34. Huang, Y. _et al_ . Measurements and models of electric fields in the _in vivo_ human brain during transcranial electric stimulation. _eLife_ **6** , https://doi.org/10.7554/eLife.18834 (2017). 

35. Huang, Y., Parra, L. C. & Haufe, S. The New York Head-a precise standardized volume conductor model for EEG source localization and tES targeting. _NeuroImage_ **140** , 150–162, https://doi.org/10.1016/j.neuroimage.2015.12.019 (2016). 

36. Khadka, N. _et al_ . Realistic anatomically detailed open-source spinal cord stimulation (RADO-SCS) model. _Journal of Neural Engineering_ **17** , 026033, https://doi.org/10.1088/1741-2552/ab8344 (2020). 

Scientific **Data** | _(2021) 8:274_ | https://doi.org/10.1038/s41597-021-01046-y 

13 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

37. Esmaeilpour, Z., Kronberg, G., Reato, D., Parra, L. C. & Bikson, M. Temporal interference stimulation targets deep brain regions by modulating neural oscillations. Preprint at https://doi.org/10.1101/2019.12.25.888412 (2020). 

38. Botvinik-Nezer, R. _et al_ . Variability in the analysis of a single neuroimaging dataset by many teams. _Nature_ **582** , 84–88, https://doi. org/10.1038/s41586-020-2314-9 (2020). 

39. Wiese, E., Abubshait, A., Azarian, B. & Blumberg, E. J. Brain stimulation to left prefrontal cortex modulates attentional orienting to gaze cues. _Philosophical Transactions of the Royal Society of London. Series B, Biological Sciences_ **374** , 20180430, https://doi. org/10.1098/rstb.2018.0430 (2019). 

40. Lo, O. Y., van Donkelaar, P. & Chou, L. S. Effects of transcranial direct current stimulation over right posterior parietal cortex on attention function in healthy young adults. _The European Journal of Neuroscience_ **49** , 1623–1631, https://doi.org/10.1111/ejn.14349 (2019). 

41. Nelson, J. T. _et al_ . Enhancing vigilance in operators with prefrontal cortex transcranial direct current stimulation (tDCS). _NeuroImage_ **85 Pt 3** , 909–917, https://doi.org/10.1016/j.neuroimage.2012.11.061 (2014). Pt 3. 

42. Clark, V. P. _et al_ . TDCS guided using fMRI significantly accelerates learning to identify concealed objects. _NeuroImage_ **59** , 117–128, https://doi.org/10.1016/j.neuroimage.2010.11.036 (2012). 

43. Fiori, V., Nitsche, M. A., Cucuzza, G., Caltagirone, C. & Marangolo, P. High-definition transcranial direct current stimulation improves verb recovery in aphasic patients depending on current intensity. _Neuroscience_ **406** , 159–166, https://doi.org/10.1016/j. neuroscience.2019.03.010 (2019). 

44. Martin, D. M. _et al_ . Pre-treatment attentional processing speed and antidepressant response to transcranial direct current stimulation: results from an international randomized controlled trial. _Brain Stimulation_ **11** , 1282–1290, https://doi.org/10.1016/j. brs.2018.08.011 (2018). 

45. Shiasy, Y., Shakiba, S., Taremian, F., Akhavan Hejazi, S. M. & Abasi, A. The effectiveness of attention bias modification with and without trans cranial direct current stimulation in chronic low back pain. _Iranian Journal of Psychiatry_ **15** , 112–125 (2020). 

46. Myruski, S., Cho, H., Bikson, M. & Dennis-Tiwary, T. A. Transcranial direct current stimulation (tDCS) augments the effects of gamified, mobile attention bias modification. Preprint at https://doi.org/10.1101/2020.04.20.20057141 (2020). 

47. Makeig, S. & Jolley, K. _COMPTRACK: a compensatory tracking task for monitoring alertness_ . (Naval Health Research Center San Diego Ca, 1995). 

48. Makeig, S., Jung, T. P. & Sejnowski, T. J. Awareness during drowsiness: dynamics and electrophysiological correlates. _Canadian Journal of Experimental Psychology_ **54** , 266–273, https://doi.org/10.1037/h0087346 (2000). 

49. Huang, R. S., Jung, T. P., Delorme, A. & Makeig, S. Tonic and phasic electroencephalographic dynamics during continuous compensatory tracking. _NeuroImage_ **39** , 1896–1909, https://doi.org/10.1016/j.neuroimage.2007.10.036 (2008). 

50. Huang, R. S., Jung, T. P. & Makeig, S. Analyzing event-related brain dynamics in continuous compensatory tracking tasks. _2005 IEEE Engineering in Medicine and Biology 27th Annual Conference_ . 5750–5753, https://doi.org/10.1109/IEMBS.2005.1615794 (2005). 

51. Huber, R. _et al_ . Human cortical excitability increases with time awake. _Cerebral Cortex_ **23** , 1–7, https://doi.org/10.1093/cercor/ bhs014 (2013). 

52. Huang, R. S., Jung, T. P. & Makeig, S. Event-related brain dynamics in continuous sustained-attention tasks. _International Conference on Foundations of Augmented Cognition_ , 65-74, https://doi.org/10.1007/978-3-540-73216-7_8 (2007). 

53. Schenka, C., Schnupp, T., Heinze, C., Krajewski, J. & Golz, M. The compensatory tracking task: a pattern recognition based approach for classifying vigilance. _Proceedings Measuring Behavior_ **7** , 470–472 (2010). 

54. Nitsche, M. A. & Paulus, W. Excitability changes induced in the human motor cortex by weak transcranial direct current stimulation. _J Physiol_ **527** , 633–639 (2000). Pt 3. 

55. Bindman, L. J., Lippold, O. C. J. & Redfearn, J. W. T. The action of brief polarizing currents on the cerebral cortex of the rat (1) during current flow and (2) in the production of long-lasting after-effects. _The Journal of Physiology_ **172** , 369–382 (1964). 

56. Reato, D., Bikson, M. & Parra, L. C. Lasting modulation of _in vitro_ oscillatory activity with weak direct current stimulation. _Journal of Neurophysiology_ **113** , 1334–1341, https://doi.org/10.1152/jn.00208.2014 (2015). 

57. Antal, A. _et al_ . Comparatively weak after-effects of transcranial alternating current stimulation (tACS) on cortical excitability in humans. _Brain Stimulation_ **1** , 97–105, https://doi.org/10.1016/j.brs.2007.10.001 (2008). 

58. Kronberg, G., Rahman, A., Sharma, M., Bikson, M. & Parra, L. C. Direct current stimulation boosts hebbian plasticity _in vitro_ . _Brain Stimulation_ **13** , 287–301, https://doi.org/10.1016/j.brs.2019.10.014 (2020). 

59. Reato, D., Rahman, A., Bikson, M. & Parra, L. C. Low-intensity electrical stimulation affects network dynamics by modulating population rate and spike timing. _The Journal of Neuroscience: The Official Journal of the Society for Neuroscience_ **30** , 15067–15079, https://doi.org/10.1523/JNEUROSCI.2059-10.2010 (2010). 

60. Fröhlich, F. & McCormick, D. A. Endogenous electric fields may guide neocortical network activity. _Neuron_ **67** , 129–143, https://doi. org/10.1016/j.neuron.2010.06.005 (2010). 

61. Reato, D. _et al_ . Transcranial electrical stimulation accelerates human sleep homeostasis. _PLoS computational biology_ **9** , e1002898, https://doi.org/10.1371/journal.pcbi.1002898 (2013). 

62. Gebodh, N., Vanegas, M. I. & Kelly, S. P. Effects of stimulus size and contrast on the initial primary visual cortical response in humans. _Brain Topogr_ **30** , 450–460, https://doi.org/10.1007/s10548-016-0530-2 (2017). 

63. Cancel, L. M., Arias, K., Bikson, M. & Tarbell, J. M. Direct current stimulation of endothelial monolayers induces a transient and reversible increase in transport due to the electroosmotic effect. _Scientific Reports_ **8** , 9265, https://doi.org/10.1038/s41598-01827524-9 (2018). 

64. Bikson, M. _et al_ . Effects of uniform extracellular DC electric fields on excitability in rat hippocampal slices _in vitro_ . _The Journal of Physiology_ **557** , 175–190, https://doi.org/10.1113/jphysiol.2003.055772 (2004). 

65. Deans, J. K., Powell, A. D. & Jefferys, J. G. R. Sensitivity of coherent oscillations in rat hippocampus to AC electric fields. _The Journal of Physiology_ **583** , 555–565, https://doi.org/10.1113/jphysiol.2007.137711 (2007). 

66. Maeda, K. _et al_ . Weak sinusoidal electric fields entrain spontaneous Ca transients in the dendritic tufts of CA1 pyramidal cells in rat hippocampal slice preparations. _PloS One_ **10** , e0122263, https://doi.org/10.1371/journal.pone.0122263 (2015). 

67. Radman, T., Su, Y., An, J. H., Parra, L. C. & Bikson, M. Spike timing amplifies the effect of electric fields on neurons: implications for endogenous field effects. _The Journal of Neuroscience: The Official Journal of the Society for Neuroscience_ **27** , 3030–3036, https://doi. org/10.1523/JNEUROSCI.0095-07.2007 (2007). 

68. Huang, J. _et al_ . Evoked potentials and behavioral performance during different states of brain arousal. _BMC neuroscience_ **18** , 21, https://doi.org/10.1186/s12868-017-0340-9 (2017). 

69. Oken, B. S., Salinsky, M. C. & Elsas, S. M. Vigilance, alertness, or sustained attention: physiological basis and measurement. _Clinical neurophysiology: official journal of the International Federation of Clinical Neurophysiology_ **117** , 1885–1901, https://doi.org/10.1016/j. clinph.2006.01.017 (2006). 

70. Jung, T. P. _et al_ . Arousing feedback rectifies lapse in performance and corresponding EEG power spectrum. _2010 Annual International Conference of the IEEE Engineering in Medicine and Biology_ , https://doi.org/10.1109/IEMBS.2010.5626392 (2010). 

71. Tzyy-Ping, J., Makeig, S., Stensmo, M. & Sejnowski, T. J. Estimating alertness from the EEG power spectrum. _IEEE Transactions on Biomedical Engineering_ **44** , 60–69, https://doi.org/10.1109/10.553713 (1997). 

72. Lenartowicz, A. _et al_ . Electroencephalography correlates of spatial working memory deficits in attention-deficit/hyperactivity disorder: vigilance, encoding, and maintenance. _Journal of Neuroscience_ **34** , 1171–1182, https://doi.org/10.1523/ JNEUROSCI.1765-13.2014 (2014). 

Scientific **Data** | _(2021) 8:274_ | https://doi.org/10.1038/s41597-021-01046-y 

14 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

73. Habelt, B., Arvaneh, M., Bernhardt, N. & Minev, I. Biomarkers and neuromodulation techniques in substance use disorders. _Bioelectronic Medicine_ **6** , https://doi.org/10.1186/s42234-020-0040-0 (2020). 

74. Roy, Y. _et al_ . Deep learning-based electroencephalography analysis: a systematic review. _Journal of Neural Engineering_ **16** , 051001, https://doi.org/10.1088/1741-2552/ab260c (2019). 

75. Yang, G. R. & Wang, X. J. Artificial neural networks for neuroscientists: a primer. _Neuron_ **107** , 1048–1070, https://doi.org/10.1016/j. neuron.2020.09.005 (2020). 

76. Farrens, J., Simmons, A., Luck, S. & Kappenman, E. Electroencephalogram (EEG) recording protocol for cognitive and affective human neuroscience research. https://doi.org/10.21203/rs.2.18328/v2 (2020). 

77. Buysse, D. J., Reynolds, C. F., Monk, T. H., Berman, S. R. & Kupfer, D. J. The Pittsburgh sleep quality index: a new instrument for psychiatric practice and research. _Psychiatry Research_ **28** , 193–213, https://doi.org/10.1016/0165-1781(89)90047-4 (1989). 

78. Akerstedt, T. & Gillberg, M. Subjective and objective sleepiness in the active individual. _Int J Neurosci_ **52** , 29–37, https://doi. org/10.3109/00207459008994241 (1990). 

79. Kaida, K. _et al_ . Validation of the Karolinska sleepiness scale against performance and EEG variables. _Clin Neurophysiol_ **117** , 1574–1581, https://doi.org/10.1016/j.clinph.2006.03.011 (2006). 

80. D’Atri, A. _et al_ . Bilateral 5 Hz transcranial alternating current stimulation on fronto-temporal areas modulates resting-state EEG. _Sci Rep_ **7** , https://doi.org/10.1038/s41598-017-16003-2 (2017). 

81. Iohom, G. in _Postoperative Pain Management An Evidence-Based Guide to Practice_ (ed George Shorten) Ch. 11, 102-108 (W.B. Saunders, 2006). 

82. Haefeli, M. & Elfering, A. Pain assessment. _European Spine Journal_ **15** , S17–S24, https://doi.org/10.1007/s00586-005-1044-x (2006). 

83. Mueller, S. T. & Piper, B. J. The psychology experiment building language (PEBL) and PEBL test battery. _Journal of Neuroscience Methods_ **222** , 250–259, https://doi.org/10.1016/j.jneumeth.2013.10.024 (2014). 

84. Kuo, H. I. _et al_ . Comparing cortical plasticity induced by conventional and high-definition 4 × 1 ring tDCS: a neurophysiological study. _Brain Stimulation_ **6** , 644–648, https://doi.org/10.1016/j.brs.2012.09.010 (2013). 

85. Huang, Y., Datta, A., Bikson, M. & Parra, L. C. in _2018 40th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)_ . 3072-3075 (2018). 

86. Villamar, M. F. _et al_ . Technique and considerations in the use of 4 × 1 ring high-definition transcranial direct current stimulation (HD-tDCS). _Journal of Visualized Experiments: JoVE_ , e50309, https://doi.org/10.3791/50309 (2013). 

87. Gebodh, N., Esmaeilpour, Z., Datta, A. & Bikson, M. Dataset of concurrent EEG, ECG, and behavior with multiple doses of transcranial electrical stimulation. _Zenodo_ https://doi.org/10.5281/zenodo.3837212 (2020). 

88. Gebodh, N. Dataset of concurrent EEG, ECG, and behavior with multiple doses of transcranial electrical stimulation -exp1-data downsampled. _Zenodo_ https://doi.org/10.5281/zenodo.3840615 (2020). 

89. Gebodh, N. Dataset of concurrent EEG, ECG, and behavior with multiple doses of transcranial electrical stimulation -exp2-data downsampled. _Zenodo_ https://doi.org/10.5281/zenodo.3840617 (2020). 

90. Gebodh, N., Esmaeilpour, Z., Datta, A. & Bikson, M. Dataset of concurrent EEG, ECG, and behavior with multiple doses of transcranial electrical stimulation - BIDS. _OpenNeuro_ https://doi.org/10.18112/openneuro.ds003670.v1.1.0 (2021). 

91. Gebodh, N. & Bikson, M. Dataset of concurrent EEG, ECG, and behavior with multiple doses of transcranial electrical stimulation - stimulation trials PSD. _figshare_ https://doi.org/10.6084/m9.figshare.14810517.v1 (2021). 

92. Gebodh, N. & Bikson, M. Dataset of concurrent EEG, ECG, and behavior with multiple doses of transcranial electrical stimulation - stimulation trials timeseries. _figshare_ https://doi.org/10.6084/m9.figshare.14810442.v1 (2021). 

93. Gebodh, N. & Bikson, M. Dataset of concurrent EEG, ECG, and behavior with multiple doses of transcranial electrical stimulation - stimulation trials topoplots. _figshare_ https://doi.org/10.6084/m9.figshare.14810478 (2021). 

94. Smyth, C. The pittsburgh sleep quality index (PSQI). _Insight - the Journal of the American Society of Ophthalmic Registered Nurses_ **25** , 97–98, https://doi.org/10.1067/min.2000.107649 (2000). 

95. ANT Neuro Development Team. _Supporting documentation and downloads_ https://www.ant-neuro.com/support/supportingdocumentation-and-downloads (2021). 

96. Delorme, A. & Makeig, S. EEGLAB: an open source toolbox for analysis of single-trial EEG dynamics including independent component analysis. _J Neurosci Methods_ **134** , 9–21, https://doi.org/10.1016/j.jneumeth.2003.10.009 (2004). 

97. Allen, M., Poggiali, D., Whitaker, K., Marshall, T. R. & Kievit, R. A. Raincloud plots: a multi-platform tool for robust data visualization. _Wellcome Open Research_ **4** , 63, https://doi.org/10.12688/wellcomeopenres.15191.1 ( 20 19 ). 

### **acknowledgements** 

Portions of this study were funded by X (formerly Google X), the Moonshot Factory. The funding source had no influence on study conduction or result evaluation. MB is further supported by grants from the National Institutes of Health: R01NS101362, R01NS095123, R01NS112996, R01MH111896, R01MH109289, and (to NG) NIH-GRISE T32GM136499. We would like to thank Yu Xin Zhu and Michaela Chum for all their technical assistance. 

### **author contributions** 

N. Gebodh designed the experiment, collected data, ran data analysis, created data visualizations, and wrote the manuscript. M. Bikson designed the experiment and wrote the manuscript. A. Datta designed the experiment and revised the manuscript. Z. Esmaeilpour ran _pre-hoc_ validation modeling and wrote the manuscript. All the authors read and approved the final manuscript. 

### **Competing interests** 

The City University of New York has patents on Brain Stimulation with MB and AD as inventors. MB and AD have equity in Soterix Medical Inc. MB consults, received grants, assigned inventions, and/or serves on the SAB of Boston Scientific, GlaxoSmithKline, Biovisics, Mecta, Halo Neuroscience, X. 

### **additional information** 

**Correspondence** and requests for materials should be addressed to N.G. 

**Reprints and permissions information** is available at www.nature.com/reprints. 

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

Scientific **Data** | _(2021) 8:274_ | https://doi.org/10.1038/s41597-021-01046-y 

15 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/. 

The Creative Commons Public Domain Dedication waiver http://creativecommons.org/publicdomain/zero/1.0/ applies to the metadata files associated with this article. 

© The Author(s) 2021 

16 

Scientific **Data** | _(2021) 8:274_ | https://doi.org/10.1038/s41597-021-01046-y 

