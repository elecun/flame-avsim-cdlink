from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from app_nback_visual import views


urlpatterns = [
    path('', views.index, name="app_nback_visual_index"),
    path('2back/', views.back2, name="app_nback_visual_2back"),
]

urlpatterns += staticfiles_urlpatterns()