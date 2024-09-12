from django.db import models

class Decade(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.CharField(max_length=100)
    end_year = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Fad(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.TextField()
    description = models.CharField(max_length=100)
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fad')

    def __str__(self):
        return self.name