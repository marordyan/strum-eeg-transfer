

### _Article_ 

# **A Machine Learning Approach for Real-Time Detection of Inadequate Sedation Using Non-EEG Physiological Signals** 

**Huiquan Wang**<sup>**1,†**</sup> **, Chunliang Jiang**<sup>**1,2,†**</sup> **, Guanjun Liu**<sup>**2**</sup> **, Jing Yuan**<sup>**2**</sup> **, Ming Yu**<sup>**2**</sup> **, Xin Ma**<sup>**1**</sup> **, Chong Liu**<sup>**3**</sup> **, Jingyu Xiao**<sup>**4**</sup> **and Guang Zhang**<sup>**2,**</sup> ***** 

- 1 School of Control Science and Engineering, Tiangong University, Tianjin 300387, China; huiquan85@126.com (H.W.); chunliang95@foxmail.com (C.J.); maxin2009@tiangong.edu.cn (X.M.) 

- 2 Systems Engineering Institute, Academy of Military Sciences, People’s Liberation Army, Tianjin 300161, China; guan_jun0502@163.com (G.L.); yuanjingjy@163.com (J.Y.); yuming381@sina.com (M.Y.) 

- 3 Department of Anaesthesiology, Tianjin 4th Centre Hospital, The Fourth Center Clinical College of Tianjin Medical University, Tianjin 300140, China; lchong88@163.com 

- 4 Department of Anesthesiology, Chongqing University Cancer Hospital, Chongqing 400030, China; jyxiao1989@cqu.edu.cn 

- Correspondence: zhangguang01@hotmail.com 

- These authors contributed equally to this work. 

### **Abstract** 

Academic Editor: Kwang Woo Ahn 

Received: 24 August 2025 Revised: 22 September 2025 Accepted: 26 September 2025 Published: 29 September 2025 

**Citation:** Wang, H.; Jiang, C.; Liu, G.; Yuan, J.; Yu, M.; Ma, X.; Liu, C.; Xiao, J.; Zhang, G. A Machine Learning Approach for Real-Time Detection of Inadequate Sedation Using Non-EEG Physiological Signals. _Bioengineering_ **2025** , _12_ , 1049. https://doi.org/ 10.3390/bioengineering12101049 

**Copyright:** © 2025 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/ licenses/by/4.0/). 

Sedation is an essential component of the anesthesia process. Inadequate sedation during anesthesia increases the risk of patient discomfort, intraoperative awareness, and psychological trauma. Conventional electroencephalography (EEG) based depth of anesthesia monitoring is often impractical in out-of-hospital settings due to equipment limitations and signal artifacts. Alternative non-EEG-based approaches are therefore required. In this study, we developed a machine learning model to detect inadequate sedation using 27 feature parameters, including demographics, vital signs, and heart rate variability metrics, from the open-access VitalDB database. Patient states were defined as inadequate sedation when the bispectral index (BIS) > 60. We systematically evaluated four temporal windows and four algorithms, and assessed model interpretability using Shapley Additive Explanations (SHAP). The Light Gradient Boosting Machine (LGBM) achieved the best performance, with an area under the receiver operating characteristic curve (AUC) of 0.825 and an accuracy (ACC) of 0.741 using a 2 s time window. Extending the time window to 20 s improved both metrics by approximately 0.012. Feature selection identified 12 key parameters that maintained comparable accuracy, confirming robustness with reduced complexity. These findings demonstrate the feasibility of using non-EEG-based physiological data for real-time detection of inadequate sedation. The developed model is interpretable, resource-efficient, scalable, and shows strong potential for integration into portable monitoring systems in prehospital, emergency, and low-resource surgical settings. 

**Keywords:** inadequate sedation; bispectral index; non-EEG physiological signals; machine learning; out-of-hospital 

## **1. Introduction** 

Inadequate sedation during anesthesia poses significant risks, including patient discomfort, intraoperative awareness, and psychological trauma. Timely identification of this state is therefore essential for patient safety, as early detection can reduce adverse outcomes such as pain perception, stress responses, and postoperative complications [1]. 

https://doi.org/10.3390/bioengineering12101049 

_Bioengineering_ **2025** , _12_ , 1049 

_Bioengineering_ **2025** , _12_ , 1049 

2 of 15 

In clinical practice, anesthetic depth is typically monitored using physiological parameters such as heart rate (HR), blood pressure (BP), and end-tidal carbon dioxide (ETCO2), in combination with neurophysiological measures, most notably the bispectral index (BIS) derived from electroencephalography (EEG) [2–4]. BIS is widely regarded as a reference standard, with values above 60 generally indicating inadequate sedation [5,6]. However, EEG-based monitoring is often infeasible in out-of-hospital or resource-limited environments (e.g., emergency transport, battlefield care) due to high cost, specialized equipment requirements, motion artifacts, and electromagnetic interference [7,8]. These limitations underscore the need for reliable, real-time, non-EEG-based approaches to detect inadequate sedation. 

Recent advances in machine learning (ML) and biomedical signal processing have facilitated the use of non-EEG physiological signals such as electrocardiogram (ECG), photoplethysmography (PPG), and heart rate variability (HRV) as surrogate indicators of anesthetic depth. For instance, Chowdhury et al. applied deep learning algorithms to ECG and PPG derived heatmaps, achieving an accuracy (ACC) of 86% in anesthetic state classification [9]. Gang et al. demonstrated the potential of cerebral hemodynamic features as correlates of BIS values [10]. Zhan et al. utilized HRV-derived features with deep neural networks to classify anesthesia depth, while Yin et al. employed long shortterm memory models to distinguish consciousness from general anesthesia with high accuracy [11,12]. Moreover, previous studies using the VitalDB database, such as the datadriven investigation of the BIS algorithm by Lee et al., relied on multiple EEG-derived subparameters and complex regression models [7]. 

Although these studies highlight the feasibility of non-EEG-based monitoring, most efforts have focused on differentiating between deep anesthesia and full consciousness. In contrast, the clinically critical intermediate state of inadequate sedation has received limited attention. This gap is especially concerning in non-operating-room environments, where unrecognized awakening can have severe consequences and EEG based monitoring is often unavailable. 

