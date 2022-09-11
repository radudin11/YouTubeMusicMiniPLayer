import subprocess

file = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
subprocess.check_call([file, '--remote-debugging-port=9222',  '--user-data-dir="C:\\Radu\\chromedriver_win32_105\\localhost"'])