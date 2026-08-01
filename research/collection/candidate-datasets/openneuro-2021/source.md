1 The OpenNeuro resource for sharing of neuroscience data 

- 2 

- 3 Christopher J. Markiewicz<sup>1</sup> ,  Krzysztof J. Gorgolewski<sup>1</sup> , Franklin Feingold<sup>1</sup> , Ross Blair<sup>1</sup> , Yaroslav 4 O. Halchenko<sup>2</sup> , Eric Miller<sup>3</sup> , Nell Hardcastle<sup>3</sup> , Joe Wexler<sup>1</sup> , Oscar Esteban<sup>1, 4</sup> , Mathias 5 Goncalves<sup>1</sup> , Anita Jwa<sup>1</sup> , Russell A. Poldrack<sup>1</sup> 

- 6 

- 7 1. Department of Psychology, Stanford University, Stanford, CA, USA 

- 8 2. Department of Psychological & Brain Sciences, Dartmouth College, Hanover, NH, USA 

- 9 3. Squishymedia, Portland, OR, USA 

- 10 4. Lausanne University Hospital and University of Lausanne, Lausanne, Switzerland 

- 11 Abstract 

- 12 

- 13 The sharing of research data is essential to ensure reproducibility and maximize the impact of 14 public investments in scientific research.  Here we describe OpenNeuro, a BRAIN Initiative data 15 archive that provides the ability to openly share data from a broad range of brain imaging data 16 types following the FAIR principles for data sharing. We highlight the importance of the Brain 17 Imaging Data Structure (BIDS) standard for enabling effective curation, sharing, and reuse of 18 data. The archive presently shares more than 600 datasets including data from more than 19 20,000 participants, comprising multiple species and measurement modalities and a broad 20 range of phenotypes. The impact of the shared data is evident in a growing number of published 21 reuses, currently totalling more than 150 publications.  We conclude by describing plans for 22 future development and integration with other ongoing open science efforts. 

- 23 

#### 24 

# Introduction 

- 25 

- 26 There is growing recognition of the importance of data sharing for scientific progress (National 27 Academies of Sciences, Engineering, and Medicine et al., 2018). However, not all shared data 28 are equally useful.  The FAIR principles (Wilkinson et al., 2016) have formalized the notion that 29 in order for shared data to be maximally useful, they need to be Findable, Accessible, 30 Interoperable, and Reusable.  An essential necessity for achieving these goals is that the data 31 and associated metadata follow a common standard for organization, so that data users can 32 easily understand and reuse the shared data.  Here we describe the OpenNeuro data archive 33 [RRID:SCR_005031], accessible at <u>https://openneuro.org, which enables FAIR-compliant data</u> 34 sharing for a growing range of neuroscience data types (currently including magnetic resonance 35 imaging [MRI], electroencephalography [EEG], magnetoencephalography [MEG], and positron 36 emission tomography [PET]) through the use of a common community standard, the Brain 37 Imaging Data Structure (BIDS) [RRID:SCR_016124] (Gorgolewski et al., 2016). 

- 38 

1 

- 39 Starting with early pioneering efforts by Gazzaniga and Van Horn to establish an fMRI Data 40 Center in 1999 (Van Horn and Gazzaniga, 2013), data sharing has become well established in 41 the domain of neuroimaging (Milham et al., 2018; Poldrack and Gorgolewski, 2014; Poline et al., 42 2012). A major impetus for the growth of data sharing was the International Neuroimaging Data 43 Sharing Initiative (INDI) (Mennes et al., 2013), which published a landmark paper in 2010 44 (Biswal et al., 2010) demonstrating the scientific utility of a large shared resting fMRI dataset. 45 The most prominent recent examples have been large-scale prospective data sharing projects, 46 including the Human Connectome Project [HCP] (Van Essen et al., 2013),  the NKI-Rockland 47 sample (Nooner et al., 2012), Adolescent Brain Cognitive Development (ABCD) study (Casey et 48 al., 2018), and the UK Biobank (Littlejohns et al., 2020). These datasets have provided 49 immense value to the field, and have strongly demonstrated the utility of shared data. However, 50 their scientific scope is necessarily limited, given that each dataset includes only a limited 51 number of imaging tasks and measurement types. Beyond these large focused data sharing 52 projects, there is a “long tail” of smaller neuroimaging datasets that have been collected in 53 service of specific research questions. Making these available is essential to ensure 54 reproducibility as well as to allow aggregation across many different types of measurements in 55 service of novel scientific questions. The OpenNeuro archive addresses this challenge by 56 providing researchers with the ability to easily share a broad range of neuroimaging data types 57 in a way that adheres to the FAIR principles. 

- 58 Goals and principles 

- 59 The OpenNeuro archive evolved from the OpenfMRI archive (Poldrack et al., 2013), which was 60 focused solely on the sharing of task-based human fMRI data. Some of the principles behind 61 OpenNeuro were inherited from OpenfMRI, whereas others grew out of our experiences in that 62 project as well as from new developments in the domain of open science. 

- 63 Minimal restrictions on sharing 

- 64 

- 65 There is a range of restrictiveness across data archives with regard to their data use 66 agreements (Jwa and Poldrack, 2021). At one end of the spectrum are highly restricted 67 databases such as the Alzheimer’s Disease Neuroimaging Initiative (ADNI), which requires 68 researchers to submit their scientific question for review and requires the consortium to be 69 included as a corporate author on any publications. OpenNeuro represents the other pole of 70 restrictiveness, by releasing data (by default) under a Creative Commons Zero (CC0) Public 71 Domain Dedication which places no restrictions on who can use the data or what can be done 72 with them. While not legally required, researchers using the data are expected to abide by 73 community norms and cite the data following the guidelines included within each dataset.  The 74 primary motivation for this policy is that it makes the data maximally accessible to the largest 75 possible number of researchers and citizen-scientists. 

- 76 

2 

### 77 Standards-focused data sharing 

- 78 

- 79 To ensure the utility of shared data for the purposes of efficient discovery, reuse, and 80 reproducibility, standards are required for data and metadata organization. These standards 81 make the structure of the data clear to users and thus reduce the need for support by data 82 owners and curation by repository owners, as well as enabling automated QA, preprocessing, 83 and analytics.  Unfortunately, most prior data sharing projects have relied upon custom 84 organizational schemes, which can lead to misunderstanding and can also require substantial 85 reorganization to adapt to common analysis workflows. The need for a clearly defined standard 86 for neuroimaging data emerged from our experiences in the OpenfMRI project; while the 87 repository had developed a custom scheme for data organization and file naming, this scheme 88 was ad hoc and limited in its coverage, and datasets often required substantial manual curation 89 (involving laborious interaction with data owners).  In addition, there was no way to directly 90 validate whether a particular dataset met the standard. 

- 91 

- 92 For these reasons, we focused at the outset of the OpenNeuro project on developing a more 93 robust data organization standard that could be implemented in an automated validator.  We 94 engaged a large group of researchers from the neuroimaging community to establish a standard 95 that ultimately became the Brain Imaging Data Structure (BIDS) (Gorgolewski et al., 2016), 96 which is now a highly successful community standard for a broad and growing range of 97 neuroimaging data types. BIDS defines a set of schemas for file and folder organization and 98 naming, along with a schema for metadata organization.  The framework was inspired by the 99 existing data organization frameworks used in many research laboratories, so that transitioning 

- 100 to the standard is relatively easy for most researchers.  One of the important features of BIDS is 101 its extensibility; using a scheme inspired by open source software projects, community 102 members can propose extensions to BIDS that encompass new data types. To date, modality 103 extensions include magnetoencephalography (Niso et al., 2018), scalp electroencephalography 104 (Pernet et al., 2019), intracranial EEG (Holdgraf et al., 2019), positron emission tomography 105 (Norgaard et al., 2021), and arterial spin labeling MRI.  In addition to standards for raw data, the 106 BIDS community has also developed a standard for the organization of the outputs of 107 processing operations (known as “BIDS Derivatives”), providing a framework for sharing 108 processed as well as raw data. 

- 109 

- 110 While BIDS and OpenNeuro are now independent projects, there is a strongly synergistic 111 relationship.  All data uploaded to OpenNeuro must first pass a BIDS validation step, such that 112 all data in OpenNeuro are compliant with the BIDS specifications at upload time.   Conversely, 113 the OpenNeuro team has made substantial contributions to the BIDS standard and validator. 114 The BIDS standard has been remarkably successful, with tens of thousands of datasets now 115 available in the format, including but not limited to those contained in the OpenNeuro database. 116 As a consequence, this model maximizes compatibility with processing and analysis tools 117 (Gorgolewski et al., 2017), but more importantly, it effectively minimizes the potential for data 118 misinterpretation (e.g., when owner and re-user have slightly different definitions of a critical 

- 119 acquisition parameter).  Through the adoption of BIDS, OpenNeuro has moved away from 

