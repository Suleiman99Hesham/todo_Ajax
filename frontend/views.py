from django.shortcuts import render

import frontend

# Create your views here.

def list(request):
    return render(request, 'frontend/list.html')