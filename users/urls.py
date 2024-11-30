from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'users'

urlpatterns = [
    #path("login/", views.CustomLoginView.as_view(), name='login'),
    path("signup/", views.signup, name="signup"), 
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),
]