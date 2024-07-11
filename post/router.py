from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="posts"),
    path('<int:id>', show, name="posts_show")
]