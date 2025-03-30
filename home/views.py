from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from home.models import Article
from . forms import ArticleForm, ArticleUpdateForm


# Home Page View Based On classes
class HomePageView(ListView):
    model = Article
    template_name = 'home/home.html'


# Show article detail
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'home/detail.html'


# Add a new article
class AddArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'home/add_article.html'
    ordering = ['-id']

# Update(edit) the article
class UpdateArticleView(UpdateView):
    model = Article
    form_class = ArticleUpdateForm
    # update_url_name = 'update'
    template_name = 'home/update_article.html'


class DeleteArticleView(DeleteView):
    model = Article
    success_url = reverse_lazy('home')
    template_name = 'home/delete_article.html'
