import os
import mediapipe as mp
import cv2
from cvzone.HandTrackingModule import HandDetector
import math
import numpy as np

detector = HandDetector(maxHands=1)
imgSize = 300
offset = 20
DATA_DIR = './data'
TRAIN_DATA = './train_data'

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3, max_num_hands=1)


for dir_ in os.listdir(DATA_DIR):
    counter = 0
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        print(f'{dir_, img_path}')
        image = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        hands, img = detector.findHands(image)
        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox']
            imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
            imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
            imgCropShape = imgCrop.shape
            aspectRatio = h / w
            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                imgResizeShape = imgResize.shape
                wGap = math.ceil((imgSize - wCal) / 2)
                imgWhite[:, wGap:wCal + wGap] = imgResize
            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                imgResizeShape = imgResize.shape
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite[hGap:hCal + hGap, :] = imgResize

        target_dir = os.path.join(TRAIN_DATA, dir_)
        os.makedirs(target_dir, exist_ok=True)
        if counter > 0:    #не видаляти (видаляти 0 елемент)
            cv2.imwrite(f'{TRAIN_DATA}/{dir_}/Image_{counter}.jpg', imgWhite)
        counter += 1
