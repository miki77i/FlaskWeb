from flask import Flask, render_template,request, jsonify
app = Flask(__name__)

movies = [
    {"title": "Ирония судьбы", "genre": "Комедия", "age_rating": "12+", "year": 1975},
    {"title": "Оно", "genre": "Ужасы", "age_rating": "16+", "year": 2017},
    {"title": "Матрица", "genre": "Фантастика", "age_rating": "16+", "year": 1999},
    {"title": "Достучаться до небес", "genre": "Драма", "age_rating": "16+", "year": 1997},
    {"title": "Крепкий орешек", "genre": "Боевик", "age_rating": "18+", "year": 1988},
    {"title": "Шерлок Холмс", "genre": "Детектив", "age_rating": "12+", "year": 2009},
    {"title": "Интерстеллар", "genre": "Научное", "age_rating": "12+", "year": 2014},
    {"title": "Ромео и Джульетта", "genre": "Трагедия", "age_rating": "12+", "year": 1996},
    {"title": "Молчание ягнят", "genre": "Триллер", "age_rating": "18+", "year": 1991},
    {"title": "Титаник", "genre": "Драма", "age_rating": "12+", "year": 1997},
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