from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    title = models.CharField(max_length=100, verbose_name='Título')
    content = models.TextField(verbose_name='Conteudo')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Data de publicação')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    tags = models.ManyToManyField('Tag', related_name='posts', verbose_name='Marcadores')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Tag(models.Model):

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name