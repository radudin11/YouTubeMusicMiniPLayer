from asyncio.windows_events import NULL
from timeit import repeat
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
import subprocess


from selenium.webdriver.support import expected_conditions

from selenium.webdriver.common.action_chains import ActionChains


def get_element_xpath(xpath = "", driver = NULL):
    # searches for an element from the web driver 
    # at the given xpath
    tryAgain = 50
    while tryAgain:
        try:
            button = driver.find_element(By.XPATH, xpath)
            tryAgain = 0
        except Exception as e:
            print("Element not found!")
            tryAgain -= 1
            time.sleep(1)
    return button
def get_element_className(className = "", driver = NULL):
    # searches for an element from the web driver 
    # at the given xpath
    tryAgain = 50
    while tryAgain:
        try:
            button = driver.find_element(By.CLASS_NAME, className)
            tryAgain = 0
        except Exception as e:
            print("Element not found!")
            tryAgain -= 1
            time.sleep(1)
    return button

def get_element_id(id = "", driver = NULL):
    # searches for an element from the web driver 
    # at the given xpath
    tryAgain = 50
    while tryAgain:
        try:
            button = driver.find_element(By.ID, id)
            tryAgain = 0
        except Exception as e:
            print("Element not found!")
            tryAgain -= 1
            time.sleep(1)
    return button


def driver_setup():
    # sets all the options for the chrome driver, opens it
    # and returns
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--verbose")
    chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")

    driver = webdriver.Chrome(service = Service(".\\chromedriver_win32_105\\chromedriver.exe"), options = chrome_options)
    driver.get("https://music.youtube.com/")
    return driver

def isDriverClosed(driver):
    if driver:
        if not driver.window_handles:
            return True
        else:
            return False

def pressButton(button):
    # tries to call .click() method on the elemnt given
    # returns true or false
    try:
        button.click()
        return True
    except Exception as e:
        print("Can't press button")
        return False

def main():
    # command = './Chrome/Application/chrome.exe --remote-debugging-port=9222 --user-data-dir="./chromedriver_win32_105/localhost"\n'
    # subprocess.run(command)
    # print("SetUping")

    expandedMenuIsClicked = False

    driver = driver_setup()
    print("Setup done!")
    buttonNext = get_element_xpath(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[1]/div/tp-yt-paper-icon-button[5]")
    buttonPrev = get_element_xpath(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[1]/div/tp-yt-paper-icon-button[1]")
    buttonPlayPause = get_element_xpath(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[1]/div/tp-yt-paper-icon-button[3]/tp-yt-iron-icon")
    buttonMute = get_element_xpath(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[3]/ytmusic-player-expanding-menu/tp-yt-paper-icon-button[1]/tp-yt-iron-icon")
    #buttonMute = get_element_id(driver=driver, id= "expand-volume")
    
    # expandingMenu = driver.find_element(By.XPATH, '//*[@id="expanding-menu"]')
    # expandVolume = expandingMenu.find_element(By.XPATH, '//*[@id="expand-volume"]')
    # buttonMute = expandVolume.find_element(By.XPATH, '//*[@id="icon"]')

    buttonExpandMenu = get_element_xpath(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[3]/div/tp-yt-paper-icon-button[4]/tp-yt-iron-icon")
    buttonRepeat = get_element_xpath(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[3]/ytmusic-player-expanding-menu/tp-yt-paper-icon-button[2]")
    expandMenuState = get_element_xpath(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[3]/ytmusic-player-expanding-menu")
    buttonShuffle = get_element_xpath(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[3]/ytmusic-player-expanding-menu/tp-yt-paper-icon-button[3]/tp-yt-iron-icon")
    playPauseState = get_element_xpath(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[1]/div/tp-yt-paper-icon-button[3]")
    muteState = get_element_xpath(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[3]/ytmusic-player-expanding-menu/tp-yt-paper-icon-button[1]")
    while 1:
        cmd = input("Give command: ")
        if cmd == 'n' :  # next
            if pressButton(buttonNext):
                print("Next")
            continue
        if cmd == 'p' :  # previous
            if pressButton(buttonPrev):
                print("Previous")
            continue
        if cmd == 'P' :  # pause/play
            print(playPauseState.get_attribute('aria-label'))
            pressButton(buttonPlayPause)
            continue
        if cmd == 'm' :  # mute/unmute
            if expandMenuState.get_attribute('aria-hidden') == 'true':
                hover = ActionChains(driver).move_to_element(expandMenuState)
                hover.perform()
            if pressButton(buttonMute) :
                time.sleep(0.2)
                if muteState.get_attribute('aria-pressed') == 'false' :
                    print("Unmute")
                else :
                    print("Mute")
            continue
        if cmd == 'r' :  # repeat
            if expandMenuState.get_attribute('aria-hidden') == 'true':
                pressButton(buttonExpandMenu)
            if pressButton(buttonRepeat) :
                print(buttonRepeat.get_attribute('title'))
            continue
        if cmd == 's' :  # shuffle
            if expandMenuState.get_attribute('aria-hidden') == 'true':
                pressButton(buttonExpandMenu)
            if pressButton(buttonShuffle) :
                print("Shuffle")
            continue
        if cmd == 'q':  # quit
            break
        print("Button unrecognised")

    driver.quit()
if __name__ == '__main__':
    main()
        