- 120 project- or database-specific data structures designed by the owner or the distributor (as used in 

3 

121 earlier projects such as OpenfMRI and HCP) and toward a uniform and unambiguous 122 representation model agreed upon by the research community prior to sharing and reuse. 123 

- 124 FAIR sharing 

- 125 

- 126 The FAIR principles (Wilkinson et al., 2016) have provided an important framework to guide the 127 development and assessment of open data resources. OpenNeuro implements each of these 128 principles. 

- 129 

- 130 _Findable_ . Each dataset within OpenNeuro is associated with metadata, both directly from the 131 BIDS dataset along with additional dataset-level metadata provided by the submitter at time of 132 submission. Both data and metadata are assigned a persistent unique identifier (Digital Object 133 Identifier [DOI]). Within the repository, a machine-readable summary of BIDS metadata is 134 collected by the BIDS validator and indexed with an ElasticSearch mapping. In addition, 135 dataset-level metadata are exposed according to the schema.org standard, which allows 136 indexing by external resources such as Google Dataset Search. 

- 137 

- 138 _Accessible_ . Data and metadata can be retrieved using a number of access methods (directly 139 from Amazon S3, using the openneuro command-line tool, or using DataLad) via standard 140 protocols (http/https).  Metadata are also accessible programmatically via a web API. Metadata 141 remain available even in the case that data must be removed (e.g., in cases of human subjects 142 concerns). No authentication is necessary to access the data. 

- 143 

- 144 _Interoperable_ . The data and metadata use the BIDS standard to ensure accessible 145 representation and interoperation with analysis workflows, such as BIDS Apps (Gorgolewski et 146 al., 2017). Ongoing work is extending the metadata representation to use richer formats and to 147 link to relevant FAIR ontologies or vocabularies. 

- 148 

- 149 _Reusable_ . The data are released with a clear data use agreement (currently defaulting to a CC0 150 public domain dedication). Through use of the BIDS standard, the data and metadata are 151 consistent with community standards in the field. 

- 152 

- 153 

- 154 Data versioning and preservation 

- 155 OpenNeuro keeps track of all changes in stored datasets, and allows researchers to 156 unambiguously report the exact version of the data used for any analysis. OpenNeuro preserves 

- 157 all versions of the data through the creation of “snapshots” that unequivocally point to one 

- 158 specific point in the lifetime of a dataset. Data management and snapshots are supported by 

- 159 DataLad (RRID:SCR_003931) (Halchenko et al., 2021), a free and open-source distributed data 160 management system (Hanke et al., 2021). 

- 161 

4 

### 162 Protecting privacy and confidentiality of data 

- 163 164 There is a direct relationship in data sharing between the openness of the data and their reuse 165 potential; all else being equal, data that are more easily or openly available will be more easily 166 and readily reused.  However, all else is not equal, as openness raises concern regarding risks 167 to subject privacy and confidentiality of data in human subjects research. Researchers are 168 ethically bound to both minimize the risks to their research participants (including risks to 169 confidentiality), and to maximize the benefits of their participation (United States. National 170 Commission for the Protection of Human Subjects of Biomedical and Behavioral Research, 171 1978) . Because sharing of data will necessarily increase the potential utility of the data, 172 researchers are ethically bound to share human subject data unless the benefits of sharing are 173 outweighed by risks to the participant (Brakewood and Poldrack, 2013). 

- 174 

- 175 In general, risks to data privacy and confidentiality are addressed through deidentification of the 176 data to be shared. For example, under the Health Insurance Portability and Accountability Act of 177 1996 (HIPAA) in the US, deidentification can be achieved through the removal of any of 18 178 personal identifiers, unless the researcher has knowledge that the remaining data could be re179 identified (known as the “safe harbor” method). With regard to neuroimaging data, a particularly 180 challenging feature is the facial structure that is present in some forms of imaging data, such as 181 structural MRI images. It is often possible to reconstruct facial structures from these images, 182 and there are proofs of concept that such data could be used to re-identify individuals from 183 photographic databases (Schwarz et al., 2019). It is thus essential to remove any image 184 features that could be used to reconstruct facial structure (Bischoff-Grethe et al., 2007).   For 185 this reason, all MRI data shared through OpenNeuro must have facial features removed prior to 186 upload, in addition to the 18 personal identifiers outlined by HIPAA.  An exception is provided in 187 cases where an investigator has explicit permission to openly share the data without defacing, 188 usually when the data are collected by the investigator themself. At present, data are examined 189 by a human curator to ensure that this requirement has been met. In the future, we plan to 190 deploy an automated face detection tool (Bansal et al., n.d.) to detect any uploads that 191 inadvertently contain facial features. 

- 192 

193 Truly informed consent requires that subjects be made aware that their data may be shared 194 publicly, and that confidentiality cannot be absolutely guaranteed in the future.  For this reason, 195 we recommend that researchers planning to share their data via OpenNeuro use a consent form 196 based on the Open Brain Consent (Bannier et al., 2021), which includes language that ensures 197 subject awareness of the intent to share and its potential impact on the risk of participating. Of 198 note, the Open Brain Consent has recently been adapted to include a data usage agreement 199 that accommodates the European Union’s  General Data Protection Regulation (GDPR 200 2016/679); however, data collected in countries covered by GDPR cannot be shared through 201 OpenNeuro at present due to the requirement for restrictive data use agreements that are not 202 currently supported by OpenNeuro. 

5 

### 203 Open source 

204 The entirety of the code for OpenNeuro is available under a permissive open source software 205 license (MIT License) at https://github.com/OpenNeuroOrg/openneuro. This enables any 206 researcher who wishes to reuse part or all of the code or to run their own instance of the 207 platform. 

## 208 Data submission and access 

209 

210 Figure 1 outlines the steps required for sharing a dataset using OpenNeuro. Once shared, data 211 can be accessed by several available mechanisms: 

212 

213 _Web download_ .  Each snapshot is associated with a link that provides immediate downloading 214 of the dataset. 

215 216 _DataLad_ . DataLad (Halchenko et al., 2016) is a decentralized data management system built on 217 top of git and git-annex. Through DataLad, researchers may install a complete copy of a 218 dataset, while deferring the retrieval of file contents until needed, permitting lightweight views of 219 large datasets. OpenNeuro’s versioned snapshots are implemented as git tags, which allows 220 specific versions to be easily retrieved or compared. The decentralized protocol also allows 221 mirrors of the datasets to be hosted on GitHub and <u>https://datasets.datalad.org, ensuring</u> 222 access during service interruptions of the OpenNeuro website. 223 224 _OpenNeuro command line tool_ . The OpenNeuro command line tool provides access to the 225 latest snapshot of all datasets, and is generally more stable than browser downloads for large 226 datasets. 227 228 _Amazon S3_ . The latest snapshot as well as all previous versions of a dataset may be fetched 229 using the Amazon Web Services (AWS) clients or directly via https. 230 

6 

231 232 233 _Figure 1._ A schematic overview of the data upload process. 



234 User support 

235 

236 _Support for individual datasets_ .  Data users sometimes have questions regarding particular 237 datasets. In order to facilitate discussion of these issues and to make those discussions 238 available to the entire community, a discussion forum is provided on each dataset page.  The 239 dataset owner is automatically notified by email of any questions that are posted.  In addition, 240 users can “follow” a dataset of interest and receive notifications of any comments posted to the 241 dataset. 

242 

243 _Site support_ .  Two mechanisms are provided for users of the OpenNeuro site to obtain help with 244 site issues. First, a helpdesk is available directly from the site, through which users can submit 245 specific help questions. Second, users are recommended to post general questions to the 

7 

- 246 Neurostars.org question and answer forum, so that the answers will be available to the entire 247 community. 

## 248 Data processing 

- 249 Data processing was initially envisioned as an incentive for researchers to share their data, and 250 the OpenNeuro site was launched in 2017 with the ability to perform cloud-based data 251 processing using a limited set of analysis workflows.  This feature was disabled in 2018, after an 252 overhaul of the site’s initial storage infrastructure.  At that time, we determined that it would be 253 preferable to collaborate with an existing platform dedicated to cloud processing rather than 254 rebuilding our own execution platform.  At present, OpenNeuro has partnered with the 255 Brainlife.io platform (RRID:SCR_020940), which provides a large set of cloud-based 256 neuroimaging workflows for data analysis and visualization. Data hosted on OpenNeuro can be 257 easily imported into Brainlife for analysis, and more than 400 OpenNeuro datasets are cached 258 for quick access; in the first 6 months of 2021, more than 700 analyses were performed on 259 these datasets. In the future we plan to partner with additional platforms, including the NEMAR 260 platform for EEG/MEG analysis; the availability of the data via DataLad and Amazon S3 also 261 enables any platform to make the data available to their users without requiring any agreement 262 or effort from OpenNeuro. 

