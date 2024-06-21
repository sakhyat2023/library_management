from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout

# Create your views here.
class UserRegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy("home")
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
    
class UserLoginView(LoginView):
    template_name = "login.html"
    
    def get_success_url(self):
        return reverse_lazy("home")
