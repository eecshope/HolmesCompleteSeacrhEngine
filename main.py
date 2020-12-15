import _pickle as pkl

import numpy as np

from model import query

raw_file = open('./data/chapter_cache.pkl', 'rb')
dictlist = pkl.load(raw_file)
raw_file.close()
dictnum = len(dictlist)

raw_file = open('./data/wordbag_cache.pkl', 'rb')
wordbag = pkl.load(raw_file)
raw_file.close()
wordnum = len(wordbag)

raw_file = open('./data/wordnumber_cache.pkl', 'rb')
wordnumber = pkl.load(raw_file)
raw_file.close()

raw_file = open('./data/idf_cache.pkl', 'rb')
idf = pkl.load(raw_file)
raw_file.close()

raw_file = open('./data/tfidf_cache.pkl', 'rb')
tfidf = pkl.load(raw_file)
raw_file.close()


def cosine_similarity(x, y):
    num = x.dot(y.T)
    denom = np.linalg.norm(x) * np.linalg.norm(y)
    return num / denom


def handle_request(local_str_query, k):
    q = query.Query(local_str_query)
    q_tfidf = [0] * wordnum
    for lemma in q.tf_count.keys():
        if lemma in wordbag:
            q_tfidf[wordnumber[lemma]] = q.tf_count[lemma] * idf[wordnumber[lemma]]

    res = [[0, 0] for _ in range(dictnum)]
    for i in range(dictnum):
        res[i][0] = cosine_similarity(np.array(q_tfidf), np.array(tfidf[i]))
        res[i][1] = i

    res = sorted(res, key=(lambda x: x[0]), reverse=True)
    for i in range(k):
        print(dictlist[res[i][1]].story + " " + dictlist[res[i][1]].part + " " + dictlist[res[i][1]].chapter)


str_query = input()
handle_request(str_query, 5)
