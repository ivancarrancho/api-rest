from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from app.serializers import UserSerializer
from app.serializers import GroupSerializer
from app.serializers import BookSerializer
from app.serializers import AuthorSerializer
from models import Book
from models import Author
# Create your views here.
#
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
