import cv2 as cv

# in this program we are writting some text on image.
# putText(1st_arg, 2nd_arg, 3rd_arg, 4th_arg, 5th_arg, 6th_arg, 7th_arg) method is used to put text on image 
# 1st_arg: it displays the output image after putting text.
# 2nd_arg: text that you want to put on image.
# 3rd_arg: position where on image you want to put that text.
# 4th_arg: what font style you want to put.
# 5th_arg: size of the font.
# 6th_arg: color in RGB tuple.
# 7th_arg: thickness of the font (only integer values).

image = cv.imread("lena.jpg")

text_image = cv.putText(image, "Girl", (0, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 3)
cv.imshow("Texted image", text_image)
cv.waitKey(0)
cv.destroyAllWindows()