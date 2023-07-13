from django.urls import path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from app_nback_visual import views


urlpatterns = [
    # 2-back task
    path('2/', views.index_2back, name="app_2back_visual_index"),
    path('2/page/', views.page_2back, name="app_2back_visual_page"),
    re_path(r'2/(?P<code>[a-zA-Z0-9]+)/$', views.page, name="app_2back_visual_page"),
    
    
    path('3/', views.index_3back, name="app_3back_visual_index"),
    path('4/', views.index_4back, name="app_4back_visual_index"),
]

urlpatterns += staticfiles_urlpatterns()