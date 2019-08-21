from django.views.generic import FormView, TemplateView, RedirectView,ListView
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .models import Test, Solution
from .forms import SolutionForm, TestForm, SolutionUpdateForm
from django.contrib.auth.models import User


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
    template_name = "tests/tests.html"
    model = Test
    form_class = TestForm

    def get_context_data(self,**kwargs):
        context = super(TestList, self).get_context_data(**kwargs)
        row = len(context['object_list'])
        context['count'] = [str(i) for i in range(row)]
        print(context)
        return context

class SolutionList(ListView):
    template_name = "solutions/solution.html"
    model = Solution
    form_class = SolutionForm

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_dev=self.request.user)

class SolutionEdit(UpdateView):
    template_name = "solutions/update_solution.html"
    model = Solution
    form_class = SolutionUpdateForm
    success_url = reverse_lazy('viewlist')

class SolutionCreate(CreateView):
    model = Solution
    template_name = "solutions/create_solution.html"
    success_url = reverse_lazy('viewlist')
    form_class = SolutionForm


    # def get_initial(self, *args, **kwargs):
    #     initial = super(SolutionCreate, self).get_initial()
    #     initial['user_dev'] = self.request.user
    #     print(initial)
    #     return initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_dev = self.request.user
        self.object.save()
        return super(SolutionCreate, self).form_valid(form)
