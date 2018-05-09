import itertools
import ast
import numpy as np
import pandas as pd
from regression import get_coefficients

# Get theta and X
X = pd.read_csv("comb_regr_data_final_fix.csv", sep=",")
theta = get_coefficients()
print(theta)
# theta = [[ 1, -0.01,  0.03390613, -0.00082851 ]]
y_pred = []

output = pd.DataFrame(columns=["id", "title", "similar_movies", "similar_books"])

# Get names for reference
df = pd.read_csv("./datasets/content/small_combined_final.csv")

def get_title_from_id(idx):
    return df.iloc[idx]["title"]

def get_comb_id_from_id(idx):
    return df.iloc[idx]["comb_id"]

def check_is_book(idx):
    return df.iloc[idx]["isbook"]    

# Make intermediate df to store id-pairs and similarities
pairs_and_simil = pd.DataFrame(data={
    "id_pair": X["actual_pairs"],
    "overall_simil": X["overall_simil"]
})

# Since data exists in batches of 1000 with the same idx1
batch_size = 1000

for i in range(1000):
    # For all items in subset, idx1 is the same
    subset = pairs_and_simil[i * batch_size : (i+1) * batch_size]
    # print(subset.info())

    simils = np.asarray(subset["overall_simil"])
    templist = []
    templist.append(get_comb_id_from_id(i))
    templist.append(get_title_from_id(i))
    booklist = []
    movielist = []

    # Go from first-last to tenth-last, in reverse
    indices = np.argsort(simils)[-1:-20:-1]

    print("Items similar to %s:" % (get_title_from_id(i)))
    for idx in indices:
        if(check_is_book(idx)):
            booklist.append(get_comb_id_from_id(idx))
        else:
            movielist.append(get_comb_id_from_id(idx))
    
    templist.append(movielist)
    templist.append(booklist)
    
    output.loc[i] = templist
    print(templist)
    print("*" * 50)

    

output.to_csv("top_n_similar.csv", index = False)