from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey


class Articles(models.Model):
    author: ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор статьи', blank=True,null=True)
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата и время публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
