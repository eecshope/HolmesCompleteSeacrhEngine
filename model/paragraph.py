import nltk
from nltk.tokenize import WordPunctTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tag import pos_tag


class Paragraph:
	def __init__(self,arg_chapter_index: int,arg_index: int, paragraph_content: str):
		self.chapter_index = arg_chapter_index
		self.index = arg_index
		self.sentences = list([])
		
		self.sentences += nltk.tokenize.sent_tokenize(paragraph_content)
		self.raw_words = [WordPunctTokenizer().tokenize(sentence) for sentence in self.sentences]
		lemmatizer = WordNetLemmatizer()

		def get_pos(words):
			for word, pos in pos_tag(words):
				if pos.startswith('NN'):
					yield word, 'n'
				elif pos.startswith('VB'):
					yield word, 'v'
				elif pos.startswith('JJ'):
					yield word, 'a'
				elif pos.startswith('R'):
					yield word, 'r'
				else:
					yield word, 'n'

		self.lemmas = [[lemmatizer.lemmatize(word.lower(), pos) for word, pos in get_pos(words)]
                       for words in self.raw_words]
		
		stop_words = stopwords.words('english') + ['!', ',', '.', '?', '-s', '-ly', '</s> ', 's']
		self.wordlist = list({})
		for sentence in self.lemmas:
			for lemma in sentence:
				if lemma not in stop_words:
					self.wordlist.append(lemma)
