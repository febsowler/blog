# Generated by Django 3.1.1 on 2020-11-09 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostsModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_post', models.CharField(max_length=32, verbose_name='Имя модели')),
                ('text_post', models.TextField(verbose_name='Обо мне')),
                ('image', models.ImageField(blank=True, upload_to='images')),
            ],
        ),
    ]
