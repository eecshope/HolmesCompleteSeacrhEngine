# This file is used to test the built inverted index. To run the test, make sure that you've already generate the
# cache files.

import _pickle as pkl
from model import inverted_unit

raw_file = open('./data/caches/inverted_index_cache.pkl', 'rb')
inverted_index = pkl.load(raw_file)
raw_file.close()

raw_file = open('./data/caches/wordbag_cache.pkl', 'rb')
wordbag = pkl.load(raw_file)
raw_file.close()

raw_file = open('./data/caches/wordnumber_cache.pkl', 'rb')
wordnumber = pkl.load(raw_file)
raw_file.close()

word = input()
try:
    print(inverted_index[wordnumber[word]].doclist)
except KeyError:
    print("This is not an archived lemma")


