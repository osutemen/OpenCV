import cv2
import numpy as np

# nothing function
def nothing(x):
    pass

# Read the input image
input_image = cv2.imread('images/hsl_kiwi.jpg')  # Replace 'path/to/your/image.jpg' with the actual path of your image

# Create a trackbar for HSV color space
cv2.namedWindow("Trackbars")
cv2.createTrackbar("Hue Min", "Trackbars", 0, 279, nothing)
cv2.createTrackbar("Hue Max", "Trackbars", 279, 279, nothing)
cv2.createTrackbar("Saturation Min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Saturation Max", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("Value Min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Value Max", "Trackbars", 255, 255, nothing)

while True:
    frame_hsv = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)

    # Get the values from the trackbars
    hue_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    hue_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    sat_min = cv2.getTrackbarPos("Saturation Min", "Trackbars")
    sat_max = cv2.getTrackbarPos("Saturation Max", "Trackbars")
    val_min = cv2.getTrackbarPos("Value Min", "Trackbars")
    val_max = cv2.getTrackbarPos("Value Max", "Trackbars")

    # Perform masking based on the HSV color range
    lower_hsv = np.array([hue_min, sat_min, val_min])
    upper_hsv = np.array([hue_max, sat_max, val_max])
    mask = cv2.inRange(frame_hsv, lower_hsv, upper_hsv)

    # Apply the masking
    result = cv2.bitwise_and(input_image, input_image, mask=mask)

    # Display the images side by side
    side_by_side = np.hstack((input_image, result))
    cv2.imshow('Trackbars', side_by_side)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Save the resulting image
#cv2.imwrite('images/resultkiwi.jpeg', result)

# Destroy the window
cv2.destroyAllWindows()
