import _pickle as pkl
from model import inverted_unit

raw_file = open('./data/inverted_index_cache.pkl','rb')
inverted_index = pkl.load(raw_file)
raw_file.close()

raw_file = open('./data/wordbag_cache.pkl','rb')
wordbag = pkl.load(raw_file)
raw_file.close()

raw_file = open('./data/wordnumber_cache.pkl','rb')
wordnumber = pkl.load(raw_file)
raw_file.close()

word = input()
print(inverted_index[wordnumber[word]].doclist)


