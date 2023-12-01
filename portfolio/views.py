from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "portfolio/global/home.html")

def sobre(resquest):
    return render(resquest, "portfolio/global/sobre.html")

def portfolio(resquest):
    return render(resquest, "portfolio/global/portfolio.html")

def contato(resquest):
    return render(resquest, "portfolio/global/contato.html")




    
