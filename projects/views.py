from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class ProjectsView(TemplateView):
    template_name = 'projects.html'


class PortfolioOptimizerView(TemplateView):
    template_name = 'portfolioOptimizer.html'


class PDFEncrypterView(TemplateView):
    template_name = 'pdfEncrypter.html'


class EbayView(TemplateView):
    template_name = 'eBay.html'


class TeslaView(TemplateView):
    template_name = 'tesla.html'


class BlackStoneView(TemplateView):
    template_name = 'blackstone.html'


class MarketWrapView(TemplateView):
    template_name = 'marketwrap.html'

class HoldbackView(TemplateView):
    template_name = 'holdback.html'
