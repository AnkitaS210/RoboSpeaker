# PROJECT 01: ROBOSPEAKER

# modules to be installed""
# 1. pip install pywin32 (installing name) and import by name "win32com.client"

import win32com.client as wincom
# this is a package used to speak for windows

# import time
# you can insert gaps in the narration by adding sleep calls

# if __name__ == '__main__':
    # pass 
# pass is a keyword which is used so that if we want to not write anything at this moment in the'if statement' then we can use 'pass' as it allows us to go ahead without throwing any error and allows to write anything afterwards.

print("This is python text-to-speech test using win32com.client")
speak = wincom.Dispatch("SAPI.SpVoice")
text = "Hello and welcome to RoboSpeaker 1.1 created by Ankita Sapnar"
speak.Speak(text)
# In this, 'Speak' is a method used with the 'SAPI.SpVoice' object and this method is called with the text "Hello and welcome to RoboSpeaker 1.1 created by Ankita Sapnar", and the 'speak' is a object which converts this text into audible speech for windows as for mac it is 'say'

# now, we'll take input from user
while True:  # this is used for infinite loop
    x = input("Enter what you want me to speak :")
    if x == "quit":   #here we can put any string which we want to break/stop this infinite while loop
        speak.Speak("Okay so bye everyone")   #it will speak this before ending while loop
        break
    speak.Speak(x)

# let's add 2 seconds of sleep/pause
#     time.sleep(2)
#     text = "This text is read after 3 seconds"
#     speak.Speak(x)


# Go to this website to know more about text to speech: https: // www.codesofinterest.com / 2020 / 05 / text - to - speech - windows - 10 - pywin32.html