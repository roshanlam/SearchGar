import re
from underthesa import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
import numpy as np

class TextProcessing:

    def __init__(self, text):
        self.text = text

    def clean_text(self):
        pattern = pattern = re.compile(r'[^áàảãạâấầẩẫậăẵẳắằặđéèẻẽẹêếềểễệíìịỉĩóòõỏọôốồổộỗơớờởỡợúùũủụưứừửữựýỳỷỹỵ\sa-z_]')
        return re.sub(pattern, ' ', self.text)

    def remove_stopwords(self):
        tokens = [token for token in self.text.split() if token not in stopwords_set]
        return tokens

    def preprocess_text(self):
        nltk_english_words = stopwords.words('english')
        cleaned_text = ""
        for word in self.text.split():
            if word not in nltk_english_words:
                cleaned_text += word + " "
        return cleaned_text