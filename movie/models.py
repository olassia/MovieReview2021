from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MovieType(models.Model):
    typename=models.CharField(max_length=255)
    typedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.typename

    class Meta:
        db_table='movietype'


class Film(models.Model):
    filmname=models.CharField(max_length=255)
    filmtype=models.ForeignKey(MovieType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateentered=models.DateField()
    filmurl=models.URLField()
    description=models.TextField()

    def __str__(self):
        return self.filmname

    class Meta:
        db_table='film'


class Review(models.Model):
    title=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    film=models.ForeignKey(Film, on_delete=models.CASCADE)
    reviewdate=models.DateField()
    reviewtext=models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table='review'                        
