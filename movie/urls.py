from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reviews/', views.reviews, name='reviews'),
    path('films/', views.films, name='films'),
    path('filmDetail/<int:id>', views.filmDetail, name='detail'),
    path('newfilm/', views.newFilm, name='newfilm'),
    path('newreview/', views.newReview, name='newreview'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]