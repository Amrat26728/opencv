import cv2

image_path = "lena.jpg"
# imread() method just read the image and put the data in the image variable
image = cv2.imread(image_path)
# to display image we have method imshow() which displays image with the given data
cv2.imshow("image window", image)
# waitkey() method waits for user to press any key 
cv2.waitKey(0)
cv2.destroyAllWindows()  # distroys all the windows after closing of image.