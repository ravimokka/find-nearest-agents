from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    path('', csrf_exempt(LoadHomePage.as_view()), name="LoadHomePage"),
    path('api/places', csrf_exempt(fetchAllPlace.as_view()), name="fetchAllPlace"),
    path('api/findAgents', csrf_exempt(findNearestAgents.as_view()), name="findNearestAgents"),

]