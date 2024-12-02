from food.views import *
from django.urls import path

urlpatterns =[
    path('food/',food,name='food'),
    path('nonveg/',nonveg,name='nonveg'),
]