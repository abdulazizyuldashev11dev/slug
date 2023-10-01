from django.shortcuts import get_object_or_404
from .models import NewsModel
from rest_framework import generics
from .serializers import NewsSerializer

class AppListApiView(generics.ListAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer