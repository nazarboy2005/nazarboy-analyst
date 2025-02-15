from django.db import models
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField

# ----------------Home Page Model----------------#


class HomePageModel(models.Model):
    name = models.CharField(max_length=30)
    quote = models.TextField(null=True)

    # image = models.ImageField(upload_to='home-image',
    #                           help_text="Image size should be 1920x1080 pixels. You can do it here: 👉https://imageresizer.com/👈 *** SIZE: 1920*1080 ***")
    image = CloudinaryField('image', help_text="Image size should be 1920x1080 pixels. You can do it here: 👉https://imageresizer.com/👈 *** SIZE: 1920*1080 ***")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Home Page'
        verbose_name_plural = 'Home Pages'


class TitleModel(models.Model):
    title = models.CharField(max_length=20, null=True)
    person = models.ForeignKey(HomePageModel, on_delete=models.CASCADE, related_name='titles')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'


class SocialMediaModel(models.Model):
    choices = (
        ('linkedin', 'linkedin'),
        ('github', 'github'),
        ('telegram', 'telegram'),
        ('instagram', 'instagram'),
        ('facebook', 'facebook'),
    )

    social_media_app = models.CharField(max_length=11, choices=choices)
    social_media_url = models.URLField()
    person = models.ForeignKey(HomePageModel, on_delete=models.CASCADE, related_name='social_media_apps')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.social_media_app

    class Meta:
        verbose_name = 'Social Media App'
        verbose_name_plural = 'Social Media Apps'


# ----------------About Page Model----------------#

class AboutPageModel(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField()
    profession = models.CharField(max_length=50)
    image_on_the_left = CloudinaryField('image')
    text_above_bio = models.TextField()
    text_below_bio = models.TextField()

    text_for_smile = models.CharField(max_length=20, null=True, blank=True)
    number_for_smile = models.IntegerField(null=True, blank=True)

    text_for_notebook = models.CharField(max_length=20, null=True, blank=True)
    number_for_notebook = models.IntegerField(null=True, blank=True)

    text_for_headphones = models.CharField(max_length=20,null=True, blank=True)
    number_for_headphones = models.IntegerField(null=True, blank=True)

    text_for_people = models.CharField(max_length=20,null=True, blank=True)
    number_for_people = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'HomePageModel.name'

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'


class BiographyModel(models.Model):
    title = models.CharField(max_length=15)
    text = models.CharField(max_length=25)
    person = models.ForeignKey(AboutPageModel, on_delete=models.CASCADE, related_name='biography_infos')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Biography Info'
        verbose_name_plural = 'Biography Infos'


class SkillsModel(models.Model):
    skill = models.CharField(max_length=15)
    max_number_skill = models.IntegerField()
    personal_number_skill = models.IntegerField()
    is_percent = models.BooleanField(default=True)
    person = models.ForeignKey(AboutPageModel, on_delete=models.CASCADE, related_name='skills')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class InterestsModel(models.Model):
    name = models.CharField(max_length=35)
    person = models.ForeignKey(AboutPageModel, on_delete=models.CASCADE, related_name='interests')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Interest'
        verbose_name_plural = 'Interests'


class TestimonialsModel(models.Model):
    name = models.CharField(max_length=25, null=True)
    profession_or_relation = models.CharField(max_length=125)
    image = CloudinaryField('image', blank=True, null=True)  # Remove default here
    text = models.TextField(null=True)
    should_show = models.BooleanField(default=True)
    person = models.ForeignKey(AboutPageModel, on_delete=models.CASCADE, related_name='testimonials')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.image:  # If no image is uploaded, assign the default manually
            self.image = "about-testimonials-default"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'







