from django.urls import path
from . import views

urlpatterns = [
    path("", views.infotinder, name="infotinder"),
]
