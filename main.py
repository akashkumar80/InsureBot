from TrainingData.Script import Branches
from Helper.voiceRecognize import voice_to_text
import pyttsx3
from TrainingData.AnswerResponse import ALL_RESPONSE
from Helper.Similarity import Similarity
from Helper.CheckQuestionExist import checkDB
import os

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)    
    engine.setProperty('volume', 1.0) 

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def return_response_key(branch, response_history):
    data = Branches[branch]
    for res in response_history:
        data= data["response"][res]
    return data["response"].keys()


def return_AIResponse(branch, res_history):
    global current_branch
    global response_history
    data = Branches[branch]
    for i in range(len(res_history)-1):
        data= data["response"][res_history[i]]
    if "instantResponse" in data["response"]:
        if isinstance(data["response"]["instantResponse"],int):
            current_branch=data["response"]["instantResponse"]
            response_history=[]
            return data["AIResponse"]
        elif data["response"]["instantResponse"]==False:
            return False
    if len(res_history)>0:
        data = data["response"][res_history[-1]]
    if isinstance(data, int):
        current_branch=data
        response_history=[]
        return return_AIResponse(current_branch, response_history)
    elif "instantResponse" in data["response"]:
        if isinstance(data["response"]["instantResponse"],int):
            current_branch=data["response"]["instantResponse"]
            response_history=[]
            return data["AIResponse"]
        elif data["response"]["instantResponse"]==False:
            return False
    else:
        return data["AIResponse"]

def main():
    os.makedirs("ModelTrainData", exist_ok=True)
    with open("ModelTrainData/textData.txt", "a") as file:
        file.write("\n{\n")
        if checkDB(Branches) is False:
            return
        global current_branch
        global response_history
        current_branch=0
        response_history = []
        while True:
            AIResponse= return_AIResponse(current_branch,response_history)
            file.write(f"AI:-{AIResponse}\n")
            print("AIResponse:-", AIResponse)
            FindSimilairty.generateSimilarityCosine(AIResponse)
            speak(AIResponse)
            if current_branch is False:
                break
            allPossibleAnswer = list(return_response_key(current_branch, response_history))
            print(allPossibleAnswer)
            voice_input = voice_to_text_input.take_speech_input()
            while voice_input is None:
                speak("Sir/Mam can you repeat yourself")
                voice_input = voice_to_text_input.take_speech_input()
                print(voice_input)
            print("voice input")
            file.write(f"User:-{voice_input}\n")
            response_result = FindSimilairty.findSimilarity(voice_input)
            response_history.append(response_result)
        file.write("}\n")
        print("Finished")


    
current_branch =0
response_history = []
voice_to_text_input = voice_to_text()
if __name__== "__main__":
    FindSimilairty = Similarity()
    main()