# Image Preprocessing Techniques

**Date:** 2026-06-26

## What is Image Preprocessing?

Image preprocessing prepares raw images for ML models or computer vision tasks — improving quality, reducing noise, and standardizing format.

```
Raw Image → Preprocessing → Clean, standardized image → Model
```

---

## Common Techniques

### Resizing
```python
import cv2

img = cv2.imread("photo.jpg")

# Resize to fixed dimensions
resized = cv2.resize(img, (224, 224))           # width, height

# Resize by scale factor
half = cv2.resize(img, None, fx=0.5, fy=0.5)   # 50% of original
```

### Grayscale Conversion
```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```

### Noise Removal
```python
# Gaussian blur — removes high frequency noise
blurred = cv2.GaussianBlur(img, (5, 5), 0)

# Median blur — good for salt-and-pepper noise
median = cv2.medianBlur(img, 5)
```

### Thresholding
```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Binary threshold
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Adaptive threshold — better for uneven lighting
adaptive = cv2.adaptiveThreshold(gray, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, 11, 2)
```

### Normalization
```python
import numpy as np

# Normalize to 0-1 range (for deep learning)
normalized = img.astype(np.float32) / 255.0

# Normalize to mean=0, std=1
mean = np.mean(img)
std = np.std(img)
standardized = (img - mean) / std
```

---

## Preprocessing Pipeline for Face Recognition

```python
import cv2
import face_recognition

def preprocess_for_recognition(image_path):
    # Load image
    img = cv2.imread(image_path)

    # Convert BGR to RGB (face_recognition uses RGB)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Resize for faster processing
    small = cv2.resize(rgb, None, fx=0.5, fy=0.5)

    return small
```

---

## What I Applied

Used resizing, BGR→RGB conversion, and normalization in my [MediCore AI Hospital System](https://github.com/adheethii/Medicore-AI-Hospital-System) — webcam frames are preprocessed before face encoding extraction.

---

## Key Takeaway

> Preprocessing directly impacts model accuracy. Always resize to consistent dimensions, convert color spaces correctly (OpenCV uses BGR, most ML libraries use RGB), and normalize pixel values to 0-1 for deep learning models.
