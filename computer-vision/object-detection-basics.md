# Object Detection Basics with OpenCV

**Date:** 2026-06-26

## What is Object Detection?

Object detection finds and locates objects in an image — answers both "what is it?" and "where is it?"

```
Image → Detection → Bounding boxes + Labels + Confidence scores
```

---

## Haar Cascade Classifier

OpenCV's built-in classical detector — fast, no GPU needed:

```python
import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

img = cv2.imread("photo.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(img, "Face", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
```

---

## Real-time Webcam Detection

```python
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    cv2.imshow("Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
```

---

## Key Takeaway

> Haar cascades are OpenCV's classical detectors — fast, no GPU, good for faces. detectMultiScale returns (x, y, width, height) bounding boxes. For better accuracy, use deep learning models like YOLO.
