from tensorflow import keras
import numpy as np
import cv2

class CatRecognizer:
    def is_cat(self, image_path: str) -> bool:
        model = keras.applications.VGG16()

        img_dir = image_path

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

        raise NotImplementedError


# img_dir = 'image_dir/photo_2022-12-18_15-03-48.jpg'

# CatRecognizer1 = CatRecognizer()
# print(CatRecognizer1.is_cat('image_dir/HERE_PUT_IMAGE_AND_NAME_IT_LIKE_THIS.jpeg'))
