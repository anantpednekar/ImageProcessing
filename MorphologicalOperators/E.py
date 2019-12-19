import cv2
import numpy

img = cv2.imread('Input.png',0)
kernel = numpy.ones((5,5),numpy.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
cv2.waitKey()

cv2.imshow('Erosion',erosion)
cv2.imwrite('ErosionOutput.png',erosion)
cv2.waitKey()
