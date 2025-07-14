import pandas as pd
import pickle
import ast

# Load datasets
movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

# Merge on title
movies = movies.merge(credits, on='title')

# Extract useful info
def parse_names(text):
    items = ast.literal_eval(text)
    return [i['name'] for i in items]

movies['genres']   = movies['genres'].apply(parse_names)
movies['keywords'] = movies['keywords'].apply(parse_names)
movies['cast']     = movies['cast'].apply(lambda x: parse_names(x)[:3])
movies['crew']     = movies['crew'].apply(parse_names)
movies['director'] = movies['crew'].apply(lambda c: [m for m in c if 'Director' in m or 'director' in m])

# Combine into a single 'tags' string
movies['tags'] = movies['genres'] + movies['keywords'] + movies['cast'] + movies['director'] + movies['overview'].fillna('').str.lower().str.split()
movies['tags'] = movies['tags'].apply(lambda x: ' '.join([i.replace(' ', '') for i in x]))

# Save preprocessed DataFrame
pickle.dump(movies[['id','title','tags']], open('movies.pkl','wb'))

print("✅ Merged and saved movies.pkl")