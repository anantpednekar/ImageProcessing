import cv2

img = cv2.imread('A.jpeg')
cv2.imshow('Original',img)
cv2.waitKey()

hx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
hy = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
laplace = cv2.Laplacian(img,cv2.CV_64F)

cv2.imshow('Sobel HX',hx)
cv2.imwrite('SobelHX.jpeg',hx)
cv2.waitKey()

cv2.imshow('Sobel Hy',hy)
cv2.imwrite('SobelHy.jpeg',hy)
cv2.waitKey()

cv2.imshow('Laplacian',laplace)
cv2.imwrite('Laplacian.jpeg',laplace)
cv2.waitKey()

