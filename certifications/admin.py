from django.contrib import admin
from certifications.models import CertificationsModel, CategoriesModel, BioModel


@admin.register(CategoriesModel)
class CategoriesModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'to_display']


@admin.register(CertificationsModel)
class CertificationsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'given_by']


@admin.register(BioModel)
class BioModelAdmin(admin.ModelAdmin):
    list_display = ['bio']