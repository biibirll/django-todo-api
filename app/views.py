from rest_framework import generics

from .models import Task
from .serializers import TaskListSerializer, TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return TaskSerializer
    
        return TaskListSerializer

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer