from django.db import models
from datetime import timedelta
from django.contrib.auth.models import User


class TaskList(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=2)




class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    due_on = models.DateTimeField(null=True) #created_at + timedelta(days=7)
    status = models.CharField(max_length=200)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')

