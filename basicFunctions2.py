import cv2
import numpy as np
print("Packages imported")

img = cv2.imread("resources/tesla_modelX.jpg")
print(img.shape)#gives shape of image (height, width, channels)

imgResize = cv2.resize(img, (1000, 300))#for resize it is first width then height
imgResizeBigger = cv2.resize(img, (2000, 800))#can also make image bigger but wont improve quality
print(imgResize.shape)

imgCropped = img[0:200, 200:500]#height first then width for cropping

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Resize Bigger", imgResizeBigger)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)