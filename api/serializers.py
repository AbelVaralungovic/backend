from rest_framework import serializers
from . import models

class ObjavaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Objava
        fields = '__all__'