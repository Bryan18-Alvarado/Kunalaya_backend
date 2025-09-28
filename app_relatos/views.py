from rest_framework import viewsets
from .serializer import StorySerializer
from .models import Story
from django.http import HttpResponse

# Create your views here.

class StoryListView(viewsets.ModelViewSet):
  serializer_class = StorySerializer
  queryset = Story.objects.all()

def home(request):
  return HttpResponse("Hello World")