import cv2 as cv

import numpy as np

img = cv.imread('IPA.png',0)

kernel = np.ones((5,5),np.uint8)

erosao = cv.erode(img,kernel,iterations = 1)

cv.imshow('erosão', erosao)
