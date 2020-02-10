from django.shortcuts import render, HttpResponse
from testapp.models import CustomUser

# Create your views here.
def home(request):
    
    return render(request, "stwn/index.html", {})