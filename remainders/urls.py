from django.urls import path
from . import views

urlpatterns = [
    path('', views.remainders_view, name='remainders'),
]
