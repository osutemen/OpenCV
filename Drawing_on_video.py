#Drawing on Video

import cv2

cap = cv2.VideoCapture(0)

# Automatically grab width and height from video feed
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# coordinates for Rectangle
x = width//2
y = height//2

# Width and height

w = width//4
h= height//4

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Draw a rectangel on stream
    cv2.rectangle(frame, (x, y), (x+w, y+h), color=(0,0,255),thickness= 4)

    #Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
# When everyting is done, release the capture
cap.release()
cv2.destroyAllWindows()
