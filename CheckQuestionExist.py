from Script import Branches
from AnswerResponse import ALL_RESPONSE

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



for branch in Branches:
    cheackQuestionExistInDB(branch)

print("NOt Exist:-",notExistQuestion)
print("Not Exist Response:-", notExistResponse)
print("Exist Response:-",existResponse)