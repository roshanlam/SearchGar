import re
from underthesa import word_tokenize

class TextProcessing:
    def __init__(self):
        pass

    def clean_text(self, text):
        pattern = pattern = re.compile(r'[^áàảãạâấầẩẫậăẵẳắằặđéèẻẽẹêếềểễệíìịỉĩóòõỏọôốồổộỗơớờởỡợúùũủụưứừửữựýỳỷỹỵ\sa-z_]')
        return re.sub(pattern, ' ', text)

    def remove_stopwords(self, text, stopwords_set):
        tokens = [token for token in text.split() if token not in stopwords_set]
        return tokens

    def preprocess_text(self, text, stopwords_set):
        processed_text = word_tokenize(text, format='text')
        processed_text = processed_text.lower()
        processed_text = clean_text(processed_text)
        tokens = remove_stopwords(processed_text, stopwords_set)
        tokens = [remove_accents(token) for token in tokens]
        return tokens