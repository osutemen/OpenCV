import cv2

img = cv2.imread('images/ape.JPG')
img_gray = cv2.imread('images/ape.JPG', 0)


# Item
# img.item(y,x,clour)

print('Blue:', img.item(200,250,0))
print('Green:', img.item(200,250,1))
print('Red:', img.item(200,250,2))

print(img[200,250])


# Itemset
#img.itemset((y,x,clour),value)

img.itemset((10,10,0),0)

#itemset with loops
#
for y in range(50):
    for x in range(50):
        img.itemset((y, x, 0), 0)
        img.itemset((y, x, 0), 1)
        img.itemset((y, x, 0), 2)

# or

for y in range(50):
    for x in range(50):
        img[y, x] = [0,0,0]


# Shape
print(img.shape)


# Size
print(img.size)


# Datatype
print(img.dtype)

# ROI
#roi = img[y1:y2, x1:x2]
roi = img[50:100, 50:100]


#  Filter of clour
img[: , : ,0] = 0

cv2.imshow('monkey',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

