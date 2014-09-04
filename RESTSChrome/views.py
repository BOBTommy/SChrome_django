from RESTSChrome.models import User,ImageBook,Image,ImageText
from RESTSChrome.serializers import UserSerializer,ImageBookSerializer,ImageSerializer,ImageTextSerializer
from rest_framework import generics

class UserListView(generics.ListCreateAPIView):
    model = User
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer

class ImageBookListView(generics.ListCreateAPIView):
    model = ImageBook
    serializer_class = ImageBookSerializer

class ImageBookDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = ImageBook
    serializer_class = ImageBookSerializer

class ImageListView(generics.ListCreateAPIView):
    model = Image
    serializer_class = ImageSerializer

class ImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = Image
    serializer_class = ImageSerializer

class ImageTextListView(generics.ListCreateAPIView):
    model = ImageText
    serializer_class = ImageTextSerializer

class ImageTextDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = ImageText
    serializer_class = ImageTextSerializer