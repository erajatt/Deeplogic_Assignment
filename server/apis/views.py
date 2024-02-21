from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def sample_api(request):
    if request.method == "GET":
        return JsonResponse({
            "message": "some-data"
        })
    
def sample_api_2(request):
    if request.method =="GET":
        return JsonResponse({
            "message": "login-successful"
        })
    
