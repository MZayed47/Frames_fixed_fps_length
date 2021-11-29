import cv2

cap = cv2.VideoCapture("/media/zayed/UbuntuWorks/videos/video03.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)

print(fps)
