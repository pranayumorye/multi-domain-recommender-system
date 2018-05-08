from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import numpy
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

# fix random seed for reproducibility
numpy.random.seed(2)

# load dataset
dataframe = pd.read_csv("nn_regr_data_final.csv", header = None)
dataset = dataframe.values

# split into input (X) and output (y) variables
X = dataset[:,0:4]
y = dataset[:,4]


# create model
model = Sequential()
model.add(Dense(8, input_dim=4, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(1, activation='relu'))

# Compile model
model.compile(loss='mean_squared_error', optimizer = 'adam', metrics=['accuracy'])

# Fit the model
model.fit(X, y, epochs=20, batch_size=100)

# evaluate the model
scores = model.evaluate(X, y)
print("\n%s: %.2f%%" % (model.metrics_names[0], scores[0]*100))

y_pred = model.predict(X)

print(mean_squared_error(y_pred,y))

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")

print("Done")