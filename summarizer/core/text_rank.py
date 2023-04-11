import numpy as np
import math
import pandas as pd
import re
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
import networkx as nx
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from core.grpc_server import *


def one_time_downloaded_files():
    nltk.download("punkt")
    nltk.download("stopwords")


def text_rank_similarities(i, j):
    sum = 0
    for w in i.split():
        if w in j.split():
            sum += 1
    return sum / (math.log(len(i.split())) + math.log(len(j.split())))


def cvtfidf_cosine_sim(stemmedSen, alg="cv"):
    if alg == "cv":
        CountVec = CountVectorizer(ngram_range=(1, 1))
        Count_data = CountVec.fit_transform(stemmedSen)
        cv_dataframe = pd.DataFrame(
            Count_data.toarray(), columns=CountVec.get_feature_names()
        )
    else:
        CountVec = TfidfVectorizer()
        Count_data = CountVec.fit_transform(stemmedSen)
        cv_dataframe = pd.DataFrame(
            Count_data.toarray(), columns=CountVec.get_feature_names()
        )

    sim_mat = np.zeros([len(stemmedSen), len(stemmedSen)])

    for i in range(len(stemmedSen)):
        for j in range(len(stemmedSen)):
            if i != j:
                sim_mat[i][j] = cosine_similarity(
                    cv_dataframe.loc[i, :].to_numpy().reshape(1, -1),
                    cv_dataframe.loc[j, :].to_numpy().reshape(1, -1),
                )[0][0]

    norm = np.sum(sim_mat, axis=1)
    sim_mat = np.divide(sim_mat, norm, where=norm != 0)

    return sim_mat


def text_rank_summarize(text, k=5, alg="trsim"):

    sentences = sent_tokenize(text)

    clearedSen = []
    for i in sentences:
        sent = re.sub("[^a-zA-ZÂâğüşöçıİĞÜŞÖÇ]", " ", i)
        sent = sent.lower()
        clearedSen.append(sent)

    stemmedSen = []

    for i in clearedSen:
        stem = ""
        for j in i.split():
            res = morphology_stub.AnalyzeSentence(
                z_morphology.SentenceAnalysisRequest(input=str(j))
            )
            if (
                res.results[0].best.dictionaryItem.lemma.lower()
                not in stopwords.words("turkish")
                and res.results[0].best.dictionaryItem.lemma.lower() != "unk"
                and len(res.results[0].best.dictionaryItem.lemma.lower()) != 1
            ):
                stem += res.results[0].best.dictionaryItem.lemma.lower() + " "
            elif res.results[0].best.dictionaryItem.lemma.lower() == "unk":
                stem += j + " "
        stem.strip()
        stemmedSen.append(stem)

    if alg == "trsim":

        sim_mat = np.zeros([len(stemmedSen), len(stemmedSen)])
        for i in range(len(stemmedSen)):
            for j in range(len(stemmedSen)):
                if i != j:
                    sim_mat[i][j] = text_rank_similarities(stemmedSen[i], stemmedSen[j])

    elif alg == "cv":
        sim_mat = cvtfidf_cosine_sim(stemmedSen, alg="cv")
    elif alg == "tfidf":
        sim_mat = cvtfidf_cosine_sim(stemmedSen, alg="tfidf")

    # PageRank
    G = nx.from_numpy_array(np.array(sim_mat))
    scores = nx.pagerank_numpy(G)

    ranked_sentences = sorted(
        ((scores[i], s) for i, s in enumerate(sentences)), reverse=True
    )

    summary_sentences = []
    for i in range(k):
        summary_sentences.append(ranked_sentences[i][1])

    return summary_sentences