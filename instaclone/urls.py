from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns = [
  #landin page 
  url(r'^$',views.home, name ="home"),
  # navigating though 
  url(r'^explore/$',views.explore,name = "explore"),
  url(r'^favourites/$', views.favourites, name = "favourites"),
  url(r'^profile/$', views.profile,name = "profile" )
  
]