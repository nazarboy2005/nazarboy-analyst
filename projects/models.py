from django.db import models
from cloudinary.models import CloudinaryField


class BioModel(models.Model):
    bio = models.TextField()

    class Meta:
        verbose_name = 'Project Bio'
        verbose_name_plural = 'Project Bios'

class CategoryModel(models.Model):
    name = models.CharField(max_length=25)
    to_display = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ProjectModel(models.Model):
    name = models.CharField(max_length=50)
    logo = CloudinaryField('image', blank=True, default='mydxtkgk21jlefrsghkn')
    short_description = models.CharField(max_length=150, null=True, blank=True)
    category = models.ManyToManyField(CategoryModel, related_name='projects')
    full_description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class SkillsAppliedModel(models.Model):
    skill = models.CharField(max_length=50)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, related_name='skills')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class ProjectInformationModel(models.Model):
    title = models.CharField(max_length=25)
    text = models.CharField(max_length=200)
    is_url = models.BooleanField(default=False)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, related_name='infos')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Info'
        verbose_name_plural = 'Infos'


class ProjectImageModel(models.Model):
    image = CloudinaryField('image')
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
