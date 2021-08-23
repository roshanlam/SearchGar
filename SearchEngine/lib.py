from datetime import datetime
import json
import codecs
from os import remove
import requests
from bs4 import BeautifulSoup
import pathlib
from sklearn.feature_extraction.text import TfidfVectorizer
#from gensim.parsing.preprocessing import remove_stopwords

class Preprocessing:
    def __init__(self, txt):
        nltk.download('punkt')
        tokens = nltk.sent_tokenize(txt)
        self.tokens = tokens
        self.tfidfvectoriser = TfidfVectorizer()
        
    def clean_sentence(self, sentence, stopwords=False):
        sentence = sentence.lower().strip()
        sentence = re.sub(r'[^a-z0-9\s]', '', sentence)
        if stopwords:
            sentence = remove_stopwords(sentence)
        return sentence
    
    def get_cleaned_sentences(self, tokens, stopwords=False):
        cleaned_sentences = []
        for line in tokens:
            cleaned = self.clean_sentence(line, stopwords)
            cleaned_sentences.append(cleaned)
        return cleaned_sentences
    
    def cleanall(self):
        cleaned_sentences = self.get_cleaned_sentences(self.tokens, stopwords=True)
        cleaned_sentences_with_stopwords = self.get_cleaned_sentences(self.tokens, stopwords=False)
        return [cleaned_sentences, cleaned_sentences_with_stopwords]
    
    def TFIDF(self, clean_sentences):
        self.tfidfvectoriser.fit(clean_sentences)
        tfidf_vectors = self.tfidfvectoriser.transform(clean_sentences)
        return tfidf_vectors
    
    def doall(self):
        cleaned_sentences, cleaned_sentences_with_stopwords = self.cleanall()
        tfidf = self.TFIDF(cleaned_sentences)
        return [cleaned_sentences, cleaned_sentences_with_stopwords, tfidf]

def crawl(url, filename):
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        print('Failed to perform HTTP GET request on "%s"\n' % url)
        return
    website = BeautifulSoup(response.text, 'lxml')
    try:
        title = website.find('title').text
        paragraph = ''
        h1 = ''
        h2 = ''
        h3 = ''
        a = ''
        div = ''
        for tag in website.findAll():
            if tag.name == 'p':
                paragraph += tag.text.strip().replace('\n', '')
            if tag.name == 'h1':
                h1 += tag.text.strip().replace('\n', '')
            if tag.name == 'h2':
                h2 += tag.text.strip().replace('\n', '')
            if tag.name == 'h3':
                h3 += tag.text.strip().replace('\n', '')

            if tag.name == 'a':
                a += tag.text.strip().replace('\n', '')
            if tag.name == 'div':
                div += tag.text.strip().replace('\n', '')
        result = {
            'url': url,
            'title': title,
            'paragraph': paragraph,
            'header1': h1,
            'header2': h2,
            'header3': h3,
            'a': a,
            'div': div
        }
    except ValueError:
        if len(result) == 0:
            raise ValueError('Crawl info is empty')
        else:
            raise ValueError('Something is wrong, it is related to value error')
    return result.values()

def saveInfo(folder, filename, info):
    try:
        folder = pathlib.Path("{}".format(folder))
        folder.mkdir(parents=True)
        filename = "{}.txt".format(filename)
        folder = pathlib.Path("{}".format(folder))
        filename = "{}.txt".format(filename)
        filepath = folder / filename
        with filepath.open("w+") as f:
            f.write(str(info))
    except FileExistsError:
        folder = pathlib.Path("{}".format(folder))
        filename = "{}.txt".format(filename)
        filepath = folder / filename
        with filepath.open("w+") as f:
            f.write(str(info))

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def saveQueryData(query, ip_address):
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    filename = ip_address
    with open(filename + '_search' + '.json', 'a+') as f:
        data = {
            ip_address: [{
                'Query': query,
                'Time': time
            }]
        }
        json.dump(data, f, indent=4, sort_keys=True)

def saveCrawlData(url, website_name, ip_address):
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    filename = ip_address
    with open(filename + '_crawl' + '.json', 'a+') as f:
        data = {
            ip_address: [{
                'Website Url': url,
                'Website Name': website_name,
                'Time': time
            }]
        }
        json.dump(data, f, indent=4, sort_keys=True)

def readFile(path, encoding='utf-8'):
    with codecs.open(path, 'r', encoding=encoding) as f:
        try:
            content = f.read()
        except UnicodeDecodeError as e:
            raise Exception("%s: %s" % (e, path))
    return content

class Colors:
    def __init__(self):
        self.HEADER = '\033[95m'
        self.OKBLUE = '\033[94m'
        self.OKCYAN = '\033[96m'
        self.OKGREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'