# 263 Results 

- 264 Usage and impact 

- 265 The OpenNeuro site was launched in June 2017, and was originally seeded with all of the 266 datasets previously shared through OpenfMRI, after converting them to the BIDS standard.  All 267 data presented below are current as of October 9, 2021. The database contains 604 datasets 268 comprising data from 20,989 individual participants.  Figure 2 shows cumulative figures for 269 numbers of datasets and subjects since 2018, demonstrating sustained and continual growth in 270 the archive since its inception. 

- 271 

8 



272 273 _Figure 2_ : The volume of data available on OpenNeuro has shown a steady growth since its 274 opening started operations in 2017. Shown are figures from July 2018, when all data were 275 migrated to a new DataLad storage backend, through the present date. The green line 276 illustrates the cumulative growth in total number of datasets, and the red line shows the 277 aggregate of subjects (in thousands). 278 

279 The overwhelming majority of datasets are from humans (574 datasets, 95%), with a small but 280 growing number of nonhuman species including mouse (17 datasets), rat (6 datasets), 281 nonhuman primates (2 datasets), dogs (1 dataset), and juvenile pigs (1 dataset).  Table 1 282 presents data for the prevalence of different modalities; while the majority of datasets include 283 some form of MRI data, other supported modalities are present including electrophysiological 284 measures and positron emission tomography. 285 286 

|**Modality**|**Number of datasets**|
|---|---|
|Anatomical MRI|501|
|Functional MRI|445|
|Electroencephalography|81|
|Diffusion-weighted MRI|53|
|Magnetoencephalography|23|



9 

|Positron emission tomography|10|
|---|---|
|Intracranial EEG|8|
|Arterial spin labeling MRI|3|



287 288 _Table 1_ .  Number of datasets by imaging modality; additional modalities present in fewer than 3 289 datasets are not included here. 

290 

291 OpenNeuro is a recommended data repository for a number of publishers and journals, 292 including: Nature Scientific Data, PLOS, eLife, F1000 Research, Gigascience, BioMed Central, 293 American Heart Association, and Wellcome Open Research. The database contains 407 DOIs 294 for publications associated with datasets (including both primary scientific publications and data 295 descriptors). 296 

### 297 Multiple dimensions of “big data” 

- 298 

- 299 Discussions of “big data” in neuroimaging (Poldrack and Gorgolewski, 2014; Smith and Nichols, 300 2018) have largely focused on datasets including large numbers of individuals. While these 301 analyses are essential for robust population inference, it is also important to recognize that large 302 numbers of subjects are only one dimension over which a neuroimaging dataset can be “big”. 303 Here we will define the number of subjects as the “width” of the dataset, the number of different 304 phenotypes measured for each individual as the “breadth” of the dataset, and the number of 305 measurements per individual as the “depth” of the dataset. 

- 306 

307 The OpenNeuro database is distinguished by sharing datasets that are extensive along each of 308 these dimensions (see Figure 3). With regard to width, the median dataset size is 23 subjects, 309 with 31 studies having sample sizes larger than 100, and a maximum sample size of 928.  With 310 regard to breadth, notable datasets include: the BOLD5000 dataset (Chang et al., 2019), which 311 includes data from subjects viewing a total of 5000 natural images; the Individual Brain Charting 312 dataset (Pinho et al., 2020, 2018), which includes data from individuals each completing 24 313 different tasks, and the Multidomain Task Battery dataset (King et al., 2019), which includes 314 data from individuals each completing 26 tasks. With regard to depth, the database currently 315 includes: the MyConnectome dataset (Poldrack et al., 2015), which includes extensive task, 316 resting, and diffusion MRI data from more than 100 sessions for a single individual; the Midnight 317 Scan Club dataset (Gordon et al., 2017) which includes extensive task and resting fMRI data 318 from ten individuals; and a number of other dense scanning datasets (Gonzalez-Castillo et al., 319 2015; Newbold et al., 2020; Salehi et al., 2020). 320 321 

10 



_Figure 3_ .  OpenNeuro datasets vary substantially in number of participants (X axis), number of sessions per participant (Y axis), and number of tasks per participant (size/color of datapoints); axes are logscaled for easier visualization. Results are based on metadata derived directly from the 502 OpenNeuro datasets available via DataLad as of 10/9/2021. 

322 

- 323 

- 324 Another unique feature of OpenNeuro is the breadth of phenotypes across datasets.  To further 325 characterize this, we searched the text associated with OpenNeuro datasets to identify terms 326 related to psychological concepts and tasks as defined in the Cognitive Atlas ontology (Poldrack 327 et al., 2011). Word clouds showing the top terms identified in this analysis are shown in 328 Supplementary Figure 1.  This analysis shows a broad range of tasks and concepts associated 329 with these datasets, highlighting the substantial conceptual and methodological breadth of the 330 archive. 

331 

332 _Figure 1 - Figure supplement 1_ .  Word clouds based on Cognitive Atlas terms for psychological 333 concepts (top) and tasks (bottom) identified from titles and README files associated with 334 OpenNeuro datasets. 

335 

- 336 Data reuse 

- 337 

- 338 OpenNeuro has distributed a substantial amount of data; from May 2020 through April 2021, a 339 total of 406 terabytes of data were distributed. Because data reuse is not directly measurable, 340 we utilize published reuse of the shared data as a proxy.  To identify published reuses of 341 OpenNeuro data, we used Google Scholar and CrossRef to identify potential reuses, and then 342 manually examined them to confirm that they were a legitimate reuse (as opposed to a primary 343 publication of the data or data descriptor); note that this is an underestimate since many papers 

11 

344 during this period reported analyses of data downloaded from OpenFMRI, which would not have 345 been identified in our searches.  We identified 165 publications that reused OpenNeuro 346 datasets; this showed a sharp increase over time (see Figure 4). Of these publications, 112 347 were journal or conference papers, 42 were preprints, and 11 were other types of publications 348 (such as theses or project reports).  A total of 111 OpenNeuro datasets were reused at least 349 once, with the most popular dataset (Poldrack et al., 2016) appearing in 28 published reuses. A 350 significant number of publications reused multiple datasets; 31 of the 165 papers reused at least 351 two datasets, with a maximum of 40 datasets reused (Esteban et al., 2019).  Collecting these 352 data from scratch would have required more than 21,000 individual subject visits; at an 353 estimated scanning cost of $1000/session  (based on the conservative cost estimate from 354 (Milham et al., 2018)), this represents a total data reuse value of nearly twenty-one million US 355 dollars.  These reuses have a total of 1329 citations (according to Google Scholar as of June 356 15, 2021); the most highly cited reuse (Esteban et al., 2019) has more than 500 citations. 357 358 



_Figure 4_ . Published reuses of OpenNeuro datasets, split by the type of reuse.  Note that the final bar includes only reuses identified through June 2021. 

359 

- 360 

361 The published reuses of OpenNeuro data span from basic neuroscience to methodological 362 studies and software development.  In particular, several studies demonstrate how OpenNeuro 363 data have enabled new insights into brain function.  For example, Martins et al. (2021) used 364 structural MRI data from several OpenNeuro datasets along with other shared data to examine 365 different patient groups suffering from physical pain or depression. Their analyses demonstrated 366 a specific pattern of anatomical change common to patients with pain syndromes but distinct 367 from depression. This kind of analysis highlights the way in which OpenNeuro enables 368 researchers to combine smaller datasets in order to test hypotheses using convergent data, 369 which can help overcome the confounds and biases present in any particular study as well as 370 increasing statistical power. Other basic neuroscience studies have used OpenNeuro data to 371 model the role of temporal context in forgetting (Chien and Honey, 2020), characterize the role 372 of edge communities in brain networks (Faskowitz et al., 2020), understand the relationship 

12 

373 between functional connectivity and sustained attention (Rosenberg et al., 2020), and to 374 demonstrate that functional parcellation changes as a function of task (Salehi et al., 2020). 

375 

