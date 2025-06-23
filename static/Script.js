document.addEventListener('DOMContentLoaded', function() {
    let selectedGenre = null;
    let selectedAge = null;
    
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
    
    // Обработчик кнопки поиска
    document.querySelector('.search-button').addEventListener('click', function() {
        if (!selectedGenre || !selectedAge) {
            alert('Пожалуйста, выберите жанр и возрастное ограничение');
            return;
        }
        
        fetch('/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                genre: selectedGenre,
                age_rating: selectedAge
            })
        })
        .then(response => response.json())
        .then(data => {
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '';
            
            if (data.length === 0) {
                resultsDiv.innerHTML = '<p>Фильмы не найдены</p>';
                return;
            }
            
            data.forEach(movie => {
                const movieDiv = document.createElement('div');
                movieDiv.className = 'movie';
                movieDiv.innerHTML = `
                    <h3>${movie.title}</h3>
                    <p><strong>Жанр:</strong> ${movie.genre}</p>
                    <p><strong>Возрастное ограничение:</strong> ${movie.age_rating}</p>
                    <p><strong>Год выпуска:</strong> ${movie.year}</p>
                `;
                resultsDiv.appendChild(movieDiv);
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});