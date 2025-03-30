from django.urls import path
from . views import HomePageView, ArticleDetailView

app_name = 'home'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
]