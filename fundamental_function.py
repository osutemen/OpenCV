import cv2

# Load the image
img = cv2.imread('images/face.jpg')

print(f"size of orginal image  {img.size}")
print(f"shape of orginal image  {img.shape}")
print("------------------------------------------")

# convert to Grag
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(f"size of gray image  {imgGray.size}")
print(f"shape of gray image  {imgGray.shape}")
print("------------------------------------------")

# Make to Blur
imgBlur = cv2.GaussianBlur(imgGray,(15,15),0)

print(f"size of blur image  {imgBlur.size}")
print(f"shape of blur image  {imgBlur.shape}")
print("------------------------------------------")

# Make to Canny
imgCanny = cv2.Canny(imgGray,150,150)

print(f"size of canny image  {imgCanny.size}")
print(f"shape of canny image  {imgCanny.shape}")
print("------------------------------------------")

# Crop the image
imgCropped = img[0:460,0:390]

print(f"size of canny image  {imgCropped.size}")
print(f"shape of canny image  {imgCropped.shape}")
print("------------------------------------------")


cv2.imshow('face', img)
cv2.imshow('gray of face', imgGray)
cv2.imshow('blur of face', imgBlur)
cv2.imshow('canny of face', imgCanny)
cv2.imshow('cropped face', imgCropped)


cv2.waitKey(0)
cv2.destroyAllWindows()