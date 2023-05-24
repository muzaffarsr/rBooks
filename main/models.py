from django.db import models


class Category(models.Model):
	name = models.CharField(max_length = 30)

	def __str__(self):
		return self.name


class Book(models.Model):
	img = models.TextField('Book Image Link')
	name = models.TextField('Book Name')
	text = models.TextField('Book Text')
	price = models.FloatField('Book Price $')
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.price

	def __str__(self):
		return self.text

	def __str__(self):
		return self.name