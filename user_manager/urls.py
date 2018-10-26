from django.urls import path
from user_manager import views

app_name = 'user_manager'

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.dev_login, name='login'),
]


