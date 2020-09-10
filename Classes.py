import webbrowser
import schedule
import time
import pyautogui
#from selenium import webdriver
#We can use Selenium to do this process much more elegantly, but this is mostly a proof of concept and I couldn't get Selenium working that quickly so I've abandoned that idea.
#If you're looking at this and actually interested in automating joining Google Meets, you should check here: https://pythonspot.com/selenium-click-button/

meetX = 3246   # width 427 height 408
meetY = 576    # These are the coordinates on my machine to click the "Join Meet" button, but you should reconfigure them if you're reusing this.
               # This tool should help: http://breakthrusoftware.com/html/onlinedocs/kb/installkb/ScreenCoordTool.html
               # If for some reason different classes had different join button positions, you could reconfigure the function and the way the URLs are stored so that the object also has the coords

statsUrl = 'https://meet.google.com/lookup/CODE?authuser=1&hs=NUM'
ecoUrl = 'https://meet.google.com/lookup/CODE?authuser=1&hs=NUM'
#potUrl = ''
#calcUrl = ''
walkUrl = 'https://meet.google.com/lookup/CODE?authuser=1&hs=NUM'


webbrowser.register('chrome', # Creating the webdriver
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))       # This should be replaced with a path to your chrome.exe

def joinClass(url): # This is the function, as named, to join the class!
    print ("It's time for class!")
    webbrowser.get('chrome').open(url)
    time.sleep(5) # Maybe the page took some time to load.
    pyautogui.moveTo(meetX, meetY)
    time.sleep(1) # Probably unnecessary.
    pyautogui.click()
    return

# Join Stats every day at 7:45 AM
schedule.every().day.at("07:47").do(joinClass, statsUrl) # You define a class by simply this line, but replacing "07:47" with the time of your class, and statsUrl with your URL.

# Join Ecology every day at 9:33 AM
schedule.every().day.at("09:35").do(joinClass, ecoUrl)

# TODO: Join Pottery every day at 10:34 AM
#schedule.every().day.at("10:34").do(joinClass, potUrl)

# TODO: Join Calculus every day at 1:00 PM (will this work? assumption)
#schedule.every().day.at("13:00").do(joinClass, calcUrl)

# Join Walking every day at 1:54 PM (same question as above)
schedule.every().day.at("13:54").do(joinClass, walkUrl)

# Testing schedule! Change the time a minute past when you're testing, make your own Google Meet on another account to test the button placement. 
schedule.every().day.at("08:55").do(joinClass, "https://meet.google.com/TESTCODE")

while True:
    schedule.run_pending()
    time.sleep(60)