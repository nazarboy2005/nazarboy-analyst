from django.contrib import admin

from .models import SummaryModel, EducationsModel, ExperiencesModel, SummarySmallInfosModel, ResumePageModel


class SummarySmallInfosInline(admin.StackedInline):
    model = SummarySmallInfosModel
    extra = 1
    max_num = 5


@admin.register(SummaryModel)  # Summary Section
class SummaryModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    inlines = [SummarySmallInfosInline]



class EducationsInline(admin.StackedInline):  # Educations Section
    model = EducationsModel
    extra = 1


class ExperiencesInline(admin.StackedInline):  # Experiences Section
    model = ExperiencesModel
    extra = 1


@admin.register(ResumePageModel)
class ResumePageModelAdmin(admin.ModelAdmin):
    list_display = ['short_intro', 'created_at']
    inlines = [EducationsInline, ExperiencesInline]

    def short_intro(self, obj):
        return obj.intro[:50]
