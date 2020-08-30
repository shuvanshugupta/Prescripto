from django.urls import path
from . import views

urlpatterns = [
    path('',views.start,name='start'),
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('appoint/',views.appoint,name='appoint'),
    path('appointlist/',views.appointlist,name='appointlist'),
]