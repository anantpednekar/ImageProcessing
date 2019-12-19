import cv2

img = cv2.imread('1.jpeg')
cv2.imshow('Original',img)
cv2.waitKey()

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('GrayScale',gray)
cv2.imwrite('gray.jpeg',gray)
cv2.waitKey()

retval2,threshold2 = cv2.threshold(gray,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Otsu threshold',threshold2)
cv2.imwrite('Otsu threshold.jpeg',threshold2)
cv2.waitKey()
