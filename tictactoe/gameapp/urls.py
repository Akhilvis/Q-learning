

from django.contrib import admin
from django.urls import path, include
from gameapp.views import *

urlpatterns = [
    path('', home),
    path('init/', first_random_step),
    path('take_move/', take_policy_step),

]
