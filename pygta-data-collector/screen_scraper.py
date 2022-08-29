import PIL
import cv2
import keyboard as keyboard
import numpy as np
import pyautogui
import mss
import time
import datetime
import typing
from typing import List
import os, os.path
from PIL import ImageGrab
from click_coordinates import *


class ScreenScrapper:
    def __init__(self) -> None:
        with open('settings.txt', "r") as file:
            lines: List[str] = file.readlines()
            self.datasetPath: str = lines[1].strip()
            print(self.datasetPath)
            self.targetDatasetSize: int = int(lines[4])
            self.timeInterval: float = float(lines[7])
            self.scriptActivationKey: str = str(lines[10])
            self.grabRegion = None
            if str(lines[13]) != '_':
                self.grabRegion = tuple(int(num) for num in lines[13].replace('(', '').replace(')', '').split(', '))

    def get_region_from_user(self) -> None:
        self.grabRegion = get_region()
        lines = []
        with open('settings.txt', "r") as file:
            lines = file.readlines()
        lines[13] = str(self.grabRegion)
        with open('settings.txt', "w") as file:
            file.writelines(lines)

    def count_files_in_dir(self) -> int:
        return len([name for name in os.listdir(self.datasetPath)])

    def process_image(self, image, canny_settings):
        image: np.array = np.array(image)
        image = image[:, :, ::-1].copy()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.GaussianBlur(image, (3, 3), 0)
        image = cv2.Canny(image, canny_settings[0], canny_settings[1])
        return image

    def grab_screen_pyauto(self, file_name, canny_settings) -> None:
        im = pyautogui.screenshot(region=self.grabRegion)
        im = self.process_image(im, canny_settings)
        cv2.imwrite(self.datasetPath + "\\" + file_name + ".png", im)

    def grab_screen_pil(self, file_name, canny_settings) -> None:
        im = ImageGrab.grab()
        im = self.process_image(im, canny_settings)
        cv2.imwrite(self.datasetPath + "\\" + file_name + ".png", im)

    def grab_screen_mss(self, file_name, canny_settings) -> None:
        with mss.mss() as sct:
            img = sct.shot(mon=-1, output=file_name)

    def collect(self) -> None:
        edge_threshold_min: int = 50
        edge_threshold_max: int = 220
        canny_settings = (edge_threshold_min, edge_threshold_max)
        curr_dataset_size = self.count_files_in_dir()
        pyautogui.PAUSE = 0

        if self.grabRegion:
            print("Found previously found grab region, do you want to still use it?")
            inp = ' '
            while inp != 'y' and inp != 'n':
                inp = str(input("Write y/n: "))
            if inp == 'n':
                self.get_region_from_user()
        else:
            self.get_region_from_user()

        if curr_dataset_size >= self.targetDatasetSize:
            raise SystemExit('Dataset already collected, exiting!')
        else:
            curr_dataset_size += 1
            print("Starting collecting data in 5 seconds!")
            print("Please switch your window, so needed region is visible!")
            time.sleep(5)

        if self.scriptActivationKey.strip() == 'num0' or self.scriptActivationKey.strip() == 'numlock' \
                or self.scriptActivationKey.strip() == 'pagedown':
            pass
        else:
            raise RuntimeError("Wrong script activation key, change settings!")

        while curr_dataset_size <= self.targetDatasetSize:
            print("...Collecting sample no.", curr_dataset_size)
            start: float = time.time()
            pyautogui.press(self.scriptActivationKey)
            file_id: str = str(curr_dataset_size) + '_' + datetime.datetime.now().strftime('%H;%M;%S.%f')[:-3]
            self.grab_screen_pyauto(file_id, canny_settings)
            curr_dataset_size += 1
            if keyboard.is_pressed('q'):
                break
            try:
                if end := time.time() - start < self.timeInterval:
                    time.sleep(self.timeInterval - (time.time() - start))
            except Exception as e:
                raise e
