from django.urls import path
from . import views

urlpatterns = [
    path('summernote/', views.summernote, name='summernote'),
    path('', views.index, name='index'),


]