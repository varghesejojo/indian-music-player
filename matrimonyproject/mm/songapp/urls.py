
from django.urls import path
from . import views
app_name='songapp'
urlpatterns = [
    path('home/',views.home,name='home'),
    path('about/', views.add_song, name='add_song'),
    path('play/<int:id>/',views.playsong,name='play'),
    path('favourite/', views.favourite, name='favourite'),

]

