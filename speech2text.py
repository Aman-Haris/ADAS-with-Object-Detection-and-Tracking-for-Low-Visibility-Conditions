import speech_recognition as sr
r = sr.Recognizer()
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

def SpeakText():
    while(1):
        try:
            with sr.Microphone(device_index=(1)) as source2:
                r.adjust_for_ambient_noise(source2, duration=1)
                print('Waiting for command')
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                SpeakText(MyText)
                print(MyText)
                return MyText
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occured")