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
    {"title": "Операция «Ы» и другие приключения Шурика", "genre": "Комедия", "age_rating": "12+", "year": 1965, "image": "https://avatars.mds.yandex.net/i?id=a0edc67fe395cf55bb5ba1b7429ba5300b4d01ad-5849765-images-thumbs&n=13"},  
    {"title": "Бриллиантовая рука", "genre": "Комедия", "age_rating": "12+", "year": 1968, "image": "https://avatars.mds.yandex.net/i?id=b1b72f7bb10b7273e5d641c4fb6006bebe150d79-5878159-images-thumbs&n=13"},  
    {"title": "Один дома", "genre": "Комедия", "age_rating": "6+", "year": 1990, "image": "https://avatars.mds.yandex.net/get-kinopoisk-image/4303601/8438872f-1964-4658-a6eb-230f7e33b165/3840x"},  
    {"title": "Мальчишник в Вегасе", "genre": "Комедия", "age_rating": "18+", "year": 2009, "image": "https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_669c02cd5de5626edd82e4f3_669cecc09c015076f8e867fe/scale_1200"},  
    {"title": "Тот самый Мюнхгаузен", "genre": "Комедия", "age_rating": "12+", "year": 1979, "image": "https://a.d-cd.net/DvyfjMmjO_gKd1UYFFIbTt2qZIs-1920.jpg"},  
    {"title": "Пила", "genre": "Ужасы", "age_rating": "18+", "year": 2004, "image": "https://avatars.mds.yandex.net/get-mpic/11763878/2a0000018b4350d12cd27ee73f9ee808f307/orig"},  
    {"title": "Звонок", "genre": "Ужасы", "age_rating": "16+", "year": 2002, "image": "https://avatars.dzeninfra.ru/get-zen_doc/10384921/pub_634c661148ecfb0f0020a1a0_64cacb6a1a2d2135217f01db/scale_1200"},    
    {"title": "Реинкарнация", "genre": "Ужасы", "age_rating": "18+", "year": 2005, "image": "http://avatars.mds.yandex.net/get-vthumb/3187201/30c70756df9e05fe6893c5fbaddfc22d/800x450"},    
    {"title": "Пulp Fiction", "genre": "Криминал", "age_rating": "18+", "year": 1994, "image": "https://avatars.mds.yandex.net/i?id=0c926e1dd58a6a0b5475fe968e87df069d044851-12601053-images-thumbs&n=13"},    
    {"title": "Город Бога", "genre": "Криминал", "age_rating": "18+", "year": 2002, "image": "https://static.okko.tv/images/v4/eab2fc68-ef64-4900-afd5-4f27b5b996eb"},  
    {"title": "Властелин колец: Братство Кольца", "genre": "Фэнтези", "age_rating": "12+", "year": 2001, "image": "http://avatars.mds.yandex.net/get-vthumb/3072928/be06f7610fe84215231573972ea9a9c2/800x450"},  
    {"title": "Гладиатор", "genre": "Исторический", "age_rating": "16+", "year": 2000, "image": "https://images.kinorium.com/movie/poster/143897/w1500_50457996.jpg"},  
    {"title": "Оппенгеймер", "genre": "Исторический", "age_rating": "18+", "year": 2023, "image": "https://static.kinoafisha.info/k/movie_posters/1920x1080/upload/movie_posters/9/1/7/6888719/04c12a356a6e0e86991b4a8a8a0e1d1b.jpg"},
    {"title": "Дюна", "genre": "Фантастика", "age_rating": "12+", "year": 2021, "image": "https://static.kinoafisha.info/k/movie_posters/1920x1080/upload/movie_posters/5/0/8/6888050/5a9e5a8e5e5a5e5a5e5a5e5a5e5a5e5a.jpg"},
    {"title": "Топ Ган: Мэверик", "genre": "Боевик", "age_rating": "12+", "year": 2022, "image": "https://static.kinoafisha.info/k/movie_posters/1920x1080/upload/movie_posters/3/0/8/6888030/5a9e5a8e5e5a5e5a5e5a5e5a5e5a5e5a.jpg"},
    {"title": "Кот в сапогах: Последнее желание", "genre": "Мультфильм", "age_rating": "6+", "year": 2022, "image": "https://static.kinoafisha.info/k/movie_posters/1920x1080/upload/movie_posters/9/0/8/6888090/5a9e5a8e5e5a5e5a5e5a5e5a5e5a5e5a.jpg"},
    {"title": "Барби", "genre": "Комедия", "age_rating": "12+", "year": 2023, "image": "https://static.kinoafisha.info/k/movie_posters/1920x1080/upload/movie_posters/7/1/8/6888170/5a9e5a8e5e5a5e5a5e5a5e5a5e5a5e5a.jpg"},
    {"title": "Аватар: Путь воды", "genre": "Фантастика", "age_rating": "12+", "year": 2022, "image": "https://static.kinoafisha.info/k/movie_posters/1920x1080/upload/movie_posters/2/0/8/6888020/5a9e5a8e5e5a5e5a5e5a5e5a5e5a5e5a.jpg"},
    {"title": "Майор Гром: Чумной Доктор", "genre": "Боевик", "age_rating": "16+", "year": 2021, "image": "https://static.kinoafisha.info/k/movie_posters/1920x1080/upload/movie_posters/1/1/8/6888110/5a9e5a8e5e5a5e5a5e5a5e5a5e5a5e5a.jpg"},
    {"title": "Нет", "genre": "Ужасы", "age_rating": "16+", "year": 2022, "image": "https://static.kinoafisha.info/k/movie_posters/1920x1080/upload/movie_posters/4/1/8/6888140/5a9e5a8e5e5a5e5a5e5a5e5a5e5a5e5a.jpg"},
    {"title": "Гнев человеческий", "genre": "Триллер", "age_rating": "18+", "year": 2021, "image": "https://static.kinoafisha.info/k/movie_posters/1920x1080/upload/movie_posters/6/1/8/6888160/5a9e5a8e5e5a5e5a5e5a5e5a5e5a5e5a.jpg"},
    {"title": "Крушение", "genre": "Триллер", "age_rating": "16+", "year": 2023, "image": "https://static.kinoafisha.info/k/movie_posters/1920x1080/upload/movie_posters/8/1/8/6888180/5a9e5a8e5e5a5e5a5e5a5e5a5e5a5e5a.jpg"},
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