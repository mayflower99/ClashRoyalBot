
from time import sleep
import tensorflow as tf
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
    @staticmethod
    def window(windowname):
        window = win32gui.FindWindow(None,windowname)
        # gets x and y of top left and top right outputs as [x1,y1,x2,y,2]
        x = win32gui.GetWindowRect(window)
        print(x)
        return x
    
    #runs launch functions for all subsiderary classes
    def launch_bot(self,training = True):
        #launches the program
        #broken currently but will open clash royal window
        self.ai = Ai(training)
        #lauches image rec and main Ai once clash up and running
        self.ai.launch()
        
    def close(self):
        pass
    #launches blue stacks and clash royal
    @staticmethod
    def init():

        try:                                       
            #replace with your path to bluestacks for the following three
            #starts the app player: what actually runs clash royal
            Bluestacksapp = Application().start("C:\\Program Files\\BlueStacks_nxt\\HD-Player.exe")

            
        except:
            print("error launching bluestacks...")
        sleep(10)
        Ai.locateandclick(img="imagelib\\gui\\clashroyalstart.png")


    # main Ai class which will do all of the Ai stuff once it starts working
class Ai(ClashRoyalBot):

    def __init__(self, training):
        self.training = training
    #presses the big yellow battle button
    #todo: make it work
    @staticmethod
    def __Screen_Shot(left=0, top=0, width=1920, height=1080):
            stc = mss.mss()
            scr = stc.grab({
                'left': left,
                'top': top,
                'width': width,
                'height': height
            })

            img = np.array(scr)
            img = cv2.cvtColor(img, cv2.IMREAD_COLOR)

            return img

    def locateandclick(img, displayimage=False):
        while True:
            window = ClashRoyalBot.window("BlueStacks App Player")
            pic = Ai.__Screen_Shot(window[0],window[1],window[2]-window[0],window[3]-window[1])
            battle_image = np.array(cv2.imread(img))
            matrix = cv2.matchTemplate(pic, battle_image, cv2.TM_CCOEFF_NORMED)
            minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(matrix)
            # draw the bounding box on the image
            cv2.rectangle(pic, maxLoc, (maxLoc[0]+battle_image.shape[1],maxLoc[1]+battle_image.shape[0]), (255, 0, 0), 10)
            if displayimage:
                image = cv2.imshow("image",pic)
                cv2.waitKey(1)
            print(maxVal)
            if maxVal*100 >= 99.0:
                for i in range(3):
                    pyautogui.click(window[0]+maxLoc[0]+(battle_image.shape[1]/2),window[1]+maxLoc[1]+(battle_image.shape[0]/2),interval=1)
                break
    
    

    def __mainloop(self):
        neuralNetwork = self.__NeuralNetwork()
        neuralNetwork.start()
        
        while True:
            Ai.locateandclick(img="imagelib\\gui\\battleicon.png")
            
            #add Ai stuff
    
    
    
    #main bot loop which will play a battle return to homescreen and do it again
    def launch(self):
        self.__mainloop()

    # class to contain all tensor flow stuff
    class __NeuralNetwork():

        def __init__(self):
            self.Elixer:int = 0
            self.Time:float = 0.0 
            self.cards = [0,[0,0,0,0]]
            import threading as th
            update = th.Thread(target=self.__update)
            update.start()
        def __update(self):
            pass
        def start(self):
            pass