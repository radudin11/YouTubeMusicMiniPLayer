from asyncio.windows_events import NULL
from cProfile import label
from timeit import repeat
from tkinter.tix import MAIN
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
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--verbose")
    chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")

    driver = webdriver.Chrome(service = Service(".\\chromedriver_win32_105\\chromedriver.exe"), options = chrome_options)
    driver.get("https://music.youtube.com/")
    return driver

def main():
    driver = driver_setup()
    buttonRepeat = get_button(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[3]/ytmusic-player-expanding-menu/tp-yt-paper-icon-button[2]")
    stateExpandMenu = get_button(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[3]/ytmusic-player-expanding-menu")
    buttonExpandMenu = get_button(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[3]/div/tp-yt-paper-icon-button[4]/tp-yt-iron-icon")
    volumeslider = get_button(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[3]/ytmusic-player-expanding-menu/tp-yt-paper-slider")
    while True:
        print(volumeslider.get_attribute('value'))
        volumeslider.setAttribute('value', 30) 
        time.sleep(3)

if __name__ == '__main__':
    main()