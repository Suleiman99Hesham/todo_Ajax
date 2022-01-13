from django.shortcuts import render
from django.http import JsonResponse
from api.models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

# Create your views here.

@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'List' : '/task_list/',
        'Detail-View' : '/task-detail/<str:pk>/',
        'Create' : '/task_create/',
        'Update' : '/task-update/<str:pk>/',
        'Delete' : '/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('completed', '-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    deserializer = TaskSerializer(data=request.data)
    if deserializer.is_valid():
        deserializer.save()
    return Response(deserializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    deserializer = TaskSerializer(instance=task,data=request.data)
    if deserializer.is_valid():
        deserializer.save()
    return Response(deserializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item Successfully Deleted!")
