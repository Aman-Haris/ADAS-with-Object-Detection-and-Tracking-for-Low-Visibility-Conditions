import dot
import sys
import speech_recognition as sr
import pyttsx3
import dateweather
r = sr.Recognizer()
engine = pyttsx3.init()
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', voice_id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 190)

dot
while(1):
    try:
         with sr.Microphone(device_index=(1)) as source2:
             r.adjust_for_ambient_noise(source2, duration=1)
             print('Waiting for command')
             audio2 = r.listen(source2)
             command = r.recognize_google(audio2)
             command = command.lower()
             print(command)
             if (command == 'start'):
                 detstat = dateweather.detstatus()
                 engine.say("welcome user")
                 engine.say("Today's weather forecast is" + detstat)
                 engine.runAndWait()
                 dot.dot(0)
                 #if (command == 'exit'):
                     #sys.exit("Program has ended")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")


