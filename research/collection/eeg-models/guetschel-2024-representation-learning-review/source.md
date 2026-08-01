# **Review of Deep Representation Learning Techniques for Brain-Computer Interfaces and Recommendations** 

**Pierre Gueschel** _†_ **, Sara Ahmadi** _†_ **, Michael Tangermann** Donders Institute for Brain, Cognition and Behavior, Radboud University, Nijmegen, Netherlands 

E-mail: `pierre.guetschel@donders.ru.nl` 

### **Abstract.** 

In the field of brain-computer interfaces (BCIs), the potential for leveraging deep learning techniques for representing electroencephalogram (EEG) signals has gained substantial interest. This review synthesizes empirical findings from a collection of articles using deep representation learning techniques for BCI decoding, to provide a comprehensive analysis of the current state-of-the-art. Each article was scrutinized based on three criteria: (1) the deep representation learning technique employed, (2) the underlying motivation for its utilization, and (3) the approaches adopted for characterizing the learned representations. Among the 81 articles finally reviewed in depth, our analysis reveals a predominance of 31 articles using autoencoders. We identified 13 studies employing self-supervised learning (SSL) techniques, among which ten were published in 2022 or later, attesting to the relative youth of the field. However, at the time being, none of these have led to standard foundation models that are picked up by the BCI community. Likewise, only a few studies have introspected their learned representations. We observed that the motivation in most studies for using representation learning techniques is for solving transfer learning tasks, but we also found more specific motivations such as to learn robustness or invariances, as an algorithmic bridge, or finally to uncover the structure of the data. Given the potential of foundation models to effectively tackle these challenges, we advocate for a continued dedication to the advancement of foundation models specifically designed for EEG signal decoding by using SSL techniques. We also underline the imperative of establishing specialized benchmarks and datasets to facilitate the development and continuous improvement of such foundation models. 

_Keywords_ : Review, EEG, BCI, Representation, Embedding, Deep Learning 

Submitted to: _J. Neural Eng._ 

> _†_ These authors contributed equally to this work. 

_Review of Deep Representation Learning Techniques for BCI and Recommendations_ 

2 

## **1. Introduction** 

Representing high-dimensional data elements into lower-dimensional vectors usually facilitates their processing by subsequent machine learning algorithms. This representational process is called _embedding_ and is carried out by an _embedding function_ . The lowdimensional vectors obtained are called _embedding vectors_ or _embeddings_ also for short. In deep learning, we typically consider that any intermediate data representation of neural networks can be regarded as embeddings. However, in this article, we will focus on studies that either explicitly introspect, or that use algorithms that directly optimize the embedding. The terms _embedding vector_ and _representation_ will be used interchangeably in the following. 

For this article, we consider embeddings in the context of brain-computer interfaces (BCIs). BCIs are systems that allow direct communication from a subject’s brain to a computer, omitting motor output. This is realized by recording brain activity, decoding the recorded signals and interpreting the decoded information. The decoding outcomes are interpreted either as brain states of interest which are to be monitored over time, or as control commands that are send to the computer. State-of-the-art BCIs for controlling devices or computer applications decode changes of brain activity which are a response to either an external stimulus or the result of a subject actively executing a mental task. As brain activity is predominantly recorded via electroencephalogram (EEG), we will primarily focus on this type of BCI in this article. This recording modality has the advantage a relatively low cost compared to other recording techniques such as magnetoencephalography and functional magnetic resonance tomography, and is often preferred over local field potentials, signals from stereotactic EEG or electrocardiography due to its non-invasiveness. BCIs based on EEG reflects electrical brain activity with minimal delay and a relatively high temporal resolution, allowing to build applications which impose high demands in the temporal domain. Here, the data elements to be represented as embedding vectors consist of short windows of EEG time-series signals, i.e., epochs or trials. 

Embedding vectors serve as a fundamental framework for _transfer learning_ or _domain adaptation_ . These terms describe the approach to employ data, 

hyperparameters, trained models or other information which had been obtained from earlier recordings or earlier users to a novel recording or user. Transfer learning is of particular interest within the BCI community [46, 122], as it may help to solve a central problem in research and clinical applications of BCI: Training a decoding method from scratch for a novel user or session is challenged by a lack of time. However, there are several caveats to consider. Firstly, there may be potential changes in strategies between subjects. Secondly, the exact location, timing, intensities, and frequencies of neural activity may vary between individuals, along with their brain morphologies. Thirdly, individual lesions in stroke patients and individual progress patterns and deficits in neurodegenerative diseases can affect transfer learning. Lastly, various confounding factors such as medication, sleep patterns, imprecise electrode placements, artefacts and environmental factors can also lead to non-stationarities in the signals. 

This review is motivated by observing a growing number of publications in the BCI field during recent years, which have used embedding techniques. However, it is unclear which techniques are most commonly used to learn embeddings for BCI. In addition, it is not established which alternative deep learning approaches so far have remained unexplored in BCI and which benefits they could bring. Finally, it might also be valuable for the BCI community to see which purposes exactly serve the different types of embedding and how they can be benchmarked and introspected. 

In this review article, our focus is threefold. Firstly, we focus on the potential motivations researchers have for using embeddings. Indeed, we observe that the use of DL-based representations in BCI can be motivated by multiple different reasons. Secondly, this review article aims to draw the spectrum of possible methods that can be used for embedding learning, and more generally feature learning, using deep learning (DL) for BCI applications. Lastly, we look at introspection techniques for embeddings. These techniques can be informative for comparing and evaluating embeddings, and reveal what type of information can be obtained from them. Throughout this article we will explore the literature on deep representation learning for BCI. Additionally, we will have a view on studies involving non-BCI EEG data with the purpose to potentially identify research gaps 

_Review of Deep Representation Learning Techniques for BCI and Recommendations_ 

3 

in the BCI field. Furthermore, we will also provide examples from leading deep learning domains, such as computer vision, natural language processing (NLP), and speech processing, to illustrate the potential of deep representation learning for the field of BCI. 

This article is organized as follows: in Section 2, our approaches for retrieving and filtering articles and for extracting information are introduced. Section 3 explores different possible motivations for learning an embedding or using an algorithm that intrinsically does that. In Section 4, we will draw a list of the different approaches that have been used to learn embeddings in the BCI field. We will also report algorithms used in neighbouring fields for non-BCI, but EEG data, as they could be relevant for BCI. Finally, in Section 5, we will explore the different methods that have been proposed to benchmark, qualify, and compare the embeddings learned. 

## **2. Our Methodology** 

With the focus of this review article being on the intersection between the notions of _deep representation learning_ and _BCI_ , the first step has been to collect articles dealing with both topics simultaneously. Unfortunately, only few articles contain these exact keywords in their title or abstract and too many contain them in the main text body. Therefore, we had to establish a finer search strategy. 

This strategy consisted of first creating, for both of the two notions, a list of terms that were either equivalent or implying it. For example, the notion of _BCI_ can either be replaced by equivalents such as _brain-computer interface_ , and _brain-machine interface_ , or by specific paradigms that may imply a BCI, such as _motor imagery_ or _event-related potential_ . Similarly, the notion of _deep representation learning_ can either be replaced by equivalents like _deep learning_ + _embedding_ , or by techniques that inherently obtain a deep learningbased representation, such as _autoencoders_ . We noted the importance of accepting many different terms that describe potential deep learning methods which can learn an embedding. To compile this list of method terms, we used the review conducted by Roy and colleagues [99]. The query finally used in search engines was the conjunction (AND) between the disjunction (OR) of all the terms of the _BCI_ list and the disjunction of all the _deep representation learning terms_ . This query contains 65 terms in total. Note that a term can eventually contain multiple words (such as _deep learning_ ). AND, OR and the parenthesis are not considered terms. We restricted our search to articles published after 2014 because we did not expect any earlier relevant work involving both deep learning and BCI. Finally, we restricted our search to the titles only 

in the search engines. 

We initially started by using three search engines: Web of Science, PubMed and Google Scholar. Unfortunately, Google Scholar did not allow for nesting terms in parenthesis. In a second attempt, we computed the disjunctive normal form of our expression (which removes the need for parenthesis) but it resulted in a 8568 terms expression which hit the 150-word limit of Google Scholar. Therefore, we had to drop Google Scholar and only used Web of Science and PubMed. The matching articles were gathered using Publish or Perish [41] and organized using Zotero [116]. 

We found 87 articles from Web of Science and 43 from PubMed, which resulted in 101 articles after removing duplicates. This search was conducted on April 1<sup>st</sup> 2024. We read all the titles and found that 25 were off-topic, which left us with 76. Among those, five were behind a paywall for which we did not have access, three were not in English and one was not available. This left us with 67 articles. We read the 67 abstracts and found that eleven articles were still offtopic, which left us with a final selection of 56 articles. We included 25 additional articles post-search directly to the final selection. They were detected either in reference sections of the 56 articles or were selected based on our prior knowledge of the field. These additional articles also include non-BCI EEG studies which have applied techniques that can be interesting to the BCI community. A flow diagram summarizing the selection process is provided by Figure 1. 

Among the resulting 56+25 articles, many use similar techniques, in particular, 34 articles employed autoencoders to learn a representation. Because of such redundant approaches we refrained from discussing every single paper, but maintained all of them in our literature list. 

While reading the resulting 81 articles, our focus was on three aspects: 

- (i) the motivation(s) for learning an embedding, 

- (ii) the algorithms and approaches used for learning the embedding, 

- (iii) and the methods used for characterizing and introspecting the obtained embeddings. 

Our findings on these three aspects are respectively reported in Section 3, Section 4 and Section 5. The first aspect, the motivation authors had to learn an embedding, was not always explicit. We estimated their motivation by reading the Introduction and Discussion sections and by identifying the problems being addressed in the article. However, we refrained from interpreting why the authors used a particular method or made a specific design choice. The second and third aspects, algorithms and characterisation/introspection techniques, were 

_Review of Deep Representation Learning Techniques for BCI and Recommendations_ 

4 



<!-- Start of picture text -->
Google Scholar: 43 PubMed 87 Web of Science results  25 added<br>search impossible results post-search<br>Duplicate removal<br>101 results overall<br>Title screening<br>25 titles<br>76 titles on-topic<br>off-topic<br>Availability check<br>5 not free<br>3 not english 67 available<br>1 not available<br>Abstract screening<br>11 abstracts 81 abstracts<br>off-topic on-topic<br><!-- End of picture text -->

**Figure 1.** Flow diagram summarizing the process for selecting which articles from the initial search results to consider in this review. Blue boxes indicate the initial available sources and number of articles, red boxes indicate articles which were not considered for various reasons (see main text), and the green box represents the finally considered articles. 

usually clearer and less prone to interpretation. Their identification was done by respectively reading the Methods and Results sections. 

Because the goal of any review, including this one, is to provide an overview of the state-of-the-art for a research topic, the aspect (ii) on algorithms is central. It allows researchers entering the field to choose from the complete panel of methods at their disposition. However, to choose between the algorithms presented, researchers need to understand which needs each of these algorithm addresses, i.e., for what reason should one algorithm be preferred over another? Hence, the aspect (i) on motivations. Moreover, this section can also be used to help researchers entering the field identify their own motivations by reviewing a list of potential ones. Finally, the aspect (iii) on introspection techniques is necessary because the algorithms presented in this review are quite specific and the introspection methods commonly used in BCI to characterise classical machine learning algorithms may be of limited use only in this BCI context. Additionally, most of the introspection techniques presented simply take embedding vectors as input, without making assumptions about the algorithm that had been used to learn the embedding. Therefore, we will see how certain introspection methods commonly paired with certain algorithms can actually be paired with many other algorithms described in Section 4. 

## **3. Motivations to learn embeddings** 

In this section, we will report on which motivations were identified as leading to the use of a DL-based embedding or to the use of a method that inherently learns one. Please note that the motivations we list in the following are not exclusive and that the authors of a study can have multiple motivations for learning an embedding. Many of the motivations listed in this section are special cases of _transfer learning_ , which turned out to be a motivation in the large majority of the articles we reviewed for learning an embedding. In the following subsections, we explain why embeddings seem specifically suited for transfer learning in BCI. 

## _3.1. Improve classification accuracy_ 

Undoubtedly, most articles share the objective of improving the classification accuracy over the state of the art in a particular scenario. However, in some articles the reference to embeddings is only motivated by that reason (e.g. [25, 69]). While this is a legitimate motivation by itself, it does not tell us much about how the embedding is learned or why a particular algorithm was used. For this reason, we will not elaborate more on this motivation. 

_Review of Deep Representation Learning Techniques for BCI and Recommendations_ 

5 

## _3.2. Learning to become robust to noise_ 

EEG is sensitive to many sources in addition to the signal of interest. These additional sources can be, for example, non-physiological noise picked up by the system, muscular artefacts or other nonneural biosignals, or background brain activity. These additional sources are considered, in many cases, not relevant to the BCI task and typically they do not help the decoding, as they may fluctuate over time, showing non-stationary distributions. We observe that the least restrictive experimental protocols tend to be most affected by these undesired sources. Examples are dry or water-based EEG systems that are easier and faster to set up than gel-based ones, but are also more prone to noise. Similarly, real-world conditions are less constrained than lab conditions where subjects are asked not to blink and to remain still during the recordings. Here, the former will lead to more artefacts and non-stationarities in the signals. Therefore, it is desirable to have systems which have learned to be robust to these additional sources. 

