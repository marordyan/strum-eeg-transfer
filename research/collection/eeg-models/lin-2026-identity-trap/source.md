# The Identity Trap in EEG Foundation Models: A Diagnostic Audit 

Jun-You Lin<sup>∗</sup> School of Medicine, National Yang Ming Chiao Tung University, Taipei, Taiwan 

Ying Choon Wu Swartz Center for Computational Neuroscience, University of California, San Diego, La Jolla, CA 92037, USA 

Tzyy-Ping Jung<sup>†</sup> Swartz Center for Computational Neuroscience, University of California, San Diego, La Jolla, CA 92037, USA 

June 8, 2026 

### **Abstract** 

**_Objective._** _EEG foundation models (FMs) report strong headline accuracy on clinical resting-state EEG. However, high accuracy under subject-disjoint cross-validation remains ambiguous: it can reflect a genuine clinical biomarker, or subject-identity features that correlate with the label in this cohort. We name this ambiguity the_ Identity Trap _and ask whether it can be diagnosed at the representation level before fine-tuning._ 

**_Approach._** _We propose FMScope, a frozen-representation pre-flight protocol packaging five diagnostics: variance decomposition, subject-axis erasure, aperiodic_ 1 _/f ablation, layer-wise label probing, and within-subject direction consistency. We apply it to three pretrained transformer FMs (LaBraM, CBraMod, REVE) across four public resting-state datasets (mental arithmetic, sleep deprivation, Alzheimer’s and frontotemporal dementia, trait stress) in an_ a priori 2 _×_ 2 _layout: subject relation of label × presence of a consensus cross-subject EEG marker._ 

**_Main results._** _(i) The Identity Trap is universal across all three FMs: the frozen subject-variance fraction is 13–89× a random-Gaussian null in 12 of 12 pairs, rising in all 12 under fine-tuning (_ +10 _to_ +63 _pp). This dominance lies on a removable linear axis: erasing it significantly improves label decoding where the label varies within subject (_ +6 _to_ +12 _pp in primary cells;_ +4 _to_ +27 _pp across four external consensus-marker cohorts; one-sided sign test p <_ 10<sup>_−_3</sup> _). (ii) Aperiodic_ 1 _/f is one identifiable subject carrier: removing it drops the subject probe by_ 9 _–_ 19 _pp uniformly on LaBraM and CBraMod. REVE saturates subject identity with no measurable aperiodic dependence and a nonlinearly-decodable residual after linear erasure: the Identity Trap is universal, but its carrier and linear removability are model-specific. (iii) Fine-tuning amplifies label-variance only in cells with a literature-established cross-subject EEG marker (_ +0 _._ 6 _to_ +8 _._ 4 _pp). No-consensus cells span zero, indicating no label signal for fine-tuning to amplify._ 

**_Significance._** _The Identity Trap is a physically-grounded instance of shortcut learning: the preferred cue has a measurable physiological component of the input, not a pure statistical artifact,_ 

> ∗ Corresponding author. `linjimmy1003.md10@nycu.edu.tw` . ORCID: 0009-0006-3951-3614. 

> †ORCID: 0000-0002-8377-2166. 

1 

Preprint 

2 

_and subject-disjoint splitting alone cannot rule it out. FMScope thus separates gains that reflect a biological marker from those that reflect subject identity._ 

**_Keywords:_** _EEG foundation models; subject-identity confounding; shortcut learning; representation analysis; clinical biomarkers; resting-state EEG._ 

## **1 Introduction** 

EEG foundation models (FMs) are pretrained on large unlabeled EEG corpora with self-supervised maskedmodeling objectives, and have been proposed as a general substrate for clinical electroencephalography (Jiang et al., 2024; Wang et al., 2025a; El Ouahidi et al., 2025). On downstream tasks with established within-subject neural contrasts (motor imagery, event-related potentials, sleep staging), reported performance is strong (Xiong et al., 2025; Wu et al., 2025; Kastrati et al., 2025), building on a decade of cross-subject classification protocols (Lotte et al., 2018). The picture fragments on small- _N_ resting-state EEG (rsEEG), the setting that matters most for psychiatric and neurodegenerative biomarkers. On cohorts of comparable size and recording quality, FM performance varies widely across clinical labels (Shen et al., 2026); what controls this variation has not been addressed at the representation level. Consider the self-reported chronic-stress dataset of Komarov et al. (2020). A prior FM evaluation on this dataset reports a peak balanced accuracy of 0 _._ 9047, using a fixed 80/10/10 train/val/test split in which the same subjects appear in different folds (best of four data-splitting seeds; the worst seed reaches 0 _._ 67) (Wang et al., 2025b). On the same dataset, under subject-disjoint cross-validation, we observe 0 _._ 43–0 _._ 50 across three FMs and five classical baselines (Sec. 4.1). Both numbers can be correct under their own protocols. Neither tells us what the FM has actually learned about the label. 

A single accuracy number cannot resolve this ambiguity. High balanced accuracy under subject-disjoint cross-validation is consistent with at least three readings: (i) the FM has captured a genuine cross-subject EEG marker of the clinical label; (ii) the FM has captured stable physiological subject traits that happen to co-vary with the label in this cohort; or (iii) the FM has captured an entanglement of the two that does not separate at the read-out. Existing benchmarks enumerate scores (Shen et al., 2026; Xiong et al., 2025; Wu et al., 2025; Kastrati et al., 2025); protocol critiques identify subject-identity leakage under trial-level cross-validation as one inflation source (Brookshire et al., 2024). The underlying tension is not EEG-specific. Resting-state fMRI fingerprinting shows that stable between-individual differences in brain activity are sufficient to identify subjects (Finn et al., 2015), and that the connections that identify a subject and the connections that predict behavior occupy different functional systems of the connectome (Mantwill et al., 2022). Together, these results suggest a recurring competition, across brain-imaging modalities, between stable subject-identifying structure and the task-related signal that biomarkers depend on. Both lines of work establish that the problem exists. Neither tells us, for a specific cohort _×_ FM pair, which of the three readings is operative at the representation level. 

We approach this question through one well-characterized physiological component of the EEG spectrum: the aperiodic 1 _/f_ background. The standard FOOOF decomposition separates the EEG power spectrum into two parts: a broadband 1 _/f_<sup>_χ_</sup> component (the aperiodic background itself) and narrow periodic peaks at canonical bands such as theta and alpha (Donoghue et al., 2020). Periodic peaks carry transient, task-related state information of the kind clinical biomarkers typically index. The aperiodic background reflects more stable properties of the recording: cortical excitation–inhibition balance and vigilance state (Gao et al., 2017), and electrode-level features that vary between individuals and persist across sessions (Kopčanová et al., 2024). In ordinary EEG analysis, researchers treat the aperiodic background as a per-subject nuisance and remove it by fitting a parametric model before they analyze the periodic peaks. FMs are pretrained without any subject-aware objective, so it is unclear whether their representations remove the aperiodic component in the same way, or instead keep it as an axis that encodes subject identity. This raises a specific, correlational question: do EEG FM representations on small- _N_ rsEEG _co-encode_ the aperiodic 1 _/f_ background with subject identity along the same representational directions? We can test it on LaBraM and CBraMod; on REVE the test is inconclusive, because REVE differs from the other two FMs along five design axes at once 

Preprint 

3 

(Sec. 5.5). Independently of this carrier question, fine-tuning shows a cell-conditional pattern: it amplifies subject-related variance in every cell, but amplifies label-related variance only in cells where the literature has already established a cross-subject neural marker. 

We test this hypothesis on four public small- _N_ clinical rsEEG datasets chosen _a priori_ to populate a 2 _×_ 2 sampling layout (subject relation of the label _×_ presence of a consensus cross-subject EEG marker) across three pretrained transformer FMs (LaBraM, CBraMod, REVE). We package the diagnostics required for the test as FMScope (Fig. 1), a frozen-representation framework with explicit scope conditions per tool. We make four contributions. 

**First** , an empirical finding we term the _Identity Trap_ : across 12 (cell _×_ FM) frozen pairs the subjectvariance fraction is 13–89 _×_ a matched random-Gaussian null; under fine-tuning, subject-variance fraction rises in all 12 pairs by +10 to +63 percentage points (pp). This dominance is confined to a removable linear axis: closed-form subject-axis erasure drives a linear subject probe to chance in all 12 pairs, and where the label varies within subject, erasing identity significantly improves label decoding (+6 to +12 pp in the primary cells; +4 to +27 pp across four external consensus-marker cohorts; one-sided sign test _p <_ 10<sup>_−_3</sup> ). 

**Second** , a representational correlate of the 1 _/f_ –subject co-encoding hypothesis: removing the aperiodic 1 _/f_ component drops a linear subject probe by 9 to 19 pp uniformly across all four cells on LaBraM and CBraMod. REVE shows no measurable aperiodic dependence; the LaBraM-and-CBraMod group differs from REVE along five concurrent design axes (Sec. 5.5), so we report this two-versus-one pattern descriptively rather than as a mechanism claim. 

**Third** , a cell-conditional outcome map: fine-tuning amplifies label-variance only in cells with a consensus cross-subject EEG marker (Mann–Whitney _U_ , one-sided _p_ = 0 _._ 0022, _n_ = 12), and the layer-wise label probe descends monotonically toward chance in the no-consensus trait cell on all three FMs. 

**Fourth** , the FMScope diagnostic framework itself, including its per-tool scope conditions, plus the clinical/protocol guidelines that follow from the three findings above: recording trait-cell labels as withinsubject contrasts where the state allows, and seeking external physiological validation where it does not; verifying that within-subject classifier directions agree across subjects before any BCI calibration claim; and a frozen-feature pre-flight that returns a per-cell verdict (Tab. 4) before any fine-tuning compute is spent. 

Preprint 

4 



<!-- Start of picture text -->
EEG inputs Subject dominant representation  FMScope<br>Subject 0 Frozen representation space Variance<br>Subject ID Decomposition<br>Subject 1 (strong axis)<br>Subject label Residual<br>Subject 2<br>Subject 3<br>label A Subject-axis erasure<br>label B (LEACE)<br>Foundation Models Clinical label<br>(weak axis) FOOOF Ablation<br>(Aperiodic removal)<br>Patch embedding<br>Position encoding Before (dominated) After (removed) Layer-wise<br>Subject/label probe<br>Remove linear<br>Attention blocks subject components layer depth<br>Within-subject<br>Pooling Direction Consistency<br>Subject Accuracy<br><!-- End of picture text -->

Figure 1: **FMScope overview.** Five frozen-representation diagnostics applied to embeddings from a pretrained transformer EEG-FM. Two of the five establish the Identity Trap: variance decomposition and subject-axis erasure (LEACE). The other three characterize its origin and structure: aperiodic input ablation, layer-wise subject/label probe, and within-subject direction consistency. Center: subject identity forms the dominant axis of the frozen representation and the clinical label a weaker one; the inset shows closed-form removal of the linear subject components (LEACE). Colors and shapes in the embedding feature space schematically represent variations contributed by cognitive labels and individual subjects, respectively. Pertool scope conditions and details in Sec. 3; results in Sec. 4. 

## **2 Related Work** 

**EEG foundation models.** We anchor on three open-weight backbones. **LaBraM** (Jiang et al., 2024) feeds raw EEG patches through a temporal CNN into a transformer encoder. The pretraining target is a discrete vector-quantized code for each patch; a separate decoder maps each code back to the patch’s Fourier amplitude and phase, so the encoder must learn features that support Fourier reconstruction. It is pretrained on _∼_ 2 _,_ 500 hours of mixed EEG. **CBraMod** (Wang et al., 2025a) uses a criss-cross transformer that factorizes spatial and temporal attention into two parallel mechanisms. Its patch embedding adds two branches: a temporal CNN and an FFT-derived energy vector. Pretraining reconstructs raw EEG patches under an MSE loss. It is pretrained on a cleaned _∼_ 9 _,_ 000-hour subset of the Temple University EEG Corpus (TUEG total: _∼_ 15 _,_ 000 subjects, _∼_ 27 _,_ 000 hours). **REVE** (El Ouahidi et al., 2025) is a spatio-temporal transformer that uses 4D Fourier sinusoidal positional encoding and a linear patch embedding on the raw signal. Pretraining reconstructs the raw EEG under an L1 loss, with an additional attention-pooling secondary task. It is pretrained on _∼_ 60 _,_ 000 hours of EEG from 92 datasets covering 25 _,_ 000 subjects. All three use masked-modeling self-supervision but differ along at least five design axes (target representation, patch embedding, reconstruction loss, positional encoding, pretraining corpus diversity), and we therefore report cross-FM contrasts descriptively rather than as mechanism claims. All three report strong downstream performance on event-related EEG benchmarks (Xiong et al., 2025; Wu et al., 2025), but none has been characterized at the representation level on small- _N_ clinical resting-state cohorts. 

