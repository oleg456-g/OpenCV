import cv2
import numpy as np


img = cv2.imread(r'images\1.jpg')
#Изменение изображения
img = cv2.resize(img, (img.shape[1] * 2, img.shape[0] * 2))
#Размытие изображения
img = cv2.GaussianBlur(img, (51, 51), 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Приведение в контур
img = cv2.Canny(img, 50, 50)
#Увеличение длины контура
kernel = np.ones((5, 5), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)

# img = cv2.erode(img, kernel, iterations=1)
cv2.imshow('result', img)

cv2.waitKey(0)
