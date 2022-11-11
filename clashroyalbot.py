
from time import sleep
import tensorflow
from pywinauto.application import Application
import cv2
import mss
import win32con,win32gui,win32ui,win32api
import numpy as np
import ctypes
import pyautogui

#This class is the main body of the bot and 
#will succeed in automating Clash royal
#plan is in notebook.txt
class ClashRoyalBot(object):
    def __init__(self):
        pass
    #runs launch functions for all subsiderary classes
    def launch(self):
        #launches the program
        Api.launch(self)
        #broken currently but will open clash royal window
        Api.openClash(self)
        #lauches image rec and main Ai once clash up and running
        Ai.launch(self)
class Api(ClashRoyalBot):
    def __init__(self):
        pass
    # copy and pasted; todo figure out how works
    #returns image of window
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

    #launches blue stacks and if fully starting tries to navigate to clash royal

    def launch(self, full_start:bool=True):
        try:                                       #replace with your path to bluestacks for the following three
            #starts main app
            self.Bluestacks = Application().start("C:\\Program Files (x86)\\BlueStacks X\\BlueStacks X.exe")

            sleep(10)
            #starts and connects to the app player: what actually runs clash royal
            self.Bluestacksapp = Application().start("C:\\Program Files\\BlueStacks_nxt\\HD-Player.exe")
            self.Bluestacksapp = Application().connect("C:\\Program Files\\BlueStacks_nxt\\HD-Player.exe")
            sleep(10)
            #should the instance of the main app after start up
            self.Bluestacks.kill()
            return True
        except:
            print("error launching bluestacks...")
            return False
    #does nothing right now but will hopfull navigate bluestacks gui to get to CR
    def openClash(self):

        print("navigate to clash royal and enter y when done")         
        sleep(15)
        window = win32gui.FindWindow(None,"BlueStacks App Player")
        # gets x and y of top left and top right outputs as [x1,y1,x2,y,2]
        x = win32gui.GetWindowRect(window)
        # print(x)
        # pyautogui.moveTo(x[0]+(x[2]*890625),x[1]+(x[3]*.18888888))
        # pyautogui.click()
        # print((x[0]+(x[2]*.880625),x[1]+(x[3]*.18888888)))

# main Ai class which will do all of the Ai stuff once it starts working
class Ai(ClashRoyalBot):
    def __init__(self):
        pass
    #presses the big yellow battle button
    #todo: make it work
    def pressBattleButton():
        pic = Api.window_capture()
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
        def start():
            pass