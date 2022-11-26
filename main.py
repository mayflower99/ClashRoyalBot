import tensorflow as tfm
from time import sleep
from pywinauto.application import Application
import pywinauto
import cv2
import sys
from clashroyalbot import ClashRoyalBot

if __name__ == "__main__":
    #initalise main class
    clashroyalbot = ClashRoyalBot()

    #sets up the clash royal bot
    clashroyalbot.init()
    clashroyalbot.launch_bot()
    clashroyalbot.close()

