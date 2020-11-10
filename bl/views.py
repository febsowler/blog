from django.shortcuts import render, redirect
from .models import PostsModels

from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.models import User

from django.views.generic import DetailView

def login_url(request):
	args = {}
	if request.POST:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			args['login_error'] = 'Пользователь не найден'
			return render(request, 'bl/login.html', args)
	else:
		return render(request, 'bl/login.html', args)

def logout_url(request):
	auth.logout(request)
	return redirect("/")

def reg_url(request):
	args = {}
	if request.POST:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		email = request.POST.get('email', '')

		User.objects.create_user(username, email, password)
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			args['login_error'] = 'Пользователь не найден'
			return render(request, 'bl/reg.html', args)
	else:
		return render(request, 'bl/reg.html', args)

def index(request):
	listposts = PostsModels.objects.all()

	for i in listposts:
		if i.image == "":
			i.image = '/images/image.jpg'
	return render(request, 'bl/index.html', {"infposts": listposts})    

class PostView(DetailView):
	model = PostsModels
	template_name = 'bl/post_view.html'
		