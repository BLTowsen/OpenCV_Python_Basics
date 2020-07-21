import cv2
import numpy as np
print("Packages Imported")

img = cv2.imread("resources/mePhoto.jfif")
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#converts image into different colour spaces
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)#kernel side must be odd numbers
imgCanny = cv2.Canny(img, 100, 100)#finding edges
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)#increases thickness of lines
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)#decreases line thickness

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)