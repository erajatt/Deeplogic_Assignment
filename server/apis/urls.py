from django.urls import path, include
from .views import * 

api_endpoints = [
    path("sample-api-endpoint", sample_api),
    path("sample-api-2", sample_api_2)
]