from django.views.generic import TemplateView
from .models import CertificationsModel, CategoriesModel, BioModel
from home.models import SocialMediaModel

class CertificationsView(TemplateView):
    template_name = 'certifications.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = CertificationsModel.objects.filter(category__to_display=True)
        context['data'] = data
        context['social_media_apps'] = SocialMediaModel.objects.all()
        context['categories'] = CategoriesModel.objects.all()
        context['bio'] = BioModel.objects.first().bio


        return context


class CertificationDetailsView(TemplateView):
    template_name = 'certification-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        certificate_id = self.kwargs.get('id')
        data = CertificationsModel.objects.filter(id=certificate_id).first()
        context['data'] = data
        context['social_media_apps'] = SocialMediaModel.objects.all()
        context['bio'] = BioModel.objects.first().bio

        return context