from django.urls import path

from . import views


#app_name = 'sightings'

urlpatterns = [
	path('',views.all_squir,name = 'list_all'),
	path('add/',views.add_a_squir,name = 'add'),
	path('stats/',views.squir_stats,name='stats'),
	path('<sid>/',views.edit_squir,name='edit'),	
]

