import _pickle as pkl
from model import query

raw_file = open('./data/caches/chapter_cache.pkl', 'rb')
dictlist = pkl.load(raw_file)
raw_file.close()

calc_index = list()
for i in range(len(dictlist)):
	calc_index.append(len(dictlist[i].text))	#calculate the index in paralist

raw_file = open('./data/caches/paragraph_cache.pkl','rb')
paralist = pkl.load(raw_file)
raw_file.close()

raw_file = open('./data/caches/wordbag_cache.pkl', 'rb')
wordbag = pkl.load(raw_file)
raw_file.close()

raw_file = open('./data/caches/inverted_index_cache.pkl','rb')
inverted_index = pkl.load(raw_file)
raw_file.close()

raw_file = open('./data/caches/wordnumber_cache.pkl', 'rb')
wordnumber = pkl.load(raw_file)
raw_file.close()

paranum = len(paralist)

words = [0 for _ in range(paranum)]
kinds = [0 for _ in range(paranum)]

alpha = 0.5 #weight of number of key words presented in paragraph

def Para_index(i,j):
	return sum(calc_index[:i])+j

def handle_request(local_str_query, k):
	q = query.Query(local_str_query)
	res = [[0,i] for i in range(paranum)]
	highlight = []
	for lemma in q.tf_count.keys():
		if lemma in wordbag:
			for i in range(len(inverted_index[wordnumber[lemma]])):
				index = Para_index(inverted_index[wordnumber[lemma]][i].chapter_index,inverted_index[wordnumber[lemma]][i].paragraph_index)
				words[index] += len(inverted_index[wordnumber[lemma]][i].position)
				kinds[index] += 1;
			highlight.append(lemma)


	for i in range(paranum):
		res[i][0] = alpha*words[i]+(1-alpha)*kinds[i]
	res = sorted(res, key=(lambda x: x[0]), reverse=True)
	print(words[res[0][1]],kinds[res[0][1]])
	print("most relevanted paragraph: "+"chapter: "+str(paralist[res[0][1]].chapter_index)+" paragraph: "+str(paralist[res[0][1]].index))
	#print(dictlist[paralist[res[0][1]].chapter_index].text[paralist[res[0][1]].index])
	for i in range(len(paralist[res[0][1]].lemmas)):
		for j in range(len(paralist[res[0][1]].lemmas[i])):
			if paralist[res[0][1]].lemmas[i][j] in highlight:
				print('\033[1;37;41m%s\033[0m' % paralist[res[0][1]].raw_words[i][j],end = " ")
			else:
				print(paralist[res[0][1]].raw_words[i][j],end = " ")
	print()

str_query = input()
handle_request(str_query,123)
	
	
