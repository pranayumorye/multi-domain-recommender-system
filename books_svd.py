import pandas as pd
import math
import numpy as np
from scipy.sparse.linalg import svds

#ratings_list = [i.strip().split("::") for i in open('/home/countnightlock/Downloads/ml-1m/ratings.dat', 'rt', encoding='latin1').readlines()]
#users_list = [i.strip().split("::") for i in open('/home/countnightlock/Downloads/ml-1m/users.dat', 'rt', encoding='latin1').readlines()]
#movies_list = [i.strip().split("::") for i in open('/home/countnightlock/Downloads/ml-1m/movies.dat', 'rt', encoding='latin1').readlines()]


ratings_df = pd.read_csv("./datasets/collab/books/reduced_ratings.csv")[-100000:]
books_df = pd.read_csv("./datasets/collab/books/books10k.csv")
books_df['book_id'] = books_df['book_id'].apply(pd.to_numeric)
R_df = ratings_df.pivot(index = 'user_id', columns ='book_id', values = 'rating').fillna(0)
R = R_df.as_matrix()
book_indices = books_df.as_matrix()

user_ratings_mean = np.mean(R, axis = 1)
R_demeaned = R - user_ratings_mean.reshape(-1, 1)
U, sigma, Vt = svds(R_demeaned, k = 50)
print(R_df.shape)
print(U.shape)
print(Vt.shape)
print(sigma.shape)
V = Vt.T
V = np.dot(np.diag(sigma),Vt)
temp = pd.DataFrame(columns = ["id1", "id2", "distance"])

Rt = R.T

# book_indices = [1,4,7,18,19]

def mod(x):
	return np.sqrt(np.dot(x, x))

for i in book_indices:
	for j in book_indices:
		sim = np.dot(Rt[i], Rt[j])/(mod(Rt[i])*mod(Rt[j]))
		print("similarity between books %d, %d is %f" % (i,j,sim))
# print(temp.head())
print("\n\n\n***********************************************************\n\n\n")

sigma = np.diag(sigma)

all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)
print(R)
print(all_user_predicted_ratings)
preds_df = pd.DataFrame(all_user_predicted_ratings, columns = R_df.columns)

def recommend_movies(predictions_df, userID, books_df, original_ratings_df, num_recommendations=5):
    
    # Get and sort the user's predictions
    user_row_number = userID - 1 # UserID starts at 1, not 0
    sorted_user_predictions = predictions_df.iloc[user_row_number].sort_values(ascending=False)
    
    # Get the user's data and merge in the movie information.
    user_data = original_ratings_df[original_ratings_df.user_id == (userID)]
    user_full = (user_data.merge(books_df, how = 'left', left_on = 'book_id', right_on = 'book_id')
                 )

    print('User {0} has already rated {1} movies.'.format(userID, user_full.shape[0]))
    print('Recommending the highest {0} predicted ratings movies not already rated.'.format(num_recommendations))
    
    # Recommend the highest predicted rating movies that the user hasn't seen yet.
    recommendations = (books_df[~books_df['book_id'].isin(user_full['book_id'])].
         merge(pd.DataFrame(sorted_user_predictions).reset_index(), how = 'left',
               left_on = 'book_id',
               right_on = 'book_id').
         rename(columns = {user_row_number: 'Predictions'}).
         sort_values('Predictions', ascending = False).
                       iloc[:num_recommendations, :-1]
                      )

    return user_full, recommendations

already_rated, predictions = recommend_movies(preds_df, 1, books_df, ratings_df, 10)

print(already_rated.head(10))
print(predictions)