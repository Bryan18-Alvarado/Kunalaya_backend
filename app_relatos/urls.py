from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register(r'relatos', views.StoryListView, 'relatos')

urlpatterns = [
  path('api/v1/', include(router.urls)),
  path('api/v1/stories/', views.CreateStoryView, name = 'create_story'),
  path('form/story/', views.story_form, name='story_form'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)