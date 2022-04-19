import cv2

image = cv2.imread("lena.jpg", 1)  # 0 for colored to gray and 1 for gray to colored and -1 for as it is.

cv2.imshow("image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()