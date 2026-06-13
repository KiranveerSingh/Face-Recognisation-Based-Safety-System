import cv2
import numpy as np

faces = []

for i in range(5):
    img = cv2.imread(f"face_GURLEEN_{i}.jpg", 0)
    faces.append(img)

labels = np.array([0]*5)

model = cv2.face.LBPHFaceRecognizer_create()
model.train(faces, labels)

model.save("trainer.yml")

print("Training complete")