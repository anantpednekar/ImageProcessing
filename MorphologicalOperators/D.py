import cv2
import numpy

img = cv2.imread('Input.png',0)
kernel = numpy.ones((5,5),numpy.uint8)
dialation = cv2.dilate(img, kernel, iterations=1)
cv2.waitKey()

cv2.imshow('Dialation',dialation)
cv2.imwrite('DialationOutput.png',dialation)
cv2.waitKey()
