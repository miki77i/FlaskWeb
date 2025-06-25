document.addEventListener('DOMContentLoaded', function() {
    // Объект для хранения выбранных фильтров
    const selectedFilters = {
        genres: [],
        ages: [],
        stars: [],
        countries: []
    };
    
    // Функция для обработки кликов по фильтрам
    function setupFilterGroup(groupClass, filterType) {
        document.querySelectorAll(`.${groupClass} .criteria`).forEach(button => {
            button.addEventListener('click', function() {
                this.classList.toggle('active');
                const value = this.getAttribute(`data-${filterType}`);
                
                if (this.classList.contains('active')) {
                    // Добавляем фильтр
                    selectedFilters[filterType + 's'].push(value);
                } else {
                    // Удаляем фильтр
                    selectedFilters[filterType + 's'] = selectedFilters[filterType + 's'].filter(item => item !== value);
                }
            });
        });
    }

    
    
    // Инициализация всех групп фильтров
    setupFilterGroup('choice1', 'genre');
    setupFilterGroup('choice2', 'age');
    setupFilterGroup('choice3', 'star');
    setupFilterGroup('choice4', 'country');
    
    // Обработчик кнопки поиска
    document.querySelector('.search-button').addEventListener('click', function() {
        // Проверяем, что выбрано хотя бы что-то в каждой категории
        if (selectedFilters.genres.length === 0 || selectedFilters.ages.length === 0) {
            alert('Пожалуйста, выберите хотя бы один жанр и одно возрастное ограничение');
            return;
        }
        
        
        fetch('/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(selectedFilters)
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
                    <p>Оценка: ${movie.star}</p>
                    <p><strong>Год выпуска:</strong> ${movie.year}</p>
                    <img src="${movie.image}">
                `;
                resultsDiv.appendChild(movieDiv);
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});

document.querySelector('.reset-button').addEventListener('click', function() {
    // Сбрасываем все активные кнопки
    document.querySelectorAll('.criteria').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Очищаем выбранные фильтры
    for (const key in selectedFilters) {
        selectedFilters[key] = [];
    }
    
    // Очищаем результаты
    document.getElementById('results').innerHTML = '';
});