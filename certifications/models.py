from django.utils import timezone
from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import URLValidator


class BioModel(models.Model):
    bio = models.TextField()

    class Meta:
        verbose_name = 'Certifications Bio'
        verbose_name_plural = 'Certifications Bios'



class CategoriesModel(models.Model):
    name = models.CharField(max_length=25)
    to_display = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def joined_name(self):
        return '_'.join(self.name.split(' '))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



class CertificationsModel(models.Model):
    title = models.CharField(max_length=125)

    image = CloudinaryField('image', null=True, blank=True)  # For photos

    description = models.TextField()
    category = models.ForeignKey(
        CategoriesModel,
        on_delete=models.PROTECT,
        related_name='certifications'
    )
    given_time = models.DateField(default=timezone.now)
    given_by = models.CharField(max_length=100)
    link = models.URLField(null=True, blank=True, validators=[URLValidator(message="Enter a valid URL.")])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"
        ordering = ['-given_time']

    def __str__(self):
        return self.title

