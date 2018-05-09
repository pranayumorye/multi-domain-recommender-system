import pandas as pd
import itertools

df = pd.read_csv("./datasets/content/small_combined_final.csv")
data = pd.read_csv("comb_regr_data_final.csv")


actual_pairs = []

print(df)

for pair in itertools.product(range(0, 1000), repeat=2):
    # print((df.iloc[pair[0]]["comb_id"], df.iloc[pair[1]]["comb_id"]))
    actual_pairs.append((df.iloc[pair[0]]["comb_id"], df.iloc[pair[1]]["comb_id"]))
    
# df["actual_id_pairs"] = actual_pairs
new = pd.DataFrame(data=actual_pairs)
new.to_csv("comb_id_pairs.csv", index = False)

print(actual_pairs)