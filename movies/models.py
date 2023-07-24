from django.db import models

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    year = models.PositiveIntegerField()
    runtime = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    posterimage = models.ImageField(upload_to='movie')

    def __str__(self):
        return self.name
    


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.name}"