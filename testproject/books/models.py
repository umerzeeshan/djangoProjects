from __future__ import unicode_literals

from django.db import models

class Books(models.Model):
	title = models.CharField(max_length=150)
	authon = models.CharField(max_length=100)
	read = models.CharField(max_length=3)
