import pandas as pd

books = pd.read_csv("books_final.csv")
books["length_rep"] = 1
books["age"] = 1

for idx, row in books.iterrows():
	len = row["length"]
	year = row["original_publication_year"]
	if(len == -1):
		books.set_value(idx, "length_rep", 1)
	elif(len < 200):
		books.set_value(idx, "length_rep", 0)
	elif(len > 600):
		books.set_value(idx, "length_rep", 2)
	
	if(year < 1800):
		books.set_value(idx, "age", 0)
	elif(year >= 1980):
		books.set_value(idx, "age", 3)
	elif(year < 1980 and year >= 1930):
		books.set_value(idx, "age", 2)

print(books.head())
books.to_csv("books_final.csv", index=False)

print("End of script")