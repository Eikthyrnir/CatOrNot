from tensorflow import keras
import numpy as np
import cv2


class Recognation:
    def __init__(self, picture):
        self.picture = picture

    def recognize(self):
        model = keras.applications.VGG16()

        img = self.picture
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


# img_dir = 'image_dir/dgwesdgfs.jpeg'
#
# img = cv2.imread(img_dir)
# Recognation1 = Recognation(img)
#
# if Recognation1.recognize() == True:
#     print(0)
# else:
#     print(1)
