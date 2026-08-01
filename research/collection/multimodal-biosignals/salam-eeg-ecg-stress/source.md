www.nature.com/scientificreports 



# **OPEN Improving cognitive stress classification via multimodal EEG and ECG fusion: gender differences in physiological response** 

**Abdus Salam**<sup>**1**</sup> **, Fakhre Alam**<sup>**1**</sup> **, Dilawar Shah**<sup>**2**</sup> **, Sami  Ur Rahman**<sup>**1**</sup> **, Shujaat Ali**<sup>**2**</sup> **& Muhammad Tahir**<sup>**3**</sup> 

**In this paper, we present a multimodal machine learning system integrating electroencephalogram (EEG) and electrocardiogram (ECG) features to discriminate cognitive stress levels and analyze gender differences. In particular, we assess how well feature fusion enhances the classification accuracy and we also compare the physiological signs of cognitive stress in male and female subjects. A publicly available dataset, namely, ECG and EEG features for mental workload and multilevel stress classification of different sexes, was used. Three essential physiological characteristics (Theta/Alpha Ratio (TAR), Heart Rate (HR), and LF/HF Ratio) were identified in EEG signals as well as in ECG signals. The discriminative power of the features was confirmed by statistical testing, such as Shapiro-Wilk and Kruskal-Wallis tests. Dimensional reduction was performed using Principal Component Analysis (PCA). Feature fusion was performed, where EEG and ECG signals were introduced and aligned to form a complete input for the classification. Six machine learning (ML) classification models, namely Decision Tree (DT), K-Nearest Neighbors (KNN), Linear Discriminant (LD), Naive Bayes (NB), Random Forest (RF), and Support Vector Machine (SVM), were tested on binary and multiclass cognitive stress tasks. In terms of overall performance, the SVM achieved the best results, attaining 94.7% accuracy in the combined-gender classification of cognitive stress. For sex-specific classifications, LD recorded the highest score (90.9%). The multimodal SVM demonstrated superiority over the unimodal EEG/ ECG models, reaching a peak average accuracy of 92.6%. Owing to the gender-based analysis, females had a better score in classification, implying a difference in sex-related physiological patterns during cognitive stress. The results show that multimodal fusion of physiological features can improve cognitive stress classification. The suggestion of gender-based analysis highlights the possibility of cognitive monitoring systems being at a personal level. This has potential applications in education, ergonomics, and human-computer interaction.** 

**Keywords** Cognitive stress, EEG, ECG, Theta/Alpha ratio, HRV, Machine learning, Feature fusion, Gender differences, SVM, Multimodal classification 

Electroencephalogram (EEG) and electrocardiogram (ECG) have a strong correlation with mental stress, and they can be classified precisely by using machine learning algorithms<sup>1</sup> . In addition, physiological responses and model performance may be greatly affected between sex, highlighting the importance of having sex-inclusive algorithms<sup>2</sup> . Such a combined assessment enhances the quantification of mental workload and could be exploited to steer the development of neuroadaptive interfaces<sup>3</sup> . The changes in EEG activity across different levels of stress, reveal marked differences in the activation of different regions of the brain, as well as time frequency features<sup>4</sup> . As stress levels increases, theta (4–8 Hz) power increases, particularly in the frontal region<sup>5</sup> . Stress can be assessed efficiently through frontal lobe EEG frequency bands<sup>6</sup> . Models trained on alpha/theta or theta/alpha ratios (rather than absolute band power) achieved high accuracy for distinguishing mental workload vs. rest, supporting the discriminative utility of band-ratio over absolute power<sup>7</sup> . 

During the transition to cognitive stress, the ECG revealed significant changes, largely due to the effect of the autonomic nervous system. In the transition between the state of rest and cognitive stress, the heart rate increases 

1Department of Computer Science & I.T , University of Malakand , KPDir Lower, Pakistan. 2Department of Computer Science , Bacha Khan University , Charsadda, Pakistan.<sup>3</sup> Department of Computer Science , Kardan University , Kabul, Afghanistan.<sup></sup> email: dilawar_shah@bkuc.edu.pk; m.tahir@kardan.edu.af 

**Scientific Reports** |         (2026) 16:7304 

1 

| https://doi.org/10.1038/s41598-026-38356-3 

www.nature.com/scientificreports/ 

with heart rate variability (HRV) reduction in the ECG recording caused by the increase in sympathetic activity and mental stress<sup>8,9</sup> . HRV reduction is correlated with increased mental workload and stress<sup>10</sup> . Decreased HRV under cognitive stress is linked to autonomic imbalance, favoring sympathetic activation<sup>11,12</sup> . 

Feature fusion is the integration of various feature sets into a cohesive representation prior to classification, which frequently leads to better model performance than relying on individual feature types<sup>13</sup> . This approach is highly effective in machine learning, as it combines different types of features, typically sourced from various . sensors or signal domains, to boost classification accuracy and reliability<sup>14,15</sup> 

Together, heart rate (HR) and EEG identify higher stress with sex-related changes, demonstrating that integrating cardiac and brain signals improves sensitivity<sup>16</sup> . EEG features, including band ratios like theta/alpha (TAR), remain central and widely validated for mental stress and workload classification<sup>17</sup> . Feature selection . HRV indicates that a small, carefully chosen HRV subset may be sufficient to distinguish stress from non-stress<sup>18</sup> measures, particularly LF/HF, are among the most often reported and strongly related aspects of psychological stress<sup>19</sup> . 

Despite extensive work on cognitive load and stress detection using physiological signals, most prior studies have focused on either EEG or ECG independently, often using high-dimensional raw signal data or complex deep learning models that limit real-time applicability. Additionally, gender-based differences in physiological responses to cognitive stress have been largely overlooked, resulting in potentially biased models and reduced generalizability. Furthermore, many approaches emphasize overall accuracy without adequately addressing the model interpretability, feature redundancy, or computational efficiency. 

Real-world applications such as adaptive learning systems, workplace stress monitoring, and driver fatigue detection require cognitive state assessment systems that are accurate, interpretable, and computationally efficient. The need to create gender-aware, multimodal, and efficient multilevel classification models that can work in real time has become increasingly urgent as physiological monitoring has become more accessible through wearable devices. 

This study introduces a novel multimodal framework that fuses EEG-derived Theta/Alpha Ratio (TAR) and ECG-derived Heart Rate (HR) and LF/HF ratio, using a small, highly informative feature set. It applies featurelevel fusion, statistical validation (e.g., Kruskal-Wallis, PCA), and gender-based performance evaluation, an area seldom addressed in previous research. The proposed method overcomes the gap between academic research and real-time applications by combining interpretability with high accuracy and reduced complexity. 

Prior studies often treat EEG and ECG separately or use them without effective feature-level fusions. Most existing models are gender-neutral and overlook known physiological variations. Many previous models rely on complex, high-dimensional inputs (e.g., raw EEG), which hinder their practical deployment. Although deep learning models are accurate, they often act as black boxes with limited clinical or ergonomic insights. 

This study aims to establish a gender-sensitive, interpretable, and efficient multilevel cognitive stress classification system by addressing these issues, making it applicable for real-world use in educational, occupational, or healthcare environments. 

The remainder of this paper is organized as follows: Sect. 2 discusses the related work, Sect. 3 explains the materials and methods, Sect. 4 presents the results, the discussion is enclosed in Sect. 5, and Sect. 6 conveys the conclusion and future work. 

## **Literature review** 

. Previous The interaction between EEG and ECG provides valuable information during cognitive tasks<sup>20,21</sup> research has indicated that these two modalities are capable of evaluating cognitive load and attention, providing better insight into brain and heart reactions during various cognitive tasks<sup>22,23</sup> . The heart-brain link in the transition between the resting state and cognitive engagement is characterized by changeable autonomic nervous system (ANS) variability dynamics, especially via vagally conducted centralization of heart rate variability (HRV). At rest, greater HRV indicates better parasympathetic (vagal) tone, which promotes flexibility of thinking and executive functioning<sup>24</sup> . 

ECG measures heart rate variability (HRV), which is also associated with cognitive involvement. Increased cognitive load and psychological stress are typically associated with a reduction in HRV, reflecting increased sympathetic activation and decreased parasympathetic modulation<sup>25,26</sup> . Experiments have also revealed that ECG may provide a practical measure of attention, where changes in cardiac rhythm track cognitive activity during task performance<sup>27</sup> . Cognitive load generally leads to a decrease in HRV, reflecting reduced parasympathetic (vagal) activity and increased sympathetic nervous system activity. This reduction in HRV measures, including time-domain (e.g., RMSSD and SDNN) and frequency-domain indices (e.g., LF power), indicates autonomic . nervous system shifts during mental effort<sup>28</sup> 

EEG records the electrical activity of the brain in real-time in order to anticipate mental states, workload, and the ability for cognitive function<sup>29</sup> . Research has shown that EEG activity varies substantially when participants engage in vigorous cognitive tasks<sup>30</sup> . EEG data analysis may provide information on the nonlinear dynamics of the brain, which are essential for cognitive processes and temporal properties<sup>31</sup> . EEG-based detection of 2D and 3D video transitions, has demonstrated that EEG band-power and ratio properties can successfully identify cognitive states<sup>32</sup> . Cognitive stress is largely observed in the EEG theta and alpha frequency band<sup>33</sup> . Studies indicate that a rise in frontal theta power and related fall in parietal alpha power are related to increasing mental stress and have been modelled using alpha, theta, and beta frequency bands ratio, which have better accuracy in classification than individual ratios to alpha or theta bands alone<sup>7,34</sup> . Using spectral-ratio features, like the Beta/ Alpha ratio, improves the sensitivity of the classification of cognitive stress states<sup>35</sup> . TAR systematically varies with cognitive task demand (vs. rest) and cognitive ability, validating TAR as a marker of cortical engagement<sup>36</sup> . Integrating features from various domains (such as temporal and spatial) provides more detailed information that enhances the classification performance<sup>37</sup> . Merged features boost the dimensionality and richness of the 

**Scientific Reports** |         (2026) 16:7304 

2 

| https://doi.org/10.1038/s41598-026-38356-3 

www.nature.com/scientificreports/ 

