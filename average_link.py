import ast

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
    
    sum = 0
    count = len(set1)
    for i1 in set1:
        max = -1
        for i2 in set2:
            pair_sim = get_pair_similarity(i1, i2)
            if pair_sim > max:
                max = pair_sim
        print("%s - %s similarity is %f" % (i1, i2, pair_sim))
        sum += max
    
    return sum/count

set1 = {"Crime", "Thriller"}
set2 = {"Documentary"}

print(get_similarity(set1, set2))