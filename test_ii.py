# This file is used to test the built inverted index. To run the test, make sure that you've already generate the
# cache files.

import _pickle as pkl
import nltk
from nltk.tokenize import WordPunctTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from model import inverted_unit

raw_file = open('./data/caches/chapter_cache.pkl', 'rb')
dictlist = pkl.load(raw_file)
raw_file.close()

raw_file = open('./data/caches/inverted_index_cache.pkl', 'rb')
inverted_index = pkl.load(raw_file)
raw_file.close()

raw_file = open('./data/caches/wordbag_cache.pkl', 'rb')
wordbag = pkl.load(raw_file)
raw_file.close()

raw_file = open('./data/caches/paragraph_cache.pkl', 'rb')
paralist = pkl.load(raw_file)
raw_file.close()


raw_file = open('./data/caches/wordnumber_cache.pkl', 'rb')
wordnumber = pkl.load(raw_file)
raw_file.close()

calc_index = list()
for i in range(len(dictlist)):
	calc_index.append(len(dictlist[i].text))	#calculate the index in paralist
#print(calc_index)
#print(len(paralist))

word = input()
try:
    #print(len(wordbag))
    #print(len(inverted_index))
    #print(wordnumber[word])
    #print(len(inverted_index[wordnumber[word]]))
    for i in range(len(inverted_index[wordnumber[word]])):
        print(inverted_index[wordnumber[word]][i].chapter_index)
        print(inverted_index[wordnumber[word]][i].paragraph_index)
        #print(inverted_index[wordnumber[word]][i].position)
        for j in range(len(inverted_index[wordnumber[word]][i].position)):
            print(paralist[sum(calc_index[:inverted_index[wordnumber[word]][i].chapter_index])+inverted_index[wordnumber[word]][i].paragraph_index].sentences[inverted_index[wordnumber[word]][i].position[j]])
except KeyError:
    print("This is not an archived lemma")


