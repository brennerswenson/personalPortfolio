from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomePage(TemplateView):
    template_name = 'index.html'


class Resume(TemplateView):
    template_name = 'resume.html'

class ReferencesView(TemplateView):
    template_name = 'references.html'
