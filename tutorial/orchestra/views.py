from django.shortcuts import render

from django.http import HttpResponse

# request: HttpRequest
def index(request):
    return HttpResponse("Orchestra says hello!")