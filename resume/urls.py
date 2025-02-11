from django.urls import path
from resume.views import ResumeView

app_name = 'resume'

urlpatterns = [
    path('', ResumeView.as_view(), name='page'),
]
