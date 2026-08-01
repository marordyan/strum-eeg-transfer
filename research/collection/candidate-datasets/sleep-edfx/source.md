# Sleep-EDF Database Expanded v1.0.0 (PhysioNet landing page snapshot)

Source URL: https://physionet.org/content/sleep-edfx/1.0.0/
Retrieved: 2026-07-31

> Snapshot of the canonical PhysioNet landing page for the dataset. The dataset has no
> stand-alone data-descriptor paper; PhysioNet directs users to cite Kemp et al. (2000),
> IEEE Trans. Biomed. Eng. 47(9):1185-1194, which is a methods paper about slow-wave
> microcontinuity rather than a description of this database. This page is therefore the
> primary documentation of the recording, and is what this card is written from.

---
Introduction
The sleep-edf database contains 197 whole-night PolySomnoGraphic sleep recordings, containing EEG, EOG, chin EMG, and event markers. Some records also contain respiration and body temperature. Corresponding hypnograms (sleep patterns) were manually scored by well-trained technicians according to the Rechtschaffen and Kales manual, and are also available. The data comes from two studies, briefly described below, and in detail in 
[1,2]
.
Data and Annotation Files
The 
*PSG.edf
 files are whole-night polysmnographic sleep recordings containing EEG (from Fpz-Cz and Pz-Oz electrode locations), EOG (horizontal), submental chin EMG, and an event marker. The 
SC*PSG.edf
 files (see the 'sleep cassette study') often also contain oro-nasal respiration and rectal body temperature.
The 
*Hypnogram.edf
 files contain annotations of the sleep patterns that correspond to the PSGs. These patterns (hypnograms) consist of sleep stages W, R, 1, 2, 3, 4, M (Movement time) and ? (not scored). All hypnograms were manually scored by well-trained technicians (identified by the eighth letter of the hypnogram filename) according to the 1968 Rechtschaffen and Kales manual 
[3]
, but based on Fpz-Cz/Pz-Oz EEGs instead of C4-A1/C3-A2 EEGs, as suggested by 
[4]
).
All EDF header fields also comply with the EDF+ specs, and unrecorded signals were removed from the ST*PSG.edf files.
The PSG files are formatted in EDF while the hypnograms are in EDF+. The specifications of EDF and EDF+ are on 
www.edfplus.info
 and in 
[5,6]
. Each EDF and EDF+ file has a header specifying the patient (in these files anonymized to only gender and age), details of the recording (in particular the recorded time period), and characteristics of the signals including their amplitude calibration.
Sleep Cassette Study and Data
The 153 
SC*
 files (SC = Sleep Cassette) were obtained in a 1987-1991 study of age effects on sleep in healthy Caucasians aged 25-101, without any sleep-related medication [2]. Two PSGs of about 20 hours each were recorded during two subsequent day-night periods at the subjects homes. Subjects continued their normal activities but wore a modified Walkman-like cassette-tape recorder described in chapter VI.4 (page 92) of Bob’s 1987 thesis [7].
Files are named in the form SC4
ssN
EO-PSG.edf where 
ss
 is the subject number, and 
N
 is the night. The first nights of subjects 36 and 52, and the second night of subject 13, were lost due to a failing cassette or laserdisk.
The EOG and EEG signals were each sampled at 100 Hz. The submental-EMG signal was electronically highpass filtered, rectified and low-pass filtered after which the resulting EMG envelope expressed in uV rms (root-mean-square) was sampled at 1Hz. Oro-nasal airflow, rectal body temperature and the event marker were also sampled at 1Hz.
Subjects and recordings are further described in the file headers, the descriptive spreadsheet 
SC-subjects.xls
, and in [2].
Sleep Telemetry Study and Data
The 44 
ST*
 files (ST = Sleep Telemetry) were obtained in a 1994 study of temazepam effects on sleep in 22 Caucasian males and females without other medication. Subjects had mild difficulty falling asleep but were otherwise healthy. The PSGs of about 9 hours were recorded in the hospital during two nights, one of which was after temazepam intake, and the other of which was after placebo intake. Subjects wore a miniature telemetry system with very good signal quality described in [8].
Files are named in the form ST7
ssN
J0-PSG.edf where 
ss
 is the subject number, and 
N
 is the night.
EOG, EMG and EEG signals were sampled at 100 Hz, and the event marker at 1 Hz. The physical marker dimension ID+M-E relates to the fact that pressing the marker (M) button generated two-second deflections from a baseline value that either identifies the telemetry unit (ID = 1 or 2 if positive) or marks an error (E) in the telemetry link if negative. Subjects and recordings are further described in the file headers, the descriptive spreadsheet 
ST-subjects.xls
, and in [1].
Software for viewing EDF and EDF+ files
Both EDF and EDF+ formats are free and can be viewed using free software such as:
	
Polyman
 (for MS-Windows only; for details, please follow the link)
	
EDFbrowser
 (for Linux, Mac OS X, and MS-Windows; at 
www.teuniz.net
)
	
LightWAVE
 and the 
PhysioBank ATM
, platform-independent web applications from PhysioNet
	
WAVE
 and other applications for Linux, Mac OS X, and MS-Windows in the 
WFDB Software Package
, also from PhysioNet
An easy way to view these recordings using Polyman is to select 
File → Open → File(s)...
 to open a PSG.edf file and its corresponding .Hypnogram.edf file; then select 
File → Apply Template → Browse...
 to open 
SC-cassette.xml
 (for an SC PSG) or 
ST-telemetry.xml
 (for an ST PSG).
