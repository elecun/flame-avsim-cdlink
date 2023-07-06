from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from app_surt import views


urlpatterns = [
    path('', views.index, name="app_surt_index"),
]
urlpatterns += staticfiles_urlpatterns()