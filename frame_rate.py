import cv2

cap = cv2.VideoCapture("/media/opus-bot-team/Ubuntu Works/OpusTech_Ubuntu/action_labeled_dataset/aim_train_zayed/Counter-Strike_ Global Offensive 2021-11-23 13-58-33.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)

print(fps)
