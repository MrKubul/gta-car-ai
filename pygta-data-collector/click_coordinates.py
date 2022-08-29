import cv2
import pyautogui


def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        position = pyautogui.position()
        params.add_coord(position)
        print("Point collected succesfully")


def get_region():
    img = cv2.imread('img.png', 1)
    cv2.namedWindow('window', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('window', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    region_image = Region()
    print("Click two point on image to mark field from screenshots will be collected")
    while not region_image.ready:
        clear_img = cv2.imread('img.png', 1)
        if region_image.is_partially_defined():
            cv2.rectangle(clear_img, region_image.first_coord,
                          pyautogui.position(), (255, 0, 0), 3)
        cv2.imshow('window', clear_img)
        cv2.setMouseCallback('window', click_event, region_image)
        cv2.waitKey(30)
    cv2.rectangle(img, region_image.first_coord,
                        region_image.second_coord, (125, 255, 0), 10)
    cv2.imshow("window", img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    return region_image.first_coord[0], region_image.first_coord[1], region_image.second_coord[0], \
           region_image.second_coord[1]


class Region:
    def __init__(self):
        self.first_coord = None
        self.second_coord = None
        self.ready = False

    def add_coord(self, coords):
        if self.first_coord is None:
            self.first_coord = coords
        elif self.second_coord is None:
            self.second_coord = coords
        if self.first_coord and self.second_coord:
            self.ready = True
            print("End o setup, ready to pass region")

    def is_partially_defined(self):
        return self.first_coord and self.second_coord is None
