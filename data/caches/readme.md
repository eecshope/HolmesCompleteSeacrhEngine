### `summary.json`

The static summary of the chapters. It's a list of chapter-level units. Each unit has the following field:

- `id` : the id of the chapter. Following the order in `chapter_cache.pkl` and starting from 0
- `chapter`: the name of the chapter in the form of **story+part+chapter**. If this chapter does not have a part name or a chapter name, the corresponding string is neglected. 
- `summary` a list of summaries. Each summary is in the form of a string. 

The order of the summaries are the same as the way in which they're presented in the original text.

To generate the summaries, just run `get_static_summary.py` in the root directory of the project then ,,, just wait because it will take up about 5 hours.

