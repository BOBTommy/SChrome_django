from RESTSChrome.models import User,ImageBook,Image,ImageText,Files
from RESTSChrome.serializers import UserSerializer,ImageBookSerializer,ImageSerializer,ImageTextSerializer,FilesSerializer
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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

@api_view(['POST','GET'])
def upload_serializers(request):
    if request.method == 'POST':
        serializer = FilesSerializer(data=request.DATA, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(data=request.DATA, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        files = Files.objects.all()
        serializer = FilesSerializer(files)
        return Response(serializer.data)