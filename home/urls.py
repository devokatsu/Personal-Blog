from django.urls import path
from .views import HomePageView, ArticleDetailView, AddArticleView, UpdateArticleView

# app_name = 'home'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('add/', AddArticleView.as_view(), name='add_article'),
    path('update/<int:pk>', UpdateArticleView.as_view(), name='update_article'),
]