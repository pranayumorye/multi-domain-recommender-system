import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

X = pd.read_csv("regr_data_final.csv", usecols = ["tfidf_simil","genre_simil","age_simil","length_simil"])

y = pd.read_csv("regr_data_final.csv", usecols = ["collab_simil"])

X_train, X_test, y_train, y_test = train_test_split(X, y)

regr = linear_model.LinearRegression()
regr.fit(X_train, y_train)

y_pred = regr.predict(X_test)

print('Coefficients: \n', regr.coef_)
print('Coefficient names: tfidf, genre, age, length')
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(y_test, y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(y_test, y_pred))


def get_coefficients():
      return regr.coef_