376 Data from OpenNeuro have been particularly useful for the development of new software tools. 377 Esteban et al. (2019) used the breadth and variety of datasets in the archive to assess the 378 robustness of the fMRIPrep preprocessing workflow to many different fMRI datasets, 379 incorporating a total of 40 datasets from OpenNeuro. Importantly, these datasets were used in 380 an iterative manner to improve the robustness of the tool; thus, the breadth of the data were 381 essential both for assessment as well as for improvement of the tool. Without OpenNeuro (and 382 BIDS), amassing such a large and diverse group of datasets would have required immense 383 efforts to reach out to many different research groups, request their data, and then format the 384 data for common usage, whereas with OpenNeuro the entirety of these datasets can be 385 downloaded automatically within a number of hours, immediately ready for analysis.  Other 386 software development projects have taken advantage of some of the particular unique datasets 387 in OpenNeuro; for example, Takeda et al. (2019) took advantage of a unique dataset that 388 combines EEG, MEG, and MRI data on the same individuals (Wakeman and Henson, 2015) to 389 demonstrate the broad range of functions of their VBMEG toolbox.  Other software publications 390 using OpenNeuro data include FastSurfer (Henschel et al., 2020) for structural MRI analysis, 391 and Brainstorm (Tadel et al., 2019) for MEG/EEG analysis. 392 

393 The data in OpenNeuro have been particularly useful for methodological researchers.  One 394 prominent example was published by Bowring et al. (2019), who examined how the use of 395 different analysis software impacted statistical results from fMRI activation analyses.  Their 396 study included an in-depth analysis of the publications associated with each of 55 datasets, in 397 order to identify studies with analysis pipelines and activation results that could be easily 398 compared with their multi-platform results.  Based on this process, they selected three datasets 399 and processed each using several different analysis pipelines; their results highlighted 400 substantial similarity in unthresholded maps but substantial discordance in thresholded maps, 401 highlighting the need for better understanding of the impact of software packages on statistical 402 results.  Another example that would have been challenging to perform without OpenNeuro was 403 published by Dadi et al. (2020), who developed a set of functional atlases using 27 datasets. 404 This breadth allowed them to ensure that the specific features of the atlas were not driven by 405 any particular dataset or task.  Other examples include studies that used OpenNeuro data to 406 assess the impact of confound regression on fMRI signals and develop new methods for 407 confound modeling (Aquino et al., 2020), and to develop and benchmark new methods for 408 multiple comparison correction (Spisák et al., 2019). 

409 Discussion 

410 The OpenNeuro data archive plays an important role in advancing neuroscience research and 411 ensuring its reproducibility by enabling the sharing of a broad range of neuroscience data types 412 according to the FAIR principles.  Its tight integration with the community-driven BIDS standard 413 enhances the ease of sharing, the reusability of the shared data, and the extensibility of the 414 archive in the future.  The shared data have enabled a growing number of publications that 

13 

415 provide novel neuroscientific insights, as well as supporting novel methodological advances and 416 software development. 

## 417 Lessons learned 

- 418 The experiences of our group in developing the OpenNeuro project have provided a number of 419 lessons that may be useful more generally for researchers interested in establishing a culture of 420 data sharing within their scientific subdomain. 

- 421 

- 422 Foremost, we have found that the use of a common community-driven format for data 423 organization is essential to effective sharing. In our case, the BIDS standard has enabled data 424 owners to easily share a growing range of data types (through the use of client-side validator), 425 and has enabled researchers to easily reuse the data.  Because any dataset that passes the 426 validator can be shared, the community’s efforts on extending the standard (which are 427 implemented in the validator) has provided a steady stream of additions to the types of data that 428 OpenNeuro can share.  Another important point is that data sharing does not only include 429 sharing with other researchers, but also with one’s own research group in the future; thus, the 430 use of a well-structured data standard can help researchers ensure that data collected by 431 current lab members can be effectively utilized by other lab members in future, as well as 432 making it easy to share the data beyond one’s own lab.  On the flipside, we continue to see that 433 conversion of data into the BIDS standard remains a stumbling block for many researchers; the 434 continued development of conversion tools is necessary to support these researchers. 

- 435 

- 436 Second, we have found that “it takes an ecosystem” to make data sharing successful. 437 OpenNeuro is only one of the data sharing projects within the field of neuroimaging, and each of 438 the projects has its own particular features and advantages, but together these projects have 439 increasingly led the field to view data sharing as a net positive for our field. In addition, the 440 availability of these data resources has allowed others to build projects that support new 441 mechanisms for data representation and distribution (such as the DataLad project) and new 442 platforms for analysis (such as Brainlife.io).  Together, these tools have provided researchers 443 with additional incentives to share their data via OpenNeuro through its deep integration with 444 those projects. While we believe that sharing is most effective when it is most open, we also 445 realize that some researchers will be unable to share their data on OpenNeuro for ethical or 446 regulatory reasons; for this reason, we believe that a variety of data sharing resources that vary 447 in their sharing policies (Jwa and Poldrack, 2021)will remain essential to support the broadest 448 possible degree of data sharing. 

- 449 

- 450 Finally, we would highlight the importance of domain-specific data repositories that support a 451 particular research community.  All of the sharing activities accomplished using OpenNeuro 452 could in principle have been accomplished using more general data sharing repositories (such 453 as Figshare or Dryad).  A unique benefit of OpenNeuro has been in making a large number of 454 datasets easily findable by researchers, rather than requiring a trawl through a much larger 455 body of datasets to find ones that are relevant.  By developing upload and download systems 456 that are tailored for imaging data, OpenNeuro has also greatly lowered the barrier to sharing 

14 

- 457 and reusing data.  These benefits argue for the continued need for domain-specific data sharing 458 projects designed in close consultation with researchers in the area. Domain-specificity has also 459 allowed OpenNeuro to nurture a community around the resource. Through our social media 460 presence we have engaged the community with regular blog posts that highlight the most open 461 and sharing labs over the previous six months to promote more social incentives to sharing. 

#### 462 

## Long-term sustainability 

- 463 A continual challenge for any investigator-initiated data repository is the long-term sustainability 464 of the archive, in order to ensure researchers’ trust in the platform (Lin et al., 2020).  The 465 ongoing costs of running a repository are substantial, primarily due to the continuing cost of 466 technological upkeep of a web platform with regard to security and stability, as well as the 467 ongoing costs of storage and bandwidth on cloud platforms or hardware maintenance when 468 using on-premise computing systems.  Performant web applications require the use of cutting469 edge software tools, which can often become deprecated or unstable over time, leading to 470 substantial technical debt that must be continually addressed to maintain stable and secure 471 operation. 

- 472 

- 473 One major challenge for repositories that are reliant upon federal grants is the usual three year 474 funding period, in addition to the preference of standard grant mechanisms for funding novel 475 projects rather than ongoing maintenance and operations.  One welcome development has 476 been the instigation of longer-term funding for data archives through the US BRAIN Initiative 477 (Koroshetz et al., 2018), which has explicitly dedicated funding to the development and long478 term sustainability of data archives for neuroscience data. These renewable five-year grants (of 479 which OpenNeuro is one of the recipients) provide a much-needed longer term funding source 480 for data repositories. 

- 481 

- 482 Another resource for longer term sustainability is institutional data repositories, which are 483 increasingly available at many universities. OpenNeuro is working with the Stanford Digital 484 Repository to develop a plan to deposit all raw datasets within the university’s archive, which 485 would provide a digital backstop to the archive’s cloud storage. 

- 486 

