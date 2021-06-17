from django.shortcuts import render, get_object_or_404
from .models import Film, MovieType, Review
from django.urls import reverse_lazy
from .forms import FilmForm, ReviewForm



# Create your views here.
def index(request):
    return render(request, 'movie/index.html')

def reviews(request):
    review_list=Review.objects.all()
    return render(request, 'movie/reviews.html', {'review_list': review_list})

def films(request):
    film_list=Film.objects.all()
    return render(request, 'movie/films.html', {'film_list': film_list})

def filmDetail(request, id):
    film=get_object_or_404(Film, pk=id)
    return render(request, 'movie/filmdetail.html', {'film': film})

def newFilm(request):
    form=FilmForm

    if request.method=='POST':
        form=FilmForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=FilmForm()

    else:
        form=FilmForm()
        return render(request, 'movie/newfilm.html', {'form': form})

def newReview(request):
    form=ReviewForm

    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ReviewForm()

    else:
        form=ReviewForm()
        return render(request, 'movie/newreview.html', {'form': form})