from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('uregister',views.uregister,name='uregister'),
    path('ulogin',views.ulogin,name='ulogin'),

]