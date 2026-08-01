# Snapshot: Temple University EEG Corpus - Downloads

Retrieved 2026-07-31 from https://isip.piconepress.com/projects/nedc/html/tuh_eeg/
Plain-text rendering of the HTML page; navigation chrome retained as it appeared.


------------------------------------------------------------------------------

Temple University EEG Corpus - Downloads 

 992px. Any lower resolution will
 collapse the navbar and create a button for the links.
----------------------------------------------------------------------------->

 Open Source EEG Resources

 Home 

 Overview 

 Downloads 

 FAQ 

 Electroencephalography (EEG) Resources

 Corpora: 
 TUEG |
 TUAB |
 TUAR |
 TUEP |
 TUEV |
 TUSZ |
 TUSL 

 Software: 
 EGAS |
 ERDR |
 EEGR |
 EVAL |
 PYPR |
 MEDF |
 EDFB |
 PYED 

 Documentation: 
 ELEC |
 ANNO |
 RPRT 

 Instructions: 
 RSYN |
 DISK 

 To request access to the TUH EEG Corpus, please fill out
 
 this form 

 and email a signed copy to

 help@nedcdata.org .

 Please include "Download The TUH EEG Corpus" in the subject line
 or click on this

 link .

 Note this is an Adobe Acrobat form, and it is best filled out
 using Adobe Acrobat or a similarly compatible tool. We suggest you
 download a copy to your desktop and fill it out using a local app,
 rather than attempt to complete the form from within a browser.

 The form must be filled out correctly or it will be returned to you.
 Please follow the instructions on the form very carefully, including
 completing the address information accurately. This is very important
 and we cannot accept forms with incorrect addresses.

 Once your form is accepted, you will receive information about
 the credentials used to access the data in a separate email, and
 be added to our listserv. This usually takes about 24 to 48
 hours. We need to track who downloads the data. We also want to
 be able to inform you of any updates to the releases.

 Corpora 

 Once you have successfully registered and transmitted your
 ssh keys, you can download our corpora using rsync. The
 path for the most current release is shown with each entry.

 The TUH EEG Corpus
 ( TUEG )
 [rsync path: data/tuh_eeg/tuh_eeg/v2.0.2]:

 A rich archive of 26,846 clinical EEG recordings collected 
 at Temple University Hospital (TUH) from 2002 - 2017.
 Read this 
 
 journal paper 
 for a more complete description of the corpus.

 The TUH Abnormal EEG Corpus
 ( TUAB )
 [rsync path: data/tuh_eeg/tuh_eeg_abnormal/v3.0.1]:

 A corpus of EEGs that have been annotated as normal or abnormal.
 Read
 
 Silvia Lopez's MS thesis 
 for a description of the corpus.

 The TUH EEG Artifact Corpus
 ( TUAR )
 [rsync path: data/tuh_eeg/tuh_eeg_artifact/v3.0.1]:

 This subset of TUEG that contains annotations of
 5 different artifacts: (1) eye movement (EYEM), (2) chewing (CHEW), 
 (3) shivering (SHIV), (4) electrode pop, electrode static, 
 and lead artifacts (ELPP), and (5) muscle artifacts (MUSC).

 The TUH EEG Epilepsy Corpus
 ( TUEP )
 [rsync path: data/tuh_eeg/tuh_eeg_epilepsy/v3.1.0]:

 This is a subset of TUEG that contains 100 subjects 
 epilepsy and 100 subjects without epilepsy, as determined
 by a certified neurologist. The data was developed in collaboration
 with a number of partners including NIH. This new version of
 the corpus has seizure annotations and includes metadata on
 diseases, medications and other relevant information.

 The TUH EEG Events Corpus
 ( TUEV )
 [rsync path: data/tuh_eeg/tuh_eeg_events/v2.0.1]:

 This corpus is a subset of TUEG that contains annotations
 of EEG segments as one of six classes:
 (1) spike and sharp wave (SPSW),
 (2) generalized periodic epileptiform discharges (GPED),
 (3) periodic lateralized epileptiform discharges (PLED),
 (4) eye movement (EYEM), (5) artifact (ARTF) and
 (6) background (BCKG).

 The TUH EEG Seizure Corpus (TUSZ)
 [rsync path: data/tuh_eeg/tuh_eeg_seizure/v2.0.6]:

 This corpus has EEG signals that have been manually
 annotated data for seizure events (start time, stop, channel and
 seizure type). For more information about this
 corpus, please refer to our
 book section .
 The annotation guidelines are described
 here .
 The electrode configurations and channel labels are described
 here .

 The TUH EEG Slowing Corpus
 ( TUSL )
 [rsync path: data/tuh_eeg/tuh_eeg_slowing/v2.0.1]:

 This is another subset of TUEG that contains annotations
 of slowing events. This corpus has been used to study common 
 error modalities in automated seizure detection.

 Software 

 This section of our web site contains a rich collection of machine
 learning systems and supporting software, including our best
 EEG seizure detection system.

 NEDC EEG Annotation System 
 ( EAS: v6.0.2 ):
 A tool that allows rapid annotation of EEG signals.
 The tool includes spectrogram and energy plots, and is capable
 of transcribing data in real time. Learn more about this
 tool from our
 
 IEEE SPMB 2018 paper .

 NEDC ResNet Decoder Real-Time 
 ( ERDR: v1.0.1 ):
 A real-time EEG seizure detection system based on a ResNet-18
 neural network and transfer learning. This package contains a
 real-time decoder that is described in this
 
 publication .
 This is also part of our real-time demonstration system.

 NEDC ResNet Seizure Detection System 
 ( EEGR: v1.0.1 ):
 A research version of our real-time seizure detection system
 that includes a trainer and a decoder. This package is used to
 develop and evaluate models. This package contains a decoder
 that is described in this
 
 publication .

 NEDC Eval EEG 
 ( EVAL v6.0.0 ):
 A Python-based scoring package that implements a variety
 of standard evaluation metrics. A complete description
 of the software can be found
 
 here .

 NEDC PyPrint EDF 
 ( PYPR v1.0.0 ):
 A Python-based tool that decodes the header and signal data
 in an Edf file. This is not as simple as it might seem because channels
 can be permuted and must be decoded using channel labels.

 MATLAB EDF 
 ( MEDF ):
 MATLAB code that loads EEG signal data from an EDF file.

 EDF Browser 
 ( EDFB ):
 An open-source program that can be used to view files such as 
 EEG, EMG, ECG, etc., available for Windows and Linux. 

 Python-based EDF 
 ( PYED ):
 A Python interface to EDFLib that lets you read and write
 EDF files (the distribution format for TUH EEG).

 Documentation 

 We have several tutorials available to facilitate acquisition
 of our data, including these

 videos .

 Electrodes 
 ( ELEC ):
 A document that describes how EEG signals are stored in a
 multichannel signal file format. This document also includes
 a description of the channel labels, which are required to 
 properly decode the data.

 Annotations: 
 ( ANNO ):
 A document that describes how we annotate seizures and store
 the annotations in various file formats.

 Reports: 
 ( RPRT ):
 We no longer distribute reports with our corpora. However, we do
 offer users the opportunity to search the anonymized reports for
 keywords or items of interest. If you provide a simple Python script
 that executes your search criteria, we can run it on the reports,
 and report which files matched your search criteria.

 A example script demonstrating the interface we need is

 here .

 This script takes as input a file containing a list of filenames,
 and returns filenames that match your search criteria.

 Our users have used this service to select subsets of our corpora
 that meet their needs. Note, however, that searching these reports
 is not trivial, since the reports are unstructured text. It is very
 difficult to parse these using natural language processing tools
 to avoid false positives when doing these kinds of searchers.

 Users interested in this service should email a simple Python script
 that does not use any non-standard libraries to

 help@nedcdata.org .

 Instructions 

 As of January 2026, our released corpora are now distributed using
 ssh keys and rsync. The process for this begins with your submission
 of the above form. Once approved, you will receive instructions on
 how to transmit your key and access the data.

 Rsync ,
 which is available on Linux and Mac platforms, is our
 preferred way of downloading data. It allows you to easily keep
 your copy of the data in sync with ours. Windows users can get
 access to rsync by installing MobaXterm. Some
 tips on how to install and use MobaXterm are

 here .

 Before you attempt to download an entire corpus, you should test
 your ability to download data by executing this command:

 rsync -auvxL -e "ssh -i ~/.ssh/id_ed25519" \

 nedc-tuh-eeg@www.isip.piconepress.com:data/tuh_eeg/TEST .

 This command must be typed on one line in your command line tool.

 If for some reason this fails, change "-auxvL" 
 to "-auxvvvL" . This will generate a log file that your IT
 support team can use to diagnose the problems with your downloads.

 Note that the "-L" option in rsync instructs it to follow links.
 All of our corpora are linked back to TUEG. It is best to always
 use the "-L" option.

 If Internet connectivity is a problem, you can send us a

 8T USB drive .
 
 We will copy the data to this disk and send it to you. You
 must arrange for postage as described below.
 If you elect this option, you need to send
 us a 8T USB drive and provide a UPS or FedEx account number
 for return shipping.

 Please send us a conventional USB-mounted
 disk drive. We have had problems with other types of media
 such as thumb drives. Any standard USB-powered USB 2.0 or 3.0 compatible
 8T drive will work fine. Because of the time it takes to copy the
 data, we need a drive that can maintain a stable connection, and thumb
 drives have proven to be unreliable.

 Mail the drive to:

 Joseph Picone

 1610 Rhawn Street

 Philadelphia, PA 19111

 Tel: 708-848-2846

 Please

 email us 

 for details before shipping the drive. If you ship us a drive 
 directly from a reseller such as Amazon, please make sure 
 that the shipment contains information that we can use to 
 identify you. This information should include a point of 
 contact (POC), the name of your institution, and contact 
 information (name, surface mail address and 
 telephone number for the POC).

 Please note that disk drives sent to international destinations
 will often get caught in Customs for weeks. Rsync is a much
 better option than going through your local governments.

 If you are having trouble deciding what to do,

 email us 

 and describe what specific resources in which you are interested.
 We will be happy to guide you through the process.

 The Neural Engineering Data Consortium

 Social Media 

 Help 

 Contact Us

