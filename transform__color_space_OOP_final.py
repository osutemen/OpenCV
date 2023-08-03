"""
-------------------------------------------------------------------------------------------------------------
Transforming Color Spaces

After running the program for the color space you want to select, press the corresponding key on the keyboard.
You can refer to the list below. Also, press 'q' to exit.

Color Space Select

HLS --> s (also efault color space)
HSV --> v
LAB --> b
LUV --> u

-------------------------------------------------------------------------------------------------------------
"""

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
        # Create trackbars for the selected color space.
        if self.color_space == "HLS":
            cv2.createTrackbar('Hue Shift', 'Color Transformation', 0, 229, self.update_color_transform)
            cv2.createTrackbar('Saturation Scale', 'Color Transformation', 100, 200, self.update_color_transform)
            cv2.createTrackbar('Lightness Scale', 'Color Transformation', 100, 200, self.update_color_transform)

        elif self.color_space == "HSV":
            cv2.createTrackbar('Hue Shift', 'Color Transformation', 0, 229, self.update_color_transform)
            cv2.createTrackbar('Saturation Scale', 'Color Transformation', 100, 200, self.update_color_transform)
            cv2.createTrackbar('Value Scale', 'Color Transformation', 100, 200, self.update_color_transform)

        elif self.color_space == "LAB":
            cv2.createTrackbar('Lightness Scale', 'Color Transformation', 0, 179, self.update_color_transform)
            cv2.createTrackbar('Green-Red Axis', 'Color Transformation', 100, 200, self.update_color_transform)
            cv2.createTrackbar('Blue-Yellow Axis', 'Color Transformation', 100, 200, self.update_color_transform)

        elif self.color_space == "LUV":
            cv2.createTrackbar('Lightness Scale', 'Color Transformation', 0, 179, self.update_color_transform)
            cv2.createTrackbar('Red-GreenAxis', 'Color Transformation', 100, 200, self.update_color_transform)
            cv2.createTrackbar('Yellow-Blue Axis', 'Color Transformation', 100, 200, self.update_color_transform)

        # Call update_color_transform() to initialize the transformation with default values
        self.update_color_transform()

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
        if self.color_space in ["HLS", "HSV"]:
            hue_shift = cv2.getTrackbarPos('Hue Shift', 'Color Transformation')
            saturation_scale = cv2.getTrackbarPos('Saturation Scale', 'Color Transformation') / 100.0
            lightness_scale = cv2.getTrackbarPos('Lightness Scale', 'Color Transformation') / 100.0
        elif self.color_space == "LAB":
            lightness_scale = cv2.getTrackbarPos('Lightness Scale', 'Color Transformation') / 100.0
            green_red_axis = cv2.getTrackbarPos('Green-Red Axis', 'Color Transformation') / 100.0
            blue_yellow_axis = cv2.getTrackbarPos('Blue-Yellow Axis', 'Color Transformation') / 100.0
        elif self.color_space == "LUV":
            lightness_scale = cv2.getTrackbarPos('Lightness Scale', 'Color Transformation') / 100.0
            red_green_axis = cv2.getTrackbarPos('Red-GreenAxis', 'Color Transformation') / 100.0
            yellow_blue_axis = cv2.getTrackbarPos('Yellow-Blue Axis', 'Color Transformation') / 100.0

        # Apply the color transformation based on the color space
        if self.color_space in ["HLS", "HSV"]:
            image_hsv[:, :, 0] = (image_hsv[:, :, 0] + hue_shift) % 180
            image_hsv[:, :, 1] = np.clip(image_hsv[:, :, 1] * lightness_scale, 0, 255)
            image_hsv[:, :, 2] = np.clip(image_hsv[:, :, 2] * saturation_scale, 0, 255)
        elif self.color_space == "LAB":
            image_hsv[:, :, 0] = np.clip(image_hsv[:, :, 0] * lightness_scale, 0, 255)
            image_hsv[:, :, 1] = np.clip(image_hsv[:, :, 1] * green_red_axis, -128, 127)
            image_hsv[:, :, 2] = np.clip(image_hsv[:, :, 2] * blue_yellow_axis, -128, 127)
        elif self.color_space == "LUV":
            image_hsv[:, :, 0] = np.clip(image_hsv[:, :, 0] * lightness_scale, 0, 255)
            image_hsv[:, :, 1] = np.clip(image_hsv[:, :, 1] * red_green_axis, -134, 220)
            image_hsv[:, :, 2] = np.clip(image_hsv[:, :, 2] * yellow_blue_axis, -134, 220)

        # Convert the image back to the BGR color space
        if self.color_space in ["HLS", "HSV"]:
            self.transformed_image = cv2.cvtColor(image_hsv, cv2.COLOR_HLS2BGR)
        else:
            self.transformed_image = cv2.cvtColor(image_hsv, cv2.COLOR_LAB2BGR)

    def update_color_transform(self, _=None):
        self.apply_color_transform()

        # Display the transformed image and the original image side by side
        side_by_side = np.hstack((self.original_image, self.transformed_image))
        cv2.imshow('Color Transformation', side_by_side)

    def set_color_space(self, color_space):
        self.color_space = color_space
        self.create_trackbars()

        # Reset trackbar values based on the selected color space
        if self.color_space in ["HLS", "HSV"]:
            cv2.setTrackbarPos('Hue Shift', 'Color Transformation', 0)
            cv2.setTrackbarPos('Saturation Scale', 'Color Transformation', 100)
            cv2.setTrackbarPos('Lightness Scale', 'Color Transformation', 100)
        elif self.color_space == "LAB":
            cv2.setTrackbarPos('Lightness Scale', 'Color Transformation', 100)
            cv2.setTrackbarPos('Green-Red Axis', 'Color Transformation', 100)
            cv2.setTrackbarPos('Blue-Yellow Axis', 'Color Transformation', 100)
        elif self.color_space == "LUV":
            cv2.setTrackbarPos('Lightness Scale', 'Color Transformation', 100)
            cv2.setTrackbarPos('Red-GreenAxis', 'Color Transformation', 100)
            cv2.setTrackbarPos('Yellow-Blue Axis', 'Color Transformation', 100)

        # Update the color transformation with the default values
        self.update_color_transform()

    def run(self):
        while True:
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('s'):
                self.set_color_space("HLS")
            elif key == ord('v'):
                self.set_color_space("HSV")
            elif key == ord('b'):
                self.set_color_space("LAB")
            elif key == ord('u'):
                self.set_color_space("LUV")

        # Destroy all windows
        cv2.destroyAllWindows()

# Create an instance of the ColorTransformer class and run the program
transformer = ColorTransformer('images/kiwi.jpeg')
transformer.run()
