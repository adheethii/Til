# Color Detection with OpenCV

**Date:** 2026-06-30

## What is Color Detection?

Color detection identifies specific colors in an image or video frame using HSV color space — more reliable than RGB for color-based filtering.

```
Image → Convert to HSV → Create color mask → Apply mask → Detected region
```

---

## Why HSV Instead of RGB?

```
RGB: color depends on lighting → unreliable
HSV: separates color (Hue) from brightness → reliable ✅

H = Hue (color type: 0-179)
S = Saturation (color intensity: 0-255)
V = Value (brightness: 0-255)
```

---

## Color Detection Example

```python
import cv2
import numpy as np

img = cv2.imread("image.jpg")

# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define color range (green)
lower_green = np.array([40, 50, 50])
upper_green = np.array([80, 255, 255])

# Create mask
mask = cv2.inRange(hsv, lower_green, upper_green)

# Apply mask to original image
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Original", img)
cv2.imshow("Mask", mask)
cv2.imshow("Detected Color", result)
cv2.waitKey(0)
```

---

## Common HSV Color Ranges

| Color | Lower HSV | Upper HSV |
|-------|-----------|-----------|
| Red | [0, 50, 50] | [10, 255, 255] |
| Green | [40, 50, 50] | [80, 255, 255] |
| Blue | [100, 50, 50] | [130, 255, 255] |
| Yellow | [20, 50, 50] | [40, 255, 255] |
| Orange | [10, 50, 50] | [20, 255, 255] |

---

## Real-time Color Detection from Webcam

```python
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Detect blue color
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Find contours of detected color
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt) > 500:    # ignore small noise
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame, "Blue Object", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    cv2.imshow("Color Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

---

## Key Takeaway

> Always use HSV for color detection — never RGB. HSV separates color (Hue) from lighting (Value), making detection robust to shadows and brightness changes. Use cv2.inRange() to create a binary mask, then find contours to locate objects.
