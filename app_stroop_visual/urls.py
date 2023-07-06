from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from app_stroop_visual import views



urlpatterns = [
    path('', views.index, name="app_stroop_visual_index"),
]
urlpatterns += staticfiles_urlpatterns()