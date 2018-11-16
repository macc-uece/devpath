from django.urls import path
from user_manager import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'user_manager'

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.dev_login, name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


