from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from app_relatos.models import Story, MultimediaStoryFiles
from .models import CustomUser, Localizations, Category, Comment

# Register your models here.

class CustomUserAdmin(UserAdmin):
  add_form = CustomUserCreationForm
  form = CustomUserChangeForm
  models = CustomUser
  list_display = [
    "email",
    "username",
    "is_staff",
    "is_active",
  ]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Story)
admin.site.register(MultimediaStoryFiles)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Localizations)