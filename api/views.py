from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers 

class GetAllPosts(generics.ListAPIView):
    queryset = models.Objava.objects.all()
    serializer_class = serializers.ObjavaSerializer

class GetPostDetial(generics.RetrieveAPIView):
    serializer_class = serializers.ObjavaSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('pk')
        return models.Objava.objects.get(pk = post_id)
