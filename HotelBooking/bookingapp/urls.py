from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("booking/<int:id>", views.addbooking, name="booking"),
]

