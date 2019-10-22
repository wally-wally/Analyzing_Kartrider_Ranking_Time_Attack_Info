from django.urls import path
from . import views

app_name = 'data_pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('collect/', views.collect_form, name='collect_form'),
    path('collect/result', views.collect_result, name='collect_result'),
    path('collect/backtocollectmenu', views.back_collect_menu, name='back_collect_menu'),
    path('analysis/', views.analysis_form, name='analysis_form'),
    path('analysis/result', views.analysis_result, name='analysis_result'),
    path('analysis/backtoanalysismenu', views.back_analysis_menu, name='back_analysis_menu'),
    path('storage/', views.storage_index, name='storage_index'),
    path('storage/<int:datapage_pk>', views.storage_detail, name='storage_detail'),
    path('storage/<int:datapage_pk>/delete', views.storage_delete, name='storage_delete'),
]
