# OpenCV Image Processing Basics

**Date:** 2026-06-25

## What is OpenCV?

OpenCV (Open Source Computer Vision Library) is the most popular Python library for image and video processing — used in face recognition, object detection, and computer vision projects.

---

## Installation

```bash
pip install opencv-python
```

---

## Reading and Displaying Images

```python
import cv2

# Read image
img = cv2.imread("photo.jpg")

# Display
cv2.imshow("Image", img)
cv2.waitKey(0)          # wait for keypress
cv2.destroyAllWindows()

# Image shape
print(img.shape)        # (height, width, channels) e.g. (480, 640, 3)
```

---

## Color Spaces

```python
# BGR (default in OpenCV) → RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# BGR → Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# BGR → HSV (useful for color detection)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
```

---

## Basic Operations

```python
import cv2
import numpy as np

img = cv2.imread("photo.jpg")

# Resize
resized = cv2.resize(img, (300, 300))

# Crop
cropped = img[100:300, 50:250]    # [y1:y2, x1:x2]

# Flip
flipped = cv2.flip(img, 1)        # 1=horizontal, 0=vertical

# Draw rectangle
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 2)

# Draw text
cv2.putText(img, "Hello", (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
```

---

## Webcam Capture

```python
import cv2

cap = cv2.VideoCapture(0)    # 0 = default webcam

while True:
    ret, frame = cap.read()  # read frame
    if not ret:
        break

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # press Q to quit
        break

cap.release()
cv2.destroyAllWindows()
```

---

## What I Used It For

Used OpenCV in my [MediCore AI Hospital System](https://github.com/adheethii/Medicore-AI-Hospital-System) — capturing live webcam frames, converting to RGB for face_recognition library, and drawing patient name overlays on detected faces.

---

## Key Takeaway

> OpenCV reads images in BGR (not RGB) — always convert when using with other libraries. `cv2.imread()` reads, `cv2.imshow()` displays, `cv2.VideoCapture(0)` opens webcam. It's the foundation of any computer vision project in Python.
