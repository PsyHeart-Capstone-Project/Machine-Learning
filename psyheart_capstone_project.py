# -*- coding: utf-8 -*-
"""PsyHeart Capstone Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1u6ReYhC9DI_w7fG_PWY1ZGOidXVg9qr8

# Input The Dataset
The dataset we use is GTZAN Audio Dataset and only uses 3 types of audio according to the initial concept of our project, namely Classic, Pop, and Metal.
"""

import tensorflow as tf
from google.colab import drive
import pandas as pd
import os
import random
from IPython.display import Audio
import numpy as np
import librosa
import subprocess
from collections import Counter
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from google.colab import drive
drive.mount('/content/drive')

# Path to folder
folder = '/content/drive/Shareddrives/dataset'

# Get a list of files in a folder
files = os.listdir(folder)

# Show all files in a folder
print("All files in", folder, ":\n")
for file_or_folder in files:
    print(file_or_folder)

# Count the number of files
number_of_files = len(files)
print("\nTotal number of files in a folder:", number_of_files)

import wave

# Path to the "classical" folder
classical_folder = os.path.join(folder, 'classical')

# Function to open and read wav file in folder
def read_wav_file(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.wav'):  # Check if the file is in .wav format
                print(f"Open file: {file_path}\n")
                try:
                    with wave.open(file_path, 'rb') as wav_file:
                        # Get basic information about the wav file
                        n_channels = wav_file.getnchannels()
                        sampwidth = wav_file.getsampwidth()
                        framerate = wav_file.getframerate()
                        n_frames = wav_file.getnframes()
                        duration = n_frames / float(framerate)

                        print(f"Number of channels: {n_channels}")
                        print(f"Sample width: {sampwidth} bytes")
                        print(f"Frame rate: {framerate} frames/second")
                        print(f"Number of frames: {n_frames}")
                        print(f"Duration: {duration:.2f} seconds")
                        print("\n")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

# Show files in the "dataset" folder
print("Read WAV file in dataset folder:\n")
read_wav_file(folder)

"""Check one of the files in the folder"""

from IPython.display import Audio

# Path to the wav file that you want to play
file_path = '/content/drive/Shareddrives/dataset/classical/classical.00007.wav'

# Play the wav file
print(f"Opening and playing file: {file_path}")
Audio(file_path, autoplay=True)

"""#Label The Data

Label the data based on BPM (Beat Per Minute) which is divided into 3 classifications: low, medium, and high.


*   Low: sleeplessness and relaxation
*   Medium: anxiety and positive emotion reinforcement.
*   Medium to High: depression and motivation.



"""

# Path to a folder that contains the audio files
folder_path = '/content/drive/Shareddrives/dataset/'

# Get a list of folders inside the dataset folder
folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]

# Show the list of folders as data labels
labels = []
for folder in folders:
    folder_files = os.listdir(os.path.join(folder_path, folder))
    for file in folder_files:
        labels.append(folder)

# Show the data label
print("Data label:")
print(labels)

!pip install pydub

"""Classify music genres based on therapy needs"""

from pydub import AudioSegment
import os
import numpy as np
import librosa

# Classify music genres based on therapy needs
genre_to_therapy = {
    "classical": ["Sleeplessness", "Relaxation"],
    "metal": ["Depression", "Motivation"],
    "pop": ["Anxiety", "Positive Emotion Reinforcement"],
}

# Function to calculate the BPM of an audio file
def get_bpm(file_path):
    audio = AudioSegment.from_file(file_path)
    samples = np.array(audio.get_array_of_samples(), dtype=np.float32)
    samples /= np.max(np.abs(samples))  # Normalize to range [-1, 1]
    tempo, _ = librosa.beat.beat_track(y=samples, sr=audio.frame_rate)
    return tempo

# Determine therapy classification based on genre and BPM
def determine_therapy_classification(folder, bpm):
    genre = folder.lower()
    if genre in genre_to_therapy:
        therapy_classifications = genre_to_therapy[genre]
        for therapy_classification in therapy_classifications:
            if "relaxation" in therapy_classification.lower() and 30 < bpm <= 170:
                return therapy_classification
            elif "motivation" in therapy_classification.lower() and 60 < bpm <= 200:
                return therapy_classification
            elif "positive emotion reinforcement" in therapy_classification.lower() and 50 < bpm <= 180:
                return therapy_classification
            elif "sleeplessness" in therapy_classification.lower() and 30 < bpm <= 130:
                return therapy_classification
            elif "depression" in therapy_classification.lower() and 60 < bpm <= 150:
                return therapy_classification
            elif "anxiety" in therapy_classification.lower() and 50 < bpm <= 140:
                return therapy_classification
    return "Unknown"

