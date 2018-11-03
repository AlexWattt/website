from django.db import models
from django.urls import reverse
# database


class Post(models.Model):
    resturant = models.CharField(max_length=100)
    address = models.TextField()
    yelp = models.TextField()

    def __str__(self):
        return self.resturant
