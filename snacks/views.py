from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView): # we imported 'from django.views.generic import TemplateView' to fix as_view no module
    template_name = 'home.html' # from inside template folder ... then we will go to settings.py to Templates in DIR = [we import os first then put os.path.join(BASE_DIR, 'templates']

class AboutView(TemplateView):
    template_name = 'about.html'
