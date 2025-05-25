from django.urls import path
from .views import HomePageView, ArticleDetailView, AddArticleView, UpdateArticleView, DeleteArticleView, SearchView

# app_name = 'home'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('add/', AddArticleView.as_view(), name='add_article'),
    path('article/edit/<int:pk>', UpdateArticleView.as_view(), name='update_article'),
    path('article/<int:pk>/remove', DeleteArticleView.as_view(), name='delete_article'),
    path('search/', SearchView.as_view(), name='search'),
]