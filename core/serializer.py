from rest_framework import serializers
from .models import CustomUser, Localizations, Category, Comment

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ['id', 'username', 'first_name', 'last_name', 'email']
    
class LocalizationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Localizations
    fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'
    
class CommentSerializer(serializers.ModelSerializer):
  user = UserSerializer()

  class Meta:
    model = Comment
    fields = ['id', 'user', 'content', 'created_at']