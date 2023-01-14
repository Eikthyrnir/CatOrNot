import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt


def normalize(image, label):
    return image / 255, label

directory = ""

train_ds = tf.keras.utils.image_dataset_from_directory(directory,
                                                       validation_split=0.2, subset="training", seed=123, batch_size=32,
                                                       image_size=(512, 512), color_mode='grayscale')

val_ds = tf.keras.utils.image_dataset_from_directory(directory,
                                                     validation_split=0.2, subset="validation", seed=123, batch_size=32,
                                                     image_size=(512, 512), color_mode='grayscale')

train_ds = train_ds.map(normalize)
val_ds = val_ds.map(normalize)


model = keras.Sequential([
    keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=(512, 512, 1)),
    keras.layers.MaxPool2D((2, 2)),

    keras.layers.Conv2D(128, (3, 3), activation='relu'),
    keras.layers.MaxPool2D((2, 2)),

    keras.layers.Conv2D(256, (3, 3), activation='relu'),
    keras.layers.MaxPool2D((2, 2)),

    keras.layers.Flatten(),
    keras.layers.Dense(1024, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

print(model.summary())

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

trainHistory = model.fit(train_ds, epochs=10, validation_data=val_ds)

(loss, accuracy) = model.evaluate(val_ds)
print(loss)
print(accuracy)

model.save("mode2.h5")
