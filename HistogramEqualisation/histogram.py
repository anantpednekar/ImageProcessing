import cv2
import matplotlib.pyplot as plt

img = cv2.imread('A.jpeg')
cv2.imshow('Original',img)
cv2.waitKey()

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('GrayScale',gray)
cv2.imwrite('gray.jpeg',gray)
cv2.waitKey()

hist = cv2.calcHist([gray],[0],None,[256],[0,256])

plt.xlabel('Pixel Value')
plt.ylabel('Number of Pixels')
plt.plot(hist)
plt.savefig('HistogramBefore')
plt.show()


equ = cv2.equalizeHist(gray)

hist = cv2.calcHist([equ],[0],None,[256],[0,256])

plt.xlabel('Pixel Value')
plt.ylabel('Number of Pixels')
plt.plot(hist)
plt.savefig('HistogramAfter')
plt.show()

cv2.imshow('Equalised Histogram',equ)
cv2.imwrite('HistEqu.jpeg',equ)
cv2.waitKey()

