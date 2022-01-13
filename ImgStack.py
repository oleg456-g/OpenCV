import cv2
import numpy

img = cv2.imread('images/1.jpg')
HorizontStack = numpy.hstack((img, img))
VertStack = numpy.vstack((img, img))

cv2.imshow('HorizontStack', HorizontStack)
cv2.imshow('VertStack', VertStack)

cv2.waitKey(0)
