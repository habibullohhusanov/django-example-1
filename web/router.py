from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('dashboard', dashboard, name="dashboard")
]