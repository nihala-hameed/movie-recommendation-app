import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load your dataset
movies = pd.read_csv('tmdb_5000_movies.csv')

# Fill missing overviews with empty strings
movies['overview'] = movies['overview'].fillna('')

# Convert overviews to vectors using TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['overview'])

# Calculate cosine similarity matrix
similarity = cosine_similarity(tfidf_matrix)

# Save the similarity matrix as pickle
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print("✅ similarity.pkl file created successfully.")