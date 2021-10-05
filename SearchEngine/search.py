import os
import re
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt')
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
        pattern = re.compile('[\W_]+')
        name = dir + file
        file_to_terms[file] = open(name, 'r').read().lower();
        file_to_terms[file] = pattern.sub(' ', file_to_terms[file])
        re.sub(r'[\W_]+', '', file_to_terms[file])
        file_to_terms[file] = file_to_terms[file].split()
    return file_to_terms

listdata = process_files("Data/", files)

def indexFile(wordList):
    file_index = {}
    for index, word in enumerate(wordList):
        if word in file_index.keys():
            file_index[word].append(index)
        else:
            file_index[word] = [index]
    return file_index


def make_indices(wordLists):
    total = {}
    for filename in wordLists.keys():
        total[filename] = indexFile(wordLists[filename])
    return total

indexwordallfiles = make_indices(listdata)


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
        return list(invertedIndex[word])
    else:
        return []

def standard_query(query):
    pattern = re.compile('[\W_]+')
    query = pattern.sub(' ', query.lower())
    result = []
    for word in query.split():
        result.append(set(one_word_query(word, word_index)))
    i = len(result)
    A = result[0].intersection(result[i - 1])
    for i in range(1, len(result) - 1):
        A = A.intersection(result[i + 1])
    return list(A)

def rankResults(result, query):
    vector = create_vector(result)
    results = []
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

k = len(files)
dic = {}
for item in word_index:
    k = 0
    for fil in word_index[item]:
        k += (len(word_index[item][fil]))
    dic[item] = k

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
    from .query import Query
    q = Query()
    listfilename = q.phrase_query(query)
    print(listfilename)
    return listfilename
