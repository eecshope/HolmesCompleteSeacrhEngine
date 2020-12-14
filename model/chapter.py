import nltk
from nltk.tokenize import WordPunctTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tag import pos_tag


class Chapter:
    def __init__(self, chapter_unit: dict):
        """
        The meaning of 'story', 'part', 'chapter' and 'text' can be found in the doc.
        n_paragraph: the length of text, the number of the paragraphs
        raw_words:  a list of lists of words and punc. Each sublist corresponds to an original sentence
        lemmas: a list of lists of lemmatized words. Aligned to 'raw words'
        tf_count: a dict containing the non-stopwords and their frequencies. eg: tf_count['hello'] = 1
        non_stop_word_count: number of the non-stopwords


        :param chapter_unit:
        """
        self.story = chapter_unit['story']
        self.part = chapter_unit['part']
        self.chapter = chapter_unit['chapter']
        self.text = chapter_unit['text']
        self.n_paragraph = len(self.text)

        # parse the paragraph into several sentences
        sentences = list([])
        for paragraph in self.text:
            sentences += nltk.tokenize.sent_tokenize(paragraph)

        # parse the sentences and do lemma
        self.raw_words = [WordPunctTokenizer().tokenize(sentence) for sentence in sentences]
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

        # build the word bag for this chapter
        stop_words = stopwords.words('english') + ['!', ',', '.', '?', '-s', '-ly', '</s> ', 's']
        self.tf_count = dict({})
        self.non_stop_word_count = 0

        for sentence in self.lemmas:
            for lemma in sentence:
                if lemma not in stop_words:
                    if lemma not in self.tf_count.keys():
                        self.tf_count[lemma] = 1
                    else:
                        self.tf_count[lemma] += 1
                    self.non_stop_word_count += 1
