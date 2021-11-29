from django.db import models
from ckeditor.fields import RichTextField


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


class SubCategory(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=50)
    description = RichTextField(max_length=255, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'


class Category(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=50)
    description = RichTextField(max_length=255, blank=False)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Item(models.Model):
    # Weight categories choices
    half_kilo = 'Half kilo'
    kilogram = "One kilo"
    twokilograms = "Two kilos"

    WEIGHT_CHOICES = [
        (half_kilo, '0.5kg'),
        (kilogram, "One kilo"),
        (twokilograms, "Two kilos"),
    ]

    # Taste categories choices
    banana = "Banana"
    chocolate = "Chocolate"
    vanilla = "Vanilla"
    cookies = "Cookies"
    latte = "Latte"

    TASTE_CHOICES = [
        (banana, "Banana"),
        (chocolate, "Chocolate"),
        (vanilla, "Vanilla"),
        (cookies, "Cookies"),
        (latte, "Latte"),
    ]

    slug = models.SlugField()
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    old_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.CharField(max_length=20, choices=WEIGHT_CHOICES, default=kilogram)
    taste = models.CharField(max_length=20, choices=TASTE_CHOICES, default=chocolate)
    is_hot_offer = models.BooleanField(default=False)
    in_stock_quantity = models.IntegerField(default=10)
    short_description = models.TextField(max_length=200)
    description = models.TextField(max_length=500)
    item_in_banner = models.BooleanField(blank=True)
    image = models.ImageField(upload_to='media/items')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # def get_category(self):
    #     return self.Category.name
    #
    # def get_subcategory(self):
    #     return self.SubCategory.name

    class Meta:
        order_with_respect_to = 'create_date'
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
