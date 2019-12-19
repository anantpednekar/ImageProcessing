import cv2
import numpy

img = cv2.imread('O_Input.png',0)
kernel = numpy.ones((5,5),numpy.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.waitKey()

cv2.imshow('Opening',opening)
cv2.imwrite('OpeningOutput.png',opening)
cv2.waitKey()
