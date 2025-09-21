from django.db import models
from core.models import BaseModel, CustomUser, Localizations, Category, Comment


# Create your models here.

class Story(BaseModel):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  content = models.TextField()
  author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="stories")
  publication_date = models.DateTimeField(auto_now_add=True)
  localization = models.ForeignKey(Localizations, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title
  
class MultimediaStoryFiles(models.Model):
  type_file = [
    ("image", "Image"),
    ("audio", "Audio"),
    ("video", "Video"),
    ("document", "Document"),
  ]
  
  story = models.ForeignKey(Story, on_delete=models.CASCADE)
  types = models.CharField(max_length=20, choices=type_file)
  files = models.FileField(upload_to="stories/")
  
  def __str__(self):
    return f"{self.types} - {self.files.url}"