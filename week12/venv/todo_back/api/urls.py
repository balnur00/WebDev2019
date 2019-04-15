from django.urls import path
from api import views

urlpatterns = [
    path('tasklist/', views.tasks_list),
    path('tasklist/<int:pk>/', views.tasks_detail),
    path('tasklist/<int:pk>/task', views.list_of_tasks)
]