from django.conf.urls import url
from hello_world import views

urlpattern = [
	url(r'^$', views.index, name='index'),
]