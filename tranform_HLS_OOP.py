
import cv2
import numpy as np

class HSLTransformer:
    def __init__(self, image_path):
        self.original_image = cv2.imread(image_path)
        self.transformed_image = self.original_image.copy()

        self.create_window()
        self.create_trackbars()
        self.update_hsl_transform()

    def create_window(self):
        cv2.namedWindow('HSL Transformation')

    def create_trackbars(self):
        cv2.createTrackbar('Hue Shift', 'HSL Transformation', 0, 179, self.update_hsl_transform)
        cv2.createTrackbar('Saturation Scale', 'HSL Transformation', 100, 200, self.update_hsl_transform)
        cv2.createTrackbar('Lightness Scale', 'HSL Transformation', 100, 200, self.update_hsl_transform)

    def apply_hsl_transform(self):
        # Convert the image to the HSL color space
        hsl_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2HLS)

        # Get current trackbar values
        hue_shift = cv2.getTrackbarPos('Hue Shift', 'HSL Transformation')
        saturation_scale = cv2.getTrackbarPos('Saturation Scale', 'HSL Transformation') / 100.0
        lightness_scale = cv2.getTrackbarPos('Lightness Scale', 'HSL Transformation') / 100.0

        # Apply the HSL transformation
        hsl_image[:, :, 0] = (hsl_image[:, :, 0] + hue_shift) % 180
        hsl_image[:, :, 1] = np.clip(hsl_image[:, :, 1] * lightness_scale, 0, 255)
        hsl_image[:, :, 2] = np.clip(hsl_image[:, :, 2] * saturation_scale, 0, 255)

        # Convert the image back to the BGR color space
        self.transformed_image = cv2.cvtColor(hsl_image, cv2.COLOR_HLS2BGR)

    def update_hsl_transform(self, _=None):
        self.apply_hsl_transform()

        # Display the transformed image and the original image side by side
        side_by_side = np.hstack((self.original_image, self.transformed_image))
        cv2.imshow('HSL Transformation', side_by_side)

    def run(self):
        while True:
            # Wait for the user to press 'q' to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Destroy all windows
        cv2.destroyAllWindows()


# Create an instance of the HSLTransformer class and run the program
transformer = HSLTransformer('images/result.jpeg')
transformer.run()

