"""practicalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dima.views import *
from roma.views import show_roma
from nastya.views import show_nastya
from prohor.views import *
from german.views import show_german
from maxim.views import show_max
from nazar.views import *
from kyrylo.views import show_kyrylo
from pasha.views import Show_Pashok
from vlad.views import show_vlad
from sergey.views import show_sergey
from danya.views import show_danya
from artem.views import *




urlpatterns = [
    path('admin/', admin.site.urls),
    path('dima/',DimaView),
    path('roma/',show_roma),
    path('nazar/', show_nazar),
    path('nastya/',show_nastya),
    path('Pashok/', Show_Pashok),
    path('prohor/',show_prohor),
    path('maxim/', show_max),
    path('vlad/', show_vlad),
    path('german/',show_german),
    path('kyrylo/',show_kyrylo),
    path('danya/', show_danya),
    path('sergey/',show_sergey),
    path("artem/",show_artem)
]
