from django.shortcuts import render
from django.views.generic import TemplateView
from resume.models import SummaryModel, ResumePageModel
from home.models import SocialMediaModel


class ResumeView(TemplateView):
    template_name = 'resume.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        resume_data = ResumePageModel.objects.first()
        summary = SummaryModel.objects.all()
        if summary:
            summary = summary.first()

        social_media_apps = SocialMediaModel.objects.all()
        context['social_media_apps'] = social_media_apps
        context['resume_data'] = resume_data
        context['summary'] = summary

        return context
