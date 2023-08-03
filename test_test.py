import cv2
import numpy as np

def apply_LoG_filter(image_path, kernel_size=(5, 5), ddepth=cv2.CV_64F):
    # Load the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply Gaussian blur
    img_blurred = cv2.GaussianBlur(img, kernel_size, 0)

    # Apply Laplacian of Gaussian (LoG) operator
    laplacian = cv2.Laplacian(img_blurred, ddepth, ksize=kernel_size[1])

    return laplacian

if __name__ == "__main__":
    # Set the image file path
    image_path = 'images/face.jpg'

    # Define the parameters for LoG filter
    kernel_size = (5, 5)  # Gaussian blur kernel size, should be an odd integer tuple (e.g., (3, 3), (5, 5), etc.)
    ddepth = cv2.CV_64F   # Output image depth, use cv2.CV_64F for float64 or cv2.CV_8U for uint8

    # Apply LoG filter to the image
    filtered_image = apply_LoG_filter(image_path, kernel_size=kernel_size, ddepth=ddepth)

    # Display the original image and the filtered result
    cv2.imshow('Original Image', cv2.imread(image_path))
    cv2.imshow('LoG Filtered Image', filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
