from tensorflow import keras
import numpy as np
import cv2


model = keras.applications.VGG16()

def CATorNOT(img_dir):
    img = cv2.imread(img_dir)
    img = cv2.resize(img, (224, 224))
    img = np.array(img)
    x = keras.applications.vgg16.preprocess_input(img)
    x = np.expand_dims(x, axis=0)

    res = model.predict(x)
    res = np.argmax(res)

    if 281 <= res <= 285:
        return True
    else:
        return False

