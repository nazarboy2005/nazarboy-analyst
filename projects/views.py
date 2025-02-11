from django.shortcuts import render
from django.views.generic import TemplateView
from projects.models import ProjectModel, CategoryModel, BioModel
from home.models import SocialMediaModel


class ProjectsView(TemplateView):
    template_name = 'projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = ProjectModel.objects.filter(category__to_display=True).distinct().order_by('-created_at')
        context['data'] = data
        context['bio'] = BioModel.objects.first().bio
        social_media_apps = SocialMediaModel.objects.all()
        context['social_media_apps'] = social_media_apps
        return context


class ProjectDetailsView(TemplateView):
    template_name = 'project-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        project_id = self.kwargs.get('id')
        project = ProjectModel.objects.get(id=project_id)
        context['project'] = project
        context['bio'] = BioModel.objects.first().bio
        context['social_media_apps'] = SocialMediaModel.objects.all()
        context['categories'] = CategoryModel.objects.filter(to_display=True)
        return context