We will see two methods that allow learning robustness. The first one, for robustness to noise specifically, is _denoising autoencoders_ [17, 91] that will be explained in Paragraph 4.2.2. The second method is through _data augmentations_ [96] which will be explained in Paragraph 4.3.3. 

## _3.3. Learning invariances_ 

This motivation addresses experimental scenarios or protocols which record brain signals under multiple _conditions_ . Typical conditions are the subject id, the session number, or the source dataset. Data collected over conditions can be expected to follow different distributions. The conditions usually are orthogonal to the main BCI classes, i.e., there can be examples with any combination of condition and BCI class. A model is said to be invariant with respect to a condition if the representation it produces does not depend on that condition. Learning domain-invariant representations is a typical approach to _transfer learning_ because it allows using the same representation on multiple data distributions. The notion of invariance is close to that of robustness described in Subsection 3.2. However, we made a distinction between the two as in the case of robustness, we will systematically refer to factors that are only obstacles to the decoding (such as noise and artefacts), whereas in the case of invariance, we will refer to contextual information for which a conscious choice is made to maintain invariance. 

We will see in Paragraph 4.4.2 that invariant representations can be learned through an adversarial objective [47] or by using deep metric learning [36], see Subsection 4.5. 

## _3.4. Learning from small datasets_ 

The ability to learn from as little as possible data while still reaching satisfactory classification scores is desirable in BCI systems for two main reasons: First, it allows for the quick start of BCI applications because only a small amount of calibration data needs to be recorded. Second, BCI datasets are quite small in general. 

_Shortening calibration times_ can be addressed with two different types of algorithms: algorithms able to exploit very well the few available examples of the ongoing session [106, 110], or algorithms that can take advantage of existing data recorded before the current session such that only little adaptation is needed for the ongoing session [37, 57]. The former is generally not a strong point of deep learning models but rather of classical machine learning models that exploit expert knowledge, e.g., in the form of domainspecific regularization approaches [104, 105, 106, 110]. The latter is better known as _transfer learning_ , and using it is nearly always motivated by the reduction of calibration times. 

_Tackling small datasets_ essentially involves the same principle as _shortening calibration times_ , hence it can also be done in two different ways: either by simply exploiting well the small existing datasets or by pre-training models on other types of datasets. Most of the algorithms we will mention in this article allow for some form of transfer learning. However, we will see in Paragraph 4.0.2 that unsupervised algorithms are particularly useful for this purpose as they allow the use of non-BCI EEG datasets that are much more abundant [78]. The unsupervised algorithms will be described in detail in Subsections 4.2, 4.3, 4.4.1 and 4.5. 

## _3.5. Bridging heterogeneous components_ 

Raw data elements generally have intrinsic structures: An image has a width and a height, a text has a certain number of words, and an EEG recording has a duration, sampling rate and a specific spatial layout of recording channels. These intrinsic structures define a relation of the features contained in an example: the pixels of an image, the words of a text, and the samples of an EEG recording follow specific orders. Each data type requires specialized layers in DL architectures and/or pre-processing steps to capture their internal structures. These layers and steps are necessary to transform the data elements into _forms_ that allow for better processing by the following classifiers (or classification layers). As explained in the Introduction (Section 1), these forms are called embeddings, i. e., collections of features, where the eventual purpose of each feature is automatically defined by the training 

_Review of Deep Representation Learning Techniques for BCI and Recommendations_ 

6 

algorithm. We observed in the literature that an embedding can be used as an algorithmic bridge in multiple ways: 

_3.5.1. Between different types of algorithms._ Because there is no a priori hypothesis about the features of an embedding, virtually any classification or regression algorithm can use embedding features as input. Therefore, it is common to use an embedding as a bridge between different types of decoding algorithms [37, 124]. A typical scenario uses a deep learning model as feature extractor and a classical machine learning model to decode those features. This configuration can be employed for transfer learning scenarios. 

_3.5.2. Between different data types._ Because the purpose of each feature in an embedding is learned automatically by the algorithm, it is possible to design the learning task such that different data types can be projected into a common embedding space. Even if every data type requires a different processing pipeline, they can all produce an embedding of the same dimensionality. Then, techniques exist to align the embedding spaces of different data types according to their semantic similarity. This so-called _joint embedding learning_ is commonly used to relate image and text data into an embedding [52, 63], but first publications have now shown, how joint embeddings can be learned also for EEG and MRI data [28]. 

_3.5.3. Between different recording systems._ Despite existing norms for EEG electrode placement, there are many different EEG systems available, all with particularities and slight variations. Additionally, not all datasets are recorded using the same set or even the same number of channels. To address this obstacle, recent studies have begun investigating architectures that can receive recordings from multiple different channel sets as input [130, 35, 120, 126, 13], see Paragraph 4.3.2. These architectures show promise for transfer learning or for handling corrupt channels. 

_3.5.4. To enforce multiple objectives._ Finally, the embedding can enable the combination of multiple high-level objectives as in the following example: During training (in opposition to joint embeddings) a single processing pipeline is employed to create the embedding layer. From this point on the processing can be split into multiple branches, each computing a specific objective. Finally, the global loss would be a weighted sum of these different objectives. In this scenario, the embedding provides a high-level representation of the data which tends to satisfy all the different objectives. One could 

want to enforce multiple objectives simultaneously, for example, to both optimize the performance of the model on a BCI task and to obtain a subject-independent representation as proposed by Ozdenizci and colleagues [82], see Paragraph 4.4.2, or to simultaneously enforce a supervised and an unsupervised objective for the purpose of mitigating the risk of overfitting and enhancing generalization, see Li and colleagues [62] and Subsection 4.3. 

## _3.6. Uncover the structure of the data_ 

Finally, self-supervised learning (SSL) algorithms differ from the aforementioned approaches by not relying on labelled data (see Subsection 4.3). Instead, they learn representations in a data-driven manner. As a result, the patterns that emerge when summarizing datasets using visualization methods such as UMAP (see Subsection 5.3) may reveal underlying structures in the data, rather than simply reflecting the prior assumptions of an experimenter. In this direction, Banville and colleagues demonstrated that the representations learned through SSL contained structures that translated physiological and clinical phenomena [9]. This finding highlights the potential of SSL algorithms to uncover meaningful structures in complex data. 

## **4. Approaches used to obtain embeddings** 

Here, we will try to draw an exhaustive list of all the algorithms and methods that can be put into place to meet the objectives described in Section 3. We distinguish two types of algorithms which learn representations in either a supervised or unsupervised way. 

_4.0.1. Supervised methods._ We say an algorithm is supervised when it directly exploits examples with human-annotated labels. In BCI, such labels can for example be the type of mental imagery task being executed, or the stimulus attended during an epoch, i.e., the BCI classes. In general, such examples have to be recorded under controlled conditions where the participant has to execute a pre-scripted task, as opposed to online/free BCI control. The representations learned in this way are typically only tailored for the task corresponding to the labels and do not generalize well. 

Not many of the reviewed articles learn a representation in this supervised manner. Nevertheless, in Subsection 4.1, we described one very simple example. In Subsection 4.5, we will see how metric learning can also be used to learn embeddings in a supervised way. Yet, supervised learning is often used to fine-tune 

_Review of Deep Representation Learning Techniques for BCI and Recommendations_ 

7 

pre-trained models. In such a case, the supervised algorithm does not properly learn the embedding but rather uses it and eventually improves it. 

_4.0.2. Unsupervised methods._ Algorithms implementing unsupervised learning do not use human-annotated labels [49]. This bears the advantage of being able to be trained on any raw EEG signal, i.e., not necessarily recorded under a BCI protocol, which is far more abundant than labelled recordings of BCI sessions. It is generally the class of unsupervised algorithms that is employed to train so-called _foundation models_ , i.e., general-purpose embeddings trained from large amounts of data. In a typical scenario, an unsupervised algorithm pre-trains a neural network on what is called a pretext task, and a supervised algorithm later on fine-tunes it, or part of it, on what is called a downstream task. In the context of BCI, downstream tasks can be the classification of an imagined or executed movement, of attended vs. ignored stimuli, of sleep stages, the detection of seizures, emotions, or the regression of the level of mental workload, of the level of drowsiness, etc. We will see in the following sections some pretext tasks that can or could be used in BCI. 

The overall goal is typically to obtain a good score on the downstream task, and the goal of the pretext task is to provide a pre-trained network that can already extract information relevant to the downstream task. If the pretext task manages to learn information relevant to the downstream task, the workload of the latter is alleviated. This way, the network might need fewer examples from the downstream task to be fine-tuned. Because the pretext and downstream tasks are inevitably different to some extent, the data features that must be learned to solve each of them are also different. This leads to the question of how similar a particular pretext task is compared to actual BCI tasks (i.e., downstream tasks), or slightly rephrased, whether a given pretext task is general enough to learn a representation that is sufficiently general to contain information that is relevant to (various) BCI classification tasks. 

Many different unsupervised algorithms exist, each with its own way of relating to the notion of an embedding. In Subsection 4.2, we will review articles realizing autoencoder paradigms and variants of it as pretext tasks. Then, in Subsection 4.3, we will look at the subfield of unsupervised learning that uses pseudo labels, called self-supervised learning (SSL). In Paragraph 4.4.1, we will see how generative adversarial network (GAN) can be used for unsupervised representation learning. Finally, in Subsection 4.5, we will show how metric learning techniques can be realized in unsupervised manners. 

## _4.1. Hidden layer of a classification network_ 

The simplest approach one can think of to obtain an embedding is to train a feed-forward neural network with at least one hidden layer on a classification task, i.e., using a cross-entropy loss. Here each output node of the network will correspond to a specific class. Receiving a novel input example, the task of each output node is to predict the probability that the true class label is that of the node in question. To obtain as many outputs as there are classes, there is usually a fully connected layer that linearly maps the latent representation from the last hidden layer to these outputs. This last latent representation can be considered as an embedding, and it is common to treat it as such [37], i.e., re-using that representation for other purposes, analysing the information contained in this latent representation, etc. This method has the advantage of being extremely simple to implement. In addition, it is generally more computationally efficient than most unsupervised methods. However, this simple method produces representations that are very targeted, which means they are typically not transferable to other tasks and sometimes not to other distributions as well. 

To obtain more flexible representations, it is common to use multiple objectives simultaneously, i.e., multi-task learning. For example, one can enforce the representation to be invariant to the subject in addition to allowing the classification of mental imagery tasks. We will see in detail how such domain-invariant representations can be learned in Paragraph 4.4.2. Another approach consists of representations that allow the reconstruction of the original input. This can be achieved by combining the classifier with an autoencoder [24], c.f. Subsection 4.2. 

## _4.2. Autoencoder_ 

Autoencoders encompass relatively well-established methods for unsupervised representation learning [8]. In their canonical form, their architecture can be decomposed into two parts: an _encoder_ and a _decoder_ . The encoder takes as input an example _X_ and returns a hidden representation _z_ . The decoder takesestimationas inputof thetheoriginalrepresentationinput _X_ ˆ _z_ . andThereturnsobjectivean isandto theminimizeoriginaltheinputsdifference _X_ ˆ andbetween _X_ . Typically,the estimatedthe dimension of the hidden representation _z_ is smaller than that of the input _X_ such that the network learns to extract important features from the input data, which are necessary to reconstruct the original input. Autoencoders are unsupervised and can virtually be applied to any type of input. Over the years, a significant amount of variants were developed. This 

_Review of Deep Representation Learning Techniques for BCI and Recommendations_ 

8 

is reflected in the 34 studies we have found using autoencoders. 

_4.2.1. VAE._ Variational autoencoders (VAEs) is a variant in which the latent representation predicted by the encoder is not directly fed to the decoder, but rather used as parameters for a random distribution, typically an isotropic Gaussian. Then, a point sampled from this distribution is given to the decoder as input [8]. Modelling the problem in this way allows to gain control over the meaning of a latent representation, which would not be possible with a regular autoencoder. Additionally, depending on the distribution used, it can force the hidden representation to have disentangled features [43]. These reasons might explain why VAEs have been well adopted by the BCI community. For example, Ozdenizci et al. used them in combination with adversarial networks (c.f. Subsection 4.4) to learn subject-invariant representations of motor imagery recordings [81]. 

_4.2.2. DAE and MAE._ Denoising autoencoders (DAEs) and masked autoencoders (MAEs) are variants where the input for the encoder is corrupted, either by adding noise or by masking parts of it. Nevertheless, the output of the decoder is still compared to the original unaltered input. This way, the network can learn how to handle noisy or corrupted input examples. These are interesting characteristics for EEG data and explain why they are commonly used [19, 123, 91, 17]. 

