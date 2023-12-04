# todo_app/urls.py
from django.urls import path
from .views import (
    TodoCreateView, TodoListView,
    TodoUpdateView, TodoRetrieveView, TodoDestroyView
)


urlpatterns = [
    # List and Create operations
    path('create/', TodoCreateView.as_view(), name='todo-create'),
    path('list/', TodoListView.as_view(), name='to-do-list'),
    path('update/<int:pk>/', TodoUpdateView.as_view(), name='todo-update'),
    path('delete/<int:pk>/', TodoDestroyView.as_view(), name='todo-destroy'),  # Fixed the name here
    path('read/<int:pk>/', TodoRetrieveView.as_view(), name='todo-retrieve'),
]
