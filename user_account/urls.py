from django.urls import path
from . import views

urlpatterns = [
	path('', views.home_page, name='home_page'),
	path('login_page/', views.login_page, name='login_page'),
	path('sign_up/', views.sign_up, name='sign_up'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('login_check/', views.login_check, name='login_check'),
	path('logout/', views.logout, name='logout'),
	path('register/', views.register, name='register'),
]
