# Google-Meet-Joiner
Automatically join Google Meet classes with ease!

This is a simple project I made to combat the mandatory checking in of online classes as a result of the COVID-19 Pandemic. This method is not fool proof, as hosts may ask for you to type in chat to mark your attendance, to speak, or to have your web cam on, however there are ways around all of those, such as programming the chat input via this script, playing an audio file through a virtual audio cable, or using a virtual webcam loop. Still, this should work for classes if there are no other requirements other than to join. 

You can define new classes like this:
```python
mathUrl = 'https://meet.google.com/lookup/xxxxxxxx?authuser=1&hs=xxx'
schedule.every().day.at("01:23").do(joinClass, mathUrl)
```
This code will join mathUrl at 1:23 AM. If you have multiple Google accounts, "authuser=1" is what changes which Google account you are using on the link. This is mainly to be used for Google Classroom linked Google Meets because they have a static link assigned to them to look up the current meeting. 


If you frequently encounter the error in which there is a present button, replace the joinClass function with this:

```python
def joinClass(url): # This is the function, as named, to join the class!
    print ("It's time for class!")
    webbrowser.get('chrome').open(url)
    time.sleep(5) # Maybe the page took some time to load.
    pyautogui.moveTo(meetX, meetY)
    time.sleep(1) # Probably unnecessary.
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(meet2X, meet2Y) #{X=3214,Y=576,Width=427,Height=408}
    time.sleep(1)
    pyautogui.click()
    return
```

And of course, define meet2X and meet2Y to be the secondary button position. This way, it'll click both. I didn't want to include this in the main fix since it's not applicable for everyone (I didn't start having this issue until a couple days in) but it is a working fix!
