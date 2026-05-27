# How Face Recognition Works (Python `face_recognition` Library)

**Date:** 2026-05-27

## Overview

Face recognition is the process of identifying a person from an image or video by comparing facial features against known faces.

## How It Works (Step by Step)

```
Input Image
    ↓
1. DETECT — Find face locations in the image (HOG or CNN model)
    ↓
2. ALIGN — Normalize the face (rotation, scale)
    ↓
3. ENCODE — Convert face to a 128-dimension vector (face embedding)
    ↓
4. COMPARE — Calculate distance between embeddings
    ↓
5. MATCH — If distance < tolerance → same person
    ↓
Result: Known / Unknown
```

## Key Functions in Python

```python
import face_recognition

# Load and encode a known face
known_image = face_recognition.load_image_file("adheethi.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

# Load unknown image and encode
unknown_image = face_recognition.load_image_file("unknown.jpg")
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

# Compare
results = face_recognition.compare_faces([known_encoding], unknown_encoding, tolerance=0.6)
# True = match, False = no match
```

## Tolerance Value

| Tolerance | Behaviour |
|-----------|-----------|
| `0.4` | Very strict — fewer false positives |
| `0.6` | Default — balanced accuracy |
| `0.8` | Lenient — more false positives |

## What I Built

Used this in [MediCore AI Hospital System](https://github.com/adheethii/Medicore-AI-Hospital-System) — patients are registered with their photo, and on each visit the system recognizes their face via webcam and auto-fills their details.

## Key Takeaway

> Face recognition works by comparing 128-point facial embeddings. The lower the distance between two encodings, the more similar the faces. Tolerance controls how strict the match is.
