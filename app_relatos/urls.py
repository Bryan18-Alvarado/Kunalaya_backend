from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register(r'stories', views.StoryListView, 'stories')

urlpatterns = [
  path('', views.home),
  path("api/v1/", include(router.urls))
]
