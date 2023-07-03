# ROBOSPEAKER

import win32com.client as wincom
# this is a package used to speak for windows

# import time
# you can insert gaps in the narration by adding sleep calls

# if __name__ == '__main__':
    # pass 
print("This is python text-to-speech test using win32com.client")
speak = wincom.Dispatch("SAPI.SpVoice")
text = "Hello and welcome to RoboSpeaker 1.1 created by Ankita Sapnar"
speak.Speak(text)

# now, we'll take input from user
while True:  # for infinite loop
    x = input("Enter what you want me to speak :")
    if x == "quit":  
        speak.Speak("Okay so bye everyone")   #will speak this before ending while loop
        break
    speak.Speak(x)

# let's add 2 seconds of sleep/pause
#     time.sleep(2)
#     text = "This text is read after 3 seconds"
#     speak.Speak(x)