_4.2.3. SAE._ Sparse autoencoders (SAEs) differ from regular autoencoders in that they enforce sparsity in the hidden representation through an additional loss term. Sparsity means that only a small number of dimensions of the representation are simultaneously non-zero. The sparsity is typically enforced by adding a penalty term which enforces a minimal Kullback-Leibler (KL) divergence [59] between the average activation of each hidden unit and a sparsity hyperparameter. Liu et al. [70] proposed a deep learning architecture for EEG-based emotion recognition, which consists of a convolutional neural network (CNN) for feature extraction, followed by a SAE and a multilayer perceptron (MLP) classifier. Their approach involves training the CNN in a supervised manner, then discarding the linear classification layer and training the SAE in an unsupervised way using the CNN features. Finally, the MLP is trained in a supervised way using the SAE features. Their results support that the proposed approach outperforms other methods, including the CNN part alone. Qui et al. [91] proposed an approach combining denoising and sparse autoencoders 

for seizure detection. They demonstrated that the joint use of these two techniques resulted in better performance than either approach used independently. The DAE component was shown to prevent overfitting and improve the robustness of the model to noise, while the SAE allowed for the learning of higher-level features in the EEG data. 

## _4.3. Self-Supervised Learning (SSL)_ 

Self-supervised learning (SSL) is a form of unsupervised learning that uses pseudo labels, or automatically generated labels, to train a network [49]. Designing these pseudo labels is typically done by using known properties of the data, e.g., an example is similar to itself, a time sample comes before the next one, samples from different channels are correlated, etc. A pseudo label could be, for example, the chronological order of different time windows of a recording. The unsupervised learning is guided by the necessity to create pretext tasks which either are similar to the downstream tasks or sufficiently general to learn features that would be relevant for them. SSL have been extremely successful in the fields of computer vision [16, 10], speech processing [6] and NLP [23]. 

As the topic is fairly new, it is still relatively unknown within the BCI community. Out of the 13 studies we found using SSL with BCI data, 10 were published after 2021. 

_4.3.1. SSL Tasks Using Temporal Structure._ In their early 2021 study, Banville et al. [9] compared three different SSL pretext tasks that all exploit the temporal structure of EEG recordings. The first task, _relative positioning_ , consists of predicting whether two time windows were within a certain distance or further apart. The second task, _temporal shuffling_ , requires to determine if three time windows are in the correct order or not. The last task, _contrastive predictive coding_ , uses a number of consecutive windows and distractors that had been sampled elsewhere. The first two consecutive windows constitute the context. The task is to predict, for each other window, whether it is following the context or is a distractor. A similar approach was taken by Ou and colleagues [80]. 

_4.3.2. Masking-based SSL._ Also in 2021, Kostas et al. [58] published an SSL method called wav2vec that was originally developed for speech processing [6]. Wav2vec shares similarities with masked autoencoders (c.f. Paragraph 4.2.2), where temporal regions of the signal are masked, but directly optimises the distance between embedding vectors instead of going back to the input space. This work sparked a number of studies, which also experimented with temporal masking strategies [42, 13, 21, 62, 30]. 

_Review of Deep Representation Learning Techniques for BCI and Recommendations_ 

9 

Most masking-based SSL studies rely on transformer architectures [117]. This is because the attention mechanism of transformers allows the network by design to selectively focus on the unmasked portions of the signal and predict the masked portions. Yang and colleagues pioneered the use of transformers with independent encoding of the EEG channels [126]. This novel approach enables the exploration of masking strategies over the channels that allow to pre-train an attention mechanism over the channel structure. Such pre-trainings pave the way for the development of pre-trained models that are independent of specific channel sets. Subsequent studies by Li et al. and Guetschel et al. further expanded on this concept with a domain-inspired spatial masking strategy [62, 35]. 

_4.3.3. Augmentation-based contrastive SSL._ As a third pioneering article (2020), Mohsenvand and colleagues experimented with SSL based on data augmentations [75], and were followed by Yand and colleagues [127]. The general idea of such methods is to _first_ sample two data augmentations from a pre-defined family of plausible augmentations. In the image domain such augmentations could be a combination of cropping, rotation, colour shift and addition of noise. Sampling an augmentation would then mean sampling a set of parameters for cropping, rotating, shifting the colours and adding noise. _Second_ , the two augmentations are applied to the examples of the batch, resulting in two augmented versions of every example. _Third_ , the augmented examples are passed to a network to obtain embeddings. _Finally_ , the loss function enforces the embeddings of the two versions of each example to be either similar (non-contrastive) or to share a higher similarity with each other than with the representations of the other examples in the batch (contrastive). 

Plausible and efficient augmentations are different for each domain. Domain knowledge about EEG signals and neural processes can guide the design of novel, plausible data augmentations for BCI. For example, a slight shift in the orientation of the source dipoles [140] or of their amplitude [14] are plausible and can be used as data augmentation. However, it is not established which augmentations would be the most efficient for self-supervised representation learning with BCI data and EEG processing in general. Rommel et al. [97] reviewed data augmentations which have already been tested on EEG data. The authors underline that different BCI tasks require different data augmentations. They also recognize that the list of augmentations that have already been introduced for or tested on EEG signals is probably not exhaustive and new ones could still be discovered. 

Overall, the field of SSL remains relatively 

unexplored in BCI but is part of the _hot topics_ in deep learning. The BCI community would probably gain much from exploring SSL further. 

## _4.4. Adversarial network-based training_ 

Some learning objectives are complex, i.e., non-trivial to compute. In other words, they can not simply be evaluated by non-parameterised loss functions such as the mean squared error, or the cross-entropy loss. Such complex objectives may, for example, maximize the level of realism of a generated example [27], minimize the mutual information between two embeddings [47], or minimize the amount of domain-specific information present in a latent representation [81]. To enforce such complex objectives, it is possible to utilize _auxiliary_ neural networks. These auxiliary networks can deliver richer feedback to the main networks than a nonparameterized loss functions. The specificity of the methods presented in this section is that their auxiliary networks all learn to maximize their objective, whereas their main networks are trained to minimize it. For this reason, these auxiliary networks are actually called _adversarial networks_ . In mathematical terms, the objective function being optimized is the _minimum_ over the possible main networks of the _maximum_ over the possible adversary networks of the loss function. 

_4.4.1. Generative adversarial networks._ A specific case an adversarial network training can be found in generative adversarial networks (GANs), where the main network is called _generator_ and the adversary network is called _discriminator_ . The generators are optimised for generating realistic data from random noise vectors, and the discriminators are trained to discriminate if the examples they receive as input are real or have been artificially created by the generators [34]. 

In the image domain, Radford et al. emphasized that GANs can be used to learn representations in an unsupervised way [92]. Indeed, the discriminators can take as input any kind of data and are trained on a relatively high-level task (depending on how good the outputs of the generator are), such that there is a good chance to find features relevant to other learning tasks in their hidden representations. Furthermore, it has been shown by Vondrick and colleagues that relevant features can be learned from video data this way [118]. However, GANs are known to be difficult to train (long and unstable) such that their use as unsupervised feature extractors remains marginal in general. 

In the context of BCIs, we did not find any article using them for that purpose, but it could be worth investigating this further. However, there are many successful examples of GANs being used to 

_Review of Deep Representation Learning Techniques for BCI and Recommendations_ 

10 

generate fake BCI examples in the context of data augmentation [40, 32, 27]. 

_4.4.2. Domain-invariant representations._ A particular use of adversarial networks is to learn domaininvariant representations. In the context of BCI, the domains are typically the subjects or the sessions, but they can also be the recording equipment, the dataset, the stimulation parameters, or factors. A domaininvariant representation is particularly interesting for cross-domain transfer, e.g., if we have a decoding model pre-trained on multiple subjects and want to apply it to a novel one. Transfer learning is one of the current challenges of BCI [121]. 

To enforce representations to be domain-invariant, a usual objective of adversarial networks is to identify from which domain the input examples come. In this context, the auxiliary networks taking the adversary role are often called _domain discriminators_ . The objective of the main network is partly to fool the domain discriminator by leaving no domain-specific information in the representations they generate and partly to complete another task such as classification [31, 102]. 

¨Ozdenizci and colleagues implemented this for subject-independent motor imagery feature extraction [81, 82]. Their adversarial network is trained to discriminate the subjects and is paired with a VAE (see Paragraph 4.2.1). 

Jeon and colleagues argued that using a domain discriminator can introduce problems like discard classrelevant information, also referred to as _negative transfer [83]_ . They instead trained their adversarial network to estimate the mutual information between _class-relevant_ and _class-irrelevant features_ [47]. Their main network’s objectives are to minimize the mutual information between the _class-relevant_ and _classirrelevant features_ and to classify motor imagery examples using the _class-relevant features_ . Note that Jeon et al. used the term _adversarial learning_ which to our knowledge is slightly unconventional in this context while it commonly describes attacks on models (i.e., reverse engineering, trying to fool the models, etc.). 

## _4.5. Deep metric learning_ 

Deep metric learning is a sub-field of deep learning focussed on training neural networks to embed examples into vector spaces whose metrics implement _notions of similarity_ between examples. A typical notion of similarity would be class membership: examples from the same class would be considered more similar, i.e., close to each other in the embedding space, than examples from different classes. It is possible to define notions of similarity even without human-annotated labels by using pseudo labels or 

by simply considering that an example is _similar_ to itself. These cases will also be referred to as SSL (see Subsection 4.3). 

A loss function commonly used for deep metric learning is the _triplet loss_ [101]. The triplet loss takes three examples as input: an anchor, a positive and a negative example. The anchor and the positive examples are expected to be similar, while the anchor and the negative ones are dissimilar. The loss minimizes the distance between the representations of anchor and positive and at the same time also maximizes the distance between the representations of anchor and negative. Most of the loss functions used for deep metric learning are relatively similar to the triplet loss or the _contrastive loss_ [38] which does not involve negative examples. A particularity of deep metric learning techniques is, that even if they can be supervised, they directly optimize the representations or the embedding space. In other words, the data representations are obtained explicitly and not merely as a side-product. Deep metric learning is frequently used in computer vision for tasks such as face recognition [101] or place recognition [2]. In these tasks, the class is the identity of the person on the picture or the place where the photo was taken. These tasks have in common that they usually have only a few examples per class but many different classes. Additionally, they require models which can work on classes that were unseen during training. This last requirement makes it impossible to use regular classifiers for these tasks. 

Schneider et al. [100] used a variation of the triplet loss and introduced a novel triplet sampling scheme for learning embeddings for neural data jointly with behavioural data and/or time. Triplet sampling holds an important role in metric learning [101]. While the authors tested their framework only on animal data, it would be interesting to investigate its use on human data and eventually for BCI. 

For BCI data, Guetschel et al. [36] developed a variation of the triplet loss that allows creating a hierarchical structure in the embedding space according to metadata associated with the recordings. In their framework, the hierarchy between the different meta-labels is defined by the researcher using expert knowledge. The authors demonstrated their framework by structuring the embedding space according to the subjects and motor imagery class labels, but this approach could theoretically be applied also to structure according to sessions, datasets or paradigms. 

Studies exploiting metadata are at the border between supervised and unsupervised learning as they effectively use labels, but these metadata labels usually come ”for free”. On the other hand, contrastive losses 

_Review of Deep Representation Learning Techniques for BCI and Recommendations_ 

11 

can also be used to simply separate the classes as an alternative to a classification task [89]. 

Looking at the successful examples of deep metric learning techniques for face recognition, which works even for subjects outside the training set, we might wonder if this concept is not under-exploited for BCI data. Indeed, we typically restrict ourselves to only a few classes in BCI, but the use of deep metric learning techniques could potentially deeply transform the BCI domain by, for example, allowing to learn from 24/7 multimodal recordings with both EEG and video for action recognition. 

## **5. Characterizing embeddings** 

In most studies, the introspection effort invested to characterize the learned representation is shallow and limited to simple score comparisons with a few baselines. This limited approach can often miss important details about the learned representations. Fortunately, more elaborate techniques exist for introspecting DL-based embeddings, which can provide valuable insights into the learned representations. In this section, we will stress the importance of having common benchmarks with commonly agreedon fine-tuning procedures to reliably compare a novel technique for obtaining an embedding with other existing techniques. We will also explain how the score on the pretext task can be used to better understand an embedding. Finally, we will see projection methods for visualizing embeddings in lower dimensions, where it can be easier for humans to obtain insights. 

## _5.1. Score on downstream task_ 

While the performance an embedding enables for various tasks is a very high-level characteristic, it nevertheless is important. For testing how well an embedding will perform in transfer learning scenarios or to compare pretext tasks, specific benchmarks are required. The MOABB library [3] allows for rigorous benchmarking models on between-sessions and between-subject transfer scenarios with motor imagery, event-related potential (ERP), c-VEP and SSVEP datasets [18]. However, these evaluations are not meant to allow fine-tuning the models on the target distribution. This fine-tuning aspect was addressed in the 2021 BEETL competition [121]. In this competition, the participants had to solve a crossdatasets transfer task for motor imagery BCI data. They received a few labelled examples also from the final test dataset, which makes this competition similar to a transfer-learning-with-fine-tuning task. However, the participants of the BEETL competition were allowed to use the data as they wished. Therefore, the challenge was simultaneously testing the initial 

training strategy and the eventual fine-tuning strategy of the participants. 

