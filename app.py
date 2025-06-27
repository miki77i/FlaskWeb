from flask import Flask, render_template,request, jsonify
app = Flask(__name__)

movies = [
    {"title": "Ирония судьбы", "genre": "Комедия", "age_rating": "12+", "country": "Россия", "star": 8, "year": 1975, "image" : "https://avatars.mds.yandex.net/i?id=85018b87656b4cc4dc87f374dab6d1d1_l-5192585-images-thumbs&n=13"},
    {"title": "Оно", "genre": "Ужасы", "age_rating": "16+" , "country": "США", "star": 9.5 , "year": 2017, "image" : "https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_65b45e2d98779f1cacad455d_65b462ae0a0e6d0513caceed/scale_1200"},
    {"title": "Матрица", "genre": "Фантастика", "age_rating": "16+" , "country": "США", "star": 8, "year": 1999, "image" : "https://avatars.mds.yandex.net/i?id=6b88d5c41634b799beb94b8e6da36e07_l-4303535-images-thumbs&n=13"},
    {"title": "Достучаться до небес", "genre": "Драма", "age_rating": "16+", "country": "Германия", "star": 6.5, "year": 1997, "image" : "https://static.okko.tv/images/v4/94423745-9dce-487c-b126-e72b1c4d234d"},
    {"title": "Крепкий орешек", "genre": "Боевик", "age_rating": "18+", "country": "США", "star":7.5, "year": 1988, "image" : "https://static.okko.tv/images/v4/74cf1bca-3878-4841-989d-40c78a9f6396"},
    {"title": "Шерлок Холмс", "genre": "Детектив", "age_rating": "12+", "country": "Великобритания", "star": 8.5, "year": 2009, "image" : "https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_6543efd38b85625d917eb8cb_6543f11a0aa2423ce6cd8883/scale_1200"},
    {"title": "Интерстеллар", "genre": "Научное", "age_rating": "12+", "country": "США", "star":5.5, "year": 2014, "image" : "https://cs12.pikabu.ru/post_img/2020/11/07/6/og_og_1604736347254738206.jpg"},
    {"title": "Ромео и Джульетта", "genre": "Трагедия", "age_rating": "12+", "country": "Италия", "star":9, "year": 1996, "image" : "https://static.kinoafisha.info/k/movie_posters/1920x1080/upload/movie_posters/2/1/5/8142512/4a1396ee3b3d774fd15d5776e62e2e91.jpg"},
    {"title": "Молчание ягнят", "genre": "Триллер", "age_rating": "18+", "country": "США", "star":7, "year": 1991, "image" : "https://static.kinoafisha.info/k/movie_posters/1920x1080/upload/movie_posters/4/0/8/3906804/92ec465a68dfd9ac388cf7c1c7339e57.jpeg"},
    {"title": "Титаник", "genre": "Драма", "age_rating": "12+", "country": "США", "star":6, "year": 1997, "image" : "https://avatars.mds.yandex.net/i?id=a3b4ef2c9fd4b047c1590ed013665be7_l-10471914-images-thumbs&n=13"},
    {"title": "Операция «Ы» и другие приключения Шурика", "genre": "Комедия", "age_rating": "12+","country": "Россия", "star":8, "year": 1965, "image": "https://avatars.mds.yandex.net/i?id=a0edc67fe395cf55bb5ba1b7429ba5300b4d01ad-5849765-images-thumbs&n=13"},  
    {"title": "Бриллиантовая рука", "genre": "Комедия", "age_rating": "12+","country": "Россия", "star":6.5, "year": 1968, "image": "https://avatars.mds.yandex.net/i?id=b1b72f7bb10b7273e5d641c4fb6006bebe150d79-5878159-images-thumbs&n=13"},  
    {"title": "Один дома", "genre": "Комедия", "age_rating": "6+", "country": "США", "star":9.5, "year": 1990, "image": "https://avatars.mds.yandex.net/get-kinopoisk-image/4303601/8438872f-1964-4658-a6eb-230f7e33b165/3840x"},  
    {"title": "Мальчишник в Вегасе", "genre": "Комедия", "age_rating": "18+", "country": "США", "star":8.5, "year": 2009, "image": "https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_669c02cd5de5626edd82e4f3_669cecc09c015076f8e867fe/scale_1200"},  
    {"title": "Тот самый Мюнхгаузен", "genre": "Комедия", "age_rating": "12+", "country": "Россия", "star":5, "year": 1979, "image": "https://a.d-cd.net/DvyfjMmjO_gKd1UYFFIbTt2qZIs-1920.jpg"},  
    {"title": "Пила", "genre": "Ужасы", "age_rating": "18+", "country": "США", "star":7.5, "year": 2004, "image": "https://avatars.mds.yandex.net/get-mpic/11763878/2a0000018b4350d12cd27ee73f9ee808f307/orig"},  
    {"title": "Звонок", "genre": "Ужасы", "age_rating": "16+", "country": "США", "star":6, "year": 2002, "image": "https://avatars.dzeninfra.ru/get-zen_doc/10384921/pub_634c661148ecfb0f0020a1a0_64cacb6a1a2d2135217f01db/scale_1200"},    
    {"title": "Реинкарнация", "genre": "Ужасы", "age_rating": "18+", "country": "США", "star":8, "year": 2005, "image": "http://avatars.mds.yandex.net/get-vthumb/3187201/30c70756df9e05fe6893c5fbaddfc22d/800x450"},    
    {"title": "Пulp Fiction", "genre": "Криминал", "age_rating": "18+", "country": "США", "star":7, "year": 1994, "image": "https://avatars.mds.yandex.net/i?id=0c926e1dd58a6a0b5475fe968e87df069d044851-12601053-images-thumbs&n=13"},    
    {"title": "Город Бога", "genre": "Криминал", "age_rating": "18+", "country": "Бразилия", "star":5.5,"year": 2002, "image": "https://static.okko.tv/images/v4/eab2fc68-ef64-4900-afd5-4f27b5b996eb"},  
    {"title": "Властелин колец: Братство Кольца", "genre": "Фэнтези", "age_rating": "12+", "country": "Новая Зеландия", "star":9, "year": 2001, "image": "http://avatars.mds.yandex.net/get-vthumb/3072928/be06f7610fe84215231573972ea9a9c2/800x450"},  
    {"title": "Гладиатор", "genre": "Исторический", "age_rating": "16+", "country": "США", "star":8.5, "year": 2000, "image": "https://images.kinorium.com/movie/poster/143897/w1500_50457996.jpg"},  
    {"title": "Оппенгеймер", "genre": "Исторический", "age_rating": "18+", "country": "Великобритания", "star":6.5, "year": 2023, "image": "https://www.curzon.org.uk/wp-content/uploads/2023/07/maxresdefault.jpg"},
    {"title": "Дюна", "genre": "Фантастика", "age_rating": "12+", "country": "США", "star":9, "year": 2021, "image": "https://sun9-36.userapi.com/impg/QZWfH4y1IblZC431ZOLXmpuhUc-2XCg9aF0dPA/zeEiB6EXH_k.jpg?size=408x604&quality=96&sign=8f2944604077e98f87a6f94fe68b02d6&type=album"},
    {"title": "Топ Ган: Мэверик", "genre": "Боевик", "age_rating": "12+", "country": "США", "star":6 ,"year": 2022, "image": "https://coolmusicltd.com/wp-content/uploads/2023/11/TG.jpg"},
    {"title": "Кот в сапогах: Последнее желание", "genre": "Мультфильм",  "age_rating": "6+", "country": "США", "star":9.5, "year": 2022, "image": "https://pic.rutubelist.ru/video/9d/a6/9da6f8420a5d82aad46e0db169b70b60.jpg"},
    {"title": "Аватар: Путь воды", "genre": "Фантастика", "age_rating": "12+", "country": "Великобритания", "star":9.5 ,"year": 2022, "image": "https://www.lafilm.edu/wp-content/uploads/2023/01/Avatarthewayofwater.png"},
    {"title": "Майор Гром: Чумной Доктор", "genre": "Боевик", "age_rating": "16+", "country": "Россия", "star":9, "year": 2021, "image": "https://avatars.mds.yandex.net/i?id=e986b875bb1b38e370fed51f2d284ca4_l-8316779-images-thumbs&n=13"},
    {"title": "Нет", "genre": "Ужасы", "age_rating": "16+", "country": "Франция", "star":7, "year": 2022, "image": "https://sun9-72.userapi.com/impg/N1P-8vSFijTskUOJEcq7KV5unnt0DpSlxyZkNA/u1b6b-XKwV4.jpg?size=1280x720&quality=95&sign=0e0b826c1979ce08cc0423ddc9571f87&type=video_thumb"},
    {"title": "Гнев человеческий", "genre": "Триллер", "age_rating": "18+", "country": "США", "star":8, "year": 2021, "image": "https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_66c6b49ff93157776a357276_66c6b5269a81156e1f3e4480/scale_1200"},
    {"title": "Крушение", "genre": "Триллер", "age_rating": "16+", "country": "Великобритания", "star":8.5, "year": 2023, "image": "http://avatars.mds.yandex.net/get-vthumb/4265575/30dbb0606d5df9029b4f8502d69c46c3/800x450"},
    {"title": "Все везде и сразу", "genre": "Фантастика/Комедия", "age_rating": "16+", "country": "США", "star":5.5, "year": 2022, "image": "https://static.kinoafisha.info/k/movie_posters/1920x1080/upload/movie_posters/3/2/8/6888230/01.jpg", "note": "Оскар-2023 за лучший фильм"},
    {"title": "Круэлла", "genre": "Криминал/Драма", "age_rating": "16+", "country": "США", "star":7.5, "year": 2021, "image": "https://avatars.mds.yandex.net/i?id=bfe202d07341f1a5355ee17640f00e49_l-4251039-images-thumbs&n=13", "note": "Готический стиль и Эмма Стоун"},
    {"title": "Человек-паук: Паутина вселенных", "genre": "Мультфильм", "age_rating": "12+", "country": "США", "star":9.5, "year": 2023, "image": "https://static.wikia.nocookie.net/spiderverseseries/images/3/39/Site-community-image/revision/latest?cb=20230404164047", "note": "Визуальная революция"},
    {"title": "Меню", "genre": "Триллер/Сатира", "age_rating": "18+", "country": "США", "star":8, "year": 2022, "image": "https://avatars.mds.yandex.net/i?id=dfcd38fd9ff862f4de84cb8f5e993710_l-9106775-images-thumbs&n=13", "note": "Готовка + психология"},
    {"title": "Бунтарь", "genre": "Биография/Драма", "age_rating": "16+", "country": "Франция", "star":6.5, "year": 2023, "image": "https://www.kino-teatr.ru/movie/poster/162859/147840.jpg", "note": "Протесты в Беларуси"},
    {"title": "Телефон мистера Харригана", "genre": "Триллер", "age_rating": "16+", "country": "США", "star":7.5, "year": 2022, "image": "https://avatars.mds.yandex.net/get-vthumb/905851/f721c2b5acfdf0663d515e8acd1fc459/564x318_1", "note": "Мистика от Стивена Кинга"},
    {"title": "Годзилла и Конг: Новая империя", "genre": "Фантастика", "age_rating": "12+", "country": "США", "star": 7.5, "year": 2024, "image": "https://i.ytimg.com/vi/_cmc5xrZHzg/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGHIgPChQMA8=&rs=AOn4CLDdRJKcmxsyARb041tKs-2WM0554Q", "note": "Эпическое противостояние титанов"},
    {"title": "Вызов", "genre": "Драма", "age_rating": "12+", "country": "Россия", "star": 7.2, "year": 2023, "image": "https://mf.b37mrtl.ru/actualidad/public_images/2023.04/article/6438332859bf5b3e3673ade5.jpg", "note": "Первый в мире фильм, снятый в космосе"}
]


@app.route("/")
def slide1():
    return render_template("s1.html")

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    genres = data.get('genres', [])
    ages = data.get('ages', [])
    stars = data.get('stars', [])
    countries = data.get('countries', [])
    
    filtered_movies = movies
    
    if genres and not "Любое" in genres:
        filtered_movies = [m for m in filtered_movies if m['genre'] in genres]
    
    # Фильтрация по возрастным ограничениям (если выбраны)
    if ages and not "Любое" in ages:
        filtered_movies = [m for m in filtered_movies if m['age_rating'] in ages]
    
    # Фильтрация по рейтингу (если выбраны)
    if stars and not "0" in stars:
        try:
            # Конвертируем все значения в числа для сравнения
            star_values = [float(s) for s in stars]
            filtered_movies = [m for m in filtered_movies 
                             if any(float(m['star']) > sv for sv in star_values)]
        except ValueError:
            pass
    
    # Фильтрация по странам (если реализовано в данных)
    if countries and not "Любая" in genres:
        # Предполагаем, что у фильмов есть поле 'country'
        filtered_movies = [m for m in filtered_movies if m.get('country') in countries]
    
    return jsonify(filtered_movies)


if __name__ == "__main__":
    app.run(debug=True)