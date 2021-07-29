import math
import numpy as np
import nltk 
import re
import genism
from genism.parsing.preprocessing import remove_stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import heapq

class TS_SS:
    
    def cosine_similarity(self, vector1, vector2):
        dotProduct = np.dot(vector1, vector2.T)
        denominator = (np.linalg.norm(vector1) * np.linalg.norm(vector2))
        return dotProduct/denominator
    
    def euclidean_distance(self, vector1, vector2):
        vec1 = vector1.copy()
        vec2 = vector2.copy()
        if len(vec1) < len(vec2): vec1, vec2 = vec1, vec2
        vec2 = np.resize(vec2, (vec1.shape[0], vec1.shape[1]))
        return np.linalg.norm(vec1 - vec2)
    
    def theta(self, vector1, vector2):
        return np.arccos(self.cosine_similarity(vector1, vector2)) + np.radians(10)
    
    def triangle(self, vector1, vector2):
        theta = np.radians(self.theta(vector1, vector2))
        return ((np.linalg.norm(vector1) * np.linalg.norm(vector2)) * np.sin(theta)) / 2
    
    def magnitude_difference(self, vec1, vec2):
        return abs((np.linalg.norm(vec1) - np.linalg.norm(vec2)))
    
    def sector(self, vector1, vector2):
        ed = self.euclidean_distance(vector1, vector2)
        md = self.magnitude_difference(vector1, vector2)
        theta = self.theta(vector1, vector2)
        return math.pi * (ed + md) ** 2 * theta / 360
    
    def __call__(self, vector1, vector2, method):
        if method == 1: return self.euclidean_distance(vector1, vector2)
        elif method == 2: return self.cosine_similarity(vector1, vector2)
        else: return self.triangle(vector1, vector2) * self.sector(vector1, vector2)
    
    def RetrieveAnswer(question_embedding, tfidf_vectors,method=1):
        similarity_heap = []
        if method==1: max_similarity = float('inf')
        else: max_similarity = -1
        index_similarity = -1

        for index, embedding in enumerate(tfidf_vectors):  
            find_similarity = TS_SS()
            similarity = find_similarity((question_embedding).toarray(),(embedding).toarray(),method).mean()
            if method==1:
                heapq.heappush(similarity_heap,(similarity,index))
            elif method==2:
                heapq.heappush(similarity_heap,(-similarity,index))
            else:
                heapq.heappush(similarity_heap,(similarity,index))
        return similarity_heap
