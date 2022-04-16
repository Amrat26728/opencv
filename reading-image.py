import cv2

image_path = r"lena.jpg"
# imread methos just read the image and put the data in the image variable
image = cv2.imread(image_path)
print(image)