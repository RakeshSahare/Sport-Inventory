from django.db import models

# Create your models here.

class Equipments(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100,decimal_places=2)

    def __str__(self):
        return self.name