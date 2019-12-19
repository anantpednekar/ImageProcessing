import cv2
import numpy

img = cv2.imread('C_Input.png',0)
kernel = numpy.ones((5,5),numpy.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.waitKey()

cv2.imshow('Closing',closing)
cv2.imwrite('ClosingOutput.png',closing)
cv2.waitKey()
