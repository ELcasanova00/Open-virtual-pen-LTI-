# Open virtual pen LTI
Description

Virtual Pen is a simple computer vision project that allows users to draw on the screen using a colored object as a virtual pen. The program tracks the chosen color in real-time from a webcam feed and maps its movement onto a transparent canvas. This project is ideal for beginners learning OpenCV, image processing, and basic contour detection.


🛠 Features

Detect and track a specific color in real-time (default: blue, configurable).

Draw freely on a virtual canvas using the tracked object.

Visualize both the webcam feed and the drawing overlay.

Lightweight and easy to run on any modern system with Python.

🔧 Usage

Move a colored object (e.g., blue marker or pen) in front of the webcam.

The program will track its motion and draw corresponding strokes on the screen.

Press ESC to exit.

import cv2
import numpy as np

# Buka webcam
cap = cv2.VideoCapture(0)

# Canvas kosong untuk menggambar
canvas = np.zeros((480, 640, 3), dtype=np.uint8)

# Rentang warna biru (HSV)
lower = np.array([100, 120, 70])
upper = np.array([140, 255, 255])





