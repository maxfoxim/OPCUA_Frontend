from django.urls import path
from . import views

urlpatterns = [
    path('Frontend/', views.Frontend, name='Frontend'),
]
