# 📚 Collaborative Filtering Book Recommender System

A **Collaborative Filtering--based Book Recommendation System** built
using\
**Python, Pandas, Scikit-learn, Flask, and Bootstrap**.

This project recommends books based on **user similarity and item
similarity** and provides a clean web interface to explore popular books
and get personalized recommendations.

------------------------------------------------------------------------

## 🚀 Features

-   🔍 Collaborative Filtering Recommendations\
-   ⭐ Top 50 Popular Books based on ratings\
-   🧠 Cosine Similarity--based recommendation model\
-   🌐 Flask Web Application\
-   🎨 Clean Dark UI using Bootstrap\
-   🖼 Image fallback for broken/missing covers\
-   ⚡ Fast recommendations using precomputed similarity matrices

------------------------------------------------------------------------

## 🧠 Recommendation Technique

This project uses **Item-Based Collaborative Filtering**:

1.  A user--book interaction matrix is created\
2.  Cosine similarity is calculated between books\
3.  Similar books are recommended based on the selected book

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Programming Language: **Python**
-   Libraries: **Pandas, NumPy, Scikit-learn**
-   Backend: **Flask**
-   Frontend: **HTML, CSS, Bootstrap 3**
-   Model Storage: **Pickle**

------------------------------------------------------------------------

## 📂 Project Structure

    Collaborative-Filtering-Book-Recommender/
    │
    ├── app.py
    ├── popular.pkl
    ├── pt.pkl
    ├── books.pkl
    ├── similarity.pkl
    │
    ├── templates/
    │   ├── index.html
    │   ├── recommend.html
    │
    ├── requirements.txt
    ├── README.md
    ├── .gitignore

------------------------------------------------------------------------

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

``` bash
git clone https://github.com/Priyrajsinh/collaborative-filtering-book-recommender.git
cd collaborative-filtering-book-recommender
```

### 2️⃣ Create virtual environment

``` bash
python -m venv venv
```

### 3️⃣ Activate virtual environment

**Windows**

``` bash
venv\Scripts\Activate.ps1
```

**Linux / Mac**

``` bash
source venv/bin/activate
```

### 4️⃣ Install dependencies

``` bash
pip install -r requirements.txt
```

### 5️⃣ Run the application

``` bash
python app.py
```

Open browser:

    http://127.0.0.1:5000

------------------------------------------------------------------------

## 📸 Screenshots

-   Top 50 Popular Books\
-   Collaborative Book Recommendations\
-   Clean Responsive UI

*(Add screenshots here)*

------------------------------------------------------------------------

## 📈 Future Improvements

-   🔎 Autocomplete search\
-   👤 User authentication\
-   📊 Hybrid recommendation system\
-   ☁️ Cloud deployment (Render / AWS)\
-   📱 Mobile-friendly UI

------------------------------------------------------------------------

## 👨‍💻 Author

**Priyrajsinh**\
Computer Engineering Student\
Aspiring Machine Learning / AI Engineer

------------------------------------------------------------------------

## ⭐ If you like this project

Give it a ⭐ on GitHub --- it really helps!
