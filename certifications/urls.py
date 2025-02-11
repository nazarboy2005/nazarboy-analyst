from django.urls import path
from .views import CertificationsView, CertificationDetailsView


app_name = 'certifications'

urlpatterns = [
    path('', CertificationsView.as_view(), name='page'),
    path('details/<int:id>/', CertificationDetailsView.as_view(), name='details'),
]