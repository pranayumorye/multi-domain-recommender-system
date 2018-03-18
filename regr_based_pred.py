import itertools
import ast
import numpy as np
import pandas as pd
from regression import get_coefficients

# Get theta and X
X = pd.read_csv("regr_data.csv", sep=",")
theta = get_coefficients()
y_pred = []


# Get names for reference
books = pd.read_csv("books_final.csv", usecols=["title"])

def get_book_from_id(idx):
    return books.iloc[idx]["title"]

# Calculate predicted y via theta dot X[idx]
for idx, row in X.iterrows():
    idx1, idx2 = ast.literal_eval(row["id_pair"])
    x = np.asarray([
        row["tfidf_simil"],
        row["genre_simil"],
        row["age_simil"],
        row["length_simil"]
    ])
    y_pred.append(np.dot(theta[0], x))

# Make intermediate df to store id-pairs and similarities
pairs_and_simil = pd.DataFrame(data={
    "id_pair": X["id_pair"],
    "overall_simil": y_pred
})

# Since data exists in batches of 100 with the same idx1
batch_size = 100

for i in range(11):
    # For all books in subset, idx1 is the same
    subset = pairs_and_simil[i * batch_size : (i+1) * batch_size]
    # print(subset.info())

    simils = np.asarray(subset["overall_simil"])

    # Go from first-last to tenth-last, in reverse
    indices = np.argsort(simils)[-1:-10:-1]

    print("Books similar to %s:" % (get_book_from_id(i)))
    for idx in indices:
        print("%4d - %s" % (idx, get_book_from_id(idx)))
    
    print("*" * 50)