import pickle
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
movies = pickle.load(open('movies.pkl','rb'))
vectorizer = CountVectorizer(max_features=5000, stop_words='english')
vectors = vectorizer.fit_transform(movies['tags'])
similarity = cosine_similarity(vectors)

# TMDB settings
API_KEY = 'a958953e581cec6201ebcb9f5823b19b'

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    j = requests.get(url).json()
    if j.get('poster_path'):
        return f"https://image.tmdb.org/t/p/w500{j['poster_path']}"
    return "https://via.placeholder.com/300x450.png?text=No+Poster"

def recommend(title):
    title = title.lower()
    titles = movies['title'].str.lower()
    if title not in titles.values:
        return [], []
    idx = titles[titles == title].index[0]
    sims = list(enumerate(similarity[idx]))
    top = sorted(sims, key=lambda x: x[1], reverse=True)[1:6]
    rec_titles = []
    rec_posters = []
    for i,_ in top:
        rec_titles.append(movies.iloc[i]['title'])
        rec_posters.append(fetch_poster(movies.iloc[i]['id']))
    return rec_titles, rec_posters
   