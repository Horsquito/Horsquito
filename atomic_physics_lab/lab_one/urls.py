from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path ('', views.home_page, name = 'home_url' ),
    path ('energy', Energy.as_view(), name = 'energy_url' ),
    path ('current', Current.as_view(), name = 'current_url' ),
    path ('collision_probability', CollisionProbability.as_view(), name = 'collision_probability_url' ),
]
