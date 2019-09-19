# Multi-domain Recommender System

## Implementation

The system consists of two databases: the user ratings database
which consists of movies and book as separate tables and the metadata
database which contains both movies and books in a single table. The user
ratings database is used to nd cosine similarity between item-pairs from
both the tables. This similarity value is used as the output(y) in regression
to determine weights. The metadata database is split into plot/summary,
genre, length and release/publish date. All these parameters are quantified
to give the input values (x1, x2, x3, x4) for regression. Therefore by break-
ing down the problem into inter-domain and intra-domain we obtain weights
that give good recommendations across the movies and books domains.

### Intra-domain aproach

Here both the domains are considered independently and various algorithms
are used to develop recommender systems in each domain. Collaborative
Filtering which is used here gives excellent recommendations when it comes
to a single domain.

#### Matrix factorization using singular value decomposition

The user-ratings matrix is the original data that we have and this matrix is
broken down into three matrices which are an accurate approximation of the
original matrix. Mathematically it decomposes R into two unitary matrices
and a diagonal matrix.
<br>
U matrix is the user features matrix which represents how much the
users like each feature and the V T matrix is the movie features matrix which
represents how relevant is each feature to each movie. This helps us derive
the underlying tastes and the preferences of the users from the raw data.
This technique of low rank factorization is quite accurate and scales well
to large datasets as well. It outperforms other techniques for collaborative
filtering and yields meaningful results as well. It is capable of computing
large data at a much faster rate and is quite efficient compared to other
methods.

### Inter-domain approach

In this approach we use combine the data of both the domains and with
the help of several algorithms obtain the input values for regression. This
approach uses content based filtering approach, and the features that are
common to both movies and books are selected to make recommendations
across the two domains. We use the plot/summary of movies/books, genre,
release/publish date and length.

#### Plot similarities using TF-IDF

TF-IDF weight is used as a statistical measure of how important a word is
to a document in a collection. This is a product of two terms: the term-
frequency (TF) and the inverse document frequency (IDF).
<br>
Using this algorithm certain keywords are obtained with a coefficient
depending on how strongly they define the plot. The similarities are mapped
based on the keywords and similar movies/books pairs are formed of the top
results.
<br>
The similarity between a pair of items is calculated
using the cosine similarity measure.

#### Genre similarity

Unique genres are identified from the datasets of movies and books and each
of them is mapped into a set of genres which are common to both movies
and books. After this mapping, similarities are drawn for the respective
movies/books based on how close the genres are to each other. These simi-
larities are based on the results of a research paper which clusters the genres
based on their similarity.
<br>
Genres of items are acquired in sets. We then find
the similarities between the two items by finding the average link between
the two sets of genres. Average link is found by adding all the similarities
of the cartesian product of the two sets and dividing it by the cardinality of
the resultant set.

#### Release/Publish Date

The time of release of the respective movies and books is also considered as
it reflects the trends and the tastes of those times. The release is in the date
format and using the year of release it is converted into a coefficient which
determines the movies/books from new to old.

#### Length

The length of the movies or the number of pages in a book can also be
considered a measure if a user might like it or not. Someone might just
prefer short movies or someone might love to read long books. So the books
and movies are distributed across three categories of short, medium and long.
Short movies would range from 0-40 mins, medium ones would range from
40-120 mins and the long ones above 120 mins. Similarly ranges are defined
for books and they are categorized. Similarity can then be drawn from this
feature as well.

All the features link the two domains but not equally. Each of them affects
the recommendations to a different extent. So to find out how important each
one is and their impact on the recommendations, regression is used to find
out the weights associated with each feature.
