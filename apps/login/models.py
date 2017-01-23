from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import bcrypt
import re
import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex = re.compile(r'^[A-Za-z]{2}')
password_regex = re.compile(r'^.{8}')
# Create your models here.
class LoginManager(models.Manager):
	def register(self, user, alias, email, passw, confirm, date):
		errors = []
		if User.objects.filter(alias = alias).exists() == True:
			errors.append('Alias already exists!')
		if not name_regex.match(user):
			errors.append('first name must be no fewer than 2 characters and letters only')
		if User.objects.filter(email = email).exists() == True:
			errors.append('email already in use')
		if not EMAIL_REGEX.match(email):
			errors.append('Please enter a valid email')
		if not password_regex.match(passw):
			errors.append('password must be no fewer than 8 characters')
		if passw != confirm:
			errors.append('passwords must match')
		if not date:
			errors.append('please enter a date')
		if len(errors) != 0:
			return (False, errors)
		else:
			passw = passw.encode()
			hashed = bcrypt.hashpw(passw, bcrypt.gensalt())
			e = User.objects.create(username = user, alias = alias, email = email, password = hashed, dob = date)
			e.save()
			return (True, e)
	def login(self, email, password):
		errors = []
		try:
			result = User.objects.get(email = email)
		except:
			errors.append('Email does not exist')
			return (False, errors)
		if not bcrypt.hashpw(password.encode(), result.password.encode()) == result.password.encode():
			errors.append('password is incorrect')
			return (False, errors)
		return (True, result)

class User(models.Model):
	username = models.CharField(max_length=50)
	alias = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=200)
	dob = models.DateField(blank = True, null = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = LoginManager()
