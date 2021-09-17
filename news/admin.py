from django.contrib import admin

from .models import News, Tag, NewsTag


class NewsTagInline(admin.TabularInline):
    model = NewsTag


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'text',
        'pub_date',
        'image',
        'author'
    )
    inlines = [
        NewsTagInline,
    ]
    search_fields = ('title',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
    exclude = ('views',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug',
    )
    search_fields = ('name',)
    empty_value_display = '-пусто-'
