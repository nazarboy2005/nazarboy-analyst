from django.db import models


class ContactInfoModel(models.Model):
    contact_bio = models.TextField()
    address = models.CharField(max_length=125, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contact Info'
        verbose_name_plural = 'Contact Infos'