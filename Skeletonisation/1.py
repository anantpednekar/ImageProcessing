import cv2
from skimage.morphology import skeletonize

img = cv2.imread('Input.png',0)
skel = cv2.skeletonize(img)

cv2.imshow("skel",skel)
cv2.imwrite('Skel_Output.png',skel)
cv2.waitKey(0)
cv2.destroyAllWindows()
