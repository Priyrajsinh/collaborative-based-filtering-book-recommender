from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

# Load files
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))               # pivot table
books = pickle.load(open('books.pkl', 'rb'))         # books dataframe
similarity_score = pickle.load(open('similarity_scores.pkl', 'rb'))

# --- CLEAN DATA (IMPORTANT) ---
books['Book-Title'] = books['Book-Title'].fillna("Unknown Title")
books['Book-Author'] = books['Book-Author'].fillna("Unknown Author")
books['Image-URL-M'] = books['Image-URL-M'].fillna("https://via.placeholder.com/150")

def clean_image(url):
    if pd.isna(url) or url.strip() == "":
        return "https://via.placeholder.com/150"
    if url.startswith("http://"):
        return url.replace("http://", "https://")
    return url

books['Image-URL-M'] = books['Image-URL-M'].apply(clean_image)

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route('/')
def index():
    return render_template(
        'index.html',
        books=popular_df.head(50).to_dict(orient='records')
    )

# ---------------- RECOMMEND PAGE ----------------
@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

# ---------------- RECOMMEND LOGIC ----------------
@app.route('/recommend_books', methods=['POST'])
def recommend_books():
    user_input = request.form.get('user_input')

    if user_input not in pt.index:
        return render_template(
            'recommend.html',
            error="Book not found. Please enter an exact book title."
        )

    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(
        list(enumerate(similarity_score[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    data = []
    for i in similar_items:
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        data.append([
            temp_df['Book-Title'].values[0],
            temp_df['Book-Author'].values[0],
            temp_df['Image-URL-M'].values[0]
        ])

    return render_template('recommend.html', data=data)

# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
