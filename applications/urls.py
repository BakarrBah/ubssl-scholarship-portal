# applications/urls.py
from django.urls import path
from .views import apply

app_name = "applications"

urlpatterns = [
    path("", apply, name="home"),
    path("apply/", apply, name="apply"),
]
