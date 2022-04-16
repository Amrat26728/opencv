import cv2

image = cv2.imread('lena.jpg')
# cv2.imshow('lena image', image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # imwrite() method is used to write the image.
# cv2.imwrite("lena-saved-image.png", image)
# print("Successfully saved image!")

# resolutiom = rows x columns
print(image.shape)  # output: (rows, columns, channels) channels means image contains 3 colors.