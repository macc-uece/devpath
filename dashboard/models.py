from django.db import models

# Create your models here.
class Skill(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	level = models.IntegerField()

	def __srt__(self):
		return self.name