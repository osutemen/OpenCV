import numpy as np
import cv2 as cv

def nothing(x):
    pass

# Load the image
image_path = "images/colors.png"
img = cv.imread(image_path)


# Convert the image to HSV color space
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Create a window for trackbars
cv.namedWindow('Adjust Colors')

# Create trackbars for each HSV channel
cv.createTrackbar('Hue', 'Adjust Colors', 0, 179, nothing)
cv.createTrackbar('Saturation', 'Adjust Colors', 0, 255, nothing)
cv.createTrackbar('Value', 'Adjust Colors', 0, 255, nothing)

while True:
    # Get current trackbar positions
    hue_value = cv.getTrackbarPos('Hue', 'Adjust Colors')
    saturation_value = cv.getTrackbarPos('Saturation', 'Adjust Colors')
    value_value = cv.getTrackbarPos('Value', 'Adjust Colors')

    # Apply the adjusted values to the HSV image
    adjusted_img = hsv_img.copy()
    adjusted_img[:, :, 0] += hue_value  # Hue channel
    adjusted_img[:, :, 1] += saturation_value  # Saturation channel
    adjusted_img[:, :, 2] += value_value  # Value channel

    # Convert the adjusted image back to BGR color space
    adjusted_img_bgr = cv.cvtColor(adjusted_img, cv.COLOR_HSV2BGR)

    # Display the adjusted image
    cv.imshow('Adjusted Image', adjusted_img_bgr)

    # Wait for key press
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv.destroyAllWindows()
