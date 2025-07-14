# Movie Recommendation App
A content-based movie recommendation system built using *Python, **Flask, and **TMDB API*, where users can enter a movie name and get 5 similar movie suggestions along with real movie posters.
## Features
- Enter a movie name and get top 5 similar movies instantly  
- Real movie posters fetched from TMDB API  
- Cosine similarity-based recommendation engine using genres, keywords, cast & crew  
- Responsive and clean UI with HTML, CSS & Bootstrap  
- Built using Flask framework for smooth backend/frontend integration  
## Technologies Used
- Python (Pandas, Scikit-learn)
- Flask
- TMDB API (for posters)
- HTML, CSS, Bootstrap
- Jupyter Notebook (for data preprocessing)
- Git & GitHub (for version control)
## Project Structure
movie-recommendation-app/
│
├── app.py                     # Main Flask application
├── recommendation.py          # Contains the recommendation logic using cosine similarity
├── create_pickle.py           # Script to generate pickle files from datasets
├── tmdb_5000_movies.csv       # Movie dataset from TMDB
├── tmdb_5000_credits.csv      # Credits dataset from TMDB
├── movies.pkl                 # Pickle file containing movie data
├── similarity.pkl             # Pickle file with cosine similarity matrix
│
├── templates/
│   └── index.html             # HTML frontend for the app
│
├── static/
│   └── style.css              # CSS file for styling the UI
│
└── README.md                  # Project documentation
## Note:
Due to GitHub's file size limit (25MB), the following files could not be uploaded:
- movies.pkl
- similarity.pkl
- tmdb_5000_credits.csv
- tmdb_5000_movies.csv
To run the project fully:
1. Use create_pickle.py and create_similarity.py to regenerate the .pkl files.
2. Download the TMDB datasets manually from Kaggle:  
   [https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
You can then place the files in the appropriate directories and run the project locally.
## Color Styling
The UI is styled using Bootstrap with a dark theme and custom text colors to create a cinematic vibe.
## Connect 
If you're interested in trying it out or want the full project, feel free to connect! 
