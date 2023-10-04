from rest_framework import serializers
from .models import Users, LessonStatus, Products

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['name']

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonStatus
        fields = ['status', "durationViewed", "lastViewed"]

class ProductStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id']
