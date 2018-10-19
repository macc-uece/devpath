from django.urls import path
from .views import *

app_name = 'dashboard'
urlpatterns = [

	# urls for skills
	path('',list_skills, name='list_skills'),
	path('new',create_skill,name='create_skill'),
	path('update/<int:id>/', update_skill, name='update_skill'),
	path('delete/<int:id>/', delete_skill, name='delete_skill'),
	
]