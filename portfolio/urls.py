from django.urls import path
from portfolio.views import home, sobre, portfolio, contato
urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('portfolio/', portfolio),
    path('contato/', contato),
    
]