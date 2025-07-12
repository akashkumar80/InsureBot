from TrainingData.AnswerResponse import ALL_RESPONSE
from sentence_transformers import SentenceTransformer, util

# def findSimilarity(question, query):
#     response_key = []
#     maxSimilarityResponse = []
#     for res in ALL_RESPONSE[question]:
#         response_key.append(res)
#         corpus_embedding = Similarity_Cosine_Model.encode(ALL_RESPONSE[question][res], convert_to_tensor = True)
#         query_embedding = Similarity_Cosine_Model.encode(query, convert_to_tensor = True)

#         cosineSimilarity = util.cos_sim(query_embedding,corpus_embedding)
#         maxSimilarityResponse.append(max(cosineSimilarity[0]))
#     maxIndex = 0
#     maxValue =  maxSimilarityResponse[0]

#     for i in range(len(maxSimilarityResponse)):
#         if maxSimilarityResponse[i]>maxValue:
#             maxIndex = i
#     return response_key[maxIndex]


class Similarity:
    def __init__(self):
        self.Similarity_Cosine_Model = SentenceTransformer('all-mpnet-base-v2')
        self.response_key=[]
        self.maxSimilarityResponse= []
        self.corpus_embedding = []

    def generateSimilarityCosine(self,question):
        self.corpus_embedding = []
        self.response_key=[]
        for res in ALL_RESPONSE[question]:
            self.response_key.append(res)
            self.corpus_embedding.append(self.Similarity_Cosine_Model.encode(ALL_RESPONSE[question][res], convert_to_tensor = True))
        
    
    def findSimilarity(self,query):
        maxSimilarityResponse = []
        query_Embedding = self.Similarity_Cosine_Model.encode(query, convert_to_tensor=True)
        for corp_emb in self.corpus_embedding:
            cosineSimilarity = util.cos_sim(query_Embedding,corp_emb)
            maxSimilarityResponse.append(max(cosineSimilarity[0]))
        maxIndex = 0
        maxValue = maxSimilarityResponse[0]

        for i in range(len(maxSimilarityResponse)):
            if maxSimilarityResponse[i]>maxValue:
                maxIndex = i
        return self.response_key[maxIndex]