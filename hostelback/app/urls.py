from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name = "signin"),
    path('verify', views.verify, name="verify"),
    path('dashboard', views.dashboard, name="dashboard")
]
