from django.urls import path

from support import views

urlpatterns = [
    path('networking/', views.networking, name="networking"),
    path('index/', views.index, name='index'),
    path('workshop/', views.workshop, name='workshop'),
    path('register/', views.register_request, name="register"),
    path('login/', views.login_request, name='login'),
    path("logout", views.logout_request, name="logout"),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path('add_task', views.add_task, name='add_task'),
    path('edit', views.Edit, name='edit'),
    path('task_text', views.task_text, name='task_text'),
    path('task_csv', views.task_csv, name='task_csv'),
    path('task_pdf', views.task_pdf, name='task_pdf'),

]
