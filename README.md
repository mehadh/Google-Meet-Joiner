# Classes.py vs Classes2.py

I've decided to split this project into two files. Classes.py is the original file, it can join classes on its own, and it can turn off your webcam for you. You can easily add microphone disable capabilities if needed, however most calls do this automatically, for my own use case my microphone would be off by hardware anyways.

Classes2.py is more the "all-in" set up. It has a leaveClass function which can leave the meeting at a certain time, but it also initializes and kills [webcamoid](https://github.com/webcamoid/webcamoid), which I use to project a fake live video feed of myself. I find that webcamoid is easier to automate than ManyCam, uses less resources, and has a much cleaner startup and shutdown process. Classes2 will be the file I push most updates to, but I'll keep Classes.py incase someone just wants to join meets automatically.


# Google-Meet-Joiner
Automatically join Google Meet classes with ease!

This is a simple project I made to combat the mandatory checking in of online classes as a result of the COVID-19 Pandemic. This method is not fool proof, as hosts may ask for you to type in chat to mark your attendance, to speak, or to have your web cam on, however there are ways around all of those, such as programming the chat input via this script, playing an audio file through a virtual audio cable, or using a virtual webcam loop. Still, this should work for classes if there are no other requirements other than to join. 

You can define new classes like this:
```python
mathUrl = 'https://meet.google.com/lookup/xxxxxxxx?authuser=1&hs=xxx'
schedule.every().day.at("01:23").do(joinClass, mathUrl)
```
This code will join mathUrl at 1:23 AM. If you have multiple Google accounts, "authuser=1" is what changes which Google account you are using on the link. This is mainly to be used for Google Classroom linked Google Meets because they have a static link assigned to them to look up the current meeting. 

I've added an extra click so that it will join regardless of if there is a present option or not. Furthermore, I've added code to add the possibility of turning off your webcam. I don't have a webcam myself so I didn't need this, but I've started using ManyCam so I've decided to add that feature in. Currently, I have my webcam stay on during one Google Meet, and turn off during the rest of them, however you can modify this to however you see fit.
