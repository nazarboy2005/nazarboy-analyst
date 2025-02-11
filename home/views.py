from django.shortcuts import render
from django.views.generic import TemplateView
from home.models import HomePageModel, AboutPageModel, SocialMediaModel


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = HomePageModel.objects.first()
        context['name'] = data.name
        context['titles'] = data.titles.all()
        context['first_title'] = context['titles'][0] if context['titles'] else "No one"
        context['quote'] = data.quote
        context['image'] = data.image
        context['social_media_apps'] = SocialMediaModel.objects.all()

        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = AboutPageModel.objects.first()
        biography_infos = data.biography_infos.all()
        if biography_infos:
            context['biography_infos_left'] = biography_infos[:(len(biography_infos) + 1) // 2]
            context['biography_infos_right'] = biography_infos[(len(biography_infos) + 1) // 2:]

        skills = data.skills.all()
        if skills:
            context['skills_left'] = skills[:(len(skills) + 1) // 2]
            context['skills_right'] = skills[(len(skills) + 1) // 2:]

        social_media_apps = SocialMediaModel.objects.all()
        context['social_media_apps'] = social_media_apps

        context['data'] = data
        return context
