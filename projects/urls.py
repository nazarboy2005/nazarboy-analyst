from django.urls import path
from .views import ProjectsView, ProjectDetailsView


app_name = 'projects'

urlpatterns = [
    path('', ProjectsView.as_view(), name='page'),
    path('details/<int:id>/', ProjectDetailsView.as_view(), name='details'),
]