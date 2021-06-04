from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

cachedStopWords = stopwords.words("english")

def iIndex(info):
    line = 1
    for word in info:
        if word == '\n':
            line += 1
    array = [info]
    punctuation = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for r in info:
        if r in punctuation:
            info = info.replace(r, " ")


    for _ in range(1):
        textToTokens = word_tokenize(info)

    tokens = [word for word in textToTokens if not word in stopwords.words()]
    index = {}
    for i in range(line):
        check = array[i].lower()
        for item in tokens:
            if item in check:
                if item not in index:
                    index[item] = []
                if item in index:
                    index[item].append(i + 1)

    return index


def word_split(text):
    word_list = []
    wcurrent = []
    windex = None
    for i, c in enumerate(text):
        if c.isalnum():
            wcurrent.append(c)
            windex = i
        elif wcurrent:
            word = u''.join(wcurrent)
            word_list.append((windex - len(word) + 1, word))
            wcurrent = []
    if wcurrent:
        word = u''.join(wcurrent)
        word_list.append((windex - len(word) + 1, word))
    return word_list

def words_cleanup(words):
    cleaned_words = []
    for index, word in words:
        word = ''.join([word for word in words.split() if word not in cachedStopWords])
        cleaned_words.append((index, word))
    return cleaned_words

def words_normalize(words):
    normalized_words = []
    for index, word in words:
        wnormalized = word.lower()
        normalized_words.append((index, wnormalized))
    return normalized_words


def word_index(text):
    words = word_split(text)
    return words

def inverted_index(text):
    inverted = {}
    for index, word in word_index(text):
        pass
    return inverted