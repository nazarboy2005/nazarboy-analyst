from django.contrib import admin
from .models import ContactInfoModel


@admin.register(ContactInfoModel)
class ContactInfoModelAdmin(admin.ModelAdmin):
    list_display = ['email_address', 'phone_number']
