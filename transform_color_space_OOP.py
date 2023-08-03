import cv2
import numpy as np

class ColorTransformer:
    def __init__(self, image_path):
        self.original_image = cv2.imread(image_path)
        self.transformed_image = self.original_image.copy()
        self.color_space = "HLS"  # Default color space

        self.create_window()
        self.create_trackbars()
        self.update_color_transform()

    def create_window(self):
        cv2.namedWindow('Color Transformation')

    def create_trackbars(self):
        cv2.createTrackbar('Hue Shift', 'Color Transformation', 0, 179, self.update_color_transform)
        cv2.createTrackbar('Saturation Scale', 'Color Transformation', 100, 200, self.update_color_transform)
        cv2.createTrackbar('Lightness Scale', 'Color Transformation', 100, 200, self.update_color_transform)

    def apply_color_transform(self):
        # Convert the image to the selected color space
        if self.color_space == "HLS":
            image_hsv = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2HLS)
        elif self.color_space == "HSV":
            image_hsv = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2HSV)
        elif self.color_space == "LAB":
            image_hsv = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2LAB)
        elif self.color_space == "LUV":
            image_hsv = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2LUV)
        else:
            return

        # Get current trackbar values
        hue_shift = cv2.getTrackbarPos('Hue Shift', 'Color Transformation')
        saturation_scale = cv2.getTrackbarPos('Saturation Scale', 'Color Transformation') / 100.0
        lightness_scale = cv2.getTrackbarPos('Lightness Scale', 'Color Transformation') / 100.0

        # Apply the color transformation
        image_hsv[:, :, 0] = (image_hsv[:, :, 0] + hue_shift) % 180
        image_hsv[:, :, 1] = np.clip(image_hsv[:, :, 1] * lightness_scale, 0, 255)
        image_hsv[:, :, 2] = np.clip(image_hsv[:, :, 2] * saturation_scale, 0, 255)

        # Convert the image back to the BGR color space
        self.transformed_image = cv2.cvtColor(image_hsv, cv2.COLOR_HLS2BGR)

    def update_color_transform(self, _=None):
        self.apply_color_transform()

        # Display the transformed image and the original image side by side
        side_by_side = np.hstack((self.original_image, self.transformed_image))
        cv2.imshow('Color Transformation', side_by_side)

    def set_color_space(self, color_space):
        self.color_space = color_space
        self.update_color_transform()

    def run(self):
        while True:
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('h'):
                self.set_color_space("HLS")
            elif key == ord('v'):
                self.set_color_space("HSV")
            elif key == ord('l'):
                self.set_color_space("LAB")
            elif key == ord('u'):
                self.set_color_space("LUV")

        # Destroy all windows
        cv2.destroyAllWindows()


# Create an instance of the ColorTransformer class and run the program
transformer = ColorTransformer('images/background/3.jpg')
transformer.run()
