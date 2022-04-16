import cv2

# this program is to draw circle on image
# circle(1st_arg, 2nd_arg, 3rd_arg, 4th_arg, 5th_arg) method is used to draw circle on image.
# 1st_arg: image on which you want to draw circle.
# 2nd_arg: position of center of circle.
# 3rd_arg: radius of circle.
# 4th_arg: color in RGB tuple.
# 5th_arg: thickness of circle.

image = cv2.imread("lena.jpg")

cv2.circle(image, (200, 200), 200, (0, 0, 0), 2)
cv2.imshow("circled image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()