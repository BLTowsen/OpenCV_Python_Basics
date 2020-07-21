import cv2
print("Package imported")

cap = cv2.VideoCapture(0)#0 selects default webcam
cap.set(3, 640)#width
cap.set(4, 480)#height
cap.set(10, 50)#brightness

while True:
    success, img = cap.read()
    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break