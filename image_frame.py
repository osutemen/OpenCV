import cv2
import matplotlib.pyplot as plt

# Load the image

img = cv2.imread('images/ape.JPG')

# BORDER_REPLICATE
replicate = cv2.copyMakeBorder(img,10,10,10,10, cv2.BORDER_REPLICATE)

# BORDER_REFLECT
reflect = cv2.copyMakeBorder(img,10,10,10,10, cv2.BORDER_REFLECT)

# BORDER_REFLECT_101
reflect_101 = cv2.copyMakeBorder(img,10,10,10,10, cv2.BORDER_REFLECT_101)

# BORDER_WRAP
wrap = cv2.copyMakeBorder(img,10,10,10,10, cv2.BORDER_WRAP)

# BORDER_CONSTANT
greenclour = [0,255,0]
constant = cv2.copyMakeBorder(img,10,10,10,10, cv2.BORDER_CONSTANT, value = greenclour)


#cv2.imshow('main',img)
#cv2.imshow('replicate',replicate)
##cv2.imshow('main',img)
##cv2.imshow('main',img)
#
#cv2.waitKey(0)
#cv2.destroyAllWindows()

plt.subplot(2, 3, 1), plt.imshow(img), plt.title('orjinal')
plt.subplot(2, 3, 2), plt.imshow(replicate), plt.title('replicate')
plt.subplot(2, 3, 3), plt.imshow(reflect), plt.title('reflect')
plt.subplot(2, 3, 4), plt.imshow(reflect_101), plt.title('reflect_101')
plt.subplot(2, 3, 5), plt.imshow(wrap), plt.title('wrap')
plt.subplot(2, 3, 6), plt.imshow(constant), plt.title('constant')


plt.show()