from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<region>/<ign>', views.index, name='summoner')
]
