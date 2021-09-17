from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import News, Tag, Ip

User = get_user_model()


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    news_list = News.objects.all()
    paginator = Paginator(news_list, settings.PAGE_SIZE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'page': page,
    }
    return render(request, 'news/index.html', context)


def news_view(request, item_id):
    item = get_object_or_404(News, pk=item_id)
    ip = get_client_ip(request)
    if Ip.objects.filter(ip=ip).exists():
        item.views.add(Ip.objects.get(ip=ip))
    else:
        Ip.objects.create(ip=ip)
        item.views.add(Ip.objects.get(ip=ip))
    context = {
        'item': item,
    }
    return render(request, 'news/news.html', context)


def tag_news(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    news_list = tag.news.all()
    paginator = Paginator(news_list, settings.PAGE_SIZE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'tag': tag,
        'page': page
    }
    return render(request, 'news/tag.html', context)


def statistics(request):
    news_list = News.objects.all()
    paginator = Paginator(news_list, settings.PAGE_SIZE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'page': page,
    }
    return render(request, 'news/statistics.html', context)
