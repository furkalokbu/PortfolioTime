from django.shortcuts import render
import requests
from django.conf import settings
from .models import Portfolio


def home(request):
    template_name = "index.html"
    # portfolios = Portfolio.objects.all()
    # context = {'portfolios': portfolios}
    response = requests.get("http://127.0.0.1:8000/api/portfolio/")

    print(settings.STATIC_ROOT)

    if response.status_code == 200:
        context = {
            "portfolios": response.json(),
        }
    else:
        context = {"error": "Bad response!"}


    return render(request, template_name, context)
