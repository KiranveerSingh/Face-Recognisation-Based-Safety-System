import cv2

cap = cv2.VideoCapture(0)

count = 0

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Capture Face", gray)

    if cv2.waitKey(1) & 0xFF == 32:  # SPACE
        cv2.imwrite(f"face_GURLEEN_{count}.jpg", gray)
        count += 1
        print("Captured")

    if count >= 5:
        break

cap.release()
cv2.destroyAllWindows()