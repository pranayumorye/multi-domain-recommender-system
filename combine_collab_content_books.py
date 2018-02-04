import pandas as pd

tandp = pd.read_csv("../datasets/titles_and_pageids.csv",delimiter="\t")[0:4000]
booksummaries = pd.read_csv("../datasets/booksummaries.csv",delimiter="\t")

tandp["plot"] = "Sample"

for idx,row in tandp.iterrows():
	index = row["booksummaries_index"]
	if(index==-1):
		continue
	plot = booksummaries.iloc[index]["plot"]
	tandp.set_value(idx,"plot",plot)
	print("inserted plot in line %d for title %s"%(idx,booksummaries.iloc[index+2]["title"]))
	print()
	
	
tandp.to_csv("../datasets/titles_and_pageids.csv",sep="\t",index=False)
	
print("End of script")	
