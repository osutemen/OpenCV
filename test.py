import cv2
import numpy as np

# Trackbar callback function
def update_thresholds(x):
    # Get current trackbar positions
    lower_hue = cv2.getTrackbarPos("Lower Hue", "Thresholded Image")
    lower_saturation = cv2.getTrackbarPos("Lower Saturation", "Thresholded Image")
    lower_lightness = cv2.getTrackbarPos("Lower Lightness", "Thresholded Image")
    upper_hue = cv2.getTrackbarPos("Upper Hue", "Thresholded Image")
    upper_saturation = cv2.getTrackbarPos("Upper Saturation", "Thresholded Image")
    upper_lightness = cv2.getTrackbarPos("Upper Lightness", "Thresholded Image")

    # Set lower and upper threshold values for HSL channels
    lower_threshold = (lower_hue, lower_saturation, lower_lightness)
    upper_threshold = (upper_hue, upper_saturation, upper_lightness)

    # Apply HSL color thresholding
    thresholded_image = hsl_color_threshold(original_image, lower_threshold, upper_threshold)

    # Display the original and thresholded images
    cv2.imshow("Original Image", original_image)
    cv2.imshow("Thresholded Image", thresholded_image)

# Function for HSL color thresholding
def hsl_color_threshold(image, lower_threshold, upper_threshold):
    # Convert image from BGR to HSL
    hsl_image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

    # Define lower and upper threshold arrays
    lower_array = np.array(lower_threshold, dtype=np.uint8)
    upper_array = np.array(upper_threshold, dtype=np.uint8)

    # Threshold the image based on the specified HSL ranges
    thresholded_image = cv2.inRange(hsl_image, lower_array, upper_array)

    return thresholded_image

# Load image
original_image = cv2.imread("images/at.png")

# Convert the original image to HSL
original_hsl_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HLS)

# Get the H, S, L values from the original image
h, s, l = cv2.split(original_hsl_image)

# Calculate the minimum and maximum values for each channel
min_hue = np.min(h)
min_saturation = np.min(s)
min_lightness = np.min(l)
max_hue = np.max(h)
max_saturation = np.max(s)
max_lightness = np.max(l)

# Set the initial lower and upper thresholds based on the original image values
initial_lower_threshold = (min_hue, min_saturation, min_lightness)
initial_upper_threshold = (max_hue, max_saturation, max_lightness)

# Create a window to display the original and thresholded images
cv2.namedWindow("Original Image")
cv2.namedWindow("Thresholded Image")

# Create trackbars for lower and upper thresholds
cv2.createTrackbar("Lower Hue", "Thresholded Image", initial_lower_threshold[0], 179, update_thresholds)
cv2.createTrackbar("Lower Saturation", "Thresholded Image", initial_lower_threshold[1], 255, update_thresholds)
cv2.createTrackbar("Lower Lightness", "Thresholded Image", initial_lower_threshold[2], 255, update_thresholds)
cv2.createTrackbar("Upper Hue", "Thresholded Image", initial_upper_threshold[0], 179, update_thresholds)
cv2.createTrackbar("Upper Saturation", "Thresholded Image", initial_upper_threshold[1], 255, update_thresholds)
cv2.createTrackbar("Upper Lightness", "Thresholded Image", initial_upper_threshold[2], 255, update_thresholds)

# Display the original image
cv2.imshow("Original Image", original_image)

# Initialize the thresholded image with default thresholds
thresholded_image = hsl_color_threshold(original_image, initial_lower_threshold, initial_upper_threshold)

# Display the initial thresholded image
cv2.imshow("Thresholded Image", thresholded_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