input data, enabling classifiers to differentiate more effectively between varying levels of cognitive stress<sup>38</sup> . The integration of heart rate variability (HRV) from ECG with pulse rate variability (PRV) from photoplethysmography (PPG) has been demonstrated to enhance the detection accuracy for distinguishing cognitive stress states<sup>39</sup> . Utilizing feature fusion from multiple sensors, including EEG, ECG, and eye tracking, improves the precision of cognitive workload estimation in machine learning, thereby increasing the robustness of practical applications<sup>40</sup> . The EEG hybrid feature fusion vector provides high accuracy in cognitive stress classification<sup>41</sup> . Multiple physiological signals (ECG, Electrodermal Activity (EDA), and PPG) achieved higher stress recognition accuracy (98.52%, 88.38%) on two datasets and ultimately higher classification performance with machine learning models<sup>42</sup> . EEG, galvanic skin response (GSR), and PPG demonstrating that their fusion enhances cognitive load classification accuracy by addressing information redundancy and revealing common physiological mechanisms, achieving significant accuracy of 95% for two levels and 77.5% for three levels, stress classification<sup>43</sup> . EEG and EOG signal fusion for biometric authentication, emphasizing that combining features enhances recognition accuracy<sup>44</sup> . A mental stress classification method that utilizes feature fusion, integrating shallow statistical features and deep features from physiological signals, enhances the classification accuracy. Utilizing the squeezeexcitation attention mechanism and voting classifier indicates that similar methods could potentially improve . cognitive load classification by leveraging multiple physiological signals such as EEG, ECG, HRV, and GSR<sup>13</sup> ECG signals can effectively supplement EEG signals, and the fusion of ECG with EEG improves classification accuracy, demonstrating the potential of multimodal signal fusion for effective mental stress estimation in cognitive activities<sup>45</sup> . The classification of cognitive stress using functional near-infrared spectroscopy (fNIRS) and ECG signals achieved mean accuracies ranging from 61% to 84% for different n-back task difficulties, indicating the potential benefits of feature-level fusion in machine learning algorithms such as SVM<sup>46</sup> . Manifold learning techniques such as Multidimensional Scaling (MDS) applied in intermediate fusion can reduce feature dimensionality while preserving important relationships, achieving high accuracy (up to 96%) in stress detection<sup>47</sup> . EEG frequency bands especially theta, alpha, and beta supplied to extreme learning machine classifier, contributed accuracy of 98.56% of detecting stress<sup>48</sup> . EEG Alpha waves are strongly associated with relaxation, while theta are linked to focused attention and cognitive engagement<sup>49</sup> . The EEG frontal theta and posterior alpha electrode responses appeared to be more related to mental arithmetic tasks<sup>50</sup> . 

The value of EEG characteristics is demonstrated by studies that compare brain responses across different visual contexts. For example, the EEG-based classification of vision disparities while watching 2D and 3D movies demonstrates how EEG may detect small cognitive and perceptual differences<sup>51</sup> . Multimodal feature fusion of EEG with ECG and machine learning models achieve good classification performance using a compact and interpretable feature set<sup>52</sup> . ECG (HRV) and EEG signals were recorded under rest, stress, and meditation, and the correlations between HRV features (including LF/HF) and EEG features (alpha power, asymmetry) revealed . five significant relationships between EEG and HRV features associated with stress<sup>53</sup> 

SVM classifier was used to differentiate stress conditions using a wearable device that simultaneously monitored EEG and ECG. The results showed that multimodal input performed better than unimodal data with 87.5% accuracy<sup>21</sup> . EEG and ECG based feature fusion approach for the detection of driver fatigue, achieved 92% accuracy in real time, revealed the practical utility of EEG and ECG fusion for physiological monitoring beyond controlled lab stress tasks<sup>54</sup> . Novel multimodal emotion detection method fused EEG and ECG data and used a deep-learning model to classify emotional states, achieving high classification accuracy (96.12% in binary), which supports the broader viability of EEG and ECG fusion for physiological state recognition<sup>55</sup> . 

Although numerous EEG and ECG features (e.g., RMSSD, SDNN, Beta power, EDA, PPG) have been reported in stress research, we focus on TAR, HR, and LF/HF because these markers directly reflect cortical workload and autonomic balance and have repeatedly shown discriminative value in mental-stress tasks. Importantly, this minimal set enables physiological interpretability and supports gender-oriented comparisons without relying on large, complex feature spaces. However, most multimodal experiments used raw EEG and ECG Features for cognitive stress classification, and gender-based evaluation of EEG Theta to Alpha band ratio (TAR), with HRV metrics received less attention. This inspired us to investigate a gender-based machine learning model for multilevel cognitive stress classification using multimodal (EEG-based TAR and ECG-based HRV) feature fusion techniques. 

To the best of our knowledge, relatively few studies have jointly fused EEG theta to alpha band-ratio (TAR) features with ECG-derived HRV measures at the feature level while simultaneously performing gender-aware analyses of cognitive stress classification, by utilizing a relatively large sample size. This approach not only enhances the robustness and generalizability of the cognitive stress classification model but also evaluates the use of both EEG and ECG modalities for cognitive stress classification. 

## **Methodology** 

This section summarizes the experimental protocol employed for the study, EEG and ECG data acquisition and preprocessing, feature extraction, feature selection, statistical techniques, feature fusion, and performance evaluation using machine learning models. Figure 1 shows our proposed system architecture. Our methodology comprises three basic steps. The former is the dataset description, which is explained in detail in Sect. 3.1. The feature selection and statistical techniques are explained in Sect. 3.2. In Sect. 3.3, the experimental setup and machine learning models used to show model accuracy are explained, which investigate our findings/hypothesis and lead to our results and conclusions. 

### **Dataset description** 

#### _Data source and ethical approval_ 

The data used in this study were obtained from a publicly available dataset hosted on Mendeley Data  ( h t t p s : / / d a t a . m e n d e l e y . c o m / d a t a s e t s / c y h c h p x w p s / 2 ) . This dataset contains anonymized EEG and ECG recordings of 

**Scientific Reports** |         (2026) 16:7304 

3 

| https://doi.org/10.1038/s41598-026-38356-3 

www.nature.com/scientificreports/ 



**Fig. 1** . General illustration of the suggested framework for classifying cognitive stress using multi-modal (EEG & ECG) feature fusion. 

human subjects for cognitive stress analysis. As stated by the authors in the original dataset, all experiments were performed following the relevant guidelines and regulations, the protocol of the study was approved by the institutional ethics committee and informed consent was obtained in writing from all participants. Since the study was a secondary analysis of publicly available, fully anonymized data, further approval from an ethics committee was not necessary. 

#### _Participants of the study_ 

This study utilized a publicly accessible dataset of “ECG & EEG features for mental workload and multilevel stress classification in different sexes”<sup>56</sup> . EEG and ECG data were collected simultaneously from 66 healthy university students (21 males, 45 females) at The Prince of Songkla University, Songkhla, Thailand, with no history of cardiovascular or neurological diseases. The institute’s Human Research Ethics Committee approved the experimental protocol. The Thai version of the Perceived Stress Scale (T-PSS-10)<sup>57</sup> was used to quantify the subject’s underlying stress during the month before to the experiment. The questionnaire can be used to determine four levels of stress: low, moderate, high and very high. 

#### _Experimental protocol_ 

The Montreal Imaging Stress Task (MIST), extensively used to produce mild stress and investigate brain activation and physiological responses (salivary free cortisol levels) in functional imaging studies<sup>58,59</sup> , was adapted and used in this study. A sequence of computer-assisted mental arithmetic tasks (Rest ➜ AC1 ➜ AC2 ➜ AC3 ➜ AC4) for all the participants, was created to assess responses in both controlled and stressful situations. Consequently, the experiments were conducted over two distinct sessions (control and mental stress conditions). Each of these two sessions included 7 phases: training, eyes open (EO), mental arithmetic task (MAT) across four successive levels of difficulty (arithmetic calculation level 1 (AC1) to arithmetic calculation level 4 (AC4)), and recovery. 

A varying arithmetic task was employed to induce cognitive stress. Eyes open (EO Relaxation phase): After the training session, recordings were commenced for 5 min while the participants were in a relaxed position. Subjects were trained with minimal head and body movement to look at a fixation dot on the computer screen. The mental arithmetic task consisted of four difficulty levels: Each stress level was conducted for 5 min. Stress level 1 (AC1): involves addition (+) and subtraction (−) of three single-digit numbers. Stress level 2 (AC2): addition (+), subtraction (−), and multiplication (×) of three single- and double-digit numbers. Stress level 3 (AC3): Covers addition (+), subtraction (−), and multiplication (×) of four single- and double-digit numbers. Stress level 4 (AC4): Incorporates addition (+) or subtraction (−), multiplication (×), and division (/) of four single- and double-digit numbers, such as 87/3 × 7–65. 

The methods employed for both the mental stress condition and the control condition were identical, except that participants were limited in time, ensuring that they did not surpass an accuracy of 50%, while incorporating elements of social evaluative threat. An elapsed-time bar was displayed at the top of the screen, and negative feedback (‘delayed response’ and ‘time out’) was presented to impose time pressure. After each question, correctness feedback was shown, and after each difficulty level, comparative performance percentages were displayed as additional negative feedback. These elements were used to actively induce stress in participants. 

#### _Data acquisition_ 

The ECG signals were captured at a frequency of 1 kHz and underwent bandpass filtering between 0.3 and 200 Hz using two bipolar limb lead connected to an ECG amplifier (ADInstruments, Castle Hill, Australia). Eight EEG electrodes (Fp1, Fp2, F3, F4, P3, P4, T3, and T4) were positioned according to the international 10–20 system. Monopolar recordings were obtained by referencing each active electrode against the reference electrode (average mastoids), connected to EEG acquisition unit (asalab™ ANT neuro, Hengelo, the Netherlands). The 

**Scientific Reports** |         (2026) 16:7304 

4 

| https://doi.org/10.1038/s41598-026-38356-3 

www.nature.com/scientificreports/ 

impedance was maintained below 10kΩ. The signals were sampled at a rate of 2 kHz and subjected to a low-pass filter at 200 Hz. 

#### _Feature extraction_ 

A high-pass filter with a cutoff frequency of 1 Hz was applied to the ECG signals. The trained experimenter excluded cardiac arrhythmias, such as tachycardia (heart rate [HR], > 100 bpm), bradycardia (HR, < 60 bpm), and premature contractions. Subsequently, the mean HR (beats per minute) along with the following HRV features were computed: LF Norm, HF Norm, LF (0.04–0.15 Hz) (ms²), HF (0.15–0.4 Hz) (ms²), the LF/HF ratio, SDNN (ms), RMSSD (ms), NN50 (beats), AVNN (ms), pNN50 (%), SD1 (ms), SD2 (ms), the SD2/SD1 ratio, Sample Entropy (SampEn), Approximate Entropy (ApEn), DFA-Alpha1, and DFA-Alpha2. 

