from django.contrib import admin
from django.urls import path
from transfer import views

urlpatterns = [
    path('', views.index,name='index'),

    path("customers", views.customers,name='customers'),

    path("history", views.history,name='history'),

    path("t_money", views.t_money,name='t_money'),
    path("about", views.about,name='about')

]
