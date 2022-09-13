import tkinter as tk
import sys 
import os
sys.path.append(os.path.abspath("C:\\Radu\coding_2022\\YouTubeMusicMiniPLayer\\"))
from MiniPLayerV1_0 import *
import ctypes as ct

class main :

    global buttonNext
    global buttonPrev
    global buttonPlayPause
    global songTitle
    global artist
    global songTime
    global driver


    def dark_title_bar(window):
        """
        MORE INFO:
        https://docs.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
        """
        window.update()
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
        get_parent = ct.windll.user32.GetParent
        hwnd = get_parent(window.winfo_id())
        rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
        value = 2
        value = ct.c_int(value)
        set_window_attribute(hwnd, rendering_policy, ct.byref(value),
                            ct.sizeof(value))

    def setUp():
        main.driver = driver_setup()

        main.buttonNext = get_element(driver=main.driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[1]/div/tp-yt-paper-icon-button[5]")
        main.buttonPrev = get_element(driver=main.driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[1]/div/tp-yt-paper-icon-button[1]")
        main.buttonPlayPause = get_element(driver=main.driver, xpath="/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[1]/div/tp-yt-paper-icon-button[3]/tp-yt-iron-icon")
        main.songTitle = get_element(driver=main.driver, xpath='/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[2]/div[2]/yt-formatted-string')
        main.artist = get_element(driver=main.driver, xpath='/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[2]/div[2]/span/span[2]/yt-formatted-string')
        main.songTime = get_element(driver=main.driver, xpath='/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/tp-yt-paper-slider')
    def pressPlayPause():
        pressButton(main.buttonPlayPause)
    def pressNext():
        pressButton(main.buttonNext)
    def pressPrev():
        pressButton(main.buttonPrev)

    def updateTitle(window, labelTitle, labelArtist, labelSongTime):
        tryAgain = 10
        while tryAgain:
            try:
                labelTitle.config(text=main.songTitle.get_attribute('title'))
                labelArtist.config(text=main.artist.get_attribute('title'))
                labelSongTime.config(text=main.songTime.get_attribute('aria-valuetext'))
                tryAgain = 0
            except Exception as e:
                main.artist = get_element(driver=main.driver, xpath='/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[2]/div[2]/span/span[2]/yt-formatted-string')
                main.songTime = get_element(driver=main.driver, xpath='/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/tp-yt-paper-slider')
                tryAgain -= 1
        window.after(1000, main.updateTitle, window, labelTitle, labelArtist, labelSongTime)
    def main():

        main.setUp()
        window = tk.Tk()
        main.dark_title_bar(window)

        window.iconphoto(False, tk.PhotoImage(file='images\YTMusicLogoWhiteOnBlack.png'))
        window.title("YouTubeMusicPlayer")

        buttonFrame = tk.Frame(master = window, background= "black", width= 300, height = 50)
        buttonFrame.pack(fill=tk.BOTH, expand=True)

        titleFrame = tk.Frame(master = window, background= "black",height=20, width=100)
        titleFrame.pack(fill=tk.BOTH, expand=True)

        lbl_songTitle = tk.Label(background="black", foreground='white', text = main.songTitle.get_attribute('title'),master=titleFrame)
        lbl_songTitle.pack(fill='x', expand=False, pady=1)

        lbl_artist = tk.Label(background="black", foreground='white', text = main.artist.get_attribute('title'),master=titleFrame)
        lbl_artist.pack(fill=tk.BOTH, expand=False, pady=0)
        
        lbl_songTime = tk.Label(background="black", foreground='white', text = main.songTime.get_attribute('aria-valuetext'),master=titleFrame)
        lbl_songTime.pack(side = tk.RIGHT)

        btnPlayPause = tk.Button(background="gray", master=buttonFrame, width=10, height=5, text="Play/Pause", borderwidth=5, command=main.pressPlayPause)
        # btnPlayPause.grid(row=0, column=1, padx=5, pady=5, sticky='n')
        btnPlayPause.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        btnPrevious = tk.Button(background="gray", master=buttonFrame, width=10, height=5, text="<<", borderwidth=5, command=main.pressPrev)
        # btnPrevious.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        btnPrevious.place(relx=0, rely=0.5, anchor="w")
        
        btnNext = tk.Button(background="gray", master=buttonFrame, width=10, height=5, text=">>", borderwidth=5, command=main.pressNext)
        # btnNext.grid(row=0, column=2, padx=5, pady=5, sticky='w')
        btnNext.place(relx=1, rely=0.5, anchor="e")
        
        main.updateTitle(window ,lbl_songTitle, lbl_artist, lbl_songTime)

        window.mainloop()

if __name__ == '__main__':
        main.main()