# Path to the audio dataset folder
folder_path = "/content/drive/Shareddrives/dataset"   # Replace with folder path containing genre folders
folders = ["classical", "metal", "pop"]  # List of genre folders

# Data label
labels = []

for folder in folders:
    folder_path_full = os.path.join(folder_path, folder)
    folder_files = os.listdir(folder_path_full)
    for file in folder_files:
        file_path = os.path.join(folder_path_full, file)
        if file_path.endswith('.wav'):  # Make sure to process only audio files
            try:
                bpm = get_bpm(file_path)
                therapy_classification = determine_therapy_classification(folder, bpm)
                labels.append((file, therapy_classification))
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

# Show the data label
print("Data label:")
for label in labels:
    print(label)

"""Check the BPM of each file"""

from pydub import AudioSegment
import numpy as np
import librosa
import os

# Classify music genres based on therapy needs
genre_to_therapy = {
    "classical": ["Sleeplessness", "Relax"],
    "metal": ["Depression", "Motivation"],
    "pop": ["Anxiety", "Positive Emotion Reinforcement"],
}

# Function to calculate BPM and beats from audio files
def get_bpm_and_beats(file_path):
    audio = AudioSegment.from_file(file_path)
    samples = np.array(audio.get_array_of_samples(), dtype=np.float32)
    samples /= np.max(np.abs(samples))  # Normalize to range [-1, 1]
    tempo, beat_frames = librosa.beat.beat_track(y=samples, sr=audio.frame_rate)
    beats = librosa.frames_to_time(beat_frames, sr=audio.frame_rate)
    print(f"File name: {file_path.split('/')[-1]}, BPM: {tempo}")
    return tempo, beats


# Path to the audio dataset folder
folder_path = "/content/drive/Shareddrives/dataset"  # Replace with folder path that contains genre folders

for folder in genre_to_therapy:
    folder_path_full = os.path.join(folder_path, folder)
    folder_files = os.listdir(folder_path_full)
    for file in folder_files:
        file_path = os.path.join(folder_path_full, file)
        if file_path.endswith('.wav'):  # Make sure to process only audio files
            try:
                bpm, beats = get_bpm_and_beats(file_path)
                labels.append((file, genre_to_therapy[folder], bpm, beats))
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

"""Extract features from the file"""

# Classify music genres based on therapy needs
genre_to_therapy = {
    "classical": ["Sleeplessness", "Relax"],
    "metal": ["Depression", "Motivation"],
    "pop": ["Anxiety", "Positive Emotion Reinforcement"],
}

# Function to calculate BPM and extract MFCC features
def extract_features_and_bpm(file_paths):
    features = []
    for file_path in file_paths:
        # Load audio file
        audio, sr = librosa.load(file_path)
        # Feature extraction (example: 20 MFCC coefficients)
        mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=20)
        # Average of each MFCC coefficient
        mfccs_mean = np.mean(mfccs, axis=1)

        # Calculate the BPM
        audio_segment = AudioSegment.from_file(file_path)
        samples = np.array(audio_segment.get_array_of_samples(), dtype=np.float32)
        samples /= np.max(np.abs(samples))  # Normalize to range [-1, 1]
        bpm, _ = librosa.beat.beat_track(y=samples, sr=audio_segment.frame_rate)

        # Combining MFCC and BPM features
        features.append(np.append(mfccs_mean, bpm))
    return np.array(features)

"""# Exploratory Data Analysis
Conducting exploratory data analysis by checking the data format and the amount of data aims to find out whether all the data are already in wav format or not and also to find out whether the data has a balanced amount for each class.

1. Check the data format
"""

# Path to a folder that contains the audio files
folder_path = '/content/drive/Shareddrives/dataset'

# Dictionary to store the number of files for each type of data format
format_count = {}

# List of folders that we will explore
folders_to_explore = ['classical', 'pop', 'metal']

# Loop through all the files in the folder
for file_name in os.listdir(folder_path):
    # Retrieve file extension
    file_ext = os.path.splitext(file_name)[1].lower()
    # Check if the file extension has been placed in the dictionary
    if file_ext in format_count:
        # Add the number of files for an existing extension
        format_count[file_ext] += 1
    else:
        # Create a new entry in the dictionary if the extension does not already exist
        format_count[file_ext] = 1

