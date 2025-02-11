from django.contrib import admin
from .models import HomePageModel, SocialMediaModel, TitleModel, InterestsModel, AboutPageModel, SkillsModel, \
    BiographyModel, TestimonialsModel


# ----------------Home Page Admin----------------#
class SocialMediaModelAdmin(admin.StackedInline):
    model = SocialMediaModel
    extra = 1


class TitleModelAdmin(admin.StackedInline):
    model = TitleModel
    extra = 1


@admin.register(HomePageModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    inlines = [SocialMediaModelAdmin, TitleModelAdmin]


# ----------------About Page Admin----------------#
class BiographyModelAdmin(admin.StackedInline):
    model = BiographyModel
    extra = 1


class SkillsModelAdmin(admin.TabularInline):
    model = SkillsModel
    extra = 1


class InterestsModelAdmin(admin.StackedInline):
    model = InterestsModel
    extra = 1


class TestimonialsModelAdmin(admin.StackedInline):
    model = TestimonialsModel
    extra = 1



@admin.register(AboutPageModel)
class AboutPageModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    inlines = [BiographyModelAdmin, SkillsModelAdmin, InterestsModelAdmin, TestimonialsModelAdmin]


# ----------------Resume Page Admin----------------#

