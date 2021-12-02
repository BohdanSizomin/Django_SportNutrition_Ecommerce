from django.contrib import admin
from django.contrib.admin import display
from .models import Contact


# Register your models here.

@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ('email', 'subject', 'created_at')
    list_display_links = ('subject', 'email')
    fields = ('email', 'subject', 'message', 'is_responsed')
    list_filter = ('subject', 'is_responsed', 'created_at')
