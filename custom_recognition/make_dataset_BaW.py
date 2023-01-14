import os

import cv2

directory_BaW = r''
directory_RGB = r''

for i in range(2500):
    stry = directory_RGB+str(i)+'.jpeg'

    # print(stry)

    img = cv2.imread(stry)

    img = cv2.GaussianBlur(img, (1,1), 0)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.Canny(img, 100, 150)

    # cv2.imshow('Result', img)
    # cv2.waitKey(0)

    os.chdir(directory_BaW)

    filename = 'CAT_'+str(i)+'.jpeg'
    cv2.imwrite(filename, img)

    os.chdir(directory_BaW)

print('hello')

