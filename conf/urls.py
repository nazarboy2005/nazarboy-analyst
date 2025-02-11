"""
URL configuration for conf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from conf.views import handler404

urlpatterns = [
    path('admin-nazarboy-change-everything/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('resume/', include('resume.urls', namespace='resume')),
    path('certifications/', include('certifications.urls', namespace='certifications')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('contact/', include('contact.urls', namespace='contact')),
]

handler404 = 'conf.views.handler404'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
