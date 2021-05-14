import os
from nltk import word_tokenize
import re

files = os.listdir("Data/")

f=open("words.txt","r")
contents= f.readlines()
vocab=[]
for word in contents:
	vocab.append(word[0:-1].lower())
word_set = set(vocab)

def process_files(location,filenames):
	file_to_terms = {}
	for file in filenames:
		pattern = re.compile('[\W_]+')
		name = location+file
		file_to_terms[file] = open(name, 'r').read().lower();
		file_to_terms[file] = pattern.sub(' ',file_to_terms[file])
		re.sub(r'[\W_]+','', file_to_terms[file])
		file_to_terms[file] = file_to_terms[file].split()
	return file_to_terms

listdata=[]
listdata = process_files("Data/",files)
print("storing keywords in dictionary done")

def index_one_file(termlist):
	fileIndex = {}
	for index, word in enumerate(termlist):
		if word in fileIndex.keys():
			fileIndex[word].append(index)
		else:
			fileIndex[word] = [index]
	return fileIndex


def make_indices(termlists):
	total = {}
	for filename in termlists.keys():
		total[filename] = index_one_file(termlists[filename])
	return total

indexwordallfiles=make_indices(listdata)

print("constructing inverted index.")
def fullIndex(regdex):
	total_index = {}
	for filename in regdex.keys():
		for word in regdex[filename].keys():
			if word in total_index.keys():
				if filename in total_index[word].keys():
					total_index[word][filename].extend(regdex[filename][word][:])
				else:
					total_index[word][filename] = regdex[filename][word]
			else:
				total_index[word] = {filename: regdex[filename][word]}
	return total_index

wordindex = fullIndex(indexwordallfiles)

print("now proceeding with the query part")
def one_word_query(word, invertedIndex):
	pattern = re.compile('[\W_]+')
	word = pattern.sub(' ',word)
	if word in invertedIndex.keys():
		return [filename for filename in invertedIndex[word].keys()]
	else:
		return []


def free_text_query(string):
	pattern = re.compile('[\W_]+')
	string = pattern.sub(' ',string.lower())
	result = []
	print(" returning intersection of files")
	for word in string.split():
		result.append(set(one_word_query(word,wordindex)))
	A={}
	A = result[0].intersection(result[1])
	for i in range(1,len(result)-1):
		A = A.intersection(result[i+1])
	return list(A)

#calculating lt which is k/Dt
k=len(files)
dic={}
for item in wordindex:
	k=0
	for fil in wordindex[item]:
		k += (len(wordindex[item][fil]))
	dic[item]=k

print(len(dic))

def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     try:
      v=list(d.values())
      k=list(d.keys())
      value = k[v.index(max(v))]
      return value
     except:
      return

def startQuery(query):
	txt = query
	pattern = re.compile('[\W_]+')
	txt = pattern.sub(' ',txt.lower())
	txtlist = word_tokenize(str(txt))
	print(txtlist)
	toreturn={}
	for f in files:
		toreturn[f]=0
	for item in txtlist:
		listfilename = one_word_query(item,wordindex)
		for t in listfilename:
			toreturn[t] +=1
	num_of_files = len([iq for iq in os.scandir('Data/')])
	for i in range(0,num_of_files):
		tx = keywithmaxval(toreturn)
		print("filename ", tx ," score ", toreturn[tx])
		return tx
		if toreturn[tx] != 0:
			del toreturn[tx]