# Show the number of files with different formats
print("Number of files with format:")
for ext, count in format_count.items():
    print(f"{ext}: {count}")

# Loop through the files in the folder and open a file for each existing format
for ext in format_count.keys():
    # Specify the folder path for the specified file format
    format_folder_path = os.path.join(folder_path, ext.replace('.', ''))
    # Show the file name of each format
    print(f"\nFile in {ext} format:")
    for file_name in os.listdir(format_folder_path):
        print(file_name)

# Show all files in each subfolder
for folder_name in folders_to_explore:
    folder_subpath = os.path.join(folder_path, folder_name)
    print(f"\nFile in {folder_name} folder:")
    for file_name in os.listdir(folder_subpath):
        print(file_name)

"""2. Checking the number of datasets"""

# Dictionary to store the amount of data for each class
class_count = {folder_name: 0 for folder_name in folders_to_explore}

# Loop through each folder
for folder_name in folders_to_explore:
    folder_subpath = os.path.join(folder_path, folder_name)
    class_count[folder_name] = len(os.listdir(folder_subpath))

# Show the amount of data for each class
print("The amount of data for each class:")
for folder_name, count in class_count.items():
    print(f"{folder_name}: {count}")

"""#Split The Data into Train Data and Test Data
Divide the data into training data and testing data with a division ratio is 80% for training data and 20% for testing data.
"""

# Initialize a list to hold the file paths of each class
file_paths = []
labels = []

# Loop through each folder
for folder_name in folders_to_explore:
    folder_subpath = os.path.join(folder_path, folder_name)
    # MGet the file path of each class
    class_files = [os.path.join(folder_subpath, file_name) for file_name in os.listdir(folder_subpath)]
    file_paths.extend(class_files)
    labels.extend([folder_name] * len(class_files))  # Add a label for each file

# Splitting data into training and test data
train_files, test_files, train_labels, test_labels = train_test_split(file_paths, labels, test_size=0.2, random_state=42)

# Path to the folder containing the audio files
folder_path = '/content/drive/Shareddrives/dataset'

# List of folders that we will explore
folders_to_explore = ['classical', 'pop', 'metal']

# Function to extract features from audio files (example: MFCC)
def extract_features(file_paths):
    features = []
    for file_path in file_paths:
        # Load audio file
        audio, sr = librosa.load(file_path)
        # Feature extraction (example: 20 MFCC coefficients)
        mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=20)
        # Average of each MFCC coefficient
        mfccs_mean = np.mean(mfccs, axis=1)
        features.append(mfccs_mean)
    return np.array(features)

# Read files and extract features for training and test data
X_train = extract_features_and_bpm(train_files)
X_test = extract_features_and_bpm(test_files)

# Create numeric labels for classes
class_mapping = {class_name: index for index, class_name in enumerate(folders_to_explore)}
y_train = np.array([class_mapping[label] for label in train_labels])
y_test = np.array([class_mapping[label] for label in test_labels])

# Show the information about data sharing
print("Number of training data:", len(train_files))
print("Number of test data:", len(test_files))
print("X_train feature size:", X_train.shape)
print("X_test feature size:", X_test.shape)
print("y_train label size:", y_train.shape)
print("y_test label size:", y_test.shape)

"""Modeling using Dense Neural Network (DNN) or Feedforward Neural Network/Multilayer Perceptron (MLP)"""

from sklearn.metrics import classification_report

num_classes = len(class_mapping)
input_dim = X_train.shape[1]

# Definition the model with hybrid method
inputs = tf.keras.layers.Input(shape=(input_dim,))
x = tf.keras.layers.Dense(512, activation='relu')(inputs)
x = tf.keras.layers.Dropout(0.5)(x)
x = tf.keras.layers.Dense(256, activation='relu')(x)
x = tf.keras.layers.BatchNormalization()(x)
x = tf.keras.layers.Dropout(0.5)(x)
x = tf.keras.layers.Dense(128, activation='relu')(x)
x = tf.keras.layers.Dropout(0.5)(x)
x = tf.keras.layers.Flatten()(x)
outputs = tf.keras.layers.Dense(num_classes, activation='softmax')(x)

# Model initialization
model = tf.keras.Model(inputs=inputs, outputs=outputs)

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=150, batch_size=32, validation_data=(X_test, y_test))

# Model evaluation on test data
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Loss: {loss:.4f}')
print(f'Test Accuracy: {accuracy:.4f}')

# Prediction on test data
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)

# Show the classification report
print('\nClassification Report:')
print(classification_report(y_test, y_pred_classes))

