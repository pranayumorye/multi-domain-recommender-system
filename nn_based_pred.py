import itertools
import ast
import numpy as np
import pandas as pd
from keras.models import model_from_json

# load weights and model from disk
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")


# Get theta and X
X = pd.read_csv("nn_regr_data_final.csv")
dataset = X.values
data = pd.read_csv("regr_data_final.csv")
dataset = dataset[:,:4]
y_pred = loaded_model.predict(dataset)
print(y_pred)

# Get names for reference
df = pd.read_csv("./books_final.csv", usecols=["title"])

def get_title_from_id(idx):
    return df.iloc[idx]["title"]

# Make intermediate df to store id-pairs and similarities
pairs_and_simil = pd.DataFrame(data={
    "id_pair": data["id_pair"],
    "overall_simil": y_pred[:,0]
})

pairs_and_simil.to_csv("nn_pred.csv", index = False)

# Since data exists in batches of 1000 with the same idx1
batch_size = 1000

for i in range(11):
    # For all items in subset, idx1 is the same
    subset = pairs_and_simil[i * batch_size : (i+1) * batch_size]
    # print(subset.info())

    simils = np.asarray(subset["overall_simil"])

    # Go from first-last to tenth-last, in reverse
    indices = np.argsort(simils)[-1:-10:-1]

    print("Items similar to %s:" % (get_title_from_id(i)))
    for idx in indices:
        print("%4d - %s" % (idx, get_title_from_id(idx)))

    print("*" * 50)