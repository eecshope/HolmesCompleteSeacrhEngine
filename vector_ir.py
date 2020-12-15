import _pickle as pkl
import math

from model import inverted_unit

raw_file = open('./data/chapter_cache.pkl', 'rb')
dictlist = pkl.load(raw_file)
raw_file.close()

dictnum = len(dictlist)
wordbag = set({})
wordnumber = dict({})
for i in range(dictnum):
    for lemma in dictlist[i].tf_count.keys():
        wordbag.add(lemma)
wordbag = list(wordbag)

wordbag_file = open('./data/wordbag_cache.pkl', 'wb')
pkl.dump(wordbag, wordbag_file)
wordbag_file.close()

wordnum = len(wordbag)
inverted_index = list()

for i in range(wordnum):
    wordnumber[wordbag[i]] = i

wordnumber_file = open('./data/wordnumber_cache.pkl', 'wb')
pkl.dump(wordnumber, wordnumber_file)
wordnumber_file.close()

idf = [0 for _ in range(wordnum)]
tfidf = [[0 for _ in range(wordnum)] for __ in range(dictnum)]

for lemma in wordbag:
    doclist = list({})
    for i in range(dictnum):
        if lemma in dictlist[i].tf_count.keys():
            idf[wordnumber[lemma]] += 1
            doclist.append(i)
    inverted_index.append(inverted_unit.InvertedUnit(doclist))

inverted_file = open('./data/inverted_index_cache.pkl', 'wb')
pkl.dump(inverted_index, inverted_file)
inverted_file.close()

for i in range(wordnum):
    idf[i] = math.log((1 + dictnum) / idf[i])

for i in range(dictnum):
    for lemma in dictlist[i].tf_count.keys():
        tfidf[i][wordnumber[lemma]] = dictlist[i].tf_count[lemma] * idf[wordnumber[lemma]]

idf_file = open('./data/idf_cache.pkl', 'wb')
pkl.dump(idf, idf_file)
idf_file.close()

tfidf_file = open('./data/tfidf_cache.pkl', 'wb')
pkl.dump(tfidf, tfidf_file)
tfidf_file.close()
