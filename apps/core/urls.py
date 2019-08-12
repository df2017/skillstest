from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name= 'login'),
    path('logout/', views.LogoutView.as_view(), name= 'logout'),
    path('home/', login_required(views.HomeView.as_view()), name= 'home'),
]