# Face Recognition Deep Dive

**Date:** 2026-06-27

## How face_recognition Library Works

The `face_recognition` library wraps dlib's deep learning models to make face recognition simple in Python.

```
Image → Detect faces → Extract 128-dim encoding → Compare encodings → Match
```

---

## Installation

```bash
pip install face-recognition
pip install cmake dlib  # required dependencies
```

---

## Core Functions

```python
import face_recognition
import numpy as np

# Load image
image = face_recognition.load_image_file("person.jpg")

# Find face locations in image
locations = face_recognition.face_locations(image)
# → [(top, right, bottom, left), ...]

# Get 128-dimension face encodings
encodings = face_recognition.face_encodings(image)
# → [array of 128 floats]

# Compare two faces
results = face_recognition.compare_faces(
    [known_encoding],
    unknown_encoding,
    tolerance=0.6      # lower = stricter
)
# → [True] or [False]

# Get distance (lower = more similar)
distance = face_recognition.face_distance([known_encoding], unknown_encoding)
# → [0.42] — below 0.6 = same person
```

---

## Full Registration + Recognition Pipeline

```python
import face_recognition
import cv2
import pickle

def register_face(name, image_path):
    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)
    if not encodings:
        return "No face found"
    encoding = encodings[0]
    # Save encoding
    with open(f"{name}_encoding.pkl", "wb") as f:
        pickle.dump(encoding, f)
    return "Registered successfully"

def recognize_from_webcam(known_encodings, known_names):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        locations = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, locations)

        for encoding, location in zip(encodings, locations):
            matches = face_recognition.compare_faces(known_encodings, encoding)
            name = "Unknown"
            if True in matches:
                idx = matches.index(True)
                name = known_names[idx]

            top, right, bottom, left = location
            cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
            cv2.putText(frame, name, (left, top-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

        cv2.imshow("Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
```

---

## Tolerance Tuning

| Tolerance | Behaviour |
|-----------|-----------|
| 0.4 | Very strict — fewer false positives |
| 0.6 | Default — balanced |
| 0.8 | Lenient — more false positives |

---

## What I Built

This exact pipeline powers my [MediCore AI Hospital System](https://github.com/adheethii/Medicore-AI-Hospital-System) — patients register with a photo, and on each visit the webcam recognizes their face and auto-fills their details.

---

## Key Takeaway

> face_recognition uses 128-dimension embeddings — closer vectors = same person. Tolerance 0.6 is the sweet spot. Always convert BGR→RGB before passing to face_recognition. Save encodings to disk so you don't re-encode on every run.
