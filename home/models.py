from django.db import models
from ckeditor.fields import RichTextField
from django.db.models import Avg, Count
from django.urls import reverse
from users.models import Account


# Create your models here.


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = RichTextField(max_length=700, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=None, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50)
    description = RichTextField(max_length=700, blank=False)

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
    old_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=0)

    stock = models.IntegerField(default=10)
    is_available = models.BooleanField(default=True)
    is_hot_offer = models.BooleanField(default=False)

    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    subcategory = models.ForeignKey('SubCategory', on_delete=models.CASCADE, blank=True, null=True)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def averageReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def countReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count

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


class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
