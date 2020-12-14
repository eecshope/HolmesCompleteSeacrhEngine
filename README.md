# HolmesCompleteSeacrhEngine

This is the class project of the Modern Information Retreival Methods about designing an search engine of the Sherlock Holmes Complete

## Chapter Structure

We use a chapter as the basic unit in this project. The python notebook 'data/parse_raw.ipynb' is used to parse the raw text 'sherlock.txt' into several objects for chapters arranged in a python list. Besides, it seperates the stories and write them into several isolated files, each file name of which is the true name of the story.

A Python dictionary is used to describe the content of a chapter. It's fields are listed below:

- story: a str field. The name of the story this chapter belongs to.
- part: a str field. The part of the story belongs to. If the story has just one part, this filed will be 'NO PART'
- chapter: a str field. The title of this chapter. Usually it's in the form of 'CHAPTER I XXX' and there's situation that 'XXX' is not provided. If the story has only one chapter, this field wiil be 'NO CHAPTER'
- text: a list field of str. The raw data of this chapter and the words are seperated by white spaces.

To use the notebook, just run all of the cells. Then the stories are seperated and a file `raw_records.pkl` is generated. It's the list of these chapter dictionaries.

To further exploit the usage of these chapters, we design a class for the chapters. The definition of the data model is in 'data/chapter.py'. The attributes are listed below:

- The meaning of 'story', 'part', 'chapter' and 'text' can be found in the doc.
- n_paragraph: the length of text, the number of the paragraphs
- raw_words:  a list of lists of words and punc. Each sublist corresponds to an original sentence
- lemmas: a list of lists of lemmatized words. Aligned to 'raw words'
- tf_count: a dict containing the non-stopwords and their frequencies. eg: tf_count['hello'] = 1
- non_stop_word_count: number of the non-stopwords

The dirty work are done by standard `nltk` library. The lemmatized work uses the POS of the words which comes come `nltk.tag.pos_tag`

These dirty wordk is a little bit time-consuming that parsing all the chapters needs 2min56s. So we cache the binary form of the python objects in `data/chapter_cache.pkl`