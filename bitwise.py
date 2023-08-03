import cv2
import numpy as np

class BitwiseOperations:
    def __init__(self, image1_path, image2_path):
        self.image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
        self.image2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)
        self.mask1 = None
        self.mask2 = None

    # ... (rest of the class methods remain the same)

def main():
    # Take input for image paths
    image1_path = input("Enter the path of the first image: ")
    image2_path = input("Enter the path of the second image: ")

    bit_ops = BitwiseOperations(image1_path, image2_path)

    # ... (rest of the main function remains the same)

if __name__ == "__main__":
    main()
