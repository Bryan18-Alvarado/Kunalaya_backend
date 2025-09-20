from rest_framework import serializers
from .models import Story
from core.serializer import UserSerializer, LocalizationSerializer, Category

class StorySerializer(serializers.ModelSerializer):
  category = Category()
  author = UserSerializer()
  localization = LocalizationSerializer()
  
  class Meta:
    model = Story
    fields = ['id', 'category', 'title', 'content', 'author', 'publication_date', 'localization', 'created_at', 'updated_at']