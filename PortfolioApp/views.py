from django.shortcuts import render, get_object_or_404
from .models import Portfolio


# Create your views here.
def allportfolio(request):
    AllPortfolio = Portfolio.objects.all()
    return render(request, 'PortfolioApp/allportfolio.html', {'AllPortfolio': AllPortfolio})


def portfoliodetail(request, Portfolio_id):
    PortfolioDetail = get_object_or_404(Portfolio, pk=Portfolio_id)
    return render(request, 'PortfolioApp/Detail.html', {'PortfolioDetail': PortfolioDetail})
