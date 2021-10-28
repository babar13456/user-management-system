from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_page(request):
	return render(request, 'home.html')

def login_page(request):
	return render(request, 'login.html')

def login_check(request):
	username = request.POST['username']
	password = request.POST['password']
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request, user)
		messages.success(request, "Welcome User...")
		return redirect('dashboard')
	else:
		messages.error(request, "Invalid Username Or Password...")
		return redirect('login_page')

def logout(request):
	auth.logout(request)
	messages.error(request, "You have logout")
	return redirect('home_page')

def sign_up(request):
	return render(request, 'sign_up.html')

def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		username = request.POST['username']
		password = request.POST['password']
		password2 = request.POST['password2']

		if password == password2:
			if User.objects.filter(username=username).exists():
				messages.error(request, 'Username Already Taken')
				return render(request, 'sign_up.html')
			elif User.objects.filter(email=email).exists():
				messages.error(request, 'Email Already Exist Try a Different One...')
				return render(request, 'sign_up.html')
			else:
				user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
										username=username, password=password)
				user.save()
				return HttpResponse("User Created Successfully...")
		else:
			messages.error(request, 'Password Did not Matching...')
			return render(request, 'sign_up.html')
	else:
		return render(request, 'sign_up.html')

@login_required(login_url='login_check')
def dashboard(request):
	return render(request, 'dashboard.html')


