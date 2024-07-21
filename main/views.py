from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели Home'
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'content': 'О нас', 
        'text_on_page': 'Текст о том, почему мебель нужно покупать именно у нас.'
    }
    return render(request, 'main/about.html', context)
