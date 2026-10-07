import cv2
image = cv2.imread("data/test.jpg")
cv2.imshow("FixMyArea Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()