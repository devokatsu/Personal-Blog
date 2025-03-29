from django.shortcuts import render
from django.views.generic import ListView

from home.models import Article


class HomePageView(ListView):
    model = Article
    template_name = 'home/home.html'
