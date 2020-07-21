import cv2
print("Package Imported")

cap = cv2.VideoCapture("resources/dashcam.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break