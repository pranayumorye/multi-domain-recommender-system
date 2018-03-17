matrix = {}

with open("genre_simil.txt", "r") as f:
    lines = f.readlines()
    columns = [line.strip() for line in lines if line[0] != '0']
    values = [line.strip() for line in lines if line[0] == '0']

for col, val in zip(columns, values):
    val = [float(i) for i in val.split(",")]
    tuples = zip(columns[columns.index(col)+1:], val)
    for col2, sim in tuples:
        temp_tuple = tuple([col, col2])
        matrix[temp_tuple] = sim
        temp_tuple = temp_tuple[1], temp_tuple[0]
        matrix[temp_tuple] = sim

for col in columns:
    matrix[(col, col)] = 1.00

print(matrix)

with open("genre_matrix.txt", "w") as outfile:
    outfile.writelines(str(matrix))

# for key in matrix.keys():
#     print("%15s %15s %10.3f" % (*list(key), matrix[key]))

# def get_similarity(genre1, genre2):
# 	return matrix[tuple([genre1, genre2])]

# print(get_similarity("Short", "Adventure"))
# print(get_similarity("Adventure", "Short"))
# print(get_similarity("History", "Documentary"))