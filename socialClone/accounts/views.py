from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView
from . import forms
from django.urls import reverse_lazy

# Create your views here.

class index(TemplateView):
    template_name = 'index.html'


class signup(CreateView):
    template_name = 'accounts/signup.html'
    form_class = forms.signupForm
