"""web_cdlink URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_cdlink.urls')),
    path('app/nback/visual/', include('app_nback_visual.urls')),
    path('app/nback/auditory/', include('app_nback_auditory.urls')),
    path('app/stroop/visual/', include('app_stroop_visual.urls')),
    path('app/stroop/auditory/', include('app_stroop_auditory.urls')),
    path('app/surt/', include('app_surt.urls')),
]

urlpatterns += staticfiles_urlpatterns()