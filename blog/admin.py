from django.contrib import admin
from django.contrib.admin import display

from .models import Post, UserTrainer
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


# Register your models here.

# admin.py
class CustomUserAdmin(UserAdmin):
    model = UserTrainer
    add_form = CustomUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'TrainerInfo',
            {
                'fields': (
                    'age', 'info', 'image', 'inst',
                )
            }
        )
    )


admin.site.register(UserTrainer, CustomUserAdmin)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('article', 'slug', 'trainer')
    list_display_links = ('article',)
    fields = ('article', 'slug', 'keywords', 'text', 'trainer')
    readonly_fields = ()
