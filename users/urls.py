from django.urls import path

from core.urls import urlpatterns
from .views import (
    profile,
    register,
)
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
]