_5.1.1. Intertwined evaluation._ In general, the performance score on a downstream task provides an intertwined evaluation of both the embedding method and the fine-tuning method. Yet, the methods involved in both are independent and thus should be evaluated separately. This separation is already common in the image domain [10, 22]. To only test the initial training, i.e., compare different pretext tasks, the typical approach is to always use the same fine-tuning strategy. A first fine-tuning strategy is to continue the training of the whole network for a fixed number of epochs but on the downstream task and with examples from the target distribution [58]. This strategy can be computationally heavy and may easily overfit depending on the amount of fine-tuning data. A second fine-tuning strategy also commonly used in representation learning is to train a linear classifier on top of the frozen representations [49, 10]. This strategy produces reproducible results, and its simplicity favours methods able to extract representations which are easy to classify according to the downstream tasks. It thus may not obtain the best classification scores, but this is not crucial for benchmarking purposes. Unfortunately, it is not always possible to use this so-called linear probing, depending on the SSL strategy used [35]. 

_5.1.2. Multiple downstream tasks._ Furthermore, a single downstream task is insufficient for the evaluation of models that claim a certain generalization characteristic, e.g., a EEG representation learned by unsupervised methods which shall be used for different BCI protocols as well as sleep staging, emotion recognition etc. Instead, benchmarks containing sets of tasks are required, comparable to the benchmarks used in the image or language domain. For NLP, the GLUE benchmark [119] evaluates models on a range of natural language understanding tasks, while the SQuAD benchmark [93] evaluates models on question-answering tasks. In computer vision, commonly used classification benchmarks are ImageNet [22], Places205 [139], VOC07 [26], and iNat18 [115]; and for object detection or segmentation, VOC07+12 [26], and COCO [67] are often used. The development of these benchmarks has played a crucial role in advancing the field of NLP and computer vision. 

Similar benchmarks are needed for BCI to evaluate general-purpose embeddings. In particular, such a benchmark would need to include all types of BCI tasks and should reflect a diversity of user groups, noise conditions, number and placements of recording channels, recording qualities, number of calibration examples and contamination with artefacts. 

_Review of Deep Representation Learning Techniques for BCI and Recommendations_ 

12 

Aspects like the number of calibration examples, the number of channels, and the presence of noise or artefacts, can be simulated by applying corruptions or ablations to datasets. Such transformations are already used in studies for testing the robustness of models [77, 37, 19, 126]. Unfortunately, the approaches are not consistent over publications, which makes comparison between studies difficult. Normalizing these corruptions or ablations could be an option for establishing a standardized benchmark, allowing for more consistent and comparable evaluations across studies. 

_5.1.3. Community adoption._ Finally, a good benchmark is one adopted by the community. If each article reports its results on a new benchmark, the authors should also provide baseline performances. The high demands on computing resources in deep learning limits the number of baselines a new approach can be compared against. Additionally, there is always a concern that authors applying a method as a baseline may not be using it to its fullest potential, whether intentionally or not. For instance, a baseline method may be poorly optimized or implemented, leading to sub-optimal results. 

In summary, the BCI community requires benchmarks that can evaluate general-purpose embeddings across a full range of tasks, have a deterministic finetuning procedure, and are widely adopted by the community for systematic model testing. 

## _5.2. Score on pretext task_ 

Obtaining a score evaluating the performance of a network on a pretext task is straightforward, as each task comes with its own intrinsic metric. It can simply be the value of the loss function or an accuracy score for tasks involving classification. However, these scores are not ideal for comparing different pretext tasks with each other because they are heterogeneous. Nonetheless, scores on pretext tasks should not be disregarded, as they still provide important information which can complement downstream task scores. In particular, they can help with introspecting the embeddings learned by the model and their generalization abilities. For example, in Banville et al. [9], plotting pretext and downstream task performances simultaneously allowed for a comparison of task difficulty and downstream benefits. Kostas et al. [58] used the score on the pretext task to evaluate its difficulty with respect to its main hyperparameter. This relation between difficulty and hyperparameter allowed them to speculate on how the network was solving the task. Additionally, the low variability of the score on the pretext task across subjects, hardware, and tasks, allowed them to claim 

that the learned embeddings had good generalization abilities. Overall, while pretext task scores should not be used to compare different pre-training methods together, they are useful for introspection during the development of a given pre-training method. 

## _5.3. Introspection by lower-dimensional visualizations of the embedding vectors_ 

Embedding vectors typically have a few hundred dimensions. Therefore, these vectors can not directly be visualised. Thus it is common to first project embedding vectors into a two-dimensional space. Then, all the examples of the dataset can be visualized simultaneously as a 2D scatter plot, each point representing a different example. This type of plot allows to obtain insights about the distribution of the data in the original embedding space. Additionally, it is common to colour the examples according to a label, typically the label corresponding to a downstream task [9, 36, 37, 54, 47], but we sometimes encounter colourings corresponding to the age, gender, date, presence of a pathology [9], continuous behavioural labels [100], the subject id [36] or other meta-data. A colouring can be applied to investigate how difficult it will probably be to separate the learned features according to the label. The examples can also be coloured according to whether they belong to the train or the test set. A comparison of the two distributions would allow inspecting potential non-stationarities between the two sets, which may impact the generalization abilities of the model. Such comparison is particularly beneficial for transfer learning scenarios. An example of such a projected plot can be found in Figure 2. 

Naturally, some information is lost in the projection. Thus the different projection methods are required to intrinsically make assumptions about the type of information that is important and should be preserved. The following paragraphs describe the most commonly used methods for embedding vector projections. 

_5.3.1. PCA._ A well-established technique that linearly projects data into a new coordinate system is principal component analysis (PCA) [111]. The coordinates of the new system are arranged in decreasing order of the variance, which the original data displays in each novel coordinate. To reduce the dimensionality of the embeddings, one typically choses the first two dimensions of this new coordinate system. Therefore, we see that PCA gives importance to the variance of the data: only the directions with the highest variance between the embedding vectors will be represented in the projection. 

_Review of Deep Representation Learning Techniques for BCI and Recommendations_ 

13 

Because the projection is linear, the aspects of the original high-dimensional embedding space represented by it are faithful. However, variance as a measure of importance for the dimensions may not be a relevant criterion to describe the data. Nevertheless, PCA is the least computationally expensive one for visualising embeddings out of the three methods identified by this review [39]. 

_5.3.2. t-SNE._ The t-distributed stochastic neighbor embedding (t-SNE) [114, 44] is also a well-established, but non-linear method for dimensionality reduction. It first models the embedding vectors as a graph where each node is one vector and where edges represent a pairwise similarity between vectors, i.e., a normalized version of their Euclidean distance. Then, it builds a low-dimensional projection of each embedding vector along with a graph following similar principles as the original graph. The projections are optimized such that the Kullback-Leibler divergences between the edge weights of their graph and those of the original graph are minimized, i.e., it enforces the graphs in both, the high- and the low-dimensional space to be similar. 

This procedure preserves local structures: embedding vectors which are close to each other will also be close to each other after the projection. However, with the random initialisation of the projections originally proposed, t-SNE does not allow to preserve the global structure [56]. Thus the distances between eventual clusters in the projected space should not be interpreted. 

Finally, in current implementations, t-SNE is significantly more computationally expensive than PCA. It has a complexity of _O_ ( _n_<sup>2</sup> ) with _n_ the number of embedding vectors and assuming that _k_ , the number of projected dimension, is small ( _k ≤_ 3) [114]. 

_5.3.3. UMAP._ Uniform manifold qpproximation and projection (UMAP) [73] is the most recent of the three methods presented here. It is very similar to t-SNE, but it has been formulated using stronger mathematical principles to guide its design choices. In particular, it is better than the original formulation of t-SNE at preserving the global structure of the original embedding space as discussed by Oskolkov [79] because of its initialisation and the choice of crossentropy for the loss function. Also, it is less computationally expensive than the original t-SNE while still being significantly more expensive than PCA [72]. Its complexity is _O_ ( _n_<sup>1</sup><sup>_._14</sup> ) [73]. However, It was recently shown [56] that t-SNE can preserve the global structure as well as UMAP if its random initialisation is replaced with a PCA initialisation. Also, recent optimized versions of t-SNE, such as fast Fourier transform (FFT)-accelerated interpolation- 



<!-- Start of picture text -->
subject = 1 subject = 4<br>subject = 8<br><!-- End of picture text -->

**Figure 2.** Example of UMAP-projected visualisation of embeddings. _Figure description._ In this figure, each point corresponds to one embedding vector. Its color denotes the class labels. The sub-plots depict embedding vectors obtained for different subjects, but all vectors were generated by the same embedding function. The sub-plot of test subject 1 is marked by a red frame. The topographic isolines in the background indicate the four class distributions as derived from the complete data of all subjects. The plots of only three subjects are displayed here for space reasons. _Comments._ This plot was used to realize that overall, the features learned were relevant for the targeted classification task, even for the test subject. Additionally, it indicated a hierarchy in the difficulty to separate the different pairs of classes. The topographic isolines in the background served as a visual reference to compare sub-plots and allowed to observe distribution shifts between the embeddings of different subjects. _Source:_ Guetschel et al. 2022 [37]. 

based t-SNE (t-SNE) [68], seem comparable to UMAP in terms of speed when projecting data into 2D or 3D [55]. Still, UMAP can effortlessly scale up with the projection dimension _k_ whereas t-SNE’s complexity grows exponentially with _k_ [73]. Increasing _k_ is not relevant for visualisation purposes but can be if we want to use these algorithms for dimensionality reduction, for example, before applying a clustering approach. 

## _5.4. Visual qualitative evaluation_ 

A visual qualitative evaluation of embeddings can be achieved using conditioned generation techniques. These techniques involve a neural network, typically called _generator_ , whose objective is to generate artificial examples (i.e., EEG epochs) that are as similar as possible to real examples. In this context, the only information the generator receives about a target (real) example that is to be imitated, is an embedding vector that represents it. For this reason, 

_Review of Deep Representation Learning Techniques for BCI and Recommendations_ 

14 

we say that the generation process is _conditioned_ by an embedding vector. Assuming the generator is properly trained, the similarity between the artificial and the real examples is limited by the information contained in the embedding vectors which act as a bottleneck. If a example is perfectly represented in its embedding vector (i.e., without information loss), then a welltrained generator will be able to reconstruct it exactly. If some information is lost by the embedding, however, then the generator can only ”guess” the original input. Visually comparing an artificial example and its target is a way to evaluate which information was lost and which was maintained in the corresponding embedding. Views of these examples can also be visualised in the form of spatial patterns [64] of frequency spectra [132]. 

Autoencoders (c.f. Subsection 4.2) intrinsically train a generator and allow for this type of analysis without additional effort [64, 132]. However, this is not the case for other embedding methods. Border et al. proposed to use diffusion models as generators and investigated this introspection method with images [12]. However, this has not been explored yet, to our knowledge, with EEG embeddings and there have only been a few studies experimenting with diffusion models and EEG signals [113, 4, 53]. 

## **6. Discussion and Recommendations** 

In the previous sections, we reported as factually as possible our findings on the methods that can or could be used to learn embeddings for BCI, along with reasons for why one would want to do so, and the methods available to introspect them. We will now synthesise those findings and extract the main outcomes and discuss them. We will close with recommendations for future research on deep representation learning for BCI and EEG. 

Concerning the methods employed to learn embeddings by the articles we analysed, we found that a large majority were autoencoder-based, accounting for approximately half of the articles surveyed. This observation was not surprising as they are based on a quite straightforward principle which has been in existence for a long time and as many variants have been developed [8] even if we could reported on three only in our study. Furthermore, we found a significant number of GANs, representing approximately a fourth of the surveyed articles. Again, this result was expected as GANs used to be the state-of-the-art of generative models, before the arrival of diffusion models, and have been abundantly used for EEG generation. However, none of the surveyed articles employed GANs for the purpose of EEG representation learning, leaving this area open for further investigation. Finally, if we leave aside the 

studies that simply use the hidden layer of a classifier as embedding, the remaining methods were only observed sporadically. This shows how little the field of deep representation learning has been explored in BCI by now. Regardless, we close this paragraph by reminding the reader that we did not conduct a systematic review so these percentages might not reflect the real distribution of the current research on deep representation learning for BCI; they should be taken with a grain of salt. 

In addition to these findings, we make three primary observations: _firstly_ , in very few studies the authors were using representations in a transfer learning scenario. Yet, there is great potential: deep learning models shine in BCI transfer learning scenarios [121]. Moreover, re-using a pre-trained representation can completely erase (in the case of linear probing [37]) or at least alleviate (in the case of fine-tuning [58]) the cost of using deep learning techniques, which qualifies them for online BCI applications. _Secondly_ , when it comes to cross-dataset transfer learning, the authors of the reviewed articles all applied their own procedures for pre-training, finetuning and evaluating of models. This makes the comparison of methods difficult. To compare pretraining methods, the two other steps (fine-tuning and evaluating) should be fixed and standardised. To our knowledge there currently is only one standard benchmark for cross-dataset transfer in BCI [121] but it still leaves room for improvement as discussed in Subsection 5.1. _Finally_ , the authors often learned an embedding as a side product of the method they use rather than as an explicit objective. In most cases, they ignore the obtained embedding and continue with their primary task despite the large panel of introspection techniques available, as delineated in Section 5. 

