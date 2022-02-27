import datetime
import cv2
import numpy as np
import pyautogui
import time


def grab_screen(region_1, region_2, file_name):
    im = pyautogui.screenshot(path + "\\" + file_name + "_depth.png", region=region_1)
    im = pyautogui.screenshot(region=region_2)
    open_cv_image = np.array(im)
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
    open_cv_image = cv2.GaussianBlur(open_cv_image, (5, 5), 0)
    open_cv_image = cv2.Canny(open_cv_image, edge_threshold_min, edge_threshold_max)
    cv2.imwrite(path+"\\"+file_name + "_edge.png", open_cv_image)


path = r"path_to_dataset"

image_to_collect = 10
id_number = 1

edge_threshold_min = 176 ## best setting to collect road stripes
edge_threshold_max = 180

region1 = (128, 450, 384, 256)  ## left, top, width, and height
region2 = (768, 546, 384, 160)  ## colect only road-view

while id_number <= image_to_collect:
    start = time.time()
    file_id = str(id_number) + '_' + datetime.datetime.now().strftime('%H;%M;%S.%f')[:-3]
    grab_screen(region1, region2, file_id)
    print("\n", id_number)
    id_number = id_number + 1
    end = time.time()
    print(end-start)
