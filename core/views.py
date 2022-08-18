from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio/portfolio.html')

def portfolio_detail(request):
    return render(request, 'portfolio/portfolio-detail.html')
