from django.db import models

# Create your models here.
class Decade(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return self.name
    
class Fad(models.Model):
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='songs')
    name = models.CharField(max_length=100, default='no name selected')
    image_url = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title