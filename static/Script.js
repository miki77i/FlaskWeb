document.addEventListener('DOMContentLoaded', function() {
    let selectedGenre = null;
    let selectedAge = null;
    let selectedStar = null;
    let selectedcountry = null
    
    // Обработчики для жанров
    document.querySelectorAll('.choice1 .criteria').forEach(button => {
        button.addEventListener('click', function() {
            document.querySelectorAll('.choice1 .criteria').forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            selectedGenre = this.getAttribute('data-genre');
        });
    });
    
    // Обработчики для возрастных ограничений
    document.querySelectorAll('.choice2 .criteria').forEach(button => {
        button.addEventListener('click', function() {
            document.querySelectorAll('.choice2 .criteria').forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            selectedAge = this.getAttribute('data-age');
        });
    });
    
    // Обработчики для рейтинга
    document.querySelectorAll('.choice3 .criteria').forEach(button => {
        button.addEventListener('click', function() {
            document.querySelectorAll('.choice3 .criteria').forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            selectedStar = this.getAttribute('data-star');
        });
    });
    

    // Обработчик кнопки поиска
    document.querySelector('.search-button').addEventListener('click', function() {
        if (!selectedGenre || !selectedAge) {
            alert('Пожалуйста, выберите жанр и возрастное ограничение');
            return;
        }

        // Обработчики для страны
    document.querySelectorAll('.choice4 .criteria').forEach(button => {
        button.addEventListener('click', function() {
            document.querySelectorAll('.choice4 .criteria').forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            selectedStar = this.getAttribute('data-country');
        });
    });
        
        fetch('/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                genre: selectedGenre,
                age_rating: selectedAge,
                star: selectedStar,
                country: selectedcountry
            })
        })
        .then(response => response.json())
        .then(data => {
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '';
            
            
            
            data.forEach(movie => {
                const movieDiv = document.createElement('div');
                movieDiv.className = 'movie';
                const encodedTitle = encodeURIComponent(movie.title);
                movieDiv.innerHTML = `
                    <h3 style="color:white">${movie.title}</h3>
                    <a href="/movie/${encodedTitle}">
                        <img src="${movie.image}" alt="${movie.title}">
                    </a>
                `;
                resultsDiv.appendChild(movieDiv);
            });

            if (data.length === 0) {
                resultsDiv.innerHTML = '<p>Фильмы не найдены</p>';
                return;
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});