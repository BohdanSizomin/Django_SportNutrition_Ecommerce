from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import Account


# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'username')
    readonly_fields = ('password', 'date_joined',)
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ('is_active','username')
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
