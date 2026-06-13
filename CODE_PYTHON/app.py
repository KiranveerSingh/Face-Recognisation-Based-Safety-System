import streamlit as st
import cv2
import serial
import time

# ---------------- SESSION STATE ----------------
if "running" not in st.session_state:
    st.session_state.running = False

if "status" not in st.session_state:
    st.session_state.status = "Idle"

if "ser" not in st.session_state:
    st.session_state.ser = None

if "unlock_time" not in st.session_state:
    st.session_state.unlock_time = None

if "cap" not in st.session_state:
    st.session_state.cap = None

if "last_check" not in st.session_state:
    st.session_state.last_check = 0

if "alarm_time" not in st.session_state:
    st.session_state.alarm_time = None

# ---------------- LOAD MODEL ----------------
model = cv2.face.LBPHFaceRecognizer_create()
model.read("trainer.yml")

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# ---------------- UI ----------------
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>🔐 Face Recognition Door Lock</h1>",
    unsafe_allow_html=True
)

st.markdown("---")
st.write("### Status:", st.session_state.status)

frame_placeholder = st.empty()

# ---------------- BUTTON ----------------
if st.button("Unlock"):
    if not st.session_state.running:

        st.session_state.running = True
        st.session_state.status = "Starting..."

        if st.session_state.ser is None:
            try:
                st.session_state.ser = serial.Serial('COM3', 9600)
                time.sleep(2)
            except:
                st.error("❌ COM3 busy. Close Arduino IDE.")
                st.stop()

# ---------------- CAMERA INIT ----------------
if st.session_state.running and st.session_state.cap is None:
    st.session_state.cap = cv2.VideoCapture(0)
    time.sleep(1)

# ---------------- DETECTION ----------------
if st.session_state.running and st.session_state.cap:

    cap = st.session_state.cap

    if not cap.isOpened():
        st.session_state.status = "Camera Error ❌"

    else:
        ret, frame = cap.read()

        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            # Draw face boxes
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

            current_time = time.time()

            # ---------------- UNLOCK TIMER ----------------
            if st.session_state.unlock_time:

                if current_time - st.session_state.unlock_time > 5:

                    if st.session_state.ser:
                        st.session_state.ser.write(b'L')  # lock

                    st.session_state.running = False
                    st.session_state.unlock_time = None
                    st.session_state.status = "Locked 🔒"

                    # Release camera (LED OFF)
                    if st.session_state.cap:
                        st.session_state.cap.release()
                        st.session_state.cap = None

                    # Release COM port
                    if st.session_state.ser:
                        st.session_state.ser.close()
                        st.session_state.ser = None

                    # Clear UI
                    frame_placeholder.empty()

                    st.rerun()

                else:
                    st.session_state.status = "Unlocked 🔓"

            # ---------------- CONTROLLED DETECTION ----------------
            else:

                # Detect only every 2 seconds
                if current_time - st.session_state.last_check > 2:

                    st.session_state.last_check = current_time

                    if len(faces) > 0:
                        (x,y,w,h) = faces[0]
                        face = gray[y:y+h, x:x+w]

                        label, confidence = model.predict(face)

                        if confidence < 70:
                            st.session_state.status = "AUTHORIZED ✅"

                            if st.session_state.ser:
                                st.session_state.ser.write(b'L')  # stop buzzer
                                st.session_state.ser.write(b'U')  # unlock

                            st.session_state.unlock_time = time.time()

                        else:
                            st.session_state.status = "UNAUTHORIZED ❌"

                            if st.session_state.ser:
                                st.session_state.ser.write(b'A')  # buzzer ON

                            st.session_state.alarm_time = time.time()

                    else:
                        st.session_state.status = "No Face"

                # Stop buzzer after 1 sec
                if st.session_state.alarm_time:
                    if current_time - st.session_state.alarm_time > 1:
                        if st.session_state.ser:
                            st.session_state.ser.write(b'L')  # buzzer OFF
                        st.session_state.alarm_time = None

            # Overlay status
            cv2.putText(
                frame,
                st.session_state.status,
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            frame_placeholder.image(frame, channels="BGR")

# ---------------- CONTROLLED LOOP ----------------
if st.session_state.running:
    time.sleep(0.08)
    st.rerun()

st.info("Click 'Unlock' to start detection")