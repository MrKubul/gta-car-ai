#Module for using trained neural network

import numpy as np
import tensorflow as tf

filepath_angle = './car_angle.h5'
filepath_throttle = './car_angle.h5'
trained_model_angle = tf.keras.models.load_model(filepath_angle, compile=True)
trained_model_throttle = tf.keras.models.load_model(filepath_throttle, compile=True)


def predict_values(image):
    arr = np.array([image, ])
    angle_prediction = trained_model_angle.predict(arr, batch_size=1)[0]
    throttle_prediction = trained_model_throttle.predict(arr, batch_size=1)[0]
    return [angle_prediction, throttle_prediction]