from flask import Flask, render_template, request
from recommendation import recommend

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        names, posters = recommend(request.form['movie'])
        return render_template('index.html', recommended_movies=names, recommended_posters=posters)
    return render_template('index.html')

if __name__=='main_':
    app.run(debug=True)