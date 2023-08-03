import cv2

class CannyEdgeDetector:
    def __init__(self, image_path):
        self.original = cv2.imread(image_path, 1)
        self.img = self.original.copy()
        self.img = cv2.GaussianBlur(self.img, (5, 5), 0)

        cv2.namedWindow('canny')
        cv2.createTrackbar('thresh1', 'canny', 0, 255, self.funcCan)
        cv2.createTrackbar('thresh2', 'canny', 0, 255, self.funcCan)
        self.funcCan(0)

        cv2.imshow('Frame', self.original)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    
    def funcCan(self, thresh1=0):
        self.thresh1 = cv2.getTrackbarPos('thresh1', 'canny')
        self.thresh2 = cv2.getTrackbarPos('thresh2', 'canny')
        edge = cv2.Canny(self.img, self.thresh1, self.thresh2)
        cv2.imshow('canny', edge)


if __name__ == '__main__':
    image_path = "images/face.jpg"
    edge_detector = CannyEdgeDetector(image_path)
