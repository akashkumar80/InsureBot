import speech_recognition as sr

class voice_to_text:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def take_speech_input(self):
        with sr.Microphone() as source:
            print("🎤 Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

            try:
                print("🔍 Recognizing...")
                text = self.recognizer.recognize_google(audio)
                print("✅ You said:", text)
                return text
            except sr.UnknownValueError:
                print("Can you Repeat")
            except sr.RequestError as e:
                print("Please try to change internet")
            return None
