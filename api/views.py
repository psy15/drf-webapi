from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins
from django.http import Http404
from rest_framework import status


class TaskView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TaskSerializer

    def get(self, request, format='json'):
        snippets = Task.objects.all().order_by('id')
        serializer = TaskSerializer(snippets, many=True)
        return Response(serializer.data)


class TaskDetail(GenericAPIView):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = TaskSerializer

    def get(self, request, format='json', *args, **kwargs):
        snippet = self.kwargs.get('pk')
        tasks = Task.objects.get(id=snippet)
        serializer = TaskSerializer(tasks, many=False)
        return Response(serializer.data)


class TaskCreate(GenericAPIView):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = TaskSerializer

    def post(self, request, format='json'):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskUpdate(GenericAPIView):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = TaskSerializer

    def post(self, request, format='json', *args, **kwargs):
        snippet = self.kwargs.get('pk')
        task_ins = Task.objects.get(id=snippet)
        serializer = TaskSerializer(instance=task_ins, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class TaskDelete(GenericAPIView):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = TaskSerializer

    def delete(self, request, format='json', *args, **kwargs):
        snippet = self.kwargs.get('pk')
        task_ins = Task.objects.get(id=snippet)
        task_ins.delete()
        return Response("item successfully deleted")
