from django.db import models

# Create your models here.
class Decade(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    # name ('eighties', 'nineties'...)
    # start_year
    # end_year

    def __str__(self):
        return self.name


class Fad(models.Model):
    pass
    name = models.CharField(max_length=100)
    image_url = models.TextField()
    description = models.TextField()
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='decades')
    # name
    # image_url
    # description
    # decade

    def __str__(self):
        return self.name
