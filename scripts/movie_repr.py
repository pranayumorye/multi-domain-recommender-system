import pandas as pd

movies = pd.read_csv("tmdb_movies_final.csv")
movies["runtime_rep"] = 1
movies["age"] = 1
c0 = c1 = c2 = 0

for idx, row in movies.iterrows():
	length = row["runtime"]
	year = row["release_year"]
	if(length < 85):
		movies.set_value(idx, "runtime_rep", 0)
		c0 += 1
	elif(length > 135):
		movies.set_value(idx, "runtime_rep", 2)
		c2 += 1
	
	if(year < 1950):
		movies.set_value(idx, "age", 0)
	elif(year >= 1950 and year <1970):
		movies.set_value(idx, "age", 1)
	elif(year >= 1970 and year < 2000):
		movies.set_value(idx, "age", 2)
	elif(year >= 2000):
		movies.set_value(idx, "age", 3)

print(movies)
print(c0, len(movies)-c0-c2, c2)
movies.to_csv("tmdb_movies_final.csv", index = False)	

print("End of script")