from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse(f"Main page. Request: {request}")


def about(request):
    return HttpResponse("Testing Django. Otus Basic. Implementation of Store app.")
