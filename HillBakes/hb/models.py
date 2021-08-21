from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import PROTECT 

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=75, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='product')
    costField = models.ManyToManyField('Cost', related_name='product')
    image = models.ImageField(upload_to='product', blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=75, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Cost(models.Model):
    name = models.CharField(max_length=75, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name