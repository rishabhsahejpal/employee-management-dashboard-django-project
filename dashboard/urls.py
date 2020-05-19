from django.urls import path

from . import views

urlpatterns = [
	path('<int:employee_id>/', views.index , name='index'),
	path('documentation/',views.documentation, name = 'documentation'),
	path('resources/',views.resources, name = 'resources'),
	path('ajax/<str:action>/', views.ajax_calls , name='ajax_calls'),
]