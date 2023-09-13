from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    objects = None
    name = models.CharField('Имя', max_length=30)
    content = models.CharField('Мечта', max_length=1000)
    date = models.DateField('Дата', auto_now_add=True)
    likes = models.IntegerField(verbose_name='Нравится', default=0)
    liked_by = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    # rating = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'


class Comment(models.Model):
    objects = None
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField('Имя', max_length=30)
    content = models.CharField('Комментарий', max_length=300)
    date = models.DateField('Дата', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

