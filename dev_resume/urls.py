from django.urls import path
from dev_resume import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'resume'

urlpatterns = [
    path('/dev/resume', views.load_resume, name='resume')
]