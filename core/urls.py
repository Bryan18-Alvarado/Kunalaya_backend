from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'comentarios', views.CommentListView, 'comentarios')

urlpatterns = [
  path('', views.home),
  path('api/v1/', include(router.urls))
]