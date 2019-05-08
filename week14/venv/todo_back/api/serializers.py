from rest_framework import serializers
from api.models import TaskList, Task
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


# class TaskListSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=True)
#
#     def create(self, validated_data):
#         list = TaskList(**validated_data)
#         list.save()
#         return list
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.save()
#         return instance


class TaskListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = TaskList
        fields = ('__all__')


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    task_list_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'created_at', 'due_on', 'status', 'task_list_id')


class TaskListSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_by = UserSerializer(read_only=True)
    tasks = serializers.StringRelatedField(many=True)

    class Meta:
        model = TaskList
        fields = ('__all__')

