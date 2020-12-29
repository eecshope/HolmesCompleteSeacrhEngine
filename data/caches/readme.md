### `summary.json`

The static summary of the chapters. It's a list of chapter-level units. Each unit has the following field:

- `id` : the id of the chapter. Following the order in `chapter_cache.pkl` and starting from 0
- `chapter`: the name of the chapter in the form of **story+part+chapter**. If this chapter does not have a part name or a chapter name, the corresponding string is neglected. 
- `summary` a list of summaries. Each summary is in the form of a string. 

The order of the summaries are the same as the way in which they're presented in the original text.

To generate the summaries, just run `get_static_summary.py` in the root directory of the project then ,,, just wait because it will take up about 5 hours.



### `main_character.json`

A brief view of main characters. It's a list of dict which includes several information about a character. Each dict has the following field:

	* `id` : the id of the character. Make no sense.
	* `name`: the name of the character.
	* `subscribe` : A brief subscribe of the character.
	* `chapters` : A str list of the name of chapter that the character presents. 


### `tfifd_cache.pkl`
This is a pickle-form cache for the preprocessed tf-idf vectors for each chapter. Each vector is in a list and the lists are wrapped by a big list. The vectors are arranged in the order of `chapter_cahce.pkl` and the words are arranged in the order of `wordbag_cache.pkl`.

The actual number is the result of `tf: term frequency (unnormalized)`* `idf: inverted document frequency`, where

$$
idf = log(\frac{n_{doc}}{n_{appeared}})
$$

### `recommend.json`
This is cached for the recommended documents for each document in the corpus. It's a big list ane the structure of the sub-unit is listed below:

- `chapter_id`: the id of this chapter. An integer
- `recommend`: the ids of the recommended chapters. A list of integers.

Example:
```
{"chapter_id": 0, "recommend": [1, 64, 51, 60, 12]}
```

### `chapter_characters.json`
This is a cache of characters appearing in each chapter. A big list. The structure of each sub-unit is listed below:
-  `idx` the id of the chapter
-  `names` a list of names 

### `chapter_cache_spoiler.pkl`
Add 'spoiler' attribute to the objects. run `add_spoiler.py` in directory `misc` to generate this file. Be sure to generate `chapter_cache.pkl` beforehand.