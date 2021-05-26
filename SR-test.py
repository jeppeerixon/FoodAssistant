import speech_recognition

recognizer = speech_recognition.Recognizer()


with speech_recognition.Microphone() as mic:
        print('say something...')
        audio = recognizer.listen(mic)

        try:
            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"I hear {text}")

        except:
            print("Sorry could not hear")
