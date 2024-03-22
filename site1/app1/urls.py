from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.nhapbn, name="nhapbn"),
    path('/savebn/',views.savebn, name="savebn"),
    path('/hienbn/',views.hien, name="hienbn")
]