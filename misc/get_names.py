from utils import nlp
import _pickle as pkl
import json
from tqdm import tqdm


def get_names():
    with open("../data/caches/chapter_cache.pkl", "rb") as file:
        chapters = pkl.load(file)
    names = [{"idx": idx, "names": nlp.get_names(chapter.raw_words)}
             for idx, chapter in tqdm(enumerate(chapters), total=len(chapters))]
    with open('../data/caches/chapter_characters.json', "w") as file:
        json.dump(names, file, ensure_ascii=False)


if __name__ == "__main__":
    get_names()
