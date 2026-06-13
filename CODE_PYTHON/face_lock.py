import cv2
import serial
import time

ser = serial.Serial('COM3', 9600)
time.sleep(2)

model = cv2.face.LBPHFaceRecognizer_create()
model.read("trainer.yml")

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

cap = cv2.VideoCapture(0)

last_scan = 0
scan_interval = 2

busy = False
busy_end_time = 0

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    current_time = time.time()

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw rectangle
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)

    # 🔴 IF BUSY → no detection
    if busy:
        if current_time > busy_end_time:
            print("🔒 Auto Lock")

            # 🔥 TURN OFF RELAY AFTER 5 SEC
            ser.write(b'L')

            busy = False

        cv2.imshow("Face Lock", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
        continue

    # 🔵 Scan every 2 sec
    if current_time - last_scan > scan_interval:

        if len(faces) > 0:
            (x,y,w,h) = faces[0]
            face = gray[y:y+h, x:x+w]

            label, confidence = model.predict(face)
            print("Confidence:", confidence)

            if confidence < 70:
                print("✅ AUTHORIZED")

                # Stop alarm + unlock
                ser.write(b'L')  
                ser.write(b'U')

                # 🔥 ENTER BUSY MODE (pause detection)
                busy = True
                busy_end_time = current_time + 5  # 5 seconds

            else:
                print("❌ UNAUTHORIZED")

                # Alarm only once per scan
                ser.write(b'A')

        else:
            print("No face")

        last_scan = current_time

    cv2.imshow("Face Lock", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()