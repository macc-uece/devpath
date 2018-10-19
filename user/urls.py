from django.urls import path

from user import views

app_name = 'user'
urlpatterns = [
    path('register', views.CreateView.as_view(), name='create_view'),
]