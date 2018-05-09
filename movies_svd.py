import pandas as pd
import numpy as np
from scipy.sparse.linalg import svds

ratings_df = pd.read_csv("./datasets/collab/movies/reduced_ratings.csv")[0:1000000]
movies_df = pd.read_csv("./tmdb_movies_final.csv")
movies_df['id'] = movies_df['id'].apply(pd.to_numeric)
R_df = ratings_df.pivot(index = 'userId', columns ='movieId', values = 'rating').fillna(0)
R = R_df.as_matrix()
user_ratings_mean = np.mean(R, axis=1)
R_demeaned = R - user_ratings_mean.reshape(-1, 1)
U, sigma, Vt = svds(R_demeaned, k=50)


print(Vt.shape)

print("**********")


sigma = np.diag(sigma)

all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)
print(R)
print(all_user_predicted_ratings)
preds_df = pd.DataFrame(all_user_predicted_ratings, columns = R_df.columns)

def recommend_movies(predictions_df, userID, movies_df, original_ratings_df, num_recommendations=5):
    
    # Get and sort the user's predictions
    user_row_number = userID - 1 # UserID starts at 1, not 0
    sorted_user_predictions = predictions_df.iloc[user_row_number].sort_values(ascending=False)
    
    # Get the user's data and merge in the movie information.
    user_data = original_ratings_df[original_ratings_df.userId == (userID)]
    user_full = (user_data.merge(movies_df, how='left', left_on='movieId', right_on='id').
                 sort_values(['rating'], ascending=False)
                )

    print('User {0} has already rated {1} movies.'.format(userID, user_full.shape[0]))
    print('Recommending the highest {0} predicted ratings movies not already rated.'.format(num_recommendations))

    # Recommend the highest predicted rating movies that the user hasn't seen yet.
    recommendations = (movies_df[~movies_df['id'].isin(user_full['movieId'])].
         merge(pd.DataFrame(sorted_user_predictions).reset_index(), how = 'left',
               left_on='id',
               right_on='movieId').
         rename(columns={user_row_number: 'Predictions'}).
         sort_values('Predictions', ascending = False).
                       iloc[:num_recommendations, :-1]
                      )

    return user_full, recommendations

already_rated, predictions = recommend_movies(preds_df, 11220, movies_df, ratings_df, 10)

print(already_rated.head(10))
print(predictions)