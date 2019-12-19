import cv2
import matplotlib.pyplot as plt

img = cv2.imread('A.jpeg')
cv2.imshow('Original',img)
cv2.waitKey()

med = cv2.medianBlur(img,5)
cv2.imwrite('Output.jpeg',med)
cv2.imshow('Original',med)
cv2.waitKey()

