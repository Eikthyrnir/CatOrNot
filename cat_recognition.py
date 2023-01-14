from tensorflow import keras
from cat_recognizer import CatRecognizer
import numpy as np
import cv2


class MyCatRecognizer(CatRecognizer):

    def is_cat(self, image_path: str) -> bool:
        model = keras.applications.VGG16()

        img = cv2.imread(image_path)
        img = cv2.resize(img, (224, 224))
        img = np.array(img)

        x = keras.applications.vgg16.preprocess_input(img)
        x = np.expand_dims(x, axis=0)

        res = model.predict(x)
        res = np.argmax(res)

        # VGG16 is based on imagenet dataset, in this dataset the cat IDs range from 281 to 285
        return 281 <= res <= 285


# img_dir = 'image_dir/photo_2022-12-18_15-03-48.jpg'

# CatRecognizer1 = MyCatRecognizer()
# print(CatRecognizer1.is_cat('image_dir/photo_2022-12-18_15-03-48.jpg'))
