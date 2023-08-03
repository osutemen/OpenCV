import cv2
import numpy as np


def apply_hsl_transform(image, hue_shift, saturation_scale, lightness_scale):
    # Convert the image to the HSL color space
    hsl_image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

    # Apply the HSL transformation
    hsl_image[:, :, 0] = (hsl_image[:, :, 0] + hue_shift) % 180
    hsl_image[:, :, 1] = np.clip(hsl_image[:, :, 1] * lightness_scale, 0, 255)
    hsl_image[:, :, 2] = np.clip(hsl_image[:, :, 2] * saturation_scale, 0, 255)

    # Convert the image back to the BGR color space
    result_image = cv2.cvtColor(hsl_image, cv2.COLOR_HLS2BGR)

    return result_image


def update_hsl_transform(_):
    # Get current trackbar values
    hue_shift = cv2.getTrackbarPos('Hue Shift', 'HSL Transformation')
    saturation_scale = cv2.getTrackbarPos('Saturation Scale', 'HSL Transformation') / 100.0
    lightness_scale = cv2.getTrackbarPos('Lightness Scale', 'HSL Transformation') / 100.0

    # Apply the HSL transformation to the image
    transformed_image = apply_hsl_transform(original_image.copy(), hue_shift, saturation_scale, lightness_scale)

    # Display the transformed image and the original image side by side
    side_by_side = np.hstack((original_image, transformed_image))
    cv2.imshow('HSL Transformation', side_by_side)


# Load the image
original_image = cv2.imread('images/background/lazer.jpg')

# Create a window to display the transformed image
cv2.namedWindow('HSL Transformation')

# Create trackbars for HSL parameters
cv2.createTrackbar('Hue Shift', 'HSL Transformation', 0, 179, update_hsl_transform)
cv2.createTrackbar('Saturation Scale', 'HSL Transformation', 100, 200, update_hsl_transform)
cv2.createTrackbar('Lightness Scale', 'HSL Transformation', 100, 200, update_hsl_transform)
    
# Initialize the HSL transformation
update_hsl_transform(0)

# Wait for the user to press 'q' to exit
while cv2.waitKey(1) & 0xFF != ord('q'):
    pass

# Destroy all windows
cv2.destroyAllWindows()
