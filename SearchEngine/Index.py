from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

cachedStopWords = stopwords.words("english")

def iIndex(file):
    file = open(file, encoding='utf8')
    info = file.read()
    file.seek(0)

    line = 1
    for word in info:
        if word == '\n':
            line += 1
    array = [info]
    punctuation = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for r in info:
        if r in punctuation:
            info = info.replace(r, " ")

    textToTokens = ''
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

print(iIndex('../Data/roshanlamichhane.tech.txt'))

