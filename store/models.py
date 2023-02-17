import secrets

from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from common.models import BaseModel


# Create your models here.


class Country(BaseModel):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class Customer(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)


class Category(BaseModel):
    name = models.CharField(max_length=255, null=True)
    slug = AutoSlugField(populate_from="name", unique=True, always_update=True, null=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"


class SubCategory(BaseModel):
    name = models.CharField(max_length=255, null=True)
    slug = AutoSlugField(populate_from="name", unique=True, always_update=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="sub_category")

    class Meta:
        ordering = ["-created"]
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return f"{self.name} - {self.category}"


class Size(BaseModel):
    name = models.CharField(max_length=255, null=True, unique=True, blank=True)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return f"{self.name}"


class Color(BaseModel):
    name = models.CharField(max_length=255, null=True, unique=True, blank=True)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return f"{self.name}"


class SelectProductManager(models.Manager):
    def get_queryset(self):
        return super(SelectProductManager, self).get_queryset().select_related('category')


class Product(BaseModel):
    ALL_GENDER = "A"
    ALL_MALE = "M"
    ALL_FEMALE = "F"
    GENDER_CHOICES = (
        (ALL_GENDER, "ALL"),
        (ALL_MALE, "MALE"),
        (ALL_FEMALE, "FEMALE"),
    )
    objects = models.Manager()
    selected = SelectProductManager()
    name = models.CharField(max_length=255, null=True)
    slug = AutoSlugField(populate_from="name", unique=True, always_update=True, null=True)
    category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, related_name="products")
    description = models.TextField(null=True)
    available_color = models.ManyToManyField(Color, blank=True)
    specifications = models.TextField(null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, default=ALL_GENDER, null=True)
    sizes = models.ManyToManyField(Size, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0)], null=True)
    available_quantity = models.PositiveIntegerField(default=0, null=True)
    featured = models.BooleanField(default=None, null=True)

    class Meta:
        ordering = ["-created", "name"]

    def __str__(self):
        return f"{self.name} = {self.category}"

    @property
    def display_sizes(self):
        sizes_list = []
        for size in self.sizes.values_list('name', flat=True):
            sizes_list.append(size)
        sizes = '/'.join(str(item) for item in sizes_list)
        return sizes

    @property
    def display_color(self):
        colors_list = []
        for color in self.available_color.values_list('name', flat=True):
            colors_list.append(color)
        colors = '/'.join(str(item) for item in colors_list)
        return colors


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = ProcessedImageField(processors=[ResizeToFill(257, 343)], format='JPEG', options={'quality': 60}, null=True)

    def __str__(self):
        return self.product.name

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = None
        return url


class ShippingAddress(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name="address")
    first_name = models.CharField(max_length=1000, null=True)
    last_name = models.CharField(max_length=1000, null=True)
    email = models.EmailField(max_length=1000, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True)
    address1 = models.CharField(max_length=1000, null=True)
    address2 = models.CharField(max_length=1000, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.IntegerField(null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Shipping Addresses'

    def __str__(self):
        return f"{self.customer} = {self.order}"


class Order(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name="order")
    tx_ref = models.CharField(max_length=10, null=True, blank=True, unique=True)
    placed_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE, blank=True, null=True)
    payment_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer} = {self.payment_complete}"

    def save(self, *args, **kwargs) -> None:
        while not self.tx_ref:
            allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
            unique_code = "".join(secrets.choice(allowed_chars) for i in range(10))
            tx_ref = unique_code
            similar_obj_tx_ref = Order.objects.filter(tx_ref=tx_ref)
            if not similar_obj_tx_ref:
                self.tx_ref = tx_ref
        super().save(*args, **kwargs)


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, related_name='items', null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name="orderitems")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='orderitems', null=True)
    color = models.ForeignKey(Color, related_name="orderitems", on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product} = {self.quantity} = {self.unit_price}"

    @property
    def get_total(self):
        product = self.product
        price = product.price
        self.unit_price = price * self.quantity
        return self.unit_price


class Cart(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name="carts")
    order_items = models.ForeignKey(OrderItem, on_delete=models.SET_NULL, null=True, related_name="carts")
