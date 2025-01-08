from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status

from .models import Todo
from .serializer import TodoSerializer


# Create your views here.
class TodoList(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            todo_item = serializer.save()
            todo_item.completed = False
            todo_item.url = reverse('todo_one', args=[todo_item.id], request=request)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request):
        Todo.objects.all().delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class TodoOne(APIView):
    def get(self, request, todo_id):
        try:
            todo = Todo.objects.get(pk=todo_id)
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Todo.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
    
    def patch(self, request, todo_id):
        try:
            todo = Todo.objects.get(pk=todo_id)
            serializer = TodoSerializer(data=request.data, instance=todo, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Todo.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, todo_id):
        try:
            Todo.objects.get(pk=todo_id).delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Todo.DoesNotExist:
            return Response(status=204)


