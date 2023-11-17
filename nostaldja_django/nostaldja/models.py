from django.db import models

# Create your models here.
class Decades(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.CharField()
    end_year = models.CharField()

    def __str__(self):
        return self.name

class Fads(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.CharField()
    description = models.TextField(max_length=200)
    decade = models.TextField()

    def __str__(self):
        return self.name
