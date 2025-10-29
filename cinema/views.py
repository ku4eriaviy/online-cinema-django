from django.shortcuts import render
from .data import MOVIES, GENRES

def home(request):
    # Получаем выбранный жанр из URL (например: ?genre=sci-fi)
    selected_genre = request.GET.get('genre', 'all')
    
    # Фильтруем фильмы
    if selected_genre == 'all':
        filtered_movies = MOVIES
    else:
        filtered_movies = [movie for movie in MOVIES if movie['genre'] == selected_genre]

    # Рендерим шаблон и передаём данные
    response = render(request, 'index.html', {
        'movies': filtered_movies,
        'genres': GENRES,
        'selected_genre': selected_genre,
    })
    
    # Сохраняем выбор в cookie на 30 дней
    response.set_cookie('last_genre', selected_genre, max_age=30*24*60*60)
    
    return response
