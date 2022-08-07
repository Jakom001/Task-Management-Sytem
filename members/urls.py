from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView
from django.urls import path

from . import views
from .views import PasswordChangeView

urlpatterns = [
    path('register/', views.register_request, name="register"),
    path('login/', views.login_request, name='login'),
    path("logout", views.logout_request, name="logout"),
    # path("password/", auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path("password/", PasswordChangeView.as_view(template_name='registration/change-password.html'),
         name="change_password"),
    path("reset_password/", PasswordResetView.as_view(template_name='registration/password_reset.html'),
         name="reset_password"),
    path('password_reset_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password_success', views.password_success, name="password_success"),
    path('profile/', views.profile, name='profile'),
    path('profile_update/', views.profile_update, name='profile_update'),
    # path('password-reset/',
    #      'django.contrib.auth.views.password_reset',
    #      {'post_reset_redirect': '/user/password/reset/done/',
    #       'html_email_template_name': 'registration/password_reset_email.html',
    #       'password_reset_form': CustomEmailValidationOnForgotPassword},
    #      name="password_reset"),

]
