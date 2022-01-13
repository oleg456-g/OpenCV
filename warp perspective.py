import cv2
import numpy

img = cv2.imread('images/play_carts.jpg')

width, height = 260, 350

#Даём координаты углов
pts1 = numpy.float32([[101, 408], [320, 322], [152, 641], [342, 558]])
#Определяем широту и высоту
pts2 = numpy.float32([[0, 0], [width, 0], [0, height], [width, height]])
#Расчитывает перспективное преобразование по 4 парам точек
matrix = cv2.getPerspectiveTransform(pts1, pts2)
#Выполняет перспективное преобразование
imgOutput = cv2.warpPerspective(img, matrix, (width, height))
#Выделяет цель точками
for i in range(4):
    cv2.circle(img, (int(pts1[i][0]), int(pts1[i][1])), 6, (0, 0, 255), cv2.FILLED)
#Отображает изображения
cv2.imshow('Before', img)

cv2.imshow('After', imgOutput)

cv2.waitKey(0)
