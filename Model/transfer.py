### File with code from transfer learning model training on google collab

!pip install -U efficientnet

import efficientnet.keras as efn
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.applications import EfficientNetB0, EfficientNetB3, EfficientNetB4

base_model = EfficientNetB0(input_shape = (160,384, 3), include_top = False, weights = 'imagenet')

for layer in base_model.layers:
    layer.trainable = False

x = base_model.output
x = layers.Flatten()(x)
x = layers.Dense(1024, activation="relu")(x)
x = layers.Dropout(0.5)(x)

# Add a final sigmoid layer with 1 node for classification output
predictions = layers.Dense(1, activation="sigmoid")(x)
model_final = keras.Model(base_model.input, outputs = predictions)

from tensorflow import keras
from tensorflow.keras import layers

callbacks = [
    keras.callbacks.ModelCheckpoint(
        filepath="/content/drive/MyDrive/gta-car-ai_transfer",
        save_best_only = True,
        monitor = "val_loss")
]

model_final.compile(optimizer='adam',loss='mean_squared_error')

angle_history = model_final.fit(angle_train_generator,validation_data=angle_validation_generator, epochs = 5, callbacks=callbacks)