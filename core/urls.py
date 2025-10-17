from django.urls import path, include, re_path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'comentarios', views.CommentListView, 'comentarios')

urlpatterns = [
  path('', views.home),
  path('api/v1/', include(router.urls)),
  path('login/', views.login),
  path('register/', views.register),
  path('profile/', views.profile),
]