from time import sleep
import tensorflow
from pywinauto.application import Application
import cv2
import mss
import win32con,win32gui,win32ui,win32api
import numpy as np
import ctypes
import pyautogui
from clashroyalbot import ClashRoyalBot
# main Ai class which will do all of the Ai stuff once it starts working
class Ai(ClashRoyalBot):
    def __init__(self, training):
        self.training = training
    #presses the big yellow battle button
    #todo: make it work
    def window_capture(self):

        hwnd = "BlueStacks App"
        hwndDC = win32gui.GetWindowDC(hwnd)
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()
        saveBitMap = win32ui.CreateBitmap()

        MoniterDev = win32api.EnumDisplayMonitors(None, None)
        w = MoniterDev[0][2][2]
        h = MoniterDev[0][2][3]

        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        saveDC.SelectObject(saveBitMap)
        saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
        im = saveBitMap.GetBitmapBits(True)  # Tried False also
        img = np.frombuffer(im, dtype=np.uint8).reshape((h, w, 4))
        return img

    def pressBattleButton():
        pic = super.Api.window_capture()
        pic = cv2.imread(pic)
        cv2.imshow(pic)

    def launch(self):
        self.mainloop()
    #main bot loop which will play a battle return to homescreen and do it again
    def mainloop(self):
        neuralNetwork = self.NeuralNetwork()
        neuralNetwork.start()
        
        while True:
            self.pressBattleButton()
            #add Ai stuff

    # class to contain all tensor flow stuff
    class NeuralNetwork():
        def __init__(self):
            pass
        def start(self):
            pass