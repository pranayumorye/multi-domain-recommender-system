import pandas as pd

tandp = pd.read_csv("../datasets/books/titles_and_pageids.csv",delimiter="\t")[0:4000]
booksummaries = pd.read_csv("../datasets/books/booksummaries.csv",delimiter="\t")

tandp["genres"] = "Sample"

for idx, row in tandp.iterrows():
	index = row["booksummaries_index"]
	if(index == -1):
		continue
	genres = booksummaries.iloc[index]["genres"]
	tandp.set_value(idx,"genres",genres)
	print("inserted genres in line %d for title %s" % (idx,booksummaries.iloc[index]["title"]))
	print()
	

tandp.to_csv("../datasets/titles_and_pageids.csv", sep="\t", index=False)

print("End of script")	
