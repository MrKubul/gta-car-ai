import cv2
import keyboard as keyboard
import numpy as np
import pyautogui
import time
import datetime
from model import *
import pyvjoy

def grab_screen(region_2):
    im = pyautogui.screenshot(region=region_2)
    open_cv_image = np.array(im)
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
    open_cv_image = cv2.GaussianBlur(open_cv_image, (3, 3), 0)
    open_cv_image = cv2.Canny(open_cv_image, 50, 220)
    return open_cv_image


region1 = (128, 450, 384, 256)  ## left, top, width, and height
region2 = (768, 546, 384, 160)  ## colect only road-view

pyautogui.PAUSE = 0
j = pyvjoy.VJoyDevice(1)

vjoy_max = 32768

print("starting in 5 seconds")
time.sleep(2)

while True:
    image = grab_screen(region2)
    filename = "image.jpg"
    cv2.imwrite(filename, image)
    img = cv2.imread('image.jpg')
    predictions = predict_values(img)
    print(predictions)
    j.data.wAxisX = vjoy_max//2
    j.data.wAxisY = vjoy_max//2
    j.update()
    time.sleep(0.1)
    if keyboard.is_pressed('q'):
        break
