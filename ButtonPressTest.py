from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(service = Service("C:\\Radu\\chromedriver_win32_105\\chromedriver.exe"), options = chrome_options)
    driver.get("https://music.youtube.com/")
    #time.sleep(10)
    tryAgain = 1;
    while tryAgain:
        try:
            buttonNext = driver.find_element(By.XPATH, "/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[1]/div/tp-yt-paper-icon-button[5]")
            tryAgain = 0;
        except Exception as e:
            print("ButtonNext not found!")
            tryAgain = 1;
            time.sleep(1);


    tryAgain = 1;
    while tryAgain:
        try:
            buttonPrev = driver.find_element(By.XPATH, "/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[1]/div/tp-yt-paper-icon-button[1]")
            tryAgain = 0;
        except Exception as e:
            print("ButtonPrev not found!")
            tryAgain = 1;
            time.sleep(1);


    while(1):
        cmd = input("Give command: ")
        if cmd == 'n' :
            try:
                buttonNext.click();
            except Exception as e:
                print("Can't press buttonNext")
        if cmd == 'p' :
            try:
                buttonPrev.click();
            except Exception as e:
                print("Can't press buttonPrev")
        if cmd == 'q':
            driver.quit()
            break;
        
if __name__ == '__main__':
    main()