- 487 OpenNeuro has also been fortunate to be part of the Amazon Public Datasets project 488 ( <mark>https://registry.opendata.aws/openneuro/ )</mark> , which has provided free data storage and bandwidth for 489 the openly available datasets in the OpenNeuro archive. 

- 490 

## Current limitations and future directions 

- 491 

- 492 There are a number of additional features planned for future development.  These include: 

- 493 

- 494 _Enhanced metadata_ .  At present, a limited amount of dataset-level metadata is collected beyond 495 that present within the BIDS metadata.  Working with the CEDAR Metadata Center (Musen et 496 al., 2015), we plan to add the ability for researchers to enter additional metadata that is linked to 

15 

497 standard ontologies, including those being developed for BIDS data in the context of the 498 Neuroimaging Data Model (Maumet et al., 2016). These annotations will provide the basis for 499 more powerful queries of the archive. 

500 

501 _Sharing of derivatives_ . At present, OpenNeuro only shares raw data. However, the availability of 502 a BIDS standard for the outputs of data processing (i.e. “derivative” data) now provides the 503 ability to include derivative data within a BIDS dataset. We plan to enable researchers to share 504 derivatives, e.g. allowing the sharing of preprocessed MRI data in addition to raw data. This will 505 greatly enhance the reuse of data by researchers who do not have the resources or expertise to 506 preprocess these complex datasets as well as provide a standard baseline for downstream 507 analyses, reducing the potential effects of analytic flexibility (Botvinik-Nezer et al., 2020; 508 Bowring et al., 2019). 

- 509 

510 _Bringing computing to data_ .  The availability of the OpenNeuro data on the Amazon Web 511 Services allows researchers direct access to computing on the data, but doing so requires a 512 substantial degree of cloud computing expertise. To ease the application of computing to the 513 data, we plan to adapt the DANDI Hub infrastructure developed by the Distributed Archives for 514 Neurophysiology Data Integration (DANDI: <u>https://www.dandiarchive.org/), which will allow</u> 515 direct access to the data via a Jupyter notebook. 

- 516 

517 _Beyond MRI data_ . Driven by the initial seeding of data from OpenfMRI, and reflecting the fact 518 that BIDS was originally MRI-centric, the data currently available from OpenNeuro are heavily 519 skewed towards MRI, and fMRI in particular (Table 1). However, BIDS is quickly expanding to 520 other modalities that can readily be uploaded to OpenNeuro, and there has been a rapid 521 increase in sharing of other modalities; for example, more than 60 EEG datasets have been 522 deposited since the publication of the BIDS-EEG standard in 2019 (Pernet et al., n.d.). . This 523 organic expansion beyond MRI will be supported with the necessary adaptations (e.g., online 524 visualization of new modalities) of OpenNeuro’s user interface. 

525 Conclusion 

526 Data sharing ensures the transparency and reproducibility of scientific research, and allows 527 aggregation across datasets that improves statistical power and enables new research 528 questions. The OpenNeuro repository plays a central role in the data sharing ecosystem by 529 promoting maximally open sharing of data, and by enhancing open availability of data from a 530 wide range of datasets spanning   The growth and impact of the repository demonstrate the 531 viability of minimally restrictive sharing, and the importance of common standards such as BIDS 532 for the effective sharing and reuse of data. 533 534 

16 

# 535 Materials and Methods 

#### 536 

## OpenNeuro Infrastructure 

537 Code for the OpenNeuro platform is available at <u>https://github.com/OpenNeuroOrg/openneuro.</u> 538 The application utilizes a cloud-based containerized architecture and is built in JavaScript and 539 Python with a MongoDB database for application data storage. OpenNeuro is hosted on 540 Amazon Web Services (AWS) using the Kubernetes container orchestration platform. Services 541 are deployed as containers and integrated via a JavaScript GraphQL API gateway and the AWS 542 Application Load Balancer. Several clients access this API, the React website, OpenNeuro 543 command line interface, and an ElasticSearch indexer. Datasets are stored as DataLad 544 repositories and managed by a Python backend service container. Each DataLad repository is 545 assigned to a ZFS pool backed by AWS Elastic Block Store. This allows DataLad versioning 546 and filesystem level access to datasets with existing processing and validation tools. Persistent 547 metadata such as user accounts and permissions are maintained in a MongoDB database. 548 Ephemeral caching is provided by Redis. Search indexes, performance monitoring, and logging 549 are implemented with ElasticSearch. CloudFront is used as a global cache and network to 550 provide global presence. 

- 551 

## Content analysis 

- 552 Data regarding OpenNeuro contents and usage were current as of October 9, 2021.  Code and 553 data needed to execute all analyses and generate all figures are available from 554 https://doi.org/10.5281/zenodo.5559041. 

- 555 

- 556 _Reuse analyses_ .  Potential reuses were identified by first searching Google Scholar for the term 557 “openneuro.”; note that this will exclude any paper that mention “OpenfMRI” instead of 558 OpenNeuro, thus the reported results are underestimates of the true impact of the data, given 559 that many of the datasets in OpenNeuro came from OpenFMRI.  Papers matching this search 560 were examined manually to confirm that they had reused data; data descriptor papers were 561 excluded from further analysis.  Citation counts were obtained from Google Scholar using the 562 Python package 'scholarly'. 

- 563 

- 564 _Dataset size analyses_ . Dataset size analyses were performed using DataLad to obtain the full 565 BIDS metadata for the 502 datasets available as of 10/9/2021, and then using pybids (Yarkoni 566 et al., 2019) to load the metadata for each dataset. 

- 567 

#### 568 

# Acknowledgements 

569 The work described here has been supported by the National Institute Of Mental Health of the 570 National Institutes of Health under Award Numbers R24MH117179 and <mark>R24MH114705.</mark> The 

17 

- 571 content is solely the responsibility of the authors and does not necessarily represent the official 572 views of the National Institutes of Health. Development of OpenNeuro and OpenfMRI was also 573 supported by a grant from the Laura and John Arnold Foundation, and the National Science 574 Foundation (OAC-1131441). Sharing of OpenNeuro datasets has been enabled by support from 575 Amazon Web Services. We would like to thank all of the users who have uploaded data to 576 OpenNeuro.  Thanks to Franco Pestili for providing usage data on Brainlife.io, and Nico 577 Dosenbach, Michael Hawrylycz, Karel Svoboda, and Armin Thomas for helpful comments on an 578 earlier draft. 

# 579 References 

- 580 Aquino KM, Fulcher BD, Parkes L, Sabaroedin K, Fornito A. 2020. Identifying and removing 581 widespread signal deflections from fMRI data: Rethinking the global signal regression 582 problem. _Neuroimage_ **212** :116614. 

- 583 Bannier E, Barker G, Borghesani V, Broeckx N, Clement P, Emblem KE, Ghosh S, Glerean E, 584 Gorgolewski KJ, Havu M, Halchenko YO, Herholz P, Hespel A, Heunis S, Hu Y, Hu C-P, 585 Huijser D, de la Iglesia Vayá M, Jancalek R, Katsaros VK, Kieseler M-L, Maumet C, 586 Moreau CA, Mutsaerts H-J, Oostenveld R, Ozturk-Isik E, Pascual Leone Espinosa N, 587 Pellman J, Pernet CR, Pizzini FB, Trbalić AŠ, Toussaint P-J, Visconti di Oleggio Castello 588 M, Wang F, Wang C, Zhu H. 2021. The Open Brain Consent: Informing research 589 participants and obtaining consent to share brain imaging data. _Hum Brain Mapp_ **42** :1945– 590 1951. 

- 591 Bansal S, Kori A, Zulfikar W, Wexler J, Markiewicz C, Feingold F, Poldrack R, Esteban O. n.d. 592 High-sensitivity detection of facial features on MRI brain scans with a convolutional 593 network. doi:10.1101/2021.04.25.441373 

- 594 Bischoff-Grethe A, Burak Ozyurt I, Busa E, Quinn BT, Fennema-Notestine C, Clark CP, Morris 595 S, Bondi MW, Jernigan TL, Dale AM, Brown GG, Fischl B. 2007. A technique for the 596 deidentification of structural brain MR images. _Human Brain Mapping_ . 597 doi:10.1002/hbm.20312 

- 598 Biswal BB, Mennes M, Zuo X-N, Gohel S, Kelly C, Smith SM, Beckmann CF, Adelstein JS, 599 Buckner RL, Colcombe S, Dogonowski A-M, Ernst M, Fair D, Hampson M, Hoptman MJ, 600 Hyde JS, Kiviniemi VJ, Kötter R, Li S-J, Lin C-P, Lowe MJ, Mackay C, Madden DJ, Madsen 601 KH, Margulies DS, Mayberg HS, McMahon K, Monk CS, Mostofsky SH, Nagel BJ, Pekar 602 JJ, Peltier SJ, Petersen SE, Riedl V, Rombouts SARB, Rypma B, Schlaggar BL, Schmidt S, 603 Seidler RD, Siegle GJ, Sorg C, Teng G-J, Veijola J, Villringer A, Walter M, Wang L, Weng 604 X-C, Whitfield-Gabrieli S, Williamson P, Windischberger C, Zang Y-F, Zhang H-Y, 605 Castellanos FX, Milham MP. 2010. Toward discovery science of human brain function. _Proc_ 606 _Natl Acad Sci U S A_ **107** :4734–4739. 

- 607 Botvinik-Nezer R, Holzmeister F, Camerer CF, Dreber A, Huber J, Johannesson M, Kirchler M, 608 Iwanir R, Mumford JA, Adcock RA, Avesani P, Baczkowski BM, Bajracharya A, Bakst L, 609 Ball S, Barilari M, Bault N, Beaton D, Beitner J, Benoit RG, Berkers RMWJ, Bhanji JP, 610 Biswal BB, Bobadilla-Suarez S, Bortolini T, Bottenhorn KL, Bowring A, Braem S, Brooks 611 HR, Brudner EG, Calderon CB, Camilleri JA, Castrellon JJ, Cecchetti L, Cieslik EC, Cole 612 ZJ, Collignon O, Cox RW, Cunningham WA, Czoschke S, Dadi K, Davis CP, Luca AD, 613 Delgado MR, Demetriou L, Dennison JB, Di X, Dickie EW, Dobryakova E, Donnat CL, 614 Dukart J, Duncan NW, Durnez J, Eed A, Eickhoff SB, Erhart A, Fontanesi L, Fricke GM, Fu 615 S, Galván A, Gau R, Genon S, Glatard T, Glerean E, Goeman JJ, Golowin SAE, González616 García C, Gorgolewski KJ, Grady CL, Green MA, Guassi Moreira JF, Guest O, Hakimi S, 

18 

- 617 Hamilton JP, Hancock R, Handjaras G, Harry BB, Hawco C, Herholz P, Herman G, Heunis 618 S, Hoffstaedter F, Hogeveen J, Holmes S, Hu C-P, Huettel SA, Hughes ME, Iacovella V, 619 Iordan AD, Isager PM, Isik AI, Jahn A, Johnson MR, Johnstone T, Joseph MJE, Juliano AC, 620 Kable JW, Kassinopoulos M, Koba C, Kong X-Z, Koscik TR, Kucukboyaci NE, Kuhl BA, 621 Kupek S, Laird AR, Lamm C, Langner R, Lauharatanahirun N, Lee H, Lee S, Leemans A, 622 Leo A, Lesage E, Li F, Li MYC, Lim PC, Lintz EN, Liphardt SW, Losecaat Vermeer AB, 623 Love BC, Mack ML, Malpica N, Marins T, Maumet C, McDonald K, McGuire JT, Melero H, 624 Méndez Leal AS, Meyer B, Meyer KN, Mihai G, Mitsis GD, Moll J, Nielson DM, Nilsonne G, 625 Notter MP, Olivetti E, Onicas AI, Papale P, Patil KR, Peelle JE, Pérez A, Pischedda D, 626 Poline J-B, Prystauka Y, Ray S, Reuter-Lorenz PA, Reynolds RC, Ricciardi E, Rieck JR, 627 Rodriguez-Thompson AM, Romyn A, Salo T, Samanez-Larkin GR, Sanz-Morales E, 628 Schlichting ML, Schultz DH, Shen Q, Sheridan MA, Silvers JA, Skagerlund K, Smith A, 629 Smith DV, Sokol-Hessner P, Steinkamp SR, Tashjian SM, Thirion B, Thorp JN, Tinghög G, 630 Tisdall L, Tompson SH, Toro-Serey C, Torre Tresols JJ, Tozzi L, Truong V, Turella L, van ’t 631 Veer AE, Verguts T, Vettel JM, Vijayarajah S, Vo K, Wall MB, Weeda WD, Weis S, White 632 DJ, Wisniewski D, Xifra-Porxas A, Yearling EA, Yoon S, Yuan R, Yuen KSL, Zhang L, 633 Zhang X, Zosky JE, Nichols TE, Poldrack RA, Schonberg T. 2020. Variability in the analysis 634 of a single neuroimaging dataset by many teams. _Nature_ **582** :84–88. 635 Bowring A, Maumet C, Nichols TE. 2019. Exploring the impact of analysis software on task fMRI 636 results. _Hum Brain Mapp_ **40** :3362–3384. 

- 637 Brakewood B, Poldrack RA. 2013. The ethics of secondary data analysis: considering the 

- 638 application of Belmont principles to the sharing of neuroimaging data. _Neuroimage_ **82** :671– 639 676. 640 Casey BJ, Cannonier T, Conley MI, Cohen AO, Barch DM, Heitzeg MM, Soules ME, Teslovich 641 T, Dellarco DV, Garavan H, Orr CA, Wager TD, Banich MT, Speer NK, Sutherland MT, 642 Riedel MC, Dick AS, Bjork JM, Thomas KM, Chaarani B, Mejia MH, Hagler DJ Jr, Daniela 643 Cornejo M, Sicat CS, Harms MP, Dosenbach NUF, Rosenberg M, Earl E, Bartsch H, Watts 644 R, Polimeni JR, Kuperman JM, Fair DA, Dale AM, ABCD Imaging Acquisition Workgroup. 645 2018. The Adolescent Brain Cognitive Development (ABCD) study: Imaging acquisition 646 across 21 sites. _Dev Cogn Neurosci_ **32** :43–54. 

- 647 Chang N, Pyles JA, Marcus A, Gupta A, Tarr MJ, Aminoff EM. 2019. BOLD5000, a public fMRI 648 dataset while viewing 5000 visual images. _Sci Data_ **6** :49. 

- 649 Chien H-YS, Honey CJ. 2020. Constructing and Forgetting Temporal Context in the Human 650 Cerebral Cortex. _Neuron_ **106** :675–686.e11. 

- 651 Dadi K, Varoquaux G, Machlouzarides-Shalit A, Gorgolewski KJ, Wassermann D, Thirion B, 652 Mensch A. 2020. Fine-grain atlases of functional modes for fMRI analysis. _Neuroimage_ 653 **221** :117126. 

- 654 Esteban O, Markiewicz CJ, Blair RW, Moodie CA, Isik AI, Erramuzpe A, Kent JD, Goncalves M, 655 DuPre E, Snyder M, Oya H, Ghosh SS, Wright J, Durnez J, Poldrack RA, Gorgolewski KJ. 656 2019. fMRIPrep: a robust preprocessing pipeline for functional MRI. _Nat Methods_ **16** :111– 657 116. 

- 658 Faskowitz J, Esfahlani FZ, Jo Y, Sporns O, Betzel RF. 2020. Edge-centric functional network 659 representations of human cerebral cortex reveal overlapping system-level architecture. _Nat_ 660 _Neurosci_ **23** :644–1654. 

- 661 Gonzalez-Castillo J, Hoy CW, Handwerker DA, Roopchansingh V, Inati SJ, Saad ZS, Cox RW, 662 Bandettini PA. 2015. Task Dependence, Tissue Specificity, and Spatial Distribution of 663 Widespread Activations in Large Single-Subject Functional MRI Datasets at 7T. _Cereb_ 664 _Cortex_ **25** :4667–4677. 

- 665 Gordon EM, Laumann TO, Gilmore AW, Newbold DJ, Greene DJ, Berg JJ, Ortega M, Hoyt666 Drazen C, Gratton C, Sun H, Hampton JM, Coalson RS, Nguyen AL, McDermott KB, 667 Shimony JS, Snyder AZ, Schlaggar BL, Petersen SE, Nelson SM, Dosenbach NUF. 2017. 

19 

- 668 Precision Functional Mapping of Individual Human Brains. _Neuron_ **95** :791–807.e7. 669 Gorgolewski KJ, Alfaro-Almagro F, Auer T, Bellec P, Capotă M, Chakravarty MM, Churchill NW, 670 Cohen AL, Craddock RC, Devenyi GA, Eklund A, Esteban O, Flandin G, Ghosh SS, 671 Guntupalli JS, Jenkinson M, Keshavan A, Kiar G, Liem F, Raamana PR, Raffelt D, Steele 672 CJ, Quirion P-O, Smith RE, Strother SC, Varoquaux G, Wang Y, Yarkoni T, Poldrack RA. 673 2017. BIDS apps: Improving ease of use, accessibility, and reproducibility of neuroimaging 674 data analysis methods. _PLoS Comput Biol_ **13** :e1005209. 

- 675 Gorgolewski KJ, Auer T, Calhoun VD, Craddock RC, Das S, Duff EP, Flandin G, Ghosh SS, 676 Glatard T, Halchenko YO, Handwerker DA, Hanke M, Keator D, Li X, Michael Z, Maumet C, 677 Nichols BN, Nichols TE, Pellman J, Poline J-B, Rokem A, Schaefer G, Sochat V, Triplett W, 678 Turner JA, Varoquaux G, Poldrack RA. 2016. The brain imaging data structure, a format for 679 organizing and describing outputs of neuroimaging experiments. _Sci Data_ **3** :160044. 680 Halchenko Y, Meyer K, Poldrack B, Solanky D, Wagner A, Gors J, MacFarlane D, Pustina D, 681 Sochat V, Ghosh S, Mönch C, Markiewicz C, Waite L, Shlyakhter I, de la Vega A, Hayashi 682 S, Häusler C, Poline J-B, Kadelka T, Skytén K, Jarecka D, Kennedy D, Strauss T, Cieslak 683 M, Vavra P, Ioanas H-I, Schneider R, Pflüger M, Haxby J, Eickhoff S, Hanke M. 2021. 684 DataLad: distributed system for joint management of code, data, and their relationship. 685 _Journal of Open Source Software_ . doi:10.21105/joss.03262 

- 686 Halchenko YO, Poldrack B, Hanke M. 2016. DataLad--decentralized data distribution for 687 consumption and sharing of scientific datasetsOrganization of Human Brain Mapping 688 Poster. Organization of Human Brain Mapping Annual Meeting, Geneva, Switzerland. 

- 689 Hanke M, Pestilli F, Wagner AS, Markiewicz CJ, Poline J-B, Halchenko YO. 2021. In defense of 690 decentralized research data management. _Neuroforum_ **0** . doi:10.1515/nf-2020-0037 

- 691 Henschel L, Conjeti S, Estrada S, Diers K, Fischl B, Reuter M. 2020. FastSurfer - A fast and 692 accurate deep learning based neuroimaging pipeline. _Neuroimage_ **219** :117012. 

- 693 Holdgraf C, Appelhoff S, Bickel S, Bouchard K, D’Ambrosio S, David O, Devinsky O, Dichter B, 694 Flinker A, Foster BL, Gorgolewski KJ, Groen I, Groppe D, Gunduz A, Hamilton L, Honey 695 CJ, Jas M, Knight R, Lachaux J-P, Lau JC, Lee-Messer C, Lundstrom BN, Miller KJ, 696 Ojemann JG, Oostenveld R, Petridou N, Piantoni G, Pigorini A, Pouratian N, Ramsey NF, 697 Stolk A, Swann NC, Tadel F, Voytek B, Wandell BA, Winawer J, Whitaker K, Zehl L, 698 Hermes D. 2019. iEEG-BIDS, extending the Brain Imaging Data Structure specification to 699 human intracranial electrophysiology. _Sci Data_ **6** :102. 

- 700 Jwa A, Poldrack R. 2021. The Spectrum of Data sharing Policies in Neuroimaging Data 701 Repositories. _PsyArXiv_ . doi:10.31234/osf.io/cnuy7 

- 702 King M, Hernandez-Castillo CR, Poldrack RA, Ivry RB, Diedrichsen J. 2019. Functional 703 boundaries in the human cerebellum revealed by a multi-domain task battery. _Nat Neurosci_ 704 **22** :1371–1378. 

- 705 Koroshetz W, Gordon J, Adams A, Beckel-Mitchener A, Churchill J, Farber G, Freund M, Gnadt 706 J, Hsu NS, Langhals N, Lisanby S, Liu G, Peng GCY, Ramos K, Steinmetz M, Talley E, 707 White S. 2018. The State of the NIH BRAIN Initiative. _J Neurosci_ **38** :6427–6438. 

- 708 Lin D, Crabtree J, Dillo I, Downs RR, Edmunds R, Giaretta D, De Giusti M, L’Hours H, Hugo W, 709 Jenkyns R, Khodiyar V, Martone ME, Mokrane M, Navale V, Petters J, Sierman B, 710 Sokolova DV, Stockhause M, Westbrook J. 2020. The TRUST Principles for digital 711 repositories. _Scientific Data_ . doi:10.1038/s41597-020-0486-7 

- 712 Littlejohns TJ, Holliday J, Gibson LM, Garratt S, Oesingmann N, Alfaro-Almagro F, Bell JD, 713 Boultwood C, Collins R, Conroy MC, Crabtree N, Doherty N, Frangi AF, Harvey NC, 714 Leeson P, Miller KL, Neubauer S, Petersen SE, Sellors J, Sheard S, Smith SM, Sudlow 715 CLM, Matthews PM, Allen NE. 2020. The UK Biobank imaging enhancement of 100,000 716 participants: rationale, data collection, management and future directions. _Nat Commun_ 717 **11** :2624. 

- 718 Martins D, Dipasquale O, Veronese M, Turkheimer F, Loggia ML, McMahon S, Howard MA, 

20 

- 719 Williams SCR. 2021. Transcriptional and cellular signatures of cortical morphometric 720 similarity remodelling in chronic pain. _bioRxiv_ . doi:10.1101/2021.03.24.436777 721 Maumet C, Auer T, Bowring A, Chen G, Das S, Flandin G, Ghosh S, Glatard T, Gorgolewski KJ, 722 Helmer KG, Jenkinson M, Keator DB, Nichols BN, Poline J-B, Reynolds R, Sochat V, 723 Turner J, Nichols TE. 2016. Sharing brain mapping statistical results with the neuroimaging 724 data model. _Sci Data_ **3** :160102. 

- 725 Mennes M, Biswal BB, Castellanos FX, Milham MP. 2013. Making data sharing work: the 726 FCP/INDI experience. _Neuroimage_ **82** :683–691. 727 Milham MP, Craddock RC, Son JJ, Fleischmann M, Clucas J, Xu H, Koo B, Krishnakumar A, 728 Biswal BB, Castellanos FX, Colcombe S, Di Martino A, Zuo X-N, Klein A. 2018. 729 Assessment of the impact of shared brain imaging data on the scientific literature. _Nat_ 730 _Commun_ **9** :2818. 731 Musen MA, Bean CA, Cheung K-H, Dumontier M, Durante KA, Gevaert O, Gonzalez-Beltran A, 732 Khatri P, Kleinstein SH, O’Connor MJ, Pouliot Y, Rocca-Serra P, Sansone S-A, Wiser JA, 733 CEDAR team. 2015. The center for expanded data annotation and retrieval. _J Am Med_ 734 _Inform Assoc_ **22** :1148–1152. 735 National Academies of Sciences, Engineering, and Medicine, Policy and Global Affairs, Board 736 on Research Data and Information, Committee on Toward an Open Science Enterprise. 737 2018. Open Science by Design: Realizing a Vision for 21st Century Research. National 738 Academies Press. 

- 739 Newbold DJ, Laumann TO, Hoyt CR, Hampton JM, Montez DF, Raut RV, Ortega M, Mitra A, 740 Nielsen AN, Miller DB, Adeyemo B, Nguyen AL, Scheidter KM, Tanenbaum AB, Van AN, 741 Marek S, Schlaggar BL, Carter AR, Greene DJ, Gordon EM, Raichle ME, Petersen SE, 742 Snyder AZ, Dosenbach NUF. 2020. Plasticity and Spontaneous Activity Pulses in Disused 743 Human Brain Circuits. _Neuron_ **107** :580–589.e6. 

- 744 Niso G, Gorgolewski KJ, Bock E, Brooks TL, Flandin G, Gramfort A, Henson RN, Jas M, Litvak 745 V, T Moreau J, Oostenveld R, Schoffelen J-M, Tadel F, Wexler J, Baillet S. 2018. MEG746 BIDS, the brain imaging data structure extended to magnetoencephalography. _Sci Data_ 747 **5** :180110. 748 Nooner KB, Colcombe SJ, Tobe RH, Mennes M, Benedict MM, Moreno AL, Panek LJ, Brown S, 749 Zavitz ST, Li Q, Sikka S, Gutman D, Bangaru S, Schlachter RT, Kamiel SM, Anwar AR, 750 Hinz CM, Kaplan MS, Rachlin AB, Adelsberg S, Cheung B, Khanuja R, Yan C, Craddock 751 CC, Calhoun V, Courtney W, King M, Wood D, Cox CL, Kelly AMC, Di Martino A, Petkova 752 E, Reiss PT, Duan N, Thomsen D, Biswal B, Coffey B, Hoptman MJ, Javitt DC, Pomara N, 753 Sidtis JJ, Koplewicz HS, Castellanos FX, Leventhal BL, Milham MP. 2012. The NKI754 Rockland Sample: A Model for Accelerating the Pace of Discovery Science in Psychiatry. 755 _Front Neurosci_ **6** :152. 

- 756 Norgaard M, Matheson GJ, Hansen HD, Thomas A, Searle G, Rizzo G, Veronese M, Giacomel 757 A, Yaqub M, Tonietto M, Funck T, Gillman A, Boniface H, Routier A, Dalenberg JR, 758 Betthauser T, Feingold F, Markiewicz CJ, Gorgolewski KJ, Blair RW, Appelhoff S, Gau R, 759 Salo T, Niso G, Pernet C, Phillips C, Oostenveld R, Gallezot J-D, Carson RE, Knudsen GM, 760 Innis RB, Ganz M. 2021. PET-BIDS, an extension to the brain imaging data structure for 761 positron emission tomography. _bioRxiv_ . doi:10.1101/2021.06.16.448390 

- 762 Pernet CR, Appelhoff S, Flandin G, Phillips C, Delorme A, Oostenveld R. n.d. BIDS-EEG: an 763 extension to the Brain Imaging Data Structure (BIDS) Specification for 764 electroencephalography. doi:10.31234/osf.io/63a4y 

- 765 Pernet CR, Appelhoff S, Gorgolewski KJ, Flandin G, Phillips C, Delorme A, Oostenveld R. 2019. 766 EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. 767 _Sci Data_ **6** :103. 768 Pinho AL, Amadon A, Gauthier B, Clairis N, Knops A, Genon S, Dohmatob E, Torre JJ, Ginisty 769 C, Becuwe-Desmidt S, Roger S, Lecomte Y, Berland V, Laurier L, Joly-Testault V, 

21 

- 770 Médiouni-Cloarec G, Doublé C, Martins B, Salmon E, Piazza M, Melcher D, Pessiglione M, 771 van Wassenhove V, Eger E, Varoquaux G, Dehaene S, Hertz-Pannier L, Thirion B. 2020. 772 Individual Brain Charting dataset extension, second release of high-resolution fMRI data for 773 cognitive mapping. _Sci Data_ **7** :353. 

- 774 Pinho AL, Amadon A, Ruest T, Fabre M, Dohmatob E, Denghien I, Ginisty C, Becuwe-Desmidt 775 S, Roger S, Laurier L, Joly-Testault V, Médiouni-Cloarec G, Doublé C, Martins B, Pinel P, 776 Eger E, Varoquaux G, Pallier C, Dehaene S, Hertz-Pannier L, Thirion B. 2018. Individual 777 Brain Charting, a high-resolution fMRI dataset for cognitive mapping. _Sci Data_ **5** :180105. 

- 778 Poldrack RA, Barch DM, Mitchell JP, Wager TD, Wagner AD, Devlin JT, Cumba C, Koyejo O, 779 Milham MP. 2013. Toward open sharing of task-based fMRI data: the OpenfMRI project. 780 _Front Neuroinform_ **7** :12. 781 Poldrack RA, Congdon E, Triplett W, Gorgolewski KJ, Karlsgodt KH, Mumford JA, Sabb FW, 782 Freimer NB, London ED, Cannon TD, Bilder RM. 2016. A phenome-wide examination of 783 neural and cognitive function. _Sci Data_ **3** :160110. 

- 784 Poldrack RA, Gorgolewski KJ. 2014. Making big data open: data sharing in neuroimaging. _Nat_ 785 _Neurosci_ **17** :1510–1517. 

- 786 Poldrack RA, Kittur A, Kalar D, Miller E, Seppa C, Gil Y, Parker DS, Sabb FW, Bilder RM. 2011. 787 The cognitive atlas: toward a knowledge foundation for cognitive neuroscience. _Front_ 788 _Neuroinform_ **5** :17. 

- 789 Poldrack RA, Laumann TO, Koyejo O, Gregory B, Hover A, Chen M-Y, Gorgolewski KJ, Luci J, 790 Joo SJ, Boyd RL, Hunicke-Smith S, Simpson ZB, Caven T, Sochat V, Shine JM, Gordon E, 791 Snyder AZ, Adeyemo B, Petersen SE, Glahn DC, Reese Mckay D, Curran JE, Göring HHH, 792 Carless MA, Blangero J, Dougherty R, Leemans A, Handwerker DA, Frick L, Marcotte EM, 793 Mumford JA. 2015. Long-term neural and physiological phenotyping of a single human. _Nat_ 794 _Commun_ **6** :8885. 

- 795 Poline J-B, Breeze JL, Ghosh S, Gorgolewski K, Halchenko YO, Hanke M, Haselgrove C, 796 Helmer KG, Keator DB, Marcus DS, Others. 2012. Data sharing in neuroimaging research. 797 _Front Neuroinform_ **6** . 

- 798 Rosenberg MD, Scheinost D, Greene AS, Avery EW, Kwon YH, Finn ES, Ramani R, Qiu M, 799 Constable RT, Chun MM. 2020. Functional connectivity predicts changes in attention 800 observed across minutes, days, and months. _Proc Natl Acad Sci U S A_ **117** :3797–3807. 

- 801 Salehi M, Greene AS, Karbasi A, Shen X, Scheinost D, Constable RT. 2020. There is no single 802 functional atlas even for a single individual: Functional parcel definitions change with task. 803 _Neuroimage_ **208** :116366. 

- 804 Schwarz CG, Kremers WK, Therneau TM, Sharp RR, Gunter JL, Vemuri P, Arani A, Spychalla 805 AJ, Kantarci K, Knopman DS, Petersen RC, Jack CR Jr. 2019. Identification of Anonymous 806 MRI Research Participants with Face-Recognition Software. _N Engl J Med_ **381** :1684–1686. 

- 807 Smith SM, Nichols TE. 2018. Statistical Challenges in “Big Data” Human Neuroimaging. _Neuron_ 808 **97** :263–268. 

- 809 Spisák T, Spisák Z, Zunhammer M, Bingel U, Smith S, Nichols T, Kincses T. 2019. Probabilistic 810 TFCE: A generalized combination of cluster size and voxel intensity to increase statistical 811 power. _Neuroimage_ **185** :12–26. 

- 812 Tadel F, Bock E, Niso G, Mosher JC, Cousineau M, Pantazis D, Leahy RM, Baillet S. 2019. 813 MEG/EEG Group Analysis With Brainstorm. _Front Neurosci_ **13** :76. 

- 814 Takeda Y, Suzuki K, Kawato M, Yamashita O. 2019. MEG Source Imaging and Group Analysis 815 Using VBMEG. _Front Neurosci_ **13** :241. 

- 816 United States. National Commission for the Protection of Human Subjects of Biomedical and 817 Behavioral Research. 1978. The Belmont Report: Ethical Principles and Guidelines for the 818 Protection of Human Subjects of Research. The Commission. 

- 819 Van Essen DC, Smith SM, Barch DM, Behrens TEJ, Yacoub E, Ugurbil K, WU-Minn HCP 820 Consortium. 2013. The WU-Minn Human Connectome Project: an overview. _Neuroimage_ 

22 

- 821 **80** :62–79. 

- 822 Van Horn JD, Gazzaniga MS. 2013. Why share data? Lessons learned from the fMRIDC. 823 _Neuroimage_ **82** :677–682. 

- 824 Wakeman DG, Henson RN. 2015. A multi-subject, multi-modal human neuroimaging dataset. 825 _Sci Data_ **2** :150001. 

- 826 Wilkinson MD, Dumontier M, Aalbersberg IJJ, Appleton G, Axton M, Baak A, Blomberg N, 827 Boiten J-W, da Silva Santos LB, Bourne PE, Bouwman J, Brookes AJ, Clark T, Crosas M, 828 Dillo I, Dumon O, Edmunds S, Evelo CT, Finkers R, Gonzalez-Beltran A, Gray AJG, Groth 829 P, Goble C, Grethe JS, Heringa J, ’t Hoen PAC, Hooft R, Kuhn T, Kok R, Kok J, Lusher SJ, 830 Martone ME, Mons A, Packer AL, Persson B, Rocca-Serra P, Roos M, van Schaik R, 831 Sansone S-A, Schultes E, Sengstag T, Slater T, Strawn G, Swertz MA, Thompson M, van 832 der Lei J, van Mulligen E, Velterop J, Waagmeester A, Wittenburg P, Wolstencroft K, Zhao 833 J, Mons B. 2016. The FAIR Guiding Principles for scientific data management and 834 stewardship. _Sci Data_ **3** :160018. 

- 835 Yarkoni T, Markiewicz CJ, de la Vega A, Gorgolewski KJ, Salo T, Halchenko YO, McNamara Q, 836 DeStasio K, Poline J-B, Petrov D, Hayot-Sasson V, Nielson DM, Carlin J, Kiar G, Whitaker 837 K, DuPre E, Wagner A, Tirrell LS, Jas M, Hanke M, Poldrack RA, Esteban O, Appelhoff S, 838 Holdgraf C, Staden I, Thirion B, Kleinschmidt DF, Lee JA, Visconti di Oleggio Castello M, 839 Notter MP, Blair R. 2019. PyBIDS: Python tools for BIDS datasets. _J Open Source Softw_ **4** . 840 doi:10.21105/joss.01294 

- 841 

23 

