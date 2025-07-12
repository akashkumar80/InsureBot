import speech_recognition as sr


allChatHistoryOfUser = []

class voice_to_text:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()


    def take_speech_input(self):
        with self.microphone as source:
            print("🎤 Listening...")
            try:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source,timeout=3)
                print("🔍 Recognizing...")
                text = self.recognizer.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                print("Can you Repeat")
                return None
            except sr.RequestError as e:
                print("Please try to change internet")
                return None
            except sr.WaitTimeoutError:
                return None
            except Exception as e:
                print("error:-",e)
                return None