To address this challenge, the present study proposes a machine learning based framework for real-time detection of inadequate sedation using multi-source, non-invasive physiological signals. Leveraging the large-scale VitalDB database, we extracted 27 features including demographics, conventional vital signs, and HRV metrics. Four machine learning classifiers were systematically evaluated across multiple temporal windows, and model interpretability was assessed using Shapley Additive Explanations (SHAP) [13–16]. This study provides a scalable, interpretable, and resource-efficient solution for sedation monitoring in prehospital, emergency, and other resource-constrained settings. 

## **2. Methods** 

As shown in Figure 1A, the conceptual framework of this study consists of four major components: source of dataset, raw data acquisition, decision making based on multiparameter features, and identification of inadequate sedation. Building on this framework, Figure 1B further illustrates the detailed workflow for detecting inadequate sedation using non-EEG physiological signals: 

1. Data integration: Data from multiple time dimensions and heterogeneous sources are integrated into a unified feature set. 

2. Data preprocessing: Signals were denoised, HRV features extracted, missing values imputed, and categorical variables encoded. 

3. Data split: Data were split into training (80%) and testing (20%) sets. 

4. Model construction: ML classifiers were trained to classify patients as inadequately or adequately sedated using non-EEG features [17,18]. 

_Bioengineering_ **2025** , _12_ , 1049 

3 of 15 

5. Model tuning: Hyperparameters were optimized with 10-fold cross-validation. 

6. Evaluation metrics: Models were evaluated on the test set using standard performance measures. 

7. Interpretability analysis: SHAP was applied to quantify feature contributions and enhance clinical interpretability. 



**Figure 1.** Conceptual framework and workflow of the proposed machine learning approach for detecting inadequate sedation using non-EEG physiological signals. ( **A** ) shows the conceptual framework comprising four components: source of dataset, raw data acquisition, decision making based on multi-parameter features, and identification of inadequate sedation. ( **B** ) illustrates the detailed workflow, including data preprocessing, feature extraction, model training and validation, and interpretability analysis using SHAP. 

### _2.1. Source of Data_ 

