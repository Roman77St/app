from django.shortcuts import render
from goods.models import Categories


def index(request):
    categories = Categories.objects.all()
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели Home',
        'categories': categories,
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'content': 'О нас', 
        'text_on_page': 'Текст о том, почему мебель нужно покупать именно у нас.'
    }
    return render(request, 'main/about.html', context)
