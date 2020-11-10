from django.db import models

class PostsModels(models.Model):
	title_post = models.CharField('Имя модели', max_length=64)
	text_post = models.TextField('Обо мне')
	image = models.ImageField(upload_to='images')

	def __str__(self):
		return self.title_post

	def get_absolute_url(self):
		return "/post/%i/" % self.id
