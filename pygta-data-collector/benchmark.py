import PIL
from mss import mss
from PIL import ImageGrab, Image
import pyautogui
import numpy as np
import cv2
import time

# Simple benchmark to test result of different screenshot collectors on you machine.

# My results for saving 1000 screenshots:
# mss:  90.7238256931305s
# PIL:  67.09843254089355s
# pyauto:  67.16531896591187s

TESTPATH = r'path'


def test_pil():
    start: float = time.time()
    for i in range(1000):
        im = ImageGrab.grab()
        open_cv_image: np.array = np.array(im)
        cv2.imwrite(TESTPATH + "\\" + str(i) + ".png", open_cv_image)
    print("Result for pil: ", time.time() - start)


def test_mss():
    start: float = time.time()
    with mss() as sct:
        for i in range(1000):
            t = TESTPATH + '\\' + str(i) + '.png'
            img = sct.shot(mon=-1, output=t)

    print("Result for mss: ", time.time() - start)


def test_pyauto():
    start: float = time.time()
    for i in range(1000):
        im: PIL.Image = pyautogui.screenshot()
        open_cv_image: np.array = np.array(im)
        cv2.imwrite(TESTPATH + "\\" + str(i) + ".png", open_cv_image)
    print("Result for pyauto: ", time.time() - start)


def run_benchmark():
    test_mss()
    test_pil()
    test_pyauto()


if __name__ == "__main__":
    print("Running benchmarks...")
    run_benchmark()
    print("Finished")
