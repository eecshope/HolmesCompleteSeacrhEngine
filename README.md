# HolmesCompleteSeacrhEngine

This is the class project of the Modern Information Retreival Methods about designing an search engine of the Sherlock Holmes Complete

## Chapter Structure

We use a chapter as the basic unit in this project. The python notebook 'data/raw_chapters/parse_raw.ipynb' is used to parse the raw text 'sherlock.txt' into several objects for chapters arranged in a python list. Besides, it seperates the stories and write them into several isolated files, each file name of which is the true name of the story.

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

## vector_based_retrieval

We use the chapter_dictionary listed above to build our wordbag: a list field of str. The lemmas in each chapter_dictionary.tf_count.keys() will be appended to this list. Of course we make sure that the lemmas in the bag are different from each other. Besides, this is a set so no duplicated record is in this set.

Another important data structure: wordnumber, a python dictionary that convert a word into it's index in wordbag list (if it exists in wordbag). To be concise, it's a dictionary of the lemmas appeared in the corpus.

A Python dictionary is used to describe the content of a query. In fact, it looks a little bit like an chapter. The fields are listed below:

 * text: a str field. The content of this query
 * raw_words: a list field of str. Corresponding to the query.text .
 * lemmas: a list of lemmatized words.
 * tf_count: a dict containing the non-stopwords and their frequencies.
 * non_stop_word_count: number of the non-stopwords.

The definition of the data model is in 'model/query.py'

With all structure we have, it's simply to calculate tf-idf vector of each \'document\'---chapter, and each query. Note: even if the query.tf_count.keys() may contain words that are not in the wordbag, we only calculate the tf-idf value of the words in the wordbag. The \[UNK\] are neglected. 

The documents corresponding to the K vectors with the highest cosine_similarity to the query vector are selected as the related documents and returned as the final retrieval results.

All of these data mentioned above are cached in `data/caches` with their names and the suffice '.pkl'. To generate them, just run `vector_ir.py` in the root directory of the project. 
## inverted_index

It's a list of lists of numbers. Each sublist records the indexs in the dictlist of the document in which the corresponding word appears. eg:  inverted_index\[i\] records all the indexes of document containing wordbag[i]. 

