from django.urls import path
from . import views

urlpatterns = [
    path('', views.remainders, name='remainders'),
]