==============================================================================

# Snapshot: Temple University EEG Corpus - Overview

Retrieved 2026-07-31 from https://isip.piconepress.com/projects/tuh_eeg/html/overview.shtml
Plain-text rendering of the HTML page; navigation chrome retained as it appeared.


------------------------------------------------------------------------------

Temple University EEG Corpus - Overview

 992px. Any lower resolution will
 collapse the navbar and create a button for the links.
----------------------------------------------------------------------------->

 Open Source EEG Resources

 Home 

 Overview 

 Downloads 

 FAQ 

 Electroencephalography (EEG) Resources

 Significance

 Data-driven approaches have made enormous advances in recent
 years in terms of their ability to predict events through
 supervised training on big data resources. Equally important,
 however, is the fact that many of these techniques have the
 ability to discover underlying structure of the data using
 latent variables and unsupervised training techniques. These
 types of algorithms can provide enormous insight into the
 data. The only impediment to applying these techniques has been
 the lack of a suitable amount of data to support comprehensive
 experimentation.

 The Neural Engineering Data Consortium (NEDC) 

 has been established at Temple University to address this issue.

 Goal

 The existence of massive corpora has proven to substantially
 accelerate research progress, as shown to the right.
 NEDC will broaden participation by making
 data available to research groups who have significant signal
 processing expertise but who lack capacity for data
 generation. This effort is modeled in part after similar
 successful endeavors, particularly in the human language
 technology field where a data consortium has led to systematic
 research and technology advances over a 20 year span.

 The TUH EEG Corpus represents NEDC's first effort to provide a
 massive corpus to the community. In this project, we are
 focusing on clinical electroencephalogram (EEG) recordings, as
 shown to the left. These recordings were conducted at Temple
 University Hospital (TUH) from 2002 to 2013 (and beyond). 
 The first release of the corpus is expected to contain over
 20,000 EEGs. We expect to continue the development of the
 corpus at a rate of about 1,000 EEGs per year. We also hope to
 convince other hospitals to provide similar data. The end goal
 for the corpus is over 100,000 EEGs.

 Such a large corpus will support the development of technology
 to automatically interpret EEGs in addition to advancing the
 basic science of what aspects of a patient's medical record
 correlate with various pathologies that can be diagnosed from
 EEG studies. Automatic interpretation of EEG data using
 machine learning approaches has evolved in recent
 years. Several specific applications have been studied
 extensively, including seizure detection, movement and brain
 activity. What most of these studies have in common, however,
 is that the data sets are small, typically involving 100 or
 less EEG studies. Such small studies simply do not produce
 statistically significant outcomes, and do not represent enough
 data to support complex statistical models. Further, when
 correlates such as drug treatments, patient medical histories,
 or patient gender or age are factored in, studies consisting of
 100 subjects are not sufficient to draw conclusions about best
 practices. It is the goal of this project to fundamentally
 change this.

 Electroencephalography

 Electroencephalography (EEG) 

 is the recording of electrical activity along the scalp
 using an array of electrodes positioned strategically
 around a patient's head. For an excellent tutorial
 on the hardware aspects of this problem, see E. Pavlick's
 
 EEG 
 Tutorial .
 
 EEGs are used today to diagnose many problems ranging from
 epilepsy to sleep disorders. The EEGs contained in the TUH EEG
 Corpus consist of 24 to 36 channels of signal data and an
 annotation channel containing markers identifying events of
 interest to the physicians and technicians. Signals are sampled
 at 250 Hz using 16 bits per sample. A typical EEG file contains
 about 20 Mbytes of data. These files are stored in an
 
 European Data Format (EDF+) 
 
 file format.

 The Neural Engineering Data Consortium

 Social Media 

 Help 

 Contact Us