from django.contrib import admin
from projects.models import ProjectModel, CategoryModel, ProjectImageModel, ProjectInformationModel, SkillsAppliedModel, BioModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'to_display', 'created_at']


class ProjectImageModelInline(admin.StackedInline):
    model = ProjectImageModel
    extra = 1


class ProjectInformationModelInline(admin.StackedInline):
    model = ProjectInformationModel
    extra = 1


class SkillsAppliedModelInline(admin.StackedInline):
    model = SkillsAppliedModel
    extra = 1

@admin.register(ProjectModel)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    inlines = [ProjectImageModelInline, ProjectInformationModelInline, SkillsAppliedModelInline]


@admin.register(BioModel)
class BioModelAdmin(admin.ModelAdmin):
    list_display = ['bio']