To eliminate artifacts and noise from the EEG signal, a low-pass filter with a cutoff frequency of 200 Hz and a high-pass filter ranging from 1 to 50 Hz (Notch FIR filter with a ± 1 Hz cutoff) were utilized. The absolute power of the EEG was calculated for each frequency band (delta 1–4 Hz, theta 4–8 Hz, alpha 8–13 Hz, beta − Ι 13–20 Hz, beta − ΙΙ 20–30 Hz, gamma 30–45 Hz) using the fast Fourier transform (FFT) across the eight electrodes. Relative power was obtained by dividing the absolute power of a specific frequency band by the total power of the EEG band (1–45 Hz). Furthermore, interhemispheric asymmetries were determined in four homologous pairs of electrodes: Fp1-Fp2 (prefrontal cortex), F3-F4 (frontal cortex), P3-P4 (parietal cortex), and T3-T4 (temporal cortex). The features extracted from all epochs for each participant were averaged to represent a single data point. Consequently, the EEG features analyzed in this research included: (1) the absolute and relative power from 8 electrode locations across 6 frequency bands, totaling 96 EEG features; and (2) the interhemispheric asymmetry of both absolute and relative power from 4 electrode pairs across 3 bands, amounting to 24 EEG features. The dataset comprised 18 ECG and 120 EEG features (138 in total). 

### **Calculation** 

#### _Feature selection_ 

Feature selection was performed using univariate statistical tests (Shapiro-Wilk and Kruskal-Wallis) to identify features with significant discriminative power. To further reduce dimensionality and eliminate redundancy, Principal Component Analysis (PCA) was applied prior to feature fusion. Rather than using absolute Theta or Alpha band power alone, we selected the Theta/Alpha Ratio (TAR). Previous work has shown that theta/alpha ratios can yield higher sensitivity to mental workload and cognitive stress than absolute power measures<sup>7</sup> .This combined approach ensured that the final feature set (HR, LF/HF, TAR) was both physiologically meaningful and compact, enhancing interpretability and preventing overfitting. 

**Theta to alpha ratio (TAR) calculation** TAR was calculated for all participants across four stress task conditions by using the following formula. 



Where: _theta F_ 3 and _theta F_ 4 are the frontal absolute spectral powers, _alpha P_ 3 and _alpha P_ 4 are the absolute spectral powers of parietal lobe of the brain. Previous studies have used different electrode sites to compute the Theta/Alpha Ratio (TAR)<sup>60,61</sup> , they collectively support a common neurophysiological principle: frontal regions generate workload-related theta activity, and parietal regions generate alpha activity associated with attentional disengagement or reduced cognitive demand. Based on this convergent evidence, our study adopts a widely generalizable TAR definition using the sum of absolute frontal theta averaged across F3 and F4 divided by the sum of absolute parietal alpha averaged across P3 and P4. 

TAR derived from EEG is indicative of mental effort, HR reflects cardiovascular response to stress, and LF/HF Ratio (from HRV) represents autonomic nervous system balance. The analysis focused on these three physiologically relevant features (TAR, HR, and LF/HF) extracted from the EEG and ECG signals. However, quality assurance checks were performed to detect and remove outliers or missing entries. 

#### _Normalization_ 

Although the authors had already preprocessed the dataset, further normalization was applied to ensure comparability across feature scales. All the selected feature values were z-score normalized across participants to reduce inter-individual variance and to scale all modalities consistently, thereby improving the robustness and generalizability of classifiers<sup>62–64</sup> . All feature variables _xi_ were standardized using the formula: 



where µ is the mean and σ is the standard deviation of that feature. 

#### _Shapiro–wilk test_ 

The Shapiro–Wilk test was conducted for each feature within each sex group to determine whether the data followed a normal distribution. 



**Scientific Reports** |         (2026) 16:7304 

5 

| https://doi.org/10.1038/s41598-026-38356-3 

www.nature.com/scientificreports/ 

Where _x_ are ordered feature values, _ai_ are derived constants of covariance matrix of the order statistics, _~~x~~_ is the sample mean. Features that failed the normality test ( _p_ <.05) were analyzed using non-parametric methods. 

#### _Kruskal–wallis h-test_ 

The Kruskal–Wallis H-test is a non-parametric statistical test used to determine whether statistically significant differences exist between the medians of three or more independent groups. This test was used to examine the differences in TAR, HR, and LF/HF across the three experimental segments. Effect sizes were reported using epsilon squared (ε²) with 95% confidence intervals. Post hoc pairwise comparisons were conducted using rankbased methods. 



Where _Ri_ = average rank of the feature in group _i_ , N = total observations, _ni_ = size of group _i_ . 

#### _Principal component analysis (PCA)_ 

Principal Component Analysis (PCA) is a foundational tool in data science and research that enables the simplification, visualization, and improved analysis of complex datasets. Its ability to reduce dimensionality while preserving essential information 



Where _X_ is the original data matrix, _W_ is the matrix of eigenvectors and _Z_ is the transformed data in the principal component space. 

Although the dataset initially contained 138 features (120 EEG and 18 ECG), statistical analyses and prior domain knowledge identified Theta/Alpha Ratio (TAR), Heart Rate (HR), and LF/HF ratio as the most discriminative and physiologically interpretable features for cognitive stress classification. To further reduce dimensionality and remove potential redundancies, Principal Component Analysis (PCA) was applied before feature fusion, ensuring that the final feature set remained compact, informative, and suitable for gender-specific analysis without overfitting. 

### **Experimental setup and performance evaluation** 

#### _Feature fusion_ 

A feature-level fusion strategy was employed to capture complementary information from both the EEG and ECG signals. Each data instance (trial or session) was represented by a fused feature vector combining the selected physiological measures into a single multimodal feature vector for each sample as follows: 



Where “ _|_ ” Denotes concatenation (not multiplication or dot product). _F_ is The fused feature vector, _F_ 1 _, F_ 2 _, · · · , Fn_ Feature vectors from different sources or models, and 

#### _Classification performance evaluation_ 

The classification process involved using six machine learning models: Decision Tree (DT), K-Nearest Neighbors (KNN), Linear Discriminant (LD), Naïve Bayes (NB), Random Forest (RF), and Support Vector Machine (SVM) for both, binary (baseline vs. stress level) and three-class (baseline vs. low vs. high stress) stress tasks, and was carried out in two separate sessions. Initially, the EEG and ECG features were introduced independently into the classification algorithms to showcase the results of the unimodal classification. Subsequently, the results of the multimodal fusion classification were displayed using feature fusion techniques. In the feature fusion method, EEG and ECG features are combined and input into the classifier. The data were grouped by subject ID and ensured that all data points corresponding to a single subject were assigned exclusively to either the training or the testing set. The final dataset was split into training and testing sets with an 80%−20% ratio. All models were evaluated using stratified 10-fold cross-validation to ensure robustness and mitigate overfitting. Evaluation metrics such as accuracy, F1 score, precision, recall, Matthews correlation coefficient (MCC), and confusion matrices were computed. 







**Scientific Reports** |         (2026) 16:7304 

6 

| https://doi.org/10.1038/s41598-026-38356-3 

www.nature.com/scientificreports/ 



**Fig. 2** . Performance evaluation architectural diagram of Machine Learning Classifier for multi-level stress classification. 

|**Feature**|**Mean**|**Std. Deviation**|**Skewness**|**Kurtosis**|**Shapiro-Wilk**|**_P_-value of Shapiro-Wilk**|**Minimum**|**Maximum**|
|---|---|---|---|---|---|---|---|---|
|TAR|−2.554 × 10<sup>–12</sup>|1|3.601|25.381|0.756|< 0.001|−1.237|9.298|
|HR|1.145 × 10<sup>–12</sup>|1|0.156|−0.185|0.99|0.027|−2.485|2.46|
|LF/HF|−1.253 × 10<sup>–11</sup>|1|4.565|38.811|0.671|< 0.001|−0.908|10.532|



**Table 1** . Descriptive statistics and normality test result of EEG and ECG features. 

Where: TP: True Positives, TN: True Negatives, FP: False Positives, and FN: False Negatives. 

**Area under the curve (AUC)** AUC represents the area under the Receiver Operating Characteristic (ROC) curve, summarizing the trade-off between the True Positive Rate (TPR) and False Positive Rate (FPR) across 2. various thresholds. The architectural diagram of the machine learning classifier is shown in Fig. 

#### _Tools and software_ 

Analyses were performed using statistical and modeling software, IBM SPSS Statistics-25 and JASP (version 0.19), capable of statistical tests and machine learning modeling. 

## **Results** 

Table 1 summarizes the descriptive statistics and normality test results for the three selected features, Theta/ Alpha Ratio (TAR), Heart Rate (HR), and LF/HF Ratio after the Z-score normalization. The Shapiro-Wilk test indicated that TAR and LF/HF significantly deviated from normality ( _p_ <.001), whereas HR showed a marginal deviation ( _p_ =.027). High skewness and kurtosis values for TAR and LF/HF further confirmed their non-normal and positively skewed distributions. These findings justify the use of nonparametric statistical tests for subsequent analyses. 

The Kruskal-Wallis H test was performed to assess whether the extracted features significantly differed across the cognitive stress segments, as shown in Table 2. TAR showed the strongest discriminative power (H = 49.946, _p_ <.001), with a large effect size (ε² = 0.154); LF/HF also significantly distinguished between segments (H = 30.598, _p_ <.001), with a medium effect size; HR exhibited a weaker but statistically significant effect (H = 9.683, _p_ =.046), with a small effect size. These findings confirm the discriminative capability of each feature and validate their inclusion in both the unimodal and multimodal classification pipelines. Principal Component Analysis (PCA) of EEG and ECG features, as shown in Table 3, demonstrates that TAR and LF/HF are not significantly associated with the main factor (RC1) and represent unique variance, possibly 

**Scientific Reports** |         (2026) 16:7304 

7 

| https://doi.org/10.1038/s41598-026-38356-3 

www.nature.com/scientificreports/ 

||||||**_²_**|**95% CI**<br>**Rank ε²**<br>|**for**<br> <br>|
|---|---|---|---|---|---|---|---|
|**Factor**||**Statistic**|**df**|**_P_**|**_Rank ε_**|**Lower**|**Upper**|
|TAR|Segment|49.946|4|< 0.001|0.154|0.091|0.242|
|HR|Segment|9.683|4|0.046|0.030|0.011|0.095|
|LF/HF|Segment|30.598|4|< 0.001|0.094|0.046|0.166|



**Table 2** . Kruskal-Wallis test for significant differences across segments (EO, AC1, AC2, AC3, AC4). 

|**Features**|**pNN50 (%)**|**NN50 (beats)**|**SDNN (ms)**|**AVNN (ms)**|**HR**|**RMSSD (ms)**|**TAR**|**LF/HF**|
|---|---|---|---|---|---|---|---|---|
|RC1|0.942|0.882|0.839|0.831|−0.67|0.529|||
|Uniqueness|0.113|0.223|0.296|0.31|0.552|0.72|0.988|0.858|



