import cv2
import numpy as np

img2 = cv2.imread("images/final_kiwi.png")
print(img2.shape)

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

# Eşikleme işlemi
_, mask = cv2.threshold(blurred, 15, 255, cv2.THRESH_BINARY)


# Görüntüyü maskeleyin
masked_img = cv2.bitwise_and(img2, img2, mask=mask)

cv2.imshow("blurred", blurred)
cv2.imshow("img2gray", gray)
cv2.imshow("img2", img2)
cv2.imshow("mask", mask)
cv2.imshow("masked_img", masked_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
