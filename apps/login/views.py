from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

def index(request):
	return render(request, 'login/index.html')

def register(request):
	result = User.objects.register(request.POST['user'], request.POST['alias'], request.POST['email'], request.POST['passw'], request.POST['confirm'], request.POST['date'])
	if result[0]:
		request.session['id'] = result[1].id
		print request.session['id']
		return redirect(reverse('quotes:index'))
	else:
		for error in result[1]:
			messages.error(request, error)
	return redirect(reverse('login:index'))

def login(request):
	result = User.objects.login(request.POST['email'], request.POST['password'])
	if result[0]:
		request.session['id'] = result[1].id
		return redirect(reverse('quotes:index'))
	else:
		for error in result[1]:
			messages.error(request, error)
	return redirect(reverse('login:index'))

def logout(request):
	request.session.flush()
	return redirect(reverse('login:index'))