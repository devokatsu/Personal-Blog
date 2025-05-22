from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import View
from . import forms
from django.conf import settings



class LoginPage(View):
    form_class = forms.LoginForm
    template_name = "member/login.html"

    def get(self, request):
        form = self.form_class()
        message = ""
        return render(request, self.template_name, context={"form": form, "message": message})

    def post(self, request):
        form = self.form_class(request.POST)
        message = ""
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Login failed!'
                
        return render(request, self.template_name, context={'form': form, 'message': message})



def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'member/signup.html', context={'form': form})
   
        
  

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')