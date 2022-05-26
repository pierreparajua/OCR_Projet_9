

from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    # date_hierarchy = 'publication_date'
    list_display = ('username', 'email', 'is_superuser', 'is_staff', 'is_active')
    list_filter = ('is_superuser', 'is_active')


# Register your models here.
admin.site.register(User, UserAdmin)
