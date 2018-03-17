import itertools
import numpy as np
import pandas as pd

params = {
    "sep": ",",
    "usecols": [
        "book_id",
        "original_title",
        "length_rep",
        "age"
    ]
}

df = pd.read_csv("./books_final.csv", **params)

df = df[:100]
book_id_pairs = []

tfidf_simil = np.loadtxt("tfidf_simil.txt", dtype = np.float16)
collab_simil = np.loadtxt("collab_simil.txt", dtype = np.float16)


# for length simil
def get_length_simil(idx1, idx2):
    return (1 - abs(df.iloc[idx1]["length_rep"] - df.iloc[idx2]["length_rep"])/2)

# for age simil
def get_age_simil(idx1, idx2):
    return (1- abs(df.iloc[idx1]["age"] - df.iloc[idx2]["age"])/3)

# for tfidf simil
def get_tfidf_simil(idx1, idx2):
    return (tfidf_simil[idx1, idx2])

# for output vector from collaborative similarities
def get_collab_simil(idx1, idx2):
    return (collab_simil[idx1, idx2])



for pair in itertools.product(range(0, 100), repeat=2):
    book_id_pairs.append(pair)

for idx1, idx2 in book_id_pairs[:10]:
    print(get_collab_simil(idx1, idx2), get_tfidf_simil(idx1, idx2), get_age_simil(idx1, idx2), get_length_simil(idx1, idx2))

# Storing in a csv
regr_data = pd.DataFrame(columns = ["id_pair","tfidf_simil", "age_simil", "length_simil", "collab_simil"])


for idx1, idx2 in book_id_pairs:
    

regr_data.to_csv("regr_data.csv", index = False)