from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from manger import views

urlpatterns = [
    path('',views.managerHome,name="managerHome"),
    path('magerLogin/',views.managerLogin,name="magerLogin"),
    path('recrutment/',views.recrutment,name="recrutment"),
    path('newrecuirtment/',views.newRecuirtment,name="newrecuirtment"),
    path('managerhome/',views.managerHomepage,name="managerHomepage"),



]
