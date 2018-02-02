import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

df = pd.read_csv("../datasets/combined.csv")
dfc = df.sample(n=5000)
dfc = dfc.reset_index()
print(dfc.head())

tf = TfidfVectorizer(analyzer='word',ngram_range=(1,2),min_df=0,stop_words='english')

tfidf_matrix = tf.fit_transform(dfc['plot'])
print (tfidf_matrix.shape)
cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)


for idx, row in dfc.iterrows():
    similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
    if row['isbook'] == 1:
        similar_items = [(round(cosine_similarities[idx][i],2), dfc['title'][i])
                        for i in similar_indices if dfc['isbook'][i] == 0]
    else:
        similar_items = [(round(cosine_similarities[idx][i],2), dfc['title'][i])
                        for i in similar_indices if dfc['isbook'][i] == 1]
    if len(similar_items) >= 10:
        similar_items = similar_items[:10]
    print(row['title'])
    print(similar_items)

# print (cosine_similarities)
        
#print (tfidf_matrix)