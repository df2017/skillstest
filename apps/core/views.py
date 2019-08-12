from django.views.generic import FormView, TemplateView, RedirectView
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,UpdateView,DetailView
from .models import Test, Solution
from django.shortcuts import render
from .forms import SolutionForm

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "login/login.html"
    success_url = '/home/'

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

class LogoutView(RedirectView):
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(self.login_url)

class HomeView(TemplateView):
    template_name = 'home/home.html'


class TestList(ListView):
    model = Test
    template_name = "tests/tests.html"
    success_url = '/test/'

class SolucionDetail(ListView):
    model = Solution
    template_name = "tests/solucion.html"


class SolucionCreate(CreateView):
    model = Solution
    template_name = "tests/tests.html"
    success_url = reverse_lazy('test')
    form_class = SolutionForm

    def form_valid(self, form):
        form.save()
        return super(SolucionCreate, self).form_valid(form)