**Subject leakage and evaluation protocols.** Prior critiques have established that trial-level crossvalidation in clinical EEG inflates accuracy through subject leakage at the train–test boundary (Brookshire 

Preprint 

5 

et al., 2024), and recent benchmarks (Xiong et al., 2025; Wu et al., 2025; Kastrati et al., 2025; Shen et al., 2026) broadly adopt subject-disjoint splitting (with task-specific exceptions, e.g. subject-dependent splits retained for emotion recognition in EEG-FM-Bench). These works document the inflation; they do not characterize what the FM has learned in place of the leaked subject signal once subject-disjoint splitting is enforced. Our starting point is the ambiguity that remains even after subject-disjoint splitting: accuracy could still reflect subject-correlated features that happen to co-vary with the clinical label in a particular cohort. We ask, at the representation level, what those features actually are. A concurrent study (Tang et al., 2026) asks the same of EEG-FMs and also uses LEACE-style erasure as a diagnostic, but applied to a lexicon of hand-crafted neuro-features (band power, connectivity, entropy). It reports that removing those features degrades decoding and does not examine the subject-identity axis. We erase the subject axis instead and find that its removal can improve consensus-marker decoding, the complementary direction. 

**Prior cross-subject EEG markers for clinical labels.** Prior research documents resting-state or task-related EEG features that have been used as cross-subject biomarkers. For mental arithmetic, a substantial corpus links frontal-midline theta and parieto-occipital alpha modulation to cognitive task load (including mental arithmetic) (Klimesch, 1999; Gevins et al., 1997; Klimesch, 2012). For Alzheimer’s and frontotemporal dementia, an expert-panel consensus (Babiloni et al., 2021) cites posterior alpha peak-frequency and power reduction as a candidate clinical biomarker; a recent two-cohort replication (Kopčanová et al., 2024) reports that the AD-versus-HC spectral signature is “purely oscillatory” and that aperiodic features do not differ between groups. The aperiodic 1 _/f_ slope therefore remains a contested sub-component for AD. Comparable expert-consensus markers do not exist for our other two labels: frontal alpha asymmetry as a stress or depression marker remains contested (Reznik and Allen, 2018; van der Vinne et al., 2017), and the sleep-deprivation dataset paper (Xiang et al., 2024) tabulates individual differences in sleep quality and traits alongside the rested-versus-deprived recordings without identifying a cross-subject EEG marker. This asymmetry across the four labels is what motivates our _a priori_ sampling layout (Sec. 3.1). None of these works ask whether a pretrained FM’s representation has actually learned the marker; that is the question we take up in Sec. 4.3 via aperiodic ablation of the input. 

**Aperiodic** 1 _/f_ **background as a subject feature in EEG.** The aperiodic 1 _/f_ slope and offset are parametrized by FOOOF (Donoghue et al., 2020). Demuru and Fraschini (2020) demonstrate that these aperiodic features are stable within an individual across sessions and distinguish subjects independently of task-evoked oscillations, in parallel to functional-connectivity fingerprinting on fMRI (Finn et al., 2015) and earlier EEG biometric work (Campisi and La Rocca, 2014; Marcel and Millán, 2007). Demuru and Fraschini (2020) specifically report that handcrafted aperiodic features identify subjects with higher accuracy than canonical band-power features, and remain consistent across eyes-open and eyes-closed conditions. This makes the aperiodic 1 _/f_ one identifiable subject-specific carrier in classical EEG features. The fMRI fingerprinting work cited above documents the same between-subject stability for that modality, without specifying which spectral component carries it. A follow-on connectome analysis further reports that the edges discriminating individuals show no single-edge overlap with the edges predicting behavior across cognitive, language, and motor variables, indicating that subject-identifying and label-relevant signals can dissociate at the network-feature level (Mantwill et al., 2022). To our knowledge, no prior work has asked which spectral component carries that subject identity inside a pretrained EEG-FM, nor whether it survives self-supervised pretraining on cross-subject corpora. Sec. 4.3 addresses this question via FOOOF-aperiodic input ablation as a correlational intervention on the frozen representation. 

**Mechanism hypotheses for FM representation bias.** Three lines of prior ML work motivate, but do not establish, the mechanisms by which a self-supervised FM might preferentially encode stable physiological subject features over transient task-related features. Geirhos et al. (2020) document that neural networks tend to exploit dataset-stable cues that correlate with labels ( _shortcut features_ ) over invariant discriminative cues. Under an MSE (squared-error) reconstruction loss, masked-modeling objectives put most of their loss on the high-variance components of the input, and the model is widely conjectured to spend proportionally 

Preprint 

6 

more capacity on those same components. In EEG, the broadband aperiodic 1 _/f_ baseline carries most of the low-frequency spectral variance by construction. El Ouahidi et al. (2025) explicitly motivate their L1 (rather than MSE) reconstruction loss as a counter to the L2 sensitivity to noise and outliers in EEG. This is one concrete design choice on which our three FMs differ. Linear-network analyses (Saxe et al., 2019) additionally show that gradient descent on a linear network preferentially learns the largest-singular-value directions of the input–output correlation first, and we conjecture that an analogous direction-ordering operates under small- _N_ supervised fine-tuning of the FM head. Each of these is a candidate contributing factor for our findings; we do not isolate any of them experimentally. 

**Multi-axis taxonomies in EEG-FM benchmarking.** Existing aggregate benchmarks organize EEG-FM evaluation either as a single-dataset case study or as a leaderboard that aggregates across many tasks and datasets. EEG-FM-Bench (Xiong et al., 2025), AdaBrain-Bench (Wu et al., 2025), EEG-Bench (Kastrati et al., 2025), and Brain4FMs (Shen et al., 2026) report dozens of task–dataset cells and broadly converge on the observation that FMs are not uniformly superior across clinical cross-subject tasks (Aristimunha et al., 2025): AdaBrain-Bench reports that on clinical monitoring tasks “foundation models perform comparable or even worse than traditional models” (Wu et al., 2025). An independent review of ten early EEG-FMs reaches a parallel conclusion at the methodology level: that evaluation strategies across the field remain heterogeneous and limited, and that standardized, scaled evaluations are a prerequisite for assessing practical off-the-shelf utility (Kuruppu et al., 2025). Their taxonomies are organized along axes orthogonal to ours (task category, pretraining objective, or fine-tuning strategy), and none ask which physiological component of the EEG spectrum the learned representation aligns with. Three FMs and four datasets, selected _a priori_ to span complementary labeling outcomes, support representation-level diagnostics that read each pair against the literature-fixed properties the cell carries. 

## **3 Methods** 

This section covers the sampling layout, feature extraction and evaluation protocol, the fine-tuning recipe, and the five FMScope diagnostics. 

### **3.1 The** 2 _×_ 2 **sampling layout** 

We assign the four datasets a priori to a 2 _×_ 2 layout cross-classifying (a) subject relation of the label and (b) consensus cross-subject marker. _Axis A_ is read from dataset structure: **within-subject paired** when each subject contributes recordings under both classes (EEGMAT, SleepDep) versus **subject-label trait** when the label is fixed per subject (ADFTD; Stress under per-recording DASS-21 binarization (Lovibond and Lovibond, 1995)). For Stress, 14 of 17 subjects carry a single label across all their recordings; the 3 mixed-cutoff subjects are kept for the headline benchmark and dropped from any mechanistic diagnostic that requires a subject-level label. _Axis B_ is a literature-anchored a priori expectation. The **consensus** column comprises labels for which prior peer-reviewed EEG work has established a replicable cross-subject signature: frontal-midline _θ_ and parieto-occipital _α_ modulation for mental arithmetic (EEGMAT; (Klimesch, 1999; Gevins et al., 1997; Klimesch, 2012)), and posterior _α_ peak-frequency reduction for AD/FTD (ADFTD; (Babiloni et al., 2021) expert-panel consensus). The **no-consensus** column comprises labels for which no such signature has been replicated: chronic stress (Stress; frontal alpha asymmetry contested, (Reznik and Allen, 2018; van der Vinne et al., 2017)) and sleep deprivation (SleepDep; the dataset paper reports no candidate cross-subject EEG marker, (Xiang et al., 2024)). The 2 _×_ 2 layout is fixed before any FM is trained, and we state its falsifiable consequence in advance: fine-tuning should amplify label-variance preferentially in consensus cells (tested in Sec. 4.4). Tab. 1 summarizes the assignment. 

### **3.2 Per-dataset specifications** 

All four datasets are small- _N_ ( _N ≤_ 65) resting-state (or rest-plus-task) EEG at 19–30 channels, 200 Hz after per-dataset resampling. We standardize preprocessing across cells: per-channel mean subtraction, 1–45 Hz 

Preprint 

7 

Table 1: **Dataset assignment to the** 2 _×_ 2 **sampling layout.** Rows: subject relation of the label (Axis A, read from dataset structure). Columns: consensus cross-subject marker (Axis B, fixed a priori from peer-reviewed EEG literature under the criterion in Sec. 3.1). Each cell gives the dataset, its literature anchor, and recordings / subjects. 

||**Consensus marker**|**No-consensus marker**|
|---|---|---|
|**Within-subject**<br>**paired**|**EEGMAT**<br>FMT _θ_ + occipital _α_<br>(Klimesch, 1999; Gevins et al., 1997)<br>72 rec / 36 subj|**SleepDep**<br>no replicated marker<br>(Xiang et al., 2024)<br>72 / 36|
|**Subject-label**|**ADFTD**<br>|**Stress (DASS)**|
|**trait**|posterior _α_ peak / power<br>(Babiloni et al., 2021)<br>65 / 65|FAA contested<br>(Reznik and Allen, 2018; van der Vinne et al., 2017)<br>70 / 17|



zero-phase Butterworth band-pass, 5 s non-overlapping epochs. 

**EEGMAT** : 36 subjects _×_ 72 recordings (3-min eyes-closed rest vs. 1-min serial-subtraction arithmetic); 19-channel 10–20 montage (Zyma et al., 2019); within-subject paired, consensus marker. **ADFTD** : 65 subjects (AD = 36, HC = 29), one recording per subject (Miltiadous et al., 2023); restricted to AD vs. HC for Axis B alignment with the AD-specific prior (Babiloni et al., 2021); 19-channel 10–20 montage; subject-label trait, consensus marker. **SleepDep** : the dataset of Xiang et al. (2024) has 71 participants; 38 of them contributed an eyes-closed recording. We use that eyes-closed subset and exclude 2 subjects whose session files are corrupted, leaving 36 subjects _×_ 72 recordings (baseline vs. 24 h sleep deprivation); 19-channel; within-subject paired, no-consensus marker. **Stress-DASS** : 17 subjects _×_ 70 recordings with per-recording DASS-21 self-report (Komarov et al., 2020); 30-channel; subject-label trait, no-consensus marker. 

### **3.3 Foundation model feature extraction and per-FM input normalization** 

We evaluate three open-weight EEG foundation models spanning complementary pretraining objectives and tokenization strategies: LaBraM (Jiang et al., 2024), CBraMod (Wang et al., 2025a), and REVE (El Ouahidi et al., 2025). Each backbone receives a 5 s by _C_ -channel input at 200 Hz and emits a pooled embedding: a single fixed-length vector summarizing that 5 s window, of dimension _d ∈{_ 200 _,_ 200 _,_ 512 _}_ depending on the backbone. The backbone determines the pooling rule, and we do not re-pool the data. LaBraM and CBraMod both produce their embedding by mean pooling over encoder output tokens: LaBraM averages patch tokens after stripping a prepended classification (CLS) token (matching the release-default head described in Jiang et al., 2024 §2.1), and CBraMod applies 2D adaptive average pooling over the (channel, patch) grid (one of the head variants provided in the CBraMod release). REVE returns the attention-pooling secondary-task token (a learnable query that attends over all channel–patch tokens, per El Ouahidi et al., 2025 §2.4). 

**Input normalization.** All three backbones receive raw microvolt-scale input and each applies its releasedefault internal rescaling before its patch embedding. We hold the input contract fixed across cells and do not sweep it. 

**Feature extraction modes.** Frozen linear probe (LP) freezes the backbone (no gradient) and passes the pooled embedding through a percentile-based clip (fit per dimension on each fold’s training data), a standard scaler, and an _L_ 2-penalized logistic regression with balanced class weights, all held at fixed canonical values. Per-window posterior probabilities are mean-pooled within a recording and thresholded at 0 _._ 5 to produce the recording-level decision; the threshold is fixed by design and not tuned. Full fine-tuning (FT) unfreezes the backbone and adds a single linear classification head trained end-to-end under the recipe in Sec. 3.5. All three backbones expose the same interface. They take a multi-channel EEG epoch as input and return a pooled embedding, so the training loop is backbone-agnostic. 

Preprint 

8 

### **3.4 Evaluation protocol** 

**Primary protocol: subject-disjoint 5-fold CV.** All cells report balanced accuracy (BA), defined as the unweighted mean of per-class recall, which we use because the cells are class-imbalanced. Cross-validation is subject-stratified group _K_ -fold with _K_ = 5, grouped by subject so that no subject contributes recordings to both the train and test folds of a given split (Brookshire et al., 2024). We aggregate at the recording level by averaging per-window posteriors within a recording, thresholding at 0 _._ 5, and comparing to the recording label. This is the single evaluation rule used for the sampling layout axis B classification and the baseline performance table (Tab. 2). 

