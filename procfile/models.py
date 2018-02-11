from django.db import models

# Create your models here.
class total(models.Model):


    name = models.CharField(max_length=12)

    email=models.EmailField(max_length=120)
    description = models.TextField(default="description text")
    phno = models.IntegerField()

    def __str__(self):
        return (self.name)