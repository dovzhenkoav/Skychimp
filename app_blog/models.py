from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=128, verbose_name='заголовок')
    text = models.TextField(verbose_name='тело')
    image = models.ImageField(upload_to='blog/', verbose_name='картинка')
    view_counter = models.IntegerField(default=0, verbose_name='просмотры')
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name='время публикации')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
