from django.shortcuts import render


def home(request):
    return render(request,"view.html")

def home1(request):
    return render(request,"bs1.html")