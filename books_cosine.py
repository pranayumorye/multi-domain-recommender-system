import pandas as pd
import numpy as np

ratings_df = pd.read_csv("./datasets/collab/books/reduced_ratings.csv")[-100000:]
books_df = pd.read_csv("./datasets/collab/books/books10k.csv")
books_df['book_id'] = books_df['book_id'].apply(pd.to_numeric)
R_df = ratings_df.pivot(index = 'user_id', columns ='book_id', values = 'rating').fillna(0)
R = R_df.as_matrix()
book_indices = books_df["book_id"].as_matrix()

book_indices = book_indices[:100]

Rt = R.T

# book_indices = [1,4,7,18,19]
similarity_matrix = np.zeros((book_indices.shape[0], book_indices.shape[0]))

def mod(x):
	return np.sqrt(np.dot(x, x))

def similarity(x1, x2):
	return np.dot(x1 - np.mean(x1),x2 - np.mean(x2))/(mod(x1 - np.mean(x1))*mod(x2 - np.mean(x2)))
	
def find_books(book_indices):
	return [books_df.iloc[index]["title"] for index in book_indices]

for i in range(book_indices.shape[0]):
	for j in range(book_indices.shape[0]):
		sim = similarity(Rt[i], Rt[j])
		similarity_matrix[i][j] = sim
		
for i in range(similarity_matrix.shape[0]):
	book = similarity_matrix[i]
	print("Closest books to book ", find_books([i]), ": ", find_books(np.argsort(book)[::-1][1:11]))

# for book in similarity_matrix:
	
book = similarity_matrix[0]
indices = np.argsort(book)[::-1][1:11]

print("\n\n\n***********************************************************\n\n\n")
# print(similarity_matrix)