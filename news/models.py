from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Ip(models.Model):
    ip = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Айпишки'
        verbose_name = 'Айпишка'

    def __str__(self):
        return self.ip


class Tag(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)
    slug = models.SlugField(verbose_name='slug', unique=True)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['-id']

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='news',
        verbose_name='Автор'
    )
    tag = models.ManyToManyField(
        Tag,
        through='NewsTag',
        related_name='news',
        verbose_name='тэги'
    )
    views = models.ManyToManyField(
        Ip,
        related_name='news',
        blank=True,
        verbose_name='просмотры'
    )

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    def total_views(self):
        return self.views.count()


class NewsTag(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['news', 'tag'],
                name='unique_news_tag'
            )
        ]
