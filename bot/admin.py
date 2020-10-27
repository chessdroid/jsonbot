from django.contrib import admin
from .models import Account



@admin.register(Account)
class RespondentAdmin(admin.ModelAdmin):
    search_fields = ("first_name", "last_name", "username")
    list_display = ("first_name", "last_name", "username",)
