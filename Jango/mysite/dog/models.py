from django.db import models
import datetime

from django.utils import timezone

# Create your models here.

class Breed(models.Model):
	displayName = models.CharField(max_length=100, default='NULL')
	activity_level = models.CharField(max_length=7, default='NULL')
	coat_length = models.CharField(max_length=7, default='NULL')
	drools = models.BooleanField(max_length=7, default='NULL')
	good_with_children = models.BooleanField(max_length=7, default='NULL')
	grooming_demand = models.CharField(max_length=7, default='NULL')
	intelligence = models.CharField(max_length=7, default='NULL')
	shedding_level = models.CharField(max_length=7, default='NULL')
	size = models.CharField(max_length=12, default='NULL')
	imageName = models.CharField(max_length=100, default='NULL')
