from django.urls import path
from api.views import old_view
from api.views import fbv
from api import views

# urlpatterns = [
#     path('tasklist/', old_view.tasks_list),
#     path('tasklist/<int:pk>/', old_view.tasks_detail),
#     path('tasklist/<int:pk>/task/', old_view.list_of_tasks),
#     # path('tasklist/<int:pk>/task/<int:pk/>', views.list_of_tasks)
# ]

# urlpatterns = [
#     path('tasklist/', fbv.show_taskLists),
#     path('tasklist/<int:pk>/', fbv.show_current_taskList),
#     path('tasklist/<int:pk>/task/', fbv.show_current_tasks)
# ]

urlpatterns = [
    path('tasklist/', views.TaskLists.as_view()),
    path('tasklist/<int:pk>/', views.TaskListDetail.as_view()),
    path('tasklist/<int:pk>/task/', views.TaskList_task.as_view()),
    path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout)
]