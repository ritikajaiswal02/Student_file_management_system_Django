from django.db import models

# Create your models here.
class StudentModel(models.Model):
	rno = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=40)
	ms = models.ImageField()
	
	def __str__(self):
		return str(self.name)