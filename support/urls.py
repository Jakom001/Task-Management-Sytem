from django.urls import path

from . import views

urlpatterns = [
    path('new_task/', views.new_task, name="new_task"),
    path('index/', views.index, name='index'),
    path('workshop/', views.workshop, name='workshop'),
    path('add_task', views.add_task, name='add_task'),
    path('task_text', views.task_text, name='task_text'),
    # path('task_excel', views.task_excel, name='task_excel'),
    path('task_csv', views.task_csv, name='task_csv'),
    path('task_pdf', views.task_pdf, name='task_pdf'),
    path('delete/<str:id>', views.Delete, name='delete'),
    path('update/<int:pk>', views.Update, name='update'),
    path('support/<int:id>/', views.support_detail, name='detail'),
    path('assigned_tasks/', views.assigned_tasks, name='assigned_tasks'),


]
