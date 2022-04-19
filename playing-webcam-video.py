import cv2

# video = cv2.VideoCapture("D:\OpenCV Practice/video.mp4")
video = cv2.VideoCapture(0)

while True:

     ret, frame = video.read()
     cv2.imshow("Video", frame)
     if cv2.waitKey(1) & 0xFF == ord("q"):  # if cv2.waitKey(1) == ord('q')
          break
video.release()
cv2.destroyAllWindows()