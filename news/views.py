from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic.base import ContextMixin, TemplateResponseMixin
from .models import Articles
from .forms import ArticlesForm, AuthUserForm, RegUserForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView,  TemplateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import User, authenticate
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(TemplateView):
    template_name = 'main/index.html'


class Page(ListView):
    model = Articles
    template_name = 'news/news_home.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        kwargs['news'] = Articles.objects.all()
        return super().get_context_data(**kwargs)


class NewsDetailView(LoginRequiredMixin, DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model = Articles
    template_name = 'news/news_update.html'

    form_class = ArticlesForm


class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = Articles
    success_url = reverse_lazy('news_home')
    template_name = 'news/news_delete.html'


class TestWebLoginViews(LoginView):
    template_name = 'news/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('login_page')

    def get_success_url(self):
        return self.success_url


class RegUserView(CreateView):
    model = User
    template_name = 'news/register.html'
    form_class = RegUserForm
    success_url = reverse_lazy('register_page')
    success_msg = 'Пользователь успешно создан'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid


class UserLogout(LogoutView):
    next_page = reverse_lazy('login_page')


class NewsCreateArticles(LoginRequiredMixin, CreateView):
    model = Articles
    template_name = 'news/create.html'
    success_url = reverse_lazy('news_home')
    form_class = ArticlesForm


