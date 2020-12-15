import nltk
from nltk.tokenize import WordPunctTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tag import pos_tag


class Query:
    def __init__(self, str_query: str):
        self.text = str_query
        self.raw_words = WordPunctTokenizer().tokenize(self.text)
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

        self.lemmas = [lemmatizer.lemmatize(word.lower(), pos) for word, pos in get_pos(self.raw_words)]
        stop_words = stopwords.words('english') + ['!', ',', '.', '?', '-s', '-ly', '</s> ', 's']
        self.tf_count = dict({})
        self.non_stop_word_count = 0
        for lemma in self.lemmas:
            if lemma not in stop_words:
                if lemma not in self.tf_count.keys():
                    self.tf_count[lemma] = 1
                else:
                    self.tf_count[lemma] += 1
                self.non_stop_word_count += 1
