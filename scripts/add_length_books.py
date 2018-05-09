import requests
import json
import pandas as pd

baseurl = "http://openlibrary.org/api/books"
isbnstr = "ISBN:"
parameters = {"bibkeys": isbnstr}
parameters["jscmd"] = "details"
parameters["format"] = "json"

#res = requests.get(baseurl,params=parameters)
#res_json = json.loads(res.text)

df = pd.read_csv("./bookswithlength.csv")
df_to_search = df[3000:4000]

for idx, row in df_to_search.iterrows():
	isbn = row["isbn"]
	isbnstr = "ISBN:"
	if(type(isbn) is float):
		continue
	if(len(isbn) == 9):
		isbn = "0" + isbn
	isbnstr = isbnstr + isbn
	parameters["bibkeys"] = isbnstr
	try:
		res = requests.get(baseurl, params=parameters)
		res_dic = json.loads(res.text)
	except:
		print("response not found")
		isbnstr = "ISBN:"
		continue
	print(isbnstr)
	try:
		df.set_value(idx, "length", res_dic[isbnstr]["details"]["number_of_pages"])
		print(res_dic[isbnstr]["details"]["number_of_pages"])
	except:
		print("not found")
	print ()
	isbnstr="ISBN:"
df.to_csv("bookswithlength.csv",index=False)	
print("End of script")