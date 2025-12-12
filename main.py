import cv2
import numpy as np


lower_color = np.array([100, 150, 50])
upper_color = np.array([140, 255, 255])


cap = cv2.VideoCapture(0)


canvas = None


x_prev, y_prev = None, None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

   
    if canvas is None:
        canvas = np.zeros_like(frame)

    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

   
    mask = cv2.inRange(hsv, lower_color, upper_color)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    
    cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)

        if radius > 10:
            x, y = int(x), int(y)

            # Gambar garis jika ada titik sebelumnya
            if x_prev is not None and y_prev is not None:
                cv2.line(canvas, (x_prev, y_prev), (x, y), (255, 0, 0), 5)

            x_prev, y_prev = x, y

    else:
        # Reset jika warna hilang
        x_prev, y_prev = None, None

   
    output = cv2.add(frame, canvas)

    cv2.imshow("Virtual Pen", output)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)
    if key == ord('c'):   # clear canvas
        canvas = np.zeros_like(frame)
    if key == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()

