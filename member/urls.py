from django.urls import path
from member.views import LoginPage, LogoutView
from . import views 

urlpatterns = [
    path('login', LoginPage.as_view(), name='login'),
    path('register', views.signup_page, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]