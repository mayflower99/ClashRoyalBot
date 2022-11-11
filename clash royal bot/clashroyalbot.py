
from time import sleep
import tensorflow
from pywinauto.application import Application
import cv2
import mss
import win32con,win32gui,win32ui,win32api
import numpy as np
import ctypes
import pyautogui
class ClashRoyalBot(object):
    def __init__(self):
        pass
    def launch(self):
        Api.launch(self)
        Api.openClash(self)
        Ai.launch(self)
class Api(ClashRoyalBot):
    def __init__(self):
        pass
    #launches blue stacks and if fully starting tries to navigate to clash royal
    def window_capture(self):
        # copy and pasted; todo figure out how works
        #returns image of window
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


    def launch(self, full_start:bool=True):
        try:
            self.Bluestacks = Application().start("C:\\Program Files (x86)\\BlueStacks X\\BlueStacks X.exe")
            sleep(10)
            self.Bluestacksapp = Application().start("C:\\Program Files\\BlueStacks_nxt\\HD-Player.exe")
            self.Bluestacksapp = Application().connect("C:\\Program Files\\BlueStacks_nxt\\HD-Player.exe")
            sleep(10)
            self.Bluestacks.kill()
            return True
        except:
            print("error launching bluestacks...")
            return False
    
    def openClash(self):
        print("navigate to clash royal and enter y when done")         
        sleep(15)
        window = win32gui.FindWindow(None,"BlueStacks App Player")
        x = win32gui.GetWindowRect(window)
        # print(x)
        # pyautogui.moveTo(x[0]+(x[2]*890625),x[1]+(x[3]*.18888888))
        # pyautogui.click()
        # print((x[0]+(x[2]*.880625),x[1]+(x[3]*.18888888)))
    #finds the clash royal window
    def waitloop(self,time:int):
        sleep(time)
class Ai(ClashRoyalBot):
    def __init__(self):
        pass
    def pressBattleButton():
        pic = Api.window_capture()
        pic = cv2.imread(pic)
        cv2.imshow(pic)
    def launch(self):
        self.mainloop()

    def mainloop(self):
        neuralNetwork = self.NeuralNetwork()
        neuralNetwork.start()
        
        while True:
            self.pressBattleButton()
    class NeuralNetwork():
        def __init__(self):
            pass
        def start():
            pass