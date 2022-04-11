
from django.urls import include, path

from rest_framework import routers

from . import views

urlpatterns = [

    path('emp/', views.emp_list),
    path('emp/<int:pk>/', views.emp_detail),


]