**Table 3** . Principal component analysis of EEG and ECG features, TAR, and LF/HF showed unique variance. 



**Fig. 3** . Principal component analysis path diagram, TAR, and LF/HF represent unique variance and are not significantly associated with the main factor (RC1). 

reflecting distinct EEG and autonomic dynamics. HR is moderately inversely related to the parasympatheticdominated RC1 factor, consistent with its physiological role. 

The PCA path diagram in Fig. 3 revealed that most HRV time-domain features (e.g., pNN50, SDNN) represent a strong common component valuable for classification, while frequency-domain (LF/HF) and EEG measures (TAR) add complementary, independent information. 

Among all models, SVM consistently achieved the highest accuracy, F1-scores, precision, recall, and MCC across most segment comparisons, peaking at 93.3% accuracy for EO vs. AC1 and maintaining high performance for AC2, AC3, and AC4, as shown in Table 4; Fig. 4. 

Sex differences in model performance suggest physiological and cognitive variability, highlighting the importance of personalized models or data balancing. For male participants, LD showed consistently high accuracy, F1-scores, precision, recall, and MCC across all cognitive stress comparisons, achieving 90% accuracy, as shown in Table 5; Fig. 5. 

For female participant classification performance, LD again led across all comparisons, reaching 90.9% accuracy and F1-score, as shown in Table 6; Fig. 6. 

Table 7 shows that, SVM and LD consistently deliver the best performance, reinforcing their suitability for physiological signal classification. LD performed competitively, especially for male and female group. The ROC curve of the ML models with highest-accuracy for combined gender, male, and female are shown in Fig. 7. 

### **Classification of low and high stress tasks** 

To assess the discriminative power of the multimodal feature set across broader cognitive states, classification was conducted for three task conditions: rest (EO), Low Stress (AC1 + AC2), and High Stress (AC3 + AC4). The performance was measured for binary classifications (rest vs. Low, Rest vs. high) and a 3-class problem (rest vs. low vs. high). 

SVM achieved the highest performance in both binary and multiclass settings, reaching 94.7% accuracy for Rest vs. Low and 89.5% for Rest vs. High, as shown in Table 8; Fig. 8. 

For the male sex, SVM again led across all comparisons, particularly excelling in the 3-class classification (86.7% accuracy, 75.4% F1), as shown in Table 9; Fig. 9. 

**Scientific Reports** |         (2026) 16:7304 

8 

| https://doi.org/10.1038/s41598-026-38356-3 

www.nature.com/scientificreports/ 

|**Performance Metrics**|**Stress levels**|**DT**|**KNN**|**LD**|**NB**|**RF**|**SVM**|
|---|---|---|---|---|---|---|---|
|Highest Accuracy|1|65.4|76.9|91.7|75|85.7|93.3|
||2|80.8|69.2|76.9|62.5|69.2|92.3|
||3|73.1|53.8|84.2|67.5|76.9|92.3|
||4|80.8|76.9|84.2|72.5|30.8|92.3|
||Average|75.0|69.2|84.3|69.4|65.7|92.6|
|F1 Score|1|65.7|76.6|91.7|75|85.7|93.3|
||2|80.7|69.6|76.8|58.1|71.4|92.4|
||3|73.2|53.3|84|67.2|78.7|92.3|
||4|80.9|78.7|84.1|72.7|29.9|92|
||Average|75.1|69.6|84.2|68.3|66.4|92.5|
|Precision|1|76.2|77.3|93.1|76.5|85.7|94.1|
||2|81|73.3|77.6|61|76.5|93.6|
||3|75.3|55.4|84.3|67.7|88.5|93.4|
||4|81.2|88.5|84.5|72.9|29.4|93.1|
||Average|78.4|73.625|84.88|69.53|70.03|93.6|
|Recall|1|65.4|76.9|91.7|75|85.7|93.3|
||2|80.8|69.2|76.9|62.5|69.2|92.3|
||3|73.1|53.8|84.2|67.5|76.9|92.3|
||4|80.8|76.9|84.2|72.5|30.8|92.3|
||Average|75.03|69.2|84.25|69.4|65.65|92.6|
|MCC|1|40.9|53.7|84.5|51.5|70.8|87.3|
||2|61.7|41.5|54.5|16.1|31.8|85.4|
||3|48|0.09|67.5|34.7|59.2|85.7|
||4|61.3|59.2|68.5|42.2|0.4|82.2|
||Average|52.98|38.623|68.75|36.13|40.55|85.2|



**Table 4** . Classification performance for combined gender of six machine learning models with highest accuracy of rest (EO) vs. Cognitive stress levels (AC1-AC4). The SVM classifier outperformed all the ML Models. 



**Fig. 4** . Classification performances for combined gender of six ML Models with the highest accuracy among Rest (EO) vs. four levels of stress (AC1-AC4). The SVM classifier outperformed all the ML Models. 

Female participants showed exceptionally high performance with SVM, especially in the Rest vs. High (92.3% accuracy and 92.4% F1) classification, as shown in Table 10; Fig. 10. The classification performance for females was consistently higher than that for males across nearly all models, suggesting potential sex-specific physiological and neurophysiological response patterns under cognitive stress. The rest vs. high stress condition 

**Scientific Reports** |         (2026) 16:7304 

9 

| https://doi.org/10.1038/s41598-026-38356-3 

www.nature.com/scientificreports/ 

|**Performance Metrics**|**Stress levels**|**DT**|**KNN**|**LD**|**NB**|**RF**|**SVM**|
|---|---|---|---|---|---|---|---|
|Highest Accuracy|1|75|62.5|85.7|25|50|62.5|
||2|50|50|83.3|50|37.5|75|
||3|62.5|50|87.5|25|62.5|75|
||4|62.5|75|90|58.3|50|87.5|
||Average|62.5|59.4|86.6|39.6|46.4|75|
|F1 Score|1|75|60.7|85.1|30|43.3|63.1|
||2|50|33.3|82.3|50|34.5|76.7|
||3|68.6|50|87.7|20|63.1|73.3|
||4|57.7|73.3|89.9|57.4|50|88.2|
||Average|62.8|54.3|86.3|39.4|47.7|75.3|
|Precision|1|75|81.3|88.6|37.5|78.6|65.6|
||2|50|25|87|50|43.8|87.5|
||3|90.6|50|90.6|16.7|65.6|83.3|
||4|53.6|83.3|91.7|57.3|83.3|91.7|
||Average|67.3|59.9|89.5|40.4|67.8|82.0|
|Recall|1|75|62.5|85.7|25|50|62.5|
||2|50|50|83.3|50|37.5|75|
||3|62.5|50|87.5|25|62.5|75|
||4|62.5|75|90|58.3|50|87.5|
||Average|62.5|59.4|86.6|39.6|50.0|75.0|
|MCC|1|46.7|44.7|73|0.5|29.3|25.8|
||2|0|0|68.3|0|0|57.7|
||3|37.8|0|77.5|0.6|25.8|57.7|
||4|0.2|75.7|81.6|0.2|33.3|74.5|
||Average|21.2|30.1|75.1|0.3|22.1|53.9|



**Table 5** . Classification performance for males of six machine learning models with the highest accuracy of rest (EO) vs. cognitive stress levels (AC1-AC4). The LD classifier outperformed all the ML Models. 



**Fig. 5** . Classification performances for male gender of six ML Models with the highest accuracy among Rest (EO) vs. four levels of stress (AC1-AC4). The LD classifier outperformed all the ML Models. 

was generally easier to classify than rest vs. low stress, indicating a larger physiological shift under a high cognitive stress. 

Table 11 shows that, SVM is the top-performing model across all gender groups and task configurations, particularly excelling in both binary-class (rest vs. high) and multiclass (rest vs. low vs. high) stress classification. The ROC curve of the ML models with highest-accuracy for combined gender, male, and female under low and high cognitive stress is shown in Fig. 11. 

**Scientific Reports** |         (2026) 16:7304 

10 

| https://doi.org/10.1038/s41598-026-38356-3 

www.nature.com/scientificreports/ 

|**Performance Metrics**|**Stress levels**|**DT**|**KNN**|**LD**|**NB**|**RF**|**SVM**|
|---|---|---|---|---|---|---|---|
|Highest Accuracy|1|72.2|66.7|84.2|77.8|38.9|66.7|
||2|33.3|88.9|90|55.6|72.2|88.9|
||3|72.2|77.8|84.6|77.8|77.8|83.3|
||4|55.6|66.7|90.9|63|77.8|83.3|
||Average|58.3|75|87.4|68.6|66.7|80.6|
|F1 Score|1|70.8|67.5|84.1|77.2|38.7|64.1|
||2|16.7|89.2|90|54.4|70|88.9|
||3|71.4|77.8|84.4|77.2|77.5|83.3|
||4|55.6|68.7|90.9|62|77.8|83.3|
||Average|53.6|75.8|87.4|67.7|66|79.9|
|Precision|1|74|75|84.5|85.2|38.7|81|
||2|11.1|91.7|90|59.3|82.1|88.9|
||3|75|77.8|85.3|85.2|79.2|83.7|
||4|56.9|72.2|90.9|67.9|77.8|83.7|
||Average|54.3|79.2|87.7|74.4|69.5|84.3|
|Recall|1|72.2|66.7|84.2|77.8|38.9|66.7|
||2|33.3|88.9|90|55.6|72.2|88.9|
||3|72.2|77.8|84.6|77.8|77.8|83.3|
||4|55.6|66.7|90.9|63|77.8|83.3|
||Average|58.3|75.0|87.4|68.6|66.7|80.6|
|MCC|1|44.4|39.5|68.5|63.2|0.2|47.8|
||2|0|79.1|79.8|15.8|53.5|77.8|
||3|47.1|50|69.5|63.2|57|67.1|
||4|0.13|18.9|81.2|31.6|55|67.1|
||Average|22.9|46.9|74.8|43.5|41.4|65.0|



**Table 6** . Classification performance for women of six machine learning models with the highest accuracy of rest (EO) vs. cognitive stress levels (AC1-AC4). The LD classifier outperformed all the ML Models. 



**Fig. 6** . Classification performances for the female gender of six ML Models with the highest classification accuracy among Rest (EO) vs. four levels of stress (AC1-AC4). The LD classifier outperformed all the ML Models. 

_SVM-based classification: cognitive stress discrimination using unimodal and multimodal features_ To evaluate the impact of feature fusion on cognitive stress classification, performance comparisons were made between the unimodal and multimodal implementations of the Support Vector Machine (SVM) classifier. The unimodal models were trained separately on EEG-based TAR and ECG-based features (HR and LF/HF), whereas the multimodal model combined both modalities. 

