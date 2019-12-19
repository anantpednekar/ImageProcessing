import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Input.jpeg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(imgray,230,255)

cv2.imshow("Canny Edge", edges)
cv2.imwrite('CannyEdge.jpeg',edges)
cv2.waitKey()

contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (255,0,0), 3)

cv2.imshow("BorderTracing", img)
cv2.imwrite('BorderTracing.jpeg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

