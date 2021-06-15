from movie.models import Review
from django.shortcuts import render, get_object_or_404
from .models import Film, MovieType, Review
from django.urls import reverse_lazy



# Create your views here.
def index(request):
    return render(request, 'movie/index.html')

def reviews(request):
    review_list=Review.objects.all()
    return render(request, 'movie/reviews.html', {'review_list': review_list})

