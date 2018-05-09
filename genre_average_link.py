import ast
import pandas as pd
import numpy as np
import itertools

with open("genre_matrix.txt", "r") as f:
    line = f.readlines()[0]

genre_matrix = ast.literal_eval(line)


def get_pair_similarity(genre1, genre2):
    return genre_matrix[(genre1, genre2)]


# def get_similarity(set1, set2):
#     sum = 0
#     count = 0
#     for i1 in set1:
#         for i2 in set2:
#             if i1 == i2:
#                 pair_sim = 1.000
#             else:
#                 pair_sim = get_pair_similarity(i1, i2)
#             print("%s - %s similarity is %f" % (i1, i2, pair_sim))
#             sum += pair_sim
#             count += 1

#     return sum/count


def get_similarity(set1, set2):
    if len(set1) < len(set2):
        set1, set2 = set2, set1
    if(len(set2) == 0):
        return 0
    sum = 0
    count = len(set1)
    for i1 in set1:
        max = -1
        for i2 in set2:
            pair_sim = get_pair_similarity(i1, i2)
            if pair_sim > max:
                max = pair_sim
        sum += max
    if(count):
        return sum/count
    return 0  

df = pd.read_csv("./datasets/content/combined_final.csv")
books = df[2550:3050]
movies = df[0:500]
books = books.append(movies)
book_id_pairs = []
similarity_matrix = np.zeros((1000, 1000))

for pair in itertools.product(range(0, 1000), repeat=2):
    book_id_pairs.append(pair)

for idx1, idx2 in book_id_pairs:
    print(idx1, idx2)
    genre_set1 = ast.literal_eval(books.iloc[idx1]["genres"])
    genre_set2 = ast.literal_eval(books.iloc[idx2]["genres"])
    similarity_matrix[idx1, idx2] = np.float16(get_similarity(genre_set1, genre_set2))

np.savetxt("comb_genre_simil_matrix.txt", similarity_matrix)
