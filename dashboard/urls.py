from django.urls import path
from dashboard import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('servicos', views.servicos, name='servicos'),
    path('contato', views.contato, name='contato'),
    path('dev/skills', views.add_skill, name='add_skill'),
    path('dev/education', views.add_education, name='add_education'),
    path('dev/experience', views.add_experience, name='add_experience'),
    path('dev/project', views.add_project, name='add_project'),
    path('dev/resume', views.load_resume, name='load_resume'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