Applications using 
WFDB library
 version 10.4.5 (February 2008) or later can read EDF files directly with no conversion required. Note that the WFDB library does not decode annotations in EDF+ files, however.
Version History
	
Version 0: A small subset of this dataset was previously contributed in 2002 and remains available 
here
 for reference and to support ongoing studies.
	
Version 1: In 2013, the database was greatly expanded to contain 61 PSGs with accompanying hypnograms.
	
Version 2: In March 2018, the database was greatly expanded to contain 197 PSGs with accompanying hypnograms
Database Creator and Contact
Bob Kemp, The Netherlands bk at hsr dot nl
References
	
B Kemp, AH Zwinderman, B Tuk, HAC Kamphuisen, JJL Oberyé. 
Analysis of a sleep-dependent neuronal feedback loop: the slow-wave microcontinuity of the EEG
. 
IEEE-BME
47
(9):1185–1194 (2000)
	
MS Mourtazaev, B Kemp, AH Zwinderman, HAC Kamphuisen. 
Age and gender affect different characteristics of slow waves in the sleep EEG
. 
Sleep
18
(7):557–564 (1995).
	
A Rechtschaffen, AE Kales. A manual of standardized terminology, techniques and scoring systems for sleep stages of human subjects. Los Angeles, CA: UCLA Brain Information Service. Brain Research Institute 10 (1968).
	
B van Sweden, B Kemp, HAC Kamphuisen, EA van der Velde. 
Alternative electrode placement in (automatic) sleep scoring (Fpz-Cz/Pz-Oz versus C4-A1/C3-A2)
. 
Sleep
13
(3):279–283 (1990).
	
B Kemp, A Värri, AC Rosa, KD Nielsen, J Gade. 
A simple format for exchange of digitized polygraphic recordings
. 
Electroencephalography and Clinical Neurophysiology
82
:391–393 (1992).
	
B Kemp, J Olivan. 
European data format 'plus' (EDF+), an EDF alike standard format for the exchange of physiological data
. 
Clinical Neurophysiology
114
:1755–1761 (2002).
	
B Kemp. 
Model-based monitoring of human sleep stages
. Ph.D. thesis, Twente University (1987).
	
B Kemp, AJMW Janssen, MJ Roessen. 
A digital telemetry system for ambulatory sleep recording
. In: 
Sleep-Wake Research in The Netherlands
 4, eds ML Coenen and J Arends, Dutch Society for Sleep Wake Research, pp 129–132 (1993).
        
        
      
      
      
        
        
        
          
Share
          
            
            
            
            
            
          
        
        
          
Access
          
            
              
Access Policy:
              
              Anyone can access the files, as long as they conform to the terms of the specified license.
            
              
License (for files):
              
              
Open Data Commons Attribution License v1.0
            
            
            
        
        
          
Discovery
          
            
DOI (version 1.0.0):
                
                
https://doi.org/10.13026/C2X676
              
            
            
            
            
Topics:
                
                
polysomnogram
                
sleep
                
multiparameter
                
            
            
        
        
          
Project Views
          
            
              
                
1487
                
Current Version
              
              
                
1487
                
All Versions
              
            
            
Project Views by Unique Registered Users
            
              
View Details
            
          
        
        
          
Corresponding Author
          
            
You must be logged in to view the contact information.
            
        
        
  
Versions
  
    
        
          
1.0.0
          
            Oct. 24, 2013
        
      
    
      
      
    
    
Files
    
        
            
Total uncompressed size: 8.1 GB.
          
        
Access the files
        
        
          
Download
              the ZIP file
 (8.1 GB)
          
            
           
          
              Download the files using your terminal:
wget -r -N -c -np https://physionet.org/files/sleep-edfx/1.0.0/
            
          
          
            
              Download the files using AWS command line tools:
aws s3 sync --no-sign-request s3://physionet-open/sleep-edfx/1.0.0/ DESTINATION
            
          
        
        
        
            
 Visualize waveforms
          
        
          
  Folder Navigation:
<base>
  
  
  
  
  
    
      
Name
      
Size
      
Modified
    
  
  
  
    
      
sleep-cassette
      
      
    
  
      
sleep-telemetry
      
      
    
  
    
      
RECORDS
        
          
(download)
        
      
      
6.2 KB
      
2018-04-05
    
  
      
RECORDS-v1
        
          
(download)
        
      
      
1.0 KB
      
2018-04-05
    
  
      
SC-subjects.xls
        
          
(download)
        
      
      
23.5 KB
      
2018-04-05
    
  
      
SHA256SUMS.txt
        
          
(download)
        
      
      
38.9 KB
      
2019-02-20
    
  
      
ST-subjects.xls
        
          
(download)
        
      
      
23 KB
      
2018-04-05
    
  
        
      
      
    
    
    
  
    
      
      
        
          
Maintained by the MIT Laboratory for Computational Physiology
          
            
Supported by the National Institute of Biomedical Imaging and Bioengineering (NIBIB), National Heart Lung and Blood Institute (NHLBI), and NIH Office of the Director under NIH grant numbers U24EB037545 and R01EB030362
          
        
          
Navigation
          
Discover Data
          
Share Data
          
About
          
News
        
        
          
Explore
          
Data
          
Software
          
Challenges
          
Tutorials
          
        
          
Subscribe to our Newsletter
          
          
Subscribe Now
        
 -->
      
      
        
          
          
          
          
        
        
          
          
Accessibility
          
      
    
  
    
    
  
    
  
  
  