This retrospective observational study followed the Transparent Reporting of a Multivariable Prediction Model for Individual Prognosis or Diagnosis (TRIPOD) guidelines. Data were obtained from the publicly available VitalDB database (http://vitaldb.net/, accessed on 15 March 2023), which contains high-resolution intraoperative physiological waveforms and clinical records. VitalDB was developed to support artificial intelligence research in perioperative medicine and anesthesia. The database includes 486 intraoperative monitoring parameters, 73 perioperative clinical variables, and 34 time-series laboratory parameters collected from 6388 surgical patients at a single tertiary medical center. Among these, 5543 patients had BIS monitoring records available and were considered for inclusion in this study on inadequate sedation detection [19,20]. 

### _2.2. Participants and Eligibility Criteria_ 

Based on established clinical literature and to ensure population consistency, this study focused on a relatively healthy adult surgical cohort for developing a machine learning model to detect inadequate sedation [21,22]. 

Inclusion criteria: 

_Bioengineering_ **2025** , _12_ , 1049 

4 of 15 

- Age between 18 and 65 years; 

- American Society of Anesthesiologists (ASA) physical status classification I–III; 

- _•_ Body mass index (BMI) > 18 kg/m<sup>2</sup> and _≤_ 30 kg/m<sup>2</sup> ; 

- Undergoing elective surgery with a minimum duration of 2 h; 

- Receiving total intravenous anesthesia (TIVA) as the primary anesthetic technique. Exclusion criteria: 

- Cranial neurosurgery: Procedures involving the central nervous system were excluded due to potential EEG signal interference and BIS distortion. 

- Transplantation or cardiopulmonary bypass: These cases were excluded because of significant and frequent hemodynamic fluctuations that could confound physiological signal interpretation. 

- Incomplete data: Patients lacking synchronized ECG, PPG, and BIS waveform data, or exhibiting substantial waveform loss after extraction, were excluded. 

After applying these criteria, 5366 patients were excluded, yielding a final study cohort of 1022 patients. This cohort was used for model training, validation, and analysis. To avoid potential data leakage, train/test splitting was performed at the patient ID level, with 80% of patients allocated to the training set and 20% to the test set. The detailed screening process is illustrated in Figure 2. 



<!-- Start of picture text -->
6388 patients monitored using BIS in the VitalDB database<br>Excluded 2223 patients who were younger than<br>18 or older than 65 years old<br>Excluded 125 patients with an ASA<br>classification greater than III<br>Excluded 400 patients with a BMI ≤ 18 kg/m² or<br>≥ 30 kg/m²<br>Excluded 1769 patients with a surgery duration<br>of less than 2 hours<br>Excluded 283 patients who underwent<br>craniocerebral neurosurgery, transplantation,<br>and establishment of cardiopulmonary bypass<br>Excluded 9 patients who underwent non-<br>general anesthesia surgeries<br>Excluded 557 patients who did not have<br>simultaneous BIS, ECG, and PPG waveform<br>data, or had missing data after download.<br>1022 patients undergoing general anesthesia with BIS monitoring<br>included in the study<br><!-- End of picture text -->

**Figure 2.** Cohort selection process. 

### _2.3. Outcome Definition and Predictors_ 

The primary objective of this study was to develop a model for detecting inadequate sedation during anesthesia using non-invasive physiological monitoring data. In clinical practice, BIS is widely used as a surrogate for anesthetic depth, and values above 60 are commonly referenced in guidelines and clinical studies as indicating insufficient sedation, associated with an increased risk of intraoperative awareness, patient movement, or hemo- 

_Bioengineering_ **2025** , _12_ , 1049 

5 of 15 

dynamic instability [5–7,9]. Given the retrospective nature of the dataset, which did not include postoperative interviews to confirm awareness, BIS thresholds were adopted as the operational definition in this study. 

Accordingly, binary outcome labels were assigned as follows: inadequate sedation was defined as a BIS value > 60, whereas adequate anesthesia was defined as BIS _≤_ 60 [17,18]. 

This dichotomy reflects a clinically relevant classification consistent with perioperative monitoring practice, particularly valuable in environments where EEG-based systems are not feasible. A total of 27 feature parameters were extracted for analysis (Table 1), with HRV parameter definitions provided in Supplementary Materials (Table S1). These features were derived from the Parameter List of the VitalDB database and accessed through different API views: Clinical Information, Track list, and Data track. 

**Table 1.** The 27 feature parameters extracted from the VitalDB database. 

|**Dataset Composition**|**Detailed Parameters**|**Data Source**|
|---|---|---|
|Basic Patient Information|Age, Gender, ASA, BMI|Clinical Information|
|Conventional Physiological Parameters<br>Heart Rate Variability Parameters|HR, DBP, MBP, SBP, SPO2, ETCO2<br>HRV_Mean, HRV_SDNN, HRV_RMSSD,<br>HRV_SDSD, HRV_CVNN, HRV_HF, HRV_HFn,<br>HRV_pNN50, HRV_pNN20, HRV_LnHF,<br>HRV_SD1,HRV_SD2, HRV_SD1SD2, HRV_S,<br>HRV_ShanEn, HRV_ApEn, HRV_CVSD|Data track<br>Derived from ECG (Track<br>list) after preprocessing|



### _2.4. Data Preprocessing and Handling of Missing Data_ 

Dynamic time window: Physiological parameters inherently exhibit temporal continuity. To capture this dynamic information, a time windowing approach was implemented. The construction of the dynamic window was designed to approximate the calculation principle of BIS, thereby enabling the model to incorporate short-term physiological variability. Detailed definitions and the implementation process are provided in Figure 3. 



**Figure 3.** Dynamic time window. Construction of a 6 s sliding window, where T0 represents the initial time point for collecting the patient’s physiological data; Tn denotes the sampling moments during the patient’s anesthesia process, with a sampling interval of 2 s; and Dn represents the length of the constructed dynamic time window. 

Heart rate variability calculation: HRV features were computed from 30 s ECG segments after noise reduction and artifact correction, both performed using NeuroKit2, and included time-domain indices, frequency-domain measures, and nonlinear metrics in accordance with established HRV analysis protocols [23]. 

Missing value handling: The overall missing rate of the extracted physiological monitoring data was less than 10%, ensuring sufficient data completeness. To maintain consistency with real-world clinical monitoring and minimize potential imputation bias, 

_Bioengineering_ **2025** , _12_ , 1049 

6 of 15 

mean imputation was applied only to continuous physiological parameters with missing values. No imputation was necessary for categorical variables, as these were complete in the final cohort. The detailed missing rates for each parameter are provided in the Supplementary Materials (Table S2). Supplementary Materials (Figure S1) presents violin plots of the 23 parameters, illustrating the data after preprocessing. 

One-hot encoding of categorical variables: Categorical variables were encoded as binary vectors using one-hot encoding [24]. In this study, gender was the only categorical variable, encoded as 1 for male and 0 for female. 

Feature standardization: To ensure comparability across features with different units and scales, all continuous variables were standardized using z-score normalization. Each feature was transformed by subtracting the mean and dividing by the standard deviation, based on the training set distribution [25]. 

Feature dimensionality across different time windows: Temporal features, defined as conventional physiological parameters and HRV metrics extracted from ECG signals, together with demographic variables, constituted the feature set for model input. The input dimensionality increased with window length: 27 features for 2 s, 142 for 6 s, 234 for 10 s, and 464 for 20 s. Details of the feature composition are provided in the Supplementary Materials (Table S3). 

### _2.5. Model Development_ 

Four ML algorithms were tested for real-time identification of patients with inadequate sedation: Random Forest (RF) [26], Light Gradient Boosting Machine (LGBM) [27], Logistic Regression (LR) [28], and Naïve Bayes (NB) [29]. These methods were chosen to represent diverse methodological families, including decision tree ensembles, gradient boosting, regression-based classification, and probabilistic modeling. Model parameters were optimized on the training set using 10-fold cross-validation, with the learning rate adjusted during cross-validation and kept constant throughout the entire training process. 

### _2.6. Model Performance and Validation_ 

The performance of the machine learning models was evaluated using multiple standard metrics, including accuracy (ACC), area under the receiver operating characteristic curve (AUC), sensitivity (SEN), specificity (SPE), Bayesian error rate (BER), Matthews correlation coefficient (MCC), F1-score, Cohen’s kappa coefficient (KAPPA), and confidence interval (CI). 

### _2.7. Feature Selection Using Recursive Elimination_ 

Recursive feature elimination with cross-validation (RFECV) was used to balance model complexity and predictive performance. Less informative features were iteratively removed to obtain a parsimonious subset of predictors, thereby enhancing both ACC and interpretability. This process reduced dimensionality by eliminating irrelevant or redundant variables without compromising recognition performance [30,31]. The optimal feature subset (OPT_subset) was defined as the configuration yielding the lowest average Bayesian error rate (BER), while the minimum feature subset (MIN_subset) corresponded to the smallest number of features within one standard deviation of the BER in the OPT_subset [32]. 

### _2.8. Model Explainability Analysis_ 

To enhance interpretability, we applied SHapley Additive exPlanations (SHAP), an explainable AI approach grounded in cooperative game theory, to quantify the marginal contribution of each predictor to the model outputs. SHAP provided consistent and additive attributions and, for the tree-based models used in this study (LGBM), allowed efficient 

_Bioengineering_ **2025** , _12_ , 1049 

7 of 15 

computation through the TreeExplainer framework. The method enabled both global interpretation, by summarizing the average impact of features across the dataset, and local interpretation, by illustrating how specific features influenced predictions for individual patients. From a technical perspective, SHAP offered intuitive visualizations that linked changes in physiological parameters to predicted sedation states. Compared with alternative interpretability techniques, SHAP yielded theoretically consistent attributions with high local fidelity, thereby improving transparency, supporting clinical decision-making, and facilitating potential translation of the model into real-world anesthetic monitoring. 

### _2.9. Software and Reproducibility_ 

All data preprocessing, feature selection, model training, and interpretability analyses were conducted in Python 3.9 using open-source packages, including scikit-learn, LGBM, SHAP, pandas, and NumPy. The computational workflow was implemented in a Jupyter Notebook 6.5 environment. Source data were stored in and queried from a PostgreSQL 15.3 database, which enabled efficient data extraction and timewindow alignment from the VitalDB relational database. The detailed pseudocode for real-time detection of inadequate sedation using non-EEG signals is presented in the Supplementary Materials (Algorithm S1). 

## **3. Results** 

### _3.1. Baseline Characteristics of Included Patients_ 

The baseline characteristics of the included patients are summarized in the Supplementary Materials (Table S4). No statistically significant differences were observed between the training and test datasets, which were randomly divided. Comparisons between the two datasets were performed using the chi-square test or F-test. 

### _3.2. Comparison of Various ML Approaches_ 

Table 2 and Figure 4 summarize the performance of the four ML models across all time windows (2, 6, 10, and 20 s). Among the algorithms evaluated, LGBM consistently achieved the best classification performance, with higher AUC and ACC values than RF, LR, and NB at each window length. Using a 2 s time window, LGBM reached an AUC of 0.825 (95% CI [0.823–0.826]) and an ACC of 0.741 (95% CI [0.740–0.742]), outperforming the other models under identical conditions. From a clinical perspective, minimizing false negatives is critical to avoid unrecognized inadequate sedation. To reflect this requirement, model performance was further evaluated under a fixed sensitivity of 90%. Under this conservative setting, LGBM again outperformed the other algorithms, achieving an ACC of 0.878 (95% CI [0.877–0.878]). The corresponding sensitivity and specificity were 0.900 (95% CI [0.900–0.901]) and 0.595 (95% CI [0.592–0.598]), respectively. 

Taken together, these findings demonstrate that LGBM provided the most robust and clinically reliable performance among the evaluated ML approaches. 

**Table 2.** Results of the 2 s time windows model using various ML methods. 

|**Model**|**Operating**<br>**Point**|**AUROC**|**ACC**|**SEN**|**Results**<br>**SPE**|**(95% CI)**<br>**BER**|**MCC**|**F1_Score**|**KAPPA**|
|---|---|---|---|---|---|---|---|---|---|
|LGBM|Sen = Spe<br>Sen of 90%|0.825<br>(0.823–0.826)|0.741<br>(0.740–0.742)<br>0.878<br>|0.741<br>(0.740–0.742)<br>0.900<br>|0.741<br>(0.738–0.744)<br>0.595<br>|0.259<br>(0.258–0.260)<br>0.252<br>|0.275<br>(0.273–0.277)<br>0.376<br>|0.294<br>(0.293–0.296)<br>0.416<br>|0.201<br>(0.200–0.202)<br>0.354<br>|
||||(0.877–0.878)|(0.900–0.901)|(0.592–0.598)|(0.251–0.254)|(0.373–0.378)|(0.413–0.418)|(0.352–0.356)|
||Sen = Se||0.654<br>|0.654<br>|0.654<br>|0.346<br>|0.166<br>|0.216<br>|0.107<br>|
|LR|p<br>S f 90%|0.716<br>(0.714–0.718)|(0.653–0.655)<br>0.862|(0.653–0.655)<br>0.900|(0.651–0.657)<br>0.377|(0.345–0.348)<br>0.361|(0.164–0.168)<br>0.222|(0.215–0.217)<br>0.285|(0.106–0.108)<br>0.213|
||en o||(0.861–0.862)|(0.899–0.901)|(0.374–0.381)|(0.360–0.363)|(0.219–0.224)|(0.282–0.287)|(0.211–0.216)|



_Bioengineering_ **2025** , _12_ , 1049 

8 of 15 

**Table 2.** _Cont._ 

|**Mdl**|**Operating**||||**Results**<br>|**(95% CI)**<br>||||
|---|---|---|---|---|---|---|---|---|---|
|**oe**|**Point**|**AUROC**|**ACC**|**SEN**|**SPE**|**BER**|**MCC**|**F1_Score**|**KAPPA**|
|RF|Sen = Spe<br>Sen of 90%|0.794<br>(0.793–0.795)|0.703<br>(0.702–0.704)<br>0.876<br>(0.876–0.877)|0.701<br>(0.701–0.702)<br>0.900<br>(0.900–0.901)|0.725<br>(0.722–0.728)<br>0.565<br>(0.563–0.567)|0.287<br>(0.285–0.288)<br>0.267<br>(0.266–0.268)|0.236<br>(0.234–0.237)<br>0.356<br>(0.354–0.358)|0.263<br>(0.261–0.264)<br>0.399<br>(0.398–0.402)|0.163<br>(0.161–0.164)<br>0.337<br>(0.335–0.339)|
|NB|Sen = Spe<br>S f 90%|0.741<br>(0.739–0.743)|0.675<br>(0.675–0.676)<br>0.864|0.675<br>(0.674–0.676)<br>0.900|0.675<br>(0.673–0.679)<br>0.408|0.325<br>(0.323–0.326)<br>0.346|0.191<br>(0.190–0.193)<br>0.245|0.233<br>(0.231–0.234)<br>0.305|0.127<br>(0.126–0.129)<br>0.235|
||en o||(0.864–0.865)|(0.900–0.901)|(0.406–0.412)|(0.344–0.347)|(0.243–0.248)|(0.303–0.308)|(0.233–0.238)|





<!-- Start of picture text -->
Time Window   2S<br>0.85  0.835 0.837 0.837 Time Window   6S<br>0.825<br>Time Window  10S<br>0.804 0.805 0.809 Time Window  20S<br>0.794<br>0.80<br>0.75  0.737 0.741 0.738 0.738 0.739<br>0.730<br>0.725<br>0.716<br>0.70<br>0.65<br>0.60<br>LGBM LR RF NB<br>ROC<br><!-- End of picture text -->

**Figure 4.** AUC values for the performance of inadequate sedation recognition under different time windows across various ML methods. 

### _3.3. Analysis of ML Performance Across Different Time Windows_ 

To evaluate the effect of temporal resolution, static windows of 2, 6, 10, and 20 s were constructed. For each duration, four machine learning models were trained and assessed using standard metrics. Figure 5 illustrates the AUC trends across different window lengths. The results indicate that LGBM consistently outperformed the other algorithms across all time windows. As the window length increased from 2 to 20 s, the performance of LGBM, RF, and LR improved, whereas NB showed minimal change. LR demonstrated the largest relative improvement, with an AUC increase of 0.021, although it remained inferior to LGBM. Detailed results for each model–window combination are provided in the Supplementary Materials (Table S5). 

### _3.4. Analysis of Model Interpretability_ 

Model interpretability was assessed using SHAP, applied to the best-performing classifier (LGBM). This method quantified the relative contribution and direction of each physiological and demographic feature to the prediction of inadequate sedation. The analysis identified MBP, ETCO2, SBP, HR, BMI, HRV_CVNN, gender, and ASA physical status as the most influential predictors (Figure 6). Positive SHAP values indicated that higher values of these variables were associated with an increased likelihood of classification into the inadequate sedation group. 

Furthermore, the model revealed sex-related differences, with female patients showing a higher likelihood of being classified as inadequately sedated, potentially reflecting physiological differences in anesthetic sensitivity. 

_Bioengineering_ **2025** , _12_ , 1049 

9 of 15 



**Figure 5.** ROC curves illustrating the performance of inadequate sedation identification using different machine learning methods. For inadequate sedation detection at different time windows: ( **A** ) 2 s, ( **B** ) 6 s, ( **C** ) 10 s, and ( **D** ) 20 s. The dashed diagonal line represents the performance of a random classifier (AUC = 0.5). 



**Figure 6.** SHAP summary plot illustrates the contribution of input features to the prediction of inadequate sedation based on the LGBM model. The plot shows the top 20 features ranked by their overall importance. Features with greater cumulative impact are positioned higher on the _y_ -axis. SHAP values along the _x_ -axis represent both the direction and magnitude of each feature’s influence on the model output. Positive SHAP values indicate that the feature increases the predicted probability of being classified into the inadequate sedation group. For continuous variables, the color gradient (red = high values, blue = low values) depicts how changes in feature magnitude affect the classification likelihood. 

_Bioengineering_ **2025** , _12_ , 1049 

10 of 15 

### _3.5. The Influence of Feature Selection on the Performance of Algorithms_ 

To assess the impact of dimensionality reduction, two feature subsets were derived from the SHAP-based rankings. The OPT_subset included 20 predictors identified as most influential for model performance, while the MIN_subset comprised 12 features that preserved most of the model’s discriminative capacity. Their classification performance is shown in Figure 7 and detailed in the Supplementary Materials (Table S6). 



**Figure 7.** Feature selection curve for the LGBM model in inadequate sedation detection. The _X_ -axis shows the number of features included, and the _Y_ -axis represents the average balanced error rate (BER) from 10-fold cross-validation. The gray shaded area indicates the standard deviation of BER across folds. Features were added sequentially in descending order of SHAP importance. The red circle marks the OPT_subset (lowest average BER), while the green triangle marks the MIN_subset (fewest features achieving near-optimal performance). 

For the LGBM model, the OPT_subset achieved an AUC of 0.827 and an ACC of 0.743, representing a slight improvement over the Sorted full feature set (SOR_subset). The MIN_subset achieved an AUC of 0.825 and an ACC of 0.738 only marginally lower than the SOR_subset, despite a 55.6% reduction in dimensionality. 

## **4. Discussion** 

This study developed a real-time ML model to detect inadequate sedation during general anesthesia using non-invasive, non-EEG physiological signals, with BIS serving as a surrogate reference standard. The results demonstrate that routine intraoperative physiological parameters effectively identify inadequate sedation, particularly in environments where EEG-based methods are impractical, such as prehospital, emergency, and battlefield care. This approach offers a scalable, cost-effective alternative for anesthesia monitoring in resource-limited or mobile clinical settings. 

First, among the four ML algorithms evaluated, LGBM exhibited the best performance, achieving an AUC of 0.825 (95% CI: 0.823–0.826) using real-time physiological data. When SEN was fixed at 90%, ACC increased to 0.878 (95% CI: 0.877–0.878). These findings highlight the feasibility of using non-EEG physiological parameters for real-time detection of inadequate sedation, offering a more cost-effective and efficient alternative to traditional BIS systems. In contrast to BIS, which can be expensive and prone to signal interference in high-motion environments, this ML model provides a scalable solution, especially 

_Bioengineering_ **2025** , _12_ , 1049 

11 of 15 

valuable in settings such as emergency care or battlefield care, where rapid decision-making is essential. 

Second, the length of the monitoring time window significantly influenced model performance. Extending the time window from 2 s to 20 s resulted in an AUC increase of 0.012, capturing more detailed physiological dynamics and improving prediction reliability. Clinically, longer time windows improve the ACC of detecting inadequate sedation. However, while shorter windows slightly decrease ACC, they offer a faster, more efficient model, which is better suited for high-demand environments requiring rapid decision-making. 

Third, the SHAP-based interpretability analysis revealed that several key features (MBP, ETCO2, SBP, HR, BMI, HRV_CVNN, and ASA) significantly impacted the model’s predictions. Increases in MBP, SBP, HR, and changes in HRV_CVNN reflect the body’s physiological response to inadequate sedation, which aligns with clinical observations of inadequate sedation. In Figure 6, the high feature values in red indicate a positive correlation with classification into the inadequate sedation group. The increase in HRV_CVNN corresponds to heightened sympathetic activity. The high importance of ETCO2 reflects the impact of inadequate sedation on respiratory function. Higher BMI may alter the pharmacokinetics of anesthetic drugs, thereby increasing the risk of inadequate sedation, while the ASA classification highlights the challenges of maintaining appropriate sedation in patients with underlying health conditions. The model also predicts a higher probability of inadequate sedation in female patients, which aligns with studies reporting that women exhibit increased emergence sensitivity and faster recovery from anesthesia. These findings emphasize the importance of individualized sedation protocols based on physiological markers and patient demographics, and highlight the model’s potential to optimize sedation management and improve patient safety. 

Fourth, this study examined the impact of feature dimensionality on model performance. Initially, the LGBM model utilized 27 physiological features. Reducing the feature set to the top 20 features (OPT_subset) resulted in a slight AUC improvement of 0.002, suggesting that irrelevant or redundant features could introduce noise. Further reducing the model to a minimal set of 12 features (MIN_subset) led to decreases of only 0.002 in AUC and 0.003 in ACC, despite a 55.6% reduction in input dimensionality. These findings highlight the importance of feature selection in simplifying models while maintaining strong classification performance. Clinically, this is particularly significant for real-time or embedded systems in low-resource settings, such as emergency care or battlefield scenarios, where reduced computational complexity and faster response times are critical for ensuring patient safety and facilitating effective decision-making. 

Finally, to explore the model’s dynamic behavior and interpretability in real-time monitoring, an individual case analysis is presented in Figure 8. This example involves a 64-year-old male patient undergoing general anesthesia for colon cancer surgery, with 172 points, each representing 2 s of continuous intraoperative data. During the initial phase (0 to 113 points), when BIS values remained below 60, the SHAP contribution map (Figure 8E) shows minimal influence of features such as MBP, SBP, and HR on classifying inadequate sedation. However, once BIS exceeds 60, these SHAP regions expand and shift toward red, indicating an increased importance of MBP, SBP, and HR in detecting lighter sedation states. 

_Bioengineering_ **2025** , _12_ , 1049 

12 of 15 





**Figure 8.** Dynamic influence of physiological parameters on real-time detection of inadequate sedation. ( **A** – **D** ) show the time series of BIS, SBP, MBP, and HR, with the _x_ -axis representing intraoperative time (0–113 points). ( **E** ) shows the SHAP-based feature contribution map, and ( **F** ) displays synchronized trends of key physiological parameters. 

The consistent trends across Figure 8A–D (physiological time series), Figure 8E (SHAP heatmap), and Figure 8F (aggregated parameter visualization) demonstrate a strong temporal correlation between BIS transitions and model-predicted states. The model is in accordance with the expected physiological changes resulting from insufficient anesthetic drug dosage. As sedation becomes inadequate, sympathetic activation is reflected by elevated HR and BP, which the model accurately predicts. The SHAP-based feature contributions demonstrate the model’s transparency, ensuring it is not a “black box” but a tool offering clear insights into physiological mechanisms driving predictions. This interpretability allows anesthesiologists to trust the model’s decisions, facilitating timely adjustments and improving patient outcomes. 

## **5. Challenges, Limitations, and Future Directions** 

This study has several challenges and limitations that should be acknowledged. First, the dataset was derived from intraoperative cases in a controlled hospital environment, which may not fully represent real-world, out-of-hospital settings such as emergency care or mass casualty incidents. Noise, motion artifacts, and incomplete data in such environments can hinder model performance; therefore, future work should focus on enhancing robustness through denoising algorithms and data augmentation techniques. Second, the study was retrospective and limited to a single center. To improve generalizability and clinical utility, future research will collect real-world out-of-hospital data, expand the sample to include patients of different ages, comorbidities, and anesthetic responses, and conduct multi-center validation. Individualized optimization will also be explored to adapt model parameters to patient-specific characteristics and clinical needs. Third, the reliance on BIS > 60 as the sole definition of inadequate sedation, although clinically accepted, has 

_Bioengineering_ **2025** , _12_ , 1049 

13 of 15 

inherent limitations. BIS is susceptible to artifacts and inter-patient variability, which may introduce label noise into the training process. Future studies should therefore integrate BIS with complementary clinical endpoints such as anesthetic drug concentrations, patient movement responses, and hemodynamic indicators to construct a more precise and robust multimodal ground truth for defining sedation depth. Finally, this approach may offer economic advantages, as models based on routine vital signs could provide a more cost-effective alternative to EEG or BIS based systems in resource-limited settings. 

Taken together, these considerations highlight key opportunities for future research, particularly in enhancing robustness, expanding validation, and integrating multimodal endpoints, which will strengthen the methodological foundation and advance clinical translation. 

## **6. Conclusions** 

This study developed and validated a real-time machine learning model that uses noninvasive, non-electroencephalography (EEG) physiological signals to detect inadequate sedation during surgery, demonstrating good performance. By integrating multi-source data, including vital signs and heart rate variability (HRV) metrics, the model offers a costeffective and scalable alternative to traditional anesthesia depth monitoring systems. This approach is particularly beneficial in high-demand, resource-limited environments, such as emergency medical transport and battlefield care, where out-of-hospital monitoring is required. Future work will focus on further optimizing the model, conducting multi-center validation, and expanding its application to other clinical scenarios to enhance sedation management and improve patient safety. 

## **7. Patents** 

Tiangong University. Huiquan Wang, Chunliang Jiang. et al. Anesthesia depth dynamic identification auxiliary analysis method, device, server and medium: ZL202510458834.5[P] 25 July 2025. 

**Supplementary Materials:** The following supporting information can be downloaded at: https: //www.mdpi.com/article/10.3390/bioengineering12101049/s1, Table S1. Definition of heart rate variability (HRV) parameters. Table S2. Missing Values Table. Table S3. The 27 feature parameters extracted from the VitalDB database. Table S4. Dataset characteristics. Table S5. Results of time window model using various ML methods. Table S6. Outcomes of feature selection for the model: Identification results of the LGBM algorithms for different feature subsets. Figure S1. Violin plots of the 23 physiological parameters included in this study showing the distribution of the parameters after preprocessing. Algorithm S1. Pseudocode for real-time detection of inadequate sedation using non-EEG signals. 

**Author Contributions:** Conceptualization, H.W., C.J. and G.Z.; Methodology, H.W., C.J. and G.Z.; Software, H.W., X.M. and M.Y.; Validation, H.W., C.J., G.Z. and J.Y.; Formal analysis, H.W. and C.J.; Data curation, H.W. and G.Z.; Writing—original draft, H.W.; Writing—review and editing, H.W., C.J., G.Z., G.L. and J.Y.; Project administration, G.Z.; Supervision, G.Z.; Investigation, G.L., J.Y., C.L. and J.X.; Resources, G.L., J.Y., C.L. and J.X. All authors have read and agreed to the published version of the manuscript. 

**Funding:** This research was funded by the National Key Research and Development Program of China, grant number 2023YFC3011802. 

**Institutional Review Board Statement:** The data utilized in this study were obtained from the publicly accessible VitalDB database (https://vitaldb.net/dataset/?query=viewer, accessed on 15 March 2023), a de-identified repository with all personal identifiers removed to ensure patient privacy. Given the open-access nature of the dataset and its full anonymization, this study was exempt from institutional ethics committee approval and the requirement for written informed consent from 

_Bioengineering_ **2025** , _12_ , 1049 

14 of 15 

participants, in compliance with applicable ethical guidelines for secondary analyses of pre-existing anonymized data. 

**Informed Consent Statement:** Not applicable. 

**Data Availability Statement:** The data and code used to support the findings of this study are available from the corresponding author on request. 

**Acknowledgments:** We sincerely thank the VitalLab team for their open-access VitalDB database (https://vitaldb.net/, accessed on 15 March 2023), which provided essential clinical data for this study. 

**Conflicts of Interest:** The authors have no conflicts of interest to declare. 

## **Abbreviations** 

The following abbreviations are used in this manuscript:EEG: Electroencephalography; BIS: Bispectral Index; AUC: Area Under the Curve; ACC: Accuracy; SHAP: SHapley Additive exPlanations; LGBM: Light Gradient Boosting Machine; HR: Heart Rate; BP: Blood Pressure; DBP: Diastolic Blood Pressure; MBP: Mean Blood Pressure; SBP: Systolic Blood Pressure; SPO2: Peripheral Oxygen Saturation; ETCO2: End-Tidal Carbon Dioxide; HRV: Heart Rate Variability; ASA: American Society of Anesthesiologists; BMI: Body Mass Index; RF: Random Forest; LR: Logistic Regression; NB: Naive Bayes; ML: Machine Learning; CI: Confidence Interval; ROC: Receiver Operating Characteristic; SEN: Sensitivity; SPE: Specificity; BER: Bayesian Error Rate; MCC: Matthews Correlation Coefficient; KAPPA: Cohen’s Kappa; PPG: Photoplethysmography; ECG: Electrocardiogram; OPT_subset: Optimal Feature Subset; MIN_subset: Minimum Feature Subset; SOR_subset: Sorted Full Feature Subset. 

## **References** 

1. Schmierer, T.; Li, T.; Li, Y. Harnessing machine learning for EEG signal analysis: Innovations in depth of anaesthesia assessment. _Artif. Intell. Med._ **2024** , _151_ , 102869. [CrossRef] 

2. Thiele, R.H.; Shaw, A.D.; Bartels, K.; Brown Grocott, H., IV; Heringlake, M.; Gan, T.J.; Miller, T.E.; McEvoy, M.D.; Perioperative Quality Initiative (POQI) 6 Workgroup. American Society for Enhanced Recovery and Perioperative Quality Initiative Joint Consensus Statement on the Role of Neuromonitoring in Perioperative Outcomes: Cerebral Near-Infrared Spectroscopy. _Anesth. Analg._ **2020** , _131_ , 1444–1455. [CrossRef] [PubMed] 

3. Brown, E.N.; Purdon, P.L.; Akeju, O.; Solt, K. _40-Monitoring the State of the Brain and Central Nervous System During General Anesthesia and Sedation_ ; Elsevier Inc.: Amsterdam, The Netherlands, 2020. 

4. Mathur, S.; Patel, J.; Goldstein, S.; Hendrix, J.M.; Jain, A. Bispectral Index. In _StatPearls_ ; StatPearls Publishing: Treasure Island, FL, USA, 2025. [PubMed] 

5. Hight, D.; Kreuzer, M.; Ugen, G.; Schuller, P.; Stüber, F.; Sleigh, J.; Kaiser, H.A. Five commercial ‘depth of anaesthesia’ monitors provide discordant clinical recommendations in response to identical emergence-like EEG signals. _Br. J. Anaesth._ **2023** , _130_ , 536–545. [CrossRef] [PubMed] 

6. Ellerkmann, R.K.; Soehle, M.; Kreuer, S. Brain monitoring revisited: What is it all about? _Best Pract. Res. Clin. Anaesthesiol._ **2013** , _27_ , 225–233. [CrossRef] 

7. Lee, H.C.; Ryu, H.G.; Park, Y.; Yoon, S.B.; Yang, S.M.; Oh, H.W.; Jung, C.W. Data Driven Investigation of Bispectral Index Algorithm. _Sci. Rep._ **2019** , _9_ , 13769. [CrossRef] [PubMed] [PubMed Central] 

8. Liu, Q.; Ma, L.; Chiu, R.C.; Fan, S.Z.; Abbod, M.F.; Shieh, J.S. HRV-derived data similarity and distribution index based on ensemble neural network for measuring depth of anaesthesia. _PeerJ_ **2017** , _5_ , e4067. [CrossRef] [PubMed] [PubMed Central] 

9. Chowdhury, M.R.; Madanu, R.; Abbod, M.F.; Fan, S.Z.; Shieh, J.S. Deep learning via ECG and PPG signals for prediction of depth of anesthesia. _Biomed. Signal Process. Control_ **2021** , _68_ , 102663. [CrossRef] 

10. Wang, G.; Liu, Z.; Feng, Y.; Li, J.; Dong, H.; Wang, D.; Li, J.; Yan, N.; Liu, T.; Yan, X. Monitoring the Depth of Anesthesia Through the Use of Cerebral Hemodynamic Measurements Based on Sample Entropy Algorithm. _IEEE Trans. Biomed. Eng._ **2020** , _67_ , 807–816. [CrossRef] [PubMed] 

11. Zhan, J.; Wu, Z.X.; Duan, Z.X.; Yang, G.Y.; Du, Z.Y.; Bao, X.H.; Li, H. Heart rate variability-derived features based on deep neural network for distinguishing different anaesthesia states. _BMC Anesthesiol._ **2021** , _21_ , 66. [CrossRef] [PubMed] [PubMed Central] 

_Bioengineering_ **2025** , _12_ , 1049 

15 of 15 

12. Yin, Q.; Shen, D.; Ding, Q. Influence of Sliding Time Window Size Selection Based on Heart Rate Variability Signal Analysis on Intelligent Monitoring of Noxious Stimulation under Anesthesia. _Neural Plast._ **2021** , _2021_ , 6675052. [CrossRef] [PubMed] [PubMed Central] 

13. Lundberg, S.M.; Lee, S.I. A unified approach to interpreting model predictions. In Proceedings of the Advances in Neural Information Processing Systems 30, Long Beach, CA, USA, 4–9 December 2017. 

14. Sundararajan, M.; Najmi, A. The many Shapley values for model explanation. In Proceedings of the International Conference on Machine Learning PMLR, Virtual, 12–18 July 2020; pp. 9269–9278. 

15. Lundberg Scott, M.; Gabriel, G. Erion, and Su-In Lee. Consistent individualized feature attribution for tree ensembles. _arXiv_ **2018** , arXiv:1802.03888. 

16. Gong, K.D.; Lu, R.; Bergamaschi, T.S.; Sanyal, A.; Guo, J.; Kim, H.B.; Nguyen, H.T.; Greenstein, J.L.; Winslow, R.L.; Stevens, R.D. Predicting Intensive Care Delirium with Machine Learning: Model Development and External Validation. _Anesthesiology_ **2023** , _138_ , 299–311. [CrossRef] [PubMed] 

17. Afshar, S.; Boostani, R.; Sanei, S. A Combinatorial Deep Learning Structure for Precise Depth of Anesthesia Estimation From EEG Signals. _IEEE J. Biomed. Health Inform._ **2021** , _25_ , 3408–3415. [CrossRef] [PubMed] 

18. Nguyen-Ky, T.; Tuan, H.D.; Savkin, A.; Do, M.N.; Van, N.T.T. Real-Time EEG Signal Classification for Monitoring and Predicting the Transition Between Different Anaesthetic States. _IEEE Trans. Biomed. Eng._ **2021** , _68_ , 1450–1458. [CrossRef] [PubMed] 

19. Lee, H.C.; Park, Y.; Yoon, S.B.; Yang, S.M.; Park, D.; Jung, C.W. VitalDB, a high-fidelity multi-parameter vital signs database in surgical patients. _Sci. Data_ **2022** , _9_ , 279. [CrossRef] [PubMed] [PubMed Central] 

20. Lee, H.C.; Jung, C.W. Vital Recorder-a free research tool for automatic recording of high-resolution time-synchronised physiological data from multiple anaesthesia devices. _Sci. Rep._ **2018** , _8_ , 1527. [CrossRef] [PubMed] [PubMed Central] 

21. Feng, C.D.; Xu, Y.; Chen, S.; Song, N.; Meng, X.W.; Liu, H.; Ji, F.H.; Peng, K. Opioid-free anaesthesia reduces postoperative nausea and vomiting after thoracoscopic lung resection: A randomised controlled trial. _Br. J. Anaesth._ **2024** , _132_ , 267–276. [CrossRef] [PubMed] 

22. Short, T.G.; Campbell, D.; Frampton, C.; Chan, M.T.V.; Myles, P.S.; Corcoran, T.B.; Sessler, D.I.; Mills, G.H.; Cata, J.P.; Painter, T.; et al. Anaesthetic depth and complications after major surgery: An international, randomised controlled trial. _Lancet_ **2019** , _394_ , 1907–1914. [CrossRef] [PubMed] 

23. Frasch, M.G. Comprehensive HRV estimation pipeline in Python using Neurokit2, Application to sleep physiology. _MethodsX_ **2022** , _9_ , 101782. [CrossRef] [PubMed] [PubMed Central] 

24. Tsvetanova, A.; Sperrin, M.; Peek, N.; Buchan, I.; Hyland, S.; Martin, G.P. Missing data was handled inconsistently in UK prediction models: A review of method used. _J. Clin. Epidemiol._ **2021** , _140_ , 149–158. [CrossRef] [PubMed] 

25. Mei, Z.; Grummer-Strawn, L.M. Standard deviation of anthropometric Z-scores as a data quality assessment tool using the 2006 WHO growth standards: A cross country analysis. _Bull. World Health Organ._ **2007** , _85_ , 441–448. [CrossRef] [PubMed] [PubMed Central] 

26. Drewe, J.; Küsters, E.; Hammann, F.; Kreuter, M.; Boss, P.; Schöning, V. Modeling Structure-Activity Relationship of AMPK Activation. _Molecules_ **2021** , _26_ , 6508. [CrossRef] [PubMed] [PubMed Central] 

27. Ke, G.; Meng, Q.; Finley, T.; Wang, T.; Chen, W.; Ma, W.; Ye, Q.; Liu, T.-Y. LGBM: A highly efficient gradient boosting decision tree. In Proceedings of the Advances in Neural Information Processing Systems 30, Long Beach, CA, USA, 4–9 December 2017; pp. 1–11. 

28. Dodek, P.M.; Wiggs, B.R. Logistic regression model to predict outcome after in-hospital cardiac arrest: Validation, accuracy, sensitivity and specificity. _Resuscitation_ **1998** , _36_ , 201–208. [CrossRef] [PubMed] 

29. Yang, F.-J. An implementation of naive Bayes classifier. In Proceedings of the 2018 International Conference on Computational Science and Computational Intelligence (CSCI), Las Vegas, NV, USA, 7–9 December 2018; pp. 1091–1096. 

30. Theng, D.; Bhoyar, K.K. Feature selection techniques for machine learning: A survey of more than two decades of research. _Knowl. Inf. Syst._ **2024** , _66_ , 1575–1637. [CrossRef] 

31. Pedregosa, F.; Varoquaux, G.; Gramfort, A.; Michel, V.; Thirion, B.; Grisel, O.; Blondel, M.; Prettenhofer, P.; Weiss, R.; Dubourg, V.; et al. Scikit-learn: Machine learning in Python. _J. Mach. Learn. Res._ **2011** , _12_ , 2825–2830. 

32. Braithwaite, H.E.; Payne, T.; Duce, N.; Lim, J.; McCulloch, T.; Loadsman, J.; Leslie, K.; Webster, A.C.; Gaskell, A.; Sanders, R.D. Impact of female sex on anaesthetic awareness, depth, and emergence: A systematic review and meta-analysis. _Br. J. Anaesth._ **2023** , _131_ , 510–522. [CrossRef] [PubMed] 

**Disclaimer/Publisher’s Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content. 

