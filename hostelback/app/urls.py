from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name = "signin"),
    path('verify', views.verify, name="verify"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('leave', views.leave, name="leave"),
    path('complaint', views.complaint, name="complaint"),
    path('admin/register', views.register, name="register")
]
