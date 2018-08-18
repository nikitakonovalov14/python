from django.db import models

# Create your models here.
class Person(models.Model):
    first_name=models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

class no(models.Model):
    n = models.CharField(max_length=30)
class yes(models.Model):
    n = models.CharField(max_length=30)