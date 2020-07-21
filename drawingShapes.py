import cv2
import numpy as np

img = np.zeros((512,512, 3), np.uint8)#black image with 3 channels
# print(img.shape)
# img[:] = 255,0,0 #changes image to blue
# img[200:300, 100:300] = 0,0,255 #changes image to have red square

cv2.line(img, (0, 0), (300, 300), (0, 255 ,0), 3)#for drawing a line on image
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 2)#draw across whole image
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)#filled fills rectangle
cv2.rectangle(img, (0, 0), (250, 350), (255, 0, 0), 2)
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)#first centre then radius
cv2.putText(img, " OPENCV ", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1.3, (0, 150, 0), 3)
cv2.imshow("Image", img)

cv2.waitKey(0)