from asyncio.windows_events import NULL
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
import subprocess





def get_button(xpath = "", driver = NULL):
    tryAgain = 50
    while tryAgain:
        try:
            button = driver.find_element(By.XPATH, xpath)
            tryAgain = 0
        except Exception as e:
            print("ButtonNext not found!")
            tryAgain -= 1
            time.sleep(1)
    return button

def driver_setup():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument("--verbose")
    # chrome_options.add_argument(r"--user-data-dir=C:\path\to\chrome\user\data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
    # chrome_options.add_argument(r'--profile-directory="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"')
    chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")

    driver = webdriver.Chrome(service = Service("C:\\Radu\\chromedriver_win32_105\\chromedriver.exe"), options = chrome_options)
    driver.get("https://music.youtube.com/")
    return driver

def isDriverClosed(driver):
    if driver:
        if not driver.window_handles:
            return True
        else:
            return False

def pressButton(button):
    try:
        button.click()
        return True
    except Exception as e:
        print("Can't press button")
        return False
def main():
    # command = 'C:\\Program^ Files\\Google\\Chrome\\Application\\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\\Radu\\chromedriver_win32_105\\localhost"'
    # os.system(command)
    # file = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    # subprocess.call([file])
    # os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')

    expandedMenuIsClicked = False

    driver = driver_setup()
    buttonNext = get_button(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[1]/div/tp-yt-paper-icon-button[5]")
    buttonPrev = get_button(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[1]/div/tp-yt-paper-icon-button[1]")
    buttonPlayPause = get_button(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[1]/div/tp-yt-paper-icon-button[3]/tp-yt-iron-icon")
    buttonMute = get_button(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[3]/ytmusic-player-expanding-menu/tp-yt-paper-icon-button[1]/tp-yt-iron-icon")
    buttonVolumeOptions = get_button(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[3]/div/tp-yt-paper-icon-button[4]/tp-yt-iron-icon")
    
    while 1:
        cmd = input("Give command: ")
        if cmd == 'n' :
            pressButton(buttonNext)
            continue
        if cmd == 'p' :
            pressButton(buttonPrev)
            continue
        if cmd == 'P' :
            pressButton(buttonPlayPause)
            continue
        if cmd == 'm' :
            if expandedMenuIsClicked == False:
                expandedMenuIsClicked = pressButton(buttonVolumeOptions)
            pressButton(buttonMute)
            continue
        if cmd == 'q':
            break
        print("Button unrecognised")

    driver.quit()
if __name__ == '__main__':
    main()
        
