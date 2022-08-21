from django.shortcuts import render
from .models import Project


def home(request):
    context = {
        'projects': Project.objects.all()
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    context = {
        'projects': Project.objects.all()
    }
    return render(request, 'portfolio/portfolio.html', context)


def portfolio_detail(request, id=1):
    context = {
        'project': Project.objects.get(id=id)
    }
    return render(request, 'portfolio/portfolio-detail.html', context)
