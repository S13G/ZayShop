from autoslug import AutoSlugField
from django.core.validators import MinValueValidator
from django.db import models

from common.models import TimeStampedUUID


# Create your models here.


class Category(TimeStampedUUID):
    name = models.CharField(max_length=255, null=True)
    slug = AutoSlugField(populate_from=name, unique=True, always_update=True, null=True)

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"


class SubCategory(TimeStampedUUID):
    GENDER_CHOICES = (
        ("M", "MALE"),
        ("F", "FEMALE")
    )
    name = models.CharField(max_length=255, null=True)
    slug = AutoSlugField(populate_from=name, unique=True, always_update=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="sub_category")
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, default="M", null=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return f"{self.name} - {self.category}"


class Product(TimeStampedUUID):
    SIZE_CHOICES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large')
    )
    name = models.CharField(max_length=255, null=True)
    slug = AutoSlugField(populate_from=name, unique=True, always_update=True, null=True)
    category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, related_name="products")
    product_main_image = models.ImageField(default="assets/img/default.jpg", upload_to="media", null=True)
    second_product_image = models.ImageField(default="assets/img/default.jpg", upload_to="media", null=True, blank=True)
    third_product_image = models.ImageField(default="assets/img/default.jpg", upload_to="media", null=True, blank=True)
    fourth_product_image = models.ImageField(default="assets/img/default.jpg", upload_to="media", null=True, blank=True)
    fifth_product_image = models.ImageField(default="assets/img/default.jpg", upload_to="media", null=True, blank=True)
    description = models.TextField(null=True)
    available_color = models.CharField(max_length=400, null=True, blank=True)
    specifications = models.TextField(null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    sizes = models.CharField(max_length=255, choices=SIZE_CHOICES, default=None, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0)], null=True)
    quantity = models.PositiveIntegerField(default=0, null=True)
    featured = models.BooleanField(default=False, null=True)

    class Meta:
        ordering = ["-created", "name"]

    def __str__(self):
        return f"{self.name} - {self.category}"
