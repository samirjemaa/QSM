
from django.contrib import admin
from django.urls import path

from societe import views

urlpatterns = [
    path('', views.SocietePage, name='societepage'),
    path('list/', views.SocieteList, name='listsociete'),
    path('<int:id>/', views.SocieteDetail, name='detailsociete'),
    path('add/', views.create_Societe, name='addsociete'),
    path('edit/<int:id>/', views.update_Societe, name='editsociete'),
    path('delete/<int:id>/', views.delete_Societe, name='deletesociete'),
]
