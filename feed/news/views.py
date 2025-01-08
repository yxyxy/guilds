from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm

def news_list(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')  # Перезагрузка страницы после добавления
    else:
        form = NewsForm()

    news = News.objects.order_by('-created_at')  # Сортировка новостей по дате (от новых к старым)
    return render(request, 'news/news_list.html', {'news': news, 'form': form})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')  # Название маршрута для списка новостей
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})

