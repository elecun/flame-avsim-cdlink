from django.urls import path
from app_cdlink import views


urlpatterns = [
    path('', views.index, name="index"),
]