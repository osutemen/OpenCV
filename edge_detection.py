import cv2
import numpy as np

class EdgeDetector:
    def __init__(self, image_path):
        self.image_path = image_path
        self.img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    def _apply_gaussian_blur(self):
        # Apply Gaussian blur to reduce noise (optional but recommended)
        self.img_blurred = cv2.GaussianBlur(self.img, (5, 5), 0)

    def detect_edges_with_canny(self, low_threshold, high_threshold):
        # Apply Gaussian blur
        self._apply_gaussian_blur()

        # Perform edge detection using Canny edge detector
        edges = cv2.Canny(self.img_blurred, low_threshold, high_threshold)
        edges = np.clip(edges, 0, 255)

        return edges

    def detect_edges_with_sobel(self):
        # Apply Gaussian blur
        self._apply_gaussian_blur()

        # Perform edge detection using Sobel operator
        sobel_x = cv2.Sobel(self.img_blurred, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y = cv2.Sobel(self.img_blurred, cv2.CV_64F, 0, 1, ksize=3)

        # Calculate the magnitude of the gradient
        edges = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
        edges = np.clip(edges, 0, 255)

        return edges.astype(np.uint8)

    def detect_edges_with_laplacian(self):
        # Apply Gaussian blur
        self._apply_gaussian_blur()

        # Perform edge detection using Laplacian operator
        edges = cv2.Laplacian(self.img_blurred, cv2.CV_64F)
        edges = np.abs(edges)
        edges = np.clip(edges, 0, 255)

        return edges.astype(np.uint8)

if __name__ == "__main__":
    # Set the image file path
    image_path = 'images/face.jpg'

    # Create an instance of the EdgeDetector class
    edge_detector = EdgeDetector(image_path)

    # Perform edge detection with different algorithms
    canny_edges = edge_detector.detect_edges_with_canny(50, 150)
    sobel_edges = edge_detector.detect_edges_with_sobel()
    laplacian_edges = edge_detector.detect_edges_with_laplacian()


    # Display the original image and the edge-detected results
    cv2.imshow('Original Image', cv2.imread(image_path))
    cv2.imshow('Canny Edge Detection', canny_edges)
    cv2.imshow('Sobel Edge Detection', sobel_edges)
    cv2.imshow('Laplacian Edge Detection', laplacian_edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
