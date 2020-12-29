import _pickle as pkl


def add_spoiler(cache_path, sys_path, tgt_path):
    with open(cache_path, "rb") as file:
        chapters = pkl.load(file)

    with open(sys_path, "r", encoding='utf8') as file:
        synopsis = [s.strip() for s in file.readlines()]

    story_set = set()
    for chapter in chapters:
        story_set.add(chapter.story)

    s_dict = dict({})
    for story in story_set:
        s_dict[story] = list([])

    cur_story = ""
    for line in synopsis:
        if line in story_set:
            cur_story = line
        else:
            s_dict[cur_story].append(line)

    for chapter in chapters:
        try:
            chapter.spoiler = s_dict[chapter.story]
        except KeyError:
            chapter.spoiler = 'TBD'

    with open(tgt_path, "wb") as file:
        pkl.dump(chapters, file)


if __name__ == "__main__":
    add_spoiler("../data/caches/chapter_cache.pkl", "../data/raw_chapters/synopsis.dat",
                "../data/caches/chapter_cache_spoiler.pkl")