**Scientific Reports** |         (2026) 16:7304 

11 

| https://doi.org/10.1038/s41598-026-38356-3 

www.nature.com/scientificreports/ 

||**Performance Metrics**|**DT**|**KNN**|**LD**|**NB**|**RF**|**SVM**|
|---|---|---|---|---|---|---|---|
|Combined Gender|Highest Accuracy|75|69.2|84.3|69.4|65.7|92.6|
||F1 Score|75.1|69.6|84.2|68.3|66.4|92.5|
||Precision|78.4|73.6|84.8|69.5|70|93.6|
||Recall|75|69.2|84.2|69.4|65.6|92.6|
||MCC|52.9|38.6|68.7|36.13|40.5|85.2|
|Male Group|Highest Accuracy|62.5|59.4|86.6|39.6|46.4|75|
||F1 Score|62.8|54.3|86.3|39.4|47.7|75.3|
||Precision|67.3|59.9|89.5|40.4|67.8|82|
||Recall|62.5|59.4|86.6|39.6|50|75|
||MCC|21.2|30.1|75.1|0.3|22.1|53.9|
|Female Group|Highest Accuracy|58.3|75|87.4|68.6|66.7|80.6|
||F1 Score|53.6|75.8|87.4|67.7|66|79.9|
||Precision|54.3|79.2|87.7|74.4|69.5|84.3|
||Recall|58.3|75|87.4|68.6|66.7|80.6|
||MCC|22.9|46.9|**74.8**|43.5|41.4|65|



**Table 7** . Summary of the classification performance with averaged performance metrics of rest (EO) vs. stress levels (AC1-AC4), for combined gender, male and female group. 



**Fig. 7** . ROC curve for **a** ) combined gender **b** ) Female and **c** ) Male with the highest classification accuracy among six ML Models performance comparison of Rest (EO) vs. cognitive stress (AC1 − AC4). 

The multimodal SVM consistently outperformed both unimodal approaches across all cognitive stress levels (AC1–AC4), with the highest average accuracy of 92.6%, as shown in Table 12; Fig. 12. EEG and ECG provide non-redundant and complementary physiological insights into cognitive stress states. Unimodal TAR is reasonably strong on its own in high-stress contexts but underperforms in subtle tasks without an ECG. The fusion of EEG and ECG provides complementary information, boosting the classification accuracy and F1score in all cases, which confirms the effectiveness of multimodal feature fusion for improving cognitive stress classification performance. 

_Unimodal vs. multimodal SVM classification performance of low and high cognitive stress_ 

This section highlights the classification performance of Support Vector Machine (SVM) models for distinguishing between rest (EO) and different cognitive stress states, low stress (AC1 + AC2) and high stress (AC3 + AC4), using both unimodal and multimodal features. 

13 The results in Table indicate that multimodal data integration substantially improves the classification performance. The multimodal configuration resulted in an accuracy of 85.7% and an F1 score of 80.4, reflecting a strong positive correlation and a considerable improvement in the model’s predictive power, where the accuracy increased by ~ 14% and the F1 score improved by 27%, as shown in Fig. 13. These results highlight the complementary nature of EEG and ECG features, in which the fusion of neurophysiological and cardiovascular data enables more accurate and reliable classification. 

These findings demonstrate the potency of multimodal feature grouping for cognitive burden recognition. Combining EEG (TAR) with ECG (HR and LF/HF) characteristics, the SVM classifier is better able to detect the physiological variations that correlate with different levels of mental stress. This supports the establishment of multimodal monitoring systems to detect the real-time cognitive state. 

Table 14 represent repeated-measures ANOVA showed, no significant main effect of RM Factor 1, _F_ (2, 646) = 1.13, _p_ =.324, but a significant interaction between RM Factor 1 and gender, _F_ (2, 646) = 7.64, _p_ <.001, indicating that the pattern of responses across levels differed between males and females. In the between-subjects analysis, females showed significantly higher overall scores than males, _F_ (1, 323) = 6.82, _p_ =.009. 

As shown in Table 15 , Descriptive statistics revealed consistent mean differences between genders across all three physiological features. Females showed higher average HR and lower LF/HF relative to males, while 

**Scientific Reports** |         (2026) 16:7304 

12 

| https://doi.org/10.1038/s41598-026-38356-3 

www.nature.com/scientificreports/ 

|**Performance Metrics**|**Stress levels**|**DT**|**KNN**|**LD**|**NB**|**RF**|**SVM**|
|---|---|---|---|---|---|---|---|
|Highest Accuracy|Low|69|56.4|52|69|56|94.7|
||High|77|66.7|67|77|77|89.5|
||Low & High|66|63.1|72|67|65|72.9|
||Average|70.8|62.1|63.6|71.0|66.1|85.7|
|F1 Score|Low|70|56|43|68|46|94.3|
||High|77|64.9|68|78|78|88|
||Low & High|50|44.4|57|50|48|59|
||Average|65.6|55.1|55.8|65.1|57.4|80.4|
|Precision|Low|71|55.7|36|68|48|95|
||High|78|65.5|69|79|80|79.1|
||Low & High|51|44|59|52|48|70.1|
||Average|66.7|55.1|54.5|66.3|58.7|81.4|
|Recall|Low|69|56.4|52|69|56|94.7|
||High|77|66.7|67|77|77|78.9|
||Low & High|49|43.1|58|51|48|59.4|
||Average|65|55.4|58.9|65.5|60.3|77.7|
|MCC|Low|28|3.8|0|30|0|79.2|
||High|45|26|14|48|43|53.5|
||Low & High|23|12.4|30|24|18|44.8|
||Average|31.8|14.1|14.6|34|20|59.2|



**Table 8** . Classification performance for combined gender of six machine learning models with highest accuracy of rest vs. Low, rest vs. high, and rest vs. low vs. high cognitive stress tasks. The SVM classifier outperformed all ML models: rest (EO), low (AC1 + AC2), and high (AC3 + AC4). 



**Fig. 8** . Classification performance of six machine learning models for combined gender with highest accuracy of rest vs. Low stress, Rest vs. high stress, and rest vs. low vs. high cognitive stress tasks. The SVM classifier outperformed all ML Models: Rest (EO), low stress (AC1 + AC2), and high stress (AC3 + AC4). 

TAR also differed in direction. Together with the significant gender effects observed in the repeated-measures ANOVA, these descriptive results indicate that females exhibit more pronounced physiological responses across stress conditions, providing a plausible explanation for the superior classification performance observed in the female subgroup. 

Figure 14 summarizes gender differences in the EEG-TAR and HRV measures. Females showed slightly higher TAR and notably higher HR, whereas males displayed a small trend toward higher LF/HF values. Variability overlapped across groups, indicating modest gender-related differences without strong separation. 

**Scientific Reports** |         (2026) 16:7304 

13 

| https://doi.org/10.1038/s41598-026-38356-3 

www.nature.com/scientificreports/ 

|**Performance Metrics**|**Stress levels**|**DT**|**KNN**|**LD**|**NB**|**RF**|**SVM**|
|---|---|---|---|---|---|---|---|
|Highest Accuracy|Low|67|41.7|33|58|50|83.3|
||High|75|50|67|58|67|83.3|
||Low & High|60|53.3|71|67|50|86.7|
||Average|67.2|48.3|57.0|61.1|55.6|84.4|
|F1 Score|Low|53|44.1|25|59|50|75.8|
||High|77|45.7|67|61|67|81.5|
||Low & High|22|27|57|49|24|75.4|
||Average|50.7|38.9|49.6|56.6|46.9|77.6|
|Precision|Low|44|46.9|20|61|50|69.4|
||High|80|80|67|71|67|86.7|
||Low & High|16|25.1|63|50|34|75|
||Average|46.7|50.7|49.8|61|50|77.0|
|Recall|Low|67|41.7|33|58|50|83.3|
||High|75|50|67|58|67|83.3|
||Low & High|40|30|57|50|25|80|
||Average|60.6|40.6|52.2|55.5|47.2|82.2|
|MCC|Low|0|0|0|12|0|0|
||High|26|31.6|0|19|11|63.2|
||Low & High|0|0|34|26|0|68.8|
||Average|8.6|10.5|11.3|19|3.7|44|



**Table 9** . Classification performance of six machine learning models for males with the highest accuracy of rest vs. Low, rest vs. high, and rest vs. low vs. high stress tasks. The SVM classifier outperformed all ML models: rest (EO), low (AC1 + AC2), and high (AC3 + AC4). 



**Fig. 9** . Classification performance of six machine learning models for males with the highest accuracy of rest vs. Low stress, Rest vs. high stress, and rest vs. low vs. high cognitive stress tasks. The SVM classifier outperformed all ML Models: Rest (EO), low stress (AC1 + AC2), and high stress (AC3 + AC4). 

## **Discussion** 

In this work, unimodal and multimodal physiological features for cognitive stress level classification with ML are investigated and gender-based differences are analyzed. EEG theta to alpha ratio and ECG indices, such as heart rate and LF to HF ratio, provide an in-depth assessment of neural and autonomic responses under cognitive stress. The fusion of features by employing feature fusion significantly improved the classification accuracy, and further illustrated that both EEG and ECG were complementary in the measurement of mental stress. 

Many pre-existing studies have dealt with the possibility of using EEG or ECG to measure mental stress; however, they all have crucial flaws concerning the scope of modalities covered, dimensionality of the features used, gender factor, and possibility of deployment. This paper provides an in-depth comparative view of these major dimensions. 

**Scientific Reports** |         (2026) 16:7304 

14 

| https://doi.org/10.1038/s41598-026-38356-3 

www.nature.com/scientificreports/ 

|**Performance Metrics**|**Stress levels**|**DT**|**KNN**|**LD**|**NB**|**RF**|**SVM**|
|---|---|---|---|---|---|---|---|
|Highest Accuracy|Low|77.8|70.4|42.9|63|74.1|84.6|
||High|66.7|59.3|85.7|81.5|88.9|92.3|
||Low & High|65.9|57|60.2|57.2|55.6|72.7|
||Average|70.1|62.2|62.9|67.2|72.9|83.2|
|F1 Score|Low|76.1|65.1|30|63.7|73.7|81.5|
||High|68.7|50|84|81.3|88.4|92.4|
||Low & High|48|35.2|35.8|33|31.2|60|
||Average|64.3|50.1|49.9|59.3|64.4|78.0|
|Precision|Low|75.4|69.4|23.1|65.2|73.5|87.2|
||High|75|77.2|88.1|81.3|88.3|93.6|
||Low & High|47.9|35|32.8|43.9|31.8|63.6|
||Average|66.1|60.5|48|63.5|64.5|81.5|
|Recall|Low|77.8|70.4|42.9|63|74.1|84.6|
||High|66.7|59.3|85.7|81.5|88.9|92.3|
||Low & High|48.9|35.6|40.3|35.8|33.3|59.1|
||Average|64.5|55.1|56.3|60.1|65.4|78.7|
|MCC|Low|27.9|25|0|21.3|40.1|52.7|
||High|32.1|29.4|64.5|59.7|60.6|85.4|
||Low & High|21|0|0|8.1|0|38.2|
||Average|27|18.1|21.5|29.7|33.6|58.8|



