from django.db import models

class Todo(models.Model):
	title = models.CharField(max_length=150)
	description = models.CharField(max_length=300, blank=True)
	content = models.CharField(max_length=3000, blank=True)
	time_create = models.DateTimeField(auto_now_add=True)
	time_update = models.DateTimeField(auto_now=True)
	is_published = models.BooleanField(default=True)
	status = models.ForeignKey("Status", verbose_name='Статус', on_delete=models.CASCADE)

	def __str___(self):
		return self.title

class Status(models.Model):
	name = models.CharField(max_length=100, db_index=True)

	def __str__(self):
		return self.name