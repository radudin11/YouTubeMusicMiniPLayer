from asyncio.windows_events import NULL
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


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
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(service = Service("C:\\Radu\\chromedriver_win32_105\\chromedriver.exe"), options = chrome_options)
    driver.get("https://music.youtube.com/")
    return driver

def isDriverClosed(driver):
    if driver:
        if not driver.window_handles:
            return True
        else:
            return False
def main():
    volumeOptionsIsClicked = False

    driver = driver_setup()
    buttonNext = get_button(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[1]/div/tp-yt-paper-icon-button[5]")
    buttonPrev = get_button(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[1]/div/tp-yt-paper-icon-button[1]")
    buttonPlayPause = get_button(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[1]/div/tp-yt-paper-icon-button[3]/tp-yt-iron-icon")
    buttonMute = get_button(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[3]/ytmusic-player-expanding-menu/tp-yt-paper-icon-button[1]/tp-yt-iron-icon")
    buttonVolumeOptions = get_button(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[3]/div/tp-yt-paper-icon-button[4]/tp-yt-iron-icon")
    while 1:
        buttonWasPressed = False
        cmd = input("Give command: ")
        if cmd == 'n' :
            try:
                buttonNext.click()
            except Exception as e:
                print("Can't press buttonNext")
            buttonWasPressed = True
        if cmd == 'p' :
            try:
                buttonPrev.click()
            except Exception as e:
                print("Can't press buttonPrev")
            buttonWasPressed = True
        if cmd == 'P' :
            try:
                buttonPlayPause.click()
            except Exception as e:
                print("Can't press buttonPlayPause")
            buttonWasPressed = True
        if cmd == 'm' :
            try:
                if volumeOptionsIsClicked == False :
                    buttonVolumeOptions.click()
                    volumeOptionsIsClicked = True
                # time.sleep(1)
                buttonMute.click()
            except Exception as e:
                print("Can't press buttonMute")
            buttonWasPressed = True
        if cmd == 'q':
            break
        if buttonWasPressed == False:
            print("Button unrecognised")

    driver.quit()
if __name__ == '__main__':
    main()
        
