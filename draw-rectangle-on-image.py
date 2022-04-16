import cv2

image = cv2.imread("lena.jpg")

cv2.rectangle(image, (20, 50), (100, 100), (0, 0, 0), 2)

cv2.imshow("image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()