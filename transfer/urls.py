from django.contrib import admin
from django.urls import path
from . import views

from django.urls.resolvers import URLPattern
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index,name='index'),

    path("customers", views.customers,name='customers'),

    path("history", views.history,name='history'),

    path("t_money", views.t_money,name='t_money'),
    path("about", views.about,name='about')

]

if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

    