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

It's a list of class InvertedUnit for each word in wordbag. Class InvertedUnit defined as follow:

​	It is consist of three member variables:

​	chapter_index: record the chapter's index in struct `dictlist`. 

​	paragraph_index: record the paragraph's index in struct `paralist`.

​	position: a list of number. Each number record one position of the word presented in the paragraph.

## Key words highlight

Given a query str, We count the number of keywords and the types of keywords presented in each paragraph, and retrival the related paragraph of this query. After getting the most related paragraph, we print the content of it, and highlight every key words.

## Get Static Summary

We retrieve the sentences that have the most important 'concepts' (bigrams) and the number of the total words is less than a given upper bound. Obviously, it's a Integer Linear Programming problem and the key problem is that how can we say that 'a concept' is important.

According to Dan Gillick and Benoit Favre, the 'concepts' that are more likely to appear in the retrieved sentences have higher idf scores. So we weight the concepts by their idf scores. 

As for the implementation, we use `pulp` as the frontend and `GLPK` as the backend to solve the ILP problem. Because ILP is a NP-Hard problem, getting the results is very time-consuming. Considering that we want to get the static summaries for these chapters and there aren't many chapters in this corpus, we preprocess these summaries beforehand and store them in a `JSON` file: `data/cache/summary.json`. It's a list of chapter-level units. Each unit has the following field:

- `id` : the id of the chapter. Following the order in `chapter_cache.pkl` and starting from 0
- `chapter`: the name of the chapter in the form of **story+part+chapter**. If this chapter does not have a part name or a chapter name, the corresponding string is neglected. 
- `summary` a list of summaries. Each summary is in the form of a string. 

There's one thing that worth mentioning. The sentences are presented in the order of their presentation in the original text. Because *Holmes Complete* has too much dialogue, we find than arrange the summaries in this way makes the summaries seem like a standalone story but filled with mysterious. 

To generate the summaries, just run `get_static_summary.py` in the root directory of the project then ,,, just wait because it will take up about 5 hours.

## Recommend System
The recommend system is somehow simple. We fully utilize the tf-idf features retrieved beforehand and calculate the cosine similarities to find out the most close ones. The document itself is not included. The result are cached in `recommend.json`.

## Names Retrieval 
We retrieve the names of each chapter and formed them into a list. Duplicated names are removed. The method for retrieving the names is based on NER, implemented by NLTK group. The result is cached in `chapter_characters.json`. 