import whisper
import os

class voiceToText:
    def __init__(self):
        self.model= whisper.load_model("base")

    def voiceToText(self, filePath: str, language: str="hi"):
        result = self.model.transcribe(filePath,language=language)
        return result["text"]

def main(audioFolder):
    voiceToTextObj= voiceToText()
    files = os.listdir(audioFolder)
    os.makedirs("training_text", exist_ok=True)

    for fileName in files:
        fullpath = os.path.join(audioFolder, fileName)
        transcript = voiceToTextObj.voiceToText(fullpath)
        
        baseFileName = os.path.join("training_text",os.path.split(fileName)[0]+".txt")
        with open(baseFileName, "w", encoding="utf-8") as f:
            f.write(transcript)
        print(baseFileName," Generated Successfully")

if __name__ == "__main__":
    audio_folder = "Voices_Data/AudioFile"
    main(audio_folder)