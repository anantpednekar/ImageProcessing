import cv2
import numpy as np

img = cv2.imread('Input.jpeg')
cv2.imshow('Original',img)
cv2.waitKey()

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('GrayScale',gray)
cv2.imwrite('gray.jpg',gray)
cv2.waitKey()

dgray = np.float32(gray)/255.0
dct = cv2.dct(dgray)
image_inverse_dct = cv2.idct(dct)
cv2.imshow('DCT',dct)
cv2.imwrite('DCT.jpg',dct)
cv2.waitKey()

cv2.imshow('IDCT',image_inverse_dct)
cv2.imwrite('IDCT.jpg',image_inverse_dct)
cv2.waitKey()

cv2.destroyAllWindows()
