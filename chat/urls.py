from django.urls import path
from chat import views

app_name = 'home'
urlpatterns = [
	path('', views.index, name='index'),
]
