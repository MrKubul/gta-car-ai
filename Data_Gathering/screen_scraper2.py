import cv2
import keyboard as keyboard
import numpy as np
import pyautogui
import time
import datetime


def grab_screen(region_1, region_2, file_name):
    #im = pyautogui.screenshot(path + "\\" + folder + "\\"+file_name + "_depth.png", region=region_1)   depth capture
    im = pyautogui.screenshot(region=region_2)     #normal capture
    open_cv_image = np.array(im)
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
    open_cv_image = cv2.GaussianBlur(open_cv_image, (3, 3), 0)
    open_cv_image = cv2.Canny(open_cv_image, edge_threshold_min, edge_threshold_max)
    cv2.imwrite(path+"\\" + folder +"\\"+file_name + "_edge.png", open_cv_image)


path = r"C:\Users"

image_to_collect = 1500
id_number = 1
folder = "Data_1"

edge_threshold_min = 50
edge_threshold_max = 220

region1 = (128, 450, 384, 256)  ## left, top, width, and height
region2 = (768, 546, 384, 160)  ## colect only road-view

pyautogui.PAUSE = 0

print("starting in 5 seconds")
time.sleep(5)

while id_number <= image_to_collect:
    start = time.time()
    pyautogui.press('num1')
    file_id = str(id_number) + '_' + datetime.datetime.now().strftime('%H;%M;%S.%f')[:-3]
    grab_screen(region1, region2, file_id)
    id_number = id_number + 1
    if keyboard.is_pressed('q'):  # if key 'q' is pressed
        break
    try:
        time.sleep(0.09-(time.time() - start))
    except:
        pass
    print(id_number-1)