**Multi-seed requirement.** Small- _N_ cells exhibit non-trivial seed-to-seed FT variability under deterministic cuDNN. We average every balanced accuracy claim over three FT training seeds (seeds _{_ 42 _,_ 123 _,_ 2024 _}_ ) and report it as mean _±_ sample standard deviation; LP additionally averages over a fixed eight-seed set. Wide confidence intervals reflect the inherent instability of fine-tuning on small- _N_ cohorts; the relative performance gaps between tiers remain consistent across seeds. 

### **3.5 Fine-tuning configuration** 

Each foundation model is fine-tuned under the configuration published in its original repository, applied uniformly across the four cells; we do not run a per-dataset hyperparameter sweep. All three FMs share the AdamW optimizer, the cross-entropy loss with label smoothing, early stopping on a moving-average of held-out balanced accuracy, and a single linear classification head with two output units. LaBraM additionally uses the small-scale head initialization prescribed in its release (Jiang et al., 2024). 

### **3.6 Reference baselines (classical and non-FM-deep)** 

Two reference baselines situate the FM tier in Tab. 2. 

**Classical handcrafted-feature baseline.** A per-recording feature vector is built from the time-averaged power spectrum (Welch, _n_ perseg = min(256 _, T_ )): for each channel, mean band-power in _θ_ (4–8 Hz), _α_ (8–13 Hz) and _β_ (13–30 Hz); per-channel _θ/α_ and _θ/β_ ratios; and frontal/parietal alpha-asymmetry log _Pα_<sup>right</sup> _−_ log _Pα_<sup>left</sup> over six electrode pairs (Fp1/Fp2, F3/F4, F7/F8, C3/C4, P3/P4, O1/O2). At 19 channels this yields 5 _×_ 19 + 6 = 101 features. We fit _L_ 2-regularized logistic regression with feature standardization, inverse regularization strength _C_ = 1, and balanced class weights, under the same subject-disjoint 5-fold CV, three seeds. 

**Non-FM-deep baselines.** Four convolutional / hybrid architectures trained from scratch on raw EEG: EEGNet (Lawhern et al., 2018), ShallowConvNet and DeepConvNet (Schirrmeister et al., 2017), and EEGConformer (Song et al., 2023). Each is trained per dataset under the same CV splits and seeds, with _z_ -score input normalization (matching the early-BatchNorm convention used in standard implementations of these architectures). No foundation-model pretrained weights are used. 

### **3.7 Diagnostic method specifications** 

FMScope comprises five frozen-representation diagnostics, organized by the question each answers. Two of these establish the Identity Trap itself: whether subject identity dominates the representation (variance decomposition, Sec. 3.7.1) and whether that dominance is confined to a linearly removable axis (subject-axis erasure, Sec. 3.7.2). The other three characterize its origin and structure: its spectral carrier (aperiodic ablation, Sec. 3.7.3), the depth at which it becomes linearly separable (layer-wise probe, Sec. 3.7.4), and whether subjects encode the task contrast along a shared direction (direction consistency, Sec. 3.7.5). Each diagnostic carries a scope condition stating the cells in which it returns a defined answer and is read only where that scope is met, so a cohort need not exercise all five. 

Preprint 

9 



<!-- Start of picture text -->
Phase I Phase II Phase III<br>Characterize subject-driven variance Detailed Mechanism Diagnostic Integrated report<br>Variance Decomposition Layer-wise probing<br>Quantify dominance Localize the depth at<br>of subject-specific which identity emerges<br>variance in  Integrated report<br>embedding space.<br>FOOOF Ablation Converge diagnostics<br>Frozen  into per-cell assignment<br>embeddings Pinpoint spectral carrier<br>Subject-axis erasure that contains identity.<br>(LEACE)<br>Test if identity is Direction consistency<br>confined to a<br>removable linear Check if subjects share<br>space a common contrast axis<br><!-- End of picture text -->

Figure 2: **FMScope diagnostic pipeline.** The framework evaluates frozen representations from EEG foundation models across three sequential phases. **Phase I** establishes the existence of the Identity Trap by quantifying subject-variance dominance and testing its linear removability via least-squares concept erasure (LEACE). **Phase II** characterizes the underlying mechanisms using three tools: localizing the depth of subject-identity emergence (layer-wise probing), isolating the physiological carrier via spectral input ablation (FOOOF), and evaluating task-axis alignment across subjects (direction consistency). **Phase III** synthesizes these diagnostic outputs into an integrated report, converging on a final cell-level verdict for the specific cohort-model pair. 

**3.7.1 Variance decomposition of frozen representations** For each (dataset, FM) we decompose per-window embedding variance via a crossed two-factor sum-of-squares partition with label and subject as factors; this is the marginalization step of demixed PCA (Kobak et al., 2016). 

SStotal _≈_ SSlabel + SSsubject + SSresidual _,_ (1) 

where, for a factor _g ∈{_ label _,_ subject _}_ with groups indexed by _c_ , we compute the between-group SS marginally over the other factor as 



with<sup>¯</sup> **f** _c_ the per-group mean embedding,<sup>¯</sup> **f** the grand mean, _nc_ the group window count, and SSresidual obtained by subtraction and clipped at zero. We operate at the window level so the partition is defined for single-session trait cells (ADFTD: each recording yields _≥_ 2 windows). Cluster-bootstrap CIs over subjects ( _B_ = 2 _,_ 000) preserve the within-subject correlation structure (Field and Welsh, 2007). Reading the partition is cell-conditional. In within-subject paired cells the two factors are orthogonal so the fractions sum to _<_ 1; in trait cells the subject factor structurally contains the label factor, which naturally allows the marginal fractions to sum to _>_ 1 because they represent overlapping variance components. We therefore emphasize the within-cell label-fraction shift (FT _−_ frozen) rather than absolute fractions. Let _f_ label = SSlabel _/_ SStotal and _f_ subj = SSsubject _/_ SStotal denote the label- and subject-variance fractions; throughout, ∆denotes the change after the relevant intervention (here fine-tuning; in Sec. 3.7.3, aperiodic removal), so ∆ _f_ label is the FT _−_ frozen change in label-variance fraction and ∆ _f_ subj is the analogous change in subject-variance fraction. Scope condition: all cells; for Stress the 3/17 mixed-cutoff subjects are dropped, leaving a 14-subject strict-trait subset. 

Preprint 

10 

**Column-effect test on** ∆ _f_ label **.** Across the 12 (cell, FM) pairs we contrast the 6 consensus-marker pairs against the 6 no-consensus pairs on ∆ _f_ label using a one-sided Mann–Whitney U test; the test is non-parametric and distribution-free, appropriate for the small sample. The 12 pairs share data within cell (cell-level _n_ = 4 with 3 FMs nested per cell), so we read U as an effect-size summary (we report the rank-biserial _r_ in the Results) rather than as axis-level inference. 

#### **3.7.2 Subject-axis erasure** 

Variance decomposition measures how much of the representation subject identity occupies; erasure tests whether that identity is confined to a removable linear axis and at what cost to the clinical label. We apply LEACE (Belrose et al., 2023), least-squares concept erasure: the minimum-displacement affine map that renders a target concept linearly unpredictable. For per-window embeddings **X** and one-hot subject labels **Z** , LEACE removes the subspace spanned by **W** Σ **XZ** , with **W** = Σ<sup>_−_</sup> **XX**<sup>1</sup><sup>_/_2</sup> the whitening transform, which we estimate under Ledoit–Wolf shrinkage for numerical conditioning. Centred one-hot labels for _k_ subjects span _k −_ 1 dimensions, so the erased subspace has rank _k −_ 1: it is the between-subject-mean subspace. After erasure no linear classifier recovers subject identity above chance; the guarantee is linear only, so we report the identity still recoverable by a nonlinear probe (a one-hidden-layer MLP) alongside it. The map is undefined when _k −_ 1 _≥ d_ , where the subject subspace fills the feature space; we test this condition and skip the cell when it holds. To quantify the cost of erasure to the task, we re-run the recording-level label probe (Sec. 3.7.3) on the erased features and report ∆erase, the change in label balanced accuracy. Scope condition: all cells for the erasure and nonlinear-residual read-out. ∆erase is interpretable only in within-subject paired cells, where the label varies within subject and is therefore separable from the erased between-subject subspace; in trait cells the label is a per-subject constant whose class-mean direction lies inside the subject subspace, so erasure removes it by construction and ∆erase is undefined. It is read only where the un-erased baseline also clears chance. 

#### **3.7.3 Spectral Anchor Ablation (FOOOF)** 

We intervene on the EEG via FOOOF ablation, which modifies the spectral shape (aperiodic background vs. periodic peaks) while preserving frequency support, and observe how the FM’s frozen probe responds. 

For each recording we fit a per-channel FOOOF decomposition (Donoghue et al., 2020) on the 1–45 Hz band, parameterizing the log-power spectrum as 



where _b_ is an offset, _χ_ (Greek chi) the aperiodic exponent (slope of 1 _/f_ on log-log axes; higher _χ_ means relatively more low-frequency power), and each _Gn_ ( _f_ ) a Gaussian peak in log-power. With _X_ ( _f_ ) the perchannel FFT, _A_<sup>ˆ</sup> ( _f_ ) = 10<sup>_L_(</sup><sup>_f_)</sup><sup>_/_2</sup> the fitted aperiodic amplitude envelope, and _Pn_ ( _f_ ) = _A_<sup>ˆ</sup> ( _f_ )<sup>2</sup> (10<sup>_Gn_(</sup><sup>_f_)</sup> _−_ 1) the linear-power contribution of peak _n_ , we construct three phase-preserving reconstructions 



each combined with the original phase spectrum and inverted via FFT. Each reconstruction is re-extracted through the FM and probed with two diagnostics. The label probe is a binary _L_ 2-penalized logistic regression on per-window features under subject-stratified group _K_ -fold ( _K_ = 5). The pipeline matches the LP recipe (percentile clip + standard scaler) and aggregates to the recording level by mean-pooling per-window posteriors; balanced accuracy is averaged over 8 seeds (the LP seed set). The subject-identity probe is a multi-class classifier of subject identity (one class per subject) under a 5-fold _temporal-block_ protocol: per subject, the windows are concatenated across recordings in canonical order and split into 5 contiguous blocks; 

Preprint 

11 

fold _f_ tests block _f_ from every subject and trains on the remaining four blocks. The classifier is linear discriminant analysis with Ledoit–Wolf shrinkage of the within-class covariance toward a scaled identity matrix. The shrinkage stabilizes the covariance estimate when the number of windows per subject is small. The classifier uses a closed-form solver with no stochastic optimization, so we run it at a single seed. Per-fold balanced accuracy is averaged across the 5 folds. On multi-recording cells (EEGMAT, SleepDep, Stress) the blocks cross recording boundaries, so the probe also tests whether the subject signal is stable across sessions. ADFTD has only one recording per subject by design, so its blocks are always within a single recording. 

**FT extension.** To extend the intervention from the frozen representation to the fine-tuned representation, we re-extract and fine-tune each backbone end-to-end on the ablated input under the same recipe as Sec. 3.5 and run both probes (state and subject) on the resulting test-fold per-window features concatenated across the 5 CV folds. Per (cell, FM, condition) we average ∆probe BA = ablated minus original input over 3 fine-tuning seeds; the FT extension covers both conditions (aperiodic-removed and periodic-removed). Output. The diagnostic returns a per-cell 1 _/f_ -role reading derived from the joint change in label-probe BA and subject-probe BA under aperiodic removal, where each ∆is computed as aperiodic-removed minus original. 

Scope condition: all four cells for the label probe and subject probe at frozen and FT representations. 

**3.7.4 Layer-wise probe** 

To localize the depth at which subject identity emerges within the encoder, we replay each FM’s forward pass with eight intermediate-depth captures and apply the same two read-outs used elsewhere in the paper (temporal-block subject-ID probe; canonical recording-level linear probe with three CV seeds) at every captured depth. Pooling at each captured depth uses the backbone’s own canonical scheme, so the final-depth row reproduces the main-paper frozen feature to numerical precision. 

Scope condition: all four cells for both probes. 

#### **3.7.5 Within-subject direction and signal-to-noise characterization** 

For within-subject paired cells we measure (i) whether subjects encode the state contrast along a consistent direction in FM feature space, and (ii) whether per-subject contrast magnitudes separate from cross-subject heterogeneity. For each subject _s_ we form the per-subject contrast vector 



where<sup>¯</sup> **f** _s,y_ is the window-mean embedding for subject _s_ under label class _y_ . The within-subject direction consistency index _c_ ¯ (WSCI) is the mean pairwise cosine similarity across the _n_ per-subject contrast vectors, 



high _c_ ¯ implies a shared cross-subject axis, _c_ ¯ _≈_ 0 implies idiosyncratic directions. The per-subject SNR is a signal-to-noise ratio of mean contrast magnitude _σs_ = _∥_ **∆** _s∥_ to its cross-subject standard deviation, 



_c_ ¯ and SNR together characterize direction agreement and magnitude-vs-noise; we do not compose them into a single assessment. Scope condition: within-subject paired cells only (EEGMAT, SleepDep); marked inapplicable in trait cells. 

