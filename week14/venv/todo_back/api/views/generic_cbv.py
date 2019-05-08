from api.serializers import TaskListSerializer, TaskSerializer, UserSerializer,TaskListSerializer2
from api.models import Task, TaskList
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from api.filters import TaskFilter

class TaskLists(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        print(type(self.request.auth))
        return TaskList.objects.filter(created_by=self.request.user)
    # queryset = TaskList.objects.all()
    # serializer_class = TaskListSerializer

    def get_serializer_class(self):
        return TaskListSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskListDetail(generics.RetrieveUpdateAPIView):
    queryset = TaskList.objects.all() #whyyyyyyyyyy
    serializer_class = TaskListSerializer2
    permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     return TaskList.objects.get(id=self.kwargs['pk'])
# filter(self.request.user).


class TaskList_task(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_queryset(self):
        try:
            task_list = TaskList.objects.get(id=self.kwargs['pk'])
        except TaskList.DoesNotExist:
            raise Http404
        return task_list.tasks.all()

    # TODO DjangoFilterBackend
    # filterset_fields = ('name', 'price',)

    filter_class = TaskFilter

    # TODO SearchFilter
    search_fields = ('name', 'status')

    # TODO OrderingFilter
    ordering_fields = ('name')
    ordering = ('price',)