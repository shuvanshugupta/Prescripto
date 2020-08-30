from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf.urls import url

urlpatterns = [
    path('logout',views.logout,name='logout'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
]