**Table 10** . Classification performance of six machine learning models for women with the highest accuracy of rest vs. Low stress, rest vs. high stress, and rest vs. low vs. high stress tasks. The SVM classifier outperformed all ML models: rest (EO), low stress (AC1 + AC2), and high stress (AC3 + AC4). 



**Fig. 10** . Classification performance of six machine learning models for women with the highest accuracy of rest vs. low stress, rest vs. high stress, and rest vs. low vs. high cognitive stress tasks. The SVM classifier outperformed all ML Models: Rest (EO), low stress (AC1 + AC2), and high stress (AC3 + AC4). 

As presented in Table 16, past studies largely concentrated on the unimodal methodologies, especially the EEG with raw signals or power spectral characteristics of several channels. For example<sup>65</sup> , work based on heavy convolutional networks on EEG data fared well in terms of accuracy, but at the expense of interpretation and effective computations. However, in our study, our proposed multimodal fusion comprises combining the Theta/ Alpha Ratio (TAR) extracted using EEG and Heart Rate (HR) and LF/HF ratio derived using ECG, which are in addition to being physiologically meaningful, are computationally inexpensive. 

Unlike high-dimensional raw signal approaches<sup>14,66</sup> , our model relies on three carefully selected lowdimensional features. This enhances the model interpretability and supports real-time applications without sacrificing performance. Principal Component Analysis (PCA) in our workflow further confirmed the sufficiency and orthogonality of these features. 

**Scientific Reports** |         (2026) 16:7304 

15 

| https://doi.org/10.1038/s41598-026-38356-3 

www.nature.com/scientificreports/ 

||**Performance Metrics**|**DT**|**KNN**|**LD**|**NB**|**RF**|**SVM**|
|---|---|---|---|---|---|---|---|
|Combined Gender|Highest Accuracy|70.8|62.1|63.6|71|66.1|85.7|
||F1 Score|65.6|55.1|55.8|65.1|57.4|80.4|
||Precision|66.7|55.1|54.5|66.3|58.7|81.4|
||Recall|65|55.4|58.9|65.5|60.3|77.7|
||MCC|31.8|14.1|14.6|34|20|59.2|
|Male Group|Highest Accuracy|67.2|48.3|57|61.1|55.6|84.4|
||F1 Score|50.7|38.9|49.6|56.6|46.9|77.6|
||Precision|46.7|50.7|49.8|61|50|77|
||Recall|60.6|40.6|52.2|55.5|47.2|82.2|
||MCC|8.6|10.5|11.3|19|3.7|44|
|Female Group|Highest Accuracy|70.1|62.2|62.9|67.2|72.9|83.2|
||F1 Score|64.3|50.1|49.9|59.3|64.4|78|
||Precision|66.1|60.5|48|63.5|64.5|81.5|
||Recall|64.5|55.1|56.3|60.1|65.4|78.7|
||MCC|27|18.1|21.5|29.7|33.6|58.8|



**Table 11** . Summary of the classification performance with averaged performance metrics of rest (EO), low stress (AC1 + AC2), and high stress (AC3 + AC4), for combined gender, male and female group. The SVM classifier outperformed across all ML Models. 



**Fig. 11** . Average ROC curve for **a** ) combined gender **b** ) Female and **c** ) Male with the highest accuracy among six ML Models performance comparison of Rest (EO) vs. low & high cognitive stress. 

|**Modality**|**Features**|**Performance Metrics**|**Average**|
|---|---|---|---|
|Unimodal|EEG (TAR)|Accuracy|80|
|||F1 Score|80.1|
|||Precision|81.675|
|||Recall|80|
|||MCC|59.8|
||ECG (HR and LF/HF)|Accuracy|66.65|
|||F1 Score|65.7|
|||Precision|69.1|
|||Recall|66.65|
|||MCC|33.35|
|Multimodal|EEG & ECG|Accuracy|**92.6**|
|||F1 Score|**92.5**|
|||Precision|**93.6**|
|||Recall|**92.6**|
|||MCC|**85.2**|



**Table 12** . Cognitive stress classification performance of SVM classifier for combined gender between unimodal vs. multimodal. The SVM classifier for multimodal data outperformed between rest (EO) vs. cognitive stress levels (AC1 − AC4). 

**Scientific Reports** |         (2026) 16:7304 

16 

| https://doi.org/10.1038/s41598-026-38356-3 

www.nature.com/scientificreports/ 



**Fig. 12** . Cognitive stress classification performance of SVM classifier for combined gender between uni-modal vs. multimodal. The SVM classifier for multimodal outperformed among cognitive stress levels. 

|**Modality**|**Features**|**Performance Metrics**|**Average**|
|---|---|---|---|
|Unimodal|EEG (TAR)|Accuracy|75.2|
|||F1 Score|63.3|
|||Precision|68.2|
|||Recall|69|
|||MCC|25.2|
||ECG (HR and LF/HF)|Accuracy|71.3|
|||F1 Score|57.1|
|||Precision|50.8|
|||Recall|65.8|
|||MCC|0.0|
|Multimodal|EEG & ECG|Accuracy|**85.7**|
|||F1 Score|**80.4**|
|||Precision|**81.4**|
|||Recall|**77.7**|
|||MCC|**59.2**|



**Table 13** . Cognitive stress classification performance of SVM classifier for combined gender between unimodal vs. multimodal. The SVM classifier for multimodal outperformed for rest, low and high stress: rest (EO), low stress (AC1 + AC2), and high stress (AC3 + AC4). 

A critical innovation of this study lies in its explicit gender-based analysis, where the classification performance is reported separately for male and female participants. This finding aligns with previous studies<sup>1</sup> , suggesting sexbased variability in the physiological responses to cognitive tasks. Such variations may be attributed to hormonal influences, neuroanatomical differences, or differential autonomic reactivity under cognitive stress. Existing studies rarely address this, despite the known physiological and hormonal differences that affect cognitive and cardiovascular responses to stress. These findings underscore the necessity of incorporating gender as a factor in developing personalized cognitive monitoring systems. 

Many previous studies<sup>43,45,67</sup> have relied on complex deep learning architectures that require large datasets and significant computational power. In contrast, this study uses traditional machine learning models (e.g., SVM, LD, NB), which showed high performance with much lower computational costs. Notably, the SVM with feature fusion achieved an accuracy of up to 94.7%, surpassing many EEG-only and ECG-only benchmarks. 

Compared to existing literature, the proposed framework offers a balanced trade-off between accuracy, efficiency and interpretability. To the best of our knowledge, relatively few studies have jointly fused EEG (TAR) and ECG signals (HR, LF/HF) at the feature level, incorporating gender-aware performance analysis, using statistically validated compact and scalable features for enhanced cognitive stress discrimination. This 

**Scientific Reports** |         (2026) 16:7304 

17 

| https://doi.org/10.1038/s41598-026-38356-3 

www.nature.com/scientificreports/ 



**Fig. 13** . Cognitive stress classification performance of SVM classifier for combined gender between uni-modal vs. multimodal. The SVM classifier for multimodal outperformed for rest, low and high stress: rest (EO), low stress (AC1 + AC2), and high stress (AC3 + AC4). 

|**Cases**|**Sum of Squares**|**df**|**Mean Square**|**F**|**_p_**|
|---|---|---|---|---|---|
|Within-subjects efects||||||
|RM Factor 1|2.15|2|1.08|1.13|0.324|
|RM Factor 1✻Gender|14.55|2|7.27|7.64|< 0.001|
|Residuals (within)|615.08|646|0.95|||
|_Between Subjects Efects_||||||
|Gender|7.08|1|7.081|6.821|0.009|
|Residuals|335.29|323|1.038|||



**Table 14** . Repeated-measures ANOVA results for Within- and Between-Subjects Effects. Note. Type III Sum of Squares. 

|**RM Factor 1**|**Gender**|**_N_**|**Mean**|**SD**|**SE**|**Coefcient of**<br>**variation**|
|---|---|---|---|---|---|---|
|**TAR**|Male|100|−0.063|0.837|0.084|−13.19|
||Female|225|0.028|1.065|0.071|37.735|
|**HR**|Male|100|−0.377|1.095|0.109|−2.9|
||Female|225|0.168|0.908|0.061|5.416|
|**LF/HF**|Male|100|0.057|0.849|0.085|14.803|
||Female|225|−0.026|1.061|0.071|−41.602|



**Table 15** . Descriptive statistics for TAR, HR, and LF/HF by Gender. 

comparative assessment highlights the potential of the proposed system to serve as a real-time, personalized cognitive stress monitoring tool, particularly in the fields of education, healthcare, and ergonomics. Unimodal analysis revealed that the EEG-derived Theta/Alpha Ratio (TAR) consistently outperformed ECGbased features (HR and LF/HF) in most classification tasks. This is consistent with the prior literature<sup>7,68</sup> , as EEG captures direct cortical activity, making it more sensitive to changes in cognitive states. However, although more stable and less intrusive, the ECG features alone demonstrated limited discriminative power, particularly under low stress conditions. 

The multimodal fusion of EEG and ECG features substantially improved the classification performance across binary (e.g., EO vs. AC1 − AC4) and multiclass (e.g., EO vs. low vs. high) conditions. Specifically, the fused model reached a peak average accuracy of 92.6% using SVM. This highlights the advantage of leveraging multiple physiological pathways (cortical and autonomic) for a more robust cognitive stress assessment. 

**Scientific Reports** |         (2026) 16:7304 

18 

| https://doi.org/10.1038/s41598-026-38356-3 

www.nature.com/scientificreports/ 



**Fig. 14** . Descriptive statistics for gender differences in physiological measures. ( **a** ) EEG theta-to-alpha ratio (TAR), ( **b** ) ECG heart rate (HR), and ( **c** ) ECG LF/HF ratio for male and female participants. Points represent group means, and error bars indicate variability. Females showed slightly higher TAR and HR, whereas males exhibited a marginally higher LF/HF ratio, with considerable overlap in variability across groups. 

