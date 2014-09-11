from RESTSChrome.models import User,ImageBook,Image,ImageText,Files,Base64Image
from RESTSChrome.serializers import UserSerializer,ImageBookSerializer,ImageSerializer,ImageTextSerializer,FilesSerializer
from RESTSChrome.serializers import Base64ImageSerializer
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import base64
from django.core.files.base import ContentFile

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

class Base64ListView(generics.ListCreateAPIView):
    model = Base64Image
    serializer_class = Base64ImageSerializer

class Base64DetailView(generics.RetrieveDestroyAPIView):
    model = Base64Image
    serializer_class = Base64ImageSerializer

@api_view(['POST','GET'])
def upload_serializers(request):
    if request.method == 'POST':
        #img_file = base64.b64decode(request.DATA['img_file'])
        img_file = ContentFile(base64.b64decode(request.DATA['img_file'])
                               , name=request.DATA['title'] + "png")
        serializer = FilesSerializer(data=request.DATA, files=img_file)
        if serializer.is_valid():
            serializer.save()
            return Response(data=request.DATA, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        files = Files.objects.all()
        serializer = FilesSerializer(files)
        return Response(serializer.data)

@api_view(['GET','POST'])
def upload_form(request):
    if request.method == 'POST':
        instance = Files(img_file=request.FILES['img_file'], title=request.DATA['title'])
        instance.save()
        return Response('uploaded')

    elif request.method == 'GET':
        files = Files.objects.all()
        serializer = FilesSerializer(files)
        return Response(serializer.data)

@api_view(['POST','GET'])
def upload_files(request):
     if request.method == 'POST':
        serializer = FilesSerializer(data=request.DATA, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(data=request.DATA, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)