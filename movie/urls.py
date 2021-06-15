from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reviews/', views.reviews, name='reviews'),
]