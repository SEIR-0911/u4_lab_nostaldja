from django.db import models

class Decade(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.IntegerField(default=2000)
    end_year = models.IntegerField(default=2000) 

    def __str__(self):
        return self.name
    
class Fad(models.Model):
    name = models.CharField(max_length=100, default='no name')
    image_url = models.CharField(max_length=100, default='no image url')
    description = models.TextField(default='no desc.')
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='decades')

    def __str__(self):
        return self.name
