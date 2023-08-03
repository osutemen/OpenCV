import cv2
import numpy as np

# Load the image
img = cv2.imread('images/cat.jpg')

# Split the image into RGB channels
blue, green, red = cv2.split(img)

print(blue)
print(green)
print(red)

# Modify the pixel values of the channels
blue = np.zeros_like(blue)  # Set all blue channel values to 0
green = 125 * np.ones_like(green, dtype=np.uint8)  # Set all green channel values to 125
red = (red * 0.5).astype(np.uint8)  # Multiply all red channel values by 0.5


# Merge the modified channels back into an image
modified_image = cv2.merge((blue, green, red))

cv2.imshow('modified image ', modified_image )

cv2.waitKey(0)
cv2.destroyAllWindows()

