from django.urls import path
from . import views
from .views import add_usage, dashboard

app_name = 'electricity'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-usage/', add_usage, name='add_usage'),
    path('usage-info/<int:usage_id>/', views.usage_info, name='usage_info'),
    path('dashboard/', dashboard, name='dashboard'),
]