from rest_framework import viewsets, status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializer import StorySerializer
from .models import Story
from core.models import Category, Localizations, Media
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.utils.firebase_storage import upload_to_firebase
from django.contrib.contenttypes.models import ContentType

# Create your views here.

class StoryListView(viewsets.ModelViewSet):
  serializer_class = StorySerializer
  queryset = Story.objects.all()
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def CreateStoryView(request):
  data = request.data.copy()
  data['user'] = request.user.id
  
  serializer = StorySerializer(data = data, context = {'request': request})
  
  if serializer.is_valid():
    story = serializer.save()
    return Response(StorySerializer(story, context = {'request': request}).data, status = status.HTTP_201_CREATED)

@login_required
def story_form(request):
  # categories = Category.objects.all()
  localizations = Localizations.objects.all()
  
  if request.method == "POST":
    title = request.POST.get("title")
    content = request.POST.get("content")
    localization_id = request.POST.get("localization")
    files = request.FILES.getlist("files")
    
    category = Category.objects.get(slug = "relato")
    localization = Localizations.objects.get(id=localization_id)
    
    story = Story.objects.create(
      title=title,
      content=content,
      category=category,
      localization=localization,
      author=request.user
    )
    
    content_type = ContentType.objects.get_for_model(Story)
    for file in files:
      url = upload_to_firebase(file, file.name)
      Media.objects.create(
        file_url=url,
        file_type=file.content_type.split("/")[0],
        content_type=content_type,
        object_id=story.id
      )

    return render(request, "relatos/success.html", {"story": story})

  return render(request, "relatos/story_form.html", {
    "localizations": localizations
    })