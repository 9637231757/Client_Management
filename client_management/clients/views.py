from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # When a client is created, associate it with the logged-in user
        serializer.save(created_by=self.request.user)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Associate the project with the logged-in user
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        # Return projects that are assigned to the logged-in user
        return Project.objects.filter(users=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        Custom create method for handling project creation, including user assignment.
        """
        client_id = request.data.get('client_id')
        users = request.data.get('users', [])
        
        # Check if client_id is provided
        if not client_id:
            return Response({"detail": "Client ID is required."}, status=400)

        # Check if users are provided
        if not users:
            return Response({"detail": "At least one user is required."}, status=400)

        # Fetch client instance
        client = Client.objects.filter(id=client_id).first()
        if not client:
            return Response({"detail": "Client not found."}, status=404)

        # Fetch user instances
        user_instances = User.objects.filter(id__in=users)
        if not user_instances.exists():
            return Response({"detail": "One or more users not found."}, status=404)

        # Create the project and assign users
        project_data = {
            'project_name': request.data.get('project_name'),
            'client': client,
            'users': user_instances
        }

        serializer = ProjectSerializer(data=project_data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
