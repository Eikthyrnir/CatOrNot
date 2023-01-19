import os

from keras_cat_recognizer import KerasCatRecognizer

cat_dir_name = "cat_images"
not_cat_dirs = ["horse_images", "art_images"]
cat_recognizer = KerasCatRecognizer()


def count_recognition_answers(dir_name: str) -> tuple[int, int]:
    count_positive = 0
    count_imgs = 0

    for file_name in os.listdir(dir_name):
        count_imgs += 1
        if cat_recognizer.is_cat(os.path.join(dir_name, file_name)):
            count_positive += 1

    return count_imgs, count_positive


attempts, correct = count_recognition_answers(cat_dir_name)
print("cats accuracy :", correct / attempts)

for dir_name in not_cat_dirs:
    attempts, incorrect = count_recognition_answers(dir_name)
    print(dir_name + " accuracy :", 1 - incorrect / attempts)