**Within-cell label-structure detector (cosine PERMANOVA).** _c_ ¯ is undefined in trait cells (no within-subject contrast) and uninterpretable when subjects do not share a direction ( _c_ ¯ _≈_ 0). To detect whether a label-associated signature exists in feature geometry, independent of whether subjects share a 

Preprint 

12 

contrast direction, we run PERMANOVA (Anderson, 2001) on the cosine dissimilarity matrix of per-window embeddings. The design factor is the labeling unit (subject for ADFTD; recording within pair block for EEGMAT and SleepDep; recording for Stress). We use 999 permutations per (cell, FM, state), giving a floor of _p ≈_ 0 _._ 001. We read PERMANOVA as a within-cell test for whether label-related geometric structure exists at all, not as the axis-level consensus-vs-no-consensus contrast (which is reported on ∆ _f_ label in Sec. 3.7.1). Scope condition: all four cells. Per-cell assessments are tabulated in App. C. 

## **4 Results** 

The Results proceed in four steps. We start with the baseline performance picture: full fine-tuning rarely improves over a frozen linear probe (Sec. 4.1). To see what fine-tuning starts from, we then characterize the frozen representation itself; subject identity dominates, and the encoder amplifies it into a linearly separable direction within its first few transformer blocks (Sec. 4.2). A natural next question is which input feature carries that subject identity. The aperiodic 1 _/f_ background is one such carrier on LaBraM and CBraMod (Sec. 4.3). Sec. 4.4 summarizes the per-cell evidence for the final assessment. 

### **4.1 Baseline performance and the fine-tuning paradox** 

Tab. 2 reports subject-disjoint balanced accuracy across the four cells under three FMs (linear probe and full fine-tuning), four convolutional / hybrid baselines trained from scratch, and a classical handcrafted-feature LogReg. 

Table 2: **Subject-disjoint 5-fold CV balanced accuracy across the four cells.** Rows: classical handcrafted-feature LogReg, four non-FM deep baselines, and three foundation models under linear probe (LP) and full fine-tuning (FT). Columns ordered by the four-cell layout. Values are 3-seed mean with sample std (seeds _{_ 42 _,_ 123 _,_ 2024 _}_ ); **bold** = global best within column. Method details: Sec. 3.5. 

|**Method**|**Strategy**|**EEGMAT**<br>_within×consensus_|**ADFTD**<br>_trait×consensus_|**SleepDep**<br>_within×no-consensus_|**Stress**<br>_trait×no-consensus_|
|---|---|---|---|---|---|
|Classical LR|–|**0.847**_±_**0.050**|0.587_±_0.004|0.542_±_0.037|0.506_±_0.019|
|EEGNet|–|0.671_±_0.042|0.793_±_0.016|0.500_±_0.014|**0.545**_±_**0.059**|
|ShallowConvNet|–|0.699_±_0.008|0.788_±_0.041|0.505_±_0.040|0.476_±_0.031|
|DeepConvNet|–|0.602_±_0.021|0.773_±_0.038|0.482_±_0.095|0.524_±_0.066|
|EEGConformer|–|0.676_±_0.032|0.792_±_0.021|0.514_±_0.048|0.530_±_0.045|
|LaBraM|LP|0.755_±_0.070|**0.814**_±_**0.023**|0.542_±_0.037|0.464_±_0.032|
||FT|0.718_±_0.032|0.769_±_0.045|0.546_±_0.045|0.429_±_0.063|
|CBraMod|LP|0.708_±_0.037|0.751_±_0.010|0.542_±_0.050|0.440_±_0.019|
||FT|0.694_±_0.014|0.772_±_0.042|0.481_±_0.049|0.438_±_0.024|
|REVE|LP|0.755_±_0.021|0.762_±_0.017|**0.556**_±_**0.024**|0.497_±_0.019|
||FT|0.727_±_0.021|0.796_±_0.009|0.542_±_0.061|0.491_±_0.015|



Fine-tuning rarely beats the frozen linear probe: 10 of 12 pairs fall within _±_ 1 pp of the corresponding LP. ADFTD is the one cell where FM pretraining yields a measurable advantage over the classical and non-FM-deep baselines. On EEGMAT the classical RF beats every FM tier. On Stress and SleepDep all four tiers fall within a 0 _._ 43–0 _._ 57 band. The Wang _et al._ 0 _._ 9047 Stress headline (Wang et al., 2025b) does not reproduce under subject-disjoint cross-validation; the gap is _∼_ 45 pp. 

### **4.2 Subject-dominant baseline geometry** 

We decompose per-window frozen and fine-tuned features into label, subject, and residual variance components (Sec. 3.7.1; Fig. 3). The frozen subject-variance fraction is 13–89 _×_ a matched random-Gaussian null in 12 

Preprint 

13 



<!-- Start of picture text -->
EEGMAT SleepDep<br>(Within-subject × consensus marker) (Within-subject × no consensus marker)<br>100 null  f subj  ≈ 2.05% null  f subj  ≈ 0.83%<br>75<br>2.6<br>9.7 4.6 0.3 0.3 0.3<br>50<br>0.5<br>1.3 1.1 1.8 0.5 2.2<br>25<br>frz FT frz FT frz FT frz FT frz FT frz FT<br>0<br>LaBraM CBraMod REVE LaBraM CBraMod REVE<br>ADFTD Stress (DASS)<br>(Subject/label-trait × consensus marker) (Subject/label-trait × no consensus marker)<br>100 13.3 10.7 null  f subj  ≈ 0.66% 5.2 2.2 null  f subj  ≈ 0.29%<br>75 6.6 5.5 2.6<br>2.5<br>4.6<br>50<br>25 2.9 1.4 2.1<br>frz FT frz FT frz FT frz FT frz FT frz FT<br>0<br>LaBraM CBraMod REVE LaBraM CBraMod REVE<br>subject_frac label_frac frozen fine-tuned null subject_frac<br>variance explained (%)<br>variance explained (%)<br><!-- End of picture text -->

Figure 3: **Variance decomposition across the four cells.** Window-level subject and label fractions for frozen and fine-tuned features. Stacked bars: subject (lower) + label (upper); gap to 100% is residual. Dashed red line marks the matched random-Gaussian null _f_ subj (mean over 20 seeds; per-cell numeric callout in each panel). Frozen subject fraction exceeds the null by 13–89 _×_ across 12 (cell, FM) pairs; under fine-tuning, subject fraction rises in 12 of 12 pairs (largest on Stress: +32 / +63 / +43 pp on LaBraM / CBraMod / REVE), while label fraction rises only in cells with a consensus cross-subject marker (per-pair values in Tab. A1; null-control values in Tab. A2). 

of 12 (cell _×_ FM) pairs (per-pair values in Tab. A2); fine-tuning increases the subject fraction in all 12 pairs (+10 to +63 pp, largest on Stress), while ∆ _f_ label is positive in 6 of 6 consensus-marker pairs (+0 _._ 6 to +8 _._ 4 pp) and spans zero in 6 of 6 no-consensus pairs ( _−_ 1 _._ 9 to +0 _._ 8 pp). The two ∆ _f_ label ranges do not overlap (one-sided Mann–Whitney U on the 12 values: _p_ = 0 _._ 0022, rank-biserial _r_ = +0 _._ 94; Sec. 3.7.1). 

This subject dominance is a removable linear axis, not diffuse structure (Tab. 3). Closed-form erasure (Sec. 3.7.2) drives the linear subject probe to chance in all 12 pairs. A nonlinear probe still recovers part of the identity, substantial for REVE, which we report alongside. Whether removing the axis helps the task can be asked only in within-subject paired cells, where the label varies within subject. On EEGMAT, the one such cell with an above-chance baseline, the frozen probes start below the classical baseline (0 _._ 847); erasure lifts all three FMs and closes this gap, with LaBraM reaching 0 _._ 875. On SleepDep (no-consensus, near-chance baseline) the change is small and inconsistent across FMs, as expected when little label signal is present. This is a single clean demonstration; App. E extends it to five further cohorts with a within-subject contrast, where ∆erase stays positive on all three consensus-marker cohorts and turns mixed-to-negative on the two without an established marker (positive in 12 of 12 consensus cell _×_ FM values including the primary cell; one-sided sign test _p_ = 2 _._ 4 _×_ 10<sup>_−_4</sup> ). 

A layer-wise re-probe (Sec. 3.7.4; Fig. 4) shows that the subject axis becomes linearly decodable inside the encoder rather than at the embedding output: the encoder actively amplifies subject identity into a separable 

Preprint 

14 

Table 3: **Subject-axis erasure on frozen features.** BA _×_ 100; chance = 100 _/k_ ; erased subspace rank = _k −_ 1. Subject BA is a linear subject classifier before and after erasure; nonlinear residual is an MLP after erasure (LEACE guarantees linear erasure only). ∆erase is the change in recording-level label BA (3 seeds, mean _±_ SD), defined only in within-subject paired cells; trait cells (ADFTD, Stress) are marked “—” because the label is a fixed subject attribute lying inside the subject subspace. 

|**Cell**|**FM**|**Subj. pre**|**Subj. post**|**Nonlin.**|∆erase|
|---|---|---|---|---|---|
||LaBraM|79.6|0.0|1.6|+12_._0_±_7_._4|
|EEGMAT|CBraMod|70.5|0.0|2.5|+6_._0_±_3_._3|
||REVE|99.5|0.0|3.3|+7_._4_±_0_._7|
||LaBraM|93.4|0.3|1.5|—|
|ADFTD|CBraMod|90.6|0.3|1.4|—|
||REVE|99.4|0.6|11.5|—|
||LaBraM|73.2|0.1|4.3|+1_._9_±_0_._7|
|SleepDep|CBraMod|73.2|0.4|5.5|+0_._9_±_4_._7|
||REVE|97.3|1.1|56.4|+7_._4_±_2_._9|
||LaBraM|64.7|4.2|6.9|—|
|Stress|CBraMod|59.0|4.0|5.2|—|
||REVE|98.0|5.3|40.0|—|



direction within its first two to three blocks. The label probe is cell-conditional; the per-cell trajectories feed the per-cell assessment in Sec. 4.4. 

### **4.3 Aperiodic** 1 _/f_ **as a subject-identity carrier** 

We intervene on the input EEG via FOOOF spectral-shape ablation (aperiodic background versus periodic peaks; frequency support preserved) and observe the FM probe response (Sec. 3.7.3; Fig. 5). 

**Removing the aperiodic** 1 _/f_ **component drops the subject probe uniformly on LaBraM and CBraMod.** On LaBraM and CBraMod, FOOOF _−_ aperiodic drops the linear subject probe BA by 9 to 19 pp across all four cells (per-(cell, FM) values in Tab. A4; LaBraM: _−_ 18 _._ 4 / _−_ 10 _._ 9 / _−_ 17 _._ 9 / _−_ 9 _._ 1 pp on EEGMAT / ADFTD / SleepDep / Stress; CBraMod: _−_ 18 _._ 9 / _−_ 10 _._ 2 / _−_ 17 _._ 1 / _−_ 9 _._ 3 pp). The drop is large, uniform across cells of very different paradigms, and goes in the same direction on both FMs. 

REVE’s baseline subject probe is already at _≥_ 0 _._ 93 BA and shifts by _≤_ 1 _._ 2 pp under _−_ aperiodic; we therefore limit the aperiodic-anchor claim to LaBraM and CBraMod (Sec. 5.5). FOOOF _−_ periodic shows no effect across all 12 (cell, FM) pairs ( _≤_ 0 _._ 8 pp on both probes). Because both ablations pass through the same FOOOF decompose-and-invert reconstruction (Eq. 4) and differ only in which component is removed, this _−_ periodic null rules out the reconstruction round-trip itself as the cause and attributes the _−_ aperiodic drop to the removed aperiodic content. The label-probe response under _−_ aperiodic is cell-conditional and feeds the per-cell 1 _/f_ role column of Tab. 4. 

**The same intervention extends to the fine-tuned representation.** To test whether FT inherits the frozen aperiodic dependence, we re-extracted and fine-tuned each FM end-to-end on both ablated inputs under the same recipe as the baseline run (3 seeds; Sec. 3.7.3) and recomputed both probes on the resulting features (Fig. 5b, bottom row). On LaBraM and CBraMod, the FT subject probe drops under _−_ aperiodic on 7 of 8 (cell, FM) pairs (mean ∆ranging from _−_ 4 to _−_ 20 pp, with the per-seed range staying below zero). LaBraM _×_ ADFTD is the borderline case ( _−_ 2 _._ 0 _±_ 4 _._ 7 pp). This is consistent with two properties of that cell: its frozen subject probe is already near ceiling, and its high recording-level redundancy gives the encoder multiple non-aperiodic carriers to amplify. _−_ Periodic at the FT level shifts the subject probe by _|_ ∆ _| ≤_ 2 _._ 5 pp on all 8 (cell, LaBraM/CBraMod) pairs, matching the frozen null and confirming that the FT carrier is the 1 _/f_ component, not narrowband peaks. REVE’s FT subject probe shifts by _|_ ∆ _| ≤_ 2 _._ 5 pp on every cell under both ablations, preserving the negative control at the FT representation. 

