from django.urls import path
from home.views import *


urlpatterns = [
    path('', monthlystatistic, name='news_url'),


]


