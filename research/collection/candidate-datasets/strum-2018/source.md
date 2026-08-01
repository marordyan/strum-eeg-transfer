IEEE Xplore Full-Text PDF: 

2018 IEEE International Conference on Systems, Man, and Cybernetics 

# STRUM: A new Dataset for Neuroergonomics Research 

Christian A. Kothe Tim R. Mullen _Intheon Labs Intheon Labs Intheon Intheon_ San Diego, CA, USA San Diego, CA, USA christian.kothe@intheon.io tim.mullen@intheon.io 

Scott Makeig _Swartz Center for Compuational Neuroscience Institute for Neural Computation_ La Jolla, CA, USA smakeig@ucsd.edu 

**_Abstract_ — The past decade has seen a gradual expansion of Brain-Computer Interface applications from their clinical roots into entertainment, automotive, workplace, and military domains. However, many of these new-found applications have yet to pass the prototype stage, among others due to challenges posed by real-world data noise levels and increased context variability and complexity. Tackling these challenges requires sufficiently realistic and rich datasets that allow for benchmarking competing approaches, and in this paper, we present a task battery modeled after a complex real-world scenario, together with a new open dataset for BCI research. Results from an exemplary analysis of a slice of this large trove of data are presented, and it is found that the data mirror some of the challenges encountered in real-world deployments, with various well-known BCI algorithms showing a pronounced performance differential to highly simplified lab experiments. The results also show significant performance differences among alternative methods, indicating possible trajectories for future improvements BCI methodology applied to complex real-world contexts.** 

**_Keywords—neuroergonomics, passive BCI, benchmark, dataset, experiment design_** 

## I. INTRODUCTION 

Over the past decade, numerous new applications have been found for Brain-Computer Interfaces (BCIs) outside their original field of use in clinical or rehabilitative settings [1][2]. Major thrusts along these lines have been workplace applications [3], such as driver state monitoring [4], workplace environments and entertainment [5], or military use [6]. However, BCI technology for these applications has yet to fully transition out of the lab, for reasons such as signal variability [7], depending on the type of environment, increased noise [8]. Against this background, the Cognition and Neuroergonomics Collaborative Technology Alliance (CaN CTA), a US-led research programme in Neuroergonomics, has recognized a need for publicly available datasets facilitating the development and benchmarking of BCI methods on complex, multi-faceted, and realistic tasks. Here 

Research was sponsored by the Army Research Laboratory and was accomplished under Cooperative Agreement Number W911NF-10-2-0022 (CAST 076910227001). The views and the conclusions contained in this document are those of the authors and should not be interpreted as representing the official policies, either expressed or implied, of the Army Research Laboratory or the U.S Government. The U.S Government is authorized to reproduce and distribute reprints for Government purposes notwithstanding any copyright notation herein. 

we present one of three large-scale datasets that were collected under the CaN CTA to address this need. In the following we summarize the task design (source code available at [9]) and data collection procedure, and then we describe an exemplary analysis on the resulting dataset. We illustrate both the challenges and opportunities opened by this new data corpus. 

## II. EXPERIMENTAL TASK 

## _A. Overview_ 

The task battery underlying this experiment was designed around a controlled but rich collection of subtasks, consisting of a sequence of foreground activities along with parallel side tasks. The experiment is loosely modeled after workloads encountered by operators of complex multi-display consoles such as those used in military vehicles (crew stations), although the stimulus material used here (graphics, sounds, text, and speech) was chosen to be generic and video game like. The task can be configured for one or two subjects, and data was collected with pairs of subjects. Note that, due to the complexity and richness of the task, some details of the design are beyond the scope of this paper and will be presented in a future article. 

## _B. Cognitive Processes of Interest_ 

The experiment is designed to elicit a variety of controlled cognitive processes in the subject, including perception, memory retrieval, decision-making, and response. The goal is to enable extensive post-hoc analysis to help answer diverse scientific questions relating to brain and behavioral states under complex settings, as well as to performance of various types of passive BCIs [10] in such scenarios. Due to its multi-task nature, the paradigm puts heavy emphasis on selective attention in visual and auditory domains. Also, throughout the experiment, task load, fatigue, and attention distribution are expected to vary, and individual tasks are designed to elicit frequent perceptual and response errors. To maximize the utility of the data, events are recorded in great detail and described using an ontology extended from the HED 1.0 event marker specification [11]. 

## _C. Spatial Layout_ 

The laboratory space, which includes two identical seats for the subjects, each equipped with three vertically mounted 

2577-1655/18/$31.00 ©2018 IEEE DOI 10.1109/SMC.2018.00023 

Authorized licensed use limited to: Univ of  Calif San Diego. Downloaded on August 01,2026 at 17:35:35 UTC from IEEE Xplore.  Restrictions apply. 

77 

1 of 1 

