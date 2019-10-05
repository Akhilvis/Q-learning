

from django.contrib import admin
from django.urls import path, include
from gameapp.views import *

urlpatterns = [
    path('', home),
    # path('game/', include('app_urls')),

]
