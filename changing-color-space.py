import cv2

image = cv2.imread("lena.jpg")
black_and_white_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("black_and_white_image", black_and_white_image)
cv2.waitKey(0)
cv2.destroyAllWindows()