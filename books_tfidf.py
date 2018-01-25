import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

ds = pd.read_csv("../datasets/booksummaries/booksummaries.csv",delimiter="\t")
# print(ds.head())

tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 3),min_df=0,stop_words='english')

test_ds = ds #[0:100]

#print (test_ds)

tfidf_matrix = tf.fit_transform(test_ds['plot'])

# print(tfidf_matrix[9])
# print("*************************")
# print(tfidf_matrix[8])

cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

for idx, row in test_ds.iterrows():
    similar_indices = cosine_similarities[idx].argsort()[:-10:-1]
    similar_items = [(round(cosine_similarities[idx][i],2), test_ds['title'][i]) for i in similar_indices]
    print(similar_items)

# print (cosine_similarities)
		
#print (tfidf_matrix)
