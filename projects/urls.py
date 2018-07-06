from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.ProjectsView.as_view(), name='projects'),
    path('optimizer', views.PortfolioOptimizerView.as_view(), name='optimizer'),
    path('PDFencrypter', views.PDFEncrypterView.as_view(), name='encrypter'),
    path('ebay', views.EbayView.as_view(), name='ebay'),
    path('tesla', views.TeslaView.as_view(), name='tesla'),
    path('blackstone', views.BlackStoneView.as_view(), name='blackstone'),
    path('marketwrap', views.MarketWrapView.as_view(), name='marketwrap'),
    path('holdback', views.HoldbackView.as_view(), name='holdback'),

]
