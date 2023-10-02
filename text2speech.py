import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

# Use female voice
engine.setProperty('voice', voice_id)

engine.runAndWait()

rate = engine.getProperty('rate')
engine.setProperty('rate', 190)
engine.say('Akshay kumar')
engine.runAndWait()
 