Preprint 

15 



<!-- Start of picture text -->
consensus marker no consensus marker<br>EEGMAT SleepDep<br>1.00<br>0.75<br>0.50<br>0.25<br>0.00<br>ADFTD Stress<br>1.00<br>0.75<br>0.50<br>0.25<br>0.00<br>0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0<br>Relative transformer depth Relative transformer depth<br>subject-ID probe label probe<br>within-subject paired<br>Probe balanced accuracy<br>subject-label trait<br>Probe balanced accuracy<br><!-- End of picture text -->

Figure 4: **Layer-wise subject and label probes.** Rows show the subject relation of the label (within-subject paired on top, trait on the bottom); columns show the consensus axis (consensus on the left, no-consensus on the right). Each panel shows two probes: the temporal-block subject-ID probe (red) and the canonical recording-level label probe (blue). Lines are the mean across the three FMs (LaBraM, CBraMod, REVE); shaded bands span their min–max range ( _n_ = 3 FMs, an envelope rather than a confidence interval). The horizontal axis is relative transformer depth (0 is post-embedding pre-block; 1 is the final pooled feature). Across all four cells the subject probe rises toward 0 _._ 55–0 _._ 99 within two to three transformer blocks; the wide early-depth band reflects FMs that reach this ceiling at different depths. The label probe is cell-conditional. Dotted lines mark label chance (0 _._ 5) and the per-cell subject-ID chance. 

### **4.4 Cell-conditional label-side outcomes** 

Two cell-level diagnostics remain. The layer-wise label-probe trajectory shows how much label-aligned variance survives to the final pooled feature, and the within-subject direction-consistency test asks whether subjects share a contrast axis at all. The combined assessment matrix appears with the Discussion (Tab. 4). 

**Layer-wise label-probe trajectory** (Sec. 3.7.4; Fig. 4). On EEGMAT, the label probe is stable across depth (0 _._ 69–0 _._ 78) for all three FMs. On ADFTD, the label probe peaks early (relative depth _∼_ 0 _._ 17, BA 0 _._ 78–0 _._ 83) and descends as later blocks compress along the subject axis without further label gain. On SleepDep, the label probe is flat near chance (0 _._ 50–0 _._ 59) at every depth. On Stress, the label probe descends monotonically with depth on all three FMs (LaBraM 0 _._ 49 _→_ 0 _._ 42; CBraMod 0 _._ 49 _→_ 0 _._ 36; REVE 0 _._ 47 _→_ 0 _._ 41): the modest label-aligned signal in the pre-block embedding does not survive to the final pooled feature. 

**Within-subject direction consistency** (Sec. 3.7.5; Fig. 6). EEGMAT yields group-level mean pairwise ¯ cosine _c ∈_ [+0 _._ 07 _,_ +0 _._ 15] across three FMs (subjects share a contrast axis above the isotropic null). SleepDep yields _c_ ¯ _≈_ 0 (subjects do not share a contrast axis); cosine PERMANOVA (Sec. 3.7.5; App. C, Tab. A3) still detects label-associated structure on every (FM, state) pair ( _p ≤_ 0 _._ 001). A local per-subject contrast 

Preprint 

16 



