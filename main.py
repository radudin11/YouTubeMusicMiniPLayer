import tkinter as tk
import sys 
import os
sys.path.append(os.path.abspath("C:\\Radu\coding_2022\\YouTubeMusicMiniPLayer\\"))
from MiniPLayerV1_0 import *

class main :

    global buttonNext
    global buttonPrev
    global buttonPlayPause

    def setUp():
        driver = driver_setup()
        print("Setup done!")
        main.buttonNext = get_element(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[1]/div/tp-yt-paper-icon-button[5]")
        main.buttonPrev = get_element(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[1]/div/tp-yt-paper-icon-button[1]")
        main.buttonPlayPause = get_element(driver=driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[1]/div/tp-yt-paper-icon-button[3]/tp-yt-iron-icon")
        
    def pressPlayPause():
        pressButton(main.buttonPlayPause)
    def pressNext():
        pressButton(main.buttonNext)
    def pressPrev():
        pressButton(main.buttonPrev)

    def main():

        main.setUp()
        window = tk.Tk()

        frame = tk.Frame(master = window, background= "black", width= 500, height = 100)
        frame.pack(fill=tk.BOTH, expand=True)



        btnPlayPause = tk.Button(background="gray", master=frame, width=10, height=5, text="Play/Pause", borderwidth=5, command=main.pressPlayPause)
        btnPlayPause.grid(row=0, column=1, padx=5, pady=5)
        btnPrevious = tk.Button(background="gray", master=frame, width=10, height=5, text="<<", borderwidth=5, command=main.pressPrev)
        btnPrevious.grid(row=0, column=0, padx=5, pady=5)
        btnNext = tk.Button(background="gray", master=frame, width=10, height=5, text=">>", borderwidth=5, command=main.pressNext)
        btnNext.grid(row=0, column=2, padx=5, pady=5)

        window.mainloop()

if __name__ == '__main__':
        main.main()
