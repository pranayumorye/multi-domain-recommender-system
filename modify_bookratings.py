import pandas as pd

books = pd.read_csv("./datasets/collab/books/books10k.csv")
ratings = pd.read_csv("./datasets/collab/books/ratings.csv")[0:100000]

modified = pd.DataFrame(columns = ["user_id","book_id","rating"])

for idx,row in books.iterrows():
	id = row["book_id"]
	temp = pd.DataFrame([[374355,id,3]], columns=["user_id","book_id","rating"])
	modified = modified.append(temp)
	
modified.to_csv("addedratings.csv", index = False)	