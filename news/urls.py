from django.urls import path

from . import views

urlpatterns = [
    path('statistics/', views.statistics, name='statistics'),
    path('<int:item_id>/', views.news_view, name='news'),
    path('<slug:slug>/', views.tag_news, name='tag_news'),
    path('', views.index, name='index'),
]
