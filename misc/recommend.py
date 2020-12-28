import numpy as np
import json
import _pickle as pkl


def build_recommend_full(features, n_recommend) -> list:
    """
    This function is used to build a recommend list for every document in the corpus based
    on the cosine similarities of their features
    :param n_recommend: number of documents to be recommended
    :param features: list of list
    :return: a list of dicts
    """
    features = np.array(features)
    n_doc, n_vocab = features.shape

    def get_idx(i):
        inner_product = np.matmul(features[i:i+1, :], features.T)[0]  # 1-D array
        cos = inner_product / np.sqrt((np.sum(np.square(features[i])) * np.sum(np.square(features), -1)))
        ll = np.argsort(cos, -1)[-n_recommend-1:-1].tolist()
        ll.reverse()
        return ll

    return list([{"chapter_id": i, "recommend": get_idx(i)} for i in range(n_doc)])


if __name__ == '__main__':
    with open('../data/caches/tfidf_cache.pkl', 'rb') as file:
        real_features = pkl.load(file)
    with open('../data/caches/recommend.json', 'w') as file:
        json.dump(build_recommend_full(real_features, 5), file, ensure_ascii=False)
