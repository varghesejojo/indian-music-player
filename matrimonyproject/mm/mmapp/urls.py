from django.urls import path
from . import views
app_name='mmapp'
urlpatterns = [
    path('',views.log_in,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_user,name='logout'),
    path('thank/',views.thank,name='thank'),
    path('contact/',views.contact,name='contact'),

]
