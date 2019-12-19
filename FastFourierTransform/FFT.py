import numpy as np
import cv2

img = cv2.imread('Input.jpeg')
cv2.imshow('Original',img)
cv2.waitKey()

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('GrayScale',gray)
cv2.imwrite('gray.jpg',gray)
cv2.waitKey()

dft = cv2.dft(np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

cv2.imshow('MagnitudeSpectrum',magnitude_spectrum)
cv2.imwrite('MagnitudeSpectrum.jpg',magnitude_spectrum)
cv2.waitKey()

cv2.destroyAllWindows()
