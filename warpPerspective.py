import cv2
import numpy as np
#Flattens aspect of image
img = cv2.imread("resources/cards.jpg")
width, height = 250, 350 #set width and height of card

pts1 = np.float32([[387, 170], [567, 143], [469, 408], [678, 376]])#points where card corners are
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])#assigns which points are which part of card
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)
cv2.waitKey(0)