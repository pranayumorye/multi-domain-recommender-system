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


def get_length_reps(idx1, idx2):
    return df.iloc[idx1]["length_rep"], df.iloc[idx2]["length_rep"]


for pair in itertools.product(range(0, 100), repeat=2):
    book_id_pairs.append(pair)

for idx1, idx2 in book_id_pairs[:10]:
    print(get_length_reps(idx1, idx2))
