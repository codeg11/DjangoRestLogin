# api/serializers.py
from rest_framework import serializers
from . import models

from django.contrib.auth.models import User

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = models.Todo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User