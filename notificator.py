from time import sleep
import pyautogui
import winsound
import os
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
        
os.system('cls')
print("Ready !\nWaiting for invitations...")

while True:
    sleep(1)
    try:
        x = pyautogui.locateCenterOnScreen('new_request.PNG', confidence = 0.9)
    except Exception as e:
        print(e)
        sleep(5)
    
    if x != None:
        try:
            winsound.PlaySound(dname+'\\sound.wav', winsound.SND_FILENAME)
        except:
            print("Audio file not found !")