from django.urls import path
from dashboard import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'dashboard'
urlpatterns = [

    # urls for skills
    # path('',list_skills, name='list_skills'),
    # path('new',create_skill,name='create_skill'),
    # path('update/<int:id>/', update_skill, name='update_skill'),
    # path('delete/<int:id>/', delete_skill, name='delete_skill'),

    path('', views.index, name='index'),
    path('servicos', views.servicos, name='servicos'),
    path('contato', views.contato, name='contato')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
