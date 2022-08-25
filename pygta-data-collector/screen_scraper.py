import PIL
import cv2
import keyboard as keyboard
import numpy as np
import pyautogui
import time
import datetime
import typing
import os, os.path

# rewite to underscore_style

class ScreenScrapper:
    def __init__(self) -> None:
        with open(file) as file:
            lines: list[str]= file.readlines()
            self.datasetPath: str = lines[1]
            self.targetDatasetSize: int = int(lines[4])
            self.grabRegion: typing.Tuple[int, int] = lines[7]
            self.timeInterval: float = float(lines[10])

    def getRegionFromUser(self) -> None:
        pass

    def countFilesInDir(self) -> int:
        return len([name for name in os.listdir(self.datasetPath) if os.path.isfile(os.path.join(self.datasetPath, name))])

    def grab_screen_pyauto(self, file_name, canny_settings) -> None:
        im: PIL.Image = pyautogui.screenshot(region=self.grabRegion)
        open_cv_image: np.array = np.array(im)
        open_cv_image = open_cv_image[:, :, ::-1].copy()
        open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
        open_cv_image = cv2.GaussianBlur(open_cv_image, (3, 3), 0)
        open_cv_image = cv2.Canny(open_cv_image, canny_settings[0], canny_settings[1])
        cv2.imwrite(self.datasetPath + "\\" + file_name + ".png", open_cv_image)
    
    def grab_screen_pil(self, file_name, canny_settings) -> None:
        im: PIL.Image = pyautogui.screenshot(region=self.grabRegion)
        open_cv_image: np.array = np.array(im)
        open_cv_image = open_cv_image[:, :, ::-1].copy()
        open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
        open_cv_image = cv2.GaussianBlur(open_cv_image, (3, 3), 0)
        open_cv_image = cv2.Canny(open_cv_image, canny_settings[0], canny_settings[1])
        cv2.imwrite(self.datasetPath + "\\" + file_name + ".png", open_cv_image)

    def grab_screen_mss(self, file_name, canny_settings) -> None:
        im: PIL.Image = pyautogui.screenshot(region=self.grabRegion)
        open_cv_image: np.array = np.array(im)
        open_cv_image = open_cv_image[:, :, ::-1].copy()
        open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
        open_cv_image = cv2.GaussianBlur(open_cv_image, (3, 3), 0)
        open_cv_image = cv2.Canny(open_cv_image, canny_settings[0], canny_settings[1])
        cv2.imwrite(self.datasetPath + "\\" + file_name + ".png", open_cv_image)
    

    def collect(self) -> None:
        edge_threshold_min: int = 50
        edge_threshold_max: int = 220
        canny_settings = (edge_threshold_min, edge_threshold_max)
        region = (128, 450, 384, 256)     # input from user
        currentDatasetSize = self.countFilesInDir() # read from user
        pyautogui.PAUSE = 0

        if currentDatasetSize >= self.targetDatasetSize:
            raise SystemExit('Dataset already collected, exiting!')
        else:
            currentDatasetSize += 1
            print("Starting collecting data in 5 seconds!")
            print("Please switch your window, so needed region is visible!")
            time.sleep(5)

        while currentDatasetSize <= self.targetDatasetSize:
            print("...Collecting sample no.", currentDatasetSize)
            start: float = time.time()
            pyautogui.press('num1')     # signal for game to collect vehicle data
            file_id: str = str(currentDatasetSize) + '_' + datetime.datetime.now().strftime('%H;%M;%S.%f')[:-3]
            self.grab_screen_pyauto(region, file_id, canny_settings)
            currentDatasetSize += 1
            if keyboard.is_pressed('q'):
                break
            try:
                time.sleep(self.timeInterval - (time.time() - start))
            except:
                pass

