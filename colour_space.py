import cv2

img = cv2.imread('images/colors.png')

# image is converted from BGR to RGB
img0 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# image is converted from BGR to RGB
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# image is converted from BGR to HSV
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# image is converted from BGR to HSV
img3 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)

# image is converted from BGR to YUV
img4 = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)

# View the images
cv2.imshow('colour', img)
cv2.imshow('altered colours as GRAY', img0)
cv2.imshow('altered colours as RGB', img1)
cv2.imshow('altered colours as HSV', img2)
cv2.imshow('altered colours as HSV_FULL', img3)
cv2.imshow('altered colours as YUV', img4)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Example of BGR to HSV.
#P.S. don't forget to remove the comment !!
"""
In this example, we start by loading an image named "image.jpg". Then, we perform the BGR to HSV conversion on 
the image. We define a lower and upper color range for the blue color. These ranges are usually determined through 
trial and error and can vary depending on the specific color you're working with. Next, we use the cv2.inRange() 
function to filter pixels within the specified color range and create a mask that contains only the blue pixels. 
Finally, we display the filtered image on the screen.

In this example, we've defined the color ranges to detect blue objects. Similarly, by defining different color 
ranges for different colors, you can separate other objects as well.

"""
#import cv2
#import numpy as np
#
## Load the image
#img = cv2.imread("images/cats.jpg")
#
## Convert BGR to HSV
#hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
## Define the blue color range
#lower_blue = np.array([90, 50, 50])  # Lower color values (e.g., 90 for blue)
#upper_blue = np.array([130, 255, 255])  # Upper color values (e.g., 130 for blue)
#
## Filter blue pixels
#blue_mask = cv2.inRange(hsv_img, lower_blue, upper_blue)
#
## Show the filtered image
#cv2.imshow("Blue Objects", blue_mask)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#