import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import plot_model
from sklearn.metrics import classification_report
from IPython.display import Image

plot_model(model, to_file='model.png', show_shapes=True, show_layer_names=True)
Image(filename='model.png')

"""Accuracy from Dense Neural Network (DNN) model."""

from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

# Create a plot to check for overfitting
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Train and Validation Accuracy Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')

plt.show()

"""Loss from Dense Neural Network (DNN) model"""

from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

# Create a plot to check for overfitting
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Train and Validation Loss Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend(loc='upper right')

plt.show()

"""Modeling using Convolutional Neural Network (CNN)"""

import tensorflow as tf

# CNN model initialization
model_cnn = tf.keras.Sequential([
    tf.keras.layers.Reshape((X_train.shape[1], 1), input_shape=(X_train.shape[1],)),
    tf.keras.layers.Conv1D(64, 3, activation='relu', padding='same'),
    tf.keras.layers.MaxPooling1D(2),
    tf.keras.layers.Conv1D(128, 3, activation='relu', padding='same'),
    tf.keras.layers.MaxPooling1D(2),
    tf.keras.layers.Conv1D(256, 3, activation='relu', padding='same'),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(num_classes, activation='softmax')
])

# Compile the model
model_cnn.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Show the model summary
model_cnn.summary()

# Train the CNN model
history_cnn = model_cnn.fit(X_train[..., np.newaxis], y_train, epochs=150, batch_size=32, validation_data=(X_test[..., np.newaxis], y_test))

# Model evaluation on test data
loss_cnn, accuracy_cnn = model_cnn.evaluate(X_test[..., np.newaxis], y_test)
print(f'Test Loss (CNN): {loss_cnn:.4f}')
print(f'Test Accuracy (CNN): {accuracy_cnn:.4f}')

"""Modeling using Recurrent Neural Network (RNN)"""

import tensorflow as tf

# RNN model initialization
model_rnn = tf.keras.Sequential([
    tf.keras.layers.Reshape((X_train.shape[1], 1), input_shape=(X_train.shape[1],)),
    tf.keras.layers.LSTM(64, return_sequences=True),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.LSTM(128),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(num_classes, activation='softmax')
])

# Compile the model
model_rnn.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Show the model summary
model_rnn.summary()

# Train the RNN model
history_rnn = model_rnn.fit(X_train[..., np.newaxis], y_train, epochs=150, batch_size=32, validation_data=(X_test[..., np.newaxis], y_test))

# Model evaluation on test data
loss_rnn, accuracy_rnn = model_rnn.evaluate(X_test[..., np.newaxis], y_test)
print(f'Test Loss (RNN): {loss_rnn:.4f}')
print(f'Test Accuracy (RNN): {accuracy_rnn:.4f}')

"""Modeling using a hybrid model (CNN-RNN)"""

import tensorflow as tf

# Initialize the hybrid model
inputs = tf.keras.layers.Input(shape=(X_train.shape[1],))
x = tf.keras.layers.Reshape((X_train.shape[1], 1), input_shape=(X_train.shape[1],))(inputs)
x = tf.keras.layers.Conv1D(64, 3, activation='relu')(x)
x = tf.keras.layers.MaxPooling1D(pool_size=2)(x)
x = tf.keras.layers.LSTM(64)(x)
x = tf.keras.layers.Dense(128, activation='relu')(x)
outputs = tf.keras.layers.Dense(num_classes, activation='softmax')(x)

# Model initialization
model_hybrid = tf.keras.Model(inputs=inputs, outputs=outputs)

# Compile the model
model_hybrid.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Show the model summary
model_hybrid.summary()

# Train the hybrid model
history_hybrid = model_hybrid.fit(X_train, y_train, epochs=150, batch_size=32, validation_data=(X_test, y_test))

# Model evaluation on test data
loss_hybrid, accuracy_hybrid = model_hybrid.evaluate(X_test, y_test)
print(f'Test Loss (Hybrid): {loss_hybrid:.4f}')
print(f'Test Accuracy (Hybrid): {accuracy_hybrid:.4f}')

"""Out of four modeling performed, the selected model is Dense Neural Network (DNN). The four models have approximately the same level of accuracy but the DNN model has the lowest loss value.

Change the file format to TensorFlow.js
"""

# Save the model in TensorFlow SavedModel format
model.save('/content/saved_model/my_model')

!pip install tensorflowjs

!tensorflowjs_converter --input_format=tf_saved_model --output_format=tfjs_graph_model /content/saved_model/my_model /content/tfjs_model