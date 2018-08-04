import time
import webbrowser

intialCount = 1
breakTimeCount = 3
while intialCount <= breakTimeCount:
    time.sleep(10)
    webbrowser.open("https://www.gmail.com")
    intialCount = intialCount + 1
