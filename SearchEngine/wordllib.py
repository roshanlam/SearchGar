from nltk.corpus import stopwords

cachedStopWords = stopwords.words("english")

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
