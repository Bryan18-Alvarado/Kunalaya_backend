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

#coords for histories, cultural events and more
class Localizations(models.Model):
  name = models.CharField(max_length=100)
  coords = models.CharField(max_length=300)

  def __str__(self):
    return self.name