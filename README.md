# Machine-Learning
PsyHeart is a sound therapy application that can be personalized based on the user's circumstances. Users can select sounds according to their current feelings. The sounds used are classified based on BPM and genre which can help users handle their mental conditions.

## Dataset
The dataset we use is GTZAN Audio Dataset and only uses 3 types of audio according to the initial concept of our project, namely Classic, Pop, and Metal.

## Classification
The dataset classification in this project consists of 2 classifications, namely by genre and by Beat Per Minute (BPM). The classification is divided into 6 therapeutic needs, namely sleeplessness, relaxation, depression, motivation, anxiety, and positive energy reinforcement.

For classification by Genre we divided the 3 genres used into 6, namely:
- Classical: Sleeplessness and Relaxation
- Metal : Depression and Motivation
- Pop : Anxiety and Positive Energy Reinforcement

Then the classification based on the above genres is combined with the classification based on BPM, with the BPM classification:
- BPM 31-170: Relaxation
- BPM 61-200 : Motivation
- BPM 51-180 : Positive Energy Reinforcement
- BPM 31-130 : Sleeplessness
- BPM 61-150 : Depression
- BPM 51-140 : Anxiety

## Model
<p align="center">
  <img src="https://github.com/PsyHeart-Capstone-Project/Machine-Learning/assets/159974285/a3c6c122-fd33-4750-b74e-82fb31c6eddd" alt="Loss Graph">
</p>

The model used in this project is Dense Neural Network or Multi-Layer Perceptron (MLP). This model was chosen because it has the lowest loss and highest accuracy among other models.

## Result
The modeling results can be seen below:
<p align="center">
  <img src="https://github.com/PsyHeart-Capstone-Project/Machine-Learning/assets/159974285/935f8e7c-ce65-4ab7-9c5c-2aee3e51497f" alt="Loss Graph">
</p>

from the graph of the analysis results above, a low model loss value of 0.0489 is obtained.

<p align="center">
  <img src="https://github.com/PsyHeart-Capstone-Project/Machine-Learning/assets/159974285/d02c1346-fa4d-4333-90db-23770cf9d7fe" alt="Accuracy Graph">
</p>

and from the graph of the analysis results above, a high model accuracy value of 96.67% is obtained.

## Contributors
The Machine Learning team is responsible for preparing the dataset used, preprocessing the data, building the model, evaluating the model, and storing the model in TFJS for deployment.

The Machine Learning team consists of:
1. [Anggie Alnurin Prasetya](https://github.com/anggiealnrn27) - M011D4KX2154
2. [Anindya Nitisari](https://github.com/anindyantsr) - M011D4KX2156
3. [Tiara Shafadiva](https://github.com/tirshaf) - M227D4KX1860
