from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_invoice, name='upload_invoice'),
    path('', views.index, name='index'),
]
