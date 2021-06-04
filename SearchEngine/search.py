import os, nltk, re
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# from .Index import iIndex

#nltk.download('stopwords')
#nltk.download('punkt')
ps = PorterStemmer()
cachedStopWords = stopwords.words("english")
files = os.listdir("Data/")

vocab = []
with open('words.txt', 'r') as f:
    contents = f.readlines()
    for word in contents:
        vocab.append(word[0:-1].lower())
word_set = set(vocab)

def process_files(dir, filenames):
    file_to_terms = {}
    for file in filenames:
        # Match a string consisting of a single character like letters and numbers
        pattern = re.compile('[\W_]+')
        name = dir + file
        file_to_terms[file] = open(name, 'r').read().lower();
        file_to_terms[file] = pattern.sub(' ', file_to_terms[file])
        re.sub(r'[\W_]+', '', file_to_terms[file])
        file_to_terms[file] = file_to_terms[file].split()
    return file_to_terms

# Storing Keywords in a dict
listdata = process_files("Data/", files)

#
# Input - [word1, word2, word3, word4....]
#
# Output - {word1: [position1, position2],....}
#
def indexFile(wordList):
    fileIndex = {}
    for index, word in enumerate(wordList):
        if word in fileIndex.keys():
            fileIndex[word].append(index)
        else:
            fileIndex[word] = [index]
    return fileIndex


#
# Takes the result of fileToTerms and creates
# a new hashtable (in python it's basically a dict)
# with key of filename and with values which are result of
# the previous function which makes it a nested
# hashtable/dict
#
def make_indices(wordLists):
    total = {}
    for filename in wordLists.keys():
        total[filename] = indexFile(wordLists[filename])
    return total

indexwordallfiles = make_indices(listdata)


# input (indexinfo) = {filename: {word: [position1, position2, position3 ...], ... }}
# result = {word: {filename: [position1, position2, position3]}, ...}, ...}

def InvertedIndex(indexInfo):
    total_index = {}
    for filename in indexInfo.keys():
        for _word in indexInfo[filename].keys():
            if _word in total_index.keys():
                if filename in total_index[_word].keys():
                    total_index[_word][filename].extend(indexInfo[filename][_word][:])
                else:
                    total_index[_word][filename] = indexInfo[filename][_word]
            else:
                total_index[_word] = {filename: indexInfo[filename][_word]}
    return total_index

word_index = InvertedIndex(indexwordallfiles)

def one_word_query(word, invertedIndex):
    pattern = re.compile('[\W_]+')
    word = pattern.sub(' ', word)
    word = ''.join([w for w in word.split() if w not in cachedStopWords])
    if word in invertedIndex.keys():
        #a = [filename for filename in invertedIndex[word].keys()]
        #print(type(a))
        #return a
        return list(invertedIndex[word])
    else:
        return []

# makes sure one of the words in the query appears in the document
def standard_query(query):
    pattern = re.compile('[\W_]+')
    query = pattern.sub(' ', query.lower())
    result = []
    for word in query.split():
        result.append(set(one_word_query(word, word_index)))
    i = len(result)
    # Ensures every word in query shows up in the final list
    A = result[0].intersection(result[i - 1])
    for i in range(1, len(result) - 1):
        A = A.intersection(result[i + 1])
    return list(A)
    #return rankResults(list(set(result)), query)

def rankResults(result, query):
    vector = create_vector(result)
    #query_vector = query_vector(query)
    #results = [[dotProduct(vectors[_result], query_vector), _result] for _result in result]
    results = []
    # sort and return index 0 of the lists element
    results.sort(key = lambda y: y[0])
    results = [y[1] for y in results]
    return results


def execute(self):
    return self.InvertedIndex()

def get_uniques(self):
    return self.execute().keys()

def genScore(term, doc):
    pass

def create_vector(self, docs):
    vector = {}
    for doc in docs:
        docVector = [0] * len(self.get_uniques())
        for i, term in enumerate(self.get_uniques()):
            docVector[i] = self.genScore(term, doc)
        vector[doc] = docVector
    return vector
# Calculating inverse document frequency - the total num of documents divided by the num
# of docs term x shows up in
#             Num. of doc x shows up
# idf = NOD / NODxSU
k = len(files)
dic = {}
for item in word_index:
    k = 0
    for fil in word_index[item]:
        k += (len(word_index[item][fil]))
    dic[item] = k

"""
1. Creates a list of dict's keys and values
2. Returns key with the maxium value
"""
def keywithmaxval(d):
    try:
        v = list(d.values())
        k = list(d.keys())
        value = k[v.index(max(v))]
        return value
    except:
        return

def startQuery(query):
    pattern = re.compile('[\W_]+')
    query = pattern.sub(' ', query.lower())
    txtlist = word_tokenize(str(query))
    txtlist = [word for word in txtlist if not word in stopwords.words('english')]
    toreturn = {}
    for file in files:
        toreturn[file] = 0
    for _item in txtlist:
        #listfilename = one_word_query(_item, word_index)
        listfilename = standard_query(query)
        for t in listfilename:
            toreturn[t] += 1
    # num_of_files = len([iq for iq in os.scandir('Data/')])
    tx = keywithmaxval(toreturn)
    for i in range(1):
        # tx = dict((k, v) for k, v in toreturn.items() if v >= 1)
        # print("filename ", tx, " score ", toreturn[tx])
        print(tx, toreturn[tx])
    return tx