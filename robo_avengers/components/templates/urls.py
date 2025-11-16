from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This means: when someone visits /components/, show the home view
]