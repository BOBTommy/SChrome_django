from RESTSChrome.models import User,ImageBook,Image,ImageText
from RESTSChrome.serializers import UserSerializer,ImageBookSerializer,ImageSerializer,ImageTextSerializer
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
class UserListView(generics.ListCreateAPIView):
    model = User
    serializer_class = UserSerializer

@csrf_exempt
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer

@csrf_exempt
class ImageBookListView(generics.ListCreateAPIView):
    model = ImageBook
    serializer_class = ImageBookSerializer

@csrf_exempt
class ImageBookDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = ImageBook
    serializer_class = ImageBookSerializer

@csrf_exempt
class ImageListView(generics.ListCreateAPIView):
    model = Image
    serializer_class = ImageSerializer

@csrf_exempt
class ImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = Image
    serializer_class = ImageSerializer

@csrf_exempt
class ImageTextListView(generics.ListCreateAPIView):
    model = ImageText
    serializer_class = ImageTextSerializer

@csrf_exempt
class ImageTextDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = ImageText
    serializer_class = ImageTextSerializer