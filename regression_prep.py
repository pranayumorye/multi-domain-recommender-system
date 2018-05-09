import itertools
import numpy as np
import pandas as pd

params = {
    "sep": ",",
    "usecols": [
        "comb_id",
        "title",
        "length_rep",
        "age"
    ]
}

df = pd.read_csv("./datasets/content/small_combined_final.csv", **params)
comb_id_pairs = []
actual_pairs = []

tfidf_simil = np.loadtxt("comb_tfidf_simil.txt", dtype=np.float16)
collab_simil = np.zeros((1000,1000))
genre_simil = np.loadtxt("comb_genre_simil_matrix.txt", dtype=np.float16)

# for length simil
def get_length_simil(idx1, idx2):
    return 2 * (1 - abs(df.iloc[idx1]["length_rep"] - df.iloc[idx2]["length_rep"])/2)


# for age simil
def get_age_simil(idx1, idx2):
    return 2 * (1- abs(df.iloc[idx1]["age"] - df.iloc[idx2]["age"])/3)


# for tfidf simil
def get_tfidf_simil(idx1, idx2):
    return (tfidf_simil[idx1, idx2])


# for output vector from collaborative similarities
def get_collab_simil(idx1, idx2):
    return 1 + (collab_simil[idx1, idx2])


def get_genre_simil(idx1, idx2):
    return 2 * genre_simil[idx1, idx2]


for pair in itertools.product(range(0, 1000), repeat=2):
    comb_id_pairs.append(pair)
    actual_pairs.append((df.iloc[pair[0]]["comb_id"], df.iloc[pair[1]]["comb_id"]))




print(actual_pairs.head())


# Storing in a csv
columns = ["id_pair","tfidf_simil", "genre_simil", "age_simil", "length_simil", "collab_simil"]
regr_data = pd.DataFrame(columns=columns)

tfidf_simil_list = []
age_simil_list = []
length_simil_list = []
genre_simil_list = []
collab_simil_list = []

for idx1, idx2 in comb_id_pairs:
    print(idx1, idx2)
    tfidf_simil_list.append(get_tfidf_simil(idx1, idx2))
    age_simil_list.append(get_age_simil(idx1, idx2))
    genre_simil_list.append(get_genre_simil(idx1, idx2))
    length_simil_list.append(get_length_simil(idx1, idx2))
    collab_simil_list.append(get_collab_simil(idx1, idx2))
    print("Done for", idx1, idx2, actual_pairs.iloc[idx1 + idx2*1000 - 1])

regr_data = pd.DataFrame(data={
    "id_pair": actual_pairs,
    "tfidf_simil": tfidf_simil_list,
    "age_simil": age_simil_list,
    "length_simil": length_simil_list,
    "genre_simil": genre_simil_list,
    "collab_simil": collab_simil_list,
})

print(regr_data.head())

regr_data.to_csv("comb_regr_data_final.csv", index = False, columns=columns)