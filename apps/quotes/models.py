from __future__ import unicode_literals
from ..login.models import User
from django.db import models

# Create your models here.
class Quotes(models.Model):
	quoter = models.CharField(max_length = 100)
	quote = models.TextField()
	user = models.ForeignKey(User)

class Favorites(models.Model):
	user = models.ForeignKey(User)
	quotes = models.ForeignKey(Quotes)