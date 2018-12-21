from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


# Create your models here.

COURSE = [
	('BtechCSE', 'B.Tech-CSE'),
	('BtechIT', 'B.Tech-IT'),
	('BtechECE', 'B.Tech-ECE'),
]

SEMESTER = [
	('First', 'First'),
	('Second', 'Second'),
	('Third', 'Third'),
	('Fourth', 'Fourth'),
	('Fifth', 'Fifth'),
	('Sixth', 'Sixth'),
	('Seventh', 'Seventh'),
	('Eighth', 'Eighth'),
]

class Paper(models.Model):
	course = models.CharField(max_length = 50, choices = COURSE)
	semester = models.CharField(max_length=50, choices = SEMESTER)
	subject = models.CharField(max_length = 100)
	year = models.IntegerField(validators=[MinValueValidator(2010), MaxValueValidator(datetime.date.today().year)])
	image = models.ImageField(upload_to = 'media/papers/usict')
