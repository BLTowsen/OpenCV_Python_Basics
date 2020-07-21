import cv2
print('Package Imported')

img = cv2.imread("resources/mePhoto.jfif")

cv2.imshow("Output", img)
cv2.waitKey(0)#0 means that image will stay until closed