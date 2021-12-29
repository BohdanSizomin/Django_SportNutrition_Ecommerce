from django.contrib import admin
from home.models import Category, SubCategory, Product, Variation, ReviewRating,Product


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
    list_display = ('name', 'slug',)
    list_filter = ('name',)


class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
    list_display = ('name', 'slug', 'category')
    list_filter = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category', 'subcategory', 'create_date')
    prepopulated_fields = {'slug': ('name',), }
    list_filter = ('is_available',)
    search_fields = ('name',)


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value',)




admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating)
