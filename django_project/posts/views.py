from django.shortcuts import render
from django.views.generic import ListView
from .models import post
# Create your views here.


class Home(ListView):
    model=post
    template_name='home.html'