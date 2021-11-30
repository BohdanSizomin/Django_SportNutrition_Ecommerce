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
    fields = ('article', 'slug', 'keywords', 'text', 'preview_image', 'is_published')
    readonly_fields = ('trainer',)
    list_filter = ('article', 'is_published')
    search_fields = ('trainer', 'article')

    def save_model(self, request, obj, form, change):
        obj.trainer = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.trainer != request.user:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.trainer != request.user:
            return False
        return True

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('article', 'slug', 'trainer')
#     list_display_links = ('article',)
#     fields = ('article', 'slug', 'keywords', 'text', 'trainer')
#     readonly_fields = ()
