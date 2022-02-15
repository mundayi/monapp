"""pollster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from .import settings
from django.contrib.staticfiles import views
from django.conf.urls.static import static
from django.urls.resolvers import URLPattern
from django.urls import re_path
from polls.models import Choice
from g3 import models
from g3 import urls


urlpatterns = [
    path('', include('accueil.urls')),
    path('g3/', include('g3.urls')),
    path('pages/', include('pages.urls')),
    path('polls/', include('polls.urls')), 
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
