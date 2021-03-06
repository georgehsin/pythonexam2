from django.shortcuts import render, redirect
from ..login.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Quotes, Favorites
# Create your views here.
def index(request):
	if 'id' not in request.session:
		return redirect(reverse('login:index'))
	users = User.objects.all().order_by('alias')
	user = User.objects.get(id = request.session['id'])
	userid = request.session['id']
	favorites = Favorites.objects.filter(user = user)
	quotes = Quotes.objects.exclude(favorites__user = user)
	context = {'user':user, 'quotes':quotes, 'favorites':favorites, "userid":userid, 'users':users}
	return render(request, 'quotes/index.html', context)

def about(request):
	user = User.objects.get(id = request.session['id'])	
	context = {'user':user}
	return render(request, 'quotes/about.html', context)	

def quote(request):
	x = False
	if len(request.POST['quoter'])<3:
		messages.error(request, "Quoted by must be more than 3 characters")
		x = True
	if len(request.POST['quote'])<10:
		messages.error(request, "Quote must be greater than 10 characters")
		x = True
	if x:
		return redirect(reverse('quotes:index'))
	user = User.objects.get(id = request.session['id'])
	Quotes.objects.create(quoter = request.POST['quoter'], quote = request.POST['quote'], user = user)
	return redirect(reverse('quotes:index'))

def favorite(request, id):
	user = User.objects.get(id = request.session['id'])
	quote = Quotes.objects.get(id = id)
	Favorites.objects.create(quotes = quote, user = user)
	return redirect(reverse('quotes:index'))

def delete(request, id):
	user = User.objects.get(id = request.session['id'])
	quote = Quotes.objects.get(id = id)
	Favorites.objects.filter(quotes = id).delete()
	return redirect(reverse('quotes:index'))	

def users(request, id):
	if 'id' not in request.session:
		return redirect(reverse('login:index'))
	user = User.objects.get(id = id)
	users = User.objects.all().order_by('alias')
	print user.alias
	quotes = Quotes.objects.filter(user = user)
	count = 0 
	for quote in quotes:
		count +=1
	context = {'user':user, 'users':users, 'count':count, 'quotes':quotes}
	return render(request, 'quotes/profile.html', context)

def dash(request):
	return redirect(reverse('quotes:index'))