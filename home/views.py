from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from home.models import Article
from . forms import ArticleForm

class HomePageView(ListView):
    model = Article
    template_name = 'home/home.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'home/detail.html'

class AddArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'home/add_article.html'
