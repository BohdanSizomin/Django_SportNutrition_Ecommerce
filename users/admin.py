from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from users.models import Account, UserProfile


# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'username')
    readonly_fields = ('password', 'date_joined',)
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ('is_active', 'username')
    fieldsets = ()


class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(
            '<img src="{}" width="30" height="30" style="border-radius:50%;">'.format(object.profile_picture.url))

    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'user', 'city', 'state', 'country')


admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile,UserProfileAdmin)