from django.urls import path
from . import views

urlpatterns = [
    path('', views.Todo.as_view(), name='todo'),
    path('task/<pk>/update', views.TaskUpdate.as_view(), name='task-update'),
    path('task/<pk>/update-status', views.task_update_status, name='task-update-status'),
    path('task/<pk>/delete', views.TaskDelete.as_view(), name='task-delete'),
]