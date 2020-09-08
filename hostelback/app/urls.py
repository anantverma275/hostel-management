from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.land, name="land"),
    path('login', views.login_req, name="login"),
    path('admin/login', views.login_admin_req, name="login_admin_req"),
    path('dashboard', views.dashboard, name="dashboard"),
    # path('admin/dashboard', views.admin_dashboard, name="admin_dashboard"),
    # path('admin/occupants', views.admin_dashboard, name="admin_dashboard"),
    path('leave', views.leave, name="leave"),
    path('leave_req', views.leave_req, name="leave_req"),
    path('complaint', views.complaint, name="complaint"),
    path('complaint_req', views.complaint_req, name="complaint_req"),
    path('notice_stud', views.notice_stud, name="notice_stud"),
    path('profilechange', views.profile_change, name="profilechange"),
    path('register', views.register, name="register"),
    path('logout', auth_views.LogoutView.as_view(template_name="login_stud.html"), name='logout'),
]
