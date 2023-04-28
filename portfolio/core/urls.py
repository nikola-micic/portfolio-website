from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>/', views.detail, name="detail"),
    path('contact/', views.contact, name="contact"),
    path('contact/success/', views.success, name="success"),
    path('download-cv/', views.download_cv, name="download"),
]