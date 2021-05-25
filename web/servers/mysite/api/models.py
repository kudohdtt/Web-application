from django.db import models


# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=50)
    num_star = models.FloatField()
    address = models.TextField(max_length=100)
    script = models.TextField(max_length=200)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name





