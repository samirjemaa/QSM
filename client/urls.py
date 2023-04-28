
from django.contrib import admin
from django.urls import path

from client import views

urlpatterns = [
    path('', views.ClientPage, name='clientpage'),
    path('list/', views.ClientList, name='listclient'),
    path('<int:id>/', views.ClientDetail, name='detailclient'),
    path('add/', views.create_Client, name='addclient'),
    path('edit/<int:id>/', views.update_Client, name='editclient'),
    path('delete/<int:id>/', views.delete_Client, name='deleteclient'),
]
