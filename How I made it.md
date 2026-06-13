# How I Made This Project

## Project Idea

The main goal of this project was to create a secure locker system that does not require keys, passwords, or fingerprint sensors.

I wanted to build a contactless security system that could recognize a person's face and automatically unlock a locker.

---

## Step 1: Understanding Face Recognition

Before building the project, I learned:

- Python programming
- OpenCV
- Image processing
- Face detection
- Face recognition techniques
- Arduino communication

After researching different methods, I selected the LBPH (Local Binary Pattern Histogram) algorithm because it is simple, lightweight, and works well on normal computers.

---

## Step 2: Collecting Face Images

I created a Python script called:

face_image_capture.py

This program:

- Opens the webcam
- Detects the face
- Captures multiple face images
- Stores them for training

These images are used to train the face recognition model.

---

## Step 3: Training the Face Recognition Model

After collecting face images:

1. Images were converted to grayscale.
2. Face regions were extracted.
3. LBPH model was trained using OpenCV.
4. Trained model was saved for future recognition.

This model acts as the system's database of authorized users.

---

## Step 4: Building Face Recognition Logic

I created:

face_lock.py

This file:

- Opens the webcam
- Detects faces using Haar Cascade Classifier
- Recognizes users using the trained LBPH model
- Checks whether the detected face belongs to an authorized user

If authorized:

- Send Unlock command

If unauthorized:

- Send Alert command

---

## Step 5: Arduino Integration

I used an Arduino Uno as the hardware controller.

The Arduino receives commands from Python through USB serial communication.

Commands used:

'U' = Unlock

'L' = Lock

'A' = Alarm

The Arduino controls:

- Relay Module
- Solenoid Lock
- Buzzer

---

## Step 6: Relay and Solenoid Lock

A 12V solenoid lock requires more current than Arduino can provide.

To solve this:

- Arduino controls a relay.
- Relay controls the 12V power supply.
- Solenoid lock receives power only when authorized.

This allows safe operation of the lock.

---

## Step 7: Adding Security Alerts

To improve security:

- A buzzer was connected to Arduino.
- Unauthorized users trigger the buzzer.
- Authorized users keep the buzzer OFF.

This provides an immediate alert during unauthorized access attempts.

---

## Step 8: Creating User Interface

I used Streamlit to build a simple graphical interface.

The interface displays:

- Unlock button
- Authorized status
- Unauthorized status
- Locked status
- System messages

This makes the project easy to use without running multiple commands.

---

## Step 9: Testing

The project was tested in different situations:

### Authorized User
Result: Locker unlocked successfully.

### Unauthorized User
Result: Buzzer activated.

### No Face Detected
Result: No action taken.

### Auto Lock
Result: Locker automatically locked after a few seconds.

---

## Challenges Faced

### Lighting Conditions

Face recognition accuracy decreased in poor lighting.

Solution:
- Improved room lighting.
- Adjusted camera position.

### Serial Communication

Communication between Python and Arduino occasionally failed.

Solution:
- Proper COM port configuration.
- Added delays where necessary.

### Solenoid Power Requirements

Arduino could not directly drive the solenoid.

Solution:
- Used relay module and external 12V adapter.

---

## Results

- Face recognition accuracy: approximately 90-95%
- Response time: approximately 1-2 seconds
- Successful hardware integration
- Reliable locking and unlocking operation

---

## Skills Learned

Through this project, I gained experience in:

- Python Programming
- OpenCV
- Machine Learning Basics
- Computer Vision
- Streamlit
- Arduino Programming
- Serial Communication
- Hardware Interfacing
- Embedded Systems
- System Integration

---

## Conclusion

This project successfully demonstrates how Artificial Intelligence, Computer Vision, and Embedded Systems can be combined to create a modern and contactless security system.

It provides a practical and low-cost solution for smart lockers and access control applications.