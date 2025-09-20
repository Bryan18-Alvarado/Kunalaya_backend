from django.db import models
from django.contrib.auth.models import AbstractUser

#Base models for the other models
class BaseModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    abstract = True

#Custom user registration and update for all posts
class CustomUser(AbstractUser):
  pass

  def __str__(self):
    return self.username

class Category(models.Model):
  name = models.CharField(max_length=100, unique=True)
  slug = models.SlugField(unique=True)
  
  def __str__(self):
    return self.name
  
class Comment(BaseModel):
  user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  post_id = models.PositiveIntegerField()
  content = models.TextField()
  
  def __str__(self):
    return f"Comment of {self.user} in {self.category} -- Post {self.post_id}"
  
#coords for histories, cultural events and more
class Localizations(models.Model):
  name = models.CharField(max_length=100)
  coords = models.CharField(max_length=300)

  def __str__(self):
    return self.name