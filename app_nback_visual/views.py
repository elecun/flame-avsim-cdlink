from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.shortcuts import redirect


# 2-back task index page
def index_2back(request):
    return render(request, "html/index_2back.html")
def card_2back(request):
    return render(request, "html/card_2back.html")

# 3-back task index page
def index_3back(request):
    return render(request, "html/index_3back.html")

# 4-back task index page
def index_4back(request):
    return render(request, "html/index_4back.html")

