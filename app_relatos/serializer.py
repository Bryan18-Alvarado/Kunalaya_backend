from django.db.models import Avg
from rest_framework import serializers
from core.models import Rating, Comment
from .models import Story
from core.serializer import UserSerializer, LocalizationSerializer, CategorySerializer, CommentSerializer

class StorySerializer(serializers.ModelSerializer):
  category = CategorySerializer()
  author = UserSerializer()
  localization = LocalizationSerializer()
  
  comment = serializers.SerializerMethodField()
  rating = serializers.SerializerMethodField()
  
  class Meta:
    model = Story
    fields = ['id', 'category', 'title', 'content', 'author', 'publication_date', 'localization', 'comment', 'rating', 'created_at', 'updated_at']
  
  #Add the comment already filtered
  def get_comment(self, obj):
    qs = Comment.objects.filter(
        category__slug=obj.category.slug, post_id=obj.id
    )
    return CommentSerializer(qs, many=True).data
  
  #Add rating already average
  def get_rating(self, obj):
    return Rating.objects.filter(
      category__slug = "relato", post_id = obj.id
    ).aggregate(rating = Avg("score"))["rating"]