from django.shortcuts import render
import requests
from django.conf import settings
from .models import Portfolio


def Home(request):
    template_name = "index.html"
    # portfolios = Portfolio.objects.all()
    # context = {'portfolios': portfolios}
    response = requests.get("http://127.0.0.1:8000/api/portfolio/")

    if response.status_code == 200:
        context = {
            "portfolios": response.json(),
        }
    else:
        context = {
            "portfolios": {},
            "error": "Bad response!"}


    return render(request, template_name, context)

def PortfolioDetail(request, pk):
    
    template_name = "detail.html"
    
    detail = Portfolio.objects.filter(pk=pk).first()

    context = {
        'detail': detail
    }

    return render (request, template_name, context)