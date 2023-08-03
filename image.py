import cv2

# Load the image
img = cv2.imread('images/ape.JPG', cv2.IMREAD_GRAYSCALE)

#
cv2.imshow('Monkey', img)

#
cv2.waitKey(0)
cv2.destroyAllWindows()