In light of these observations, we proceed to sketch recommendations regarding the future of deep representation learning for EEG data. The first recommendation is, when an embedding has been learned, to introspect this representation. Authors can choose from a number of existing techniques, as explained in Section 5, that can all provide valuable insights about what has actually been learned. Moreover, this additional introspection step requires relatively little computational effort compared to the initial one for learning the embedding. 

The second recommendation focuses on foundation models. We call _foundation model_ an architecture which has been pre-trained on large amounts of data. Such models can typically produce general representations of their input data. Foundation models serve as starting points or as building blocks for fine-tuning on downstream tasks. We believe that the development of EEG-specific foundation models would offer a great 

_Review of Deep Representation Learning Techniques for BCI and Recommendations_ 

15 

benefit for the BCI community. In the computer vision domain, foundation models are typically trained using SSL techniques [7] so this seems to be a promising avenue for BCI, too. Although the idea of developing foundation models for BCI or EEG has started to be discussed [21], there currently is no such model that has been widely adopted by the BCI community. 

Our third recommendation is about the eventual creation of novel EEG datasets for the training of foundation models. Experience from the language processing and the computer vision fields has shown that foundation models require extremely large, but not necessarily labelled datasets to be trained [23, 1]. We assume this will probably be the case also for EEG foundation models. In non-EEG domains, those large datasets were coming from very diverse sources, which would probably translate for EEG foundation models into many different EEG recording systems, subjects and recording conditions. The Temple University Hospital EEG data corpus [78] might be such a resource and has already been explored by Kostas et al. [58] to train a SSL model, but we still lack hindsight on whether this corpus is a good dataset for training foundation models. 

Our final recommendation is about the eventual creation of novel benchmarks for evaluating SSL methods and foundation models for BCI. To go beyond the BEETL benchmark [121], we first need to establish a set of fixed fine-tuning procedures to focus on a comparison between pre-trained models and not the combinations of pre-trained models and fine-tuning procedures. The choice of such fixed finetuning procedures should be relatively deterministic and realistic for BCI usage. Two simple fine-tuning procedures could for example be linear probing [37] and whole network fine-tuning [58]. Second, this new benchmark would need a large diversity of downstream tasks. As the main purpose of foundation models is to be re-used, they also need to be tested and compared on as many re-usage scenarios as possible. For BCI, this would translate into including datasets from as many BCI paradigms, recording scenarios and user groups as possible. We can even go a step further and mention that novel datasets could be recorded explicitly for this benchmark. As the goal of using a foundation model is to reduce the amount of calibration data needed, those novel datasets could probably contain less repetitions per condition but instead represent more and diverse conditions. Third, and finally, a benchmark is useful if it is adopted and used by the community. For this reason, the needs of the BCI community must be kept in mind. Also, it might be relevant to include such a benchmark in a tool already actively used by the community such as the MOABB library [3]. An adoption would also be 

encouraged, if reviewers regularly require comparisons with baseline approaches. 

The conceptualization and successful training of foundation models for EEG data processing, potentially facilitated by novel benchmarks and datasets, could revolutionize the field of BCI. In particular, it would reduce the amount of data needed to train BCI decoding models, implying reduced calibration times for novel sessions or subjects and a facilitation of rapidly explorating novel experimental paradigms and user tasks. This efficiency could accelerate research cycles, potentially catalyzing the emergence of a new generation of BCI paradigms. For novel application fields of BCI such as invasive neurotechnological applications, where the small sample problems may be even more severe, this efficiency may even be decisive. Furthermore, the generalized EEG representations we would obtain from future foundation models could facilitate the alignment of brain signals with other data modalities, such as subject videos or medical records. Such crossmodal embedding alignments would open the door for a broader scope of predictive tasks, extending beyond traditional imagery- and evoked potentialbased paradigms to directly forecast attributes or states represented in other domains. 

In summary, the advent of EEG foundation models could mark a paradigm shift, with implications ranging from streamlined model training and enhanced cross-modal applicability to the eradication of cumbersome calibration procedures. Therefore, a focus on establishing such models should be considered a priority within the EEG and BCI research communities and for funding decisions. 

## **7. Acknowledgements** 

This work is in part supported by the Donders Center for Cognition (DCC) and is part of the project Dutch Brain Interface Initiative (DBI2) with project number 024.005.022 of the research program Gravitation which is (partly) financed by the Dutch Research Council (NWO). 

_Glossary_ 

16 

## **Glossary** 

## **Acronyms** 

**BCI** brain-computer interface. 1, 2, 3, 16 

- **c-VEP** code-modulated visually evoked potential. 11, 16 

- **CNN** convolutional neural network. 8, 16 

- **DAE** denoising autoencoder. 8, 16 

**DL** deep learning. 2, 16 

- **DNN** deep neural Network. 16 

- **EEG** electroencephalogram. 1, 2, 3, 16 

- **ERP** event-related potential. 11, 16 

- **FFT** fast Fourier transform. 13, 16 

- **FIt-SNE** FFT-accelerated interpolation-based t-SNE. 13, 16 

- **GAN** generative adversarial network. 7, 9, 14, 16 

**ICA** independent component analysis. 16 

**MAE** masked autoencoder. 8, 16 

**MLP** multilayer perceptron. 8, 16 

- **NLP** natural language processing. 3, 8, 11, 16 

- **PCA** principal component analysis. 12, 13, 16 

- **SAE** sparse autoencoder. 8, 16 

- **SSL** self-supervised learning. _Glossary:_ selfsupervised learning, 1, 6, 7, 8, 9, 10, 11, 15, 16 

- **SSVEP** steady-state visually evoked potential. 11, 16 **SVM** support vector machine. 16 

- **t-SNE** t-distributed stochastic neighbor embedding. 13, 16 

   - **downstream task** Learning task on which a network can be pre-trained. Downstream tasks are typically supervised. In the context of BCI, downstream tasks can be the classification of imagined concepts, responses to sensory stimuli, sleep stages, emotions, mental workload, drowsiness, seizure, etc. 7, 11, 12, 14, 16 

   - **human-annotated label** Labels that, unlike pseudo labels, were manually annotated by humans or, in the context of BCI, that required the subject to execute a pre-scripted task. Examples of such labels in BCI are the imagery class that was executed during an epoch, the stimulus that was attended during an epoch, the sleep phase, the reported mental workload, the level of drowsiness, etc. However, we would not consider the subject’s id or the electrode names as human-annotated labels. 6, 7, 10, 16 

   - **pretext task** Learning task on which a network can be pre-trained. Training for pretext tasks is typically done by unsupervised learning algorithms. 7, 11, 12, 16 

   - **pseudo label** Pseudo labels, unlike human-annotated labels, are automatically generated labels based on data attributes (e.g., chronological order of the time samples, spatial position of the electrodes), or on the meta-data associated with the recordings, (i.g., subject id, subject age, electrode names, etc.). 7, 8, 10, 16 

   - **self-supervised learning** Subset of the unsupervised learning algorithms that are trained with pseudo labels [49] . 16 

   - **unsupervised learning** Machine learning algorithms that do not use human-annotated labels. 7, 8, 16 

- **UMAP** uniform manifold qpproximation and projection. 6, 13, 16 

**VAE** variational autoencoder. 8, 10, 16 

_REFERENCES_ 

17 

## **References** 

- [1] J.-B. Alayrac, J. Donahue, P. Luc, A. Miech, I. Barr, Y. Hasson, K. Lenc, A. Mensch, K. Millican, M. Reynolds, R. Ring, E. Rutherford, S. Cabi, T. Han, Z. Gong, S. Samangooei, M. Monteiro, J. L. Menick, S. Borgeaud, A. Brock, A. Nematzadeh, S. Sharifzadeh, M. Bi´nkowski, R. Barreira, O. Vinyals, A. Zisserman, and K. Simonyan. Flamingo: a Visual Language Model for Few-Shot Learning. _Advances in Neural Information Processing Systems_ , 35:23716–23736, Dec. 2022. 

- [2] R. Arandjelovic, P. Gronat, A. Torii, T. Pajdla, and J. Sivic. NetVLAD: CNN Architecture for Weakly Supervised Place Recognition. In _Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition_ , pages 5297–5307, 2016. 

- [3] B. Aristimunha, I. Carrara, P. Guetschel, S. Sedlar, P. Rodrigues, J. Sosulski, D. Narayanan, E. Bjareholt, B. Quentin, R. T. Schirrmeister, E. Kalunga, L. Darmet, C. Gregoire, A. Abdul Hussain, R. Gatti, V. Goncharenko, J. Thielen, T. Moreau, Y. Roy, V. Jayaram, A. Barachant, and S. Chevallier. Mother of all BCI Benchmarks. Zenodo, Oct. 2023. doi: `10.5281/ ZENODO.10034223` . 

- [4] B. Aristimunha, R. Y. de Camargo, S. Chevallier, O. Lucena, A. G. Thomas, M. J. Cardoso, W. H. L. Pinaya, and J. Dafflon. Synthetic Sleep EEG Signal Generation using Latent Diffusion Models. In _Deep Generative Models for Health Workshop NeurIPS 2023_ , Oct. 2023. 

- [5] N. Ayoobi and E. B. Sadeghian. A subjectindependent brain-computer interface framework based on supervised autoencoder. In _Annual International Conference of the IEEE Engineering in Medicine and Biology Society_ , pages 218–221, 2022. doi: `10 . 1109 / embc48229.2022.9871590` . 

- [6] A. Baevski, Y. Zhou, A. Mohamed, and M. Auli. Wav2vec 2.0: A Framework for SelfSupervised Learning of Speech Representations. In _Advances in Neural Information Processing Systems_ , volume 33, pages 12449–12460. Curran Associates, Inc., 2020. 

- [7] R. Balestriero, M. Ibrahim, V. Sobal, A. Morcos, S. Shekhar, T. Goldstein, F. Bordes, A. Bardes, G. Mialon, Y. Tian, A. Schwarzschild, A. G. Wilson, J. Geiping, Q. Garrido, P. Fernandez, A. Bar, H. Pirsiavash, Y. LeCun, and M. Goldblum. A Cookbook of SelfSupervised Learning, Apr. 2023. doi: `10 .` 

`48550/arXiv.2304.12210` . arXiv: `2304.12210 [cs]` . 

- [8] D. Bank, N. Koenigstein, and R. Giryes. Autoencoders, Apr. 2021. arXiv: `2003.05991 [cs, stat]` . 

- [9] H. Banville, O. Chehab, A. Hyv¨arinen, D.-A. Engemann, and A. Gramfort. Uncovering the structure of clinical EEG signals with selfsupervised learning. _Journal of Neural Engineering_ , 18(4):046020, Aug. 2021. issn: 17412560, 1741-2552. doi: `10.1088/1741- 2552/ abca18` . 

- [10] A. Bardes, J. Ponce, and Y. LeCun. VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning, Jan. 2022. doi: `10.48550/arXiv.2105.04906` . arXiv: `2105. 04906 [cs]` . 

- [11] P. Bashivan, I. Rish, M. Yeasin, and N. Codella. Learning Representations from EEG with Deep Recurrent-Convolutional Neural Networks, Feb. 2016. doi: `10 . 48550 / arXiv . 1511 . 06448` . arXiv: `1511.06448 [cs]` . 

- [12] F. Bordes, R. Balestriero, and P. Vincent. High Fidelity Visualization of What Your SelfSupervised Representation Knows About, Aug. 2022. doi: `10 . 48550 / arXiv . 2112 . 09164` . arXiv: `2112.09164 [cs]` . 

- [13] T. Br¨usch, M. N. Schmidt, and T. S. Alstrøm. Multi-view self-supervised learning for multivariate variable-channel time series, July 2023. doi: `10 . 48550 / arXiv . 2307 . 09614` . arXiv: `2307.09614 [cs, eess, stat]` . 

- [14] S. Casta˜no-Candamil, A. Meinel, and M. Tangermann. Post-hoc Labeling of Arbitrary M/EEG Recordings for Data-Efficient Evaluation of Neural Decoding Methods. _Frontiers in Neuroinformatics_ , 13, 2019. issn: 1662-5196. doi: `10.3389/fninf.2019.00055` . 

- [15] H. Chen, D. Wang, M. Xu, and Y. Chen. CRETSCAE: A novel classification model based on stacked convolutional autoencoder for dualtarget RSVP-BCI tasks. _IEEE transactions on bio-medical engineering_ , 2024. issn: 1558-2531. doi: `10.1109/TBME.2024.3361716` . 

- [16] T. Chen, S. Kornblith, M. Norouzi, and G. Hinton. A Simple Framework for Contrastive Learning of Visual Representations, June 2020. doi: `10 . 48550 / arXiv . 2002 . 05709` . arXiv: `2002.05709 [cs, stat]` . 

- [17] Y.-J. Chen, P.-C. Chen, S.-C. Chen, and C.-M. Wu. Denoising autoencoder-based feature extraction to robust SSVEP-Based BCIs. _Sensors (Basel, Switzerland)_ , 21(15), 2021. issn: 14248220. doi: `10.3390/s21155019` . 

_REFERENCES_ 

18 

