from flask import Flask, render_template,request, jsonify
app = Flask(__name__)

movies = [
    {"title": "Ирония судьбы", "genre": "Комедия", "age_rating": "12+", "year": 1975, "image" : "https://avatars.mds.yandex.net/i?id=85018b87656b4cc4dc87f374dab6d1d1_l-5192585-images-thumbs&n=13"},
    {"title": "Оно", "genre": "Ужасы", "age_rating": "16+", "year": 2017, "image" : "https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_65b45e2d98779f1cacad455d_65b462ae0a0e6d0513caceed/scale_1200"},
    {"title": "Матрица", "genre": "Фантастика", "age_rating": "16+", "year": 1999, "image" : "https://avatars.mds.yandex.net/i?id=6b88d5c41634b799beb94b8e6da36e07_l-4303535-images-thumbs&n=13"},
    {"title": "Достучаться до небес", "genre": "Драма", "age_rating": "16+", "year": 1997, "image" : "https://static.okko.tv/images/v4/94423745-9dce-487c-b126-e72b1c4d234d"},
    {"title": "Крепкий орешек", "genre": "Боевик", "age_rating": "18+", "year": 1988, "image" : "https://static.okko.tv/images/v4/74cf1bca-3878-4841-989d-40c78a9f6396"},
    {"title": "Шерлок Холмс", "genre": "Детектив", "age_rating": "12+", "year": 2009, "image" : "https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_6543efd38b85625d917eb8cb_6543f11a0aa2423ce6cd8883/scale_1200"},
    {"title": "Интерстеллар", "genre": "Научное", "age_rating": "12+", "year": 2014, "image" : "https://cs12.pikabu.ru/post_img/2020/11/07/6/og_og_1604736347254738206.jpg"},
    {"title": "Ромео и Джульетта", "genre": "Трагедия", "age_rating": "12+", "year": 1996, "image" : "https://static.kinoafisha.info/k/movie_posters/1920x1080/upload/movie_posters/2/1/5/8142512/4a1396ee3b3d774fd15d5776e62e2e91.jpg"},
    {"title": "Молчание ягнят", "genre": "Триллер", "age_rating": "18+", "year": 1991, "image" : "https://static.kinoafisha.info/k/movie_posters/1920x1080/upload/movie_posters/4/0/8/3906804/92ec465a68dfd9ac388cf7c1c7339e57.jpeg"},
    {"title": "Титаник", "genre": "Драма", "age_rating": "12+", "year": 1997, "image" : "https://avatars.mds.yandex.net/i?id=a3b4ef2c9fd4b047c1590ed013665be7_l-10471914-images-thumbs&n=13"},
]

@app.route("/")
def slide1():
    return render_template("s1.html")

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    genre = data.get('genre')
    age_rating = data.get('age_rating')
    
    filtered_movies = movies
    
    if genre and genre != 'Любой':
        filtered_movies = [m for m in filtered_movies if m['genre'] == genre]
    
    if age_rating and age_rating != 'Любое':
        filtered_movies = [m for m in filtered_movies if m['age_rating'] == age_rating]
    
    return jsonify(filtered_movies)


if __name__ == "__main__":
    app.run(debug=True)