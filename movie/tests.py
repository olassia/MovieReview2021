from django.test import TestCase
from django.contrib.auth.models import User
from .models import MovieType, Film, Review
import datetime
from .forms import FilmForm, ReviewForm
from django.urls import reverse_lazy, reverse

# Create your tests here.

class MovieTypeTest(TestCase):
    def setUp(self):
        self.type=MovieType(typename='Horror')
    
    def test_typestring(self):
        self.assertEqual(str(self.type), 'Horror')

    def test_tablename(self):
        self.assertEqual(str(MovieType._meta.db_table), 'movietype') 


class FilmTest(TestCase):
    def setUp(self):
        self.type=MovieType(typename='Comedy')
        self.user=User(username='user1')
        self.film=Film(filmname='Young Frankenstein', filmtype=self.type, user=self.user, dateentered=datetime.date(2021,6,17), filmurl='http://www.youngfrankenstein.com', description="lolz")

    def test_string(self):
        self.assertEqual(str(self.film), 'Young Frankenstein')

    def test_tablename(self):
        self.assertEqual(str(Film._meta.db_table), 'film')  


class ReviewTest(TestCase):
    def setUp(self):
        self.film=Film(filmname='IT')
        self.user=User(username='user1')
        self.review=Review(title='Scurry', reviewdate=datetime.date(2021,6,17), reviewtext="This movie is so scary!")

    def test_string(self):
        self.assertEqual(str(self.review), 'Scurry')

    def test_tablename(self):
        self.assertEqual(str(Review._meta.db_table), 'review')


class NewFilmForm(TestCase):
    def test_filmform(self):
        data={
               'filmname': 'Robin Hood: Men in Tights', 
               'filmtype' : 'Comedy', 
               'user': 'Nick', 
               'dateentered': '2021-6-17',
               'filmurl': 'http://www.MelBrooks.com',
               'description': 'Funny Mel Brooks film.'
            } 

        form=FilmForm (data)
        self.assertTrue(form.is_valid)


class NewReviewForm(TestCase):
    def test_reviewform(self):
        data={
               'title': 'The Laughs keep on coming',  
               'user': 'Nick',
               'film': 'Robin Hood: Men in Tights', 
               'reviewdate': '2021-6-17',
            } 

        form=ReviewForm (data)
        self.assertTrue(form.is_valid) 


class New_Film_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.type=MovieType.objects.create(typename='Horror')
        self.product=Film.objects.create(filmname='IT',filmtype=self.type, user=self.test_user, dateentered=datetime.date(2021,6,17), filmurl='http://www.IT.com', description="Scary clown movie")

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newfilm'))
        self.assertRedirects(response, '/accounts/login/?next=/movie/newfilm/')                           