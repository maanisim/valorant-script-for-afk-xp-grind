# Valorant afk deathmatch farmer
# author: https://github.com/michalani
# version 1.3
# screen 1920x1080
# windowed mode (alt+enter)
# xp = 4.5k per hour on deathmatch (can be used on other game modes however it's undetectable on deathmatch due to low chance of getting reported)

import pyautogui
import time
from colorthief import ColorThief
import cv2

#settings
script_refresh_rate = 3
first_start_boolean = True

def first_start(is_start):
    if(is_start == True):
        time.sleep(4.5)
        pyautogui.click(945, 950)

def save_screenshot(name,x,y,height,width):
    pyautogui.screenshot(region=(x,y,height,width)).save(name)
    
#compares two pictures using dominant colors to decide whether they are the same picture
def dominant_color_comparison(img,img2):
    if(ColorThief(img).get_color(quality=1) == ColorThief(img2).get_color(quality=1)):
        return True
    else:
        return False

# anti afk
def press_W(sec):
    t_end = time.time() + sec
    #press w for 0.2seconds
    while time.time() < t_end:
        pyautogui.keyDown('w')
    pyautogui.keyUp('w')
        
def main():
    first_start(first_start_boolean)
    #Delay start so user has time to click game
    while True:
        save_screenshot("black_square2.png",1817,1011,38,18)
        save_screenshot("top_black_square2.png",1816,125,18,28)
    
        #1st color check
        if(dominant_color_comparison('black_square.png','black_square2.png') == True):
            #2nd color check
            if(dominant_color_comparison('top_black_square.png','top_black_square2.png')):
                #delay due to broken MVP bug.
                time.sleep(5.5)
                #location of press again in valorant
                pyautogui.click(931, 990)
                time.sleep(360)
        
        time.sleep(script_refresh_rate)
        press_W(0.2)
main()
