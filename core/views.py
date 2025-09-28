from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializer import CommentSerializer
from .models import Comment

# Create your views here.
class CommentListView(viewsets.ModelViewSet):
  serializer_class = CommentSerializer
  queryset = Comment.objects.all()

def home(request):
  return HttpResponse('Home, hello there')