import cv2 as cv

# in this program we will draw line on image
# line(1st_arg, 2nd_arg, 3rd_arg, 4th_arg, 5th_arg)
# 1st_arg: on which image you want to draw line
# 2nd_arg: starting coordinates
# 3rd_arg: ending coordinates
# 4th_arg: color in RGB tuple of line
# 5th_arg: thickness of line

image = cv.imread("lena.jpg")

cv.line(image, (100, 5), (5,100), (230, 115, 186), 2)
cv.imshow("lined-image", image)

cv.waitKey(0)
cv.destroyAllWindows()