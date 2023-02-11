# import PIL.Image as pillow_image
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from common.models import TimeStampedUUID


# Create your models here.


class Customer(TimeStampedUUID):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)


class Category(TimeStampedUUID):
    name = models.CharField(max_length=255, null=True)
    slug = AutoSlugField(populate_from="name", unique=True, always_update=True, null=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"


class SubCategory(TimeStampedUUID):
    name = models.CharField(max_length=255, null=True)
    slug = AutoSlugField(populate_from="name", unique=True, always_update=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="sub_category")

    class Meta:
        ordering = ["-created"]
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return f"{self.name} - {self.category}"


class Size(TimeStampedUUID):
    name = models.CharField(max_length=255, null=True, unique=True, blank=True)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return f"{self.name}"


class Color(TimeStampedUUID):
    name = models.CharField(max_length=255, null=True, unique=True, blank=True)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return f"{self.name}"


class SelectProductManager(models.Manager):
    def get_queryset(self):
        return super(SelectProductManager, self).get_queryset().select_related('category')


class Product(TimeStampedUUID):
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
    product_main_image = ProcessedImageField(processors=[ResizeToFill(257, 343)], format='JPEG',
                                             options={'quality': 60}, null=True)
    second_product_image = ProcessedImageField(processors=[ResizeToFill(600, 600)], format='JPEG',
                                               options={'quality': 60}, null=True, blank=True)
    third_product_image = ProcessedImageField(processors=[ResizeToFill(600, 600)], format='JPEG',
                                              options={'quality': 60}, null=True, blank=True)
    fourth_product_image = ProcessedImageField(processors=[ResizeToFill(600, 600)], format='JPEG',
                                               options={'quality': 60}, null=True, blank=True)
    fifth_product_image = ProcessedImageField(processors=[ResizeToFill(600, 600)], format='JPEG',
                                              options={'quality': 60}, null=True, blank=True)
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

    # code can be used in replacement for the imagekit library
    # def save(self, *args, **kwargs):
    #     super(Product, self).save(*args, **kwargs)
    #     # this code is adjusting the image to fit the box default sizes so as to prevent different box sizes
    #     product_main_image = self.product_main_image
    #     product_main_image.open()
    #     img = pillow_image.open(product_main_image)
    #     width, height = img.size
    #     if height < 257 or height > 257:
    #         height = 257
    #     target_width = 257
    #     height_coefficient = width / 257
    #     target_height = height / height_coefficient
    #     img = img.resize((int(target_width), int(target_height)), pillow_image.ANTIALIAS)
    #     img.save(product_main_image.path, 'JPEG', quality=95)
    #     img.close()
    #     product_main_image.close()

    @property
    def image_urls(self):
        try:
            url = [self.product_main_image, self.second_product_image, self.third_product_image,
                   self.fourth_product_image]
        except:
            url = ''
        return url

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


class Order(TimeStampedUUID):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name="order")
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer} = {self.payment_complete}"


class OrderItem(TimeStampedUUID):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, related_name='items', null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='orderitems', null=True)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    placed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} = {self.quantity} = {self.unit_price}"


class Cart(TimeStampedUUID):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name="cart")
    order_items = models.ForeignKey(OrderItem, on_delete=models.SET_NULL, null=True, related_name="cart")


class ShippingAddress(TimeStampedUUID):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name="address")
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, related_name="shipping_address")
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Shipping Addresses'

    def __str__(self):
        return f"{self.customer} = {self.order}"
