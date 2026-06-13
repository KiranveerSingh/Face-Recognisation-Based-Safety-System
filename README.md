# Face Recognition Based Safety System

## Overview

This project is a Face Recognition Based Safety Locker System that uses Artificial Intelligence and Embedded Systems to provide secure and contactless access control.

Instead of using keys, passwords, or fingerprint sensors, the system identifies authorized users through facial recognition and automatically unlocks the locker.

The project combines Computer Vision, Machine Learning, Arduino, and Hardware Interfacing to create a smart security system.

---

## Features

- Real-time face detection using OpenCV
- Face recognition using LBPH algorithm
- Contactless authentication
- Automatic locker unlocking for authorized users
- Buzzer alert for unauthorized access
- Streamlit-based user interface
- Arduino-controlled relay and solenoid lock
- Automatic re-locking after a few seconds

---

## Technologies Used

### Software

- Python
- OpenCV
- Streamlit
- PySerial

### Hardware

- Arduino Uno
- Relay Module
- 12V Solenoid Lock
- Buzzer
- Laptop Camera
- 12V Power Adapter

---

## System Workflow

1. User clicks the Unlock button.
2. Camera starts capturing live video.
3. OpenCV detects the face.
4. LBPH model recognizes the user.
5. If the user is authorized:
   - Python sends "U" command to Arduino.
   - Relay activates.
   - Solenoid lock opens.
   - Locker remains unlocked for a few seconds.
   - Arduino receives "L" command and locks again.
6. If the user is not authorized:
   - Python sends "A" command.
   - Buzzer turns ON.

---

## Hardware Connections

| Component   | Arduino Pin |
| Relay IN    | D8          |
| Buzzer IN   | D9          |
| Relay VCC   | 5V          |
| Relay GND   | GND         |
| Buzzer VCC  | 5V          |
| Buzzer GND  | GND         |

---

## Project Structure

FACE-RECOGNISATION-BASED-SAFETY-SYSTEM/
│
├── CODE_IDE/
│   └── CODE_IDE.ino
│
├── CODE_PYTHON/
│   ├── app.py
│   ├── face_image_capture.py
│   ├── face_lock.py
│   ├── model_training.py
│   ├── trainer.yml
│   ├── .vscode/
│   └── faceenv/            (ignored via .gitignore)
│
├── Circuit-Diagram.png
├── DEMO_VIDEO_LINK.txt
├── Face_Recognisation_based_safety_locker_system.mp4  (ignored via .gitignore due to its large size)
├── How I made it.md
├── LICENSE
├── README.md
├── requirements.txt
└── .gitignore

---

## Applications

- Smart Lockers
- Home Security Systems
- Office Access Control
- Hostel Room Security
- Restricted Area Access

---

## Future Improvements

- Deep Learning based face recognition
- Mobile App Integration
- IoT-based remote monitoring
- Cloud database support
- Multi-factor authentication
- Access logs and analytics

---

## Author

Kiranveer Singh and Gurleen Kaur
