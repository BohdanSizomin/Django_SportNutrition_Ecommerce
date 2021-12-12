from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


# Create your models here.


class Brand(models.Model):
    ENGLAND = 'England'
    USA = "United States"
    POLAND = "Poland"
    HUNGARY = "Hungary"
    CANADA = "Canada"

    BRAND_CHOICES = [
        (ENGLAND, 'England'),
        (USA, 'United States'),
        (POLAND, "Poland"),
        (HUNGARY, "Hungary"),
        (CANADA, "Canada"),
    ]

    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(
        max_length=20,
        choices=BRAND_CHOICES,
        default=USA,
    )

    def __str__(self):
        self.name + self.manufacturer

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = RichTextField(max_length=255, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=None, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50)
    description = RichTextField(max_length=255, blank=False)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='media/items')

    price = models.DecimalField(max_digits=6, decimal_places=2)
    old_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=0)

    stock = models.IntegerField(default=10)
    is_available = models.BooleanField(default=True)
    is_hot_offer = models.BooleanField(default=False)

    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    subcategory = models.ForeignKey('SubCategory', on_delete=models.CASCADE)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    # Product variants
    # weight = models.CharField(max_length=20, choices=WEIGHT_CHOICES, default=kilogram)
    # taste = models.CharField(max_length=20, choices=TASTE_CHOICES, default=chocolate)
    # brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    class Meta:
        order_with_respect_to = 'create_date'
        verbose_name = 'Product'
        verbose_name_plural = 'Items'


VARIATION_CHOICES = [
    ('taste', 'taste'),
    ('weight', 'weight')
]


class VariationManager(models.Manager):
    def tastes(self):
        return super(VariationManager, self).filter(variation_category='taste', is_active=True)

    def weights(self):
        return super(VariationManager, self).filter(variation_category='weight', is_active=True)


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=30, choices=VARIATION_CHOICES)
    variation_value = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_value
