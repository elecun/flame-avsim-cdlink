from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.shortcuts import redirect


def index(request):
    return render(request, "html/index.html")

def back2(request):
    return render(request, "html/n2_back.html")