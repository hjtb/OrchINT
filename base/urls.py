from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('channel/<str:key>/', views.channel, name="channel"),
]
