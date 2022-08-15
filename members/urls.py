from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from django.views.generic import RedirectView

from . import views
from .views import PasswordChangeView

urlpatterns = [

    path('register/', views.register_request, name="register"),
    path('login/', views.login_request, name='login'),
    path("logout", views.logout_request, name="logout"),

    # path("password/", auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path("password/", PasswordChangeView.as_view(template_name='registration/password/change-password.html'),
         name="change_password"),
    path('password_success', views.password_success, name="password_success"),
    # Password reset stuff
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="registration/password/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password/password_reset_complete.html'),
         name='password_reset_complete'),

    path('profile/', views.profile, name='profile'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico'))),
    path('users/', views.user_details, name='users'),
    path('profile_detail/<int:pk>/', views.profile_detail, name='profile_detail'),


]
