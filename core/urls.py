from django.urls import path
from .views import (
    home,
    about,
    contact,
    portfolio,
    portfolio_detail,
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('portfolio/', portfolio, name='portfolio'),
    path('portfolio-detail/', portfolio_detail, name='portfolio-detail'),
]