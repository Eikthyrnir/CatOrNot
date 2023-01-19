from tensorflow import keras
from cat_recognizer import CatRecognizer
import numpy as np
import cv2


class KerasCatRecognizer(CatRecognizer):

    def __init__(self) -> None:
        self.model = keras.applications.VGG16()

    def is_cat(self, image_path: str) -> bool:
        img = cv2.imread(image_path)
        img = cv2.resize(img, (224, 224))
        img = np.array(img)

        x = keras.applications.vgg16.preprocess_input(img)
        x = np.expand_dims(x, axis=0)

        res = self.model.predict(x)
        res = np.argmax(res)

        # VGG16 is based on imagenet dataset, in this dataset the cat IDs range from 281 to 285
        return 281 <= res.item() <= 285
