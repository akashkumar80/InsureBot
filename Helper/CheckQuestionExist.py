from TrainingData.Script import Branches
from TrainingData.AnswerResponse import ALL_RESPONSE

notExistQuestion= []
notExistResponse = []
existResponse=[]

def cheackQuestionExistInDB(data):
    if data["AIResponse"] not in ALL_RESPONSE:
        notExistQuestion.append(data["AIResponse"])
    else:
        for key in list(data["response"].keys()):
            if key not in list(ALL_RESPONSE[data["AIResponse"]].keys()):
                notExistResponse.append(key)
                existResponse.append(data["AIResponse"])
    if "instantResponse" in data["response"]:
        return
    for res in data["response"]:
        if isinstance(data["response"][res], int):
            continue
        cheackQuestionExistInDB(data["response"][res])


def checkDB(Branch):
    for branch in Branches:
        cheackQuestionExistInDB(branch)

    if len(notExistQuestion)> 0:
        print("There is missing question in AnswerResponse Data:-", notExistQuestion)
        return False

    if len(notExistResponse)> 0:
        print("There is something missing in AnswerResponse Data:-", notExistResponse)
        return False

    return True