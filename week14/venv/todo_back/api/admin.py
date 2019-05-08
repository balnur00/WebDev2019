from django.contrib import admin
from api.models import Task, TaskList


admin.site.register(Task)


@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by')