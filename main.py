# Valorant afk deathmatch farmer
# author: https://github.com/michalani
# version 1.5
# screen 1920x1080
# windowed mode (alt+enter)
# xp = 4.5k per hour on deathmatch (can be used on other game modes (if modified correctly) however it's undetectable on deathmatch due to low chance of getting reported)

import pyautogui
import time
from colorthief import ColorThief
import cv2

# Settings (changable)
launch_valorant = True # if valorant is already started simply set to False and go to valorant.
time_to_launch_valorant = 90 # increase this if you have any problems of script starting before the game launches
valorant_location = '"C:\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=valorant --launch-patchline=live'

# [DONT CHANGE OR RISK BREAKEAGE]
gamemode = 3 # DO NOT CHANGE!
script_refresh_rate = 5
first_start_boolean = True
is_in_queue = False

# Mouse click at x,y cordinates
def click(x,y):
    print("clicked ("+str(x)+","+str(y)+")")
    pyautogui.moveTo(x, y, 2, pyautogui.easeInOutQuad)
    pyautogui.click(x, y)
    time.sleep(2)

# Select which game mode will be played
def select_mode(mode):
    click(610+(160*mode), 120)

# As queuing for the first time takes more buttons it has it's own function   
def queue_up_for_first_time(is_start):
    if(is_start == True):
        print("queuing up for gamemode: "+str(gamemode))
        time.sleep(4.5)
        click(943,50)
        select_mode(gamemode)
        click(945,950)
        first_start_boolean = False
# Takes a pic (used in order to determine current location in valorant (are we playing? are we in mainscreen?)
def save_screenshot(name,x,y,height,width):
    print("saving screenshot: "+name)
    pyautogui.screenshot(region=(x,y,height,width)).save(name)

# Compares two pictures using dominant colors to decide whether they are the same picture
def dominant_color_comparison(stored_color,img):
    print("comparing: "+img)
    if(stored_color == ColorThief(img).get_color(quality=1)):
        return True
    else:
        return False

# Anti afk
def press_W(sec):
    t_end = time.time() + sec
    #press w for 0.2seconds
    while time.time() < t_end:
        pyautogui.keyDown('w')
    pyautogui.keyUp('w')

# Detects game disconections and black screens    
def is_error():
    col_error = (255, 84, 84)
    if(pyautogui.screenshot().getpixel((1111, 394)) == col_error):
        if(pyautogui.screenshot().getpixel((795, 404)) == col_error):
            first_start_boolean = True
            launch_game()
            print("Connection Error detected!")
    else:
        save_screenshot("err3_c.png",197,65,1561,883)
        if(dominant_color_comparison((4, 4, 4),'err3_c.png') == True):
            time.sleep(4.96)
            save_screenshot("err3_c2.png",197,65,1561,883)
            if(dominant_color_comparison((4, 4, 4),'err3_c2.png') == True):
                first_start_boolean = True
                launch_game()
                print("Connection Error detected!")

# Launches the game for the first time, can be used to restart the game as it kills game first.
def launch_game():
    print("launching valorant")
    pyautogui.hotkey('win','r')
    time.sleep(2)
    pyautogui.write('cmd', interval=0.001)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write('taskkill /f /im VALORANT-Win64-Shipping.exe')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write(valorant_location)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write("exit")
    pyautogui.press('enter')
    time.sleep(time_to_launch_valorant)
    pyautogui.hotkey('win','up')

def main():
    if(launch_valorant == True):
        launch_game()
    else:
        time.sleep(3)
    queue_up_for_first_time(first_start_boolean)
    while True:
        save_screenshot("black_square2.png",1817,1011,38,18)
        save_screenshot("top_black_square2.png",1816,125,18,28)
        if(dominant_color_comparison((44, 52, 60),'black_square2.png') == True): #1st color check
            time.sleep(5.5) #delay due to broken MVP bug.
            
            if(dominant_color_comparison((44, 52, 60),'top_black_square2.png')): #2nd color check
                if(is_in_queue == True):
                    time.sleep(10)
                else:
                    click(931,990) #location of press again in valorant
                    press_W(0.2)
                    time.sleep(8)
                    is_in_queue = True
        else:
            is_in_queue = False
        
        time.sleep(script_refresh_rate)
        press_W(0.2)
        is_error()
main()
