from django.urls import path
from support import views
from support.views import SupportHTMxTableView
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('htmx/', SupportHTMxTableView.as_view(), name='support_htmx'),
    path('networking/', views.networking, name="networking"),
    path('workshop/', views.workshop, name='workshop'),
    path('register/', views.register_request, name="register"),
    path('login/', views.login_request, name='login'),
    path("logout", views.logout_request, name="logout"),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path('<int:id>/generatePDF/', views.generatePDF, name='generatePDF'),
]
