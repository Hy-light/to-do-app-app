from django.urls import path

from . import views

urlpatterns = [
    # Your API endpoints here
    path('', views.TodoList.as_view()),
    path('<todo_id>/', views.TodoOne.as_view(), name='todo_one'),
]
