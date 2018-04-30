from django.urls import path
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('userpage/', views.userpage, name='userpage'),
    path('login/', login, name='login'),
    path('logout/', views.logout, name='logout'),
]
