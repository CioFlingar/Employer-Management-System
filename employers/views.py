from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Employer
from .serializers import EmployerSerializer
from .permissions import IsOwner

class EmployerCreateListView(generics.ListCreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class EmployerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    permission_classes = [IsAuthenticated, IsOwner]