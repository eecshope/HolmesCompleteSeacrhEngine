import pickle as pkl
import json
from tqdm import tqdm
from utils import nlp

# load chapters
with open("data/caches/chapter_cache.pkl", "rb") as file:
    chapters = pkl.load(file)

# build concept idf
bigram = set()
idf_bigram = dict({})
neglected_sentences = 0
for chapter in chapters:
    chapter_bigram_set = set()
    for sentence in chapter.lemmas:
        if len(sentence) < 5:
            neglected_sentences += 1
            continue
        for i in range(1, len(sentence)):
            if sentence[i-1] in nlp.STOPWORDS and sentence[i] in nlp.STOPWORDS:
                continue
            concept = (sentence[i-1], sentence[i])
            bigram.add(concept)
            chapter_bigram_set.add(concept)
    for concept in chapter_bigram_set:
        if concept not in idf_bigram:
            idf_bigram[concept] = 1
        else:
            idf_bigram[concept] += 1

print("There're %d concepts and %d sentences have been skiped" % (len(bigram), neglected_sentences))

summaries = list([])
for idx, chapter in tqdm(enumerate(chapters), total=len(chapters)):
    summary_ids = nlp.get_summary(idf_bigram, chapter.lemmas, 300)

    name = chapter.story
    if chapter.part != "NO PART":
        name += " " + chapter.part
    if chapter.chapter != "NO CHAPTER":
        name += " " + chapter.chapter

    data = {
        "id": idx,
        "chapter": name,
        "summary": [" ".join(chapter.raw_words[summary_id]) for summary_id in summary_ids]
    }
    summaries.append(data)

with open("data/caches/summary.json", "w") as file:
    json.dump(summaries, file, ensure_ascii=True)
