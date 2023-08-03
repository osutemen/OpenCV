import cv2 as cv

def nothing(x):
    pass

# Load the image
image_path = "images/result.jpeg"
img = cv.imread(image_path)


# Create a window for trackbars
cv.namedWindow('Adjust Colors')

# Create trackbars for each color channel
cv.createTrackbar('B', 'Adjust Colors', 0, 255, nothing)
cv.createTrackbar('G', 'Adjust Colors', 0, 255, nothing)
cv.createTrackbar('R', 'Adjust Colors', 0, 255, nothing)

while True:
    # Get current trackbar positions
    b_value = cv.getTrackbarPos('B', 'Adjust Colors')
    g_value = cv.getTrackbarPos('G', 'Adjust Colors')
    r_value = cv.getTrackbarPos('R', 'Adjust Colors')

    # Apply the adjusted values to each color channel
    adjusted_img = img.copy()
    adjusted_img[:, :, 0] += b_value  # Blue channel
    adjusted_img[:, :, 1] += g_value  # Green channel
    adjusted_img[:, :, 2] += r_value  # Red channel

    # Display the adjusted image
    cv.imshow('Adjusted Image', adjusted_img)

    # Wait for key press
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv.destroyAllWindows()