- [18] S. Chevallier, I. Carrara, B. Aristimunha, P. Guetschel, S. Sedlar, B. Lopes, S. Velut, S. Khazem, and T. Moreau. The largest EEGbased BCI reproducibility study for open science: the MOABB benchmark, Apr. 2024. doi: `10 . 48550 / arXiv . 2404 . 15319` . arXiv: `2404.15319 [cs, eess, q-bio]` . 

- [19] H.-Y. S. Chien, H. Goh, C. M. Sandino, and J. Y. Cheng. MAEEG: Masked Auto-encoder for EEG Representation Learning, Oct. 2022. doi: `10 . 48550 / arXiv . 2211 . 02625` . arXiv: `2211.02625 [cs, eess]` . 

- [20] C.-C. Chuang, C.-C. Lee, C.-H. Yeng, E.-C. So, B.-S. Lin, and Y.-J. Chen. Convolutional denoising autoencoder based SSVEP signal enhancement to SSVEP-based BCIs. _Microsystem Technologies-Micro-And Nanosystems-Information Storage And Processing Systems_ , 28(1):237–244, 2022. issn: 0946-7076. doi: `10.1007/s00542019-04654-2` . 

- [21] W. Cui, W. Jeong, P. Th¨olke, T. Medani, K. Jerbi, A. A. Joshi, and R. M. Leahy. NeuroGPT: Developing A Foundation Model for EEG, Nov. 2023. doi: `10.48550/arXiv.2311. 03764` . arXiv: `2311.03764 [cs, eess]` . 

- [22] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei. ImageNet: A largescale hierarchical image database. In _IEEE Conference on Computer Vision and Pattern Recognition_ , pages 248–255, June 2009. doi: `10. 1109/CVPR.2009.5206848` . 

- [23] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding, May 2019. doi: `10 . 48550 / arXiv . 1810.04805` . arXiv: `1810.04805 [cs]` . 

- [24] A. Ditthapron, N. Banluesombatkul, S. Ketrat, E. Chuangsuwanich, and T. Wilaiprasitporn. Universal Joint Feature Extraction for P300 EEG Classification Using Multi-Task Autoencoder. _IEEE Access_ , 7:68415–68428, 2019. issn: 2169-3536. doi: `10.1109/ACCESS.2019. 2919143` . 

- [25] H. Dose, J. S. Møller, H. K. Iversen, and S. Puthusserypady. An end-to-end deep learning approach to MI-EEG signal classification for BCIs. _Expert Systems with Applications_ , 114:532–542, Dec. 2018. issn: 0957-4174. doi: `10.1016/j.eswa.2018.08.031` . 

- [26] M. Everingham, L. Van Gool, C. K. I. Williams, J. Winn, and A. Zisserman. The Pascal Visual Object Classes (VOC) Challenge. _International Journal of Computer Vision_ , 88(2):303–338, 

June 2010. issn: 1573-1405. doi: `10 . 1007 / s11263-009-0275-4` . 

- [27] F. Fahimi, S. Dosen, K. K. Ang, N. MrachaczKersting, and C. Guan. Generative adversarial networks-based data augmentation for braincomputer interface. _IEEE transactions on neural networks and learning systems_ , 32(9):4039– 4051, 2021. issn: 2162-2388. doi: `10 . 1109 / tnnls.2020.3016666` . 

