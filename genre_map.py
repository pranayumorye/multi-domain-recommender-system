import ast
import pandas as pd

new = pd.read_csv("books_final.csv")
old = pd.read_csv("combined_books10k_summaries.csv", delimiter="\t")

adventure_genres = set(["Adventure novel", "Young adult literature", 
                        "Children's literature", "Juvenile fantasy", 
                        "High fantasy", "Heroic fantasy", "Fairy tale"])

def powerset(s):
    x = len(s)
    l = []
    for i in range(1, 1 << x):
        l.append({s[j] for j in range(x) if (i & (1 << j))})
   
    return l

for idx, row in new.iterrows():
    print(idx)
    newgenre = ast.literal_eval(row["genres"])
    oldgenre = ast.literal_eval(old.iloc[idx]["genres"])
    print(newgenre)
    if oldgenre in powerset(["Fiction", "Novel", "Novella", "Literary fiction"]):
        newgenre = set(["Drama"])
        new.at[idx, "genres"] = newgenre
        print(newgenre)
    if "Fantasy" in newgenre and "Fantasy" not in oldgenre:
        newgenre -= {"Fantasy"}
        new.at[idx, "genres"] = newgenre
        print(newgenre)
    if "Sci-Fi" in newgenre and "Science Fiction" not in oldgenre:
        newgenre -= {"Sci-Fi"}
        new.at[idx, "genres"] = newgenre
        print(newgenre)
    if "Fiction" in oldgenre:
        if adventure_genres.intersection(oldgenre):
            newgenre -= {"Adventure"}
        newgenre.add("Drama")
    
    print("*"*50)

print(new["genres"])

new.to_csv("new.csv", sep=",", index=False)
