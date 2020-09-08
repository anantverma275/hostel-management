from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path to homepage sign in
    path('', views.land, name="land"),
    path('login', views.login_req, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('redisplay', views.redisplay, name="redisplay"),
    path('leave', views.leave, name="leave"),
    path('apply_leave', views.apply_leave, name="apply_leave"),
    path('leave_req', views.leave_req, name="leave_req"),
    path('complaint', views.complaint, name="complaint"),
    path('complaint_req', views.complaint_req, name="complaint_req"),
    path('notice_stud', views.notice_stud, name="notice_stud"),
    path('profilechange', views.profile_change, name="profilechange"),
    path('occupant', views.occupant, name="occupant"),
    path('logout/', auth_views.LogoutView.as_view(template_name="login.html"), name='logout'),
    # admin paths
    path('login_admin', views.login_req_admin, name="login_admin"),
    path('register_page', views.register_page, name="register_page"),
    path('dashboard_admin', views.dashboard_admin, name="dashboard_admin"),
    path('redisplay_admin', views.redisplay, name="redisplay"),
    path('leave_admin', views.leave_admin, name="leave_admin"),
    path('complaint_admin', views.complaint_admin, name="complaint_admin"),
    path('occupant_admin', views.occupant_admin, name="occupant_admin"),
    path('notice_admin_page', views.notice_admin_page, name="notice_admin_page"),
    path('notice_admin_add', views.notice_admin_add, name="notice_admin_add"),
]
