from django.urls import path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from app_nback_visual import views


urlpatterns = [
    # 2-back task
    path('2/', views.index_2back, name="app_2back_visual_index"),
    path('2/card/', views.card_2back, name="app_2back_visual_card"),
    
    
    path('3/', views.index_3back, name="app_3back_visual_index"),
    path('4/', views.index_4back, name="app_4back_visual_index"),
]

urlpatterns += staticfiles_urlpatterns()