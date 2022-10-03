from rest_framework.response import Response
from .models import profile
from .serializers import profileserializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class ImageuploadModelViewSet(viewsets.ModelViewSet):
  queryset = profile.objects.all()
  serializer_class = profileserializer

  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]


