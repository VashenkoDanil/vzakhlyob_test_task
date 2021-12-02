# Generated by Django 3.2.8 on 2021-10-19 08:17

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок')),
                ('cover', models.ImageField(upload_to='stories/', verbose_name='Обложка')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'История',
                'verbose_name_plural': 'Истории',
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode_number', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Номер эпизода')),
                ('text', models.TextField(verbose_name='Текст')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', related_query_name='episode', to='story.story', verbose_name='История')),
            ],
            options={
                'verbose_name': 'Эпизод',
                'verbose_name_plural': 'Эпизоды',
                'unique_together': {('story', 'episode_number')},
            },
        ),
    ]
