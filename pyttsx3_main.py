import pyttsx3

if __name__ == '__main__':
    engine = pyttsx3.init(driverName='sapi5')

    voices = engine.getProperty('voices')
    # for voice in voices:
    #     print(voice.id)
    #     engine.setProperty('voice', voice.id)
    #     engine.say("I am Atar-hat")
    #     engine.runAndWait()

    engine.setProperty('voice', voices[0].id)
    engine.say("I am Atar-hat")
    engine.runAndWait()
