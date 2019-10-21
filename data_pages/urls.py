from django.urls import path
from . import views

app_name = 'data_pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('collect/', views.collect_form, name='collect_form'),
    path('collect/result', views.collect_result, name='collect_result'),
    path('analysis/', views.analysis_form, name='analysis_form'),
    path('analysis/result', views.analysis_result, name='analysis_result'),
]
