from django.db import models

# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    content = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.content)

        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.content


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    ctg = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    gabarit_uzun = models.IntegerField()
    gabarit_eni = models.IntegerField()
    gabarit_baland = models.IntegerField()
    is_spalni = models.BooleanField()
    spalni_uzun = models.IntegerField(null=True, blank=True)
    spalni_eni = models.IntegerField(null=True, blank=True)
    spalni_baland = models.IntegerField(null=True, blank=True)
    color = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class ProductImg(models.Model):
    img = models.ImageField()
    pro = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
