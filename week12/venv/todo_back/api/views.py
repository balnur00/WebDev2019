import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import TaskList, Task
from api.serializers import TaskListSerializer, TaskSerializer


@csrf_exempt
def tasks_list(request):
    if request.method == 'GET':
        tasks = TaskList.objects.all()
        serializer = TaskListSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = TaskListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors)


@csrf_exempt
def tasks_detail(request, pk):
    try:
        task = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    if request.method == 'GET':
        serializer = TaskListSerializer(task)
        return JsonResponse(serializer.data, status=200)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = TaskListSerializer(instance=task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse({}, status=204)


def list_of_tasks(request, pk):
    try:
        task = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    tasks = task.task_set.all()
    json_tasks = [t.to_json() for t in tasks]
    return JsonResponse(json_tasks, safe=False)
#
# @csrf_exempt
# def list_of_tasks(request, pk):
#     try:
#         task = TaskList.objects.get(id=pk)
#     except TaskList.DoesNotExist as e:
#         return JsonResponse({'error': str(e)}, safe=False)
#
#     if request.method == 'GET':
#         serializer = TaskSerializer(task)
#         return JsonResponse(serializer.data, status=200)
#     elif request.method == 'PUT':
#         data = json.loads(request.body)
#         serializer = TaskSerializer(instance=task, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors)
#     elif request.method == 'DELETE':
#         task.delete()
#         return JsonResponse({}, status=204)
