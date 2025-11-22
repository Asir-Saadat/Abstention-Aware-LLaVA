This project focuses on training Visual Question Answering (VQA) models to abstain from answering when a question is unanswerable instead of hallucinating a response. The work combines unanswerable question datasets with continual learning methods so models can adapt to new types of unanswerable scenarios without forgetting previous ones.

What is VQA?
Visual Question Answering is a multimodal task where a model answers natural language questions about an image. Typical models extract image features (e.g., via CNN or CLIP), encode the question using a language model, and fuse features to output an answer.

Problem: Models Don’t Abstain
Existing models still output answers even when the question cannot be answered from the image (object missing, masked, altered, mismatched). This occurs because they are not trained to abstain.
Existing Unanswerable Datasets
Examples of how unanswerable questions are created:
Word replacement (swap key nouns in question)
Semantic negation
Image replacement with similar mismatched images
Object masking or copy-move edits

However, every new dataset typically requires retraining models from scratch.

Continual Learning Motivation
Instead of retraining, the model should learn new unanswerable question types over time while maintaining performance on previous datasets. Continual learning balances:
Stability (retain past knowledge)
Plasticity (learn new tasks)


Continual Learning Methods Used
Zero-shot evaluation
Sequential training
Experience Replay
Dark Experience Replay (with distillation)
Dark Experience Replay++
Elastic Weight Consolidation (EWC)
Memory Aware Synapses (MAS)


Abstention Mechanism
A new Image-Question Relevancy Module is introduced, inspired by CLIP and CLIP-UP. This module computes similarity between the question and the visual content using CLIP encoders. A learnable projection layer connects similarity scores to the language model so the system can determine whether to answer or abstain.


Benchmarks and Metrics
Continual Learning metrics
Average Accuracy
Forward Transfer
Backward Transfer


Unanswerable evaluation metrics
Answerable accuracy
Unanswerable accuracy
Abstention rate


Proposed combined metric
Hallucination-Aware Accuracy — takes accuracy + abstention across datasets into account.


Datasets Used
QRPE
UNK-VQA 1
UNK-VQA 2
HaloQuest
UPD


Each dataset provides different forms of unanswerable cases (relevancy labeling, masked objects, counterfactual edits, etc.).


Research Goal
To build the first VQA model that:
Learns to abstain across different datasets
Trains continuously without catastrophic forgetting
Uses relevancy scoring to avoid hallucinations


Timeline (Summary)
Set up LLaVA and scripts
Implement continual learning methods
Add relevancy-based abstention module
Evaluate across all datasets
Final comparison and model selection