from django.db import models

# Create your models here.
class Decade(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return self.name
    



class Fads(models.Model):
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='Fads')
    name = models.CharField(max_length=100, default='no fad name')
    description = models.CharField( default='no description')
    preview_url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name