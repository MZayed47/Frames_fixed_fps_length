'''
Extract all frames according to default fps
'''

import os
import numpy as np
import cv2
from glob import glob


def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR: creating directory with name {path}")


def save_frame(video_path, save_dir, gap=1):
    name = video_path.split("/")[-1].split(".")[0]
    save_path = os.path.join(save_dir, name)
    create_dir(save_path)
    
    cap = cv2.VideoCapture(video_path)
    idx = 1
    
    while True:
        ret, frame = cap.read()

        if ret == False:
            cap.release()
            break

        if idx % gap == 0:
            filename = save_path + "_" + str(idx) + ".png"
            cv2.imwrite(filename, frame)

        idx += 1


if __name__ == "__main__":
    
    video_paths = glob("all_videos/*")
    
    save_dir = "frames"

    for path in video_paths:
        save_frame(path, save_dir, gap=1)

