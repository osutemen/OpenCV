import cv2
import numpy as np

# Create function based on CV2 Event( left button click)

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(250,250,250),-1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),10,(250,250,250),-1)



# Create a black image
img = cv2.imread('images/wb_kiwi.png')
cv2.namedWindow(winname='my_drawing')
# Connects the mouse button to our callback function
cv2.setMouseCallback('my_drawing',draw_circle)

while True:
    cv2.imshow('my_drawing',img)

    if cv2.waitKey(20) & 0xFF ==27:
        break

cv2.destroyAllWindows()



