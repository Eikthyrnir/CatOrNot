import os
import numpy as np
import tensorflow as tf
from tensorflow import keras

directory = ""

train_ds = tf.keras.utils.image_dataset_from_directory(directory, validation_split=0.2,
                                                       subset="training", seed=123, batch_size=32)
val_ds = tf.keras.utils.image_dataset_from_directory(directory, validation_split=0.2,
                                                     subset="validation", seed=123, batch_size=32)

model = keras.models.load_model("C:/Users/KimD/PycharmProjects/Project_AI3/ver/mode2.h5")
predictions = model.predict(val_ds.take(32))


classNames = ['not', 'cat']

direct = ''
os.chdir(direct)

i = 0
for image, _ in val_ds.take(32):
    predictedLabel = int(predictions[i] >= 0.5)

    filename = classNames[predictedLabel] + str(i) + '.jpeg'
    tf.keras.preprocessing.image.save_img(direct+filename, image[0])
    i += 1
