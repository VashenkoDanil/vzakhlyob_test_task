from django.core.validators import MinValueValidator
from django.db import models

from apps.account.models import User


def stories_user_directory_path(instance, filename):
    return f'stories/user_{instance.user.id}/{filename}'


class Story(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    cover = models.ImageField(verbose_name='Обложка', upload_to='stories/')

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'

    def __str__(self):
        return f'{self.title} {self.author}'


class Episode(models.Model):
    story = models.ForeignKey(Story,
                              verbose_name='История',
                              on_delete=models.CASCADE,
                              related_name='stories',
                              related_query_name='episode')
    episode_number = models.PositiveIntegerField(verbose_name='Номер эпизода',
                                                 validators=[MinValueValidator(1)])
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Эпизод'
        verbose_name_plural = 'Эпизоды'
        unique_together = ('story', 'episode_number')

    def __str__(self):
        return f'{self.story} {self.episode_number}'
