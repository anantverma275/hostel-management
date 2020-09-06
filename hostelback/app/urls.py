from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.signin, name = "signin"),
    # path('verify', views.verify, name="verify"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('leave', views.leave, name="leave"),
    path('apply_leave', views.apply_leave, name="apply_leave"),
    path('complaint', views.complaint, name="complaint"),
    path('profilechange', views.profile_change, name="profilechange"),
    path('register', views.register, name="register"),
    path('logout/', auth_views.LogoutView.as_view(template_name="login.html"), name='logout'),
]