|**Study**|**Modality**|**Features Used**|**Fusion**|**Gender-Based**|**Accuracy**|
|---|---|---|---|---|---|
|66|ECG + EDA|Raw signals|CNN based feature fusion|✗|79.3%|
|45|EEG + ECG|Frequency bands, HRV|CNN based feature fusion|✗|91.97%|
|1|EEG + ECG|Frequency bands, HRV|✔|✔|92.7%|
|14|EDA, BVP, TEMP, and ACC|Raw signals|✔|✗|93%|
|67|EEG|Multi Domain|✗|✗|92%|
|Tis Study|EEG + ECG|TAR, HR, LF/HF|Feature-level|✔|94.7%|



**Table 16** . Comparative study of cognitive stress classification models based on EEG, ECG, and other types of data. Blood Volume Pulse (BVP), skin temperature (TEMP), accelerometer (ACC), Convolutional Neural Networks (CNN),. 

Principal Component Analysis (PCA) was applied to reduce feature dimensionality and manage multicollinearity among HRV metrics. The analysis revealed that features such as pNN50, NN50, SDNN, and AVNN loaded heavily onto the first principal component, indicating high redundancy. TAR and LF/HF also contributed uniquely, justifying their inclusion in the final fused feature set. This dimensionality reduction improved the classifier efficiency without significant loss of performance. 

The statistical tests supported the discriminative validity of the selected features. The Shapiro-Wilk test confirmed non-normality for several features (e.g., TAR and LF/HF), justifying the use of non-parametric Kruskal-Wallis tests, which revealed significant differences across task segments ( _p_ <.001). The effect size (Rank ε²) further confirmed meaningful differences in feature distributions, particularly for TAR and LF/HF, supporting their relevance in classifying stress. 

Among all classifiers, the Support Vector Machine (SVM) consistently outperformed the others, showing robustness in both unimodal and multimodal contexts. Linear discriminants (LD) also performed well, especially in multiclass settings, whereas KNN, DT, and RF showed greater variability, likely because of their sensitivity to class imbalance and noise. Naïve Bayes (NB) performed adequately but was outpaced by SVM and LD, particularly in high-stress scenarios. 

Importantly, the proposed framework is computationally efficient and streamlined; by utilizing only three physiologically derived features (TAR, HR, and LF/HF), the model avoids the complexity and high dimensionality often associated with raw EEG or deep learning-based approaches. Classical machine learning classifiers, particularly SVM and LD, achieved high accuracy without the need for extensive signal processing or large amounts of computational resources. This positions the model as a suitable candidate for real-time cognitive stress monitoring systems, particularly in resource-constrained or wearable settings. 

The high accuracy of the multimodal SVM classifier suggests a strong potential for real-time adaptive cognitive stress monitoring systems, particularly in high-stakes environments such as aviation, education, and human-computer interaction. Gender-specific performance differences further highlight the importance of tailoring these systems to individual physiological baselines. 

Although the results are promising, several limitations must be noted. First, the dataset was limited to a controlled experimental setting, and used only arithmetic tasks (MIST) to induce stress, which may not be generalizable to real-world cognitive stress scenarios. Additionally, the sample size, particularly the imbalance gender subgroups can bias classification, may constrain generalizability. Future work should explore longitudinal, real-world data collection and expand to other physiological modalities (e.g., eye-tracking and galvanic skin response). 

Moreover, future studies should investigate deep learning models, temporal dynamics (e.g., time-series modeling), and real-world stress classification. Gender-aware modeling techniques can further improve the performance and fairness of cognitive stress prediction. 

**Scientific Reports** |         (2026) 16:7304 

19 

| https://doi.org/10.1038/s41598-026-38356-3 

www.nature.com/scientificreports/ 

## **Conclusion** 

This study proposed the development of a gender-sensitive, multimodal system of cognitive stress, based on the combination of EEG (Theta/Alpha Ratio) and ECG (Heart Rate and LF/HF Ratio) features obtained using sophisticated machine learning methods. A statistical analysis followed by dimensionality reduction and model assessment using the suggested methodology showed that multimodal feature fusion is a much more effective way to discriminate between cognitive stress than using unimodal approaches. Support Vector Machine (SVM) performed better, with the highest accuracy of 94.7% and an F1-score of 94.3% in the rest versus cognitive stress classification. Principal Component Analysis (PCA) proved that feature duplication existed and assisted in reducing the dimensionality, which aided in model stability. The Shapiro-Wilk and Kruskal-Wallis statistical tests also proved that the distribution was not normal and that the features chosen, that is TAR and LF/HF were discriminative. 

Moreover, gender-based analysis exhibited some interesting physiological differences in the cognitive stress responses, whereby the performance of the female participants was higher in some conditions. These findings highlight the necessity of developing individual-specific and gender-conscious cognitive surveillance systems. In addition to its performance in classification, the proposed framework is based on a few highly informative features and universal machine learning models. This not only saves computational resources but also ensures high prediction quality, so the method can be applied in practical settings with real-time constraints in the form of portable or embedded devices. 

Ultimately, this study offers a framework that includes a validated, machine learning-based, real-time multimodal system for assessing cognitive stress. It provides the basis for the building of adaptive systems in fields such as education, neuroergonomics, and human-computer interaction. The future study is expected to extend the dataset, involve more biosignals, investigate deep learning framework, and apply the framework to real-life circumstances to improve its generalizability and implementations. 

## **Data availability** 

The publicly available datasets used in the current study can be found at  [ h t t p s : / / d a t a . m e n d e l e y . c o m / d a t a s e t s / c y h c h p x w p s / 2 ] ( h t t p s : / d a t a . m e n d e l e y . c o m / d a t a s e t s / c y h c h p x w p s / 2 ) . 

Received: 11 October 2025; Accepted: 29 January 2026 



## **References** 

1. Hemakom, A., Atiwiwat, D. & Israsena, P. ECG and EEG based detection and multilevel classification of stress using machine learning for specified genders: A preliminary study. _Plos One_ **18** , e0291070 (2023). 

2. Hemakom, A., Atiwiwat, D. & Israsena, P. Ecg and Eeg based machine learning models for the classification of mental workload and stress levels for women in different menstrual phases, men, and mixed sexes. _Biomed. Signal Process. Control_ . **95** , 106379 (2024). 

3. Seo, S. H., Lee, J. T. & Crisan, M. Stress and EEG, Convergence and hybrid information technologies, vol. 27, pp. 413–424, (2010). 

4. Saffari, F., Norouzi, K., Bruni, L. E., Zarei, S. & Ramsøy, T. Z. Impact of varying levels of mental stress on phase information of EEG signals: A study on the Frontal, Central, and parietal regions. _Biomed. Signal Process. Control_ . **86** , 105236 (2023). 

5. Arsalan, A., Majid, M., Butt, A. R. & Anwar, S. M. Classification of perceived mental stress using a commercially available EEG headband. _IEEE J. Biomedical Health Inf._ **23** , 2257–2264 (2019). 

6. AlShorman, O. et al. Frontal lobe real-time EEG analysis using machine learning techniques for mental stress detection. _J. Integr. Neurosci._ **21** , 20 (2022). 

7. Raufi, B. & Longo, L. An evaluation of the EEG alpha-to-theta and theta-to-alpha band ratios as indexes of mental workload. _Front. Neuroinformatics_ . **16** , 861967 (2022). 

8. Alshanskaia, E. I., Zhozhikashvili, N. A., Polikanova, I. S. & Martynova, O. V. Heart rate response to cognitive load as a marker of depression and increased anxiety. _Front. Psychiatry_ . **15** , 1355846 (2024). 

9. Kim, H. G., Cheon, E. J., Bai, D. S., Lee, Y. H. & Koo, B. H. Stress and heart rate variability: a meta-analysis and review of the literature. _Psychiatry Invest._ **15** , 235 (2018). 

10. da Silva, A. G. C. B. et al. Increase in perceived stress is correlated to lower heart rate variability in healthy young subjects. _Acta Scientiarum Health Sci._ **37** , 7 (2015). 

11. Järvelin-Pasanen, S., Sinikallio, S. & Tarvainen, M. P. Heart rate variability and occupational stress—systematic review. _Ind. Health_ **56** , 500–511 (2018). 

12. Wulsin, L., Herman, J. & Thayer, J. F. Stress, autonomic imbalance, and the prediction of metabolic risk: a model and a proposal for research. _Neurosci. Biobehavioral Reviews_ . **86** , 12–20 (2018). 

13. Sun, M. & Cao, X. A mental stress classification method based on feature fusion using physiological signals. _J. Circuits Syst. Computers_ . **33** , 2450016 (2024). 

14. Dogan, G. & Akbulut, F. P. Multi-modal fusion learning through biosignal, audio, and visual content for detection of mental stress. _Neural Comput. Appl._ **35** , 24435–24454 (2023). 

15. Song, C. H., Kim, J. S., Kim, J. M. & Pan, S. Stress classification using ECGs based on a Multi-dimensional feature fusion of LSTM and Xception. _IEEE Access._ **12** , 19077–19086 (2024). 

16. Wriessnegger, S., Leitner, M. & Kostoglou, K. The brain under pressure: Exploring neurophysiological responses to cognitive stress, Brain and Cognition, vol. 182, p. 106239, (2024). 

17. Badr, Y. et al. A review on evaluating mental stress by deep learning using EEG signals. _Neural Comput. Appl._ **36** , 12629–12654 (2024). 

18. Behradfar, M., Roy, S. & Nuamah, J. Optimizing Mental Stress Detection via Heart Rate Variability Feature Selection, Sensors, vol. 25, p. 4154, (2025). 

19. Immanuel, S., Teferra, M. N., Baumert, M. & Bidargaddi, N. Heart rate variability for evaluating psychological stress changes in healthy adults: a scoping review. _Neuropsychobiology_ **82** , 187–202 (2023). 

20. Xiong, R., Kong, F., Yang, X., Liu, G. & Wen, W. Pattern recognition of cognitive load using EEG and ECG signals. _Sensors_ **20** ,  5122 (2020). 

21. Ahn, J. W., Ku, Y. & Kim, H. C. A Novel Wearable EEG and ECG Recording System for Stress Assessment, Sensors, vol. 19, p. 2019. (1991). 

**Scientific Reports** |         (2026) 16:7304 | https://doi.org/10.1038/s41598-026-38356-3 

20 

www.nature.com/scientificreports/ 

22. Nuamah, J. K., Seong, Y. & Yi, S. Electroencephalography (EEG) classification of cognitive tasks based on task engagement index, in IEEE Conference on Cognitive and Computational Aspects of Situation Management (CogSIMA), 2017, pp. 1–6. (2017). 

23. Billones, R. K. C. et al. Cardiac and brain activity correlation analysis using electrocardiogram and electroencephalogram signals, in 2018 IEEE 10th International Conference on Humanoid, Nanotechnology, Information Technology, Communication and Control, Environment and Management (HNICEM), pp. 1–6. (2018). 