<!-- Start of picture text -->
EEGMAT SleepDep Stress ADFTD<br>10 1<br>10 0<br>10 0 10 1<br>10 0<br>10 −2<br>10 −2 10 0 10 −1<br>10 0 10 1 10 0 10 1 10 0 10 1 10 0 10 1<br>Freq (Hz) Freq (Hz) Freq (Hz) Freq (Hz)<br>PSD aperiodic fit periodic peaks<br>(a)<br>LABRAM CBRAMOD REVE<br>10 10 10<br>5 5 5<br>0 0 0<br>−5 −5 −5<br>−10 −10 −10<br>10 10 10<br>5 5 5<br>0 0 0<br>−5 −5 −5<br>−10 −10 −10<br>−40 −20 0 20 40 −40 −20 0 20 40 −40 −20 0 20 40<br>Δ Subject probe BA (pp) Δ Subject probe BA (pp) Δ Subject probe BA (pp)<br>−aperiodic −periodic EEGMAT SleepDep Stress ADFTD<br>(b)<br>/Hz)<br>2<br>V<br>μ<br>PSD (<br>[Frozen]<br>Δ State probe BA (pp)<br>[FT, intervention]<br>Δ State probe BA (pp)<br><!-- End of picture text -->

Figure 5: **Aperiodic and periodic ablation of the input, frozen and intervention-FT. (a)** Representative log-log power spectrum per cell with FOOOF decomposition: black solid, measured PSD; orange dashed, 1 _/f_ aperiodic fit; blue shading, periodic peaks (PSD minus aperiodic). The aperiodic fit defines the input ablation (Sec. 3.7.3). **(b)** ∆probe BA under FOOOF ablation; circles mark _−_ aperiodic, squares mark _−_ periodic, a line within each FM connects the two conditions per cell, colour codes the cell; top row frozen, bottom row FT (intervention, 3-seed mean). Frozen: FOOOF _−_ aperiodic on LaBraM and CBraMod uniformly drops the subject probe by 9 to 19 pp across all four cells; _−_ periodic shifts probe BA by _≤_ 0 _._ 8 pp on every (FM, cell) combination; REVE’s already-saturated subject probe ( _≥_ 0 _._ 93 baseline) shows no measurable aperiodic dependence. FT (intervention): re-extracting and fine-tuning under aperiodic-removed input attenuates the FT subject probe on 7 of 8 (cell, FM) pairs for LaBraM/CBraMod ( _−_ 4 to _−_ 20 pp); LaBraM _×_ ADFTD is borderline ( _−_ 2 _._ 0 _±_ 4 _._ 7 pp). _−_ Periodic FT shifts the subject probe by _|_ ∆ _| ≤_ 2 _._ 5 pp on every (cell, LaBraM/CBraMod) pair, mirroring the frozen null and locating the FT effect in the 1 _/f_ component rather than narrowband peaks. REVE’s FT bottom-row shifts _|_ ∆ _| ≤_ 2 _._ 5 pp on every cell under both ablations, preserving the negative control downstream. Cell-conditional label-probe response is interpreted in the main text. 

Preprint 

17 



<!-- Start of picture text -->
LaBraM CBraMod REVE<br>θ EEGMAT  = 64° θ EEGMAT  = 64° θ EEGMAT  = 61°<br>θ Sleepdep  = 80° θ Sleepdep  = 76° θ Sleepdep  = 77°<br>90° 90° 90°<br>135° 45° 135° 45° 135° 45°<br>180° 0° 180° 0° 180° 0°<br>EEGMAT SleepDep<br>(a)<br>frozen FT frozen FT<br>0.4<br>0.3 3<br>0.2 2<br>0.1<br>1<br>0.0<br>0<br>LaBraM CBraMod REVE LaBraM CBraMod REVE<br>(b) (c)<br>)<br>s<br>c ( σ<br>s<br> / SD<br>s<br>σ<br>Directional Consistency<br>Per-subject SNR<br><!-- End of picture text -->

Figure 6: **Within-subject direction and SNR (frozen vs. FT).** For each subject the contrast vector _vi_ = _µi,_ 1 _− µi,_ 0 is formed in the FM’s full feature space; the group consensus is _vc_ = _<u>vi/∥vi</u>_ _~~∥~~_ . Filled gray = EEGMAT, outlined black = SleepDep. **(a)** Polar half-circle rose (frozen), one panel per FM: _θi_ = arccos _⟨vi, vc⟩_ ; 0<sup>_◦_</sup> aligns, 90<sup>_◦_</sup> is the high-dimensional isotropic null. **(b)** Group-level ¯ _c_ (Eq. 6) across 3 FMs _×_ 2 within-subject paired cells, frozen vs. FT. Trait cells (Stress, ADFTD) lack within-subject contrast by design. **(c)** Per-subject SNR (Eq. 7); dashed line at SNR = 1 (signal _∼_ noise). 

exists but does not generalize across subjects (per-cell assessment in Tab. 4). We read these four outcomes as different sides of a single representation bottleneck (Sec. 5). 

## **5 Discussion** 

The empirical core of this paper is the Identity Trap: across four small- _N_ clinical resting-state cohorts, subject identity dominates the frozen features of all three EEG-FMs we test, and standard fine-tuning amplifies this subject geometry in 12 of 12 (cell, FM) pairs while amplifying label geometry only in cells where prior literature has already established a cross-subject EEG marker. On two of the three FMs, the aperiodic 1 _/f_ background is one identifiable carrier of this subject axis. The four cells map onto four distinct outcomes (Tab. 4), but they share a single representation bottleneck rather than acting as four unrelated cases. 

Preprint 

18 

Table 4: **Cross-diagnostic results and per-cell assessment.** Numeric summary of FMScope’s four diagnostics per cell. All values are the arithmetic mean across the three foundation models (LaBraM, CBraMod, REVE); per-FM values appear in Tab. A1 (∆ _f_ label), Fig. 4 (layer probe), Fig. 6 ( _c_ ¯), and Tab. A4 (1 _/f_ ablation drops). Columns: ∆ _f_ label = FT minus frozen label-explained variance fraction; _layer probe BA max / last_ = max and last-layer balanced accuracy of the layer-wise label probe; _c_ ¯ = median within-subject direction-consistency (“—” in trait cells where no within-subject paired contrast exists); 1 _/f drops state / subj_ = drops in label-state and subject-identity probe BAs after aperiodic-component ablation (positive values mean the ablated component carried that signal). _Outcome_ is the qualitative cell-level reading (Sec. 4.4); the four outcomes are exhaustive over the 2 _×_ 2 cell layout: W = within-subject paired, T = subject-label trait, C = consensus cross-subject marker, N = no consensus marker. 

|**Cell**|∆_f_label|**layer p**<br>**max**|**robe BA**<br>**last**|¯_c_|1_/f_ **drops**<br>**state / subj**|**Outcome**|
|---|---|---|---|---|---|---|
|EEGMAT _(W, C)_|+0_._043|0_._77|0_._74|+0_._16|+0_._04_/_+ 0_._13|**Cross-subject-aligned**|
|ADFTD _(T, C)_|+0_._041|0_._82|0_._78|—|+0_._00_/_+ 0_._07|**Label–subject coupled**|
|SleepDep _(W, N)_|_−_0_._008|0_._58|0_._55|+0_._01|_−_0_._04_/_+ 0_._12|**Idiosyncratic within-subject**|
|Stress _(T, N)_|+0_._003|0_._50|0_._40|—|_−_0_._01_/_+ 0_._06|**Below linear-probe resolution**|



### **5.1 The representation bottleneck** 

FM features carry stable subject geometry more strongly than task-aligned variance, and fine-tuning reinforces this ordering rather than correcting it. The frozen-state evidence has three parts. The subject-variance fraction is 13–89 _×_ a matched random-Gaussian null in 12 of 12 frozen pairs (Tab. A2); the layer-wise probe shows that the subject axis becomes linearly decodable within the first two to three transformer blocks rather than at the embedding output, so the encoder actively amplifies subject identity into a separable direction; and closed-form subject-axis erasure confirms this dominance sits on a removable linear axis, collapsing the linear subject probe to chance in every pair (Tab. 3). On LaBraM and CBraMod, the aperiodic 1 _/f_ background is one identifiable carrier: removing it drops the linear subject probe by 9 to 19 pp uniformly across all four cells. REVE shows no measurable aperiodic dependence; the design-axis differences between REVE and the LaBraM-plus-CBraMod group are listed in Sec. 5.5. 

Fine-tuning then amplifies whatever subject axis it inherits. ∆ _f_ subj is positive in every pair (+10 to +63 pp), whereas ∆ _f_ label is positive in 6 of 6 consensus-marker pairs (+0 _._ 6 to +8 _._ 4 pp) and spans zero in the 6 no-consensus pairs. When no literature-supported cross-subject marker is available for FT to amplify toward, FT still adapts, but what it adapts toward is the subject axis. This connects to a recurring caution in the EEG-FM literature. Subject-disjoint critiques (Brookshire et al., 2024) establish that trial-level splits inflate accuracy via subject identity. Our diagnostic addresses the next concern: even under subject-disjoint splitting, subject-correlated features can still survive the split. The bottleneck here is not opaque feature noise; it is the stable presence of a single identifiable component in the input signal. Prior work identifies subject-disjoint splitting as a necessary protocol; we show that this protocol alone is not sufficient for clinical discovery if the model instead aligns its features with stable subject traits. FMScope provides a representation-level account of this persistent failure. 

### **5.2 Spectral-bias amplification under random-head fine-tuning** 

We interpret the cell-conditional amplification asymmetry through a gradient-geometry reading, now supported on LaBraM and CBraMod by the FT row of Fig. 5b. Fine-tuning concentrates supervised signal along whichever direction already carries the most variance in the pretrained representation, regardless of whether that direction aligns with the supervised objective. Across 12 (cell, FM) pairs, ∆ _f_ subj is positive in every case (+10 to +63 pp), and the largest amplifications fall in the no-consensus trait cell where Stress reaches +32 to +63 pp on the three FMs. ∆ _f_ label is positive in 6 of 6 consensus-marker pairs (+0 _._ 6 to +8 _._ 4 pp) and spans 

Preprint 

19 

zero in the 6 no-consensus pairs ( _−_ 1 _._ 9 to +0 _._ 8 pp). This asymmetry is what we expect if FT acts on existing axes: subject-axis amplification is universal because that axis is large in every frozen representation, whereas label-axis amplification depends on whether a label-aligned axis is already large enough to be amplified at all. Under a randomly initialized classification head, this gradient-geometry reading has formal anchors: linear probing then fine-tuning analyses show that LP induces a linear-head-norm regime that preserves the backbone’s pretrained feature directions during the subsequent FT stage (Tomihari and Sato, 2024), and parameter-efficient adaptation directions that capture the most activation variance provably maximize the expected gradient signal (Paischer et al., 2024). These results combine with classical linear-network results showing that gradient descent preferentially learns the largest-singular-value directions of the input–output correlation (Saxe et al., 2019). The prescription that follows from this combination is layer-localized finetuning keyed to shift type (Lee et al., 2023). Our variance fractions correspond to the marginalization step of demixed PCA (Kobak et al., 2016), the established systems-neuroscience predecessor of factor-wise variance accounting. 

### **5.3 A coding pattern shared across modalities** 

Our finding sits between two adjacent observations, neuroscience-side fingerprinting and ML-side shortcut learning, which converge on the same operational competition between stable biometric structure and unstable task signal. Our diagnostic documents the Identity Trap as a specific dissociation: subject variance dominates the frozen features, label variance is subordinate, and on LaBraM and CBraMod the aperiodic 1 _/f_ background is one identifiable subject carrier. The same dissociation between stable subject structure and task signal is documented across resting-state fMRI fingerprinting and EEG biometrics (Sec. 2); we show it holds inside EEG-FM representations as well, using variance decomposition as the test. The broader observation that deep networks exploit dataset-stable shortcut features over invariant discriminative cues (Geirhos et al., 2020) supplies the cross-architecture frame. Our diagnostic in turn provides a physically-grounded instance of that phenomenon in biosignal foundation models: the shortcut here is not a pure statistical artifact of the training corpus but has a measurable physiological component of the input (the aperiodic 1 _/f_ background), highenergy, cross-session stable, and easier to reconstruct than the clinical signal the model is nominally trained to support. Concurrent prescriptive work on cross-subject EEG/MEG-FM adaptation includes SuLoRA, which decomposes each weight matrix into a shared component and a per-subject low-rank correction (Klein et al., 2025), and SCOPE, a prototype-guided adaptation framework for label-limited EFM fine-tuning (Ma et al., 2026). Both prescribe a fix (adding subject-specific parameters or prototypes) without measuring the subject axis they adapt to, and neither relates it to a physiological component of the signal. Our diagnostic is complementary and upstream: it quantifies the axis in the frozen feature space, shows it is removable in closed form, and identifies one physiological carrier. Both adaptation methods are evaluated on within-subject task contrasts or consensus-marker datasets; whether they extend to the no-consensus column, which we predict to be intractable, remains open. 

### **5.4 Implications and FMScope use** 

We draw three deployment-side implications from the assessment matrix. The pre-pilot frozen-feature pass is a cheap filter: when the assessment falls below linear-probe resolution (Stress on all three FMs), the bottleneck lies in the recording substrate itself (an information deficit) rather than in model capacity. Scaling the pretraining corpus or model size does not address this class of failure; the remedy lies in how the data are collected, not in the model. Trait-cell labels collected within a single session conflate disease state with stable subject features (aperiodic 1 _/f_ being one identifiable carrier on LaBraM and CBraMod). To separate the two, the label must change within a subject. Only then does its discriminative axis fall outside the between-subject subspace that LEACE erases. Some labels allow this: when the underlying state changes over time, recording each subject under both conditions captures the variation. Other labels do not: a dementia diagnosis is a fixed subject attribute, so no recording protocol can separate it from identity. For these labels the entanglement is irreducible at the representation level, and the discriminative features must instead be validated as physiological rather than biometric. Scaling model capacity helps in neither case. 

Preprint 

20 

Brain–computer-interface calibration claims should pass a within-subject direction-consistency check before any subject-independent generalization is asserted; a cell like SleepDep, where contrasts are idiosyncratic within each subject, can support high in-subject calibration accuracy with near-zero cross-subject transfer. These assessments also depend on reading the diagnostics jointly: the SleepDep assessment is recoverable only from the disagreement pattern across tools, not from any single one. Building on the established subject-disjoint splitting culture in EEG (Brookshire et al., 2024; Lotte et al., 2018), the assessment matrix turns this into a frozen-feature pre-pilot test: whether the features show the geometric signatures (subject dominance, aperiodic anchoring, axis disagreement) that predict cross-subject failure before any fine-tuning compute is committed. 

### **5.5 Limitations and scope** 

We note five limitations to the present claims. _(i)_ Our 2 _×_ 2 layout relies on one dataset per cell; consequently, although the FMScope framework is generalizable, the specific cell-level clinical observations remain empirical features of these four cohorts and await broader validation. _(ii)_ All four cells are small by machine-learning standards (Stress _N_ = 17 subjects; EEGMAT and SleepDep _N_ = 36; ADFTD _N_ = 65); we mitigate seed sensitivity with 3-seed FT and 8-seed LP, but per-cell confidence intervals are wide and pointwise comparisons across cells are descriptive. The Mann–Whitney U is computed across 12 (cell _×_ FM) points drawn from four independent cells; the column claim rests on the non-overlapping effect-size ranges (+0 _._ 6 to +8 _._ 4 pp vs _−_ 1 _._ 9 to +0 _._ 8 pp), which the test summarizes. _(iii)_ Our ablations are input-level interventions; they establish statistical entanglement between aperiodic 1 _/f_ and subject identity, not a causal mechanism. The aperiodic-anchor effect holds on LaBraM and CBraMod but not on REVE, and these two groups differ along at least five concurrent design axes that we cannot factorially separate in an N=3 model panel: (a) the presence of spectral processing in the pretraining pipeline (LaBraM’s encoder targets discrete codes whose decoder reconstructs Fourier amplitude+phase; CBraMod’s patch embedding adds an FFT-derived branch to a temporal CNN; REVE operates on raw signal throughout); (b) reconstruction loss (CBraMod’s MSE versus REVE’s explicitly motivated L1, chosen by El Ouahidi et al. (2025) to avoid L2 amplification of high-amplitude EEG content); (c) pretraining corpus diversity (REVE’s 25,000 subjects across 92 heterogeneous datasets versus CBraMod’s _∼_ 15 _,_ 000 subjects from a single clinical source); (d) positional encoding (REVE’s 4D Fourier sinusoidal versus learned or convolutional alternatives); (e) an attention-pooling secondary task that REVE adds and the other two omit. We therefore report the two-versus-one pattern descriptively, not as a mechanism claim; an architecture-level controlled ablation would be required to isolate any single axis. _(iv)_ All analyses assume subject-disjoint cross-validation, recording-level labels, and a _≥_ 19-channel 10–20 montage; cells with finer label resolution or trial-level splitting may produce different readings. The DASS-21 self-report on Stress (Lovibond and Lovibond, 1995) is a past-week screener, and we adopt the per-recording binarization of Komarov et al. (2020) for cross-protocol comparability with Wang et al. (2025b); our subject-disjoint numbers reproduce that work’s protocol-side configuration but apply each FM’s release-default fine-tuning recipe rather than a per-dataset hyperparameter sweep. _(v)_ Single-session ADFTD cannot separate disease state from stable subject traits by data alone. The diagnosis is a fixed subject attribute and does not change within a subject, so collecting more sessions would not separate them either. For such labels the limit is intrinsic, and the discriminative features must be validated against external physiological evidence rather than addressed with more recordings. We did not pre-align signals using Riemannian or Euclidean alignment methods before fine-tuning. This engineering step may attenuate the subject-axis amplification and is a natural follow-up, but it is not a prerequisite for the diagnostic claim itself. 

### **5.6 Future directions** 

We see three algorithmic directions following from the bottleneck reading: FOOOF-detrended pretraining (the causal test of whether aperiodic 1 _/f_ is the masked objective’s primary subject carrier), explicit gradientreversal objectives at fine-tuning (Ganin and Lempitsky, 2015) that could augment existing general-purpose SSL pretraining recipes for EEG (Banville et al., 2021; Kostas et al., 2021), and explicit cross-subject alignment regularization at pretraining. On the empirical side, replication with a second dataset per cell, a 

Preprint 

21 

layer-wise FOOOF-aperiodic probe, a broader FM panel that varies the five design axes independently, and a within-subject paired protocol on a no-consensus label would sharpen the present descriptive observations into axis-level claims. Integrating FMScope-style diagnostics into large-scale community benchmarks (Aristimunha et al., 2025; Kastrati et al., 2025; Shen et al., 2026) would complement leaderboard accuracy with a representation-level check that distinguishes models rewarded for learning clinical biomarkers from those rewarded for optimizing subject-specific aperiodic anchors. The diagnostic framework we report here characterizes the substrate; pretraining-objective work is the path that moves the substrate. 

## **6 Conclusion** 

Subject-disjoint cross-validation is necessary but not sufficient for representation discovery in small- _N_ clinical resting-state EEG. Across the 12 (cell, FM) pairs we examined, the frozen embedding already placed subject identity on its largest-variance direction, and fine-tuning amplified that direction whether or not the label aligned with it; a high accuracy is therefore consistent either with a transferable clinical biomarker or with subject identity that merely co-varies with the label in this cohort, and accuracy alone cannot separate the two. FMScope is a frozen-feature pre-flight check, complementary to subject-disjoint splitting, that tells the user before any fine-tuning whether a cell’s representation carries label-aligned biological structure or subject identity dressed up as a label. Where it signals an information deficit rather than a capacity limit, the remedy is methodological: a within-subject label should be recorded under both conditions so that its discriminative axis separates from between-subject identity, whereas a label fixed at the subject level cannot be disentangled by any protocol, and its discriminative features must instead be shown to correspond to an independently established physiological marker rather than to incidental subject traits. The framework generalizes; the per-cell outcomes are empirical features of these four cohorts and three FMs, and broader validation awaits future cohorts. 

## **Data availability** 

This study uses four previously collected EEG datasets. EEGMAT (Zyma et al., 2019) is available from PhysioNet ( `https://physionet.org/content/eegmat/1.0.0/` ); the ADFTD dataset (Miltiadous et al., 2023) is available from OpenNeuro (ds004504); the sleep-deprivation rsEEG dataset (Xiang et al., 2024) is available as published by the original authors. The resting-state stress dataset (Komarov et al., 2020) is not currently deposited in a public repository; it was shared by the originating laboratory (co-author T.-P. Jung’s group) for the present secondary analysis and is available from the authors upon reasonable request and with permission from the original investigators. No new data were collected. 

## **Code availability** 

The FMScope toolkit, comprising the five frozen-representation diagnostics used in this paper (variance decomposition, subject-axis erasure, aperiodic FOOOF ablation, layer-wise probe, and within-subject direction consistency), together with the exact scripts that reproduce every table and figure, is available at `https: //github.com/Jimmy110101013/fmscope` . Reproduction runs from bundled aggregate results and frozenfeature caches, without raw EEG or model weights. Pretrained foundation-model weights (LaBraM, CBraMod, REVE) are obtained from the respective original repositories and are not redistributed by this work. 

## **Ethics statement** 

This work uses previously collected, de-identified EEG datasets. EEGMAT, ADFTD, and the sleep-deprivation dataset are publicly released; the Komarov et al. stress dataset was obtained from the original investigators (co-author T.-P. Jung’s lab) for secondary analysis. The original data-collection studies were conducted under their respective IRB approvals and consent procedures, which we cite. No new human-subject data were 

Preprint 

22 

collected, and no additional IRB approval was required. 

## **Conflict of interest** 

The authors declare no competing interests. 

## **Funding** 

This work received no external funding. 

## **Author contributions** 

J.-Y.L.: conceptualization, methodology, software, formal analysis, investigation, data curation, writing — original draft, writing — review and editing, visualization. T.-P.J.: supervision, conceptual input, writing — review and editing. 

## **Appendix** 

## **A Variance decomposition: per-pair values** 

Window-level variance decomposition, full per-(cell, FM) values for the 12 frozen and 12 fine-tuned pairs underlying Sec. 4.2 and Fig. 3. ∆columns are FT minus frozen. 

Table A1: Per-pair label-fraction and subject-fraction values (window-level variance decomposition). Frozen and FT in percentage points; ∆= FT _−_ frozen. 

|**Cell**|**FM**|**Froze**|**n %**|**FT **|**%**|∆|**(pp)**|
|---|---|---|---|---|---|---|---|
|||label|subj|label|subj|label|subj|
||LaBraM|1.3|26.8|9.7|45.4|+8_._4|+18_._6|
|EEGMAT|CBraMod|1.1|29.6|2.6|60.3|+1_._5|+30_._7|
||REVE|1.8|29.7|4.6|50.0|+2_._9|+20_._3|
||LaBraM|6.6|55.4|13.3|78.9|+6_._6|+23_._5|
|ADFTD|CBraMod|5.5|58.8|10.7|81.6|+5_._2|+22_._8|
||REVE|4.6|46.5|5.2|80.5|+0_._6|+34_._0|
||LaBraM|0.5|30.8|0.3|51.3|_−_0_._1|+20_._4|
|SleepDep|CBraMod|0.5|39.3|0.3|49.4|_−_0_._3|+10_._1|
||REVE|2.2|32.4|0.3|51.2|_−_1_._9|+18_._7|
||LaBraM|2.9|20.7|2.5|52.8|_−_0_._5|+32_._0|
|Stress|CBraMod|1.4|18.5|2.2|81.2|+0_._8|+62_._7|
||REVE|2.1|20.7|2.6|64.0|+0_._5|+43_._3|



The ∆ _f_ label column-effect Mann–Whitney (method: Sec. 3.7.1) operates on the 12 ∆label values above. Cosine PERMANOVA per-cell assessments are reported in App. C. 

## **B Random-Gaussian null control for the Identity-Trap inequality** 

The raw inequality _f_ subj _> f_ label on a crossed sum-of-squares decomposition is combinatorially guaranteed whenever the number of subjects _S_ exceeds the number of labels _L_ : for an iid Gaussian embedding with _N_ rows the marginal sum-of-squares fractions converge to their degrees of freedom, E[ _f_ subj] _≈_ ( _S−_ 1) _/_ ( _N −_ 1) and E[ _f_ label] _≈_ ( _L−_ 1) _/_ ( _N −_ 1), with _S > L_ for every cell in our panel. We therefore quantify the Identity-Trap 

Preprint 

23 

evidence as the _excess of the frozen f_ subj _over a matched random-Gaussian null_ of identical shape ( _N, D_ ), averaged over _K_ = 20 seeds. Tab. A2 reports per-pair excess ratios; the empirical null mean agrees with the closed-form ( _S−_ 1) _/_ ( _N −_ 1) prediction to three decimal places. 

Table A2: Frozen subject-variance fraction (real FM vs. matched random-Gaussian null of identical shape) for the 12 (cell, FM) pairs. _N_ is the number of windows, _S_ the number of subjects, _L_ = 2 for every cell. “Null _f_ subj” is the mean _±_ SD over _K_ = 20 iid Gaussian draws; “df pred” is the closed-form ( _S−_ 1) _/_ ( _N −_ 1); “Excess _×_ ” is real / null mean. ∆ _f_ label (Tab. A1) is intrinsically null-corrected because the combinatorial offset cancels in the frozen-to-FT difference. 

|**Cell**|**FM**|_N_|_S_<br>**Real**|_f_subj **(%)**|**Null** _f_subj **(%)**|**df pred (%)**|**Excess **|**(**_×_**)**|
|---|---|---|---|---|---|---|---|---|
||LaBraM|1707|36|26.85|2.04_±_0.02|2.05||13.2|
|EEGMAT|CBraMod|1707|36|29.56|2.06_±_0.03|2.05||14.3|
||REVE|1707|36|29.74|2.05_±_0.03|2.05||14.5|
||LaBraM|9701|65|55.40|0.66_±_0.01|0.66||83.9|
|ADFTD|CBraMod|9701|65|58.76|0.66_±_0.01|0.66||89.3|
||REVE|9701|65|46.49|0.66_±_0.01|0.66||70.4|
||LaBraM|4207|36|30.83|0.84_±_0.01|0.83||36.7|
|SleepDep|CBraMod|4207|36|39.27|0.83_±_0.02|0.83||47.3|
||REVE|4207|36|32.45|0.83_±_0.01|0.83||39.1|
||LaBraM|4421|14|20.75|0.29_±_0.01|0.29||70.7|
|Stress|CBraMod|4421|14|18.46|0.30_±_0.01|0.29||62.6|
||REVE|4421|14|20.69|0.29_±_0.00|0.29||70.1|



## **C Cosine PERMANOVA: per-cell label-structure detection** 

Per-cell PERMANOVA _p_ -values on the variance-triangulation cache (method: Sec. 3.7.5). 

Table A3: Cosine PERMANOVA _p_ label per cell _×_ FM _×_ state. Floor _≈_ 0 _._ 001 (999 permutations). EEGMAT, ADFTD, and SleepDep clear the floor on every (FM, state) cell; Stress is null on every cell. 

|**Cell**|**FM**|**Frozen** _p_|**FT** _p_|
|---|---|---|---|
||LaBraM|0.001|0.001|
|EEGMAT|CBraMod|0.001|0.001|
||REVE|0.001|0.001|
||LaBraM|0.001|0.001|
|ADFTD|CBraMod|0.004|0.001|
||REVE|0.001|0.002|
||LaBraM|0.001|0.001|
|SleepDep|CBraMod|0.001|0.001|
||REVE|0.001|0.001|
||LaBraM|0.165|0.647|
|Stress|CBraMod|0.477|0.957|
||REVE|0.417|0.933|



PERMANOVA on SleepDep is significant on every (FM, state) pair even though ∆ _f_ label is negative across all three FMs. This is consistent with the within-subject paired design: each pair block is anchored to one subject, and the per-pair contrast leaves a label-detectable signature in the cosine geometry whether 

Preprint 

24 

or not fine-tuning amplifies it. We therefore use PERMANOVA as a within-cell detector of label-related structure rather than as the axis-level test; the consensus-vs-no-consensus contrast is given by the ∆ _f_ label Mann–Whitney U above. On Stress, PERMANOVA shows no effect on any (FM, state) pair, which supports the below-linear-probe-resolution assessment (Tab. 4) without relying on the layer-wise probe alone. 

## **D FOOOF aperiodic / periodic ablation: full probe BA table** 

Label and subject probe baseline BAs and ablation deltas for the 4 cells _×_ 3 FMs underlying Sec. 4.3 and Fig. 5. The subject probe is a 5-fold temporal-block LDA with Ledoit–Wolf shrinkage. All values in BA _×_ 100; ∆values in percentage points. 

Table A4: Label probe and subject probe baseline BA, with deltas under FOOOF _−_ aperiodic and _−_ periodic. Label probe: subject-disjoint 5-fold logistic regression on per-window features. Subject probe: 5-fold temporalblock LDA. ∆values are ablation BA minus baseline BA. 

|**Cell**|**FM**|**L**|**abel pro**|**be**|**Su**|**bject pr**|**obe**|
|---|---|---|---|---|---|---|---|
|||base|∆aper.|∆per.|base|∆aper.|∆per.|
||LaBraM|76.2|_−_8_._3|_−_0_._4|87.6|_−_18_._4|+0_._1|
|EEGMAT|CBraMod|70.7|_−_1_._0|+0_._2|92.6|_−_18_._9|_−_0_._1|
||REVE|75.7|_−_2_._8|_−_0_._0|99.0|_−_0_._2|+0_._0|
||LaBraM|80.7|_−_2_._8|+0_._3|88.3|_−_10_._9|_−_0_._0|
|ADFTD|CBraMod|74.7|+3_._1|+0_._5|92.8|_−_10_._2|+0_._2|
||REVE|79.5|_−_0_._1|_−_0_._1|99.3|+0_._1|+0_._0|
||LaBraM|55.7|+2_._8|_−_0_._3|78.9|_−_17_._9|_−_0_._1|
|SleepDep|CBraMod|54.9|+6_._9|+0_._0|86.1|_−_17_._1|_−_0_._4|
||REVE|55.4|+2_._1|+0_._1|95.6|_−_1_._2|+0_._0|
||LaBraM|42.3|+0_._6|_−_0_._2|67.3|_−_9_._1|_−_0_._0|
|Stress|CBraMod|37.7|+5_._1|+0_._4|73.5|_−_9_._3|+0_._0|
||REVE|39.4|_−_1_._9|+0_._1|92.6|_−_0_._0|+0_._1|



The _−_ aperiodic intervention drops the subject probe by 9–19 pp on LaBraM and CBraMod uniformly across all four cells, while leaving REVE’s already-saturated subject probe (baseline _≥_ 0 _._ 93) unchanged. Periodic peak removal shifts either probe by _≤_ 0 _._ 8 pp on every (FM, cell) pair. Cell-conditional label-probe response is interpreted in Sec. 4.3. 

## **E Subject-axis erasure across independent cohorts** 

The single EEGMAT erasure demonstration generalises. Applying the identical procedure (freeze, LEACEerase the subject subspace, label BA pre/post under subject-level CV) to four further marker families and the five external audit cohorts (Tab. A5), ∆erase is positive on all three FMs wherever a literature-established consensus marker exists — arithmetic _θ_ , motor-imagery ERD, auditory P300 — and mixed-to-negative for the two external cohorts whose markers are not established (SAM40, TDBRAIN-state); the three subject-trait cohorts have ∆erase undefined but show the same subject probe collapse to chance. Magnitudes are not comparable across rows (windows 1–5 s, ceiling effects, recording- vs window-level scoring), but the signs are. Across the twelve consensus-marker cells (four cohorts _×_ three FMs, the primary EEGMAT cell included) ∆erase is positive in all twelve (one-sided sign test _p_ = 2 _._ 4 _×_ 10<sup>_−_4</sup> ; consensus vs. non-consensus cohorts, one-sided Mann–Whitney _U_ , _p_ = 2 _._ 2 _×_ 10<sup>_−_4</sup> ). Erasing identity thus aids the label exactly where a cross-subject marker exists, reinforcing Sec. 4.2 (Tab. 3). 

Preprint 

25 

Table A5: Subject-axis erasure beyond the EEGMAT demonstration (Tab. 3). Raw BA: pre-erasure label BA _×_ 100 (range over the three FMs). ∆erase: post _−_ pre change (pp, 3-seed mean). Top: established consensus markers; bottom: external cohorts with non-established markers. 

|**Cohort**|**Raw BA**||∆erase (pp)||
|---|---|---|---|---|
|||LaBraM|CBraMod|REVE|
|EEGMAT (Zyma et al., 2019)|71–76|+12_._0|+6_._0|+7_._4|
|Test–retest (Wang et al., 2022)|68–78|+4_._2|+4_._4|+13_._9|
|EEGMMIDB (Schalk et al., 2004)|61–73|+17_._5|+8_._3|+26_._7|
|Aud.–Vis. Shift (Ceponiene et al., 2008)|74–86|+24_._2|+21_._6|+14_._4|
|SAM40 (Ghosh et al., 2022)|61–69|_−_5_._2|_−_7_._3|+4_._6|
|TDBRAIN-state (van Dijk et al., 2022)|53–68|_−_7_._9|_−_18_._4|_−_0_._4|



## **References** 

- Marti J. Anderson. A new method for non-parametric multivariate analysis of variance. _Austral Ecology_ , 26 (1):32–46, 2001. 

- Bruno Aristimunha, Dung Truong, Pierre Guetschel, Seyed Yahya Shirazi, Isabelle Guyon, Alexandre R. Franco, Michael P. Milham, Aviv Dotan, Scott Makeig, Alexandre Gramfort, Jean-Remi King, MarieConstance Corsi, Pedro A. Valdés-Sosa, Amit Majumdar, Alan Evans, Terrence J. Sejnowski, Oren Shriki, Sylvain Chevallier, and Arnaud Delorme. EEG foundation challenge: From cross-task to cross-subject EEG decoding. _arXiv preprint arXiv:2506.19141_ , 2025. 

- Claudio Babiloni, Xianghong Arakaki, Hamed Azami, et al. Measures of resting state EEG rhythms for clinical trials in Alzheimer’s disease: Recommendations of an expert panel. _Alzheimer’s & Dementia_ , 17(9): 1528–1553, 2021. doi: 10.1002/alz.12311. 

- Hubert Banville, Omar Chehab, Aapo Hyvärinen, Denis-Alexander Engemann, and Alexandre Gramfort. Uncovering the structure of clinical EEG signals with self-supervised learning. _Journal of Neural Engineering_ , 18(4):046020, 2021. doi: 10.1088/1741-2552/abca18. 

- Nora Belrose, David Schneider-Joseph, Shauli Ravfogel, Ryan Cotterell, Edward Raff, and Stella Biderman. LEACE: Perfect linear concept erasure in closed form. In _Advances in Neural Information Processing Systems (NeurIPS)_ , 2023. 

- Gregory Brookshire et al. Data leakage in deep learning studies of translational EEG. _Frontiers in Neuroscience_ , 2024. doi: 10.3389/fnins.2024.1373515. 

- Patrizio Campisi and Daria La Rocca. Brain waves for automatic biometric-based user recognition. _IEEE Trans. Information Forensics and Security_ , 9(5):782–800, 2014. doi: 10.1109/TIFS.2014.2308640. 

- Rita Ceponiene, Marissa Westerfield, Mara Torki, and Jeanne Townsend. Modality-specificity of sensory aging in vision and audition: Evidence from event-related potentials. _Brain Research_ , 1215:53–68, 2008. doi: 10.1016/j.brainres.2008.02.010. 

- Matteo Demuru and Matteo Fraschini. EEG fingerprinting: Subject-specific signature based on the aperiodic component of power spectrum. _Computers in Biology and Medicine_ , 120:103748, 2020. doi: 10.1016/j. compbiomed.2020.103748. 

- Thomas Donoghue, Matar Haller, Erik J. Peterson, Paroma Varma, Priyadarshini Sebastian, Richard Gao, Torben Noto, Antonio H. Lara, Joni D. Wallis, Robert T. Knight, Avgusta Shestyuk, and Bradley Voytek. Parameterizing neural power spectra into periodic and aperiodic components. _Nature Neuroscience_ , 23: 1655–1665, 2020. 

Preprint 

26 

- Yassine El Ouahidi, Jonathan Lys, Philipp Thölke, Nicolas Farrugia, Bastien Pasdeloup, Vincent Gripon, Karim Jerbi, and Giulia Lioi. REVE: A foundation model for EEG – adapting to any setup with large-scale pretraining on 25,000 subjects. _arXiv preprint arXiv:2510.21585_ , 2025. 

- Christopher A. Field and Alan H. Welsh. Bootstrapping clustered data. _Journal of the Royal Statistical Society: Series B_ , 69(3):369–390, 2007. 

- Emily S. Finn et al. Functional connectome fingerprinting: Identifying individuals using patterns of brain connectivity. _Nature Neuroscience_ , 2015. 

- Yaroslav Ganin and Victor Lempitsky. Unsupervised domain adaptation by backpropagation. In _ICML_ , 2015. 

- Richard Gao, Erik J. Peterson, and Bradley Voytek. Inferring synaptic excitation/inhibition balance from field potentials. _NeuroImage_ , 158:70–78, 2017. 

- Robert Geirhos, Jörn-Henrik Jacobsen, Claudio Michaelis, Richard Zemel, Wieland Brendel, Matthias Bethge, and Felix A. Wichmann. Shortcut learning in deep neural networks. _Nature Machine Intelligence_ , 2(11): 665–673, 2020. doi: 10.1038/s42256-020-00257-z. 

- Alan Gevins, Michael E. Smith, Linda McEvoy, and Daphne Yu. High-resolution EEG mapping of cortical activation related to working memory: effects of task difficulty, type of processing, and practice. _Cerebral Cortex_ , 7(4):374–385, 1997. doi: 10.1093/cercor/7.4.374. 

- Rajdeep Ghosh, Nabamita Deb, Kakuli Sengupta, Achyut Phukan, Nimisha Choudhury, Sayan Kashyap, Souvik Phadikar, Rachita Saha, Pranesh Das, Nidul Sinha, and Paramita Dutta. SAM 40: Dataset of 40 subject EEG recordings to monitor the induced-stress while performing stroop color-word test, arithmetic task, and mirror image recognition task. _Data in Brief_ , 40:107772, 2022. doi: 10.1016/j.dib.2021.107772. 

- Wei-Bang Jiang, Liming Zhao, and Bao-Liang Lu. LaBraM: Large brain model for learning generic representations with tremendous EEG data in BCI. In _International Conference on Learning Representations_ , 2024. 

- Ard Kastrati, Josua Bürki, Jonas Lauer, Cheng Xuan, Raffaele Iaquinto, and Roger Wattenhofer. EEG-Bench: A benchmark for EEG foundation models in clinical applications. In _NeurIPS_ , 2025. arXiv:2512.08959. 

- Timon Klein, Piotr Minakowski, Sebastian Sager, and Steffen Schotthöfer. Mitigating subject dependency in EEG decoding with subject-specific low-rank adapters. _arXiv preprint arXiv:2510.08059_ , 2025. 

- Wolfgang Klimesch. EEG alpha and theta oscillations reflect cognitive and memory performance: a review and analysis. _Brain Research Reviews_ , 29(2-3):169–195, 1999. 

- Wolfgang Klimesch. Alpha-band oscillations, attention, and controlled access to stored information. _Trends in Cognitive Sciences_ , 16(12):606–617, 2012. 

- Dmitry Kobak, Wieland Brendel, Christos Constantinidis, Claudia E. Feierstein, Adam Kepecs, Zachary F. Mainen, Xue-Lian Qi, Ranulfo Romo, Naoshige Uchida, and Christian K. Machens. Demixed principal component analysis of neural population data. _eLife_ , 5:e10989, 2016. doi: 10.7554/eLife.10989. 

- Oleksii Komarov, Li-Wei Ko, and Tzyy-Ping Jung. Associations among emotional state, sleep quality, and resting-state EEG spectra: A longitudinal study in graduate students. _IEEE Transactions on Neural Systems and Rehabilitation Engineering_ , 28(4):795–804, 2020. 

- Martina Kopčanová, Luke Tait, Thomas Donoghue, George Stothart, Laura Smith, Aimee Arely FloresSandoval, Paula Davila-Perez, Stephanie Buss, Mouhsin M. Shafi, Alvaro Pascual-Leone, Peter J. Fried, and Christopher S. Y. Benwell. Resting-state EEG signatures of Alzheimer’s disease are driven by periodic but not aperiodic changes. _Neurobiology of Disease_ , 190:106380, 2024. doi: 10.1016/j.nbd.2023.106380. 

Preprint 

27 

- Demetres Kostas, Stéphane Aroca-Ouellette, and Frank Rudzicz. BENDR: Using transformers and a contrastive self-supervised learning task to learn from massive amounts of EEG data. _Frontiers in Human Neuroscience_ , 15:653659, 2021. doi: 10.3389/fnhum.2021.653659. 

- Gayal Kuruppu, Neeraj Wagh, Vaclav Kremen, Sandipan Pati, Gregory Worrell, and Yogatheesan Varatharajah. EEG foundation models: A critical review of current progress and future directions. _arXiv preprint arXiv:2507.11783_ , 2025. 

- Vernon J. Lawhern, Amelia J. Solon, Nicholas R. Waytowich, Stephen M. Gordon, Chou P. Hung, and Brent J. Lance. EEGNet: a compact convolutional neural network for EEG-based brain-computer interfaces. _Journal of Neural Engineering_ , 15(5):056013, 2018. 

- Yoonho Lee, Annie S. Chen, Fahim Tajwar, Ananya Kumar, Huaxiu Yao, Percy Liang, and Chelsea Finn. Surgical fine-tuning improves adaptation to distribution shifts. In _International Conference on Learning Representations_ , 2023. 

- Fabien Lotte, Laurent Bougrain, Andrzej Cichocki, Maureen Clerc, Marco Congedo, Alain Rakotomamonjy, and Florian Yger. A review of classification algorithms for EEG-based brain–computer interfaces: a 10 year update. _Journal of Neural Engineering_ , 15(3):031005, 2018. doi: 10.1088/1741-2552/aab2f2. 

- Sydney H. Lovibond and Peter F. Lovibond. The structure of negative emotional states: Comparison of the Depression Anxiety Stress Scales (DASS) with the Beck depression and anxiety inventories. _Behaviour Research and Therapy_ , 33(3):335–343, 1995. 

- Jingying Ma, Feng Wu, Yucheng Xing, Qika Lin, Tianyu Liu, Chenyu Liu, Ziyu Jia, and Mengling Feng. SCOPE: Structured prototype-guided adaptation for EEG foundation models with limited labels. _arXiv preprint arXiv:2602.17251_ , 2026. 

- Maron Mantwill, Martin Gell, Stephan Krohn, and Carsten Finke. Brain connectivity fingerprinting and behavioural prediction rest on distinct functional systems of the human connectome. _Communications Biology_ , 5:261, 2022. doi: 10.1038/s42003-022-03185-3. 

- Sébastien Marcel and José del R. Millán. Person authentication using brainwaves (EEG) and maximum a posteriori model adaptation. _IEEE Trans. Pattern Anal. Mach. Intell._ , 2007. 

- Andreas Miltiadous et al. A dataset of scalp EEG recordings of Alzheimer’s disease, frontotemporal dementia and healthy subjects from routine EEG. _Data_ , 2023. 

- Fabian Paischer, Lukas Hauzenberger, Thomas Schmied, Benedikt Alkin, Marc Peter Deisenroth, and Sepp Hochreiter. Parameter efficient fine-tuning via explained variance adaptation. In _Advances in Neural Information Processing Systems_ , 2024. 

- Samantha J. Reznik and John J. B. Allen. Frontal asymmetry as a mediator and moderator of emotion: An updated review. _Psychophysiology_ , 55(1):e12965, 2018. doi: 10.1111/psyp.12965. 

- Andrew M. Saxe, James L. McClelland, and Surya Ganguli. A mathematical theory of semantic development in deep neural networks. _Proceedings of the National Academy of Sciences_ , 116(23):11537–11546, 2019. doi: 10.1073/pnas.1820226116. 

- Gerwin Schalk, Dennis J. McFarland, Thilo Hinterberger, Niels Birbaumer, and Jonathan R. Wolpaw. BCI2000: A general-purpose brain-computer interface (BCI) system. _IEEE Transactions on Biomedical Engineering_ , 51(6):1034–1043, 2004. doi: 10.1109/TBME.2004.827072. 

- Robin Tibor Schirrmeister, Jost Tobias Springenberg, Lukas Dominique Josef Fiederer, Martin Glasstetter, Katharina Eggensperger, Michael Tangermann, Frank Hutter, Wolfram Burgard, and Tonio Ball. Deep learning with convolutional neural networks for EEG decoding and visualization. _Human Brain Mapping_ , 38(11):5391–5420, 2017. 

Preprint 

28 

- Fanqi Shen, Enhong Yang, Jiahe Li, Junru Hong, Xiaoran Pan, Zhizhang Yuan, Meng Li, and Yang Yang. Brain4FMs: A benchmark of foundation models for electrical brain signal. _arXiv preprint arXiv:2602.11558_ , 2026. 

- Yonghao Song, Qingqing Zheng, Bingchuan Liu, and Xiaorong Gao. EEG Conformer: Convolutional transformer for EEG decoding and visualization. _IEEE Trans. Neural Syst. Rehabil. Eng._ , 2023. 

- Ling Tang, Qian Chen, Jilin Mei, Houshi Xu, Quanshi Zhang, Jing Shao, Na Zou, Xia Hu, and Dongrui Liu. What do EEG foundation models capture from human brain signals? _arXiv preprint arXiv:2605.11410_ , 2026. 

- Akiyoshi Tomihari and Issei Sato. Understanding linear probing then fine-tuning language models from NTK perspective. In _Advances in Neural Information Processing Systems_ , 2024. 

- Nikita van der Vinne, Madelon A. Vollebregt, Michel J. A. M. van Putten, and Martijn Arns. Frontal alpha asymmetry as a diagnostic marker in depression: Fact or fiction? a meta-analysis. _NeuroImage: Clinical_ , 16:79–87, 2017. doi: 10.1016/j.nicl.2017.07.006. 

- Hanneke van Dijk, Guido van Wingen, Damiaan Denys, Sebastian Olbrich, Rosalinde van Ruth, and Martijn Arns. The two decades brainclinics research archive for insights in neurophysiology (TDBRAIN) database. _Scientific Data_ , 9(1):333, 2022. doi: 10.1038/s41597-022-01409-z. 

- Jiquan Wang et al. CBraMod: A criss-cross brain foundation model for EEG decoding. _ICLR_ , 2025a. 

- Siwen Wang, Shitou Zhang, Wan-Lin Chen, Dung Truong, and Tzyy-Ping Jung. From theory to application: Fine-tuning large EEG model with real-world stress data. _arXiv preprint arXiv:2505.23042_ , 2025b. 

- Yulin Wang, Wei Duan, Debo Dong, Lihong Ding, and Xu Lei. A test-retest resting, and cognitive state EEG dataset during multiple subject-driven states. _Scientific Data_ , 9(1):566, 2022. doi: 10.1038/ s41597-022-01607-9. 

- Jiamin Wu, Zichen Ren, Junyu Wang, Pengyu Zhu, Yonghao Song, Mianxin Liu, Qihao Zheng, Lei Bai, Wanli Ouyang, and Chunfeng Song. AdaBrain-Bench: Benchmarking brain foundation models for brain-computer interface applications. _arXiv preprint arXiv:2507.09882_ , 2025. 

- Chuqin Xiang, Xinrui Fan, Duo Bai, Ke Lv, and Xu Lei. A resting-state EEG dataset for sleep deprivation. _Scientific Data_ , 11:427, 2024. doi: 10.1038/s41597-024-03268-2. 

- Wei Xiong, Jiangtong Li, Jie Li, Kun Zhu, and Changjun Jiang. EEG-FM-Bench: A comprehensive benchmark for the systematic evaluation of EEG foundation models. _arXiv preprint arXiv:2508.17742_ , 2025. 

- Igor Zyma, Sergii Tukaev, Ivan Seleznov, Ken Kiyono, Anton Popov, Mariia Chernykh, and Oleksii Shpenkov. Electroencephalograms during mental arithmetic task performance. _Data_ , 4(1):14, 2019. PhysioNet EEGMAT dataset. 

