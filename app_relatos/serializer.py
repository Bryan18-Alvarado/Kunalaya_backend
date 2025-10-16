from django.db.models import Avg
from rest_framework import serializers
from core.models import Rating, Comment, Media
from .models import Story
from core.serializer import UserSerializer, LocalizationSerializer, CategorySerializer, CommentSerializer
from core.utils.firebase_storage import upload_to_firebase
from django.contrib.contenttypes.models import ContentType

class MediaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Media
    fields = '__all__'

class StorySerializer(serializers.ModelSerializer):
  category = CategorySerializer()
  author = UserSerializer()
  localization = LocalizationSerializer()
  
  comment = serializers.SerializerMethodField()
  rating = serializers.SerializerMethodField()
  multimedia = MediaSerializer(many = True, read_only = True)
  
  files = serializers.ListField(
    child=serializers.FileField(),
    write_only=True,
    required=False
    )
  file_types = serializers.ListField(
    child=serializers.CharField(),
    write_only=True,
    required=False
    )
  
  class Meta:
    model = Story
    fields = ['id', 'category', 'title', 'content', 'author', 'publication_date', 'localization', 'comment', 'rating', 'multimedia', 'files', 'file_types', 'created_at', 'updated_at']
    read_only_fields = ['id', 'created_at', 'multimedia']
    
  def create(self, validated_data):
    files = validated_data.pop('files', [])
    file_types = validated_data.pop('file_types')
    
    story = Story.objects.create(**validated_data)
    content_type = ContentType.objects.get_for_model(Story)
    
    for index, file_obj in enumerate(files):
      tipo = file_types[index] if index < len(file_types) else 'image'
      url = upload_to_firebase(file_obj, file_obj.name)
      
      Media.objects.create (
        file_url = url,
        file_type = tipo,
        content_type = content_type,
        object_id = story.id
      )
    
    return story

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