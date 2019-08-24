from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('collect_info/', views.collect_info),
    path('collect_situation/', views.collect_situation),
    path('analysis_info/', views.analysis_info),
    path('analysis_data/', views.analysis_data),
]