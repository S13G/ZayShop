from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.


class Category(models.Model):
    Male = 'M'
    Female = 'F'

    Sale_sport = 'S'
    Sale_luxury = 'L'

    Bag_product = 'B'
    Sweather_product = 'S'
    Sunglass_product = 'SG'

    GENDER_CHOICES = [
        (Male, 'Male'),
        (Female, 'Female'),
    ]

    SALE_CHOICES = [
        (Sale_sport, 'Sports'),
        (Sale_luxury, 'Luxury'),
    ]

    PRODUCT_CHOICES = [
        (Bag_product, 'Bags'),
        (Sweather_product, 'Sweather'),
        (Sunglass_product, 'Sunglass'),
    ]

    title = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='', blank=True)
    sale = models.CharField(max_length=5, choices=SALE_CHOICES, default='', blank=True)
    product = models.CharField(max_length=5, choices=PRODUCT_CHOICES, default='', blank=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    featured_product = models.BooleanField(default=False, null=True)
    specifications = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=False, related_name='category')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
