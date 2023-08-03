import cv2

# Load the image
#
#img = cv2.imread('images/ape.JPG')
#print('orginal size', img.shape)
#
## The image  resize
#img_resized = cv2.resize(img, (150,150))
#
#cv2.imshow('resized', img_resized)
#
#cv2.imshow('orginal', img)
#
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#
## The image crop
#
#img_cropped = img [0:150, 0:150]
#
#cv2.imshow('cropped', img_cropped)
#
#cv2.waitKey(0)
#cv2.destroyAllWindows()

import numpy as np

##Some calculating for CV
#
#x = np.uint8([250])
#y = np.uint8([10])
#
#sum_1 = x+y
#sum_2 = cv2.add(x,y)
#
#print(f' sum of normal, {sum_1}')
#print(f' sum of CV2, {sum_2}')
#
#img_star = cv2.imread('star.jpg')
#img_face = cv2.imread('face.jpg')
#
## Sum as weight of images
#sum_weight = cv2.addWeighted(img_star,0.5,img_face,0.5,0)

# Calculating for bites

img_cv = cv2.imread('images/cv.png')
img_clours = cv2.imread('images/colors.png')

img_gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)

cv2.imshow('cv logo gray', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