- [28] R. Ferri, C. Babiloni, V. Karami, A. I. Triggiani, F. Carducci, G. Noce, R. Lizio, M. T. Pascarelli, A. Soricelli, F. Amenta, A. Bozzao, A. Romano, F. Giubilei, C. D. Percio, F. Stocchi, G. B. Frisoni, F. Nobili, L. Patan`e, and P. Arena. Stacked autoencoders as new models for an accurate Alzheimer’s disease classification support using resting-state EEG and MRI measurements. _Clinical neurophysiology : official journal of the International Federation of Clinical Neurophysiology_ , 132(1):232–245, 2021. issn: 1872-8952. doi: `10 . 1016 / j . clinph . 2020.09.015` . 

- [29] R. D. Flint, M. C. Tate, K. Li, J. W. Templer, J. M. Rosenow, C. Pandarinath, and M. W. Slutzky. The Representation of Finger Movement and Force in Human Motor and Premotor Cortices. _eNeuro_ , 7(4), Aug. 2020. issn: 2373-2822. doi: `10.1523/ENEURO.006320.2020` . 

- [30] N. M. Foumani, G. Mackellar, S. Ghane, S. Irtza, N. Nguyen, and M. Salehi. EEG2Rep: Enhancing Self-supervised EEG Representation Through Informative Masked Inputs, Feb. 2024. doi: `10 . 48550 / arXiv . 2402 . 17772` . arXiv: `2402.17772 [cs, eess]` . 

- [31] Y. Ganin and V. Lempitsky. Unsupervised Domain Adaptation by Backpropagation. In _Proceedings of the 32nd International Conference on Machine Learning_ , pages 1180–1189. PMLR, June 2015. 

- [32] B. Gao, J. Zhou, Y. Yang, J. Chi, and Q. Yuan. Generative adversarial network and convolutional neural network-based EEG imbalanced classification model for seizure detection. _Biocybernetics And Biomedical Engineering_ , 42(1):1– 15, 2022. issn: 0208-5216. doi: `10.1016/j.bbe. 2021.11.002` . 

- [33] H. Ghazikhani and M. Rouhani. A stacked autoencoders approach for a P300 speller BCI. In _8th International Conference On Computer And Knowledge Engineering_ , pages 1–6, 2018. doi: `10.1109/iccke.2018.8566534` . 

_REFERENCES_ 

19 

- [34] I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair, A. Courville, and Y. Bengio. Generative adversarial networks. _Communications of the ACM_ , 63(11):139–144, Oct. 2020. issn: 0001-0782. doi: `10.1145/3422622` . 

- [35] P. Guetschel, T. Moreau, and M. Tangermann. S-JEPA: towards seamless cross-dataset transfer through dynamic spatial attention, Mar. 2024. doi: `10 . 48550 / arXiv . 2403 . 11772` . arXiv: `2403.11772 [cs]` . 

- [36] P. Guetschel, T. Papadopoulo, and M. Tangermann. An embedding for EEG signals learned using a triplet loss, Mar. 2023. doi: `10.48550/ ARXIV.2304.06495` . arXiv: `2304.06495 [cs, eess]` . 

- [37] P. Guetschel, T. Papadopoulo, and M. Tangermann. Embedding neurophysiological signals. In _International Conference on Metrology for eXtended Reality, Artificial Intelligence, and Neural Engineering (MetroXRAINE)_ , pages 169– 174, Rome. IEEE, Oct. 2022. doi: `10.1109/ metroxraine54828.2022.9967496` . 

- [38] R. Hadsell, S. Chopra, and Y. LeCun. Dimensionality Reduction by Learning an Invariant Mapping. In _IEEE Computer Society Conference on Computer Vision and Pattern Recognition (CVPR’06)_ , volume 2, pages 1735–1742, June 2006. doi: `10.1109/CVPR.2006.100` . 

- [39] N. Halko, P. G. Martinsson, and J. A. Tropp. Finding Structure with Randomness: Stochastic Algorithms for Constructing Approximate matrix Decompositions. _California Institute of Technology_ , Oct. 2011. doi: `10 . 7907 / PK8V - V047` . 

- [40] K. G. Hartmann, R. T. Schirrmeister, and T. Ball. EEG-GAN: Generative adversarial networks for electroencephalograhic (EEG) brain signals, June 2018. doi: `10 . 48550 / arXiv.1806.01875` . arXiv: `1806.01875 [cs, eess, q-bio, stat]` . 

- [41] A.-W. Harzing -. Publish or Perish, 2007. 

- [42] Y. He, Z. Lu, J. Wang, S. Ying, and J. Shi. A self-supervised learning based channel attention MLP-Mixer network for motor imagery decoding. _IEEE transactions on neural systems and rehabilitation engineering_ , 30:2406–2417, 2022. issn: 1558-0210. doi: `10.1109/tnsre.2022. 3199363` . 

- [43] I. Higgins, L. Matthey, X. Glorot, A. Pal, B. Uria, C. Blundell, S. Mohamed, and A. Lerchner. Early Visual Concept Learning with Unsupervised Deep Learning, Sept. 2016. doi: `10.48550/arXiv.1606.05579` . arXiv: `1606. 05579 [cs, q-bio, stat]` . 

- [44] G. E. Hinton and S. Roweis. Stochastic Neighbor Embedding. In _Advances in Neural Information Processing Systems_ , volume 15. MIT Press, 2002. 

- [45] J. F. Hwaidi and T. M. Chen. Classification of motor imagery EEG signals based on deep autoencoder and convolutional neural network approach. _IEEE access : practical innovations, open solutions_ , 10:48071–48081, 2022. issn: 2169-3536. doi: `10 . 1109 / access . 2022 . 3171906` . 

- [46] V. Jayaram, M. Alamgir, Y. Altun, B. Scholkopf, and M. Grosse-Wentrup. Transfer learning in brain-computer interfaces. _IEEE Computational Intelligence Magazine_ , 11(1):20– 31, 2016. issn: 1556-603X. doi: `10.1109/MCI. 2015.2501545` . 

- [47] E. Jeon, W. Ko, J. S. Yoon, and H.-I. Suk. Mutual Information-Driven Subject-Invariant and Class-Relevant Deep Representation Learning in BCI. _IEEE Transactions on Neural Networks and Learning Systems_ :1–11, 2021. issn: 2162237X, 2162-2388. doi: `10.1109/TNNLS.2021. 3100583` . 

- [48] R. Jiang, L. Sun, X. Wang, and Y. Xu. Application of transformer with auto-encoder in motor imagery EEG signals. In _14th International Conference on Wireless Communication and Signal Processing_ , pages 631–637, 2022. isbn: 978-1-66545-085-0. doi: `10.1109/WCSP55476. 2022.10039415` . 

- [49] L. Jing and Y. Tian. Self-Supervised Visual Feature Learning With Deep Neural Networks: A Survey. _IEEE Transactions on Pattern Analysis and Machine Intelligence_ , 43(11):4037–4058, Nov. 2021. issn: 1939-3539. doi: `10 . 1109 / TPAMI.2020.2992393` . 

- [50] L. Jingwei, C. Yin, and Z. Weidong. Deep learning EEG response representation for brain computer interface. In _2015 34th Chinese Control Conference (CCC)_ , pages 3518–3523, Hangzhou, China. IEEE, July 2015. isbn: 978988-15638-9-7. doi: `10 . 1109 / ChiCC . 2015 . 7260182` . 

_REFERENCES_ 

20 

- [51] Y. H. Kang, D. Kim, and S. W. Lee. Meta-BCI: Perspectives on a role of self-supervised learning in meta brain computer interface. In _10th International Winter Conference On BrainComputer Interface (Bci2022)_ , 2022. doi: `10. 1109/bci53720.2022.9734995` . 

- [52] R. Kiros, R. Salakhutdinov, and R. S. Zemel. Unifying Visual-Semantic Embeddings with Multimodal Neural Language Models, 2014. doi: `10.48550/ARXIV.1411.2539` . 

- [53] G. Klein, P. Guetschel, G. Silvestri, and M. Tangermann. Synthesizing EEG Signals from Event-Related Potential Paradigms with Conditional Diffusion Models, Mar. 2024. doi: `10.48550/arXiv.2403.18486` . arXiv: `2403. 18486 [cs, eess]` . 

- [54] W. Ko, E. Jeon, S. Jeong, and H.-I. Suk. MultiScale Neural Network for EEG Representation Learning in BCI. _IEEE Computational Intelligence Magazine_ , 16(2):31–45, May 2021. issn: 1556-603X, 1556-6048. doi: `10 . 1109 / MCI . 2021.3061875` . 

- [55] D. Kobak and P. Berens. The art of using t-SNE for single-cell transcriptomics. _Nature Communications_ , 10(1):5416, Nov. 2019. issn: 2041-1723. doi: `10.1038/s41467-019-13056x` . 

- [56] D. Kobak and G. C. Linderman. Initialization is critical for preserving global data structure in both t-SNE and UMAP. _Nature Biotechnology_ , 39(2):156–157, Feb. 2021. issn: 1546-1696. doi: `10.1038/s41587-020-00809-z` . 

- [57] R. J. Kobler, J.-i. Hirayama, Q. Zhao, and M. Kawanabe. SPD domain-specific batch normalization to crack interpretable unsupervised domain adaptation in EEG, Oct. 2022. doi: `10. 48550/arXiv.2206.01323` . arXiv: `2206.01323 [cs, eess]` . 

- [58] D. Kostas, S. Aroca-Ouellette, and F. Rudzicz. BENDR: Using Transformers and a Contrastive Self-Supervised Learning Task to Learn From Massive Amounts of EEG Data. _Frontiers in Human Neuroscience_ , 15:653659, June 2021. issn: 1662-5161. doi: `10.3389/fnhum.2021. 653659` . 

- [59] S. Kullback and R. A. Leibler. On Information and Sufficiency. _The Annals of Mathematical Statistics_ , 22(1):79–86, Mar. 1951. issn: 00034851, 2168-8990. doi: `10 . 1214 / aoms / 1177729694` . 

- [60] S. Kumaraguru and M. R. E. Jebarani. Trust aware routing using sunflower sine cosine-based stacked autoencoder approach for EEG signal classification in WSN. _Journal Of High Speed Networks_ , 27(2):101–119, 2021. issn: 0926-6801. doi: `10.3233/jhs-210654` . 

- [61] D.-Y. Lee, J.-H. Jeong, B.-H. Lee, and S.-W. Lee. Motor imagery classification using intertask transfer learning via a channel-wise variational autoencoder-based convolutional neural network. _IEEE transactions on neural systems and rehabilitation engineering_ , 30:226– 237, 2022. issn: 1558-0210. doi: `10 . 1109 / tnsre.2022.3143836` . 

- [62] H. Li, J. Tang, W. Li, W. Dai, Y. Liu, and Z. Zhou. Multi-task collaborative network: Bridge the supervised and self-supervised learning for EEG classification in RSVP tasks. _IEEE transactions on neural systems and rehabilitation engineering_ , 32:638–651, 2024. issn: 1558-0210. doi: `10.1109/TNSRE.2024.3357863` . 

- [63] L. H. Li, M. Yatskar, D. Yin, C.-J. Hsieh, and K.-W. Chang. VisualBERT: A Simple and Performant Baseline for Vision and Language, 2019. doi: `10.48550/ARXIV.1908.03557` . 

- [64] X. Li, Z. Zhao, D. Song, Y. Zhang, C. Niu, J. Zhang, J. Huo, and J. Li. Variational autoencoder based latent factor decoding of multichannel EEG for emotion recognition. _IEEE International Conference On Bioinformatics And Biomedicine_ :684–687, 2019. issn: 2156-1125. doi: `10.1109/bibm47256.2019.8983341` . 

- [65] X. Li, Z. Zhao, D. Song, Y. Zhang, J. Pan, L. Wu, J. Huo, C. Niu, and D. Wang. Latent factor decoding of multi-channel EEG for emotion recognition through autoencoderlike neural networks. _Frontiers in neuroscience_ , 14:87, 2020. issn: 1662-4548. doi: `10 . 3389 / fnins.2020.00087` . 

- [66] Q. Lin, S.-q. Ye, X.-m. Huang, S.-y. Li, M.-z. Zhang, Y. Xue, and W.-S. Chen. Classification of epileptic EEG signals with stacked sparse autoencoder based on deep learning. _Intelligent Computing Methodologies_ , 9773:802–810, 2016. issn: 0302-9743. doi: `10.1007/978- 3- 31942297-8_74` . 

- [67] T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ramanan, P. Doll´ar, and C. L. Zitnick. Microsoft COCO: Common Objects in Context. In D. Fleet, T. Pajdla, B. Schiele, and T. Tuytelaars, editors, _Computer Vision – ECCV 2014_ , Lecture Notes in Computer Science, pages 740–755, Cham. Springer International Publishing, 2014. isbn: 

_REFERENCES_ 

21 

      - [77] P. Nejedly, V. Kremen, K. Lepkova, F. Mivalt, V. Sladky, T. Pridalova, F. Plesinger, P. Jurak, M. Pail, M. Brazdil, P. Klimes, and G. Worrell. Utilization of temporal autoencoder for semisupervised intracranial EEG clustering and classification. _Scientific reports_ , 13(1):744, 2023. issn: 2045-2322. doi: `10.1038/s41598-02327978-6` . 

   - 978-3-319-10602-1. doi: `10.1007/978-3-31910602-1_48` . 

- [68] G. C. Linderman, M. Rachh, J. G. Hoskins, S. Steinerberger, and Y. Kluger. Fast interpolationbased t-SNE for improved visualization of single-cell RNA-seq data. _Nature Methods_ , 16(3):243–245, Mar. 2019. issn: 1548-7105. doi: `10.1038/s41592-018-0308-4` . 

   - [78] I. Obeid and J. Picone. The Temple University Hospital EEG Data Corpus. _Frontiers in Neuroscience_ , 10, May 2016. issn: 1662-453X. doi: `10.3389/fnins.2016.00196` . 

- [69] C. Liu, J. Jin, R. Xu, S. Li, C. Zuo, H. Sun, X. Wang, and A. Cichocki. Distinguishable spatialspectral feature learning neural network framework for motor imagery-based brain-computer interface. _Journal of neural engineering_ , 18(4), 2021. issn: 1741-2552. doi: `10 . 1088 / 1741 - 2552/ac1d36` . 

   - [79] N. Oskolkov. tSNE vs. UMAP: Global Structure. https://towardsdatascience.com/tsne-vsumap-global-structure-4d8045acba17, Mar. 2020. (Visited on 05/17/2024). 

- [70] J. Liu, G. Wu, Y. Luo, S. Qiu, S. Yang, W. Li, and Y. Bi. EEG-Based emotion classification using a deep neural network and sparse autoencoder. _Frontiers in systems neuroscience_ , 14:43, 2020. issn: 1662-5137. doi: `10 . 3389 / fnsys.2020.00043` . 

   - [80] Y. Ou, S. Sun, H. Gan, R. Zhou, and Z. Yang. An improved self-supervised learning for EEG classification. _Mathematical Biosciences and Engineering_ , 19(7):6907–6922, 2022. issn: 1551-0018. doi: `10.3934/mbe.2022325` . 

- [71] N. Mammone, C. Ieracitano, H. Adeli, and F. C. Morabito. AutoEncoder filter bank common spatial patterns to decode motor imagery from EEG. _IEEE journal of biomedical and health informatics_ , 27(5):2365–2376, 2023. issn: 21682208. doi: `10.1109/JBHI.2023.3243698` . 

   - [81] O. Ozdenizci,<sup>¨</sup> Y. Wang, T. Koike-Akino, and D. Erdogmus. Transfer Learning in BrainComputer Interfaces with Adversarial Variational Autoencoders. In _2019 9th International IEEE/EMBS Conference on Neural Engineering (NER)_ , pages 207–210, San Francisco, CA, USA. IEEE, Mar. 2019. isbn: 978-1-5386-79210. doi:: `10.1109/NER.2019.8716897` . 

- [72] L. McInnes. Performance Comparison of DiUSA. IEEE, Mar. 2019. mension Reduction Implementations. UMAP 0. doi:: documentation. https://umap-learn.readthedocs.io/en/latest/benchmarking.html.[82] O.<sup>¨</sup> (Visited on 05/17/2024). 

   - [82] O. Ozdenizci, Y. Wang, T. Koike-Akino, and D.<sup>¨</sup> Erdo˘gmu¸s. Learning Invariant Representations From EEG via Adversarial Inference. _IEEE Access_ , 8:27074–27085, 2020. issn: 2169-3536. doi: `10.1109/ACCESS.2020.2971600` . 

- [73] L. McInnes, J. Healy, and J. Melville. UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction, Sept. 2020. doi: `10.48550/arXiv.1802.03426` . arXiv: `1802. 03426 [cs, stat]` . 

   - [83] S. J. Pan and Q. Yang. A Survey on Transfer Learning. _IEEE Transactions on Knowledge and Data Engineering_ , 22(10):1345–1359, Oct. 2010. issn: 1558-2191. doi: `10 . 1109 / TKDE . 2009.191` . 

- [74] S. Mirzaei and P. Ghasemi. EEG motor imagery classification using dynamic connectivity patterns and convolutional autoencoder. _Biomedical Signal Processing And Control_ , 68, 2021. issn: 1746-8094. doi: `10.1016/j.bspc.2021. 102584` . 

   - [84] P. K. Parashiva and A. P. Vinod. A New Channel Selection Method using Autoencoder for Motor Imagery based Brain Computer Interface. In _2019 IEEE International Conference on Systems, Man and Cybernetics (SMC)_ , pages 3641–3646, Bari, Italy. IEEE, Oct. 2019. isbn: 978-1-72814-569-3. doi: `10.1109/SMC. 2019.8914251` . 

- [75] M. N. Mohsenvand, M. R. Izadi, and P. Maes. Contrastive Representation Learning for Electroencephalogram Classification. In _Proceedings of the Machine Learning for Health NeurIPS Workshop_ , pages 238–253. PMLR, Nov. 2020. 

   - [85] S. Parija, M. Sahani, R. Bisoi, and P. K. Dash. Autoencoder-based improved deep learning approach for schizophrenic EEG signal classification. _Pattern Analysis And Applications_ , 2022. issn: 1433-7541. doi: `10.1007/s10044-02201107-x` . 

- [76] A. V. Nair, K. M. Kumar, and J. Mathew. An improved approach for EEG signal classification using autoencoder. In _8th International Symposium On Embedded Computing And System Design_ , pages 6–10, 2018. doi: `10.1109/ised. 2018.8704011` . 

_REFERENCES_ 

22 

- [86] D. Pei, M. Burns, R. Chandramouli, and R. Vinjamuri. Decoding asynchronous reaching in electroencephalography using stacked autoencoders. _IEEE access : practical innovations, open solutions_ , 6:52889–52898, 2018. issn: 21693536. doi: `10.1109/access.2018.2869687` . 

- [87] V. M. Petrutiu, L. D. Palcu, C. Lemnaru, M. Dinsoreanu, R. Potolea, R. Mursesan, and V. V. Moca. Enhancing the Classification of EEG Signals using Wasserstein Generative Adversarial Networks. In _2020 IEEE 16th International Conference on Intelligent Computer Communication and Processing (ICCP)_ , pages 29–34, Cluj-Napoca, Romania. IEEE, Sept. 2020. isbn: 978-1-72819-080-8. doi: `10.1109/ICCP51029. 2020.9266157` . 

- [88] S. Phadikar, N. Sinha, and R. Ghosh. Unsupervised feature extraction with autoencoders for EEG based multiclass motor imagery BCI. _Expert Systems With Applications_ , 213, 2023. issn: 0957-4174. doi: `10.1016/j.eswa.2022. 118901` . 

- [89] C. Phunruangsakao, D. Achanccaray, S.-I. Izumi, and M. Hayashibe. Multibranch convolutional neural network with contrastive representation learning for decoding same limb motor imagery tasks. _Frontiers in human neuroscience_ , 16:1032724, 2022. issn: 1662-5161. doi: `10.3389/fnhum.2022.1032724` . 

- [90] S. K. Prabhakar and S.-W. Lee. SASDL and RBATQ: Sparse autoencoder with swarm based deep learning and reinforcement based Q- learning for EEG classification. _IEEE open journal of engineering in medicine and biology_ , 3:58–68, 2022. issn: 2644-1276. doi: `10.1109/ ojemb.2022.3161837` . 

- [91] Y. Qiu, W. Zhou, N. Yu, and P. Du. Denoising sparse autoencoder-based ictal EEG classification. _IEEE transactions on neural systems and rehabilitation engineering_ , 26(9):1717– 1726, 2018. issn: 1558-0210. doi: `10 . 1109 / tnsre.2018.2864306` . 

- [92] A. Radford, L. Metz, and S. Chintala. Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks, Jan. 2016. doi: `10.48550/arXiv.1511.06434` . arXiv: `1511.06434 [cs]` . 

- [93] P. Rajpurkar, J. Zhang, K. Lopyrev, and P. Liang. SQuAD: 100,000+ Questions for Machine Comprehension of Text, Oct. 2016. doi: `10 . 48550 / arXiv . 1606 . 05250` . arXiv: `1606.05250 [cs]` . 

- [94] X. Ran, W. Chen, B. Yvert, and S. Zhang. A hybrid autoencoder framework of dimensionality reduction for brain-computer interface decoding. _Computers in biology and medicine_ , 148:105871, 2022. issn: 1879-0534. doi: `10 . 1016/j.compbiomed.2022.105871` . 

- [95] C. Rommel, T. Moreau, and A. Gramfort. Deep invariant networks with differentiable augmentation layers, Oct. 2022. doi: `10.48550/ arXiv.2202.02142` . arXiv: `2202.02142 [cs]` . 

- [96] C. Rommel, T. Moreau, J. Paillard, and A. Gramfort. CADDA: Class-wise Automatic Differentiable Data Augmentation for EEG Signals, Feb. 2022. doi: `10 . 48550 / arXiv . 2106.13695` . arXiv: `2106.13695 [cs]` . 

- [97] C. Rommel, J. Paillard, T. Moreau, and A. Gramfort. Data augmentation for learning predictive models on EEG: a systematic comparison. _Journal of Neural Engineering_ , 2022. issn: 1741-2552. doi: `10 . 1088 / 1741 - 2552/aca220` . 

- [98] S. Roy, S. Dora, K. McCreadie, and G. Prasad. MIEEG-GAN: Generating artificial motor imagery electroencephalography signals. _International Joint Conference On Neural Networks_ , 2020. issn: 2161-4393. doi: `10.1109/ ijcnn48605.2020.9206942` . 

- [99] Y. Roy, H. Banville, I. Albuquerque, A. Gramfort, T. H. Falk, and J. Faubert. Deep learningbased electroencephalography analysis: a systematic review. _Journal of Neural Engineering_ , 16(5):051001, Oct. 2019. issn: 1741-2560, 17412552. doi: `10.1088/1741-2552/ab260c` . 

- [100] S. Schneider, J. H. Lee, and M. W. Mathis. Learnable latent embeddings for joint behavioral and neural analysis, Oct. 2022. doi: `10. 48550/arXiv.2204.00673` . arXiv: `2204.00673 [cs, q-bio]` . 

- [101] F. Schroff, D. Kalenichenko, and J. Philbin. FaceNet: A unified embedding for face recognition and clustering. In _2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)_ , pages 815–823, Boston, MA, USA. IEEE, June 2015. isbn: 978-1-4673-69640. doi: `10.1109/CVPR.2015.7298682` . 

- [102] D. Serdyuk, K. Audhkhasi, P. Brakel, B. Ramabhadran, S. Thomas, and Y. Bengio. Invariant Representations for Noisy Speech Recognition, Nov. 2016. doi: `10.48550/arXiv. 1612.01928` . arXiv: `1612.01928 [cs, stat]` . 

_REFERENCES_ 

23 

- [103] Y. Song, Q. Zheng, B. Liu, and X. Gao. EEG Conformer: Convolutional Transformer for EEG Decoding and Visualization. _IEEE Transactions on Neural Systems and Rehabilitation Engineering_ , 31:710–719, 2023. issn: 1558-0210. doi: `10. 1109/TNSRE.2022.3230250` . 

- [104] J. Sosulski, J.-P. Kemmer, and M. Tangermann. Improving Covariance Matrices Derived from Tiny Training Datasets for the Classification of Event-Related Potentials with Linear Discriminant Analysis. _Neuroinformatics_ , 19(3):461– 476, July 2021. issn: 1559-0089. doi: `10.1007/ s12021-020-09501-8` . 

- [105] J. Sosulski and M. Tangermann. Introducing block-Toeplitz covariance matrices to remaster linear discriminant analysis for event-related potential brain–computer interfaces. _Journal of Neural Engineering_ , 19(6):066001, Nov. 2022. issn: 1741-2552. doi: `10 . 1088 / 1741 - 2552 / ac9c98` . 

- [106] J. Sosulski and M. Tangermann. UMM: Unsupervised Mean-difference Maximization, June 2023. doi: `10 . 48550 / arXiv . 2306 . 11830` . arXiv: `2306.11830 [cs, stat]` . 

- [107] S. Stephe, T. Jayasankar, and K. V. Kumar. Motor imagery EEG recognition using deep generative adversarial network with EMD for BCI applications. _Tehnicki Vjesnik-Technical Gazette_ , 29(1):92–100, 2022. issn: 1330-3651. doi: `10.17559/tv-20210121112228` . 

- [108] C. Tan, F. Sun, B. Fang, T. Kong, and W. Zhang. Autoencoder-based transfer learning in brain-computer interface for rehabilitation robot. _International Journal Of Advanced Robotic Systems_ , 16(2), 2019. issn: 1729-8814. doi: `10.1177/1729881419840860` . 

- [109] X. Tang, T. Wang, Y. Du, and Y. Dai. Motor imagery EEG recognition with KNN-based smooth auto-encoder. _Artificial intelligence in medicine_ , 101:101747, 2019. issn: 1873-2860. doi: `10.1016/j.artmed.2019.101747` . 

- [110] J. Thielen, P. Marsman, J. Farquhar, and P. Desain. From full calibration to zero training for a code-modulated visual evoked potentials for brain–computer interface. _Journal of Neural Engineering_ , 18(5):056007, Apr. 2021. issn: 1741-2552. doi: `10.1088/1741-2552/abecef` . 

- [111] M. E. Tipping and C. M. Bishop. Probabilistic Principal Component Analysis. _Journal of the Royal Statistical Society Series B: Statistical Methodology_ , 61(3):611–622, Sept. 1999. issn: 1369-7412, 1467-9868. doi: `10 . 1111 / 1467 - 9868.00196` . 

- [112] K. Tomonaga, T. Hayakawa, and J. Kobayashi. Experiments on classification of electroencephalography (EEG) signals in imagination of direction using stacked autoencoder. _Journal Of Robotics Networking And Artificial Life_ , 4(2):124–128, 2017. issn: 2352-6386. doi: `10. 2991/jrnal.2017.4.2.4` . 

- [113] S. Torma and D. L. Szegletes. EEGWave: a Denoising Diffusion Probablistic Approach for EEG Signal Generation, 2023. EasyChair: `10275` . 

- [114] L. van der Maaten and G. Hinton. Visualizing Data using t-SNE. _Journal of Machine Learning Research_ , 9(86):2579–2605, 2008. issn: 15337928. 

- [115] G. Van Horn, O. Mac Aodha, Y. Song, Y. Cui, C. Sun, A. Shepard, H. Adam, P. Perona, and S. Belongie. The INaturalist Species Classification and Detection Dataset. In _Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition_ , pages 8769–8778, 2018. 

- [116] T. E. Vanhecke. Zotero. _Journal of the Medical Library Association : JMLA_ , 96(3):275–276, July 2008. issn: 1536-5050. doi: `10 . 3163 / 1536-5050.96.3.022` . 

- [117] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, �L. Kaiser, and I. Polosukhin. Attention is All you Need. In _Advances in Neural Information Processing Systems_ , volume 30. Curran Associates, Inc., 2017. 

- [118] C. Vondrick, H. Pirsiavash, and A. Torralba. Generating Videos with Scene Dynamics. In _Advances in Neural Information Processing Systems_ , volume 29. Curran Associates, Inc., 2016. 

- [119] A. Wang, A. Singh, J. Michael, F. Hill, O. Levy, and S. R. Bowman. GLUE: A MultiTask Benchmark and Analysis Platform for Natural Language Understanding, Feb. 2019. arXiv: `1804.07461 [cs]` . 

- [120] H. Wang, L. Cao, C. Huang, J. Jia, Y. Dong, C. Fan, and V. H. C. de Albuquerque. A novel algorithmic structure of EEG channel attention combined with swin transformer for motor patterns classification. _IEEE transactions on neural systems and rehabilitation engineering_ , 31:3132–3141, 2023. issn: 1558-0210. doi: `10. 1109/TNSRE.2023.3297654` . 

- [121] X. Wei, A. A. Faisal, M. Grosse-Wentrup, A. Gramfort, S. Chevallier, V. Jayaram, C. Jeunet, S. Bakas, S. Ludwig, K. Barmpas, M. Bahri, Y. Panagakis, N. Laskaris, D. A. Adamos, S. Zafeiriou, W. C. Duong, S. M. 

_REFERENCES_ 

24 

   - Gordon, V. J. Lawhern, M. Sliwowski,<sup>´</sup> V. Rouanne, and P. Tempczyk. 2021 BEETL Competition: Advancing Transfer Learning for Subject Independence & Heterogenous EEG Data Sets. In _Proceedings of the NeurIPS 2021 Competitions and Demonstrations Track_ , pages 205–219. PMLR, July 2022. 

- [122] D. Wu, Y. Xu, and B.-L. Lu. Transfer Learning for EEG-Based Brain–Computer Interfaces: A Review of Progress Made Since 2016. _IEEE Transactions on Cognitive and Developmental Systems_ , 14(1):4–19, Mar. 2022. issn: 23798939. doi: `10.1109/TCDS.2020.3007453` . 

- [123] T. Xie, W. Ma, X. Li, W. Li, B. Hao, and X. Tang. Motor imagery EEG recognition based on scheduled empirical mode decomposition and adaptive denoising autoencoders. _IEEE Chinese Automation Congress_ :1528–1532, 2020. issn: 2688-092X. doi: `10 . 1109 / cac51589 . 2020 . 9327855` . 

- [124] F. Xu, F. Rong, Y. Miao, Y. Sun, G. Dong, H. Li, J. Li, Y. Wang, and J. Leng. Representation Learning for Motor Imagery Recognition with Deep Neural Network. _Electronics_ , 10(2):112, Jan. 2021. issn: 2079-9292. doi: `10 . 3390 / electronics10020112` . 

- [125] B. Yan, Y. Wang, Y. Li, Y. Gong, L. Guan, and S. Yu. An EEG signal classification method based on sparse auto-encoders and support vector machine. _IEEE International Conference On Communications In China_ , 2016. issn: 2377-8644. doi: `10 . 1109 / iccchina . 2016 . 7636897` . 

- [126] C. Yang, M. B. Westover, and J. Sun. BIOT: Cross-data Biosignal Learning in the Wild, May 2023. doi: `10 . 48550 / arXiv . 2305 . 10351` . arXiv: `2305.10351 [cs, eess]` . 

- [127] C. Yang, D. Xiao, M. B. Westover, and J. Sun. Self-supervised EEG Representation Learning for Automatic Sleep Staging, Feb. 2023. doi: `10.48550/arXiv.2110.15278` . arXiv: `2110. 15278 [cs, eess]` . 

- [128] J. Yang, Z. Ma, J. Wang, and Y. Fu. A Novel Deep Learning Scheme for Motor Imagery EEG Decoding Based on Spatial Representation Fusion. _IEEE Access_ , 8:202100–202110, 2020. issn: 2169-3536. doi: `10.1109/ACCESS.2020. 3035347` . 

- [129] S. Yang, Z. Yin, Y. Wang, W. Zhang, Y. Wang, and J. Zhang. Assessing cognitive mental workload via EEG signals and an ensemble deep learning classifier based on denoising autoencoders. _Computers in biology_ 

_and medicine_ , 109:159–170, 2019. issn: 18790534. doi: `10.1016/j.compbiomed.2019.04. 034` . 

- [130] X. Yao, T. Li, P. Ding, F. Wang, L. Zhao, A. Gong, W. Nan, and Y. Fu. Emotion classification based on transformer and CNN for EEG spatial-temporal feature learning. _Brain sciences_ , 14(3), 2024. issn: 2076-3425. doi: `10. 3390/brainsci14030268` . 

- [131] Z. Yin, M. Zhao, W. Zhang, Y. Wang, Y. Wang, and J. Zhang. Physiological-signal-based mental workload estimation via transfer dynamical autoencoders in a deep learning framework. _Neurocomputing_ , 347:212–229, 2019. issn: 09252312. doi: `10.1016/j.neucom.2019.02.061` . 

- [132] Z. Yu, L. Li, W. Zhang, H. Lv, Y. Liu, and U. Khalique. An adaptive EEG feature extraction method based on stacked denoising autoencoder for mental fatigue connectivity. _Neural plasticity_ , 2021:3965385, 2021. issn: 1687-5443. doi: `10.1155/2021/3965385` . 

- [133] P. Zhang, X. Wang, J. Chen, W. You, and W. Zhang. Spectral and temporal feature learning with two-stream neural networks for mental workload assessment. _IEEE transactions on neural systems and rehabilitation engineering_ , 27(6):1149–1159, 2019. issn: 1558-0210. doi: `10.1109/tnsre.2019.2913400` . 

- [134] X. Zhang, X. Chen, M. Dong, H. Liu, C. Ge, and L. Yao. Multi-task Generative Adversarial Learning on Geometrical Shape Reconstruction from EEG Brain Signals, Feb. 2020. doi: `10. 48550/arXiv.1907.13351` . arXiv: `1907.13351 [cs, eess]` . 

- [135] X. Zhang, L. Yao, C. Huang, S. S. Kanhere, D. Zhang, and Y. Zhang. Brain2Object: Printing Your Mind from Brain Signals with Spatial Correlation Embedding, June 2020. doi: `10 . 48550/arXiv.1810.02223` . arXiv: `1810.02223 [cs]` . 

- [136] X. Zhang, L. Yao, Q. Z. Sheng, S. S. Kanhere, T. Gu, and D. Zhang. Converting Your Thoughts to Texts: Enabling Brain Typing via Deep Feature Learning of EEG Signals. In _2018 IEEE International Conference on Pervasive Computing and Communications (PerCom)_ , pages 1–10, Mar. 2018. doi: `10.1109/PERCOM. 2018.8444575` . 

- [137] X. Zhang, Z. Lu, T. Zhang, H. Li, Y. Wang, and Q. Tao. Realizing the application of EEG modeling in BCI classification: Based on a conditional GAN converter. _Frontiers in neuroscience_ , 15:727394, 2021. issn: 1662-4548. doi: `10.3389/fnins.2021.727394` . 

_REFERENCES_ 

25 

- [138] X. Zhao, D. Liu, L. Ma, Q. Liu, K. Chen, S. Xie, and Q. Ai. Deep CNN model based on serialparallel structure optimization for four-class motor imagery EEG classification. _Biomedical Signal Processing And Control_ , 72, 2022. issn: 1746-8094. doi: `10 . 1016 / j . bspc . 2021 . 103338` . 

- [139] B. Zhou, A. Lapedriza, J. Xiao, A. Torralba, and A. Oliva. Learning Deep Features for Scene Recognition using Places Database. In _Advances in Neural Information Processing Systems_ , volume 27. Curran Associates, Inc., 2014. 

- [140] O. Zlatov and B. Blankertz. Towards physiologyinformed data augmentation for EEG-based BCIs, Mar. 2022. doi: `10.48550/arXiv.2203. 14392` . arXiv: `2203.14392 [cs, eess]` . 

