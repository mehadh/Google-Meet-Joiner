import webbrowser
import schedule
import time
import pyautogui
import os

#from selenium import webdriver
#We can use Selenium to do this process much more elegantly, but this is mostly a proof of concept and I couldn't get Selenium working that quickly so I've abandoned that idea.
#If you're looking at this and actually interested in automating joining Google Meets, you should check here: https://pythonspot.com/selenium-click-button/

meetX = 3246   # width 427 height 408
meetY = 576    # These are the coordinates on my machine to click the "Join Meet" button, but you should reconfigure them if you're reusing this.
               # This tool should help: http://breakthrusoftware.com/html/onlinedocs/kb/installkb/ScreenCoordTool.html
               # If for some reason different classes had different join button positions, you could reconfigure the function and the way the URLs are stored so that the object also has the coords
               # {X=3210,Y=583,Width=427,Height=408} this is a coord on the join button when there's a present button

meet2X = 3214 # New! This is to avoid not being logged into the meeting due to mismatched button placement. FIrst the script clicks the first position, then it clicks this one.
meet2Y = 583    # So, define these coords when you see two buttons, the present and the join button.

# I've added a virtual webcam to my setup, but I only want it for one class, so I've now decided to define where the button is to turn off the camera in other cases.
# {X=2678,Y=712,Width=427,Height=408}

cameraX = 2678
cameraY = 712

statsUrl = 'https://meet.google.com/lookup/gjftx4nhwq?authuser=1&hs=179'
ecoUrl = 'https://meet.google.com/lookup/br2ozwm7ey?authuser=1&hs=179'
#potUrl = ''
#calcUrl = ''
walkUrl = 'https://meet.google.com/lookup/d6tzj5ljdi?authuser=1&hs=179'


webbrowser.register('chrome', # Creating the webdriver
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))       # This should be replaced with a path to your chrome.exe

def joinClass(url): # This is the function, as named, to join the class!
    print ("It's time for class!")
    webbrowser.get('chrome').open(url)
    time.sleep(5) # Maybe the page took some time to load.
    if (url != walkUrl):    # For me, I only want my camera (a ManyCam virtual webcam) enabled during my Walking class, so for every other class, the camera is turned off.
        pyautogui.moveTo(cameraX, cameraY)
        time.sleep(1)
        pyautogui.click()
    pyautogui.moveTo(meetX, meetY)
    time.sleep(1) # Probably unnecessary.
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(meet2X, meet2Y) #{X=3214,Y=576,Width=427,Height=408}
    time.sleep(1)
    pyautogui.click()
    return

def leaveClass():
    print("It's time to leave class!")
    pyautogui.hotkey('ctrlleft', 'w')

def initCam():
    print("Starting the webcam!")
    os.system('"C://Users/Temporary User/Downloads/webcamoid/bin/webcamoid.exe"')

def killCam():
    print("Killing the webcam!")
    os.system("taskkill /im webcamoid.exe")

# Join Stats every day at 7:45 AM
schedule.every().day.at("07:45").do(joinClass, statsUrl) # You define a class by simply this line, but replacing "07:47" with the time of your class, and statsUrl with your URL.

# I don't know when this teacher likes to end class, so I'll set it around the official ending time. It might be earlier though. A bit of a give away, but not much we can do yet.
# I'll try to find out if I can get info off of the page for when people start leaving, but this is tricky because you don't really know when to leave since usually the teacher leaves last.

schedule.every().day.at("08:35").do(leaveClass)

# Join Ecology every day at 9:33 AM
schedule.every().day.at("09:33").do(joinClass, ecoUrl)

# I'm usually in this class physically, but I'll set a leave for this anyways.

schedule.every().day.at("10:28").do(leaveClass)

# TODO: Join Pottery every day at 10:34 AM
#schedule.every().day.at("10:34").do(joinClass, potUrl)

# TODO: Leave Pottery every day.
#schedule.every().day.at("11:24").do(leaveClass)

# TODO: Join Calculus every day at 1:00 PM 
#schedule.every().day.at("13:00").do(joinClass, calcUrl)

# I need to rewrite this part since Calculus is using Zoom :/ Luckily it's not mandatory to meet in that class so I'll be fine.

# Before walking, initialize the fake webcam
schedule.every().day.at("13:52").do(initCam)

# Join Walking every day at 1:54 PM 
schedule.every().day.at("13:54").do(joinClass, walkUrl)

# Walking is usually pretty quick, probably 10 minutes, but I'll set it to leave after 15 and hope that it gets it right.

schedule.every().day.at("14:09").do(leaveClass)

schedule.every().day.at("14:10").do(killCam)

# Testing schedule! Change the time a minute past when you're testing, make your own Google Meet on another account to test the button placement. 
#schedule.every().day.at("08:55").do(joinClass, "https://meet.google.com/code")

while True:
    schedule.run_pending()
    time.sleep(60)