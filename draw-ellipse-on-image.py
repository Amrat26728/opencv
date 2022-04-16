import cv2

image = cv2.imread("lena.jpg")

# ellipse(image, center-of-ellipse, axes-length, angle-of-ellipse, star-angle, end-angle, thickness)
cv2.ellipse(image, (100, 100), (100, 50), 0, 0, 360, -1)

cv2.imshow("image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()