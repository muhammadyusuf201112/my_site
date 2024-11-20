from django.shortcuts import render
from django.views.generic import ListView

from .models import User
# Create your views here.

# def home(request):
#     return render(request, 'index.html')

class List_View(ListView):
    model = User
    template_name = 'index.html'
    context_object_name = 'user'