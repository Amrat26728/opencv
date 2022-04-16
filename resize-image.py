import cv2

# if quality of the image is low and if we make its size high it will be blure.

image = cv2.imread("lena.jpg")

resized_image = cv2.resize(image, (800, 650))

cv2.imshow("original image", image)
cv2.imshow("resized image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()