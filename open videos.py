import cv2
cap = cv2.VideoCapture(r'videos\New Year - 100050.mp4')
#
while True:
    success, img = cap.read()
    cv2.imshow('Result', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
