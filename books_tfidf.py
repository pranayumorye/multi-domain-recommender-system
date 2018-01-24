import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

ds = pd.read_csv("../datasets/booksummaries/booksummaries.csv",delimiter="\t")

tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 3),min_df=0,stop_words='english')

test_ds = ds[0:10]

#print (test_ds)

tfidf_matrix = tf.fit_transform(test_ds['plot'])

cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

# for idx, row in ds.iterrows():
	# similar_indices = cosine_similarities[idx].argsort()[:-10:-1]
	# similar_items = [(cosine_similarities[idx][i], test_ds['wiki_id'][i]) for i in similar_indices]
	
for i in cosine_similarities:
	for j in i:
		j = round(j,2)
	
print (cosine_similarities)
		
#print (tfidf_matrix)