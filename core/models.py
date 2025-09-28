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

# 4 Categories in total (stories, library, cultural_evente and games)
class Category(models.Model):
  name = models.CharField(max_length=100, unique=True)
  slug = models.SlugField(unique=True)

  def __str__(self):
    return self.name

#Common comments for all the publications
class Comment(BaseModel):
  user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  post_id = models.PositiveIntegerField()
  content = models.TextField()
  
  def __str__(self):
    return f"Comment of {self.user} in {self.category} -- Post {self.post_id}"
  
class Rating(BaseModel):
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  post_id = models.PositiveIntegerField()
  score = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range (1, 6)])
  
  class Meta:
    unique_together = ('user', 'category', 'post_id')
    ordering = ['-created_at']
    
  def __str__(self):
    return f"{self.user} cualify {self.category} (post {self.post_id} with {self.score})"
  

#coords for histories, cultural events and more
class Localizations(models.Model):
  name = models.CharField(max_length=100)
  coords = models.CharField(max_length=300)

  def __str__(self):
    return self.name