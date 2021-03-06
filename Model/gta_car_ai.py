### File with code from model training on google collab

import unzip as unzip
from google.colab import drive
drive.mount('/content/drive')

!unzip /content/drive/MyDrive/Projekty/dataset.zip

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

traindf = pd.read_csv('/content/dataset/balanced_data2.csv', sep=';')
print(traindf)

def append_ext(fn):
    return fn+".png"
def round_values(val):
  return float(val)
def rescale_angle(angle):
  return round((float(angle)/40), 3)

traindf=pd.read_csv('/content/dataset/balanced_data2.csv', sep=';', dtype='string')
traindf["ID"]=traindf["ID"].apply(append_ext)
traindf["Angle"]=traindf["Angle"].apply(rescale_angle)
traindf["Throttle"]=traindf["Throttle"].apply(round_values)
print(traindf)

datagen=tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255.,validation_split=0.1)
angle_train_generator=datagen.flow_from_dataframe(
    dataframe=traindf,
    directory="/content/dataset",
    x_col= 'ID',
    y_col="Angle",
    subset="training",
    batch_size=8,
    seed=42,
    shuffle=True,
    class_mode="raw",
    target_size=(160,384))

angle_validation_generator=datagen.flow_from_dataframe(
    dataframe=traindf,
    directory="/content/dataset",
    x_col= 'ID',
    y_col="Angle",
    subset="validation",
    batch_size=8,
    seed=42,
    shuffle=True,
    class_mode="raw",
    target_size=(160,384))

throttle_train_generator=datagen.flow_from_dataframe(
    dataframe=traindf,
    directory="/content/dataset",
    x_col= 'ID',
    y_col="Throttle",
    subset="training",
    batch_size=32,
    seed=42,
    shuffle=True,
    class_mode="raw",
    target_size=(160,384))

throttle_validation_generator=datagen.flow_from_dataframe(
    dataframe=traindf,
    directory="/content/dataset",
    x_col= 'ID',
    y_col="Throttle",
    subset="validation",
    batch_size=32,
    seed=42,
    shuffle=True,
    class_mode="raw",
    target_size=(160,384))

from tensorflow import keras
from tensorflow.keras import layers

inputs = keras.Input(shape=(160,384,3))
x = layers.Conv2D(filters = 32, kernel_size = 3, activation = "relu") (inputs)
x = layers.MaxPooling2D(pool_size=2) (x)
x = layers.Conv2D(filters = 64, kernel_size = 3, activation = "relu") (x)
x = layers.MaxPooling2D(pool_size=2) (x)
x = layers.Conv2D(filters = 128, kernel_size = 3, activation = "relu") (x)
x = layers.Flatten() (x)
x = layers.Dense(64, activation="relu") (x)
x = layers.Dropout(0.2) (x)
x = layers.Dense(32, activation="relu") (x)
x = layers.Dropout(0.1) (x)
x = layers.Dense(8, activation="relu") (x)
outputs_angle = layers.Dense(1) (x)

model_angle = keras.Model(inputs, outputs=outputs_angle)
print(model_angle.summary())

inputs = keras.Input(shape=(160,384,3)) 
x = layers.Conv2D(filters = 32, kernel_size = 3, activation = "relu") (inputs)
x = layers.MaxPooling2D(pool_size=2) (x)
x = layers.Conv2D(filters = 64, kernel_size = 3, activation = "relu") (x)
x = layers.MaxPooling2D(pool_size=2) (x)
x = layers.Conv2D(filters = 128, kernel_size = 3, activation = "relu") (x)
x = layers.Flatten() (x)
x = layers.Dense(64, activation="relu") (x)
x = layers.Dropout(0.2) (x)
x = layers.Dense(32, activation="relu") (x)
x = layers.Dropout(0.1) (x)
x = layers.Dense(8, activation="relu") (x)
outputs_throttle = layers.Dense(1) (x)

model_throttle = keras.Model(inputs, outputs=outputs_throttle)
print(model_throttle.summary())

model_angle.compile(loss={'dense_11': 'mean_squared_error'},
              optimizer='adam')

callbacks = [
    keras.callbacks.ModelCheckpoint(
        filepath="/content/drive/MyDrive/gta-car-ai_angle",
        save_best_only = True,
        monitor = "val_loss")
]


angle_history = model_angle.fit(angle_train_generator,validation_data=angle_validation_generator, epochs = 3, callbacks=callbacks)

model_throttle.compile(loss={'dense_15': 'mean_squared_error'},
              optimizer='adam')

callbacks = [
    keras.callbacks.ModelCheckpoint(
        filepath="/content/drive/MyDrive/gta-car-ai_throttle",
        save_best_only = True,
        monitor = "val_loss")
]


throttle_history = model_throttle.fit(throttle_train_generator,validation_data=throttle_validation_generator, epochs = 1, callbacks=callbacks)

import matplotlib.pyplot as plt
import numpy as np


test_model_angle = keras.models.load_model("/content/drive/MyDrive/gta-car-ai_angle")
test_model_throttle = keras.models.load_model("/content/drive/MyDrive/gta-car-ai_throttle")

for i in range(1):
     image, label = angle_train_generator.next()
     plt.imshow(image[0])
     prediction = test_model_angle.predict(image, batch_size=1)[0]
     print(prediction)
     prediction = test_model_throttle.predict(image, batch_size=1)[0]
     print(prediction)

test_model_angle.save('car_angle.h5')
test_model_throttle.save('car_throttle.h5')
from google.colab import files
files.download('car_angle.h5')
files.download('car_throttle.h5')