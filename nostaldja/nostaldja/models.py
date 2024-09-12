from django.db import models

# Create your models here.
class Decade(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.CharField(max_length=100)
    end_year = models.CharField(max_length=100)

class Fad(models.Model):
    name = models.CharField(max_length=100, default='no description')
    image_url = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=200,)
    description = models.CharField(max_length=100, default='no description')
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fads')

    def __str__(self):
        return self.name