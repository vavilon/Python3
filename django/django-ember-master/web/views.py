from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Registration
from .serializers import RegistrationSerializer

class RegistrationViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Registration.objects.all()
        serializer = RegistrationSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
