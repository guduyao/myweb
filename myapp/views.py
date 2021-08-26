from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Users


# Create your views here.
def index(request):
    return render(request, 'all.html')