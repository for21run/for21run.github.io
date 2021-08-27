from django.db import models


class Articles(models.Model):
	title = models.Charfield('Название', max_length=20)
	task = models.TextField('Описание')

	def __str__(self):
		return self.title

"""
class articles(models.Model):
	title = models.Charfield('Название')
	task = models.TextField('Описание')

	def __str__(self):
		return self.title