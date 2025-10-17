from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
import logging

from .serializer import CommentSerializer, UserSerializer
from .models import Comment, CustomUser

# Create your views here.
class CommentListView(viewsets.ModelViewSet):
  serializer_class = CommentSerializer
  queryset = Comment.objects.all()

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
  try:
    # Require email (not username) for login.
    email = (request.data.get('email') or '').strip()
    password = request.data.get('password')

    if not email or not password:
      return Response({"error": "Email y contraseña son requeridos"}, status=status.HTTP_400_BAD_REQUEST)

    if '@' not in email:
      return Response({"error": "Se requiere un correo electrónico válido"}, status=status.HTTP_400_BAD_REQUEST)

    try:
      user = CustomUser.objects.filter(email__iexact=email).first()
    except Exception:
      logging.exception('Error looking up user by email')
      user = None

    if not user or not user.check_password(password):
      return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)

    return Response({
      "token": token.key,
      "user": serializer.data
    }, status=status.HTTP_200_OK)
  except Exception as e:
    logging.exception("Error in login view")
    return Response({"error": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
  serializer = UserSerializer(data=request.data)
  
  if serializer.is_valid():
    serializer.save()
    
    user = CustomUser.objects.get(username=serializer.data['email'])
    user.set_password(serializer.data['password'])
    user.save()
    
    token = Token.objects.create(user=user)
    return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
  serializer = UserSerializer(instance = request.user)
  return Response(serializer.data, status=status.HTTP_200_OK)

def home(request):
  return HttpResponse('Home, hello there')