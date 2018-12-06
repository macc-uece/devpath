from django.urls import path
from dashboard import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('servicos', views.servicos, name='servicos'),
    path('contato', views.contato, name='contato')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