24. Forte, G. & Casagrande, M. The intricate brain–heart connection: the relationship between heart rate variability and cognitive functioning. _Neuroscience_ **565** , 369–376 (2025). 

25. Amancharla, A. & Shanbhag, A. A. Analysis of EEG and ECG time series in response to olfactory and cognitive tasks. _Procedia Comput. Sci._ **235** , 745–756 (2024). 

26. Rudics, E. et al. Quantifying Stress and Relaxation: A New Measure of Heart Rate Variability as a Reliable Biomarker, Biomedicines, vol. 13, p. 81, (2025). 

27. Belle, A., Hargraves, R. H. & Najarian, K. An automated optimal engagement and attention detection system using electrocardiogram, Computational and mathematical methods in medicine, vol. p. 528781, 2012. (2012). 

28. Jha, A., Bhattarai, B., Kunwar, B. B., & Pant, S. Time and frequency domain analysis of heart rate variability (HRV) in response to cold stress in subjects with family history of hypertension. _Int. J. Health Sci. Res._ **8** (3), 226–231 (2018). 

29. S. N., Abdulkader, A., Atia & Mostafa, M. S. M. Brain computer interfacing: applications and challenges. _Egypt. Inf. J._ **16** , 213–230 (2015). 

30. Zhong, H. et al. Reorganization of brain functional network during task switching before and after mental fatigue. _Sensors_ **22** , 8036 (2022). 

31. Kumar, A., Ram, L., Sharma, R., Pandey, T. & Saxena, P. Electroencephalograms (EEG) During Mental Arithmetic Task Performance. 

32. Manshouri, N., Melek, M. & Kayıkcıoglu, T. Detection of 2D and 3D video transitions based on EEG power. _Comput. J._ **65** , 396–409 (2022). 

33. E. T. & Attar Review of electroencephalography signals approaches for mental stress assessment. _Neurosciences J._ **27** , 209–215 (2022). 

34. T. Y., Wen & Aris, S. M. Electroencephalogram (EEG) stress analysis on alpha/beta ratio and theta/beta ratio, Indones. _J. Electr. Eng. Comput. Sci._ **17** , 175–182 (2020). 

35. Roy, S., Islam, M., Yusuf, M. S. U. & Jahan, N. EEG based stress analysis using rhythm specific spectral feature for video game play. _Comput. Biol. Med._ **148** , 105849 (2022). 

36. Trammell, J. P., MacRae, P. G., Davis, G., Bergstedt, D. & Anderson, A. E. The relationship of cognitive performance and the thetaalpha power ratio is age-dependent: an EEG study of short term memory and reasoning during task and resting-state in healthy young and old adults. _Front. Aging Neurosci._ **9** , 364 (2017). 

37. Yu, S. et al. Cross-task cognitive load based on EEG multidomain feature fusion. _Experimental Technol. Manage._ **41** , 73–80 (2024). 

38. Canova, G. Machine learning and data fusion of physiological signals for assessing a subject’s stress level and cognitive load. _Politecnico Di Torino_ (Master Thesis, 2024). 

39. Awasthi, K., Nanda, P. & Suma, K. Performance analysis of Machine Learning techniques for classification of stress levels using PPG signals, in 2020 IEEE International Conference on Electronics, Computing and Communication Technologies (CONECCT), pp. 1–6. (2020). 

40. Debie, E. et al. Multimodal fusion for objective assessment of cognitive workload: A review. _IEEE Trans. Cybernetics_ . **51** , 1542– 1555 (2019). 

41. Hag, A. et al. Enhancing EEG-based mental stress state recognition using an improved hybrid feature selection algorithm. _Sensors_ **21** , 8370 (2021). 

42. Wang, C. et al. A Framework for Cognitive Load Recognition Based on Machine Learning and Multimodal Physiological Signals by Wearable Sensors, in 2023 IEEE 4th International Conference on Pattern Recognition and Machine Learning (PRML), pp. 299–306. (2023). 

43. Arsalan, A. et al. Human stress assessment: A comprehensive review of methods using wearable sensors and non-wearable techniques. arXiv:2202.03033 (2022). 

44. Bhateja, V., Gupta, A., Mishra, A. & Mishra, A. Artificial neural networks based fusion and classification of EEG/EOG signals, in Information Systems Design and Intelligent Applications: Proceedings of Fifth International Conference INDIA Volume 2, 2019, pp. 141–148. (2018). 

45. Zhou, B., Wang, L. & Jiang, C. Psychological Stress Classification Using EEG and ECG: A CNN Based Multimodal Fusion Model, (2024). 

46. Kesedžić, I., Šarlija, M., Božek, J., Popović, S. & Ćosić, K. Classification of cognitive load based on neurophysiological features from functional near-infrared spectroscopy and electrocardiography signals on n-back task. _IEEE Sens. J._ **21** , 14131–14140 (2020). 

47. Bodaghi, M., Hosseini, M. & Gottumukkala, R. A multimodal intermediate fusion network with manifold learning for stress detection, in 2024 IEEE 3rd International Conference on Computing and Machine Intelligence (ICMI), pp. 1–8. (2024). 

48. Wali, M. K., Fayadh, R. A. & Al_shamaa, N. K. Electroencephalogram based stress detection using extreme learning machine. _Nano Biomed. Eng._ **14** , 208–215 (2022). 

49. Klimesch, W. EEG alpha and theta oscillations reflect cognitive and memory performance: a review and analysis. _Brain Res. Rev._ **29** , 169–195 (1999). 

50. Sammer, G. et al. Relationship between regional hemodynamic activity and simultaneously recorded EEG-theta associated with mental arithmetic‐induced workload. _Hum. Brain. Mapp._ **28** , 793–803 (2007). 

51. Manshouri, N., Maleki, M. & Kayıkçıoğlu, T. Classification of human vision discrepancy during watching 2D and 3D movies based on EEG signals. _Int. J. Comput. Sci. Inform. Secur._ **15** , 430–436 (2017). 

52. Manshouri, N. & Kayıkçıoğlu, T. Classification of 2D and 3D videos based on EEG waves, in 2016 24th Signal Processing and Communication Application Conference (SIU), pp. 949–952. (2016). 

53. Attar, E. T., Balasubramanian, V., Subasi, E. & Kaya, M. Stress analysis based on simultaneous heart rate variability and EEG monitoring. _IEEE J. Translational Eng. Health Med._ **9** , 1–7 (2021). 

54. Wang, L., Song, F., Zhou, T. H., Hao, J. & Ryu, K. H. EEG and ECG-based multi-sensor fusion computing for real-time fatigue driving recognition based on feedback mechanism. _Sensors_ **23** ,  8386 (2023). 

55. Saha, P. et al. Novel multimodal emotion detection method using electroencephalogram and electrocardiogram signals. _Biomed. Signal Process. Control_ . **92** , 106002 (2024). 

56. Hemakom, A. A., Israsena, D. & Pasin _ECG & EEG Features for Mental Workload and Multilevel Stress Classification in Different sexes, V2 Ed_ (Mendeley Data, 2024). 

57. Wongpakaran, N. & Wongpakaran, T. The Thai version of the PSS-10: An Investigation of its psychometric properties, BioPsychoSocial medicine, vol. **4** , p. 6, (2010). 

58. Dedovic, K. et al. The Montreal imaging stress task: using functional imaging to investigate the effects of perceiving and processing psychosocial stress in the human brain. _J. Psychiatry Neurosci._ **30** , 319–325 (2005). 

59. Pruessner, J. C. et al. Stress regulation in the central nervous system: evidence from structural and functional neuroimaging studies in human populations-2008 Curt Richter award Winner. _Psychoneuroendocrinology_ **35** , 179–191 (2010). 

60. Cabañero, L. et al. Analysis of cognitive load using EEG when interacting with mobile devices, in Proceedings, p. 70. (2019). 

**Scientific Reports** |         (2026) 16:7304 

21 

| https://doi.org/10.1038/s41598-026-38356-3 

www.nature.com/scientificreports/ 

61. Holm, A., Lukander, K., Korpela, J., Sallinen, M. & Müller, K. M. Estimating brain load from the EEG. _Sci. World J._ **9** , 639–651 (2009). 

62. Melek, N. Comparison of EEG and EOG signals in classification of sleep stages. _Pamukkale Üniversitesi Mühendislik Bilimleri Dergisi_ . **29** , 607–616 (2023). 

63. Apicella, A., Isgrò, F., Pollastro, A. & Prevete, R. On the effects of data normalization for domain adaptation on EEG data. _Eng. Appl. Artif. Intell._ **123** , 106205 (2023). 

64. Das, A., Singh, S., Kim, J., Ahanger, T. A. & Pise, A. A. Enhanced EEG signal classification in brain computer interfaces using hybrid deep learning models, Scientific Reports, vol. **15** , p. 27161, (2025). 

65. Kwak, Y., Kong, K., Song, W. J., Min, B. K. & Kim, S. E. Multilevel feature fusion with 3d convolutional neural network for eegbased workload Estimation. _IEEE access._ **8** , 16009–16021 (2020). 

66. Kuttala, R., Subramanian, R. & Oruganti, V. R. M. Multimodal hierarchical CNN feature fusion for stress detection. _IEEe Access._ **11** , 6867–6878 (2023). 

67. Dong, Y. et al. A Hybrid EEG-Based Stress State Classification Model Using Multi-Domain Transfer Entropy and PCANet, Brain Sciences, vol. **14** , p. 595, (2024). 

68. Chikhi, S., Matton, N. & Blanchet, S. EEG power spectral measures of cognitive workload: A meta-analysis, Psychophysiology, vol. **59** , p. e14009, (2022). 

## **Author contributions** 

A.S. conceived the study, designed the methodology, conducted the formal analysis, and wrote the main manuscript text. F.A. and S.U.R. supervised the research, provided resources, and reviewed & edited the manuscript. D.S. contributed to software development, validation, and manuscript review. S.A. assisted with data curation, software development, and formal analysis. M.T. contributed to the investigation and manuscript review. All authors reviewed the manuscript. 

## **Funding** 

The authors have received no specific funding for this study. 

## **Declarations** 

## **Competing interests** 

The authors declare no competing interests. 

## **Additional information** 

**Correspondence** and requests for materials should be addressed to D.S. or M.T. 

**Reprints and permissions information** is available at www.nature.com/reprints. 

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

**Open Access** This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p : / / c r e a t i v e c o m m o n s . o r g / l i c e n s e s / b y - n c - n d / 4 . 0 / . 

© The Author(s) 2026 

**Scientific Reports** |         (2026) 16:7304 

22 

| https://doi.org/10.1038/s41598-026-38356-3 

