from nltk.corpus import stopwords
from pulp import LpMaximize, LpProblem, LpVariable, GLPK_CMD
import numpy as np

STOPWORDS = stopwords.words('english') + ["'", '"', '!', ',', '.', '?', '-s', '-ly', '</s> ', 's']


def get_summary_parameters(concept_idf: dict, lemmas: list):
    """
    This function is used to get the parameters used in ILP. Sentences shorter than 3 or with no concept is removed.
    So n_concept is the number of the concepts and n_sentences is the number of valid sentences.

    :param concept_idf: a dictionary of the IDF of each possible concept
    :param lemmas: list of list of lemmas
    :return: occ: int8 array of shape [n_concepts, n_sentences]; w: mat of shape [n_concepts], sentence_id_map: map the
    sentences used in the computation to the original idx.
    """
    concept_vocab = dict({})
    concepts = list([])
    sentence_id_map = list([])
    num_concepts = 0
    num_sentences = 0

    for j, sentence in enumerate(lemmas):
        if len(sentence) < 5:
            continue

        concept_in_sentence = list([])
        for i in range(1, len(sentence)):
            concept = (sentence[i-1], sentence[i])
            if not (concept[0] in STOPWORDS and concept[1] in STOPWORDS):
                if concept not in concept_vocab:
                    concept_vocab[concept] = num_concepts
                    concept_in_sentence.append(num_concepts)
                    num_concepts += 1
                else:
                    concept_in_sentence.append(concept_vocab[concept])

        if len(concept_in_sentence) > 0:
            sentence_id_map.append(j)
            concepts.append(concept_in_sentence)
            num_sentences += 1

    occ = np.zeros((num_concepts, num_sentences), np.int8)
    for i, sentence in enumerate(concepts):
        for concept in sentence:
            occ[concept][i] = 1
    w = np.zeros([num_concepts])
    for concept, idx in concept_vocab.items():
        w[idx] = concept_idf[concept]

    return occ, w, sentence_id_map


def get_summary(concept_idf, lemmas, max_length):
    occ, w, sentence_id_map = get_summary_parameters(concept_idf, lemmas)
    num_concepts, num_sentences = occ.shape
    concept_vars = [LpVariable("concept_" + str(idx), cat='Binary') for idx in range(num_concepts)]
    sentence_vars = [LpVariable("sentence_" + str(idx), cat='Binary') for idx in range(num_sentences)]

    l_constrained = sum([len(lemmas[idx]) * s_var for idx, s_var in zip(sentence_id_map, sentence_vars)]) <= max_length
    con_1 = [[s_var * occ[i][j] <= c_var for j, s_var in enumerate(sentence_vars)]
             for i, c_var in enumerate(concept_vars)]
    con_2 = [sum([s_var * occ[i][j] for j, s_var in enumerate(sentence_vars)]) >= c_var
             for i, c_var in enumerate(concept_vars)]

    target = sum([c_w * c_var for c_w, c_var in zip(w, concept_vars)])

    model = LpProblem(name="Summary", sense=LpMaximize)
    model += (l_constrained, "l_constrained")
    for i, con in enumerate(con_2):
        model += (con, "con_2_" + str(i))
    cnt = 0
    for ll in con_1:
        for con in ll:
            model += (con, "con_1_" + str(cnt))
            cnt += 1

    model += target
    model.solve(solver=GLPK_CMD(msg=False))

    selected_sentence = list([])
    for var in model.variables():
        if var.name.startswith("sentence") and var.value() == 1:
            selected_sentence.append(sentence_id_map[int(var.name[9:])])
    selected_sentence_id = sorted(selected_sentence)

    return selected_sentence_id
