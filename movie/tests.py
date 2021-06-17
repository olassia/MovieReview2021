from django.test import TestCase
from django.contrib.auth.models import User
from .models import MovieType, Film, Review
import datetime
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


    #title=models.CharField(max_length=255)
    #reviewdate=models.DateField()
    #reviewtext=models.TextField()